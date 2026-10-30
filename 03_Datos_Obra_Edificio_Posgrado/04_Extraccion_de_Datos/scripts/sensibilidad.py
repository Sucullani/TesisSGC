"""Escenarios de sensibilidad de cantidades_teoricas.py (no modifican el CSV base).
Salida: ../intermedios/sensibilidad.json y tabla en pantalla."""
import json, os, subprocess, sys
BASE = os.path.dirname(os.path.abspath(__file__)); INT = os.path.join(BASE, '..', 'intermedios')
ESC = {
    'base (S1)': {},
    'negativos 1φ10': {'neg_diam': 'phi10'},
    'negativos 1φ6': {'neg_diam': 'phi6'},
    'bloque envolvente 0,44×0,20 (0,088 m²)': {'A_blk': 0.088},
    'n según etiquetas (franja inferior 20)': {'adopta_n': {'A34': 20, 'A35': 20, 'A36': 20, 'A38': 20}},
    'n según dibujo (18/18/18/19)': {'adopta_n': {'A34': 18, 'A35': 18, 'A36': 18, 'A38': 19}},
    'nervio si luz ≥ 3,0 m': {'nerv_luz_min': 3.0},
    'sin nervios (luz mín. 99 m)': {'nerv_luz_min': 99.0},
    'geometría Plano 02 (0,15 + 0,05)': {'h_eps': 0.15, 'h_total': 0.20},
    'vigueta 19,5 kg/m (Concretec Cbba.)': {'vig_masa': 19.5},
    'malla sin anclajes ni traslapes': {'malla_anclaje': 0.0, 'malla_traslape': 0.0},
    'apoyo de vigueta 0,10 m por extremo': {'apoyo': 0.10},
}
out = {}
for i, (nm, par) in enumerate(ESC.items()):
    env = dict(os.environ, CT_PAR=json.dumps(par), CT_SUF=f'_sens{i}')
    subprocess.run([sys.executable, os.path.join(BASE, 'cantidades_teoricas.py')], env=env, check=True, capture_output=True)
    R = json.load(open(os.path.join(INT, f'resumen_cantidades_sens{i}.json')))
    out[nm] = {k: R[k] for k in ['n_vig', 'm_vig', 'eps_net_S1', 'eps_pra_S1', 'V_hor_S1', 'V_hor_S1_m2', 'kg_S1', 'kg_S1_m2',
                                 'IDM_eps_net_S1', 'dif_4171_kg_S1', 'n_nerv']}
    os.remove(os.path.join(INT, f'resumen_cantidades_sens{i}.json'))
json.dump(out, open(os.path.join(INT, 'sensibilidad.json'), 'w'), indent=1, ensure_ascii=False)
print(f"{'escenario':42} {'n_vig':>5} {'m_vig':>7} {'EPSnet':>7} {'EPSpr':>6} {'IDM%':>5} {'Hº m3':>6} {'m3/m2':>6} {'kg':>7} {'kg/m2':>5} {'4171%':>6} nerv")
for nm, r in out.items():
    print(f"{nm:42} {r['n_vig']:5d} {r['m_vig']:7.1f} {r['eps_net_S1']:7.1f} {r['eps_pra_S1']:6d} {r['IDM_eps_net_S1']:5.1f} {r['V_hor_S1']:6.2f} {r['V_hor_S1_m2']:6.4f} {r['kg_S1']:7.1f} {r['kg_S1_m2']:5.2f} {r['dif_4171_kg_S1']:6.1f} {r['n_nerv']}")
