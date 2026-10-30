# -*- coding: utf-8 -*-
"""Bibliografía para pandoc/citeproc.

* Une todos los .bib de 05_Tesis_LaTeX/bib/ en el orden de \\addbibresource del
  preámbulo (los demás .bib al final, en orden alfabético).  Si una clave se
  repite en varios archivos se conserva la PRIMERA (igual que biber).
* Adapta campos de biblatex-apa que citeproc no interpreta igual:
  - titleaddon -> type (se imprime entre corchetes: «[Certificado]»);
  - langid se elimina para que pandoc no cambie las mayúsculas de los títulos.
* Prepara el estilo CSL APA 7 en español: «y» en lugar de «&», sin coma antes
  de «y» y guion corto (–) en los rangos de páginas.
* Devuelve las abreviaturas de autores corporativos (campo shortauthor), que
  el filtro de citas usa para escribir «(Organización ... [ISO], 2026)» la
  primera vez y «(ISO, 2026)» después, como biblatex-apa.
"""

import re
from pathlib import Path

from .latex import leer_grupo


def _entradas(texto):
    """Itera (tipo, clave, cuerpo_completo) de un archivo .bib."""
    i = 0
    n = len(texto)
    while True:
        m = re.compile(r'@(\w+)\s*([{(])').search(texto, i)
        if not m:
            return
        tipo = m.group(1).lower()
        inicio = m.start()
        if m.group(2) == '{':
            try:
                cuerpo, fin = leer_grupo(texto, m.end() - 1)
            except ValueError:
                return
        else:
            fin = texto.find(')', m.end())
            cuerpo = texto[m.end():fin]
            fin += 1
        clave = cuerpo.split(',', 1)[0].strip() if tipo not in ('string', 'comment', 'preamble') else None
        yield tipo, clave, texto[inicio:fin], cuerpo
        i = fin


def _campos(cuerpo):
    """Diccionario simple campo -> valor (sin llaves externas)."""
    campos = {}
    resto = cuerpo.split(',', 1)[1] if ',' in cuerpo else ''
    i = 0
    while i < len(resto):
        m = re.compile(r'\s*([A-Za-z_\-]+)\s*=\s*').match(resto, i)
        if not m:
            break
        k = m.end()
        if k < len(resto) and resto[k] == '{':
            valor, k = leer_grupo(resto, k)
        elif k < len(resto) and resto[k] == '"':
            j = resto.find('"', k + 1)
            valor, k = resto[k + 1:j], j + 1
        else:
            j = re.compile(r'[,}]').search(resto, k)
            j = j.start() if j else len(resto)
            valor, k = resto[k:j].strip(), j
        campos[m.group(1).lower()] = valor
        j = resto.find(',', k)
        if j < 0:
            break
        i = j + 1
    return campos


def unir_bib(dir_tesis, destino, avisos):
    dir_bib = Path(dir_tesis) / 'bib'
    preambulo = (Path(dir_tesis) / 'preambulo.tex').read_text(encoding='utf-8', errors='replace')
    orden = []
    for m in re.finditer(r'\\addbibresource(?:\[[^\]]*\])?\{([^}]*)\}', preambulo):
        p = (Path(dir_tesis) / m.group(1).strip()).resolve()
        if p.is_file() and p not in orden:
            orden.append(p)
    for p in sorted(dir_bib.glob('*.bib')):
        if p.resolve() not in orden:
            orden.append(p.resolve())
    vistas = {}
    salida = []
    abreviaturas = {}
    duplicadas = []
    for p in orden:
        texto = p.read_text(encoding='utf-8', errors='replace')
        for tipo, clave, completo, cuerpo in _entradas(texto):
            if tipo in ('comment', 'preamble'):
                continue
            if tipo == 'string':
                salida.append(completo)
                continue
            if clave in vistas:
                if vistas[clave] != p.name:
                    duplicadas.append('%s (%s, se usa %s)' % (clave, p.name, vistas[clave]))
                continue
            vistas[clave] = p.name
            campos = _campos(cuerpo)
            nuevo = completo
            if 'titleaddon' in campos and 'type' not in campos:
                nuevo = re.sub(r'(\n\s*)titleaddon(\s*=)', r'\1type\2', nuevo, count=1)
            nuevo = re.sub(r'\n\s*langid\s*=\s*\{[^}]*\}\s*,?', '\n', nuevo)
            salida.append(nuevo)
            corto = campos.get('shortauthor')
            autor = campos.get('author', '')
            if corto and autor.startswith('{') and autor.endswith('}'):
                nombre = autor[1:-1].strip()
                corto = corto.strip()
                if corto.startswith('{') and corto.endswith('}'):
                    corto = corto[1:-1]
                abreviaturas[nombre] = corto
    if duplicadas:
        avisos.append('Claves bibliográficas repetidas entre archivos .bib (se usa la primera): %s'
                      % ', '.join(duplicadas[:12]) + (' ...' if len(duplicadas) > 12 else ''))
    Path(destino).write_text('\n\n'.join(salida) + '\n', encoding='utf-8')
    return {'archivos': [p.name for p in orden], 'entradas': len(vistas), 'abreviaturas': abreviaturas}


def preparar_csl(origen, destino):
    """Copia apa.csl con los ajustes para español (ver docstring del módulo)."""
    csl = Path(origen).read_text(encoding='utf-8')
    csl = csl.replace('and="symbol"', 'and="text"')
    csl = csl.replace('delimiter-precedes-last="always"', 'delimiter-precedes-last="never"')
    termino = '<term name="page-range-delimiter">–</term>'
    if '<locale xml:lang="es">' in csl:
        csl = re.sub(r'(<locale xml:lang="es">\s*<terms>)', r'\1\n      ' + termino, csl, count=1)
    else:
        csl = csl.replace('</info>', '</info>\n  <locale xml:lang="es"><terms>%s</terms></locale>' % termino, 1)
    Path(destino).write_text(csl, encoding='utf-8')
    return destino
