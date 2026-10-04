# -*- coding: utf-8 -*-
"""BD II · Clase 15 · Presentación del proyecto y cierre: ideas proyectadas y GUION por lámina.

Formato: `notas_guion.py` (se fusiona en `bd2_contenido_data.CONTENIDO`). Las animaciones están en
`config/animaciones/bd2/clase15/`: «Al entrar» es su primer paso y cada «Clic» el siguiente.

Es la sesión de SUSTENTACIONES EN VIVO (lunes 16 de noviembre, por Meet). No hay tema nuevo: las
láminas de concepto (de «Sustentar no es describir» al «Q&A de modelado») son lo que se va a
preguntar y se recorren rápido antes del primer turno; «El cierre del curso» se da al final,
después de los turnos, aunque en el deck vaya antes de «Cómo se ordena la sesión».
"""

CONTENIDO = {
    15: {
        "Encuadre de hoy": {
            "notas": {
                "min": 2,
                "explica": "Hoy no hay tema nuevo: es la sustentación en vivo del proyecto y el "
                           "cierre del curso. Cada estudiante, o equipo, defiende sus decisiones "
                           "en 5 a 8 minutos y responde preguntas al azar.",
                "pasos": [
                    "Lee la lámina y anuncia lo práctico: el orden de los turnos se sortea en un "
                    "momento, el paquete tenía que estar subido antes del turno y la sustentación "
                    "no se reemplaza por un video.",
                    ("Antes del primer turno",
                     "Lee en voz alta el reparto de los 100 puntos del proyecto: 20 modelo y DDL, "
                     "15 seguridad y respaldo, 25 procedimientos, funciones y disparadores con "
                     "pruebas, 15 optimización, 10 integración y 15 informe y sustentación. Vale el "
                     "20 % del Corte 3; el Parcial 3 vale 15 % y la asistencia 5 %. El proyecto no "
                     "reemplaza al parcial."),
                ],
                "cuidado": "Los 15 puntos de sustentación son la sexta parte, pero la sustentación "
                           "es como se verifica que los otros 85 son de quien presenta. Dilo para "
                           "evitar el reclamo de «solo vale 15».",
                "puente": "Cómo se reparte el bloque de hoy.",
            },
        },
        "Mapa del bloque": {
            "notas": {
                "min": 1,
                "explica": "El bloque es casi todo turnos: encuadre y sorteo, sustentaciones con su "
                           "Q&A, y el cierre del curso al final.",
                "pasos": [
                    "Señala los tres tramos. Las láminas de concepto que siguen son lo que se va a "
                    "preguntar: recórrelas en unos 12 minutos, así que los turnos empiezan hacia el "
                    "minuto 15 y no en el 10.",
                ],
                "puente": "Lo primero que hay que tener claro: sustentar no es describir.",
            },
        },
        "Sustentar no es describir": {
            "ideas": [
                "Describir es decir **qué hay**: «tenemos dueño, mascota, cita, veterinario, insumo "
                "y factura».",
                "Sustentar es responder **por qué quedó así** y qué alternativa se descartó.",
                "En bases de datos importa más por el **costo de revertir**: cambiar un esquema con "
                "datos exige una migración.",
                "Por eso cada decisión del modelo tiene que poder **defenderse** con dos o tres "
                "preguntas.",
            ],
            "notas": {
                "min": 2,
                "explica": "La sustentación no es una visita guiada por el diagrama. Es explicar por "
                           "qué cada decisión quedó como quedó y qué se descartó, porque en una base "
                           "de datos deshacer una decisión cuesta caro.",
                "pasos": [
                    "A la izquierda, describir: una lista de «tenemos…». Pregunta: ¿qué aprende el "
                    "evaluador de esa lista que no vea ya en el diagrama? Nada.",
                    "A la derecha, sustentar: por qué quedó así y qué se descartó. Son las dos "
                    "preguntas que se van a hacer en cada turno.",
                    "El costo de revertir: cambiar código es la barra corta; cambiar un esquema con "
                    "datos (partir una tabla con cien mil filas y seis procedimientos apuntándole) "
                    "es la barra larga: migración, ventana de mantenimiento y riesgo de perder "
                    "datos.",
                ],
                "ejemplo": "Describir: «hay una tabla cita con una FK». Sustentar: «la FK va en cita "
                           "y no en mascota porque una mascota tiene muchas citas; sin ella podría "
                           "existir una cita de una mascota que no existe».",
                "preguntas": [
                    ("¿Entonces no muestro el diagrama?",
                     "Sí, pero como apoyo de dos decisiones justificadas, no para nombrar las tablas "
                     "una por una."),
                ],
                "cuidado": "No califiques bien un recorrido de seis minutos por el ER porque "
                           "«explicaron todo»: si nadie dio un porqué, no hubo sustentación.",
                "puente": "Las preguntas de porqué que casi siempre llegan son cuatro.",
            },
        },
        "Las cuatro preguntas de por que": {
            "ideas": [
                "**Normalización:** tercera forma normal, y la desnormalización deliberada "
                "declarada con su razón.",
                "**Índice:** la consulta que lo aprovecha y la medición de antes y después.",
                "**Tipo de dato:** fecha en TIMESTAMP, teléfono en VARCHAR (no se suma y conserva "
                "el cero inicial).",
                "**Disparador:** por qué la regla vive ahí y no en la aplicación.",
            ],
            "notas": {
                "min": 3,
                "explica": "Casi toda sustentación de bases de datos termina en las mismas cuatro "
                           "preguntas. Quien las trae respondidas sustenta; quien no, improvisa.",
                "pasos": [
                    "Normalización: «está en tercera forma normal», es decir, cada atributo depende "
                    "de la clave completa y de nada más (el teléfono del dueño vive en dueno, no "
                    "repetido en cada mascota). Y si existe, la desnormalización deliberada: "
                    "guardar el total en factura porque es un valor histórico.",
                    "Índice: nombrar la consulta que lo usa (la agenda filtra por veterinario y "
                    "ordena por hora, de ahí un índice sobre (id_veterinario, fecha_hora)) y "
                    "mostrar EXPLAIN ANALYZE antes y después.",
                    "Tipo de dato: la fecha es TIMESTAMP porque se compara y se ordena; el teléfono "
                    "es VARCHAR porque no se hace aritmética con él y un tipo numérico pierde el "
                    "cero inicial.",
                    "La cuarta, la del disparador, es la que más se falla: tiene lámina propia.",
                ],
                "ejemplo": "«Guardamos el total en factura aunque se pueda sumar del detalle, porque "
                           "es un valor histórico: si mañana sube el precio del insumo, la factura "
                           "de ayer no debe cambiar.»",
                "preguntas": [
                    ("¿Desnormalizar es un error?",
                     "No, si es deliberado y está escrito con su razón. El error es desnormalizar "
                     "sin saberlo."),
                ],
                "cuidado": "«Está normalizado», sin decir qué forma normal ni dar un ejemplo, no "
                           "responde la pregunta.",
                "puente": "La cuarta pregunta, la que más se falla.",
            },
        },
        "La cuarta pregunta": {
            "ideas": [
                "Un **disparador** (trigger) lo ejecuta el motor solo, cuando ocurre un evento "
                "sobre una tabla.",
                "Su argumento es la **cobertura**: se cumple escriba la aplicación, un script de "
                "carga o alguien a mano.",
                "Si la regla vive en la aplicación, el script y el cliente SQL la evaden sin "
                "esfuerzo.",
                "El contra-argumento: es **lógica invisible**, así que se reserva para integridad "
                "y auditoría.",
            ],
            "notas": {
                "min": 2,
                "explica": "La pregunta es por qué una regla vive en un disparador y no en la "
                           "aplicación. La respuesta que vale es una sola, la cobertura, y hay que "
                           "saber también el contra-argumento.",
                "pasos": [
                    "Regla en la aplicación: escriben en insumo la aplicación, un script de carga y "
                    "alguien con un cliente SQL. Solo el primero pasa por la regla; los otros dos "
                    "llegan a la tabla con la X roja.",
                    "Regla en el disparador: la barra del trigger está pegada a la tabla y los tres "
                    "caminos pasan por ella.",
                    "A favor: cobertura. En contra: lógica invisible (no aparece en el código de la "
                    "aplicación, sorprende al que depura y puede dispararse en cascada). Criterio: "
                    "disparadores para integridad y auditoría; el flujo de negocio, en "
                    "procedimientos que se llaman a propósito.",
                ],
                "ejemplo": "La auditoría de precios: si alguien cambia a mano el precio de una "
                           "vacuna desde un cliente SQL, solo un disparador deja constancia de "
                           "quién y cuándo.",
                "preguntas": [
                    ("¿Un CHECK no hace lo mismo?",
                     "Para una regla que mira una sola fila, sí, y es preferible (Clase 4). El "
                     "disparador se justifica cuando mira otra fila u otra tabla, o escribe en "
                     "otra tabla, como la auditoría."),
                ],
                "cuidado": "Si el estudiante solo da el argumento a favor, pide el "
                           "contra-argumento: es la mitad de la respuesta.",
                "puente": "Además de defenderse, el proyecto tiene que poder correrlo otra persona.",
            },
        },
        "Reproducible": {
            "ideas": [
                "Es **reproducible** si un tercero, solo con el archivo y sin hablar con el autor, "
                "llega a la misma base.",
                "Los archivos van **numerados** en el orden de ejecución, del 00_LEEME.txt al "
                "08_pruebas.sql.",
                "El orden es **dependencia**: la FK necesita su tabla y el trigger no se crea sin "
                "ella.",
                "El LEEME declara **motor y versión**, el orden, una consulta de verificación y los "
                "límites.",
            ],
            "notas": {
                "min": 2,
                "explica": "Reproducible quiere decir que otra persona ejecuta tus archivos en una "
                           "base vacía y obtiene lo mismo que tú, sin preguntarte nada. Es la prueba "
                           "que el evaluador aplica literalmente.",
                "pasos": [
                    "La carpeta con nueve archivos numerados: 00_LEEME, 01_ddl, 02_datos_prueba, "
                    "03_roles, 04_procedimientos, 05_funciones, 06_triggers, 07_optimizacion y "
                    "08_pruebas.",
                    "Por qué el orden importa: una FOREIGN KEY no se crea antes que la tabla a la "
                    "que apunta, y un trigger no se puede crear si su tabla todavía no existe.",
                    "La definición, en la caja final. Repasa los cuatro detalles que la rompen: no "
                    "declarar motor y versión, suponer un estado previo, no ser idempotente (los "
                    "DROP … IF EXISTS van primero, en orden inverso) y un LEEME que no sirve.",
                ],
                "ejemplo": "Un LEEME que sirve: «Motor: PostgreSQL 16.4 (lo dice SELECT version()). "
                           "Ejecutar 01 a 08 en orden. Verificación: SELECT COUNT(*) FROM cita; "
                           "devuelve 10. Límite: los datos de prueba no traen facturas anuladas.»",
                "preguntas": [
                    ("¿Cuántos datos de prueba hacen falta?",
                     "Con dos filas por tabla no se demuestra nada. Un mínimo razonable: 3 dueños, 5 "
                     "mascotas, 2 veterinarios, 10 citas, 5 insumos y 3 facturas, incluidos los "
                     "casos borde: una mascota inactiva y un insumo con stock 1."),
                    ("¿Qué es idempotente?",
                     "Que se puede correr dos veces seguidas sin fallar: por eso los DROP TABLE IF "
                     "EXISTS van primero, en orden inverso al de creación."),
                ],
                "cuidado": "Evalúalo ejecutando en una base limpia: un script que se ve bien puede "
                           "fallar en la tercera sentencia por una FK que apunta a una tabla creada "
                           "más abajo.",
                "puente": "Con el paquete listo: ¿cómo caben las decisiones en 5 a 8 minutos?",
            },
        },
        "El reparto de los 5 a 8": {
            "ideas": [
                "El límite de **5 a 8 minutos** obliga a decidir qué se deja fuera.",
                "Primero se cuenta: el **problema** en lenguaje de negocio (45 s) y el **modelo** "
                "con dos decisiones (90 s).",
                "Luego se demuestra **ejecutando**: seguridad, automatización con caso válido e "
                "inválido, y optimización.",
                "Cierra la integración con su **punto débil** declarado y 30 s finales: unos 7 "
                "minutos.",
            ],
            "notas": {
                "min": 1,
                "explica": "Siete minutos no alcanzan para todo, así que el reparto es una decisión. "
                           "Este es el que funciona; es una convención, no una regla dura.",
                "pasos": [
                    "Lo que se cuenta: 45 s para el problema de la clínica en lenguaje de negocio, "
                    "sin tablas en pantalla, y 90 s para el modelo: el ER y dos decisiones "
                    "justificadas, no quince.",
                    "Lo que se demuestra ejecutando: 60 s de seguridad (la matriz de roles y por qué "
                    "recepción no ve el historial clínico), 90 s de automatización (un "
                    "procedimiento con su caso válido y su caso inválido, en vivo) y 60 s de "
                    "optimización (el plan antes y después).",
                    "El cierre: 45 s de integración con su punto débil declarado y 30 s finales. En "
                    "total, unos 7 minutos de un máximo de 8.",
                ],
                "ejemplo": "Los 45 segundos del problema: «la clínica atiende unas 150 citas al día "
                           "con agenda de papel; perder una cita o dar dos en la misma franja le "
                           "cuesta clientes».",
                "preguntas": [
                    ("¿Puedo mostrar capturas en vez de ejecutar?",
                     "No para la automatización: el caso válido y el inválido se ejecutan en vivo. "
                     "Una consulta corriendo delante del evaluador es la evidencia más difícil de "
                     "fingir."),
                    ("Si trabajamos en equipo, ¿cada uno presenta su parte?",
                     "Cada integrante debe poder explicar cualquier parte en 60 segundos, porque "
                     "el Q&A se dirige al azar."),
                ],
                "cuidado": "Cronometra cada turno: el que pasa de 8 minutos le quita tiempo al Q&A, "
                           "que es donde se verifica la autoría.",
                "puente": "Después del pitch, las preguntas: las de modelado se repiten.",
            },
        },
        "El Q&A de modelado": {
            "ideas": [
                "Una buena respuesta tiene tres partes: la **decisión**, la alternativa descartada "
                "y la razón.",
                "¿Dos mascotas llamadas Pelusa? Nada: la identidad la da **id_mascota**, no el "
                "nombre.",
                "¿Por qué no borrar las citas canceladas? Son historia del negocio: se usa **borrado "
                "lógico**.",
                "«No lo medimos» vale si se dice **cómo se mediría**; inventar un número, no.",
            ],
            "notas": {
                "min": 2,
                "explica": "El Q&A de modelado tiene preguntas que se repiten, y todas son de "
                           "porqué, no de qué. Tener las respuestas listas sirve para formularlas "
                           "bien y para calificar igual a todos.",
                "pasos": [
                    "Dos mascotas del mismo dueño con el mismo nombre: la tabla las acepta porque "
                    "cada una tiene su id_mascota. No pasa nada.",
                    "Si se quisiera prohibirlo: UNIQUE (id_dueno, nombre), y la segunda Pelusa se "
                    "rechaza.",
                    "Es una decisión que se defiende en cualquiera de los dos sentidos; lo que no "
                    "vale es no haberla pensado. Repasa las otras: nombre y apellido separados "
                    "(para ordenar y buscar por apellido) y citas canceladas (borrado lógico con un "
                    "campo de estado).",
                ],
                "ejemplo": "«¿Cuánto mejoró esa consulta?» Respuesta válida: «No lo medimos con "
                           "volumen real porque la base de práctica se reinicia, pero el plan pasa "
                           "de Seq Scan a Index Scan; la prueba sería cargar cincuenta mil citas y "
                           "comparar los tiempos».",
                "preguntas": [
                    ("¿Por qué nombre y apellido separados?",
                     "Para ordenar y buscar por apellido; separar después un campo unido falla con "
                     "los nombres compuestos."),
                    ("¿Por qué no borrar las citas canceladas?",
                     "Son información de negocio (quién cancela siempre) y una cita con consulta y "
                     "factura no se puede borrar sin dejar filas huérfanas: la FK lo impide."),
                ],
                "cuidado": "Anuncia la regla antes del primer turno: «no lo medimos» no penaliza si "
                           "viene con cómo se mediría. Inventar un número se cae en la siguiente "
                           "pregunta.",
                "puente": "Ahora, cómo se ordena la sesión; el cierre del curso viene al final de "
                          "los turnos.",
            },
        },
        "El cierre del curso": {
            "ideas": [
                "Lo que hiciste (ER, DDL, roles, procedimientos, triggers, planes) es el **trabajo de "
                "un primer empleo**.",
                "Leer un plan de ejecución y decidir si un índice sobra es una **habilidad que se "
                "paga**.",
                "En producción cambian el **volumen** y el costo de un error; la sintaxis es la "
                "misma.",
                "Autoevaluación: ¿qué decisión de modelado te costó más revertir, y **en qué "
                "clase** lo notaste?",
            ],
            "notas": {
                "min": 5,
                "explica": "El cierre conecta el semestre con el trabajo: lo que se produjo es lo que "
                           "hace un desarrollador de bases de datos o un administrador junior en su "
                           "primer año. Se termina con una autoevaluación concreta, no con una "
                           "reflexión vaga.",
                "pasos": [
                    "Dala al final, después del último turno (minuto 110). Recorre la columna de la "
                    "izquierda, los siete productos del semestre, y la flecha a «tareas del primer "
                    "año». Subraya la caja azul: leer un plan y decidir si un índice sobra.",
                    ("Banda del medio",
                     "Las herramientas: PostgreSQL en el navegador, Excalidraw o draw.io y Mermaid "
                     "se usaron por equidad, porque funcionan en cualquier navegador. El SQL es el "
                     "mismo de un servidor PostgreSQL de producción."),
                    ("Banda amarilla",
                     "Lanza la autoevaluación y pide la respuesta escrita en el chat. Lee dos o tres "
                     "en voz alta."),
                ],
                "ejemplo": "Una respuesta útil: «separar nombre y apellido; lo noté en la Clase 6, "
                           "cuando la búsqueda por apellido sobre un nombre completo no podía usar "
                           "un índice».",
                "preguntas": [
                    ("¿Vale la pena guardar los scripts?",
                     "Sí: son portafolio. El paquete (ER, DDL, roles, procedimientos, triggers y "
                     "optimización) se muestra en una entrevista técnica mejor que un certificado."),
                ],
                "cuidado": "No cierres con «¿qué aprendieron?»: da respuestas genéricas. La consigna "
                           "concreta da material real para ajustar el curso el próximo semestre.",
                "puente": "La lámina de cierre.",
            },
        },
        "Como se ordena la sesion": {
            "notas": {
                "min": 3,
                "explica": "Las reglas de los turnos, dichas una vez para todos. Después de esta "
                           "lámina empiezan las sustentaciones, que ocupan el resto del bloque hasta "
                           "el minuto 110.",
                "pasos": [
                    "Lee las cinco reglas y sortea el orden en voz alta; pega la lista en el chat de "
                    "Meet para que cada quien sepa cuándo le toca.",
                    ("En cada turno",
                     "El estudiante comparte su pantalla. Cronometra 5 a 8 minutos de pitch con la "
                     "ejecución real de un procedimiento (caso válido y caso rechazado) y haz dos o "
                     "tres preguntas de porqué, al azar, a cualquier integrante."),
                    ("Entre turnos",
                     "Anota la calificación en 30 segundos, antes de llamar al siguiente: al final "
                     "del bloque ya no se recuerda quién dijo qué."),
                    ("Si alguien se desconecta",
                     "Pasa al siguiente turno y vuelve a llamarlo al final de la lista. Si no "
                     "logra reconectarse, deja constancia de la hora y acuerda por correo cómo se "
                     "completa la sustentación."),
                ],
                "ejemplo": "Con turnos de unos 11 minutos (7 de pitch y 3-4 de Q&A) caben unos 8 en "
                           "el bloque; si el grupo es más grande, reduce el Q&A a dos preguntas y "
                           "anúncialo al sortear.",
                "cuidado": "Haz las preguntas a quien no está hablando: si siempre responde el mismo "
                           "integrante, no se verifica que el trabajo sea de todos.",
                "puente": "Al terminar el último turno, vuelve a «El cierre del curso».",
            },
        },
        "Clase 15 ·": {
            "notas": {
                "min": 3,
                "explica": "Cierre del proyecto y del curso: sustentar es justificar decisiones, y "
                           "el paquete que cada uno entregó es su portafolio.",
                "pasos": [
                    "Agradece al grupo, explica por qué canal y cuándo se publicarán las notas del "
                    "proyecto, y pide que conserven el paquete (ER, DDL, roles, procedimientos, "
                    "triggers y optimización).",
                ],
            },
        },
    },
}
