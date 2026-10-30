#!/usr/bin/env python3
"""
Genera la EXPLICACIÓN DE LA TESIS PARA TODO PÚBLICO en Word y PDF (lenguaje coloquial).

Entrada:  07_Entregables/Explicacion_Para_Todo_Publico/partes/*.md (un archivo por capítulo, en orden)
Salida:   07_Entregables/Explicacion_Para_Todo_Publico/Tesis_SGC_Version_Sencilla.md   (texto unido)
          07_Entregables/Explicacion_Para_Todo_Publico/Tesis_SGC_Version_Sencilla.docx (Word con índice)
          07_Entregables/Explicacion_Para_Todo_Publico/Tesis_SGC_Version_Sencilla.pdf  (PDF con índice paginado)

Uso (desde la raíz del repositorio):
    python3 07_Entregables/Explicacion_Para_Todo_Publico/generar_version_sencilla.py

Requiere pandoc, python-docx y LibreOffice (para el PDF).
"""
from __future__ import annotations

import re
import shutil
import socket
import subprocess
import tempfile
import time
from pathlib import Path

from docx import Document
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
PARTES = AQUI / "partes"
NOMBRE = "Tesis_Explicada_para_Todo_Publico"
MD = AQUI / f"{NOMBRE}.md"
DOCX = AQUI / f"{NOMBRE}.docx"
PDF = AQUI / f"{NOMBRE}.pdf"
REF = AQUI / "estilo_explicacion.docx"

AZUL = RGBColor(0x1F, 0x38, 0x64)
AZUL_MEDIO = RGBColor(0x2E, 0x5C, 0x8A)
FUENTE = "Calibri"  # en LibreOffice se sustituye por Carlito (mismas medidas)

METADATOS = """---
title: "Diseño de un Sistema de Gestión de la Calidad basado en la norma ISO 9001 para reducir costos mediante el control de materiales en losas alivianadas con viguetas pretensadas del Edificio de Posgrado de la Universidad Autónoma Tomás Frías, Potosí"
subtitle: "La tesis explicada para todo público"
date: "Universidad Autónoma Tomás Frías · Facultad de Ingeniería · Carrera de Ingeniería Civil · Potosí, 2026"
lang: es-BO
toc-title: "Contenido"
---

"""


# ---------------------------------------------------------------------------
def unir_partes() -> str:
    partes = sorted(PARTES.glob("*.md"))
    if not partes:
        raise SystemExit("No hay partes en " + str(PARTES))
    textos = []
    for p in partes:
        t = p.read_text(encoding="utf-8").strip()
        # sin marcas de tareas pendientes ni instrucciones al autor
        t = re.sub(r"\\(pendiente|guia)\{[^}]*\}", "", t)
        textos.append(t)
    texto = METADATOS + "\n\n".join(textos) + "\n"
    MD.write_text(texto, encoding="utf-8")
    return texto


# ---------------------------------------------------------------------------
def _fuente(estilo, nombre=FUENTE, tam=None, negrita=None, cursiva=None, color=None):
    f = estilo.font
    f.name = nombre
    rpr = estilo.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(a), nombre)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        if rfonts.get(qn(a)) is not None:
            del rfonts.attrib[qn(a)]
    if tam:
        f.size = Pt(tam)
    if negrita is not None:
        f.bold = negrita
    if cursiva is not None:
        f.italic = cursiva
    if color is not None:
        f.color.rgb = color


def _sombreado(estilo, relleno="EAF1FB", borde="2E5C8A"):
    ppr = estilo.element.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), relleno)
    ppr.append(shd)
    bdr = OxmlElement("w:pBdr")
    izq = OxmlElement("w:left")
    for k, v in (("w:val", "single"), ("w:sz", "24"), ("w:space", "8"), ("w:color", borde)):
        izq.set(qn(k), v)
    bdr.append(izq)
    ppr.append(bdr)


def crear_estilo():
    """Plantilla de estilos legible (letra grande, títulos en azul, recuadros sombreados)."""
    datos = subprocess.run(["pandoc", "-o", str(REF), "--print-default-data-file", "reference.docx"],
                           capture_output=True)
    if datos.returncode != 0:
        raise SystemExit(datos.stderr.decode())
    doc = Document(str(REF))
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.59), Cm(27.94)  # carta
    for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, m, Cm(2.5))
    estilos = {s.name: s for s in doc.styles}

    class _E(dict):
        def __getitem__(self, k):
            return estilos[k]

        def __iter__(self):
            return iter(estilos.values())
    est = _E()
    for nombre in ("Normal", "Body Text", "First Paragraph", "Compact"):
        if nombre in estilos:
            s = est[nombre]
            _fuente(s, tam=12)
            pf = s.paragraph_format
            pf.line_spacing = 1.3
            pf.space_after = Pt(8)
            pf.space_before = Pt(0)
    est["Compact"].paragraph_format.space_after = Pt(2)
    _fuente(est["Title"], tam=24, negrita=True, color=AZUL)
    est["Title"].paragraph_format.space_before = Pt(120)
    est["Title"].paragraph_format.space_after = Pt(24)
    _fuente(est["Subtitle"], tam=16, cursiva=False, color=AZUL_MEDIO)
    est["Subtitle"].paragraph_format.space_after = Pt(36)
    if "Date" in estilos:
        _fuente(est["Date"], tam=12, color=AZUL)
    for nombre, tam, color, antes in (("Heading 1", 20, AZUL, 0), ("Heading 2", 15, AZUL_MEDIO, 18),
                                     ("Heading 3", 13, AZUL_MEDIO, 12)):
        s = est[nombre]
        _fuente(s, tam=tam, negrita=True, cursiva=False, color=color)
        s.paragraph_format.space_before = Pt(antes)
        s.paragraph_format.space_after = Pt(8)
        s.paragraph_format.keep_with_next = True
    est["Heading 1"].paragraph_format.page_break_before = True
    if "Block Text" in estilos:
        s = est["Block Text"]
        _fuente(s, tam=12, color=RGBColor(0x1A, 0x1A, 0x1A))
        s.paragraph_format.left_indent = Cm(0.4)
        s.paragraph_format.right_indent = Cm(0.4)
        s.paragraph_format.space_before = Pt(6)
        s.paragraph_format.space_after = Pt(10)
        _sombreado(s)
    for nombre in ("Image Caption", "Table Caption", "Caption"):
        if nombre in estilos:
            _fuente(est[nombre], tam=10.5, cursiva=False, color=RGBColor(0x33, 0x33, 0x33))
    if "TOC Heading" in estilos:
        _fuente(est["TOC Heading"], tam=20, negrita=True, color=AZUL)
    doc.save(str(REF))


# ---------------------------------------------------------------------------
def pandoc_docx():
    r = subprocess.run(["pandoc", str(MD), "-o", str(DOCX), "--toc", "--toc-depth=2",
                        "--reference-doc", str(REF), "--resource-path", f"{RAIZ}:{AQUI}",
                        "--from", "markdown+pipe_tables+grid_tables+link_attributes"],
                       cwd=RAIZ, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr)
    if r.stderr.strip():
        print(r.stderr.strip())


def _borde_tabla(tbl):
    tblpr = tbl._tbl.tblPr
    bordes = OxmlElement("w:tblBorders")
    for lado in ("top", "bottom", "insideH"):
        b = OxmlElement(f"w:{lado}")
        for k, v in (("w:val", "single"), ("w:sz", "6"), ("w:space", "0"), ("w:color", "8EA9C8")):
            b.set(qn(k), v)
        bordes.append(b)
    tblpr.append(bordes)
    ancho = OxmlElement("w:tblW")
    ancho.set(qn("w:w"), "5000")
    ancho.set(qn("w:type"), "pct")
    for viejo in tblpr.findall(qn("w:tblW")):
        tblpr.remove(viejo)
    tblpr.append(ancho)


def posproceso():
    doc = Document(str(DOCX))
    # tablas: bordes suaves, ancho completo, letra un poco menor y encabezado en negrita
    for tbl in doc.tables:
        _borde_tabla(tbl)
        for i, fila in enumerate(tbl.rows):
            for celda in fila.cells:
                for p in celda.paragraphs:
                    p.paragraph_format.line_spacing = 1.1
                    p.paragraph_format.space_after = Pt(2)
                    for run in p.runs:
                        run.font.size = Pt(10.5)
                        if i == 0:
                            run.font.bold = True
    # salto de página después de la portada (antes del índice)
    for p in doc.paragraphs:
        if p.style.name == "Date":
            p.add_run().add_break(WD_BREAK.PAGE)
            break
    # número de página centrado al pie
    pie = doc.sections[0].footer.paragraphs[0]
    pie.alignment = 1
    run = pie.add_run()
    for tipo, texto in (("begin", None), (None, "PAGE"), ("end", None)):
        if tipo:
            f = OxmlElement("w:fldChar")
            f.set(qn("w:fldCharType"), tipo)
            run._r.append(f)
        else:
            it = OxmlElement("w:instrText")
            it.set(qn("xml:space"), "preserve")
            it.text = texto
            run._r.append(it)
    # que Word actualice el índice al abrir el archivo
    ajustes = doc.settings.element
    uf = OxmlElement("w:updateFields")
    uf.set(qn("w:val"), "true")
    ajustes.append(uf)
    doc.save(str(DOCX))


# ---------------------------------------------------------------------------
def pdf_con_libreoffice():
    """Abre el Word en LibreOffice, actualiza el índice y exporta el PDF."""
    try:
        import uno
        from com.sun.star.beans import PropertyValue
    except ImportError:
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(AQUI), str(DOCX)],
                       check=True)
        return

    def pv(n, v):
        p = PropertyValue()
        p.Name, p.Value = n, v
        return p

    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    puerto = s.getsockname()[1]
    s.close()
    perfil = tempfile.mkdtemp(prefix="lo_exp_")
    proc = subprocess.Popen(["soffice", "--headless", "--invisible", "--nologo", "--norestore", "--nodefault",
                             f"-env:UserInstallation={Path(perfil).as_uri()}",
                             f"--accept=socket,host=127.0.0.1,port={puerto};urp;StarOffice.ComponentContext"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        local = uno.getComponentContext()
        resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
        ctx, t0 = None, time.time()
        while ctx is None and time.time() - t0 < 60:
            try:
                ctx = resolver.resolve(f"uno:socket,host=127.0.0.1,port={puerto};urp;StarOffice.ComponentContext")
            except Exception:
                time.sleep(0.5)
        escritorio = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
        doc = escritorio.loadComponentFromURL(DOCX.resolve().as_uri(), "_blank", 0,
                                              (pv("Hidden", True), pv("UpdateDocMode", 3)))
        indices = doc.getDocumentIndexes()
        for i in range(indices.getCount()):
            indices.getByIndex(i).update()
        doc.getTextFields().refresh()
        doc.storeToURL(PDF.resolve().as_uri(), (pv("FilterName", "writer_pdf_Export"),))
        doc.close(True)
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=20)
        except Exception:
            proc.kill()
        shutil.rmtree(perfil, ignore_errors=True)


def main():
    texto = unir_partes()
    print(f"Texto unido: {len(texto.split()):,} palabras".replace(",", "."))
    crear_estilo()
    pandoc_docx()
    posproceso()
    pdf_con_libreoffice()
    print("Listo:", DOCX.relative_to(RAIZ), "y", PDF.relative_to(RAIZ))


if __name__ == "__main__":
    main()
