"""Cuenta las filas de bloques de EPS dibujadas en el Plano 03 (líneas grises 0.388 = juntas de bloques cada 1,00 m).
Para cada paño: juntas perpendiculares a la dirección de las viguetas, agrupadas por nivel; filas = moda del n.º de juntas
por nivel. Salida: ../intermedios/p03_filas_eps.json"""
import json, os, collections, math
import pymupdf
from matplotlib.path import Path
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, '..', 'intermedios')
POLY = json.load(open(os.path.join(OUT, 'p03_viguetas_por_pano.json')))['POLY']
VIG = json.load(open(os.path.join(OUT, 'p03_viguetas_por_pano.json')))['viguetas']
page = pymupdf.open('/home/user/TesisSGC/03_Datos_Obra_Edificio_Posgrado/01_Planos/Plano_03_Cantidad_de_Viguetas_Primera_Losa.pdf')[0]
G = []
for d in page.get_drawings():
    c = tuple(round(v, 3) for v in d['color']) if d.get('color') else None
    if c != (0.388, 0.392, 0.4):
        continue
    for it in d['items']:
        if it[0] == 'l':
            a, b = it[1], it[2]
            G.append((a.x, a.y, b.x, b.y))
res = {}
for k, poly in POLY.items():
    pa = Path(poly)
    v = VIG[k]
    o = collections.Counter(q['o'] for q in v).most_common(1)[0][0] if v else 'H'
    lev = collections.defaultdict(int)
    for x0, y0, x1, y1 in G:
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        if not pa.contains_point((mx, my)):
            continue
        L = math.hypot(x1 - x0, y1 - y0)
        if o == 'H' and abs(x1 - x0) < 0.05 and L < 7:   # juntas verticales (bloques a lo largo de x)
            lev[round(mx, 0)] += 1
        if o == 'V' and abs(y1 - y0) < 0.05 and L < 7:   # juntas horizontales
            lev[round(my, 0)] += 1
    counts = sorted(lev.values())
    moda = collections.Counter(counts).most_common(1)[0][0] if counts else 0
    res[k] = dict(dir=o, niveles=len(lev), filas_moda=moda, filas_max=max(counts) if counts else 0, n_vig=len(v))
    print(k, res[k])
json.dump(res, open(os.path.join(OUT, 'p03_filas_eps.json'), 'w'), indent=1)
