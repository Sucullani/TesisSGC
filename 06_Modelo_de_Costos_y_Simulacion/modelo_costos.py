#!/usr/bin/env python3
"""
Modelo de costos y simulación de Monte Carlo del SGC propuesto
Tesis: Diseño de un SGC basado en ISO 9001 para reducir costos mediante el
control de materiales en losas alivianadas con viguetas pretensadas
(Edificio de Posgrado, UATF, Potosí).

Qué hace (en orden):
  1. Lee los parámetros documentados en parametros.json (cada valor trae su fuente).
  2. Calcula la línea base determinista (O1) y el escenario con SGC (X) con los
     valores más probables (modas).
  3. Simula N escenarios (Monte Carlo) del costo unitario de ejecución de la losa
     a precios constantes del contrato, sin SGC (control) y con SGC (tratamiento).
  4. Contrasta las hipótesis con reglas de decisión probabilísticas:
        HG : se acepta si P(r >= umbral) >= nivel de confianza
        HE1: se acepta si P(IDM_con < IDM_sin) >= nivel de confianza
        HE2: se acepta si P(CNC_con < CNC_sin) >= nivel de confianza
  5. Analiza la sensibilidad (correlación de rangos de Spearman y variación de un
     factor a la vez), el punto de equilibrio y la convergencia de la simulación.
  6. Escribe resultados (JSON, CSV), tablas LaTeX y figuras (PDF y PNG).

Uso:  python3 modelo_costos.py            (desde esta carpeta)
Requisitos: numpy, scipy, matplotlib.
"""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np
from scipy import stats

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

AQUI = Path(__file__).resolve().parent
FIG = AQUI / "figuras"
RES = AQUI / "resultados"
TEX = AQUI / "tablas_latex"
for d in (FIG, RES, TEX):
    d.mkdir(exist_ok=True)

import os
SOLO_RESUMEN = os.environ.get("MODELO_SOLO_RESUMEN") == "1"
P = json.loads(Path(os.environ.get("MODELO_PARAMS", AQUI / "parametros.json")).read_text(encoding="utf-8"))
SIM = P["simulacion"]
N = int(SIM["iteraciones"])
RNG = np.random.default_rng(int(SIM["semilla"]))
UMBRAL = float(SIM["umbral_reduccion"])
CONF = float(SIM["nivel_confianza"])

MATS = list(P["materiales"].keys())


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def fmt(x: float, dec: int = 2) -> str:
    """Número con coma decimal y punto de miles (formato boliviano)."""
    s = f"{x:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def tex(texto) -> str:
    """Escapa caracteres especiales de LaTeX en textos de fuentes y descripciones."""
    t = str(texto)
    for a, b in (("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("#", r"\#"),
                 ("_", r"\_"), ("$", r"\$"), ("~", r"\textasciitilde{}")):
        t = t.replace(a, b)
    return t


def pct(x: float, dec: int = 2) -> str:
    return fmt(100 * x, dec) + r"~\%"


def tri(spec: dict, n: int = N) -> np.ndarray:
    """Muestra triangular (mín, moda, máx); si mín == máx devuelve constante."""
    a, m, b = float(spec["min"]), float(spec["moda"]), float(spec["max"])
    if math.isclose(a, b):
        return np.full(n, a)
    return RNG.triangular(a, m, b, n)


def moda(spec: dict) -> float:
    return float(spec["moda"])


def media_tri(spec: dict) -> float:
    return (float(spec["min"]) + float(spec["moda"]) + float(spec["max"])) / 3.0


# ---------------------------------------------------------------------------
# 1. Costo teórico (sin desperdicio) calibrado al precio del contrato
# ---------------------------------------------------------------------------
A_SALDO = float(P["superficies"]["saldo_m2"])
A_LOSA1 = float(P["superficies"]["primera_losa_m2"])
PU13 = float(P["precios_contrato"]["item13_Bs_m2"])
PU_ACERO = float(P["precios_contrato"]["acero_Bs_kg"])
Q_ACERO_PAGO = float(P["precios_contrato"]["acero_losa_kg_m2_computo"])
PU_LOSA = PU13 + Q_ACERO_PAGO * PU_ACERO  # precio contractual de 1 m2 de losa con su acero

q = {m: float(P["materiales"][m]["q_teorica_m2"]) for m in MATS}


# ---------------------------------------------------------------------------
# 1a. APU de referencia reconstruido (Anexo I) y precios de valoración
#     Precios base: Cocarico Mamani (2022) e INE Potosí (dic-2023). Se calibra
#     al precio contractual con un factor único kappa por ítem.
# ---------------------------------------------------------------------------
APU = P["apu_referencia"]
INC = APU["incidencias"]
F_IND = (1 + INC["gastos_generales"]) * (1 + INC["utilidad"]) * (1 + INC["it"])


def cantidad(c):
    """Cantidad del APU: número o referencia «=q:material» a la cantidad teórica."""
    if isinstance(c, str) and c.startswith("=q:"):
        return q[c[3:]]
    if isinstance(c, str) and c.startswith("=qh:"):        # insumo por m3 de hormigón
        return q["hormigon"] * float(c[4:])
    return float(c)


def apu(bloque: dict):
    """Devuelve filas del APU y sus totales a precios base."""
    filas, tot = [], {}
    for grupo in ("materiales", "mano_obra", "equipo"):
        sub = 0.0
        for it in bloque.get(grupo, []):
            cant = cantidad(it["cantidad"])
            parc = cant * float(it["precio_base"])
            filas.append((grupo, it["insumo"], it["unidad"], cant, float(it["precio_base"]), parc, it.get("fuente", "")))
            sub += parc
        tot[grupo] = sub
    mo = tot["mano_obra"]
    bs = mo * INC["beneficios_sociales"]
    iva = (mo + bs) * INC["iva_mano_obra"]
    mo_total = mo + bs + iva
    herr = mo_total * INC["herramientas"]
    directo = tot["materiales"] + mo_total + tot["equipo"] + herr
    precio = directo * F_IND
    return filas, {"materiales": tot["materiales"], "mano_obra": mo, "beneficios_sociales": bs,
                   "iva_mo": iva, "mano_obra_total": mo_total, "equipo": tot["equipo"],
                   "herramientas": herr, "directo": directo, "precio_base": precio}


FILAS13, TOT13 = apu(APU["item13"])
KAPPA13 = float(P["precios_contrato"]["item13_Bs_m2"]) / TOT13["precio_base"]
FILASAC, TOTAC = apu(APU["acero_kg"])
KAPPAAC = float(P["precios_contrato"]["acero_Bs_kg"]) / TOTAC["precio_base"]


def precio_material_base(clave_insumos):
    """Suma de precios base de los insumos de un material por su unidad."""
    tot = 0.0
    for nombre, factor in clave_insumos:
        it = next(i for i in APU["item13"]["materiales"] + APU["acero_kg"]["materiales"] if i["insumo"] == nombre)
        tot += factor * float(it["precio_base"])
    return tot


p = {}
for m in MATS:
    val = P["materiales"][m]["valoracion"]
    base = precio_material_base([(x[0], float(x[1])) for x in val["insumos"]])
    kap = KAPPAAC if val["kappa"] == "acero" else KAPPA13
    p[m] = base * F_IND * kap          # precio de valoración a nivel de precio contractual
costo_mat_teo = {m: q[m] * p[m] for m in MATS}           # Bs/m2 de cada material
CM_TEO = sum(costo_mat_teo.values())


def cnc_y_cu(w: dict, rho, coc, cd_teo):
    """Costo de no calidad, costo unitario e IDM ponderado para un escenario."""
    perd = sum(costo_mat_teo[m] * w[m] for m in MATS)     # pérdidas de materiales
    retr = rho * cd_teo                                    # retrabajos y reparaciones
    cnc = perd + retr
    cu = cd_teo + cnc + coc
    idm_pond = perd / CM_TEO                               # IDM ponderado por costo
    return cnc, cu, idm_pond, perd, retr


# Calibración (opción A): el precio del contrato representa el costo esperado de
# ejecutar con la práctica habitual (sin SGC): E[CU_sin] = PU_LOSA.
w_sin_media = {m: media_tri(P["materiales"][m]["idm_sin_sgc"]) for m in MATS}
rho_sin_media = media_tri(P["retrabajo"]["fraccion_sin_sgc"])
COC_SIN = float(P["costos_sgc"]["costo_calidad_sin_sgc_Bs_m2"])
perd_sin_media = sum(costo_mat_teo[m] * w_sin_media[m] for m in MATS)
# PU = CD + perd + rho*CD + COC_SIN  ->  CD = (PU - perd - COC_SIN)/(1+rho)
CD_TEO = (PU_LOSA - perd_sin_media - COC_SIN) / (1.0 + rho_sin_media)


# ---------------------------------------------------------------------------
# 2. Escenario determinista (modas): línea base y con SGC
# ---------------------------------------------------------------------------
def costo_sgc_m2(muestras: bool):
    """Costos de prevención y evaluación del SGC por m2 del saldo."""
    tot = 0.0 if not muestras else np.zeros(N)
    filas = []
    for clave, item in P["costos_sgc"]["componentes"].items():
        val = tri(item["Bs_total"]) if muestras else moda(item["Bs_total"])
        tot = tot + val
        filas.append((clave, item))
    return tot / A_SALDO, filas


w_sin_det = {m: moda(P["materiales"][m]["idm_sin_sgc"]) for m in MATS}
e_det = {m: moda(P["materiales"][m]["eficacia_sgc"]) for m in MATS}
w_con_det = {m: w_sin_det[m] * (1 - e_det[m]) for m in MATS}
rho_sin_det = moda(P["retrabajo"]["fraccion_sin_sgc"])
rho_con_det = rho_sin_det * (1 - moda(P["retrabajo"]["eficacia_sgc"]))
coc_con_det, comp_sgc = costo_sgc_m2(False)

cnc_s, cu_s, idm_s, perd_s, retr_s = cnc_y_cu(w_sin_det, rho_sin_det, COC_SIN, CD_TEO)
cnc_c, cu_c, idm_c, perd_c, retr_c = cnc_y_cu(w_con_det, rho_con_det, coc_con_det, CD_TEO)
r_det = (cu_s - cu_c) / cu_s

# ---------------------------------------------------------------------------
# 3. Simulación de Monte Carlo
# ---------------------------------------------------------------------------
W_SIN = {m: tri(P["materiales"][m]["idm_sin_sgc"]) for m in MATS}
E_SGC = {m: tri(P["materiales"][m]["eficacia_sgc"]) for m in MATS}
W_CON = {m: W_SIN[m] * (1 - E_SGC[m]) for m in MATS}
RHO_SIN = tri(P["retrabajo"]["fraccion_sin_sgc"])
E_RET = tri(P["retrabajo"]["eficacia_sgc"])
RHO_CON = RHO_SIN * (1 - E_RET)
COC_CON, _ = costo_sgc_m2(True)

CNC_SIN, CU_SIN, IDM_SIN, PERD_SIN, RETR_SIN = cnc_y_cu(W_SIN, RHO_SIN, COC_SIN, CD_TEO)
CNC_CON, CU_CON, IDM_CON, PERD_CON, RETR_CON = cnc_y_cu(W_CON, RHO_CON, COC_CON, CD_TEO)
R = (CU_SIN - CU_CON) / CU_SIN
AHORRO_SALDO = (CU_SIN - CU_CON) * A_SALDO

# Escenario de «SGC de papel»: con probabilidad pi_falla el sistema no se aplica
# en obra (eficacia nula) pero sí se pagan sus costos.
PI_FALLA = float(SIM.get("prob_sgc_no_aplicado", 0.0))
FALLA = RNG.random(N) < PI_FALLA
W_CON_F = {m: np.where(FALLA, W_SIN[m], W_CON[m]) for m in MATS}
RHO_CON_F = np.where(FALLA, RHO_SIN, RHO_CON)
_, CU_CON_F, _, _, _ = cnc_y_cu(W_CON_F, RHO_CON_F, COC_CON, CD_TEO)
R_F = (CU_SIN - CU_CON_F) / CU_SIN


# Escenario complementario: costos ocultos de no calidad (tiempos muertos,
# supervisión adicional, horas extra), que el modelo principal no incluye.
ESC_OC = P.get("escenario_costos_ocultos")
if ESC_OC:
    rho_h_media = media_tri(ESC_OC["fraccion_sin_sgc"])
    CD_TEO_H = (PU_LOSA - perd_sin_media - COC_SIN) / (1.0 + rho_sin_media + rho_h_media)
    RHO_H_SIN = tri(ESC_OC["fraccion_sin_sgc"])
    RHO_H_CON = RHO_H_SIN * (1 - E_RET)
    _, CU_SIN_H, _, _, _ = cnc_y_cu(W_SIN, RHO_SIN + RHO_H_SIN, COC_SIN, CD_TEO_H)
    _, CU_CON_H, _, _, _ = cnc_y_cu(W_CON, RHO_CON + RHO_H_CON, COC_CON, CD_TEO_H)
    R_H = (CU_SIN_H - CU_CON_H) / CU_SIN_H
else:
    R_H = None


def resumen(x: np.ndarray) -> dict:
    return {
        "media": float(np.mean(x)), "desv_est": float(np.std(x, ddof=1)),
        "p05": float(np.percentile(x, 5)), "p50": float(np.percentile(x, 50)),
        "p95": float(np.percentile(x, 95)), "min": float(np.min(x)), "max": float(np.max(x)),
    }


p_hg = float(np.mean(R >= UMBRAL))
p_r_pos = float(np.mean(R > 0))
p_he1 = float(np.mean(IDM_CON < IDM_SIN))
p_he2 = float(np.mean(CNC_CON < CNC_SIN))
dec = lambda pr: "Se acepta H1" if pr >= CONF else "No se acepta H1 (se mantiene H0)"  # noqa: E731

# Intervalo de confianza de la probabilidad estimada (error de simulación)
def ic_prop(pr: float) -> tuple[float, float]:
    se = math.sqrt(max(pr * (1 - pr), 1e-12) / N)
    return pr - 1.96 * se, pr + 1.96 * se


# ---------------------------------------------------------------------------
# 4. Sensibilidad, punto de equilibrio y convergencia
# ---------------------------------------------------------------------------
entradas = {f"IDM sin SGC: {P['materiales'][m]['nombre']}": W_SIN[m] for m in MATS}
entradas.update({f"Eficacia del SGC: {P['materiales'][m]['nombre']}": E_SGC[m] for m in MATS})
entradas["Fracción de retrabajo sin SGC"] = RHO_SIN
entradas["Eficacia del SGC en retrabajos"] = E_RET
entradas["Costo del SGC (Bs/m²)"] = COC_CON
spearman = {k: float(stats.spearmanr(v, R)[0]) for k, v in entradas.items()}
spearman = dict(sorted(spearman.items(), key=lambda kv: -abs(kv[1])))

# Un factor a la vez: cada entrada en su mínimo y su máximo, las demás en la moda
def r_con(w_sin, e, rho_s, e_r, coc):
    w_con = {m: w_sin[m] * (1 - e[m]) for m in MATS}
    _, a, _, _, _ = cnc_y_cu(w_sin, rho_s, COC_SIN, CD_TEO)
    _, b, _, _, _ = cnc_y_cu(w_con, rho_s * (1 - e_r), coc, CD_TEO)
    return (a - b) / a

oat = []
base_args = dict(w_sin=dict(w_sin_det), e=dict(e_det), rho_s=rho_sin_det,
                 e_r=moda(P["retrabajo"]["eficacia_sgc"]), coc=coc_con_det)
for m in MATS:
    for campo, etiqueta in (("idm_sin_sgc", "IDM sin SGC"), ("eficacia_sgc", "Eficacia del SGC")):
        spec = P["materiales"][m][campo]
        vals = []
        for extremo in ("min", "max"):
            args = {k: (dict(v) if isinstance(v, dict) else v) for k, v in base_args.items()}
            if campo == "idm_sin_sgc":
                args["w_sin"][m] = float(spec[extremo])
            else:
                args["e"][m] = float(spec[extremo])
            vals.append(r_con(**args))
        oat.append((f"{etiqueta}: {P['materiales'][m]['nombre']}", vals[0], vals[1]))
for campo, etiqueta, clave in (("fraccion_sin_sgc", "Fracción de retrabajo sin SGC", "rho_s"),
                               ("eficacia_sgc", "Eficacia del SGC en retrabajos", "e_r")):
    spec = P["retrabajo"][campo]
    vals = []
    for extremo in ("min", "max"):
        args = {k: (dict(v) if isinstance(v, dict) else v) for k, v in base_args.items()}
        args[clave] = float(spec[extremo])
        vals.append(r_con(**args))
    oat.append((etiqueta, vals[0], vals[1]))
coc_min = sum(float(c["Bs_total"]["min"]) for c in P["costos_sgc"]["componentes"].values()) / A_SALDO
coc_max = sum(float(c["Bs_total"]["max"]) for c in P["costos_sgc"]["componentes"].values()) / A_SALDO
oat.append(("Costo del SGC (Bs/m²)",
            r_con(**{**base_args, "coc": coc_max}), r_con(**{**base_args, "coc": coc_min})))
oat.sort(key=lambda t: -abs(t[2] - t[1]))

# Punto de equilibrio: factor uniforme de eficacia k (misma eficacia en todo)
def r_k(k: float, coc: float = coc_con_det) -> float:
    e = {m: k for m in MATS}
    return r_con(dict(w_sin_det), e, rho_sin_det, k, coc)

def raiz(objetivo: float) -> float | None:
    lo, hi = 0.0, 1.0
    if (r_k(hi) - objetivo) < 0:
        return None
    for _ in range(80):
        mid = (lo + hi) / 2
        if r_k(mid) - objetivo >= 0:
            hi = mid
        else:
            lo = mid
    return hi

k_equilibrio = raiz(0.0)
k_umbral = raiz(UMBRAL)
r_max_teorico = r_k(1.0)

# Convergencia: media acumulada de r y su error estándar
idx = np.arange(1, N + 1)
media_acum = np.cumsum(R) / idx
se_final = float(np.std(R, ddof=1) / math.sqrt(N))

# ---------------------------------------------------------------------------
# 5. Salidas
# ---------------------------------------------------------------------------
salida = {
    "iteraciones": N, "semilla": int(SIM["semilla"]),
    "umbral_reduccion": UMBRAL, "nivel_confianza": CONF,
    "precio_contrato_losa_Bs_m2": PU_LOSA, "item13_Bs_m2": PU13,
    "acero_losa_Bs_m2": Q_ACERO_PAGO * PU_ACERO,
    "costo_directo_teorico_Bs_m2": CD_TEO,
    "costo_materiales_teorico_Bs_m2": costo_mat_teo,
    "determinista": {
        "sin_sgc": {"CU": cu_s, "CNC": cnc_s, "perdidas": perd_s, "retrabajo": retr_s,
                     "IDM_ponderado": idm_s, "CC": COC_SIN, "IDM": w_sin_det},
        "con_sgc": {"CU": cu_c, "CNC": cnc_c, "perdidas": perd_c, "retrabajo": retr_c,
                     "IDM_ponderado": idm_c, "CC": coc_con_det, "IDM": w_con_det},
        "r": r_det, "ahorro_saldo_Bs": (cu_s - cu_c) * A_SALDO,
    },
    "monte_carlo": {
        "CU_sin": resumen(CU_SIN), "CU_con": resumen(CU_CON), "r": resumen(R),
        "CNC_sin": resumen(CNC_SIN), "CNC_con": resumen(CNC_CON),
        "IDM_sin": resumen(IDM_SIN), "IDM_con": resumen(IDM_CON),
        "CC_con": resumen(COC_CON), "ahorro_saldo_Bs": resumen(AHORRO_SALDO),
        "IDM_material_sin": {m: resumen(W_SIN[m]) for m in MATS},
        "IDM_material_con": {m: resumen(W_CON[m]) for m in MATS},
        "error_estandar_media_r": se_final,
    },
    "contraste": {
        "HG": {"P(r>=umbral)": p_hg, "IC95": ic_prop(p_hg), "decision": dec(p_hg)},
        "P(r>0)": p_r_pos,
        "HE1": {"P(IDM_con<IDM_sin)": p_he1, "IC95": ic_prop(p_he1), "decision": dec(p_he1)},
        "HE2": {"P(CNC_con<CNC_sin)": p_he2, "IC95": ic_prop(p_he2), "decision": dec(p_he2)},
    },
    "sgc_no_aplicado": {"prob_falla": PI_FALLA, "r": resumen(R_F),
                         "P(r>=umbral)": float(np.mean(R_F >= UMBRAL)),
                         "P(r>0)": float(np.mean(R_F > 0))},
    "costos_ocultos": None if R_H is None else {
        "r": resumen(R_H), "P(r>=umbral)": float(np.mean(R_H >= UMBRAL)), "P(r>0)": float(np.mean(R_H > 0))},
    "sensibilidad_spearman": spearman,
    "sensibilidad_un_factor": [{"factor": f, "r_min": a, "r_max": b} for f, a, b in oat],
    "punto_equilibrio": {"eficacia_para_r_0": k_equilibrio, "eficacia_para_umbral": k_umbral,
                          "r_con_eficacia_100": r_max_teorico},
}
if SOLO_RESUMEN:
    print(json.dumps({"r_media": float(np.mean(R)), "r_p05": float(np.percentile(R, 5)),
                      "P_umbral": p_hg, "P_pos": p_r_pos, "r_max": r_max_teorico,
                      "kappa13": KAPPA13, "cc_m2": coc_con_det}))
    raise SystemExit(0)
(RES / "resumen_resultados.json").write_text(json.dumps(salida, indent=2, ensure_ascii=False),
                                             encoding="utf-8")

with open(RES / "simulacion_muestras.csv", "w", newline="", encoding="utf-8") as fh:
    wr = csv.writer(fh)
    cab = ["iteracion"] + [f"idm_sin_{m}" for m in MATS] + [f"eficacia_{m}" for m in MATS] + \
          ["rho_sin", "eficacia_retrabajo", "cc_con_Bs_m2", "cu_sin", "cu_con", "r"]
    wr.writerow(cab)
    for i in range(N):
        wr.writerow([i + 1] + [f"{W_SIN[m][i]:.6f}" for m in MATS] +
                    [f"{E_SGC[m][i]:.6f}" for m in MATS] +
                    [f"{RHO_SIN[i]:.6f}", f"{E_RET[i]:.6f}", f"{COC_CON[i]:.4f}",
                     f"{CU_SIN[i]:.4f}", f"{CU_CON[i]:.4f}", f"{R[i]:.6f}"])

# ---------------------------- Figuras ---------------------------------------
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                     "axes.spines.top": False, "axes.spines.right": False})
GRIS, AZUL, NAR = "#555555", "#2b6cb0", "#c05621"


from matplotlib.ticker import FuncFormatter  # noqa: E402

COMA = FuncFormatter(lambda v, _: (f"{v:,.2f}".rstrip("0").rstrip(".") if abs(v) < 1e4 else f"{v:,.0f}")
                     .replace(",", "X").replace(".", ",").replace("X", "."))


def guardar(fig, nombre, ejes=("x", "y")):
    """Guarda la figura con coma decimal en los ejes numéricos indicados."""
    for ax in fig.axes:
        if "x" in ejes and ax.get_xscale() == "linear":
            ax.xaxis.set_major_formatter(COMA)
        if "y" in ejes and ax.get_yscale() == "linear":
            ax.yaxis.set_major_formatter(COMA)
    fig.tight_layout()
    fig.savefig(FIG / f"{nombre}.pdf")
    fig.savefig(FIG / f"{nombre}.png", dpi=200)
    plt.close(fig)


# Histograma de r
fig, ax = plt.subplots(figsize=(6.3, 3.4))
ax.hist(100 * R, bins=60, color=AZUL, alpha=0.85, edgecolor="white")
ax.axvline(100 * UMBRAL, color=NAR, ls="--", lw=1.6, label=f"Umbral de la hipótesis ({fmt(100*UMBRAL,0)} %)")
ax.axvline(100 * np.mean(R), color="black", lw=1.2, label=f"Media ({fmt(100*np.mean(R))} %)")
ax.set_xlabel("Reducción del costo unitario, r (%)")
ax.set_ylabel("Frecuencia (escenarios)")
ax.legend(frameon=False, fontsize=8)
guardar(fig, "fig_histograma_reduccion")

# Distribución acumulada de CU sin y con SGC
fig, ax = plt.subplots(figsize=(6.3, 3.4))
for datos, et, col in ((CU_SIN, "Sin SGC (control)", GRIS), (CU_CON, "Con SGC (tratamiento)", AZUL)):
    xs = np.sort(datos)
    ax.plot(xs, np.arange(1, N + 1) / N, color=col, lw=1.8, label=et)
ax.axvline(PU_LOSA, color=NAR, ls=":", lw=1.2, label="Precio contractual")
ax.set_xlabel("Costo unitario de ejecución (Bs/m²)")
ax.set_ylabel("Probabilidad acumulada")
ax.legend(frameon=False, fontsize=8)
guardar(fig, "fig_acumulada_costo_unitario")

# Tornado (un factor a la vez)
fig, ax = plt.subplots(figsize=(6.3, 0.42 * len(oat) + 1.4))
ys = np.arange(len(oat))[::-1]
for y, (f, a, b) in zip(ys, oat):
    lo, hi = min(a, b), max(a, b)
    ax.barh(y, 100 * (hi - lo), left=100 * lo, color=AZUL, alpha=0.8)
ax.axvline(100 * r_det, color="black", lw=1, label=f"Caso base con valores más probables ({fmt(100*r_det)} %)")
ax.axvline(100 * UMBRAL, color=NAR, ls="--", lw=1.2, label=f"Umbral de la hipótesis ({fmt(100*UMBRAL,0)} %)")
lo_all = min(min(a, b) for _, a, b in oat)
hi_all = max(max(a, b) for _, a, b in oat)
ax.set_xlim(100 * lo_all - 0.4, max(100 * hi_all, 100 * UMBRAL) + 0.4)
ax.legend(frameon=False, fontsize=8, loc="upper center", bbox_to_anchor=(0.45, -0.12), ncol=2)
ax.set_yticks(ys)
ax.set_yticklabels([t[0] for t in oat], fontsize=8)
ax.set_xlabel("Reducción del costo unitario, r (%)")
guardar(fig, "fig_tornado_sensibilidad", ejes=("x",))

# Convergencia
fig, ax = plt.subplots(figsize=(6.3, 3.0))
ax.plot(idx, 100 * media_acum, color=AZUL, lw=1.2)
ax.set_xscale("log")
ax.set_xlabel("Número de iteraciones (escala logarítmica)")
ax.set_ylabel("Media acumulada de r (%)")
guardar(fig, "fig_convergencia", ejes=("y",))

# Composición del costo de no calidad (determinista)
fig, ax = plt.subplots(figsize=(6.3, 3.4))
etqs = [P["materiales"][m]["nombre"] for m in MATS] + ["Retrabajos"]
sin_v = [costo_mat_teo[m] * w_sin_det[m] for m in MATS] + [retr_s]
con_v = [costo_mat_teo[m] * w_con_det[m] for m in MATS] + [retr_c]
x = np.arange(len(etqs))
ax.bar(x - 0.2, sin_v, 0.4, color=GRIS, label="Sin SGC")
ax.bar(x + 0.2, con_v, 0.4, color=AZUL, label="Con SGC")
ax.set_xticks(x)
ax.set_xticklabels(etqs, fontsize=8)
ax.set_ylabel("Costo de no calidad (Bs/m²)")
ax.legend(frameon=False, fontsize=8)
guardar(fig, "fig_cnc_por_componente", ejes=("y",))

# ---------------------------- Tablas LaTeX ----------------------------------
def tabla(nombre: str, contenido: str):
    (TEX / f"{nombre}.tex").write_text(contenido, encoding="utf-8")


mc = salida["monte_carlo"]
filas = [
    ("Costo unitario sin SGC (Bs/m\\textsuperscript{2})", mc["CU_sin"], 2, False),
    ("Costo unitario con SGC (Bs/m\\textsuperscript{2})", mc["CU_con"], 2, False),
    ("Reducción del costo unitario, $r$", mc["r"], 2, True),
    ("Costo de no calidad sin SGC (Bs/m\\textsuperscript{2})", mc["CNC_sin"], 2, False),
    ("Costo de no calidad con SGC (Bs/m\\textsuperscript{2})", mc["CNC_con"], 2, False),
    ("Costo de la calidad del SGC (Bs/m\\textsuperscript{2})", mc["CC_con"], 2, False),
    ("IDM ponderado sin SGC", mc["IDM_sin"], 2, True),
    ("IDM ponderado con SGC", mc["IDM_con"], 2, True),
    ("Ahorro en el saldo de 2.234,60~m\\textsuperscript{2} (Bs)", mc["ahorro_saldo_Bs"], 0, False),
]
cuerpo = "\n".join(
    f"{et} & {(pct if es_pct else lambda v, d=dec: fmt(v, d))(s['media'])} & "
    f"{(pct if es_pct else lambda v, d=dec: fmt(v, d))(s['desv_est'])} & "
    f"{(pct if es_pct else lambda v, d=dec: fmt(v, d))(s['p05'])} & "
    f"{(pct if es_pct else lambda v, d=dec: fmt(v, d))(s['p50'])} & "
    f"{(pct if es_pct else lambda v, d=dec: fmt(v, d))(s['p95'])} \\\\"
    for et, s, dec, es_pct in filas)
tabla("tab_resultados_montecarlo",
      "\\begin{tabularx}{\\linewidth}{@{}Lrrrrr@{}}\n\\toprule\n"
      "\\textbf{Indicador} & \\textbf{Media} & \\textbf{Desv. est.} & \\textbf{P5} & \\textbf{P50} & \\textbf{P95} \\\\\n"
      "\\midrule\n" + cuerpo + "\n\\bottomrule\n\\end{tabularx}\n")

ct = salida["contraste"]
tabla("tab_contraste_hipotesis",
      "\\begin{tabularx}{\\linewidth}{@{}P{2.2cm}LP{2.6cm}P{3.6cm}@{}}\n\\toprule\n"
      "\\textbf{Hipótesis} & \\textbf{Criterio de aceptación} & \\textbf{Probabilidad estimada} & \\textbf{Decisión} \\\\\n\\midrule\n"
      f"General (HG) & $P(r \\geq {fmt(100*UMBRAL,0)}~\\%) \\geq {fmt(CONF,2)}$ & {fmt(p_hg,4)} & {ct['HG']['decision']} \\\\\n"
      f"Específica 1 (HE1) & $P(IDM_{{con}} < IDM_{{sin}}) \\geq {fmt(CONF,2)}$ & {fmt(p_he1,4)} & {ct['HE1']['decision']} \\\\\n"
      f"Específica 2 (HE2) & $P(CNC_{{con}} < CNC_{{sin}}) \\geq {fmt(CONF,2)}$ & {fmt(p_he2,4)} & {ct['HE2']['decision']} \\\\\n"
      "\\bottomrule\n\\end{tabularx}\n")

filas_idm = "\n".join(
    f"{P['materiales'][m]['nombre']} & {pct(w_sin_det[m])} & {pct(e_det[m],0)} & {pct(w_con_det[m])} & "
    f"{pct(mc['IDM_material_sin'][m]['media'])} & {pct(mc['IDM_material_con'][m]['media'])} \\\\"
    for m in MATS)
tabla("tab_idm_por_material",
      "\\begin{tabularx}{\\linewidth}{@{}Lrrrrr@{}}\n\\toprule\n"
      "\\textbf{Material} & \\textbf{IDM sin SGC (moda)} & \\textbf{Eficacia (moda)} & \\textbf{IDM con SGC (moda)} & "
      "\\textbf{IDM sin SGC (media MC)} & \\textbf{IDM con SGC (media MC)} \\\\\n\\midrule\n"
      + filas_idm + "\n\\bottomrule\n\\end{tabularx}\n")

# ------------------- APU de referencia (Anexo I) ---------------------------
NOMBRE_GRUPO = {"materiales": "Materiales", "mano_obra": "Mano de obra", "equipo": "Equipo y herramientas"}


def tabla_apu(filas, tot, kappa, precio_contrato, unidad_item):
    lin = []
    for grupo in ("materiales", "mano_obra", "equipo"):
        lin.append(f"\\multicolumn{{6}}{{@{{}}l}}{{\\textbf{{{NOMBRE_GRUPO[grupo]}}}}} \\\\")
        for g, ins, un, cant, pb, parc, fte in filas:
            if g == grupo:
                lin.append(f"{tex(ins)} & {tex(un)} & {fmt(cant, 4)} & {fmt(pb)} & {fmt(parc)} & {tex(fte)} \\\\")
    lin.append("\\midrule")
    lin.append(f"\\multicolumn{{4}}{{@{{}}l}}{{Subtotal materiales}} & {fmt(tot['materiales'])} & \\\\")
    lin.append(f"\\multicolumn{{4}}{{@{{}}l}}{{Mano de obra (sin cargas)}} & {fmt(tot['mano_obra'])} & \\\\")
    lin.append(f"\\multicolumn{{4}}{{@{{}}l}}{{Beneficios sociales ({fmt(100*INC['beneficios_sociales'],0)}~\\% de la mano de obra)}} & {fmt(tot['beneficios_sociales'])} & \\\\")
    lin.append(f"\\multicolumn{{4}}{{@{{}}l}}{{IVA sobre mano de obra ({fmt(100*INC['iva_mano_obra'])}~\\%)}} & {fmt(tot['iva_mo'])} & \\\\")
    lin.append(f"\\multicolumn{{4}}{{@{{}}l}}{{Equipo}} & {fmt(tot['equipo'])} & \\\\")
    lin.append(f"\\multicolumn{{4}}{{@{{}}l}}{{Herramientas menores ({fmt(100*INC['herramientas'],0)}~\\% de la mano de obra total)}} & {fmt(tot['herramientas'])} & \\\\")
    lin.append(f"\\multicolumn{{4}}{{@{{}}l}}{{\\textbf{{Costo directo}}}} & \\textbf{{{fmt(tot['directo'])}}} & \\\\")
    lin.append(f"\\multicolumn{{4}}{{@{{}}l}}{{Gastos generales ({fmt(100*INC['gastos_generales'],0)}~\\%), utilidad ({fmt(100*INC['utilidad'],0)}~\\%) e IT ({fmt(100*INC['it'])}~\\%): factor {fmt(F_IND,4)}}} & {fmt(tot['precio_base'])} & \\\\")
    lin.append(f"\\multicolumn{{4}}{{@{{}}l}}{{Precio unitario contractual ({unidad_item})}} & {fmt(precio_contrato, 4)} & \\\\")
    lin.append(f"\\multicolumn{{4}}{{@{{}}l}}{{\\textbf{{Factor de calibración $\\kappa$ = precio contractual / precio reconstruido}}}} & \\textbf{{{fmt(kappa, 4)}}} & \\\\")
    return ("\\begin{longtable}{@{}P{4.6cm}P{0.9cm}rrrP{4.2cm}@{}}\n\\toprule\n"
            "\\textbf{Insumo} & \\textbf{Unid.} & \\textbf{Cantidad} & \\textbf{Precio base (Bs)} & \\textbf{Parcial (Bs)} & \\textbf{Fuente} \\\\\n\\midrule\n\\endhead\n"
            + "\n".join(lin) + "\n\\bottomrule\n\\end{longtable}\n")


tabla("tab_apu_item13", tabla_apu(FILAS13, TOT13, KAPPA13, PU13, "Bs/m\\textsuperscript{2}"))
tabla("tab_apu_acero", tabla_apu(FILASAC, TOTAC, KAPPAAC, PU_ACERO, "Bs/kg"))

# ------------------- Tabla de parámetros del modelo (Anexo L) ---------------
def fila_tri(etq, spec, es_pct=True, unidad=""):
    f = (lambda v: pct(v, 1)) if es_pct else (lambda v: fmt(v, 0))
    return (f"{etq} & {f(float(spec['min']))} & {f(float(spec['moda']))} & {f(float(spec['max']))} & "
            f"{tex(spec.get('fuente', ''))} \\\\")


lp = []
for m in MATS:
    nm = P["materiales"][m]["nombre"]
    lp.append(fila_tri(f"IDM sin SGC -- {nm}", P["materiales"][m]["idm_sin_sgc"]))
for m in MATS:
    nm = P["materiales"][m]["nombre"]
    lp.append(fila_tri(f"Eficacia del SGC -- {nm}", P["materiales"][m]["eficacia_sgc"]))
lp.append(fila_tri("Fracción de retrabajo sin SGC ($\\rho$)", P["retrabajo"]["fraccion_sin_sgc"]))
lp.append(fila_tri("Eficacia del SGC en retrabajos ($e_R$)", P["retrabajo"]["eficacia_sgc"]))
for c in P["costos_sgc"]["componentes"].values():
    lp.append(fila_tri(f"{tex(c['descripcion'])} (Bs)", c["Bs_total"], es_pct=False))
ENC_PARAM = ("\\toprule\n\\textbf{Parámetro} & \\textbf{Mín.} & \\textbf{Moda} & \\textbf{Máx.} & "
             "\\textbf{Fuente o justificación} \\\\\n\\midrule\n")
tabla("tab_parametros",
      "\\begin{longtable}{@{}P{4.3cm}rrrP{6.0cm}@{}}\n"
      "\\caption{Parámetros inciertos del modelo de costos y sus fuentes}\\label{tab:parametros-modelo}\\\\\n"
      + ENC_PARAM + "\\endfirsthead\n"
      "\\multicolumn{5}{@{}l}{\\textit{(continuación)}}\\\\\n" + ENC_PARAM + "\\endhead\n"
      "\\bottomrule\n\\endfoot\n"
      + "\n".join(lp) + "\n\\end{longtable}\n")

# ------------------- Macros con las cifras clave (para el texto) ------------
def macro(nombre: str, valor: str) -> str:
    return f"\\newcommand{{\\{nombre}}}{{{valor}}}\n"


ce = salida["contraste"]
mac = [
    macro("MCiter", fmt(N, 0)), macro("MCsemilla", str(SIM["semilla"])),
    macro("MCumbral", fmt(100 * UMBRAL, 0) + r"~\%"), macro("MCconf", fmt(CONF, 2)),
    macro("PUlosa", fmt(PU_LOSA)), macro("PUitemTrece", fmt(PU13)),
    macro("PUaceroLosa", fmt(Q_ACERO_PAGO * PU_ACERO)), macro("CDteo", fmt(CD_TEO)),
    macro("CMteo", fmt(CM_TEO)),
    macro("CUsinDet", fmt(cu_s)), macro("CUconDet", fmt(cu_c)), macro("rDet", pct(r_det)),
    macro("CNCsinDet", fmt(cnc_s)), macro("CNCconDet", fmt(cnc_c)),
    macro("CNCsinDetPct", pct(cnc_s / cu_s)), macro("CNCconDetPct", pct(cnc_c / cu_c)),
    macro("CCconDet", fmt(coc_con_det)), macro("CCconDetPct", pct(coc_con_det / cu_c)),
    macro("IDMsinDet", pct(idm_s)), macro("IDMconDet", pct(idm_c)),
    macro("AhorroDet", fmt((cu_s - cu_c) * A_SALDO, 0)),
    macro("CUsinMedia", fmt(mc["CU_sin"]["media"])), macro("CUconMedia", fmt(mc["CU_con"]["media"])),
    macro("rMedia", pct(mc["r"]["media"])), macro("rDesv", pct(mc["r"]["desv_est"])),
    macro("rPcinco", pct(mc["r"]["p05"])), macro("rPcincuenta", pct(mc["r"]["p50"])),
    macro("rPnoventaycinco", pct(mc["r"]["p95"])),
    macro("CNCsinMedia", fmt(mc["CNC_sin"]["media"])), macro("CNCconMedia", fmt(mc["CNC_con"]["media"])),
    macro("CNCreduccionPct", pct(1 - mc["CNC_con"]["media"] / mc["CNC_sin"]["media"])),
    macro("CCconMedia", fmt(mc["CC_con"]["media"])),
    macro("IDMsinMedia", pct(mc["IDM_sin"]["media"])), macro("IDMconMedia", pct(mc["IDM_con"]["media"])),
    macro("AhorroMedia", fmt(mc["ahorro_saldo_Bs"]["media"], 0)),
    macro("AhorroPcinco", fmt(mc["ahorro_saldo_Bs"]["p05"], 0)),
    macro("AhorroPnoventaycinco", fmt(mc["ahorro_saldo_Bs"]["p95"], 0)),
    macro("PHG", fmt(p_hg, 4)), macro("PRpos", fmt(p_r_pos, 4)),
    macro("PHEuno", fmt(p_he1, 4)), macro("PHEdos", fmt(p_he2, 4)),
    macro("DecHG", ce["HG"]["decision"]), macro("DecHEuno", ce["HE1"]["decision"]),
    macro("DecHEdos", ce["HE2"]["decision"]),
    macro("SEr", fmt(100 * se_final, 4) + r"~\%"),
    macro("PiFalla", fmt(100 * PI_FALLA, 0) + r"~\%"),
    macro("rMediaFalla", pct(salida["sgc_no_aplicado"]["r"]["media"])),
    macro("PRposFalla", fmt(salida["sgc_no_aplicado"]["P(r>0)"], 4)),
    macro("KequilibrioCero", pct(k_equilibrio, 1) if k_equilibrio is not None else "no alcanzable"),
    macro("KequilibrioUmbral", pct(k_umbral, 1) if k_umbral is not None else "no alcanzable"),
    macro("rMaxTeorico", pct(r_max_teorico)),
    macro("rMediaOcultos", pct(float(np.mean(R_H))) if R_H is not None else "--"),
    macro("rPcincoOcultos", pct(float(np.percentile(R_H, 5))) if R_H is not None else "--"),
    macro("PHGocultos", fmt(float(np.mean(R_H >= UMBRAL)), 4) if R_H is not None else "--"),
    macro("KappaTrece", fmt(KAPPA13, 3)), macro("KappaAcero", fmt(KAPPAAC, 3)),
    macro("FactorInd", fmt(F_IND, 4)),
    macro("APUtreceBase", fmt(TOT13["precio_base"])), macro("APUaceroBase", fmt(TOTAC["precio_base"], 2)),
]
for m in MATS:
    nm = {"viguetas": "Vig", "eps": "Eps", "hormigon": "Hor", "acero": "Ace"}.get(m, m.capitalize())
    mac.append(macro(f"IDMsin{nm}", pct(w_sin_det[m])))
    mac.append(macro(f"IDMcon{nm}", pct(w_con_det[m])))
    mac.append(macro(f"Ef{nm}", pct(e_det[m], 0)))
    mac.append(macro(f"Precio{nm}", fmt(p[m])))
    mac.append(macro(f"Qteo{nm}", fmt(q[m], 4)))
    mac.append(macro(f"Costo{nm}", fmt(costo_mat_teo[m])))
(TEX / "valores_modelo.tex").write_text(
    "% Archivo generado por modelo_costos.py: no editar a mano.\n" + "".join(mac), encoding="utf-8")

print(json.dumps({"PU_losa": PU_LOSA, "CD_teo": CD_TEO, "r_det": r_det,
                  "r_media": float(np.mean(R)), "P(r>=umbral)": p_hg, "P(r>0)": p_r_pos,
                  "P_HE1": p_he1, "P_HE2": p_he2, "k_equilibrio": k_equilibrio,
                  "k_umbral": k_umbral, "r_max": r_max_teorico}, indent=2, ensure_ascii=False))

# Macros en inglés para el Abstract (leen el JSON recién escrito).
import runpy  # noqa: E402
runpy.run_path(str(Path(__file__).with_name("macros_en.py")))
