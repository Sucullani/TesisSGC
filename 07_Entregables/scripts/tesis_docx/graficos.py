# -*- coding: utf-8 -*-
"""Conversión de figuras para Word: TikZ, \\includegraphics e \\includepdf.

* Las figuras TikZ se compilan con pdflatex usando EL MISMO preámbulo de la
  tesis (paquetes, bibliotecas TikZ, letra y macros) y el paquete «preview»,
  que recorta cada tikzpicture en una página propia.  Luego cada página se
  convierte a PNG.
* Los PDF de \\includegraphics se convierten a PNG; los PNG/JPG se usan tal cual.
* Las páginas de \\includepdf (planos, certificados, cómputos) se convierten a PNG.

Todo se guarda en una caché (carpeta de trabajo) indexada por el contenido, de
modo que una segunda ejecución solo recompila lo que cambió.
"""

import hashlib
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

import pymupdf
from PIL import Image

VERSION_CACHE = '3'


def _hash(*partes):
    h = hashlib.sha256()
    for p in partes:
        h.update(p.encode('utf-8') if isinstance(p, str) else p)
    return h.hexdigest()[:20]


def entorno_tex():
    env = dict(os.environ)
    # Evita que kpathsea intente generar fuentes (y deje missfont.log en 05_Tesis_LaTeX)
    env.update({'MKTEXTFM': '0', 'MKTEXPK': '0', 'MKTEXMF': '0', 'MKTEXTEX': '0'})
    return env


class Graficos:
    def __init__(self, dir_tesis, dir_trabajo, fuente, avisos, dpi_tikz=300, dpi_pdf=150, dpi_img=300):
        self.dir_tesis = Path(dir_tesis).resolve()
        dir_trabajo = Path(dir_trabajo).resolve()
        self.dir = dir_trabajo / 'imagenes'
        self.dir.mkdir(parents=True, exist_ok=True)
        self.dir_tikz = Path(dir_trabajo) / 'tikz'
        self.dir_tikz.mkdir(parents=True, exist_ok=True)
        self.f = fuente
        self.avisos = avisos
        self.dpi_tikz = dpi_tikz
        self.dpi_pdf = dpi_pdf
        self.dpi_img = dpi_img
        self.registro = []
        self.usados = set()

    # ------------------------------------------------------------------
    def resolver(self, nombre, extensiones=('.pdf', '.png', '.jpg', '.jpeg', '.PDF', '.PNG', '.JPG')):
        nombre = nombre.strip().strip('"')
        rutas = [''] + list(self.f.graphicspath)
        candidatos = []
        for base in rutas:
            p = self.dir_tesis / base / nombre
            if Path(nombre).suffix:
                candidatos.append(p)
            else:
                candidatos += [Path(str(p) + e) for e in extensiones]
        for c in candidatos:
            if c.is_file():
                return c.resolve()
        return None

    @staticmethod
    def _opciones(texto):
        op = {}
        for parte in re.split(r',(?![^{]*\})', texto or ''):
            if not parte.strip():
                continue
            k, _, v = parte.partition('=')
            v = v.strip()
            if v.startswith('{') and v.endswith('}'):
                v = v[1:-1]
            op[k.strip()] = v if _ else True
        return op

    @staticmethod
    def _recortar_blanco(png, ancho_cm, alto_cm, margen=0.015):
        """Recorta los márgenes blancos de un plano (deja un 1,5 % de margen)."""
        from PIL import ImageChops, ImageOps
        with Image.open(png) as im:
            gris = ImageOps.invert(im.convert('L'))
            gris = gris.point(lambda v: 255 if v > 25 else 0)
            caja = gris.getbbox()
            if not caja:
                return ancho_cm, alto_cm
            w, h = im.size
            mx, my = int(w * margen), int(h * margen)
            caja = (max(0, caja[0] - mx), max(0, caja[1] - my), min(w, caja[2] + mx), min(h, caja[3] + my))
            if (caja[2] - caja[0]) * (caja[3] - caja[1]) > 0.92 * w * h:
                return ancho_cm, alto_cm
            im.crop(caja).save(png)
        return ancho_cm * (caja[2] - caja[0]) / w, alto_cm * (caja[3] - caja[1]) / h

    def _pdf_a_png(self, ruta_pdf, pagina, dpi, prefijo, recortar=False):
        st = ruta_pdf.stat()
        clave = _hash(VERSION_CACHE, str(ruta_pdf), str(st.st_size), str(int(st.st_mtime)), str(pagina), str(dpi),
                      str(recortar))
        destino = self.dir / ('%s_%s.png' % (prefijo, clave))
        meta = destino.with_suffix('.json')
        self.usados.update({destino.name, meta.name})
        if destino.is_file() and meta.is_file():
            return destino, json.loads(meta.read_text())
        doc = pymupdf.open(str(ruta_pdf))
        if pagina < 1 or pagina > doc.page_count:
            doc.close()
            return None, None
        pg = doc[pagina - 1]
        pix = pg.get_pixmap(dpi=dpi, alpha=False)
        pix.save(str(destino))
        ancho_cm, alto_cm = pg.rect.width / 72 * 2.54, pg.rect.height / 72 * 2.54
        if recortar:
            ancho_cm, alto_cm = self._recortar_blanco(destino, ancho_cm, alto_cm)
        info = {'ancho_cm': ancho_cm, 'alto_cm': alto_cm, 'px': [pix.width, pix.height]}
        meta.write_text(json.dumps(info))
        doc.close()
        return destino, info

    # ------------------------------------------------------------------
    def imagen(self, nombre, opciones):
        """Devuelve (png, ancho_cm, alto_cm) según las opciones de \\includegraphics."""
        from .latex import a_cm
        ruta = self.resolver(nombre)
        if not ruta:
            self.avisos.append('No se encontró la imagen «%s».' % nombre)
            return None
        op = self._opciones(opciones)
        if ruta.suffix.lower() == '.pdf':
            pagina = int(op.get('page', 1)) if str(op.get('page', 1)).isdigit() else 1
            png, info = self._pdf_a_png(ruta, pagina, self.dpi_img, 'graf')
            if not png:
                return None
            nat_w, nat_h = info['ancho_cm'], info['alto_cm']
        else:
            png = ruta
            with Image.open(ruta) as im:
                dpi = im.info.get('dpi', (72, 72))[0] or 72
                nat_w = im.width / float(dpi) * 2.54
                nat_h = im.height / float(dpi) * 2.54
            if ruta.suffix.lower() not in ('.png', '.jpg', '.jpeg'):
                destino = self.dir / ('graf_%s.png' % _hash(str(ruta)))
                self.usados.add(destino.name)
                with Image.open(ruta) as im:
                    im.convert('RGB').save(destino)
                png = destino
        angulo = op.get('angle')
        if angulo and str(angulo).strip() not in ('0', ''):
            try:
                a = float(angulo)
                destino = self.dir / ('rot_%s.png' % _hash(str(png), str(a)))
                self.usados.add(destino.name)
                if not destino.is_file():
                    with Image.open(png) as im:
                        im.rotate(a, expand=True, fillcolor='white').save(destino)
                png = destino
                if abs(a) % 180 == 90:
                    nat_w, nat_h = nat_h, nat_w
            except ValueError:
                pass
        ancho = a_cm(op.get('width')) if op.get('width') else None
        alto = a_cm(op.get('height')) if op.get('height') else None
        if ancho is None and alto is not None:
            ancho = alto * nat_w / nat_h
        if ancho is None:
            try:
                ancho = nat_w * float(op.get('scale', 1))
            except ValueError:
                ancho = nat_w
        return str(png), ancho, ancho * nat_h / nat_w

    # ------------------------------------------------------------------
    def paginas_pdf(self, nombre, opciones):
        """Páginas de \\includepdf -> [(png, ancho_cm, alto_cm, horizontal)]."""
        ruta = self.resolver(nombre, extensiones=('.pdf', '.PDF'))
        if not ruta:
            self.avisos.append('No se encontró el PDF de \\includepdf: «%s».' % nombre)
            return []
        op = self._opciones(opciones)
        doc = pymupdf.open(str(ruta))
        total = doc.page_count
        doc.close()
        paginas = []
        espec = str(op.get('pages', '1')).replace(' ', '')
        for parte in espec.split(','):
            if not parte or parte == '{}':
                continue
            if parte == '-':
                paginas += list(range(1, total + 1))
            elif '-' in parte:
                a, b = parte.split('-', 1)
                a = int(a) if a else 1
                b = total if b in ('', 'last') else int(b)
                paginas += list(range(a, b + 1))
            elif parte == 'last':
                paginas.append(total)
            elif parte.isdigit():
                paginas.append(int(parte))
        res = []
        for p in paginas:
            png, info = self._pdf_a_png(ruta, p, self.dpi_pdf, 'pdfpag', recortar=True)
            if not png:
                self.avisos.append('La página %d de %s no existe.' % (p, ruta.name))
                continue
            w, h = info['ancho_cm'], info['alto_cm']
            res.append((str(png), w, h, w > h))
        return res

    # ------------------------------------------------------------------
    def _documento_tikz(self, codigos):
        cuerpo = []
        for c in codigos:
            cuerpo.append('\\begingroup\\setstretch{1}\\centering\n%s\n\\endgroup\n\\clearpage\n' % c)
        return ('\\documentclass[12pt,letterpaper,oneside]{report}\n' + self.f.preambulo +
                '\n\\usepackage[active,tightpage]{preview}\n\\PreviewEnvironment{tikzpicture}\n'
                '\\setlength\\PreviewBorder{3pt}\n\\begin{document}\n\\pagestyle{empty}\n' +
                ''.join(cuerpo) + '\\end{document}\n')

    def _compilar(self, nombre, codigos):
        tex = self.dir_tikz / (nombre + '.tex')
        tex.write_text(self._documento_tikz(codigos), encoding='utf-8')
        pdf = self.dir_tikz / (nombre + '.pdf')
        if pdf.exists():
            pdf.unlink()
        cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-output-directory',
               str(self.dir_tikz), '-jobname', nombre, str(tex)]
        try:
            r = subprocess.run(cmd, cwd=str(self.dir_tesis), env=entorno_tex(), capture_output=True,
                               text=True, errors='replace', timeout=600)
        except subprocess.TimeoutExpired:
            return None
        if not pdf.is_file():
            log = self.dir_tikz / (nombre + '.log')
            if log.is_file():
                err = re.findall(r'^! .*$', log.read_text(errors='replace'), flags=re.M)
                self.registro.append('%s: %s' % (nombre, '; '.join(err[:3])))
            return None
        doc = pymupdf.open(str(pdf))
        if doc.page_count != len(codigos):
            doc.close()
            return None
        return doc

    def compilar_tikz(self, codigos):
        """Devuelve, para cada código, (png, ancho_cm, alto_cm) o None si falló."""
        resultados = [None] * len(codigos)
        claves = [_hash(VERSION_CACHE, self.f.preambulo, c, str(self.dpi_tikz)) for c in codigos]
        faltan = []
        for k, clave in enumerate(claves):
            png = self.dir_tikz / ('tikz_%s.png' % clave)
            meta = png.with_suffix('.json')
            self.usados.update({png.name, meta.name})
            if png.is_file() and meta.is_file():
                info = json.loads(meta.read_text())
                resultados[k] = (str(png), info['ancho_cm'], info['alto_cm'])
            else:
                faltan.append(k)
        if not faltan:
            return resultados

        def guardar(doc, indices):
            for j, k in enumerate(indices):
                pg = doc[j]
                pix = pg.get_pixmap(dpi=self.dpi_tikz, alpha=False)
                png = self.dir_tikz / ('tikz_%s.png' % claves[k])
                pix.save(str(png))
                info = {'ancho_cm': pg.rect.width / 72 * 2.54, 'alto_cm': pg.rect.height / 72 * 2.54}
                png.with_suffix('.json').write_text(json.dumps(info))
                resultados[k] = (str(png), info['ancho_cm'], info['alto_cm'])
            doc.close()

        doc = self._compilar('figuras_tikz', [codigos[k] for k in faltan])
        if doc:
            guardar(doc, faltan)
        else:
            # Se compila cada figura por separado para aislar la que falla
            for k in faltan:
                d = self._compilar('figura_tikz_%d' % (k + 1), [codigos[k]])
                if d:
                    guardar(d, [k])
                else:
                    self.avisos.append('No se pudo compilar la figura TikZ n.º %d (ver %s).'
                                       % (k + 1, self.dir_tikz / ('figura_tikz_%d.log' % (k + 1))))
        return resultados

    def limpiar_cache(self):
        """Borra de la caché las imágenes que ya no usa la tesis (versiones anteriores)."""
        n = 0
        for carpeta, prefijos in ((self.dir, ('graf_', 'pdfpag_', 'rot_')), (self.dir_tikz, ('tikz_',))):
            for f in carpeta.iterdir():
                if f.name.startswith(prefijos) and f.name not in self.usados:
                    f.unlink()
                    n += 1
        return n
