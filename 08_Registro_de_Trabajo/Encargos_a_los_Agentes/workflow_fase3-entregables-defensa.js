export const meta = {
  name: 'fase3-entregables-defensa',
  description: 'Redacta la explicacion en lenguaje sencillo, las preguntas del tribunal y la presentacion de defensa (HTML y PPTX), con revision adversarial de cifras, coherencia y diseno',
  phases: [
    { title: 'Redactar', detail: 'explicacion, preguntas del tribunal, presentacion' },
    { title: 'Verificar', detail: 'cifras y coherencia; diseno y Taller 6' },
    { title: 'Corregir', detail: 'aplicar hallazgos confirmados' },
  ],
}

const S = '/tmp/claude-0/-home-user-TesisSGC/c22f603c-c695-5c98-b48f-e99a1e2bf286/scratchpad'
const R = '/home/user/TesisSGC'
const E = `${R}/07_Entregables`

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

const FUENTES = `FUENTES (léelas antes de escribir): ${S}/CONTEXTO_MAESTRO.md (completo), ${S}/NOTAS_DEFENSA.md, ${S}/PROMPTS_FASE3.md; la tesis en ${R}/05_Tesis_LaTeX/capitulos/ (10_introduccion.tex; 20_capitulo1_marco_teorico.tex solo para conceptos; 30_, 31_ y 32_ del capítulo 2; 40_capitulo3_resultados.tex y 50_conclusiones.tex los está terminando otro agente ahora: léelos al final de tu trabajo y ajusta lo tuyo si ya están completos); las cifras del modelo SOLO de ${R}/06_Modelo_de_Costos_y_Simulacion/tablas_latex/valores_modelo.tex (macros), resultados/resumen_resultados.json y resultados/variantes.json; figuras en ${R}/06_Modelo_de_Costos_y_Simulacion/figuras/*.png y ${R}/05_Tesis_LaTeX/figuras/*.png; PDF compilado más reciente en ${R}/05_Tesis_LaTeX/Tesis_SGC_Borrador.pdf (puede estar algo desactualizado). `

const REGLAS = `REGLAS: (1) Toda cifra debe coincidir con su fuente; formato boliviano (punto de miles, coma decimal); al redondear, di «aproximadamente». (2) Decisiones del contraste: la hipótesis general (reducción ≥ 5 %) NO se acepta; HE1 y HE2 se aceptan (condicionadas a que el SGC se aplique); usa las macros \\DecHG, \\DecHEuno, \\DecHEdos y \\PHG, \\PRpos, \\rMedia, etc. para obtener los valores. (3) Los hallazgos sensibles de acero y cantidades son «inconsistencias documentales que deben verificar la Supervisión y la Fiscalización»: nunca «sobrepago», «corrupción», «fraude», ni nombres de personas. (4) Pendientes del postulante (nombres del postulante y del tutor, validación por expertos, APU contractual, etc.) quedan como marcadores visibles «[…]», nunca inventados. (5) No hagas git commit ni push. (6) LibreOffice: usa siempre un perfil propio para no chocar con otros agentes: soffice -env:UserInstallation=file://${S}/lo_<tu_nombre> --headless --convert-to pdf --outdir <dir> <archivo>. (7) Playwright para Node ya está instalado (require('playwright'); chromium.launch() sin opciones); no instales navegadores. `

const ENCARGOS = [
  {
    key: 'explicacion',
    salida: `${E}/Tesis_Explicada_en_Lenguaje_Sencillo.md, .docx y .html`,
    prompt: FUENTES + REGLAS +
`ENCARGO: escribir ${E}/Tesis_Explicada_en_Lenguaje_Sencillo.md, una explicación de la tesis que CUALQUIER persona pueda entender (familia, autoridades, estudiantes de primer año): español claro de Bolivia, oraciones cortas, sin jerga (o explicándola al usarla), con analogías concretas (la losa alivianada como un «sándwich» de viguetas, bloques de plastoformo y una capa de hormigón; el SGC como la lista de chequeo de un piloto o una receta con controles; Monte Carlo como «tirar los dados miles de veces»; el costo de no calidad como «pagar dos veces por hacer mal la primera»).
Estructura: 1) La tesis en un minuto (5–7 líneas). 2) ¿Qué se construía y qué pasó? (edificio, losa, paralización por la crisis de combustibles y resolución del contrato). 3) ¿Cuál era el problema? (desperdicio, falta de registros, costos de no calidad; ejemplos documentados: ≈5 % más plastoformo que el necesario, acero pagado ≈17 % por encima del teórico —como inconsistencia por verificar—, ninguna probeta de la losa). 4) ¿Qué es un sistema de gestión de la calidad y qué se diseñó? (plan de la calidad, puntos de inspección, control de materiales, conciliación de cantidades; en palabras simples). 5) ¿Cómo se evaluó sin construir la segunda losa? (simulación con y sin SGC). 6) ¿Qué se encontró? (reducción media del costo, probabilidad de ahorro, reducción del costo de no calidad, costo del propio SGC, ahorro esperado en bolivianos para los 2.234,60 m² restantes; el 5 % no se alcanza). 7) ¿Por qué no se alcanzó el 5 % y por qué igual vale la pena? 8) Límites honestos y qué falta. 9) Recomendaciones prácticas. 10) Glosario (20–30 términos). 11) Preguntas frecuentes (8–10).
Extensión: 3.500–5.000 palabras. Incluye 2–3 figuras del modelo con una explicación sencilla de cómo leerlas y una tabla resumen de cifras clave.
Después genera: (a) .docx con pandoc (--reference-doc=${E}/scripts/plantilla_apa.docx si da buen resultado; imágenes incluidas; título y tabla de contenidos); (b) .html autocontenido (CSS en línea, imágenes en base64, ancho máximo ≈ 760 px, letra grande, índice, colores definidos como variables con modo oscuro por prefers-color-scheme, imprimible, sin recursos externos). Verifica: abre el HTML con Playwright y mira 2 capturas (claro y oscuro); convierte el DOCX a PDF con LibreOffice y mira 2 páginas. Corrige lo que se vea mal.
Responde con un resumen (palabras, secciones, archivos).`,
    lentes: [
      { key: 'cifras', texto: `LENTE: cifras y fidelidad. Lee ${E}/Tesis_Explicada_en_Lenguaje_Sencillo.md y comprueba CADA cifra y afirmación contra valores_modelo.tex, resumen_resultados.json, variantes.json, el CONTEXTO_MAESTRO y los capítulos. Revisa también que el lenguaje sea realmente sencillo (señala frases con jerga sin explicar), que no haya acusaciones y que las decisiones sobre las hipótesis estén bien explicadas. Comprueba que el .docx y el .html tengan el mismo contenido que el .md (pandoc -t plain del docx y comparación de secciones).` },
    ],
  },
  {
    key: 'preguntas',
    salida: `${E}/Preguntas_del_Tribunal_y_Respuestas.md y .docx`,
    prompt: FUENTES + REGLAS +
`ENCARGO: escribir ${E}/Preguntas_del_Tribunal_y_Respuestas.md (y su .docx), la guía para que el postulante prepare la defensa ante el tribunal.
Contenido: 70–90 preguntas agrupadas por tema: título y alcance; problema y justificación; objetivos; hipótesis y umbral del 5 %; metodología y diseño (no experimental, línea base documental, evaluación ex ante); simulación de Monte Carlo y supuestos (triangulares, independencia/correlación, 20.000 iteraciones y convergencia, semilla, regla P ≥ 0,95 frente a α = 0,05, por qué no prueba t); línea base y datos (fuentes, IDM documentados, ausencia de registros); SGC, ISO 9001:2026, ISO 10005, PPI, procedimientos; normas técnicas (ACI 318-25 cap. 26 —26.12.7 para resultados bajos—, NB 997, NB 1225001/NBDS, CBH-87 citada por la ET); costos (PAF, APU de referencia y calibración κ, costo del SGC, quién paga y quién se beneficia); hallazgos documentales de acero y cantidades; resultados y no aceptación de la HG; validación por expertos pendiente; ética e integridad; aplicabilidad y replicabilidad; normativa boliviana de contratación (NB-SABS art. 89, DBC sustituido por la R.M. 048/2024, D.S. 5597, resolución del contrato); clima de Potosí; preguntas trampa.
Para CADA pregunta: «Respuesta sugerida» (3–6 líneas, precisa, con respaldo: sección/tabla/figura de la tesis o página de la fuente), «Qué decir» (frases clave) y «Qué NO decir».
Además: sección «Debilidades del trabajo y cómo defenderlas» (todas las de NOTAS_DEFENSA.md más: el marco normativo del hormigón —CBH-87 frente a NBDS/NB 1225001—; el Plano 02 frente a la altura mínima de 250 mm de la NBDS; el DBC 2022 sustituido; la elección de la PAO 3 firmada frente al Excel; la calibración κ del APU; el umbral del 5 % fijado en el perfil; independencia de las distribuciones; que el autor diseñe y evalúe su propio sistema; costo para el contratista frente a la entidad; un solo caso). Tabla «Cifras que debe saber de memoria» (con fuente). «Lista de verificación antes de la defensa» (nombres, tutor, escudo, validación por expertos aplicada y fichas firmadas, APU contractual solicitado, NB/ISO 9001:2026 en mano, conjunto de datos INE archivado, ensayo cronometrado de la presentación, planos y certificados impresos). «Conducta durante la defensa» según el Taller 6 (${R}/00_Material_Docente/Taller_6_Defensa_del_Trabajo_de_Graduacion.pdf; léelo con pdftotext).
Genera el .docx con pandoc (reference-doc ${E}/scripts/plantilla_apa.docx si queda bien) con títulos navegables y tablas legibles; conviértelo a PDF con LibreOffice y mira 2 páginas.
Responde con un resumen (n.º de preguntas por tema, debilidades cubiertas).`,
    lentes: [
      { key: 'cifras', texto: `LENTE: cifras, citas y exactitud técnica. Lee ${E}/Preguntas_del_Tribunal_y_Respuestas.md y comprueba cada cifra, cláusula de norma, artículo legal y página citada contra sus fuentes (macros del modelo, CONTEXTO_MAESTRO, fichas en ${R}/04_Bibliografia/07_Fichas_de_Citas/*.json, capítulos). Señala respuestas técnicamente débiles o incorrectas (estadística, costos, hormigón, ISO), y cualquier «qué decir» que contradiga la tesis.` },
      { key: 'cobertura', texto: `LENTE: cobertura y estrategia. Actúa como un tribunal exigente de Ingeniería Civil de la UATF. Lista las 15 preguntas más difíciles que harías sobre esta tesis (lee 10_, 30_, 31_, 32_ y, si están, 40_ y 50_) y comprueba si ${E}/Preguntas_del_Tribunal_y_Respuestas.md las cubre con una respuesta sólida. Informa como hallazgo cada pregunta difícil no cubierta o mal respondida (con la respuesta propuesta en «correccion»), y cada debilidad de NOTAS_DEFENSA.md que falte.` },
    ],
  },
  {
    key: 'presentacion',
    salida: `${E}/Presentacion_Defensa/ (Defensa_Tesis_SGC.html, Defensa_Tesis_SGC.pptx, Guion_de_Defensa.md)`,
    prompt: FUENTES + REGLAS +
`ENCARGO: preparar la presentación de la defensa en ${E}/Presentacion_Defensa/. Lee primero el Taller 6 (${R}/00_Material_Docente/Taller_6_Defensa_del_Trabajo_de_Graduacion.pdf, con pdftotext -layout) y cumple sus reglas (duración, estructura, tamaños de letra, cantidad de texto).
Productos:
(a) Defensa_Tesis_SGC.html: un solo archivo autocontenido (CSS y JS en línea, imágenes en base64, sin CDN), 16:9, escalado a la ventana; navegación con teclado (←/→/espacio/Inicio/Fin) y clic; barra de progreso y número de diapositiva; vista del orador con la tecla N (notas, cronómetro, siguiente diapositiva); modo impresión (una diapositiva por página). Títulos ≥ 28 pt y texto ≥ 24 pt a 1280 × 720.
(b) Defensa_Tesis_SGC.pptx (python-pptx, 13,333 × 7,5 in) con el mismo contenido y NOTAS DEL ORADOR en cada diapositiva (lo que se dice y el tiempo sugerido). Figuras del modelo y de la tesis; los diagramas del SGC que en la tesis son TikZ puedes recortarlos del PDF compilado (pdftoppm -r 200) o redibujarlos con formas nativas.
(c) Guion_de_Defensa.md: guion con tiempos por diapositiva (total dentro del rango del Taller 6) y transiciones.
Contenido (25–32 diapositivas + 4–6 de respaldo al final): carátula (título completo, «[Nombre del postulante]», «[Nombre del tutor]», UATF, Facultad de Ingeniería, Carrera de Ingeniería Civil, Potosí, 2026); problema con datos del caso; objeto, objetivos, hipótesis; metodología (diseño no experimental, línea base documental, simulación de Monte Carlo ex ante, regla de decisión P ≥ 0,95); marco teórico esencial (ISO 9001:2026, costo de la calidad PAF, desperdicio); caso de estudio (edificio, losa de 41 paños y 1.109,84 m², paralización y resolución); diagnóstico (cumplimiento ISO por cláusula, no conformidades y Pareto, línea base: EPS +5,01 %, acero +16,75 %, 0 probetas de losa); diseño del SGC (mapa de procesos, plan de la calidad, PPI, control de materiales, conciliación de cantidades, costo del SGC); modelo de costos y simulación; resultados (histograma, curva acumulada, tornado, costo de no calidad por componente; tabla del contraste HG/HE1/HE2); robustez (variantes); discusión breve frente a antecedentes; conclusiones por objetivo con el cumplimiento de la hipótesis; recomendaciones; limitaciones; cierre. Respaldo: APU de referencia, parámetros, convergencia, hallazgos documentales de acero, reglas de decisión.
Diseño: sobrio y académico (fondo claro, un color de acento sobrio, alto contraste), máximo 6 viñetas de ≤ 12 palabras, una idea por diapositiva, figuras grandes.
QA VISUAL OBLIGATORIO: convierte el PPTX a PDF con LibreOffice y renderiza CADA diapositiva (pdftoppm -r 50 -png); revísalas TODAS con Read buscando texto desbordado, superpuesto, cortado o ilegible, y corrige. Para el HTML, captura todas las diapositivas con Playwright a 1280 × 720 y revísalas igual. Repite hasta que no queden defectos.
Responde con: n.º de diapositivas, duración total del guion, defectos corregidos.`,
    lentes: [
      { key: 'contenido', texto: `LENTE: contenido y cifras. Revisa ${E}/Presentacion_Defensa/ (extrae el texto del PPTX con python-pptx, incluidas las notas; el HTML; el guion). Comprueba cada cifra contra las macros del modelo y los capítulos, que las conclusiones y decisiones sobre hipótesis coincidan con la tesis, que la estructura y los tiempos cumplan el Taller 6 (${R}/00_Material_Docente/Taller_6_Defensa_del_Trabajo_de_Graduacion.pdf) y que no haya acusaciones ni datos inventados. Comprueba que HTML y PPTX tengan las mismas diapositivas.` },
      { key: 'diseno', texto: `LENTE: diseño visual. Convierte el PPTX a PDF con LibreOffice (perfil propio) y renderiza TODAS las diapositivas (pdftoppm -r 50); captura con Playwright TODAS las diapositivas del HTML a 1280 × 720 (navega con la tecla ArrowRight). Míralas una por una con Read e informa cada defecto: texto desbordado, cortado o superpuesto; letra por debajo de 24 pt (títulos 28 pt); figuras pixeladas o deformadas; contraste bajo; diapositivas recargadas (> 6 viñetas o > 12 palabras por viñeta); inconsistencias entre HTML y PPTX. Prueba también la tecla N (vista del orador) y el modo impresión del HTML.` },
    ],
  },
]

const resultados = await pipeline(
  ENCARGOS,
  e => agent(e.prompt, { label: `redactar:${e.key}`, phase: 'Redactar' }),
  (informe, e) => parallel(e.lentes.map(l => () => agent(
    `Eres un revisor adversarial e independiente de un entregable de la tesis en ${R} (contexto: ${S}/CONTEXTO_MAESTRO.md y ${S}/NOTAS_DEFENSA.md; cifras del modelo en ${R}/06_Modelo_de_Costos_y_Simulacion/tablas_latex/valores_modelo.tex). Entregable: ${e.salida}. Informe del autor:\n${String(informe).slice(0, 5000)}\n\n${l.texto}\nNO edites ningún archivo (usa ${S}/revision_${e.key}_${l.key}/ para tus archivos temporales; LibreOffice con perfil propio: -env:UserInstallation=file://${S}/lo_rev_${e.key}_${l.key}). Si no hay problemas, devuelve la lista vacía. No inventes problemas.`,
    { label: `verificar:${e.key}:${l.key}`, phase: 'Verificar', schema: FINDINGS }
  )))
    .then(vs => ({ informe, hallazgos: vs.filter(Boolean).flatMap(v => v.hallazgos || []) })),
  (r, e) => {
    if (!r.hallazgos.length) return { encargo: e.key, informe: r.informe, hallazgos: [], correccion: 'Sin hallazgos.' }
    return agent(
      `Eres el autor del entregable «${e.key}» de la tesis en ${R}: ${e.salida}. ` + REGLAS +
      `Revisores independientes informaron estos hallazgos (JSON):\n${JSON.stringify(r.hallazgos, null, 1)}\n\n` +
      `Para CADA hallazgo verifica primero su evidencia (puede estar equivocado); si es correcto, corrígelo en TODOS los formatos del entregable (md/docx/html o html/pptx/guion) y regenera los derivados. Repite la revisión visual de lo que cambiaste. Edita solo archivos de tu entregable. Responde con una tabla: hallazgo → aplicado / descartado (motivo).`,
      { label: `corregir:${e.key}`, phase: 'Corregir' }
    ).then(c => ({ encargo: e.key, informe: r.informe, n_hallazgos: r.hallazgos.length, correccion: c }))
  }
)
return resultados