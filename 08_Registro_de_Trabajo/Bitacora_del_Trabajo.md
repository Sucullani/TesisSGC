# Bitácora del trabajo: tesis SGC, Edificio de Posgrado UATF

Registro de todo lo que se hizo en la sesión de Claude Code en la nube (29 y 30 de octubre de 2026), para continuar en una sesión local.

**Estado al cierre:** la tesis está redactada completa y hay borradores de todos los entregables. La **auditoría general (verificación) no se hizo**, porque el usuario pidió terminar rápido y dejarla para después. El plan está listo en [`Plan_de_Auditoria_Pendiente.md`](Plan_de_Auditoria_Pendiente.md).

## 1. Estado de cada pedido

| Pedido del usuario | Estado | Dónde está |
|---|---|---|
| Borrador final de la tesis (APA del repositorio) | Redactado completo. Falta la auditoría. | [`05_Tesis_LaTeX/Tesis_SGC_Borrador.pdf`](../05_Tesis_LaTeX/Tesis_SGC_Borrador.pdf) (fuente LaTeX en `05_Tesis_LaTeX/`) |
| Explicación en lenguaje sencillo | Borrador terminado, sin revisión | `07_Entregables/Tesis_Explicada_en_Lenguaje_Sencillo.md` (+ `.docx` y `.html`) |
| Citas resaltadas en la bibliografía, con comentario y página | Script y PDF resaltados, sin revisión | `04_Bibliografia/08_Citas_Resaltadas/` (índice `Indice_de_Citas.md/.csv/.xlsx`) |
| Auditoría general y correcciones | **Pendiente** (plan listo) | [`Plan_de_Auditoria_Pendiente.md`](Plan_de_Auditoria_Pendiente.md) |
| Presentación de defensa en HTML y PowerPoint | Borrador, sin revisión | `07_Entregables/Presentacion_Defensa/` |
| Preguntas del tribunal: qué decir y qué no | Borrador, sin revisión | `07_Entregables/Preguntas_del_Tribunal_y_Respuestas.md` (+ `.docx`) |
| Documento Word de toda la tesis | Regenerado al cierre | `07_Entregables/Tesis_SGC_Borrador_Final.docx` |
| Trabajo por fases, con commits directos a `main` | Hecho (sin ramas) | Historial de `main` (sección 10) |

La sección 11 resume lo que entregó cada agente al cierre.

## 2. Qué se hizo, fase por fase

### Fase 1: datos de obra y fuentes

- **Extracción de datos de obra** (`03_Datos_Obra_Edificio_Posgrado/04_Extraccion_de_Datos/`):
  - Planilla de Avance N.º 2 (139 páginas) en tres partes: `PAO02_Contenido_p001-046.md`, `p047-092.md` y `p093-139.md`.
  - Expediente del ítem 13: `Expediente_Item13_Contenido.md`.
  - Cantidades teóricas de la primera losa paño por paño: `Cantidades_Teoricas_Primera_Losa_por_Pano.csv` y `Metodo_Cantidades_Teoricas.md`.
- **Fichas de citas verificadas:** 725 en total. Cada una tiene el texto literal, la página del PDF y la página citable, y se comprobó con búsqueda en el PDF. Están en `04_Bibliografia/07_Fichas_de_Citas/`, en cuatro grupos, cada uno con su `.json` y su `.md` legible:
  - tesis, grupos 1 y 2;
  - artículos y documentos técnicos;
  - normas, legislación y metodología (298 citas).
- **Bibliografía BibLaTeX** en `05_Tesis_LaTeX/bib/`: un archivo por grupo, con las entradas verificadas contra el PDF. Además, `scripts/depurar_bib.py` quita las claves duplicadas de `00_base.bib`.

### Fase 2: redacción de la tesis (LaTeX)

- **Formato APA 7**, según `04_Bibliografia/02_Metodologia_y_Redaccion/Guia_Normas_APA_7ma_Edicion.pdf` (configurado en `preambulo.tex`):
  - papel carta, márgenes de 2,54 cm, Times de 12 pt, interlineado doble y texto alineado a la izquierda;
  - sangría de 1,27 cm y número de página arriba a la derecha;
  - tablas y figuras en estilo APA, y «y» entre autores (biblatex-apa adaptado).
  - Capítulos y secciones van numerados porque lo exige la estructura del Taller 1.
- **Contenido redactado:**
  - Resumen (≈ 247 palabras) y *Abstract*, con las cifras del modelo como macros.
  - Introducción.
  - Capítulo 1: marco teórico y estado del arte.
  - Capítulo 2: diagnóstico y línea base (2.1–2.5), diseño del SGC (2.6), implementación, evaluación *ex ante*, validación y contraste (2.7–2.9).
  - Capítulo 3: resultados y discusión.
  - Conclusiones y recomendaciones.
  - Anexos A a L.
- **Modelo de costos y simulación de Monte Carlo** en `06_Modelo_de_Costos_y_Simulacion/`. Usa 20.000 iteraciones con la semilla 2026 y genera las tablas, las figuras y las macros de cifras (`tablas_latex/valores_modelo.tex`). Así el texto de la tesis se actualiza solo.

### Fase 3: entregables (`07_Entregables/`)

- **Word de la tesis:** conversor propio LaTeX → DOCX (`scripts/tesis_a_docx.py`, documentado en `scripts/README_docx.md`). Respeta el formato APA, convierte las figuras TikZ en imágenes y expande las macros del modelo.
- **Explicación sencilla:** archivos `.md`, `.docx` y `.html`.
- **Preguntas del tribunal:** archivos `.md` y `.docx`.
- **Presentación de defensa:** `.html` autocontenido, `.pptx` con notas del orador y guion con tiempos.
- **Citas resaltadas:** en `04_Bibliografia/08_Citas_Resaltadas/`.

### Fase 4: auditoría

No se hizo. El plan está en [`Plan_de_Auditoria_Pendiente.md`](Plan_de_Auditoria_Pendiente.md), con las revisiones, los problemas ya detectados y los encargos listos para usar.

## 3. Decisiones metodológicas y de datos (el postulante debe conocerlas)

1. **Diseño *ex ante*.** El contrato se paralizó el 05/01/2026 y se resolvió (respuesta de la UATF del 10/02/2026), así que la segunda losa no se construyó. Por eso:
   - la primera losa (41 paños; 1.109,84 m²), ejecutada sin SGC, es la **línea base retrospectiva y documental** (O1);
   - el SGC diseñado es el tratamiento (X);
   - el efecto se evalúa con un **modelo de costos y una simulación de Monte Carlo** sobre los 2.234,60 m² restantes, con escenario de control (sin SGC) y de tratamiento (con SGC).

   El Taller 4 acepta la «modelación de simulación teórica». El diseño es **no experimental**.
2. **Contraste probabilístico.** Se acepta la hipótesis si la probabilidad de cumplir su condición es de al menos 0,95 (equivale a α = 0,05 unilateral).
   - HG: reducción del costo unitario de al menos 5 %.
   - HE1: menor desperdicio.
   - HE2: menor costo de no calidad.
3. **PAO N.º 3 oficial = versión FIRMADA** (expediente, p. 2): ítem 8 con −1.862,81 kg y acumulado de 50.561,84 kg. La versión Excel (−1.915,16 kg) se presenta como segunda versión del documento, es decir, como una inconsistencia que debe verificarse.
4. **Losas superiores:** cada una mide 1.117,30 m² y las dos suman 2.234,60 m², que es el saldo. No son 2 × la primera losa.
5. **APU de referencia reconstruido** (Anexo I). El APU contractual no está disponible. Se reconstruyó con la estructura de costos boliviana (Cocarico, 2022) y precios del INE, y se calibró con el factor κ (0,962 para el ítem 13).
6. **Línea base documentada:**
   - plastoformo: 2.350 piezas entregadas frente a 2.237,9 teóricas, es decir, +5,01 %;
   - acero de losa pagado: 4.171,18 kg frente a 3.572,80 kg teóricos, es decir, +16,75 %;
   - viguetas y hormigón: no hay registros de consumo, así que se usaron rangos de literatura con su página.
7. **Hallazgos sensibles** (acero computado 3 × 4.171,18 kg en el cierre, tres cifras distintas de acero acumulado, dos versiones de la PAO 3): se redactan siempre como **inconsistencias documentales que deben verificar la Supervisión y la Fiscalización**. Nunca como sobrepago ni con nombres de personas.
8. **Integridad.** No se inventaron resultados de expertos, entrevistas ni ensayos. La validación por expertos (V de Aiken) y las entrevistas quedan como `\pendiente` del postulante.

## 4. Resultados principales

Las cifras salen de `valores_modelo.tex`.

| Indicador | Valor |
|---|---|
| Costo unitario de la línea base (calibrado al precio de la losa) | Bs 278,65/m² |
| Reducción media del costo unitario con el SGC | 1,47 % (P5 −0,05 %; P95 3,21 %) |
| Probabilidad de que el SGC reduzca el costo, P(r > 0) | 0,9422 |
| Probabilidad de alcanzar el 5 %, P(r ≥ 5 %) | 0,0008 → **la hipótesis general no se acepta** |
| HE1 (desperdicio) y HE2 (costo de no calidad) | P = 1,00 → **se aceptan** (si el SGC se aplica) |
| Reducción del costo de no calidad | 44,82 % |
| Costo del propio SGC | ≈ 1,79 % del costo unitario |
| Ahorro esperado en los 2.234,60 m² restantes | ≈ Bs 9.177 |
| Eficacia del SGC necesaria para no perder / para llegar al 5 % | 24,8 % / 95,1 % (la literatura reporta entre 10 % y 89 %) |
| Reducción con eficacia del 100 % | 5,35 % |
| Escenario con costos ocultos (Khadim et al., 2023) | r ≈ 3,22 %; P(r ≥ 5 %) ≈ 0,13 |
| Diagnóstico ISO 9001:2026 | 19,8 % de cumplimiento global; 22 no conformidades |

**Lectura.** El SGC reduce el desperdicio y el costo de no calidad, y probablemente el costo total. Pero en un solo ítem no llega al 5 % fijado en el perfil, porque el costo de no calidad del ítem es ≈ 7 % del costo unitario y el propio SGC cuesta ≈ 1,8 %. La recomendación es un SGC «ligero», con controles de alto impacto: control volumétrico del hormigón, despiece del acero, recepción por lotes y conciliación de cantidades.

## 5. Mapa de archivos

| Carpeta o archivo | Contenido |
|---|---|
| `05_Tesis_LaTeX/tesis.tex` | Archivo principal (orden de capítulos, modo borrador `\borradortrue`) |
| `05_Tesis_LaTeX/preambulo.tex` | Formato APA, paquetes, macros, bibliografía |
| `05_Tesis_LaTeX/capitulos/` | `00` carátula · `01` resumen/abstract · `02` abreviaturas · `10` introducción · `20` cap. 1 · `30` cap. 2 (2.1–2.5) · `31` cap. 2 (2.6) · `32` cap. 2 (2.7–2.9) · `40` cap. 3 · `50` conclusiones · `90`, `91`, `91a`, `92` anexos |
| `05_Tesis_LaTeX/bib/` | Bibliografía por grupos |
| `06_Modelo_de_Costos_y_Simulacion/` | `parametros.json`, `modelo_costos.py`, `variantes.py`, `macros_en.py`, resultados, figuras y tablas |
| `07_Entregables/` | Word de la tesis, explicación sencilla, preguntas del tribunal, presentación y scripts |
| `04_Bibliografia/07_Fichas_de_Citas/` | 725 fichas verificadas |
| `04_Bibliografia/08_Citas_Resaltadas/` | PDF resaltados (extractos en obras protegidas) e índice |
| `03_Datos_Obra_Edificio_Posgrado/04_Extraccion_de_Datos/` | Datos extraídos de planillas, expediente y planos |
| `08_Registro_de_Trabajo/` | Esta bitácora, el contexto maestro, las notas de defensa, el plan de auditoría y los encargos a los agentes |

## 6. Cómo regenerar todo

```bash
# 1) Modelo (solo si cambias parametros.json)
cd 06_Modelo_de_Costos_y_Simulacion
python3 modelo_costos.py
python3 variantes.py

# 2) Tesis en PDF (desde 05_Tesis_LaTeX)
cd ../05_Tesis_LaTeX
latexmk                          # genera build/tesis.pdf
cp build/tesis.pdf Tesis_SGC_Borrador.pdf

# 3) Word de la tesis (desde la raíz del repositorio)
cd ..
python3 07_Entregables/scripts/tesis_a_docx.py

# 4) Citas resaltadas (desde la raíz)
python3 04_Bibliografia/08_Citas_Resaltadas/scripts/resaltar_citas.py

# 5) Presentación (si se generó con script)
python3 07_Entregables/scripts/generar_presentacion.py
```

Para la versión final, cambia `\borradortrue` por `\borradorfalse` en `tesis.tex`. Así desaparecen las marcas rojas (`\pendiente`) y los recuadros grises (`\guia`).

## 7. Pendientes que solo puede resolver el postulante

Se marcan en rojo en el PDF con `\pendiente{...}`.

1. Nombres del postulante y del tutor, y el escudo de la UATF (carátula y presentación).
2. **Validación por juicio de expertos** (Anexo C.8 y Anexo D): aplicar el formato a 3–5 ingenieros, calcular la V de Aiken y registrar los resultados en la sección de resultados de expertos y en el Anexo D. Ideal antes de la defensa.
3. **Entrevistas** al Residente, al Supervisor y al Fiscal (guía C.7), y ajustar la lista C.1 si corresponde.
4. **APU contractual del ítem 13** (pedirlo a la Fiscalización) para contrastarlo con el APU de referencia del Anexo I.
5. **NB/ISO 9001:2026** de IBNORCA: contrastar la numeración de subcláusulas (capítulo 2.6 y Anexo C.1) y los principios de la ISO 9000:2026 (capítulo 1).
6. Archivar en el repositorio el **conjunto de datos del INE** de precios de Potosí (introducción).
7. Notas de entrega de PRETENSA y UNICON, vales de cemento y volúmenes por vaciado, si se consiguen, para completar la línea base.
8. Instrucciones de montaje del fabricante de viguetas; verificar tolerancias con la NB 997:2016.
9. Fuente oficial del periodo de transición de ISO 9001:2015 a 2026.
10. Antecedentes locales del repositorio de tesis de Ingeniería Civil de la UATF.
11. Instrumento legal vigente sobre la obligatoriedad de la CBH-87 y de la NB 1225001.
12. Fuente estadística específica para Shapiro-Wilk y Wilcoxon (Hernández-Sampieri no trata la primera).
13. Dedicatoria y agradecimientos (opcionales).

## 8. Verificación pendiente

El detalle está en el [plan de auditoría](Plan_de_Auditoria_Pendiente.md). Lo más importante:

- Verificar **todas las citas** contra las fichas: que el texto diga lo atribuido y que la página sea la correcta. El índice de citas resaltadas marca como «cita sin ficha verificada» las que no coinciden con ninguna ficha: empezar por ahí.
- Verificar **todas las cifras** contra sus fuentes (macros del modelo, planillas, PAO 3 firmada).
- Coherencia entre capítulos: objetivos ↔ resultados ↔ conclusiones ↔ resumen ↔ Anexo A, y decisiones de hipótesis iguales en todas partes.
- Formato APA y compilación: referencias indefinidas, numeración de tablas, cajas desbordadas, revisión visual.
- Revisar los entregables (explicación, preguntas y presentación) contra la versión final de la tesis, y regenerar el Word.

## 9. Cómo continuar en la sesión local

1. Actualiza tu copia: `git pull`.
2. Instala lo necesario:
   - TeX Live o MiKTeX con `biber` y `latexmk`;
   - Python 3 con `numpy`, `scipy`, `matplotlib`, `pymupdf`, `openpyxl`, `python-docx` y `python-pptx`;
   - `pandoc` y LibreOffice (para el Word y las revisiones).
3. Abre Claude Code en la raíz del repositorio. El archivo `CLAUDE.md` le da el contexto. Pídele, por ejemplo: «Lee `08_Registro_de_Trabajo/Bitacora_del_Trabajo.md` y `Plan_de_Auditoria_Pendiente.md` y ejecuta la etapa 1 de la auditoría sobre el Capítulo 3».
4. Al terminar cada etapa: compila, revisa el PDF y haz commit.

## 10. Historial de commits en `main`

Todos los cambios se subieron directamente a `main` (sin ramas). Comandos para revisarlos:

- `git log --oneline`: lista de commits.
- `git show --stat <commit>`: archivos de cada commit.

Commits principales:

- `745b2fe` Fase 1 (parcial): formato APA, modelo de costos y secciones 2.7–2.9.
- `f8ac0d2` Fase 1: extracción de la PAO N.º 2, fichas de citas y bibliografía verificada.
- `1dc5677` Modelo con línea base documentada: cantidades teóricas por paño.
- `76490c5` Formato APA en citas y tablas del modelo; introducción completa.
- `40e1f27` Fichas de normas, bibliografía depurada y versión Word.
- `ecd48c4` Resumen y abstract definitivos; tabla de parámetros con título APA.
- Commits de cierre de esta sesión: Capítulo 3, conclusiones, anexos, entregables y esta bitácora.

## 11. Informe de cierre de cada agente

Se completa al final de la sesión.
