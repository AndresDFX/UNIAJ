# Guion docente — Clase 7: Ciclo de vida de los proyectos de ingeniería

## Información de la clase
- Asignatura: Introducción a la Ingeniería (FI300101)
- Duración del bloque: **90 min**
- Tipo: Clase virtual sincrónica por Microsoft Teams · Sesión 5 de 11 (sesión doble junto con la Clase 8) · corresponde al tema 7 del microcurrículo
- Modalidad: **Virtual (síncrona)** por Microsoft Teams · actividades en plataformas gratuitas en la nube · los 5 equipos trabajan en **salas de grupo**
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

Proyectado en la lamina «La pregunta de entrada: la curva del costo del cambio» (4 vinetas).

- Mover una pared en el plano cuesta un borrador; en el ladrillo cuesta tumbar y volver a levantar; en la casa entregada cuesta la obra, la mudanza y el enojo del dueño.

- Lo que hay que hacer explícito en el minuto 12 es que **en software la curva es igual pero se ve menos**, y ahí está el problema.

- Por eso en ingeniería de software hubo que inventar fases, revisiones y criterios de aceptación: son el equivalente a mirar el plano antes de pedir el cemento.

- Recoja las respuestas en el muro.

### Las seis fases, y por qué el orden importa - diapositiva 5

Proyectado en la lamina «Las seis fases, y por qué el orden importa (1/2)» (4 vinetas).

- Conviene presentar las fases como una cadena de preguntas, no como una lista de etapas administrativas.

- Eso reordena la percepción del curso: no estaban haciendo un ejercicio, estaban cerrando una fase. **Requisitos** responde *qué tiene que hacer la solución para resolver eso, y cómo sabremos que lo hace*.

- Cada fase existe porque descubrir un error en ella cuesta menos que descubrirlo en la siguiente.

### La curva del costo del cambio: qué se puede afirmar y qué no - diapositiva 6

Proyectado en la lamina «Las seis fases, y por qué el orden importa (2/2)» (4 vinetas).

### Cascada, iterativo, y lo que Royce dijo de verdad - diapositiva 7

Proyectado en la lamina «La curva del costo del cambio: qué se puede afirmar y qué no (1/2)» (5 vinetas).

- La dirección de la curva no está en discusión; la pendiente sí.

### Requisitos, criterios de aceptación y hitos: lo que se entrega hoy - diapositivas 8 y 9

Proyectado en la lamina «La curva del costo del cambio: qué se puede afirmar y qué no (2/2)» (3 vinetas).

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
10. La pregunta de entrada: la curva del costo del cambio
11. Las seis fases, y por qué el orden importa (1/2)
12. Las seis fases, y por qué el orden importa (2/2)
13. La curva del costo del cambio: qué se puede afirmar y qué no (1/2)
14. La curva del costo del cambio: qué se puede afirmar y qué no (2/2)
15. Cascada, iterativo, y lo que Royce dijo de verdad (1/2)
16. Cascada, iterativo, y lo que Royce dijo de verdad (2/2)
17. Requisitos, criterios de aceptación y hitos: lo que se entrega hoy (1/3)
18. Requisitos, criterios de aceptación y hitos: lo que se entrega hoy (2/3)
19. Requisitos, criterios de aceptación y hitos: lo que se entrega hoy (3/3)
20. Taller de hoy: Ciclo de vida del proyecto
21. Cómo se expone en 3 minutos
22. Para la Clase 8
23. Cierre · Nos vemos en la sesión 8

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
