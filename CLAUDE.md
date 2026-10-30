# Tesis SGC – Edificio de Posgrado UATF

Tesis de grado de Ingeniería Civil (UATF, Potosí, Bolivia): diseño de un Sistema de Gestión de la Calidad (ISO 9001:2026) centrado en el control de materiales de las losas alivianadas con viguetas pretensadas, con evaluación *ex ante* mediante un modelo de costos y una simulación de Monte Carlo.

## Antes de trabajar, lee

- `08_Registro_de_Trabajo/Bitacora_del_Trabajo.md`: qué se hizo, el estado de cada parte, las decisiones y los pendientes.
- `08_Registro_de_Trabajo/Contexto_Maestro.md`: datos verificados del caso. Úsalos tal cual.
- `08_Registro_de_Trabajo/Plan_de_Auditoria_Pendiente.md`: la verificación que falta y los problemas ya detectados.

## Reglas

- **No inventes datos.** Cada número sale de un documento del repositorio (con su página) o de un cálculo reproducible. No inventes resultados de expertos, entrevistas ni ensayos: van como `\pendiente{...}`.
- **Citas:** solo fuentes del repositorio que se hayan leído, sin citas de segunda mano (Taller 2). Verifícalas con las fichas de `04_Bibliografia/07_Fichas_de_Citas/*.json`. En Hernández-Sampieri (2018), la página impresa es la del PDF − 39; en el ACI 318-25, la del PDF − 1.
- **Formato:** APA 7 según `04_Bibliografia/02_Metodologia_y_Redaccion/Guia_Normas_APA_7ma_Edicion.pdf`. Números en formato boliviano (1.109,84). Español de Bolivia, registro impersonal.
- **Cifras del modelo:** usa siempre las macros de `06_Modelo_de_Costos_y_Simulacion/tablas_latex/valores_modelo.tex` (por ejemplo, `\rMedia`, `\PHG`), nunca números escritos a mano.
- **Hallazgos sensibles** (acero, dos versiones de la PAO 3): son «inconsistencias documentales que deben verificar la Supervisión y la Fiscalización». Nunca «sobrepago» ni nombres de personas.
- **PAO N.º 3 oficial:** la versión firmada (ítem 8: −1.862,81 kg; acumulado 50.561,84 kg).
- **Obras protegidas:** el ACI 318-25 y Hernández-Sampieri (2018) no se redistribuyen. El repositorio debe seguir privado.

## Comandos

```bash
cd 05_Tesis_LaTeX && latexmk                        # versión académica: build/tesis.pdf
cd 05_Tesis_LaTeX && latexmk tesis_sencilla.tex     # versión sencilla para presentar: build/tesis_sencilla.pdf
cd 06_Modelo_de_Costos_y_Simulacion && python3 modelo_costos.py && python3 variantes.py
python3 07_Entregables/scripts/tesis_a_docx.py      # Word de la tesis (desde la raíz)
python3 04_Bibliografia/08_Citas_Resaltadas/scripts/resaltar_citas.py
```

Después de compilar, copia `build/tesis.pdf` a `05_Tesis_LaTeX/Tesis_SGC_Borrador.pdf` y `build/tesis_sencilla.pdf` a `05_Tesis_LaTeX/Tesis_SGC_Version_Sencilla.pdf`.

La **versión sencilla** (`tesis_sencilla.tex`, `capitulos_sencilla/`) es la que se presenta: mismo formato, contenido simplificado y modo final, sin `\pendiente` ni `\guia`.

Su Word se genera con:

```bash
python3 07_Entregables/scripts/tesis_a_docx.py --principal tesis_sencilla.tex --aux 05_Tesis_LaTeX/build/tesis_sencilla.aux --salida 07_Entregables/Tesis_SGC_Version_Sencilla.docx --trabajo 07_Entregables/scripts/_trabajo_sencilla
```

Los commits van directo a `main`.
