# Conversión de la tesis LaTeX a Word (.docx) con formato APA 7

`tesis_a_docx.py` genera **`07_Entregables/Tesis_SGC_Borrador_Final.docx`** a partir de la fuente LaTeX
(`05_Tesis_LaTeX/tesis.tex`, sus capítulos, `bib/*.bib` y las cifras y tablas de
`06_Modelo_de_Costos_y_Simulacion/tablas_latex/`). Solo **lee** esas carpetas: no escribe nada en
`05_Tesis_LaTeX/` ni en `06_.../` (la compilación de LaTeX se hace en una carpeta temporal).

## Cómo regenerar el Word (un solo comando)

Desde la raíz del repositorio:

```bash
python3 07_Entregables/scripts/tesis_a_docx.py
```

Tarda unos 2 a 3 minutos (la compilación con latexmk es lo más lento; las figuras TikZ y las páginas de
PDF se guardan en caché y solo se rehacen si cambian). Al final imprime un informe que también queda en
`07_Entregables/scripts/_trabajo/informe_conversion.txt`.

Opciones útiles:

| Opción | Para qué |
|---|---|
| `--pdf` | Exporta además un PDF de verificación con LibreOffice (`_trabajo/Tesis_SGC_Borrador_Final.pdf`). |
| `--sin-compilar` | No compila LaTeX; usa el último `.aux` válido de la caché (más rápido). |
| `--latex-rapido` | Una sola pasada de `pdflatex -draftmode` en lugar de latexmk (basta para el `.aux`). |
| `--aux RUTA` | Usa ese `.aux` (por ejemplo `05_Tesis_LaTeX/build/tesis.aux`). |
| `--salida RUTA` | Otro nombre o carpeta para el `.docx`. |
| `--regenerar-plantilla` | Vuelve a crear `plantilla_apa.docx` (si no, se usa la existente, que puede editarse a mano). |
| `--tabla-pt 11` | Tamaño de letra de las tablas (APA: 12, valor por defecto). Los formularios con cuadrícula usan `--formulario-pt` (10). |
| `--dpi-pdf 100`, `--dpi-tikz 250` | Bajan la resolución de las páginas insertadas desde PDF (150 por defecto) o de las figuras TikZ (300) para un archivo más liviano. |
| `--sin-paginas` | No abre LibreOffice para escribir los números de página del índice. |

Requisitos (ya instalados en este entorno): Python 3 con `python-docx`, `pymupdf` y `Pillow`; pandoc ≥ 3.1;
TeX Live (pdflatex, latexmk, biber, paquetes `preview` y TikZ); LibreOffice (opcional, para los números de
página del índice y el PDF de verificación; para ver las fórmulas en ese PDF hace falta `libreoffice-math`).

## Qué hace, paso a paso

1. **`.aux` de LaTeX.** Compila la tesis con `latexmk -f` en `_trabajo/latex/` (sin generar fuentes, para no
   dejar `missfont.log`). Si la compilación no termina porque alguien está editando un archivo, usa el último
   `.aux` válido de la caché (`_trabajo/aux_valido/`) o, en último caso, `05_Tesis_LaTeX/build/tesis.aux`.
2. **Numeración y referencias.** El programa numera capítulos, secciones, tablas, figuras, ecuaciones y anexos
   igual que LaTeX (incluidas las rarezas: `\setcounter`, `\appendix` con letras, la introducción con secciones
   1, 2, 3..., `longtable` que avanza el contador aunque no tenga `\caption`) y compara el resultado con el `.aux`;
   las diferencias se listan en el informe. `\ref`, `\eqref`, `\autoref`, `\nameref` se sustituyen por los números.
3. **Aplanado.** Resuelve `\input`, `\include`, `\IfFileExists`, `\tablamodelo{x}` y `\VerbatimInput`; expande
   todas las `\newcommand` (las de `tesis.tex`, `preambulo.tex`, `valores_modelo.tex` y las definidas dentro de
   los capítulos: `\titulotesis`, `\mdos`→m², `\MCiter`, `\casilla`...). `\guia{}` se elimina; `\pendiente{x}`
   → «**[Pendiente:** x**]**» en rojo (desaparece si `tesis.tex` tiene `\borradorfalse`); `\nota{x}` → «*Nota.* x».
4. **Tablas.** Tipos de columna propios (`L`, `C`, `R`, `P{}`, `Q{}` y cualquier `\newcolumntype`), `tabularx`,
   `longtable` (`\endfirsthead`/`\endhead` sin duplicar encabezados; `\endfoot` se omite), `\multicolumn`,
   `\multirow`, `\makecell`, `\addlinespace`, `\cmidrule`. Los anchos de columna se calculan desde la fuente
   (p{...}, X, contenido) y ninguna columna queda más estrecha que su palabra más larga.
   Bordes: tablas con `booktabs`/`\hline` → **APA** (arriba, bajo el encabezado, abajo y sobre los totales);
   tablas con líneas verticales `|` (formularios para imprimir del Anexo C) → **cuadrícula**; tablas sin
   líneas (lista de abreviaturas) → sin bordes. El encabezado se repite en cada página.
5. **Figuras.** Cada `tikzpicture` se compila con el mismo preámbulo de la tesis (paquete `preview`) y se
   convierte a PNG de 300 ppp; los `\ref` dentro del dibujo se resuelven antes. Los PDF de `\includegraphics`
   se convierten a PNG (300 ppp). Las páginas de `\includepdf` (planos, cómputos, certificados, fotos) se
   convierten a PNG de 150 ppp, cada una en su página; las horizontales (planos) van en **secciones apaisadas**
   y se les recortan los márgenes blancos.
6. **pandoc** con `--citeproc`, el estilo APA 7 (`tesis_docx/csl/apa.csl`, ajustado al español: «y» en lugar
   de «&», sin coma antes de «y», guion «–» en rangos de páginas) y todos los `.bib` de `05_Tesis_LaTeX/bib/`
   (en el orden de `\addbibresource`; si una clave se repite, vale la primera, como en biber; `titleaddon`
   → «[Certificado]»). Las citas salen en español («y», «p.», «s. f.») y los autores corporativos con
   `shortauthor` siguen la regla APA: «(Organización Internacional de Normalización [ISO], 2026)» la primera
   vez y «(ISO, 2026)» después, como en el PDF de biblatex-apa.
7. **Posproceso (python-docx).** «**Tabla N**» / «**Figura N**» en negrita y título en *cursiva* en la línea
   siguiente; «*Nota.*»; ecuaciones numeradas «(N)» a la derecha; índice general, de tablas y de figuras con
   hipervínculos y números de página (campos `PAGEREF`); carátula centrada sin número; páginas preliminares
   en romanos y cuerpo en arábigos desde la Introducción; salto de página antes de cada capítulo y anexo.
8. **LibreOffice (opcional).** Abre el `.docx`, calcula la página de cada entrada del índice y la escribe
   como valor de los campos (para que se vean aunque Word no actualice); con `--pdf` exporta un PDF.

## Formato aplicado (Guía de Normas APA 7.ª ed. del repositorio)

Papel carta; márgenes de 2,54 cm; Times New Roman 12; interlineado doble sin espacio extra; alineado a la
izquierda (sin justificar); sangría de 1,27 cm en la primera línea; número de página arriba a la derecha;
nivel 1 centrado y negrita, nivel 2 a la izquierda y negrita, nivel 3 negrita y cursiva, nivel 4 con sangría;
cuerpo de tablas a espacio sencillo (número, título y nota a doble espacio); referencias con sangría
francesa de 1,27 cm; código fuente en Courier New 9. Se conservan la numeración de capítulos y secciones y
los títulos de nivel 1 en MAYÚSCULAS porque así está la tesis en LaTeX (estructura del docente).
Los estilos están en `plantilla_apa.docx`: se pueden retocar en Word (Inicio → Estilos) y la siguiente
conversión los respeta (no usar `--regenerar-plantilla`, que la sobrescribe).

## Archivos

| Archivo | Contenido |
|---|---|
| `tesis_a_docx.py` | Programa principal (este proceso). |
| `tesis_docx/latex.py` | Lectura, aplanado, numeración y transformación del LaTeX. |
| `tesis_docx/graficos.py` | TikZ, `\includegraphics` e `\includepdf` → PNG (con caché). |
| `tesis_docx/bibliografia.py` | Unión de los `.bib` y ajuste del estilo CSL. |
| `tesis_docx/word.py` | Plantilla APA y posproceso del `.docx`. |
| `tesis_docx/libreoffice.py` | Números de página del índice y PDF de verificación. |
| `tesis_docx/filtro_apa.lua`, `filtro_citas.lua` | Filtros de pandoc (estilos y abreviaturas de autores). |
| `tesis_docx/csl/` | `apa.csl` y `locales-es-ES.xml` originales. |
| `plantilla_apa.docx` | Plantilla de estilos de Word (se crea si no existe). |
| `_trabajo/` | Intermedios y caché (ignorado por git): `tesis_pandoc.tex`, imágenes, `.aux`, informe. |

## Limitaciones conocidas

- **Índices:** son entradas fijas con hipervínculo y número de página (`PAGEREF`), generadas desde la fuente
  LaTeX (mismo contenido que el índice del PDF). Word pregunta al abrir si desea actualizar los campos: responder
  **Sí** recalcula las páginas. Si se agregan títulos en Word, el índice no los incluye (habría que regenerar el
  .docx o insertar un índice automático de Word, ya que los títulos usan los estilos Título 1 a 3).
- **Números de página del índice en LibreOffice:** LibreOffice muestra las páginas preliminares en arábigos
  (3 en lugar de iii); Word las muestra en romanos.
- **Ecuaciones:** se convierten a ecuaciones nativas de Word (OMML) con pandoc. Los entornos `align` se separan
  en una ecuación por línea (se pierde la alineación en «=»; se conserva el número de cada línea). Algunos
  comandos poco comunes de LaTeX matemático podrían no tener equivalente.
- **Título de nivel 4** (`\subsubsection`): APA lo pone en la misma línea del párrafo; en Word queda como
  párrafo propio con sangría y punto final.
- **Figuras TikZ y diagramas:** son imágenes (no editables en Word). Para cambiarlas, edite el LaTeX y regenere.
- **Formularios del Anexo C** (cuadrícula, casillas ☐, líneas para llenar «____»): se convierten de forma
  aproximada; el color de fondo de las celdas (`\cellcolor`) no se conserva.
- **Etiquetas duplicadas** (`\label` repetido) y `\ref` a etiquetas inexistentes: se resuelven como LaTeX
  (vale la última; las inexistentes salen como «??» en rojo) y se listan en el informe para corregir la fuente.
- **Citas:** si una clave no está en ningún `.bib`, pandoc la escribe como «(clave?)» en negrita y el informe
  la lista. Los títulos de la bibliografía se copian tal como están en los `.bib`.
- **Tamaño del archivo:** las páginas escaneadas y fotos de los anexos se insertan como PNG de 150 ppp (unos
  15–20 MB en total). Con `--dpi-pdf 100` el archivo se reduce.
- Si la compilación LaTeX falla, la conversión continúa con la numeración calculada desde la fuente (el informe
  lo advierte); un entorno o comando que no se pueda convertir se deja como está y se informa.

## Qué conviene revisar a mano en Word

1. Aceptar **«Actualizar campos»** al abrir (o Ctrl+A y F9) para que los números de página del índice coincidan
   con la paginación de Word.
2. Carátula: que quepa en una página y el lugar del escudo (`[Pendiente: insertar el escudo...]`).
3. Tablas anchas o largas (matriz de consistencia, operacionalización, APU, lista de verificación C.1):
   anchos de columna, cortes de página y que el encabezado se repita.
4. Ecuaciones: aspecto general y números a la derecha.
5. Figuras: tamaño y que la figura no quede separada de su título o de su nota al cambiar de página.
6. Anexos con planos (páginas apaisadas) y escaneos: legibilidad.
7. Marcas en rojo `[Pendiente: ...]` y `??` (referencias a secciones o tablas que aún no existen).
8. Bibliografía: entradas sin fecha («s. f.»), autores corporativos y que no falte ninguna cita.
