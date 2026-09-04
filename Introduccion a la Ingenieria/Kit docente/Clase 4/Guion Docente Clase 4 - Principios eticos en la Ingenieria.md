# Guion docente — Clase 4: Principios éticos en la Ingeniería

## Información de la clase
- Asignatura: Introducción a la Ingeniería (FI300101)
- Duración del bloque: **90 min**
- Tipo: Clase virtual sincrónica por Google Meet · Sesión 3 de 11 (sesión doble junto con la Clase 5) · corresponde al tema 4 del microcurrículo
- Modalidad: **Virtual (síncrona)** por Google Meet · actividades en plataformas gratuitas en la nube · los 5 equipos trabajan en **salas de grupo**
- Corte **1** (30%) · RAA: **RAA3**
- **Material general para los tres grupos** (SB141B, SB141C, LB141F): sin fechas ni horarios de reloj. El reloj de pared de cada grupo está en su `CALENDARIO_2026-2 - <GRUPO>.md`.
- Enfoque: Aprendizaje basado en competencia + Aprendizaje Invertido · Estrategia: ABPr — Aprendizaje Basado en Proyectos

## Objetivos de la clase
- Distinguir un **problema ético** de un problema técnico y de un problema legal.
- Usar los principios del **código de ética de ACM/IEEE** y de la **Ley 842 de 2003** para juzgar un caso.
- Nombrar **tres normas colombianas** que obligan al ingeniero de sistemas, y qué exige cada una.
- Identificar en un caso real **el momento en que se pudo parar** y quién tenía que hablar.

## Hoy avanzamos el proyecto en…

**Identificar a quién puede perjudicar el proyecto del equipo y qué norma colombiana lo obliga a cuidar eso — sobre todo si va a manejar datos de personas**

**Entregable concreto:** un acta de comité de cinco bloques en el documento del equipo, con al menos un numeral de código o de norma citado literalmente

**Herramientas de esta sesión:** Google Drive (Docs y Slides) · Padlet

> Hoy **no se usa asistente de IA**, y la razón es del tema: un caso ético se juzga leyendo el código de ética y los hechos, no pidiéndole una opinión a una herramienta que no responde por ella. El texto del código de ética de ACM/IEEE y el de la Ley 842 de 2003 se comparten en la carpeta del curso y **hay que citar el numeral**, no resumirlo de memoria.

## Fundamento teórico para el docente

Esta sección está escrita para dictar la clase **sin consultar otra fuente**, y va dividida por diapositiva: cada bloque dice a qué diapositiva corresponde.

### La pregunta de entrada: el ingeniero que fue a la cárcel - diapositiva 4

La apertura de hoy es un caso verdadero y conviene no revelar el nombre en el primer minuto, porque la fuerza está en la pregunta. Un ingeniero de Volkswagen escribió el software que detectaba cuándo el carro estaba en la prueba de emisiones para bajar los contaminantes solo durante el examen. El software funcionaba perfecto: hacía exactamente lo que se le pidió, sin errores. En 2017 ese ingeniero se declaró culpable en Estados Unidos y fue condenado a cuarenta meses de prisión, además de una multa.

El estudiante de primer semestre tiene interiorizada la idea de que la responsabilidad es del jefe y que el programador ejecuta. Este caso la rompe con un hecho verificable, y por eso es mejor abrir con él que con una definición de ética. Recoja las respuestas en el muro los primeros diez minutos —van a aparecer «robó», «hackeó», «se equivocó»— y en el minuto 30, cuando llegue al caso en la tabla, muestre que ninguna era: **no hubo error, no hubo robo, hubo una decisión de diseño que se ejecutó bien**.

### Qué es la ética en una profesión y qué no es - diapositiva 5

Hay tres confusiones que hay que desmontar antes de tocar cualquier caso, porque si no, la discusión del taller se vuelve una conversación de opiniones y no se puede calificar.

**La primera: la ética profesional no es tener buenas intenciones.** Es tomar decisiones defendibles con información incompleta y poder explicar el criterio. Un ingeniero con excelentes intenciones que no preguntó a quién afecta su sistema hizo algo mal, y el resultado no mejora por su buena voluntad. Al revés, un ingeniero que detecta un riesgo y lo escribe está actuando bien aunque el proyecto igual salga mal.

**La segunda: no es un tema de opinión.** Esta es la que más rinde en clase, porque el estudiante llega convencido de que en ética «cada uno piensa distinto». Existen códigos escritos, con principios numerados, que uno puede citar como se cita un artículo de una norma. El código de ética de ACM e IEEE Computer Society para ingeniería de software es de 1999 y tiene ocho principios; el código de ética del ingeniero en Colombia es la Ley 842 de 2003. Un veredicto que cita el numeral es un argumento; «a mí me parece que estuvo mal» no lo es. En el taller de hoy se califica exactamente esa diferencia.

**La tercera: la ley es el piso, no el techo.** El caso de Cambridge Analytica es el mejor para mostrarlo: la interfaz que permitía a una aplicación tomar datos de los amigos del usuario estaba documentada públicamente y era permitida por las reglas de la plataforma. Era legal y es indefendible. Al revés también ocurre: algo puede ser éticamente correcto y estar prohibido por una política interna. La ley y la ética se cruzan pero no coinciden, y el ingeniero tiene que mirar las dos.

Una cuarta idea, que es la que más les sirve: **el momento de la ética es el momento de decidir, y casi siempre es temprano**. Quitar un seguro físico de una máquina de radioterapia porque el software ya lo cubre es una decisión que cuesta una reunión; enterarse de las consecuencias cuesta vidas y una investigación de años. La ética no es lo que se hace después del desastre.

### Los códigos y las tres normas colombianas que hay que saber nombrar - diapositiva 6

**ACM/IEEE, 1999.** Ocho principios en este orden: público, cliente y empleador, producto, juicio, gestión, profesión, colegas y sí mismo. El orden importa y hay que decirlo en voz alta: el principio 1 —actuar de forma consistente con el interés público— **está por encima** del principio 2, que es el cliente y el empleador. Eso significa que el código ya resolvió el conflicto que el estudiante cree irresoluble: si lo que pide el jefe daña al público, el código dice cuál gana. La ACM actualizó además su código general en 2018.

**Ley 842 de 2003.** Es el código de ética profesional de la ingeniería en Colombia y es la que aplica aquí, no las de otros países. Establece los deberes del ingeniero con la sociedad, con la profesión, con sus colegas y con sus clientes, y define las faltas y las sanciones. El punto práctico que hay que aterrizar para un estudiante de primer semestre es la **matrícula profesional**: en Colombia el ejercicio de la ingeniería requiere matrícula, la expide el COPNIA —Consejo Profesional Nacional de Ingeniería—, y el COPNIA puede sancionar y suspenderla. Es decir, la ética profesional aquí no es un discurso: tiene una autoridad, un procedimiento y una consecuencia sobre el derecho a ejercer.

**Ley 1581 de 2012** (con el Decreto 1377 de 2013) es la de protección de datos personales, y es la norma que más van a tocar en su vida laboral, empezando por el proyecto de este curso. Los principios que hay que poder nombrar: finalidad (los datos se piden para algo declarado y no se usan para otra cosa), libertad (hace falta autorización previa, expresa e informada), veracidad, transparencia, acceso restringido, seguridad y confidencialidad. Los **datos sensibles** —salud, biometría, orientación política, sexual o religiosa, datos de niños— tienen protección reforzada. La autoridad es la Superintendencia de Industria y Comercio. Aterrícelo en el curso: si un equipo quiere hacer un proyecto con una base de datos de pacientes de un consultorio del barrio, esta ley le aplica completa, y por eso el curso prohíbe subir nombres y cédulas.

**Ley 1273 de 2009** agregó al Código Penal un título sobre la protección de la información y los datos: acceso abusivo a un sistema informático, obstaculización ilegítima, interceptación de datos, daño informático, hurto por medios informáticos. La diferencia con la anterior hay que subrayarla: aquí la consecuencia es **pena de prisión para la persona**, no una sanción administrativa a la empresa. Es la norma que convierte en delito lo que un estudiante puede considerar una travesura —entrar a un sistema ajeno «solo para probar»— y conviene decirlo hoy, en la sesión 4, y no cuando ya pasó.

### Los cuatro casos: qué contar de cada uno y cuál es el momento de parar - diapositiva 7

**Therac-25 (1985–1987).** Máquina de radioterapia de la Atomic Energy of Canada Limited. Seis accidentes conocidos con sobredosis masivas de radiación y varios muertos. Las causas son de manual y hay que contarlas completas porque son técnicas: los modelos anteriores tenían **seguros físicos** que impedían mecánicamente una configuración peligrosa, y en el Therac-25 se quitaron confiando en que el software lo evitaría; el software venía reutilizado de los modelos anteriores, con errores que antes quedaban tapados por esos seguros; había una condición de carrera que se disparaba cuando la operadora corregía la pantalla muy rápido, algo que hacían las operadoras expertas; los mensajes de error eran crípticos («MALFUNCTION 54») y aparecían tan seguido que se ignoraban; nunca hubo revisión independiente del código; y el fabricante sostuvo al principio que la sobredosis era imposible. La investigación de Nancy Leveson y Clark Turner (1993) es la fuente canónica y está disponible. **El momento de parar** fue la decisión de quitar los seguros físicos: ahí, en una reunión de diseño, era gratis.

**Volkswagen (2015).** El «defeat device»: software que reconocía las condiciones de la prueba de laboratorio y activaba el control de emisiones solo en ese momento. En circulación real el vehículo emitía óxidos de nitrógeno muy por encima del límite. Se descubrió en 2015 y el detalle que interesa aquí es judicial: el ingeniero James Liang se declaró culpable y fue condenado en 2017 a cuarenta meses de prisión y una multa; un directivo recibió una pena mayor. **El momento de parar** fue cuando le pidieron escribir la detección de la prueba: no hacía falta ser experto en emisiones para ver que un código cuyo propósito es comportarse distinto durante el examen existe para engañar.

**Boeing 737 MAX (2018–2019).** El MCAS empujaba el morro hacia abajo con base en **un solo sensor de ángulo de ataque**, podía activarse repetidamente, y no estaba explicado en el manual de vuelo, así que los pilotos no sabían que existía. Dos accidentes —Lion Air 610 en octubre de 2018 y Ethiopian 302 en marzo de 2019— con 346 muertos en total, y la flota mundial en tierra. Un detalle que vale oro para una clase de ingeniería: la alerta que avisaba de la discrepancia entre sensores era una **opción de pago**. **El momento de parar** fue la decisión de arquitectura de depender de un sensor único en un sistema capaz de mover el avión, y la de no documentarlo para no obligar a reentrenar pilotos.

**Cambridge Analytica (2018).** Una aplicación de cuestionarios recogía datos del usuario **y de sus amigos**, que nunca la instalaron ni supieron de ella, aprovechando una interfaz de la plataforma que lo permitía. Los datos de decenas de millones de personas terminaron en perfilamiento político. La consecuencia fue una multa histórica a la plataforma. **El momento de parar** fue el diseño de esa interfaz: alguien decidió que el consentimiento de una persona alcanzara para entregar los datos de sus contactos. Es el caso que conecta directo con la Ley 1581 y con el principio de finalidad.

El hilo común hay que enunciarlo al final de la tabla: **en los cuatro casos el software funcionó**. No hubo un error de programación que causara el desastre —salvo parcialmente en Therac-25, y ahí el error existía desde antes y estaba tapado por un seguro que alguien decidió quitar—. Lo que falló fue lo que se pidió construir y el hecho de que nadie con información suficiente lo detuvo. Esa frase es la tesis de la clase.

### La defensa que no sirve y las cinco preguntas que sí - diapositivas 8 y 9

«Yo solo programé lo que me pidieron» es la frase que el estudiante va a usar espontáneamente en el taller, y hay que desarmarla con hechos en vez de con moralina. Legalmente no funciona: el caso Volkswagen tiene un ingeniero condenado a prisión por ejecutar. Profesionalmente tampoco: el código ACM/IEEE pone el interés público por encima del empleador, así que el conflicto ya está resuelto en el texto.

Pero la parte útil no es la condena, es la alternativa, y conviene enseñarla en términos prácticos porque el estudiante que salga a trabajar el próximo año la va a necesitar: **dejar rastro y escalar temprano**. Un correo corto que diga «esto que se me pide tiene este riesgo para estas personas, lo dejo por escrito y propongo esta alternativa» hace tres cosas: aumenta la probabilidad de que se corrija, obliga a quien decide a decidir de verdad, y protege a quien lo escribió. Hay que decirlo sin heroísmo: no se le está pidiendo a un practicante que renuncie, se le está pidiendo que no sea el único que sabe. La única postura que no tiene defensa posible es callar.

Las cinco preguntas son el método del taller. La más potente es la tercera —«¿aguanta que se sepa?»— porque no requiere saber nada de códigos ni de leyes y descarta la mayoría de las malas ideas en diez segundos: si la decisión depende de que los afectados no se enteren, ya está juzgada. La cuarta —buscar el numeral— es la que convierte una intuición en un argumento profesional, y es la que más pesa en la rúbrica. Y la quinta —¿cuándo se pudo parar?— es la que le da a la clase valor de ingeniería y no de conferencia: en los cuatro casos hubo un momento temprano, identificable y barato, en el que una persona con la información suficiente podía cambiar el resultado.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 4 - Principios eticos en la Ingenieria/Presentacion.pptx`. Las etiquetas [Slide N] del plan y las referencias del fundamento apuntan aquí.

1. Portada · Clase 4
2. Agenda de hoy (90 min)
3. Objetivos de la sesión
4. Pregunta de entrada
5. Tres cosas que se confunden
6. Los principios que sí están escritos
7. Cuatro casos donde el software funcionó
8. «Yo solo programé lo que me pidieron»
9. Cinco preguntas para decidir sin ser experto
10. Taller de hoy: Comité de ética
11. Cómo se expone en 3 minutos
12. Para la Clase 5
13. Cierre · Nos vemos en la sesión 5

## Plan de clase minuto a minuto (90 min)

### 00:00–00:10 · Apertura · [Slide 4]

Comparta pantalla antes de que entre el primero:

> «Un ingeniero escribió el código que le pidieron, funcionó perfecto, y terminó en la cárcel. ¿Cómo llega alguien ahí?»

**[Nota docente]:** no diga todavía que es Volkswagen. Recoja las respuestas en el muro; van a aparecer «robó», «hackeó», «se equivocó». Ninguna es correcta y ese es el punto.

**[Nota docente]:** hoy hay lectura previa (el código de ética). Verifique en el chat quién lo abrió: el taller se cae sin ese texto a mano.

### 00:10–00:55 · Teoría · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]

Reparto sugerido de los 45 min:

- **8 min** · Tres cosas que se confunden [Slide 5]. Insista en la segunda: **hay códigos escritos y se citan por numeral**. De eso depende que el taller sea evaluable y no una tertulia.

- **10 min** · Los principios y las tres normas [Slide 6]. En ACM/IEEE, diga que el orden importa: el público está antes que el empleador. En Colombia, mencione la matrícula del COPNIA: la ética aquí tiene autoridad y consecuencia.

- **16 min** · Los cuatro casos [Slide 7], unos 4 min cada uno. Therac-25 completo; en Volkswagen revele que este era el de la apertura y **vuelva al muro**.

- **6 min** · «Yo solo programé lo que me pidieron» [Slide 8]. La parte importante es la salida práctica: dejar rastro y escalar temprano.

- **5 min** · Las cinco preguntas [Slide 9]. Es el método del taller.

**[Nota docente]:** si el tiempo aprieta, recorte Cambridge Analytica y 737 MAX a dos minutos. **Therac-25 y Volkswagen no se recortan**: uno da el argumento técnico y el otro el argumento legal.

### 00:55–01:12 · Taller en salas de grupo · [Slide 10]

**2 min** para repartir casos: un caso por equipo, asignado por número de equipo. El quinto equipo recibe un caso local en vez de uno famoso (está en el taller), porque hace falta que al menos uno juzgue algo que podría pasarles a ellos.

**15 min** en salas. Entre a las cinco, ~3 min cada una, y revise **una sola cosa: que haya un numeral citado**. Un veredicto sin numeral es una opinión y no puntúa el bloque más pesado.

**[Nota docente]:** el error que hay que cortar en caliente es el veredicto genérico («actuaron con negligencia»). Pida el sujeto: **quién** decidió, en qué momento y qué información tenía.

**[Nota docente]:** cuando alguien diga «pero le habrían echado del trabajo», no lo descarte: es la objeción honesta. Responda con lo que sí se le pide —dejar rastro y escalar— y con lo que le pasó a quien no lo hizo.

### 01:12–01:27 · Exposiciones · [Slide 11]

5 equipos × 3 min, vocero con la pantalla ya compartida. **El minuto obligatorio de hoy es «el momento en que se pudo parar»**: sin eso la exposición es un resumen de noticia.

**[Nota docente]:** los cinco enlaces en el chat antes de arrancar.

**[Nota docente]:** anote qué numeral citó cada equipo. Si tres equipos citaron el principio 1 del código ACM/IEEE, dígalo en el cierre: es la señal de que el interés público es el principio que resuelve la mayoría de los casos.

### 01:27–01:30 · Cierre · [Slide 12][Slide 13]

Una idea: **en los cuatro casos el software funcionó.** Falló lo que se pidió construir y el hecho de que nadie lo detuvo. La ética profesional es la decisión temprana, no el arrepentimiento posterior.

Anuncie la sesión 5: hoy se vio el daño a personas; la próxima, el daño que no tiene una víctima con nombre y que casi nadie mide — el ambiental.

## Errores frecuentes y cómo cortarlos en caliente

| Lo que dice el equipo | Por qué no sirve | Qué pedir en su lugar |
|---|---|---|
| «La empresa actuó con negligencia» | «La empresa» no decide: deciden personas con un cargo, y sin sujeto el caso no enseña nada. | Quién tomó la decisión (el rol), en qué momento y con qué información. |
| «El culpable fue el programador que dejó el error» | En los cuatro casos el software hizo lo que se le pidió; el error, cuando existió, era inofensivo hasta que alguien quitó la barrera. | La decisión de diseño o de negocio que convirtió el error en daño. |
| «El código de ética dice que hay que ser responsable» | Eso no está en ningún numeral; es una paráfrasis vacía y no puntúa el bloque más pesado. | El número del principio o del artículo y la cita literal del texto compartido. |
| «Debieron probar mejor el software» | Es correcto y es tardío: no toca la decisión que creó el riesgo. | El momento más temprano en que alguien pudo cambiar el resultado, y qué debía hacer ahí. |
| «Si era legal, no hay problema ético» | Cambridge Analytica era legal según las reglas de la plataforma y es indefendible. | Que apliquen la pregunta 3: ¿aguanta que se sepa? Y que digan quién quedó sin saber. |

## Dudas frecuentes del estudiante

**¿Y si me despiden por negarme?**

Es la objeción honesta y no se le va a responder con heroísmo. Lo que el curso le pide no es renunciar ni denunciar: es **dejar rastro y escalar temprano**. Un correo que diga «esto tiene este riesgo para estas personas, lo dejo por escrito» hace que decida quien tiene la autoridad, sabiendo. Y le recuerdo el dato de Volkswagen: quien ejecutó calladamente fue a prisión, y eso también le cuesta el trabajo.

**¿Un estudiante de primer semestre ya tiene responsabilidad profesional?**

Legalmente la matrícula profesional viene después del título. Pero la Ley 1581 de 2012 y la Ley 1273 de 2009 le aplican **hoy**, como a cualquier persona: si sube datos de pacientes a un enlace público en el proyecto de este curso, eso ya es un problema real, no un ejercicio.

**¿Los códigos de ética tienen fuerza legal en Colombia?**

El de ACM/IEEE no: es un compromiso profesional internacional, y su fuerza está en que es el estándar que la profesión reconoce. La **Ley 842 de 2003** sí es ley colombiana, y el COPNIA puede sancionar y suspender la matrícula profesional con base en ella. Las leyes 1581 y 1273 tienen consecuencias directas: sanciones administrativas la primera, penales la segunda.

**¿En el proyecto del curso podemos usar datos reales de personas?**

No. Ni nombres, ni cédulas, ni teléfonos, ni fotos de terceros: se usa el rol. Si su proyecto necesita datos para funcionar, se inventan datos de prueba. Esa regla es la Ley 1581 de 2012 aplicada a su trabajo, y es la primera cosa que se revisa en el informe final.

## Notas operativas

- Comparta el **texto del código ACM/IEEE y el de la Ley 842 de 2003** en la carpeta del curso antes de la sesión. Sin el texto a mano, el bloque del numeral —30 % de la nota— no se puede hacer y el taller se convierte en opinión.
- El caso del equipo 5 (el local, de datos de salud en un enlace público) **no se cambia**: es el que amarra la clase al proyecto del semestre y a la regla de datos personales del curso.
- Si un equipo trae una cifra de muertos o de multas, pida la fuente y el año. Los números de estos casos circulan con variaciones.
- Al calificar, sea estricto con la **cita literal**. Un resumen del principio, aunque sea correcto, no vale igual: la habilidad que se está formando es citar la norma que obliga.
- Esta sesión no usa asistente de IA. Si un equipo lo usa, la falla típica es un numeral **inventado**: el asistente cita artículos que no existen con total naturalidad. Verifique cualquier numeral contra el texto compartido.

## Material de esta clase

- Deck: `Clases/Clase 4 - Principios eticos en la Ingenieria/Presentacion.pptx`
- Taller del estudiante: `Clases/Clase 4 - Principios eticos en la Ingenieria/Taller Clase 4 - Comite de etica.docx`
- Solución del taller (**solo docente**): `Kit docente/Clase 4/Solucion Taller Clase 4 - Comite de etica.docx`
- Este guion: `Kit docente/Clase 4/Guion Docente Clase 4 - Principios eticos en la Ingenieria.docx`

> **Recordatorio de datos personales:** ninguna actividad de este curso sube nombres, cédulas, teléfonos ni fotos de terceros. Si el caso del equipo los trae, se usa el rol («la dueña de la papelería», «el auxiliar de la biblioteca»).
