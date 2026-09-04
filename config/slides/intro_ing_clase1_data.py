# -*- coding: utf-8 -*-
"""Contenido de la Clase 1 de Introduccion a la Ingenieria (FI300101) · 2026-2.

**Material general para cualquier grupo.** Aqui no hay fechas, ni horarios de reloj,
ni codigo de grupo: los tres grupos (SB141B, SB141C, LB141F) dictan esta misma clase.
Todo lo que cambia por grupo vive en el deck de Presentacion del Curso (Sesion 0), que
lo genera ``build_uniajc_intro_ing_curso.py`` desde el JSON del calendario.

Que hay aqui
------------
* ``OBJETIVOS``, ``AGENDA``            → diapositivas 2 y 3
* ``FUNDAMENTO``                       → «Fundamento teorico para el docente» del guion,
  dividido por diapositiva (estandar aprobado en ARQ Clase 1)
* ``CAMPOS``                           → los 5 campos de accion, uno por equipo
* ``ACTIVIDAD``, ``RUBRICA``           → la consigna de los 17 min y como se califica
* ``SOLUCION``                         → respuesta modelo del entregable (documento docente)
* ``DIAGNOSTICO``                      → los 13 items de la evaluacion diagnostica + que revela cada uno
* ``FAQ``, ``ERRORES``, ``ORALES``     → guion

Convencion de tildes: este modulo SI las lleva. Su texto acaba proyectado o impreso;
el problema de escapado que justificaba escribir sin tildes en los modulos de datos de
los talleres SQL no aplica aqui. Lo que nunca se usa es la comilla doble escapada
dentro de estas cadenas: se usan comillas angulares « ».
"""
from __future__ import annotations

CLASE_N = 1
SLUG = "Presentacion del curso y diagnostico inicial"
TITULO = "Presentación del curso y diagnóstico inicial"
SUBTITULO = "¿Qué hace un ingeniero de sistemas y para qué sirve lo que hace?"

# Sesion 1 es la unica que reparte los 45 min de teoria entre el encuadre del curso
# (deck de Sesion 0) y el diagnostico. Se documenta explicitamente para que el docente
# no llegue al minuto 40 creyendo que todavia le quedan 45 de tema.
NOTA_BLOQUE = (
    "La sesión 1 es la única del semestre en la que los 45 min de teoría se reparten: "
    "**30 min** de encuadre del curso (deck «Presentación del Curso», el del grupo) y "
    "**15 min** de evaluación diagnóstica. El tema propio de la clase se dicta dentro de "
    "esos 30 min y se cierra con la actividad de equipos."
)

OBJETIVOS = [
    "Distinguir la **Ingeniería de Sistemas** de la programación, y la **decisión de ingeniería** "
    "del conocimiento técnico que la soporta.",
    "Nombrar los **cinco campos de acción** del programa y decir, con un ejemplo, qué hace alguien "
    "que trabaja en cada uno.",
    "Detectar **un problema del entorno** propio y escribirlo con afectado y magnitud: es la semilla "
    "del proyecto que se evalúa en la sesión 6.",
    "Quedar en un **equipo estable** de los cinco del curso, con carpeta en la nube y vocero de la "
    "primera sesión definidos.",
]

# slots del timeline: reloj RELATIVO al arranque efectivo, porque el material es comun a
# los tres grupos y cada uno arranca a una hora distinta (14:40 / 14:40 / 18:40).
AGENDA = [
    {"t": "00:00–00:10 · 10 min",
     "label": "**Apertura** — pregunta de entrada en el muro mientras llegan"},
    {"t": "00:10–00:40 · 30 min",
     "label": "**Encuadre + tema** — de qué es este curso y qué es la ingeniería"},
    {"t": "00:40–00:55 · 15 min",
     "label": "**Diagnóstico** — 13 preguntas, no tiene nota"},
    {"t": "00:55–01:12 · 17 min",
     "label": "**Actividad** — ficha del campo, en equipos, en la nube"},
    {"t": "01:12–01:27 · 15 min",
     "label": "**Exposiciones** — 5 equipos × 3 min, con cronómetro"},
    {"t": "01:27–01:30 · 3 min",
     "label": "**Cierre** — una idea, la tarea y el tema de la sesión 2"},
]

PREGUNTA_ENTRADA = (
    "En una frase: ¿qué crees que hace un ingeniero de sistemas en su trabajo un martes "
    "cualquiera a las 10 de la mañana?"
)

# --------------------------------------------------------------- campos de accion

# Cinco campos, uno por equipo. La consigna de la actividad es la misma para los cinco;
# lo que cambia es el campo sorteado, para que las cinco exposiciones sumen el mapa
# completo del perfil en vez de repetirlo cinco veces.
CAMPOS = [
    {
        "n": 1,
        "nombre": "Desarrollo de software",
        "corto": "Construir el sistema",
        "que_hace": "Traduce una necesidad en un programa que funciona: entiende qué se necesita, "
                    "lo diseña, lo escribe, lo prueba y lo mantiene cuando el mundo cambia.",
        "ejemplo": "La aplicación con la que el estudiante consulta sus notas.",
        "confusion": "Que es «solo escribir código». Escribir es la parte corta; entender qué hay "
                     "que escribir y por qué es la parte larga.",
        "riesgo": "Un sistema que funciona para quien lo programó y no para quien lo usa: "
                  "se abandona y el dinero invertido se pierde.",
    },
    {
        "n": 2,
        "nombre": "Datos e inteligencia artificial",
        "corto": "Sacar decisiones de los datos",
        "que_hace": "Reúne datos dispersos, los limpia, los organiza y construye con ellos algo que "
                    "ayude a decidir: un informe, un indicador o un modelo que predice.",
        "ejemplo": "El sistema que estima cuántos estudiantes van a matricular el próximo semestre.",
        "confusion": "Que la inteligencia artificial «decide sola». Decide sobre los datos que alguien "
                     "eligió darle, y esa elección es una decisión de ingeniería.",
        "riesgo": "Un modelo entrenado con datos sesgados repite el sesgo a escala y con apariencia "
                  "de objetividad.",
    },
    {
        "n": 3,
        "nombre": "Infraestructura, redes y nube",
        "corto": "Que esté disponible",
        "que_hace": "Decide dónde corre el sistema, cómo llega al usuario y qué pasa cuando algo se "
                    "cae: servidores, redes, respaldos y capacidad.",
        "ejemplo": "Que la plataforma de matrículas no se caiga el día en que matriculan 6.000 personas.",
        "confusion": "Que «la nube» es internet o el disco de otra persona. Es un modelo de pago por "
                     "uso, y cada decisión de diseño cambia lo que se paga.",
        "riesgo": "Sin respaldo verificado, un solo fallo borra años de información. "
                  "Y un centro de datos mal dimensionado gasta energía que nadie usa.",
    },
    {
        "n": 4,
        "nombre": "Ciberseguridad",
        "corto": "Que no lo rompan",
        "que_hace": "Busca cómo podría fallar o ser atacado el sistema antes que otro lo encuentre, y "
                    "protege la información de las personas que confiaron en él.",
        "ejemplo": "Revisar que la app de la universidad no deje ver las notas de otro estudiante "
                   "cambiando un número en la dirección web.",
        "confusion": "Que es un antivirus. Es sobre todo diseño: la mayoría de las fugas de datos no "
                     "empiezan con un virus sino con un permiso mal puesto.",
        "riesgo": "Los datos personales filtrados no se pueden «devolver». El daño es de la persona "
                  "afectada, no de la empresa.",
    },
    {
        "n": 5,
        "nombre": "Gestión de proyectos y consultoría",
        "corto": "Que llegue a tiempo y sirva",
        "que_hace": "Coordina gente, plazos y dinero para que el sistema llegue a existir; traduce "
                    "entre quien tiene el problema y quien construye la solución.",
        "ejemplo": "Decidir qué se entrega en marzo y qué se posterga cuando el equipo se reduce a la mitad.",
        "confusion": "Que es «el que no hace nada técnico». Sin criterio técnico no se puede decidir "
                     "qué se recorta sin romper el resto.",
        "riesgo": "Prometer un alcance imposible: se entrega tarde, mal, o se entrega a costa de la "
                  "salud del equipo.",
    },
]

# ---------------------------------------------------------------- teoria proyectada

QUE_ES = [
    "@@Definición de trabajo para el semestre:@@ la ingeniería es el oficio de **decidir** cómo "
    "resolver un problema real **con recursos limitados**, y responder por las consecuencias de "
    "esa decisión.",
    "Las tres palabras que hacen el trabajo: **problema** (algo le duele a alguien concreto), "
    "**restricción** (tiempo, dinero, energía, personas, ley) y **consecuencia** (a quién afecta "
    "que se haga así y no de otra forma).",
    "Si no hay restricción, no hay ingeniería: hay un deseo. **Cualquiera puede resolver un problema "
    "con recursos infinitos.**",
    "@@La Ingeniería de Sistemas@@ es la que aplica ese oficio a los sistemas de información: "
    "software, datos, redes y las personas que los usan.",
    "El término «ingeniería de sistemas» nace en los años cuarenta, en proyectos de "
    "telecomunicaciones demasiado grandes para una sola especialidad. **La historia es el tema de "
    "la sesión 2**; hoy basta la idea: apareció cuando los sistemas dejaron de caber en una cabeza.",
]

NO_ES_CREENCIA = [
    "«Es programar todo el día.»",
    "«Es arreglar computadores e instalar Windows.»",
    "«El que sabe más lenguajes es el mejor ingeniero.»",
    "«Lo técnico es lo difícil; hablar con la gente es lo fácil.»",
    "«La respuesta correcta existe y está en internet.»",
]

NO_ES_REALIDAD = [
    "Programar es **una** de las cinco áreas, y en las otras cuatro se programa poco.",
    "Eso es soporte técnico: un oficio válido y distinto, que no requiere este título.",
    "El lenguaje se aprende en semanas. **Decidir con criterio** toma años y es lo que se evalúa.",
    "Casi todo proyecto que fracasa, fracasa porque **nadie entendió bien el problema**.",
    "Hay varias respuestas defendibles. Se elige una y **se argumenta el precio** que se paga.",
]

METODO = [
    ("Observar el entorno",
     "Encontrar algo que hoy funciona mal para alguien concreto. No «la ciudad», no «los "
     "usuarios»: una persona con un rol y un problema que se repite."),
    ("Medir el dolor",
     "Ponerle un número, aunque sea estimado: cuántas veces al día pasa, cuánto tiempo cuesta, "
     "cuánta gente afecta. Sin número no hay contra qué comparar la solución."),
    ("Decidir una solución y su precio",
     "Proponer qué se hace, con qué recursos y qué se sacrifica. Toda solución sacrifica algo: "
     "la respuesta correcta es la que dice qué."),
    ("Responder por las consecuencias",
     "Quién gana, quién pierde, qué gasta de energía, qué datos toca. Es la parte que separa la "
     "ingeniería de una buena idea."),
]

PROYECTO = [
    "@@Este curso no se aprueba con un examen final.@@ Se aprueba con un **proyecto de equipo** "
    "que arranca hoy y se expone en la Clase 15.",
    "**Qué es:** una propuesta de mejora tecnológica para un problema real del entorno de ustedes "
    "—el barrio, la universidad, el trabajo, la casa—. No hay que programarla: hay que **diseñarla "
    "y defenderla**.",
    "**Cómo se construye:** Clase 6, el problema y la propuesta inicial (cierra Corte 1) · "
    "Clases 7 a 11, el ciclo de vida y un prototipo (cierra Corte 2) · Clases 12 a 14, "
    "evaluación de impacto y ensayo · Clase 15, exposición final · Clase 16, informe.",
    "@@La semilla es la actividad de hoy:@@ el problema del entorno que su equipo escriba en los "
    "próximos 17 minutos es el candidato número uno a ser el proyecto del semestre.",
    "**Estrategia del curso:** ABPr, Aprendizaje Basado en Proyectos. La teoría de cada sesión "
    "entra porque el proyecto la necesita, no al revés.",
]

EQUIPOS = [
    "@@Cinco equipos, y son los mismos todo el semestre.@@ El proyecto es del equipo: cambiar de "
    "equipo en la sesión 9 significa empezar de cero.",
    "**Cuántos van en cada uno** depende de cuántos seamos hoy: si somos 25, equipos de 5; si "
    "somos 35, equipos de 7. **Lo fijo es el número de equipos, no el tamaño.**",
    "**Por qué cinco:** 5 equipos × 3 min = **15 min de exposiciones**, y el bloque cierra a los "
    "90 min. Con equipos de 4 personas y 35 matriculados serían 9 equipos y 27 min: no cabe.",
    "**El vocero rota cada sesión** y se anota en la bitácora del equipo. Al final del semestre "
    "todos han expuesto al menos dos veces. No hay «el que siempre habla».",
    "@@Hoy quedan tres cosas listas:@@ los integrantes, la **carpeta compartida en la nube** con "
    "permiso de lectura para el docente, y el **vocero de hoy**.",
]

# --------------------------------------------------------------------- actividad

ACTIVIDAD = {
    "titulo": "Ficha del campo de acción",
    "duracion_min": 17,
    "exposicion_min": 3,
    "entregable": "Una ficha de cinco bloques en la carpeta del equipo (Google Docs o Slides), "
                  "más el enlace de lectura entregado al docente antes de exponer.",
    "consigna": (
        "A cada equipo le corresponde uno de los cinco campos de acción de la Ingeniería de "
        "Sistemas. En 17 minutos completen la ficha de cinco bloques sobre SU campo y elijan qué "
        "van a decir en los 3 minutos de exposición."
    ),
    "bloques": [
        {"clave": "CAMPO",
         "pide": "El nombre del campo y una frase propia que explique de qué se ocupa. "
                 "No copiar la frase de la diapositiva.",
         "check": "La frase no sirve igual para otro de los cinco campos."},
        {"clave": "UN DÍA DE TRABAJO",
         "pide": "Tres tareas concretas que alguien de ese campo hace en una jornada. En verbo: "
                 "«revisa…», «escribe…», «negocia…».",
         "check": "Las tres son tareas, no cualidades. «Ser organizado» no es una tarea."},
        {"clave": "PROBLEMA DEL ENTORNO",
         "pide": "Un problema real que ustedes hayan visto y que ese campo podría mejorar. Con "
                 "**quién lo sufre** (un rol concreto) y **una cifra** que lo mida, aunque sea estimada.",
         "check": "No dice «los usuarios» ni «se pierde mucho tiempo». Dice quién y cuánto."},
        {"clave": "LO QUE NO ES",
         "pide": "Una confusión frecuente sobre ese campo y por qué es falsa.",
         "check": "Es una confusión sobre el campo, no un insulto a otra profesión."},
        {"clave": "SI SE HACE MAL",
         "pide": "Una consecuencia concreta —social, ambiental o económica— de hacer mal ese "
                 "trabajo. A quién le pasa y qué pierde.",
         "check": "La consecuencia le pasa a una persona identificable, no «a la sociedad»."},
    ],
    # Los textos empiezan por el contenido, sin repetir su propio rotulo: los documentos ya
    # los introducen con un prefijo en negrita y quedaba la frase dos veces seguidas.
    "reparto": "se sortea al azar delante del curso. En un curso de primer semestre nadie tiene "
               "información para elegir bien todavía, y sortear evita que los cinco equipos pidan "
               "«inteligencia artificial».",
    "plan_b": "el documento del equipo está en Drive, así que lo escrito no se pierde. Quien se "
              "cayó vuelve a entrar a la sala de su equipo o aporta por el documento, y si el que "
              "se cayó era el vocero expone el siguiente de la lista. La nota es del equipo.",
}

RUBRICA = [
    ("Los cinco bloques están completos", 20,
     "Un bloque vacío no se negocia: son 17 minutos y cinco bloques."),
    ("El problema del entorno tiene afectado con rol y una cifra", 30,
     "Es el bloque que alimenta el proyecto del semestre. Sin rol ni cifra, no sirve como semilla."),
    ("«Un día de trabajo» son tareas en verbo, no cualidades", 20,
     "Verifica que el equipo entendió qué se hace en el campo, no cómo suena."),
    ("La consecuencia de hacerlo mal le pasa a alguien identificable", 15,
     "Primer contacto con el RAA de ética y sostenibilidad; se retoma en las sesiones 4 y 5."),
    ("La exposición dura 3 min o menos y la hace el vocero", 15,
     "El cronómetro se proyecta. Pasarse de tiempo le quita minutos al equipo siguiente."),
]

# --------------------------------------------------------------- fundamento docente

FUNDAMENTO = [
    {
        "titulo": "Pregunta de entrada y para qué sirven los primeros diez minutos",
        "slide": "{{slide:¿Qué hace un ingeniero}}",
        "cuerpo": [
            "Los diez minutos de apertura existen porque el curso es virtual y entrar a una sesión "
            "nunca es instantáneo: hay quien viene de trabajar, quien pelea con el micrófono y quien "
            "entra desde el celular. Si se arranca a la hora exacta, la mitad del curso se pierde la "
            "primera explicación y hay que repetirla en pedazos cada vez que alguien entra. Pero "
            "esperar en silencio convierte diez minutos en tiempo muerto dieciséis veces al "
            "semestre, que son casi tres horas. La solución es que la pregunta de entrada quede en "
            "pantalla compartida desde el primer minuto y quien va entrando la responda en el muro "
            "del curso, sin crear cuenta.",
            "La pregunta de hoy es deliberadamente ingenua: «¿qué crees que hace un ingeniero de "
            "sistemas un martes a las 10 de la mañana?». No se busca la respuesta correcta, se "
            "busca el punto de partida. En un grupo de primer semestre las respuestas se agrupan "
            "casi siempre en tres montones: programar frente a un computador, arreglar computadores "
            "y algo vago sobre tecnología. Ese resultado es el material de la clase: al minuto 40, "
            "cuando se contrasten los cinco campos de acción, el docente vuelve al muro y muestra "
            "que ninguna de las respuestas del curso mencionó negociar un plazo, revisar un permiso "
            "mal puesto o decidir qué se recorta. Ese contraste hace el trabajo que un discurso "
            "sobre «el amplio campo de acción de la profesión» no hace.",
            "Nota operativa: no se corrige ninguna respuesta del muro en voz alta ni se señala a "
            "quien la escribió. Es el primer día de universidad de varios de ellos y el muro tiene "
            "que quedar como un lugar donde se puede escribir sin costo. Lo que se comenta es el "
            "patrón del conjunto, nunca una respuesta individual.",
        ],
    },
    {
        "titulo": "Qué es la evaluación diagnóstica y por qué se dice en voz alta que no tiene nota",
        "slide": "{{slide:diagnóstico}}",
        "cuerpo": [
            "El Plan de curso asigna a la sesión 1 una evaluación diagnóstica, y conviene entender "
            "para qué sirve antes de aplicarla, porque aplicada mal produce el efecto contrario al "
            "que busca. Un diagnóstico no mide conocimiento para calificarlo: mide de dónde parte "
            "el grupo para poder ajustar lo que sigue. Sus resultados cambian decisiones concretas "
            "del docente. Si la mayoría del grupo no distingue ingeniería de programación, la "
            "sesión 3 necesita más tiempo en análisis de caso y menos en herramientas. Si media "
            "clase entra solo con datos del celular, las actividades no pueden pedir subir video ni "
            "abrir cinco pestañas a la vez, y las salas de grupo se arman mezclando a quien tiene "
            "buena conexión con quien no la tiene. Si nadie ha usado una herramienta de "
            "diagramación, la sesión 2 empieza con cinco minutos de manejo de la herramienta y no "
            "se da por sabido.",
            "Hay que decir tres cosas en voz alta antes de repartirlo, y decirlas sin adornos. "
            "Primera: no tiene nota, ni suma ni resta. Segunda: no se espera que sepan las "
            "respuestas, y si supieran todo el curso no tendría razón de existir. Tercera: quien "
            "responde lo que cree que el profesor quiere oír arruina el instrumento, porque el "
            "docente va a planear las quince sesiones siguientes con esos datos. La tercera es la "
            "que hay que insistir: en primer semestre el reflejo aprendido en el colegio es "
            "adivinar la respuesta esperada, y ese reflejo hay que desactivarlo el primer día.",
            "Los últimos tres ítems del diagnóstico no son de contenido sino de condiciones de "
            "trabajo: computador propio, conexión en casa y horas de trabajo remunerado a la "
            "semana. Se preguntan porque determinan si el trabajo independiente semanal es viable "
            "tal como está planeado, y porque los equipos se pueden conformar mezclando "
            "condiciones en vez de dejar que se agrupen por afinidad y quede un equipo entero sin "
            "acceso a un computador. Estos tres ítems se responden de forma agregada: el docente "
            "necesita el conteo del grupo, no una ficha personal de cada estudiante. Conviene "
            "decirlo así, y no recoger nada que no se vaya a usar.",
        ],
    },
    {
        "titulo": "Ingeniería no es programación: la confusión que hay que desarmar el primer día",
        "slide": "{{slide:no es programación}}",
        "cuerpo": [
            "La creencia con la que llega casi todo el grupo es que Ingeniería de Sistemas es "
            "programar, y no es una creencia tonta: el mercado laboral, las series y los avisos de "
            "empleo la refuerzan. El problema es que si no se desarma hoy, produce dos efectos "
            "predecibles y costosos. El primero es que el estudiante que ya programa un poco "
            "concluye que este curso no le enseña nada y se desconecta, cuando es justamente el "
            "curso que le va a mostrar que su habilidad no responde ninguna de las preguntas que "
            "hacen fracasar los proyectos. El segundo es que el estudiante que no ha programado "
            "nunca concluye que se equivocó de carrera y empieza a considerar el retiro en las "
            "primeras semanas, que es cuando ocurre la mayor parte de la deserción de primer "
            "semestre.",
            "El desarme se hace con una comparación, no con una afirmación de autoridad. Programar "
            "es escribir las instrucciones que un computador ejecuta; es una habilidad que se "
            "aprende, que hoy además tiene asistentes que escriben buena parte del código, y que "
            "en cuatro de los cinco campos de acción de esta carrera se usa poco. La ingeniería es "
            "lo que va antes y después: decidir qué hay que construir, con qué restricciones, a "
            "costa de qué, y responder por lo que pase cuando funcione. Un ejemplo que aterriza en "
            "veinte segundos: dos equipos escriben el mismo programa de reservas con el mismo "
            "lenguaje; uno decide guardar los datos en el computador del cliente y el otro en un "
            "servidor compartido. El código se parece; las consecuencias no se parecen en nada "
            "cuando el cliente cambia de celular o cuando dos personas reservan el mismo turno al "
            "mismo tiempo. Esa diferencia es la ingeniería, y no está en el código.",
            "La segunda confusión, más frecuente en Cali de lo que uno esperaría, es con el soporte "
            "técnico: instalar sistemas operativos, cambiar memorias, limpiar equipos. Hay que "
            "responderla con respeto explícito, porque en el salón hay estudiantes que se pagan la "
            "carrera haciendo exactamente eso, y descalificar su trabajo el primer día los deja "
            "fuera. La formulación correcta es que el soporte técnico es un oficio válido, "
            "necesario y distinto, que no requiere cinco años de universidad, y que este programa "
            "forma para decidir qué sistema construir y por qué, no para mantener el que ya "
            "existe. Quien hoy hace soporte tiene una ventaja real en este curso: ya vio de primera "
            "mano lo que pasa cuando un sistema se diseñó mal.",
            "La tercera creencia es la del lenguaje: que el mejor ingeniero es el que sabe más "
            "lenguajes de programación. Un lenguaje se aprende en semanas y la lista de lenguajes "
            "de moda cambia cada pocos años; decidir con criterio toma años y no caduca. Vale "
            "cerrar diciendo qué se evalúa en este curso, porque el estudiante necesita saberlo "
            "hoy: no se evalúa saber, se evalúa **argumentar una decisión y decir su precio**.",
        ],
    },
    {
        "titulo": "Qué es la ingeniería: problema, restricción y consecuencia",
        "slide": "{{slide:Qué es la Ingeniería de Sistemas}}",
        "cuerpo": [
            "La definición que sostiene todo el semestre cabe en una frase: la ingeniería es el "
            "oficio de decidir cómo resolver un problema real con recursos limitados, y responder "
            "por las consecuencias de esa decisión. Las tres palabras que hacen el trabajo son "
            "problema, restricción y consecuencia, y conviene desarrollar cada una en voz alta "
            "porque los estudiantes van a usarlas las dieciséis sesiones.",
            "Problema significa que a alguien concreto le duele algo. «Mejorar la movilidad de "
            "Cali» no es un problema en este sentido, es un titular: no dice a quién, ni qué "
            "pierde, ni cuánto. «El auxiliar de la biblioteca lleva los préstamos en una hoja de "
            "cálculo que solo él puede abrir, y el semestre pasado se perdieron treinta y ocho "
            "cobros de multa porque nadie vio los vencimientos» sí es un problema: tiene un "
            "afectado con rol, una situación observable y una magnitud. La prueba rápida para "
            "saber si un enunciado es un problema o un deseo es preguntar si serviría igual para "
            "otro sistema cualquiera; si sirve igual, todavía no es un problema.",
            "Restricción es lo que hace que el oficio exista. Cualquiera resuelve un problema con "
            "tiempo infinito, dinero infinito y gente infinita; el trabajo aparece cuando hay tres "
            "meses, dos personas y ningún presupuesto. Las restricciones típicas son tiempo, "
            "dinero, personas disponibles, energía, capacidad de red, y también la ley: una "
            "solución que trate datos personales de terceros en Colombia está sujeta a la "
            "normativa de protección de datos, y eso limita el diseño igual que limita un "
            "presupuesto. Si un estudiante presenta una propuesta sin nombrar ninguna restricción, "
            "no presentó una propuesta de ingeniería.",
            "Consecuencia es la palabra que este programa toma en serio y muchos cursos técnicos "
            "no. Toda decisión de diseño reparte beneficios y costos entre personas distintas: un "
            "sistema de turnos que solo funciona en aplicación móvil excluye a quien no tiene "
            "teléfono con datos; un modelo que decide a quién se le aprueba un crédito hereda el "
            "sesgo de los datos con los que se entrenó; un servicio que se despliega sin apagar "
            "los servidores que dejó de usar gasta energía indefinidamente. Es útil dar un dato "
            "concreto porque el estudiante lo recuerda: según la Agencia Internacional de Energía, "
            "los centros de datos consumieron en 2024 alrededor del 1,5 % de la electricidad "
            "mundial, y esa cifra viene creciendo con la demanda de inteligencia artificial. El "
            "software no es inmaterial: se paga en kilovatios. Este hilo es el que abren las "
            "sesiones 4 y 5, dedicadas a ética y a sostenibilidad.",
            "Sobre la palabra «sistemas» conviene una aclaración breve y no extenderse, porque el "
            "detalle histórico es el tema de la sesión 2. La expresión ingeniería de sistemas nace "
            "en los años cuarenta en proyectos de telecomunicaciones y defensa que se volvieron "
            "demasiado grandes para una sola especialidad: había que coordinar decisiones que "
            "ninguna disciplina individual podía tomar sola. En Colombia el título de Ingeniería de "
            "Sistemas se orienta sobre todo a computación, software y datos, más cerca de lo que "
            "en el mundo anglosajón se llama ingeniería de software o computación que de la "
            "ingeniería de sistemas original. Vale decirlo hoy porque el estudiante que busque "
            "«systems engineering» en internet va a encontrar otra cosa y conviene que sepa por qué.",
        ],
    },
    {
        "titulo": "Los cinco campos de acción, y por qué se sortean en vez de elegirse",
        "slide": "{{slide:cinco campos}}",
        "cuerpo": [
            "Los cinco campos que este curso usa como mapa del perfil son desarrollo de software, "
            "datos e inteligencia artificial, infraestructura y nube, ciberseguridad, y gestión de "
            "proyectos y consultoría. No son las únicas categorías posibles ni una taxonomía "
            "oficial: son cinco divisiones reconocibles en las ofertas de empleo del país y, "
            "sobre todo, son cinco, que es exactamente el número de equipos del curso. Conviene "
            "decir en clase que es un mapa práctico y no una verdad, porque un estudiante puede "
            "preguntar por robótica, videojuegos o bioinformática, y la respuesta honesta es que "
            "son combinaciones de estos cinco vistas desde un dominio de aplicación.",
            "De cada campo el docente necesita poder decir dos cosas sin leer: qué hace alguien de "
            "ese campo en un día de trabajo, y qué se rompe si lo hace mal. Desarrollo de software "
            "traduce una necesidad en un programa que funciona y se puede mantener; si se hace mal, "
            "queda un sistema que funciona para quien lo escribió y no para quien lo usa, y se "
            "abandona. Datos e inteligencia artificial reúne información dispersa y construye con "
            "ella algo que ayude a decidir; si se hace mal, un modelo entrenado con datos sesgados "
            "repite el sesgo a escala y con apariencia de objetividad, que es peor que no tener "
            "modelo. Infraestructura y nube decide dónde corre el sistema y qué pasa cuando algo se "
            "cae; si se hace mal, un solo fallo borra años de información porque el respaldo existía "
            "en el papel pero nunca se probó. Ciberseguridad busca cómo podría ser atacado el "
            "sistema antes de que otro lo encuentre; si se hace mal, se filtran datos personales "
            "que no se pueden devolver, y el daño lo sufre la persona afectada, no la empresa. "
            "Gestión de proyectos coordina gente, plazos y dinero, y traduce entre quien tiene el "
            "problema y quien construye; si se hace mal, se promete un alcance imposible y se "
            "entrega tarde, incompleto, o a costa de la salud del equipo.",
            "Hay una confusión asociada a cada campo que conviene nombrar porque los estudiantes "
            "la traen. Que desarrollar es solo escribir código, cuando escribir es la parte corta. "
            "Que la inteligencia artificial decide sola, cuando decide sobre los datos que alguien "
            "eligió darle. Que la nube es internet o el disco de otra persona, cuando es un modelo "
            "de pago por uso en el que cada decisión de diseño cambia la factura. Que "
            "ciberseguridad es un antivirus, cuando la mayoría de las fugas empieza en un permiso "
            "mal configurado. Y que gestión de proyectos es el puesto de quien no hace nada "
            "técnico, cuando sin criterio técnico es imposible decidir qué se recorta sin romper el "
            "resto.",
            "El campo de cada equipo se sortea delante del curso y no se elige, y la razón hay que "
            "darla porque alguien va a protestar. En primer semestre nadie tiene todavía "
            "información para elegir bien: elegir se parecería a repartirse por lo que suena mejor, "
            "y en la práctica los cinco equipos pedirían inteligencia artificial. Sortear garantiza "
            "que las cinco exposiciones cubran el mapa completo y que ningún campo quede sin "
            "explorar. Vale añadir, porque tranquiliza, que el campo sorteado no compromete el "
            "proyecto del semestre: es el objeto de la ficha de hoy, no el tema del proyecto.",
        ],
    },
    {
        "titulo": "El método del curso y el proyecto que se evalúa",
        "slide": "{{slide:método del curso}} {{slide:El proyecto del curso}}",
        "cuerpo": [
            "El curso corre con la estrategia de Aprendizaje Basado en Proyectos, y eso tiene una "
            "consecuencia que hay que declarar hoy: la teoría de cada sesión entra porque el "
            "proyecto la necesita, no al revés. El proyecto es una propuesta de mejora tecnológica "
            "para un problema real del entorno del equipo, y no exige programar nada: exige "
            "diseñarla, evaluar su impacto y defenderla. Que no se programe es deliberado y "
            "conviene explicarlo, porque el estudiante que ya programa va a querer construir: en "
            "primer semestre el grupo todavía no tiene las herramientas técnicas, y si el proyecto "
            "se juzgara por lo construido, ganaría quien llegó sabiendo y el curso no habría "
            "enseñado nada.",
            "El método tiene cuatro pasos y son los mismos cuatro que la ficha de hoy practica en "
            "miniatura. Observar el entorno hasta encontrar algo que funciona mal para alguien "
            "concreto. Medir el dolor con un número, aunque sea estimado, porque sin número no hay "
            "contra qué comparar la solución después. Decidir una solución y decir su precio, es "
            "decir, qué se sacrifica, porque toda solución sacrifica algo y la propuesta correcta "
            "es la que lo dice. Y responder por las consecuencias: quién gana, quién pierde, qué "
            "energía gasta, qué datos toca.",
            "El arco del semestre conviene tenerlo claro para poder responder cuándo se hace cada "
            "cosa. En la sesión 6 se entrega el problema y la propuesta inicial, y ahí cierra el "
            "primer corte. Entre las sesiones 7 y 11 entra el ciclo de vida de un proyecto y se "
            "produce un prototipo, con lo que cierra el segundo corte. Entre las 12 y la 14 se "
            "evalúa el impacto de la propuesta y se ensaya. La 15 es la exposición final y la 16 el "
            "informe. Todo eso descansa sobre lo que se escriba hoy en el bloque «problema del "
            "entorno» de la ficha, y por eso ese bloque vale el treinta por ciento de la actividad "
            "de hoy: es la semilla, y una semilla vaga produce cinco meses de proyecto vago.",
        ],
    },
    {
        "titulo": "Los equipos: por qué cinco, por qué estables y qué queda listo hoy",
        "slide": "{{slide:cinco equipos}}",
        "cuerpo": [
            "El número de equipos es fijo en cinco y el tamaño es lo que varía con la cantidad de "
            "matriculados. La aritmética es la razón y conviene mostrarla en pantalla, porque "
            "planteada así nadie discute: cinco equipos por tres minutos son quince minutos de "
            "exposición, y el bloque de noventa minutos ya tiene comprometidos diez de apertura, "
            "cuarenta y cinco de teoría, diecisiete de actividad y tres de cierre. Si en vez del "
            "número se fijara el tamaño —«de cuatro en cuatro», que es lo que se hace por "
            "costumbre—, un grupo de treinta y cinco matriculados daría nueve equipos y "
            "veintisiete minutos de exposición, y la sesión se pasaría doce minutos todas las "
            "semanas. La única excepción prevista es un grupo con menos de diez matriculados, "
            "donde se baja a cuatro equipos y los tres minutos liberados se suman a la actividad.",
            "Los equipos son estables todo el semestre porque el proyecto es del equipo: cambiar de "
            "equipo en la sesión nueve significa empezar el proyecto de cero con cinco sesiones por "
            "delante. Lo que rota es el vocero, cada sesión, y se anota en la bitácora del equipo. "
            "Esa rotación no es un detalle administrativo: es lo que impide que exponga siempre el "
            "mismo y que los demás lleguen a la sesión quince sin haber hablado nunca en público. "
            "Con quince sesiones y cinco integrantes, cada persona expone al menos dos veces.",
            "Al conformar los equipos hoy conviene mezclar en vez de dejar que se agrupen por "
            "afinidad, y hay dos criterios concretos. El primero es el acceso a un computador: si "
            "los equipos se forman por amistad, es probable que quede un equipo entero sin equipo "
            "propio, y ese equipo va a arrastrar el problema quince semanas. Los tres últimos ítems "
            "del diagnóstico dan justamente ese dato. El segundo es la jornada laboral: un equipo "
            "en el que las cinco personas trabajan de día no va a poder reunirse fuera de clase, "
            "así que conviene repartir. Con eso, tres cosas tienen que quedar listas antes del "
            "cierre de hoy: los integrantes de cada equipo, la carpeta compartida en la nube con "
            "permiso de lectura para el docente, y el vocero de la sesión.",
        ],
    },
    {
        "titulo": "La actividad de hoy, cómo se corrige en caliente y cómo se expone en tres minutos",
        "slide": "{{slide:Actividad de hoy}} {{slide:Cómo se expone}}",
        "cuerpo": [
            "La consigna es la misma para los cinco equipos y lo único que cambia es el campo "
            "sorteado: así las cinco exposiciones suman el mapa completo del perfil en vez de "
            "repetirlo cinco veces. La ficha tiene cinco bloques —campo, un día de trabajo, "
            "problema del entorno, lo que no es, y si se hace mal— y se llena en diecisiete "
            "minutos en la carpeta del equipo en la nube. El docente no se queda en el escritorio "
            "durante esos diecisiete minutos: rota por los cinco equipos con un orden fijo, unos "
            "tres minutos en cada uno, y en cada parada revisa una sola cosa, el bloque del "
            "problema del entorno, porque es el que alimenta el proyecto del semestre y el único "
            "que no se puede arreglar después.",
            "Hay tres correcciones que se hacen en caliente y sin discusión, y conviene tenerlas "
            "memorizadas porque van a aparecer en los cinco equipos. La primera: el problema dice "
            "«los usuarios» o «la gente». Se pide un rol concreto en el momento y no se acepta el "
            "avance hasta que esté escrito. La segunda: el problema no tiene cifra y dice «se "
            "pierde mucho tiempo». Se pide un número aunque sea estimado y se acepta la "
            "estimación, porque el objetivo es que exista algo medible contra lo que comparar, no "
            "la exactitud del dato. La tercera: el problema describe la solución en vez del dolor, "
            "«el problema es que no tienen una aplicación». Se corrige recordando que el problema "
            "es lo que pasa hoy sin el sistema, y que si la solución ya está decidida antes de "
            "entender el problema, no hay nada que diseñar.",
            "Los tres minutos de exposición son cortos a propósito, y hay que decirlo antes de que "
            "empiecen porque el reflejo del primer semestre es leer la ficha completa en voz alta. "
            "Un guion que cabe en tres minutos tiene esta forma: treinta segundos para el campo y "
            "qué hace, un minuto para el problema del entorno con su afectado y su cifra, treinta "
            "segundos para la confusión frecuente, y un minuto para la consecuencia de hacerlo mal. "
            "El cronómetro se proyecta y se corta al llegar a cero, sin excepciones desde la "
            "primera sesión: si hoy se permite estirar, en la sesión quince las exposiciones "
            "finales no caben en el bloque. La retroalimentación no se da equipo por equipo, porque "
            "cinco rondas de comentarios no caben en quince minutos; se da toda junta en el cierre, "
            "con dos observaciones del conjunto y no una nota individual.",
            "Error del docente que conviene evitar en esta sesión: dictar los cuarenta y cinco "
            "minutos de encuadre y teoría y dejar la actividad para la sesión siguiente «porque hoy "
            "es el primer día». Si eso pasa, la sesión uno enseña al grupo que la dinámica anunciada "
            "es negociable, y recuperar esa disciplina en la sesión dos cuesta más que sostenerla "
            "hoy. La actividad de hoy es corta y sencilla precisamente para que quepa en el primer "
            "día y el grupo salga habiendo hecho el ciclo completo una vez.",
        ],
    },
]

FAQ = [
    {
        "p": "¿Este curso tiene programación? Yo no sé programar nada.",
        "r": "No, y no hace falta. Este curso es sobre decidir qué construir y por qué; la "
             "programación se aprende en otros cursos del programa. Quien no ha programado nunca "
             "no está en desventaja aquí, y quien ya programa no tiene ventaja: lo que se evalúa "
             "es argumentar una decisión, no escribir código.",
    },
    {
        "p": "¿Puedo cambiar de equipo si no me llevo bien con los míos?",
        "r": "Hasta la sesión 5, con aviso al docente y si los dos equipos quedan con tamaños "
             "viables. Desde la sesión 6 no, porque el problema del proyecto ya está entregado y "
             "cerrado, y cambiar de equipo sería empezar de cero. Si el problema es que alguien no "
             "trabaja, eso se resuelve en la bitácora del equipo, que registra quién hizo qué "
             "cada sesión.",
    },
    {
        "p": "¿Hay que pagar algo por las plataformas o poner una tarjeta?",
        "r": "No, nunca. Todas las herramientas del curso tienen plan gratuito permanente y se "
             "usan desde el navegador. Si alguna llega a pedir tarjeta de crédito, avisan y se "
             "cambia la herramienta: la regla es del curso, no de la herramienta.",
    },
    {
        "p": "¿Y si me toca un campo que no me interesa?",
        "r": "El campo sorteado es el objeto de la ficha de hoy, no el tema del proyecto del "
             "semestre. El proyecto lo elige el equipo en las sesiones siguientes y puede ser de "
             "cualquier campo, incluido uno que no le tocó a nadie.",
    },
    {
        "p": "¿Por qué empezamos diez minutos después de la hora?",
        "r": "Porque el curso es virtual y conectarse nunca es instantáneo: hay quien viene de "
             "trabajar y quien pelea con el micrófono. Esos diez minutos no son de descanso: la "
             "pregunta de entrada está en pantalla compartida y se responde en el muro. A la hora "
             "efectiva se arranca con el bloque de teoría, y ahí sí no se espera a nadie.",
    },
    {
        "p": "¿Hay examen final?",
        "r": "No hay examen escrito en todo el curso. El tercer corte, que vale el 40 %, son la "
             "exposición final del proyecto en la Clase 15 y el informe en la Clase 16. Lo que "
             "más pesa en los dos primeros cortes es lo que se hace en clase cada semana.",
    },
]

ERRORES = [
    "**Problema del entorno sin afectado concreto** («los usuarios», «la gente», «la ciudad»). Es "
    "el error que hay que cortar hoy porque arrastra todo el proyecto. Se pide un rol y no se "
    "acepta el avance del equipo hasta que esté escrito.",
    "**Problema sin cifra** («se pierde mucho tiempo», «es muy desorganizado»). Se pide un número "
    "aunque sea estimado; la estimación se acepta, la ausencia no.",
    "**Confundir el problema con la ausencia de la solución** («el problema es que no tienen una "
    "app»). El problema es lo que pasa hoy sin el sistema.",
    "**«Un día de trabajo» lleno de cualidades y no de tareas** («ser ordenado», «trabajar en "
    "equipo»). Se pide verbo más objeto: «revisa los permisos de acceso», «negocia el plazo con "
    "el cliente».",
    "**Leer la ficha completa en voz alta** en la exposición. Se corta a los 3 min. Conviene "
    "avisarlo antes de que empiecen y no después del primer equipo.",
    "**La consecuencia de hacerlo mal escrita como «afecta a la sociedad».** Se pide una persona "
    "identificable y qué pierde: es el primer contacto con el criterio ético que se evalúa en la "
    "sesión 4.",
]

ORALES = [
    "Diga una tarea de su campo que NO sea escribir código.",
    "¿Quién sufre el problema que escribieron? Dígame el rol, no «los usuarios».",
    "¿Qué se sacrifica si se resuelve ese problema como ustedes proponen?",
    "¿Cuál es la diferencia entre este curso y un curso de programación?",
]

# --------------------------------------------------------------------- diagnostico

DIAGNOSTICO = {
    "titulo": "Evaluación diagnóstica — Introducción a la Ingeniería",
    "duracion_min": 15,
    "nota": "SIN NOTA. No suma ni resta. Sirve para ajustar las 15 sesiones siguientes.",
    "instrucciones": [
        "Son 13 preguntas y hay 15 minutos. Si no sabe una respuesta, escriba «no sé»: es una "
        "respuesta válida y útil.",
        "No se evalúa. No busque la respuesta que cree que el profesor quiere leer: eso arruina el "
        "instrumento, porque con estos datos se planean las 15 sesiones que siguen.",
        "Las tres últimas preguntas son sobre condiciones de trabajo. Se usan de forma agregada "
        "(el conteo del grupo) para decidir cómo se arma el trabajo independiente y cómo se "
        "conforman los equipos.",
    ],
    "bloques": [
        {
            "nombre": "Bloque A · Qué cree que es la ingeniería (5 preguntas)",
            "items": [
                {
                    "n": 1,
                    "tipo": "cerrada",
                    "pregunta": "¿Cuál de estas frases describe mejor lo que hace un ingeniero de sistemas?",
                    "opciones": [
                        "Escribir programas de computador todo el día.",
                        "Decidir cómo resolver un problema con recursos limitados y responder por las consecuencias.",
                        "Instalar y reparar computadores y redes.",
                        "Investigar tecnologías nuevas y publicar artículos.",
                    ],
                    "clave": "b",
                    "revela": "Si más de la mitad del grupo marca (a) o (c), la diapositiva de «ingeniería "
                              "no es programación» necesita más tiempo y la sesión 3 (análisis de caso) "
                              "hay que reforzarla.",
                },
                {
                    "n": 2,
                    "tipo": "cerrada",
                    "pregunta": "Dos equipos escriben el mismo programa con el mismo lenguaje, pero uno guarda "
                                "los datos en el celular del usuario y el otro en un servidor. Esa diferencia es…",
                    "opciones": [
                        "un detalle de programación, sin importancia.",
                        "una decisión de arquitectura con consecuencias distintas para el usuario.",
                        "un error: solo una de las dos formas es correcta.",
                        "lo mismo, porque el programa hace lo mismo.",
                    ],
                    "clave": "b",
                    "revela": "Mide si el estudiante ya distingue «qué hace» de «cómo se decidió que lo "
                              "haga». Es la distinción que sostiene el curso completo.",
                },
                {
                    "n": 3,
                    "tipo": "cerrada",
                    "pregunta": "«Mejorar la movilidad de Cali» es, para efectos de este curso…",
                    "opciones": [
                        "un problema bien planteado.",
                        "un problema, pero le falta presupuesto.",
                        "un deseo: no dice a quién le duele, ni qué pierde, ni cuánto.",
                        "un objetivo de ingeniería civil, no de sistemas.",
                    ],
                    "clave": "c",
                    "revela": "Es el criterio con el que se calificará el bloque «problema del entorno» "
                              "hoy y el proyecto en la sesión 6. Si el grupo falla mucho aquí, conviene "
                              "dedicar más de los 3 min de rotación por equipo a este bloque.",
                },
                {
                    "n": 4,
                    "tipo": "abierta",
                    "pregunta": "Escriba en dos frases un problema de su entorno (barrio, casa, trabajo, "
                                "universidad) que crea que la tecnología podría mejorar. Diga quién lo sufre.",
                    "revela": "Es el dato más valioso del diagnóstico: da la lista de problemas reales del "
                              "grupo y adelanta candidatos al proyecto del semestre. Guardar las respuestas "
                              "para la sesión 6.",
                },
                {
                    "n": 5,
                    "tipo": "abierta",
                    "pregunta": "¿Por qué escogió Ingeniería de Sistemas? Una o dos frases.",
                    "revela": "Detecta a quien entró creyendo que era programación o soporte técnico, que es "
                              "el perfil con más riesgo de retiro en las primeras semanas. Vale hablar con "
                              "esas personas al final de la sesión.",
                },
            ],
        },
        {
            "nombre": "Bloque B · Qué sabe ya (5 preguntas)",
            "items": [
                {
                    "n": 6,
                    "tipo": "cerrada_multi",
                    "pregunta": "Marque todas las herramientas que ya ha usado alguna vez (aunque sea poco).",
                    "opciones": [
                        "Documentos o presentaciones en línea (Google Docs, Slides, Word en la web).",
                        "Alguna herramienta para hacer diagramas (draw.io, Canva, PowerPoint).",
                        "Un asistente de inteligencia artificial (ChatGPT, Gemini, Claude).",
                        "Ninguna de las anteriores.",
                    ],
                    "revela": "Define si la sesión 2 arranca con 5 min de manejo de la herramienta de "
                              "diagramación o se da por sabido, y si el uso de IA de las sesiones 3 y 11 "
                              "necesita una explicación previa.",
                },
                {
                    "n": 7,
                    "tipo": "cerrada",
                    "pregunta": "Un proyecto de ingeniería suele pasar por fases. ¿Cuál de estos órdenes tiene sentido?",
                    "opciones": [
                        "Construir → entender qué se necesita → probar → entregar.",
                        "Entender qué se necesita → diseñar → construir → probar → mantener.",
                        "Diseñar → entregar → entender qué se necesita → construir.",
                        "No hay orden: cada proyecto es distinto y no se puede generalizar.",
                    ],
                    "clave": "b",
                    "revela": "Punto de partida para el ciclo de vida de las sesiones 7 y 8. Si el grupo "
                              "acierta mayoritariamente, esas dos sesiones pueden ir más rápido en lo "
                              "conceptual y más despacio en el caso.",
                },
                {
                    "n": 8,
                    "tipo": "cerrada",
                    "pregunta": "El software que usamos todos los días…",
                    "opciones": [
                        "no consume energía: no tiene partes móviles.",
                        "consume energía solo en el celular o computador de quien lo usa.",
                        "consume energía también en centros de datos, y eso es parte del costo del diseño.",
                        "consume energía, pero es tan poca que no vale considerarla.",
                    ],
                    "clave": "c",
                    "revela": "Línea base para la sesión 5 (sostenibilidad e impacto ambiental). Casi "
                              "siempre falla, y el dato del 1,5 % de la electricidad mundial en centros "
                              "de datos funciona bien como corrección.",
                },
                {
                    "n": 9,
                    "tipo": "cerrada",
                    "pregunta": "Un ingeniero descubre que el sistema que construyó deja ver, cambiando un número "
                                "en la dirección web, las notas de otros estudiantes. El sistema ya está entregado "
                                "y funcionando. ¿Qué hace?",
                    "opciones": [
                        "Nada: el sistema ya se entregó y cumplió lo que se le pidió.",
                        "Lo reporta de inmediato a quien corresponda, aunque implique reconocer un error propio.",
                        "Lo arregla en silencio sin decirle a nadie.",
                        "Espera a que alguien lo reclame para no generar alarma.",
                    ],
                    "clave": "b",
                    "revela": "Línea base de la sesión 4 (rol social y ético). La opción (c) es la que "
                              "más se marca y es la interesante para discutir: arreglar sin reportar deja "
                              "a los afectados sin saber que sus datos estuvieron expuestos.",
                },
                {
                    "n": 10,
                    "tipo": "abierta",
                    "pregunta": "¿Qué espera saber HACER al terminar este semestre? Sea concreto.",
                    "revela": "Sirve para ajustar expectativas hoy mismo: quien responda «programar en "
                              "Python» necesita saber en esta sesión que ese no es el objetivo de este "
                              "curso, y en qué curso del programa sí lo es.",
                },
            ],
        },
        {
            "nombre": "Bloque C · Condiciones de trabajo (3 preguntas · se usan en conteo agregado)",
            "items": [
                {
                    "n": 11,
                    "tipo": "cerrada",
                    "pregunta": "¿Tiene computador propio disponible para trabajar fuera de clase?",
                    "opciones": [
                        "Sí, de uso propio.",
                        "Sí, pero compartido con la familia.",
                        "No, uso las salas de cómputo de la universidad.",
                        "No tengo acceso regular a un computador.",
                    ],
                    "revela": "Si hay respuestas (c) y (d), el trabajo independiente semanal tiene que "
                              "poder hacerse desde el celular, y esas personas se reparten entre equipos "
                              "distintos en vez de quedar juntas: en un curso virtual un equipo entero "
                              "con mala conexión no alcanza a producir nada en los 17 min de actividad.",
                },
                {
                    "n": 12,
                    "tipo": "cerrada",
                    "pregunta": "¿Tiene conexión a internet estable en casa?",
                    "opciones": [
                        "Sí.",
                        "Sí, pero lenta o intermitente.",
                        "Solo datos del celular.",
                        "No.",
                    ],
                    "revela": "Es el ítem más importante del bloque C, porque en un curso virtual la "
                              "conexión no es una comodidad: decide si la persona puede asistir. Las "
                              "respuestas (c) y (d) obligan a tres cosas: la grabación de la sesión "
                              "disponible en la carpeta del curso, actividades que funcionen con una sola "
                              "pestaña abierta, y aceptar la exposición grabada por el equipo cuando alguien "
                              "no logró sostener la sala.",
                },
                {
                    "n": 13,
                    "tipo": "cerrada",
                    "pregunta": "¿Trabaja de forma remunerada? ¿Cuántas horas a la semana, aproximadamente?",
                    "opciones": [
                        "No trabajo.",
                        "Menos de 20 horas.",
                        "Entre 20 y 40 horas.",
                        "Más de 40 horas.",
                    ],
                    "revela": "Determina si los equipos pueden reunirse fuera de clase. Conviene repartir "
                              "las jornadas entre equipos para que ninguno quede con las cinco personas "
                              "trabajando en el mismo horario.",
                },
            ],
        },
    ],
}

# ----------------------------------------------------------------------- solucion

SOLUCION_CAMPO = "Ciberseguridad"

SOLUCION = {
    "dominio": SOLUCION_CAMPO,
    "por_que_ese": (
        "La ficha modelo se resuelve sobre **Ciberseguridad** a propósito: es el campo que menos "
        "se conoce en primer semestre y el que produce las fichas más flojas. Tener resuelto el "
        "caso difícil sirve para calificar los cuatro fáciles. Si el equipo al que le tocó "
        "ciberseguridad entrega algo parecido a esto, es un 100."
    ),
    "bloques": [
        {
            "clave": "CAMPO",
            "respuesta": "**Ciberseguridad.** Se ocupa de encontrar cómo podría fallar o ser atacado un "
                         "sistema **antes** que alguien con malas intenciones, y de proteger la "
                         "información de las personas que confiaron en él.",
            "como_calificar": [
                "4 pts que la frase sea propia y no la de la diapositiva.",
                "No se acepta «protege de los hackers»: no dice de qué protege ni a quién.",
                "Se acepta cualquier formulación que contenga las dos ideas: anticipar el fallo y "
                "proteger información de terceros.",
            ],
        },
        {
            "clave": "UN DÍA DE TRABAJO",
            "respuesta": "1. **Revisa** los permisos de acceso de un sistema y busca cuentas que puedan "
                         "ver más de lo que les corresponde.\n"
                         "2. **Intenta romper** su propio sistema con las técnicas conocidas, y escribe "
                         "qué encontró y qué tan grave es.\n"
                         "3. **Explica** a un equipo que no es de seguridad por qué hay que cambiar algo "
                         "que hoy funciona, y negocia cuándo se hace.",
            "como_calificar": [
                "6 pts las tres tareas en verbo más objeto.",
                "La tercera tarea es la que separa una ficha buena de una ficha copiada de internet: "
                "casi nadie escribe que el trabajo incluye convencer a otros. Si aparece, súbale la nota.",
                "Se descuenta si alguna «tarea» es una cualidad: «ser desconfiado», «estar actualizado».",
            ],
        },
        {
            "clave": "PROBLEMA DEL ENTORNO",
            "respuesta": "En la papelería donde trabaja un compañero del equipo, **la dueña y los tres "
                         "empleados usan la misma clave** del computador de la caja, y esa clave está "
                         "escrita en un papel pegado al monitor. En el último año **se perdieron dos "
                         "veces las ventas del día** porque alguien borró el archivo sin querer y no se "
                         "supo quién. La dueña no puede saber quién hizo qué.",
            "como_calificar": [
                "9 pts (es el bloque que más pesa). 4 pts el afectado con rol concreto: «la dueña de "
                "la papelería», no «los usuarios». 4 pts la cifra: «dos veces en el último año». 1 pt "
                "que el problema sea observable por el equipo y no sacado de una noticia.",
                "**Si el problema no tiene rol o no tiene cifra, este bloque vale la mitad**, y hay "
                "que decirle al equipo por qué en la retroalimentación del cierre: es el bloque que "
                "alimenta el proyecto de la sesión 6.",
                "Se acepta una cifra estimada. No se acepta «muchas veces», «con frecuencia», "
                "«bastante».",
                "Se descuenta si el enunciado describe la solución («el problema es que no tienen "
                "contraseñas individuales») en vez del dolor.",
            ],
        },
        {
            "clave": "LO QUE NO ES",
            "respuesta": "**No es instalar un antivirus.** La mayoría de las fugas de información no "
                         "empieza con un virus, sino con un permiso mal puesto o una clave compartida —"
                         "como en el caso de arriba, donde ningún antivirus habría evitado nada.",
            "como_calificar": [
                "4 pts que la confusión sea sobre el campo y esté explicada, no solo negada.",
                "Vale mucho si el equipo conecta la confusión con su propio problema del entorno, como "
                "en la respuesta modelo. Es señal de que entendieron y no copiaron.",
                "No se acepta una confusión que descalifique otro oficio («no es ser el que arregla "
                "computadores porque eso es más fácil»).",
            ],
        },
        {
            "clave": "SI SE HACE MAL",
            "respuesta": "Si se filtran los datos de los clientes de la papelería —nombres, teléfonos, "
                         "qué compraron y a crédito—, **esa información no se puede devolver**. El daño "
                         "lo sufre el cliente, que empieza a recibir llamadas de estafa, no el negocio "
                         "que perdió el archivo. Y el cliente nunca decidió confiar en ese sistema: "
                         "confió en la papelería.",
            "como_calificar": [
                "4 pts que la consecuencia le pase a una persona identificable y se diga qué pierde.",
                "El punto que hay que reconocer y elogiar es el de la última frase: la persona "
                "afectada no es la que tomó la decisión técnica. Es exactamente el argumento de la "
                "sesión 4 y si un equipo de primer semestre lo produce solo, hay que decirlo en voz alta.",
                "No se acepta «afecta a la sociedad» ni «se pierde la confianza» sin decir de quién "
                "en quién.",
            ],
        },
    ],
    "otros_campos": [
        {
            "campo": "Desarrollo de software",
            "esperable": "El problema del entorno casi siempre es bueno aquí porque es el campo que más "
                         "conocen. Lo que falla es «un día de trabajo»: escriben tres formas de decir "
                         "«programa». Exija que una de las tres no incluya escribir código: entender el "
                         "requisito, probar, o mantener lo que ya existe.",
        },
        {
            "campo": "Datos e inteligencia artificial",
            "esperable": "Riesgo de ficha entusiasta y vacía, con «un día de trabajo» copiado de un "
                         "asistente de IA. La señal es un texto impecable sin nada del entorno del "
                         "equipo. Pregunte al vocero por el problema del entorno: si no lo puede "
                         "explicar en sus palabras, la ficha no es del equipo.",
        },
        {
            "campo": "Infraestructura, redes y nube",
            "esperable": "Suelen confundir el campo con el soporte técnico. Se corrige con la pregunta "
                         "«¿quién decide cuántos servidores se necesitan el día de matrículas?»: eso no "
                         "lo decide quien cambia una memoria.",
        },
        {
            "campo": "Gestión de proyectos y consultoría",
            "esperable": "El campo que produce las fichas más flojas después de ciberseguridad, porque "
                         "les parece «no técnico». Búsqueda concreta: que en «si se hace mal» aparezca "
                         "el costo humano de prometer un alcance imposible, y no solo «se entrega tarde».",
        },
    ],
    "cierre": (
        "Las cinco fichas quedan en la carpeta de cada equipo y no se vuelven a tocar hasta la "
        "**sesión 6**, cuando el bloque «problema del entorno» de las cinco fichas se pone sobre la "
        "mesa y cada equipo elige de ahí el problema de su proyecto. Conviene decirlo hoy en el "
        "cierre: lo que escribieron en 17 minutos es el material con el que van a trabajar cinco "
        "meses, y por eso vale la pena escribirlo bien."
    ),
}

TI_SIGUIENTE = {
    "tid": "Lectura del documento maestro del programa y mapa conceptual del perfil del ingeniero "
           "de sistemas (una hoja, a mano o en la herramienta que prefieran).",
    "ti": "Revisión de la historia de la Ingeniería de Sistemas: buscar tres hechos anteriores a "
          "1990 que hoy sigan afectando cómo se construye software, y traer la fuente de cada uno.",
    "tema_siguiente": "Sesión 2 · Historia y evolución de la ingeniería — se construye una línea de "
                      "tiempo por equipos en diagrams.net.",
    "aviso": "Quien no traiga los tres hechos no puede aportar a la línea de tiempo de su equipo, y "
             "la línea de tiempo es la actividad calificada de la sesión 2.",
}
