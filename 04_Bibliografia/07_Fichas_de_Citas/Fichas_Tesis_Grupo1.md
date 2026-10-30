# Fichas de citas — Tesis, grupo 1

Fichaje bibliográfico de 14 trabajos de grado (16 PDF) de `04_Bibliografia/03_Tesis/`, en orden alfabético de archivo.
Cada documento incluye la referencia APA 7 verificada en la portada y páginas preliminares, una fila de la tabla de
antecedentes y sus fichas. Archivo de máquina: `Fichas_Tesis_Grupo1.json` (mismas fichas). Entradas BibLaTeX:
`05_Tesis_LaTeX/bib/tesis_grupo1.bib`.

**Convenciones**

- `texto_exacto` es copia literal de la capa de texto (PyMuPDF). Lo único normalizado son los espacios: saltos de línea
  y espacios dobles se reducen a un espacio, lo que `page.search_for` tolera. Cada cita se verificó con
  `page.search_for(texto_exacto[:60])` y con el texto completo en `pagina_pdf`. Las erratas del original se conservan.
- `pagina_pdf` = índice 1-based del archivo; `pagina_citable` = número impreso en la página. Todas las fichas tienen capa
  de texto (`capa_de_texto: true`).
- Las paráfrasis usan formato boliviano de números (punto de miles, coma decimal). Lo marcado como *cálculo propio* u
  *observación propia* es nuestro, no del autor. Las **[Notas de verificación]** son para el tesista: no van en el texto.
- No se cita de segunda mano: cuando la ficha recoge un dato que el autor toma de otra fuente, la paráfrasis lo dice.

**Advertencias generales**

- Los repositorios en línea (`repositorio.umsa.bo`, `tesis.pucp.edu.pe`) no son accesibles desde esta sesión (red no
  permitida). Los *handles* se tomaron de `Bibliografia_Recomendada.md`, y los años de publicación en repositorio que
  difieren de la portada se mantienen y se señalan; hay que confirmarlos cuando se habilite el acceso.
- En la memoria laboral de Cajías Luna (2023) faltan las pp. 153–293: la Parte 1 llega a la p. 152 y la Parte 2 empieza
  en la p. 294.
- Aguilar Caseux y Torres Benites (2016, pp. 48–50) reproducen casi literalmente las definiciones de costos de prevención,
  evaluación y fallas de Alfaro Félix (2011, pp. 12–13). Para esas definiciones conviene citar a Alfaro Félix.
- Cabrera Bellido y Vásquez Sangama (2021) presentan cifras y frases que coinciden con Galarza Meza (2011): 4.796 frente
  a 3.918 m³ y 22 %; acero con 7 %, 4,04 % y 3,75 %; trabajo no productivo de 23 % a 12 %. Es una inconsistencia
  documental que debe verificarse. Para esas cifras conviene citar a Galarza Meza (2011).

_Documentos fichados: 14 de 14 · fichas: 106._

## Tabla de antecedentes (resumen)

| Autor (año) | País | Institución | Objetivo | Diseño y muestra | Resultados con cifras | Relación con nuestra tesis |
|---|---|---|---|---|---|---|
| Aguilar Caseux y Torres Benites (2016) | Perú (Trujillo) | Universidad Privada Antenor Orrego | Determinar los costos de calidad y de no calidad en las estructuras de las obras de COAM Contratistas S.A.C. (ene.–jun. 2015) y su efecto en la rentabilidad. | Población = muestra (proyectos en ejecución de la empresa); datos solo de la obra Luzmila III (12 pisos) porque la otra obra se paralizó; método inductivo-deductivo; observación directa y prueba documentaria; registros de control de concreto, encofrado y acero; estadística descriptiva. | Hormigón de placas: S/ 960,41 (no calidad) frente a S/ 966,42 (calidad); valorización semanal S/ 2.997,35 frente a S/ 3.048,41; rentabilidad −41 % y −42 %; sin probetas ni slump por falta de equipo; la hipótesis no se confirmó. | Antecedente y discusión: costeo de calidad y no calidad por partida de hormigón armado (incluye losa aligerada) y ejemplo de control ausente (probetas, curado). Modelo de registro de control. |
| Alcón Aranda (2009) | Bolivia (La Paz) | Universidad Mayor de San Andrés, Facultad Técnica (Construcciones Civiles) | Presentar el proceso de fabricación, el control de calidad y la aplicación en obra de las viguetas pretensadas. | Estudio técnico descriptivo con seguimiento en planta y en obra: control estadístico de la resistencia del hormigón (probetas), tracción de trenzas, inspección visual por lotes y ensayos de carga; recomendaciones de recepción y ejecución en obra. | Hormigón de viguetas: fm = 443,50 kg/cm², S = 25,97 kg/cm² (control «excelente»); trenzas de 1.987 a 1.995 MPa (> 1.813 MPa); lotes de viguetas > 5,00 m rechazados por 3 defectos secundarios; losa de 17 cm con viguetas y plastoformo de 173,80 kg/m² y 1,00 h/m², frente a 408,00 kg/m² y 2,50 h/m² de la losa llena. | Marco teórico del sistema de losa y procedimiento de recepción de viguetas en obra (Cap. 2: PPI). Sustenta la discusión sobre el efecto de la supervisión en la calidad. |
| Alfaro Félix (2011) | Perú (Lima) | Pontificia Universidad Católica del Perú | Ofrecer los conceptos y herramientas para entender, diseñar, implementar, mantener y mejorar un SGC según ISO 9001:2000 en una empresa constructora y en un proyecto. | Monografía con estudio de caso: revisión conceptual y normativa, experiencias de tres constructoras peruanas, implementación en HV Contratistas S.A. y en el Condominio Residencial Parque de Monterrico (registros de calidad y no conformidades). | 675 registros de calidad y 26 no conformidades (junio–setiembre), con eficiencia del sistema de 96,1 %; concreto: 201 registros y 14 no conformidades; acero: 189 y 3; encofrado: 175 y 6; partidas de control elegidas con la regla 80/20; costos de implementación bajos. | Marco teórico (modelo PEF y CRC = CDC + CNC), selección de partidas de control (justifica centrarse en el ítem 13) e indicador de no conformidades por registro para el Cap. 2. |
| Álvarez Quintero (2014) | Colombia (Cartagena) | Universidad de Cartagena | Analizar críticamente el efecto de la gestión de la calidad en la reducción de los reprocesos en proyectos de construcción civil. | Revisión de literatura con análisis crítico de estudios internacionales (2000–2014); sin trabajo de campo. | Reprocesos de hasta 12,4 % del costo (promedio 6,59 %, de 8 estudios); con SGC, 0,72 % (Australia) y en promedio 1 %; reducción estimada de 84,82 % (de 6,59 % a 1 %); Barclay Construction pasó de 5 % a menos de 1 % del contrato. | Introducción (magnitud del problema) y discusión: referencia de reducción esperable con un SGC frente a nuestro criterio de r ≥ 5 %. Dato secundario: usar con cautela. |
| Cabrera Bellido y Vásquez Sangama (2021) | Perú (Iquitos) | Universidad Científica del Perú | Analizar el desperdicio de materiales en obras de edificación de Iquitos y sus métodos de control y medición. | Descriptivo correlacional; muestra por conveniencia de 2 edificaciones públicas (obras A y B, 2016–2017); observación con lista de cotejo, guías de observación y de análisis; chi cuadrado, Spearman y Kendall declarados. | Índice de residuos de 0,13 y 0,10 m³/m² techado; hormigón 3,6 % (verticales) y 1,6 % (horizontales) en la obra A; acero 0,25 % (A) y 0,10 % (B), frente a 5 % del expediente técnico; ahorro de ≈ S/ 7.000 en eliminación de desmonte (360 m³). Cifras con inconsistencias. | Marco teórico (pérdida relativa a una situación de referencia) y discusión. Usar con cautela por las coincidencias con Galarza Meza (2011). |
| Cajías Luna (2023) | Bolivia (El Alto, La Paz) | Universidad Mayor de San Andrés | Plantear un método de control de calidad de obras viales con pavimento rígido aplicado a la supervisión de una obra municipal (pavimentado de la Av. Las Kantutas, El Alto). | Memoria laboral con método descriptivo: sistematiza la experiencia del autor como supervisor del GAM de El Alto (2006–2015) y describe documentos, flujos de control técnico y administrativo y plan de calidad de la obra. | Procedimientos de supervisión: certificados de calidad de materiales, ensayos confirmatorios por lote, presencia del supervisor en el muestreo y el ensayo, rechazo de resultados dudosos, límites de 5 % (orden de cambio) y 10 % (contrato modificatorio). Sin cifras de costos de calidad. | Marco normativo y procedimental boliviano de la supervisión (Cap. 1 y 2): sustenta la exigencia de muestreo presenciado y la crítica al certificado n.º 000293, con probetas elaboradas por el contratista. |
| Calizaya Paco (2022) | Bolivia (La Paz) | Universidad Mayor de San Andrés (Maestría en Administración de Negocios) | Diseñar un modelo de predicción de la demanda de los principales productos de acero para obras civiles en Importadora Colinas S.R.L. | Aplicado, descriptivo, no experimental, longitudinal (2017–2019); censo no probabilístico de 9 directivos y 3 gestiones de ventas; encuesta con preguntas cerradas y análisis documental. | Quiebres de stock en 2019: 6.449 t de fierro corrugado sin atender (10,96 % de la demanda) y 8.653 t en total (USD 8.106.016); hipótesis aceptada con «porcentaje de aceptabilidad» de 5/5; proyección 2021 de 47.500 t de fierro corrugado con «probabilidad de 94 %» sin método explícito. | Contexto del abastecimiento de acero en Bolivia (situación problemática: escasez y retrasos de fierro) y contraejemplo metodológico de contraste de hipótesis sin inferencia estadística. |
| Capcha Canaza (2016) | Bolivia (La Paz/El Alto) | Universidad Mayor de San Andrés (Ingeniería Industrial) | Diseñar e implementar la certificación de viguetas pretensadas con sello IBNORCA (NB 997) y un SGC en PREVITEC S.R.L. | Proyecto de grado aplicado: diagnóstico con listas de verificación (NB 997 y anexo 2 del reglamento del sello, NB ISO 9001:2008), diseño documental del SGC, plan de calidad, ensayos e inspección por lotes, y costos de calidad con y sin proyecto (CAE). | Incumplimiento de 88 % de la NB 997; reglamento del sello: 64 % de incumplimiento, 19 % parcial y 17 % de cumplimiento; costos de calidad sin proyecto Bs 292.851 (2016), con 31 % por fallas externas; con proyecto Bs 540.431 el primer año y luego Bs 161.323–193.550 al año; CAE menor con el proyecto. | Criterios de recepción de viguetas (defectos, tolerancias, aceptación por lote) para el PPI del Cap. 2 y antecedente de costos PEF con y sin SGC en un fabricante boliviano. |
| Castañeda Briceño (2017) | Perú (Lima) | Universidad César Vallejo | Determinar si el uso de viguetas pretensadas en losas aligeradas incrementa la productividad en la obra Escuela PNP de Puente Piedra. | Aplicada, no experimental, transversal, descriptiva comparativa; observación participante con fichas de recopilación de datos validadas por 3 expertos («aplicable», sin coeficiente); una losa de 271,05 m² comparada con el sistema convencional mediante presupuestos. | Costo 27 % menor (S/ 60.476,97 frente a S/ 82.763,19 para 271,05 m²); tiempo 40 % menor (3 frente a 5 días); peso «14 % menor» según el texto, aunque la tabla da 287 frente a 300 kg/m² (≈ 4,3 %). | Antecedente sobre el sistema de viguetas pretensadas (costo, plazo y peso) y ejemplo de validación por expertos sin coeficiente, frente a la V de Aiken prevista en nuestra tesis. |
| Ccoyllo Sifuentes (2016) | Perú (Lima, San Borja) | Universidad César Vallejo | Mejorar la productividad de las partidas de mayor incidencia para reducir el desperdicio de materiales en un edificio de 5 niveles y 2 sótanos. | Aplicada, explicativa, no experimental; muestreo intencional; observación con cartas balance y registro de desperdicios en dos etapas de la obra; validez «aceptable» por juicio de expertos, sin coeficiente. | Materiales = 55 % del costo directo; desperdicio final de ladrillo 4,03 % y de mezcla de tarrajeo 6,57 %; productividad +8,2 % (ladrillo) y +7,3 % (tarrajeo); falta de control de almacén en la recepción como causa de desperdicio. | Marco teórico del desperdicio (directo e indirecto; % aceptables de CAPECO) y causas ligadas a la recepción de materiales (Cap. 2: diagnóstico de causas). |
| Cepeda Godoy (2017) | Ecuador (Riobamba) | Universidad de Cuenca (Maestría en Construcciones) | Analizar la gestión de calidad en la planificación y construcción de edificios de departamentos de Riobamba y crear un plan de control de calidad. | Encuestas (preguntas dicotómicas y de selección simple) a 15 planificadores y constructores, de una población de 158, y entrevistas a 10 autoridades de control; muestreo intencional; contraste con la distribución muestral de proporciones (α = 0,05). | 60 % de los encuestados (9 de 15) atribuye 90 % de incidencia a implantar un plan de gestión de calidad; Z = −12,96 y rechazo de H0 (procedimiento cuestionable); plan con control de recepción de materiales y ensayos en laboratorios independientes y acreditados. | Modelo de plan de control de calidad (recepción, ejecución y obra terminada) para el Cap. 2 y contraejemplo de cálculo muestral y de contraste para el Cap. 3. |
| Chafloque Rodriguez (2024) | Perú (provincia del Santa, Áncash) | Universidad César Vallejo (Escuela de Posgrado) | Determinar la influencia de la gestión de abastecimiento de materiales de construcción en la calidad de un proyecto de edificaciones. | Aplicada, cuantitativa, no experimental transversal, correlacional causal; muestra no probabilística de 80 colaboradores de 8 proyectos; cuestionarios Likert; validación por 3 jueces (sin coeficiente); alfa de Cronbach de 0,944 y 0,804 (piloto de 15); Kolmogorov-Smirnov, rho de Spearman y pseudo R² de Nagelkerke. | ρ = 0,512 (p < 0,05); pseudo R² = 0,401; 42,5 % de los casos con abastecimiento y calidad óptimos; dimensión «asegurar el suministro» con influencia de 77,8 %. | Antecedente del vínculo entre el abastecimiento o control de materiales y la calidad, y referencia de validación y confiabilidad de instrumentos para el Cap. 2. |
| Chino Quispe y Zarate Chilqquetuma (2024) | Perú (Cusco) | Universidad Nacional de San Antonio Abad del Cusco | Reducir el desperdicio de acero de refuerzo (material y mano de obra) con el despiece pre ejecución, comparado con el acero dimensionado y el uso convencional. | Aplicada, cuantitativa (o «mixta»), de nivel experimental en 2 edificios multifamiliares de más de 8 pisos; registro de ingresos de acero, metrado diario, horas-hombre y cotizaciones; desperdicio medido como exceso sobre el metrado teórico. | Desperdicio convencional de 14,58 % (7.312,57 kg) y 17,09 % (17.808,75 kg); con despiece, 3,15 % y 3,19 % medidos, y 8,94 % y 6,71 % proyectados; productividad de habilitado de 0,014 a 0,021 hh/kg; utilidad +1,48 % y +5,87 %. | Método de medición del desperdicio (consumo real frente a metrado) para el Cap. 2 y referencia de desperdicio de acero; precedente de proyección ex ante, análogo a nuestra simulación de la segunda y tercera losa. |
| Cocarico Mamani (2022) | Bolivia (La Paz) | Universidad Mayor de San Andrés | Comparar técnica y económicamente entrepisos de losa nervada postensada con tendones no adheridos y de losa nervada de HºAº en el Edificio Ares (25 niveles y 2 sótanos). | Proyecto de grado de análisis comparativo: dos modelos estructurales con la misma arquitectura, diseño según la NB 1225001, verificación de estados límite, cómputos métricos, precios unitarios (formulario B-2) y cronogramas (MS Project). | Estructura 20 % más liviana (21.636 frente a 27.134 t); 26 % menos acero pasivo; costo 2,53 % menor (11,66 % sin fundación); plazo de 403 frente a 484 días (−16,7 %); incidencias: beneficios sociales 71 %, herramientas 5 %, gastos generales 13 %, utilidad 10 %, IVA 14,94 % e IT 3,09 %. | Referencia boliviana para la estructura del precio unitario (costos directos e incidencias) del modelo de costos del Cap. 2 y contexto de sistemas de losa. No trata la gestión de la calidad. |

## 1. Aguilar Caseux y Torres Benites (2016) — costos de calidad y de no calidad (UPAO, Perú)

**Referencia APA 7 (verificada):** Aguilar Caseux, K. O., & Torres Benites, V. Y. (2016). *Costos de calidad y costos de no calidad en las estructuras de las obras de COAM Contratistas SAC, 2015* [Tesis de licenciatura, Universidad Privada Antenor Orrego]. https://hdl.handle.net/20.500.12759/2055

**Archivo(s):** `04_Bibliografia/03_Tesis/Aguilar_Torres_2016_Tesis_Costos_Calidad_No_Calidad_Estructuras_UPAO.pdf` (346 págs.)

**Verificación de portada y correcciones a la referencia propuesta:**

- Portada (pág. PDF 1): Universidad Privada Antenor Orrego, Facultad de Ingeniería, Escuela Profesional de Ingeniería Civil; «Tesis para optar el título profesional de Ingeniero Civil»; autores Kevin O’snar Aguilar Caseux y Viviana Yoreli Torres Benites; asesor Ms. Carlos Manuel Vargas Cárdenas; Trujillo, Perú.
- El título y los autores coinciden con la referencia propuesta.
- Año: la portada dice «Diciembre 2015»; la referencia propuesta (repositorio) dice 2016. Se conserva 2016 (año de publicación en el repositorio, handle 20.500.12759/2055) y la clave `aguilar2016`; confirmar en el repositorio.
- Las definiciones de costos de prevención, evaluación y fallas (pp. 48–50) reproducen casi literalmente a Alfaro Félix (2011, pp. 12–13): para esas definiciones citar a Alfaro Félix.

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Aguilar Caseux y Torres Benites (2016) |
| País | Perú (Trujillo) |
| Institución | Universidad Privada Antenor Orrego |
| Objetivo | Determinar los costos de calidad y de no calidad en las estructuras de las obras de COAM Contratistas S.A.C. (ene.–jun. 2015) y su efecto en la rentabilidad. |
| Diseño y muestra | Población = muestra (proyectos en ejecución de la empresa); datos solo de la obra Luzmila III (12 pisos) porque la otra obra se paralizó; método inductivo-deductivo; observación directa y prueba documentaria; registros de control de concreto, encofrado y acero; estadística descriptiva. |
| Resultados (cifras) | Hormigón de placas: S/ 960,41 (no calidad) frente a S/ 966,42 (calidad); valorización semanal S/ 2.997,35 frente a S/ 3.048,41; rentabilidad −41 % y −42 %; sin probetas ni slump por falta de equipo; la hipótesis no se confirmó. |
| Relación con nuestra tesis | Antecedente y discusión: costeo de calidad y no calidad por partida de hormigón armado (incluye losa aligerada) y ejemplo de control ausente (probetas, curado). Modelo de registro de control. |

**Fichas (8):**

**aguilar2016-01** · p. 9 (pág. PDF 23) · *metodo* · Uso: Introducción-Antecedentes de investigación | Cap.3 Discusión (3.7)

> «Demostrar que los estudios de costos de calidad y costos de no calidad en las estructuras de las obras influyen positivamente en la rentabilidad de la empresa COAM Contratistas S.A.C. 2015.»

Paráfrasis: Aguilar Caseux y Torres Benites (2016) plantearon como hipótesis que el estudio de los costos de calidad y de no calidad en las estructuras de las obras de COAM Contratistas S.A.C. influye positivamente en la rentabilidad de la empresa; la variable independiente fue el estudio de esos costos y la dependiente, la rentabilidad (p. 9).

**aguilar2016-02** · p. 55 (pág. PDF 69) · *metodo* · Uso: Introducción-Metodología de la investigación (población y muestra)

> «La población coincidirá con la muestra como estudio de investigación se centra en los proyectos de ejecución de la empresa COAM Contratistas S.A.C. constituida legalmente en la ciudad de Trujillo.»

Paráfrasis: La investigación trabajó con una población igual a la muestra, los proyectos en ejecución de COAM Contratistas S.A.C. en Trujillo, con método inductivo-deductivo y técnicas de observación directa y prueba documentaria (Aguilar Caseux y Torres Benites, 2016, p. 55).

**aguilar2016-03** · p. 60 (pág. PDF 74) · *metodo* · Uso: Cap.2 sección 2.1 (alcance del modelo ante la paralización de la obra) | Cap.3 Discusión (3.7)

> «La toma de datos de las partidas solamente se realizó en la obra Residencial Luzmila III, ya que el Conjunto Residencial Albrecht II sufrió una paralización el día 5 de junio del 2015»

Paráfrasis: Aguilar Caseux y Torres Benites (2016) restringieron la toma de datos a la obra Residencial Luzmila III porque el Conjunto Residencial Albrecht II se paralizó el 5 de junio de 2015, con solo las calzaduras y cerca del 65 % de los muros pantalla, sin partidas de concreto armado que medir (p. 60). Es un precedente de ajuste del diseño de investigación ante la paralización de una obra.

**aguilar2016-04** · p. 43 (pág. PDF 57) · *definicion* · Uso: Cap.1 sección 1.4 (costos de la calidad)

> «Se define los costos de calidad como: “Los costos en los que la empresa incurre para asegurar que el producto cumple con las especificaciones y requisitos establecidos en la fase de diseño”.»

Paráfrasis: Para Aguilar Caseux y Torres Benites (2016), los costos de calidad son los que asume la empresa para asegurar que el producto cumpla las especificaciones y los requisitos fijados en la fase de diseño, e incluyen aspectos económicos, materiales e inmateriales de difícil cuantificación (p. 43).

**aguilar2016-05** · p. 81 (pág. PDF 95) · *conclusion* · Uso: Introducción-Antecedentes de investigación | Cap.3 Discusión (3.7)

> «hay malos procesos constructivos y en su mayoría se dieron por la ausencia del residente de obra, por lo que se determina que las pérdidas se generan principalmente por la deficiente administración del contratista.»

Paráfrasis: En la obra estudiada no se contó con topógrafo ni con capacitación para el vibrado, y hubo malos procesos constructivos, atribuidos sobre todo a la ausencia del residente de obra; los autores concluyeron que las pérdidas se originan principalmente en la deficiente administración del contratista (Aguilar Caseux y Torres Benites, 2016, p. 81).

**aguilar2016-06** · p. 81 (pág. PDF 95) · *hallazgo* · Uso: Cap.3 sección 3.3 (control del hormigón) | Cap.3 Discusión (3.7)

> «Contratistas y obreros no dieron la importancia que amerita el curado del concreto, la realización de probetas y el ensayo del SLUMP debido a que no contaron con el equipo adecuado.»

Paráfrasis: Contratistas y obreros no dieron importancia al curado del hormigón, a la elaboración de probetas ni al ensayo de asentamiento (slump) porque no contaban con el equipo adecuado (Aguilar Caseux y Torres Benites, 2016, p. 81); el registro de control del vaciado consigna que no se hicieron probetas ni ensayo de slump (p. 64).

**aguilar2016-07** · p. 81 (pág. PDF 95) · *dato* · Uso: Cap.1 sección 1.4.1 (modelo PEF) | Cap.3 sección 3.4 (resultados de costos)

> «la empresa obtiene con el costo de no calidad en el concreto en placas f´c =210 Kg/cm2 en S/. 960.41, cuando en realidad cumpliendo todos los parámetros constructivos y el registro de control de calidad S/. 966.42»

Paráfrasis: Con solo el costo directo, el hormigón f'c = 210 kg/cm² en placas costó S/ 960,41 tal como se ejecutó (costo de no calidad) y habría costado S/ 966,42 cumpliendo los procedimientos y el registro de control de calidad (costo de calidad); en la valorización semanal, S/ 2.997,35 frente a S/ 3.048,41 (Aguilar Caseux y Torres Benites, 2016, p. 81). Cumplir el control habría elevado el costo directo en 0,6 % y 1,7 %, respectivamente (cálculo propio).

**aguilar2016-08** · p. 82 (pág. PDF 96) · *conclusion* · Uso: Cap.3 Discusión (3.7)

> «en el concreto en placas con f’c=210kg/cm2 obtenemos con los costos de no calidad una rentabilidad del -41% y con los costos de calidad una rentabilidad -42%, por lo que se tienen perdidas en la ejecución del proyecto»

Paráfrasis: En las placas de hormigón f'c = 210 kg/cm² la rentabilidad fue de −41 % con costos de no calidad y de −42 % con costos de calidad. Los autores atribuyen las pérdidas a que el expediente técnico no tuvo un análisis de costos unitarios adecuado y concluyen que el estudio de costos no influyó positivamente en la rentabilidad, contra su hipótesis (Aguilar Caseux y Torres Benites, 2016, p. 82).

## 2. Alcón Aranda (2009) — fabricación, control y aplicación de viguetas pretensadas (UMSA, Bolivia)

**Referencia APA 7 (verificada):** Alcón Aranda, M. W. (2009). *Evaluación del proceso de fabricación y aplicación de viguetas pretensadas en estructuras* [Tesis de licenciatura, Universidad Mayor de San Andrés]. https://repositorio.umsa.bo/handle/123456789/7465

**Archivo(s):** `04_Bibliografia/03_Tesis/Alcon_2009_Tesis_Viguetas_Pretensadas_Fabricacion_Aplicacion_UMSA.pdf` (154 págs.)

**Verificación de portada y correcciones a la referencia propuesta:**

- El PDF no tiene portada ni páginas preliminares: empieza en la «1. Introducción» (pág. PDF 1). Título, grado, año y tutor no pueden verificarse en el archivo. Se toman de la referencia propuesta (repositorio UMSA), que no fue accesible desde esta sesión.
- El encabezado de cada página dice «Universidad Mayor de San Andrés · Facultad Técnica – Construcciones Civiles · Marcelo W. Alcón Aranda». Corrección: el apellido lleva tilde (**Alcón**), y la carrera es Construcciones Civiles de la Facultad Técnica, no Ingeniería Civil. El tipo «Tesis de licenciatura» queda por confirmar en el repositorio.
- Año: el único dato interno es un registro de ensayo fechado el 23/05/2008. Se conserva 2009 (repositorio) y la clave `alcon2009`.
- La paginación impresa coincide con la del archivo (p. N = pág. PDF N).

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Alcón Aranda (2009) |
| País | Bolivia (La Paz) |
| Institución | Universidad Mayor de San Andrés, Facultad Técnica (Construcciones Civiles) |
| Objetivo | Presentar el proceso de fabricación, el control de calidad y la aplicación en obra de las viguetas pretensadas. |
| Diseño y muestra | Estudio técnico descriptivo con seguimiento en planta y en obra: control estadístico de la resistencia del hormigón (probetas), tracción de trenzas, inspección visual por lotes y ensayos de carga; recomendaciones de recepción y ejecución en obra. |
| Resultados (cifras) | Hormigón de viguetas: fm = 443,50 kg/cm², S = 25,97 kg/cm² (control «excelente»); trenzas de 1.987 a 1.995 MPa (> 1.813 MPa); lotes de viguetas > 5,00 m rechazados por 3 defectos secundarios; losa de 17 cm con viguetas y plastoformo de 173,80 kg/m² y 1,00 h/m², frente a 408,00 kg/m² y 2,50 h/m² de la losa llena. |
| Relación con nuestra tesis | Marco teórico del sistema de losa y procedimiento de recepción de viguetas en obra (Cap. 2: PPI). Sustenta la discusión sobre el efecto de la supervisión en la calidad. |

**Fichas (8):**

**alcon2009-01** · p. 115 (pág. PDF 115) · *metodo* · Uso: Cap.1 sección 1.6.2 (proceso constructivo) | Cap.2 sección 2.6.1 (procedimiento de recepción)

> «En obra, quizás uno de los aspectos más importantes es la recepción de cualquier tipo de material y en este caso el de las viguetas pretensadas, que es un aspecto importante para que la obra sea de calidad.»

Paráfrasis: Alcón Aranda (2009) señala que la recepción del material en obra, y en particular la de las viguetas pretensadas, es uno de los aspectos más importantes para que la obra sea de calidad (p. 115).

**alcon2009-02** · p. 115 (pág. PDF 115) · *metodo* · Uso: Cap.2 sección 2.6.1 (procedimiento de recepción) | Introducción-Justificación técnica

> «Dedicar unos minutos a la recepción y el control de calidad del material en el mismo momento de su descarga puede evitar muchos problemas durante y después de la ejecución de la obra.»

Paráfrasis: Controlar la calidad en el momento de la descarga permite exigir de inmediato el cambio del material defectuoso. Detectarlo cuando ya está colocado obliga a retirarlo, detiene la obra y genera pérdidas de tiempo y dinero (Alcón Aranda, 2009, p. 115).

**alcon2009-03** · p. 116 (pág. PDF 116) · *metodo* · Uso: Cap.2 sección 2.6.1 (lista de verificación de recepción de viguetas)

> «Que las cantidades y medidas de las viguetas que nos trae el camión coincidan con las que necesitamos o que nos fueron ofrecidas. - Que los tipos de viguetas que nos trae el camión coinciden con las del plano de montaje del propio proveedor.»

Paráfrasis: Al llegar las viguetas deben verificarse dos aspectos: que las cantidades y medidas coincidan con lo requerido u ofertado, y que los tipos de vigueta coincidan con el plano de montaje del proveedor. Ese plano debe acompañar la entrega, porque un error de tipología puede causar graves problemas estructurales (Alcón Aranda, 2009, p. 116).

**alcon2009-04** · p. 116 (pág. PDF 116) · *definicion* · Uso: Cap.1 sección 1.6.4 (defectos y fallas frecuentes) | Cap.2 sección 2.6.1 (no conformidades)

> «Graves: son aquellos que implican un riesgo para la estructura de la obra, o bien, impidan el montaje de las viguetas. En este caso es totalmente necesario devolver el material al proveedor y que éste lo sustituya por otro en buen estado.»

Paráfrasis: Alcón Aranda (2009) clasifica los defectos de las viguetas en dos grupos. Los leves no implican riesgo estructural pero dificultan el montaje, y su aceptación queda a criterio del supervisor. Los graves implican riesgo para la estructura o impiden el montaje, por lo que el material debe devolverse al proveedor para que lo reponga (p. 116).

**alcon2009-05** · p. 150 (pág. PDF 150) · *hallazgo* · Uso: Introducción-Antecedentes de investigación | Cap.3 Discusión (3.7)

> «Durante el proceso de fabricación se observó que cuando existe la adecuada supervisión, el producto a realizar va tener calidad óptima o buena, pero cuando no existe supervisión la calidad del producto es mala o regular.»

Paráfrasis: Durante la fabricación de viguetas se observó que, con una supervisión adecuada, el producto alcanza calidad óptima o buena, mientras que sin supervisión su calidad es mala o regular (Alcón Aranda, 2009, p. 150).

**alcon2009-06** · p. 150 (pág. PDF 150) · *dato* · Uso: Cap.1 sección 1.6.1 (componentes: viguetas) | Cap.3 sección 3.3

> «Los ensayos realizados al hormigón dieron como resultado una Resistencia Media de 443.50 Kg/cm2, estando por encima del valor teórico.»

Paráfrasis: Los ensayos del hormigón de las viguetas dieron una resistencia media de 443,50 kg/cm². El valor supera la resistencia media teórica de 400 kg/cm² exigida para una resistencia característica de 350 kg/cm² (Alcón Aranda, 2009, p. 150).

**alcon2009-07** · p. 58 (pág. PDF 58) · *metodo* · Uso: Cap.1 sección 1.7.4 (normas de ensayo) | Cap.3 sección 3.3 (evaluación de probetas)

> «El American Concrete Institute relaciona el grado de control de la obra con la magnitud de la desviación típica “S”, estableciendo para resistencias características superiores a 200 Kg/cm2 la siguiente calificación:»

Paráfrasis: Siguiendo al American Concrete Institute, Alcón Aranda (2009) califica el grado de control del hormigón con resistencia característica superior a 200 kg/cm² según su desviación típica S: excelente (S < 28 kg/cm²), muy bueno (28–35), bueno (35–42), regular (42–49) y pobre (> 49). Con S = 25,97 kg/cm², su producción resultó de control excelente (p. 58).

**alcon2009-08** · p. 151 (pág. PDF 151) · *dato* · Uso: Cap.1 sección 1.6.1 (descripción del sistema) | Cap.1 sección 1.6.3 (consumos)

> «Reducción del Peso Propio, debido al uso de elementos alivianantes, éste le reduce el peso propio a la losa, por lo tanto se reduce la acción de las cargas en la estructura.»

Paráfrasis: Los elementos alivianantes reducen el peso propio de la losa y, con él, las cargas sobre la estructura. Para 17 cm de altura, la losa con viguetas y plastoformo pesa 173,80 kg/m², con un rendimiento de 1,00 h/m² de albañil, frente a 408,00 kg/m² y 2,50 h/m² de la losa llena de HºAº (Alcón Aranda, 2009, p. 151).

## 3. Alfaro Félix (2011) — sistemas de aseguramiento de la calidad en la construcción (PUCP, Perú)

**Referencia APA 7 (verificada):** Alfaro Félix, O. C. (2011). *Sistemas de aseguramiento de la calidad en la construcción* [Tesis de licenciatura, Pontificia Universidad Católica del Perú]. http://hdl.handle.net/20.500.12404/185

**Archivo(s):** `04_Bibliografia/03_Tesis/Alfaro_2011_Tesis_Sistemas_Aseguramiento_Calidad_Construccion_PUCP.pdf` (95 págs.)

**Verificación de portada y correcciones a la referencia propuesta:**

- Portada (pág. PDF 2, hoja de tema): Pontificia Universidad Católica del Perú, Facultad de Ciencias e Ingeniería; «Tema para optar por el título de Ingeniero Civil: Sistemas de aseguramiento de la calidad en la construcción»; presentada por Omar Cristian Alfaro Felix (en mayúsculas, sin tilde); «Febrero 2008».
- Título y autor coinciden con la referencia propuesta. El índice interno titula el trabajo «Sistemas de aseguramiento de la calidad en el sector construcción»; se usa el título de la portada.
- Año: la hoja de tema dice febrero de 2008; el repositorio PUCP (handle 20.500.12404/185) consigna 2011. Se conserva 2011 y la clave `alfaro2011`; confirmar en el repositorio, que no fue accesible desde esta sesión. Aguilar Caseux y Torres Benites (2016) lo citan como «Alfaro Felix, 2014».
- Paginación impresa: p. N = pág. PDF N + 3.

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Alfaro Félix (2011) |
| País | Perú (Lima) |
| Institución | Pontificia Universidad Católica del Perú |
| Objetivo | Ofrecer los conceptos y herramientas para entender, diseñar, implementar, mantener y mejorar un SGC según ISO 9001:2000 en una empresa constructora y en un proyecto. |
| Diseño y muestra | Monografía con estudio de caso: revisión conceptual y normativa, experiencias de tres constructoras peruanas, implementación en HV Contratistas S.A. y en el Condominio Residencial Parque de Monterrico (registros de calidad y no conformidades). |
| Resultados (cifras) | 675 registros de calidad y 26 no conformidades (junio–setiembre), con eficiencia del sistema de 96,1 %; concreto: 201 registros y 14 no conformidades; acero: 189 y 3; encofrado: 175 y 6; partidas de control elegidas con la regla 80/20; costos de implementación bajos. |
| Relación con nuestra tesis | Marco teórico (modelo PEF y CRC = CDC + CNC), selección de partidas de control (justifica centrarse en el ítem 13) e indicador de no conformidades por registro para el Cap. 2. |

**Fichas (8):**

**alfaro2011-01** · p. 12 (pág. PDF 15) · *definicion* · Uso: Cap.1 sección 1.4.1 (modelo de prevención, evaluación y fallas)

> «Representan el costo de todas las actividades llevadas a cabo para evitar defectos desde los inicios de diseño, desarrollo y finalmente la comercialización un producto o servicio.»

Paráfrasis: Los costos de prevención comprenden todas las actividades destinadas a evitar defectos, desde el diseño y el desarrollo hasta la comercialización del producto: revisión de diseños y especificaciones, planes de aseguramiento de la calidad y evaluación y capacitación de proveedores, entre otras (Alfaro Félix, 2011, p. 12).

**alfaro2011-02** · p. 12 (pág. PDF 15) · *definicion* · Uso: Cap.1 sección 1.4.1 (modelo PEF) | Cap.2 sección 2.6.1 (costos de evaluación del plan)

> «Aquellos desembolsos generados por la búsqueda y detección de imperfecciones en los productos finales. Estos costos proceden de actividades de inspección, pruebas, evaluaciones que se han planeado para determinar el cumplimiento de los requisitos establecidos»

Paráfrasis: Los costos de evaluación son los desembolsos para buscar y detectar imperfecciones mediante inspecciones, pruebas y evaluaciones planificadas que verifican el cumplimiento de los requisitos, entre ellas las inspecciones y pruebas de aceptación y recepción (Alfaro Félix, 2011, p. 12).

**alfaro2011-03** · p. 38 (pág. PDF 41) · *definicion* · Uso: Cap.1 sección 1.4.2 (costo de no calidad y reprocesos)

> «Los costos relacionados a la No Calidad se refieren a aquellos gastos extras realizados al proyecto con la intención de rehacer o reparar productos por haberse realizado erróneamente en una primera oportunidad.»

Paráfrasis: Alfaro Félix (2011) define los costos de no calidad como los gastos adicionales para rehacer o reparar lo que se ejecutó mal la primera vez. Incluyen reprocesos, el reemplazo de materiales que no cumplen los requisitos de calidad y el tiempo para completar trabajos retrasados. Nunca se consideran en los presupuestos, por lo que son una pérdida neta (p. 38).

**alfaro2011-04** · p. 38 (pág. PDF 41) · *definicion* · Uso: Cap.1 sección 1.4 (costos de la calidad) | Cap.2 sección 2.5.4 (modelo de costos)

> «Los Costos relativos a la calidad de un proyecto (CRC) es la suma de los costos invertidos en el aseguramiento de la calidad más los costos de la no calidad»

Paráfrasis: Con base en un artículo de Gómez Sánchez, Alfaro Félix (2011) expresa los costos relativos a la calidad como CRC = CDC + CNC, es decir, la suma de lo invertido en aseguramiento de la calidad (CDC) y de los costos de no calidad (CNC). Una inversión controlada en CDC reduce los CNC a su mínima expresión (pp. 38–39).

**alfaro2011-05** · p. 70 (pág. PDF 73) · *metodo* · Uso: Cap.2 sección 2.3 (selección de partidas de control) | Cap.1 sección 1.9 (herramientas de la calidad)

> «aproximadamente el 80% de nuestros problemas de calidad radica en el 20% de las partidas de nuestro presupuesto, es por esta razón que una de las tareas principales al iniciar la obra fue definir las partidas de control.»

Paráfrasis: En la obra analizada se aplicó la regla de Pareto (el 80 % de los problemas de calidad se concentra en el 20 % de las partidas) para definir las partidas de control al iniciar la obra, con tres criterios: importancia económica, importancia técnica y ubicación en la ruta crítica (Alfaro Félix, 2011, p. 70).

**alfaro2011-06** · p. 84 (pág. PDF 87) · *dato* · Uso: Cap.2 sección 2.6.1 (indicadores del SGC) | Cap.3 Discusión (3.7)

> «Este informe pretende mostrar los resultados reales del sistema de aseguramiento de la calidad seguido en este proyecto»

Paráfrasis: El informe del sistema de aseguramiento de la calidad del Condominio Residencial Parque de Monterrico registró, de junio a setiembre, 675 registros de calidad y 26 no conformidades: 14 en vaciados de concreto (201 registros), 3 en refuerzo de acero (189) y 6 en encofrados (175). La eficiencia del sistema fue de 96,1 % (Alfaro Félix, 2011, p. 84, tabla 2).

**alfaro2011-07** · p. 87 (pág. PDF 90) · *conclusion* · Uso: Introducción-Justificación económica | Cap.3 Discusión (3.7)

> «Los costos de implementación son bajos, y cuando el departamento de calidad se encuentra establecido, los beneficios obtenidos justifican los gastos realizados.»

Paráfrasis: Alfaro Félix (2011) concluye que los costos de implementar un sistema de calidad son bajos y que, una vez establecido el departamento de calidad, los beneficios justifican los gastos (p. 87).

**alfaro2011-08** · p. 88 (pág. PDF 91) · *conclusion* · Uso: Introducción-Justificación económica | Cap.3 Discusión (3.7)

> «La aplicación de este tipo de mecanismos ha permitido verificar que el costo de diseñar y construir con calidad, es muchísimo menor que el de no hacerlo, para todos los involucrados»

Paráfrasis: La aplicación del sistema de aseguramiento permitió verificar que diseñar y construir con calidad cuesta mucho menos que no hacerlo. Por eso debe priorizarse la inversión en prevención, que reduce los costos de evaluación y de no calidad (Alfaro Félix, 2011, p. 88).

## 4. Álvarez Quintero (2014) — gestión de la calidad y reducción de reprocesos (U. de Cartagena, Colombia)

**Referencia APA 7 (verificada):** Álvarez Quintero, L. R. (2014). *Gestión de la calidad en la reducción de los reprocesos en los proyectos de construcción civil* [Monografía de especialización, Universidad de Cartagena].

**Archivo(s):** `04_Bibliografia/03_Tesis/Alvarez_Quintero_2014_Gestion_Calidad_Reduccion_Reprocesos_Construccion_UdeCartagena.pdf` (30 págs.)

**Verificación de portada y correcciones a la referencia propuesta:**

- Portada (págs. PDF 1–2): Universidad de Cartagena, Facultad de Ingeniería, Especialización en Gerencia de Proyectos de Construcción; «Monografía para obtener el título de Especialista en Gerencia de Proyectos de Construcción»; autor Luis Rodolfo Álvarez Quintero; director Ing. Jorge Luis Álvarez Carrascal; Cartagena de Indias, 2014.
- Autor, título, tipo y año coinciden con la referencia propuesta y con la entrada `alvarez2014` de `bib/00_base.bib`. Se añade la ubicación.
- Sin URL: no figura en el PDF ni en `Bibliografia_Recomendada.md`. Si se localiza en el repositorio de la Universidad de Cartagena, agregar el enlace; si no, APA 7 la trata como trabajo no publicado.
- Es una revisión de literatura: sus cifras son secundarias (Palaneeswaran, 2006; Hwang et al., 2009; Love y Edwards, 2005). Se citan como datos recopilados por Álvarez Quintero, sin atribuirlos a las fuentes originales, que no se leyeron.
- Paginación impresa: p. N = pág. PDF N.

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Álvarez Quintero (2014) |
| País | Colombia (Cartagena) |
| Institución | Universidad de Cartagena |
| Objetivo | Analizar críticamente el efecto de la gestión de la calidad en la reducción de los reprocesos en proyectos de construcción civil. |
| Diseño y muestra | Revisión de literatura con análisis crítico de estudios internacionales (2000–2014); sin trabajo de campo. |
| Resultados (cifras) | Reprocesos de hasta 12,4 % del costo (promedio 6,59 %, de 8 estudios); con SGC, 0,72 % (Australia) y en promedio 1 %; reducción estimada de 84,82 % (de 6,59 % a 1 %); Barclay Construction pasó de 5 % a menos de 1 % del contrato. |
| Relación con nuestra tesis | Introducción (magnitud del problema) y discusión: referencia de reducción esperable con un SGC frente a nuestro criterio de r ≥ 5 %. Dato secundario: usar con cautela. |

**Fichas (8):**

**alvarez2014-01** · p. 5 (pág. PDF 5) · *metodo* · Uso: Introducción-Antecedentes de investigación

> «Para cumplir este objetivo se hizo una revisión de la literatura y un análisis crítico de los resultados de los estudios realizados a nivel mundial en este campo de la ingeniería.»

Paráfrasis: Álvarez Quintero (2014) hizo una revisión de literatura con análisis crítico de estudios internacionales sobre el efecto de la gestión de la calidad en los reprocesos de los proyectos de construcción civil (p. 5).

**alvarez2014-02** · p. 5 (pág. PDF 5) · *dato* · Uso: Introducción-Situación problemática | Cap.1 sección 1.4.2 (no calidad y reprocesos)

> «Se evidenció que los costos por reprocesos ascendían hasta 12.4% de los costos de los proyectos y en promedio resultaba ser del 6.59%.»

Paráfrasis: Según la revisión de Álvarez Quintero (2014), los costos por reprocesos llegan hasta el 12,4 % del costo de los proyectos, con un promedio de 6,59 % (p. 5). Ese promedio es la media aritmética de ocho valores publicados entre 2000 y 2010 (p. 13).

**alvarez2014-03** · p. 5 (pág. PDF 5) · *hallazgo* · Uso: Introducción-Situación problemática | Cap.3 Discusión (3.7)

> «una efectiva implementación de un sistema de gestión de la calidad reduce los reprocesos hasta en un 84.82%, llegando en ocasiones al 0.72% y en promedio al 1% del total de costos del proyecto.»

Paráfrasis: La literatura revisada indica que la implementación efectiva de un SGC reduce los reprocesos hasta en 84,82 %, con valores de 0,72 % y, en promedio, de 1 % del costo total del proyecto (Álvarez Quintero, 2014, p. 5).

**alvarez2014-04** · p. 12 (pág. PDF 12) · *dato* · Uso: Cap.1 sección 1.4.2 | Cap.3 Discusión (3.7)

> «el promedio de costos por reprocesos en proyectos sin un sistema de gestión de la calidad era de un 6.5% del valor del contrato. Por el contrario, el promedio de los costos de reprocesos para proyectos con sistemas de gestión de la calidad era de 0.72%.»

Paráfrasis: Con datos del Industry Development Authority de Australia (2004), recopilados por Palaneeswaran (2006), Álvarez Quintero (2014) reporta que el costo promedio de los reprocesos fue de 6,5 % del valor del contrato en proyectos sin SGC y de 0,72 % en proyectos con SGC (p. 12).

**alvarez2014-05** · p. 20 (pág. PDF 20) · *dato* · Uso: Cap.3 Discusión (3.7)

> «se estimaba que los costos por reprocesos eran el 5% del valor del contrato. Cuando se implementó el sistema de aseguramiento de la calidad, los reprocesos estuvieron por debajo del 1% del valor del contrato en la mayoría de sus proyectos.»

Paráfrasis: Álvarez Quintero (2014), con base en Love y Edwards (2005), refiere que Barclay Construction Ltd. (Australia) estimaba sus reprocesos en 5 % del valor del contrato antes de implantar un sistema de aseguramiento de la calidad, y por debajo de 1 % en la mayoría de sus proyectos después de implantarlo (p. 20).

**alvarez2014-06** · p. 20 (pág. PDF 20) · *hallazgo* · Uso: Cap.3 Discusión (3.7) | Introducción-Justificación económica

> «se puede establecer que la implementación de un sistema de gestión de la calidad puede reducir el costo de los reprocesos hasta en un 84.82%, al pasar de 6,59% a 1% del total de los costos del proyecto.»

Paráfrasis: La reducción de 84,82 % es un cálculo del propio autor: pasar del promedio de 6,59 % al 1 % del costo total del proyecto al implementar un SGC (Álvarez Quintero, 2014, p. 20). Como el trabajo es una revisión bibliográfica, la cifra es una estimación a partir de promedios publicados y no una medición en obra.

**alvarez2014-07** · p. 22 (pág. PDF 22) · *metodo* · Uso: Cap.2 sección 2.6.1 (compras y recepción de materiales)

> «Reforzar las cadenas de proveedores, y que estos cuenten con los certificados de calidad de sus materiales.»

Paráfrasis: Entre las medidas para evitar reprocesos, Álvarez Quintero (2014), siguiendo a Palaneeswaran (2006), recomienda fortalecer la cadena de proveedores y exigirles certificados de calidad de sus materiales (p. 22).

**alvarez2014-08** · p. 19 (pág. PDF 19) · *hallazgo* · Uso: Cap.1 sección 1.4.2 | Cap.3 Discusión (3.7) (hormigón de la losa sin probetas)

> «Reconocer la existencia de reprocesos ocultos y evadir sus consecuencias, principalmente los errores que generan más errores, por ejemplo la fundición de una zapata con un concreto de menor resistencia a la compresión se podría detectar a los 7 días»

Paráfrasis: Álvarez Quintero (2014) advierte sobre los reprocesos ocultos. Una zapata vaciada con hormigón de menor resistencia solo se detecta a los 7 días, cuando ya pueden haberse adelantado trabajos posteriores. Por eso recomienda detectar y corregir antes de iniciar el trabajo siguiente (p. 19).

## 5. Cabrera Bellido y Vásquez Sangama (2021) — desperdicio de materiales en Iquitos (UCP, Perú)

**Referencia APA 7 (verificada):** Cabrera Bellido, J. A., & Vásquez Sangama, P. O. (2021). *Análisis de los desperdicios de materiales en obras de construcción civil en Iquitos metropolitano – Loreto: Métodos de control y medición* [Tesis de licenciatura, Universidad Científica del Perú]. http://hdl.handle.net/20.500.14503/1682

**Archivo(s):** `04_Bibliografia/03_Tesis/Cabrera_Vasquez_2021_Tesis_Desperdicios_Materiales_Iquitos_UCP.pdf` (143 págs.)

**Verificación de portada y correcciones a la referencia propuesta:**

- Portada (pág. PDF 1): Universidad Científica del Perú, Facultad de Ciencias e Ingeniería, Programa Académico de Ingeniería Civil; «Informe final de tesis»; «Requisito para optar el título profesional de Ingeniero Civil»; autores Bach. Jorge Ayrton Cabrera Bellido y Bach. Pául Odiseo Vásquez Sangama; asesor Ing. Ulises Octavio Irigoin Cabrera; Iquitos, Perú, 2021.
- Se completa el título, que en la referencia propuesta estaba truncado: «…en Iquitos metropolitano – Loreto: Métodos de control y medición».
- Inconsistencia documental (requiere verificación): varias cifras y frases de los resultados coinciden con Galarza Meza (2011): 4.796 frente a 3.918 m³ y 22 %; acero con 7 %, 4,04 % y 3,75 %; trabajo no productivo de 23 % a 12 %. Además, sus conclusiones dan para el acero 0,25 % y 0,10 %, mientras la sección 4.4 (pp. 115–117) da 7 %, 4,04 % y 3,75 %. Para esas cifras citar a Galarza Meza (2011).
- Paginación impresa: p. N = pág. PDF N + 15.

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Cabrera Bellido y Vásquez Sangama (2021) |
| País | Perú (Iquitos) |
| Institución | Universidad Científica del Perú |
| Objetivo | Analizar el desperdicio de materiales en obras de edificación de Iquitos y sus métodos de control y medición. |
| Diseño y muestra | Descriptivo correlacional; muestra por conveniencia de 2 edificaciones públicas (obras A y B, 2016–2017); observación con lista de cotejo, guías de observación y de análisis; chi cuadrado, Spearman y Kendall declarados. |
| Resultados (cifras) | Índice de residuos de 0,13 y 0,10 m³/m² techado; hormigón 3,6 % (verticales) y 1,6 % (horizontales) en la obra A; acero 0,25 % (A) y 0,10 % (B), frente a 5 % del expediente técnico; ahorro de ≈ S/ 7.000 en eliminación de desmonte (360 m³). Cifras con inconsistencias. |
| Relación con nuestra tesis | Marco teórico (pérdida relativa a una situación de referencia) y discusión. Usar con cautela por las coincidencias con Galarza Meza (2011). |

**Fichas (6):**

**cabrera2021-01** · p. 48 (pág. PDF 63) · *metodo* · Uso: Introducción-Antecedentes de investigación

> «La investigación es del tipo descriptiva correlacional. Es descriptiva, porque las variables se estudian tal y como se encontraron en la realidad durante la ejecución de dos edificaciones en la ciudad metropolitana de Iquitos.»

Paráfrasis: Cabrera Bellido y Vásquez Sangama (2021) hicieron una investigación descriptiva correlacional sobre dos edificaciones públicas de Iquitos, en la que las variables se estudiaron tal como se presentaron durante la ejecución (p. 48). Para medir la asociación entre variables declararon usar chi cuadrado y los coeficientes de Spearman y Kendall (p. 49).

**cabrera2021-02** · p. 49 (pág. PDF 64) · *metodo* · Uso: Introducción-Metodología de la investigación (muestra por conveniencia)

> «Obtenida a conveniencia de los investigadores, en razón a haber participado en los controles de calidad durante la ejecución de las edificaciones que se señalan a continuación»

Paráfrasis: La muestra se eligió por conveniencia, porque los autores participaron en el control de calidad de las dos obras: la Escuela Técnica Superior de la PNP en Iquitos y una institución educativa de Belén. La técnica fue la observación, y los instrumentos, una lista de cotejo, cuadros estadísticos y guías de observación y de análisis (Cabrera Bellido y Vásquez Sangama, 2021, pp. 49–50).

**cabrera2021-03** · p. 19 (pág. PDF 34) · *definicion* · Uso: Cap.1 sección 1.5.2 (índices de desperdicio y su medición)

> «Paliari (1999), sin embargo, sostiene que las pérdidas son un concepto relativo ya que se debe determinar en primer lugar una situación de referencia.»

Paráfrasis: Siguiendo a Paliari (1999), Cabrera Bellido y Vásquez Sangama (2021) presentan la pérdida como un concepto relativo: primero debe fijarse una situación de referencia, es decir, un consumo estimado o aceptable, y es desperdicio todo consumo que la supere (pp. 19–20).

**cabrera2021-04** · p. 91 (pág. PDF 106) · *dato* · Uso: Cap.1 sección 1.5.2 (medición por consumo de insumos) — preferir Galarza Meza (2011)

> «cumpliendo los diseños de mezcla en el total de la obra era suficiente para producir un volumen de 4,796 M3 cuando el metrado del presupuesto estimaba solamente 3,918M3 para las estructuras de concreto, de lo que se puede colegir que se generó un desperdicio del orden del 22%.»

Paráfrasis: Con guías de compra de cemento y vales de salida de almacén, los autores estimaron que el cemento consumido alcanzaba para 4.796 m³ de hormigón, frente a 3.918 m³ del metrado del presupuesto: un desperdicio del orden de 22 % (Cabrera Bellido y Vásquez Sangama, 2021, p. 91). [Nota de verificación: las tres cifras coinciden con las que Galarza Meza (2011) reporta para su obra A; verificar su origen y, de ser el caso, citar la fuente original.]

**cabrera2021-05** · p. 122 (pág. PDF 137) · *conclusion* · Uso: Cap.3 Discusión (3.7) (desperdicio de acero) — con cautela

> «En cuanto al acero de refuerzo para la obra A se alcanzó un porcentaje de desperdicios de 0.25% y para la B de 0.10%; en ambos casos el desperdicio previsto en el expediente técnico de 5% es muy superior al realmente perdido.»

Paráfrasis: Los autores concluyen que el desperdicio de acero de refuerzo fue de 0,25 % en la obra A y de 0,10 % en la obra B, muy por debajo del 5 % previsto en el expediente técnico (Cabrera Bellido y Vásquez Sangama, 2021, p. 122). [Nota de verificación: la sección 4.4 del mismo documento (pp. 115–117) da para la obra B 7 %, 4,04 % y 3,75 %, cifras que coinciden con Galarza Meza (2011); el dato no es consistente.]

**cabrera2021-06** · p. 121 (pág. PDF 136) · *conclusion* · Uso: Introducción-Antecedentes de investigación | Cap.3 Discusión (3.7)

> «El nivel de desperdicios de materiales de construcción en las dos obras estudiadas no superan los máximos permisibles y tampoco supera los porcentajes previstos en los expedientes técnicos de obras de edificación, pero si generan pérdidas en las empresas constructoras; y, además contribuyen al deterioro ambiental.»

Paráfrasis: Concluyen que el desperdicio de materiales de ambas obras no superó los máximos permisibles ni los porcentajes de los expedientes técnicos, aunque sí causó pérdidas a las constructoras y deterioro ambiental. El índice de residuos fue de 0,13 y 0,10 m³ de desmonte por m² techado (Cabrera Bellido y Vásquez Sangama, 2021, pp. 118 y 121).

## 6. Cajías Luna (2023) — control de calidad en la supervisión de obras municipales (UMSA, Bolivia)

**Referencia APA 7 (verificada):** Cajías Luna, E. C. (2023). *Control de calidad en la supervisión de obras municipales* [Memoria laboral de licenciatura, Universidad Mayor de San Andrés]. https://repositorio.umsa.bo/handle/123456789/34372

**Archivo(s):** `04_Bibliografia/03_Tesis/Cajias_2023_MemoriaLaboral_Control_Calidad_Supervision_Obras_Municipales_UMSA_Parte1.pdf` (170 págs.: preliminares y pp. 1–152) y `…_Parte2.pdf` (27 págs.: pp. 294–320)

**Verificación de portada y correcciones a la referencia propuesta:**

- Portada (Parte 1, pág. PDF 1): Universidad Mayor de San Andrés, Facultad de Ingeniería, Carrera de Ingeniería Civil; «Memoria laboral para obtener el título de licenciatura en Ingeniería Civil»; postulante Eynar Cesar Cajías Luna; asesor M.Sc. Ing. Alex Ramiro Calle Andrade; La Paz, Bolivia, 2023.
- Autor, título, tipo y año coinciden con la referencia propuesta.
- El documento está incompleto en el repositorio local: la Parte 1 termina en la p. 152 y la Parte 2 empieza en la p. 294 (bibliografía, área III y anexos con planos as built y fotografías). Faltan las pp. 153–293, entre ellas los ensayos de probetas y de flexotracción (pp. 199–203 según el índice).
- La memoria se elaboró en el marco del PETAENG de la Facultad de Ingeniería (p. iii). En la p. 16 la llama «Proyecto de Grado», pero la portada dice «Memoria laboral».
- Paginación impresa: Parte 1, p. N = pág. PDF N + 18; Parte 2, p. N = pág. PDF N + 293. Todas las fichas son de la Parte 1.

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Cajías Luna (2023) |
| País | Bolivia (El Alto, La Paz) |
| Institución | Universidad Mayor de San Andrés |
| Objetivo | Plantear un método de control de calidad de obras viales con pavimento rígido aplicado a la supervisión de una obra municipal (pavimentado de la Av. Las Kantutas, El Alto). |
| Diseño y muestra | Memoria laboral con método descriptivo: sistematiza la experiencia del autor como supervisor del GAM de El Alto (2006–2015) y describe documentos, flujos de control técnico y administrativo y plan de calidad de la obra. |
| Resultados (cifras) | Procedimientos de supervisión: certificados de calidad de materiales, ensayos confirmatorios por lote, presencia del supervisor en el muestreo y el ensayo, rechazo de resultados dudosos, límites de 5 % (orden de cambio) y 10 % (contrato modificatorio). Sin cifras de costos de calidad. |
| Relación con nuestra tesis | Marco normativo y procedimental boliviano de la supervisión (Cap. 1 y 2): sustenta la exigencia de muestreo presenciado y la crítica al certificado n.º 000293, con probetas elaboradas por el contratista. |

**Fichas (8):**

**cajias2023-01** · p. 16 (pág. PDF 34) · *metodo* · Uso: Introducción-Antecedentes de investigación

> «se aplicará un Método de Investigación Descriptivo; ya que, determinaremos los aspectos más representativos de la experiencia técnica obtenida como supervisor de obras»

Paráfrasis: La memoria laboral de Cajías Luna (2023) aplica un método descriptivo para sistematizar la experiencia del autor como supervisor de obras y proponer, a partir de una obra concreta, un método de control de calidad para obras viales con pavimento rígido (p. 16).

**cajias2023-02** · p. 14 (pág. PDF 32) · *definicion* · Uso: Cap.1 sección 1.10 (definición de términos) | Cap.2 sección 2.2 (roles de supervisión y fiscalización)

> «que tendrá como responsabilidad la correcta ejecución física del proyecto, certificar los volúmenes y calidad de todos los ítems ejecutados por la Entidad Ejecutora o Contratista y de aprobar o elaborar los certificados de pago»

Paráfrasis: Con base en la Guía de Supervisión de Obras del Ministerio de Obras Públicas (2016), Cajías Luna (2023) define al supervisor de obras como la empresa o el profesional contratado para velar por la correcta ejecución física del proyecto, certificar los volúmenes y la calidad de todos los ítems ejecutados por el contratista y aprobar o elaborar los certificados de pago (p. 14).

**cajias2023-03** · p. 36 (pág. PDF 54) · *definicion* · Uso: Cap.1 sección 1.10 | Cap.2 sección 2.6.1 (recepción de materiales con certificado)

> «Documento que certifica la calidad de los materiales ensayados en laboratorio o recibidos del fabricante en el caso de los manufacturados, emitidos por organismos nacionales oficiales de control de calidad»

Paráfrasis: Los certificados de calidad de materiales acreditan la calidad de los materiales ensayados en laboratorio o, si son manufacturados, la de los recibidos del fabricante. Los emiten organismos oficiales de control de calidad y sus resultados deben estar dentro de las tolerancias de las normas (ISO, IBNORCA, NB) y de las especificaciones técnicas (Cajías Luna, 2023, p. 36).

**cajias2023-04** · p. 36 (pág. PDF 54) · *metodo* · Uso: Cap.2 sección 2.6.1 (ensayos confirmatorios por lote) | Cap.3 Discusión (3.7)

> «Esta disposición no impide que durante la construcción y para cada lote de materiales o partes entregadas en obra, se realicen pruebas y ensayos confirmatorios, con la única finalidad de garantizar la calidad en la ejecución de la obra»

Paráfrasis: Contar con certificados de calidad no impide hacer pruebas y ensayos confirmatorios en cada lote de materiales entregado en obra para garantizar la calidad de la ejecución (Cajías Luna, 2023, p. 36).

**cajias2023-05** · p. 36 (pág. PDF 54) · *metodo* · Uso: Cap.3 sección 3.3 (evaluación del certificado de laboratorio) | Cap.3 Discusión (3.7)

> «El Supervisor de Obra se reserva el derecho de rechazar resultados o certificaciones que considere de dudosa procedencia, dispersos (varianzas extremas), adulterados o irrelevantes en el proceso de verificación de la calidad de las obras y materiales»

Paráfrasis: Con base en el manual de supervisión y fiscalización del Gobierno Municipal de El Alto (2006), Cajías Luna (2023) señala que el supervisor puede rechazar resultados o certificaciones de dudosa procedencia, con dispersión extrema, adulterados o irrelevantes para verificar la calidad de obras y materiales (p. 36).

**cajias2023-06** · p. 37 (pág. PDF 55) · *metodo* · Uso: Cap.2 sección 2.6.1 (procedimiento de muestreo de hormigón) | Cap.3 Discusión (3.7)

> «El Supervisor de Obras deberá estar siempre presente el momento de la “toma de muestras” y el momento de “ensayo de las mismas”, con el objeto de certificar resultados.»

Paráfrasis: El supervisor debe presenciar la toma de muestras y su ensayo para certificar los resultados, y registrar ambos hechos en el Libro de Órdenes. Las muestras van a un laboratorio aprobado, que emite certificados firmados; el supervisor los verifica y aprueba o rechaza lo ejecutado (Cajías Luna, 2023, p. 37).

**cajias2023-07** · p. 40 (pág. PDF 58) · *requisito_normativo* · Uso: Cap.2 sección 2.2 (datos contractuales) — para el requisito citar el D.S. 0181

> «El incremento o decremento del monto del contrato, mediante Contrato Modificatorio (una o varios) tiene como límite máximo del diez por ciento (10%) del monto original del contrato.»

Paráfrasis: Con base en Barrón (2014), Cajías Luna (2023) indica que los contratos modificatorios pueden aumentar o disminuir el monto contractual hasta un 10 % del monto original, y que las órdenes de cambio tienen un límite de 5 % del monto total (pp. 38 y 40). Es una fuente secundaria: el requisito debe citarse del D.S. 0181 (NB-SABS).

**cajias2023-08** · p. 60 (pág. PDF 78) · *definicion* · Uso: Cap.1 sección 1.2.1 (aseguramiento de la calidad) | Cap.2 sección 2.6.1

> «ASEGURAR LA CALIDAD DEL PRODUCTO: Este tipo de control es de carácter preventivo, se aplica estableciendo procedimientos preventivos sencillos que puedan proporcionar anticipadamente la certeza de que los materiales utilizados son los indicados y cumplen con las normas de calidad del fabricante»

Paráfrasis: En el control técnico, asegurar la calidad del producto es un control preventivo. Consiste en establecer procedimientos sencillos que den, con anticipación, la certeza de que los materiales empleados son los indicados y cumplen las normas de calidad del fabricante (Cajías Luna, 2023, p. 60).

## 7. Calizaya Paco (2022) — predicción de la demanda de acero e inventarios (UMSA, Bolivia)

**Referencia APA 7 (verificada):** Calizaya Paco, J. (2022). *Modelo de predicción de la demanda de los principales ítems de acero para la construcción de obras civiles como medio para optimizar la reposición de inventarios* [Tesis de maestría, Universidad Mayor de San Andrés]. https://repositorio.umsa.bo/handle/123456789/41575

**Archivo(s):** `04_Bibliografia/03_Tesis/Callizaya_2022_TesisMaestria_Prediccion_Demanda_Acero_Inventarios_UMSA.pdf` (91 págs.)

**Verificación de portada y correcciones a la referencia propuesta:**

- Portada (pág. PDF 1): Universidad Mayor de San Andrés, Facultad de Ciencias Económicas y Financieras, Carrera de Administración de Empresas, Instituto de Investigación y Capacitación en Ciencias Administrativas (IICCA); «Tesis — Maestría en Administración de Negocios, versión VII, paralelo B»; maestrante Lic. Jesús Calizaya Paco; tutor M.Sc. Omar Javier Trujillo Infantes; La Paz, Bolivia, 2021.
- Corrección del apellido: la portada dice **Calizaya** (con una sola «l»), no «Callizaya». Se mantiene la clave `callizaya2022` que pidió el coordinador; el autor va en la entrada como figura en la portada. Si el repositorio dice «Callizaya», documentar la variante.
- Año: la portada dice 2021 y el PDF se generó el 06/04/2022. Se conserva 2022 (repositorio), por confirmar.
- Se completa el título, que en la referencia propuesta estaba truncado. La portada escribe «ITEMS»; en minúsculas, «ítems».
- Paginación impresa: p. N = pág. PDF N + 7.

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Calizaya Paco (2022) |
| País | Bolivia (La Paz) |
| Institución | Universidad Mayor de San Andrés (Maestría en Administración de Negocios) |
| Objetivo | Diseñar un modelo de predicción de la demanda de los principales productos de acero para obras civiles en Importadora Colinas S.R.L. |
| Diseño y muestra | Aplicado, descriptivo, no experimental, longitudinal (2017–2019); censo no probabilístico de 9 directivos y 3 gestiones de ventas; encuesta con preguntas cerradas y análisis documental. |
| Resultados (cifras) | Quiebres de stock en 2019: 6.449 t de fierro corrugado sin atender (10,96 % de la demanda) y 8.653 t en total (USD 8.106.016); hipótesis aceptada con «porcentaje de aceptabilidad» de 5/5; proyección 2021 de 47.500 t de fierro corrugado con «probabilidad de 94 %» sin método explícito. |
| Relación con nuestra tesis | Contexto del abastecimiento de acero en Bolivia (situación problemática: escasez y retrasos de fierro) y contraejemplo metodológico de contraste de hipótesis sin inferencia estadística. |

**Fichas (7):**

**callizaya2022-01** · p. 4 (pág. PDF 11) · *dato* · Uso: Introducción-Situación problemática (abastecimiento de acero)

> «La empresa está vulnerable a quiebres de stock frecuentes, con mucha probabilidad de alcanzar a todas las familias que ocupan el mayor porcentaje en ventas, lo que repercutirá en los ingresos y en la reputación de la empresa.»

Paráfrasis: En Importadora Colinas S.R.L., los quiebres de stock de 2019 dejaron sin atender 6.449 t de fierro corrugado (10,96 % de una demanda de 58.843 t) y 8.653 t en total, equivalentes a USD 8.106.016 en ventas no realizadas (Calizaya Paco, 2022, p. 4, tabla 1).

**callizaya2022-02** · p. 21 (pág. PDF 28) · *metodo* · Uso: Introducción-Metodología de la investigación (diseño longitudinal documental)

> «Por la ubicación de los hechos en el tiempo, el presente estudio es longitudinal, se estudia un periodo entre las gestiones 2017, 2018 y 2019. Se ha realizado un análisis documental de las ventas consolidadas de las tres gestiones.»

Paráfrasis: El estudio fue aplicado, descriptivo, no experimental y longitudinal: analizó documentalmente las ventas consolidadas de 2017, 2018 y 2019 (Calizaya Paco, 2022, p. 21).

**callizaya2022-03** · p. 22 (pág. PDF 29) · *metodo* · Uso: Introducción-Metodología de la investigación (población censal)

> «La población del estudio está conformada por cuatro Gerentes Regionales, cuatro Jefes de Agencia Departamentales, el gerente de operaciones, y tres gestiones de ventas a nivel nacional.»

Paráfrasis: La población, trabajada como censo no probabilístico, comprendió cuatro gerentes regionales, cuatro jefes de agencia departamentales, el gerente de operaciones y tres gestiones de ventas. Se aplicaron encuestas con preguntas cerradas y análisis documental (Calizaya Paco, 2022, pp. 22–25).

**callizaya2022-04** · p. 52 (pág. PDF 59) · *metodo* · Uso: Cap.3 sección 3.5 (contraste de hipótesis; contraejemplo)

> «De las cinco dimensiones de aceptabilidad de la hipótesis, todos son relevantes y tienen incidencia en las ventas totales de cada gestión.»

Paráfrasis: La hipótesis se aceptó con un «porcentaje de aceptabilidad» de cinco indicadores aceptados sobre cinco (100 %), sin una prueba estadística inferencial (Calizaya Paco, 2022, p. 52).

**callizaya2022-05** · p. 54 (pág. PDF 61) · *hallazgo* · Uso: Cap.2 sección 2.5.3 (no conformidades en recepción) | Cap.3 Discusión (3.7)

> «No existe un seguimiento minucioso a los volúmenes que son recepcionados tanto en Santa Cruz como en La Paz, siendo estos los centros de distribución a nivel nacional.»

Paráfrasis: El estudio de campo encontró que no hay un seguimiento minucioso de los volúmenes recibidos en los centros de distribución de Santa Cruz y La Paz, y que el sistema informático no registra las ventas perdidas por falta de stock (Calizaya Paco, 2022, p. 54).

**callizaya2022-06** · p. 66 (pág. PDF 73) · *conclusion* · Uso: Cap.2 sección 2.6.1 (registro diario de materiales)

> «los quiebres de stock deben ser registrados de forma diaria y ser consolidados para luego ser tomados en cuenta en los pedidos al gerente de operaciones.»

Paráfrasis: Calizaya Paco (2022) concluye que los quiebres de stock deben registrarse a diario y consolidarse para tenerlos en cuenta en los pedidos, porque las ventas pasadas no bastan para definir la demanda (p. 66).

**callizaya2022-07** · p. 67 (pág. PDF 74) · *dato* · Uso: Cap.3 Discusión (3.7) (simulación y probabilidad; contraejemplo)

> «El volumen proyectado tiene una probabilidad de ocurrencia del 94 %.»

Paráfrasis: Para 2021 el modelo proyectó, entre otras familias, ventas de 47.500 t de fierro corrugado, con «una probabilidad de ocurrencia del 94 %» (Calizaya Paco, 2022, p. 67). El documento no explica cómo se calculó esa probabilidad, y su «simulación» suma a las ventas históricas los volúmenes de quiebre de stock.

## 8. Capcha Canaza (2016) — certificación de viguetas con la NB 997 y SGC en PREVITEC (UMSA, Bolivia)

**Referencia APA 7 (verificada):** Capcha Canaza, J. (2016). *Diseño e implementación para la certificación del producto viguetas prefabricadas con sello IBNORCA de conformidad con la NB 997 y un sistema de gestión de la calidad «Empresa PREVITEC S.R.L.»* [Proyecto de grado de licenciatura, Universidad Mayor de San Andrés]. https://repositorio.umsa.bo/handle/123456789/21835

**Archivo(s):** `04_Bibliografia/03_Tesis/Capcha_2016_PG_Certificacion_Viguetas_NB997_SGC_Previtec_UMSA.pdf` (341 págs.)

**Verificación de portada y correcciones a la referencia propuesta:**

- Portada (págs. PDF 1–2): Universidad Mayor de San Andrés, Facultad de Ingeniería, Carrera de Ingeniería Industrial; «Proyecto de grado presentado para la obtención del grado de licenciatura» en Ingeniería Industrial; autor José Capcha Canaza; tutora Ing. Gabriela Torrico Pérez; La Paz, Bolivia, 2016.
- Título, tipo, autor y año coinciden con la referencia propuesta y con `capcha2016` de `bib/00_base.bib`. Precisión: la carrera es Ingeniería Industrial, no Civil.
- Los requisitos de la NB 997 que transcribe provienen de la edición que cita en su bibliografía (IBNORCA, diciembre de 2005). Contrastarlos con la NB 997:2016 vigente antes de usarlos como criterio de aceptación.
- Paginación impresa («Página N»): p. N = pág. PDF N + 19.

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Capcha Canaza (2016) |
| País | Bolivia (La Paz/El Alto) |
| Institución | Universidad Mayor de San Andrés (Ingeniería Industrial) |
| Objetivo | Diseñar e implementar la certificación de viguetas pretensadas con sello IBNORCA (NB 997) y un SGC en PREVITEC S.R.L. |
| Diseño y muestra | Proyecto de grado aplicado: diagnóstico con listas de verificación (NB 997 y anexo 2 del reglamento del sello, NB ISO 9001:2008), diseño documental del SGC, plan de calidad, ensayos e inspección por lotes, y costos de calidad con y sin proyecto (CAE). |
| Resultados (cifras) | Incumplimiento de 88 % de la NB 997; reglamento del sello: 64 % de incumplimiento, 19 % parcial y 17 % de cumplimiento; costos de calidad sin proyecto Bs 292.851 (2016), con 31 % por fallas externas; con proyecto Bs 540.431 el primer año y luego Bs 161.323–193.550 al año; CAE menor con el proyecto. |
| Relación con nuestra tesis | Criterios de recepción de viguetas (defectos, tolerancias, aceptación por lote) para el PPI del Cap. 2 y antecedente de costos PEF con y sin SGC en un fabricante boliviano. |

**Fichas (8):**

**capcha2016-01** · p. 132 (pág. PDF 151) · *dato* · Uso: Introducción-Antecedentes de investigación | Cap.1 sección 1.7.3 (norma de viguetas)

> «Se realizó el diagnóstico de conformidad con la NB 997, teniendo un grado de incumplimiento del 88%»

Paráfrasis: El diagnóstico de conformidad de las viguetas de PREVITEC S.R.L. con la NB 997 dio un grado de incumplimiento de 88 % (Capcha Canaza, 2016, p. 132).

**capcha2016-02** · p. 132 (pág. PDF 151) · *dato* · Uso: Introducción-Antecedentes de investigación | Cap.2 sección 2.5.1 (diagnóstico de brechas)

> «Se realizó el diagnóstico de conformidad con el reglamento del sello según anexo 2, teniendo un grado de incumplimiento del 64%, cumplimiento parcial 19% y con el 17% de cumplimiento.»

Paráfrasis: Frente al reglamento del sello IBNORCA (anexo 2, con requisitos de la NB ISO 9001:2008), la empresa presentó 64 % de incumplimiento, 19 % de cumplimiento parcial y 17 % de cumplimiento (Capcha Canaza, 2016, p. 132).

**capcha2016-03** · p. 128 (pág. PDF 147) · *dato* · Uso: Cap.1 sección 1.4.1 (modelo PEF) | Cap.3 Discusión (3.7) (costos)

> «Situación sin proyecto situación actual en la que refleja gastos ascendentes sobre 290.000 Bs. Por concepto de errores de fabricación, devoluciones por fisuras, cortes de las viguetas mantenimiento de máquinas y costos de ensayos en laboratorio.»

Paráfrasis: Sin el proyecto, los costos de calidad y no calidad de PREVITEC superaban Bs 290.000 al año por errores de fabricación, devoluciones por fisuras, cortes de viguetas, mantenimiento de máquinas y ensayos de laboratorio. En 2016 sumaron Bs 292.851, de los cuales Bs 91.000 eran fallas externas (Capcha Canaza, 2016, p. 128, tabla 6-2).

**capcha2016-04** · p. 128 (pág. PDF 147) · *dato* · Uso: Cap.3 Discusión (3.7) (inversión en prevención frente a fallas)

> «La situación con proyecto “situación ideal” refleja que se requiere una inversión de 540.431Bs esto el primer año debido a los montos de inversión en compra de equipos y construcción del laboratorio»

Paráfrasis: Con el proyecto, el primer año exigía Bs 540.431, que incluían Bs 396.997 de implementación y certificación, con equipos y laboratorio. Los años siguientes los costos de calidad bajaban a Bs 161.323–193.550 anuales (2017–2020), frente a Bs 295.290–391.294 sin el proyecto (Capcha Canaza, 2016, p. 128, tablas 6-2 y 6-3).

**capcha2016-05** · p. 129 (pág. PDF 148) · *hallazgo* · Uso: Cap.1 sección 1.4.1 | Cap.3 Discusión (3.7)

> «donde se muestra que la empresa aplica pocas actividades de prevención y tiene muchas fallas externas es por eso que se presentan perdidas en términos monetarios.»

Paráfrasis: Sin el proyecto, la empresa hacía pocas actividades de prevención y tenía muchas fallas externas, lo que le causaba pérdidas (Capcha Canaza, 2016, p. 129). Con el proyecto, la estructura de costos pasaba de 7 % de evaluación, 53 % de prevención, 9 % de fallas internas y 31 % de fallas externas a 21 %, 69 %, 6 % y 4 % (pp. 129–130), y el costo anual equivalente resultaba menor (p. 131).

**capcha2016-06** · p. 89 (pág. PDF 108) · *requisito_normativo* · Uso: Cap.1 sección 1.7.3 (NB 997) | Cap.2 sección 2.6.1 (PPI de recepción de viguetas)

> «Las viguetas pretensadas, no presentaran discontinuidades en el hormigonado que sean apreciables a simple vista, oquedades armaduras visibles por falta de recubrimiento, fisuras visibles, ni rebabas que afecten el uso.»

Paráfrasis: Según la NB 997, en la versión que recoge Capcha Canaza (2016), las viguetas pretensadas no deben tener discontinuidades de hormigonado visibles a simple vista, oquedades, armaduras expuestas por falta de recubrimiento, fisuras visibles ni rebabas que afecten su uso. Además, la resistencia característica del hormigón debe ser de al menos 350 kgf/cm² a los 28 días (p. 89).

**capcha2016-07** · p. 89 (pág. PDF 108) · *requisito_normativo* · Uso: Cap.2 sección 2.6.1 (tolerancias en recepción) — contrastar con la NB 997:2016

> «Las discrepancias admisibles en las medidas de la vigueta respecto a los valores nominales serán los siguientes.»

Paráfrasis: Las tolerancias dimensionales de las viguetas respecto de los valores nominales son de +5 mm/−2 mm en las medidas transversales y de +30 mm/−20 mm en las longitudinales, y la flecha lateral y la contraflecha no deben superar L/300 (Capcha Canaza, 2016, pp. 89–90). [Nota de verificación: Capcha cita la NB 997 de 2005; contrastar con la NB 997:2016.]

**capcha2016-08** · p. 92 (pág. PDF 111) · *requisito_normativo* · Uso: Cap.2 sección 2.6.1 (criterio de aceptación o rechazo por lote)

> «si la suma de defectos principales o secundarios sobrepasa los límites específicos, se dará por finalizada la inspección rechazándose el lote correspondiente.»

Paráfrasis: La inspección por lotes clasifica los defectos en principales (oquedad que deja ver armadura, armadura visible, fisuras de más de 0,1 mm, flecha lateral excesiva) y secundarios. El registro admite hasta 2 defectos principales y 4 secundarios; si se superan, se rechaza el lote (Capcha Canaza, 2016, pp. 90–92).

## 9. Castañeda Briceño (2017) — viguetas pretensadas y productividad (UCV, Perú)

**Referencia APA 7 (verificada):** Castañeda Briceño, C. A. (2017). *Uso de viguetas pretensadas para el incremento de la productividad en la obra Escuela PNP-Puente Piedra-Lima-2017* [Tesis de licenciatura, Universidad César Vallejo]. https://hdl.handle.net/20.500.12692/23107

**Archivo(s):** `04_Bibliografia/03_Tesis/Castaneda_2017_Tesis_Viguetas_Pretensadas_Productividad_UCV.pdf` (75 págs.)

**Verificación de portada y correcciones a la referencia propuesta:**

- Portada (pág. PDF 1): Facultad de Ingeniería, Escuela Profesional de Ingeniería Civil; «Tesis para obtener el título profesional de Ingeniero Civil»; autor Bach. Carlos Anderson Castañeda Briceño; asesor Mg. Félix Delgado Ramírez; Lima, Perú, 2017. El nombre de la universidad está en el logotipo; la declaratoria (pág. PDF 5) confirma «Universidad César Vallejo, Sede Lima/filial Lima norte».
- Se completa el título, que en la referencia propuesta estaba truncado: «…en la obra Escuela PNP-Puente Piedra-Lima-2017».
- Inconsistencia interna: el texto afirma que la losa con viguetas es «14 % más liviana» (pp. 49 y 64), pero su tabla 9 da 287 frente a 300 kg/m², una diferencia de ≈ 4,3 % (cálculo propio). La «población» declarada es el propio investigador (p. 37).
- Paginación impresa: preliminares en romanos; desde la p. 32, p. N = pág. PDF N.

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Castañeda Briceño (2017) |
| País | Perú (Lima) |
| Institución | Universidad César Vallejo |
| Objetivo | Determinar si el uso de viguetas pretensadas en losas aligeradas incrementa la productividad en la obra Escuela PNP de Puente Piedra. |
| Diseño y muestra | Aplicada, no experimental, transversal, descriptiva comparativa; observación participante con fichas de recopilación de datos validadas por 3 expertos («aplicable», sin coeficiente); una losa de 271,05 m² comparada con el sistema convencional mediante presupuestos. |
| Resultados (cifras) | Costo 27 % menor (S/ 60.476,97 frente a S/ 82.763,19 para 271,05 m²); tiempo 40 % menor (3 frente a 5 días); peso «14 % menor» según el texto, aunque la tabla da 287 frente a 300 kg/m² (≈ 4,3 %). |
| Relación con nuestra tesis | Antecedente sobre el sistema de viguetas pretensadas (costo, plazo y peso) y ejemplo de validación por expertos sin coeficiente, frente a la V de Aiken prevista en nuestra tesis. |

**Fichas (7):**

**castaneda2017-01** · p. xii (pág. PDF 12) · *metodo* · Uso: Introducción-Antecedentes de investigación | Introducción-Metodología de la investigación

> «La investigación fue de tipo aplicada, de diseño no experimental, transversal de nivel descriptivo comparativo. Para la recolección de datos se utilizó la técnica de la observación, cuyo instrumento fue la ficha de recopilación de datos para la variable viguetas pretensadas y productividad.»

Paráfrasis: Castañeda Briceño (2017) hizo una investigación aplicada, no experimental, transversal y descriptiva comparativa. Usó la observación como técnica y fichas de recopilación de datos para las variables viguetas pretensadas y productividad, con procesamiento en tablas porcentuales (p. xii). Declaró como población al propio investigador y una muestra no probabilística (p. 37).

**castaneda2017-02** · p. 40 (pág. PDF 40) · *metodo* · Uso: Cap.2 sección 2.7 (validación) | Cap.3 sección 3.6 (V de Aiken)

> «La validez del instrumento se obtuvo bajo el criterio de juicio de experto. En base a los siguientes criterios:»

Paráfrasis: La validez del instrumento se obtuvo por juicio de tres expertos según pertinencia, relevancia, claridad y suficiencia. Todos lo declararon «aplicable», pero no se informa un coeficiente de validez (Castañeda Briceño, 2017, p. 40).

**castaneda2017-03** · p. 48 (pág. PDF 48) · *dato* · Uso: Introducción-Antecedentes de investigación | Cap.3 Discusión (3.7)

> «Se demostró que en el presupuesto de la losa construida con el sistema de viguetas pretensadas es 27% menor al costo del sistema de losa convencional.»

Paráfrasis: El presupuesto de la losa con viguetas pretensadas y bovedillas resultó 27 % menor que el de la losa aligerada convencional: S/ 60.476,97 frente a S/ 82.763,19 para 271,05 m² (Castañeda Briceño, 2017, pp. 48 y 54).

**castaneda2017-04** · p. 49 (pág. PDF 49) · *dato* · Uso: Cap.3 Discusión (3.7) — con la corrección indicada

> «Se tuvo como resultado que la construcción de una losa aligerada con el sistema de viguetas pretensadas y bovedilla es 14% más liviana que la losa construida convencionalmente.»

Paráfrasis: El autor afirma que la losa con viguetas pretensadas es 14 % más liviana que la convencional (Castañeda Briceño, 2017, p. 49). Sin embargo, su tabla 9 consigna 287 frente a 300 kg/m² (77,74 frente a 81,31 t), una diferencia de aproximadamente 4,3 % (cálculo propio).

**castaneda2017-05** · p. 49 (pág. PDF 49) · *dato* · Uso: Cap.1 sección 1.6.2 (proceso constructivo) | Cap.3 Discusión (3.7)

> «Se demostró que la construcción de una losa aligerada con el sistema de viguetas pretensadas y bovedilla ahorras un 40% del tiempo normal que se demora construyendo una losa con el sistema convencional.»

Paráfrasis: Construir la losa de 271,05 m² con viguetas pretensadas tomó 3 días, frente a 5 días con el sistema convencional: un ahorro de 40 % del tiempo (Castañeda Briceño, 2017, p. 49).

**castaneda2017-06** · p. 43 (pág. PDF 43) · *dato* · Uso: Cap.1 sección 1.6.1 (descripción del sistema: viguetas)

> «lo de alta resistencia refiere a su carga de rotura de 18000 Kg/cm2 que es 4.5 veces mayor a los 4200Kg/cm2 que tienen los aceros que se usan en las estructuras convencionales.»

Paráfrasis: Las viguetas usan acero de pretensado de alta resistencia y baja relajación, con carga de rotura de 18.000 kg/cm², unas 4,5 veces la del acero convencional de 4.200 kg/cm². Su hormigón tiene de 350 a 480 kg/cm² según el tipo de vigueta (Castañeda Briceño, 2017, p. 43).

**castaneda2017-07** · p. 54 (pág. PDF 54) · *dato* · Uso: Cap.3 Discusión (3.7) (costos directos de sistemas de losa)

> «Teniendo un cuadro comparativo de presupuesto entre la construcción de la losa aligerada en un área total de 271.05 m2,entre el sistema de viguetas pretensadas y bovedilla de concreto y el sistema de construcción de losa aligerada convencional.»

Paráfrasis: El cuadro comparativo de presupuestos para 271,05 m² da un costo directo de S/ 43.433,62 con viguetas pretensadas y bovedillas de concreto, y de S/ 59.439,23 con el sistema convencional, que incluye 271,05 m² de encofrado y 2.260 ladrillos de techo (Castañeda Briceño, 2017, p. 54).

## 10. Ccoyllo Sifuentes (2016) — productividad y reducción de desperdicios en edificaciones (UCV, Perú)

**Referencia APA 7 (verificada):** Ccoyllo Sifuentes, M. A. (2016). *Mejoramiento de la productividad para una reducción de los desperdicios de materiales de un proyecto de edificaciones en San Borja en el 2016* [Tesis de licenciatura, Universidad César Vallejo]. https://hdl.handle.net/20.500.12692/21410

**Archivo(s):** `04_Bibliografia/03_Tesis/Ccoyllo_2016_Tesis_Productividad_Reduccion_Desperdicios_Edificacion_UCV.pdf` (106 págs.)

**Verificación de portada y correcciones a la referencia propuesta:**

- Portada (págs. PDF 1–2): Facultad de Ingeniería, Escuela Profesional de Ingeniería Civil de la Universidad César Vallejo; «Tesis para obtener el título profesional de Ingeniero Civil»; autor Miguel Aurelio Ccoyllo Sifuentes; asesor Mgs. Rodolfo Marquina Callacna; Lima, Perú, 2016-II.
- Se completa el título, que en la referencia propuesta estaba truncado: «…de un proyecto de edificaciones en San Borja en el 2016».
- Inconsistencia interna: el resumen (p. vii) dice que la productividad aumentó «en un promedio del 10 %», pero las conclusiones (p. 76) dan 8,2 % (asentado de ladrillo) y 7,3 % (tarrajeo).
- Paginación impresa: p. N = pág. PDF N + 13.

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Ccoyllo Sifuentes (2016) |
| País | Perú (Lima, San Borja) |
| Institución | Universidad César Vallejo |
| Objetivo | Mejorar la productividad de las partidas de mayor incidencia para reducir el desperdicio de materiales en un edificio de 5 niveles y 2 sótanos. |
| Diseño y muestra | Aplicada, explicativa, no experimental; muestreo intencional; observación con cartas balance y registro de desperdicios en dos etapas de la obra; validez «aceptable» por juicio de expertos, sin coeficiente. |
| Resultados (cifras) | Materiales = 55 % del costo directo; desperdicio final de ladrillo 4,03 % y de mezcla de tarrajeo 6,57 %; productividad +8,2 % (ladrillo) y +7,3 % (tarrajeo); falta de control de almacén en la recepción como causa de desperdicio. |
| Relación con nuestra tesis | Marco teórico del desperdicio (directo e indirecto; % aceptables de CAPECO) y causas ligadas a la recepción de materiales (Cap. 2: diagnóstico de causas). |

**Fichas (8):**

**ccoyllo2016-01** · p. vii (pág. PDF 7) · *hallazgo* · Uso: Introducción-Antecedentes de investigación — usar las cifras de la p. 76

> «aplicando mejoras en los procesos constructivo, sean tales mejoras tecnológicas o cambios en las actividades, aumentamos la productividad en un promedio del 10%, reduciendo los desperdicios considerablemente»

Paráfrasis: Ccoyllo Sifuentes (2016) informa que las mejoras tecnológicas y de procedimiento aumentaron la productividad en un promedio de 10 % y redujeron considerablemente los desperdicios (p. vii). En las conclusiones, sin embargo, los incrementos son de 8,2 % en el asentado de ladrillo y de 7,3 % en el tarrajeo (p. 76).

**ccoyllo2016-02** · p. 14 (pág. PDF 27) · *definicion* · Uso: Cap.1 sección 1.5.2 (índices de desperdicio)

> «toda actividad (proceso) tiene un porcentaje de residuo, pero estos porcentajes de residuo de materiales deben de estar dentro de un margen de aceptabilidad»

Paráfrasis: Todo proceso genera residuos, pero estos deben mantenerse dentro de un margen de aceptabilidad. Con base en CAPECO (2003), Ccoyllo Sifuentes (2016) da como aceptables 5 % para mezcla de concreto, 10 % para mortero, 5 % para ladrillo y de 3 % a 10 % para el acero de refuerzo, según el diámetro de Φ 3/8″ a Φ 1″ (p. 14).

**ccoyllo2016-03** · p. 15 (pág. PDF 28) · *definicion* · Uso: Cap.1 sección 1.5.1 (clasificación de las pérdidas)

> «El otro tipo de desperdicio presentado por estos autores es el indirecto, el cual se refiere a todo material que es colocado dentro de la obra sin que esté considerado en los planos o especificaciones técnicas del proyecto.»

Paráfrasis: Siguiendo a Skoyles y Skoyles (1987), Ccoyllo Sifuentes (2016) distingue la pérdida directa, el material que se elimina como desmonte, de la indirecta, que es todo material colocado en la obra sin estar previsto en los planos o en las especificaciones técnicas, como los espesores excesivos de tarrajeo (p. 15).

**ccoyllo2016-04** · p. 15 (pág. PDF 28) · *hallazgo* · Uso: Cap.1 sección 1.5.1 | Cap.3 Discusión (3.7) (sobreconsumo como falla de control de calidad)

> «Este tipo de desperdicio podría asociarse con un defectuoso control de calidad dentro del proyecto, ya que como se puede apreciar en todos los casos se refiere a utilizar material»

Paráfrasis: El desperdicio indirecto puede asociarse con un control de calidad deficiente: supone usar material adicional para ocultar fallas o sustituir sin necesidad el material especificado por otro de calidad superior (Ccoyllo Sifuentes, 2016, pp. 15–16).

**ccoyllo2016-05** · p. 26 (pág. PDF 39) · *metodo* · Uso: Cap.2 sección 2.7 (validación) | Cap.3 sección 3.6 (V de Aiken)

> «Se determinó la validez de la investigación mediante el uso de una evaluación de expertos, dando como resultado, una validez aceptable al encontrarse este dentro de rango correcto.»

Paráfrasis: La validez del instrumento se determinó por evaluación de expertos, con resultado «aceptable». La confiabilidad se obtuvo presentando la ficha a tres ingenieros, sin informar ningún coeficiente (Ccoyllo Sifuentes, 2016, p. 26).

**ccoyllo2016-06** · p. 30 (pág. PDF 43) · *dato* · Uso: Introducción-Justificación económica

> «Se aprecia claramente que los costos de los materiales de construcción en este proyecto llegan a representar un 55% del monto total de este, por ello es importante el tener un buen seguimiento sobre los materiales»

Paráfrasis: En el edificio estudiado, los materiales representaron el 55 % del costo directo. Por eso el autor justifica el seguimiento de los materiales con mayores índices de desperdicio (Ccoyllo Sifuentes, 2016, p. 30).

**ccoyllo2016-07** · p. 32 (pág. PDF 45) · *hallazgo* · Uso: Cap.2 sección 2.5.3 (no conformidades y análisis de causas)

> «Recepción de materiales: Existe una gran posibilidad de que la cantidad de los materiales entregados en obra no sean los solicitados, esto debido a que no existe un debido control del almacén»

Paráfrasis: Entre las causas de desperdicio observadas en la obra figura la recepción de materiales: es muy probable que las cantidades entregadas no sean las solicitadas, porque no existe un control de almacén adecuado (Ccoyllo Sifuentes, 2016, p. 32).

**ccoyllo2016-08** · p. 76 (pág. PDF 89) · *conclusion* · Uso: Cap.3 Discusión (3.7)

> «habiendo mejorado la productividad, existe un desperdicio de unidades de ladrillo de 4.03% y un 6.57% de mezcla de tarrajeo, de la cual el primer desperdicio está dentro de lo normal, pero el segundo porcentaje aún necesita mejorarse.»

Paráfrasis: Aun con la productividad mejorada, persistió un desperdicio de 4,03 % en unidades de ladrillo, considerado normal, y de 6,57 % en mezcla de tarrajeo, que todavía debía reducirse (Ccoyllo Sifuentes, 2016, p. 76).

## 11. Cepeda Godoy (2017) — plan de control de calidad para edificios de departamentos (U. de Cuenca, Ecuador)

**Referencia APA 7 (verificada):** Cepeda Godoy, H. M. (2017). *Análisis de gestión de calidad en los procesos de planificación y construcción de departamentos en edificios de la ciudad de Riobamba, creación de un plan de control de calidad* [Tesis de maestría, Universidad de Cuenca].

**Archivo(s):** `04_Bibliografia/03_Tesis/Cepeda_2017_TesisMaestria_Plan_Control_Calidad_Edificios_Riobamba_UCuenca.pdf` (148 págs.)

**Verificación de portada y correcciones a la referencia propuesta:**

- Portada (pág. PDF 1): Universidad de Cuenca, Facultad de Arquitectura y Urbanismo, Maestría en Construcciones (tercera cohorte); «Tesis previa a la obtención del título de Magíster en Construcciones»; autor Héctor Manuel Cepeda Godoy; directora Arq. Carla Marcela Hermida Palacios; Cuenca, Ecuador, 2017.
- Se completa el título, que en la referencia propuesta estaba truncado: «…de la ciudad de Riobamba, creación de un plan de control de calidad».
- Sin URL: el PDF no trae handle y `Bibliografia_Recomendada.md` lo marca «verificar handle». Pendiente de buscar en el repositorio institucional de la Universidad de Cuenca; no se inventa.
- Observaciones metodológicas (cálculo propio): con los parámetros declarados (N = 158, σ = 0,5, Z = 1,96, e = 0,06) la fórmula da n ≈ 99, no 15; n = 15 corresponde a e ≈ 0,24. En el contraste usa como «proporción muestral» P = n/N = 0,0949, que es la fracción de muestreo, por lo que el Z = −12,96 no es válido.
- Paginación impresa: p. N = pág. PDF N.

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Cepeda Godoy (2017) |
| País | Ecuador (Riobamba) |
| Institución | Universidad de Cuenca (Maestría en Construcciones) |
| Objetivo | Analizar la gestión de calidad en la planificación y construcción de edificios de departamentos de Riobamba y crear un plan de control de calidad. |
| Diseño y muestra | Encuestas (preguntas dicotómicas y de selección simple) a 15 planificadores y constructores, de una población de 158, y entrevistas a 10 autoridades de control; muestreo intencional; contraste con la distribución muestral de proporciones (α = 0,05). |
| Resultados (cifras) | 60 % de los encuestados (9 de 15) atribuye 90 % de incidencia a implantar un plan de gestión de calidad; Z = −12,96 y rechazo de H0 (procedimiento cuestionable); plan con control de recepción de materiales y ensayos en laboratorios independientes y acreditados. |
| Relación con nuestra tesis | Modelo de plan de control de calidad (recepción, ejecución y obra terminada) para el Cap. 2 y contraejemplo de cálculo muestral y de contraste para el Cap. 3. |

**Fichas (8):**

**cepeda2017-01** · p. 23 (pág. PDF 23) · *metodo* · Uso: Introducción-Antecedentes de investigación

> «En procesos de planificación y construcción de edificios de departamentos en la ciudad de Riobamaba, NO se cuenta con un sistema de gestión de calidad que permita realizar un control de calidad que responda a la realidad local.»

Paráfrasis: Cepeda Godoy (2017) planteó como hipótesis que la planificación y construcción de edificios de departamentos de Riobamba carece de un sistema de gestión de calidad que permita un control de calidad acorde con la realidad local (p. 23).

**cepeda2017-02** · p. 48 (pág. PDF 48) · *metodo* · Uso: Introducción-Antecedentes de investigación | Cap.2 sección 2.4 (población y muestra)

> «La muestra utilizada según calculo es de 15 planificadores y constructores que intervienen en el proceso de planificación y construcción de departamentos en edificios.»

Paráfrasis: De una población de 158 profesionales registrados (52 arquitectos y 106 ingenieros civiles), la muestra calculada fue de 15 planificadores y constructores, a los que se sumaron 10 autoridades de control para contrastar la información (Cepeda Godoy, 2017, p. 48).

**cepeda2017-03** · p. 49 (pág. PDF 49) · *metodo* · Uso: Cap.3 Discusión (3.7) (contraejemplo de cálculo muestral)

> «e = Límite admisible de error muestral que, por lo general cuando no se tiene su valor, se utiliza un valor que varía entre el 1% (0,01) y 9% (0,09), quedando a criterio del encuestador.»

Paráfrasis: Para el tamaño de muestra se usó la fórmula para poblaciones finitas con σ = 0,5, Z = 1,96 y un error admisible de 1 % a 9 % a criterio del investigador; con N = 158 y e = 0,06 el autor obtuvo n = 14,88 ≈ 15 (Cepeda Godoy, 2017, p. 49). Con esos mismos parámetros la fórmula da n ≈ 99, y n = 15 corresponde a un error cercano a 24 % (cálculo propio).

**cepeda2017-04** · p. 115 (pág. PDF 115) · *metodo* · Uso: Cap.3 sección 3.5 (contraste de hipótesis; contraejemplo)

> «Como el valor de la proporción Z calculada es de -12,96 ≤ -1,645 valor de la tabla, se rechaza la hipótesis nula y acepta la hipótesis alterna»

Paráfrasis: La hipótesis se contrastó con la distribución muestral de proporciones: con Z = −12,96 ≤ −1,645 se rechazó la hipótesis nula con 95 % de confianza (Cepeda Godoy, 2017, p. 115). Sin embargo, la «proporción muestral» fue P = n/N = 15/158 = 0,0949 (p. 114), que es la fracción de muestreo y no la proporción observada de respuestas, por lo que el contraste no es válido (observación propia).

**cepeda2017-05** · p. 85 (pág. PDF 85) · *metodo* · Uso: Cap.2 sección 2.6.1 (ensayos por laboratorio independiente) | Cap.3 sección 3.3

> «ensayos o pruebas de servicio que deben ser realizados por entidades o laboratorios de control de calidad de la edificación, debidamente homologados y acreditados, distintos e independientes del constructor de los materiales usados en el proyecto.»

Paráfrasis: En su plan de control de calidad, Cepeda Godoy (2017) dispone que los ensayos y pruebas de servicio los hagan laboratorios homologados y acreditados, distintos e independientes del constructor (p. 85).

**cepeda2017-06** · p. 83 (pág. PDF 83) · *metodo* · Uso: Cap.2 sección 2.6.1 (control de recepción en obra)

> «En esta sección del Plan de Control de Calidad se consigna a la consulta de las “Prescripciones sobre los materiales” es decir de los datos, parámetros técnicos y certificaciones de calidad, en donde se establecen las condiciones de suministro; recepción, control, conservación, almacenamiento y manipulación»

Paráfrasis: La sección de control de recepción en obra del plan reúne las prescripciones sobre los materiales (datos, parámetros técnicos y certificaciones de calidad) y fija las condiciones de suministro, recepción, control, conservación, almacenamiento y manipulación de todos ellos (Cepeda Godoy, 2017, p. 83).

**cepeda2017-07** · p. 116 (pág. PDF 116) · *conclusion* · Uso: Cap.3 Discusión (3.7) (certificación de materiales)

> «Los materiales que no cumplen normativas nacionales e internacionales, como los sellos de calidad INEN no se deberían comercializar, porque ponen en peligro la calidad de los edificios»

Paráfrasis: Cepeda Godoy (2017) concluye que los materiales que no cumplen las normas nacionales e internacionales, como los sellos de calidad INEN, no deberían comercializarse, porque ponen en riesgo la calidad de los edificios (p. 116).

**cepeda2017-08** · p. 117 (pág. PDF 117) · *conclusion* · Uso: Introducción-Situación problemática | Cap.3 Discusión (3.7)

> «Una de las causas más relevantes para el incumplimiento de las normas de control de calidad es, el desconocimiento de las mismas por parte de planificadores, constructores y autoridades de control.»

Paráfrasis: Una de las principales causas del incumplimiento de las normas de control de calidad es que planificadores, constructores y autoridades de control las desconocen (Cepeda Godoy, 2017, p. 117).

## 12. Chafloque Rodriguez (2024) — gestión de abastecimiento de materiales y calidad (UCV, Perú)

**Referencia APA 7 (verificada):** Chafloque Rodriguez, C. (2024). *Gestión de abastecimiento de materiales de construcción en la calidad de un proyecto de edificaciones, Santa 2023* [Tesis de maestría, Universidad César Vallejo]. https://hdl.handle.net/20.500.12692/140280

**Archivo(s):** `04_Bibliografia/03_Tesis/Chafloque_2024_TesisMaestria_Abastecimiento_Materiales_Calidad_Edificaciones_UCV.pdf` (98 págs.)

**Verificación de portada y correcciones a la referencia propuesta:**

- Portada (pág. PDF 1): Escuela de Posgrado, Programa Académico de Maestría en Ingeniería Civil con Mención en Dirección de Empresas de la Construcción; «Tesis para obtener el grado académico de Maestro en Ingeniería Civil con Mención en Dirección de Empresas de la Construcción»; autor Cristian Chafloque Rodriguez (ORCID 0009-0004-5496-964X); asesores Mg. Jorge Humberto Ninatanta Alva y Mg. Cristhian Renzho Elsayed Rodriguez Mendoza; Trujillo, Perú, 2024. La declaratoria (pág. PDF 4) confirma la Universidad César Vallejo, Trujillo.
- Corrección: la portada escribe **Rodriguez** sin tilde; la referencia propuesta decía «Rodríguez». Se sigue la portada.
- Inconsistencia interna: la conclusión 1 (p. 44) atribuye 46,25 % a una gestión de abastecimiento «regular», pero en la tabla 2 (p. 23) esa variable tiene 31,3 % en nivel regular; 46,3 % corresponde a la calidad del proyecto. La «influencia de 40,1 %» es un pseudo R² de Nagelkerke y no implica causalidad.
- Paginación impresa: preliminares en romanos; cuerpo, p. N = pág. PDF N + 10.

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Chafloque Rodriguez (2024) |
| País | Perú (provincia del Santa, Áncash) |
| Institución | Universidad César Vallejo (Escuela de Posgrado) |
| Objetivo | Determinar la influencia de la gestión de abastecimiento de materiales de construcción en la calidad de un proyecto de edificaciones. |
| Diseño y muestra | Aplicada, cuantitativa, no experimental transversal, correlacional causal; muestra no probabilística de 80 colaboradores de 8 proyectos; cuestionarios Likert; validación por 3 jueces (sin coeficiente); alfa de Cronbach de 0,944 y 0,804 (piloto de 15); Kolmogorov-Smirnov, rho de Spearman y pseudo R² de Nagelkerke. |
| Resultados (cifras) | ρ = 0,512 (p < 0,05); pseudo R² = 0,401; 42,5 % de los casos con abastecimiento y calidad óptimos; dimensión «asegurar el suministro» con influencia de 77,8 %. |
| Relación con nuestra tesis | Antecedente del vínculo entre el abastecimiento o control de materiales y la calidad, y referencia de validación y confiabilidad de instrumentos para el Cap. 2. |

**Fichas (7):**

**chafloque2024-01** · p. ix (pág. PDF 9) · *metodo* · Uso: Introducción-Antecedentes de investigación | Introducción-Metodología de la investigación

> «La Metodología de estudio fue de tipo aplicada, con un enfoque cuantitativo, no experimental de corte transversal, método fue hipotético deductivo y nivel correlacional causal. La muestra estuvo compuesta por 80 colaboradores de las diversas áreas de gestión de 8 proyectos de edificación.»

Paráfrasis: Chafloque Rodriguez (2024) hizo un estudio aplicado, cuantitativo, no experimental transversal, hipotético-deductivo y de nivel correlacional causal. Encuestó con cuestionarios a una muestra de 80 colaboradores de 8 proyectos de edificación de la provincia del Santa (p. ix), elegida sin muestreo probabilístico (p. 20).

**chafloque2024-02** · p. 21 (pág. PDF 31) · *metodo* · Uso: Cap.2 sección 2.7 (validación) | Cap.3 sección 3.6 (V de Aiken)

> «la validez del instrumento fue analizado por tres jueces expertos, quienes determinaron que el instrumento evaluado cumple la pertinencia, relevancia y claridad, declarándolo aplicable.»

Paráfrasis: La validez del instrumento se estableció por juicio de tres expertos, que lo declararon aplicable por su pertinencia, relevancia y claridad, sin informar un coeficiente de validez (Chafloque Rodriguez, 2024, p. 21).

**chafloque2024-03** · p. 21 (pág. PDF 31) · *metodo* · Uso: Cap.2 sección 2.7 (confiabilidad de instrumentos)

> «se aplicó a una prueba piloto de 15 colaboradores, para poder determinar el coeficiente de fiabilidad alfa de Cronbach para preguntas con opciones politómicas. Se determinó una confiabilidad de gestión de abastecimiento de 0,944; y la variable dependiente calidad de un proyecto de edificaciones tuvo una fiabilidad de 0,804»

Paráfrasis: La confiabilidad se estimó con alfa de Cronbach en una prueba piloto de 15 colaboradores: 0,944 para la gestión de abastecimiento y 0,804 para la calidad del proyecto (Chafloque Rodriguez, 2024, p. 21).

**chafloque2024-04** · p. 24 (pág. PDF 34) · *hallazgo* · Uso: Introducción-Antecedentes de investigación | Cap.3 Discusión (3.7)

> «se estableció un coeficiente de correlación de 0,512 y una sig. <0.05, por ello, se rechazó la hipótesis nula, existiendo una influencia significativa entre la gestión de abastecimiento de materiales de construcción en la calidad de un proyecto de edificaciones, Santa 2023.»

Paráfrasis: Como la prueba de Kolmogorov-Smirnov indicó que los datos no eran normales (p < 0,05), se aplicó la rho de Spearman: ρ = 0,512 con p < 0,05. Se rechazó la hipótesis nula y se aceptó una relación significativa entre la gestión de abastecimiento de materiales y la calidad del proyecto (Chafloque Rodriguez, 2024, pp. 23–24).

**chafloque2024-05** · p. 25 (pág. PDF 35) · *dato* · Uso: Cap.3 Discusión (3.7) — interpretar como asociación, no como causalidad

> «el valor del Pseudo R cuadrado de Nagelkerke fue de ,401, es decir, que la variable independiente gestión de abastecimiento influye en un 40,1% en la variable dependiente calidad de proyectos de edificaciones.»

Paráfrasis: El pseudo R² de Nagelkerke fue de 0,401, que el autor interpreta como una influencia de 40,1 % de la gestión de abastecimiento sobre la calidad de los proyectos de edificación (Chafloque Rodriguez, 2024, p. 25).

**chafloque2024-06** · p. 44 (pág. PDF 54) · *conclusion* · Uso: Cap.3 Discusión (3.7) (aseguramiento del suministro)

> «se determinó una influencia significativa del 77.8% entre el aseguramiento del suministro de materiales de construcción en la calidad de un proyecto de edificaciones, Santa 2023.»

Paráfrasis: De las dimensiones estudiadas, asegurar el suministro de materiales mostró la mayor influencia sobre la calidad del proyecto, con 77,8 % (Chafloque Rodriguez, 2024, p. 44). [Nota de verificación: la conclusión 1 de la misma página da porcentajes de niveles que no coinciden con la tabla 2 (p. 23).]

**chafloque2024-07** · p. 45 (pág. PDF 55) · *conclusion* · Uso: Conclusiones y recomendaciones | Cap.3 Discusión (3.7) (alza de precios de materiales)

> «planificar la adquisición de materiales de manera anticipada, para poder evitar así las variaciones en costos por materiales de construcción y aumentando la rentabilidad.»

Paráfrasis: El autor recomienda planificar con anticipación la compra de materiales para evitar las variaciones de sus costos y mejorar la rentabilidad (Chafloque Rodriguez, 2024, p. 45).

## 13. Chino Quispe y Zarate Chilqquetuma (2024) — despiece de acero y desperdicio (UNSAAC, Perú)

**Referencia APA 7 (verificada):** Chino Quispe, A., & Zarate Chilqquetuma, K. B. (2024). *Análisis comparativo del método de despiece de acero pre ejecución frente al acero dimensionado y uso convencional del acero corrugado en la construcción de edificaciones en la ciudad del Cusco 2023* [Tesis de licenciatura, Universidad Nacional de San Antonio Abad del Cusco]. https://hdl.handle.net/20.500.12918/9553

**Archivo(s):** `04_Bibliografia/03_Tesis/Chino_Zarate_2024_Tesis_Despiece_Acero_Reduccion_Desperdicio_UNSAAC.pdf` (264 págs.)

**Verificación de portada y correcciones a la referencia propuesta:**

- Portada (pág. PDF 1): Universidad Nacional de San Antonio Abad del Cusco, Facultad de Ingeniería Civil, Escuela Profesional de Ingeniería Civil; «Tesis para optar el título profesional de Ingeniero Civil»; autores Bach. Andrés Chino Quispe y Bach. Kenny Boris Zarate Chilqquetuma; asesor Mgt. Ing. Luis Gerardo Becerra Infantas; Cusco, Perú, 2024. El informe de similitud (pág. PDF 3) es del 29/09/2024.
- Autores, título, tipo y año coinciden con la referencia propuesta y con `chino2024` de `bib/00_base.bib`. Se añaden nombres completos y ubicación.
- Precisión metodológica: el 14,58 % y el 17,09 % son desperdicios medidos con el método convencional (cimentación al quinto nivel). El 8,94 % y el 6,71 % son proyecciones del despiece pre ejecución sobre esos mismos niveles. Lo medido con despiece en los niveles superiores fue 3,15 % y 3,19 %. El resumen llama al enfoque «cuantitativo de nivel experimental» (p. i) y la metodología lo llama «mixto» (p. 7).
- Paginación impresa: preliminares en romanos (resumen, pág. PDF 27 = p. i); cuerpo, p. N = pág. PDF N + 30.

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Chino Quispe y Zarate Chilqquetuma (2024) |
| País | Perú (Cusco) |
| Institución | Universidad Nacional de San Antonio Abad del Cusco |
| Objetivo | Reducir el desperdicio de acero de refuerzo (material y mano de obra) con el despiece pre ejecución, comparado con el acero dimensionado y el uso convencional. |
| Diseño y muestra | Aplicada, cuantitativa (o «mixta»), de nivel experimental en 2 edificios multifamiliares de más de 8 pisos; registro de ingresos de acero, metrado diario, horas-hombre y cotizaciones; desperdicio medido como exceso sobre el metrado teórico. |
| Resultados (cifras) | Desperdicio convencional de 14,58 % (7.312,57 kg) y 17,09 % (17.808,75 kg); con despiece, 3,15 % y 3,19 % medidos, y 8,94 % y 6,71 % proyectados; productividad de habilitado de 0,014 a 0,021 hh/kg; utilidad +1,48 % y +5,87 %. |
| Relación con nuestra tesis | Método de medición del desperdicio (consumo real frente a metrado) para el Cap. 2 y referencia de desperdicio de acero; precedente de proyección ex ante, análogo a nuestra simulación de la segunda y tercera losa. |

**Fichas (8):**

**chino2024-01** · p. i (pág. PDF 27) · *metodo* · Uso: Introducción-Antecedentes de investigación

> «La metodología empleada en la investigación tiene un enfoque cuantitativo de nivel experimental, la técnica de recolección de datos se apoya en formatos como metrado de avance diario, ingreso de acero a obra, cantidad de horas hombre diario por actividad y cotizaciones de acero de refuerzo.»

Paráfrasis: Chino Quispe y Zarate Chilqquetuma (2024) aplicaron un enfoque cuantitativo de nivel experimental en dos edificios multifamiliares de más de ocho pisos en Cusco. Usaron formatos de metrado de avance diario, ingreso de acero a obra, horas-hombre por actividad y cotizaciones de acero (p. i). En el capítulo metodológico, en cambio, describen un enfoque mixto (p. 7).

**chino2024-02** · p. 7 (pág. PDF 37) · *metodo* · Uso: Cap.1 sección 1.5.2 (medición del desperdicio) | Cap.2 sección 2.5.4 (cuantificación del desperdicio)

> «La toma de datos incluye la cantidad de acero de refuerzo empleado, el porcentaje de acero en exceso del metrado teórico, así también los metrados ejecutados por cuadrilla para el cálculo del rendimiento real de la mano de obra.»

Paráfrasis: La toma de datos registró el acero empleado, el porcentaje de acero en exceso respecto del metrado teórico y los metrados ejecutados por cuadrilla para calcular el rendimiento real de la mano de obra (Chino Quispe y Zarate Chilqquetuma, 2024, p. 7).

**chino2024-03** · p. 147 (pág. PDF 177) · *dato* · Uso: Introducción-Situación problemática | Cap.3 Discusión (3.7) (desperdicio de acero)

> «En los niveles desde la cimentación hasta el nivel cinco se tiene un metrado de 50 143.36 kg y un uso de acero de 57 455. 93 kg, teniendo un desperdicio de 7 312.57 kg representando un desperdicio porcentual del 14.58%»

Paráfrasis: En el proyecto 01, de la cimentación al quinto nivel, se usaron 57.455,93 kg de acero frente a un metrado de 50.143,36 kg: un desperdicio de 7.312,57 kg, es decir, de 14,58 % con el método convencional (Chino Quispe y Zarate Chilqquetuma, 2024, p. 147).

**chino2024-04** · p. 147 (pág. PDF 177) · *dato* · Uso: Cap.3 Discusión (3.7) (desperdicio con control del corte)

> «en tanto el metrado desde el nivel seis hasta el nivel de techo es de 26 646.48 kg en estas se aplicó de método de despiece de acero pre ejecución resultando en un uso de 27 486.86 kg teniendo un desperdicio de 840.38 kg dejando un desperdicio porcentual del 3.15%»

Paráfrasis: En los niveles superiores del proyecto 01, del sexto al techo, donde sí se aplicó el despiece pre ejecución, se usaron 27.486,86 kg frente a 26.646,48 kg de metrado: un desperdicio medido de 840,38 kg (3,15 %) (Chino Quispe y Zarate Chilqquetuma, 2024, p. 147). En el proyecto 02 el valor medido fue de 3,19 % (p. 169).

**chino2024-05** · p. 148 (pág. PDF 178) · *metodo* · Uso: Cap.2 sección 2.6.2 (evaluación ex ante; precedente) | Cap.3 Discusión (3.7)

> «Para fines de la presente investigación se proyecta el uso del método de despiece pre ejecución en los niveles inferiores, es decir, desde la cimentación hasta el nivel cinco.»

Paráfrasis: El 8,94 % atribuido al despiece pre ejecución en los niveles inferiores es una proyección: los autores aplicaron el método, en forma teórica, a los niveles de la cimentación al quinto, que se habían construido con el método convencional (Chino Quispe y Zarate Chilqquetuma, 2024, p. 148).

**chino2024-06** · p. 169 (pág. PDF 199) · *dato* · Uso: Introducción-Situación problemática | Cap.3 Discusión (3.7)

> «En los niveles desde la cimentación hasta el nivel cinco se tiene un metrado de 104 210.62 kg y un uso de acero de 122 019.37 kg, teniendo un desperdicio de 17 808.752 kg representando un desperdicio porcentual del 17.09 %»

Paráfrasis: En el proyecto 02, de la cimentación al quinto nivel, se usaron 122.019,37 kg frente a 104.210,62 kg de metrado: 17.808,75 kg de desperdicio, equivalentes a 17,09 % con el método convencional (Chino Quispe y Zarate Chilqquetuma, 2024, p. 169).

**chino2024-07** · p. 192 (pág. PDF 222) · *conclusion* · Uso: Cap.3 Discusión (3.7)

> «En esta investigación el uso del método de despiece pre ejecución en la cantidad de material en el proyecto 01 se redujo de 14.58% a 8.94% y en el proyecto 02 se redujo de 17.09% a 6.71%»

Paráfrasis: Los autores concluyen que el despiece pre ejecución redujo el desperdicio de 14,58 % a 8,94 % en el proyecto 01 y de 17,09 % a 6,71 % en el proyecto 02, aunque bajó la productividad de la mano de obra: en el proyecto 01, el habilitado pasó de 0,014 a 0,021 hh/kg (Chino Quispe y Zarate Chilqquetuma, 2024, p. 192).

**chino2024-08** · p. 190 (pág. PDF 220) · *dato* · Uso: Cap.3 sección 3.4 (resultados de costos) | Cap.3 Discusión (3.7)

> «Con respecto al incremento de la utilidad de las empresas usando el método de despiece de acero pre ejecución en el proyecto 01 incrementa la utilidad en 3 250.31 soles en un porcentaje de 1.48% con respecto al método convencional.»

Paráfrasis: Frente al método convencional, el despiece pre ejecución aumentó la utilidad en S/ 3.250,31 (1,48 %) en el proyecto 01 y en S/ 27.516,30 (5,87 %) en el proyecto 02; el acero dimensionado la aumentó en 4,08 % y 6,63 % (Chino Quispe y Zarate Chilqquetuma, 2024, p. 190).

## 14. Cocarico Mamani (2022) — losa nervada postensada frente a HºAº, Edificio Ares (UMSA, Bolivia)

**Referencia APA 7 (verificada):** Cocarico Mamani, F. C. (2022). *Análisis comparativo técnico-económico de entrepisos de losa nervada postensada con tendones no adheridos y losa nervada de hormigón armado aplicado al Edificio Ares* [Proyecto de grado de licenciatura, Universidad Mayor de San Andrés]. https://repositorio.umsa.bo/handle/123456789/41974

**Archivo(s):** `04_Bibliografia/03_Tesis/Cocarico_2022_PG_Comparativo_Losa_Nervada_Postensada_vs_HA_UMSA_Parte1.pdf` (240 págs.: preliminares y pp. 1–212) y `…_Parte2.pdf` (200 págs.: pp. 213 en adelante, con capítulos 3–6, bibliografía y anexos; 25 páginas de anexos sin capa de texto)

**Verificación de portada y correcciones a la referencia propuesta:**

- Portada (Parte 1, pág. PDF 1): Universidad Mayor de San Andrés, Facultad de Ingeniería, Carrera de Ingeniería Civil; «Proyecto de grado»; postulante Franz Cleto Cocarico Mamani; asesor M.Sc. Ing. Nelson A. Vega Aguirre; La Paz, Bolivia, 2022.
- Se completa el título, que en la referencia propuesta estaba truncado: «…y losa nervada de hormigón armado aplicado al Edificio Ares». La portada dice «Proyecto de grado» sin precisar el grado; los agradecimientos lo sitúan en la formación de pregrado, de ahí «de licenciatura».
- Las cifras de costos usan precios de La Paz de 2022 y su formato de precios unitarios (formulario B-2 del DBC). No son directamente trasladables a Potosí 2025–2026.
- Paginación impresa: Parte 1, cuerpo p. N = pág. PDF N − 28; Parte 2, p. N = pág. PDF N + 212. El resumen (Parte 1, pág. PDF 5) no tiene número de página. Todas las fichas son de la Parte 2.

**Fila de la tabla de antecedentes:**

| Campo | Contenido |
|---|---|
| Autor (año) | Cocarico Mamani (2022) |
| País | Bolivia (La Paz) |
| Institución | Universidad Mayor de San Andrés |
| Objetivo | Comparar técnica y económicamente entrepisos de losa nervada postensada con tendones no adheridos y de losa nervada de HºAº en el Edificio Ares (25 niveles y 2 sótanos). |
| Diseño y muestra | Proyecto de grado de análisis comparativo: dos modelos estructurales con la misma arquitectura, diseño según la NB 1225001, verificación de estados límite, cómputos métricos, precios unitarios (formulario B-2) y cronogramas (MS Project). |
| Resultados (cifras) | Estructura 20 % más liviana (21.636 frente a 27.134 t); 26 % menos acero pasivo; costo 2,53 % menor (11,66 % sin fundación); plazo de 403 frente a 484 días (−16,7 %); incidencias: beneficios sociales 71 %, herramientas 5 %, gastos generales 13 %, utilidad 10 %, IVA 14,94 % e IT 3,09 %. |
| Relación con nuestra tesis | Referencia boliviana para la estructura del precio unitario (costos directos e incidencias) del modelo de costos del Cap. 2 y contexto de sistemas de losa. No trata la gestión de la calidad. |

**Fichas (7):**

**cocarico2022-01** · p. 267 (pág. PDF 55) · *metodo* · Uso: Introducción-Antecedentes de investigación

> «se realizó el análisis y diseño de dos modelos de edificios, cada uno con el sistema de entrepiso correspondiente, además se realizó las verificaciones en Estado Límite Último para las losas postensadas y en Estado Límite de Servicio para las losas de H°A°»

Paráfrasis: Cocarico Mamani (2022) analizó y diseñó dos modelos del Edificio Ares, cada uno con su sistema de entrepiso (losa nervada postensada con tendones no adheridos y losa nervada de HºAº). Verificó los estados límite correspondientes y determinó para cada uno el presupuesto y el plazo de construcción (p. 267).

**cocarico2022-02** · p. 254 (pág. PDF 42) · *definicion* · Uso: Cap.1 sección 1.8 (control de costos en obras públicas) | Cap.2 sección 2.5.4 (modelo de costos)

> «Donde los Costos Directos son: Materiales, Mano de Obra, Equipo y Maquinaria. Y los Costos Indirectos son las incidencias: Beneficios sociales, Herramientas, Gastos generales, Utilidad e Impuestos (IVA e IT).»

Paráfrasis: El precio unitario se compone de costos directos (materiales, mano de obra y equipo y maquinaria) y de costos indirectos o incidencias (beneficios sociales, herramientas, gastos generales, utilidad e impuestos IVA e IT) (Cocarico Mamani, 2022, p. 254).

**cocarico2022-03** · p. 256 (pág. PDF 44) · *dato* · Uso: Cap.2 sección 2.5.4 (supuestos del modelo de costos) — solo como referencia

> «Para la elaboración de precio unitarios se calculan las incidencias (ver ANEXO D-3), en la siguiente tabla se presentan todos los porcentajes de incidencias.»

Paráfrasis: En los precios unitarios del proyecto (La Paz, 2022) se aplicaron estas incidencias: beneficios sociales 71 %, herramientas 5 %, gastos generales 13 %, utilidad 10 %, IVA 14,94 % e IT 3,09 % (Cocarico Mamani, 2022, p. 256). Entre los precios de materiales figuran el fierro corrugado a Bs 8,35/kg y el hormigón premezclado H-25 con bomba a Bs 840/m³ (p. 255).

**cocarico2022-04** · p. 257 (pág. PDF 45) · *metodo* · Uso: Cap.1 sección 1.7.5 (contratación pública) | Cap.2 sección 2.5.4

> «Se adopta el formato de análisis de precios unitarios (formulario B-2) del Modelo de Documento Base de Contratación en el marco del Decreto Supremo N°181 de Normas Básicas del Sistema de Administración de Bienes y Servicios (SABS).»

Paráfrasis: Los precios unitarios se elaboraron con el formulario B-2 del modelo de Documento Base de Contratación del D.S. 181 (NB-SABS) (Cocarico Mamani, 2022, p. 257).

**cocarico2022-05** · p. 268 (pág. PDF 56) · *dato* · Uso: Cap.1 sección 1.6.1 (sistemas de losa) | Cap.3 Discusión (3.7)

> «Comparando el peso propio de la estructura de ambos edificios, se observa que el edificio con losas postensadas (21 636 ton) es 20% más liviana con respecto al edificio con losas de H°A° (27 134 ton).»

Paráfrasis: La estructura con losas postensadas, de 21.636 t, resultó 20 % más liviana que la de losas de HºAº, de 27.134 t. Usó 20 % menos hormigón sin contar la fundación y 26 % menos acero pasivo: 1.251.562,13 frente a 1.693.127,62 kg (Cocarico Mamani, 2022, pp. 268–269).

**cocarico2022-06** · p. 270 (pág. PDF 58) · *dato* · Uso: Cap.3 Discusión (3.7) (comparación de costos de sistemas de losa)

> «Determinado el precio total de construcción del edificio EHP presenta un ahorro económico del 2,53% con respecto al edificio EHA, y despreciando la fundación el ahorro incrementa a un 11,66% tal como se detalla en la siguiente tabla.»

Paráfrasis: El edificio con losas postensadas costó 2,53 % menos que el de HºAº (Bs 101.786.635,23 frente a Bs 104.424.285,47), y el ahorro sube a 11,66 % sin contar la fundación (Cocarico Mamani, 2022, p. 270).

**cocarico2022-07** · p. 271 (pág. PDF 59) · *dato* · Uso: Cap.3 Discusión (3.7) (plazos)

> «el edificio con losas de H°A° tiene una duración de 484 días y 403 días para el edificio con losas postensadas, resultando una reducción beneficiosa de 81 días (16,7%) del tiempo de construcción del edificio con losas postensadas con respecto al de H°A°.»

Paráfrasis: La construcción con losas postensadas tomaría 403 días, frente a 484 con losas de HºAº: 81 días menos (16,7 %) (Cocarico Mamani, 2022, p. 271).
