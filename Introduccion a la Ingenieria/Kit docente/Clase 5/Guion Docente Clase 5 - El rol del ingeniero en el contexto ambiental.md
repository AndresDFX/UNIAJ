# Guion docente — Clase 5: El rol del ingeniero en el contexto ambiental

## Información de la clase
- Asignatura: Introducción a la Ingeniería (FI300101)
- Duración del bloque: **90 min**
- Tipo: Clase virtual sincrónica por Google Meet · Sesión 5 de 16 · corresponde al tema 5 del microcurrículo
- Modalidad: **Virtual (síncrona)** por Google Meet · actividades en plataformas gratuitas en la nube · los 5 equipos trabajan en **salas de grupo**
- Corte **1** (30%) · RAA: **RAA2**
- **Material general para los tres grupos** (SB141B, SB141C, LB141F): sin fechas ni horarios de reloj. El reloj de pared de cada grupo está en su `CALENDARIO_2026-2 - <GRUPO>.md`.
- Enfoque: Aprendizaje basado en competencia + Aprendizaje Invertido · Estrategia: ABPr — Aprendizaje Basado en Proyectos

## Objetivos de la clase
- Nombrar las **cuatro etapas** de la huella material de un sistema de software: fabricación, uso, red y fin de vida.
- Explicar qué mide el **PUE** de un centro de datos y por qué el enfriamiento cambia la cuenta.
- Relacionar una decisión de diseño con un **efecto ambiental medible**.
- Nombrar la norma colombiana de **residuos electrónicos** y qué obliga.

## Hoy avanzamos el proyecto en…

**Ponerle al proyecto del equipo una restricción ambiental verificable y un indicador que se pueda medir al final del semestre**

**Entregable concreto:** un diagrama de huella en Excalidraw exportado a PNG en la carpeta del equipo, más las dos decisiones y el indicador escritos en el documento del equipo

**Herramientas de esta sesión:** Excalidraw · Google Drive (Docs y Slides)

> El taller se hace en **Excalidraw**, que abre sin cuenta y sirve para dibujar rápido y a mano alzada — es lo que se necesita hoy, porque el diagrama de la huella es un mapa de flechas, no un plano bonito. El PNG exportado va a la carpeta del equipo en Drive. Hoy **no se usa IA**: las cifras ambientales son justo donde más inventa.

## Fundamento teórico para el docente

Esta sección está escrita para dictar la clase **sin consultar otra fuente**, y va dividida por diapositiva: cada bloque dice a qué diapositiva corresponde.

### La pregunta de entrada: darle materia a algo que parece no tenerla - diapositiva 4

«¿Dónde está la nube?» funciona porque casi nadie ha visto un centro de datos y porque la metáfora está diseñada para que no se piense en el edificio. La segunda parte —cuánta agua se bebió una consulta a un asistente de IA— incomoda a propósito y hay que manejarla con cuidado: la respuesta honesta es que **depende del centro de datos, del modelo, del clima y del año**, y que las cifras que circulan varían por órdenes de magnitud. Eso no debilita la clase: es la clase. El objetivo no es que se lleven un número, es que entiendan que hay agua y electricidad detrás de algo que se siente inmaterial, y que quien afirme un número tiene que decir de dónde salió.

Recoja las respuestas en el muro y no las corrija. En el minuto 20, al llegar al PUE y al enfriamiento, vuelva al muro: alguien va a haber escrito «en internet» o «en un servidor», y ahí se muestra que el servidor está en un edificio que consume tanto en enfriarse como en computar.

### Las cuatro etapas y por qué la fabricación cambia la recomendación - diapositiva 5

La huella material de un sistema de software se reparte en cuatro etapas y conviene recorrerlas con un ejemplo único: una aplicación de citas médicas usada desde el celular.

**Fabricación.** El celular del paciente, el computador de la secretaria y los servidores donde corre el sistema tuvieron que ser fabricados: minería de metales —incluidos varios escasos y con extracción problemática—, ensamblaje y transporte. Este es el punto que más sorprende y el más importante para las decisiones: **en muchos dispositivos personales la mayor parte de la huella de toda su vida ya está gastada cuando se enciende por primera vez**. La consecuencia es contraintuitiva: optimizar el consumo de batería es útil, pero **alargar la vida útil del aparato pesa mucho más**, y eso depende de decisiones de software.

**Uso.** Electricidad del dispositivo, del servidor y —esto es lo que se olvida— del enfriamiento del centro de datos. Aquí entra el PUE.

**Red.** Cada byte que viaja pasa por antenas, cables, enrutadores y equipos que consumen. No es gratis y crece con el volumen: una pantalla que carga imágenes en tamaño original mil veces al día mueve un múltiplo de lo necesario.

**Fin de vida.** El aparato se vuelve residuo electrónico. Tiene metales recuperables y sustancias peligrosas, y cuando no se recoge formalmente se desarma a mano, quemando plásticos, con daño directo a las personas que lo hacen.

El punto pedagógico de la diapositiva es que las palabras «software» y «nube» están construidas para que uno no piense en nada de esto. Nombrar las cuatro etapas es lo que permite discutir el tema con seriedad.

### PUE, agua, RAEE y obsolescencia: los cuatro conceptos que hay que dejar - diapositiva 6

**PUE (Power Usage Effectiveness).** Es la energía total que entra al centro de datos dividida por la energía que efectivamente llega a los servidores. Si fuera 1.0, todo lo que entra se usa en computar. Un PUE de 1.6 significa que por cada vatio de cómputo se gastan 0,6 en enfriar, iluminar y en pérdidas. Los centros de datos grandes y modernos operan bastante mejor que el promedio de las salas de servidores de empresa, que suelen estar en el rango de 1.5 a 1.6 según las encuestas del sector. La idea que hay que dejar no es el número exacto: es que **una parte grande de la energía de un centro de datos no computa nada**, y que existe una métrica con nombre para medirlo. Un ingeniero que sabe que el PUE existe puede preguntar por él.

**El agua.** Enfriar con evaporación de agua es más barato en electricidad que enfriar con máquinas, así que muchos centros de datos usan agua. Eso traslada el costo: baja la factura de luz y sube el consumo de una cuenca que normalmente abastece a población. Es un buen ejemplo de algo que el curso repite: **optimizar una variable suele mover el problema a otra**, y el ingeniero tiene que saber a cuál. Hay métricas para esto (WUE, litros por kilovatio-hora), y aquí también vale la advertencia de las cifras.

**RAEE y la Ley 1672 de 2013.** Es la norma colombiana que fija los lineamientos para la gestión de residuos de aparatos eléctricos y electrónicos. Lo que hay que poder decir: **obliga a los productores** a establecer sistemas de recolección y gestión, y **establece el deber del usuario** de entregar el aparato en esos puntos en vez de tirarlo a la basura común. Los informes globales de residuos electrónicos (Global E-waste Monitor, de UNITAR e ITU) reportan decenas de millones de toneladas al año y una tasa de recolección formal baja: el orden de magnitud es que **la mayor parte no se recoge**. Si un equipo cita una cifra exacta, exija la edición del informe y el año, porque cambia entre ediciones.

**Obsolescencia inducida por software.** Es el concepto que más les sirve porque está bajo su control profesional. Cuando una nueva versión de una aplicación —o de un sistema operativo— deja de funcionar en dispositivos que servían, el software convierte en basura un aparato que estaba bien. No hace falta discutir si hay intención: el efecto es material y medible. Y la contracara es una decisión concreta que un equipo de este curso puede tomar: **sostener el soporte para dispositivos viejos**, que además es lo correcto para el contexto de la universidad, donde muchos estudiantes trabajan con equipos de varios años.

### De la conciencia a la decisión: la diapositiva que convierte el tema en ingeniería - diapositivas 7 y 9

Esta es la diapositiva que salva la clase de volverse un discurso. Las cinco parejas son decisiones reales de diseño, y en las cinco la versión de la derecha **cumple la misma función**. Eso hay que decirlo explícitamente: no se está pidiendo sacrificar calidad por ambiente, se está pidiendo no desperdiciar.

La primera —pedir la ubicación cada cinco segundos o cada cinco minutos— es la más fácil de entender y toca batería y red a la vez. La tercera —guardar el resultado en vez de recalcular el reporte completo en cada consulta— es la que más sorprende, porque el estudiante todavía no tiene la intuición de que el cómputo cuesta energía; sirve para conectar con la sesión 7 y con la idea de que la eficiencia no es coquetería de programador. La cuarta —sostener dispositivos viejos— es la de mayor impacto real por lo dicho sobre la fabricación. Y la quinta es la más contemporánea y hay que decirla sin miedo: **agregarle un asistente de IA a una función que resolvía una condición simple gasta energía en cada llamada, para siempre**. Es una decisión de arquitectura, y hoy se toma con frecuencia por moda.

El método de cinco pasos es el del taller. El paso 2 —buscar lo que se repite— es el que enseña a estimar: lo que ocurre una vez no mueve la aguja, lo que ocurre mil veces al día sí. Y el paso 5 —definir un indicador medible— es el que separa una intención de una decisión de ingeniería. «Vamos a ser sostenibles» no se puede verificar; «vamos a mover menos de 200 KB por consulta» sí, y en la sesión 16 se puede mirar si se cumplió.

### Colombia, y la honestidad con las cifras - diapositivas 8 y 10

El dato local más útil es la composición de la matriz eléctrica. Una parte importante de la generación en Colombia es hidráulica, lo que significa que un kilovatio-hora consumido aquí tiene un factor de emisiones distinto —menor— que en un país con generación a carbón. La consecuencia metodológica es la que hay que enseñar: **no se copian factores de emisión de otro país**; se usa el factor local, y el operador del sistema (XM) publica datos de generación. Un equipo que cite una fuente colombiana en vez de un blog extranjero ya está haciendo ingeniería.

La contracara es igual de importante y menos conocida: cuando el fenómeno de El Niño reduce los aportes a los embalses, entran las plantas térmicas y el factor de emisiones del país sube. Es decir, **la misma aplicación, sin cambiar una línea de código, emite más en un año seco**. Eso enseña algo que vale para todo el curso: la huella de un sistema no es una propiedad del sistema, es una propiedad del sistema en su contexto.

La diapositiva de las trampas es la más importante para el rigor y conviene dedicarle tiempo real. Las cifras ambientales del sector digital son un campo donde circulan números espectaculares sin alcance definido: litros de agua por consulta a un modelo de lenguaje, gramos de CO₂ por búsqueda, porcentajes del consumo mundial de electricidad. Muchos provienen de estimaciones legítimas pero con supuestos muy específicos, y se citan luego como hechos universales. La regla del curso a partir de hoy es simple y se aplica en la rúbrica: **cifra con fuente, año y alcance, o no va**. Y hay que decir en voz alta lo que sí se puede afirmar sin exagerar: que la huella existe, que tiene cuatro etapas, que se puede reducir con decisiones de diseño y que casi nadie la mide. Con eso alcanza para trabajar con seriedad, y es mucho más defendible que un número impresionante mal citado.

Sobre la comparación «lo digital contra el papel»: alguien la va a proponer y la respuesta correcta es que depende del número de usos y de si obliga a comprar dispositivos. Un documento leído una vez en un computador nuevo no gana contra una hoja; el mismo documento leído por trescientas personas en aparatos que ya existen, sí. La lección es que **comparar sin decir qué se comparó no es un argumento**.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 5 - El rol del ingeniero en el contexto ambiental/Presentacion.pptx`. Las etiquetas [Slide N] del plan y las referencias del fundamento apuntan aquí.

1. Portada · Clase 5
2. Agenda de hoy (90 min)
3. Objetivos de la sesión
4. Pregunta de entrada
5. Las cuatro etapas de la huella de un sistema
6. Cuatro conceptos con nombre propio
7. La misma función, dos decisiones
8. Colombia: dos datos locales que cambian el análisis
9. Cómo se estima una huella sin ser experto
10. Dos trampas de esta clase
11. Taller de hoy: Huella del sistema
12. Cómo se expone en 3 minutos
13. Para la sesión 6
14. Cierre · Nos vemos en la sesión 6 — cierra el corte 1

## Plan de clase minuto a minuto (90 min)

### 00:00–00:10 · Apertura · [Slide 4]

Comparta pantalla antes de que entre el primero:

> «¿Dónde está la nube? ¿Y cuánta agua se bebió su última consulta a un asistente de IA?»

**[Nota docente]:** enlace del muro en el chat. Van a escribir «en internet», «en un servidor», «en Estados Unidos». Ninguna se corrige ahora.

**[Nota docente]:** si alguien escribe una cifra de agua, márquela: en el minuto 35 esa cifra es el mejor ejemplo de la diapositiva de las trampas.

### 00:10–00:55 · Teoría · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9][Slide 10]

Reparto sugerido de los 45 min:

- **9 min** · Las cuatro etapas [Slide 5]. Use un solo ejemplo (la app de citas) y recórralo por las cuatro. Detenga la clase en **fabricación**: la mayor parte de la huella de un celular ya está gastada al encenderlo.

- **9 min** · Los cuatro conceptos [Slide 6]. **Vuelva al muro** al explicar PUE y enfriamiento: ahí se responde «¿dónde está la nube?».

- **10 min** · La misma función, dos decisiones [Slide 7]. Es la diapositiva que convierte el tema en ingeniería. Diga explícitamente que la columna derecha **cumple la misma función**.

- **7 min** · Colombia [Slide 8]. Matriz hidráulica, El Niño y la Ley 1672 de 2013.

- **5 min** · Cómo se estima una huella [Slide 9]. Es el método del taller.

- **5 min** · Las dos trampas [Slide 10]. **No la recorte**: es la que sostiene el rigor de la sesión y de la rúbrica.

**[Nota docente]:** si el tiempo aprieta, recorte Colombia a cuatro minutos quedándose con la matriz hidráulica y la Ley 1672. La diapositiva de las dos decisiones y la de las trampas no se recortan.

### 00:55–01:12 · Taller en salas de grupo · [Slide 11]

**3 min** para abrir Excalidraw y repartir. Cada equipo trabaja **el sistema de su propio proyecto**, el que viene de las sesiones 1 y 3.

**14 min** de trabajo. Entre a las cinco salas, ~3 min cada una, y revise **una sola cosa: el indicador medible del paso 5**. Es donde se cae el taller.

**[Nota docente]:** la falla más común es proponer decisiones sobre el comportamiento del usuario («que apaguen el celular»). Corte eso en caliente: se piden decisiones **de diseño**, que están bajo control del equipo.

**[Nota docente]:** si aparece una cifra sin fuente, pídala en el momento. Si no la tienen, que la borren y escriban la afirmación sin número: se califica mejor una afirmación honesta que una cifra inventada.

### 01:12–01:27 · Exposiciones · [Slide 12]

5 equipos × 3 min con el diagrama compartido. **El minuto obligatorio es «la etapa que más pesa y por qué»**, y el cierre de cada exposición es el indicador.

**[Nota docente]:** los cinco enlaces (o los PNG) en el chat antes de arrancar.

**[Nota docente]:** anote los cinco indicadores. En la sesión 16 se revisa si se cumplieron, y tener la lista de hoy es lo que hace posible esa revisión.

### 01:27–01:30 · Cierre · [Slide 13][Slide 14]

Una idea: **el software no es inmaterial.** Tiene fabricación, consumo, red y residuo, y las decisiones que bajan la huella son decisiones de diseño, no de buena voluntad. La más fuerte que ellos pueden tomar es no obligar a cambiar de aparato.

Anuncie la sesión 6: **cierra el corte 1** y sale la ficha del problema del proyecto, con evaluación de corte en ExamLab al final de la sesión.

## Errores frecuentes y cómo cortarlos en caliente

| Lo que dice el equipo | Por qué no sirve | Qué pedir en su lugar |
|---|---|---|
| «La nube no contamina, es virtual» | La nube es un edificio con servidores, electricidad y enfriamiento, muchas veces con agua. | Que dibujen dónde está el servidor y qué se prende para que funcione. Y que nombren el PUE. |
| «Vamos a pedirle al usuario que ahorre energía» | No es una decisión de diseño: es comportamiento de otra persona, fuera de su control. | Algo que ellos puedan decidir en su propio sistema: cada cuánto consulta, cuánto pesa lo que envía, qué dispositivos soporta. |
| «Todas las etapas pesan igual» | Significa que no eligieron, y sin elegir no se puede actuar. | Una sola etapa y el argumento, aunque sea aproximado. |
| «Cada consulta a la IA gasta X litros de agua» | Las cifras que circulan varían por órdenes de magnitud y casi nunca dicen de qué sistema ni de qué año son. | Fuente, año y alcance. Si no lo tienen, que midan lo que sí pueden contar: el número de llamadas. |
| «Ser un sistema sostenible» como indicador | No tiene unidad y no se puede revisar en la sesión 16. | Un número con unidad, el valor de hoy y cómo se va a medir. |

## Dudas frecuentes del estudiante

**¿No es exagerado hablar de agua y minería en un curso de primer semestre?**

Es lo contrario: es el momento de decirlo, porque las decisiones que más pesan se toman al diseñar y ustedes están aprendiendo a diseñar. Y no se les pide militancia: se les pide saber que la huella existe, poder nombrar sus cuatro etapas y tomar dos decisiones que la bajen sin perder función.

**¿Y si nuestro proyecto casi no tiene huella?**

Entonces escríbanlo así, con el argumento, y les vale nota completa. Inflar el impacto ambiental de un formulario es tan malo como negar el de un centro de datos. Lo que se califica es el análisis, no el tamaño del problema.

**¿Dónde consigo el factor de emisiones de Colombia?**

El operador del sistema eléctrico (XM) publica datos de generación y composición de la matriz. Úsenlo con el año, y tengan presente que en años de El Niño el factor sube porque entran las térmicas. No copien un factor de otro país: el de Colombia es distinto por la generación hidráulica.

**¿Usar IA en el proyecto está mal ambientalmente?**

No está mal ni bien por sí solo: es una decisión con un costo. Lo que sí es un error de ingeniería es llamar a un modelo para algo que resuelve una condición simple, porque ese costo se paga en cada llamada, para siempre. Si su proyecto la usa, cuenten las llamadas: es lo único que pueden medir de verdad.

## Notas operativas

- Las cinco salas de grupo se crean **antes** de la sesión.
- Hoy **no se usa IA**: es la sesión donde más inventa cifras. Si un equipo la usa, verifique cualquier número contra una fuente con año.
- La falla más frecuente del taller es proponer **comportamiento del usuario** en vez de decisiones de diseño. Córtela en la primera sala, no en la calificación.
- **Anote los cinco indicadores** que salgan de las exposiciones. Se revisan en la sesión 16 y esta es la única oportunidad de tenerlos todos juntos.
- Si algún equipo pide fuentes, las útiles y verificables son: los datos de generación de XM para Colombia, la Ley 1672 de 2013 para RAEE, y el Global E-waste Monitor para residuos globales. Pida siempre el año de la edición.
- **Publique hoy** el documento «Evaluación del Corte 1 — cómo prepararse» (está con el material de la sesión 6) y dígalo en voz alta en el cierre. Trae la lista de qué repasar por sesión; entregarlo el mismo día de la evaluación no sirve de nada. Las preguntas y la clave están en el Kit docente de la sesión 6: **esos dos no se comparten**.

## Material de esta clase

- Deck: `Clases/Clase 5 - El rol del ingeniero en el contexto ambiental/Presentacion.pptx`
- Taller del estudiante: `Clases/Clase 5 - El rol del ingeniero en el contexto ambiental/Taller Clase 5 - Huella del sistema.docx`
- Solución del taller (**solo docente**): `Kit docente/Clase 5/Solucion Taller Clase 5 - Huella del sistema.docx`
- Este guion: `Kit docente/Clase 5/Guion Docente Clase 5 - El rol del ingeniero en el contexto ambiental.docx`

> **Recordatorio de datos personales:** ninguna actividad de este curso sube nombres, cédulas, teléfonos ni fotos de terceros. Si el caso del equipo los trae, se usa el rol («la dueña de la papelería», «el auxiliar de la biblioteca»).
