---
title: "Diseño de un Sistema de Gestión de la Calidad basado en la norma ISO 9001 para reducir costos mediante el control de materiales en losas alivianadas con viguetas pretensadas del Edificio de Posgrado de la Universidad Autónoma Tomás Frías, Potosí"
subtitle: "La tesis explicada para todo público"
date: "Universidad Autónoma Tomás Frías · Facultad de Ingeniería · Carrera de Ingeniería Civil · Potosí, 2026"
lang: es-BO
toc-title: "Contenido"
---

# Antes de empezar

## Qué es este documento

Este documento explica, en lenguaje cotidiano, una tesis de grado de Ingeniería Civil de la Universidad Autónoma Tomás Frías (UATF), en Potosí. Cuenta el trabajo completo: el problema, lo que se hizo, lo que se encontró y lo que se recomienda. Está escrito para cualquier persona: familias, autoridades, estudiantes y trabajadores de la construcción.

El documento que se presenta al tribunal es la tesis, con su formato oficial, sus citas y sus anexos. Esta explicación no la reemplaza: la acompaña y ayuda a entenderla.

## Cómo leerlo

- Cada capítulo explica primero lo esencial.
- Las secciones terminan con un recuadro **«En pocas palabras»** que resume la idea principal.
- Las palabras técnicas se explican la primera vez que aparecen. También están en el **Glosario**, al final.
- Las cifras usan el formato boliviano: el punto separa los miles y la coma, los decimales. Por ejemplo, 1.109,84 m² se lee «mil ciento nueve coma ochenta y cuatro metros cuadrados».
- «Bs» son bolivianos y «m²», metros cuadrados.

## La tesis en un minuto

En el campus de la UATF se construía el Edificio de Posgrado. Una parte importante de la obra eran las **losas alivianadas**, que son los pisos y techos hechos con viguetas de hormigón pretensado, bloques de plastoformo y una capa de hormigón encima.

La primera losa se construyó en 2025 sin un sistema que controlara la calidad y el uso de los materiales. No se tomaron muestras del hormigón de esa losa. Además, se entregó más plastoformo del necesario, y el acero pagado supera en 16,75 % al que resulta de los planos, una diferencia entre documentos que conviene aclarar.

A inicios de 2026, la subida del precio de los combustibles llevó a paralizar la obra, y el contrato se resolvió. Por eso, el resto de la losa no se construyó durante el estudio.

La tesis diseñó un **Sistema de Gestión de la Calidad**, basado en la norma internacional ISO 9001, para controlar los materiales de las losas que faltan. Como no se podía probar en la obra, se evaluó con una **simulación por computadora** de 20.000 escenarios posibles.

El resultado: el sistema reduce el desperdicio y el costo de los errores, y en 94 de cada 100 escenarios baja el costo por metro cuadrado. Pero lo baja en promedio un 1,47 %, no el 5 % que se esperaba al empezar.

## La tesis en 10 cifras

**Tabla 0.1.** Las cifras principales de la tesis

| Qué se midió | Cifra | Qué significa |
|---|---|---|
| Superficie de la primera losa | 1.109,84 m² en 41 paños | Es la losa que se usó como punto de comparación |
| Losa que faltaba construir | 2.234,60 m² | Es la parte que el sistema propuesto debía controlar |
| Peso de las losas en el contrato | 21,45 % del monto original | Más de la quinta parte del dinero del contrato |
| Cumplimiento de la norma ISO 9001 | 19,8 % | La obra cumplía menos de una quinta parte de lo que pide la norma |
| No conformidades encontradas | 22 | Son fallas frente a lo que exigían la norma, el contrato o las especificaciones |
| Plastoformo entregado de más | 5,01 % por encima de lo necesario | Llegó a la obra material que no hacía falta |
| Acero pagado frente al calculado | 16,75 % por encima | Es una diferencia entre documentos que conviene aclarar |
| Muestras de hormigón de la losa | 0 | No hay prueba de la resistencia del hormigón de la losa |
| Ahorro medio con el sistema | 1,47 % del costo por m² (unos Bs 9.177 en el saldo) | El sistema ahorra, pero poco en un solo ítem |
| Probabilidad de ahorrar / de llegar al 5 % | 0,9422 / 0,0008 | Casi siempre ahorra; casi nunca llega al 5 % |

> **En pocas palabras:** la tesis muestra que controlar bien los materiales de la losa reduce el desperdicio y el costo de los errores, y casi siempre ahorra dinero. Pero en una sola parte de la obra el ahorro es pequeño: alrededor de 1,5 % y no 5 %.

# Introducción: el problema y lo que se buscó

## Qué se estudió y por qué

La tesis estudia la calidad, el control de los materiales y los costos de las losas alivianadas con viguetas pretensadas del Edificio de Posgrado de la Universidad Autónoma Tomás Frías (UATF), en Potosí.

Una **losa** es la placa de hormigón que hace de techo de un piso y de suelo del siguiente. La losa **alivianada** pesa menos porque combina tres piezas (Figura I.1). Las **viguetas pretensadas** son piezas de hormigón hechas en fábrica, con alambres de acero tensados, y cargan el peso. Los bloques de **plastoformo**, el material blanco de los embalajes, solo ocupan espacio. Encima, una capa de hormigón vaciada en la obra une todo.

![**Figura I.1.** Corte de la losa alivianada (Plano 02 del proyecto). Cómo leerla: las «T» invertidas son las viguetas; los bloques con puntitos, el plastoformo, y la franja de arriba, la capa de hormigón o carpeta de compresión.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/plano02_seccion_losa_viguetas.png){width=60%}

Las obras pierden dinero por tres causas frecuentes: los **retrabajos** (rehacer lo que salió mal), el **desperdicio** (material comprado que no queda en la obra) y el incumplimiento de las especificaciones técnicas. Estas fijan cómo debe ser cada material y trabajo. Según Álvarez Quintero (2014), los retrabajos llegan hasta el 12,4 % del costo de un proyecto.

Para evitarlo existe el **Sistema de Gestión de la Calidad (SGC)**: reglas, controles y registros que dicen qué revisar, quién lo hace y cómo se deja constancia. Funciona como la lista de chequeo de un piloto antes de despegar. La norma internacional **ISO 9001** fija sus requisitos con un ciclo que se repite: planificar, hacer, verificar y actuar (ISO, 2026).

La Tabla I.1 resume los estudios previos más cercanos a este trabajo.

**Tabla I.1.** Estudios previos más importantes

| Estudio | Qué encontró |
|---|---|
| Forcada et al. (2017), España | Retrabajos: 2,75 % del valor original del contrato en 40 proyectos de una constructora certificada con ISO 9001 |
| Chino Quispe y Zarate Chilqquetuma (2024), Perú | Desperdicio de acero: 14,58 % y 17,09 % con el método común; 3,15 % y 3,19 % planificando el corte de las barras |
| Alcón Aranda (2009), Bolivia | Con buena supervisión, viguetas de calidad óptima o buena; sin ella, mala o regular. Su recepción en obra es clave |

En Bolivia, los estudios más cercanos tratan de fábricas de viguetas, que cumplían el 24 % y el 43 % de los requisitos de la ISO 9001 (Mamani Calsina, 2025; Peña Callisaya, 2024). Ninguna investigación boliviana revisada aplica un SGC a este tipo de losa en la obra. Tampoco estima su efecto en el costo y el desperdicio con documentos de obra, un escenario de comparación y su margen de incertidumbre. Ese es el vacío que aborda la tesis.

> **En pocas palabras:** los retrabajos y el desperdicio encarecen las obras. Ningún estudio boliviano revisado había aplicado un sistema de calidad a este tipo de losa en la obra.

## El problema en la obra

### El contrato y la primera losa

Se contrató la **obra gruesa** del edificio (su «esqueleto» de hormigón armado) hasta la tercera losa. El contrato, firmado el 24 de abril de 2025, no admitía reajuste de precios. Sus precios incluían las «reparaciones por trabajos defectuosos». Controlaban la obra la **Supervisión**, que revisa los trabajos, y la **Fiscalización**, que vela por el contrato, ambas de la UATF.

La losa alivianada valía el 21,45 % del contrato original, a Bs 215,68 por metro cuadrado (m²). La **primera losa** tiene 41 **paños** (tramos de losa entre vigas) y mide 1.109,84 m². Fue la única construida, y entró completa en la Planilla de avance N.º 2, el documento con que se mide y se paga lo construido (Tabla I.2).

**Tabla I.2.** El contrato y la losa en cifras

| Concepto | Cifra |
|---|---|
| Monto del contrato | Bs 3.367.031,95 → Bs 3.610.125,43 (+7,22 %) |
| Plazo | 270 → 360 días (+33,3 %) |
| Avance al cierre del contrato | Bs 2.073.392,68 (57,43 %) |
| Primera losa, construida | 1.109,84 m²; Bs 239.365,07 (33,18 % del total de losa) |
| Segunda y tercera losa, sin construir | 2.234,60 m² (1.117,30 m² cada una); Bs 481.948,03 |

La escasez de combustibles golpeó a la obra. En junio de 2025, la Fábrica Nacional de Cemento paró por un tiempo porque no tenía diésel, y el proveedor del acero había entregado solo el 30 % de un pedido. En Potosí, entre diciembre de 2023 y septiembre de 2026, el cemento subió 74,1 % y el fierro corrugado, 65,7 % (Instituto Nacional de Estadística [INE], 2026).

### Lo que muestran los documentos

Los documentos muestran una losa sin control de calidad registrado:

- **Hormigón sin ensayar.** Su resistencia se comprueba rompiendo en laboratorio cilindros llamados **probetas**. El único certificado, del 5 de diciembre de 2025, es de columnas y vigas, no de la losa. Aun así, la losa entró en la planilla cerrada el 8 de diciembre, antes de cumplirse 28 días desde la autorización del vaciado.
- **Ningún problema anotado.** El **Libro de Órdenes** es el cuaderno oficial entre la empresa y la Supervisión. Sus 24 anotaciones, de septiembre a noviembre de 2025, no registran ninguna **no conformidad** (un incumplimiento de lo exigido), material rechazado ni trabajo rehecho.
- **Certificados tardíos.** Los de las viguetas y del plastoformo son del 27 de noviembre, cuando la losa ya se armaba, y no tienen firma ni sello.

El acero de la losa se paga en la partida de acero estructural. Ahí hay diferencias entre documentos que conviene aclarar con la Supervisión y la Fiscalización:

- En la Planilla N.º 2, ese acero figura una vez (4.171,18 kg). En el cómputo de cierre (la cuenta final de cantidades) de una versión en Excel, figura multiplicado por tres (12.513,54 kg), aunque solo se construyó una losa.
- La planilla de cierre tiene dos versiones: la firmada, que la tesis usa como oficial, descuenta 1.862,81 kg de acero, y la de Excel, 1.915,16 kg.
- La especificación de la losa también incluye ese fierro, de modo que podría estar contado dos veces. Sin el desglose de precios del contrato, el estudio no puede confirmarlo ni descartarlo.

El 5 de enero de 2026, la empresa pidió resolver el contrato por fuerza mayor y paralizar la obra. Alegó que el fin de la subvención a la gasolina y al diésel (Decreto Supremo 5503) encareció materiales, transporte y mano de obra. La UATF respondió favorablemente el 10 de febrero de 2026, y la segunda losa no se construyó durante la investigación.

Sin registros de resistencia, recepción, no conformidades ni consumos, el desperdicio y el costo de no calidad de la primera losa no pueden conocerse directamente.

> **En pocas palabras:** la primera losa se construyó y se pagó sin pruebas ni registros de calidad. Si las dos losas restantes se hacen igual, pueden repetirse esas deficiencias.

## Las preguntas de la investigación

La pregunta general fue: **¿de qué manera un SGC basado en la norma ISO 9001, centrado en el control de materiales, permite reducir los costos de construcción de estas losas?** Las específicas fueron cuatro:

1. ¿Cómo se manejaron la calidad y los materiales en la primera losa?
2. ¿Cuánto material se desperdició y cuál fue el **costo de no calidad**, es decir, lo que costó hacer mal las cosas?
3. ¿Qué partes debe tener un SGC para este tipo de losa?
4. ¿En qué medida reduce el SGC el costo por m² y el desperdicio, frente a la primera losa?

## Los objetivos

El **objetivo general** fue diseñar un SGC basado en la norma ISO 9001, centrado en el control de materiales, para reducir los costos de construcción de estas losas. Los objetivos específicos fueron cinco:

1. **Diagnosticar la primera losa:** cómo se manejaron la calidad y los materiales, qué no conformidades hubo y por qué.
2. **Medir la línea base**, que es el punto de partida para comparar, como pesarse antes de una dieta. Consiste en cuantificar el desperdicio de cada material y el costo de no calidad, comparando lo que piden los planos, lo que se compró y lo que se pagó.
3. **Armar el sistema.** Incluye un plan de la calidad, que define controles y registros, y un plan de puntos de inspección y ensayo (PPI): la lista de momentos en que el trabajo se revisa antes de seguir. Suma procedimientos de control de materiales, el manejo de las no conformidades y un registro de costos de la calidad. Se basa en las normas ISO 9001:2026 e ISO 10005:2018.
4. **Calcular su efecto por adelantado** (*ex ante*) en el costo por m² y el desperdicio de los 2.234,60 m² restantes, con un modelo de costos y una simulación de Monte Carlo.
5. **Decidir y validar:** contrastar la hipótesis con reglas de probabilidad (nivel de significancia de 0,05) y validar el SGC con juicio de expertos, es decir, con la calificación de ingenieros con experiencia. Para ese juicio se preparó un formulario; las conclusiones se apoyan en los documentos y en la simulación, sin opiniones de expertos.

> **En pocas palabras:** el objetivo fue diseñar un sistema de calidad para las losas, en cinco pasos: diagnosticar, medir, armar el sistema, simular su efecto y decidir.

## Las hipótesis

Una **hipótesis** es una respuesta tentativa que se pone a prueba con datos. Es como cuando un maestro de obra dice «si curamos bien el hormigón, saldrá más resistente» y lo comprueba rompiendo probetas.

La **hipótesis general** afirma que el SGC reduce **en al menos 5 %** el costo de construcción por m² de las losas, con los precios del contrato, frente a la primera losa. No bastaba con que el costo bajara un poco: de cada Bs 100 por m², el ahorro debía ser de Bs 5 o más. La **hipótesis nula** sostiene lo contrario (Hernández-Sampieri y Mendoza Torres, 2018): que el SGC no reduce el costo o lo reduce en menos de 5 %.

Las dos **hipótesis específicas** dicen que el SGC reduce el **índice de desperdicio** y el costo de no calidad. El índice de desperdicio es el porcentaje de material consumido por encima de lo que piden los planos. El costo de no calidad suma las fallas internas, detectadas antes de entregar la obra, y las externas, que aparecen después.

> **En pocas palabras:** la tesis planteó que el sistema bajaría al menos 5 % el costo por m², además del desperdicio y del costo de no calidad.

## Las variables

Una **variable** es algo que cambia y se puede medir. La tesis compara la losa sin y con sistema (lo que se cambia) y observa su costo (lo que se mide). Como los precios subieron mucho, todo se calcula con los precios del contrato. Así, si el costo baja, es por el sistema y no por la inflación (Tabla I.3).

**Tabla I.3.** Las variables del estudio

| Tipo | Variable | Qué se observa |
|---|---|---|
| Independiente: lo que se cambia | El SGC | Planificación, control de materiales, control del proceso, seguimiento y mejora |
| Dependiente: lo que se mide | Costo por m² de la losa | Desperdicio, costo de no calidad, costo de la calidad (lo que cuesta prevenir y revisar) y cumplimiento del hormigón |
| Interviniente, controlada | Precios de los materiales | Se fijan en los del contrato |

## Por qué importa

**En lo técnico**, la tesis ofrece un procedimiento para planificar, inspeccionar y aceptar materiales y trabajos según la ISO 9001:2026 y el código de hormigón ACI 318-25 (ACI Committee 318, 2025). Ese código pide al menos una muestra de hormigón por cada 5.000 pies cuadrados de losa (unos 464,5 m²). En la primera losa correspondían al menos tres, y no se registró ninguna.

**En lo económico**, el saldo de 2.234,60 m² vale Bs 481.948,03, y alcanzar justo la meta del 5 % ahorraría unos Bs 24.097. Es una referencia, no el ahorro esperado, que se presenta en los resultados. Sin reajuste de precios, y con una oferta 15,8 % menor que el presupuesto estimado por la UATF (cálculo de la tesis), el desperdicio y los retrabajos los paga la empresa. Reducirlos protege la obra y el dinero público.

**En lo social**, el edificio servirá a la comunidad universitaria y a la región, y la UATF podrá usar el sistema en otras obras.

**En el método**, la tesis deja herramientas reutilizables: listas de verificación, fichas de control de materiales y una planilla de costos de la calidad. También muestra cómo estimar el efecto de un SGC que no se puede medir en obra.

> **En pocas palabras:** el sistema ayuda a controlar la losa como pide la técnica, cuida el dinero público y sirve para otras obras.

## Hasta dónde llega el estudio

El SGC cubre la losa desde la compra y la recepción de los materiales hasta la medición y el pago. Su efecto se calculó por adelantado sobre los 2.234,60 m² restantes. El estudio no abarca el diseño estructural, los demás trabajos de la obra ni la certificación ISO de la empresa. Tampoco aplica el sistema en la obra: la tesis lo describe como un protocolo para construir el saldo. Usa documentos de mayo a diciembre de 2025 e información hasta octubre de 2026.

## Cómo se investigó

La investigación es **aplicada**: busca resolver un problema práctico. Es **cuantitativa**: trabaja con números y pone a prueba hipótesis. Y es **explicativa**: busca el efecto del SGC sobre el costo (Hernández-Sampieri y Mendoza Torres, 2018).

### Un cambio de plan

El plan inicial era un «antes y después» (diseño cuasiexperimental): la primera losa, sin sistema, frente a la segunda, con él. Como la segunda no se construyó, se aplicó la alternativa prevista. Es un diseño **no experimental**, porque el SGC no se aplicó en la obra, y tiene tres partes:

1. **Línea base:** la primera losa se reconstruyó con documentos (planillas, cómputos, certificados y el Libro de Órdenes), sin entrevistas. Se revisaron sus 41 paños, todos: es un censo, no una muestra.
2. **Tratamiento:** el SGC diseñado.
3. **Evaluación por adelantado:** un modelo de costos, con los precios del contrato, calcula el costo de los 2.234,60 m² restantes sin SGC, que hace de **control**, y con SGC.

### Tirar los dados miles de veces

Para cada dato incierto, como el hormigón perdido, que nadie anotó, el modelo usa un rango: un valor mínimo, uno más probable y uno máximo. La **simulación de Monte Carlo** es como tirar los dados miles de veces. En cada tiro, la computadora elige un valor de cada rango y calcula el costo sin y con el sistema. Se hicieron 20.000 tiros, con una «semilla» fija para que cualquiera pueda repetir el cálculo. Contar cuántos tiros cumplen una condición da su probabilidad.

### La regla para decidir

La hipótesis general se acepta solo si el costo por m² baja 5 % o más en al menos el 95 % de los tiros, es decir, en 19.000 de 20.000. Equivale a un nivel de significancia de 0,05: aceptar como máximo 5 posibilidades en 100 de equivocarse. Las hipótesis específicas siguen la misma regla.

> **En pocas palabras:** la tesis reconstruyó la primera losa con documentos y simuló 20.000 veces el costo de las restantes, sin y con el sistema. La meta del 5 % debía cumplirse en al menos el 95 % de los tiros.

# Capítulo 1. Lo que ya se sabe: calidad, desperdicio y losas alivianadas

Este capítulo resume lo que ya se sabe: otros estudios, las ideas básicas de la tesis, la losa, sus normas técnicas y las reglas de la obra pública en Bolivia.

## Lo que encontraron otros estudios

El **estado del arte** es lo que otros investigadores ya descubrieron. La tesis revisó 14 artículos científicos, 26 trabajos de grado de Bolivia, Perú, Colombia y Ecuador, y documentos técnicos. La Tabla 1.1 resume los principales.

**Tabla 1.1.** Estudios previos más importantes para la tesis

| Estudio | País | Qué encontró |
|---|---|---|
| Forcada et al. (2017) | España | Rehacer trabajos costó el 2,75 % del valor del contrato |
| Khadim et al. (2023) | Pakistán | Con las fallas ocultas, el costo de la calidad llegó al 12,76 % |
| Álvarez Quintero (2014) | Colombia | Trabajos rehechos: 6,59 % en promedio; 0,72 % con sistema de calidad |
| Galarza Meza (2011) | Perú | Desperdicio de hormigón: 22 % sin control; 2,8 % con pedidos limitados |
| Chino Quispe y Zarate Chilqquetuma (2024) | Perú | Desperdicio de acero: 14,58 % y 17,09 % con el método usual; 3,15 % y 3,19 % con despiece previo |
| Pajarito Mamani (2015), Mamani Gutiérrez (2017), Peña Callisaya (2024) y Mamani Calsina (2025) | Bolivia | Cumplimiento inicial de la ISO 9001 en fábricas de viguetas: 33,43 %, 12 %, 43 % y 24 % |
| Alcón Aranda (2009) | Bolivia | En obra, la calidad de las viguetas dependió de la supervisión |
| Castañeda Briceño (2017) | Perú | La losa de viguetas costó 27 % menos y tardó 40 % menos que la aligerada convencional |

Hay tres lecciones: la mayor parte del costo de los errores nunca se registra (Khadim et al., 2023); el desperdicio nace sobre todo de la gestión y es en gran parte evitable (Formoso et al., 1999); y un sistema de calidad rinde poco a poco (Prado-Román et al., 2018) y, si no se aplica de verdad, queda «en el papel» (Romero y Serpell, 2007).

No se encontraron mediciones del desperdicio de viguetas ni de plastoformo, y los estudios bolivianos sobre calidad miran las fábricas, no la obra. Además, varios estudios previos aceptaron su **hipótesis** (la respuesta que ponen a prueba) sin un punto de comparación ni un cálculo de la incertidumbre (De la Vega Sernades, 2023). La tesis cubre ese **vacío de conocimiento** (lo que nadie había estudiado): diseña un sistema de calidad para construir la losa y compara escenarios sin y con sistema, midiendo la incertidumbre.

> **En pocas palabras:** los errores y el desperdicio cuestan caro, y un sistema de calidad ayuda si se aplica de verdad. Nadie lo había estudiado en Bolivia para construir losas con viguetas pretensadas.

## Qué es la calidad en una obra

Para las normas ISO, la **calidad** es el grado en que algo cumple sus **requisitos**, es decir, lo que se pide o se espera (ISO 9000:2026). No es lujo: una losa sencilla tiene calidad si cumple sus documentos. Los requisitos están en los planos, el contrato, las normas y las **especificaciones técnicas**, que dicen cómo deben ser los materiales y el trabajo. Por ejemplo, la losa pide hormigón de 250 kg/cm²: cada centímetro cuadrado endurecido debe aguantar 250 kilos.

### Controlar no es lo mismo que asegurar

**Controlar** es revisar, ensayar y aceptar o rechazar: detecta el error, pero no lo evita. **Asegurar** es planificar acciones que den confianza, antes de trabajar, de que se cumplirán los requisitos (Alfaro Félix, 2011).

Las **probetas** son cilindros de hormigón que se llenan durante el vaciado y se rompen en un laboratorio a los 28 días para medir su resistencia. Romperlas es controlar, porque el hormigón ya está puesto. Aprobar la **dosificación** (la receta del hormigón) y revisar el fierro antes de vaciar es asegurar. En la cocina, controlar es probar la sopa servida; asegurar, revisar la receta antes de cocinar.

En la construcción, el cambio de la inspección final a la prevención está incompleto (Pons Achell, 2014). En la primera losa del Edificio de Posgrado, el control se limitó a una revisión antes del vaciado, sin registros de recepción de materiales ni ensayos del hormigón de la losa.

> **En pocas palabras:** calidad es cumplir lo que se pidió. Controlar es encontrar el error cuando ya ocurrió; asegurar es organizarse para que no ocurra.

## El sistema de gestión de la calidad y la norma ISO 9001:2026

Un **sistema de gestión de la calidad (SGC)** es la forma ordenada en que una organización fija su política, sus objetivos y sus procesos para lograr la calidad. La norma que dice qué debe tener es la **ISO 9001**, la única de su familia que permite certificarse (Zurita Ferrel, 2024). Su sexta edición, la **ISO 9001:2026**, se publicó el 16 de septiembre de 2026 y reemplaza a la de 2015 sin cambiar su estructura. El Instituto Boliviano de Normalización y Calidad (IBNORCA) la adoptó como NB/ISO 9001:2026. Esta edición refuerza la cultura de la calidad y la ética, el cambio climático, los **riesgos** (lo que podría salir mal) y la planificación de los cambios.

### Las cláusulas 4 a 10

La norma se divide en capítulos llamados **cláusulas**; las cláusulas 4 a 10 contienen los requisitos (Tabla 1.2).

**Tabla 1.2.** Las cláusulas 4 a 10 de la norma ISO 9001

| Cláusula | De qué trata |
|---|---|
| 4. Contexto | Situación interna y externa, partes interesadas y alcance |
| 5. Liderazgo | Compromiso de la dirección, política de la calidad y responsabilidades |
| 6. Planificación | Riesgos y oportunidades, objetivos y cambios |
| 7. Apoyo | Recursos, personal competente, comunicación y documentos |
| 8. Operación | Control del trabajo, de los proveedores y de lo que no cumple |
| 9. Evaluación del desempeño | Seguimiento, medición, auditoría interna y revisión por la dirección |
| 10. Mejora | Incumplimientos (**no conformidades**) y **acciones correctivas**, que eliminan su causa |

### El ciclo planificar, hacer, verificar y actuar

Las cláusulas siguen el **ciclo PHVA** (Zurita Ferrel, 2024), como una cocinera que planifica el menú, cocina, prueba y ajusta la receta. Planificar es la cláusula 6; hacer, la 7 y la 8; verificar, la 9; y actuar, la 10 (Figura 1.1). En una obra, cada losa puede recorrer el ciclo.

![**Figura 1.1.** La norma ISO 9001 en el ciclo PHVA. Cómo leerla: las cajas de color son los pasos del ciclo, con su número de cláusula; el liderazgo está al centro. A la izquierda, lo que entra al sistema; a la derecha, lo que sale. Basada en la ISO 9001:2026 y en Zurita Ferrel (2024).](07_Entregables/Explicacion_Para_Todo_Publico/figuras/diagramas/tikz_1694af51624b76f04e5e.png){width=90%}

### Los siete principios

La norma se apoya en siete **principios**: enfoque al cliente, liderazgo, compromiso de las personas, enfoque a procesos, mejora, decisiones basadas en la evidencia y gestión de las relaciones (Peña Callisaya, 2024). Solo valen si se aplican (Prado-Román et al., 2018): en la losa, decidir con evidencia es aceptar el hormigón con ensayos y pagar con registros.

### El plan de la calidad

Como cada obra es única, se usa un **plan de la calidad** (norma ISO 10005:2018), que dice qué procesos, procedimientos y recursos se aplicarán, quién y cuándo, aunque la empresa no esté certificada. En la obra se concreta en el **plan de puntos de inspección y ensayo (PPI)**: para cada revisión fija el criterio, la frecuencia y el responsable, y marca **puntos de espera**, donde el trabajo se detiene hasta que alguien aprueba (Muro Núñez, 2020). Es como la lista de chequeo de un piloto: si algo no está bien, el avión no despega.

> **En pocas palabras:** un SGC ordena el trabajo para que las cosas salgan bien. La ISO 9001:2026 lo organiza en las cláusulas 4 a 10 y en el ciclo PHVA; en una obra se aplica con un plan de la calidad y un PPI.

## El costo de la calidad

Los **costos de la calidad** suman lo que se gasta para cumplir los requisitos y lo que cuesta no cumplirlos (Gracia Villar y Dzul López, 2007). El modelo más usado (PAF) los separa en cuatro grupos:

- **Prevención**, para evitar errores: plan de la calidad, revisión de planos, capacitación.
- **Evaluación**, para comprobar el trabajo: revisión de materiales, ensayos del hormigón.
- **Fallas internas**, halladas antes de entregar la obra: viguetas rotas, hormigón y acero desperdiciados, fierro armado de nuevo.
- **Fallas externas**, halladas después: reparación de grietas, descuentos por cantidades medidas de más.

### Pagar dos veces por hacer mal la primera

Las fallas forman el **costo de no calidad**, que nunca está en el presupuesto y es una pérdida neta (Alfaro Félix, 2011): se paga el material perdido y se vuelve a pagar para corregir. Algunos errores quedan escondidos: sin probetas del hormigón de la losa, una resistencia baja solo se nota cuando aparecen grietas o hundimientos.

Según la regla 1-10-100 que recogen Khadim et al. (2023), es mejor invertir una unidad en prevención que gastar diez en corregir o cien en una falla. Como cada aumento de la prevención rinde menos, el costo total tiene un **punto óptimo** (Figura 1.2), que no es cero fallas: no existe el proceso perfecto (Gracia Villar y Dzul López, 2007).

![**Figura 1.2.** Las curvas de los costos de la calidad. Cómo leerla: hacia la derecha crece la inversión en prevenir. La línea azul (prevención y evaluación) sube, la roja (fallas) baja y la negra, su suma, tiene el óptimo en su punto más bajo. Curvas ilustrativas, adaptadas de Gracia Villar y Dzul López (2007).](07_Entregables/Explicacion_Para_Todo_Publico/figuras/diagramas/tikz_de8bf16d8fe4eacf7bae.png){width=90%}

> **En pocas palabras:** prevenir y revisar cuesta; equivocarse cuesta más, porque obliga a pagar dos veces. Un poco de prevención ahorra mucho en correcciones.

## El desperdicio de materiales y cómo se mide

El **desperdicio** es toda pérdida que cuesta dinero sin agregar valor para el cliente (Formoso et al., 1999). Es **directo** si sale como escombro, como una vigueta rota, e **incorporado** si queda en la obra sin que los planos lo pidan, como una carpeta más gruesa que la especificada (Ccoyllo Sifuentes, 2016). Las causas que más influyen son los cambios de diseño, el trabajo descuidado y el mal almacenamiento (Luangcharoenrat et al., 2019).

### El índice de desperdicio

Para medir una pérdida hay que saber cuánto material se necesitaba (Galarza Meza, 2011). La tesis usa el **índice de desperdicio de materiales (IDM)**:

**IDM = (cantidad real − cantidad teórica) ÷ cantidad teórica × 100**

La **cantidad teórica** sale de los planos; la **real** es la consumida. Si los planos piden 100 bloques y se usan 105, el índice es 5 %. En el acero, la teórica debe salir de la **planilla de despiece**, que detalla cada barra (Abbott y Rodríguez, 2008). La real sale de los documentos de compra, del almacén y de los vales de salida (Galarza Meza, 2011), y conviene medirla cada semana o en cada vaciado (Formoso et al., 1999).

> **En pocas palabras:** desperdicio es el material que se paga y no agrega valor. Se mide comparando lo usado con lo que pedían los planos, con registros de compra, almacén y consumo.

## La losa alivianada: un sándwich de tres capas

Una **losa** es la placa de hormigón que hace de techo de un piso y de piso del siguiente. La **losa alivianada** pesa menos que una maciza porque parte de su volumen es un material liviano. Funciona como un sándwich (Figura 1.3):

- **Abajo, las viguetas pretensadas:** barras de hormigón hechas en fábrica, con alambres de acero muy estirados por dentro que les dan fuerza. Van en paralelo, cada 50 cm, y cargan el peso.
- **En medio, el plastoformo:** bloques de poliestireno expandido, el material blanco de las cajas de electrodomésticos, que aligeran la losa.
- **Arriba, la carpeta de compresión:** hormigón de 5 cm con una malla de fierro delgado, vaciado en obra junto con las vigas.

Unos **nervios** de hormigón cruzan las viguetas para darles rigidez. Con 17 cm de alto, una losa así pesa 173,80 kg/m², y una llena, 408,00 kg/m² (Alcón Aranda, 2009).

![**Figura 1.3.** Sección de la losa. Cómo leerla: es la losa cortada como un pan. Las «T» invertidas son las viguetas; los bloques con puntitos, el plastoformo; la franja de arriba, la carpeta. Tomada del Plano 02.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/plano02_seccion_losa_viguetas.png){width=90%}

### Los materiales

Las especificaciones técnicas piden viguetas certificadas por IBNORCA e ISO; plastoformo de 100 × 50 × 20 cm; hormigón de 250 kg/cm² (H25) con al menos 400 kg de cemento por metro cúbico; y fierro para la malla y para los **negativos**, refuerzos sobre los apoyos. El fabricante de las viguetas certificó una losa de 20 + 5 = 25 cm con ejes cada 50 cm (PRETENSA, 2025). Pero el proveedor del plastoformo certificó 2.350 bloques de otra medida, 20 × 100 × 44 cm (UNICON, 2025), y el corte del Plano 02 marca 15 + 5 cm (Figura 1.4). El capítulo 2 analiza estas diferencias.

![**Figura 1.4.** Corte transversal de la losa. Cómo leerla: viguetas cada 0,50 m, plastoformo entre ellas y, encima, la carpeta de 5 cm con malla de 6 mm cada 20 cm («φ6c/20»). A la derecha: 0,05 m de carpeta y 0,15 m de bloque. Tomado del Plano 02.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/plano02_corte_transversal.png){width=90%}

### Cómo se construye y qué se revisa

La losa se construye en once pasos (Tabla 1.3), cada uno con un **punto crítico**: algo que, si no se revisa a tiempo, solo se corrige rehaciendo o desperdiciando. Lo más importante es recibir bien los materiales (Alcón Aranda, 2009); **liberar** cada **paño** (cada recuadro de losa entre vigas), es decir, aprobarlo por escrito antes del vaciado; y tomar las muestras de hormigón ante el supervisor (Cajías Luna, 2023). **Apuntalar** es sostener las viguetas con soportes provisionales; **curar**, mantener húmedo el hormigón para que endurezca.

**Tabla 1.3.** Los once pasos de la losa y lo que se revisa

| Pasos | Qué se revisa |
|---|---|
| 1 a 3. Recibir los materiales | Cantidad, tipo y medidas; piezas enteras y sin fisuras; cemento bajo techo; acero certificado y sin óxido excesivo |
| 4. Apuntalar | Puntales antes de montar los bloques |
| 5 y 6. Colocar viguetas y plastoformo | Ejes cada 50 cm; viguetas bien apoyadas; bloques enteros y sin pisar |
| 7 y 8. Armar nervios, fierros e instalaciones | Malla de 6 mm cada 20 cm; fierros sobre los apoyos; tubos fijos |
| 9. Liberar el paño | Punto de espera: autorización escrita de la Supervisión |
| 10. Vaciar el hormigón | Sin interrupciones; bien vibrado; sin agua de más; muestras al azar |
| 11. Curar y desapuntalar | Hormigón húmedo al menos 7 días; puntales retirados solo cuando las probetas alcanzan la resistencia requerida |

> **En pocas palabras:** la losa es un sándwich de viguetas, plastoformo y hormigón con malla de fierro. Se construye en once pasos; lo clave es recibir bien los materiales, liberar cada paño y tomar muestras del hormigón.

## Cómo se controlan el hormigón y el acero

La especificación técnica de la losa cita la **CBH-87**, Norma Boliviana del Hormigón Armado. La norma boliviana actual de hormigón estructural es la **NB 1225001-1:2017**, basada en el código estadounidense ACI 318 (Cocarico Mamani, 2022). A ella remite la **Norma Boliviana de Diseño Sísmico (NBDS)**, obligatoria desde la R.M. 271/2023, que no menciona la CBH-87 (MOPSV, 2023). Por eso la tesis toma como marco vigente la NBDS y la NB 1225001, y trata la CBH-87 como la norma citada por la especificación. Las viguetas siguen la **NB 997:2016**, que su fabricante declara cumplir (PRETENSA, 2025).

Para el hormigón, la tesis sigue el capítulo 26 del **ACI 318-25** (ACI Committee 318, 2025):

- **Muestras:** al menos una por día, por cada 114,7 m³ y, en losas, por cada 464,5 m²; una losa de 1.109,84 m², como la primera, necesita al menos tres. Cada ensayo promedia dos o más probetas rotas a los 28 días.
- **Aceptación:** el promedio de tres ensayos seguidos debe alcanzar la resistencia pedida, y ningún ensayo del H25 puede bajar de unos 214,8 kg/cm².
- **Curado:** hormigón húmedo 7 días a 10 °C o más, con un plan especial para el frío.

En el acero, el código admite las barras corrugadas de la norma ASTM A615, que deben llegar sin óxido excesivo, barro ni aceite, y quedar bien apoyadas para no moverse al vaciar.

La NBDS pide para las losas de viguetas al menos 250 mm de altura total, con una carpeta de 50 mm o más, vaciada junto con las vigas (MOPSV, 2023). La especificación (20 + 5 cm) cumple; el corte del Plano 02 (0,20 m en total), no. Según la tesis, corresponde a la Supervisión resolverlo con el proyectista.

> **En pocas palabras:** la especificación cita la CBH-87, pero la norma sísmica obligatoria remite a la NB 1225001, basada en el ACI 318. Según el ACI 318-25, una losa como la primera necesita al menos tres muestras de hormigón.

## Las reglas de la obra pública en Bolivia

La obra de la UATF es pública: se paga con dinero del Estado y sigue la Ley 1178 (SAFCO) y sus normas básicas de contratación, las **NB-SABS** (D.S. 0181). Estas limitan los cambios a un contrato de obra, que no pueden subir los **precios unitarios** (lo que se paga por cada unidad, como un metro cuadrado de losa): hasta 10 % con un **contrato modificatorio**, hasta 5 % con una **orden de cambio** y hasta 15 % con ambos en una licitación pública. En esta obra, el contrato modificatorio (+7,22 %) quedó dentro del límite.

### Quién controla y cómo se paga

La **empresa contratista** construye. Por la UATF, la **Supervisión** controla la calidad y libera los paños, y la **Fiscalización** controla el contrato, las planillas y las modificaciones. Las órdenes quedan escritas en el **Libro de Órdenes**, el cuaderno oficial de la obra. Cada mes, el Supervisor mide la obra con el contratista y aprueba su **planilla de pago**, que solo incluye lo realmente ejecutado (Ministerio de Economía y Finanzas Públicas, 2022).

El precio unitario sale de un **análisis de precios unitarios (APU)**: materiales, mano de obra y equipo, más beneficios sociales, gastos generales, utilidad e impuestos (Cocarico Mamani, 2022). En un APU boliviano documentado, cada boliviano de costo directo se vuelve unos 1,28 bolivianos de precio: el desperdicio encarece también gastos, utilidad e impuestos. Como el precio es fijo, el desperdicio no previsto lo paga la empresa; el riesgo de la UATF es pagar cantidades no ejecutadas o mal medidas. Por eso, comparar planos, consumo y pago (**conciliación de cantidades**) también es un control de la calidad.

Las normas ISO son voluntarias, pero obligan si entran en las especificaciones del contrato. Por eso la tesis propone incluir el plan de la calidad y el PPI al contratar el saldo de la obra.

> **En pocas palabras:** la obra pública tiene reglas fijas: precios unitarios, cambios limitados al 10 %, el 5 % y el 15 %, y pagos solo por lo medido. La Supervisión controla la calidad; la Fiscalización, el contrato y los pagos.

# Capítulo 2. Cómo se hizo el estudio, qué se encontró en la obra y qué se propone

Este capítulo explica cómo se hizo el estudio, describe la obra y su losa, y presenta el diagnóstico de la primera losa, punto de partida del sistema que se propone más adelante.

## El modelo de investigación

La tesis quiere saber si un sistema de gestión de la calidad (SGC) basado en la norma ISO 9001 baja el costo de la losa. Un SGC es un conjunto de reglas escritas, controles y registros que dicen qué revisar, cuándo y quién lo hace. Según la hipótesis general, el sistema reduce al menos en 5 % el costo de cada metro cuadrado de losa, porque se desperdicia menos material y se corrigen menos errores.

El plan original era como la foto del «antes y después» de una remodelación: la primera losa, hecha sin sistema, sería el «antes», y la segunda, con el sistema, el «después». Pero la segunda losa no se construyó. El 5 de enero de 2026, la empresa contratista pidió por carta notariada terminar el contrato por fuerza mayor y paralizar la obra; lo atribuyó al Decreto Supremo 5503, que quitó la subvención a la gasolina y al diésel. La UATF respondió favorablemente el 10 de febrero de 2026.

Por eso se aplicó el plan alternativo que el proyecto de la tesis ya preveía (Tabla 2.1). La **línea base** es el punto de partida contra el que se compara. La **simulación de Monte Carlo** repite el cálculo del costo 20.000 veces con valores posibles distintos de los datos inciertos, como quien lanza un dado muchas veces para ver qué sale más seguido.

**Tabla 2.1.** Las tres piezas del estudio

| Pieza | Qué es | Cómo se obtuvo |
|:--------|:--------------|:------------|
| Línea base («antes») | La primera losa: 41 paños y 1.109,84 m², hechos sin sistema en noviembre y diciembre de 2025 | Con los documentos de la obra |
| Tratamiento | El SGC: plan de la calidad, inspecciones y ensayos, control de materiales, registro de problemas y de costos | Diseñado en la tesis con la guía de la norma ISO 10005 |
| «Después» simulado | El costo de los 2.234,60 m² restantes (segunda y tercera losa), sin y con sistema | Modelo de costos y simulación de Monte Carlo |

La guía del Seminario de Grado acepta la simulación si incluye un tratamiento de control y calcula la incertidumbre (Barrios C., 2021). El control cumple el papel del grupo que no recibe el tratamiento en un experimento (Hernández-Sampieri y Mendoza Torres, 2018), como el que no toma el remedio en la prueba de un medicamento. Aquí, el **escenario de control** repite lo que pasó en la primera losa y el **escenario de tratamiento** aplica el sistema. Ambos usan los mismos paños y los precios del contrato, que no admite reajustes: lo único que cambia es el sistema.

La hipótesis se acepta si el costo baja 5 % o más en al menos 95 de cada 100 escenarios. El estudio es no experimental, porque no se cambió nada en la obra, y su evaluación es *ex ante*, es decir, anticipada.

> **En pocas palabras:** la segunda losa no se construyó. Por eso el «antes» salió de los documentos de la primera losa, y el «después» se calculó en computadora, sin sistema (control) y con sistema.

## La obra y su contrato

El Edificio de Posgrado, de seis niveles, se construye en la Ciudadela Universitaria de la UATF, en Potosí. El contrato abarcaba solo la **obra gruesa** hasta la tercera losa: el «esqueleto» de hormigón armado, con cimientos, columnas, vigas, losas y escaleras (Tabla 2.2).

**Tabla 2.2.** Datos clave de la obra y del contrato

| Dato | Valor |
|:----------|:---------------------|
| Obra | Edificio de Posgrado de la UATF (CUCE 25-0143-00-1531493-1-1), financiado con el Impuesto Directo a los Hidrocarburos |
| Empresa contratista | Constructora Kodesh |
| Firma del contrato | 24 de abril de 2025 |
| Monto | Bs 3.367.031,95; con el contrato modificatorio, Bs 3.610.125,43 (+7,22 %) |
| Plazo | 270 días, ampliado a 360 días (+33,3 %) |
| Losa alivianada (ítem 13) | 3.344,44 m² en tres losas, a Bs 215,68 por m²; su acero se paga por kilo, en el ítem 8 |
| Avance al cierre (planilla firmada, 16/03/2026) | Bs 2.073.392,68 (57,43 %) |

El contrato tiene tres reglas clave: sus precios incluyen la reparación de los trabajos defectuosos y no admiten reajustes, así que el desperdicio lo paga la empresa; la empresa tiene que ensayar los materiales antes de usarlos; y solo se paga la cantidad neta construida. Por la UATF, la **Supervisión** controla la calidad y verifica el trabajo antes de cada vaciado, y la **Fiscalización** controla el contrato y los pagos.

La obra avanzó en plena crisis de combustibles: en junio de 2025, FANCESA paró por un tiempo su producción de cemento por escasez de diésel, y el distribuidor del acero entregó solo el 30 % de un pedido.

> **En pocas palabras:** la UATF contrató el «esqueleto» del edificio. La crisis de combustibles retrasó los materiales y el contrato se cerró con un avance del 57,43 %.

## La losa alivianada de la obra

Como se vio en el Capítulo 1, la **losa alivianada** es un sándwich de 25 cm: abajo, **viguetas pretensadas** hechas en fábrica y colocadas cada 50 cm; en medio, **bloques de plastoformo**; y arriba, una **carpeta** de 5 cm de hormigón vaciado en obra, con una malla de acero de 6 mm cada 20 cm. Ese hormigón debe resistir 250 kg/cm² a los 28 días: cada centímetro cuadrado aguanta 250 kg.

La primera losa tiene 41 **paños**, que son los recuadros de losa rodeados de vigas, como los cuadros de un piso de baldosas grandes. Miden de 1,40 a 52,38 m² y suman 1.109,84 m² (Figura 2.1).

![**Figura 2.1.** Paños de la primera losa (Plano 01). Cómo leerla: es la losa vista desde arriba. Cada recuadro rayado es un paño, con su nombre y su área; el plano usa punto decimal: «A1 = 35.86 M2» son 35,86 m². Las franjas entre paños son las vigas, y los cuadrados negros, las columnas.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/plano01_geometria_primera_losa.png){width=90%}

Los documentos no coinciden en el bloque: las especificaciones técnicas piden piezas de 100 × 50 × 20 cm, se entregaron 2.350 de 20 × 100 × 44 cm y el corte del Plano 02 dibuja un bloque de 15 cm, que daría una losa de 20 cm (Figura 1.4). La tesis considera que el plano tiene un error, porque los demás documentos dicen 25 cm, el mínimo que exige la Norma Boliviana de Diseño Sísmico para que esta losa trabaje como una pieza rígida (MOPSV, 2023). Conviene aclararlo con la Supervisión.

> **En pocas palabras:** la primera losa tiene 41 paños y 1.109,84 m². Los documentos no coinciden en la medida del bloque de plastoformo, algo que conviene aclarar con la Supervisión.

## Qué se midió

Las **variables** son lo que se mide. La causa es el sistema de calidad, y el efecto principal, el **costo unitario**: lo que cuesta hacer un metro cuadrado de losa. También se midieron:

- el **índice de desperdicio** de cada material: cuánto se usó de más frente a los planos (si piden 100 bolsas de cemento y se gastan 110, el desperdicio es de 10 %);
- el **costo de no calidad**: lo que cuesta hacer mal las cosas, es decir, el material desperdiciado y los trabajos rehechos;
- el **costo de la calidad**: lo que cuesta prevenir y revisar, con inspecciones y ensayos;
- la **reducción del costo** por m² que logra el sistema.

El clima, el abastecimiento y la inflación quedan fuera del cálculo; el sistema los trata como riesgos.

> **En pocas palabras:** se midió el costo, el desperdicio y lo que cuesta hacer bien o mal las cosas.

## Qué se estudió: toda la primera losa

No se eligió una muestra: se estudiaron los 41 paños de la primera losa, que son todos los que se construyeron. Es un **censo**, como contar a toda la población en lugar de encuestar a una parte (Hernández-Sampieri y Mendoza Torres, 2018).

Las dos losas restantes suman 2.234,60 m², 1.117,30 m² cada una. El cómputo del contrato, que es su lista de cantidades, las calcula con los mismos 41 paños de la primera; solo cinco áreas son algo mayores. Sus paños son **homólogos**, o «gemelos»: el A1 de la segunda losa ocupa el lugar del A1 de la primera y tiene casi su misma forma. Por eso el modelo les aplica las cantidades por m² de la primera losa.

> **En pocas palabras:** se estudiaron los 41 paños construidos; los de las losas restantes son casi iguales.

## El diagnóstico frente a la norma ISO 9001

El diagnóstico usa solo documentos. Las diferencias de cantidades o pagos son diferencias entre documentos que conviene aclarar con la Supervisión y la Fiscalización, no acusaciones.

Para medir la distancia entre lo hecho y lo que pide la norma se usó una **lista de verificación**, como la que recorre un piloto antes de despegar. El autor la redactó con 50 requisitos basados en las cláusulas 4 a 10 de la norma ISO 9001:2026 (ISO, 2026); 48 se aplican a la losa. Cada uno recibió 1 punto si se cumple, 0,5 si se cumple a medias y 0 si no se cumple o no deja evidencia (Tabla 2.3).

**Tabla 2.3.** Cumplimiento de la norma ISO 9001 en la primera losa

| Cláusula | De qué trata | Requisitos | Cumplimiento |
|:-----------|:---------------|------:|-------:|
| 4. Contexto | Conocer el entorno de la obra | 4 | 25,0 % |
| 5. Liderazgo | Compromiso de quienes dirigen | 5 | 20,0 % |
| 6. Planificación | Prever riesgos y fijar metas | 4 | 12,5 % |
| 7. Apoyo | Personas, recursos y documentos | 10 | 25,0 % |
| 8. Operación | Comprar, recibir y ejecutar con control | 14 | 17,9 % |
| 9. Evaluación | Medir y revisar los resultados | 6 | 25,0 % |
| 10. Mejora | Corregir los errores | 5 | 10,0 % |
| **Global** | | **48** | **19,8 %** |

El cumplimiento global fue de **19,8 %**: ningún requisito se cumplió por completo, 19 se cumplieron a medias y 29 no se cumplieron. Lo más débil fue la mejora (10,0 %), porque no se registraron los problemas ni sus causas, y la planificación (12,5 %), porque no se previeron los riesgos de abastecimiento, precios y clima. Los puntos obtenidos vienen de controles del contrato que funcionaron, como revisar el armado antes de cada vaciado.

Dos fábricas bolivianas de viguetas obtuvieron más (Figura 2.2): 24 % (Mamani Calsina, 2025) y 43 % (Peña Callisaya, 2024). Una fábrica repite sus procesos con personal estable; la losa de una obra pública es un trabajo temporal, controlado casi solo por la Supervisión. La comparación es solo orientativa. Según Peña Callisaya (2024), con 50 % o menos se necesita diseñar un sistema, no solo mejorar prácticas sueltas.

![**Figura 2.2.** Cumplimiento de la norma ISO 9001 por cláusula. Cómo leerla: cada grupo de barras es una cláusula, y el de la derecha, el resultado global. La barra azul es la primera losa; la naranja y la verde, las dos fábricas. Más alta la barra, más se cumple; «n. e.»: no evaluado.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/fig_brechas_iso9001.png){width=90%}

Un 0 indica que el requisito no dejó rastro en los documentos, no necesariamente que la práctica no existió.

> **En pocas palabras:** la obra cumplió el 19,8 % de los requisitos de la norma. Lo más débil fue aprender de los errores y prever los riesgos.

## Las no conformidades y sus causas

Una **no conformidad** es el incumplimiento de un requisito, como un material que llega sin certificado. La obra no las registraba; se reconstruyeron con los documentos y se identificaron 22. El **Libro de Órdenes**, el cuaderno oficial donde la empresa y la Supervisión se comunican, lo muestra: sus 8 solicitudes de vaciado se aprobaron el mismo día y ninguna de sus 24 anotaciones registra un defecto. Eso no prueba que no hubo problemas; solo que no quedó constancia.

Se clasificaron en las **6M**, seis familias de causas (materiales, método, mano de obra, medición, maquinaria y medio ambiente), más una de gestión (Tabla 2.4).

**Tabla 2.4.** Las 22 no conformidades, por tipo

| Tipo | Cantidad | Ejemplos |
|:-------|:----:|:-----------------------------|
| Medición | 6 | Losa sin ensayos de resistencia; calidad calificada de «buena» sin registros; cifras de acero que no coinciden |
| Gestión | 6 | Tres medidas distintas del bloque; ningún problema registrado; riesgos sin prever |
| Materiales | 4 | Certificados tardíos y sin firma; cambio de diseño por escasez de viguetas, sin documento |
| Método | 3 | Sin receta aprobada de la mezcla ni registro del curado (mantener húmedo el hormigón); materiales sin inventario |
| Mano de obra | 2 | Malla pisada durante el vaciado; capacitación sin registrar |
| Medio ambiente | 1 | Sin previsiones para lluvias y frío |

La Figura 2.3 es un **diagrama de Pareto**: ordena los problemas de mayor a menor, porque pocos factores suelen explicar la mayoría de los problemas (Alfaro Félix, 2011). Medición y gestión reúnen 12 de las 22 no conformidades (54,5 %); con materiales y método llegan al 86,4 %.

![**Figura 2.3.** Diagrama de Pareto de las no conformidades. Cómo leerla: cada barra es un tipo, con su cantidad (n) y su porcentaje. La línea naranja va sumando los porcentajes; la línea gris marca el 80 %.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/fig_pareto_nc.png){width=90%}

Un diagrama de **Ishikawa**, o de «espina de pescado», ordenó las causas. Las externas (escasez de combustible y de viguetas, subida de precios y lluvias) se volvieron problemas porque ningún sistema las anticipó: sin plan de compras, se recibieron materiales sin inspección; sin cantidades por paño, el material de más no se detectó; sin ensayos, no se pudo demostrar que el hormigón cumplía. La causa de fondo es la ausencia de un sistema de calidad: la calidad se confió a la revisión de la Supervisión antes de cada vaciado.

> **En pocas palabras:** se hallaron 22 no conformidades, sobre todo en la medición y la gestión. La causa de fondo es la ausencia de un sistema que mida y registre.

## La línea base: cuánto material se usó y cuánto costó

La línea base es el «antes» en números: compara lo que pedían los planos con lo que se entregó y lo que se pagó.

La **cantidad teórica** es lo que la losa necesita según los planos, sin desperdicio. Se calculó paño por paño: se contaron viguetas y bloques, se obtuvo el volumen de hormigón y se sumó el acero. Como ningún plano ubica los nervios (pequeñas vigas que cruzan las viguetas) ni define todas las barras, se usaron supuestos; con ellos, el acero teórico va de 2,72 a 3,44 kg/m² (Tabla 2.5).

**Tabla 2.5.** Cantidades teóricas, entregadas y pagadas de la primera losa

| Material | Según los planos | Entregado o pagado | Diferencia |
|:-------|:----------|:------------|:---------|
| Viguetas | 531 piezas (2.205,1 m) | Sin notas de entrega | Sin dato |
| Plastoformo | 2.237,9 piezas | 2.350 piezas entregadas | +5,01 % |
| Hormigón | 79,31 m³ | Sin remisiones ni vales de cemento | Sin dato |
| Acero | 3.572,8 kg (3,22 kg/m²) | 4.171,18 kg pagados (3,76 kg/m²) | +16,75 % (por aclarar) |

**Plastoformo.** Se entregaron 112 bloques más que los teóricos: un desperdicio de 5,01 %. Sin notas de entrega ni kárdex (la tarjeta de entradas y salidas del almacén), no se sabe cuántos se colocaron ni cuántos sobraron.

**Acero.** Se pagaron 4.171,18 kg, un 16,75 % más que lo teórico; con cualquiera de los supuestos probados, lo pagado es mayor (de +9,2 % a +38,3 %). Los documentos no permiten saber si es desperdicio real, barras que los planos no definen o una medición mayor que lo colocado. Es una diferencia que conviene aclarar con la Supervisión y la Fiscalización; la tesis la usa solo como aproximación del desperdicio.

También conviene aclarar otras diferencias sobre el acero. El cómputo de cierre anota la losa como 3 × 4.171,18 kg = 12.513,54 kg, aunque se construyó una sola; la tesis no usó esa cifra. La planilla de cierre tiene dos versiones: la firmada, que la tesis toma como oficial, descuenta 1.862,81 kg de acero, y la digital, 1.915,16 kg. Y las especificaciones de la losa incluyen su acero, que se pagó en el ítem 8; no se sabe si el precio de la losa ya lo incluía. Esto no prueba un error: muestra que las cantidades se revisaron al cerrar el contrato y no en el mes en que se originaron.

**Hormigón y viguetas.** Sin notas de entrega ni vales de cemento, su desperdicio no se puede medir. Para el hormigón se usó un rango de otras investigaciones, de 5 % a 22 % (Galarza Meza, 2011), con 10 % como valor más probable. Para las viguetas se supuso un desperdicio pequeño por roturas, y para los trabajos rehechos, un 2,34 % del costo directo como valor más probable (Khadim et al., 2023).

### Ninguna probeta de la losa

Una **probeta** es un cilindro de hormigón fresco que se deja endurecer y se rompe en el laboratorio para saber cuánto aguanta. El 28 de noviembre de 2025, la Supervisión autorizó vaciar la losa sin pedir probetas. El único certificado de laboratorio tiene 12 probetas, de columnas y vigas. **Ninguna es de la losa**, aunque el código de hormigón ACI 318-25 pide al menos una muestra por cada 464,5 m² de losa, aproximadamente: tres para la primera losa (ACI Committee 318, 2025). Además, la losa entró en la planilla de pago del 8 de diciembre de 2025, antes de que su hormigón pudiera cumplir 28 días.

### El costo de no calidad

Valorados con precios ajustados al contrato, los materiales teóricos cuestan Bs 182,35 por m², y su desperdicio promedio, con más peso para los más caros, es de 7,47 % (Tabla 2.6). El **costo de no calidad**, que suma el desperdicio en dinero y los trabajos rehechos, se estima en **Bs 19,60 por m²**: el **7,12 %** del costo de un metro cuadrado sin sistema (Bs 275,38). El escenario de control repite este desempeño en las losas restantes, y el Capítulo 3 lo compara con el escenario con sistema.

**Tabla 2.6.** Costo teórico de los materiales y desperdicio más probable sin sistema

| Material | Costo teórico (Bs/m²) | Desperdicio | Origen del dato |
|:-------|---------:|---------:|:-----------|
| Viguetas | 63,08 | 1,00 % | Supuesto del autor |
| Plastoformo | 31,40 | 5,01 % | Documentos de la obra |
| Hormigón | 48,99 | 10,00 % | Otras investigaciones |
| Acero | 38,88 | 16,75 % | Documentos de la obra |
| **Total** | **182,35** | **7,47 %** | Promedio ponderado |

> **En pocas palabras:** llegó 5,01 % más plastoformo del necesario y se pagó 16,75 % más acero que el teórico, una diferencia por aclarar. La losa no tiene probetas. Hacer mal las cosas cuesta, según la estimación, Bs 19,60 por m², el 7,12 % del costo.

## El sistema de gestión de la calidad propuesto

Esta sección presenta la propuesta central de la tesis: el sistema de gestión de la calidad (SGC) para las dos losas restantes. Un SGC funciona como la lista de chequeo de un piloto: dice qué revisar, cuándo, quién lo hace y cómo se deja constancia.

El sistema responde a los nueve problemas, o **brechas**, de la primera losa (41 paños; 1.109,84 m²), como el hormigón sin probetas, los certificados tardíos, las cantidades de acero que no cuadran y los consumos sin registro. Un **paño** es cada recuadro de losa entre vigas.

### Para qué sirve y quién lo aplica

El sistema no busca certificar a una empresa, sino que la segunda y la tercera losa (2.234,60 m²) cumplan los planos con el menor desperdicio. Se concreta en un plan de la calidad, preparado con la norma ISO 10005:2018, y se ordena con los capítulos 4 a 10 de la norma ISO 9001:2026.

Lo aplica la empresa que construya esas losas, porque compra y coloca los materiales. La UATF, por medio de la Supervisión y la Fiscalización, lo exige y lo controla. Por eso la tesis recomienda incluirlo como obligación en la contratación del saldo de la obra.

### El ciclo planificar, hacer, verificar y actuar

El sistema gira en el ciclo **PHVA** (Figura 2.10), como una receta que también dice cómo comprobar que todo salió bien. Se **planifica** (metas, riesgos y capacitación), se **hace** (compra, armado, vaciado y curado), se **verifica** (liberación de paños, conciliación y ensayos) y se **actúa** (corrección de problemas y ajuste de metas). Como las losas restantes repiten la forma de la primera, cada vuelta aprovecha las lecciones de la anterior.

![**Figura 2.10.** El ciclo planificar-hacer-verificar-actuar aplicado a la losa alivianada. Cómo leerla: el ciclo gira en el sentido de las flechas, desde «Planificar» (arriba a la izquierda) hasta «Actuar», que vuelve a empezar. Arriba entran los requisitos de la obra y abajo salen los resultados.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/diagramas/tikz_b1113ccb13014bbbbbe2.png){width=90%}

### El mapa de procesos

Un **proceso** es un grupo de tareas que convierte lo que entra en lo que sale. El mapa de la Figura 2.11 los ordena en tres franjas: los estratégicos dirigen, los operativos construyen y controlan, y los de apoyo sostienen a los demás. El control de cantidades es parte del trabajo diario. Una diferencia descubierta al cerrar el contrato, como la del acero de la primera losa, ya no se corrige a tiempo.

![**Figura 2.11.** Mapa de procesos de la losa alivianada. Cómo leerla: de izquierda a derecha, entran los requisitos (contrato, especificaciones, planos y normas) y sale la losa conforme, con las cantidades conciliadas y pagadas.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/diagramas/tikz_ef0d407eba42c9b93f4d.png){width=90%}

### Quién hace qué

Cada tarea tiene un responsable (Tabla 2.10).

**Tabla 2.10.** Quién hace qué en el sistema

Persona | Papel en el sistema
---------------------------|---------------------------------------------
Director de obra (empresa) | Responde por el sistema y asigna los recursos
Residente de obra | Es el encargado de calidad: inspecciona, registra y concilia
Almacenero | Recibe los materiales, lleva el kardex y entrega con vales
Capataz y armadores | Ejecutan el trabajo y lo revisan ellos mismos
Supervisor de obra (UATF) | Aprueba el plan y libera cada paño
Fiscal de obra (UATF) | Controla el contrato, los pagos y los cambios
Laboratorio | Ensaya las probetas e informa a ambas partes

> **En pocas palabras:** el sistema es la lista de chequeo de la losa. Lo aplica la empresa constructora, lo exige la UATF y cada persona sabe qué le toca.

## El plan de la calidad

El **plan de la calidad** es el manual de la losa: dice qué se controla, con qué criterio, quién responde y qué formulario se llena (Tabla 2.11). Se revisa al cerrar cada losa.

**Tabla 2.11.** Qué contiene el plan de la calidad

Parte del plan | Qué dice para esta obra
------------------|------------------------------------------------------
Alcance | De la compra de los materiales hasta el pago; excluye el diseño estructural y la fabricación de viguetas y plastoformo
Objetivos | Doce metas; por ejemplo, desperdicio máximo de 3 % en el hormigón, 4 % en el acero, 1 % en las viguetas y 3 % en el plastoformo
Documentos | Lista maestra con la versión vigente de cada plano y formato
Recursos | Personal con tiempo asignado, almacén, equipos y tres charlas de 2 horas
Comunicación | Libro de Órdenes con todas las firmas, reunión semanal e informe mensual
Controles | Recepción de materiales, PPI, control del hormigón y auditorías internas

El plan se apoya en una **política de la calidad** de seis compromisos; el primero es ejecutar cada paño según los planos y no vaciar ninguno sin liberar. El sistema también identifica 14 **riesgos**, como la escasez de cemento o las heladas, cada uno con su respuesta.

Un ejemplo: el bloque de plastoformo mide 20 cm de alto en la especificación técnica y en el certificado, pero 15 cm en el Plano 02. El plan exige que el proyectista y la Supervisión definan la medida y corrijan el plano antes de comprar.

> **En pocas palabras:** el plan es el manual de la losa: metas, riesgos, documentos y responsables. Su regla de oro: ningún paño se vacía sin estar liberado.

## El plan de puntos de inspección y ensayo de cada paño

El **plan de puntos de inspección y ensayo (PPI)** reúne los 14 controles de cada paño (Tabla 2.12). En un **punto de espera (H)**, como ante un semáforo en rojo, el trabajo no sigue hasta que la Supervisión revisa y firma. En un **punto de aviso (W)**, se avisa a la Supervisión. En una **revisión (R)**, se revisan certificados o informes. El **apuntalamiento** son los puntales que sostienen las viguetas; los **nervios**, pequeñas vigas de hormigón que las cruzan; los **negativos**, fierros sobre los apoyos, y el **vaciado**, el llenado con hormigón.

**Tabla 2.12.** Controles de cada paño antes, durante y después del vaciado

Cuándo | Control | Qué se revisa | Tipo
---------|-------------------|------------------------------------------|----
Antes | 1. Recepción | Material aceptado, con su certificado | R
Antes | 2. Encofrado de vigas | Ejes y niveles según el Plano 01 | W
Antes | 3. Apuntalamiento | Puntales cada 0,80 a 1,00 m, firmes y unidos en cruz | **H**
Antes | 4. Viguetas | Tipo, número y largo según el Plano 03; sin fisuras | W
Antes | 5. Plastoformo | Piezas enteras y ajustadas | W
Antes | 6. Fierro | Malla de 6 mm cada 20 cm, nervios y negativos; separadores que levantan la malla | **H**
Antes | 7. Instalaciones | Tubos sin cortar viguetas ni nervios | W
Antes | 8. Liberación | Todo conforme; mezcla aprobada; sin lluvia prevista | **H**
Durante | 9. Vaciado | Prueba del cono, temperaturas y vibrado | W
Durante | 10. Probetas | Muestras al azar, marcadas con su paño | W
Después | 11. Curado | Hormigón húmedo al menos 7 días | W
Después | 12. Resistencia | Ensayos a 28 días aceptados | R
Después | 13. Retiro de puntales | Al menos 15 o 21 días, según la distancia entre apoyos | **H**
Después | 14. Conciliación | Consumos del paño dentro de las metas | R

En la primera losa, el vaciado se autorizó el mismo día en que se pidió, sin pedir probetas, y las fotos muestran la malla pisada. Con el PPI, cada paño se libera por escrito y se paga solo con ensayos conformes y cantidades conciliadas. Si los ensayos aún no llegan, la tesis recomienda pagarlo con una retención.

> **En pocas palabras:** cada paño pasa por 14 controles. En cuatro de ellos, el trabajo se detiene hasta que la Supervisión firma.

## Los cinco procedimientos de control de materiales

Un **procedimiento** es una receta escrita de pasos. Los cinco procedimientos de control de materiales (PCM) siguen al material desde que llega hasta que se paga.

### PCM-01: recibir por lotes, antes de usar

Un **lote** es un grupo de piezas fabricadas juntas, con un mismo certificado; en el acero se llama **colada**. En la primera losa, los certificados de las viguetas y del plastoformo no tienen firma y son posteriores al inicio del armado. El PCM-01 invierte ese orden: primero se revisa (Tabla 2.13) y solo lo aceptado se coloca.

**Tabla 2.13.** Qué se revisa al recibir cada material

Material | Qué se revisa | Se acepta si…
-------------|-----------------------------------|----------------------------------------
Viguetas | Certificado con lote; se miden cinco por entrega | Largo según el Plano 03 (+30/−20 mm), sin fisuras; con más de 2 defectos principales o 4 secundarios, se rechaza el lote
Plastoformo | Certificado con lote; se miden y pesan cinco piezas | Medida aprobada, densidad de 10 kg/m³ o más y piezas enteras
Acero | Certificado de cada colada y diámetro; se pesan tres barras | Al menos 94 % del peso nominal, sin óxido suelto
Cemento | Guía con fecha y sello IBNORCA | Bolsas intactas, sin grumos
Arena, grava y agua | Origen conocido; se mide cada volquete | Limpias; agua a más de 5 °C

### PCM-02: guardar e identificar

Cada material se guarda según su tipo; por ejemplo, el cemento, techado y en pilas de hasta 10 bolsas. Cada lote lleva una tarjeta de semáforo: verde (aceptado), amarillo (retenido) o rojo (rechazado). El **kardex** registra entradas, salidas y saldo, como la libreta de una cuenta de ahorro, y cada semana se compara con lo que hay en el almacén.

### PCM-03: entregar por paño y medir el consumo

Antes de cada paño se calcula la **cantidad teórica** de cada material. El Almacenero entrega solo con un **vale** firmado, y lo que sobra vuelve con un vale de devolución. Dos controles pesan mucho en el costo:

- **Despiece del acero:** la lista de cada barra por cortar, con su diámetro, largo y forma, para aprovechar los recortes. En dos edificaciones, el despiece y el prearmado bajaron el desperdicio de acero de 14,58 % a 8,94 % y de 17,09 % a 6,71 % (Chino Quispe y Zarate Chilqquetuma, 2024).
- **Control del volumen del hormigón:** en cada vaciado se anotan los **pastones** (las cargas de la mezcladora) y las bolsas de cemento. Los pastones por el rendimiento de la mezcla dan el volumen producido.

El **índice de desperdicio** compara lo colocado con lo teórico. En la primera losa se entregaron 2.350 piezas de plastoformo para 2.237,9 teóricas, un 5,01 % más, sin registro de cuántas se colocaron.

### PCM-04: conciliar las cantidades

**Conciliar** es comparar varias cuentas de lo mismo, como cuadrar la caja de una tienda cada día. En cada paño se comparan cinco cantidades: la teórica (planos), la entregada (remisiones), la colocada (vales), la medida (con la Supervisión) y la pagada (planilla). Si una diferencia pasa su umbral, como 5 % en el acero por m², se abre una no conformidad y ese ítem no se cobra hasta aclararlo. La Tabla 2.14 aplica estos controles, hacia atrás, a la primera losa.

**Tabla 2.14.** Lo que la conciliación habría detectado en el acero de la primera losa

Control | Lo que dicen los documentos | Alerta
--------------|-----------------------------------------------|---------------------
Acero por m² | Planilla N.º 2: 4.171,18 kg para 1.109,84 m² (3,76 kg/m²); cómputo de cierre: 3 × 4.171,18 = 12.513,54 kg (11,28 kg/m²) | El triple: aclarar el factor 3
Pago frente a medición | De 52.424,65 kg pagados, al cierre se descontaron 1.862,81 kg (planilla firmada) o 1.915,16 kg (versión digital) | Conciliar en cada planilla
Coherencia | Cuatro cifras de acero acumulado: 52.424,65; 50.509,49; 50.509,23 y 50.561,84 kg | Un registro único
Ítem de pago | Acero pagado en el ítem 8; la especificación del ítem 13 incluye la malla | Posible doble cómputo

Las alertas habrían saltado en el mes en que nació cada diferencia. No prueban un error: son inconsistencias documentales que deben verificar la Supervisión y la Fiscalización.

### PCM-05: separar el material defectuoso

El material rechazado lleva una tarjeta roja de «no usar» y se separa. Luego se devuelve, se usa en algo menor con aprobación, se acepta por escrito o se descarta. Una vigueta fisurada nunca se coloca.

> **En pocas palabras:** el material se revisa al llegar, se entrega con vale y se concilia antes de cobrar. Así se paga solo lo que corresponde.

## Qué pasa cuando algo sale mal: las no conformidades

Una **no conformidad** es el incumplimiento de un plano, de la especificación, del PPI o del contrato. Puede ser **crítica** (afecta a la seguridad, o un paño se vació sin liberar), **mayor** (afecta a la calidad, las cantidades o el costo) o **menor** (solo de papeles). Se registra en 24 horas y se cierra en 7 días o menos, en siete pasos (Figura 2.12).

Corregir no es eliminar la causa. Ante una gotera, secar el piso es la corrección; arreglar el techo, la acción correctiva. La causa se busca con los **5 porqués**: se pregunta «¿por qué?» hasta llegar al fondo. En la primera losa no hubo probetas porque nadie tenía esa tarea ni había un plan de muestreo, y no lo había porque no se exigió un plan de la calidad. La acción correctiva es el plan de muestreo con responsables.

Si un paño vaciado tiene un defecto, como nidos de grava (huecos en el hormigón), la Supervisión decide si se repara, se refuerza, se demuele o se acepta por escrito, y su pago se retiene. En la primera losa, ninguna de las 24 anotaciones del Libro de Órdenes registró un problema.

![**Figura 2.12.** Flujo del procedimiento de no conformidades. Cómo leerla: se baja paso a paso, desde la detección hasta el cierre; a la derecha figura quién actúa y en qué plazo. Si la acción no funcionó, la flecha «No» vuelve al análisis de la causa.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/diagramas/tikz_d2b305aed1f48392c842.png){width=90%}

> **En pocas palabras:** cada problema se anota en 24 horas, se corrige, se elimina su causa y se cierra en 7 días o menos.

## El control del hormigón y el clima de Potosí

El hormigón de la losa es **H25**: debe resistir al menos 250 kg por cm² a los 28 días. Su control sigue el código ACI 318-25, base de la norma boliviana NB 1225001-1:2017.

- **Mezcla.** La **dosificación**, o receta del hormigón, se aprueba antes del primer vaciado. La prueba del **cono de Abrams** muestra si el hormigón fresco tiene demasiada agua.
- **Probetas.** Una **probeta** es un cilindro de 15 × 30 cm de hormigón fresco que se rompe en el laboratorio. Cada ensayo promedia dos probetas rotas a los 28 días, tomadas al azar.
- **Cantidad.** Entre otras reglas, el código pide un ensayo por cada 464,5 m² de losa: 3 en una losa de 1.117,30 m². El sistema exige **5 por losa**.
- **Aceptación.** Todo promedio de tres ensayos seguidos debe llegar a 250 kg/cm², y ningún ensayo puede bajar de unos 215 kg/cm². No valen resistencias «proyectadas» desde otras edades. Si un ensayo sale bajo, se extraen **núcleos**, cilindros cortados de la losa endurecida.

**El clima.** A 3.650 m s. n. m. hay lluvias y heladas; entre septiembre y noviembre de 2025 se notificaron siete días de lluvia. Por eso el hormigón se **cura**: se mantiene húmedo al menos 7 días a 10 °C o más, como se riega una planta recién sembrada. La empresa presenta un **plan de tiempo frío**: bajo 4,4 °C se registra la temperatura del hormigón, y el agua de la mezcla debe superar los 5 °C. Los vaciados se programan con el pronóstico del SENAMHI.

> **En pocas palabras:** cada losa tendrá al menos 5 ensayos de su propio hormigón, rotos a los 28 días, y protección contra el frío y la lluvia de Potosí.

## El registro de los costos de la calidad

El sistema anota los costos con el **modelo PAF**, de prevención, evaluación y fallas (Tabla 2.15). Es como el mantenimiento de un auto: se paga el cambio de aceite para no pagar después un motor fundido.

**Tabla 2.15.** Los cuatro tipos de costos de la calidad en la losa

Tipo | Ejemplos en la losa
--------------------------------|------------------------------------------
Prevención: evitar errores | Plan de la calidad, despiece del acero, charlas, plan de tiempo frío
Evaluación: revisar | Ensayos, inspecciones, inventarios y conciliación
Fallas internas: antes de entregar | Desperdicio, trabajos rehechos, viguetas rotas, esperas
Fallas externas: después de entregar o pagar | Cantidades corregidas después de pagadas, reparaciones, multas

Prevenir y evaluar es el **costo de la calidad**; las fallas son el **costo de no calidad**. Todo se valora con los precios fijos del contrato y se resume por mes y por losa en la planilla C.6. El sistema baja el costo solo si lo que reduce en fallas supera lo que gasta en prevenir y evaluar.

> **En pocas palabras:** el sistema conviene si los errores que evita valen más que su propio costo.

## Formatos e instrumentos

Cada control deja huella en un formulario sencillo, archivado por losa y por paño (Tabla 2.16).

**Tabla 2.16.** Formatos e instrumentos del sistema

Código | Formato | Uso
------|-----------------------------|-----------------------------------
C.1 | Lista de verificación ISO 9001:2026 | Diagnóstico y auditoría interna
C.2 | Ficha de liberación del paño | Una por paño, con las firmas
C.3 | Ficha de recepción | Una por entrega de material
C.4 | Control de materiales | Vales, kardex y conciliación
C.5 | Registro de no conformidades | Uno por problema, con su costo
C.6 | Planilla de costos de la calidad | Una por mes y una por losa
C.7 | Guía de entrevista | Diagnóstico de la investigación
C.8 | Validación por expertos | Calificación del sistema

Los equipos de medición son sencillos: cono de Abrams, moldes, termómetros, balanza, flexómetro y cajones dosificadores calibrados. Cada paño se compara con su **paño homólogo**, el de igual forma en la losa anterior. Hay una reunión semanal de calidad, una revisión mensual con la Supervisión y la Fiscalización, y dos auditorías internas por losa.

> **En pocas palabras:** cada control queda en un registro firmado que cualquiera puede revisar.

## Cuánto cuesta el sistema y quién lo paga

La Tabla 2.17 muestra el costo estimado del sistema: mínimo, más probable y máximo.

**Tabla 2.17.** Costo del sistema en las dos losas restantes

Componente | Mínimo (Bs) | Más probable (Bs) | Máximo (Bs)
------------------------------------|--------|--------|--------
Encargado de calidad a tiempo parcial (3 meses) | 4.000 | 6.750 | 13.500
Ensayos del hormigón | 720 | 1.200 | 1.920
Capacitación (tres charlas) | 1.000 | 1.700 | 5.874
Control del almacén y conciliación | 500 | 820 | 1.500
Formatos e impresión | 200 | 400 | 1.000
**Suma de los valores más probables** | | **10.870** |

Con los valores más probables, el sistema cuesta Bs 10.870, es decir, **Bs 4,86 por m²** de los 2.234,60 m² restantes: el 1,79 % del costo por metro cuadrado. En la simulación, con la incertidumbre de cada parte, el costo medio fue de Bs 6,11 por m².

**Quién lo paga.** El costo recae en la empresa constructora, que aplica el sistema. El contrato pone los ensayos a su cargo, no reajusta los precios e incluye en ellos la reparación de los trabajos defectuosos. Por eso la empresa es también la principal beneficiada si bajan las fallas, y la UATF gana una losa con calidad demostrada y pagos correctos. Como el costo del sistema es el dato que más pesa en el resultado (Capítulo 3), la tesis recomienda un sistema «ligero»: con el personal que ya existe y centrado en el volumen del hormigón, el despiece del acero, la recepción por lotes y la conciliación de cantidades.

> **En pocas palabras:** el sistema cuesta unos Bs 4,86 por m² y lo paga la empresa constructora, que también gana si bajan las fallas.

## Cómo se evaluó el sistema sin construir la segunda losa

El sistema de gestión de la calidad (SGC) se diseñó para la segunda y la tercera losa, cuyos paños son «gemelos» de los de la primera.

### Cómo se aplicaría el sistema en el saldo de la obra

En cada losa, el sistema seguiría siete etapas, y cada una dejaría un registro escrito (Tabla 2.20).

**Tabla 2.20.** Etapas del sistema en cada losa

| Etapa | Qué se hace | Registro |
|---|---|---|
| 0. Preparación | Se aprueba el plan de la calidad y se capacita al personal | Acta; lista de asistencia |
| 1. Abastecimiento | Se pide el material por paño y se revisa antes de aceptarlo | Ficha de recepción; registro de almacén |
| 2. Armado | El trabajo se detiene en puntos de espera hasta que la Supervisión firma | Fichas de inspección |
| 3. Hormigonado | Se controla la mezcla, se toman probetas y se cura el hormigón (se mantiene húmedo) | Planillas de hormigonado y de muestreo |
| 4. Consumos | Se comparan las cantidades de los planos, entregadas, colocadas, medidas y pagadas | Ficha de control de materiales |
| 5. Verificación | Las probetas se rompen a los 28 días para medir la resistencia; cada problema se corrige | Certificados; registro de no conformidades |
| 6. Revisión | Cada semana se revisan indicadores y costos de la calidad | Planilla de costos de la calidad |

Esta secuencia no pudo aplicarse: el 5 de enero de 2026 la contratista pidió paralizar la obra y resolver el contrato, la UATF respondió favorablemente el 10 de febrero y el saldo no se contrató durante el estudio. Por eso, como preveía el diseño de la investigación, el efecto se evaluó *ex ante* (antes de que ocurra), con un modelo de costos y una simulación.

### El modelo de costos: una receta de tres partes

Como pide la guía del Seminario de Grado, el modelo tiene un escenario de control y mide la incertidumbre. Compara el costo de los 2.234,60 m² restantes **sin SGC** (control: como la primera losa) y **con SGC** (tratamiento), como un ensayo de un medicamento, con esta receta:

**Costo de 1 m² = lo que piden los planos + lo que se pierde o se rehace + lo que cuesta controlar**

- **Lo que piden los planos** (costo directo teórico): construir con las cantidades exactas, sin perder nada.
- **Lo que se pierde o se rehace** (costo de no calidad): el material usado de más, por su precio, y los trabajos rehechos (retrabajos). El material de más se mide con el **índice de desperdicio (IDM)**: si los planos piden 100 bloques y se usan 105, el IDM es de 5 %.
- **Lo que cuesta controlar** (costo de la calidad): encargado de calidad, ensayos, capacitación, almacén y formularios. Sin sistema vale cero, porque en la primera losa no se registró ese gasto.

El sistema reduce el desperdicio y los retrabajos en un porcentaje llamado **eficacia** (con 44 %, un desperdicio de 10 % baja a 5,6 %), pero agrega su propio costo. El resultado clave es la **reducción del costo de 1 m²**: de Bs 100 a Bs 98 sería de 2 %. Todo va a precios constantes del contrato, para que la subida de precios no se confunda con el efecto del sistema.

### El precio de referencia y su calibración

El análisis de precios unitarios (APU) del contrato desglosa el precio de 1 m², como la lista de ingredientes de una receta con sus precios, pero no estaba disponible. La tesis reconstruyó uno de referencia con las cantidades de los planos y precios bolivianos publicados, y lo ajustó al contrato con un **factor de calibración (κ)**: el precio del contrato dividido entre el reconstruido. Resultó de 0,962 para la losa y de 1,129 para el acero; un valor cercano a 1 indica una reconstrucción coherente.

El contrato paga Bs 278,65 por m² de losa: Bs 215,68 del ítem de la losa y Bs 62,98 de su acero, pagado en otro ítem. El modelo supone que ese precio refleja la forma habitual de trabajar, con sus desperdicios, y ajusta la primera parte de la receta para que el costo promedio sin sistema sea igual a él. Así, lo que piden los planos resultó de Bs 255,78 por m².

### La simulación de Monte Carlo: tirar los dados 20.000 veces

Muchos datos son inciertos. Para cada uno se fijaron un mínimo, un valor más probable y un máximo (una **distribución triangular**), como el maestro de obra que dice: «mínimo dos días, lo normal tres, como mucho cinco». Esos rangos salen de la primera losa y de otros estudios. Con los valores más probables, el sistema cuesta Bs 4,86 por m².

Luego la computadora «tiró los dados» 20.000 veces: en cada tirada eligió al azar un valor de cada dato y calculó el costo sin sistema y con sistema. Así obtuvo 20.000 futuros posibles, o **escenarios**. La probabilidad de algo es la proporción de escenarios en que ocurre: 10.000 de 20.000 es 0,50, es decir, 50 de cada 100. Una **semilla** fija (2026) permite repetir las mismas tiradas. Como la certificación no garantiza que la calidad se cumpla en obra (Romero y Serpell, 2007), también se simuló un sistema «de papel», que en el 15 % de los casos se paga pero no se aplica.

> **En pocas palabras:** sin segunda losa, el sistema se evaluó en la computadora, con la receta del costo de 1 m² y 20.000 tiradas de dados, sin sistema y con él.

## Cómo se comprobó que la evaluación es confiable

Cada cantidad de la primera losa se contrastó en al menos dos documentos, como un periodista que confirma una noticia con dos fuentes. El modelo reprodujo la cuenta hecha a mano, y 20.000 tiradas bastaron: el margen de error del promedio (error estándar) fue de 0,0070 %. Además, se midió qué datos mueven más el resultado (sensibilidad).

La tesis deja diseñada, además, una **validación por juicio de expertos**, como el jurado de una feria de ciencias: al menos tres ingenieros civiles con experiencia en supervisión, hormigón o gestión de la calidad califican de 1 a 4, en el formulario C.8, 22 componentes del sistema según su pertinencia, claridad, suficiencia y aplicabilidad. Las notas se resumen con el **coeficiente V de Aiken**, que va de 0 (todos dan la nota mínima) a 1 (todos dan la máxima). Un componente se acepta con V de 0,70 o más, y los demás se corrigen. Este procedimiento no se aplicó durante el estudio, así que esta edición no reporta resultados de expertos.

> **En pocas palabras:** los datos se cruzaron entre documentos y el resultado es estable. El juicio de expertos quedó diseñado, con su criterio de 0,70, pero no se aplicó.

## Cómo se decide: la regla del 95 %

La **hipótesis de investigación (H1)** es lo que se quiere demostrar; la **hipótesis nula (H0)** afirma lo contrario y se mantiene mientras no haya pruebas suficientes, como la presunción de inocencia. La regla, fijada antes de calcular, acepta H1 solo si se cumple en al menos 95 de cada 100 escenarios, es decir, con una probabilidad de 0,95 o más (Tabla 2.21). Equivale al nivel de significancia habitual de 0,05: aceptar como máximo 5 posibilidades en 100 de dar por cierto algo falso.

**Tabla 2.21.** Hipótesis y reglas de decisión

| Qué afirma H1 | Se acepta si, en al menos 95 de cada 100 escenarios… |
|---|---|
| General (HG): el costo de 1 m² baja 5 % o más | la reducción llega al 5 % |
| Específica 1 (HE1): baja el desperdicio, ponderado por el costo de cada material | el desperdicio con sistema es menor |
| Específica 2 (HE2): baja el costo de no calidad | ese costo con sistema es menor |

También se calculan la **probabilidad de ahorro** (que el costo baje), el ahorro esperado y el **punto de equilibrio**: la eficacia mínima para no perder dinero.

### La comprobación con datos medidos en obra

Cuando se ejecute el saldo, las cifras se comprobarán con datos reales: los formularios registrarán el consumo y el costo de la calidad de cada paño, que se comparará con su gemelo de la primera losa mediante la prueba t de Student para muestras relacionadas, como quien pesa a las mismas personas antes y después de una dieta. Si las diferencias no tienen forma de campana (prueba de Shapiro-Wilk), se usará la prueba de Wilcoxon, con un nivel de significancia de 0,05.

> **En pocas palabras:** cada hipótesis se acepta solo si se cumple en al menos 95 de cada 100 escenarios, y las cifras se comprobarán paño por paño cuando se construya el saldo.

# Capítulo 3. Resultados: qué se encontró y qué significa

Todas las cifras están a precios constantes del contrato.

## Lo que mostró el diagnóstico

La primera losa cumplió el 19,8 % de los 48 requisitos aplicables de la norma ISO 9001:2026, y ninguno de forma plena. De sus 22 no conformidades, es decir, incumplimientos de un requisito, el 54,5 % estaba en la medición y la gestión. La causa de fondo fue la ausencia de un sistema: el control se confió a la revisión de la Supervisión antes de cada vaciado, sin criterios escritos ni registros. La losa se certificó para pago sin ninguna probeta de su hormigón, y el acero acumulado del ítem 8 tiene cuatro cifras distintas.

> **En pocas palabras:** la primera losa se hizo sin registros que probaran su calidad ni respaldaran las cantidades pagadas.

## La línea base: cuánto se perdía sin sistema

La **línea base** es la foto del «antes». Solo dos materiales tuvieron un dato documental. Del plastoformo se entregaron 2.350 piezas frente a 2.237,9 según los planos: un desperdicio de 5,01 %. Del acero se pagaron 4.171,18 kg, 3,76 kg por m², un 16,75 % más que lo teórico. Como esta cifra es lo pagado y no lo consumido, se usó solo como aproximación: también puede reflejar una medición mayor que lo ejecutado o armaduras que los planos no definen. Para las viguetas y el hormigón no hubo registros, y se adoptaron 1,00 % (supuesto del autor) y 10,00 % (otros estudios) (Tabla 3.1).

**Tabla 3.1.** Desperdicio por material con los valores más probables

| Material | Sin sistema | Eficacia del sistema | Con sistema |
|---|---|---|---|
| Viguetas | 1,00 % | 44 % | 0,56 % |
| Plastoformo | 5,01 % | 44 % | 2,81 % |
| Hormigón | 10,00 % | 44 % | 5,60 % |
| Acero | 16,75 % | 42 % | 9,72 % |

Con los valores más probables, el desperdicio ponderado por costo fue de 7,47 %, y el **costo de no calidad**, de Bs 19,60 por m²: el 7,12 % del costo sin sistema (Figura 3.1). Para el plastoformo no se hallaron valores de referencia en otros estudios: el 5,01 % es un primer dato documental.

![**Figura 3.1.** Costo de no calidad por componente (valores más probables). Cómo leerla: en cada par, la barra gris es el costo sin sistema y la azul, con sistema, en bolivianos por m². Las mayores pérdidas están en el acero, los retrabajos y el hormigón, y todas las azules son más bajas.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/fig_cnc_por_componente.png){width=90%}

> **En pocas palabras:** sin sistema, cada m² perdía Bs 19,60 en material desperdiciado y trabajos rehechos: el 7,12 % de su costo.

## El resultado con los valores más probables

Con el valor más probable de cada dato, el costo de 1 m² bajó de Bs 275,38 a Bs 271,46: una reducción de 1,43 %, que en los 2.234,60 m² del saldo equivale a Bs 8.780 (Tabla 3.2).

**Tabla 3.2.** Costo de 1 m² con los valores más probables (Bs por m²)

| Parte de la receta | Sin sistema | Con sistema |
|---|---|---|
| Lo que piden los planos | 255,78 | 255,78 |
| Lo que se pierde o se rehace | 19,60 | 10,81 |
| Lo que cuesta controlar | 0,00 | 4,86 |
| **Costo de 1 m²** | **275,38** | **271,46** |

> **En pocas palabras:** en el caso más probable, el sistema baja el costo de 1 m² en 1,43 % y ahorra Bs 8.780, ya descontado su propio costo.

## Lo que mostraron los 20.000 escenarios

El costo promedio de 1 m² fue de Bs 278,59 sin sistema, casi igual al precio del contrato, y de Bs 274,48 con sistema (Tabla 3.3 y Figura 3.3). La reducción promedio fue de 1,47 %. El costo de no calidad bajó en promedio 44,82 %, con un costo del sistema de Bs 6,11 por m², y el desperdicio ponderado, de 8,16 % a 4,70 %.

**Tabla 3.3.** Resultados de los 20.000 escenarios

| Indicador | Promedio | Límite bajo (P5) | Límite alto (P95) |
|---|---|---|---|
| Costo de 1 m² sin sistema (Bs) | 278,59 | 272,38 | 285,35 |
| Costo de 1 m² con sistema (Bs) | 274,48 | 269,95 | 279,73 |
| Reducción del costo de 1 m² | 1,47 % | −0,05 % | 3,21 % |
| Costo de no calidad sin sistema (Bs/m²) | 22,80 | 16,60 | 29,57 |
| Costo de no calidad con sistema (Bs/m²) | 12,58 | 8,42 | 17,60 |
| Ahorro en el saldo (Bs) | 9.177 | −328 | 20.328 |

*Nota:* el 90 % central de los escenarios queda entre P5 y P95. Un ahorro negativo significa que el sistema costó más de lo que ahorró.

![**Figura 3.2.** Reducción del costo de 1 m² en los 20.000 escenarios. Cómo leerla: cada barra cuenta los escenarios de un tramo de reducción. La línea negra es el promedio (1,47 %) y la anaranjada discontinua, la meta del 5 %. Casi todas quedan a la derecha del cero (con ahorro) y casi ninguna cerca de la meta.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/fig_histograma_reduccion.png){width=90%}

![**Figura 3.3.** Costo de 1 m² sin sistema y con sistema (distribución acumulada). Cómo leerla: se elige un costo abajo y se sube hasta la curva; la altura indica qué parte de los escenarios cuesta eso o menos. La curva azul (con sistema) queda siempre a la izquierda de la gris: cuesta menos en cada nivel de probabilidad. La línea punteada es el precio del contrato.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/fig_acumulada_costo_unitario.png){width=90%}

![**Figura 3.4.** Promedio de la reducción según el número de tiradas. Cómo leerla: la escala de abajo crece de diez en diez veces. El promedio salta al principio y, tras unas mil tiradas, casi no se mueve, cerca de 1,47 %: 20.000 tiradas bastan.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/fig_convergencia.png){width=90%}

> **En pocas palabras:** en promedio, el sistema baja el costo de 1 m² en 1,47 %, reduce casi a la mitad el costo de no calidad y ahorra Bs 9.177 en el saldo, pero casi nunca llega al 5 %.

## La decisión sobre cada hipótesis

La reducción llegó al 5 % solo en 8 de cada 10.000 escenarios (probabilidad de 0,0008), lejos de los 9.500 que exige la regla: la hipótesis general **no se acepta**. La reducción que se alcanza en 95 de cada 100 escenarios fue de −0,05 %, prácticamente nula, aunque el sistema ahorra en 94 de cada 100 (0,9422). La razón está en la receta: el sistema solo actúa sobre el 7,12 % que se pierde o se rehace y cuesta el 1,79 %; aun eliminando todas las pérdidas, la reducción máxima sería de 5,35 %.

En cambio, el desperdicio y el costo de no calidad bajaron en todos los escenarios (probabilidad de 1,0000): **se aceptan HE1 y HE2**. Ocurre porque el modelo da al sistema una eficacia mínima de 10 %; por eso, la aceptación vale solo si el sistema se aplica de verdad.

**Tabla 3.4.** Decisión sobre las hipótesis (regla: probabilidad de 0,95 o más)

| Hipótesis | Probabilidad | Decisión |
|---|---|---|
| General (HG): el costo baja 5 % o más | 0,0008 | No se acepta H1 (se mantiene H0) |
| Específica 1 (HE1): baja el desperdicio | 1,0000 | Se acepta H1 |
| Específica 2 (HE2): baja el costo de no calidad | 1,0000 | Se acepta H1 |

> **En pocas palabras:** la hipótesis general no se acepta; las específicas sí, siempre que el sistema se aplique en obra.

## Qué pesa más en el resultado

Lo que más mueve la reducción es el costo del sistema, la fracción de retrabajo sin sistema y la eficacia sobre los retrabajos; las viguetas y el plastoformo pesan poco (Figura 3.5). Solo el costo máximo del sistema vuelve negativa la reducción (−0,67 %), y ningún dato llega al 5 %: el mejor caso es 3,20 %.

![**Figura 3.5.** Efecto de cada dato sobre la reducción del costo (diagrama de tornado). Cómo leerla: cada barra es un dato; sus extremos dan la reducción con su mínimo y su máximo, y cuanto más larga, más pesa. La línea negra es el caso más probable (1,43 %) y la anaranjada discontinua, la meta del 5 %, que ninguna barra alcanza. En el costo del sistema, el extremo izquierdo es el máximo.](07_Entregables/Explicacion_Para_Todo_Publico/figuras/fig_tornado_sensibilidad.png){width=90%}

**Punto de equilibrio.** Como en un negocio, es el punto en que lo ahorrado iguala lo gastado. Con una eficacia igual para todo, el sistema paga su costo con 24,8 % y llega al 5 % recién con 95,1 % (con eficacia total, 5,35 %); los estudios usados reportan máximos de 70 % a 89 %.

**Otros supuestos.** La simulación se repitió con cinco variantes de los supuestos, y en todas la probabilidad de llegar al 5 % siguió prácticamente nula. Quitar del costo del sistema los ensayos del hormigón, que ya paga la contratista, o suponer más desperdicio de hormigón y acero subieron un poco la reducción media; otra estimación de la mano de obra (Alcón Aranda, 2009) la bajó. Dos variantes cambian el balance: con una eficacia más baja, la reducción media cae a 0,06 % y el sistema ahorra en cerca de la mitad de los escenarios (0,527); con su costo duplicado, la reducción media es de −0,73 % y ahorra en menos de un tercio (0,266).

**Otros escenarios.** Si el sistema se paga pero no se aplica en el 15 % de los escenarios, la reducción media baja a 0,90 %, la probabilidad de ahorro, a 0,7983, y la de HE1 y HE2 queda bajo 0,95. Con los costos ocultos, como demoras y baja productividad (hasta 8,59 % del costo total, según Khadim et al., 2023), la reducción media sube a 3,22 %, pero llegar al 5 % tiene una probabilidad de solo 0,1316.

> **En pocas palabras:** pesan sobre todo el costo del sistema y los retrabajos. El sistema paga su costo con 24,8 % de eficacia, pero el 5 % exigiría 95,1 %.

## El beneficio de conciliar las cantidades

El modelo no mide el control de las cantidades pagadas. Esa es la tarea del procedimiento de conciliación (PCM-04): comparar, antes de cada planilla de pago, las cantidades de los planos, entregadas, colocadas, medidas y pagadas, como quien cuadra la caja cada día. Aplicado a la primera losa y al cierre del contrato, habría alertado sobre las diferencias de la Tabla 3.5, que son inconsistencias documentales que deben verificar la Supervisión y la Fiscalización, no pagos indebidos confirmados.

**Tabla 3.5.** Principales diferencias de cantidades documentadas

| Diferencia | Magnitud | Valor a precio del contrato (Bs) |
|---|---|---|
| Acero de la losa computado como 3 × 4.171,18 kg en el cierre (versión digital), con una sola losa construida | +8.342,36 kg | 139.783,25 |
| Acero de los demás elementos en ese cómputo, sin desglose | −10.257,78 kg | −171.877,72 |
| Versiones firmada y digital de la planilla de cierre | 52,35 kg de acero y la limpieza general | 877,17 y 2.566,96 |
| Acero de la losa pagado en el ítem 8, que la especificación también incluye en el ítem 13 | 4.171,18 kg | 69.891,62 |

*Nota:* las filas no se suman, porque varias se refieren al mismo acero.

Ninguna diferencia se detectó en el mes en que se originó. El control que las habría detectado cuesta, lo más probable, Bs 820 en todo el saldo, y varias de ellas superan por sí solas el ahorro esperado de Bs 9.177.

> **En pocas palabras:** controlar las cantidades pagadas puede valer más que todo el ahorro en materiales.

## La validación por juicio de expertos

El juicio de expertos descrito en el Capítulo 2 no se aplicó durante el estudio, por lo que esta edición no reporta sus resultados. No cambia la decisión sobre las hipótesis, que se basa en el modelo, pero forma parte del quinto objetivo de la tesis.

## Discusión: qué significan los resultados

### Por qué no se llega al 5 %

La meta del 5 % era demasiado alta para un solo ítem. Lo que piden los planos es más del 90 % del costo de 1 m² y no depende del sistema. Es como una panadería que bota 7 de cada 100 panes y gasta casi 2 en vigilar el horno: aunque no perdiera ni uno, ahorraría apenas algo más de 5 de cada 100.

Los estudios con reducciones mayores miden otra cosa. Salazar Retuerto (2018) halló 8,93 % respecto del costo planificado al comparar dos proyectos homólogos, con y sin la guía de gestión PMBOK, pero esa guía actuó sobre todo el proyecto; los reprocesos de 6,59 % de Álvarez Quintero (2014) también se refieren al costo total de los proyectos. En cambio, el 1,47 % se parece a los estudios de un solo material: el despiece del acero (planificar sus cortes) aumentó la utilidad en 1,48 % y 5,87 % (Chino Quispe y Zarate Chilqquetuma, 2024), y la gestión del acero ahorró 3 % y 8 % en dos etapas de una obra, con un exceso de 1 % en la tercera (Galarza Meza, 2011).

### Por qué igual conviene el sistema

- **Reduce casi a la mitad la no calidad**, como en otros estudios: el desperdicio de acero bajó de 7 % a 4,04 % con prearmado (Galarza Meza, 2011) y de 17,09 % a 6,71 % con despiece previo (Chino Quispe y Zarate Chilqquetuma, 2024). La coincidencia se debe en parte a que las eficacias salieron de esos estudios.
- **Probablemente ahorra:** en 94 de cada 100 escenarios, con Bs 9.177 esperados.
- **Su costo es razonable:** 1,79 % del costo, cerca del 1,83 % invertido en prevención y evaluación en 25 proyectos (Khadim et al., 2023) y en el límite bajo de la franja de 2 % a 4 % que recogen Palanisamy y Palanichamy (2025).
- **El resultado es prudente:** no cuenta los costos ocultos, que más que triplican las fallas visibles (Khadim et al., 2023), ni el control de las cantidades pagadas.
- **Para la UATF**, buena parte del beneficio está en comprobar el hormigón y pagar las cantidades correctas, más que en el costo de construir, que asume la contratista.

El margen es estrecho, como hallaron Gudiel Cairampoma y Solis Puente (2020), y los beneficios de la norma ISO 9001 llegan de forma gradual (Prado-Román et al., 2018). Por eso la tesis recomienda un **sistema ligero**: con el personal existente y pocos controles de alto impacto, como el volumen de hormigón, el despiece del acero, la recepción por lotes y la conciliación de cantidades.

### Límites y alcance

La evaluación fue *ex ante*, con una sola obra, y solo el plastoformo y el acero tuvieron datos documentales. Además, el APU se reconstruyó, los datos se sortearon por separado, no se incluyeron los costos de plazo y el diagnóstico fue documental, sin entrevistas ni juicio de expertos. Aun así, la decisión sobre la hipótesis general es sólida: el 5 % exige una eficacia cercana al 100 %, y ninguna variante se acercó a 0,95. Las magnitudes se comprobarán con datos de obra cuando se ejecute el saldo, y el método sirve para otras obras.

> **En pocas palabras:** el 5 % era una meta demasiado alta para un solo ítem. Pero el sistema probablemente ahorra, reduce casi a la mitad las pérdidas y permite comprobar el hormigón y pagar lo correcto. Conviene aplicarlo, ligero y de verdad.

# Conclusiones y recomendaciones

## Conclusión general

La tesis se preguntó si un sistema de gestión de la calidad (SGC) basado en la ISO 9001 y centrado en el control de materiales permite bajar el costo de las losas alivianadas del Edificio de Posgrado. Se estudió con documentos la primera losa y se simuló el costo de los 2.234,60 m² restantes.

La respuesta es sí, pero menos de lo esperado. El SGC reduce el desperdicio y los retrabajos, que forman el costo de no calidad, y controla las cantidades que se pagan. El costo por m² bajó en promedio 1,47 %, de Bs 278,59 a Bs 274,48, con una probabilidad de 0,9422 de que baje. El costo de no calidad bajó 44,82 %. El ahorro esperado en el saldo es de Bs 9.177; en 90 de cada 100 escenarios, va de una pérdida de Bs 328 a un ahorro de Bs 20.328.

La hipótesis general, una reducción de al menos 5 %, no se acepta: su probabilidad fue de 0,0008, lejos del 0,95 exigido. El SGC solo actúa sobre el costo de no calidad, el 7,12 % del costo por m², y cuesta el 1,79 %. Aun con una eficacia del 100 %, la reducción sería de 5,35 %, y llegar al 5 % exigiría una eficacia de 95,1 %, mayor que la reportada en otros estudios. Las hipótesis específicas sí se aceptan: el SGC reduce el desperdicio (HE1) y el costo de no calidad (HE2), si se aplica de verdad en la obra.

> **En pocas palabras:** el sistema ahorra, pero poco. Para la UATF, una parte importante del beneficio está en comprobar que el hormigón cumple y en pagar solo lo correcto.

## Conclusiones por objetivo

### Objetivo 1: calidad en la primera losa

La primera losa se hizo sin SGC y cumplió el 19,8 % de los requisitos de la ISO 9001:2026, con todas las cláusulas en nivel deficiente; las más débiles, la mejora (10,0 %) y la planificación (12,5 %). Hubo 22 no conformidades, el 54,5 % en la medición y la gestión: la losa se aprobó para el pago sin ensayos de su hormigón, los certificados de viguetas y plastoformo son posteriores al inicio del armado y no se registraron consumos ni problemas. El acero muestra diferencias entre documentos que conviene aclarar con la Supervisión y la Fiscalización. La causa de fondo: la calidad dependió de una revisión de la Supervisión antes de cada vaciado, sin criterios escritos, registros ni seguimiento.

### Objetivo 2: desperdicio y costo de no calidad

Solo dos materiales tenían datos documentales. Del plastoformo se entregaron 2.350 piezas frente a 2.237,9 teóricas: 5,01 % de desperdicio. Del acero se pagó 16,75 % más que lo teórico; es una aproximación, no un consumo medido. Para el hormigón y las viguetas se usaron valores de otros estudios. Con los valores más probables, el desperdicio ponderado por costo fue de 7,47 % y el costo de no calidad, de Bs 19,60 por m² (7,12 % del costo por m²); con la incertidumbre, su promedio fue de Bs 22,80. El acero, los retrabajos y el hormigón pesan más. Sin registros de consumo, el desperdicio no podía conocerse ni controlarse.

### Objetivo 3: las piezas del sistema

El SGC sigue las cláusulas 4 a 10 de la ISO 9001:2026 y se concreta en un plan de la calidad de la losa (ISO 10005:2018). Incluye una política y 12 objetivos con metas; matrices de riesgos y responsabilidades; un plan de inspección con 14 controles, 4 de ellos puntos de espera; cinco procedimientos de control de materiales, de la recepción a la conciliación de cantidades; el control del hormigón según el ACI 318-25, con al menos cinco ensayos por losa; el manejo de no conformidades; el registro de costos de la calidad; y los formatos C.1 a C.8. Con los valores más probables, cuesta Bs 4,86 por m².

### Objetivo 4: efecto del sistema

Con los valores más probables, el costo por m² bajó de Bs 275,38 a Bs 271,46 (1,43 %). En 20.000 escenarios, la reducción promedio fue de 1,47 %: en 90 de cada 100, entre −0,05 % (un leve aumento) y 3,21 %. En promedio, el desperdicio ponderado bajó de 8,16 % a 4,70 % y el costo de no calidad, de Bs 22,80 a Bs 12,58 por m². Lo que más influyó: el costo del SGC y los datos del retrabajo. El SGC cubre su propio costo con una eficacia de 24,8 %. Si no se aplicara en el 15 % de los casos, la reducción bajaría a 0,90 %; con los costos ocultos (tiempo perdido y demoras), subiría a 3,22 %. Deja de ser rentable con una eficacia claramente menor que la reportada o con el doble de costo.

### Objetivo 5: hipótesis y validación

Una hipótesis se aceptaba si se cumplía en al menos 95 de cada 100 escenarios, regla equivalente a un nivel de significancia de 0,05 (Tabla C.1). La decisión sobre la hipótesis general se mantuvo con todas las variantes de los supuestos y con los costos ocultos, donde la probabilidad de llegar al 5 % fue de 0,1316.

**Tabla C.1.** Decisión sobre las hipótesis

| Hipótesis | Qué afirma | Probabilidad | Decisión |
|---|---|---|---|
| General (HG) | El costo por m² baja 5 % o más | 0,0008 | No se acepta H1 (se mantiene H0) |
| Específica 1 (HE1) | El desperdicio baja | 1,0000 | Se acepta H1 |
| Específica 2 (HE2) | El costo de no calidad baja | 1,0000 | Se acepta H1 |

La validación por juicio de expertos (V de Aiken) se preparó con el formato C.8, pero no se aplicó; se recomienda aplicarla, porque de ella depende la aplicabilidad del sistema.

## Recomendaciones

### Para la UATF

1. Exigir en la contratación del saldo un plan de la calidad de la losa, con el plan de inspección, el muestreo del hormigón y los formatos del Anexo C, y aprobar con observación y retención de pago el paño sin resultados de ensayos a 28 días.
2. Antes de liquidar el contrato resuelto, revisar el acero del ítem 8 elemento por elemento. Hay diferencias entre documentos que conviene aclarar con la Supervisión y la Fiscalización: la losa computada como 3 × 4.171,18 kg, la baja de 10.257,78 kg en otros elementos, las dos versiones de la planilla de cierre y los 85.777,46 kg de la tabla de tiempos. Conviene definir con el APU del contrato si el ítem 13 incluye la parrilla y los negativos.
3. Actualizar las especificaciones: cambiar la CBH-87 y las normas antiguas por la NB 1225001-1:2017 y las ediciones vigentes de IBNORCA, incluir la NB 997:2016, fijar el criterio de aceptación del hormigón, definir el bloque de plastoformo y ubicar en los planos los nervios y los negativos.
4. Evaluar con la Supervisión y el proyectista si conviene verificar en el sitio la resistencia del hormigón de la primera losa antes de cargarla con los niveles superiores.

### Para la empresa constructora

Aplicar un SGC «ligero», con el personal existente y cuatro controles clave: producir solo el hormigón de cada vaciado, despiece y prearmado del acero, recepción por lotes con criterios conocidos y conciliación por paño. Como su costo es lo que más pesa, conviene mantenerlo cerca de lo previsto y registrar los costos de la calidad desde el inicio. La empresa es la que más gana al reducir el desperdicio: sus precios incluyen la reparación de trabajos defectuosos y no se reajustan.

### Para la Supervisión y la Fiscalización

Liberar cada paño en los puntos de espera con la ficha C.2 y el asiento del Libro de Órdenes firmado por el Director de Obra; exigir probetas en cada vaciado, tomadas por personal ajeno a la producción, sin aceptar resistencias proyectadas desde otras edades; pedir certificados por lote o colada antes de colocar los materiales; conciliar las cantidades antes de aprobar cada planilla; y registrar las no conformidades y su cierre, para que la calificación de la calidad se apoye en evidencia.

### Para futuros estudios

1. Medir en obra el efecto real, paño por paño, cuando se construya el saldo (prueba *t* para muestras relacionadas o de Wilcoxon) y actualizar el modelo.
2. Incluir los costos del plazo (multas, gastos de ampliaciones y esperas) y los costos ocultos.
3. Evaluar otros ítems de hormigón armado y la obra completa, para ver si así se alcanza un 5 %.
4. Medir el desperdicio de viguetas y plastoformo, sin valores de referencia en la literatura revisada.
5. Modelar la relación entre los datos y repetir el estudio en otras obras públicas.

## Límites del estudio

- Evaluación previa (*ex ante*), por simulación: la segunda losa no se construyó durante la investigación.
- Un solo caso: una obra y una losa.
- Datos documentales: sin registros de consumo, solo el plastoformo y el acero tuvieron un dato propio; lo demás viene de otros estudios.
- Precio de referencia reconstruido, sin el APU del contrato y ajustado con un factor de 0,962.
- Precios constantes, sin costos del plazo.
- Diagnóstico sin entrevistas: un cero indica que algo no quedó registrado, no que no se hizo.
- La lista de verificación resume la norma con palabras propias, sin su texto oficial.
- Sin opinión de expertos.

Por eso, las cifras de ahorro son estimaciones; se recomienda comprobarlas con datos medidos en obra.

# Qué contienen los anexos

La versión académica tiene doce anexos (Tabla A.1).

**Tabla A.1.** Anexos de la tesis

| Anexo | Qué contiene y para qué sirve |
|---|---|
| A. Matriz de consistencia | Une problema, objetivos, hipótesis, variables y método, para ver que todo encaja. |
| B. Operacionalización de variables | Dice cómo se midió cada variable: indicadores, fórmulas e instrumentos. |
| C. Instrumentos y formatos del SGC | Trae los formatos C.1 a C.8 (verificación, liberación por paño, recepción, conciliación, no conformidades, costos, entrevista y validación) para aplicar el sistema. |
| D. Validación por juicio de expertos | Explica cómo tres a cinco ingenieros califican el sistema, para organizar esa revisión. |
| E. Planos de la primera losa | Muestran ejes, detalles y viguetas por paño, base de las cantidades teóricas. |
| F. Cómputos métricos y planillas de avance | Dan el área de los 41 paños, de donde salen los 1.109,84 m² pagados. |
| G. Certificados de calidad de materiales | Muestran qué garantizaron PRETENSA (viguetas) y UNICON (plastoformo), y en qué fecha. |
| H. Resultados de ensayos de laboratorio | Presenta el certificado N.º 000293: 10 probetas de columnas y 2 de vigas, ninguna de la losa. |
| I. Análisis de precios unitarios de referencia | Reconstruye el precio de la losa y del acero, ajustado al contrato, para valorar el material perdido. |
| J. Panel fotográfico | Muestra la construcción de las vigas y de la primera losa. |
| K. Documentos de contexto | Reúne comunicados de FANCESA y de la Cámara de la Construcción de Tarija (2025) sobre la crisis del cemento. |
| L. Modelo de costos y simulación | Da los parámetros, sus fuentes y el código para repetir los 20.000 escenarios con las mismas cifras. |

# Glosario

- **Análisis de precios unitarios (APU):** desglose del precio de una unidad de trabajo en materiales, mano de obra, equipo, gastos generales, utilidad e impuestos.
- **Carpeta de compresión:** capa de hormigón de 5 cm, con una malla de acero (parrilla), vaciada sobre las viguetas y el plastoformo.
- **Conciliación de cantidades:** comparar, por paño, las cantidades de los planos, entregadas, colocadas, medidas y pagadas, y aclarar las diferencias antes del pago.
- **Costo de la calidad:** gasto en prevenir y revisar (personal de calidad, capacitación, inspecciones y ensayos).
- **Costo de no calidad:** costo de las fallas, como el material desperdiciado y los trabajos rehechos.
- **Desperdicio:** material consumido por encima de lo necesario según los planos.
- **Eficacia del sistema:** parte del desperdicio o del retrabajo que el SGC elimina; con 44 %, el desperdicio de hormigón baja de 10,00 % a 5,60 %.
- **Fiscalización:** control del fiscal de obra de la UATF sobre el avance físico y financiero y los cambios del contrato.
- **Hipótesis nula (H0):** lo contrario de la hipótesis puesta a prueba (H1); se mantiene si no se cumple la regla de decisión.
- **Hormigón H25:** hormigón de la losa, con resistencia característica de 250 kg/cm² a los 28 días.
- **Índice de desperdicio de materiales (IDM):** diferencia entre la cantidad consumida y la teórica, en porcentaje de la teórica.
- **ISO 9001:** norma internacional de requisitos para un SGC; edición vigente de 2026, adoptada en Bolivia por IBNORCA.
- **Libro de Órdenes:** cuaderno oficial de la obra donde el Supervisor anota sus instrucciones y la empresa, sus solicitudes.
- **Línea base:** situación de partida para comparar una mejora; aquí, la primera losa, hecha sin SGC.
- **Losa alivianada:** losa de viguetas pretensadas, bloques livianos de plastoformo y carpeta de compresión; aquí, de 25 cm de alto.
- **No conformidad:** incumplimiento de un requisito de los planos, las especificaciones, las normas o el contrato.
- **Paño:** cada sector en que se divide la losa para medirla y controlarla; la primera losa tiene 41.
- **Plan de la calidad:** documento que dice qué se controla, con qué criterio, quién responde y qué se registra (ISO 10005:2018).
- **Plan de puntos de inspección y ensayo (PPI):** lista ordenada de controles, cada uno con criterio de aceptación, frecuencia y responsable.
- **Planilla de avance de obra:** documento que mide lo ejecutado en un periodo y sirve para pagar a la empresa.
- **Plastoformo (EPS):** poliestireno expandido; bloque liviano que va entre las viguetas para alivianar la losa.
- **Precios constantes:** precios fijos del contrato, para que las alzas no se confundan con el efecto del sistema.
- **Probeta:** cilindro de hormigón tomado en el vaciado y ensayado a compresión a los 28 días para comprobar su resistencia.
- **Punto de equilibrio:** eficacia mínima con la que el ahorro del SGC iguala su costo (24,8 %).
- **Punto de espera:** control del PPI en el que el trabajo se detiene hasta que la Supervisión revisa y firma.
- **Retrabajo:** volver a hacer lo que se ejecutó mal la primera vez.
- **Simulación de Monte Carlo:** repetir un cálculo miles de veces con datos tomados al azar dentro de rangos.
- **Sistema de gestión de la calidad (SGC):** conjunto de políticas, objetivos, procesos, controles y registros para cumplir los requisitos de un trabajo.
- **Supervisión:** quien controla técnicamente la obra por cuenta de la UATF; según el contrato, responde directamente del control de calidad.
- **V de Aiken:** número de 0 a 1 que mide el acuerdo de los expertos; se acepta con 0,70 o más.
- **Vigueta pretensada:** pieza prefabricada de hormigón y acero de pretensado que resiste la flexión de los nervios de la losa (NB 997:2016).

# Fuentes principales

ACI Committee 318. (2025). *Building code for structural concrete: Code requirements and commentary (ACI CODE-318-25)*. American Concrete Institute.

Alcón Aranda, M. W. (2009). *Evaluación del proceso de fabricación y aplicación de viguetas pretensadas en estructuras* [Tesis de licenciatura]. Universidad Mayor de San Andrés. <https://repositorio.umsa.bo/handle/123456789/7465>

Alfaro Félix, O. C. (2011). *Sistemas de aseguramiento de la calidad en la construcción* [Tesis de licenciatura]. Pontificia Universidad Católica del Perú. <http://hdl.handle.net/20.500.12404/185>

Barrios C., J. C. (2021). *Documento de graduación* [Diapositivas de clase, Taller 1]. CIV 400 Seminario de Grado II, Carrera de Ingeniería Civil, Universidad Autónoma Tomás Frías.

Chino Quispe, A. y Zarate Chilqquetuma, K. B. (2024). *Análisis comparativo del método de despiece de acero pre ejecución frente al acero dimensionado y uso convencional del acero corrugado en la construcción de edificaciones en la ciudad del Cusco 2023* [Tesis de licenciatura]. Universidad Nacional de San Antonio Abad del Cusco. <https://hdl.handle.net/20.500.12918/9553>

Galarza Meza, M. P. (2011). *Desperdicio de materiales en obras de construcción civil: métodos de medición y control* [Tesis de licenciatura]. Pontificia Universidad Católica del Perú. <http://hdl.handle.net/20.500.12404/888>

Gudiel Cairampoma, R. A. y Solis Puente, N. P. (2020). *Propuesta para reducir los costos de la no calidad en las partidas de concreto armado utilizando los lineamientos del PMBOK en proyectos de edificación en pequeñas y medianas empresas en la ciudad de Lima* [Tesis de licenciatura]. Universidad Peruana de Ciencias Aplicadas. <https://doi.org/10.19083/tesis/652829>

Hernández-Sampieri, R. y Mendoza Torres, C. P. (2018). *Metodología de la investigación: las rutas cuantitativa, cualitativa y mixta*. McGraw-Hill Interamericana Editores.

Instituto Boliviano de Normalización y Calidad. (2016). *Elementos prefabricados de hormigón: viguetas prefabricadas de hormigón pretensado. Requisitos y métodos de ensayo* (Norma Boliviana N.º NB 997:2016). <https://www.ibnorca.org/tienda/catalogo/detalle-norma/nb-997:2016-nid=2436-12>

Khadim, N., Thaheem, M. J., Ullah, F. y Mahmood, M. N. (2023). Quantifying the cost of quality in construction projects: An insight into the base of the iceberg. *Quality & Quantity*, *57*(6), 5403–5429. <https://doi.org/10.1007/s11135-022-01574-8>

Mamani Calsina, D. (2025). *Diseño de un sistema de gestión de calidad en la empresa «PRENSOCRET» basado en la NB ISO 9001:2015* [Proyecto de grado de licenciatura]. Universidad Mayor de San Andrés. <https://repositorio.umsa.bo/handle/123456789/42372>

Ministerio de Economía y Finanzas Públicas. (2025). *NB-SABS: Decreto Supremo N.º 0181, Decreto Supremo N.º 1497, Decreto Supremo N.º 4453, Reglamento del RUPE, Reglamento de Contrataciones con Apoyo de Medios Electrónicos y Manual de Operaciones del SICOES* [Texto compilado, actualizado 2025].

Ministerio de Obras Públicas, Servicios y Vivienda. (2023). *Norma Boliviana de Diseño Sísmico (NBDS 2023)*. Aprobada por Resolución Ministerial N.º 271 de 27 de noviembre de 2023.

Muro Núñez, E. A. (2020). *Evaluación del control de calidad en la construcción del sistema de estructuras del Open Plaza Pucallpa* [Tesis de licenciatura]. Universidad César Vallejo. <https://hdl.handle.net/20.500.12692/92836>

Organización Internacional de Normalización. (2018). *Gestión de la calidad: directrices para los planes de la calidad* (Norma ISO N.º 10005:2018).

Organización Internacional de Normalización. (2026). *Sistemas de gestión de la calidad: requisitos* (Norma ISO N.º 9001:2026). <https://www.iso.org/standard/88464.html>

Peña Callisaya, J. A. (2024). *Diseño de un sistema de gestión de la calidad según la NB/ISO 9001:2015 en el área de producción de la empresa «ISOCRET»* [Proyecto de grado de licenciatura]. Universidad Mayor de San Andrés. <https://repositorio.umsa.bo/handle/123456789/41024>

Ruiz Muñoz, N. A. y Rojas Bonilla, C. E. (2018). *Análisis de los desperdicios del concreto y su incidencia en el presupuesto final* [Trabajo de grado de tecnólogo en construcciones arquitectónicas]. Universidad La Gran Colombia. <http://hdl.handle.net/11396/3329>

La lista completa de referencias está en la versión académica de la tesis.
