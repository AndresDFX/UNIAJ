# -*- coding: utf-8 -*-
"""BD II · Clase 10 (Control de concurrencia): ideas proyectadas y GUION de cada lamina.

Mismo formato que la Clase 4 en `bd2_contenido_data.py` (ver `notas_guion.py`); se fusiona solo.
Los pasos de cada animacion estan en `config/animaciones/bd2/clase10/<huella>.js`: «Al entrar» es
el primer fotograma y «Clic k» cada uno de los siguientes. En las laminas sin animacion (codigo,
diagrama, ilustracion) los pasos llevan su propio rotulo («Lineas 1-4»), porque ahi no hay clics.

Las cifras son las de los datos sembrados del curso y las salidas se comprobaron en PostgreSQL
(PGlite): insumo 2 = Vacuna triple felina con stock 3, veterinario 1 con cita el 2026-09-01 08:00,
mascotas 4 (Mishi) y 5 (Bobby).
"""

CONTENIDO = {
    10: {
        "Encuadre de hoy": {
            "ideas": [
                "**Tema de hoy:** control de concurrencia, o qué pasa cuando dos personas tocan el "
                "mismo dato al mismo tiempo.",
                "Herramienta: **PostgreSQL en el navegador** · Bloque **120 min**",
                "Gratis + navegador · sin software de pago obligatorio.",
                "Recorrido: teoría del tema, una lámina por concepto, y demo del docente sobre la "
                "base de la clínica.",
                "Cada lámina se sostiene sola: sirve para repasar aunque hayas faltado.",
                "**Conceptos de hoy:** transacción y aislamiento · los tres fenómenos · los cuatro "
                "niveles · bloqueo pesimista y optimista · deadlock · el índice único parcial.",
            ],
            "notas": {
                "min": 4,
                "explica": "Hoy la pregunta es qué pasa cuando dos personas modifican el mismo dato "
                           "al mismo tiempo. La base no se daña: cumple las dos órdenes aunque se "
                           "contradigan. La clase muestra las cuatro formas de decirle que no.",
                "pasos": [
                    "Lee el tema y haz la pregunta de arranque: «dos recepcionistas agendan con la "
                    "misma veterinaria a la misma hora, en el mismo segundo: ¿qué guarda la base?». "
                    "Toma una o dos respuestas sin corregir todavía.",
                    ("Después", "Cierra: «al final van a poder nombrar el fenómeno, el nivel de "
                     "aislamiento que lo tapa y la línea de SQL que lo hace imposible»."),
                ],
                "cuidado": "Esta clase cae en festivo y es autónoma: si la grabas, este guion es el "
                           "de la grabación; si no, el estudiante la estudia con las láminas y estas "
                           "notas, así que cada una tiene que entenderse sola.",
                "puente": "Empezamos por lo que ya se vio en la Clase 8: la transacción.",
            },
        },
        "Mapa del bloque": {
            "notas": {
                "min": 1,
                "explica": "El recorrido de las dos horas: teoría con una lámina por concepto, demo "
                           "sobre la base de la clínica y práctica opcional.",
                "pasos": ["Señala solo los tramos; no te detengas. La práctica está en la carpeta "
                          "de la clase y es opcional."],
            },
        },
        "La transaccion como unidad de todo o nada": {
            "ideas": [
                "Una **transacción** agrupa las sentencias de un hecho: con COMMIT quedan todas, con "
                "ROLLBACK ninguna.",
                "**Concurrencia** es tener dos transacciones abiertas a la vez sobre los mismos "
                "datos, con sus operaciones intercaladas.",
                "Las dos consultan la franja, la ven **libre** y las dos insertan: dos citas al "
                "mismo minuto.",
                "Nada falló: el todo o nada protege **una** transacción, no a dos que se cruzan.",
            ],
            "notas": {
                "min": 5,
                "explica": "Una transacción es un grupo de sentencias que el motor trata como un "
                           "solo hecho: o se confirman todas con COMMIT o se deshacen todas con "
                           "ROLLBACK. Eso la protege de quedar a medias, pero no de otra transacción "
                           "que trabaja al mismo tiempo sobre los mismos datos. Cuando hay dos a la "
                           "vez, el motor intercala sus operaciones, y de ese intercalado salen "
                           "todos los problemas de hoy.",
                "pasos": [
                    "Todo o nada: agendar la cita (INSERT INTO cita) y descontar la vacuna (UPDATE "
                    "insumo) son un solo hecho. Con COMMIT quedan las dos; si la segunda falla, "
                    "ROLLBACK y no queda ninguna. Pregunta: «¿qué pasa si queda la cita y no el "
                    "descuento?» (el inventario miente).",
                    "Dos transacciones a la vez: la recepción A (T1) y la recepción B (T2) preguntan "
                    "si la veterinaria Restrepo tiene libre las 10:00. Las dos reciben 0 filas. "
                    "Subraya que las dos leen antes de que ninguna escriba.",
                    "Las dos insertan su cita (Mishi y Toby) y las dos confirman con COMMIT, sin "
                    "ningún error. Cada una decidió con un dato que la otra estaba a punto de "
                    "cambiar.",
                    "El resultado: dos filas en cita a las 10:00 con la misma veterinaria. La base "
                    "no está dañada: cumplió dos órdenes contradictorias porque nada le dijo que no "
                    "podía. El resto de la clase son las formas de decírselo.",
                ],
                "ejemplo": "Con varias recepcionistas y unas 150 citas al día, que dos agenden la "
                           "misma franja en el mismo segundo no es una rareza: es cuestión de "
                           "tiempo.",
                "preguntas": [
                    ("¿Y si pongo BEGIN y COMMIT alrededor del SELECT y el INSERT?",
                     "Sigue pasando. En READ COMMITTED, el nivel por omisión de PostgreSQL, cada "
                     "transacción solo ve lo confirmado: las dos leen «libre» antes de que la otra "
                     "confirme. La transacción da atomicidad, no exclusión."),
                    ("¿El motor no debería detectar la doble cita?",
                     "Solo si se le dice qué es inválido, con una restricción UNIQUE sobre "
                     "(id_veterinario, fecha_hora). Sin ella, dos citas a la misma hora son datos "
                     "perfectamente válidos."),
                ],
                "cuidado": "El error típico del docente es afirmar que «poner una transacción» "
                           "resuelve la concurrencia. No la resuelve: garantiza que las sentencias "
                           "de UNA transacción se apliquen juntas, nada más.",
                "puente": "Si el problema es que se intercalan, ¿por qué no ejecutar una detrás de "
                          "otra? Existe, y cuesta.",
            },
        },
        "Serializar de verdad existe": {
            "ideas": [
                "**Serializar** es ejecutar las transacciones una tras otra, sin choques, pero cada "
                "una espera a la anterior.",
                "Con ocho recepcionistas en fila, el tiempo de espera frente a la pantalla se "
                "**multiplica**.",
                "**Aislamiento** es lo que mi transacción puede ver de las otras que aún no "
                "terminan.",
                "Es la **I de ACID** y se configura con el nivel de aislamiento, a cambio de "
                "rendimiento.",
            ],
            "notas": {
                "min": 3,
                "explica": "La solución obvia es no intercalar: ejecutar las transacciones una "
                           "detrás de otra. Eso se llama serializar, y funciona, pero convierte ocho "
                           "operaciones simultáneas en una fila de ocho. Por eso el estándar SQL "
                           "ofrece una perilla, el nivel de aislamiento, para elegir cuánto se "
                           "protege cada transacción de las demás a cambio de cuánto rendimiento.",
                "pasos": [
                    "Ocho agendamientos a la vez terminan juntos: una unidad de tiempo para todos.",
                    "Los mismos ocho en fila: cada uno espera al anterior y el último tarda ocho "
                    "veces más. En recepción eso se siente como «el sistema está lento».",
                    "La pregunta que define el aislamiento: ¿qué puede ver mi transacción de las "
                    "otras que todavía no terminan? Es la I de ACID y la única de las cuatro que el "
                    "desarrollador configura; atomicidad, consistencia y durabilidad las garantiza "
                    "el motor siempre.",
                ],
                "ejemplo": "En PostgreSQL se pide con BEGIN ISOLATION LEVEL SERIALIZABLE. El motor "
                           "no pone a todas en fila literalmente: las deja correr en paralelo y, si "
                           "el resultado no equivale a ningún orden de una tras otra, aborta una con "
                           "un error de serialización que la aplicación debe reintentar.",
                "preguntas": [
                    ("¿Entonces siempre conviene SERIALIZABLE?",
                     "No: se paga en transacciones abortadas que hay que reintentar. Se usa donde la "
                     "anomalía cuesta más que el reintento."),
                    ("¿Qué significa cada letra de ACID?",
                     "Atomicidad (todo o nada), Consistencia (las reglas se cumplen), Aislamiento "
                     "(qué se ve de las otras) y Durabilidad (lo confirmado sobrevive a una caída)."),
                ],
                "cuidado": "No presentes SERIALIZABLE como la respuesta universal: el estudiante "
                           "aprende que el aislamiento es gratis y no reconoce el síntoma opuesto "
                           "(esperas, reintentos, tiempos de espera agotados).",
                "puente": "Para elegir el nivel hay que conocer las anomalías que existen: son tres.",
            },
        },
        "Los tres fenomenos indeseables": {
            "ideas": [
                "**Lectura sucia** es leer un dato que otra transacción aún no confirma, y que "
                "después deshace.",
                "**Lectura no repetible** es leer dos veces la misma fila en una transacción y "
                "obtener dos valores.",
                "**Lectura fantasma** es repetir un conteo y obtener otro número por una fila nueva "
                "que cumple el WHERE.",
                "La no repetible **cambia** una fila que ya existía; la fantasma **agrega** o quita "
                "filas.",
            ],
            "notas": {
                "min": 5,
                "explica": "El estándar SQL nombra tres cosas que pueden salir mal cuando una "
                           "transacción ve el trabajo de otra. Se entienden mejor con una escena de "
                           "la clínica, y la diferencia entre las dos últimas es la pregunta de "
                           "examen más fallada.",
                "pasos": [
                    "Lectura sucia: T1 inserta la cita de las 10:00 sin hacer COMMIT; T2 la ve y le "
                    "dice al dueño que la franja está ocupada; luego T1 hace ROLLBACK porque el "
                    "pago no pasó. T2 decidió con un dato que nunca existió.",
                    "Lectura no repetible: dentro de una facturación, T1 lee el stock del insumo 2 "
                    "(Vacuna triple felina) y obtiene 3; T2 vende 3 y confirma; T1 relee la misma "
                    "fila y obtiene 0. Misma consulta, misma transacción, dos valores.",
                    "Fantasma: T1 cuenta las citas del martes y obtiene 4; T2 inserta otra y "
                    "confirma; T1 vuelve a contar y obtiene 5. Ninguna fila vieja cambió: apareció "
                    "una nueva que cumple el WHERE.",
                ],
                "ejemplo": "La doble reserva del comienzo se parece al fantasma: las dos preguntan "
                           "«¿hay alguna cita a esa hora?» y la fila que cambiaría la respuesta "
                           "todavía no existe cuando preguntan.",
                "preguntas": [
                    ("¿En PostgreSQL puede pasar la lectura sucia?",
                     "No. Aunque se pida READ UNCOMMITTED, PostgreSQL nunca muestra datos sin "
                     "confirmar: lo trata como READ COMMITTED."),
                    ("¿Cómo distingo no repetible de fantasma en un ejercicio?",
                     "Pregunta si la fila ya existía. Si existía y cambió su valor, es no "
                     "repetible; si apareció o desapareció una fila del resultado, es fantasma."),
                ],
                "cuidado": "No digas que la lectura sucia es la más común: en PostgreSQL es "
                           "imposible. Las que sí aparecen con el nivel por omisión son la no "
                           "repetible y la fantasma.",
                "puente": "Veamos la doble reserva en dos líneas de tiempo.",
            },
        },
        "Doble reserva sin control": {
            "notas": {
                "min": 2,
                "explica": "La misma doble reserva, en dos líneas de tiempo: cada transacción lee "
                           "«libre», inserta y confirma. Es una condición de carrera: el resultado "
                           "depende de quién llega primero, y aquí las dos llegan antes de que la "
                           "otra confirme.",
                "pasos": [
                    ("Al entrar", "Arriba T1: lee la franja libre, inserta y su COMMIT sale bien. "
                     "Abajo T2 hace exactamente lo mismo y su COMMIT deja la doble reserva. "
                     "Subraya que ningún paso de T2 da error."),
                    ("Nota inferior", "Lee la mitigación: con UNIQUE (id_veterinario, fecha_hora) "
                     "el segundo INSERT falla en vez de crear la doble reserva. Se ve en código al "
                     "final del bloque."),
                ],
                "ejemplo": "Así se documenta un escenario de concurrencia que no se puede ejecutar: "
                           "una tabla con columnas paso, T1, T2 y estado de la fila, en orden de "
                           "tiempo.",
                "preguntas": [
                    ("¿Por qué no se puede ver esto en la base del curso?",
                     "Porque PostgreSQL en el navegador tiene una sola sesión: no hay dos "
                     "transacciones abiertas a la vez. Se demuestra lo que sí se puede (que la base "
                     "acepta el dato inválido y que la restricción lo rechaza) y el cruce se "
                     "documenta en la línea de tiempo."),
                ],
                "cuidado": "Validar con «si COUNT(*) = 0, inserto» dentro de un procedimiento "
                           "tampoco lo evita: entre el SELECT y el INSERT cabe la otra transacción.",
                "puente": "¿Qué nivel de aislamiento tapa cada fenómeno? Los cuatro niveles.",
            },
        },
        "Los cuatro niveles de aislamiento": {
            "ideas": [
                "Cada nivel se define por cuáles de los **tres fenómenos** deja pasar, de menos a "
                "más aislado.",
                "**READ COMMITTED** es el nivel por omisión de PostgreSQL e impide la lectura sucia, "
                "nada más.",
                "**REPEATABLE READ** impide además la no repetible, y en PostgreSQL tampoco deja ver "
                "fantasmas.",
                "**SERIALIZABLE** impide los tres, y a cambio puede abortar transacciones que hay "
                "que reintentar.",
            ],
            "notas": {
                "min": 5,
                "explica": "Los cuatro niveles del estándar no se memorizan como lista: se definen "
                           "por cuáles de los tres fenómenos permiten, y cada uno tapa uno más que "
                           "el anterior. Subir de nivel nunca es gratis: se paga en esperas o en "
                           "transacciones abortadas.",
                "pasos": [
                    "La tabla tiene las tres anomalías como columnas; rojo significa «puede "
                    "ocurrir». READ UNCOMMITTED: rojo en las tres. En PostgreSQL se puede pedir, "
                    "pero se comporta como READ COMMITTED: nunca muestra datos sin confirmar.",
                    "READ COMMITTED: verde en lectura sucia, rojo en las otras dos. Es el nivel por "
                    "omisión de PostgreSQL (también de Oracle y SQL Server): el que tiene cualquier "
                    "base que nadie configuró. Cada sentencia ve una foto nueva de lo confirmado.",
                    "REPEATABLE READ: impide también la no repetible, porque toda la transacción "
                    "trabaja sobre la foto tomada al empezar. El estándar todavía permite "
                    "fantasmas; PostgreSQL no los deja ver, por esa misma foto.",
                    "SERIALIZABLE: verde en las tres; el resultado equivale a ejecutar una tras "
                    "otra. Cuando PostgreSQL detecta que eso no se cumple, aborta una con un error "
                    "de serialización y la aplicación debe reintentarla.",
                ],
                "ejemplo": "Pregunta al grupo: con READ COMMITTED, si en una facturación leo dos "
                           "veces el stock del insumo 2, ¿puedo obtener 3 y luego 0? (Sí: lectura no "
                           "repetible.) ¿Y con REPEATABLE READ? (No: las dos lecturas ven la misma "
                           "foto.)",
                "preguntas": [
                    ("¿REPEATABLE READ evita la doble reserva?",
                     "No. Cada transacción ve su foto, las dos ven la franja libre e insertan filas "
                     "distintas. Solo SERIALIZABLE la detecta (abortando una) o una restricción "
                     "UNIQUE la impide siempre."),
                    ("¿Por qué en MySQL REPEATABLE READ tampoco muestra fantasmas?",
                     "Porque su motor InnoDB usa una foto para las lecturas y candados de rango "
                     "(gap locks) para las lecturas con bloqueo. Es una desviación del estándar, "
                     "como la de PostgreSQL."),
                ],
                "cuidado": "Rojo en la tabla significa «la anomalía puede ocurrir», no «el nivel "
                           "está mal». Dilo al entrar: la X confunde.",
                "puente": "Así se consulta y se cambia el nivel en PostgreSQL.",
            },
        },
        "Niveles de aislamiento: que anomalia": {
            "notas": {
                "min": 3,
                "explica": "Cómo se consulta y cómo se cambia el nivel de aislamiento en "
                           "PostgreSQL. El nivel se elige por transacción, al abrirla.",
                "pasos": [
                    ("Línea 1", "SHOW transaction_isolation responde read committed: el nivel por "
                     "omisión."),
                    ("Líneas 3-5", "BEGIN ISOLATION LEVEL REPEATABLE READ abre una transacción que "
                     "trabaja sobre una foto fija: la misma consulta devuelve lo mismo hasta el "
                     "COMMIT."),
                    ("Líneas 7-10", "SERIALIZABLE: si dos transacciones no se pueden ordenar, "
                     "PostgreSQL aborta una con «could not serialize access due to read/write "
                     "dependencies among transactions» (SQLSTATE 40001)."),
                    ("Líneas 12-13", "READ UNCOMMITTED existe en la sintaxis pero se comporta como "
                     "READ COMMITTED. Y SERIALIZABLE no evita el error: obliga a reintentar."),
                ],
                "ejemplo": "La otra forma de pedirlo: BEGIN; SET TRANSACTION ISOLATION LEVEL "
                           "SERIALIZABLE; como primera sentencia de la transacción.",
                "preguntas": [
                    ("Si pido READ UNCOMMITTED, ¿SHOW dice read committed?",
                     "No: SHOW transaction_isolation dice read uncommitted, porque informa lo que se "
                     "pidió; lo que cambia es el comportamiento, que es el de READ COMMITTED."),
                    ("¿El nivel queda para toda la sesión?",
                     "Con BEGIN ISOLATION LEVEL vale solo para esa transacción. Para la sesión: SET "
                     "SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL …"),
                ],
                "cuidado": "En una sola sesión no se ve ningún aborto de serialización: hacen falta "
                           "dos transacciones concurrentes. El código corre sin error y es todo lo "
                           "que se puede mostrar aquí.",
                "puente": "Otra forma de evitar el choque: no dejar que la segunda lea. El bloqueo "
                          "pesimista.",
            },
        },
        "Control pesimista": {
            "ideas": [
                "El control **pesimista** asume que el choque va a ocurrir y bloquea la fila antes "
                "de tocarla.",
                "**SELECT … FOR UPDATE** toma la fila, y otra transacción que la pida así espera "
                "hasta el COMMIT.",
                "Al entrar, la segunda lee el **dato verdadero**: stock 0, y rechaza la venta.",
                "Su costo es la **espera**: transacciones cortas, o NOWAIT y SKIP LOCKED para no "
                "esperar.",
            ],
            "notas": {
                "min": 4,
                "explica": "El control pesimista parte de que el conflicto va a ocurrir, así que "
                           "bloquea el recurso antes de usarlo. SELECT … FOR UPDATE lee la fila y la "
                           "deja tomada hasta el COMMIT o el ROLLBACK: otra transacción que la pida "
                           "con FOR UPDATE, o que intente modificarla, espera. Cuando la primera "
                           "termina, la segunda entra y ve el valor ya actualizado.",
                "pasos": [
                    "T1 ejecuta SELECT stock FROM insumo WHERE id_insumo = 2 FOR UPDATE: lee stock 3 "
                    "y la fila queda con bloqueo exclusivo (en rojo). T2 pide la misma fila con FOR "
                    "UPDATE y queda esperando (el reloj).",
                    "T1 descuenta 3 (UPDATE insumo SET stock = stock - 3) y confirma. El stock queda "
                    "en 0 y el COMMIT libera la fila.",
                    "T2 por fin entra y lee stock 0, no 3. Su validación «¿alcanza para 3?» dice que "
                    "no y rechaza la venta. Sin el bloqueo, T2 habría decidido con el 3 que leyó "
                    "antes y vendido unidades que ya no existen.",
                    "El costo es la espera. Regla de diseño: entre el FOR UPDATE y el COMMIT no va "
                    "ninguna llamada externa ni una pantalla esperando al usuario. Si no se quiere "
                    "esperar: NOWAIT falla de inmediato y SKIP LOCKED salta la fila tomada.",
                ],
                "ejemplo": "Dos auxiliares facturan la última Vacuna triple felina (stock 3) y las "
                           "dos piden 3. Con FOR UPDATE solo una la vende; la otra recibe «no "
                           "alcanza» en vez de vender unidades que no hay.",
                "preguntas": [
                    ("¿Un SELECT normal también espera?",
                     "No. En PostgreSQL un SELECT sin FOR UPDATE nunca espera: lee la última versión "
                     "confirmada (aquí, 3). Solo esperan quienes piden la fila con FOR UPDATE o "
                     "intentan modificarla."),
                    ("¿Y si T1 nunca confirma?",
                     "T2 espera indefinidamente, salvo que use NOWAIT, SKIP LOCKED o SET "
                     "lock_timeout = '5s', que hace fallar la espera a los cinco segundos."),
                ],
                "cuidado": "FOR UPDATE WAIT 5 es sintaxis de Oracle: en PostgreSQL da error de "
                           "sintaxis. El equivalente es SET lock_timeout.",
                "puente": "En código: el bloqueo explícito y una alternativa que no bloquea nada.",
            },
        },
        "El bloqueo explicito y la actualizacion condicional": {
            "notas": {
                "min": 3,
                "explica": "Dos maneras de que el doble descuento no ocurra. La A bloquea la fila y "
                           "obliga a esperar; la B no bloquea nada: mete la condición dentro del "
                           "UPDATE para que comprobar y escribir sean una sola sentencia.",
                "pasos": [
                    ("Líneas 1-5", "Opción A: BEGIN, SELECT … FOR UPDATE (devuelve 3 y toma la "
                     "fila), UPDATE que resta 3 y COMMIT, que la libera. Es la que hace falta "
                     "cuando hay que leer, calcular con datos de varias tablas y después escribir."),
                    ("Líneas 7-9", "Opción B: UPDATE … WHERE id_insumo = 2 AND stock >= 3. Si "
                     "alcanza, resta y responde UPDATE 1; si no, no toca nada y responde UPDATE 0. "
                     "Comprobar y escribir son atómicos."),
                    ("Líneas 10-11", "Ejecutadas en orden, la B responde UPDATE 0 porque la A ya "
                     "dejó el stock en 0: ese 0 es la señal de que otro llegó primero. En PL/pgSQL "
                     "se lee con GET DIAGNOSTICS v_filas = ROW_COUNT."),
                ],
                "ejemplo": "Después de las dos: SELECT id_insumo, nombre, stock FROM insumo WHERE "
                           "id_insumo = 2; → 2 | Vacuna triple felina | 0.",
                "preguntas": [
                    ("¿Cuál es mejor?",
                     "Para un descuento de stock, la B: una sola sentencia y sin esperas largas. La "
                     "A cuando la decisión necesita leer y calcular antes de escribir."),
                    ("¿El UPDATE de la B no bloquea también?",
                     "Sí, pero solo lo que dura la sentencia: la segunda transacción que quiera la "
                     "fila espera ese instante y vuelve a evaluar la condición con el valor nuevo."),
                ],
                "cuidado": "En una sola sesión FOR UPDATE nunca espera, porque nadie más tiene la "
                           "fila: que corra sin error no demuestra el bloqueo. La espera se explica "
                           "con la línea de tiempo.",
                "puente": "El enfoque opuesto: no bloquear nada y verificar al escribir.",
            },
        },
        "Control optimista": {
            "ideas": [
                "El control **optimista** no bloquea al leer: asume que el choque es raro y "
                "verifica al escribir.",
                "Se agrega una columna **version** y el UPDATE exige en el WHERE la versión que "
                "se leyó.",
                "Si otro guardó antes, la versión ya cambió y el UPDATE afecta **0 filas**: esa es "
                "la señal de conflicto.",
                "Se elige por la **frecuencia** del choque: frecuente, pesimista; raro, optimista.",
            ],
            "notas": {
                "min": 4,
                "explica": "El control optimista hace la apuesta contraria: deja que todos lean sin "
                           "bloquear y solo comprueba, al escribir, que nadie cambió el dato "
                           "mientras tanto. Para eso la tabla lleva una columna version (un entero, "
                           "o una fecha de última modificación) que sube en cada cambio.",
                "pasos": [
                    "Se lee la cita 812 con version 7, sin bloquear nada; el usuario cambia la hora "
                    "en pantalla. Al guardar: UPDATE cita SET fecha_hora = …, version = version + 1 "
                    "WHERE id_cita = 812 AND version = 7.",
                    "Sin conflicto: nadie tocó la cita, la versión guardada sigue en 7, el UPDATE "
                    "encuentra la fila (UPDATE 1) y la deja en version 8.",
                    "Con conflicto: otra transacción guardó primero y la dejó en 8. El WHERE "
                    "version = 7 ya no encuentra nada: UPDATE 0. Cero filas afectadas es la señal; "
                    "no hay error.",
                    "La aplicación lee ese 0 y decide: reintenta o avisa «la cita cambió mientras "
                    "la editabas». Criterio: si la misma fila se disputa muchas veces al día (el "
                    "stock del insumo más vendido), pesimista; si el choque es raro (el teléfono de "
                    "un dueño), optimista, porque nadie espera.",
                ],
                "ejemplo": "La columna no existe en el esquema del curso; se agregaría con ALTER "
                           "TABLE cita ADD COLUMN version INT NOT NULL DEFAULT 1;",
                "preguntas": [
                    ("¿Por qué no comparar todas las columnas en vez de una versión?",
                     "Se puede, pero es largo y frágil. Un entero que sube en cada UPDATE resume "
                     "«alguien cambió esta fila» en una sola comparación."),
                    ("¿Quién sube la versión?",
                     "El mismo UPDATE que guarda: version = version + 1. Si alguna ruta del código "
                     "actualiza sin subirla, el mecanismo deja de detectar conflictos."),
                ],
                "cuidado": "El optimista no da error cuando hay conflicto: da 0 filas. Si la "
                           "aplicación no revisa cuántas filas afectó, el cambio del usuario se "
                           "pierde en silencio.",
                "puente": "Cuando dos transacciones se bloquean entre sí aparece el último "
                          "problema: el deadlock.",
            },
        },
        "Deadlock: la escena": {
            "ideas": [
                "Un **deadlock** ocurre cuando dos transacciones se esperan mutuamente y ninguna "
                "puede avanzar.",
                "PostgreSQL detecta el ciclo, aborta a una **víctima** con el error 40P01 y deja "
                "terminar a la otra.",
                "La aplicación debe **reintentar** la abortada: es el mecanismo funcionando, no una "
                "falla.",
                "Se previene tocando las tablas **siempre en el mismo orden** en todos los "
                "procedimientos.",
            ],
            "notas": {
                "min": 4,
                "explica": "Un deadlock, o interbloqueo, es un ciclo de esperas: cada transacción "
                           "tiene algo que la otra necesita y espera lo que la otra tiene. Ninguna "
                           "espera termina sola, así que el motor rompe el ciclo abortando una.",
                "pasos": [
                    "Facturación toma la fila de factura y luego pide la de insumo; devolución toma "
                    "la de insumo y luego pide la de factura. Flechas sólidas: lo que tiene; "
                    "punteadas: lo que espera. Es un ciclo: ninguna avanza.",
                    "PostgreSQL revisa su grafo de esperas (después de un segundo de espera, por "
                    "omisión), encuentra el ciclo y aborta una con «deadlock detected», código "
                    "40P01. Facturación obtiene la fila y termina. La abortada se deshace completa "
                    "y debe reintentarse.",
                    "Prevención: un orden fijo. Si todos los procedimientos tocan factura antes que "
                    "insumo, el ciclo no puede formarse. Se escribe una vez en el documento de "
                    "diseño y no cuesta rendimiento.",
                ],
                "ejemplo": "En Oracle el mismo error es ORA-00060 y en MySQL el 1213: cambia el "
                           "número, no el mecanismo.",
                "preguntas": [
                    ("¿Cuál transacción elige como víctima?",
                     "La documentación de PostgreSQL dice que es difícil de predecir y que no hay "
                     "que depender de eso. Por eso cualquier transacción que participe debe estar "
                     "lista para reintentar."),
                    ("¿El deadlock deja datos a medias?",
                     "No: la víctima se deshace completa, como cualquier transacción abortada."),
                ],
                "cuidado": "No presentes el deadlock como una catástrofe que se evita a toda costa: "
                           "lo correcto es prevenirlo con un orden fijo y, si igual ocurre, capturar "
                           "el error y reintentar.",
                "puente": "Antes de todos estos mecanismos hay una solución de una sola línea para "
                          "el caso estrella.",
            },
        },
        "Antes de los niveles": {
            "ideas": [
                "Un **índice único** sobre (id_veterinario, fecha_hora) hace imposible la doble "
                "reserva con una sola sentencia.",
                "El motor deja pasar el primer INSERT y rechaza el segundo con **violación de "
                "unicidad**.",
                "El procedimiento captura el error y responde en lenguaje de **negocio**: «ese "
                "horario acaba de ser tomado».",
                "Es **parcial** (WHERE estado <> 'CANCELADA') porque una cita cancelada no ocupa la "
                "franja.",
            ],
            "notas": {
                "min": 4,
                "explica": "Antes de pensar en niveles o bloqueos, la doble reserva tiene una "
                           "solución declarativa: decirle al motor que no pueden existir dos citas "
                           "vigentes del mismo veterinario a la misma hora. Una regla escrita así se "
                           "cumple siempre, venga la escritura de la aplicación, de un script de "
                           "carga o de alguien corrigiendo a mano.",
                "pasos": [
                    "La regla: CREATE UNIQUE INDEX uq_cita_vet_franja ON cita (id_veterinario, "
                    "fecha_hora) WHERE estado <> 'CANCELADA'. Una sentencia, y el motor la revisa "
                    "en cada INSERT y UPDATE.",
                    "Las dos recepciones insertan la misma franja (veterinario 1, 2026-09-01 "
                    "08:00). La primera entra; la segunda choca: «duplicate key value violates "
                    "unique constraint \"uq_cita_vet_franja\"», SQLSTATE 23505. Da igual el orden "
                    "o la velocidad: alguna llega segunda.",
                    "El procedimiento captura esa excepción (EXCEPTION WHEN unique_violation) y "
                    "responde «Ese horario acaba de ser tomado, elija otro». Nadie tuvo que "
                    "razonar sobre aislamiento.",
                    "Por qué es parcial: una cita CANCELADA no ocupa la franja, así que esa sí "
                    "entra aunque haya una vigente a la misma hora. Un UNIQUE de tabla no admite "
                    "WHERE: también contaría las canceladas y una franja cancelada no se podría "
                    "volver a agendar.",
                ],
                "ejemplo": "Con dos sesiones simultáneas, la segunda espera un instante a que la "
                           "primera confirme y solo entonces recibe la violación de unicidad: la "
                           "regla funciona también en concurrencia, que es lo que un trigger que "
                           "cuenta citas no logra.",
                "preguntas": [
                    ("¿Un índice es una restricción?",
                     "Un índice único hace el mismo trabajo que una restricción UNIQUE (el error "
                     "incluso dice «unique constraint»), pero admite WHERE. Por eso se usa aquí."),
                    ("¿Y si ya existe un ALTER TABLE … ADD CONSTRAINT uq_cita_vet_franja?",
                     "El nombre es de un solo objeto: el CREATE UNIQUE INDEX responde «relation "
                     "\"uq_cita_vet_franja\" already exists». Se borra la restricción (ALTER TABLE "
                     "cita DROP CONSTRAINT uq_cita_vet_franja) y se crea el índice."),
                ],
                "cuidado": "Si la tabla ya tiene duplicados, el índice no se crea («could not create "
                           "unique index … is duplicated»): primero se detectan y se limpian. Es lo "
                           "que hace la lámina siguiente.",
                "puente": "Primero, el problema reproducido y detectado en código.",
            },
        },
        "La doble reserva, reproducida y detectada": {
            "notas": {
                "min": 3,
                "explica": "En una sola sesión no se pueden ver dos transacciones cruzándose, pero "
                           "sí lo esencial: sin restricción, la base acepta dos citas en la misma "
                           "franja sin quejarse. Esta lámina reproduce el dato inválido, lo detecta "
                           "y lo limpia.",
                "pasos": [
                    ("Líneas 1-4", "Un INSERT con dos filas: Mishi (4) y Bobby (5), veterinario 2, "
                     "2026-09-15 10:00. Responde INSERT 0 2: las dos entran y no hay ningún error."),
                    ("Líneas 6-11", "La consulta de detección agrupa las citas vigentes por "
                     "veterinario y hora y se queda con los grupos de más de una: devuelve 1 fila, "
                     "veterinario 2, 2026-09-15 10:00, 2 citas. Es la que se corre antes de crear "
                     "la restricción en una base que ya tiene datos."),
                    ("Líneas 13-14", "Se borra la cita de mayor id_cita, la duplicada. Si no se "
                     "borra, el CREATE UNIQUE INDEX de la lámina siguiente falla con «could not "
                     "create unique index \"uq_cita_vet_franja\"» porque la clave está repetida."),
                ],
                "ejemplo": "Con los datos sembrados, antes de estos INSERT la consulta de detección "
                           "devuelve 0 filas: no hay ninguna franja duplicada.",
                "preguntas": [
                    ("¿Por qué el WHERE estado <> 'CANCELADA'?",
                     "Porque una cita cancelada no ocupa la franja: una cancelada y una vigente a la "
                     "misma hora no son doble reserva."),
                    ("¿Borrar la de mayor id no es arbitrario?",
                     "Sí. En una base real se decide con el negocio a quién se le reprograma; aquí "
                     "sobra la segunda que entró."),
                ],
                "cuidado": "SELECT MAX(id_cita) borra la última cita de toda la tabla: sirve justo "
                           "después de este INSERT, no como limpieza general.",
                "puente": "Con la tabla limpia, el índice que lo hace imposible.",
            },
        },
        "El indice unico parcial": {
            "notas": {
                "min": 3,
                "explica": "La regla que la clínica necesita y la prueba de que funciona: dos citas "
                           "vigentes del mismo veterinario a la misma hora ya no pueden existir, y "
                           "una cancelada no estorba.",
                "pasos": [
                    ("Líneas 1-4", "CREATE UNIQUE INDEX uq_cita_vet_franja ON cita "
                     "(id_veterinario, fecha_hora) WHERE estado <> 'CANCELADA'. Con los datos "
                     "limpios por la lámina anterior se crea sin error."),
                    ("Líneas 6-8", "Una cita CANCELADA en la franja que ya tiene la cita 1 "
                     "(Firulais, veterinario 1, 2026-09-01 08:00) entra: INSERT 0 1. El índice no "
                     "mira las canceladas."),
                    ("Líneas 10-14", "La misma franja, ahora vigente (PROGRAMADA): ERROR: duplicate "
                     "key value violates unique constraint \"uq_cita_vet_franja\", con el detalle "
                     "Key (id_veterinario, fecha_hora)=(1, 2026-09-01 08:00:00) already exists. "
                     "SQLSTATE 23505."),
                    ("Leyenda", "BEGIN y COMMIT no bastaban porque las dos leían «libre»; el índice "
                     "se verifica al escribir, el único momento que no depende de quién leyó "
                     "primero."),
                ],
                "ejemplo": "Para dar el mensaje de negocio: DO $$ BEGIN INSERT … ; EXCEPTION WHEN "
                           "unique_violation THEN RAISE NOTICE 'Ese horario acaba de ser tomado, "
                           "elija otro'; END $$; responde con ese NOTICE y la cita no entra.",
                "preguntas": [
                    ("¿El error deshace algo más?",
                     "Deshace la sentencia que falló, y la transacción en curso queda abortada "
                     "hasta su ROLLBACK si no se captura el error."),
                    ("¿Por qué el error dice «unique constraint» si es un índice?",
                     "Porque PostgreSQL informa igual cualquier violación de unicidad, venga de una "
                     "restricción UNIQUE o de un índice único."),
                ],
                "cuidado": "El nombre uq_cita_vet_franja es exacto y se usa una sola vez: si antes "
                           "se creó una restricción con ese nombre, este CREATE falla con «relation "
                           "\"uq_cita_vet_franja\" already exists».",
                "puente": "Ahora todo esto ejecutado en la demo.",
            },
        },
        "Demo del dia": {
            "ideas": [
                "Sin restricción, dos INSERT de la misma franja **entran** y la consulta de "
                "detección los encuentra.",
                "Con el índice único parcial, el segundo INSERT **falla** con violación de "
                "unicidad (23505).",
                "FOR UPDATE corre sin error en **una sola sesión**: la espera se documenta en una "
                "línea de tiempo.",
            ],
            "notas": {
                "min": 15,
                "explica": "La demo ejecuta lo que se proyectó: el dato inválido aceptado, la "
                           "restricción que lo rechaza y el bloqueo que, en una sola sesión, corre "
                           "pero no se ve esperar.",
                "pasos": [
                    ("1 · Problema", "Ejecuta la lámina «La doble reserva, reproducida y "
                     "detectada»: el INSERT de dos filas (INSERT 0 2), la detección (1 fila: "
                     "veterinario 2, 2026-09-15 10:00, 2 citas) y el DELETE del duplicado."),
                    ("2 · Solución", "Ejecuta la lámina del índice único parcial: el CREATE UNIQUE "
                     "INDEX, la cancelada que sí entra y el INSERT vigente del veterinario 1 a las "
                     "08:00 del 2026-09-01, que sale con duplicate key value violates unique "
                     "constraint. Muestra el SELECT de cita para que se vea que no entró."),
                    ("3 · Bloqueo", "Ejecuta las opciones A y B: A devuelve stock 3 y descuenta; B "
                     "responde UPDATE 0. Cierra con SELECT stock FROM insumo WHERE id_insumo = 2; "
                     "→ 0."),
                    ("4 · Lo que no se ve", "Dibuja en una tabla paso / T1 / T2 / estado de la fila "
                     "la espera de T2 durante el FOR UPDATE: en una sola sesión nadie más tiene la "
                     "fila, así que nunca hay espera visible."),
                ],
                "ejemplo": "Tiempos sugeridos: problema 4 min, solución 4 min, bloqueo 4 min, línea "
                           "de tiempo 3 min.",
                "preguntas": [
                    ("¿Puedo abrir dos pestañas para simular dos recepcionistas?",
                     "No: cada pestaña levanta su propia base en memoria y no comparten nada. Para "
                     "ver la espera real hacen falta dos sesiones de psql contra un servidor, y las "
                     "vistas pg_locks y pg_stat_activity."),
                ],
                "cuidado": "Sin el DELETE del duplicado el índice no se crea («could not create "
                           "unique index … is duplicated») y el INSERT siguiente entra como una cita "
                           "más: borra el duplicado antes de crear el índice. El script del Kit "
                           "(Codigo/10_concurrencia_clinica.sql) hace la misma secuencia sobre una "
                           "tabla propia y termina en el INSERT que falla a propósito.",
                "puente": "Cierre de la clase.",
            },
        },
        "Clase 10 ·": {
            "notas": {
                "min": 3,
                "explica": "Cierre: el todo o nada protege una transacción, no a dos que se cruzan. "
                           "Para las que se cruzan hay cuatro herramientas: la restricción "
                           "declarativa, el nivel de aislamiento, el bloqueo pesimista y la "
                           "verificación optimista.",
                "pasos": [
                    "Pregunta de salida: «dos auxiliares venden la última vacuna al mismo tiempo: "
                    "¿qué mecanismo usan y qué recibe la aplicación cuando pierde?». Respuesta "
                    "esperada: el UPDATE con stock >= cantidad (o FOR UPDATE); la que pierde recibe "
                    "UPDATE 0 y debe avisar.",
                    ("Después", "Amarre: la revisión del avance (Clase 11) mira estos escenarios "
                     "documentados, y el contrato de operaciones (Clase 12) declara qué error "
                     "devuelve cada operación cuando pierde la carrera."),
                ],
            },
        },
    },
}
