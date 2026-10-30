"""Plano 03 — detección automática de viguetas (pares de líneas paralelas de color), recorte por las caras de las vigas
(ráster de las líneas negras de 0,72 pt y rellenos negros) y asignación a los paños A1…A41 (polígonos por ejes).
Uso: python3 p03_viguetas.py  → escribe ../intermedios/p03_viguetas_por_pano.json y un resumen en pantalla.
Coordenadas: espacio NO rotado del PDF (las de page.get_text('words')). Escala 12,564 pt/m (ejes 1–5 = 10,00 m)."""
import json, math, os, collections
import numpy as np, pymupdf
from PIL import Image, ImageDraw
from matplotlib.path import Path

PDF = '/home/user/TesisSGC/03_Datos_Obra_Edificio_Posgrado/01_Planos/Plano_03_Cantidad_de_Viguetas_Primera_Losa.pdf'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'intermedios')
os.makedirs(OUT, exist_ok=True)
ESC = 12.564  # pt/m (calculado en p01_p03_textos.py)
K = 8         # px por pt del ráster de vigas

# ---------------- ejes (Plano 03) ----------------
X = dict(A=505.43, Ap=485.5, B=474.11, Bp=459.8, Bpp=453.27, C=442.67, Cp=427.29, D=403.19, E=379.79, F=348.47,
         G=285.59, H=222.83, I=191.39, J=159.95, K=128.51, Kp=113.19, L=97.07, M=65.75)
Y = {'1': 115.66, "1'": 136.0, '2': 147.1, "2'": 161.7, '3': 178.42, "3'": 194.2, '4': 209.86, '5': 241.3,
     "5'": 272.7, '6': 304.06, '7': 327.1, "7'": 351.15, '8': 366.94, "8'": 398.3, '9': 429.7, "9'": 445.35,
     '10': 469.51, '11': 492.55, "11'": 523.95, '12': 555.31, '13': 586.75, "13'": 602.4, '14': 618.07,
     "14'": 634.95, '15': 649.51, "15'": 660.6, '16': 680.95}
XVP = 363.6   # viga plana VP 30x25 a media distancia E–F (límite de A8/A28 y A15/A25…; medido en el dibujo)
XVP2 = 303.5  # VP 30x25 entre A9/A10/A15 y A11/A16 (medido)

def R(x0, x1, y0, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]

def P(*pts):
    return list(pts)

x, y = X, Y
POLY = {
    'A1': R(x['Bpp'], x['A'], y['1'], y['5']), 'A2': R(x['D'], x['Bpp'], y['1'], y['5']),
    'A3': R(x['F'], x['D'], y['1'], y['5']), 'A4': R(x['G'], x['F'], y['1'], y['5']),
    'A5': R(x['H'], x['G'], y['1'], y['5']), 'A6': R(x['J'], x['H'], y['1'], y['5']),
    'A7': P((x['J'], y['1']), (x['K'], y['1']), (x['K'], y['3']), (x['L'], y['4']), (x['K'], y['5']), (x['J'], y['5'])),
    'A8': R(XVP, x['A'], y['5'], y['6']),
    'A9': R(XVP2, XVP, y['5'], 262.0), 'A10': R(XVP2, XVP, 283.0, y['6']),
    'A11': R(x['G'], XVP2, y['5'], y['6']),
    'A12': R(x['I'], x['G'], y['5'], y['6']),
    'A13': P((x['I'], y['5']), (x['I'], y['6']), (x['J'], y['6']), (x['J'], y["5'"]), (x['K'], y['5']), ),
    'A14': R(x['E'], x['B'], y['6'], y['8']), 'A15': R(XVP2, x['E'], y['6'], y['8']),
    'A16': R(x['G'], XVP2, y['6'], 324.0), 'A17': R(x['I'], x['G'], y['6'], y['8']),
    'A18': P((x['I'], y['6']), (x['I'], y['8']), (x['Kp'], y["7'"]), (x['J'], y['6'])),
    'A19': R(x['E'], x['C'], y['8'], y['9']), 'A20': R(x['G'], x['E'], y['8'], y['9']),
    'A21': R(x['I'], x['G'], y['8'], y['9']),
    'A22': P((x['I'], y['8']), (x['I'], y['9']), (x['Kp'], y["9'"]), (x['Kp'], y["7'"])),
    'A23': P((x['Kp'], y["7'"]), (x['Kp'], y["9'"]), (x['M'], y["8'"])),
    'A24': R(x['E'], x['B'], y['9'], y['11']), 'A25': R(x['G'], x['E'], y['9'], y['11']),
    'A26': R(x['I'], x['G'], y['9'], y['11']),
    'A27': P((x['I'], y['9']), (x['I'], y['11']), (x['J'], y['11']), (x['Kp'], y["9'"])),
    'A28': R(XVP, x['A'], y['11'], y['12']),
    'A29': R(XVP2, XVP, y['11'], 514.0), 'A30': R(XVP2, XVP, 534.0, y['12']),
    'A31': R(x['G'], XVP2, y['11'], y['12']), 'A32': R(x['I'], x['G'], y['11'], y['12']),
    'A33': P((x['I'], y['11']), (x['I'], y['12']), (x['K'], y['12']), (x['J'], y["11'"]), (x['J'], y['11'])),
    'A34': R(x['Bpp'], x['A'], y['12'], y['16']), 'A35': R(x['D'], x['Bpp'], y['12'], y['16']),
    'A36': R(x['F'], x['D'], y['12'], y['16']), 'A37': R(x['G'], x['F'], y['12'], y['13']),
    'A38': R(x['H'], x['G'], y['12'], y['16']), 'A39': R(x['I'], x['H'], y['12'], y['14']),
    'A40': P((x['I'], y['12']), (x['I'], y['14']), (x['K'], y['14']), (x['L'], y['13']), (x['K'], y['12'])),
    'A41': P((x['H'], y['14']), (x['H'], y['16']), (x['J'], y['16']), (x['J'], y['15']), (x['K'], y['14'])),
}

page = pymupdf.open(PDF)[0]
W, H = page.mediabox.width, page.mediabox.height  # 612 x 792 (no rotado)
drs = page.get_drawings()

def col(v):
    return tuple(round(c, 3) for c in v) if v else None

# ---------------- ráster de vigas ----------------
img = Image.new('L', (int(W * K) + 1, int(H * K) + 1), 0)
dw = ImageDraw.Draw(img)
for d in drs:
    c = col(d.get('color')); f = col(d.get('fill'))
    if d['type'] in ('f', 'fs') and f == (0.0, 0.0, 0.0):
        for it in d['items']:
            pass
        r = d['rect']
        if r.width < 12 and r.height < 12:  # columnas y pequeños rellenos
            dw.rectangle([r.x0 * K, r.y0 * K, r.x1 * K, r.y1 * K], fill=255)
    if c == (0.0, 0.0, 0.0) and round(d.get('width') or 0, 2) == 0.72:
        for it in d['items']:
            if it[0] == 'l':
                dw.line([it[1].x * K, it[1].y * K, it[2].x * K, it[2].y * K], fill=255, width=6)
            elif it[0] == 'c':
                pts = [it[1], it[2], it[3], it[4]]
                bez = []
                for t in np.linspace(0, 1, 25):
                    xx = (1 - t) ** 3 * pts[0].x + 3 * (1 - t) ** 2 * t * pts[1].x + 3 * (1 - t) * t ** 2 * pts[2].x + t ** 3 * pts[3].x
                    yy = (1 - t) ** 3 * pts[0].y + 3 * (1 - t) ** 2 * t * pts[1].y + 3 * (1 - t) * t ** 2 * pts[2].y + t ** 3 * pts[3].y
                    bez.append((xx * K, yy * K))
                dw.line(bez, fill=255, width=6)
            elif it[0] == 're':
                r = it[1]
                dw.rectangle([r.x0 * K, r.y0 * K, r.x1 * K, r.y1 * K], outline=255, width=6)
B = np.array(img) > 0

def is_beam(px, py):
    i, j = int(round(py * K)), int(round(px * K))
    return B[max(0, min(B.shape[0] - 1, i)), max(0, min(B.shape[1] - 1, j))]

# ---------------- segmentos de viguetas por color ----------------
VCOL = {(1.0, 1.0, 0.0): 'amarillo', (1.0, 1.0, 1.0): 'blanco', (0.447, 0.455, 0.188): 'oliva',
        (0.075, 0.404, 0.204): 'verde', (0.0, 1.0, 1.0): 'cian', (0.0, 0.0, 1.0): 'azul', (1.0, 0.0, 1.0): 'magenta',
        (1.0, 0.0, 0.0): 'rojo', (0.949, 0.404, 0.133): 'naranja'}
segs = collections.defaultdict(list)
for d in drs:
    c = col(d.get('color')) or col(d.get('fill'))
    if c not in VCOL:
        continue
    if c == (0.0, 0.0, 1.0) and round(d.get('width') or 0, 2) != 0:
        continue
    for it in d['items']:
        if it[0] != 'l':
            continue
        a, b = it[1], it[2]
        L = math.hypot(b.x - a.x, b.y - a.y)
        if L < 6:  # flechas, marcas
            continue
        if abs(b.y - a.y) < 0.02 * L:
            o = 'H'; off = (a.y + b.y) / 2; s0, s1 = sorted((a.x, b.x))
        elif abs(b.x - a.x) < 0.02 * L:
            o = 'V'; off = (a.x + b.x) / 2; s0, s1 = sorted((a.y, b.y))
        else:
            continue
        segs[(VCOL[c], o)].append((off, s0, s1))

# pares: dos líneas del mismo color y orientación, separadas 0,8–1,8 pt, con solape ≥ 60 %
runs = []
for (cname, o), lst in segs.items():
    lst = sorted(set((round(a, 2), round(b, 2), round(c, 2)) for a, b, c in lst))
    used = set()
    for i, (off, s0, s1) in enumerate(lst):
        if i in used:
            continue
        best = None
        for j in range(i + 1, len(lst)):
            off2, t0, t1 = lst[j]
            if off2 - off > 1.9:
                break
            if j in used or off2 - off < 0.8:
                continue
            ov = min(s1, t1) - max(s0, t0)
            if ov >= 0.6 * min(s1 - s0, t1 - t0):
                best = j; break
        if best is not None:
            used.update({i, best})
            off2, t0, t1 = lst[best]
            runs.append(dict(color=cname, o=o, off=(off + off2) / 2, s0=min(s0, t0), s1=max(s1, t1)))
# eliminar duplicados entre colores (p. ej., naranja superpuesto a cian en A7)
runs.sort(key=lambda r: (r['o'], round(r['off'], 0), r['s0']))
ded = []
for r in runs:
    dup = False
    for q in ded:
        if q['o'] == r['o'] and abs(q['off'] - r['off']) < 0.5 and min(q['s1'], r['s1']) - max(q['s0'], r['s0']) > 0.8 * (r['s1'] - r['s0']):
            dup = True; q.setdefault('colores', {q['color']}).add(r['color']); break
    if not dup:
        ded.append(r)
runs = ded

paths = {k: Path(v) for k, v in POLY.items()}

def pano_of(px, py):
    for k, pa in paths.items():
        if pa.contains_point((px, py), radius=0.01) or pa.contains_point((px, py), radius=-0.01):
            return k
    return None

# ---------------- recorte por vigas y asignación ----------------
pieces = []
step = 0.2
for r in runs:
    n = int((r['s1'] - r['s0']) / step) + 1
    ts = np.linspace(r['s0'], r['s1'], n)
    pts = [(t, r['off']) if r['o'] == 'H' else (r['off'], t) for t in ts]
    free = [not is_beam(px, py) for px, py in pts]
    cur = None
    for t, f, (px, py) in zip(ts, free, pts):
        if f and cur is None:
            cur = [t, t]
        elif f:
            cur[1] = t
        if (not f or t == ts[-1]) and cur is not None:
            a, b = cur
            if (b - a) / ESC > 0.33:  # descarta el interior de las vigas (0,19–0,27 m) y marcas cortas
                m = (a + b) / 2
                mx, my = (m, r['off']) if r['o'] == 'H' else (r['off'], m)
                pieces.append(dict(color=r['color'], o=r['o'], off=round(r['off'], 2), a=round(a, 2), b=round(b, 2),
                                   L=round((b - a) / ESC, 3), pano=pano_of(mx, my), run=(r['o'], round(r['off'], 2), round(r['s0'], 1))))
            cur = None

# agrupar piezas por paño y por vigueta (misma corrida) → longitud libre (cara a cara) y longitud de EPS (suma de tramos)
res = {}
for k in POLY:
    pk = [q for q in pieces if q['pano'] == k]
    by = collections.defaultdict(list)
    for q in pk:
        by[q['run']].append(q)
    vig = []
    for run, qs in by.items():
        a = min(q['a'] for q in qs); b = max(q['b'] for q in qs)
        vig.append(dict(o=run[0], off=run[1], L_libre=round((b - a) / ESC, 3), L_tramos=round(sum(q['L'] for q in qs), 3),
                        n_tramos=len(qs), colores=sorted({q['color'] for q in qs})))
    vig.sort(key=lambda v: v['off'])
    res[k] = vig
json.dump(dict(POLY=POLY, viguetas=res), open(os.path.join(OUT, 'p03_viguetas_por_pano.json'), 'w'), indent=1, ensure_ascii=False)
labels = json.load(open(os.path.join(OUT, 'p01_p03_textos.json')))
for k in POLY:
    v = res[k]
    os_ = collections.Counter(q['o'] for q in v)
    Ls = [q['L_libre'] for q in v]
    print(f"{k:4} n={len(v):3}  dir={dict(os_)}  L_libre: min {min(Ls) if Ls else 0:.2f} max {max(Ls) if Ls else 0:.2f} media {np.mean(Ls) if Ls else 0:.2f}  Σ={sum(Ls):.2f}  colores={sorted({c for q in v for c in q['colores']})}")
