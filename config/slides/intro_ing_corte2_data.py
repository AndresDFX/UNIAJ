# -*- coding: utf-8 -*-
"""Contenido de las clases 7 a 11 de Introduccion a la Ingenieria (FI300101) · Corte 2.

Este modulo SI lleva tildes: casi todo su texto acaba proyectado o convertido a .docx.
Nunca usar comillas dobles escapadas dentro de estos textos: se usan « ».

Material general para los tres grupos: nada de fechas, horas de pared ni codigos de grupo.

Hilo del corte 2 (30%): la ficha del problema que salio de la sesion 6 se convierte en una
solucion prototipada. Sesion 7 el ciclo de vida, sesion 8 la decision entre alternativas,
sesion 9 los antecedentes y la propuesta de mejora, sesion 10 el prototipo de baja fidelidad,
sesion 11 el prototipo v2 con IA + evaluacion de corte. Cierra en la sesion 11.
"""

TEMAS = {}


# =============================================================================
# CLASE 7 · Ciclo de vida de los proyectos de ingenieria
# =============================================================================

TEMAS[7] = {
    "n": 7,
    "titulo": "Ciclo de vida de los proyectos de ingeniería",
    "subtitulo": "Por qué el orden de las fases decide el costo del error",
    "hook": "¿Cuánto cuesta mover una pared? Depende de si está en el plano, "
            "en el ladrillo o en la casa ya entregada.",
    "hook_lines": [
        "En el plano cuesta un borrador. En la casa terminada cuesta tumbarla.",
        "El software tiene la misma curva, y es la razón por la que existen las fases.",
    ],
    "objetivos": [
        "Nombrar las **fases del ciclo de vida** de un proyecto y qué se entrega en cada una.",
        "Explicar por qué **el costo de corregir un error crece** con la fase en que se descubre.",
        "Distinguir un **requisito funcional** de uno **no funcional**, y escribir su criterio de aceptación.",
        "Ubicar el proyecto del equipo en una fase y decir **qué falta para cerrarla**.",
    ],
    "agenda": {
        "Teoría y guía del docente": "Teoría — fases, costo del cambio, cascada vs. iterativo y requisitos",
        "Actividad en equipos": "Taller — el ciclo de vida del proyecto, en draw.io",
        "Exposiciones": "5 equipos × 3 min — en qué fase están y qué falta para cerrarla",
    },
    "herramienta_nota": "El mapa del ciclo de vida se hace en **diagrams.net (draw.io)**, que abre "
                        "sin cuenta y guarda en la carpeta del equipo. La tabla de requisitos va "
                        "en el **documento del equipo**. Hoy no se usa IA: los requisitos tienen "
                        "que salir de la ficha del problema de la sesión 6, y un asistente los "
                        "devuelve genéricos y sin las restricciones del caso.",
    "avance_proyecto": "Escribir los requisitos mínimos del proyecto con su criterio de aceptación, "
                       "y el plan de hitos hasta la exposición final",

    "teoria": [
        {
            "tipo": "steps",
            "titulo": "Las seis fases del ciclo de vida",
            "steps": [
                ("DEFINICIÓN DEL PROBLEMA", "Qué se va a resolver y para quién. **Esto ya lo hicieron en la sesión 6**: es la ficha del problema"),
                ("REQUISITOS", "Qué tiene que hacer la solución para resolverlo, y cómo se sabrá que lo hace"),
                ("DISEÑO", "Cómo va a estar construida: las partes, el flujo, las pantallas o los pasos"),
                ("CONSTRUCCIÓN", "Se construye. Es la fase que todo el mundo cree que es «el proyecto», y es una de seis"),
                ("VALIDACIÓN", "Se prueba contra los criterios de aceptación **y con el usuario real**, no solo con el equipo"),
                ("OPERACIÓN Y RETIRO", "Funcionando en la vida real, con mantenimiento. Y al final, cómo se apaga y qué pasa con los datos"),
            ],
            "sub": "El orden no es burocracia: cada fase produce lo que la siguiente necesita para no adivinar",
        },
        {
            "tipo": "tabla",
            "titulo": "Lo que cuesta cambiar en cada fase",
            "headers": ["Se descubre en…", "Qué hay que rehacer", "Orden de magnitud del costo"],
            "rows": [
                ["Definición del problema",
                 "Una frase en un documento. Nada más existe todavía.",
                 "**1** — el costo de una conversación"],
                ["Requisitos",
                 "Una línea de la tabla de requisitos y su criterio de aceptación.",
                 "**pocas veces** más que en la fase anterior"],
                ["Diseño",
                 "El diagrama, y las decisiones que colgaban de él.",
                 "**varias veces** más: hay que rediseñar y volver a acordar"],
                ["Construcción",
                 "Lo construido, más el diseño, más el requisito que estaba mal.",
                 "**decenas de veces** más"],
                ["Después de entregado",
                 "Todo lo anterior, con el usuario ya usándolo, más el daño que alcanzó a hacer.",
                 "**órdenes de magnitud** más"],
            ],
            "note": "La forma de esta curva la documentó Barry Boehm en los años setenta y sigue "
                    "vigente. Los múltiplos exactos se discuten; **la dirección no**: el error "
                    "barato es el que se encuentra temprano.",
            "col_w": [2.0, 4.0, 3.8],
        },
        {
            "tipo": "before_after",
            "titulo": "Una sola pasada o varias vueltas",
            "before_title": "Cascada de una sola pasada",
            "before": [
                "Se recorren las fases una vez, de arriba abajo.",
                "El usuario ve el resultado **al final**.",
                "Si un requisito estaba mal, se descubre en validación.",
                "Funciona cuando el problema es conocido y estable.",
                "**Royce, que dibujó el diagrama en 1970, advirtió en el mismo texto que hacerlo de una sola pasada invita al fracaso.**",
            ],
            "after_title": "Iterativo e incremental",
            "after": [
                "Se recorren las fases **varias veces**, con un pedazo cada vez.",
                "El usuario ve algo **en cada vuelta** y corrige temprano.",
                "El requisito mal escrito se cae en la primera iteración, barato.",
                "Funciona cuando hay incertidumbre — es decir, casi siempre.",
                "Es lo que va a hacer este curso: **una vuelta corta en las sesiones 10–11 y otra en las 12–14**.",
            ],
            "sub": "Las fases son las mismas en los dos. Lo que cambia es cuántas veces se recorren y cuándo aparece el usuario",
            "size": 13,
        },
        {
            "tipo": "cards",
            "titulo": "Cuatro cosas que se entregan y no son código",
            "cards": [
                ("Requisito funcional",
                 "Algo que la solución **hace**: «el usuario puede consultar si un libro está "
                 "disponible sin ir a la biblioteca». Se escribe desde el usuario, no desde la "
                 "tecnología."),
                ("Requisito no funcional",
                 "Una **condición** que debe cumplir: funcionar en un computador de siete años, "
                 "abrir sin crear cuenta, no guardar datos personales. **Salen de las "
                 "restricciones del árbol de la sesión 6.**"),
                ("Criterio de aceptación",
                 "Cómo se comprueba que el requisito se cumple, con un caso concreto: «un usuario "
                 "que no conoce el sistema encuentra la disponibilidad de un libro en menos de un "
                 "minuto, sin ayuda»."),
                ("Hito",
                 "Un punto del calendario donde algo queda **terminado y verificable**. No es «ir "
                 "avanzando»: es «en la sesión 10 hay tres pantallas probadas con un usuario»."),
            ],
            "columns": 2,
        },
        {
            "tipo": "box",
            "titulo": "Tres malentendidos que salen caros",
            "notas": [
                ("advertencia",
                 "**«Las fases son burocracia, lo importante es construir.»** Construir sin "
                 "requisitos es construir algo que habrá que rehacer, y rehacer en la fase de "
                 "construcción cuesta decenas de veces más que corregir una línea de la tabla de "
                 "requisitos. Las fases no son papeleo: son el orden que hace barato el error."),
                ("aclaracion",
                 "**«Trabajar iterativo o ágil significa no planear.»** Es lo contrario: se planea "
                 "más seguido y en pedazos más pequeños. Una iteración sin requisitos ni criterio "
                 "de aceptación no es una iteración, es improvisación con nombre nuevo."),
                ("info",
                 "**Las fases no son departamentos ni personas.** En un equipo de cinco, las seis "
                 "fases las recorren los mismos cinco. Lo que cambia no es quién trabaja: es qué "
                 "pregunta se está respondiendo en ese momento."),
            ],
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada: la curva del costo del cambio",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "La analogía de la pared es la más eficiente que existe para esta clase porque "
                "nadie necesita saber de software para responderla. Mover una pared en el plano "
                "cuesta un borrador; en el ladrillo cuesta tumbar y volver a levantar; en la casa "
                "entregada cuesta la obra, la mudanza y el enojo del dueño. Todo el mundo lo "
                "intuye, y esa intuición es exactamente la curva del costo del cambio.",
                "Lo que hay que hacer explícito en el minuto 12 es que **en software la curva es "
                "igual pero se ve menos**, y ahí está el problema. En una casa, una pared mal "
                "puesta se ve; en un sistema, un requisito mal entendido no se ve hasta que "
                "alguien lo usa. Por eso en ingeniería de software hubo que inventar fases, "
                "revisiones y criterios de aceptación: son el equivalente a mirar el plano antes de "
                "pedir el cemento.",
                "Recoja las respuestas en el muro. Van a salir cifras espontáneas —«mil veces más "
                "caro»— y conviene no corregirlas ahí, sino usarlas cuando llegue la tabla: la "
                "dirección de la curva es correcta y los múltiplos exactos son discutibles, lo cual "
                "es una buena lección sobre cómo se citan los datos.",
            ],
        },
        {
            "titulo": "Las seis fases, y por qué el orden importa",
            "slide": "{{slide:Las seis fases}}",
            "cuerpo": [
                "Conviene presentar las fases como una cadena de preguntas, no como una lista de "
                "etapas administrativas. Cada fase responde una pregunta y produce lo que la "
                "siguiente necesita para no adivinar.",
                "**Definición del problema** responde *qué se va a resolver y para quién*, y hay "
                "que decir en voz alta que **esa fase ya la hicieron en la sesión 6**: la ficha del "
                "problema es el entregable de la primera fase del ciclo de vida de su propio "
                "proyecto. Eso reordena la percepción del curso: no estaban haciendo un ejercicio, "
                "estaban cerrando una fase.",
                "**Requisitos** responde *qué tiene que hacer la solución para resolver eso, y cómo "
                "sabremos que lo hace*. Es la fase de hoy y la que más se salta la gente.",
                "**Diseño** responde *cómo va a estar construido*: las partes, el flujo, las "
                "pantallas o los pasos. **Construcción** es la única fase que el estudiante "
                "reconoce como «el proyecto», y vale la pena decirle que es una de seis, y no la "
                "más determinante. **Validación** responde *funciona contra los criterios y con el "
                "usuario real*; la trampa clásica es probar con el propio equipo, que ya sabe cómo "
                "se usa. Y **operación y retiro** es la fase que nadie enseña en primer semestre y "
                "que conviene nombrar por dos razones: la mayor parte de la vida de un sistema "
                "ocurre ahí, y el retiro —qué pasa con los datos cuando el sistema se apaga— es un "
                "asunto ético y legal que ya vieron en la sesión 4 con la Ley 1581.",
                "El punto que amarra todo: **el orden no es burocracia, es economía**. Cada fase "
                "existe porque descubrir un error en ella cuesta menos que descubrirlo en la "
                "siguiente. Quien se salta requisitos no ahorra tiempo: mueve el costo hacia "
                "adelante y lo multiplica.",
            ],
        },
        {
            "titulo": "La curva del costo del cambio: qué se puede afirmar y qué no",
            "slide": "{{slide:Lo que cuesta cambiar}}",
            "cuerpo": [
                "Esta tabla es el corazón cuantitativo de la sesión y hay que manejarla con el "
                "mismo rigor que se les exigió en la sesión 5 con las cifras ambientales. **Lo que "
                "se puede afirmar con seguridad: el costo de corregir un error crece con la fase en "
                "que se descubre, y crece por órdenes de magnitud entre los extremos.** La forma de "
                "esa curva la documentó Barry Boehm en los años setenta a partir de datos de "
                "proyectos reales, y se ha vuelto a medir muchas veces desde entonces.",
                "**Lo que no conviene afirmar: los múltiplos exactos.** Circulan tablas con «1× / "
                "5× / 10× / 100×» presentadas como leyes de la naturaleza, y hay literatura que "
                "discute si en desarrollo iterativo la curva es tan pronunciada. Diga eso "
                "explícitamente en clase: es una oportunidad de oro para mostrar que un ingeniero "
                "puede usar un resultado clásico sin exagerarlo. La dirección de la curva no está "
                "en discusión; la pendiente sí.",
                "El uso práctico de la tabla es una pregunta que los equipos van a responder en el "
                "taller: *¿qué decisión que estamos tomando hoy sería carísima cambiar en la sesión "
                "14?* Casi siempre la respuesta es un requisito mal entendido o una restricción "
                "ignorada, y hacer la pregunta hoy es lo que la vuelve barata.",
                "Hay un segundo uso, más sutil, que vale la pena señalar si el grupo responde bien: "
                "la curva explica por qué las revisiones tempranas —que se sienten como pérdida de "
                "tiempo porque todavía no hay nada construido— son la actividad más rentable del "
                "proyecto. En el Therac-25 de la sesión 4, la revisión independiente del software "
                "que nunca se hizo era justamente eso.",
            ],
        },
        {
            "titulo": "Cascada, iterativo, y lo que Royce dijo de verdad",
            "slide": "{{slide:Una sola pasada}}",
            "cuerpo": [
                "En la sesión 2 apareció Royce y su artículo de 1970. Hoy se cierra el punto, "
                "porque es una de las confusiones más extendidas de la profesión: **el diagrama de "
                "cascada de una sola pasada suele atribuirse a Royce como su propuesta, y en el "
                "mismo texto él lo presentó como el modo riesgoso y advirtió que hacerlo así invita "
                "al fracaso**. Su propuesta incluía volver atrás, prototipar y hacer el trabajo "
                "dos veces. La profesión se quedó con el dibujo y perdió la advertencia.",
                "La comparación que importa para el curso no es «cascada mala, ágil bueno» —esa es "
                "una caricatura y hay que evitarla—. Es esta: **las fases son las mismas en los "
                "dos; lo que cambia es cuántas veces se recorren y cuándo aparece el usuario**. La "
                "cascada de una pasada es razonable cuando el problema es conocido, estable y el "
                "costo de equivocarse al final es asumible. El enfoque iterativo es mejor cuando "
                "hay incertidumbre sobre qué necesita el usuario, que es la situación normal y en "
                "particular la de todos los proyectos de este curso.",
                "Aterrícelo en el calendario, porque eso les hace sentir la diferencia: **este "
                "curso va a hacer dos vueltas completas**. Una corta en las sesiones 10 y 11 "
                "—prototipo de baja fidelidad, prueba, corrección— y otra en las sesiones 12 a 14, "
                "con la retroalimentación de la presentación de avances. No es una decisión "
                "estética del docente: es la manera de que el error de requisitos aparezca en la "
                "sesión 10 y no en la 15, cuando ya no hay tiempo.",
                "Si alguien pregunta por el Manifiesto Ágil de 2001, que salió en la sesión 2: la "
                "respuesta honesta es que reordenó prioridades —software funcionando sobre "
                "documentación, colaboración sobre contrato— y que no eliminó las fases. Un equipo "
                "ágil sigue definiendo el problema, escribiendo requisitos, diseñando, "
                "construyendo y validando; lo hace en ciclos cortos y con menos ceremonia.",
            ],
        },
        {
            "titulo": "Requisitos, criterios de aceptación y hitos: lo que se entrega hoy",
            "slide": "{{slide:Cuatro cosas que se entregan}} {{slide:Tres malentendidos}}",
            "cuerpo": [
                "**Requisito funcional** es algo que la solución hace, escrito desde el usuario: "
                "«el usuario puede consultar si un libro está disponible sin ir a la biblioteca». "
                "El error típico de primer semestre es escribirlo desde la tecnología —«el sistema "
                "tendrá una base de datos MySQL»—, que no es un requisito sino una decisión de "
                "diseño disfrazada, y encima toma la decisión en la fase equivocada.",
                "**Requisito no funcional** es una condición que la solución debe cumplir: "
                "funcionar en un computador viejo, abrir sin crear cuenta, responder en menos de "
                "tanto, no guardar datos personales. Aquí hay una conexión que hay que hacer "
                "explícita y que le da sentido a dos sesiones anteriores: **los requisitos no "
                "funcionales de sus proyectos salen de las restricciones que marcaron en el árbol "
                "de la sesión 6 y del indicador ambiental de la sesión 5**. Si la biblioteca no "
                "tiene computador en el mostrador, «funciona desde el celular de la voluntaria» es "
                "un requisito no funcional, no un detalle.",
                "**Criterio de aceptación** es la parte que casi nadie escribe y la que vuelve "
                "verificable el proyecto: cómo se comprueba que el requisito se cumple, con un caso "
                "concreto y un umbral. «Un usuario que no conoce el sistema encuentra la "
                "disponibilidad de un libro en menos de un minuto, sin ayuda» se puede ejecutar "
                "delante de alguien. «El sistema debe ser fácil de usar» no se puede ejecutar, y "
                "por lo tanto no sirve. La regla que conviene dictar: **si no se puede convertir en "
                "una prueba que alguien haga, no es un criterio**.",
                "**Hito** es un punto del calendario donde algo queda terminado y verificable. Es "
                "el concepto que salva el proyecto de la última semana: «vamos avanzando» no es un "
                "hito; «en la sesión 10 hay tres pantallas probadas con un usuario» sí. En el "
                "taller de hoy se les pide el plan de hitos hasta la sesión 15, y conviene revisarlo "
                "con severidad, porque un plan con todo el trabajo en la sesión 14 es un proyecto "
                "que va a fallar y todavía se puede corregir.",
                "Los tres malentendidos de la última diapositiva son los que aparecen en las salas. "
                "El primero —que las fases son burocracia— se responde con la tabla del costo. El "
                "segundo —que iterativo significa no planear— se responde señalando que se planea "
                "más seguido, no menos. El tercero conviene decirlo porque tranquiliza: **las fases "
                "no son departamentos ni personas**; en un equipo de cinco, las seis fases las "
                "recorren los mismos cinco, y lo que cambia es la pregunta que están respondiendo.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:10 · Apertura · [Slide 4]",
            "cuerpo": [
                "Comparta pantalla antes de que entre el primero:",
                "> «¿Cuánto cuesta mover una pared? Depende de si está en el plano, en el ladrillo "
                "o en la casa ya entregada.»",
                "**[Nota docente]:** enlace del muro en el chat. Van a aparecer cifras inventadas "
                "(«mil veces más»). No las corrija: úselas en el minuto 25 con la tabla.",
                "**[Nota docente]:** pida que abran la **ficha del problema de la sesión 6**. Todo "
                "el taller de hoy cuelga de ella; sin ficha no hay requisitos.",
            ],
        },
        {
            "titulo": "00:10–00:55 · Teoría · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]",
            "cuerpo": [
                "Reparto sugerido de los 45 min:",
                "- **9 min** · Las seis fases [Slide 5]. Diga explícitamente que **la fase 1 ya la "
                "cerraron en la sesión 6**: eso reordena cómo ven el curso.",
                "- **10 min** · La curva del costo [Slide 6]. Vuelva al muro. Sea honesto con las "
                "cifras: la dirección de la curva no se discute, los múltiplos sí.",
                "- **9 min** · Una sola pasada o varias vueltas [Slide 7]. Cierre el punto de Royce "
                "de la sesión 2 y anuncie las **dos vueltas** de este curso (10–11 y 12–14).",
                "- **12 min** · Cuatro cosas que se entregan [Slide 8]. Es la más operativa: de "
                "aquí sale el taller. Insista en que **los requisitos no funcionales salen de las "
                "restricciones del árbol de la sesión 6**.",
                "- **5 min** · Tres malentendidos [Slide 9].",
                "**[Nota docente]:** si va retrasado, recorte los malentendidos a dos minutos. **No "
                "recorte la diapositiva de requisitos y criterios**: sin ella el taller no se puede "
                "hacer.",
            ],
        },
        {
            "titulo": "00:55–01:12 · Taller en salas de grupo · [Slide 10]",
            "cuerpo": [
                "**2 min** para abrir draw.io y el documento del equipo. Cada equipo trabaja su "
                "propio proyecto.",
                "**15 min** en salas. Entre a las cinco, ~3 min cada una, con **una sola pregunta: "
                "¿cómo se comprueba ese requisito?** El criterio de aceptación es lo que falta "
                "siempre.",
                "**[Nota docente]:** el error a cortar en caliente es el requisito escrito desde la "
                "tecnología («el sistema tendrá una base de datos»). Pregunte «¿y eso qué le permite "
                "hacer al usuario?» y reescríbalo con ellos.",
                "**[Nota docente]:** revise el plan de hitos con severidad. Si todo el trabajo cae "
                "en la sesión 14, dígalo ahora: es un proyecto que va a fallar y todavía hay nueve "
                "sesiones para arreglarlo.",
            ],
        },
        {
            "titulo": "01:12–01:27 · Exposiciones · [Slide 11]",
            "cuerpo": [
                "5 equipos × 3 min con el diagrama compartido. **El minuto obligatorio es «en qué "
                "fase estamos y qué falta para cerrarla»**.",
                "**[Nota docente]:** los cinco enlaces en el chat antes de arrancar.",
                "**[Nota docente]:** anote la fase declarada por cada equipo y su hito de la sesión "
                "10. En la sesión 10 se verifica contra eso, y es la manera más simple de detectar "
                "a un equipo atrasado antes de que sea tarde.",
            ],
        },
        {
            "titulo": "01:27–01:30 · Cierre · [Slide 12][Slide 13]",
            "cuerpo": [
                "Una idea: **el orden de las fases no es burocracia, es economía.** El error barato "
                "es el que se encuentra temprano, y por eso hoy escribieron requisitos en vez de "
                "empezar a construir.",
                "Anuncie la sesión 8: se aplica esto a **casos reales de proyectos que se saltaron "
                "una fase**, y cada equipo decide entre sus dos alternativas de solución.",
            ],
        },
    ],

    "taller": {
        "archivo": "Ciclo de vida del proyecto",
        "titulo": "Ciclo de vida del proyecto",
        "min": 17,
        "exposicion": 3,
        "consigna": "Ubiquen su proyecto en el ciclo de vida y escriban lo que falta para avanzar: "
                    "en qué **fase** están, **tres requisitos funcionales** y **dos no "
                    "funcionales** con su **criterio de aceptación**, la decisión de hoy que sería "
                    "carísima cambiar después, y el **plan de hitos** hasta la sesión 15.",
        "entregable": "el mapa del ciclo de vida del proyecto en draw.io (PNG en la carpeta del "
                      "equipo) más la tabla de requisitos y el plan de hitos en el documento del "
                      "equipo",
        "entregable_corto": "mapa del ciclo de vida + tabla de requisitos + plan de hitos",
        "reparto_titulo": "No se sortea nada:",
        "reparto": "cada equipo trabaja su propio proyecto, con la ficha del problema de la sesión 6 "
                   "abierta al lado. Los requisitos no funcionales salen de las **restricciones** "
                   "que marcaron en el árbol, y uno de ellos es el **indicador ambiental** de la "
                   "sesión 5.",
        "reparto_corto": "cada equipo, su propio proyecto",
        "bloques": [
            {"clave": "EN QUÉ FASE ESTAMOS",
             "pide": "La fase donde está el proyecto hoy, y **qué falta exactamente para cerrarla**. "
                     "Una fase se cierra con un entregable, no con una sensación.",
             "check": "hay una fase y un entregable pendiente concreto. «Estamos en diseño» sin decir qué falta no cuenta."},
            {"clave": "TRES REQUISITOS FUNCIONALES",
             "pide": "Tres cosas que la solución **hace**, escritas desde el usuario: «el usuario "
                     "puede…». Sin mencionar tecnología.",
             "check": "los tres empiezan por el usuario y ninguno nombra una herramienta, un lenguaje o una base de datos."},
            {"clave": "DOS REQUISITOS NO FUNCIONALES",
             "pide": "Dos condiciones que la solución debe cumplir, **derivadas de las "
                     "restricciones del árbol de la sesión 6**. Uno de los dos tiene que ser el "
                     "indicador ambiental de la sesión 5.",
             "check": "los dos se pueden rastrear a una restricción escrita antes. Un requisito no funcional inventado hoy no cuenta."},
            {"clave": "LOS CRITERIOS DE ACEPTACIÓN",
             "pide": "Para cada uno de los cinco requisitos: cómo se comprueba, con un caso "
                     "concreto y un umbral. Tiene que poder ejecutarlo otra persona.",
             "check": "cada criterio es una prueba que alguien puede hacer delante de ustedes. «Debe ser fácil de usar» no es un criterio."},
            {"clave": "EL PLAN DE HITOS",
             "pide": "Qué queda **terminado y verificable** en cada una de las sesiones 8, 9, 10, "
                     "11, 12 y 14. Y la decisión de hoy que sería carísima cambiar en la sesión 14.",
             "check": "cada hito es verificable y el trabajo está repartido. Si todo cae en la sesión 14, el plan está mal."},
        ],
        "expo": [
            ("30 s · La fase", "En qué fase están y qué falta para cerrarla. Es el minuto obligatorio."),
            ("50 s · Los requisitos", "Uno funcional y uno no funcional, leídos tal cual."),
            ("50 s · El criterio de aceptación", "De ese requisito: cómo se comprueba y con qué umbral."),
            ("40 s · El plan de hitos", "Qué queda listo en la sesión 10 y en la 12."),
            ("10 s · La decisión costosa", "Qué sería carísimo cambiar después."),
        ],
    },

    "rubrica": [
        ("La fase está identificada y se dice qué entregable falta para cerrarla", 15,
         "Cerrar una fase con un entregable, y no con una sensación de avance, es la disciplina que ordena el proyecto."),
        ("Los tres requisitos funcionales están escritos desde el usuario y sin tecnología", 25,
         "Un requisito escrito desde la tecnología toma una decisión de diseño en la fase equivocada."),
        ("Los dos requisitos no funcionales se rastrean a restricciones ya escritas", 20,
         "Es lo que conecta el análisis de las sesiones 5 y 6 con la construcción: las restricciones son insumo, no adorno."),
        ("Cada requisito tiene un criterio de aceptación ejecutable por otra persona", 25,
         "Sin criterio de aceptación no hay validación posible, y la sesión 16 pide demostrar, no afirmar."),
        ("El plan de hitos reparte el trabajo y cada hito es verificable", 15,
         "Un plan con todo al final es la causa más común de proyectos que no se entregan."),
    ],

    "solucion": {
        "para_que": "Este documento trae el ciclo de vida completo del caso de la biblioteca, con "
                    "los cinco requisitos escritos y sus criterios de aceptación, más el plan de "
                    "hitos hasta la sesión 15. Es el modelo que hay que tener a mano en las salas, "
                    "porque el criterio de aceptación es lo que ningún equipo escribe solo. Si el "
                    "docente solo alcanza a leer un bloque, que sea **LOS CRITERIOS DE "
                    "ACEPTACIÓN**.",
        "caso_titulo": "La biblioteca del barrio · del problema a los requisitos",
        "caso": "Se retoma la ficha cerrada en la sesión 6: los usuarios no pueden saber si un libro "
                "está disponible antes de ir, así que hacen viajes que terminan sin préstamo (unas 4 "
                "de cada 10 visitas). Causa elegida: el registro de préstamos solo se puede "
                "consultar en el mostrador. Restricciones marcadas: presupuesto cero, no hay "
                "computador disponible en el mostrador durante la atención, las voluntarias rotan y "
                "no se les puede exigir capacitación larga, y nadie puede atender un teléfono en "
                "horario fijo.",
        "por_que_este_caso": "Es el mismo caso desde la sesión 1, y hoy es donde se cobra: las "
                             "cuatro restricciones que en la sesión 6 parecían una formalidad se "
                             "convierten hoy en requisitos no funcionales que descartan la mitad de "
                             "las soluciones posibles. Mostrar esa conversión es la lección de la "
                             "sesión.",
        "bloques": [
            {
                "clave": "EN QUÉ FASE ESTAMOS",
                "respuesta": "**Fase: requisitos.** La fase 1 —definición del problema— quedó "
                             "cerrada en la sesión 6 con la ficha, que tiene enunciado, línea base, "
                             "árbol de causas, actores y criterio de éxito.\n\n"
                             "**Qué falta para cerrar la fase de requisitos:** la tabla de "
                             "requisitos con sus criterios de aceptación **validada con la "
                             "coordinadora de la biblioteca**. Este último detalle es el que "
                             "distingue una fase cerrada de una fase que se cree cerrada: los "
                             "requisitos no se aprueban entre los cinco del equipo, se confirman "
                             "con quien vive el problema.\n\n"
                             "**Qué NO es cerrar la fase:** tener una idea clara de lo que se va a "
                             "hacer. Una fase se cierra con un entregable que otra persona puede "
                             "leer y objetar.",
                "como_calificar": "15 pts. Se califica que haya **un entregable pendiente "
                                  "concreto**, no una sensación. «Estamos en diseño» vale 5; "
                                  "«estamos en requisitos y falta la tabla validada con la "
                                  "coordinadora» vale los 15. Si el equipo dice que está en "
                                  "construcción sin tener requisitos escritos, es la señal de alarma "
                                  "de la sesión y hay que decírselo en la sala: está a punto de "
                                  "construir algo que va a rehacer."
            },
            {
                "clave": "TRES REQUISITOS FUNCIONALES",
                "respuesta": "1. **El usuario puede saber si un libro está disponible sin ir a la "
                             "biblioteca.**\n"
                             "2. **La voluntaria puede registrar un préstamo y una devolución en "
                             "menos pasos que en el cuaderno**, sin dejar de atender al usuario que "
                             "tiene enfrente.\n"
                             "3. **El usuario puede ver qué libros hay sobre un tema**, aunque no "
                             "sepa el título exacto — es el caso real del estudiante de colegio con "
                             "una tarea.\n\n"
                             "Los tres empiezan por el actor y ninguno menciona tecnología: podrían "
                             "resolverse con una lista publicada, un mensaje automático o una "
                             "aplicación, y esa apertura es deliberada, porque la decisión de "
                             "**cómo** es de la fase de diseño y se toma en la sesión 8.\n\n"
                             "**Ejemplos de requisitos mal escritos, para comparar en clase:** «el "
                             "sistema tendrá una base de datos con los libros» (decisión de diseño "
                             "disfrazada de requisito, y tomada dos fases antes de tiempo); «el "
                             "sistema será rápido y fácil de usar» (no es funcional y no es "
                             "verificable); «hacer una app para la biblioteca» (es la solución, no "
                             "el requisito, y es el error de la sesión 6 reapareciendo).",
                "como_calificar": "25 pts. Dos verificaciones mecánicas: (a) **¿empieza por el "
                                  "actor?** Si empieza por «el sistema tendrá», reescríbalo con "
                                  "ellos y baje a 15; (b) **¿nombra alguna tecnología?** Si nombra "
                                  "lenguaje, base de datos o plataforma, baje a 12 y explique por "
                                  "qué: no es un error de forma, es tomar una decisión en la fase "
                                  "equivocada. Acepte requisitos modestos: tres requisitos "
                                  "pequeños y bien escritos valen más que diez ambiciosos."
            },
            {
                "clave": "DOS REQUISITOS NO FUNCIONALES",
                "respuesta": "1. **Funciona sin computador en el mostrador**: la voluntaria lo usa "
                             "desde su propio celular, y el usuario desde el suyo. *Viene de la "
                             "restricción «no hay computador disponible en el mostrador durante la "
                             "atención».*\n"
                             "2. **Se aprende en menos de cinco minutos y sin manual**, porque las "
                             "voluntarias rotan. *Viene de la restricción «las voluntarias rotan y "
                             "no se les puede exigir capacitación larga».*\n\n"
                             "**Y el que exige el curso, derivado del indicador ambiental de la "
                             "sesión 5:** *funciona en el computador de siete años del consultorio "
                             "—en este caso, en celulares de gama baja y con datos móviles—, "
                             "moviendo menos de 200 KB por consulta*. Este requisito no es "
                             "decoración: descarta soluciones con imágenes pesadas y con "
                             "actualización permanente, y por lo tanto **es información de diseño**.\n\n"
                             "Nótese el efecto conjunto: estos tres requisitos no funcionales "
                             "**descartan la mitad de las soluciones imaginables** antes de "
                             "diseñar nada. Eso es exactamente lo que deben hacer, y es la razón "
                             "por la que las restricciones de la sesión 6 no eran una formalidad.\n\n"
                             "**Lo que no se acepta:** un requisito no funcional inventado hoy y "
                             "sin rastro («debe ser escalable», «debe usar la nube»). Si no se "
                             "puede señalar la restricción de donde salió, no entró por la puerta "
                             "correcta.",
                "como_calificar": "20 pts, 10 por requisito. El criterio duro es la **trazabilidad**: "
                                  "pida que señalen la restricción del árbol de la sesión 6 de donde "
                                  "salió. Sin rastro, 4 puntos. Si el equipo incorpora el indicador "
                                  "ambiental de la sesión 5 como requisito no funcional, dé los 20 "
                                  "completos: significa que el curso está acumulando y no "
                                  "empezando de cero cada semana."
            },
            {
                "clave": "LOS CRITERIOS DE ACEPTACIÓN",
                "respuesta": "**R1 · saber la disponibilidad sin ir.** *Un usuario que nunca ha "
                             "usado el sistema, con el celular en la mano y sin ayuda, averigua si "
                             "un libro concreto está disponible en menos de un minuto. Se prueba "
                             "con tres personas distintas; se acepta si las tres lo logran.*\n\n"
                             "**R2 · registrar préstamo y devolución.** *La voluntaria registra un "
                             "préstamo en menos de 30 segundos, cronometrado, mientras el usuario "
                             "espera. Se compara contra el tiempo del cuaderno, medido antes.*\n\n"
                             "**R3 · buscar por tema.** *Un estudiante que solo sabe el tema («algo "
                             "sobre la Guerra de los Mil Días») obtiene al menos un título "
                             "disponible o la respuesta «no hay», sin preguntarle a nadie.*\n\n"
                             "**RNF1 · sin computador.** *Todo el flujo de R1, R2 y R3 se ejecuta "
                             "completo desde un celular, con el navegador, sin instalar nada.*\n\n"
                             "**RNF2 · se aprende sin manual.** *Una persona que no participó en el "
                             "proyecto y no recibió explicación registra un préstamo correctamente "
                             "en el primer intento.*\n\n"
                             "**RNF3 · menos de 200 KB por consulta.** *Se mide con las "
                             "herramientas del navegador en tres consultas seguidas.*\n\n"
                             "Los seis tienen la misma forma: **un actor, una acción, una condición "
                             "y un umbral**, y todos los puede ejecutar alguien que no sea del "
                             "equipo. Eso es lo que se está calificando.",
                "como_calificar": "25 pts, el bloque que decide. La prueba es literal: **lea el "
                                  "criterio y pregúntese si usted podría ejecutarlo mañana sin "
                                  "pedir aclaraciones**. Si no, no es un criterio. «Debe ser "
                                  "intuitivo», «debe funcionar bien», «el usuario quedará "
                                  "satisfecho» valen 0 y hay que reescribirlos en la sala, no en la "
                                  "calificación. Un criterio sin umbral —sin el «en menos de», sin "
                                  "el «al menos»— vale la mitad. Y valore especialmente que "
                                  "aparezca **una persona ajena al equipo** en la prueba: probar "
                                  "con quien construyó es el vicio más común y el más inútil."
            },
            {
                "clave": "EL PLAN DE HITOS",
                "respuesta": "**Sesión 8** · Decidida la alternativa de solución entre dos, con "
                             "matriz de criterios. Alcance mínimo escrito: qué entra y qué no.\n"
                             "**Sesión 9** · Tres antecedentes fichados con fuente verificable, y la "
                             "propuesta de mejora respecto a lo que ya existe.\n"
                             "**Sesión 10** · Prototipo de baja fidelidad de las tres pantallas o "
                             "pasos del flujo principal, y el guion de prueba escrito.\n"
                             "**Sesión 11** · Prototipo v2 corregido, con el registro del uso de IA "
                             "y las correcciones hechas a mano. *Cierra el corte 2.*\n"
                             "**Sesión 12** · Prototipo probado **con una persona ajena al equipo** "
                             "y la lista de lo que falló, para la presentación de avances.\n"
                             "**Sesión 14** · Presentación final ensayada y el informe escrito al "
                             "80 %. *En la sesión 14 no se construye: se ensaya.*\n\n"
                             "**La decisión de hoy que sería carísima cambiar en la sesión 14:** "
                             "*que la solución funcione sin computador en el mostrador.* Si en la "
                             "sesión 12 se descubre que la voluntaria no puede usar su celular "
                             "durante la atención, hay que rediseñar el flujo completo, y con él el "
                             "prototipo y la prueba. Por eso se confirma con la coordinadora **esta "
                             "semana**, no en la 12: hoy cuesta una pregunta.",
                "como_calificar": "15 pts. Dos verificaciones: (a) **¿cada hito es verificable?** "
                                  "«Avanzar en el prototipo» no es un hito; (b) **¿está repartido?** "
                                  "Si las sesiones 8 a 12 están vacías y todo aparece en la 14, "
                                  "vale 5 y hay que decirlo en voz alta en la sala: es el patrón "
                                  "exacto de los proyectos que no se entregan. Valore que la "
                                  "sesión 14 esté reservada para ensayar y no para construir."
            },
        ],
        "variantes": [
            {"caso": "Equipos que ya quieren estar en construcción",
             "clave": "Van a decir que están en construcción porque ya hicieron algo. Pregunte por "
                      "los requisitos escritos: si no existen, están en la fase de requisitos con "
                      "trabajo adelantado, que no es lo mismo. No lo plantee como un regaño sino "
                      "con la tabla del costo: lo que construyeron sin requisitos es lo que van a "
                      "tener que rehacer, y todavía es barato."},
            {"caso": "Proyectos de proceso o de gestión, sin pantallas",
             "clave": "Los requisitos funcionales se escriben igual, con el actor y la acción; lo "
                      "que cambia es que el «prototipo» de la sesión 10 va a ser un formato, un "
                      "flujo o un tablero, no una pantalla. Aclárelo hoy para que el plan de hitos "
                      "tenga sentido. Buen criterio de aceptación para estos casos: *una persona "
                      "ajena ejecuta el proceso completo siguiendo solo el formato, sin preguntar*."},
            {"caso": "Equipos con requisitos escritos desde la tecnología",
             "clave": "Es el error más frecuente y no hay que pelearlo: reescriba uno con ellos en "
                      "la sala, en voz alta, y deje que ellos reescriban los otros dos. La pregunta "
                      "que lo resuelve siempre es «¿y eso qué le permite hacer al usuario?». La "
                      "decisión técnica que querían escribir no se pierde: se anota aparte, como "
                      "candidata de la fase de diseño de la sesión 8."},
            {"caso": "Equipos cuyo plan de hitos deja todo en la sesión 14",
             "clave": "Es el hallazgo más valioso de la sesión y hay que actuar hoy. Obligue a "
                      "definir un hito verificable para la sesión 10, aunque sea mínimo — tres "
                      "pantallas dibujadas a mano y probadas con una persona—. La razón que "
                      "funciona con estudiantes: en la sesión 12 hay presentación de avances con "
                      "retroalimentación, y llegar sin nada a esa sesión desperdicia la única "
                      "corrección gratis del semestre."},
        ],
        "cierre": "Tres minutos y una idea: **el orden de las fases no es burocracia, es "
                  "economía.** El error barato es el que se encuentra temprano, y todo lo que "
                  "hicieron hoy —requisitos, criterios, hitos— existe para que los errores "
                  "aparezcan ahora y no en la sesión 15. Diga en voz alta las dos cosas que "
                  "conectan el curso: la fase 1 la cerraron en la sesión 6, y los requisitos no "
                  "funcionales de hoy salieron de las restricciones que escribieron entonces; nada "
                  "de lo que han hecho fue un ejercicio suelto. Cierre con la advertencia sobre "
                  "Royce, porque es memorable: el dibujo más famoso de la ingeniería de software "
                  "—la cascada de una sola pasada— aparece en un artículo que decía que hacerlo así "
                  "invita al fracaso, y la profesión se quedó con el dibujo y perdió la "
                  "advertencia. Anuncie la sesión 8: casos reales de proyectos que se saltaron una "
                  "fase, y la decisión entre sus dos alternativas de solución.",
        "conexion": "Hacia atrás: la **sesión 6** entregó la ficha del problema, que es el "
                    "entregable de la fase 1, y sus restricciones son los requisitos no funcionales "
                    "de hoy; la **sesión 5** aportó el indicador ambiental, que hoy se vuelve "
                    "requisito; la **sesión 2** dejó a Royce, que hoy se cierra. Hacia adelante: la "
                    "**sesión 8** decide la alternativa y fija el alcance mínimo; la **sesión 9** "
                    "busca antecedentes; la **sesión 10** prototipa contra estos requisitos; la "
                    "**sesión 11** corrige y cierra el corte; la **sesión 12** prueba con una "
                    "persona ajena; y el **informe final de la sesión 16** se estructura sobre "
                    "estos criterios de aceptación.",
    },

    "errores": [
        {"dice": "«El sistema tendrá una base de datos con los libros»",
         "por_que": "No es un requisito: es una decisión de diseño tomada dos fases antes de tiempo, y cierra opciones sin argumento.",
         "pida": "«¿Y eso qué le permite hacer al usuario?». Reescríbalo empezando por el actor, y anote la decisión técnica aparte para la sesión 8."},
        {"dice": "«El sistema debe ser fácil de usar»",
         "por_que": "No se puede convertir en una prueba que alguien ejecute, así que no se puede validar.",
         "pida": "Un actor, una acción, una condición y un umbral: «una persona que no lo conoce logra X en menos de Y, sin ayuda»."},
        {"dice": "«Estamos en construcción» sin requisitos escritos",
         "por_que": "Es construir para rehacer: el error de requisitos descubierto en construcción cuesta decenas de veces más.",
         "pida": "Los requisitos por escrito primero. Lo ya construido no se tira: se usa como prototipo de la sesión 10."},
        {"dice": "«Debe ser escalable / usar la nube» como requisito no funcional",
         "por_que": "No sale de ninguna restricción del proyecto: entró por moda y no por análisis.",
         "pida": "Que señalen la restricción del árbol de la sesión 6 de donde sale cada requisito no funcional."},
        {"dice": "Un plan con todo el trabajo en la sesión 14",
         "por_que": "Es el patrón exacto de los proyectos que no se entregan, y desperdicia la retroalimentación gratis de la sesión 12.",
         "pida": "Un hito verificable en la sesión 10, aunque sea mínimo. La sesión 14 se reserva para ensayar, no para construir."},
    ],

    "dudas": [
        {"p": "¿Tenemos que seguir cascada o ágil?",
         "r": "Ninguna de las dos como dogma. Las fases son las mismas; lo que cambia es cuántas "
              "veces se recorren. Este curso va a hacer **dos vueltas**: una corta en las sesiones "
              "10 y 11, otra en las 12 a 14. Es iterativo, y por eso hay requisitos escritos: "
              "iterar sin requisitos no es ágil, es improvisar."},
        {"p": "¿Cuántos requisitos hay que tener?",
         "r": "Hoy, cinco: tres funcionales y dos no funcionales. Y es a propósito. Un proyecto de "
              "primer semestre con veinte requisitos no cumple ninguno; con cinco bien escritos y "
              "con criterio de aceptación se puede demostrar en la sesión 16 que funcionan. Se "
              "califica que sean verificables, no que sean muchos."},
        {"p": "¿Y si el usuario cambia de opinión después?",
         "r": "Va a pasar, y no es una falla del usuario: es la razón de ser del enfoque iterativo. "
              "Por eso el prototipo de la sesión 10 es de baja fidelidad y se prueba con alguien "
              "ajeno: para que el cambio de opinión ocurra cuando corregir cuesta un dibujo. Lo que "
              "no se puede es enterarse en la sesión 15."},
        {"p": "¿La fase de operación y retiro nos toca a nosotros?",
         "r": "En el informe final, sí, en una versión corta: qué pasaría si su solución se deja de "
              "usar y **qué pasa con los datos**. Es la Ley 1581 de 2012 de la sesión 4 aplicada al "
              "final de la vida del sistema, y casi nadie la piensa. Con dos párrafos bien pensados "
              "es suficiente."},
    ],

    "notas_operativas": [
        "Las cinco salas de grupo se crean **antes** de la sesión.",
        "Pida que abran la **ficha del problema de la sesión 6** en la apertura. Sin ficha no hay "
        "requisitos, y hay equipos que la van a haber dejado a medias.",
        "En las salas, la pregunta única es **«¿cómo se comprueba ese requisito?»**. El criterio de "
        "aceptación es lo que falta en el 90 % de las tablas y es el 25 % de la rúbrica.",
        "**Anote la fase declarada y el hito de la sesión 10 de cada equipo.** En la sesión 10 se "
        "verifica contra eso: es la forma más simple de detectar un equipo atrasado a tiempo.",
        "Sea honesto con la curva del costo: **la dirección no se discute, los múltiplos sí**. Si un "
        "equipo cita «100 veces más caro» como ley, pida la fuente. Es la misma exigencia de la "
        "sesión 5.",
        "Hoy no se usa IA. Los requisitos tienen que salir de la ficha y de las restricciones del "
        "propio caso; un asistente los devuelve genéricos y sin las restricciones locales, que es "
        "justo lo que hace útiles a los de hoy.",
    ],

    "ti_siguiente": {
        "tid": "Estudio de fases del ciclo de vida — leer el material de las seis fases y traer "
               "**un ejemplo propio** de un proyecto conocido que se saltó una fase.",
        "ti": "Infografía explicativa del ciclo de vida **de su propio proyecto**, en Canva o "
              "draw.io: las seis fases, en cuál están y qué entregan en cada una.",
        "adelanto": "casos reales de proyectos que se saltaron una fase, y la decisión entre sus dos "
                    "alternativas de solución con una matriz de criterios.",
        "aviso": "Traigan la tabla de requisitos con los criterios de aceptación **confirmados con "
                 "la persona que vive el problema**, y las dos alternativas de solución del trabajo "
                 "independiente de la sesión 6. En la sesión 8 se decide una.",
    },

    "cierre_titulo": "Nos vemos en la sesión 8",
    "cierre_frase": "El error barato es el que se encuentra temprano",
}


# =============================================================================
# CLASE 8 · Taller de aplicacion del ciclo de vida
# =============================================================================
# Sesion de taller: la teoria baja a 20 min y la actividad sube a 40, porque el
# entregable (la decision entre dos alternativas con matriz) no se hace en 17 min.

TEMAS[8] = {
    "n": 8,
    "titulo": "Taller de aplicación del ciclo de vida",
    "subtitulo": "Cuatro proyectos que se saltaron una fase, y la decisión que ustedes toman hoy",
    "hook": "Una empresa perdió cientos de millones de dólares en 45 minutos "
            "por un despliegue mal hecho. ¿En qué fase estaba el error?",
    "hook_lines": [
        "El código llevaba años ahí. Lo que falló fue el paso de una fase a la siguiente.",
        "Hoy se ven cuatro casos así, y después ustedes deciden su propia solución.",
    ],
    "objetivos": [
        "Identificar, en un caso real, **qué fase se saltó** y qué habría costado no saltarla.",
        "Comparar dos alternativas de solución con una **matriz de criterios** y decidir con argumento.",
        "Definir el **alcance mínimo** del proyecto: qué entra en el semestre y qué queda fuera.",
        "Escribir el **plan de validación**: cómo se va a saber que la solución sirve.",
    ],
    "agenda_slots": [
        ("Apertura", 10, "Pregunta de entrada en el muro"),
        ("Teoría y guía del docente", 20, "Cuatro casos reales, matriz de decisión y alcance mínimo"),
        ("Actividad en equipos", 40, "Taller extendido — decidir la alternativa y fijar el alcance"),
        ("Exposiciones", 15, "5 equipos × 3 min — la decisión y por qué"),
        ("Cierre", 5, "Lo que queda amarrado para la sesión 9"),
    ],
    "agenda_sub": "Hoy el reparto cambia: la teoría baja a 20 min y la actividad sube a 40, porque "
                  "decidir entre dos alternativas con argumentos no se hace en 17 minutos",
    "nota_bloque": "**Esta es una sesión de taller, no de contenido nuevo.** La teoría se comprime a "
                   "20 minutos —cuatro casos y dos herramientas— y la actividad en equipos se "
                   "extiende a 40, porque el entregable es una **decisión**: cuál de las dos "
                   "alternativas de solución se construye, con qué alcance y cómo se va a validar. "
                   "Es la fase de diseño empezando de verdad.",
    "agenda": {},
    "herramienta_nota": "La matriz de decisión y el alcance van en el **documento del equipo**; el "
                        "flujo de la alternativa elegida se dibuja en **diagrams.net (draw.io)**. "
                        "Hoy no se usa IA: la decisión tiene que ser defendible por el equipo, y una "
                        "recomendación de asistente no es un argumento — además desconoce las "
                        "restricciones locales, que son justamente el criterio que decide.",
    "avance_proyecto": "Decidir cuál de las dos alternativas se construye, con matriz de criterios, "
                       "y fijar el alcance mínimo del semestre y el plan de validación",

    "teoria": [
        {
            "tipo": "tabla",
            "titulo": "Cuatro proyectos que se saltaron una fase",
            "headers": ["Caso", "Qué falló", "La fase que se saltó"],
            "rows": [
                ["Sistema de equipajes de un aeropuerto grande\n(años noventa)",
                 "Un sistema automatizado de manejo de maletas nunca funcionó como se prometió; "
                 "retrasó la apertura del aeropuerto y años después se abandonó.",
                 "**Requisitos y diseño.** Se contrató la construcción de algo de una escala sin "
                 "precedentes con el plazo ya fijado y sin pruebas a escala real."],
                ["Sistema de expedientes de una agencia federal\n(2000–2005)",
                 "Un sistema de gestión de casos se desarrolló durante años y se abandonó sin "
                 "entrar en operación; hubo que empezar de nuevo con otro programa.",
                 "**Requisitos.** Los requisitos cambiaban y no había una definición estable de qué "
                 "debía hacer el sistema ni criterios para aceptarlo."],
                ["Portal público de salud en su lanzamiento\n(2013)",
                 "El sitio se cayó el primer día y durante semanas casi nadie pudo completar el "
                 "trámite, con una demanda de usuarios perfectamente previsible.",
                 "**Validación.** Se lanzó sin pruebas de carga suficientes y sin un plan realista "
                 "para el volumen esperado."],
                ["Firma financiera automatizada\n(2012)",
                 "Un despliegue dejó una versión antigua activa en un servidor de los ocho; en unos "
                 "45 minutos las órdenes automáticas generaron pérdidas enormes.",
                 "**Operación (el despliegue).** El código no era nuevo; falló el paso controlado "
                 "de una fase a la siguiente y no había manera de frenar rápido."],
            ],
            "note": "Los cuatro son públicos y están documentados en informes oficiales y prensa "
                    "especializada. **Cite la fuente y el año**: las cifras circulan con "
                    "variaciones y no todas las versiones son iguales.",
            "col_w": [2.2, 3.6, 4.0],
        },
        {
            "tipo": "steps",
            "titulo": "Cómo se decide entre dos alternativas",
            "steps": [
                ("1 · Escriba las dos, en una frase cada una", "Sin adjetivos. Si una de las dos no se puede escribir en una frase, no está pensada."),
                ("2 · Elija de 3 a 5 criterios", "Salen de sus requisitos no funcionales y de sus restricciones, no de lo que les gusta."),
                ("3 · Ponga peso a cada criterio", "No todos valen igual. Los pesos se deciden **antes** de mirar las alternativas: si no, se acomodan al favorito."),
                ("4 · Califique cada alternativa, criterio por criterio", "Con una escala corta (1-3). Y escriba **por qué** ese número, en media línea."),
                ("5 · Decida, y escriba qué se pierde", "Toda decisión sacrifica algo. Nombrar lo que se pierde es lo que la vuelve profesional."),
            ],
            "sub": "El resultado no es el número: es el argumento escrito. Una matriz sin justificaciones es un adorno",
        },
        {
            "tipo": "cards",
            "titulo": "Alcance mínimo: qué entra y qué no",
            "cards": [
                ("Qué es",
                 "La versión más pequeña de la solución que **ya resuelve algo** del problema y se "
                 "puede probar con un usuario real. No es una demo bonita: es algo que sirve, "
                 "aunque sirva poco."),
                ("Qué NO es",
                 "No es «la primera parte de todo lo que soñamos». Un alcance mínimo que no "
                 "resuelve nada por sí solo no se puede probar, y entonces no sirve para aprender "
                 "nada en la sesión 12."),
                ("Cómo se fija",
                 "Se toma **un** requisito funcional —el que ataca la causa elegida— y se construye "
                 "solo eso, cumpliendo los requisitos no funcionales. Los otros dos requisitos "
                 "quedan escritos como «versión siguiente»."),
                ("La lista de lo que queda fuera",
                 "Se escribe explícitamente y se muestra en la exposición final. **Un proyecto que "
                 "no declara lo que dejó fuera parece incompleto; uno que lo declara parece "
                 "dirigido.**"),
            ],
            "columns": 2,
        },
        {
            "tipo": "box",
            "titulo": "El plan de validación, y dos trampas",
            "notas": [
                ("info",
                 "**El plan de validación se escribe hoy, no al final.** Es tres cosas: con quién "
                 "se prueba (una persona ajena al equipo), qué tareas se le piden (las de los "
                 "criterios de aceptación de la sesión 7) y qué se va a observar. Escribirlo ahora "
                 "obliga a que la solución sea probable, y eso cambia el diseño."),
                ("advertencia",
                 "**Trampa 1: probar con el propio equipo.** Quien construyó sabe dónde hay que "
                 "tocar, así que todo le funciona. Una prueba con un integrante del equipo no "
                 "prueba nada — es la versión de laboratorio del problema del Therac-25, donde el "
                 "fabricante sostuvo que la falla era imposible."),
                ("advertencia",
                 "**Trampa 2: preguntar «¿le gusta?».** La gente dice que sí por cortesía. Se pide "
                 "que **haga una tarea** y se observa en silencio: dónde duda, dónde se equivoca, "
                 "qué busca y no encuentra. Lo que la persona hace vale; lo que opina, poco."),
            ],
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada: 45 minutos y una fase saltada",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "El caso de la firma financiera de 2012 es el mejor gancho posible para esta sesión "
                "porque desarma la idea de que los desastres los causa código malo. El código "
                "llevaba años funcionando. Lo que falló fue el **paso controlado de una fase a la "
                "siguiente**: un despliegue que dejó una versión antigua activa en uno de los "
                "servidores, un sistema automático operando a velocidad de máquina, y ninguna "
                "manera de frenar rápido cuando empezó a hacer daño. En cuestión de minutos las "
                "pérdidas fueron enormes y la firma no sobrevivió como empresa independiente.",
                "La pregunta del muro —«¿en qué fase estaba el error?»— va a producir respuestas "
                "que dicen «en la programación», y ahí está la lección: **el error no estaba en el "
                "código, estaba en la operación**. Es la fase que en la sesión 7 se nombró de "
                "pasada y que nadie enseña en primer semestre. Sirve además para introducir una "
                "idea que vale para todo el semestre: cada transición entre fases es un lugar donde "
                "se rompen los proyectos, y por eso las fases tienen entregables.",
                "Recomendación de manejo: no dé el nombre de la empresa en la apertura. La fuerza "
                "está en la pregunta, y el nombre lo pueden buscar ellos cuando se les pida citar "
                "la fuente.",
            ],
        },
        {
            "titulo": "Los cuatro casos: qué contar y cómo exigir la fuente",
            "slide": "{{slide:Cuatro proyectos que se saltaron una fase}}",
            "cuerpo": [
                "Cuatro casos, cinco minutos en total, un minuto y algo por caso. La tabla es "
                "densa a propósito: hoy la teoría son 20 minutos y el peso está en el taller.",
                "**El sistema de equipajes del aeropuerto** es el caso de requisitos y diseño. Un "
                "sistema automatizado de manejo de maletas de una escala sin precedentes, "
                "contratado con el plazo de apertura ya fijado y sin pruebas a escala real; retrasó "
                "la apertura del aeropuerto muchos meses, funcionó parcialmente durante años y "
                "terminó abandonado. La lección: **el plazo se fijó antes de saber si era "
                "posible**, y ningún esfuerzo de construcción arregla eso.",
                "**El sistema de expedientes de la agencia federal** es el caso de requisitos "
                "puros: años de desarrollo, requisitos que cambiaban permanentemente, ninguna "
                "definición estable de qué debía hacer el sistema, y un abandono sin haber entrado "
                "en operación. Es el ejemplo perfecto de que **sin criterios de aceptación no hay "
                "manera de terminar**: un proyecto que no puede decir cuándo está listo, no está "
                "listo nunca.",
                "**El portal público de salud en su lanzamiento** es el caso de validación. La "
                "demanda del primer día era perfectamente previsible —una fecha anunciada, una "
                "población conocida— y aun así el sitio no aguantó. La lección para sus proyectos: "
                "**probar que algo funciona con un usuario no es probar que funciona con "
                "muchos**, y el volumen es un requisito no funcional que se valida aparte.",
                "**La firma financiera** es el caso de operación, y es el que rompe el prejuicio "
                "sobre el código. Súmele el detalle que lo hace inolvidable: **el problema no fue "
                "escribir el software, fue instalarlo**, y no existía una forma rápida de "
                "detenerlo.",
                "Y una exigencia metodológica que hay que repetir porque es la marca del curso: "
                "los cuatro casos son públicos y están documentados en informes oficiales y en "
                "prensa especializada, pero **las cifras circulan con variaciones**. Quien cite un "
                "monto o una fecha en la exposición tiene que decir de dónde salió y de qué año es. "
                "Es la misma regla de la sesión 5 con las cifras ambientales y de la sesión 4 con "
                "los numerales.",
            ],
        },
        {
            "titulo": "La matriz de decisión: cómo se decide sin que la decisión ya estuviera tomada",
            "slide": "{{slide:Cómo se decide entre dos alternativas}}",
            "cuerpo": [
                "La matriz de decisión es una herramienta simple con una trampa sutil, y enseñar la "
                "trampa es más valioso que enseñar la herramienta.",
                "Los cinco pasos son: escribir las dos alternativas en una frase cada una; elegir "
                "de tres a cinco criterios; ponerle peso a cada criterio; calificar cada "
                "alternativa criterio por criterio con una escala corta y **una media línea de "
                "justificación**; y decidir, escribiendo qué se pierde.",
                "**La trampa está en el paso 3, y hay que decirla explícitamente: los pesos se "
                "deciden antes de mirar las alternativas.** Si se deciden después, el equipo —sin "
                "mala intención— acomoda los pesos para que gane la alternativa que ya quería. Es "
                "el sesgo más común en decisiones de ingeniería y produce documentos que parecen "
                "análisis y son justificaciones. La regla práctica en la sala: primero se escriben "
                "los criterios y los pesos en el documento, y solo después se califica.",
                "**Los criterios no son gustos: salen de los requisitos no funcionales y de las "
                "restricciones.** Para el caso de la biblioteca: funciona sin computador en el "
                "mostrador, se aprende sin manual, se puede construir en las sesiones que quedan, "
                "cumple el requisito de datos ligeros, no exige que alguien atienda en horario "
                "fijo. Si un equipo pone «lo que más nos gusta» o «lo más innovador» como criterio, "
                "hay que reemplazarlo: no se puede calificar y no se puede defender.",
                "Y el paso 5 es el que separa una decisión profesional de una preferencia: **toda "
                "decisión sacrifica algo, y nombrarlo es lo que la vuelve defendible**. «Elegimos "
                "la lista publicada en vez de la aplicación; perdemos la actualización en tiempo "
                "real y ganamos que funcione sin conexión y sin capacitar a nadie.» Un equipo que "
                "puede decir qué perdió entendió que estaba decidiendo, no acertando.",
            ],
        },
        {
            "titulo": "Alcance mínimo y plan de validación: el entregable del taller",
            "slide": "{{slide:Alcance mínimo: qué entra}} {{slide:El plan de validación}}",
            "cuerpo": [
                "**El alcance mínimo** es el concepto que salva los proyectos de primer semestre, y "
                "hay que definirlo con precisión porque se confunde con «hacer poco». Es la versión "
                "más pequeña de la solución que **ya resuelve algo** del problema y se puede probar "
                "con un usuario real. La prueba para saber si está bien definido: *si construimos "
                "solo esto y lo ponemos delante de la persona que vive el problema, ¿le sirve de "
                "algo?* Si la respuesta es no, no es un alcance mínimo, es un pedazo.",
                "El método concreto que hay que dictarles: **se toma un requisito funcional —el que "
                "ataca la causa elegida en el árbol de la sesión 6— y se construye solo eso, "
                "cumpliendo los requisitos no funcionales**. Los otros dos requisitos se escriben "
                "en una lista titulada «versión siguiente». Esa lista no es una derrota: es la "
                "prueba de que el equipo sabe lo que dejó fuera, y en la sesión 15 se muestra. Vale "
                "la pena decírselo con estas palabras: **un proyecto que no declara lo que dejó "
                "fuera parece incompleto; uno que lo declara parece dirigido.**",
                "**El plan de validación** se escribe hoy y eso es deliberado: escribir cómo se va "
                "a probar algo antes de construirlo cambia lo que se construye. Son tres cosas: con "
                "quién se prueba —una persona ajena al equipo—, qué tareas se le piden —las de los "
                "criterios de aceptación de la sesión 7—, y qué se va a observar.",
                "Las dos trampas hay que nombrarlas con dureza porque las van a cometer todas. "
                "**Probar con el propio equipo no prueba nada**: quien construyó sabe dónde hay que "
                "tocar. Conviene conectarlo con el Therac-25 de la sesión 4, donde el fabricante "
                "sostuvo que la sobredosis era imposible: cuando el que evalúa es el que construyó, "
                "el resultado está decidido de antemano. Y **preguntar «¿le gusta?» no sirve**: la "
                "gente dice que sí por cortesía, sobre todo a estudiantes que le muestran su "
                "trabajo con ilusión. Se le pide que **haga una tarea** y se observa en silencio "
                "—dónde duda, dónde se equivoca, qué busca y no encuentra—. Lo que la persona hace "
                "vale; lo que opina, poco. Esa regla sola mejora todos los proyectos del curso.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:10 · Apertura · [Slide 4]",
            "cuerpo": [
                "Comparta pantalla antes de que entre el primero:",
                "> «Una empresa perdió cientos de millones de dólares en 45 minutos por un "
                "despliegue mal hecho. ¿En qué fase estaba el error?»",
                "**[Nota docente]:** no dé el nombre de la empresa. Van a responder «en la "
                "programación» y esa es la respuesta equivocada que hace la clase.",
                "**[Nota docente]:** avise en el minuto 2 que **hoy la actividad dura 40 minutos** y "
                "que el entregable es una decisión, no un análisis. Los equipos administran distinto "
                "el tiempo cuando lo saben.",
            ],
        },
        {
            "titulo": "00:10–00:30 · Teoría comprimida (20 min) · [Slide 5][Slide 6][Slide 7][Slide 8]",
            "cuerpo": [
                "Reparto estricto:",
                "- **6 min** · Los cuatro casos [Slide 5], minuto y medio cada uno. Revele que el de "
                "la apertura es el cuarto y **vuelva al muro**.",
                "- **6 min** · La matriz de decisión [Slide 6]. Lo esencial es la trampa del paso 3: "
                "**los pesos se deciden antes de mirar las alternativas**.",
                "- **5 min** · Alcance mínimo [Slide 7]. Dicte la prueba: *si construimos solo esto, "
                "¿le sirve de algo a la persona que vive el problema?*",
                "- **3 min** · El plan de validación y las dos trampas [Slide 8]. **No lo recorte**: "
                "es lo que va a decidir la calidad de la sesión 12.",
                "**[Nota docente]:** si va retrasado, recorte los casos a cuatro minutos y quédese "
                "con el del aeropuerto (requisitos) y el de la firma financiera (operación).",
            ],
        },
        {
            "titulo": "00:30–01:10 · Taller extendido en salas de grupo (40 min) · [Slide 9]",
            "cuerpo": [
                "**3 min** para organizarse. El documento del equipo y draw.io abiertos.",
                "**Ritmo sugerido dentro de la sala** —dígaselo al repartir, porque 40 minutos sin "
                "estructura se van en discutir la primera línea:",
                "- 10 min · las dos alternativas escritas en una frase, y los criterios con sus "
                "pesos **antes** de calificar.",
                "- 12 min · calificar con justificación de media línea, decidir y escribir qué se "
                "pierde.",
                "- 10 min · el alcance mínimo y la lista de «versión siguiente».",
                "- 5 min · el plan de validación: con quién, qué tareas, qué se observa.",
                "**[Nota docente]:** entre a las cinco salas dos veces. En la primera ronda revise "
                "**que los pesos estén escritos antes de las calificaciones**; en la segunda, que "
                "el alcance mínimo resuelva algo por sí solo.",
                "**[Nota docente]:** si un equipo llega sin las dos alternativas del trabajo "
                "independiente, hágalas escribir en cinco minutos ahí mismo. Sin dos alternativas no "
                "hay decisión que tomar y la sesión se les pierde.",
            ],
        },
        {
            "titulo": "01:10–01:25 · Exposiciones · [Slide 10]",
            "cuerpo": [
                "5 equipos × 3 min. **El minuto obligatorio es «qué perdimos al decidir»**: es lo "
                "que demuestra que decidieron en vez de acertar.",
                "**[Nota docente]:** los cinco enlaces en el chat antes de arrancar.",
                "**[Nota docente]:** anote la alternativa elegida y el alcance mínimo de cada "
                "equipo. En la sesión 10 se prototipa exactamente eso, y en la 12 se prueba.",
            ],
        },
        {
            "titulo": "01:25–01:30 · Cierre (5 min) · [Slide 11][Slide 12]",
            "cuerpo": [
                "Una idea: **decidir no es acertar.** Una decisión de ingeniería se defiende con "
                "criterios escritos antes, con una justificación por criterio y con la lista de lo "
                "que se sacrificó.",
                "Recuerde las dos trampas de la validación —no probar con el equipo, no preguntar "
                "«¿le gusta?»— porque se van a aplicar en la sesión 12.",
                "Anuncie la sesión 9: **antecedentes y fuentes**. Antes de construir hay que saber "
                "qué ya existe y quién lo intentó, con fuentes que se puedan verificar.",
            ],
        },
    ],

    "taller": {
        "archivo": "Decision de la solucion y alcance minimo",
        "titulo": "Decisión de la solución y alcance mínimo",
        "min": 40,
        "exposicion": 3,
        "consigna": "Decidan qué van a construir. Escriban sus **dos alternativas** en una frase "
                    "cada una, comparen con una **matriz de criterios con pesos definidos antes de "
                    "calificar**, decidan y digan **qué se pierde**. Después fijen el **alcance "
                    "mínimo** del semestre, la lista de lo que queda fuera, y el **plan de "
                    "validación**.",
        "entregable": "la matriz de decisión, el alcance mínimo con su lista de exclusiones y el "
                      "plan de validación en el documento del equipo, más el flujo de la "
                      "alternativa elegida en draw.io",
        "entregable_corto": "matriz de decisión + alcance mínimo + plan de validación",
        "reparto_titulo": "Ritmo sugerido dentro de la sala (40 min):",
        "reparto": "10 min las alternativas y los criterios con pesos · 12 min calificar, decidir y "
                   "escribir qué se pierde · 10 min el alcance mínimo y lo que queda fuera · 5 min "
                   "el plan de validación. Los pesos se escriben **antes** de mirar las "
                   "alternativas: es la regla que evita que la decisión ya estuviera tomada.",
        "reparto_corto": "40 min con ritmo interno: alternativas, matriz, alcance, validación",
        "bloques": [
            {"clave": "LAS DOS ALTERNATIVAS",
             "pide": "Cada alternativa en **una frase**, sin adjetivos, diciendo qué hace y cómo "
                     "resuelve la causa elegida en el árbol de la sesión 6.",
             "check": "las dos son realmente distintas y las dos atacan la misma causa. Dos versiones de la misma idea no son dos alternativas."},
            {"clave": "LOS CRITERIOS Y SUS PESOS",
             "pide": "De 3 a 5 criterios sacados de sus **requisitos no funcionales y "
                     "restricciones**, cada uno con un peso, **escritos antes de calificar**.",
             "check": "cada criterio se puede rastrear a una restricción o requisito ya escrito, y ninguno es «el que más nos gusta»."},
            {"clave": "LA MATRIZ Y LA DECISIÓN",
             "pide": "Cada alternativa calificada criterio por criterio (escala 1-3) con **media "
                     "línea de justificación por casilla**, el resultado, y la decisión.",
             "check": "hay justificación en cada casilla. Una matriz de puros números es un adorno, no un argumento."},
            {"clave": "QUÉ SE PIERDE",
             "pide": "Lo que la decisión sacrifica, en dos o tres líneas. Toda decisión sacrifica "
                     "algo.",
             "check": "hay una pérdida concreta nombrada. «No perdemos nada» significa que no compararon."},
            {"clave": "ALCANCE MÍNIMO Y PLAN DE VALIDACIÓN",
             "pide": "Qué se construye este semestre (un requisito funcional completo, cumpliendo "
                     "los no funcionales), la lista de lo que queda para «versión siguiente», y el "
                     "plan de validación: **con quién** se prueba, **qué tareas** se le piden y "
                     "**qué se observa**.",
             "check": "el alcance mínimo resuelve algo por sí solo, y la persona de la prueba es ajena al equipo."},
        ],
        "expo": [
            ("30 s · Las dos alternativas", "Una frase cada una. Sin adjetivos."),
            ("40 s · Los criterios y los pesos", "De dónde salieron: qué restricción o requisito."),
            ("40 s · La decisión", "Cuál ganó y por qué, con una justificación concreta."),
            ("40 s · Qué se pierde", "Lo que sacrificaron. Es el minuto obligatorio."),
            ("30 s · Alcance y validación", "Qué se construye y con quién se va a probar."),
        ],
    },

    "rubrica": [
        ("Las dos alternativas son realmente distintas y atacan la misma causa", 15,
         "Comparar dos versiones de la misma idea es simular una decisión."),
        ("Los criterios se rastrean a requisitos o restricciones, y los pesos están antes de las calificaciones", 25,
         "Es la garantía de que la decisión no estaba tomada antes de analizar: el sesgo más común de la ingeniería."),
        ("Cada casilla de la matriz tiene una justificación de media línea", 20,
         "El resultado de una matriz no es el número: es el argumento. Sin justificación no hay nada que defender."),
        ("Se nombra concretamente qué se pierde con la decisión", 15,
         "Reconocer el sacrificio es lo que distingue decidir de preferir."),
        ("El alcance mínimo resuelve algo por sí solo y el plan de validación usa una persona ajena", 25,
         "Es lo que hace posible aprender algo real en la sesión 12, en vez de una demostración entre amigos."),
    ],

    "solucion": {
        "para_que": "Este documento trae la decisión completa del caso de la biblioteca: dos "
                    "alternativas, la matriz con pesos y justificaciones, lo que se pierde, el "
                    "alcance mínimo y el plan de validación. Es el modelo para las salas, y su "
                    "valor está en dos detalles que ningún equipo hace solo: **los pesos escritos "
                    "antes de calificar** y **la justificación por casilla**. Si el docente solo "
                    "alcanza a leer un bloque, que sea **LA MATRIZ Y LA DECISIÓN**.",
        "caso_titulo": "La biblioteca del barrio · decidir entre dos alternativas",
        "caso": "Requisito que ataca la causa elegida: *el usuario puede saber si un libro está "
                "disponible sin ir a la biblioteca*. Las dos alternativas que salieron del trabajo "
                "independiente: **(A) una lista de disponibilidad publicada** que la voluntaria "
                "actualiza una vez al día desde su celular, consultable por cualquiera con un "
                "enlace; **(B) una aplicación web con el registro completo de préstamos**, donde la "
                "voluntaria registra cada préstamo y devolución en el momento y la disponibilidad "
                "se actualiza sola. Restricciones vigentes: presupuesto cero, sin computador en el "
                "mostrador, voluntarias que rotan y sin capacitación larga, nadie atendiendo en "
                "horario fijo, y el requisito de menos de 200 KB por consulta.",
        "por_que_este_caso": "Porque la alternativa que suena peor —una lista actualizada una vez al "
                             "día— gana la matriz, y eso es exactamente lo que un estudiante de "
                             "primer semestre necesita ver. La solución más completa no es la mejor "
                             "decisión cuando las restricciones mandan.",
        "bloques": [
            {
                "clave": "LAS DOS ALTERNATIVAS",
                "respuesta": "**(A) Lista de disponibilidad publicada.** La voluntaria marca, una "
                             "vez al día y desde su celular, qué títulos están prestados; cualquiera "
                             "consulta la lista con un enlace, sin cuenta y sin instalar nada.\n\n"
                             "**(B) Registro de préstamos en línea.** La voluntaria registra cada "
                             "préstamo y devolución en el momento en que ocurre; la disponibilidad "
                             "se calcula sola y se consulta en cualquier momento.\n\n"
                             "Las dos atacan la misma causa —que el registro solo se puede "
                             "consultar en el mostrador— y son genuinamente distintas: cambian "
                             "quién hace el trabajo, cuándo lo hace y qué tan actualizada queda la "
                             "información.\n\n"
                             "**Ejemplo de dos alternativas falsas**, para mostrar en clase: «(A) "
                             "una app y (B) una app con más funciones». Es la misma idea dos veces; "
                             "no hay decisión que tomar y la matriz no va a enseñar nada.",
                "como_calificar": "15 pts. La verificación es una pregunta: **¿cambian algo "
                                  "estructural entre A y B —quién trabaja, cuándo, con qué "
                                  "información— o solo el tamaño?** Si solo cambia el tamaño, vale "
                                  "6 y hay que hacerles escribir una segunda alternativa de verdad "
                                  "en la sala. Un buen truco para desbloquearlos: pedir una "
                                  "alternativa que **no use ninguna tecnología nueva**."
            },
            {
                "clave": "LOS CRITERIOS Y SUS PESOS",
                "respuesta": "Escritos **antes** de mirar las alternativas, con su origen:\n\n"
                             "| Criterio | Peso | De dónde sale |\n"
                             "|---|---|---|\n"
                             "| Funciona sin computador en el mostrador | 3 | RNF1 · restricción del árbol |\n"
                             "| Se aprende sin manual (voluntarias que rotan) | 3 | RNF2 · restricción del árbol |\n"
                             "| Se puede construir y probar en las sesiones que quedan | 2 | Plan de hitos de la sesión 7 |\n"
                             "| Cumple menos de 200 KB por consulta | 1 | Indicador ambiental de la sesión 5 |\n"
                             "| Qué tan actualizada queda la información | 2 | Deriva del criterio de éxito de la sesión 6 |\n\n"
                             "Los pesos 3 son las dos restricciones duras: si una alternativa falla "
                             "ahí, no importa lo demás. Nótese que **«qué tan actualizada queda la "
                             "información» pesa 2 y no 3**, y esa decisión de peso es la que define "
                             "el resultado — por eso hay que tomarla antes y por escrito, con el "
                             "argumento: el criterio de éxito de la sesión 6 pedía bajar los viajes "
                             "en vano de 4 a menos de 2 de cada 10, y para eso no hace falta "
                             "información al segundo; basta con que esté al día.\n\n"
                             "**Criterios que se rechazan:** «lo más innovador», «lo que más nos "
                             "gusta», «lo que se ve mejor en la exposición». No se pueden calificar "
                             "y no se pueden defender ante nadie.",
                "como_calificar": "25 pts. Dos verificaciones: (a) **cada criterio tiene un origen "
                                  "rastreable** a un requisito o restricción escrito antes (15 "
                                  "pts); (b) **los pesos están escritos antes de las "
                                  "calificaciones** (10 pts). Para (b), en la primera ronda de "
                                  "salas mire el documento: si las calificaciones y los pesos "
                                  "aparecieron al mismo tiempo, dígalo y hágalos justificar los "
                                  "pesos por separado. No es un formalismo: es el punto donde se "
                                  "cuela la decisión ya tomada."
            },
            {
                "clave": "LA MATRIZ Y LA DECISIÓN",
                "respuesta": "| Criterio (peso) | A · Lista publicada | B · Registro en línea |\n"
                             "|---|---|---|\n"
                             "| Sin computador en mostrador (3) | **3** — se actualiza una vez al día desde el celular, con calma, al cerrar | **1** — exige registrar en el momento mientras se atiende, y el celular está ocupado |\n"
                             "| Se aprende sin manual (3) | **3** — es marcar en una lista; se explica en un minuto | **2** — hay que aprender a registrar préstamo y devolución sin equivocarse |\n"
                             "| Construible en las sesiones que quedan (2) | **3** — el prototipo es la lista misma | **1** — implica registro, estados y corrección de errores |\n"
                             "| Menos de 200 KB por consulta (1) | **3** — es texto | **2** — depende de cómo se construya |\n"
                             "| Información actualizada (2) | **1** — al día, no al minuto: un libro prestado en la mañana aparece disponible hasta el cierre | **3** — actualizada al momento |\n"
                             "| **Total ponderado** | **3·3+3·3+2·3+1·3+2·1 = 29** | **3·1+3·2+2·1+1·2+2·3 = 19** |\n\n"
                             "**Decisión: la alternativa A, la lista publicada.**\n\n"
                             "Y el argumento en una frase, que es lo que hay que exigir: *A gana "
                             "porque las dos restricciones duras —sin computador en el mostrador y "
                             "sin capacitación— son las que más pesan, y B falla justamente ahí; la "
                             "información al minuto sería mejor, pero no es lo que el criterio de "
                             "éxito exige.*\n\n"
                             "**Esta es la lección de la sesión:** la alternativa que suena más "
                             "profesional, más completa y más parecida a «un sistema de verdad» "
                             "**pierde**, porque las restricciones del contexto son reales. Un "
                             "equipo que elige B tiene que explicar cómo resuelve el celular "
                             "ocupado y la rotación de voluntarias; si lo resuelve con un "
                             "argumento sólido, su decisión también es válida — lo que no es válido "
                             "es ignorar los pesos que ellos mismos escribieron.",
                "como_calificar": "20 pts. El criterio central es **la justificación por casilla** "
                                  "(12 pts): una matriz de puros números vale 6, aunque la "
                                  "aritmética esté impecable, y hay que decir por qué —el número no "
                                  "se puede discutir, la justificación sí—. Los otros 8 son por la "
                                  "coherencia entre el total y la decisión: si el equipo eligió la "
                                  "alternativa con menor puntaje, tiene que explicar el porqué "
                                  "explícitamente; si lo explica bien, dé los 8 completos, porque "
                                  "una matriz es una ayuda para pensar y no un oráculo."
            },
            {
                "clave": "QUÉ SE PIERDE",
                "respuesta": "**Se pierde la actualización inmediata.** Un libro prestado a las "
                             "nueve de la mañana va a aparecer como disponible hasta que la "
                             "voluntaria actualice al cierre. Eso significa que **algunos viajes en "
                             "vano van a seguir ocurriendo**, y hay que decirlo sin maquillar: la "
                             "solución elegida no lleva el problema a cero, lo baja.\n\n"
                             "**Se pierde también** el registro histórico de préstamos, que habría "
                             "servido para el otro problema de la biblioteca —los libros que no "
                             "vuelven—, y que en la sesión 6 se declaró explícitamente fuera de la "
                             "frontera.\n\n"
                             "**Y se gana:** que funcione sin computador, que cualquier voluntaria "
                             "nueva lo use sin capacitación, que se pueda construir y probar de "
                             "verdad en las sesiones que quedan, y que consuma casi nada de datos. "
                             "El intercambio es explícito y defendible.\n\n"
                             "Un equipo que escriba «no perdemos nada» no comparó: si una "
                             "alternativa fuera mejor en todos los criterios, no habría habido "
                             "decisión que tomar.",
                "como_calificar": "15 pts. Se califica que haya **una pérdida concreta y "
                                  "verificable**, no una fórmula de cortesía. «Perdemos un poco de "
                                  "funcionalidad» vale 5; «un libro prestado en la mañana aparece "
                                  "disponible hasta el cierre, así que algunos viajes en vano van a "
                                  "seguir» vale los 15. «No perdemos nada» vale 0 y hay que "
                                  "explicar por qué en el momento: significa que no compararon."
            },
            {
                "clave": "ALCANCE MÍNIMO Y PLAN DE VALIDACIÓN",
                "respuesta": "**Alcance mínimo del semestre:** *la lista de disponibilidad "
                             "consultable por enlace, con la pantalla de consulta para el usuario y "
                             "la pantalla de actualización para la voluntaria, funcionando desde un "
                             "celular y sin cuenta.* Un solo requisito funcional completo, "
                             "cumpliendo los tres no funcionales.\n\n"
                             "Pasa la prueba: si se construye solo eso y se pone delante de un "
                             "estudiante que necesita un libro, **le sirve** — puede saber si vale "
                             "la pena el viaje.\n\n"
                             "**Versión siguiente (declarado fuera):** búsqueda por tema · registro "
                             "histórico de préstamos · aviso automático de devolución · el "
                             "catálogo completo del acervo · reservas.\n\n"
                             "**Plan de validación:**\n\n"
                             "- **Con quién:** la coordinadora (rol de voluntaria) y **dos usuarios "
                             "reales en la puerta de la biblioteca**, ninguno del equipo.\n"
                             "- **Qué tareas se le piden**, tomadas de los criterios de aceptación "
                             "de la sesión 7: *(1) averigüe si el libro «X» está disponible; (2) "
                             "marque este libro como prestado; (3) dígame qué haría si el libro que "
                             "busca no aparece.*\n"
                             "- **Qué se observa:** cuánto tarda, dónde duda, qué toca por error, "
                             "qué busca y no encuentra, y si termina la tarea sin ayuda. **Se "
                             "observa en silencio**: no se explica, no se ayuda y no se pregunta si "
                             "le gustó.\n\n"
                             "La tarea (3) es la más valiosa y casi nadie la incluye: pregunta por "
                             "el caso en que el sistema **no** tiene la respuesta, que es donde se "
                             "cae la mayoría de los prototipos.",
                "como_calificar": "25 pts. Dos requisitos duros: (a) **el alcance mínimo resuelve "
                                  "algo por sí solo** (12 pts) — aplique la prueba en voz alta: «si "
                                  "construyen solo esto, ¿le sirve a la persona que vive el "
                                  "problema?»; si la respuesta es no, es un pedazo y vale 5; (b) "
                                  "**la persona de la prueba es ajena al equipo** (13 pts). Si "
                                  "planean probar entre ellos, corríjalo en la sala, no en la "
                                  "nota: es la trampa que arruina la sesión 12. Valore mucho que "
                                  "haya una tarea sobre el caso en que el sistema no tiene la "
                                  "respuesta."
            },
        ],
        "variantes": [
            {"caso": "Equipos que llegan sin las dos alternativas",
             "clave": "Va a pasar en al menos un equipo. No los deje discutir el trabajo "
                      "independiente durante veinte minutos: deles cinco para escribir dos frases, "
                      "y sugiera el truco que desbloquea siempre — **una de las dos alternativas no "
                      "puede usar ninguna tecnología nueva**. La comparación entre «lo que se puede "
                      "hacer con lo que ya existe» y «lo que queremos construir» es la más "
                      "instructiva de todas."},
            {"caso": "Equipos donde la alternativa ambiciosa gana la matriz",
             "clave": "Puede ser legítimo y no hay que forzar el resultado de la biblioteca. La "
                      "verificación es si los pesos son coherentes: si «construible en las sesiones "
                      "que quedan» pesa 1 y la alternativa exige diez semanas de trabajo, el "
                      "problema no es la matriz, es el peso. Pregunte «¿qué pasa si en la sesión 12 "
                      "no está listo?» y deje que ajusten el peso ellos."},
            {"caso": "Proyectos de proceso o gestión, sin pantallas",
             "clave": "El alcance mínimo suele ser **un formato más un acuerdo de quién lo llena y "
                      "cuándo**; el prototipo de la sesión 10 será ese formato. El plan de "
                      "validación se hace igual: se le pide a una persona ajena que ejecute el "
                      "proceso siguiendo solo el formato, sin preguntar nada, y se observa dónde se "
                      "queda trabada. Funciona igual de bien que con pantallas."},
            {"caso": "Equipos que planean probar entre ellos",
             "clave": "Es el error más costoso de la sesión, porque no se ve hasta la 12, cuando ya "
                      "no hay tiempo de arreglarlo. Exija hoy **el nombre del rol** de la persona "
                      "ajena que va a probar —no el nombre propio, por la regla de datos "
                      "personales— y cómo la van a contactar. Si no pueden nombrar a nadie ajeno, "
                      "el proyecto no pasó el criterio de acceso a los actores de la sesión 6 y hay "
                      "que reducirlo ya."},
        ],
        "cierre": "Cinco minutos hoy, que es más de lo habitual, y conviene usarlos en tres cosas. "
                  "Primero, la idea de la sesión: **decidir no es acertar.** Una decisión de "
                  "ingeniería se sostiene con criterios escritos antes, una justificación por "
                  "criterio y la lista de lo que se sacrificó; sin eso es una preferencia con "
                  "tabla. Segundo, el hallazgo del caso modelo, que vale la pena decir con estas "
                  "palabras: **la alternativa que sonaba más profesional perdió**, porque las "
                  "restricciones del contexto son reales y ellos mismos les habían puesto el peso "
                  "más alto. Tercero, las dos trampas de la validación —no probar con el equipo, no "
                  "preguntar «¿le gusta?»— porque se aplican en la sesión 12 y es donde se gana o "
                  "se pierde el corte 3. Anuncie la sesión 9: antes de construir hay que saber qué "
                  "ya existe y quién lo intentó, con fuentes verificables — y una respuesta de "
                  "asistente de IA no es una fuente.",
        "conexion": "Hacia atrás: la **sesión 7** dejó los requisitos y los criterios de "
                    "aceptación, que hoy se volvieron los criterios de la matriz y las tareas del "
                    "plan de validación; la **sesión 6** dejó las restricciones, que son los pesos "
                    "altos; la **sesión 5** dejó el indicador ambiental, que es un criterio más; la "
                    "**sesión 4** dejó el Therac-25, que es el argumento contra evaluarse a sí "
                    "mismo. Hacia adelante: la **sesión 9** busca antecedentes de la alternativa "
                    "elegida; la **sesión 10** prototipa exactamente el alcance mínimo de hoy; la "
                    "**sesión 11** lo corrige y cierra el corte 2; la **sesión 12** ejecuta este "
                    "plan de validación con una persona ajena; y la lista de «versión siguiente» se "
                    "muestra en la **exposición final de la sesión 15**.",
    },

    "errores": [
        {"dice": "«(A) una app y (B) una app con más funciones»",
         "por_que": "Es la misma idea dos veces: no hay decisión que tomar y la matriz no enseña nada.",
         "pida": "Una alternativa que **no use ninguna tecnología nueva**. La comparación entre lo que ya se puede hacer y lo que se quiere construir es la más instructiva."},
        {"dice": "Los pesos y las calificaciones escritos al mismo tiempo",
         "por_que": "Ahí se cuela la decisión ya tomada: sin mala intención, los pesos se acomodan para que gane el favorito.",
         "pida": "Los criterios y los pesos primero, en el documento, y solo después las calificaciones."},
        {"dice": "Una matriz de puros números, sin justificaciones",
         "por_que": "El número no se puede discutir ni defender; la justificación sí. Sin ella la matriz es un adorno.",
         "pida": "Media línea por casilla: por qué ese número para esa alternativa en ese criterio."},
        {"dice": "«No perdemos nada con esta decisión»",
         "por_que": "Si una alternativa fuera mejor en todos los criterios no habría habido nada que decidir.",
         "pida": "Qué se sacrifica, concreto y verificable. Y que se diga en la exposición final."},
        {"dice": "«Vamos a probar el prototipo entre nosotros»",
         "por_que": "Quien construyó sabe dónde hay que tocar: la prueba está decidida antes de empezar. Es el error del Therac-25 en pequeño.",
         "pida": "El rol de una persona ajena al equipo y cómo la van a contactar, hoy mismo."},
    ],

    "dudas": [
        {"p": "¿Y si las dos alternativas nos parecen igual de buenas?",
         "r": "Entonces los criterios están mal elegidos o los pesos no reflejan sus restricciones. "
              "Revisen los requisitos no funcionales: casi siempre hay uno que una de las dos no "
              "cumple, y ahí se rompe el empate. Y si de verdad empatan, elijan la más simple: es "
              "la que se puede construir y probar en el tiempo que queda."},
        {"p": "¿Podemos cambiar la decisión después?",
         "r": "Sí, y por eso se escribe la matriz: si en la sesión 10 aparece un dato nuevo, se "
              "cambia una calificación y se ve si la decisión se mueve. Eso es rediseñar con "
              "argumento. Lo que no funciona es cambiar de idea sin registro, porque en la sesión "
              "15 nadie va a poder explicar por qué se hizo lo que se hizo."},
        {"p": "¿El alcance mínimo no nos va a dejar con un proyecto muy pobre?",
         "r": "Al contrario. Se califica lo que funciona y se puede demostrar, más lo que ustedes "
              "declaran que dejaron fuera y por qué. Un alcance mínimo cumplido y probado con un "
              "usuario real, con su lista de «versión siguiente», se ve dirigido; un proyecto "
              "grande a medias se ve incompleto."},
        {"p": "¿A quién le pedimos que pruebe el prototipo?",
         "r": "A alguien que viva el problema y que no sea del equipo: el actor que identificaron "
              "en la sesión 6. Si no logran conseguir a nadie, ese es un problema de proyecto, no "
              "de logística, y hay que resolverlo ahora. Y recuerden la regla del curso: se usa el "
              "**rol** de la persona, no su nombre ni sus datos."},
    ],

    "notas_operativas": [
        "**El reparto de hoy es distinto: teoría 20 min, actividad 40 min.** Avísele al grupo en el "
        "minuto 2: los equipos administran mejor 40 minutos cuando saben que los tienen.",
        "**Dé el ritmo interno de la sala al repartir** (10-12-10-5). Cuarenta minutos sin estructura "
        "se van en discutir la primera línea.",
        "Entre a cada sala **dos veces**. Primera ronda: que los pesos estén escritos antes de las "
        "calificaciones. Segunda: que el alcance mínimo resuelva algo por sí solo.",
        "Si un equipo llega sin las dos alternativas, deles **cinco minutos** para escribirlas y "
        "sugiera que una no use tecnología nueva. No los deje improvisar veinte minutos.",
        "**Anote la alternativa elegida y el alcance mínimo de cada equipo.** En la sesión 10 se "
        "prototipa eso mismo y en la 12 se prueba: la lista es la que permite detectar desvíos.",
        "Exija el **rol** de la persona ajena que va a validar y cómo la van a contactar. Si un "
        "equipo no puede nombrar a nadie, el proyecto falló el criterio de acceso a los actores y "
        "hay que reducirlo hoy.",
        "Si un equipo cita montos o fechas de los cuatro casos, pida fuente y año. Las cifras de "
        "estos casos circulan con variaciones.",
    ],

    "ti_siguiente": {
        "tid": "Discusión de ejemplos reales — buscar **un caso propio** de proyecto que falló por "
               "saltarse una fase, con fuente verificable, y decir qué fase fue.",
        "ti": "Ajuste de propuestas de solución: dejar en el documento del equipo la alternativa "
              "elegida con su alcance mínimo y el flujo dibujado, ya corregido con lo que salió en "
              "las exposiciones.",
        "adelanto": "los **antecedentes**: qué ya existe, quién lo intentó y cómo se busca eso con "
                    "fuentes que se puedan verificar. Una respuesta de asistente de IA no es una "
                    "fuente.",
        "aviso": "Para la sesión 9 traigan la alternativa elegida escrita y el flujo dibujado. Se va "
                 "a buscar qué soluciones parecidas ya existen, y sin la propia decisión clara no "
                 "hay con qué comparar.",
    },

    "cierre_titulo": "Nos vemos en la sesión 9",
    "cierre_frase": "Decidir no es acertar: es poder defender lo que se eligió y lo que se perdió",
}


# =============================================================================
# CLASE 9 · Estrategias de innovacion en Ingenieria
# =============================================================================

TEMAS[9] = {
    "n": 9,
    "titulo": "Estrategias de innovación en Ingeniería",
    "subtitulo": "Nadie parte de cero: qué ya existe, quién lo intentó y qué van a hacer distinto",
    "hook": "Si su solución no existe en ningún lugar del mundo, hay dos posibilidades: "
            "es una gran idea, o no buscaron bien. ¿Cuál es más probable?",
    "hook_lines": [
        "Casi siempre es la segunda. Y descubrirlo hoy es barato.",
        "Buscar antecedentes no le quita mérito al proyecto: le da argumento.",
    ],
    "objetivos": [
        "Distinguir **innovación** de novedad tecnológica, y explicar por qué la adopción es lo que decide.",
        "Aplicar **cuatro maneras concretas** de generar una mejora sobre algo que ya existe.",
        "Buscar antecedentes con una **pregunta de búsqueda** y **evaluar la calidad de una fuente**.",
        "Fichar tres antecedentes verificables y escribir **qué van a hacer distinto y por qué**.",
    ],
    "agenda": {
        "Teoría y guía del docente": "Teoría — innovación, cuatro maneras de mejorar, búsqueda y calidad de fuentes",
        "Actividad en equipos": "Taller — tres antecedentes fichados y la propuesta de mejora",
        "Exposiciones": "5 equipos × 3 min — el antecedente más útil y qué van a hacer distinto",
    },
    "herramienta_nota": "La búsqueda se hace en el navegador y las fichas van en el **documento del "
                        "equipo**; el mapa de antecedentes se dibuja en **Excalidraw**. Hoy **no se "
                        "usa IA, y hay una razón de fondo**: la sesión de hoy es sobre fuentes "
                        "verificables, y un asistente puede devolver títulos, autores y años que "
                        "parecen reales y no existen. Una respuesta de asistente **no es una "
                        "fuente**: es un intermediario que no responde por lo que dice.",
    "avance_proyecto": "Tres antecedentes fichados con fuente verificable y la propuesta de mejora "
                       "del proyecto respecto a lo que ya existe",

    "teoria": [
        {
            "tipo": "cards",
            "titulo": "Qué es innovación y qué no",
            "cards": [
                ("No es novedad tecnológica",
                 "Usar lo último no es innovar. **Innovación es una solución que alguien adopta y "
                 "que cambia algo en la práctica.** Si nadie la usa, fue un experimento — "
                 "respetable, pero no innovación."),
                ("Incremental y radical",
                 "**Incremental**: mejorar algo que ya funciona, un paso a la vez. **Radical**: "
                 "cambiar la manera de hacerlo. La incremental es la que ocurre el 95 % de las "
                 "veces, y la única que cabe en un semestre."),
                ("De producto y de proceso",
                 "No solo se innova en el **qué** —un producto nuevo—, también en el **cómo**: el "
                 "mismo servicio con la mitad de pasos ya es innovación de proceso, y en un "
                 "proyecto de primer semestre suele ser lo más alcanzable."),
                ("Casi nunca empieza de cero",
                 "Casi toda innovación es una **recombinación**: algo que ya existía, traído a un "
                 "contexto donde no estaba. Por eso buscar antecedentes no le resta mérito al "
                 "proyecto: es de donde sale el material."),
            ],
            "columns": 2,
        },
        {
            "tipo": "steps",
            "titulo": "Cuatro maneras de generar una mejora",
            "steps": [
                ("QUITAR", "Sacar un paso, un requisito o un dato. **Es la más subestimada y la más efectiva**: quitar el registro previo, quitar la contraseña, quitar la visita presencial."),
                ("COMBINAR", "Juntar dos cosas que ya existen y que nadie había juntado en este contexto: una lista pública + un mensaje automático."),
                ("INVERTIR", "Dar vuelta a quién hace el trabajo o cuándo se hace: que el usuario consulte en vez de que alguien responda; que el dato se cargue al cerrar y no en el momento."),
                ("ADAPTAR DE OTRO DOMINIO", "Traer una solución que funciona en otro campo. La disponibilidad de un libro y la de una mesa en un restaurante son el mismo problema."),
            ],
            "sub": "Se aplican sobre un antecedente concreto, no sobre una hoja en blanco. Sin antecedente, estas cuatro no producen nada",
        },
        {
            "tipo": "steps",
            "titulo": "Cómo se busca un antecedente en cinco pasos",
            "steps": [
                ("1 · Escriba la pregunta de búsqueda", "No una palabra: una pregunta. «¿Cómo publican su disponibilidad las bibliotecas pequeñas sin sistema?». **Sin pregunta, la búsqueda no tiene final.**"),
                ("2 · Traduzca a términos de búsqueda", "Dos o tres versiones: el término técnico, el término común y el término en inglés. La mayoría de lo publicado está en inglés."),
                ("3 · Busque en más de un sitio", "Buscador general, buscador académico, repositorio institucional y normas oficiales. **Un solo sitio nunca alcanza.**"),
                ("4 · Filtre por calidad, no por posición", "El primer resultado no es el mejor. Mire autor, año, dónde se publicó y si se puede verificar."),
                ("5 · Fiche mientras lee, no después", "Autor o responsable, año, dónde, qué hace, **qué le falta para su caso** y el enlace. Lo que no se ficha, se pierde."),
            ],
            "sub": "El paso que casi nadie hace es el 1, y es el que evita las tres horas perdidas",
        },
        {
            "tipo": "tabla",
            "titulo": "Dónde buscar y qué esperar de cada sitio",
            "headers": ["Dónde", "Qué se encuentra", "Qué tener en cuenta"],
            "rows": [
                ["Buscador académico\n(Google Scholar y similares)",
                 "Artículos, tesis y capítulos. Se ve cuántas veces lo han citado.",
                 "Muchos están de pago. **Busque el PDF en el repositorio de la universidad del "
                 "autor**: casi siempre está libre y es legal."],
                ["Repositorios institucionales\ny bibliotecas digitales",
                 "Tesis y trabajos de grado de universidades, muchos sobre problemas locales.",
                 "Es la mejor fuente para un proyecto de contexto colombiano. **Verifique el año**: "
                 "hay trabajos muy viejos."],
                ["Portales regionales\n(SciELO, Redalyc y similares)",
                 "Revistas de América Latina, en español y de acceso abierto.",
                 "Muy útiles cuando el problema es regional y lo publicado en inglés no aplica."],
                ["Sitios oficiales y normas",
                 "Leyes, decretos, guías de ministerios, estadísticas de entidades públicas.",
                 "Es fuente **primaria**: se cita el documento, no la noticia que lo comenta. Ya lo "
                 "practicaron en las sesiones 4 y 5."],
                ["Documentación de proyectos\ny software reales",
                 "Soluciones que ya funcionan, con su manual y sus limitaciones declaradas.",
                 "Es el antecedente más útil para prototipar. **Cite versión y fecha de consulta**: "
                 "cambia todo el tiempo."],
                ["Asistente de IA",
                 "Pistas, sinónimos, términos en inglés para buscar mejor.",
                 "**No es una fuente.** Puede devolver autores, títulos y años que parecen reales y "
                 "no existen. Sirve para buscar, nunca para citar."],
            ],
            "note": "Regla del curso: **si no puede abrir el enlace y ver el documento, no lo cite.** "
                    "Y de las tres fuentes del taller, al menos una tiene que ser académica o "
                    "normativa.",
            "col_w": [2.3, 3.3, 4.2],
        },
        {
            "tipo": "box",
            "titulo": "Tres reglas sobre las fuentes",
            "notas": [
                ("advertencia",
                 "**Nunca invente una cita, y nunca copie una que no abrió.** Una cita falsa es la "
                 "falta más grave de un trabajo académico, y hoy es más fácil que nunca cometerla "
                 "sin querer: los asistentes de IA generan referencias con formato perfecto que no "
                 "existen. Si no abrió el documento, no lo cite."),
                ("info",
                 "**«No encontramos nada» es un resultado válido, si se escribe bien.** Se anota "
                 "qué se buscó, con qué términos, en qué sitios, y qué se encontró de lo más "
                 "cercano. Eso es un hallazgo y se califica. Lo que no se acepta es rellenar el "
                 "vacío con fuentes de adorno que nadie leyó."),
                ("aclaracion",
                 "**Encontrar que su idea ya existe no arruina el proyecto: lo mejora.** Significa "
                 "que el problema es real y que hay de dónde partir. La pregunta deja de ser «¿lo "
                 "inventamos?» y pasa a ser «¿qué hacemos distinto, y por qué eso importa en "
                 "nuestro contexto?», que es una pregunta de ingeniería mucho mejor."),
            ],
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada: si no existe en ningún lado, probablemente no buscaron",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "La pregunta es deliberadamente incómoda y funciona porque casi todos los equipos "
                "llegan a esta altura del semestre convencidos de que su solución es original. La "
                "respuesta estadística es dura: en un mundo con millones de ingenieros y "
                "cincuenta años de software publicado, la probabilidad de que un problema común "
                "—disponibilidad, inventario, turnos, avisos— no tenga antecedentes es "
                "prácticamente cero.",
                "Lo que hay que evitar es que el grupo lo lea como un desaire. El encuadre que "
                "funciona: **buscar antecedentes no le quita mérito al proyecto, le da "
                "argumento**. Un equipo que dice «esto no existe» está apostando; un equipo que "
                "dice «existen estas tres soluciones, ninguna funciona sin computador en el "
                "mostrador, y nosotros resolvemos justamente eso» tiene una posición defendible "
                "ante cualquiera. La segunda frase es la que se califica en la sesión 15.",
                "Aproveche el muro para recoger las respuestas y luego voltee la pregunta: *¿qué "
                "sería peor, descubrir hoy que ya existe, o descubrirlo el día de la exposición "
                "final cuando alguien del público lo diga?* Esa reformulación convierte la sesión "
                "en una protección y no en una tarea.",
            ],
        },
        {
            "titulo": "Innovación: por qué la adopción es lo que decide",
            "slide": "{{slide:Qué es innovación}}",
            "cuerpo": [
                "La confusión que hay que desarmar en primer semestre es **innovación = tecnología "
                "nueva**. Con esa definición, un equipo se siente obligado a meter inteligencia "
                "artificial, blockchain o lo que esté de moda en un proyecto que no lo necesita, y "
                "el resultado es peor que la solución simple.",
                "La definición útil: **innovación es una solución que alguien adopta y que cambia "
                "algo en la práctica**. La palabra clave es *adopta*. Si nadie la usa, fue un "
                "experimento — respetable, pero no innovación. Esto tiene una consecuencia directa "
                "sobre sus proyectos y conviene decirla: la biblioteca que empieza a usar una lista "
                "publicada es más innovadora que la aplicación perfecta que quedó en el "
                "computador del equipo.",
                "**Incremental y radical.** Lo incremental —mejorar algo que ya funciona, un paso a "
                "la vez— es lo que ocurre casi siempre y lo único que cabe en un semestre. Hay que "
                "decirlo sin condescendencia: la mayoría de la ingeniería del mundo es "
                "incremental, y la mejora incremental bien hecha y adoptada vale más que la "
                "revolución no entregada.",
                "**De producto y de proceso.** Innovar en el *cómo* —el mismo servicio con la mitad "
                "de los pasos— es innovación de proceso, y para muchos de sus proyectos es lo más "
                "alcanzable y lo más útil. Si un equipo tiene un proyecto de gestión sin pantallas, "
                "este es su lugar en la sesión.",
                "Y el punto que abre el resto de la clase: **casi toda innovación es una "
                "recombinación** de cosas que ya existían, traídas a un contexto donde no estaban. "
                "Eso convierte la búsqueda de antecedentes en la materia prima del proyecto, y no "
                "en un requisito académico. Sin antecedentes no hay con qué recombinar.",
            ],
        },
        {
            "titulo": "Las cuatro maneras de generar una mejora",
            "slide": "{{slide:Cuatro maneras}}",
            "cuerpo": [
                "Estas cuatro operaciones son deliberadamente simples porque tienen que poder "
                "usarse en quince minutos dentro de una sala de grupo. Y hay una condición que hay "
                "que repetir: **se aplican sobre un antecedente concreto, no sobre una hoja en "
                "blanco**. Sin antecedente no producen nada.",
                "**QUITAR** es la más subestimada y casi siempre la más efectiva. Quitar un paso, un "
                "requisito, un dato, una pantalla. En el caso de la biblioteca: quitar el registro "
                "previo del usuario, quitar la contraseña, quitar la visita presencial. Cada cosa "
                "que se quita elimina una razón para que la solución no se use. Vale la pena "
                "señalar que **quitar también reduce la huella** —menos datos, menos consultas, "
                "menos transferencia—, que es el indicador de la sesión 5.",
                "**COMBINAR** es juntar dos cosas que ya existen y que nadie había juntado en ese "
                "contexto: una lista publicada más un mensaje automático; un formulario más un "
                "tablero. Es la operación de la que sale la mayoría de las innovaciones "
                "incrementales reales.",
                "**INVERTIR** es dar vuelta a quién hace el trabajo o cuándo se hace: que el "
                "usuario consulte en vez de que alguien responda —que es exactamente la decisión "
                "de la sesión 8—, que el dato se cargue al cerrar y no en el momento de atender. "
                "Invertir suele resolver restricciones de personal, que son las más duras y las "
                "que menos se pueden comprar.",
                "**ADAPTAR DE OTRO DOMINIO** es traer una solución que ya funciona en otro campo. "
                "El ejemplo que conviene dar porque desbloquea a todos los equipos: *la "
                "disponibilidad de un libro y la disponibilidad de una mesa en un restaurante son "
                "el mismo problema*. Si un equipo se queda sin ideas, la pregunta que hay que "
                "hacerle es «¿qué otro negocio tiene este mismo problema y cómo lo resolvió?».",
            ],
        },
        {
            "titulo": "Buscar: la pregunta de búsqueda y los cinco pasos",
            "slide": "{{slide:Cómo se busca un antecedente}}",
            "cuerpo": [
                "El paso que casi nadie hace es el primero, y es el que ahorra las tres horas "
                "perdidas: **escribir la pregunta de búsqueda antes de buscar**. No una palabra "
                "—«bibliotecas»— sino una pregunta: *¿cómo publican su disponibilidad las "
                "bibliotecas pequeñas que no tienen sistema?* Sin pregunta la búsqueda no tiene "
                "final, porque nada permite decidir si un resultado sirve o no.",
                "**Traducir a términos de búsqueda** es el paso técnico: dos o tres versiones del "
                "mismo concepto —el término técnico, el término común y el término en inglés—. Hay "
                "que decirles sin rodeos que **la mayoría de lo publicado está en inglés** y que "
                "buscar solo en español recorta el mundo disponible a una fracción. El navegador "
                "traduce; la falta de resultados no.",
                "**Buscar en más de un sitio** es donde la mayoría falla por comodidad: un buscador "
                "general, un buscador académico, un repositorio institucional y las normas "
                "oficiales. Cada uno devuelve un tipo distinto de cosa y ninguno cubre a los "
                "otros.",
                "**Filtrar por calidad y no por posición** es el criterio que hay que dejar "
                "instalado para toda la carrera: el primer resultado es el mejor posicionado, que "
                "no es lo mismo que el mejor. Cuatro preguntas rápidas bastan: quién lo escribe "
                "—hay un autor o una institución responsable—, de qué año es, dónde se publicó, y "
                "si se puede verificar abriendo el documento.",
                "**Fichar mientras se lee** cierra el método. La ficha del curso tiene seis campos: "
                "autor o responsable, año, dónde, qué hace, **qué le falta para nuestro caso**, y "
                "el enlace. El quinto campo es el que convierte una bibliografía en un insumo de "
                "diseño: es la brecha donde va a entrar su propuesta de mejora, y es lo que se "
                "califica más alto en el taller.",
            ],
        },
        {
            "titulo": "Calidad de las fuentes, la IA y qué hacer cuando no se encuentra nada",
            "slide": "{{slide:Dónde buscar}} {{slide:Tres reglas sobre las fuentes}}",
            "cuerpo": [
                "La tabla de sitios hay que recorrerla rápido y con un consejo práctico por fila. El "
                "más valioso: **cuando un artículo académico está de pago, busque el PDF en el "
                "repositorio institucional de la universidad del autor**; una parte grande está "
                "disponible de manera libre y legal. Esto le resuelve a un estudiante de primer "
                "semestre el muro más desmoralizante de la búsqueda académica.",
                "Los **repositorios institucionales** merecen un énfasis especial en este curso: "
                "son la mejor fuente para problemas de contexto colombiano, porque las tesis y "
                "trabajos de grado suelen atacar exactamente el tipo de problema local que ellos "
                "eligieron. Y los **sitios oficiales y las normas** son fuente primaria: se cita el "
                "documento, no la noticia que lo comenta, que es la misma regla que ya practicaron "
                "en la sesión 4 con los numerales y en la sesión 5 con las cifras.",
                "**El asistente de IA** merece su propia fila y hay que ser preciso, porque este "
                "curso lo autoriza en dos sesiones y lo prohíbe en el resto. Sirve para buscar "
                "—pistas, sinónimos, el término en inglés que uno no conoce— y **no sirve para "
                "citar**. La razón técnica hay que decirla explícitamente: un modelo de lenguaje "
                "genera texto plausible, y una referencia bibliográfica plausible tiene autor, "
                "título, revista y año con formato perfecto **aunque no exista**. Ha habido "
                "abogados sancionados por presentar ante un juez citas de jurisprudencia generadas "
                "así. La regla del curso es simple y verificable: **si no puede abrir el enlace y "
                "ver el documento, no lo cite.**",
                "Las tres reglas del cierre son las que definen la ética del trabajo académico en "
                "este curso. **No inventar una cita ni copiar una que no se abrió** es la falta más "
                "grave, y hoy es más fácil cometerla sin mala intención que nunca. **«No "
                "encontramos nada» es un resultado válido** si se escribe con qué términos, en qué "
                "sitios y qué fue lo más cercano que apareció: eso es un hallazgo, se califica, y "
                "es infinitamente mejor que tres fuentes de adorno que nadie leyó. Y la tercera "
                "tranquiliza y hay que decirla con convicción: **encontrar que su idea ya existe "
                "mejora el proyecto**, porque confirma que el problema es real y da un punto de "
                "partida; la pregunta deja de ser «¿lo inventamos?» y pasa a ser «¿qué hacemos "
                "distinto y por qué eso importa en nuestro contexto?», que es una pregunta de "
                "ingeniería mucho mejor.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:10 · Apertura · [Slide 4]",
            "cuerpo": [
                "Comparta pantalla antes de que entre el primero:",
                "> «Si su solución no existe en ningún lugar del mundo, hay dos posibilidades: es "
                "una gran idea, o no buscaron bien. ¿Cuál es más probable?»",
                "**[Nota docente]:** después de recoger respuestas, voltee la pregunta: *¿qué sería "
                "peor, descubrir hoy que ya existe, o descubrirlo el día de la exposición final "
                "cuando alguien del público lo diga?* Eso convierte la sesión en una protección.",
                "**[Nota docente]:** pida que abran la **alternativa elegida en la sesión 8**. Los "
                "antecedentes se buscan sobre esa decisión, no sobre el tema en general.",
            ],
        },
        {
            "titulo": "00:10–00:55 · Teoría · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]",
            "cuerpo": [
                "Reparto sugerido de los 45 min:",
                "- **8 min** · Qué es innovación y qué no [Slide 5]. El punto es **la adopción**: "
                "una lista que la biblioteca usa vale más que la app perfecta que quedó en el "
                "computador del equipo.",
                "- **8 min** · Cuatro maneras de generar una mejora [Slide 6]. Insista en **QUITAR** "
                "y en el ejemplo del restaurante para desbloquear equipos.",
                "- **10 min** · Cómo se busca [Slide 7]. Haga escribir la pregunta de búsqueda "
                "**en el chat**, un equipo a la vez: son 2 minutos y cambia el taller entero.",
                "- **12 min** · Dónde buscar [Slide 8]. Un consejo por fila. No se salte el truco "
                "del repositorio institucional para los artículos de pago.",
                "- **7 min** · Tres reglas sobre las fuentes [Slide 9]. **No la recorte:** es la "
                "diapositiva de integridad académica de todo el curso.",
                "**[Nota docente]:** si va retrasado, comprima innovación a 5 minutos. La búsqueda y "
                "las reglas son lo que se califica hoy.",
            ],
        },
        {
            "titulo": "00:55–01:12 · Taller en salas de grupo · [Slide 10]",
            "cuerpo": [
                "**2 min** para abrir el documento del equipo y Excalidraw.",
                "**15 min** en salas. Entre a las cinco con **una sola pregunta: ¿qué le falta a "
                "ese antecedente para servir en su caso?** Es el campo que convierte la búsqueda en "
                "diseño y es el 30 % de la rúbrica.",
                "**[Nota docente]:** en 15 minutos no se hace una revisión bibliográfica completa, y "
                "está bien. Se hacen **tres fichas verificables**. Si un equipo trae una sola "
                "fuente excelente y bien fichada, vale más que tres a medias.",
                "**[Nota docente]:** si ve una referencia sin enlace o que no abre, pídala en "
                "pantalla en ese momento. Es la única forma de cortar la cita inventada, y hacerlo "
                "en la sala enseña más que descontarlo en la nota.",
            ],
        },
        {
            "titulo": "01:12–01:27 · Exposiciones · [Slide 11]",
            "cuerpo": [
                "5 equipos × 3 min. **El minuto obligatorio es «qué le falta a lo que ya existe y "
                "qué vamos a hacer distinto»**.",
                "**[Nota docente]:** los cinco enlaces en el chat antes de arrancar.",
                "**[Nota docente]:** haga que muestren **el documento abierto**, no la referencia "
                "escrita. Diez segundos de pantalla compartida valen más que cualquier declaración.",
                "**[Nota docente]:** anote la propuesta de mejora de cada equipo. Es el eje del "
                "informe final de la sesión 16 y de la exposición de la 15.",
            ],
        },
        {
            "titulo": "01:27–01:30 · Cierre · [Slide 12][Slide 13]",
            "cuerpo": [
                "Una idea: **nadie parte de cero, y decirlo es una fortaleza.** «Existen estas tres "
                "soluciones, ninguna funciona sin computador en el mostrador, y nosotros resolvemos "
                "eso» es una posición defendible ante cualquiera.",
                "Repita la regla: **si no puede abrir el enlace y ver el documento, no lo cite.**",
                "Anuncie la sesión 10: **prototipado**. Se pasa de la decisión y los antecedentes a "
                "las tres pantallas o pasos del flujo principal.",
            ],
        },
    ],

    "taller": {
        "archivo": "Antecedentes y propuesta de mejora",
        "titulo": "Antecedentes y propuesta de mejora",
        "min": 17,
        "exposicion": 3,
        "consigna": "Averigüen qué ya existe. Escriban su **pregunta de búsqueda**, fichen **tres "
                    "antecedentes verificables** —al menos uno académico o normativo—, digan **qué "
                    "buscaron y no encontraron**, y escriban la **propuesta de mejora**: qué van a "
                    "hacer distinto, con cuál de las cuatro operaciones, y qué van a reusar.",
        "entregable": "las tres fichas de antecedentes y la propuesta de mejora en el documento del "
                      "equipo, más el mapa de antecedentes en Excalidraw (PNG en la carpeta del "
                      "equipo)",
        "entregable_corto": "tres fichas de antecedentes + propuesta de mejora + mapa en Excalidraw",
        "reparto_titulo": "Reparto sugerido dentro del equipo:",
        "reparto": "no busquen los cinco lo mismo. **Dos personas** en buscador académico y "
                   "repositorios institucionales, **dos** en soluciones y software que ya funcionan, "
                   "**una** en normas y datos oficiales. A los 10 minutos se juntan y se escriben "
                   "las tres mejores fichas. La búsqueda se hace sobre la **alternativa elegida en "
                   "la sesión 8**, no sobre el tema en general.",
        "reparto_corto": "búsqueda repartida: 2 académico · 2 soluciones reales · 1 normas",
        "bloques": [
            {"clave": "LA PREGUNTA DE BÚSQUEDA",
             "pide": "Una **pregunta**, no una palabra, y sus términos de búsqueda en dos o tres "
                     "versiones — incluida una en inglés.",
             "check": "es una pregunta que se puede responder con un sí, un no o un ejemplo. «Bibliotecas» no es una pregunta."},
            {"clave": "TRES ANTECEDENTES FICHADOS",
             "pide": "Tres fichas con los seis campos: **autor o responsable · año · dónde · qué "
                     "hace · qué le falta para nuestro caso · enlace**. Al menos una fuente "
                     "académica o normativa.",
             "check": "los tres enlaces abren y muestran el documento. Una referencia que no abre no cuenta, aunque el formato sea impecable."},
            {"clave": "QUÉ BUSCAMOS Y NO ENCONTRAMOS",
             "pide": "Qué buscaron, con qué términos, en qué sitios, y **qué fue lo más cercano** "
                     "que apareció. «No encontramos nada» bien escrito es un hallazgo.",
             "check": "se pueden repetir sus búsquedas leyendo lo que escribieron. Si no se pueden repetir, no está escrito."},
            {"clave": "LA PROPUESTA DE MEJORA",
             "pide": "Qué van a hacer distinto respecto a lo fichado, **con cuál de las cuatro "
                     "operaciones** (quitar, combinar, invertir, adaptar), y por qué eso importa en "
                     "su contexto.",
             "check": "la mejora se apoya en la brecha que ustedes mismos escribieron en el campo «qué le falta». Si no se apoya en nada, es un deseo."},
            {"clave": "LO QUE VAMOS A REUSAR",
             "pide": "Qué de lo que ya existe piensan aprovechar: una idea de diseño, una forma de "
                     "organizar los datos, una herramienta, una lista de errores conocidos.",
             "check": "hay al menos una cosa concreta que se reusa. «Nada» significa que no leyeron lo que ficharon."},
        ],
        "expo": [
            ("25 s · La pregunta de búsqueda", "Leída tal cual, con un término en inglés."),
            ("50 s · El antecedente más útil", "Cuál es, de qué año, y **muéstrenlo en pantalla**."),
            ("50 s · Qué le falta", "La brecha respecto a su caso. Es el minuto obligatorio."),
            ("40 s · La propuesta de mejora", "Qué hacen distinto y con cuál de las cuatro operaciones."),
            ("15 s · Qué reusan", "Una cosa concreta que aprovechan de lo que ya existe."),
        ],
    },

    "rubrica": [
        ("La pregunta de búsqueda es una pregunta y tiene términos en dos o tres versiones", 15,
         "Sin pregunta la búsqueda no tiene final, y sin términos en inglés se recorta el mundo disponible a una fracción."),
        ("Las tres fichas están completas y los tres enlaces abren y muestran el documento", 30,
         "Es la verificación de integridad académica del curso: una referencia que no se puede abrir no es una fuente."),
        ("Se escribe qué se buscó y no se encontró, de forma que otra persona pueda repetirlo", 15,
         "Declarar el vacío es un hallazgo, y es lo contrario de rellenar con fuentes de adorno."),
        ("La propuesta de mejora se apoya en la brecha escrita y nombra la operación usada", 25,
         "Es lo que convierte una bibliografía en una decisión de diseño defendible."),
        ("Se identifica al menos una cosa concreta que se reusa de lo existente", 15,
         "Nadie parte de cero: reconocer lo que se aprovecha es honestidad y ahorro de trabajo."),
    ],

    "solucion": {
        "para_que": "Este documento trae la búsqueda completa del caso de la biblioteca: la pregunta, "
                    "tres fichas con la brecha de cada una, lo que no se encontró y la propuesta de "
                    "mejora. Su valor está en dos cosas que ningún equipo hace solo: **el campo "
                    "«qué le falta para nuestro caso»** y **el bloque de lo que no se encontró**. Si "
                    "el docente solo alcanza a leer un bloque, que sea **TRES ANTECEDENTES "
                    "FICHADOS**.\n\n"
                    "**Aviso operativo:** los antecedentes de este documento son reales y "
                    "verificables, pero **las direcciones web cambian**. Ábralas antes de la sesión; "
                    "si alguna no abre, dígalo en clase — es la mejor demostración posible de por "
                    "qué se anota la fecha de consulta.",
        "caso_titulo": "La biblioteca del barrio · qué ya existe y qué vamos a hacer distinto",
        "caso": "Decisión de la sesión 8: una **lista de disponibilidad publicada** que la voluntaria "
                "actualiza una vez al día desde su celular. Restricciones vigentes: presupuesto "
                "cero, sin computador en el mostrador, voluntarias que rotan sin capacitación larga, "
                "menos de 200 KB por consulta. La búsqueda de hoy es sobre **esa** decisión: cómo "
                "publican su disponibilidad las bibliotecas pequeñas que no tienen sistema.",
        "por_que_este_caso": "Porque la búsqueda encuentra algo incómodo y muy instructivo: existe "
                             "software libre maduro que resuelve el problema completo desde hace más "
                             "de veinte años, y **no sirve para este caso**. Ver por qué un "
                             "antecedente excelente no aplica es exactamente lo que hay que "
                             "enseñar.",
        "bloques": [
            {
                "clave": "LA PREGUNTA DE BÚSQUEDA",
                "respuesta": "**Pregunta:** *¿cómo publican su disponibilidad de libros las "
                             "bibliotecas pequeñas o comunitarias que no tienen un sistema de "
                             "gestión ni presupuesto?*\n\n"
                             "**Términos de búsqueda, en tres versiones:**\n\n"
                             "- Técnico: «catálogo en línea biblioteca», «OPAC», «sistema integrado "
                             "de gestión bibliotecaria»\n"
                             "- Común: «cómo saber si un libro está disponible biblioteca», «lista "
                             "de préstamos biblioteca pequeña»\n"
                             "- Inglés: *«small library catalog without ILS»*, *«community library "
                             "book availability»*, *«low-cost library management»*\n\n"
                             "El término técnico **OPAC** (*Online Public Access Catalog*) es un "
                             "buen ejemplo de lo que se gana en el paso 2: es la palabra que usa el "
                             "mundo bibliotecario para exactamente esto, y sin ella la búsqueda "
                             "devuelve blogs; con ella devuelve documentación, normas y "
                             "software.\n\n"
                             "**Ejemplo de mala pregunta**, para contrastar en clase: «biblioteca». "
                             "Devuelve millones de resultados y ninguno permite decidir si sirve.",
                "como_calificar": "15 pts. Dos verificaciones: (a) **¿es una pregunta?** Si es una "
                                  "palabra o un tema, vale 5 y hay que reescribirla en la sala; (b) "
                                  "**¿hay una versión en inglés?** Si no, vale 9 como máximo: no es "
                                  "un capricho, es la diferencia entre buscar en una fracción del "
                                  "mundo publicado o en todo. Valore especialmente si el equipo "
                                  "encontró **el término técnico del dominio** —como OPAC aquí—, "
                                  "porque es lo que multiplica la calidad de los resultados."
            },
            {
                "clave": "TRES ANTECEDENTES FICHADOS",
                "respuesta": "**Ficha 1 · Software libre de gestión bibliotecaria (Koha)**\n\n"
                             "- *Responsable:* comunidad del proyecto Koha (se originó en "
                             "Horowhenua Library Trust, Nueva Zelanda)\n"
                             "- *Año:* 1999, en desarrollo continuo desde entonces\n"
                             "- *Dónde:* sitio y documentación oficial del proyecto\n"
                             "- *Qué hace:* sistema integrado completo de gestión bibliotecaria "
                             "—catálogo, circulación, préstamos, catálogo público en línea—, "
                             "software libre, sin costo de licencia\n"
                             "- **Qué le falta para nuestro caso:** requiere instalarse y "
                             "administrarse en un servidor, y catalogar el acervo completo antes de "
                             "servir de algo. Con presupuesto cero, sin computador en el mostrador y "
                             "con voluntarias que rotan, **la barrera no es el precio: es la "
                             "administración**\n"
                             "- *Enlace:* sitio oficial del proyecto (anotar fecha de consulta)\n\n"
                             "**Ficha 2 · Norma nacional sobre bibliotecas públicas (Colombia)**\n\n"
                             "- *Responsable:* Congreso de la República de Colombia — **Ley 1379 de "
                             "2010**, que organiza la Red Nacional de Bibliotecas Públicas\n"
                             "- *Año:* 2010\n"
                             "- *Dónde:* diario oficial y sitio del Ministerio de Cultura / "
                             "Biblioteca Nacional de Colombia\n"
                             "- *Qué hace:* define qué es una biblioteca pública, qué servicios debe "
                             "prestar y cómo se articula la red nacional\n"
                             "- **Qué le falta para nuestro caso:** la biblioteca del barrio es "
                             "comunitaria y puede no estar inscrita en la red, así que la norma "
                             "**no le da acceso a los recursos** pero sí sirve para dos cosas: "
                             "fundamentar por qué el acceso a la información es un servicio "
                             "esperable, y descubrir si inscribirse es una vía de solución que no "
                             "habíamos considerado\n"
                             "- *Enlace:* texto oficial de la ley (anotar fecha de consulta)\n\n"
                             "**Ficha 3 · Catálogo público en línea de una biblioteca grande**\n\n"
                             "- *Responsable:* Biblioteca Nacional de Colombia (u otra biblioteca "
                             "pública con catálogo en línea)\n"
                             "- *Año:* consulta del año en curso\n"
                             "- *Dónde:* su portal web\n"
                             "- *Qué hace:* permite buscar un título y ver si está disponible, sin ir "
                             "físicamente\n"
                             "- **Qué le falta para nuestro caso:** está construido sobre un sistema "
                             "de gestión con personal dedicado; **lo que sí se puede reusar es el "
                             "diseño de la pantalla de consulta** —qué campos muestra, en qué orden, "
                             "qué dice cuando un libro no está disponible—, que es información de "
                             "diseño gratis\n"
                             "- *Enlace:* portal consultado (anotar fecha de consulta)\n\n"
                             "**El hallazgo de la búsqueda, y la lección de la sesión:** existe "
                             "software libre y maduro que resuelve el problema completo desde hace "
                             "más de veinte años, y **no sirve para este caso**. Eso no invalida el "
                             "proyecto: define su lugar. La brecha real no es «no hay software de "
                             "bibliotecas», es «**no hay una solución que funcione sin administrador, "
                             "sin computador en el mostrador y sin catalogar el acervo completo "
                             "primero**». Ese es un problema legítimo de ingeniería y está "
                             "sustentado con fuentes.",
                "como_calificar": "30 pts, el bloque que decide. La verificación es literal y hay que "
                                  "hacerla en la sala o en la exposición: **pida que abran el enlace "
                                  "en pantalla**. Una referencia con formato impecable que no abre "
                                  "vale 0 en esa ficha, y hay que explicar por qué sin dramatizar: "
                                  "es la falta más grave del trabajo académico y hoy se comete sin "
                                  "querer. 10 pts por ficha completa con sus seis campos; el campo "
                                  "**«qué le falta para nuestro caso»** vale la mitad de cada ficha, "
                                  "porque es el único que exige haber leído. Si el equipo trae dos "
                                  "fichas excelentes en vez de tres regulares, dé 25: premie la "
                                  "lectura, no el conteo."
            },
            {
                "clave": "QUÉ BUSCAMOS Y NO ENCONTRAMOS",
                "respuesta": "**Lo que se buscó y no apareció:** ningún trabajo publicado sobre "
                             "disponibilidad de libros en **bibliotecas comunitarias de barrio sin "
                             "presupuesto en Colombia**. Se buscó con los términos «biblioteca "
                             "comunitaria», «biblioteca de barrio» y «biblioteca popular» combinados "
                             "con «catálogo», «disponibilidad» y «préstamos», en un buscador "
                             "académico, en dos repositorios institucionales y en portales de "
                             "revistas regionales.\n\n"
                             "**Lo más cercano que apareció:** trabajos sobre bibliotecas escolares "
                             "y sobre la red pública nacional, que tienen personal asignado y "
                             "presupuesto — es decir, **no comparten la restricción que define "
                             "nuestro caso**.\n\n"
                             "**Lo que eso significa, dicho con precisión:** no significa «somos los "
                             "primeros en el mundo». Significa dos cosas mucho más útiles y "
                             "defendibles: (1) el caso específico está poco documentado, así que hay "
                             "que **adaptar** soluciones de contextos vecinos en vez de copiarlas; y "
                             "(2) **el trabajo del equipo tiene valor documental propio**: si "
                             "escriben bien lo que hicieron y midieron, están produciendo el "
                             "antecedente que no encontraron.\n\n"
                             "Lo que **no** se hizo, y no hay que hacer: rellenar el bloque con tres "
                             "referencias sobre «bibliotecas» en general, sin leerlas, para que la "
                             "bibliografía se vea larga.",
                "como_calificar": "15 pts. El criterio es la **reproducibilidad**: ¿puede otra "
                                  "persona repetir esas búsquedas leyendo lo que escribieron? Si "
                                  "solo dice «buscamos y no encontramos nada», vale 4. Si dice qué "
                                  "términos, en qué sitios y qué fue lo más cercano, valen los 15. "
                                  "Y valore mucho la interpretación correcta del vacío: un equipo "
                                  "que escribe «somos los primeros del mundo» no entendió nada, "
                                  "mientras uno que escribe «está poco documentado, hay que adaptar "
                                  "de contextos vecinos» entendió exactamente la clase."
            },
            {
                "clave": "LA PROPUESTA DE MEJORA",
                "respuesta": "**La mejora, en una frase:** *publicar la disponibilidad sin catalogar "
                             "el acervo completo y sin administrar un sistema — solo los títulos que "
                             "se prestan, actualizados una vez al día desde el celular de la "
                             "voluntaria.*\n\n"
                             "**La operación usada: QUITAR.** Se le quitan al antecedente principal "
                             "—el sistema integrado de gestión— las tres cosas que lo vuelven "
                             "inaplicable en este contexto: el servidor que hay que administrar, la "
                             "catalogación completa previa, y el registro en el momento de la "
                             "atención. Lo que queda es mucho menos potente y **es lo único que "
                             "puede existir en esta biblioteca**.\n\n"
                             "**Y una segunda operación, INVERTIR:** en el antecedente, el "
                             "encargado responde consultas; aquí el usuario consulta solo. Se "
                             "invierte quién hace el trabajo, que es lo que resuelve la restricción "
                             "más dura — la que no se puede comprar, porque es personal "
                             "voluntario.\n\n"
                             "**Por qué eso importa en nuestro contexto:** las tres cosas que se "
                             "quitaron son exactamente las tres restricciones del árbol de la sesión "
                             "6. La mejora no es una idea suelta: **es la brecha del campo «qué le "
                             "falta» convertida en decisión de diseño.** Eso es lo que la vuelve "
                             "defendible ante cualquiera en la sesión 15.\n\n"
                             "**Comparación con una propuesta débil**, útil para mostrar en clase: "
                             "«nuestra mejora es que va a ser más fácil de usar y más moderna». No "
                             "se apoya en ninguna brecha escrita, no nombra ninguna operación, y no "
                             "se puede verificar. Es un deseo, no una propuesta.",
                "como_calificar": "25 pts. Una sola verificación, y es dura: **¿la mejora se apoya "
                                  "en una brecha que ellos mismos escribieron en el campo «qué le "
                                  "falta»?** Si sí, y nombran la operación (quitar / combinar / "
                                  "invertir / adaptar), valen los 25. Si la mejora aparece de la "
                                  "nada —«más fácil», «más moderno», «con IA»—, vale 8, y "
                                  "muéstreles la conexión que les falta señalando su propia ficha. "
                                  "Dé el puntaje completo también a mejoras modestas: quitar un paso "
                                  "bien argumentado es innovación incremental, que es de lo que "
                                  "estaba hecha la primera diapositiva."
            },
            {
                "clave": "LO QUE VAMOS A REUSAR",
                "respuesta": "**Del catálogo público de la biblioteca grande (ficha 3): el diseño de "
                             "la pantalla de consulta.** Qué campos muestra —título, autor, estado—, "
                             "en qué orden, y sobre todo **qué dice cuando el libro no está "
                             "disponible**, que es el caso donde se cae la mayoría de los "
                             "prototipos. Es información de diseño gratis y probada con miles de "
                             "usuarios.\n\n"
                             "**Del software libre de gestión (ficha 1): el vocabulario y la manera "
                             "de organizar los datos.** Qué se guarda de un préstamo, qué estados "
                             "puede tener un ejemplar, la diferencia entre título y ejemplar. No se "
                             "reusa el software: se reusa el modelo, que es la parte difícil y está "
                             "resuelta desde hace veinte años.\n\n"
                             "**De la norma (ficha 2): el argumento del informe final.** Sirve para "
                             "sustentar por qué el acceso a la información es un servicio esperable "
                             "y no un lujo, que es exactamente lo que va a pedir la evaluación de "
                             "impacto social de la sesión 13.\n\n"
                             "Escribir esto explícitamente tiene un efecto adicional que vale la "
                             "pena señalarles: **es lo contrario del plagio.** Usar lo que otros "
                             "resolvieron, diciendo de dónde salió, es la práctica normal de la "
                             "ingeniería; usarlo sin decirlo es la falta.",
                "como_calificar": "15 pts. Se califica que haya **al menos una cosa concreta y "
                                  "nombrada**. «Vamos a reusar la idea general» vale 5; «reusamos "
                                  "los campos y el orden de la pantalla de consulta, y el modelo de "
                                  "estados de un ejemplar» valen los 15. «Nada» vale 0 y significa "
                                  "que no leyeron lo que ficharon — se nota de inmediato, porque un "
                                  "equipo que leyó siempre encuentra algo que aprovechar."
            },
        ],
        "variantes": [
            {"caso": "Equipos que llegan con tres referencias que no abren",
             "clave": "Va a pasar, sobre todo si usaron un asistente pese a la indicación. No lo "
                      "trate como trampa: pida abrir los tres enlaces en pantalla y deje que el "
                      "resultado hable. Ahí es donde la advertencia de la diapositiva 9 deja de ser "
                      "teórica. Deles diez minutos para reemplazar las que no abran, y anote el caso "
                      "para la sesión 11, donde la IA sí está autorizada y esta experiencia se "
                      "vuelve el argumento de por qué hay que verificar todo lo que devuelve."},
            {"caso": "Equipos que encuentran que su solución ya existe, completa y gratis",
             "clave": "Es el mejor escenario pedagógico y hay que celebrarlo, no consolarlo. La "
                      "pregunta que reencuadra el proyecto: **¿y por qué la biblioteca / el negocio "
                      "/ el colegio no la está usando?** La respuesta —hay que administrarla, exige "
                      "capacitación, cuesta después del primer año, no funciona sin internet— **es "
                      "el problema real**, y suele ser más interesante que el original. El proyecto "
                      "no muere: se afila."},
            {"caso": "Equipos que no encuentran absolutamente nada",
             "clave": "Casi siempre es un problema de términos, no de vacío. Dos intervenciones "
                      "rápidas que funcionan: pedirles el término en inglés, y pedirles **el término "
                      "técnico del dominio** —como OPAC en el caso de la biblioteca—, que se "
                      "consigue mirando cómo se llama a sí mismo el sector. Si de verdad no hay "
                      "nada, hágalos escribir bien el bloque de lo que no encontraron: es un "
                      "hallazgo y se califica igual."},
            {"caso": "Proyectos de proceso o gestión, sin software de referencia",
             "clave": "Los antecedentes no tienen que ser software. Sirven manuales de procedimiento, "
                      "guías de entidades públicas, normas técnicas y trabajos de grado de "
                      "administración o ingeniería industrial. La operación más productiva para "
                      "estos casos suele ser **ADAPTAR DE OTRO DOMINIO**: cómo lo resuelve un sector "
                      "distinto con el mismo problema."},
        ],
        "cierre": "Tres minutos y una idea que vale para toda la carrera: **nadie parte de cero, y "
                  "decirlo es una fortaleza.** Contraste las dos frases en voz alta, porque la "
                  "diferencia es lo que se califica en la sesión 15: «esto no existe» es una "
                  "apuesta; «existen estas tres soluciones, ninguna funciona sin computador en el "
                  "mostrador ni sin administrador, y nosotros resolvemos justamente eso» es una "
                  "posición defendible ante cualquier jurado. Repita la regla de integridad, que es "
                  "la más importante del curso en materia académica: **si no puede abrir el enlace "
                  "y ver el documento, no lo cite** — y recuerde que un asistente de IA devuelve "
                  "referencias con formato perfecto que pueden no existir. Cierre con el hallazgo "
                  "del caso modelo, porque es contraintuitivo y se recuerda: existe software libre "
                  "excelente que resuelve el problema completo desde hace veinte años, y no sirve "
                  "aquí; ver por qué un antecedente magnífico no aplica es de lo que está hecha la "
                  "ingeniería. Anuncie la sesión 10: se prototipa el alcance mínimo, y de lo que "
                  "ficharon hoy sale el diseño de las pantallas.",
        "conexion": "Hacia atrás: la **sesión 8** dejó la alternativa elegida, que es sobre lo que se "
                    "buscó hoy; la **sesión 6** dejó las restricciones, que son las que explican por "
                    "qué un antecedente excelente no aplica; las **sesiones 4 y 5** instalaron la "
                    "exigencia de citar fuente, año y alcance; la **sesión 3** ya había dicho que la "
                    "IA no responde por lo que dice. Hacia adelante: la **sesión 10** reusa el "
                    "diseño de pantallas que ficharon hoy; la **sesión 11** usa IA con la "
                    "verificación que hoy se practicó; la **sesión 13** usa la fuente normativa para "
                    "el impacto social; y el **informe final de la sesión 16** se construye sobre "
                    "estas tres fichas, la brecha y la propuesta de mejora.",
    },

    "errores": [
        {"dice": "Una referencia con autor, título, revista y año que no abre en ningún lado",
         "por_que": "Es el patrón exacto de una cita generada por un asistente: formato perfecto, documento inexistente. Es la falta más grave de un trabajo académico.",
         "pida": "Que abran el enlace en pantalla en ese momento. Lo que no abre, se reemplaza."},
        {"dice": "«Buscamos y no encontramos nada»",
         "por_que": "Sin términos ni sitios, no se puede verificar ni repetir: no es un hallazgo, es una excusa.",
         "pida": "Qué términos, en qué sitios, y qué fue lo más cercano que apareció. Escrito así, se califica igual que una fuente encontrada."},
        {"dice": "«Nuestra mejora es que será más fácil de usar y más moderna»",
         "por_que": "No se apoya en ninguna brecha escrita ni nombra ninguna operación: es un deseo, no una propuesta.",
         "pida": "Que señalen el campo «qué le falta» de una de sus fichas y digan cuál de las cuatro operaciones aplican sobre eso."},
        {"dice": "«Ya existe algo igual, entonces cambiamos de tema»",
         "por_que": "Cambiar de tema en la sesión 9 tira por la borda las sesiones 6, 7 y 8, y el problema nuevo llega sin análisis.",
         "pida": "«¿Y por qué no lo están usando?». La respuesta a eso casi siempre es el problema real, y es mejor que el original."},
        {"dice": "Tres fuentes sobre el tema en general, ninguna leída",
         "por_que": "Una bibliografía de adorno no aporta nada al diseño y se detecta con una sola pregunta.",
         "pida": "El campo «qué le falta para nuestro caso» de cada ficha. Sin haber leído, ese campo no se puede llenar."},
    ],

    "dudas": [
        {"p": "¿Cuántas fuentes hay que tener?",
         "r": "Hoy, tres, y al menos una académica o normativa. Y es a propósito: se califica que "
              "estén leídas y verificables, no que sean muchas. Dos fichas excelentes valen más que "
              "tres regulares, y una lista de diez sin leer vale menos que una bien fichada."},
        {"p": "¿Podemos citar en inglés si no entendemos bien todo?",
         "r": "Sí, y de hecho hay que buscar en inglés porque ahí está la mayoría de lo publicado. "
              "Use el traductor del navegador para leer y cite el original. Lo que no se puede es "
              "citar algo que no se entendió en absoluto: el campo «qué le falta para nuestro caso» "
              "no se puede llenar sin haber comprendido qué hace."},
        {"p": "¿Un video de YouTube o un blog sirven como fuente?",
         "r": "Depende de quién lo firma y de para qué se usa. La documentación oficial de un "
              "proyecto en un blog institucional sirve; un video sin autor identificable, no. Regla "
              "práctica: sirve para **aprender a hacer algo** y no sirve para **sustentar una "
              "afirmación**. Para sustentar, se busca la fuente primaria."},
        {"p": "¿Y si usamos IA solo para encontrar las fuentes y después las verificamos?",
         "r": "Eso es exactamente el uso correcto, y en la sesión 11 se practica formalmente. Hoy "
              "no se usa porque la sesión es sobre aprender a buscar, y quien empieza con el "
              "atajo no aprende el método. Pero la regla vale desde ya: **la IA puede darle pistas "
              "y términos; la fuente se abre, se lee y se cita usted.**"},
    ],

    "notas_operativas": [
        "Las cinco salas de grupo se crean **antes** de la sesión.",
        "**Ábrale los enlaces del documento de solución antes de la clase.** Las URL cambian; si "
        "alguna se cayó, úsela como ejemplo en vivo de por qué se anota la fecha de consulta.",
        "Haga escribir **la pregunta de búsqueda en el chat** antes de repartir salas, un equipo por "
        "línea. Son dos minutos y cambia la calidad de todo el taller.",
        "**Reparta la búsqueda dentro del equipo** (2 académico · 2 soluciones reales · 1 normas). "
        "Cinco personas buscando lo mismo producen una sola ficha.",
        "En las salas y en las exposiciones, **pida abrir el enlace en pantalla**. Es la única forma "
        "de cortar la cita inventada, y hacerlo en vivo enseña más que descontar en la nota.",
        "Hoy no se usa IA, y la razón hay que decirla: la sesión es sobre fuentes verificables y un "
        "asistente devuelve referencias plausibles inexistentes. En la **sesión 11** sí está "
        "autorizada, con verificación obligatoria.",
        "Si un equipo descubre que su solución ya existe completa, **no lo deje cambiar de tema**: "
        "pregúntele por qué no la están usando. Ahí está el proyecto afilado.",
    ],

    "ti_siguiente": {
        "tid": "Revisión bibliográfica — completar las tres fichas con los seis campos y **abrir cada "
               "enlace** para confirmar que sirve, anotando la fecha de consulta.",
        "ti": "Propuesta de mejora escrita en el documento del equipo: la brecha, la operación usada "
              "y por qué importa en su contexto. Máximo una página.",
        "adelanto": "**prototipado**: qué es un prototipo y qué no, los niveles de fidelidad, y por "
                    "qué el dibujo a mano da mejor retroalimentación que la pantalla terminada.",
        "aviso": "Para la sesión 10 traigan la propuesta de mejora escrita y el **alcance mínimo de "
                 "la sesión 8** a la vista. Se van a dibujar las tres pantallas o pasos del flujo "
                 "principal, y de las fichas de hoy sale el diseño.",
    },

    "cierre_titulo": "Nos vemos en la sesión 10",
    "cierre_frase": "Nadie parte de cero: lo que se cita se puede abrir, y lo que se mejora se puede señalar",
}


# =============================================================================
# CLASE 10 · Herramientas digitales aplicadas a la Ingenieria
# =============================================================================

TEMAS[10] = {
    "n": 10,
    "titulo": "Herramientas digitales aplicadas a la Ingeniería",
    "subtitulo": "Prototipar: el dibujo a mano recibe mejores críticas que la pantalla terminada",
    "hook": "Si les muestro un dibujo a lápiz, me dicen todo lo que está mal. "
            "Si les muestro una pantalla terminada, me dicen «está muy bonita». ¿Por qué?",
    "hook_lines": [
        "Porque nadie quiere destruir algo que parece costoso.",
        "Y por eso el primer prototipo se hace a propósito feo.",
    ],
    "objetivos": [
        "Distinguir un **prototipo** de una versión inacabada, y saber qué pregunta responde cada nivel de **fidelidad**.",
        "Dibujar las **tres pantallas o pasos** del flujo principal del proyecto, con textos reales.",
        "Diseñar el **estado vacío y el estado de error**, que es donde se cae la mayoría de los prototipos.",
        "Elegir la **herramienta según la pregunta** que se quiere responder, no según la que se conoce.",
    ],
    "agenda": {
        "Teoría y guía del docente": "Teoría — qué es un prototipo, fidelidad, cómo se dibuja una pantalla y qué herramienta usar",
        "Actividad en equipos": "Taller — las tres pantallas del flujo principal, en Excalidraw o draw.io",
        "Exposiciones": "5 equipos × 3 min — el flujo dibujado y el estado de error",
    },
    "herramienta_nota": "Hoy se prototipa en **Excalidraw** (que se ve dibujado a mano, y eso es una "
                        "ventaja) o en **diagrams.net (draw.io)** si el proyecto es un flujo o un "
                        "proceso. Las dos abren sin cuenta. **Google Slides** sirve como prototipo "
                        "navegable —una diapositiva por pantalla, enlazadas entre sí— y es el truco "
                        "más útil de la sesión. Hoy no se usa IA: dibujar el flujo es la parte del "
                        "diseño que hay que entender con las manos, y en la **sesión 11** la IA "
                        "entra a generar variantes sobre lo que hoy dibujen.",
    "avance_proyecto": "Prototipo de baja fidelidad del alcance mínimo: tres pantallas o pasos con "
                       "textos reales, estado vacío, estado de error y el guion de prueba",

    "teoria": [
        {
            "tipo": "cards",
            "titulo": "Qué es un prototipo y qué no",
            "cards": [
                ("Es una pregunta hecha objeto",
                 "Un prototipo se construye **para responder una pregunta concreta**: ¿la gente "
                 "entiende esta pantalla? ¿alcanza el tiempo? ¿el flujo tiene sentido? Sin pregunta "
                 "es una maqueta decorativa."),
                ("No es la versión 1 a medias",
                 "Una versión inacabada intenta ser el producto y falla. **Un prototipo no intenta "
                 "ser el producto**: puede ser papel, puede no tener datos reales, y aun así "
                 "responde la pregunta."),
                ("Es desechable, y eso lo libera",
                 "Se hace sabiendo que se va a tirar. Por eso se puede probar una idea rara sin "
                 "costo. **Un prototipo que da pesar tirar ya costó demasiado.**"),
                ("Se prueba con alguien ajeno",
                 "Un prototipo que solo vio el equipo no probó nada. Su única razón de existir es "
                 "que **una persona de afuera intente usarlo delante de ustedes**, y que ustedes se "
                 "queden callados."),
            ],
            "columns": 2,
        },
        {
            "tipo": "tabla",
            "titulo": "Niveles de fidelidad: qué se prueba con cada uno",
            "headers": ["Nivel", "Cómo se ve", "Qué pregunta responde", "Cuánto cuesta cambiarlo"],
            "rows": [
                ["**Baja**\n(papel, Excalidraw)",
                 "Cajas, líneas, letra a mano. Se nota que es un borrador.",
                 "¿El flujo tiene sentido? ¿La gente entiende qué hacer?",
                 "**Un minuto.** Se borra y se dibuja otra vez."],
                ["**Media**\n(draw.io, Slides enlazadas)",
                 "Pantallas ordenadas, con textos reales y navegación entre ellas.",
                 "¿Se puede completar la tarea sin ayuda? ¿Faltan pasos?",
                 "**Minutos.** Se mueve una caja, se cambia un enlace."],
                ["**Alta**\n(Canva, herramientas de diseño)",
                 "Se parece al producto final: colores, tipografías, íconos.",
                 "¿Se ve confiable? ¿La marca comunica lo que debe?",
                 "**Horas.** Y la gente ya no se atreve a criticarlo."],
                ["**Funcional**\n(algo que corre)",
                 "Funciona de verdad, aunque sea con datos de prueba.",
                 "¿Aguanta? ¿Es rápido? ¿Sirve en el celular viejo?",
                 "**Días.** Es la fase de construcción, no de prototipo."],
            ],
            "note": "En este curso el prototipo del corte 2 es de **baja o media** fidelidad. La alta "
                    "aparece en la sesión 14, solo para la presentación final.",
            "col_w": [1.7, 2.7, 2.9, 2.5],
        },
        {
            "tipo": "steps",
            "titulo": "Cómo se dibuja una pantalla que sirve",
            "steps": [
                ("1 · Escriba arriba para qué existe la pantalla", "Una frase: «aquí el usuario averigua si el libro está disponible». Si no se puede escribir, la pantalla hace dos cosas y hay que partirla."),
                ("2 · Un solo camino principal, visible", "Lo que la persona va a hacer el 90 % de las veces, grande y primero. Todo lo demás, más pequeño o más abajo."),
                ("3 · Textos reales, nunca relleno", "«Buscar título» y no «texto aquí». **Los textos falsos esconden los problemas**: el botón que no se sabe cómo llamar es un botón que no se sabe qué hace."),
                ("4 · Dibuje el estado vacío y el de error", "Qué se ve cuando no hay datos, cuando no se encuentra nada, cuando algo falla. **Es donde se cae casi todo prototipo.**"),
                ("5 · Diga qué pasa al tocar cada cosa", "Una flecha y una palabra por cada botón. Un botón sin destino escrito es una decisión que nadie tomó."),
            ],
            "sub": "Cinco pasos, tres pantallas. Si un paso no se puede cumplir, el problema está en el diseño y no en el dibujo",
        },
        {
            "tipo": "tabla",
            "titulo": "Qué herramienta usar, según la pregunta",
            "headers": ["Herramienta", "Para qué sirve de verdad", "Cuándo NO usarla"],
            "rows": [
                ["**Excalidraw**",
                 "Pantallas y esquemas de baja fidelidad. Se ve dibujado a mano **y eso es una "
                 "ventaja**: invita a criticar. Abre sin cuenta y se comparte con un enlace.",
                 "Cuando el proyecto es un proceso con decisiones y ramas: para eso hay algo mejor."],
                ["**diagrams.net (draw.io)**",
                 "Flujos, procesos, arquitecturas y diagramas con decisiones. Formas estándar y "
                 "conectores que se quedan pegados al mover las cajas.",
                 "Para diseñar cómo se ve una pantalla: queda rígido y frío."],
                ["**Google Slides**",
                 "**Prototipo navegable**: una diapositiva por pantalla y un enlace en cada botón "
                 "hacia la diapositiva de destino. En modo presentación se puede usar como si "
                 "funcionara. Es el truco más útil de esta sesión.",
                 "Cuando hace falta lógica real —cálculos, datos que cambian—: ahí ya es "
                 "construcción."],
                ["**Canva**",
                 "Fidelidad alta para la presentación final y para material que alguien externo va "
                 "a ver.",
                 "En un primer prototipo. Se ve tan terminado que la gente deja de criticarlo."],
                ["**Papel y una foto**",
                 "Lo más rápido que existe: se dibuja, se fotografía y se sube a la carpeta del "
                 "equipo. Perfectamente válido en este curso.",
                 "Si la foto sale ilegible o si el equipo no puede editarla después entre todos."],
            ],
            "note": "Todas abren en el navegador y **ninguna exige pago ni tarjeta**. La pregunta "
                    "para elegir no es «¿cuál sé usar?» sino **«¿qué quiero responder con esto?»**.",
            "col_w": [1.9, 4.2, 3.7],
        },
        {
            "tipo": "box",
            "titulo": "La paradoja de la fidelidad, y dos advertencias",
            "notas": [
                ("info",
                 "**Cuanto más terminado se ve un prototipo, peor retroalimentación recibe.** "
                 "Delante de un dibujo a lápiz la gente dice «esto no se entiende, ¿dónde busco?»; "
                 "delante de una pantalla con colores y tipografía dice «está muy bonita». Nadie "
                 "quiere destruir algo que parece haber costado mucho. Por eso el primer prototipo "
                 "se hace a propósito feo."),
                ("advertencia",
                 "**No pulan el prototipo: no es lo que se califica.** Se califica que el flujo se "
                 "entienda, que los textos sean reales y que existan el estado vacío y el de error. "
                 "Un equipo que gasta el taller eligiendo colores llega a la sesión 12 sin nada que "
                 "probar."),
                ("advertencia",
                 "**Si el prototipo lleva datos, que sean inventados.** Ningún nombre, cédula, "
                 "teléfono, dirección ni foto de una persona real, ni siquiera de ustedes mismos. "
                 "Es la regla del curso y es la Ley 1581 de 2012 de la sesión 4: los datos de "
                 "prueba se inventan."),
            ],
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada: la paradoja de la fidelidad",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "Este es uno de los hallazgos más útiles y menos intuitivos del diseño, y funciona "
                "perfectamente como gancho porque todos lo han vivido del otro lado: cuando a uno "
                "le muestran algo que parece terminado, le da pena criticarlo.",
                "El fenómeno es consistente: **delante de un dibujo a lápiz la gente dice «esto no "
                "se entiende, ¿dónde busco?»; delante de una pantalla con colores y tipografía dice "
                "«está muy bonita»**. La explicación es social, no técnica. Un dibujo comunica «esto "
                "es un borrador, opine»; una pantalla pulida comunica «esto costó trabajo, no lo "
                "destruya». Y hay un segundo efecto, sobre el propio equipo: cuanto más trabajo "
                "hay invertido en algo, más cuesta cambiarlo — eso ya lo vieron como curva del costo "
                "en la sesión 7, y aquí aparece en versión psicológica.",
                "La conclusión práctica hay que decirla como regla y no como curiosidad: **el primer "
                "prototipo se hace a propósito feo**. Excalidraw es la herramienta de la sesión "
                "justamente porque todo lo que se dibuja ahí se ve hecho a mano.",
                "Recoja las respuestas del muro y no revele la explicación de inmediato: deje que "
                "alguien la formule. Suele salir en dos o tres intentos, y sale mejor de ellos que "
                "del docente.",
            ],
        },
        {
            "titulo": "Qué es un prototipo: una pregunta hecha objeto",
            "slide": "{{slide:Qué es un prototipo}}",
            "cuerpo": [
                "La definición que hay que dejar instalada: **un prototipo es una pregunta hecha "
                "objeto**. Se construye para responder algo concreto —¿la gente entiende esta "
                "pantalla?, ¿alcanza el tiempo?, ¿el flujo tiene sentido?— y sin esa pregunta es "
                "una maqueta decorativa. Pídale a cada equipo, en la sala, que escriba la pregunta "
                "de su prototipo en una línea antes de dibujar nada.",
                "**No es la versión 1 a medias**, y esta distinción es la que más cuesta en primer "
                "semestre. Una versión inacabada intenta ser el producto y falla en el intento; un "
                "prototipo no intenta ser el producto, así que puede ser papel, puede no tener "
                "datos reales, puede no funcionar, y aun así responder la pregunta con precisión.",
                "**Es desechable, y eso lo libera.** Se hace sabiendo que se va a tirar, y por eso "
                "se puede probar una idea rara sin costo. La frase que conviene dejarles: **un "
                "prototipo que da pesar tirar ya costó demasiado.**",
                "Y el punto que amarra la sesión con la 8 y con la 12: **se prueba con alguien "
                "ajeno**. Un prototipo que solo vio el equipo no probó nada. Su única razón de "
                "existir es que una persona de afuera intente usarlo delante de ustedes **y que "
                "ustedes se queden callados** — el silencio del equipo es parte del método, no una "
                "cortesía.",
            ],
        },
        {
            "titulo": "Fidelidad: cada nivel responde una pregunta distinta",
            "slide": "{{slide:Niveles de fidelidad}}",
            "cuerpo": [
                "La tabla de fidelidad no es una escala de calidad, y hay que decirlo explícitamente "
                "porque el estudiante la va a leer como «de peor a mejor». **Es una escala de "
                "preguntas**: cada nivel responde una pregunta distinta y cuesta un orden de "
                "magnitud más cambiarlo que el anterior.",
                "**Baja fidelidad** —papel, Excalidraw— responde *¿el flujo tiene sentido?, ¿la "
                "gente entiende qué hacer?*, y se cambia en un minuto. **Media** —draw.io, "
                "diapositivas enlazadas— responde *¿se puede completar la tarea sin ayuda?, ¿faltan "
                "pasos?*, y se cambia en minutos. **Alta** —Canva, herramientas de diseño— responde "
                "*¿se ve confiable?*, cuesta horas, y tiene el efecto secundario de la paradoja: la "
                "gente deja de criticarlo. **Funcional** ya no es prototipo: es construcción, y "
                "responde *¿aguanta?, ¿sirve en el celular viejo?*.",
                "La regla del curso, que hay que dejar clara para que nadie pierda el fin de semana: "
                "**el prototipo del corte 2 es de baja o media fidelidad**. La alta aparece en la "
                "sesión 14, y solo para la presentación final. Un equipo que llega a la sesión 11 "
                "con una pantalla preciosa y sin estado de error entendió mal la sesión.",
                "Vale la pena conectarlo con la curva de la sesión 7: los niveles de fidelidad son "
                "esa misma curva vista desde el diseño. Prototipar en baja fidelidad es exactamente "
                "«descubrir el error en la fase donde cuesta un borrador».",
            ],
        },
        {
            "titulo": "Los cinco pasos de una pantalla, y el estado de error",
            "slide": "{{slide:Cómo se dibuja una pantalla que sirve}}",
            "cuerpo": [
                "Estos cinco pasos son el método operativo del taller y cada uno esconde una "
                "decisión de diseño.",
                "**Escribir arriba para qué existe la pantalla** parece trivial y es un filtro "
                "potente: si la frase no se puede escribir, la pantalla está haciendo dos cosas y "
                "hay que partirla. Es el equivalente, en diseño, del «problema en una frase» de la "
                "sesión 6.",
                "**Un solo camino principal, visible.** Lo que la persona va a hacer el 90 % de las "
                "veces va grande y primero; todo lo demás, más pequeño o más abajo. El error típico "
                "es la pantalla democrática, donde ocho opciones tienen el mismo tamaño y el usuario "
                "no sabe por dónde empezar.",
                "**Textos reales, nunca relleno.** Esta es la regla que más mejora los prototipos "
                "del curso y hay que insistir en ella: escribir «Buscar título» y no «texto aquí». "
                "La razón es profunda y conviene decirla: **los textos falsos esconden los "
                "problemas**. El botón que no se sabe cómo llamar es un botón que no se sabe qué "
                "hace, y con relleno ese vacío no se nota hasta que alguien lo usa.",
                "**Dibujar el estado vacío y el de error** es el paso que casi nadie hace y donde se "
                "cae la mayoría de los prototipos. ¿Qué se ve la primera vez, cuando no hay datos? "
                "¿Qué se ve cuando no se encuentra lo que se buscó? ¿Qué se ve cuando algo falla? "
                "Un prototipo que solo muestra el camino feliz no sirve para probar nada, porque en "
                "la vida real el camino feliz es la minoría de los casos. Aquí hay un puente con "
                "la sesión 8: la tarea (3) del plan de validación —«dígame qué haría si el libro que "
                "busca no aparece»— exige justamente esta pantalla.",
                "**Decir qué pasa al tocar cada cosa**: una flecha y una palabra por botón. Un botón "
                "sin destino escrito es una decisión que nadie tomó, y en la sesión 12 la va a "
                "tomar el usuario por ustedes, mal.",
            ],
        },
        {
            "titulo": "Elegir la herramienta por la pregunta, y las dos advertencias",
            "slide": "{{slide:Qué herramienta usar}} {{slide:La paradoja de la fidelidad}}",
            "cuerpo": [
                "La tabla de herramientas hay que recorrerla rápido, con la idea que la ordena: **la "
                "pregunta para elegir no es «¿cuál sé usar?» sino «¿qué quiero responder con "
                "esto?»**. Es la misma lógica de la matriz de la sesión 8 aplicada a herramientas.",
                "**Excalidraw** para pantallas de baja fidelidad, y su apariencia de dibujo a mano "
                "es una ventaja funcional, no un defecto estético. **draw.io** para flujos, procesos "
                "y diagramas con decisiones —los equipos con proyectos de gestión trabajan aquí—; "
                "sus conectores se quedan pegados al mover las cajas, que es exactamente lo que se "
                "necesita cuando el flujo cambia diez veces.",
                "**Google Slides como prototipo navegable es el truco más útil de la sesión y hay "
                "que demostrarlo en vivo, no describirlo**: una diapositiva por pantalla, y en cada "
                "botón un enlace hacia la diapositiva de destino. En modo presentación se recorre "
                "como si funcionara. Con eso un equipo de primer semestre puede probar un flujo "
                "completo con un usuario real sin escribir una línea de código. Dedíquele dos "
                "minutos de pantalla compartida: es lo que más van a agradecer.",
                "**Canva** queda reservado para la sesión 14 y para material que verá alguien "
                "externo. Y **papel con una foto** es perfectamente válido en este curso: es lo más "
                "rápido que existe y hay que decirlo, porque hay equipos que se paralizan buscando "
                "la herramienta perfecta.",
                "Las dos advertencias del cierre son operativas. **No pulir el prototipo**: se "
                "califica que el flujo se entienda, que los textos sean reales y que existan el "
                "estado vacío y el de error; un equipo que gasta el taller eligiendo colores llega "
                "a la sesión 12 sin nada que probar. Y **si el prototipo lleva datos, que sean "
                "inventados**: ningún nombre, cédula, teléfono, dirección ni foto de una persona "
                "real, ni de ellos mismos. Es la regla del curso y es la Ley 1581 de 2012 de la "
                "sesión 4 aplicada al lugar donde de verdad se incumple — los datos de prueba se "
                "inventan.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:10 · Apertura · [Slide 4]",
            "cuerpo": [
                "Comparta pantalla antes de que entre el primero:",
                "> «Si les muestro un dibujo a lápiz, me dicen todo lo que está mal. Si les muestro "
                "una pantalla terminada, me dicen «está muy bonita». ¿Por qué?»",
                "**[Nota docente]:** no dé la explicación. Deje que la formule alguien del grupo: "
                "sale en dos o tres intentos y sale mejor de ellos.",
                "**[Nota docente]:** pida que abran el **alcance mínimo de la sesión 8** y la "
                "**propuesta de mejora de la sesión 9**. Hoy se dibuja eso, no una idea nueva.",
            ],
        },
        {
            "titulo": "00:10–00:55 · Teoría · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]",
            "cuerpo": [
                "Reparto sugerido de los 45 min:",
                "- **8 min** · Qué es un prototipo [Slide 5]. La frase que se queda: **un prototipo "
                "que da pesar tirar ya costó demasiado**.",
                "- **9 min** · Niveles de fidelidad [Slide 6]. Diga explícitamente que **no es una "
                "escala de calidad sino de preguntas**, y fije la regla: baja o media en el corte 2.",
                "- **12 min** · Los cinco pasos [Slide 7]. Es la diapositiva del taller. **Dedique "
                "la mitad al paso 4**, el estado vacío y el de error.",
                "- **10 min** · Qué herramienta usar [Slide 8]. **Demuestre en vivo el prototipo "
                "navegable en Google Slides** (dos minutos de pantalla compartida): una diapositiva "
                "por pantalla, un enlace en cada botón, modo presentación.",
                "- **6 min** · La paradoja y las advertencias [Slide 9]. No omita la de datos "
                "inventados.",
                "**[Nota docente]:** si va retrasado, recorte fidelidad a 5 minutos. **No recorte el "
                "paso 4 ni la demostración de Slides**: son las dos cosas que cambian los "
                "entregables.",
            ],
        },
        {
            "titulo": "00:55–01:12 · Taller en salas de grupo · [Slide 10]",
            "cuerpo": [
                "**2 min** para abrir Excalidraw o draw.io. Reparto sugerido: **dos dibujan, dos "
                "escriben los textos reales, uno escribe el guion de prueba**. Nadie mira sin hacer "
                "nada.",
                "**15 min** en salas. Entre a las cinco con **una sola pregunta: ¿qué se ve cuando "
                "no se encuentra nada?** Es el estado de error y falta siempre.",
                "**[Nota docente]:** corte en caliente a quien esté eligiendo colores o buscando "
                "íconos. Dígalo sin rodeos: eso no se califica hoy y les está costando la sesión 12.",
                "**[Nota docente]:** si un equipo tiene proyecto de proceso sin pantallas, las «tres "
                "pantallas» son **tres pasos del proceso o el formato que se va a llenar**. Los "
                "cinco pasos aplican igual.",
            ],
        },
        {
            "titulo": "01:12–01:27 · Exposiciones · [Slide 11]",
            "cuerpo": [
                "5 equipos × 3 min con el prototipo compartido. **El minuto obligatorio es «qué se "
                "ve cuando algo falla o no hay datos»**.",
                "**[Nota docente]:** los cinco enlaces en el chat antes de arrancar.",
                "**[Nota docente]:** haga una pregunta de usuario a cada equipo mientras exponen "
                "—«soy la voluntaria y no sé qué es esto, ¿qué toco?»—. Diez segundos, y es la mejor "
                "preparación posible para la sesión 12.",
                "**[Nota docente]:** anote qué le falta a cada prototipo. En la sesión 11 se corrige "
                "exactamente eso, con IA y a mano.",
            ],
        },
        {
            "titulo": "01:27–01:30 · Cierre · [Slide 12][Slide 13]",
            "cuerpo": [
                "Una idea: **el prototipo no es una maqueta, es una pregunta.** Y se hace feo a "
                "propósito, para que la gente se atreva a decir lo que está mal.",
                "Recuerde: textos reales, estado de error, datos inventados.",
                "Anuncie la sesión 11: **prototipo v2 con IA**, y **cierra el corte 2** con la "
                "evaluación en ExamLab sobre las sesiones 7 a 11.",
            ],
        },
    ],

    "taller": {
        "archivo": "Prototipo de baja fidelidad",
        "titulo": "Prototipo de baja fidelidad",
        "min": 17,
        "exposicion": 3,
        "consigna": "Dibujen el **flujo principal del alcance mínimo** en tres pantallas o tres pasos: "
                    "cada una con su frase de propósito, un solo camino principal, **textos reales**, "
                    "el **estado vacío y el de error**, y una flecha con destino por cada botón. "
                    "Después escriban el **guion de prueba** con tres tareas.",
        "entregable": "el prototipo de tres pantallas en Excalidraw o draw.io (PNG en la carpeta del "
                      "equipo) y el guion de prueba en el documento del equipo",
        "entregable_corto": "prototipo de tres pantallas + guion de prueba con tres tareas",
        "reparto_titulo": "Reparto sugerido dentro del equipo:",
        "reparto": "**dos personas dibujan**, **dos escriben los textos reales** —los rótulos de los "
                   "botones y los mensajes—, y **una escribe el guion de prueba** a partir de los "
                   "criterios de aceptación de la sesión 7. A los 12 minutos se juntan y revisan que "
                   "cada botón tenga destino. Se dibuja el **alcance mínimo de la sesión 8**, no una "
                   "idea nueva.",
        "reparto_corto": "2 dibujan · 2 escriben textos · 1 escribe el guion de prueba",
        "bloques": [
            {"clave": "EL FLUJO EN TRES PASOS",
             "pide": "El camino principal del alcance mínimo, en tres pantallas o tres pasos, y **una "
                     "frase de propósito por cada uno**.",
             "check": "cada frase describe una sola cosa. Si una pantalla necesita «y» para explicarse, hace dos cosas y hay que partirla."},
            {"clave": "LAS TRES PANTALLAS DIBUJADAS",
             "pide": "Las tres dibujadas de verdad, con el camino principal grande y primero, y una "
                     "**flecha con destino** por cada botón.",
             "check": "no hay ningún botón sin destino escrito, y se distingue a primera vista qué es lo principal."},
            {"clave": "EL ESTADO VACÍO Y EL DE ERROR",
             "pide": "Qué se ve la primera vez sin datos, qué se ve cuando la búsqueda no encuentra "
                     "nada, y qué se ve cuando algo falla. **Con el texto exacto del mensaje.**",
             "check": "los tres existen y el mensaje dice qué hacer, no solo que hubo un error."},
            {"clave": "LOS TEXTOS REALES",
             "pide": "Todos los rótulos y mensajes escritos como van a quedar. **Cero relleno**, "
                     "cero «texto aquí», cero «lorem ipsum».",
             "check": "no queda ningún texto de relleno. Un botón que no se supo cómo llamar es una función que no está definida."},
            {"clave": "EL GUION DE PRUEBA",
             "pide": "Tres tareas para pedirle a una persona ajena, salidas de los **criterios de "
                     "aceptación de la sesión 7**, y una de ellas sobre el caso en que el sistema "
                     "**no** tiene la respuesta.",
             "check": "las tres son tareas («averigüe si…»), no preguntas de opinión («¿le gusta?»), y una cubre el caso sin respuesta."},
        ],
        "expo": [
            ("30 s · El flujo", "Los tres pasos y para qué existe cada pantalla."),
            ("50 s · El camino principal", "Qué hace el usuario el 90 % de las veces, señalado en el dibujo."),
            ("50 s · Qué se ve cuando falla", "Estado vacío y de error, con el mensaje leído tal cual. Es el minuto obligatorio."),
            ("30 s · Los textos", "Dos rótulos que costó decidir y por qué quedaron así."),
            ("20 s · El guion de prueba", "Las tres tareas, y con qué rol van a probar."),
        ],
    },

    "rubrica": [
        ("El flujo son tres pasos con una frase de propósito por pantalla, cada una haciendo una sola cosa", 20,
         "Una pantalla que hace dos cosas confunde al usuario y esconde una decisión de diseño no tomada."),
        ("Las tres pantallas están dibujadas, con el camino principal destacado y cada botón con destino", 25,
         "Un botón sin destino es una decisión que va a tomar el usuario por ustedes, mal, en la sesión 12."),
        ("Existen el estado vacío y el de error, con el texto exacto del mensaje", 20,
         "El camino feliz es la minoría de los casos reales: un prototipo sin errores no prueba nada."),
        ("Todos los textos son reales, sin relleno", 15,
         "Los textos falsos esconden los problemas: el rótulo que no se sabe escribir es una función que no está definida."),
        ("El guion de prueba tiene tres tareas ejecutables y una cubre el caso sin respuesta", 20,
         "Es lo que hace posible la validación de la sesión 12: se pide hacer, no opinar."),
    ],

    "solucion": {
        "para_que": "Este documento trae el prototipo completo del caso de la biblioteca: las tres "
                    "pantallas descritas caja por caja, los textos exactos, el estado vacío y el de "
                    "error, y el guion de prueba. Su valor está en dos cosas que ningún equipo hace "
                    "solo: **los mensajes de error escritos con su texto exacto** y **la fecha de "
                    "última actualización visible en pantalla**, que es la consecuencia de diseño de "
                    "lo que se perdió al decidir en la sesión 8. Si el docente solo alcanza a leer "
                    "un bloque, que sea **EL ESTADO VACÍO Y EL DE ERROR**.",
        "caso_titulo": "La biblioteca del barrio · el prototipo de la lista de disponibilidad",
        "caso": "Alcance mínimo de la sesión 8: la lista de disponibilidad consultable por enlace, "
                "con una pantalla de consulta para el usuario y una de actualización para la "
                "voluntaria, funcionando desde un celular y sin cuenta. Propuesta de mejora de la "
                "sesión 9: publicar la disponibilidad **sin catalogar el acervo completo y sin "
                "administrar un sistema**, solo los títulos que se prestan. Requisitos no "
                "funcionales vigentes: sin computador en el mostrador, se aprende sin manual, menos "
                "de 200 KB por consulta.",
        "por_que_este_caso": "Porque el prototipo obliga a resolver visualmente el sacrificio que el "
                             "equipo aceptó en la sesión 8: la información no está al minuto. La "
                             "solución de diseño —mostrar en pantalla cuándo se actualizó por última "
                             "vez— es pequeña, evidente en retrospectiva, y ningún equipo la piensa "
                             "solo. Ver eso es ver cómo una decisión de la sesión 8 se convierte en "
                             "un elemento de interfaz en la 10.",
        "bloques": [
            {
                "clave": "EL FLUJO EN TRES PASOS",
                "respuesta": "**Pantalla 1 · Consultar.** *Aquí el usuario busca un título para saber "
                             "si está disponible.*\n\n"
                             "**Pantalla 2 · Resultado.** *Aquí el usuario ve si el título está "
                             "disponible, prestado o no está en la biblioteca.*\n\n"
                             "**Pantalla 3 · Actualizar (solo la voluntaria).** *Aquí la voluntaria "
                             "marca un título como prestado o como devuelto, al cerrar el día.*\n\n"
                             "Las tres frases tienen un solo verbo y un solo actor. Nótese que la "
                             "pantalla 2 contempla **tres resultados posibles** desde el enunciado "
                             "—disponible, prestado, no está—, y ese tercer caso es el que la "
                             "mayoría de los equipos descubre solo cuando un usuario lo encuentra.\n\n"
                             "**Ejemplo de frase mal escrita**, para contrastar: «aquí el usuario "
                             "busca un libro **y** la voluntaria registra el préstamo». Tiene una "
                             "«y» y dos actores: son dos pantallas, y juntarlas es el error que "
                             "obliga a la voluntaria y al usuario a compartir el mismo teléfono.",
                "como_calificar": "20 pts. La verificación es mecánica y rápida: **¿la frase de "
                                  "propósito necesita una «y»?** Si la necesita, la pantalla hace "
                                  "dos cosas y vale la mitad; hágalos partirla en la sala, toma dos "
                                  "minutos. Y verifique que el flujo sea el **alcance mínimo de la "
                                  "sesión 8** y no una idea nueva: si aparecieron funciones que "
                                  "estaban en la lista de «versión siguiente», el equipo se está "
                                  "saliendo del alcance que él mismo fijó, y eso hay que cortarlo "
                                  "hoy."
            },
            {
                "clave": "LAS TRES PANTALLAS DIBUJADAS",
                "respuesta": "**Pantalla 1 · Consultar** — de arriba abajo:\n\n"
                             "- Título: «Biblioteca del barrio · ¿está disponible?»\n"
                             "- **Un campo de texto grande**, con la indicación «Escriba el título o "
                             "el autor» — es el camino principal y ocupa el centro de la pantalla\n"
                             "- Botón grande: «Buscar» → *va a la pantalla 2*\n"
                             "- Debajo, en letra pequeña: «Lista actualizada el viernes a las 6:00 "
                             "p. m.»\n"
                             "- Enlace pequeño al pie: «Ver todos los títulos prestados» → *va a una "
                             "lista simple*\n\n"
                             "**Pantalla 2 · Resultado** — tres versiones dibujadas, porque son tres "
                             "estados distintos:\n\n"
                             "- *Disponible:* «**Cien años de soledad** — Disponible. Última "
                             "actualización: viernes 6:00 p. m.» + botón «Buscar otro» → *vuelve a "
                             "la 1*\n"
                             "- *Prestado:* «**Cien años de soledad** — Prestado. Se esperaba de "
                             "vuelta el lunes.» + «Buscar otro»\n"
                             "- *No está:* «No encontramos «Cien años de soledad» en la lista. Puede "
                             "que no esté en la biblioteca o que no esté registrado.» + «Buscar "
                             "otro»\n\n"
                             "**Pantalla 3 · Actualizar (voluntaria)** — de arriba abajo:\n\n"
                             "- Título: «Actualizar la lista»\n"
                             "- Lista de los títulos registrados, cada uno con **un solo botón que "
                             "alterna**: «Marcar prestado» / «Marcar devuelto» → *cambia el estado "
                             "en la misma pantalla*\n"
                             "- Campo pequeño abajo: «Agregar un título que no está en la lista» + "
                             "botón «Agregar»\n"
                             "- Botón grande al final: «Publicar cambios» → *muestra «Lista "
                             "publicada. Los usuarios ya ven la información nueva.»*\n\n"
                             "**Dos decisiones de diseño que hay que señalar en clase, porque son "
                             "las que salvan el proyecto:**\n\n"
                             "1. **La fecha de última actualización aparece en las dos pantallas del "
                             "usuario.** No es un detalle estético: es la manera de ser honesto con "
                             "el sacrificio que el equipo aceptó en la sesión 8 —la información no "
                             "está al minuto—. Si el usuario ve «actualizada el viernes a las 6:00 "
                             "p. m.», puede decidir por sí mismo si vale la pena el viaje. **Sin "
                             "esa línea, la solución miente por omisión.**\n"
                             "2. **Un solo botón que alterna** en la pantalla de la voluntaria, en "
                             "vez de dos botones separados: menos decisiones, menos errores, y "
                             "cumple el requisito no funcional «se aprende sin manual».",
                "como_calificar": "25 pts. Tres verificaciones: (a) **¿cada botón tiene destino "
                                  "escrito?** Un botón huérfano es una decisión no tomada; reste 3 "
                                  "por cada uno; (b) **¿se distingue a primera vista qué es lo "
                                  "principal?** Si las ocho cosas tienen el mismo tamaño, es la "
                                  "«pantalla democrática» y vale 12; (c) que estén **las tres "
                                  "pantallas dibujadas**, no descritas en texto. Dé puntos extra "
                                  "informales —dígalo en la retroalimentación— al equipo que "
                                  "resuelva un estado visible de honestidad como la fecha de "
                                  "actualización: casi ninguno lo hace y es la marca de un buen "
                                  "diseñador."
            },
            {
                "clave": "EL ESTADO VACÍO Y EL DE ERROR",
                "respuesta": "**Estado vacío** (la primera vez, o cuando no hay nada registrado):\n\n"
                             "> «Todavía no hay títulos en la lista. La biblioteca la está armando: "
                             "por ahora, pregunte en el mostrador.»\n\n"
                             "**Búsqueda sin resultados** (el caso más frecuente y el más "
                             "olvidado):\n\n"
                             "> «No encontramos «Cien años de soledad» en la lista. Puede que no "
                             "esté en la biblioteca o que no esté registrado. **Pregunte en el "
                             "mostrador o intente con el nombre del autor.**»\n\n"
                             "**Error** (no carga, no hay conexión):\n\n"
                             "> «No pudimos cargar la lista. Revise su conexión e intente otra vez. "
                             "**Si no funciona, la biblioteca abre de 2 a 6 p. m.**»\n\n"
                             "**Y un cuarto estado que casi nadie dibuja y que este caso exige: "
                             "información vieja.**\n\n"
                             "> «Esta lista se actualizó hace 3 días. Puede estar desactualizada.»\n\n"
                             "**Lo que hace buenos a estos mensajes**, y es lo que hay que enseñar: "
                             "los cuatro **dicen qué hacer**, no solo que algo salió mal. Compare "
                             "con las versiones malas, que son las que van a escribir los equipos: "
                             "«Error», «No hay resultados», «Sin datos», «Ha ocurrido un problema». "
                             "Todas informan y ninguna ayuda. La regla en una línea: **un mensaje de "
                             "error sin una salida es una puerta cerrada con un letrero.**\n\n"
                             "Nótese además que dos de los cuatro mensajes mandan al usuario **fuera "
                             "del sistema** —al mostrador, al horario de la biblioteca—. Eso es "
                             "correcto y hay que decirlo: la solución no tiene que resolver todo, "
                             "tiene que no dejar tirada a la persona.",
                "como_calificar": "20 pts, y es el bloque que más diferencia. Se califica que **los "
                                  "tres estados existan dibujados** (12 pts) y que **cada mensaje "
                                  "diga qué hacer** (8 pts). «Error» o «No hay resultados» a secas "
                                  "vale 2 en ese estado: hágalos reescribir uno en la sala, en voz "
                                  "alta, y los otros salen solos. Valore especialmente el estado de "
                                  "información desactualizada si el proyecto lo necesita: es el "
                                  "puente entre la decisión de la sesión 8 y la interfaz, y es lo "
                                  "que separa un prototipo honesto de uno que oculta su limitación."
            },
            {
                "clave": "LOS TEXTOS REALES",
                "respuesta": "Los rótulos que costó decidir, con el porqué —esta es la parte que "
                             "conviene leer en voz alta en clase:\n\n"
                             "- **«¿está disponible?»** en el título, en vez de «Sistema de gestión "
                             "de préstamos». El usuario no viene a gestionar nada: viene a saber si "
                             "vale la pena caminar.\n"
                             "- **«Escriba el título o el autor»** en vez de «Buscar». La primera "
                             "dice qué escribir; la segunda deja al usuario adivinando si acepta "
                             "temas, códigos o solo títulos exactos.\n"
                             "- **«Marcar prestado» / «Marcar devuelto»** en vez de «Editar estado». "
                             "La voluntaria no piensa en estados: piensa en que alguien se llevó un "
                             "libro.\n"
                             "- **«Publicar cambios»** en vez de «Guardar». «Guardar» no dice si "
                             "alguien más ya lo ve; «publicar» sí, y en esta solución esa diferencia "
                             "es justamente el momento en que la información se vuelve pública.\n"
                             "- **«Se esperaba de vuelta el lunes»** en vez de «Fecha de "
                             "vencimiento: lunes». El segundo es lenguaje de sistema; el primero es "
                             "lenguaje de persona, y además admite honestamente que es una "
                             "expectativa y no una certeza.\n\n"
                             "**Lo que revela este bloque:** al escribir «Publicar cambios» el equipo "
                             "descubrió una decisión que no había tomado —¿los cambios se ven de "
                             "inmediato o hay un momento de publicación?—. **Eso es exactamente lo "
                             "que hacen los textos reales**: obligan a decidir lo que el relleno "
                             "permite postergar. Si hubieran escrito «botón aquí», la pregunta no "
                             "habría aparecido hasta la sesión 12, con un usuario delante.",
                "como_calificar": "15 pts. Verificación literal: **recorra el dibujo buscando "
                                  "«texto», «botón», «aquí va», «lorem ipsum»**. Cada uno resta 4. Y "
                                  "haga la pregunta que enseña: «¿por qué este botón se llama "
                                  "así?». Si no saben responder, ese botón no tiene función "
                                  "definida, y eso es un hallazgo más valioso que la nota. Valore "
                                  "mucho al equipo que cuente que un texto los obligó a tomar una "
                                  "decisión que no habían tomado: entendió el punto entero de la "
                                  "diapositiva."
            },
            {
                "clave": "EL GUION DE PRUEBA",
                "respuesta": "**Con quién:** la coordinadora (rol de voluntaria) y dos usuarios "
                             "reales en la puerta de la biblioteca. **Ninguno del equipo** —viene "
                             "del plan de validación de la sesión 8.\n\n"
                             "**Las tres tareas**, derivadas de los criterios de aceptación de la "
                             "sesión 7:\n\n"
                             "1. *«Averigüe si el libro X está disponible.»* — mide el criterio «en "
                             "menos de un minuto, sin ayuda».\n"
                             "2. *«Acaba de prestar el libro X. Déjelo registrado.»* (a la "
                             "voluntaria) — mide «en menos de 30 segundos, sin manual».\n"
                             "3. *«Busque un libro que sabemos que no está en la lista. Dígame qué "
                             "haría ahora.»* — **es la tarea del caso sin respuesta**, y la más "
                             "valiosa: prueba el estado de error, que es donde se cae todo.\n\n"
                             "**Qué se observa, sin intervenir:** cuánto tarda · dónde duda · qué "
                             "toca por error · qué busca y no encuentra · si termina sin ayuda · **y "
                             "si se da cuenta de que la información puede estar desactualizada** "
                             "(¿lee la fecha?).\n\n"
                             "**Las reglas del que aplica la prueba**, que hay que escribir en el "
                             "guion porque en el momento se olvidan:\n\n"
                             "- No explicar nada antes. Se entrega y se dice la tarea.\n"
                             "- **No ayudar**, aunque duela. El silencio incómodo es el dato.\n"
                             "- No preguntar «¿le gusta?» ni «¿se entiende?». Se pregunta «¿qué "
                             "está pensando?» mientras lo hace.\n"
                             "- Al final, una sola pregunta abierta: «¿qué esperaba que pasara y no "
                             "pasó?».\n"
                             "- **Se anota lo que hizo, no lo que opinó.**\n\n"
                             "Y la regla de datos del curso: en las notas de la prueba se escribe el "
                             "**rol** —«usuaria 1», «voluntaria»—, nunca el nombre, el teléfono ni "
                             "la foto de la persona.",
                "como_calificar": "20 pts. Tres verificaciones: (a) **¿son tareas o son preguntas de "
                                  "opinión?** «¿Le parece claro?» no es una tarea: reste a la mitad; "
                                  "(b) **¿hay una tarea sobre el caso sin respuesta?** Vale 7 de los "
                                  "20 por sí sola, porque es la que prueba el estado de error; (c) "
                                  "**¿la persona es ajena al equipo?** Si planean probar entre "
                                  "ellos, corríjalo hoy — es la trampa de la sesión 8 reapareciendo "
                                  "y arruina la sesión 12. Valore que estén escritas las reglas del "
                                  "que aplica la prueba: sin ellas, el equipo ayuda al usuario sin "
                                  "darse cuenta y la prueba no mide nada."
            },
        ],
        "variantes": [
            {"caso": "Equipos que se ponen a elegir colores, íconos y tipografías",
             "clave": "Es el desperdicio de taller más común de esta sesión. Córtelo en caliente y "
                      "con el argumento, no con la orden: la paradoja de la fidelidad dice que "
                      "cuanto más terminado se vea, menos crítica útil van a recibir en la sesión "
                      "12, así que **pulir hoy es perder información mañana**. Redirija con la "
                      "pregunta del estado de error, que es lo que les falta."},
            {"caso": "Proyectos de proceso o gestión, sin pantallas",
             "clave": "Las «tres pantallas» son **tres pasos del proceso** o **el formato que "
                      "alguien va a llenar**, y draw.io es la herramienta. Los cinco pasos aplican "
                      "igual, incluido el estado de error: en un proceso, el estado de error es "
                      "**qué pasa cuando el paso anterior no se hizo** o cuando falta un dato, y es "
                      "exactamente donde fallan los procesos en la vida real. El guion de prueba es "
                      "el mismo: una persona ajena ejecuta el proceso siguiendo solo el formato."},
            {"caso": "Equipos que dibujan solo el camino feliz",
             "clave": "Va a pasar en la mayoría. La intervención de tres segundos que funciona: "
                      "entre a la sala, señale el campo de búsqueda y diga «busco un libro que no "
                      "existe, ¿qué veo?». El silencio que sigue es la clase. Hágalos dibujar ese "
                      "estado ahí mismo, y los otros dos salen por sí solos."},
            {"caso": "Equipos que quieren usar una herramienta de prototipado profesional que no está en la lista",
             "clave": "Se permite **si es gratuita, si abre en el navegador y si no pide tarjeta** — "
                      "esa es la regla del curso y no se negocia. Pero adviértales el riesgo real: "
                      "aprender la herramienta se les va a comer el tiempo de diseñar, y lo que se "
                      "califica es el diseño. Si a los cinco minutos no tienen nada dibujado, "
                      "mándelos a papel y una foto: es un entregable perfectamente válido."},
        ],
        "cierre": "Tres minutos y una idea que hay que dejar bien plantada: **el prototipo no es una "
                  "maqueta, es una pregunta**, y se hace feo a propósito para que la gente se atreva "
                  "a decir lo que está mal. Repita las tres exigencias concretas, porque son las que "
                  "van a definir la nota y la calidad de la sesión 12: textos reales, estado de "
                  "error con salida, datos inventados. Vale la pena cerrar con el hallazgo del caso "
                  "modelo, que es pequeño y memorable: la línea «lista actualizada el viernes a las "
                  "6:00 p. m.» es la manera de ser honesto en la interfaz con el sacrificio que el "
                  "equipo aceptó en la sesión 8 — sin esa línea, la solución miente por omisión, y "
                  "con ella el usuario decide por sí mismo si vale la pena el viaje. Es una decisión "
                  "de diseño de dos segundos que nace de un análisis de dos sesiones atrás, y esa "
                  "cadena es lo que se está enseñando. Anuncie la sesión 11: prototipo v2 con IA "
                  "autorizada, con entrega del prompt y de las correcciones, y **cierra el corte 2** "
                  "con la evaluación en ExamLab sobre las sesiones 7 a 11.",
        "conexion": "Hacia atrás: la **sesión 8** fijó el alcance mínimo que hoy se dibuja y el plan "
                    "de validación que hoy se convierte en guion; la **sesión 9** aportó el diseño de "
                    "pantalla que se reusa de los antecedentes; la **sesión 7** dejó los criterios de "
                    "aceptación, que son las tareas de la prueba; la **sesión 4** dejó la Ley 1581, "
                    "que es la regla de datos inventados. Hacia adelante: la **sesión 11** genera "
                    "variantes de estas pantallas con IA y corrige a mano; la **sesión 12** ejecuta "
                    "este guion con una persona ajena; la **sesión 14** sube la fidelidad solo para "
                    "la presentación; y el **informe final** documenta la evolución del prototipo.",
    },

    "errores": [
        {"dice": "Un prototipo con «texto aquí» y botones sin nombre",
         "por_que": "El relleno esconde los problemas: un botón que no se supo cómo llamar es una función que no está definida.",
         "pida": "Los rótulos reales, y la pregunta «¿por qué este botón se llama así?» para cada uno."},
        {"dice": "Solo el camino feliz, sin búsqueda vacía ni error",
         "por_que": "En la vida real el camino feliz es la minoría de los casos, así que el prototipo no prueba nada.",
         "pida": "«Busco algo que no existe, ¿qué veo?». Que lo dibujen en la sala, con el mensaje exacto."},
        {"dice": "«Error» o «No hay resultados» como mensaje",
         "por_que": "Informa que algo salió mal y no ofrece salida: es una puerta cerrada con un letrero.",
         "pida": "Un mensaje que diga **qué hacer ahora**, aunque la salida sea fuera del sistema."},
        {"dice": "Media hora eligiendo colores y tipografías",
         "por_que": "La fidelidad alta reduce la crítica útil: pulir hoy es perder información en la sesión 12.",
         "pida": "El estado de error y los textos reales. Los colores, en la sesión 14."},
        {"dice": "Datos de personas reales en el prototipo, «porque es solo de prueba»",
         "por_que": "Es tratamiento de datos personales sin autorización: la Ley 1581 de 2012 no distingue entre prueba y producción.",
         "pida": "Datos inventados, siempre. Y en las notas de la prueba, el rol y no el nombre."},
    ],

    "dudas": [
        {"p": "¿Tiene que estar hecho en computador?",
         "r": "No. **Papel y una foto es un entregable válido en este curso**, y a veces es el mejor: "
              "es lo más rápido y lo que más crítica útil recibe. La única condición es que la foto "
              "sea legible y que el equipo pueda seguir editándolo después entre todos."},
        {"p": "¿Tres pantallas no son muy pocas?",
         "r": "Son las del **flujo principal del alcance mínimo**, y son suficientes para probar si "
              "la idea funciona. Un prototipo de doce pantallas en la sesión 10 significa que el "
              "alcance mínimo de la sesión 8 quedó mal definido, o que el equipo va a llegar a la "
              "12 sin haber probado nada con nadie."},
        {"p": "¿Podemos usar una herramienta de prototipado profesional?",
         "r": "Sí, si es gratuita, abre en el navegador y no pide tarjeta — esa es la regla del "
              "curso. Pero cuidado con el tiempo: aprender la herramienta se come el tiempo de "
              "diseñar, y lo que se califica es el diseño. Si a los cinco minutos no tienen nada "
              "dibujado, pásense a papel."},
        {"p": "¿El prototipo tiene que funcionar?",
         "r": "No, y ahí está la ventaja. Un prototipo navegable en Google Slides —una diapositiva "
              "por pantalla, un enlace en cada botón— se puede poner en manos de un usuario real y "
              "recorrer como si funcionara, sin una línea de código. Con eso se responde casi todo "
              "lo que hace falta responder en el corte 2."},
    ],

    "notas_operativas": [
        "Las cinco salas de grupo se crean **antes** de la sesión.",
        "**Demuestre en vivo el prototipo navegable en Google Slides** (dos minutos de pantalla "
        "compartida): una diapositiva por pantalla, un enlace en cada botón, modo presentación. Es "
        "lo que más van a usar.",
        "Pida que abran el **alcance mínimo de la sesión 8** en la apertura. Hoy se dibuja eso; si "
        "aparecen funciones de la lista de «versión siguiente», hay que cortarlo.",
        "En las salas, la pregunta única es **«¿qué se ve cuando no se encuentra nada?»**. El estado "
        "de error falta siempre y vale 20 puntos.",
        "**Corte en caliente a quien esté eligiendo colores.** Use el argumento de la paradoja de la "
        "fidelidad, no la orden: pulir hoy es perder crítica útil en la sesión 12.",
        "Haga **una pregunta de usuario a cada equipo durante su exposición** —«soy la voluntaria y "
        "no sé qué es esto, ¿qué toco?»—. Diez segundos y es el mejor ensayo para la sesión 12.",
        "**Anote qué le falta a cada prototipo.** En la sesión 11 se corrige exactamente eso, y la "
        "lista permite verificar si el equipo corrigió o solo generó variantes nuevas.",
        "Repita la regla de datos: **inventados siempre**, ni siquiera los propios. Es donde de "
        "verdad se incumple la Ley 1581 en trabajos de estudiantes.",
        "**Publique hoy** el documento «Evaluación del Corte 2 — cómo prepararse» (está con el "
        "material de la sesión 11) y subraye una cosa en el cierre: esa evaluación es **a libro "
        "abierto sobre los documentos del propio equipo**, y cuatro preguntas valen 49 de los 100 "
        "puntos copiando de ahí. El equipo que llegue sin sus documentos abiertos no las puede "
        "responder, y avisarlo hoy es lo que hace justa esa regla. Las preguntas y la clave están "
        "en el Kit docente de la sesión 11: **esos dos no se comparten**.",
    ],

    "ti_siguiente": {
        "tid": "Introducción a software de prototipado — terminar las tres pantallas con **todos** "
               "los textos reales y los tres estados dibujados, y dejar el PNG en la carpeta del "
               "equipo.",
        "ti": "Práctica básica con herramientas digitales: convertir el prototipo en **navegable** "
              "—diapositivas enlazadas o enlaces entre marcos— para poder recorrerlo delante de una "
              "persona.",
        "adelanto": "**prototipo v2 con IA autorizada**: generar variantes, elegir con criterio y "
                    "corregir lo que la IA no sabía. Y la **evaluación del corte 2** en ExamLab, "
                    "sobre las sesiones 7 a 11.",
        "aviso": "La sesión 11 **cierra el corte 2**: hay 20 minutos de evaluación al final, sobre "
                 "las sesiones 7 a 11. Traigan el prototipo terminado y navegable — sin él no hay "
                 "nada que corregir con IA, y ese es el entregable de la sesión. La evaluación es "
                 "**a libro abierto sobre los documentos de su equipo**: lean el documento "
                 "«Evaluación del Corte 2 — cómo prepararse», que dice exactamente qué pestañas "
                 "tener abiertas.",
    },

    "cierre_titulo": "Nos vemos en la sesión 11",
    "cierre_frase": "Un prototipo no es una maqueta: es una pregunta, y por eso se hace feo a propósito",
}


# =============================================================================
# CLASE 11 · Taller de prototipado inicial con IA · CIERRA EL CORTE 2
# =============================================================================
# Sesion con reparto de tiempo propio: la evaluacion de corte se aplica al final,
# despues de las exposiciones, porque cubre las sesiones 7 a 11 completas.
# Es la segunda y ultima sesion con asistente de IA autorizado (la otra es la 3).

TEMAS[11] = {
    "n": 11,
    "titulo": "Taller de prototipado inicial con IA",
    "subtitulo": "La IA propone, ustedes deciden — y lo que corrigieron es lo que se califica",
    "hook": "Le pedí a un asistente que mejorara el prototipo de la biblioteca. "
            "Me devolvió algo mejor... y además ilegal. ¿Cómo puede pasar eso?",
    "hook_lines": [
        "Propuso crear cuentas de usuario y enviar avisos por correo.",
        "Nadie le dijo que el proyecto no puede pedir datos personales.",
    ],
    "objetivos": [
        "Escribir un **prompt con contexto**: problema, actores y **restricciones** del proyecto.",
        "Pedir **variantes** en vez de una respuesta, y elegir una con criterio propio.",
        "Detectar y **corregir lo que la IA no podía saber**: el contexto local y las restricciones.",
        "Dejar **trazabilidad del uso de IA**: el prompt, lo corregido y lo descartado.",
    ],
    "agenda_slots": [
        ("Apertura", 8, "Pregunta de entrada en el muro"),
        ("Teoría y guía del docente", 17, "Qué hace bien y qué mal la IA, cómo se le pide y cómo se corrige"),
        ("Actividad en equipos", 27, "Prototipo v2 con IA, en salas de grupo"),
        ("Exposiciones", 15, "5 equipos × 3 min — lo que corrigieron a mano"),
        ("Evaluación de corte 2", 20, "En ExamLab · cubre las sesiones 7 a 11"),
        ("Cierre", 3, "Qué queda amarrado para el corte 3"),
    ],
    "agenda_sub": "Hoy cierra el corte 2: la evaluación va al final, después de las exposiciones, "
                  "porque cubre las cinco sesiones completas",
    "nota_bloque": "**Esta sesión cierra el corte 2 (30 %).** La teoría baja a 17 minutos y la "
                   "actividad a 27 para que quepan los **20 minutos de evaluación** al final, en "
                   "ExamLab, sobre las sesiones 7 a 11. Es además la **segunda y última sesión con "
                   "asistente de IA autorizado** —la otra fue la sesión 3—, y aplica la misma regla, "
                   "hoy con más peso: se entrega el prompt usado y la lista de lo que se corrigió a "
                   "mano.",
    "agenda": {},
    "herramienta_nota": "Hoy **sí se usa asistente de IA**, con dos condiciones que son la mitad de "
                        "la nota: **se entrega el prompt completo** y **la lista de lo que se "
                        "corrigió a mano**. Cualquier asistente gratuito sirve, sin pagar y sin "
                        "tarjeta. El prototipo corregido se edita en **Excalidraw** o **draw.io** y "
                        "el registro va en el **documento del equipo**. Regla que no se negocia: "
                        "**no se le pasan datos personales a un asistente**, ni de ustedes ni de "
                        "nadie — lo que se escribe ahí sale del computador.",
    "avance_proyecto": "Prototipo v2 corregido, con el registro del prompt, las variantes, lo "
                       "corregido a mano y lo descartado — cierra el corte 2",

    "teoria": [
        {
            "tipo": "cards",
            "titulo": "Qué hace bien y qué hace mal la IA en prototipado",
            "cards": [
                ("Hace bien: variantes",
                 "Pedir tres maneras distintas de organizar una pantalla, o diez nombres para un "
                 "botón. **Es rapidísima para abrir opciones**, que es justo lo que cuesta cuando un "
                 "equipo lleva dos horas mirando su propio dibujo."),
                ("Hace bien: textos y casos de prueba",
                 "Rótulos, mensajes de error, y sobre todo **listas de casos que a nadie se le "
                 "ocurrieron**: «¿qué pasa si el usuario escribe el título con una tilde de más?». "
                 "Ahí es muy útil."),
                ("Hace mal: el contexto local",
                 "No sabe que no hay computador en el mostrador, que las voluntarias rotan ni que "
                 "el presupuesto es cero. **Va a proponer la solución promedio de internet**, que "
                 "es una solución para un contexto que no es el suyo."),
                ("Hace mal: inventar con seguridad",
                 "Va a proponer funciones que violan sus propias restricciones, y a veces la ley — "
                 "cuentas de usuario, avisos por correo, recolección de datos— sin avisar de "
                 "ninguna manera que hay un problema."),
            ],
            "columns": 2,
        },
        {
            "tipo": "steps",
            "titulo": "Cómo se le pide algo a la IA en este curso",
            "steps": [
                ("1 · Dé el contexto que no puede saber", "El problema en una frase (sesión 6), quién lo usa, y **las restricciones** — es el paso que decide la calidad de todo lo demás."),
                ("2 · Pida variantes, no una respuesta", "«Dame tres maneras distintas de…». Una sola respuesta invita a aceptarla; tres obligan a elegir, y elegir es su trabajo."),
                ("3 · Prohíba explícitamente lo prohibido", "«Sin crear cuentas de usuario, sin pedir datos personales, sin instalar nada.» **Si no lo dice, lo va a proponer.**"),
                ("4 · Corrija a mano y anote qué corrigió", "Esa lista **es el entregable**. Es la prueba de que ustedes pensaron, y es lo que más pesa en la rúbrica de hoy."),
                ("5 · Declare el uso", "En el documento: qué asistente, para qué, qué se aceptó y qué se descartó. **Declararlo es lo profesional; esconderlo es la falta.**"),
            ],
            "sub": "El prompt sin contexto ni restricciones devuelve la solución promedio de internet, que no es la solución de su proyecto",
        },
        {
            "tipo": "before_after",
            "titulo": "La variante de la IA y la corrección del equipo",
            "before_title": "Lo que devolvió el asistente",
            "before": [
                "Pantalla de **registro con correo y contraseña** antes de consultar.",
                "**Aviso automático por correo** cuando el libro se devuelva.",
                "Sistema de **reservas** con historial por usuario.",
                "Catálogo con **imágenes de portadas**.",
                "Mensaje: «No se encontraron resultados».",
            ],
            "after_title": "Lo que quedó después de corregir",
            "after": [
                "**Sin cuenta**: se consulta con un enlace. *Requisito no funcional de la sesión 7.*",
                "**Nada de correos**: pedir el correo es recolectar datos personales. *Ley 1581 de 2012.*",
                "**Sin reservas ni historial**: quedó fuera del alcance en la sesión 8.",
                "**Sin imágenes**: rompía el límite de 200 KB por consulta. *Indicador de la sesión 5.*",
                "«No encontramos «X» en la lista. Pregunte en el mostrador o intente con el autor.»",
            ],
            "sub": "Ninguna de las cinco propuestas era absurda. Las cinco eran incorrectas para este proyecto, y el asistente no tenía manera de saberlo",
            "size": 13,
        },
        {
            "tipo": "box",
            "titulo": "Cómo cierra el corte 2 hoy",
            "notas": [
                ("info",
                 "**Al final de la sesión hay 20 minutos de evaluación del corte 2**, sobre las "
                 "sesiones 7 a 11: ciclo de vida y costo del cambio, requisitos y criterios de "
                 "aceptación, decisión entre alternativas y alcance mínimo, antecedentes y fuentes, "
                 "prototipado y niveles de fidelidad, y uso responsable de IA. Es individual y a "
                 "libro abierto: **pueden consultar sus propios documentos del equipo**."),
                ("aclaracion",
                 "**La evaluación se aplica en ExamLab**, que es la herramienta que usa este curso "
                 "para las evaluaciones y **no es una plataforma oficial de la universidad**. El "
                 "enlace se comparte en el chat en el momento; si algo falla, la evaluación se "
                 "reprograma y se avisa por el canal del curso."),
                ("advertencia",
                 "**Lo que se califica hoy del taller no es la variante de la IA: es lo que "
                 "corrigieron.** Un equipo que entrega tal cual lo que devolvió el asistente tiene "
                 "la nota más baja del corte, aunque se vea bien. Y no se le pasan datos personales "
                 "a un asistente: lo que se escribe ahí sale del computador y no vuelve."),
            ],
        },
    ],

    "fundamento": [
        {
            "titulo": "La pregunta de entrada: mejor y además ilegal",
            "slide": "{{slide:Pregunta de entrada}}",
            "cuerpo": [
                "El gancho de hoy es un hecho concreto y reproducible, no una hipótesis: si se le "
                "pide a un asistente que mejore un prototipo de consulta de disponibilidad de "
                "libros, **con altísima probabilidad va a proponer cuentas de usuario con correo y "
                "contraseña, y avisos automáticos por correo cuando el libro esté disponible**. Las "
                "dos propuestas son razonables en abstracto, están en casi todos los sistemas "
                "parecidos del mundo, y las dos son incorrectas para este proyecto: violan el "
                "requisito no funcional «sin crear cuenta» de la sesión 7 y convierten al equipo en "
                "responsable del tratamiento de datos personales bajo la Ley 1581 de 2012, que "
                "vieron en la sesión 4.",
                "El punto que hay que hacer explícito, y que es el eje de toda la sesión: **el "
                "asistente no se equivocó por ser malo. Se equivocó porque nadie le dijo las "
                "restricciones.** Propuso la solución promedio de internet, que es exactamente lo "
                "que hace bien; el problema es que la solución promedio no es la solución de un "
                "proyecto con restricciones locales duras. Y lo hizo **con total seguridad**, sin "
                "ninguna señal de advertencia, que es la parte peligrosa.",
                "Vale la pena hacerlo en vivo si el tiempo alcanza —dos minutos de pantalla "
                "compartida con un prompt sin restricciones—, porque verlo proponer la cuenta de "
                "usuario delante de todos vale más que la diapositiva. Si no alcanza, la apertura "
                "sola sirve: en el muro, la pregunta «¿cómo puede pasar eso?» produce respuestas que "
                "ya contienen la respuesta correcta.",
                "Recuerde el encuadre general del curso, que hoy se cierra: la IA está autorizada en "
                "dos sesiones de dieciséis, con la misma regla en las dos —se entrega el prompt y "
                "lo que se corrigió—. Hoy esa regla vale la mitad de la nota del taller.",
            ],
        },
        {
            "titulo": "Qué hace bien y qué hace mal: un mapa honesto",
            "slide": "{{slide:Qué hace bien y qué hace mal}}",
            "cuerpo": [
                "Conviene ser preciso y no moralizante, porque estos estudiantes van a trabajar con "
                "estas herramientas toda su carrera y lo que necesitan es criterio, no prohibición.",
                "**Hace bien: variantes.** Pedir tres maneras distintas de organizar una pantalla o "
                "diez nombres para un botón es un uso excelente. La razón es concreta: un equipo que "
                "lleva dos horas mirando su propio dibujo pierde la capacidad de ver alternativas, y "
                "abrir opciones es justo lo que más cuesta en ese momento.",
                "**Hace bien: textos y casos de prueba.** Rótulos, mensajes de error y, sobre todo, "
                "**listas de casos que a nadie se le ocurrieron** — «¿qué pasa si el usuario escribe "
                "el título con una tilde de más?», «¿qué pasa si dos personas piden el mismo libro "
                "el mismo día?». Aquí la IA es genuinamente superior a un equipo de primer semestre, "
                "porque enumerar casos es exactamente lo que hace bien. Vale la pena decírselo, "
                "porque es el uso que más les va a servir en la sesión 12.",
                "**Hace mal: el contexto local.** No sabe que no hay computador en el mostrador, que "
                "las voluntarias rotan, que el presupuesto es cero, que la conexión es intermitente. "
                "Y como no lo sabe, propone para un contexto que no es el suyo.",
                "**Hace mal: inventar con seguridad.** Esta es la característica que hay que dejar "
                "instalada para siempre, y ya la vieron en la sesión 9 con las referencias "
                "bibliográficas inexistentes: **un modelo de lenguaje genera texto plausible, y no "
                "tiene manera de señalar cuándo lo plausible es incorrecto**. Va a proponer "
                "funciones que violan las restricciones del equipo y a veces la ley, con el mismo "
                "tono seguro con el que propone las buenas. No hay una alarma; la alarma son "
                "ustedes.",
            ],
        },
        {
            "titulo": "El método: cinco pasos y por qué el primero decide todo",
            "slide": "{{slide:Cómo se le pide algo a la IA}}",
            "cuerpo": [
                "**Paso 1: dar el contexto que no puede saber** — el problema en una frase de la "
                "sesión 6, quién lo usa, y las restricciones. Es el paso que decide la calidad de "
                "todo lo demás, y el que los estudiantes se saltan. La diferencia entre «mejora esta "
                "pantalla de biblioteca» y un prompt de diez líneas con las cuatro restricciones "
                "escritas no es de grado: es la diferencia entre recibir la solución promedio de "
                "internet y recibir tres opciones aplicables.",
                "**Paso 2: pedir variantes, no una respuesta.** «Dame tres maneras distintas de…». "
                "El argumento es psicológico y hay que decirlo: una sola respuesta invita a "
                "aceptarla —está ahí, está completa, está bien escrita—; tres obligan a comparar, y "
                "comparar es donde ellos aportan. Es la matriz de decisión de la sesión 8 aplicada "
                "a lo que devuelve un asistente.",
                "**Paso 3: prohibir explícitamente lo prohibido.** «Sin crear cuentas de usuario, "
                "sin pedir datos personales, sin instalar nada, sin imágenes.» La regla en cuatro "
                "palabras: **si no lo dice, lo va a proponer**. Y aquí hay una lección de "
                "ingeniería más general que vale la pena señalar: los requisitos no funcionales que "
                "escribieron en la sesión 7 son precisamente lo que hay que poner en el prompt, "
                "porque son lo que el mundo no adivina. Un equipo que tiene sus requisitos no "
                "funcionales escritos hace un prompt bueno sin esfuerzo; uno que no los tiene, no "
                "puede.",
                "**Paso 4: corregir a mano y anotar qué se corrigió.** Esa lista **es el "
                "entregable**, y hay que decirlo sin ambigüedad porque cambia cómo trabajan: es la "
                "prueba de que pensaron, y es lo que más pesa en la rúbrica de hoy —30 de 100—. Un "
                "equipo que no corrigió nada no usó el asistente: lo obedeció.",
                "**Paso 5: declarar el uso.** Qué asistente, para qué, qué se aceptó y qué se "
                "descartó. El encuadre correcto no es de sospecha sino de profesión: **declarar el "
                "uso de una herramienta es lo normal en ingeniería** —nadie esconde que usó una "
                "calculadora o una biblioteca de código—, y esconderlo es lo que constituye la "
                "falta. En la vida laboral esto ya es requisito en muchas organizaciones, y "
                "acostumbrarse ahora les ahorra un problema después.",
            ],
        },
        {
            "titulo": "El antes y después, y cómo cierra el corte",
            "slide": "{{slide:La variante de la IA}} {{slide:Cómo cierra el corte 2}}",
            "cuerpo": [
                "La diapositiva de antes y después es el corazón didáctico de la sesión, y hay que "
                "recorrerla con una insistencia: **ninguna de las cinco propuestas del asistente era "
                "absurda**. Cuentas de usuario, avisos por correo, reservas con historial, portadas, "
                "y un mensaje de error estándar: las cinco están en sistemas reales de bibliotecas "
                "en todo el mundo. **Las cinco eran incorrectas para este proyecto**, y cada una por "
                "una razón distinta que el equipo ya había escrito en una sesión anterior — el "
                "requisito «sin cuenta» de la sesión 7, la Ley 1581 de la sesión 4, el alcance "
                "mínimo de la sesión 8, el límite de 200 KB de la sesión 5, y la regla de mensajes "
                "con salida de la sesión 10.",
                "Ese es el hallazgo que hay que dejar dicho en voz alta, porque justifica todo el "
                "corte: **el equipo pudo corregir al asistente porque tenía sus decisiones "
                "escritas.** Un equipo sin requisitos no funcionales, sin alcance definido y sin "
                "indicador ambiental no habría tenido con qué objetar, y habría aceptado las cinco. "
                "La documentación de las sesiones 6 a 10 no era burocracia académica: es lo que hoy "
                "les permite ejercer criterio frente a una herramienta que suena más segura que "
                "ellos.",
                "**El cierre del corte.** Los últimos 20 minutos son la evaluación del corte 2 en "
                "ExamLab, individual y a libro abierto sobre sus propios documentos del equipo. "
                "Cubre las sesiones 7 a 11: fases y costo del cambio, requisitos y criterios de "
                "aceptación, matriz de decisión y alcance mínimo, calidad de fuentes, fidelidad de "
                "prototipos y uso responsable de IA. Que sea a libro abierto es deliberado y "
                "conviene explicarlo: **premia al equipo que documentó**, que es exactamente la "
                "conducta que el corte entero intentó enseñar.",
                "Hay que decir con claridad, como en la sesión 6, que **ExamLab es la herramienta "
                "que usa este curso para las evaluaciones y no es una plataforma oficial de la "
                "universidad**; el enlace se comparte en el chat en el momento y, si algo falla, la "
                "evaluación se reprograma y se avisa por el canal del curso. Y la advertencia final "
                "del taller, que hay que repetir aunque ya esté en la diapositiva: **no se le pasan "
                "datos personales a un asistente** —ni propios ni de terceros—, porque lo que se "
                "escribe ahí sale del computador y no vuelve.",
            ],
        },
    ],

    "plan": [
        {
            "titulo": "00:00–00:08 · Apertura · [Slide 4]",
            "cuerpo": [
                "Comparta pantalla antes de que entre el primero:",
                "> «Le pedí a un asistente que mejorara el prototipo de la biblioteca. Me devolvió "
                "algo mejor... y además ilegal. ¿Cómo puede pasar eso?»",
                "**[Nota docente]:** avise de una vez el reparto de hoy: **teoría 17 min, taller 27 "
                "min, exposiciones 15 min y evaluación del corte 2 al final, 20 min en ExamLab**. "
                "Que nadie se vaya antes.",
                "**[Nota docente]:** si tiene dos minutos, hágalo en vivo: un prompt sin "
                "restricciones sobre su prototipo, y muestre cómo propone la cuenta de usuario. Vale "
                "más que la diapositiva.",
            ],
        },
        {
            "titulo": "00:08–00:25 · Teoría (17 min) · [Slide 5][Slide 6][Slide 7][Slide 8]",
            "cuerpo": [
                "Reparto estricto, hoy no hay margen:",
                "- **4 min** · Qué hace bien y qué mal [Slide 5]. Destaque el uso bueno que más les "
                "va a servir: **pedir listas de casos de prueba**.",
                "- **6 min** · Los cinco pasos [Slide 6]. El paso 3 es el que salva la sesión: **si "
                "no lo dice, lo va a proponer**. Y diga que el paso 4 vale 30 puntos.",
                "- **5 min** · El antes y después [Slide 7]. Recórralo fila por fila diciendo **de "
                "qué sesión sale cada corrección**. Es la diapositiva que justifica el corte entero.",
                "- **2 min** · Cómo cierra el corte [Slide 8]. Diga que es a libro abierto **sobre "
                "sus propios documentos** y que ExamLab no es plataforma oficial de la universidad.",
            ],
        },
        {
            "titulo": "00:25–00:52 · Taller en salas de grupo (27 min) · [Slide 9]",
            "cuerpo": [
                "**2 min** para abrir el asistente, el prototipo y el documento del equipo.",
                "Ritmo sugerido dentro de la sala, dígaselo al repartir:",
                "- 8 min · escribir el prompt **con contexto, restricciones y prohibiciones** y "
                "pedir tres variantes.",
                "- 7 min · elegir una con criterio y escribir por qué.",
                "- 8 min · corregir a mano y **anotar cada corrección con la razón**.",
                "- 2 min · dejar el registro y el PNG en la carpeta.",
                "**[Nota docente]:** entre a las cinco salas y pida ver **el prompt**, no el "
                "resultado. Un prompt de dos líneas explica por sí solo una mala variante.",
                "**[Nota docente]:** si un equipo dice «quedó perfecto, no corregimos nada», "
                "revíselo contra sus propios requisitos no funcionales: siempre hay algo. Es la "
                "señal más clara de que aceptaron sin leer.",
            ],
        },
        {
            "titulo": "00:52–01:07 · Exposiciones · [Slide 10]",
            "cuerpo": [
                "5 equipos × 3 min. **El minuto obligatorio es «qué corregimos y por qué»**, no la "
                "variante elegida.",
                "**[Nota docente]:** los cinco enlaces en el chat antes de arrancar. Sea estricto con "
                "el tiempo: detrás viene la evaluación y no se puede recortar.",
                "**[Nota docente]:** pregunte a cada equipo **de qué sesión salió una de sus "
                "correcciones**. Es la manera de cerrar el corte mostrando que todo estaba "
                "conectado.",
            ],
        },
        {
            "titulo": "01:07–01:27 · Evaluación del corte 2 en ExamLab (20 min) · [Slide 8]",
            "cuerpo": [
                "Cierre las salas y devuelva a todos a la sala principal antes de compartir el "
                "enlace.",
                "**[Nota docente]:** el enlace de ExamLab va **en el chat**, no en la diapositiva. "
                "Confirme por chat que los cinco equipos lo abrieron antes de arrancar el "
                "cronómetro.",
                "Recuerde en voz alta: **individual y a libro abierto sobre sus propios documentos "
                "del equipo**. Cubre las sesiones 7 a 11.",
                "**[Nota docente]:** deje claro que **ExamLab no es una plataforma oficial de la "
                "universidad** y que si algo falla la evaluación se reprograma y se avisa por el "
                "canal del curso. Tenga a mano el plan B: si la herramienta no responde, la "
                "evaluación se reprograma — no la improvise por chat.",
                "Quédese con la cámara encendida y el micrófono abierto para dudas de enunciado, "
                "sin resolver contenido.",
            ],
        },
        {
            "titulo": "01:27–01:30 · Cierre · [Slide 11][Slide 12]",
            "cuerpo": [
                "Una idea: **pudieron corregir al asistente porque tenían sus decisiones "
                "escritas.** Eso es lo que hicieron en el corte 2.",
                "Anuncie el corte 3: empieza con la **presentación de avances** de la sesión 12, "
                "donde el prototipo se prueba con una persona ajena al equipo. Es la única "
                "retroalimentación gratis del semestre.",
            ],
        },
    ],

    "taller": {
        "archivo": "Prototipo v2 con IA",
        "titulo": "Prototipo v2 con IA",
        "min": 27,
        "exposicion": 3,
        "consigna": "Mejoren el prototipo con ayuda de un asistente, y dejen el rastro completo. "
                    "Escriban un **prompt con contexto, restricciones y prohibiciones**, pidan "
                    "**tres variantes**, elijan una **con criterio**, **corrijan a mano** lo que la "
                    "IA no podía saber, y anoten **qué descartaron y por qué**.",
        "entregable": "el prototipo v2 corregido (PNG en la carpeta del equipo) y el registro "
                      "completo en el documento del equipo: prompt, las tres variantes, la elegida "
                      "con su razón, la lista de correcciones y la de descartes",
        "entregable_corto": "prototipo v2 + registro de prompt, variantes, correcciones y descartes",
        "reparto_titulo": "Ritmo sugerido dentro de la sala (27 min):",
        "reparto": "8 min escribir el prompt y pedir las tres variantes · 7 min elegir una y "
                   "escribir por qué · 8 min corregir a mano anotando la razón de cada corrección · "
                   "2 min dejar el registro y el PNG en la carpeta. **Una persona escribe el "
                   "registro mientras las otras corrigen**: si se deja para el final, no se hace.",
        "reparto_corto": "27 min: prompt, variantes, elección, correcciones y registro",
        "bloques": [
            {"clave": "EL PROMPT QUE USAMOS",
             "pide": "El prompt completo, copiado tal cual. Tiene que incluir **el problema en una "
                     "frase, quién lo usa, las restricciones y lo que está prohibido proponer**.",
             "check": "están las restricciones de la sesión 6 y los requisitos no funcionales de la sesión 7. Un prompt de dos líneas no cumple."},
            {"clave": "LAS TRES VARIANTES",
             "pide": "Las tres opciones que devolvió, resumidas en dos o tres líneas cada una. **No "
                     "una sola respuesta**: tres.",
             "check": "hay tres y son distintas entre sí. Si solo pidieron una, el bloque no está hecho."},
            {"clave": "LA QUE ELEGIMOS Y POR QUÉ",
             "pide": "Cuál eligieron y el criterio, apoyado en sus **requisitos y restricciones** — "
                     "no en «nos gustó más».",
             "check": "el criterio se puede rastrear a un requisito escrito antes de hoy."},
            {"clave": "LO QUE CORREGIMOS A MANO",
             "pide": "Cada corrección con **la razón y la sesión de donde sale**: qué proponía la "
                     "IA, qué quedó, y por qué. Es el bloque que más pesa.",
             "check": "hay al menos tres correcciones con razón. «No corregimos nada» significa que aceptaron sin revisar."},
            {"clave": "LO QUE DESCARTAMOS Y POR QUÉ",
             "pide": "Las propuestas que se rechazaron completas, y el motivo: fuera del alcance, "
                     "viola una restricción, viola la ley, o consume demasiado.",
             "check": "cada descarte tiene un motivo verificable, no una impresión."},
        ],
        "expo": [
            ("25 s · El prompt", "Lean las restricciones que pusieron. Solo esa parte."),
            ("30 s · Las tres variantes", "En una frase cada una."),
            ("30 s · La que eligieron", "Y el requisito en el que se apoyaron."),
            ("70 s · Lo que corrigieron", "Dos correcciones con su razón y **de qué sesión sale cada una**. Es el minuto obligatorio."),
            ("25 s · Lo que descartaron", "Una propuesta rechazada y el motivo."),
        ],
    },

    "rubrica": [
        ("El prompt incluye el problema, los actores, las restricciones y lo prohibido", 20,
         "Sin contexto la IA devuelve la solución promedio de internet, que no es la del proyecto."),
        ("Se pidieron y se registraron tres variantes distintas", 15,
         "Una sola respuesta invita a aceptarla; tres obligan a comparar, y comparar es el trabajo del ingeniero."),
        ("La variante elegida se justifica con un requisito o restricción escrito antes", 20,
         "Es la matriz de decisión de la sesión 8 aplicada a lo que devuelve una herramienta."),
        ("Hay al menos tres correcciones a mano, cada una con su razón y su origen", 30,
         "Es la prueba de que el equipo ejerció criterio: lo que se califica no es la variante, es la corrección."),
        ("Se declara qué se descartó y por qué, con motivo verificable", 15,
         "Declarar el uso y los límites de una herramienta es la práctica profesional; esconderlo es la falta."),
    ],

    "solucion": {
        "para_que": "Este documento trae el ejercicio completo del caso de la biblioteca: el prompt "
                    "literal, las tres variantes, la elección, las correcciones con su origen y los "
                    "descartes. Su valor está en el bloque de correcciones, donde **cada una se "
                    "rastrea a una sesión anterior** — es la demostración de que el corte 2 estaba "
                    "conectado. Si el docente solo alcanza a leer un bloque, que sea **LO QUE "
                    "CORREGIMOS A MANO**.\n\n"
                    "**Aviso:** un asistente no devuelve dos veces lo mismo. Las variantes de este "
                    "documento son representativas de lo que devuelve un prompt sin restricciones, "
                    "no una transcripción a reproducir. Si lo prueba antes de clase y le devuelve "
                    "otra cosa, mejor: úselo como ejemplo en vivo.",
        "caso_titulo": "La biblioteca del barrio · prototipo v2 con asistente",
        "caso": "Prototipo v1 de la sesión 10: tres pantallas —consultar, resultado con sus tres "
                "estados, y actualizar para la voluntaria—, con la fecha de última actualización "
                "visible. Restricciones y requisitos vigentes: sin cuenta, sin computador en el "
                "mostrador, se aprende sin manual, menos de 200 KB por consulta, alcance mínimo sin "
                "reservas ni historial. La pregunta del prototipo: *¿la voluntaria puede actualizar "
                "la lista en menos de 30 segundos sin equivocarse?*",
        "por_que_este_caso": "Porque el asistente propone cinco cosas sensatas y las cinco son "
                             "incorrectas aquí, cada una por una razón que el equipo ya había "
                             "escrito en una sesión distinta. Es la manera más clara de mostrar que "
                             "la documentación de las sesiones 6 a 10 no era un trámite: es lo que "
                             "les permite objetar a una herramienta que suena más segura que ellos.",
        "bloques": [
            {
                "clave": "EL PROMPT QUE USAMOS",
                "respuesta": "El prompt, tal cual:\n\n"
                             "> Estoy diseñando un prototipo de baja fidelidad para una biblioteca "
                             "comunitaria de barrio, en un proyecto universitario de primer "
                             "semestre.\n>\n"
                             "> **Problema:** los usuarios no saben si un libro está disponible "
                             "antes de ir, y hacen viajes que terminan sin préstamo (4 de cada 10 "
                             "visitas).\n>\n"
                             "> **Quiénes lo usan:** vecinos del barrio que consultan desde su "
                             "celular, y voluntarias que rotan cada pocas semanas y actualizan la "
                             "información al cerrar el día.\n>\n"
                             "> **Restricciones que no se pueden cambiar:** presupuesto cero; no hay "
                             "computador disponible en el mostrador durante la atención; las "
                             "voluntarias rotan y no se les puede exigir capacitación larga; nadie "
                             "puede atender un teléfono en horario fijo; cada consulta debe mover "
                             "menos de 200 KB porque muchos usuarios tienen datos móviles "
                             "limitados.\n>\n"
                             "> **Prohibido proponer:** crear cuentas de usuario o contraseñas; "
                             "pedir datos personales de cualquier tipo (correo, teléfono, "
                             "documento); instalar aplicaciones; funciones de reserva o historial por "
                             "usuario; imágenes.\n>\n"
                             "> **Lo que ya tengo:** tres pantallas —consultar, resultado "
                             "(disponible / prestado / no está) y actualizar para la voluntaria—, con "
                             "la fecha de última actualización visible al usuario.\n>\n"
                             "> **Lo que necesito:** dame **tres maneras distintas** de organizar la "
                             "pantalla de actualización de la voluntaria para que pueda marcar un "
                             "préstamo en menos de 30 segundos y sin manual. Para cada una, dime qué "
                             "gana y qué pierde.\n\n"
                             "**Los cinco elementos que hacen bueno este prompt**, y que hay que "
                             "señalar uno por uno: el problema con su cifra, los actores reales, las "
                             "restricciones explícitas, **la lista de lo prohibido**, y una petición "
                             "de tres variantes con sus contras. Nótese que todo eso ya existía "
                             "escrito: el problema es de la sesión 6, las restricciones son del "
                             "árbol de la sesión 6, las prohibiciones son los requisitos no "
                             "funcionales de la sesión 7 más el alcance de la sesión 8 y el "
                             "indicador de la sesión 5. **El prompt no se inventó hoy: se armó "
                             "copiando lo ya documentado.**\n\n"
                             "**Comparación con el prompt malo**, para mostrar en clase: «mejora esta "
                             "pantalla de biblioteca para que sea más fácil de usar». Devuelve la "
                             "solución promedio de internet, que incluye cuentas de usuario y "
                             "notificaciones por correo.",
                "como_calificar": "20 pts. Verificación por partes: contexto y actores (5), "
                                  "restricciones explícitas (7), **lista de lo prohibido** (5), "
                                  "petición de variantes (3). El bloque de prohibiciones es el que "
                                  "más equipos van a omitir, y es el que evita el problema entero: "
                                  "si falta, muéstreles la conexión con lo que les devolvió la IA. "
                                  "Un prompt de dos líneas vale 5, y la conversación que sigue vale "
                                  "más que el descuento — dígales que su prompt malo explica por sí "
                                  "solo la variante mala que recibieron."
            },
            {
                "clave": "LAS TRES VARIANTES",
                "respuesta": "**Variante 1 · Lista con un botón por título.** Todos los títulos "
                             "registrados en una lista; cada uno con un botón que alterna entre "
                             "«Marcar prestado» y «Marcar devuelto». *Gana: un solo toque por "
                             "movimiento. Pierde: si la lista crece, hay que buscar el título "
                             "desplazándose.*\n\n"
                             "**Variante 2 · Buscar y marcar.** Un campo de búsqueda arriba; la "
                             "voluntaria escribe el título, aparece uno solo y lo marca. *Gana: "
                             "funciona con muchos títulos. Pierde: exige escribir, que es más lento "
                             "y se equivoca más en un celular.*\n\n"
                             "**Variante 3 · Dos columnas: prestados y disponibles.** Los títulos "
                             "repartidos en dos listas, y se mueven de una a otra al tocarlos. "
                             "*Gana: se ve de un vistazo el estado completo. Pierde: en pantalla de "
                             "celular las dos columnas quedan muy angostas.*\n\n"
                             "Las tres son razonables y las tres respetan las prohibiciones — porque "
                             "el prompt las incluía. **Eso ya es un resultado**: la calidad de las "
                             "tres variantes es consecuencia directa de la calidad del prompt, y "
                             "conviene decirlo al comparar con lo que reciban los equipos que "
                             "escribieron dos líneas.",
                "como_calificar": "15 pts, 5 por variante registrada de forma comprensible. El "
                                  "criterio duro es que **sean tres y sean distintas**: si el equipo "
                                  "pidió una sola respuesta, vale 5 en total y hay que explicar por "
                                  "qué —una respuesta única invita a aceptarla, y aceptar no es "
                                  "decidir—. Valore que hayan pedido «qué gana y qué pierde» cada "
                                  "variante: es la matriz de la sesión 8 hecha en una línea."
            },
            {
                "clave": "LA QUE ELEGIMOS Y POR QUÉ",
                "respuesta": "**Elegimos la variante 1: lista con un botón por título.**\n\n"
                             "**El criterio, apoyado en requisitos escritos antes:**\n\n"
                             "- El requisito no funcional **«se aprende en menos de cinco minutos y "
                             "sin manual»** (sesión 7) favorece la que tiene menos decisiones: un "
                             "toque, un cambio. La variante 2 exige escribir, y escribir en un "
                             "celular con una fila de gente enfrente es donde se cometen los "
                             "errores.\n"
                             "- El criterio de aceptación **«registra un préstamo en menos de 30 "
                             "segundos»** (sesión 7) también favorece la 1: tocar es más rápido que "
                             "escribir.\n"
                             "- La contra de la variante 1 —que la lista crezca— **no aplica en el "
                             "alcance mínimo** (sesión 8), porque solo se registran los títulos que "
                             "se prestan, que son pocas decenas. Si algún día crece, se agrega la "
                             "búsqueda: eso queda anotado en «versión siguiente».\n\n"
                             "Nótese que la razón por la que la contra no aplica **sale de una "
                             "decisión de la sesión 8**. Sin ese alcance escrito, la variante 2 "
                             "habría parecido más segura, y el equipo habría elegido lo más "
                             "complicado por miedo a un problema que su propio alcance ya había "
                             "descartado.\n\n"
                             "**Lo que no es un criterio:** «nos gustó más», «se ve más moderna», «la "
                             "IA dijo que era la mejor». La última es la más peligrosa de las tres, "
                             "porque suena a argumento.",
                "como_calificar": "20 pts. Una sola verificación: **¿el criterio se rastrea a un "
                                  "requisito o restricción escrito antes de hoy?** Si sí, 20. Si es "
                                  "«nos gustó más» o «se ve mejor», 6. Y si es **«la IA recomendó "
                                  "esta»**, vale 0 en este bloque y hay que decir por qué en voz "
                                  "alta: la recomendación de la herramienta no es un criterio del "
                                  "equipo, es la ausencia de criterio con buena redacción."
            },
            {
                "clave": "LO QUE CORREGIMOS A MANO",
                "respuesta": "Las correcciones, cada una con su razón **y la sesión de donde sale** — "
                             "este es el bloque que hay que leer en voz alta en clase:\n\n"
                             "**1 · Quitamos la pantalla de ingreso con contraseña para la "
                             "voluntaria.** El asistente la agregó igual, pese a la prohibición, "
                             "«para proteger la lista». *Razón:* el requisito no funcional «se "
                             "aprende sin manual» y la rotación de voluntarias hacen inviable "
                             "administrar contraseñas — y pedir un correo para recuperarla sería "
                             "recolectar datos personales. **Sesiones 7 y 4 (Ley 1581 de 2012).** "
                             "*Cómo lo resolvimos en su lugar:* la pantalla de actualización vive en "
                             "un enlace distinto que solo se comparte con las voluntarias. No es "
                             "seguridad fuerte, y lo anotamos como limitación conocida en el "
                             "informe.\n\n"
                             "**2 · Quitamos el campo «nombre de quien presta».** *Razón:* es un "
                             "dato personal y no hace falta para el requisito —el usuario solo "
                             "necesita saber si está o no está—. **Sesión 4.** *En su lugar:* el "
                             "estado es «prestado», sin decir a quién.\n\n"
                             "**3 · Cambiamos «Fecha de vencimiento: 12/09» por «Se esperaba de "
                             "vuelta el lunes».** *Razón:* lenguaje de persona y no de sistema, y "
                             "además admite que es una expectativa. **Sesión 10 (textos reales).**\n\n"
                             "**4 · Agregamos la fecha de última actualización, que la variante "
                             "había eliminado.** *Razón:* es la manera de ser honestos con el "
                             "sacrificio aceptado al decidir —la información no está al minuto—. "
                             "**Sesiones 8 y 10.** Sin esa línea, la solución miente por omisión.\n\n"
                             "**5 · Reescribimos «No se encontraron resultados» por «No encontramos "
                             "«X» en la lista. Pregunte en el mostrador o intente con el autor».** "
                             "*Razón:* un mensaje de error tiene que decir qué hacer. **Sesión "
                             "10.**\n\n"
                             "**6 · Quitamos los íconos de colores de cada título.** *Razón:* suben "
                             "el peso de la página y el límite es 200 KB por consulta. **Sesión "
                             "5.**\n\n"
                             "**El hallazgo, y la lección de cierre del corte:** las seis "
                             "correcciones salen de cinco sesiones distintas, y **ninguna se podía "
                             "hacer sin tener esas decisiones escritas**. Un equipo sin requisitos "
                             "no funcionales, sin alcance definido y sin indicador ambiental habría "
                             "aceptado las seis propuestas, todas razonables en abstracto. El corte "
                             "2 no fue documentar por documentar: fue construir el criterio con el "
                             "que hoy se objeta a una herramienta que suena más segura que uno.",
                "como_calificar": "30 pts, el bloque que decide la nota. 5 pts por corrección con "
                                  "**razón explícita**, hasta 30; sin razón, 2 pts cada una. Valore "
                                  "el doble —dígalo en la retroalimentación— a las correcciones que "
                                  "**citan la sesión de origen**: es la señal de que el estudiante "
                                  "está acumulando y no empezando de cero. Y atención al caso "
                                  "crítico: si un equipo dice **«no corregimos nada, quedó "
                                  "perfecto»**, revíselo delante de ellos contra sus propios "
                                  "requisitos no funcionales. Siempre hay algo, y encontrarlo juntos "
                                  "enseña más que el descuento. Si de verdad no hay nada que "
                                  "corregir, casi siempre significa que el prompt era tan detallado "
                                  "que el equipo ya había hecho todo el trabajo — dígalo, es un "
                                  "resultado válido y bueno."
            },
            {
                "clave": "LO QUE DESCARTAMOS Y POR QUÉ",
                "respuesta": "Propuestas rechazadas completas, con motivo verificable:\n\n"
                             "- **Avisos automáticos por correo cuando el libro se devuelva.** "
                             "*Motivo:* exige pedir el correo del usuario, es decir recolectar datos "
                             "personales, con todo lo que eso implica en autorización, finalidad y "
                             "custodia. **Ley 1581 de 2012 · sesión 4.** Y además nadie en la "
                             "biblioteca puede responder por esos datos.\n"
                             "- **Sistema de reservas con historial por usuario.** *Motivo:* quedó "
                             "explícitamente fuera del alcance mínimo y está en la lista de «versión "
                             "siguiente». **Sesión 8.** No es una mala idea: es una idea para otro "
                             "semestre.\n"
                             "- **Imágenes de portadas para reconocer los libros.** *Motivo:* rompe "
                             "el límite de 200 KB por consulta, que es un requisito no funcional "
                             "derivado del indicador ambiental. **Sesiones 5 y 7.**\n"
                             "- **Estadísticas de los libros más prestados.** *Motivo:* interesante y "
                             "fuera del problema; el problema es el viaje en vano. **Frontera de la "
                             "sesión 6.** Anotado como idea para el informe final, no para el "
                             "prototipo.\n\n"
                             "**Y la declaración del uso**, que va en el documento del equipo y en el "
                             "informe final:\n\n"
                             "> *Para la pantalla de actualización se usó un asistente de IA "
                             "(nombre y versión, fecha) pidiendo tres variantes de organización. Se "
                             "eligió una y se le hicieron seis correcciones, documentadas arriba. Se "
                             "descartaron cuatro propuestas por violar restricciones del proyecto o "
                             "la Ley 1581 de 2012. No se le entregó ningún dato personal ni "
                             "información de la biblioteca distinta de la ya publicada en este "
                             "documento.*\n\n"
                             "Esa última frase importa y hay que señalarla: **la trazabilidad "
                             "incluye decir qué NO se le entregó a la herramienta.**",
                "como_calificar": "15 pts. Se califica que cada descarte tenga un **motivo "
                                  "verificable** —fuera del alcance, viola una restricción, viola la "
                                  "ley, consume demasiado— y no una impresión (10 pts), y que exista "
                                  "la **declaración del uso** con asistente, fecha y qué se aceptó y "
                                  "descartó (5 pts). Un equipo que descarta diciendo «no nos "
                                  "convenció» vale 4. Y valore que digan qué **no** le entregaron al "
                                  "asistente: es el nivel de trazabilidad que se espera en un "
                                  "entorno profesional."
            },
        ],
        "variantes": [
            {"caso": "Equipos que dicen «no corregimos nada, quedó perfecto»",
             "clave": "Es la señal más clara de que aceptaron sin leer. No lo discuta: abra su lista "
                      "de requisitos no funcionales y revise la variante contra ella, punto por "
                      "punto, delante de ellos. En dos minutos aparece algo — casi siempre un dato "
                      "personal, un texto de sistema o un elemento que pesa. Encontrarlo juntos "
                      "enseña la sesión entera. Si de verdad no hay nada, felicítelos: significa que "
                      "su prompt era tan bueno que ya habían hecho el trabajo, y eso también hay que "
                      "reconocerlo."},
            {"caso": "Equipos sin acceso a un asistente o que se quedan sin cupo gratuito",
             "clave": "Pasa y no puede costarle la nota a nadie. Dos salidas: que trabajen con el "
                      "asistente de un compañero del equipo compartiendo pantalla —es trabajo en "
                      "equipo, no copia—, o que hagan el ejercicio con **las variantes de este "
                      "documento de solución** como si las hubiera devuelto un asistente, "
                      "declarándolo así. Lo que se califica es el criterio con el que corrigen, y "
                      "eso se puede evaluar igual. **Ningún estudiante tiene que pagar por nada.**"},
            {"caso": "Equipos que le pasaron datos reales al asistente",
             "clave": "Ocurre sin mala intención: el nombre de la coordinadora, la dirección de la "
                      "biblioteca, un teléfono de contacto. Hay que decirlo sin dramatizar y con "
                      "precisión: **lo que se escribe ahí salió del computador y no vuelve.** No hay "
                      "manera de deshacerlo, así que la corrección es hacia adelante — que lo "
                      "declaren en el registro y que no vuelva a pasar. Es exactamente la sesión 4 "
                      "ocurriendo en vivo, y como lección vale más que cualquier advertencia previa."},
            {"caso": "Proyectos de proceso o gestión, sin pantallas",
             "clave": "El ejercicio es idéntico cambiando el objeto: se piden **tres maneras "
                      "distintas de organizar el formato o la secuencia de pasos**. El asistente es "
                      "especialmente útil aquí para pedir **casos que no se previeron** —«¿qué pasa "
                      "si el paso 2 se hizo pero el 1 no?»—, y esa lista es un insumo directo para "
                      "la prueba de la sesión 12."},
        ],
        "cierre": "Tres minutos, y hay dos cosas que decir. La primera es la idea del corte: **el "
                  "equipo pudo corregir al asistente porque tenía sus decisiones escritas.** Las "
                  "seis correcciones del caso modelo salen de cinco sesiones distintas —el requisito "
                  "sin cuenta de la 7, la Ley 1581 de la 4, el alcance de la 8, el indicador de la "
                  "5, los textos reales de la 10— y ninguna se podía hacer sin ese material. Dígalo "
                  "con estas palabras, porque es la respuesta a la pregunta que todos se hacen en "
                  "primer semestre: documentar no fue un trámite, fue construir el criterio con el "
                  "que hoy se le objeta a una herramienta que suena más segura que uno. La segunda "
                  "es operativa: recuerde que la evaluación del corte 2 viene inmediatamente "
                  "después de las exposiciones, en ExamLab, individual y a libro abierto sobre sus "
                  "propios documentos — que sea a libro abierto premia exactamente al equipo que "
                  "documentó—. Y anuncie el corte 3, que empieza con la sesión 12: el prototipo se "
                  "prueba **con una persona ajena al equipo**, y es la única retroalimentación "
                  "gratis del semestre.",
        "conexion": "Hacia atrás: la **sesión 10** dejó el prototipo que hoy se mejora; la **sesión "
                    "8** dejó el alcance que descarta la mitad de las propuestas; la **sesión 7** "
                    "dejó los requisitos no funcionales que se copian en el prompt; la **sesión 5** "
                    "dejó el límite de datos; la **sesión 4** dejó la Ley 1581, que hoy se aplica "
                    "dos veces; la **sesión 3** dejó la regla de entregar el prompt y las "
                    "correcciones. Hacia adelante: la **sesión 12** prueba este prototipo v2 con una "
                    "persona ajena; la **sesión 13** evalúa el impacto social y ambiental de la "
                    "solución; la **sesión 14** sube la fidelidad para la presentación; y el "
                    "**informe final de la sesión 16** incluye la declaración del uso de IA que hoy "
                    "quedó escrita.",
    },

    "errores": [
        {"dice": "«Mejora esta pantalla de biblioteca para que sea más fácil de usar»",
         "por_que": "Sin contexto ni restricciones devuelve la solución promedio de internet, que incluye cuentas de usuario y notificaciones por correo.",
         "pida": "El problema en una frase, los actores, las restricciones y **la lista de lo prohibido**. Todo eso ya lo tienen escrito de las sesiones 6, 7 y 8."},
        {"dice": "«La IA dijo que esta era la mejor opción»",
         "por_que": "La recomendación de la herramienta no es un criterio del equipo: es la ausencia de criterio con buena redacción.",
         "pida": "El requisito o la restricción en la que se apoya la elección. Si no hay ninguno, todavía no eligieron."},
        {"dice": "«No corregimos nada, quedó perfecto»",
         "por_que": "Significa que aceptaron sin revisar. Revisado contra los propios requisitos no funcionales, siempre aparece algo.",
         "pida": "Revisar la variante punto por punto contra su lista de requisitos, delante de usted. Aparece en dos minutos."},
        {"dice": "Datos reales de personas escritos en el prompt",
         "por_que": "Lo que se escribe ahí sale del computador y no vuelve: es tratamiento de datos personales sin autorización.",
         "pida": "Que lo declaren en el registro y que en adelante usen roles y datos inventados. La corrección es hacia adelante."},
        {"dice": "Un registro escrito al final, de memoria",
         "por_que": "Las correcciones y sus razones se olvidan en minutos, y sin razones el bloque de 30 puntos no se puede calificar.",
         "pida": "Que una persona del equipo escriba el registro **mientras** los otros corrigen. Si se deja para el final, no se hace."},
    ],

    "dudas": [
        {"p": "¿Podemos usar IA en las otras sesiones?",
         "r": "No. Este curso la autoriza en dos sesiones de dieciséis —la 3 y hoy— y en las dos con "
              "la misma regla: se entrega el prompt y lo que se corrigió. En las demás el trabajo es "
              "propio, y la razón no es desconfianza: es que hay cosas —escribir un requisito, "
              "dibujar un flujo, leer una fuente— que solo se aprenden haciéndolas. En el informe "
              "final se declara todo uso de IA del semestre."},
        {"p": "¿Cuál asistente hay que usar?",
         "r": "Cualquiera gratuito. **No se paga nada y no se dan datos de tarjeta**: es regla del "
              "curso. Si a alguien se le agota el cupo gratuito, trabaja con el de un compañero "
              "compartiendo pantalla, o hace el ejercicio con las variantes del documento de la "
              "clase declarándolo así. Nadie pierde nota por no tener acceso."},
        {"p": "¿Es trampa usar IA para el proyecto?",
         "r": "No, si se declara y si el criterio es suyo. Lo que sería falta es presentar como "
              "propio algo que no se revisó ni se entendió — igual que copiar un texto sin citarlo, "
              "que ya vieron en la sesión 9. La declaración del uso es lo que convierte una "
              "herramienta en una herramienta: **declararla es lo profesional; esconderla es la "
              "falta.**"},
        {"p": "¿La evaluación del corte es a libro abierto de verdad?",
         "r": "Sí, individual y con sus propios documentos del equipo a la vista: la ficha del "
              "problema, la tabla de requisitos, la matriz de decisión, las fichas de antecedentes y "
              "el prototipo. Es deliberado — **premia al equipo que documentó**, que es justo lo que "
              "el corte intentó enseñar. Lo que no se puede es resolverla entre varios: es "
              "individual."},
    ],

    "notas_operativas": [
        "**El reparto de hoy es distinto y hay que anunciarlo en el minuto 2:** teoría 17 min · "
        "taller 27 min · exposiciones 15 min · **evaluación del corte 2, 20 min al final**. Que nadie "
        "se vaya antes.",
        "**Prepare la evaluación en ExamLab con anticipación** y téngala abierta antes de la sesión. "
        "El enlace va **en el chat**, nunca en la diapositiva.",
        "**Cierre las salas de grupo y devuelva a todos a la sala principal** antes de compartir el "
        "enlace de la evaluación. Confirme por chat que los cinco equipos lo abrieron antes de "
        "arrancar el cronómetro.",
        "Diga en voz alta que **ExamLab no es una plataforma oficial de la universidad** y que si "
        "falla la evaluación se reprograma por el canal del curso. **Tenga el plan B decidido de "
        "antemano:** reprogramar, no improvisar por chat.",
        "En las salas pida ver **el prompt**, no el resultado. Un prompt de dos líneas explica por sí "
        "solo la variante mala que recibieron.",
        "Si un equipo dice que no corrigió nada, revise la variante contra sus requisitos no "
        "funcionales **delante de ellos**. Aparece algo en dos minutos y enseña más que el descuento.",
        "**Ningún estudiante paga nada.** Si a alguien se le agotó el cupo gratuito, comparte "
        "pantalla con un compañero o usa las variantes del documento de clase declarándolo.",
        "Repita la regla dura: **no se le pasan datos personales a un asistente.** Si ya pasó, se "
        "declara en el registro y no vuelve a pasar — no hay manera de deshacerlo.",
        "Sea estricto con el tiempo de las exposiciones: detrás viene la evaluación y no se puede "
        "recortar.",
    ],

    "ti_siguiente": {
        "tid": "Uso de IA para generación de ideas — completar el registro del taller (prompt, "
               "variantes, elección, correcciones con su origen, descartes y declaración del uso) en "
               "el documento del equipo.",
        "ti": "Corrección del prototipo: dejar el **v2 navegable** en la carpeta del equipo, con "
              "todas las correcciones aplicadas, y **conseguir a la persona ajena** que va a "
              "probarlo — solo el rol, no el nombre.",
        "adelanto": "arranca el **corte 3** con la **presentación de avances**: el prototipo se prueba "
                    "con una persona ajena al equipo y se recibe retroalimentación entre pares.",
        "aviso": "Para la sesión 12 traigan el prototipo v2 navegable **y la prueba ya hecha con una "
                 "persona ajena al equipo**, con la lista de lo que falló. Sin esa lista no hay nada "
                 "que presentar: la sesión 12 es sobre lo que salió mal, no sobre lo que se planeó.",
    },

    "cierre_titulo": "Cierra el corte 2 · Nos vemos en la sesión 12",
    "cierre_frase": "Pudieron corregir al asistente porque tenían sus decisiones escritas",
}
