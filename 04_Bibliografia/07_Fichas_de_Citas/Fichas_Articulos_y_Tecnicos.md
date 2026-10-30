# Fichas de citas: artículos científicos y documentos técnicos

Grupo: 14 artículos de `04_Articulos_Cientificos/` y 7 documentos de `05_Documentos_Tecnicos/`. Actualizado el 30/10/2026. Documentos procesados: 21 de 21; fichas: 195.

**Cómo se verificó.**

- Cada `texto_exacto` es una copia literal de la capa de texto del PDF, con los espacios normalizados y los guiones de fin de línea unidos, tal como hace PyMuPDF.
- Para cada ficha se comprobó con PyMuPDF que `page.search_for(texto_exacto[:60])` lo encuentra en `pagina_pdf`, que el texto completo está en esa página y que tiene entre 8 y 50 palabras.
- Koskela (1992) es un escaneo sin capa de texto: se le aplicó OCR (`ocrmypdf --skip-text -l eng`), sus fichas llevan `capa_de_texto: false` y se verificaron sobre la copia OCR.
- `pagina_citable` es el folio impreso; si el documento no tiene folios, se indica «s. p.» con la sección o la tabla.
- No hubo acceso a Crossref (dominio bloqueado en la sesión). Por eso los datos que el PDF no imprime se señalan como **no verificados** en las notas de cada documento.

**Convenciones.** Hecho documentado = texto del PDF; cálculo propio = operación reproducible; cita secundaria = dato que el autor atribuye a otra fuente (por la regla del Taller 2, no citarlo como si se hubiera leído la fuente original).

## Consumos por m² en las fichas Concretec (lo que dicen y lo que no dicen)

**Hecho documentado.** Ninguna de las tres fichas Concretec del repositorio (ES-CC-1018 de hormigón premezclado, ES-CC-1021 de plastoform y ES-CC-1022 de viguetas) contiene tablas de consumo por m², es decir, metros de vigueta, piezas de complemento ni volumen de hormigón por m² de losa. Se revisaron la capa de texto y las imágenes de las 12 páginas. Lo que sí traen es la geometría:

- **Vigueta (ES-CC-1022, hoja 2):** a = 56 mm, b = 110 mm, h = 114,4 mm, L variable, peso promedio 17,2 kg, fyk 18.000 kg/cm² y hormigón de 350 kg/cm² (Santa Cruz, La Paz y Sucre); en Cochabamba, 60 × 121 × 112 mm y 19,5 kg. Tolerancias según la NB 997:2016: ±5 en la sección y +30/−20 en la longitud.
- **Sistema (ES-CC-1022, hoja 3):** paso D de 50, 55, 58 o 60 cm con vigueta simple y de 62, 70 o 72 cm con vigueta doble; complemento h1 de 10 a 25 cm (simple) o de 12 a 25 cm (doble); carpeta h2 = 5 cm; paquete H de 15 a 30 cm (simple) o de 17 a 30 cm (doble).
- **Complementos (ES-CC-1021):** 42 códigos con alto c de 10, 12, 15, 16, 20, 25 y 30 cm, ancho a de 42 a 63 cm, largo b de 100 o 130 cm y densidad de 8 a 10 kg/m³ (tabla completa en la ficha concretec2016plastoformo-02). Para 20 cm de alto hay 20 × 42, 20 × 43, 20 × 52 y 20 × 53 cm, con 100 o 130 cm de largo; **no hay 20 × 50 × 100 cm**, que es la medida de la ET de la obra.
- **Hormigón (ES-CC-1018):** H-10 a H-40, asentamiento de 8-10 cm (bombeado) o 6 cm (descarga directa) con tolerancia de ±2, y mixer de 8 m³; no da cantidades por m² de losa.

**Cálculo propio (geometría de la ficha, no dato del fabricante).** Para una losa de viguetas simples con paso D y complementos de largo L, la cantidad teórica bruta por m² es: vigueta = 1/D (m/m²); complementos = 1/(D × L) (pza/m²); carpeta = h2 × 1 m² = 0,05 m³/m². No se descuentan apoyos, bordes, nervios transversales ni macizados, ni se incluye desperdicio. El hormigón de los nervios no puede calcularse con las fichas, porque no dan el área de la sección de la vigueta ni el perfil del complemento.

| D (m) | Vigueta (m/m²) | Complementos de 1,00 m (pza/m²) | Complementos de 1,30 m (pza/m²) | Carpeta h2 (m³/m², mínimo) |
|---|---|---|---|---|
| 0,50 | 2,00 | 2,00 | 1,54 | 0,05 |
| 0,55 | 1,82 | 1,82 | 1,40 | 0,05 |
| 0,58 | 1,72 | 1,72 | 1,33 | 0,05 |
| 0,60 | 1,67 | 1,67 | 1,28 | 0,05 |

Con D = 0,50 m, que es la separación del certificado PRETENSA de la obra, y piezas de 1,00 m resultan 2,00 m de vigueta/m² y 2,00 complementos/m²; para 1.109,84 m², unos 2.220 complementos teóricos, lo que coincide con la estimación preliminar del contexto (≈ 2.220 piezas teóricas frente a 2.350 entregadas según el certificado de UNICON, sin descontar nervios ni bordes). La cantidad definitiva debe obtenerse con el Plano 03 (viguetas por paño) y con el manual del proveedor real (PRETENSA o UNICON), porque Concretec no es el proveedor de la obra.

## Tabla de antecedentes (artículos)

| Autores (año) | País | Objetivo | Método y muestra | Resultados con cifras | Uso en la tesis |
|---|---|---|---|---|---|
| Forcada, Gangolells, Casals y Macarulla (2017) | España | Determinar la influencia de las características del proyecto y de la gestión en el costo de los retrabajos. | Análisis documental de fichas técnicas e informes de no conformidad de una constructora certificada ISO 9001:2008: 788 incidencias en 40 proyectos (72,5 % infraestructura civil, 27,5 % edificación; 2005-2012); correlación de Pearson, pruebas t, ANOVA y regresión por pasos. | Retrabajo = 2,75 % del valor original del contrato; crecimiento medio del costo = 11 % (DE 14,99 %), sobre todo por ampliaciones de alcance pedidas por el cliente; sobreplazo medio de 15 %; el modelo retiene el valor del contrato y la ubicación de la obra (R² = 0,561); la edificación presenta mayor retrabajo que la obra civil. | Antecedente internacional y referencia del orden de magnitud del retrabajo; justifica registrar las no conformidades de forma estructurada dentro del SGC. |
| Khadim, Thaheem, Ullah y Mahmood (2023) | Pakistán | Identificar y cuantificar los costos de calidad visibles y ocultos (la «base del iceberg») en proyectos de edificación. | Modelo PAF modificado con fallas ocultas tangibles e intangibles; revisión de literatura, encuesta a 102 expertos para seleccionar 11 costos ocultos y recolección de datos de presupuestos e informes de 25 proyectos de edificación de 40 visitados. | Costo de la calidad medio = 12,76 % del costo total (DE 5,84 %); fallas visibles 2,34 % y ocultas 8,59 % (relación 1:3,67); conformidad 1,83 % (prevención 12 % y evaluación 2 % del costo de la calidad); COPQ = 10,94 %. | Base del instrumento de costos de calidad (rubros PAF y ecuaciones 1-6) y antecedente de la magnitud de la no calidad. |
| Dzul y Gracia (2009) | España (revisión internacional) | Analizar los sistemas de costos de la calidad aplicados a proyectos de construcción y su limitación en la fase de diseño. | Revisión bibliográfica de los sistemas QPMS, QPTS, QCM, CQCQS, PCM/QCPCM y PROMQACS, y de las prácticas de diseño. | Costos de calidad de 8-15 % del costo de obra (cita secundaria); QPMS: reprocesos de 12,4 % en 9 proyectos industriales; QCPCM en hormigonado: no conformidad de 0,48 % a 0,43 % (edificio) y de 3,55 % a 0,03 % (obra civil); los sistemas solo se aplican desde la ejecución. | Marco teórico de los costos de la calidad (PEF, COC/CONC) y contexto de su medición en obra. |
| Gracia Villar y Dzul López (2007) | España (revisión aplicada a constructoras) | Plantear el modelo PEF de costos de la calidad como herramienta de gestión en empresas constructoras. | Revisión bibliográfica de los modelos genéricos de costos de la calidad y propuesta de cuentas contables de calidad. | El modelo PEF sigue siendo el más usado; costos de calidad de 8-15 % de la construcción (cita de Lam et al., 1994, vía Low y Yeo, 1998); define prevención, evaluación y fallas internas y externas, el punto óptimo operativo provisional y el margen de no calidad aceptable. | Definiciones PEF en español para el marco teórico y estructura de cuentas del sistema de costos de calidad del SGC. |
| Maciel, Stumpf y Kern (2016) | Brasil | Proponer un sistema de planificación y control de residuos integrado al sistema de planificación y control de la producción de pequeñas y medianas constructoras. | Estudio de caso en una constructora de Novo Hamburgo: edificio residencial de 8 plantas y unos 5.000 m², con 25 meses de plazo; prueba en la mampostería (9 meses) con mediciones quincenales. | Pérdida presupuestada de mampostería de 8 % (46 m³ previstos); el indicador PPCRC de generación promedió 107,1 % y el de reúso 80,7 %; la Tabla 1 compila pérdidas brasileñas (acero 11-26 %, hormigón 1,5-13 %, cemento 33-83 %). | Índices de referencia de pérdidas de materiales, definición de «pérdida incorporada» y modelo de indicador de control integrado a la planificación (análogo para el SGC). |
| Rossi, Torres y Almeida (2001) | Brasil | Desarrollar un método para medir el costo de las pérdidas de mano de obra y de materiales en la construcción. | Combinación de costeo patrón (materiales) y costeo ABC (operaciones); dos estudios de caso de mampostería en Salvador (Bahía) con muestreo del trabajo, tarjetas de producción, control de viajes verticales y de dosificación e inventarios inicial y final. | Pérdidas de 38,5 % del costo de la mampostería en el caso A (≈ 29 % mano de obra y 9,2 % materiales) y de 49,2 % en el caso B; las pérdidas de mano de obra superan a las de materiales; se detectaron deficiencias de almacenamiento y manipulación de materiales. | Fórmula operativa del costo de las pérdidas de materiales, CPM = (CR − CTM) × costo unitario, para el modelo de costos de la tesis. |
| Romero y Serpell (2007) | Chile | Determinar si las constructoras habitacionales certificadas ISO 9001:2000 cumplen los principios de la gestión de la calidad. | Encuesta en entrevista personal, con escala Likert de 7 puntos, a 118 personas de 11 constructoras (universo de 34 certificadas); α de Cronbach = 0,973; análisis factorial y ANOVA. | Cumplimiento parcial de los principios (promedios de 5,3 a 6,3 sobre 7); las no conformidades se perciben como castigo (≈ 39 %) o para «cubrirse las espaldas» (≈ 39 %); el 40 % cree que los indicadores se miden solo por cumplir; los SGC «funcionan en el papel». | Advierte el riesgo de un SGC documental: la propuesta debe incluir verificación en obra, gestión real de no conformidades e indicadores útiles. |
| Prado-Román, del Castillo-Peces, Mercado-Idoeta y del Castillo-Peces (2018) | España | Analizar los efectos de implantar ISO 9001 en constructoras españolas de ingeniería civil y si dependen del tamaño y de la antigüedad de la certificación. | Cuestionario postal y en línea a los responsables de calidad de 302 empresas medianas, grandes y muy grandes (CNAE 42 y 43.1); 126 respuestas (41,72 %; error muestral 6,7 %); estadística descriptiva y ANOVA. | Efectos muy o extremadamente relevantes: comerciales 86,6 %, organizativos 74,4 %, gestión de clientes 62,2 %, operativos 53,7 %, financieros 34,2 % y de recursos humanos 31,7 %; el tamaño no influye y la antigüedad (≥ 5 años) sí, salvo en los efectos comerciales. | Evidencia de los beneficios internos (operaciones, reducción de costos por mala calidad) que justifica el SGC y advierte que maduran con el tiempo. |
| Luangcharoenrat, Intrachooto, Peansupap y Sutthinarakorn (2019) | Tailandia | Identificar y jerarquizar los factores que generan desperdicio de construcción en edificación. | Revisión de literatura (166 factores reducidos a 28, en 4 categorías); encuesta Likert de 5 puntos a contratistas (178 respuestas, marzo-diciembre de 2017; piloto α = 0,985); índice de importancia relativa (RII). | Factores principales: cambio de diseño (RII 0,726), actitudes de trabajo descuidadas (0,679) y almacenamiento inadecuado de materiales (0,669); por categorías: diseño y documentación 0,656, recursos humanos 0,642, métodos y planificación 0,603, materiales y adquisiciones 0,595. | Base para el diagrama de Ishikawa de las pérdidas de materiales y para los controles de recepción y almacenamiento del SGC; el RII sirve de modelo para la validación por expertos. |
| Abbott y Rodríguez (2008) | República Dominicana | Comparar los métodos de asignación directa y de optimización para cuantificar el acero de losas macizas y su efecto en el desperdicio. | Estudio descriptivo-correlacional: cuantificación del acero en 8 proyectos multifamiliares de Santo Domingo y encuesta a 40 ingenieros residentes. | El 54 % usa asignación directa y el 35 % optimización; el 86 % de quienes usan asignación directa reporta falta de acero; diferencia de 8,71 % en acero estructural y de 50,27 % en acero constructivo; se requeriría 19,5 % en lugar del 10 % recomendado. | Discusión del método de cómputo del acero de la losa (posible sobremedición o remedición del ítem 8, −3,65 %) y del desperdicio de acero por cortes. |
| Palanisamy y Palanichamy (2025) | India | Evaluar el efecto de los elementos del costo de la calidad (prevención, evaluación, fallas interna y externa) sobre el costo total de la calidad. | Datos de 16 proyectos de edificación de una constructora certificada ISO 9001 (entrevistas, informes de no conformidad y observación); diseño factorial 2⁴ y algoritmo de Yates; ANOVA con α = 0,05. | Costo total de la calidad de 1,571 % a 12,29 % del valor del proyecto; solo las fallas interna y externa resultan significativas (se rechaza H0 al 5 %); en el proyecto 13, la prevención permitiría bajar el costo de 12,29 % a 6,21 %. | Respaldo estadístico del efecto de la prevención sobre las fallas y modelo de contraste de hipótesis con nivel de significancia del 5 %. |
| Porras Díaz, Sánchez Rivera y Galvis Guerra (2014) | Colombia | Revisar la filosofía Lean Construction y sus herramientas para la gestión de proyectos de construcción. | Revisión bibliográfica: modelo TFV, Sistema del Último Planificador, LPDS, IPD y BIM. | Siete categorías de desperdicio; pérdidas estimadas de 30 % del costo de una obra de edificación (Picchi, 1993, citado); once principios de Koskela; PPC como indicador de cumplimiento. | Sección de Lean Construction y clasificación de pérdidas del marco teórico, en español. |
| Shaikh y Sohu (2020) | Pakistán | Identificar el grado de implementación de los elementos esenciales de ISO 9001 y sus ventajas en constructoras. | Cuestionario a profesionales de empresas certificadas (51; 49 % consultores, 38 % clientes, 13 % contratistas); 34 elementos de la literatura; índices RII y AI; SPSS. | Elemento más implementado: identificación de problemas actuales (RII 0,86); inspección del material antes de su uso, 0,83; rechazo de materiales no conformes, 0,66 (último lugar); la disminución del desperdicio de material es la segunda ventaja (AI 0,87). | Respalda que ISO 9001 reduce el desperdicio de material y muestra que el rechazo de material no conforme es el punto débil que el SGC debe reforzar. |
| Formoso, Isatto y Hirota (1999) | Brasil | Desarrollar un método para controlar el desperdicio en obras de edificación como parte de la gestión rutinaria. | Estudio de casos múltiples en tres pequeñas constructoras (septiembre de 1998 a febrero de 1999): mampostería, hormigonado, revoque y cerámica; planillas de producción y de consumo de recursos, inventarios, gráficos de control y auditorías mensuales. | Clasificación del desperdicio por posibilidad de control (evitable o inevitable), origen y naturaleza (nueve tipos); los gerentes no perciben la variabilidad; el control del desperdicio no está integrado a la planificación y se verifica en lugar de monitorear. | Definición de desperdicio, clasificación evitable/inevitable y diseño de los registros de control de materiales del SGC. |

## Referencias y fichas por documento

### Forcada et al. (2017) — Factors affecting rework costs in construction

**Referencia APA 7:** Forcada, N., Gangolells, M., Casals, M., & Macarulla, M. (2017). Factors affecting rework costs in construction. *Journal of Construction Engineering and Management, 143*(8), Artículo 04017032. https://doi.org/10.1061/(ASCE)CO.1943-7862.0001324

Clave BibLaTeX: `forcada2017` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/Forcada_2017_Factors_Affecting_Rework_Costs.pdf`

**Verificación:**

- El PDF del repositorio es el **manuscrito aceptado** (21 pp. numeradas 1-21), no la versión maquetada de ASCE. Por eso `pagina_citable` usa la numeración del manuscrito.
- La cabecera del manuscrito trae un dato erróneo: «2017, 20(4): 445-465». Ese volumen y esas páginas corresponden a Forcada et al. (2014a, *Journal of Civil Engineering and Management*), citado en la p. 18. Se conserva 143(8), Artículo 04017032, de Bibliografia_Recomendada.md: el PDF no imprime esos datos, pero sí el DOI (verificar en ASCE Library).
- Autores verificados en el PDF: Nuria Forcada, Marta Gangolells, Miquel Casals y Marcel Macarulla (UPC).
- El resumen dice «40 Spanish building projects», pero la p. 6 indica que el 72,5 % fueron de infraestructura civil y el 27,5 % de edificación. El borrador (10_introduccion.tex) habla de «40 obras de edificación»: conviene corregirlo por «40 proyectos de construcción».

#### forcada2017-01 · metodo · p. 1 (numeración del manuscrito aceptado) (PDF p. 1)

> In this study, data were analyzed from 788 construction incidents in 40 Spanish building projects to determine the influence of project and managerial characteristics on rework costs.

**Paráfrasis:** Forcada et al. analizaron 788 incidencias registradas en 40 proyectos de construcción españoles para determinar cómo influyen las características del proyecto y de la gestión en el costo de los retrabajos.

**Uso sugerido:** Introducción-Antecedentes

**Observación:** El resumen dice «building projects», pero la p. 6 precisa que el 72,5 % de los 40 proyectos fueron de infraestructura civil y el 27,5 % de edificación; no describir la muestra como «40 obras de edificación».

#### forcada2017-02 · dato · p. 2 (numeración del manuscrito aceptado) (PDF p. 2)

> Rework costs have been found to range from 5% to 20% of the contract value in construction and engineering projects, and changes in the scope of the design account for as much as 50% of the rework that occurs (Barber et al., 2000; Love and Edwards, 2004).

**Paráfrasis:** En la literatura revisada por Forcada et al., el costo de los retrabajos oscila entre el 5 % y el 20 % del valor del contrato, y los cambios de alcance del diseño explican hasta el 50 % de los retrabajos.

**Uso sugerido:** Introducción-Situación problemática | Cap.1 sección 1.4.2

**Observación:** Cita secundaria: el dato pertenece a Barber et al. (2000) y Love y Edwards (2004); citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### forcada2017-03 · definicion · p. 2 (numeración del manuscrito aceptado) (PDF p. 2)

> ISO 9000:2005 defines non-conformance as “the failure to fulfil a requirement”, and defect as “the non-fulfilment of a requirement related to an intended or specified use”.

**Paráfrasis:** La no conformidad se define como el incumplimiento de un requisito, mientras que el defecto es el incumplimiento de un requisito asociado a un uso previsto o especificado.

**Uso sugerido:** Cap.1 sección 1.10 (términos básicos)

**Observación:** Definición tomada por Forcada et al. de ISO 9000:2005; para la tesis conviene citar directamente ISO 9000:2026 si se dispone del texto.

#### forcada2017-04 · definicion · p. 2 (numeración del manuscrito aceptado) (PDF p. 2)

> The occurrence and subsequent rectification of a defect can be called rework, which is defined as “the unnecessary effort of redoing an activity or process that was incorrectly implemented the first time” (Love, 2002; Love and Edwards, 2004).

**Paráfrasis:** La aparición de un defecto y su posterior corrección constituyen el retrabajo, entendido como el esfuerzo innecesario de rehacer una actividad o proceso que se ejecutó incorrectamente la primera vez.

**Uso sugerido:** Cap.1 sección 1.4.2 | 1.10

**Observación:** Cita secundaria: el dato pertenece a Love (2002) y Love y Edwards (2004); citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### forcada2017-05 · metodo · p. 4 (numeración del manuscrito aceptado) (PDF p. 4)

> The data used for the purposes of this research were technical datasheets and non-conformance reports provided by one of the largest Spanish contractors. This company uses a structured method to register non-conformances, in accordance with ISO 9001:2008 certification. Therefore, it best met the aims of the research.

**Paráfrasis:** Los datos provinieron de fichas técnicas y de informes de no conformidad de una gran constructora española que registraba las no conformidades con un método estructurado conforme a su certificación ISO 9001:2008; ese registro sistemático hizo posible cuantificar el retrabajo.

**Uso sugerido:** Cap.2 (registro de no conformidades)

#### forcada2017-06 · dato · p. 6 (numeración del manuscrito aceptado) (PDF p. 6)

> Civil infrastructure projects comprised 72.5% of the total, and building projects comprised 27.5%. Public projects accounted for 82.5% of the total, whilst 17.5% were private projects.

**Paráfrasis:** De los 40 proyectos analizados, el 72,5 % correspondió a infraestructura civil y el 27,5 % a edificación; el 82,5 % fueron proyectos públicos y el 17,5 % privados.

**Uso sugerido:** Introducción-Antecedentes

#### forcada2017-07 · hallazgo · p. 8 (numeración del manuscrito aceptado) (PDF p. 8)

> Although the mean cost growth for the projects was 11%, with a standard deviation of 14.99%, the total costs of rework were found to vary considerably between projects. Rework costs stood at 2.75% of the OCV

**Paráfrasis:** El crecimiento medio del costo de los proyectos fue del 11 % (desviación estándar de 14,99 %), mientras que el costo de los retrabajos alcanzó el 2,75 % del valor original del contrato, con gran variación entre proyectos.

**Uso sugerido:** Introducción-Antecedentes | Cap.3 Discusión

#### forcada2017-08 · metodo · p. 15 (numeración del manuscrito aceptado) (PDF p. 15)

> The regression equation (R-squared=0.561, p<0.01) is expressed as: Ln(Rework costs) = -2.502+0.628* Ln(OCV)+0.316*Project Location (1) The value of 0.561 R-squared means that 56.1% of the rework cost variation is explained by this equation.

**Paráfrasis:** El modelo de regresión por pasos solo retuvo como predictores el valor original del contrato y la ubicación de la obra respecto de la sede de la empresa, y explica el 56,1 % de la variación del costo de retrabajo (R² = 0,561; p < 0,01).

**Uso sugerido:** Cap.3 Discusión

**Observación:** La ecuación (1) combina la constante no estandarizada (−2,502) con los coeficientes β estandarizados de la Tabla 6 (0,628 y 0,316), cuyos B son 0,757 y 0,647; usar la ecuación con cautela.

#### forcada2017-09 · hallazgo · p. 10 (numeración del manuscrito aceptado) (PDF p. 10)

> Figure 1 shows that building projects incur higher rework costs than civil engineering projects.

**Paráfrasis:** Los proyectos de edificación presentaron costos de retrabajo mayores que los de ingeniería civil, lo que los autores atribuyen a la complejidad de gestión: muchos interesados, plazos ajustados y clientes no especializados.

**Uso sugerido:** Cap.3 Discusión

#### forcada2017-10 · conclusion · p. 16 (numeración del manuscrito aceptado) (PDF p. 16)

> While the cost of rework was found to be 2.75% of the OCV and was due to errors and defects assumed by the contractor, the mean cost growth represented 11% of the OCV and mainly included extensions to the project scope requested by the client.

**Paráfrasis:** El costo de los retrabajos (2,75 % del valor original del contrato) se debió a errores y defectos asumidos por el contratista, mientras que el crecimiento medio del costo (11 %) se explicó sobre todo por ampliaciones de alcance solicitadas por el cliente.

**Uso sugerido:** Introducción-Antecedentes | Cap.3 Discusión

### Khadim et al. (2023) — Quantifying the cost of quality in construction projects

**Referencia APA 7:** Khadim, N., Thaheem, M. J., Ullah, F., & Mahmood, M. N. (2023). Quantifying the cost of quality in construction projects: An insight into the base of the iceberg. *Quality & Quantity, 57*(6), 5403–5429. https://doi.org/10.1007/s11135-022-01574-8

Clave BibLaTeX: `khadim2023` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/Khadim_2023_Quantifying_Cost_of_Quality_Construction.pdf`

**Verificación:**

- Verificado en el PDF: «Quality & Quantity (2023) 57:5403–5429», DOI, autores y título. Publicado en línea el 17/01/2023.
- El número del fascículo (6) no aparece impreso en el PDF; se toma de Bibliografia_Recomendada.md (pendiente de confirmar en Springer, porque no hubo acceso a Crossref).

#### khadim2023-01 · hallazgo · p. 5403 (PDF p. 1)

> Accordingly, a modified prevention, appraisal, and failure model is developed and applied to the primary data of 25 building projects. The findings highlight the unfamiliarity and passive attitude of the involved construction firms towards quality, thus, incurring higher failure costs amounting to over 12% of the total project cost.

**Paráfrasis:** Los autores desarrollaron un modelo de prevención, evaluación y fallas modificado, lo aplicaron a datos primarios de 25 proyectos de edificación y hallaron costos de falla superiores al 12 % del costo total del proyecto, atribuidos a la actitud pasiva de las empresas frente a la calidad.

**Uso sugerido:** Introducción-Antecedentes

#### khadim2023-02 · definicion · p. 5404 (PDF p. 2)

> Juran (1951) defined COQ to represent “all those costs which would disappear if there were no shortcomings”.

**Paráfrasis:** El costo de la calidad comprende todos los costos que desaparecerían si no existieran deficiencias.

**Uso sugerido:** Cap.1 sección 1.4.1 | 1.10

**Observación:** Cita secundaria: el dato pertenece a Juran (1951); citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### khadim2023-03 · metodo · p. 5406 (PDF p. 4)

> PAF model classifies the COQ into the Cost of Conformance (COC) and the Cost of Poor Quality (COPQ). COC is positive while COPQ is the negative cost, as shown in Fig. 1. The COC consists of prevention and appraisal costs.

**Paráfrasis:** El modelo PAF divide el costo de la calidad en costo de conformidad (prevención y evaluación), considerado positivo, y costo de la mala calidad o no conformidad, considerado negativo.

**Uso sugerido:** Cap.1 sección 1.4.1

#### khadim2023-04 · metodo · p. 5407 (PDF p. 5)

> The rule states that prevention is less costly than correction, which is less costly than failure. Therefore, it makes more sense to invest $1 in prevention than to spend $10 on correction or incur a $100 failure cost.

**Paráfrasis:** La regla 1-10-100 sostiene que prevenir cuesta menos que corregir y que corregir cuesta menos que fallar: conviene invertir 1 en prevención antes que gastar 10 en corrección o asumir 100 por una falla.

**Uso sugerido:** Cap.1 sección 1.4.1 | Cap.2 (justificación de la prevención)

#### khadim2023-05 · definicion · p. 5407 (PDF p. 5)

> COPQ is the cost of the product not meeting the requirement, also known as failure cost (Kazaz and Birgonul 2005). COPQ can be split into VF and HF.

**Paráfrasis:** El costo de la mala calidad (no calidad) es el costo de que el producto no cumpla el requisito, también llamado costo de falla, y se divide en fallas visibles y fallas ocultas.

**Uso sugerido:** Cap.1 sección 1.4.2 | 1.10

#### khadim2023-06 · metodo · p. 5416 (PDF p. 14)

> The cost items of prevention, appraisal, internal failure, and external failure were defined based on Table 1. Further, a new category of ‘HF cost’ was introduced in the original PAF model to accommodate hidden costs.

**Paráfrasis:** El marco de Khadim et al. define los rubros de prevención, evaluación, falla interna y falla externa, y añade una categoría de fallas ocultas (tangibles e intangibles). Sus ecuaciones son: COQ = COC + COPQ; COC = ΣP + ΣA; COPQ = ΣVF + ΣHF; ΣVF = ΣIF + ΣEF; ΣHF = Σht + Σhi; y el porcentaje respecto del costo total = costo considerado / (% de avance × costo total) × 100.

**Uso sugerido:** Cap.2 (instrumento de costos de la calidad)

**Observación:** Las ecuaciones 1-6 están en la misma página (p. 5416), pero en la capa de texto aparecen desordenadas; se transcribieron leyendo la página.

#### khadim2023-07 · dato · p. 5420 (PDF p. 18)

> The average VF (2.34%) for the given projects is greater than the average COC (1.83%) for all 25 projects.

**Paráfrasis:** En promedio, el costo de las fallas visibles (2,34 % del costo total) superó la inversión en conformidad (1,83 %) en los 25 proyectos, lo que ubica a las empresas a la izquierda del punto óptimo del diagrama de conformidad.

**Uso sugerido:** Cap.3 Discusión

#### khadim2023-08 · hallazgo · p. 5421 (PDF p. 19)

> On average, the VF is 2.34%, while HF amounts to 8.59% of the TPC. This means that the majority part of the failure cost is never realized.

**Paráfrasis:** Las fallas visibles representaron en promedio el 2,34 % del costo total y las ocultas el 8,59 %, de modo que la mayor parte del costo de las fallas nunca llega a percibirse.

**Uso sugerido:** Cap.1 sección 1.4.2 | Cap.3 Discusión

#### khadim2023-09 · dato · p. 5422 (PDF p. 20)

> COC only shares 14% of COQ, with significant spending (12%) on prevention activities. The low appraisal cost highlights the lack of quality checks and product tests in the studied projects.

**Paráfrasis:** La conformidad representó solo el 14 % del costo de la calidad, casi todo en prevención (12 %); el bajo gasto de evaluación revela pocas inspecciones y ensayos en los proyectos estudiados.

**Uso sugerido:** Cap.3 Discusión

**Observación:** Desglose completo de la Figura 8 (p. 5423): prevención 12 %, evaluación 2 %, falla interna 18 %, falla externa 1 %, oculta tangible 51 % y oculta intangible 16 % del costo de la calidad.

#### khadim2023-10 · hallazgo · p. 5423 (PDF p. 21)

> The average COQ for all the projects is 12.76% of TPC. According to Abdelsalam and Gad (2009), this percentage is greater than the best COQ practices; around 1% of TPC.

**Paráfrasis:** El costo de la calidad promedio de los 25 proyectos fue el 12,76 % del costo total, muy superior al valor de las mejores prácticas (alrededor del 1 %) citado por los autores.

**Uso sugerido:** Introducción-Antecedentes

**Observación:** La misma página reporta una desviación estándar de 5,84 %. El 1 % de buenas prácticas es cita secundaria de Abdelsalam y Gad (2009).

### Dzul y Gracia (2009) — Contexto actual de los sistemas de costes de la calidad

**Referencia APA 7:** Dzul, L. A., & Gracia, S. (2009). Contexto actual de los sistemas de costes de la calidad desarrollados y aplicados a proyectos de construcción: la necesidad de medición de la calidad en el diseño. *Informes de la Construcción, 61*(514), 41–50. https://doi.org/10.3989/ic.07.004

Clave BibLaTeX: `dzul2009` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/Dzul_2009_Costes_Calidad_Proyectos_Construccion.pdf`

**Verificación:**

- Verificado en el PDF: vol. 61, n.º 514, pp. 41-50, abril-junio de 2009, DOI y orden de autores (L. A. Dzul, S. Gracia).
- El 8-15 % del costo de obra es una **cita secundaria**: la referencia (2) es Low y Yeo (1998), que a su vez lo atribuyen a Lam et al. (1994), según Gracia Villar y Dzul López (2007, p. 44).

#### dzul2009-01 · dato · p. 42 (PDF p. 2)

> En el caso de la industria de la construcción, se estima que los costes de la calidad se encuentran entre un 8 a 15% de los costes de la construcción total (2).

**Paráfrasis:** En la industria de la construcción se estima que los costos de la calidad representan entre el 8 % y el 15 % del costo total de la obra.

**Uso sugerido:** Introducción-Situación problemática | Cap.1 sección 1.4

**Observación:** Cita secundaria: la referencia (2) es Low y Yeo (1998), quienes a su vez lo atribuyen a Lam et al. (1994), según Gracia Villar y Dzul López (2007, p. 44).

#### dzul2009-02 · definicion · p. 42 (PDF p. 2)

> Los costes de la calidad son aquellos gastos que se refieren a la corrección de fallos, a la verificación de procesos, a medidas que se tienen que tomar para obtener un mejor producto

**Paráfrasis:** Los costos de la calidad son los gastos asociados a corregir fallas, verificar procesos y adoptar medidas para obtener un mejor producto.

**Uso sugerido:** Cap.1 sección 1.4.1 | 1.10

#### dzul2009-03 · metodo · p. 42 (PDF p. 2)

> La mayoría de las compañías han empleado la universalmente aceptada estructura de costes de la calidad: costes de Prevención, Evaluación y Fallos (PEF), planteada recientemente en el contexto de las empresas constructoras por Gracia y Dzul (3).

**Paráfrasis:** La estructura de costos de la calidad más usada por las empresas es la de prevención, evaluación y fallas (PEF), adaptada a las constructoras por Gracia y Dzul.

**Uso sugerido:** Cap.1 sección 1.4.1

#### dzul2009-04 · dato · p. 43 (PDF p. 3)

> En esta investigación se observó que el 43% de las empresas certificadas, una vez deducidos los gastos por la implantación del sistema de calidad, incluidos los costes de certificación, se habían reducido los costes totales de la empresa al implantar un sistema de calidad.

**Paráfrasis:** En empresas certificadas ISO 9000 de la Comunidad Valenciana, el 43 % redujo sus costos totales al implantar el sistema de calidad, aun después de descontar los gastos de implantación y certificación.

**Uso sugerido:** Cap.1 sección 1.3 | Cap.3 Discusión

**Observación:** Cita secundaria: el dato pertenece a Climent Serrano (2003), referencia (7); citar como hallazgo reportado por el autor del artículo, no como fuente primaria. La misma página indica que la construcción fue el segundo sector en reducir costos.

#### dzul2009-05 · dato · p. 44 (PDF p. 4)

> Se probó en 9 proyectos industriales, produciendo un coste promedio de reprocesos o fallos del 12,4% del coste del proyecto (10).

**Paráfrasis:** El sistema QPMS del Construction Industry Institute, probado en 9 proyectos industriales, arrojó un costo promedio de reprocesos o fallas del 12,4 % del costo del proyecto.

**Uso sugerido:** Cap.1 sección 1.4.2

**Observación:** Cita secundaria: el dato pertenece a Aoieong et al. (2002), referencia (10); citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### dzul2009-06 · definicion · p. 45 (PDF p. 5)

> Los COC son los costes intrínsecos requeridos para proveer el producto final tal como es especificado y requerido, los CONC son los costes del tiempo de retraso, materiales, recursos y otros costes asociados a la rectificación de la insatisfacción del producto.

**Paráfrasis:** Los costos de conformidad son los costos intrínsecos necesarios para entregar el producto tal como se especificó; los de no conformidad son los de demoras, materiales, recursos y demás costos de corregir un producto insatisfactorio.

**Uso sugerido:** Cap.1 sección 1.4.1 | 1.10

#### dzul2009-07 · dato · p. 46 (PDF p. 6)

> En el caso del edificio 38 plantas, los costes de no conformidad, disminuyeron en el transcurso del estudio, de un 0,48% a un 0,43% de los costes totales del proceso.

**Paráfrasis:** Al aplicar el modelo de costos de proceso al hormigonado de un edificio de 38 plantas, los costos de no conformidad bajaron del 0,48 % al 0,43 % del costo total del proceso durante el estudio.

**Uso sugerido:** Cap.3 Discusión

**Observación:** Cita secundaria: el dato pertenece a Tang et al. (2004), referencia (20); citar como hallazgo reportado por el autor del artículo, no como fuente primaria. En el mismo párrafo, en una obra civil bajaron del 3,55 % al 0,03 %.

#### dzul2009-08 · conclusion · p. 48 (PDF p. 8)

> Los sistemas de costes de la calidad desarrollados para proyectos de construcción se aplican a partir de la fase de ejecución del proyecto; el diseño se considera solamente como una causa de fallos.

**Paráfrasis:** Los sistemas de costos de la calidad para obras se aplican desde la fase de ejecución, y el diseño solo se considera como causa de fallas, lo que limita su alcance.

**Uso sugerido:** Cap.1 sección 1.4

#### dzul2009-09 · conclusion · p. 49 (PDF p. 9)

> La medición de los costes de la calidad debería ser parte de cualquier programa de gestión de calidad.

**Paráfrasis:** La medición de los costos de la calidad debería formar parte de todo programa de gestión de la calidad.

**Uso sugerido:** Cap.2 (indicadores del SGC)

### Gracia Villar y Dzul López (2007) — Modelo PEF de costes de la calidad

**Referencia APA 7:** Gracia Villar, S., & Dzul López, L. A. (2007). Modelo PEF de costes de la calidad como herramienta de gestión en empresas constructoras: una visión actual. *Revista Ingeniería de Construcción, 22*(1), 43–56. https://ojs-az.lib.uc.cl/index.php/ric/article/view/16739

Clave BibLaTeX: `graciavillar2007` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/GraciaVillar_2007_Modelo_PEF_Costes_Calidad_Constructoras.pdf`

**Verificación:**

- **Orden de autores verificado en el PDF:** «Santos Gracia Villar, Luis A. Dzul López» (firma de la p. 43 y cornisas). El orden de Bibliografia_Recomendada.md es correcto; se elimina la nota «verificar el orden de autores». Dzul y Gracia (2009, ref. 3) lo citan en el mismo orden.
- Verificado: vol. 22, n.º 1, abril de 2007, pp. 43-56 («PAG. 43 - 56»).
- El PDF solo imprime www.ing.puc.cl/ric; la URL OJS proviene de Bibliografia_Recomendada.md (no verificada en línea).

#### graciavillar2007-01 · hallazgo · p. 43 (PDF p. 1)

> Se observó que el modelo genérico empleado con mayor frecuencia, sigue siendo el enfoque tradicional PEF (prevención, evaluación y fallos).

**Paráfrasis:** La revisión bibliográfica concluye que el modelo genérico de costos de la calidad más empleado sigue siendo el tradicional de prevención, evaluación y fallas (PEF).

**Uso sugerido:** Cap.1 sección 1.4.1

#### graciavillar2007-02 · definicion · p. 44 (PDF p. 2)

> Los QC son entendidos como la suma de costes de conformidad más costes de no conformidad, donde los primeros son el precio pagado por la prevención de la mala calidad generalmente (por ejemplo, la inspección y la evaluación de calidad)

**Paráfrasis:** Los costos de la calidad son la suma de los costos de conformidad y de no conformidad; los primeros son el precio de prevenir la mala calidad, por ejemplo, la inspección y la evaluación.

**Uso sugerido:** Cap.1 sección 1.4.1 | 1.10

#### graciavillar2007-03 · dato · p. 44 (PDF p. 2)

> Lam et al. (1994 citado por Low y Yeo, 1998) afirmaron que los costes de la calidad estaban entre de 8 a 15 % de los costes de la construcción total

**Paráfrasis:** Se ha reportado que los costos de la calidad en construcción se ubican entre el 8 % y el 15 % del costo total de la obra.

**Uso sugerido:** Introducción-Situación problemática

**Observación:** Cita de tercera mano (Lam et al., 1994, citado por Low y Yeo, 1998). Muestra el origen del 8-15 % que repite Dzul y Gracia (2009, p. 42); usar con esa advertencia.

#### graciavillar2007-04 · definicion · p. 46 (PDF p. 4)

> Los costes de prevención son los destinados a las actividades encargadas de asegurar la calidad del producto o servicio y lo costes de evaluación aquellos destinados a medir el nivel de la calidad conseguido en el proceso

**Paráfrasis:** Los costos de prevención se destinan a asegurar la calidad del producto o servicio, y los de evaluación a medir el nivel de calidad alcanzado en el proceso.

**Uso sugerido:** Cap.1 sección 1.4.1 | 1.10

**Observación:** El original dice «lo costes de evaluación» (errata del artículo).

#### graciavillar2007-05 · definicion · p. 46 (PDF p. 4)

> por otra parte los costes de fallos son aquellos derivados por la falta de calidad en productos o servicios antes de (internos) o después de ser entregados (externos) al cliente.

**Paráfrasis:** Los costos de fallas son los derivados de la falta de calidad de productos o servicios, ya sea antes de entregarlos (internos) o después de entregarlos al cliente (externos).

**Uso sugerido:** Cap.1 sección 1.4.1 | 1.10

#### graciavillar2007-06 · definicion · p. 49 (PDF p. 7)

> los costes de evaluación son todos los gastos para determinar si una actividad se realizo bien todas la veces: inspección y pruebas de materiales comprados, pruebas de aceptación en laboratorio, inspección, pruebas, comprobación de uso de mano de obra, entre otros.

**Paráfrasis:** Los costos de evaluación son los gastos para comprobar que una actividad se hizo bien siempre; incluyen la inspección y prueba de materiales comprados y las pruebas de aceptación en laboratorio.

**Uso sugerido:** Cap.2 (costos de evaluación del control de materiales)

#### graciavillar2007-07 · definicion · p. 49 (PDF p. 7)

> Los costes de fallas internas se refieren a los costes en que incurren las empresas como consecuencia de los errores detectados antes de que la producción sea aceptada por los clientes. Algunos ejemplos: desperdicios, repetición del trabajo, costes por suministro de materiales

**Paráfrasis:** Los costos de fallas internas son los que se originan en errores detectados antes de que el cliente acepte la producción; entre ellos figuran los desperdicios, la repetición del trabajo y los costos de suministro de materiales.

**Uso sugerido:** Cap.1 sección 1.4.1 | Cap.2

#### graciavillar2007-08 · metodo · p. 49 (PDF p. 7)

> De esta manera, un sistema eficaz de calidad debería operar en el punto de la curva llamado punto óptimo operativo provisional. Este punto representa el costo total de calidad mínimo y el rendimiento de la inversión es máximo en este punto para un momento determinado.

**Paráfrasis:** Un sistema de calidad eficaz debería operar en el punto óptimo operativo provisional de la curva de costos, donde el costo total de la calidad es mínimo y el rendimiento de la inversión es máximo en un momento dado.

**Uso sugerido:** Cap.1 sección 1.4.1

#### graciavillar2007-09 · metodo · p. 53 (PDF p. 11)

> Es conveniente incluir en estos estándares un cierto margen de maniobra para la no calidad aceptable, convenientemente controlado, ya que no existe el proceso perfecto.

**Paráfrasis:** Los costos normales deben incluir un margen controlado de no calidad aceptable, porque no existe un proceso perfecto; cada empresa define su margen según su competitividad.

**Uso sugerido:** Cap.2 (línea base y desperdicio aceptable)

#### graciavillar2007-10 · conclusion · p. 56 (PDF p. 14)

> un sistema de costes de la calidad no puede resolver por sí mismo los problemas de calidad u optimizar el sistema de gestión de calidad.

**Paráfrasis:** Un sistema de costos de la calidad no resuelve por sí solo los problemas de calidad ni optimiza el SGC: es una herramienta para dimensionar el problema y debe acompañarse de un proceso de mejora eficaz.

**Uso sugerido:** Cap.2 | Cap.3 Discusión

### Maciel, Stumpf y Kern (2016) — Sistema de planificación y control de residuos

**Referencia APA 7:** Maciel, T., Stumpf, M., & Kern, A. (2016). Propuesta de un sistema de planificación y control de residuos en la construcción. *Revista Ingeniería de Construcción, 31*(2), 105–116. https://doi.org/10.4067/S0718-50732016000200004

Clave BibLaTeX: `maciel2016` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/Maciel_2016_Sistema_Planificacion_Control_Residuos_Construccion.pdf`

**Verificación:**

- Verificado en el PDF: vol. 31, n.º 2, agosto de 2016, pp. 105-116, título en español (el título en inglés es «Management system proposal for planning and controlling construction waste») y autores tal como se imprimen: «T. Maciel, M. Stumpf, A. Kern».
- El DOI no figura en el PDF; se toma de Bibliografia_Recomendada.md (formato SciELO coherente con el vol. 31, n.º 2).
- El correo de correspondencia (mgonzalez@unisinos.br) sugiere que «M. Stumpf» es M. A. Stumpf González; se conserva la forma impresa.
- La Tabla 1 (p. 106) es una **compilación** de Pinto (1989), Soibelman (1993) y Agopyan et al. (1998): acero 11-26 % y hormigón premezclado 1,5-13 %. Se confirma la cifra «○» de Bibliografia_Recomendada.md.

#### maciel2016-01 · definicion · pp. 105-106 (PDF p. 1)

> Sin embargo, según Alarcón (2002), son consideradas pérdidas de la construcción todos los consumos de recursos (materiales, componentes, máquinas y mano de

**Paráfrasis:** Se consideran pérdidas en la construcción todos los consumos de recursos (materiales, componentes, máquinas y mano de obra) que superan el mínimo necesario para ejecutar la obra según el proyecto, es decir, los recursos que no agregan valor.

**Uso sugerido:** Cap.1 sección 1.5.1 | 1.10

**Observación:** La definición continúa en la p. 106; citar «pp. 105-106». Cita secundaria: el dato pertenece a Alarcón (2002); citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### maciel2016-02 · definicion · p. 106 (PDF p. 2)

> otra situación de pérdida de materiales, que son aquellos empleados en exceso pero que se quedan incorporados en la construcción. Por ejemplo, es el caso de un revoque ejecutado en espesor mayor que lo previsto en el proyecto. Se puede llamar esa situación de “pérdida incorporada”.

**Paráfrasis:** Además de los residuos visibles, existe la pérdida incorporada: material empleado en exceso que queda dentro de la construcción, como un revoque más grueso que el previsto en el proyecto.

**Uso sugerido:** Cap.1 sección 1.5.1 | 1.10

#### maciel2016-03 · dato · p. 106 (PDF p. 2)

> Pinto (1989) ha demostrado que la industria brasileña aceptó anteriormente altas pérdidas de materiales de construcción, incluyendo la pérdida incorporada, de aproximadamente 20% a 30% en masa.

**Paráfrasis:** En Brasil se aceptaban antes pérdidas de materiales, incluida la pérdida incorporada, de aproximadamente el 20 % al 30 % en masa.

**Uso sugerido:** Introducción-Situación problemática

**Observación:** Cita secundaria: el dato pertenece a Pinto (1989); citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### maciel2016-04 · hallazgo · p. 106 (PDF p. 2)

> Según Souza (2004), el nivel de pérdidas en la construcción disminuyó con la adopción de planes y certificaciones de calidad ISO, que entraron en el sector en los años 90.

**Paráfrasis:** El nivel de pérdidas en la construcción brasileña disminuyó con la adopción de planes de calidad y de certificaciones ISO desde los años noventa.

**Uso sugerido:** Introducción-Antecedentes | Cap.3 Discusión

**Observación:** Cita secundaria: el dato pertenece a Souza (2004); citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### maciel2016-05 · dato · p. 106 (PDF p. 2)

> Tabla 1. Pérdida de materiales en relación a las cantidades previstas en el proyecto (Brasil)

**Paráfrasis:** La Tabla 1 de Maciel et al. compila las pérdidas de materiales respecto de las cantidades del proyecto en Brasil: acero 11-26 %, cemento 33-83 %, hormigón premezclado 1,5-13 %, bloques y ladrillos 13-52 %.

**Uso sugerido:** Introducción-Situación problemática | Cap.1 sección 1.5.2

**Observación:** Compilación de Pinto (1989), Soibelman (1993) y Agopyan et al. (1998); citar como «compilado en Maciel et al. (2016, Tabla 1)».

*Tabla 1. Pérdida de materiales en relación a las cantidades previstas en el proyecto (Brasil)*

| Material | Pinto (1989) | Soibelman (1993) | Agopyan et al. (1998) |
|---|---|---|---|
| Acero | 26% | 19% | 11% |
| Arena | 39% | 44% | 44% |
| Bloques y ladrillos | 13% | 52% | 13% |
| Cal | 102% | - | 36% |
| Cemento | 33% | 83% | 56% |
| Hormigón premezclado | 1.5% | 13% | 9% |

#### maciel2016-06 · dato · p. 107 (PDF p. 3)

> Dias (2013) hice la medición de residuos en 20 obras de edificios construidos en el sur de Brasil calculando un promedio de 0.128 m3/m2.

**Paráfrasis:** En 20 edificios del sur de Brasil se midió una generación media de residuos de 0,128 m³ por m² construido; otro estudio con 18 obras halló 0,162 m³/m².

**Uso sugerido:** Cap.1 sección 1.5.2

**Observación:** Cita secundaria: el dato pertenece a Dias (2013) y Teixeira (2015); citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### maciel2016-07 · dato · p. 108 (PDF p. 4)

> Un PPC es bueno cuando está entre 60% y 80% (Akkari et al., 2004; Bortolazza, 2006).

**Paráfrasis:** Un porcentaje de planes completados (PPC) entre el 60 % y el 80 % se considera bueno.

**Uso sugerido:** Cap.2 (indicadores de planificación)

**Observación:** Cita secundaria: el dato pertenece a Akkari et al. (2004) y Bortolazza (2006); citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### maciel2016-08 · dato · p. 111 (PDF p. 7)

> La predicción de volumen generado tomó como base la tasa de pérdidas para mampostería considerada en el presupuesto inicial, de 8% de pérdidas, que es un valor común en la región.

**Paráfrasis:** La previsión de residuos de mampostería se basó en la tasa de pérdidas del presupuesto inicial, del 8 %, considerada un valor común en la región.

**Uso sugerido:** Cap.2 (línea base de desperdicio)

#### maciel2016-09 · dato · p. 113 (PDF p. 9)

> El volumen recolectado fue de 3.0 m3, mayor que el volumen planeado de 2.6 m3. Así, el índice PPCRC para generación puede ser calculado en 115.4%.

**Paráfrasis:** En la tercera quincena se recolectaron 3,0 m³ de residuos frente a 2,6 m³ previstos, por lo que el indicador PPCRC de generación fue del 115,4 %.

**Uso sugerido:** Cap.2 (indicador de control de residuos)

#### maciel2016-10 · hallazgo · p. 115 (PDF p. 11)

> El PPCRC de generación mediano fue mayor que 107%. Eso indica una generación mayor que la planeada. Por otro lado, el PPCRC de reúso mediano fue cerca de 81%, casi 20% menor que lo planeado.

**Paráfrasis:** En toda la etapa de mampostería, la generación de residuos superó lo planeado (PPCRC medio de 107 %) y el reúso quedó cerca del 81 %, casi 20 % por debajo de lo previsto.

**Uso sugerido:** Cap.3 Discusión

**Observación:** Las pp. 113 y 115 dan promedios de 107,1 % (generación) y 80,7 % (reúso).

### Rossi, Torres y Almeida (2001) — Método para medir los costos de las pérdidas

**Referencia APA 7:** Rossi, I., Torres, C., & Almeida, M. (2001). Método para medir los costos de las pérdidas en la industria de la construcción. *Revista Ingeniería de Construcción, 16*(2), 127–133. https://ojs-az.lib.uc.cl/index.php/ric/article/view/17303

Clave BibLaTeX: `rossi2001` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/Rossi_2001_Metodo_Medir_Costos_Perdidas_Construccion.pdf`

**Verificación:**

- Verificado en el PDF: «Revista Ingeniería de Construcción Volumen 16 Nº 2, Julio Diciembre 2001», título y autores tal como se imprimen («Iamara Rossi, Carlos Torres, Marcos Almeida»).
- **El PDF no tiene paginación impresa** (12 páginas sin folio). El rango 127-133 y la URL provienen de Bibliografia_Recomendada.md y no pudieron verificarse; por eso las fichas usan «s. p.» y la sección o tabla.
- El segundo autor firma con el correo formoso@vortex.ufrgs.br (UFRGS), lo que sugiere que es Carlos Torres Formoso; se conserva la forma impresa «Torres, C.».

#### rossi2001-01 · metodo · s. p. (secc. 1, Introducción) (PDF p. 1)

> Además de esto, busca introducir en la gestión de producción indicadores de costo de pérdidas, evitando que la toma de decisión sea basada solamente a través de indicadores de consumo de recursos.

**Paráfrasis:** El método busca incorporar a la gestión de la producción indicadores del costo de las pérdidas, para que las decisiones no se basen solo en indicadores de consumo de recursos.

**Uso sugerido:** Cap.2 (indicadores de costo de pérdidas)

#### rossi2001-02 · definicion · s. p. (secc. 2) (PDF p. 2)

> La pérdida corresponde a las operaciones que no agregan valor, estableciendo el desafío de eliminarlos del proceso.

**Paráfrasis:** La pérdida corresponde a las operaciones que no agregan valor, cuya eliminación del proceso constituye el desafío de la gestión.

**Uso sugerido:** Cap.1 sección 1.5.1 | 1.10

**Observación:** Concepto adoptado de Ohno (1997).

#### rossi2001-03 · definicion · s. p. (secc. 2) (PDF p. 3)

> la diferencia entre la cantidad realmente empleada en la ejecución del trabajo y la cantidad necesaria según el diseño.

**Paráfrasis:** La pérdida de materiales es la diferencia entre la cantidad realmente empleada en la ejecución y la cantidad necesaria según el diseño.

**Uso sugerido:** Cap.1 sección 1.5.2 | Cap.2 (índice de desperdicio)

**Observación:** La oración empieza en la página anterior: «la pérdida de materiales es dada por…». Concepto tomado de Soibelman (1993) y Agopyan et al. (1997).

#### rossi2001-04 · metodo · s. p. (secc. 4.5, Tabla 2) (PDF p. 8)

> Costo de las pérdidas de materiales (CPM) CR = Consumo real de material CTM = consumo teórico de material

**Paráfrasis:** El costo de las pérdidas de materiales se calcula como CPM = (CR − CTM) × costo unitario, donde CR es el consumo real y CTM el consumo teórico del material; el costo total de materiales es CR × costo unitario.

**Uso sugerido:** Cap.2 (modelo de costos) | Cap.1 sección 1.5.2

**Observación:** Las fórmulas son objetos de ecuación: en la capa de texto aparecen desordenadas y con la palabra portuguesa «Custo». En la tabla, la sigla CTM se usa tanto para el costo total de materiales como para el consumo teórico.

#### rossi2001-05 · metodo · s. p. (secc. 4.5) (PDF p. 8)

> Considerando que la parte tenida como esencial en las operaciones auxiliares es de difícil medición en la práctica, se consideró como pérdidas 75% de los tiempos auxiliares, a partir del indicador propuesto por Oglesby et al. (1989) para trabajo esencial (TEsencial).

**Paráfrasis:** Como la parte esencial de las operaciones auxiliares es difícil de medir, se consideró pérdida el 75 % de los tiempos auxiliares, según el indicador de trabajo esencial de Oglesby et al. (1989).

**Uso sugerido:** Cap.2 (supuestos del modelo)

#### rossi2001-06 · hallazgo · s. p. (secc. 5.1, Tabla 4) (PDF p. 9)

> Se observa que 38,5% de los costos totales de la producción de la mampostería fueron identificados como pérdidas, siendo cerca de 29% referentes a mano de obra (operaciones) y 9,2% a los materiales.

**Paráfrasis:** En el caso A, el 38,5 % del costo total de producción de la mampostería se identificó como pérdida: cerca del 29 % por mano de obra y el 9,2 % por materiales.

**Uso sugerido:** Introducción-Antecedentes | Cap.3 Discusión

#### rossi2001-07 · hallazgo · s. p. (secc. 5.1) (PDF p. 9)

> Además se notó, también, deficiencias en la administración de los materiales, principalmente con relación al almacenamiento y manejo de los mismos en las obras.

**Paráfrasis:** Se detectaron deficiencias en la administración de los materiales, sobre todo en su almacenamiento y manipulación en obra.

**Uso sugerido:** Cap.1 sección 1.5.1 | Cap.2 (control de materiales)

#### rossi2001-08 · hallazgo · s. p. (secc. 5.2, Tabla 6) (PDF p. 10)

> Se observa que 49,2 % de los costos totales de la producción de la mampostería fueron identificados como pérdidas, siendo éstas referentes, especialmente a mano de obra (operaciones).

**Paráfrasis:** En el caso B, el 49,2 % del costo total de producción de la mampostería se identificó como pérdida, principalmente de mano de obra.

**Uso sugerido:** Cap.3 Discusión

#### rossi2001-09 · conclusion · s. p. (secc. 6, Conclusiones) (PDF p. 10)

> Los costos de las pérdidas en la mano de obra son superiores a los de los materiales, principalmente los relacionados a las actividades que no agregan valor al producto

**Paráfrasis:** Las pérdidas de mano de obra costaron más que las de materiales, sobre todo las asociadas a actividades que no agregan valor, como la inspección y el transporte.

**Uso sugerido:** Cap.3 Discusión

### Romero y Serpell (2007) — Principios de la gestión de la calidad en constructoras ISO 9001

**Referencia APA 7:** Romero, T., & Serpell, A. (2007). Evaluando el logro de los principios de la gestión de la calidad en empresas constructoras certificadas según ISO 9001:2000. *Revista Ingeniería de Construcción, 22*(3), 197–213. https://doi.org/10.4067/S0718-50732007000300006

Clave BibLaTeX: `romero2007` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/Romero_2007_Principios_Gestion_Calidad_ISO9001_Constructoras.pdf`

**Verificación:**

- Verificado en el PDF: vol. 22, n.º 3, diciembre de 2007, pp. 197-213 («PAG. 197 - 213»), autores y título.
- El DOI no figura en el PDF; se toma de Bibliografia_Recomendada.md (formato SciELO coherente con el vol. 22, n.º 3).

#### romero2007-01 · metodo · p. 197 (PDF p. 1)

> se empleó un instrumento de medición que consistió en una encuesta aplicada como entrevista personal, que fue respondida por 118 personas de 11 constructoras habitacionales chilenas, de un universo de 34 empresas certificadas ISO 9001:2000.

**Paráfrasis:** El estudio aplicó una encuesta mediante entrevista personal a 118 personas de 11 constructoras habitacionales chilenas, de un universo de 34 empresas certificadas ISO 9001:2000.

**Uso sugerido:** Introducción-Antecedentes

#### romero2007-02 · hallazgo · p. 197 (PDF p. 1)

> El principal resultado de este estudio indica que las personas perciben que los principios de gestión de la calidad se están aplicando de manera insuficiente.

**Paráfrasis:** El personal de las constructoras certificadas percibe que los principios de la gestión de la calidad se aplican de manera insuficiente.

**Uso sugerido:** Introducción-Antecedentes

#### romero2007-03 · definicion · p. 199 (PDF p. 3)

> La norma ISO 9001:2000 identifica ocho principios que pueden ser utilizados por la dirección

**Paráfrasis:** La norma ISO 9001:2000 identifica ocho principios para mejorar el desempeño: enfoque al cliente, liderazgo, participación del personal, enfoque basado en procesos, enfoque de sistema para la gestión, mejora continua, enfoque basado en hechos para la toma de decisiones y relaciones mutuamente beneficiosas con el proveedor.

**Uso sugerido:** Cap.1 sección 1.2.3

**Observación:** La lista de principios figura en la misma página (p. 199).

#### romero2007-04 · hallazgo · p. 202 (PDF p. 6)

> los Profesionales creen que “las no conformidades se entienden como una forma de castigo” (aproximadamente 39%), que “el personal desvirtúa las no conformidades usándolas para cubrir sus espaldas” (alrededor del 39%) y sólo un 23% cree que se entienden como una forma de mejorar los procesos.

**Paráfrasis:** Cerca del 39 % de los profesionales cree que las no conformidades se entienden como castigo, otro 39 % que se usan para «cubrirse las espaldas» y solo el 23 % que sirven para mejorar los procesos.

**Uso sugerido:** Cap.2 (gestión de no conformidades) | Cap.3 Discusión

#### romero2007-05 · hallazgo · p. 202 (PDF p. 6)

> el 45% piensa que “se están midiendo los más importantes”, sin embargo, el 40% cree que “se miden sólo por cumplir y en realidad no se están utilizando para retroalimentar los procesos”.

**Paráfrasis:** El 45 % de los profesionales cree que se miden los indicadores más importantes, pero el 40 % opina que se miden solo por cumplir y que no retroalimentan los procesos.

**Uso sugerido:** Cap.2 (indicadores) | Cap.3 Discusión

#### romero2007-06 · hallazgo · p. 204 (PDF p. 8)

> el personal de obra piensa que “los recursos no están disponibles en forma oportuna por diferencias de objetivos entre la oficina central y las obras” (46%), “por problemas de flujo de caja” (18%), “problemas del proveedor” (18%), “mala planificación” (9%) o “por burocracia” (9%).

**Paráfrasis:** Para el personal de obra, los recursos no llegan a tiempo por diferencias de objetivos entre la oficina central y las obras (46 %), problemas de flujo de caja (18 %), problemas del proveedor (18 %), mala planificación (9 %) y burocracia (9 %).

**Uso sugerido:** Cap.1 sección 1.5.1 | Cap.3 Discusión

#### romero2007-07 · dato · p. 205 (PDF p. 9)

> El promedio más alto es de la “participación del personal” (6.3) y el promedio más bajo es de las “relaciones mutuamente beneficiosas con el proveedor”, la parte correspondiente a la relación contractual (5.3).

**Paráfrasis:** En la escala de 1 a 7, la participación del personal obtuvo el promedio más alto (6,3) y la relación contractual con el proveedor el más bajo (5,3).

**Uso sugerido:** Cap.3 Discusión

#### romero2007-08 · conclusion · p. 208 (PDF p. 12)

> Los resultados de esta investigación permiten establecer que las empresas constructoras habitacionales cumplen parcialmente con los principios de gestión de la calidad propuestos por la norma ISO 9001:2000,

**Paráfrasis:** Las constructoras habitacionales certificadas cumplen solo parcialmente los principios de la gestión de la calidad de ISO 9001:2000.

**Uso sugerido:** Introducción-Antecedentes

#### romero2007-09 · hallazgo · p. 208 (PDF p. 12)

> queda de manifiesto que la mayoría no está convencida de que la aplicación de esta norma les sea útil, más bien la ven como una fuente de trabajo extra.

**Paráfrasis:** La mayoría del personal no está convencida de la utilidad de la norma y la percibe como una fuente de trabajo adicional.

**Uso sugerido:** Introducción-Situación problemática | Cap.3 Discusión

#### romero2007-10 · conclusion · p. 209 (PDF p. 13)

> En el fondo, sus sistemas de gestión de la calidad funcionan en el papel perfectamente (la medida del desempeño de un sistema de gestión de la calidad es la mejora que ocurre en los sistemas de producción), pero en la práctica tienen varias falencias

**Paráfrasis:** Los SGC funcionan perfectamente en el papel, pero tienen varias falencias en la práctica, aunque su desempeño debería medirse por la mejora real de los sistemas de producción.

**Uso sugerido:** Cap.2 (implementación efectiva) | Cap.3 Discusión

### Prado-Román et al. (2018) — The effects of implementing ISO 9001 in the Spanish construction industry

**Referencia APA 7:** Prado-Román, C., del Castillo-Peces, C., Mercado-Idoeta, C., & del Castillo-Peces, J. (2018). The effects of implementing ISO 9001 in the Spanish construction industry. *Cuadernos de Gestión, 18*(1), 149–172. https://doi.org/10.5295/cdg.140507cd

Clave BibLaTeX: `pradoroman2018` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/PradoRoman_2018_Efectos_ISO9001_Construccion.pdf`

**Verificación:**

- Verificado en el PDF: vol. 18, n.º 1 (2018), pp. 149-172 según la cornisa del artículo (la portada de Redalyc dice «pp. 149-171»), DOI y autores. Publicado en línea el 4/05/2016.
- **Corrección de contenido:** el artículo concluye que el tamaño de la empresa **no** modifica significativamente los beneficios de ISO 9001 (ANOVA, p > 0,05), mientras que la antigüedad de la certificación **sí** influye, salvo en los efectos comerciales. Bibliografia_Recomendada.md y el borrador (10_introduccion.tex) dicen que los beneficios «dependen del tamaño y de la antigüedad», lo que debe corregirse.
- La capa de texto codifica la ligadura «fi» como «À» y «fl» como «Á». Los textos exactos se eligieron de modo que sus 60 primeros caracteres no contengan esos glifos, porque `search_for` no los encuentra.

#### pradoroman2018-01 · metodo · p. 150 (PDF p. 3)

> Para ello se ha remitido un cuestionario a los directores de calidad de 302 empresas de dicho sector, recibiéndose 126 cuestionarios válidos, cuyas respuestas fueron tratadas mediante un análisis descriptivo y ANOVA.

**Paráfrasis:** Se envió un cuestionario a los responsables de calidad de 302 empresas constructoras españolas y se obtuvieron 126 respuestas válidas, analizadas con estadística descriptiva y ANOVA.

**Uso sugerido:** Introducción-Antecedentes

#### pradoroman2018-02 · hallazgo · p. 152 (PDF p. 5)

> The standard must be effectively implemented in parallel with the internal development of basic quality management principles such as the systematisation of processes, continuous improvement, involvement of the entire Àrm and customer focus.

**Paráfrasis:** Para obtener beneficios, la norma debe implantarse de forma efectiva junto con los principios de la gestión de la calidad: sistematización de procesos, mejora continua, participación de toda la empresa y enfoque al cliente.

**Uso sugerido:** Cap.2 | Cap.3 Discusión

#### pradoroman2018-03 · definicion · p. 156 (PDF p. 9)

> Better use of resources, reduction in inspection costs, improvements in general efÀciency, reduction in logistics costs and production costs, reduction in nonconformities, improvements in meeting deadlines, reduction in expenses due to poor quality, etc.

**Paráfrasis:** Entre los efectos internos operativos de ISO 9001 figuran el mejor uso de los recursos, la reducción de los costos de inspección, logística y producción, la disminución de no conformidades y de los gastos por mala calidad, y el cumplimiento de plazos.

**Uso sugerido:** Cap.1 sección 1.3 | Cap.2 (beneficios esperados)

#### pradoroman2018-04 · metodo · p. 157 (PDF p. 10)

> Population 302 Sample size 126 (response rate: 41.72% of the population) ConÀdence level 95% (z = 1.96; p = q = 0.5) Sampling error 6.7%

**Paráfrasis:** La población fue de 302 empresas y la muestra de 126 (tasa de respuesta del 41,72 %), con un nivel de confianza del 95 % y un error muestral del 6,7 %.

**Uso sugerido:** Introducción-Antecedentes

#### pradoroman2018-05 · hallazgo · p. 163 (PDF p. 16)

> (74.4% and 53.7%, respectively) reported that ISO 9001 was ‘highly relevant’ or ‘extremely relevant’.

**Paráfrasis:** El 74,4 % de las empresas calificó a ISO 9001 como muy o extremadamente relevante para mejorar sus procesos organizativos, y el 53,7 % para mejorar sus operaciones.

**Uso sugerido:** Introducción-Antecedentes | Cap.3 Discusión

#### pradoroman2018-06 · hallazgo · p. 163 (PDF p. 16)

> (86.6% and 62.2%, respectively) reported that ISO 9001 was ‘highly relevant’ or ‘extremely relevant’.

**Paráfrasis:** El 86,6 % de las empresas calificó a ISO 9001 como muy o extremadamente relevante para los efectos comerciales y el 62,2 % para la gestión de clientes; el efecto financiero fue el menos valorado (34,2 %).

**Uso sugerido:** Introducción-Antecedentes

#### pradoroman2018-07 · hallazgo · p. 161 (PDF p. 14)

> Hence, the ANOVA showed the absence of differences in behaviour depending on the size of Spanish construction Àrms that have implemented ISO 9001.

**Paráfrasis:** El ANOVA no mostró diferencias en los efectos de ISO 9001 según el tamaño de las constructoras: el tamaño no condiciona los beneficios.

**Uso sugerido:** Introducción-Antecedentes | Cap.3 Discusión

**Observación:** Corrige el borrador y Bibliografia_Recomendada.md, que afirman que los beneficios «dependen del tamaño»: según el artículo, no dependen del tamaño, pero sí de la antigüedad de la certificación.

#### pradoroman2018-08 · hallazgo · p. 162 (PDF p. 15)

> Hence, the ANOVA showed the existence of differences in behaviour depending on the time elapsed since Spanish construction Àrms Àrst implemented ISO 9001 (more than Àve years vs. less than Àve years).

**Paráfrasis:** El ANOVA sí mostró diferencias según el tiempo transcurrido desde la certificación (más o menos de cinco años): las diferencias fueron significativas para todos los efectos internos y para los externos financieros y de clientes, pero no para los comerciales.

**Uso sugerido:** Introducción-Antecedentes | Cap.3 Discusión

**Observación:** La capa de texto codifica la ligadura «fi» como «À» y «fl» como «Á» (por ejemplo, «Àrms», «Àve», «inÁuence»); se respetó la copia literal.

#### pradoroman2018-09 · conclusion · p. 164 (PDF p. 17)

> Nevertheless, managers must be aware that these internal improvements in quality emerge gradually after the Àrm has implemented ISO 9001.

**Paráfrasis:** Las mejoras internas de calidad aparecen de forma gradual después de implantar ISO 9001.

**Uso sugerido:** Cap.3 Discusión (horizonte temporal del SGC)

#### pradoroman2018-10 · conclusion · p. 165 (PDF p. 18)

> Second, respondents were heads of quality at the participating Àrms, so their opinions may be biased due to a desire to portray implementation of the ISO 9001 as having had a positive outcome.

**Paráfrasis:** Como respondieron los responsables de calidad, sus opiniones pueden estar sesgadas a favor de mostrar un resultado positivo de ISO 9001; además, el error muestral del 6,7 % limita la generalización.

**Uso sugerido:** Cap.3 Discusión (limitaciones)

### Luangcharoenrat et al. (2019) — Factors influencing construction waste generation

**Referencia APA 7:** Luangcharoenrat, C., Intrachooto, S., Peansupap, V., & Sutthinarakorn, W. (2019). Factors influencing construction waste generation in building construction: Thailand's perspective. *Sustainability, 11*(13), Artículo 3638. https://doi.org/10.3390/su11133638

Clave BibLaTeX: `luangcharoenrat2019` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/Luangcharoenrat_2019_Factors_Construction_Waste_Generation.pdf`

**Verificación:**

- Verificado en el PDF: «Sustainability 2019, 11, 3638; doi:10.3390/su11133638», autores y título; recibido el 2/06/2019 y publicado el 2/07/2019.
- El número del fascículo (13) no está impreso, pero se deduce del DOI (patrón de MDPI: su + volumen 11 + número 13 + artículo 3638). La paginación citable es la impresa («N of 17»).
- La capa de texto usa ligaduras (ﬁ, ﬀ, ﬂ); los textos exactos las conservan literalmente, y `search_for` las encuentra así.

#### luangcharoenrat2019-01 · metodo · p. 1 (PDF p. 1)

> A total of 28 causes of construction waste were identiﬁed and grouped into the four categories: design and documentation, material and procurement, construction method and planning, and human resources.

**Paráfrasis:** A partir de la literatura se identificaron 28 causas del desperdicio de construcción, agrupadas en cuatro categorías: diseño y documentación, materiales y adquisiciones, métodos constructivos y planificación, y recursos humanos.

**Uso sugerido:** Cap.1 sección 1.5.1 | Cap.2 (Ishikawa)

**Observación:** La capa de texto usa ligaduras tipográficas (ﬁ, ﬀ); se respetó la copia literal.

#### luangcharoenrat2019-02 · hallazgo · p. 1 (PDF p. 1)

> Design change, inattentive working attitudes and behaviors, ineﬀective planning and scheduling, and material storage were among the highest impact factors on construction waste generation in each category.

**Paráfrasis:** Los factores de mayor impacto en cada categoría fueron el cambio de diseño, las actitudes y conductas de trabajo descuidadas, la planificación y programación ineficaces y el almacenamiento de materiales.

**Uso sugerido:** Cap.1 sección 1.5.1

#### luangcharoenrat2019-03 · metodo · p. 9 (PDF p. 9)

> The literature review identiﬁed 166 factors that aﬀect construction waste. These factors were cross referenced and reduced to 28

**Paráfrasis:** Los 166 factores identificados en la literatura se depuraron y combinaron hasta quedar en 28 factores de generación de desperdicio.

**Uso sugerido:** Cap.2 (Ishikawa)

#### luangcharoenrat2019-04 · metodo · p. 10 (PDF p. 10)

> The survey was open for ten months between March and December 2017. There were all together 178 survey respondents.

**Paráfrasis:** La encuesta estuvo abierta diez meses, de marzo a diciembre de 2017, y obtuvo 178 respuestas de contratistas tailandeses.

**Uso sugerido:** Introducción-Antecedentes

#### luangcharoenrat2019-05 · metodo · p. 10 (PDF p. 10)

> where W represents the weight that gives to each factor by the respondents and ranges from 1 to 5; (1) is strongly disagree and (5) is strongly agree; A represents the highest weight (i.e., 5 in this case); and N represents the total number of respondents.

**Paráfrasis:** El índice de importancia relativa se calcula como RII = ΣW/(A×N), con 0 < RII < 1, donde W es la puntuación de 1 a 5 de cada encuestado, A la puntuación máxima (5) y N el número de encuestados.

**Uso sugerido:** Cap.2 (validación por expertos)

#### luangcharoenrat2019-06 · hallazgo · p. 12 (PDF p. 12)

> The respondents ranked the “change to design” factor as the most contributing factor for construction waste generation, with RII equal to 0.726.

**Paráfrasis:** El cambio de diseño fue el factor que más contribuye a generar desperdicio (RII = 0,726).

**Uso sugerido:** Cap.1 sección 1.5.1

*Table 7. Relative important index (RII) and ranking of construction waste generation factors (n = 178)*

| Código | Factor | RII | Rango |
|---|---|---|---|
| D1 | Change to design | 0.726 | 1 |
| H3 | Inattentive working attitudes and behaviours | 0.679 | 2 |
| M1 | Improper material storage | 0.669 | 3 |
| H2 | Designers’ inexperience | 0.665 | 4 |
| H1 | Incompetent workers | 0.664 | 5 |
| D5 | Complicated design | 0.662 | 6 |
| D3 | Design errors | 0.653 | 7 |
| C11 | Ineffective planning and scheduling | 0.644 | 8 |
| C2 | Control and supervision | 0.634 | 9 |
| C4 | Poor waste management | 0.634 | 9 |
| C8 | Wrong teams/subcontractors selection | 0.631 | 10 |
| M3 | Material ordering problems | 0.626 | 11 |
| D4 | Construction drawing errors | 0.624 | 12 |
| M4 | Improper material handling | 0.620 | 13 |
| D2 | Documents problems | 0.618 | 14 |
| C3 | Construction methods | 0.615 | 15 |
| M5 | Material transporting problems | 0.608 | 16 |
| C7 | Reworks | 0.608 | 16 |
| C9 | By Process waste | 0.596 | 17 |
| C1 | Coordination problems | 0.585 | 18 |
| C5 | Tools and equipment misuse/malfunction | 0.585 | 18 |
| M7 | Defective materials | 0.580 | 19 |
| C10 | Construction errors | 0.578 | 20 |
| M6 | Packaging problems | 0.567 | 21 |
| H4 | Lack of suppliers involvement | 0.561 | 22 |
| M8 | Damaged materials | 0.552 | 23 |
| M2 | Material quality problems | 0.540 | 24 |
| C6 | Misuse of material | 0.528 | 25 |

Nota: Transcrito de la capa de texto (pp. 12-13). La tabla lista 28 factores con rangos compartidos.

#### luangcharoenrat2019-07 · dato · p. 12 (PDF p. 12)

> Table 8. Mean RII and ranking of categories of construction waste generation factors (n = 178).

**Paráfrasis:** Por categorías, el diseño y la documentación fue el grupo de mayor influencia (RII medio 0,656), seguido de recursos humanos (0,642), métodos constructivos y planificación (0,603) y materiales y adquisiciones (0,595).

**Uso sugerido:** Cap.1 sección 1.5.1

*Table 8. Mean RII and ranking of categories of construction waste generation factors (n = 178)*

| Categoría | RII | Rango |
|---|---|---|
| Design and Documentation (DEDO) | 0.656 | 1 |
| Human Resources (HUMA) | 0.642 | 2 |
| Construction Methods and Planning (COPL) | 0.603 | 3 |
| Material and Procurement (MAPR) | 0.595 | 4 |

#### luangcharoenrat2019-08 · hallazgo · p. 13 (PDF p. 13)

> The respondents ranked the “improper material storage” factor as the most contributing factor for construction waste generation, with RII equal to 0.669.

**Paráfrasis:** En materiales y adquisiciones, el almacenamiento inadecuado fue el factor más influyente (RII = 0,669), tercero entre los 28 factores.

**Uso sugerido:** Cap.1 sección 1.5.1 | Cap.2 (control de materiales)

#### luangcharoenrat2019-09 · hallazgo · p. 13 (PDF p. 13)

> Improper material storage is the third highest RII among construction waste generation factors. This problem always includes unsuitable storing methods and inappropriate protection [65]. Proper storage of material is highly necessary to mitigate construction waste generation.

**Paráfrasis:** El almacenamiento inadecuado incluye métodos de acopio impropios y protección insuficiente; un almacenamiento correcto es necesario para reducir el desperdicio.

**Uso sugerido:** Cap.2 (procedimiento de recepción y almacenamiento)

#### luangcharoenrat2019-10 · conclusion · p. 14 (PDF p. 14)

> (4) The amount and quality of materials on site should be checked and stored in the proper locations; (5) Site supervision and management should be done regularly, the lack of supervision may result in mistakes, reworks, and poor workmanship

**Paráfrasis:** Se recomienda verificar la cantidad y la calidad de los materiales en obra, almacenarlos en lugares adecuados y supervisar con regularidad, porque la falta de supervisión causa errores, retrabajos y mala ejecución.

**Uso sugerido:** Cap.2 (PPI y control de materiales)

### Abbott y Rodríguez (2008) — Cuantificación del refuerzo en placas sólidas y desperdicios

**Referencia APA 7:** Abbott, M., & Rodríguez, T. (2008). Análisis comparativo entre el método de asignación directa y el de optimización para la cuantificación del refuerzo levantado en los apoyos en placas sólidas y su efecto en la generación de desperdicios. *Ciencia y Sociedad, 33*(4), 572–594. https://www.redalyc.org/articulo.oa?id=87012672004

Clave BibLaTeX: `abbott2008` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/Abbott_2008_Cuantificacion_Refuerzo_Placas_Desperdicios.pdf`

**Verificación:**

- Verificado en el PDF: «Ciencia y Sociedad, vol. XXXIII, núm. 4, octubre-diciembre, 2008, pp. 572-594», autores y URL de Redalyc. La revista imprime el volumen en números romanos (XXXIII = 33).
- La primera página del PDF es la portada de Redalyc; el artículo empieza en la página 2 del PDF (p. 572).

#### abbott2008-01 · dato · p. 574 (PDF p. 4)

> Se sabe que entre un 35% y un 60% del valor de muchos proyectos que se ejecutan en la actualidad es destinado a las partidas de hormigón armado.

**Paráfrasis:** Entre el 35 % y el 60 % del valor de muchos proyectos actuales se destina a las partidas de hormigón armado.

**Uso sugerido:** Introducción-Situación problemática

**Observación:** El artículo no indica la fuente de este dato.

#### abbott2008-02 · metodo · p. 574 (PDF p. 4)

> Se conoce por una parte el método de Asignación Directa, que es el más antiguo, y consiste fundamentalmente en considerar la longitud de los elementos estructurales de forma directa y afectarla, según la experiencia o recomendaciones particulares, con un porcentaje de desperdicio.

**Paráfrasis:** El método de asignación directa toma la longitud de los elementos estructurales y la incrementa con un porcentaje de desperdicio fijado por experiencia o recomendación.

**Uso sugerido:** Cap.1 sección 1.5.2 | Cap.3 Discusión (cómputo del acero)

#### abbott2008-03 · dato · p. 583 (PDF p. 13)

> El desperdicio para acero precortado en fabrica es menos de un 1% y cuando este es cortado en obra es de 10%”.

**Paráfrasis:** El desperdicio del acero precortado en fábrica es inferior al 1 %, mientras que el del acero cortado en obra llega al 10 %.

**Uso sugerido:** Cap.1 sección 1.5.2

**Observación:** Cita secundaria: el dato pertenece a Dagostino y Feigenbaum (Estimating in Building Construction); citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### abbott2008-04 · metodo · p. 584 (PDF p. 14)

> Otra consideración importante que se plantea en este método es que los elementos constructivos o auxiliares de la losa (amarres y asientos) se asumen como el 20% del acero estructural.

**Paráfrasis:** En el método de asignación directa, el acero de los elementos auxiliares de la losa (amarres y asientos) se estima como el 20 % del acero estructural.

**Uso sugerido:** Cap.3 Discusión (cómputo del acero)

**Observación:** La misma página indica que las guías locales aplican un 7 % (Jiménez) o un 10 % (García Simó) de desperdicio.

#### abbott2008-05 · definicion · p. 587 (PDF p. 17)

> Desperdicio de acero. Es la longitud de acero no utilizable que resta al cortar una barra de dimensiones comerciales. Este desperdicio se expresa de manera cuantitativa como un porcentaje obtenido como el cociente de la longitud de acero no utilizable y la longitud total de la barra.

**Paráfrasis:** El desperdicio de acero es la longitud no utilizable que queda al cortar una barra comercial y se expresa como el porcentaje que representa respecto de la longitud total de la barra.

**Uso sugerido:** Cap.1 sección 1.10 | Cap.2

#### abbott2008-06 · metodo · p. 588 (PDF p. 18)

> No obstante, se seleccionó, para poder medir también la aplicabilidad en obra, una muestra de 8 proyectos al azar de viviendas multifamiliares ubicadas dentro del polígono central de Santo Domingo con sistemas constructivos adecuados al estudio y que estaban en construcción.

**Paráfrasis:** Se analizaron 8 proyectos de viviendas multifamiliares de Santo Domingo, elegidos al azar, y se encuestó a 40 ingenieros residentes.

**Uso sugerido:** Introducción-Antecedentes

#### abbott2008-07 · hallazgo · p. 589 (PDF p. 19)

> De los encuestados que dicen utilizar el método de asignación directa el 86% afirma que le falta acero con relación al calculado inicialmente

**Paráfrasis:** El 86 % de quienes usan el método de asignación directa declara que el acero estimado inicialmente resulta insuficiente en obra.

**Uso sugerido:** Cap.3 Discusión

#### abbott2008-08 · dato · p. 589 (PDF p. 19)

> Esto además se confirma que en el análisis comparativo existe una diferencia de un 8.71% entre el acero estructural calculado por optimización y el de asignación directa.

**Paráfrasis:** La diferencia entre el acero estructural calculado por optimización y por asignación directa fue del 8,71 %.

**Uso sugerido:** Cap.3 Discusión

#### abbott2008-09 · dato · p. 589 (PDF p. 19)

> Otro punto aún más evidente es el relacionado con el refuerzo del acero constructivo (amarres y asientos) donde se verifica una diferencia de un 50.27%

**Paráfrasis:** En el acero constructivo (amarres y asientos), la diferencia entre ambos métodos llegó al 50,27 %, por lo que no debería seguir usándose la «receta» del 20 %.

**Uso sugerido:** Cap.3 Discusión

#### abbott2008-10 · hallazgo · p. 590 (PDF p. 20)

> Para que por el método de asignación directa se pueda alcanzar la misma cantidad de acero estructural o lo más similar posible habría que aplicar a sus cálculos un 19.50 % en lugar de el 10% que recomienda.

**Paráfrasis:** Para igualar el acero estructural obtenido por optimización, el método de asignación directa tendría que aplicar un 19,50 % en lugar del 10 % que recomienda.

**Uso sugerido:** Cap.1 sección 1.5.2 | Cap.3 Discusión

### Palanisamy y Palanichamy (2025) — Cost of quality elements: design of experiments

**Referencia APA 7:** Palanisamy, I., & Palanichamy, S. (2025). Analysis and evaluation of cost of quality (COQ) elements on total quality costs in construction projects: Design of experiments. *Matéria (Rio de Janeiro), 30*, Artículo e20240738. https://doi.org/10.1590/1517-7076-RMAT-2024-0738

Clave BibLaTeX: `palanisamy2025` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/Palanisamy_2025_Cost_of_Quality_Elements_DOE.pdf`

**Verificación:**

- Verificado en el PDF: autores, título, DOI, «revista Matéria, v.30, 2025», recibido el 27/10/2024 y aceptado el 10/12/2024.
- **El PDF no imprime número de artículo ni paginación.** El número e20240738 proviene de Bibliografia_Recomendada.md y es coherente con el DOI, pero no se verificó; las fichas usan «s. p.» y la sección.
- Inconsistencias internas: el proyecto 13 aparece con 12,29 % (Tabla 1) y 12,19 % (secc. 3.1), y la prevención más la evaluación del proyecto 13 suman 29,45 % en la Tabla 1, no 29,54 % como dice el texto.

#### palanisamy2025-01 · metodo · s. p. (Abstract) (PDF p. 1)

> This study investigates the impact of COQ elements on total quality costs, analyzing 16 building projects using factorial design techniques.

**Paráfrasis:** El estudio analiza el efecto de los elementos del costo de la calidad sobre el costo total de la calidad en 16 proyectos de edificación, mediante diseño factorial.

**Uso sugerido:** Introducción-Antecedentes

#### palanisamy2025-02 · definicion · s. p. (secc. 1, Introduction) (PDF p. 2)

> It can be comprehensively defined as all expenditures incurred as a project progresses, encompassing both non-conformance-related costs and those associated with monitoring project quality [26].

**Paráfrasis:** El costo de la calidad comprende todos los gastos que se generan a lo largo del proyecto, tanto los asociados a las no conformidades como los de seguimiento de la calidad.

**Uso sugerido:** Cap.1 sección 1.4 | 1.10

#### palanisamy2025-03 · metodo · s. p. (secc. 2.1, Data collection) (PDF p. 3)

> The bill of quantities or current market prices are used to assess the cost of the supplies required to address the quality issue [50]. The projected time required to solve the problem is used to determine man and machine costs [51].

**Paráfrasis:** El costo de los materiales para corregir un problema de calidad se valora con el presupuesto (planilla de cantidades) o con precios de mercado, y el de mano de obra y equipo con el tiempo estimado de corrección.

**Uso sugerido:** Cap.2 (valoración de los costos de falla)

#### palanisamy2025-04 · dato · s. p. (secc. 2.2, Tabla 1) (PDF p. 4)

> Table 1: Percentage of total cost of quality which includes cost of prevention, cost of appraisal, and cost of failure.

**Paráfrasis:** La Tabla 1 muestra, para los 16 proyectos, el reparto del costo de la calidad entre prevención, evaluación, falla interna y falla externa, y el costo total de la calidad, que va del 1,571 % al 12,29 % del valor del proyecto.

**Uso sugerido:** Cap.3 Discusión

**Observación:** El texto (secc. 3.1) dice 12,19 % para el proyecto 13, pero la Tabla 1 indica 12,29 %.

*Table 1: Percentage of total cost of quality which includes cost of prevention, cost of appraisal, and cost of failure*

| Proyecto | Prevención % | Evaluación % | Falla interna % | Falla externa % | Costo total de calidad % |
|---|---|---|---|---|---|
| 1 | 29.81 | 45.30 | 14.90 | 9.99 | 2.237 |
| 2 | 63.41 | 27.81 | 8.78 | 0 | 1.587 |
| 3 | 29.31 | 58.50 | 10.23 | 1.96 | 3.079 |
| 4 | 38.34 | 47.92 | 13.74 | 0 | 2.312 |
| 5 | 27.38 | 39.92 | 32.7 | 0 | 3.720 |
| 6 | 54.03 | 27.58 | 18.39 | 0 | 1.571 |
| 7 | 28.07 | 46.83 | 25.1 | 0 | 4.543 |
| 8 | 36.97 | 45.95 | 17.09 | 0 | 3.552 |
| 9 | 24.36 | 24.06 | 14.27 | 37.31 | 4.921 |
| 10 | 35.80 | 22.17 | 13.08 | 28.95 | 5.046 |
| 11 | 14.84 | 60.01 | 14.08 | 11.06 | 5.323 |
| 12 | 35.98 | 46.11 | 7.51 | 10.4 | 2.910 |
| 13 | 18.99 | 10.46 | 33.35 | 37.19 | 12.29 |
| 14 | 36.59 | 14.96 | 38.31 | 10.41 | 7.820 |
| 15 | 22.63 | 48.01 | 17.62 | 11.75 | 5.741 |
| 16 | 29.90 | 44.66 | 15.24 | 10.3 | 6.040 |

Nota: Las cuatro primeras columnas son porcentajes del costo de la calidad; la última es el porcentaje del valor del proyecto.

#### palanisamy2025-05 · dato · s. p. (secc. 2.2.1) (PDF p. 4)

> In project 10, the cost is rectification of this failure is Rs.9,12,000. This can be avoided by soil investigations and suitable ground improvement techniques. The approximate cost is acquired for these activities Rs.2,00,000. The net saving is Rs.7,12,000.

**Paráfrasis:** En el proyecto 10, corregir el asentamiento del piso costó Rs 9,12,000, mientras que prevenirlo con estudios de suelo y mejora del terreno habría costado Rs 2,00,000: un ahorro neto de Rs 7,12,000.

**Uso sugerido:** Cap.3 Discusión (prevención frente a falla)

#### palanisamy2025-06 · hallazgo · s. p. (secc. 2.2.1) (PDF p. 5)

> The cost of saving through appropriate prevention and appraisal activities is Rs.22,19,500. The total quality cost reduces to 6.21%. Internal and external failure costs fall as preventative costs rise.

**Paráfrasis:** En el proyecto 13, que tenía el mayor costo de la calidad (12,29 %), las actividades de prevención y evaluación adecuadas permitirían ahorrar Rs 22,19,500 y reducir el costo total de la calidad al 6,21 %, porque las fallas internas y externas disminuyen al aumentar la prevención.

**Uso sugerido:** Cap.3 Discusión

#### palanisamy2025-07 · dato · s. p. (secc. 2.2.1) (PDF p. 5)

> In 2009, ROSENFELD [36] claimed that paying less than 2% on prevention and appraisal will unquestionably result in increased failure costs while investing more than 4% is likely to have no return.

**Paráfrasis:** Invertir menos del 2 % en prevención y evaluación aumenta inevitablemente los costos de falla, mientras que invertir más del 4 % probablemente no tiene retorno.

**Uso sugerido:** Cap.1 sección 1.4.1 | Cap.2

**Observación:** Cita secundaria: el dato pertenece a Rosenfeld (2009); citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### palanisamy2025-08 · dato · s. p. (secc. 3.1) (PDF p. 7)

> Project 13 has the highest failure cost (70.54%) due to excessively low preventive and appraisal costs (29.54%).

**Paráfrasis:** El proyecto 13 tuvo el mayor costo de falla (70,54 % del costo de la calidad) debido a una inversión muy baja en prevención y evaluación.

**Uso sugerido:** Cap.3 Discusión

**Observación:** Según la Tabla 1, la prevención más la evaluación del proyecto 13 suman 29,45 % (18,99 + 10,46), no 29,54 %.

#### palanisamy2025-09 · hallazgo · s. p. (secc. 3.3, Hypothesis) (PDF p. 8)

> The calculated F-values for internal failure costs (C) and external failure costs (D) surpass the tabulated F-values, indicating statistical significance.

**Paráfrasis:** Los valores F calculados para los costos de falla interna y externa superaron los valores tabulados: con un 95 % de confianza, ambos tienen un efecto significativo sobre el costo total de la calidad.

**Uso sugerido:** Cap.1 sección 1.4.2 | Cap.3 Discusión

#### palanisamy2025-10 · conclusion · s. p. (secc. 4, Conclusions) (PDF p. 11)

> is the essence of the quality cost: that spending on prevention yields a far higher return than spending on appraisal. This research proves the pre-eminence of prevention rather than the amelioration from appraisal.

**Paráfrasis:** La esencia del costo de la calidad es que invertir en prevención rinde mucho más que invertir en evaluación; el estudio sostiene la preeminencia de la prevención.

**Uso sugerido:** Cap.2 (justificación de la prevención)

### Porras Díaz, Sánchez Rivera y Galvis Guerra (2014) — Filosofía Lean Construction

**Referencia APA 7:** Porras Díaz, H., Sánchez Rivera, O. G., & Galvis Guerra, J. A. (2014). Filosofía Lean Construction para la gestión de proyectos de construcción: una revisión actual. *Avances: Investigación en Ingeniería, 11*(1), 32–53. https://doi.org/10.18041/1794-4953/avances.1.298

Clave BibLaTeX: `porrasdiaz2014` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/PorrasDiaz_2014_Filosofia_Lean_Construction_Gestion_Proyectos.pdf`

**Verificación:**

- Verificado en el PDF: «AVANCES Investigación en Ingeniería Vol. 11 - No. 1 (2014)», pp. 32-53 (folios impresos en la primera y la última página) y autores (Hernán Porras Díaz, Omar Giovanny Sánchez Rivera, José Alberto Galvis Guerra).
- El DOI no figura en el PDF; se toma de Bibliografia_Recomendada.md (no verificado en línea).

#### porrasdiaz2014-01 · definicion · p. 35 (PDF p. 4)

> Según el Lean Construction Institute (ILC), Lean construction es una filosofía que se orienta hacia la administración de la producción en construcción y su objetivo principal es reducir o eliminar las actividades que no agregan valor al proyecto y optimizar las actividades que sí lo hacen

**Paráfrasis:** Lean Construction es una filosofía de gestión de la producción en construcción cuyo objetivo es reducir o eliminar las actividades que no agregan valor y optimizar las que sí lo agregan.

**Uso sugerido:** Cap.1 sección 1.5.3 | 1.10

**Observación:** Cita secundaria: el dato pertenece a Lean Construction Institute; citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### porrasdiaz2014-02 · definicion · p. 35 (PDF p. 4)

> Entendiéndose por residuos todo lo que no genera valor a las actividades necesarias para completar una unidad productiva, LC clasifica los residuos de construcción en siete categorías como se muestra en la Tabla 1 [8].

**Paráfrasis:** Se entiende por residuo o desperdicio todo lo que no genera valor; Lean Construction los clasifica en siete categorías: defectos, demoras, excesos de procesado, exceso de producción, inventarios excesivos, transporte innecesario y movimiento no útil de personas.

**Uso sugerido:** Cap.1 sección 1.5.1

**Observación:** La Tabla 1 está en la p. 36 y proviene de un estudio sobre Abu Dhabi.

*Tabla 1. Desperdicios en la producción*

| Desperdicios en la construcción |
|---|
| Defectos |
| Demoras |
| Excesos de procesado |
| Exceso de producción |
| Inventarios excesivos |
| Transporte innecesario |
| Movimiento no útil de personas |

#### porrasdiaz2014-03 · dato · p. 36 (PDF p. 5)

> La tesis doctoral del doctor Flavio Picchi en 1993 plantea que en una obra de edificación normal el porcentaje de pérdidas por torre ejecutada es del 30%

**Paráfrasis:** En una obra de edificación normal, las pérdidas por torre ejecutada se estimaron en el 30 % del costo total de la obra.

**Uso sugerido:** Introducción-Situación problemática

**Observación:** Cita secundaria: el dato pertenece a Picchi (1993); la Tabla 2 se tomó de Orihuela; citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

*Tabla 2. Estimación de desperdicios en obras de edificación (porcentaje del costo total de obra)*

| Ítem | Descripción | % |
|---|---|---|
| Restos de material | Restos de mortero, de ladrillo y de madera; limpieza; retirada de material | 5% |
| Espesores adicionales de mortero | Tarrajeo de techos, de paredes internas y externas; contrapisos | 5% |
| Dosificaciones no optimizadas | Concreto; morteros de tarrajeo, contrapisos y revestimientos | 2% |
| Reparaciones y re-trabajos no computados en el resto de materiales | Repintado; retoques; corrección de otros servicios | 2% |
| Proyectos no optimizados | Arquitectura; estructuras; instalaciones sanitarias y eléctricas | 6% |
| Pérdidas de productividad debidas a problemas de calidad | Parada y operaciones adicionales por falta de calidad de los materiales y servicios anteriores | 3.5% |
| Costos debidos a atrasos | Pérdidas financieras por atrasos de las obras y costos adicionales de administración, equipos y multas | 1.5% |
| Costos en obras entregadas | Reparo de patologías ocurridas después de la entrega de obra | 5% |
| Total |  | 30% |

#### porrasdiaz2014-04 · metodo · p. 36 (PDF p. 5)

> La propuesta del concepto de producción de la filosofía “Lean” es verla como una transformación de materiales, un flujo de recursos y una generación de valor

**Paráfrasis:** Lean concibe la producción a la vez como transformación de materiales, flujo de recursos y generación de valor (modelo TFV).

**Uso sugerido:** Cap.1 sección 1.5.3

#### porrasdiaz2014-05 · definicion · p. 36 (PDF p. 5)

> El objetivo de LC es optimizar las transformaciones minimizando o eliminando los flujos que los materiales deben seguir hacia los lugares de ejecución de los trabajos de obra para obtener más valor en los productos finales [10].

**Paráfrasis:** El objetivo de Lean Construction es optimizar las transformaciones reduciendo o eliminando los flujos de materiales hacia los frentes de trabajo, para obtener más valor en el producto final.

**Uso sugerido:** Cap.1 sección 1.5.3

#### porrasdiaz2014-06 · metodo · p. 38 (PDF p. 7)

> Es decir, para que LC funcione se deben aplicar sus principios en forma concreta a las actividades del proyecto. Lauri Koskela propone once principios [22]:

**Paráfrasis:** Koskela propone once principios: reducir las actividades que no agregan valor, incrementar el valor del producto, reducir la variabilidad y el tiempo de ciclo, simplificar, flexibilizar, dar transparencia, controlar el proceso completo, mejorar continuamente, equilibrar las mejoras de flujo y de conversión, y aplicar la referenciación.

**Uso sugerido:** Cap.1 sección 1.5.3

**Observación:** La lista completa está en la misma página (p. 38).

#### porrasdiaz2014-07 · conclusion · p. 38 (PDF p. 7)

> Para la implementación de Lean Construction en los proyectos es necesario iniciar con el compromiso de tener una cultura de mejora continua de la producción

**Paráfrasis:** Implementar Lean Construction exige, ante todo, el compromiso con una cultura de mejora continua de la producción.

**Uso sugerido:** Cap.2 (cultura de la calidad)

#### porrasdiaz2014-08 · definicion · p. 42 (PDF p. 11)

> el Sistema Último Planificador mide el cumplimiento de lo programado en el plan mediante el porcentaje de programa cumplido PPC, el cual compara lo que se planeó hacer según el plan de trabajo semanal con lo que realmente fue hecho en obra.

**Paráfrasis:** El Sistema del Último Planificador mide el cumplimiento del plan con el porcentaje de programa cumplido (PPC), que compara lo planificado en el plan semanal con lo realmente ejecutado; PPC = actividades cumplidas / actividades programadas × 100.

**Uso sugerido:** Cap.2 (indicador PPC)

#### porrasdiaz2014-09 · conclusion · p. 50 (PDF p. 19)

> por que se genera desperdicios de recursos en obra que pueden llegar a casos de aproximadamente 30% de desperdicio.

**Paráfrasis:** Concebir la construcción solo como transformación genera desperdicios de recursos en obra que pueden llegar a cerca del 30 %.

**Uso sugerido:** Introducción-Situación problemática

### Shaikh y Sohu (2020) — Implementation, advantages and management of ISO 9001

**Referencia APA 7:** Shaikh, F. A., & Sohu, S. (2020). Implementation, advantages and management of ISO 9001 in the construction industry. *Civil Engineering Journal, 6*(6), 1136–1142. https://doi.org/10.28991/cej-2020-03091535

Clave BibLaTeX: `shaikh2020` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/Shaikh_2020_Implementation_ISO9001_Construction_Industry.pdf`

**Verificación:**

- Verificado en el PDF: vol. 6, n.º 6, junio de 2020, pp. 1136-1142, DOI y autores (Fazal Ali Shaikh, Samiullah Sohu).
- Inconsistencias internas: el resumen habla de 51 empresas con una tasa de respuesta del 59 %, y la p. 1138 de 51 profesionales; el texto da índices de 0,87 y 0,86 a las dos primeras ventajas, mientras que la Tabla 3 da 0,88 y 0,88 (el desperdicio de material tiene 0,87).

#### shaikh2020-01 · metodo · p. 1136 (PDF p. 1)

> Total 51 recognized Pakistani construction companies were considered and studied however the respondent rate remained 59%.

**Paráfrasis:** El estudio consideró 51 empresas constructoras pakistaníes reconocidas, con una tasa de respuesta del 59 %.

**Uso sugerido:** Introducción-Antecedentes

**Observación:** La p. 1138 menciona 51 profesionales de empresas certificadas; el artículo no aclara la relación entre las 51 empresas, la tasa del 59 % y los 51 encuestados.

#### shaikh2020-02 · hallazgo · p. 1136 (PDF p. 1)

> Advantages of ISO in the construction industry are Satisfaction of employees, Increment in the ratio of captivation new projects, Decrease in wastage of material and better contacts in global markets respectively.

**Paráfrasis:** Las principales ventajas de ISO 9001 en construcción fueron la satisfacción del personal, el aumento de la proporción de nuevos proyectos ganados, la disminución del desperdicio de material y mejores contactos en mercados globales.

**Uso sugerido:** Introducción-Antecedentes | Cap.1 sección 1.3

#### shaikh2020-03 · hallazgo · p. 1136 (PDF p. 1)

> ISO 9001 quality management system enhances performance and quality, in addition, it reduces the cost and time of construction projects; it is the result of the number of research studies [6].

**Paráfrasis:** Según la investigación previa revisada, el SGC ISO 9001 mejora el desempeño y la calidad y reduce el costo y el plazo de los proyectos de construcción.

**Uso sugerido:** Cap.1 sección 1.3

**Observación:** Cita secundaria: el dato pertenece a la referencia [6] del artículo; citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### shaikh2020-04 · hallazgo · p. 1137 (PDF p. 2)

> Similarly, advantages observed in construction firm later to implementation of ISO quality management system are as following; better job gratification of the employee, reduction in quality costs, work was carried out correctly right from the beginning, closer relationships with subcontractors and suppliers

**Paráfrasis:** Tras implantar el SGC ISO se observaron mayor satisfacción laboral, reducción de los costos de la calidad, trabajo bien hecho desde el inicio y relaciones más estrechas con subcontratistas y proveedores.

**Uso sugerido:** Cap.1 sección 1.3

**Observación:** Cita secundaria: el dato pertenece a las referencias [17-18] del artículo; citar como hallazgo reportado por el autor del artículo, no como fuente primaria.

#### shaikh2020-05 · metodo · p. 1138 (PDF p. 3)

> Figure 1 shows that respondents who were selected for this research were mostly consultants with 49%, client with 38% and contractor with 13%.

**Paráfrasis:** Los encuestados fueron consultores (49 %), clientes (38 %) y contratistas (13 %).

**Uso sugerido:** Introducción-Antecedentes

#### shaikh2020-06 · metodo · p. 1139 (PDF p. 4)

> The scale set here expresses that ISO elements having RII value 0.80 and above are fully implemented (F.I). Likewise, ISO elements having RII value between 0.80 and 0.65 are partially implemented (P.I) and ISO elements having RII value below 0.65 are not implemented (N.I).

**Paráfrasis:** Con el índice de importancia relativa, un elemento se considera totalmente implementado si RII ≥ 0,80, parcialmente implementado si está entre 0,65 y 0,80 y no implementado si RII < 0,65.

**Uso sugerido:** Cap.2 (diagnóstico ISO 9001)

#### shaikh2020-07 · dato · p. 1139 (PDF p. 4)

> Materials not per requirement and specification are rejected

**Paráfrasis:** El rechazo de materiales que no cumplen los requisitos y especificaciones fue el elemento de ISO 9001 con menor implementación (RII = 0,66, último de 34), mientras que la inspección antes del uso del material obtuvo RII = 0,83 (tercer lugar).

**Uso sugerido:** Cap.2 (control de materiales) | Cap.3 Discusión

*Table 2 (extracto). Questionnaire survey results on the endorsement of basic aspects’ in their firms*

| N.º | Aspecto básico de ISO 9001 | RII | Rango |
|---|---|---|---|
| 1 | Identification of current issues and removal of preventable credentials | 0.86 | 01 |
| 2 | Achievement of quality requirements is based on the quality system | 0.84 | 02 |
| 3 | Inspection before the usage of material | 0.83 | 03 |
| 4 | Regular inspection of construction work | 0.83 | 03 |
| 5 | Regular inspection of quality by team | 0.83 | 03 |
| 6 | Specification and information must be obtained prior to the purchase of any material or asset | 0.82 | 04 |
| 10 | Suppliers are continuously monitored | 0.79 | 06 |
| 23 | Quality based suppliers are selected | 0.74 | 10 |
| 34 | Materials not per requirement and specification are rejected | 0.66 | 18 |

Nota: Extracto de las filas relativas a materiales y proveedores (p. 1139); la tabla completa tiene 34 aspectos.

#### shaikh2020-08 · hallazgo · p. 1140 (PDF p. 5)

> Furthermore, the decrease in wastage of material was ranked second as the main advantage after the Implementation of ISO 9001. The AI values of first and second advantages are 0.87 and 0.86 respectively.

**Paráfrasis:** La disminución del desperdicio de material fue la segunda ventaja más importante de implantar ISO 9001.

**Uso sugerido:** Introducción-Antecedentes | Cap.3 Discusión

**Observación:** Inconsistencia interna: el texto da índices de 0,87 y 0,86, pero la Tabla 3 asigna 0,88 a los dos primeros factores y 0,87 a la disminución del desperdicio (rango 02).

*Table 3 (extracto). Questionnaire survey results on advantages after implementation of ISO 9001 in firms*

| N.º | Ventaja | AI | Rango |
|---|---|---|---|
| 1 | Satisfaction of employees | 0.88 | 01 |
| 2 | Increment in ratio of captivation new projects | 0.88 | 01 |
| 3 | Decrease in wastage of material | 0.87 | 02 |
| 4 | Better contacts in global markets | 0.84 | 03 |
| 5 | Overall efficiently of organization is improved | 0.82 | 04 |
| 7 | Defected work are improved at early stage | 0.80 | 05 |
| 8 | Optimization of resource usage | 0.79 | 06 |
| 15 | a smaller amount of rework is required | 0.73 | 09 |
| 17 | Boost in profit | 0.68 | 11 |
| 18 | Ease in identifying quality issues | 0.64 | 12 |

Nota: Valores AI leídos con pymupdf (find_tables) de la p. 1140; extracto de 10 de los 18 factores.

#### shaikh2020-09 · conclusion · p. 1140 (PDF p. 5)

> Most advantages of implementation for implementation of ISO are employees are satisfied, winning ratio of new construction projects, decrease in waste of material, increased efficiency of the company and contacts in the global market respectively.

**Paráfrasis:** Las ventajas más destacadas de implantar ISO 9001 fueron la satisfacción del personal, la mayor tasa de adjudicación de proyectos, la disminución del desperdicio de material, la mayor eficiencia de la empresa y los contactos en el mercado global.

**Uso sugerido:** Introducción-Antecedentes

### Formoso, Isatto y Hirota (1999) — Method for waste control in the building industry

**Referencia APA 7:** Formoso, C. T., Isatto, E. L., & Hirota, E. H. (1999). Method for waste control in the building industry. En *Proceedings of the 7th Annual Conference of the International Group for Lean Construction (IGLC-7)* (pp. 325–334). University of California, Berkeley. https://iglc.net/Papers/Details/69

Clave BibLaTeX: `formoso1999` · Archivo: `04_Bibliografia/04_Articulos_Cientificos/Formoso_1999_Method_Waste_Control_Building_Industry_IGLC.pdf`

**Verificación:**

- **Corrección de páginas:** el PDF va de la p. 325 a la p. 334 (10 páginas), no de 325 a 330 como dice Bibliografia_Recomendada.md.
- Verificado en el PDF: «Proceedings IGLC-7», «26-28 July 1999, University of California, Berkeley, CA, USA» y autores (Carlos Torres Formoso, Eduardo Luís Isatto, Ercilia Hitomi Hirota).
- El PDF no nombra al editor de las actas ni la URL; la URL proviene de Bibliografia_Recomendada.md (no verificada en línea).

#### formoso1999-01 · hallazgo · p. 326 (PDF p. 2)

> The waste of building materials is far higher than the nominal figures assumed by the companies in their cost estimates.

**Paráfrasis:** El desperdicio de materiales en edificación es muy superior a los valores nominales que las empresas suponen en sus presupuestos.

**Uso sugerido:** Introducción-Situación problemática | Cap.1 sección 1.5.2

**Observación:** Conclusión de los estudios brasileños previos (Soibelman, 1993; Agopyan et al., 1998) resumida por los autores.

#### formoso1999-02 · hallazgo · p. 327 (PDF p. 3)

> There is a very high variability of waste indices from site to site. Furthermore, similar sites might present different levels of wastes for the same material. This indicates that a considerable portion of this wastage can be avoided.

**Paráfrasis:** Los índices de desperdicio varían mucho entre obras, incluso entre obras similares y para el mismo material, lo que indica que una parte considerable de ese desperdicio es evitable.

**Uso sugerido:** Cap.1 sección 1.5.2 | Cap.3 Discusión

#### formoso1999-03 · hallazgo · p. 327 (PDF p. 3)

> As in the work of Skoyles (1976), most causes of waste are related to flaws in the management system, and have very little to do with the lack of qualification and motivation of workers.

**Paráfrasis:** La mayoría de las causas del desperdicio se relacionan con fallas del sistema de gestión y muy poco con la falta de calificación o motivación de los trabajadores.

**Uso sugerido:** Cap.1 sección 1.5.1

#### formoso1999-04 · hallazgo · p. 327 (PDF p. 3)

> A significant portion of waste is caused by problems which occur in stages that precede production, such as inadequate design, lack of planning, flaws in the material supply system, etc.

**Paráfrasis:** Una parte significativa del desperdicio se origina en etapas anteriores a la producción: diseño inadecuado, falta de planificación y fallas del sistema de suministro de materiales.

**Uso sugerido:** Cap.1 sección 1.5.1

#### formoso1999-05 · definicion · p. 328 (PDF p. 4)

> Therefore, waste should be defined as any losses produced by activities that generate direct or indirect costs but do not add any value to the product from the point of view of the client.

**Paráfrasis:** El desperdicio es toda pérdida producida por actividades que generan costos directos o indirectos sin agregar valor al producto desde el punto de vista del cliente.

**Uso sugerido:** Cap.1 sección 1.5.1 | 1.10

#### formoso1999-06 · definicion · p. 328 (PDF p. 4)

> Thus, waste can be classified in unavoidable waste (or natural waste), in which the investment necessary to its reduction is higher than the economy produced, and avoidable waste, when the cost of waste is significantly higher than the cost to prevent it.

**Paráfrasis:** El desperdicio inevitable (o natural) es aquel cuya reducción cuesta más que lo que ahorra; el evitable es aquel cuyo costo supera claramente el costo de prevenirlo.

**Uso sugerido:** Cap.1 sección 1.5.1 | Cap.2 (desperdicio aceptable)

#### formoso1999-07 · definicion · p. 329 (PDF p. 5)

> Production of defective products: it occurs when the final or intermediate product does not fit the quality specifications. This may lead to rework or to the incorporation of unnecessary materials to the building (indirect waste), such as the excessive thickness of plastering.

**Paráfrasis:** La producción de productos defectuosos ocurre cuando el producto final o intermedio no cumple las especificaciones de calidad y provoca retrabajo o la incorporación de material innecesario (desperdicio indirecto), como un revoque de espesor excesivo.

**Uso sugerido:** Cap.1 sección 1.5.1 | 1.4.2

#### formoso1999-08 · definicion · p. 329 (PDF p. 5)

> Inventories: related to excessive or unnecessary inventories which lead to material waste (by deterioration, losses due to inadequate stock conditions on site, robbery, vandalism), and monetary losses due to the capital that is tied up.

**Paráfrasis:** El desperdicio por inventarios se debe a existencias excesivas o innecesarias que generan pérdidas de material (deterioro, malas condiciones de acopio, robo, vandalismo) y pérdidas monetarias por capital inmovilizado.

**Uso sugerido:** Cap.1 sección 1.5.1 | Cap.2 (gestión del acopio)

#### formoso1999-09 · metodo · p. 331 (PDF p. 7)

> Data about the usage of materials and man-hours spent in the process are collected through a resource usage chart. In addition to the production and resource usage charts, a periodical inventory survey is necessary to monitor the amount of materials stored on site, and identify the origins of it.

**Paráfrasis:** El uso de materiales y de horas-hombre se registra en una planilla de consumo de recursos, complementada con un inventario periódico de los materiales acopiados en obra.

**Uso sugerido:** Cap.2 (registros de control de materiales)

#### formoso1999-10 · conclusion · p. 334 (PDF p. 10)

> The lack of integration of waste control with the planning and control process, and the need for not only verifying but also monitoring the efficiency of construction processes.

**Paráfrasis:** Una conclusión central es que el control del desperdicio no está integrado a la planificación y el control de la producción, y que hace falta no solo verificar sino monitorear la eficiencia de los procesos.

**Uso sugerido:** Cap.2 (integración del SGC con la planificación)

### Concretec (2018) — Ficha técnica de viguetas pretensadas (ES-CC-1022)

**Referencia APA 7:** Concretec. (2018). *Viguetas pretensadas* [Ficha técnica ES-CC-1022, rev. 7.0]. https://www.concretec.com.bo

Clave BibLaTeX: `concretec2018viguetas` · Archivo: `04_Bibliografia/05_Documentos_Tecnicos/Concretec_ES-CC-1022_2018_Ficha_Viguetas_Pretensadas.pdf`

**Verificación:**

- Verificado en la cabecera (capa de texto): «Código: ES-CC-1022 Rev.: 7.0 Fecha: 21/03/2018». El autor corporativo es la marca CONCRETEC; la razón social no figura. La URL www.concretec.com.bo solo aparece en el pie de página como imagen.
- **La ficha no contiene tablas de consumo por m²** (ni metros de vigueta por m², ni piezas de complemento por m², ni volumen de hormigón por m²). Se revisaron la capa de texto y las imágenes de las 4 páginas. Solo trae la geometría de la sección y del sistema (ver la sección «Consumos por m²»).
- Concretec no es el proveedor de la obra: las viguetas de la obra son de PRETENSA y el EPS de UNICON (certificados del 27/11/2025). La ficha sirve como referencia técnica nacional.

#### concretec2018viguetas-01 · definicion · s. p. (hoja 1) (PDF p. 1)

> Una vigueta es parte de un sistema estructural que constituye una losa alivianada, su función es absorber los esfuerzos de flexión que se presentan en los nervios modulares de la placa de losa

**Paráfrasis:** La vigueta es el elemento de una losa alivianada que absorbe los esfuerzos de flexión de los nervios y transmite las cargas de uso a la estructura y, de ella, a las fundaciones.

**Uso sugerido:** Cap.1 sección 1.6.1

#### concretec2018viguetas-02 · dato · s. p. (hoja 2, tabla de dimensiones) (PDF p. 2)

> SANTA CRUZ, LA PAZ, SUCRE VIGUETA PRETENSADA 56 110 114.4 Variable 17.2 18.000 350 Kg/cm2

**Paráfrasis:** La vigueta pretensada que Concretec fabrica en Santa Cruz, La Paz y Sucre mide 56 mm en la cabeza (a), 110 mm en la base (b) y 114,4 mm de alto (h); tiene un peso promedio de 17,2 kg, acero con fyk de 18.000 kg/cm² y hormigón de 350 kg/cm².

**Uso sugerido:** Cap.1 sección 1.6.1 | 1.6.3

**Observación:** La ficha no indica la longitud a la que corresponde el peso promedio.

*Vigueta pretensada Concretec: dimensiones de la sección (hoja 2 de la ficha ES-CC-1022)*

| Regional | Producto | a [mm] | b [mm] | h [mm] | L | Peso promedio [kg] | Fyk [kg/cm²] | Tipo de hormigón |
|---|---|---|---|---|---|---|---|---|
| Santa Cruz, La Paz, Sucre | Vigueta pretensada | 56 | 110 | 114.4 | Variable | 17.2 | 18.000 | 350 kg/cm² |
| Cochabamba | Vigueta pretensada | 60 | 121 | 112 | Variable | 19.5 | 18.000 | 350 kg/cm² |

Nota: La ficha no indica a qué longitud corresponde el «peso promedio [Kg]» (la longitud L es variable). Tolerancias: ±5 en la sección transversal y +30/−20 en la longitud, según la NB 997:2016.

#### concretec2018viguetas-03 · requisito_normativo · s. p. (hoja 2) (PDF p. 2)

> Nota: Las dimensiones pueden variar en la sección transversal ±5, longitudinal +30;-20 según lo establecido en norma NB 997:2016.

**Paráfrasis:** Las tolerancias dimensionales de la vigueta son ±5 en la sección transversal y +30/−20 en la longitud, según la NB 997:2016; sirven como criterio de aceptación en la recepción.

**Uso sugerido:** Cap.1 sección 1.7.3 | Cap.2 (recepción de viguetas)

**Observación:** La ficha no indica las unidades de la tolerancia; por coherencia con la tabla de dimensiones serían milímetros (verificar en la NB 997:2016).

#### concretec2018viguetas-04 · dato · s. p. (hoja 3, «Sistema de aplicación de la vigueta») (PDF p. 3)

> El espaciamiento entre viguetas permite aumentar la capacidad resistente de las losas, de la misma manera la variación de la altura del complemento permite generar losas más rígidas y estables.

**Paráfrasis:** La separación entre viguetas y la altura del complemento definen la capacidad y la rigidez de la losa: con vigueta simple, el paso D es de 50, 55, 58 o 60 cm, el complemento mide de 10 a 25 cm de alto, la carpeta 5 cm y el paquete estructural de 15 a 30 cm.

**Uso sugerido:** Cap.1 sección 1.6.1 | 1.6.3

**Observación:** La geometría de esta tabla permite calcular la cantidad teórica por m² (ver la sección «Consumos por m²»).

*Sistema de aplicación de la vigueta (hoja 3 de la ficha ES-CC-1022)*

| Descripción | Referencia | Simple [cm] | Doble [cm] |
|---|---|---|---|
| Distancia entre ejes (paso) | D | 50-55-58-60 | 62-70-72 |
| Altura de complemento | h1 | de 10 a 25 | de 12 a 25 |
| Altura de carpeta de compresión | h2 | 5 | 5 |
| Altura paquete estructural | H | de 15 a 30 | de 17 a 30 |

Nota: En la imagen de la ficha aparecen en negrita los valores 55 (paso simple), 25 (h1 simple) y 12 y 25 (h1 doble).

#### concretec2018viguetas-05 · requisito_normativo · s. p. (hoja 3) (PDF p. 3)

> Para un correcto manipuleo de la vigueta y su correspondiente colocado en obra, CONCRETEC cuenta con un Manual de Colocación de Viguetas que será provisto en el momento de adquirir nuestro producto.

**Paráfrasis:** El fabricante entrega con la compra un Manual de Colocación de Viguetas para la manipulación y la colocación correctas en obra.

**Uso sugerido:** Cap.2 (procedimiento de colocación)

**Observación:** El manual no está en el repositorio; los consumos por m² y las recomendaciones de colocación deberían buscarse en él o en el del proveedor real (PRETENSA).

#### concretec2018viguetas-06 · requisito_normativo · s. p. (hoja 3, «Ventajas») (PDF p. 3)

> Cumplimiento de la Norma Boliviana NB 997 Elementos Prefabricados de Hormigón - Viguetas Prefabricadas de Hormigón Pretensado - Requisitos y Métodos de Ensayos

**Paráfrasis:** La vigueta cumple la NB 997 (viguetas prefabricadas de hormigón pretensado: requisitos y métodos de ensayo), cuenta con sello de calidad IBNORCA y el fabricante tiene un SGC certificado con ISO 9001:2008.

**Uso sugerido:** Cap.1 sección 1.7.3

#### concretec2018viguetas-07 · dato · s. p. (hoja 3) (PDF p. 3)

> Mayor sección de vigueta que disminuye la cantidad de hormigón vaciado en la losa de compresión

**Paráfrasis:** Según el fabricante, la mayor sección de su vigueta reduce la cantidad de hormigón vaciado en la losa de compresión.

**Uso sugerido:** Cap.1 sección 1.6.3

**Observación:** Afirmación promocional del fabricante, no verificada de forma independiente.

#### concretec2018viguetas-08 · dato · s. p. (hoja 4) (PDF p. 4)

> El acero de alta resistencia utilizando como armadura de la vigueta Concretec, proporciona a la losa una resistencia superior a tres veces respecto al acero usado en hormigón armado In Situ

**Paráfrasis:** El acero de alta resistencia de la vigueta proporciona a la losa una resistencia superior a tres veces la del acero usado en hormigón armado vaciado en sitio.

**Uso sugerido:** Cap.1 sección 1.6.1

**Observación:** Afirmación promocional del fabricante, no verificada de forma independiente.

### Concretec (2016b) — Ficha técnica del complemento de plastoformo (ES-CC-1021)

**Referencia APA 7:** Concretec. (2016b). *Plastoform* [Ficha técnica ES-CC-1021, rev. 5.0]. https://www.concretec.com.bo

Clave BibLaTeX: `concretec2016plastoformo` · Archivo: `04_Bibliografia/05_Documentos_Tecnicos/Concretec_ES-CC-1021_2016_Ficha_Plastoformo_Complemento.pdf`

**Verificación:**

- Verificado en la cabecera: «Código: ES-CC-1021 Rev.: 5.0 Fecha: 15/09/2016»; el título impreso es «Plastoform» (no «plastoformo»). Lleva la letra «b» porque comparte autor y año con la ficha de hormigón premezclado («Hormigón…» precede a «Plastoform» en el orden alfabético).
- La ficha trae la tabla completa de dimensiones de 42 complementos y 3 casetones (transcrita abajo), pero **no da consumos por m²**.
- Posibles erratas del fabricante: el código 103322 se rotula «20*43*100», pero sus columnas dicen a = 53 y d = 49 (lo esperable sería 43 y 39); el 103333 («15*52*130») tiene d = 46 en lugar de 48.
- No existe en la ficha un complemento de 20 × 50 × 100 cm, como el que pide la especificación técnica de la obra. Los de 20 cm de alto tienen anchos a de 42, 43, 52 y 53 cm, y largos de 100 o 130 cm.

#### concretec2016plastoformo-01 · definicion · s. p. (hoja 1) (PDF p. 1)

> El poliestireno expandido, también llamado plastoform, es un material plástico espumado, fabricado bajo un proceso de expansión con vapor de agua y tiene como características principales su ligereza, resistencia a la humedad y capacidad de absorción de impactos.

**Paráfrasis:** El poliestireno expandido (plastoform) es un plástico espumado que se fabrica por expansión con vapor de agua; es ligero, resiste la humedad y absorbe impactos.

**Uso sugerido:** Cap.1 sección 1.6.1

#### concretec2016plastoformo-02 · requisito_normativo · s. p. (hoja 1) (PDF p. 1)

> Nota: Las medidas pueden variar longitudinalmente ±2cm.; transversal ±1 cm. También se realizan cortes con medidas a pedido.

**Paráfrasis:** Las piezas de plastoform admiten tolerancias de ±2 cm en largo y ±1 cm en ancho, y pueden cortarse a medida.

**Uso sugerido:** Cap.1 sección 1.6.3 | Cap.2 (recepción de complementos)

*Complemento Plastoform: dimensiones [cm] y densidad [kg/m³] (hojas 1 y 2 de la ficha ES-CC-1021)*

| Código | Medidas | a | b | c | d | Densidad [kg/m³] |
|---|---|---|---|---|---|---|
| 103300 | 10*42*130 | 42 | 130 | 10 | 38 | 8-10 |
| 103301 | 10*42*100 | 42 | 100 | 10 | 38 | 8-10 |
| 103302 | 10*50*100 | 50 | 100 | 10 | 46 | 8-10 |
| 103303 | 10*50*130 | 50 | 130 | 10 | 46 | 8-10 |
| 103304 | 10*43*100 | 43 | 100 | 10 | 39 | 8-10 |
| 103305 | 10*51*100 | 51 | 100 | 10 | 47 | 8-10 |
| 103306 | 12*42*100 | 42 | 100 | 12 | 38 | 8-10 |
| 103307 | 12*42*130 | 42 | 130 | 12 | 38 | 8-10 |
| 103308 | 12*52*100 | 52 | 100 | 12 | 48 | 8-10 |
| 103309 | 12*52*130 | 52 | 130 | 12 | 48 | 8-10 |
| 103310 | 12*43*100 | 43 | 100 | 12 | 39 | 8-10 |
| 103311 | 12*53*100 | 53 | 100 | 12 | 49 | 8-10 |
| 103312 | 15*42*100 | 42 | 100 | 15 | 38 | 8-10 |
| 103313 | 15*43*100 | 43 | 100 | 15 | 39 | 8-10 |
| 103314 | 15*52*100 | 52 | 100 | 15 | 48 | 8-10 |
| 103315 | 15*53*100 | 53 | 100 | 15 | 49 | 8-10 |
| 103316 | 16*42*130 | 42 | 130 | 16 | 38 | 8-10 |
| 103317 | 16*52*130 | 52 | 130 | 16 | 48 | 8-10 |
| 103318 | 20*42*130 | 42 | 130 | 20 | 38 | 8-10 |
| 103319 | 20*42*100 | 42 | 100 | 20 | 38 | 8-10 |
| 103320 | 20*52*100 | 52 | 100 | 20 | 48 | 8-10 |
| 103321 | 20*52*130 | 52 | 130 | 20 | 48 | 8-10 |
| 103322 | 20*43*100 | 53 | 100 | 20 | 49 | 8-10 |
| 103323 | 20*53*100 | 53 | 100 | 20 | 49 | 8-10 |
| 103327 | 10*53*100 | 53 | 100 | 10 | 49 | 8-10 |
| 103329 | 12*50*130 | 50 | 130 | 12 | 46 | 8-10 |
| 103330 | 25*52*130 | 52 | 130 | 25 | 48 | 8-10 |
| 103332 | 15*42*130 | 42 | 130 | 15 | 38 | 8-10 |
| 103333 | 15*52*130 | 52 | 130 | 15 | 46 | 8-10 |
| 103334 | 10*43*130 | 43 | 130 | 10 | 39 | 8-10 |
| 103335 | 12*43*130 | 43 | 130 | 12 | 39 | 8-10 |
| 103336 | 12*53*130 | 53 | 130 | 12 | 49 | 8-10 |
| 103337 | 15*43*130 | 43 | 130 | 15 | 39 | 8-10 |
| 103338 | 15*53*130 | 53 | 130 | 15 | 49 | 8-10 |
| 103339 | 20*43*130 | 43 | 130 | 20 | 39 | 8-10 |
| 103340 | 20*53*130 | 53 | 130 | 20 | 49 | 8-10 |
| 103342 | 10*53*130 | 53 | 130 | 10 | 49 | 8-10 |
| 103345 | 12*63*130 | 63 | 130 | 12 | 59 | 8-10 |
| 103346 | 16*53*130 | 53 | 130 | 16 | 49 | 8-10 |
| 103357 | 15*48*130 | 48 | 130 | 15 | 44 | 8-10 |
| 103358 | 15*63*130 | 63 | 130 | 15 | 59 | 8-10 |
| 103360 | 30*53*130 | 53 | 130 | 30 | 49 | 8-10 |

Nota: Transcripción automática de la capa de texto, cotejada con la imagen de la página. «Medidas» = c × a × b (alto × ancho × largo), excepto el código 103322, rotulado 20*43*100 con a = 53 (posible errata). Tolerancias: ±2 cm en sentido longitudinal y ±1 cm en sentido transversal.

#### concretec2016plastoformo-03 · dato · s. p. (hoja 1, tabla «Complemento Plastoform») (PDF p. 1)

> 103318 20*42*130 42 130 20 38 8-10 103319 20*42*100 42 100 20 38 8-10 103320 20*52*100 52 100 20 48 8-10

**Paráfrasis:** Los complementos de 20 cm de alto de la hoja 1 son: 20 × 42 × 130 cm (a = 42, d = 38), 20 × 42 × 100 cm (a = 42, d = 38) y 20 × 52 × 100 cm (a = 52, d = 48), todos con densidad de 8 a 10 kg/m³.

**Uso sugerido:** Cap.1 sección 1.6.3

**Observación:** Ninguno coincide con el complemento de 100 × 50 × 20 cm de la especificación técnica de la obra ni con el «Plastobloq» de 20 × 100 × 44 cm del certificado de UNICON.

#### concretec2016plastoformo-04 · dato · s. p. (hoja 2) (PDF p. 2)

> 103322 20*43*100 53 100 20 49 8-10 103323 20*53*100 53 100 20 49 8-10

**Paráfrasis:** Los códigos 103322 y 103323 corresponden a complementos de 20 cm de alto y 100 cm de largo; el primero se rotula 20 × 43 × 100, pero sus columnas indican a = 53 y d = 49, igual que el segundo.

**Uso sugerido:** Cap.1 sección 1.6.3

**Observación:** Posible errata del fabricante en el código 103322.

*Casetones de Plastoform (hoja 2)*

| Código | Medidas | a | b | c | d | Densidad [kg/m³] |
|---|---|---|---|---|---|---|
| 103400 | D = 10 | Variable | Variable | Variable | - | 8-10 |
| 103401 | D = 14 | Variable | Variable | Variable | - | 12-15 |
| 103402 | D = 20 | Variable | Variable | Variable | - | 18-21 |

#### concretec2016plastoformo-05 · dato · s. p. (hoja 3, «Usos y aplicaciones») (PDF p. 3)

> Utilizando principalmente como complemento en losas alivianadas, reduciendo significativamente el peso de la losa, permitiendo optimizar las secciones de la estructura.

**Paráfrasis:** El plastoform se usa sobre todo como complemento de losas alivianadas, porque reduce el peso de la losa y permite optimizar las secciones de la estructura.

**Uso sugerido:** Cap.1 sección 1.6.1

#### concretec2016plastoformo-06 · requisito_normativo · s. p. (hoja 3, «Recomendaciones de colocado») (PDF p. 3)

> Se recomienda que las viguetas se encuentren apuntaladas en el momento de colocarse el complemento de plastoform, para evitar deformaciones en la losa y hasta posibles caídas de la misma por la circulación del personal que coloca los mismos.

**Paráfrasis:** Las viguetas deben estar apuntaladas al colocar los complementos, para evitar deformaciones de la losa e incluso su caída por el tránsito del personal.

**Uso sugerido:** Cap.1 sección 1.6.2 | Cap.2 (PPI de colocación)

#### concretec2016plastoformo-07 · requisito_normativo · s. p. (hoja 3, «Recomendaciones de colocado») (PDF p. 3)

> Se recomienda no pisar las piezas una vez colocadas en la losa, estas pueden sufrir deformaciones que provoquen pérdida de rendimiento por m2 en el hormigón de la carpeta de compresión.

**Paráfrasis:** No deben pisarse los complementos ya colocados: sus deformaciones provocan pérdida de rendimiento por m² del hormigón de la carpeta de compresión, es decir, mayor consumo de hormigón.

**Uso sugerido:** Cap.1 sección 1.6.4 | Cap.2 (control del hormigón de la carpeta)

**Observación:** Vincula de forma directa la manipulación del complemento con el desperdicio de hormigón de la losa.

### Concretec (2016a) — Ficha técnica del hormigón premezclado (ES-CC-1018)

**Referencia APA 7:** Concretec. (2016a). *Hormigón premezclado* [Ficha técnica ES-CC-1018, rev. 4.0]. https://www.concretec.com.bo

Clave BibLaTeX: `concretec2016hormigon` · Archivo: `04_Bibliografia/05_Documentos_Tecnicos/Concretec_ES-CC-1018_2016_Ficha_Hormigon_Premezclado.pdf`

**Verificación:**

- Verificado en la cabecera: «Código: ES-CC-1018 Rev.: 4.0 Fecha: 15/09/2016».
- La ficha **no da consumos por m² de losa** ni dosificaciones por m³: trae los tipos de hormigón (H-10 a H-40), los modos de entrega con tamaño máximo y asentamiento, la materia prima con sus normas y los usos recomendados.
- Las normas citadas en la ficha están desactualizadas (NB 598-91, NB 596-94, NB 011-12, NB 637-94); compárese con las vigentes en Bibliografia_Recomendada.md (NB 011:2025, NB 596:2016, NB 637:2018).

#### concretec2016hormigon-01 · definicion · s. p. (hoja 1) (PDF p. 1)

> El Hormigón es el producto resultante de la mezcla de cemento, agregado fino (arena), agregado grueso (ripio), agua y en ocasiones aditivos de diferentes propiedades.

**Paráfrasis:** El hormigón es el producto de la mezcla de cemento, agregado fino (arena), agregado grueso (ripio), agua y, en ocasiones, aditivos.

**Uso sugerido:** Cap.1 sección 1.10

#### concretec2016hormigon-02 · dato · s. p. (hoja 1) (PDF p. 1)

> En el caso del hormigón premezclado a diferencia de los hormigones preparados in situ, todas las materias primas han sido sometidas a un estricto control de calidad, garantizando de esta manera su óptimo rendimiento y resistencia.

**Paráfrasis:** A diferencia del hormigón preparado en obra, en el premezclado todas las materias primas pasan por un control de calidad estricto, lo que garantiza su rendimiento y resistencia.

**Uso sugerido:** Cap.1 sección 1.6.2 | Cap.3 Discusión

**Observación:** Afirmación promocional del fabricante, no verificada de forma independiente.

#### concretec2016hormigon-03 · requisito_normativo · s. p. (hoja 1, «Modo de entrega») (PDF p. 1)

> Nota: Tolerancia de ± 2 en el asentamiento. En obra se pueden conseguir asentamientos mayores de acuerdo a requerimiento, con el uso de aditivos.

**Paráfrasis:** El asentamiento de entrega tiene una tolerancia de ±2 cm; en obra pueden lograrse asentamientos mayores con aditivos.

**Uso sugerido:** Cap.2 (recepción del hormigón)

*Modo de entrega del hormigón premezclado (hoja 1 de la ficha ES-CC-1018)*

| Modo de entrega | Tipo de hormigón | TM del agregado [mm] | Asentamiento [cm] |
|---|---|---|---|
| Bombeado (HB) | 10, 15, 18, 21, 23, 25, 28, 30, 35, 40 | 20 | 8-10 |
| Bombeado (HB) | ídem | 25 | 8-10 |
| Descarga directa (H) | 10, 15, 18, 21, 23, 25, 28, 30, 35, 40 | 20 | 6 |
| Descarga directa (H) | ídem | 25 | 6 |
| Descarga directa (H) | ídem | 40 | 6 |
| Descarga directa (H) | ídem | 50 | 6 |

Nota: Tolerancia de ±2 en el asentamiento. El bombeo solo es posible con agregado de 20 mm (¾") y 25 mm (1").

#### concretec2016hormigon-04 · dato · s. p. (hoja 1, «Materia prima») (PDF p. 1)

> Cemento IP – 40 : IP - 30 Fancesa NB 011 – 12

**Paráfrasis:** El fabricante emplea cemento IP-40 o IP-30 de Fancesa conforme a la NB 011-12, y agregados y agua conforme a las NB 596, 598 y 637.

**Uso sugerido:** Cap.1 sección 1.7.2

**Observación:** Las ediciones de las normas citadas están desactualizadas respecto de las vigentes.

*Materia prima del hormigón premezclado (hoja 1)*

| Insumo | Tipo | Proveedor | Norma de requisito |
|---|---|---|---|
| Agregado fino | Arenilla # 4 | Planta de Agregados Concretec | NB 598 – 91 |
| Agregado grueso | ¾" - 1" - 1½" | Planta de Agregados Concretec | NB 596 – 94 |
| Cemento | IP – 40 : IP - 30 | Fancesa | NB 011 – 12 |
| Agua | - | Pozo Profundo Propio | NB 637 – 94 |

#### concretec2016hormigon-05 · dato · s. p. (hoja 2) (PDF p. 2)

> La dosificación del hormigón se realiza por peso, obtenido mediante procesos altamente tecnificados, logrando cantidades exactas y controladas.

**Paráfrasis:** La dosificación del hormigón premezclado se hace por peso, con procesos tecnificados que dan cantidades exactas y controladas.

**Uso sugerido:** Cap.2 (dosificación) | Cap.3 Discusión

#### concretec2016hormigon-06 · dato · s. p. (hoja 2, «Usos recomendados») (PDF p. 2)

> Nota: Esta tabla es referencial, el requerimiento del cliente y/o el cálculo estructural de la obra será lo que determine el tipo y el uso del Hormigón Premezclado

**Paráfrasis:** La tabla de usos es referencial: el tipo de hormigón lo fijan el requerimiento del cliente y el cálculo estructural. La ficha recomienda H-18 a H-21 para losas y H-25 para estructuras y fundaciones especiales.

**Uso sugerido:** Cap.1 sección 1.6.1

*Usos recomendados por tipo de hormigón (hoja 2)*

| Tipo de hormigón | Usos recomendados |
|---|---|
| 100 Kg/cm2 (H-10) | Hormigón pobre y nivelación de terrenos. |
| 150 Kg/cm2 (H-15) | Hormigón pobre, nivelación de terrenos, piso y contra-piso. |
| 180 Kg/cm2 (H-18) | Elementos estructurales, muros de contención, pisos, losas, vigas y columnas. |
| 210 Kg/cm2 (H-21) | Vigas, losas, zapatas, pavimento rígido, canales y muros de contención |
| 230 Kg/cm2 (H-23) | Pavimento con armaduras, estacionamiento, columnas. |
| 250 Kg/cm2 (H-25) | Puentes, columnas, estructuras y fundaciones especiales. |
| 280 Kg/cm2 (H-28) | Puentes, estructuras especiales y fundaciones especiales. |
| 300 Kg/cm2 (H-30) | Puentes, estructuras especiales y fundaciones especiales. |
| 350 Kg/cm2 (H-35) | Puentes, estructuras especiales y fundaciones especiales. |
| 400 Kg/cm2 (H-40) | Puentes, estructuras especiales y fundaciones especiales. |

Nota: Tabla referencial: el tipo de hormigón lo determinan el requerimiento del cliente y el cálculo estructural.

#### concretec2016hormigon-07 · requisito_normativo · s. p. (hoja 2) (PDF p. 2)

> los hormigones de CONCRETEC cuentan con certificación de uso de sello de conformidad con norma NB 604 que garantizan la calidad del hormigón adquirido.

**Paráfrasis:** El hormigón cuenta con sello de conformidad con la NB 604, y el fabricante con un SGC certificado con ISO 9001:2008 avalado por IBNORCA; son evidencias de calidad que pueden exigirse a un proveedor de hormigón.

**Uso sugerido:** Cap.1 sección 1.7.2 | Cap.2 (evaluación de proveedores)

#### concretec2016hormigon-08 · dato · s. p. (hoja 3) (PDF p. 3)

> Nuestros laboratorios especializados para el control de calidad en obra y en Planta, realizan ensayos para el control de resistencias del hormigón a la compresión simple a 28 días, verificando de esta manera la calidad y el buen comportamiento del producto.

**Paráfrasis:** El fabricante ensaya la resistencia a compresión simple a 28 días, en obra y en planta, para verificar la calidad del producto.

**Uso sugerido:** Cap.2 (ensayos de control)

#### concretec2016hormigon-09 · dato · s. p. (hoja 4, «Equipos») (PDF p. 4)

> Camiones mixer de 8 m3 de capacidad. Plantas dosificadoras y mezcladoras en todo el país. Bombas móviles.

**Paráfrasis:** El fabricante dispone de camiones mezcladores de 8 m³, plantas dosificadoras en todo el país y bombas móviles.

**Uso sugerido:** Cap.2 (logística del hormigonado)

**Observación:** En la misma hoja, el camión bomba tiene una capacidad aproximada de 160 m³/h.

#### concretec2016hormigon-10 · dato · s. p. (hoja 5, «Ventajas de uso») (PDF p. 5)

> Ahorro de tiempo de ejecución de obra.  Ahorro del 50% en mano de obra.

**Paráfrasis:** Entre las ventajas declaradas del hormigón premezclado figuran el ahorro de tiempo de ejecución y un ahorro del 50 % en mano de obra.

**Uso sugerido:** Cap.3 Discusión

**Observación:** Afirmación promocional del fabricante, no verificada de forma independiente.

### INE (2026) — Boletín Sectorial de Construcción N.º 09

**Referencia APA 7:** Instituto Nacional de Estadística. (2026, 30 de septiembre). *Producción de cemento alcanza 1,84 millones de toneladas a julio de 2026* (Boletín Sectorial de Construcción N.º 09).

Clave BibLaTeX: `ine2026boletin` · Archivo: `04_Bibliografia/05_Documentos_Tecnicos/INE_BSC-09_2026_Boletin_Sectorial_Construccion.pdf`

**Verificación:**

- Verificado en el PDF: «BOLETÍN SECTORIAL DE CONSTRUCCIÓN Nº 09, 30/09/26», titular «Producción de cemento alcanza 1,84 millones de toneladas a julio de 2026» y fuente «Instituto Nacional de Estadística». Son 2 páginas sin folio.
- El boletín **no contiene precios de materiales**: trae la producción y venta de cemento, los permisos de construcción y la ocupación. Las variaciones de precios de Potosí (cemento +74,1 %, fierro +65,7 %, vigueta con plastoformo +61,6 %) provienen del XLSX citado como `ine2026precios`, que no está en el repositorio; no pudieron verificarse en este grupo.
- El PDF no imprime la URL de descarga.

#### ine2026boletin-01 · dato · s. p. (secc. «Producción y venta de cemento») (PDF p. 1)

> A julio de 2026, la producción de cemento alcanzó 1,84 millones de toneladas métricas (TM), registrando una disminución de 19,6% respecto al mismo período de 2025, cuando llegó a 2,29 millones de TM.

**Paráfrasis:** A julio de 2026, la producción acumulada de cemento en Bolivia fue de 1,84 millones de toneladas, un 19,6 % menos que en el mismo periodo de 2025 (2,29 millones).

**Uso sugerido:** Introducción-Situación problemática

#### ine2026boletin-02 · dato · s. p. (secc. «Producción y venta de cemento») (PDF p. 1)

> Por su parte, las ventas de cemento alcanzaron un volumen de 1,76 millones de TM, marcando una disminución de 21,9% en comparación con el mismo período del año anterior, cuando alcanzaron 2,25 millones TM.

**Paráfrasis:** Las ventas de cemento llegaron a 1,76 millones de toneladas a julio de 2026, un 21,9 % menos que en el mismo periodo del año anterior (2,25 millones).

**Uso sugerido:** Introducción-Situación problemática

#### ine2026boletin-03 · dato · s. p. (secc. «Permisos de construcción») (PDF p. 2)

> En julio de 2026, se registraron 67 mil metros cuadrados de superficie autorizada para construcciones residenciales y no residenciales en ciudades capitales y principales conurbaciones del país. Esta superficie fue menor a la registrada el mes anterior, cuando se alcanzaron 100 mil metros cuadrados.

**Paráfrasis:** En julio de 2026 se autorizaron 67 mil m² de construcción en las ciudades capitales y principales conurbaciones, frente a 100 mil m² en junio.

**Uso sugerido:** Introducción-Situación problemática

#### ine2026boletin-04 · dato · s. p. (secc. «Ocupación en la actividad económica de la construcción») (PDF p. 2)

> en junio de 2026, el número de personas ocupadas en actividades relacionadas con la construcción en el área urbana, alcanzó a 358 mil, cifra mayor a la registrada en el mismo período del año 2025, cuando se contabilizaron 353 mil personas ocupadas.

**Paráfrasis:** En junio de 2026, la construcción ocupaba a 358 mil personas en el área urbana, frente a 353 mil en junio de 2025.

**Uso sugerido:** Introducción-Situación problemática

### Koskela (1992) — Application of the new production philosophy to construction

**Referencia APA 7:** Koskela, L. (1992). *Application of the new production philosophy to construction* (Technical Report No. 72). Center for Integrated Facility Engineering, Stanford University. https://purl.stanford.edu/kh328xt3298

Clave BibLaTeX: `koskela1992` · Archivo: `04_Bibliografia/05_Documentos_Tecnicos/Koskela_1992_Application_New_Production_Philosophy_Construction.pdf`

**Verificación:**

- Verificado en la portada escaneada: «CIFE Center for Integrated Facility Engineering — Application of the new production philosophy to construction — by Lauri Koskela — Technical Report Number 72 — September, 1992 — Stanford University». La hoja de resumen dice «August, 1992»; se usa la fecha de la portada.
- **Sin capa de texto:** se aplicó `ocrmypdf --skip-text -l eng` (con Python 3.12, porque pikepdf solo está compilado para esa versión). La copia OCR quedó en el directorio de trabajo: `.../scratchpad/grupo_art_tec/ocr/Koskela_1992_OCR.pdf`. Las fichas llevan `capa_de_texto: false`.
- Folios: el desfase entre la página del PDF y el folio impreso varía porque hay hojas sin folio intercaladas (PDF 12 = p. 1; PDF 19-38 = pp. 10-29; PDF 40-60 = pp. 30-50; PDF 62 = p. 51; PDF 80 = p. 68). Por eso se usó el folio leído en cada página. Las pp. 19 y 20 están invertidas en el escaneo (PDF 28 = p. 20 y PDF 29 = p. 19).
- La URL proviene de Bibliografia_Recomendada.md (no impresa en el PDF).

#### koskela1992-01 · definicion · p. 14 (PDF p. 23)

> the output of each conversion is usually variable, to such an extent that a share of the output does not fulfill the implicit or explicit specification for that conversion and has to be scrapped or reworked

**Paráfrasis:** Desde el punto de vista de la calidad, el resultado de cada conversión es variable, de modo que una parte no cumple la especificación y debe desecharse o rehacerse.

**Uso sugerido:** Cap.1 sección 1.4.2

**Observación:** Texto obtenido por OCR (ocrmypdf 15.2 con Tesseract, idioma eng) porque el PDF escaneado no tiene capa de texto; la verificación con search_for se hizo sobre la copia OCR del directorio de trabajo.

#### koskela1992-02 · definicion · p. 15 (PDF p. 24)

> Production is a flow of material and/or information from raw material to the end product (Figure 2). In this flow, the material is processed (converted), it is inspected, it is waiting or it is moving.

**Paráfrasis:** La producción es un flujo de material o información desde la materia prima hasta el producto final; en ese flujo el material se procesa, se inspecciona, espera o se traslada.

**Uso sugerido:** Cap.1 sección 1.5.3

**Observación:** Texto obtenido por OCR (ocrmypdf 15.2 con Tesseract, idioma eng) porque el PDF escaneado no tiene capa de texto; la verificación con search_for se hizo sobre la copia OCR del directorio de trabajo.

#### koskela1992-03 · definicion · p. 15 (PDF p. 24)

> Flow processes can be characterized by time, cost and value. Value refers to the fulfillment of customer requirements. In most cases, only processing activities are value-adding activities.

**Paráfrasis:** Los procesos de flujo se caracterizan por su tiempo, costo y valor; el valor es el cumplimiento de los requisitos del cliente, y en general solo las actividades de procesamiento agregan valor.

**Uso sugerido:** Cap.1 sección 1.2.1 | 1.10

**Observación:** Texto obtenido por OCR (ocrmypdf 15.2 con Tesseract, idioma eng) porque el PDF escaneado no tiene capa de texto; la verificación con search_for se hizo sobre la copia OCR del directorio de trabajo.

#### koskela1992-04 · metodo · p. 16 (PDF p. 25)

> While all activities expend cost and consume time, only conversion activities add value to the material or piece of information being transformed to a product.

**Paráfrasis:** Todas las actividades consumen costo y tiempo, pero solo las de conversión agregan valor; por ello, las actividades de flujo deben reducirse o eliminarse y las de conversión hacerse más eficientes.

**Uso sugerido:** Cap.1 sección 1.5.3

**Observación:** Texto obtenido por OCR (ocrmypdf 15.2 con Tesseract, idioma eng) porque el PDF escaneado no tiene capa de texto; la verificación con search_for se hizo sobre la copia OCR del directorio de trabajo.

#### koskela1992-05 · metodo · p. 16 (PDF p. 25)

> Reduce the share of non value-adding activities. Increase output value through systematic consideration of customer requirements. Reduce variability. Reduce the cycle time. Simplify by minimizing the number of steps, parts and linkages.

**Paráfrasis:** Koskela propone once principios para diseñar y mejorar los procesos de flujo: reducir las actividades que no agregan valor; aumentar el valor del producto según los requisitos del cliente; reducir la variabilidad; reducir el tiempo de ciclo; simplificar; aumentar la flexibilidad; aumentar la transparencia; enfocar el control en el proceso completo; incorporar la mejora continua; equilibrar las mejoras de flujo y de conversión; y hacer benchmarking.

**Uso sugerido:** Cap.1 sección 1.5.3

**Observación:** Texto obtenido por OCR (ocrmypdf 15.2 con Tesseract, idioma eng) porque el PDF escaneado no tiene capa de texto; la verificación con search_for se hizo sobre la copia OCR del directorio de trabajo.

*Principios para el diseño y la mejora de los procesos de flujo (Koskela, 1992, p. 16)*

| N.º | Principio |
|---|---|
| 1 | Reduce the share of non value-adding activities |
| 2 | Increase output value through systematic consideration of customer requirements |
| 3 | Reduce variability |
| 4 | Reduce the cycle time |
| 5 | Simplify by minimizing the number of steps, parts and linkages |
| 6 | Increase output flexibility |
| 7 | Increase process transparency |
| 8 | Focus control on the complete process |
| 9 | Build continuous improvement into the process |
| 10 | Balance flow improvement with conversion improvement |
| 11 | Benchmark |

Nota: Lista transcrita del OCR de la p. 16; la numeración del escaneo quedó ilegible en el OCR y se repuso según el orden.

#### koskela1992-06 · definicion · p. 17 (PDF p. 26)

> Value-adding activity: Activity that converts material and/or information towards that which is required by the customer. Non value-adding activity (also called waste): Activity that takes time, resources or space but does not add value.

**Paráfrasis:** La actividad que agrega valor convierte material o información hacia lo que requiere el cliente; la que no agrega valor, también llamada desperdicio, consume tiempo, recursos o espacio sin agregar valor.

**Uso sugerido:** Cap.1 sección 1.5.1 | 1.10

**Observación:** Texto obtenido por OCR (ocrmypdf 15.2 con Tesseract, idioma eng) porque el PDF escaneado no tiene capa de texto; la verificación con search_for se hizo sobre la copia OCR del directorio de trabajo.

#### koskela1992-07 · dato · p. 18 (PDF p. 27)

> Experience shows that non value-adding activities dominate most processes; usually only 3 to 20 % of steps add value (Ciampa 1991), and their share of the total cycle time is negligible, from 0.5 to 5 % (Stalk & Hout 1990).

**Paráfrasis:** Las actividades que no agregan valor dominan la mayoría de los procesos: solo entre el 3 % y el 20 % de los pasos agregan valor, y su participación en el tiempo de ciclo es de apenas 0,5 % a 5 %.

**Uso sugerido:** Cap.1 sección 1.5.1

**Observación:** Texto obtenido por OCR (ocrmypdf 15.2 con Tesseract, idioma eng) porque el PDF escaneado no tiene capa de texto; la verificación con search_for se hizo sobre la copia OCR del directorio de trabajo. Cita secundaria: el dato pertenece a Ciampa (1991) y Stalk y Hout (1990); citar como hallazgo reportado por el autor, no como fuente primaria.

#### koskela1992-08 · dato · p. 35 (PDF p. 45)

> In numerous studies from different countries, the cost of poor quality (non conformance), as measured on site, has turned out to be 10 - 20 % of total project costs (Cnudde 1991).

**Paráfrasis:** En numerosos estudios de distintos países, el costo de la mala calidad (no conformidad) medido en obra fue del 10 % al 20 % del costo total del proyecto.

**Uso sugerido:** Introducción-Situación problemática | Cap.1 sección 1.4.2

**Observación:** Texto obtenido por OCR (ocrmypdf 15.2 con Tesseract, idioma eng) porque el PDF escaneado no tiene capa de texto; la verificación con search_for se hizo sobre la copia OCR del directorio de trabajo. Cita secundaria: el dato pertenece a Cnudde (1991); citar como hallazgo reportado por el autor, no como fuente primaria.

#### koskela1992-09 · dato · p. 35 (PDF p. 45)

> According to a Swedish study, excess consumption of materials on site (scrap, wastage and surplus) is on average 10 %, varying in the range of 5 - 30 % for different materials

**Paráfrasis:** El consumo excesivo de materiales en obra (recortes, desperdicio y sobrantes) es en promedio del 10 % y varía entre el 5 % y el 30 % según el material.

**Uso sugerido:** Introducción-Situación problemática | Cap.1 sección 1.5.2

**Observación:** Texto obtenido por OCR (ocrmypdf 15.2 con Tesseract, idioma eng) porque el PDF escaneado no tiene capa de texto; la verificación con search_for se hizo sobre la copia OCR del directorio de trabajo. Cita secundaria: el dato pertenece a un estudio sueco (Bättre materialhantering på bygget, 1990); citar como hallazgo reportado por el autor, no como fuente primaria.

#### koskela1992-10 · dato · p. 35 (PDF p. 45)

> It has been estimated that 10 - 12 % savings in labor costs could be produced by materials-management systems (Bell & Stukhart 1986). Further, a reduction of the bulk material surplus from 5 - 10 % to 1 - 3 % would result.

**Paráfrasis:** Los sistemas de gestión de materiales podrían ahorrar entre el 10 % y el 12 % del costo de mano de obra y reducir los sobrantes de materiales a granel de 5-10 % a 1-3 %.

**Uso sugerido:** Cap.1 sección 1.5.2 | Cap.2 (gestión de materiales)

**Observación:** Texto obtenido por OCR (ocrmypdf 15.2 con Tesseract, idioma eng) porque el PDF escaneado no tiene capa de texto; la verificación con search_for se hizo sobre la copia OCR del directorio de trabajo. Cita secundaria: el dato pertenece a Bell y Stukhart (1986); citar como hallazgo reportado por el autor, no como fuente primaria.

### Pons Achell (2014) — Introducción a Lean Construction

**Referencia APA 7:** Pons Achell, J. F. (2014). *Introducción a Lean Construction*. Fundación Laboral de la Construcción.

Clave BibLaTeX: `pons2014` · Archivo: `04_Bibliografia/05_Documentos_Tecnicos/Pons_2014_Introduccion_Lean_Construction.pdf`

**Verificación:**

- Verificado en la página de créditos: «1ª edición: marzo 2014 — © Juan Felipe Pons Achell — Edita: Fundación Laboral de la Construcción, C/ Rivas, 25 - 28052 Madrid — Depósito Legal: M-6849-2014». Director del proyecto: Emilio Lezana Pérez; prólogo de Luis Fernando Alarcón.
- Es un libro (nivel 3 de la jerarquía del docente), aunque esté en la carpeta de documentos técnicos. Folio impreso = página del PDF − 1.
- La capa de texto contiene guiones blandos (U+00AD) al final de línea; se eliminaron al normalizar, igual que hace `search_for`.

#### pons2014-01 · hallazgo · p. 11 (PDF p. 12)

> Control de calidad ineficaz basado en métodos estadísticos que están lejos de garantizar el cien por cien de la calidad.

**Paráfrasis:** Uno de los problemas del modelo tradicional de gestión de proyectos es un control de calidad ineficaz, basado en métodos estadísticos que no garantizan la calidad total.

**Uso sugerido:** Cap.1 sección 1.2.2

#### pons2014-02 · dato · p. 12 (PDF p. 13)

> hasta el 57% del tiempo, el esfuerzo y el material de la inversión en proyectos de construcción no añade valor al producto final, mientras que en comparación en la industria de la fabricación la cifra es solo del 26%.

**Paráfrasis:** Hasta el 57 % del tiempo, el esfuerzo y el material invertidos en proyectos de construcción no agrega valor al producto final, frente al 26 % en la industria manufacturera.

**Uso sugerido:** Introducción-Situación problemática

**Observación:** Cita secundaria: el dato pertenece a un estudio de 2004 del Construction Industry Institute y el Lean Construction Institute; citar como hallazgo reportado por el autor, no como fuente primaria.

#### pons2014-03 · definicion · p. 18 (PDF p. 19)

> Muda es una palara japonesa que significa desperdicio, en el sentido de toda aquella actividad humana que absorbe recursos, pero no crea valor

**Paráfrasis:** Muda es el término japonés para desperdicio: toda actividad humana que absorbe recursos pero no crea valor.

**Uso sugerido:** Cap.1 sección 1.5.1 | 1.10

**Observación:** El original dice «palara» (errata del libro); el pasaje se apoya en Womack y Jones (1996).

#### pons2014-04 · metodo · p. 19 (PDF p. 20)

> Taiichi Ohno clasificó los 7 desperdicios que causaban la mayor parte de las interrupciones del flujo dentro de la cadena o flujo de valor en la planta de producción que él mismo dirigía.

**Paráfrasis:** Ohno clasificó los siete desperdicios que causan la mayoría de las interrupciones del flujo de valor; Pons los adapta a la construcción y agrega un octavo, el talento desaprovechado (Liker).

**Uso sugerido:** Cap.1 sección 1.5.1

*Figura 5. Los 8 desperdicios de la construcción (síntesis de la tabla de Pons, p. 19)*

| Desperdicio | Ejemplos de la tabla |
|---|---|
| Sobreproducción | Cantidades mayores o más tempranas que las requeridas; planos no esenciales; equipo más sofisticado de lo necesario; más calidad que la esperada |
| Esperas o tiempo de inactividad | Falta de información, planos, materiales o equipos; espera de aprobaciones o resultados de laboratorio; repetición del trabajo por cambios de diseño |
| Transporte innecesario | Movimiento interno de recursos por mala distribución y falta de planificación; posible pérdida de material en el transporte |
| Sobreprocesamiento | Procesos adicionales con uso excesivo de materia prima, equipos o energía; inspecciones excesivas o duplicadas |
| Exceso de inventario | Pérdidas de material por deterioro, obsolescencia, malas condiciones de acopio, robo y vandalismo; costos financieros |
| Movimientos innecesarios | Movimientos ineficientes de los trabajadores por equipo inadecuado o falta de estandarización |
| Defectos de calidad | Errores de diseño, mediciones y planos; métodos incorrectos; mano de obra poco cualificada; repetición del trabajo |
| Talento | Ideas y oportunidades de mejora perdidas por no motivar ni escuchar al personal |

Nota: Síntesis de las descripciones de la tabla original; los textos literales relevantes están en las fichas pons2014-05 y pons2014-06.

#### pons2014-05 · definicion · p. 19 (PDF p. 20)

> Se refiere a los inventarios excesivos, innecesarios o antes de tiempo que conducen a pérdidas de material (por deterioro, obsolescencias, pérdidas debidas a condiciones inadecuadas de stock en la obra, robo y vandalismo)

**Paráfrasis:** El exceso de inventario, es decir, los acopios excesivos, innecesarios o anticipados, provoca pérdidas de material por deterioro, obsolescencia, malas condiciones de almacenamiento en obra, robo y vandalismo.

**Uso sugerido:** Cap.1 sección 1.5.1 | Cap.2 (gestión del acopio)

#### pons2014-06 · definicion · p. 19 (PDF p. 20)

> Errores en el diseño, mediciones y planos; desajuste entre planos de diseño y planos de estructura o instalaciones, uso de métodos de trabajo incorrectos, mano de obra poco cualificada. Las dos consecuencias principales de la mala calidad son: la repetición del trabajo y la insatisfacción del cliente.

**Paráfrasis:** Los defectos de calidad (errores de diseño, mediciones y planos, incompatibilidades entre planos, métodos de trabajo incorrectos y mano de obra poco cualificada) tienen dos consecuencias principales: la repetición del trabajo y la insatisfacción del cliente.

**Uso sugerido:** Cap.1 sección 1.4.2 | 1.5.1

#### pons2014-07 · hallazgo · p. 20 (PDF p. 21)

> Porque no medimos ni cuantificamos el desperdicio y por lo tanto no somos conscientes del dinero que nos cuesta la improductividad.

**Paráfrasis:** Una razón por la que el desperdicio es difícil de eliminar es que no se mide ni se cuantifica, y por eso no se conoce cuánto dinero cuesta la improductividad.

**Uso sugerido:** Introducción-Situación problemática | Cap.2

#### pons2014-08 · metodo · p. 24 (PDF p. 25)

> 1) si decidimos aumentar el precio de venta, estamos haciendo responsable al cliente de nuestros costes improductivos (D) que surgen durante la fase de ejecución; 2) si mantenemos el precio, entonces baja el margen de beneficio y hacemos peligrar la estabilidad del negocio.

**Paráfrasis:** Con el principio de costos tradicional (precio = costo + beneficio), si los costos de producción suben de forma inesperada hay dos salidas: trasladar al cliente los costos improductivos, subiendo el precio, o mantener el precio y reducir el margen, poniendo en riesgo el negocio.

**Uso sugerido:** Cap.3 Discusión (contrato a precio fijo)

**Observación:** Aplicable al contrato público a precio unitario fijo de la obra: el desperdicio reduce el margen del contratista.

#### pons2014-09 · definicion · p. 26 (PDF p. 27)

> La aplicación de los principios y herramientas del sistema Lean a lo largo de todo el ciclo de vida de un proyecto de construcción se conoce como Lean Construction o construcción sin pérdidas.

**Paráfrasis:** Lean Construction, o construcción sin pérdidas, es la aplicación de los principios y herramientas Lean a todo el ciclo de vida de un proyecto de construcción.

**Uso sugerido:** Cap.1 sección 1.5.3 | 1.10

#### pons2014-10 · dato · p. 56 (PDF p. 57)

> Los proyectos con LPS han demostrado una fiabilidad de planificación del 85%, que se compara con los proyectos tradicionales, donde es de alrededor del 50%.

**Paráfrasis:** Los proyectos que usan el Last Planner System alcanzan una fiabilidad de planificación del 85 %, frente a cerca del 50 % en los proyectos tradicionales.

**Uso sugerido:** Cap.2 (planificación) | Cap.3 Discusión

**Observación:** El pasaje no indica la fuente del dato.

### Pliego de especificaciones técnicas de hormigón armado según la NB 1225001 (archivo «UCB-SCZ», 2025)

**Referencia APA 7:** Fernando Aragón Ingeniería Estructural. (2025). *Pliego de especificaciones técnicas generales: Hormigón armado. Proyecto: Ampliación del bloque de simulación de medicina y laboratorios de ingeniería y arquitectura* [Especificaciones técnicas].

Clave BibLaTeX: `ucb2025et` · Archivo: `04_Bibliografia/05_Documentos_Tecnicos/UCB-SCZ_ET-HA_2025_Especificaciones_Hormigon_Armado_NB1225001.pdf`

**Verificación:**

- **Atribución no verificada:** el PDF no menciona a la Universidad Católica Boliviana ni a Santa Cruz. La única marca de autoría es el logotipo «Fernando Aragón — Ingeniería Estructural» (imagen de la portada y marca de agua). El nombre del proyecto es «Ampliación del bloque de simulación de medicina y laboratorios de ingeniería y arquitectura». La atribución «UCB-SCZ» del nombre del archivo y de Bibliografia_Recomendada.md debe confirmarse con la fuente de descarga.
- El documento no imprime fecha; 2025 se toma de los metadatos del PDF (creado el 10/09/2025). Si no se confirma con la fuente, APA admitiría «(s. f.)».
- Tiene 19 páginas con folio impreso igual a la página del PDF. No trae URL.

#### ucb2025et-01 · requisito_normativo · p. 2 (PDF p. 2)

> Ante cualquier duda por omisión en el pliego o por causa de desacuerdo en la interpretación del pliego, prevalecerá lo establecido en el siguiente orden: a) Norma NB 1225001 b) Norma Americana ASTM.

**Paráfrasis:** Ante omisiones o desacuerdos en la interpretación del pliego, prevalece primero la NB 1225001 y luego las normas ASTM.

**Uso sugerido:** Cap.1 sección 1.7.2 | Cap.3 Discusión (comparación con la ET de la UATF)

**Observación:** Contrasta con la especificación técnica de la UATF, que cita la CBH-87 y normas bolivianas antiguas.

#### ucb2025et-02 · requisito_normativo · p. 8 (PDF p. 8)

> Ningún elemento estructural podrá vaciarse sin la autorización estricta de la Supervisión, para ello el contratista, deberá comunicar con al menos 24 horas de anticipación, al detalle del vaciado a efectuarse.

**Paráfrasis:** Ningún elemento estructural puede vaciarse sin autorización expresa de la Supervisión, que el contratista debe solicitar con al menos 24 horas de anticipación y con el detalle del vaciado.

**Uso sugerido:** Cap.2 (punto de liberación del PPI)

#### ucb2025et-03 · requisito_normativo · p. 9 (PDF p. 9)

> los resultados obtenidos en los ensayos de las muestras obtenidas en obra, cumplen a un nivel de confianza del 95%, considerando una distribución normal y debe ser mayor o igual que la resistencia especificada, 𝒇′𝒄 , tal como lo exige el artículo 5.6.5 de la norma NB 1225001

**Paráfrasis:** La resistencia característica estimada estadísticamente con los ensayos de las muestras de obra, con un 95 % de confianza y distribución normal, debe ser igual o mayor que la resistencia especificada, según el artículo 5.6.5 de la NB 1225001.

**Uso sugerido:** Cap.2 (aceptación del hormigón) | Cap.3 Discusión

**Observación:** El texto contiene los símbolos f′k y f′c en caracteres matemáticos Unicode.

#### ucb2025et-04 · requisito_normativo · p. 11 (PDF p. 11)

> La cantidad mínima de cemento, por metro cúbico de hormigón será de 300 kg/m3.

**Paráfrasis:** El contenido mínimo de cemento es de 300 kg por m³ de hormigón.

**Uso sugerido:** Cap.3 Discusión

**Observación:** La ET de la losa de la UATF exige como mínimo 400 kg/m³ para el H25. En la misma página, la relación agua/cemento máxima es 0,60 en ambientes interiores y 0,55 en exteriores no agresivos.

#### ucb2025et-05 · requisito_normativo · p. 12 (PDF p. 12)

> Como norma general, no debe transcurrir más de una hora entre la fabricación del hormigón y su puesta en obra y compactación.

**Paráfrasis:** En general, entre la fabricación del hormigón y su colocación y compactación no debe transcurrir más de una hora.

**Uso sugerido:** Cap.2 (control del hormigonado)

**Observación:** El mismo párrafo prohíbe añadir agua a la mezcla una vez que sale de la mezcladora.

#### ucb2025et-06 · requisito_normativo · p. 13 (PDF p. 13)

> siempre que sea posible, las probetas de control se fabricarán en el lugar de puesta en obra y no a la salida de la hormigonera

**Paráfrasis:** Siempre que sea posible, las probetas de control deben fabricarse en el lugar de colocación y no a la salida de la hormigonera, para que representen el hormigón realmente colocado.

**Uso sugerido:** Cap.2 (muestreo de probetas) | Cap.3 Discusión

**Observación:** Pertinente para discutir que las probetas del Certificado N.º 000293 fueron «traídas y elaboradas por la empresa solicitante» y que no hay probetas de la losa.

#### ucb2025et-07 · requisito_normativo · p. 15 (PDF p. 15)

> se empezara a aplicar la protección al hormigón, tan pronto como este haya endurecido lo suficiente para que su superficie no resulte afectada y se prolongarán durante el plazo mínimo de 7 días o el que la Supervisión lo indique.

**Paráfrasis:** El curado debe comenzar en cuanto la superficie del hormigón lo permita y prolongarse durante un plazo mínimo de 7 días, o el que indique la Supervisión.

**Uso sugerido:** Cap.2 (curado)

#### ucb2025et-08 · requisito_normativo · p. 16 (PDF p. 16)

> Hasta H 25 4 días 10 días 28 días

**Paráfrasis:** Para hormigones de hasta H 25 se recomiendan, como mínimo, 4 días para retirar los tableros laterales de vigas, 10 días para el encofrado de losas y 28 días para el apuntalamiento de vigas y losas de gran luz.

**Uso sugerido:** Cap.1 sección 1.6.2 | Cap.2 (desapuntalamiento)

**Observación:** Plazos orientativos para temperaturas mínimas superiores a 5 °C.

*Plazos mínimos de desencofrado (p. 16)*

| Tipo de hormigón | Tableros laterales de vigas y encofrado de muros y pilares | Encofrados de losas | Apuntalamiento de vigas y losas de gran luz |
|---|---|---|---|
| Hasta H 25 | 4 días | 10 días | 28 días |
| H 35 | 3 días | 8 días | 20 días |
| H 45 | 2 días | 5 días | 10 días |
| Mayor a H 55 | 1 día | 3 días | 6 días |

#### ucb2025et-09 · requisito_normativo · p. 17 (PDF p. 17)

> El acero deberá llegar a la obra en las cantidades en sección y tipo que fija el proyecto (incluyendo los desperdicios posibles), sin oxidación exagerada, exento de aceites, grasas, escamas y también exento de deformaciones.

**Paráfrasis:** El acero debe llegar a obra en las cantidades, secciones y tipos del proyecto, incluyendo los desperdicios posibles, sin oxidación excesiva y libre de aceites, grasas, escamas y deformaciones.

**Uso sugerido:** Cap.2 (recepción del acero) | Cap.3 Discusión

#### ucb2025et-10 · requisito_normativo · p. 19 (PDF p. 19)

> LOSAS: CON VIGUETAS PREFABRICADAS: Por metro cuadrado (m2), entre ejes de vigas a las que llegan. En el cómputo debe figurar la cantidad de metros cuadrados de losa y el volumen de hormigón para la misma como items diferentes.

**Paráfrasis:** Las losas con viguetas prefabricadas se miden por m² entre ejes de las vigas a las que llegan, y el cómputo debe consignar como ítems distintos los m² de losa y el volumen de hormigón.

**Uso sugerido:** Cap.3 Discusión (medición del ítem 13) | Cap.2

**Observación:** En la obra de la UATF, el ítem 13 paga la losa por m² con el hormigón incluido; esta forma de medición separa ambos conceptos y facilita el control del consumo de hormigón.
