# Fichas de citas: normas, legislación boliviana y metodología

**Tesis:** Diseño de un sistema de gestión de la calidad basado en la norma ISO 9001 para reducir costos mediante el control de materiales en losas alivianadas con viguetas pretensadas del Edificio de Posgrado de la UATF, Potosí.

Generado el 2026-10-30. Fichas verificadas: **298**. Archivo de datos: `Fichas_Normas_Legislacion_Metodologia.json` (mismo contenido, formato del contexto maestro). Entradas BibLaTeX: `05_Tesis_LaTeX/bib/normas_legislacion_metodologia.bib`.

## Cómo leer estas fichas

- **Verificación.** Cada `texto_exacto` es copia literal de la capa de texto del PDF (8 a 50 palabras; saltos de línea convertidos en espacios y guiones de corte de línea unidos) y fue comprobado con `pymupdf`: `page.search_for(texto_exacto[:60])` y la búsqueda del texto completo devuelven coincidencias en `pagina_pdf`. Las fichas que no pasaron la verificación no se incluyeron.
- **Páginas.** `pagina_pdf` es el índice del archivo (base 1); `pagina_citable` es el número impreso que va en la cita APA, o «s. p.» si el documento no está paginado. `localizador` indica la sección, artículo o cláusula (en normas y leyes conviene citarlo además de la página).
- **OCR.** Cuando el PDF no tenía capa de texto se generó una con tesseract (`spa`, 300 ppp, escala de grises); esas fichas llevan `capa_de_texto: false` y el campo `pdf_ocr` con la ruta del PDF con OCR (carpeta de trabajo). El texto OCR puede contener errores menores, que se señalan en `nota`.
- **Obras protegidas** (ACI CODE-318-25 y Hernández-Sampieri y Mendoza, 2018): úsense citas breves (menos de 40 palabras, entre comillas y con página) o, preferiblemente, la paráfrasis; no redistribuir los PDF.
- **Integridad.** Las paráfrasis distinguen lo que dice la fuente de las conversiones o cálculos propios, que se marcan como «cálculo propio». Nada de lo aquí fichado sustituye la revisión del contrato y del DBC reales de la obra (CUCE 25-0143-00-1531493-1-1).

## 1. ACI CODE-318-25: Building Code for Structural Concrete (capítulos 2 y 26)

- **Archivo:** `04_Bibliografia/01_Normas_y_Codigos/ACI_318-25_Building_Code_for_Structural_Concrete.pdf`
- **Clave BibLaTeX:** `aci318_2025`
- **Referencia (APA 7):** ACI Committee 318. (2025). *Building code for structural concrete: Code requirements and commentary (ACI CODE-318-25)*. American Concrete Institute. (Primera impresión: enero de 2025; ISBN 978-1-64195-309-2.)

- **Paginación:** número impreso = página del PDF − 1 en todo el cuerpo (p. ej., PDF 602 → p. 601). El índice del código (PDF 8) remite a 26.5 en p. 578 y a 26.13 en p. 607. Las páginas están en dos columnas: CÓDIGO (izquierda) y COMENTARIO (derecha, secciones «R»); las fichas indican cuál es comentario.
- **Unidades:** es la edición en unidades inglesas (*Inch-Pound*). Las equivalencias SI de las paráfrasis son **cálculo propio**: 50 °F = 10 °C; 40 °F ≈ 4,4 °C; 95 °F = 35 °C; 150 yd³ ≈ 114,7 m³; 50 yd³ ≈ 38,2 m³; 5000 ft² ≈ 464,5 m²; 500 psi ≈ 3,45 MPa ≈ 35,2 kg/cm²; 5000 psi ≈ 34,5 MPa ≈ 351,5 kg/cm²; probetas 4 × 8 in ≈ 100 × 200 mm y 6 × 12 in ≈ 150 × 300 mm.
- **Numeración que corrige el encargo:** en ACI CODE-318-25 la investigación de resultados bajos es **26.12.7** (*Investigation of strength tests*, PDF 606–608, pp. 605–607); el 26.12.6 trata la densidad del hormigón liviano. La definición de *strength test* no está en 2.3 sino en **26.12.1.1(a)**; el símbolo fc′ se define en 2.2 (PDF 20, p. 19).
- **Aplicación al caso (cálculo propio):** f′c = 250 kg/cm² ≈ 24,5 MPa ≈ 3.556 psi ≤ 5.000 psi, por lo que rige el criterio «ningún ensayo por debajo de f′c − 500 psi», es decir, ningún ensayo < 250 − 35,2 ≈ 214,8 kg/cm², y el promedio de cada 3 ensayos consecutivos ≥ 250 kg/cm²; en núcleos, promedio de 3 ≥ 0,85 f′c = 212,5 kg/cm² y ningún núcleo < 0,75 f′c = 187,5 kg/cm². Con el criterio de superficie de 26.12.2.1(a)(1)(iii), los 1.109,84 m² de la primera losa exigirían al menos ⌈1.109,84 / 464,5⌉ = 3 muestras (además del criterio diario y del de volumen) y, por 26.12.2.1(a)(2), al menos 5 ensayos por mezcla en el proyecto. El Certificado N.º 000293 no contiene probetas de la losa (dato del expediente).
- **Estatus en Bolivia:** ACI 318 no es obligatorio por sí mismo en Bolivia; la NB 1225001 está basada en ACI 318 (véase la ficha de la NBDS). Por eso se recomienda citar ACI 318-25 como referencia técnica de criterios de aceptación, sin atribuirle numeración de la NB 1225001, cuyo texto no está en el repositorio.

**aci318_2025-01** · PDF p. 20 · cita: p. 19 · 2.2 Notación · *definicion*
> «fc′ = specified compressive strength of concrete, psi»
- **Paráfrasis:** En la notación del código, f′c es la resistencia especificada a la compresión del hormigón (en psi en esta edición); equivale a la resistencia característica H25 (f′c = 250 kg/cm²) que fija la especificación técnica de la losa.
- **Uso sugerido:** Cap.1 marco conceptual (definiciones normativas)

**aci318_2025-02** · PDF p. 38 · cita: p. 37 · 2.3 Terminología · *definicion*
> «compliance requirements—construction-related code requirements directed to the contractor to be incorporated into construction documents by the licensed design professional, as applicable.»
- **Paráfrasis:** Los «requisitos de cumplimiento» son las exigencias del código relativas a la construcción que se dirigen al contratista y que el profesional responsable del diseño incorpora en los documentos de construcción; el capítulo 26 los separa de la «información de diseño».
- **Uso sugerido:** Cap.1 marco conceptual (definiciones normativas)

**aci318_2025-03** · PDF p. 40 · cita: p. 39 · 2.3 Terminología · *definicion*
> «design information—project-specific information to be incorporated into construction documents by the licensed design professional, as applicable.»
- **Paráfrasis:** La «información de diseño» es la información específica del proyecto que el profesional responsable del diseño debe incluir en los documentos de construcción (por ejemplo, f′c, edad de ensayo o clases de exposición).
- **Uso sugerido:** Cap.1 marco conceptual (definiciones normativas)

**aci318_2025-04** · PDF p. 40 · cita: p. 39 · 2.3 Terminología · *definicion*
> «construction documents—written and graphic documents and specifications prepared or assembled for describing the location, design, materials, and physical characteristics of the elements of a project necessary for obtaining a building permit and construction of the project.»
- **Paráfrasis:** Los documentos de construcción comprenden los documentos escritos y gráficos y las especificaciones que describen la ubicación, el diseño, los materiales y las características físicas de los elementos del proyecto; en la obra corresponden a planos y especificaciones técnicas.
- **Uso sugerido:** Cap.1 marco conceptual (definiciones normativas) | Cap.3 Discusión (discrepancias entre ET y Plano 02)

**aci318_2025-05** · PDF p. 38 · cita: p. 37 · 2.3 Terminología · *definicion*
> «building official—term used to identify the Authority having jurisdiction or individual charged with administration and enforcement of provisions of the building code.»
- **Paráfrasis:** La «autoridad de la edificación» es la autoridad competente o la persona encargada de administrar y hacer cumplir el código de edificación; en una obra pública boliviana ese papel de control lo ejercen la entidad contratante, su Fiscal y la Supervisión, según el contrato.
- **Uso sugerido:** Cap.1 marco conceptual (definiciones normativas)

**aci318_2025-06** · PDF p. 44 · cita: p. 43 · 2.3 Terminología · *definicion*
> «inspection—observation, verification, and required documentation of the materials, installation, fabrication, erection, or placement of components and connections to determine compliance with construction documents and referenced standards.»
- **Paráfrasis:** La inspección es la observación, verificación y documentación de materiales, instalación, fabricación, montaje o colocación de componentes para determinar su conformidad con los documentos de construcción y las normas referidas; la documentación forma parte de la definición.
- **Uso sugerido:** Cap.1 marco conceptual (definiciones normativas) | Cap.2 PPI

**aci318_2025-07** · PDF p. 44 · cita: p. 43 · 2.3 Terminología · *definicion*
> «inspection, continuous—the full-time observation, verification, and required documentation of construction being performed. inspection, periodic—the part-time or intermittent observation, verification, and required documentation of construction being performed.»
- **Paráfrasis:** El código distingue la inspección continua (observación y registro a tiempo completo mientras se ejecuta el trabajo) de la periódica (observación y registro a tiempo parcial o intermitente); el PPI puede asignar uno u otro tipo a cada punto de control.
- **Uso sugerido:** Cap.1 marco conceptual (definiciones normativas) | Cap.2 PPI (frecuencia de inspección)

**aci318_2025-08** · PDF p. 45 · cita: p. 44 · 2.3 Terminología · *definicion*
> «licensed design professional—an individual who is licensed to practice structural design as defined by the statutory requirements of the professional licensing laws of the state or jurisdiction in which the project is to be constructed, and who is in responsible charge for all or part of the structural design.»
- **Paráfrasis:** El «profesional de diseño habilitado» es la persona legalmente habilitada para el diseño estructural en la jurisdicción de la obra y responsable de todo o parte de ese diseño; es quien revisa dosificaciones y planes de hormigonado en el esquema del código.
- **Uso sugerido:** Cap.1 marco conceptual (definiciones normativas)

**aci318_2025-09** · PDF p. 54 · cita: p. 53 · 2.3 Terminología · *definicion*
> «Work—the entire construction or separately identifiable parts thereof that are required to be furnished under the construction documents.»
- **Paráfrasis:** «La Obra» (Work) es toda la construcción, o sus partes identificables, que debe entregarse según los documentos de construcción.
- **Uso sugerido:** Cap.1 marco conceptual (definiciones normativas)

**aci318_2025-10** · PDF p. 569 · cita: p. 568 · 26.4.1.1.1(a) · *requisito_normativo*
> «Cementitious materials shall conform to the specifications in Table 26.4.1.1.1(a), except as permitted in 26.4.1.1.1(b).»
- **Paráfrasis:** Los materiales cementantes deben cumplir las especificaciones de la Tabla 26.4.1.1.1(a) (por ejemplo, cemento portland ASTM C150 o cementos adicionados ASTM C595), salvo materiales alternativos aprobados con datos de ensayo.
- **Uso sugerido:** Cap.1 sección normativa (control de materiales del hormigón) | Cap.2 PPI y procedimiento de recepción de materiales

**aci318_2025-11** · PDF p. 570 · cita: p. 569 · 26.4.1.2.1(a) · *requisito_normativo*
> «Aggregates shall conform to (1) or (2): (1) Normalweight aggregate: ASTM C33. (2) Lightweight aggregate: ASTM C330.»
- **Paráfrasis:** Los áridos de peso normal deben cumplir ASTM C33 y los livianos ASTM C330.
- **Uso sugerido:** Cap.1 sección normativa (control de materiales del hormigón) | Cap.2 PPI y procedimiento de recepción de materiales

**aci318_2025-12** · PDF p. 570 · cita: p. 569 · 26.4.1.2.1(b) · *requisito_normativo*
> «Aggregates not conforming to ASTM C33 or ASTM C330 are permitted if they have been shown by test or actual service to produce concrete of adequate strength and durability and are approved by the building official.»
- **Paráfrasis:** Se admiten áridos que no cumplan ASTM C33 o C330 solo si se demuestra, por ensayos o por su desempeño en servicio, que producen hormigón de resistencia y durabilidad adecuadas, y si la autoridad competente los aprueba; es la vía documental exigible a los áridos locales.
- **Uso sugerido:** Cap.1 sección normativa (control de materiales del hormigón) | Cap.2 PPI y procedimiento de recepción de materiales

**aci318_2025-13** · PDF p. 571 · cita: p. 570 · 26.4.1.4.1(a) · *requisito_normativo*
> «26.4.1.4 Water 26.4.1.4.1 Compliance requirements: (a) Mixing water shall conform to ASTM C1602.»
- **Paráfrasis:** El agua de amasado debe cumplir ASTM C1602.
- **Uso sugerido:** Cap.1 sección normativa (control de materiales del hormigón) | Cap.2 PPI y procedimiento de recepción de materiales

**aci318_2025-14** · PDF p. 577 · cita: p. 576 · 26.4.3.1(a) · *requisito_normativo*
> «Concrete mixture proportions shall be established so that the concrete satisfies (1) through (4): (1) Can be placed without segregation and fully encase reinforcement. (2) Meets durability requirements given in the construction documents.»
- **Paráfrasis:** La dosificación debe establecerse para que el hormigón pueda colocarse sin segregación y recubra por completo la armadura, cumpla la durabilidad exigida y satisfaga los requisitos de resistencia (y, si se exige, de módulo de elasticidad).
- **Uso sugerido:** Cap.1 sección normativa (control de materiales del hormigón) | Cap.2 PPI y procedimiento de recepción de materiales | Cap.3 Discusión (dosificaciones no presentadas)

**aci318_2025-15** · PDF p. 578 · cita: p. 577 · 26.4.3.1(c) · *requisito_normativo*
> «The concrete materials used to develop the concrete mixture proportions shall correspond to those to be used in the Work.»
- **Paráfrasis:** Los materiales con que se desarrolla la dosificación deben ser los mismos que se usarán en la obra; si cambia la fuente de cemento o de áridos, la dosificación debe revisarse.
- **Uso sugerido:** Cap.1 sección normativa (control de materiales del hormigón) | Cap.2 PPI y procedimiento de recepción de materiales

**aci318_2025-16** · PDF p. 578 · cita: p. 577 · 26.4.4.1(a) · *requisito_normativo*
> «Documentation of concrete or shotcrete mixture characteristics shall be submitted for review by the licensed design professional before the mixture is used and before making changes to mixtures already in use.»
- **Paráfrasis:** La documentación de cada mezcla debe presentarse para revisión antes de usarla y antes de modificarla; esa documentación incluye registros de ensayos consecutivos o resultados de pastones de prueba.
- **Uso sugerido:** Cap.1 sección normativa (control de materiales del hormigón) | Cap.2 PPI y procedimiento de recepción de materiales | Cap.3 Discusión (el Informe de Supervisión del PAO 2 pide presentar dosificaciones)

**aci318_2025-17** · PDF p. 578 · cita: p. 577 · 26.4.4.1(b) · *requisito_normativo*
> «If field or laboratory test data are not available, and fc′ ≤ 5000 psi, concrete proportions shall be based on other experience or information, if approved by the licensed design professional.»
- **Paráfrasis:** Si no hay datos de ensayo de campo o laboratorio y f′c ≤ 5000 psi (≈ 351,5 kg/cm², cálculo propio), la dosificación puede basarse en otra experiencia o información, siempre que la apruebe el profesional responsable; para el H25 de la losa esta vía exige aprobación expresa.
- **Uso sugerido:** Cap.1 sección normativa (control de materiales del hormigón) | Cap.2 PPI y procedimiento de recepción de materiales

**aci318_2025-18** · PDF p. 579 · cita: p. 578 · 26.5.1.1(a)-(b) · *requisito_normativo*
> «Cementitious materials and aggregates shall be stored to prevent deterioration or contamination. (b) Material that has deteriorated or has been contaminated shall not be used in concrete.»
- **Paráfrasis:** Cemento y áridos deben almacenarse de modo que no se deterioren ni contaminen, y el material deteriorado o contaminado no debe usarse; es la base normativa del control de acopio en obra.
- **Uso sugerido:** Cap.1 sección normativa (control de materiales del hormigón) | Cap.2 PPI y procedimiento de recepción de materiales (almacenamiento y acopio)

**aci318_2025-19** · PDF p. 579 · cita: p. 578 · 26.5.1.1(d) · *requisito_normativo*
> «Ready-mixed and site-mixed concrete shall be batched, mixed, and delivered in accordance with ASTM C94 or ASTM C685.»
- **Paráfrasis:** Tanto el hormigón premezclado como el elaborado en obra deben dosificarse, mezclarse y entregarse conforme a ASTM C94 o ASTM C685.
- **Uso sugerido:** Cap.1 sección normativa (producción y colocación del hormigón) | Cap.2 PPI de la losa (vaciado)

**aci318_2025-20** · PDF p. 580 · cita: p. 579 · 26.5.2.2(e)(3)-(4) · *requisito_normativo*
> «(3) Without segregation or loss of materials. (4) Without interruptions sufficient to permit loss of workability between successive placements that would result in cold joints.»
- **Paráfrasis:** El hormigón debe colocarse sin segregación ni pérdida de materiales y sin interrupciones que hagan perder trabajabilidad entre colocaciones sucesivas y generen juntas frías.
- **Uso sugerido:** Cap.1 sección normativa (producción y colocación del hormigón) | Cap.2 PPI de la losa (vaciado)

**aci318_2025-21** · PDF p. 581 · cita: p. 580 · 26.5.2.2(f) · *requisito_normativo*
> «Concrete that has been contaminated or has lost its initial workability to the extent that it can no longer be consolidated by the intended methods shall not be used.»
- **Paráfrasis:** No debe usarse hormigón contaminado ni el que haya perdido su trabajabilidad hasta el punto de no poder compactarse con los métodos previstos; es un criterio de rechazo en el punto de vaciado.
- **Uso sugerido:** Cap.1 sección normativa (producción y colocación del hormigón) | Cap.2 PPI de la losa (vaciado) | Cap.2 tratamiento de no conformidades

**aci318_2025-22** · PDF p. 581 · cita: p. 580 · 26.5.2.2(h) · *requisito_normativo*
> «After starting, concreting shall be carried on as a continuous operation until the completion of a panel or section, as defined by its boundaries or predetermined joints.»
- **Paráfrasis:** Una vez iniciado, el hormigonado debe ser continuo hasta completar el paño o sección delimitado por sus bordes o por juntas predeterminadas; es compatible con el vaciado por franjas que prevé la especificación técnica si las juntas están definidas de antemano.
- **Uso sugerido:** Cap.1 sección normativa (producción y colocación del hormigón) | Cap.2 PPI de la losa (vaciado) (vaciado de la losa por franjas, según la ET)

**aci318_2025-23** · PDF p. 581 · cita: p. 580 · 26.5.2.2(i) · *requisito_normativo*
> «Concrete shall be consolidated by suitable means during placement and shall be worked around reinforcement and embedments and into corners of forms.»
- **Paráfrasis:** Durante la colocación el hormigón debe compactarse por medios adecuados y trabajarse alrededor de armaduras e insertos y hasta las esquinas del encofrado.
- **Uso sugerido:** Cap.1 sección normativa (producción y colocación del hormigón) | Cap.2 PPI de la losa (vaciado)

**aci318_2025-24** · PDF p. 582 · cita: p. 581 · 26.5.3.2(a)(1) · *requisito_normativo*
> «concrete shall be maintained in a condition that retains water in the concrete for the duration given in (1), (2), or (3). (1) For 7 days after placement with concrete maintained at a temperature of at least 50°F.»
- **Paráfrasis:** El hormigón debe mantenerse en condiciones que retengan el agua durante 7 días después de su colocación y a una temperatura no menor de 50 °F (10 °C, cálculo propio), salvo las alternativas de 3 días con mezcla de alta resistencia inicial o de alcanzar 0,7 f′c in situ.
- **Uso sugerido:** Cap.1 sección normativa (curado) | Cap.2 PPI de la losa (curado, tiempo frío en Potosí, 3.650 m s. n. m.)

**aci318_2025-25** · PDF p. 582 · cita: p. 581 · 26.5.3.2(a)(2) · *requisito_normativo*
> «For 3 days after placement with concrete maintained at a temperature of at least 50°F and proportioned to attain a strength of 0.7fc′ within 3 days.»
- **Paráfrasis:** El curado puede reducirse a 3 días solo si el hormigón, mantenido a 10 °C o más, se dosificó para alcanzar 0,7 f′c en ese plazo, lo que debe demostrarse con probetas ensayadas y documentadas.
- **Uso sugerido:** Cap.1 sección normativa (curado) | Cap.2 PPI de la losa (curado, tiempo frío en Potosí, 3.650 m s. n. m.)

**aci318_2025-26** · PDF p. 583 · cita: p. 582 · 26.5.3.2(e) · *requisito_normativo*
> «Procedures for protecting and curing concrete shall be considered adequate if (1) or (2) are satisfied: (1) Average strength of field-cured cylinders at test age designated for determination of fc′ is equal to or at least 85% of that of companion standard-cured cylinders.»
- **Paráfrasis:** La protección y el curado se consideran adecuados si las probetas curadas en obra alcanzan, a la edad de ensayo, al menos el 85 % de la resistencia de sus compañeras curadas en condiciones normalizadas (o superan f′c en más de 500 psi); sirve como indicador verificable del curado de la losa.
- **Uso sugerido:** Cap.1 sección normativa (curado) | Cap.2 PPI de la losa (curado, tiempo frío en Potosí, 3.650 m s. n. m.) | Cap.2 indicador de eficacia del curado

**aci318_2025-27** · PDF p. 584 · cita: p. 583 · 26.5.4.1(a)-(b) · *requisito_normativo*
> «(a) Temperature limits for concrete as delivered in cold weather. (b) Minimum temperature for embedments, forms, and reinforcement before concrete placement in cold weather.»
- **Paráfrasis:** Para el hormigonado en tiempo frío, los documentos de construcción deben fijar los límites de temperatura del hormigón entregado y la temperatura mínima de insertos, encofrados y armaduras antes del vaciado.
- **Uso sugerido:** Cap.1 sección normativa (curado) | Cap.2 PPI de la losa (curado, tiempo frío en Potosí, 3.650 m s. n. m.)

**aci318_2025-28** · PDF p. 584 · cita: p. 583 · 26.5.4.2(a) · *requisito_normativo*
> «A cold weather concreting plan shall be submitted by the contractor to be reviewed by the licensed design professional.»
- **Paráfrasis:** En tiempo frío el contratista debe presentar un plan de hormigonado para revisión del profesional responsable; en Potosí (3.650 m s. n. m.) este plan debería formar parte del plan de la calidad de la losa.
- **Uso sugerido:** Cap.1 sección normativa (curado) | Cap.2 PPI de la losa (curado, tiempo frío en Potosí, 3.650 m s. n. m.) | Cap.2 plan de la calidad (procedimiento de tiempo frío)

**aci318_2025-29** · PDF p. 584 · cita: p. 583 · R26.5.4.2(a) (comentario) · *metodo*
> «(a) The cold weather concreting plan should contain means and methods to: (i) retain water, (ii) provide or retain sufficient heat in the concrete during the curing period»
- **Paráfrasis:** Según el comentario, el plan de tiempo frío debe prever medios para retener el agua, aportar o conservar calor en el hormigón durante el curado y controlar el descenso de temperatura superficial en las primeras 24 horas tras retirar la protección térmica.
- **Uso sugerido:** Cap.1 sección normativa (curado) | Cap.2 PPI de la losa (curado, tiempo frío en Potosí, 3.650 m s. n. m.)

**aci318_2025-30** · PDF p. 585 · cita: p. 584 · 26.5.4.2(b)-(c) · *requisito_normativo*
> «Aggregates that contain frozen lumps or ice shall not be used. (c) Forms, fillers, and ground with which concrete is to come in contact shall be free from frost and ice.»
- **Paráfrasis:** No deben usarse áridos con terrones congelados o hielo, y encofrados, rellenos y terreno en contacto con el hormigón deben estar libres de escarcha y hielo.
- **Uso sugerido:** Cap.1 sección normativa (curado) | Cap.2 PPI de la losa (curado, tiempo frío en Potosí, 3.650 m s. n. m.) | Cap.2 lista de verificación previa al vaciado

**aci318_2025-31** · PDF p. 585 · cita: p. 584 · 26.5.5.2(a) · *requisito_normativo*
> «A hot weather concreting plan shall be submitted by the contractor to be reviewed by the licensed design professional.»
- **Paráfrasis:** En tiempo caluroso también se exige un plan de hormigonado presentado por el contratista y revisado por el profesional responsable.
- **Uso sugerido:** Cap.1 sección normativa (curado) | Cap.2 PPI de la losa (curado, tiempo frío en Potosí, 3.650 m s. n. m.)

**aci318_2025-32** · PDF p. 585 · cita: p. 584 · R26.5.5.1(a) (comentario) · *dato*
> «ACI SPEC-301 and ACI SPEC-305.1 limit the maximum concrete temperature to 95°F at the time of placement, unless otherwise approved or specified by the licensed design professional.»
- **Paráfrasis:** El comentario indica que ACI SPEC-301 y SPEC-305.1 limitan a 95 °F (35 °C, cálculo propio) la temperatura máxima del hormigón al momento de la colocación, salvo aprobación distinta del profesional responsable.
- **Uso sugerido:** Cap.1 sección normativa (curado) | Cap.2 PPI de la losa (curado, tiempo frío en Potosí, 3.650 m s. n. m.)

**aci318_2025-33** · PDF p. 588 · cita: p. 587 · 26.6.1.2(b) · *requisito_normativo*
> «(b) Mill test reports for reinforcement shall be submitted.»
- **Paráfrasis:** Deben presentarse los certificados de ensayo de fábrica de la armadura; es el documento mínimo de recepción del fierro corrugado.
- **Uso sugerido:** Cap.1 sección normativa (armaduras) | Cap.2 PPI de la losa (parrilla y negativos) | Cap.3 Discusión (control del acero, ítem 8)

**aci318_2025-34** · PDF p. 589 · cita: p. 588 · 26.6.1.2(h) · *requisito_normativo*
> «At the time concrete is placed, reinforcement to be bonded shall be clean of ice, mud, oil, or other deleterious coatings that decrease bond.»
- **Paráfrasis:** Al momento del vaciado, la armadura adherente debe estar libre de hielo, barro, aceite u otros recubrimientos que reduzcan la adherencia.
- **Uso sugerido:** Cap.1 sección normativa (armaduras) | Cap.2 PPI de la losa (parrilla y negativos) | Cap.3 Discusión (control del acero, ítem 8)

**aci318_2025-35** · PDF p. 589 · cita: p. 588 · 26.6.2.1(a) y Tabla 26.6.2.1(a) · *requisito_normativo*
> «Tolerances on location of reinforcement taking into consideration tolerances on d and specified concrete cover in accordance with Table 26.6.2.1(a).»
- **Paráfrasis:** Los documentos deben fijar las tolerancias de ubicación de la armadura según la Tabla 26.6.2.1(a): para d ≤ 8 in, ±3/8 in en d y −3/8 in o −1/3 del recubrimiento (el menor) en el recubrimiento; para d > 8 in, ±1/2 in y −1/2 in o −1/3 del recubrimiento; −1/4 in en fondos encofrados (≈ 9,5; 12,7 y 6,4 mm, cálculo propio).
- **Uso sugerido:** Cap.1 sección normativa (armaduras) | Cap.2 PPI de la losa (parrilla y negativos) | Cap.3 Discusión (control del acero, ítem 8) | Cap.2 criterios de aceptación del armado en el PPI

**aci318_2025-36** · PDF p. 590 · cita: p. 589 · 26.6.2.2(a) · *requisito_normativo*
> «Reinforcement, including bundled bars, shall be placed within required tolerances and supported to prevent displacement beyond required tolerances during concrete placement.»
- **Paráfrasis:** La armadura debe colocarse dentro de las tolerancias y apoyarse de modo que no se desplace fuera de ellas durante el vaciado (por ejemplo, separadores y sillas para la parrilla de la carpeta).
- **Uso sugerido:** Cap.1 sección normativa (armaduras) | Cap.2 PPI de la losa (parrilla y negativos) | Cap.3 Discusión (control del acero, ítem 8)

**aci318_2025-37** · PDF p. 602 · cita: p. 601 · 26.12.1.1(a) · *definicion*
> «A strength test is the average of the compressive strengths of at least two 4 x 8 in. or two 6 x 12 in. cylinders made from the same sample of concrete taken in accordance with ASTM C172 at the point of delivery»
- **Paráfrasis:** Un «ensayo de resistencia» es el promedio de al menos dos probetas cilíndricas (100 × 200 o 150 × 300 mm aprox.) de la misma muestra, tomada según ASTM C172 en el punto de entrega, curadas según ASTM C31 y ensayadas según ASTM C39 a 28 días o a la edad designada para f′c.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293)

**aci318_2025-38** · PDF p. 603 · cita: p. 602 · R26.12.1.1(a) (comentario) · *definicion*
> «Note that the term “strength test” does not apply to results of tests on cylinders field cured in or on the structure as described in ASTM C31, nor does it apply to results of tests on cylinders from laboratory trial batches.»
- **Paráfrasis:** El comentario aclara que no son «ensayos de resistencia» para aceptación los resultados de probetas curadas en obra ni los de pastones de prueba de laboratorio.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293)

**aci318_2025-39** · PDF p. 603 · cita: p. 602 · 26.12.1.1(d) · *requisito_normativo*
> «Certified field testing technicians shall perform tests on fresh concrete at the job site, prepare specimens for standard curing, prepare specimens for field curing, if required, and record the temperature of the fresh concrete when preparing specimens for strength tests.»
- **Paráfrasis:** Los ensayos del hormigón fresco y la elaboración de probetas en obra deben estar a cargo de técnicos de campo certificados, que además registran la temperatura del hormigón al moldear las probetas.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293) (probetas «traídas y elaboradas por la empresa solicitante»)

**aci318_2025-40** · PDF p. 603 · cita: p. 602 · 26.12.1.1(f) · *requisito_normativo*
> «All reports of acceptance tests shall be provided to the licensed design professional, contractor, concrete producer, and, if requested, to the owner and the building official.»
- **Paráfrasis:** Todos los informes de ensayos de aceptación deben entregarse al profesional responsable del diseño, al contratista y al productor del hormigón, y al propietario y a la autoridad si lo solicitan.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293) | Cap.2 control de registros

**aci318_2025-41** · PDF p. 604 · cita: p. 603 · 26.12.2.1(a)(1)(i)-(ii) · *requisito_normativo*
> «Samples for preparing strength-test specimens of each concrete mixture placed each day shall be taken in accordance with (i) through (iii): (i) At least once a day. (ii) At least once for each 150 yd3 of concrete.»
- **Paráfrasis:** De cada mezcla colocada cada día debe tomarse al menos una muestra diaria y al menos una por cada 150 yd³ (≈ 114,7 m³, cálculo propio) de hormigón.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293) | Cap.2 frecuencia de muestreo del plan de la calidad

**aci318_2025-42** · PDF p. 604 · cita: p. 603 · 26.12.2.1(a)(1)(iii) · *requisito_normativo*
> «(iii) At least once for each 5000 ft2 of surface area for slabs or walls.»
- **Paráfrasis:** En losas y muros se exige además al menos una muestra por cada 5000 ft² (≈ 464,5 m², cálculo propio) de superficie; para los 1.109,84 m² de la primera losa serían al menos 3 muestras (cálculo propio).
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293) | Cap.2 frecuencia de muestreo de la losa

**aci318_2025-43** · PDF p. 604 · cita: p. 603 · 26.12.2.1(a)(2) · *requisito_normativo*
> «if total volume of concrete is such that frequency of testing would provide fewer than five strength tests for a given concrete mixture, strength test specimens shall be made from at least five randomly selected batches or from each batch if fewer than five batches are used.»
- **Paráfrasis:** Si la frecuencia anterior diera menos de cinco ensayos de resistencia para una mezcla en el proyecto, deben moldearse probetas de al menos cinco pastones elegidos al azar, o de cada pastón si son menos de cinco.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293)

**aci318_2025-44** · PDF p. 604 · cita: p. 603 · 26.12.2.1(a)(3) · *requisito_normativo*
> «If the total quantity of a given concrete mixture is less than 50 yd3, strength tests are not required if evidence of satisfactory strength is submitted to and approved by the building official.»
- **Paráfrasis:** Solo cuando la cantidad total de una mezcla es menor de 50 yd³ (≈ 38,2 m³, cálculo propio) pueden omitirse los ensayos, y únicamente si la autoridad aprueba la evidencia de resistencia satisfactoria presentada.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293)

**aci318_2025-45** · PDF p. 604 · cita: p. 603 · R26.12.2.1(a)(1) (comentario) · *metodo*
> «Concrete samples for preparing strength-test specimens are to be taken on a strictly random basis if they are to measure properly the acceptability of the concrete.»
- **Paráfrasis:** Para que midan correctamente la aceptabilidad del hormigón, las muestras deben tomarse de forma estrictamente aleatoria, no por apariencia o conveniencia, porque de lo contrario el análisis estadístico pierde validez.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293) | Cap.2 método de muestreo

**aci318_2025-46** · PDF p. 604 · cita: p. 603 · R26.12.2.1(a)(1) (comentario) · *metodo*
> «In calculating surface area, only one side of the slab or wall is considered. Criterion (iii) will require more frequent sampling than once for each 150 yd3 placed if average wall or slab thickness is less than 9-3/4 in.»
- **Paráfrasis:** La superficie se calcula con una sola cara de la losa; el criterio de superficie gobierna sobre el de volumen cuando el espesor medio es menor de 9-3/4 in (≈ 248 mm, cálculo propio), caso de una losa alivianada cuyo espesor equivalente de hormigón es menor que su altura de 25 cm.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293)

**aci318_2025-47** · PDF p. 604 · cita: p. 603 · 26.12.3.1(a)(1) · *requisito_normativo*
> «Strength level of a concrete mixture shall be acceptable if (1) and (2) are satisfied: (1) Every average of any three consecutive strength tests equals or exceeds fc′.»
- **Paráfrasis:** El nivel de resistencia de una mezcla es aceptable si todo promedio de tres ensayos consecutivos iguala o supera f′c y, además, se cumple el límite para ensayos individuales.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293) | Cap.2 criterio de aceptación

**aci318_2025-48** · PDF p. 604 · cita: p. 603 · 26.12.3.1(a)(2) · *requisito_normativo*
> «No strength test falls below fc′ by more than 500 psi if fc′ is 5000 psi or less; or by more than 0.10fc′ if fc′ exceeds 5000 psi.»
- **Paráfrasis:** Ningún ensayo individual puede quedar por debajo de f′c en más de 500 psi cuando f′c ≤ 5000 psi (o en más de 0,10 f′c si f′c > 5000 psi); para f′c = 250 kg/cm², el umbral individual es ≈ 214,8 kg/cm² (cálculo propio).
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293) | Cap.3 Discusión (4 de 12 valores < 260 kg/cm² en el Certificado N.º 000293)

**aci318_2025-49** · PDF p. 604 · cita: p. 603 · 26.12.3.1(b) · *requisito_normativo*
> «If either of the requirements of 26.12.3.1(a) is not satisfied, steps shall be taken to increase subsequent strength tests.»
- **Paráfrasis:** Si no se cumple alguno de los dos criterios, deben tomarse medidas para aumentar la resistencia de los ensayos siguientes (acción correctiva).
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293) | Cap.2 acción correctiva

**aci318_2025-50** · PDF p. 604 · cita: p. 603 · R26.12.3.1 (comentario) · *dato*
> «Strength tests failing to meet these criteria will occur occasionally, with a probability of approximately once in 100 tests (ACI PRC-214) even though concrete strength and uniformity are satisfactory.»
- **Paráfrasis:** Aun con hormigón satisfactorio, cerca de un ensayo de cada cien incumplirá los criterios por variación estadística, lo que debe considerarse antes de concluir que la resistencia es inadecuada.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293) | Cap.2 fundamento probabilístico del criterio

**aci318_2025-51** · PDF p. 605 · cita: p. 604 · 26.12.3.1(c) · *requisito_normativo*
> «(c) Requirements of 26.12.7 for investigating strength tests shall apply if the requirements of 26.12.3.1(a)(2) are not met.»
- **Paráfrasis:** Si un ensayo individual incumple el límite de 26.12.3.1(a)(2), se aplica el procedimiento de investigación de 26.12.7.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293)

**aci318_2025-52** · PDF p. 605 · cita: p. 604 · 26.12.4.1(a) · *requisito_normativo*
> «Before application of prestressing forces or removal of shoring and formwork supporting beams and slabs, the compressive strength of field-cured cylinders shall be acceptable if the strengths of all cylinders made from the same sample»
- **Paráfrasis:** Antes de retirar puntales y encofrados de vigas y losas, todas las probetas curadas en obra de una misma muestra deben igualar o superar la resistencia requerida para esa etapa, salvo aprobación distinta del profesional responsable.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293) | Cap.2 PPI (desencofrado y retiro de puntales de la losa)

**aci318_2025-53** · PDF p. 607 · cita: p. 606 · 26.12.7.1(a) · *requisito_normativo*
> «If any strength test of standard-cured cylinders falls below fc′ by more than the limit allowed for acceptance, or if tests of field-cured cylinders indicate deficiencies in protection and curing, steps shall be taken to ensure that structural adequacy of the structure is not jeopardized.»
- **Paráfrasis:** Si un ensayo de probetas normalizadas queda por debajo del límite de aceptación, o si las probetas curadas en obra revelan deficiencias de protección y curado, deben adoptarse medidas para asegurar que no se comprometa la seguridad estructural.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293) | Cap.2 tratamiento de no conformidades

**aci318_2025-54** · PDF p. 607 · cita: p. 606 · 26.12.7.1(b) · *requisito_normativo*
> «In such cases, three cores shall be taken for each strength test that falls below fc′ by more than the limit allowed for acceptance.»
- **Paráfrasis:** Confirmada la probable baja resistencia y si los cálculos muestran reducción significativa de la capacidad, se extraen tres núcleos (ASTM C42) por cada ensayo que incumplió el límite de aceptación.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293)

**aci318_2025-55** · PDF p. 607 · cita: p. 606 · 26.12.7.1(e) · *requisito_normativo*
> «Concrete in an area represented by core tests shall be considered structurally adequate if (1) and (2) are satisfied: (1) The average of three cores is equal to at least 85% of fc′. (2) No single core is less than 75% of fc′.»
- **Paráfrasis:** El hormigón representado por los núcleos se considera estructuralmente adecuado si el promedio de tres núcleos es al menos 0,85 f′c y ninguno es menor de 0,75 f′c (212,5 y 187,5 kg/cm² para H25, cálculo propio).
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293)

**aci318_2025-56** · PDF p. 608 · cita: p. 607 · 26.12.7.1(g) · *requisito_normativo*
> «the responsible authority shall be permitted to order a strength evaluation in accordance with Chapter 27 for the questionable portion of the structure or take other appropriate action.»
- **Paráfrasis:** Si los núcleos no cumplen y persiste la duda, la autoridad puede ordenar una evaluación de resistencia según el capítulo 27 para la parte cuestionada o adoptar otra medida apropiada.
- **Uso sugerido:** Cap.1 sección normativa (evaluación y aceptación del hormigón) | Cap.2 plan de muestreo y ensayos | Cap.3 Discusión (Certificado N.º 000293)

**aci318_2025-57** · PDF p. 609 · cita: p. 608 · 26.13.1.1 · *requisito_normativo*
> «Concrete construction shall be inspected as required by the general building code, and as a minimum, the inspection shall comply with the requirements provided in 26.13. In the absence of a general building code, concrete construction shall be inspected in accordance with the provisions of this Code.»
- **Paráfrasis:** La construcción de hormigón debe inspeccionarse según el código general de edificación y, como mínimo, conforme a 26.13; a falta de un código general, se inspecciona según el propio ACI 318.
- **Uso sugerido:** Cap.1 sección normativa (inspección) | Cap.2 registros de calidad e inspección del SGC

**aci318_2025-58** · PDF p. 609 · cita: p. 608 · 26.13.1.2 · *requisito_normativo*
> «Inspection of concrete construction shall be conducted by the licensed design professional responsible for the design, a person under the supervision of the licensed design professional, or a qualified inspector. The inspection shall verify conformance with construction documents throughout the various stages of construction.»
- **Paráfrasis:** La inspección la realiza el profesional responsable del diseño, una persona bajo su supervisión o un inspector calificado, y debe verificar la conformidad con los documentos de construcción en todas las etapas de la obra.
- **Uso sugerido:** Cap.1 sección normativa (inspección) | Cap.2 registros de calidad e inspección del SGC | Cap.1 (paralelo con la Supervisión técnica del DBC)

**aci318_2025-59** · PDF p. 611 · cita: p. 610 · 26.13.2.1 · *requisito_normativo*
> «Records of the inspection shall be preserved by the party performing the inspection for at least 2 years after completion of the project.»
- **Paráfrasis:** Quien inspecciona debe conservar los registros de inspección al menos 2 años después de terminado el proyecto.
- **Uso sugerido:** Cap.1 sección normativa (inspección) | Cap.2 registros de calidad e inspección del SGC | Cap.2 control de la información documentada

**aci318_2025-60** · PDF p. 611 · cita: p. 610 · 26.13.2.2(c) · *requisito_normativo*
> «The date and time of mixing, quantity of concrete placed, identification of mixtures used, approximate placement location in the structure, and results of tests for fresh and hardened concrete properties for all concrete mixtures used in the Work.»
- **Paráfrasis:** Los informes de inspección deben registrar fecha y hora del mezclado, cantidad de hormigón colocado, mezcla usada, ubicación aproximada en la estructura y resultados de ensayos en estado fresco y endurecido.
- **Uso sugerido:** Cap.1 sección normativa (inspección) | Cap.2 registros de calidad e inspección del SGC | Cap.2 formato de registro de vaciado

**aci318_2025-61** · PDF p. 611 · cita: p. 610 · 26.13.2.2(d) · *requisito_normativo*
> «Concrete temperatures and protection given to concrete during placement and curing if the ambient temperature falls below 40°F or rises above 95°F.»
- **Paráfrasis:** Si la temperatura ambiente baja de 40 °F (≈ 4,4 °C) o supera 95 °F (35 °C) (conversiones propias), deben registrarse las temperaturas del hormigón y la protección dada durante la colocación y el curado.
- **Uso sugerido:** Cap.1 sección normativa (inspección) | Cap.2 registros de calidad e inspección del SGC | Cap.1 sección normativa (curado) | Cap.2 PPI de la losa (curado, tiempo frío en Potosí, 3.650 m s. n. m.)

**aci318_2025-62** · PDF p. 612 · cita: p. 611 · 26.13.3.2(a) · *requisito_normativo*
> «Items requiring verification and continuous inspection shall include (a) through (e): (a) Prior to placement, concrete mixture for intended location.»
- **Paráfrasis:** Antes del vaciado, la verificación de que la mezcla corresponde al elemento previsto es un punto de inspección continua.
- **Uso sugerido:** Cap.1 sección normativa (inspección) | Cap.2 registros de calidad e inspección del SGC | Cap.2 PPI (punto de espera antes del vaciado)

**aci318_2025-63** · PDF p. 612 · cita: p. 611 · 26.13.3.3(a) · *requisito_normativo*
> «26.13.3.3 Items requiring verification and periodic inspection shall include (a) through (m): (a) Placement of reinforcement, embedments»
- **Paráfrasis:** La colocación de armaduras e insertos es un punto de inspección periódica obligatoria; en la obra corresponde a la verificación del armado de la losa solicitada en el Libro de Órdenes.
- **Uso sugerido:** Cap.1 sección normativa (inspección) | Cap.2 registros de calidad e inspección del SGC | Cap.2 PPI (verificación del armado)

**aci318_2025-64** · PDF p. 612 · cita: p. 611 · 26.13.3.3(c)-(d) · *requisito_normativo*
> «(c) Curing method and duration of curing for each member. (d) Construction and removal of forms and reshoring.»
- **Paráfrasis:** También son puntos de inspección periódica el método y la duración del curado de cada elemento y la construcción y el retiro de encofrados y reapuntalamientos.
- **Uso sugerido:** Cap.1 sección normativa (inspección) | Cap.2 registros de calidad e inspección del SGC | Cap.2 PPI (curado y desencofrado)


## 2. Norma Boliviana de Diseño Sísmico 2023 (MOPSV) y R.M. N.º 271/2023

- **Archivo:** `04_Bibliografia/01_Normas_y_Codigos/MOPSV_NBDS_2023_Norma_Boliviana_Diseno_Sismico.pdf`
- **Clave BibLaTeX:** `mopsv2023nbds`
- **Referencia (APA 7):** Ministerio de Obras Públicas, Servicios y Vivienda. (2023). *Norma Boliviana de Diseño Sísmico (NBDS 2023)*. Aprobada por Resolución Ministerial N.º 271 de 27 de noviembre de 2023.

- **Capa de texto:** el cuerpo de la norma tiene capa de texto; las PDF 6–8 (la R.M. N.º 271, escaneada) no la tienen y se procesaron con OCR. La NBDS no está escaneada en su totalidad.
- **Paginación:** número impreso = PDF − 14 en el cuerpo (PDF 15 → p. 1; PDF 139 → p. 125); la presentación usa romanos (PDF 11 → p. iii). La R.M. 271 (PDF 6–8) no lleva la paginación de la norma («Página 1 de 3» a «3 de 3»): se cita como s. p. con su punto resolutivo.
- **Qué dice sobre la norma de hormigón (respuesta al encargo):**
  1. La NBDS remite expresamente a la **NB 1225001** como «norma de diseño específica» para hormigón estructural (art. 1) y a ella se remiten las definiciones de pórticos y muros de hormigón armado y el uso de inercias modificadas (pp. 22 y 28); en su bibliografía la cita como «NB 1225001. (s.f.). Hormigón Estructural (Primera ed.) … IBNORCA» (p. 125).
  2. Ordena aplicar la NBDS «en conjunto» con las normas de cada material y que, en caso de contradicción, prevalezca la NBDS (art. 10, p. 19).
  3. La obligatoriedad que consta en el documento es la **de la propia NBDS**: la R.M. N.º 271 (27/11/2023) la aprueba y dispone que «es de aplicación obligatoria a nivel nacional» (resuelve tercero). **No hay en la NBDS ni en la R.M. 271 una declaración expresa de obligatoriedad de la NB 1225001**, ni mención alguna de la CBH-87 (búsqueda sin resultados) ni del D.S. 22976/1991. La obligatoriedad de la NB 1225001 queda, por tanto, como dato a verificar en su propio instrumento de aprobación (Bibliografia_Recomendada.md menciona una R.M. MOPSV 172/2020 que no está en el repositorio).
  4. La R.M. 271 deja sin efecto la R.M. N.º 177 de 18/09/2020; el PDF no indica el objeto de esa resolución.
- **Utilidad directa para la losa:** el art. 12.I fija requisitos para que una losa de viguetas prefabricadas funcione como diafragma rígido (altura mínima 250 mm con carpeta, carpeta ≥ 50 mm con malla de 6 mm c/250 mm, separación entre ejes ≤ 2 × altura, hormigonado simultáneo con las vigas, etc.). Comparación con el caso (cálculo propio sobre datos del expediente): la ET y los certificados (20 + 5 = 25 cm; separación 50 cm; parrilla φ6 c/20; vaciado monolítico con vigas) son coherentes con esos mínimos, mientras que el corte del Plano 02 (0,15 + 0,05 = 0,20 m) no alcanzaría los 250 mm: inconsistencia documental que debe verificar la Supervisión.

**mopsv2023nbds-01** · PDF p. 15 · cita: p. 1 · Art. 1 (Objeto) · *requisito_normativo*
> «Esta norma junto con las normas de diseño específicas [p. ej. para hormigón estructural (NB 1225001)] está orientada a lograr estructuras que:»
- **Paráfrasis:** La NBDS se concibe para aplicarse junto con las normas de diseño específicas de cada material y señala como ejemplo, para el hormigón estructural, la NB 1225001.
- **Uso sugerido:** Cap.1 sección normativa (marco normativo del hormigón en Bolivia)

**mopsv2023nbds-02** · PDF p. 15 · cita: p. 1 · Art. 2 (Campo de aplicación) · *requisito_normativo*
> «Esta norma es aplicable al análisis, diseño y construcción de edificaciones sismorresistentes, además se incluyen recomendaciones para realizar el diagnóstico y refuerzo sísmico de estructuras.»
- **Paráfrasis:** La NBDS rige el análisis, el diseño y la construcción de edificaciones sismorresistentes; su art. 2 incluye expresamente a las universidades entre las edificaciones públicas y privadas alcanzadas, por lo que comprende al Edificio de Posgrado.
- **Uso sugerido:** Cap.1 sección normativa (marco normativo del hormigón en Bolivia)

**mopsv2023nbds-03** · PDF p. 33 · cita: p. 19 · Art. 10 (Coordinación con otras normas) · *requisito_normativo*
> «Las disposiciones de la presente norma deben aplicarse en conjunto con lo dispuesto en otras normas de análisis y en las recomendaciones específicas de diseño para cada material. En caso de contradicción deben prevalecer las disposiciones de la presente norma.»
- **Paráfrasis:** La NBDS debe aplicarse conjuntamente con las normas de análisis y de diseño de cada material, y prevalece sobre ellas en caso de contradicción.
- **Uso sugerido:** Cap.1 sección normativa (marco normativo del hormigón en Bolivia)

**mopsv2023nbds-04** · PDF p. 36 · cita: p. 22 · Art. 12.I (Viguetas prefabricadas), incs. a)-b) · *requisito_normativo*
> «Para que un sistema de piso formado por viguetas prefabricadas funja como diafragma rígido, este deberá cumplir lo siguiente: a) La altura máxima de la estructura deberá ser 30 m, medidos desde la rasante de vía. b) Altura mínima de 250 mm (Incluye carpeta de compresión).»
- **Paráfrasis:** Para que una losa de viguetas prefabricadas funcione como diafragma rígido, la estructura no debe superar 30 m de altura y la losa debe tener al menos 250 mm de altura total, incluida la carpeta de compresión.
- **Uso sugerido:** Cap.1 sección normativa (losas de viguetas pretensadas) | Cap.2 PPI (criterios de verificación de la losa) | Cap.3 Discusión (ET, Plano 02 y certificado PRETENSA)

**mopsv2023nbds-05** · PDF p. 36 · cita: p. 22 · Art. 12.I, incs. c)-e) · *requisito_normativo*
> «c) Las viguetas deben estar empotradas en vigas de borde, por lo menos 100 mm y en vigas centrales, al menos 70 mm. d) Las viguetas deben empotrarse en vigas altas (peraltadas).»
- **Paráfrasis:** Las viguetas deben empotrarse al menos 100 mm en vigas de borde y 70 mm en vigas centrales, y apoyarse en vigas peraltadas; además deben llevar acero de refuerzo sobre los apoyos (inc. e).
- **Uso sugerido:** Cap.1 sección normativa (losas de viguetas pretensadas) | Cap.2 PPI (criterios de verificación de la losa) | Cap.3 Discusión (ET, Plano 02 y certificado PRETENSA)

**mopsv2023nbds-06** · PDF p. 36 · cita: p. 22 · Art. 12.I, inc. f) · *requisito_normativo*
> «f) La carpeta de compresión deberá tener al menos 50 mm de espesor y mínimamente contar con una malla de acero de 6 mm cada 250 mm.»
- **Paráfrasis:** La carpeta de compresión debe tener al menos 50 mm de espesor y una malla mínima de barras de 6 mm cada 250 mm; la parrilla φ6 c/20 de la especificación técnica supera ese mínimo (comparación propia).
- **Uso sugerido:** Cap.1 sección normativa (losas de viguetas pretensadas) | Cap.2 PPI (criterios de verificación de la losa) | Cap.3 Discusión (ET, Plano 02 y certificado PRETENSA) (parrilla φ6 c/20 de la ET)

**mopsv2023nbds-07** · PDF p. 36 · cita: p. 22 · Art. 12.I, incs. g)-h) · *requisito_normativo*
> «g) Las losas de viguetas deberán tener una dimensión máxima de 6 x 6 m2. h) Las losas de viguetas deberán contar con nervios rigidizadores perpendiculares a las viguetas con una separación máxima de 2.50 m.»
- **Paráfrasis:** Cada paño de losa de viguetas debe limitarse a 6 × 6 m y llevar nervios rigidizadores perpendiculares a las viguetas separados como máximo 2,50 m.
- **Uso sugerido:** Cap.1 sección normativa (losas de viguetas pretensadas) | Cap.2 PPI (criterios de verificación de la losa) | Cap.3 Discusión (ET, Plano 02 y certificado PRETENSA)

**mopsv2023nbds-08** · PDF p. 36 · cita: p. 22 · Art. 12.I, incs. i)-j) · *requisito_normativo*
> «i) La separación entre ejes de viguetas será como máximo, el doble de la altura de la losa. j) La losa de viguetas deberá ser hormigonada simultáneamente con las vigas de apoyo directo e indirecto.»
- **Paráfrasis:** La separación entre ejes de viguetas no debe exceder el doble de la altura de la losa (50 cm para 25 cm de altura, cálculo propio) y la losa debe hormigonarse simultáneamente con sus vigas de apoyo.
- **Uso sugerido:** Cap.1 sección normativa (losas de viguetas pretensadas) | Cap.2 PPI (criterios de verificación de la losa) | Cap.3 Discusión (ET, Plano 02 y certificado PRETENSA) (vaciado monolítico con vigas)

**mopsv2023nbds-09** · PDF p. 36 · cita: p. 22 · Art. 12.I, inc. k) · *requisito_normativo*
> «k) Si las viguetas están simplemente apoyadas sobre las vigas, entonces, no se debe tomar en cuenta la contribución de este tipo de losa a la rigidez lateral de la estructura y tampoco esta losa define un diafragma rígido.»
- **Paráfrasis:** Si las viguetas quedan simplemente apoyadas, la losa no aporta rigidez lateral ni puede considerarse diafragma rígido; por eso el control del empotramiento y del armado sobre apoyos es un punto crítico de inspección.
- **Uso sugerido:** Cap.1 sección normativa (losas de viguetas pretensadas) | Cap.2 PPI (criterios de verificación de la losa) | Cap.3 Discusión (ET, Plano 02 y certificado PRETENSA) (el certificado PRETENSA indica luz máxima de 7,50 m «simplemente apoyada»)

**mopsv2023nbds-10** · PDF p. 42 · cita: p. 28 · Art. 16.I c) (Resistencia a compresión) · *requisito_normativo*
> «debe ser de 21 MPa; pero, se recomienda el empleo de 25 MPa.»
- **Paráfrasis:** Para estructuras de hormigón armado, la resistencia mínima a compresión es 21 MPa y se recomienda 25 MPa; el H25 especificado (≈ 24,5 MPa, cálculo propio) se ubica en ese rango recomendado.
- **Uso sugerido:** Cap.1 sección normativa (marco normativo del hormigón en Bolivia) | Cap.3 Discusión (H25 de la ET; carpeta f′c ≥ 21 MPa del certificado PRETENSA)

**mopsv2023nbds-11** · PDF p. 42 · cita: p. 28 · Art. 16.I a) · *dato*
> «La (NB 1225001) indica el uso de momentos de inercia modificados en los elementos estructurales, pero para efectos de esta norma se pueden utilizar los momentos de inercia sin modificar.»
- **Paráfrasis:** La NBDS toma la NB 1225001 como referencia del diseño de hormigón (por ejemplo, para las inercias modificadas), aunque para sus propios fines permite usar inercias sin modificar.
- **Uso sugerido:** Cap.1 sección normativa (marco normativo del hormigón en Bolivia)

**mopsv2023nbds-12** · PDF p. 82 · cita: p. 68 · Título V, cap. I, III (Requisitos de evaluación) · *dato*
> «La resistencia a cada una de las solicitaciones de los elementos estructurales se obtendrá según lo estipulado en la normativa estadounidense de hormigón armado (ACI 318, 2019)»
- **Paráfrasis:** Para evaluar estructuras existentes, la NBDS remite a la normativa estadounidense de hormigón armado (ACI 318-19), lo que muestra la base ACI del marco técnico boliviano.
- **Uso sugerido:** Cap.1 sección normativa (marco normativo del hormigón en Bolivia)

**mopsv2023nbds-13** · PDF p. 139 · cita: p. 125 · Título VII, Bibliografía · *dato*
> «NB 1225001. (s.f.). Hormigón Estructural (Primera ed.). Santa Cruz de la Sierra, Santa Cruz, Bolivia: Instituto Boliviano de Normalización y Calidad.»
- **Paráfrasis:** La bibliografía de la NBDS registra la NB 1225001, Hormigón estructural, primera edición, de IBNORCA, sin fecha.
- **Uso sugerido:** Cap.1 sección normativa (marco normativo del hormigón en Bolivia)

**mopsv2023nbds-14** · PDF p. 8 · cita: s. p. · R.M. N.º 271/2023, resuelve primero · *requisito_normativo* · OCR
> «Aprobar la Norma Boliviana de Diseño Sísmico — NBDS, elaborada por el Comité Técnico para la Elaboración de la Norma Boliviana de Diseño Sísmico, en sus»
- **Paráfrasis:** El Ministerio de Obras Públicas, Servicios y Vivienda aprobó la NBDS elaborada por su comité técnico, en sus catorce capítulos y tres anexos.
- **Uso sugerido:** Cap.1 sección normativa (marco normativo del hormigón en Bolivia)
- **Nota:** OCR: en el original el guion tras «NBDS» es una raya corta (–); el texto se lee completo en la imagen («…en sus catorce (14) capítulos y sus 3 Anexos…»).

**mopsv2023nbds-15** · PDF p. 8 · cita: s. p. · R.M. N.º 271/2023, resuelve segundo · *dato* · OCR
> «Se deja sin efecto la Resolución Ministerial No. 177 del 18 de septiembre de»
- **Paráfrasis:** La R.M. 271 deja sin efecto la Resolución Ministerial N.º 177 de 18 de septiembre de 2020 (el PDF no indica su objeto).
- **Uso sugerido:** Cap.1 sección normativa (marco normativo del hormigón en Bolivia)
- **Nota:** OCR verificado contra la imagen: «SEGUNDO.- Se deja sin efecto la Resolución Ministerial No. 177 del 18 de septiembre de 2020.»

**mopsv2023nbds-16** · PDF p. 8 · cita: s. p. · R.M. N.º 271/2023, resuelve tercero · *requisito_normativo* · OCR
> «La presente Resolución Ministerial es, de aplicación obligatoria a nivel nacional.»
- **Paráfrasis:** La resolución que aprueba la NBDS dispone su aplicación obligatoria en todo el territorio nacional; la obligatoriedad documentada corresponde a la NBDS, no a la NB 1225001.
- **Uso sugerido:** Cap.1 sección normativa (marco normativo del hormigón en Bolivia)
- **Nota:** OCR: la coma tras «es» es una mancha del escaneo; en la imagen se lee «TERCERO.- La presente Resolución Ministerial es de aplicación obligatoria a nivel nacional.» Fecha de la R.M. (sello): La Paz, 27 de noviembre de 2023.

**mopsv2023nbds-17** · PDF p. 7 · cita: s. p. · R.M. N.º 271/2023, considerandos (Informe INF/MOPSV/VMVU/DGVU/UPC N.º 0084/2023) · *dato* · OCR
> «de contar en nuestro Estado Plurinacional de Bolivia con una Norma de carácter vinculante»
- **Paráfrasis:** El informe técnico que sustenta la R.M. 271 justifica la aprobación por la necesidad de contar en Bolivia con una norma sísmica de carácter vinculante para departamentos, municipios, colegios profesionales y universidades.
- **Uso sugerido:** Cap.1 sección normativa (marco normativo del hormigón en Bolivia)
- **Nota:** El pasaje completo comienza en la línea anterior: «Por la necesidad de contar en nuestro Estado Plurinacional de Bolivia con una Norma de carácter vinculante…».


## 3. Hernández-Sampieri y Mendoza Torres (2018): Metodología de la investigación

- **Archivo:** `04_Bibliografia/02_Metodologia_y_Redaccion/Hernandez-Sampieri_Mendoza_2018_Metodologia_de_la_Investigacion.pdf`
- **Clave BibLaTeX:** `hernandez2018`
- **Referencia (APA 7):** Hernández-Sampieri, R., & Mendoza Torres, C. P. (2018). *Metodología de la investigación: las rutas cuantitativa, cualitativa y mixta*. McGraw-Hill Interamericana Editores. (Primera edición; ISBN 978-1-4562-6096-5.)

- **Paginación:** en todo el cuerpo del libro el número impreso = PDF − 39 (PDF 145 → p. 106; PDF 411 → p. 372); los preliminares usan romanos (índice en PDF 14–17 = pp. xiii–xvi).
- **Mapa de páginas útiles (número impreso):** ruta cuantitativa pp. 5–7 (cap. 1); alcances pp. 104–116 (cap. 5: exploratorio 106, descriptivo 108, correlacional 109, explicativo 110–112, alcances mixtos 113); hipótesis pp. 122–140 (cap. 6: definición 124, de investigación 127, direccionales 129–131, nulas 133, prueba de hipótesis 135, definición operacional 137–138); diseños pp. 148–191 (cap. 7: diseño 150, experimento 151, validez interna y Tabla 7.1 de amenazas 158–159, clasificación de Campbell y Stanley 161, preexperimentos y preprueba-posprueba con un grupo 163, cuasiexperimentos 173, no experimentales 174–183, transeccionales 176–179, retrospectivos 180, longitudinales 180–183); muestra pp. 194–217 (cap. 8: censo 196, no probabilística 200 y 215); confiabilidad y validez pp. 228–239 (cap. 9: confiabilidad 228, validez 229, contenido 230, validez de expertos 235, coeficientes 239); análisis pp. 310–373 (cap. 10: nivel de significancia 341–342, supuestos paramétricos 345, prueba *t* 352–353, no paramétricos 362, tabla de pruebas 372).
- **Lo que NO está en la obra impresa (no citar a este libro para ello):** la prueba de Shapiro-Wilk no aparece (el único «Shapiro» es una cita sobre regresión, p. 350); Kolmogorov-Smirnov solo figura como prueba para dos muestras en la tabla de la p. 372, no como prueba de normalidad; la prueba de Wilcoxon solo aparece nombrada en esa tabla (pares de rangos, muestras correlacionadas), sin desarrollo; la **simulación (Monte Carlo)** no se trata como método de análisis (solo «simulación de sufragio» o «preguntas de simulación»). Para Shapiro-Wilk, Wilcoxon y Monte Carlo debe citarse una fuente estadística específica. El juicio de expertos aparece como «validez de expertos» (p. 235), pero el coeficiente **V de Aiken** no figura en el libro.

**hernandez2018-01** · PDF p. 44 · cita: p. 5 · Cap. 1 · *definicion*
> «El significado original del término cuantitativo (del latín “quantitas”) se vincula a conteos numéricos y métodos matemáticos (Niglas, 2010).»
- **Paráfrasis:** El término cuantitativo remite, por su origen, a conteos numéricos y métodos matemáticos; la ruta cuantitativa organiza procesos secuenciales para comprobar suposiciones.
- **Uso sugerido:** Cap.2 sección de metodología (tipo y enfoque de la investigación)

**hernandez2018-02** · PDF p. 45 · cita: p. 6 · Cap. 1 · *definicion*
> «La ruta cuantitativa es apropiada cuando queremos estimar las magnitudes u ocurrencia de los fenómenos y probar hipótesis.»
- **Paráfrasis:** La ruta cuantitativa es la adecuada cuando se busca estimar magnitudes de los fenómenos y someter hipótesis a prueba, como ocurre al estimar la reducción del costo unitario de la losa.
- **Uso sugerido:** Cap.2 sección de metodología (tipo y enfoque de la investigación)

**hernandez2018-03** · PDF p. 45 · cita: p. 6 · Cap. 1 · *metodo*
> «3. Las hipótesis se generan antes de recolectar y analizar los datos. 4. Los datos se encuentran en forma de números (cantidades) y, por tanto, su recolección se fundamenta en la medición»
- **Paráfrasis:** En la ruta cuantitativa las hipótesis se formulan antes de recolectar los datos, y estos, al ser numéricos, se obtienen por medición con procedimientos estandarizados.
- **Uso sugerido:** Cap.2 sección de metodología (tipo y enfoque de la investigación)

**hernandez2018-04** · PDF p. 145 · cita: p. 106 · Cap. 5 · *definicion*
> «Los alcances son cuatro: exploratorio, descriptivo, correlacional y explicativo. No representan clases o tipos de investigación, ni son mutuamente excluyentes, sino que constituyen puntos entrelazados de un continuo de causalidad»
- **Paráfrasis:** Los cuatro alcances (exploratorio, descriptivo, correlacional y explicativo) no son tipos excluyentes de investigación sino puntos de un continuo de causalidad, de modo que un estudio puede combinarlos.
- **Uso sugerido:** Cap.2 sección de metodología (alcance o nivel: explicativo con fase descriptiva)

**hernandez2018-05** · PDF p. 145 · cita: p. 106 · Cap. 5 · *definicion*
> «Los estudios exploratorios se llevan a cabo cuando el propósito es examinar un fenómeno o problema de investigación nuevo o poco estudiado, sobre el cual se tienen muchas dudas o no se ha abordado antes.»
- **Paráfrasis:** Los estudios exploratorios examinan problemas nuevos o poco estudiados, sobre los que existen muchas dudas o que no se han abordado antes.
- **Uso sugerido:** Cap.2 sección de metodología (alcance o nivel: explicativo con fase descriptiva)

**hernandez2018-06** · PDF p. 147 · cita: p. 108 · Cap. 5 · *definicion*
> «Los estudios descriptivos pretenden especificar las propiedades, características y perfiles de personas, grupos, comunidades, procesos, objetos o cualquier otro fenómeno que se someta a un análisis.»
- **Paráfrasis:** Los estudios descriptivos especifican propiedades, características y perfiles de procesos u objetos sometidos a análisis, como la caracterización documental de la primera losa ejecutada sin SGC.
- **Uso sugerido:** Cap.2 sección de metodología (alcance o nivel: explicativo con fase descriptiva) (fase descriptiva de la línea base O1)

**hernandez2018-07** · PDF p. 148 · cita: p. 109 · Cap. 5 · *definicion*
> «Este tipo de estudios tiene como finalidad conocer la relación o grado de asociación que existe entre dos o más conceptos, categorías o variables en un contexto en particular.»
- **Paráfrasis:** Los estudios correlacionales buscan conocer la relación o el grado de asociación entre dos o más variables en un contexto particular.
- **Uso sugerido:** Cap.2 sección de metodología (alcance o nivel: explicativo con fase descriptiva)

**hernandez2018-08** · PDF p. 149 · cita: p. 110 · Cap. 5 · *definicion*
> «Los estudios explicativos van más allá de la descripción de fenómenos, conceptos o variables o del establecimiento de relaciones entre estas; están dirigidos a responder por las causas de los eventos»
- **Paráfrasis:** Los estudios explicativos superan la descripción y la correlación: buscan responder por las causas de los fenómenos y por qué se relacionan las variables, como el efecto del SGC sobre el costo de la losa.
- **Uso sugerido:** Cap.2 sección de metodología (alcance o nivel: explicativo con fase descriptiva)

**hernandez2018-09** · PDF p. 152 · cita: p. 113 · Cap. 5 · *metodo*
> «Algunas veces, una investigación puede caracterizarse como básicamente exploratoria, descriptiva, correlacional o explicativa, pero no situarse únicamente como tal.»
- **Paráfrasis:** Una investigación puede ser esencialmente de un alcance y contener elementos de otros; esto respalda declarar un nivel explicativo con una fase descriptiva previa.
- **Uso sugerido:** Cap.2 sección de metodología (alcance o nivel: explicativo con fase descriptiva)

**hernandez2018-10** · PDF p. 163 · cita: p. 124 · Cap. 6 · *definicion*
> «Las hipótesis son explicaciones tentativas del fenómeno o problema investigado formuladas como proposiciones o afirmaciones y constituyen las guías de un estudio.»
- **Paráfrasis:** Las hipótesis son explicaciones tentativas, formuladas como proposiciones, que guían el estudio y responden provisionalmente a las preguntas de investigación.
- **Uso sugerido:** Introducción (hipótesis) | Cap.2 sección de metodología (sistema de hipótesis) | Cap.3 contraste de hipótesis

**hernandez2018-11** · PDF p. 166 · cita: p. 127 · Cap. 6 · *definicion*
> «Lo que a lo largo del capítulo hemos presentado como hipótesis son en realidad las hipótesis de investigación (proposiciones tentativas acerca de la o las posibles relaciones entre dos o más variables).»
- **Paráfrasis:** Las hipótesis de investigación (Hi o H1) son proposiciones tentativas sobre las posibles relaciones entre dos o más variables; pueden ser predictivas de un valor, correlacionales, de diferencia de grupos o causales.
- **Uso sugerido:** Introducción (hipótesis) | Cap.2 sección de metodología (sistema de hipótesis) | Cap.3 contraste de hipótesis

**hernandez2018-12** · PDF p. 168 · cita: p. 129 · Cap. 6 · *metodo*
> «Cuando el investigador no tiene bases para presuponer a favor de qué grupo será la diferencia, formula una hipótesis no direccional; y cuando sí tiene bases, establece una hipótesis direccional de diferencia de grupos.»
- **Paráfrasis:** Si el investigador tiene bases teóricas o antecedentes para anticipar a favor de qué grupo será la diferencia, formula una hipótesis direccional; si no, una no direccional.
- **Uso sugerido:** Introducción (hipótesis) | Cap.2 sección de metodología (sistema de hipótesis) | Cap.3 contraste de hipótesis (H1 direccional: reducción del costo ≥ 5 %)

**hernandez2018-13** · PDF p. 169 · cita: p. 130 · Cap. 6 · *definicion*
> «pero todas estas hipótesis establecen relaciones de causa-efecto. Regularmente son direccionales.»
- **Paráfrasis:** Las hipótesis causales proponen una explicación de la relación entre variables (causa-efecto) y suelen ser direccionales.
- **Uso sugerido:** Introducción (hipótesis) | Cap.2 sección de metodología (sistema de hipótesis) | Cap.3 contraste de hipótesis

**hernandez2018-14** · PDF p. 172 · cita: p. 133 · Cap. 6 · *definicion*
> «Las hipótesis nulas como su nombre lo indica refutan o niegan lo que afirman las hipótesis de investigación. Representan el reverso o contradicción de estas»
- **Paráfrasis:** La hipótesis nula (H0) niega o refuta lo que afirma la hipótesis de investigación y representa su contradicción.
- **Uso sugerido:** Introducción (hipótesis) | Cap.2 sección de metodología (sistema de hipótesis) | Cap.3 contraste de hipótesis

**hernandez2018-15** · PDF p. 174 · cita: p. 135 · Cap. 6 · *metodo*
> «En realidad, no podemos probar que una hipótesis sea verdadera o falsa, sino argumentar que fue respaldada o no de acuerdo con los datos obtenidos y análisis realizados en nuestro estudio»
- **Paráfrasis:** Una hipótesis no se prueba como verdadera o falsa: se concluye que los datos y análisis del estudio la respaldan o no, en el contexto de casos, lugar y tiempo investigados.
- **Uso sugerido:** Introducción (hipótesis) | Cap.2 sección de metodología (sistema de hipótesis) | Cap.3 contraste de hipótesis

**hernandez2018-16** · PDF p. 176 · cita: p. 137 · Cap. 6 · *definicion*
> «Una definición operacional consiste en el conjunto de procedimientos, técnicas y métodos para medir una variable en los casos de la investigación.»
- **Paráfrasis:** La definición operacional especifica los procedimientos, técnicas y métodos con que se mide cada variable en los casos estudiados; es la base de la matriz de operacionalización (dimensiones, indicadores, instrumentos).
- **Uso sugerido:** Cap.2 sección de metodología (operacionalización de variables)

**hernandez2018-17** · PDF p. 189 · cita: p. 150 · Cap. 7 · *definicion*
> «El término diseño se refiere al plan o estrategia concebida para obtener la información que deseas con el propósito de responder al planteamiento del problema»
- **Paráfrasis:** El diseño de investigación es el plan o estrategia para obtener la información necesaria y responder al planteamiento del problema.
- **Uso sugerido:** Cap.2 sección de metodología (diseño de investigación: no experimental longitudinal retrospectivo + evaluación ex ante por simulación)

**hernandez2018-18** · PDF p. 190 · cita: p. 151 · Cap. 7 · *definicion*
> «La esencia de esta concepción de experimento es la manipulación intencional de una acción para analizar sus posibles resultados.»
- **Paráfrasis:** Lo esencial de un experimento es la manipulación intencional de una acción o variable independiente para analizar sus resultados; la tesis no manipula el SGC en obra, por lo que no es experimental.
- **Uso sugerido:** Cap.2 sección de metodología (diseño de investigación: no experimental longitudinal retrospectivo + evaluación ex ante por simulación)

**hernandez2018-19** · PDF p. 193 · cita: p. 154 · Cap. 7 · *definicion*
> «el grupo de control no recibe el tratamiento o estímulo experimental.»
- **Paráfrasis:** En un experimento, el grupo experimental recibe el tratamiento y el grupo de control no; por analogía, la simulación compara un escenario de control sin SGC con otro con SGC (tratamiento).
- **Uso sugerido:** Cap.2 sección de metodología (diseño de investigación: no experimental longitudinal retrospectivo + evaluación ex ante por simulación) (escenario de control «sin SGC» en la simulación)

**hernandez2018-20** · PDF p. 197 · cita: p. 158 · Cap. 7 · *definicion*
> «El control o validez interna se refiere a que, si en el experimento observas que una o más variables independientes hacen variar a las dependientes, la variación de estas últimas se deba verdaderamente a la manipulación de las primeras y no a otros factores o causas»
- **Paráfrasis:** La validez interna existe cuando la variación observada en la variable dependiente se debe realmente a la variable independiente y no a otros factores.
- **Uso sugerido:** Cap.2 sección de metodología (validez interna y limitaciones) | Cap.3 Discusión (limitaciones)

**hernandez2018-21** · PDF p. 198 · cita: p. 159 · Cap. 7, Tabla 7.1 · *definicion*
> «Su nombre se debe a que, precisamente, atentan contra la validez interna de un experimento, y esta se refiere a cuánta confianza podemos tener en que sea posible interpretar los resultados del experimento y estos sean válidos.»
- **Paráfrasis:** Las fuentes de invalidación interna son explicaciones rivales que reducen la confianza con que pueden interpretarse los resultados como efecto del tratamiento.
- **Uso sugerido:** Cap.2 sección de metodología (validez interna y limitaciones) | Cap.3 Discusión (limitaciones)

**hernandez2018-22** · PDF p. 198 · cita: p. 159 · Cap. 7, Tabla 7.1 (historia) · *definicion*
> «Historia Eventos o acontecimientos externos que ocurran durante el experimento e inﬂuyan solamente a algunos de los participantes»
- **Paráfrasis:** La amenaza de «historia» consiste en acontecimientos externos que ocurren durante el estudio y afectan los resultados; en el caso, la crisis de combustibles y el alza de precios de 2025–2026 son eventos de este tipo que la simulación a precios constantes neutraliza.
- **Uso sugerido:** Cap.2 sección de metodología (validez interna y limitaciones) | Cap.3 Discusión (limitaciones) (D.S. 5503, alza de combustibles y paralización de la obra)
- **Nota:** La capa de texto usa la ligadura «ﬂ» en «inﬂuyan»; al citar, escríbase «influyan».

**hernandez2018-23** · PDF p. 198 · cita: p. 159 · Cap. 7, Tabla 7.1 (maduración) · *definicion*
> «Maduración Los participantes pueden cambiar o madurar durante el experimento y esto afectar los resultados»
- **Paráfrasis:** La «maduración» es el cambio natural de los participantes durante el estudio que puede confundirse con el efecto del tratamiento; en obra, el aprendizaje de la cuadrilla entre losas es un análogo que debe declararse.
- **Uso sugerido:** Cap.2 sección de metodología (validez interna y limitaciones) | Cap.3 Discusión (limitaciones) (curva de aprendizaje de la cuadrilla entre la primera y las siguientes losas)

**hernandez2018-24** · PDF p. 198 · cita: p. 159 · Cap. 7, Tabla 7.1 (instrumentación) · *definicion*
> «Instrumentación Las pruebas o instrumentos aplicados a los distintos grupos que participan en el experimento no sean equivalentes»
- **Paráfrasis:** La amenaza de «instrumentación» surge cuando se usan instrumentos no equivalentes entre grupos; por eso la línea base y los escenarios simulados deben medirse con el mismo cómputo y los mismos precios unitarios.
- **Uso sugerido:** Cap.2 sección de metodología (validez interna y limitaciones) | Cap.3 Discusión (limitaciones)

**hernandez2018-25** · PDF p. 200 · cita: p. 161 · Cap. 7 · *metodo*
> «la clásica tipología de Campbell y Stanley (1966) en: 1. Preexperimentos. 2. Experimentos puros (con control). 3. Cuasiexperimentos.»
- **Paráfrasis:** Siguiendo a Campbell y Stanley (1966), los diseños experimentales se clasifican en preexperimentos, experimentos puros con control y cuasiexperimentos.
- **Uso sugerido:** Cap.2 sección de metodología (diseño de investigación: no experimental longitudinal retrospectivo + evaluación ex ante por simulación)

**hernandez2018-26** · PDF p. 202 · cita: p. 163 · Cap. 7 · *definicion*
> «Los preexperimentos se denominan así porque su grado de control es mínimo. Son diseños con un grupo único.»
- **Paráfrasis:** Los preexperimentos tienen un control mínimo y trabajan con un solo grupo.
- **Uso sugerido:** Cap.2 sección de metodología (diseño de investigación: no experimental longitudinal retrospectivo + evaluación ex ante por simulación)

**hernandez2018-27** · PDF p. 202 · cita: p. 163 · Cap. 7 (G M1 X M2) · *metodo*
> «A un grupo se le aplica una prueba previa al estímulo o tratamiento experimental, después se le administra el tratamiento y finalmente se le aplica una prueba posterior al estímulo.»
- **Paráfrasis:** En el diseño de preprueba-posprueba con un solo grupo (G M1 X M2) se mide al grupo antes del tratamiento, se aplica el tratamiento y se vuelve a medir.
- **Uso sugerido:** Cap.2 sección de metodología (diseño de investigación: no experimental longitudinal retrospectivo + evaluación ex ante por simulación) (diseño previsto en el perfil, no ejecutable por la paralización)

**hernandez2018-28** · PDF p. 202 · cita: p. 163 · Cap. 7 · *hallazgo*
> «el diseño no resulta conveniente para fines de establecer causalidad: no hay manipulación ni grupo de comparación y es posible que actúen varias fuentes de invalidación interna, por ejemplo, la historia.»
- **Paráfrasis:** El diseño de un solo grupo con preprueba y posprueba no permite establecer causalidad: carece de grupo de comparación y queda expuesto a amenazas como la historia; de ahí la decisión de usar un escenario de control simulado.
- **Uso sugerido:** Cap.2 sección de metodología (validez interna y limitaciones) | Cap.3 Discusión (limitaciones)

**hernandez2018-29** · PDF p. 202 · cita: p. 163 · Cap. 7 · *conclusion*
> «Los diseños de un grupo único no poseen un control riguroso y más bien se les utiliza como exploratorios»
- **Paráfrasis:** Por su escaso control, los diseños de un solo grupo se usan más bien con fines exploratorios y sus resultados deben interpretarse con cautela.
- **Uso sugerido:** Cap.2 sección de metodología (validez interna y limitaciones) | Cap.3 Discusión (limitaciones)

**hernandez2018-30** · PDF p. 212 · cita: p. 173 · Cap. 7 · *definicion*
> «En los diseños cuasiexperimentales, los sujetos no se asignan al azar a los grupos ni se emparejan, sino que dichos grupos ya están formados antes del experimento: son grupos intactos»
- **Paráfrasis:** Los cuasiexperimentos manipulan al menos una variable independiente, pero trabajan con grupos intactos, formados antes del estudio y no asignados al azar.
- **Uso sugerido:** Cap.2 sección de metodología (diseño de investigación: no experimental longitudinal retrospectivo + evaluación ex ante por simulación)

**hernandez2018-31** · PDF p. 213 · cita: p. 174 · Cap. 7 · *dato*
> «como las encuestas de opinión, los estudios ex post facto retrospectivos y prospectivos, etc.»
- **Paráfrasis:** Entre los estudios no experimentales se cuentan los ex post facto retrospectivos y prospectivos, en los que las variables independientes ya ocurrieron y no pueden manipularse.
- **Uso sugerido:** Cap.2 sección de metodología (diseño de investigación: no experimental longitudinal retrospectivo + evaluación ex ante por simulación)

**hernandez2018-32** · PDF p. 214 · cita: p. 175 · Cap. 7 · *definicion*
> «La investigación no experimental es sistemática y empírica en la que las variables independientes no se manipulan porque ya han sucedido.»
- **Paráfrasis:** La investigación no experimental es sistemática y empírica, y no manipula las variables independientes porque ya ocurrieron; las relaciones se observan tal como se dieron en su contexto.
- **Uso sugerido:** Cap.2 sección de metodología (diseño de investigación: no experimental longitudinal retrospectivo + evaluación ex ante por simulación) (línea base documental de la primera losa)

**hernandez2018-33** · PDF p. 215 · cita: p. 176 · Cap. 7 · *definicion*
> «Los diseños transeccionales o transversales recolectan datos en un solo momento, en un tiempo único.»
- **Paráfrasis:** Los diseños transeccionales o transversales recolectan los datos en un único momento.
- **Uso sugerido:** Cap.2 sección de metodología (diseño de investigación: no experimental longitudinal retrospectivo + evaluación ex ante por simulación)

**hernandez2018-34** · PDF p. 219 · cita: p. 180 · Cap. 7 · *definicion*
> «Asimismo, a veces se reconstruyen las relaciones causales a partir de las variables dependientes, en otras a partir de las independientes y en otras más sobre la base de variabilidad amplia de las independientes y dependientes (León y Montero, 2003). Al primer caso se le conoce como diseños retrospectivos»
- **Paráfrasis:** Cuando las relaciones causales se reconstruyen a partir de las variables dependientes ya observadas, el diseño se denomina retrospectivo; si se parte de las independientes, prospectivo.
- **Uso sugerido:** Cap.2 sección de metodología (diseño de investigación: no experimental longitudinal retrospectivo + evaluación ex ante por simulación) (reconstrucción de la línea base a partir de planillas y cómputos)

**hernandez2018-35** · PDF p. 219 · cita: p. 180 · Cap. 7 · *definicion*
> «Diseños longitudinales Estudios que recaban datos en diferentes puntos del tiempo para realizar inferencias acerca de la evolución del problema de investigación o fenómeno, sus causas y sus efectos.»
- **Paráfrasis:** Los diseños longitudinales recaban datos en distintos momentos para inferir la evolución del fenómeno, sus causas y efectos; las planillas sucesivas de avance permiten un análisis de este tipo.
- **Uso sugerido:** Cap.2 sección de metodología (diseño de investigación: no experimental longitudinal retrospectivo + evaluación ex ante por simulación) (PAO N.º 1 a 3 como cortes sucesivos)

**hernandez2018-36** · PDF p. 235 · cita: p. 196 · Cap. 8 · *definicion*
> «Únicamente cuando pretendas realizar un censo debes incluir en el estudio a todos los casos (personas, productos, procesos, organizaciones, animales, plantas, objetos) del universo o la población.»
- **Paráfrasis:** Un censo incluye todos los casos de la población; estudiar los 41 paños de la primera losa constituye un censo de la línea base y no una muestra.
- **Uso sugerido:** Cap.2 sección de metodología (población, muestra y censo de los 41 paños)

**hernandez2018-37** · PDF p. 239 · cita: p. 200 · Cap. 8 · *definicion*
> «En las muestras no probabilísticas, la elección de las unidades no depende de la probabilidad, sino de razones relacionadas con las características y contexto de la investigación.»
- **Paráfrasis:** En las muestras no probabilísticas las unidades se eligen por las características y el contexto de la investigación, no por probabilidad.
- **Uso sugerido:** Cap.2 sección de metodología (población, muestra y censo de los 41 paños) (selección intencional de la losa y de los expertos)

**hernandez2018-38** · PDF p. 254 · cita: p. 215 · Cap. 8 · *metodo*
> «La ventaja de una muestra no probabilística —desde la visión cuantitativa— es su utilidad para determinados diseños de estudio que requieren no tanto una representatividad de elementos de una población, sino una cuidadosa y controlada elección de casos»
- **Paráfrasis:** La muestra no probabilística es útil cuando interesa una elección cuidadosa de casos con características definidas más que la representatividad; su costo es que los resultados no pueden generalizarse rigurosamente a la población.
- **Uso sugerido:** Cap.2 sección de metodología (población, muestra y censo de los 41 paños) | Cap.3 Discusión (generalización limitada)

**hernandez2018-39** · PDF p. 267 · cita: p. 228 · Cap. 9 · *definicion*
> «La confiabilidad o fiabilidad de un instrumento de medición se refiere al grado en que su aplicación repetida al mismo individuo, caso o muestra produce resultados iguales»
- **Paráfrasis:** La confiabilidad de un instrumento es el grado en que su aplicación repetida a los mismos casos produce resultados iguales o consistentes.
- **Uso sugerido:** Cap.2 sección de metodología (validez y confiabilidad de instrumentos; juicio de expertos y V de Aiken)

**hernandez2018-40** · PDF p. 268 · cita: p. 229 · Cap. 9 · *definicion*
> «La validez, en términos generales, se refiere al grado en que un instrumento mide con exactitud la variable que verdaderamente pretende medir.»
- **Paráfrasis:** La validez es el grado en que un instrumento mide con exactitud la variable que pretende medir.
- **Uso sugerido:** Cap.2 sección de metodología (validez y confiabilidad de instrumentos; juicio de expertos y V de Aiken)

**hernandez2018-41** · PDF p. 269 · cita: p. 230 · Cap. 9 · *definicion*
> «La validez de contenido se refiere al grado en que un instrumento refleja un dominio específico de contenido de lo que se mide»
- **Paráfrasis:** La validez de contenido es el grado en que el instrumento representa el dominio de contenido de lo que se mide; en la tesis, que los ítems de la lista de verificación cubran los requisitos del SGC y del control de materiales.
- **Uso sugerido:** Cap.2 sección de metodología (validez y confiabilidad de instrumentos; juicio de expertos y V de Aiken)

**hernandez2018-42** · PDF p. 274 · cita: p. 235 · Cap. 9 · *definicion*
> «la validez de expertos o face validity, la cual se refiere al grado en que aparentemente un instrumento mide la variable en cuestión de acuerdo con voces calificadas.»
- **Paráfrasis:** La validez de expertos es el grado en que, según voces calificadas, el instrumento mide la variable; está vinculada a la validez de contenido y hoy se considera una evidencia adicional.
- **Uso sugerido:** Cap.2 sección de metodología (validez y confiabilidad de instrumentos; juicio de expertos y V de Aiken)

**hernandez2018-43** · PDF p. 274 · cita: p. 235 · Cap. 9 · *metodo*
> «Regularmente se establece mediante la evaluación del instrumento ante expertos.»
- **Paráfrasis:** La validez de expertos se obtiene sometiendo el instrumento a la evaluación de especialistas; el libro no desarrolla el coeficiente V de Aiken, que debe citarse de otra fuente.
- **Uso sugerido:** Cap.2 sección de metodología (validez y confiabilidad de instrumentos; juicio de expertos y V de Aiken) (la aplicación del juicio de expertos queda pendiente para el postulante)

**hernandez2018-44** · PDF p. 274 · cita: p. 235 · Cap. 9 · *conclusion*
> «Un instrumento de medición puede ser confiable, pero no necesariamente válido»
- **Paráfrasis:** Confiabilidad y validez son requisitos distintos: un instrumento consistente puede no medir lo que pretende, por lo que deben demostrarse ambas.
- **Uso sugerido:** Cap.2 sección de metodología (validez y confiabilidad de instrumentos; juicio de expertos y V de Aiken)

**hernandez2018-45** · PDF p. 278 · cita: p. 239 · Cap. 9 · *dato*
> «La mayoría oscilan entre cero y uno, donde un coeficiente de cero (0) significa nula confiabilidad y uno (1) representa un máximo de confiabilidad (fiabilidad total, perfecta).»
- **Paráfrasis:** Los coeficientes de confiabilidad suelen variar entre 0 (confiabilidad nula) y 1 (confiabilidad total).
- **Uso sugerido:** Cap.2 sección de metodología (validez y confiabilidad de instrumentos; juicio de expertos y V de Aiken)

**hernandez2018-46** · PDF p. 381 · cita: p. 342 · Cap. 10 · *metodo*
> «El nivel de significancia de 0.05, el cual implica que el investigador (tú) tiene 95% de seguridad para generalizar sin equivocarse y solo 5% en contra. En términos de probabilidad, 0.95 y 0.05, respectivamente; ambos suman la unidad.»
- **Paráfrasis:** Con un nivel de significancia de 0,05 el investigador tiene 95 % de seguridad para generalizar y 5 % de riesgo de equivocarse; es el criterio adoptado en la regla de decisión probabilística de la tesis.
- **Uso sugerido:** Cap.2 plan de análisis estadístico | Cap.3 contraste de hipótesis (criterio P(r ≥ 5 %) ≥ 0,95, equivalente a α = 0,05)

**hernandez2018-47** · PDF p. 381 · cita: p. 342 · Cap. 10 · *dato*
> «Muy utilizado cuando las generalizaciones implican riesgos vitales para las personas (pruebas de vacunas, medicamentos, arneses de aviones, resistencia de materiales de construcción al fuego o al peso, etcétera).»
- **Paráfrasis:** El nivel de 0,01 se reserva para generalizaciones con riesgo vital, como la resistencia de materiales de construcción; para una decisión económica como la reducción de costos basta 0,05.
- **Uso sugerido:** Cap.2 plan de análisis estadístico | Cap.3 contraste de hipótesis

**hernandez2018-48** · PDF p. 382 · cita: p. 343 · Cap. 10 · *metodo*
> «cabe destacar que en una misma investigación es posible llevar a cabo análisis paramétricos para algunas hipótesis y variables, y análisis no paramétricos para otras.»
- **Paráfrasis:** En una misma investigación pueden combinarse análisis paramétricos y no paramétricos según el tipo de hipótesis y el nivel de medición de cada variable.
- **Uso sugerido:** Cap.2 plan de análisis estadístico | Cap.3 contraste de hipótesis

**hernandez2018-49** · PDF p. 384 · cita: p. 345 · Cap. 10 · *metodo*
> «Para realizar análisis paramétricos debe partirse de los siguientes supuestos: 1. La distribución poblacional de la variable dependiente es normal: el universo tiene una distribución normal.»
- **Paráfrasis:** Los análisis paramétricos suponen distribución normal de la variable dependiente en la población, medición por intervalos o razón y varianzas homogéneas; de ahí la necesidad de verificar la normalidad (con una prueba que debe citarse de otra fuente).
- **Uso sugerido:** Cap.2 plan de análisis estadístico | Cap.3 contraste de hipótesis (verificar normalidad antes de usar la prueba t)

**hernandez2018-50** · PDF p. 391 · cita: p. 352 · Cap. 10 · *definicion*
> «Definición: es una prueba estadística para que evalúes si dos grupos difieren entre sí de manera significativa respecto a sus medias y distribuciones en una variable.»
- **Paráfrasis:** La prueba t evalúa si dos grupos difieren significativamente en sus medias de una variable medida por intervalos o razón.
- **Uso sugerido:** Cap.2 plan de análisis estadístico | Cap.3 contraste de hipótesis

**hernandez2018-51** · PDF p. 392 · cita: p. 353 · Cap. 10 · *metodo*
> «cualquiera, pero reducida a dos categorías (individuos productivos-individuos no productivos, género, dos productos que compiten entre sí, preprueba y posprueba de un grupo experimental).»
- **Paráfrasis:** En la prueba t la variable de agrupación debe reducirse a dos categorías, entre ellas la preprueba y la posprueba de un mismo grupo experimental.
- **Uso sugerido:** Cap.2 plan de análisis estadístico | Cap.3 contraste de hipótesis

**hernandez2018-52** · PDF p. 401 · cita: p. 362 · Cap. 10 · *metodo*
> «La mayoría de estos análisis no requieren de presupuestos acerca de la forma de la distribución poblacional. Aceptan distribuciones no normales (distribuciones “libres”).»
- **Paráfrasis:** Los análisis no paramétricos no exigen supuestos sobre la forma de la distribución poblacional y admiten distribuciones no normales.
- **Uso sugerido:** Cap.2 plan de análisis estadístico | Cap.3 contraste de hipótesis

**hernandez2018-53** · PDF p. 411 · cita: p. 372 · Cap. 10, tabla de pruebas · *definicion*
> «Mientras que en las correlacionadas sí existe una relación entre las unidades o participantes de las muestras; por ejemplo, el mismo grupo antes y después de un tratamiento experimental, preprueba y posprueba.»
- **Paráfrasis:** Las muestras correlacionadas (relacionadas o pareadas) son las que guardan relación entre sí, como el mismo grupo medido antes y después de un tratamiento.
- **Uso sugerido:** Cap.2 plan de análisis estadístico | Cap.3 contraste de hipótesis

**hernandez2018-54** · PDF p. 411 · cita: p. 372 · Cap. 10, tabla de pruebas (dos grupos, muestras correlacionadas) · *metodo*
> «Prueba de McNemar Prueba de Wilcoxon para pares de rangos Prueba t para muestras correlacionadas»
- **Paráfrasis:** Para comparar dos grupos de muestras correlacionadas, la tabla del libro indica McNemar (datos nominales), Wilcoxon para pares de rangos (ordinales) y t para muestras correlacionadas (intervalos o razón); el libro solo las nombra.
- **Uso sugerido:** Cap.2 plan de análisis estadístico | Cap.3 contraste de hipótesis


## 4. Guía Normas APA 7.ª edición (resumen de normas-apa.org)

- **Archivo:** `04_Bibliografia/02_Metodologia_y_Redaccion/Guia_Normas_APA_7ma_Edicion.pdf`
- **Clave BibLaTeX:** `apaguia`
- **Referencia (APA 7):** Normas APA. (s. f.). *Guía Normas APA 7.ª edición* [Archivo PDF]. https://normas-apa.org/

- **Naturaleza:** es un resumen no oficial «producido por un lector del blog normas-apa.org» (p. 5), que remite al manual oficial (American Psychological Association, 2020; p. 57). No consta autor personal ni fecha en el documento (los metadatos del PDF indican creación el 25/05/2020): se referencia con autor corporativo y «s. f.».
- **Paginación:** el número impreso coincide con la página del PDF.
- **Choques con la estructura del docente que conviene declarar:** la guía pide no numerar títulos (p. 29) y titular la lista final «Referencias» (p. 45); la tesis conserva capítulos numerados y el título «Bibliografía» porque lo exige la estructura del Taller 1 (contexto maestro). La guía llama «apéndices» (pp. 23–25) a lo que la tesis llama «Anexos».

**apaguia-01** · PDF p. 5 · cita: p. 5 · Introducción · *dato*
> «Esta es una guía resumida con los principales puntos de las Normas APA (7ª edición), producida por un lector del blog normas-apa.org»
- **Paráfrasis:** La guía del repositorio es un resumen no oficial de la séptima edición elaborado a partir del blog normas-apa.org; para casos no cubiertos debe consultarse el manual oficial.
- **Uso sugerido:** Nota metodológica sobre la norma de redacción adoptada

**apaguia-02** · PDF p. 6 · cita: p. 6 · Actualizaciones 7.ª ed. · *requisito_normativo*
> «Use et al. en todas las citas de un trabajo con tres o más autores, siempre que no haya ambigüedad con respecto a la fuente»
- **Paráfrasis:** En la séptima edición, «et al.» se usa desde la primera cita para obras de tres o más autores, salvo ambigüedad.
- **Uso sugerido:** Redacción de todos los capítulos (citas en el texto)

**apaguia-03** · PDF p. 26 · cita: p. 26 · Formato: tamaño de papel · *requisito_normativo*
> «La configuración del tamaño de página en Word debe ser Tamaño Carta, que tiene las medidas de 21.59 cm x 27.94 cm (equivalente a 8 1/2 x 11 pulgadas).»
- **Paráfrasis:** El papel es tamaño carta (21,59 × 27,94 cm).
- **Uso sugerido:** Formato general de la tesis (plantilla LaTeX: preambulo.tex)

**apaguia-04** · PDF p. 26 · cita: p. 26 · Formato: márgenes · *requisito_normativo*
> «El tamaño de los márgenes en formato APA debe ser de 2.54 cm (equivalente a 1 pulgada) de todos los lados.»
- **Paráfrasis:** Los márgenes son de 2,54 cm en los cuatro lados.
- **Uso sugerido:** Formato general de la tesis (plantilla LaTeX: preambulo.tex)

**apaguia-05** · PDF p. 26 · cita: p. 26 · Formato: tipo y tamaño de fuente · *requisito_normativo*
> «Debes utilizar el mismo tipo y tamaño de fuente en todo el documento, incluso en los títulos y subtítulos, con las siguientes excepciones:»
- **Paráfrasis:** Se usa una sola fuente en todo el documento, incluidos los títulos (por ejemplo, Times New Roman 12; también se admiten Calibri 11, Arial 11, Georgia 11 o Computer Modern 10), con excepciones para figuras, código y notas al pie.
- **Uso sugerido:** Formato general de la tesis (plantilla LaTeX: preambulo.tex)

**apaguia-06** · PDF p. 27 · cita: p. 27 · Formato: encabezado · *requisito_normativo*
> «Para los trabajos de los estudiantes, el encabezado de la página consiste únicamente en el número de la página.»
- **Paráfrasis:** En trabajos de estudiantes el encabezado lleva solo el número de página, sin título abreviado.
- **Uso sugerido:** Formato general de la tesis (plantilla LaTeX: preambulo.tex)

**apaguia-07** · PDF p. 27 · cita: p. 27 · Formato: numeración de páginas · *requisito_normativo*
> «Debes utilizar la función de numeración de páginas de Word para insertar números de página. • La numeración debe estar ubicada en la esquina superior derecha.»
- **Paráfrasis:** Los números de página van en la esquina superior derecha, en todas las páginas, y la portada es la página 1 (p. 28).
- **Uso sugerido:** Formato general de la tesis (plantilla LaTeX: preambulo.tex)

**apaguia-08** · PDF p. 28 · cita: p. 28 · Títulos y subtítulos · *requisito_normativo*
> «Nota que en la séptima edición, todos los niveles de título van en negrita y todos van con cada palabra del título iniciando en mayúscula (Capitalización de Títulos).»
- **Paráfrasis:** Se admiten hasta cinco niveles de título; en la séptima edición todos van en negrita y con mayúscula inicial en cada palabra; el nivel 1 va centrado, los niveles 2 y 3 a la izquierda (el 3 en cursiva) y los niveles 4 y 5 sangrados y con punto final (p. 29).
- **Uso sugerido:** Formato general de la tesis (plantilla LaTeX: preambulo.tex)

**apaguia-09** · PDF p. 29 · cita: p. 29 · Títulos: advertencias · *requisito_normativo*
> «No etiquete los títulos y subtítulos con números o letras;»
- **Paráfrasis:** La guía recomienda no numerar los títulos; la tesis se aparta de esta recomendación porque la estructura del docente exige capítulos y secciones numerados, lo que conviene declarar en la nota de formato.
- **Uso sugerido:** Formato general de la tesis (plantilla LaTeX: preambulo.tex) (excepción justificada: el docente exige capítulos y secciones numerados)

**apaguia-10** · PDF p. 30 · cita: p. 30 · Interlineado · *requisito_normativo*
> «Como regla general siempre utilizaremos interlineado doble, incluyendo el resumen, texto de citas de más de 40 palabras, números de tablas y figuras, títulos y subtítulos y en la lista de referencias.»
- **Paráfrasis:** El interlineado es doble en todo el documento, incluidos resumen, citas en bloque, títulos y referencias; el cuerpo de tablas y figuras puede ir a espacio sencillo, 1,5 o doble (p. 31).
- **Uso sugerido:** Formato general de la tesis (plantilla LaTeX: preambulo.tex)

**apaguia-11** · PDF p. 31 · cita: p. 31 · Alineación · *requisito_normativo*
> «Utilices alineación a la izquierda en todo el documento. Es decir, el margen derecho quedará “irregular”. No utilices justificación de texto, al menos que tu universidad te solicite lo contrario.»
- **Paráfrasis:** El texto se alinea a la izquierda con margen derecho irregular; no se justifica salvo exigencia de la universidad.
- **Uso sugerido:** Formato general de la tesis (plantilla LaTeX: preambulo.tex)

**apaguia-12** · PDF p. 32 · cita: p. 32 · Sangría de párrafo · *requisito_normativo*
> «La primera línea de cada párrafo del texto debe tener un sangrado de ½ pulg. (1,27 cm) desde el margen izquierdo.»
- **Paráfrasis:** La primera línea de cada párrafo lleva sangría de 1,27 cm; las citas en bloque se sangran 1,27 cm completas.
- **Uso sugerido:** Formato general de la tesis (plantilla LaTeX: preambulo.tex)

**apaguia-13** · PDF p. 33 · cita: p. 33 · Sangría francesa · *requisito_normativo*
> «lista de referencias: las entradas de la lista de referencias bibliográficas deben tener una sangría francesa de ½ pulg. (1,27 cm).»
- **Paráfrasis:** Cada entrada de la lista de referencias lleva sangría francesa de 1,27 cm (también en p. 46); en LaTeX se fija con \bibhang = 1,27 cm.
- **Uso sugerido:** Bibliografía (lista de referencias; biblatex-apa)

**apaguia-14** · PDF p. 18 · cita: p. 18 · Tablas: número y título · *requisito_normativo*
> «número de tabla: el número de la tabla (por ejemplo, Tabla 1) es lo primero que aparece. Utilice negrita. Numere las tablas en el orden en que se mencionan en su investigación.»
- **Paráfrasis:** Cada tabla se identifica con su número en negrita (Tabla 1, Tabla 2…), en el orden en que se menciona, y debajo lleva un título breve y descriptivo en cursiva.
- **Uso sugerido:** Tablas y figuras de todos los capítulos

**apaguia-15** · PDF p. 18 · cita: p. 18 · Tablas: bordes · *requisito_normativo*
> «En general, se usa un borde en la parte superior e inferior de la tabla, debajo de los encabezados de columna y encima de los totales de columna. No utilice bordes verticales para separar los datos»
- **Paráfrasis:** Las tablas solo llevan líneas horizontales (arriba, bajo los encabezados, sobre los totales y al final) y nunca bordes verticales ni alrededor de cada celda.
- **Uso sugerido:** Tablas y figuras de todos los capítulos (booktabs en LaTeX)

**apaguia-16** · PDF p. 18 · cita: p. 18 · Tablas: nota · *requisito_normativo*
> «nota: utilice las notas para describir los contenidos de la tabla que no pueden entenderse solo con el título o con los mismos datos.»
- **Paráfrasis:** Las notas de tabla explican abreviaturas, fuentes o derechos de autor que no se entienden con el título o los datos.
- **Uso sugerido:** Tablas y figuras de todos los capítulos (nota de fuente: «Elaborado con datos de…»)

**apaguia-17** · PDF p. 20 · cita: p. 20 · Tablas y figuras: llamada en el texto · *requisito_normativo*
> «Al citar una tabla o una figura en el texto, debes hacerlo por su número, como “Tabla 3” o “Figura 2”.»
- **Paráfrasis:** Las tablas y figuras se mencionan en el texto por su número, nunca por su posición («la tabla siguiente») ni por la página.
- **Uso sugerido:** Tablas y figuras de todos los capítulos

**apaguia-18** · PDF p. 20 · cita: p. 20 · Figuras · *definicion*
> «Todos los tipos de elementos visuales que no sean tablas se consideran figuras en el estilo APA.»
- **Paráfrasis:** Todo elemento visual que no sea tabla (planos, fotografías, gráficos, diagramas) es una figura y sigue el mismo esquema: número en negrita, título en cursiva, imagen, leyenda y nota.
- **Uso sugerido:** Tablas y figuras de todos los capítulos

**apaguia-19** · PDF p. 22 · cita: p. 22 · Figuras: derechos de autor · *requisito_normativo*
> «Si está adaptando o reproduciendo una tabla o figura que fue publicada originalmente por otra persona, deberás proporcionar una declaración de derechos de autor debajo de la tabla o figura»
- **Paráfrasis:** Al reproducir o adaptar una tabla o figura ajena se coloca debajo una nota con la atribución («Adaptado de…») y se incluye la referencia correspondiente.
- **Uso sugerido:** Tablas y figuras de todos los capítulos (planos y cortes tomados del expediente)

**apaguia-20** · PDF p. 23 · cita: p. 23 · Figuras de elaboración propia · *requisito_normativo*
> «Cuando la figura es de elaboración propia no es necesario agregar ningún tipo de declaración de derechos de autor.»
- **Paráfrasis:** Las figuras de elaboración propia no requieren declaración de derechos de autor.
- **Uso sugerido:** Tablas y figuras de todos los capítulos

**apaguia-21** · PDF p. 36 · cita: p. 36 · Citas: número de página · *requisito_normativo*
> «Siempre que vayamos a citar debemos informar autor, el año y número de página.»
- **Paráfrasis:** Toda cita textual informa autor, año y número de página, ya sea en forma narrativa o entre paréntesis.
- **Uso sugerido:** Redacción de todos los capítulos (citas en el texto)

**apaguia-22** · PDF p. 39 · cita: p. 39 · Paráfrasis: número de página · *requisito_normativo*
> «Es recomendado, pero no obligatorio como en la cita directa, que proporciones el número de página (o párrafo para materiales no paginados)»
- **Paráfrasis:** En la paráfrasis el número de página es recomendable pero no obligatorio; conviene darlo en textos largos como normas y libros.
- **Uso sugerido:** Redacción de todos los capítulos (citas en el texto)

**apaguia-23** · PDF p. 41 · cita: p. 41 · Cita textual corta (< 40 palabras) · *requisito_normativo*
> «Si la cita tiene menos de 40 palabras, incorpórela en el texto y encierre la cita con comillas dobles.»
- **Paráfrasis:** Las citas de menos de 40 palabras se integran al párrafo entre comillas dobles, con autor, año y página.
- **Uso sugerido:** Redacción de todos los capítulos (citas en el texto)

**apaguia-24** · PDF p. 43 · cita: p. 43 · Cita en bloque (> 40 palabras) · *requisito_normativo*
> «Las citas de más de 40 palabras se escriben aparte del texto, con sangría, sin comillas, sin cursiva y con interlineado doble. Al final de la cita se coloca el punto antes de los datos»
- **Paráfrasis:** Las citas de más de 40 palabras van en bloque aparte, sangradas 1,27 cm, sin comillas ni cursiva y a doble espacio, con el punto final antes de la referencia entre paréntesis.
- **Uso sugerido:** Redacción de todos los capítulos (citas en el texto)

**apaguia-25** · PDF p. 43 · cita: p. 43 · Cita en bloque: fuente · *requisito_normativo*
> «Al final de una cita en bloque, cite la fuente y el número de página o párrafo entre paréntesis después del signo de puntuación final.»
- **Paráfrasis:** En la cita en bloque, la fuente y la página van entre paréntesis después del punto final.
- **Uso sugerido:** Redacción de todos los capítulos (citas en el texto)

**apaguia-26** · PDF p. 37 · cita: p. 37 · Autor corporativo · *requisito_normativo*
> «Cuando se trate de una organización que no sea muy conocida, debes escribir el nombre completo en la primera cita e inserte la abreviatura entre paréntesis/corchetes después del nombre completo.»
- **Paráfrasis:** Con autores corporativos poco conocidos se escribe el nombre completo en la primera cita con la sigla entre corchetes y después solo la sigla.
- **Uso sugerido:** Redacción de todos los capítulos (citas en el texto) (p. ej., Ministerio de Economía y Finanzas Públicas [MEFP], 2022; luego MEFP, 2022)

**apaguia-27** · PDF p. 38 · cita: p. 38 · Citas secundarias · *requisito_normativo*
> «Si es posible encuentre la fuente primaria, léala y cítela directamente en lugar de citar una fuente secundaria.»
- **Paráfrasis:** Debe buscarse y citarse la fuente primaria; la cita secundaria («como se citó en») es excepcional.
- **Uso sugerido:** Redacción de todos los capítulos (citas en el texto) (coincide con la regla del Taller 2: no citar de segunda mano)

**apaguia-28** · PDF p. 38 · cita: p. 38 · Comunicaciones personales · *definicion*
> «Son consideradas comunicaciones personales cartas privadas, comunicaciones electrónicas (como el e-mail o mensajes de grupos de WhatsApp), entrevistas personales, conversaciones telefónicas y similares.»
- **Paráfrasis:** Son comunicaciones personales las cartas privadas, correos, mensajes, entrevistas y conversaciones no recuperables por el lector.
- **Uso sugerido:** Redacción de todos los capítulos (citas en el texto)

**apaguia-29** · PDF p. 39 · cita: p. 39 · Comunicaciones personales · *requisito_normativo*
> «Como estos datos, por lo general no son recuperables, las comunicaciones personales no se incluyen en la lista de referencias.»
- **Paráfrasis:** Las comunicaciones personales se citan solo en el texto, con iniciales, apellido y fecha exacta, y no van en la lista de referencias.
- **Uso sugerido:** Redacción de todos los capítulos (citas en el texto) | Bibliografía (lista de referencias; biblatex-apa)

**apaguia-30** · PDF p. 45 · cita: p. 45 · Lista de referencias: formato · *requisito_normativo*
> «La lista de referencias debe iniciar en una nueva página separada del texto. El título de esta página debe ser “Referencias” y debe estar centrado en la parte superior de la página.»
- **Paráfrasis:** La lista de referencias empieza en página nueva, con el título centrado y en negrita, a doble espacio.
- **Uso sugerido:** Bibliografía (lista de referencias; biblatex-apa) (la tesis la titula «Bibliografía» por exigencia del docente)

**apaguia-31** · PDF p. 46 · cita: p. 46 · Elementos de una referencia · *requisito_normativo*
> «Cada entradas en una lista de referencia debe incluir los cuatro elementos básicos de una referencia: el autor, fecha de publicación, título del trabajo y fuente para recuperación.»
- **Paráfrasis:** Toda referencia contiene autor, fecha, título y fuente de recuperación (quién, cuándo, qué y dónde).
- **Uso sugerido:** Bibliografía (lista de referencias; biblatex-apa)

**apaguia-32** · PDF p. 47 · cita: p. 47 · Referencias con información incompleta · *requisito_normativo*
> «En muchos casos, no vamos a tener la referencia completa. Es decir, muchas veces nos faltará la fecha de publicación, el año, a veces no encontramos el autor de determinado texto en una página web.»
- **Paráfrasis:** La guía reconoce referencias con datos incompletos (sin fecha o sin autor) y remite a su tratamiento específico; en APA se usa «s. f.» cuando falta la fecha.
- **Uso sugerido:** Bibliografía (lista de referencias; biblatex-apa) (documentos inéditos del expediente sin fecha: «s. f.»)

**apaguia-33** · PDF p. 47 · cita: p. 47 · Orden y número de autores · *requisito_normativo*
> «La lista de referencias debe ser ordenada en alfabéticamente por el primer apellido del autor seguido de las iniciales del nombre del autor.»
- **Paráfrasis:** Las referencias se ordenan alfabéticamente por el apellido del primer autor; se listan hasta 20 autores.
- **Uso sugerido:** Bibliografía (lista de referencias; biblatex-apa)

**apaguia-34** · PDF p. 48 · cita: p. 48 · Páginas en la referencia · *requisito_normativo*
> «Se incluye un rango de páginas en una referencia cuando la fuente es parte de un trabajo paginado más grande, como un capítulo en un libro editado o un artículo en una publicación periódica»
- **Paráfrasis:** El rango de páginas va en la referencia solo cuando la fuente forma parte de una obra mayor (capítulo de libro editado o artículo de revista).
- **Uso sugerido:** Bibliografía (lista de referencias; biblatex-apa)

**apaguia-35** · PDF p. 49 · cita: p. 49 · Ejemplo: tesis · *requisito_normativo*
> «Martínez Ribón, J. G. T. (2011) Propuesta de metodología para la implementación de la filosofía Lean (construcción esbelta) en proyectos de construcción [Tesis de Maestría, Universidad Nacional de Colombia].»
- **Paráfrasis:** Las tesis se referencian con autor, año, título en cursiva, entre corchetes el grado y la universidad, y la URL del repositorio.
- **Uso sugerido:** Bibliografía (lista de referencias; biblatex-apa) (tesis de UMSA, UMSS, UCV, PUCP del repositorio)

**apaguia-36** · PDF p. 49 · cita: p. 49 · Ejemplo: artículo de revista · *requisito_normativo*
> «Castañeda Naranjo, L. A. y Palacios Neri, J. (2015). Nanotecnología: fuente de nuevos paradigmas. Mundo Nano. Revista Interdisciplinaria en Nanociencias y Nanotecnología, 7(12), 45-49.»
- **Paráfrasis:** Los artículos llevan autores, año, título del artículo, nombre de la revista en cursiva, volumen, número entre paréntesis, páginas y DOI.
- **Uso sugerido:** Bibliografía (lista de referencias; biblatex-apa)

**apaguia-37** · PDF p. 50 · cita: p. 50 · Ejemplo: leyes y documentos legales · *requisito_normativo*
> «Ley 1060 de 2006. Por la cual se modifican las normas que regulan la impugnación de la paternidad y la maternidad. 26 de julio de 2006. D.O. No. 46341.»
- **Paráfrasis:** El ejemplo de la guía (formato colombiano) da para las leyes: número y año, título u objeto, fecha completa y publicación oficial con su número; la tesis puede usar ese orden o el formato autor-fecha con el Estado como autor, de manera uniforme.
- **Uso sugerido:** Bibliografía (lista de referencias; biblatex-apa) (Ley 1178, D.S. 0181, D.S. 5597, etc.)

**apaguia-38** · PDF p. 50 · cita: p. 50 · Ejemplo: informes · *requisito_normativo*
> «Organización para la Cooperación y el Desarrollo Económico (2020). La dinámica de la urbanización de África 2020: Áfricapolis, mapeando una nueva geografía urbana.»
- **Paráfrasis:** Los informes se referencian con autor corporativo, año, título en cursiva, serie o editorial y DOI o URL.
- **Uso sugerido:** Bibliografía (lista de referencias; biblatex-apa) (informes de Supervisión, planillas y certificados como documentos institucionales)

**apaguia-39** · PDF p. 57 · cita: p. 57 · Referencia del manual oficial · *dato*
> «American Psychological Association. (2020). Publication manual of the American Psychological Association (7th ed.).»
- **Paráfrasis:** La guía se basa en el Manual de publicaciones de la APA, 7.ª edición (2020), que es la fuente para los casos no cubiertos (conjuntos de datos, documentos inéditos, normas técnicas).
- **Uso sugerido:** Bibliografía (lista de referencias; biblatex-apa) (para los casos que la guía no cubre)

### Tabla de reglas APA 7 que afectan a la tesis (regla → página de la guía)

| Regla | Qué exige la guía | Página(s) |
|---|---|---|
| Tamaño de papel | Carta, 21,59 × 27,94 cm | p. 26 |
| Márgenes | 2,54 cm en los cuatro lados | p. 26 |
| Fuente | Una sola fuente: Times New Roman 12 (o Calibri 11, Arial 11, Georgia 11, Computer Modern 10); excepciones en figuras, código y notas | pp. 5, 26–27 |
| Encabezado | Estudiantes: solo número de página; título corto (≤ 50 caracteres, mayúsculas) solo en trabajos profesionales | pp. 27–28 |
| Numeración de páginas | Arriba a la derecha, en todas las páginas; la portada es la 1 | pp. 27–28 |
| Portada de estudiante | Título, autor, afiliación (universidad), curso, docente y fecha | p. 7; título de unas 12 palabras, p. 9 |
| Resumen | 150–250 palabras, un solo párrafo sin sangría, palabras clave en cursiva | pp. 12–13 |
| Niveles de título | Hasta 5 niveles, todos en negrita y con mayúscula inicial; N1 centrado, N2 izquierda, N3 izquierda cursiva, N4–N5 sangrados con punto | pp. 28–29 |
| Numeración de títulos | La guía pide no numerarlos (la tesis los numera por exigencia del docente) | p. 29 |
| Interlineado | Doble en todo (incluye resumen, citas en bloque, títulos y referencias); tablas y figuras pueden ir a 1 o 1,5 | pp. 30–31 |
| Alineación | A la izquierda, sin justificar; sin guiones automáticos | pp. 31–32 |
| Sangría de párrafo | 1,27 cm en la primera línea | p. 32 |
| Tablas | Número en negrita, título en cursiva, encabezados de columna, solo bordes horizontales, notas; misma fuente; tablas largas repiten encabezados | pp. 17–19 |
| Llamada a tablas y figuras | Por su número («Tabla 3»), no por su posición ni página | p. 20 |
| Figuras | Todo lo que no es tabla; número, título, imagen, leyenda y nota | pp. 20–21 |
| Derechos de autor de figuras/tablas ajenas | Nota «Adaptado de…» y entrada en referencias; las propias no la requieren | pp. 22–23 |
| Notas al pie | Pie o final; fuente menor e interlineado sencillo permitidos | pp. 15–17, 31 |
| Apéndices | «Apéndice» o «Apéndice A, B…», cada uno en página nueva tras las referencias (en la tesis: Anexos) | pp. 23–25 |
| Sistema de citas | Autor-fecha; toda cita en el texto debe estar en las referencias | p. 34 |
| Cita textual con número de página | Siempre autor, año y página | pp. 36, 40–41 |
| Cita de menos de 40 palabras | Dentro del párrafo, entre comillas dobles | pp. 41–42 |
| Cita de más de 40 palabras | En bloque, sangría 1,27 cm, sin comillas, doble espacio, punto antes de la referencia | pp. 32, 43 |
| Paráfrasis | Autor y año obligatorios; página recomendada | pp. 39–40 |
| et al. | Desde la primera cita con tres o más autores | p. 6 |
| Autor corporativo | Nombre completo y sigla entre corchetes en la primera cita; luego la sigla | p. 37 |
| Cita secundaria | Excepcional, «como se citó en»; preferir la fuente primaria | p. 38 |
| Comunicaciones personales | Solo en el texto (iniciales, apellido, fecha); no van en referencias | pp. 38–39, 45, 54 |
| Lista de referencias | Página nueva, título centrado en negrita, doble espacio, orden alfabético | pp. 45, 47 |
| Sangría francesa | 1,27 cm en cada entrada | pp. 33, 46 |
| Elementos de la referencia | Autor, fecha, título y fuente | p. 46 |
| Información incompleta | Sin fecha («s. f.») o sin autor: tratamiento específico | p. 47 |
| Número de autores | Hasta 20 en la referencia | p. 47 |
| Libro | Autor, año, título en cursiva, editorial (sin ciudad en la 7.ª ed.) | pp. 6, 48 |
| Artículo de revista | Revista en cursiva, volumen(número), páginas, DOI | p. 49 |
| Tesis | [Tesis de maestría/licenciatura, Universidad] y URL | p. 49 |
| Leyes y documentos legales | Número y año, título, fecha, publicación oficial y número | p. 50 |
| Informes | Autor corporativo, año, título, editorial, DOI/URL | p. 50 |
| Archivo PDF | Descripción [Archivo PDF] y URL | p. 50 |
| Conjuntos de datos | **No figura en la guía**; aplicar el manual APA 7 (p. 57): autor, año, *título* [Conjunto de datos], editor, URL (p. ej., datos del INE) | — |
| Documentos inéditos (planillas, informes de Supervisión, certificados) | **No figura en la guía**; aplicar el manual APA 7: autor (institución), año o «s. f.», *título* [descripción: documento inédito], institución | — |
| Normas técnicas (ISO, ASTM, NB, ACI) | **No figura en la guía**; aplicar el manual APA 7: organismo, año, *título* (designación de la norma), URL si existe | — |


## 5. Ley N.º 1178 de Administración y Control Gubernamentales (SAFCO), 1990

- **Archivo:** `04_Bibliografia/06_Legislacion_Bolivia/Bolivia_Ley1178_1990_SAFCO_Texto_WIPOLex.pdf`
- **Clave BibLaTeX:** `ley1178_1990`
- **Referencia (APA 7):** República de Bolivia. (1990, 20 de julio). *Ley N.º 1178 de Administración y Control Gubernamentales*. Texto consultado en WIPO Lex (Organización Mundial de la Propiedad Intelectual).

- **Fuente del texto:** versión de WIPO Lex; no lleva números de página (se cita por artículo, «s. p.») ni número de Gaceta Oficial, que por eso no se consigna. Sancionada por el Congreso Nacional el 09/07/1990 y promulgada el 20/07/1990 por Jaime Paz Zamora (PDF 18). Se usa como autor «República de Bolivia», denominación del Estado en 1990.
- El texto de 1990 nombra a la «Contraloría General de la República»; el modelo de contrato del DBC 2022 ya la denomina «Contraloría General del Estado» (cláusula cuadragésima primera).
- **Uso prudente:** los artículos sobre responsabilidad civil (art. 31) alcanzan también a particulares que causen daño al Estado; en la tesis solo deben vincularse a las inconsistencias del cómputo del acero como marco de lo que la Supervisión y la Fiscalización deben verificar, nunca como imputación.

**ley1178_1990-01** · PDF p. 1 · cita: s. p. · Art. 1, inc. c) · *requisito_normativo*
> «Lograr que todo servidor público, sin distinción de jerarquía, asuma plena responsabilidad por sus actos rindiendo cuenta no sólo de los objetivos a que se destinaron los recursos públicos que le fueron confiados, sino también de la forma y resultado de su aplicación»
- **Paráfrasis:** Uno de los fines de la Ley 1178 es que todo servidor público rinda cuentas tanto del destino de los recursos públicos confiados como de la forma y el resultado de su uso.
- **Uso sugerido:** Cap.1 marco legal (responsabilidad por la función pública de Fiscal y Supervisor) | Cap.3 Discusión (inconsistencias documentales a verificar)

**ley1178_1990-02** · PDF p. 4 · cita: s. p. · Art. 10 · *requisito_normativo*
> «El Sistema de Administración de Bienes y Servicios establecerá la forma de contratación, manejo y disposición de bienes y servicios.»
- **Paráfrasis:** La Ley 1178 crea el Sistema de Administración de Bienes y Servicios, que regula la contratación, el manejo y la disposición de bienes y servicios; su norma básica es el D.S. 0181 (NB-SABS).
- **Uso sugerido:** Cap.1 marco legal (origen del SABS y de las NB-SABS)

**ley1178_1990-03** · PDF p. 4 · cita: s. p. · Art. 10, inc. a) · *requisito_normativo*
> «identificará a los responsables de la decisión de contratación con relación a la calidad, oportunidad y competitividad del precio del suministro, incluyendo los efectos de los términos de pago.»
- **Paráfrasis:** El SABS debe identificar a los responsables de las decisiones de contratación respecto de la calidad, la oportunidad y el precio de lo contratado.
- **Uso sugerido:** Cap.1 marco legal (calidad como responsabilidad en la contratación pública)

**ley1178_1990-04** · PDF p. 6 · cita: s. p. · Art. 13 · *requisito_normativo*
> «El Control Gubernamental tendrá por objetivo mejorar la eficiencia en la captación y uso de los recursos públicos y en las operaciones del Estado; la confiabilidad de la información que se genere sobre los mismos»
- **Paráfrasis:** El control gubernamental busca mejorar la eficiencia en el uso de los recursos públicos y la confiabilidad de la información que se genera sobre ellos.
- **Uso sugerido:** Cap.1 marco legal (control gubernamental) | Cap.2 articulación del SGC con el control interno de la UATF

**ley1178_1990-05** · PDF p. 6 · cita: s. p. · Art. 13, inc. a) · *requisito_normativo*
> «El Sistema de Control Interno que comprenderá los instrumentos de control previo y posterior incorporados en el plan de organización y en los reglamentos y manuales de procedimientos de cada entidad, y la auditoria interna»
- **Paráfrasis:** El control interno se compone de controles previos y posteriores incorporados en la organización, los reglamentos y los manuales de procedimientos de cada entidad, además de la auditoría interna; los procedimientos del SGC pueden integrarse como controles de este tipo.
- **Uso sugerido:** Cap.1 marco legal (control gubernamental) | Cap.2 articulación del SGC con el control interno de la UATF

**ley1178_1990-06** · PDF p. 6 · cita: s. p. · Art. 14 · *requisito_normativo*
> «Los procedimientos de control interno previo se aplicarán por todas las unidades de la entidad antes de la ejecución de sus operaciones y actividades o de que sus actos causen efecto.»
- **Paráfrasis:** El control interno previo se aplica antes de ejecutar las operaciones o de que los actos surtan efecto, lógica equivalente a los puntos de espera del plan de inspección y ensayos.
- **Uso sugerido:** Cap.1 marco legal (control gubernamental) | Cap.2 articulación del SGC con el control interno de la UATF (control previo = puntos de espera del PPI)

**ley1178_1990-07** · PDF p. 10 · cita: s. p. · Art. 28, inc. a) · *requisito_normativo*
> «Todo servidor público respondera de los resultados emergentes del desempeño de las funciones, deberes y atribuciones asignados a su cargo. A este efecto: a) La responsabilidad administrativa, ejecutiva, civil y penal se determinará tomando en cuenta los resultados de la acción u omisión.»
- **Paráfrasis:** Todo servidor público responde por los resultados de sus funciones, y su responsabilidad administrativa, ejecutiva, civil o penal se determina según los resultados de su acción u omisión.
- **Uso sugerido:** Cap.1 marco legal (responsabilidad por la función pública de Fiscal y Supervisor) | Cap.3 Discusión (inconsistencias documentales a verificar)
- **Nota:** La capa de texto dice «respondera» (sin tilde); al citar puede añadirse [sic] o escribir «responderá».

**ley1178_1990-08** · PDF p. 11 · cita: s. p. · Art. 29 · *definicion*
> «La responsabilidad es administrativa cuando la acción u omisión contraviene el ordenamiento jurídico-administrativo y las normas que regulan la conducta funcionaria del servidor público.»
- **Paráfrasis:** La responsabilidad administrativa surge cuando la acción u omisión del servidor público contraviene el ordenamiento jurídico-administrativo o las normas de conducta funcionaria.
- **Uso sugerido:** Cap.1 marco legal (responsabilidad por la función pública de Fiscal y Supervisor) | Cap.3 Discusión (inconsistencias documentales a verificar)

**ley1178_1990-09** · PDF p. 11 · cita: s. p. · Art. 30 · *definicion*
> «cuando se encuentre que las deficiencias o negligencia de la gestión ejecutiva son de tal magnitud que no permiten lograr, dentro de las circunstancias existentes, resultados razonables en términos de eficacia, eficiencia y economía.»
- **Paráfrasis:** Hay responsabilidad ejecutiva, entre otros casos, cuando las deficiencias de gestión impiden lograr resultados razonables de eficacia, eficiencia y economía.
- **Uso sugerido:** Cap.1 marco legal (responsabilidad por la función pública de Fiscal y Supervisor) | Cap.3 Discusión (inconsistencias documentales a verificar)

**ley1178_1990-10** · PDF p. 11 · cita: s. p. · Art. 31 · *definicion*
> «La responsabilidad es civil cuando la acción u omisión del Servidor público o de las personas naturales o jurídicas privadas cause daño al Estado valuable en dinero.»
- **Paráfrasis:** La responsabilidad civil se configura cuando la acción u omisión de un servidor público o de un particular causa al Estado un daño valuable en dinero.
- **Uso sugerido:** Cap.1 marco legal (responsabilidad por la función pública de Fiscal y Supervisor) | Cap.3 Discusión (inconsistencias documentales a verificar)

**ley1178_1990-11** · PDF p. 11 · cita: s. p. · Art. 31, inc. b) · *requisito_normativo*
> «Incurrirán en responsabilidad civil las personas naturales o jurídicas que no siendo servidores públicos, se beneficiaren indebidamente con recursos públicos o fueren causantes de daño al patrimonio del Estado y de sus entidades.»
- **Paráfrasis:** Los particulares, como los contratistas, también pueden incurrir en responsabilidad civil si se benefician indebidamente con recursos públicos o causan daño al patrimonio del Estado; de ahí la importancia de que la Supervisión verifique los cómputos pagados.
- **Uso sugerido:** Cap.1 marco legal (responsabilidad por la función pública de Fiscal y Supervisor) | Cap.3 Discusión (inconsistencias documentales a verificar)

**ley1178_1990-12** · PDF p. 16 · cita: s. p. · Art. 47 · *requisito_normativo*
> «Créase la jurisdicción coactiva fiscal para el conocimiento de todas las demandas que se interpongan con ocasión de los actos de los servidores públicos, de los distintos entes de derecho público o de las personas naturales o jurídicas privadas que hayan suscrito contratos administrativos con el Estado»
- **Paráfrasis:** La ley crea la jurisdicción coactiva fiscal para las demandas por responsabilidad civil derivadas de contratos administrativos, como los de obra; el modelo de contrato del DBC remite a ella para el cobro de saldos y multas.
- **Uso sugerido:** Cap.1 marco legal (vía de cobro de saldos y multas citada por el DBC)


## 6. D.S. N.º 0181 (NB-SABS), texto de 28 de junio de 2009 (Gaceta Oficial, texto de consulta)

- **Archivo:** `04_Bibliografia/06_Legislacion_Bolivia/Bolivia_DS0181_2009_NB-SABS_Texto_Original.pdf`
- **Clave BibLaTeX:** `ds0181_2009`
- **Referencia (APA 7):** Estado Plurinacional de Bolivia. (2009, 28 de junio). *Decreto Supremo N.º 0181: Normas Básicas del Sistema de Administración de Bienes y Servicios*. Gaceta Oficial del Estado Plurinacional de Bolivia.

- **Fuente:** «Texto de consulta» de la Gaceta Oficial del Estado Plurinacional de Bolivia (© 2014, PDF 152); sin paginación impresa (se cita por artículo, «s. p.») ni número de edición de la Gaceta. Firmado por Evo Morales Ayma el 28/06/2009; vigente desde el 15/07/2009.
- **Diferencia con el texto compilado 2025:** el art. 89 del texto de 2009 ya fija 10 % (contratos modificatorios), 5 % (órdenes de cambio) y 15 % (ambos, licitación pública); el párrafo que limita a 10 % la suma en la modalidad ANPE solo aparece en el texto compilado. Para la obra (licitación pública, contrato modificatorio de +7,22 %) los tres límites coinciden en ambas versiones.

**ds0181_2009-01** · PDF p. 6 · cita: s. p. · Art. 5, inc. c) · *definicion*
> «c) Caso Fortuito: Obstáculo interno atribuible al hombre, imprevisto o inevitable, relativas a las condiciones mismas en que la obligación debía ser cumplida (conmociones civiles, huelgas, bloqueos, revoluciones, etc.);»
- **Paráfrasis:** Las NB-SABS definen el caso fortuito como un obstáculo interno atribuible al hombre, imprevisto o inevitable (conmociones civiles, huelgas, bloqueos, revoluciones).
- **Uso sugerido:** Cap.1 marco legal (fuerza mayor y caso fortuito) | Cap.3 Discusión (paralización por el D.S. 5503)

**ds0181_2009-02** · PDF p. 7 · cita: s. p. · Art. 5, inc. p) · *definicion*
> «p) Fuerza Mayor: Obstáculo externo, imprevisto o inevitable que origina una fuerza extraña al hombre que impide el cumplimiento de la obligación (incendios, inundaciones y otros desastres naturales);»
- **Paráfrasis:** La fuerza mayor es un obstáculo externo, imprevisto o inevitable, ajeno al hombre (incendios, inundaciones u otros desastres naturales); la medida económica que motivó la paralización encaja mejor en la noción de caso fortuito que el D.S. 5597 utiliza (lectura propia a verificar con asesoría legal).
- **Uso sugerido:** Cap.1 marco legal (fuerza mayor y caso fortuito) | Cap.3 Discusión (carta notariada de 05/01/2026)

**ds0181_2009-03** · PDF p. 19 · cita: s. p. · Art. 21, inc. b) · *requisito_normativo*
> «Garantía de Cumplimiento de Contrato. Tiene por objeto garantizar la conclusión y entrega del objeto del contrato. Será equivalente al siete por ciento (7%) del monto del contrato.»
- **Paráfrasis:** La garantía de cumplimiento de contrato asegura la conclusión y entrega del objeto contratado y equivale al 7 % del monto del contrato.
- **Uso sugerido:** Cap.1 marco legal (garantías contractuales)

**ds0181_2009-04** · PDF p. 70 · cita: s. p. · Art. 89, parág. I · *requisito_normativo*
> «Las modificaciones al contrato deberán estar destinadas al cumplimiento del objeto de la contratación y ser sustentadas por informe técnico y legal que establezca la viabilidad técnica y de financiamiento.»
- **Paráfrasis:** Toda modificación contractual debe servir al cumplimiento del objeto del contrato y sustentarse en informes técnico y legal sobre su viabilidad técnica y financiera.
- **Uso sugerido:** Cap.1 marco legal (modificaciones contractuales) | Cap.3 Discusión (contrato modificatorio de +7,22 %)

**ds0181_2009-05** · PDF p. 70 · cita: s. p. · Art. 89, parág. II, inc. a) · *requisito_normativo*
> «Se podrán realizar uno o varios contratos modificatorios, que sumados no deberán exceder el diez por ciento (10%) del monto del contrato principal.»
- **Paráfrasis:** Los contratos modificatorios, sumados, no pueden superar el 10 % del monto del contrato principal; el incremento de la obra (+7,22 %) queda dentro de ese límite (cálculo del expediente).
- **Uso sugerido:** Cap.1 marco legal (modificaciones contractuales) | Cap.3 Discusión (contrato modificatorio de +7,22 %)

**ds0181_2009-06** · PDF p. 71 · cita: s. p. · Art. 89, parág. II, inc. d) · *requisito_normativo*
> «La Orden de Cambio deberá ser aprobada por la instancia responsable del seguimiento de la obra en la entidad y no podrá exceder el cinco por ciento (5%) del monto del contrato principal.»
- **Paráfrasis:** La orden de cambio la aprueba la instancia responsable del seguimiento de la obra y no puede superar el 5 % del monto del contrato principal.
- **Uso sugerido:** Cap.1 marco legal (modificaciones contractuales) | Cap.3 Discusión (contrato modificatorio de +7,22 %)

**ds0181_2009-07** · PDF p. 71 · cita: s. p. · Art. 89, parág. II, inc. d) · *requisito_normativo*
> «En la modalidad de Licitación Pública, cuando además de realizarse Órdenes de Cambio se realicen Contratos Modificatorios, sumados no deberán exceder el quince por ciento (15%) del monto del contrato principal.»
- **Paráfrasis:** En licitación pública, órdenes de cambio y contratos modificatorios sumados no pueden exceder el 15 % del monto del contrato principal.
- **Uso sugerido:** Cap.1 marco legal (modificaciones contractuales) | Cap.3 Discusión (contrato modificatorio de +7,22 %)

**ds0181_2009-08** · PDF p. 140 · cita: s. p. · Disposición final tercera · *dato*
> «Las presentes NB-SABS entrarán en vigencia el 15 de julio de 2009, conjuntamente la reglamentación que será elaborada y aprobada por el Órgano Rector, mediante Resolución Ministerial»
- **Paráfrasis:** Las NB-SABS rigen desde el 15 de julio de 2009, junto con la reglamentación que el Órgano Rector aprueba por resolución ministerial (como los modelos de DBC).
- **Uso sugerido:** Cap.1 marco legal


## 7. NB-SABS: texto compilado del MEFP actualizado a 2025 (D.S. 0181 y sus modificaciones)

- **Archivo:** `04_Bibliografia/06_Legislacion_Bolivia/Bolivia_DS0181_2025_NB-SABS_Texto_Compilado_MEFP.pdf`
- **Clave BibLaTeX:** `ds0181_2025compilado`
- **Referencia (APA 7):** Ministerio de Economía y Finanzas Públicas. (2025). *NB-SABS: Decreto Supremo N.º 0181, Decreto Supremo N.º 1497, Decreto Supremo N.º 4453, Reglamento del RUPE, Reglamento de Contrataciones con Apoyo de Medios Electrónicos y Manual de Operaciones del SICOES* (texto compilado, actualizado 2025). Distribución gratuita.

- **Paginación:** el número impreso coincide con la página del PDF (PDF 92 → p. 92). El compilado incorpora las modificaciones hasta el D.S. N.º 5423 de 09/07/2025 (lista en PDF 13); no incluye el D.S. 5600 de 2026, que derogó el art. 83 bis.
- **Lo que la NB-SABS no contiene:** no define «Supervisor» ni «Fiscal de Obra» ni regula el Libro de Órdenes, los ensayos o las planillas: esas figuras están en el modelo de contrato del DBC (ficha 14). Tampoco detalla el procedimiento de resolución; solo prevé la contratación por excepción ante una resolución (art. 65 c) y el registro de la resolución en el SICOES (Manual de Operaciones).
- **Art. 89 (texto vigente):** contrato modificatorio ≤ 10 %; orden de cambio ≤ 5 %; ambos ≤ 15 % en licitación pública y ≤ 10 % en ANPE. Los D.S. 5321/5406 y 5597 permiten superar excepcionalmente estos porcentajes para ajustes de precios.

**ds0181_2025compilado-01** · PDF p. 20 · cita: p. 20 · Art. 5, inc. c) · *definicion*
> «c) Caso Fortuito: Obstáculo interno atribuible al hombre, imprevisto o inevitable, relativas a las condiciones mismas en que la obligación debía ser cumplida (conmociones civiles, huelgas, bloqueos, revoluciones, etc.);»
- **Paráfrasis:** El caso fortuito es un obstáculo interno atribuible al hombre, imprevisto o inevitable, como conmociones civiles, huelgas o bloqueos (definición vigente en el texto compilado).
- **Uso sugerido:** Cap.1 marco conceptual (definiciones legales) | Cap.3 Discusión (paralización de 05/01/2026)

**ds0181_2025compilado-02** · PDF p. 22 · cita: p. 22 · Art. 5, inc. p) · *definicion*
> «p) Fuerza Mayor: Obstáculo externo, imprevisto o inevitable que origina una fuerza extraña al hombre que impide el cumplimiento de la obligación (incendios, inundaciones y otros desastres naturales);»
- **Paráfrasis:** La fuerza mayor es un obstáculo externo e inevitable, ajeno al hombre, como incendios, inundaciones u otros desastres naturales.
- **Uso sugerido:** Cap.1 marco conceptual (definiciones legales) | Cap.3 Discusión (carta notariada por fuerza mayor)

**ds0181_2025compilado-03** · PDF p. 21 · cita: p. 21 · Art. 5, inc. j) · *definicion*
> «j) Contrato: Instrumento legal de naturaleza administrativa que regula la relación contractual entre la entidad contratante y el proveedor o contratista, estableciendo derechos, obligaciones y condiciones para la provisión de bienes, construcción de obras, prestación de servicios generales o servicios de consultoría;»
- **Paráfrasis:** El contrato público es un instrumento de naturaleza administrativa que fija derechos, obligaciones y condiciones entre la entidad y el contratista, también para la construcción de obras.
- **Uso sugerido:** Cap.1 marco conceptual (definiciones legales)

**ds0181_2025compilado-04** · PDF p. 21 · cita: p. 21 · Art. 5, inc. m) · *definicion*
> «m) Especificaciones Técnicas: Parte integrante del DBC, elaborada por la entidad contratante, donde se establecen las características técnicas de los bienes, obras o servicios generales a contratar;»
- **Paráfrasis:** Las especificaciones técnicas forman parte del DBC, las elabora la entidad contratante y fijan las características técnicas de la obra; por eso las normas que citan obligan contractualmente.
- **Uso sugerido:** Cap.1 marco conceptual (definiciones legales) | Cap.3 Discusión (ET de la losa que cita CBH-87 y NB antiguas)

**ds0181_2025compilado-05** · PDF p. 23 · cita: p. 23 · Art. 5, inc. aa) · *definicion*
> «aa) Modelo de Documento Base de Contratación – DBC: Documento estándar, elaborado y aprobado por el Órgano Rector, que forma parte de la reglamentación de las presentes NB-SABS y es de utilización obligatoria por las entidades públicas;»
- **Paráfrasis:** El modelo de DBC es un documento estándar aprobado por el Ministerio de Economía y Finanzas Públicas, forma parte de la reglamentación de las NB-SABS y su uso es obligatorio para las entidades públicas.
- **Uso sugerido:** Cap.1 marco conceptual (definiciones legales) (fundamento del uso del modelo de DBC)

**ds0181_2025compilado-06** · PDF p. 35 · cita: p. 35 · Art. 21, parág. I, inc. b) · *requisito_normativo*
> «b) Garantía de Cumplimiento de Contrato. Tiene por objeto garantizar la conclusión y entrega del objeto del contrato. Será equivalente al siete por ciento (7%) del monto del contrato.»
- **Paráfrasis:** La garantía de cumplimiento de contrato equivale al 7 % del monto contratado y asegura la conclusión y entrega de la obra.
- **Uso sugerido:** Cap.1 marco legal (garantías)

**ds0181_2025compilado-07** · PDF p. 36 · cita: p. 36 · Art. 21, parág. I, inc. b) · *requisito_normativo*
> «La vigencia de la garantía será computable a partir de la firma del contrato hasta la recepción definitiva del bien, obra, servicio general o servicio de consultoría.»
- **Paráfrasis:** La garantía de cumplimiento rige desde la firma del contrato hasta la recepción definitiva y se devuelve con la conformidad de esa recepción.
- **Uso sugerido:** Cap.1 marco legal (garantías)

**ds0181_2025compilado-08** · PDF p. 54 · cita: p. 54 · Art. 39, parág. II, inc. b) · *requisito_normativo*
> «Elaborar y firmar el Acta de Recepción o emitir el Informe de Conformidad, según corresponda, aspecto que no exime las responsabilidades del proveedor ni del supervisor respecto de la entrega del bien o servicio;»
- **Paráfrasis:** La firma del acta de recepción por la comisión no libera al contratista ni al supervisor de sus responsabilidades sobre lo entregado.
- **Uso sugerido:** Cap.1 marco legal (recepción de obras) | Cap.2 procedimiento de recepción y control

**ds0181_2025compilado-09** · PDF p. 54 · cita: p. 54 · Art. 39, parág. III · *requisito_normativo*
> «La recepción de bienes podrá estar sujeta a verificación, de acuerdo con sus características; la recepción de obras se realizará en dos etapas: provisional y definitiva, emitiéndose las actas respectivas»
- **Paráfrasis:** Las obras se reciben en dos etapas, provisional y definitiva, cada una con su acta.
- **Uso sugerido:** Cap.1 marco legal (recepción de obras) | Cap.2 procedimiento de recepción y control

**ds0181_2025compilado-10** · PDF p. 55 · cita: p. 55 · Art. 40, inc. d) · *requisito_normativo*
> «d) Iniciar procesos de contratación de obras, con planos o diseños no actualizados;»
- **Paráfrasis:** Se prohíbe a los servidores públicos iniciar contrataciones de obras con planos o diseños no actualizados, lo que respalda la exigencia de coherencia entre planos y especificaciones.
- **Uso sugerido:** Cap.1 marco legal | Cap.3 Discusión (discrepancias entre planos y ET)

**ds0181_2025compilado-11** · PDF p. 71 · cita: p. 71 · Art. 65, inc. c) · *requisito_normativo*
> «c) Ante la resolución de contrato por las causales establecidas en el mismo; la interposición de recurso o proceso no impedirá la contratación;»
- **Paráfrasis:** La resolución de un contrato por sus causales habilita la contratación por excepción para concluir el objeto, aunque existan recursos o procesos pendientes; es una vía para contratar el saldo de la obra.
- **Uso sugerido:** Cap.1 marco legal (resolución del contrato y saldo de obra) | Cap.3 Discusión (contrato paralizado y saldo de 2.234,60 m²)

**ds0181_2025compilado-12** · PDF p. 89 · cita: p. 89 · Art. 85 · *requisito_normativo*
> «ARTÍCULO 85.- (NATURALEZA). Los contratos que suscriben las entidades públicas para la provisión de bienes y servicios, son de naturaleza administrativa.»
- **Paráfrasis:** Los contratos que firman las entidades públicas, incluidos los de obra, son de naturaleza administrativa.
- **Uso sugerido:** Cap.1 marco legal

**ds0181_2025compilado-13** · PDF p. 90 · cita: p. 90 · Art. 87, incs. j)-l) · *requisito_normativo*
> «j) Multas y penalidades por incumplimiento de las partes; k) Condiciones para la entrega y recepción de los bienes y servicios, según corresponda; l) Terminación;»
- **Paráfrasis:** Todo contrato debe incluir, entre sus cláusulas mínimas, las multas y penalidades, las condiciones de entrega y recepción y la terminación.
- **Uso sugerido:** Cap.1 marco legal (contenido mínimo del contrato)

**ds0181_2025compilado-14** · PDF p. 91 · cita: p. 91 · Art. 89, parág. I · *requisito_normativo*
> «Las modificaciones al contrato deberán estar destinadas al cumplimiento del objeto de la contratación y ser sustentadas por informe técnico y»
- **Paráfrasis:** Las modificaciones contractuales deben destinarse a cumplir el objeto del contrato y sustentarse en informes técnico y legal de viabilidad técnica y financiera (el texto continúa en p. 92).
- **Uso sugerido:** Cap.1 marco legal (modificaciones contractuales) | Cap.3 Discusión (contrato modificatorio de +7,22 % e ítems nuevos por Bs 79.087,22)

**ds0181_2025compilado-15** · PDF p. 92 · cita: p. 92 · Art. 89, parág. II, inc. a) · *definicion*
> «Contrato Modificatorio. Es aplicable cuando la modificación a ser introducida afecte el alcance, monto y/o plazo del contrato, sin dar lugar al incremento de los precios unitarios.»
- **Paráfrasis:** El contrato modificatorio procede cuando cambia el alcance, el monto o el plazo, sin aumentar los precios unitarios.
- **Uso sugerido:** Cap.1 marco legal (modificaciones contractuales) | Cap.3 Discusión (contrato modificatorio de +7,22 % e ítems nuevos por Bs 79.087,22)

**ds0181_2025compilado-16** · PDF p. 92 · cita: p. 92 · Art. 89, parág. II, inc. a) · *requisito_normativo*
> «Se podrán realizar uno o varios contratos modificatorios, que sumados no deberán exceder el diez por ciento (10%) del monto del contrato principal.»
- **Paráfrasis:** Los contratos modificatorios, en conjunto, no pueden superar el 10 % del monto del contrato principal; el de la obra (+Bs 243.093,48; +7,22 %) cumple ese límite.
- **Uso sugerido:** Cap.1 marco legal (modificaciones contractuales) | Cap.3 Discusión (contrato modificatorio de +7,22 % e ítems nuevos por Bs 79.087,22)

**ds0181_2025compilado-17** · PDF p. 92 · cita: p. 92 · Art. 89, parág. II, inc. a) · *requisito_normativo*
> «Si para el cumplimiento del objeto del Contrato, fuese necesaria la creación de nuevos ítems (volúmenes o cantidades no previstas), los precios unitarios de estos ítems deberán ser negociados.»
- **Paráfrasis:** Si para cumplir el objeto se requieren ítems nuevos, sus precios unitarios deben negociarse; es el caso de los ítems nuevos del contrato modificatorio de la obra.
- **Uso sugerido:** Cap.1 marco legal (modificaciones contractuales) | Cap.3 Discusión (contrato modificatorio de +7,22 % e ítems nuevos por Bs 79.087,22)

**ds0181_2025compilado-18** · PDF p. 93 · cita: p. 93 · Art. 89, parág. II, inc. d) · *definicion*
> «Órdenes de Cambio. Se utilizará únicamente para la contratación de obras. Es aplicable cuando la modificación a ser introducida implique una modificación del precio del contrato o plazo del mismo, sin dar lugar al incremento de los precios unitarios ni creación de nuevos ítems.»
- **Paráfrasis:** La orden de cambio, exclusiva de obras, modifica el precio o el plazo sin aumentar precios unitarios ni crear ítems nuevos.
- **Uso sugerido:** Cap.1 marco legal (modificaciones contractuales) | Cap.3 Discusión (contrato modificatorio de +7,22 % e ítems nuevos por Bs 79.087,22)

**ds0181_2025compilado-19** · PDF p. 93 · cita: p. 93 · Art. 89, parág. II, inc. d) · *requisito_normativo*
> «La Orden de Cambio deberá ser aprobada por la instancia responsable del seguimiento de la obra en la entidad y no podrá exceder el cinco por ciento (5%) del monto del contrato principal.»
- **Paráfrasis:** Las órdenes de cambio las aprueba la instancia de seguimiento de la obra y no pueden superar el 5 % del monto del contrato principal.
- **Uso sugerido:** Cap.1 marco legal (modificaciones contractuales) | Cap.3 Discusión (contrato modificatorio de +7,22 % e ítems nuevos por Bs 79.087,22)

**ds0181_2025compilado-20** · PDF p. 93 · cita: p. 93 · Art. 89, parág. II, inc. d) · *requisito_normativo*
> «En la modalidad de Licitación Pública, cuando además de realizarse Órdenes de Cambio se realicen Contratos Modificatorios, sumados no deberán exceder el quince por ciento (15%) del monto del contrato principal.»
- **Paráfrasis:** En licitación pública, la suma de órdenes de cambio y contratos modificatorios no puede exceder el 15 % del monto del contrato principal.
- **Uso sugerido:** Cap.1 marco legal (modificaciones contractuales) | Cap.3 Discusión (contrato modificatorio de +7,22 % e ítems nuevos por Bs 79.087,22)

**ds0181_2025compilado-21** · PDF p. 93 · cita: p. 93 · Art. 89, parág. II, inc. d) · *requisito_normativo*
> «En la modalidad ANPE, cuando además de realizarse Órdenes de Cambio se realicen Contratos Modificatorios, sumados no deberán exceder el diez por ciento (10%) del monto del contrato principal.»
- **Paráfrasis:** En la modalidad ANPE el tope conjunto de órdenes de cambio y contratos modificatorios es del 10 % (párrafo que no figura en el texto de 2009).
- **Uso sugerido:** Cap.1 marco legal (modificaciones contractuales) | Cap.3 Discusión (contrato modificatorio de +7,22 % e ítems nuevos por Bs 79.087,22)

**ds0181_2025compilado-22** · PDF p. 93 · cita: p. 93 · Art. 89, parág. III · *requisito_normativo*
> «Procederá la cesión o la subrogación de contratos por causa de fuerza mayor, caso fortuito o necesidad pública, previa aprobación de la MAE de la entidad contratante.»
- **Paráfrasis:** Por fuerza mayor, caso fortuito o necesidad pública puede cederse o subrogarse el contrato con aprobación de la máxima autoridad de la entidad.
- **Uso sugerido:** Cap.1 marco legal (resolución del contrato y saldo de obra) | Cap.3 Discusión (contrato paralizado y saldo de 2.234,60 m²)

**ds0181_2025compilado-23** · PDF p. 264 · cita: p. 264 · Manual de Operaciones del SICOES (incluido en el compilado), num. 37.1 · *requisito_normativo*
> «37.1. Plazo de registro: Máximo veinte (20) días hábiles computables a partir de la fecha de resolución de Contrato, incumplimiento a la Orden de Compra u Orden de Servicio.»
- **Paráfrasis:** La entidad debe registrar en el SICOES la resolución del contrato (Formulario 600) dentro de los 20 días hábiles siguientes a la fecha de resolución.
- **Uso sugerido:** Cap.1 marco legal (resolución del contrato y saldo de obra) | Cap.3 Discusión (contrato paralizado y saldo de 2.234,60 m²)


## 8. D.S. N.º 5321 de 23 de enero de 2025 y su Anexo (ajuste de precios de materiales importados)

- **Archivo:** `04_Bibliografia/06_Legislacion_Bolivia/Bolivia_DS5321_2025_Ajuste_Precios_Materiales_Importados_Obras.pdf`
- **Clave BibLaTeX:** `ds5321_2025`
- **Referencia (APA 7):** Estado Plurinacional de Bolivia. (2025, 23 de enero). *Decreto Supremo N.º 5321: mecanismos operativos para el ajuste de precios unitarios de materiales de construcción, maquinaria y equipos, importados, en contratos de obra en ejecución*. Gaceta Oficial del Estado Plurinacional de Bolivia. http://www.gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/280603

- **Fuente:** texto de consulta de la Gaceta Oficial; sin paginación impresa ni número de edición (se cita por artículo). Firmado por Luis Alberto Arce Catacora el 23/01/2025. El Anexo es un archivo aparte (`Bolivia_DS5321_2025_Anexo_Materiales_Importados.pdf`) que forma parte del mismo decreto. La URL proviene de `bib/00_base.bib` (no figura en el PDF).
- **Cronología de la serie:** D.S. 5321 (plazo para el contrato modificatorio hasta el 30/05/2025) → D.S. 5406 (amplía a contratos llave en mano y extiende el plazo al 31/10/2025) → D.S. 5452 (redefine la fórmula y el ajuste en contratos llave en mano) → D.S. 5597 (2026, nuevo régimen hasta el 31/12/2026). Las fórmulas del D.S. 5321 son imágenes sin texto; su versión vigente está en el D.S. 5452 (ficha 10).
- **Relación con el caso:** el Anexo incluye el acero corrugado (ítem 8 de la obra) entre los materiales importados ajustables; no incluye cemento ni viguetas pretensadas.

**ds5321_2025-01** · PDF p. 1 · cita: s. p. · Art. 1 (Objeto) · *requisito_normativo*
> «el presente Decreto Supremo tiene por objeto establecer mecanismos operativos para el ajuste de precios unitarios de materiales de construcción, maquinaria y equipos, importados, así como otorgar un anticipo adicional para la adquisición de los mismos, en los contratos de obra en ejecución, suscritos por entidades públicas.»
- **Paráfrasis:** El D.S. 5321 creó, de forma excepcional, mecanismos para ajustar los precios unitarios de materiales, maquinaria y equipos importados y para otorgar anticipos adicionales en contratos de obra pública en ejecución.
- **Uso sugerido:** Introducción (contexto de crisis y alza de materiales) | Cap.1 marco legal (ajuste de precios) | Cap.3 Discusión (supuesto de precios constantes del modelo)

**ds5321_2025-02** · PDF p. 1 · cita: s. p. · Art. 3, parág. I · *requisito_normativo*
> «podrán efectuar el ajuste de precios unitarios de los materiales de construcción, maquinaria y equipos, importados, detallados en el Anexo del presente Decreto Supremo, a través de un contrato modificatorio que debe ser suscrito hasta el 30 de mayo de 2025.»
- **Paráfrasis:** El ajuste solo procedía para los materiales del Anexo y mediante un contrato modificatorio suscrito hasta el 30 de mayo de 2025 (plazo ampliado luego por el D.S. 5406).
- **Uso sugerido:** Introducción (contexto de crisis y alza de materiales) | Cap.1 marco legal (ajuste de precios) | Cap.3 Discusión (supuesto de precios constantes del modelo)

**ds5321_2025-03** · PDF p. 1 · cita: s. p. · Art. 3, parág. III · *metodo*
> «El ajuste de precios unitarios se realizará únicamente sobre el precio del material importado señalado en el numeral 1 (materiales) del Formulario B-2 (Análisis de Precios Unitarios) de la propuesta adjudicada o documento similar que incluya este tipo de información.»
- **Paráfrasis:** El ajuste afecta solo al precio del material importado consignado en el rubro de materiales del análisis de precios unitarios (Formulario B-2) de la propuesta.
- **Uso sugerido:** Introducción (contexto de crisis y alza de materiales) | Cap.1 marco legal (ajuste de precios) | Cap.3 Discusión (supuesto de precios constantes del modelo)

**ds5321_2025-04** · PDF p. 2 · cita: s. p. · Art. 4, parág. I · *requisito_normativo*
> «El ajuste de precios unitarios en los contratos de obra en ejecución será efectuado mediante contrato modificatorio, por única vez, pudiendo aplicarse porcentajes adicionales a los establecidos en el Decreto Supremo N° 0181, de acuerdo a disponibilidad financiera, sustentado con informes técnico, financiero y legal.»
- **Paráfrasis:** El ajuste se formaliza por única vez con un contrato modificatorio que puede superar los porcentajes del art. 89 de las NB-SABS, según disponibilidad financiera y con informes técnico, financiero y legal.
- **Uso sugerido:** Introducción (contexto de crisis y alza de materiales) | Cap.1 marco legal (ajuste de precios) | Cap.3 Discusión (supuesto de precios constantes del modelo) | Cap.1 (excepción a los límites del art. 89 NB-SABS)

**ds5321_2025-05** · PDF p. 2 · cita: s. p. · Art. 4, parág. II, inc. b) · *requisito_normativo*
> «El contratista debe actualizar la Garantía de Cumplimiento de Contrato de acuerdo al monto total del contrato resultante del contrato modificatorio por ajustes de precios unitarios.»
- **Paráfrasis:** Tras el ajuste, el contratista debe actualizar la garantía de cumplimiento al nuevo monto total del contrato.
- **Uso sugerido:** Cap.1 marco legal (garantías)

**ds5321_2025-06** · PDF p. 1 · cita: s. p. · Anexo, numeral 1 (Materiales de acero) · *dato*
> «1 MATERIALES DE ACERO 1.1 Acero corrugado 1.2 Acero liso 1.3 Acero pretensado»
- **Paráfrasis:** El Anexo del D.S. 5321 incluye entre los materiales importados ajustables el acero corrugado, el liso y el pretensado, además de perfiles, pletinas y planchas.
- **Uso sugerido:** Introducción (contexto de crisis y alza de materiales) | Cap.1 marco legal (ajuste de precios) | Cap.3 Discusión (supuesto de precios constantes del modelo) (ítem 8: acero estructural)


## 9. D.S. N.º 5406 de 28 de mayo de 2025 (modifica el D.S. 5321)

- **Archivo:** `04_Bibliografia/06_Legislacion_Bolivia/Bolivia_DS5406_2025_Modifica_DS5321_Ampliacion_Plazos.pdf`
- **Clave BibLaTeX:** `ds5406_2025`
- **Referencia (APA 7):** Estado Plurinacional de Bolivia. (2025, 28 de mayo). *Decreto Supremo N.º 5406: modificaciones al Decreto Supremo N.º 5321, de 23 de enero de 2025*. Gaceta Oficial del Estado Plurinacional de Bolivia.

- Texto de consulta de la Gaceta Oficial; sin paginación impresa ni número de edición. Amplía el D.S. 5321 a los contratos llave en mano y extiende hasta el 31/10/2025 el plazo para los contratos modificatorios y los anticipos adicionales; su disposición adicional única modifica además el D.S. 5353 (gasto en combustibles de las entidades públicas).

**ds5406_2025-01** · PDF p. 1 · cita: s. p. · Art. 2, parág. I (nuevo art. 1 del D.S. 5321) · *requisito_normativo*
> «en los contratos de obra y contratos llave en mano, que se encuentren en ejecución, suscritos por entidades públicas.»
- **Paráfrasis:** El D.S. 5406 extendió el objeto del D.S. 5321 a los contratos llave en mano en ejecución, además de los contratos de obra.
- **Uso sugerido:** Cap.1 marco legal (ajuste de precios 2025) | Cap.3 Discusión (contexto del contrato)

**ds5406_2025-02** · PDF p. 2 · cita: s. p. · Art. 2, parág. III (nuevo art. 3.I del D.S. 5321) · *requisito_normativo*
> «podrán efectuar el ajuste de precios unitarios de los materiales de construcción, maquinaria y equipos, importados, detallados en el Anexo del presente Decreto Supremo, a través de un contrato modificatorio que debe ser suscrito hasta el 31 de octubre de 2025.»
- **Paráfrasis:** El plazo para suscribir el contrato modificatorio de ajuste de precios de materiales importados se amplió hasta el 31 de octubre de 2025.
- **Uso sugerido:** Cap.1 marco legal (ajuste de precios 2025) | Cap.3 Discusión (contexto del contrato)

**ds5406_2025-03** · PDF p. 2 · cita: s. p. · Art. 2, parág. V (nuevo art. 5.I del D.S. 5321) · *requisito_normativo*
> «La entidad pública podrá otorgar, hasta el 31 de octubre de 2025, uno o varios anticipos adicionales para los contratos de obra y contratos llave en mano, que se encuentren en ejecución»
- **Paráfrasis:** Hasta el 31 de octubre de 2025 las entidades podían otorgar anticipos adicionales para adquirir materiales importados pendientes.
- **Uso sugerido:** Cap.1 marco legal (ajuste de precios 2025) | Cap.3 Discusión (contexto del contrato)

**ds5406_2025-04** · PDF p. 2 · cita: s. p. · Art. 2, parág. VII (nueva DA segunda del D.S. 5321) · *requisito_normativo*
> «De manera excepcional, hasta el 31 de octubre de 2025, se faculta a las entidades públicas realizar el ajuste de precios, pudiendo aplicar porcentajes adicionales a los establecidos en el Decreto Supremo Nº 0181»
- **Paráfrasis:** Hasta el 31 de octubre de 2025 también se autorizó ajustar el precio del diésel y las gasolinas importados, aun por encima de los porcentajes de las NB-SABS.
- **Uso sugerido:** Cap.1 marco legal (ajuste de precios 2025) | Cap.3 Discusión (contexto del contrato) (combustibles: diésel y gasolinas)


## 10. D.S. N.º 5452 de 3 de septiembre de 2025 (modifica e incorpora disposiciones en el D.S. 5321) — OCR

- **Archivo:** `04_Bibliografia/06_Legislacion_Bolivia/Bolivia_DS5452_2025_Modifica_DS5321_Ajuste_Precios.pdf`  
- **PDF con OCR (capa de texto generada con tesseract, `spa`):** `/tmp/claude-0/-home-user-TesisSGC/c22f603c-c695-5c98-b48f-e99a1e2bf286/scratchpad/normas/ocr/Bolivia_DS5452_2025_OCR.pdf`
- **Clave BibLaTeX:** `ds5452_2025`
- **Referencia (APA 7):** Estado Plurinacional de Bolivia. (2025, 3 de septiembre). *Decreto Supremo N.º 5452: modificaciones e incorporaciones en el Decreto Supremo N.º 5321, de 23 de enero de 2025*. Gaceta Oficial del Estado Plurinacional de Bolivia.

- **Sin capa de texto:** el PDF original (2 páginas, texto vectorizado) se procesó con tesseract (`spa`, 300 ppp); todas las fichas llevan `capa_de_texto: false` y se verificaron en el PDF con OCR. El OCR transcribe «N°» como «N*»; las fórmulas se leyeron en la imagen.
- **Fórmulas vigentes (leídas en la imagen, PDF 1–2):** Vᵢ = PAᵢ − PIᵢ, donde PAᵢ es el precio unitario del material, maquinaria o equipo «al momento de su cotización o proforma» y PIᵢ el precio unitario inicial señalado en el contrato; y MCM = Σᵢ₌₁ⁿ (Vᵢ × Cᵢ), donde Cᵢ es la cantidad «por aplicar (saldo) a la obra». Este es el mecanismo legal de ajuste; el modelo de la tesis trabaja a precios constantes del contrato para aislar el efecto del SGC.
- Firmado en La Paz el 03/09/2025 (Luis Alberto Arce Catacora). Sin número de edición de la Gaceta en el PDF.

**ds5452_2025-01** · PDF p. 1 · cita: s. p. · Art. 1 (Objeto) · *dato* · OCR
> «El presente Decreto Supremo tiene por objeto realizar modificaciones e incorporaciones en el Decreto Supremo N* 5321, de 23 de enero de 2025.»
- **Paráfrasis:** El D.S. 5452 modifica e incorpora disposiciones en el D.S. 5321 sobre ajuste de precios de materiales importados.
- **Uso sugerido:** Cap.1 marco legal (fórmula oficial de ajuste de precios) | Cap.2 modelo de costos (por qué se trabaja a precios constantes) | Cap.3 Discusión
- **Nota:** OCR: «N*» corresponde a «N°» en la imagen.

**ds5452_2025-02** · PDF p. 1 · cita: s. p. · Art. 2 (nuevo art. 3.IV, inc. a) del D.S. 5321) · *metodo* · OCR
> «a) La entidad pública determinará la variación de precios aplicando la siguiente fórmula para cada material, maquinaria o equipo:»
- **Paráfrasis:** La variación de precio de cada material se calcula como la diferencia entre su precio unitario al momento de la cotización o proforma y el precio unitario inicial del contrato (Vᵢ = PAᵢ − PIᵢ).
- **Uso sugerido:** Cap.1 marco legal (fórmula oficial de ajuste de precios) | Cap.2 modelo de costos (por qué se trabaja a precios constantes) | Cap.3 Discusión

**ds5452_2025-03** · PDF p. 2 · cita: s. p. · Art. 2 (nuevo art. 3.IV, inc. b) del D.S. 5321), definición de Cᵢ · *metodo* · OCR
> «No se considerarán las cantidades de los materiales/maquinania/equipo utilizados y adquiridos en la obra previo a la vigencia del contrato modificatorio»
- **Paráfrasis:** El monto del contrato modificatorio es la suma de las variaciones de precio multiplicadas por las cantidades pendientes (saldo) de cada material; no se ajustan las cantidades ya utilizadas o adquiridas antes de su vigencia.
- **Uso sugerido:** Cap.1 marco legal (fórmula oficial de ajuste de precios) | Cap.2 modelo de costos (por qué se trabaja a precios constantes) | Cap.3 Discusión
- **Nota:** OCR: «maquinania» corresponde a «maquinaria» en la imagen.

**ds5452_2025-04** · PDF p. 1 · cita: s. p. · Art. 2 (nuevo art. 3.III del D.S. 5321) · *requisito_normativo* · OCR
> «De manera excepcional por la situación económica y el incremento de precios, en contratos llave en mano en ejecución, en sustitución de los documentos señalados, se elaborará un informe técnico que justifique el ajuste de precios del material importado.»
- **Paráfrasis:** En contratos llave en mano en ejecución, a falta del Formulario B-2, el ajuste del material importado se justifica con un informe técnico, en atención a la situación económica y al alza de precios.
- **Uso sugerido:** Cap.1 marco legal (fórmula oficial de ajuste de precios) | Cap.2 modelo de costos (por qué se trabaja a precios constantes) | Cap.3 Discusión

**ds5452_2025-05** · PDF p. 2 · cita: s. p. · Fecha y lugar · *dato* · OCR
> «Es dado en la Casa Grande del Pueblo de la ciudad de La Paz, a los tres días del mes de septiembre del año dos mil veinticinco.»
- **Paráfrasis:** El D.S. 5452 se dictó en La Paz el 3 de septiembre de 2025.
- **Uso sugerido:** Bibliografía (fecha del decreto)


## 11. D.S. N.º 5597 de 30 de marzo de 2026 (ajuste de precios en contratos de obra)

- **Archivo:** `04_Bibliografia/06_Legislacion_Bolivia/Bolivia_DS5597_2026_Ajuste_Precios_Materiales_Contratos_Obra.pdf`
- **Clave BibLaTeX:** `ds5597_2026`
- **Referencia (APA 7):** Estado Plurinacional de Bolivia. (2026, 30 de marzo). *Decreto Supremo N.º 5597: mecanismos operativos para el ajuste de precios de materiales de construcción, maquinaria y equipo en contratos de obra y llave en mano*. Gaceta Oficial del Estado Plurinacional de Bolivia. http://www.gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281136

- Texto de consulta de la Gaceta Oficial (© 2025); sin paginación impresa ni número de edición. Firmado por Rodrigo Paz Pereira en el Palacio de Gobierno el 30/03/2026. La URL proviene de `bib/00_base.bib`.
- **Relevancia para el caso:** a diferencia del D.S. 5321, alcanza a todos los materiales (no solo importados) y a contratos sin orden de proceder; permite contratos modificatorios por encima de los límites de las NB-SABS hasta el 31/12/2026; y su **disposición adicional quinta** prevé la resolución del contrato por «situación ajena a las partes», asimilable a caso fortuito, sin registro del contratista como impedido ni ejecución de la garantía. La carta notariada de la obra (05/01/2026) es anterior a este decreto: su aplicabilidad al caso debe valorarla la asesoría legal de la UATF (no se afirma aquí).

**ds5597_2026-01** · PDF p. 1 · cita: s. p. · Considerandos · *dato*
> «Que el Estado Plurinacional de Bolivia enfrenta una crisis económica y financiera de carácter estructural heredada, que ha obligado al Gobierno Nacional a la adopción de medidas para estabilizar la economía, las cuales inciden en el costo de los insumos utilizados en la construcción.»
- **Paráfrasis:** El propio decreto reconoce una crisis económica y financiera estructural cuyas medidas de estabilización encarecieron los insumos de la construcción.
- **Uso sugerido:** Introducción (planteamiento del problema: alza de precios 2026) | Cap.1 marco legal (ajuste de precios 2026)

**ds5597_2026-02** · PDF p. 1 · cita: s. p. · Art. 1 (Objeto) · *requisito_normativo*
> «tiene por objeto establecer, de manera excepcional, mecanismos operativos para el ajuste de precios de materiales de construcción, maquinaria y equipo en los contratos de obra y contratos llave en mano suscritos por las entidades públicas.»
- **Paráfrasis:** El D.S. 5597 establece, de forma excepcional, mecanismos de ajuste de precios de materiales, maquinaria y equipo en contratos de obra y llave en mano de entidades públicas.
- **Uso sugerido:** Introducción (planteamiento del problema: alza de precios 2026) | Cap.1 marco legal (ajuste de precios 2026)

**ds5597_2026-03** · PDF p. 1 · cita: s. p. · Art. 2 (Ámbito de aplicación) · *requisito_normativo*
> «El presente Decreto Supremo es aplicable a los contratos de obra y contratos llave en mano, que no cuenten con orden de proceder y aquellos que se encuentren en ejecución»
- **Paráfrasis:** Se aplica a contratos de obra y llave en mano suscritos bajo las NB-SABS hasta su vigencia, tanto en ejecución como sin orden de proceder.
- **Uso sugerido:** Introducción (planteamiento del problema: alza de precios 2026) | Cap.1 marco legal (ajuste de precios 2026)

**ds5597_2026-04** · PDF p. 1 · cita: s. p. · Art. 3, parág. II · *metodo*
> «El ajuste de precios se realizará únicamente sobre el precio del material señalado en el numeral 1 (materiales) del Formulario B-2 (Análisis de Precios Unitarios) o documento similar que incluya este tipo de información, sin considerar los costos indirectos establecidos en el contrato vigente.»
- **Paráfrasis:** El ajuste recae solo en el componente de materiales del análisis de precios unitarios (Formulario B-2), sin incluir los costos indirectos.
- **Uso sugerido:** Introducción (planteamiento del problema: alza de precios 2026) | Cap.1 marco legal (ajuste de precios 2026) | Cap.2 modelo de costos (componente de materiales del precio unitario)

**ds5597_2026-05** · PDF p. 2 · cita: s. p. · Art. 3, parág. IV · *requisito_normativo*
> «No estarán sujetos al ajuste de precios aquellos materiales, maquinaria y equipo que hayan sido ajustados en el marco del Decreto Supremo N° 5321, de 23 de enero de 2025 y sus modificaciones.»
- **Paráfrasis:** No se puede volver a ajustar lo que ya se ajustó con el D.S. 5321 y sus modificaciones.
- **Uso sugerido:** Introducción (planteamiento del problema: alza de precios 2026) | Cap.1 marco legal (ajuste de precios 2026)

**ds5597_2026-06** · PDF p. 2 · cita: s. p. · Art. 4, parág. I · *requisito_normativo*
> «El ajuste de precios en los contratos de obra y contratos llave en mano será efectuado mediante contrato modificatorio, a ser suscrito por única vez hasta el 31 de diciembre de 2026, pudiendo aplicarse porcentajes adicionales a los establecidos en el Decreto Supremo N° 0181»
- **Paráfrasis:** El ajuste se formaliza con un único contrato modificatorio, suscrito hasta el 31 de diciembre de 2026, que puede exceder los porcentajes del art. 89 de las NB-SABS según disponibilidad financiera.
- **Uso sugerido:** Introducción (planteamiento del problema: alza de precios 2026) | Cap.1 marco legal (ajuste de precios 2026) | Cap.1 (excepción a los límites del art. 89)

**ds5597_2026-07** · PDF p. 3 · cita: s. p. · Disposición adicional tercera · *requisito_normativo*
> «De manera excepcional, la entidad contratante podrá modificar el alcance del contrato de obra o contrato llave en mano, sin que afecte su funcionalidad, mediante contrato modificatorio a ser suscrito por única vez hasta el 31 de diciembre de 2026»
- **Paráfrasis:** Hasta el 31 de diciembre de 2026 la entidad puede, por única vez, modificar el alcance del contrato sin afectar su funcionalidad, aun por encima de los porcentajes de las NB-SABS.
- **Uso sugerido:** Cap.1 marco legal (resolución por situación ajena a las partes) | Cap.3 Discusión (paralización y resolución del contrato de la obra)

**ds5597_2026-08** · PDF p. 3 · cita: s. p. · Disposición adicional quinta, parág. I · *requisito_normativo*
> «cuando se identifique la necesidad del incremento de precio de los materiales, maquinaria y equipo, y este no sea viable, podrá tener lugar la resolución de contrato por una situación ajena a las partes»
- **Paráfrasis:** Si el incremento de precios de materiales, maquinaria y equipo es necesario pero no viable, el contrato puede resolverse por una situación ajena a las partes.
- **Uso sugerido:** Cap.1 marco legal (resolución por situación ajena a las partes) | Cap.3 Discusión (paralización y resolución del contrato de la obra)

**ds5597_2026-09** · PDF p. 3 · cita: s. p. · Disposición adicional quinta, parág. I · *requisito_normativo*
> «medida que será una decisión de la entidad contratante con aceptación del Contratista. Esta inviabilidad podrá considerarse como caso fortuito.»
- **Paráfrasis:** Esa resolución la decide la entidad con aceptación del contratista, y la inviabilidad del ajuste puede considerarse caso fortuito.
- **Uso sugerido:** Cap.1 marco legal (resolución por situación ajena a las partes) | Cap.3 Discusión (paralización y resolución del contrato de la obra)

**ds5597_2026-10** · PDF p. 3 · cita: s. p. · Disposición adicional quinta, parág. II · *requisito_normativo*
> «no corresponderá el registro como impedido en el Sistema de Contrataciones Estatales – SICOES, ni la ejecución de la garantía de cumplimiento de contrato.»
- **Paráfrasis:** Resuelto el contrato por esta vía, el contratista no se registra como impedido en el SICOES ni se ejecuta su garantía de cumplimiento.
- **Uso sugerido:** Cap.1 marco legal (resolución por situación ajena a las partes) | Cap.3 Discusión (paralización y resolución del contrato de la obra)

**ds5597_2026-11** · PDF p. 3 · cita: s. p. · Disposición adicional quinta, parág. III · *requisito_normativo*
> «La resolución de contrato efectuada en el marco de la presente Disposición, no dará lugar a reconocimiento de daños y perjuicios a favor del contratista»
- **Paráfrasis:** Esta resolución no genera derecho del contratista a daños y perjuicios en ninguna vía.
- **Uso sugerido:** Cap.1 marco legal (resolución por situación ajena a las partes) | Cap.3 Discusión (paralización y resolución del contrato de la obra)


## 12. D.S. N.º 5600 de 6 de abril de 2026 (contrataciones directas; deroga el art. 83 bis del D.S. 0181)

- **Archivo:** `04_Bibliografia/06_Legislacion_Bolivia/Bolivia_DS5600_2026_Contrataciones_Directas_Deroga_Art83bis.pdf`
- **Clave BibLaTeX:** `ds5600_2026`
- **Referencia (APA 7):** Estado Plurinacional de Bolivia. (2026, 6 de abril). *Decreto Supremo N.º 5600: abrogación y derogación de autorizaciones de contrataciones directas*. Gaceta Oficial del Estado Plurinacional de Bolivia.

- Texto de consulta de la Gaceta Oficial; sin paginación impresa ni número de edición. Es la modificación de las NB-SABS posterior al texto compilado de 2025. Su efecto para la tesis es indirecto: confirma que la contratación del saldo de la obra debe seguir el D.S. 0181 (por ejemplo, la contratación por excepción del art. 65 c tras una resolución), no autorizaciones de contratación directa por normativa específica.

**ds5600_2026-01** · PDF p. 1 · cita: s. p. · Art. 1 (Objeto) · *requisito_normativo*
> «la presente norma tiene por objeto abrogar y derogar las autorizaciones de contrataciones directas establecidas en decretos supremos, como excepción al Decreto Supremo Nº 0181»
- **Paráfrasis:** El D.S. 5600 deja sin efecto las autorizaciones de contratación directa dispuestas por decretos supremos como excepción a las NB-SABS, para transparentar las contrataciones públicas.
- **Uso sugerido:** Cap.1 marco legal (vigencia de las NB-SABS en 2026; contratación del saldo de obra)

**ds5600_2026-02** · PDF p. 1 · cita: s. p. · Art. 2, parág. II · *requisito_normativo*
> «Se deroga el Artículo 83 Bis del Decreto Supremo Nº 0181, incorporado por el Artículo 5 del Decreto Supremo N° 4453, de 14 de enero de 2021, modificado por el Decreto Supremo Nº 5216, de 4 de septiembre de 2024.»
- **Paráfrasis:** Deroga el art. 83 bis de las NB-SABS, introducido en 2021 y modificado en 2024, por lo que el texto compilado de 2025 debe leerse con esta salvedad.
- **Uso sugerido:** Cap.1 marco legal (vigencia de las NB-SABS en 2026; contratación del saldo de obra)

**ds5600_2026-03** · PDF p. 1 · cita: s. p. · Disposición transitoria primera · *requisito_normativo*
> «Las entidades públicas que hayan iniciado procesos de contratación directa de bienes, obras y servicios con anterioridad a la vigencia del presente Decreto Supremo, deben concluir los mismos aplicando la norma vigente al momento de su inicio.»
- **Paráfrasis:** Los procesos de contratación directa iniciados antes de su vigencia concluyen con la norma vigente a su inicio.
- **Uso sugerido:** Cap.1 marco legal (vigencia de las NB-SABS en 2026; contratación del saldo de obra)

**ds5600_2026-04** · PDF p. 2 · cita: s. p. · Fecha y lugar · *dato*
> «Es dado en el Palacio de Gobierno, a los seis días del mes de abril del año dos mil veintiséis.»
- **Paráfrasis:** El D.S. 5600 se dictó el 6 de abril de 2026.
- **Uso sugerido:** Bibliografía (fecha del decreto)


## 13. R.M. MEFP N.º 048 de 4 de marzo de 2024 (aprueba nuevos modelos de DBC de obras)

- **Archivo:** `04_Bibliografia/06_Legislacion_Bolivia/MEFP_RM048_2024_Aprueba_Modelos_DBC_Obras.pdf`
- **Clave BibLaTeX:** `rm048_2024`
- **Referencia (APA 7):** Ministerio de Economía y Finanzas Públicas. (2024, 4 de marzo). *Resolución Ministerial N.º 048: aprueba el Reglamento de Contrataciones con Apoyo de Medios Electrónicos y los modelos de documento base de contratación de obras (ANPE y Licitación Pública)*.

- El PDF es un escaneo con capa de texto propia (generada por el escáner): las citas son literales de esa capa, que contiene errores menores de reconocimiento (p. ej., «O 4 MAR, 2024» por «04 MAR. 2024», «modalidade»); no tiene paginación impresa (s. p.) ni datos de publicación en Gaceta.
- **Consecuencia para la tesis:** la R.M. 048/2024 sustituye los modelos de DBC de obras aprobados por la R.M. 021/2022 y se aplica a los procesos iniciados desde su vigencia (20 días hábiles después de su publicación). El proceso de la obra (CUCE 25-0143-…, gestión 2025) debió regirse por el modelo de 2024, no por el de 2022 que está en el repositorio: las cláusulas del DBC 2022 (ficha 14) son una referencia que debe contrastarse con el DBC y el contrato reales publicados en el SICOES.

**rm048_2024-01** · PDF p. 1 · cita: s. p. · Encabezado · *dato*
> «RESOLUCIÓN MINISTERIAL N° 048 La Paz, O 4 MAR, 2024 VISTOS Y CONSIDERANDO»
- **Paráfrasis:** La resolución es la R.M. N.º 048 del Ministerio de Economía y Finanzas Públicas, de 4 de marzo de 2024.
- **Uso sugerido:** Bibliografía (número y fecha de la R.M.)
- **Nota:** Capa de texto del escáner: «O 4 MAR, 2024» corresponde a «04 MAR. 2024».

**rm048_2024-02** · PDF p. 2 · cita: s. p. · Considerandos · *dato*
> «es necesario aprobar un nuevo Reglamento de Contrataciones con Apoyo de Medios Electrónicos, nuevos modelos de DBC de obras en las modalidades de ANPE y Licitación Pública, así como modificar el Manual de Operaciones del SICOES.»
- **Paráfrasis:** El MEFP justificó la R.M. 048/2024 en la necesidad de un nuevo reglamento de contrataciones electrónicas (con subasta electrónica de obras) y de nuevos modelos de DBC de obras.
- **Uso sugerido:** Cap.1 marco legal (modelo de DBC aplicable a la obra) | Nota metodológica sobre el uso del modelo de DBC 2022

**rm048_2024-03** · PDF p. 2 · cita: s. p. · Resuelve segundo · *requisito_normativo*
> «Aprobar los Modelos de Documento Base de Contratación - DBC de obras, en las modalidades de Apoyo Nacional a la Producción y Empleo - ANPE Licitación Pública.»
- **Paráfrasis:** La R.M. 048/2024 aprueba los nuevos modelos de DBC de obras para las modalidades ANPE y Licitación Pública.
- **Uso sugerido:** Cap.1 marco legal (modelo de DBC aplicable a la obra) | Nota metodológica sobre el uso del modelo de DBC 2022
- **Nota:** La capa de texto omite la «y» entre «ANPE» y «Licitación Pública».

**rm048_2024-04** · PDF p. 2 · cita: s. p. · Resuelve tercero · *requisito_normativo*
> «aprobados por los subíndices ii. de los incisos a) y b) del punto resolutivo TERCERO de la Resolución Ministerial N° 021 de 2 de febrero de 2022»
- **Paráfrasis:** Deja sin efecto los modelos de DBC de obras (ANPE y Licitación Pública) aprobados por la R.M. 021 de 2 de febrero de 2022, que quedan reemplazados por los nuevos.
- **Uso sugerido:** Cap.1 marco legal (modelo de DBC aplicable a la obra) | Nota metodológica sobre el uso del modelo de DBC 2022

**rm048_2024-05** · PDF p. 3 · cita: s. p. · Resuelve quinto, parág. II · *requisito_normativo*
> «Todo proceso de contratación de obras en las modalidades ANPE y Licitación Pública, iniciado a partir de la aplicación de la presente Resolución, incluyendo aquellos que cuenten con segundas o siguientes convocatorias de procesos declarados desiertos, así como nuevas convocatorias, se realizarán conforme los modelos de DBC aprobados en Anexo.»
- **Paráfrasis:** Todo proceso de contratación de obras iniciado desde la aplicación de la R.M. 048/2024 debe usar los nuevos modelos de DBC; los iniciados antes concluyen con la norma anterior.
- **Uso sugerido:** Cap.1 marco legal (modelo de DBC aplicable a la obra) | Nota metodológica sobre el uso del modelo de DBC 2022

**rm048_2024-06** · PDF p. 3 · cita: s. p. · Resuelve sexto · *requisito_normativo*
> «La presente Resolución Ministerial será publicada conforme a normativa vigente, siendo aplicable a los veinte (20) días hábiles, computables a partir del día hábil siguiente de su publicación.»
- **Paráfrasis:** La R.M. 048/2024 se aplica a los veinte días hábiles de su publicación.
- **Uso sugerido:** Cap.1 marco legal (modelo de DBC aplicable a la obra) | Nota metodológica sobre el uso del modelo de DBC 2022


## 14. Modelo de DBC de obras — Licitación Pública (R.M. MEFP N.º 021/2022, sustituido)

- **Archivo:** `04_Bibliografia/06_Legislacion_Bolivia/MEFP_RM021_2022_Modelo_DBC_Obras_LP_SUSTITUIDO.pdf`
- **Clave BibLaTeX:** `dbc2022`
- **Referencia (APA 7):** Ministerio de Economía y Finanzas Públicas. (2022). *Modelo de documento base de contratación de obras: Licitación Pública* [Aprobado por Resolución Ministerial N.º 021 de 2 de febrero de 2022; sustituido por la R.M. N.º 048/2024].

- **Paginación:** portada sin número; preliminares en romanos (PDF 2–4); desde la PDF 5 el número impreso = PDF − 4 (PDF 75 → p. 71). El modelo de contrato es el Anexo 6 (PDF 63–92, pp. 59–88).
- **Vigencia:** este modelo fue **sustituido** por la R.M. 048/2024 (ficha 13). Sus cláusulas se fichan porque describen las figuras contractuales (Fiscal, Supervisor, Libro de Órdenes, ensayos a cargo del contratista, planillas, multas, resolución, garantías) con las que la tesis diseña el SGC, pero deben confrontarse con el contrato real de la obra antes de afirmar que rigen en ella.
- **Fórmula de multas por mora (leída en la imagen, p. 78):** Mᵢ = (2/3) · (DMᵢ / nᵢ) · MHᵢ, con DMᵢ días de mora del hito i, nᵢ días pactados para el hito y MHᵢ monto del hito; multa acumulada Mₐ = M₁ + … + Mₖ; resolución optativa al 10 % y obligatoria al 20 % del monto del contrato.
- **Roles (síntesis):** el Fiscal de Obra es el representante de la entidad que exige el cumplimiento del contrato a través del Supervisor y controla al Supervisor; el Supervisor ejerce la inspección técnica, aprueba planillas y es «responsable directo» del control de calidad; el contratista asume el costo de los ensayos y la obligación de cumplir las especificaciones.

**dbc2022-01** · PDF p. 1 · cita: s. p. · Portada · *dato*
> «MODELO DE DOCUMENTO BASE DE CONTRATACIÓN DE OBRAS LICITACIÓN PÚBLICA Aprobado Mediante Resolución Ministerial N° 021 de 2 de febrero de 2022»
- **Paráfrasis:** El modelo de DBC de obras por licitación pública del repositorio es el aprobado por la R.M. 021 de 2 de febrero de 2022, elaborado en el marco del D.S. 0181.
- **Uso sugerido:** Bibliografía (identificación del modelo)

**dbc2022-02** · PDF p. 24 · cita: p. 20 · Parte I, num. 32 (Modificaciones al contrato) · *requisito_normativo*
> «En todos los casos son responsables por los resultados de la aplicación de los instrumentos de modificación descritos, el FISCAL DE OBRA, SUPERVISOR y CONTRATISTA.»
- **Paráfrasis:** Fiscal de Obra, Supervisor y contratista responden conjuntamente por los resultados de las órdenes de trabajo, órdenes de cambio y contratos modificatorios.
- **Uso sugerido:** Cap.1 marco legal (modificaciones de obra) | Cap.3 Discusión (contrato modificatorio)

**dbc2022-03** · PDF p. 24 · cita: p. 20 · Parte I, num. 32, inc. a) (Orden de Trabajo) · *definicion*
> «La Orden de Trabajo se aplica cuando se realiza un ajuste o redistribución de cantidades de obra, siempre que no existan modificaciones del precio de contrato, ni plazos en el mismo, ni se introduzcan ítems nuevos»
- **Paráfrasis:** La orden de trabajo redistribuye cantidades de obra sin cambiar precio, plazo ni crear ítems; la emite el Supervisor por carta o en el Libro de Órdenes.
- **Uso sugerido:** Cap.1 marco legal (modificaciones de obra) | Cap.3 Discusión (contrato modificatorio)

**dbc2022-04** · PDF p. 66 · cita: p. 62 · Cláusula séptima (Garantías) · *requisito_normativo*
> «equivalente al siete por ciento (7%) del monto total del Contrato.»
- **Paráfrasis:** La garantía de cumplimiento del contrato de obra es del 7 % del monto total y se ejecuta a solo requerimiento de la entidad ante incumplimiento.
- **Uso sugerido:** Cap.1 marco legal (garantías)

**dbc2022-05** · PDF p. 67 · cita: p. 63 · Cláusula séptima (Garantías) · *requisito_normativo*
> «El SUPERVISOR llevará el control directo de la vigencia de la (s) garantía (s) en cuanto al monto y plazo, a efectos de requerir su ampliación al CONTRATISTA, o solicitar a la ENTIDAD su ejecución.»
- **Paráfrasis:** El Supervisor controla la vigencia y el monto de las garantías y pide su ampliación o su ejecución.
- **Uso sugerido:** Cap.1 marco legal (Fiscal y Supervisor) | Cap.2 asignación de responsabilidades del SGC (matriz de roles)

**dbc2022-06** · PDF p. 71 · cita: p. 67 · Cláusula vigésima (Fuerza mayor y caso fortuito) · *requisito_normativo*
> «En ningún caso y bajo ninguna circunstancia, se considerará como causa de Fuerza Mayor el mal tiempo que no sea notablemente fuera de lo común en el área de ejecución de la Obra»
- **Paráfrasis:** El mal tiempo que no sea notablemente anormal en la zona no es fuerza mayor, porque el contratista debía preverlo en su cronograma.
- **Uso sugerido:** Cap.1 marco legal (fuerza mayor, suspensión y resolución) | Cap.3 Discusión (paralización y resolución del contrato) (lluvia del 21/11/2025 anotada en el Libro de Órdenes)

**dbc2022-07** · PDF p. 71 · cita: p. 67 · Cláusula vigésima · *requisito_normativo*
> «tampoco se considerarán como fuerza mayor o caso fortuito, las demoras en la entrega en la obra de los materiales, equipos e implementos necesarios, por ser obligación del CONTRATISTA tomar y adoptar todas las previsiones necesarias para evitar demoras por dichas contingencias.»
- **Paráfrasis:** Las demoras en la entrega de materiales no constituyen fuerza mayor ni caso fortuito, porque prever el abastecimiento es obligación del contratista; de ahí el valor de un plan de abastecimiento dentro del SGC.
- **Uso sugerido:** Cap.1 marco legal (fuerza mayor, suspensión y resolución) | Cap.3 Discusión (paralización y resolución del contrato) (carta de Import Export Las Lomas sobre la entrega parcial del fierro)

**dbc2022-08** · PDF p. 71 · cita: p. 67 · Cláusula vigésima · *requisito_normativo*
> «el CONTRATISTA deberá solicitar al FISCAL la emisión de un certificado de constancia de la existencia del hecho de fuerza mayor, caso fortuito u otras causas debidamente justificadas, dentro de los tres (3) días hábiles de ocurrido el hecho»
- **Paráfrasis:** Para justificar demoras por fuerza mayor o caso fortuito, el contratista debe pedir al Fiscal un certificado de constancia dentro de los tres días hábiles del hecho, con sus respaldos.
- **Uso sugerido:** Cap.1 marco legal (fuerza mayor, suspensión y resolución) | Cap.3 Discusión (paralización y resolución del contrato)

**dbc2022-09** · PDF p. 72 · cita: p. 68 · Cláusula vigésima primera, 21.2.1, inc. g) · *requisito_normativo*
> «g) Por negligencia reiterada en tres (3) oportunidades en el cumplimiento de las especificaciones, planos, o de instrucciones escritas del SUPERVISOR.»
- **Paráfrasis:** La negligencia reiterada (tres veces) en el cumplimiento de especificaciones, planos o instrucciones escritas del Supervisor es causal de resolución atribuible al contratista.
- **Uso sugerido:** Cap.1 marco legal (fuerza mayor, suspensión y resolución) | Cap.3 Discusión (paralización y resolución del contrato) | Cap.2 (las no conformidades registradas sustentan esta causal)

**dbc2022-10** · PDF p. 72 · cita: p. 68 · Cláusula vigésima primera, 21.2.1, incs. i)-j) · *requisito_normativo*
> «i) De manera optativa cuando el monto de la multa acumulada alcance el diez por ciento (10%) del monto total del contrato. j) De manera obligatoria cuando el monto de la multa acumulada alcance el veinte por ciento (20%) del monto total del contrato.»
- **Paráfrasis:** La resolución es optativa cuando las multas acumuladas llegan al 10 % del monto del contrato y obligatoria cuando llegan al 20 %.
- **Uso sugerido:** Cap.1 marco legal (multas) | Cap.2 costos de no calidad (penalidades)

**dbc2022-11** · PDF p. 73 · cita: p. 69 · Cláusula vigésima primera, 21.2.3 · *metodo*
> «la ENTIDAD o el CONTRATISTA darán aviso escrito mediante carta notariada, a la otra parte, de su intención de resolver el CONTRATO, estableciendo claramente la causal que se aduce.»
- **Paráfrasis:** La resolución se inicia con una carta notariada de intención que expresa la causal; si en quince días hábiles no se enmiendan las fallas, se notifica por la misma vía que la resolución se hizo efectiva.
- **Uso sugerido:** Cap.1 marco legal (fuerza mayor, suspensión y resolución) | Cap.3 Discusión (paralización y resolución del contrato) (carta notariada de 05/01/2026)

**dbc2022-12** · PDF p. 74 · cita: p. 70 · Cláusula vigésima primera, 21.3 · *requisito_normativo*
> «la ENTIDAD se encontrase con situaciones fuera de control de las partes que imposibiliten la ejecución o conclusión de la obra, o vayan contra los intereses del Estado, la ENTIDAD en cualquier momento, mediante carta notariada dirigida al CONTRATISTA, suspenderá los trabajos y resolverá el CONTRATO total o parcialmente.»
- **Paráfrasis:** Ante situaciones fuera del control de las partes que impidan concluir la obra, la entidad puede suspender los trabajos y resolver total o parcialmente el contrato mediante carta notariada.
- **Uso sugerido:** Cap.1 marco legal (fuerza mayor, suspensión y resolución) | Cap.3 Discusión (paralización y resolución del contrato)

**dbc2022-13** · PDF p. 74 · cita: p. 70 · Cláusula vigésima primera, 21.3 · *metodo*
> «El CONTRATISTA conjuntamente con el SUPERVISOR, procederán con la medición del trabajo ejecutado hasta la fecha de suspensión, el avalúo de los materiales en obra que pudieran ser empleados posteriormente»
- **Paráfrasis:** Tras la resolución, contratista y Supervisor miden lo ejecutado hasta la suspensión y valoran los materiales en obra aprovechables; con ello el Supervisor elabora la planilla de medición final.
- **Uso sugerido:** Cap.1 marco legal (fuerza mayor, suspensión y resolución) | Cap.3 Discusión (paralización y resolución del contrato) | Cap.1 marco legal (medición y pago) | Cap.3 Discusión (cómputo del acero y planilla de cierre, a verificar por la Supervisión) (PAO N.º 3 de resolución)

**dbc2022-14** · PDF p. 75 · cita: p. 71 · Cláusula vigésima quinta (Libro de Órdenes) · *requisito_normativo*
> «Bajo su responsabilidad y en la obra, el CONTRATISTA llevará un Libro de Órdenes de Trabajo con páginas numeradas y dos copias, el mismo que deberá ser aperturado con participación de Notario de Fe Pública en la fecha en que el CONTRATISTA reciba la Orden de Proceder.»
- **Paráfrasis:** El contratista lleva en obra un Libro de Órdenes foliado, con dos copias, abierto ante notario de fe pública al recibir la orden de proceder.
- **Uso sugerido:** Cap.1 marco legal (Libro de Órdenes) | Cap.2 control de la información documentada | Cap.3 (análisis del Libro de Órdenes del ítem 13)

**dbc2022-15** · PDF p. 75 · cita: p. 71 · Cláusula vigésima quinta · *requisito_normativo*
> «En este libro el SUPERVISOR anotará las instrucciones, órdenes y observaciones impartidas al CONTRATISTA, que se refieran a los trabajos, cada orden llevará fecha y firma del SUPERVISOR y la constancia firmada del Superintendente de Obra de haberla recibido.»
- **Paráfrasis:** En el Libro de Órdenes el Supervisor registra instrucciones y observaciones con fecha y firma, y el superintendente firma su recepción; es el registro formal de la ejecución.
- **Uso sugerido:** Cap.1 marco legal (Libro de Órdenes) | Cap.2 control de la información documentada | Cap.3 (análisis del Libro de Órdenes del ítem 13)

**dbc2022-16** · PDF p. 75 · cita: p. 71 · Cláusula vigésima quinta · *requisito_normativo*
> «en el caso de los días de lluvia que puedan afectar la ruta crítica del cronograma de ejecución de la obra, el día en que suceda el hecho a efectos de que el SUPERVISOR se pronuncie de forma objetiva.»
- **Paráfrasis:** El contratista puede registrar en el Libro de Órdenes, el mismo día, hechos como lluvias que afecten la ruta crítica, para que el Supervisor se pronuncie objetivamente.
- **Uso sugerido:** Cap.1 marco legal (Libro de Órdenes) | Cap.2 control de la información documentada | Cap.3 (análisis del Libro de Órdenes del ítem 13) (asiento del 21/11/2025)

**dbc2022-17** · PDF p. 75 · cita: p. 71 · Cláusula vigésima quinta · *requisito_normativo*
> «Las comunicaciones cursadas entre partes, sólo entrarán en vigor cuando sean efectuadas y entregadas por escrito, a través del Libro de Órdenes o notas oficiales.»
- **Paráfrasis:** Solo tienen efecto las comunicaciones escritas, por el Libro de Órdenes o por notas oficiales.
- **Uso sugerido:** Cap.1 marco legal (Libro de Órdenes) | Cap.2 control de la información documentada | Cap.3 (análisis del Libro de Órdenes del ítem 13)

**dbc2022-18** · PDF p. 75 · cita: p. 71 · Cláusula vigésima sexta, 26.1 (Fiscalización) · *definicion*
> «a) Exigir a través del SUPERVISOR el cumplimiento del Contrato de Obra. b) Exigir directamente el cumplimiento del Contrato de SUPERVISIÓN TÉCNICA, realizando seguimiento y control de los actos del SUPERVISOR en la SUPERVISIÓN Técnica de la Obra.»
- **Paráfrasis:** El Fiscal de Obra, nombrado por la entidad, exige el cumplimiento del contrato de obra a través del Supervisor y controla directamente al Supervisor; además vela por el buen uso de los recursos y conoce los certificados de obra.
- **Uso sugerido:** Cap.1 marco legal (Fiscal y Supervisor) | Cap.2 asignación de responsabilidades del SGC (matriz de roles)

**dbc2022-19** · PDF p. 76 · cita: p. 72 · Cláusula vigésima sexta, 26.1 · *definicion*
> «El FISCAL tiene funciones diferentes a las del SUPERVISOR, por lo que no está facultado para suplantar en el ejercicio de sus funciones específicas y responsabilidades al SUPERVISOR.»
- **Paráfrasis:** Fiscal y Supervisor tienen funciones distintas: el Fiscal no puede sustituir al Supervisor en sus funciones y responsabilidades específicas.
- **Uso sugerido:** Cap.1 marco legal (Fiscal y Supervisor) | Cap.2 asignación de responsabilidades del SGC (matriz de roles)

**dbc2022-20** · PDF p. 76 · cita: p. 72 · Cláusula vigésima sexta, 26.3 (Supervisión técnica) · *definicion*
> «denominada en este Contrato el SUPERVISOR, con todas las facultades inherentes al buen desempeño de las funciones de SUPERVISIÓN e inspección técnica»
- **Paráfrasis:** El Supervisor es el consultor (individual o firma) contratado para la supervisión e inspección técnica de la obra, con todas las facultades necesarias para ello.
- **Uso sugerido:** Cap.1 marco legal (Fiscal y Supervisor) | Cap.2 asignación de responsabilidades del SGC (matriz de roles)

**dbc2022-21** · PDF p. 76 · cita: p. 72 · Cláusula vigésima sexta, 26.3, inc. f) · *requisito_normativo*
> «f) Realizar mediciones conjuntas con el CONTRATISTA de la obra ejecutada y aprobar los Certificados o Planillas de avance de obra.»
- **Paráfrasis:** El Supervisor mide junto con el contratista la obra ejecutada y aprueba las planillas de avance.
- **Uso sugerido:** Cap.1 marco legal (medición y pago) | Cap.3 Discusión (cómputo del acero y planilla de cierre, a verificar por la Supervisión)

**dbc2022-22** · PDF p. 77 · cita: p. 73 · Cláusula vigésima sexta, 26.3 · *requisito_normativo*
> «Será responsabilidad directa de la SUPERVISIÓN, el control de calidad y el cumplimiento de las especificaciones del contrato.»
- **Paráfrasis:** El control de calidad y el cumplimiento de las especificaciones son responsabilidad directa de la Supervisión.
- **Uso sugerido:** Cap.1 marco legal (control de calidad contractual) | Cap.2 PPI y procedimiento de control de materiales | Cap.3 Discusión (probetas, certificados y garantías de materiales)

**dbc2022-23** · PDF p. 77 · cita: p. 73 · Cláusula vigésima sexta, 26.6 (Inspección de la calidad de los materiales) · *requisito_normativo*
> «Todos los materiales a ser utilizados en la Obra deberán cumplir estrictamente con las Especificaciones Técnicas pertinentes y estarán sujetos a inspección, examen y ensayos dispuestos por la SUPERVISIÓN en cualquier momento»
- **Paráfrasis:** Todos los materiales deben cumplir las especificaciones técnicas y pueden ser inspeccionados y ensayados por orden de la Supervisión, en el lugar de producción o en obra, antes de incorporarse.
- **Uso sugerido:** Cap.1 marco legal (control de calidad contractual) | Cap.2 PPI y procedimiento de control de materiales | Cap.3 Discusión (probetas, certificados y garantías de materiales)

**dbc2022-24** · PDF p. 77 · cita: p. 73 · Cláusula vigésima sexta, 26.6 · *requisito_normativo*
> «antes de su incorporación a la misma. Los costos para la realización de ensayos están a cargo del CONTRATISTA.»
- **Paráfrasis:** El costo de los ensayos de materiales corre por cuenta del contratista, por lo que es un costo de evaluación que el modelo de costos de la calidad debe imputarle.
- **Uso sugerido:** Cap.1 marco legal (control de calidad contractual) | Cap.2 PPI y procedimiento de control de materiales | Cap.3 Discusión (probetas, certificados y garantías de materiales) | Cap.2 costos de la calidad (evaluación a cargo del contratista)

**dbc2022-25** · PDF p. 77 · cita: p. 73 · Cláusula vigésima sexta, 26.9 (Almacenamiento y acopio) · *requisito_normativo*
> «Los materiales almacenados, serán inspeccionados y aprobados por la SUPERVISIÓN antes de su uso en la Obra, para verificar si cumplen los requisitos especificados en el momento de ser utilizados.»
- **Paráfrasis:** Los materiales acopiados deben ser inspeccionados y aprobados por la Supervisión antes de usarse, para comprobar que siguen cumpliendo los requisitos.
- **Uso sugerido:** Cap.1 marco legal (control de calidad contractual) | Cap.2 PPI y procedimiento de control de materiales | Cap.3 Discusión (probetas, certificados y garantías de materiales)

**dbc2022-26** · PDF p. 78 · cita: p. 74 · Cláusula vigésima sexta, 26.10, inc. c) · *requisito_normativo*
> «La SUPERVISIÓN estará autorizada para llamar la atención del CONTRATISTA sobre cualquier discordancia del trabajo con los planos o especificaciones, para suspender todo trabajo mal ejecutado y rechazar material defectuoso.»
- **Paráfrasis:** La Supervisión puede observar discordancias con planos o especificaciones, suspender trabajos mal ejecutados y rechazar materiales defectuosos, ratificando por escrito en el Libro de Órdenes.
- **Uso sugerido:** Cap.1 marco legal (control de calidad contractual) | Cap.2 PPI y procedimiento de control de materiales | Cap.3 Discusión (probetas, certificados y garantías de materiales) | Cap.2 tratamiento de no conformidades

**dbc2022-27** · PDF p. 78 · cita: p. 74 · Cláusula vigésima sexta, 26.10, inc. d) · *requisito_normativo*
> «Ningún trabajo será cubierto o puesto fuera de vista sin la previa aprobación de la SUPERVISIÓN.»
- **Paráfrasis:** Ningún trabajo puede cubrirse sin aprobación previa de la Supervisión, como el armado de la losa antes del hormigonado (solicitud del 20/11/2025 y autorización del 28/11/2025).
- **Uso sugerido:** Cap.1 marco legal (control de calidad contractual) | Cap.2 PPI y procedimiento de control de materiales | Cap.3 Discusión (probetas, certificados y garantías de materiales) (punto de espera antes del vaciado de la losa)

**dbc2022-28** · PDF p. 78 · cita: p. 74 · Cláusula vigésima sexta, 26.11 (Pruebas) · *requisito_normativo*
> «Si la SUPERVISIÓN ordena al CONTRATISTA realizar alguna prueba que no esté contemplada en las especificaciones a fin de verificar si algún trabajo tiene defectos y la prueba revela que los tiene, el costo de la prueba y las muestras serán de cargo del CONTRATISTA.»
- **Paráfrasis:** Las pruebas adicionales que revelan defectos corren a cargo del contratista; si no hay defecto, se tratan como evento compensable.
- **Uso sugerido:** Cap.1 marco legal (control de calidad contractual) | Cap.2 PPI y procedimiento de control de materiales | Cap.3 Discusión (probetas, certificados y garantías de materiales) | Cap.2 costos de falla

**dbc2022-29** · PDF p. 78 · cita: p. 74 · Cláusula vigésima sexta, 26.12 (Corrección de defectos) · *definicion*
> «Toda parte de la Obra que no cumpla con los requerimientos de las especificaciones, planos u otros documentos del Contrato, será considerada trabajo defectuoso.»
- **Paráfrasis:** Es trabajo defectuoso toda parte de la obra que no cumple especificaciones, planos u otros documentos del contrato, y debe removerse y reemplazarse a satisfacción de la Supervisión.
- **Uso sugerido:** Cap.1 marco legal (control de calidad contractual) | Cap.2 PPI y procedimiento de control de materiales | Cap.3 Discusión (probetas, certificados y garantías de materiales) | Cap.2 definición contractual de no conformidad

**dbc2022-30** · PDF p. 79 · cita: p. 75 · Cláusula vigésima séptima (Medición de cantidades) · *requisito_normativo*
> «Las obras deberán medirse netas, excepto cuando los documentos de Contrato prescriban un procedimiento diferente. No se medirán volúmenes excedentes cuya ejecución no haya sido aprobada por escrito por el SUPERVISOR.»
- **Paráfrasis:** La obra se mide neta y no se pagan volúmenes excedentes sin aprobación escrita del Supervisor; es el criterio contra el cual debe verificarse el cómputo del acero de la losa.
- **Uso sugerido:** Cap.1 marco legal (medición y pago) | Cap.3 Discusión (cómputo del acero y planilla de cierre, a verificar por la Supervisión)

**dbc2022-31** · PDF p. 79 · cita: p. 75 · Cláusula vigésima séptima · *metodo*
> «Los resultados de las mediciones efectuadas conjuntamente y los cálculos respectivos se consignarán en una planilla especial que será elaborada por el CONTRATISTA en dos ejemplares»
- **Paráfrasis:** Las mediciones conjuntas y sus cálculos se registran en una planilla que prepara el contratista y controla y aprueba el Supervisor.
- **Uso sugerido:** Cap.1 marco legal (medición y pago) | Cap.3 Discusión (cómputo del acero y planilla de cierre, a verificar por la Supervisión)

**dbc2022-32** · PDF p. 79 · cita: p. 75 · Cláusula vigésima octava (Forma de pago) · *metodo*
> «El pago será paralelo al progreso de la obra, a este fin mensualmente y dentro de los cinco (5) días hábiles siguientes a cada mes vencido, el CONTRATISTA presentará al SUPERVISOR, para su revisión en versión definitiva, una planilla o certificado de pago debidamente firmado»
- **Paráfrasis:** Los pagos siguen el avance: el contratista presenta mensualmente la planilla al Supervisor, que la aprueba o devuelve en tres días hábiles y la remite al Fiscal antes del pago.
- **Uso sugerido:** Cap.1 marco legal (medición y pago) | Cap.3 Discusión (cómputo del acero y planilla de cierre, a verificar por la Supervisión)

**dbc2022-33** · PDF p. 81 · cita: p. 77 · Cláusula trigésima, 30.4, inc. b) (Orden de Cambio) · *requisito_normativo*
> «El incremento o disminución mediante Orden de Cambio (una o varias sumadas) solo admite el máximo del cinco por ciento (5%) del monto total de Contrato.»
- **Paráfrasis:** Las órdenes de cambio, sumadas, admiten como máximo un 5 % del monto del contrato.
- **Uso sugerido:** Cap.1 marco legal (modificaciones de obra) | Cap.3 Discusión (contrato modificatorio)

**dbc2022-34** · PDF p. 81 · cita: p. 77 · Cláusula trigésima, 30.4, inc. c) (Contrato Modificatorio) · *requisito_normativo*
> «Esta modalidad de modificación de la obra sólo es admisible hasta el diez por ciento (10%) del monto original del contrato e independiente de la emisión de Orden (es) de Cambio.»
- **Paráfrasis:** El contrato modificatorio, reservado a casos extraordinarios, solo admite hasta el 10 % del monto original, con independencia de las órdenes de cambio.
- **Uso sugerido:** Cap.1 marco legal (modificaciones de obra) | Cap.3 Discusión (contrato modificatorio)

**dbc2022-35** · PDF p. 82 · cita: p. 78 · Cláusula trigésima, 30.5 · *requisito_normativo*
> «La Orden de Trabajo, Orden de Cambio o Contrato Modificatorio, deben ser emitidos y suscritos de forma previa a la ejecución de los trabajos por parte del CONTRATISTA, en ninguno de los casos constituye un documento regularizador de procedimiento de ejecución de obra»
- **Paráfrasis:** Los instrumentos de modificación deben emitirse antes de ejecutar los trabajos y no pueden usarse para regularizar trabajos ya hechos, salvo emergencia declarada.
- **Uso sugerido:** Cap.1 marco legal (modificaciones de obra) | Cap.3 Discusión (contrato modificatorio)

**dbc2022-36** · PDF p. 82 · cita: p. 78 · Cláusula trigésima segunda (Morosidad y penalidades) · *requisito_normativo*
> «el CONTRATISTA se constituirá en mora sin necesidad de ningún previo requerimiento de la ENTIDAD obligándose a ésta última, aplicar una multa por cada día calendario de retraso de acuerdo a la siguiente fórmula:»
- **Paráfrasis:** Si un hito verificable del cronograma vence sin concluirse, el contratista entra en mora automáticamente y se le aplica una multa diaria Mᵢ = (2/3)·(DMᵢ/nᵢ)·MHᵢ (fórmula leída en la imagen).
- **Uso sugerido:** Cap.1 marco legal (multas) | Cap.2 costos de no calidad (penalidades)

**dbc2022-37** · PDF p. 83 · cita: p. 79 · Cláusula trigésima segunda · *requisito_normativo*
> «En todos los casos de resolución de contrato por causas atribuibles al CONTRATISTA, la ENTIDAD no podrá cobrar multas que excedan el veinte por ciento (20%) del monto total del contrato.»
- **Paráfrasis:** En la resolución por causas atribuibles al contratista, las multas cobrables no pueden superar el 20 % del monto del contrato; se descuentan en la liquidación final.
- **Uso sugerido:** Cap.1 marco legal (multas) | Cap.2 costos de no calidad (penalidades)

**dbc2022-38** · PDF p. 86 · cita: p. 82 · Cláusula trigésima tercera, 33.1 · *requisito_normativo*
> «El CONTRATISTA y su representante en la obra están obligados a conocer minuciosamente los planos, instrucciones, especificaciones técnicas y demás documentos de la Obra que le fueron proporcionados.»
- **Paráfrasis:** El contratista debe conocer a fondo planos y especificaciones y consultar sus dudas al Supervisor antes de ejecutar; de lo contrario asume los costos de subsanación.
- **Uso sugerido:** Cap.1 marco legal (control de calidad contractual) | Cap.2 PPI y procedimiento de control de materiales | Cap.3 Discusión (probetas, certificados y garantías de materiales) (revisión de planos y ET antes de ejecutar)

**dbc2022-39** · PDF p. 86 · cita: p. 82 · Cláusula trigésima tercera, 33.2 · *requisito_normativo*
> «EL CONTRATISTA no podrá entregar obra defectuosa o mal ejecutada aduciendo errores, defectos y omisiones en los planos y especificaciones técnicas, debiendo el trabajo erróneo o defectuoso ser subsanado y enmendado por su exclusiva cuenta.»
- **Paráfrasis:** El contratista no puede justificar obra defectuosa en errores de planos o especificaciones: debe corregirla a su costo, lo que refuerza la revisión documental previa que propone el SGC.
- **Uso sugerido:** Cap.1 marco legal (control de calidad contractual) | Cap.2 PPI y procedimiento de control de materiales | Cap.3 Discusión (probetas, certificados y garantías de materiales) | Cap.3 Discusión (discrepancias Plano 02 vs. ET)

**dbc2022-40** · PDF p. 87 · cita: p. 83 · Cláusula trigésima tercera, 33.10 · *requisito_normativo*
> «El CONTRATISTA custodiará todos los materiales, equipo y todo trabajo ejecutado, hasta la Recepción Definitiva de la obra, por la ENTIDAD.»
- **Paráfrasis:** El contratista custodia materiales, equipo y obra ejecutada hasta la recepción definitiva.
- **Uso sugerido:** Cap.1 marco legal (control de calidad contractual) | Cap.2 PPI y procedimiento de control de materiales | Cap.3 Discusión (probetas, certificados y garantías de materiales) (custodia de materiales en obra)

**dbc2022-41** · PDF p. 89 · cita: p. 85 · Cláusula trigésima sexta (Suspensión de los trabajos) · *requisito_normativo*
> «el SUPERVISOR podrá ordenar la suspensión temporal de la obra por condiciones meteorológicas excepcionalmente desfavorables, por la inseguridad total de las obras o de una parte de las mismas o si se presentan situaciones de Fuerza Mayor.»
- **Paráfrasis:** El Supervisor puede suspender temporalmente la obra por clima excepcionalmente desfavorable, inseguridad o fuerza mayor; si la suspensión supera 15 días y afecta la ruta crítica, se amplía el plazo mediante orden de cambio.
- **Uso sugerido:** Cap.1 marco legal (fuerza mayor, suspensión y resolución) | Cap.3 Discusión (paralización y resolución del contrato)

**dbc2022-42** · PDF p. 89 · cita: p. 85 · Cláusula trigésima séptima (Comisión de Recepción) · *requisito_normativo*
> «La Comisión de Recepción tiene la responsabilidad de efectuar la recepción, provisional y/o definitiva de las obras contratadas, en concordancia con lo establecido en el Documento Base de Contratación»
- **Paráfrasis:** La Comisión de Recepción, que integra el Fiscal de la obra, recibe la obra en sus etapas provisional y definitiva verificando especificaciones, términos y condiciones del contrato.
- **Uso sugerido:** Cap.1 marco legal (recepción y cierre)

**dbc2022-43** · PDF p. 90 · cita: p. 86 · Cláusula trigésima octava, 38.1 (Liquidación de saldos) · *requisito_normativo*
> «Dentro de los diez (10) días calendario siguientes a la fecha de Recepción Provisional, el SUPERVISOR elaborará una planilla de cantidades finales de obra, con base a la Obra efectiva y realmente ejecutada»
- **Paráfrasis:** La planilla de cantidades finales debe basarse en la obra efectiva y realmente ejecutada, criterio clave para verificar cómputos que incluyan elementos no ejecutados.
- **Uso sugerido:** Cap.1 marco legal (medición y pago) | Cap.3 Discusión (cómputo del acero y planilla de cierre, a verificar por la Supervisión) | Cap.1 marco legal (recepción y cierre)

**dbc2022-44** · PDF p. 91 · cita: p. 87 · Cláusula trigésima octava, 38.2 (Recepción Definitiva) · *requisito_normativo*
> «Ningún otro documento que no sea el Acta de Recepción Definitiva de la Obra podrá considerarse como una admisión de que el contrato, o alguna parte del mismo, ha sido debidamente ejecutado»
- **Paráfrasis:** Solo el acta de recepción definitiva acredita que el contrato, o una parte de él, fue debidamente ejecutado; las planillas pagadas no equivalen a aceptación.
- **Uso sugerido:** Cap.1 marco legal (recepción y cierre)

**dbc2022-45** · PDF p. 92 · cita: p. 88 · Cláusula trigésima novena (Cierre de contrato) · *requisito_normativo*
> «El cierre de Contrato deberá ser acreditado con un CERTIFICADO DE CUMPLIMIENTO DE CONTRATO, otorgado por la ENTIDAD, luego de la recepción definitiva»
- **Paráfrasis:** El contrato se cierra con el certificado de cumplimiento que emite la entidad después de la recepción definitiva y de la liquidación.
- **Uso sugerido:** Cap.1 marco legal (recepción y cierre)

## 15. Síntesis para la redacción

### Requisitos de ACI CODE-318-25 para el control del hormigón de la losa (página impresa; PDF = impresa + 1)

| Requisito | Sección | Página |
|---|---|---|
| Materiales: cemento según Tabla 26.4.1.1.1(a); áridos ASTM C33/C330; agua ASTM C1602 | 26.4.1.1.1, 26.4.1.2.1, 26.4.1.4.1 | pp. 568–570 |
| Dosificación: sin segregación, durable, con los mismos materiales de la obra; documentarla y someterla a revisión antes de usarla o cambiarla | 26.4.3.1, 26.4.4.1 | pp. 576–577 |
| Almacenamiento sin deterioro ni contaminación; producción según ASTM C94/C685 | 26.5.1.1 | p. 578 |
| Colocación sin segregación ni juntas frías; continuidad por paño; compactación | 26.5.2.2 | pp. 579–580 |
| Curado: retener humedad 7 días a ≥ 50 °F (10 °C), o 3 días si se alcanza 0,7 f′c; eficacia ≥ 85 % de probetas normalizadas | 26.5.3.2(a), (e) | pp. 581–582 |
| Tiempo frío y caluroso: plan de hormigonado del contratista revisado por el profesional responsable; sin hielo en áridos, encofrados ni terreno; 95 °F máx. al colocar (comentario) | 26.5.4–26.5.5 | pp. 583–584 |
| Armaduras: certificados de fábrica; limpias al vaciar; tolerancias de la Tabla 26.6.2.1(a); fijadas para no desplazarse | 26.6.1.2, 26.6.2 | pp. 587–589 |
| Ensayo de resistencia = promedio de ≥ 2 cilindros (ASTM C172, C31, C39) a 28 días | 26.12.1.1(a) | p. 601 |
| Muestreo: 1 vez al día, cada 150 yd³ (≈ 114,7 m³) y cada 5000 ft² (≈ 464,5 m²) de losa; mínimo 5 ensayos por mezcla; aleatorio | 26.12.2.1 | p. 603 |
| Aceptación: promedio de 3 consecutivos ≥ f′c y ningún ensayo < f′c − 500 psi si f′c ≤ 5000 psi (≈ 214,8 kg/cm² para H25) | 26.12.3.1 | p. 603 |
| Probetas curadas en obra para desencofrar o retirar puntales | 26.12.4.1 | p. 604 |
| Investigación de resultados bajos: núcleos (3 por ensayo), aceptables si promedio ≥ 0,85 f′c y ninguno < 0,75 f′c; luego cap. 27 | 26.12.7 (no 26.12.6) | pp. 606–607 |
| Inspección por profesional o inspector calificado; registros ≥ 2 años; registro de vaciados y temperaturas; inspección continua de la mezcla y periódica de armado, curado y encofrados | 26.13 | pp. 608–611 |

### Artículos clave de la legislación (citar por artículo; las NB-SABS compiladas tienen página = PDF)

| Tema | Fuente | Localizador |
|---|---|---|
| Responsabilidad por la función pública (administrativa, ejecutiva, civil, penal) | Ley 1178 | arts. 1 c), 28–31; jurisdicción coactiva fiscal, art. 47 |
| Control interno previo y posterior | Ley 1178 | arts. 13–14 |
| Fuerza mayor y caso fortuito | D.S. 0181 | art. 5 c) y p) (compilado pp. 20 y 22) |
| Garantía de cumplimiento 7 %, vigente hasta la recepción definitiva | D.S. 0181 | art. 21 I b) (pp. 35–36) |
| Recepción provisional y definitiva | D.S. 0181 | art. 39 (p. 54) |
| Contrato modificatorio ≤ 10 %; orden de cambio ≤ 5 %; ambos ≤ 15 % (LP) o ≤ 10 % (ANPE); ítems nuevos con precios negociados | D.S. 0181 | art. 89 (pp. 91–93) |
| Contratación por excepción tras una resolución | D.S. 0181 | art. 65 c) (p. 71) |
| Registro de la resolución en el SICOES (20 días hábiles) | Manual SICOES en el compilado | num. 37.1 (p. 264) |
| Ajuste de precios de materiales importados (acero corrugado en el Anexo) | D.S. 5321 → 5406 → 5452 | arts. 1, 3 y 4; Anexo num. 1 |
| Ajuste de precios 2026 por encima de los límites del art. 89, hasta el 31/12/2026; resolución como caso fortuito sin ejecución de garantía | D.S. 5597 | arts. 1–4; DA tercera y quinta |
| Supervisor responsable directo del control de calidad; ensayos a cargo del contratista; trabajos no se cubren sin aprobación | DBC 2022 (sustituido) | cl. 26.3, 26.6, 26.10 (pp. 72–74) |
| Libro de Órdenes | DBC 2022 | cl. 25 (p. 71) |
| Medición neta; sin pago de excedentes no aprobados; planilla final con obra realmente ejecutada | DBC 2022 | cl. 27 (p. 75) y 38.1 (p. 86) |
| Multas por mora y resolución al 10 %/20 % | DBC 2022 | cl. 21.2.1 i)-j) (p. 68) y 32 (pp. 78–79) |

### Páginas de Hernández-Sampieri y Mendoza (2018) más útiles (número impreso)

| Tema | Páginas |
|---|---|
| Ruta cuantitativa | 5–7 |
| Alcances (exploratorio 106, descriptivo 108, correlacional 109, explicativo 110–112, mixtos 113) | 104–116 |
| Hipótesis (definición 124; de investigación 127; direccionales 129–131; nula 133; prueba 135) | 122–140 |
| Definición operacional | 137–138 |
| Diseño y experimento | 150–151 |
| Validez interna y amenazas (Tabla 7.1: historia, maduración, instrumentación, selección, mortalidad…) | 158–159 |
| Preexperimentos y preprueba-posprueba con un grupo (G M1 X M2) | 161–163 |
| Cuasiexperimentos | 173 |
| No experimentales: definición, transeccionales, retrospectivos, longitudinales | 174–183 |
| Censo y muestra no probabilística | 196, 200, 215 |
| Confiabilidad, validez, validez de contenido y de expertos | 228–239 |
| Nivel de significancia 0,05 | 341–342 |
| Supuestos paramétricos (normalidad), prueba *t*, no paramétricos, tabla de pruebas (Wilcoxon solo nombrada) | 343–372 |
| No están en la obra impresa: Shapiro-Wilk, simulación Monte Carlo, V de Aiken | — |

### Normas de pago incluidas en el `.bib` (sin PDF en el repositorio; no fichadas textualmente)

`iso9001_2026` (ISO 9001:2026), `iso9000_2026` (ISO 9000:2026), `ibnorca9001_2026` (NB/ISO 9001:2026), `iso10005_2018` (ISO 10005:2018), `iso10006_2017` (ISO 10006:2017), `nb997_2016` (NB 997:2016), `nb1225001_2017` (NB 1225001-1:2017), `cbh87` (CBH-87, 1987; autor y editor por verificar), `astmc31` (C31/C31M-26b), `astmc39` (C39/C39M-26), `astmc143` (C143/C143M-26b), `astmc172` (C172/C172M-25) y `astma615` (A615/A615M-26), con las ediciones de `Bibliografia_Recomendada.md`.

### Pendientes y advertencias

1. **Claves duplicadas** con `bib/00_base.bib` al generar este archivo: `ds0181_2009`, `ds5321_2025`, `ds5597_2026`, `ibnorca9001_2026`, `iso10005_2018`, `iso9000_2026`, `iso9001_2026`, `nb1225001_2017`, `nb997_2016`. Biber conserva la primera definición que carga (00_base.bib) y avisa «Duplicate entry key»; conviene dejar una sola (las de este archivo están contrastadas con los PDF: fecha completa, autor corporativo, ISBN).
2. **NB 1225001:** ni la NBDS ni la R.M. 271/2023 la declaran obligatoria; la obligatoriedad documentada es la de la NBDS. La R.M. MOPSV 172/2020 mencionada en `Bibliografia_Recomendada.md` no está en el repositorio. Tampoco hay en él texto del D.S. 22976/1991 sobre la CBH-87.
3. **DBC:** el modelo de 2022 fue sustituido por la R.M. 048/2024; descargar del SICOES el DBC y el contrato reales de la obra (CUCE 25-0143-00-1531493-1-1) antes de afirmar qué cláusulas rigen.
4. **Hernández-Sampieri** no cubre Shapiro-Wilk, Monte Carlo ni V de Aiken: buscar fuentes específicas (nivel 1 o 3) para esas técnicas.
5. **Gaceta Oficial:** ninguno de los PDF de decretos indica número de edición; las referencias lo omiten.
