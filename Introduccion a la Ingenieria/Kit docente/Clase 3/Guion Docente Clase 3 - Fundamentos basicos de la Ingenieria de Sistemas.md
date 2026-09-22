# Guion docente — Clase 3: Fundamentos básicos de la Ingeniería de Sistemas

## Información de la clase
- Asignatura: Introducción a la Ingeniería (FI300101)
- Duración del bloque: **90 min**
- Tipo: Clase virtual sincrónica por Microsoft Teams · Sesión 2 de 11 (sesión doble junto con la Clase 2) · corresponde al tema 3 del microcurrículo
- Modalidad: **Virtual (síncrona)** por Microsoft Teams · actividades en plataformas gratuitas en la nube · los 5 equipos trabajan en **salas de grupo**
- Corte **1** (30%) · RAA: **RAA1**
- **Material general para los tres grupos** (SB141B, SB141C, LB141F): sin fechas ni horarios de reloj. El reloj de pared de cada grupo está en su `CALENDARIO_2026-2 - <GRUPO>.md`.
- Enfoque: Aprendizaje basado en competencia + Aprendizaje Invertido · Estrategia: ABPr — Aprendizaje Basado en Proyectos

## Objetivos de la clase
- Definir **sistema** con sus cinco elementos: entradas, proceso, salidas, retroalimentación y frontera.
- Distinguir el **sistema** del **software** que lo soporta, y decir por qué confundirlos hace fracasar proyectos.
- Identificar los **actores** de un sistema, incluidos los que no lo usan pero sí lo sufren.
- Usar un asistente de IA para descomponer un sistema y **corregir a mano lo que inventó**.

## Hoy avanzamos el proyecto en…

**Ver el problema de la sesión 1 como un sistema completo, con actores y frontera, en vez de como «una app que falta»**

**Entregable concreto:** una ficha de sistema de cinco bloques en el documento del equipo, con el prompt usado y una lista de las correcciones hechas a la respuesta de la IA

**Herramientas de esta sesión:** Asistente de IA · Google Drive (Docs y Slides) · Padlet

> Es la **primera de las dos sesiones** en que el Plan de curso autoriza usar un asistente de IA (la otra es la 11). La regla es firme y se dice en voz alta: se entrega el **prompt usado** y **lo que se corrigió a mano**. Una respuesta de IA pegada sin revisar no puntúa, porque el criterio de hoy es justamente distinguir lo que la herramienta acertó de lo que inventó. Sirve cualquier asistente en plan gratuito.

## Fundamento teórico para el docente

Esta sección está escrita para dictar la clase **sin consultar otra fuente**, y va dividida por diapositiva: cada bloque dice a qué diapositiva corresponde.

### La pregunta de entrada y por qué esos tres ejemplos - diapositiva 4

Proyectado en la lamina «La pregunta de entrada y por qué esos tres ejemplos (1/2)» (3 vinetas).

### Qué es un sistema y por qué la frontera es la decisión difícil - diapositiva 5

Proyectado en la lamina «La pregunta de entrada y por qué esos tres ejemplos (2/2)» (2 vinetas).

### El sistema no es el software: la confusión que hace fracasar proyectos - diapositiva 6

Proyectado en la lamina «Qué es un sistema y por qué la frontera es la decisión difícil (1/2)» (5 vinetas).

- Lo importante de esa definición no son las palabras sino la consecuencia: **el propósito es lo primero que hay que poder decir**.

- Los cinco elementos se explican con un ejemplo concreto y de una sola pasada.

- El estudiante de primer semestre tiende a creer que la frontera viene dada por el problema.

### Actores, requisitos y retroalimentación: los tres que se olvidan - diapositiva 7

Proyectado en la lamina «Qué es un sistema y por qué la frontera es la decisión difícil (2/2)» (5 vinetas).

### El asistente de IA: cómo usarlo hoy sin que haga el trabajo - diapositivas 9 y 8

Proyectado en la lamina «El sistema no es el software: la confusión que hace fracasar proyectos (1/2)» (3 vinetas).

- Casi todos llegan a primer semestre con la mirada de programador, y no por ignorancia: es la que el entorno premia.

- La columna derecha es la que la carrera enseña.

- El ejemplo de las citas médicas conviene desarrollarlo hasta el final porque muestra el fracaso completo.

- El software funciona y el problema sigue. **En la lógica de este curso, ese proyecto fracasó**, y no por un error técnico.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 3 - Fundamentos basicos de la Ingenieria de Sistemas/Presentacion.pptx`. Las etiquetas [Slide N] del plan y las referencias del fundamento apuntan aquí.

1. Portada · Clase 3
2. Agenda de hoy (90 min)
3. Objetivos de la sesión
4. Pregunta de entrada
5. Los cinco elementos de un sistema
6. Mirar el software o mirar el sistema
7. Cuatro conceptos que se usan todo el semestre
8. Cómo se descompone un sistema en cinco pasos
9. El asistente de IA: qué hace bien y en qué miente
10. La pregunta de entrada y por qué esos tres ejemplos (1/2)
11. La pregunta de entrada y por qué esos tres ejemplos (2/2)
12. Qué es un sistema y por qué la frontera es la decisión difícil (1/2)
13. Qué es un sistema y por qué la frontera es la decisión difícil (2/2)
14. El sistema no es el software: la confusión que hace fracasar proyectos (1/2)
15. El sistema no es el software: la confusión que hace fracasar proyectos (2/2)
16. Actores, requisitos y retroalimentación: los tres que se olvidan (1/2)
17. Actores, requisitos y retroalimentación: los tres que se olvidan (2/2)
18. El asistente de IA: cómo usarlo hoy sin que haga el trabajo (1/2)
19. El asistente de IA: cómo usarlo hoy sin que haga el trabajo (2/2)
20. Plantilla del entregable: los 5 bloques
21. Guion de la exposicion, con tiempos
22. Taller de hoy: Anatomía del sistema
23. Cómo se expone en 3 minutos
24. Para la Clase 4
25. Cierre · Nos vemos en la sesión 4

## Plan de clase minuto a minuto (90 min)

### 00:00–00:10 · Apertura · [Slide 4]

Comparta pantalla con la pregunta de entrada antes de que entre el primero:

> «¿Qué tienen en común un semáforo, la matrícula de la UNIAJC y la fila de una EPS?»

**[Nota docente]:** enlace del muro en el chat. Las respuestas van a girar en torno a «tecnología» y «son procesos». Ninguna se corrige ahora.

**[Nota docente]:** recuerde que hoy se usa asistente de IA y que hay que traer la línea de tiempo de la sesión 2 en la carpeta del equipo.

### 00:10–00:55 · Teoría · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]

Reparto sugerido de los 45 min:

- **10 min** · Los cinco elementos [Slide 5], con el ejemplo de las citas del consultorio recorrido completo. Detenga la clase en **frontera** y haga la pregunta del transporte del paciente: es la que produce discusión.

- **12 min** · Mirar el software o mirar el sistema [Slide 6]. Línea por línea. Cierre con el caso de la app impecable y la fila que no se movió.

- **10 min** · Los cuatro conceptos [Slide 7]. En **actor**, insista en el vecino que ya no consigue cita: es el actor que se olvida siempre.

- **7 min** · El método de cinco pasos [Slide 8]. Es el orden del taller.

- **6 min** · El asistente de IA [Slide 9]. La regla se dice completa: prompt + correcciones, o no puntúa.

**[Nota docente]:** al terminar, vuelva al muro de la apertura y muestre que «son procesos» era una respuesta a medias: son sistemas, y en los tres el software es la parte pequeña.

### 00:55–01:12 · Taller en salas de grupo · [Slide 10]

**2 min** para repartir. Cada equipo trabaja **el sistema del problema que escribió en la sesión 1**: no se sortea nada nuevo, porque el objetivo es que ese problema madure hacia el proyecto.

**15 min** de trabajo. Entre a las cinco salas, unos 3 min en cada una, y revise **una sola cosa: la frontera y su justificación**. Es el campo que decide si el proyecto va a ser abordable en un semestre.

**[Nota docente]:** si un equipo pega la respuesta de la IA sin marcar correcciones, no lo deje avanzar: pídale tres verificaciones concretas antes de seguir. Es más útil cortarlo en el minuto 5 que castigarlo en la nota.

**[Nota docente]:** la trampa que hay que buscar son las cifras inventadas. Si en el documento aparece «el promedio de espera es de 45 min», pregunte de dónde salió. Si salió de la IA, esa es exactamente la corrección que se califica.

### 01:12–01:27 · Exposiciones · [Slide 11]

5 equipos × 3 min. Habla el vocero con el documento ya compartido. **El último minuto de cada exposición es obligatoriamente «qué se inventó la IA»**: es la parte que hace la sesión distinta de una clase de teoría de sistemas.

**[Nota docente]:** los cinco enlaces en el chat antes de la primera exposición.

**[Nota docente]:** anote los actores olvidados que aparezcan. Son material directo para la Clase 13 y conviene tener la lista.

### 01:27–01:30 · Cierre · [Slide 12][Slide 13]

Una idea: **el sistema no es el software.** Un proyecto de este curso se juzga por si el problema del entorno se redujo y se puede medir, no por si el prototipo funciona.

Anuncie la sesión 4 —principios éticos— con el gancho: hoy vimos que un sistema puede funcionar y ser injusto; la próxima se ve qué responsabilidad tiene el ingeniero cuando eso pasa.

## Errores frecuentes y cómo cortarlos en caliente

| Lo que dice el equipo | Por qué no sirve | Qué pedir en su lugar |
|---|---|---|
| «El sistema es la app / la plataforma» | Confunde el sistema con una de sus partes; es la falla que la clase entera ataca. | Que señalen dónde está el software DENTRO del proceso, y qué partes del sistema no son software. |
| «Los usuarios» como actor | No es un rol: no dice qué le importa a quién ni permite encontrar al perjudicado. | Roles concretos y, obligatorio, uno que no use el sistema y sí sufra el resultado. |
| «Dentro de la frontera: todo lo relacionado» | Una frontera sin exclusiones no es una frontera, y produce proyectos que no se acaban. | Una cosa que dejen fuera a propósito, con la razón escrita. |
| «La retroalimentación es que el usuario se queja» | Es tardía y sesgada: solo se queja una parte, y ya pasó el daño. | Cómo se enteraría el sistema ANTES de que alguien reclame. Si no hay manera, que lo escriban: es un hallazgo. |
| Un dato con cifra que salió de la IA | El asistente inventa cifras locales con total naturalidad y sin avisar. | La fuente. Si salió de la IA, que lo borren y lo anoten como corrección: eso es lo que se califica. |

## Dudas frecuentes del estudiante

**¿Entonces podemos usar IA en todo el curso?**

No. El Plan de curso la autoriza en las sesiones 3 y 11. En las demás no se usa, y la razón es práctica: para poder verificar lo que dice hay que saber del tema, y el tema es lo que estamos aprendiendo. Cuando se use, siempre se declara el prompt y las correcciones.

**¿Se penaliza usar IA?**

No. Se penaliza **no verificarla**. Un texto pegado sin correcciones vale 0 en ese bloque porque no muestra ningún trabajo de ingeniería, igual que copiar un párrafo de una página web sin leerlo.

**¿Qué pasa si la IA acertó en todo y no encontramos nada que corregir?**

Vuelvan a mirar las cifras, los nombres propios y las normas. En un caso local siempre hay algo inventado o asumido. Si de verdad no encuentran nada, escriban qué verificaron y cómo: eso también se califica, pero tiene que estar la verificación.

**¿El sistema de nuestro proyecto tiene que ser el problema de la sesión 1?**

Sí, hoy sí. La idea es que ese problema madure: en la sesión 6 se entrega la ficha del problema del proyecto y es más fácil si vienen trabajándolo desde la primera semana.

## Notas operativas

- Las cinco salas de grupo se crean **antes** de la sesión.
- Es la primera de las dos sesiones con IA autorizada. Diga la regla completa **antes** de abrir las salas, no después: prompt + correcciones, o no puntúa.
- El error más útil de cazar en las salas es la **cifra inventada**. Si aparece un porcentaje o un promedio en el documento, pregunte de dónde salió.
- Anote los actores no-usuarios que aparezcan en las cinco exposiciones: es la lista de entrada de la Clase 13 y no se vuelve a tener tan fácil.
- Ningún equipo debe subir nombres de funcionarios ni de personas reales. Si el sistema es de la propia universidad, se usa el rol.

## Material de esta clase

- Deck: `Clases/Clase 3 - Fundamentos basicos de la Ingenieria de Sistemas/Presentacion.pptx`
- Taller del estudiante: `Clases/Clase 3 - Fundamentos basicos de la Ingenieria de Sistemas/Taller Clase 3 - Anatomia del sistema.docx`
- Solución del taller (**solo docente**): `Kit docente/Clase 3/Solucion Taller Clase 3 - Anatomia del sistema.docx`
- Este guion: `Kit docente/Clase 3/Guion Docente Clase 3 - Fundamentos basicos de la Ingenieria de Sistemas.docx`

> **Recordatorio de datos personales:** ninguna actividad de este curso sube nombres, cédulas, teléfonos ni fotos de terceros. Si el caso del equipo los trae, se usa el rol («la dueña de la papelería», «el auxiliar de la biblioteca»).
