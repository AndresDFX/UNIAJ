# Guion docente — Clase 7: Ciclo de vida de los proyectos de ingeniería

## Información de la clase
- Asignatura: Introducción a la Ingeniería (FI300101)
- Duración del bloque: **90 min**
- Tipo: Clase virtual sincrónica por Google Meet · Sesión 5 de 11 (sesión doble junto con la Clase 8) · corresponde al tema 7 del microcurrículo
- Modalidad: **Virtual (síncrona)** por Google Meet · actividades en plataformas gratuitas en la nube · los 5 equipos trabajan en **salas de grupo**
- Corte **2** (30%) · RAA: **RAA3**
- **Material general para los tres grupos** (SB141B, SB141C, LB141F): sin fechas ni horarios de reloj. El reloj de pared de cada grupo está en su `CALENDARIO_2026-2 - <GRUPO>.md`.
- Enfoque: Aprendizaje basado en competencia + Aprendizaje Invertido · Estrategia: ABPr — Aprendizaje Basado en Proyectos

## Objetivos de la clase
- Nombrar las **fases del ciclo de vida** de un proyecto y qué se entrega en cada una.
- Explicar por qué **el costo de corregir un error crece** con la fase en que se descubre.
- Distinguir un **requisito funcional** de uno **no funcional**, y escribir su criterio de aceptación.
- Ubicar el proyecto del equipo en una fase y decir **qué falta para cerrarla**.

## Hoy avanzamos el proyecto en…

**Escribir los requisitos mínimos del proyecto con su criterio de aceptación, y el plan de hitos hasta la exposición final**

**Entregable concreto:** el mapa del ciclo de vida del proyecto en draw.io (PNG en la carpeta del equipo) más la tabla de requisitos y el plan de hitos en el documento del equipo

**Herramientas de esta sesión:** diagrams.net (draw.io) · Canva

> El mapa del ciclo de vida se hace en **diagrams.net (draw.io)**, que abre sin cuenta y guarda en la carpeta del equipo. La tabla de requisitos va en el **documento del equipo**. Hoy no se usa IA: los requisitos tienen que salir de la ficha del problema de la sesión 6, y un asistente los devuelve genéricos y sin las restricciones del caso.

## Fundamento teórico para el docente

Esta sección está escrita para dictar la clase **sin consultar otra fuente**, y va dividida por diapositiva: cada bloque dice a qué diapositiva corresponde.

### La pregunta de entrada: la curva del costo del cambio - diapositiva 4

La analogía de la pared es la más eficiente que existe para esta clase porque nadie necesita saber de software para responderla. Mover una pared en el plano cuesta un borrador; en el ladrillo cuesta tumbar y volver a levantar; en la casa entregada cuesta la obra, la mudanza y el enojo del dueño. Todo el mundo lo intuye, y esa intuición es exactamente la curva del costo del cambio.

Lo que hay que hacer explícito en el minuto 12 es que **en software la curva es igual pero se ve menos**, y ahí está el problema. En una casa, una pared mal puesta se ve; en un sistema, un requisito mal entendido no se ve hasta que alguien lo usa. Por eso en ingeniería de software hubo que inventar fases, revisiones y criterios de aceptación: son el equivalente a mirar el plano antes de pedir el cemento.

Recoja las respuestas en el muro. Van a salir cifras espontáneas —«mil veces más caro»— y conviene no corregirlas ahí, sino usarlas cuando llegue la tabla: la dirección de la curva es correcta y los múltiplos exactos son discutibles, lo cual es una buena lección sobre cómo se citan los datos.

### Las seis fases, y por qué el orden importa - diapositiva 5

Conviene presentar las fases como una cadena de preguntas, no como una lista de etapas administrativas. Cada fase responde una pregunta y produce lo que la siguiente necesita para no adivinar.

**Definición del problema** responde *qué se va a resolver y para quién*, y hay que decir en voz alta que **esa fase ya la hicieron en la sesión 6**: la ficha del problema es el entregable de la primera fase del ciclo de vida de su propio proyecto. Eso reordena la percepción del curso: no estaban haciendo un ejercicio, estaban cerrando una fase.

**Requisitos** responde *qué tiene que hacer la solución para resolver eso, y cómo sabremos que lo hace*. Es la fase de hoy y la que más se salta la gente.

**Diseño** responde *cómo va a estar construido*: las partes, el flujo, las pantallas o los pasos. **Construcción** es la única fase que el estudiante reconoce como «el proyecto», y vale la pena decirle que es una de seis, y no la más determinante. **Validación** responde *funciona contra los criterios y con el usuario real*; la trampa clásica es probar con el propio equipo, que ya sabe cómo se usa. Y **operación y retiro** es la fase que nadie enseña en primer semestre y que conviene nombrar por dos razones: la mayor parte de la vida de un sistema ocurre ahí, y el retiro —qué pasa con los datos cuando el sistema se apaga— es un asunto ético y legal que ya vieron en la sesión 4 con la Ley 1581.

El punto que amarra todo: **el orden no es burocracia, es economía**. Cada fase existe porque descubrir un error en ella cuesta menos que descubrirlo en la siguiente. Quien se salta requisitos no ahorra tiempo: mueve el costo hacia adelante y lo multiplica.

### La curva del costo del cambio: qué se puede afirmar y qué no - diapositiva 6

Esta tabla es el corazón cuantitativo de la sesión y hay que manejarla con el mismo rigor que se les exigió en la sesión 5 con las cifras ambientales. **Lo que se puede afirmar con seguridad: el costo de corregir un error crece con la fase en que se descubre, y crece por órdenes de magnitud entre los extremos.** La forma de esa curva la documentó Barry Boehm en los años setenta a partir de datos de proyectos reales, y se ha vuelto a medir muchas veces desde entonces.

**Lo que no conviene afirmar: los múltiplos exactos.** Circulan tablas con «1× / 5× / 10× / 100×» presentadas como leyes de la naturaleza, y hay literatura que discute si en desarrollo iterativo la curva es tan pronunciada. Diga eso explícitamente en clase: es una oportunidad de oro para mostrar que un ingeniero puede usar un resultado clásico sin exagerarlo. La dirección de la curva no está en discusión; la pendiente sí.

El uso práctico de la tabla es una pregunta que los equipos van a responder en el taller: *¿qué decisión que estamos tomando hoy sería carísima cambiar en la Clase 14?* Casi siempre la respuesta es un requisito mal entendido o una restricción ignorada, y hacer la pregunta hoy es lo que la vuelve barata.

Hay un segundo uso, más sutil, que vale la pena señalar si el grupo responde bien: la curva explica por qué las revisiones tempranas —que se sienten como pérdida de tiempo porque todavía no hay nada construido— son la actividad más rentable del proyecto. En el Therac-25 de la sesión 4, la revisión independiente del software que nunca se hizo era justamente eso.

### Cascada, iterativo, y lo que Royce dijo de verdad - diapositiva 7

En la sesión 2 apareció Royce y su artículo de 1970. Hoy se cierra el punto, porque es una de las confusiones más extendidas de la profesión: **el diagrama de cascada de una sola pasada suele atribuirse a Royce como su propuesta, y en el mismo texto él lo presentó como el modo riesgoso y advirtió que hacerlo así invita al fracaso**. Su propuesta incluía volver atrás, prototipar y hacer el trabajo dos veces. La profesión se quedó con el dibujo y perdió la advertencia.

La comparación que importa para el curso no es «cascada mala, ágil bueno» —esa es una caricatura y hay que evitarla—. Es esta: **las fases son las mismas en los dos; lo que cambia es cuántas veces se recorren y cuándo aparece el usuario**. La cascada de una pasada es razonable cuando el problema es conocido, estable y el costo de equivocarse al final es asumible. El enfoque iterativo es mejor cuando hay incertidumbre sobre qué necesita el usuario, que es la situación normal y en particular la de todos los proyectos de este curso.

Aterrícelo en el calendario, porque eso les hace sentir la diferencia: **este curso va a hacer dos vueltas completas**. Una corta en las sesiones 10 y 11 —prototipo de baja fidelidad, prueba, corrección— y otra en las Clases 12 a 14, con la retroalimentación de la presentación de avances. No es una decisión estética del docente: es la manera de que el error de requisitos aparezca en la sesión 10 y no en la 15, cuando ya no hay tiempo.

Si alguien pregunta por el Manifiesto Ágil de 2001, que salió en la sesión 2: la respuesta honesta es que reordenó prioridades —software funcionando sobre documentación, colaboración sobre contrato— y que no eliminó las fases. Un equipo ágil sigue definiendo el problema, escribiendo requisitos, diseñando, construyendo y validando; lo hace en ciclos cortos y con menos ceremonia.

### Requisitos, criterios de aceptación y hitos: lo que se entrega hoy - diapositivas 8 y 9

**Requisito funcional** es algo que la solución hace, escrito desde el usuario: «el usuario puede consultar si un libro está disponible sin ir a la biblioteca». El error típico de primer semestre es escribirlo desde la tecnología —«el sistema tendrá una base de datos MySQL»—, que no es un requisito sino una decisión de diseño disfrazada, y encima toma la decisión en la fase equivocada.

**Requisito no funcional** es una condición que la solución debe cumplir: funcionar en un computador viejo, abrir sin crear cuenta, responder en menos de tanto, no guardar datos personales. Aquí hay una conexión que hay que hacer explícita y que le da sentido a dos sesiones anteriores: **los requisitos no funcionales de sus proyectos salen de las restricciones que marcaron en el árbol de la sesión 6 y del indicador ambiental de la sesión 5**. Si la biblioteca no tiene computador en el mostrador, «funciona desde el celular de la voluntaria» es un requisito no funcional, no un detalle.

**Criterio de aceptación** es la parte que casi nadie escribe y la que vuelve verificable el proyecto: cómo se comprueba que el requisito se cumple, con un caso concreto y un umbral. «Un usuario que no conoce el sistema encuentra la disponibilidad de un libro en menos de un minuto, sin ayuda» se puede ejecutar delante de alguien. «El sistema debe ser fácil de usar» no se puede ejecutar, y por lo tanto no sirve. La regla que conviene dictar: **si no se puede convertir en una prueba que alguien haga, no es un criterio**.

**Hito** es un punto del calendario donde algo queda terminado y verificable. Es el concepto que salva el proyecto de la última semana: «vamos avanzando» no es un hito; «en la sesión 10 hay tres pantallas probadas con un usuario» sí. En el taller de hoy se les pide el plan de hitos hasta la Clase 15, y conviene revisarlo con severidad, porque un plan con todo el trabajo en la Clase 14 es un proyecto que va a fallar y todavía se puede corregir.

Los tres malentendidos de la última diapositiva son los que aparecen en las salas. El primero —que las fases son burocracia— se responde con la tabla del costo. El segundo —que iterativo significa no planear— se responde señalando que se planea más seguido, no menos. El tercero conviene decirlo porque tranquiliza: **las fases no son departamentos ni personas**; en un equipo de cinco, las seis fases las recorren los mismos cinco, y lo que cambia es la pregunta que están respondiendo.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 7 - Ciclo de vida de los proyectos de ingenieria/Presentacion.pptx`. Las etiquetas [Slide N] del plan y las referencias del fundamento apuntan aquí.

1. Portada · Clase 7
2. Agenda de hoy (90 min)
3. Objetivos de la sesión
4. Pregunta de entrada
5. Las seis fases del ciclo de vida
6. Lo que cuesta cambiar en cada fase
7. Una sola pasada o varias vueltas
8. Cuatro cosas que se entregan y no son código
9. Tres malentendidos que salen caros
10. Taller de hoy: Ciclo de vida del proyecto
11. Cómo se expone en 3 minutos
12. Para la Clase 8
13. Cierre · Nos vemos en la sesión 8

## Plan de clase minuto a minuto (90 min)

### 00:00–00:10 · Apertura · [Slide 4]

Comparta pantalla antes de que entre el primero:

> «¿Cuánto cuesta mover una pared? Depende de si está en el plano, en el ladrillo o en la casa ya entregada.»

**[Nota docente]:** enlace del muro en el chat. Van a aparecer cifras inventadas («mil veces más»). No las corrija: úselas en el minuto 25 con la tabla.

**[Nota docente]:** pida que abran la **ficha del problema de la sesión 6**. Todo el taller de hoy cuelga de ella; sin ficha no hay requisitos.

### 00:10–00:55 · Teoría · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]

Reparto sugerido de los 45 min:

- **9 min** · Las seis fases [Slide 5]. Diga explícitamente que **la fase 1 ya la cerraron en la sesión 6**: eso reordena cómo ven el curso.

- **10 min** · La curva del costo [Slide 6]. Vuelva al muro. Sea honesto con las cifras: la dirección de la curva no se discute, los múltiplos sí.

- **9 min** · Una sola pasada o varias vueltas [Slide 7]. Cierre el punto de Royce de la sesión 2 y anuncie las **dos vueltas** de este curso (10–11 y 12–14).

- **12 min** · Cuatro cosas que se entregan [Slide 8]. Es la más operativa: de aquí sale el taller. Insista en que **los requisitos no funcionales salen de las restricciones del árbol de la sesión 6**.

- **5 min** · Tres malentendidos [Slide 9].

**[Nota docente]:** si va retrasado, recorte los malentendidos a dos minutos. **No recorte la diapositiva de requisitos y criterios**: sin ella el taller no se puede hacer.

### 00:55–01:12 · Taller en salas de grupo · [Slide 10]

**2 min** para abrir draw.io y el documento del equipo. Cada equipo trabaja su propio proyecto.

**15 min** en salas. Entre a las cinco, ~3 min cada una, con **una sola pregunta: ¿cómo se comprueba ese requisito?** El criterio de aceptación es lo que falta siempre.

**[Nota docente]:** el error a cortar en caliente es el requisito escrito desde la tecnología («el sistema tendrá una base de datos»). Pregunte «¿y eso qué le permite hacer al usuario?» y reescríbalo con ellos.

**[Nota docente]:** revise el plan de hitos con severidad. Si todo el trabajo cae en la Clase 14, dígalo ahora: es un proyecto que va a fallar y todavía hay nueve sesiones para arreglarlo.

### 01:12–01:27 · Exposiciones · [Slide 11]

5 equipos × 3 min con el diagrama compartido. **El minuto obligatorio es «en qué fase estamos y qué falta para cerrarla»**.

**[Nota docente]:** los cinco enlaces en el chat antes de arrancar.

**[Nota docente]:** anote la fase declarada por cada equipo y su hito de la sesión 10. En la sesión 10 se verifica contra eso, y es la manera más simple de detectar a un equipo atrasado antes de que sea tarde.

### 01:27–01:30 · Cierre · [Slide 12][Slide 13]

Una idea: **el orden de las fases no es burocracia, es economía.** El error barato es el que se encuentra temprano, y por eso hoy escribieron requisitos en vez de empezar a construir.

Anuncie la sesión 8: se aplica esto a **casos reales de proyectos que se saltaron una fase**, y cada equipo decide entre sus dos alternativas de solución.

## Errores frecuentes y cómo cortarlos en caliente

| Lo que dice el equipo | Por qué no sirve | Qué pedir en su lugar |
|---|---|---|
| «El sistema tendrá una base de datos con los libros» | No es un requisito: es una decisión de diseño tomada dos fases antes de tiempo, y cierra opciones sin argumento. | «¿Y eso qué le permite hacer al usuario?». Reescríbalo empezando por el actor, y anote la decisión técnica aparte para la sesión 8. |
| «El sistema debe ser fácil de usar» | No se puede convertir en una prueba que alguien ejecute, así que no se puede validar. | Un actor, una acción, una condición y un umbral: «una persona que no lo conoce logra X en menos de Y, sin ayuda». |
| «Estamos en construcción» sin requisitos escritos | Es construir para rehacer: el error de requisitos descubierto en construcción cuesta decenas de veces más. | Los requisitos por escrito primero. Lo ya construido no se tira: se usa como prototipo de la sesión 10. |
| «Debe ser escalable / usar la nube» como requisito no funcional | No sale de ninguna restricción del proyecto: entró por moda y no por análisis. | Que señalen la restricción del árbol de la sesión 6 de donde sale cada requisito no funcional. |
| Un plan con todo el trabajo en la Clase 14 | Es el patrón exacto de los proyectos que no se entregan, y desperdicia la retroalimentación gratis de la Clase 12. | Un hito verificable en la Clase 10, aunque sea mínimo. La Clase 14 se reserva para ensayar, no para construir. |

## Dudas frecuentes del estudiante

**¿Tenemos que seguir cascada o ágil?**

Ninguna de las dos como dogma. Las fases son las mismas; lo que cambia es cuántas veces se recorren. Este curso va a hacer **dos vueltas**: una corta en las sesiones 10 y 11, otra en las 12 a 14. Es iterativo, y por eso hay requisitos escritos: iterar sin requisitos no es ágil, es improvisar.

**¿Cuántos requisitos hay que tener?**

Hoy, cinco: tres funcionales y dos no funcionales. Y es a propósito. Un proyecto de primer semestre con veinte requisitos no cumple ninguno; con cinco bien escritos y con criterio de aceptación se puede demostrar en la Clase 16 que funcionan. Se califica que sean verificables, no que sean muchos.

**¿Y si el usuario cambia de opinión después?**

Va a pasar, y no es una falla del usuario: es la razón de ser del enfoque iterativo. Por eso el prototipo de la sesión 10 es de baja fidelidad y se prueba con alguien ajeno: para que el cambio de opinión ocurra cuando corregir cuesta un dibujo. Lo que no se puede es enterarse en la Clase 15.

**¿La fase de operación y retiro nos toca a nosotros?**

En el informe final, sí, en una versión corta: qué pasaría si su solución se deja de usar y **qué pasa con los datos**. Es la Ley 1581 de 2012 de la sesión 4 aplicada al final de la vida del sistema, y casi nadie la piensa. Con dos párrafos bien pensados es suficiente.

## Notas operativas

- Las cinco salas de grupo se crean **antes** de la sesión.
- Pida que abran la **ficha del problema de la sesión 6** en la apertura. Sin ficha no hay requisitos, y hay equipos que la van a haber dejado a medias.
- En las salas, la pregunta única es **«¿cómo se comprueba ese requisito?»**. El criterio de aceptación es lo que falta en el 90 % de las tablas y es el 25 % de la rúbrica.
- **Anote la fase declarada y el hito de la sesión 10 de cada equipo.** En la sesión 10 se verifica contra eso: es la forma más simple de detectar un equipo atrasado a tiempo.
- Sea honesto con la curva del costo: **la dirección no se discute, los múltiplos sí**. Si un equipo cita «100 veces más caro» como ley, pida la fuente. Es la misma exigencia de la sesión 5.
- Hoy no se usa IA. Los requisitos tienen que salir de la ficha y de las restricciones del propio caso; un asistente los devuelve genéricos y sin las restricciones locales, que es justo lo que hace útiles a los de hoy.

## Material de esta clase

- Deck: `Clases/Clase 7 - Ciclo de vida de los proyectos de ingenieria/Presentacion.pptx`
- Taller del estudiante: `Clases/Clase 7 - Ciclo de vida de los proyectos de ingenieria/Taller Clase 7 - Ciclo de vida del proyecto.docx`
- Solución del taller (**solo docente**): `Kit docente/Clase 7/Solucion Taller Clase 7 - Ciclo de vida del proyecto.docx`
- Este guion: `Kit docente/Clase 7/Guion Docente Clase 7 - Ciclo de vida de los proyectos de ingenieria.docx`

> **Recordatorio de datos personales:** ninguna actividad de este curso sube nombres, cédulas, teléfonos ni fotos de terceros. Si el caso del equipo los trae, se usa el rol («la dueña de la papelería», «el auxiliar de la biblioteca»).
