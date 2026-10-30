"""Renderiza un recorte de un plano PDF en coordenadas NO rotadas (las mismas de get_text('words')).
Uso: python3 render_clip.py <pdf> <x0> <y0> <x1> <y1> <dpi> <salida.png> [rot]
rot (opcional): ángulo para girar la imagen resultante (p. ej. 90) y leer textos verticales."""
import sys, pymupdf
from PIL import Image
pdf, x0, y0, x1, y1, dpi, out = sys.argv[1], *map(float, sys.argv[2:6]), int(sys.argv[6]), sys.argv[7]
rot = int(sys.argv[8]) if len(sys.argv) > 8 else 0
d = pymupdf.open(pdf)
p = d[0]
p.set_rotation(0)
pix = p.get_pixmap(dpi=dpi, clip=pymupdf.Rect(x0, y0, x1, y1))
pix.save(out)
if rot:
    im = Image.open(out).rotate(rot, expand=True)
    im.save(out)
print(out, pix.width, pix.height)
