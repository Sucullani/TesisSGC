#!/usr/bin/env python3
"""Quita de bib/00_base.bib las entradas cuya clave también está en otro .bib de bib/.

Las fichas de cada grupo verificaron sus referencias en los PDF; como biber usa la
primera definición que encuentra y 00_base.bib se carga primero, las versiones
antiguas de 00_base.bib taparían las corregidas. Uso: python3 scripts/depurar_bib.py
"""
import re
from pathlib import Path

BIB = Path(__file__).resolve().parents[1] / "bib"
ENTRADA = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,")


def entradas(texto):
    """Devuelve (clave, inicio, fin) de cada entrada, respetando llaves anidadas."""
    res = []
    for m in ENTRADA.finditer(texto):
        nivel, i = 0, texto.index("{", m.start())
        for j in range(i, len(texto)):
            if texto[j] == "{":
                nivel += 1
            elif texto[j] == "}":
                nivel -= 1
                if nivel == 0:
                    res.append((m.group(1), m.start(), j + 1))
                    break
    return res


base = BIB / "00_base.bib"
otras = {}
for f in sorted(BIB.glob("*.bib")):
    if f.name == base.name:
        continue
    for clave, _, _ in entradas(f.read_text(encoding="utf-8")):
        otras.setdefault(clave, f.name)

texto = base.read_text(encoding="utf-8")
quitar = [(c, a, b) for c, a, b in entradas(texto) if c in otras]
for c, a, b in sorted(quitar, key=lambda t: -t[1]):
    texto = texto[:a] + f"% [{c}: definida en {otras[c]}]" + texto[b:]
base.write_text(texto, encoding="utf-8")
print("Quitadas de 00_base.bib:", ", ".join(c for c, _, _ in quitar) or "ninguna")

# Duplicados entre los demás archivos (se informan para corregir a mano)
vistos = {}
for f in sorted(BIB.glob("*.bib")):
    for clave, _, _ in entradas(f.read_text(encoding="utf-8")):
        if clave in vistos and vistos[clave] != f.name:
            print(f"AVISO: {clave} está en {vistos[clave]} y en {f.name}")
        vistos.setdefault(clave, f.name)
