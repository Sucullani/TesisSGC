export const meta = {
  name: 'fase2b-anexos-normas-citas',
  description: 'Actualiza anexos A, B, D, F y H, integra las fichas de normas en los capitulos 1-2 y resalta las citas en los PDF de la bibliografia, con verificacion adversarial',
  phases: [
    { title: 'Trabajar', detail: 'anexos, normas en capitulos, resaltado de citas' },
    { title: 'Verificar', detail: 'revisor adversarial por encargo' },
    { title: 'Corregir', detail: 'aplicar hallazgos confirmados' },
  ],
}

const S = '/tmp/claude-0/-home-user-TesisSGC/c22f603c-c695-5c98-b48f-e99a1e2bf286/scratchpad'
const R = '/home/user/TesisSGC'

const FINDINGS = {
  type: 'object',
  properties: {
    hallazgos: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          archivo: { type: 'string' },
          ubicacion: { type: 'string' },
          problema: { type: 'string' },
          evidencia: { type: 'string' },
          correccion: { type: 'string' },
          gravedad: { type: 'string', enum: ['alta', 'media', 'baja'] },
        },
        required: ['archivo', 'problema', 'evidencia', 'correccion', 'gravedad'],
      },
    },
  },
  required: ['hallazgos'],
}

const BASE = `Contexto obligatorio: lee COMPLETO ${S}/CONTEXTO_MAESTRO.md antes de trabajar (no hagas git commit ni push; el coordinador lo hace). ` +
  `Herramientas: python3 (pymupdf, pypdf, openpyxl, pandas), pdftotext, pdftoppm, tesseract, latexmk/biber. Para mirar una página renderizada usa pdftoppm -r 60 -png y la herramienta Read sobre el PNG. `

const ENCARGOS = [
  {
    key: 'anexos',
    archivos: 'capitulos/90_anexos.tex, capitulos/91_anexo_instrumentos.tex, capitulos/91a_lista_verificacion_iso9001.tex',
    prompt: BASE +
`Eres responsable de los ANEXOS de la tesis en ${R}/05_Tesis_LaTeX/capitulos/. Edita SOLO 90_anexos.tex, 91_anexo_instrumentos.tex y 91a_lista_verificacion_iso9001.tex. Otros agentes editan ahora mismo los capítulos 10_, 20_, 30_, 31_, 32_, 40_ y 50_: NO los toques.
Tareas:
1. Anexo A «Matriz de consistencia» (label anx:matriz): hoy describe el diseño antiguo (cuasi-experimental O1–X–O2 con prueba t). Reescríbelo para que coincida EXACTAMENTE con la introducción final (capitulos/10_introduccion.tex: pregunta general y específicas, objetivo general y OE1–OE5, hipótesis HG, HE1, HE2 con sus umbrales, variables) y con el diseño final (capitulos/30_capitulo2_diseno_sgc.tex secciones 2.1–2.3 y capitulos/32_capitulo2_implementacion.tex: evaluación ex ante, Monte Carlo de 20.000 iteraciones, reglas de decisión de la tabla tab:reglas-decision, sensibilidad, validación por expertos con V de Aiken pendiente). Copia las formulaciones literales de la introducción; no las parafrasees.
2. Anexo B «Operacionalización de variables» (label anx:operacionalizacion): debe coincidir con la operacionalización del capítulo 2 (búscala en 30_capitulo2_diseno_sgc.tex). Mismas variables, dimensiones, indicadores, fórmulas (con \\ref a ecuaciones que EXISTAN: verifica cada label con grep en todos los .tex) e instrumentos del Anexo C (C.1–C.8). Puede ser la versión extendida, con escala de medición, fuente de datos y momento de medición (línea base documental / simulación ex ante / verificación futura en obra).
3. Anexo D «Validación de instrumentos por juicio de expertos»: hoy solo tiene un \\guia. Redáctalo: propósito; procedimiento (3–5 expertos, criterios de selección, ficha C.8 y su escala); cálculo de la V de Aiken con su fórmula; tabla vacía de resultados por ítem lista para llenar; y un \\pendiente{} con lo que debe aportar el postulante (fichas firmadas, currículos resumidos, cálculo). No inventes resultados. Cita solo fuentes con ficha verificada en ${R}/04_Bibliografia/07_Fichas_de_Citas/*.json (Hernández-Sampieri, p. 235, sirve para la validez de expertos; NO trata la V de Aiken: si no hay ficha de Aiken, presenta la fórmula sin atribuirla a una fuente que no la contiene, o búscala en otra ficha verificada).
4. Anexo F «Cómputos métricos y planillas de avance»: resuelve el \\pendiente. Localiza en ${R}/03_Datos_Obra_Edificio_Posgrado/ las páginas de la Planilla de Avance N.º 2 (PAO 2) y de la PAO N.º 3 FIRMADA (expediente del ítem 13, p. 2) que corresponden al ítem 13 y al ítem 8 (orientación: PAO 2 pp. 16, 19–20, 28–29 y 60; usa los .md de 03_Datos_Obra_Edificio_Posgrado/04_Extraccion_de_Datos/ para confirmarlas) e insértalas con \\includepdf igual que las existentes. Verifica CADA número de página renderizándola y mirándola. Una frase introductoria por documento.
5. Anexo H «Resultados de ensayos de laboratorio»: el \\pendiente actual («agregar los resultados de los ensayos de la losa obtenidos durante la aplicación del SGC») es obsoleto: la segunda losa no se ejecutó. Sustitúyelo por un texto que diga que de la primera losa no se ensayó ninguna probeta (dato del diagnóstico; el certificado 000293 solo trae columnas y vigas) y, si corresponde, deja un \\pendiente para los ensayos de la verificación futura con datos de obra (la sección de 32_capitulo2_implementacion.tex que describe esa verificación).
6. Tablas sin \\caption: 90_anexos.tex tiene 2 longtables sin caption y 91_anexo_instrumentos.tex 5. La guía APA del repositorio exige «Tabla N» en negrita y el título en cursiva encima. A las tablas de los anexos A y B ponles caption APA con label (dentro de la longtable, con \\endfirsthead y un \\endhead de continuación). Para los formularios del Anexo C decide con criterio (formato para llenar como Tabla con título), pero la numeración de tablas del documento debe quedar consecutiva y sin saltos. Mira cómo trata preambulo.tex las longtables y copia el estilo de las tablas que ya tienen caption.
7. Revisa en tus tres archivos las citas a normas y metodología contra ${R}/04_Bibliografia/07_Fichas_de_Citas/Fichas_Normas_Legislacion_Metodologia.json y .md: página correcta (Hernández-Sampieri: página impresa = PDF − 39; ACI 318-25: impresa = PDF − 1) y que lo atribuido esté en la fuente.
8. Compila: cd ${R}/05_Tesis_LaTeX && latexmk -f -interaction=nonstopmode -outdir=${S}/build_anexos tesis.tex . Corrige los errores que vengan de tus archivos y revisa visualmente las páginas de los anexos A, B, D y F (orientación correcta, nada desbordado).
Responde con un resumen: cambios por anexo, labels nuevos y pendientes que quedan.`,
    verificar:
`LENTE: anexos. Revisa con git diff (cd ${R} && git diff -- 05_Tesis_LaTeX/capitulos/90_anexos.tex 05_Tesis_LaTeX/capitulos/91_anexo_instrumentos.tex 05_Tesis_LaTeX/capitulos/91a_lista_verificacion_iso9001.tex) y leyendo los archivos completos. Comprueba: (1) cada pregunta, objetivo, hipótesis y variable del Anexo A es LITERALMENTE igual a la de capitulos/10_introduccion.tex; (2) el diseño descrito coincide con 30_ y 32_ (no quedan rastros de cuasi-experimento, prueba t como método principal, OE redactados a la antigua); (3) el Anexo B coincide con la operacionalización de 30_; (4) cada \\ref y \\label existe; (5) las páginas insertadas en el Anexo F son las correctas (renderízalas desde el PDF compilado en ${S}/build_anexos/tesis.pdf y míralas); (6) la numeración de tablas es consecutiva (revisa el .lot o el PDF); (7) no hay resultados inventados en el Anexo D; (8) cumplimiento de la guía APA del repositorio en tablas. Informa solo problemas reales, con evidencia.`,
  },
  {
    key: 'normas',
    archivos: 'capitulos/10_introduccion.tex, 20_capitulo1_marco_teorico.tex, 30_capitulo2_diseno_sgc.tex, 31_capitulo2_propuesta_sgc.tex, 32_capitulo2_implementacion.tex',
    prompt: BASE +
`Un agente fichó y verificó 298 citas de normas, legislación y metodología: ${R}/04_Bibliografia/07_Fichas_de_Citas/Fichas_Normas_Legislacion_Metodologia.json y .md (incluye una tabla regla → página). Tu tarea: integrar esos hallazgos en los capítulos ya redactados, con cambios quirúrgicos. Edita SOLO ${R}/05_Tesis_LaTeX/capitulos/10_introduccion.tex, 20_capitulo1_marco_teorico.tex, 30_capitulo2_diseno_sgc.tex, 31_capitulo2_propuesta_sgc.tex, 32_capitulo2_implementacion.tex y, si hace falta, bib/normas_legislacion_metodologia.bib. NO edites 40_, 50_, 90_, 91_, 91a_ ni 92_ (otros agentes trabajan en ellos ahora).
1. Recorre TODAS las citas (\\parencite, \\textcite, \\cite…) a claves de bib/normas_legislacion_metodologia.bib en esos 5 archivos (hernandez2018, ACI, NB, ISO, D.S., R.M., leyes, DBC, guía APA, etc.). Para cada una comprueba con las fichas, y si hace falta con el PDF (pdftotext -f N -l N -layout), que (a) lo afirmado está en la fuente y (b) la página es la correcta. Corrige la página o la redacción. Hallazgos ya conocidos que DEBES resolver:
 - Hernández-Sampieri (2018): página impresa = PDF − 39. Prueba t: p. 352; Wilcoxon solo aparece nombrado en la tabla de la p. 372; el libro NO trata Shapiro-Wilk, Monte Carlo ni la V de Aiken: no se le pueden atribuir (en 32_capitulo2_implementacion.tex, cerca de la línea 119, hay «… Shapiro-Wilk … \\parencite{hernandez2018}» sin página: corrígelo). Hipótesis: pp. 124–135 (verifica la p. 133 citada para la hipótesis nula). Validez de expertos: p. 235. Revisa también pp. 6, 108, 110, 113, 151, 154, 163, 175, 180, 196, 200, 342 y 372 citadas en 10_, 20_ y 30_.
 - ACI CODE-318-25 (impresa = PDF − 1): la investigación de resultados bajos de resistencia es 26.12.7 (núcleos: promedio ≥ 0,85 f′c y ninguno < 0,75 f′c), pp. 606–607; el 26.12.6 trata del hormigón liviano. Muestreo 26.12.2.1 (p. 603); aceptación 26.12.3.1 (p. 603); curado 26.5.3 (p. 581); tiempo frío 26.5.4 (pp. 583–584); inspección 26.13 (pp. 608–611). Revisa cada mención de cláusulas del ACI.
 - Marco normativo boliviano del hormigón: según las fichas, la R.M. 271/2023 del MOPSV declara obligatoria la NBDS, que remite a la NB 1225001 como norma de diseño (arts. 1 y 10) y no menciona la CBH-87. Revisa cómo la tesis presenta la CBH-87: afirmar que es «obligatoria por el D.S. 22976/1991» solo si hay ficha o fuente verificada en el repositorio; si no, redacta con prudencia («norma citada por la especificación técnica del ítem») y presenta la NB 1225001/NBDS como el marco vigente según las fichas.
 - DBC: el modelo de DBC 2022 fue sustituido por la R.M. 048/2024; las funciones del Supervisor y del Fiscal y el Libro de Órdenes están en el DBC (cláusulas 25–27 y 38), no en la NB-SABS. Corrige atribuciones.
 - NB-SABS (D.S. 0181), art. 89: contrato modificatorio ≤ 10 %, orden de cambio ≤ 5 %, conjunto ≤ 15 % (páginas según la ficha). Fuerza mayor y caso fortuito: art. 5 c) y p). D.S. 5597, disposición adicional quinta: úsalo donde se explique la resolución del contrato, si encaja.
 - Plano 02 y NBDS: la NBDS exige 250 mm de altura mínima para que una losa de viguetas funcione como diafragma rígido (toma la página de la ficha). El Plano 02 acota 0,15 m de complemento + 0,05 m de carpeta (0,20 m), mientras la ET, el ítem 13 («h = 25 cm») y el certificado PRETENSA indican 20 + 5 = 25 cm. Donde el capítulo 2 describe esa discrepancia del Plano 02 (busca «0,15»), agrega UNA frase: la sección del plano tampoco alcanzaría la altura mínima de la NBDS, lo que refuerza que se trata de un error del plano que la Supervisión debe aclarar. No afirmes que la losa construida sea deficiente.
2. No cambies cifras del modelo ni la estructura de secciones. No toques citas de tesis o artículos salvo un error evidente (anótalo en tu respuesta).
3. Compila: cd ${R}/05_Tesis_LaTeX && latexmk -f -interaction=nonstopmode -outdir=${S}/build_normas tesis.tex ; sin errores nuevos; revisa el .blg de biber.
Responde con una tabla: archivo:línea → cita antes → cita después (motivo), y la lista de afirmaciones que no pudiste verificar.`,
    verificar:
`LENTE: citas normativas. Revisa el diff (cd ${R} && git diff -- 05_Tesis_LaTeX/capitulos/10_introduccion.tex 05_Tesis_LaTeX/capitulos/20_capitulo1_marco_teorico.tex 05_Tesis_LaTeX/capitulos/30_capitulo2_diseno_sgc.tex 05_Tesis_LaTeX/capitulos/31_capitulo2_propuesta_sgc.tex 05_Tesis_LaTeX/capitulos/32_capitulo2_implementacion.tex 05_Tesis_LaTeX/bib/normas_legislacion_metodologia.bib). Para CADA cita modificada o añadida, abre el PDF en la página indicada (pdftotext -f N -l N con N = página PDF) y confirma que dice lo que la tesis afirma. Busca además citas a hernandez2018 y a ACI que sigan atribuyendo contenidos que la fuente no tiene (Shapiro-Wilk, Monte Carlo, V de Aiken, 26.12.6 como resultados bajos), afirmaciones sobre la CBH-87 sin fuente verificada y frases nuevas que contradigan el CONTEXTO_MAESTRO. Informa solo problemas reales, con evidencia.`,
  },
  {
    key: 'resaltado',
    archivos: '04_Bibliografia/08_Citas_Resaltadas/',
    prompt: BASE +
`Tarea: «remarcar las citas en las bibliografías y archivarlas, con comentario y páginas». Hay un script escrito pero nunca ejecutado: ${R}/04_Bibliografia/08_Citas_Resaltadas/scripts/resaltar_citas.py. Hay 725 fichas en ${R}/04_Bibliografia/07_Fichas_de_Citas/*.json (4 grupos; revisa los campos de cada grupo —clave_bib, archivo_pdf, pagina_pdf, pagina_citable, texto_exacto, capa_de_texto, tipo, uso_sugerido, parafrasis— y normaliza nombres distintos). No edites la tesis ni las fichas.
Requisitos:
1. Para cada ficha cuya clave se cita en la tesis (05_Tesis_LaTeX/capitulos/*.tex), resalta en amarillo el texto exacto en su página del PDF y agrega una anotación (comentario emergente) con: ID de ficha; página citable APA; dónde se cita en la tesis (capítulo > sección, archivo:línea y la página que indica la cita); tipo; paráfrasis. Si la tesis cita la clave con una página que no coincide con ninguna ficha, márcalo en el índice como «cita sin ficha verificada» (lo revisará la auditoría).
2. Fichas no citadas en la tesis: resáltalas en otro color (azul claro) con la nota «Ficha verificada, no citada en la versión actual».
3. PDF sin capa de texto (capa_de_texto=false): usa la copia OCR si existe (04_Bibliografia/08_Citas_Resaltadas/_ocr/ o ${S}/normas/ocr/); si no, haz OCR con tesseract (spa+eng) para ubicar el pasaje; si aun así no se encuentra, pon una nota de página (icono de comentario) en la página indicada.
4. Salida: 04_Bibliografia/08_Citas_Resaltadas/<misma subcarpeta que el original>/<nombre>_RESALTADO.pdf. Para PDF de más de 60 páginas, y SIEMPRE para las obras protegidas (ACI CODE-318-25 y Hernández-Sampieri 2018, sin importar su tamaño), guarda SOLO un extracto: portada + páginas citadas, con el número de página original anotado en el margen (p. ej. «Página original: PDF 603 / impresa 602»).
5. Índice: 08_Citas_Resaltadas/Indice_de_Citas.md, .csv y .xlsx (openpyxl, con filtros, encabezado fijo y anchos legibles). Columnas: clave, referencia APA corta, archivo resaltado, página PDF, página citable, texto citado, dónde se cita en la tesis, estado (resaltado / nota de página / no encontrado / sin ficha). Al inicio del .md, un resumen por fuente (n.º de citas, páginas).
6. README.md de 08_Citas_Resaltadas: contenido, comando para regenerar, significado de los colores y nota de derechos de autor (extractos para revisión académica privada; no redistribuir; el repositorio debe seguir privado).
7. El script debe ser idempotente y re-ejecutable (se volverá a correr cuando la tesis esté cerrada). Ejecútalo; comprueba el tamaño total de la carpeta (objetivo < 60 MB; si excede, usa extractos también para PDF > 30 páginas y guarda con garbage=4, deflate=True) y revisa visualmente 4 páginas resaltadas de fuentes distintas (pdftoppm -r 60 + Read) para confirmar que el resaltado cae sobre el texto correcto.
Responde con un resumen: fichas por estado, fuentes, tamaño y problemas.`,
    verificar:
`LENTE: resaltado de citas. Revisa ${R}/04_Bibliografia/08_Citas_Resaltadas/ (script, PDF, índice y README). Comprueba: (1) toma 12 filas al azar del índice con estado «resaltado» de al menos 8 fuentes distintas; para cada una abre el PDF resaltado, ubica la anotación (pymupdf: page.annots()) y confirma que el rectángulo resaltado contiene el texto_exacto de la ficha (page.get_textbox(rect)) y que el comentario indica la página citable y el lugar de la tesis; renderiza 3 de ellas y míralas; (2) ACI 318-25 y Hernández-Sampieri solo aparecen como extractos; (3) ningún PDF de más de 60 páginas se copió completo; (4) el índice cubre todas las claves citadas en 05_Tesis_LaTeX/capitulos/*.tex; (5) el script se ejecuta de nuevo sin errores y sin duplicar anotaciones (ejecútalo dos veces y compara el número de anotaciones); (6) tamaño total de la carpeta. Informa solo problemas reales, con evidencia.`,
  },
]

const resultados = await pipeline(
  ENCARGOS,
  e => agent(e.prompt, { label: `trabajar:${e.key}`, phase: 'Trabajar' }),
  (informe, e) => agent(
    `Eres un revisor adversarial e independiente. Contexto: ${S}/CONTEXTO_MAESTRO.md. Otro agente acaba de hacer este encargo en ${R} (archivos: ${e.archivos}). Su informe fue:\n${String(informe).slice(0, 6000)}\n\n${e.verificar}\nNO edites ningún archivo. Si no hay problemas, devuelve la lista vacía. No inventes problemas.`,
    { label: `verificar:${e.key}`, phase: 'Verificar', schema: FINDINGS }
  ).then(v => ({ informe, hallazgos: (v && v.hallazgos) || [] })),
  (r, e) => {
    if (!r.hallazgos.length) return { encargo: e.key, informe: r.informe, hallazgos: [], correccion: 'Sin hallazgos.' }
    return agent(
      `Eres el editor del encargo «${e.key}» en ${R} (contexto: ${S}/CONTEXTO_MAESTRO.md). Archivos a tu cargo: ${e.archivos}. No edites otros archivos (otros agentes trabajan en paralelo). Un revisor informó estos hallazgos (JSON):\n${JSON.stringify(r.hallazgos, null, 1)}\n\n` +
      `Para CADA hallazgo verifica primero su evidencia en la fuente (puede estar equivocado); si es correcto, corrígelo. ` +
      (e.key === 'resaltado'
        ? `Vuelve a ejecutar el script y confirma el resultado. `
        : `Después compila con cd ${R}/05_Tesis_LaTeX && latexmk -f -interaction=nonstopmode -outdir=${S}/build_fix_${e.key} tesis.tex y confirma que no hay errores nuevos. `) +
      `Responde con una tabla: hallazgo → aplicado / descartado (motivo).`,
      { label: `corregir:${e.key}`, phase: 'Corregir' }
    ).then(c => ({ encargo: e.key, informe: r.informe, hallazgos: r.hallazgos, correccion: c }))
  }
)
return resultados