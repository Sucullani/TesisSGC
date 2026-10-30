# Método de cálculo de las cantidades teóricas de la primera losa (ítem 13)

> Ítem 13 «HºSº losa aliv. c/vigueta simple pretensada y plastoformo h = 25 cm» — primera losa, 41 paños, 1.109,84 m².
> Producto: `Cantidades_Teoricas_Primera_Losa_por_Pano.csv` (una fila por paño). Scripts reproducibles en `scripts/`.
> Convención: **[H]** hecho documentado · **[C]** cálculo propio · **[S]** supuesto (con fuente o justificación) · **[P]** pendiente.
> Formato numérico boliviano (punto de miles, coma decimal). Fecha de elaboración: 30/10/2026.

## 1. Fuentes utilizadas

| Fuente | Qué se tomó |
|---|---|
| `01_Planos/Plano_01_Geometria_Sistema_de_Ejes_Primera_Losa.pdf` (vectorial) | Áreas A1…A41 con coordenadas, ejes y cotas entre ejes, secciones de vigas. |
| `01_Planos/Plano_02_Seccion_y_Detalles_Losa_Viguetas_Pretensadas.pdf` (vectorial + 1 imagen) | Módulo, alturas, perfil del bloque, armaduras, detalle de apoyo (§3). |
| `01_Planos/Plano_03_Cantidad_de_Viguetas_Primera_Losa.pdf` (vectorial) | Etiquetas de cantidad de viguetas, cotas rojas de longitudes, líneas de viguetas y bloques. |
| `03_Planillas_y_Computos/PAO_03_…xlsx`, hoja «COMPUTOS MÉTRICOS» | Áreas del cómputo (filas 1033–1037 y 1053–1088); acero de la losa (fila 538: 3 × 4.171,18 kg). |
| Expediente del ítem 13, p. 8 (PRETENSA) y p. 9 (UNICON) | Sistema 20 + 5 cm, módulo 50 cm; Plastobloq 20 × 100 × 44 cm, 2.350 piezas. |
| `02_Especificaciones_Tecnicas/ET_…pdf`, p. 3 | Plastoform 100 × 50 × 20 cm, parrilla de compresión y negativos incluidos en el ítem. |
| `04_Bibliografia/05_Documentos_Tecnicos/Concretec_ES-CC-1021_2016…` y `…ES-CC-1022_2018…` | Geometría y masa de vigueta tipo; tabla de complementos y pasos (comparación). |

## 2. Paso 1 — Áreas por paño (Plano 01 frente al Excel) [H]

- Se extrajeron con `pymupdf` los 41 textos «Ax = valor M2» del Plano 01 con sus coordenadas (script `p01_p03_textos.py`; tabla `intermedios/plano01_areas_vs_excel.csv`).
- **Resultado:** las 41 áreas del Plano 01 son **idénticas** a las del Excel (diferencia 0,00 m² en todos los paños); suma = **1.109,84 m²** = celda K1031 (`=SUM(I1033:I1037)+SUM(I1053:I1096)`).
- Las áreas son **áreas libres entre caras de vigas** (p. ej., A4 = 45,97 m² frente a (5,00 − 0,125 − 0,15) × (10,00 − 0,25) = 46,07 m²) [C]. Por eso el hormigón de vigas (ítem 12) queda fuera del ítem 13.
- El cómputo escaneado del expediente (pp. 2–3) repite las mismas 41 áreas.

## 3. Paso 2 — Datos del Plano 02 (sección y detalles) [H]

| Elemento | Dato en el plano | Observación |
|---|---|---|
| Corte transversal (esc. 1:25) | Separación entre ejes de viguetas **0,50 m**; altura de complemento **0,15 m**; carpeta **0,05 m** («Carpeta de compresión e = 5 cm»); «**φ6 c/20 EN AMBAS DIRECCIONES**»; «Vigueta pretensada», «Bloques de plastoformo». | 0,15 + 0,05 = 0,20 m **≠** 25 cm del ítem, de la ET y del certificado PRETENSA (20 + 5). |
| Nervio transversal | Módulos de 0,50 m; perfil del bloque: 0,03 m a cada lado en la parte superior (→ ancho superior 0,44 m), **ancho inferior 0,40 m**, altura 0,15 m. Corte A-A′: sección **0,10 × 0,15 m**, **P1: 2 φ10** (inferior), **P2: 2 φ10** (superior) y un estribo (sin diámetro ni separación). | La ubicación de los nervios **no** se indica en ningún plano. |
| Detalle típico de apoyo de vigueta en viga peraltada «(Con Ref. Mom Negativo)» (imagen) | «ACERO NEGATIVO» en la carpeta sobre la viga; «**5 cm. Empotramiento**» de la vigueta en la viga; los bloques llegan a la cara de la viga (sin macizado). | No se dan diámetro, separación ni longitud de los negativos. |
| Detalle de vigueta paralela a una viga (esc. 1:25) | Leyendas: CAPA DE COMPRESIÓN, FE DE ACUERDO A PLANOS, PLASTOBLOCK, VIGUETA PREFABRICADA, ENCOFRADO. | Vigueta colocada junto a la viga, bloques a ambos lados. |
| Viguetas que se apoyan sobre una viga a vaciar (esc. 1:25) | Leyendas: ARMADURA DE ACUERDO A PLANOS, PLASTOBLOCK, VIGUETA PREFABRICADA, ENCOFRADO. | Viguetas que entran en la viga vaciada in situ. |
| Sección losa c/viguetas pretensadas (esc. 1:25) | Carpeta de compresión, vigueta pretensada, plastoformo (bloque con chaflanes que asienta en las alas de la vigueta). | Sin cotas. |
| Recubrimientos | **No acotados** en el Plano 02. | [P] |

## 4. Paso 3 — Viguetas por paño desde el Plano 03 [H + C]

1. **Asociación de etiquetas** (`p01_p03_textos.py`): transformación lineal Plano 01 → Plano 03 ajustada con los globos de ejes A…M y 1…16 (residuo máximo 0,07 pt; escala del Plano 03 = 12,564 pt/m). Cada etiqueta de cantidad (número negro de 5,53 pt) se asocia al rótulo de área más cercano: **37 etiquetas, 37 paños distintos** (distancias 0,7–35 pt; ver `intermedios/plano03_etiquetas_y_cotas.csv`). A18, A22, A23 y A27 no tienen etiqueta de cantidad (solo cotas rojas).
2. **Detección automática** (`p03_viguetas.py`): cada vigueta está dibujada como **dos líneas paralelas** del mismo color separadas 0,8–1,8 pt (amarillo A–B″, blanco B″–D, oliva D–F, verde, cian, azul, magenta, rojo, naranja). Se emparejan las líneas, se recorta cada eje de vigueta por un ráster de las vigas (trazos negros de 0,72 pt y columnas) y cada tramo libre se asigna al paño cuyo polígono por ejes lo contiene. Las líneas están dibujadas **de eje a eje** (p. ej., verdes de 15,0 m de J a F que cruzan G y H), de modo que: luz entre ejes = tramo dentro del polígono; **luz libre (cara a cara) = tramo libre + 0,06 m** (corrección por el grosor del trazo rasterizado).
3. **Verificación visual** con recortes ampliados (zona izquierda, centro, ángulo inferior izquierdo y franja superior): confirma las lecturas siguientes.

| Paño | Etiqueta del plano | Viguetas dibujadas | Adoptadas | Comentario |
|---|---|---|---|---|
| A1–A6 | 19 | 19 | 19 | Dirección de ejes literales (apoyos en ejes A, B″, D, F, G, H, J). |
| A7 | 10 | 10 + 9 | **19** | «10» = 10 viguetas rojas de 2,49 m (J–K × 1–3); la parte triangular K3–L4–K5 tiene 9 viguetas sin etiqueta (3,0…4,83 m entre ejes; cotas 3,00/3,50/4,50). |
| A13, A33 | 4 | 7 y 8 | 7 y 8 | 4 viguetas de 5,00 m entre ejes + triángulo (cotas 2,0/1,50/1,00); en A33 hay además una vigueta sobre la línea J (≈2,50 m) sin cota. |
| A18, A27 | — | 10 | 10 | Cotas 4,90; 4,80; 4,70; 4,60; 3,40; 2,80; 2,20; 1,60; 1,00 + una vigueta sin cota sobre la línea J (≈4,40 m). |
| A22 | — | 14 | 14 | 10 × 6,20 m (eje I → eje K′) + en cada cuña 1 × 4,80 y 1 × 2,30 m. |
| A23 | — | 6 | 6 | 6,50; 5,50; 4,50; 3,50; 2,50; 1,50 m. |
| A40 | 10 | 14 | 14 | 9 en I–K + 1 sobre la línea K + 4 en el triángulo (4,00/3,00/2,00/1,00). |
| A41 | 9 | 13 | 13 | 9 en H–J + 4 en el triángulo (2,00/1,50/1,00 + 1 sin cota sobre J). |
| A16 | 2 | 0 | 2 | Sin viguetas dibujadas; se adopta la etiqueta y la cota 1,60 m (celda libre 1,10 × 1,28 m). |
| **A34, A35, A36** | **20** | **18** | **19** | **Caso ambiguo:** etiqueta 20, dibujo 18; 10,00 m entre ejes (12–16) con módulo 0,50 m admite 19, igual que la franja homóloga 1–5. |
| **A38** | **20** | **19** | **19** | Ídem. |
| Resto (A8–A12, A14, A15, A17, A19–A21, A24–A26, A28–A32, A37, A39) | = dibujo | = etiqueta | = etiqueta | Dirección de ejes numéricos (luz 5,00 m) salvo A37 y A39 (ejes literales). |

- Las cotas negras del borde (4,20 · 4,00 · 4,40 · 5,00 · 5,00 · 5,00 · 2,50 y 5,00 × 5) son **luces entre ejes** (A–B″, B″–D, D–F, F–G, G–H, H–J, J–K; 5–6, 6–8, 8–9, 9–11, 11–12), no longitudes de pedido.
- Las filas de bloques dibujadas (líneas grises: juntas cada 1,00 m) dan **n + 1 filas** en los paños regulares (p. ej., A4: 20 filas de 0,40 m, las de borde de 0,30–0,33 m). El sombreado no es un plan de cortes (empieza con piezas de 0,66 m) y en la franja inferior es incompleto (16–17 filas).

## 5. Paso 4 — Viguetas (piezas y metros) [C]

- **Luz libre** Lᵢ (cara a cara) = medida del Plano 03 (ráster) + 0,06 m.
- **Longitud de vigueta** ℓᵢ = Lᵢ + 2 × 0,05 m **[S]** (empotramiento de 5 cm por extremo según el detalle de apoyo del Plano 02; la ficha Concretec ES-CC-1022 no fija el apoyo). Sensibilidad con 0,10 m por extremo en §11.
- En A1, A2, A34 y A35 la viga plana curva VP 30 × 25 cruza el paño; se asume **vigueta continua** (el dibujo la muestra de viga a viga) con la luz libre máxima del paño **[S]**.
- Totales: **531 viguetas; 2.205,1 m; 0,478 pza/m²; 1,987 m/m²** (el valor ideal del módulo de 0,50 m es 2,0 m/m²).

## 6. Paso 5 — Complementos de EPS [C]

**Filas.** Cada par de viguetas consecutivas separadas ≤ 0,60 m delimita una fila; en los bordes se mide por ráster la distancia e del eje de la vigueta a la cara de la viga (a 25 %, 50 % y 75 % de su longitud). Si el ancho útil e − 0,03 m ≥ 0,15 m se coloca una fila (bloque cortado a lo largo si e − 0,03 < 0,44 m); si el borde es inclinado (e varía > 0,08 m) la fila se toma con la mitad de la longitud. Longitud de fila = media de las luces libres de las viguetas que la limitan (en A1/A2/A34/A35 se descuenta la VP curva).

**Piezas (Plastobloq 20 × 100 × 44, largo 1,00 m):**
- Neto (sin desperdicio) = Σ (L_fila − n_nerv × 0,10) / 1,00.
- Práctico (piezas enteras por fila, sin reaprovechar recortes entre filas) = Σ ⌈(L_fila − n_nerv × 0,10) / 1,00⌉.

**Nervios transversales.** Escenario base **S1 [S]**: un nervio de 0,10 m a media luz en los paños con luz libre media ≥ 4,0 m (23 nervios). Los planos no ubican nervios; el criterio es una práctica usual que debe confirmar el proyectista. Escenario S0: sin nervios.

**Bloque de la ET (100 × 50 × 20).** Un bloque de 0,50 m de ancho no cabe en el módulo de 0,50 m del plano y de PRETENSA. Con la misma holgura de 0,06 m del sistema suministrado (0,44 + 0,06 = 0,50), el módulo compatible sería 0,56 m **[S]**: filas_ET = round(filas × 0,50 / 0,56). Resultado: **1.996,9 pza (1,80 pza/m²)**, es decir, unas 11 % menos piezas y también menos viguetas. Es solo una referencia de lo que habría implicado cumplir la ET; no sirve para medir el desperdicio.

## 7. Paso 6 — Hormigón in situ [C]

V = A_paño × 0,25 − V_EPS − V_vigueta. Detalle:
- **Bloque [S]:** perfil trapecial del Plano 02 (ancho superior 0,44 m, inferior 0,40 m) con la altura suministrada de 0,20 m → A_bloque = 0,084 m²/m. Las filas de borde cortadas se reducen en proporción a su ancho. Cada nervio resta 0,10 m de bloque por fila.
- **Vigueta [S]:** 17,2 kg/m (Concretec ES-CC-1022, Santa Cruz/La Paz/Sucre; no hay ficha PRETENSA en el repositorio) / 2.500 kg/m³ → 0,00688 m²; solo cuenta la parte comprendida en la luz libre.
- No hay macizados en los planos: el detalle de apoyo muestra los bloques hasta la cara de la viga.
- **Módulo ideal** (sin bordes ni nervios): 2 × (0,50 × 0,25 − 0,084 − 0,00688) = **0,0682 m³/m²**. Con el bloque envolvente 0,44 × 0,20 (0,088 m²): 0,0602 m³/m².
- **Comparación con la geometría Concretec** (complemento 20 × 42 × 100, a = 42 cm, d = 38 cm, paso 50 cm, vigueta 17,2 kg/m, carpeta 5 cm): 2 × (0,125 − 0,080 − 0,00688) = **0,0762 m³/m²**. La ficha ES-CC-1022 da paso 50–55–58–60 cm, h₁ de 10 a 25 cm y h₂ = 5 cm, pero ninguna de las dos fichas publica consumo de hormigón. La cifra es un cálculo propio con sus dimensiones; el Plastobloq de 44 cm deja menos hueco que el de 42 cm.

## 8. Paso 7 — Acero de la losa [C]

| Componente | Fórmula | Supuestos |
|---|---|---|
| Malla φ6 c/20 en dos direcciones [H: Plano 02, ET] | L = (2·A/0,20 + (P/2/0,20)·2·0,15) × 12/11,70; kg = L × 0,2220 | **[S]** Anclaje de 0,15 m por extremo de barra en la viga; traslape de 0,30 m por barra de 12 m; P = perímetro del polígono por ejes. |
| Negativos (continuidad) [H: existen; cuantía no definida] | 1 barra por vigueta en cada apoyo con viguetas alineadas a ambos lados (detección automática: 332 pares); ℓ = 0,25·(L₁ + L₂) + ancho de viga | **[S]** φ8 (0,3946 kg/m); sensibilidad con φ6 y φ10. |
| Nervios transversales (S1) [H: sección y barras; ubicación no definida] | 4φ10 × (W + 2 × 0,30) + estribos φ6 c/0,20 de 0,56 m; W = A/L_media | **[S]** Anclaje 0,30 m; estribo φ6 c/20 (el plano dibuja el estribo sin cota). |

## 9. Resultados — primera losa (escenario base S1)

| Material | Total teórico | Por m² | Componentes |
|---|---|---|---|
| Viguetas | **531 pza / 2.205,1 m** | 0,478 pza/m² · **1,987 m/m²** | Longitud media 4,15 m. |
| EPS Plastobloq — neto S1 | **2.238,1 pza** | **2,017 pza/m²** | S0 (sin nervios): 2.272,6 (2,048 pza/m²). |
| EPS Plastobloq — práctico S1 | 2.476 pza | 2,231 pza/m² | S0: 2.516 (2,267 pza/m²). |
| EPS bloque de la ET (módulo 0,56 m) | 1.996,9 pza | 1,799 pza/m² | Referencia (§6). |
| Hormigón in situ S1 | **79,30 m³** | **0,0715 m³/m²** | Carpeta 55,49 m³ (0,050 m³/m²) + nervaduras; S0: 76,48 m³ (0,0689 m³/m²). |
| Acero S1 | **3.573,1 kg** | **3,22 kg/m²** | Malla 2.685,3 kg (2,42 kg/m²) + negativos 330,4 (0,30) + nervios 557,4 (0,50). |
| Acero S0 (sin nervios) | 3.015,7 kg | 2,72 kg/m² | Malla + negativos. |

**Segunda y tercera losa** (paños homólogos × 2 = 2.219,68 m², como en el cómputo del contrato modificado): 1.062 viguetas / 4.410,2 m; EPS neto 4.476 pza (práctico 4.952); hormigón 158,6 m³; acero 7.146,2 kg (S1) o 6.031,4 kg (S0).
**Saldo de 2.234,60 m²** (consumos por m² × área): 4.439,8 m de vigueta (≈ 1.069 pza); EPS 4.506 pza; hormigón 159,7 m³; acero 7.194,2 kg (S1) o 6.072,0 kg (S0).

## 10. Comparación con lo entregado y lo computado; IDM preliminares [C]

**EPS (UNICON, 2.350 piezas, p. 9 del expediente).** IDM = (real − teórico) / teórico × 100:

| Teórico de referencia | Piezas | IDM |
|---|---|---|
| Neto S1 (base) | 2.238,1 | **+5,0 %** (+112 pza) |
| Neto S0 (sin nervios) | 2.272,6 | +3,4 % |
| Regla de 2 pza/m² | 2.219,7 | +5,9 % |
| Práctico S1 (sin reaprovechar recortes entre filas) | 2.476 | −5,1 % |

Lectura: lo entregado está entre el neto y el práctico. Es compatible con un 3–6 % de desperdicio sobre el neto si se reaprovecharon recortes. Supuesto crítico: que las 2.350 piezas se destinaron solo a la primera losa y que no hubo devoluciones ni sobrantes **[P]**: el expediente no tiene notas de entrega ni kardex.

**Acero de la losa.** El cómputo de cierre del ítem 8 (Excel, fila 538) registra 4.171,18 kg por losa (3,76 kg/m²) y lo multiplica por 3 (12.513,54 kg):
- 4.171,18 kg es **16,7 % mayor** que el teórico S1 (3.573,1 kg; +598,1 kg ≈ Bs 10.021,75 al PU de 16,75584 Bs/kg) y **38,3 % mayor** que el S0. Con negativos φ10 la diferencia baja al 11,0 % y con nervios en todas las luces ≥ 3 m, al 9,2 %. La cuantía computada está **por encima del rango teórico obtenido** (2,72–3,44 kg/m²).
- 12.513,54 kg equivale a **3,5 veces** el teórico de una losa (+250 %). Solo hay ejecutada una losa (ítem 13: 1.109,84 m²), así que el factor 3 añade 8.342,36 kg (≈ Bs 139.783,25) de losas no ejecutadas. Además, la ET del ítem 13 incluye la parrilla y los negativos en el precio por m². Ambos puntos se presentan como **inconsistencias documentales que requieren verificación por la Supervisión y la Fiscalización**.
- En la versión firmada de la PAO 3 (expediente, p. 2) el descuento del ítem 8 es −1.862,81 kg (acumulado 50.561,84 kg), distinto del Excel (−1.915,16 kg; acumulado 50.509,49 kg). Ver `Expediente_Item13_Contenido.md`.

**Hormigón.** No hay en el repositorio volúmenes vaciados de la losa (m³ por vaciado, remisiones o vales de cemento). El IDM del hormigón queda **[P]**. Teórico de referencia: 79,30 m³ (0,0715 m³/m²).
**Viguetas.** No hay notas de entrega de PRETENSA. El IDM de viguetas queda **[P]**. Teórico: 531 pza / 2.205,1 m, con el detalle de longitudes por paño en el CSV.

## 11. Sensibilidad (`scripts/sensibilidad.py`, `intermedios/sensibilidad.json`)

| Escenario | Viguetas (m) | EPS neto | IDM EPS | Hº (m³/m²) | Acero (kg/m²) | 4.171,18 vs teórico |
|---|---|---|---|---|---|---|
| Base S1 | 2.205,1 | 2.238,1 | +5,0 % | 0,0715 | 3,22 | +16,7 % |
| Negativos 1φ10 / 1φ6 | = | = | = | = | 3,39 / 3,09 | +11,0 % / +21,7 % |
| Bloque envolvente 0,088 m² | = | = | = | 0,0636 | = | = |
| n según etiquetas (20 en franja inferior) | 2.221,9 | 2.258,9 | +4,0 % | 0,0698 | 3,22 | +16,7 % |
| n según dibujo (18/18/18/19) | 2.193,2 | 2.226,5 | +5,5 % | 0,0724 | 3,22 | +16,8 % |
| Nervio si luz ≥ 3,0 m (34 nervios) | = | 2.222,7 | +5,7 % | 0,0726 | 3,44 | +9,2 % |
| Sin nervios (S0) | = | 2.272,6 | +3,4 % | 0,0689 | 2,72 | +38,3 % |
| Geometría del Plano 02 (0,15 + 0,05) | = | = | = | 0,0628 | = | = |
| Vigueta de 19,5 kg/m | = | = | = | 0,0697 | = | = |
| Malla sin anclajes ni traslapes | = | = | = | = | 3,02 | +24,5 % |
| Apoyo de 0,10 m por extremo | 2.258,2 | = | = | = | = | = |

## 12. Incertidumbres y pendientes

1. **Nervios transversales:** el Plano 02 tiene el detalle (0,10 × 0,15; 2φ10 + 2φ10; estribo), pero ningún plano los ubica. Son el supuesto que más mueve el acero (2,72 → 3,44 kg/m²) [P: confirmar con el proyectista o la Supervisión].
2. **Negativos:** cuantía no definida («de acuerdo a planos»); se asumió 1φ8 por vigueta y apoyo continuo, con 0,25·L a cada lado.
3. **Altura del complemento:** 0,15 m en el Plano 02 frente a 0,20 m en la ET, PRETENSA y UNICON. Se usó 0,20 m (material suministrado).
4. **Viguetas de la franja inferior (A34–A36, A38):** etiqueta 20 frente a dibujo 18/19. Se adoptó 19 (geometría).
5. **Perfil del bloque y sección de la vigueta:** perfil 0,44/0,40 (Plano 02) y masa de la vigueta Concretec (no PRETENSA). Afectan sobre todo al hormigón (±0,008 m³/m²).
6. **Medición sobre el dibujo:** precisión de ±0,05 m en las luces (ráster de 8 px/pt). Las líneas se dibujaron eje a eje y las luces libres se obtuvieron restando la parte de viga, con la corrección de 0,06 m.
7. **Paños curvos (VP 30 × 25):** se asumió vigueta continua bajo la viga plana.
8. **Entrega de EPS:** no se sabe si las 2.350 piezas fueron solo para la primera losa ni si hubo sobrantes [P: notas de entrega o kardex].
9. **Sin datos reales** de viguetas, hormigón ni acero de la losa (remisiones, vaciados, planillas de fierro) [P].

## 13. Reproducibilidad

```bash
cd 03_Datos_Obra_Edificio_Posgrado/04_Extraccion_de_Datos/scripts
python3 p01_p03_textos.py      # textos de los Planos 01 y 03, transformación y asociación (intermedios/p01_p03_textos.json)
python3 p03_viguetas.py        # detección de viguetas por paño (intermedios/p03_viguetas_por_pano.json)
python3 p03_filas_eps.py       # filas de bloques dibujadas (verificación)
python3 cantidades_teoricas.py # CSV final + intermedios/resumen_cantidades.json
python3 sensibilidad.py        # escenarios
python3 tablas_planos.py       # tablas de trazabilidad (Plano 01 vs Excel; etiquetas del Plano 03)
python3 render_clip.py <pdf> x0 y0 x1 y1 dpi salida.png [rot]   # recortes para verificación visual
```
