# Documento de la tesis (LaTeX)

**PDF más reciente:** [`Tesis_SGC_Borrador.pdf`](Tesis_SGC_Borrador.pdf)

## Estructura

| Archivo | Contenido |
|---|---|
| `tesis.tex` | Archivo principal: título, postulante, tutor y orden de los capítulos. |
| `preambulo.tex` | Formato: carta, márgenes de 3 / 2,5 cm, letra tipo Times de 12 pt, interlineado 1,5, leyendas APA y estilo de bibliografía. |
| `capitulos/00_caratula.tex` | Carátula |
| `capitulos/01_preliminares.tex` | Dedicatoria, agradecimientos, resumen y abstract |
| `capitulos/02_abreviaturas.tex` | Lista de abreviaturas y siglas |
| `capitulos/10_introduccion.tex` | Introducción: antecedentes, problema, objetivos, hipótesis, variables, justificación y metodología |
| `capitulos/20_capitulo1_marco_teorico.tex` | Capítulo 1 – Marco teórico |
| `capitulos/30_capitulo2_diseno_sgc.tex` | Capítulo 2 – Diseño e implementación del SGC (modelo de investigación) |
| `capitulos/40_capitulo3_resultados.tex` | Capítulo 3 – Resultados y análisis |
| `capitulos/50_conclusiones.tex` | Conclusiones y recomendaciones |
| `capitulos/90_anexos.tex` | Anexos A a K. Los planos y certificados se insertan desde `../03_Datos_Obra_Edificio_Posgrado/`. |
| `bibliografia.bib` | Referencias en formato BibTeX (estilo APA 7 con biblatex) |
| `figuras/` | Imágenes de la tesis |

## Marcas de borrador

- `\pendiente{...}`: dato o texto que falta (aparece en **rojo** en el PDF).
- `\guia{...}`: instrucciones para redactar la sección (aparece en un **recuadro gris**).
- Para la versión final, cambia `\borradortrue` por `\borradorfalse` en `tesis.tex`. Así desaparecen todas las marcas.

## Cómo compilar

En esta carpeta:
```bash
latexmk          # genera build/tesis.pdf (pdflatex + biber)
latexmk -c       # limpia archivos auxiliares
```
En VS Code puedes instalar la extensión **LaTeX Workshop** (James Yu). Compila al guardar y muestra el PDF al lado del texto.

## Cómo pedir cambios al agente

Indica el archivo o la sección, por ejemplo:
- «Redacta la sección 1.4 (costos de la calidad) siguiendo su guía».
- «Agrega a la bibliografía y al estado del arte la tesis de X».
- «Actualiza la Tabla 2 con los datos de la planilla N.º 4».

## Cómo citar
- `\textcite{clave}` → Álvarez Quintero (2014)
- `\parencite{clave}` → (Álvarez Quintero, 2014)
- Las claves están en `bibliografia.bib`.
