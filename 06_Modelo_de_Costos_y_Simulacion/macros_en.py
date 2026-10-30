#!/usr/bin/env python3
"""
Escribe tablas_latex/valores_modelo_en.tex: las cifras clave del modelo con formato
inglés (punto decimal, coma de miles, «%» sin espacio), para el Abstract.

Lee resultados/resumen_resultados.json, que genera modelo_costos.py; este script se
ejecuta automáticamente al final de modelo_costos.py. Uso manual:

    python3 macros_en.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
RES = json.loads((BASE / "resultados" / "resumen_resultados.json").read_text(encoding="utf-8"))
MC = RES["monte_carlo"]


def num(x: float, dec: int = 2) -> str:
    return f"{x:,.{dec}f}"


def pct(x: float, dec: int = 2) -> str:
    return num(100 * x, dec) + r"\%"


valores = {
    "MCiterEN": num(RES["iteraciones"], 0),
    "rMediaEN": pct(MC["r"]["media"]),
    "PRposEN": num(RES["contraste"]["P(r>0)"], 4),
    "PHGEN": num(RES["contraste"]["HG"]["P(r>=umbral)"], 4),
    "CNCreduccionPctEN": pct(1 - MC["CNC_con"]["media"] / MC["CNC_sin"]["media"]),
}

texto = "% Archivo generado por macros_en.py (desde modelo_costos.py): no editar a mano.\n"
texto += "".join(f"\\newcommand{{\\{k}}}{{{v}}}\n" for k, v in valores.items())
(BASE / "tablas_latex" / "valores_modelo_en.tex").write_text(texto, encoding="utf-8")
print(texto)
