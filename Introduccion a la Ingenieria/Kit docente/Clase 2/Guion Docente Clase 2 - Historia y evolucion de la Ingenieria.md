# Guion docente — Clase 2: Historia y evolución de la Ingeniería

## Información de la clase
- Asignatura: Introducción a la Ingeniería (FI300101)
- Duración del bloque: **90 min**
- Tipo: Clase virtual sincrónica por Google Meet · Sesión 2 de 11 (sesión doble junto con la Clase 3) · corresponde al tema 2 del microcurrículo
- Modalidad: **Virtual (síncrona)** por Google Meet · actividades en plataformas gratuitas en la nube · los 5 equipos trabajan en **salas de grupo**
- Corte **1** (30%) · RAA: **RAA1**
- **Material general para los tres grupos** (SB141B, SB141C, LB141F): sin fechas ni horarios de reloj. El reloj de pared de cada grupo está en su `CALENDARIO_2026-2 - <GRUPO>.md`.
- Enfoque: Aprendizaje basado en competencia + Aprendizaje Invertido · Estrategia: ABPr — Aprendizaje Basado en Proyectos

## Objetivos de la clase
- Ubicar **seis hitos** de la historia de la disciplina y decir qué problema resolvía cada uno.
- Explicar por qué la ingeniería de sistemas **nace como respuesta a un fracaso**, no a un avance técnico.
- Construir una **línea de tiempo** en una herramienta de diagramación en la nube.
- Identificar, para un hito, **qué parte de ese problema sigue vivo hoy**.

## Hoy avanzamos el proyecto en…

**Entender que el problema del proyecto tiene que ser un problema real y medible, porque los proyectos que fracasaron en la historia fracasaron por no tener eso**

**Entregable concreto:** un diagrama de línea de tiempo con 4 hitos en diagrams.net (draw.io), guardado en la carpeta del equipo en Drive, más las cuatro respuestas escritas por hito en el documento del equipo

**Herramientas de esta sesión:** diagrams.net (draw.io) · Google Drive (Docs y Slides)

> El taller se hace en **diagrams.net (draw.io)**, que abre sin cuenta y guarda directo en la carpeta del equipo en Drive. Si alguien no logra abrirlo, la línea de tiempo se puede armar en Google Slides con cuadros de texto: lo que se evalúa es el contenido de los hitos, no el diseño.

## Fundamento teórico para el docente

Esta sección está escrita para dictar la clase **sin consultar otra fuente**, y va dividida por diapositiva: cada bloque dice a qué diapositiva corresponde.

### La pregunta de entrada y para qué sirve incomodar con una fecha - diapositiva 4

La pregunta de apertura —«un proyecto de software se pasa del plazo y del presupuesto, ¿es un problema de 2026 o de 1968?»— está formulada para producir una respuesta equivocada. Casi todo el grupo va a decir que es de 2026, porque la intuición de un estudiante de primer semestre es que la historia de la tecnología es una escalera: cada década resuelve los problemas de la anterior. Esa intuición es la que hay que romper hoy, porque de ella se deriva una creencia más dañina: que basta con aprender la herramienta nueva.

Los primeros diez minutos, mientras se conectan, sirven para recoger esas respuestas en el muro. No hay que corregir ninguna. En el minuto 25, cuando ya esté contada la conferencia de Garmisch de 1968, se vuelve al muro y se lee en voz alta lo que escribieron. El contraste hace el trabajo solo: el problema que el grupo cree contemporáneo tiene casi sesenta años y un nombre propio.

### Por qué la disciplina nace de un fracaso y no de un invento - diapositivas 5 y 6

Hay una diferencia grande entre contar la historia de la informática y contar la historia de la ingeniería de sistemas. La primera es una historia de máquinas: válvulas, transistores, circuitos integrados, microprocesadores. Es la que el estudiante espera y es la menos útil, porque sugiere que el progreso viene del hardware. La segunda es una historia de **fracasos de organización**, y es la que explica por qué existe la carrera que el estudiante está empezando.

En los años cuarenta y cincuenta el cuello de botella era la máquina. Programar el ENIAC significaba reconfigurar cables físicamente; escribir en lenguaje de máquina era lento porque la máquina era lo escaso y lo caro. Fortran (1957) y COBOL (1959) atacan exactamente ese problema: permitir decirle algo a la máquina sin hablar su idioma. Hasta aquí el trabajo lo hace una persona o un puñado de personas, y el método no importa mucho porque el problema cabe en una cabeza.

En los años sesenta pasa algo que cambia la naturaleza del problema: el hardware se abarata y se vuelve más capaz, y entonces se vuelven pensables sistemas que antes no lo eran. El sistema de reservas aéreas SABRE, el software de navegación del programa Apollo, el sistema operativo OS/360 de IBM. Son proyectos de cientos y hasta miles de personas y de varios años. Y fracasan de forma espectacular en plazo y en costo, no porque las máquinas fueran lentas, sino porque **nadie sabía cómo coordinar a mil personas construyendo una sola cosa que nadie puede ver ni tocar**. Fred Brooks, que dirigió el OS/360, escribió después el libro que explica por qué.

En 1968 la OTAN convoca una conferencia en Garmisch para hablar del asunto, y ahí se populariza el término «ingeniería de software». Vale la pena detenerse en que el término era una **propuesta, casi una provocación**: si construir software se parece a construir un puente, entonces debería tener método, estándares, mediciones y responsabilidad profesional, en vez de depender del talento de individuos. Ese es el momento fundacional que el estudiante tiene que recordar: la disciplina no nace de una máquina nueva, nace del reconocimiento público de que se estaba trabajando mal.

### Los seis hitos: qué decir de cada uno en dos minutos - diapositiva 7

La tarjeta de 1945–1957 se cuenta rápido: arquitectura de von Neumann (programa y datos en la misma memoria, que es la razón por la que un computador puede cargar cualquier programa) y los primeros lenguajes de alto nivel. El punto no es memorizar nombres, es entender que el problema de la época era **traducir**.

1968 es el hito central de la clase y merece la mitad del tiempo. Se cuenta como está arriba: los tres proyectos que fracasaron, la conferencia, el término. Si el docente solo alcanza a contar un hito bien, que sea este.

1970 es Winston Royce y el esquema que el mundo llamó «cascada». Aquí hay que ser preciso porque es el error histórico más repetido en las clases de ingeniería: Royce dibujó el esquema lineal para decir que **así no se debe hacer**, y propuso hacerlo dos veces, con prototipo y retroalimentación. La industria se quedó con el dibujo y tiró la advertencia. La lección para el estudiante es doble: sobre el ciclo de vida (que se ve en la sesión 7) y sobre cómo se deforman las ideas cuando se citan de segunda mano.

1975 es Brooks y «The Mythical Man-Month». La idea que hay que dejar es contraintuitiva y utilísima para un curso donde se trabaja en equipos de cinco: **agregar gente a un proyecto atrasado lo atrasa más**, porque los canales de comunicación crecen mucho más rápido que las personas. Con 5 personas hay 10 parejas que se tienen que entender; con 10 personas hay 45. Es un dato verificable con una fórmula de bachillerato y explica por qué en este curso los equipos son de cinco y no de diez.

1991–2001 junta software libre (Linux, y con él la idea de que miles de personas que no se conocen pueden construir algo serio si el proceso es público) y el Manifiesto Ágil de 2001. El problema que atacan es el mismo: **los requisitos cambian mientras se construye**, y un plan de dos años escrito el primer día es una obra de ficción. Ágil no elimina las fases, cambia su tamaño.

2006 en adelante es la nube y los datos. Aquí el problema muda otra vez y es importante que el estudiante lo note, porque es el problema de su generación: cuando alquilar mil servidores por hora cuesta poco y una biblioteca de IA se instala en un comando, la pregunta técnica «¿se puede construir?» deja de ser la difícil. La difícil es **«¿se debe construir, a quién afecta y quién responde?»**. Esa pregunta es el hilo de las Clases 4, 5 y 13.

### El método de lectura de un hito y por qué la cuarta pregunta es la que se califica - diapositivas 8 y 9

Las cuatro preguntas (qué dolía, qué propuso, qué resolvió, qué sigue vivo) son el método de trabajo del taller y conviene dictarlas como método, no como curiosidad. Las tres primeras se pueden buscar; la cuarta exige pensar, y por eso es la que más pesa en la rúbrica. Un equipo puede escribir «1975: Brooks dijo que agregar gente atrasa el proyecto» y estar en lo correcto sin haber entendido nada. La cuarta pregunta obliga a decir algo como «sigue vivo porque cuando nuestro equipo se atrasó en el taller de la sesión anterior, la reacción natural fue pedir ayuda a otro equipo, y eso nos costó veinte minutos de explicar el contexto».

Las tres aclaraciones de la última diapositiva de teoría hay que decirlas en voz alta aunque parezcan detalles, porque son las tres cosas que el estudiante va a encontrar mal contadas en el primer video o resumen que busque en internet. Advertirlas hoy le da una herramienta que sirve para todo el curso: **cuando una fuente cuenta una idea histórica sin decir quién la dijo y contra qué discutía, conviene desconfiar**.

Sobre la tercera aclaración conviene ser honesto en el aula y no inflarla. Los informes de la industria sobre fracaso de proyectos usan definiciones distintas de «fracaso» y sus cifras varían mucho entre ediciones y entre fuentes. Lo que sí se puede afirmar sin exagerar es que **el fracaso por plazo, costo y alcance sigue siendo un problema reportado sistemáticamente**, y que ninguna metodología ha declarado el problema cerrado. Si un equipo trae una cifra de internet, se le pide la fuente y el año: es el primer ejercicio de rigor bibliográfico del curso.

### El taller, la exposición y por qué las cinco líneas de tiempo se suman - diapositivas 10 y 11

Cada equipo recibe un periodo distinto y arma su tramo de línea de tiempo. La consecuencia es que las cinco exposiciones, puestas en orden histórico, producen la línea de tiempo completa de la disciplina, que es justo el trabajo independiente de la semana. Esto hay que decírselo al grupo antes de empezar: no están haciendo cinco trabajos que compiten, están armando un solo mapa por pedazos, y el pedazo de cada uno le sirve a los otros cuatro.

Por eso las exposiciones van **en orden histórico y no por sorteo**: el equipo del periodo 1945–1957 abre y el de 2006–hoy cierra. Cuesta lo mismo y el grupo se lleva una narración en vez de cinco fragmentos. El docente escribe el orden en el chat antes de que empiecen.

El taller pide cuatro hitos por periodo, no más. La tentación del equipo será meter diez fechas para verse completo, y el resultado es una línea de tiempo que nadie puede exponer en tres minutos. Cuatro hitos bien leídos, con su «qué sigue vivo», valen mucho más y es lo que la rúbrica premia.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 2 - Historia y evolucion de la Ingenieria/Presentacion.pptx`. Las etiquetas [Slide N] del plan y las referencias del fundamento apuntan aquí.

1. Portada · Clase 2
2. Agenda de hoy (90 min)
3. Objetivos de la sesión
4. Pregunta de entrada
5. Cómo se cuenta la historia y cómo fue
6. Cuándo el problema dejó de ser la máquina
7. Seis hitos y el problema que atacaba cada uno
8. Cómo se lee un hito sin quedarse en la anécdota
9. Tres cosas que se repiten y son falsas
10. Taller de hoy: Línea de tiempo del periodo
11. Cómo se expone en 3 minutos
12. Para la Clase 3
13. Cierre · Nos vemos en la sesión 3

## Plan de clase minuto a minuto (90 min)

### 00:00–00:10 · Apertura · [Slide 4]

Entre a Meet 5 min antes y comparta pantalla con la pregunta de entrada antes de que entre el primer estudiante:

> «Un proyecto de software se pasa del plazo y del presupuesto. ¿Es un problema de 2026 o de 1968?»

**[Nota docente]:** el enlace del muro de Padlet va en el chat de Meet. No corrija ninguna respuesta ahora: el valor de este muro está en releerlo en el minuto 25, cuando ya se haya contado Garmisch.

**[Nota docente]:** confirme que las cinco salas de grupo están creadas y que cada equipo tiene su documento de la sesión 1 a mano — hoy se trabaja en el mismo documento, en una pestaña nueva.

### 00:10–00:55 · Teoría · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]

Reparto sugerido de los 45 min:

- **8 min** · Cómo se cuenta la historia y cómo fue [Slide 5]. Es el desmontaje de la idea de escalera.

- **12 min** · Cuándo el problema dejó de ser la máquina [Slide 6]. Aquí va Garmisch 1968, que es el corazón de la clase. Al terminar, **vuelva al muro de Padlet** y lea dos o tres respuestas: el problema que creían de 2026 tiene cincuenta y ocho años.

- **15 min** · Los seis hitos [Slide 7], unos dos minutos y medio por tarjeta. Si el tiempo aprieta, recorte 1945–1957 y 1991–2001, nunca 1968 ni 1975.

- **6 min** · Cómo se lee un hito [Slide 8]. Se dicta como método porque es lo que van a aplicar en 17 minutos.

- **4 min** · Las tres cosas falsas [Slide 9].

**[Nota docente]:** la aritmética de Brooks se explica en treinta segundos y se queda: 5 personas son 10 parejas que se tienen que entender; 10 personas son 45. Es la razón por la que los equipos de este curso son de cinco.

### 00:55–01:12 · Taller en salas de grupo · [Slide 10]

**3 min** para repartir periodos y abrir la herramienta. El periodo de cada equipo **no se sortea hoy**: se asigna en orden, del equipo 1 al 5, para que las exposiciones queden en orden histórico sin reorganizar nada.

**14 min** de trabajo con los equipos ya en sus salas. Entre a las cinco salas con un orden fijo, unos 3 min en cada una, y en cada entrada revise **una sola cosa: el «qué sigue vivo hoy»**. Los otros tres campos los pueden buscar; ese no.

**[Nota docente]:** si un equipo se atasca con draw.io más de dos minutos, mándelo a Google Slides con cuadros de texto y siga. La herramienta no es lo evaluado y perder cinco minutos en una interfaz arruina el taller.

**[Nota docente]:** cuando un equipo escriba una cifra de internet («el 70 % de los proyectos fracasa»), pida fuente y año en el documento. Es el primer ejercicio de rigor bibliográfico del curso y se vuelve a pedir en la sesión 9.

### 01:12–01:27 · Exposiciones · [Slide 11]

**En orden histórico**, equipo 1 a equipo 5. Escriba el orden en el chat antes de empezar. 3 min por equipo, cronómetro en pantalla, habla el vocero con el diagrama ya compartido.

**[Nota docente]:** exija los cinco enlaces pegados en el chat antes de que empiece la primera exposición. Compartir pantalla con el cronómetro corriendo se come el turno.

**[Nota docente]:** no dé retroalimentación equipo por equipo. Anote y guarde todo para el cierre; cinco rondas de comentarios no caben en 15 min.

### 01:27–01:30 · Cierre · [Slide 12][Slide 13]

Una sola idea: **la disciplina nació de un fracaso de organización, no de un invento**, y los problemas de plazo, costo y requisitos que cambian siguen abiertos. El curso entero está puesto para que ellos no los repitan por ignorancia.

Anuncie el trabajo independiente y el tema de la sesión 3, y pida los enlaces en el chat.

## Errores frecuentes y cómo cortarlos en caliente

| Lo que dice el equipo | Por qué no sirve | Qué pedir en su lugar |
|---|---|---|
| «Antes no había internet / no había computadores» | Es una carencia de tecnología, no un problema. | Qué no podía hacer una persona concreta por eso. «Un banco no podía consultar un saldo desde otra ciudad». |
| «En 1968 hubo una conferencia importante» | No dice de qué se habló ni por qué importó. | El problema que llevó a convocarla y la palabra que salió de ahí. |
| «Royce inventó la cascada y estaba equivocado» | Royce propuso ese esquema advirtiendo que lineal es riesgoso. | Que lo cuenten con la advertencia incluida, y que digan de dónde sacaron la versión sin ella. |
| «El 70 % de los proyectos fracasa» | Es una cifra que circula sin fuente y con definiciones distintas de «fracaso». | Autor o institución y año. Si no lo tienen, que lo digan como afirmación general sin número. |
| «Sigue vigente hoy» (sin más) | Es la parte que más pesa y así escrita no dice nada. | Un ejemplo concreto que ellos hayan visto, aunque sea de este mismo curso. |

## Dudas frecuentes del estudiante

**¿Nos van a preguntar fechas en la evaluación de corte?**

No de memoria suelta. Lo que se evalúa es que puedan decir **qué problema resolvía** un hito y qué parte de ese problema sigue abierta. Una fecha sin problema asociado no vale nada en este curso.

**¿Tenemos que usar draw.io obligatoriamente?**

No. Es la recomendada porque abre sin cuenta y guarda en Drive, pero si no les funciona, Google Slides con cuadros de texto sirve igual. Lo que se califica es el contenido de los hitos.

**¿Podemos usar un video de YouTube como fuente?**

Sí, si dicen quién lo hizo y de qué año es, y si el video a su vez dice de dónde sacó los datos. Un video sin autor identificable no es fuente. En la sesión 9 se trabaja esto con más detalle.

**¿La línea de tiempo del trabajo independiente es la de mi equipo o la completa?**

La completa. Cada equipo expone su tramo y con los cinco tramos se arma la línea de tiempo entera de la disciplina: esa es la que hay que dejar en la carpeta del equipo esta semana.

## Notas operativas

- Las cinco salas de grupo se crean **antes** de empezar la sesión: abrirlas en vivo se come los 17 min del taller.
- El periodo de cada equipo se asigna por número de equipo, **no se sortea**, para que las exposiciones queden en orden histórico y el grupo se lleve una narración y no cinco fragmentos.
- Si un equipo pelea con draw.io más de dos minutos, mándelo a Google Slides. La herramienta no es lo evaluado.
- Esta clase es la primera vez que se exige fuente con autor y año. Dígalo explícitamente: es un criterio que se va a repetir en las Clases 9 y 13.
- El muro de Padlet de la apertura se relee en el minuto 25. Si no se relee, los diez minutos de apertura se desperdiciaron.

## Material de esta clase

- Deck: `Clases/Clase 2 - Historia y evolucion de la Ingenieria/Presentacion.pptx`
- Taller del estudiante: `Clases/Clase 2 - Historia y evolucion de la Ingenieria/Taller Clase 2 - Linea de tiempo del periodo.docx`
- Solución del taller (**solo docente**): `Kit docente/Clase 2/Solucion Taller Clase 2 - Linea de tiempo del periodo.docx`
- Este guion: `Kit docente/Clase 2/Guion Docente Clase 2 - Historia y evolucion de la Ingenieria.docx`

> **Recordatorio de datos personales:** ninguna actividad de este curso sube nombres, cédulas, teléfonos ni fotos de terceros. Si el caso del equipo los trae, se usa el rol («la dueña de la papelería», «el auxiliar de la biblioteca»).
