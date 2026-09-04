# -*- coding: utf-8 -*-
"""Las DOS evaluaciones de corte de Introduccion a la Ingenieria (FI300101) en ExamLab.

Son dos y solo dos. No es una omision:

  - Corte 1 · se entrega en la sesion de calendario 4 (Clase 6) · cubre las Clases 1 a 6
    · 20 min dentro de la sesion
  - Corte 2 · se entrega en la sesion de calendario 7 (Clase 11) · cubre las Clases 7 a 11
    · 20 min dentro de la sesion
  - Corte 3 · se cierra en la sesion de calendario 11 (Clases 15+16, doble) · NO tiene
    evaluacion escrita. El 40 % del corte se reparte en exposicion final 15 % (Clase 15)
    + informe final 20 % (Clase 16) + asistencia 5 %.

OJO con el vocabulario: desde que el curso paso de 16 a 11 sesiones de calendario (5
sesiones dobles, ver `clases_material`/`sesion_doble` en el JSON), «Sesion» (calendario,
1-11) y «Clase» (contenido del microcurriculo, 1-16) YA NO SON LO MISMO. Los numeros de
este archivo —el campo `sesion` de cada pregunta, `cubre`, `repaso[].sesion`— son
SIEMPRE numero de CLASE (contenido), estable pase lo que pase con el calendario. El unico
campo que es numero de SESION de calendario es `CORTE1["sesion"]`/`CORTE2["sesion"]` (la
fecha en que se entrega), y por eso lleva su propio comentario en la definicion.

Eso esta declarado en `config/calendario/introduccion_ingenieria_2026_2.json` (clave
`cortes`) y explicado en el docstring de `intro_ing_corte3_data.py`. Si alguien viene a
agregar una tercera evaluacion, la respuesta es que el corte 3 se evalua con producto,
no con examen.

Restricciones que vienen del material ya construido y que NO se pueden cambiar aqui
sin cambiar tambien el deck y el guion de las Clases 6 y 11:

  - Son **20 minutos** cronometrados, al final de la sesion, despues de las
    exposiciones. Lo dicen la agenda del deck (`agenda_slots`) y el plan minuto a
    minuto del guion: «01:07-01:27 · Evaluacion de corte».
  - Son **individuales**. El taller de la sesion es de equipo; la evaluacion no.
  - La del **corte 1 es de memoria**; la del **corte 2 es a libro abierto sobre los
    propios documentos del equipo**. Asi lo anuncian los dos guiones, y no es un
    detalle: la del corte 2 esta escrita a proposito para que solo la pueda responder
    rapido el equipo que documento. Cuatro de sus diez preguntas piden abrir el
    documento del equipo y copiar de ahi.
  - ExamLab **no es plataforma oficial de la UNIAJC**. El enlace se comparte en el chat
    de la reunion, nunca en la diapositiva, y eso hay que decirlo en voz alta.

Diseno del tiempo: 20 minutos no alcanzan para diez preguntas abiertas. Cada evaluacion
mezcla preguntas cerradas (rapidas, de reconocimiento) con abiertas cortas (donde se ve
el criterio). El reparto quedo asi:

  - Corte 1  · 7 cerradas ~= 6 min  + 3 abiertas ~= 12 min  -> 18 min, 2 de margen
  - Corte 2  · 6 cerradas ~= 5 min  + 4 abiertas ~= 14 min  -> 19 min, 1 de margen
    (el corte 2 aguanta una abierta mas porque es a libro abierto: copiar del propio
    documento es mas rapido que redactar de memoria)

Los distractores de las cerradas no son relleno: casi todos son contenido REAL de otra
sesion puesto donde no corresponde (Fortran 1957 y Royce 1970 como distractores del
hito de 1968, la Ley 1273 y la Ley 1672 como distractores de la Ley 1581). Un
distractor inventado se descarta por absurdo; uno verdadero fuera de lugar obliga a
discriminar, que es lo que se quiere medir.

Cada pregunta declara `sesion` (numero de CLASE, no de sesion de calendario: ver la nota
de vocabulario arriba), que es de donde sale. Sirve para dos cosas: revisar de un vistazo
que la evaluacion cubre todas las clases del corte, y responderle al estudiante que
reclama «eso no lo vimos» con el numero de clase.

Consume este modulo `build_uniajc_intro_ing_examlab.py`, que produce por corte:
    Kit docente/Clase N/ExamLab Corte X - Configuracion.md / .docx
    Kit docente/Clase N/ExamLab Corte X - CLAVE DOCENTE.md / .docx
    Kit docente/Clase N/ExamLab Corte X - Que vas a responder.md   (fuente)
    Clases/Clase N - <slug>/Evaluacion Corte X - Que vas a responder.docx
"""

# =============================================================================
# CORTE 1 · entrega en sesion 4 (Clase 6) · cubre Clases 1 a 6 · 20 min · individual · de memoria
# =============================================================================

CORTE1 = {
    "corte": 1,
    "clase": 6,    # numero de CLASE (carpeta Kit docente/Clases): NO cambia con el calendario
    "sesion": 4,   # sesion de CALENDARIO en que se entrega (Clase 6, ver clases_material)
    "cubre": "1 a 6",   # rango de CLASES (contenido), no de sesiones de calendario
    "minutos": 20,
    "libro_abierto": False,
    "titulo": "Evaluacion del Corte 1 - Que es la ingenieria, el sistema, la etica y el problema",
    "resumen": (
        "Diez preguntas sobre las Clases 1 a 6: qué es y qué no es la ingeniería, historia "
        "y hitos, los cinco elementos de un sistema, principios éticos y normas colombianas, "
        "la huella ambiental de un sistema, y la diferencia entre problema, síntoma y solución "
        "disfrazada. Es individual, se responde en los últimos 20 minutos de la sesión y no "
        "se consulta material."
    ),
    "por_que_asi": (
        "La evaluación del corte 1 es **de memoria** porque lo que mide son las distinciones "
        "que el estudiante tiene que llevar puestas el resto del semestre: problema contra "
        "síntoma, sistema contra software, ético contra legal. Si se responde consultando, no "
        "se sabe si las distinguen o si saben buscar en el documento. La del corte 2 sí es a "
        "libro abierto, y ahí el criterio cambia: lo que se mide es que el equipo documentó."
    ),
    "cierre": "los últimos 20 minutos de la sesión 4 del calendario (Clase 6), después de las exposiciones",
    # Lo que recibe el ESTUDIANTE. No es el listado de las diez preguntas: publicar los
    # diez titulos cinco sesiones antes convierte una evaluacion de criterio en la
    # memorizacion de diez respuestas. Es una guia de repaso por sesion, y esta escrita
    # para que quien la siga pueda responder la evaluacion — no para que la adivine.
    "repaso": [
        {
            "sesion": 1,
            "tema": "Qué es y qué no es la ingeniería",
            "revise": [
                "Las tres palabras de la definición del curso, y por qué sin una de ellas "
                "hay un deseo y no un problema de ingeniería.",
                "Las cinco creencias que se desmontaron en la sesión, con su realidad al "
                "lado. Sabérselas de a pares: la creencia sola no sirve.",
                "Los cuatro pasos del método: observar, medir, decidir con su precio, y "
                "responder por las consecuencias.",
            ],
        },
        {
            "sesion": 2,
            "tema": "Historia y hitos de la ingeniería",
            "revise": [
                "Los seis hitos con su fecha y en una frase qué propuso cada uno. Las "
                "fechas importan: cuatro de los seis se parecen y hay que distinguirlos.",
                "De cada hito, qué dolía ANTES y a quién. Es lo que la mayoría no repasa "
                "y es la mitad de lo que se pregunta.",
                "Prepare, para el hito que más le interese, una frase propia sobre qué "
                "parte de ese problema sigue abierta hoy.",
            ],
        },
        {
            "sesion": 3,
            "tema": "El sistema y sus elementos",
            "revise": [
                "Los cinco elementos de un sistema, de memoria y sin confundirlos con "
                "piezas de software (una base de datos no es un elemento del sistema).",
                "Por qué el sistema no es el software: practique describir un caso "
                "cotidiano como sistema, sin nombrar ni una pantalla.",
                "Cómo se identifica un actor, incluido el que no va a usar la solución y "
                "sí sufre el resultado. Y qué es una decisión de frontera.",
            ],
        },
        {
            "sesion": 4,
            "tema": "Ética, normas y responsabilidad",
            "revise": [
                "Las cuatro normas colombianas por su número y por lo que regula cada "
                "una: 1581 de 2012, 1273 de 2009, 1672 de 2013 y 842 de 2003. Se "
                "confunden entre sí, y ahí está la pregunta.",
                "Por qué legal y ético no son lo mismo, con el caso que se usó en clase.",
                "Por qué «yo solo programé lo que me pidieron» no protege, y qué sí: "
                "dejar el riesgo por escrito y escalar temprano.",
            ],
        },
        {
            "sesion": 5,
            "tema": "Huella ambiental de un sistema",
            "revise": [
                "Las cuatro etapas de la huella de un sistema, y qué entra en cada una. "
                "Ojo con lo que parece una quinta etapa y está dentro de otra.",
                "Qué mide el PUE, en sus propias palabras.",
            ],
        },
        {
            "sesion": 6,
            "tema": "Problema, síntoma y solución disfrazada",
            "revise": [
                "Cómo se distingue un síntoma de un problema y de una solución "
                "disfrazada. Practique con tres frases que oiga esta semana.",
                "Cómo se escribe un problema bien planteado: a quién le pasa qué, con "
                "qué consecuencia, y sin nombrar la solución.",
                "Qué es una línea base y por qué tiene que ser algo que se pueda contar.",
            ],
        },
    ],
    "preguntas": [
        {
            "sesion": 1,
            "tipo": "cerrada",
            "puntos": 7,
            "enunciado": (
                "## 1. Cuando hay ingenieria y cuando hay un deseo\n\n"
                "Un estudiante propone este proyecto: «vamos a hacer una plataforma que "
                "resuelva la movilidad de Cali, con la tecnología que haga falta y el tiempo "
                "que sea necesario».\n\n"
                "Según la definición de trabajo que usa este curso, ¿qué le falta a esa frase "
                "para ser un problema de ingeniería?"
            ),
            "opciones": [
                "Le falta la **restricción**: sin límite de tiempo, dinero, energía o personas "
                "cualquiera resuelve cualquier cosa, y entonces no hay nada que decidir.",
                "Le falta decir con qué lenguaje de programación se va a construir.",
                "Le falta que sea un problema de software: la movilidad no es un problema de "
                "ingeniería de sistemas.",
                "No le falta nada: nombra un problema real y propone una solución, que es lo "
                "que se pide.",
            ],
            "correctas": [0],
            "respuesta_modelo": (
                "La restricción. La definición del curso tiene tres palabras: problema, "
                "restricción y consecuencia. «El tiempo que sea necesario» borra la "
                "restricción, y sin restricción no hay ingeniería: hay un deseo."
            ),
            "rubrica": "7 puntos si marca la primera. 0 en cualquier otra. No hay puntaje parcial.",
            "error_comun": (
                "Marcar la segunda. Elegir tecnología se siente como «lo técnico», pero la "
                "tecnología es una decisión posterior y de hecho no va en el enunciado del "
                "problema (regla de la sesión 6)."
            ),
        },
        {
            "sesion": 1,
            "tipo": "cerrada_multi",
            "puntos": 8,
            "enunciado": (
                "## 2. Que es falso sobre el oficio\n\n"
                "Marque **todas** las afirmaciones que son FALSAS según lo trabajado en la "
                "sesión 1."
            ),
            "opciones": [
                "«Ser ingeniero de sistemas es programar todo el día.»",
                "«El que sabe más lenguajes de programación es el mejor ingeniero.»",
                "«Para cada problema de ingeniería existe una única respuesta correcta, y está "
                "en internet.»",
                "«La mayoría de los proyectos que fracasan, fracasan porque nadie entendió bien "
                "el problema.»",
                "«Instalar sistemas operativos y arreglar computadores es soporte técnico: un "
                "oficio válido y distinto de este.»",
            ],
            "correctas": [0, 1, 2],
            "respuesta_modelo": (
                "Falsas: las tres primeras. Programar es una de las cinco áreas y en las otras "
                "cuatro se programa poco; el lenguaje se aprende en semanas y lo que toma años "
                "es decidir con criterio; y hay varias respuestas defendibles, se elige una y "
                "se argumenta el precio. Las dos últimas son verdaderas."
            ),
            "rubrica": (
                "8 puntos con las tres correctas y ninguna incorrecta. 4 puntos con dos "
                "correctas y ninguna incorrecta. 0 si marca alguna de las dos verdaderas."
            ),
            "error_comun": (
                "Marcar la cuarta. Suena a acusación y por eso parece falsa, pero es "
                "exactamente lo que se dijo en la sesión 1 y se repitió en la 6."
            ),
        },
        {
            "sesion": 2,
            "tipo": "cerrada",
            "puntos": 7,
            "enunciado": (
                "## 3. Que paso en 1968 y por que importa\n\n"
                "¿Cuál de estos hechos corresponde a 1968 y por qué se lo considera el "
                "nacimiento de la disciplina?"
            ),
            "opciones": [
                "La OTAN convocó una conferencia en Garmisch y ahí se acuñó el término "
                "«ingeniería de software», porque los proyectos grandes se estaban pasando de "
                "plazo y de presupuesto de forma escandalosa.",
                "Se creó el primer lenguaje de alto nivel, y eso permitió dejar de programarle "
                "a la máquina en su propio idioma.",
                "Se publicó el esquema de fases que se popularizó como «cascada», y por primera "
                "vez quedó claro en qué orden se hace el trabajo.",
                "Se demostró que meter más programadores a un proyecto atrasado lo atrasa "
                "todavía más.",
            ],
            "correctas": [0],
            "respuesta_modelo": (
                "La primera. Y lo importante del hito no es la fecha: la disciplina no nace de "
                "un invento sino del reconocimiento público de que el trabajo se estaba "
                "haciendo mal y nadie sabía cómo hacerlo bien."
            ),
            "rubrica": "7 puntos si marca la primera. 0 en cualquier otra.",
            "error_comun": (
                "Marcar la tercera. Los tres distractores son hitos reales de otras fechas "
                "(Fortran 1957, Royce 1970, Brooks 1975): quien confunde 1968 con 1970 no tiene "
                "clara la diferencia entre nombrar el problema y proponer un método."
            ),
        },
        {
            "sesion": 2,
            "tipo": "abierta",
            "puntos": 13,
            "enunciado": (
                "## 4. Un hito, y la parte del problema que sigue viva\n\n"
                "Elija **uno** de los seis hitos de la sesión 2 (1945-1957 · 1968 · 1970 · "
                "1975 · 1991-2001 · 2006-hoy) y responda en **tres frases**, una por línea:\n\n"
                "1. Qué dolía antes del hito, y a quién.\n"
                "2. Qué propuso el hito, en una frase y sin nombres técnicos que usted no pueda "
                "explicar.\n"
                "3. Qué parte de ese problema **sigue abierta hoy**.\n\n"
                "La tercera frase tiene que ser suya: no repita la tarjeta de la diapositiva."
            ),
            "respuesta_modelo": (
                "Ejemplo con 1975 (el mes-hombre mítico):\n\n"
                "1. Dolía a los jefes de proyecto: cuando un proyecto se atrasaba, la única "
                "reacción disponible era meter más gente, y el proyecto se atrasaba más.\n"
                "2. Brooks mostró que sumar personas suma también los canales de comunicación "
                "entre ellas, y eso crece más rápido que la capacidad de trabajo que se agregó.\n"
                "3. Sigue abierta la decisión de cuándo un equipo ya es demasiado grande. Se "
                "sigue reaccionando al atraso contratando, y en un trabajo de curso pasa igual: "
                "un equipo de cinco que se reparte mal pierde más tiempo coordinando que "
                "haciendo.\n\n"
                "Cualquiera de los seis hitos sirve. Lo que se califica es la estructura de las "
                "tres frases, no cuál eligió."
            ),
            "rubrica": (
                "13 puntos repartidos así:\n\n"
                "- **4 pts** · qué dolía antes, con el afectado nombrado (un rol, no «la "
                "sociedad»). 2 pts si dice el problema pero no a quién le pasaba.\n"
                "- **4 pts** · qué propuso, en una frase entendible. 2 pts si usa un término "
                "técnico como respuesta completa («propuso la cascada») sin explicar qué es.\n"
                "- **5 pts** · qué sigue vivo hoy, con algo propio. 5 pts si trae un ejemplo o "
                "una consecuencia actual; 2 pts si repite la tarjeta de la diapositiva; 0 si "
                "dice que el problema ya se resolvió.\n\n"
                "No se descuenta por escoger un hito «fácil»: los seis valen igual."
            ),
            "error_comun": (
                "Contestar «ya se resolvió». Es justo lo que la sesión 2 marcó como falso: los "
                "informes de la industria siguen reportando fracasos de plazo, costo y alcance. "
                "El método mejoró; el problema no desapareció."
            ),
        },
        {
            "sesion": 3,
            "tipo": "cerrada_multi",
            "puntos": 10,
            "enunciado": (
                "## 5. Los elementos de un sistema\n\n"
                "Marque **todos** los que son uno de los cinco elementos de un sistema, según "
                "la sesión 3."
            ),
            "opciones": [
                "Entradas",
                "Proceso",
                "Salidas",
                "Retroalimentación",
                "Frontera",
                "Base de datos",
                "Interfaz de usuario",
                "Presupuesto del proyecto",
            ],
            "correctas": [0, 1, 2, 3, 4],
            "respuesta_modelo": (
                "Entradas, proceso, salidas, retroalimentación y frontera. Las otras tres son "
                "piezas de una solución posible, no elementos de un sistema: un sistema puede "
                "existir sin base de datos y sin pantalla."
            ),
            "rubrica": (
                "10 puntos con los cinco y ninguno de más. 6 puntos con cuatro de cinco y "
                "ninguno de más. 0 si marca base de datos, interfaz o presupuesto."
            ),
            "error_comun": (
                "Marcar «base de datos» e «interfaz de usuario». Es el error que da nombre a la "
                "sesión: confundir el sistema con el software que lo soporta."
            ),
        },
        {
            "sesion": 3,
            "tipo": "abierta",
            "puntos": 15,
            "enunciado": (
                "## 6. El sistema no es el software\n\n"
                "En un centro de salud hay 40 personas en fila desde las 5 de la mañana, porque "
                "las citas se asignan por orden de llegada. Un equipo propone «una app para "
                "pedir cita».\n\n"
                "Responda las tres cosas:\n\n"
                "1. El problema escrito como **sistema** y no como pantalla: una frase que diga "
                "a quién le pasa qué, con qué consecuencia.\n"
                "2. **Tres actores** del sistema, y entre ellos **uno que no va a usar la app y "
                "sí sufre el resultado**.\n"
                "3. **Una decisión de frontera**: algo que usted deja FUERA del sistema, y por "
                "qué lo deja fuera."
            ),
            "respuesta_modelo": (
                "1. «Los pacientes del centro de salud hacen fila desde las 5 de la mañana "
                "porque las citas se asignan por orden de llegada, y quien no puede madrugar "
                "—por trabajo o por edad— se queda sin cita.»\n\n"
                "2. Paciente, secretaria que asigna, médico que recibe la agenda. El que no usa "
                "la app y sí sufre el resultado: el médico, que recibe una agenda desordenada; "
                "o el vecino mayor que no tiene celular y ahora consigue menos citas que antes. "
                "Ese último es la mejor respuesta, porque es el actor que la solución "
                "perjudica.\n\n"
                "3. «Dejo fuera el transporte del paciente hasta el centro de salud: aunque es "
                "parte del problema real, el equipo no puede intervenirlo en un semestre.» "
                "Sirve cualquier frontera con su razón escrita."
            ),
            "rubrica": (
                "15 puntos repartidos así:\n\n"
                "- **5 pts** · el problema como sistema, con afectado y consecuencia. 2 pts si "
                "dice el hecho («hay fila») sin la consecuencia. 0 si responde con la solución "
                "(«hacer una app»).\n"
                "- **6 pts** · tres actores (3 pts) y el actor que no usa la app y sí sufre "
                "(3 pts). Este último es el que discrimina: si los tres actores son «usuario, "
                "administrador y sistema», 1 pt en total.\n"
                "- **4 pts** · la decisión de frontera CON su razón. 2 pts si dice qué deja "
                "fuera y no por qué. 0 si no hay frontera.\n\n"
                "No exija que la frontera sea la «correcta»: no hay una. Exija que esté "
                "defendida."
            ),
            "error_comun": (
                "Poner «el sistema» o «la app» como actor. Un actor es una persona o un grupo "
                "afectado; el sistema no es actor de sí mismo."
            ),
        },
        {
            "sesion": 4,
            "tipo": "cerrada",
            "puntos": 10,
            "enunciado": (
                "## 7. Que norma colombiana aplica\n\n"
                "Un equipo quiere publicar en su prototipo la lista de morosos de la biblioteca "
                "del barrio, con nombre completo y teléfono, para presionar la devolución. "
                "Nadie les pidió permiso a esas personas.\n\n"
                "¿Cuál es la norma colombiana que se está incumpliendo?"
            ),
            "opciones": [
                "Ley 1581 de 2012, de protección de datos personales: no hay autorización "
                "previa del titular, y el principio de finalidad no cubre ese uso.",
                "Ley 1273 de 2009, de delitos informáticos: hay acceso abusivo a un sistema "
                "informático.",
                "Ley 1672 de 2013, de residuos de aparatos eléctricos y electrónicos.",
                "Ley 842 de 2003: el equipo todavía no tiene matrícula profesional, así que no "
                "puede publicar nada.",
            ],
            "correctas": [0],
            "respuesta_modelo": (
                "La Ley 1581 de 2012. El dato es personal, no hay autorización previa y la "
                "finalidad declarada (presionar) no es una finalidad legítima informada al "
                "titular. Es además la regla del curso: se usa el rol, no el nombre."
            ),
            "rubrica": "10 puntos si marca la primera. 0 en cualquier otra.",
            "error_comun": (
                "Marcar la 1273. Las dos son de datos, pero la 1273 castiga acceder o "
                "interceptar sin autorización; aquí el equipo tiene los datos legítimamente y "
                "el problema es qué hace con ellos."
            ),
        },
        {
            "sesion": 4,
            "tipo": "cerrada_multi",
            "puntos": 10,
            "enunciado": (
                "## 8. La defensa que no funciona\n\n"
                "Marque **todas** las afirmaciones correctas sobre la frase «yo solo programé "
                "lo que me pidieron», según la sesión 4."
            ),
            "opciones": [
                "No funciona legalmente: en el caso Volkswagen un ingeniero que ejecutó la "
                "orden se declaró culpable y fue condenado a prisión.",
                "No funciona profesionalmente: el primer principio del código ACM/IEEE pone el "
                "interés público por encima del cliente y del empleador.",
                "Lo que sí protege, y además ayuda a que la decisión se corrija, es dejar por "
                "escrito el riesgo y a quién afecta, y escalarlo temprano.",
                "Funciona mientras lo que se pidió sea legal, porque la ley es el criterio "
                "final de lo que está bien.",
                "La responsabilidad es solo de quien firma el proyecto, no de quien lo ejecuta.",
            ],
            "correctas": [0, 1, 2],
            "respuesta_modelo": (
                "Correctas: las tres primeras. La cuarta es falsa porque la ley es el mínimo y "
                "muchas cosas legales son indefendibles (Cambridge Analytica era legal). La "
                "quinta es falsa porque el que firma responde y el que ejecuta también."
            ),
            "rubrica": (
                "10 puntos con las tres y ninguna de más. 5 puntos con dos y ninguna de más. "
                "0 si marca la cuarta o la quinta: son las dos creencias que la sesión desmontó."
            ),
            "error_comun": (
                "Marcar la cuarta. Es la confusión central de la sesión: legal y ético no son "
                "lo mismo, y la ley es el piso, no el techo."
            ),
        },
        {
            "sesion": 5,
            "tipo": "cerrada_multi",
            "puntos": 10,
            "enunciado": (
                "## 9. Las etapas de la huella de un sistema\n\n"
                "Marque **todas** las que son una de las cuatro etapas de la huella material de "
                "un sistema de software, según la sesión 5."
            ),
            "opciones": [
                "Fabricación",
                "Uso",
                "Red",
                "Fin de vida",
                "Enfriamiento del centro de datos",
                "Programación del software",
            ],
            "correctas": [0, 1, 2, 3],
            "respuesta_modelo": (
                "Fabricación, uso, red y fin de vida. El enfriamiento del centro de datos no es "
                "una quinta etapa: está dentro de «uso», y es justamente lo que mide el PUE "
                "(energía total del centro dividida por la que llega a los servidores)."
            ),
            "rubrica": (
                "10 puntos con las cuatro y ninguna de más. 6 puntos con tres y ninguna de más. "
                "0 si marca «enfriamiento» o «programación»."
            ),
            "error_comun": (
                "Marcar el enfriamiento. Se nombró mucho en clase porque cambia la cuenta, y "
                "por eso se recuerda como etapa aparte. Es el distractor que discrimina entre "
                "recordar palabras y entender el reparto."
            ),
        },
        {
            "sesion": 6,
            "tipo": "abierta",
            "puntos": 10,
            "enunciado": (
                "## 10. Sintoma, problema o solucion disfrazada\n\n"
                "Clasifique cada una de estas tres frases como **síntoma**, **problema** o "
                "**solución disfrazada**:\n\n"
                "a) «Falta una app para la tienda del barrio.»\n"
                "b) «Los clientes se quejan de las entregas.»\n"
                "c) «El inventario se lleva en un cuaderno.»\n\n"
                "Después elija **una sola** de las tres, reescríbala como problema bien "
                "planteado (a quién le pasa qué, con qué consecuencia) e indique **qué cifra** "
                "mediría hoy como línea base.\n\n"
                "Responda en cuatro líneas: tres clasificaciones y la frase reescrita con su "
                "cifra."
            ),
            "respuesta_modelo": (
                "a) Solución disfrazada — la app es la respuesta y falta la pregunta.\n"
                "b) Síntoma — la queja es la señal, no el problema. ¿Se queja de qué?\n"
                "c) Casi un problema, pero descrito por el cómo: «manual» no dice a quién le "
                "cuesta qué. Se acepta como síntoma o como solución disfrazada solo si el "
                "estudiante explica por qué.\n\n"
                "Reescritura de (c): «El dueño de la tienda pierde ventas porque no sabe qué se "
                "agotó hasta que un cliente lo pide, y reponer tarda dos días.»\n"
                "Línea base: número de productos agotados encontrados en un conteo de una "
                "semana, o número de veces al día que un cliente pide algo que no hay. Medido "
                "contando, no estimado; y si es estimación, se escribe «estimado»."
            ),
            "rubrica": (
                "10 puntos repartidos así:\n\n"
                "- **4 pts** · las tres clasificaciones (a: solución disfrazada, b: síntoma). "
                "La (c) se acepta con cualquiera de las dos etiquetas SI viene justificada; sin "
                "justificación, no puntúa.\n"
                "- **4 pts** · la reescritura con afectado y consecuencia. 2 pts si nombra al "
                "afectado y no la consecuencia.\n"
                "- **2 pts** · la cifra, si es algo que de verdad se puede contar esta semana. "
                "0 pts a «medir la satisfacción del cliente»: no se puede contar.\n\n"
                "Que la cifra sea distinta a la del modelo no resta: lo que resta es que no se "
                "pueda medir."
            ),
            "error_comun": (
                "Reescribir el problema metiendo la solución («el dueño necesita un sistema "
                "de inventario»). Es la misma solución disfrazada de la frase (a), con otras "
                "palabras."
            ),
        },
    ],
}


# =============================================================================
# CORTE 2 · entrega en sesion 7 (Clase 11) · cubre Clases 7 a 11 · 20 min · individual · LIBRO ABIERTO
# =============================================================================
# Cuatro de las diez preguntas piden abrir el documento del equipo. Es deliberado: la
# la Clase 11 (sesion 7 del calendario) cierra el corte con la idea de que «el equipo pudo corregir al asistente
# porque tenia sus decisiones escritas», y una evaluacion a libro abierto es la unica
# que premia eso de verdad. El equipo que no documento no encuentra qué copiar, y esa
# es la informacion que la evaluacion tiene que dar.

CORTE2 = {
    "corte": 2,
    "clase": 11,   # numero de CLASE (carpeta Kit docente/Clases): NO cambia con el calendario
    "sesion": 7,   # sesion de CALENDARIO en que se entrega (Clase 11, ver clases_material)
    "cubre": "7 a 11",   # rango de CLASES (contenido), no de sesiones de calendario
    "minutos": 20,
    "libro_abierto": True,
    "titulo": "Evaluacion del Corte 2 - Ciclo de vida, requisitos, decision, antecedentes y prototipo",
    "resumen": (
        "Diez preguntas sobre las Clases 7 a 11: ciclo de vida y costo del cambio, "
        "requisitos y criterios de aceptación, decisión entre alternativas y alcance mínimo, "
        "antecedentes y calidad de las fuentes, prototipado y niveles de fidelidad, y uso "
        "responsable de un asistente de IA. Es individual y **a libro abierto sobre los "
        "documentos de su propio equipo**: cuatro preguntas piden abrirlos y copiar de ahí."
    ),
    "por_que_asi": (
        "A libro abierto, y sobre los propios documentos, no sobre internet. Cuatro preguntas "
        "(3, 5, 7 y 10) piden datos que solo existen en el documento del equipo: el requisito "
        "con su criterio de aceptación, el alcance mínimo y lo que quedó fuera, una ficha de "
        "antecedente, y una corrección hecha al asistente. Quien documentó las responde "
        "copiando y ajustando en cuatro minutos; quien no documentó no tiene de dónde. Esa es "
        "la medición que interesa en el corte 2, y es coherente con lo que el cierre de la "
        "sesión 11 le dice al grupo: documentar no fue un trámite, fue construir el criterio."
    ),
    "cierre": "los últimos 20 minutos de la sesión 7 del calendario (Clase 11), después de las exposiciones",
    # En el corte 2 el repaso incluye QUE TENER ABIERTO, porque cuatro preguntas se
    # responden copiando del documento del equipo. Quien llegue sin el documento pierde
    # 49 de los 100 puntos, y eso hay que decirlo con anticipacion, no el mismo dia.
    "repaso": [
        {
            "sesion": 7,
            "tema": "Ciclo de vida y requisitos",
            "revise": [
                "Por qué un error de requisitos cuesta órdenes de magnitud más tarde que "
                "temprano, y en qué momento cuesta más.",
                "Cómo distinguir un requisito funcional de uno no funcional. Practique con "
                "los requisitos de su propio proyecto.",
                "Qué hace que un criterio de aceptación sea comprobable: persona, tarea y "
                "condición. «Que funcione bien» no es un criterio.",
            ],
            "abrir": "El documento de requisitos de su equipo, con los criterios de aceptación.",
        },
        {
            "sesion": 8,
            "tema": "Decisión entre alternativas y alcance mínimo",
            "revise": [
                "Para qué sirve de verdad la matriz de criterios, y por qué los pesos se "
                "fijan ANTES de mirar las alternativas.",
                "Qué hace que un alcance mínimo sea mínimo de verdad: que resuelva algo "
                "por sí solo y se pueda probar con alguien de afuera.",
                "Las trampas de la validación: probar con el propio equipo, y preguntar "
                "«¿le gusta?» en vez de pedir una tarea.",
            ],
            "abrir": "La matriz de criterios y la definición del alcance mínimo de su equipo, "
                     "con lo que quedó fuera.",
        },
        {
            "sesion": 9,
            "tema": "Antecedentes y calidad de las fuentes",
            "revise": [
                "Los criterios para filtrar una fuente: autor, año, dónde se publicó, si "
                "se puede verificar. No la posición en el buscador.",
                "Los cinco datos de una ficha de antecedente, y por qué el «qué le falta "
                "para nuestro caso» es el que se olvida y el que más pesa.",
                "Por qué «no encontramos nada» es un resultado válido si está documentado, "
                "y por qué un asistente de IA no es una fuente citable.",
            ],
            "abrir": "Las fichas de antecedentes de su equipo, con sus enlaces. Verifique HOY "
                     "que abren: si uno no abre, tráigalo declarado.",
        },
        {
            "sesion": 10,
            "tema": "Prototipado y niveles de fidelidad",
            "revise": [
                "La paradoja de la fidelidad: por qué un prototipo que se ve terminado "
                "recibe peor retroalimentación que un dibujo a lápiz.",
                "Qué se califica de un prototipo: estado vacío, estado de error, textos "
                "reales, y datos inventados por la Ley 1581 de 2012.",
            ],
            "abrir": "El prototipo de su equipo, con las pantallas que ya tenga.",
        },
        {
            "sesion": 11,
            "tema": "Uso responsable de un asistente de IA",
            "revise": [
                "Qué dato no se le puede pasar nunca a un asistente de IA, y por qué.",
                "La diferencia entre corregir por criterio y corregir la redacción. Solo "
                "lo primero cuenta.",
            ],
            "abrir": "El registro del taller de hoy: qué le pidieron al asistente y qué le "
                     "corrigieron.",
        },
    ],
    "preguntas": [
        {
            "sesion": 7,
            "tipo": "cerrada",
            "puntos": 7,
            "enunciado": (
                "## 1. Donde cuesta mas corregir un requisito mal escrito\n\n"
                "Un requisito quedó mal escrito en la fase de requisitos y nadie lo notó. "
                "¿En qué momento su corrección cuesta órdenes de magnitud más, y por qué?"
            ),
            "opciones": [
                "Después de entregado: hay que rehacer el requisito, el diseño y lo construido, "
                "con el usuario ya usándolo y con el daño que el error alcanzó a hacer.",
                "En la fase de requisitos: es cuando el documento tiene más detalle y hay más "
                "que reescribir.",
                "En el diseño: es la fase con más diagramas que actualizar.",
                "Cuesta lo mismo en cualquier fase, porque un requisito es una sola línea de "
                "texto.",
            ],
            "correctas": [0],
            "respuesta_modelo": (
                "La primera. El costo no es el de reescribir la línea: es el de rehacer todo lo "
                "que se apoyó en ella. En la definición del problema cuesta una conversación; "
                "después de entregado cuesta órdenes de magnitud más."
            ),
            "rubrica": "7 puntos si marca la primera. 0 en cualquier otra.",
            "error_comun": (
                "Marcar la cuarta. Confunde el tamaño del texto con el costo del cambio, que es "
                "exactamente lo que la tabla de la sesión 7 desmonta."
            ),
        },
        {
            "sesion": 7,
            "tipo": "cerrada_multi",
            "puntos": 8,
            "enunciado": (
                "## 2. Requisito funcional o no funcional\n\n"
                "Marque **todos** los que son requisitos **NO funcionales**."
            ),
            "opciones": [
                "«Funciona en un computador de siete años.»",
                "«Se puede usar sin crear cuenta.»",
                "«No guarda datos personales de los usuarios.»",
                "«El usuario puede consultar si un libro está disponible sin ir a la "
                "biblioteca.»",
                "«El auxiliar puede registrar un préstamo.»",
            ],
            "correctas": [0, 1, 2],
            "respuesta_modelo": (
                "No funcionales: las tres primeras. Son condiciones que la solución debe "
                "cumplir, y salen de las restricciones del árbol de la sesión 6. Las dos "
                "últimas son funcionales: describen algo que la solución hace, escrito desde "
                "el usuario."
            ),
            "rubrica": (
                "8 puntos con las tres y ninguna de más. 4 puntos con dos y ninguna de más. "
                "0 si marca una funcional."
            ),
            "error_comun": (
                "Marcar la cuarta porque incluye «sin ir a la biblioteca» y suena a condición. "
                "No lo es: describe lo que el usuario logra hacer, que es la definición de "
                "requisito funcional."
            ),
        },
        {
            "sesion": 7,
            "tipo": "abierta",
            "puntos": 13,
            "enunciado": (
                "## 3. Un requisito de su proyecto, con su criterio de aceptacion\n\n"
                "Abra el documento de su equipo. Copie **un requisito funcional** de su "
                "proyecto y escriba debajo su **criterio de aceptación**: un caso concreto con "
                "la persona, la tarea y la condición que se puede comprobar (tiempo, cantidad o "
                "resultado observable).\n\n"
                "No vale «que funcione bien» ni «que sea fácil de usar»: eso no se puede "
                "comprobar. Si el criterio que tienen escrito no se puede comprobar, corríjalo "
                "aquí y diga que lo corrigió."
            ),
            "respuesta_modelo": (
                "Ejemplo con el caso de la biblioteca:\n\n"
                "Requisito funcional: «el vecino puede consultar si un libro está disponible "
                "sin ir a la biblioteca».\n\n"
                "Criterio de aceptación: «una persona que nunca ha visto el prototipo encuentra "
                "la disponibilidad de un título que se le dicta, en menos de un minuto y sin "
                "que nadie del equipo le indique dónde buscar».\n\n"
                "Tiene los tres pedazos: la persona (alguien ajeno), la tarea (encontrar la "
                "disponibilidad de un título dictado) y la condición comprobable (menos de un "
                "minuto, sin ayuda)."
            ),
            "rubrica": (
                "13 puntos repartidos así:\n\n"
                "- **4 pts** · el requisito es funcional y está escrito desde el usuario. 2 pts "
                "si está escrito desde la tecnología («el sistema tendrá una base de datos»).\n"
                "- **6 pts** · el criterio nombra persona, tarea y condición comprobable. 2 pts "
                "por cada pieza presente.\n"
                "- **3 pts** · la condición se puede comprobar de verdad: hay un número, un "
                "conteo o un resultado observable. 0 pts a «que sea intuitivo».\n\n"
                "Si el estudiante declara que corrigió un criterio no verificable de su "
                "documento, se le dan los 3 pts completos: eso es exactamente lo que se quiere."
            ),
            "error_comun": (
                "Copiar el requisito y poner como criterio el mismo requisito en otras "
                "palabras. El criterio no repite el qué: dice cómo se comprueba."
            ),
        },
        {
            "sesion": 8,
            "tipo": "cerrada",
            "puntos": 8,
            "enunciado": (
                "## 4. Para que sirve la matriz de criterios\n\n"
                "¿Para qué sirve la matriz de criterios con la que el equipo eligió entre sus "
                "dos alternativas?"
            ),
            "opciones": [
                "Para hacer explícito el criterio con el que se decide: los pesos se fijan "
                "antes de mirar las alternativas, y la decisión queda con su argumento y con lo "
                "que se pierde.",
                "Para que el resultado del cálculo decida por el equipo, y así nadie tenga que "
                "argumentar la decisión.",
                "Para demostrar que la alternativa que el equipo prefería desde el principio "
                "era la mejor.",
                "Para comparar las dos tecnologías y quedarse con la más moderna.",
            ],
            "correctas": [0],
            "respuesta_modelo": (
                "La primera. El orden importa: los pesos se deciden antes de mirar las "
                "alternativas, porque si se deciden después se acomodan al favorito. Y la "
                "matriz no reemplaza el argumento: lo obliga."
            ),
            "rubrica": "8 puntos si marca la primera. 0 en cualquier otra.",
            "error_comun": (
                "Marcar la segunda. Es la trampa de la sesión 8: la matriz ordena el "
                "razonamiento, no lo sustituye. Quien la usa para no decidir sigue decidiendo, "
                "solo que sin decirlo."
            ),
        },
        {
            "sesion": 8,
            "tipo": "abierta",
            "puntos": 14,
            "enunciado": (
                "## 5. Que quedo fuera del alcance minimo de su proyecto\n\n"
                "Abra el documento de su equipo y responda las tres cosas:\n\n"
                "1. El **alcance mínimo** en una frase: lo más pequeño que ya resuelve algo del "
                "problema y se puede probar con un usuario real.\n"
                "2. **Dos cosas que quedaron FUERA**, y por qué cada una.\n"
                "3. **Con quién** van a probar en la Clase 12 y **qué tarea** le van a pedir. "
                "No «¿le gusta?»: una tarea.\n\n"
                "Si su alcance mínimo no resuelve nada por sí solo, no se va a poder probar. Si "
                "está así, dígalo y corríjalo aquí."
            ),
            "respuesta_modelo": (
                "1. «Una página que muestra si un libro está disponible, consultable desde el "
                "celular sin crear cuenta.» Resuelve algo por sí sola: evita el viaje a la "
                "biblioteca para averiguar.\n\n"
                "2. Fuera: (a) reservas e historial por usuario, porque exigen identificar a la "
                "persona y eso rompe el requisito de no guardar datos personales; (b) imágenes "
                "de portadas, porque rompen el límite de 200 KB por consulta que el equipo fijó "
                "en la sesión 5.\n\n"
                "3. Con una vecina que usa la biblioteca y no es del equipo. Tarea: «averigüe "
                "si el libro que le voy a dictar está disponible». Se observa en silencio "
                "dónde duda, y se cronometra."
            ),
            "rubrica": (
                "14 puntos repartidos así:\n\n"
                "- **5 pts** · el alcance mínimo resuelve algo por sí solo. 2 pts si es «la "
                "primera parte de todo lo que soñamos» y no sirve suelto.\n"
                "- **5 pts** · dos exclusiones CON su razón (2,5 cada una). Sin razón, la mitad.\n"
                "- **4 pts** · la validación: persona ajena al equipo (2 pts) y una tarea, no "
                "una opinión (2 pts). 0 pts si va a probar con un integrante del equipo, y "
                "0 pts si la pregunta es «¿le gusta?».\n\n"
                "Declarar que el alcance estaba mal y corregirlo aquí puntúa completo."
            ),
            "error_comun": (
                "Probar con un integrante del equipo. Quien construyó sabe dónde tocar, así que "
                "todo le funciona: es la trampa 1 de la sesión 8 y no prueba nada."
            ),
        },
        {
            "sesion": 9,
            "tipo": "cerrada_multi",
            "puntos": 10,
            "enunciado": (
                "## 6. Que hace utilizable una fuente\n\n"
                "Marque **todas** las afirmaciones correctas sobre fuentes y antecedentes, "
                "según la sesión 9."
            ),
            "opciones": [
                "Una cita que no se abrió no se puede usar: hay que verificar que el enlace "
                "existe y anotar la fecha de consulta.",
                "«No encontramos nada» es un resultado válido, si se escribe qué se buscó, con "
                "qué términos, en qué sitios y qué fue lo más cercano.",
                "Un asistente de IA sirve para encontrar términos y sinónimos con los que "
                "buscar mejor, pero no es una fuente y no se cita.",
                "El primer resultado del buscador es el más confiable, porque el buscador ya "
                "ordenó por calidad.",
                "Si la idea del proyecto ya existe, el proyecto pierde validez y hay que "
                "cambiar de tema.",
            ],
            "correctas": [0, 1, 2],
            "respuesta_modelo": (
                "Correctas: las tres primeras. La cuarta es falsa: se filtra por calidad "
                "—autor, año, dónde se publicó, si se puede verificar—, no por posición. La "
                "quinta es falsa y al revés: encontrar que la idea ya existe confirma que el "
                "problema es real y da de dónde partir."
            ),
            "rubrica": (
                "10 puntos con las tres y ninguna de más. 5 puntos con dos y ninguna de más. "
                "0 si marca la cuarta o la quinta."
            ),
            "error_comun": (
                "Dejar sin marcar la segunda. Cuesta creer que «no encontramos nada» puntúe, "
                "pero es un hallazgo cuando está documentado; lo que no puntúa es no haber "
                "buscado."
            ),
        },
        {
            "sesion": 9,
            "tipo": "abierta",
            "puntos": 12,
            "enunciado": (
                "## 7. Uno de sus antecedentes, y que van a hacer distinto\n\n"
                "Abra las fichas de antecedentes de su equipo. Escriba **uno** con sus cinco "
                "datos: responsable o autor, año, dónde está publicado, qué hace, y **qué le "
                "falta para su caso**.\n\n"
                "Después, en una frase: **qué van a hacer distinto** ustedes, y por qué eso "
                "importa para su problema.\n\n"
                "Si el enlace de esa ficha no abre hoy, dígalo. Vale más declararlo que "
                "sostener una cita que no se puede verificar."
            ),
            "respuesta_modelo": (
                "Ficha: «Biblioteca pública municipal de (ciudad) · 2023 · catálogo en línea "
                "publicado en el sitio de la alcaldía · permite consultar disponibilidad por "
                "título y autor · le falta para nuestro caso que exige crear una cuenta y que "
                "no funciona bien en celular, y nuestra biblioteca no tiene quien administre "
                "cuentas.»\n\n"
                "Qué haremos distinto: «consulta sin cuenta y pensada para celular, porque "
                "nuestros usuarios entran desde el teléfono y no hay nadie que administre "
                "registros.»\n\n"
                "Cualquier antecedente sirve. Lo que se califica es que los cinco datos estén y "
                "que el «qué le falta» sea específico de su caso, no genérico."
            ),
            "rubrica": (
                "12 puntos repartidos así:\n\n"
                "- **5 pts** · los cinco datos de la ficha, 1 pt cada uno.\n"
                "- **4 pts** · el «qué le falta para nuestro caso» es específico del proyecto. "
                "1 pt si es genérico («le falta ser más moderno»).\n"
                "- **3 pts** · el «qué haremos distinto» se apoya en ese faltante y en el "
                "contexto propio. 0 pts si es «lo haremos mejor».\n\n"
                "Declarar que el enlace no abre no descuenta: descuenta sostener una cita sin "
                "verificar. Si el estudiante inventa una ficha, la pregunta es 0 y hay que "
                "hablar con el equipo."
            ),
            "error_comun": (
                "Traer una ficha sin el «qué le falta». Es el único de los seis campos que "
                "obliga a comparar contra el propio problema, y es el que se olvida."
            ),
        },
        {
            "sesion": 10,
            "tipo": "cerrada",
            "puntos": 8,
            "enunciado": (
                "## 8. Que nivel de fidelidad conviene\n\n"
                "El equipo quiere saber si una persona ajena entiende el flujo y sabe qué hacer "
                "en cada pantalla. ¿Con qué nivel de fidelidad conviene probar, y por qué?"
            ),
            "opciones": [
                "Baja fidelidad: cuesta un minuto cambiarlo y, al verse como un borrador, la "
                "gente se atreve a criticar el flujo.",
                "Alta fidelidad: si se ve terminado, la persona lo toma en serio y la crítica "
                "es más útil.",
                "Funcional: solo se puede saber si el flujo sirve cuando el sistema ya corre de "
                "verdad.",
                "Media siempre: es el nivel intermedio y por eso es el más seguro en cualquier "
                "caso.",
            ],
            "correctas": [0],
            "respuesta_modelo": (
                "La primera. Es la paradoja de la fidelidad: cuanto más terminado se ve un "
                "prototipo, peor retroalimentación recibe. Delante de un dibujo a lápiz la "
                "gente dice «no entiendo dónde busco»; delante de una pantalla con colores dice "
                "«está muy bonito»."
            ),
            "rubrica": "8 puntos si marca la primera. 0 en cualquier otra.",
            "error_comun": (
                "Marcar la segunda. Es la intuición natural y es exactamente la que la sesión "
                "10 contradice con la paradoja de la fidelidad."
            ),
        },
        {
            "sesion": 10,
            "tipo": "cerrada_multi",
            "puntos": 10,
            "enunciado": (
                "## 9. Que se califica de un prototipo\n\n"
                "Marque **todas** las afirmaciones correctas sobre lo que se califica de un "
                "prototipo en este curso."
            ),
            "opciones": [
                "El estado vacío y el estado de error tienen que estar dibujados: es donde se "
                "cae casi todo prototipo.",
                "Los textos tienen que ser reales («Buscar título»), no relleno: un texto falso "
                "esconde el problema de un botón que nadie sabe qué hace.",
                "Si el prototipo lleva datos, tienen que ser inventados: ni nombres, ni "
                "cédulas, ni teléfonos, ni fotos de personas reales, ni del propio equipo.",
                "Lo que más pesa es que el prototipo se vea pulido, con colores y tipografías "
                "propias.",
                "Un prototipo que solo vio el equipo ya sirve como validación, si el equipo se "
                "puso de acuerdo.",
            ],
            "correctas": [0, 1, 2],
            "respuesta_modelo": (
                "Correctas: las tres primeras. La cuarta es falsa —pulir no es lo que se "
                "califica, y además empeora la retroalimentación—. La quinta es falsa: un "
                "prototipo que solo vio el equipo no probó nada, su única razón de existir es "
                "que alguien de afuera intente usarlo delante de ustedes."
            ),
            "rubrica": (
                "10 puntos con las tres y ninguna de más. 5 puntos con dos y ninguna de más. "
                "0 si marca la cuarta o la quinta."
            ),
            "error_comun": (
                "Dejar sin marcar la tercera. La regla de datos inventados se lee como una "
                "formalidad del curso y es la Ley 1581 de 2012 de la sesión 4."
            ),
        },
        {
            "sesion": 11,
            "tipo": "abierta",
            "puntos": 10,
            "enunciado": (
                "## 10. Una correccion que le hicieron al asistente\n\n"
                "Abra el registro del taller de hoy. Escriba **una** corrección que su equipo "
                "le hizo a lo que devolvió el asistente de IA, y para ella:\n\n"
                "1. Qué propuso el asistente.\n"
                "2. Qué pusieron ustedes en su lugar.\n"
                "3. **De qué sesión salió el criterio** con el que lo corrigieron: el requisito "
                "no funcional, el alcance, el indicador, la norma…\n\n"
                "Y al final, en una línea: **qué dato NO se le puede pasar** a un asistente de "
                "IA en este curso, y por qué."
            ),
            "respuesta_modelo": (
                "1. El asistente propuso un aviso automático por correo cuando el libro se "
                "devuelva.\n"
                "2. Lo quitamos: la consulta no pide correo y no se avisa nada.\n"
                "3. El criterio salió de la sesión 4: pedir el correo es recolectar un dato "
                "personal, y la Ley 1581 de 2012 exige autorización previa y finalidad. Además "
                "choca con el requisito no funcional de la sesión 7 de usar sin crear cuenta.\n\n"
                "Dato que no se le pasa: ningún dato personal de una persona real —nombre, "
                "cédula, teléfono, dirección, foto, datos de salud—, porque lo que se escribe "
                "en el asistente sale del computador y no vuelve, y ninguna de esas personas "
                "autorizó ese tratamiento."
            ),
            "rubrica": (
                "10 puntos repartidos así:\n\n"
                "- **3 pts** · qué propuso el asistente, concreto.\n"
                "- **3 pts** · qué pusieron en su lugar, concreto.\n"
                "- **2 pts** · la sesión de la que salió el criterio, con el criterio nombrado. "
                "1 pt si dice la sesión sin el criterio.\n"
                "- **2 pts** · el dato que no se le pasa, con su razón. 1 pt sin la razón.\n\n"
                "Si la «corrección» es de redacción o de estilo, la primera mitad vale la "
                "mitad: lo que se pedía es una corrección de criterio, no de forma."
            ),
            "error_comun": (
                "Reportar como corrección un cambio de palabras. La sesión 11 es explícita: se "
                "califica lo que corrigieron por criterio, y un equipo que entrega tal cual lo "
                "que devolvió el asistente tiene la nota más baja del corte."
            ),
        },
    ],
}


EVALUACIONES = {
    CORTE1["sesion"]: CORTE1,
    CORTE2["sesion"]: CORTE2,
}


# --------------------------------------------------------------------- validacion
# Se valida al importar y no en el builder, para que un error de datos falle donde
# esta el error y no tres archivos despues.

for _s, _e in EVALUACIONES.items():
    _total = sum(p["puntos"] for p in _e["preguntas"])
    if _total != 100:
        raise SystemExit(
            "La evaluacion del corte %d (sesion %d) suma %d puntos, no 100."
            % (_e["corte"], _s, _total)
        )
    _a, _b = (int(v) for v in _e["cubre"].split(" a "))
    for _p in _e["preguntas"]:
        if not _a <= _p["sesion"] <= _b:
            raise SystemExit(
                "La evaluacion del corte %d cubre las sesiones %s, pero una pregunta "
                "declara sesion %d." % (_e["corte"], _e["cubre"], _p["sesion"])
            )
        if _p["tipo"] in ("cerrada", "cerrada_multi"):
            if not _p.get("opciones") or not _p.get("correctas"):
                raise SystemExit(
                    "Corte %d: una pregunta %s no trae opciones o correctas."
                    % (_e["corte"], _p["tipo"])
                )
            if max(_p["correctas"]) >= len(_p["opciones"]):
                raise SystemExit(
                    "Corte %d: una pregunta apunta a una opcion que no existe."
                    % _e["corte"]
                )
            if _p["tipo"] == "cerrada" and len(_p["correctas"]) != 1:
                raise SystemExit(
                    "Corte %d: una pregunta de seleccion unica tiene %d correctas."
                    % (_e["corte"], len(_p["correctas"]))
                )
        for _k in ("rubrica", "respuesta_modelo", "error_comun"):
            if not _p.get(_k):
                raise SystemExit(
                    "Corte %d: una pregunta no trae `%s`." % (_e["corte"], _k)
                )

# Las sesiones del corte tienen que estar TODAS representadas, en las preguntas y en la
# guia de repaso. Si una queda sin pregunta, el estudiante estudio algo que no se evaluo;
# si queda sin repaso, se le evaluo algo que no se le dijo que repasara.
for _s, _e in EVALUACIONES.items():
    _a, _b = (int(v) for v in _e["cubre"].split(" a "))
    _esperadas = list(range(_a, _b + 1))
    for _campo, _vistas in (
        ("evalua", {p["sesion"] for p in _e["preguntas"]}),
        ("repasa", {r["sesion"] for r in _e["repaso"]}),
    ):
        _faltan = [x for x in _esperadas if x not in _vistas]
        if _faltan:
            raise SystemExit(
                "La evaluacion del corte %d no %s las sesiones %s."
                % (_e["corte"], _campo, ", ".join(str(x) for x in _faltan))
            )
    for _r in _e["repaso"]:
        if not _r.get("tema") or not _r.get("revise"):
            raise SystemExit(
                "Corte %d: el repaso de la sesion %d no trae tema o `revise`."
                % (_e["corte"], _r["sesion"])
            )
    # El repaso va en el orden de las sesiones: el estudiante lo lee como cronologia.
    _orden = [r["sesion"] for r in _e["repaso"]]
    if _orden != sorted(_orden):
        raise SystemExit(
            "Corte %d: el repaso no esta en orden de sesion: %r" % (_e["corte"], _orden)
        )
