# Encargos para terminar la Fase 3 en la sesión local

Cópialos tal cual en Claude Code, abierto en la raíz del repositorio. Cada encargo es independiente: se pueden lanzar en paralelo.

**Fuentes comunes para todos los encargos:**

- `08_Registro_de_Trabajo/Contexto_Maestro.md` y `08_Registro_de_Trabajo/Notas_para_la_Defensa.md`.
- La tesis: `05_Tesis_LaTeX/capitulos/*.tex`. Ya está completa, incluidos el Capítulo 3 y las conclusiones.
- Las cifras del modelo, solo de `06_Modelo_de_Costos_y_Simulacion/tablas_latex/valores_modelo.tex`, `resultados/resumen_resultados.json` y `resultados/variantes.json`.
- Las figuras: `06_Modelo_de_Costos_y_Simulacion/figuras/*.png` y `05_Tesis_LaTeX/figuras/*.png`.

**Reglas comunes:**

- Números con formato boliviano (1.109,84).
- Los hallazgos de acero y cantidades son «inconsistencias documentales que deben verificar la Supervisión y la Fiscalización»: nunca «sobrepago» ni nombres de personas.
- Los nombres del postulante y del tutor van como «[…]».

## 1. Presentación de defensa (HTML y PowerPoint)

> Lee el Taller 6 (`00_Material_Docente/Taller_6_Defensa_del_Trabajo_de_Graduacion.pdf`) y cumple su duración (40–45 min), su estructura y sus tamaños de letra (títulos ≥ 28 pt; texto ≥ 24 pt). Define el contenido una sola vez en `07_Entregables/scripts/generar_presentacion.py` (lista de diapositivas con título, viñetas, imagen y notas del orador) y genera desde ahí:
> - `07_Entregables/Presentacion_Defensa/Defensa_Tesis_SGC.pptx` (python-pptx, 16:9, con notas del orador en cada diapositiva);
> - `Defensa_Tesis_SGC.html`: un solo archivo autocontenido, sin CDN, con navegación por teclado, barra de progreso, tecla N para las notas e impresión de una diapositiva por página;
> - `Guion_de_Defensa.md`, con tiempos por diapositiva.
>
> Contenido, en 26–30 diapositivas más 4–5 de respaldo: carátula; problema con datos del caso; objeto; objetivos; hipótesis; metodología (no experimental, línea base documental, Monte Carlo *ex ante* de 20.000 iteraciones, regla P ≥ 0,95); marco teórico esencial; caso de estudio; diagnóstico (19,8 % de cumplimiento, 22 NC, Pareto; línea base: EPS +5,01 %, acero +16,75 %, 0 probetas de losa); diseño del SGC; modelo; resultados (histograma, curva acumulada, tornado, CNC por componente; tabla del contraste: HG no se acepta, HE1 y HE2 sí); robustez y punto de equilibrio; discusión; conclusiones por objetivo; recomendaciones; limitaciones; cierre.
>
> Diseño sobrio: fondo claro, acento azul oscuro, máximo 6 viñetas. Revisa una vez la conversión del PPTX a PDF con LibreOffice y una hoja de miniaturas.

## 2. Citas resaltadas en los PDF de la bibliografía

> Ejecuta y completa `04_Bibliografia/08_Citas_Resaltadas/scripts/resaltar_citas.py` con las 725 fichas de `04_Bibliografia/07_Fichas_de_Citas/*.json`:
> - resalta en amarillo el `texto_exacto` de las fichas citadas en la tesis, con un comentario que indique el ID de la ficha, la página citable, el lugar de la tesis donde se cita, el tipo y la paráfrasis;
> - resalta en azul claro las fichas no citadas;
> - si no hay capa de texto, usa la copia de `_ocr/` o pon una nota de página;
> - guarda `<subcarpeta>/<nombre>_RESALTADO.pdf`, y solo extractos (portada y páginas citadas) para los PDF de más de 60 páginas y siempre para el ACI 318-25 y Hernández-Sampieri;
> - genera `Indice_de_Citas.md`, `.csv` y `.xlsx`, marcando como «cita sin ficha verificada» las páginas citadas que no coinciden con ninguna ficha;
> - escribe un README con la nota de derechos de autor.
>
> El script debe poder ejecutarse de nuevo sin duplicar anotaciones. La carpeta debe pesar menos de 60 MB.

## 3. Preguntas del tribunal

> Escribe `07_Entregables/Preguntas_del_Tribunal_y_Respuestas.md` (y su `.docx` con pandoc):
> - 70–90 preguntas agrupadas por tema: título, problema, objetivos, hipótesis y umbral del 5 %, diseño *ex ante*, Monte Carlo y supuestos, línea base, SGC e ISO 9001:2026, normas técnicas (ACI 318-25 26.12.7, NB 997, NB 1225001/NBDS, CBH-87), costos (PAF, APU y κ), hallazgos de acero, resultados, validación pendiente, ética, normativa boliviana de contratación, clima de Potosí y preguntas trampa;
> - para cada una: respuesta sugerida con su respaldo en la tesis, qué decir y qué NO decir;
> - además: debilidades y cómo defenderlas (ver `Notas_para_la_Defensa.md` y la sección 1 del plan de auditoría), cifras que hay que saber de memoria, una lista de verificación antes de la defensa y la conducta según el Taller 6.

## 4. Explicación en lenguaje sencillo

> Revisa `07_Entregables/Tesis_Explicada_en_Lenguaje_Sencillo.md` contra la versión final de la tesis (cifras y conclusiones). Genera el `.docx` (pandoc, con imágenes) y un `.html` autocontenido con CSS en línea, imágenes en base64 y modo oscuro.

## 5. Word de la tesis

```bash
python3 07_Entregables/scripts/tesis_a_docx.py
```

Ver `07_Entregables/scripts/README_docx.md`. Requiere pandoc, LibreOffice y una distribución LaTeX.
