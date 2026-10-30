# Plan de la auditoría pendiente

La auditoría general no se hizo en la sesión en la nube: el usuario pidió terminar rápido y dejar la verificación para después. Este plan sirve para hacerla en la sesión local, por etapas, con Claude Code o a mano.

**Regla de oro:** antes de cambiar algo, comprueba la evidencia en la fuente (PDF y página, planilla, `valores_modelo.tex`). Un hallazgo sin evidencia no se corrige.

## 1. Problemas ya detectados (revisar primero)

| # | Problema | Dónde | Qué hacer |
|---|---|---|---|
| 1 | Citas de Hernández-Sampieri (2018) con contenidos que el libro no trata: Shapiro-Wilk, Monte Carlo, V de Aiken | `32_capitulo2_implementacion.tex`, `91_anexo_instrumentos.tex`, anexo D | La página impresa es la del PDF − 39. Prueba *t*: p. 352. Wilcoxon solo nombrado en la tabla de la p. 372. Validez de expertos: p. 235. Buscar otra fuente para Shapiro-Wilk y para la V de Aiken. |
| 2 | Cláusula del ACI 318-25 para resultados bajos | Capítulos 1, 2 y 3 | Es la 26.12.7 (núcleos: promedio ≥ 0,85 f′c y ninguno < 0,75 f′c), pp. 606–607. La 26.12.6 es de hormigón liviano. La página impresa es la del PDF − 1. |
| 3 | La CBH-87 se presenta como «obligatoria por el D.S. 22976/1991» sin fuente verificada | Capítulo 1, contexto | Según las fichas, la R.M. 271/2023 declara obligatoria la NBDS, que remite a la NB 1225001. Redactar con prudencia o conseguir el instrumento legal. |
| 4 | Modelo de DBC 2022 sustituido por la R.M. 048/2024; funciones del Supervisor y del Fiscal | Capítulos 1 y 2 | Están en el DBC (cláusulas 25–27 y 38), no en la NB-SABS. |
| 5 | Plano 02: complemento de 0,15 m + carpeta de 0,05 m = 0,20 m | Capítulo 2 (diagnóstico) | Está por debajo de los 250 mm mínimos de la NBDS para diafragma rígido. Presentarlo como error del plano: lo construido es 20 + 5 = 25 cm según la ET, el ítem 13 y PRETENSA. |
| 6 | Las secciones de la introducción se numeran 1, 1.1, 1.2…, igual que el Capítulo 1 | `10_introduccion.tex` | Fue una decisión deliberada, pero las referencias «sección 1.2» son ambiguas. Decidir con el tutor, o escribir «sección 1.2 de la Introducción». |
| 7 | `\small` quizá no se aplica dentro de las tablas flotantes | `preambulo.tex` (`\AtBeginEnvironment{table}`) | Comprobarlo en el PDF y corregirlo si hace falta. |
| 8 | Etiquetas que el Capítulo 2 cita y que crea el Capítulo 3: `tab:resultado-determinista`, `sec:resultados-expertos`, `tab:variantes` | `40_capitulo3_resultados.tex` | Compilar y confirmar que no queden referencias indefinidas. |
| 9 | Tablas largas sin título APA | Anexos C (`91_anexo_instrumentos.tex`) y otros | Ponerles título o dejar constancia de que son formularios. La numeración de tablas debe quedar consecutiva. |
| 10 | Capítulos largos: Cap. 1 ≈ 44 páginas; sección 2.6 ≈ 37 páginas | `20_`, `31_` | Valorar recortes con el tutor. |
| 11 | Título de la lista final: «Bibliografía» (Taller 1) frente a «Referencias» (guía APA) | `preambulo.tex` / `tesis.tex` | Se mantuvo «Bibliografía». Confirmar con el tutor. |
| 12 | Documentos de planificación con el diseño antiguo (cuasi-experimental) | `01_Titulo_y_Consistencia/`, `02_Indice_y_Capitulos/` | Actualizarlos o marcarlos como versión del perfil. |
| 13 | `Resumen_de_Datos_de_Obra.md` y `Bibliografia_Recomendada.md` quizá desactualizados | `03_...`, `04_...` | Contrastarlos con la tesis. |
| 14 | Entregables escritos en paralelo con el Capítulo 3, sin revisión | `07_Entregables/` | Contrastar cifras y conclusiones con la versión final de la tesis. |
| 15 | La versión Excel de la PAO 3 aparece en tablas o cálculos donde debería usarse la firmada | Capítulos 2 y 3, anexos | La versión oficial es la firmada (−1.862,81 kg; acumulado de 50.561,84 kg). |

## 2. Etapas

### Etapa 1: revisión por grupos de archivos

Hacer una revisión por grupo, con tres lentes cada una:

| Grupo | Archivos |
|---|---|
| G1 | `01_preliminares`, `02_abreviaturas`, `10_introduccion` |
| G2 | `20_capitulo1_marco_teorico` |
| G3 | `30_capitulo2_diseno_sgc` |
| G4 | `31_capitulo2_propuesta_sgc` |
| G5 | `32_capitulo2_implementacion`, `40_capitulo3_resultados`, `50_conclusiones`, `92_anexo_modelo` |
| G6 | `90_anexos`, `91_anexo_instrumentos`, `91a_lista_verificacion_iso9001` |
| G7 | `bib/*.bib` (lista de referencias) |

**Lente A, cifras y hechos.** Cada número debe coincidir con su fuente:

- macros de `06_Modelo_de_Costos_y_Simulacion/tablas_latex/valores_modelo.tex` (los números del modelo deben ir con macros, no escritos a mano);
- `resultados/*.json`;
- `08_Registro_de_Trabajo/Contexto_Maestro.md` (secciones 4, 7, 8 y 9);
- `03_Datos_Obra_Edificio_Posgrado/04_Extraccion_de_Datos/*.md` y el CSV de cantidades teóricas.

Revisar también la aritmética, las unidades, las fechas y el formato boliviano (1.109,84).

**Lente B, citas y APA.** Para cada `\parencite` y `\textcite`:

- la clave existe;
- lo atribuido está en la fuente (fichas en `04_Bibliografia/07_Fichas_de_Citas/*.json`, o el PDF en esa página);
- la página es la correcta;
- no hay citas de segunda mano;
- el formato APA es correcto (p./pp., «y» entre dos autores, *et al.* desde tres).

En G7, revisar cada entrada contra la portada del PDF (autores, año, título, institución, URL o DOI).

**Lente C, redacción y estructura:**

- ortografía y tildes; registro impersonal; resultados en pasado y sin juicios de valor (Taller 5);
- cada tabla y figura se menciona en el texto, tiene título arriba y nota abajo;
- las siglas se definen la primera vez y figuran en la lista de abreviaturas;
- la terminología es uniforme (IDM, CNC, CC, CU, PAF, SGC, EPS/plastoformo);
- no hay restos del diseño antiguo (cuasi-experimento, prueba *t* como método principal).

Cada hallazgo se anota con: archivo, ubicación, problema, evidencia, corrección y gravedad (alta, media o baja). Otro revisor (u otra pasada) intenta **refutar** cada hallazgo antes de corregirlo.

### Etapa 2: revisiones globales

1. **Compilación y formato.** Compilar con `latexmk -f` y revisar errores, referencias o citas indefinidas, etiquetas duplicadas y cajas desbordadas de más de 10 pt. Revisar los índices de tablas y figuras (numeración sin saltos). Mirar unas 20 páginas repartidas por todo el documento: márgenes, número de página, niveles de título, tablas, notas, sangría francesa de las referencias y páginas horizontales.
2. **Cumplimiento del docente:**
   - estructura del Taller 1;
   - etapas del modelo de investigación del Taller 4 en el Capítulo 2;
   - comunicación de resultados del Taller 5 en el Capítulo 3;
   - normas de citas del Taller 2 (sin segunda mano, jerarquía de fuentes).
3. **Coherencia global:**
   - OE1–OE5 ↔ resultados ↔ conclusiones ↔ resumen y abstract ↔ Anexo A;
   - las decisiones sobre HG, HE1 y HE2 son iguales en todas partes;
   - tabla de hechos clave (fechas, montos, áreas, 41 paños, 22 NC, 19,8 %, κ, PAO 3 firmada) buscada en todos los archivos.
4. **Integridad:**
   - lista de `\pendiente`;
   - ningún dato inventado (expertos, entrevistas, ensayos);
   - redacción neutral de los hallazgos de acero;
   - ningún nombre de persona;
   - nota de derechos de autor (ACI y Hernández-Sampieri solo en extractos).

### Etapa 3: correcciones

Corregir por grupo de archivos (un solo editor por archivo a la vez). Después compilar y revisar de nuevo lo cambiado.

### Etapa 4: cierre

1. Ejecutar el modelo (`python3 modelo_costos.py` y `python3 variantes.py`) y confirmar con `git diff` que no cambian las cifras.
2. Compilar la tesis y copiar `build/tesis.pdf` a `Tesis_SGC_Borrador.pdf`.
3. Regenerar el Word (`python3 07_Entregables/scripts/tesis_a_docx.py`) y las citas resaltadas (`python3 04_Bibliografia/08_Citas_Resaltadas/scripts/resaltar_citas.py`).
4. Actualizar la explicación sencilla, las preguntas del tribunal y la presentación con las cifras y conclusiones finales.
5. Escribir `07_Entregables/Informe_de_Auditoria.md`: hallazgos, decisiones y correcciones.
6. Cambiar a `\borradorfalse` cuando no queden pendientes.

## 3. Encargos listos para usar en Claude Code

**Etapa 1, ejemplo para un grupo:**

> Lee `08_Registro_de_Trabajo/Contexto_Maestro.md` y la sección 1 de `08_Registro_de_Trabajo/Plan_de_Auditoria_Pendiente.md`. Audita `05_Tesis_LaTeX/capitulos/40_capitulo3_resultados.tex` y `50_conclusiones.tex` con las lentes A (cifras), B (citas y APA) y C (redacción) del plan. Para cada hallazgo da archivo, ubicación, problema, evidencia (fuente y página o valor), corrección y gravedad. No edites todavía: primero muéstrame la lista.

**Etapa 3:**

> Aplica las correcciones confirmadas de la lista anterior. Verifica antes cada evidencia en la fuente, compila con `latexmk -f` y dime qué aplicaste y qué descartaste, y por qué.

**Etapa 2, coherencia:**

> Construye una tabla con los hechos clave de la tesis (fechas, montos, áreas, cantidades, porcentajes del diagnóstico y del modelo, decisiones de hipótesis) y busca cada uno en todos los archivos de `05_Tesis_LaTeX/capitulos/`. Informa toda contradicción con su ubicación.

Los scripts de los workflows que se usaron en la nube, con todos los encargos detallados, están en `Encargos_a_los_Agentes/`.
