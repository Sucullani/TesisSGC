#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convierte la tesis LaTeX (05_Tesis_LaTeX/tesis.tex) en un .docx con formato APA 7.

Uso (desde cualquier carpeta):
    python3 07_Entregables/scripts/tesis_a_docx.py

Salida por defecto: 07_Entregables/Tesis_SGC_Borrador_Final.docx
Ver README_docx.md (misma carpeta) para las opciones y las limitaciones.

Pasos:
 1. Compila la tesis con latexmk en una carpeta temporal para obtener el .aux
    (si falla, usa el último .aux válido) y lo contrasta con la numeración
    que el programa calcula desde la fuente.
 2. Aplana la fuente: \\input, \\IfFileExists, \\tablamodelo, macros propias y
    de valores_modelo.tex; quita \\guia; marca \\pendiente en rojo; convierte
    \\nota, tablas (tipos L, C, R, P, Q; longtable), ecuaciones numeradas,
    listas con etiquetas, títulos numerados y \\ref/\\eqref.
 3. Figuras: TikZ -> PNG (compiladas con el preámbulo de la tesis); PDF -> PNG;
    páginas de \\includepdf (planos, certificados, cómputos) -> PNG.
 4. pandoc + citeproc (APA 7, español) con todos los .bib y la plantilla APA.
 5. Posproceso con python-docx (leyendas, notas, bordes APA, ecuaciones,
    índices, secciones con numeración romana/arábiga, páginas apaisadas).
 6. (Opcional) LibreOffice calcula los números de página del índice y
    exporta un PDF de verificación.
"""

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))

from tesis_docx import bibliografia, compilacion, libreoffice, word          # noqa: E402
from tesis_docx.graficos import Graficos                                   # noqa: E402
from tesis_docx import latex as modulo_latex                              # noqa: E402
from tesis_docx.latex import Fuente, Transformador, leer_aux               # noqa: E402

RAIZ = AQUI.parents[1]
DIR_TESIS = RAIZ / '05_Tesis_LaTeX'
SALIDA = RAIZ / '07_Entregables' / 'Tesis_SGC_Borrador_Final.docx'
PLANTILLA = AQUI / 'plantilla_apa.docx'
TRABAJO = AQUI / '_trabajo'


def metadatos(fuente):
    import re
    pre = fuente.preambulo
    titulo = fuente.macros.get('titulotesis', (0, None, ''))[2].replace('~', ' ')
    asunto = re.search(r'pdfsubject=\{([^}]*)\}', pre)
    autor = fuente.macros.get('postulante', (0, None, ''))[2]
    return {'titulo': titulo, 'asunto': asunto.group(1) if asunto else 'Tesis de grado',
            'autor': '' if autor.startswith('[') else autor,
            'palabras_clave': 'gestión de la calidad; ISO 9001; control de materiales; losa alivianada'}


def main():
    global DIR_TESIS
    ap = argparse.ArgumentParser(description='Convierte la tesis LaTeX en un .docx con formato APA 7.')
    ap.add_argument('--salida', default=str(SALIDA), help='ruta del .docx (por defecto: %(default)s)')
    ap.add_argument('--dir-tesis', default=str(RAIZ / '05_Tesis_LaTeX'),
                    help='carpeta de la tesis LaTeX (por defecto: %(default)s)')
    ap.add_argument('--trabajo', default=str(TRABAJO), help='carpeta de archivos intermedios y caché')
    ap.add_argument('--principal', default='tesis.tex',
                    help='archivo principal dentro de --dir-tesis (por defecto: %(default)s; p. ej. tesis_sencilla.tex)')
    ap.add_argument('--sin-compilar', action='store_true', help='no compila LaTeX; usa el último .aux válido')
    ap.add_argument('--aux', help='usar este .aux en lugar de compilar')
    ap.add_argument('--regenerar-plantilla', action='store_true', help='vuelve a crear plantilla_apa.docx')
    ap.add_argument('--tabla-pt', type=float, default=12, help='tamaño de letra en tablas (APA: 12)')
    ap.add_argument('--formulario-pt', type=float, default=10, help='tamaño de letra en formularios con cuadrícula')
    ap.add_argument('--dpi-tikz', type=int, default=300, help='resolución de las figuras TikZ (mín. 200)')
    ap.add_argument('--dpi-pdf', type=int, default=150, help='resolución de las páginas de \\includepdf')
    ap.add_argument('--latex-rapido', action='store_true',
                    help='una sola pasada de pdflatex -draftmode en lugar de latexmk (basta para el .aux)')
    ap.add_argument('--pdf', nargs='?', const='auto', help='exporta también un PDF con LibreOffice')
    ap.add_argument('--sin-paginas', action='store_true',
                    help='no usa LibreOffice para escribir los números de página del índice')
    args = ap.parse_args()

    t0 = time.time()
    DIR_TESIS = Path(args.dir_tesis).resolve()
    trabajo = Path(args.trabajo).resolve()
    trabajo.mkdir(parents=True, exist_ok=True)
    avisos = []

    def paso(msg):
        print('[%5.1f s] %s' % (time.time() - t0, msg), flush=True)

    # 1. .aux
    if args.aux:
        ruta_aux, origen = Path(args.aux), 'indicado con --aux'
    elif args.sin_compilar:
        ruta_aux = trabajo / 'aux_valido' / 'tesis.aux'
        origen = 'último .aux válido (caché)'
        if not ruta_aux.is_file():
            ruta_aux, origen = DIR_TESIS / 'build' / 'tesis.aux', '05_Tesis_LaTeX/build/tesis.aux'
    else:
        paso('Compilando la tesis con latexmk (carpeta temporal) para obtener el .aux...')
        ruta_aux, origen = compilacion.compilar_tesis(DIR_TESIS, trabajo, avisos,
                                                      usar_latexmk=not args.latex_rapido)
    paso('.aux: %s (%s)' % (ruta_aux, origen))

    # 2-3. LaTeX -> LaTeX para pandoc (+ figuras)
    paso('Aplanando y transformando la fuente LaTeX...')
    fuente = Fuente(DIR_TESIS, archivo=args.principal, avisos=avisos).cargar()
    graficos = Graficos(DIR_TESIS, trabajo, fuente, avisos, dpi_tikz=max(200, args.dpi_tikz),
                        dpi_pdf=args.dpi_pdf)
    aux = leer_aux(ruta_aux) if ruta_aux else {}
    tr = Transformador(fuente, graficos, avisos, aux)
    latex = tr.procesar()
    (trabajo / 'tesis_pandoc.tex').write_text(latex, encoding='utf-8')
    diferencias = tr.comparar_con_aux()
    datos = {'tablas': tr.tablas, 'metadatos': metadatos(fuente)}
    (trabajo / 'datos_posproceso.json').write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding='utf-8')
    paso('Transformación lista: %d tablas, %d figuras con leyenda, %d ecuaciones numeradas, %d títulos.'
         % (len(tr.lot), len(tr.lof), tr.c['equation'], tr.n_titulo))

    # 4. bibliografía y pandoc
    bib = trabajo / 'bibliografia.bib'
    info_bib = bibliografia.unir_bib(DIR_TESIS, bib, avisos)
    csl = bibliografia.preparar_csl(AQUI / 'tesis_docx' / 'csl' / 'apa.csl', trabajo / 'apa_es.csl')
    meta = {'lang': 'es-ES', 'link-citations': False, 'abreviaturas-autores': info_bib['abreviaturas'],
            'title': '', 'suppress-bibliography': False}
    (trabajo / 'metadatos.json').write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding='utf-8')
    if args.regenerar_plantilla or not PLANTILLA.is_file():
        paso('Creando la plantilla %s...' % PLANTILLA.name)
        word.crear_plantilla(PLANTILLA, trabajo)
    docx_pandoc = trabajo / 'tesis_pandoc.docx'
    cmd = ['pandoc', str(trabajo / 'tesis_pandoc.tex'), '-f', 'latex', '-t', 'docx', '-o', str(docx_pandoc),
           '--reference-doc', str(PLANTILLA), '--lua-filter', str(AQUI / 'tesis_docx' / 'filtro_apa.lua'),
           '--citeproc', '--bibliography', str(bib), '--csl', str(csl),
           '--metadata-file', str(trabajo / 'metadatos.json'),
           '--lua-filter', str(AQUI / 'tesis_docx' / 'filtro_citas.lua'),
           '--resource-path', '%s:%s' % (trabajo, DIR_TESIS)]
    paso('Ejecutando pandoc (citeproc, APA 7 en español)...')
    r = subprocess.run(cmd, capture_output=True, text=True, errors='replace')
    if r.returncode != 0:
        print(r.stderr)
        sys.exit('pandoc terminó con error.')
    advertencias_pandoc = [l for l in r.stderr.splitlines() if l.strip()]
    import re as _re
    sin_cita = sorted(set(m.group(1) for l in advertencias_pandoc
                          for m in [_re.search(r'citation (\S+) not found', l)] if m))

    # 5. posproceso
    paso('Posproceso con python-docx...')
    pp = word.Posproceso(docx_pandoc, datos, avisos, tabla_pt=args.tabla_pt, formulario_pt=args.formulario_pt)
    pp.ejecutar()
    salida = Path(args.salida).resolve()
    salida.parent.mkdir(parents=True, exist_ok=True)
    pp.guardar(salida)

    # 6. LibreOffice: números de página del índice y PDF
    ruta_pdf = None
    if args.pdf:
        ruta_pdf = (trabajo / (salida.stem + '.pdf')) if args.pdf == 'auto' else Path(args.pdf).resolve()
    if not args.sin_paginas or ruta_pdf:
        paso('Calculando páginas del índice con LibreOffice%s...' % (' y exportando PDF' if ruta_pdf else ''))
        paginas = libreoffice.abrir_con_libreoffice(salida, ruta_pdf, avisos)
        if paginas and not args.sin_paginas:
            n = libreoffice.escribir_paginas(salida, paginas)
            paso('Números de página escritos en %d entradas de los índices.' % n)

    graficos.limpiar_cache()

    # informe
    informe = []
    informe.append('Documento: %s' % salida)
    informe.append('Fuente del .aux: %s (%s)' % (ruta_aux, origen))
    informe.append('Bibliografía: %d entradas de %s' % (info_bib['entradas'], ', '.join(info_bib['archivos'])))
    if ruta_pdf:
        informe.append('PDF de verificación: %s' % ruta_pdf)
    if sin_cita:
        informe.append('Citas sin entrada en los .bib: %s' % ', '.join(sin_cita))
    if tr.refs_faltantes:
        informe.append('Referencias \\ref a etiquetas inexistentes (aparecen como ?? en rojo): %s'
                       % ', '.join(sorted(set(tr.refs_faltantes))))
    if tr.duplicadas:
        informe.append('Etiquetas \\label duplicadas en la fuente (se usa la última, como LaTeX): %s'
                       % ', '.join(sorted(set(tr.duplicadas))))
    if diferencias:
        informe.append('Diferencias entre la numeración calculada y la del .aux (%s): %s'
                       % (origen, '; '.join(diferencias[:15]) + (' ...' if len(diferencias) > 15 else '')))
    desconocidos = tr.comandos_desconocidos(latex)
    if desconocidos:
        informe.append('Comandos LaTeX que pandoc podría ignorar: %s'
                       % ', '.join('%s (%d)' % kv for kv in sorted(desconocidos.items())))
    otros = [l for l in advertencias_pandoc if 'Citeproc: citation' not in l]
    if otros:
        informe.append('Advertencias de pandoc: %s' % ' | '.join(otros[:10]))
    for a in avisos:
        informe.append('Aviso: %s' % a)
    for a in modulo_latex.ERRORES:
        informe.append('Aviso (conversión): %s' % a)
    if graficos.registro:
        informe.append('Errores TikZ: %s' % ' | '.join(graficos.registro))
    texto = '\n'.join(informe)
    (trabajo / 'informe_conversion.txt').write_text(texto + '\n', encoding='utf-8')
    print('\n' + texto)
    paso('Listo.')


if __name__ == '__main__':
    main()
