#!/usr/bin/env python3
"""Análisis de robustez: corre el modelo con variantes de supuestos clave.

Cada variante modifica una copia de parametros.json y ejecuta modelo_costos.py en
modo resumen. Escribe tablas_latex/tab_variantes.tex y resultados/variantes.json.
"""
import copy
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BASE = json.loads((AQUI / "parametros.json").read_text(encoding="utf-8"))


def correr(params):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
        json.dump(params, fh, ensure_ascii=False)
        ruta = fh.name
    env = dict(os.environ, MODELO_PARAMS=ruta, MODELO_SOLO_RESUMEN="1")
    out = subprocess.run([sys.executable, str(AQUI / "modelo_costos.py")], env=env,
                         capture_output=True, text=True, check=True).stdout
    os.unlink(ruta)
    return json.loads(out.strip().splitlines()[-1])


def v_sin_ensayos(p):
    p["costos_sgc"]["componentes"].pop("ensayos", None)
    return p


def v_mano_obra_alcon(p):
    for it in p["apu_referencia"]["item13"]["mano_obra"]:
        if it["insumo"] == "Albañil":
            it["cantidad"] = 1.00
        if it["insumo"] == "Ayudante":
            it["cantidad"] = 1.00
    return p


def v_eficacia_baja(p):
    for m in p["materiales"].values():
        e = m["eficacia_sgc"]
        e["min"], e["moda"], e["max"] = e["min"], e["min"] + (e["moda"] - e["min"]) / 2, e["moda"]
    r = p["retrabajo"]["eficacia_sgc"]
    r["min"], r["moda"], r["max"] = r["min"], r["min"] + (r["moda"] - r["min"]) / 2, r["moda"]
    return p


def v_costo_sgc_doble(p):
    for c in p["costos_sgc"]["componentes"].values():
        for k in ("min", "moda", "max"):
            c["Bs_total"][k] *= 2
    return p


def v_desperdicio_alto(p):
    for clave in ("hormigon", "acero"):
        d = p["materiales"][clave]["idm_sin_sgc"]
        d["moda"] = (d["moda"] + d["max"]) / 2
    return p


VARIANTES = [
    ("Caso principal", lambda p: p),
    ("Sin ensayos de hormigón en el costo del SGC (obligación contractual)", v_sin_ensayos),
    ("Mano de obra del APU según Alcón (2009): 1,00 h/m² de albañil y de ayudante", v_mano_obra_alcon),
    ("Eficacia del SGC más baja (moda y máximo reducidos)", v_eficacia_baja),
    ("Costo del SGC duplicado", v_costo_sgc_doble),
    ("Desperdicio de hormigón y acero más alto (moda desplazada al máximo)", v_desperdicio_alto),
]


def fmt(x, d=2):
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


res = []
for nombre, f in VARIANTES:
    r = correr(f(copy.deepcopy(BASE)))
    res.append({"variante": nombre, **r})
    print(nombre, {k: round(v, 4) for k, v in r.items()})

(AQUI / "resultados" / "variantes.json").write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
filas = "\n".join(
    f"{v['variante']} & {fmt(100*v['r_media'])}~\\% & {fmt(100*v['r_p05'])}~\\% & {fmt(v['P_pos'],3)} & "
    f"{fmt(v['P_umbral'],3)} & {fmt(100*v['r_max'])}~\\% \\\\" for v in res)
(AQUI / "tablas_latex" / "tab_variantes.tex").write_text(
    "\\begin{tabularx}{\\linewidth}{@{}Lrrrrr@{}}\n\\toprule\n"
    "\\textbf{Variante} & \\textbf{$r$ media} & \\textbf{$r$ P5} & \\textbf{$P(r>0)$} & "
    "\\textbf{$P(r \\geq 5~\\%)$} & \\textbf{$r$ con eficacia 100~\\%} \\\\\n\\midrule\n"
    + filas + "\n\\bottomrule\n\\end{tabularx}\n", encoding="utf-8")
