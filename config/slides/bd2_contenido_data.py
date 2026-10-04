# -*- coding: utf-8 -*-
"""BD II · Contenido de cada lámina: ideas claras proyectadas y GUION en las notas.

`CONTENIDO[n][comienzo_del_titulo_visible] = {"ideas": [...], "notas": {...}}`
(formato y uso: `notas_guion.py`). Las ideas reemplazan las viñetas recortadas del fundamento
por frases que se entienden solas; las notas son todo lo necesario para dar ESA lámina:
qué es, qué decir al entrar y en cada clic de la animación, el ejemplo, las preguntas que
salen y la respuesta, el error típico y la frase que lleva a la siguiente.

Los pasos de cada animación están en `config/animaciones/bd2/claseN/<huella>.js` (`pasos`):
«Al entrar» es el primer fotograma, «Clic k» cada uno de los siguientes.
"""

CONTENIDO = {
    4: {
        "Encuadre de hoy": {
            "notas": {
                "min": 4,
                "explica": "Hoy la base deja de ser solo un lugar donde se guardan datos y empieza "
                           "a defenderse sola: funciones que calculan, triggers que reaccionan sin "
                           "que nadie los llame, y un plan para el día en que algo salga mal.",
                "pasos": [
                    "Lee el tema en voz alta y haz la pregunta de arranque: «si mañana alguien "
                    "conecta un programa nuevo a la base y se salta la aplicación, ¿qué reglas "
                    "siguen protegiendo los datos?». Deja que respondan 1-2 personas.",
                    "Cierra: «al final de hoy van a poder responder eso con nombres concretos: "
                    "CHECK, trigger, función, y qué hacer si de todos modos se pierde algo».",
                ],
                "puente": "Empezamos por la diferencia que más confunde: función y procedimiento.",
            },
        },
        "Mapa del bloque": {
            "notas": {
                "min": 1,
                "explica": "El recorrido de las dos horas: teoría con una lámina por concepto, "
                           "demo sobre la base de la clínica y práctica opcional.",
                "pasos": ["Señala solo los tramos; no te detengas. La práctica está en la carpeta "
                          "de la clase y es opcional."],
            },
        },
        "Funcion y procedimiento": {
            "ideas": [
                "Una **función** se usa para **obtener un valor**: va dentro de un SELECT, "
                "como cualquier columna.",
                "Un **procedimiento** se usa para **hacer algo**: se llama con CALL y cambia "
                "los datos.",
                "Se escriben casi igual; la función añade **RETURNS** y al menos un **RETURN**.",
                "La pregunta para elegir: ¿necesito un valor o necesito un cambio?",
            ],
            "notas": {
                "min": 4,
                "explica": "Función y procedimiento se parecen mucho al escribirlos, así que no "
                           "se distinguen por la sintaxis sino por para qué se usan. La función "
                           "devuelve un valor y vive dentro de una consulta; el procedimiento "
                           "ejecuta acciones (insertar, validar, actualizar) y se invoca con CALL.",
                "pasos": [
                    "Columna izquierda completa: «el SELECT llama a fn_precio_consulta, la "
                    "función calcula 40000 y ese valor vuelve a la consulta como una columna más "
                    "del resultado». Subraya que la función no cambió ningún dato.",
                    "Columna derecha: «el CALL ejecuta sp_agendar_cita, que valida y escribe: "
                    "aparece una fila nueva en cita». Aquí el resultado no es un valor, es un "
                    "cambio en la tabla.",
                    "Lee la conclusión y pregunta: «¿calcular el precio de una consulta es "
                    "función o procedimiento? ¿Y registrar una cita?».",
                ],
                "ejemplo": "SELECT nombre, fn_precio_consulta(especie, FALSE) AS tarifa FROM "
                           "mascota; devuelve una tarifa por cada mascota, como si fuera una "
                           "columna calculada.",
                "preguntas": [
                    ("¿Una función puede hacer INSERT?",
                     "En PostgreSQL técnicamente sí, pero no conviene: dentro de un SELECT el "
                     "motor decide cuántas veces la ejecuta. Si hay que modificar datos, es un "
                     "procedimiento."),
                    ("¿Puedo hacer SELECT de un procedimiento?",
                     "No: el motor responde que es un procedimiento y que se llama con CALL."),
                ],
                "cuidado": "No digas «la función es la que devuelve algo y el procedimiento no "
                           "devuelve nada» como regla absoluta: el criterio es el uso (valor "
                           "dentro de una consulta vs. acción).",
                "puente": "Veamos una función real de la clínica y la palabra que más se olvida: "
                          "IMMUTABLE.",
            },
        },
        "La funcion de tarifas, y por que": {
            "notas": {
                "min": 3,
                "explica": "Una función completa que calcula un recargo de fin de semana. Sirve "
                           "para ver el molde entero y entender IMMUTABLE.",
                "pasos": [
                    "Recorre de arriba abajo: nombre y parámetros (línea 1), RETURNS DECIMAL "
                    "(qué tipo devuelve), LANGUAGE plpgsql, IMMUTABLE, y el cuerpo entre $$.",
                    "En el cuerpo: si el día es sábado o domingo (DOW 6 o 0) devuelve la base "
                    "por 1,25; si no, la base. Cada camino termina en un RETURN.",
                    "Lee el comentario final: IMMUTABLE significa «mismos argumentos, mismo "
                    "resultado, siempre», y por eso el motor puede guardar el resultado o usar "
                    "la función en un índice.",
                ],
                "ejemplo": "fn_recargo_festivo(100000, DATE '2026-10-04') — 4 de octubre de 2026 "
                           "es domingo — devuelve 125000.00.",
                "preguntas": [
                    ("¿Por qué no puede ser IMMUTABLE si usa NOW()?",
                     "Porque con los mismos argumentos el resultado cambia según el momento. "
                     "Una función que lee la hora o una tabla es STABLE o VOLATILE."),
                    ("¿Qué pasa si declaro IMMUTABLE algo que no lo es?",
                     "El motor confía en la promesa y puede devolver resultados viejos o "
                     "incorrectos, sobre todo si la función se usa en un índice."),
                ],
                "cuidado": "No confundir con Oracle: aquí es RETURNS (no RETURN ... IS) y el "
                           "cuerpo va entre $$.",
                "puente": "Ahora la función de tarifas de la clínica y sus tres detalles finos.",
            },
        },
        "Los tres detalles de fn_precio_consulta": {
            "ideas": [
                "**UPPER()** iguala cómo llega escrita la especie: «Canino», «canino» y "
                "«CANINO» cobran lo mismo.",
                "El **CASE** es la tabla de tarifas; su **ELSE** da precio a cualquier especie "
                "no prevista.",
                "**COALESCE(urgencia, FALSE)** convierte un NULL en un «no»: el recargo nunca "
                "deja la factura vacía.",
            ],
            "notas": {
                "min": 4,
                "explica": "La función de tarifas tiene tres decisiones pequeñas que evitan "
                           "errores reales: comparar el texto sin importar mayúsculas, no dejar "
                           "ninguna especie sin precio y no dejar que un NULL contamine la cuenta.",
                "pasos": [
                    "UPPER: tres formas de escribir la especie llegan a UPPER() y salen iguales. "
                    "Pregunta: «sin UPPER, ¿cuánto cobraría 'canino' en minúscula?» (respuesta: "
                    "35000, porque caería en el ELSE).",
                    "CASE: la especie normalizada elige su fila: CANINO 45000, FELINO 40000, "
                    "cualquier otra 35000. Subraya que el ELSE es una decisión de negocio.",
                    "COALESCE: si la casilla de urgencia llega vacía (NULL), COALESCE la vuelve "
                    "FALSE y no hay recargo. Sin él, base * NULL da NULL y la factura sale vacía.",
                    "Conclusión: la función nunca devuelve NULL; toda entrada tiene tarifa.",
                ],
                "ejemplo": "fn_precio_consulta('canino', NULL) → 45000. "
                           "fn_precio_consulta('FELINO', TRUE) → 54000 (40000 × 1,35).",
                "preguntas": [
                    ("¿Un IF con NULL no se trata ya como falso?",
                     "Sí, el IF no entra; el problema aparece cuando el NULL entra en una "
                     "cuenta: ahí todo el resultado se vuelve NULL."),
                ],
                "cuidado": "El recargo de urgencia es 1,35 (35 %); revisa que el número que digas "
                           "coincida con el de la lámina siguiente.",
                "puente": "Juntemos todo en la firma completa de la función.",
            },
        },
        "La funcion de tarifas: RETURNS NUMERIC": {
            "ideas": [
                "**La firma decide todo:** nombre, parámetros, RETURNS NUMERIC e IMMUTABLE.",
                "Es **RETURNS NUMERIC**, no RETURNS TRIGGER: no se asocia a una tabla, se llama "
                "desde una consulta.",
                "**IMMUTABLE** solo si no lee tablas: el filtro «mascota activa» va en la "
                "consulta, no en la función.",
            ],
            "notas": {
                "min": 3,
                "explica": "Esta lámina reúne la función completa y los tres errores que más "
                           "aparecen al escribirla: copiar RETURNS TRIGGER del trigger, olvidar "
                           "UPPER() y declarar IMMUTABLE una función que consulta tablas.",
                "pasos": [
                    "Recorre la ilustración de arriba abajo: CREATE FUNCTION + nombre, "
                    "parámetros con su tipo, RETURNS NUMERIC y la volatilidad IMMUTABLE. Abajo, "
                    "por qué RETURNS TRIGGER está tachado y qué promete IMMUTABLE.",
                ],
                "ejemplo": "SELECT nombre, especie, fn_precio_consulta(especie, FALSE) AS "
                           "normal, fn_precio_consulta(especie, TRUE) AS urgencia FROM mascota;",
                "preguntas": [
                    ("¿Dónde filtro las mascotas inactivas?",
                     "En el WHERE de la consulta que llama a la función. Si la función leyera "
                     "la tabla mascota dejaría de ser IMMUTABLE (sería STABLE)."),
                ],
                "cuidado": "RETURNS TRIGGER solo existe para la función que ejecuta un trigger; "
                           "si aparece aquí, la función no se puede usar en un SELECT.",
                "puente": "Pasamos al objeto que nadie invoca: el trigger.",
            },
        },
        "El trigger: el unico que nadie invoca": {
            "ideas": [
                "Un **trigger** se ejecuta **solo**, cuando ocurre un INSERT, UPDATE o DELETE "
                "sobre una tabla.",
                "En PostgreSQL son **dos objetos**: la **función** (RETURNS TRIGGER) y la "
                "**asociación** (CREATE TRIGGER).",
                "La asociación dice **cuándo** se dispara y **qué función** llama.",
            ],
            "notas": {
                "min": 4,
                "explica": "Todo lo anterior se ejecuta porque alguien lo llama. El trigger no: se "
                           "declara una vez y el motor lo ejecuta cada vez que ocurre el evento. "
                           "En PostgreSQL se escribe en dos piezas separadas.",
                "pasos": [
                    "Las dos piezas: arriba la función fn_trg_audit_cita() RETURNS TRIGGER y la "
                    "asociación CREATE TRIGGER … AFTER UPDATE OF estado ON cita, que apunta a la "
                    "función. Abajo, la tabla cita y la tabla audit_cita, todavía vacía.",
                    "Llega un UPDATE que cambia el estado de la cita 7 de 'confirmada' a "
                    "'atendida'. Nadie ha llamado al trigger.",
                    "El cambio es el evento: el motor dispara la asociación, que ejecuta la "
                    "función, y aparece la fila en audit_cita con el antes y el después.",
                    "Lee la frase: «nadie lo llama: lo dispara el evento». Ese es todo el "
                    "concepto.",
                ],
                "ejemplo": "Cada vez que recepción cambia el estado de una cita, queda registrado "
                           "quién y cuándo, sin que la aplicación tenga que acordarse.",
                "preguntas": [
                    ("Creé la función y no pasa nada.",
                     "Falta la segunda pieza, el CREATE TRIGGER. Sin asociación la función "
                     "nunca se ejecuta."),
                ],
                "cuidado": "No dictes la forma de Oracle (cuerpo dentro del CREATE TRIGGER y "
                           ":NEW con dos puntos): en PostgreSQL no compila.",
                "puente": "¿En qué momento corre el trigger, antes o después de escribir la fila? "
                          "Eso cambia lo que puede hacer.",
            },
        },
        "BEFORE o AFTER, y que significa": {
            "ideas": [
                "**BEFORE** corre antes de escribir la fila: puede **cambiarla** o **impedirla**.",
                "**AFTER** corre con la fila ya escrita: solo **registra**; su valor de retorno "
                "se ignora.",
                "Para rechazar se usa **RAISE EXCEPTION**: un RETURN NULL cancela en silencio.",
            ],
            "notas": {
                "min": 4,
                "explica": "La diferencia entre BEFORE y AFTER es el momento, y el momento decide "
                           "qué se puede hacer. En BEFORE lo que la función retorna es lo que se "
                           "guarda; en AFTER la fila ya está guardada.",
                "pasos": [
                    "La fila NEW viaja por la vía y llega a BEFORE, todavía sin escribir.",
                    "Lo que BEFORE puede retornar: NEW (se guarda tal cual), NEW cambiado (se "
                    "guarda la versión cambiada) o NULL (la operación se cancela sin aviso).",
                    "La fila se escribe y llega a AFTER: ya está en la tabla, así que el retorno "
                    "se ignora (se escribe RETURN NEW por convención).",
                    "La regla práctica: para rechazar, RAISE EXCEPTION, nunca RETURN NULL.",
                ],
                "ejemplo": "BEFORE: poner el estado en mayúsculas o rechazar un stock negativo. "
                           "AFTER: escribir la fila de auditoría.",
                "preguntas": [
                    ("¿Por qué no usar RETURN NULL para rechazar?",
                     "Porque no da error: la aplicación cree que guardó y el dato nunca llegó. "
                     "RAISE EXCEPTION aborta y avisa con un mensaje."),
                ],
                "cuidado": "Poner AFTER en el trigger que debe impedir algo es el error más "
                           "común: cuando corre, el dato ya está escrito.",
                "puente": "Veamos el trigger BEFORE que impide un stock negativo, en código.",
            },
        },
        "BEFORE o AFTER: uno puede impedir": {
            "notas": {
                "min": 3,
                "explica": "Un trigger BEFORE completo que impide que el stock de un insumo quede "
                           "negativo. Son las dos piezas: la función y la asociación.",
                "pasos": [
                    "La función: si NEW.stock < 0, RAISE EXCEPTION con el id y el valor; si no, "
                    "RETURN NEW para que la fila se guarde.",
                    "La asociación: BEFORE UPDATE OF stock ON insumo, FOR EACH ROW, EXECUTE "
                    "FUNCTION. Solo se dispara cuando cambia la columna stock.",
                    "Lee el comentario: en BEFORE, devolver NULL cancelaría sin aviso; por eso se "
                    "usa RAISE EXCEPTION.",
                ],
                "ejemplo": "Con 3 unidades, UPDATE insumo SET stock = stock - 10 WHERE "
                           "id_insumo = 2 → ERROR: Stock negativo en el insumo 2 (-7). El stock "
                           "sigue en 3.",
                "preguntas": [
                    ("¿El error deshace solo esa fila?",
                     "Deshace toda la sentencia (y la transacción en curso, si no se maneja): "
                     "nada del UPDATE queda escrito."),
                ],
                "puente": "El uso donde los triggers brillan de verdad: la auditoría.",
            },
        },
        "La auditoria: donde el trigger brilla": {
            "ideas": [
                "La auditoría es ideal para un trigger: **no se puede olvidar** llamarla.",
                "**AFTER UPDATE OF estado** solo audita cambios de esa columna.",
                "**WHEN (OLD.estado IS DISTINCT FROM NEW.estado)** descarta los UPDATE que no "
                "cambian nada.",
                "Por eso **3 UPDATE dejan 2 filas** de auditoría.",
            ],
            "notas": {
                "min": 4,
                "explica": "Un trigger de auditoría guarda el antes y el después de cada cambio. "
                           "Es el mejor uso de un trigger porque nadie puede saltárselo. La "
                           "cláusula WHEN decide qué cambios valen la pena registrar.",
                "pasos": [
                    "UPDATE 1: pendiente → confirmada. Cambió el estado, el WHEN lo deja pasar y "
                    "aparece la primera fila en audit_cita.",
                    "UPDATE 2: confirmada → atendida. Otra vez cambió: segunda fila.",
                    "UPDATE 3: atendida → atendida. No cambió nada: el WHEN lo detiene y no se "
                    "escribe nada.",
                    "Resultado: tres UPDATE, dos filas. Sin el WHEN serían tres, y la auditoría "
                    "se llenaría de ruido.",
                ],
                "preguntas": [
                    ("¿Por qué IS DISTINCT FROM y no <>?",
                     "Porque si uno de los dos es NULL, <> devuelve NULL y el cambio no se "
                     "registra. IS DISTINCT FROM trata NULL como un valor comparable."),
                ],
                "cuidado": "En la demo ejecuta los tres UPDATE y muestra la tabla audit_cita; si "
                           "no se ve el resultado, el grupo concluye que el trigger no hizo nada.",
                "puente": "El código completo de este trigger.",
            },
        },
        "La auditoria de cita: funcion, trigger y WHEN": {
            "notas": {
                "min": 3,
                "explica": "El trigger de auditoría completo, con sus dos piezas rotuladas.",
                "pasos": [
                    "Pieza 1, la función: inserta en audit_cita el id, la acción y el estado "
                    "anterior y nuevo. Usuario y fecha los pone la tabla por DEFAULT. Termina "
                    "en RETURN NEW.",
                    "Pieza 2, la asociación: AFTER UPDATE OF estado ON cita, FOR EACH ROW, con el "
                    "WHEN que descarta los no-cambios, y EXECUTE FUNCTION.",
                    "Señala que NEW y OLD van sin dos puntos (en Oracle llevan dos puntos).",
                ],
                "ejemplo": "Después de los tres UPDATE: SELECT accion, valor_anterior, "
                           "valor_nuevo FROM audit_cita; → 2 filas.",
                "cuidado": "El trigger es invisible para quien solo lee el código de la "
                           "aplicación: documéntalo junto al esquema.",
                "puente": "Ahora el trigger que no registra sino que impide.",
            },
        },
        "El trigger que impide": {
            "ideas": [
                "Sin defensa, la base acepta un imposible: stock **−7**.",
                "Un trigger **BEFORE** con **RAISE EXCEPTION** rechaza el cambio y el stock "
                "sigue en 3.",
                "Si la regla mira solo la propia fila, basta un **CHECK**: es más barato.",
                "El trigger es para lo que mira **otra fila u otra tabla**.",
            ],
            "notas": {
                "min": 4,
                "explica": "La demo retira a propósito el CHECK (stock >= 0) para mostrar qué "
                           "pasa sin defensa, y luego la defensa con un trigger. La lección no es "
                           "«trigger mejor que CHECK»: es saber cuándo cada uno.",
                "pasos": [
                    "Sin defensa: el UPDATE resta 10 a un insumo con 3 unidades y la base guarda "
                    "−7. Pregunta: «¿qué significa tener −7 vacunas?».",
                    "Con el trigger BEFORE: el mismo UPDATE choca con RAISE EXCEPTION, se "
                    "rechaza y el stock sigue en 3.",
                    "La regla: si cabe en un CHECK, va en un CHECK; el trigger es para lo que "
                    "necesita mirar otra fila u otra tabla.",
                ],
                "preguntas": [
                    ("Entonces, ¿para qué el trigger si el CHECK ya lo hacía?",
                     "Para esta regla, no hace falta. El trigger se justifica cuando la regla "
                     "consulta otra tabla, por ejemplo que la mascota esté activa al agendar."),
                ],
                "cuidado": "Si no retiras el CHECK antes de la demo, el UPDATE falla por la "
                           "restricción y nadie ve el trigger actuar.",
                "puente": "Ordenemos dónde va cada regla: las cuatro capas.",
            },
        },
        "Las cuatro capas": {
            "ideas": [
                "**1. CHECK, NOT NULL, DEFAULT:** lo que se decide mirando una sola fila.",
                "**2. UNIQUE y FK:** relaciones entre filas y entre tablas.",
                "**3. Trigger:** OLD contra NEW, otra tabla, o escribir en otra tabla.",
                "**4. Aplicación:** solo lo que la base no puede saber.",
            ],
            "notas": {
                "min": 4,
                "explica": "Cada regla tiene una capa natural, y el orden de las capas es el "
                           "orden de preferencia: lo más simple y difícil de saltarse primero.",
                "pasos": [
                    "Las cuatro capas, de la más preferida a la menos. Léelas en orden.",
                    "Dos reglas caen en su capa: «stock >= 0» en CHECK; «un veterinario, una "
                    "franja» en UNIQUE (id_veterinario, fecha_hora).",
                    "Otras dos: «auditar el cambio de estado» en trigger; «el formato del "
                    "correo» en la aplicación.",
                    "Cierre: lo que solo vive en la aplicación se salta conectándose por otra "
                    "vía (como hicimos con SET ROLE en la Clase 2).",
                ],
                "preguntas": [
                    ("¿La doble reserva no es para un trigger que cuente citas?",
                     "No: un UNIQUE la impide siempre, incluso con dos usuarios a la vez. El "
                     "trigger que cuenta puede fallar con concurrencia (se ve en la Clase 10)."),
                ],
                "puente": "Una guía rápida para decidirlo con preguntas.",
            },
        },
        "Donde vive cada validacion": {
            "ideas": [
                "¿Se decide mirando **una fila**? → **CHECK**.",
                "¿Relaciona **filas o tablas**? → **UNIQUE / FK**.",
                "¿Necesita **otra fila, OLD/NEW u otra tabla**? → **trigger**.",
                "¿La base **no puede saberlo**? → **aplicación**.",
            ],
            "notas": {
                "min": 2,
                "explica": "Las mismas cuatro capas convertidas en preguntas: la primera "
                           "respuesta «sí» decide dónde va la regla.",
                "pasos": [
                    "Recorre el árbol con dos reglas del grupo: pide una regla de la clínica y "
                    "bájenla pregunta por pregunta hasta su capa.",
                ],
                "ejemplo": "«Una cita no puede ser en domingo» → mira solo su fila → CHECK. "
                           "«No agendar a una mascota inactiva» → mira otra tabla → trigger o "
                           "procedimiento.",
                "puente": "¿Y cuándo un trigger es mala idea?",
            },
        },
        "Cuando NO se usa un trigger": {
            "ideas": [
                "Si lo resuelve un **CHECK o un UNIQUE**: la restricción gana.",
                "Si la regla admite **excepciones autorizadas**: va en la aplicación.",
                "Si envía un **correo** o llama un servicio: fuera de la transacción.",
                "Si tiene **varios pasos y decisiones**: es un procedimiento.",
            ],
            "notas": {
                "min": 3,
                "explica": "Los triggers son poderosos pero invisibles. Estos cuatro casos son "
                           "señales de que la regla debe vivir en otro lado.",
                "pasos": [
                    "Caso 1: si una restricción declarativa lo resuelve, no se escribe trigger.",
                    "Caso 2: un descuento que el administrador puede autorizar: el trigger no "
                    "distingue el caso autorizado.",
                    "Caso 3: enviar un correo dentro del trigger alarga la transacción y la "
                    "deja esperando a un servicio externo.",
                    "Caso 4: lógica con varios pasos va en un procedimiento, que se llama a "
                    "propósito y se prueba solo.",
                ],
                "cuidado": "Un trigger también se ejecuta en cargas masivas: un UPDATE de 10.000 "
                           "filas dispara 10.000 veces un trigger FOR EACH ROW.",
                "puente": "Cambiamos de tema: proteger y recuperar los datos.",
            },
        },
        "Seguridad y respaldo": {
            "ideas": [
                "La **seguridad** intenta que nada malo pase: roles y GRANT.",
                "El **respaldo** asume que igual va a pasar y prepara la vuelta.",
                "**pg_dump** respalda UNA base; los **roles** salen con "
                "**pg_dumpall --globals-only**.",
            ],
            "notas": {
                "min": 3,
                "explica": "Seguridad y respaldo responden preguntas distintas. La seguridad "
                           "reduce la probabilidad de daño; el respaldo reduce cuánto duele "
                           "cuando el daño ocurre.",
                "pasos": [
                    "Los dos lados: el escudo (roles y permisos de la Clase 2) y la base que "
                    "se copia.",
                    "pg_dump -Fc -d clinica -f clinica_AAAAMMDD.dump: copia una base, tablas y "
                    "datos, en formato que permite restaurar selectivamente.",
                    "pg_dumpall --globals-only: copia los roles, que pg_dump no incluye porque "
                    "son del servidor, no de la base.",
                ],
                "preguntas": [
                    ("Si restauro el dump, ¿vuelven los permisos?",
                     "Los GRANT sobre las tablas sí, pero si los roles no existen en el "
                     "servidor nuevo, nadie puede entrar. Por eso se respaldan aparte."),
                ],
                "puente": "Un plan de respaldo de verdad tiene seis partes.",
            },
        },
        "Plan de respaldo": {
            "ideas": [
                "**Qué y con qué**, y **con qué frecuencia** (con su razón de negocio).",
                "**Cuántas copias** y dónde: al menos una fuera del servidor.",
                "**RPO y RTO** en números, y un **restore de prueba** medido.",
                "**Qué NO cubre:** el riesgo que se acepta.",
            ],
            "notas": {
                "min": 3,
                "explica": "Un plan de respaldo no es una lista de comandos: dice cuánto se "
                           "puede perder, en cuánto se vuelve y cómo se comprueba que la vuelta "
                           "funciona.",
                "pasos": [
                    "Recorre las seis tarjetas en orden. Detente en la 2 (la hora se justifica "
                    "con el negocio: dump a las 20:30 porque la facturación cierra a las 20:00) "
                    "y en la 5: un respaldo que nunca se restauró es solo un archivo.",
                ],
                "ejemplo": "Retención 7 diarias, 4 semanales y 12 mensuales, con una copia fuera "
                           "del servidor.",
                "puente": "Las dos siglas del plan que más se confunden: RPO y RTO.",
            },
        },
        "RPO y RTO": {
            "ideas": [
                "**RPO:** cuántos datos se acepta perder, medido en tiempo.",
                "**RTO:** cuánto tiempo puede estar caída la base.",
                "Solo sirven con un **número acordado** con el dueño del negocio.",
            ],
            "notas": {
                "min": 4,
                "explica": "RPO mira hacia atrás (cuánto de lo último se pierde); RTO mira hacia "
                           "adelante (cuánto tarda en volver). Los dos se fijan con el negocio, "
                           "no con el administrador de la base.",
                "pasos": [
                    "La línea de tiempo: el último respaldo y el momento en que la base se cae.",
                    "Lo que hay entre el respaldo y la caída se pierde: eso es el RPO. Lo que "
                    "tarda en volver: el RTO.",
                    "Con números de la clínica: 4 horas de RPO son 15 a 20 citas sin registro; "
                    "8 horas de RTO un sábado es cerrar el día.",
                    "Quién decide: el dueño del negocio, porque es quien paga la pérdida.",
                ],
                "preguntas": [
                    ("¿Con un dump diario cuál es el RPO?",
                     "Hasta 24 horas. Si es demasiado, hace falta archivado continuo del WAL."),
                ],
                "puente": "¿Qué de todo esto podemos ejecutar en el navegador?",
            },
        },
        "Lo que PostgreSQL en el navegador": {
            "ideas": [
                "En el navegador corre todo el SQL de hoy: funciones, triggers, RAISE y bloques DO.",
                "pg_dump, pg_dumpall y pg_restore **no corren** ahí: son programas de línea de "
                "comandos.",
                "Lo que corre se demuestra con su salida; el plan de respaldo **se documenta**.",
            ],
            "notas": {
                "min": 2,
                "explica": "La herramienta del curso es PostgreSQL ejecutándose dentro del "
                           "navegador. Todo el código SQL de hoy funciona ahí; las herramientas "
                           "de respaldo no, porque necesitan archivos y un servidor.",
                "pasos": [
                    "Columna izquierda: lo que se ejecuta y se ve. Columna derecha: lo que se "
                    "escribe en el plan con su comando exacto.",
                ],
                "cuidado": "No digas «la herramienta no sirve para respaldos»: la razón precisa "
                           "es que esos programas leen y escriben archivos del servidor.",
                "puente": "Cómo se conecta lo de hoy con lo que ya vimos.",
            },
        },
        "Como amarra con las clases vecinas": {
            "ideas": [
                "**Clase 1:** el esquema y el CHECK de stock.",
                "**Clase 2:** los roles: current_user en la auditoría, pg_dumpall para "
                "respaldarlos.",
                "**Clase 3:** procedimientos y bloques DO, con los que se prueban los triggers.",
            ],
            "notas": {
                "min": 2,
                "explica": "Nada de hoy es nuevo del todo: cada pieza se apoya en una clase "
                           "anterior, y lo de hoy se usa en las siguientes.",
                "pasos": [
                    "Recorre la cadena de izquierda a derecha y cierra con lo que viene: la "
                    "Clase 8 retoma la transacción dentro de la que corre todo trigger, y la "
                    "Clase 10 explica por qué un trigger que cuenta no evita la doble reserva.",
                ],
                "puente": "Vamos a la demo.",
            },
        },
        "Demo del dia": {
            "ideas": [
                "Crear fn_precio_consulta y usarla dentro de un SELECT.",
                "Crear el trigger de auditoría y ejecutar **tres UPDATE**.",
                "Probar el trigger de stock con un UPDATE que lo dejaría negativo.",
            ],
            "notas": {
                "min": 15,
                "explica": "La demo muestra en vivo lo que se explicó: una función que se usa en "
                           "una consulta, un trigger que audita y un trigger que impide.",
                "pasos": [
                    "1) CREATE de fn_precio_consulta y SELECT con la tarifa por mascota. "
                    "2) Las dos piezas del trigger de auditoría; tres UPDATE de estado (el "
                    "tercero sin cambio) y SELECT de audit_cita: 2 filas. 3) Quitar el CHECK, "
                    "UPDATE a −7, crear el trigger BEFORE, repetir: error y stock en 3.",
                ],
                "cuidado": "Muestra siempre el SELECT del resultado: el trigger es invisible si "
                           "no se mira la tabla.",
                "puente": "Cierre de la clase.",
            },
        },
        "Clase 4 ·": {
            "notas": {
                "min": 3,
                "explica": "Cierre: la base ya no solo guarda; calcula con funciones, reacciona "
                           "con triggers y tiene un plan para volver si algo se pierde.",
                "pasos": [
                    "Pregunta de salida: «nombren una regla de la clínica y digan en qué capa "
                    "va». Toma dos o tres respuestas y corrige la capa si hace falta.",
                ],
            },
        },
    },
}


# Las demas clases viven en su propio archivo `bd2_contenido_cN.py` (CONTENIDO = {n: {...}}),
# para poder trabajarlas por separado; aqui se juntan.
import glob as _glob
import importlib as _importlib
import os as _os

for _f in sorted(_glob.glob(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),
                                           "bd2_contenido_c*.py"))):
    _m = _importlib.import_module(_os.path.splitext(_os.path.basename(_f))[0])
    for _n, _d in _m.CONTENIDO.items():
        CONTENIDO.setdefault(_n, {}).update(_d)
