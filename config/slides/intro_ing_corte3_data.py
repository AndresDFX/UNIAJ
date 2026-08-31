# -*- coding: utf-8 -*-
"""Contenido de las clases 12 a 16 de Introduccion a la Ingenieria (FI300101) · Corte 3.

Este modulo SI lleva tildes: casi todo su texto acaba proyectado o convertido a .docx.
Nunca usar comillas dobles escapadas dentro de estos textos: se usan « ».

Material general para los tres grupos: nada de fechas, horas de pared ni codigos de grupo.

Hilo del corte 3 (40%): el prototipo de la sesion 11 se convierte en un proyecto presentable
y en un informe. Sesion 12 la prueba con una persona ajena y la retroalimentacion entre pares,
sesion 13 el impacto social y ambiental, sesion 14 la preparacion de la presentacion final,
sesion 15 la exposicion final (15%), sesion 16 el informe final (20%) y la autoevaluacion.

OJO con el desglose del corte 3: NO hay evaluacion escrita. El 40% se reparte en
exposicion final 15% (sesion 15) + informe final 20% (sesion 16) + asistencia 5%.
Las dos evaluaciones escritas del semestre son las de los cortes 1 y 2 (sesiones 6 y 11).

Cuatro de las cinco sesiones rompen el reparto estandar de bloques y usan `agenda_slots`,
porque exponer 5 equipos en 12 minutos cada uno no cabe en un bloque de 15 min.
"""

TEMAS = {}


# =============================================================================
# CLASE 12 · Presentacion de avances de proyectos
# =============================================================================
# Sesion con reparto propio: las exposiciones suben a 40 min (5 equipos x 8 min,
# 5 de avance + 3 de retroalimentacion del curso) porque la retroalimentacion
# entre pares ES el contenido de la sesion, no un adorno al final.

TEMAS[12] = {
    "n": 12,
    "titulo": "Presentación de avances de proyectos",
    "subtitulo": "Lo que falló cuando alguien de afuera usó su prototipo",
    "hook": "Ustedes probaron el prototipo con una persona ajena al equipo. "
            "¿Cuántas veces tuvieron que decirle «no, ahí no, toca acá»?",
    "hook_lines": [
        "Cada una de esas veces es un hallazgo, no un error de la persona.",
        "Hoy no venimos a mostrar lo que funciona: venimos a mostrar lo que falló.",
    ],
    "objetivos": [
        "Separar **lo que la persona hizo** de lo que la persona **dijo** en una prueba.",
        "Clasificar cada tropiezo por **tipo y gravedad**, y encontrar el **patrón**.",
        "Presentar un avance en 5 minutos: **el problema, lo que falló y la decisión pendiente**.",
        "Dar y recibir **retroalimentación útil**: observación en vez de opinión.",
    ],
    "agenda_slots": [
        ("Apertura", 8, "Pregunta de entrada en el muro"),
        ("Teoría y guía del docente", 20, "Cómo se lee una prueba y cómo se da retroalimentación"),
        ("Actividad en equipos", 12, "Armar la ficha de avance con los hallazgos de la prueba"),
        ("Exposiciones y retroalimentación", 40, "5 equipos × 8 min — 5 de avance y 3 de curso"),
        ("Cierre", 10, "El plan de ajustes de cada equipo, en el muro"),
    ],
    "agenda_sub": "Arranca el corte 3. Hoy las exposiciones se llevan casi la mitad de la sesión, "
                  "porque la retroalimentación del curso es el contenido y no el adorno",
    "nota_bloque": "**Sesión distinta a las anteriores.** El bloque de exposiciones sube a 40 "
                   "minutos: cada equipo tiene **5 minutos de avance y 3 minutos de "
                   "retroalimentación del curso**. La actividad en equipos baja a 12 minutos porque "
                   "el trabajo grueso —probar el prototipo con una persona ajena— **ya venía hecho "
                   "de la sesión 11**. Un equipo que no hizo la prueba no tiene avance que "
                   "presentar, y eso hay que decirlo en el minuto 2.",
    "agenda": {},
    "herramienta_nota": "El muro de **Padlet** de hoy tiene **una columna por equipo**: mientras un "
                        "equipo expone, los demás escriben ahí su retroalimentación, y así queda "
                        "por escrito y no se pierde. El equipo se lleva su columna. La ficha de "
                        "avance y el plan de ajustes van en el **documento del equipo** en Google "
                        "Drive. **Hoy no se usa asistente de IA.**",
    "avance_proyecto": "Ficha de avance con los hallazgos de la prueba, y el plan de ajustes que "
                       "sale de la retroalimentación del curso",

    "teoria": [
        {
            "tipo": "steps",
            "titulo": "Cómo se lee una prueba con una persona real",
            "steps": [
                ("1 · Separe lo que hizo de lo que dijo", "**Lo que hizo es el dato.** Si dudó cinco segundos frente a un botón, eso pasó — aunque después diga «no, estaba clarísimo». La gente es amable con quien le muestra su trabajo."),
                ("2 · Escriba el tropiezo, no la solución", "«Buscó el botón de volver en la esquina de arriba» es un hallazgo. «Hay que poner un botón arriba» es una conclusión, y es prematura."),
                ("3 · Clasifique cada tropiezo", "¿No entendió una palabra? ¿Se perdió en el flujo? ¿Esperaba algo que no existe? ¿Falló por una suposición nuestra? Cada tipo se arregla distinto."),
                ("4 · Busque el patrón", "Un tropiezo de una persona puede ser casualidad. **El mismo tropiezo en dos de tres personas es un defecto de diseño**, y esos son los que se arreglan primero."),
                ("5 · Decida qué NO se arregla", "No todo cabe antes de la sesión 14. Lo que se deja fuera **se escribe**, con su razón: eso es una decisión de ingeniería, no un olvido."),
            ],
            "sub": "La persona que prueba nunca se equivoca: si se perdió, el diseño la perdió",
        },
        {
            "tipo": "tabla",
            "titulo": "Los cuatro tipos de hallazgo y qué hacer con cada uno",
            "headers": ["Tipo", "Cómo se reconoce", "Qué se cambia"],
            "rows": [
                ["**Lenguaje**",
                 "Preguntó qué significa una palabra, o entendió otra cosa.",
                 "El **texto**. Es el arreglo más barato del mundo y el que más rinde."],
                ["**Flujo**",
                 "Hizo los pasos en otro orden, o se quedó sin saber dónde seguir.",
                 "El **orden de las pantallas** o el botón que falta. Cuesta más, pero es visible."],
                ["**Expectativa**",
                 "Buscó una función que no existe: «¿y aquí puedo reservarlo?».",
                 "Nada, si está fuera del alcance — pero **el prototipo debe decirlo**, no callarlo."],
                ["**Suposición nuestra**",
                 "Falló algo que dábamos por obvio: que tiene datos, que sabe leer una tabla.",
                 "La **restricción**. Es el hallazgo más caro y el más valioso de todos."],
            ],
            "note": "Los dos primeros tipos se arreglan antes de la sesión 14. Los dos últimos, a "
                    "veces, se declaran en el informe final y se dejan como trabajo siguiente.",
            "col_w": [2.1, 4.0, 3.7],
        },
        {
            "tipo": "cards",
            "titulo": "Qué es un avance y qué no",
            "cards": [
                ("Un avance NO es un resumen",
                 "Nadie necesita oír otra vez el problema completo, los actores y las seis fases. "
                 "**El curso ya conoce su proyecto**: lleva cinco sesiones oyéndolo."),
                ("Un avance ES lo que falló",
                 "Los tres hallazgos de la prueba, con lo que la persona **hizo**. Es lo único que "
                 "el curso no sabe todavía, y por eso es lo único que vale contar."),
                ("Un avance TRAE una pregunta",
                 "«Tenemos dos maneras de arreglar esto y no nos decidimos.» Ahí es donde los otros "
                 "cuatro equipos les sirven de algo. Sin pregunta, la retroalimentación es vacía."),
                ("Un avance ADMITE lo pendiente",
                 "Lo que todavía no está, dicho sin rodeos. **Esconder lo pendiente hoy es pagarlo "
                 "en la sesión 15**, delante de todo el mundo y con nota."),
            ],
            "columns": 2,
        },
        {
            "tipo": "steps",
            "titulo": "Cómo se da retroalimentación que sirve",
            "steps": [
                ("1 · Primero una pregunta, no una opinión", "«¿Por qué eligieron mostrar la fecha ahí?» antes de «la fecha está mal ahí». Muchas veces la respuesta ya cierra el tema."),
                ("2 · Describa lo que observó", "«Cuando mostraron la pantalla, no encontré cómo volver» dice más que «la navegación está confusa». **Lo observable se puede arreglar; una impresión no.**"),
                ("3 · Diga qué esperaba", "«Yo esperaba que el estado dijera cuándo vuelve.» Su expectativa es un dato, y no obliga a nadie: es información, no una orden."),
                ("4 · Una sola cosa, la más importante", "Cinco comentarios en tres minutos no se aplican. Uno bien dicho, sí. Elija el que más le cambiaría el proyecto al otro equipo."),
                ("5 · Sobre el trabajo, nunca sobre la persona", "«Este texto no lo entendí» y no «no supieron escribirlo». Es la diferencia entre un equipo que escucha y un equipo que se defiende."),
            ],
            "sub": "Regla del curso: observación, expectativa, y una sola cosa — en ese orden",
        },
        {
            "tipo": "box",
            "titulo": "Tres trampas de la retroalimentación entre pares",
            "notas": [
                ("advertencia",
                 "**El elogio vacío.** «Está muy bien, me gustó mucho» no es retroalimentación: es "
                 "amabilidad, y no le sirve a nadie. Si de verdad algo está bien, diga **qué** y "
                 "**por qué** — «el mensaje de error me dijo qué hacer» es un elogio útil, porque el "
                 "otro equipo aprende qué conservar."),
                ("advertencia",
                 "**Rediseñar el proyecto ajeno.** Aparece siempre: «yo lo habría hecho con una "
                 "aplicación». No es retroalimentación al avance, es otro proyecto. El otro equipo "
                 "tomó decisiones documentadas en las sesiones 6 a 11 que usted no vio; **hable de "
                 "lo que se presentó, no de lo que usted haría**."),
                ("aclaracion",
                 "**Tomarlo personal.** Recibir es más difícil que dar. Regla mientras les hablan: "
                 "**anotar, no responder.** Solo se pregunta para entender —«¿en qué momento se "
                 "perdió?»—. Defenderse en vivo desperdicia los únicos tres minutos gratis de "
                 "revisión externa que van a tener antes de la nota."),
            ],
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada: «no, ahí no, toca acá»",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "El gancho de hoy funciona porque todos los equipos van a reconocerse en él. Le "
                "pidieron a alguien ajeno que usara el prototipo y, casi con seguridad, en algún "
                "momento intervinieron: «no, ahí no, toca acá». Esa frase es el dato más valioso que "
                "el equipo tiene hoy, y viene disfrazada de incomodidad.",
                "El giro que hay que hacer explícito, y que es el eje de la sesión: **cada "
                "intervención es un hallazgo, no un error de la persona.** Si tuvieron que explicar "
                "algo, el prototipo no lo explicaba. Y en la vida real nadie va a estar al lado del "
                "usuario para aclarárselo. Vale la pena decirlo con una frase que se les quede: **la "
                "persona que prueba nunca se equivoca; si se perdió, el diseño la perdió.**",
                "Aproveche la apertura para tomar el pulso operativo: en el muro, cada equipo "
                "escribe **cuántas veces tuvo que intervenir**. Ese número, además de romper el "
                "hielo, le dice de inmediato quién hizo la prueba y quién no. Un equipo que "
                "responde «ninguna, quedó perfecto» casi siempre no probó, o probó con la mamá de un "
                "integrante mientras le explicaba todo.",
                "Y aquí conviene ser directo, porque es la primera sesión del corte 3 y las reglas "
                "se fijan hoy: **un equipo que no hizo la prueba no tiene avance que presentar.** No "
                "se le puede improvisar retroalimentación a un avance inexistente. Si ocurre, "
                "dígalo, deje que expongan lo que tengan y que hagan la prueba antes de la sesión "
                "13 — pero que quede claro que arrancaron el corte con desventaja.",
            ],
        },
        {
            "titulo": "Lo que hizo vale más que lo que dijo, y el patrón vale más que el caso",
            "slide": "{{slide:Cómo se lee una prueba}} {{slide:Los cuatro tipos de hallazgo}}",
            "cuerpo": [
                "**Paso 1: separar lo que hizo de lo que dijo.** Esta es la idea central y hay que "
                "insistir en ella. Cuando alguien prueba el trabajo de un amigo, es amable: dice que "
                "estaba claro, que le gustó, que es intuitivo. Y sin embargo dudó cinco segundos "
                "frente a un botón, se equivocó de pantalla y preguntó qué significaba una palabra. "
                "**Lo que hizo es el dato; lo que dijo es cortesía.** No es que la persona mienta: "
                "es que nadie quiere hacer sentir mal a quien le muestra algo con orgullo. Por eso "
                "en la industria se observa y se cronometra, en vez de preguntar «¿le gustó?» — "
                "exactamente la trampa que vieron en la sesión 8.",
                "**Paso 2: escribir el tropiezo, no la solución.** Los estudiantes van a saltar "
                "directo a arreglar. Hay que frenarlos: «buscó el botón de volver arriba» es un "
                "hecho; «hay que poner un botón arriba» es una conclusión que quizá no sea la mejor. "
                "Si se anota la conclusión y se pierde el hecho, ya no se puede pensar de nuevo.",
                "**Pasos 3 y 4: clasificar y buscar el patrón.** La tabla de los cuatro tipos es la "
                "herramienta de la sesión, y su valor es que **cada tipo se arregla con un trabajo "
                "distinto y a un costo distinto**. Un hallazgo de lenguaje se arregla cambiando una "
                "palabra: es el arreglo más barato que existe y el que más rinde, lo cual conecta con "
                "el bloque de textos reales de la sesión 10. Uno de flujo exige reordenar pantallas. "
                "Uno de expectativa muchas veces **no se arregla**, porque está fuera del alcance de "
                "la sesión 8, pero obliga a que el prototipo lo diga en vez de callarlo. Y uno de "
                "suposición nuestra es el más caro y el más valioso: descubrir que dábamos por obvio "
                "que el usuario tiene datos móviles, o que sabe leer una tabla, cambia una "
                "restricción del proyecto.",
                "Sobre el patrón, dé el criterio operativo sin pretensiones de rigor estadístico: "
                "**un tropiezo en una persona puede ser casualidad; el mismo tropiezo en dos de tres "
                "personas es un defecto de diseño.** Con tres o cinco pruebas no se hace "
                "estadística, y hay que decirlo — pero sí se hace ingeniería: la práctica "
                "profesional de pruebas de usabilidad trabaja con muy pocos usuarios justamente "
                "porque los defectos gruesos aparecen con los primeros. Si algún equipo probó con "
                "una sola persona, dígale que el hallazgo sigue valiendo, pero que no sabe si es "
                "patrón.",
                "**Paso 5: decidir qué no se arregla.** Es el paso que separa a un equipo que "
                "entendió el curso de uno que no. No todo cabe antes de la sesión 14, y **lo que se "
                "deja fuera se escribe con su razón**. Eso ya lo practicaron con el alcance mínimo "
                "de la sesión 8 y con los descartes de la sesión 11: es la misma disciplina.",
            ],
        },
        {
            "titulo": "Qué es un avance: cinco minutos que no repiten nada",
            "slide": "{{slide:Qué es un avance y qué no}}",
            "cuerpo": [
                "El error universal en una presentación de avance es empezar por el principio. El "
                "equipo vuelve a contar el problema, los actores, el árbol de causas y las seis "
                "fases, y cuando llega a lo interesante se le acabó el tiempo. Hay que cortarlo de "
                "raíz con un argumento simple: **el curso ya conoce su proyecto**, lleva cinco "
                "sesiones oyéndolo. Repetirlo es gastar los cinco minutos en lo único que ya no "
                "aporta.",
                "Lo que sí es un avance: **los tres hallazgos de la prueba**, contados por lo que la "
                "persona hizo. Eso es lo único que el curso no sabe, y por lo tanto lo único que "
                "vale la pena contar. Una frase útil para dárselo como regla: *en un avance se "
                "cuenta lo que cambió desde la última vez, no lo que se es.*",
                "Y una exigencia que cambia radicalmente la calidad de la sesión: **cada avance tiene "
                "que traer una pregunta abierta.** «Tenemos dos maneras de arreglar esto y no nos "
                "decidimos» convierte los tres minutos de retroalimentación en algo útil; sin "
                "pregunta, los otros equipos improvisan comentarios genéricos. Exíjala explícitamente "
                "al repartir el taller —es uno de los cuatro bloques de la ficha— y verá la "
                "diferencia.",
                "Por último, la parte incómoda: **admitir lo pendiente**. Los equipos tienden a "
                "maquillar el avance porque hay compañeros mirando. El argumento que funciona no es "
                "moral sino de conveniencia: **esconder lo pendiente hoy es pagarlo en la sesión "
                "15**, cuando ya hay nota de por medio y ya no hay tiempo de arreglarlo. Hoy la "
                "retroalimentación es gratis; en la sesión 15 vale el 15 % del curso.",
            ],
        },
        {
            "titulo": "Dar y recibir: la única revisión externa gratis del semestre",
            "slide": "{{slide:Cómo se da retroalimentación}} {{slide:Tres trampas de la retroalimentación}}",
            "cuerpo": [
                "La retroalimentación entre pares no sale bien sola: sin reglas, un grupo de primer "
                "semestre produce diez minutos de «está muy bien, me gustó». Por eso hoy se enseña "
                "el formato, y conviene proyectarlo mientras exponen.",
                "El orden **observación, expectativa, una sola cosa** funciona por razones "
                "concretas. Empezar con una **pregunta** en vez de una opinión evita la mitad de los "
                "comentarios equivocados, porque muchas veces el equipo ya tenía una razón "
                "documentada: preguntar «¿por qué eligieron mostrar la fecha ahí?» y oír «porque la "
                "información no está al minuto y no queremos mentir» cierra el tema y además enseña "
                "al que preguntó. Describir **lo observable** —«no encontré cómo volver»— entrega "
                "algo que se puede arreglar, mientras que «la navegación está confusa» solo entrega "
                "una impresión. Decir **qué esperaba** aporta un dato sin dar una orden. Y limitarse "
                "a **una sola cosa** es aritmética: en tres minutos con cinco comentarios no se "
                "aplica ninguno.",
                "La regla de **hablar del trabajo y no de la persona** hay que enunciarla en voz "
                "alta la primera vez, porque marca el clima del corte 3 completo: «este texto no lo "
                "entendí» y no «no supieron escribirlo». Es la diferencia entre un equipo que "
                "escucha y un equipo que se defiende.",
                "De las tres trampas, la que más daño hace es **rediseñar el proyecto ajeno**: "
                "aparece siempre, en la forma de «yo lo habría hecho con una aplicación». Hay que "
                "cortarla con respeto y con argumento: el otro equipo tomó decisiones documentadas "
                "en las sesiones 6 a 11 que usted no vio, y **la retroalimentación es al avance "
                "presentado, no al proyecto que usted haría**. La segunda es el **elogio vacío**, "
                "que se arregla pidiendo el «qué» y el «por qué» —un elogio con razón sí es útil, "
                "porque le dice al equipo qué conservar—. Y la tercera es de quien recibe: "
                "**anotar, no responder**. Solo se pregunta para entender. Cierre con el argumento "
                "de peso: estos tres minutos son **la única revisión externa gratis** que van a "
                "tener antes de que la exposición valga nota; defenderse en vivo es tirarlos a la "
                "basura.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:08 · Apertura · [Slide 4]",
            "cuerpo": [
                "Comparta pantalla antes de que entre el primero:",
                "> «Ustedes probaron el prototipo con una persona ajena al equipo. ¿Cuántas veces "
                "tuvieron que decirle «no, ahí no, toca acá»?»",
                "En el muro, cada equipo escribe **el número**. Eso rompe el hielo y le dice de "
                "inmediato quién hizo la prueba.",
                "**[Nota docente]:** anuncie el reparto de hoy —teoría 20, taller 12, **exposiciones "
                "y retroalimentación 40**, cierre 10— y diga la regla: **quien no hizo la prueba no "
                "tiene avance que presentar.** Es la primera sesión del corte 3 y las reglas se "
                "fijan hoy.",
                "**[Nota docente]:** si un equipo responde «ninguna, quedó perfecto», pregunte con "
                "quién probaron y si le explicaron mientras usaba. Casi siempre ahí está la "
                "respuesta.",
            ],
        },
        {
            "titulo": "00:08–00:28 · Teoría (20 min) · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]",
            "cuerpo": [
                "Reparto:",
                "- **5 min** · Cómo se lee una prueba [Slide 5]. La frase que se tiene que quedar: "
                "**lo que hizo es el dato; lo que dijo es cortesía.**",
                "- **4 min** · Los cuatro tipos de hallazgo [Slide 6]. Señale que el de **lenguaje** "
                "es el arreglo más barato y el de **suposición nuestra** el más valioso.",
                "- **4 min** · Qué es un avance [Slide 7]. Diga tres veces que **no se repite el "
                "problema** y que **cada avance trae una pregunta abierta**.",
                "- **5 min** · Cómo se da retroalimentación [Slide 8]. Deje esta diapositiva "
                "proyectada durante todas las exposiciones.",
                "- **2 min** · Las tres trampas [Slide 9]. Enuncie en voz alta la regla de quien "
                "recibe: **anotar, no responder.**",
            ],
        },
        {
            "titulo": "00:28–00:40 · Taller en salas de grupo (12 min) · [Slide 10]",
            "cuerpo": [
                "Bloque corto a propósito: el trabajo grueso ya venía hecho. Ritmo:",
                "- 5 min · escribir los tres hallazgos **como lo que la persona hizo**.",
                "- 3 min · clasificarlos y marcar el patrón.",
                "- 4 min · decidir qué se arregla, qué no, y **cuál es la pregunta para el curso**.",
                "**[Nota docente]:** entre a las cinco salas con una sola consigna: **exija la "
                "pregunta abierta.** Un equipo sin pregunta desperdicia sus tres minutos de "
                "retroalimentación y hace que los otros improvisen.",
                "**[Nota docente]:** abra el muro de Padlet con **una columna por equipo** antes de "
                "que salgan de las salas, y ponga el enlace en el chat.",
            ],
        },
        {
            "titulo": "00:40–01:20 · Exposiciones y retroalimentación (40 min) · [Slide 11]",
            "cuerpo": [
                "5 equipos × 8 min: **5 de avance y 3 de retroalimentación del curso**. Cronómetro en "
                "pantalla, se corta al llegar a cero.",
                "Mientras un equipo expone, los otros cuatro escriben **en la columna de ese equipo** "
                "en el muro. Así la retroalimentación queda por escrito y no se pierde.",
                "**[Nota docente]:** en los tres minutos, dé la palabra a **dos equipos distintos** y "
                "haga cumplir el formato: observación, expectativa, una sola cosa. Si alguien empieza "
                "a rediseñar el proyecto ajeno, córtelo con respeto y explique por qué.",
                "**[Nota docente]:** el equipo que recibe **anota y no responde**; solo pregunta para "
                "entender. Recuérdelo la primera vez y no hará falta repetirlo.",
                "**[Nota docente]:** aporte usted **un** comentario por equipo, al final de los tres "
                "minutos, y que sea el que nadie dijo. No repita lo que ya dijeron los compañeros.",
            ],
        },
        {
            "titulo": "01:20–01:30 · Cierre · [Slide 12][Slide 13]",
            "cuerpo": [
                "Cada equipo escribe en su columna del muro **las dos cosas que va a ajustar** con lo "
                "que oyó hoy. Dos minutos, y queda el compromiso por escrito.",
                "Una idea: **la persona que prueba nunca se equivoca; si se perdió, el diseño la "
                "perdió.**",
                "Anuncie la sesión 13: **el impacto social y ambiental** del proyecto — a quién más "
                "afecta esto, aunque no lo use. Vuelve el listado de actores no usuarios de la "
                "sesión 3.",
            ],
        },
    ],

    "taller": {
        "archivo": "Ficha de avance y plan de ajustes",
        "titulo": "Ficha de avance y plan de ajustes",
        "min": 12,
        "exposicion": 5,
        "consigna": "Con los resultados de la prueba que ya hicieron, armen la ficha de avance: "
                    "**tres hallazgos contados por lo que la persona hizo**, su clasificación y "
                    "gravedad, qué se arregla y qué no, y **la pregunta abierta que le hacen al "
                    "curso**. Después de la retroalimentación, el plan de ajustes.",
        "entregable": "la ficha de avance en el documento del equipo, y —al cerrar— las dos cosas que "
                      "van a ajustar escritas en su columna del muro de Padlet",
        "entregable_corto": "ficha de avance + las dos cosas que se van a ajustar en el muro",
        "reparto_titulo": "Ritmo sugerido dentro de la sala (12 min):",
        "reparto": "5 min escribir los tres hallazgos como **lo que la persona hizo** · 3 min "
                   "clasificarlos y marcar el patrón · 4 min decidir qué se arregla, qué no y **cuál "
                   "es la pregunta para el curso**. El bloque es corto porque el trabajo grueso —la "
                   "prueba— ya venía hecho de la sesión 11.",
        "reparto_corto": "12 min: hallazgos, clasificación, decisión y la pregunta al curso",
        "bloques": [
            {"clave": "LOS TRES HALLAZGOS",
             "pide": "Tres tropiezos de la prueba, escritos como **lo que la persona hizo o "
                     "preguntó** — no como lo que dijo al final, y no como la solución.",
             "check": "cada hallazgo describe una acción observable. «Le pareció confuso» no es un hallazgo; «dudó cinco segundos frente al botón de volver» sí."},
            {"clave": "LA CLASIFICACIÓN Y EL PATRÓN",
             "pide": "El tipo de cada hallazgo —lenguaje, flujo, expectativa o suposición nuestra— y "
                     "si se repitió en más de una persona.",
             "check": "los tipos están bien asignados y se dice explícitamente cuáles son patrón y cuáles casos aislados."},
            {"clave": "QUÉ ARREGLAMOS Y QUÉ NO",
             "pide": "Lo que se arregla antes de la sesión 14, y **lo que no se arregla con su "
                     "razón**: fuera del alcance, no alcanza el tiempo, o cambia una restricción.",
             "check": "hay al menos una cosa en la lista de «no se arregla», con razón. Un equipo que dice que va a arreglar todo no priorizó."},
            {"clave": "LA PREGUNTA PARA EL CURSO",
             "pide": "Una pregunta abierta, concreta, sobre una decisión que el equipo no logra "
                     "tomar. Es lo que hace útiles los tres minutos de retroalimentación.",
             "check": "es una pregunta de verdad y no un «¿qué opinan?». Debe tener al menos dos alternativas identificadas."},
        ],
        "expo": [
            ("30 s · Recordatorio mínimo", "El problema en **una frase**. Nada más: el curso ya conoce su proyecto."),
            ("2 min · Los tres hallazgos", "Lo que la persona **hizo**. Es el corazón del avance."),
            ("1 min · Qué arreglan y qué no", "Y por qué lo que queda fuera queda fuera."),
            ("1 min · La pregunta para el curso", "Con las dos alternativas que están considerando."),
            ("30 s · Cierre", "Qué van a tener listo para la sesión 14."),
        ],
    },

    "rubrica": [
        ("Los tres hallazgos describen acciones observables de la persona, no opiniones", 30,
         "Es la competencia central de la sesión: separar el dato de la cortesía."),
        ("Cada hallazgo está clasificado y se distingue el patrón del caso aislado", 20,
         "Sin clasificación no se puede priorizar, porque cada tipo cuesta distinto arreglarlo."),
        ("Hay una lista explícita de lo que NO se arregla, con su razón", 25,
         "Priorizar es una decisión de ingeniería; querer arreglar todo es no haber decidido."),
        ("La pregunta al curso es concreta y tiene alternativas identificadas", 15,
         "Es lo que convierte la retroalimentación entre pares en algo útil."),
        ("El plan de ajustes recoge por escrito lo que se oyó en la retroalimentación", 10,
         "Recibir retroalimentación y no anotarla equivale a no haberla pedido."),
    ],

    "solucion": {
        "para_que": "Este documento trae la ficha de avance completa del caso de la biblioteca, con "
                    "los tres hallazgos redactados **como acciones observables** — que es lo que más "
                    "cuesta y donde el docente va a tener que corregir más—. Si solo alcanza a leer "
                    "un bloque antes de clase, que sea **LOS TRES HALLAZGOS**: la diferencia entre "
                    "un hallazgo bien y mal escrito está ahí, lado a lado.",
        "caso_titulo": "La biblioteca del barrio · prueba del prototipo v2 con dos personas ajenas",
        "caso": "Prototipo v2 de la sesión 11: tres pantallas —consultar, resultado con sus tres "
                "estados, y actualizar para la voluntaria—, con la fecha de última actualización "
                "visible y sin cuentas de usuario. Se probó con dos personas ajenas al equipo: un "
                "vecino de 34 años que usa el celular todos los días, y una señora de 61 que usa "
                "sobre todo mensajería. A cada uno se le dio una tarea —«averigüe si está *Cien años "
                "de soledad*»— sin explicarle nada, y el equipo solo observó y anotó.",
        "por_que_este_caso": "Porque los hallazgos de las dos personas no coinciden, y esa "
                             "discrepancia es la lección: uno de los tropiezos es patrón y los otros "
                             "son de una sola persona, así que se priorizan distinto. Además aparece "
                             "el hallazgo más caro de todos —una suposición del equipo—, que obliga a "
                             "reconocer una limitación en vez de arreglar una pantalla.",
        "bloques": [
            {
                "clave": "LOS TRES HALLAZGOS",
                "respuesta": "**Hallazgo 1 · Las dos personas tocaron el estado «Prestado» esperando "
                             "que se abriera algo.**\n\n"
                             "El vecino lo tocó dos veces y después dijo «no hace nada». La señora lo "
                             "tocó una vez, esperó, y preguntó «¿y aquí me dice cuándo llega?». "
                             "**Ninguno de los dos comentó nada al final de la prueba**: el vecino "
                             "dijo que todo estaba claro.\n\n"
                             "**Hallazgo 2 · La señora leyó la fecha de actualización y preguntó si "
                             "eso significaba que el libro se había prestado ese día.**\n\n"
                             "Se quedó unos segundos en la línea «Lista actualizada el viernes a las "
                             "6:00 p. m.» y la interpretó como la fecha del préstamo, no como la "
                             "fecha del dato. El vecino no la miró.\n\n"
                             "**Hallazgo 3 · La señora escribió «cien años» con el teclado y no "
                             "apareció nada, porque escribió «100 años».**\n\n"
                             "Después intentó dos veces más y abandonó: le pasó el celular a un "
                             "integrante del equipo. El vecino escribió «cien» y encontró el "
                             "resultado sin problema.\n\n"
                             "---\n\n"
                             "**Comparación · así NO se escribe un hallazgo**, para mostrar en clase:\n\n"
                             "| Mal escrito | Bien escrito |\n"
                             "|---|---|\n"
                             "| «Le pareció confusa la pantalla de resultado.» | «Tocó el estado "
                             "«Prestado» dos veces esperando que se abriera algo.» |\n"
                             "| «Hay que poner la fecha más clara.» | «Leyó la fecha de actualización "
                             "y la interpretó como la fecha del préstamo.» |\n"
                             "| «El buscador no funciona bien.» | «Escribió «100 años» en vez de "
                             "«cien años», no obtuvo resultados y abandonó al tercer intento.» |\n\n"
                             "La columna izquierda tiene tres problemas: **es una opinión, no un "
                             "hecho**; **mezcla el hallazgo con la solución**; y **no se puede "
                             "verificar**. La derecha se puede volver a probar.",
                "como_calificar": "30 pts, 10 por hallazgo. La verificación es una sola pregunta: "
                                  "**¿describe algo que se pueda volver a observar?** Si dice «le "
                                  "pareció», «no le gustó», «estaba confuso», vale 3 — y hay que "
                                  "reescribirlo con el equipo ahí mismo, porque es la competencia "
                                  "central de la sesión. Valore especialmente al equipo que anota "
                                  "**la contradicción entre lo que la persona hizo y lo que dijo** "
                                  "(«dijo que estaba claro, pero lo tocó dos veces»): eso es "
                                  "observación de nivel profesional."
            },
            {
                "clave": "LA CLASIFICACIÓN Y EL PATRÓN",
                "respuesta": "| Hallazgo | Tipo | ¿Patrón? |\n"
                             "|---|---|---|\n"
                             "| 1 · Tocaron «Prestado» esperando algo | **Expectativa** — esperan una "
                             "función que no existe (saber cuándo vuelve) | **Sí: 2 de 2 personas** |\n"
                             "| 2 · Interpretó mal la fecha de actualización | **Lenguaje** — el "
                             "rótulo no dice de qué es la fecha | No: 1 de 2 |\n"
                             "| 3 · Escribió «100 años» y abandonó | **Suposición nuestra** — dimos "
                             "por hecho que el título se escribe como está en la lista | No: 1 de 2, "
                             "pero **gravedad alta** |\n\n"
                             "**Lo que se aprende de la tabla, y hay que decirlo en voz alta:**\n\n"
                             "- El **hallazgo 1 es el único patrón** —le pasó a las dos personas— y "
                             "por eso es el primero que se atiende. Y nótese que **es de tipo "
                             "expectativa**: la función que esperan (saber cuándo vuelve el libro) "
                             "quedó fuera del alcance mínimo en la sesión 8. Entonces no se agrega la "
                             "función: **se cambia el prototipo para que no prometa lo que no hace.**\n"
                             "- El **hallazgo 3 no es patrón pero es grave**, y ahí está la lección "
                             "sobre el criterio: patrón y gravedad son dos cosas distintas. Le pasó a "
                             "una sola persona, pero esa persona **abandonó la tarea**, que es el peor "
                             "resultado posible de una prueba. Un tropiezo que termina en abandono "
                             "pesa más que uno que termina en duda.\n"
                             "- El **hallazgo 2 es el más barato de todos**: se arregla cambiando "
                             "cuatro palabras del rótulo.",
                "como_calificar": "20 pts: 12 por la asignación correcta de tipos (4 cada uno) y 8 "
                                  "por distinguir explícitamente patrón de caso aislado. El error más "
                                  "común y el más interesante para corregir es clasificar el hallazgo "
                                  "3 como «flujo» o «lenguaje» en vez de **suposición nuestra**: si "
                                  "pasa, pregunte «¿qué dábamos por obvio?» y el equipo llega solo. "
                                  "Valore con puntos extra —dígalo en la retroalimentación— al equipo "
                                  "que separa **patrón** de **gravedad** en vez de tratarlos como lo "
                                  "mismo."
            },
            {
                "clave": "QUÉ ARREGLAMOS Y QUÉ NO",
                "respuesta": "**Se arregla antes de la sesión 14:**\n\n"
                             "1. **El estado «Prestado» deja de parecer un botón** y pasa a ser una "
                             "etiqueta gris sin borde, con el texto «Prestado · no sabemos cuándo "
                             "vuelve». *Hallazgo 1, el patrón.* Nótese que **no agregamos la función, "
                             "hacemos honesta la pantalla**: es la misma decisión que tomamos con la "
                             "fecha de actualización en la sesión 10.\n"
                             "2. **El rótulo de la fecha cambia** de «Lista actualizada el viernes a "
                             "las 6:00 p. m.» a «Esta información es del viernes a las 6:00 p. m.». "
                             "*Hallazgo 2.* Cuatro palabras, cinco minutos de trabajo.\n"
                             "3. **La pantalla de consulta gana una línea de ayuda**: «Escriba parte "
                             "del título o del autor». *Hallazgo 3, mitigación parcial.*\n\n"
                             "**No se arregla, y por qué:**\n\n"
                             "1. **La búsqueda que tolera «100» por «cien», tildes de más y errores de "
                             "escritura.** *Razón:* es un cambio en la lógica de búsqueda, no en el "
                             "prototipo, y **excede lo que el equipo puede construir en el semestre**. "
                             "Queda en el informe final como la **primera limitación conocida** y "
                             "como el trabajo siguiente número uno. Se declara, no se esconde.\n"
                             "2. **La función de avisar cuándo vuelve el libro.** *Razón:* quedó fuera "
                             "del alcance mínimo en la sesión 8, y la manera de avisar —correo o "
                             "mensaje— exigiría pedir datos personales, que está descartado desde la "
                             "sesión 4 por la Ley 1581 de 2012. **Está en «versión siguiente» y ahí "
                             "se queda.**\n"
                             "3. **Un buscador con sugerencias mientras se escribe.** *Razón:* rompe "
                             "el límite de 200 KB por consulta, que es el requisito no funcional "
                             "derivado del indicador ambiental de la sesión 5.\n\n"
                             "**Lo importante de esta lista:** los tres «no» tienen razones de tres "
                             "tipos distintos —capacidad del equipo, alcance más ley, y una "
                             "restricción técnica—, y las tres estaban escritas antes de hoy. Un "
                             "equipo con sus decisiones documentadas puede decir «no» con argumento; "
                             "uno sin ellas solo puede decir «no nos alcanzó el tiempo».",
                "como_calificar": "25 pts: 12 por la lista de lo que se arregla con su hallazgo "
                                  "asociado, y **13 por la lista de lo que NO se arregla con razón "
                                  "verificable**. El criterio duro: si la lista de «no se arregla» "
                                  "está vacía, el bloque vale 8 como máximo, y hay que explicar por "
                                  "qué —querer arreglar todo en dos sesiones no es ambición, es "
                                  "ausencia de priorización—. Valore mucho el equipo que resuelve un "
                                  "hallazgo **haciendo honesta la pantalla en vez de agregando la "
                                  "función**: es la lección de diseño más difícil del corte."
            },
            {
                "clave": "LA PREGUNTA PARA EL CURSO",
                "respuesta": "**La pregunta del equipo:**\n\n"
                             "> Cuando alguien busca un libro que **no está en la lista**, tenemos dos "
                             "maneras de responder y no nos decidimos:\n>\n"
                             "> **(A)** «No encontramos «X» en la lista» — honesto, pero deja a la "
                             "persona sin saber si el libro no existe en la biblioteca o si "
                             "simplemente nadie lo ha registrado todavía.\n>\n"
                             "> **(B)** «No encontramos «X». La lista solo incluye los libros que se "
                             "prestan seguido; puede haber otros en el estante» — más completo, pero "
                             "es un párrafo, y en la sesión 10 aprendimos que los textos largos no se "
                             "leen.\n>\n"
                             "> ¿Cuál sirve más para una persona que está decidiendo si camina hasta "
                             "la biblioteca?\n\n"
                             "**Por qué esta pregunta está bien hecha**, y conviene señalarlo en "
                             "clase: es **concreta** (un mensaje específico, no «¿qué opinan del "
                             "proyecto?»), tiene **dos alternativas identificadas** con su pro y su "
                             "contra, y **el equipo ya pensó** —no está tercerizando el trabajo—. Con "
                             "una pregunta así, tres minutos de retroalimentación alcanzan para "
                             "decidir.\n\n"
                             "**Lo que el curso respondió** (útil para el docente como ejemplo de "
                             "retroalimentación bien dada): un equipo observó que la duda real de la "
                             "persona no es «existe o no existe» sino «camino o no camino», así que la "
                             "respuesta tiene que incluir **qué hacer**: «No encontramos «X» en la "
                             "lista. Puede haber otros libros en el estante — pregunte en el "
                             "mostrador». Es la opción B recortada, y aplica la regla de la sesión 10: "
                             "un mensaje de error dice qué hacer.",
                "como_calificar": "15 pts. Tres cosas: que sea una pregunta **concreta** y no un «¿qué "
                                  "opinan?» (6), que tenga **al menos dos alternativas** identificadas "
                                  "(6), y que el equipo muestre que ya pensó —cada alternativa con su "
                                  "pro y su contra— (3). Un «¿qué le mejorarían?» vale 3 y hay que "
                                  "decir por qué: convierte los tres minutos en comentarios genéricos "
                                  "y desperdicia a los otros cuatro equipos."
            },
        ],
        "variantes": [
            {"caso": "Equipos que no hicieron la prueba",
             "clave": "Va a pasar con uno o dos equipos, y hay que manejarlo sin drama y sin "
                      "premiarlo. Que expongan lo que tengan —el prototipo v2 y su pregunta— y que "
                      "hagan la prueba **antes de la sesión 13**, con dos personas. Dígalo claro: "
                      "los hallazgos son insumo obligatorio del informe final, así que no es un "
                      "entregable que se pueda saltar, solo se puede atrasar. Y señale el costo "
                      "real: perdieron los tres minutos de retroalimentación del curso sobre lo que "
                      "más importaba."},
            {"caso": "Equipos que probaron con un familiar y le explicaron mientras usaba",
             "clave": "El resultado es una prueba sin información, y hay que explicar por qué sin "
                      "regañar: si usted explica, está probando su explicación, no el prototipo. La "
                      "salida es corta: una segunda prueba de cinco minutos con alguien más, con la "
                      "regla de **dar una tarea y callarse**. Cinco minutos de silencio dan más "
                      "datos que media hora de acompañamiento."},
            {"caso": "Equipos con hallazgos que se contradicen entre las dos personas",
             "clave": "No es un problema: es el caso normal y es la razón de ser del criterio de "
                      "patrón. Lo que hay que exigir es que **no promedien**. Si a uno le funcionó y "
                      "al otro no, se anota así, se marca como caso aislado, y se decide con la "
                      "gravedad: un tropiezo que terminó en abandono pesa más que uno que terminó en "
                      "duda, aunque le haya pasado a una sola persona."},
            {"caso": "Proyectos de proceso o gestión, sin pantallas",
             "clave": "La prueba es la misma cambiando el objeto: se le pide a una persona ajena que "
                      "**siga el procedimiento o llene el formato** sin ayuda. Los cuatro tipos de "
                      "hallazgo aplican tal cual —una casilla que no se entiende es lenguaje, un paso "
                      "que se hace en otro orden es flujo—. El hallazgo de suposición aparece igual: "
                      "«dimos por hecho que sabía qué es un radicado»."},
        ],
        "cierre": "Diez minutos, y conviene usarlos bien porque cierran la primera sesión del corte "
                  "3. Pida que cada equipo escriba en su columna del muro **las dos cosas que va a "
                  "ajustar** con lo que oyó: dos minutos, y el compromiso queda por escrito y "
                  "verificable en la sesión 14. Después, la idea de la sesión, dicha completa: **la "
                  "persona que prueba nunca se equivoca; si se perdió, el diseño la perdió.** Vale la "
                  "pena agregar la versión profesional de eso, porque les va a servir toda la "
                  "carrera: en ingeniería el trabajo no se evalúa por lo que el autor cree que "
                  "quedó claro, sino por lo que un tercero logra hacer con él. Y cierre con la "
                  "cuenta que importa: **la retroalimentación de hoy fue gratis; la de la sesión 15 "
                  "vale el 15 % del curso.** Anuncie la sesión 13 —el impacto social y ambiental, "
                  "donde vuelve el listado de actores no usuarios de la sesión 3— y recuerde que el "
                  "prototipo ajustado se necesita para la sesión 14, no para la 15.",
        "conexion": "Hacia atrás: la **sesión 11** dejó el prototipo v2 y la tarea de probarlo; la "
                    "**sesión 10** dejó la regla de los textos reales y de los mensajes que dicen qué "
                    "hacer, que hoy resuelve dos de los tres hallazgos; la **sesión 8** dejó el "
                    "alcance mínimo, que es la razón por la que un hallazgo **no** se arregla; la "
                    "**sesión 5** dejó el límite de 200 KB; la **sesión 4** dejó la Ley 1581, que "
                    "cierra la puerta a la función de avisos. Hacia adelante: la **sesión 13** evalúa "
                    "el impacto social y ambiental de la solución; la **sesión 14** convierte todo "
                    "esto en la presentación final; y en el **informe final de la sesión 16** los "
                    "hallazgos de hoy son la sección de resultados de la prueba, y la lista de «no se "
                    "arregla» es la sección de limitaciones conocidas.",
    },

    "errores": [
        {"dice": "«Le pareció confusa la pantalla»",
         "por_que": "Es una opinión, no se puede verificar y no dice qué cambiar. Además suele ser la versión amable de lo que en realidad pasó.",
         "pida": "La acción: «tocó el estado dos veces esperando que se abriera algo». Eso sí se puede volver a probar."},
        {"dice": "«Dijo que estaba todo clarísimo»",
         "por_que": "La gente es amable con quien le muestra su trabajo. Lo que dijo es cortesía; lo que hizo es el dato.",
         "pida": "Lo que hizo mientras usaba: dónde dudó, dónde se equivocó, qué preguntó. Y si hay contradicción, que la anoten: es el mejor hallazgo."},
        {"dice": "Un hallazgo que ya viene con la solución adentro",
         "por_que": "Si se anota «hay que poner un botón arriba» y se pierde el hecho, ya no se puede pensar otra solución mejor.",
         "pida": "Primero el hecho, después la decisión. Son dos columnas distintas de la ficha."},
        {"dice": "«Vamos a arreglar todo antes de la sesión 14»",
         "por_que": "No cabe, y decirlo es no haber priorizado. Priorizar es una decisión de ingeniería, no una rendición.",
         "pida": "Qué queda fuera y por qué: fuera del alcance, excede la capacidad del equipo, o rompe una restricción."},
        {"dice": "«¿Qué le mejorarían a nuestro proyecto?»",
         "por_que": "Como pregunta al curso es demasiado abierta: produce comentarios genéricos y desperdicia a los otros cuatro equipos.",
         "pida": "Una decisión concreta con dos alternativas, cada una con su pro y su contra."},
    ],

    "dudas": [
        {"p": "¿Con cuántas personas hay que probar?",
         "r": "Con dos o tres basta para lo que necesitamos hoy. Con tan pocas pruebas **no se hace "
              "estadística** y hay que ser honestos con eso, pero sí se encuentran los defectos "
              "gruesos: es la práctica normal en pruebas de usabilidad, porque los primeros usuarios "
              "tropiezan justo con lo que está mal diseñado. Lo que **no** sirve es probar con cero "
              "personas, ni probar con alguien a quien se le explica mientras usa."},
        {"p": "¿Y si la persona no logró terminar la tarea?",
         "r": "Es el hallazgo más importante de todos, y hay que registrarlo así: **abandono**. Un "
              "tropiezo que termina en abandono pesa más que uno que termina en duda, incluso si le "
              "pasó a una sola persona. No lo suavicen en el avance: es lo que el curso más necesita "
              "oír para poder ayudarles."},
        {"p": "¿Podemos defendernos si la retroalimentación nos parece injusta?",
         "r": "En los tres minutos, no: se **anota y no se responde**, y solo se pregunta para "
              "entender —«¿en qué momento se perdió?»—. No es una regla de sumisión, es de "
              "eficiencia: defenderse consume el único tiempo de revisión externa gratis que van a "
              "tener. Después, en el documento del equipo, escriben qué van a aplicar y qué no, con "
              "su razón. **Descartar retroalimentación con argumento es perfectamente válido**; "
              "descartarla en el momento y sin pensarla, no."},
        {"p": "¿Los ajustes de hoy tienen que estar listos para la sesión 15?",
         "r": "Para la **sesión 14**, no para la 15. La sesión 14 es la preparación de la "
              "presentación final y el ensayo general: si el prototipo no está ajustado, van a "
              "ensayar con la versión vieja y el ensayo no sirve. La 15 es la exposición con nota, y "
              "ahí ya no hay margen."},
    ],

    "notas_operativas": [
        "**Reparto distinto hoy y hay que anunciarlo en el minuto 2:** teoría 20 · taller 12 · "
        "**exposiciones y retroalimentación 40** · cierre 10.",
        "**Prepare el muro de Padlet con una columna por equipo** antes de la sesión, y ponga el "
        "enlace en el chat antes de que salgan de las salas de grupo.",
        "Diga la regla en la apertura: **quien no hizo la prueba no tiene avance que presentar.** Es "
        "la primera sesión del corte 3 y las reglas se fijan hoy.",
        "Deje la diapositiva de **cómo se da retroalimentación** proyectada durante las 40 minutos de "
        "exposiciones. Sin el formato a la vista, se vuelve «me gustó mucho».",
        "En los tres minutos de cada equipo, dé la palabra a **dos equipos distintos** y aporte usted "
        "**un solo comentario al final** — el que nadie dijo.",
        "Cronómetro en pantalla y corte estricto: cinco equipos por ocho minutos no perdona. Si un "
        "equipo se pasa, el que pierde tiempo es el último.",
        "Si alguien empieza a **rediseñar el proyecto ajeno**, córtelo con respeto y explique por qué: "
        "el otro equipo tomó decisiones documentadas que quien comenta no vio.",
        "Recuerde a quien recibe: **anotar, no responder.** Una vez basta si se dice antes de la "
        "primera exposición.",
        "Los ajustes se necesitan para la **sesión 14** —el ensayo general—, no para la 15.",
    ],

    "ti_siguiente": {
        "tid": "Retroalimentación y ajustes — aplicar al prototipo los ajustes comprometidos en el "
               "muro, y dejar en el documento del equipo la ficha de avance completa con la lista de "
               "lo que no se arregla.",
        "ti": "Revisión entre pares: leer el documento de **otro equipo** (el docente asigna la "
              "pareja) y dejarle **dos observaciones escritas** con el formato de hoy — observación "
              "y expectativa, una sola cosa importante cada una.",
        "adelanto": "vemos el **impacto social y ambiental** del proyecto: a quién más afecta esto "
                    "aunque no lo use, y cómo se mide.",
        "aviso": "Traigan a la sesión 13 el **listado de actores no usuarios de la sesión 3** y el "
                 "**indicador ambiental de la sesión 5**: los dos se usan directamente en el taller. "
                 "Si los perdieron, recupérenlos del documento del equipo antes de la sesión.",
    },

    "cierre_titulo": "Nos vemos en la sesión 13",
    "cierre_frase": "La persona que prueba nunca se equivoca: si se perdió, el diseño la perdió",
}


# =============================================================================
# CLASE 13 · Evaluacion de impacto social y ambiental
# =============================================================================
# Unica sesion del corte 3 con el reparto estandar de bloques (10/45/17/15/3).

TEMAS[13] = {
    "n": 13,
    "titulo": "Evaluación de impacto social y ambiental",
    "subtitulo": "A quién más le pasa algo por culpa de su solución, aunque nunca la use",
    "hook": "Si su solución funciona perfectamente y la usa todo el mundo, "
            "¿quién queda peor que antes?",
    "hook_lines": [
        "Siempre hay alguien. Y casi nunca es un usuario.",
        "Un ingeniero que no puede responder esa pregunta no terminó el diseño.",
    ],
    "objetivos": [
        "Distinguir **impacto** de intención, y **directo** de indirecto.",
        "Identificar a los afectados que **no son usuarios**, con el listado de la sesión 3.",
        "Llenar una **matriz de impacto** con indicadores medibles, no con adjetivos.",
        "Declarar los impactos **negativos** y proponer **medidas de mitigación**.",
    ],
    "agenda": {
        "Apertura": "Pregunta de entrada en el muro: ¿quién queda peor?",
        "Teoría y guía del docente": "Impacto, afectados, la matriz y cómo se califica",
        "Actividad en equipos": "Matriz de impacto del proyecto, en salas de grupo",
        "Exposiciones": "5 equipos × 3 min — el impacto negativo y su mitigación",
        "Cierre": "Lo que queda amarrado para la sesión 14",
    },
    "herramienta_nota": "La matriz se llena en una tabla del **documento del equipo** en Google "
                        "Drive; si quieren dibujar el mapa de afectados, **draw.io** con la "
                        "plantilla de red. **Hoy no se usa asistente de IA**: la lista de afectados "
                        "de un proyecto local es justo lo que un modelo entrenado con internet no "
                        "puede conocer.",
    "avance_proyecto": "Matriz de impacto social y ambiental con indicadores, impactos negativos "
                       "declarados y medidas de mitigación",

    "teoria": [
        {
            "tipo": "cards",
            "titulo": "Impacto: cuatro distinciones que hay que tener claras",
            "cards": [
                ("Impacto NO es intención",
                 "«Queremos ayudar a la comunidad» es una intención. El impacto es **lo que de hecho "
                 "cambia** en la vida de alguien, medible, ocurra o no lo que queríamos."),
                ("Directo e indirecto",
                 "Directo: la persona hace menos viajes en vano. Indirecto: la voluntaria dedica diez "
                 "minutos más al cierre. **El indirecto es el que se olvida, y el que trae los "
                 "problemas.**"),
                ("Positivo y negativo",
                 "Toda solución tiene efectos de los dos signos. Un informe con solo impactos "
                 "positivos no es un informe optimista: **es un informe incompleto**."),
                ("Corto y largo plazo",
                 "Hay efectos que solo aparecen cuando la solución se usa mucho y por mucho tiempo. "
                 "Nombrarlos, aunque no se puedan medir hoy, ya es hacer ingeniería."),
            ],
            "columns": 2,
        },
        {
            "tipo": "steps",
            "titulo": "Cómo se encuentra a los afectados que no son usuarios",
            "steps": [
                ("1 · Empiece por su propia lista", "En la **sesión 3** hicieron un listado de actores no usuarios. Ábranlo: la mitad del trabajo de hoy ya está hecho y casi todos lo olvidaron."),
                ("2 · Siga la cadena de trabajo", "¿A quién le llega **más trabajo** por su solución? ¿A quién le llega menos? Ese es el impacto indirecto más frecuente y el que genera resistencia real."),
                ("3 · Pregunte quién NO puede usarla", "Quien no tiene celular, datos, lectura fluida, buena vista o el idioma. **Si su solución solo mejora a quien ya estaba mejor, empeoró la brecha.**"),
                ("4 · Mire qué consume", "Energía, datos móviles, papel, hardware que se vuelve basura. El software también tiene huella, y en la sesión 5 ya midieron un pedazo de la suya."),
                ("5 · Pregunte a quién desplaza", "Si su solución reemplaza algo, alguien hacía ese algo. Ni siempre es malo ni siempre es evitable, pero **omitirlo sí es un error del análisis**."),
            ],
            "sub": "Los usuarios son la parte fácil: por definición eligieron usarla. Los afectados no eligieron nada",
        },
        {
            "tipo": "tabla",
            "titulo": "La matriz de impacto: qué se pregunta en cada dimensión",
            "headers": ["Dimensión", "La pregunta", "Cómo se mide"],
            "rows": [
                ["**Social · acceso**",
                 "¿Quién puede usarla y quién no?",
                 "% o número de personas del grupo objetivo que quedan fuera, y por qué motivo."],
                ["**Social · equidad**",
                 "¿Mejora más a quien ya estaba mejor?",
                 "Comparación entre dos grupos: quien tiene el recurso y quien no lo tiene."],
                ["**Social · carga de trabajo**",
                 "¿A quién le llega más trabajo?",
                 "Minutos por día o por semana, para cada rol afectado."],
                ["**Ambiental · consumo**",
                 "¿Cuántos datos, energía o papel mueve?",
                 "KB por consulta × consultas estimadas; hojas al mes; horas de equipo encendido."],
                ["**Ambiental · residuos**",
                 "¿Exige comprar o botar algo?",
                 "Equipos, cartuchos, impresiones. Si no exige nada, **dígalo**: es un resultado."],
                ["**Económico**",
                 "¿Quién paga y quién ahorra?",
                 "Costo mensual de operación, y ahorro estimado para el usuario o la organización."],
            ],
            "note": "No todas las dimensiones aplican a todos los proyectos. Una fila que no aplica "
                    "se escribe «no aplica» **con una línea de razón** — dejarla en blanco parece un "
                    "olvido y se califica como tal.",
            "col_w": [2.3, 3.1, 4.4],
        },
        {
            "tipo": "tabla",
            "titulo": "Cómo se califica un impacto, sin fingir precisión",
            "headers": ["Criterio", "Qué pregunta", "Escala que usamos"],
            "rows": [
                ["**Carácter**", "¿Mejora o empeora la situación?", "Positivo · Negativo"],
                ["**Magnitud**", "¿Qué tan grande es el cambio para quien lo recibe?", "Baja · Media · Alta"],
                ["**Extensión**", "¿A cuánta gente le pasa?", "Pocas personas · Un grupo · Todo el barrio"],
                ["**Duración**", "¿Cuánto dura el efecto?", "Temporal · Permanente mientras se use"],
                ["**Reversibilidad**", "¿Se puede deshacer si sale mal?", "Reversible · Difícil de revertir"],
            ],
            "note": "Los cinco criterios vienen de las metodologías de evaluación de impacto "
                    "ambiental, que trabajan con matrices de este tipo desde los años setenta. "
                    "Aviso de honestidad intelectual: **las escalas son una convención para "
                    "comparar y ordenar, no una medición.** Dos equipos pueden calificar distinto el "
                    "mismo impacto; lo que no se puede es no justificar la calificación.",
            "col_w": [2.0, 3.9, 3.9],
            "fs_body": 11,
        },
        {
            "tipo": "before_after",
            "titulo": "Un impacto declarado y un impacto medido",
            "before_title": "Lo que escribe casi todo el mundo",
            "before": [
                "«Nuestra solución beneficia a la comunidad.»",
                "«Contribuye al cuidado del medio ambiente.»",
                "«Mejora la calidad de vida de los usuarios.»",
                "«Promueve la inclusión y el acceso a la cultura.»",
                "«No genera ningún impacto negativo.»",
            ],
            "after_title": "Lo que se puede verificar",
            "after": [
                "«Evita **4 de cada 10 viajes** sin préstamo: unas 60 visitas al mes.»",
                "«Cada consulta mueve **menos de 200 KB**, sin imágenes.»",
                "«Ahorra al usuario **un pasaje** y unos 25 minutos por visita evitada.»",
                "«Alcanza a quien tiene celular con datos: **queda fuera 1 de cada 5** vecinos.»",
                "«Añade **10 minutos diarios** de trabajo a la voluntaria del cierre.»",
            ],
            "sub": "Nótese que las dos últimas líneas de la derecha son impactos NEGATIVOS, y son las que hacen creíble a todas las demás",
            "size": 13,
        },
        {
            "tipo": "box",
            "titulo": "Tres honestidades sobre el impacto",
            "notas": [
                ("advertencia",
                 "**«No genera ningún impacto negativo» es la frase que más credibilidad quita en un "
                 "informe de ingeniería.** Toda solución tiene costos: alguien trabaja más, algo se "
                 "consume, alguien queda fuera. Un equipo que no encuentra ni uno no buscó — y quien "
                 "lea el informe lo va a notar antes que ustedes."),
                ("info",
                 "**No todo impacto es cuantificable, y eso no es excusa para no nombrarlo.** Si no "
                 "se puede medir, se describe con precisión y se dice cómo **se podría** medir. "
                 "«No sabemos cuántos vecinos no tienen datos móviles; se sabría con una encuesta de "
                 "diez casas» es una respuesta profesional. «No aplica» no lo es."),
                ("aclaracion",
                 "**El software también consume.** Datos móviles que alguien paga, energía del "
                 "servidor, hardware que se vuelve residuo. En la sesión 5 midieron un pedazo de eso "
                 "—el límite de 200 KB por consulta— y hoy ese número entra a la matriz como "
                 "indicador ambiental. **Un requisito no funcional bien elegido es, a la vez, una "
                 "medida de mitigación.**"),
            ],
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada: ¿quién queda peor?",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "El gancho de hoy está construido para incomodar, y hay que dejarlo incomodar unos "
                "segundos antes de explicarlo: **si su solución funciona perfectamente y la usa todo "
                "el mundo, ¿quién queda peor que antes?** La reacción típica es «nadie», y esa "
                "respuesta es el punto de partida de la sesión.",
                "Siempre hay alguien, y casi nunca es un usuario. En el caso de la biblioteca: la "
                "voluntaria del cierre, que ahora dedica diez minutos más a actualizar la lista; y "
                "el vecino sin datos móviles, que antes llegaba al mostrador en igualdad de "
                "condiciones y ahora llega detrás de tres personas que ya sabían qué pedir. Ninguno "
                "de los dos usa el sistema para consultar, y a los dos les cambió la vida por él.",
                "El encuadre que justifica la sesión completa, y que conviene decir sin solemnidad: "
                "**un ingeniero que no puede responder esa pregunta no terminó el diseño.** No es un "
                "asunto de ética añadida al final ni un requisito de acreditación: es parte del "
                "análisis técnico, igual que estimar el consumo o el costo. Los proyectos que fallan "
                "socialmente casi nunca fallan por el código; fallan porque nadie preguntó a quién "
                "más le pasaba algo.",
                "Operativamente, use la apertura para verificar el insumo: pida que cada equipo "
                "escriba en el muro **un afectado que no sea usuario**. Los equipos que traigan el "
                "listado de la sesión 3 lo van a hacer en treinta segundos; los que no, van a "
                "escribir «los usuarios». Ahí ya sabe con quién tiene que sentarse en las salas de "
                "grupo.",
            ],
        },
        {
            "titulo": "Impacto no es intención, y el indirecto es el que muerde",
            "slide": "{{slide:Impacto: cuatro distinciones}}",
            "cuerpo": [
                "**Impacto no es intención.** Es la distinción más importante del día y la que más "
                "cuesta. «Queremos ayudar a la comunidad» es una intención, y no informa nada: no se "
                "puede verificar, no se puede medir y nadie puede estar en contra. El impacto es lo "
                "que **de hecho** cambia en la vida de alguien, ocurra o no lo que queríamos. "
                "Conviene decirlo de frente: el mundo está lleno de proyectos con buenas intenciones "
                "y malos impactos, y el propósito de una matriz es precisamente separar las dos "
                "cosas.",
                "**Directo e indirecto.** El directo es fácil porque es el que buscábamos: la persona "
                "hace menos viajes en vano. El indirecto es el que se olvida y el que trae los "
                "problemas: la voluntaria del cierre dedica diez minutos más cada día. Un dato "
                "importante para su formación profesional: **la resistencia a una solución nueva casi "
                "siempre viene de un impacto indirecto que nadie consideró.** Cuando en una empresa "
                "un sistema «no lo quieren usar», nueve de diez veces es porque a alguien le llegó "
                "trabajo extra que nunca se contó.",
                "**Positivo y negativo.** Hay que anticipar y desactivar la creencia de que declarar "
                "un impacto negativo baja la nota. Es lo contrario, y hay que decirlo explícitamente "
                "porque van a dudar: **un informe con solo impactos positivos no es optimista, es "
                "incompleto**, y quien lo lea va a desconfiar de todo lo demás. En este curso "
                "declarar un negativo con su mitigación **sube** la nota.",
                "**Corto y largo plazo.** Algunos efectos solo aparecen con el uso sostenido: la "
                "lista que crece y se vuelve inmanejable, la dependencia de una sola voluntaria que "
                "sabe actualizarla. Nombrarlos sin poder medirlos ya es hacer ingeniería, y es "
                "material directo para la sección de trabajo futuro del informe final.",
            ],
        },
        {
            "titulo": "Los afectados que no eligieron nada",
            "slide": "{{slide:Cómo se encuentra a los afectados}}",
            "cuerpo": [
                "La frase que ordena este bloque: **los usuarios son la parte fácil, porque por "
                "definición eligieron usarla; los afectados no eligieron nada.** De ahí la "
                "obligación de buscarlos activamente.",
                "**Paso 1: empezar por la propia lista.** En la sesión 3 hicieron un listado de "
                "actores no usuarios. Casi todos lo olvidaron, y ahí está la mitad del trabajo de "
                "hoy. Vale la pena señalar la lección de método —es la tercera vez en el curso que "
                "un material viejo resuelve un problema nuevo—: **documentar es una inversión, no un "
                "trámite.**",
                "**Paso 2: seguir la cadena de trabajo.** ¿A quién le llega más trabajo y a quién "
                "menos? Es el impacto indirecto más frecuente. En el caso modelo, la voluntaria del "
                "cierre; en un proyecto de gestión, la persona que ahora tiene que llenar el "
                "formato.",
                "**Paso 3: preguntar quién NO puede usarla.** Este paso es el corazón ético de la "
                "sesión y hay que darle tiempo. Quien no tiene celular, datos, lectura fluida, buena "
                "vista, o el idioma. La regla, dicha en una frase que se les debería quedar: **si su "
                "solución solo mejora a quien ya estaba mejor, empeoró la brecha.** Y el matiz que "
                "hace la idea difícil y verdadera: el excluido puede quedar peor **en términos "
                "relativos** aunque nada haya cambiado para él, porque los demás mejoraron y la "
                "atención se reordenó. Ese caso es real, es incómodo y es exactamente lo que hay que "
                "aprender a ver.",
                "**Paso 4: mirar qué consume.** Energía, datos, papel, hardware que acaba en basura "
                "electrónica. En la sesión 5 ya midieron un pedazo de su huella; hoy ese número entra "
                "a la matriz.",
                "**Paso 5: preguntar a quién desplaza.** Si la solución reemplaza algo, alguien hacía "
                "ese algo. Aquí conviene ser equilibrado y no moralizar: no siempre es malo ni "
                "siempre es evitable —la ingeniería lleva dos siglos automatizando trabajo—, pero "
                "**omitirlo del análisis sí es un error técnico**.",
            ],
        },
        {
            "titulo": "La matriz, la calificación y los límites del método",
            "slide": "{{slide:La matriz de impacto}} {{slide:Cómo se califica un impacto}}",
            "cuerpo": [
                "La primera tabla es la plantilla del taller y conviene recorrerla dimensión por "
                "dimensión, deteniéndose en la columna de la derecha: **cómo se mide**. Ahí está el "
                "aprendizaje. «Acceso» no se mide con adjetivos sino con el número de personas del "
                "grupo objetivo que quedan fuera y por qué motivo. «Carga de trabajo» se mide en "
                "minutos por día. «Consumo» se mide en KB por consulta por número de consultas "
                "estimadas — y ese número ya lo tienen desde la sesión 5.",
                "Insista en la nota al pie: **una fila que no aplica se escribe «no aplica» con una "
                "línea de razón.** Dejarla en blanco parece un olvido, y en un informe real el lector "
                "no puede distinguir entre «no aplica» y «no lo pensamos».",
                "La segunda tabla es la calificación, y aquí hay que hacer un ejercicio de honestidad "
                "intelectual que vale más que la tabla misma. Los cinco criterios —carácter, "
                "magnitud, extensión, duración, reversibilidad— provienen de las metodologías de "
                "evaluación de impacto ambiental, que trabajan con matrices de este tipo desde los "
                "años setenta; la matriz de Leopold, de 1971, es el ejemplo clásico y sigue siendo "
                "el punto de partida de la mayoría de las variantes que se usan hoy. Si algún "
                "estudiante quiere profundizar, esa es la palabra que debe buscar, y ya saben de la "
                "sesión 9 cómo verificar una fuente.",
                "Y ahora el límite, que hay que decir en voz alta porque es formativo: **las escalas "
                "son una convención para comparar y ordenar, no una medición.** Poner «magnitud: "
                "alta» no convierte un juicio en un dato. Dos equipos honestos pueden calificar "
                "distinto el mismo impacto, y eso no invalida el método: la matriz sirve para "
                "**ordenar prioridades y forzar la conversación**, no para producir un número "
                "objetivo. Lo que sí es exigible es que **cada calificación tenga una línea de "
                "justificación**. Un estudiante que entiende esto no va a confundir nunca más una "
                "escala ordinal con una medición, y esa es una de las confusiones más comunes en "
                "informes técnicos.",
            ],
        },
        {
            "titulo": "Del adjetivo al indicador, y las tres honestidades",
            "slide": "{{slide:Un impacto declarado y un impacto medido}} {{slide:Tres honestidades}}",
            "cuerpo": [
                "La diapositiva de antes y después es la que más rinde en clase, porque la columna "
                "izquierda es literalmente lo que van a escribir si no se les enseña otra cosa: "
                "«beneficia a la comunidad», «contribuye al cuidado del medio ambiente», «mejora la "
                "calidad de vida». Leerlas en voz alta produce risa incómoda, y ese es el momento de "
                "hacer la pregunta: **¿qué proyecto NO podría escribir estas cinco frases?** "
                "Ninguno. Una afirmación que sirve para todo no informa de nada.",
                "La columna derecha muestra el mismo contenido convertido en indicador: 4 de cada 10 "
                "viajes evitados, menos de 200 KB por consulta, un pasaje y 25 minutos ahorrados por "
                "visita. Y el detalle que hay que señalar con el cursor: **las dos últimas líneas de "
                "la derecha son impactos negativos** —1 de cada 5 vecinos queda fuera, 10 minutos "
                "diarios extra para la voluntaria— **y son precisamente las que hacen creíbles a las "
                "otras tres**. Un lector experimentado confía en un informe que reconoce sus costos.",
                "De las tres honestidades, la primera es la que hay que repetir hasta que se instale: "
                "**«no genera ningún impacto negativo» es la frase que más credibilidad quita en un "
                "informe de ingeniería.** Toda solución tiene costos. Un equipo que no encuentra "
                "ninguno no buscó.",
                "La segunda desactiva la excusa más común: si no se puede medir, **se describe con "
                "precisión y se dice cómo se podría medir**. «No sabemos cuántos vecinos no tienen "
                "datos móviles; se sabría con una encuesta de diez casas» es una respuesta "
                "profesional, y de hecho es el tipo de frase que aparece en informes reales. Lo que "
                "no es profesional es un «no aplica» sin razón.",
                "La tercera cierra el arco del curso: **el software también consume.** Datos que "
                "alguien paga, energía, hardware que se vuelve residuo. Y aquí hay un hallazgo que "
                "vale la pena hacerles ver, porque conecta cuatro sesiones: el límite de 200 KB por "
                "consulta que definieron en la sesión 5 como indicador, se volvió requisito no "
                "funcional en la sesión 7, sirvió para descartar imágenes en las sesiones 10 y 11, y "
                "hoy entra a la matriz como **medida de mitigación ambiental**. Un requisito no "
                "funcional bien elegido es, a la vez, una mitigación — y eso no se puede improvisar "
                "en la sesión 13 si no se escribió en la 5.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:10 · Apertura · [Slide 4]",
            "cuerpo": [
                "Comparta pantalla antes de que entre el primero:",
                "> «Si su solución funciona perfectamente y la usa todo el mundo, ¿quién queda peor "
                "que antes?»",
                "Deje el silencio incómodo unos segundos. La respuesta típica es «nadie», y esa es la "
                "puerta de entrada.",
                "En el muro, cada equipo escribe **un afectado que no sea usuario**. Los que traigan "
                "el listado de la sesión 3 lo hacen en treinta segundos; los que no, escriben «los "
                "usuarios» — y ya sabe con quién sentarse después.",
                "**[Nota docente]:** la frase de encuadre, sin solemnidad: **un ingeniero que no "
                "puede responder esa pregunta no terminó el diseño.**",
            ],
        },
        {
            "titulo": "00:10–00:55 · Teoría (45 min) · [Slide 5]…[Slide 10]",
            "cuerpo": [
                "Reparto:",
                "- **7 min** · Las cuatro distinciones [Slide 5]. Deténgase en **impacto ≠ "
                "intención** y en que el **indirecto** es el que trae los problemas.",
                "- **9 min** · Cómo se encuentra a los afectados [Slide 6]. Dé tiempo al paso 3: "
                "**si su solución solo mejora a quien ya estaba mejor, empeoró la brecha.**",
                "- **10 min** · La matriz [Slide 7]. Recórrala por la **columna de la derecha**: ahí "
                "está el aprendizaje. Insista en que «no aplica» va con razón.",
                "- **8 min** · Cómo se califica [Slide 8]. Diga en voz alta el límite del método: "
                "**es una convención para ordenar, no una medición.**",
                "- **8 min** · Antes y después [Slide 9]. Lea la columna izquierda en voz alta y "
                "pregunte: **¿qué proyecto NO podría escribir esto?**",
                "- **3 min** · Las tres honestidades [Slide 10]. La primera, repetida: «no genera "
                "impacto negativo» es la frase que más credibilidad quita.",
            ],
        },
        {
            "titulo": "00:55–01:12 · Taller en salas de grupo (17 min) · [Slide 11]",
            "cuerpo": [
                "Ritmo sugerido dentro de la sala:",
                "- 4 min · abrir el listado de actores de la **sesión 3** y completarlo con los pasos "
                "2 a 5.",
                "- 5 min · tres impactos positivos, **cada uno con su indicador**.",
                "- 4 min · dos impactos negativos o riesgos, con quién los recibe.",
                "- 4 min · calificar la matriz y escribir **una mitigación por cada negativo**.",
                "**[Nota docente]:** entre a las cinco salas con una sola pregunta: **«¿quién queda "
                "peor?»**. Si responden «nadie», use el paso 3 —quién no puede usarla— y aparece en "
                "un minuto.",
                "**[Nota docente]:** el error de calibración más común es escribir adjetivos donde va "
                "un número. Pida el indicador en voz alta: «beneficia a la comunidad» → **¿cuántas "
                "personas, cuántas veces al mes?**",
            ],
        },
        {
            "titulo": "01:12–01:27 · Exposiciones · [Slide 12]",
            "cuerpo": [
                "5 equipos × 3 min. **El minuto obligatorio es el impacto NEGATIVO y su mitigación**, "
                "no la lista de bondades.",
                "**[Nota docente]:** si un equipo dice que no tiene ningún impacto negativo, no lo "
                "deje pasar y no lo humille: pregúntele **quién trabaja más** por su solución. La "
                "respuesta aparece siempre, y el curso entero aprende de ese intercambio.",
                "**[Nota docente]:** premie en voz alta al equipo que declare el negativo más "
                "incómodo. Es la conducta que quiere ver en el informe final.",
            ],
        },
        {
            "titulo": "01:27–01:30 · Cierre · [Slide 13][Slide 14]",
            "cuerpo": [
                "Una idea: **los usuarios eligieron usarla; los afectados no eligieron nada.**",
                "Recuerde la conexión que cierra cuatro sesiones: el límite de 200 KB de la sesión 5 "
                "es hoy una **medida de mitigación ambiental**. Documentar fue una inversión.",
                "Anuncie la sesión 14: **la preparación de la presentación final** y el **ensayo "
                "general cronometrado**. Y avise que la exposición de la sesión 15 vale el **15 %**.",
            ],
        },
    ],

    "taller": {
        "archivo": "Matriz de impacto social y ambiental",
        "titulo": "Matriz de impacto social y ambiental",
        "min": 17,
        "exposicion": 3,
        "consigna": "Completen la matriz de impacto de su proyecto: **quiénes son los afectados que "
                    "no son usuarios**, tres impactos positivos **con su indicador**, dos impactos "
                    "negativos o riesgos, la matriz calificada con su justificación, y **una medida "
                    "de mitigación por cada negativo**.",
        "entregable": "la matriz de impacto completa en el documento del equipo, con indicadores "
                      "medibles y las medidas de mitigación — es una sección del informe final",
        "entregable_corto": "matriz de impacto con indicadores, negativos declarados y mitigaciones",
        "reparto_titulo": "Ritmo sugerido dentro de la sala (17 min):",
        "reparto": "4 min abrir el listado de actores de la **sesión 3** y completarlo · 5 min tres "
                   "impactos positivos con indicador · 4 min dos negativos con quién los recibe · 4 "
                   "min calificar y escribir las mitigaciones. **Empiecen por el listado de la sesión "
                   "3**: si arrancan de cero pierden la mitad del tiempo.",
        "reparto_corto": "17 min: afectados, positivos con indicador, negativos, matriz y mitigación",
        "bloques": [
            {"clave": "LOS AFECTADOS QUE NO SON USUARIOS",
             "pide": "La lista de quienes reciben un efecto sin usar la solución: a quién le llega "
                     "más trabajo, quién **no puede** usarla, y a quién desplaza.",
             "check": "hay al menos tres y ninguno es un usuario. «La comunidad» no es un afectado: es una palabra que evita nombrarlos."},
            {"clave": "TRES IMPACTOS POSITIVOS CON SU INDICADOR",
             "pide": "Tres efectos buenos, cada uno con **un número y una unidad**: cuántas personas, "
                     "cuántas veces, cuántos minutos, cuántos pesos.",
             "check": "cada impacto tiene un indicador verificable. «Mejora la calidad de vida» no cuenta; «ahorra un pasaje por visita evitada» sí."},
            {"clave": "DOS IMPACTOS NEGATIVOS O RIESGOS",
             "pide": "Dos efectos malos, con **quién los recibe** exactamente. Si no encuentran "
                     "ninguno, pregúntense quién trabaja más por su solución.",
             "check": "los dos existen y tienen un afectado concreto. «No genera impactos negativos» se califica como bloque no hecho."},
            {"clave": "LA MATRIZ CALIFICADA",
             "pide": "Cada impacto con su carácter, magnitud, extensión, duración y reversibilidad — y "
                     "**una línea de justificación** por calificación.",
             "check": "las calificaciones están justificadas. Una matriz de «altas» sin razón no vale más que una sin calificar."},
            {"clave": "LAS MEDIDAS DE MITIGACIÓN",
             "pide": "Qué van a hacer para reducir cada impacto negativo. Puede ser **una medida no "
                     "digital**, y muchas veces es la mejor.",
             "check": "hay una mitigación por cada negativo y es realizable con los recursos del proyecto."},
        ],
        "expo": [
            ("30 s · Los afectados que no son usuarios", "Nómbrelos. Sin «la comunidad»."),
            ("40 s · Un impacto positivo con su número", "El más fuerte, con indicador."),
            ("70 s · El impacto negativo y su mitigación", "**El minuto obligatorio.** El más incómodo que hayan encontrado."),
            ("30 s · La calificación", "Cuál es el impacto más grave y por qué lo calificaron así."),
            ("10 s · Cierre", "Qué dimensión no aplica en su proyecto, y por qué."),
        ],
    },

    "rubrica": [
        ("La lista de afectados incluye al menos tres que no son usuarios, nombrados", 15,
         "Los afectados no eligieron nada: encontrarlos es el trabajo técnico de la sesión."),
        ("Los tres impactos positivos tienen indicador con número y unidad", 25,
         "Un impacto sin indicador es una intención, y una intención no se puede verificar."),
        ("Hay dos impactos negativos declarados, con su afectado concreto", 20,
         "Declarar los costos es lo que hace creíble el resto del informe."),
        ("La matriz está calificada y cada calificación tiene una línea de justificación", 20,
         "La escala es una convención para ordenar: sin justificación no ordena nada."),
        ("Cada impacto negativo tiene una medida de mitigación realizable", 20,
         "Detectar un daño y no proponer nada es un diagnóstico, no ingeniería."),
    ],

    "solucion": {
        "para_que": "Este documento trae la matriz completa del caso de la biblioteca. Su valor está "
                    "en dos partes concretas: **el impacto negativo de exclusión**, que es el que "
                    "ningún equipo encuentra solo, y **la mitigación no digital** —una cartelera "
                    "impresa— que suele sorprender al curso porque contradice la intuición de que "
                    "todo se arregla con más tecnología. Si solo alcanza a leer un bloque, que sea "
                    "**DOS IMPACTOS NEGATIVOS**.",
        "caso_titulo": "La biblioteca del barrio · impacto social y ambiental de la consulta de disponibilidad",
        "caso": "Solución del semestre: una lista en línea de los libros que se prestan seguido, "
                "consultable desde el celular sin cuenta, actualizada por la voluntaria al cierre de "
                "cada día. Datos disponibles: unas 150 visitas mensuales a la biblioteca, de las "
                "cuales **4 de cada 10 terminan sin préstamo** porque el libro no estaba; el trayecto "
                "típico es de 25 minutos y un pasaje; el barrio tiene un porcentaje alto pero no "
                "universal de celulares con datos; la biblioteca la sostienen tres voluntarias que "
                "rotan.",
        "por_que_este_caso": "Porque el impacto positivo es evidente y fácil de medir, y eso hace más "
                             "visible el trabajo real de la sesión: encontrar los dos negativos. Uno "
                             "es de carga de trabajo y el equipo lo encuentra con ayuda; el otro es "
                             "de **exclusión relativa** —el vecino sin datos queda peor sin que nada "
                             "cambie para él— y casi nunca lo encuentran solos. Es el hallazgo que "
                             "justifica la sesión completa.",
        "bloques": [
            {
                "clave": "LOS AFECTADOS QUE NO SON USUARIOS",
                "respuesta": "Del listado de la sesión 3, completado con los pasos 2 a 5:\n\n"
                             "| Afectado | Cómo lo afecta | Paso que lo encontró |\n"
                             "|---|---|---|\n"
                             "| **La voluntaria del cierre** | Le llega trabajo nuevo: actualizar la "
                             "lista todos los días antes de cerrar. | 2 · cadena de trabajo |\n"
                             "| **El vecino sin celular o sin datos** | No puede consultar. Y en el "
                             "mostrador ahora llega detrás de quien ya sabía qué pedir. | 3 · quién no "
                             "puede usarla |\n"
                             "| **La persona con dificultad de lectura o de visión** | La lista es "
                             "texto en una pantalla pequeña. Antes preguntaba de viva voz. | 3 · quién "
                             "no puede usarla |\n"
                             "| **La coordinadora de la biblioteca** | Depende de que la lista esté "
                             "al día: si no lo está, la reclamación le llega a ella. | 2 · cadena de "
                             "trabajo |\n"
                             "| **Quien atendía las llamadas de consulta** | Menos llamadas por "
                             "atender: es un desplazamiento pequeño de trabajo, y en este caso "
                             "positivo para ella. | 5 · a quién desplaza |\n\n"
                             "**Nótese que ninguno de los cinco es un usuario de la solución**, y que "
                             "dos de ellos —el vecino sin datos y la persona con dificultad de "
                             "lectura— **no pueden usarla en absoluto**. Ese es exactamente el grupo "
                             "que un análisis centrado en el usuario no ve nunca.\n\n"
                             "**Lo que NO es un afectado:** «la comunidad», «los ciudadanos», «la "
                             "sociedad». Son palabras que evitan el trabajo de nombrar. Si un equipo "
                             "las usa, la pregunta que las rompe es: **¿quién, exactamente, y qué le "
                             "pasa?**",
                "como_calificar": "15 pts, 5 por afectado bien identificado hasta tres. La "
                                  "verificación: **¿es alguien que no usa la solución?** Si el equipo "
                                  "listó usuarios, vale 5 en total y hay que reencuadrar con el paso "
                                  "3 —quién no puede usarla—, que produce resultados en un minuto. "
                                  "«La comunidad» vale 0 y hay que decir por qué: es una palabra que "
                                  "evita nombrar. Valore el equipo que trajo el listado de la sesión "
                                  "3: es la conducta que el curso quiere premiar."
            },
            {
                "clave": "TRES IMPACTOS POSITIVOS CON SU INDICADOR",
                "respuesta": "**1 · Se evitan viajes sin préstamo.** *Indicador:* de 150 visitas "
                             "mensuales, 4 de cada 10 terminan sin préstamo — unas **60 visitas "
                             "fallidas al mes**. Si la consulta previa evita la mitad, son **30 "
                             "viajes evitados por mes**. *De dónde sale el número:* el conteo de la "
                             "ficha del problema de la sesión 6.\n\n"
                             "**2 · Ahorro directo para el usuario.** *Indicador:* **un pasaje y unos "
                             "25 minutos** por visita evitada. Con 30 visitas evitadas al mes, son "
                             "unas **12 horas y 30 pasajes** que el barrio no gasta.\n\n"
                             "**3 · Menos desplazamientos, menos emisiones.** *Indicador:* **30 "
                             "trayectos de ida y vuelta menos al mes**, la mayoría en transporte "
                             "público o a pie. No calculamos toneladas de CO₂ porque no tenemos con "
                             "qué hacerlo bien; el indicador honesto es el número de trayectos "
                             "evitados.\n\n"
                             "**Sobre el tercero, que es el más instructivo:** la tentación es "
                             "escribir «reduce la huella de carbono en X toneladas», con un número "
                             "sacado de una calculadora en línea sin entenderlo. Es preferible "
                             "—y más profesional— **contar trayectos evitados y decir explícitamente "
                             "que no se convierte a emisiones por falta de datos confiables**. Un "
                             "número honesto y modesto vale más que uno grande e indefendible, y esa "
                             "es la misma lección de la sesión 9 sobre las fuentes.\n\n"
                             "**Y un cuarto que NO incluimos, a propósito:** «promueve el acceso a la "
                             "cultura». Es cierto, es bonito y no se puede medir con nada que "
                             "tengamos. Se puede mencionar en el informe como efecto esperado de "
                             "largo plazo, pero **no entra a la matriz como impacto medido**.",
                "como_calificar": "25 pts. La verificación es mecánica: **¿cada impacto tiene un "
                                  "número y una unidad?** Sí, 8 pts cada uno; sin indicador, 2. "
                                  "Acepte estimaciones razonadas —«si evita la mitad»— siempre que "
                                  "digan de dónde sale el supuesto: estimar con el supuesto a la "
                                  "vista es exactamente lo que se hace en ingeniería. Valore "
                                  "especialmente al equipo que **se niega a convertir a toneladas de "
                                  "CO₂ por falta de datos** y cuenta trayectos en su lugar: es "
                                  "criterio, no pereza, y conviene decirlo en voz alta al curso."
            },
            {
                "clave": "DOS IMPACTOS NEGATIVOS O RIESGOS",
                "respuesta": "**Negativo 1 · La voluntaria del cierre trabaja más.**\n\n"
                             "*Quién lo recibe:* la voluntaria de turno, tres personas que rotan. "
                             "*Indicador:* actualizar la lista toma unos **20 segundos por movimiento**; "
                             "con 10 a 15 movimientos diarios son **5 a 8 minutos al día**, más el "
                             "tiempo de abrir y cerrar: en la práctica, **unos 10 minutos diarios** al "
                             "final de una jornada de voluntariado no remunerada. *Riesgo asociado:* si "
                             "un día no se actualiza, el sistema **miente** — y una lista "
                             "desactualizada es peor que no tener lista, porque la gente ya confía en "
                             "ella.\n\n"
                             "**Negativo 2 · Exclusión relativa de quien no tiene celular con datos.**\n\n"
                             "*Quién lo recibe:* el vecino sin celular, sin datos, o con dificultad "
                             "para leer en pantalla. *Indicador:* no lo sabemos con precisión. "
                             "**Estimamos que 1 de cada 5 vecinos del grupo objetivo queda fuera, y "
                             "decimos explícitamente que es una estimación**; se sabría con una "
                             "encuesta de diez casas, que cabe en el trabajo siguiente.\n\n"
                             "*Y aquí está el hallazgo más difícil de la sesión, que hay que explicar "
                             "despacio:* para esa persona **no cambió nada** —sigue llegando al "
                             "mostrador y preguntando—, y sin embargo **queda peor que antes en "
                             "términos relativos**. Antes todos llegaban en igualdad de condiciones. "
                             "Ahora tres personas llegan sabiendo exactamente qué pedir, la atención "
                             "se vuelve más rápida para ellas, y quien pregunta de viva voz espera "
                             "más y ocupa más tiempo del mostrador. **La solución no le quitó nada: "
                             "les dio a los demás, y con eso reordenó la fila.** Ese es el impacto "
                             "que ningún equipo encuentra solo y el que justifica la sesión completa. "
                             "Es la forma concreta de la regla: *si su solución solo mejora a quien ya "
                             "estaba mejor, empeoró la brecha.*\n\n"
                             "**Un tercer riesgo, de largo plazo, que vale mencionar:** la biblioteca "
                             "queda **dependiendo de que alguien sepa y quiera actualizar la lista**. "
                             "Si la voluntaria que aprendió se va, el sistema se degrada en silencio "
                             "—nadie recibe un error, simplemente los datos envejecen—. Es un riesgo "
                             "de sostenibilidad y va en el informe final.",
                "como_calificar": "20 pts, 10 por negativo con afectado concreto e indicador o "
                                  "estimación declarada como tal. **Caso crítico:** si el equipo "
                                  "escribió «no genera impactos negativos», el bloque vale 0 — y la "
                                  "conversación es más importante que la nota. Pregunte «¿quién "
                                  "trabaja más por su solución?» y aparece el primero de inmediato; "
                                  "después pregunte «¿quién no puede usarla?» y aparece el segundo. "
                                  "Hágalo delante del curso: es el intercambio del que más se "
                                  "aprende hoy. Valore con puntos extra al equipo que encuentre solo "
                                  "una **exclusión relativa**, y dígale en voz alta por qué: es "
                                  "pensamiento de ingeniero, no buena voluntad."
            },
            {
                "clave": "LA MATRIZ CALIFICADA",
                "respuesta": "| Impacto | Carácter | Magnitud | Extensión | Duración | Reversibilidad |\n"
                             "|---|---|---|---|---|---|\n"
                             "| Viajes evitados | Positivo | **Alta** | Un grupo (~30/mes) | Permanente mientras se use | Reversible |\n"
                             "| Ahorro de pasaje y tiempo | Positivo | Media | Un grupo | Permanente mientras se use | Reversible |\n"
                             "| Menos trayectos | Positivo | **Baja** | Un grupo | Permanente mientras se use | Reversible |\n"
                             "| Carga extra a la voluntaria | Negativo | Media | Pocas personas (3) | Permanente mientras se use | Reversible |\n"
                             "| Exclusión relativa | Negativo | **Media** | Un grupo (~1 de 5) | Permanente mientras se use | **Difícil de revertir** |\n\n"
                             "**Las justificaciones, que son lo que se califica:**\n\n"
                             "- *Viajes evitados · magnitud alta:* elimina el problema completo para "
                             "quien consulta, que es el motivo del proyecto.\n"
                             "- *Menos trayectos · magnitud baja:* son 30 trayectos al mes en un "
                             "barrio; el efecto ambiental real es pequeño y **decirlo así es más "
                             "honesto que inflarlo**. Un equipo que califica de «alta» la magnitud "
                             "ambiental de 30 trayectos está haciendo publicidad, no evaluación.\n"
                             "- *Carga extra · magnitud media, pocas personas:* son 10 minutos "
                             "diarios, pero le caen a tres personas que trabajan gratis. **Poca "
                             "extensión no significa poca importancia**, y aquí se ve por qué los "
                             "cinco criterios se leen juntos y no se promedian.\n"
                             "- *Exclusión relativa · difícil de revertir:* es la calificación más "
                             "discutible y la más interesante. Una vez que la mayoría consulta "
                             "primero, la dinámica del mostrador cambia y no vuelve sola al estado "
                             "anterior, aunque se apague el sistema.\n\n"
                             "**Recuerde el límite del método al calificar en clase:** dos equipos "
                             "honestos pueden poner «media» y «alta» al mismo impacto. Eso no "
                             "invalida nada — **la matriz sirve para ordenar prioridades y forzar la "
                             "conversación, no para producir un número objetivo.** Lo que no se puede "
                             "es calificar sin justificar.",
                "como_calificar": "20 pts: 8 por la matriz completa y **12 por las justificaciones**. "
                                  "El criterio es explícito: una matriz llena de «altas» sin razón no "
                                  "vale más que una sin calificar, porque no ordena nada. Valore dos "
                                  "conductas y nómbrelas: calificar un impacto propio como **de "
                                  "magnitud baja** cuando lo es —señal de que están evaluando y no "
                                  "vendiendo—, y notar que **poca extensión no implica poca "
                                  "importancia**. No penalice una calificación distinta a la de este "
                                  "documento si está bien justificada: no hay respuesta única."
            },
            {
                "clave": "LAS MEDIDAS DE MITIGACIÓN",
                "respuesta": "**Mitigación del negativo 1 · la carga de la voluntaria:**\n\n"
                             "- La pantalla de actualización se diseñó para **20 segundos por "
                             "movimiento con un solo toque**, que fue el criterio de aceptación de la "
                             "sesión 7 y la razón por la que en la sesión 11 se eligió la variante "
                             "de lista con botón en vez de la de búsqueda. **La mitigación estaba "
                             "hecha antes de saber que era una mitigación.**\n"
                             "- **La fecha de última actualización visible al usuario** (sesión 10) "
                             "mitiga el riesgo asociado: si un día no se actualizó, el sistema no "
                             "miente, lo dice. Quita presión a la voluntaria y honestidad al dato.\n"
                             "- Medida nueva: **una hoja de instrucciones de media página pegada en "
                             "el mostrador**, para que la voluntaria que llega no dependa de que "
                             "alguien le explique.\n\n"
                             "**Mitigación del negativo 2 · la exclusión relativa:**\n\n"
                             "- **Una cartelera impresa en la puerta, actualizada una vez por "
                             "semana**, con los treinta títulos más pedidos y su estado. Cuesta una "
                             "hoja a la semana, no requiere celular, no requiere datos, y **la lee "
                             "cualquiera que llegue caminando**.\n"
                             "- **Que el mostrador atienda por orden de llegada y no por rapidez de "
                             "la consulta.** Es una medida organizacional, no técnica: no la "
                             "implementa el equipo, se recomienda a la coordinadora.\n\n"
                             "**Y aquí está la lección de la sesión, que conviene decir completa:** "
                             "**la mejor mitigación del proyecto no es digital.** Una hoja impresa en "
                             "la puerta atiende exactamente al grupo que la solución digital deja "
                             "fuera, y cuesta prácticamente nada. Un equipo que solo sabe pensar en "
                             "software nunca la propone — va a proponer una versión por mensajes de "
                             "texto, o una aplicación más liviana, o un teléfono de consulta, todo "
                             "más caro y menos efectivo. Vale la pena decirlo tal cual: **la "
                             "ingeniería no consiste en poner tecnología, sino en resolver el "
                             "problema con los recursos que hay.** Y nótese que la cartelera "
                             "reintroduce un consumo de papel: una hoja por semana. Eso también se "
                             "declara, porque toda mitigación tiene su propio costo.",
                "como_calificar": "20 pts, 10 por mitigación. Dos requisitos: que **corresponda al "
                                  "negativo** que dice mitigar, y que sea **realizable con los "
                                  "recursos del proyecto** —presupuesto cero, tres voluntarias—. Una "
                                  "mitigación que exige contratar a alguien o comprar equipos vale 3. "
                                  "Valore alto, y explique por qué al curso, la **mitigación no "
                                  "digital**: es la señal más clara de que el equipo entendió que la "
                                  "ingeniería resuelve problemas y no instala tecnología. Y reconozca "
                                  "al equipo que **declara el costo de su propia mitigación** (la "
                                  "hoja semanal de papel): ese nivel de honestidad es lo que se "
                                  "espera en un informe profesional."
            },
        ],
        "variantes": [
            {"caso": "Equipos que insisten en que no hay ningún impacto negativo",
             "clave": "Es el caso más frecuente y se resuelve con dos preguntas en este orden: "
                      "**«¿quién trabaja más por su solución?»** —aparece el negativo de carga— y "
                      "**«¿quién no puede usarla?»** —aparece el de exclusión—. No lo trate como "
                      "falta de honestidad: es falta de entrenamiento, porque nadie les había pedido "
                      "antes buscar el costo de su propia idea. Hágalo delante del curso: es el "
                      "intercambio del que más se aprende hoy."},
            {"caso": "Equipos que quieren calcular toneladas de CO₂",
             "clave": "Aparece siempre y hay que encauzarlo sin apagar el entusiasmo. Pregunte de "
                      "dónde sacaron el factor de conversión y si pueden explicar qué supone. Casi "
                      "nunca pueden, y ahí está la lección de la sesión 9 aplicada: **un número que "
                      "no se puede defender es peor que no tener número**. La salida profesional es "
                      "contar **trayectos evitados** y declarar que no se convierte a emisiones por "
                      "falta de datos confiables."},
            {"caso": "Equipos cuyo proyecto no tiene impacto ambiental evidente",
             "clave": "Pasa con proyectos de gestión o de procesos, y la respuesta correcta no es "
                      "inventar uno. Se buscan los consumos reales —**hojas impresas al mes**, horas "
                      "de equipo encendido, datos móviles— y si de verdad son marginales **se "
                      "escribe «marginal» con la razón y el número**. Un «no aplica» con una línea "
                      "de justificación es una respuesta válida y bien calificada; un «no aplica» "
                      "solo, no."},
            {"caso": "Equipos que confunden impacto con función del sistema",
             "clave": "Escriben «permite consultar la disponibilidad» como impacto. No lo es: es una "
                      "función. El impacto es **lo que le cambia a alguien** por poder consultar: "
                      "menos viajes, menos gasto, menos tiempo. La pregunta que lo corrige en el "
                      "acto es **«¿y eso qué le cambia a quién?»**, repetida hasta llegar a una "
                      "persona y un número."},
        ],
        "cierre": "Tres minutos. La idea, dicha completa: **los usuarios eligieron usar la solución; "
                  "los afectados no eligieron nada**, y por eso encontrarlos es trabajo técnico y no "
                  "un gesto de buena voluntad. Aproveche para cerrar una conexión que atraviesa "
                  "cuatro sesiones y que hoy se vuelve visible: el límite de 200 KB por consulta que "
                  "definieron en la sesión 5 como indicador ambiental se convirtió en requisito no "
                  "funcional en la sesión 7, sirvió para descartar imágenes en las sesiones 10 y 11, "
                  "y hoy entra a la matriz como **medida de mitigación**. No se puede improvisar en "
                  "la sesión 13 lo que no se escribió en la 5 — y es la tercera vez en el corte que "
                  "el curso lo demuestra. Termine con la otra lección, la que más los va a "
                  "sorprender: **la mejor mitigación de este proyecto no es digital**, es una hoja "
                  "impresa en la puerta. Anuncie la sesión 14 —preparación de la presentación final "
                  "y ensayo general cronometrado— y recuerde que la exposición de la sesión 15 vale "
                  "el **15 %** del curso.",
        "conexion": "Hacia atrás: la **sesión 3** dejó el listado de actores no usuarios, que es la "
                    "mitad del taller de hoy; la **sesión 5** dejó el indicador ambiental, que hoy es "
                    "mitigación; la **sesión 6** dejó las cifras del problema, que hoy son los "
                    "indicadores de impacto; la **sesión 7** dejó el criterio de los 20 segundos, que "
                    "resultó ser una mitigación; la **sesión 9** dejó la exigencia de no citar lo que "
                    "no se puede defender, que hoy evita el cálculo inventado de emisiones; la "
                    "**sesión 12** dejó la lista de limitaciones conocidas, donde entra el riesgo de "
                    "sostenibilidad. Hacia adelante: la **sesión 14** convierte esto en dos "
                    "diapositivas de la presentación final —el impacto positivo con su número y el "
                    "negativo con su mitigación—; en la **sesión 15** el impacto es uno de los cinco "
                    "tramos calificados; y en el **informe final de la sesión 16** la matriz completa "
                    "es una sección propia.",
    },

    "errores": [
        {"dice": "«Nuestra solución beneficia a la comunidad»",
         "por_que": "Sirve para cualquier proyecto del mundo, así que no informa de nada. Y «la comunidad» es la palabra que evita nombrar a los afectados.",
         "pida": "A quién, exactamente, y qué le cambia, con un número: «evita unas 30 visitas fallidas al mes»."},
        {"dice": "«No genera ningún impacto negativo»",
         "por_que": "Es la frase que más credibilidad quita en un informe de ingeniería: toda solución tiene costos y el lector lo sabe.",
         "pida": "Quién trabaja más por su solución, y quién no puede usarla. Con esas dos preguntas aparecen los dos negativos."},
        {"dice": "«Reduce la huella de carbono en X toneladas»",
         "por_que": "El factor de conversión suele venir de una calculadora que nadie del equipo puede explicar. Un número indefendible es peor que ninguno.",
         "pida": "Trayectos evitados al mes, y una frase que diga que no se convierte a emisiones por falta de datos confiables."},
        {"dice": "«Permite consultar la disponibilidad» como impacto",
         "por_que": "Eso es una función del sistema, no un impacto. El impacto es lo que le cambia a alguien por poder consultar.",
         "pida": "«¿Y eso qué le cambia a quién?», repetido hasta llegar a una persona y un número."},
        {"dice": "Una fila de la matriz en blanco",
         "por_que": "El lector no puede distinguir entre «no aplica» y «no lo pensamos», así que asume lo segundo.",
         "pida": "«No aplica» con una línea de razón. Es una respuesta válida y bien calificada."},
    ],

    "dudas": [
        {"p": "¿Declarar un impacto negativo nos baja la nota?",
         "r": "Al contrario: **la sube**, y está en la rúbrica —20 de 100 puntos son exactamente por "
              "eso—. Un informe con solo impactos positivos no es optimista, es incompleto, y quien "
              "lo lea va a desconfiar del resto. En la práctica profesional pasa igual: el informe "
              "que reconoce sus costos y propone cómo reducirlos es el que se aprueba."},
        {"p": "¿Y si de verdad no podemos medir un impacto?",
         "r": "Se describe con precisión y se dice **cómo se podría medir**. «No sabemos cuántos "
              "vecinos no tienen datos móviles; se sabría con una encuesta de diez casas» es una "
              "respuesta profesional y se califica como tal. Lo que no sirve es un «no aplica» sin "
              "razón, ni un número inventado para llenar la casilla."},
        {"p": "¿La matriz da un puntaje objetivo del proyecto?",
         "r": "No, y es importante que quede claro: las escalas son **una convención para comparar y "
              "ordenar**, no una medición. Dos equipos honestos pueden calificar distinto el mismo "
              "impacto. La matriz sirve para priorizar y para forzar la conversación sobre lo que "
              "nadie había mirado; lo que sí es exigible es que cada calificación tenga su línea de "
              "justificación."},
        {"p": "¿Una mitigación puede ser algo que no sea software?",
         "r": "Sí, y muchas veces **es la mejor**. En el caso de la biblioteca, la mitigación más "
              "efectiva de la exclusión es una cartelera impresa en la puerta: cuesta una hoja a la "
              "semana y atiende justo a quien la solución digital deja fuera. La ingeniería no "
              "consiste en poner tecnología, sino en resolver el problema con los recursos que hay."},
    ],

    "notas_operativas": [
        "**Avise en la sesión 12 que hay que traer dos cosas:** el listado de actores no usuarios de "
        "la **sesión 3** y el indicador ambiental de la **sesión 5**. Sin ellos, el taller de 17 "
        "minutos no alcanza.",
        "En la apertura, pida en el muro **un afectado que no sea usuario** por equipo. Es el "
        "diagnóstico más rápido de quién trajo el material y quién no.",
        "En las salas, entre con una sola pregunta: **«¿quién queda peor?»**. Si responden «nadie», "
        "use el paso 3 y aparece en un minuto.",
        "El error de calibración más común es **adjetivo donde va un número**. Pida el indicador en "
        "voz alta: «beneficia a la comunidad» → ¿cuántas personas, cuántas veces al mes?",
        "**No deje pasar un «no tenemos impactos negativos»**, y no humille al equipo: pregunte quién "
        "trabaja más por su solución. Hágalo delante del curso, es el intercambio del que más se "
        "aprende.",
        "Diga en voz alta el límite del método: **la escala ordena, no mide.** Evita que confundan "
        "una convención con un dato, que es un error frecuente en informes técnicos.",
        "Premie públicamente al equipo que declare el negativo más incómodo y al que proponga una "
        "**mitigación no digital**: son las dos conductas que quiere ver en el informe final.",
        "Recuerde que la exposición de la **sesión 15 vale el 15 %** y el informe final de la 16 el "
        "**20 %**. Desde hoy conviene que lo tengan presente.",
    ],

    "ti_siguiente": {
        "tid": "Aplicación de matrices de evaluación — dejar la matriz de impacto completa en el "
               "documento del equipo, con indicadores, negativos y mitigaciones.",
        "ti": "Informe de evaluación del impacto: media página que resuma **el impacto positivo más "
              "fuerte con su número y el negativo más importante con su mitigación**. Es el borrador "
              "de dos diapositivas de la presentación final.",
        "adelanto": "preparamos la **presentación final**: la estructura de 8 minutos, las "
                    "diapositivas, el reparto entre integrantes y el **ensayo general cronometrado**.",
        "aviso": "Para la sesión 14 el **prototipo tiene que estar ya ajustado** con lo que salió de "
                 "la sesión 12: si ensayan con la versión vieja, el ensayo no sirve. Traigan también "
                 "la cuenta de Canva o Google Slides lista y **quién va a hablar de qué**.",
    },

    "cierre_titulo": "Nos vemos en la sesión 14",
    "cierre_frase": "Los usuarios eligieron usarla; los afectados no eligieron nada",
}


# =============================================================================
# CLASE 14 · Preparacion de la presentacion final
# =============================================================================
# Reparto propio: el bloque de exposiciones se convierte en ensayo cronometrado de
# los PRIMEROS 4 MINUTOS de cada equipo (5 x 6 min = 4 de ensayo + 2 de correccion).
# Se ensaya solo el arranque porque es donde todos los equipos se pasan de tiempo.

TEMAS[14] = {
    "n": 14,
    "titulo": "Preparación de la presentación final",
    "subtitulo": "Nueve minutos, ocho diapositivas y un plan B para cuando falle internet",
    "hook": "En la sesión 15 tienen nueve minutos y se corta al llegar a cero. "
            "¿Cuánto creen que dura contar el problema, los actores y el árbol de causas?",
    "hook_lines": [
        "Más de nueve minutos. Por eso hoy se decide qué NO se cuenta.",
        "Una presentación no se acorta hablando rápido: se acorta eligiendo.",
    ],
    "objetivos": [
        "Armar un guion de **nueve minutos en cinco tramos**, con el tiempo asignado a cada uno.",
        "Hacer diapositivas que **se miren** en vez de leerse.",
        "Repartir la presentación entre los integrantes, con **tarea para quien no habla**.",
        "Preparar la **demostración del prototipo** y su **plan B** para cuando algo falle.",
    ],
    "agenda_slots": [
        ("Apertura", 6, "Pregunta de entrada en el muro"),
        ("Teoría y guía del docente", 22, "Los cinco tramos, las diapositivas, el reparto y el plan B"),
        ("Actividad en equipos", 27, "Armar el guion, las diapositivas y la demostración"),
        ("Ensayo cronometrado", 30, "5 equipos × 6 min — 4 de ensayo del arranque y 2 de corrección"),
        ("Cierre", 5, "Lo que falta antes de la sesión 15"),
    ],
    "agenda_sub": "Hoy nadie expone para lucirse: se ensaya con cronómetro y se corrige. La "
                  "presentación con nota es la próxima sesión",
    "nota_bloque": "**El bloque de exposiciones de hoy es un ensayo**, no una presentación: cada "
                   "equipo ensaya **los primeros 4 minutos** frente al cronómetro y recibe 2 minutos "
                   "de corrección. Se ensaya solo el arranque porque **es donde todos los equipos se "
                   "pasan de tiempo**: quien controla los primeros cuatro minutos casi siempre llega "
                   "bien al final. El resto se ensaya en equipo, fuera de clase, antes de la sesión "
                   "15.",
    "agenda": {},
    "herramienta_nota": "Las diapositivas en **Canva** o en **Google Slides**, como prefieran: las "
                        "dos son gratuitas y sirven igual. Google Slides tiene una ventaja concreta "
                        "—se abre desde cualquier computador y no depende de una cuenta de Canva—. "
                        "El guion y el reparto van en el **documento del equipo**. **Hoy no se usa "
                        "asistente de IA.** Y una obligación técnica: **la presentación descargada en "
                        "PDF** y **capturas de cada paso del prototipo**, guardadas en la carpeta del "
                        "equipo antes de salir de clase.",
    "avance_proyecto": "Guion de nueve minutos, diapositivas, reparto entre integrantes, "
                       "demostración preparada y plan B técnico — todo listo para la sesión 15",

    "teoria": [
        {
            "tipo": "steps",
            "titulo": "Los cinco tramos de nueve minutos",
            "steps": [
                ("1 · El problema, con su cifra · 1 min", "Una frase y un número: «4 de cada 10 visitas terminan sin préstamo». **Sin rodeos y sin presentaciones personales**: el nombre del equipo está en la diapositiva."),
                ("2 · A quién le pasa y qué decidimos · 2 min", "Los afectados —incluido el que no es usuario— y **la decisión de la matriz**: qué alternativa se eligió y qué se sacrificó."),
                ("3 · La solución y el prototipo en vivo · 3 min", "El tramo más largo. **Se muestra funcionando**, no se describe: un recorrido de tres pasos por la pantalla."),
                ("4 · Lo que falló en la prueba · 2 min", "Los hallazgos con una persona ajena, qué se arregló y **qué se decidió no arreglar**. Es el tramo que distingue un proyecto de una idea."),
                ("5 · Impacto y siguiente paso · 1 min", "El impacto positivo con su número, **el negativo con su mitigación**, y qué haría el próximo equipo que lo continúe."),
            ],
            "sub": "Nueve minutos exactos y se corta al llegar a cero. El tramo 4 es el que más suben la nota y el que todos quieren saltarse",
        },
        {
            "tipo": "cards",
            "titulo": "Cuatro reglas de diapositiva",
            "cards": [
                ("Una idea por diapositiva",
                 "Ocho diapositivas para nueve minutos: **un poco más de un minuto cada una**. Si una "
                 "diapositiva tiene tres ideas, en realidad son tres diapositivas apuradas."),
                ("La diapositiva no se lee",
                 "Si está escrito completo, el público lo lee más rápido de lo que usted lo dice, y "
                 "deja de escucharlo. **El texto es rótulo; el contenido lo pone la voz.**"),
                ("Un número grande vale más que un párrafo",
                 "«4 de 10» en tamaño enorme se recuerda; «se identificó que aproximadamente el "
                 "cuarenta por ciento…» no. Los datos de su proyecto merecen tamaño."),
                ("Se ve desde el fondo del salón",
                 "Texto grande, contraste alto, sin fondos que compitan. En una pantalla compartida "
                 "por video **todo se ve más pequeño y más borroso** de lo que usted lo ve."),
            ],
            "columns": 2,
        },
        {
            "tipo": "tabla",
            "titulo": "El reparto: qué hace cada integrante, incluso quien no habla",
            "headers": ["Tramo", "Quién habla", "Qué hace el resto del equipo"],
            "rows": [
                ["1 y 2 · Problema y decisión",
                 "Un integrante, el más claro para arrancar.",
                 "Uno controla el **cronómetro** y avisa por chat interno a los 2 min."],
                ["3 · La solución en vivo",
                 "Uno narra y **otro maneja la pantalla**. Nunca la misma persona.",
                 "Quien no narra ni maneja tiene abiertas las **capturas del plan B**."],
                ["4 · Lo que falló",
                 "Preferiblemente quien hizo la prueba: cuenta lo que vio.",
                 "El que sigue **ya tiene su diapositiva a la vista** para no perder segundos."],
                ["5 · Impacto y siguiente paso",
                 "El que cierra. Es el que deja la última impresión.",
                 "Todos preparados para las preguntas: **cada uno responde de su tramo**."],
            ],
            "note": "Todos los integrantes hablan, y **nadie habla menos de un minuto ni más de "
                    "tres**. Un equipo donde uno solo presenta pierde puntos de reparto, y además "
                    "arriesga todo a que esa persona tenga buena conexión ese día.",
            "col_w": [2.4, 3.5, 3.9],
        },
        {
            "tipo": "before_after",
            "titulo": "La diapositiva que se lee y la que se mira",
            "before_title": "Lo que casi todos hacen",
            "before": [
                "Título: «Planteamiento del problema».",
                "Seis viñetas de dos líneas cada una.",
                "El texto completo de lo que la persona va a decir.",
                "Una tabla con las quince filas de la matriz de decisión.",
                "Letra de tamaño 14 «porque así cabe todo».",
            ],
            "after_title": "Lo que se mira y se recuerda",
            "after": [
                "Título: «**4 de cada 10 visitas terminan sin préstamo**».",
                "Tres viñetas de **cinco palabras**.",
                "Un número enorme y una frase corta debajo.",
                "**Solo las dos alternativas y el ganador**; la matriz completa va en el informe.",
                "Letra grande: si no cabe, **es que hay que quitar contenido**, no reducir la letra.",
            ],
            "sub": "El público no puede leer y escuchar a la vez. Si la diapositiva lo dice todo, usted está de sobra",
            "size": 13,
        },
        {
            "tipo": "box",
            "titulo": "El plan B técnico, y tres trampas del ensayo",
            "notas": [
                ("advertencia",
                 "**El plan B no es opcional: es parte de la nota.** Antes de salir hoy, en la "
                 "carpeta del equipo: la presentación **descargada en PDF**, **capturas de cada paso** "
                 "de la demostración del prototipo, y un acuerdo de **quién comparte pantalla si al "
                 "primero se le cae la conexión**. Un equipo que no puede mostrar su prototipo porque "
                 "«no cargó» pierde el tramo más largo de su presentación."),
                ("advertencia",
                 "**No ensayar «mentalmente».** Leer el guion en silencio dura la mitad que decirlo "
                 "en voz alta, y por eso todos los equipos que no ensayan se pasan de tiempo. **Se "
                 "ensaya hablando, con cronómetro, aunque dé pena.** Es la única manera de saber "
                 "cuánto dura de verdad."),
                ("aclaracion",
                 "**No leer la diapositiva ni el guion palabra por palabra.** Se lleva una "
                 "**tarjeta con cuatro palabras clave** por tramo, no un texto. Y la última: **no "
                 "improvisar el arranque.** Las dos primeras frases se aprenden de memoria; son las "
                 "que más nervios dan y las que fijan el tono de los nueve minutos."),
            ],
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada: cuánto dura contarlo todo",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "La apertura de hoy es una pregunta con trampa aritmética, y funciona porque la "
                "respuesta la descubren ellos: **¿cuánto dura contar el problema, los actores y el "
                "árbol de causas?** Más de nueve minutos. Solo el árbol de causas de la sesión 6, "
                "contado como lo contaron entonces, se lleva cuatro.",
                "De ahí sale la idea que ordena toda la sesión y que conviene decir literalmente: "
                "**una presentación no se acorta hablando rápido, se acorta eligiendo.** Es la misma "
                "operación del alcance mínimo de la sesión 8 aplicada al tiempo en vez del producto. "
                "Los equipos que fracasan en la sesión 15 no fracasan por hablar mal: fracasan porque "
                "intentaron contarlo todo y se les acabó el tiempo en el tramo 2, dejando fuera "
                "precisamente el prototipo y los hallazgos, que es lo único que el jurado no conoce.",
                "En el muro, cada equipo escribe **qué va a dejar fuera**. Es una pregunta incómoda y "
                "es exactamente el trabajo de hoy: dejar fuera el árbol de causas completo, la "
                "revisión bibliográfica extensa, la historia de cómo se conocieron, las quince filas "
                "de la matriz.",
                "Y una advertencia de encuadre para el docente: hoy nadie expone para lucirse. El "
                "bloque de 30 minutos es un **ensayo con corrección**, y hay que decirlo al principio "
                "para que los equipos traigan lo que tienen aunque esté a medias. Un equipo que "
                "esconde su presentación hoy porque «no está lista» está renunciando a la única "
                "corrección antes de la nota.",
            ],
        },
        {
            "titulo": "Los cinco tramos, y por qué el tramo 4 es el que sube la nota",
            "slide": "{{slide:Los cinco tramos}}",
            "cuerpo": [
                "La estructura de cinco tramos no es un formato arbitrario: es el orden en que un "
                "lector técnico necesita la información —problema, decisión, solución, evidencia, "
                "consecuencias— y coincide con la estructura de cualquier informe de ingeniería. Vale "
                "la pena decirlo, porque el mismo esqueleto les va a servir en la sesión 16 para el "
                "informe y en toda la carrera para cualquier sustentación.",
                "**Tramo 1 · el problema con su cifra, 1 minuto.** El error universal es empezar con "
                "presentaciones personales y agradecimientos: «buenas tardes, somos el equipo tal, "
                "integrado por…». Eso consume el minuto más valioso de los nueve. **El nombre del "
                "equipo está en la diapositiva**; se arranca con el problema y su número.",
                "**Tramo 2 · a quién le pasa y qué decidimos, 2 minutos.** Aquí entra un afectado que "
                "no es usuario —trabajo de la sesión 13— y, sobre todo, **la decisión de la matriz de "
                "la sesión 8 con lo que se sacrificó**. Decir «elegimos la lista publicada y "
                "sacrificamos tener la información al minuto» en diez segundos comunica más madurez "
                "que cinco minutos de descripción.",
                "**Tramo 3 · la solución y el prototipo en vivo, 3 minutos.** Es el tramo más largo y "
                "la regla es una: **se muestra funcionando, no se describe.** Un recorrido de tres "
                "pasos por la pantalla, narrado por una persona mientras otra maneja el mouse.",
                "**Tramo 4 · lo que falló, 2 minutos.** Este es el tramo que hay que defender con "
                "insistencia, porque **todos los equipos quieren saltárselo** y es el que más sube la "
                "nota. Contar que una persona ajena abandonó la tarea, que se arregló el rótulo y que "
                "se decidió **no** arreglar la búsqueda tolerante, es lo que distingue un proyecto de "
                "una idea bonita. Un jurado técnico premia eso; un equipo que presenta todo perfecto "
                "genera desconfianza inmediata, porque nadie cree que un prototipo de primer semestre "
                "funcionó a la primera.",
                "**Tramo 5 · impacto y siguiente paso, 1 minuto.** El positivo con su número, **el "
                "negativo con su mitigación** —de nuevo la sesión 13— y qué haría quien continúe el "
                "proyecto. Cerrar con el siguiente paso deja la sensación de trabajo vivo y no de "
                "tarea entregada.",
            ],
        },
        {
            "titulo": "Diapositivas que se miran, y el reparto que reparte de verdad",
            "slide": "{{slide:Cuatro reglas de diapositiva}} {{slide:El reparto}} {{slide:La diapositiva que se lee}}",
            "cuerpo": [
                "El argumento central sobre diapositivas es de atención, no de estética, y hay que "
                "darlo así porque es el que convence: **el público no puede leer y escuchar a la vez.** "
                "Si la diapositiva tiene el texto completo, la gente lo lee más rápido de lo que "
                "usted lo dice, termina antes, y deja de escucharlo justo cuando usted está "
                "explicando lo importante. La conclusión es incómoda y hay que decirla: **si la "
                "diapositiva lo dice todo, usted está de sobra.**",
                "De las cuatro reglas, la que más cuesta es **una idea por diapositiva**. Con ocho "
                "diapositivas para nueve minutos hay poco más de un minuto por diapositiva; si una "
                "tiene tres ideas, en realidad son tres diapositivas apuradas. Y la regla del tamaño "
                "de letra tiene una consecuencia práctica que conviene enunciar como ley: **si no "
                "cabe, hay que quitar contenido, no reducir la letra.** En una pantalla compartida "
                "por video todo se ve más pequeño y más borroso de lo que se ve en el computador de "
                "quien la hizo.",
                "La diapositiva de antes y después es el ejercicio más eficaz de la sesión. La "
                "columna izquierda es literalmente lo que van a entregar si no se les enseña otra "
                "cosa; la derecha muestra el mismo contenido convertido en rótulo. Deténgase en la "
                "cuarta fila: **la matriz de decisión completa no va en la presentación** —van las dos "
                "alternativas y el ganador—, porque la matriz es material de informe. Distinguir qué "
                "va en el informe y qué va en la presentación es una habilidad profesional y es lo "
                "que más les va a servir la próxima vez.",
                "Sobre el reparto, hay dos exigencias que evitan los dos fracasos típicos. La "
                "primera: **todos los integrantes hablan, y nadie habla menos de un minuto ni más de "
                "tres.** Un equipo donde solo uno presenta pierde puntos y, peor, arriesga la nota "
                "entera a que esa persona tenga buena conexión ese día. La segunda: **quien no habla "
                "también tiene tarea** —cronómetro, capturas del plan B, la diapositiva siguiente "
                "lista—. En la demostración del tramo 3, **narrar y manejar la pantalla no las hace "
                "la misma persona**: intentar las dos cosas a la vez es la causa más común de que una "
                "demostración se caiga. Y para las preguntas, cada integrante responde de su tramo, "
                "lo cual además obliga a que todos entiendan el proyecto completo.",
            ],
        },
        {
            "titulo": "El plan B, el ensayo, y por qué se ensaya solo el arranque",
            "slide": "{{slide:El plan B técnico}}",
            "cuerpo": [
                "**El plan B es parte de la nota y hay que ser explícito.** Antes de salir hoy, en la "
                "carpeta del equipo tienen que quedar tres cosas: la presentación **descargada en "
                "PDF**, **capturas de cada paso** de la demostración del prototipo, y un acuerdo de "
                "**quién comparte pantalla si al primero se le cae la conexión**. El argumento no es "
                "burocrático sino aritmético: la demostración es el tramo de 3 minutos, un tercio de "
                "la presentación; un equipo que no puede mostrar su prototipo porque «no cargó» "
                "perdió un tercio de su nota por algo que se prevenía en cinco minutos. Y en clase "
                "virtual esto no es hipotético: pasa cada semestre.",
                "**Sobre el ensayo, la trampa principal es ensayar «mentalmente».** Leer el guion en "
                "silencio dura aproximadamente la mitad que decirlo en voz alta, y por eso todos los "
                "equipos que no ensayan se pasan de tiempo — creen que su presentación dura seis "
                "minutos y dura trece. Hay que insistir aunque dé pena: **se ensaya hablando, con "
                "cronómetro.**",
                "Las otras dos trampas: **no leer** —se lleva una tarjeta con cuatro palabras clave "
                "por tramo, no un texto, porque leer mata el contacto con el público y además suena "
                "peor— y **no improvisar el arranque**. Las dos primeras frases se aprenden de "
                "memoria: son las que más nervios dan y las que fijan el tono de los nueve minutos. "
                "Es un consejo pequeño y funciona.",
                "**Por qué hoy se ensayan solo los primeros 4 minutos**, y conviene explicarlo para "
                "que no parezca un recorte: cinco equipos por nueve minutos son 45 minutos y no "
                "caben con corrección. Pero además **el arranque es donde se pierde el tiempo**: el "
                "equipo que controla los tramos 1 y 2 casi siempre llega bien al final, y el que se "
                "pasa en el tramo 2 ya no tiene manera de recuperarse. Ensayar el arranque con "
                "cronómetro es la intervención con mejor rendimiento por minuto invertido. El resto "
                "se ensaya en equipo, fuera de clase, y hay que decirlo con claridad: **quien no "
                "ensaye completo antes de la sesión 15 se va a pasar de tiempo, y a los nueve minutos "
                "se corta.**",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:06 · Apertura · [Slide 4]",
            "cuerpo": [
                "Comparta pantalla antes de que entre el primero:",
                "> «En la sesión 15 tienen nueve minutos y se corta al llegar a cero. ¿Cuánto creen "
                "que dura contar el problema, los actores y el árbol de causas?»",
                "En el muro, cada equipo escribe **qué va a dejar fuera**. Es el trabajo de hoy en "
                "una línea.",
                "**[Nota docente]:** encuadre el día: **hoy nadie expone para lucirse, hoy se ensaya "
                "y se corrige.** Que traigan lo que tengan aunque esté a medias — esconderlo hoy es "
                "renunciar a la única corrección antes de la nota.",
                "**[Nota docente]:** diga la frase que ordena la sesión: **una presentación no se "
                "acorta hablando rápido, se acorta eligiendo.**",
            ],
        },
        {
            "titulo": "00:06–00:28 · Teoría (22 min) · [Slide 5]…[Slide 9]",
            "cuerpo": [
                "Reparto:",
                "- **6 min** · Los cinco tramos [Slide 5]. Defienda el **tramo 4**: es el que todos "
                "quieren saltarse y el que más sube la nota.",
                "- **4 min** · Las cuatro reglas de diapositiva [Slide 6]. La ley: **si no cabe, se "
                "quita contenido, no se reduce la letra.**",
                "- **4 min** · El reparto [Slide 7]. Las dos exigencias: **todos hablan** y **narrar "
                "y manejar la pantalla no las hace la misma persona.**",
                "- **5 min** · Antes y después [Slide 8]. Deténgase en la fila de la matriz: **la "
                "matriz completa va en el informe, no en la presentación.**",
                "- **3 min** · Plan B y trampas del ensayo [Slide 9]. Diga que el plan B **es parte "
                "de la nota** y que se entrega hoy, no la próxima sesión.",
            ],
        },
        {
            "titulo": "00:28–00:55 · Taller en salas de grupo (27 min) · [Slide 10]",
            "cuerpo": [
                "Ritmo sugerido dentro de la sala:",
                "- 8 min · el **guion de los cinco tramos** con el tiempo de cada uno y quién habla.",
                "- 10 min · las **ocho diapositivas** — rótulos, no párrafos.",
                "- 5 min · ensayar **la demostración del prototipo** dos veces: quién narra, quién "
                "maneja la pantalla.",
                "- 4 min · el **plan B**: PDF descargado, capturas, quién comparte si se cae el "
                "primero.",
                "**[Nota docente]:** entre a las cinco salas con una sola pregunta: **«¿cuánto dura "
                "su tramo 2?»**. Si no lo saben, no tienen guion: tienen intenciones.",
                "**[Nota docente]:** verifique el plan B equipo por equipo **antes de que termine el "
                "bloque**. Después ya no hay tiempo, y en la sesión 15 es tarde.",
            ],
        },
        {
            "titulo": "00:55–01:25 · Ensayo cronometrado (30 min) · [Slide 11]",
            "cuerpo": [
                "5 equipos × 6 min: **4 minutos de ensayo del arranque** (tramos 1, 2 y el comienzo "
                "del 3) y **2 minutos de corrección**. Cronómetro en pantalla, visible para todos.",
                "**[Nota docente]:** corte exactamente a los 4 minutos, incluso en mitad de una "
                "frase. Es incómodo y es el aprendizaje: en la sesión 15 va a pasar lo mismo.",
                "**[Nota docente]:** en los 2 minutos de corrección, diga **una sola cosa** — la que "
                "más les cambie la presentación. Lo más frecuente, en orden: se presentaron en vez de "
                "empezar por el problema; leyeron la diapositiva; se pasaron en el tramo 2; la misma "
                "persona narraba y manejaba la pantalla.",
                "**[Nota docente]:** anote **dónde iba cada equipo al minuto 4**. Si a los 4 minutos "
                "no llegó al prototipo, no va a alcanzar: dígaselo con ese dato en la mano.",
                "Los demás equipos observan y anotan una cosa que van a copiar y una que van a "
                "evitar. Se comparte en el muro, sin nombres.",
            ],
        },
        {
            "titulo": "01:25–01:30 · Cierre · [Slide 12][Slide 13]",
            "cuerpo": [
                "Verifique en voz alta la lista de la sesión 15: **guion con tiempos, ocho "
                "diapositivas, reparto, demostración ensayada, PDF descargado y capturas en la "
                "carpeta.**",
                "Una idea: **una presentación no se acorta hablando rápido, se acorta eligiendo.**",
                "Recuerde lo que vale: la exposición de la sesión 15 es el **15 %** del curso, y "
                "**se corta a los nueve minutos**. Quien no ensaye completo se va a pasar.",
            ],
        },
    ],

    "taller": {
        "archivo": "Guion de la presentacion final",
        "titulo": "Guion de nueve minutos y plan B",
        "min": 27,
        "exposicion": 4,
        "consigna": "Armen la presentación final: el **guion de los cinco tramos con sus tiempos y "
                    "quién habla**, las **ocho diapositivas**, el **reparto** con tarea para quien no "
                    "habla, la **demostración del prototipo** ensayada dos veces, y el **plan B "
                    "técnico** guardado en la carpeta antes de salir.",
        "entregable": "el guion con tiempos en el documento del equipo, las diapositivas, y en la "
                      "carpeta del equipo: la presentación en PDF y las capturas de cada paso de la "
                      "demostración",
        "entregable_corto": "guion con tiempos + diapositivas + PDF y capturas del plan B",
        "reparto_titulo": "Ritmo sugerido dentro de la sala (27 min):",
        "reparto": "8 min el guion de los cinco tramos con tiempos y quién habla · 10 min las ocho "
                   "diapositivas · 5 min ensayar la demostración dos veces · 4 min el plan B. **No "
                   "empiecen por las diapositivas**: sin guion, las diapositivas se hacen dos veces.",
        "reparto_corto": "27 min: guion, diapositivas, demostración y plan B",
        "bloques": [
            {"clave": "EL GUION DE LOS CINCO TRAMOS",
             "pide": "Los cinco tramos con **el tiempo asignado a cada uno** —que sume nueve "
                     "minutos— y **quién habla** en cada uno.",
             "check": "los tiempos suman 9 y están asignados por persona. Un guion sin tiempos no es un guion: es una lista de temas."},
            {"clave": "LAS OCHO DIAPOSITIVAS",
             "pide": "Máximo ocho, **una idea cada una**, con rótulos y no párrafos. La matriz "
                     "completa **no va**: van las dos alternativas y el ganador.",
             "check": "ninguna diapositiva tiene el texto completo de lo que se va a decir, y la letra se ve desde lejos."},
            {"clave": "EL REPARTO ENTRE INTEGRANTES",
             "pide": "Quién habla en cada tramo, y **qué hace quien no habla**: cronómetro, capturas "
                     "del plan B, la diapositiva siguiente lista.",
             "check": "todos hablan, nadie habla menos de un minuto ni más de tres, y quien no habla tiene tarea asignada."},
            {"clave": "LA DEMOSTRACIÓN DEL PROTOTIPO",
             "pide": "El recorrido de **tres pasos** que se va a mostrar, con **una persona narrando "
                     "y otra manejando la pantalla**. Ensayado dos veces.",
             "check": "el recorrido cabe en 3 minutos y narrar y manejar la pantalla son dos personas distintas."},
            {"clave": "EL PLAN B TÉCNICO",
             "pide": "En la carpeta del equipo: la presentación **en PDF**, **capturas de cada paso** "
                     "de la demostración, y quién comparte pantalla si se cae el primero.",
             "check": "los archivos están en la carpeta hoy, no prometidos para mañana. Es parte de la nota."},
        ],
        "expo": [
            ("Tramo 1 · 1 min", "El problema con su cifra. **Sin presentaciones personales.**"),
            ("Tramo 2 · 2 min", "Los afectados y la decisión de la matriz, con lo que se sacrificó."),
            ("Comienzo del tramo 3 · 1 min", "Arrancar la demostración: hasta donde llegue en el minuto."),
            ("Corte a los 4 min", "Se corta en mitad de la frase. En la sesión 15 pasa igual."),
            ("2 min de corrección", "El docente dice **una sola cosa**, la que más cambie la presentación."),
        ],
    },

    "rubrica": [
        ("El guion tiene los cinco tramos, con tiempos que suman nueve minutos y quién habla", 25,
         "Un guion sin tiempos asignados es una lista de temas, y las listas de temas se pasan de tiempo."),
        ("Las diapositivas son rótulos y no párrafos, máximo ocho, legibles", 20,
         "El público no puede leer y escuchar a la vez: si la diapositiva lo dice todo, el expositor está de sobra."),
        ("Todos los integrantes hablan y quien no habla tiene tarea asignada", 15,
         "Reparte el riesgo técnico y obliga a que todos entiendan el proyecto completo."),
        ("La demostración cabe en tres minutos, con narrador y operador distintos", 25,
         "Es el tramo más largo y el que más se cae: intentar narrar y manejar la pantalla a la vez es la causa habitual."),
        ("El plan B está en la carpeta hoy: PDF, capturas y quién comparte pantalla", 15,
         "Perder el tramo de la demostración por un problema técnico previsible es perder un tercio de la nota."),
    ],

    "solucion": {
        "para_que": "Este documento trae el guion completo de nueve minutos del caso de la "
                    "biblioteca, **tramo por tramo y con las frases textuales del arranque y del "
                    "cierre**, más las ocho diapositivas descritas una por una. Sirve como modelo "
                    "para proyectar y como referencia al corregir en el ensayo. Si solo alcanza a "
                    "leer un bloque, que sea **EL GUION DE LOS CINCO TRAMOS**: las frases del tramo "
                    "1 son las que más rinde leer en voz alta en clase.",
        "caso_titulo": "La biblioteca del barrio · presentación final de nueve minutos",
        "caso": "Equipo de cuatro integrantes. Proyecto: lista en línea de disponibilidad de libros, "
                "consultable desde el celular sin cuenta, actualizada por la voluntaria al cierre. "
                "Material acumulado: ficha del problema (sesión 6), requisitos y criterios (7), matriz "
                "de decisión y alcance mínimo (8), antecedentes (9), prototipo v1 y v2 (10 y 11), "
                "hallazgos de la prueba con dos personas (12) y matriz de impacto (13).",
        "por_que_este_caso": "Porque tiene más material del que cabe en nueve minutos —igual que "
                            "todos los equipos— y por eso obliga a mostrar las decisiones de "
                            "recorte: el árbol de causas completo no entra, la matriz de quince "
                            "filas no entra, los tres antecedentes no entran. Ver qué se sacrifica "
                            "enseña más que ver qué se incluye.",
        "bloques": [
            {
                "clave": "EL GUION DE LOS CINCO TRAMOS",
                "respuesta": "**Tramo 1 · El problema, con su cifra · 1:00 · habla Ana**\n\n"
                             "> «De cada diez personas que van a la biblioteca del barrio Los "
                             "Cámbulos, **cuatro se devuelven sin el libro** que iban a buscar. "
                             "Veinticinco minutos de camino y un pasaje, para nada. Eso es lo que "
                             "quisimos resolver.»\n\n"
                             "*Son 18 segundos. El resto del minuto: cómo lo contaron —el conteo de "
                             "dos semanas— y quiénes son los afectados en una frase.* **Nótese que no "
                             "hay saludo, ni nombres, ni «vamos a presentar»**: el nombre del equipo "
                             "está en la diapositiva 1.\n\n"
                             "**Tramo 2 · A quién le pasa y qué decidimos · 2:00 · habla Ana (1 min) "
                             "y Brayan (1 min)**\n\n"
                             "*Ana, 1 min:* los usuarios que consultan, **y los dos afectados que no "
                             "son usuarios**: la voluntaria del cierre, a quien le llega trabajo "
                             "nuevo, y el vecino sin datos móviles, que queda atrás en el mostrador.\n\n"
                             "*Brayan, 1 min, la decisión:*\n"
                             "> «Teníamos dos caminos: publicar una lista que la voluntaria actualiza "
                             "una vez al día, o un registro en línea en tiempo real. Con una matriz de "
                             "cinco criterios ganó la lista, **y perdimos algo a propósito: la "
                             "información no está al minuto**. Aceptamos eso porque la alternativa "
                             "exigía un computador en el mostrador, que no existe.»\n\n"
                             "*Diez segundos para decir qué se sacrificó. Es el momento de mayor "
                             "madurez de toda la presentación.*\n\n"
                             "**Tramo 3 · La solución y el prototipo en vivo · 3:00 · narra Brayan, "
                             "maneja la pantalla Camila**\n\n"
                             "Recorrido de tres pasos, sin describir la interfaz: (1) buscar «cien "
                             "años», (2) ver el resultado con su estado y **la fecha del dato**, (3) "
                             "la pantalla de la voluntaria marcando un préstamo en menos de 20 "
                             "segundos, cronometrado en vivo.\n\n"
                             "**Tramo 4 · Lo que falló en la prueba · 2:00 · habla Camila**\n\n"
                             "> «Le dimos el prototipo a dos personas que no son del equipo y no les "
                             "explicamos nada. **Las dos tocaron el estado «Prestado» esperando que se "
                             "abriera algo**, y una señora escribió «100 años» en vez de «cien años», "
                             "no encontró nada y abandonó.»\n\n"
                             "*Y después, lo que se hizo:* el estado dejó de parecer un botón y ahora "
                             "dice «no sabemos cuándo vuelve»; el rótulo de la fecha se reescribió. "
                             "**Y lo que se decidió no hacer:** la búsqueda que tolera errores de "
                             "escritura excede lo que el equipo puede construir este semestre, y "
                             "queda declarada como limitación conocida.\n\n"
                             "**Tramo 5 · Impacto y siguiente paso · 1:00 · habla Daniel**\n\n"
                             "> «Si la mitad de esos viajes fallidos se evitan, son **30 viajes menos "
                             "al mes**: 30 pasajes y unas 12 horas que el barrio no gasta. Pero hay un "
                             "costo: **la voluntaria del cierre trabaja diez minutos más cada día**, y "
                             "**una de cada cinco personas no tiene datos para consultar**. Por eso "
                             "propusimos una cartelera impresa en la puerta, una hoja por semana, para "
                             "quien llega caminando. El siguiente equipo que lo continúe debería "
                             "empezar por la búsqueda tolerante a errores.»\n\n"
                             "---\n\n"
                             "**Lo que quedó fuera, y es la parte instructiva del guion:** el árbol de "
                             "causas completo de la sesión 6, los tres antecedentes de la sesión 9 "
                             "—se mencionan en una frase: «revisamos qué existía y encontramos "
                             "software libre maduro que no servía para este caso»—, las quince filas "
                             "de la matriz, el prototipo v1, y toda la matriz de impacto salvo dos "
                             "números. **Todo eso va en el informe final de la sesión 16.**\n\n"
                             "*Tiempos: 1 + 2 + 3 + 2 + 1 = 9 minutos exactos. En el ensayo real, "
                             "este guion dio 10:40 la primera vez y 9:10 la tercera.*",
                "como_calificar": "25 pts: 10 por los cinco tramos con **tiempos que sumen 9**, 8 por "
                                  "la asignación de quién habla, y 7 por evidencia de recorte "
                                  "—que exista una lista explícita de lo que queda fuera—. El "
                                  "criterio duro: **un guion sin tiempos por tramo vale 8 como "
                                  "máximo**, porque es una lista de temas y las listas de temas se "
                                  "pasan. Valore alto al equipo que dedica diez segundos a decir "
                                  "**qué sacrificó** en la decisión: es lo que un evaluador técnico "
                                  "más premia y casi nadie lo hace."
            },
            {
                "clave": "LAS OCHO DIAPOSITIVAS",
                "respuesta": "| # | Título en pantalla | Contenido | Se usa en |\n"
                             "|---|---|---|---|\n"
                             "| 1 | **4 de cada 10 visitas terminan sin préstamo** | El número enorme. Debajo, pequeño: nombre del proyecto, integrantes, curso. | Tramo 1 |\n"
                             "| 2 | **A quién le pasa** | Tres rótulos: *quien consulta · la voluntaria del cierre · quien no tiene datos*. | Tramo 2 |\n"
                             "| 3 | **Dos caminos, uno elegido** | Solo las dos alternativas y una marca en la ganadora. Debajo: «sacrificamos la información al minuto». | Tramo 2 |\n"
                             "| 4 | **El prototipo** | Casi vacía: sirve para pasar a la pantalla compartida del prototipo. | Tramo 3 |\n"
                             "| 5 | **20 segundos por préstamo** | Una captura de la pantalla de la voluntaria y el número grande. | Tramo 3 |\n"
                             "| 6 | **Lo que falló con dos personas reales** | Dos rótulos: *tocaron «Prestado» esperando algo · escribió «100 años» y abandonó*. | Tramo 4 |\n"
                             "| 7 | **Qué arreglamos y qué no** | Dos columnas de tres palabras cada línea. | Tramo 4 |\n"
                             "| 8 | **30 viajes menos al mes · y 10 minutos más para la voluntaria** | Los dos números, positivo y negativo, del mismo tamaño. | Tramo 5 |\n\n"
                             "**Tres decisiones de diseño que conviene señalar en clase:**\n\n"
                             "- **La diapositiva 1 no dice «Planteamiento del problema»**: dice el "
                             "problema. Un título que es el dato ahorra una frase y arranca fuerte.\n"
                             "- **La diapositiva 4 está casi vacía a propósito.** Su función es "
                             "servir de puente para cambiar a la pantalla compartida del prototipo sin "
                             "que quede una diapositiva llena de texto detrás. Es un truco de oficio.\n"
                             "- **La diapositiva 8 pone el número positivo y el negativo del mismo "
                             "tamaño.** No es modestia: es la señal de honestidad que hace creíble "
                             "todo lo anterior, y un evaluador la nota.\n\n"
                             "**Lo que NO tiene ninguna diapositiva:** el árbol de causas, la matriz "
                             "completa, la lista de antecedentes, una diapositiva de «gracias» —los "
                             "nueve minutos terminan con el siguiente paso, que es más útil— y "
                             "ninguna con más de veinticinco palabras.",
                "como_calificar": "20 pts. Dos verificaciones rápidas que puede hacer de un vistazo: "
                                  "**¿hay alguna diapositiva con el texto completo de lo que se va a "
                                  "decir?** (si sí, máximo 10) y **¿se lee el texto más pequeño en la "
                                  "pantalla compartida?** (si no, máximo 12). Valore la diapositiva "
                                  "de transición vacía y la que pone el impacto positivo y el "
                                  "negativo con el mismo tamaño: las dos son decisiones de oficio y "
                                  "conviene nombrarlas al curso."
            },
            {
                "clave": "EL REPARTO ENTRE INTEGRANTES",
                "respuesta": "| Tramo | Habla | Los demás |\n"
                             "|---|---|---|\n"
                             "| 1 · Problema (1 min) | **Ana** | Daniel con el cronómetro. Camila con las capturas del plan B abiertas. |\n"
                             "| 2 · Afectados y decisión (2 min) | **Ana** (1) y **Brayan** (1) | Camila ya tiene la pestaña del prototipo cargada. |\n"
                             "| 3 · Solución en vivo (3 min) | Narra **Brayan** · maneja la pantalla **Camila** | Daniel avisa por chat interno al minuto 2 del tramo. |\n"
                             "| 4 · Lo que falló (2 min) | **Camila** — hizo la prueba, cuenta lo que vio | Brayan deja la diapositiva 7 lista. |\n"
                             "| 5 · Impacto y cierre (1 min) | **Daniel** | Todos preparados para preguntas, cada uno de su tramo. |\n\n"
                             "**Los tiempos por persona:** Ana 2:00 · Brayan 2:00 (más los 3 min "
                             "narrando) · Camila 2:00 (más el manejo de pantalla) · Daniel 1:00. "
                             "**Todos hablan, nadie baja de un minuto ni pasa de tres seguidos.**\n\n"
                             "**Dos decisiones que valen la nota:**\n\n"
                             "- **Camila narra el tramo 4 porque fue quien hizo la prueba.** Quien vio "
                             "a la señora abandonar lo cuenta con detalles que nadie más tiene. "
                             "Asignar los tramos por quién hizo el trabajo, y no por quién habla "
                             "mejor, mejora la presentación y además es justo.\n"
                             "- **En el tramo 3, Brayan narra y Camila maneja la pantalla.** Nunca la "
                             "misma persona: intentar hablar mientras se busca la pestaña correcta es "
                             "la causa más frecuente de que una demostración se caiga.\n\n"
                             "**Y las preguntas:** cada integrante responde de su tramo. Además de "
                             "repartir la presión, **obliga a que todos entiendan el proyecto "
                             "completo**, que es la mitad del sentido de un trabajo en equipo.",
                "como_calificar": "15 pts: 8 porque **todos hablen** entre uno y tres minutos, 7 "
                                  "porque **quien no habla tenga tarea escrita** (cronómetro, "
                                  "capturas, diapositiva siguiente). Un equipo donde presenta una "
                                  "sola persona vale 4, y hay que explicar los dos costos: pierde "
                                  "puntos y arriesga la nota entera a la conexión de esa persona. "
                                  "Valore que asignen el tramo 4 a **quien hizo la prueba**: es "
                                  "criterio de oficio."
            },
            {
                "clave": "LA DEMOSTRACIÓN DEL PROTOTIPO",
                "respuesta": "**El recorrido de tres pasos, con los tiempos del ensayo:**\n\n"
                             "**Paso 1 · 50 s · Buscar un libro que sí está.** Camila escribe «cien "
                             "años» y aparece el resultado: *Disponible · Esta información es del "
                             "viernes a las 6:00 p. m.* Brayan narra: **«esa segunda línea es "
                             "nuestra decisión más importante: preferimos decir cuándo es el dato "
                             "antes que fingir que está al minuto».**\n\n"
                             "**Paso 2 · 60 s · Buscar uno que está prestado.** Aparece *Prestado · no "
                             "sabemos cuándo vuelve*. Brayan cuenta que esa etiqueta **antes parecía "
                             "un botón** y que dos personas la tocaron esperando algo, así que se "
                             "cambió. *Conecta el tramo 3 con el 4 sin gastar tiempo.*\n\n"
                             "**Paso 3 · 70 s · La pantalla de la voluntaria, cronometrada en vivo.** "
                             "Camila marca un préstamo mientras Brayan cuenta en voz alta: «uno, dos, "
                             "tres… **catorce segundos**». *El criterio de aceptación era menos de "
                             "30.* **Cronometrar en vivo es el momento más efectivo de toda la "
                             "presentación**, porque el público ve cumplirse un criterio que se "
                             "definió cinco sesiones antes.\n\n"
                             "*Total 3:00. En el primer ensayo dio 4:20, porque narraron la interfaz "
                             "botón por botón. El recorte fue dejar de describir y empezar a mostrar.*\n\n"
                             "**Lo que NO se muestra:** el prototipo v1, las pantallas que no cambiaron, "
                             "los mensajes de error uno por uno —se menciona uno—, y nada que exija "
                             "explicar cómo está hecho por dentro.\n\n"
                             "**El error que hay que cazar en el ensayo:** narrar la interfaz. «Aquí "
                             "arriba tenemos un campo de búsqueda, y a la derecha un botón que dice "
                             "buscar…» consume el tramo entero sin decir nada. **Se muestra una tarea "
                             "cumpliéndose, no un inventario de la pantalla.**",
                "como_calificar": "25 pts: 10 porque el recorrido **quepa en 3 minutos** (cronométrelo "
                                  "en el ensayo, no lo estime), 8 porque **narrador y operador sean "
                                  "personas distintas**, 7 porque **muestre tareas y no describa la "
                                  "interfaz**. Si el equipo narra botón por botón, vale 10 y la "
                                  "corrección es de una frase: «no describa la pantalla, muestre a "
                                  "alguien logrando algo». Valore mucho el cronometraje en vivo de un "
                                  "criterio de aceptación: es la manera más convincente de cerrar el "
                                  "arco del curso en veinte segundos."
            },
            {
                "clave": "EL PLAN B TÉCNICO",
                "respuesta": "**Lo que quedó en la carpeta del equipo antes de salir de clase:**\n\n"
                             "1. **`Presentacion final.pdf`** — descargada, no solo compartida. Un "
                             "enlace no sirve si la conexión falla.\n"
                             "2. **`Capturas/` con seis imágenes numeradas** — un paso por captura del "
                             "recorrido de tres pasos, incluida la pantalla de la voluntaria con el "
                             "cronómetro visible. Si el prototipo no carga, **Brayan narra el mismo "
                             "recorrido sobre las capturas** y el tramo 3 se salva completo.\n"
                             "3. **El acuerdo de pantalla, escrito:** comparte Camila; si a Camila se "
                             "le cae la conexión, comparte Daniel, que tiene los mismos archivos "
                             "descargados en su computador. *No basta con que estén en la nube: "
                             "**descargados en dos computadores distintos**.*\n"
                             "4. **El orden de emergencia:** si falta un integrante, sus tramos los "
                             "asume quien está en la fila siguiente de la tabla de reparto. Decidido "
                             "hoy, no improvisado ese día.\n\n"
                             "**Por qué esto vale 15 puntos y no es burocracia:** la demostración es "
                             "el tramo de 3 minutos, un tercio de la presentación y 25 de los 100 "
                             "puntos de la rúbrica de la sesión 15. Un equipo que no puede mostrar su "
                             "prototipo porque «no cargó» **pierde un tercio de su nota por algo que "
                             "se prevenía en cinco minutos**. Y en sesiones virtuales esto no es "
                             "hipotético: pasa todos los semestres, en al menos un equipo.\n\n"
                             "**La versión corta para decir en clase:** *el plan B no es "
                             "desconfianza en la tecnología, es respeto por el tiempo de los demás.*",
                "como_calificar": "15 pts, y se califica **hoy, en la carpeta**, no prometido para "
                                  "mañana: 6 por el PDF descargado, 6 por las capturas de cada paso, "
                                  "3 por el acuerdo escrito de quién comparte. Revíselo equipo por "
                                  "equipo **antes de que termine el bloque de taller** — después no "
                                  "hay tiempo y en la sesión 15 es tarde. Un equipo que dice «lo "
                                  "hacemos en casa» vale 0 en este bloque, y conviene decirlo sin "
                                  "dramatismo: es la parte más fácil de los cien puntos del día."
            },
        ],
        "variantes": [
            {"caso": "Equipos que llegan sin nada preparado",
             "clave": "Pasa, y hoy es el mejor día para que pase. Que usen los 27 minutos para el "
                      "guion y el plan B —que son 40 de los 100 puntos— y dejen las diapositivas "
                      "para después: **sin guion, las diapositivas se hacen dos veces**. En el "
                      "ensayo, que presenten con las diapositivas a medias; lo que se corrige hoy es "
                      "el tiempo y la estructura, no el diseño."},
            {"caso": "Equipos que se pasan de tiempo en el ensayo",
             "clave": "Le va a pasar a los cinco. Córtelos exactamente a los 4 minutos, aunque sea a "
                      "mitad de frase, y **dígales dónde iban**: «a los 4 minutos usted apenas "
                      "empezaba el tramo 2, y le faltan tres tramos». Ese dato concreto convence más "
                      "que cualquier consejo. La corrección casi siempre es la misma: se presentaron "
                      "en vez de empezar por el problema, y contaron el árbol de causas completo."},
            {"caso": "Equipos con un integrante que no quiere hablar",
             "clave": "No lo fuerce a hablar más de lo mínimo, pero **no lo exima**: el tramo 5, de "
                      "un minuto, con la tarjeta de cuatro palabras clave, es perfectamente "
                      "manejable y es un logro real para quien le da pánico. Si de plano no puede, "
                      "asígnele el manejo de pantalla del tramo 3 —que es trabajo visible y "
                      "necesario— y déjelo con un cierre de treinta segundos. Lo que no funciona es "
                      "que un integrante quede sin rol: eso perjudica al equipo y a él."},
            {"caso": "Proyectos sin prototipo digital que mostrar",
             "clave": "El tramo 3 se convierte en **mostrar el formato, el procedimiento o la maqueta "
                      "en papel** con la cámara o con fotos, y funciona igual de bien. La regla no "
                      "cambia: se muestra una tarea cumpliéndose —alguien llenando el formato en "
                      "menos de X— y no se describe el documento. El plan B en este caso son las "
                      "fotos, que ya deberían estar en la carpeta desde la sesión 10."},
        ],
        "cierre": "Cinco minutos, y conviene usarlos como una lista de verificación en voz alta más "
                  "que como una reflexión: **guion con tiempos, ocho diapositivas, reparto con tarea "
                  "para quien no habla, demostración ensayada dos veces, PDF descargado y capturas en "
                  "la carpeta.** Pregunte equipo por equipo qué le falta y anótelo: eso vale más que "
                  "cualquier cierre inspirador, porque la próxima sesión tiene nota. Después, la idea "
                  "del día, dicha completa: **una presentación no se acorta hablando rápido, se "
                  "acorta eligiendo** — es la misma operación del alcance mínimo de la sesión 8, "
                  "aplicada al tiempo en vez del producto, y es una habilidad que van a usar en cada "
                  "sustentación de su carrera. Cierre con los dos datos que importan: la exposición "
                  "de la sesión 15 vale el **15 %** del curso y **se corta a los nueve minutos**; "
                  "quien no ensaye completo, hablando y con cronómetro, se va a pasar. Y recuerde que "
                  "el informe final de la sesión 16 vale el **20 %** y que casi todo su contenido ya "
                  "está escrito desde las sesiones anteriores.",
        "conexion": "Hacia atrás: la **sesión 6** dio la cifra del problema que abre el tramo 1; la "
                    "**sesión 8** dio la decisión y el sacrificio del tramo 2, y su lógica de recorte "
                    "es la misma que hoy se aplica al tiempo; la **sesión 7** dio el criterio de "
                    "aceptación que se cronometra en vivo en el tramo 3; la **sesión 11** dio el "
                    "prototipo v2; la **sesión 12** dio los hallazgos del tramo 4 y la lista de lo "
                    "que no se arregla; la **sesión 13** dio los dos números del tramo 5. Hacia "
                    "adelante: la **sesión 15** es esta misma presentación, con nota y con corte a "
                    "los nueve minutos; y el **informe final de la sesión 16** recibe todo lo que hoy "
                    "quedó fuera de la presentación — el árbol de causas, la matriz completa, los "
                    "antecedentes y la matriz de impacto entera.",
    },

    "errores": [
        {"dice": "«Buenas tardes, somos el equipo 3, integrado por…»",
         "por_que": "Consume el minuto más valioso de los nueve en información que ya está en la diapositiva 1.",
         "pida": "Arrancar con el problema y su número. Los nombres se leen en pantalla."},
        {"dice": "Una diapositiva con el texto completo de lo que se va a decir",
         "por_que": "El público lo lee más rápido de lo que usted lo dice y deja de escucharlo justo en lo importante.",
         "pida": "Rótulos de cinco palabras. El contenido lo pone la voz."},
        {"dice": "«No cabe, mejor le bajo el tamaño de la letra»",
         "por_que": "En una pantalla compartida por video todo se ve más pequeño y borroso de lo que se ve en el computador propio.",
         "pida": "Quitar contenido. Si no cabe con letra grande, es que hay dos ideas en una diapositiva."},
        {"dice": "«Aquí arriba tenemos un campo de búsqueda, y a la derecha un botón que dice buscar…»",
         "por_que": "Narrar la interfaz consume los tres minutos del tramo más importante sin mostrar nada que funcione.",
         "pida": "Mostrar una tarea cumpliéndose: alguien encontrando un libro, alguien marcando un préstamo en 14 segundos."},
        {"dice": "«El plan B lo hacemos en casa»",
         "por_que": "Es la parte más fácil de los cien puntos del día y la que se olvida siempre. En la sesión 15 ya es tarde.",
         "pida": "El PDF y las capturas en la carpeta hoy, antes de salir, y el acuerdo de quién comparte pantalla."},
    ],

    "dudas": [
        {"p": "¿Nueve minutos exactos? ¿Qué pasa si nos pasamos?",
         "r": "Se corta al llegar a cero, y hoy lo van a experimentar en el ensayo con los 4 minutos "
              "del arranque. No es rigidez por rigidez: en la sesión 15 hay cinco equipos y un "
              "bloque de 90 minutos, así que el tiempo que un equipo se pasa lo pierde el último. En "
              "la vida profesional funciona igual — en una sustentación o en una reunión de comité, "
              "el tiempo asignado es el tiempo que hay."},
        {"p": "¿Tenemos que hablar todos?",
         "r": "Sí, y entre uno y tres minutos cada uno. Hay dos razones: reparte el riesgo técnico "
              "—si uno solo presenta y se le cae la conexión, se cae la nota del equipo— y obliga a "
              "que todos entiendan el proyecto completo, porque en las preguntas **cada uno responde "
              "de su tramo**. A quien le dé pánico, el tramo 5 de un minuto con una tarjeta de "
              "cuatro palabras es perfectamente manejable."},
        {"p": "¿Podemos mostrar el prototipo en vivo o es mejor con capturas?",
         "r": "En vivo, siempre que se pueda: mostrar una tarea cumpliéndose convence mucho más que "
              "una imagen. Pero **con las capturas listas al lado**, porque si no carga hay que poder "
              "seguir sin perder los tres minutos del tramo. Es exactamente para eso el plan B, y por "
              "eso vale 15 puntos hoy."},
        {"p": "¿Y todo lo que no alcanzamos a contar?",
         "r": "Va en el **informe final de la sesión 16**, que vale el 20 %. El árbol de causas "
              "completo, la matriz de decisión con sus quince filas, los tres antecedentes, la matriz "
              "de impacto entera: todo eso es material de informe. Distinguir qué va en la "
              "presentación y qué va en el informe es una habilidad profesional, y es media hora de "
              "trabajo ganado para la próxima sesión."},
    ],

    "notas_operativas": [
        "**Reparto propio hoy:** apertura 6 · teoría 22 · taller 27 · **ensayo cronometrado 30** · "
        "cierre 5. Anúncielo en el minuto 2 y aclare que el ensayo **no tiene nota**.",
        "**Cronómetro grande y visible en pantalla compartida** durante el ensayo. Sin cronómetro "
        "visible, el ejercicio pierde la mitad del efecto.",
        "**Corte exactamente a los 4 minutos**, incluso en mitad de una frase, y diga **dónde iba el "
        "equipo**. Ese dato concreto convence más que cualquier consejo.",
        "En los 2 minutos de corrección diga **una sola cosa**. Las cuatro más frecuentes, en orden: "
        "se presentaron en vez de arrancar por el problema · leyeron la diapositiva · se pasaron en "
        "el tramo 2 · la misma persona narraba y manejaba la pantalla.",
        "**Verifique el plan B equipo por equipo antes de que termine el bloque de taller**: PDF "
        "descargado, capturas y acuerdo de quién comparte. Después ya no hay tiempo.",
        "En las salas, entre con una sola pregunta: **«¿cuánto dura su tramo 2?»**. Si no lo saben, "
        "no tienen guion.",
        "Diga que **no se empieza por las diapositivas**: sin guion, las diapositivas se hacen dos "
        "veces. Es el consejo que más tiempo les ahorra.",
        "Los equipos que observan anotan **una cosa que van a copiar y una que van a evitar**, y lo "
        "dejan en el muro **sin nombres**.",
        "Recuerde los dos pesos: exposición de la sesión 15 = **15 %**, informe final de la 16 = "
        "**20 %**.",
    ],

    "ti_siguiente": {
        "tid": "Diseño de presentación y recursos visuales — dejar terminadas las ocho diapositivas y "
               "el guion con tiempos en la carpeta del equipo, junto con el PDF y las capturas.",
        "ti": "Ensayo general: ensayar **los nueve minutos completos, hablando y con cronómetro, al "
              "menos dos veces**, y ajustar el guion con el tiempo real. Leerlo en silencio no "
              "cuenta: dura la mitad.",
        "adelanto": "es la **exposición final**, con nota: nueve minutos por equipo y tres de "
                    "preguntas. Vale el **15 %** del curso.",
        "aviso": "En la sesión 15 **se corta a los nueve minutos**, sin excepción. Conéctense cinco "
                 "minutos antes con la presentación y el prototipo ya abiertos, y con las capturas a "
                 "mano. El orden de exposición se sortea al empezar, así que todos los equipos deben "
                 "estar listos desde el primer minuto.",
    },

    "cierre_titulo": "Nos vemos en la sesión 15",
    "cierre_frase": "Una presentación no se acorta hablando rápido: se acorta eligiendo",
}


# =============================================================================
# CLASE 15 · Exposicion final de proyectos · 15 % DE LA NOTA DEL CURSO
# =============================================================================
# Reparto propio: 60 min de exposiciones (5 equipos x 12 = 9 de exposicion + 3 de
# preguntas). La teoria es minima y se proyecta en la apertura: hoy la clase la dan
# los estudiantes. El `taller` de este tema ES la exposicion calificada.

TEMAS[15] = {
    "n": 15,
    "titulo": "Exposición final de proyectos",
    "subtitulo": "Nueve minutos por equipo y tres de preguntas — hoy la clase la dan ustedes",
    "hook": "En quince sesiones pasaron de «se me ocurrió una app» a un prototipo probado con "
            "personas reales. ¿Cuál fue la decisión que más les costó tomar?",
    "hook_lines": [
        "Una línea por equipo en el muro, antes de empezar. Nada más.",
        "Esa decisión es la que hay que contar hoy: no el resultado, la decisión.",
    ],
    "objetivos": [
        "Sustentar el proyecto en **nueve minutos**, con la estructura de cinco tramos.",
        "**Mostrar el prototipo funcionando** y los hallazgos de la prueba con personas reales.",
        "Responder preguntas del curso y del docente **sobre el propio tramo**.",
        "Valorar el trabajo de los otros equipos con **criterios y no con opiniones**.",
    ],
    "agenda_slots": [
        ("Apertura y encuadre", 10, "Pregunta de entrada, sorteo del orden y reglas del día"),
        ("Exposiciones finales", 60, "5 equipos × 12 min — 9 de exposición y 3 de preguntas"),
        ("Valoración entre pares", 12, "La ficha de valoración de los otros equipos, en el muro"),
        ("Cierre", 8, "Lo que se vio hoy y qué falta para el informe final"),
    ],
    "agenda_sub": "Hoy la clase la dan los estudiantes. El docente cronometra, pregunta y califica",
    "nota_bloque": "**Se corta a los nueve minutos**, sin excepción y aunque quede una frase a "
                   "medias: con cinco equipos en 90 minutos, el tiempo que un equipo se pasa lo "
                   "pierde el último. Los **tres minutos de preguntas** también se califican, y "
                   "**cada integrante responde de su tramo**. El orden se sortea al empezar, así que "
                   "los cinco equipos tienen que estar listos desde el primer minuto.",
    "agenda": {},
    "herramienta_nota": "Cada equipo comparte su propia pantalla. **Antes de empezar, todos** dejan "
                        "en la carpeta del equipo la presentación **en PDF** y las **capturas del "
                        "prototipo** — es el plan B de la sesión 14 y hoy es el día en que sirve. La "
                        "**ficha de valoración entre pares** se llena en el muro, con una columna por "
                        "equipo. **Hoy no se usa asistente de IA.**",
    "avance_proyecto": "Exposición final sustentada y calificada (15 % del curso), y la lista de "
                       "ajustes que cada equipo se lleva para el informe final",

    "teoria": [
        {
            "tipo": "tabla",
            "titulo": "Con qué se califica hoy",
            "headers": ["Tramo de la exposición", "Qué se busca", "Pts"],
            "rows": [
                ["1 · El problema con su cifra",
                 "Arranca por el problema, no por presentaciones. Trae **un número** y de dónde salió.",
                 "20"],
                ["2 · Los afectados y la decisión",
                 "Incluye un afectado que **no es usuario** y dice **qué se sacrificó** al decidir.",
                 "20"],
                ["3 · La solución y el prototipo en vivo",
                 "**Muestra una tarea cumpliéndose**, no describe la pantalla. Cabe en 3 minutos.",
                 "25"],
                ["4 · Lo que falló y lo que aprendimos",
                 "Hallazgos con personas reales, qué se arregló y **qué se decidió no arreglar**.",
                 "20"],
                ["5 · Impacto y siguiente paso",
                 "El impacto positivo con su número **y el negativo con su mitigación**.",
                 "15"],
            ],
            "note": "Además: **se corta a los 9 minutos**, y de los cien puntos se descuentan hasta "
                    "**10 si no todos los integrantes hablan** y hasta **10 si nadie sabe responder "
                    "una pregunta de su propio tramo**. La exposición vale el **15 %** del curso.",
            "col_w": [2.9, 5.4, 0.9],
            "fs_body": 11,
        },
        {
            "tipo": "steps",
            "titulo": "El orden del día, y qué hace el equipo que no está exponiendo",
            "steps": [
                ("1 · Se sortea el orden", "Al empezar, en pantalla. **Nadie sabe si es primero**, así que los cinco equipos están listos desde el minuto uno."),
                ("2 · El equipo que expone comparte pantalla", "Un solo integrante comparte; los demás tienen la presentación en PDF abierta por si se cae."),
                ("3 · Nueve minutos, con cronómetro visible", "Se corta al llegar a cero. A los 8 minutos aparece un aviso en el chat."),
                ("4 · Tres minutos de preguntas", "Primero una pregunta del curso, después una del docente. **Responde quien tenga el tramo.**"),
                ("5 · Los que no exponen llenan la ficha", "Una fila por equipo: lo más fuerte, lo que no quedó claro y **una pregunta**. Se entrega en el muro."),
            ],
            "sub": "Escuchar también es trabajo de hoy: la ficha de valoración se califica dentro de la nota de exposiciones del corte",
        },
        {
            "tipo": "cards",
            "titulo": "Los tres minutos de preguntas también se califican",
            "cards": [
                ("Responde quien tiene el tramo",
                 "Si preguntan por la prueba con usuarios, responde quien la hizo. **No responde "
                 "siempre el mismo**: eso es lo que se está evaluando."),
                ("«No lo medimos» es una respuesta válida",
                 "Decir **«no tenemos ese dato»** vale más que inventar una cifra. Lo que hunde una "
                 "sustentación es responder con seguridad algo que no se verificó."),
                ("Responder con la decisión, no con la excusa",
                 "«No lo hicimos porque no alcanzamos» suena a excusa. **«Decidimos no hacerlo y "
                 "sacrificamos esto»** es ingeniería, y está escrito desde la sesión 8."),
                ("Corto y al grano",
                 "Tres minutos alcanzan para dos o tres preguntas si las respuestas duran treinta "
                 "segundos. Una respuesta de dos minutos se come las preguntas de los demás."),
            ],
            "columns": 2,
        },
        {
            "tipo": "box",
            "titulo": "Tres cosas antes de empezar",
            "notas": [
                ("advertencia",
                 "**El PDF y las capturas, en la carpeta, ahora.** No al final, no «después de "
                 "exponer». Si el prototipo no carga en vivo, el equipo narra el mismo recorrido "
                 "sobre las capturas y **no pierde el tramo de 25 puntos**. Es literalmente para hoy "
                 "que se preparó eso en la sesión 14."),
                ("info",
                 "**Se corta a los nueve minutos y no es rigidez por rigidez:** con cinco equipos en "
                 "90 minutos, cada minuto que un equipo se pasa lo pierde el último en exponer. En "
                 "una sustentación de grado o en un comité funciona igual — el tiempo asignado es "
                 "todo el tiempo que hay."),
                ("aclaracion",
                 "**Nada de esto termina hoy.** De cada exposición sale una lista de ajustes para el "
                 "**informe final de la sesión 16, que vale el 20 %**. Anoten lo que el curso no "
                 "entendió: eso es exactamente lo que hay que escribir mejor en el informe."),
            ],
        },
    ],

    "fundamento": [
        {
            "titulo": "Cómo se encuadra el día, y por qué el sorteo importa",
            "slide": "{{slide:Pregunta de entrada}} {{slide:El orden del día}}",
            "cuerpo": [
                "La apertura de hoy tiene una función distinta a la de las otras sesiones: no "
                "introduce un tema, **baja la ansiedad y fija las reglas**. La pregunta de entrada "
                "—«¿cuál fue la decisión que más les costó tomar?»— se responde con una línea por "
                "equipo en el muro y sirve para dos cosas: los pone a hablar antes de exponer, y les "
                "recuerda que **lo que se califica es la decisión, no el resultado**. Muchos equipos "
                "llegan creyendo que van a ser juzgados por si su prototipo es bonito.",
                "**El sorteo del orden se hace en vivo y en pantalla.** No es teatro: si el orden se "
                "anuncia antes, los últimos equipos siguen preparando durante las primeras "
                "exposiciones y no escuchan. Sorteado al empezar, los cinco equipos tienen que estar "
                "listos desde el primer minuto y todos escuchan a todos. Dígalo así.",
                "Antes de la primera exposición, **verifique en voz alta el plan B de los cinco "
                "equipos**: PDF descargado y capturas en la carpeta. Toma dos minutos y cada semestre "
                "salva al menos un equipo. Un equipo que no lo tenga y cuyo prototipo no cargue "
                "pierde el tramo de 25 puntos por algo que se prevenía en cinco minutos.",
                "Sobre el rol de quien no expone, hay que ser explícito porque de lo contrario nadie "
                "escucha: **la ficha de valoración entre pares se califica**, dentro de la nota de "
                "exposiciones del corte. Una fila por equipo con lo más fuerte, lo que no quedó claro "
                "y una pregunta. Y la ficha tiene un beneficio para quien la llena: obliga a "
                "comparar el proyecto propio con cuatro más, que es la manera más rápida de ver los "
                "vacíos del propio informe.",
            ],
        },
        {
            "titulo": "Cómo se califica cada tramo, sin discutir con el reloj",
            "slide": "{{slide:Con qué se califica hoy}}",
            "cuerpo": [
                "La rúbrica se proyecta al empezar y hay que dejarla visible: calificar con criterios "
                "publicados evita la discusión posterior y, sobre todo, **le dice al que expone qué "
                "es lo importante**. Los pesos no son arbitrarios — el tramo 3 vale más porque es la "
                "evidencia de que hicieron algo, y el tramo 4 vale 20 porque es lo que distingue un "
                "proyecto de una idea.",
                "**Califique mientras escucha, no después.** Con cinco equipos seguidos, la memoria "
                "mezcla las exposiciones y termina premiando al último. Tenga la tabla de cinco "
                "tramos por equipo abierta y anote el puntaje al terminar cada tramo, más una frase "
                "de por qué. Esa frase es lo que después se devuelve como retroalimentación.",
                "**Los dos descuentos hay que aplicarlos, y anunciarlos antes.** Hasta 10 puntos si "
                "no todos los integrantes hablan —porque la exposición en equipo es lo que se está "
                "evaluando— y hasta 10 si nadie sabe responder una pregunta de su propio tramo. El "
                "segundo descuento es el que más enseña: destapa al equipo donde uno solo hizo el "
                "trabajo y los demás leyeron un guion.",
                "**Sobre el corte a los nueve minutos:** avise en el chat a los 8, y corte a los 9 "
                "aunque quede una frase a medias. Es incómodo la primera vez y después el curso lo "
                "acepta como parte del juego. El argumento, si alguien reclama, es aritmético y no "
                "disciplinario: cinco equipos por 12 minutos son 60, y el tiempo que un equipo se "
                "pasa lo pierde el último. **No descuente puntos adicionales por pasarse**: el corte "
                "ya es el castigo, porque los tramos que faltaban valen cero.",
                "Un criterio de calificación que conviene tener claro de antemano: **un equipo que "
                "cuenta un fracaso con honestidad saca más que uno que presenta todo perfecto.** No "
                "es generosidad: en un prototipo de primer semestre, «todo funcionó a la primera» "
                "significa casi siempre que no se probó con nadie. Si un equipo no reporta ningún "
                "hallazgo en el tramo 4, la pregunta obligatoria es **«¿con quién lo probaron y qué "
                "hizo esa persona?»**.",
            ],
        },
        {
            "titulo": "Las preguntas: los tres minutos que destapan el trabajo real",
            "slide": "{{slide:Los tres minutos de preguntas}}",
            "cuerpo": [
                "Los tres minutos de preguntas no son un trámite: son la parte de la sesión donde se "
                "ve quién entendió el proyecto. Por eso la regla es **responde quien tiene el tramo**, "
                "y hay que hacerla cumplir con firmeza —si el mismo integrante responde todo, "
                "redirija: «esa es del tramo 4, ¿quién lo presentó?»—.",
                "Enseñe explícitamente que **«no lo medimos» es una respuesta válida y buena**. Un "
                "estudiante de primer semestre cree que no saber es un fracaso, y por eso inventa "
                "cifras. Hay que decirle lo contrario: lo que hunde una sustentación es afirmar con "
                "seguridad algo que no se verificó, porque una sola cifra inventada vuelve dudoso "
                "todo lo demás. Es la misma lección de la sesión 5 sobre datos con fuente y de la 11 "
                "sobre la IA que **inventa con seguridad**.",
                "La segunda enseñanza es la diferencia entre excusa y decisión. «No lo hicimos porque "
                "no nos alcanzó el tiempo» suena a incumplimiento; **«decidimos no hacerlo y "
                "sacrificamos esto a cambio»** es exactamente el lenguaje del alcance mínimo de la "
                "sesión 8. Los equipos ya tienen la decisión escrita desde entonces: solo hay que "
                "recordarles que la usen.",
                "**Reserve una pregunta suya para cada equipo, y hágala útil.** Las tres que más "
                "rinden: «¿con quién lo probaron y qué hizo esa persona?» —destapa si hubo prueba "
                "real—, «¿qué pasa con alguien que no tiene datos móviles?» —destapa si pensaron en "
                "los afectados no usuarios— y «si tuvieran una semana más, ¿qué harían primero?» "
                "—destapa si tienen criterio de prioridad o solo una lista de deseos—.",
                "Cuide el tiempo de las respuestas: tres minutos alcanzan para dos o tres preguntas "
                "**si las respuestas duran treinta segundos**. Una respuesta de dos minutos se come "
                "las preguntas de los demás, y hay que interrumpirla con cortesía.",
            ],
        },
        {
            "titulo": "El cierre: qué hacer con lo que salió hoy",
            "slide": "{{slide:Tres cosas antes de empezar}}",
            "cuerpo": [
                "Los ocho minutos de cierre no son para felicitar. Son para **convertir las cinco "
                "exposiciones en trabajo concreto para el informe final**, que se entrega la próxima "
                "sesión y vale el 20 %.",
                "La instrucción operativa para cada equipo es una: **anoten lo que el curso no "
                "entendió de su proyecto, porque eso es exactamente lo que hay que escribir mejor en "
                "el informe.** Si tres personas preguntaron cómo se actualiza la lista, la sección de "
                "la solución no está clara. Una pregunta repetida es un diagnóstico gratis.",
                "Devuelva **una observación por equipo, dicha en público y en una frase** —lo que más "
                "sumó y la única cosa que cambiaría—. La retroalimentación detallada va después, por "
                "escrito, con las frases que anotó mientras calificaba. En público, una sola cosa: es "
                "la misma regla de la sesión 12 sobre retroalimentación útil.",
                "Y cierre nombrando lo que efectivamente pasó, sin discurso: hace quince sesiones "
                "estos equipos tenían una ocurrencia; hoy sustentaron un problema con evidencia, una "
                "decisión con criterios, un prototipo probado con personas reales y un impacto con "
                "sus costos. **Eso es el ciclo completo de un proyecto de ingeniería**, y lo hicieron "
                "en primer semestre. Vale decirlo una vez, en serio y corto.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:10 · Apertura y encuadre · [Slide 4]…[Slide 8]",
            "cuerpo": [
                "Comparta pantalla antes de que entre el primero:",
                "> «En quince sesiones pasaron de «se me ocurrió una app» a un prototipo probado con "
                "personas reales. ¿Cuál fue la decisión que más les costó tomar?»",
                "Una línea por equipo en el muro. Sirve para bajar la ansiedad y para recordar que "
                "**se califica la decisión, no el resultado**.",
                "- **2 min** · La rúbrica en pantalla [Slide 5]. Anuncie los dos descuentos: **todos "
                "hablan** y **cada uno responde de su tramo**.",
                "- **2 min** · El orden del día [Slide 6] y **el sorteo en vivo**. Nadie sabe si es "
                "primero.",
                "- **1 min** · Las preguntas [Slide 7]. Diga que **«no lo medimos» es respuesta "
                "válida**.",
                "- **2 min** · [Slide 8] **Verifique el plan B de los cinco equipos**: PDF y capturas "
                "en la carpeta. Ahora, no después.",
                "**[Nota docente]:** el sorteo se hace ahora y no antes, para que los últimos equipos "
                "escuchen en vez de seguir preparando.",
            ],
        },
        {
            "titulo": "00:10–01:10 · Exposiciones finales (60 min) · [Slide 9][Slide 10]",
            "cuerpo": [
                "5 equipos × 12 min: **9 de exposición y 3 de preguntas**. Cronómetro grande en "
                "pantalla compartida, aviso en el chat a los 8 minutos, corte a los 9.",
                "**[Nota docente]:** califique **mientras escucha**, tramo por tramo, con una frase de "
                "por qué. Si califica al final, la memoria mezcla las cinco exposiciones y premia al "
                "último.",
                "**[Nota docente]:** reserve **una pregunta suya por equipo**. Las tres que más "
                "rinden: «¿con quién lo probaron y qué hizo esa persona?» · «¿qué pasa con alguien "
                "que no tiene datos móviles?» · «si tuvieran una semana más, ¿qué harían primero?».",
                "**[Nota docente]:** si el mismo integrante responde todo, redirija: «esa es del "
                "tramo 4, ¿quién lo presentó?». Ese es el descuento que más enseña.",
                "**[Nota docente]:** si un equipo no reporta **ningún** hallazgo en el tramo 4, la "
                "pregunta obligatoria es «¿con quién lo probaron y qué hizo esa persona?».",
                "**[Nota docente]:** si a un equipo no le carga el prototipo, dígale de inmediato "
                "**«usen las capturas»** y no le descuente el tiempo perdido buscando.",
            ],
        },
        {
            "titulo": "01:10–01:22 · Valoración entre pares (12 min)",
            "cuerpo": [
                "Cada equipo completa en el muro, en la columna de los **otros cuatro** equipos: lo "
                "más fuerte · lo que no quedó claro · una pregunta que se queda sin responder.",
                "**[Nota docente]:** recuerde las reglas de la sesión 12 — **observación, no "
                "adjetivo; una sola cosa; no rediseñar el proyecto ajeno**. «Estuvo bien» no cuenta "
                "como valoración.",
                "**[Nota docente]:** esta ficha **se califica** dentro de la nota de exposiciones del "
                "corte. Dígalo antes de que empiecen a llenarla, no después.",
                "Lea en voz alta **dos o tres observaciones anónimas** que sean buenas. Enseña más "
                "sobre cómo se da retroalimentación que cualquier explicación.",
            ],
        },
        {
            "titulo": "01:22–01:30 · Cierre · [Slide 11][Slide 12]",
            "cuerpo": [
                "**Una observación por equipo, en una frase**: lo que más sumó y la única cosa que "
                "cambiaría. La retroalimentación detallada va después, por escrito.",
                "La instrucción que convierte hoy en trabajo: **anoten lo que el curso no entendió de "
                "su proyecto — eso es lo que hay que escribir mejor en el informe.** Una pregunta "
                "repetida es un diagnóstico gratis.",
                "Recuerde: el **informe final de la sesión 16 vale el 20 %**, y **once de sus doce "
                "secciones ya están escritas** desde las sesiones anteriores.",
                "Y dígalo una vez, corto y en serio: hace quince sesiones tenían una ocurrencia; hoy "
                "sustentaron un problema con evidencia, una decisión con criterios, un prototipo "
                "probado y un impacto con sus costos. **Eso es un proyecto de ingeniería completo.**",
            ],
        },
    ],

    "taller": {
        "archivo": "Guia de la exposicion final",
        "titulo": "Exposición final del proyecto",
        "min": 60,
        "exposicion": 9,
        "consigna": "Sustenten el proyecto en **nueve minutos**, con los cinco tramos de la sesión "
                    "14, **mostrando el prototipo funcionando** y los hallazgos de la prueba con "
                    "personas reales. Después, **tres minutos de preguntas**: responde quien tiene el "
                    "tramo. Vale el **15 %** del curso.",
        "entregable": "la exposición sustentada, y la ficha de valoración de los otros cuatro equipos "
                      "en el muro",
        "entregable_corto": "exposición de 9 min + ficha de valoración de los otros equipos",
        "reparto_titulo": "Los nueve minutos, tramo por tramo:",
        "reparto": "1 min el problema con su cifra · 2 min los afectados y la decisión · 3 min la "
                   "solución y el prototipo en vivo · 2 min lo que falló y lo que aprendimos · 1 min "
                   "impacto y siguiente paso. **Se corta a los nueve minutos.**",
        "reparto_corto": "9 min de exposición + 3 de preguntas, por equipo",
        "bloques": [
            {"clave": "EL PROBLEMA CON SU CIFRA",
             "pide": "Una frase y **un número**, con de dónde salió. **Sin saludos ni presentaciones "
                     "personales**: el nombre del equipo está en la diapositiva.",
             "check": "arrancó por el problema y trajo un dato propio, no una cifra genérica de internet."},
            {"clave": "LOS AFECTADOS Y LA DECISIÓN",
             "pide": "Quiénes son los afectados —**incluido uno que no es usuario**— y qué "
                     "alternativa se eligió, **diciendo qué se sacrificó**.",
             "check": "nombró un afectado que no usa la solución y dijo en voz alta qué se perdió al decidir."},
            {"clave": "LA SOLUCIÓN Y EL PROTOTIPO EN VIVO",
             "pide": "Un recorrido de **tres pasos** mostrando **una tarea cumpliéndose**. Narra una "
                     "persona y maneja la pantalla otra.",
             "check": "mostró en vez de describir, cupo en 3 minutos, y narrador y operador fueron distintos."},
            {"clave": "LO QUE FALLÓ Y LO QUE APRENDIMOS",
             "pide": "Los hallazgos con personas reales, qué se arregló y **qué se decidió no "
                     "arreglar**, con el motivo.",
             "check": "hay al menos un hallazgo concreto de una persona ajena al equipo, y una limitación declarada."},
            {"clave": "IMPACTO Y SIGUIENTE PASO",
             "pide": "El impacto positivo **con su número** y el negativo **con su mitigación**. Qué "
                     "haría quien continúe el proyecto.",
             "check": "el impacto negativo aparece con el mismo peso que el positivo, y hay un siguiente paso concreto."},
        ],
        "expo": [
            ("Tramo 1 · 1 min", "El problema con su cifra. Arranca sin saludos."),
            ("Tramo 2 · 2 min", "Los afectados —uno que no es usuario— y la decisión con su sacrificio."),
            ("Tramo 3 · 3 min", "El prototipo en vivo: tres pasos, una tarea cumpliéndose."),
            ("Tramo 4 · 2 min", "Los hallazgos de la prueba, lo que se arregló y lo que no."),
            ("Tramo 5 · 1 min", "Impacto positivo con su número, negativo con su mitigación, siguiente paso."),
            ("Preguntas · 3 min", "Una del curso y una del docente. **Responde quien tiene el tramo.**"),
        ],
    },

    "rubrica": [
        ("Tramo 1 · El problema con su cifra, sin gastar el minuto en presentaciones", 20,
         "Un problema con un dato propio es lo que separa un proyecto de una ocurrencia, y es lo primero que se juzga."),
        ("Tramo 2 · Los afectados, incluido uno que no es usuario, y la decisión con su sacrificio", 20,
         "Decir qué se sacrificó en diez segundos comunica más madurez técnica que cinco minutos de descripción."),
        ("Tramo 3 · El prototipo mostrado funcionando, en tres minutos, narrando una tarea", 25,
         "Es la evidencia de que el equipo construyó algo; describir la interfaz consume el tramo sin mostrar nada."),
        ("Tramo 4 · Hallazgos con personas reales, lo arreglado y lo que se decidió no arreglar", 20,
         "Un prototipo que «funcionó a la primera» casi siempre significa que no se probó con nadie."),
        ("Tramo 5 · Impacto positivo con número y negativo con mitigación, más siguiente paso", 15,
         "Poner el costo al lado del beneficio es la señal de honestidad que hace creíble todo lo anterior."),
    ],

    "solucion": {
        "para_que": "Este documento es la **guía de calificación** de la sesión: la planilla por "
                    "tramo, qué distingue un 20 de un 12 en cada uno, las preguntas que conviene "
                    "reservar para cada equipo y la ficha de valoración entre pares. Si solo alcanza "
                    "a leer un bloque antes de clase, que sea **LA SOLUCIÓN Y EL PROTOTIPO EN VIVO**: "
                    "es el tramo de más puntos y el que más se cae.",
        "caso_titulo": "Cómo calificar cinco exposiciones seguidas sin perder el criterio",
        "caso": "Cinco equipos, 12 minutos cada uno, 60 minutos corridos. El riesgo real no es que "
                "los equipos expongan mal: es que el docente califique el primero con un criterio y "
                "el quinto con otro. Todo lo que sigue está armado para evitar eso.",
        "por_que_este_caso": "Porque calificar de memoria al final de los 60 minutos premia "
                            "sistemáticamente al último equipo que se escuchó. Con la planilla "
                            "abierta y un puntaje anotado al terminar cada tramo, la calificación es "
                            "comparable entre los cinco y la retroalimentación sale escrita sin "
                            "trabajo extra.",
        "bloques": [
            {
                "clave": "EL PROBLEMA CON SU CIFRA",
                "respuesta": "**Qué se oye en un tramo de 20 puntos** (ejemplo real del caso de la "
                             "biblioteca):\n\n"
                             "> «De cada diez personas que van a la biblioteca del barrio, **cuatro "
                             "se devuelven sin el libro**. Contamos durante dos semanas en la puerta: "
                             "38 de 94 visitas. Veinticinco minutos de camino y un pasaje, para nada.»\n\n"
                             "Dieciocho segundos, un número, y **de dónde salió el número**.\n\n"
                             "| Puntaje | Qué se oyó |\n"
                             "|---|---|\n"
                             "| **18–20** | Arranca por el problema, con un dato propio y su fuente. Se entiende a quién le pasa. |\n"
                             "| **14–17** | Arranca por el problema y hay una cifra, pero no se dice de dónde salió. |\n"
                             "| **10–13** | Hay saludo y presentación de integrantes antes del problema, o la cifra es genérica de internet. |\n"
                             "| **5–9** | El problema se enuncia como categoría («el problema de la desorganización») y sin ningún dato. |\n"
                             "| **0–4** | No queda claro qué problema resuelve el proyecto. |\n\n"
                             "**El error más común, y hay que anotarlo sin dramatismo:** gastar el "
                             "minuto en «buenas tardes, somos el equipo 3, integrado por…». Se avisó "
                             "en la sesión 14 y aun así lo hacen dos o tres equipos. Cuesta puntos "
                             "porque consume el minuto más valioso en información que ya está en la "
                             "diapositiva.\n\n"
                             "**La pregunta útil si el tramo queda flojo:** «¿ese 40 % de dónde salió?». "
                             "Si la respuesta es «lo leímos en un artículo», el dato no es del "
                             "proyecto. Si es «lo contamos nosotros», súbale el puntaje.",
                "como_calificar": "20 pts. Dos cosas se verifican en veinte segundos: **¿arrancó por "
                                  "el problema?** y **¿el número es del equipo o de internet?**. La "
                                  "cifra propia —aunque sea un conteo de dos semanas en una puerta— "
                                  "vale más que una estadística nacional bien citada, porque "
                                  "demuestra trabajo de campo. Anote la frase textual del arranque: "
                                  "sirve para la retroalimentación y para comparar entre equipos."
            },
            {
                "clave": "LOS AFECTADOS Y LA DECISIÓN",
                "respuesta": "**Las dos cosas que este tramo tiene que contener**, y que casi nadie "
                             "junta bien:\n\n"
                             "1. **Un afectado que no es usuario.** En el caso de la biblioteca: la "
                             "voluntaria del cierre, a quien le llega trabajo nuevo, y el vecino sin "
                             "datos móviles, que queda atrás en el mostrador. Salió de la sesión 13.\n"
                             "2. **La decisión con su sacrificio.** «Ganó la lista publicada una vez "
                             "al día, **y perdimos la información al minuto**. Aceptamos eso porque "
                             "la alternativa exigía un computador en el mostrador, que no existe.»\n\n"
                             "| Puntaje | Qué se oyó |\n"
                             "|---|---|\n"
                             "| **18–20** | Hay un afectado no usuario **y** la decisión dice explícitamente qué se sacrificó. |\n"
                             "| **14–17** | Están los dos elementos, pero el sacrificio se menciona de pasada o suena a excusa. |\n"
                             "| **10–13** | Solo hay usuarios (nadie afectado indirecto), o la decisión se cuenta sin alternativas. |\n"
                             "| **5–9** | Se enumeran actores sin decir qué le pasa a cada uno, y no hay decisión: hay descripción. |\n"
                             "| **0–4** | No hay actores ni decisión: se pasa del problema a la solución. |\n\n"
                             "**Los diez segundos que valen más de toda la exposición:** decir qué se "
                             "sacrificó. Es el momento de mayor madurez técnica y casi ningún equipo "
                             "lo hace espontáneamente. Cuando un equipo lo dice, vale la pena "
                             "señalarlo en el cierre para que el curso entero lo oiga.\n\n"
                             "**La pregunta útil:** «¿qué pasa con alguien que no tiene datos "
                             "móviles?» — destapa en diez segundos si el equipo pensó en los "
                             "afectados no usuarios de la sesión 13 o solo en su usuario ideal.",
                "como_calificar": "20 pts: 10 por el afectado no usuario, 10 por la decisión con su "
                                  "sacrificio. La distinción que importa al calificar: **«no lo "
                                  "hicimos porque no alcanzamos» no es un sacrificio, es una "
                                  "excusa**; «decidimos no hacerlo y perdimos esto a cambio» sí lo "
                                  "es. Los equipos tienen la decisión escrita desde la sesión 8: si "
                                  "no la usan, es que no la releyeron, y conviene decírselo así."
            },
            {
                "clave": "LA SOLUCIÓN Y EL PROTOTIPO EN VIVO",
                "respuesta": "**El tramo de más puntos y el que más se cae.** Lo que se busca es un "
                             "recorrido de tres pasos donde **se ve una tarea cumpliéndose**:\n\n"
                             "- buscar un libro que está disponible, y ver **la fecha del dato**;\n"
                             "- buscar uno prestado, y ver que el estado **ya no parece un botón** "
                             "(hallazgo de la sesión 12);\n"
                             "- la pantalla de la voluntaria marcando un préstamo, **cronometrado en "
                             "vivo: catorce segundos** contra un criterio de aceptación de treinta, "
                             "definido en la sesión 7.\n\n"
                             "Ese cronometraje en vivo es el momento más convincente que puede tener "
                             "una exposición de este curso, porque el público ve **cumplirse un "
                             "criterio que se escribió ocho sesiones antes**.\n\n"
                             "| Puntaje | Qué se oyó |\n"
                             "|---|---|\n"
                             "| **22–25** | Muestra tareas cumpliéndose, cabe en 3 min, narrador y operador distintos, y conecta con un criterio de aceptación. |\n"
                             "| **18–21** | Muestra el prototipo funcionando pero sin conectarlo con los criterios, o una sola persona narra y opera. |\n"
                             "| **13–17** | Narra la interfaz botón por botón («aquí arriba tenemos un campo de búsqueda…») y se pasa de tiempo. |\n"
                             "| **8–12** | Muestra solo capturas estáticas **teniendo** el prototipo funcionando, o describe sin mostrar. |\n"
                             "| **0–7** | No hay prototipo que mostrar, ni capturas, ni maqueta. |\n\n"
                             "**Importante y hay que ser justo aquí:** un equipo que muestra el "
                             "recorrido **sobre las capturas del plan B porque el prototipo no cargó** "
                             "**no pierde puntos** si narra la tarea igual. Para eso se preparó el "
                             "plan B en la sesión 14, y usarlo bien es competencia, no fracaso. Lo "
                             "que sí cuesta puntos es no tener capturas y perder dos minutos "
                             "buscando la pestaña.\n\n"
                             "**El error a cazar:** narrar la interfaz en vez de mostrar una tarea. "
                             "La corrección cabe en una frase y conviene decirla en el cierre: **«no "
                             "describa la pantalla, muestre a alguien logrando algo».**\n\n"
                             "**La pregunta útil:** «¿cuánto se demora la voluntaria en marcar un "
                             "préstamo?». Si el equipo tiene el número, tiene criterio de "
                             "aceptación; si dice «rapidito», no lo midió.",
                "como_calificar": "25 pts. Cronométrelo, no lo estime: si el recorrido pasa de 3:30, "
                                  "el equipo se va a pasar del total de nueve. Verifique tres cosas: "
                                  "**muestra tareas o describe la pantalla** · **cabe en 3 minutos** "
                                  "· **narrador y operador son personas distintas**. Y no castigue el "
                                  "uso del plan B: un equipo que narra su recorrido sobre las "
                                  "capturas porque se cayó la conexión hizo exactamente lo que se le "
                                  "pidió."
            },
            {
                "clave": "LO QUE FALLÓ Y LO QUE APRENDIMOS",
                "respuesta": "**El tramo que todos quieren saltarse y el que más distingue.** Lo que "
                             "se busca:\n\n"
                             "> «Le dimos el prototipo a dos personas ajenas al equipo y no les "
                             "explicamos nada. **Las dos tocaron el estado «Prestado» esperando que "
                             "se abriera algo.** Y una señora escribió «100 años» en vez de «cien "
                             "años», no encontró nada y abandonó.»\n\n"
                             "Y después las dos mitades que completan el tramo: **qué se arregló** "
                             "—el estado dejó de parecer un botón, el rótulo de la fecha se "
                             "reescribió— y **qué se decidió no arreglar** —la búsqueda tolerante a "
                             "errores de escritura excede lo que el equipo puede construir este "
                             "semestre, y queda declarada como limitación conocida—.\n\n"
                             "| Puntaje | Qué se oyó |\n"
                             "|---|---|\n"
                             "| **18–20** | Hallazgos concretos de personas ajenas, con lo que hizo la persona; lo arreglado **y** lo que se decidió no arreglar con su motivo. |\n"
                             "| **14–17** | Hay hallazgos reales y arreglos, pero no hay ninguna limitación declarada: todo quedó «resuelto». |\n"
                             "| **10–13** | La prueba la hicieron entre integrantes del equipo, o los hallazgos son opiniones («dijeron que estaba bonito»). |\n"
                             "| **5–9** | Se cuenta lo que la persona **dijo** y no lo que **hizo**; sin ningún cambio derivado. |\n"
                             "| **0–4** | «Todo funcionó bien.» No hubo prueba. |\n\n"
                             "**Criterio de calificación que conviene tener decidido de antemano: un "
                             "equipo que cuenta un fracaso con honestidad saca más que uno que "
                             "presenta todo perfecto.** No es generosidad. En un prototipo de primer "
                             "semestre, «funcionó a la primera» significa casi siempre que no se "
                             "probó con nadie, y un evaluador técnico desconfía de inmediato.\n\n"
                             "**La pregunta obligatoria si el equipo no reporta ningún hallazgo:** "
                             "**«¿con quién lo probaron y qué hizo esa persona?»**. La respuesta "
                             "define el puntaje del tramo en quince segundos: si la persona es del "
                             "equipo, no fue una prueba; si la respuesta es «le pareció bien», "
                             "escucharon opiniones en vez de observar comportamiento —la distinción "
                             "de la sesión 12—.",
                "como_calificar": "20 pts: 8 por hallazgos concretos de **personas ajenas** y "
                                  "descritos como comportamiento, 7 por los cambios derivados, 5 por "
                                  "**al menos una limitación declarada con su motivo**. El puntaje "
                                  "máximo requiere las tres partes. Y valore alto la honestidad: es "
                                  "el criterio que hay que hacer explícito en el cierre para que el "
                                  "curso lo entienda de cara al informe final."
            },
            {
                "clave": "IMPACTO Y SIGUIENTE PASO",
                "respuesta": "**Sesenta segundos con tres cosas dentro.** Lo que se busca:\n\n"
                             "> «Si la mitad de esos viajes fallidos se evitan, son **30 viajes menos "
                             "al mes**. Pero hay un costo: **la voluntaria del cierre trabaja diez "
                             "minutos más cada día**, y **una de cada cinco personas no tiene datos "
                             "para consultar**. Por eso propusimos una cartelera impresa en la "
                             "puerta, una hoja por semana. El siguiente equipo debería empezar por "
                             "la búsqueda tolerante a errores.»\n\n"
                             "| Puntaje | Qué se oyó |\n"
                             "|---|---|\n"
                             "| **14–15** | Impacto positivo con número, negativo con mitigación, y un siguiente paso concreto. |\n"
                             "| **11–13** | Están el positivo y el negativo, pero el negativo no tiene mitigación, o falta el siguiente paso. |\n"
                             "| **7–10** | Solo impactos positivos, con números. Ningún costo reconocido. |\n"
                             "| **4–6** | Impacto en adjetivos: «mejora la calidad de vida», «genera conciencia». Sin ningún número. |\n"
                             "| **0–3** | No hay tramo de impacto: la exposición termina en el prototipo. |\n\n"
                             "**La señal que hay que premiar:** que el número negativo aparezca con "
                             "**el mismo peso** que el positivo. Un equipo que dice «y esto le cuesta "
                             "diez minutos diarios a una persona» está haciendo ingeniería, no "
                             "publicidad. Es exactamente lo que se trabajó en la sesión 13, y el "
                             "tramo existe para verificar que quedó.\n\n"
                             "**El error frecuente:** volver al adjetivo. «Genera conciencia "
                             "ambiental» no es un impacto: es una intención. La corrección es la de "
                             "la sesión 13 — **un impacto se declara con un indicador que alguien más "
                             "podría ir a verificar**.\n\n"
                             "**La pregunta útil:** «si tuvieran una semana más, ¿qué harían "
                             "primero?». Destapa si el equipo tiene criterio de prioridad o solo una "
                             "lista de deseos, y se responde en veinte segundos.",
                "como_calificar": "15 pts: 6 por el positivo con indicador verificable, 6 por el "
                                  "negativo **con mitigación**, 3 por el siguiente paso. Si todos los "
                                  "impactos son positivos, el máximo es 10, y la razón hay que "
                                  "decirla: toda solución le cambia algo a alguien que no la pidió. "
                                  "Rechace los adjetivos sin número — con la corrección de la sesión "
                                  "13 en la mano, no como opinión del docente."
            },
        ],
        "variantes": [
            {"caso": "Un equipo se pasa de los nueve minutos",
             "clave": "Corte, aunque quede una frase a medias. **No descuente puntos adicionales por "
                      "pasarse**: el corte ya es el castigo, porque los tramos que faltaban valen "
                      "cero y ahí está la pérdida real. Si le cortó el tramo 5, califique 0 ese tramo "
                      "y dígalo con el dato: «se pasó en el tramo 2 y perdió los 15 puntos del "
                      "impacto». Si reclaman, el argumento es aritmético: cinco equipos por 12 "
                      "minutos son 60, y el tiempo que uno se pasa lo pierde el último."},
            {"caso": "Falta un integrante el día de la exposición",
             "clave": "El equipo aplica el orden de emergencia que decidió en la sesión 14: los "
                      "tramos del ausente los asume quien sigue en la tabla de reparto. **No "
                      "descuente al equipo por la ausencia**, pero sí evalúe la exposición completa "
                      "—si faltan tramos, faltan puntos—. Al ausente se le califica aparte, con una "
                      "sustentación individual corta en la sesión 16 o en horario de asesoría; no "
                      "hereda la nota del equipo sin haber hablado."},
            {"caso": "Al equipo no le carga el prototipo en vivo",
             "clave": "Dígale de inmediato **«usen las capturas»** y no le descuente el tiempo "
                      "perdido buscando. Si narra el recorrido sobre las capturas y se entiende la "
                      "tarea, **el tramo vale completo**: usar el plan B es competencia, no fracaso, "
                      "y así se anunció en la sesión 14. Lo que sí cuesta puntos es no tener "
                      "capturas — y eso se verificó al empezar la clase, así que no debería pasar."},
            {"caso": "Un equipo presenta un proyecto claramente más débil que los otros",
             "clave": "Califique con la misma rúbrica, sin ajustar el criterio por comparación — es "
                      "justamente lo que la planilla previene. Pero en la retroalimentación pública "
                      "busque lo que sí hicieron bien, que casi siempre existe: un hallazgo de la "
                      "prueba, un afectado bien identificado. Y en la privada, sea concreto sobre "
                      "qué falta, porque **el informe final de la sesión 16 vale 20 % y todavía se "
                      "puede recuperar mucho ahí**."},
            {"caso": "Nadie del curso pregunta nada",
             "clave": "Pasa, sobre todo con el primer equipo. Tenga dos preguntas propias listas por "
                      "equipo y úselas sin esperar. Después de la segunda exposición, cambie la "
                      "mecánica: **asigne** a un equipo la tarea de preguntarle a otro —«equipo 3, "
                      "una pregunta para el 1»—. Con la ficha de valoración pidiendo «una pregunta "
                      "que se queda sin responder», ya tienen algo escrito de dónde sacarla."},
        ],
        "cierre": "Ocho minutos, y no son para felicitar: son para **convertir cinco exposiciones en "
                  "trabajo concreto para el informe final**. Devuelva **una observación por equipo, "
                  "en una frase** —lo que más sumó y la única cosa que cambiaría—; la "
                  "retroalimentación detallada va después por escrito, con las frases que anotó "
                  "mientras calificaba. Después dé la instrucción que hace útil el día: **anoten lo "
                  "que el curso no entendió de su proyecto, porque eso es exactamente lo que hay que "
                  "escribir mejor en el informe.** Si tres personas preguntaron lo mismo, esa sección "
                  "no está clara — una pregunta repetida es un diagnóstico gratis. Recuerde que el "
                  "informe final vale el **20 %** y que **once de sus doce secciones ya están "
                  "escritas** desde las sesiones anteriores: la próxima sesión es de armar y revisar, "
                  "no de empezar. Y cierre nombrando lo que pasó, una vez, corto y en serio: hace "
                  "quince sesiones estos equipos tenían una ocurrencia; hoy sustentaron un problema "
                  "con evidencia, una decisión con criterios, un prototipo probado con personas "
                  "reales y un impacto con sus costos reconocidos. **Ese es el ciclo completo de un "
                  "proyecto de ingeniería, y lo hicieron en primer semestre.**",
        "conexion": "Hacia atrás, esta sesión cobra todo el curso: la cifra del tramo 1 viene de la "
                    "**sesión 6**; los afectados no usuarios del tramo 2, de la **13**, y su mapa "
                    "inicial de la **3**; el sacrificio de la decisión, de la **8**; el criterio de "
                    "aceptación que se cronometra en el tramo 3, de la **7**; el prototipo, de las "
                    "**10 y 11**; los hallazgos y las limitaciones del tramo 4, de la **12**; los dos "
                    "números del tramo 5, de la **13**; la estructura, el reparto y el plan B, de la "
                    "**14**; y las reglas de la valoración entre pares, de la **12**. Hacia adelante: "
                    "el **informe final de la sesión 16** recibe todo lo que no cupo en nueve "
                    "minutos, y las preguntas que hoy quedaron sin responder son su lista de tareas.",
    },

    "errores": [
        {"dice": "«Buenas tardes, somos el equipo 3, integrado por…»",
         "por_que": "Gasta el minuto más valioso de los nueve en información que ya está en la primera diapositiva.",
         "pida": "Arrancar con el problema y su número. Se avisó en la sesión 14 y cuesta puntos."},
        {"dice": "«Aquí arriba tenemos un campo de búsqueda, y a la derecha un botón…»",
         "por_que": "Narrar la interfaz consume los tres minutos del tramo de más puntos sin mostrar nada funcionando.",
         "pida": "No describa la pantalla: muestre a alguien logrando algo, y cronometre si hay criterio de aceptación."},
        {"dice": "«Todo funcionó bien, no tuvimos problemas»",
         "por_que": "En un prototipo de primer semestre significa casi siempre que no se probó con nadie ajeno al equipo.",
         "pida": "Un hallazgo concreto de una persona real y una limitación declarada. La honestidad sube la nota, no la baja."},
        {"dice": "«Nuestro proyecto genera conciencia y mejora la calidad de vida»",
         "por_que": "Es una intención, no un impacto: nadie puede ir a verificarlo. Se corrigió en la sesión 13.",
         "pida": "Un indicador que alguien más podría medir, y el impacto negativo con su mitigación."},
        {"dice": "Un solo integrante responde las tres preguntas",
         "por_que": "Destapa que uno hizo el trabajo y los demás leyeron un guion. Es un descuento anunciado de hasta 10 puntos.",
         "pida": "Que responda quien tuvo el tramo. Si preguntan por la prueba, responde quien la hizo."},
    ],

    "dudas": [
        {"p": "¿De verdad nos cortan a los nueve minutos?",
         "r": "Sí, y aunque quede una frase a medias. No es rigidez por rigidez: cinco equipos por 12 "
              "minutos son 60, y el minuto que un equipo se pasa lo pierde el último en exponer. "
              "Tampoco hay descuento adicional por pasarse — el castigo es que los tramos que "
              "quedaron fuera valen cero, y suelen ser el 4 y el 5, que juntos son 35 puntos."},
        {"p": "¿Qué pasa si el prototipo no carga?",
         "r": "Usan las capturas del plan B que dejaron en la carpeta desde la sesión 14, narran el "
              "mismo recorrido sobre ellas y **el tramo vale completo**. Usar bien el plan B es "
              "competencia, no fracaso. Lo que sí cuesta puntos es no tener capturas y perder dos "
              "minutos buscando la pestaña."},
        {"p": "¿Nos baja la nota contar que algo nos falló?",
         "r": "Al contrario: es el tramo 4 y vale 20 puntos. Un equipo que cuenta un fracaso con "
              "honestidad saca más que uno que presenta todo perfecto, porque en un prototipo de "
              "primer semestre «funcionó a la primera» significa que no se probó con nadie. Lo que sí "
              "baja la nota es no tener ninguna limitación declarada."},
        {"p": "¿Y si nos preguntan algo que no medimos?",
         "r": "Se dice **«no tenemos ese dato»**, y no pasa nada. Lo que hunde una sustentación es "
              "inventar una cifra con seguridad: una sola cifra inventada vuelve dudoso todo lo "
              "demás. Es la misma lección de la sesión 5 sobre datos con fuente y de la 11 sobre el "
              "asistente que inventa con seguridad."},
        {"p": "¿Con esto ya terminamos el curso?",
         "r": "No. Falta el **informe final de la sesión 16, que vale el 20 %** —más que la "
              "exposición— y la autoevaluación. La buena noticia es que **once de sus doce secciones "
              "ya están escritas** desde las sesiones anteriores: la próxima sesión es de armar y "
              "revisar, no de empezar de cero."},
    ],

    "notas_operativas": [
        "**Reparto propio hoy:** apertura y encuadre 10 · exposiciones 60 · valoración entre pares 12 "
        "· cierre 8. Anúncielo en el minuto 1.",
        "**Verifique el plan B de los cinco equipos antes de la primera exposición**: PDF descargado y "
        "capturas en la carpeta. Dos minutos que cada semestre salvan a un equipo.",
        "**Sortee el orden en vivo**, no antes. Si se anuncia con antelación, los últimos equipos "
        "siguen preparando en vez de escuchar.",
        "**Cronómetro grande en pantalla compartida**, aviso en el chat a los 8 minutos, corte a los "
        "9. Sin descuento adicional por pasarse.",
        "**Califique mientras escucha**, tramo por tramo, con una frase de por qué. Calificar al final "
        "premia al último equipo que se escuchó.",
        "Tenga **dos preguntas propias listas por equipo**. Las tres más útiles: «¿con quién lo "
        "probaron y qué hizo esa persona?» · «¿qué pasa con alguien que no tiene datos móviles?» · "
        "«si tuvieran una semana más, ¿qué harían primero?».",
        "Si el mismo integrante responde todo, **redirija al dueño del tramo**. Es el descuento "
        "anunciado que más enseña.",
        "La **ficha de valoración entre pares se califica** dentro de la nota de exposiciones del "
        "corte. Dígalo antes de que la llenen, no después.",
        "Si falta un integrante, el equipo aplica su **orden de emergencia** de la sesión 14; al "
        "ausente se le sustenta aparte y **no hereda la nota sin haber hablado**.",
        "En el cierre, **una observación por equipo en una frase**. La retroalimentación detallada va "
        "después por escrito, con las frases que anotó al calificar.",
        "Recuerde el peso de lo que falta: **informe final = 20 %**, más que la exposición de hoy.",
    ],

    "ti_siguiente": {
        "tid": "Valoración de presentaciones — completar la ficha de valoración de los otros cuatro "
               "equipos en el muro, si no quedó terminada en clase.",
        "ti": "Ajustes del informe final: **reunir las doce secciones** en un solo documento, tomando "
              "lo que ya está escrito desde la sesión 3, y **escribir el resumen de media página**, "
              "que es lo único nuevo. Y una tarea corta que vale mucho: **anotar lo que el curso no "
              "entendió** hoy de su proyecto.",
        "adelanto": "es la última: se **entrega el informe final (20 %)**, se socializa la galería de "
                    "proyectos del curso y se hace la **autoevaluación y coevaluación**.",
        "aviso": "El informe se entrega **en la sesión 16, dentro de la clase**: se revisa y se "
                 "completa ahí mismo, con la lista de verificación. Lleguen con el documento armado "
                 "—no con las secciones dispersas en cinco archivos— porque los 24 minutos de "
                 "revisión no alcanzan para copiar y pegar el curso entero.",
    },

    "cierre_titulo": "Nos vemos en la sesión 16 · la última",
    "cierre_frase": "Hace quince sesiones era una ocurrencia; hoy es un proyecto sustentado",
}


# =============================================================================
# CLASE 16 · Socializacion y evaluacion final del curso · CIERRA EL CORTE 3
# =============================================================================
# Ultima sesion. Reparto propio: 24 min de armado y revision del informe final (20 %),
# 20 de galeria en el muro, 20 de autoevaluacion y coevaluacion, 20 de cierre del curso.
# NO hay evaluacion escrita en el corte 3: el 40 % es exposicion 15 % + informe 20 % +
# asistencia 5 %. El builder usa `ti_siguiente` para la diapositiva «Cierre del curso».

TEMAS[16] = {
    "n": 16,
    "titulo": "Socialización y evaluación final del curso",
    "subtitulo": "Once de las doce secciones del informe ya están escritas — hoy se arma y se cierra",
    "hook": "El informe final tiene doce secciones y vale el 20 %. ¿Cuántas de esas doce creen que "
            "van a escribir hoy desde cero?",
    "hook_lines": [
        "Una. El resumen. Las otras once ya están escritas desde la sesión 3.",
        "Eso es lo que se gana escribiendo en cada sesión en vez de dejarlo para el final.",
    ],
    "objetivos": [
        "Armar y entregar el **informe final** con sus doce secciones (**20 %**).",
        "**Socializar** el proyecto en la galería del curso y ver los otros cuatro.",
        "Hacer una **autoevaluación y una coevaluación** con criterios, no con impresiones.",
        "Reconocer **qué se sabe hacer hoy** que no se sabía en la sesión 1.",
    ],
    "agenda_slots": [
        ("Apertura", 6, "Pregunta de entrada y qué se hace hoy"),
        ("Armado y revisión del informe final", 24, "Las doce secciones, con la lista de verificación"),
        ("Socialización: la galería del curso", 20, "5 equipos × 3 min en el muro, y recorrido libre"),
        ("Autoevaluación y coevaluación", 20, "Individual y del equipo, con criterios"),
        ("Cierre del curso", 20, "Lo que sabían en la sesión 1 y lo que saben hoy"),
    ],
    "agenda_sub": "Última sesión. No hay evaluación escrita: lo que se califica hoy es el informe "
                  "final (20 %) y la autoevaluación",
    "nota_bloque": "**No hay examen final escrito en este curso.** El 40 % del corte 3 se reparte en "
                   "exposición final 15 % (sesión 15) + **informe final 20 % (hoy)** + asistencia "
                   "5 %. El informe **se entrega dentro de la clase**: se arma, se revisa con la "
                   "lista de verificación y se sube antes de terminar la sesión.",
    "agenda": {},
    "herramienta_nota": "El informe en **Google Docs**, en la carpeta del equipo, con **el enlace "
                        "compartido y una copia en PDF**. La galería del curso en **Padlet**: una "
                        "columna por equipo con tres imágenes y cinco líneas. La **autoevaluación y "
                        "la coevaluación** en el formato del documento del equipo, y la individual se "
                        "entrega **solo al docente**, no al muro. **Hoy no se usa asistente de IA** — "
                        "pero sí se declara el que se usó en las sesiones 3 y 11.",
    "avance_proyecto": "Informe final entregado, proyecto socializado en la galería del curso, y "
                       "autoevaluación y coevaluación completadas — el proyecto queda cerrado",

    "teoria": [
        {
            "tipo": "tabla",
            "titulo": "Qué lleva el informe final (20 %) · secciones 1 a 6",
            "headers": ["Sección", "De dónde sale", "Largo"],
            "rows": [
                ["1 · Portada, integrantes y **resumen**",
                 "**Lo único nuevo de hoy.** El resumen: problema, solución y un número, en media página.",
                 "1 pág"],
                ["2 · El problema y su evidencia",
                 "Ficha del problema · **sesión 6**. Con la cifra y cómo se obtuvo.",
                 "½ pág"],
                ["3 · Actores y afectados",
                 "Mapa de actores · **sesión 3** + los afectados que no son usuarios · **sesión 13**.",
                 "½ pág"],
                ["4 · Antecedentes: qué existía ya",
                 "Las tres fichas de antecedentes · **sesión 9**, con la brecha que justifica el proyecto.",
                 "1 pág"],
                ["5 · Requisitos y criterios de aceptación",
                 "**Sesión 7**. Los funcionales, los no funcionales y cómo se verifica cada uno.",
                 "1 pág"],
                ["6 · Alternativas y decisión",
                 "Matriz de decisión y alcance mínimo · **sesión 8**. Con lo que se sacrificó.",
                 "1 pág"],
            ],
            "col_w": [3.0, 5.4, 0.8],
            "fs_body": 11,
        },
        {
            "tipo": "tabla",
            "titulo": "Qué lleva el informe final (20 %) · secciones 7 a 12",
            "headers": ["Sección", "De dónde sale", "Largo"],
            "rows": [
                ["7 · La solución y el prototipo",
                 "**Sesiones 10 y 11**, con capturas de las pantallas y el recorrido principal.",
                 "1–2 pág"],
                ["8 · Prueba con usuarios y hallazgos",
                 "**Sesión 12**. Los hallazgos, la clasificación y el patrón.",
                 "1 pág"],
                ["9 · Impacto social y ambiental",
                 "Matriz de impacto y mitigaciones · **sesión 13**. Positivos **y** negativos.",
                 "1 pág"],
                ["10 · Limitaciones y trabajo siguiente",
                 "Lo que se decidió **no** arreglar · **sesiones 12 y 13**, con el motivo.",
                 "½ pág"],
                ["11 · Declaración del uso de IA",
                 "**Sesiones 3 y 11**: qué se le pidió, qué se corrigió y **qué no se le entregó**.",
                 "¼ pág"],
                ["12 · Referencias",
                 "**Sesión 9**, en el formato acordado. Todo lo que se citó y nada que no se leyó.",
                 "½ pág"],
            ],
            "note": "**Once de doce secciones ya están escritas.** Hoy se arman en un solo documento, "
                    "se revisan con la lista de verificación y se escribe el resumen. Eso es lo que se "
                    "gana escribiendo en cada sesión en vez de dejarlo todo para el final.",
            "col_w": [3.0, 5.4, 0.8],
            "fs_body": 11,
        },
        {
            "tipo": "steps",
            "titulo": "Cómo se arma el informe en veinticuatro minutos",
            "steps": [
                ("1 · Un documento, doce títulos, ocho minutos", "Creen el documento con **los doce títulos vacíos** y peguen debajo de cada uno lo que ya está escrito. No reescriban: peguen."),
                ("2 · La lista de verificación, seis minutos", "Recorran la lista sección por sección. Marquen lo que **falta** en rojo, no lo que está."),
                ("3 · Reparto de los huecos, cuatro minutos", "Cada integrante toma un hueco rojo. **Nadie completa dos secciones y nadie ninguna.**"),
                ("4 · El resumen, cuatro minutos, al final", "Media página: el problema con su número, la solución en dos frases y el impacto principal. **Se escribe último aunque vaya primero.**"),
                ("5 · Entrega, dos minutos", "PDF en la carpeta del equipo **y** el enlace del documento. Antes de que termine la clase."),
            ],
            "sub": "El orden importa: pegar primero y revisar después. Empezar por el resumen es el error que hace que no alcance el tiempo",
        },
        {
            "tipo": "cards",
            "titulo": "Cuatro cosas que bajan la nota del informe",
            "cards": [
                ("Un informe que no cita sus propias sesiones",
                 "Si la sección 6 no dice **qué se sacrificó** al decidir, es que se reescribió de "
                 "memoria en vez de tomar la matriz de la sesión 8. Se nota, y cuesta puntos."),
                ("Referencias que nadie leyó",
                 "Una lista de diez enlaces cuando en la sesión 9 se trabajaron tres antecedentes. "
                 "**Cite lo que leyó**; lo demás es relleno y es fácil de comprobar."),
                ("Un informe sin limitaciones",
                 "La sección 10 vacía o con «ninguna» dice que el equipo no probó nada con nadie. "
                 "Después de la sesión 12, todos los equipos tienen limitaciones reales."),
                ("Todo escrito por una sola persona",
                 "Se reconoce en el cambio de tono entre secciones y en las secciones que quedaron "
                 "vacías. Reparto: **cada integrante responde por al menos dos secciones**."),
            ],
            "columns": 2,
        },
        {
            "tipo": "box",
            "titulo": "La autoevaluación y la coevaluación, en serio",
            "notas": [
                ("info",
                 "**La autoevaluación se hace con criterios, no con impresiones.** No es «me pongo "
                 "4.5»: son cuatro preguntas con evidencia — **qué hice yo concretamente** (secciones "
                 "que escribí, prueba que hice, tramo que expuse) · **qué aprendí a hacer que no "
                 "sabía** · **en qué fallé** · **qué haría distinto**. Con hechos que se pueden "
                 "verificar en el documento del equipo."),
                ("aclaracion",
                 "**La coevaluación es del trabajo, no de la persona.** Se valora cumplimiento de "
                 "acuerdos, aporte al proyecto y disposición para ayudar — **no simpatía**. Se "
                 "escribe con la misma regla de la sesión 12: **observación, no adjetivo**. «No "
                 "aportó» no sirve; «no entregó su sección en las tres últimas sesiones» sí."),
                ("advertencia",
                 "**La autoevaluación individual se entrega solo al docente**, no al muro y no al "
                 "equipo. Y ponerse la nota máxima sin evidencia baja el puntaje: lo que se evalúa "
                 "aquí es **la capacidad de mirar el propio trabajo con honestidad**, que es una "
                 "competencia profesional y no un trámite."),
            ],
        },
        {
            "tipo": "before_after",
            "titulo": "Lo que decían en la sesión 1 y lo que pueden sostener hoy",
            "before_title": "Sesión 1 · la prueba diagnóstica",
            "before": [
                "«La ingeniería es construir cosas con máquinas.»",
                "«Un problema se resuelve pensando en la solución.»",
                "«Lo importante es que funcione.»",
                "«Investigar es buscar en internet.»",
                "«El impacto es que la gente lo use.»",
            ],
            "after_title": "Sesión 16 · con su propio proyecto como prueba",
            "after": [
                "«La ingeniería **decide bajo restricciones**, y toda decisión sacrifica algo.»",
                "«Un problema **se define antes de resolverse**: causas, actores y evidencia.»",
                "«Que funcione no basta: hay **criterios de aceptación verificables**.»",
                "«Investigar es ver **qué ya existe y por qué no sirve aquí**, con la fuente citada.»",
                "«Hay **afectados que nunca la usan** y que quedan peor que antes.»",
            ],
            "sub": "No es una lista de frases aprendidas: cada una está sostenida por una sección de su propio informe",
            "size": 13,
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada: el pago de haber escrito en cada sesión",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "La apertura de la última sesión tiene una función precisa: **quitar el pánico y "
                "hacer visible una lección de método**. La pregunta —«el informe tiene doce secciones "
                "y vale el 20 %, ¿cuántas van a escribir hoy desde cero?»— produce respuestas de "
                "«ocho», «todas», y la respuesta real es **una**.",
                "Vale la pena detenerse ahí treinta segundos, porque es una de las lecciones más "
                "transferibles del curso: **el informe no se escribió hoy, se escribió en dieciséis "
                "sesiones.** La ficha del problema de la sesión 6 es la sección 2; la matriz de la 8 "
                "es la sección 6; los hallazgos de la 12 son la sección 8. Ningún equipo tuvo que "
                "escribir un informe: tuvieron que **armarlo**.",
                "Dígalo con el contraste explícito, porque es lo que se van a llevar a las otras "
                "asignaturas: **la alternativa era llegar hoy con veinticuatro minutos y doce "
                "secciones en blanco.** Es exactamente lo que le pasa a quien deja la documentación "
                "para el final, y no es un problema de tiempo sino de método.",
                "Después, en un minuto, diga qué se hace hoy y qué **no**: se arma y se entrega el "
                "informe, se socializa, se autoevalúan y se cierra el curso. **No hay examen final "
                "escrito** — conviene decirlo explícitamente porque la mitad del curso llega "
                "esperándolo, y saberlo cambia cómo usan los veinticuatro minutos del informe.",
            ],
        },
        {
            "titulo": "Las doce secciones, y el orden correcto para armarlas",
            "slide": "{{slide:secciones 1 a 6}} {{slide:secciones 7 a 12}} {{slide:Cómo se arma el informe}}",
            "cuerpo": [
                "Las dos tablas de secciones son el corazón de la sesión y hay que proyectarlas "
                "juntas, porque el efecto está en la columna del medio: **casi todas las filas dicen "
                "una sesión.** No las lea completas —son doce filas y aburre—; señale tres o cuatro "
                "y deje que el curso vea el patrón.",
                "El **largo por sección** está en la tabla y sirve para dos cosas: evita el informe "
                "de veinticinco páginas donde nadie encuentra nada, y evita el de tres donde no cabe "
                "el trabajo. En total son unas **9 a 11 páginas**, que es una extensión razonable "
                "para un proyecto de primer semestre. Si un equipo pregunta si puede ser más largo, "
                "la respuesta es que **la extensión no es una virtud**: un informe donde la decisión "
                "está en la página 18 es un informe que no se va a leer.",
                "**El orden de armado importa y es contraintuitivo**, así que hay que insistir: "
                "**pegar primero, revisar después, y el resumen al final.** El error que hace que no "
                "alcancen los veinticuatro minutos es empezar por el resumen —o peor, por la "
                "portada— porque el resumen exige tener todo lo demás decidido. Se escribe último "
                "aunque vaya primero. Esta regla es general para cualquier documento técnico y vale "
                "la pena nombrarla como tal.",
                "**El paso 2 tiene un detalle que cambia el resultado: marcar lo que falta, no lo "
                "que está.** Un equipo que va marcando lo hecho termina con una lista de logros y "
                "sin saber qué le falta. Marcando en rojo los huecos, la lista de tareas aparece "
                "sola, y el paso 3 —repartir los huecos, uno por integrante— se hace en cuatro "
                "minutos.",
                "Sobre la **sección 11, la declaración del uso de IA**: es un cuarto de página y es "
                "la que más se olvida. Tiene que decir qué se le pidió al asistente, qué se corrigió "
                "a mano y **qué no se le entregó** —ningún dato personal de terceros, que es la regla "
                "del curso desde la sesión 4 y que se trabajó en la 11—. Los equipos que no usaron IA "
                "también escriben la sección: dicen que no la usaron. Declarar es la norma, usarla o "
                "no es la decisión.",
            ],
        },
        {
            "titulo": "La galería, y por qué socializar no es exponer otra vez",
            "slide": "{{slide:Cuatro cosas que bajan la nota}}",
            "cuerpo": [
                "Los veinte minutos de socialización **no son una segunda ronda de exposiciones** — "
                "eso fue la sesión 15 y ya tiene nota. Aquí el formato es una **galería**: cada "
                "equipo deja en su columna del muro tres imágenes —una pantalla del prototipo, la "
                "matriz de impacto y la diapositiva del problema— y **cinco líneas**: el problema, la "
                "decisión, un hallazgo, un número de impacto y el siguiente paso.",
                "El reparto son 3 minutos por equipo para presentar la columna, y los 5 restantes "
                "para **recorrido libre**: cada estudiante entra a la columna de otro equipo y deja "
                "un comentario. Es rápido, es de baja presión —después de la sesión 15 el curso está "
                "cansado— y deja un registro del semestre que se puede mostrar el año siguiente.",
                "**Por qué vale la pena y no es relleno:** en la sesión 15 cada equipo escuchó cuatro "
                "exposiciones de nueve minutos, y a esa velocidad casi nadie retiene los detalles de "
                "los otros proyectos. La galería deja los cinco proyectos **lado a lado y por "
                "escrito**, y ahí sí se ven las comparaciones: cinco maneras distintas de definir un "
                "problema, cinco matrices de decisión, cinco listas de afectados. Es la única vez en "
                "el semestre en que el curso ve su propio trabajo completo.",
                "Aproveche los cuatro errores del informe [Slide 8] durante este bloque, mientras los "
                "equipos terminan de subir la columna: son las cuatro cosas que va a encontrar "
                "calificando y decirlas ahora les da tiempo de corregirlas. **La más frecuente es la "
                "sección 10 vacía** —«ninguna limitación»—, que después de la sesión 12 no es "
                "creíble en ningún equipo.",
            ],
        },
        {
            "titulo": "Autoevaluación y coevaluación: cómo evitar que sea un trámite",
            "slide": "{{slide:La autoevaluación y la coevaluación}}",
            "cuerpo": [
                "La autoevaluación se degrada en trámite cuando se pide una nota. **Pedir cuatro "
                "respuestas con evidencia lo evita**: qué hice yo concretamente —secciones que "
                "escribí, prueba que hice, tramo que expuse—, qué aprendí a hacer que no sabía, en "
                "qué fallé, qué haría distinto. Todo verificable en el documento del equipo.",
                "Y hay que decir la consecuencia con claridad, porque cambia el resultado: **ponerse "
                "la nota máxima sin evidencia baja el puntaje.** Lo que se evalúa no es la "
                "autoestima: es **la capacidad de mirar el propio trabajo con honestidad**, que es "
                "una competencia profesional. El estudiante que escribe «no entregué mi sección a "
                "tiempo dos veces y el equipo tuvo que cubrirme» está demostrando exactamente lo que "
                "se busca.",
                "La coevaluación es más delicada y necesita una regla dura: **se evalúa el trabajo, "
                "no la persona.** Tres criterios —cumplimiento de acuerdos, aporte al proyecto, "
                "disposición para ayudar— y la misma exigencia de la sesión 12: **observación, no "
                "adjetivo**. «No aportó» no sirve como coevaluación; «no entregó su sección en las "
                "tres últimas sesiones» sí, porque es verificable y porque la persona puede "
                "responder a un hecho y no a una etiqueta.",
                "**La autoevaluación individual se entrega solo al docente**, no al muro ni al "
                "equipo. Sin esa garantía nadie escribe nada honesto, y el ejercicio se vuelve un "
                "intercambio de cortesías. Dígalo antes de que empiecen a escribir.",
                "Un caso que aparece casi siempre: un equipo donde uno trabajó mucho menos. Si tres "
                "coevaluaciones independientes lo señalan **con hechos**, es información válida y "
                "puede diferenciar la nota individual. Si es una sola persona señalando y sin hechos, "
                "no alcanza. Y no resuelva el conflicto en público: recoja las coevaluaciones, léalas "
                "después y ajuste con criterio.",
            ],
        },
        {
            "titulo": "El cierre del curso: veinte minutos que no son un discurso",
            "slide": "{{slide:Lo que decían en la sesión 1}}",
            "cuerpo": [
                "Los últimos veinte minutos se pueden desperdiciar fácilmente en un discurso de "
                "despedida. **Úselos para hacer visible el aprendizaje, con evidencia.** La "
                "diapositiva de antes y después es la herramienta: en la columna izquierda están las "
                "respuestas reales de la prueba diagnóstica de la sesión 1 —vale la pena tenerlas a "
                "mano de verdad, no parafraseadas— y en la derecha lo que hoy pueden sostener.",
                "El punto que hay que hacer explícito, y que es la diferencia entre una clase y un "
                "curso: **cada frase de la columna derecha está sostenida por una sección de su "
                "propio informe.** «Toda decisión sacrifica algo» no es una frase aprendida: está en "
                "la sección 6, escrita por ellos, con una matriz detrás. «Hay afectados que nunca la "
                "usan» está en la sección 9, con la voluntaria que trabaja diez minutos más. Eso es "
                "lo que distingue haber entendido de haber memorizado, y conviene nombrarlo.",
                "Conecte con los tres RAA sin recitar códigos: reconocer la ingeniería como práctica "
                "que decide bajo restricciones (RAA1), aplicar un método para definir y resolver un "
                "problema con evidencia (RAA2), y valorar las consecuencias sociales y ambientales de "
                "una solución (RAA3). Los tres se pueden verificar en el informe que acaban de "
                "entregar, y esa verificabilidad es el sentido de haber trabajado por proyecto.",
                "Cierre con dos cosas concretas y ninguna solemne. La primera: **lo que se llevan es "
                "un método, no un tema.** Definir un problema con evidencia, revisar qué existe, "
                "decidir con criterios, probar con personas reales y mirar a quién afecta — eso sirve "
                "igual para un trabajo de otra asignatura, para un proyecto de grado y para el primer "
                "empleo. La segunda: **el proyecto queda como evidencia.** Es un trabajo completo, "
                "documentado y con su propio prototipo, hecho en primer semestre; el documento y las "
                "capturas quedan en la carpeta y valen para un portafolio.",
                "Y una recomendación práctica de despedida, corta: **el siguiente paso de su proyecto "
                "está escrito en la sección 10.** Si alguno quiere continuarlo, no tiene que empezar "
                "por decidir qué hacer; ya lo decidió.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:06 · Apertura · [Slide 4]",
            "cuerpo": [
                "Comparta pantalla antes de que entre el primero:",
                "> «El informe final tiene doce secciones y vale el 20 %. ¿Cuántas de esas doce creen "
                "que van a escribir hoy desde cero?»",
                "Deje que respondan «ocho», «todas». La respuesta es **una: el resumen**.",
                "**[Nota docente]:** haga la lección de método explícita: **el informe no se escribe "
                "hoy, se escribió en dieciséis sesiones.** La alternativa era llegar con veinticuatro "
                "minutos y doce secciones en blanco.",
                "**[Nota docente]:** diga que **no hay examen final escrito**. La mitad del curso "
                "llega esperándolo, y saberlo cambia cómo usan los veinticuatro minutos.",
            ],
        },
        {
            "titulo": "00:06–00:30 · Armado y revisión del informe (24 min) · [Slide 5]…[Slide 7]",
            "cuerpo": [
                "- **4 min** · Las dos tablas de secciones [Slide 5][Slide 6]. **No las lea "
                "completas**: señale tres filas y deje que vean el patrón de la columna del medio.",
                "- **2 min** · El orden de armado [Slide 7]: **pegar, revisar, resumen al final**.",
                "- **18 min** · Los equipos trabajan en salas de grupo.",
                "**[Nota docente]:** insista en **marcar lo que falta, no lo que está**. Un equipo "
                "que marca lo hecho termina con una lista de logros y sin saber qué le falta.",
                "**[Nota docente]:** entre a las salas con una sola pregunta: **«¿qué secciones "
                "están en rojo y quién tomó cada una?»**.",
                "**[Nota docente]:** la sección que falta en casi todos es la **11, la declaración "
                "del uso de IA**. Recuérdela: los equipos que no la usaron **también escriben la "
                "sección**, diciendo que no la usaron.",
                "**[Nota docente]:** verifique la entrega antes de pasar al bloque siguiente: **PDF "
                "en la carpeta y enlace del documento**.",
            ],
        },
        {
            "titulo": "00:30–00:50 · Socialización: la galería del curso (20 min) · [Slide 8]",
            "cuerpo": [
                "Cada equipo deja en su columna del muro **tres imágenes** —una pantalla del "
                "prototipo, la matriz de impacto, la diapositiva del problema— y **cinco líneas**: "
                "problema · decisión · un hallazgo · un número de impacto · siguiente paso.",
                "**3 min por equipo** para presentar la columna, y **5 min de recorrido libre**: cada "
                "estudiante comenta en la columna de otro equipo.",
                "**[Nota docente]:** aclare que **esto no es exponer otra vez** — la nota fue la "
                "sesión 15. Es dejar los cinco proyectos lado a lado, que es la única vez en el "
                "semestre en que el curso ve su propio trabajo completo.",
                "**[Nota docente]:** mientras suben las columnas, comente los **cuatro errores del "
                "informe** [Slide 8]. El más frecuente es la **sección 10 vacía**: después de la "
                "sesión 12, «ninguna limitación» no es creíble en ningún equipo. Decirlo ahora les da "
                "tiempo de corregirlo.",
            ],
        },
        {
            "titulo": "00:50–01:10 · Autoevaluación y coevaluación (20 min) · [Slide 9]",
            "cuerpo": [
                "- **3 min** · Explique el formato [Slide 9]. Diga desde el principio que la "
                "**autoevaluación individual llega solo al docente**: sin esa garantía nadie escribe "
                "nada honesto.",
                "- **10 min** · Autoevaluación individual: cuatro preguntas con evidencia.",
                "- **7 min** · Coevaluación del equipo: tres criterios, **observación y no adjetivo**.",
                "**[Nota docente]:** diga la consecuencia en voz alta: **ponerse la nota máxima sin "
                "evidencia baja el puntaje**, porque lo que se evalúa es la capacidad de mirar el "
                "propio trabajo con honestidad.",
                "**[Nota docente]:** si aparece un conflicto de equipo, **no lo resuelva en público**. "
                "Recoja las coevaluaciones, léalas después y ajuste con criterio: tres "
                "coevaluaciones independientes con hechos son información válida; una sola sin hechos "
                "no alcanza.",
            ],
        },
        {
            "titulo": "01:10–01:30 · Cierre del curso (20 min) · [Slide 10][Slide 13][Slide 14]",
            "cuerpo": [
                "**[Slide 10]** Antes y después. Tenga a mano **las respuestas reales de la prueba "
                "diagnóstica de la sesión 1**, no parafraseadas: el efecto está en que sean suyas.",
                "El punto central, dicho explícitamente: **cada frase de la columna derecha está "
                "sostenida por una sección de su propio informe.** «Toda decisión sacrifica algo» "
                "está en la sección 6, con una matriz detrás.",
                "Conecte los tres RAA sin recitar códigos: la ingeniería decide bajo restricciones · "
                "un problema se define con método y evidencia · una solución tiene consecuencias "
                "sociales y ambientales. Los tres se verifican en el informe que acaban de entregar.",
                "Cierre con dos cosas concretas: **se llevan un método, no un tema** —sirve para otra "
                "asignatura, para un proyecto de grado y para el primer empleo— y **el proyecto queda "
                "como evidencia**, documentado y con prototipo, hecho en primer semestre.",
                "Y la despedida práctica: **el siguiente paso de su proyecto está escrito en la "
                "sección 10.** Quien quiera continuarlo ya no tiene que decidir por dónde empezar.",
            ],
        },
    ],

    "taller": {
        "archivo": "Informe final y autoevaluacion",
        "titulo": "Informe final y autoevaluación",
        "min": 24,
        "exposicion": 3,
        "consigna": "Armen el **informe final** con sus doce secciones en un solo documento, "
                    "revísenlo con la lista de verificación, completen los huecos y escriban el "
                    "**resumen** de media página. Después, la **autoevaluación individual** y la "
                    "**coevaluación del equipo**. El informe vale el **20 %** del curso y se entrega "
                    "**dentro de la clase**.",
        "entregable": "el informe final en PDF y el enlace del documento en la carpeta del equipo, la "
                      "columna del equipo en la galería del muro, y la autoevaluación individual "
                      "entregada solo al docente",
        "entregable_corto": "informe final en PDF + galería en el muro + autoevaluación y coevaluación",
        "reparto_titulo": "Los veinticuatro minutos, en orden:",
        "reparto": "8 min pegar lo ya escrito bajo los doce títulos · 6 min recorrer la lista de "
                   "verificación marcando **lo que falta** · 4 min repartir los huecos, uno por "
                   "integrante · 4 min el **resumen, al final** · 2 min entregar. **No empiecen por "
                   "el resumen ni por la portada.**",
        "reparto_corto": "24 min: pegar, verificar, repartir huecos, resumen y entregar",
        "bloques": [
            {"clave": "LA LISTA DE VERIFICACIÓN DEL INFORME",
             "pide": "Las **doce secciones** en un solo documento, cada una con lo que ya estaba "
                     "escrito desde su sesión, y con el largo de la tabla.",
             "check": "las doce secciones existen y ninguna está vacía. Si la 11 falta, falta la mitad de los puntos de este bloque."},
            {"clave": "LO QUE FALTABA Y SE COMPLETÓ HOY",
             "pide": "Los huecos que se marcaron en rojo, **quién tomó cada uno** y qué se escribió. "
                     "Incluido el **resumen**, que es lo único nuevo.",
             "check": "cada integrante completó al menos un hueco y el resumen tiene el problema con su número."},
            {"clave": "LA DECLARACIÓN DEL USO DE IA",
             "pide": "Qué se le pidió al asistente, **qué se corrigió a mano** y **qué no se le "
                     "entregó**. Si no se usó, se dice que no se usó.",
             "check": "dice explícitamente que no se le entregaron datos personales de terceros. Declarar es obligatorio; usarla, no."},
            {"clave": "LA AUTOEVALUACIÓN INDIVIDUAL",
             "pide": "Cuatro respuestas **con evidencia**: qué hice yo · qué aprendí a hacer que no "
                     "sabía · en qué fallé · qué haría distinto. **Solo para el docente.**",
             "check": "cada respuesta se puede verificar en el documento del equipo. Una nota sin hechos no es autoevaluación."},
            {"clave": "LA COEVALUACIÓN DEL EQUIPO",
             "pide": "Cumplimiento de acuerdos, aporte al proyecto y disposición para ayudar, con "
                     "**observaciones y no adjetivos**.",
             "check": "no hay etiquetas de persona. «No aportó» no cuenta; «no entregó su sección en las tres últimas sesiones» sí."},
        ],
        "expo": [
            ("Imagen 1", "Una pantalla del prototipo funcionando."),
            ("Imagen 2", "La matriz de impacto, o la diapositiva del problema con su cifra."),
            ("Cinco líneas", "Problema · decisión · un hallazgo · un número de impacto · siguiente paso."),
            ("Recorrido libre", "Cada estudiante comenta en la columna de otro equipo."),
        ],
    },

    "rubrica": [
        ("Las doce secciones están, con su contenido tomado de la sesión donde se trabajó", 30,
         "Es la verificación de que el proyecto se documentó a medida que se hacía, y no se reconstruyó de memoria al final."),
        ("Los huecos se completaron y el resumen tiene el problema con su número", 20,
         "El resumen es lo único nuevo del día y es lo primero que lee quien evalúa: media página decide la impresión del informe."),
        ("La declaración del uso de IA dice qué se corrigió y qué no se le entregó", 15,
         "Declarar es la norma del curso, y el «qué no se le entregó» protege datos de terceros: la regla desde la sesión 4."),
        ("La autoevaluación individual responde con evidencia verificable, incluido un fallo", 20,
         "Lo que se evalúa es la capacidad de mirar el propio trabajo con honestidad, no la nota que uno se pone."),
        ("La coevaluación usa observaciones y no adjetivos sobre las personas", 15,
         "Un hecho verificable se puede responder; una etiqueta solo se puede resentir. Es la regla de la sesión 12."),
    ],

    "solucion": {
        "para_que": "Este documento trae la **lista de verificación completa de las doce secciones** "
                    "con lo que debe contener cada una, el resumen del caso de la biblioteca escrito "
                    "como modelo, la declaración de uso de IA redactada, y los formatos de "
                    "autoevaluación y coevaluación con ejemplos de respuesta buena y mala. Si solo "
                    "alcanza a leer un bloque, que sea **LA LISTA DE VERIFICACIÓN**: es lo que se "
                    "proyecta y lo que estructura los veinticuatro minutos.",
        "caso_titulo": "La biblioteca del barrio · el informe final armado",
        "caso": "Mismo equipo de todo el corte. Todo el material existe desde las sesiones 3 a 13; el "
                "trabajo de hoy es reunirlo, encontrar los huecos y escribir media página nueva. Lo "
                "que sigue es cómo quedó, sección por sección, y qué se descubrió que faltaba.",
        "por_que_este_caso": "Porque muestra el resultado de haber escrito en cada sesión: al armar "
                            "el documento aparecieron **tres huecos y no doce**. Y los tres huecos "
                            "son los mismos que aparecen en casi todos los equipos, así que sirven "
                            "de aviso: el resumen, la declaración de uso de IA y las referencias en "
                            "formato.",
        "bloques": [
            {
                "clave": "LA LISTA DE VERIFICACIÓN DEL INFORME",
                "respuesta": "**La lista completa, para proyectar y recorrer sección por sección:**\n\n"
                             "| # | Sección | Tiene que contener | ¿De dónde? |\n"
                             "|---|---|---|---|\n"
                             "| 1 | Portada y **resumen** | Título, integrantes, curso. Resumen de ½ pág: problema con su número, solución en dos frases, impacto principal. | **Nuevo hoy** |\n"
                             "| 2 | El problema | La cifra, **cómo se obtuvo**, a quién le pasa y las causas principales. | Sesión 6 |\n"
                             "| 3 | Actores y afectados | Usuarios, quien opera, **y al menos un afectado que no es usuario**. | Sesiones 3 y 13 |\n"
                             "| 4 | Antecedentes | Tres soluciones que ya existen, qué hace cada una y **por qué no sirve aquí**. | Sesión 9 |\n"
                             "| 5 | Requisitos y criterios | Funcionales, no funcionales, y **cómo se verifica cada criterio**. | Sesión 7 |\n"
                             "| 6 | Alternativas y decisión | Al menos dos alternativas, los criterios, la elegida **y qué se sacrificó**. | Sesión 8 |\n"
                             "| 7 | La solución y el prototipo | Descripción, **capturas** y el recorrido principal paso a paso. | Sesiones 10 y 11 |\n"
                             "| 8 | Prueba y hallazgos | Con quién se probó (**solo el rol, no el nombre**), qué hizo, la clasificación y el patrón. | Sesión 12 |\n"
                             "| 9 | Impacto | Positivos con indicador **y negativos con mitigación**. | Sesión 13 |\n"
                             "| 10 | Limitaciones y siguiente paso | Lo que se decidió **no** hacer, con el motivo, y por dónde seguiría. | Sesiones 12 y 13 |\n"
                             "| 11 | Declaración del uso de IA | Qué se pidió, qué se corrigió, **qué no se le entregó**. | Sesiones 3 y 11 |\n"
                             "| 12 | Referencias | Lo que se citó, en el formato acordado. **Nada que no se haya leído.** | Sesión 9 |\n\n"
                             "**Extensión total: 9 a 11 páginas.** Si un equipo pregunta si puede ser "
                             "más largo, la respuesta es que **la extensión no es una virtud**: un "
                             "informe donde la decisión está en la página 18 es un informe que no se "
                             "va a leer.\n\n"
                             "**Los tres huecos que aparecieron al armar este informe** —y que "
                             "aparecen en casi todos los equipos—:\n\n"
                             "1. **El resumen** (sección 1), que no existía porque nunca se pidió antes.\n"
                             "2. **La declaración del uso de IA** (sección 11): el equipo tenía la del "
                             "prototipo de la sesión 11, pero **había olvidado la lluvia de ideas "
                             "asistida de la sesión 3**. Le pasa a la mayoría.\n"
                             "3. **Las referencias en formato** (sección 12): los tres antecedentes "
                             "estaban descritos, pero los enlaces estaban pegados sueltos en el "
                             "documento de la sesión 9, sin autor ni fecha de consulta.\n\n"
                             "**Y un hueco que apareció al revisar la sección 8:** el informe decía "
                             "«probamos con don Óscar, el vecino del 302». **Eso hay que corregirlo "
                             "en el momento**: en el informe va **el rol, no el nombre** —«un vecino "
                             "de 34 años, ajeno al equipo»—. Es la regla del curso desde la sesión 4 "
                             "y la sección 8 es donde más se rompe.",
                "como_calificar": "30 pts, y es el bloque de más peso. Cuente secciones: las doce "
                                  "presentes y no vacías valen 18; los otros 12 se reparten en "
                                  "**calidad del contenido tomado de su sesión** —¿la sección 6 dice "
                                  "qué se sacrificó? ¿la 9 tiene negativos? ¿la 8 describe "
                                  "comportamiento y no opiniones?—. **Si la sección 10 dice "
                                  "«ninguna», reste 5 y escríbalo:** después de la sesión 12 todos "
                                  "los equipos tienen limitaciones reales. Y revise la sección 8 "
                                  "buscando **nombres de personas**: si aparecen, pídalo corregido "
                                  "antes de cerrar la nota."
            },
            {
                "clave": "LO QUE FALTABA Y SE COMPLETÓ HOY",
                "respuesta": "**El resumen, escrito como modelo** (media página, y es lo primero que "
                             "lee quien califica):\n\n"
                             "> **Resumen.** En la biblioteca comunitaria del barrio Los Cámbulos, "
                             "**cuatro de cada diez visitas terminan sin préstamo** porque no hay "
                             "manera de saber si un libro está disponible antes de ir: lo contamos "
                             "durante dos semanas, 38 de 94 visitas. Cada visita fallida cuesta un "
                             "pasaje y unos veinticinco minutos de camino.\n>\n"
                             "> Frente a dos alternativas —un registro en línea en tiempo real y una "
                             "lista publicada que se actualiza al cierre— elegimos la segunda con una "
                             "matriz de cinco criterios, **sacrificando tener la información al "
                             "minuto** porque la primera exigía un computador en el mostrador que no "
                             "existe. Construimos un prototipo consultable desde el celular sin crear "
                             "cuenta, con la fecha del dato visible en cada resultado, y una pantalla "
                             "para que la voluntaria marque préstamos: **catorce segundos por "
                             "préstamo**, contra un criterio de aceptación de treinta.\n>\n"
                             "> Lo probamos con dos personas ajenas al equipo. Las dos intentaron "
                             "tocar el estado «Prestado» esperando una acción, así que lo "
                             "rediseñamos; una de ellas abandonó al escribir «100 años» en vez de "
                             "«cien años», y **decidimos no implementar la búsqueda tolerante a "
                             "errores**: queda declarada como limitación. Si se evita la mitad de las "
                             "visitas fallidas son **30 viajes menos al mes**; el costo es que **la "
                             "voluntaria trabaja diez minutos más cada día** y que una de cada cinco "
                             "personas no tiene datos para consultar, para quienes propusimos una "
                             "cartelera impresa en la puerta.\n\n"
                             "**Por qué este resumen funciona, y vale señalarlo en clase:** tiene los "
                             "cinco tramos de la exposición en cuatro párrafos, **un número en cada "
                             "uno**, dice qué se sacrificó, dice qué falló y **pone el costo al lado "
                             "del beneficio**. Se lee en noventa segundos y quien lo lee ya sabe si "
                             "el proyecto es serio.\n\n"
                             "**Los otros dos huecos y su reparto** (paso 3 del armado):\n\n"
                             "| Hueco | Quién lo tomó | Qué escribió |\n"
                             "|---|---|---|\n"
                             "| Resumen | Ana | El texto de arriba, después de que las demás secciones estuvieran pegadas. |\n"
                             "| Declaración de IA (sección 11) | Brayan | Agregó **la lluvia de ideas de la sesión 3**, que se había olvidado. |\n"
                             "| Referencias en formato (sección 12) | Camila | Autor, título, enlace y fecha de consulta de los tres antecedentes. |\n"
                             "| Quitar el nombre en la sección 8 | Daniel | «don Óscar, el vecino del 302» → «un vecino de 34 años, ajeno al equipo». |\n\n"
                             "**Cuatro integrantes, cuatro huecos, un hueco cada uno.** Es el reparto "
                             "que hace que veinticuatro minutos alcancen — y la razón por la que el "
                             "paso 2 marca **lo que falta** y no lo que está.",
                "como_calificar": "20 pts: 12 por el **resumen** —¿tiene el problema con su número? "
                                  "¿dice qué se sacrificó? ¿tiene un impacto con su costo?— y 8 por "
                                  "el reparto de los huecos, que se verifica preguntando en la sala "
                                  "**quién tomó cada uno**. Un resumen que solo describe la solución, "
                                  "sin problema y sin números, vale 5: es el error más común y se "
                                  "corrige leyendo el modelo en voz alta. Ojo: **si un integrante no "
                                  "completó ningún hueco**, el bloque baja a 12."
            },
            {
                "clave": "LA DECLARACIÓN DEL USO DE IA",
                "respuesta": "**La declaración completa, un cuarto de página**, como quedó en el "
                             "informe:\n\n"
                             "> **Declaración del uso de asistentes de inteligencia artificial.**\n>\n"
                             "> Usamos un asistente de IA en dos momentos del curso, los dos "
                             "autorizados en clase.\n>\n"
                             "> **Sesión 3 · lluvia de ideas.** Le pedimos alternativas para el "
                             "problema del acceso a los libros. De las siete que propuso, tomamos "
                             "dos —la lista publicada y el registro en tiempo real— y descartamos las "
                             "otras cinco porque suponían presupuesto o personal que la biblioteca no "
                             "tiene.\n>\n"
                             "> **Sesión 11 · prototipado.** Le pedimos tres variantes de la pantalla "
                             "de consulta, dándole el problema, los actores y las restricciones. "
                             "Elegimos una y **le corregimos seis cosas a mano**: agregamos la fecha "
                             "del dato, quitamos el registro de usuario que había inventado, "
                             "eliminamos un campo que pedía el número de cédula, redujimos el peso de "
                             "las imágenes para cumplir el límite de 200 KB, cambiamos el estado "
                             "«Prestado» para que no pareciera un botón y quitamos una sección de "
                             "estadísticas que nadie había pedido.\n>\n"
                             "> **Lo que no le entregamos:** ningún dato personal de la voluntaria, de "
                             "los usuarios de la biblioteca ni de las dos personas que probaron el "
                             "prototipo. Ningún nombre, teléfono, dirección o foto de terceros. "
                             "Tampoco el nombre exacto de la biblioteca.\n>\n"
                             "> **Lo que no hizo la IA:** el conteo en la puerta, la matriz de "
                             "decisión, la prueba con usuarios, la matriz de impacto y este informe.\n\n"
                             "**Los tres elementos que la hacen válida:** dice **qué se pidió**, dice "
                             "**qué se corrigió** —con las seis correcciones, no «lo revisamos»— y "
                             "dice **qué no se le entregó**. El último es el que protege a terceros y "
                             "es la regla del curso desde la sesión 4: **lo que se escribe en una "
                             "herramienta en línea sale del computador y no vuelve.**\n\n"
                             "**Si el equipo no usó IA**, la sección igual se escribe: *«No usamos "
                             "asistentes de IA en ninguna etapa del proyecto.»* Una línea. **Declarar "
                             "es obligatorio; usarla o no es la decisión del equipo**, y las dos "
                             "opciones son válidas.\n\n"
                             "**El olvido casi universal:** los equipos declaran el uso de la sesión "
                             "11 —el prototipo, que es reciente— y **olvidan la lluvia de ideas de la "
                             "sesión 3**. Vale la pena avisarlo en voz alta durante el armado.",
                "como_calificar": "15 pts: 5 por declarar **qué se pidió**, 5 por **las correcciones "
                                  "concretas** —«lo revisamos» no cuenta; se piden hechos— y 5 por el "
                                  "**qué no se le entregó**. Un equipo que declara solo el uso de la "
                                  "sesión 11 y olvida la 3 vale 10 y se le dice cuál falta. Un equipo "
                                  "que no usó IA y lo declara en una línea **vale los 15 completos**: "
                                  "lo que se evalúa es la transparencia, no el uso."
            },
            {
                "clave": "LA AUTOEVALUACIÓN INDIVIDUAL",
                "respuesta": "**El formato: cuatro preguntas, todas con evidencia verificable.** Y el "
                             "contraste que conviene proyectar, porque explica el criterio mejor que "
                             "cualquier instrucción:\n\n"
                             "| Pregunta | Respuesta que no sirve | Respuesta que sí |\n"
                             "|---|---|---|\n"
                             "| **¿Qué hice yo concretamente?** | «Ayudé en todo lo que pude y siempre estuve pendiente del grupo.» | «Escribí las secciones 4 y 9, hice la prueba con la señora de 61 años y expuse el tramo 4.» |\n"
                             "| **¿Qué aprendí a hacer que no sabía?** | «Aprendí mucho sobre ingeniería y trabajo en equipo.» | «Aprendí a separar lo que una persona **hace** de lo que **dice**: en la prueba anoté que abandonó, no que «le pareció difícil».» |\n"
                             "| **¿En qué fallé?** | «En nada, cumplí con todo.» | «Entregué mi sección tarde dos veces y Camila tuvo que cubrirme el día del prototipo.» |\n"
                             "| **¿Qué haría distinto?** | «Organizarme mejor con el tiempo.» | «Probaría el prototipo con alguien de afuera **antes** de la sesión 12: los dos hallazgos grandes salieron en veinte minutos y pudimos haberlos tenido dos semanas antes.» |\n\n"
                             "**La diferencia entre las dos columnas no es la extensión: es la "
                             "verificabilidad.** Todo lo de la derecha se puede comprobar en el "
                             "documento del equipo o en el historial del muro. Todo lo de la "
                             "izquierda podría haberlo escrito cualquier estudiante de cualquier "
                             "curso, y por eso no vale.\n\n"
                             "**La consigna que hay que decir en voz alta antes de que escriban:** "
                             "**ponerse la nota máxima sin evidencia baja el puntaje.** No es una "
                             "trampa: lo que se evalúa es **la capacidad de mirar el propio trabajo "
                             "con honestidad**, que es una competencia profesional y no un trámite. "
                             "El estudiante de la columna derecha, que reconoce haber entregado tarde "
                             "dos veces, saca más que el que dice «cumplí con todo».\n\n"
                             "**Se entrega solo al docente**, no al muro y no al equipo. Sin esa "
                             "garantía, la pregunta «¿en qué fallé?» se responde siempre con «en "
                             "nada» y el ejercicio completo se pierde.",
                "como_calificar": "20 pts: 5 por cada pregunta, y el criterio es uno solo — "
                                  "**¿se puede verificar?**. Una respuesta genérica vale 2. Y la "
                                  "pregunta 3 es la que decide el puntaje del bloque: **quien "
                                  "responde «en nada, cumplí con todo» no pasa de 10 en total**, y "
                                  "hay que devolvérselo escrito con la razón, porque es la parte "
                                  "formativa del ejercicio. Valore mucho la respuesta 4 cuando "
                                  "propone un cambio de método y no de actitud: «probaría antes» "
                                  "enseña más que «me organizaría mejor»."
            },
            {
                "clave": "LA COEVALUACIÓN DEL EQUIPO",
                "respuesta": "**Tres criterios, cada integrante evalúa a los otros**, y una sola "
                             "regla dura: **se evalúa el trabajo, no la persona.**\n\n"
                             "| Criterio | Qué se mira | Ejemplo bien escrito |\n"
                             "|---|---|---|\n"
                             "| **Cumplimiento de acuerdos** | Entregó lo que le tocaba, en el plazo que el equipo acordó. | «Entregó sus dos secciones antes de la fecha en las cuatro últimas sesiones.» |\n"
                             "| **Aporte al proyecto** | Qué del proyecto existe porque esa persona lo hizo. | «La matriz de impacto la armó ella; sin eso no teníamos la sección 9.» |\n"
                             "| **Disposición para ayudar** | Ayudó cuando otro estaba atrasado o atascado. | «Me explicó dos veces cómo se llenaba la matriz cuando no entendí.» |\n\n"
                             "**Y la comparación que enseña el criterio:**\n\n"
                             "| No sirve | Sirve |\n"
                             "|---|---|\n"
                             "| «No aportó nada.» | «No entregó su sección en las tres últimas sesiones y la cubrió Brayan.» |\n"
                             "| «Es muy desorganizado.» | «Cambió el archivo del prototipo sin avisar y perdimos las capturas del lunes.» |\n"
                             "| «Trabaja súper bien, es lo máximo.» | «Hizo las dos pruebas con personas de afuera, que era lo más incómodo del proyecto.» |\n\n"
                             "**Por qué la regla importa y no es formalismo:** un hecho verificable **se "
                             "puede responder** —la persona puede explicar, corregir o "
                             "comprometerse—; una etiqueta solo se puede resentir. Es exactamente la "
                             "regla de retroalimentación de la sesión 12, aplicada al equipo, y ese "
                             "es el punto: la coevaluación no es un desahogo, es retroalimentación.\n\n"
                             "**Cómo se usa esto al calificar, y conviene tenerlo decidido antes:** si "
                             "**tres coevaluaciones independientes** señalan a la misma persona **con "
                             "hechos**, es información válida y puede diferenciar la nota individual "
                             "del promedio del equipo. **Una sola coevaluación negativa, o varias sin "
                             "hechos, no alcanza.** Y no se resuelve en público: se recogen, se leen "
                             "después y se ajusta con criterio.\n\n"
                             "**El caso incómodo que hay que anticipar:** el equipo que se pone todos "
                             "5.0 entre sí para no incomodar a nadie. Se reconoce porque las "
                             "observaciones son adjetivos vacíos en todas las filas. La respuesta no "
                             "es castigar: es pedir **un hecho por criterio** y volver a recogerlas. "
                             "Con la exigencia de escribir un hecho, la cortesía automática se cae "
                             "sola.",
                "como_calificar": "15 pts, y se califica **la calidad de las observaciones, no la "
                                  "generosidad de las notas**: 9 por tener un hecho verificable en "
                                  "cada criterio, 6 por ausencia de etiquetas sobre la persona. Una "
                                  "coevaluación de puros adjetivos —«es lo máximo», «no aportó»— vale "
                                  "5, sin importar si es positiva o negativa. Recójalas y léalas "
                                  "**después de clase**, nunca en público, y recuerde el umbral: tres "
                                  "coevaluaciones independientes con hechos pueden diferenciar una "
                                  "nota individual; una sola sin hechos, no."
            },
        ],
        "variantes": [
            {"caso": "Equipos que llegan con las secciones dispersas en cinco archivos",
             "clave": "Es el escenario que se avisó en la sesión 15 y aun así pasa. Que **repartan "
                      "el copiar y pegar entre los integrantes en paralelo** —cada uno pega tres "
                      "secciones en el documento compartido— en vez de hacerlo uno solo mientras los "
                      "demás miran. Con cuatro personas trabajando a la vez, veinticuatro minutos "
                      "alcanzan; con una sola, no. Y no permita que reescriban: hoy se pega, no se "
                      "redacta de nuevo."},
            {"caso": "Un equipo al que le falta media sección entera",
             "clave": "Lo más frecuente es la 4 (antecedentes) o la 9 (impacto), cuando no "
                      "terminaron el taller de esa sesión. Que escriban **lo que sí tienen y una "
                      "línea honesta de lo que falta**: «solo alcanzamos a revisar dos antecedentes». "
                      "Una sección incompleta y declarada vale más que una inventada hoy en cinco "
                      "minutos, y así se lo puede decir: **inventar contenido en la última sesión es "
                      "lo único que no se puede recuperar después**."},
            {"caso": "Un estudiante que se autoevalúa con la nota máxima y sin evidencia",
             "clave": "No lo discuta en el momento. Califique según el criterio —no pasa de 10 sobre "
                      "20— y **devuélvale escrito por qué**, con un ejemplo de respuesta "
                      "verificable. Es la parte formativa del ejercicio y muchos estudiantes de "
                      "primer semestre nunca han recibido esa distinción. Si hay tiempo en el bloque, "
                      "proyecte la tabla de respuestas que sirven y que no sirven **antes** de que "
                      "escriban: reduce el problema a la mitad."},
            {"caso": "Un conflicto de equipo que estalla en la coevaluación",
             "clave": "**No lo resuelva en público y no lo deje escalar en el chat.** Recoja las "
                      "coevaluaciones, cierre el bloque y hable después con los involucrados por "
                      "separado. El criterio ya está fijado: tres coevaluaciones independientes con "
                      "hechos pueden diferenciar la nota individual; una sola sin hechos, no. Y "
                      "recuerde que la nota del informe es del equipo: lo que se ajusta con la "
                      "coevaluación es el componente individual, no el trabajo entregado."},
            {"caso": "Un equipo termina el informe en quince minutos",
             "clave": "Casi siempre significa que pegó sin revisar. Deles la lista de verificación y "
                      "**tres preguntas concretas**: «¿la sección 6 dice qué sacrificaron?», «¿la 9 "
                      "tiene impactos negativos?», «¿la 8 tiene nombres de personas?». Si las tres "
                      "respuestas son buenas, que usen el tiempo restante en la columna de la "
                      "galería, que es lo que casi siempre queda a medias."},
        ],
        "cierre": "Veinte minutos de cierre, y la tentación es usarlos en un discurso de despedida. "
                  "**Úselos para hacer visible el aprendizaje con evidencia.** Proyecte el antes y "
                  "después con **las respuestas reales de la prueba diagnóstica de la sesión 1** —no "
                  "parafraseadas: el efecto está en que sean suyas— y haga el punto explícito, que es "
                  "la diferencia entre una clase y un curso: **cada frase de la columna derecha está "
                  "sostenida por una sección de su propio informe.** «Toda decisión sacrifica algo» "
                  "no es una frase aprendida: está en la sección 6, con una matriz detrás. «Hay "
                  "afectados que nunca la usan» está en la sección 9, con la voluntaria que trabaja "
                  "diez minutos más cada día. Conecte los tres RAA sin recitar códigos —la ingeniería "
                  "decide bajo restricciones, un problema se define con método y evidencia, una "
                  "solución tiene consecuencias sociales y ambientales— y muestre que los tres se "
                  "verifican en el documento que acaban de entregar: esa verificabilidad es el "
                  "sentido de haber trabajado por proyecto en vez de por temas. Cierre con dos cosas "
                  "concretas y ninguna solemne. **Se llevan un método, no un tema:** definir un "
                  "problema con evidencia, revisar qué existe, decidir con criterios, probar con "
                  "personas reales y mirar a quién afecta — sirve igual para otra asignatura, para un "
                  "proyecto de grado y para el primer empleo. **Y el proyecto queda como evidencia:** "
                  "un trabajo completo, documentado, con prototipo propio y hecho en primer semestre; "
                  "el informe y las capturas quedan en la carpeta y valen para un portafolio. La "
                  "última frase, práctica: **el siguiente paso de su proyecto está escrito en la "
                  "sección 10** — quien quiera continuarlo ya no tiene que decidir por dónde empezar.",
        "conexion": "Hacia atrás, esta sesión cobra el curso completo y de forma literal: **once de "
                    "las doce secciones del informe se escribieron en las sesiones 3, 6, 7, 8, 9, "
                    "10, 11, 12 y 13**, y la tabla de secciones lo hace visible fila por fila. La "
                    "regla de la sección 8 —el rol y no el nombre— viene de la **sesión 4**; la "
                    "declaración de uso de IA, de las **sesiones 3 y 11**; la exigencia de "
                    "observación en vez de adjetivo en la coevaluación, de la **sesión 12**; el "
                    "resumen retoma los cinco tramos de la exposición de la **sesión 14**; y las "
                    "preguntas que el curso no resolvió en la **sesión 15** fueron la lista de tareas "
                    "de hoy. Hacia adelante, fuera del curso: el método —definir con evidencia, "
                    "revisar antecedentes, decidir con criterios, probar con personas, valorar "
                    "impacto— es el mismo de cualquier proyecto de ingeniería, y el informe queda "
                    "como evidencia de portafolio.",
    },

    "errores": [
        {"dice": "«Empecemos por la portada y el resumen»",
         "por_que": "El resumen exige tener todo lo demás decidido: escribirlo primero obliga a reescribirlo, y los 24 minutos no alcanzan.",
         "pida": "Pegar las once secciones que ya existen, revisar, y el resumen al final. Aunque vaya primero en el documento."},
        {"dice": "Ir marcando en la lista lo que ya está hecho",
         "por_que": "Se termina con una lista de logros y sin saber qué falta, que es justo lo que se necesita para repartir el trabajo.",
         "pida": "Marcar en rojo **lo que falta**. La lista de tareas aparece sola y se reparte en cuatro minutos."},
        {"dice": "«Probamos con don Óscar, el vecino del 302»",
         "por_que": "Es un dato personal de un tercero en un documento que se entrega. Es la regla del curso desde la sesión 4.",
         "pida": "El rol, no el nombre: «un vecino de 34 años, ajeno al equipo». La sección 8 es donde más se rompe esta regla."},
        {"dice": "«Limitaciones: ninguna»",
         "por_que": "Después de la sesión 12 todos los equipos tienen limitaciones reales, así que «ninguna» dice que no se probó con nadie.",
         "pida": "Lo que se decidió no arreglar, con el motivo. Declararlo sube la nota; ocultarlo la baja."},
        {"dice": "«En qué fallé: en nada, cumplí con todo»",
         "por_que": "Lo que se evalúa es la capacidad de mirar el propio trabajo con honestidad, y esa respuesta demuestra lo contrario.",
         "pida": "Un hecho verificable: «entregué mi sección tarde dos veces y otro integrante tuvo que cubrirme»."},
    ],

    "dudas": [
        {"p": "¿Hay examen final?",
         "r": "**No.** En este curso no hay evaluación escrita en el corte 3: el 40 % se reparte en la "
              "exposición final de la sesión 15 (15 %), el **informe final de hoy (20 %)** y "
              "asistencia (5 %). Las dos evaluaciones escritas del semestre fueron las de los cortes "
              "1 y 2, en las sesiones 6 y 11."},
        {"p": "¿El informe se entrega hoy o después?",
         "r": "Hoy, **dentro de la clase**. Se arma en los primeros veinticuatro minutos, se revisa "
              "con la lista de verificación y se sube antes de terminar la sesión: PDF en la carpeta "
              "del equipo y el enlace del documento. No es rigidez administrativa — es la manera de "
              "que nadie quede con una entrega pendiente después del último día."},
        {"p": "¿Cuántas páginas tiene que tener?",
         "r": "Entre **9 y 11**, con el largo por sección que está en la tabla. Y **más largo no es "
              "mejor**: un informe donde la decisión está en la página 18 es un informe que no se va "
              "a leer. Lo que se califica es que cada sección tenga lo que le corresponde, no la "
              "cantidad de texto."},
        {"p": "No usamos IA en el proyecto. ¿Igual escribimos esa sección?",
         "r": "Sí, y con una línea basta: «no usamos asistentes de IA en ninguna etapa». **Declarar "
              "es obligatorio; usarla o no es su decisión**, y las dos opciones son igual de válidas. "
              "La sección vale los mismos puntos si dice honestamente que no se usó."},
        {"p": "¿La autoevaluación la ve el equipo?",
         "r": "No. La **individual llega solo al docente** — sin esa garantía nadie responde con "
              "honestidad la pregunta de en qué falló. La **coevaluación** sí la escribe cada "
              "integrante sobre los demás, y también la recibe solo el docente; no se lee en clase ni "
              "se discute en público."},
        {"p": "¿Ponerme buena nota en la autoevaluación me ayuda?",
         "r": "Al contrario: **ponerse la nota máxima sin evidencia baja el puntaje**. Lo que se "
              "evalúa no es la nota que uno se pone, es si puede mirar su propio trabajo con "
              "honestidad y con hechos. Reconocer un fallo concreto —«entregué tarde dos veces»— saca "
              "más que «cumplí con todo»."},
    ],

    "notas_operativas": [
        "**Última sesión. Reparto propio:** apertura 6 · informe 24 · galería 20 · autoevaluación y "
        "coevaluación 20 · cierre del curso 20.",
        "**Diga en el minuto 3 que no hay examen final escrito.** La mitad del curso llega "
        "esperándolo, y saberlo cambia cómo usan los veinticuatro minutos del informe.",
        "**No lea completas las dos tablas de secciones**: son doce filas y aburre. Señale tres o "
        "cuatro y deje que el curso vea el patrón de la columna del medio.",
        "En las salas, entre con una sola pregunta: **«¿qué secciones están en rojo y quién tomó cada "
        "una?»**.",
        "Recuerde en voz alta la sección que más se olvida: **la 11**, y dentro de ella **la lluvia de "
        "ideas asistida de la sesión 3**, que casi todos declaran solo del prototipo de la 11.",
        "**Revise la sección 8 buscando nombres de personas.** Es donde más se rompe la regla de la "
        "sesión 4: va el rol, no el nombre. Pídalo corregido antes de cerrar la nota.",
        "**Verifique la entrega antes de pasar a la galería:** PDF en la carpeta del equipo y enlace "
        "del documento. Después del bloque ya nadie vuelve al informe.",
        "Aclare que la galería **no es exponer otra vez** —la nota fue la sesión 15— y que sirve para "
        "ver los cinco proyectos lado a lado, que es la única vez en el semestre.",
        "**Proyecte la tabla de respuestas que sirven y que no sirven ANTES de que escriban la "
        "autoevaluación**: reduce a la mitad las respuestas genéricas.",
        "Diga que **la autoevaluación individual llega solo al docente**, antes de que empiecen. Sin "
        "esa garantía, «¿en qué fallé?» se responde siempre con «en nada».",
        "**Si estalla un conflicto en la coevaluación, no lo resuelva en público.** Recoja, cierre el "
        "bloque y hable después por separado.",
        "Para el cierre, **tenga a mano las respuestas reales de la prueba diagnóstica de la sesión "
        "1**. El efecto está en que sean suyas, no parafraseadas.",
        "Cierre en veinte minutos sin discurso: **se llevan un método, no un tema**, y **el proyecto "
        "queda como evidencia de portafolio**.",
    ],

    # El builder usa `ti_siguiente` para la diapositiva «Cierre del curso» de la ultima
    # sesion: tid = lo que queda entregado, ti = autoevaluacion, adelanto = frase de cierre,
    # aviso = lo ultimo que hay que decir. No existe una sesion 17.
    "ti_siguiente": {
        "tid": "el **informe final** con sus doce secciones (20 %), la **exposición final** de la "
               "sesión 15 (15 %), el prototipo probado con personas reales y la galería del curso.",
        "ti": "queda hecha, con evidencia y no con impresiones — junto con la coevaluación del equipo.",
        "adelanto": "Lo que se llevan es un método, no un tema: definir un problema con evidencia, "
                    "revisar qué ya existe, decidir con criterios, probar con personas reales y mirar "
                    "a quién afecta.",
        "aviso": "El informe y las capturas quedan en la carpeta del equipo: es un proyecto completo "
                 "y documentado, hecho en primer semestre, y sirve para un portafolio. Y **el "
                 "siguiente paso de su proyecto está escrito en la sección 10** — quien quiera "
                 "continuarlo ya no tiene que decidir por dónde empezar.",
    },

    # Ojo: la diapositiva anterior ya se titula «Cierre del curso» (la genera el builder
    # para la ultima sesion), asi que aqui no se repite ese titulo.
    "cierre_titulo": "Gracias · Introducción a la Ingeniería",
    "cierre_frase": "Hace dieciséis sesiones era una ocurrencia; hoy es un proyecto con evidencia",
}
