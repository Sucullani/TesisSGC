# -*- coding: utf-8 -*-
"""Compilación de la tesis con latexmk en una carpeta temporal (solo para el .aux).

El .aux da los números «oficiales» de LaTeX (tablas, figuras, ecuaciones,
secciones y anexos).  Si la compilación falla porque otro autor está editando
un archivo, se usa el último .aux válido guardado en la caché.
Nunca se escribe dentro de 05_Tesis_LaTeX (se usa -outdir/-auxdir y se
desactiva la generación de fuentes, que dejaría un missfont.log).
"""

import shutil
import subprocess
import time
from pathlib import Path

from .graficos import entorno_tex
from .latex import aux_completo


def compilar_tesis(dir_tesis, dir_trabajo, avisos, usar_latexmk=True, timeout=900):
    """Devuelve (ruta_aux, descripcion_origen)."""
    dir_tesis = Path(dir_tesis).resolve()
    salida = Path(dir_trabajo).resolve() / 'latex'
    cache = Path(dir_trabajo).resolve() / 'aux_valido'
    salida.mkdir(parents=True, exist_ok=True)
    cache.mkdir(parents=True, exist_ok=True)
    aux = salida / 'tesis.aux'
    if aux.exists():
        aux.unlink()
    ok = False
    if usar_latexmk and shutil.which('latexmk'):
        cmd = ['latexmk', '-pdf', '-f', '-interaction=nonstopmode', '-outdir=%s' % salida,
               '-auxdir=%s' % salida, 'tesis.tex']
    else:
        cmd = ['pdflatex', '-draftmode', '-interaction=nonstopmode', '-output-directory', str(salida), 'tesis.tex']
    t0 = time.time()
    try:
        r = subprocess.run(cmd, cwd=str(dir_tesis), env=entorno_tex(), capture_output=True, text=True,
                           errors='replace', timeout=timeout)
        (salida / 'compilacion_salida.txt').write_text(r.stdout + '\n' + r.stderr, encoding='utf-8')
    except subprocess.TimeoutExpired:
        avisos.append('La compilación LaTeX superó %d s y se interrumpió.' % timeout)
    except FileNotFoundError as e:
        avisos.append('No se pudo ejecutar %s: %s' % (cmd[0], e))
    ok = aux_completo(aux)
    duracion = time.time() - t0
    log = salida / 'tesis.log'
    errores = []
    if log.is_file():
        texto = log.read_text(errors='replace')
        errores = sorted(set(l for l in texto.splitlines() if l.startswith('! ')))
    if ok:
        for ext in ('aux', 'toc', 'lot', 'lof', 'log'):
            p = salida / ('tesis.' + ext)
            if p.is_file():
                shutil.copy2(p, cache / p.name)
        if errores:
            avisos.append('LaTeX terminó con %d tipo(s) de error no fatal (p. ej. «%s»); el .aux está completo.'
                          % (len(errores), errores[0][:100]))
        return aux, 'compilación nueva (%.0f s)' % duracion
    if (cache / 'tesis.aux').is_file():
        avisos.append('La compilación LaTeX no terminó (%s); se usa el último .aux válido de la caché.'
                      % ('; '.join(errores[:2]) or 'sin detalle'))
        return cache / 'tesis.aux', 'último .aux válido (caché)'
    respaldo = dir_tesis / 'build' / 'tesis.aux'
    if aux_completo(respaldo):
        avisos.append('La compilación LaTeX no terminó; se usa 05_Tesis_LaTeX/build/tesis.aux (puede estar desactualizado).')
        return respaldo, '05_Tesis_LaTeX/build/tesis.aux'
    if aux.is_file():
        avisos.append('La compilación LaTeX no terminó; se usa un .aux parcial.')
        return aux, '.aux parcial'
    avisos.append('No hay .aux disponible: la numeración se calcula solo desde la fuente.')
    return None, 'sin .aux'
