#!/usr/bin/env python3
"""
Resalta en los PDF de la bibliografía los pasajes citados en la tesis y los archiva.

Para cada ficha de cita (04_Bibliografia/07_Fichas_de_Citas/*.json) cuya clave
BibLaTeX aparece citada en la tesis (05_Tesis_LaTeX/capitulos/*.tex):
  1. busca el texto literal en la página indicada (y en las vecinas);
  2. lo resalta en amarillo y agrega un comentario con: dónde se cita en la tesis,
     la página citable (APA), el uso y la paráfrasis;
  3. guarda una copia anotada en 04_Bibliografia/08_Citas_Resaltadas/<carpeta>/.
     Si el documento tiene más de MAX_PAGINAS_COPIA páginas, guarda solo un
     extracto con la portada y las páginas citadas (para no duplicar archivos
     pesados ni redistribuir obras protegidas completas).
Al final escribe Indice_de_Citas.md, Indice_de_Citas.csv e Indice_de_Citas.xlsx.

Uso: python3 resaltar_citas.py   (desde cualquier carpeta)
"""
from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

import pymupdf  # PyMuPDF

RAIZ = Path(__file__).resolve().parents[3]
FICHAS = RAIZ / "04_Bibliografia" / "07_Fichas_de_Citas"
SALIDA = RAIZ / "04_Bibliografia" / "08_Citas_Resaltadas"
CAPS = RAIZ / "05_Tesis_LaTeX" / "capitulos"
OCR_DIR = SALIDA / "_ocr"            # copias con capa de texto OCR (si existen)
MAX_PAGINAS_COPIA = 60
AMARILLO = (1.0, 0.93, 0.25)

CITA_RE = re.compile(r"\\(?:paren|text|foot)?cites?\*?((?:\[[^\]]*\]){0,2})\{([^}]*)\}")
SECC_RE = re.compile(r"\\(chapter|section|subsection|subsubsection)\*?\{([^}]*)\}")


def ubicaciones_en_tesis() -> dict[str, list[dict]]:
    """Clave -> lista de {archivo, linea, seccion, pagina_citada}."""
    usos: dict[str, list[dict]] = defaultdict(list)
    for tex in sorted(CAPS.glob("*.tex")):
        seccion = {"chapter": "", "section": "", "subsection": ""}
        for n, linea in enumerate(tex.read_text(encoding="utf-8").splitlines(), 1):
            for m in SECC_RE.finditer(linea):
                nivel, titulo = m.group(1), re.sub(r"\\[a-zA-Z]+\s*", "", m.group(2))
                if nivel == "chapter":
                    seccion = {"chapter": titulo, "section": "", "subsection": ""}
                elif nivel == "section":
                    seccion.update(section=titulo, subsection="")
                elif nivel == "subsection":
                    seccion["subsection"] = titulo
            for m in CITA_RE.finditer(linea):
                opciones = re.findall(r"\[([^\]]*)\]", m.group(1))
                pag = opciones[-1] if opciones else ""
                lugar = " > ".join(x for x in (seccion["chapter"], seccion["section"], seccion["subsection"]) if x)
                for clave in [c.strip() for c in m.group(2).split(",") if c.strip()]:
                    usos[clave].append({"archivo": tex.name, "linea": n, "seccion": lugar, "pagina_citada": pag})
    return usos


def cargar_fichas() -> list[dict]:
    fichas = []
    for js in sorted(FICHAS.glob("*.json")):
        try:
            datos = json.loads(js.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"AVISO: no se pudo leer {js.name}: {e}")
            continue
        for f in datos if isinstance(datos, list) else datos.get("fichas", []):
            f["_grupo"] = js.stem
            fichas.append(f)
    return fichas


def buscar(pagina: pymupdf.Page, texto: str):
    """Busca el texto completo y, si no aparece, fragmentos decrecientes."""
    t = " ".join(texto.split())
    for largo in (len(t), 120, 80, 50, 30):
        frag = t[:largo]
        if len(frag) < 15:
            break
        rects = pagina.search_for(frag)
        if rects:
            return rects
    return []


def principal():
    usos = ubicaciones_en_tesis()
    fichas = cargar_fichas()
    por_pdf: dict[str, list[dict]] = defaultdict(list)
    for f in fichas:
        if f.get("clave_bib") in usos and f.get("archivo_pdf"):
            por_pdf[f["archivo_pdf"]].append(f)

    filas_indice = []
    for rel, lista in sorted(por_pdf.items()):
        origen = RAIZ / rel
        ocr = OCR_DIR / origen.name
        fuente = ocr if ocr.exists() else origen
        if not fuente.exists():
            print(f"AVISO: no existe {rel}")
            continue
        doc = pymupdf.open(fuente)
        paginas_citadas = set()
        for f in lista:
            pnum = int(f.get("pagina_pdf") or 1)
            encontrado, pag_real = [], pnum
            for delta in (0, -1, 1, -2, 2):
                k = pnum + delta
                if 1 <= k <= doc.page_count:
                    encontrado = buscar(doc[k - 1], f.get("texto_exacto", ""))
                    if encontrado:
                        pag_real = k
                        break
            lugares = usos[f["clave_bib"]]
            donde = "; ".join(sorted({u["seccion"] or u["archivo"] for u in lugares}))
            nota = (f"TESIS SGC – cita «{f['clave_bib']}» ({f.get('pagina_citable', '')})\n"
                    f"Citado en: {donde}\n"
                    f"Uso: {f.get('uso_sugerido', '')}\n"
                    f"Paráfrasis: {f.get('parafrasis', '')}")
            pagina = doc[pag_real - 1]
            if encontrado:
                annot = pagina.add_highlight_annot(encontrado)
                annot.set_colors(stroke=AMARILLO)
                annot.set_info(title="Tesis SGC", content=nota)
                annot.update()
                estado = "resaltado"
            else:
                estado = "nota (texto no localizado: revisar)"
            icono = pagina.add_text_annot(pymupdf.Point(pagina.rect.width - 24, 24), nota, icon="Comment")
            icono.set_info(title="Tesis SGC")
            icono.update()
            paginas_citadas.add(pag_real)
            filas_indice.append({
                "clave": f["clave_bib"], "documento": origen.name, "carpeta": origen.parent.name,
                "pagina_pdf": pag_real, "pagina_citable": f.get("pagina_citable", ""),
                "tipo": f.get("tipo", ""), "texto": " ".join(str(f.get("texto_exacto", "")).split()),
                "uso_en_tesis": donde, "estado": estado,
            })
        destino_dir = SALIDA / origen.parent.name
        destino_dir.mkdir(parents=True, exist_ok=True)
        if doc.page_count > MAX_PAGINAS_COPIA:
            extracto = pymupdf.open()
            for k in sorted({1} | paginas_citadas):
                extracto.insert_pdf(doc, from_page=k - 1, to_page=k - 1, annots=True)
            destino = destino_dir / f"{origen.stem}__EXTRACTO_CITAS.pdf"
            extracto.save(destino, garbage=4, deflate=True)
        else:
            destino = destino_dir / f"{origen.stem}__CITAS.pdf"
            doc.save(destino, garbage=4, deflate=True)
        for fila in filas_indice:
            if fila["documento"] == origen.name:
                fila["archivo_resaltado"] = str(destino.relative_to(RAIZ))
        print(f"OK {destino.relative_to(RAIZ)} ({len(lista)} citas)")

    # Citas de la tesis sin ficha (para completar a mano)
    claves_con_ficha = {f["clave_bib"] for f in fichas}
    sin_ficha = sorted(k for k in usos if k not in claves_con_ficha)

    campos = ["n", "clave", "documento", "carpeta", "pagina_pdf", "pagina_citable", "tipo",
              "texto", "uso_en_tesis", "estado", "archivo_resaltado"]
    filas_indice.sort(key=lambda r: (r["clave"], r["pagina_pdf"]))
    for i, fila in enumerate(filas_indice, 1):
        fila["n"] = i
    with open(SALIDA / "Indice_de_Citas.csv", "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        w.writerows(filas_indice)
    try:
        from openpyxl import Workbook
        wb = Workbook()
        ws = wb.active
        ws.title = "Citas"
        ws.append(campos)
        for fila in filas_indice:
            ws.append([fila.get(c, "") for c in campos])
        wb.save(SALIDA / "Indice_de_Citas.xlsx")
    except ImportError:
        pass
    with open(SALIDA / "Indice_de_Citas.md", "w", encoding="utf-8") as fh:
        fh.write("# Índice de citas resaltadas\n\n")
        fh.write("Cada fila es un pasaje citado en la tesis y resaltado en su PDF. "
                 "Abre el archivo resaltado y busca el comentario amarillo en la página indicada.\n\n")
        fh.write("| N.º | Clave | Página citable | Página del PDF | Texto resaltado | Dónde se usa en la tesis | Archivo | Estado |\n")
        fh.write("|---|---|---|---|---|---|---|---|\n")
        for r in filas_indice:
            texto = r["texto"][:160] + ("…" if len(r["texto"]) > 160 else "")
            fh.write(f"| {r['n']} | `{r['clave']}` | {r['pagina_citable']} | {r['pagina_pdf']} | {texto} | "
                     f"{r['uso_en_tesis']} | [{Path(r.get('archivo_resaltado', '')).name}]({Path(r.get('archivo_resaltado', '')).relative_to('04_Bibliografia/08_Citas_Resaltadas') if r.get('archivo_resaltado') else ''}) | {r['estado']} |\n")
        if sin_ficha:
            fh.write("\n## Fuentes citadas en la tesis sin pasaje resaltado\n\n")
            fh.write("Son normas de pago, documentos de obra o fuentes citadas de forma general "
                     "(no hay un pasaje concreto que resaltar en un PDF del repositorio):\n\n")
            for k in sin_ficha:
                lugares = "; ".join(sorted({u["seccion"] or u["archivo"] for u in usos[k]}))
                fh.write(f"- `{k}` — {lugares}\n")
    print(f"Índice: {len(filas_indice)} citas; {len(sin_ficha)} claves sin ficha.")


if __name__ == "__main__":
    principal()
