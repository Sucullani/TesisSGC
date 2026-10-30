# Modelo de costos y simulación de Monte Carlo

Esta carpeta contiene el modelo con el que la tesis evalúa *ex ante* el efecto del Sistema de Gestión de la Calidad (SGC) sobre el costo de ejecutar las losas alivianadas que faltan (2.234,60 m²). Es la «posprueba simulada» del Capítulo 2 (secciones 2.7 a 2.9) y la base de los resultados del Capítulo 3.

## Archivos

| Archivo | Qué es |
|---|---|
| `parametros.json` | Todos los datos de entrada, cada uno con su fuente: precios del contrato, APU de referencia, cantidades teóricas por m², desperdicios de la línea base, eficacia del SGC y costos del SGC. |
| `modelo_costos.py` | Programa que calcula el APU de referencia, la línea base, la simulación y el contraste de hipótesis. |
| `variantes.py` | Análisis de robustez: repite la simulación con variantes de los parámetros y escribe `tablas_latex/tab_variantes.tex` y `resultados/variantes.json`. |
| `macros_en.py` | Escribe `tablas_latex/valores_modelo_en.tex` (cifras con formato inglés para el *Abstract*). Se ejecuta solo al final de `modelo_costos.py`. |
| `resultados/resumen_resultados.json` | Resumen numérico de todos los resultados. |
| `resultados/simulacion_muestras.csv` | Cada uno de los escenarios simulados (para revisarlos en Excel). |
| `tablas_latex/` | Tablas y cifras que la tesis inserta automáticamente (`valores_modelo.tex` y `valores_modelo_en.tex`). |
| `figuras/` | Gráficos de la tesis y de la presentación (PDF y PNG). |

## Cómo reproducir los resultados

```bash
cd 06_Modelo_de_Costos_y_Simulacion
python3 modelo_costos.py   # modelo, tablas, figuras y macros (también las del Abstract)
python3 variantes.py       # análisis de robustez (Tabla de variantes del Capítulo 3)
```

Requiere Python 3 con `numpy`, `scipy` y `matplotlib`. La semilla está fija, así que cada ejecución da exactamente los mismos números. Después de ejecutarlo, vuelve a compilar la tesis (`latexmk` en `05_Tesis_LaTeX`) para que el texto tome las cifras nuevas.

## Idea del modelo en una línea

Costo de 1 m² de losa = costo con las cantidades de los planos + costo de lo que se desperdicia o se rehace + costo de controlar la calidad. Se calcula **sin SGC** (como se hizo la primera losa) y **con SGC**, miles de veces, variando los datos inciertos dentro de rangos documentados. La reducción del costo es la diferencia entre ambos.
