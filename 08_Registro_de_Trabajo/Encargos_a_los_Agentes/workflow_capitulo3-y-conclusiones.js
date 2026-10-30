export const meta = {
  name: 'capitulo3-y-conclusiones',
  description: 'Redacta el Capítulo 3 (resultados y discusión) y las conclusiones de la tesis, los verifica con cuatro lentes independientes y aplica las correcciones confirmadas',
  phases: [
    { title: 'Redactar', detail: 'Capítulo 3 y conclusiones con las cifras del modelo' },
    { title: 'Verificar', detail: 'cifras, citas, metodología y coherencia global' },
    { title: 'Corregir', detail: 'aplicar hallazgos confirmados y recompilar' },
  ],
}

const S = '/tmp/claude-0/-home-user-TesisSGC/c22f603c-c695-5c98-b48f-e99a1e2bf286/scratchpad'
const R = '/home/user/TesisSGC'

const FINDINGS = {
  type: 'object',
  properties: {
    lente: { type: 'string' },
    hallazgos: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          archivo: { type: 'string' },
          ubicacion: { type: 'string', description: 'sección, línea aproximada o texto citado' },
          problema: { type: 'string' },
          evidencia: { type: 'string', description: 'fuente exacta que prueba el problema (archivo, página, valor)' },
          correccion: { type: 'string', description: 'texto o acción concreta para corregir' },
          gravedad: { type: 'string', enum: ['alta', 'media', 'baja'] },
        },
        required: ['archivo', 'problema', 'evidencia', 'correccion', 'gravedad'],
      },
    },
  },
  required: ['lente', 'hallazgos'],
}

phase('Redactar')
const redaccion = await agent(
  `Lee y sigue COMPLETAS las instrucciones del archivo ${S}/PROMPT_W4_CAP3.md (redactar el Capítulo 3 y las conclusiones de la tesis). ` +
  `Antes, lee ${S}/CONTEXTO_MAESTRO.md completo, en especial las secciones 7, 8 y 9 (hallazgos, resultados definitivos del modelo y versión oficial de la PAO 3 firmada). ` +
  `Datos finales: las cifras del modelo están en ${R}/06_Modelo_de_Costos_y_Simulacion/tablas_latex/valores_modelo.tex (usa SIEMPRE las macros, no números escritos a mano) y la tabla de robustez en tablas_latex/tab_variantes.tex (insértala con \\tablamodelo{tab_variantes} en la sección de sensibilidad, con su caption, label tab:variantes y nota). ` +
  `El diagnóstico (cumplimiento ISO 9001 por cláusula, no conformidades, línea base) está en ${R}/05_Tesis_LaTeX/capitulos/30_capitulo2_diseno_sgc.tex y el diseño del SGC en 31_capitulo2_propuesta_sgc.tex: resume sus resultados en 3.1 sin contradecirlos (lee los números directamente de esos archivos). ` +
  `Otro agente puede estar terminando de pulir esos capítulos: no los edites. Edita SOLO 40_capitulo3_resultados.tex, 50_conclusiones.tex y, si hace falta, bib/cap3_resultados.bib. Al terminar responde con un resumen de lo escrito.`,
  { label: 'redactar-capitulo3', phase: 'Redactar' }
)

phase('Verificar')
const COMUN =
  `Estás verificando la tesis de grado en ${R}/05_Tesis_LaTeX/ (contexto completo en ${S}/CONTEXTO_MAESTRO.md). ` +
  `Revisa SOLO los archivos capitulos/40_capitulo3_resultados.tex y capitulos/50_conclusiones.tex recién redactados. NO edites ningún archivo: solo informa hallazgos concretos, con evidencia verificable (archivo y página o valor) y una corrección precisa. ` +
  `Si no encuentras problemas en tu lente, devuelve la lista vacía. No inventes problemas.`

const LENTES = [
  { key: 'cifras', prompt:
    `${COMUN} LENTE: CIFRAS. Comprueba cada número de ambos archivos contra: las macros de ${R}/06_Modelo_de_Costos_y_Simulacion/tablas_latex/valores_modelo.tex, resultados/resumen_resultados.json, resultados/variantes.json, parametros.json; los resultados del diagnóstico en capitulos/30_capitulo2_diseno_sgc.tex; los datos documentales de ${R}/03_Datos_Obra_Edificio_Posgrado/04_Extraccion_de_Datos/*.md; y las cifras oficiales de la PAO 3 firmada (sección 9 del contexto). Informa: números que no coinciden con su fuente, números del modelo escritos a mano en vez de con macros, porcentajes mal calculados, unidades erróneas, uso de cifras del Excel de la PAO 3 como si fueran las oficiales, y afirmaciones de pagos indebidos que no estén redactadas como inconsistencias por verificar.` },
  { key: 'citas', prompt:
    `${COMUN} LENTE: CITAS. Para cada \\textcite, \\parencite y similares: (1) la clave existe en ${R}/05_Tesis_LaTeX/bib/*.bib; (2) lo que se atribuye a la fuente coincide con las fichas verificadas de ${R}/04_Bibliografia/07_Fichas_de_Citas/*.json y *.md (y, si hace falta, con el PDF en la página indicada usando pdftotext o pymupdf); (3) el número de página es correcto; (4) no hay citas de segunda mano (atribuir a un autor original lo que solo se leyó en otra tesis); (5) el formato APA 7 de la cita en el texto es correcto (página con p. o pp., «y» entre dos autores, et al. desde tres autores). Informa cada discrepancia con la página correcta.` },
  { key: 'metodologia', prompt:
    `${COMUN} LENTE: METODOLOGÍA Y GUÍAS DEL DOCENTE. Lee los talleres ${R}/00_Material_Docente/Taller_4_Modelo_de_Investigacion.pdf y Taller_5_Comunicacion_de_Resultados.pdf (pdftotext). Verifica: los resultados se presentan en pasado, en párrafos, sin juicios de valor (la interpretación va en la discusión); cada objetivo específico OE1–OE5 de capitulos/10_introduccion.tex tiene resultados y una conclusión propia; las decisiones sobre HG, HE1 y HE2 aplican exactamente las reglas de la tabla tab:reglas-decision de capitulos/32_capitulo2_implementacion.tex y coinciden con \\DecHG, \\DecHEuno y \\DecHEdos; las limitaciones están declaradas; la validación por expertos queda pendiente sin resultados inventados; la discusión contrasta con los antecedentes y el marco teórico; la conclusión general responde la pregunta de investigación.` },
  { key: 'coherencia', prompt:
    `${COMUN} LENTE: COHERENCIA Y FORMATO. Verifica la coherencia con el resto de la tesis (introducción, capítulos 1 y 2, anexos): objetivos, hipótesis, nombres de secciones, labels y referencias cruzadas (\\ref a etiquetas que existan), terminología (IDM, CNC, CC, CU, PAF), y que no haya contradicciones. Compila con: cd ${R}/05_Tesis_LaTeX && latexmk -f -interaction=nonstopmode -outdir=${S}/build_verif_coherencia tesis.tex ; e informa errores o advertencias que provengan de 40_ o 50_ (referencias o citas indefinidas, cajas desbordadas de más de 10 pt), y problemas de formato APA en sus tablas y figuras (caption arriba, nota debajo, label). Mira con pdftoppm y la herramienta Read 2–3 páginas del Capítulo 3.` },
]

const resultados = await parallel(LENTES.map(l => () =>
  agent(l.prompt, { label: `verificar:${l.key}`, phase: 'Verificar', schema: FINDINGS })))
const hallazgos = resultados.filter(Boolean).flatMap((r, i) =>
  (r.hallazgos || []).map(h => ({ ...h, lente: r.lente || LENTES[i].key })))
log(`Hallazgos de verificación: ${hallazgos.length} (alta: ${hallazgos.filter(h => h.gravedad === 'alta').length})`)

phase('Corregir')
let correccion = 'Sin hallazgos que corregir.'
if (hallazgos.length) {
  correccion = await agent(
    `Eres el editor final del Capítulo 3 y de las conclusiones de la tesis en ${R}/05_Tesis_LaTeX/ (contexto en ${S}/CONTEXTO_MAESTRO.md). ` +
    `Revisores independientes informaron estos hallazgos (JSON):\n${JSON.stringify(hallazgos, null, 1)}\n\n` +
    `Para CADA hallazgo: verifica primero su evidencia en la fuente indicada (algunos pueden ser erróneos); si es correcto, aplica la corrección en capitulos/40_capitulo3_resultados.tex o capitulos/50_conclusiones.tex (o en bib/cap3_resultados.bib). No edites otros capítulos salvo un cambio mínimo imprescindible para una referencia cruzada, y si lo haces, dilo. ` +
    `Después compila con latexmk -f -interaction=nonstopmode -outdir=${S}/build_corr_cap3 tesis.tex, confirma que no quedan errores ni referencias indefinidas provenientes de esos archivos y revisa visualmente 2 páginas. ` +
    `Responde con una tabla: hallazgo → aplicado / descartado (motivo).`,
    { label: 'corregir-capitulo3', phase: 'Corregir' }
  )
}
return { redaccion, hallazgos, correccion }
