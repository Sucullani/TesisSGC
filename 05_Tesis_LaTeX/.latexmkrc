# Configuración de latexmk para la tesis
$pdf_mode = 1;              # compilar con pdflatex
$out_dir = 'build';         # archivos auxiliares y PDF en build/
$bibtex_use = 2;            # ejecutar biber cuando cambie la bibliografía
@default_files = ('tesis.tex');
