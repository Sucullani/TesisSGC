# -*- coding: utf-8 -*-
"""Lectura, aplanado y transformación de la fuente LaTeX de la tesis.

El objetivo es producir un único archivo LaTeX «sencillo» que pandoc pueda
leer sin perder información.  Todo lo que pandoc no entiende (macros propias,
tipos de columna de tabularx, numeración de títulos, \\ref, figuras TikZ,
\\includepdf, notas APA, etc.) se resuelve aquí.  La información que pandoc no
puede transportar hasta el .docx (anchos de columna, números de ecuación,
marcadores para el índice...) viaja como «marcadores» de texto ⟦...⟧ que el
posproceso con python-docx interpreta y elimina.

Este módulo NO escribe nada dentro de 05_Tesis_LaTeX ni de 06_...: solo lee.
"""

import re
from pathlib import Path

ANCHO_UTIL_CM = 16.51          # 21,59 cm - 2 x 2,54 cm
ERRORES = []                   # problemas no fatales de la transformación (se informan al final)
ALTO_UTIL_CM = 22.86           # 27,94 cm - 2 x 2,54 cm

# --------------------------------------------------------------------------
#  Utilidades de análisis de texto LaTeX
# --------------------------------------------------------------------------

def es_inicio_comando(s, pos):
    """True si la barra invertida en s[pos] inicia un comando (no está escapada)."""
    n = 0
    j = pos - 1
    while j >= 0 and s[j] == '\\':
        n += 1
        j -= 1
    return n % 2 == 0


def saltar_blancos(s, i, permitir_parrafo=False):
    """Avanza sobre espacios; no cruza una línea en blanco salvo que se permita."""
    n = len(s)
    saltos = 0
    while i < n and s[i] in ' \t\r\n':
        if s[i] == '\n':
            saltos += 1
            if saltos > 1 and not permitir_parrafo:
                break
        i += 1
    return i


def leer_grupo(s, i):
    """s[i] == '{'. Devuelve (contenido, índice tras la llave de cierre)."""
    if i >= len(s) or s[i] != '{':
        raise ValueError('se esperaba "{" en la posición %d' % i)
    prof = 0
    j = i
    n = len(s)
    while j < n:
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            prof += 1
        elif c == '}':
            prof -= 1
            if prof == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError('llave sin cerrar desde la posición %d: %r' % (i, s[i:i + 60]))


def leer_opcional(s, i):
    """s[i] == '['. Devuelve (contenido, índice tras ']') respetando llaves."""
    prof = 0
    j = i + 1
    n = len(s)
    while j < n:
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            prof += 1
        elif c == '}':
            prof -= 1
        elif c == ']' and prof == 0:
            return s[i + 1:j], j + 1
        j += 1
    raise ValueError('corchete sin cerrar desde la posición %d' % i)


def leer_argumentos(s, i, n_obligatorios, n_opcionales=0, opcionales_al_inicio=True):
    """Lee argumentos tras un comando.  Devuelve (opcionales, obligatorios, fin).

    Los opcionales que no aparecen valen None.  Si falta un obligatorio se
    lanza ValueError.
    """
    opc = []
    obl = []
    if opcionales_al_inicio:
        for _ in range(n_opcionales):
            k = saltar_blancos(s, i)
            if k < len(s) and s[k] == '[':
                txt, i = leer_opcional(s, k)
                opc.append(txt)
            else:
                opc.append(None)
    for _ in range(n_obligatorios):
        k = saltar_blancos(s, i)
        if k < len(s) and s[k] == '{':
            txt, i = leer_grupo(s, k)
            obl.append(txt)
        elif k < len(s) and s[k] == '\\':
            # argumento sin llaves que es un comando: \foo\bar
            m = re.match(r'\\([A-Za-z@]+|.)', s[k:])
            obl.append(m.group(0))
            i = k + len(m.group(0))
        elif k < len(s) and s[k] not in '}':
            obl.append(s[k])
            i = k + 1
        else:
            raise ValueError('falta un argumento obligatorio en la posición %d' % i)
    return opc, obl, i


def patron_comando(nombre):
    return re.compile(r'\\' + re.escape(nombre) + r'(?![A-Za-z@])')


def buscar_comandos(s, nombre, desde=0):
    """Itera las posiciones (inicio, fin_del_nombre) de \\nombre no escapado."""
    pat = patron_comando(nombre)
    pos = desde
    while True:
        m = pat.search(s, pos)
        if not m:
            return
        if es_inicio_comando(s, m.start()):
            yield m.start(), m.end()
        pos = m.end()


def reemplazar_comando(s, nombre, funcion, n_obl=1, n_opc=0, estrella=False):
    """Sustituye cada \\nombre[opc]{obl}... por funcion(opc, obl, estrella).

    Si funcion devuelve None se conserva el texto original.
    """
    salida = []
    pos = 0
    pat = re.compile(r'\\' + re.escape(nombre) + (r'(\*?)' if estrella else r'()') + r'(?![A-Za-z@])')
    while True:
        m = pat.search(s, pos)
        if not m:
            break
        if not es_inicio_comando(s, m.start()):
            salida.append(s[pos:m.end()])
            pos = m.end()
            continue
        try:
            opc, obl, fin = leer_argumentos(s, m.end(), n_obl, n_opc)
        except ValueError:
            salida.append(s[pos:m.end()])
            pos = m.end()
            continue
        try:
            nuevo = funcion(opc, obl, bool(m.group(1)))
        except Exception as e:      # un comando mal formado no detiene la conversión
            ERRORES.append('No se pudo convertir \\%s (%s: %s); se deja sin cambios.' % (nombre, type(e).__name__, e))
            nuevo = None
        salida.append(s[pos:m.start()])
        salida.append(s[m.start():fin] if nuevo is None else nuevo)
        pos = fin
    salida.append(s[pos:])
    return ''.join(salida)


def buscar_entorno(s, nombre, desde=0):
    """Busca el primer \\begin{nombre} desde 'desde' y su \\end{nombre} pareado.

    Devuelve (ini_begin, fin_begin, ini_end, fin_end) o None.  'nombre' puede
    ser una expresión regular (grupo sin captura) como 'table\\*?'.
    """
    pat_b = re.compile(r'\\begin\{(' + nombre + r')\}')
    while True:
        m = pat_b.search(s, desde)
        if not m:
            return None
        if es_inicio_comando(s, m.start()):
            break
        desde = m.end()
    real = m.group(1)
    pat = re.compile(r'\\(begin|end)\{' + re.escape(real) + r'\}')
    prof = 0
    pos = m.start()
    while True:
        k = pat.search(s, pos)
        if not k:
            raise ValueError('entorno %s sin cerrar (posición %d)' % (real, m.start()))
        if es_inicio_comando(s, k.start()):
            if k.group(1) == 'begin':
                prof += 1
            else:
                prof -= 1
                if prof == 0:
                    return m.start(), m.end(), k.start(), k.end()
        pos = k.end()


def transformar_entornos(s, nombre, funcion):
    """Sustituye cada entorno 'nombre' (regex) por funcion(nombre_real, cuerpo, resto_tras_end).

    funcion recibe (nombre_real, cuerpo) y devuelve el texto nuevo.  Los
    entornos se procesan de izquierda a derecha; el cuerpo se pasa sin
    procesar (la función puede llamar recursivamente).
    """
    salida = []
    pos = 0
    while True:
        r = buscar_entorno(s, nombre, pos)
        if not r:
            break
        ib, fb, ie, fe = r
        real = re.match(r'\\begin\{([^}]*)\}', s[ib:fb]).group(1)
        salida.append(s[pos:ib])
        try:
            salida.append(funcion(real, s[fb:ie]))
        except Exception as e:      # un entorno mal formado no detiene la conversión
            ERRORES.append('No se pudo convertir el entorno %s (%s: %s) cerca de «%s»; se deja sin cambios.'
                           % (real, type(e).__name__, e, texto_plano(s[fb:fb + 80])))
            salida.append(s[ib:fe])
        pos = fe
    salida.append(s[pos:])
    return ''.join(salida)


def dividir_nivel_superior(s, separador):
    """Divide s por 'separador' ('\\\\' o '&') solo en el nivel superior.

    No divide dentro de llaves ni de entornos anidados.  Para '\\\\' acepta un
    argumento opcional [longitud] a continuación, que se descarta.
    """
    partes = []
    actual = []
    prof = 0
    prof_env = 0
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c == '\\':
            if s.startswith('\\begin{', i):
                prof_env += 1
            elif s.startswith('\\end{', i):
                prof_env -= 1
            if separador == '\\\\' and s.startswith('\\\\', i) and prof == 0 and prof_env == 0:
                partes.append(''.join(actual))
                actual = []
                i += 2
                # \\* y \\[longitud]
                if i < n and s[i] == '*':
                    i += 1
                k = saltar_blancos(s, i)
                if k < n and s[k] == '[':
                    try:
                        _, i = leer_opcional(s, k)
                    except ValueError:
                        pass
                continue
            actual.append(s[i:i + 2])
            i += 2
            continue
        if c == '{':
            prof += 1
        elif c == '}':
            prof -= 1
        elif c == separador and separador == '&' and prof == 0 and prof_env == 0:
            partes.append(''.join(actual))
            actual = []
            i += 1
            continue
        actual.append(c)
        i += 1
    partes.append(''.join(actual))
    return partes


def quitar_comentarios(texto):
    """Elimina comentarios % como lo hace TeX (el % consume el fin de línea)."""
    lineas = texto.split('\n')
    res = []
    for k, linea in enumerate(lineas):
        corte = None
        j = 0
        while True:
            j = linea.find('%', j)
            if j < 0:
                break
            nb = 0
            t = j - 1
            while t >= 0 and linea[t] == '\\':
                nb += 1
                t -= 1
            if nb % 2 == 0:
                corte = j
                break
            j += 1
        if corte is None:
            res.append((linea, True))
        else:
            res.append((linea[:corte], False))
    salida = []
    anterior_sin_fin = False
    for k, (linea, con_fin) in enumerate(res):
        if anterior_sin_fin:
            linea = linea.lstrip(' \t')
        if con_fin:
            salida.append(linea + ('\n' if k < len(res) - 1 else ''))
        else:
            siguiente_en_blanco = k + 1 < len(res) and res[k + 1][1] and res[k + 1][0].strip() == ''
            salida.append(linea + ('\n' if siguiente_en_blanco else ''))
        anterior_sin_fin = not con_fin
    return ''.join(salida)


def a_cm(dim, ancho_linea=ANCHO_UTIL_CM):
    """Convierte una dimensión LaTeX a centímetros (None si no se reconoce)."""
    if dim is None:
        return None
    d = dim.strip().replace(' ', '')
    m = re.fullmatch(r'([0-9]*[.,]?[0-9]*)\\(linewidth|textwidth|columnwidth|hsize)', d)
    if m:
        f = m.group(1).replace(',', '.')
        return (float(f) if f not in ('', '.') else 1.0) * ancho_linea
    m = re.fullmatch(r'([0-9]*[.,]?[0-9]+)(cm|mm|in|pt|bp|em|ex|pc)', d)
    if m:
        v = float(m.group(1).replace(',', '.'))
        u = m.group(2)
        return v * {'cm': 1.0, 'mm': 0.1, 'in': 2.54, 'pt': 2.54 / 72.27, 'bp': 2.54 / 72,
                    'em': 0.4233, 'ex': 0.19, 'pc': 12 * 2.54 / 72.27}[u]
    m = re.fullmatch(r'([0-9]*[.,]?[0-9]*)\\(textheight)', d)
    if m:
        f = m.group(1).replace(',', '.')
        return (float(f) if f not in ('', '.') else 1.0) * ALTO_UTIL_CM
    return None


def texto_plano(latex):
    """Aproximación de texto visible (para estimar anchos y para mensajes)."""
    t = latex
    t = re.sub(r'\$([^$]*)\$', lambda m: re.sub(r'\\[A-Za-z]+|[{}_^]', '', m.group(1)), t)
    t = re.sub(r'\\(textbf|textit|emph|texttt|textsc|underline|text|mbox|textsuperscript|textsubscript)\s*\{', '{', t)
    t = re.sub(r'\\textcolor\{[^}]*\}', '', t)
    t = re.sub(r'\\(multicolumn|multirow)\{[^}]*\}\{[^}]*\}', '', t)
    t = re.sub(r'\\(parencite|textcite|cite|citeauthor|citeyear)(\[[^\]]*\])*\{([^}]*)\}', r'(\3, 2025)', t)
    t = re.sub(r'\\[A-Za-z@]+\*?', ' ', t)
    t = t.replace('~', ' ').replace('{', '').replace('}', '').replace('\\', '')
    t = re.sub(r'\s+', ' ', t)
    return t.strip()


_ANCHOS_TNR = {}
for _c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÑÜ':
    _ANCHOS_TNR[_c] = 0.70
for _c in 'IJ':
    _ANCHOS_TNR[_c] = 0.38
for _c in 'MW':
    _ANCHOS_TNR[_c] = 0.92
for _c in 'abcdeghknopquvxyzáéóúñü':
    _ANCHOS_TNR[_c] = 0.50
for _c in 'fijlrstí':
    _ANCHOS_TNR[_c] = 0.31
for _c in 'mw':
    _ANCHOS_TNR[_c] = 0.75
for _c in '0123456789':
    _ANCHOS_TNR[_c] = 0.50
for _c in ' .,;:\'’!|':
    _ANCHOS_TNR[_c] = 0.26


def ancho_texto_cm(txt, pt=12.0, negrita=False):
    """Ancho aproximado de un texto en Times New Roman (anchos medios por tipo de carácter)."""
    em = sum(_ANCHOS_TNR.get(c, 0.55) for c in txt)
    if negrita:
        em *= 1.08
    return em * pt * 2.54 / 72.0


# --------------------------------------------------------------------------
#  Lectura y aplanado
# --------------------------------------------------------------------------

def proteger_verbatim(texto, almacen):
    """Sustituye entornos verbatim por marcadores ⟦VERB:n⟧ (antes de quitar comentarios)."""
    def sust(m):
        almacen.append(m.group(2))
        return '⟦VERB:%d⟧' % (len(almacen) - 1)
    return re.sub(r'\\begin\{(verbatim|Verbatim|lstlisting|minted)\}(?:\[[^\]]*\])?(?:\{[^}]*\})?(.*?)\\end\{\1\}',
                  sust, texto, flags=re.S)


class Fuente:
    """Lee tesis.tex, resuelve \\input y recoge macros y opciones."""

    def __init__(self, dir_tesis, archivo='tesis.tex', avisos=None):
        self.dir = Path(dir_tesis)
        self.archivo = archivo
        self.avisos = avisos if avisos is not None else []
        self.verbatim = []           # contenidos protegidos
        self.macros = {}             # nombre -> (n_args, defecto_opcional, cuerpo)
        self.tipos_columna = {}      # letra -> (n_args, cuerpo)
        self.nombres = {             # nombres de babel/caption (spanish, es-tabla)
            'contentsname': 'Índice', 'listtablename': 'Índice de tablas',
            'listfigurename': 'Índice de figuras', 'tablename': 'Tabla', 'figurename': 'Figura',
            'chaptername': 'Capítulo', 'appendixname': 'Apéndice', 'bibname': 'Bibliografía',
            'refname': 'Referencias', 'abstractname': 'Resumen', 'partname': 'Parte',
        }
        self.borrador = True
        self.secnumdepth = 2
        self.tocdepth = 1
        self.contadores_por_capitulo = {'table': True, 'figure': True, 'equation': True}
        self.graphicspath = []
        self.archivos_leidos = []
        self.preambulo = ''          # preámbulo de tesis.tex tal como está (para TikZ)
        self.cuerpo = ''

    # ---- archivos
    def ruta(self, nombre, ext='.tex'):
        p = (self.dir / nombre)
        if p.is_file():
            return p
        if not nombre.endswith(ext) and (self.dir / (nombre + ext)).is_file():
            return self.dir / (nombre + ext)
        return None

    def leer(self, ruta):
        texto = Path(ruta).read_text(encoding='utf-8', errors='replace')
        self.archivos_leidos.append(str(ruta))
        texto = proteger_verbatim(texto, self.verbatim)
        return quitar_comentarios(texto)

    def resolver_inclusiones(self, texto, profundidad=0):
        """Resuelve \\input, \\include, \\IfFileExists y \\VerbatimInput."""
        if profundidad > 20:
            raise RuntimeError('demasiados \\input anidados')

        def r_iffileexists(opc, obl, est):
            nombre, si, no = obl
            return si if self.ruta(nombre.strip()) else no

        anterior = None
        while anterior != texto:
            anterior = texto
            texto = reemplazar_comando(texto, 'IfFileExists', r_iffileexists, n_obl=3)

        def r_input(opc, obl, est):
            nombre = obl[0].strip()
            if '#' in nombre:          # \input dentro de la definición de una macro
                return None
            p = self.ruta(nombre)
            if not p:
                self.avisos.append('No se encontró el archivo de \\input{%s}; se omite.' % nombre)
                return ''
            return '\n' + self.resolver_inclusiones(self.leer(p), profundidad + 1) + '\n'

        texto = reemplazar_comando(texto, 'input', r_input)
        texto = reemplazar_comando(texto, 'include', lambda o, b, e: '\\clearpage' + r_input(o, b, e))

        def r_verbatiminput(opc, obl, est):
            nombre = obl[0].strip()
            p = self.ruta(nombre, ext='')
            if not p:
                self.avisos.append('No se encontró el archivo de \\VerbatimInput{%s}.' % nombre)
                return ''
            self.verbatim.append(p.read_text(encoding='utf-8', errors='replace'))
            self.archivos_leidos.append(str(p))
            return '\n\n⟦VERB:%d⟧\n\n' % (len(self.verbatim) - 1)

        texto = reemplazar_comando(texto, 'VerbatimInput', r_verbatiminput, n_obl=1, n_opc=1)
        texto = reemplazar_comando(texto, 'lstinputlisting', r_verbatiminput, n_obl=1, n_opc=1)
        return texto

    # ---- macros
    @staticmethod
    def _leer_definicion(s, i):
        """Lee {\\nombre}[n][defecto]{cuerpo} (o \\nombre sin llaves). Devuelve (nombre, n, defecto, cuerpo, fin)."""
        k = saltar_blancos(s, i)
        if k < len(s) and s[k] == '{':
            nombre, k = leer_grupo(s, k)
        else:
            m = re.match(r'\\[A-Za-z@]+|\\.|.', s[k:])
            nombre, k = m.group(0), k + len(m.group(0))
        n, defecto = 0, None
        k2 = saltar_blancos(s, k)
        if k2 < len(s) and s[k2] == '[':
            txt, k = leer_opcional(s, k2)
            n = int(txt) if txt.strip().isdigit() else 0
            k2 = saltar_blancos(s, k)
            if k2 < len(s) and s[k2] == '[':
                defecto, k = leer_opcional(s, k2)
        k2 = saltar_blancos(s, k)
        cuerpo, fin = leer_grupo(s, k2)
        return nombre.strip(), n, defecto, cuerpo, fin

    def _recoger(self, texto, comando, destino):
        salida = []
        pos = 0
        pat = re.compile(r'\\' + comando + r'\*?(?![A-Za-z@])')
        while True:
            m = pat.search(texto, pos)
            if not m:
                break
            if not es_inicio_comando(texto, m.start()):
                salida.append(texto[pos:m.end()])
                pos = m.end()
                continue
            try:
                nombre, n, defecto, cuerpo, fin = self._leer_definicion(texto, m.end())
            except (ValueError, AttributeError):
                salida.append(texto[pos:m.end()])
                pos = m.end()
                continue
            destino(nombre, n, defecto, cuerpo)
            salida.append(texto[pos:m.start()])
            pos = fin
        salida.append(texto[pos:])
        return ''.join(salida)

    def recoger_definiciones(self, texto):
        """Recoge \\newcommand/\\providecommand/\\newcolumntype y los elimina del texto."""
        def d_macro(nombre, n, defecto, cuerpo):
            if nombre.startswith('\\'):
                self.macros[nombre[1:]] = (n, defecto, cuerpo)

        def d_col(nombre, n, defecto, cuerpo):
            self.tipos_columna[nombre] = (n, cuerpo)
        for cmd in ('newcommand', 'providecommand', 'DeclareRobustCommand'):
            texto = self._recoger(texto, cmd, d_macro)
        texto = self._recoger(texto, 'newcolumntype', d_col)
        return texto

    def recoger_nombres(self, texto):
        """Nombres de índices, tablas, etc. definidos en \\addto\\captionsspanish."""
        for nombre in list(self.nombres):
            m = re.search(r'\\renewcommand\{?\\' + nombre + r'\}?\{([^{}]*)\}', texto)
            if m:
                self.nombres[nombre] = m.group(1).strip()

    def cargar(self):
        principal = self.dir / self.archivo
        texto = self.leer(principal)
        m = re.search(r'\\begin\{document\}', texto)
        if not m:
            raise RuntimeError('tesis.tex no tiene \\begin{document}')
        pre = texto[:m.start()]
        self.preambulo = re.sub(r'^.*?\\documentclass(\[[^\]]*\])?\{[^}]*\}', '', pre, count=1, flags=re.S)
        fin = re.search(r'\\end\{document\}', texto)
        cuerpo = texto[m.end():fin.start() if fin else len(texto)]

        pre = self.resolver_inclusiones(pre)
        self.recoger_nombres(pre)
        if re.search(r'\\borradorfalse', pre):
            self.borrador = False
        m2 = re.search(r'\\setcounter\{secnumdepth\}\{(-?\d+)\}', pre)
        if m2:
            self.secnumdepth = int(m2.group(1))
        m2 = re.search(r'\\setcounter\{tocdepth\}\{(-?\d+)\}', pre)
        if m2:
            self.tocdepth = int(m2.group(1))
        for c in ('table', 'figure', 'equation'):
            if re.search(r'\\counterwithout\*?\{' + c + r'\}\{chapter\}', pre):
                self.contadores_por_capitulo[c] = False
            if re.search(r'\\counterwithin\*?\{' + c + r'\}\{chapter\}', pre):
                self.contadores_por_capitulo[c] = True
        for g in re.finditer(r'\\graphicspath\{((?:\{[^}]*\})+)\}', pre):
            self.graphicspath += re.findall(r'\{([^}]*)\}', g.group(1))
        self.recoger_definiciones(pre)

        cuerpo = self.resolver_inclusiones(cuerpo)
        cuerpo = self.recoger_definiciones(cuerpo)
        if re.search(r'\\borradorfalse', cuerpo):
            self.borrador = False
        cuerpo = re.sub(r'\\borrador(true|false)', '', cuerpo)
        self.cuerpo = cuerpo
        return self


# Macros que este programa trata de forma especial (no se expanden en bloque)
MACROS_ESPECIALES = {'nota', 'pendiente', 'guia'}


def expandir_macros(texto, macros, excluir=MACROS_ESPECIALES, max_vueltas=12):
    """Expande las macros definidas por el usuario (con o sin argumentos)."""
    nombres = [n for n in macros if n not in excluir]
    if not nombres:
        return texto
    nombres.sort(key=len, reverse=True)
    pat = re.compile(r'\\(' + '|'.join(re.escape(n) for n in nombres) + r')(?![A-Za-z@])')
    for _ in range(max_vueltas):
        cambios = 0
        salida = []
        pos = 0
        for m in pat.finditer(texto):
            if m.start() < pos or not es_inicio_comando(texto, m.start()):
                continue
            n_args, defecto, cuerpo = macros[m.group(1)]
            fin = m.end()
            args = []
            try:
                if defecto is not None:
                    k = saltar_blancos(texto, fin)
                    if k < len(texto) and texto[k] == '[':
                        a, fin = leer_opcional(texto, k)
                    else:
                        a = defecto
                    args.append(a)
                    _, obl, fin = leer_argumentos(texto, fin, n_args - 1)
                    args += obl
                elif n_args:
                    _, args, fin = leer_argumentos(texto, fin, n_args)
                else:
                    # \macro{} -> se consume el grupo vacío
                    if texto.startswith('{}', fin):
                        fin += 2
            except ValueError:
                continue
            reemplazo = cuerpo
            for k, a in enumerate(args, 1):
                reemplazo = reemplazo.replace('#%d' % k, a)
            salida.append(texto[pos:m.start()])
            # \bfseries\titulotesis -> \bfseries{}DISEÑO... (no fundir nombres de comandos)
            previo = salida[-1] if salida[-1] else (salida[-2] if len(salida) > 1 else '')
            if re.search(r'\\[A-Za-z@]+$', previo) and reemplazo[:1].isalpha():
                reemplazo = '{}' + reemplazo
            # Si la expansión termina en un comando con letras y lo que sigue es una letra,
            # se protege con {} para no fundir nombres.
            if re.search(r'\\[A-Za-z@]+$', reemplazo) and fin < len(texto) and texto[fin].isalpha():
                reemplazo += '{}'
            salida.append(reemplazo)
            pos = fin
            cambios += 1
        salida.append(texto[pos:])
        texto = ''.join(salida)
        if not cambios:
            break
    return texto


def dividir_por_caracter(s, car):
    """Divide por un carácter (p. ej. ',') en el nivel superior de llaves."""
    partes, actual, prof = [], [], 0
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\':
            actual.append(s[i:i + 2])
            i += 2
            continue
        if c == '{':
            prof += 1
        elif c == '}':
            prof -= 1
        if c == car and prof == 0:
            partes.append(''.join(actual))
            actual = []
        else:
            actual.append(c)
        i += 1
    partes.append(''.join(actual))
    return partes


def a_romano(n, mayus=False):
    vals = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), (100, 'c'), (90, 'xc'),
            (50, 'l'), (40, 'xl'), (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]
    r = ''
    for v, t in vals:
        while n >= v:
            r += t
            n -= v
    return r.upper() if mayus else r


def a_letra(n, mayus=True):
    r = ''
    while n > 0:
        n, k = divmod(n - 1, 26)
        r = chr(65 + k) + r
    return r if mayus else r.lower()


ENTORNOS_ECUACION = ('equation', 'equation*', 'align', 'align*', 'gather', 'gather*', 'multline',
                     'multline*', 'eqnarray', 'eqnarray*', 'flalign', 'flalign*', 'alignat',
                     'alignat*', 'displaymath')
ENTORNOS_FLOTANTES_TABLA = ('table', 'table*', 'sidewaystable', 'sidewaystable*', 'longtable', 'longtable*', 'xltabular')
ENTORNOS_FLOTANTES_FIGURA = ('figure', 'figure*', 'sidewaysfigure', 'sidewaysfigure*')
NIVEL_SECCION = {'part': -1, 'chapter': 0, 'section': 1, 'subsection': 2, 'subsubsection': 3,
                 'paragraph': 4, 'subparagraph': 5}

EVENTO = re.compile(
    r'\\(?:'
    r'(?P<sec>chapter|section|subsection|subsubsection|paragraph|subparagraph)(?P<star>\*?)(?![A-Za-z@])'
    r'|(?P<appendix>appendix)(?![A-Za-z@])'
    r'|(?P<setc>setcounter|addtocounter)\s*\{(?P<cname>[A-Za-z]+)\}\s*\{(?P<cval>[^{}]*)\}'
    r'|(?P<renew>renewcommand)\*?\s*\{?\\the(?P<thec>[A-Za-z]+)\}?'
    r'|begin\{(?P<benv>[A-Za-z*]+)\}'
    r'|end\{(?P<eenv>[A-Za-z*]+)\}'
    r'|(?P<capof>captionof)(?P<capofstar>\*?)\s*\{(?P<capoftype>[A-Za-z]+)\}'
    r'|(?P<cap>caption)(?P<capstar>\*?)(?![A-Za-z@])'
    r'|label\s*\{(?P<label>[^{}]*)\}'
    r'|(?P<dispmath>\[)'
    r')')


class Transformador:
    """Convierte el cuerpo aplanado de la tesis en LaTeX apto para pandoc."""

    def __init__(self, fuente, graficos, avisos, etiquetas_aux=None):
        self.f = fuente
        self.g = graficos
        self.avisos = avisos
        self.aux = etiquetas_aux or {}
        self.etiquetas = {}      # etiqueta -> dict(num, tipo, titulo)
        self.tablas = []         # datos de cada tabla para el posproceso
        self.toc = []            # entradas del índice general
        self.lot = []            # índice de tablas
        self.lof = []            # índice de figuras
        self.ecuaciones = 0
        self.n_titulo = 0
        self.refs_faltantes = []
        self.duplicadas = []
        # contadores (como en LaTeX)
        self.c = {'chapter': 0, 'section': 0, 'subsection': 0, 'subsubsection': 0,
                  'paragraph': 0, 'subparagraph': 0, 'table': 0, 'figure': 0, 'equation': 0}
        self.apendice = False
        self.modo_seccion = 'chapter'   # \thesection = \thechapter.\arabic{section}
        self.ref_actual = (None, None, '')

    # ------------------------------------------------------------------
    def procesar(self):
        s = self.f.cuerpo
        for _ in range(3):
            s = expandir_macros(s, self.f.macros)
            s2 = self.f.resolver_inclusiones(s)
            s2 = self.f.recoger_definiciones(s2)
            if s2 == s:
                break
            s = s2
        s = expandir_macros(s, self.f.macros)
        s = reemplazar_comando(s, 'guia', lambda o, b, e: '', n_obl=1)
        s = reemplazar_comando(s, 'pendiente', self._pendiente, n_obl=1)
        s = self._simples(s)
        s = self._normalizar_citas(s)
        s = transformar_entornos(s, 'titlepage', self._portada)
        s = reemplazar_comando(s, 'printbibliography', self._bibliografia, n_obl=0, n_opc=1)
        s = self._envoltorios(s)
        s = self.numerar(s)
        s = transformar_entornos(s, r'(?:table|figure|sidewaystable|sidewaysfigure)\*?', self._flotante)
        s = self.transformar_tablas(s)
        s = reemplazar_comando(s, 'nota', lambda o, b, e: self._bloque_nota(b[0]), n_obl=1)
        s = self.transformar_graficos(s)
        s = self.transformar_listas(s)
        s = self._desenvolver_grupos(s)
        s = self.transformar_titulos(s)
        s = self._indices(s)
        s = self.resolver_referencias(s)
        s = self._limpiar(s)
        s = self._restaurar_verbatim(s)
        s = re.sub(r'\n{3,}', '\n\n', s)
        return s

    # ------------------------------------------------------------------
    #  Marcas de borrador y sustituciones simples
    def _pendiente(self, opc, obl, est):
        if not self.f.borrador:
            return ''
        return '\\textcolor{pendientecolor}{\\textbf{[Pendiente:} %s\\textbf{]}}' % obl[0].strip()

    def _simples(self, s):
        s = reemplazar_comando(s, 'enquote', lambda o, b, e: '«%s»' % b[0], n_obl=1, estrella=True)
        s = reemplazar_comando(s, 'texorpdfstring', lambda o, b, e: b[0], n_obl=2)
        s = reemplazar_comando(s, 'hyperref', lambda o, b, e: b[0], n_obl=1, n_opc=1)
        s = reemplazar_comando(s, 'hyperlink', lambda o, b, e: b[1], n_obl=2)
        s = reemplazar_comando(s, 'hypertarget', lambda o, b, e: b[1], n_obl=2)
        s = reemplazar_comando(s, 'foreignlanguage', lambda o, b, e: b[1], n_obl=2, n_opc=1)
        s = reemplazar_comando(s, 'ensuremath', lambda o, b, e: '$%s$' % b[0], n_obl=1)
        for nombre, valor in self.f.nombres.items():
            s = re.sub(r'\\' + nombre + r'(?![A-Za-z@])(\{\})?', lambda m, v=valor: v, s)
        # Elementos de formularios: líneas para llenar, casillas y recuadros
        def r_rule(o, b, e):
            w = a_cm(b[0])
            if w is None or w < 0.05:
                return ''
            return '\\_' * max(3, int(round(w / 0.2)))
        s = reemplazar_comando(s, 'rule', r_rule, n_obl=2, n_opc=1)
        s = re.sub(r'\\hrulefill(?![A-Za-z@])', '\\\\_' * 14, s)
        s = re.sub(r'\\dotfill(?![A-Za-z@])', '.' * 14, s)
        s = reemplazar_comando(s, 'cellcolor', lambda o, b, e: '', n_obl=1, n_opc=1)
        s = reemplazar_comando(s, 'columncolor', lambda o, b, e: '', n_obl=1, n_opc=1)

        def caja(contenido):
            limpio = re.sub(r'\\(rule|strut|vphantom|hphantom)(\[[^\]]*\])?(\{[^{}]*\})*', '', contenido).strip()
            if not limpio:
                return '☐'
            if len(texto_plano(limpio)) > 60 or re.search(r'\\par\b|\\begin\{|\n\s*\n|\\parbox', limpio):
                return '\n\n\\begin{recuadro}\n%s\n\\end{recuadro}\n\n' % limpio
            return limpio
        s = reemplazar_comando(s, 'fcolorbox', lambda o, b, e: caja(b[2]), n_obl=3, n_opc=1)
        s = reemplazar_comando(s, 'colorbox', lambda o, b, e: b[1], n_obl=2, n_opc=1)
        s = reemplazar_comando(s, 'fbox', lambda o, b, e: caja(b[0]), n_obl=1)
        s = reemplazar_comando(s, 'framebox', lambda o, b, e: caja(b[0]), n_obl=1, n_opc=2)
        s = reemplazar_comando(s, 'mbox', lambda o, b, e: b[0], n_obl=1)
        s = reemplazar_comando(s, 'makebox', lambda o, b, e: b[0], n_obl=1, n_opc=2)
        s = reemplazar_comando(s, 'raisebox', lambda o, b, e: b[1], n_obl=2, n_opc=2)
        s = reemplazar_comando(s, 'parbox', lambda o, b, e: self._celda_multilinea(b[1]), n_obl=2, n_opc=3)
        s = reemplazar_comando(s, 'makecell', lambda o, b, e: self._celda_multilinea(b[0]), n_obl=1, n_opc=1)
        s = reemplazar_comando(s, 'shortstack', lambda o, b, e: self._celda_multilinea(b[0]), n_obl=1, n_opc=1)
        s = reemplazar_comando(s, 'thead', lambda o, b, e: self._celda_multilinea(b[0]), n_obl=1, n_opc=1)
        for cmd, car in (('textdegree', '°'), ('textpm', '±'), ('texttimes', '×'), ('textminus', '−'),
                         ('textmu', 'µ'), ('textperthousand', '‰'), ('textordfeminine', 'ª'),
                         ('textordmasculine', 'º'), ('euro', '€'), ('textregistered', '®'),
                         ('texttrademark', '™'), ('textcopyright', '©'), ('textellipsis', '…'),
                         ('guillemotleft', '«'), ('guillemotright', '»'), ('textquotedblleft', '“'),
                         ('textquotedblright', '”'), ('textbullet', '•'), ('textendash', '–'),
                         ('textemdash', '—')):
            s = re.sub(r'\\' + cmd + r'(?![A-Za-z@])(\{\})?', car, s)
        return s

    def _celda_multilinea(self, txt):
        partes = [p.strip() for p in dividir_nivel_superior(txt, '\\\\')]
        txt = ' \\newline '.join(p for p in partes if p)
        return re.sub(r'\\par(?![A-Za-z@])', ' \\\\newline ', txt)

    def _desenvolver_grupos(self, s):
        """Quita llaves «sueltas» {...} que envuelven contenido de bloque.

        Ej.: {\\small\\setstretch{1}\\begin{longtable}...} o {\\footnotesize ... \\par}.
        Las llaves que son argumentos de comandos no se tocan.
        """
        cambios = True
        vueltas = 0
        while cambios and vueltas < 6:
            cambios = False
            vueltas += 1
            salida = []
            pos = 0
            i = 0
            n = len(s)
            while i < n:
                c = s[i]
                if c == '\\':
                    i += 2
                    continue
                if c != '{':
                    i += 1
                    continue
                antes = s[max(0, i - 120):i].rstrip(' \t')
                es_argumento = bool(re.search(r'(\\[A-Za-z@]+\*?|[\]}^_=]|\\begin\{[^}]*\})$', antes))
                try:
                    contenido, fin = leer_grupo(s, i)
                except ValueError:
                    i += 1
                    continue
                if not es_argumento and re.search(r'\n\s*\n|\\par(?![A-Za-z@])|\\begin\{|⟦(TBL|EQ|VERB|PDFPAG)',
                                                  contenido):
                    contenido = re.sub(r'\\(bfseries|itshape|mdseries|upshape|normalfont|small|footnotesize|'
                                       r'scriptsize|tiny|normalsize|large|Large|LARGE|huge|Huge)(?![A-Za-z@])',
                                       '', contenido)
                    salida.append(s[pos:i])
                    salida.append('\n' + contenido + '\n')
                    pos = fin
                    i = fin
                    cambios = True
                    continue
                i += 1
            salida.append(s[pos:])
            s = ''.join(salida)
        return s

    def _normalizar_citas(self, s):
        """Quita ~ de las notas previas y posteriores de las citas (p.~9 -> p. 9)."""
        pat = re.compile(r'\\(parencite|textcite|cite|citep|citet|autocite|footcite|citeauthor|citeyear|'
                         r'citetitle|parencites|textcites|Parencite|Textcite|Cite)\*?((?:\s*\[[^\]]*\])+)')

        def sust(m):
            return m.group(0)[:len(m.group(0)) - len(m.group(2))] + m.group(2).replace('~', ' ')
        return pat.sub(sust, s)

    def _envoltorios(self, s):
        """Quita \\resizebox, \\scalebox, minipage y adjustbox conservando el contenido."""
        def r_resize(o, b, e):
            ancho = a_cm(b[0]) if b[0].strip() != '!' else None
            contenido = b[2]
            if ancho and '\\begin{tikzpicture}' in contenido:
                contenido = contenido.replace('\\begin{tikzpicture}', '\\begin{tikzpicture}⟦ANCHOCM:%.3f⟧' % ancho, 1)
            return contenido
        s = reemplazar_comando(s, 'resizebox', r_resize, n_obl=3, estrella=True)

        def r_scale(o, b, e):
            contenido = b[1]
            try:
                f = float(b[0].replace(',', '.'))
            except ValueError:
                f = None
            if f and '\\begin{tikzpicture}' in contenido:
                contenido = contenido.replace('\\begin{tikzpicture}', '\\begin{tikzpicture}⟦ESCALA:%.3f⟧' % f, 1)
            return contenido
        s = reemplazar_comando(s, 'scalebox', r_scale, n_obl=2, n_opc=1)
        s = reemplazar_comando(s, 'adjustbox', lambda o, b, e: b[1], n_obl=2)

        def r_minipage(nombre, cuerpo):
            k = saltar_blancos(cuerpo, 0)
            while k < len(cuerpo) and cuerpo[k] == '[':
                _, k = leer_opcional(cuerpo, k)
                k = saltar_blancos(cuerpo, k)
            ancho = None
            if k < len(cuerpo) and cuerpo[k] == '{':
                arg, k = leer_grupo(cuerpo, k)
                ancho = a_cm(arg)
            contenido = cuerpo[k:]
            if ancho:
                # \linewidth dentro de la minipage = ancho de la minipage
                def r_graf(m):
                    return re.sub(r'([0-9]*[.,]?[0-9]*)\\(linewidth|textwidth|columnwidth|hsize)',
                                  lambda mm: '%.3fcm' % ((float(mm.group(1).replace(',', '.'))
                                                         if mm.group(1) not in ('', '.') else 1.0) * ancho),
                                  m.group(0))
                contenido = re.sub(r'\\includegraphics\*?\s*\[[^\]]*\]', r_graf, contenido)
            return '\n' + contenido + '\n'
        s = transformar_entornos(s, r'minipage', r_minipage)
        s = transformar_entornos(s, r'adjustbox', lambda n, c: re.sub(r'^\s*\{[^}]*\}', '', c))
        s = transformar_entornos(s, r'landscape|pdflscape|subequations|samepage|flushleft|small|footnotesize',
                                 lambda n, c: c)
        return s

    # ------------------------------------------------------------------
    #  Carátula
    def _portada(self, nombre, cuerpo):
        c = cuerpo
        c = re.sub(r'\\vspace\*?\s*\{\s*\\fill\s*\}', '\n\n⟦VFILL⟧\n\n', c)
        c = re.sub(r'\\vfill(?![A-Za-z])', '\n\n⟦VFILL⟧\n\n', c)

        def r_vspace(o, b, e):
            cm = a_cm(b[0])
            return '\n\n⟦VSPACE:%.2f⟧\n\n' % cm if cm else '\n\n'
        c = reemplazar_comando(c, 'vspace', r_vspace, n_obl=1, estrella=True)

        def r_tabular(nombre_t, cuerpo_t):
            k = saltar_blancos(cuerpo_t, 0)
            if cuerpo_t[k:k + 1] == '[':
                _, k = leer_opcional(cuerpo_t, k)
            _, _, k = leer_argumentos(cuerpo_t, k, 1)
            filas = [f for f in dividir_nivel_superior(cuerpo_t[k:], '\\\\') if f.strip()]
            return '\n\n' + '\n\n'.join(' '.join(x.strip() for x in dividir_nivel_superior(f, '&')) for f in filas) + '\n\n'
        c = transformar_entornos(c, r'tabular\*?|tabularx', r_tabular)

        # Grupos {\large\bfseries texto\par} -> párrafos
        salida, pos = [], 0
        while True:
            k = c.find('{', pos)
            if k < 0:
                break
            if k > 0 and c[k - 1] == '\\' and es_inicio_comando(c, k - 1):
                salida.append(c[pos:k + 1])
                pos = k + 1
                continue
            # solo grupos «sueltos» (no argumentos de comandos)
            antes = c[:k].rstrip(' \t')
            if re.search(r'\\[A-Za-z@]+\*?$', antes) or antes.endswith(('}', ']')) and not antes.endswith('\\par}'):
                txt, fin = leer_grupo(c, k)
                salida.append(c[pos:fin])
                pos = fin
                continue
            txt, fin = leer_grupo(c, k)
            negrita = bool(re.search(r'\\(bfseries|bf)(?![A-Za-z])', txt))
            cursiva = bool(re.search(r'\\(itshape|it|em)(?![A-Za-z])', txt))
            txt = re.sub(r'\\(bfseries|bf|itshape|it|em|large|Large|LARGE|huge|Huge|normalsize|small|'
                         r'footnotesize|scshape|sffamily|rmfamily|centering|par|selectfont)(?![A-Za-z])', '', txt).strip()
            if negrita:
                txt = '\\textbf{%s}' % txt
            if cursiva:
                txt = '\\emph{%s}' % txt
            salida.append(c[pos:k])
            salida.append('\n\n' + txt + '\n\n')
            pos = fin
        salida.append(c[pos:])
        c = ''.join(salida)
        c = re.sub(r'\\par(?![A-Za-z])', '\n\n', c)
        c = re.sub(r'\\\\(\[[^\]]*\])?', '\n\n', c)
        c = re.sub(r'\\(centering|setstretch\{[^}]*\}|singlespacing|onehalfspacing|doublespacing|'
                   r'thispagestyle\{[^}]*\}|null|large|Large|LARGE|huge|Huge|bfseries|normalsize)(?![A-Za-z])', '', c)
        return '\n\n\\begin{caratula}\n' + c.strip() + '\n\\end{caratula}\n\n⟦FINCARATULA⟧\n\n'

    def _bibliografia(self, opc, obl, est):
        opciones = opc[0] or ''
        titulo = self.f.nombres.get('bibname', 'Bibliografía')
        m = re.search(r'title\s*=\s*\{([^}]*)\}', opciones) or re.search(r'title\s*=\s*([^,\]]+)', opciones)
        if m:
            titulo = m.group(1).strip()
        en_indice = 'bibintoc' in opciones or 'heading' not in opciones
        r = '\n\n\\chapter*{%s}\n' % titulo
        if en_indice:
            r += '\\addcontentsline{toc}{chapter}{%s}\n' % titulo
        return r + '\n\\begin{bibliografiaapa}\n⟦REFS⟧\n\\end{bibliografiaapa}\n\n'

    # ------------------------------------------------------------------
    #  Numeración (como LaTeX): títulos, leyendas, ecuaciones y etiquetas
    def _fmt(self, contador):
        c = self.c
        cap = a_letra(c['chapter']) if self.apendice else str(c['chapter'])
        if contador == 'chapter':
            return cap
        if contador == 'section':
            return ('%s.%d' % (cap, c['section'])) if self.modo_seccion == 'chapter' else str(c['section'])
        if contador == 'subsection':
            return '%s.%d' % (self._fmt('section'), c['subsection'])
        if contador == 'subsubsection':
            return '%s.%d' % (self._fmt('subsection'), c['subsubsection'])
        if contador == 'paragraph':
            return '%s.%d' % (self._fmt('subsubsection'), c['paragraph'])
        if contador in ('table', 'figure', 'equation'):
            if self.f.contadores_por_capitulo.get(contador):
                return '%s.%d' % (cap, c[contador])
            return str(c[contador])
        return str(c.get(contador, ''))

    def _registrar_etiqueta(self, nombre, num, tipo, titulo=''):
        nombre = nombre.strip()
        if nombre in self.etiquetas:
            self.duplicadas.append(nombre)
        self.etiquetas[nombre] = {'num': num, 'tipo': tipo, 'titulo': titulo}

    def numerar(self, s):
        salida = []
        pos = 0
        pila = []
        while True:
            m = EVENTO.search(s, pos)
            if not m:
                break
            if not es_inicio_comando(s, m.start()):
                salida.append(s[pos:m.end()])
                pos = m.end()
                continue
            salida.append(s[pos:m.start()])
            g = m.groupdict()
            if g['sec']:
                sec, estrella = g['sec'], g['star']
                try:
                    opc, obl, fin = leer_argumentos(s, m.end(), 1, 1)
                except ValueError:
                    salida.append(m.group(0))
                    pos = m.end()
                    continue
                titulo = obl[0]
                num = None
                if not estrella:
                    self.c[sec] += 1
                    for inferior in ('section', 'subsection', 'subsubsection', 'paragraph', 'subparagraph'):
                        if NIVEL_SECCION[inferior] > NIVEL_SECCION[sec]:
                            self.c[inferior] = 0
                    if sec == 'chapter':
                        for cc in ('table', 'figure', 'equation'):
                            if self.f.contadores_por_capitulo.get(cc):
                                self.c[cc] = 0
                    if NIVEL_SECCION[sec] <= self.f.secnumdepth:
                        num = self._fmt(sec)
                    tipo = 'anexo' if (sec == 'chapter' and self.apendice) else sec
                    self.ref_actual = (num, tipo, titulo)
                txt = '\\%s%s' % (sec, estrella)
                if opc[0] is not None:
                    txt += '[%s]' % opc[0]
                txt += '{%s%s}' % (('⟦H:%s⟧' % num) if num else '', titulo)
                salida.append(txt)
                pos = fin
            elif g['appendix']:
                self.apendice = True
                self.c['chapter'] = 0
                salida.append(m.group(0))
                pos = m.end()
            elif g['setc']:
                nombre, val = g['cname'], g['cval'].strip()
                try:
                    v = int(val)
                    if nombre in self.c:
                        self.c[nombre] = v if g['setc'] == 'setcounter' else self.c[nombre] + v
                except ValueError:
                    pass
                salida.append(m.group(0))
                pos = m.end()
            elif g['renew']:
                contador = g['thec']
                try:
                    _, obl, fin = leer_argumentos(s, m.end(), 1)
                except ValueError:
                    salida.append(m.group(0))
                    pos = m.end()
                    continue
                if contador == 'section':
                    self.modo_seccion = 'chapter' if '\\thechapter' in obl[0] else 'plain'
                salida.append('')   # la redefinición se descarta
                pos = fin
            elif g['benv']:
                env = g['benv']
                if env in ENTORNOS_ECUACION:
                    r = buscar_entorno(s, re.escape(env), m.start())
                    if not r:
                        salida.append(m.group(0))
                        pos = m.end()
                        continue
                    ib, fb, ie, fe = r
                    salida.append(self._ecuacion(env, s[fb:ie], s[fe:]))
                    pos = fe
                    continue
                if env in ENTORNOS_FLOTANTES_TABLA or env in ENTORNOS_FLOTANTES_FIGURA:
                    pila.append(env)
                if env in ('longtable', 'xltabular'):
                    # longtable hace \refstepcounter{table} al comenzar, tenga o no \caption
                    # (por eso la tesis usa \setcounter{table}{0} tras la lista de abreviaturas)
                    self.c['table'] += 1
                    self.ref_actual = (self._fmt('table'), 'table', '')
                salida.append(m.group(0))
                pos = m.end()
            elif g['eenv']:
                env = g['eenv']
                if pila and env == pila[-1]:
                    pila.pop()
                salida.append(m.group(0))
                pos = m.end()
            elif g['cap'] or g['capof']:
                if g['capof']:
                    tipo_f = 'table' if g['capoftype'] == 'table' else 'figure'
                    estrella = g['capofstar']
                else:
                    estrella = g['capstar']
                    tipo_f = None
                    for env in reversed(pila):
                        tipo_f = 'table' if env in ENTORNOS_FLOTANTES_TABLA else 'figure'
                        break
                try:
                    opc, obl, fin = leer_argumentos(s, m.end(), 1, 1)
                except ValueError:
                    salida.append(m.group(0))
                    pos = m.end()
                    continue
                largo = obl[0]
                etiquetas = re.findall(r'\\label\s*\{([^{}]*)\}', largo)
                largo = re.sub(r'\\label\s*\{[^{}]*\}', '', largo)
                en_longtable = bool(pila) and pila[-1] in ('longtable', 'xltabular') and not g['capof']
                if tipo_f and not estrella:
                    if not en_longtable:
                        self.c[tipo_f] += 1
                    num = self._fmt(tipo_f)
                    self.ref_actual = (num, tipo_f, opc[0] if opc[0] is not None else largo)
                    marca = '⟦C:%s:%s⟧' % ('tabla' if tipo_f == 'table' else 'figura', num)
                else:
                    marca = '⟦C:%s:-⟧' % ('tabla' if tipo_f == 'table' else 'figura')
                for e in etiquetas:
                    self._registrar_etiqueta(e, self.ref_actual[0], self.ref_actual[1], self.ref_actual[2])
                txt = '\\caption'
                if opc[0] is not None:
                    txt += '[%s]' % opc[0]
                txt += '{%s%s}' % (marca, largo)
                salida.append(txt)
                pos = fin
            elif g['label'] is not None:
                num, tipo, titulo = self.ref_actual
                self._registrar_etiqueta(g['label'], num, tipo, titulo)
                pos = m.end()
            elif g['dispmath'] is not None:
                # \[ ... \]
                fin = m.end()
                k = fin
                while True:
                    k = s.find('\\]', k)
                    if k < 0 or es_inicio_comando(s, k):
                        break
                    k += 2
                if k < 0:
                    salida.append(m.group(0))
                    pos = m.end()
                    continue
                salida.append(self._ecuacion('displaymath', s[fin:k], s[k + 2:]))
                pos = k + 2
            else:
                salida.append(m.group(0))
                pos = m.end()
        salida.append(s[pos:])
        return ''.join(salida)

    def _limpiar_matematica(self, c):
        c = re.sub(r'\\label\s*\{[^{}]*\}', '', c)
        c = re.sub(r'\\(nonumber|notag)(?![A-Za-z])', '', c)
        c = re.sub(r'\\tag\*?\s*\{[^{}]*\}', '', c)
        c = c.replace('\\begin{split}', '\\begin{aligned}').replace('\\end{split}', '\\end{aligned}')
        c = re.sub(r'\n\s*\n', '\n', c)
        return c.strip()

    def _continua_parrafo(self, resto):
        m = re.match(r'[ \t]*(\n[ \t]*)?(\S)', resto)
        if not m:
            return False
        siguiente = resto[m.start(2):m.start(2) + 30]
        if re.match(r'\\(begin|end|section|subsection|subsubsection|chapter|paragraph|item|par\b|\[|caption|label)', siguiente):
            return False
        return siguiente[0] not in '⟦'

    def _ecuacion(self, env, contenido, resto):
        base = env.rstrip('*')
        estrella = env.endswith('*') or env == 'displaymath'
        if base == 'alignat':
            contenido = re.sub(r'^\s*\{[^}]*\}', '', contenido)
        if base in ('align', 'gather', 'eqnarray', 'flalign', 'alignat'):
            lineas = [l for l in dividir_nivel_superior(contenido, '\\\\') if l.strip()]
        else:
            lineas = [' '.join(l.strip() for l in dividir_nivel_superior(contenido, '\\\\'))] \
                if base == 'multline' else [contenido]
        bloques = []
        for linea in lineas:
            etiquetas = re.findall(r'\\label\s*\{([^{}]*)\}', linea)
            tag = re.search(r'\\tag\*?\s*\{([^{}]*)\}', linea)
            sin_numero = estrella or re.search(r'\\(nonumber|notag)(?![A-Za-z])', linea)
            if tag:
                num = tag.group(1)
            elif sin_numero:
                num = None
            else:
                self.c['equation'] += 1
                num = self._fmt('equation')
            if num:
                self.ref_actual = (num, 'equation', '')
            for e in etiquetas:
                self._registrar_etiqueta(e, num, 'equation')
            tex = self._limpiar_matematica(linea)
            if base in ('align', 'eqnarray', 'flalign', 'alignat'):
                tex = ' '.join(p.strip() for p in dividir_nivel_superior(tex, '&'))
            if not tex:
                continue
            bloques.append(('\n\n⟦EQ:%s⟧\n\n' % num if num else '\n\n') + '\\[ %s \\]\n\n' % tex)
        r = ''.join(bloques)
        if self._continua_parrafo(resto):
            r += '⟦NI⟧'
        return r

    # ------------------------------------------------------------------
    #  Flotantes (tablas y figuras con leyenda APA)
    def _bloque_leyenda(self, tipo, num, corto, largo):
        largo = largo.strip()
        if not num or num == '-':
            return '\n\n\\begin{apaleyenda}\\emph{%s}\\end{apaleyenda}\n\n' % largo
        nombre = self.f.nombres['tablename' if tipo == 'tabla' else 'figurename']
        bm = ('tab' if tipo == 'tabla' else 'fig') + re.sub(r'[^0-9A-Za-z]', '_', num)
        (self.lot if tipo == 'tabla' else self.lof).append(
            {'num': num, 'texto': (corto if corto is not None else largo).strip(), 'bm': bm})
        return ('\n\n\\begin{apaleyenda}⟦BM:%s⟧\\textbf{%s %s}\\\\\n\\emph{%s}\\end{apaleyenda}\n\n'
                % (bm, nombre, num, largo))

    def _bloque_nota(self, texto):
        texto = texto.strip()
        texto = re.sub(r'^\\textit\{Nota\.?\}\s*', '', texto)
        return '\n\n\\begin{apanota}\\emph{Nota.} %s\n\\end{apanota}\n\n' % texto

    def _extraer_leyendas(self, cuerpo):
        leyendas = []

        def r_cap(o, b, e):
            largo = b[0]
            m = re.match(r'⟦C:(\w+):([^⟧]*)⟧', largo)
            tipo = m.group(1) if m else None
            num = m.group(2) if m else None
            if m:
                largo = largo[m.end():]
            leyendas.append((tipo, num, o[0], largo))
            return ''
        cuerpo = reemplazar_comando(cuerpo, 'caption', r_cap, n_obl=1, n_opc=1, estrella=True)
        return cuerpo, leyendas

    def _flotante(self, nombre, cuerpo):
        tipo = 'tabla' if 'table' in nombre else 'figura'
        cuerpo = re.sub(r'^\s*\[[^\]]*\]', '', cuerpo)
        cuerpo, leyendas = self._extraer_leyendas(cuerpo)
        notas = []

        def r_nota(o, b, e):
            notas.append(b[0])
            return ''
        cuerpo = reemplazar_comando(cuerpo, 'nota', r_nota, n_obl=1)
        partes = []
        for t, num, corto, largo in leyendas[:1]:
            partes.append(self._bloque_leyenda(tipo, num, corto, largo))
        partes.append('\n\n' + cuerpo.strip() + '\n\n')
        for n in notas:
            partes.append(self._bloque_nota(n))
        return ''.join(partes)

    # ------------------------------------------------------------------
    #  Tablas
    def parsear_columnas(self, spec, prof=0):
        cols = []
        s = spec
        # expandir *{n}{...}
        for _ in range(10):
            m = re.search(r'\*\s*\{(\d+)\}\s*\{', s)
            if not m:
                break
            contenido, fin = leer_grupo(s, m.end() - 1)
            s = s[:m.start()] + contenido * int(m.group(1)) + s[fin:]
        i = 0
        pendiente_decl = ''
        n = len(s)
        while i < n:
            c = s[i]
            if c in ' \t\n|':
                i += 1
                continue
            if c in '@!<':
                k = saltar_blancos(s, i + 1)
                if k < n and s[k] == '{':
                    _, i = leer_grupo(s, k)
                else:
                    i = k + 1
                continue
            if c == '>':
                k = saltar_blancos(s, i + 1)
                if k < n and s[k] == '{':
                    decl, i = leer_grupo(s, k)
                    pendiente_decl += decl
                else:
                    i = k + 1
                continue
            col = None
            if c in 'lcr':
                col = {'tipo': c, 'alin': c, 'ancho': None}
                i += 1
            elif c in 'pmb':
                k = saltar_blancos(s, i + 1)
                arg, i = leer_grupo(s, k)
                col = {'tipo': 'p', 'alin': 'l', 'ancho': a_cm(arg)}
            elif c == 'X':
                col = {'tipo': 'X', 'alin': 'l', 'ancho': None}
                i += 1
            elif c == 'S':
                col = {'tipo': 'r', 'alin': 'r', 'ancho': None}
                i += 1
                k = saltar_blancos(s, i)
                if k < n and s[k] == '[':
                    _, i = leer_opcional(s, k)
            elif c in self.f.tipos_columna and prof < 5:
                n_args, definicion = self.f.tipos_columna[c]
                i += 1
                for k_arg in range(n_args):
                    k = saltar_blancos(s, i)
                    arg, i = leer_grupo(s, k)
                    definicion = definicion.replace('#%d' % (k_arg + 1), arg)
                sub = self.parsear_columnas(definicion, prof + 1)
                if len(sub) == 1:
                    col = sub[0]
                else:
                    cols.extend(sub)
                    continue
            else:
                i += 1
                continue
            if pendiente_decl:
                if re.search(r'\\centering', pendiente_decl):
                    col['alin'] = 'c'
                elif re.search(r'\\(raggedleft|RaggedLeft)', pendiente_decl):
                    col['alin'] = 'r'
                elif re.search(r'\\(raggedright|RaggedRight)', pendiente_decl):
                    col['alin'] = 'l'
                pendiente_decl = ''
            cols.append(col)
        return cols

    REGLAS = re.compile(r'\s*\\(toprule|midrule|bottomrule|hline|cmidrule|cline|addlinespace|specialrule|'
                        r'morecmidrules|rowcolor|noalign|hdashline|cdashline|arrayrulecolor|pagebreak|newpage|'
                        r'nopagebreak)(?![A-Za-z])')

    def _extraer_reglas(self, fila):
        reglas = []
        while True:
            m = self.REGLAS.match(fila)
            if not m:
                break
            nombre = m.group(1)
            i = m.end()
            # argumentos posibles: (trim) [ancho] {a-b} ...
            while True:
                k = saltar_blancos(fila, i)
                if k < len(fila) and fila[k] == '(':
                    j = fila.find(')', k)
                    i = j + 1 if j > 0 else k + 1
                elif k < len(fila) and fila[k] == '[':
                    _, i = leer_opcional(fila, k)
                elif k < len(fila) and fila[k] == '{' and nombre in ('cmidrule', 'cline', 'specialrule', 'rowcolor',
                                                                     'noalign', 'arrayrulecolor', 'cdashline'):
                    _, i = leer_grupo(fila, k)
                    if nombre != 'specialrule':
                        nombre_args = None
                else:
                    break
            reglas.append(nombre)
            fila = fila[i:]
        return reglas, fila

    def _filas(self, texto):
        filas = []
        pendientes = []
        for seg in dividir_nivel_superior(texto, '\\\\'):
            reglas, resto = self._extraer_reglas(seg)
            pendientes += reglas
            # reglas al final de la fila (antes de \\) no son habituales; se ignoran
            if not resto.strip():
                continue
            celdas = dividir_nivel_superior(resto, '&')
            filas.append({'celdas': [self._limpiar_celda(x) for x in celdas], 'reglas': pendientes})
            pendientes = []
        return filas

    def _limpiar_celda(self, c):
        c = c.strip()
        c = re.sub(r'\\(centering|raggedright|raggedleft|RaggedRight|RaggedLeft|arraybackslash|noindent|'
                   r'hfill|small|footnotesize|scriptsize|normalsize)(?![A-Za-z])', '', c)
        c = re.sub(r'\n\s*\n', ' \\\\newline ', c)
        c = re.sub(r'\\par(?![A-Za-z@])', ' \\\\newline ', c)
        c = re.sub(r'\\vspace\*?\{[^{}]*\}', '', c)
        # \multicolumn{n}{spec}{texto}: se simplifica el formato de columna
        def r_multi(o, b, e):
            spec = self.parsear_columnas(b[1])
            alin = spec[0]['alin'] if spec else 'l'
            return '\\multicolumn{%s}{%s}{%s}' % (b[0].strip(), alin, b[2].strip())
        c = reemplazar_comando(c, 'multicolumn', r_multi, n_obl=3)
        c = c.replace('\n', ' ')
        return c.strip()

    def transformar_tablas(self, s):
        def f(nombre, cuerpo):
            con_ancho = nombre in ('tabularx', 'tabular*', 'tabulary', 'xltabular')
            k = saltar_blancos(cuerpo, 0)
            if not con_ancho and cuerpo[k:k + 1] == '[':
                _, k = leer_opcional(cuerpo, k)
            try:
                _, obl, k = leer_argumentos(cuerpo, k, 2 if con_ancho else 1)
            except ValueError:
                self.avisos.append('Tabla %s con argumentos ilegibles; se omite.' % nombre)
                return ''
            ancho = a_cm(obl[0]) if con_ancho else None
            resto = cuerpo[k:]
            if re.search(r'\\begin\{(tabular|tabularx|longtable)', resto):
                resto = transformar_entornos(resto, r'(?:tabular\*?|tabularx|tabulary)', self._tabla_anidada)
            return self._convertir_tabla(nombre, obl[-1], ancho, resto)
        return transformar_entornos(s, r'(?:tabular\*?|tabularx|tabulary|longtable\*?|xltabular)', f)

    def _tabla_anidada(self, nombre, cuerpo):
        k = saltar_blancos(cuerpo, 0)
        if cuerpo[k:k + 1] == '[':
            _, k = leer_opcional(cuerpo, k)
        _, obl, k = leer_argumentos(cuerpo, k, 2 if nombre in ('tabularx', 'tabular*', 'tabulary') else 1)
        filas = self._filas(cuerpo[k:])
        return ' \\newline '.join(' '.join(f['celdas']) for f in filas)

    def _convertir_tabla(self, nombre, spec, ancho_total, cuerpo):
        cols = self.parsear_columnas(spec)
        if not cols:
            self.avisos.append('Tabla sin columnas reconocibles: {%s}' % spec)
            return cuerpo
        leyenda = ''
        if 'longtable' in nombre or nombre == 'xltabular':
            # \caption{...}\label{...}\\ dentro del longtable
            m = re.search(r'\\caption\*?\s*(\[[^\]]*\])?\s*\{', cuerpo)
            if m and es_inicio_comando(cuerpo, m.start()):
                arg, fin = leer_grupo(cuerpo, m.end() - 1)
                corto = m.group(1)[1:-1] if m.group(1) else None
                mm = re.match(r'⟦C:(\w+):([^⟧]*)⟧', arg)
                num = mm.group(2) if mm else None
                largo = arg[mm.end():] if mm else arg
                leyenda = self._bloque_leyenda('tabla', num, corto, largo)
                # quitar hasta el \\ que cierra la fila de la leyenda
                resto = cuerpo[fin:]
                mm2 = re.match(r'\s*(\\label\{[^}]*\}\s*)*\\\\(\[[^\]]*\])?', resto)
                cuerpo = cuerpo[:m.start()] + (resto[mm2.end():] if mm2 else resto)
        segs = re.split(r'\\(endfirsthead|endhead|endfoot|endlastfoot)(?![A-Za-z])', cuerpo)
        encabezado = None
        if len(segs) > 1:
            partes = {}
            for j in range(1, len(segs), 2):
                partes[segs[j]] = segs[j - 1]
            encabezado = partes.get('endfirsthead', partes.get('endhead'))
            cuerpo_filas = segs[-1]
        else:
            cuerpo_filas = cuerpo
        if encabezado is not None:
            enc = self._filas(encabezado)
            cuerpo_f = self._filas(cuerpo_filas)
            hay_reglas = any(f['reglas'] for f in enc + cuerpo_f) or bool(self.REGLAS.search(encabezado))
            if cuerpo_f and cuerpo_f[0]['reglas']:
                cuerpo_f[0]['reglas'] = []
        else:
            todas = self._filas(cuerpo_filas)
            hay_reglas = any(f['reglas'] for f in todas) or bool(re.search(r'\\(bottomrule|hline)', cuerpo_filas))
            corte = None
            if todas and todas[0]['reglas']:
                for j in range(1, len(todas)):
                    if any(r in ('midrule', 'hline') for r in todas[j]['reglas']):
                        corte = j
                        break
            if corte:
                enc, cuerpo_f = todas[:corte], todas[corte:]
                cuerpo_f[0]['reglas'] = []
            else:
                enc, cuerpo_f = [], todas
                if cuerpo_f:
                    cuerpo_f[0]['reglas'] = []
        reglas_cuerpo = [j for j, f in enumerate(cuerpo_f) if any(r in ('midrule', 'hline') for r in f['reglas'])]
        ncol = len(cols)
        for f_ in enc + cuerpo_f:
            ocupadas = 0
            for c in f_['celdas']:
                m = re.match(r'\\multicolumn\{(\d+)\}', c)
                ocupadas += int(m.group(1)) if m else 1
            if ocupadas > ncol:
                self.avisos.append('Una fila de tabla tiene %d celdas y la tabla %d columnas: «%s»'
                                   % (ocupadas, ncol, texto_plano(' & '.join(f_['celdas']))[:80]))
        anchos = self._anchos(cols, enc, cuerpo_f, ancho_total)
        k = len(self.tablas)
        cuadricula = '|' in re.sub(r'\{[^{}]*\}', '', spec)   # formularios con líneas verticales
        self.tablas.append({'anchos_cm': anchos, 'alin': [c['alin'] for c in cols],
                            'n_encabezado': len(enc), 'reglas_cuerpo': reglas_cuerpo,
                            'bordes': 'cuadricula' if cuadricula else ('apa' if hay_reglas else 'ninguno'),
                            'filas': len(enc) + len(cuerpo_f)})
        lineas = ['\\begin{tabular}{%s}' % ''.join(c['alin'] for c in cols)]
        if enc:
            lineas.append('\\toprule')
            for f_ in enc:
                lineas.append(' & '.join(f_['celdas']) + ' \\\\')
            lineas.append('\\midrule')
        for f_ in cuerpo_f:
            lineas.append(' & '.join(f_['celdas']) + ' \\\\')
        if enc:
            lineas.append('\\bottomrule')
        lineas.append('\\end{tabular}')
        return leyenda + '\n\n⟦TBL:%d⟧\n\n' % k + '\n'.join(lineas) + '\n\n'

    def _anchos(self, cols, enc, cuerpo_f, ancho_total):
        n = len(cols)
        nat = [0.0] * n
        for es_enc, filas in ((True, enc), (False, cuerpo_f)):
            for f_ in filas:
                j = 0
                for celda in f_['celdas']:
                    m = re.match(r'\\multicolumn\{(\d+)\}', celda)
                    span = int(m.group(1)) if m else 1
                    if span == 1 and j < n:
                        txt = texto_plano(celda)
                        if es_enc:
                            w = max([ancho_texto_cm(p, negrita=True) for p in txt.split()] or [0])
                        else:
                            lineas = re.split(r'\\newline', celda)
                            w = max(ancho_texto_cm(texto_plano(l)) for l in lineas)
                        nat[j] = max(nat[j], w)
                    j += span
        relleno = 0.38
        anchos = []
        for j, c in enumerate(cols):
            if c['ancho'] is not None:
                anchos.append(c['ancho'] + relleno)
            elif c['tipo'] == 'X':
                anchos.append(None)
            else:
                anchos.append(min(max(nat[j], 0.8), 7.5) + relleno)
        fijos = sum(a for a in anchos if a is not None)
        nx = anchos.count(None)
        if nx:
            objetivo = ancho_total or ANCHO_UTIL_CM
            resto = max(objetivo - fijos, 2.5 * nx)
            anchos = [a if a is not None else resto / nx for a in anchos]
        total = sum(anchos)
        if total > ANCHO_UTIL_CM:
            anchos = [a * ANCHO_UTIL_CM / total for a in anchos]
        # Ninguna columna más estrecha que su palabra más larga (evita «Códi-go»)
        minimos = [0.0] * n
        for es_enc, filas in ((True, enc), (False, cuerpo_f)):
            for f_ in filas:
                j = 0
                for celda in f_['celdas']:
                    m = re.match(r'\\multicolumn\{(\d+)\}', celda)
                    span = int(m.group(1)) if m else 1
                    if span == 1 and j < n:
                        palabras = texto_plano(celda).split()
                        if palabras:
                            w = max(ancho_texto_cm(p, negrita=es_enc or '\\textbf' in celda) for p in palabras)
                            minimos[j] = max(minimos[j], min(w * 1.04, 4.0) + relleno + 0.1)
                    j += span
        for _ in range(4):
            deficit = sum(max(0.0, minimos[j] - anchos[j]) for j in range(n))
            if deficit < 0.01:
                break
            holgura = [max(0.0, anchos[j] - minimos[j]) for j in range(n)]
            total_h = sum(holgura)
            if total_h <= 0:
                break
            factor = min(1.0, deficit / total_h)
            anchos = [max(anchos[j], minimos[j]) if minimos[j] > anchos[j] else anchos[j] - holgura[j] * factor
                      for j in range(n)]
        return [round(a, 3) for a in anchos]

    # ------------------------------------------------------------------
    #  Figuras: TikZ, \includegraphics e \includepdf
    def _bloque_imagen(self, png, ancho_cm):
        # Marcador provisional: se convierte en LaTeX al final de transformar_graficos
        return '\n\n⟦IMG:%.3f|%s⟧\n\n' % (ancho_cm, png)

    @staticmethod
    def _imagenes_finales(s):
        return re.sub(r'⟦IMG:([0-9.]+)\|([^⟧]+)⟧',
                      lambda m: '\\begin{apafigura}\n\\includegraphics[width=%scm]{%s}\n\\end{apafigura}'
                      % (m.group(1), m.group(2)), s)

    def transformar_graficos(self, s):
        codigos = []

        def r_tikz(nombre, cuerpo):
            ancho = escala = None
            m = re.search(r'⟦ANCHOCM:([0-9.]+)⟧', cuerpo)
            if m:
                ancho = float(m.group(1))
            m = re.search(r'⟦ESCALA:([0-9.]+)⟧', cuerpo)
            if m:
                escala = float(m.group(1))
            cuerpo = re.sub(r'⟦(ANCHOCM|ESCALA):[0-9.]+⟧', '', cuerpo)
            # \ref dentro del dibujo: se resuelven aquí (la compilación aislada no tiene .aux)
            cuerpo = self.resolver_referencias(cuerpo, faltante='??')
            codigos.append(('\\begin{tikzpicture}' + cuerpo + '\\end{tikzpicture}', ancho, escala))
            return '⟦TIKZ:%d⟧' % (len(codigos) - 1)
        s = transformar_entornos(s, r'tikzpicture', r_tikz)
        if codigos:
            resultados = self.g.compilar_tikz([c[0] for c in codigos])

            def r_marca(m):
                k = int(m.group(1))
                res = resultados[k]
                if not res:
                    return ('\n\n\\textcolor{pendientecolor}{\\textbf{[Figura TikZ %d no compilada: revise el '
                            'registro de la conversión]}}\n\n' % (k + 1))
                png, ancho_nat, alto_nat = res
                _, ancho, escala = codigos[k]
                w = ancho if ancho else ancho_nat * (escala or 1.0)
                return self._bloque_imagen(png, self._ajustar(w, alto_nat * w / ancho_nat))
            s = re.sub(r'⟦TIKZ:(\d+)⟧', r_marca, s)

        def r_graf(o, b, e):
            res = self.g.imagen(b[0].strip(), o[0] or '')
            if not res:
                return '\\textcolor{pendientecolor}{\\textbf{[Imagen no encontrada: %s]}}' % b[0].strip().replace('_', '\\_')
            png, ancho, alto = res
            return self._bloque_imagen(png, self._ajustar(ancho, alto))
        s = reemplazar_comando(s, 'includegraphics', r_graf, n_obl=1, n_opc=1, estrella=True)

        def r_pdf(o, b, e):
            paginas = self.g.paginas_pdf(b[0].strip(), o[0] or '')
            if not paginas:
                return '\\textcolor{pendientecolor}{\\textbf{[No se pudo insertar el PDF %s]}}' % b[0].strip().replace('_', '\\_')
            partes = []
            for png, ancho, alto, horizontal in paginas:
                if horizontal:
                    w = self._ajustar(ancho, alto, max_ancho=ALTO_UTIL_CM - 0.3, max_alto=ANCHO_UTIL_CM - 1.4)
                else:
                    w = self._ajustar(ancho, alto, max_ancho=ANCHO_UTIL_CM, max_alto=ALTO_UTIL_CM - 1.6)
                partes.append('\n\n⟦PDFPAG:%s⟧\n\n' % ('H' if horizontal else 'V') + self._bloque_imagen(png, w))
            return ''.join(partes)
        s = reemplazar_comando(s, 'includepdf', r_pdf, n_obl=1, n_opc=1)
        return self._imagenes_finales(s)

    def _ajustar(self, ancho, alto, max_ancho=ANCHO_UTIL_CM, max_alto=ALTO_UTIL_CM - 4.5):
        """Ancho final (cm) que respeta el ancho útil y una altura máxima."""
        w = min(ancho, max_ancho)
        if alto and ancho and alto * w / ancho > max_alto:
            w = max_alto * ancho / alto
        return w

    # ------------------------------------------------------------------
    #  Listas
    def _dividir_items(self, cuerpo):
        """Devuelve (preambulo, [(etiqueta_opcional, texto), ...])."""
        posiciones = []
        prof = 0
        prof_env = 0
        i = 0
        n = len(cuerpo)
        while i < n:
            c = cuerpo[i]
            if c == '\\':
                if cuerpo.startswith('\\begin{', i):
                    prof_env += 1
                elif cuerpo.startswith('\\end{', i):
                    prof_env -= 1
                elif prof == 0 and prof_env == 0 and re.match(r'\\item(?![A-Za-z@])', cuerpo[i:]):
                    posiciones.append(i)
                i += 2
                continue
            if c == '{':
                prof += 1
            elif c == '}':
                prof -= 1
            i += 1
        if not posiciones:
            return cuerpo, []
        items = []
        for k, p in enumerate(posiciones):
            fin = posiciones[k + 1] if k + 1 < len(posiciones) else n
            t = cuerpo[p + 5:fin]
            etiqueta = None
            j = saltar_blancos(t, 0)
            if t[j:j + 1] == '[':
                etiqueta, j2 = leer_opcional(t, j)
                t = t[j2:]
            items.append((etiqueta, t.strip()))
        return cuerpo[:posiciones[0]], items

    def _render_etiqueta(self, plantilla, i):
        r = plantilla
        r = r.replace('\\arabic*', str(i)).replace('\\alph*', a_letra(i, False)).replace('\\Alph*', a_letra(i))
        r = r.replace('\\roman*', a_romano(i)).replace('\\Roman*', a_romano(i, True))
        return r

    def transformar_listas(self, s):
        def f(nombre, cuerpo):
            cuerpo = transformar_entornos(cuerpo, r'(?:enumerate|itemize|description)\*?', f)
            opciones = None
            k = saltar_blancos(cuerpo, 0)
            if cuerpo[k:k + 1] == '[':
                opciones, k = leer_opcional(cuerpo, k)
                cuerpo = cuerpo[k:]
            base = nombre.rstrip('*')
            plantilla = None
            inicio = 1
            if opciones:
                for op in dividir_por_caracter(opciones, ','):
                    clave, _, valor = op.partition('=')
                    clave = clave.strip()
                    if clave == 'label':
                        plantilla = valor.strip()
                        if plantilla.startswith('{') and plantilla.endswith('}'):
                            plantilla = plantilla[1:-1]
                    elif clave == 'start':
                        try:
                            inicio = int(valor)
                        except ValueError:
                            pass
                    elif not valor and base == 'enumerate' and re.fullmatch(r'\s*[(\[]?[aAiI1][.)\]]?\s*', op):
                        plantilla = op.strip().replace('a', '\\alph*').replace('A', '\\Alph*') \
                            .replace('i', '\\roman*').replace('I', '\\Roman*').replace('1', '\\arabic*')
            pre, items = self._dividir_items(cuerpo)
            if not items:
                return cuerpo
            if base == 'itemize' and plantilla is not None:
                plantilla = None      # viñetas normales
            explicitas = any(e is not None for e, _ in items)
            if nombre.endswith('*'):
                partes = []
                for j, (et, txt) in enumerate(items):
                    etq = et if et is not None else (self._render_etiqueta(plantilla, j + inicio) if plantilla else
                                                     ('(%d)' % (j + inicio) if base == 'enumerate' else '•'))
                    partes.append(etq + '~' + re.sub(r'\s*\n\s*', ' ', txt))
                return ' ' + ' '.join(partes) + ' '
            if base == 'description':
                return '\\begin{description}' + cuerpo + '\\end{description}'
            if plantilla is not None or explicitas:
                partes = ['\n\n\\begin{listaetiquetada}\n']
                for j, (et, txt) in enumerate(items):
                    if et is None:
                        et = self._render_etiqueta(plantilla, j + inicio) if plantilla else (
                            '%d.' % (j + inicio) if base == 'enumerate' else '•')
                    partes.append('%s⟦TAB⟧%s\n\n' % (et, txt))
                partes.append('\\end{listaetiquetada}\n\n')
                return ''.join(partes)
            return '\\begin{%s}%s%s\\end{%s}' % (base, pre, ''.join(
                '\\item%s %s\n' % ('[%s]' % et if et is not None else '', txt) for et, txt in items), base)

        salida = []
        pos = 0
        while True:
            r = buscar_entorno(s, r'(?:enumerate|itemize|description)\*?', pos)
            if not r:
                break
            ib, fb, ie, fe = r
            real = re.match(r'\\begin\{([^}]*)\}', s[ib:fb]).group(1)
            salida.append(s[pos:ib])
            salida.append(f(real, s[fb:ie]))
            if not real.endswith('*') and self._continua_parrafo(s[fe:]):
                salida.append('\n\n⟦NI⟧')
            pos = fe
        salida.append(s[pos:])
        return ''.join(salida)

    # ------------------------------------------------------------------
    #  Títulos, índice general y entradas manuales (\addcontentsline)
    def transformar_titulos(self, s):
        pat = re.compile(
            r'\\(?:(?P<sec>chapter|section|subsection|subsubsection|paragraph|subparagraph)(?P<star>\*?)(?![A-Za-z@])'
            r'|(?P<acl>addcontentsline)\s*\{(?P<aclf>[^{}]*)\}\s*\{(?P<acll>[^{}]*)\}'
            r'|(?P<idx>tableofcontents|listoftables|listoffigures)(?![A-Za-z@])'
            r'|(?P<appendix>appendix)(?![A-Za-z@]))')
        niveles = {'part': 1, 'chapter': 1, 'section': 2, 'subsection': 3, 'subsubsection': 4,
                   'paragraph': 5, 'subparagraph': 5}
        max_nivel = self.f.tocdepth + 1
        salida = []
        pos = 0
        ultimo = None          # (bm, fin_en_entrada) del último título sin entrada en el índice
        pendientes = []        # entradas a la espera del siguiente destino
        apendice = False

        def agregar(nivel, texto, bm):
            texto = re.sub(r'\\footnote\{[^{}]*\}', '', texto)
            texto = re.sub(r'⟦H:[^⟧]*⟧', '', texto).strip()
            if nivel <= max_nivel:
                self.toc.append({'nivel': min(nivel, 3), 'texto': texto, 'bm': bm})

        while True:
            m = pat.search(s, pos)
            if not m:
                break
            if not es_inicio_comando(s, m.start()):
                salida.append(s[pos:m.end()])
                pos = m.end()
                continue
            salida.append(s[pos:m.start()])
            g = m.groupdict()
            if g['appendix']:
                apendice = True
                pos = m.end()
                continue
            if g['idx']:
                tipo = {'tableofcontents': 'toc', 'listoftables': 'lot', 'listoffigures': 'lof'}[g['idx']]
                bm = 'idx' + tipo
                for nivel, texto in pendientes:
                    agregar(nivel, texto, bm)
                pendientes = []
                salida.append('\n\n⟦INDICE:%s⟧\n\n' % tipo)
                ultimo = None
                pos = m.end()
                continue
            if g['acl']:
                try:
                    texto, fin = leer_grupo(s, saltar_blancos(s, m.end()))
                except ValueError:
                    pos = m.end()
                    continue
                pos = fin
                if g['aclf'].strip() != 'toc':
                    continue
                nivel = niveles.get(g['acll'].strip(), 2)
                entre = s[ultimo[1]:m.start()] if ultimo else 'x'
                if ultimo and re.fullmatch(r'(\s|\\phantomsection|\\label\{[^}]*\})*', entre):
                    agregar(nivel, texto, ultimo[0])
                    ultimo = None
                else:
                    pendientes.append((nivel, texto))
                continue
            # título
            sec, estrella = g['sec'], g['star']
            try:
                opc, obl, fin = leer_argumentos(s, m.end(), 1, 1)
            except ValueError:
                salida.append(m.group(0))
                pos = m.end()
                continue
            titulo = obl[0]
            mm = re.match(r'⟦H:([^⟧]*)⟧', titulo)
            num = mm.group(1) if mm else None
            if mm:
                titulo = titulo[mm.end():]
            titulo = titulo.strip()
            corto = opc[0].strip() if opc[0] is not None else titulo
            nivel = niveles[sec]
            self.n_titulo += 1
            bm = 'tit%d' % self.n_titulo
            for nv, texto in pendientes:
                agregar(nv, texto, bm)
            pendientes = []
            if nivel == 1 and num:
                nombre = self.f.nombres['appendixname' if apendice else 'chaptername']
                visible = '%s %s\\\\ %s' % (nombre.upper(), num, titulo)
                agregar(1, '%s %s. %s' % (nombre, num, corto), bm)
            elif num:
                visible = '%s. %s' % (num, titulo)
                agregar(nivel, '%s %s' % (num, corto), bm)
            else:
                visible = titulo
            if nivel >= 4 and not re.search(r'[.:?!]\s*$', visible):
                visible += '.'
            cmd = {1: 'section', 2: 'subsection', 3: 'subsubsection', 4: 'paragraph', 5: 'subparagraph'}[nivel]
            salida.append('\n\n\\%s*{%s}\\label{%s}\n\n' % (cmd, visible, bm))
            ultimo = (bm, fin) if (estrella or not num) else None
            pos = fin
        salida.append(s[pos:])
        if pendientes:
            self.avisos.append('Entradas de \\addcontentsline sin destino: %s' % pendientes)
        return ''.join(salida)

    def _indices(self, s):
        nombres = self.f.nombres

        def bloque(tipo):
            titulo = {'toc': nombres.get('contentsname'), 'lot': nombres.get('listtablename'),
                      'lof': nombres.get('listfigurename')}[tipo]
            partes = ['\n\n\\begin{tituloindice}⟦BM:idx%s⟧%s\\end{tituloindice}\n\n' % (tipo, titulo)]
            if tipo == 'toc':
                for e in self.toc:
                    partes.append('\\begin{indice%d}⟦TOCREF:%s⟧%s\\end{indice%d}\n\n'
                                  % (e['nivel'], e['bm'], e['texto'], e['nivel']))
            else:
                lista = self.lot if tipo == 'lot' else self.lof
                # orden del documento = orden de numeración (las longtable se procesan aparte)
                def clave(e):
                    return [int(p) if p.isdigit() else (1000 + ord(p[0])) for p in re.split(r'[.\-]', e['num']) if p]
                try:
                    lista = sorted(lista, key=clave)
                except (TypeError, ValueError, IndexError):
                    pass
                nombre = nombres['tablename' if tipo == 'lot' else 'figurename']
                for e in lista:
                    partes.append('\\begin{indicefig}⟦TOCREF:%s⟧%s %s. %s\\end{indicefig}\n\n'
                                  % (e['bm'], nombre, e['num'], e['texto']))
                if not lista:
                    partes.append('\\begin{indicefig}(Sin entradas)\\end{indicefig}\n\n')
            return ''.join(partes)
        return re.sub(r'⟦INDICE:(toc|lot|lof)⟧', lambda m: bloque(m.group(1)), s)

    # ------------------------------------------------------------------
    #  Referencias cruzadas
    def _buscar_etiqueta(self, nombre):
        nombre = nombre.strip()
        e = self.etiquetas.get(nombre)
        if e and e['num']:
            return e
        a = self.aux.get(nombre)
        if a:
            return {'num': a['num'], 'tipo': a.get('tipo'), 'titulo': a.get('titulo', '')}
        return None

    def resolver_referencias(self, s, faltante=None):
        def falta(nombre):
            self.refs_faltantes.append(nombre)
            return faltante if faltante is not None else '\\textcolor{pendientecolor}{\\textbf{??}}'

        def r_ref(o, b, e):
            res = []
            for nombre in b[0].split(','):
                et = self._buscar_etiqueta(nombre)
                res.append(et['num'] if et else falta(nombre.strip()))
            return ', '.join(res)

        def r_eqref(o, b, e):
            et = self._buscar_etiqueta(b[0])
            return '(%s)' % et['num'] if et else falta(b[0].strip())

        prefijos = {'table': 'Tabla', 'figure': 'Figura', 'equation': 'ecuación', 'chapter': 'capítulo',
                    'anexo': 'Anexo', 'section': 'sección', 'subsection': 'sección', 'subsubsection': 'sección',
                    'paragraph': 'sección'}

        def r_auto(o, b, e, mayus=False):
            res = []
            for nombre in b[0].split(','):
                et = self._buscar_etiqueta(nombre)
                if not et:
                    res.append(falta(nombre.strip()))
                    continue
                pre = prefijos.get(et.get('tipo') or '', '')
                num = '(%s)' % et['num'] if et.get('tipo') == 'equation' else et['num']
                if mayus and pre:
                    pre = pre[0].upper() + pre[1:]
                res.append(('%s~%s' % (pre, num)) if pre else num)
            return ', '.join(res)

        def r_nameref(o, b, e):
            et = self._buscar_etiqueta(b[0])
            return et.get('titulo') or et['num'] if et else falta(b[0].strip())

        def r_pageref(o, b, e):
            a = self.aux.get(b[0].strip())
            return a.get('pagina', '?') if a else falta(b[0].strip())

        s = reemplazar_comando(s, 'eqref', r_eqref, n_obl=1)
        s = reemplazar_comando(s, 'ref', r_ref, n_obl=1, estrella=True)
        s = reemplazar_comando(s, 'autoref', r_auto, n_obl=1, estrella=True)
        s = reemplazar_comando(s, 'cref', r_auto, n_obl=1, estrella=True)
        s = reemplazar_comando(s, 'Autoref', lambda o, b, e: r_auto(o, b, e, True), n_obl=1, estrella=True)
        s = reemplazar_comando(s, 'Cref', lambda o, b, e: r_auto(o, b, e, True), n_obl=1, estrella=True)
        s = reemplazar_comando(s, 'nameref', r_nameref, n_obl=1, estrella=True)
        s = reemplazar_comando(s, 'pageref', r_pageref, n_obl=1, estrella=True)
        return s

    def comparar_con_aux(self):
        """Lista de diferencias entre la numeración calculada y la del .aux."""
        difs = []
        for nombre, a in self.aux.items():
            e = self.etiquetas.get(nombre)
            if e and e['num'] and a.get('num') and e['num'] != a['num']:
                difs.append('%s: calculado %s / LaTeX %s' % (nombre, e['num'], a['num']))
        return difs

    # ------------------------------------------------------------------
    #  Limpieza final
    def _limpiar(self, s):
        s = re.sub(r'\\pagenumbering\s*\{\s*(roman|Roman)\s*\}', '\n\n⟦SECCION:roman⟧\n\n', s)
        s = re.sub(r'\\pagenumbering\s*\{\s*arabic\s*\}', '\n\n⟦SECCION:arabic⟧\n\n', s)
        s = re.sub(r'\\frontmatter(?![A-Za-z])', '\n\n⟦SECCION:roman⟧\n\n', s)
        s = re.sub(r'\\mainmatter(?![A-Za-z])', '\n\n⟦SECCION:arabic⟧\n\n', s)
        con_args = {  # comando: (obligatorios, opcionales)
            'setlength': (2, 0), 'addtolength': (2, 0), 'setstretch': (1, 0), 'vspace': (1, 0),
            'thispagestyle': (1, 0), 'pagestyle': (1, 0), 'captionsetup': (1, 1), 'addtocontents': (2, 0),
            'setcounter': (2, 0), 'addtocounter': (2, 0), 'stepcounter': (1, 0), 'enlargethispage': (1, 0),
            'linespread': (1, 0), 'fontsize': (2, 0), 'color': (1, 1), 'setlist': (1, 1),
            'pdfbookmark': (2, 1), 'hypersetup': (1, 0), 'graphicspath': (1, 0), 'sisetup': (1, 0),
            'index': (1, 0), 'markboth': (2, 0), 'markright': (1, 0),
            'renewcommand': (2, 1), 'newcounter': (1, 1), 'selectlanguage': (1, 0), 'hyphenation': (1, 0),
            'newpage': (0, 0), 'definecolor': (3, 0), 'usetikzlibrary': (1, 0), 'tikzset': (1, 0),
            'pgfplotsset': (1, 0), 'arrayrulecolor': (1, 0), 'rowcolors': (3, 0), 'newgeometry': (1, 0),
            'restoregeometry': (0, 0), 'counterwithin': (2, 0), 'counterwithout': (2, 0),
            'addbibresource': (1, 1), 'DeclareFieldFormat': (2, 1), 'titleformat': (2, 4),
            'titlespacing': (4, 1), 'AtBeginEnvironment': (2, 0), 'AtEndEnvironment': (2, 0),
            'newgeometry*': (1, 0), 'cftsetindents': (3, 0),
        }
        for cmd, (no, nopc) in con_args.items():
            if no == 0 and nopc == 0:
                continue
            s = reemplazar_comando(s, cmd, lambda o, b, e: '', n_obl=no, n_opc=nopc, estrella=True)
        # \label: se conservan solo los de los títulos (tit1, tit2...), que pandoc usa como marcadores
        s = reemplazar_comando(s, 'label', lambda o, b, e: None if re.fullmatch(r'tit\d+', b[0].strip()) else '',
                               n_obl=1)
        s = reemplazar_comando(s, 'hspace', lambda o, b, e: ' ', n_obl=1, estrella=True)
        s = re.sub(r'\\par(?![A-Za-z@])', '\n\n', s)
        sueltos = ('centering', 'raggedright', 'RaggedRight', 'raggedleft', 'RaggedLeft', 'noindent', 'indent',
                   'small', 'footnotesize', 'scriptsize', 'tiny', 'normalsize', 'large', 'Large', 'LARGE',
                   'huge', 'Huge', 'singlespacing', 'onehalfspacing', 'doublespacing', 'begingroup',
                   'endgroup', 'phantomsection', 'clearpage', 'newpage', 'cleardoublepage', 'pagebreak',
                   'nopagebreak', 'FloatBarrier', 'vfill', 'hfill', 'medskip', 'smallskip', 'bigskip',
                   'protect', 'relax', 'null', 'leavevmode', 'sloppy', 'fussy', 'allowbreak', 'nobreak',
                   'appendix', 'backmatter', 'maketitle', 'arraybackslash', 'normalfont', 'restoregeometry',
                   'linebreak', 'selectfont', 'unskip', 'ignorespaces', 'strut', 'break', 'filbreak',
                   'goodbreak', 'needspace', 'frenchspacing', 'nonfrenchspacing', 'printindex',
                   'listofabbreviations', 'tightlist')
        s = re.sub(r'\\(' + '|'.join(sueltos) + r')(?![A-Za-z@])(\s*\[[^\]]*\])?', '', s)
        s = re.sub(r'\\-', '', s)
        s = re.sub(r'\\begin\{(center|flushleft|flushright)\}', r'\\begin{\1}', s)
        return s

    def _restaurar_verbatim(self, s):
        def r(m):
            txt = self.f.verbatim[int(m.group(1))].expandtabs(4).strip('\n')
            txt = txt.replace('\\end{verbatim}', '\\end{verbatim }')
            return '\n\n\\begin{verbatim}\n%s\n\\end{verbatim}\n\n' % txt
        return re.sub(r'⟦VERB:(\d+)⟧', r, s)

    # ------------------------------------------------------------------
    def comandos_desconocidos(self, s):
        """Comandos que quedan en el LaTeX final y que pandoc podría no conocer."""
        conocidos = set('''textbf textit emph texttt textsc textsuperscript textsubscript underline textcolor
            parencite textcite cite citep citet autocite footcite nocite citeauthor citeyear citetitle parencites
            textcites Parencite Textcite Cite footnote url href includegraphics section subsection
            subsubsection paragraph subparagraph label item begin end toprule midrule bottomrule multicolumn
            multirow newline ldots dots textbackslash LaTeX TeX S P quad qquad textquotesingle textasciitilde
            textrm textsf textup textmd textnormal uppercase MakeUppercase today'''.split())
        sin_mate = re.sub(r'\\\[.*?\\\]', ' ', s, flags=re.S)
        sin_mate = re.sub(r'(?<!\\)\$[^$]*\$', ' ', sin_mate)
        sin_mate = re.sub(r'\\begin\{verbatim\}.*?\\end\{verbatim\}', ' ', sin_mate, flags=re.S)
        encontrados = {}
        for m in re.finditer(r'\\([A-Za-z@]+)', sin_mate):
            if es_inicio_comando(sin_mate, m.start()) and m.group(1) not in conocidos:
                encontrados[m.group(1)] = encontrados.get(m.group(1), 0) + 1
        return encontrados


def leer_aux(ruta):
    """Lee \\newlabel del .aux (formato hyperref) -> {etiqueta: {num, pagina, titulo, tipo}}."""
    res = {}
    if not ruta or not Path(ruta).is_file():
        return res
    texto = Path(ruta).read_text(encoding='utf-8', errors='replace')
    for m in re.finditer(r'\\newlabel\{([^{}]*)\}\{', texto):
        nombre = m.group(1)
        if '@' in nombre:
            continue
        try:
            arg, _ = leer_grupo(texto, m.end() - 1)
            partes = []
            i = 0
            while i < len(arg) and len(partes) < 5:
                k = saltar_blancos(arg, i)
                if k >= len(arg) or arg[k] != '{':
                    break
                p, i = leer_grupo(arg, k)
                partes.append(p)
        except ValueError:
            continue
        if not partes:
            continue
        ancla = partes[3] if len(partes) > 3 else ''
        tipo = ancla.split('.')[0] if ancla else None
        tipo = {'table': 'table', 'figure': 'figure', 'equation': 'equation', 'chapter': 'chapter',
                'section': 'section', 'subsection': 'subsection', 'subsubsection': 'subsubsection',
                'appendix': 'anexo'}.get(tipo, tipo)
        res[nombre] = {'num': partes[0], 'pagina': partes[1] if len(partes) > 1 else '',
                       'titulo': partes[2] if len(partes) > 2 else '', 'tipo': tipo}
    return res


def aux_completo(ruta):
    if not ruta or not Path(ruta).is_file():
        return False
    return '\\@abspage@last' in Path(ruta).read_text(encoding='utf-8', errors='replace')
