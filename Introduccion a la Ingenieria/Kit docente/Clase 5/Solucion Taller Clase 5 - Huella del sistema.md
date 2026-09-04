# Solución del taller — Clase 5: Huella del sistema

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni compartir pantalla con él antes de que los equipos trabajen: es la respuesta completa del entregable, y verla antes convierte el taller en copia.

## Para qué sirve este documento

Este documento resuelve la huella completa de un sistema concreto —una app de citas para un consultorio de barrio— y trae al final las claves de los cuatro tipos de proyecto que suelen aparecer. Sirve sobre todo para dos cosas que el docente necesita en el momento: distinguir una decisión de diseño de una recomendación al usuario, y tener ejemplos de indicadores bien formulados, que es donde se cae el taller.

## El caso que se resuelve aquí

**App de citas de un consultorio de barrio · huella completa**

El sistema: los pacientes piden cita desde el celular, la secretaria administra la agenda desde un computador de escritorio de hace siete años, y el sistema corre en un servicio en la nube de plan gratuito. Unos 60 pacientes al día. La app consulta el estado de la agenda cada 10 segundos mientras está abierta, para que el cupo se vea «en vivo», y cada pantalla carga la foto del consultorio en tamaño original.

> Se eligió porque tiene las dos fallas típicas plantadas a propósito —el sondeo cada 10 segundos y la imagen sin ajustar— y porque el computador de siete años de la secretaria obliga a hablar de la decisión de mayor impacto real: no forzar el cambio de aparato.

## Consigna que se les dio

> Dibujen en Excalidraw la **huella material** del sistema de su proyecto: por dónde pasa la energía, la materia y el residuo en las cuatro etapas. Marquen cuál etapa pesa más, propongan **dos decisiones de diseño** que la bajen y definan **un indicador medible** que se pueda revisar en la Clase 16.

**Entregable:** un diagrama de huella en Excalidraw exportado a PNG en la carpeta del equipo, más las dos decisiones y el indicador escritos en el documento del equipo · **17 min de trabajo · 3 min de exposición**

## Respuesta bloque por bloque

### 1. EL RECORRIDO DIBUJADO

**Se pedía:** El camino completo con flechas: dispositivo del usuario → red → servidor → almacenamiento, y todo lo que se prende para que el sistema funcione.

**Respuesta modelo:**

**Etapa 1 · Fabricación.** 60 celulares de pacientes al día (que ya existen y se usan para otras cosas), 1 computador de escritorio de siete años en el consultorio, y la fracción que le corresponde al sistema de los servidores del proveedor de nube, que están compartidos con miles de otros clientes.

**Etapa 2 · Uso.** Electricidad del celular mientras la app está abierta (pantalla y radio son lo que más gasta), electricidad del computador del consultorio encendido ocho horas al día, y electricidad del servidor **más su enfriamiento** —aquí entra el PUE: si el centro de datos tiene PUE 1.5, por cada vatio que computa el sistema se gasta medio vatio en enfriar.

**Etapa 3 · Red.** Cada consulta viaja del celular a la antena celular, de ahí a la red del operador y al centro de datos. Se dibuja como una cadena, no como una flecha: la antena y los equipos intermedios también consumen.

**Etapa 4 · Fin de vida.** El computador del consultorio, cuando se reemplace, es RAEE: debe entregarse en un punto de recolección del productor, por la Ley 1672 de 2013, no en la basura común. Los celulares de los pacientes también, pero **el sistema no controla eso**; lo que el sistema sí controla es si obliga a cambiarlos.

**Cómo calificar:** 20 pts. Lo que decide es que **estén las cuatro etapas**, no la belleza del diagrama. Casi todos los equipos dibujan bien el uso y la red —que es el flujo de datos que ya intuyen— y omiten fabricación y fin de vida. Un diagrama con solo uso y red vale 8. Si el equipo señala que la fabricación del servidor es **compartida** con otros clientes, súbale: es un razonamiento correcto y fino.

### 2. LO QUE SE REPITE

**Se pedía:** Qué operación ocurre **muchas veces al día** en su sistema, y una estimación gruesa de cuántas veces. Lo que pasa una vez no mueve nada.

**Respuesta modelo:**

**La operación repetida es la consulta del estado de la agenda cada 10 segundos mientras la app está abierta.** Estimación gruesa, declarada como estimación: si un paciente tiene la app abierta unos 3 minutos para pedir su cita, son unas 18 consultas por paciente; con 60 pacientes al día, del orden de **1.000 consultas diarias solo para mostrar algo que casi nunca cambió**.

La segunda operación repetida es la carga de la foto del consultorio en cada pantalla. Si la imagen original pesa, por decir algo verificable midiéndola, 2 MB, y se carga en cada una de las 3 pantallas por paciente, son unos 6 MB por paciente y del orden de **360 MB diarios de red** para mostrar la misma foto.

Las dos cifras están calculadas a partir de datos que el equipo puede medir en su propio sistema (peso del archivo, número de pantallas, número de pacientes). Eso es lo que se pide: **no una cifra de internet, sino una estimación construida y declarada**.

**Cómo calificar:** 15 pts. El criterio es doble: que haya un número **y** que esté declarado como estimación con el razonamiento visible. Una cifra sin razonamiento vale 5, aunque sea plausible. Un razonamiento correcto sin número vale 8. Los 15 completos exigen «aproximadamente X, calculado así».

### 3. LA ETAPA QUE MÁS PESA

**Se pedía:** Una sola etapa, con la razón. No hace falta un cálculo exacto: hace falta saber dónde apretar.

**Respuesta modelo:**

**La etapa 1, fabricación**, y el argumento es el del computador de siete años del consultorio. En un dispositivo personal la mayor parte de la huella de toda su vida se gasta al fabricarlo, así que la decisión con más efecto material no es ahorrar electricidad: es que el sistema **siga funcionando en ese computador** y no obligue a comprar uno nuevo. Un equipo que decida usar una tecnología que solo corre en navegadores muy recientes está tomando, sin darse cuenta, una decisión con consecuencia en toneladas de residuo.

**Respuesta alternativa igual de válida: la etapa 3, red**, con el argumento de las 1.000 consultas y los 360 MB diarios, que es dinero y datos de los pacientes además de energía. Lo que **no** se acepta es «todas pesan igual»: eso significa que no eligieron y no permite actuar.

**Cómo calificar:** 20 pts. Se acepta cualquier etapa **con argumento consistente con lo que escribieron antes**. Un equipo que elija «uso» argumentando solo el consumo de la batería del celular vale 10: es la respuesta intuitiva y la más débil, porque la batería del celular es lo pequeño de la cuenta. «Todas pesan» vale 0 y hay que decirlo con el argumento: elegir es el trabajo del ingeniero.

### 4. DOS DECISIONES DE DISEÑO

**Se pedía:** Dos cosas que **ustedes** pueden decidir en su sistema para bajar esa etapa. De diseño, no de comportamiento del usuario.

**Respuesta modelo:**

**Decisión 1 · Cambiar el sondeo por actualización bajo demanda.** En vez de consultar la agenda cada 10 segundos, se consulta al abrir la pantalla y cuando el paciente hace algo (recargar, confirmar). Baja de unas 18 consultas por paciente a 2 o 3. Es una decisión de diseño, está bajo control del equipo, y **no le quita nada al paciente**: la probabilidad de que un cupo cambie en los 10 segundos exactos que él está mirando es mínima.

**Decisión 2 · Sostener el soporte del computador de siete años.** Concretamente: no usar funciones que exijan un navegador de última generación, probar el sistema en ese computador antes de cada entrega, y ajustar las imágenes al tamaño real en que se muestran (la foto de 2 MB pasa a unos 80 KB). Baja red y evita el reemplazo del aparato, que es la parte gorda de la huella.

**Ejemplos de lo que NO cuenta como decisión de diseño:** «pedirle a la secretaria que apague el computador al mediodía», «recomendar a los pacientes que usen wifi en vez de datos», «concientizar sobre el reciclaje». Las tres pueden ser buenas ideas y ninguna está bajo control del equipo: son comportamiento de otros.

**Cómo calificar:** 25 pts, 12,5 por decisión. El criterio único y estricto es **¿está bajo control del equipo?**. Una recomendación al usuario vale 0 como decisión, aunque sea sensata; dígalo en el momento en la sala, porque es el error más frecuente del taller. Si las dos decisiones atacan la etapa que el equipo eligió como más pesada, dé los 25; si atacan otra, máximo 15, porque hay incoherencia entre el diagnóstico y la acción.

### 5. EL INDICADOR

**Se pedía:** Un número que se pueda medir al final del semestre para saber si la decisión funcionó. Con su unidad.

**Respuesta modelo:**

**Indicadores bien formulados para este caso:**

- «**Consultas al servidor por cita agendada.** Hoy ~18. Meta: menos de 4. Se mide contando las peticiones en el registro del servidor.»
- «**Kilobytes transferidos por pantalla.** Hoy ~2.000 KB por la imagen. Meta: menos de 200 KB. Se mide con las herramientas del navegador.»
- «**El sistema funciona en el computador de siete años del consultorio: sí / no.** Se verifica abriéndolo ahí antes de cada entrega.»

Los tres tienen unidad (o son un sí/no verificable), se miden con algo que el equipo va a tener, y se pueden revisar en la Clase 16.

**Indicadores mal formulados y por qué:** «reducir el consumo energético» (no tiene unidad ni línea base); «ser un sistema sostenible» (no es medible); «bajar las emisiones de CO₂ en un 30 %» (el equipo no puede medir eso, y para calcularlo necesitaría el factor de emisiones y datos del centro de datos que no tiene).

**Cómo calificar:** 20 pts. Tres requisitos: **unidad, línea base o valor de hoy, y cómo se mide**. Si falta el «cómo se mide», máximo 10: es el requisito que convierte el indicador en algo revisable. El indicador de emisiones de CO₂ vale 5 aunque suene ambicioso, y hay que explicar por qué: proponer medir lo que no se puede medir es peor que proponer algo modesto y verificable. **Anote los cinco indicadores**: se revisan en la Clase 16.

## Rúbrica del taller

| Criterio | Peso | Por qué pesa eso |
|---|---|---|
| El diagrama muestra las cuatro etapas, no solo el flujo de datos | **20 %** | La etapa de fabricación y la de fin de vida son las que nadie dibuja, y suelen ser las que más pesan. |
| Hay una operación repetida con una estimación declarada como estimación | **15 %** | Estimar y decir que se está estimando es la habilidad honesta que reemplaza a inventar cifras. |
| Se eligió UNA etapa como la más pesada, con argumento | **20 %** | Elegir es el trabajo del ingeniero. «Todo importa» no permite actuar. |
| Las dos decisiones son de diseño y están bajo control del equipo | **25 %** | Es lo que convierte la conciencia ambiental en ingeniería. |
| El indicador tiene unidad y se puede medir en la Clase 16 | **20 %** | Sin indicador no hay forma de saber si la decisión sirvió, y el informe final lo pide. |

> Suma **100 %**. La nota es del equipo, no del vocero.

## Si el equipo trabajó otro caso

**Proyecto de tipo inventario o ventas de un negocio.** La operación repetida suele ser la consulta de existencias o la recalculación de un reporte en cada carga. La etapa más pesada suele ser **uso**, por el cómputo repetido, y la decisión fuerte es guardar el resultado y recalcular solo al cambiar. Buen indicador: «segundos para cargar el reporte» o «consultas a la base por venta registrada». Cuidado con la trampa: los equipos proponen «imprimir menos facturas», que es comportamiento del negocio, no diseño.

**Proyecto con formularios o encuestas.** La huella es baja y hay que decírselo: no todo proyecto tiene un problema ambiental grande, y **reconocerlo es más honesto que inflarlo**. La etapa que suele pesar es **red**, por adjuntos y fotos sin ajustar. Decisión fuerte: comprimir en el dispositivo antes de subir. Indicador: «KB promedio por respuesta enviada». Si el equipo dice honestamente que su huella dominante es la fabricación de los dispositivos que ya existen y que su margen de acción es pequeño, dé la nota completa: eso es análisis correcto.

**Proyecto que incluye un asistente de IA.** Es el caso donde la clase pega más fuerte. La etapa **uso** domina, porque cada llamada al modelo consume cómputo en un centro de datos. La decisión de diseño más potente es la de la diapositiva: **no llamar al modelo cuando una regla simple resuelve**, y guardar respuestas repetidas en vez de volver a preguntar. Indicador: «llamadas al modelo por usuario atendido». Exija honestidad con las cifras: no hay un número público confiable de energía por consulta, así que se mide **el número de llamadas**, que sí se puede contar.

**Proyecto de hardware, sensores o IoT.** Aquí la etapa 1 (fabricación) y la 4 (fin de vida) son las dominantes y por primera vez son físicas y propias del equipo: cada sensor es un aparato que se fabricó y que va a ser residuo. Decisión fuerte: menos dispositivos con más cobertura, y batería reemplazable. Indicador: «número de dispositivos por área cubierta» o «meses de vida útil esperada». Es el único caso donde el equipo debería mencionar explícitamente la Ley 1672 de 2013, porque va a generar RAEE de verdad.

## Errores que hay que ver y no dejar pasar

- **«La nube no contamina, es virtual»** → La nube es un edificio con servidores, electricidad y enfriamiento, muchas veces con agua. Que dibujen dónde está el servidor y qué se prende para que funcione. Y que nombren el PUE.
- **«Vamos a pedirle al usuario que ahorre energía»** → No es una decisión de diseño: es comportamiento de otra persona, fuera de su control. Algo que ellos puedan decidir en su propio sistema: cada cuánto consulta, cuánto pesa lo que envía, qué dispositivos soporta.
- **«Todas las etapas pesan igual»** → Significa que no eligieron, y sin elegir no se puede actuar. Una sola etapa y el argumento, aunque sea aproximado.
- **«Cada consulta a la IA gasta X litros de agua»** → Las cifras que circulan varían por órdenes de magnitud y casi nunca dicen de qué sistema ni de qué año son. Fuente, año y alcance. Si no lo tienen, que midan lo que sí pueden contar: el número de llamadas.
- **«Ser un sistema sostenible» como indicador** → No tiene unidad y no se puede revisar en la Clase 16. Un número con unidad, el valor de hoy y cómo se va a medir.

## Cierre: qué decir en los 3 minutos finales

Tres minutos, una idea: **el software no es inmaterial.** Tiene cuatro etapas —fabricación, uso, red y fin de vida— y en las cuatro hay energía, materia y residuo. Diga el dato que más reordena las prioridades: en un dispositivo personal la mayor parte de la huella ya está gastada cuando se enciende, así que **la decisión ambiental más fuerte que ellos pueden tomar no es ahorrar batería, es no obligar a cambiar de aparato**. Cierre con la honestidad de las cifras, porque es lo que los va a distinguir: la huella existe, se puede reducir con decisiones de diseño y casi nadie la mide; cualquier número que digan va con fuente, año y alcance. Y anuncie la sesión 6 sin adornos: cierra el corte 1, sale la ficha del problema del proyecto —que ya viene armándose desde la sesión 1— y hay evaluación de corte en ExamLab al final de la sesión.

## Con qué se conecta

Hacia atrás: la sesión 3 dio la frontera del sistema, y hoy la huella obligó a estirarla hasta la fabricación y el residuo, que casi nadie mete dentro; la sesión 4 dio el afectado con nombre, y hoy apareció el afectado sin nombre. Hacia adelante: el **indicador** de hoy entra en la ficha del problema de la **Clase 6** y se revisa en el informe final de la **Clase 16**; la eficiencia como decisión de diseño reaparece en la **Clase 7** (ciclo de vida) y en la **Clase 10**; y la **Clase 13** retoma impacto social y ambiental con el prototipo ya construido.
