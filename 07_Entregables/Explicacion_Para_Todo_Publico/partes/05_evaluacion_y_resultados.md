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
