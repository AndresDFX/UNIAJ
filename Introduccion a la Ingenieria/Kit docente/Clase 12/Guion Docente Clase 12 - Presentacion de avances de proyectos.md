# Guion docente — Clase 12: Presentación de avances de proyectos

## Información de la clase
- Asignatura: Introducción a la Ingeniería (FI300101)
- Duración del bloque: **90 min**
- Tipo: Clase virtual sincrónica por Google Meet · Sesión 8 de 11 · corresponde al tema 12 del microcurrículo
- Modalidad: **Virtual (síncrona)** por Google Meet · actividades en plataformas gratuitas en la nube · los 5 equipos trabajan en **salas de grupo**
- Corte **3** (40%) · RAA: **RAA3**
- **Material general para los tres grupos** (SB141B, SB141C, LB141F): sin fechas ni horarios de reloj. El reloj de pared de cada grupo está en su `CALENDARIO_2026-2 - <GRUPO>.md`.
- Enfoque: Aprendizaje basado en competencia + Aprendizaje Invertido · Estrategia: ABPr — Aprendizaje Basado en Proyectos

> **Sesión distinta a las anteriores.** El bloque de exposiciones sube a 40 minutos: cada equipo tiene **5 minutos de avance y 3 minutos de retroalimentación del curso**. La actividad en equipos baja a 12 minutos porque el trabajo grueso —probar el prototipo con una persona ajena— **ya venía hecho de la sesión 11**. Un equipo que no hizo la prueba no tiene avance que presentar, y eso hay que decirlo en el minuto 2.

## Objetivos de la clase
- Separar **lo que la persona hizo** de lo que la persona **dijo** en una prueba.
- Clasificar cada tropiezo por **tipo y gravedad**, y encontrar el **patrón**.
- Presentar un avance en 5 minutos: **el problema, lo que falló y la decisión pendiente**.
- Dar y recibir **retroalimentación útil**: observación en vez de opinión.

## Hoy avanzamos el proyecto en…

**Ficha de avance con los hallazgos de la prueba, y el plan de ajustes que sale de la retroalimentación del curso**

**Entregable concreto:** la ficha de avance de cinco bloques en el documento del equipo —el quinto, el plan de ajustes, se llena al cerrar— y las dos cosas que van a ajustar escritas también en su columna del muro, para que el curso las vea

**Herramientas de esta sesión:** Padlet · Google Drive (Docs y Slides)

> El muro de **Padlet** de hoy tiene **una columna por equipo**: mientras un equipo expone, los demás escriben ahí su retroalimentación, y así queda por escrito y no se pierde. El equipo se lleva su columna. La ficha de avance y el plan de ajustes van en el **documento del equipo** en Google Drive. **Hoy no se usa asistente de IA.**

## Fundamento teórico para el docente

Esta sección está escrita para dictar la clase **sin consultar otra fuente**, y va dividida por diapositiva: cada bloque dice a qué diapositiva corresponde.

### La pregunta de entrada: «no, ahí no, toca acá» - diapositiva 4

El gancho de hoy funciona porque todos los equipos van a reconocerse en él. Le pidieron a alguien ajeno que usara el prototipo y, casi con seguridad, en algún momento intervinieron: «no, ahí no, toca acá». Esa frase es el dato más valioso que el equipo tiene hoy, y viene disfrazada de incomodidad.

El giro que hay que hacer explícito, y que es el eje de la sesión: **cada intervención es un hallazgo, no un error de la persona.** Si tuvieron que explicar algo, el prototipo no lo explicaba. Y en la vida real nadie va a estar al lado del usuario para aclarárselo. Vale la pena decirlo con una frase que se les quede: **la persona que prueba nunca se equivoca; si se perdió, el diseño la perdió.**

Aproveche la apertura para tomar el pulso operativo: en el muro, cada equipo escribe **cuántas veces tuvo que intervenir**. Ese número, además de romper el hielo, le dice de inmediato quién hizo la prueba y quién no. Un equipo que responde «ninguna, quedó perfecto» casi siempre no probó, o probó con la mamá de un integrante mientras le explicaba todo.

Y aquí conviene ser directo, porque es la primera sesión del corte 3 y las reglas se fijan hoy: **un equipo que no hizo la prueba no tiene avance que presentar.** No se le puede improvisar retroalimentación a un avance inexistente. Si ocurre, dígalo, deje que expongan lo que tengan y que hagan la prueba antes de la Clase 13 — pero que quede claro que arrancaron el corte con desventaja.

### Lo que hizo vale más que lo que dijo, y el patrón vale más que el caso - diapositivas 5 y 6

**Paso 1: separar lo que hizo de lo que dijo.** Esta es la idea central y hay que insistir en ella. Cuando alguien prueba el trabajo de un amigo, es amable: dice que estaba claro, que le gustó, que es intuitivo. Y sin embargo dudó cinco segundos frente a un botón, se equivocó de pantalla y preguntó qué significaba una palabra. **Lo que hizo es el dato; lo que dijo es cortesía.** No es que la persona mienta: es que nadie quiere hacer sentir mal a quien le muestra algo con orgullo. Por eso en la industria se observa y se cronometra, en vez de preguntar «¿le gustó?» — exactamente la trampa que vieron en la sesión 8.

**Paso 2: escribir el tropiezo, no la solución.** Los estudiantes van a saltar directo a arreglar. Hay que frenarlos: «buscó el botón de volver arriba» es un hecho; «hay que poner un botón arriba» es una conclusión que quizá no sea la mejor. Si se anota la conclusión y se pierde el hecho, ya no se puede pensar de nuevo.

**Pasos 3 y 4: clasificar y buscar el patrón.** La tabla de los cuatro tipos es la herramienta de la sesión, y su valor es que **cada tipo se arregla con un trabajo distinto y a un costo distinto**. Un hallazgo de lenguaje se arregla cambiando una palabra: es el arreglo más barato que existe y el que más rinde, lo cual conecta con el bloque de textos reales de la sesión 10. Uno de flujo exige reordenar pantallas. Uno de expectativa muchas veces **no se arregla**, porque está fuera del alcance de la sesión 8, pero obliga a que el prototipo lo diga en vez de callarlo. Y uno de suposición nuestra es el más caro y el más valioso: descubrir que dábamos por obvio que el usuario tiene datos móviles, o que sabe leer una tabla, cambia una restricción del proyecto.

Sobre el patrón, dé el criterio operativo sin pretensiones de rigor estadístico: **un tropiezo en una persona puede ser casualidad; el mismo tropiezo en dos de tres personas es un defecto de diseño.** Con tres o cinco pruebas no se hace estadística, y hay que decirlo — pero sí se hace ingeniería: la práctica profesional de pruebas de usabilidad trabaja con muy pocos usuarios justamente porque los defectos gruesos aparecen con los primeros. Si algún equipo probó con una sola persona, dígale que el hallazgo sigue valiendo, pero que no sabe si es patrón.

**Paso 5: decidir qué no se arregla.** Es el paso que separa a un equipo que entendió el curso de uno que no. No todo cabe antes de la Clase 14, y **lo que se deja fuera se escribe con su razón**. Eso ya lo practicaron con el alcance mínimo de la sesión 8 y con los descartes de la sesión 11: es la misma disciplina.

### Qué es un avance: cinco minutos que no repiten nada - diapositiva 7

El error universal en una presentación de avance es empezar por el principio. El equipo vuelve a contar el problema, los actores, el árbol de causas y las seis fases, y cuando llega a lo interesante se le acabó el tiempo. Hay que cortarlo de raíz con un argumento simple: **el curso ya conoce su proyecto**, lleva cinco sesiones oyéndolo. Repetirlo es gastar los cinco minutos en lo único que ya no aporta.

Lo que sí es un avance: **los tres hallazgos de la prueba**, contados por lo que la persona hizo. Eso es lo único que el curso no sabe, y por lo tanto lo único que vale la pena contar. Una frase útil para dárselo como regla: *en un avance se cuenta lo que cambió desde la última vez, no lo que se es.*

Y una exigencia que cambia radicalmente la calidad de la sesión: **cada avance tiene que traer una pregunta abierta.** «Tenemos dos maneras de arreglar esto y no nos decidimos» convierte los tres minutos de retroalimentación en algo útil; sin pregunta, los otros equipos improvisan comentarios genéricos. Exíjala explícitamente al repartir el taller —es uno de los cuatro bloques de la ficha— y verá la diferencia.

Por último, la parte incómoda: **admitir lo pendiente**. Los equipos tienden a maquillar el avance porque hay compañeros mirando. El argumento que funciona no es moral sino de conveniencia: **esconder lo pendiente hoy es pagarlo en la Clase 15**, cuando ya hay nota de por medio y ya no hay tiempo de arreglarlo. Hoy la retroalimentación es gratis; en la Clase 15 vale el 15 % del curso.

### Dar y recibir: la única revisión externa gratis del semestre - diapositivas 8 y 9

La retroalimentación entre pares no sale bien sola: sin reglas, un grupo de primer semestre produce diez minutos de «está muy bien, me gustó». Por eso hoy se enseña el formato, y conviene proyectarlo mientras exponen.

El orden **observación, expectativa, una sola cosa** funciona por razones concretas. Empezar con una **pregunta** en vez de una opinión evita la mitad de los comentarios equivocados, porque muchas veces el equipo ya tenía una razón documentada: preguntar «¿por qué eligieron mostrar la fecha ahí?» y oír «porque la información no está al minuto y no queremos mentir» cierra el tema y además enseña al que preguntó. Describir **lo observable** —«no encontré cómo volver»— entrega algo que se puede arreglar, mientras que «la navegación está confusa» solo entrega una impresión. Decir **qué esperaba** aporta un dato sin dar una orden. Y limitarse a **una sola cosa** es aritmética: en tres minutos con cinco comentarios no se aplica ninguno.

La regla de **hablar del trabajo y no de la persona** hay que enunciarla en voz alta la primera vez, porque marca el clima del corte 3 completo: «este texto no lo entendí» y no «no supieron escribirlo». Es la diferencia entre un equipo que escucha y un equipo que se defiende.

De las tres trampas, la que más daño hace es **rediseñar el proyecto ajeno**: aparece siempre, en la forma de «yo lo habría hecho con una aplicación». Hay que cortarla con respeto y con argumento: el otro equipo tomó decisiones documentadas en las sesiones 6 a 11 que usted no vio, y **la retroalimentación es al avance presentado, no al proyecto que usted haría**. La segunda es el **elogio vacío**, que se arregla pidiendo el «qué» y el «por qué» —un elogio con razón sí es útil, porque le dice al equipo qué conservar—. Y la tercera es de quien recibe: **anotar, no responder**. Solo se pregunta para entender. Cierre con el argumento de peso: estos tres minutos son **la única revisión externa gratis** que van a tener antes de que la exposición valga nota; defenderse en vivo es tirarlos a la basura.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 12 - Presentacion de avances de proyectos/Presentacion.pptx`. Las etiquetas [Slide N] del plan y las referencias del fundamento apuntan aquí.

1. Portada · Clase 12
2. Agenda de hoy (90 min)
3. Objetivos de la sesión
4. Pregunta de entrada
5. Cómo se lee una prueba con una persona real
6. Los cuatro tipos de hallazgo y qué hacer con cada uno
7. Qué es un avance y qué no
8. Cómo se da retroalimentación que sirve
9. Tres trampas de la retroalimentación entre pares
10. Taller de hoy: Ficha de avance y plan de ajustes
11. Cómo se expone en 5 minutos
12. Para la Clase 13
13. Cierre · Nos vemos en la Clase 13

## Plan de clase minuto a minuto (90 min)

### 00:00–00:08 · Apertura · [Slide 4]

Comparta pantalla antes de que entre el primero:

> «Ustedes probaron el prototipo con una persona ajena al equipo. ¿Cuántas veces tuvieron que decirle «no, ahí no, toca acá»?»

En el muro, cada equipo escribe **el número**. Eso rompe el hielo y le dice de inmediato quién hizo la prueba.

**[Nota docente]:** anuncie el reparto de hoy —teoría 20, taller 12, **exposiciones y retroalimentación 40**, cierre 10— y diga la regla: **quien no hizo la prueba no tiene avance que presentar.** Es la primera sesión del corte 3 y las reglas se fijan hoy.

**[Nota docente]:** si un equipo responde «ninguna, quedó perfecto», pregunte con quién probaron y si le explicaron mientras usaba. Casi siempre ahí está la respuesta.

### 00:08–00:28 · Teoría (20 min) · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]

Reparto:

- **5 min** · Cómo se lee una prueba [Slide 5]. La frase que se tiene que quedar: **lo que hizo es el dato; lo que dijo es cortesía.**

- **4 min** · Los cuatro tipos de hallazgo [Slide 6]. Señale que el de **lenguaje** es el arreglo más barato y el de **suposición nuestra** el más valioso.

- **4 min** · Qué es un avance [Slide 7]. Diga tres veces que **no se repite el problema** y que **cada avance trae una pregunta abierta**.

- **5 min** · Cómo se da retroalimentación [Slide 8]. Deje esta diapositiva proyectada durante todas las exposiciones.

- **2 min** · Las tres trampas [Slide 9]. Enuncie en voz alta la regla de quien recibe: **anotar, no responder.**

### 00:28–00:40 · Taller en salas de grupo (12 min) · [Slide 10]

Bloque corto a propósito: el trabajo grueso ya venía hecho. Ritmo:

- 5 min · escribir los tres hallazgos **como lo que la persona hizo**.

- 3 min · clasificarlos y marcar el patrón.

- 4 min · decidir qué se arregla, qué no, y **cuál es la pregunta para el curso**.

**[Nota docente]:** entre a las cinco salas con una sola consigna: **exija la pregunta abierta.** Un equipo sin pregunta desperdicia sus tres minutos de retroalimentación y hace que los otros improvisen.

**[Nota docente]:** abra el muro de Padlet con **una columna por equipo** antes de que salgan de las salas, y ponga el enlace en el chat.

### 00:40–01:20 · Exposiciones y retroalimentación (40 min) · [Slide 11]

5 equipos × 8 min: **5 de avance y 3 de retroalimentación del curso**. Cronómetro en pantalla, se corta al llegar a cero.

Mientras un equipo expone, los otros cuatro escriben **en la columna de ese equipo** en el muro. Así la retroalimentación queda por escrito y no se pierde.

**[Nota docente]:** en los tres minutos, dé la palabra a **dos equipos distintos** y haga cumplir el formato: observación, expectativa, una sola cosa. Si alguien empieza a rediseñar el proyecto ajeno, córtelo con respeto y explique por qué.

**[Nota docente]:** el equipo que recibe **anota y no responde**; solo pregunta para entender. Recuérdelo la primera vez y no hará falta repetirlo.

**[Nota docente]:** aporte usted **un** comentario por equipo, al final de los tres minutos, y que sea el que nadie dijo. No repita lo que ya dijeron los compañeros.

### 01:20–01:30 · Cierre · [Slide 12][Slide 13]

Cada equipo escribe en su columna del muro **las dos cosas que va a ajustar** con lo que oyó hoy. Dos minutos, y queda el compromiso por escrito.

Una idea: **la persona que prueba nunca se equivoca; si se perdió, el diseño la perdió.**

Anuncie la Clase 13: **el impacto social y ambiental** del proyecto — a quién más afecta esto, aunque no lo use. Vuelve el listado de actores no usuarios de la sesión 3.

## Errores frecuentes y cómo cortarlos en caliente

| Lo que dice el equipo | Por qué no sirve | Qué pedir en su lugar |
|---|---|---|
| «Le pareció confusa la pantalla» | Es una opinión, no se puede verificar y no dice qué cambiar. Además suele ser la versión amable de lo que en realidad pasó. | La acción: «tocó el estado dos veces esperando que se abriera algo». Eso sí se puede volver a probar. |
| «Dijo que estaba todo clarísimo» | La gente es amable con quien le muestra su trabajo. Lo que dijo es cortesía; lo que hizo es el dato. | Lo que hizo mientras usaba: dónde dudó, dónde se equivocó, qué preguntó. Y si hay contradicción, que la anoten: es el mejor hallazgo. |
| Un hallazgo que ya viene con la solución adentro | Si se anota «hay que poner un botón arriba» y se pierde el hecho, ya no se puede pensar otra solución mejor. | Primero el hecho, después la decisión. Son dos columnas distintas de la ficha. |
| «Vamos a arreglar todo antes de la Clase 14» | No cabe, y decirlo es no haber priorizado. Priorizar es una decisión de ingeniería, no una rendición. | Qué queda fuera y por qué: fuera del alcance, excede la capacidad del equipo, o rompe una restricción. |
| «¿Qué le mejorarían a nuestro proyecto?» | Como pregunta al curso es demasiado abierta: produce comentarios genéricos y desperdicia a los otros cuatro equipos. | Una decisión concreta con dos alternativas, cada una con su pro y su contra. |

## Dudas frecuentes del estudiante

**¿Con cuántas personas hay que probar?**

Con dos o tres basta para lo que necesitamos hoy. Con tan pocas pruebas **no se hace estadística** y hay que ser honestos con eso, pero sí se encuentran los defectos gruesos: es la práctica normal en pruebas de usabilidad, porque los primeros usuarios tropiezan justo con lo que está mal diseñado. Lo que **no** sirve es probar con cero personas, ni probar con alguien a quien se le explica mientras usa.

**¿Y si la persona no logró terminar la tarea?**

Es el hallazgo más importante de todos, y hay que registrarlo así: **abandono**. Un tropiezo que termina en abandono pesa más que uno que termina en duda, incluso si le pasó a una sola persona. No lo suavicen en el avance: es lo que el curso más necesita oír para poder ayudarles.

**¿Podemos defendernos si la retroalimentación nos parece injusta?**

En los tres minutos, no: se **anota y no se responde**, y solo se pregunta para entender —«¿en qué momento se perdió?»—. No es una regla de sumisión, es de eficiencia: defenderse consume el único tiempo de revisión externa gratis que van a tener. Después, en el documento del equipo, escriben qué van a aplicar y qué no, con su razón. **Descartar retroalimentación con argumento es perfectamente válido**; descartarla en el momento y sin pensarla, no.

**¿Los ajustes de hoy tienen que estar listos para la Clase 15?**

Para la **Clase 14**, no para la 15. La Clase 14 es la preparación de la presentación final y el ensayo general: si el prototipo no está ajustado, van a ensayar con la versión vieja y el ensayo no sirve. La 15 es la exposición con nota, y ahí ya no hay margen.

## Notas operativas

- **Reparto distinto hoy y hay que anunciarlo en el minuto 2:** teoría 20 · taller 12 · **exposiciones y retroalimentación 40** · cierre 10.
- **Prepare el muro de Padlet con una columna por equipo** antes de la sesión, y ponga el enlace en el chat antes de que salgan de las salas de grupo.
- Diga la regla en la apertura: **quien no hizo la prueba no tiene avance que presentar.** Es la primera sesión del corte 3 y las reglas se fijan hoy.
- Deje la diapositiva de **cómo se da retroalimentación** proyectada durante las 40 minutos de exposiciones. Sin el formato a la vista, se vuelve «me gustó mucho».
- En los tres minutos de cada equipo, dé la palabra a **dos equipos distintos** y aporte usted **un solo comentario al final** — el que nadie dijo.
- Cronómetro en pantalla y corte estricto: cinco equipos por ocho minutos no perdona. Si un equipo se pasa, el que pierde tiempo es el último.
- Si alguien empieza a **rediseñar el proyecto ajeno**, córtelo con respeto y explique por qué: el otro equipo tomó decisiones documentadas que quien comenta no vio.
- Recuerde a quien recibe: **anotar, no responder.** Una vez basta si se dice antes de la primera exposición.
- Los ajustes se necesitan para la **Clase 14** —el ensayo general—, no para la 15.

## Material de esta clase

- Deck: `Clases/Clase 12 - Presentacion de avances de proyectos/Presentacion.pptx`
- Taller del estudiante: `Clases/Clase 12 - Presentacion de avances de proyectos/Taller Clase 12 - Ficha de avance y plan de ajustes.docx`
- Solución del taller (**solo docente**): `Kit docente/Clase 12/Solucion Taller Clase 12 - Ficha de avance y plan de ajustes.docx`
- Este guion: `Kit docente/Clase 12/Guion Docente Clase 12 - Presentacion de avances de proyectos.docx`

> **Recordatorio de datos personales:** ninguna actividad de este curso sube nombres, cédulas, teléfonos ni fotos de terceros. Si el caso del equipo los trae, se usa el rol («la dueña de la papelería», «el auxiliar de la biblioteca»).
