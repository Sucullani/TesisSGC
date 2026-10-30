"""Extrae textos de los Planos 01 y 03 (capa vectorial) y asocia, por posición, las áreas A1…A41 (Plano 01)
con las etiquetas de cantidad de viguetas (Plano 03).
Transformación lineal entre hojas a partir de los globos de ejes (A…M, 1…16), calculada aquí mismo.
Salida: tablas impresas + JSON en ../p01_p03_asociacion.json (intermedio)."""
import json, re, sys, pymupdf, math, os
BASE = '/home/user/TesisSGC/03_Datos_Obra_Edificio_Posgrado/01_Planos/'
OUT = os.path.join(os.path.dirname(__file__), '..', 'intermedios')
os.makedirs(OUT, exist_ok=True)

def words(fn):
    return pymupdf.open(BASE + fn)[0].get_text('words')

def spans(fn):
    p = pymupdf.open(BASE + fn)[0]
    out = []
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                t = s['text'].strip()
                if t:
                    c = s['color']
                    out.append(dict(t=t, col=((c >> 16) & 255, (c >> 8) & 255, c & 255), size=round(s['size'], 2),
                                    bbox=[round(v, 2) for v in s['bbox']]))
    return out

def axes(ws, xband, yband):
    """globos de ejes: letras arriba (y en yband) y números a la derecha (x en xband)"""
    letters, numbers = {}, {}
    for w in ws:
        x0, y0, x1, y1, t = w[:5]
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        if yband[0] <= cy <= yband[1] and re.fullmatch(r'[A-M]', t):
            letters[t] = cx
        if xband[0] <= cx <= xband[1] and re.fullmatch(r'\d{1,2}', t):
            numbers[int(t)] = cy
    return letters, numbers

w1 = words('Plano_01_Geometria_Sistema_de_Ejes_Primera_Losa.pdf')
w3 = words('Plano_03_Cantidad_de_Viguetas_Primera_Losa.pdf')
L1, N1 = axes(w1, (2080, 2110), (500, 530))
L3, N3 = axes(w3, (535, 550), (75, 85))
# transformación x03 = a*x01 + b ; y03 = c*y01 + d (mínimos cuadrados con los ejes comunes)
import numpy as np
kx = sorted(set(L1) & set(L3)); ky = sorted(set(N1) & set(N3))
a, b = np.polyfit([L1[k] for k in kx], [L3[k] for k in kx], 1)
c, d = np.polyfit([N1[k] for k in ky], [N3[k] for k in ky], 1)
res_x = max(abs(a * L1[k] + b - L3[k]) for k in kx); res_y = max(abs(c * N1[k] + d - N3[k]) for k in ky)
print(f'Transformación: x03 = {a:.5f}·x01 + {b:.2f} (resid. máx {res_x:.2f} pt); y03 = {c:.5f}·y01 + {d:.2f} (resid. máx {res_y:.2f} pt)')
# escala del Plano 03 (pt por metro) con ejes 1-5 (10,00 m según cotas del Plano 01: 4 x 2,50)
esc3 = (N3[5] - N3[1]) / 10.0
print('Escala Plano 03: %.3f pt/m' % esc3)
print('Ejes letra (Plano 03, x):', {k: round(v, 2) for k, v in sorted(L3.items(), key=lambda kv: -kv[1])})
print('Ejes número (Plano 03, y):', {k: round(v, 2) for k, v in sorted(N3.items())})

# áreas del Plano 01: grupos 'Ax' '=' 'val' 'M2' (mismo bloque/línea)
areas = {}
for i, w in enumerate(w1):
    if re.fullmatch(r'A\d{1,2}', w[4]):
        same = [v for v in w1 if v[5] == w[5] and v[6] == w[6]]
        txt = ' '.join(v[4] for v in same)
        m = re.search(r'A(\d+)\s*=\s*([\d.]+)\s*M2', txt)
        if m:
            x0 = min(v[0] for v in same); x1 = max(v[2] for v in same)
            y0 = min(v[1] for v in same); y1 = max(v[3] for v in same)
            cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
            areas[int(m.group(1))] = dict(area_plano=float(m.group(2)), x01=round(cx, 1), y01=round(cy, 1),
                                          x03=round(a * cx + b, 2), y03=round(c * cy + d, 2))
print('Áreas leídas en Plano 01:', len(areas))

# etiquetas de cantidad (Plano 03): números negros de 5,53 pt dentro de la planta (excluye globos de ejes)
sp3 = spans('Plano_03_Cantidad_de_Viguetas_Primera_Losa.pdf')
counts = []
for s in sp3:
    x0, y0, x1, y1 = s['bbox']; cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    if s['col'] == (0, 0, 0) and s['size'] == 5.53 and re.fullmatch(r'\d{1,2}', s['t']) and 40 < cx < 530 and 90 < cy < 700:
        counts.append(dict(n=int(s['t']), x=round(cx, 2), y=round(cy, 2)))
reds = [dict(t=s['t'], x=round((s['bbox'][0] + s['bbox'][2]) / 2, 2), y=round((s['bbox'][1] + s['bbox'][3]) / 2, 2))
        for s in sp3 if s['col'] == (255, 0, 0)]
blacks_dim = [dict(t=s['t'], x=round((s['bbox'][0] + s['bbox'][2]) / 2, 2), y=round((s['bbox'][1] + s['bbox'][3]) / 2, 2))
              for s in sp3 if s['col'] == (0, 0, 0) and s['size'] == 3.16]
print('Etiquetas de cantidad en Plano 03:', len(counts), ' cotas rojas:', len(reds), ' cotas negras:', len(blacks_dim))
json.dump(dict(transf=dict(a=a, b=b, c=c, d=d), esc3=esc3, L3=L3, N3=N3, L1=L1, N1=N1, areas=areas, counts=counts,
               reds=reds, cotas=blacks_dim), open(os.path.join(OUT, 'p01_p03_textos.json'), 'w'), indent=1,
          ensure_ascii=False)
for k in sorted(areas):
    A = areas[k]
    near = sorted(counts, key=lambda q: math.hypot(q['x'] - A['x03'], q['y'] - A['y03']))[:2]
    print(f"A{k:<3} {A['area_plano']:>6}  p03=({A['x03']:6.1f},{A['y03']:6.1f})  cercanas: " +
          ', '.join(f"{q['n']}@({q['x']:.0f},{q['y']:.0f}) d={math.hypot(q['x']-A['x03'], q['y']-A['y03']):.0f}" for q in near))
