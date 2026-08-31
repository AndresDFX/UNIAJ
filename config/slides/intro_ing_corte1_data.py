# -*- coding: utf-8 -*-
"""Contenido de las clases 2 a 6 de Introduccion a la Ingenieria (FI300101) · Corte 1.

Este modulo SI lleva tildes: casi todo su texto acaba proyectado o convertido a .docx.
Nunca usar comillas dobles escapadas dentro de estos textos: se usan « ».

Material general para los tres grupos: nada de fechas, horas de pared ni codigos de grupo.

Corte 1 (30%) cierra en la sesion 6, que es la que entrega el problema del proyecto del
semestre. Todo lo de las clases 2 a 5 esta puesto para que ese problema salga bien escrito.
"""

TEMAS = {}

# =============================================================================
# CLASE 2 · Historia y evolucion de la Ingenieria
# =============================================================================

TEMAS[2] = {
    "n": 2,
    "titulo": "Historia y evolución de la Ingeniería",
    "subtitulo": "Por qué los problemas de 1968 siguen siendo los suyos",
    "hook": "Un proyecto de software se pasa del plazo y del presupuesto. "
            "¿Es un problema de 2026 o de 1968?",
    "hook_lines": [
        "La respuesta honesta es: exactamente el mismo, y con las mismas causas.",
        "Hoy vamos a ver de dónde salieron esas causas y por qué nadie las ha eliminado.",
    ],
    "objetivos": [
        "Ubicar **seis hitos** de la historia de la disciplina y decir qué problema resolvía cada uno.",
        "Explicar por qué la ingeniería de sistemas **nace como respuesta a un fracaso**, no a un avance técnico.",
        "Construir una **línea de tiempo** en una herramienta de diagramación en la nube.",
        "Identificar, para un hito, **qué parte de ese problema sigue vivo hoy**.",
    ],
    "agenda": {
        "Teoría y guía del docente": "Teoría — seis hitos y el problema que resolvía cada uno",
        "Actividad en equipos": "Taller — línea de tiempo del periodo en draw.io",
        "Exposiciones": "5 equipos × 3 min — la línea de tiempo, en orden histórico",
    },
    "herramienta_nota": "El taller se hace en **diagrams.net (draw.io)**, que abre sin cuenta y "
                        "guarda directo en la carpeta del equipo en Drive. Si alguien no logra "
                        "abrirlo, la línea de tiempo se puede armar en Google Slides con cuadros "
                        "de texto: lo que se evalúa es el contenido de los hitos, no el diseño.",
    "avance_proyecto": "Entender que el problema del proyecto tiene que ser un problema real y "
                       "medible, porque los proyectos que fracasaron en la historia fracasaron "
                       "por no tener eso",

    "teoria": [
        {
            "tipo": "before_after",
            "titulo": "Cómo se cuenta la historia y cómo fue",
            "before_title": "Lo que se suele contar",
            "before": [
                "«Todo empezó con los computadores».",
                "«Cada década llegó una tecnología mejor».",
                "«Antes era difícil porque las máquinas eran lentas».",
                "«Los métodos de trabajo son un invento reciente».",
                "«Los problemas viejos ya se resolvieron».",
            ],
            "after_title": "Lo que muestran los hechos",
            "after": [
                "Empezó con **proyectos que fracasaron** siendo la máquina lo de menos.",
                "Cada década llegó **un problema nuevo de escala**, no un juguete nuevo.",
                "Era difícil porque **nadie sabía cómo organizar el trabajo de 100 personas**.",
                "El primer método formal es de **1970**, y nació de un artículo crítico.",
                "Los problemas viejos **siguen abiertos**: plazo, costo y requisitos que cambian.",
            ],
            "size": 13,
        },
        {
            "tipo": "content",
            "titulo": "Cuándo el problema dejó de ser la máquina",
            "items": [
                "@@Años 40 y 50:@@ el cuello de botella es el **hardware**. Programar es escribir "
                "instrucciones para una máquina concreta, y el trabajo es de una persona o de "
                "unas pocas.",
                "@@Años 60:@@ el hardware se abarata y crece, y aparecen sistemas que necesitan "
                "**cientos de personas y años de trabajo**. Ahí el cuello de botella se muda: ya "
                "no es la máquina, es **coordinar el trabajo humano**.",
                "El sistema de reservas SABRE, el software del programa Apollo y el sistema "
                "operativo OS/360 de IBM son los tres casos que hicieron visible el problema: "
                "**se pasaron de plazo y de presupuesto de forma escandalosa**.",
                "@@1968:@@ la OTAN convoca una conferencia en Garmisch (Alemania) para hablar de "
                "eso y se acuña el término **«ingeniería de software»**. El nombre es una "
                "propuesta: si construir software se parece a construir un puente, entonces "
                "necesita **método, no talento individual**.",
                "**Ahí nace la disciplina:** no de un invento, sino del reconocimiento público de "
                "que el trabajo se estaba haciendo mal y nadie sabía cómo hacerlo bien.",
            ],
            "size": 14,
        },
        {
            "tipo": "cards",
            "titulo": "Seis hitos y el problema que atacaba cada uno",
            "cards": [
                ("1945–1957 · La máquina programable",
                 "Arquitectura de von Neumann y los primeros lenguajes (Fortran, 1957). "
                 "**Problema:** decirle algo a la máquina sin hablar su idioma binario."),
                ("1968 · La crisis del software",
                 "Conferencia de la OTAN en Garmisch. Se nombra el problema: los proyectos "
                 "grandes fracasan. **Problema:** organizar trabajo humano a escala."),
                ("1970 · El ciclo de vida",
                 "Royce publica el esquema que se popularizó como «cascada» — advirtiendo que "
                 "así, sin iterar, no funciona. **Problema:** ¿en qué orden se hace el trabajo?"),
                ("1975 · El mes-hombre mítico",
                 "Brooks: meter más gente a un proyecto atrasado lo atrasa más. **Problema:** "
                 "la comunicación crece más rápido que el equipo."),
                ("1991–2001 · Software libre y agilidad",
                 "Linux y luego el Manifiesto Ágil. **Problema:** los requisitos cambian mientras "
                 "se construye, y el plan rígido se vuelve mentira."),
                ("2006–hoy · La nube y los datos",
                 "Infraestructura alquilada por horas e IA en producción. **Problema:** ya no es "
                 "poder construirlo, es **decidir si se debe** y quién responde."),
            ],
            "columns": 3,
        },
        {
            "tipo": "steps",
            "titulo": "Cómo se lee un hito sin quedarse en la anécdota",
            "steps": [
                ("¿Qué dolía antes?", "El problema concreto que existía y a quién le pasaba. Sin "
                                      "esto, el hito es una fecha suelta."),
                ("¿Qué propuso?", "La idea, el método o la herramienta. En una frase, sin nombres "
                                  "técnicos que no se puedan explicar."),
                ("¿Qué resolvió de verdad?", "Casi nunca resuelve todo. Diga qué parte sí."),
                ("¿Qué sigue vivo hoy?", "El pedazo del problema que nadie ha cerrado. Es la parte "
                                         "que se evalúa en el taller."),
            ],
            "sub": "Un hito sin la cuarta pregunta es una fecha de examen; con ella es una herramienta",
        },
        {
            "tipo": "box",
            "titulo": "Tres cosas que se repiten y son falsas",
            "notas": [
                ("aclaracion",
                 "**«La cascada la inventó Royce y estaba equivocado».** Royce presentó ese "
                 "esquema en 1970 justamente para decir que aplicado de forma lineal es riesgoso, "
                 "y propuso iterar. Lo que se popularizó fue el dibujo sin la advertencia."),
                ("aclaracion",
                 "**«Ágil reemplazó al ciclo de vida».** No: ágil cambia el tamaño y la "
                 "frecuencia de las iteraciones. Las fases (entender, diseñar, construir, probar) "
                 "siguen ahí, solo que se recorren muchas veces en vez de una."),
                ("advertencia",
                 "**«Los problemas de 1968 ya se resolvieron».** Los informes de la industria "
                 "siguen reportando fracasos de plazo, costo y alcance en proporciones altas. "
                 "El método mejoró; el problema no desapareció."),
            ],
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada y para qué sirve incomodar con una fecha",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "La pregunta de apertura —«un proyecto de software se pasa del plazo y del "
                "presupuesto, ¿es un problema de 2026 o de 1968?»— está formulada para producir "
                "una respuesta equivocada. Casi todo el grupo va a decir que es de 2026, porque "
                "la intuición de un estudiante de primer semestre es que la historia de la "
                "tecnología es una escalera: cada década resuelve los problemas de la anterior. "
                "Esa intuición es la que hay que romper hoy, porque de ella se deriva una creencia "
                "más dañina: que basta con aprender la herramienta nueva.",
                "Los primeros diez minutos, mientras se conectan, sirven para recoger esas "
                "respuestas en el muro. No hay que corregir ninguna. En el minuto 25, cuando ya "
                "esté contada la conferencia de Garmisch de 1968, se vuelve al muro y se lee en "
                "voz alta lo que escribieron. El contraste hace el trabajo solo: el problema que "
                "el grupo cree contemporáneo tiene casi sesenta años y un nombre propio.",
            ],
        },
        {
            "titulo": "Por qué la disciplina nace de un fracaso y no de un invento",
            "slide": "{{slide:Cómo se cuenta la historia}} {{slide:Cuándo el problema dejó de ser la máquina}}",
            "cuerpo": [
                "Hay una diferencia grande entre contar la historia de la informática y contar la "
                "historia de la ingeniería de sistemas. La primera es una historia de máquinas: "
                "válvulas, transistores, circuitos integrados, microprocesadores. Es la que el "
                "estudiante espera y es la menos útil, porque sugiere que el progreso viene del "
                "hardware. La segunda es una historia de **fracasos de organización**, y es la "
                "que explica por qué existe la carrera que el estudiante está empezando.",
                "En los años cuarenta y cincuenta el cuello de botella era la máquina. Programar "
                "el ENIAC significaba reconfigurar cables físicamente; escribir en lenguaje de "
                "máquina era lento porque la máquina era lo escaso y lo caro. Fortran (1957) y "
                "COBOL (1959) atacan exactamente ese problema: permitir decirle algo a la máquina "
                "sin hablar su idioma. Hasta aquí el trabajo lo hace una persona o un puñado de "
                "personas, y el método no importa mucho porque el problema cabe en una cabeza.",
                "En los años sesenta pasa algo que cambia la naturaleza del problema: el hardware "
                "se abarata y se vuelve más capaz, y entonces se vuelven pensables sistemas que "
                "antes no lo eran. El sistema de reservas aéreas SABRE, el software de navegación "
                "del programa Apollo, el sistema operativo OS/360 de IBM. Son proyectos de "
                "cientos y hasta miles de personas y de varios años. Y fracasan de forma "
                "espectacular en plazo y en costo, no porque las máquinas fueran lentas, sino "
                "porque **nadie sabía cómo coordinar a mil personas construyendo una sola cosa "
                "que nadie puede ver ni tocar**. Fred Brooks, que dirigió el OS/360, escribió "
                "después el libro que explica por qué.",
                "En 1968 la OTAN convoca una conferencia en Garmisch para hablar del asunto, y "
                "ahí se populariza el término «ingeniería de software». Vale la pena detenerse en "
                "que el término era una **propuesta, casi una provocación**: si construir "
                "software se parece a construir un puente, entonces debería tener método, "
                "estándares, mediciones y responsabilidad profesional, en vez de depender del "
                "talento de individuos. Ese es el momento fundacional que el estudiante tiene que "
                "recordar: la disciplina no nace de una máquina nueva, nace del reconocimiento "
                "público de que se estaba trabajando mal.",
            ],
        },
        {
            "titulo": "Los seis hitos: qué decir de cada uno en dos minutos",
            "slide": "{{slide:Seis hitos}}",
            "cuerpo": [
                "La tarjeta de 1945–1957 se cuenta rápido: arquitectura de von Neumann (programa "
                "y datos en la misma memoria, que es la razón por la que un computador puede "
                "cargar cualquier programa) y los primeros lenguajes de alto nivel. El punto no "
                "es memorizar nombres, es entender que el problema de la época era **traducir**.",
                "1968 es el hito central de la clase y merece la mitad del tiempo. Se cuenta como "
                "está arriba: los tres proyectos que fracasaron, la conferencia, el término. Si "
                "el docente solo alcanza a contar un hito bien, que sea este.",
                "1970 es Winston Royce y el esquema que el mundo llamó «cascada». Aquí hay que ser "
                "preciso porque es el error histórico más repetido en las clases de ingeniería: "
                "Royce dibujó el esquema lineal para decir que **así no se debe hacer**, y "
                "propuso hacerlo dos veces, con prototipo y retroalimentación. La industria se "
                "quedó con el dibujo y tiró la advertencia. La lección para el estudiante es "
                "doble: sobre el ciclo de vida (que se ve en la sesión 7) y sobre cómo se "
                "deforman las ideas cuando se citan de segunda mano.",
                "1975 es Brooks y «The Mythical Man-Month». La idea que hay que dejar es "
                "contraintuitiva y utilísima para un curso donde se trabaja en equipos de cinco: "
                "**agregar gente a un proyecto atrasado lo atrasa más**, porque los canales de "
                "comunicación crecen mucho más rápido que las personas. Con 5 personas hay 10 "
                "parejas que se tienen que entender; con 10 personas hay 45. Es un dato "
                "verificable con una fórmula de bachillerato y explica por qué en este curso los "
                "equipos son de cinco y no de diez.",
                "1991–2001 junta software libre (Linux, y con él la idea de que miles de personas "
                "que no se conocen pueden construir algo serio si el proceso es público) y el "
                "Manifiesto Ágil de 2001. El problema que atacan es el mismo: **los requisitos "
                "cambian mientras se construye**, y un plan de dos años escrito el primer día es "
                "una obra de ficción. Ágil no elimina las fases, cambia su tamaño.",
                "2006 en adelante es la nube y los datos. Aquí el problema muda otra vez y es "
                "importante que el estudiante lo note, porque es el problema de su generación: "
                "cuando alquilar mil servidores por hora cuesta poco y una biblioteca de IA se "
                "instala en un comando, la pregunta técnica «¿se puede construir?» deja de ser la "
                "difícil. La difícil es **«¿se debe construir, a quién afecta y quién "
                "responde?»**. Esa pregunta es el hilo de las sesiones 4, 5 y 13.",
            ],
        },
        {
            "titulo": "El método de lectura de un hito y por qué la cuarta pregunta es la que se califica",
            "slide": "{{slide:Cómo se lee un hito}} {{slide:Tres cosas que se repiten}}",
            "cuerpo": [
                "Las cuatro preguntas (qué dolía, qué propuso, qué resolvió, qué sigue vivo) son "
                "el método de trabajo del taller y conviene dictarlas como método, no como "
                "curiosidad. Las tres primeras se pueden buscar; la cuarta exige pensar, y por "
                "eso es la que más pesa en la rúbrica. Un equipo puede escribir «1975: Brooks "
                "dijo que agregar gente atrasa el proyecto» y estar en lo correcto sin haber "
                "entendido nada. La cuarta pregunta obliga a decir algo como «sigue vivo porque "
                "cuando nuestro equipo se atrasó en el taller de la sesión anterior, la reacción "
                "natural fue pedir ayuda a otro equipo, y eso nos costó veinte minutos de "
                "explicar el contexto».",
                "Las tres aclaraciones de la última diapositiva de teoría hay que decirlas en voz "
                "alta aunque parezcan detalles, porque son las tres cosas que el estudiante va a "
                "encontrar mal contadas en el primer video o resumen que busque en internet. "
                "Advertirlas hoy le da una herramienta que sirve para todo el curso: **cuando una "
                "fuente cuenta una idea histórica sin decir quién la dijo y contra qué "
                "discutía, conviene desconfiar**.",
                "Sobre la tercera aclaración conviene ser honesto en el aula y no inflarla. Los "
                "informes de la industria sobre fracaso de proyectos usan definiciones distintas "
                "de «fracaso» y sus cifras varían mucho entre ediciones y entre fuentes. Lo que "
                "sí se puede afirmar sin exagerar es que **el fracaso por plazo, costo y alcance "
                "sigue siendo un problema reportado sistemáticamente**, y que ninguna metodología "
                "ha declarado el problema cerrado. Si un equipo trae una cifra de internet, se le "
                "pide la fuente y el año: es el primer ejercicio de rigor bibliográfico del curso.",
            ],
        },
        {
            "titulo": "El taller, la exposición y por qué las cinco líneas de tiempo se suman",
            "slide": "{{slide:Taller de hoy}} {{slide:Cómo se expone}}",
            "cuerpo": [
                "Cada equipo recibe un periodo distinto y arma su tramo de línea de tiempo. La "
                "consecuencia es que las cinco exposiciones, puestas en orden histórico, "
                "producen la línea de tiempo completa de la disciplina, que es justo el trabajo "
                "independiente de la semana. Esto hay que decírselo al grupo antes de empezar: no "
                "están haciendo cinco trabajos que compiten, están armando un solo mapa por "
                "pedazos, y el pedazo de cada uno le sirve a los otros cuatro.",
                "Por eso las exposiciones van **en orden histórico y no por sorteo**: el equipo "
                "del periodo 1945–1957 abre y el de 2006–hoy cierra. Cuesta lo mismo y el grupo "
                "se lleva una narración en vez de cinco fragmentos. El docente escribe el orden "
                "en el chat antes de que empiecen.",
                "El taller pide cuatro hitos por periodo, no más. La tentación del equipo será "
                "meter diez fechas para verse completo, y el resultado es una línea de tiempo que "
                "nadie puede exponer en tres minutos. Cuatro hitos bien leídos, con su «qué sigue "
                "vivo», valen mucho más y es lo que la rúbrica premia.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:10 · Apertura · [Slide 4]",
            "cuerpo": [
                "Entre a Meet 5 min antes y comparta pantalla con la pregunta de entrada antes de "
                "que entre el primer estudiante:",
                "> «Un proyecto de software se pasa del plazo y del presupuesto. ¿Es un problema "
                "de 2026 o de 1968?»",
                "**[Nota docente]:** el enlace del muro de Padlet va en el chat de Meet. No "
                "corrija ninguna respuesta ahora: el valor de este muro está en releerlo en el "
                "minuto 25, cuando ya se haya contado Garmisch.",
                "**[Nota docente]:** confirme que las cinco salas de grupo están creadas y que "
                "cada equipo tiene su documento de la sesión 1 a mano — hoy se trabaja en el "
                "mismo documento, en una pestaña nueva.",
            ],
        },
        {
            "titulo": "00:10–00:55 · Teoría · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]",
            "cuerpo": [
                "Reparto sugerido de los 45 min:",
                "- **8 min** · Cómo se cuenta la historia y cómo fue [Slide 5]. Es el "
                "desmontaje de la idea de escalera.",
                "- **12 min** · Cuándo el problema dejó de ser la máquina [Slide 6]. Aquí va "
                "Garmisch 1968, que es el corazón de la clase. Al terminar, **vuelva al muro de "
                "Padlet** y lea dos o tres respuestas: el problema que creían de 2026 tiene "
                "cincuenta y ocho años.",
                "- **15 min** · Los seis hitos [Slide 7], unos dos minutos y medio por tarjeta. "
                "Si el tiempo aprieta, recorte 1945–1957 y 1991–2001, nunca 1968 ni 1975.",
                "- **6 min** · Cómo se lee un hito [Slide 8]. Se dicta como método porque es lo "
                "que van a aplicar en 17 minutos.",
                "- **4 min** · Las tres cosas falsas [Slide 9].",
                "**[Nota docente]:** la aritmética de Brooks se explica en treinta segundos y se "
                "queda: 5 personas son 10 parejas que se tienen que entender; 10 personas son 45. "
                "Es la razón por la que los equipos de este curso son de cinco.",
            ],
        },
        {
            "titulo": "00:55–01:12 · Taller en salas de grupo · [Slide 10]",
            "cuerpo": [
                "**3 min** para repartir periodos y abrir la herramienta. El periodo de cada "
                "equipo **no se sortea hoy**: se asigna en orden, del equipo 1 al 5, para que las "
                "exposiciones queden en orden histórico sin reorganizar nada.",
                "**14 min** de trabajo con los equipos ya en sus salas. Entre a las cinco salas "
                "con un orden fijo, unos 3 min en cada una, y en cada entrada revise **una sola "
                "cosa: el «qué sigue vivo hoy»**. Los otros tres campos los pueden buscar; ese no.",
                "**[Nota docente]:** si un equipo se atasca con draw.io más de dos minutos, "
                "mándelo a Google Slides con cuadros de texto y siga. La herramienta no es lo "
                "evaluado y perder cinco minutos en una interfaz arruina el taller.",
                "**[Nota docente]:** cuando un equipo escriba una cifra de internet («el 70 % de "
                "los proyectos fracasa»), pida fuente y año en el documento. Es el primer "
                "ejercicio de rigor bibliográfico del curso y se vuelve a pedir en la sesión 9.",
            ],
        },
        {
            "titulo": "01:12–01:27 · Exposiciones · [Slide 11]",
            "cuerpo": [
                "**En orden histórico**, equipo 1 a equipo 5. Escriba el orden en el chat antes "
                "de empezar. 3 min por equipo, cronómetro en pantalla, habla el vocero con el "
                "diagrama ya compartido.",
                "**[Nota docente]:** exija los cinco enlaces pegados en el chat antes de que "
                "empiece la primera exposición. Compartir pantalla con el cronómetro corriendo se "
                "come el turno.",
                "**[Nota docente]:** no dé retroalimentación equipo por equipo. Anote y guarde "
                "todo para el cierre; cinco rondas de comentarios no caben en 15 min.",
            ],
        },
        {
            "titulo": "01:27–01:30 · Cierre · [Slide 12][Slide 13]",
            "cuerpo": [
                "Una sola idea: **la disciplina nació de un fracaso de organización, no de un "
                "invento**, y los problemas de plazo, costo y requisitos que cambian siguen "
                "abiertos. El curso entero está puesto para que ellos no los repitan por "
                "ignorancia.",
                "Anuncie el trabajo independiente y el tema de la sesión 3, y pida los enlaces "
                "en el chat.",
            ],
        },
    ],

    "taller": {
        "archivo": "Linea de tiempo del periodo",
        "titulo": "Línea de tiempo del periodo",
        "min": 17,
        "exposicion": 3,
        "consigna": "A su equipo le corresponde un periodo de la historia de la Ingeniería de "
                    "Sistemas. Armen la línea de tiempo de **ese periodo** con **cuatro hitos**, "
                    "y para cada hito respondan las cuatro preguntas del método. No metan más de "
                    "cuatro: una línea de tiempo con diez fechas no se puede exponer en 3 min y "
                    "no se califica mejor.",
        "entregable": "un diagrama de línea de tiempo con 4 hitos en diagrams.net (draw.io), "
                      "guardado en la carpeta del equipo en Drive, más las cuatro respuestas "
                      "escritas por hito en el documento del equipo",
        "entregable_corto": "línea de tiempo de 4 hitos en draw.io",
        "reparto_titulo": "El periodo no se elige:",
        "reparto": "se asigna por número de equipo, del 1 al 5, en orden histórico. Así las cinco "
                   "exposiciones puestas en fila producen la línea de tiempo completa de la "
                   "disciplina, que es el trabajo independiente de esta semana.",
        "reparto_corto": "un periodo por equipo, asignado en orden histórico",
        "bloques": [
            {"clave": "LOS CUATRO HITOS",
             "pide": "Cuatro hechos de su periodo, con año, puestos en orden en la línea de tiempo.",
             "check": "son cuatro, tienen año y están en orden. Ni tres ni diez."},
            {"clave": "QUÉ DOLÍA ANTES",
             "pide": "Para cada hito: el problema concreto que existía antes y a quién le pasaba.",
             "check": "es un problema, no una carencia de tecnología. «No había internet» no es un problema; «un banco no podía saber el saldo de una cuenta desde otra ciudad» sí."},
            {"clave": "QUÉ PROPUSO",
             "pide": "Para cada hito: la idea, el método o la herramienta, en una frase que ustedes puedan explicar.",
             "check": "no hay términos que el equipo no sepa explicar si se le pregunta."},
            {"clave": "QUÉ SIGUE VIVO HOY",
             "pide": "Para **al menos dos** de los cuatro hitos: qué parte de ese problema todavía "
                     "no está resuelta, con un ejemplo de algo que ustedes hayan visto.",
             "check": "el ejemplo es concreto y propio. «Sigue vigente» sin ejemplo no cuenta."},
            {"clave": "LA FUENTE",
             "pide": "De dónde sacaron cada dato: autor o institución, y año. Si usaron una cifra "
                     "(«el 70 % de los proyectos…»), la fuente es obligatoria.",
             "check": "hay fuente por hito. Un enlace pegado sin autor ni año no es una fuente."},
        ],
        "expo": [
            ("45 s · El periodo y qué dolía", "Qué años les tocaron y cuál era el problema de la época."),
            ("60 s · Los cuatro hitos", "En orden, con año. Una frase por hito, sin leer la pantalla."),
            ("60 s · Qué sigue vivo", "Los dos hitos cuyo problema no está cerrado, con su ejemplo propio. Es lo que más pesa."),
            ("15 s · Las fuentes", "De dónde salió lo que dijeron."),
        ],
    },

    "rubrica": [
        ("Los cuatro hitos están, con año y en orden", 20,
         "Es el mínimo verificable del entregable: sin esto no hay línea de tiempo."),
        ("«Qué dolía antes» está escrito como problema, no como falta de tecnología", 25,
         "Es la habilidad que el curso entero entrena y la que se evalúa en la sesión 6."),
        ("«Qué sigue vivo hoy» en al menos dos hitos, con ejemplo propio", 30,
         "Es lo único que no se puede copiar de internet, y por eso es lo que más pesa."),
        ("Fuentes con autor o institución y año", 15,
         "Primer ejercicio de rigor bibliográfico del curso. Se vuelve a exigir en la sesión 9."),
        ("La exposición cupo en 3 min y habló el vocero", 10,
         "El presupuesto de 15 min de exposiciones no se puede estirar."),
    ],

    "solucion": {
        "para_que": "Este documento resuelve el taller completo para **un** periodo, el de "
                    "1968–1975, que es el más difícil de los cinco porque sus hitos son ideas y "
                    "no aparatos. Sirve para tres cosas: ver el nivel de detalle que se espera, "
                    "tener respuesta lista si un equipo se atasca, y calificar con un referente "
                    "en vez de con una impresión. Al final hay una nota por cada uno de los "
                    "otros cuatro periodos con lo que no puede faltar.",
        "caso_titulo": "Periodo 1968–1975 · De la crisis del software al mes-hombre mítico",
        "caso": "Es el periodo del equipo 2. Se eligió para esta solución porque es donde los "
                "equipos fallan más: los hitos no son máquinas que se puedan describir, son "
                "**artículos y conferencias**, y el estudiante de primer semestre tiende a "
                "escribir «en 1968 hubo una conferencia» sin poder decir de qué se habló ni por "
                "qué importa.",
        "por_que_este_caso": "Si el docente solo alcanza a leer una parte de este documento antes "
                             "de clase, que sea el bloque «QUÉ SIGUE VIVO HOY»: es el que decide "
                             "el 30 % de la nota y el que casi ningún equipo hace bien sin ayuda.",
        "bloques": [
            {
                "clave": "LOS CUATRO HITOS",
                "respuesta": "**1968 · Conferencia de la OTAN en Garmisch, Alemania.** Se reúne un "
                             "grupo de académicos e ingenieros de la industria a discutir por qué "
                             "los grandes proyectos de software fracasan, y se populariza el "
                             "término «ingeniería de software».\n\n"
                             "**1968 · «Go To Statement Considered Harmful», de Edsger Dijkstra.** "
                             "Un artículo de dos páginas que sostiene que cierta forma de escribir "
                             "programas los vuelve imposibles de entender, y propone la "
                             "programación estructurada.\n\n"
                             "**1970 · «Managing the Development of Large Software Systems», de "
                             "Winston Royce.** El artículo que contiene el esquema que después se "
                             "llamó «cascada», presentado con la advertencia de que en forma "
                             "puramente lineal es riesgoso.\n\n"
                             "**1975 · «The Mythical Man-Month», de Fred Brooks.** El libro donde "
                             "el director del OS/360 de IBM explica por qué su propio proyecto se "
                             "atrasó, y formula que agregar gente a un proyecto atrasado lo atrasa "
                             "más.",
                "como_calificar": "20 pts si están los cuatro con año y en orden. Se acepta "
                                  "cambiar Dijkstra por «1969 · primer nodo de ARPANET» o por «1972 "
                                  "· C y Unix», que también caen en el periodo. **No** se acepta "
                                  "meter 1991 (Linux) ni 2001 (ágil): están fuera del periodo y es "
                                  "la señal de que el equipo no leyó su asignación. Reste 5 pts por "
                                  "hito sin año.",
            },
            {
                "clave": "QUÉ DOLÍA ANTES",
                "respuesta": "**Garmisch 1968:** proyectos como el sistema operativo OS/360 de IBM "
                             "y el software del programa Apollo movían cientos o miles de personas "
                             "y varios años, y se pasaban de plazo y de presupuesto de forma "
                             "escandalosa. Le dolía a quien pagaba —empresas y gobiernos— y a los "
                             "propios equipos, que trabajaban sin saber si iban bien. No existía "
                             "manera de estimar, medir el avance ni repartir el trabajo.\n\n"
                             "**Dijkstra 1968:** los programas se escribían con saltos libres de un "
                             "punto a otro del código. Le dolía a quien tenía que corregir un "
                             "programa que no había escrito: seguir el flujo era casi imposible, "
                             "así que un error pequeño costaba días.\n\n"
                             "**Royce 1970:** no había una respuesta compartida a «¿en qué orden se "
                             "hace el trabajo?». Cada proyecto grande improvisaba su propio orden, "
                             "y le dolía al cliente, que no tenía en qué momento revisar nada ni "
                             "con qué comparar lo prometido.\n\n"
                             "**Brooks 1975:** cuando un proyecto se atrasaba, la reacción "
                             "administrativa era contratar más programadores. Le dolía a todos, "
                             "porque el atraso empeoraba y nadie entendía por qué.",
                "como_calificar": "25 pts. Lo que se califica es que esté escrito como **problema "
                                  "que le pasa a alguien**, no como carencia. «No había métodos» es "
                                  "una carencia y vale la mitad; «el cliente no tenía en qué "
                                  "momento revisar nada» es un problema y vale completo. Exija el "
                                  "«a quién le pasaba» en los cuatro hitos: es el hábito que se "
                                  "evalúa en la sesión 6.",
            },
            {
                "clave": "QUÉ PROPUSO",
                "respuesta": "**Garmisch:** tratar la construcción de software como una ingeniería "
                             "—con método, medición, estándares y responsabilidad profesional— en "
                             "vez de depender del talento de individuos.\n\n"
                             "**Dijkstra:** escribir programas con tres estructuras claras "
                             "(secuencia, decisión y repetición) en vez de saltos libres, para que "
                             "el programa se pueda leer de arriba abajo y razonar sobre él.\n\n"
                             "**Royce:** hacer el trabajo en fases identificables, cada una con un "
                             "producto que se pueda revisar, y —esta es la parte que la industria "
                             "olvidó— **recorrerlas dos veces**, usando la primera pasada como "
                             "prototipo para aprender.\n\n"
                             "**Brooks:** la comunicación crece mucho más rápido que el equipo, así "
                             "que agregar gente a un proyecto atrasado le agrega coordinación y lo "
                             "atrasa más. Corolario: hay trabajo que no se puede paralelizar.",
                "como_calificar": "20 pts. El criterio es **que el equipo pueda explicar la frase "
                                  "sin leerla**. Pregúntele al vocero qué significa «programación "
                                  "estructurada» o «no se puede paralelizar»: si no lo sabe, es una "
                                  "frase copiada y vale la mitad. Se acepta lenguaje coloquial "
                                  "correcto; no se acepta jerga sin comprensión.",
            },
            {
                "clave": "QUÉ SIGUE VIVO HOY",
                "respuesta": "**De Brooks (el más fácil de aterrizar):** sigue vivo entero. Cinco "
                             "personas son diez parejas que se tienen que entender; diez personas "
                             "son cuarenta y cinco. Un ejemplo propio y verificable: en el taller "
                             "de la sesión 1 el equipo tuvo 14 minutos; si en el minuto 10 hubiera "
                             "entrado un integrante nuevo, habría habido que contarle todo el "
                             "contexto y el equipo habría terminado con menos, no con más. Es la "
                             "razón declarada por la que los equipos de este curso son de cinco.\n\n"
                             "**De Garmisch:** sigue vivo el problema de fondo, que es estimar y "
                             "medir avance en algo que no se ve. Ejemplo propio: cuando un equipo "
                             "dice «ya casi terminamos el documento», nadie puede verificar ese "
                             "«casi». Es exactamente el problema de 1968 en escala de 17 minutos, "
                             "y es el que se ataca en la sesión 7 con hitos y entregables.\n\n"
                             "**De Royce:** sigue vivo el malentendido. Cualquier búsqueda rápida "
                             "presenta la cascada como un método malo que Royce propuso, cuando el "
                             "artículo dice lo contrario. Ejemplo propio: comparen dos resúmenes de "
                             "internet sobre la cascada y verán que ninguno cita la advertencia.\n\n"
                             "**De Dijkstra:** está en buena parte resuelto, y decirlo es correcto. "
                             "Los lenguajes actuales ya no ofrecen saltos libres; lo que sobrevive "
                             "es la idea general de que **el código se escribe para que otro humano "
                             "lo lea**.",
                "como_calificar": "30 pts, el bloque que decide la nota. Exija **dos hitos como "
                                  "mínimo y un ejemplo propio en cada uno**. «Sigue vigente porque "
                                  "los proyectos todavía se atrasan» es una afirmación sin ejemplo "
                                  "y vale 10 de 30. Un ejemplo tomado de la experiencia del propio "
                                  "equipo en este curso vale completo: es la señal de que "
                                  "entendieron. Vale también reconocer que Dijkstra está resuelto: "
                                  "distinguir lo cerrado de lo abierto es parte de la habilidad.",
            },
            {
                "clave": "LA FUENTE",
                "respuesta": "Para este periodo las fuentes primarias existen y son cortas: las "
                             "actas de la conferencia de Garmisch de 1968 (Naur y Randell, "
                             "editores), el artículo de Dijkstra en Communications of the ACM "
                             "(1968), el de Royce en las actas de la IEEE WESCON (1970) y el libro "
                             "de Brooks (Addison-Wesley, 1975). Lo aceptable en primer semestre es "
                             "**autor o institución + año**, no una cita en formato APA completo.",
                "como_calificar": "15 pts. Un enlace pegado sin autor ni año vale 0 en ese hito. Si "
                                  "el equipo usó una cifra de fracaso de proyectos y no trae "
                                  "fuente, reste todo el bloque y dígalo en voz alta: es el punto "
                                  "donde el curso empieza a exigir rigor, y es más útil que se "
                                  "note hoy que en la sesión 9.",
            },
        ],
        "variantes": [
            {"caso": "Periodo 1945–1957 · Equipo 1",
             "clave": "Hitos esperables: ENIAC (1945), arquitectura de von Neumann (1945), "
                      "el primer «bug» documentado de Grace Hopper y su trabajo en compiladores, "
                      "Fortran (1957). Lo que **no** puede faltar: que el problema de la época era "
                      "**traducir** —hablarle a la máquina sin usar su idioma— y que el trabajo "
                      "cabía en pocas personas. Error típico: contar la historia del hardware sin "
                      "decir qué problema humano resolvía."},
            {"caso": "Periodo 1976–1990 · Equipo 3",
             "clave": "Hitos esperables: el computador personal (Apple II 1977, IBM PC 1981), las "
                      "primeras bases de datos relacionales comerciales sobre el modelo de Codd, "
                      "el modelo en espiral de Boehm (1988), la aparición de los estándares IEEE "
                      "de software. Lo que **no** puede faltar: el problema muda a **muchos "
                      "usuarios que no son técnicos**, y con eso nace el requisito de usabilidad. "
                      "Error típico: quedarse en las marcas de computadores."},
            {"caso": "Periodo 1991–2005 · Equipo 4",
             "clave": "Hitos esperables: la web (1991), Linux (1991), los patrones de diseño "
                      "(1994), el Manifiesto Ágil (2001). Lo que **no** puede faltar: el problema "
                      "es que **los requisitos cambian mientras se construye**, y que ágil no "
                      "elimina las fases sino que las hace pequeñas y repetidas. Error típico: "
                      "presentar ágil como «trabajar sin plan»."},
            {"caso": "Periodo 2006–hoy · Equipo 5",
             "clave": "Hitos esperables: la nube como servicio por horas (AWS, 2006), el "
                      "teléfono inteligente como plataforma (2007–2008), DevOps y la entrega "
                      "continua, la IA generativa en producción (2022 en adelante). Lo que **no** "
                      "puede faltar: cuando construir se vuelve barato, la pregunta difícil deja "
                      "de ser «¿se puede?» y pasa a ser **«¿se debe, a quién afecta y quién "
                      "responde?»**. Error típico: convertirlo en una lista de productos."},
        ],
        "cierre": "Tres minutos, una sola idea: **la ingeniería de sistemas nació de un fracaso de "
                  "organización, no de un invento técnico.** En 1968 se reconoció en público que "
                  "no se sabía coordinar el trabajo de mil personas construyendo algo invisible, y "
                  "de ahí salieron el método, las fases y los estándares. Cierre con la aritmética "
                  "de Brooks porque los toca directamente: cinco personas son diez parejas que se "
                  "tienen que entender, diez personas son cuarenta y cinco, y por eso los equipos "
                  "de este curso son de cinco y no de diez. Y anuncie la sesión 3 con una pregunta "
                  "abierta: si el problema de fondo es coordinar y entender, entonces hay que "
                  "aprender a mirar un sistema completo y no solo su software.",
        "conexion": "Hacia atrás: la sesión 1 dejó cinco problemas del entorno escritos, y hoy se "
                    "vio que los proyectos que fracasan en la historia fracasan por no tener el "
                    "problema bien planteado. Hacia adelante: la sesión 7 retoma a Royce para el "
                    "ciclo de vida, la sesión 9 vuelve sobre las fuentes y el rigor bibliográfico, "
                    "y la sesión 6 —cierre del corte— exige el problema del proyecto escrito con "
                    "el mismo criterio que hoy se le exigió a «qué dolía antes».",
    },

    "errores": [
        {"dice": "«Antes no había internet / no había computadores»",
         "por_que": "Es una carencia de tecnología, no un problema.",
         "pida": "Qué no podía hacer una persona concreta por eso. «Un banco no podía consultar un saldo desde otra ciudad»."},
        {"dice": "«En 1968 hubo una conferencia importante»",
         "por_que": "No dice de qué se habló ni por qué importó.",
         "pida": "El problema que llevó a convocarla y la palabra que salió de ahí."},
        {"dice": "«Royce inventó la cascada y estaba equivocado»",
         "por_que": "Royce propuso ese esquema advirtiendo que lineal es riesgoso.",
         "pida": "Que lo cuenten con la advertencia incluida, y que digan de dónde sacaron la versión sin ella."},
        {"dice": "«El 70 % de los proyectos fracasa»",
         "por_que": "Es una cifra que circula sin fuente y con definiciones distintas de «fracaso».",
         "pida": "Autor o institución y año. Si no lo tienen, que lo digan como afirmación general sin número."},
        {"dice": "«Sigue vigente hoy» (sin más)",
         "por_que": "Es la parte que más pesa y así escrita no dice nada.",
         "pida": "Un ejemplo concreto que ellos hayan visto, aunque sea de este mismo curso."},
    ],

    "dudas": [
        {"p": "¿Nos van a preguntar fechas en la evaluación de corte?",
         "r": "No de memoria suelta. Lo que se evalúa es que puedan decir **qué problema resolvía** "
              "un hito y qué parte de ese problema sigue abierta. Una fecha sin problema asociado "
              "no vale nada en este curso."},
        {"p": "¿Tenemos que usar draw.io obligatoriamente?",
         "r": "No. Es la recomendada porque abre sin cuenta y guarda en Drive, pero si no les "
              "funciona, Google Slides con cuadros de texto sirve igual. Lo que se califica es el "
              "contenido de los hitos."},
        {"p": "¿Podemos usar un video de YouTube como fuente?",
         "r": "Sí, si dicen quién lo hizo y de qué año es, y si el video a su vez dice de dónde "
              "sacó los datos. Un video sin autor identificable no es fuente. En la sesión 9 se "
              "trabaja esto con más detalle."},
        {"p": "¿La línea de tiempo del trabajo independiente es la de mi equipo o la completa?",
         "r": "La completa. Cada equipo expone su tramo y con los cinco tramos se arma la línea de "
              "tiempo entera de la disciplina: esa es la que hay que dejar en la carpeta del "
              "equipo esta semana."},
    ],

    "notas_operativas": [
        "Las cinco salas de grupo se crean **antes** de empezar la sesión: abrirlas en vivo se "
        "come los 17 min del taller.",
        "El periodo de cada equipo se asigna por número de equipo, **no se sortea**, para que las "
        "exposiciones queden en orden histórico y el grupo se lleve una narración y no cinco "
        "fragmentos.",
        "Si un equipo pelea con draw.io más de dos minutos, mándelo a Google Slides. La "
        "herramienta no es lo evaluado.",
        "Esta clase es la primera vez que se exige fuente con autor y año. Dígalo explícitamente: "
        "es un criterio que se va a repetir en las sesiones 9 y 13.",
        "El muro de Padlet de la apertura se relee en el minuto 25. Si no se relee, los diez "
        "minutos de apertura se desperdiciaron.",
    ],

    "ti_siguiente": {
        "tid": "Investigación sobre hitos históricos — cada equipo completa la línea de tiempo del "
               "curso juntando los cinco tramos expuestos hoy, en la carpeta del equipo.",
        "ti": "Elaboración de línea de tiempo: la versión completa (los cinco periodos), con al "
              "menos un «qué sigue vivo hoy» por periodo.",
        "adelanto": "qué es un sistema y por qué el software es solo una parte de él. Se trabaja "
                    "con un asistente de IA, y hay que declarar el prompt usado.",
        "aviso": "Traigan la línea de tiempo completa en la carpeta del equipo. En la sesión 3 se "
                 "descompone un sistema del entorno y la línea de tiempo es el punto de partida.",
    },

    "cierre_titulo": "Nos vemos en la sesión 3",
    "cierre_frase": "La disciplina nació de un fracaso de organización, no de un invento",
}


# =============================================================================
# CLASE 3 · Fundamentos basicos de la Ingenieria de Sistemas
# =============================================================================

TEMAS[3] = {
    "n": 3,
    "titulo": "Fundamentos básicos de la Ingeniería de Sistemas",
    "subtitulo": "Qué es un sistema, y por qué el software es solo una parte",
    "hook": "¿Qué tienen en común un semáforo, la matrícula de la UNIAJC y la fila de una EPS?",
    "hook_lines": [
        "Los tres son sistemas, y en los tres el software es la parte más pequeña del problema.",
        "Hoy aprendemos a ver el sistema completo, que es lo que distingue a un ingeniero de "
        "sistemas de alguien que solo programa.",
    ],
    "objetivos": [
        "Definir **sistema** con sus cinco elementos: entradas, proceso, salidas, retroalimentación y frontera.",
        "Distinguir el **sistema** del **software** que lo soporta, y decir por qué confundirlos hace fracasar proyectos.",
        "Identificar los **actores** de un sistema, incluidos los que no lo usan pero sí lo sufren.",
        "Usar un asistente de IA para descomponer un sistema y **corregir a mano lo que inventó**.",
    ],
    "agenda": {
        "Teoría y guía del docente": "Teoría — sistema, frontera, actores y retroalimentación",
        "Actividad en equipos": "Taller — anatomía de un sistema, con IA y corrección a mano",
        "Exposiciones": "5 equipos × 3 min — el sistema y lo que la IA se inventó",
    },
    "herramienta_nota": "Es la **primera de las dos sesiones** en que el Plan de curso autoriza "
                        "usar un asistente de IA (la otra es la 11). La regla es firme y se dice "
                        "en voz alta: se entrega el **prompt usado** y **lo que se corrigió a "
                        "mano**. Una respuesta de IA pegada sin revisar no puntúa, porque el "
                        "criterio de hoy es justamente distinguir lo que la herramienta acertó de "
                        "lo que inventó. Sirve cualquier asistente en plan gratuito.",
    "avance_proyecto": "Ver el problema de la sesión 1 como un sistema completo, con actores y "
                       "frontera, en vez de como «una app que falta»",

    "teoria": [
        {
            "tipo": "steps",
            "titulo": "Los cinco elementos de un sistema",
            "steps": [
                ("ENTRADAS", "Lo que llega: datos, dinero, personas, materiales"),
                ("PROCESO", "Lo que se hace con eso. Aquí vive el software, si hay. **Casi nunca es todo el sistema**"),
                ("SALIDAS", "Lo que produce: decisiones, documentos, servicio prestado"),
                ("RETROALIMENTACIÓN", "La salida vuelve como entrada y corrige el proceso"),
                ("FRONTERA", "Qué queda dentro y qué queda fuera. La decisión más difícil, y la toma el ingeniero"),
            ],
            "sub": "Un sistema es un conjunto de partes que interactúan para un propósito. Confundir el software con el sistema es la causa más común de proyectos que funcionan y no sirven",
        },
        {
            "tipo": "before_after",
            "titulo": "Mirar el software o mirar el sistema",
            "before_title": "Mirada de programador",
            "before": [
                "«Hay que hacer una app para las citas».",
                "El usuario es quien abre la pantalla.",
                "Termina cuando el código funciona.",
                "El éxito es que no haya errores.",
                "Lo que no está en la pantalla no existe.",
            ],
            "after_title": "Mirada de ingeniero de sistemas",
            "after": [
                "«Hay 40 personas en fila a las 5 a. m. porque las citas se asignan por orden de llegada».",
                "Los actores son el paciente, la secretaria, el médico y quien paga.",
                "Termina cuando **la fila se acortó**, o se sabe por qué no.",
                "El éxito es que **el problema del entorno se redujo**, y se puede medir.",
                "Lo que pasa antes y después de la pantalla es parte del sistema.",
            ],
            "size": 13,
        },
        {
            "tipo": "cards",
            "titulo": "Cuatro conceptos que se usan todo el semestre",
            "cards": [
                ("Frontera del sistema",
                 "Qué se decide incluir y qué se deja fuera. Si la fila de la EPS empieza en la "
                 "casa del paciente, el transporte es parte del sistema. **Toda frontera es una "
                 "decisión, y hay que poder defenderla.**"),
                ("Actor (o interesado)",
                 "Cualquiera afectado por el sistema, **use o no** la pantalla. La secretaria que "
                 "digita, el médico que recibe, el vecino que ya no consigue cita. Olvidar "
                 "actores es la falla más costosa."),
                ("Requisito vs. deseo",
                 "Requisito: sin eso el sistema no sirve para su propósito. Deseo: mejoraría, y se "
                 "puede posponer. **Todo el mundo presenta sus deseos como requisitos**; separarlos "
                 "es trabajo del ingeniero."),
                ("Retroalimentación",
                 "Cuando la salida vuelve a entrar y corrige el proceso. Sin ella un sistema no "
                 "aprende: repite el mismo error para siempre y nadie se enteró."),
            ],
            "columns": 2,
        },
        {
            "tipo": "steps",
            "titulo": "Cómo se descompone un sistema en cinco pasos",
            "steps": [
                ("1 · Nombre el propósito", "Para qué existe, en una frase. Si no puede, no ha entendido el sistema."),
                ("2 · Dibuje la frontera", "Qué queda dentro y qué fuera, y por qué. Escriba la razón."),
                ("3 · Liste los actores", "Todos, incluidos los que no usan nada y sí sufren el resultado."),
                ("4 · Siga una entrada", "Tome un caso real y sígalo de la entrada a la salida. Ahí aparecen los huecos."),
                ("5 · Busque la retroalimentación", "¿Cómo se enteran de que salió mal? Si no hay respuesta, ese es el hallazgo."),
            ],
            "sub": "Es el método del taller de hoy y el que se aplica al proyecto en la sesión 6",
        },
        {
            "tipo": "box",
            "titulo": "El asistente de IA: qué hace bien y en qué miente",
            "notas": [
                ("info",
                 "**Hace bien:** darle estructura rápida a algo que usted ya entiende. Si le "
                 "describe el sistema, arma entradas, proceso y salidas en segundos, y suele "
                 "sugerir actores que a usted se le pasaron."),
                ("advertencia",
                 "**Miente con confianza en lo local y en lo cuantitativo.** Va a inventar cifras "
                 "(«el tiempo promedio de espera es de 45 minutos»), nombres de dependencias y "
                 "normas colombianas que no existen. Lo escribe con el mismo tono que lo verdadero: "
                 "**no hay señal de que está inventando**."),
                ("aclaracion",
                 "**Por eso el entregable de hoy incluye el prompt y la corrección.** Se califica "
                 "lo que ustedes detectaron que estaba mal. Un texto de IA pegado sin correcciones "
                 "no puntúa, y no por castigo: es que no muestra ningún trabajo de ingeniería."),
            ],
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada y por qué esos tres ejemplos",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "La pregunta de apertura junta un semáforo, la matrícula de la universidad y la "
                "fila de una EPS a propósito: son tres cosas que el estudiante no clasificaría "
                "junto y que comparten exactamente lo que la clase quiere mostrar. En los tres hay "
                "entradas, un proceso, salidas y personas afectadas; en los tres el software "
                "existe pero es la parte pequeña; y en los tres el problema real está en la "
                "coordinación entre partes, no en el código.",
                "El semáforo sirve para desactivar la idea de que un sistema es un programa: un "
                "semáforo mal sincronizado produce trancón aunque su temporizador funcione "
                "perfecto. La matrícula sirve porque la viven: el sistema de matrícula incluye la "
                "plataforma, pero también el pago en el banco, la cola de la ventanilla y la "
                "persona que revisa un documento. Y la fila de la EPS sirve porque es el caso "
                "donde es más visible que **un sistema puede funcionar según su diseño y ser "
                "injusto**: si las citas se asignan por orden de llegada física, el sistema está "
                "premiando a quien puede madrugar.",
            ],
        },
        {
            "titulo": "Qué es un sistema y por qué la frontera es la decisión difícil",
            "slide": "{{slide:Los cinco elementos}}",
            "cuerpo": [
                "La definición operativa que sirve para todo el curso es corta: un sistema es un "
                "conjunto de partes que interactúan para cumplir un propósito, de modo que si se "
                "le quita una parte deja de cumplirlo. Lo importante de esa definición no son las "
                "palabras sino la consecuencia: **el propósito es lo primero que hay que poder "
                "decir**. Si un equipo no puede decir para qué existe el sistema en una frase, "
                "todavía no lo entendió, y ningún diagrama lo va a salvar.",
                "Los cinco elementos se explican con un ejemplo concreto y de una sola pasada. En "
                "el sistema de citas de un consultorio: las entradas son las solicitudes de cita, "
                "la disponibilidad del médico y los datos del paciente; el proceso es asignar, "
                "confirmar y recordar; las salidas son la cita asignada, el paciente atendido y "
                "el registro de lo que pasó; la retroalimentación es que un paciente que no llegó "
                "libera un cupo y eso debería cambiar la asignación. La frontera es lo que hay "
                "que discutir: ¿el transporte del paciente es parte del sistema? Si el 30 % de "
                "las citas se pierden porque la gente no logra llegar, dejar el transporte fuera "
                "de la frontera hace que el sistema funcione en el papel y falle en la vida.",
                "Ese punto —**toda frontera es una decisión y hay que poder defenderla**— es el "
                "que hay que dejar clavado. El estudiante de primer semestre tiende a creer que "
                "la frontera viene dada por el problema. No viene dada: la pone el ingeniero, y de "
                "ella depende qué se puede mejorar. Una frontera muy estrecha produce sistemas que "
                "no sirven; una muy ancha produce proyectos que no se acaban. En la sesión 6, "
                "cuando cada equipo escriba el problema de su proyecto, la frontera va a ser el "
                "campo que más discusión genere, y hoy es donde se aprende a ponerla.",
            ],
        },
        {
            "titulo": "El sistema no es el software: la confusión que hace fracasar proyectos",
            "slide": "{{slide:Mirar el software o mirar el sistema}}",
            "cuerpo": [
                "La diapositiva del antes y después es el centro pedagógico de la sesión y "
                "conviene dictarla despacio, línea por línea, dejando que el grupo reconozca su "
                "propia forma de pensar en la columna izquierda. Casi todos llegan a primer "
                "semestre con la mirada de programador, y no por ignorancia: es la que el entorno "
                "premia. La columna derecha es la que la carrera enseña.",
                "El ejemplo de las citas médicas conviene desarrollarlo hasta el final porque "
                "muestra el fracaso completo. Un equipo con mirada de programador construye una "
                "app de citas impecable: sin errores, rápida, bonita. Y la fila de las cinco de la "
                "mañana no se mueve, porque las personas que hacen esa fila no tienen datos en el "
                "celular, o no confían en la app, o la secretaria sigue apuntando en el cuaderno "
                "porque el sistema nuevo le duplica el trabajo. El software funciona y el problema "
                "sigue. **En la lógica de este curso, ese proyecto fracasó**, y no por un error "
                "técnico.",
                "De ahí sale el criterio de éxito que se usa en todo el semestre y que hay que "
                "enunciar hoy con esas palabras: un proyecto de este curso se juzga por **si el "
                "problema del entorno se redujo y se puede medir**, no por si el prototipo "
                "funciona. Es la razón por la que el bloque «problema del entorno» pesó el 30 % en "
                "la sesión 1 y por la que la sesión 6 exige una línea base con una cifra.",
            ],
        },
        {
            "titulo": "Actores, requisitos y retroalimentación: los tres que se olvidan",
            "slide": "{{slide:Cuatro conceptos}}",
            "cuerpo": [
                "El concepto de actor hay que estirarlo más allá del usuario, porque ahí está la "
                "falla que más cuesta. En el sistema de citas los actores obvios son el paciente y "
                "la secretaria. Los que se olvidan son el médico (cuya agenda se llena distinto), "
                "quien paga el servicio (que quiere menos cupos perdidos) y **el vecino que antes "
                "conseguía cita madrugando y ahora no la consigue**. Ese último es el más "
                "importante para el curso, porque es un actor al que el sistema le empeoró la "
                "vida sin que nadie lo consultara. La sesión 13, sobre impacto social, es "
                "básicamente una hora dedicada a buscar a ese actor.",
                "Requisito contra deseo es la distinción práctica que más van a usar. La regla es "
                "operativa: es requisito si sin eso el sistema no cumple su propósito; es deseo si "
                "lo mejora. Y hay que advertir el fenómeno social: **todo el mundo presenta sus "
                "deseos como requisitos**, no por mala fe, sino porque desde dentro de su trabajo "
                "todo parece indispensable. Separarlos no es un trámite: es lo que permite "
                "entregar algo en un semestre en vez de nada en dos años.",
                "La retroalimentación es la más abstracta y la que más rinde cuando se aterriza "
                "con una pregunta única: **¿cómo se entera este sistema de que le salió mal?** En "
                "la mayoría de los sistemas del entorno que los equipos van a mirar, la respuesta "
                "honesta es «no se entera», o «se entera cuando alguien reclama». Encontrar eso ya "
                "es un hallazgo de ingeniería y suele ser la mejor oportunidad de mejora del "
                "proyecto, porque casi siempre es barata: un registro, un conteo, una pregunta al "
                "final del proceso.",
            ],
        },
        {
            "titulo": "El asistente de IA: cómo usarlo hoy sin que haga el trabajo",
            "slide": "{{slide:El asistente de IA}} {{slide:Cómo se descompone un sistema}}",
            "cuerpo": [
                "Esta es una de las dos sesiones donde el Plan de curso autoriza IA, y conviene "
                "encuadrarla bien porque de cómo se haga hoy depende cómo la usen todo el "
                "semestre. La postura del curso no es prohibirla ni celebrarla: es **usarla y "
                "verificarla**. El asistente es bueno dándole estructura a algo que el equipo ya "
                "entiende, y es bueno sugiriendo actores que se pasaron por alto. Es malo, y de "
                "una manera peligrosa, en todo lo local y lo cuantitativo.",
                "El punto que hay que subrayar es el mecanismo de la falla: el asistente **no "
                "avisa cuando está inventando**. Escribe «el tiempo promedio de espera en las EPS "
                "colombianas es de 47 minutos» con el mismo tono con que escribe algo correcto. "
                "Va a inventar cifras, nombres de dependencias municipales y números de leyes. Es "
                "exactamente el tipo de dato que un estudiante de primer semestre no puede "
                "distinguir, y por eso el entregable de hoy no es el texto de la IA: es **la "
                "lista de lo que el equipo detectó y corrigió**.",
                "Operativamente: el equipo escribe su prompt, pega la respuesta, y luego marca en "
                "el documento cada cosa que cambió y por qué. Tres correcciones bien "
                "argumentadas valen más que un texto largo. Y hay una consecuencia útil que "
                "conviene decirles: **la IA solo se puede verificar si uno sabe del tema**, así "
                "que la herramienta no reemplaza aprender el contenido, lo hace más necesario. "
                "Ese argumento funciona mejor que una prohibición.",
                "El método de cinco pasos de la otra diapositiva es el orden de trabajo del "
                "taller, y el paso 4 —seguir un caso real de la entrada a la salida— es el que "
                "produce los hallazgos. Los huecos de un sistema no aparecen mirando el diagrama; "
                "aparecen cuando uno intenta pasar un caso concreto por él y se topa con un paso "
                "que nadie sabe quién hace.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:10 · Apertura · [Slide 4]",
            "cuerpo": [
                "Comparta pantalla con la pregunta de entrada antes de que entre el primero:",
                "> «¿Qué tienen en común un semáforo, la matrícula de la UNIAJC y la fila de una EPS?»",
                "**[Nota docente]:** enlace del muro en el chat. Las respuestas van a girar en "
                "torno a «tecnología» y «son procesos». Ninguna se corrige ahora.",
                "**[Nota docente]:** recuerde que hoy se usa asistente de IA y que hay que traer "
                "la línea de tiempo de la sesión 2 en la carpeta del equipo.",
            ],
        },
        {
            "titulo": "00:10–00:55 · Teoría · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]",
            "cuerpo": [
                "Reparto sugerido de los 45 min:",
                "- **10 min** · Los cinco elementos [Slide 5], con el ejemplo de las citas del "
                "consultorio recorrido completo. Detenga la clase en **frontera** y haga la "
                "pregunta del transporte del paciente: es la que produce discusión.",
                "- **12 min** · Mirar el software o mirar el sistema [Slide 6]. Línea por línea. "
                "Cierre con el caso de la app impecable y la fila que no se movió.",
                "- **10 min** · Los cuatro conceptos [Slide 7]. En **actor**, insista en el vecino "
                "que ya no consigue cita: es el actor que se olvida siempre.",
                "- **7 min** · El método de cinco pasos [Slide 8]. Es el orden del taller.",
                "- **6 min** · El asistente de IA [Slide 9]. La regla se dice completa: prompt + "
                "correcciones, o no puntúa.",
                "**[Nota docente]:** al terminar, vuelva al muro de la apertura y muestre que "
                "«son procesos» era una respuesta a medias: son sistemas, y en los tres el "
                "software es la parte pequeña.",
            ],
        },
        {
            "titulo": "00:55–01:12 · Taller en salas de grupo · [Slide 10]",
            "cuerpo": [
                "**2 min** para repartir. Cada equipo trabaja **el sistema del problema que "
                "escribió en la sesión 1**: no se sortea nada nuevo, porque el objetivo es que ese "
                "problema madure hacia el proyecto.",
                "**15 min** de trabajo. Entre a las cinco salas, unos 3 min en cada una, y revise "
                "**una sola cosa: la frontera y su justificación**. Es el campo que decide si el "
                "proyecto va a ser abordable en un semestre.",
                "**[Nota docente]:** si un equipo pega la respuesta de la IA sin marcar "
                "correcciones, no lo deje avanzar: pídale tres verificaciones concretas antes de "
                "seguir. Es más útil cortarlo en el minuto 5 que castigarlo en la nota.",
                "**[Nota docente]:** la trampa que hay que buscar son las cifras inventadas. Si "
                "en el documento aparece «el promedio de espera es de 45 min», pregunte de dónde "
                "salió. Si salió de la IA, esa es exactamente la corrección que se califica.",
            ],
        },
        {
            "titulo": "01:12–01:27 · Exposiciones · [Slide 11]",
            "cuerpo": [
                "5 equipos × 3 min. Habla el vocero con el documento ya compartido. **El último "
                "minuto de cada exposición es obligatoriamente «qué se inventó la IA»**: es la "
                "parte que hace la sesión distinta de una clase de teoría de sistemas.",
                "**[Nota docente]:** los cinco enlaces en el chat antes de la primera exposición.",
                "**[Nota docente]:** anote los actores olvidados que aparezcan. Son material "
                "directo para la sesión 13 y conviene tener la lista.",
            ],
        },
        {
            "titulo": "01:27–01:30 · Cierre · [Slide 12][Slide 13]",
            "cuerpo": [
                "Una idea: **el sistema no es el software.** Un proyecto de este curso se juzga "
                "por si el problema del entorno se redujo y se puede medir, no por si el prototipo "
                "funciona.",
                "Anuncie la sesión 4 —principios éticos— con el gancho: hoy vimos que un sistema "
                "puede funcionar y ser injusto; la próxima se ve qué responsabilidad tiene el "
                "ingeniero cuando eso pasa.",
            ],
        },
    ],

    "taller": {
        "archivo": "Anatomia del sistema",
        "titulo": "Anatomía del sistema",
        "min": 17,
        "exposicion": 3,
        "consigna": "Tomen **el problema del entorno que su equipo escribió en la sesión 1** y "
                    "descríbanlo como sistema, con los cinco pasos del método. Úsenlo así: "
                    "primero lo piensan ustedes, después le piden al asistente de IA que lo "
                    "complete, y por último **corrigen a mano lo que la IA se inventó**. Lo que se "
                    "califica es la corrección, no el texto.",
        "entregable": "una ficha de sistema de cinco bloques en el documento del equipo, con el "
                      "prompt usado y una lista de las correcciones hechas a la respuesta de la IA",
        "entregable_corto": "ficha del sistema + prompt + correcciones",
        "reparto_titulo": "El sistema no se sortea:",
        "reparto": "cada equipo trabaja el problema que escribió en la sesión 1. La idea es que "
                   "ese problema madure hasta convertirse en el proyecto del semestre, que se "
                   "define en la sesión 6.",
        "reparto_corto": "cada equipo trabaja su propio problema de la sesión 1",
        "bloques": [
            {"clave": "PROPÓSITO Y FRONTERA",
             "pide": "Para qué existe el sistema, en una frase. Y qué queda **dentro** y qué "
                     "**fuera** de él, con la razón de cada exclusión importante.",
             "check": "la frontera tiene al menos una exclusión justificada. «Todo está dentro» no es una frontera."},
            {"clave": "ENTRADAS, PROCESO Y SALIDAS",
             "pide": "Qué entra, qué se hace con eso y qué sale. Señalen **dónde está el software**, si hay.",
             "check": "el software aparece como una parte del proceso, no como todo el sistema."},
            {"clave": "LOS ACTORES",
             "pide": "Todos los afectados, con su rol y qué le importa a cada uno. Incluyan **al "
                     "menos uno que no use el sistema pero sí sufra el resultado**.",
             "check": "hay un actor no-usuario. Es el bloque donde más se pierde nota."},
            {"clave": "LA RETROALIMENTACIÓN",
             "pide": "¿Cómo se entera este sistema de que algo salió mal? Si no se entera, "
                     "escríbanlo: es un hallazgo, no un error suyo.",
             "check": "hay una respuesta concreta, aunque sea «no se entera»."},
            {"clave": "LA IA: PROMPT Y CORRECCIONES",
             "pide": "El prompt exacto que usaron, y una lista de **al menos tres cosas que la IA "
                     "escribió mal** y cómo las corrigieron.",
             "check": "hay tres correcciones con su razón. Un texto de IA sin correcciones marcadas vale 0 en este bloque."},
        ],
        "expo": [
            ("30 s · El sistema y su propósito", "Qué sistema es y para qué existe, en una frase."),
            ("45 s · La frontera", "Qué dejaron fuera y por qué. Es la decisión que se discute."),
            ("45 s · El actor olvidado", "El afectado que no usa el sistema. Quién es y qué pierde."),
            ("60 s · Qué se inventó la IA", "Las tres correcciones. Es el minuto obligatorio de la exposición."),
        ],
    },

    "rubrica": [
        ("La frontera está definida con al menos una exclusión justificada", 20,
         "Sin frontera defendible, el proyecto del semestre no cabe en un semestre."),
        ("Entradas, proceso y salidas, con el software ubicado como una parte", 15,
         "Es la verificación de que entendieron que el sistema no es el software."),
        ("Hay un actor afectado que no usa el sistema", 25,
         "Es el actor que se olvida siempre y el que más problemas causa. Alimenta la sesión 13."),
        ("Las tres correcciones a la IA, con su razón", 30,
         "Es el criterio propio de esta sesión: verificar en vez de copiar. Sin esto no hay trabajo de ingeniería que evaluar."),
        ("La exposición cupo en 3 min e incluyó el minuto de la IA", 10,
         "El minuto de la IA es obligatorio: es lo que distingue esta exposición de un resumen teórico."),
    ],

    "solucion": {
        "para_que": "Este documento resuelve el taller completo sobre un sistema concreto —el de "
                    "préstamo de libros de una biblioteca de barrio— y muestra además **una "
                    "respuesta real de asistente de IA con sus errores señalados**, que es la "
                    "parte que el docente necesita tener lista: sin un ejemplo de cómo se ve una "
                    "corrección bien hecha, los equipos entregan «la IA se equivocó en varias "
                    "cosas» y no hay con qué calificar.",
        "caso_titulo": "Sistema de préstamo de una biblioteca de barrio",
        "caso": "El auxiliar anota los préstamos en un cuaderno: nombre, libro y fecha. No hay "
                "registro de devoluciones aparte de tachar el renglón. Cuando alguien pregunta si "
                "un libro está disponible, el auxiliar va al estante a mirar. En el último año "
                "**se perdieron dos cajas de libros** y nadie sabe quién los tenía. Es el mismo "
                "caso que se usa en la solución de la sesión 1, a propósito: permite ver cómo el "
                "mismo problema se ve distinto cuando se le aplica una herramienta nueva.",
        "por_que_este_caso": "Se eligió porque tiene los cinco elementos visibles, tiene un actor "
                            "no-usuario claro (quien nunca encuentra el libro porque está prestado "
                            "y no figura) y su retroalimentación **no existe**, que es el hallazgo "
                            "más frecuente y el más rentable.",
        "bloques": [
            {
                "clave": "PROPÓSITO Y FRONTERA",
                "respuesta": "**Propósito:** que los libros de la biblioteca lleguen a quien los "
                             "necesita y vuelvan al estante.\n\n"
                             "**Dentro de la frontera:** el estante y su contenido, el cuaderno de "
                             "préstamos, el auxiliar, el lector que pide, el acto de entregar y el "
                             "de devolver.\n\n"
                             "**Fuera de la frontera, con su razón:** (a) la **compra** de libros "
                             "nuevos, porque depende de un presupuesto que la biblioteca no maneja "
                             "y mejorarla no reduce las pérdidas; (b) el **estado físico** del "
                             "libro (páginas rotas), porque es un problema real pero distinto y "
                             "meterlo obligaría a un inventario de condición que no cabe en un "
                             "semestre; (c) el **transporte** del lector, porque aquí —a diferencia "
                             "del caso de las citas médicas— la biblioteca es del barrio y la "
                             "distancia no explica ninguna pérdida.\n\n"
                             "**Lo que se discutió y se decidió dejar DENTRO:** el lector que no "
                             "devuelve. Es tentador dejarlo fuera («eso es un problema de las "
                             "personas, no del sistema»), pero si se deja fuera desaparece el "
                             "problema que se quería resolver.",
                "como_calificar": "20 pts. Lo que se califica es que **haya exclusiones con razón**, "
                                  "no cuáles. Un equipo que excluya el estado físico del libro "
                                  "explicando por qué está bien; un equipo que escriba «dentro: "
                                  "todo lo de la biblioteca» vale 5. La discusión sobre si el lector "
                                  "que no devuelve entra o sale es la señal de que el equipo entendió "
                                  "que la frontera es una decisión: si aparece, dé los 20 completos.",
            },
            {
                "clave": "ENTRADAS, PROCESO Y SALIDAS",
                "respuesta": "**Entradas:** la solicitud de préstamo (un lector que llega y pide un "
                             "título), el libro devuelto, y el catálogo de lo que existe en el "
                             "estante.\n\n"
                             "**Proceso:** el auxiliar busca físicamente en el estante; si está, "
                             "anota nombre, libro y fecha en el cuaderno y entrega; cuando el libro "
                             "vuelve, tacha el renglón y lo devuelve al estante.\n\n"
                             "**Salidas:** el libro en manos del lector, el renglón en el cuaderno "
                             "y —esto es lo que hay que notar— **ninguna información utilizable**: "
                             "el cuaderno no permite responder «¿qué libros están afuera hoy?» sin "
                             "leerlo página por página.\n\n"
                             "**Dónde está el software:** hoy **no hay**. Y esto es importante para "
                             "el curso: el sistema existe, funciona a medias y no tiene una línea "
                             "de código. Si se introdujera software, iría en un solo punto del "
                             "proceso —el registro del préstamo y la consulta de disponibilidad—, "
                             "no en todo el sistema. El acto de buscar el libro, entregarlo y "
                             "recibirlo sigue siendo humano y físico.",
                "como_calificar": "15 pts. El punto que decide es el último: **el software ubicado "
                                  "como una parte del proceso**. Un equipo que escriba «el proceso "
                                  "es un sistema de gestión de biblioteca» no entendió la sesión y "
                                  "vale 5. Un equipo que diga «hoy no hay software y el sistema "
                                  "igual existe» vale los 15 completos, porque es exactamente la "
                                  "idea de la clase.",
            },
            {
                "clave": "LOS ACTORES",
                "respuesta": "**El lector que pide** (le importa encontrar el libro y llevárselo "
                             "rápido). **El auxiliar** (le importa no equivocarse y no pasar la "
                             "tarde buscando en el estante; hoy hace trabajo doble). **Quien "
                             "responde por el inventario** —la coordinación de la biblioteca— (le "
                             "importa que no se pierdan libros, porque reponerlos cuesta y a veces "
                             "no se puede).\n\n"
                             "**El actor no-usuario, que es el que se olvida:** el lector que llega, "
                             "pregunta por un libro, el auxiliar mira el estante y no lo encuentra, "
                             "y se va con la idea de que **la biblioteca no tiene ese libro**. En "
                             "realidad el libro existe y está prestado, pero como el cuaderno no se "
                             "consulta hacia atrás, nadie puede decirle «vuelva el jueves». Esa "
                             "persona no usa el sistema de préstamo —nunca llega a firmar el "
                             "cuaderno— y es la más perjudicada: pierde el acceso y además se lleva "
                             "una idea falsa del inventario.\n\n"
                             "**Un segundo no-usuario, si el equipo lo encuentra:** quien donó "
                             "libros a la biblioteca y ve que se pierden.",
                "como_calificar": "25 pts. La mitad depende del no-usuario. «El lector» genérico no "
                                  "cuenta como no-usuario: hay que nombrar a alguien que **queda "
                                  "fuera del sistema y sufre el resultado**. Si el equipo describe "
                                  "al lector que se va creyendo que el libro no existe, dé los 25: "
                                  "es el mejor hallazgo posible en este caso. Si solo lista lector, "
                                  "auxiliar y coordinación, 12.",
            },
            {
                "clave": "LA RETROALIMENTACIÓN",
                "respuesta": "**No hay.** Esta es la respuesta correcta y hay que decirlo así. El "
                             "sistema no tiene ninguna manera de enterarse de que algo salió mal: "
                             "un libro que no volvió no dispara nada, porque el renglón sin tachar "
                             "solo se ve si alguien se pone a revisar el cuaderno hacia atrás, y "
                             "nadie lo hace. Las dos cajas perdidas en un año son la consecuencia "
                             "directa: no se perdieron de golpe, se fueron perdiendo de uno en uno "
                             "sin que nada avisara.\n\n"
                             "**Y de ahí sale la mejor oportunidad de mejora, que además es "
                             "barata:** cualquier mecanismo que convierta «renglón sin tachar» en "
                             "un aviso. Puede ser software, pero también puede ser una hoja aparte "
                             "con los préstamos vencidos que el auxiliar revise los viernes. Que la "
                             "solución más obvia no requiera programar es un buen argumento para "
                             "una clase de primer semestre.",
                "como_calificar": "10 pts (dentro del bloque de actores/retroalimentación según su "
                                  "reparto). «No hay retroalimentación» **es la respuesta completa** "
                                  "si viene con la consecuencia (las cajas perdidas). Si el equipo "
                                  "escribe «la retroalimentación es que el auxiliar se da cuenta», "
                                  "pregunte cómo se da cuenta: ahí se cae solo.",
            },
            {
                "clave": "LA IA: PROMPT Y CORRECCIONES",
                "respuesta": "**Prompt de ejemplo (aceptable):** «Describe como sistema el préstamo "
                             "de libros de una biblioteca de barrio donde los préstamos se anotan "
                             "en un cuaderno. Dame entradas, proceso, salidas, actores y "
                             "retroalimentación.»\n\n"
                             "**Lo que un asistente típicamente devuelve y hay que corregir:**\n\n"
                             "**(1) Cifras inventadas.** Escribe cosas como «en promedio se pierde "
                             "el 5 % del inventario anual» o «el tiempo de búsqueda es de 3 a 5 "
                             "minutos». **Corrección:** ese dato no existe para esta biblioteca. Lo "
                             "único que se sabe es lo observado: dos cajas en un año. Se borra el "
                             "porcentaje y se deja el dato real.\n\n"
                             "**(2) Software que no existe.** Suele describir el proceso como si "
                             "hubiera un sistema de gestión, con «registro en la base de datos» y "
                             "«consulta al catálogo digital». **Corrección:** aquí el registro es un "
                             "cuaderno de papel y el catálogo es el estante. Es el error más "
                             "importante de detectar, porque es justo la confusión de la clase de "
                             "hoy: la IA asume software donde no hay.\n\n"
                             "**(3) Normas o instituciones inventadas.** Puede citar una ley o un "
                             "reglamento de bibliotecas públicas colombianas con número y año. "
                             "**Corrección:** se elimina lo que no se pueda verificar en la fuente "
                             "original. No se «arregla» una cita: se quita.\n\n"
                             "**(4) Actores genéricos, sin el no-usuario.** Lista «usuarios, "
                             "personal y administración». **Corrección:** se reemplaza por roles "
                             "concretos y se agrega el lector que se va creyendo que el libro no "
                             "existe, que la IA casi nunca propone porque no está en la descripción "
                             "que se le dio.\n\n"
                             "**(5) Retroalimentación optimista.** Suele afirmar que «el sistema se "
                             "retroalimenta con el registro de devoluciones». **Corrección:** el "
                             "registro existe pero **nadie lo lee hacia atrás**, así que no hay "
                             "retroalimentación. La IA describe el sistema como debería ser, no "
                             "como es.",
                "como_calificar": "30 pts, el bloque que decide la nota. Exija **tres correcciones "
                                  "con su razón**. Vale más una corrección profunda (la (2) o la "
                                  "(5)) que tres cosméticas de redacción. Si el equipo entrega el "
                                  "texto de la IA sin correcciones, 0 en este bloque, y dígaselo en "
                                  "voz alta con el argumento correcto: no es castigo por usar la "
                                  "herramienta, es que sin verificación no hay nada de ingeniería "
                                  "que calificar. **Corrección de tipo (1) o (3) —cifra o norma "
                                  "inventada— cuenta doble**: es la falla que más daño hace en un "
                                  "trabajo profesional.",
            },
        ],
        "variantes": [
            {"caso": "Si el equipo trabaja un sistema de citas o turnos",
             "clave": "El no-usuario es quien deja de conseguir cita porque otro madrugó, o quien "
                      "no puede madrugar. La frontera se discute en el transporte. La "
                      "retroalimentación suele existir a medias: se enteran cuando alguien reclama, "
                      "que es tarde y sesgado (solo reclaman algunos)."},
            {"caso": "Si el equipo trabaja un sistema de ventas o inventario de un negocio",
             "clave": "El no-usuario es el cliente que se fue porque le dijeron que no había "
                      "producto cuando sí había. La frontera se discute en el proveedor. La "
                      "retroalimentación casi siempre es el conteo físico de fin de mes, que "
                      "detecta el problema treinta días tarde: ese retardo es el hallazgo."},
            {"caso": "Si el equipo trabaja un sistema de transporte o rutas",
             "clave": "El no-usuario es el vecino que sufre el tráfico sin usar el servicio. La "
                      "frontera se discute en el andén y el paradero. Cuidado con las cifras: es "
                      "el caso donde la IA inventa más datos de tiempos y frecuencias, así que es "
                      "el mejor para el bloque de correcciones."},
            {"caso": "Si el equipo trabaja un sistema académico de la propia universidad",
             "clave": "Está permitido y funciona bien porque lo conocen de primera mano, pero "
                      "**sin nombres de funcionarios**: se usa el rol. El no-usuario suele ser el "
                      "aspirante que no alcanzó a matricularse. La retroalimentación es el punto "
                      "fuerte: casi siempre existe un canal de reclamos y casi nunca cambia el "
                      "proceso, lo que permite hablar de retroalimentación que no retroalimenta."},
        ],
        "cierre": "Tres minutos, una idea: **el sistema no es el software.** Muéstrelo con el caso "
                  "de la biblioteca, que es un sistema completo sin una línea de código, y con el "
                  "de la app de citas impecable junto a la fila que no se movió. Enuncie el "
                  "criterio de éxito del curso con esas palabras: un proyecto de aquí se juzga por "
                  "si **el problema del entorno se redujo y se puede medir**, no por si el "
                  "prototipo funciona. Y cierre con lo de la IA, que es la idea que se llevan para "
                  "el semestre: la herramienta solo se puede verificar si uno sabe del tema, así "
                  "que no reemplaza aprender el contenido — lo vuelve más necesario. Anuncie la "
                  "sesión 4: hoy vimos que un sistema puede funcionar y ser injusto; la próxima, "
                  "qué responsabilidad tiene el ingeniero cuando eso pasa.",
        "conexion": "Hacia atrás: la sesión 1 dejó el problema del entorno y la sesión 2 mostró que "
                    "los proyectos fracasan por no entenderlo. Hacia adelante: la frontera y los "
                    "actores de hoy son dos de los cinco campos de la ficha del problema que se "
                    "entrega en la **sesión 6** (cierre del corte 1); el actor no-usuario es el "
                    "insumo directo de la **sesión 13** (impacto social y ambiental); y el uso "
                    "declarado de IA se vuelve a exigir, con más nivel, en la **sesión 11**.",
    },

    "errores": [
        {"dice": "«El sistema es la app / la plataforma»",
         "por_que": "Confunde el sistema con una de sus partes; es la falla que la clase entera ataca.",
         "pida": "Que señalen dónde está el software DENTRO del proceso, y qué partes del sistema no son software."},
        {"dice": "«Los usuarios» como actor",
         "por_que": "No es un rol: no dice qué le importa a quién ni permite encontrar al perjudicado.",
         "pida": "Roles concretos y, obligatorio, uno que no use el sistema y sí sufra el resultado."},
        {"dice": "«Dentro de la frontera: todo lo relacionado»",
         "por_que": "Una frontera sin exclusiones no es una frontera, y produce proyectos que no se acaban.",
         "pida": "Una cosa que dejen fuera a propósito, con la razón escrita."},
        {"dice": "«La retroalimentación es que el usuario se queja»",
         "por_que": "Es tardía y sesgada: solo se queja una parte, y ya pasó el daño.",
         "pida": "Cómo se enteraría el sistema ANTES de que alguien reclame. Si no hay manera, que lo escriban: es un hallazgo."},
        {"dice": "Un dato con cifra que salió de la IA",
         "por_que": "El asistente inventa cifras locales con total naturalidad y sin avisar.",
         "pida": "La fuente. Si salió de la IA, que lo borren y lo anoten como corrección: eso es lo que se califica."},
    ],

    "dudas": [
        {"p": "¿Entonces podemos usar IA en todo el curso?",
         "r": "No. El Plan de curso la autoriza en las sesiones 3 y 11. En las demás no se usa, y "
              "la razón es práctica: para poder verificar lo que dice hay que saber del tema, y el "
              "tema es lo que estamos aprendiendo. Cuando se use, siempre se declara el prompt y "
              "las correcciones."},
        {"p": "¿Se penaliza usar IA?",
         "r": "No. Se penaliza **no verificarla**. Un texto pegado sin correcciones vale 0 en ese "
              "bloque porque no muestra ningún trabajo de ingeniería, igual que copiar un párrafo "
              "de una página web sin leerlo."},
        {"p": "¿Qué pasa si la IA acertó en todo y no encontramos nada que corregir?",
         "r": "Vuelvan a mirar las cifras, los nombres propios y las normas. En un caso local "
              "siempre hay algo inventado o asumido. Si de verdad no encuentran nada, escriban qué "
              "verificaron y cómo: eso también se califica, pero tiene que estar la verificación."},
        {"p": "¿El sistema de nuestro proyecto tiene que ser el problema de la sesión 1?",
         "r": "Sí, hoy sí. La idea es que ese problema madure: en la sesión 6 se entrega la ficha "
              "del problema del proyecto y es más fácil si vienen trabajándolo desde la primera "
              "semana."},
    ],

    "notas_operativas": [
        "Las cinco salas de grupo se crean **antes** de la sesión.",
        "Es la primera de las dos sesiones con IA autorizada. Diga la regla completa **antes** de "
        "abrir las salas, no después: prompt + correcciones, o no puntúa.",
        "El error más útil de cazar en las salas es la **cifra inventada**. Si aparece un "
        "porcentaje o un promedio en el documento, pregunte de dónde salió.",
        "Anote los actores no-usuarios que aparezcan en las cinco exposiciones: es la lista de "
        "entrada de la sesión 13 y no se vuelve a tener tan fácil.",
        "Ningún equipo debe subir nombres de funcionarios ni de personas reales. Si el sistema es "
        "de la propia universidad, se usa el rol.",
    ],

    "ti_siguiente": {
        "tid": "Análisis de caso práctico — dejen la ficha del sistema completa en la carpeta del "
               "equipo, con el prompt y las correcciones.",
        "ti": "Ensayo sobre impacto social: media página sobre a quién le empeora la vida el "
              "sistema que analizaron, aunque funcione bien.",
        "adelanto": "los principios éticos de la profesión, con casos reales donde el software "
                    "funcionó y aun así el ingeniero hizo algo mal.",
        "aviso": "Traigan identificado el **actor no-usuario** de su sistema. La sesión 4 arranca "
                 "con esa persona y el ensayo de media página es sobre ella.",
    },

    "cierre_titulo": "Nos vemos en la sesión 4",
    "cierre_frase": "El sistema no es el software: el software es una parte del proceso",
}


# =============================================================================
# CLASE 4 · Principios eticos en la Ingenieria
# =============================================================================

TEMAS[4] = {
    "n": 4,
    "titulo": "Principios éticos en la Ingeniería",
    "subtitulo": "Cuando el software funciona y aun así el ingeniero hizo algo mal",
    "hook": "Un ingeniero escribió el código que le pidieron, funcionó perfecto, "
            "y terminó en la cárcel. ¿Cómo llega alguien ahí?",
    "hook_lines": [
        "Pasó de verdad: 40 meses de prisión, y el software no tenía un solo error.",
        "Hoy vemos por qué «yo solo programé lo que me pidieron» no es una defensa.",
    ],
    "objetivos": [
        "Distinguir un **problema ético** de un problema técnico y de un problema legal.",
        "Usar los principios del **código de ética de ACM/IEEE** y de la **Ley 842 de 2003** para juzgar un caso.",
        "Nombrar **tres normas colombianas** que obligan al ingeniero de sistemas, y qué exige cada una.",
        "Identificar en un caso real **el momento en que se pudo parar** y quién tenía que hablar.",
    ],
    "agenda": {
        "Teoría y guía del docente": "Teoría — principios, normas colombianas y cuatro casos reales",
        "Actividad en equipos": "Taller — comité de ética: juzgar un caso con el código en la mano",
        "Exposiciones": "5 equipos × 3 min — el veredicto y el momento en que se pudo parar",
    },
    "herramienta_nota": "Hoy **no se usa asistente de IA**, y la razón es del tema: un caso ético "
                        "se juzga leyendo el código de ética y los hechos, no pidiéndole una "
                        "opinión a una herramienta que no responde por ella. El texto del código "
                        "de ética de ACM/IEEE y el de la Ley 842 de 2003 se comparten en la "
                        "carpeta del curso y **hay que citar el numeral**, no resumirlo de memoria.",
    "avance_proyecto": "Identificar a quién puede perjudicar el proyecto del equipo y qué norma "
                       "colombiana lo obliga a cuidar eso — sobre todo si va a manejar datos de "
                       "personas",

    "teoria": [
        {
            "tipo": "before_after",
            "titulo": "Tres cosas que se confunden",
            "before_title": "Lo que la gente cree que es la ética",
            "before": [
                "Ser buena persona y tener buenas intenciones.",
                "Un tema de opinión: cada uno tiene la suya.",
                "Algo que se ve al final, cuando ya pasó el daño.",
                "Responsabilidad del jefe, que fue el que decidió.",
                "Lo mismo que la ley: si es legal, está bien.",
            ],
            "after_title": "Lo que es en una profesión",
            "after": [
                "**Decidir bien con información incompleta** y poder explicar por qué.",
                "Hay **códigos escritos** con principios y numerales que se citan.",
                "Se ve **en el momento de decidir**, que casi siempre es temprano y barato.",
                "El que firma responde, y **el que ejecuta también**: hay ingenieros presos.",
                "La ley es el **mínimo**. Muchas cosas legales son indefendibles.",
            ],
            "size": 13,
        },
        {
            "tipo": "cards",
            "titulo": "Los principios que sí están escritos",
            "cards": [
                ("ACM/IEEE · Código de Ética del Ingeniero de Software (1999)",
                 "Ocho principios: **público**, cliente y empleador, producto, juicio, gestión, "
                 "profesión, colegas y sí mismo. El primero manda sobre los otros siete: «actuar "
                 "de forma consistente con el **interés público**»."),
                ("Ley 842 de 2003 · Colombia",
                 "Código de ética profesional de la ingeniería. Obliga a los deberes con la "
                 "sociedad, la dignidad de la profesión y el ejercicio con **matrícula "
                 "profesional** (COPNIA), que es la que se puede suspender."),
                ("Ley 1581 de 2012 · Datos personales",
                 "Principios de finalidad, libertad, veracidad, seguridad y acceso restringido. "
                 "**Nada de datos personales sin autorización previa**, y los datos sensibles "
                 "(salud, biometría, orientación) tienen protección reforzada."),
                ("Ley 1273 de 2009 · Delitos informáticos",
                 "Metió al Código Penal el acceso abusivo a un sistema informático, la "
                 "interceptación de datos y el hurto por medios informáticos. Aquí **la sanción "
                 "es cárcel**, no una multa a la empresa."),
            ],
            "columns": 2,
        },
        {
            "tipo": "tabla",
            "titulo": "Cuatro casos donde el software funcionó",
            "headers": ["Caso", "Qué pasó", "La decisión que lo causó"],
            "rows": [
                ["Therac-25\n1985–1987",
                 "Una máquina de radioterapia entregó sobredosis masivas de radiación. "
                 "Seis accidentes conocidos, con muertos.",
                 "Se quitaron los **seguros físicos** de los modelos anteriores y se confió solo "
                 "en el software. Nadie lo revisó de forma independiente."],
                ["Volkswagen\n2015",
                 "Un software detectaba la prueba de emisiones y bajaba los contaminantes solo "
                 "durante el examen. En la calle, muchas veces el límite.",
                 "Un ingeniero programó exactamente lo que le pidieron. **Se declaró culpable y "
                 "recibió 40 meses de prisión.**"],
                ["Boeing 737 MAX\n2018–2019",
                 "Un sistema automático empujaba el morro del avión hacia abajo. Dos accidentes, "
                 "346 muertos, la flota en tierra.",
                 "El sistema dependía de **un solo sensor** y no se explicó en el manual de vuelo. "
                 "La alerta que avisaba era un accesorio opcional."],
                ["Cambridge Analytica\n2018",
                 "Datos de decenas de millones de personas usados para perfilamiento político sin "
                 "que ellas lo supieran.",
                 "Una interfaz permitía a una aplicación tomar datos **de los amigos** del "
                 "usuario. Era legal, estaba documentado, y nadie preguntó si debía existir."],
            ],
            "note": "En los cuatro, el código hizo lo que se le pidió. El problema fue lo que se "
                    "le pidió, y que nadie con la información suficiente lo detuvo.",
            "col_w": [1.5, 4.0, 4.3],
        },
        {
            "tipo": "box",
            "titulo": "«Yo solo programé lo que me pidieron»",
            "notas": [
                ("advertencia",
                 "**No funciona legalmente.** En el caso Volkswagen un ingeniero que ejecutó la "
                 "orden se declaró culpable y fue condenado a prisión, además de la multa. La "
                 "orden de un superior no traslada la responsabilidad penal."),
                ("advertencia",
                 "**No funciona profesionalmente.** El primer principio del código ACM/IEEE pone "
                 "el interés público **por encima** del cliente y del empleador. Si hay conflicto, "
                 "el código ya decidió cuál gana."),
                ("info",
                 "**Lo que sí funciona: dejar rastro y escalar temprano.** Un correo que diga «esto "
                 "que me piden tiene este riesgo para estos afectados, lo dejo por escrito» cambia "
                 "el caso, ayuda a que se corrija y protege a quien lo escribió. Callar por escrito "
                 "no existe."),
            ],
        },
        {
            "tipo": "steps",
            "titulo": "Cinco preguntas para decidir sin ser experto",
            "steps": [
                ("1 · ¿Quién se puede dañar?", "Nómbrelo. Si la respuesta es «nadie», busque de nuevo: siempre hay alguien que no está en la reunión."),
                ("2 · ¿Lo sabe y lo aceptó?", "Consentimiento informado. Si el afectado no sabe que existe el sistema, ya hay un problema."),
                ("3 · ¿Aguanta que se sepa?", "Si esto sale publicado mañana con su nombre, ¿lo defiende? Es la prueba más rápida que existe."),
                ("4 · ¿Qué dice el código?", "Busque el numeral. Citar un principio escrito es más fuerte que dar una opinión."),
                ("5 · ¿Cuándo se puede parar?", "Encuentre el momento más temprano y más barato. Después de entregar cuesta cien veces más."),
            ],
            "sub": "Ninguna requiere ser abogado. La 3 es la que más rápido descarta una mala idea",
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada: el ingeniero que fue a la cárcel",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "La apertura de hoy es un caso verdadero y conviene no revelar el nombre en el "
                "primer minuto, porque la fuerza está en la pregunta. Un ingeniero de Volkswagen "
                "escribió el software que detectaba cuándo el carro estaba en la prueba de "
                "emisiones para bajar los contaminantes solo durante el examen. El software "
                "funcionaba perfecto: hacía exactamente lo que se le pidió, sin errores. En 2017 "
                "ese ingeniero se declaró culpable en Estados Unidos y fue condenado a cuarenta "
                "meses de prisión, además de una multa.",
                "El estudiante de primer semestre tiene interiorizada la idea de que la "
                "responsabilidad es del jefe y que el programador ejecuta. Este caso la rompe con "
                "un hecho verificable, y por eso es mejor abrir con él que con una definición de "
                "ética. Recoja las respuestas en el muro los primeros diez minutos —van a aparecer "
                "«robó», «hackeó», «se equivocó»— y en el minuto 30, cuando llegue al caso en la "
                "tabla, muestre que ninguna era: **no hubo error, no hubo robo, hubo una decisión "
                "de diseño que se ejecutó bien**.",
            ],
        },
        {
            "titulo": "Qué es la ética en una profesión y qué no es",
            "slide": "{{slide:Tres cosas que se confunden}}",
            "cuerpo": [
                "Hay tres confusiones que hay que desmontar antes de tocar cualquier caso, porque "
                "si no, la discusión del taller se vuelve una conversación de opiniones y no se "
                "puede calificar.",
                "**La primera: la ética profesional no es tener buenas intenciones.** Es tomar "
                "decisiones defendibles con información incompleta y poder explicar el criterio. "
                "Un ingeniero con excelentes intenciones que no preguntó a quién afecta su sistema "
                "hizo algo mal, y el resultado no mejora por su buena voluntad. Al revés, un "
                "ingeniero que detecta un riesgo y lo escribe está actuando bien aunque el "
                "proyecto igual salga mal.",
                "**La segunda: no es un tema de opinión.** Esta es la que más rinde en clase, "
                "porque el estudiante llega convencido de que en ética «cada uno piensa distinto». "
                "Existen códigos escritos, con principios numerados, que uno puede citar como se "
                "cita un artículo de una norma. El código de ética de ACM e IEEE Computer Society "
                "para ingeniería de software es de 1999 y tiene ocho principios; el código de "
                "ética del ingeniero en Colombia es la Ley 842 de 2003. Un veredicto que cita el "
                "numeral es un argumento; «a mí me parece que estuvo mal» no lo es. En el taller "
                "de hoy se califica exactamente esa diferencia.",
                "**La tercera: la ley es el piso, no el techo.** El caso de Cambridge Analytica es "
                "el mejor para mostrarlo: la interfaz que permitía a una aplicación tomar datos de "
                "los amigos del usuario estaba documentada públicamente y era permitida por las "
                "reglas de la plataforma. Era legal y es indefendible. Al revés también ocurre: "
                "algo puede ser éticamente correcto y estar prohibido por una política interna. "
                "La ley y la ética se cruzan pero no coinciden, y el ingeniero tiene que mirar "
                "las dos.",
                "Una cuarta idea, que es la que más les sirve: **el momento de la ética es el "
                "momento de decidir, y casi siempre es temprano**. Quitar un seguro físico de una "
                "máquina de radioterapia porque el software ya lo cubre es una decisión que cuesta "
                "una reunión; enterarse de las consecuencias cuesta vidas y una investigación de "
                "años. La ética no es lo que se hace después del desastre.",
            ],
        },
        {
            "titulo": "Los códigos y las tres normas colombianas que hay que saber nombrar",
            "slide": "{{slide:Los principios que sí están escritos}}",
            "cuerpo": [
                "**ACM/IEEE, 1999.** Ocho principios en este orden: público, cliente y empleador, "
                "producto, juicio, gestión, profesión, colegas y sí mismo. El orden importa y hay "
                "que decirlo en voz alta: el principio 1 —actuar de forma consistente con el "
                "interés público— **está por encima** del principio 2, que es el cliente y el "
                "empleador. Eso significa que el código ya resolvió el conflicto que el estudiante "
                "cree irresoluble: si lo que pide el jefe daña al público, el código dice cuál "
                "gana. La ACM actualizó además su código general en 2018.",
                "**Ley 842 de 2003.** Es el código de ética profesional de la ingeniería en "
                "Colombia y es la que aplica aquí, no las de otros países. Establece los deberes "
                "del ingeniero con la sociedad, con la profesión, con sus colegas y con sus "
                "clientes, y define las faltas y las sanciones. El punto práctico que hay que "
                "aterrizar para un estudiante de primer semestre es la **matrícula profesional**: "
                "en Colombia el ejercicio de la ingeniería requiere matrícula, la expide el COPNIA "
                "—Consejo Profesional Nacional de Ingeniería—, y el COPNIA puede sancionar y "
                "suspenderla. Es decir, la ética profesional aquí no es un discurso: tiene una "
                "autoridad, un procedimiento y una consecuencia sobre el derecho a ejercer.",
                "**Ley 1581 de 2012** (con el Decreto 1377 de 2013) es la de protección de datos "
                "personales, y es la norma que más van a tocar en su vida laboral, empezando por "
                "el proyecto de este curso. Los principios que hay que poder nombrar: finalidad "
                "(los datos se piden para algo declarado y no se usan para otra cosa), libertad "
                "(hace falta autorización previa, expresa e informada), veracidad, transparencia, "
                "acceso restringido, seguridad y confidencialidad. Los **datos sensibles** —salud, "
                "biometría, orientación política, sexual o religiosa, datos de niños— tienen "
                "protección reforzada. La autoridad es la Superintendencia de Industria y "
                "Comercio. Aterrícelo en el curso: si un equipo quiere hacer un proyecto con una "
                "base de datos de pacientes de un consultorio del barrio, esta ley le aplica "
                "completa, y por eso el curso prohíbe subir nombres y cédulas.",
                "**Ley 1273 de 2009** agregó al Código Penal un título sobre la protección de la "
                "información y los datos: acceso abusivo a un sistema informático, obstaculización "
                "ilegítima, interceptación de datos, daño informático, hurto por medios "
                "informáticos. La diferencia con la anterior hay que subrayarla: aquí la "
                "consecuencia es **pena de prisión para la persona**, no una sanción "
                "administrativa a la empresa. Es la norma que convierte en delito lo que un "
                "estudiante puede considerar una travesura —entrar a un sistema ajeno «solo para "
                "probar»— y conviene decirlo hoy, en la sesión 4, y no cuando ya pasó.",
            ],
        },
        {
            "titulo": "Los cuatro casos: qué contar de cada uno y cuál es el momento de parar",
            "slide": "{{slide:Cuatro casos donde el software funcionó}}",
            "cuerpo": [
                "**Therac-25 (1985–1987).** Máquina de radioterapia de la Atomic Energy of Canada "
                "Limited. Seis accidentes conocidos con sobredosis masivas de radiación y varios "
                "muertos. Las causas son de manual y hay que contarlas completas porque son "
                "técnicas: los modelos anteriores tenían **seguros físicos** que impedían "
                "mecánicamente una configuración peligrosa, y en el Therac-25 se quitaron confiando "
                "en que el software lo evitaría; el software venía reutilizado de los modelos "
                "anteriores, con errores que antes quedaban tapados por esos seguros; había una "
                "condición de carrera que se disparaba cuando la operadora corregía la pantalla "
                "muy rápido, algo que hacían las operadoras expertas; los mensajes de error eran "
                "crípticos («MALFUNCTION 54») y aparecían tan seguido que se ignoraban; nunca hubo "
                "revisión independiente del código; y el fabricante sostuvo al principio que la "
                "sobredosis era imposible. La investigación de Nancy Leveson y Clark Turner (1993) "
                "es la fuente canónica y está disponible. **El momento de parar** fue la decisión "
                "de quitar los seguros físicos: ahí, en una reunión de diseño, era gratis.",
                "**Volkswagen (2015).** El «defeat device»: software que reconocía las condiciones "
                "de la prueba de laboratorio y activaba el control de emisiones solo en ese "
                "momento. En circulación real el vehículo emitía óxidos de nitrógeno muy por "
                "encima del límite. Se descubrió en 2015 y el detalle que interesa aquí es "
                "judicial: el ingeniero James Liang se declaró culpable y fue condenado en 2017 a "
                "cuarenta meses de prisión y una multa; un directivo recibió una pena mayor. **El "
                "momento de parar** fue cuando le pidieron escribir la detección de la prueba: no "
                "hacía falta ser experto en emisiones para ver que un código cuyo propósito es "
                "comportarse distinto durante el examen existe para engañar.",
                "**Boeing 737 MAX (2018–2019).** El MCAS empujaba el morro hacia abajo con base en "
                "**un solo sensor de ángulo de ataque**, podía activarse repetidamente, y no "
                "estaba explicado en el manual de vuelo, así que los pilotos no sabían que "
                "existía. Dos accidentes —Lion Air 610 en octubre de 2018 y Ethiopian 302 en marzo "
                "de 2019— con 346 muertos en total, y la flota mundial en tierra. Un detalle que "
                "vale oro para una clase de ingeniería: la alerta que avisaba de la discrepancia "
                "entre sensores era una **opción de pago**. **El momento de parar** fue la "
                "decisión de arquitectura de depender de un sensor único en un sistema capaz de "
                "mover el avión, y la de no documentarlo para no obligar a reentrenar pilotos.",
                "**Cambridge Analytica (2018).** Una aplicación de cuestionarios recogía datos del "
                "usuario **y de sus amigos**, que nunca la instalaron ni supieron de ella, "
                "aprovechando una interfaz de la plataforma que lo permitía. Los datos de decenas "
                "de millones de personas terminaron en perfilamiento político. La consecuencia fue "
                "una multa histórica a la plataforma. **El momento de parar** fue el diseño de esa "
                "interfaz: alguien decidió que el consentimiento de una persona alcanzara para "
                "entregar los datos de sus contactos. Es el caso que conecta directo con la Ley "
                "1581 y con el principio de finalidad.",
                "El hilo común hay que enunciarlo al final de la tabla: **en los cuatro casos el "
                "software funcionó**. No hubo un error de programación que causara el desastre —"
                "salvo parcialmente en Therac-25, y ahí el error existía desde antes y estaba "
                "tapado por un seguro que alguien decidió quitar—. Lo que falló fue lo que se "
                "pidió construir y el hecho de que nadie con información suficiente lo detuvo. Esa "
                "frase es la tesis de la clase.",
            ],
        },
        {
            "titulo": "La defensa que no sirve y las cinco preguntas que sí",
            "slide": "{{slide:Yo solo programé lo que me pidieron}} {{slide:Cinco preguntas}}",
            "cuerpo": [
                "«Yo solo programé lo que me pidieron» es la frase que el estudiante va a usar "
                "espontáneamente en el taller, y hay que desarmarla con hechos en vez de con "
                "moralina. Legalmente no funciona: el caso Volkswagen tiene un ingeniero condenado "
                "a prisión por ejecutar. Profesionalmente tampoco: el código ACM/IEEE pone el "
                "interés público por encima del empleador, así que el conflicto ya está resuelto "
                "en el texto.",
                "Pero la parte útil no es la condena, es la alternativa, y conviene enseñarla en "
                "términos prácticos porque el estudiante que salga a trabajar el próximo año la va "
                "a necesitar: **dejar rastro y escalar temprano**. Un correo corto que diga «esto "
                "que se me pide tiene este riesgo para estas personas, lo dejo por escrito y "
                "propongo esta alternativa» hace tres cosas: aumenta la probabilidad de que se "
                "corrija, obliga a quien decide a decidir de verdad, y protege a quien lo escribió. "
                "Hay que decirlo sin heroísmo: no se le está pidiendo a un practicante que renuncie, "
                "se le está pidiendo que no sea el único que sabe. La única postura que no tiene "
                "defensa posible es callar.",
                "Las cinco preguntas son el método del taller. La más potente es la tercera —"
                "«¿aguanta que se sepa?»— porque no requiere saber nada de códigos ni de leyes y "
                "descarta la mayoría de las malas ideas en diez segundos: si la decisión depende de "
                "que los afectados no se enteren, ya está juzgada. La cuarta —buscar el numeral— es "
                "la que convierte una intuición en un argumento profesional, y es la que más pesa "
                "en la rúbrica. Y la quinta —¿cuándo se pudo parar?— es la que le da a la clase "
                "valor de ingeniería y no de conferencia: en los cuatro casos hubo un momento "
                "temprano, identificable y barato, en el que una persona con la información "
                "suficiente podía cambiar el resultado.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:10 · Apertura · [Slide 4]",
            "cuerpo": [
                "Comparta pantalla antes de que entre el primero:",
                "> «Un ingeniero escribió el código que le pidieron, funcionó perfecto, y terminó "
                "en la cárcel. ¿Cómo llega alguien ahí?»",
                "**[Nota docente]:** no diga todavía que es Volkswagen. Recoja las respuestas en "
                "el muro; van a aparecer «robó», «hackeó», «se equivocó». Ninguna es correcta y ese "
                "es el punto.",
                "**[Nota docente]:** hoy hay lectura previa (el código de ética). Verifique en el "
                "chat quién lo abrió: el taller se cae sin ese texto a mano.",
            ],
        },
        {
            "titulo": "00:10–00:55 · Teoría · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]",
            "cuerpo": [
                "Reparto sugerido de los 45 min:",
                "- **8 min** · Tres cosas que se confunden [Slide 5]. Insista en la segunda: "
                "**hay códigos escritos y se citan por numeral**. De eso depende que el taller sea "
                "evaluable y no una tertulia.",
                "- **10 min** · Los principios y las tres normas [Slide 6]. En ACM/IEEE, diga que "
                "el orden importa: el público está antes que el empleador. En Colombia, mencione la "
                "matrícula del COPNIA: la ética aquí tiene autoridad y consecuencia.",
                "- **16 min** · Los cuatro casos [Slide 7], unos 4 min cada uno. Therac-25 "
                "completo; en Volkswagen revele que este era el de la apertura y **vuelva al muro**.",
                "- **6 min** · «Yo solo programé lo que me pidieron» [Slide 8]. La parte importante "
                "es la salida práctica: dejar rastro y escalar temprano.",
                "- **5 min** · Las cinco preguntas [Slide 9]. Es el método del taller.",
                "**[Nota docente]:** si el tiempo aprieta, recorte Cambridge Analytica y 737 MAX a "
                "dos minutos. **Therac-25 y Volkswagen no se recortan**: uno da el argumento "
                "técnico y el otro el argumento legal.",
            ],
        },
        {
            "titulo": "00:55–01:12 · Taller en salas de grupo · [Slide 10]",
            "cuerpo": [
                "**2 min** para repartir casos: un caso por equipo, asignado por número de equipo. "
                "El quinto equipo recibe un caso local en vez de uno famoso (está en el taller), "
                "porque hace falta que al menos uno juzgue algo que podría pasarles a ellos.",
                "**15 min** en salas. Entre a las cinco, ~3 min cada una, y revise **una sola "
                "cosa: que haya un numeral citado**. Un veredicto sin numeral es una opinión y no "
                "puntúa el bloque más pesado.",
                "**[Nota docente]:** el error que hay que cortar en caliente es el veredicto "
                "genérico («actuaron con negligencia»). Pida el sujeto: **quién** decidió, en qué "
                "momento y qué información tenía.",
                "**[Nota docente]:** cuando alguien diga «pero le habrían echado del trabajo», no "
                "lo descarte: es la objeción honesta. Responda con lo que sí se le pide —dejar "
                "rastro y escalar— y con lo que le pasó a quien no lo hizo.",
            ],
        },
        {
            "titulo": "01:12–01:27 · Exposiciones · [Slide 11]",
            "cuerpo": [
                "5 equipos × 3 min, vocero con la pantalla ya compartida. **El minuto obligatorio "
                "de hoy es «el momento en que se pudo parar»**: sin eso la exposición es un resumen "
                "de noticia.",
                "**[Nota docente]:** los cinco enlaces en el chat antes de arrancar.",
                "**[Nota docente]:** anote qué numeral citó cada equipo. Si tres equipos citaron el "
                "principio 1 del código ACM/IEEE, dígalo en el cierre: es la señal de que el "
                "interés público es el principio que resuelve la mayoría de los casos.",
            ],
        },
        {
            "titulo": "01:27–01:30 · Cierre · [Slide 12][Slide 13]",
            "cuerpo": [
                "Una idea: **en los cuatro casos el software funcionó.** Falló lo que se pidió "
                "construir y el hecho de que nadie lo detuvo. La ética profesional es la decisión "
                "temprana, no el arrepentimiento posterior.",
                "Anuncie la sesión 5: hoy se vio el daño a personas; la próxima, el daño que no "
                "tiene una víctima con nombre y que casi nadie mide — el ambiental.",
            ],
        },
    ],

    "taller": {
        "archivo": "Comite de etica",
        "titulo": "Comité de ética",
        "min": 17,
        "exposicion": 3,
        "consigna": "Su equipo es un comité de ética profesional y le toca **un caso**. Emitan un "
                    "veredicto con el código en la mano: qué principio o norma se violó (**con el "
                    "numeral**), quién decidió, en qué momento se pudo parar y qué debía hacer el "
                    "ingeniero ahí. No se acepta «actuaron mal»: eso no es un veredicto.",
        "entregable": "un acta de comité de cinco bloques en el documento del equipo, con al menos "
                      "un numeral de código o de norma citado literalmente",
        "entregable_corto": "acta del comité con el numeral citado",
        "reparto_titulo": "El caso se asigna por número de equipo:",
        "reparto": "1 Therac-25 · 2 Volkswagen · 3 Boeing 737 MAX · 4 Cambridge Analytica · "
                   "5 el caso local que está al final de este taller. Los cuatro primeros son "
                   "públicos y hay fuentes; el quinto es el que podría pasarles el año entrante.",
        "reparto_corto": "un caso por equipo, del 1 al 5",
        "bloques": [
            {"clave": "LOS HECHOS, SIN ADJETIVOS",
             "pide": "Qué pasó, en cinco líneas máximo: qué sistema era, qué hizo, a quién afectó "
                     "y cómo se supo. Sin opinión todavía.",
             "check": "no hay adjetivos de juicio («terrible», «negligente») y sí hay hechos verificables."},
            {"clave": "QUIÉN DECIDIÓ QUÉ",
             "pide": "La decisión concreta que causó el daño y **quién la tomó** (el rol: el "
                     "diseñador, el gerente de producto, el ingeniero que ejecutó). Si fueron "
                     "varias personas en cadena, escriban la cadena.",
             "check": "hay un sujeto y una decisión, no «la empresa». «La empresa» no decide nada: deciden personas con un cargo."},
            {"clave": "EL NUMERAL QUE SE VIOLÓ",
             "pide": "Cite **literalmente** al menos un principio del código ACM/IEEE o un "
                     "artículo de la Ley 842 de 2003, la Ley 1581 de 2012 o la Ley 1273 de 2009, "
                     "y explique en dos líneas por qué aplica a este caso.",
             "check": "el texto está citado, no parafraseado, y la explicación conecta el numeral con el hecho. Es el bloque que más pesa."},
            {"clave": "EL MOMENTO EN QUE SE PUDO PARAR",
             "pide": "El momento **más temprano** en que alguien con la información disponible "
                     "podía cambiar el resultado, y qué debía hacer exactamente ahí "
                     "(a quién decirle qué, y por escrito o no).",
             "check": "el momento es anterior al daño y la acción es concreta. «Debieron ser más éticos» no es una acción."},
            {"clave": "LA REGLA QUE SE LLEVAN",
             "pide": "Una regla en una frase, escrita para ustedes mismos, que evite repetir esto "
                     "en el proyecto de este curso. Tiene que ser verificable.",
             "check": "la regla se puede comprobar. «Ser responsables» no se comprueba; «no subimos ningún dato de una persona sin su autorización escrita» sí."},
        ],
        "expo": [
            ("30 s · Los hechos", "Qué pasó, sin adjetivos. Cinco líneas dichas en medio minuto."),
            ("40 s · Quién decidió", "La decisión y el rol de quien la tomó. No «la empresa»."),
            ("50 s · El numeral", "Lea el principio o el artículo y diga por qué aplica. Es lo que más pesa."),
            ("50 s · El momento de parar", "Cuándo y qué había que hacer. Es el minuto obligatorio."),
            ("10 s · La regla propia", "Una frase, verificable, para su propio proyecto."),
        ],
    },

    "rubrica": [
        ("Los hechos están sin adjetivos de juicio y son verificables", 15,
         "Un comité que empieza opinando no puede juzgar. Separar hecho de juicio es la habilidad base."),
        ("Hay un sujeto y una decisión concreta, no «la empresa»", 20,
         "Es lo que convierte el caso en algo aplicable: las decisiones las toman personas con un cargo."),
        ("Se cita literalmente un numeral del código o un artículo de ley, y se conecta con el hecho", 30,
         "Es la diferencia entre un argumento profesional y una opinión. Es lo que se evalúa en el corte."),
        ("El momento de parar es anterior al daño y la acción propuesta es concreta", 25,
         "Es el valor de ingeniería de la sesión: la ética se ejerce decidiendo, no lamentando."),
        ("La regla propia es verificable y aplica al proyecto del curso", 10,
         "Cierra el ciclo: lo aprendido se convierte en una restricción de su propio trabajo."),
    ],

    "solucion": {
        "para_que": "Este documento resuelve el caso Therac-25 completo —el más difícil de los "
                    "cinco, porque exige entender una decisión técnica— y trae al final la clave "
                    "de los otros cuatro. Sirve para calificar con un referente y, sobre todo, "
                    "para tener listo el numeral citado: es el bloque que decide el 30 % y el que "
                    "los equipos improvisan si el docente no lo tiene a mano.",
        "caso_titulo": "Therac-25 · La máquina de radioterapia que dio sobredosis (1985–1987)",
        "caso": "Máquina de radioterapia de la Atomic Energy of Canada Limited (AECL). Entre 1985 "
                "y 1987 se documentaron seis accidentes con sobredosis masivas de radiación, con "
                "muertos entre los pacientes. Los modelos anteriores (Therac-6 y Therac-20) tenían "
                "**seguros físicos** que impedían mecánicamente la configuración peligrosa; en el "
                "Therac-25 se eliminaron y se dejó la protección **solo en el software**, "
                "reutilizando código de los modelos previos. Existía una condición de carrera que "
                "se activaba cuando la operadora corregía la pantalla muy rápido —justo lo que "
                "hacían las operadoras con experiencia—. Los mensajes de error eran crípticos "
                "(«MALFUNCTION 54») y tan frecuentes que se ignoraban. No hubo revisión "
                "independiente del código, y el fabricante sostuvo inicialmente que una sobredosis "
                "era imposible.",
        "por_que_este_caso": "Si el docente solo alcanza a leer una parte antes de clase, que sea "
                             "el bloque «EL MOMENTO EN QUE SE PUDO PARAR»: es el que casi ningún "
                             "equipo hace bien solo, porque exige distinguir el error de "
                             "programación de la decisión que lo volvió letal.",
        "bloques": [
            {
                "clave": "LOS HECHOS, SIN ADJETIVOS",
                "respuesta": "El Therac-25 era un acelerador lineal de uso médico para "
                             "radioterapia, fabricado por AECL y operado en hospitales de Estados "
                             "Unidos y Canadá. Entre junio de 1985 y enero de 1987 se documentaron "
                             "seis casos en que entregó dosis de radiación muy superiores a la "
                             "prescrita; hubo pacientes muertos y otros con lesiones graves.\n\n"
                             "Los afectados fueron los pacientes, y en segundo lugar las "
                             "operadoras, a las que en varios casos se responsabilizó antes de "
                             "identificar la causa. Se supo por el reporte insistente de los "
                             "hospitales y por la investigación de los reguladores; la "
                             "reconstrucción técnica de referencia es la de Nancy Leveson y Clark "
                             "Turner publicada en 1993.",
                "como_calificar": "15 pts. Se califica que **no haya juicio todavía**. Un equipo "
                                  "que escriba «la empresa fue criminalmente negligente al vender "
                                  "una máquina mortal» pierde la mitad: eso es el veredicto, y va "
                                  "en el bloque 3. Exija además el «cómo se supo»: es la parte que "
                                  "los equipos omiten y la que enseña que los casos no se "
                                  "descubren solos, alguien los reporta."
            },
            {
                "clave": "QUIÉN DECIDIÓ QUÉ",
                "respuesta": "**La decisión que causó el daño: eliminar los seguros físicos "
                             "(interlocks de hardware) que tenían los modelos anteriores y "
                             "trasladar esa protección al software.** La tomó el equipo de diseño "
                             "del producto en AECL, en la fase de diseño del Therac-25, no un "
                             "programador en una madrugada.\n\n"
                             "**La cadena completa, que es lo que se pide si fueron varias "
                             "personas:**\n\n"
                             "1. **El diseñador del producto** decide quitar los seguros físicos "
                             "confiando en el software.\n"
                             "2. **Quien decide reutilizar el código** de los modelos Therac-6 y "
                             "20 sin volver a verificarlo en el contexto nuevo. Ese código "
                             "arrastraba errores que antes eran inofensivos **porque el seguro "
                             "físico los tapaba**.\n"
                             "3. **Quien decide no someter el software a revisión independiente**, "
                             "en un equipo donde el software era ahora la única barrera entre el "
                             "paciente y una dosis letal.\n"
                             "4. **Quien diseña la interfaz** con mensajes como «MALFUNCTION 54», "
                             "sin decir qué pasó ni qué hacer, y sin distinguir un aviso trivial "
                             "de uno grave.\n"
                             "5. **Quien responde los primeros reportes de accidente** afirmando "
                             "que la sobredosis era imposible, en vez de investigarla. Esta es la "
                             "decisión que convirtió el primer accidente en seis.\n\n"
                             "Nótese que **el error de programación no aparece en la lista como "
                             "causa principal**. La condición de carrera existía; lo que la volvió "
                             "letal fueron las decisiones 1, 2 y 3.",
                "como_calificar": "20 pts. Un equipo que responda «el programador que dejó el bug» "
                                  "vale 8: es la respuesta intuitiva y es la equivocada, y hay que "
                                  "corregirla en voz alta porque es exactamente la confusión que "
                                  "la clase ataca. Los 20 completos son para quien identifique la "
                                  "eliminación de los seguros físicos como la decisión de fondo. "
                                  "Punto extra de reconocimiento —no de nota— si detectan la "
                                  "decisión 5, que es la que multiplicó el daño."
            },
            {
                "clave": "EL NUMERAL QUE SE VIOLÓ",
                "respuesta": "**Código ACM/IEEE de Ética del Ingeniero de Software (1999), "
                             "Principio 1 — PÚBLICO:** «Los ingenieros de software actuarán de "
                             "manera consistente con el interés público». Y en particular el "
                             "compromiso 1.03: **aprobar el software solo si existe la creencia "
                             "fundada de que es seguro, cumple las especificaciones, ha pasado las "
                             "pruebas apropiadas y no degrada la calidad de vida, la privacidad ni "
                             "daña el ambiente**. Aplica de forma directa: el software se aprobó "
                             "como única barrera de seguridad de una máquina capaz de matar, sin "
                             "revisión independiente y sin pruebas que cubrieran la secuencia de "
                             "teclas que las operadoras usaban a diario. No había creencia fundada "
                             "de que era seguro; había una suposición.\n\n"
                             "**También aplica el Principio 3 — PRODUCTO**, sobre asegurar que el "
                             "producto cumpla los estándares profesionales más altos posibles, y "
                             "el **Principio 6 — PROFESIÓN**, por sostener públicamente que la "
                             "sobredosis era imposible cuando ya había reportes.\n\n"
                             "**En Colombia, si el caso ocurriera aquí: Ley 842 de 2003**, que en "
                             "sus deberes del profesional frente a la sociedad obliga a que el "
                             "ejercicio de la ingeniería no ponga en riesgo la vida ni la "
                             "integridad de las personas, y establece las faltas contra la ética "
                             "profesional sancionables por el COPNIA, incluida la suspensión de la "
                             "matrícula profesional. El equipo debe citar el artículo concreto del "
                             "texto que se compartió en la carpeta del curso, no la ley en "
                             "general.",
                "como_calificar": "30 pts, el bloque que decide. Requisitos: (a) **cita literal**, "
                                  "entre comillas o transcrita, no un resumen; (b) identificación "
                                  "del principio o artículo por su número; (c) dos líneas que "
                                  "conecten el numeral con **este** hecho. Si falta (a), máximo "
                                  "15. Si el equipo cita «el código de ética dice que hay que ser "
                                  "responsable», 0: eso no está en ningún numeral. Se acepta "
                                  "cualquiera de los principios 1, 3 o 6, o la Ley 842; el 1 es el "
                                  "más fuerte y conviene decirlo al cerrar."
            },
            {
                "clave": "EL MOMENTO EN QUE SE PUDO PARAR",
                "respuesta": "**El momento más temprano y más barato fue la reunión de diseño en "
                             "que se decidió eliminar los seguros físicos.** Ahí, antes de "
                             "escribir una línea de código, alguien tenía que hacer una pregunta "
                             "que no requería ser experto en software: *si el software falla, ¿qué "
                             "impide que el paciente reciba una dosis letal?* La respuesta era "
                             "«nada», y esa respuesta bastaba para no seguir. Costo de parar en "
                             "ese punto: una reunión y un rediseño. Costo de no parar: seis "
                             "accidentes y muertos.\n\n"
                             "**Qué debía hacer el ingeniero, concretamente:** dejar por escrito "
                             "—no dicho de pasada— que al retirar los interlocks el software queda "
                             "como única barrera de seguridad, y que en esa condición se requiere "
                             "revisión independiente del código y pruebas específicas de las "
                             "secuencias de operación reales. Dirigido a quien decide el diseño, "
                             "con copia a quien responde por la certificación del equipo. Eso es "
                             "escalar temprano y dejar rastro: no es renunciar ni denunciar, es "
                             "que la decisión la tome quien tiene la autoridad **sabiendo** el "
                             "riesgo.\n\n"
                             "**Segundo momento, más caro pero todavía útil:** el primer reporte "
                             "de accidente. Ahí la acción correcta era retirar las máquinas del "
                             "servicio mientras se investigaba, en vez de afirmar que la "
                             "sobredosis era imposible. Cinco de los seis accidentes ocurrieron "
                             "después del primero.",
                "como_calificar": "25 pts. Se califica que el momento sea **anterior al daño** y "
                                  "que la acción sea ejecutable. «Debieron probar mejor el "
                                  "software» vale 10: es correcto y es tardío, porque no toca la "
                                  "decisión que creó el riesgo. «Debieron ser más responsables» "
                                  "vale 0. Los 25 son para quien ubique la reunión de diseño y "
                                  "escriba a quién había que decirle qué. Si el equipo identifica "
                                  "el segundo momento —el primer reporte—, es señal de muy buena "
                                  "lectura del caso."
            },
            {
                "clave": "LA REGLA QUE SE LLEVAN",
                "respuesta": "Ejemplos de reglas verificables que salen bien de este caso:\n\n"
                             "- «Cuando quitemos una validación de nuestro prototipo porque "
                             "*el código ya la cubre*, lo escribimos en el documento del equipo con "
                             "la fecha y quién lo decidió.»\n"
                             "- «Ningún mensaje de error de nuestro prototipo dice solo un código: "
                             "dice qué pasó y qué hacer.»\n"
                             "- «Si algo de nuestro sistema puede dañar a una persona, no "
                             "dependemos de una sola comprobación.»\n\n"
                             "Las tres son comprobables por otra persona, que es el requisito. La "
                             "primera es la que más se parece al caso; la segunda es la más fácil "
                             "de cumplir y aun así rara.",
                "como_calificar": "10 pts. El único criterio es **que se pueda comprobar**. Lea la "
                                  "regla y pregúntese: ¿podría yo revisar el documento del equipo "
                                  "en la sesión 12 y decir si la cumplieron? Si la respuesta es "
                                  "no, es una intención, no una regla, y vale 3."
            },
        ],
        "variantes": [
            {"caso": "Equipo 2 · Volkswagen (2015)",
             "clave": "**Decisión:** escribir un software cuyo único propósito era detectar la "
                      "prueba de emisiones y comportarse distinto durante ella. **Cadena:** quien "
                      "definió la meta imposible (cumplir el límite sin rediseñar el motor), quien "
                      "propuso el atajo, quien lo programó. **Numeral:** ACM/IEEE Principio 1 "
                      "(interés público: se contamina a terceros que no son parte del negocio) y "
                      "Principio 6 (profesión). **Momento de parar:** cuando le pidieron programar "
                      "la detección de la prueba; no hace falta saber de emisiones para ver que un "
                      "código que se comporta distinto durante el examen existe para engañar. "
                      "**Dato duro que hay que exigir:** el ingeniero que ejecutó fue condenado a "
                      "40 meses de prisión, así que la defensa de la obediencia ya fue probada en "
                      "un tribunal y falló."},
            {"caso": "Equipo 3 · Boeing 737 MAX (2018–2019)",
             "clave": "**Decisión:** que un sistema capaz de mover el avión dependiera de **un "
                      "solo sensor**, y no documentarlo en el manual de vuelo para no obligar a "
                      "reentrenar pilotos. **Numeral:** ACM/IEEE 1.03 (aprobar solo con creencia "
                      "fundada de que es seguro) y Principio 3 (producto). **Momento de parar:** "
                      "la decisión de arquitectura del sensor único; segundo momento, después del "
                      "primer accidente, cuando se optó por un boletín informativo en vez de dejar "
                      "la flota en tierra. **Detalle que hay que exigir porque es el más "
                      "revelador:** la alerta de discrepancia entre sensores era una opción de "
                      "pago; una función de seguridad convertida en accesorio comercial es una "
                      "decisión ética, no técnica."},
            {"caso": "Equipo 4 · Cambridge Analytica (2018)",
             "clave": "**Decisión:** diseñar una interfaz en la que el consentimiento de un "
                      "usuario alcanzaba para entregar datos **de sus amigos**, que nunca "
                      "instalaron nada. **Numeral:** ACM/IEEE Principio 1 y, en Colombia, **Ley "
                      "1581 de 2012**, principios de **finalidad** (los datos se usaron para algo "
                      "distinto de lo declarado) y **libertad** (no hubo autorización previa, "
                      "expresa e informada de los afectados). **Momento de parar:** el diseño de "
                      "esa interfaz, años antes del escándalo. **Lo que hay que exigir:** que "
                      "digan explícitamente que **era legal** según las reglas de la plataforma y "
                      "aun así indefendible. Es el caso que prueba que la ley es el piso."},
            {"caso": "Equipo 5 · El caso local (está en el taller del estudiante)",
             "clave": "El enunciado que reciben: *un equipo desarrolla la app de citas de un "
                      "consultorio de barrio. Para que el sistema «recuerde» al paciente, guardan "
                      "nombre, cédula, teléfono y el motivo de la consulta en una hoja de cálculo "
                      "compartida por enlace público, porque era la manera rápida de que todos "
                      "pudieran editarla. Nadie le dijo nada a los pacientes.* **Decisión:** usar "
                      "un enlace público para datos de salud, por comodidad de desarrollo. "
                      "**Numeral:** Ley 1581 de 2012 —principios de **seguridad**, **acceso "
                      "restringido** y **libertad**, y el tratamiento reforzado de los **datos "
                      "sensibles**, entre los que está la salud— y ACM/IEEE 1.03, que menciona "
                      "explícitamente no degradar la privacidad. **Momento de parar:** cuando se "
                      "eligió la hoja compartida; la alternativa (permisos por persona) costaba "
                      "cinco minutos. **Por qué este caso está aquí:** es el que le puede pasar a "
                      "cualquiera de ellos este semestre, y por eso el curso prohíbe subir nombres "
                      "y cédulas. La regla del curso no es una formalidad: es esta ley."},
        ],
        "cierre": "Tres minutos, una idea, dicha con estas palabras: **en los cuatro casos el "
                  "software funcionó.** No hubo un error de programación que causara el desastre; "
                  "falló lo que se pidió construir y el hecho de que nadie con información "
                  "suficiente lo detuvo. Recuerde el dato de Volkswagen —el ingeniero que ejecutó "
                  "fue a prisión— porque desarma la idea de que la responsabilidad es siempre del "
                  "jefe, y cierre con la salida práctica, que es la que se llevan para su vida "
                  "laboral: no se les pide heroísmo, se les pide **no ser los únicos que saben**. "
                  "Un correo que deje el riesgo por escrito y escale temprano cambia el caso y "
                  "protege a quien lo escribe. Callar es la única postura sin defensa. Y aterrice "
                  "en el curso: la regla de no subir nombres ni cédulas de terceros no es una "
                  "formalidad del docente, es la Ley 1581 de 2012. Anuncie la sesión 5: hoy el "
                  "daño tenía víctimas con nombre; la próxima, el daño que no tiene nombre y casi "
                  "nadie mide.",
        "conexion": "Hacia atrás: la sesión 3 dejó identificado el **actor no-usuario** de cada "
                    "sistema —el afectado que no lo usa—, y hoy ese actor es exactamente quien "
                    "aparece en los cuatro casos. Hacia adelante: la **sesión 5** extiende el "
                    "análisis al afectado ambiental, que no tiene voz; la **sesión 6** exige que "
                    "la ficha del problema del proyecto declare a quién puede perjudicar; la "
                    "**sesión 13** vuelve sobre impacto social con el proyecto ya construido; y "
                    "todo el manejo de datos del proyecto queda amarrado a la Ley 1581 desde hoy.",
    },

    "errores": [
        {"dice": "«La empresa actuó con negligencia»",
         "por_que": "«La empresa» no decide: deciden personas con un cargo, y sin sujeto el caso no enseña nada.",
         "pida": "Quién tomó la decisión (el rol), en qué momento y con qué información."},
        {"dice": "«El culpable fue el programador que dejó el error»",
         "por_que": "En los cuatro casos el software hizo lo que se le pidió; el error, cuando existió, era inofensivo hasta que alguien quitó la barrera.",
         "pida": "La decisión de diseño o de negocio que convirtió el error en daño."},
        {"dice": "«El código de ética dice que hay que ser responsable»",
         "por_que": "Eso no está en ningún numeral; es una paráfrasis vacía y no puntúa el bloque más pesado.",
         "pida": "El número del principio o del artículo y la cita literal del texto compartido."},
        {"dice": "«Debieron probar mejor el software»",
         "por_que": "Es correcto y es tardío: no toca la decisión que creó el riesgo.",
         "pida": "El momento más temprano en que alguien pudo cambiar el resultado, y qué debía hacer ahí."},
        {"dice": "«Si era legal, no hay problema ético»",
         "por_que": "Cambridge Analytica era legal según las reglas de la plataforma y es indefendible.",
         "pida": "Que apliquen la pregunta 3: ¿aguanta que se sepa? Y que digan quién quedó sin saber."},
    ],

    "dudas": [
        {"p": "¿Y si me despiden por negarme?",
         "r": "Es la objeción honesta y no se le va a responder con heroísmo. Lo que el curso le "
              "pide no es renunciar ni denunciar: es **dejar rastro y escalar temprano**. Un correo "
              "que diga «esto tiene este riesgo para estas personas, lo dejo por escrito» hace que "
              "decida quien tiene la autoridad, sabiendo. Y le recuerdo el dato de Volkswagen: "
              "quien ejecutó calladamente fue a prisión, y eso también le cuesta el trabajo."},
        {"p": "¿Un estudiante de primer semestre ya tiene responsabilidad profesional?",
         "r": "Legalmente la matrícula profesional viene después del título. Pero la Ley 1581 de "
              "2012 y la Ley 1273 de 2009 le aplican **hoy**, como a cualquier persona: si sube "
              "datos de pacientes a un enlace público en el proyecto de este curso, eso ya es un "
              "problema real, no un ejercicio."},
        {"p": "¿Los códigos de ética tienen fuerza legal en Colombia?",
         "r": "El de ACM/IEEE no: es un compromiso profesional internacional, y su fuerza está en "
              "que es el estándar que la profesión reconoce. La **Ley 842 de 2003** sí es ley "
              "colombiana, y el COPNIA puede sancionar y suspender la matrícula profesional con "
              "base en ella. Las leyes 1581 y 1273 tienen consecuencias directas: sanciones "
              "administrativas la primera, penales la segunda."},
        {"p": "¿En el proyecto del curso podemos usar datos reales de personas?",
         "r": "No. Ni nombres, ni cédulas, ni teléfonos, ni fotos de terceros: se usa el rol. Si su "
              "proyecto necesita datos para funcionar, se inventan datos de prueba. Esa regla es la "
              "Ley 1581 de 2012 aplicada a su trabajo, y es la primera cosa que se revisa en el "
              "informe final."},
    ],

    "notas_operativas": [
        "Comparta el **texto del código ACM/IEEE y el de la Ley 842 de 2003** en la carpeta del "
        "curso antes de la sesión. Sin el texto a mano, el bloque del numeral —30 % de la nota— no "
        "se puede hacer y el taller se convierte en opinión.",
        "El caso del equipo 5 (el local, de datos de salud en un enlace público) **no se cambia**: "
        "es el que amarra la clase al proyecto del semestre y a la regla de datos personales del "
        "curso.",
        "Si un equipo trae una cifra de muertos o de multas, pida la fuente y el año. Los números "
        "de estos casos circulan con variaciones.",
        "Al calificar, sea estricto con la **cita literal**. Un resumen del principio, aunque sea "
        "correcto, no vale igual: la habilidad que se está formando es citar la norma que obliga.",
        "Esta sesión no usa asistente de IA. Si un equipo lo usa, la falla típica es un numeral "
        "**inventado**: el asistente cita artículos que no existen con total naturalidad. Verifique "
        "cualquier numeral contra el texto compartido.",
    ],

    "ti_siguiente": {
        "tid": "Lectura del código ético — el código ACM/IEEE completo, los ocho principios, y los "
               "deberes del ingeniero frente a la sociedad de la Ley 842 de 2003.",
        "ti": "Análisis crítico del código ético: media página sobre **un principio que su equipo "
              "cree difícil de cumplir en la práctica**, con el motivo.",
        "adelanto": "el impacto ambiental del software, que es el daño que no tiene una víctima con "
                    "nombre y que casi nadie mide.",
        "aviso": "Traigan leído el código de ética y la regla propia de hoy escrita en el documento "
                 "del equipo. En la sesión 6 esa regla entra en la ficha del problema del proyecto.",
    },

    "cierre_titulo": "Nos vemos en la sesión 5",
    "cierre_frase": "En los cuatro casos el software funcionó. Falló lo que se pidió construir",
}


# =============================================================================
# CLASE 5 · El rol del ingeniero en el contexto ambiental
# =============================================================================

TEMAS[5] = {
    "n": 5,
    "titulo": "El rol del ingeniero en el contexto ambiental",
    "subtitulo": "El software no es inmaterial: pesa, consume agua y termina en basura",
    "hook": "¿Dónde está «la nube»? Y más incómodo: ¿cuánta agua se bebió su última "
            "consulta a un asistente de IA?",
    "hook_lines": [
        "La nube es un edificio con servidores, electricidad y un sistema de enfriamiento.",
        "Hoy le ponemos materia, energía y residuos a algo que parece que no tiene ninguna.",
    ],
    "objetivos": [
        "Nombrar las **cuatro etapas** de la huella material de un sistema de software: fabricación, uso, red y fin de vida.",
        "Explicar qué mide el **PUE** de un centro de datos y por qué el enfriamiento cambia la cuenta.",
        "Relacionar una decisión de diseño con un **efecto ambiental medible**.",
        "Nombrar la norma colombiana de **residuos electrónicos** y qué obliga.",
    ],
    "agenda": {
        "Teoría y guía del docente": "Teoría — huella material, centros de datos, RAEE y matriz eléctrica colombiana",
        "Actividad en equipos": "Taller — huella del sistema, en Excalidraw",
        "Exposiciones": "5 equipos × 3 min — la etapa que más pesa y las dos decisiones que la bajan",
    },
    "herramienta_nota": "El taller se hace en **Excalidraw**, que abre sin cuenta y sirve para "
                        "dibujar rápido y a mano alzada — es lo que se necesita hoy, porque el "
                        "diagrama de la huella es un mapa de flechas, no un plano bonito. El PNG "
                        "exportado va a la carpeta del equipo en Drive. Hoy **no se usa IA**: las "
                        "cifras ambientales son justo donde más inventa.",
    "avance_proyecto": "Ponerle al proyecto del equipo una restricción ambiental verificable y un "
                       "indicador que se pueda medir al final del semestre",

    "teoria": [
        {
            "tipo": "steps",
            "titulo": "Las cuatro etapas de la huella de un sistema",
            "steps": [
                ("FABRICACIÓN", "Minería, ensamblaje y transporte de dispositivos y servidores. **En un celular, la mayor parte de la huella ya está gastada antes de encenderlo**"),
                ("USO", "Electricidad del dispositivo, del servidor y del enfriamiento del centro de datos"),
                ("RED", "Cada byte viaja por antenas, cables y equipos que consumen"),
                ("FIN DE VIDA", "Residuo electrónico (RAEE): metales, plásticos y sustancias peligrosas"),
            ],
            "sub": "«Software» y «nube» son palabras que suenan inmateriales. Las cuatro etapas son materia, energía y residuo — y la etapa 1 cambia la recomendación: alargar la vida útil pesa más que ahorrar batería",
        },
        {
            "tipo": "cards",
            "titulo": "Cuatro conceptos con nombre propio",
            "cards": [
                ("PUE · Power Usage Effectiveness",
                 "Energía total del centro de datos ÷ energía que llega a los servidores. **1.0 "
                 "sería perfecto**: todo va a computar. Un valor de 1.6 significa que por cada "
                 "vatio de cómputo se gastan 0,6 en enfriar, iluminar y perder."),
                ("Agua de enfriamiento",
                 "Muchos centros de datos se enfrían **evaporando agua**, porque es más barato que "
                 "enfriar con electricidad. El costo se muda de la factura de luz a la cuenca de "
                 "donde sale el agua, que suele estar donde vive gente."),
                ("RAEE · Residuos de aparatos eléctricos y electrónicos",
                 "En Colombia los regula la **Ley 1672 de 2013**: obliga a los productores a tener "
                 "sistemas de recolección y al usuario a entregar el aparato en esos puntos, no en "
                 "la basura común. Contienen metales valiosos y sustancias peligrosas."),
                ("Obsolescencia inducida por software",
                 "Cuando una nueva versión exige un dispositivo más nuevo, el software **convierte "
                 "en basura** un aparato que funcionaba. Es una decisión de ingeniería con un "
                 "resultado material medible en toneladas."),
            ],
            "columns": 2,
        },
        {
            "tipo": "before_after",
            "titulo": "La misma función, dos decisiones",
            "before_title": "Decisión cómoda para el equipo",
            "before": [
                "La app pide la ubicación cada 5 segundos.",
                "Cada pantalla trae imágenes en tamaño original.",
                "El reporte se recalcula completo en cada consulta.",
                "La versión nueva solo corre en dispositivos de los últimos 3 años.",
                "«Le metemos IA» a una función que resolvía un `if`.",
            ],
            "after_title": "Misma función, menos huella",
            "after": [
                "Cada 5 minutos, o cuando el usuario se mueve. **Batería y red.**",
                "Imágenes ajustadas al tamaño real. **Menos bytes por la red.**",
                "Se guarda el resultado y se recalcula al cambiar. **Menos cómputo.**",
                "Se sostiene el soporte para dispositivos viejos. **Menos RAEE.**",
                "Se usa el `if`. **La IA cuesta energía en cada llamada.**",
            ],
            "sub": "Ninguna de las cinco decisiones de la derecha es un sacrificio de calidad: son decisiones de ingeniería",
            "size": 13,
        },
        {
            "tipo": "content",
            "titulo": "Colombia: dos datos locales que cambian el análisis",
            "items": [
                "@@La matriz eléctrica.@@ Buena parte de la generación del país es **hidráulica**, "
                "así que un kilovatio-hora consumido en Colombia tiene menos emisiones asociadas "
                "que el mismo kilovatio en un país que quema carbón. Un análisis serio no copia "
                "cifras de emisiones de otro país: **usa el factor local**, que publica el "
                "operador del sistema (XM).",
                "@@Y su contracara.@@ Cuando llega el fenómeno de El Niño y baja el nivel de los "
                "embalses, entran las plantas térmicas y **la misma aplicación pasa a emitir "
                "más sin cambiar una línea de código**. La huella de un sistema no es un número "
                "fijo: depende de cuándo y dónde corre.",
                "@@Residuos electrónicos.@@ La **Ley 1672 de 2013** fija los lineamientos de los "
                "RAEE en Colombia: el productor tiene que ofrecer puntos de recolección y el "
                "usuario tiene el deber de usarlos. Los informes internacionales (Global E-waste "
                "Monitor) muestran que **la mayor parte del residuo electrónico del mundo no se "
                "recoge formalmente**, y lo que no se recoge se desarma a mano, sin protección.",
                "@@Consecuencia práctica para su proyecto:@@ la decisión ambiental más fuerte que "
                "puede tomar un equipo de este curso casi nunca es «consumir menos batería». Es "
                "**no obligar a cambiar de aparato** y **no mover datos que no hacen falta**.",
            ],
            "size": 13,
        },
        {
            "tipo": "steps",
            "titulo": "Cómo se estima una huella sin ser experto",
            "steps": [
                ("1 · Dibuje el recorrido", "Dispositivo → red → servidor → almacenamiento. Todo lo que se prende para que el sistema funcione."),
                ("2 · Cuente lo que se repite", "Lo que pasa una vez no importa; lo que pasa mil veces al día sí. Busque el bucle."),
                ("3 · Marque la etapa más pesada", "Con una sola. No hace falta un número exacto: hace falta saber dónde apretar."),
                ("4 · Proponga dos decisiones", "Concretas y de diseño, no de comportamiento del usuario."),
                ("5 · Defina un indicador", "Algo que se pueda medir al final: bytes por consulta, consultas por día, años de vida útil soportados."),
            ],
            "sub": "El paso 5 es el que distingue una intención ambiental de una decisión de ingeniería",
        },
        {
            "tipo": "box",
            "titulo": "Dos trampas de esta clase",
            "notas": [
                ("advertencia",
                 "**Las cifras ambientales son el terreno favorito de la invención.** Circulan "
                 "números de litros de agua por consulta y de gramos de CO₂ por búsqueda que "
                 "cambian por órdenes de magnitud entre fuentes, y muchos se citan sin decir de "
                 "qué sistema ni de qué año son. Hoy **toda cifra va con fuente, año y alcance** — "
                 "o no va."),
                ("aclaracion",
                 "**«Lo digital contamina menos que el papel» no es una respuesta.** A veces sí y a "
                 "veces no: depende del número de usos, del dispositivo y de si obliga a comprar "
                 "aparatos nuevos. Comparar sirve solo si se dice qué se comparó."),
                ("info",
                 "**Lo que sí se puede afirmar sin exagerar:** que la huella existe, que tiene "
                 "cuatro etapas, que se puede reducir con decisiones de diseño y que casi nadie la "
                 "mide. Eso alcanza para trabajar con rigor en primer semestre."),
            ],
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada: darle materia a algo que parece no tenerla",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "«¿Dónde está la nube?» funciona porque casi nadie ha visto un centro de datos y "
                "porque la metáfora está diseñada para que no se piense en el edificio. La segunda "
                "parte —cuánta agua se bebió una consulta a un asistente de IA— incomoda a "
                "propósito y hay que manejarla con cuidado: la respuesta honesta es que **depende "
                "del centro de datos, del modelo, del clima y del año**, y que las cifras que "
                "circulan varían por órdenes de magnitud. Eso no debilita la clase: es la clase. "
                "El objetivo no es que se lleven un número, es que entiendan que hay agua y "
                "electricidad detrás de algo que se siente inmaterial, y que quien afirme un "
                "número tiene que decir de dónde salió.",
                "Recoja las respuestas en el muro y no las corrija. En el minuto 20, al llegar al "
                "PUE y al enfriamiento, vuelva al muro: alguien va a haber escrito «en internet» o "
                "«en un servidor», y ahí se muestra que el servidor está en un edificio que "
                "consume tanto en enfriarse como en computar.",
            ],
        },
        {
            "titulo": "Las cuatro etapas y por qué la fabricación cambia la recomendación",
            "slide": "{{slide:Las cuatro etapas}}",
            "cuerpo": [
                "La huella material de un sistema de software se reparte en cuatro etapas y "
                "conviene recorrerlas con un ejemplo único: una aplicación de citas médicas usada "
                "desde el celular.",
                "**Fabricación.** El celular del paciente, el computador de la secretaria y los "
                "servidores donde corre el sistema tuvieron que ser fabricados: minería de metales "
                "—incluidos varios escasos y con extracción problemática—, ensamblaje y "
                "transporte. Este es el punto que más sorprende y el más importante para las "
                "decisiones: **en muchos dispositivos personales la mayor parte de la huella de "
                "toda su vida ya está gastada cuando se enciende por primera vez**. La consecuencia "
                "es contraintuitiva: optimizar el consumo de batería es útil, pero **alargar la "
                "vida útil del aparato pesa mucho más**, y eso depende de decisiones de software.",
                "**Uso.** Electricidad del dispositivo, del servidor y —esto es lo que se olvida— "
                "del enfriamiento del centro de datos. Aquí entra el PUE.",
                "**Red.** Cada byte que viaja pasa por antenas, cables, enrutadores y equipos que "
                "consumen. No es gratis y crece con el volumen: una pantalla que carga imágenes en "
                "tamaño original mil veces al día mueve un múltiplo de lo necesario.",
                "**Fin de vida.** El aparato se vuelve residuo electrónico. Tiene metales "
                "recuperables y sustancias peligrosas, y cuando no se recoge formalmente se "
                "desarma a mano, quemando plásticos, con daño directo a las personas que lo hacen.",
                "El punto pedagógico de la diapositiva es que las palabras «software» y «nube» "
                "están construidas para que uno no piense en nada de esto. Nombrar las cuatro "
                "etapas es lo que permite discutir el tema con seriedad.",
            ],
        },
        {
            "titulo": "PUE, agua, RAEE y obsolescencia: los cuatro conceptos que hay que dejar",
            "slide": "{{slide:Cuatro conceptos con nombre propio}}",
            "cuerpo": [
                "**PUE (Power Usage Effectiveness).** Es la energía total que entra al centro de "
                "datos dividida por la energía que efectivamente llega a los servidores. Si fuera "
                "1.0, todo lo que entra se usa en computar. Un PUE de 1.6 significa que por cada "
                "vatio de cómputo se gastan 0,6 en enfriar, iluminar y en pérdidas. Los centros de "
                "datos grandes y modernos operan bastante mejor que el promedio de las salas de "
                "servidores de empresa, que suelen estar en el rango de 1.5 a 1.6 según las "
                "encuestas del sector. La idea que hay que dejar no es el número exacto: es que "
                "**una parte grande de la energía de un centro de datos no computa nada**, y que "
                "existe una métrica con nombre para medirlo. Un ingeniero que sabe que el PUE "
                "existe puede preguntar por él.",
                "**El agua.** Enfriar con evaporación de agua es más barato en electricidad que "
                "enfriar con máquinas, así que muchos centros de datos usan agua. Eso traslada el "
                "costo: baja la factura de luz y sube el consumo de una cuenca que normalmente "
                "abastece a población. Es un buen ejemplo de algo que el curso repite: **optimizar "
                "una variable suele mover el problema a otra**, y el ingeniero tiene que saber a "
                "cuál. Hay métricas para esto (WUE, litros por kilovatio-hora), y aquí también "
                "vale la advertencia de las cifras.",
                "**RAEE y la Ley 1672 de 2013.** Es la norma colombiana que fija los lineamientos "
                "para la gestión de residuos de aparatos eléctricos y electrónicos. Lo que hay que "
                "poder decir: **obliga a los productores** a establecer sistemas de recolección y "
                "gestión, y **establece el deber del usuario** de entregar el aparato en esos "
                "puntos en vez de tirarlo a la basura común. Los informes globales de residuos "
                "electrónicos (Global E-waste Monitor, de UNITAR e ITU) reportan decenas de "
                "millones de toneladas al año y una tasa de recolección formal baja: el orden de "
                "magnitud es que **la mayor parte no se recoge**. Si un equipo cita una cifra "
                "exacta, exija la edición del informe y el año, porque cambia entre ediciones.",
                "**Obsolescencia inducida por software.** Es el concepto que más les sirve porque "
                "está bajo su control profesional. Cuando una nueva versión de una aplicación "
                "—o de un sistema operativo— deja de funcionar en dispositivos que servían, el "
                "software convierte en basura un aparato que estaba bien. No hace falta discutir "
                "si hay intención: el efecto es material y medible. Y la contracara es una "
                "decisión concreta que un equipo de este curso puede tomar: **sostener el soporte "
                "para dispositivos viejos**, que además es lo correcto para el contexto de la "
                "universidad, donde muchos estudiantes trabajan con equipos de varios años.",
            ],
        },
        {
            "titulo": "De la conciencia a la decisión: la diapositiva que convierte el tema en ingeniería",
            "slide": "{{slide:La misma función, dos decisiones}} {{slide:Cómo se estima una huella}}",
            "cuerpo": [
                "Esta es la diapositiva que salva la clase de volverse un discurso. Las cinco "
                "parejas son decisiones reales de diseño, y en las cinco la versión de la derecha "
                "**cumple la misma función**. Eso hay que decirlo explícitamente: no se está "
                "pidiendo sacrificar calidad por ambiente, se está pidiendo no desperdiciar.",
                "La primera —pedir la ubicación cada cinco segundos o cada cinco minutos— es la "
                "más fácil de entender y toca batería y red a la vez. La tercera —guardar el "
                "resultado en vez de recalcular el reporte completo en cada consulta— es la que "
                "más sorprende, porque el estudiante todavía no tiene la intuición de que el "
                "cómputo cuesta energía; sirve para conectar con la sesión 7 y con la idea de que "
                "la eficiencia no es coquetería de programador. La cuarta —sostener dispositivos "
                "viejos— es la de mayor impacto real por lo dicho sobre la fabricación. Y la "
                "quinta es la más contemporánea y hay que decirla sin miedo: **agregarle un "
                "asistente de IA a una función que resolvía una condición simple gasta energía en "
                "cada llamada, para siempre**. Es una decisión de arquitectura, y hoy se toma con "
                "frecuencia por moda.",
                "El método de cinco pasos es el del taller. El paso 2 —buscar lo que se repite— es "
                "el que enseña a estimar: lo que ocurre una vez no mueve la aguja, lo que ocurre "
                "mil veces al día sí. Y el paso 5 —definir un indicador medible— es el que "
                "separa una intención de una decisión de ingeniería. «Vamos a ser sostenibles» no "
                "se puede verificar; «vamos a mover menos de 200 KB por consulta» sí, y en la "
                "sesión 16 se puede mirar si se cumplió.",
            ],
        },
        {
            "titulo": "Colombia, y la honestidad con las cifras",
            "slide": "{{slide:Colombia}} {{slide:Dos trampas}}",
            "cuerpo": [
                "El dato local más útil es la composición de la matriz eléctrica. Una parte "
                "importante de la generación en Colombia es hidráulica, lo que significa que un "
                "kilovatio-hora consumido aquí tiene un factor de emisiones distinto —menor— que "
                "en un país con generación a carbón. La consecuencia metodológica es la que hay "
                "que enseñar: **no se copian factores de emisión de otro país**; se usa el factor "
                "local, y el operador del sistema (XM) publica datos de generación. Un equipo que "
                "cite una fuente colombiana en vez de un blog extranjero ya está haciendo "
                "ingeniería.",
                "La contracara es igual de importante y menos conocida: cuando el fenómeno de El "
                "Niño reduce los aportes a los embalses, entran las plantas térmicas y el factor "
                "de emisiones del país sube. Es decir, **la misma aplicación, sin cambiar una "
                "línea de código, emite más en un año seco**. Eso enseña algo que vale para todo "
                "el curso: la huella de un sistema no es una propiedad del sistema, es una "
                "propiedad del sistema en su contexto.",
                "La diapositiva de las trampas es la más importante para el rigor y conviene "
                "dedicarle tiempo real. Las cifras ambientales del sector digital son un campo "
                "donde circulan números espectaculares sin alcance definido: litros de agua por "
                "consulta a un modelo de lenguaje, gramos de CO₂ por búsqueda, porcentajes del "
                "consumo mundial de electricidad. Muchos provienen de estimaciones legítimas pero "
                "con supuestos muy específicos, y se citan luego como hechos universales. La regla "
                "del curso a partir de hoy es simple y se aplica en la rúbrica: **cifra con fuente, "
                "año y alcance, o no va**. Y hay que decir en voz alta lo que sí se puede afirmar "
                "sin exagerar: que la huella existe, que tiene cuatro etapas, que se puede reducir "
                "con decisiones de diseño y que casi nadie la mide. Con eso alcanza para trabajar "
                "con seriedad, y es mucho más defendible que un número impresionante mal citado.",
                "Sobre la comparación «lo digital contra el papel»: alguien la va a proponer y la "
                "respuesta correcta es que depende del número de usos y de si obliga a comprar "
                "dispositivos. Un documento leído una vez en un computador nuevo no gana contra "
                "una hoja; el mismo documento leído por trescientas personas en aparatos que ya "
                "existen, sí. La lección es que **comparar sin decir qué se comparó no es un "
                "argumento**.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:10 · Apertura · [Slide 4]",
            "cuerpo": [
                "Comparta pantalla antes de que entre el primero:",
                "> «¿Dónde está la nube? ¿Y cuánta agua se bebió su última consulta a un asistente "
                "de IA?»",
                "**[Nota docente]:** enlace del muro en el chat. Van a escribir «en internet», «en "
                "un servidor», «en Estados Unidos». Ninguna se corrige ahora.",
                "**[Nota docente]:** si alguien escribe una cifra de agua, márquela: en el minuto "
                "35 esa cifra es el mejor ejemplo de la diapositiva de las trampas.",
            ],
        },
        {
            "titulo": "00:10–00:55 · Teoría · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9][Slide 10]",
            "cuerpo": [
                "Reparto sugerido de los 45 min:",
                "- **9 min** · Las cuatro etapas [Slide 5]. Use un solo ejemplo (la app de citas) y "
                "recórralo por las cuatro. Detenga la clase en **fabricación**: la mayor parte de "
                "la huella de un celular ya está gastada al encenderlo.",
                "- **9 min** · Los cuatro conceptos [Slide 6]. **Vuelva al muro** al explicar PUE y "
                "enfriamiento: ahí se responde «¿dónde está la nube?».",
                "- **10 min** · La misma función, dos decisiones [Slide 7]. Es la diapositiva que "
                "convierte el tema en ingeniería. Diga explícitamente que la columna derecha "
                "**cumple la misma función**.",
                "- **7 min** · Colombia [Slide 8]. Matriz hidráulica, El Niño y la Ley 1672 de 2013.",
                "- **5 min** · Cómo se estima una huella [Slide 9]. Es el método del taller.",
                "- **5 min** · Las dos trampas [Slide 10]. **No la recorte**: es la que sostiene el "
                "rigor de la sesión y de la rúbrica.",
                "**[Nota docente]:** si el tiempo aprieta, recorte Colombia a cuatro minutos "
                "quedándose con la matriz hidráulica y la Ley 1672. La diapositiva de las dos "
                "decisiones y la de las trampas no se recortan.",
            ],
        },
        {
            "titulo": "00:55–01:12 · Taller en salas de grupo · [Slide 11]",
            "cuerpo": [
                "**3 min** para abrir Excalidraw y repartir. Cada equipo trabaja **el sistema de "
                "su propio proyecto**, el que viene de las sesiones 1 y 3.",
                "**14 min** de trabajo. Entre a las cinco salas, ~3 min cada una, y revise **una "
                "sola cosa: el indicador medible del paso 5**. Es donde se cae el taller.",
                "**[Nota docente]:** la falla más común es proponer decisiones sobre el "
                "comportamiento del usuario («que apaguen el celular»). Corte eso en caliente: se "
                "piden decisiones **de diseño**, que están bajo control del equipo.",
                "**[Nota docente]:** si aparece una cifra sin fuente, pídala en el momento. Si no "
                "la tienen, que la borren y escriban la afirmación sin número: se califica mejor "
                "una afirmación honesta que una cifra inventada.",
            ],
        },
        {
            "titulo": "01:12–01:27 · Exposiciones · [Slide 12]",
            "cuerpo": [
                "5 equipos × 3 min con el diagrama compartido. **El minuto obligatorio es «la etapa "
                "que más pesa y por qué»**, y el cierre de cada exposición es el indicador.",
                "**[Nota docente]:** los cinco enlaces (o los PNG) en el chat antes de arrancar.",
                "**[Nota docente]:** anote los cinco indicadores. En la sesión 16 se revisa si se "
                "cumplieron, y tener la lista de hoy es lo que hace posible esa revisión.",
            ],
        },
        {
            "titulo": "01:27–01:30 · Cierre · [Slide 13][Slide 14]",
            "cuerpo": [
                "Una idea: **el software no es inmaterial.** Tiene fabricación, consumo, red y "
                "residuo, y las decisiones que bajan la huella son decisiones de diseño, no de "
                "buena voluntad. La más fuerte que ellos pueden tomar es no obligar a cambiar de "
                "aparato.",
                "Anuncie la sesión 6: **cierra el corte 1** y sale la ficha del problema del "
                "proyecto, con evaluación de corte en ExamLab al final de la sesión.",
            ],
        },
    ],

    "taller": {
        "archivo": "Huella del sistema",
        "titulo": "Huella del sistema",
        "min": 17,
        "exposicion": 3,
        "consigna": "Dibujen en Excalidraw la **huella material** del sistema de su proyecto: por "
                    "dónde pasa la energía, la materia y el residuo en las cuatro etapas. Marquen "
                    "cuál etapa pesa más, propongan **dos decisiones de diseño** que la bajen y "
                    "definan **un indicador medible** que se pueda revisar en la sesión 16.",
        "entregable": "un diagrama de huella en Excalidraw exportado a PNG en la carpeta del equipo, "
                      "más las dos decisiones y el indicador escritos en el documento del equipo",
        "entregable_corto": "diagrama de huella + 2 decisiones + 1 indicador",
        "reparto_titulo": "El sistema no se sortea:",
        "reparto": "cada equipo trabaja el sistema de su propio proyecto, el que viene de las "
                   "sesiones 1 y 3. El indicador que definan hoy entra en la ficha del problema de "
                   "la sesión 6 y se revisa en el informe final.",
        "reparto_corto": "cada equipo, el sistema de su propio proyecto",
        "bloques": [
            {"clave": "EL RECORRIDO DIBUJADO",
             "pide": "El camino completo con flechas: dispositivo del usuario → red → servidor → "
                     "almacenamiento, y todo lo que se prende para que el sistema funcione.",
             "check": "el diagrama tiene las cuatro etapas señaladas (fabricación, uso, red, fin de vida), no solo el flujo de datos."},
            {"clave": "LO QUE SE REPITE",
             "pide": "Qué operación ocurre **muchas veces al día** en su sistema, y una estimación "
                     "gruesa de cuántas veces. Lo que pasa una vez no mueve nada.",
             "check": "hay una operación repetida y un número estimado, aunque sea aproximado y así declarado."},
            {"clave": "LA ETAPA QUE MÁS PESA",
             "pide": "Una sola etapa, con la razón. No hace falta un cálculo exacto: hace falta "
                     "saber dónde apretar.",
             "check": "hay una etapa elegida y un argumento. Si dicen «todas pesan», no eligieron."},
            {"clave": "DOS DECISIONES DE DISEÑO",
             "pide": "Dos cosas que **ustedes** pueden decidir en su sistema para bajar esa etapa. "
                     "De diseño, no de comportamiento del usuario.",
             "check": "las dos decisiones están bajo su control. «Que el usuario cargue menos el celular» no lo está."},
            {"clave": "EL INDICADOR",
             "pide": "Un número que se pueda medir al final del semestre para saber si la decisión "
                     "funcionó. Con su unidad.",
             "check": "tiene unidad y se puede medir con lo que ustedes van a construir. «Ser sostenibles» no es un indicador."},
        ],
        "expo": [
            ("40 s · El recorrido", "El diagrama, recorrido con el cursor. Dónde está cada etapa."),
            ("30 s · Lo que se repite", "La operación repetida y cuántas veces al día."),
            ("50 s · La etapa que más pesa", "Cuál y por qué. Es el minuto obligatorio."),
            ("50 s · Las dos decisiones y el indicador", "Qué van a cambiar y cómo se sabrá si sirvió."),
            ("10 s · La fuente", "De dónde salió cualquier cifra que hayan dicho."),
        ],
    },

    "rubrica": [
        ("El diagrama muestra las cuatro etapas, no solo el flujo de datos", 20,
         "La etapa de fabricación y la de fin de vida son las que nadie dibuja, y suelen ser las que más pesan."),
        ("Hay una operación repetida con una estimación declarada como estimación", 15,
         "Estimar y decir que se está estimando es la habilidad honesta que reemplaza a inventar cifras."),
        ("Se eligió UNA etapa como la más pesada, con argumento", 20,
         "Elegir es el trabajo del ingeniero. «Todo importa» no permite actuar."),
        ("Las dos decisiones son de diseño y están bajo control del equipo", 25,
         "Es lo que convierte la conciencia ambiental en ingeniería."),
        ("El indicador tiene unidad y se puede medir en la sesión 16", 20,
         "Sin indicador no hay forma de saber si la decisión sirvió, y el informe final lo pide."),
    ],

    "solucion": {
        "para_que": "Este documento resuelve la huella completa de un sistema concreto —una app de "
                    "citas para un consultorio de barrio— y trae al final las claves de los cuatro "
                    "tipos de proyecto que suelen aparecer. Sirve sobre todo para dos cosas que el "
                    "docente necesita en el momento: distinguir una decisión de diseño de una "
                    "recomendación al usuario, y tener ejemplos de indicadores bien formulados, "
                    "que es donde se cae el taller.",
        "caso_titulo": "App de citas de un consultorio de barrio · huella completa",
        "caso": "El sistema: los pacientes piden cita desde el celular, la secretaria administra la "
                "agenda desde un computador de escritorio de hace siete años, y el sistema corre en "
                "un servicio en la nube de plan gratuito. Unos 60 pacientes al día. La app consulta "
                "el estado de la agenda cada 10 segundos mientras está abierta, para que el cupo se "
                "vea «en vivo», y cada pantalla carga la foto del consultorio en tamaño original.",
        "por_que_este_caso": "Se eligió porque tiene las dos fallas típicas plantadas a propósito "
                             "—el sondeo cada 10 segundos y la imagen sin ajustar— y porque el "
                             "computador de siete años de la secretaria obliga a hablar de la "
                             "decisión de mayor impacto real: no forzar el cambio de aparato.",
        "bloques": [
            {
                "clave": "EL RECORRIDO DIBUJADO",
                "respuesta": "**Etapa 1 · Fabricación.** 60 celulares de pacientes al día (que ya "
                             "existen y se usan para otras cosas), 1 computador de escritorio de "
                             "siete años en el consultorio, y la fracción que le corresponde al "
                             "sistema de los servidores del proveedor de nube, que están "
                             "compartidos con miles de otros clientes.\n\n"
                             "**Etapa 2 · Uso.** Electricidad del celular mientras la app está "
                             "abierta (pantalla y radio son lo que más gasta), electricidad del "
                             "computador del consultorio encendido ocho horas al día, y "
                             "electricidad del servidor **más su enfriamiento** —aquí entra el "
                             "PUE: si el centro de datos tiene PUE 1.5, por cada vatio que computa "
                             "el sistema se gasta medio vatio en enfriar.\n\n"
                             "**Etapa 3 · Red.** Cada consulta viaja del celular a la antena "
                             "celular, de ahí a la red del operador y al centro de datos. Se dibuja "
                             "como una cadena, no como una flecha: la antena y los equipos "
                             "intermedios también consumen.\n\n"
                             "**Etapa 4 · Fin de vida.** El computador del consultorio, cuando se "
                             "reemplace, es RAEE: debe entregarse en un punto de recolección del "
                             "productor, por la Ley 1672 de 2013, no en la basura común. Los "
                             "celulares de los pacientes también, pero **el sistema no controla "
                             "eso**; lo que el sistema sí controla es si obliga a cambiarlos.",
                "como_calificar": "20 pts. Lo que decide es que **estén las cuatro etapas**, no la "
                                  "belleza del diagrama. Casi todos los equipos dibujan bien el uso "
                                  "y la red —que es el flujo de datos que ya intuyen— y omiten "
                                  "fabricación y fin de vida. Un diagrama con solo uso y red vale "
                                  "8. Si el equipo señala que la fabricación del servidor es "
                                  "**compartida** con otros clientes, súbale: es un razonamiento "
                                  "correcto y fino."
            },
            {
                "clave": "LO QUE SE REPITE",
                "respuesta": "**La operación repetida es la consulta del estado de la agenda cada "
                             "10 segundos mientras la app está abierta.** Estimación gruesa, "
                             "declarada como estimación: si un paciente tiene la app abierta unos 3 "
                             "minutos para pedir su cita, son unas 18 consultas por paciente; con "
                             "60 pacientes al día, del orden de **1.000 consultas diarias solo para "
                             "mostrar algo que casi nunca cambió**.\n\n"
                             "La segunda operación repetida es la carga de la foto del consultorio "
                             "en cada pantalla. Si la imagen original pesa, por decir algo "
                             "verificable midiéndola, 2 MB, y se carga en cada una de las 3 "
                             "pantallas por paciente, son unos 6 MB por paciente y del orden de "
                             "**360 MB diarios de red** para mostrar la misma foto.\n\n"
                             "Las dos cifras están calculadas a partir de datos que el equipo "
                             "puede medir en su propio sistema (peso del archivo, número de "
                             "pantallas, número de pacientes). Eso es lo que se pide: **no una "
                             "cifra de internet, sino una estimación construida y declarada**.",
                "como_calificar": "15 pts. El criterio es doble: que haya un número **y** que esté "
                                  "declarado como estimación con el razonamiento visible. Una cifra "
                                  "sin razonamiento vale 5, aunque sea plausible. Un razonamiento "
                                  "correcto sin número vale 8. Los 15 completos exigen "
                                  "«aproximadamente X, calculado así»."
            },
            {
                "clave": "LA ETAPA QUE MÁS PESA",
                "respuesta": "**La etapa 1, fabricación**, y el argumento es el del computador de "
                             "siete años del consultorio. En un dispositivo personal la mayor parte "
                             "de la huella de toda su vida se gasta al fabricarlo, así que la "
                             "decisión con más efecto material no es ahorrar electricidad: es que "
                             "el sistema **siga funcionando en ese computador** y no obligue a "
                             "comprar uno nuevo. Un equipo que decida usar una tecnología que solo "
                             "corre en navegadores muy recientes está tomando, sin darse cuenta, "
                             "una decisión con consecuencia en toneladas de residuo.\n\n"
                             "**Respuesta alternativa igual de válida: la etapa 3, red**, con el "
                             "argumento de las 1.000 consultas y los 360 MB diarios, que es dinero "
                             "y datos de los pacientes además de energía. Lo que **no** se acepta "
                             "es «todas pesan igual»: eso significa que no eligieron y no permite "
                             "actuar.",
                "como_calificar": "20 pts. Se acepta cualquier etapa **con argumento consistente "
                                  "con lo que escribieron antes**. Un equipo que elija «uso» "
                                  "argumentando solo el consumo de la batería del celular vale 10: "
                                  "es la respuesta intuitiva y la más débil, porque la batería del "
                                  "celular es lo pequeño de la cuenta. «Todas pesan» vale 0 y hay "
                                  "que decirlo con el argumento: elegir es el trabajo del ingeniero."
            },
            {
                "clave": "DOS DECISIONES DE DISEÑO",
                "respuesta": "**Decisión 1 · Cambiar el sondeo por actualización bajo demanda.** En "
                             "vez de consultar la agenda cada 10 segundos, se consulta al abrir la "
                             "pantalla y cuando el paciente hace algo (recargar, confirmar). Baja "
                             "de unas 18 consultas por paciente a 2 o 3. Es una decisión de diseño, "
                             "está bajo control del equipo, y **no le quita nada al paciente**: la "
                             "probabilidad de que un cupo cambie en los 10 segundos exactos que él "
                             "está mirando es mínima.\n\n"
                             "**Decisión 2 · Sostener el soporte del computador de siete años.** "
                             "Concretamente: no usar funciones que exijan un navegador de última "
                             "generación, probar el sistema en ese computador antes de cada entrega, "
                             "y ajustar las imágenes al tamaño real en que se muestran (la foto de "
                             "2 MB pasa a unos 80 KB). Baja red y evita el reemplazo del aparato, "
                             "que es la parte gorda de la huella.\n\n"
                             "**Ejemplos de lo que NO cuenta como decisión de diseño:** «pedirle a "
                             "la secretaria que apague el computador al mediodía», «recomendar a los "
                             "pacientes que usen wifi en vez de datos», «concientizar sobre el "
                             "reciclaje». Las tres pueden ser buenas ideas y ninguna está bajo "
                             "control del equipo: son comportamiento de otros.",
                "como_calificar": "25 pts, 12,5 por decisión. El criterio único y estricto es "
                                  "**¿está bajo control del equipo?**. Una recomendación al usuario "
                                  "vale 0 como decisión, aunque sea sensata; dígalo en el momento "
                                  "en la sala, porque es el error más frecuente del taller. Si las "
                                  "dos decisiones atacan la etapa que el equipo eligió como más "
                                  "pesada, dé los 25; si atacan otra, máximo 15, porque hay "
                                  "incoherencia entre el diagnóstico y la acción."
            },
            {
                "clave": "EL INDICADOR",
                "respuesta": "**Indicadores bien formulados para este caso:**\n\n"
                             "- «**Consultas al servidor por cita agendada.** Hoy ~18. Meta: menos "
                             "de 4. Se mide contando las peticiones en el registro del servidor.»\n"
                             "- «**Kilobytes transferidos por pantalla.** Hoy ~2.000 KB por la "
                             "imagen. Meta: menos de 200 KB. Se mide con las herramientas del "
                             "navegador.»\n"
                             "- «**El sistema funciona en el computador de siete años del "
                             "consultorio: sí / no.** Se verifica abriéndolo ahí antes de cada "
                             "entrega.»\n\n"
                             "Los tres tienen unidad (o son un sí/no verificable), se miden con "
                             "algo que el equipo va a tener, y se pueden revisar en la sesión 16.\n\n"
                             "**Indicadores mal formulados y por qué:** «reducir el consumo "
                             "energético» (no tiene unidad ni línea base); «ser un sistema "
                             "sostenible» (no es medible); «bajar las emisiones de CO₂ en un 30 %» "
                             "(el equipo no puede medir eso, y para calcularlo necesitaría el factor "
                             "de emisiones y datos del centro de datos que no tiene).",
                "como_calificar": "20 pts. Tres requisitos: **unidad, línea base o valor de hoy, y "
                                  "cómo se mide**. Si falta el «cómo se mide», máximo 10: es el "
                                  "requisito que convierte el indicador en algo revisable. El "
                                  "indicador de emisiones de CO₂ vale 5 aunque suene ambicioso, y "
                                  "hay que explicar por qué: proponer medir lo que no se puede "
                                  "medir es peor que proponer algo modesto y verificable. **Anote "
                                  "los cinco indicadores**: se revisan en la sesión 16."
            },
        ],
        "variantes": [
            {"caso": "Proyecto de tipo inventario o ventas de un negocio",
             "clave": "La operación repetida suele ser la consulta de existencias o la "
                      "recalculación de un reporte en cada carga. La etapa más pesada suele ser "
                      "**uso**, por el cómputo repetido, y la decisión fuerte es guardar el "
                      "resultado y recalcular solo al cambiar. Buen indicador: «segundos para "
                      "cargar el reporte» o «consultas a la base por venta registrada». Cuidado con "
                      "la trampa: los equipos proponen «imprimir menos facturas», que es "
                      "comportamiento del negocio, no diseño."},
            {"caso": "Proyecto con formularios o encuestas",
             "clave": "La huella es baja y hay que decírselo: no todo proyecto tiene un problema "
                      "ambiental grande, y **reconocerlo es más honesto que inflarlo**. La etapa "
                      "que suele pesar es **red**, por adjuntos y fotos sin ajustar. Decisión "
                      "fuerte: comprimir en el dispositivo antes de subir. Indicador: «KB promedio "
                      "por respuesta enviada». Si el equipo dice honestamente que su huella "
                      "dominante es la fabricación de los dispositivos que ya existen y que su "
                      "margen de acción es pequeño, dé la nota completa: eso es análisis correcto."},
            {"caso": "Proyecto que incluye un asistente de IA",
             "clave": "Es el caso donde la clase pega más fuerte. La etapa **uso** domina, porque "
                      "cada llamada al modelo consume cómputo en un centro de datos. La decisión de "
                      "diseño más potente es la de la diapositiva: **no llamar al modelo cuando una "
                      "regla simple resuelve**, y guardar respuestas repetidas en vez de volver a "
                      "preguntar. Indicador: «llamadas al modelo por usuario atendido». Exija "
                      "honestidad con las cifras: no hay un número público confiable de energía por "
                      "consulta, así que se mide **el número de llamadas**, que sí se puede contar."},
            {"caso": "Proyecto de hardware, sensores o IoT",
             "clave": "Aquí la etapa 1 (fabricación) y la 4 (fin de vida) son las dominantes y por "
                      "primera vez son físicas y propias del equipo: cada sensor es un aparato que "
                      "se fabricó y que va a ser residuo. Decisión fuerte: menos dispositivos con "
                      "más cobertura, y batería reemplazable. Indicador: «número de dispositivos "
                      "por área cubierta» o «meses de vida útil esperada». Es el único caso donde "
                      "el equipo debería mencionar explícitamente la Ley 1672 de 2013, porque va a "
                      "generar RAEE de verdad."},
        ],
        "cierre": "Tres minutos, una idea: **el software no es inmaterial.** Tiene cuatro etapas "
                  "—fabricación, uso, red y fin de vida— y en las cuatro hay energía, materia y "
                  "residuo. Diga el dato que más reordena las prioridades: en un dispositivo "
                  "personal la mayor parte de la huella ya está gastada cuando se enciende, así que "
                  "**la decisión ambiental más fuerte que ellos pueden tomar no es ahorrar batería, "
                  "es no obligar a cambiar de aparato**. Cierre con la honestidad de las cifras, "
                  "porque es lo que los va a distinguir: la huella existe, se puede reducir con "
                  "decisiones de diseño y casi nadie la mide; cualquier número que digan va con "
                  "fuente, año y alcance. Y anuncie la sesión 6 sin adornos: cierra el corte 1, "
                  "sale la ficha del problema del proyecto —que ya viene armándose desde la sesión "
                  "1— y hay evaluación de corte en ExamLab al final de la sesión.",
        "conexion": "Hacia atrás: la sesión 3 dio la frontera del sistema, y hoy la huella obligó a "
                    "estirarla hasta la fabricación y el residuo, que casi nadie mete dentro; la "
                    "sesión 4 dio el afectado con nombre, y hoy apareció el afectado sin nombre. "
                    "Hacia adelante: el **indicador** de hoy entra en la ficha del problema de la "
                    "**sesión 6** y se revisa en el informe final de la **sesión 16**; la eficiencia "
                    "como decisión de diseño reaparece en la **sesión 7** (ciclo de vida) y en la "
                    "**sesión 10**; y la **sesión 13** retoma impacto social y ambiental con el "
                    "prototipo ya construido.",
    },

    "errores": [
        {"dice": "«La nube no contamina, es virtual»",
         "por_que": "La nube es un edificio con servidores, electricidad y enfriamiento, muchas veces con agua.",
         "pida": "Que dibujen dónde está el servidor y qué se prende para que funcione. Y que nombren el PUE."},
        {"dice": "«Vamos a pedirle al usuario que ahorre energía»",
         "por_que": "No es una decisión de diseño: es comportamiento de otra persona, fuera de su control.",
         "pida": "Algo que ellos puedan decidir en su propio sistema: cada cuánto consulta, cuánto pesa lo que envía, qué dispositivos soporta."},
        {"dice": "«Todas las etapas pesan igual»",
         "por_que": "Significa que no eligieron, y sin elegir no se puede actuar.",
         "pida": "Una sola etapa y el argumento, aunque sea aproximado."},
        {"dice": "«Cada consulta a la IA gasta X litros de agua»",
         "por_que": "Las cifras que circulan varían por órdenes de magnitud y casi nunca dicen de qué sistema ni de qué año son.",
         "pida": "Fuente, año y alcance. Si no lo tienen, que midan lo que sí pueden contar: el número de llamadas."},
        {"dice": "«Ser un sistema sostenible» como indicador",
         "por_que": "No tiene unidad y no se puede revisar en la sesión 16.",
         "pida": "Un número con unidad, el valor de hoy y cómo se va a medir."},
    ],

    "dudas": [
        {"p": "¿No es exagerado hablar de agua y minería en un curso de primer semestre?",
         "r": "Es lo contrario: es el momento de decirlo, porque las decisiones que más pesan se "
              "toman al diseñar y ustedes están aprendiendo a diseñar. Y no se les pide militancia: "
              "se les pide saber que la huella existe, poder nombrar sus cuatro etapas y tomar dos "
              "decisiones que la bajen sin perder función."},
        {"p": "¿Y si nuestro proyecto casi no tiene huella?",
         "r": "Entonces escríbanlo así, con el argumento, y les vale nota completa. Inflar el "
              "impacto ambiental de un formulario es tan malo como negar el de un centro de datos. "
              "Lo que se califica es el análisis, no el tamaño del problema."},
        {"p": "¿Dónde consigo el factor de emisiones de Colombia?",
         "r": "El operador del sistema eléctrico (XM) publica datos de generación y composición de "
              "la matriz. Úsenlo con el año, y tengan presente que en años de El Niño el factor "
              "sube porque entran las térmicas. No copien un factor de otro país: el de Colombia "
              "es distinto por la generación hidráulica."},
        {"p": "¿Usar IA en el proyecto está mal ambientalmente?",
         "r": "No está mal ni bien por sí solo: es una decisión con un costo. Lo que sí es un error "
              "de ingeniería es llamar a un modelo para algo que resuelve una condición simple, "
              "porque ese costo se paga en cada llamada, para siempre. Si su proyecto la usa, "
              "cuenten las llamadas: es lo único que pueden medir de verdad."},
    ],

    "notas_operativas": [
        "Las cinco salas de grupo se crean **antes** de la sesión.",
        "Hoy **no se usa IA**: es la sesión donde más inventa cifras. Si un equipo la usa, verifique "
        "cualquier número contra una fuente con año.",
        "La falla más frecuente del taller es proponer **comportamiento del usuario** en vez de "
        "decisiones de diseño. Córtela en la primera sala, no en la calificación.",
        "**Anote los cinco indicadores** que salgan de las exposiciones. Se revisan en la sesión 16 "
        "y esta es la única oportunidad de tenerlos todos juntos.",
        "Si algún equipo pide fuentes, las útiles y verificables son: los datos de generación de XM "
        "para Colombia, la Ley 1672 de 2013 para RAEE, y el Global E-waste Monitor para residuos "
        "globales. Pida siempre el año de la edición.",
        "**Publique hoy** el documento «Evaluación del Corte 1 — cómo prepararse» (está con el "
        "material de la sesión 6) y dígalo en voz alta en el cierre. Trae la lista de qué repasar "
        "por sesión; entregarlo el mismo día de la evaluación no sirve de nada. Las preguntas y la "
        "clave están en el Kit docente de la sesión 6: **esos dos no se comparten**.",
    ],

    "ti_siguiente": {
        "tid": "Revisión de casos de impacto ambiental — un caso documentado de impacto ambiental "
               "de infraestructura digital, con fuente, año y alcance declarados.",
        "ti": "Informe sobre sostenibilidad: una página con la huella de su sistema, las dos "
              "decisiones y el indicador, en la carpeta del equipo.",
        "adelanto": "**cierra el corte 1**: se arma la ficha del problema del proyecto del semestre "
                    "y hay evaluación de corte en ExamLab al final de la sesión.",
        "aviso": "La sesión 6 cierra el corte. Traigan **el problema de la sesión 1, la ficha de "
                 "sistema de la sesión 3, la regla ética de la sesión 4 y el indicador de hoy**: la "
                 "ficha del problema se arma con esas cuatro cosas y se entrega en clase. Y lean el "
                 "documento **«Evaluación del Corte 1 — cómo prepararse»**: trae qué repasar de "
                 "cada sesión para los 20 minutos de evaluación del final.",
    },

    "cierre_titulo": "Nos vemos en la sesión 6 — cierra el corte 1",
    "cierre_frase": "El software no es inmaterial: pesa, consume y termina en basura",
}


# =============================================================================
# CLASE 6 · Analisis de problemas tecnologicos del entorno · CIERRA EL CORTE 1
# =============================================================================
# Sesion con reparto de tiempo propio: la evaluacion de corte se aplica al final,
# despues de las exposiciones, porque cubre las sesiones 1 a 6 completas.

TEMAS[6] = {
    "n": 6,
    "titulo": "Análisis de problemas tecnológicos del entorno",
    "subtitulo": "El problema del proyecto del semestre queda escrito hoy",
    "hook": "«En el barrio falta una app.» ¿Eso es un problema? "
            "¿O es una solución a la que todavía no le encontramos el problema?",
    "hook_lines": [
        "Casi todos los proyectos que fracasan empezaron con una solución, no con un problema.",
        "Hoy sale la ficha del problema, y es la que va a gobernar el resto del semestre.",
    ],
    "objetivos": [
        "Distinguir un **problema** de un **síntoma** y de una **solución disfrazada de problema**.",
        "Construir el **árbol de causas** de un problema del entorno.",
        "Escribir una **línea base**: una cifra que se pueda decir hoy sobre el problema.",
        "Verificar que el problema elegido **cabe en un semestre** con los cuatro criterios.",
        "Entregar la **ficha del problema** del proyecto del equipo.",
    ],
    "agenda_slots": [
        ("Apertura", 10, "Pregunta de entrada en el muro"),
        ("Teoría y guía del docente", 25, "Problema vs. síntoma, árbol de causas, línea base y los cuatro criterios"),
        ("Actividad en equipos", 17, "Ficha del problema del proyecto, en salas de grupo"),
        ("Exposiciones", 15, "5 equipos × 3 min — el problema en una frase y su cifra"),
        ("Evaluación de corte 1", 20, "En ExamLab · cubre las sesiones 1 a 6"),
        ("Cierre", 3, "Qué queda amarrado para el corte 2"),
    ],
    "agenda_sub": "Hoy el reparto cambia: la teoría se comprime a 25 min para dejar 20 min de "
                  "evaluación de corte al final",
    "nota_bloque": "**Esta sesión cierra el corte 1 (30 %).** Trae dos cosas que las demás no "
                   "tienen: la **ficha del problema del proyecto**, que es el producto del corte y "
                   "gobierna el resto del semestre, y la **evaluación de corte en ExamLab**, que se "
                   "aplica en los últimos 20 minutos y cubre las sesiones 1 a 6. Por eso el bloque "
                   "de teoría baja de 45 a 25 minutos: hay que llegar con tiempo, no con la "
                   "explicación a medias.",
    "agenda": {},
    "herramienta_nota": "El árbol de causas se dibuja en **Excalidraw** —a mano alzada, que es lo "
                        "que sirve para pensar— y la ficha se escribe en el **documento del equipo "
                        "en Drive**. Hoy **no se usa IA**: el problema tiene que salir de lo que "
                        "ellos conocen del entorno, y un asistente lo devuelve genérico. La "
                        "evaluación de corte se responde en **ExamLab**, con el enlace en el chat.",
    "avance_proyecto": "Cerrar el problema del proyecto del semestre: enunciado en una frase, línea "
                       "base con cifra, árbol de causas, actores y criterio de éxito medible. Es el "
                       "entregable del corte 1",

    "teoria": [
        {
            "tipo": "before_after",
            "titulo": "Síntoma, problema y solución disfrazada",
            "before_title": "Lo que los equipos escriben",
            "before": [
                "«Falta una app para la biblioteca del barrio.»",
                "«La gente se queja del servicio.»",
                "«No hay tecnología en el negocio.»",
                "«Queremos hacer un sistema con IA.»",
                "«El proceso es muy manual.»",
            ],
            "after_title": "Lo que es cada cosa",
            "after": [
                "**Solución disfrazada.** La app es la respuesta; falta la pregunta.",
                "**Síntoma.** La queja es la señal, no el problema. ¿Se queja de qué?",
                "**Juicio, no problema.** ¿Qué no puede hacer alguien por eso?",
                "**Solución disfrazada, y con herramienta ya elegida.** Peor todavía.",
                "**Casi.** «Manual» describe el cómo; falta a quién le cuesta qué.",
            ],
            "sub": "Un problema bien escrito dice: a QUIÉN le pasa QUÉ, con qué CONSECUENCIA, y trae una CIFRA",
            "size": 13,
        },
        {
            "tipo": "steps",
            "titulo": "El árbol del problema",
            "steps": [
                ("CAUSAS DE FONDO (las raíces profundas)", "El por qué de cada causa. **Aquí aparece lo que sí se puede cambiar en un semestre**"),
                ("CAUSAS DIRECTAS (las raíces)", "Por qué ocurre el problema. Dos o tres, no diez"),
                ("PROBLEMA (el tronco)", "Una sola frase: a quién le pasa qué, con qué consecuencia. Es lo que se ataca"),
                ("EFECTOS (las ramas)", "Lo que se ve y lo que duele: quejas, demoras, pérdidas. Aquí viven los síntomas"),
            ],
            "sub": "Se dibuja de arriba hacia abajo y se lee de abajo hacia arriba, como está aquí. Regla: el proyecto ataca una CAUSA, no una rama — quien diseña para los efectos produce una solución cosmética",
        },
        {
            "tipo": "content",
            "titulo": "La línea base: la cifra de hoy",
            "items": [
                "@@Qué es.@@ Una cifra que describa el problema **como está hoy**, antes de que "
                "ustedes toquen nada. «La secretaria dedica unas 2 horas diarias a confirmar citas "
                "por teléfono.» «De 40 libros prestados al mes, unos 12 vuelven tarde.»",
                "@@Por qué es obligatoria.@@ Sin línea base **no se puede saber si el proyecto "
                "sirvió**. Un informe final que dice «mejoramos el proceso» no demuestra nada; uno "
                "que dice «pasó de 2 horas a 20 minutos» sí. En la sesión 16 se les va a pedir "
                "exactamente eso.",
                "@@Cómo se consigue sin presupuesto.@@ Preguntando, contando y midiendo con un "
                "cronómetro. Tres preguntas a la persona que hace el trabajo, un conteo de una "
                "semana, o el tiempo de un caso medido a mano. **No hace falta una encuesta "
                "científica**: hace falta un número honesto y decir cómo se obtuvo.",
                "@@La regla de honestidad.@@ Toda cifra va con **cómo se obtuvo y cuándo**. Si es "
                "una estimación, se escribe «estimado». Una cifra inventada es peor que ninguna, "
                "porque el resto del proyecto se apoya en ella.",
                "@@Si el problema no tiene cifra posible@@, es señal de que está mal delimitado: "
                "casi siempre es demasiado grande. Bájenlo hasta que se pueda contar algo.",
            ],
            "size": 13,
        },
        {
            "tipo": "cards",
            "titulo": "Cuándo un problema cabe en un semestre",
            "cards": [
                ("1 · Abordable con lo que tienen",
                 "Se puede avanzar con navegador, documentos y herramientas gratuitas. Si exige "
                 "comprar equipos, contratar servicios o permisos institucionales que no van a "
                 "llegar, **no cabe**."),
                ("2 · Medible",
                 "Existe al menos una cifra que se puede decir hoy y volver a medir en la sesión "
                 "16. Si nada se puede contar, no se va a poder demostrar nada."),
                ("3 · Con acceso a los actores",
                 "Pueden hablar con alguien que vive el problema, **esta semana y sin trámites**. Un "
                 "problema sobre una entidad a la que nadie del equipo puede preguntarle nada es un "
                 "ejercicio de imaginación."),
                ("4 · Con dueño del problema",
                 "Hay una persona o un grupo concreto al que le duele y que reconocería la mejora. "
                 "Si el afectado es «la sociedad», no hay a quién mostrarle el resultado."),
            ],
            "columns": 2,
        },
        {
            "tipo": "box",
            "titulo": "Cómo cierra el corte 1 hoy",
            "notas": [
                ("info",
                 "**La ficha del problema es el producto del corte.** Se entrega hoy, en el "
                 "documento del equipo, y a partir de la sesión 7 todo el trabajo se hace sobre "
                 "ella: el ciclo de vida, el prototipo, el impacto y el informe final. Cambiarla "
                 "después cuesta trabajo, así que vale la pena escribirla bien hoy."),
                ("info",
                 "**Los últimos 20 minutos son la evaluación de corte, en ExamLab.** Cubre las "
                 "sesiones 1 a 6: qué es la ingeniería y qué no, historia y hitos, elementos de un "
                 "sistema, principios éticos y normas, huella ambiental, y problema contra "
                 "síntoma. Es individual y se responde en la misma sesión."),
                ("aclaracion",
                 "**ExamLab no es una plataforma oficial de la universidad**: es la herramienta que "
                 "usa este curso para las evaluaciones, y el enlace se comparte en el chat. Si a "
                 "alguien no le abre, avise de inmediato en el chat y se resuelve en el momento — "
                 "no al día siguiente."),
            ],
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada: la solución disfrazada de problema",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "«En el barrio falta una app» es la frase que un profesor de primer semestre va a "
                "oír docenas de veces, y es el error más costoso del curso porque no se ve: parece "
                "un problema, tiene sujeto, tiene carencia, y sin embargo ya trae la solución "
                "adentro. Si el problema es «falta una app», entonces cualquier app resuelve el "
                "problema, y el proyecto se convierte en un ejercicio de construir algo sin saber "
                "para qué.",
                "La prueba que conviene enseñar es de una sola pregunta y sirve para toda la vida: "
                "**¿esto se podría resolver sin ninguna app?** Si la respuesta es sí —y casi "
                "siempre lo es—, entonces el problema es otro y hay que buscarlo. Si el problema "
                "verdadero es que la gente no sabe si el libro que necesita está disponible, eso se "
                "puede resolver con una app, con una lista pegada en la puerta o con un número de "
                "WhatsApp. Que existan varias soluciones posibles es la señal de que el problema "
                "está bien escrito.",
                "Recoja las respuestas del muro en los diez minutos de apertura y no las corrija: "
                "en el minuto 12, con la primera diapositiva, van a ver ellos mismos que casi todo "
                "lo que escribieron era un síntoma o una solución.",
            ],
        },
        {
            "titulo": "Las tres cosas que se confunden y cómo se escribe un problema",
            "slide": "{{slide:Síntoma, problema y solución disfrazada}}",
            "cuerpo": [
                "**El síntoma** es la señal visible: la queja, la demora, la pérdida. «La gente se "
                "queja del servicio» es un síntoma perfecto y un problema inservible, porque no "
                "dice de qué se queja ni qué no puede hacer. Los síntomas son útiles —son la pista "
                "que lleva al problema— pero atacar un síntoma produce soluciones cosméticas: si el "
                "síntoma es que la fila es larga, poner sillas mejora la fila y no toca el "
                "problema.",
                "**La solución disfrazada** es la más peligrosa porque se ve profesional. «Falta un "
                "sistema», «hay que digitalizar el proceso», «queremos hacerlo con IA». Las tres "
                "eligen la herramienta antes de saber qué se va a resolver, y cierran el análisis: "
                "una vez que el equipo decidió que va a hacer una app con IA, va a interpretar "
                "cualquier hallazgo como confirmación.",
                "**El juicio** es la tercera y la más común en primer semestre: «no hay tecnología "
                "en el negocio», «el proceso es muy anticuado». Son opiniones sobre un estado de "
                "cosas y no dicen a quién le cuesta qué. Un negocio sin tecnología puede estar "
                "funcionando perfectamente; la falta de tecnología no es un problema por sí misma, "
                "y esta es una idea que hay que decir en voz alta en un curso de ingeniería de "
                "sistemas, porque va contra el reflejo del gremio.",
                "**La fórmula del enunciado**, y conviene dictarla para que la copien: *a QUIÉN le "
                "pasa QUÉ, con qué CONSECUENCIA*, más una cifra. Ejemplo bien escrito: «los "
                "usuarios de la biblioteca del barrio no saben si un libro está disponible antes de "
                "ir, así que hacen viajes en vano; de cada diez visitas, unas cuatro terminan sin "
                "préstamo». Tiene sujeto (los usuarios), tiene el qué (no saben la disponibilidad), "
                "tiene la consecuencia (viajes en vano) y tiene una cifra. Y no menciona ninguna "
                "tecnología, que es lo que deja el espacio para diseñar.",
            ],
        },
        {
            "titulo": "El árbol del problema: la herramienta que evita las soluciones cosméticas",
            "slide": "{{slide:El árbol del problema}}",
            "cuerpo": [
                "El árbol de problemas es una técnica vieja y muy usada en formulación de "
                "proyectos, y para primer semestre tiene una virtud enorme: es un dibujo, así que "
                "se puede hacer en quince minutos y se puede discutir señalando con el dedo.",
                "Se dibuja con el **problema en el tronco**, una sola frase. Hacia arriba, las "
                "**ramas son los efectos**: lo que se ve, lo que la gente reporta, lo que duele. "
                "Hacia abajo, las **raíces son las causas**, y hay dos niveles: las causas directas "
                "(por qué ocurre el problema) y las causas de fondo (por qué ocurre cada causa). "
                "Se dibuja de arriba hacia abajo y **se lee de abajo hacia arriba**, porque así se "
                "ve la cadena completa: esta causa de fondo produce esta causa, que produce el "
                "problema, que produce estos efectos.",
                "La regla que hay que repetir hasta el cansancio: **el proyecto ataca una causa, no "
                "una rama**. Si el equipo diseña para los efectos, produce algo que alivia la "
                "molestia y deja el problema intacto. Y la segunda regla, práctica: dos o tres "
                "causas directas, no diez. Un árbol con diez raíces no es un análisis, es una lista "
                "de todo lo que se les ocurrió, y con eso no se puede decidir.",
                "El momento de aprendizaje real ocurre en el segundo nivel de raíces, y conviene "
                "provocarlo en las salas: cuando el equipo baja de «no hay un registro "
                "actualizado» a «el registro se actualiza a mano al final del día y nadie tiene "
                "tiempo», ahí aparece por primera vez algo que un estudiante de primer semestre "
                "puede efectivamente cambiar en un semestre. Antes de ese nivel, todo se ve "
                "demasiado grande.",
                "Un detalle metodológico que ahorra discusiones: si una causa no se puede afectar "
                "con nada que el equipo pueda hacer —el presupuesto del municipio, la cultura "
                "ciudadana, la ley—, se dibuja igual, pero se marca. Se llama restricción y no es "
                "una derrota: es información. Un proyecto que sabe qué no puede cambiar es más "
                "serio que uno que promete cambiarlo todo.",
            ],
        },
        {
            "titulo": "La línea base y los cuatro criterios de viabilidad",
            "slide": "{{slide:La línea base}} {{slide:cabe en un semestre}}",
            "cuerpo": [
                "**La línea base** es la exigencia que más resistencia genera y la que más valor "
                "tiene. Es una cifra sobre el problema **como está hoy**, antes de que el equipo "
                "toque nada, y su función es simple: sin ella no hay forma de saber si el proyecto "
                "sirvió. En la sesión 16 el informe final va a pedir comparar, y un equipo sin "
                "línea base solo puede escribir «mejoramos el proceso», que es una afirmación "
                "vacía.",
                "Hay que quitarles de encima la idea de que medir requiere presupuesto o "
                "estadística. La línea base de un proyecto de este curso se consigue de tres "
                "maneras: **preguntando** a la persona que hace el trabajo, **contando** durante "
                "una semana, o **midiendo con un cronómetro** un caso. «La secretaria dedica unas "
                "dos horas diarias a confirmar citas por teléfono, según lo que ella misma estima» "
                "es una línea base perfectamente aceptable, siempre que se diga que es una "
                "estimación y de quién viene. La regla de honestidad es la de la sesión 5, aplicada "
                "de nuevo: **cifra con método y fecha, o no va**.",
                "Y hay un diagnóstico gratis escondido en esta exigencia: **si el problema no "
                "admite ninguna cifra, está mal delimitado**, y casi siempre es porque es demasiado "
                "grande. «La deserción estudiantil» no se puede medir con lo que tiene un equipo de "
                "primer semestre; «cuántos de los 30 compañeros de mi grupo no saben en qué "
                "semestre pierden el beneficio de la beca» sí. Bajar el problema hasta que se pueda "
                "contar algo es la manera más rápida de volverlo abordable.",
                "**Los cuatro criterios** son un filtro y hay que aplicarlos en voz alta a cada "
                "problema propuesto, uno por uno. *Abordable* con navegador y herramientas "
                "gratuitas: nada que exija comprar equipos, contratar servicios de pago o "
                "conseguir permisos institucionales que no van a llegar en un semestre. *Medible*: "
                "existe la cifra. *Con acceso a los actores*: pueden hablar esta semana con alguien "
                "que vive el problema, sin trámites; este criterio es el que descarta más "
                "propuestas y hay que ser firme, porque un proyecto sobre una entidad a la que "
                "nadie puede preguntarle nada termina siendo un ejercicio de imaginación con "
                "aspecto de proyecto. *Con dueño del problema*: hay una persona o un grupo concreto "
                "al que le duele y que reconocería la mejora; si el afectado es «la sociedad», no "
                "hay a quién mostrarle el resultado en la sesión 15.",
                "Una advertencia sobre el ánimo del grupo: aplicar estos criterios va a matar "
                "algunas ideas ambiciosas y eso frustra. Vale la pena decirles por qué se hace: **es "
                "mejor resolver algo pequeño de verdad que simular algo grande**, y en un primer "
                "semestre el objetivo es que aprendan a formular y a demostrar, no que salven la "
                "ciudad. Un proyecto pequeño y verificable saca mejor nota que uno grandioso e "
                "imposible, y hay que decirlo hoy, antes de que se enamoren de la idea.",
            ],
        },
        {
            "titulo": "Cómo cerrar el corte: la ficha y la evaluación en ExamLab",
            "slide": "{{slide:Cómo cierra el corte 1}}",
            "cuerpo": [
                "El reparto del tiempo de hoy es distinto al de las otras sesiones y hay que "
                "respetarlo: **teoría 25 minutos**, no 45. El corte se cierra con dos entregas y "
                "las dos ocurren en clase, así que quedarse largo en la explicación significa "
                "aplicar la evaluación con la gente apurada, que es la peor manera de evaluar.",
                "**La ficha del problema** es el producto del corte 1 y conviene decirle al grupo "
                "exactamente qué peso tiene en el semestre: a partir de la sesión 7 todo se hace "
                "sobre ella. El ciclo de vida de la sesión 7 se aplica a ese problema; el "
                "prototipo de las sesiones 10 y 11 resuelve ese problema; la evaluación de impacto "
                "de la sesión 13 evalúa esa solución; el informe final de la sesión 16 compara "
                "contra esa línea base. Un equipo que hoy escriba una ficha vaga va a arrastrar el "
                "problema diez sesiones.",
                "**La evaluación de corte** son los últimos veinte minutos, en ExamLab, individual, "
                "y cubre las sesiones 1 a 6. Tres cosas operativas: el enlace va en el chat de la "
                "reunión, hay que decir explícitamente que **ExamLab no es una plataforma oficial "
                "de la universidad** sino la herramienta que usa este curso, y hay que pedir que "
                "cualquier problema para abrirlo se avise **en el chat, en el momento**, no al día "
                "siguiente por correo. En un curso virtual el problema técnico no reportado se "
                "vuelve un reclamo de nota dos semanas después.",
                "Una última recomendación de manejo del grupo: no anuncie la evaluación al final "
                "de las exposiciones, anúnciela en el minuto uno, cuando presente la agenda. La "
                "gente organiza su atención distinto cuando sabe que hay una evaluación al cierre, "
                "y además evita que alguien se desconecte después de exponer.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:10 · Apertura · [Slide 4]",
            "cuerpo": [
                "Comparta pantalla antes de que entre el primero:",
                "> «En el barrio falta una app. ¿Eso es un problema, o es una solución a la que "
                "todavía no le encontramos el problema?»",
                "**[Nota docente]:** en el minuto 2, con la agenda [Slide 2] en pantalla, **anuncie "
                "que hoy cierra el corte y que los últimos 20 min son la evaluación en ExamLab**. "
                "No lo deje para el final: cambia cómo prestan atención y evita que alguien se "
                "desconecte después de exponer.",
                "**[Nota docente]:** pida que tengan abierto el documento del equipo con las cuatro "
                "cosas de las sesiones anteriores (problema inicial, ficha de sistema, regla ética, "
                "indicador ambiental). La ficha se arma con eso.",
            ],
        },
        {
            "titulo": "00:10–00:35 · Teoría (25 min, comprimida) · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]",
            "cuerpo": [
                "Reparto estricto. Hoy el reloj manda:",
                "- **6 min** · Síntoma, problema y solución disfrazada [Slide 5]. **Vuelva al muro** "
                "y clasifique en voz alta dos o tres respuestas de la apertura. Dicte la fórmula: "
                "a quién le pasa qué, con qué consecuencia, más una cifra.",
                "- **7 min** · El árbol del problema [Slide 6]. Dibújelo en vivo con un ejemplo, no "
                "lo explique en abstracto. Repita la regla: **el proyecto ataca una causa, no una "
                "rama**.",
                "- **5 min** · La línea base [Slide 7]. Lo esencial: se consigue preguntando, "
                "contando o cronometrando; y si no hay cifra posible, el problema está muy grande.",
                "- **5 min** · Los cuatro criterios [Slide 8]. Aplíquelos en voz alta a una idea que "
                "haya salido en el muro, incluida la parte incómoda de descartar.",
                "- **2 min** · Cómo cierra el corte [Slide 9]. Ficha + evaluación, y que ExamLab no "
                "es plataforma oficial de la universidad.",
                "**[Nota docente]:** si va retrasado, recorte los criterios a tres minutos "
                "quedándose con *medible* y *acceso a los actores*, que son los dos que más "
                "descartan. **No recorte el árbol**: es la herramienta del taller.",
            ],
        },
        {
            "titulo": "00:35–00:52 · Taller en salas de grupo · [Slide 10]",
            "cuerpo": [
                "**2 min** para repartir: cada equipo trabaja **su propio problema**, el que viene "
                "desde la sesión 1. Excalidraw para el árbol, documento del equipo para la ficha.",
                "**15 min** en salas. Entre a las cinco, ~3 min cada una, con **una sola pregunta "
                "por sala: ¿cuál es la cifra?** Es lo que falta en el 80 % de las fichas.",
                "**[Nota docente]:** si un equipo tiene un problema que no pasa el criterio de "
                "acceso a los actores, **redúzcalo con ellos ahí mismo**, no lo deje para después. "
                "La técnica que funciona: pregunte «¿a quién de este problema le pueden preguntar "
                "algo esta semana?» y reescriba el problema alrededor de esa persona.",
                "**[Nota docente]:** el árbol de diez raíces es el otro error frecuente. Pida que "
                "escojan las dos causas que sí pueden tocar y marquen el resto como restricciones.",
            ],
        },
        {
            "titulo": "00:52–01:07 · Exposiciones · [Slide 11]",
            "cuerpo": [
                "5 equipos × 3 min. **El minuto obligatorio de hoy es el problema en una frase más "
                "la cifra.** Si no hay cifra, dígalo en el momento y déjelo anotado: se corrige "
                "esta semana y entra en la sesión 7.",
                "**[Nota docente]:** los cinco enlaces de Excalidraw en el chat antes de arrancar.",
                "**[Nota docente]:** anote las cinco fichas. Son el insumo directo de la sesión 7 y "
                "la referencia para el informe final.",
                "**[Nota docente]:** sea puntual con el corte a los 15 min. Lo que sigue es "
                "evaluación y no hay margen.",
            ],
        },
        {
            "titulo": "01:07–01:27 · Evaluación de corte 1 en ExamLab (20 min)",
            "cuerpo": [
                "**[Nota docente]:** pegue el enlace en el chat y verifique **por respuesta de "
                "cada uno en el chat** que abrió. No asuma: en virtual el que no abrió se queda "
                "callado.",
                "**[Nota docente]:** repita que ExamLab **no es una plataforma oficial de la "
                "universidad**, que es la herramienta de evaluación de este curso, y que cualquier "
                "problema se avisa **en el chat en el momento**.",
                "Es individual, cubre las sesiones 1 a 6 y se responde en la sesión. Mantenga la "
                "reunión abierta con el micrófono libre para dudas de enunciado —no de contenido—.",
                "**[Nota docente]:** si alguien pierde la conexión durante la evaluación, anótelo y "
                "resuélvalo con reposición el mismo día. No lo deje para la próxima sesión.",
            ],
        },
        {
            "titulo": "01:27–01:30 · Cierre · [Slide 12][Slide 13]",
            "cuerpo": [
                "Una idea: **el problema ya está escrito y de aquí en adelante todo se hace sobre "
                "esa ficha.** El corte 1 cierra con un producto, no con una nota.",
                "Anuncie la sesión 7: arranca el corte 2 con el **ciclo de vida de los proyectos de "
                "ingeniería**, y se aplica al problema de hoy.",
            ],
        },
    ],

    "taller": {
        "archivo": "Ficha del problema del proyecto",
        "titulo": "Ficha del problema del proyecto",
        "min": 17,
        "exposicion": 3,
        "consigna": "Cierren el problema del proyecto del semestre. Cinco bloques: el problema en "
                    "**una frase**, la **línea base** con una cifra, el **árbol de causas** en "
                    "Excalidraw, los **actores y la frontera**, y un **criterio de éxito medible**. "
                    "Esta ficha es el entregable del corte 1 y gobierna el resto del semestre.",
        "entregable": "la ficha de cinco bloques en el documento del equipo, más el árbol de causas "
                      "en Excalidraw exportado a PNG en la carpeta del equipo",
        "entregable_corto": "ficha del problema + árbol de causas",
        "reparto_titulo": "No se sortea nada:",
        "reparto": "cada equipo trabaja **su propio problema**, el que traen desde la sesión 1. "
                   "Usen lo que ya tienen: la ficha de sistema de la sesión 3, la regla ética de la "
                   "sesión 4 y el indicador ambiental de la sesión 5 entran en esta ficha.",
        "reparto_corto": "cada equipo, su propio problema",
        "bloques": [
            {"clave": "EL PROBLEMA EN UNA FRASE",
             "pide": "Una sola frase con la fórmula: **a quién le pasa qué, con qué consecuencia**. "
                     "Sin mencionar ninguna tecnología ni ninguna solución.",
             "check": "no aparece ninguna herramienta ni la palabra «app» o «sistema», y se entiende a quién le pasa y qué le cuesta."},
            {"clave": "LA LÍNEA BASE",
             "pide": "Una cifra que describa el problema **hoy**, antes de que ustedes toquen nada, "
                     "más **cómo la obtuvieron** y cuándo. Si es estimación, escriban «estimado».",
             "check": "hay número, unidad y método. Una cifra sin método no cuenta."},
            {"clave": "EL ÁRBOL DE CAUSAS",
             "pide": "En Excalidraw: el problema en el tronco, los efectos arriba, dos o tres "
                     "causas directas abajo y el segundo nivel de cada una. Marquen con un símbolo "
                     "las causas que **no** pueden cambiar (restricciones).",
             "check": "hay dos niveles de causas y al menos una restricción marcada. Un árbol de diez raíces sin jerarquía no cuenta."},
            {"clave": "ACTORES Y FRONTERA",
             "pide": "Quién vive el problema (el dueño del problema), quién más se afecta sin ser "
                     "usuario, y qué queda **fuera** de lo que ustedes van a abordar. Digan además "
                     "**a quién le pueden preguntar algo esta semana**.",
             "check": "hay un actor con el que se puede hablar esta semana, y hay algo declarado explícitamente fuera del alcance."},
            {"clave": "EL CRITERIO DE ÉXITO",
             "pide": "Una frase de la forma: «el proyecto sirvió si <la cifra de la línea base> "
                     "pasa de X a Y, medido así». Y la causa del árbol que van a atacar.",
             "check": "el criterio se puede verificar en la sesión 16 con la misma medición de la línea base, y ataca una causa, no un efecto."},
        ],
        "expo": [
            ("40 s · El problema en una frase", "Léanla tal cual está escrita. Sin tecnología dentro."),
            ("30 s · La cifra", "La línea base y cómo la obtuvieron. Es el minuto obligatorio."),
            ("50 s · El árbol", "Muestren el dibujo y señalen la causa que van a atacar."),
            ("40 s · Actores y frontera", "Quién vive el problema, y a quién le van a preguntar esta semana."),
            ("20 s · El criterio de éxito", "De X a Y, medido así."),
        ],
    },

    "rubrica": [
        ("El problema está en una frase, con la fórmula, y sin ninguna tecnología dentro", 25,
         "Es la habilidad central del corte: un problema con la solución adentro cierra el diseño antes de empezar."),
        ("La línea base tiene número, unidad y método declarado", 25,
         "Sin línea base el informe final de la sesión 16 no puede demostrar nada."),
        ("El árbol tiene dos niveles de causas y al menos una restricción marcada", 20,
         "Distinguir la causa que se puede tocar de la que no es lo que vuelve el proyecto realizable."),
        ("Hay un actor concreto al que se le puede preguntar esta semana y una frontera declarada", 15,
         "El acceso a los actores es el criterio que más proyectos imposibles descarta."),
        ("El criterio de éxito es verificable con la misma medición de la línea base", 15,
         "Cierra el ciclo: el proyecto queda con una manera de saber si sirvió."),
    ],

    "solucion": {
        "para_que": "Este documento trae la ficha completa del caso de la biblioteca —el mismo que "
                    "se usó en las sesiones 1 y 3, para que se vea el problema madurar— y al final "
                    "las claves de los cuatro tipos de proyecto frecuentes. Es la solución más "
                    "importante del corte, porque lo que se escriba hoy gobierna diez sesiones "
                    "más. Si el docente solo alcanza a leer dos bloques antes de clase, que sean "
                    "**LA LÍNEA BASE** y **EL CRITERIO DE ÉXITO**: son los dos que casi ningún "
                    "equipo hace bien solo.",
        "caso_titulo": "La biblioteca del barrio · ficha del problema completa",
        "caso": "La biblioteca comunitaria de un barrio presta libros con un cuaderno. Atiende de "
                "lunes a sábado con dos personas voluntarias que rotan. Los usuarios son sobre todo "
                "estudiantes de colegio y de universidad del sector. La coordinadora dice que «se "
                "pierden libros» y que «la gente se queja». Es el mismo caso de las sesiones 1 y 3: "
                "hoy se le exige lo que en la sesión 1 todavía no se sabía pedir.",
        "por_que_este_caso": "Se mantiene el caso de las sesiones 1 y 3 a propósito. En la sesión 1 "
                             "el problema se enunció como «falta un sistema para la biblioteca»; en "
                             "la 3 apareció que el sistema es el proceso de préstamo y no el "
                             "software; hoy queda escrito como un problema medible. Mostrar esa "
                             "progresión en tres versiones de la misma frase es la lección de la "
                             "sesión.",
        "bloques": [
            {
                "clave": "EL PROBLEMA EN UNA FRASE",
                "respuesta": "**Versión final (la que se acepta):**\n\n"
                             "> «Los usuarios de la biblioteca no pueden saber si un libro está "
                             "disponible antes de ir, así que hacen viajes que terminan sin "
                             "préstamo; de cada 10 visitas, unas 4 salen sin el libro que "
                             "buscaban.»\n\n"
                             "**Por qué esta funciona:** dice a quién le pasa (los usuarios), qué "
                             "le pasa (no pueden saber la disponibilidad antes de ir), con qué "
                             "consecuencia (viajes en vano), y trae una cifra. **No menciona "
                             "ninguna tecnología**, y eso es lo que deja abierto el diseño: se "
                             "podría resolver con una lista publicada, con un número de WhatsApp o "
                             "con una aplicación. Que haya varias soluciones posibles es la prueba "
                             "de que el problema está bien escrito.\n\n"
                             "**La progresión, que vale mostrarla en pantalla:**\n\n"
                             "1. Sesión 1: «Falta un sistema para la biblioteca del barrio.» "
                             "→ solución disfrazada.\n"
                             "2. Sesión 3: «El proceso de préstamo no tiene registro confiable de "
                             "qué está prestado.» → mejor, pero sigue siendo una causa, no el "
                             "problema del usuario.\n"
                             "3. Sesión 6: la versión final de arriba. → problema del actor, con "
                             "consecuencia y cifra.\n\n"
                             "**Enunciados que se rechazan y por qué:** «se pierden libros» "
                             "(síntoma, y además es el problema de la coordinadora, no del usuario "
                             "— puede ser un segundo problema, no este); «la biblioteca no está "
                             "digitalizada» (juicio con solución adentro); «los usuarios necesitan "
                             "una app de consulta» (solución disfrazada).",
                "como_calificar": "25 pts. Dos verificaciones mecánicas y rápidas: (a) **busque la "
                                  "palabra «app», «sistema», «plataforma» o «digital» en la frase**; "
                                  "si aparece, máximo 10; (b) pregúntese si se entiende **a quién le "
                                  "cuesta qué**; si el sujeto es «la biblioteca» o «el barrio», "
                                  "máximo 12, porque falta la persona. Los 25 son para la fórmula "
                                  "completa con consecuencia. No exija elegancia: exija estructura."
            },
            {
                "clave": "LA LÍNEA BASE",
                "respuesta": "**Cifra:** «De cada 10 visitas, unas 4 terminan sin el libro "
                             "buscado.»\n\n"
                             "**Método:** *un conteo hecho por el equipo durante seis días de "
                             "atención, preguntando a la salida a cada persona que salió sin libro "
                             "si el que buscaba estaba disponible. Se contaron 63 visitas, 26 "
                             "salieron sin préstamo por indisponibilidad. Datos tomados en la "
                             "semana del …*\n\n"
                             "**Segunda cifra útil, más fácil de conseguir:** «La coordinadora "
                             "estima que responde entre 15 y 20 llamadas semanales preguntando por "
                             "disponibilidad» — marcada explícitamente como **estimación de la "
                             "coordinadora**, no como medición.\n\n"
                             "Las dos son aceptables y la diferencia hay que enseñarla: la primera "
                             "es una **medición** con método declarado; la segunda es una "
                             "**estimación de un informante**, igual de legítima si se dice qué es "
                             "y de quién viene. Lo que no es aceptable es una cifra sin origen.\n\n"
                             "**Cómo se consigue esto sin presupuesto, que es la pregunta real de "
                             "los equipos:** tres preguntas a la persona que hace el trabajo, un "
                             "conteo de una semana con una hoja, o el tiempo de un caso medido con "
                             "el cronómetro del celular. Nada de esto necesita permiso "
                             "institucional ni encuesta científica.",
                "como_calificar": "25 pts, y es el bloque donde se cae la mayoría. Tres requisitos: "
                                  "**número, unidad y método**. Sin método, máximo 10, sin importar "
                                  "lo verosímil que suene la cifra — y dígalo con el argumento, "
                                  "porque es la lección: una cifra sin origen no se puede volver a "
                                  "medir en la sesión 16, así que no sirve. Una estimación bien "
                                  "declarada («estimado por la coordinadora») vale los 25 "
                                  "completos: se califica la honestidad del método, no la precisión."
            },
            {
                "clave": "EL ÁRBOL DE CAUSAS",
                "respuesta": "**TRONCO:** los usuarios no pueden saber si un libro está disponible "
                             "antes de ir.\n\n"
                             "**EFECTOS (arriba):** viajes en vano · los usuarios dejan de ir y "
                             "usan otras fuentes · la coordinadora pierde tiempo respondiendo "
                             "llamadas · la percepción de que «la biblioteca no sirve».\n\n"
                             "**CAUSAS DIRECTAS (abajo):**\n\n"
                             "1. **No existe un registro consultable de qué está prestado.**\n"
                             "2. **No hay ningún canal para preguntar antes de ir**, salvo llamar "
                             "cuando hay quien contesta.\n\n"
                             "**SEGUNDO NIVEL:**\n\n"
                             "- De la causa 1: el préstamo se anota en un cuaderno que está en el "
                             "mostrador y solo se puede consultar ahí · rotan dos voluntarias y "
                             "cada una anota distinto · las devoluciones se anotan al final del "
                             "día, cuando hay tiempo.\n"
                             "- De la causa 2: el teléfono de la biblioteca es el celular personal "
                             "de la coordinadora y no siempre está atendido · no hay horario "
                             "declarado de atención telefónica.\n\n"
                             "**RESTRICCIONES marcadas (lo que el equipo NO puede cambiar):** el "
                             "presupuesto de la biblioteca es cero · las voluntarias rotan y no se "
                             "les puede exigir capacitación larga · no hay computador disponible en "
                             "el mostrador durante la atención · no se puede pedir que alguien "
                             "atienda un teléfono en horario fijo.\n\n"
                             "**La causa que se ataca:** la 1, y dentro de ella el segundo nivel "
                             "«el registro solo se puede consultar en el mostrador». Es la que "
                             "tiene mayor efecto y la única que no depende de conseguir tiempo de "
                             "una persona. Y nótese que las restricciones **no bloquean el "
                             "proyecto: lo delimitan** —obligan a que la solución funcione sin "
                             "computador en el mostrador y sin capacitación larga, lo cual es "
                             "información de diseño valiosísima que aparece en la sesión 7.",
                "como_calificar": "20 pts. Requisitos: **dos niveles de causas** (10 pts) y **al "
                                  "menos una restricción marcada** (10 pts). El error a corregir en "
                                  "vivo es el árbol con ocho o diez raíces sin jerarquía: eso es una "
                                  "lista, no un análisis, y vale 8. El segundo error es poner "
                                  "efectos entre las causas —«la gente se queja» abajo—; señálelo "
                                  "señalando el dibujo, es la manera más rápida de que se entienda. "
                                  "Si el equipo marca restricciones **y** explica cómo delimitan la "
                                  "solución, está haciendo ingeniería de verdad."
            },
            {
                "clave": "ACTORES Y FRONTERA",
                "respuesta": "**Dueño del problema:** los usuarios que van a buscar un libro "
                             "concreto, sobre todo los estudiantes de colegio con tarea para el día "
                             "siguiente. Son quienes reconocerían la mejora de inmediato.\n\n"
                             "**Actor con quien se puede hablar esta semana:** la coordinadora de "
                             "la biblioteca, y dos o tres usuarios en la puerta un sábado. Sin "
                             "trámites, sin permisos. **Este es el criterio que decide si el "
                             "proyecto es real.**\n\n"
                             "**Afectado que no es usuario** (viene de la sesión 3): las "
                             "voluntarias, que van a tener que usar lo que el equipo construya y "
                             "que no pidieron nada. Si la solución les agrega trabajo, no se va a "
                             "usar, y el proyecto fracasa aunque funcione. Es el mismo punto de la "
                             "sesión 4: hay un afectado que no está en la reunión.\n\n"
                             "**Frontera — lo que queda FUERA, declarado explícitamente:**\n\n"
                             "- La pérdida de libros y el cobro de multas: es otro problema, con "
                             "otro dueño (la coordinadora). No se aborda.\n"
                             "- La catalogación completa del acervo: no cabe en un semestre.\n"
                             "- La compra de libros o de equipos: presupuesto cero, es restricción.\n"
                             "- La reserva de libros en línea: se deja fuera de esta primera "
                             "versión porque exige que alguien atienda las reservas, y eso choca "
                             "con la restricción de personal.\n\n"
                             "Declarar lo que queda fuera es lo que evita que el proyecto crezca "
                             "sin control en la sesión 10, cuando aparezcan las ganas de agregarle "
                             "funciones.",
                "como_calificar": "15 pts. Lo que se califica de verdad es **el actor con quien se "
                                  "puede hablar esta semana** (8 pts): si el equipo no puede "
                                  "nombrarlo, el proyecto no es viable y hay que rediseñarlo hoy, "
                                  "no en la sesión 10. Los otros 7 son por la frontera declarada; "
                                  "un equipo que no deja nada fuera no ha delimitado. Si aparece el "
                                  "afectado no-usuario —las voluntarias— súbale: significa que la "
                                  "sesión 3 quedó aprendida."
            },
            {
                "clave": "EL CRITERIO DE ÉXITO",
                "respuesta": "**Criterio:** «El proyecto sirvió si las visitas que terminan sin el "
                             "libro buscado bajan de 4 de cada 10 a menos de 2 de cada 10, medido "
                             "con el mismo conteo de seis días a la salida de la biblioteca.»\n\n"
                             "**Causa atacada:** la 1 — que el registro solo se puede consultar en "
                             "el mostrador.\n\n"
                             "**Por qué este criterio funciona:** usa **la misma medición** de la "
                             "línea base, así que es comparable; tiene un valor de partida y uno de "
                             "llegada; y se puede ejecutar en la sesión 16 con lo que el equipo "
                             "tiene. Nótese que no promete cero: prometer la eliminación total del "
                             "problema es una señal de que el equipo no lo entendió.\n\n"
                             "**Criterio secundario, más barato de verificar:** «la coordinadora "
                             "puede decir qué está prestado sin abrir el cuaderno, en menos de 30 "
                             "segundos». Es un sí/no cronometrable y sirve como verificación "
                             "intermedia en la sesión 12.\n\n"
                             "**Criterios que se rechazan:** «que la biblioteca funcione mejor» (no "
                             "medible); «que el 100 % de los usuarios encuentren su libro» "
                             "(imposible: algunos libros simplemente están prestados); «que la app "
                             "tenga 200 usuarios» (mide adopción de la solución, no la resolución "
                             "del problema — es la trampa más frecuente y hay que nombrarla).",
                "como_calificar": "15 pts. El requisito duro es que **use la misma medición de la "
                                  "línea base**: si mide otra cosa, máximo 6, porque no habrá "
                                  "comparación posible en la sesión 16. Rechace los criterios que "
                                  "miden la solución en vez del problema («cantidad de descargas», "
                                  "«usuarios registrados») y explique el porqué en voz alta: es un "
                                  "error que arrastran hasta el informe final. Prometer el 100 % "
                                  "resta: indica que no entendieron el problema."
            },
        ],
        "variantes": [
            {"caso": "Proyecto en un negocio pequeño (tienda, taller, restaurante)",
             "clave": "Es el caso más frecuente y el más fácil de aterrizar, porque el dueño del "
                      "problema está ahí y se le puede preguntar. La trampa típica es enunciar «el "
                      "negocio no tiene sistema»: hay que llevarlos al actor y a la consecuencia "
                      "(«el dueño no sabe qué producto se está agotando hasta que un cliente lo "
                      "pide y no está»). Línea base fácil y honesta: contar cuántas veces en una "
                      "semana un cliente pidió algo que no había. Restricción casi segura: el dueño "
                      "no va a dedicar media hora diaria a registrar datos. Frontera: la "
                      "contabilidad y la facturación electrónica quedan fuera."},
            {"caso": "Proyecto en la propia universidad",
             "clave": "Buen acceso a los actores —los compañeros— y por eso funciona bien, pero "
                      "**hay dos reglas firmes**: no se usan nombres de funcionarios (se usa el "
                      "rol) y no se recogen datos personales de compañeros, por la Ley 1581 de "
                      "2012 vista en la sesión 4. Línea base típica: preguntar a los 30 compañeros "
                      "del grupo algo concreto y contar. La trampa es elegir un problema cuya "
                      "solución depende de una decisión administrativa: eso no lo puede cambiar el "
                      "equipo, y va marcado como restricción. Redirija hacia el problema de "
                      "**información** del estudiante, que sí es abordable."},
            {"caso": "Proyecto comunitario o de barrio (junta, colegio, huerta, ruta)",
             "clave": "Alto valor y el riesgo más alto: casi siempre el problema viene demasiado "
                      "grande («la inseguridad», «la movilidad»). La técnica de reducción que "
                      "funciona en la sala: pregunte «¿a quién de esto le pueden preguntar algo "
                      "esta semana?» y reescriba el problema alrededor de esa persona. La cifra "
                      "suele salir de un conteo hecho por ellos mismos, y hay que aceptar muestras "
                      "pequeñas siempre que digan el tamaño. Vigile que no aparezcan fotos ni "
                      "nombres de terceros: la regla del curso aplica igual fuera del campus."},
            {"caso": "Proyecto donde el equipo ya decidió la tecnología",
             "clave": "El equipo llega diciendo «vamos a hacer una app con IA para X». No lo pelee "
                      "de frente: pídale que llene la ficha **sin mencionar la tecnología**, y "
                      "haga la pregunta clave — «¿esto se podría resolver sin ninguna app?». Si la "
                      "respuesta es sí, el problema aparece solo. La tecnología puede seguir siendo "
                      "la elegida en la sesión 10; lo que no puede es estar dentro del enunciado "
                      "del problema, porque cierra el diseño antes de empezar. Si al final de los "
                      "17 minutos el equipo no logró sacar la tecnología de la frase, ese es el "
                      "punto que se le anota como corrección para la sesión 7."},
        ],
        "cierre": "Tres minutos y una idea, con estas palabras: **el problema ya está escrito, y de "
                  "aquí en adelante todo se hace sobre esa ficha.** El corte 1 no cierra con una "
                  "nota: cierra con un producto que gobierna diez sesiones. Muestre la progresión "
                  "de la frase de la biblioteca en sus tres versiones —sesión 1, sesión 3, sesión "
                  "6— porque es la prueba visible de que aprendieron algo en cinco semanas. "
                  "Recuerde las dos exigencias que se van a cobrar en la sesión 16: la **línea base "
                  "con método** y el **criterio de éxito con la misma medición**. Y anuncie la "
                  "sesión 7 sin misterio: arranca el corte 2 con el ciclo de vida de los proyectos "
                  "de ingeniería, aplicado a este problema, no en abstracto.",
        "conexion": "Este documento cierra el corte 1 y es el que más hacia adelante mira. Hacia "
                    "atrás recoge las cuatro sesiones: el problema inicial de la **sesión 1**, la "
                    "frontera y los actores de la **sesión 3**, el afectado y la regla ética de la "
                    "**sesión 4**, el indicador ambiental de la **sesión 5**. Hacia adelante: la "
                    "**sesión 7** aplica el ciclo de vida a esta ficha; la **sesión 8** ajusta la "
                    "propuesta de solución sobre la causa elegida; las **sesiones 10 y 11** "
                    "prototipan respetando las restricciones marcadas hoy; la **sesión 13** evalúa "
                    "el impacto de esa solución; y el **informe final de la sesión 16** compara "
                    "contra la línea base de hoy. Una ficha vaga hoy es un semestre difícil.",
    },

    "errores": [
        {"dice": "«Falta una app / un sistema para X»",
         "por_que": "Es una solución disfrazada de problema: cierra el diseño antes de empezar y hace que cualquier app «resuelva» el problema.",
         "pida": "Que respondan «¿esto se podría resolver sin ninguna app?». Si es sí, el problema es otro y hay que escribirlo."},
        {"dice": "«La gente se queja» / «se pierden libros»",
         "por_que": "Es un síntoma: la señal visible. Atacar el síntoma produce soluciones cosméticas.",
         "pida": "A quién le pasa qué, con qué consecuencia. Y la cifra."},
        {"dice": "Una cifra sin decir de dónde salió",
         "por_que": "No se puede volver a medir en la sesión 16, así que no sirve como línea base.",
         "pida": "Número, unidad y método: preguntando a quién, contando qué, o cronometrando cuándo."},
        {"dice": "Un árbol con diez raíces",
         "por_que": "Es una lista de todo lo que se les ocurrió, no un análisis, y con eso no se puede decidir qué atacar.",
         "pida": "Dos o tres causas directas, su segundo nivel, y las que no pueden cambiar marcadas como restricciones."},
        {"dice": "«El éxito es tener 200 usuarios en la app»",
         "por_que": "Mide la adopción de la solución, no la resolución del problema. Se puede tener 200 usuarios y el problema intacto.",
         "pida": "El criterio con la misma medición de la línea base: de X a Y, medido así."},
    ],

    "dudas": [
        {"p": "Nuestro problema es muy grande y nos dijeron que lo bajemos. ¿No es peor un proyecto pequeño?",
         "r": "No: saca mejor nota. En este curso se evalúa que sepan formular, medir y demostrar, no "
              "el tamaño de la ambición. Un problema pequeño resuelto y medido de verdad es un "
              "proyecto completo; uno grande simulado es una presentación bonita sin evidencia. Y "
              "el informe final de la sesión 16 pide comparar con la línea base: eso solo se puede "
              "hacer con algo acotado."},
        {"p": "¿Cómo conseguimos una cifra si no tenemos acceso a datos?",
         "r": "Preguntando, contando o cronometrando. Tres preguntas a la persona que hace el "
              "trabajo, un conteo de una semana con una hoja, o el tiempo de un caso medido con el "
              "celular. Se acepta una muestra pequeña y una estimación, **siempre que digan que lo "
              "es y de dónde viene**. Lo que no se acepta es un número sin origen."},
        {"p": "¿Podemos cambiar el problema después?",
         "r": "Sí, pero cuesta. Todo lo que sigue se construye sobre esta ficha: el ciclo de vida "
              "de la sesión 7, el prototipo de la 10 y la 11, el impacto de la 13, el informe de la "
              "16. Un cambio en la sesión 8 es un ajuste; en la sesión 12 es empezar de nuevo. Por "
              "eso vale la pena discutirlo hoy hasta que quede."},
        {"p": "¿Y si ya sabemos qué tecnología queremos usar?",
         "r": "Perfecto, pero no va en el enunciado del problema. Escriban el problema sin "
              "mencionarla y en la sesión 10 la eligen con argumentos. Si la tecnología está en la "
              "frase del problema, ya no hay nada que diseñar: solo queda ejecutar una decisión que "
              "nadie justificó."},
        {"p": "¿La evaluación de corte cubre todo, incluidas las lecturas?",
         "r": "Cubre las sesiones 1 a 6: qué es y qué no es la ingeniería, historia y hitos, los "
              "cinco elementos de un sistema, los principios éticos y las tres normas colombianas, "
              "las cuatro etapas de la huella, y problema contra síntoma. Se responde en ExamLab en "
              "los últimos 20 minutos de la sesión, es individual, y si el enlace no le abre lo "
              "avisa **en el chat en el momento**."},
    ],

    "notas_operativas": [
        "**El reparto de tiempo de hoy es distinto: teoría 25 min, no 45.** Quedarse largo en la "
        "explicación significa aplicar la evaluación de corte con el grupo apurado. Ponga una alarma "
        "a los 35 minutos.",
        "**Anuncie la evaluación de corte en el minuto 2**, con la agenda en pantalla. La gente "
        "organiza la atención distinto sabiendo que hay evaluación al cierre, y así nadie se "
        "desconecta después de exponer.",
        "**Prepare el enlace de ExamLab antes de la sesión** y verifique que abre. Al pegarlo, pida "
        "que cada uno confirme en el chat que entró: en virtual, el que no pudo abrir se queda "
        "callado.",
        "Diga en voz alta que **ExamLab no es una plataforma oficial de la universidad**: es la "
        "herramienta de evaluación de este curso.",
        "Si alguien pierde la conexión durante la evaluación, anótelo y **resuélvalo el mismo día**. "
        "Un problema técnico no atendido se vuelve un reclamo de nota dos semanas después.",
        "En las salas, haga **una sola pregunta: ¿cuál es la cifra?** Es lo que falta en la mayoría "
        "de las fichas y es el 25 % de la rúbrica.",
        "**Anote las cinco fichas** al terminar las exposiciones. Son el insumo directo de la sesión "
        "7 y la referencia del informe final.",
        "Hoy no se usa IA: el problema tiene que salir del entorno que ellos conocen, y un asistente "
        "lo devuelve genérico y sin cifra.",
    ],

    "ti_siguiente": {
        "tid": "Identificación de problemáticas locales — cerrar la ficha con la cifra medida de "
               "verdad, no estimada, si esta semana alcanzan a contar o preguntar.",
        "ti": "Propuesta inicial de solución: media página con **dos** alternativas para atacar la "
              "causa elegida, sin decidir todavía cuál. Sin nombrar herramientas.",
        "adelanto": "el **ciclo de vida de los proyectos de ingeniería**, aplicado a la ficha de "
                    "hoy: qué se hace antes de construir y por qué el orden importa.",
        "aviso": "Arranca el corte 2. La ficha del problema queda como referencia fija: llévenla al "
                 "documento del equipo con el título «Ficha del problema — versión final del corte "
                 "1», porque se va a citar en todas las sesiones que siguen.",
    },

    "cierre_titulo": "Cerró el corte 1 · nos vemos en la sesión 7",
    "cierre_frase": "El problema quedó escrito. Todo lo que sigue se hace sobre esa ficha",
}
