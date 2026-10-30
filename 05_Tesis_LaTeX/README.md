# Documento de la tesis (LaTeX)

**Tesis para presentar (versión sencilla, sin notas):** en preparación. Fuente: `tesis_sencilla.tex` y `capitulos_sencilla/`. Faltan la introducción y los capítulos 1 a 3 simplificados.

**Versión académica completa:** [`Tesis_SGC_Borrador.pdf`](Tesis_SGC_Borrador.pdf) · [Word](../07_Entregables/Tesis_SGC_Borrador_Final.docx). Fuente: `tesis.tex` y `capitulos/`.

## Formato

Sigue la **Guía de Normas APA 7.ª edición** del repositorio (`04_Bibliografia/02_Metodologia_y_Redaccion/Guia_Normas_APA_7ma_Edicion.pdf`):

- Papel carta y márgenes de 2,54 cm.
- Times New Roman de 12 pt e interlineado doble.
- Texto alineado a la izquierda, sin división de palabras, y sangría de 1,27 cm.
- Número de página arriba a la derecha.
- Títulos en negrita según los niveles APA.
- Tablas y figuras con «Tabla N» o «Figura N» en negrita y el título en cursiva encima; debajo, una nota.
- Referencias con sangría francesa.

Los capítulos y secciones van numerados porque así lo pide la estructura del documento de graduación (Taller 1).

## Estructura

| Archivo | Contenido |
|---|---|
| `tesis.tex` | Archivo principal: datos de la carátula, orden de los capítulos y modo borrador. |
| `preambulo.tex` | Formato APA, paquetes, macros (`\mdos`, `\mtres`, `\nota{}`, `\pendiente{}`) y bibliografía. |
| `capitulos/00`–`02` | Carátula, preliminares (resumen y abstract) y lista de abreviaturas. |
| `capitulos/10_introduccion.tex` | Introducción: antecedentes, problema, objetivos, hipótesis, variables, justificación y metodología. |
| `capitulos/20_capitulo1_marco_teorico.tex` | Capítulo 1: marco teórico. |
| `capitulos/30_capitulo2_diseno_sgc.tex` | Capítulo 2 (2.1–2.5): modelo de investigación, caso de estudio, variables, población y diagnóstico (línea base). |
| `capitulos/31_capitulo2_propuesta_sgc.tex` | Capítulo 2 (2.6): diseño del Sistema de Gestión de la Calidad (la propuesta). |
| `capitulos/32_capitulo2_implementacion.tex` | Capítulo 2 (2.7–2.9): implementación, evaluación *ex ante*, validación y contraste. |
| `capitulos/40_capitulo3_resultados.tex` | Capítulo 3: resultados y discusión. |
| `capitulos/50_conclusiones.tex` | Conclusiones y recomendaciones. |
| `capitulos/90_anexos.tex` y `91*`, `92*` | Anexos A a L. Los planos y certificados se insertan desde `../03_Datos_Obra_Edificio_Posgrado/`. |
| `bib/*.bib` | Bibliografía, un archivo por grupo de fuentes. Cada entrada fue verificada en su PDF. Ver `../04_Bibliografia/07_Fichas_de_Citas/`. |
| `figuras/` | Imágenes de la tesis. Las figuras del modelo están en `../06_Modelo_de_Costos_y_Simulacion/figuras/`. |
| `scripts/depurar_bib.py` | Quita de `bib/00_base.bib` las claves que ya están en los archivos verificados. |

## Cifras del modelo

Las cifras de la simulación (por ejemplo, `\rMedia` o `\PHG`) y las tablas del modelo (`\tablamodelo{...}`) se leen de `../06_Modelo_de_Costos_y_Simulacion/tablas_latex/`. Si cambias `parametros.json`, sigue estos pasos:

1. Ejecuta `python3 modelo_costos.py` y `python3 variantes.py` en esa carpeta.
2. Vuelve a compilar la tesis.

Así el texto se actualiza solo.

## Marcas de borrador

- `\pendiente{...}`: dato que solo puede aportar el postulante (en **rojo**).
- `\guia{...}`: instrucciones de redacción (recuadro gris).
- Para la versión final, cambia `\borradortrue` por `\borradorfalse` en `tesis.tex`. Así desaparecen todas las marcas.

## Cómo compilar

```bash
latexmk                     # versión académica: build/tesis.pdf (pdflatex + biber)
latexmk tesis_sencilla.tex  # versión sencilla: build/tesis_sencilla.pdf
latexmk -c       # limpia archivos auxiliares
```

En VS Code puedes usar la extensión **LaTeX Workshop**.

Si tu MiKTeX no encuentra las fuentes `newtx` o `qtm`, actualiza los paquetes desde la consola de MiKTeX. El preámbulo ya carga los mapas de fuentes necesarios.

## Cómo citar

| Comando | Resultado |
|---|---|
| `\textcite{clave}` | Galarza Meza (2011) |
| `\parencite{clave}` | (Galarza Meza, 2011) |
| `\parencite[p.~75]{clave}` | (Galarza Meza, 2011, p. 75) |

Las claves están en `bib/*.bib`. Los pasajes citados están resaltados en `../04_Bibliografia/08_Citas_Resaltadas/`.
