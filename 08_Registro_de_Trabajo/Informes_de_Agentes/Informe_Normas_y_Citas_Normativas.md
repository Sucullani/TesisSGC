# Informe del agente: integración de las fichas de normas en los capítulos 1–2

Fecha: 30/10/2026. Modo rápido (sin verificación completa).

Apliqué las correcciones conocidas en los 5 capítulos y compilé una sola vez, sin errores. No edité ningún `.bib`. Quedan para la auditoría las citas que no alcancé a revisar (lista al final).

**Compilación** (`/tmp/claude-0/-home-user-TesisSGC/c22f603c-c695-5c98-b48f-e99a1e2bf286/scratchpad/build_normas/tesis.pdf`, 272 pp.): 0 errores, 0 citas indefinidas y ningún aviso ni error en el `.blg` de biber. Solo queda sin resolver la referencia `sec:discusion`, que ya existía antes y corresponde al cap. 3, que lleva otro agente.

Los archivos están en `/home/user/TesisSGC/05_Tesis_LaTeX/capitulos/`.

| archivo:línea | cita antes | cita después | motivo |
|---|---|---|---|
| 10_introduccion:222 | `aci318_2025 [pp. 601--603]` | `[sección 26.12, pp. 601--607]` | La sección 26.12 de evaluación y aceptación abarca pp. 601–607 |
| 10_introduccion:222 | `aci318_2025 [p. 603]` | `[sección 26.12.2.1, p. 603]` | Faltaba la cláusula; la página era correcta |
| 10_introduccion:302 | `hernandez2018 [p. 372]` (t y Wilcoxon) | t: `[pp. 352--353, 372]`; Wilcoxon: `[pp. 362, 372]` | La prueba t se desarrolla en pp. 352–353. Wilcoxon solo aparece nombrado en la tabla de la p. 372. Se reescribió como «prueba no paramétrica, como la de Wilcoxon» |
| 20_capitulo1:95 | `aci [sección 2.3]` | `[sección 2.3, pp. 39, 43]` | Las definiciones de documentos de construcción e inspección están en pp. 39 y 43 |
| 20_capitulo1:200 | `aci [26.5.4.2]` | `[26.5.4.2, p. 583]` | Página |
| 20_capitulo1:435 y 500 (tablas) | texto «prohibido / no añadir agua» | «sin añadir agua más allá de lo que admite ASTM C94»; en la 500 se suma la cláusula 26.5.2.2 | El ACI 26.5.2.2(g) (p. 580) permite reatemperar dentro de ASTM C94, y la ET no lo prohíbe |
| 20_capitulo1:439 | `[secciones 26.5 a 26.13]` | `[..., pp. 578--611]` | Página |
| 20_capitulo1:504 | `[secciones 26.4 a 26.12]` | `[..., pp. 577--604]` | Página |
| 20_capitulo1:519 | `mopsv [pp. 1, 19]`; `[resuelve tercero]` | `[arts. 1 y 10, pp. 1, 19]`; `[R. M. 271/2023, resuelve tercero]` | Ver nota 1 sobre la CBH-87 |
| 20_capitulo1:521 | 26.12.1.1, 26.12.2.1, 26.12.3.1, 26.12.7, 26.5.3.2, 26.5.4.2, 26.13.1.2 y 26.13.2.1, sin páginas | pp. 601, 603, 603, 606, 581, 583 y 608/610 | La numeración ya era correcta (26.12.7, no 26.12.6); se añaden páginas |
| 20_capitulo1:525 y 566 | `20.2.1.3` / `20.2.1.3 y 26.6.1.2` | p. 409 / pp. 409, 587 | Página |
| 20_capitulo1:537 | `ds5597 [art. 4 y DA quinta]` | Misma cita, con contenido ampliado; se añaden `ds0181_2025compilado [art. 5, incs. c y p, pp. 20, 22]` y `uatf_item13 [p. 14]` | Ver nota 2 |
| 20_capitulo1:560 (fila NB 1225001) | — | Se añade `\textcite[arts. 1 y 10]{mopsv2023nbds}` | La NBDS remite a la NB 1225001 |
| 20_capitulo1:562 (fila NBDS) | `[p. 22]` | `[resuelve tercero; art. 12, p. 22]` | La NBDS es obligatoria por la R.M. 271/2023 |
| 20_capitulo1:564, 730, 742 | 26.12.1.1 / 26.12.2.1 / 26.12.4.1 sin página | pp. 601 / 603 / 604 | Página |
| 20_capitulo1:570 | «R.M. 048/2024 y modelo de DBC» | «R.M. 048/2024; modelo de DBC de 2022 (sustituido)» | El DBC 2022 fue sustituido |
| 20_capitulo1:712 | «El contrato llama trabajo defectuoso…» `dbc2022 [cl. 26.12, p. 74]` | «El modelo de contrato de obras llama…» | La cita es al modelo DBC 2022, no al contrato real de la obra |
| 20_capitulo1:724, 732 | `[sección 2.3]` | `[2.3, p. 43]` / `[2.3, p. 38]` | La definición de f′c está en p. 38 |
| 30_capitulo2:409, 411, 412 | `aci [p. 603]`, `[p. 602]`, `[p. 601]` | Se añaden 26.12.2.1, 26.12.1.1 y 26.12.1.1 | Faltaban las cláusulas; las páginas eran correctas |
| 30_capitulo2:455 | — | Frase nueva + `mopsv [art. 12.I, inc. b, p. 22]` + `pretensa2025` | Ver nota 3 |
| 31_propuesta:146 | 26.12.1.1 | 26.12.1.1, p. 602 | Página |
| 31_propuesta:272 | 26.5.1.1; 26.12.1.1 | p. 578; pp. 601–602 | ASTM C1077 está en p. 601; los técnicos certificados, en p. 602 |
| 31_propuesta:276 | 26.13.2.1 | 26.13.2.1, p. 610 | La regla de los 2 años de registros está en p. 610 |
| 31_propuesta:316 | — | Se añaden la NBDS (`mopsv [p. 22]`) y la NB 1225001, «a la que la NBDS remite» | La recomendación de actualizar la ET ahora apunta al marco vigente |
| 31_propuesta:436 (PPI, punto 8) | 26.4.4.1, 26.5.2.2, 26.5.4.2 | + 26.13.2.2 | El umbral de 40 °F (4,4 °C) solo está en 26.13.2.2(d) |
| 31_propuesta:564 | 26.12.7.1 | 26.12.7.1, p. 606 | Página |
| 32_implementacion:86 | sin cita | `hernandez2018 [pp. 230, 235]` | Validez de contenido y validez de expertos |
| 32_implementacion:91 | `\pendiente` | `\pendiente` ampliado | Falta citar una fuente específica para la V de Aiken, que el libro no trata |
| 32_implementacion:119 | `\parencite{hernandez2018}` para t, Wilcoxon, Shapiro-Wilk y α | t `[pp. 352--353, 372]`; normalidad `[p. 345]`; Wilcoxon `[p. 372]`; α `[p. 342]` | Shapiro-Wilk ya no se atribuye al libro; se añade `\pendiente` para una fuente estadística |

**Notas:**
1. **CBH-87 (20_:519).** La tesis ahora dice que la NBDS no menciona la CBH-87 y la presenta como «la norma que cita la especificación técnica del ítem». Como marco vigente toma la NBDS y la NB 1225001. El `\pendiente` ya no afirma que el D.S. 22976/1991 la declare obligatoria: solo dice que la bibliografía recomendada lo menciona y que no está en el repositorio.
2. **Resolución del contrato (20_:537).** Se añadió, según la disposición adicional quinta del D.S. 5597, que la inviabilidad del ajuste puede considerarse caso fortuito, sin registro del contratista como impedido en el SICOES ni ejecución de la garantía. También se añadieron las definiciones de fuerza mayor y caso fortuito de las NB-SABS, y que la carta del 05/01/2026 invocó ambas.
3. **Plano 02 (30_:455).** La frase nueva dice que la sección de 0,20 m del plano no alcanzaría los 250 mm mínimos de la NBDS para diafragma rígido, mientras la ET, el ítem 13 y el certificado PRETENSA indican 25 cm. Concluye que es un error del plano que la Supervisión debe aclarar; no afirma que la losa construida sea deficiente.

**Ya estaban bien (verificado con PDF o fichas, sin cambios):**
- Hernández-Sampieri (página impresa = PDF − 39) en 10_, 20_ y 30_: pp. 6, 108, 110, 113, 133, 151, 154, 163, 175, 180, 196, 200 y 342.
- NB-SABS: art. 89 (≤ 10 %, ≤ 5 %, ≤ 15 %; pp. 91–93), art. 39 (p. 54) y art. 5 inc. m (p. 21).
- DBC: cláusulas 25, 26.3, 26.6, 26.10, 27, 28, 30.5 y 38.1, con sus páginas. En los 5 archivos no hay funciones del Supervisor o del Fiscal atribuidas a la NB-SABS.
- NBDS: art. 12 (p. 22) y art. 16 (p. 28).
- 26.12.6: no aparecía en ninguno de los 5 archivos.

**No alcancé a revisar (queda para la auditoría):**
1. **31_ L564, párrafo del control del hormigón:**
   - A R26.4.3.1, R26.12.2.1, 26.12.3.1 y 26.12.1.1 les falta la página.
   - El cambio de materiales como mezcla nueva está en R26.4.3.1(d), p. 577. Que «exige nueva aprobación» es inferencia a partir de 26.4.4.1.
   - «Antes del vaciado», en la elección al azar de los pastones, es un añadido del SGC, no del ACI.
   - «Se ajustan la dosificación, el control del agua o la calidad del ensayo» viene de R26.12.3.1(b), pp. 603–604, no de 26.12.3.1.
2. **Páginas que faltan en otras citas del ACI en 31_:**
   - L571 y L589 (26.12.2.1, p. 603).
   - L592: 26.5.3.2 (p. 581), 26.5.4.2 (pp. 583–584), 26.13.2.2 (p. 610) y 26.5.2.2(b) (p. 579).
   - L594: 26.12.4.1 (p. 604).
3. **Tablas del PPI en 20_ y 31_:** 26.6.2, 26.13.3.2/3 (p. 611), 26.11.1.2 (p. 599) y 26.11.2.1 (p. 600). Las cláusulas existen, pero no revisé el contenido de cada fila.
4. **Normas sin PDF en el repositorio, no verificables:** ISO 9001:2026, ISO 9000:2026, NB/ISO 9001:2026, ISO 10005, ISO 10006, NB 997, NB 1225001 y las ASTM. Tampoco pude verificar las fechas de publicación y de transición de la ISO 9001:2026.
5. **Leyes y decretos citados solo por artículo y sin página** (Ley 1178; D.S. 5321, 5406 y 5452): coinciden con las fichas, pero no los releí en el PDF.
6. **10_ L298:** la p. 342 respalda el nivel de 0,05; la equivalencia con un «contraste unilateral» es razonamiento propio de la tesis.
7. **CBH-87 fuera de mis archivos:** no edité `02_abreviaturas.tex` L12 («Código Boliviano del Hormigón Armado de 1987»), que no afirma obligatoriedad. La entrada `cbh87` del `.bib` sigue con autor y editor «por verificar» en un comentario.
8. No toqué citas de tesis ni de artículos, ni detecté en ellas errores evidentes (no las revisé). Por ejemplo, no comprobé `cocarico2022` p. 4, que respalda «NB 1225001 basada en ACI 318».