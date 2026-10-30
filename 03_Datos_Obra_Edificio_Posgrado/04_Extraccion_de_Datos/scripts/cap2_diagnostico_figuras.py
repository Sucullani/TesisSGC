#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figuras del diagnóstico de la línea base (Capítulo 2, sección 2.5).

Genera, en 05_Tesis_LaTeX/figuras/:
  - fig_brechas_iso9001.png : cumplimiento documental de ISO 9001:2026 por
    cláusula (lista de verificación C.1 aplicada a la primera losa) y
    comparación con dos diagnósticos de plantas de viguetas pretensadas.
  - fig_pareto_nc.png       : diagrama de Pareto de las no conformidades
    identificadas por el investigador, por categoría (6M + gestión).

Los datos están escritos en este archivo para que el cálculo sea
reproducible y coincida con las tablas de la tesis:
  - CALIFICACIONES reproduce la columna «Calificación» de la lista C.1
    (capitulos/91a_lista_verificacion_iso9001.tex): 1 = cumple,
    0,5 = cumple parcialmente, 0 = no cumple, None = no aplica.
  - NC reproduce la columna «Categoría» de la tabla de no conformidades
    de la sección 2.5.3 (capitulos/30_capitulo2_diseno_sgc.tex).
  - Los porcentajes de comparación provienen de:
      Mamani Calsina (2025, p. 47): 19, 38, 26, 26, 37, 11 y 24 %;
      global 24 % (p. 49) -- planta de viguetas Prensocret.
      Peña Callisaya (2024, p. 71): 30, 60, 26, 47 y 42 % (cláusulas 4 a 8;
      no evaluó 9 ni 10); global 43 % -- planta de viguetas ISOCRET.

Uso:  python3 cap2_diagnostico_figuras.py
Requiere matplotlib y numpy.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

RAIZ = Path(__file__).resolve().parents[3]          # .../TesisSGC
SALIDA = RAIZ / "05_Tesis_LaTeX" / "figuras"
SALIDA.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. Lista de verificación C.1 (calificación por requisito)
# ---------------------------------------------------------------------------
CALIFICACIONES = {
    "4": [("4.1", 0), ("4.2", 0.5), ("4.3", 0), ("4.4", 0.5)],
    "5": [("5.1.1 a", 0), ("5.1.1 b", 0), ("5.1.2", 0.5), ("5.2", 0),
          ("5.3", 0.5)],
    "6": [("6.1 a", 0), ("6.1 b", 0), ("6.2", 0), ("6.3", 0.5)],
    "7": [("7.1.2-7.1.3", 0.5), ("7.1.4", 0), ("7.1.5", 0.5), ("7.1.6", 0),
          ("7.2", 0.5), ("7.3", 0), ("7.4", 0.5), ("7.5.2", 0.5),
          ("7.5.3 a", 0), ("7.5.3 b", 0)],
    "8": [("8.1 a", 0.5), ("8.1 b", 0), ("8.2.2-8.2.3", 0.5), ("8.2.4", 0),
          ("8.3", None), ("8.4.1", 0), ("8.4.2", 0.5), ("8.4.3", 0),
          ("8.5.1 a", 0.5), ("8.5.1 b", 0), ("8.5.2", 0), ("8.5.3", None),
          ("8.5.4", 0), ("8.5.6", 0), ("8.6", 0.5), ("8.7", 0)],
    "9": [("9.1.1 a", 0.5), ("9.1.1 b", 0.5), ("9.1.2", 0.5), ("9.1.3", 0),
          ("9.2", 0), ("9.3", 0)],
    "10": [("10.1", 0), ("10.2.1 a", 0.5), ("10.2.1 b", 0), ("10.2.2", 0),
           ("10.3", 0)],
}
NOMBRES = {"4": "Contexto", "5": "Liderazgo", "6": "Planificación",
           "7": "Apoyo", "8": "Operación", "9": "Evaluación",
           "10": "Mejora"}
MAMANI = {"4": 19, "5": 38, "6": 26, "7": 26, "8": 37, "9": 11, "10": 24,
          "Global": 24}
PENA = {"4": 30, "5": 60, "6": 26, "7": 47, "8": 42, "9": None, "10": None,
        "Global": 43}


def resumen_lista():
    """Devuelve filas (cláusula, n_aplic, n_na, n1, n05, n0, puntaje, %)."""
    filas, tot_p, tot_n = [], 0.0, 0
    for c, reqs in CALIFICACIONES.items():
        aplic = [v for _, v in reqs if v is not None]
        n_na = sum(1 for _, v in reqs if v is None)
        p = sum(aplic)
        filas.append((c, len(aplic), n_na, aplic.count(1), aplic.count(0.5),
                      aplic.count(0), p, 100 * p / len(aplic)))
        tot_p += p
        tot_n += len(aplic)
    return filas, tot_p, tot_n


# ---------------------------------------------------------------------------
# 2. No conformidades identificadas (sección 2.5.3)
# ---------------------------------------------------------------------------
NC = {
    "NC-01": "Medición", "NC-02": "Medición", "NC-03": "Método",
    "NC-04": "Materiales", "NC-05": "Materiales", "NC-06": "Gestión",
    "NC-07": "Gestión", "NC-08": "Materiales", "NC-09": "Gestión",
    "NC-10": "Método", "NC-11": "Gestión", "NC-12": "Medición",
    "NC-13": "Medición", "NC-14": "Medición", "NC-15": "Medición",
    "NC-16": "Materiales", "NC-17": "Método", "NC-18": "Mano de obra",
    "NC-19": "Mano de obra", "NC-20": "Gestión", "NC-21": "Gestión",
    "NC-22": "Medio ambiente",
}
# Orden de desempate fijo (para que la figura no dependa del azar)
ORDEN_CAT = ["Medición", "Gestión", "Materiales", "Método", "Mano de obra",
             "Medio ambiente", "Maquinaria"]

# ---------------------------------------------------------------------------
# Estilo: tinta y paleta de referencia (validada para daltonismo)
# ---------------------------------------------------------------------------
TINTA, TINTA2, TENUE = "#0b0b0b", "#52514e", "#898781"
REJILLA, BASE = "#e1e0d9", "#c3c2b7"
AZUL, NARANJA, AGUA = "#2a78d6", "#eb6834", "#1baf7a"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9,
    "axes.edgecolor": BASE, "axes.labelcolor": TINTA2,
    "xtick.color": TINTA2, "ytick.color": TINTA2,
    "axes.spines.top": False, "axes.spines.right": False,
    "hatch.linewidth": 0.6, "savefig.dpi": 300,
})


def pct(x, _=None):
    return f"{x:.0f} %"


def coma(x, dec=1):
    return f"{x:.{dec}f}".replace(".", ",")


def figura_brechas(filas, global_pct):
    clausulas = [f[0] for f in filas] + ["Global"]
    este = [f[7] for f in filas] + [global_pct]
    mam = [MAMANI[c] for c in clausulas]
    pen = [PENA[c] for c in clausulas]

    x = np.arange(len(clausulas))
    w = 0.26
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.grid(axis="y", color=REJILLA, linewidth=0.6)
    ax.set_axisbelow(True)

    b1 = ax.bar(x - w, este, w * 0.92, color=AZUL, label="Esta tesis (primera losa)")
    ax.bar(x, mam, w * 0.92, color=NARANJA, hatch="////", edgecolor="white",
           linewidth=0, label="Mamani Calsina (2025)")
    pen_val = [v if v is not None else 0 for v in pen]
    b3 = ax.bar(x + w, pen_val, w * 0.92, color=AGUA, hatch="\\\\\\\\",
                edgecolor="white", linewidth=0,
                label="Peña Callisaya (2024)")
    for i, v in enumerate(pen):
        if v is None:
            b3[i].set_visible(False)
            ax.text(x[i] + w, 1.5, "n. e.", ha="center", va="bottom",
                    fontsize=7, color=TENUE, rotation=90)
    # Etiquetas directas solo para la serie principal
    for rect, v in zip(b1, este):
        ax.text(rect.get_x() + rect.get_width() / 2, v + 1.2, coma(v),
                ha="center", va="bottom", fontsize=7.5, color=TINTA)

    ax.set_xticks(x)
    ax.set_xticklabels([f"{c}\n{NOMBRES[c]}" if c in NOMBRES else "Global"
                        for c in clausulas], fontsize=7.5)
    ax.set_ylim(0, 65)
    ax.yaxis.set_major_formatter(FuncFormatter(pct))
    ax.set_ylabel("Cumplimiento de los requisitos")
    ax.axvline(len(clausulas) - 1.5, color=BASE, linewidth=0.8)
    fig.legend(loc="upper center", bbox_to_anchor=(0.55, 0.995),
               frameon=False, fontsize=8, ncol=3, handlelength=1.6,
               columnspacing=1.6)
    fig.subplots_adjust(left=0.10, right=0.99, bottom=0.16, top=0.88)
    ruta = SALIDA / "fig_brechas_iso9001.png"
    fig.savefig(ruta, facecolor="white")
    plt.close(fig)
    return ruta


def figura_pareto():
    conteo = {c: 0 for c in ORDEN_CAT}
    for cat in NC.values():
        conteo[cat] += 1
    cats = sorted([c for c in ORDEN_CAT if conteo[c] > 0],
                  key=lambda c: (-conteo[c], ORDEN_CAT.index(c)))
    n = np.array([conteo[c] for c in cats])
    total = n.sum()
    frac = 100 * n / total
    acum = np.cumsum(frac)

    x = np.arange(len(cats))
    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    ax.grid(axis="y", color=REJILLA, linewidth=0.6)
    ax.set_axisbelow(True)
    barras = ax.bar(x, frac, 0.62, color=AZUL, label="Porcentaje de las no conformidades")
    ax.plot(x, acum, color=NARANJA, linewidth=2, marker="o", markersize=5,
            markeredgecolor="white", markeredgewidth=1.2,
            label="Porcentaje acumulado")
    ax.axhline(80, color=TENUE, linewidth=0.8, linestyle=(0, (4, 3)))
    ax.text(-0.42, 81.5, "80 %", color=TENUE, fontsize=7.5,
            ha="left", va="bottom")
    for rect, k, f in zip(barras, n, frac):
        cx = rect.get_x() + rect.get_width() / 2
        if f >= 12:      # etiqueta dentro de la barra, en blanco
            ax.text(cx, f - 1.5, f"n = {k}\n{coma(f)} %", ha="center",
                    va="top", fontsize=7.5, color="white")
        else:            # barra baja: etiqueta encima
            ax.text(cx, f + 1.2, f"n = {k}\n{coma(f)} %", ha="center",
                    va="bottom", fontsize=7.5, color=TINTA)
    for i, (xi, a) in enumerate(zip(x, acum)):
        if i == 0:
            continue     # coincide con la primera barra
        ax.text(xi - 0.08, a + 2.5, f"{coma(a)} %", fontsize=7.5,
                color=TINTA2, ha="right", va="bottom")
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=8)
    ax.set_ylim(0, 108)
    ax.yaxis.set_major_formatter(FuncFormatter(pct))
    ax.set_ylabel("Porcentaje del total de no conformidades")
    ax.legend(loc="upper left", frameon=False, fontsize=7.5)
    fig.tight_layout()
    ruta = SALIDA / "fig_pareto_nc.png"
    fig.savefig(ruta, facecolor="white")
    plt.close(fig)
    return ruta, list(zip(cats, n, frac, acum)), total


if __name__ == "__main__":
    filas, tot_p, tot_n = resumen_lista()
    global_pct = 100 * tot_p / tot_n
    print("Cláusula  aplic  NA  cumple  parcial  no  puntaje  %")
    for f in filas:
        print(f"{f[0]:>8} {f[1]:6d} {f[2]:3d} {f[3]:7d} {f[4]:8d} {f[5]:3d} "
              f"{f[6]:8.1f} {f[7]:6.1f}")
    print(f"Global: {tot_p:.1f} / {tot_n} = {global_pct:.2f} %; "
          f"media de cláusulas = {np.mean([f[7] for f in filas]):.2f} %")
    print("Figura:", figura_brechas(filas, global_pct))
    ruta, tabla, total = figura_pareto()
    print("Figura:", ruta, "| total NC =", total)
    for c, k, f, a in tabla:
        print(f"  {c:15s} {k:3d} {f:6.1f} % acum {a:6.1f} %")
