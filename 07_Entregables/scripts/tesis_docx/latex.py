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
        nuevo = funcion(opc, obl, bool(m.group(1)))
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
        salida.append(funcion(real, s[fb:ie]))
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


def ancho_texto_cm(txt, pt=12.0, negrita=False):
    """Ancho aproximado de un texto en Times New Roman."""
    factor = 0.50 if negrita else 0.47     # ancho medio de un carácter en em
    return len(txt) * factor * pt * 2.54 / 72.0


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
    def recoger_definiciones(self, texto):
        """Recoge \\newcommand/\\providecommand/\\newcolumntype y los elimina del texto."""
        def r_new(opc, obl, est):
            nombre = obl[0].strip()
            if not nombre.startswith('\\'):
                return ''
            nombre = nombre[1:]
            n = int(opc[0]) if opc[0] and opc[0].strip().isdigit() else 0
            defecto = opc[1]
            if nombre not in self.macros or True:
                self.macros[nombre] = (n, defecto, obl[1])
            return ''
        for cmd in ('newcommand', 'providecommand', 'DeclareRobustCommand'):
            texto = reemplazar_comando(texto, cmd, r_new, n_obl=2, n_opc=2, estrella=True)

        def r_col(opc, obl, est):
            n = int(opc[0]) if opc[0] and opc[0].strip().isdigit() else 0
            self.tipos_columna[obl[0].strip()] = (n, obl[1])
            return ''
        texto = reemplazar_comando(texto, 'newcolumntype', r_col, n_obl=2, n_opc=1)
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
