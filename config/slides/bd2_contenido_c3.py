# -*- coding: utf-8 -*-
"""BD II · Clase 3 · Ideas proyectadas y GUION de cada lámina (notas del presentador).

Mismo formato que la Clase 4 en `bd2_contenido_data.py` (ver `notas_guion.py`); se fusiona solo.
Los pasos de cada animación salen de `config/animaciones/bd2/clase3/<huella>.js`.

Datos que se citan: los sembrados del curso (mascotas 1-8 con Rocky (3) y Kiara (8) inactivas,
10 citas con una del veterinario 1 el 2026-09-01 08:00, consultas en las citas 2, 5, 7 y 10, cita
4 CANCELADA, insumo 1 con 12 unidades). Mensajes y salidas comprobados en PostgreSQL (PGlite):
«is a procedure», «invalid transaction termination», «too few parameters specified for RAISE»,
SQLSTATE P0001, «relation "citas" does not exist» solo al llamar, y el error de FK cuando falta
IF NOT FOUND.
"""

CONTENIDO = {
    3: {
        "Encuadre de hoy": {
            "notas": {
                "min": 4,
                "explica": "Hasta hoy la base guardaba datos y decidía quién los toca. Hoy empieza "
                           "a contener comportamiento: un procedimiento almacenado que agenda una "
                           "cita solo si la regla de negocio se cumple, y una forma ordenada de "
                           "probar que la regla de verdad se cumple.",
                "pasos": [
                    "Recuerda el cierre de la Clase 1: la FK acepta una cita para una mascota "
                    "inactiva. Pregunta: «¿dónde ponemos esa regla para que ninguna pantalla se la "
                    "salte?».",
                    ("Cierre del encuadre", "«Hoy la escribimos dentro de la base, la hacemos "
                     "abortar cuando no se cumple y demostramos con pruebas que funciona»."),
                ],
                "cuidado": "Todo el código de hoy es PL/pgSQL de PostgreSQL. Si alguien escribe IS, "
                           "VARCHAR2 o la barra final de Oracle, el error es de sintaxis, no de "
                           "lógica.",
                "puente": "El recorrido de las dos horas.",
            },
        },
        "Mapa del bloque": {
            "notas": {
                "min": 1,
                "explica": "Las dos horas en cinco tramos: encuadre, teoría con una lámina por "
                           "concepto, demo en vivo, práctica opcional y cierre.",
                "pasos": ["Señala los tramos sin detenerte. La práctica tiene su guía en la carpeta "
                          "de la clase y es opcional."],
                "puente": "Qué es un procedimiento almacenado, en dos palabras.",
            },
        },
        "Que es un procedimiento almacenado": {
            "ideas": [
                "Un **procedimiento almacenado** es un bloque de código con nombre que vive dentro "
                "de la base de datos.",
                "Está **guardado** en el catálogo del motor, no en el equipo de quien lo escribió.",
                "Se **invoca** con una línea, CALL, que dispara varias sentencias dentro del motor.",
                "La regla de negocio queda escrita **una vez** y todos los que llaman pasan por "
                "ella.",
            ],
            "notas": {
                "min": 3,
                "explica": "Un procedimiento almacenado es un bloque de código con nombre que vive "
                           "en la base. Dos palabras lo explican: guardado, porque su fuente queda "
                           "en el motor aunque su autor se vaya, e invocado, porque una sola línea "
                           "dispara varias sentencias. Lo importante no es el ahorro: es que la regla "
                           "queda escrita una vez y ninguna pantalla se la puede saltar.",
                "pasos": [
                    "GUARDADO: el motor tiene un catálogo (pg_proc) con sp_agendar_cita y "
                    "sp_registrar_consulta. «Si cierran la pestaña, el procedimiento sigue ahí».",
                    "INVOCADO: CALL sp_agendar_cita(…) dispara adentro un SELECT (¿mascota "
                    "activa?), un IF con RAISE EXCEPTION y el INSERT. Una línea, varias "
                    "sentencias, una sola respuesta.",
                    "La frase de abajo: la regla queda escrita una vez y todos pasan por ella.",
                ],
                "ejemplo": "SELECT pg_get_functiondef('sp_agendar_cita'::regproc); devuelve la "
                           "definición completa, empezando por «CREATE OR REPLACE PROCEDURE "
                           "public.sp_agendar_cita(IN p_id_mascota integer, …», lista para "
                           "volver a ejecutar.",
                "preguntas": [
                    ("Ejecuté el CREATE y no dio error: ¿ya funciona?",
                     "No necesariamente. PostgreSQL revisa la sintaxis al crearlo, pero los "
                     "nombres de tablas y columnas solo al ejecutarlo: un INSERT INTO citas (con "
                     "s) se crea sin queja y falla en el CALL con relation \"citas\" does not "
                     "exist. La evidencia es el CALL corriendo."),
                ],
                "cuidado": "Si vienes de Oracle: aquí no existe el objeto «creado pero inválido». "
                           "Si el CREATE no protestó, el objeto existe; eso no quiere decir que "
                           "funcione.",
                "puente": "¿Por qué ponerlo en la base y no repetir el SQL en cada pantalla?",
            },
        },
        "Por que un procedimiento y no SQL": {
            "notas": {
                "min": 2,
                "explica": "Antes y después de poner la regla en un procedimiento: sin él, cada "
                           "pantalla la reescribe a su manera; con él, vive una vez en la base y "
                           "vale igual para la aplicación, un script de carga o soporte.",
                "pasos": [
                    "Lee las dos columnas emparejadas, fila por fila: reescribir la regla en cada "
                    "pantalla contra escribirla una vez; alguien la olvida contra todos la "
                    "respetan; SQL armado con texto (inyección) contra parámetros tipados; "
                    "cambiarla en N lugares contra cambiarla en uno.",
                ],
                "ejemplo": "La regla «una mascota inactiva no agenda» escrita en la pantalla de "
                           "agenda no protege una carga masiva desde un archivo; escrita en "
                           "sp_agendar_cita, sí, si la carga usa el procedimiento.",
                "cuidado": "La tercera fila (inyección) se explica completa dentro de unas láminas; "
                           "aquí solo nómbrala.",
                "puente": "Veamos cómo se escribe uno: el molde de PL/pgSQL.",
            },
        },
        "El molde de PL/pgSQL, y": {
            "ideas": [
                "El molde es fijo: CREATE PROCEDURE, parámetros, **LANGUAGE plpgsql** y **AS** (en "
                "Oracle era IS).",
                "Para el motor el cuerpo es **una cadena**: va entre $proc$ para no duplicar "
                "comillas ni punto y coma.",
                "La etiqueta es libre: **$$** funciona igual, y con nombre se distinguen bloques "
                "anidados.",
                "Se cierra con **$proc$;**: el punto y coma es obligatorio y la barra de Oracle es "
                "error.",
            ],
            "notas": {
                "min": 3,
                "explica": "El molde de un procedimiento es siempre el mismo, y se dicta entero "
                           "antes de escribir una sola validación, porque es donde más se pierde "
                           "tiempo sin haber entendido nada mal. Lo raro es el cuerpo entre signos "
                           "de dólar: para el motor el cuerpo es un texto, y así no hay que "
                           "duplicar comillas.",
                "pasos": [
                    "El molde completo y la primera trampa: después de LANGUAGE plpgsql va AS. En "
                    "Oracle es IS; aquí IS da error de sintaxis.",
                    "Se resalta el cuerpo, de DECLARE a END;: es una cadena. Entre $proc$ caben "
                    "punto y coma y comillas sin duplicarlas. $$ funciona igual; la etiqueta con "
                    "nombre sirve para bloques anidados.",
                    "El cierre: $proc$; con punto y coma obligatorio. La barra sola en una línea, "
                    "que en Oracle cierra el bloque, aquí es error.",
                ],
                "ejemplo": "CREATE PROCEDURE sp_y(p INT) LANGUAGE plpgsql IS $proc$ ... responde "
                           "«syntax error at or near \"IS\"».",
                "preguntas": [
                    ("¿Por qué LANGUAGE plpgsql si es obvio?",
                     "Porque PostgreSQL admite varios lenguajes (sql, plpgsql y otros) y no "
                     "adivina cuál se usa."),
                    ("¿Qué tipos uso?",
                     "INT, NUMERIC, TEXT, VARCHAR(n), TIMESTAMP, BOOLEAN, DATE. VARCHAR2 y NUMBER "
                     "son de Oracle y aquí no existen."),
                ],
                "cuidado": "sp_agendar_cita recibe tres parámetros, no cuatro: id_cita es SERIAL y "
                           "lo genera el motor. Pasarlo desde afuera no es error de sintaxis: es "
                           "error de diseño.",
                "puente": "El molde completo, en un procedimiento que corre.",
            },
        },
        "El molde de un procedimiento": {
            "notas": {
                "min": 2,
                "explica": "Un procedimiento completo y pequeño: da de baja un insumo poniendo su "
                           "stock en cero, después de comprobar que existe. Tiene todas las piezas "
                           "del molde.",
                "pasos": [
                    ("Líneas 1-4", "La firma: nombre y dos parámetros con su tipo (INT y VARCHAR). "
                     "Los dos son IN, el modo por omisión."),
                    ("Líneas 5-6", "LANGUAGE plpgsql y AS $proc$: aquí empieza el cuerpo."),
                    ("Líneas 7-8", "DECLARE: la variable local v_stock."),
                    ("Líneas 10-13", "SELECT ... INTO v_stock y, si no encontró fila, RAISE "
                     "EXCEPTION con el id. Primero se valida."),
                    ("Líneas 14-16", "Después se escribe: UPDATE del stock a cero y un RAISE NOTICE "
                     "que informa sin abortar."),
                    ("Líneas 17-18", "END; y $proc$; con su punto y coma."),
                ],
                "ejemplo": "CALL sp_dar_de_baja_insumo(1, 'vencido'); imprime «Insumo 1 dado de "
                           "baja (12 unidades): vencido». CALL sp_dar_de_baja_insumo(9999, "
                           "'inexistente'); responde «El insumo 9999 no existe».",
                "preguntas": [
                    ("¿Qué diferencia hay entre RAISE NOTICE y RAISE EXCEPTION?",
                     "NOTICE solo imprime un mensaje y el procedimiento sigue; EXCEPTION aborta y "
                     "deshace lo que se había escrito."),
                ],
                "cuidado": "La leyenda menciona $proc$: el código usa la misma etiqueta para que no "
                           "parezcan dos sintaxis distintas.",
                "puente": "Los parámetros tienen dirección, y eso decide cómo se devuelve un error.",
            },
        },
        "Los modos de parametro": {
            "ideas": [
                "El **modo** de un parámetro es la dirección del dato: IN entra, OUT sale, INOUT "
                "entra y sale.",
                "El modo **IN** es el de omisión y no se escribe: p_id_mascota INT ya es IN.",
                "Un error devuelto en un **OUT** se puede ignorar, y la fila ya quedó escrita.",
                "Con **RAISE EXCEPTION** el motor devuelve un fallo que no se ignora, y nada queda "
                "escrito.",
            ],
            "notas": {
                "min": 2,
                "explica": "Cada parámetro tiene un modo, que es la dirección en que viaja el dato. "
                           "IN entra y es el de omisión; OUT sale; INOUT entra y sale. Hoy no se "
                           "usa OUT para devolver errores, y la razón es de diseño: un código que "
                           "nadie revisa deja la cita creada.",
                "pasos": [
                    "p_id_mascota INT entra al procedimiento: es IN, y no hace falta escribirlo.",
                    "La alternativa mala: el procedimiento inserta y además pone p_resultado := "
                    "-1 en un OUT. La aplicación no lo mira, nada falla, y la regla no se cumplió.",
                    "La buena: RAISE EXCEPTION. El motor devuelve un fallo que la aplicación no "
                    "puede ignorar, y nada quedó escrito. Lee la frase final: el encabezado es un "
                    "contrato de nombre, orden y tipos.",
                ],
                "ejemplo": "En PostgreSQL el OUT de un procedimiento también se pasa al llamarlo: "
                           "con sp_out(p_id INT, OUT p_res INT), CALL sp_out(4) falla (no existe "
                           "ese procedimiento con un argumento) y CALL sp_out(4, NULL) devuelve "
                           "p_res = 8.",
                "preguntas": [
                    ("¿Cómo evito confundir el orden de dos parámetros del mismo tipo?",
                     "Con notación nombrada: CALL sp_agendar_cita(p_id_mascota => 1, "
                     "p_id_veterinario => 2, p_fecha_hora => TIMESTAMP '2026-09-15 10:00:00')."),
                ],
                "cuidado": "Si alguien intercambia dos parámetros INT en la firma, el procedimiento "
                           "se crea igual y agenda la cita para la mascota equivocada sin ningún "
                           "error.",
                "puente": "Ese RAISE EXCEPTION es la pieza que convierte el código en regla.",
            },
        },
        "RAISE EXCEPTION: la validacion": {
            "ideas": [
                "**RAISE EXCEPTION** convierte una consulta con nombre en una regla que el motor "
                "hace cumplir.",
                "Cada **%** del mensaje se reemplaza, en orden, por lo que sigue a la coma; %% "
                "imprime un porcentaje.",
                "La excepción **aborta** la llamada y deshace todo lo que ya se había escrito.",
                "El mensaje es **interfaz**: lo lee quien usa la aplicación y lo verifican las "
                "pruebas.",
            ],
            "notas": {
                "min": 3,
                "explica": "RAISE EXCEPTION lanza un error con un mensaje y aborta. No sale del "
                           "procedimiento con un aviso: el error llega hasta quien llamó y todo lo "
                           "que el procedimiento había escrito se deshace. Por eso es imposible que "
                           "quede una cita a medias, y no porque el código lo cuide: lo garantiza "
                           "el motor.",
                "pasos": [
                    "La línea RAISE EXCEPTION 'ERROR: la mascota % no existe', p_id: el % se "
                    "reemplaza por p_id (99) y el mensaje queda «ERROR: la mascota 99 no existe». "
                    "Para un porcentaje literal se escribe %%.",
                    "Dentro del CALL: se hizo un INSERT, luego una validación falla y se lanza la "
                    "excepción. La fila 3 que se había insertado desaparece: se deshizo.",
                    "La conclusión y la segunda idea: el mensaje es parte de la interfaz; se "
                    "escribe para la recepcionista, no para el programador.",
                ],
                "ejemplo": "Si hay más % que valores, el motor responde «too few parameters "
                           "specified for RAISE». Y todo RAISE EXCEPTION sin más lleva el código "
                           "SQLSTATE P0001.",
                "preguntas": [
                    ("¿Para qué sirve el SQLSTATE?",
                     "Para que la aplicación distinga un error de negocio de un fallo de la base "
                     "sin leer el texto. Se puede fijar uno propio con USING ERRCODE; hoy basta el "
                     "mensaje."),
                ],
                "cuidado": "El orden natural es validar primero y escribir después; aun así, si "
                           "algo falla tarde, el motor deshace lo escrito.",
                "puente": "Veámoslo con la regla que la FK no podía defender.",
            },
        },
        "RAISE EXCEPTION en accion": {
            "notas": {
                "min": 2,
                "explica": "La regla que quedó pendiente en la Clase 1: una mascota inactiva no "
                           "agenda. Un bloque DO la prueba con la mascota 3, Rocky, que existe pero "
                           "está inactiva.",
                "pasos": [
                    ("Líneas 2-4", "Un bloque DO, que se ejecuta una vez y no se guarda, con "
                     "p_id_mascota = 3."),
                    ("Líneas 5-8", "IF NOT EXISTS (mascota con ese id Y activa = 'S'): consulta "
                     "OTRA tabla, que es justo lo que un CHECK no puede hacer. Si no existe tal "
                     "fila, RAISE EXCEPTION."),
                    ("Línea 10", "La salida real: ERROR: La mascota 3 no existe o esta inactiva."),
                    ("Líneas 12-14", "Los comentarios: RAISE EXCEPTION no solo avisa, deshace; "
                     "por eso se valida primero y se escribe después."),
                ],
                "ejemplo": "Con p_id_mascota = 1 (Firulais, activa) el bloque termina sin mensaje: "
                           "la condición del IF es falsa.",
                "preguntas": [
                    ("¿Por qué un solo mensaje para «no existe» y «está inactiva»?",
                     "Aquí se juntan para mostrar el mecanismo. En el procedimiento de la "
                     "siguiente lámina se separan, porque la aplicación necesita distinguirlos."),
                ],
                "puente": "El mismo mecanismo dentro del procedimiento real de la clínica.",
            },
        },
        "El molde de PL/pgSQL y la validacion": {
            "notas": {
                "min": 3,
                "explica": "El procedimiento central de la clase, con su molde completo y sus tres "
                           "validaciones: la mascota debe existir, debe estar activa y la franja "
                           "del veterinario debe estar libre. Si alguna falla, el CALL aborta y no "
                           "inserta nada.",
                "pasos": [
                    ("Líneas 1-2", "Tres parámetros: mascota, veterinario y fecha_hora. id_cita no "
                     "se pasa porque es SERIAL."),
                    ("Línea 3", "LANGUAGE plpgsql AS $proc$: ni IS, ni VARCHAR2, ni barra final."),
                    ("Líneas 6-9", "SELECT activa INTO v_activa y, enseguida, IF NOT FOUND: la "
                     "mascota no existe."),
                    ("Líneas 10-12", "IF v_activa <> 'S': la mascota está inactiva."),
                    ("Líneas 13-16", "IF EXISTS una cita no cancelada del mismo veterinario a esa "
                     "hora: la franja está ocupada. Una cita CANCELADA no cuenta, porque libera la "
                     "franja."),
                    ("Líneas 17-19", "Solo si las tres pasan, el INSERT con estado 'PROGRAMADA'."),
                ],
                "ejemplo": "CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00') inserta; "
                           "con la mascota 3 responde «ERROR: la mascota 3 esta inactiva», con la "
                           "99 «ERROR: la mascota 99 no existe», y CALL sp_agendar_cita(2, 1, "
                           "TIMESTAMP '2026-09-01 08:00:00') «ERROR: el veterinario 1 ya tiene cita "
                           "en 2026-09-01 08:00:00». Ninguno de los tres deja filas nuevas. El "
                           "cliente muestra «ERROR:  ERROR: …» porque el mensaje ya trae la palabra "
                           "ERROR.",
                "preguntas": [
                    ("¿Por qué IF NOT FOUND va antes que el IF de activa?",
                     "Porque un SELECT INTO sin filas no lanza error en PL/pgSQL: deja v_activa en "
                     "NULL, y NULL <> 'S' no entra al IF. Sin NOT FOUND, el INSERT llega a la FK y "
                     "sale un error técnico de clave foránea en vez del mensaje del contrato."),
                    ("Si ya está el IF EXISTS, ¿para qué la restricción de unicidad?",
                     "Porque el IF EXISTS es código: dos sesiones a la vez pueden pasar las dos la "
                     "comprobación. La restricción la garantiza el motor; el IF EXISTS da el "
                     "mensaje claro. El porqué completo es de la Clase 10."),
                ],
                "cuidado": "La leyenda lo dice: con el mensaje en un parámetro OUT, el INSERT "
                           "seguiría corriendo. El error se lanza, no se devuelve.",
                "puente": "¿Toda la lógica debe ir en la base? La respuesta honesta.",
            },
        },
        "Donde debe vivir la logica": {
            "ideas": [
                "En la base, la regla se cumple **entre por donde se entre**: la aplicación, una "
                "carga o la consola.",
                "Permite permisos más finos: **EXECUTE** sobre el procedimiento sin INSERT sobre la "
                "tabla.",
                "Eso exige **SECURITY DEFINER**; si no, el cuerpo corre con los permisos de quien "
                "llama.",
                "En contra, se versiona peor y ata al motor; en la base van los **invariantes**.",
            ],
            "notas": {
                "min": 3,
                "explica": "La pregunta de fondo no tiene respuesta dogmática. A favor de la base: "
                           "la regla se cumple aunque alguien entre por fuera de la aplicación, se "
                           "ahorran viajes de red y se pueden dar permisos más finos. En contra: se "
                           "versiona peor, se prueba con más esfuerzo y ata el sistema al motor. El "
                           "criterio: en la base van las reglas que nunca pueden violarse.",
                "pasos": [
                    "Tres entradas, aplicación, migración y consola, pasan por sp_agendar_cita "
                    "antes de llegar a cita. «La regla se cumple entre por donde se entre».",
                    "Los permisos: GRANT EXECUTE sobre el procedimiento sí, GRANT INSERT sobre "
                    "cita no. Lee el aviso: eso solo funciona si el procedimiento es SECURITY "
                    "DEFINER (corre con los permisos de su dueño); sin esa cláusula corre con los "
                    "de quien llama y el INSERT se niega.",
                    "A favor y en contra. Cierra con el criterio de oficio: invariantes en la base; "
                    "orquestación, interfaz y reglas que cambian seguido, en la aplicación.",
                ],
                "ejemplo": "Invariantes de la clínica: el stock nunca negativo y la mascota "
                           "inactiva que no agenda. Regla volátil: el descuento de temporada, que "
                           "cambia cada mes.",
                "preguntas": [
                    ("¿Un procedimiento es más rápido?",
                     "Ahorra viajes de red y análisis repetido, pero no arregla una consulta mal "
                     "escrita; eso se ve en las Clases 6 y 7. En el navegador la mejora de red no "
                     "se puede medir."),
                ],
                "cuidado": "SECURITY DEFINER se nombra hoy y se usa en la Clase 12; no prometas que "
                           "dar EXECUTE basta.",
                "puente": "Uno de los argumentos a favor merece su lámina: la inyección de SQL.",
            },
        },
        "La inyeccion de SQL": {
            "ideas": [
                "Hay **inyección de SQL** cuando la aplicación pega texto del usuario dentro de la "
                "sentencia.",
                "Con Luna' OR '1'='1 la condición queda **siempre verdadera** y salen todas las "
                "mascotas.",
                "Un **parámetro** llega después de analizar la sentencia: se compara como dato y "
                "nunca se ejecuta.",
                "Un EXECUTE que **concatena** dentro del procedimiento reabre el agujero.",
            ],
            "notas": {
                "min": 3,
                "explica": "La inyección ocurre cuando la aplicación arma la consulta pegando texto "
                           "que escribió el usuario, y ese texto termina interpretado como código. "
                           "Un parámetro lo evita por un motivo preciso: el motor analiza la "
                           "sentencia antes de conocer el valor, así que el valor nunca vuelve a "
                           "pasar por el analizador.",
                "pasos": [
                    "El usuario escribe Luna, la aplicación arma … WHERE nombre = 'Luna' y "
                    "devuelve a Luna. Todo bien.",
                    "Escribe Luna' OR '1'='1: la sentencia queda WHERE nombre = 'Luna' OR "
                    "'1'='1', que es siempre verdadera, y la pantalla lista todas las mascotas.",
                    "Con parámetro: 1) el motor analiza la sentencia, 2) después llega el valor, "
                    "3) se compara como dato. Ninguna mascota se llama Luna' OR '1'='1. Lee el "
                    "aviso final sobre EXECUTE.",
                ],
                "ejemplo": "Si escribe '; DELETE FROM cita; -- el motor recibe dos sentencias y la "
                           "segunda borra la agenda.",
                "preguntas": [
                    ("¿Entonces un procedimiento es inmune?",
                     "No. Si dentro alguien escribe EXECUTE 'SELECT ... WHERE nombre = ' || "
                     "p_nombre, el agujero se reabre. Lo correcto es EXECUTE '... WHERE nombre = "
                     "$1' USING p_nombre, o format con %L para valores y %I para nombres."),
                ],
                "cuidado": "Regla dura del curso: ningún dato del usuario se concatena dentro de "
                           "una sentencia, ni en la aplicación ni en el procedimiento.",
                "puente": "Ya sabemos escribir el procedimiento. ¿Cómo demostramos que funciona?",
            },
        },
        "La bateria de pruebas: por que": {
            "ideas": [
                "Cuatro CALL seguidos se cortan en el **primer error**: los casos siguientes nunca "
                "corren.",
                "Un bloque **DO** es código anónimo que se ejecuta una vez y no se guarda en el "
                "motor.",
                "Con su **EXCEPTION**, cada bloque atrapa el error de su caso y deja seguir al "
                "siguiente.",
                "Cada caso deja una fila en **resultado_prueba**: una consulta muestra los cuatro "
                "veredictos.",
            ],
            "notas": {
                "min": 2,
                "explica": "Un procedimiento sin pruebas no está terminado. El problema práctico: "
                           "si se escriben los cuatro CALL seguidos y se ejecutan de un tiro, el "
                           "primero que falla aborta el resto. La solución es un bloque DO por "
                           "caso, cuya cláusula EXCEPTION atrapa el error y deja correr el "
                           "siguiente.",
                "pasos": [
                    "Cuatro CALL de un tiro: el positivo pasa, el de la mascota inactiva falla y "
                    "los otros dos quedan en gris: nunca corrieron.",
                    "Un bloque DO por caso: DO $$ BEGIN CALL … EXCEPTION … END $$;. «Se ejecuta "
                    "una vez y no se guarda en ningún catálogo».",
                    "La tabla resultado_prueba con una fila por caso: caso, esperado, obtenido y "
                    "paso.",
                ],
                "ejemplo": "Los cuatro casos con los datos de práctica: mascota 1 (activa, debe "
                           "agendar), mascota 3 (Rocky, inactiva), mascota 99 (no existe) y la "
                           "franja del veterinario 1 el 2026-09-01 a las 08:00 (ocupada).",
                "preguntas": [
                    ("¿Y si el procedimiento hace COMMIT?",
                     "Llamado desde un bloque con EXCEPTION falla con «invalid transaction "
                     "termination»: ese bloque abre un punto de retorno interno y no se puede "
                     "confirmar con él activo. Por eso el procedimiento de hoy no lleva COMMIT."),
                ],
                "cuidado": "La captura tiene costo: no se envuelve todo en EXCEPTION «por si "
                           "acaso». Es para las pruebas y para los casos que se quieren manejar.",
                "puente": "Así se escribe un caso de error completo.",
            },
        },
        "La bateria de pruebas: un bloque": {
            "notas": {
                "min": 2,
                "explica": "Un caso de error completo sobre el procedimiento del insumo: debe "
                           "fallar, y debe fallar por la razón esperada. El resultado queda en la "
                           "tabla, no en la pantalla.",
                "pasos": [
                    ("Líneas 2-4", "El bloque DO llama con el insumo 9999, que no existe."),
                    ("Líneas 5-6", "Si el CALL termina sin error, la prueba falló: se registra «no "
                     "lanzo error» con paso FALSE."),
                    ("Líneas 7-11", "Si cae en EXCEPTION, se registra SQLERRM (el texto del error) "
                     "y paso es la comparación SQLERRM ILIKE '%no existe%': falló Y por lo "
                     "esperado."),
                    ("Líneas 13-14", "El SELECT final y su salida real: insumo 9999 | El insumo 9999 "
                     "no existe | t."),
                ],
                "ejemplo": "El caso OK se escribe al revés: si el CALL termina, se registra OK con "
                           "paso TRUE; si cae en EXCEPTION, se registra SQLERRM con paso FALSE.",
                "preguntas": [
                    ("¿Dónde está la tabla resultado_prueba?",
                     "Se crea antes: resultado_prueba(id_prueba SERIAL, caso TEXT, esperado TEXT, "
                     "obtenido TEXT, paso BOOLEAN)."),
                ],
                "cuidado": "Sin el ILIKE, un procedimiento roto (una columna mal escrita) también "
                           "caería en EXCEPTION y la prueba saldría aprobada.",
                "puente": "El molde general de un caso de error, y la prueba que nadie piensa.",
            },
        },
        "El molde de un caso de error": {
            "ideas": [
                "En un caso de error, si el CALL termina **sin excepción** la prueba falló y se "
                "registra así.",
                "Si cae en **EXCEPTION**, se guarda SQLERRM, el texto del error recién capturado.",
                "Son **cuatro casos**: mascota activa, inactiva, inexistente y franja ocupada, cada "
                "uno en su bloque.",
                "Un conteo de cita antes y después debe pasar de **10 a 11**: el válido escribió y "
                "los errores no.",
            ],
            "notas": {
                "min": 2,
                "explica": "El molde de un caso de error invierte la lógica habitual: llegar al "
                           "final sin excepción es el fallo. Y la batería se cierra con una prueba "
                           "que nadie piensa: contar las citas antes y después.",
                "pasos": [
                    "Recorre la imagen: el bloque DO con sus dos salidas (sin error, se registra "
                    "«FALLO: no lanzó error»; con error, se registra SQLERRM), los cuatro casos y, "
                    "abajo, el conteo de cita: 10 antes, 11 después.",
                ],
                "ejemplo": "Si el conteo diera 14, los tres casos de error habrían dejado filas: "
                           "el procedimiento se queja pero escribe igual.",
                "preguntas": [
                    ("¿Por qué el conteo si ya tengo resultado_prueba?",
                     "Porque la tabla prueba que el procedimiento se queja; el conteo prueba que "
                     "el caso válido escribió y que los tres errores no dejaron basura."),
                ],
                "cuidado": "El conteo depende de los datos: con los de práctica son 10 citas al "
                           "empezar. Si la base ya tenía pruebas anteriores, se recrea antes de "
                           "medir.",
                "puente": "Falta la trampa más cara: qué significa la columna paso.",
            },
        },
        "Que significa la columna paso": {
            "ideas": [
                "Un procedimiento **roto** también lanza excepción: una columna mal escrita, un tipo "
                "o una tabla.",
                "Por eso paso = TRUE «porque hubo error» da un **falso positivo**.",
                "Se verifica el **texto**: paso := SQLERRM ILIKE '%inactiva%' afirma que falló y "
                "por qué.",
                "La columna paso tiene **una sola lectura** para las cuatro filas, y se declara.",
            ],
            "notas": {
                "min": 3,
                "explica": "Capturar WHEN OTHERS y marcar la prueba como superada porque hubo "
                           "excepción no prueba nada: un procedimiento roto también lanza "
                           "excepciones. Lo que se verifica es el texto del error, con SQLERRM. "
                           "Así se afirma que falló y que falló por lo esperado.",
                "pasos": [
                    "Caso negativo, mascota inactiva, contra un procedimiento roto: una columna "
                    "mal escrita da «column \"activ\" does not exist». También es una excepción.",
                    "WHEN OTHERS THEN paso := TRUE: la prueba sale aprobada. Falso positivo.",
                    "paso := SQLERRM ILIKE '%inactiva%': el texto no dice «inactiva», paso queda "
                    "en f y el error queda a la vista.",
                    "Las dos frases finales: se afirma que falló Y por qué; y una sola lectura de "
                    "paso para las cuatro filas, declarada.",
                ],
                "ejemplo": "ILIKE compara sin importar mayúsculas: 'ERROR: la mascota 3 esta "
                           "inactiva' ILIKE '%inactiva%' es verdadero.",
                "preguntas": [
                    ("¿Puedo usar SQLSTATE en vez del texto?",
                     "Sí, si el procedimiento fija un código propio con USING ERRCODE. Con RAISE "
                     "EXCEPTION simple todos los errores de negocio son P0001, así que hoy se "
                     "compara el texto."),
                ],
                "cuidado": "Al revisar una batería, no te quedes con las cuatro filas en t: mira "
                           "cómo se calculó paso.",
                "puente": "Las dos lecturas posibles de paso, lado a lado.",
            },
        },
        "La columna paso y la trampa": {
            "ideas": [
                "En un caso de error, llegar al final **sin excepción** es el fallo de la prueba.",
                "No basta con que falle: **SQLERRM ILIKE** comprueba que falló por la razón "
                "esperada.",
                "paso admite dos lecturas, **coincidió con lo esperado** o **se completó**, y las "
                "dos valen.",
                "Se usa **la misma** lectura en las cuatro filas y se dice cuál en una línea.",
            ],
            "notas": {
                "min": 2,
                "explica": "La columna paso admite dos lecturas legítimas. Si significa «coincidió "
                           "con lo esperado», con el procedimiento correcto las cuatro filas quedan "
                           "en t. Si significa «la operación se completó», los tres casos de error "
                           "quedan en f aunque el procedimiento esté perfecto. Las dos valen; lo que "
                           "no vale es no decir cuál.",
                "pasos": [
                    "Recorre la imagen: arriba, paso := TRUE (mal) contra SQLERRM ILIKE (bien); "
                    "en el medio, la misma tabla con la lectura A (t, t, t, t) y la B (t, f, f, "
                    "f); abajo, la regla: una lectura para las cuatro filas, declarada.",
                ],
                "ejemplo": "Salida de una batería sana con la lectura A: 4 filas, el caso válido "
                           "con paso t y los tres inválidos con paso t y su SQLERRM literal.",
                "preguntas": [
                    ("¿Qué hago si un caso de error sale con paso f en la lectura A?",
                     "Es un hallazgo: el procedimiento dejó pasar algo que debía rechazar. Se "
                     "corrige el procedimiento, no la prueba."),
                ],
                "puente": "Probado el procedimiento, falta documentarlo para quien lo va a llamar.",
            },
        },
        "El contrato del procedimiento": {
            "ideas": [
                "El **contrato** se escribe para quien llama al procedimiento sin abrir su código.",
                "Firma y **ejemplo de llamada** dicen cómo se declara y cómo se invoca, con valores "
                "reales.",
                "Las **pre y postcondiciones** dicen qué debe ser cierto antes y qué queda después.",
                "La **tabla de errores** lleva el mensaje literal, y la decisión de diseño explica "
                "por qué aborta.",
            ],
            "notas": {
                "min": 2,
                "explica": "El contrato no es código: es lo que necesita quien va a llamar al "
                           "procedimiento sin abrirlo, por ejemplo quien construya la aplicación. "
                           "Sirve si permite escribir la llamada y manejar los errores sin leer el "
                           "cuerpo. Son seis bloques y cada uno responde una pregunta.",
                "pasos": [
                    "Bloques 1 y 2: firma exacta (¿cómo se declara?) y ejemplo de llamada (¿cómo "
                    "se invoca?).",
                    "Bloques 3 y 4: precondiciones (¿qué debe ser verdad antes?) y "
                    "postcondiciones (¿qué queda?, y si falla, nada).",
                    "Bloques 5 y 6: tabla de errores con el mensaje literal, y la decisión de "
                    "diseño (¿por qué aborta?). La frase final: errores del contrato y de la "
                    "batería, palabra por palabra.",
                ],
                "ejemplo": "Sin la postcondición del caso malo («si falla, no queda nada»), quien "
                           "llama no sabe si tiene que limpiar algo después de un error.",
                "cuidado": "El contrato no es un resumen del código: si para escribir la llamada "
                           "hay que leer el cuerpo, el contrato no sirve.",
                "puente": "Los seis bloques, llenos para sp_agendar_cita.",
            },
        },
        "Los 6 bloques del contrato": {
            "ideas": [
                "La **firma** lleva nombre, orden y tipo de cada parámetro; sin tipos es una "
                "descripción.",
                "El **ejemplo** es un CALL con valores reales que se puede copiar y correr tal cual.",
                "La **postcondición** del caso malo es explícita: si la llamada falla, no queda "
                "nada en cita.",
                "Cada RAISE EXCEPTION es una fila de la **tabla de errores**, con su texto exacto.",
            ],
            "notas": {
                "min": 2,
                "explica": "El contrato de sp_agendar_cita, lleno. Lo que lo vuelve útil es que se "
                           "puede copiar la llamada y programar la respuesta a cada error sin abrir "
                           "el procedimiento.",
                "pasos": [
                    "Recorre la tarjeta de arriba abajo: la firma con tipos; el CALL de ejemplo "
                    "con la mascota 1, el veterinario 2 y el 15 de septiembre a las 10:00; las "
                    "precondiciones; la postcondición con su «NADA cambia»; la tabla de errores "
                    "(mensaje literal y qué hace la aplicación); y la decisión de diseño.",
                ],
                "ejemplo": "Fila de la tabla de errores: «ERROR: la mascota 3 esta inactiva» → la "
                           "aplicación avisa que hay que reactivar la mascota antes de agendar.",
                "preguntas": [
                    ("¿El mensaje del tercer error tiene que ser ese?",
                     "No: es el que cada uno escriba en su RAISE EXCEPTION. Lo que se exige es "
                     "que el contrato y la batería usen exactamente el mismo texto."),
                ],
                "cuidado": "Una paráfrasis en la tabla de errores rompe el contrato: la aplicación "
                           "compara contra el texto exacto.",
                "puente": "Una distinción que se dice hoy y no en la Clase 4: procedimiento y "
                          "función.",
            },
        },
        "Procedimiento y funcion": {
            "ideas": [
                "Un **procedimiento** se llama con CALL para que **haga** algo: cambia datos y "
                "puede hacer COMMIT.",
                "Una **función** se usa dentro de una consulta para que **devuelva** un valor.",
                "Una función corre en la transacción de quien la llama: **no** puede hacer COMMIT "
                "ni ROLLBACK.",
                "SELECT de un procedimiento es un error: el motor responde «**is a procedure**» y "
                "sugiere CALL.",
            ],
            "notas": {
                "min": 2,
                "explica": "Un procedimiento se invoca para que haga algo, con CALL; una función se "
                           "invoca para que devuelva un valor, dentro de una expresión. No son dos "
                           "sabores del mismo objeto: solo el procedimiento puede confirmar o "
                           "deshacer la transacción, y el motor no deja usar uno donde va el otro.",
                "pasos": [
                    "PROCEDIMIENTO · hace: CALL sp_agendar_cita(…) cambia los datos y puede hacer "
                    "COMMIT o ROLLBACK.",
                    "FUNCIÓN · devuelve: SELECT fn_x(…) entrega un valor a la consulta y no puede "
                    "hacer COMMIT ni ROLLBACK. «No son dos sabores del mismo objeto».",
                    "La prueba: SELECT sp_agendar_cita(…) responde «is a procedure» con la pista "
                    "«To call a procedure, use CALL». El motor no deja confundirlos.",
                ],
                "ejemplo": "Al revés también falla: CALL de una función responde «is not a "
                           "procedure» y sugiere usar SELECT.",
                "preguntas": [
                    ("¿Por qué el objeto de hoy es procedimiento?",
                     "Porque agendar es una acción que cambia datos. La tarifa de una consulta, "
                     "que es un valor, será una función en la Clase 4."),
                ],
                "puente": "Una función real, y el error al revés, en código.",
            },
        },
        "PROCEDURE o FUNCTION: la diferencia": {
            "notas": {
                "min": 2,
                "explica": "Una función de una línea que cuenta las citas de un día y se usa dentro "
                           "de un SELECT, y el error que da intentar lo mismo con un procedimiento.",
                "pasos": [
                    ("Líneas 2-8", "CREATE FUNCTION con RETURNS INT y LANGUAGE sql: el cuerpo es "
                     "una sola consulta. p_dia + 1 es el día siguiente, así que el rango es medio "
                     "abierto: desde las 00:00 hasta antes de la medianoche."),
                    ("Línea 10", "SELECT fn_citas_del_dia(DATE '2026-09-01'): con los datos de "
                     "práctica devuelve 3."),
                    ("Líneas 12-14", "SELECT de un procedimiento: «sp_dar_de_baja_insumo(integer, "
                     "unknown) is a procedure»."),
                ],
                "ejemplo": "La función se puede usar en una lista de columnas: SELECT d::date, "
                           "fn_citas_del_dia(d::date) FROM generate_series(DATE '2026-09-01', DATE "
                           "'2026-09-03', INTERVAL '1 day') d;",
                "preguntas": [
                    ("¿Una función tiene que ser LANGUAGE sql?",
                     "No: puede ser plpgsql igual que un procedimiento. Esta es sql porque su "
                     "cuerpo es una sola consulta."),
                ],
                "cuidado": "«unknown» en el mensaje es el tipo del literal 'x' sin conversión: no "
                           "es un error aparte.",
                "puente": "La regla para decidir, en una sola pregunta.",
            },
        },
        "PROCEDURE o FUNCTION: cual": {
            "ideas": [
                "Si el resultado tiene que entrar en un **SELECT**, un WHERE o un ORDER BY, es una "
                "FUNCTION.",
                "Un **PROCEDURE** se invoca solo, con CALL; dentro de un SELECT el motor lo rechaza.",
                "Las dos pueden ser **LANGUAGE plpgsql**: el lenguaje no decide si devuelve un "
                "valor.",
                "Un procedimiento admite parámetros **OUT** y aun así no puede usarse dentro de un "
                "SELECT.",
            ],
            "notas": {
                "min": 1,
                "explica": "La decisión se toma con una sola pregunta: ¿el resultado tiene que "
                           "entrar en una consulta? Si sí, es función. Si lo que se necesita es "
                           "ejecutar pasos o manejar la transacción, es procedimiento.",
                "pasos": [
                    "Recorre el árbol: la pregunta arriba, FUNCTION a la izquierda (RETURNS, "
                    "SELECT nombre, fn_precio(especie) FROM mascota) y PROCEDURE a la derecha "
                    "(CALL; el SELECT se rechaza). Abajo, los tres mitos tachados.",
                ],
                "ejemplo": "Calcular el precio sugerido de una consulta según la especie, para "
                           "mostrarlo en un listado: función que devuelve NUMERIC.",
                "preguntas": [
                    ("¿Un OUT no hace que el procedimiento «devuelva» un valor?",
                     "Devuelve valores a quien hace el CALL, pero sigue sin poder ir dentro de un "
                     "SELECT. Devolver por OUT no es lo mismo que ser invocable en una consulta."),
                ],
                "puente": "Cuando algo no funciona: depurar sin depurador.",
            },
        },
        "Depurar sin depurador": {
            "ideas": [
                "Primero, qué error se lee: el del **CREATE** es de sintaxis; el del **CALL**, de "
                "ejecución.",
                "Con **RAISE NOTICE** se dejan trazas sin abortar; solo EXCEPTION detiene la "
                "llamada.",
                "Se **aísla** la consulta que falla y se corre suelta con el valor del caso.",
                "Se prueba con **casos deliberados**: uno correcto y tres de error, cada uno en su "
                "bloque.",
            ],
            "notas": {
                "min": 2,
                "explica": "Sin depurador también se depura, con cuatro movimientos: saber qué "
                           "error se está leyendo, dejar trazas, aislar la consulta sospechosa y "
                           "probar con casos hechos a propósito.",
                "pasos": [
                    "¿Qué error leo? El del CREATE PROCEDURE es de sintaxis y señala línea y "
                    "posición. El del CALL es de ejecución: ahí salen las tablas y columnas mal "
                    "escritas.",
                    "Trazas: RAISE NOTICE 'paso 2, v_activa = %', v_activa; imprime sin abortar. "
                    "RAISE tiene niveles (NOTICE, WARNING, EXCEPTION) y solo el último aborta.",
                    "Aislar: SELECT activa FROM mascota WHERE id_mascota = 3, suelto, con el valor "
                    "que falló. Así se sabe si falla la consulta o la lógica que la rodea.",
                    "Casos deliberados: uno correcto y tres de error, cada uno en su bloque DO.",
                ],
                "ejemplo": "Un procedimiento con INSERT INTO citas (con s) se crea sin error; el "
                           "CALL responde «relation \"citas\" does not exist». Es un error de "
                           "ejecución, no de creación.",
                "cuidado": "A diferencia de Oracle, no hay vista de errores que consultar ni "
                           "objetos inválidos: si el CREATE no protestó, el objeto existe.",
                "puente": "El motor de hoy y lo que no hay que copiar de Oracle.",
            },
        },
        "El motor de hoy es PostgreSQL": {
            "ideas": [
                "El motor de la clase es **PostgreSQL**: todo el código de hoy es PL/pgSQL.",
                "Vienen de Oracle cuatro trampas: IS por **AS**, VARCHAR2 por TEXT, "
                "RAISE_APPLICATION_ERROR y la barra.",
                "Oracle sirve como **contraste** de sintaxis, no como lugar donde se trabaja.",
                "La **fuente de verdad** es el archivo .sql de la carpeta, nunca la pestaña del "
                "navegador.",
            ],
            "notas": {
                "min": 1,
                "explica": "Todo lo de hoy corre en PostgreSQL dentro del navegador: CREATE "
                           "PROCEDURE, el dólar, RAISE EXCEPTION, los bloques DO y SQLERRM. Oracle "
                           "queda como contraste para quien lo encuentre en el trabajo, con cuatro "
                           "diferencias que vale la pena nombrar y no más.",
                "pasos": [
                    "Las cuatro parejas: IS → AS; VARCHAR2 y NUMBER → TEXT e INT; "
                    "RAISE_APPLICATION_ERROR → RAISE EXCEPTION; la barra final → error de "
                    "sintaxis.",
                    "La regla operativa: la fuente de verdad es el archivo .sql de la carpeta. "
                    "Quien reconstruye procedimiento, pruebas y datos pegando su archivo, va "
                    "bien.",
                ],
                "cuidado": "No dediques más de un minuto a Oracle: cada minuto en la sintaxis del "
                           "otro motor es un minuto que no se dedica al tema.",
                "puente": "Un segundo procedimiento, donde se practica otra decisión.",
            },
        },
        "El segundo procedimiento": {
            "ideas": [
                "sp_registrar_consulta escribe en consulta, donde **UNIQUE (id_cita)** ya impide "
                "dos por cita.",
                "El **IF EXISTS** previo cambia el error técnico por un mensaje que la recepción "
                "entiende.",
                "También valida lo que el UNIQUE no ve: que la cita **exista** y que no esté "
                "**CANCELADA**.",
                "La restricción **se queda**: es la última línea de defensa si alguien entra por "
                "fuera.",
            ],
            "notas": {
                "min": 3,
                "explica": "El segundo procedimiento registra la consulta de una cita. La tabla ya "
                           "tiene UNIQUE en id_cita, así que el motor impide dos consultas para la "
                           "misma cita. Entonces, ¿para qué validar? Por el mensaje, y porque hay "
                           "reglas que la restricción no ve.",
                "pasos": [
                    "Solo con UNIQUE, la segunda consulta para la cita 7 falla con «duplicate key "
                    "value violates unique constraint \"consulta_id_cita_key\"»: técnico, nombra "
                    "el índice.",
                    "Con IF EXISTS (SELECT 1 FROM consulta WHERE id_cita = p_id_cita) THEN RAISE: "
                    "«ERROR: la cita 7 ya tiene consulta registrada». Lo entiende la "
                    "recepcionista.",
                    "Lo que el UNIQUE no ve: si la cita existe y si no está CANCELADA. La frase: "
                    "la restricción es la última línea de defensa; el procedimiento, la primera.",
                ],
                "ejemplo": "Con los datos de práctica: la cita 1 está PROGRAMADA y no tiene "
                           "consulta (debe funcionar), la cita 4 está CANCELADA (debe fallar) y la "
                           "cita 2 ya tiene consulta (debe fallar).",
                "preguntas": [
                    ("Si ya está el procedimiento, ¿quito el UNIQUE?",
                     "No. El procedimiento mejora el mensaje; la restricción sigue protegiendo "
                     "cuando alguien entra por fuera. Primero lo declarativo, encima el "
                     "procedimiento."),
                ],
                "cuidado": "El orden importa: el IF EXISTS va antes del INSERT; si se deja chocar "
                           "contra el UNIQUE, la aplicación recibe un error que no sabe traducir.",
                "puente": "Cómo se conecta todo esto con las clases vecinas.",
            },
        },
        "Como amarra con las clases vecinas": {
            "ideas": [
                "La **Clase 1** dejó el esquema y la baja lógica con activa = 'S' o 'N', que hoy "
                "se valida.",
                "La **Clase 2** dejó los roles: recepción agendará con EXECUTE y no con INSERT.",
                "La **Clase 4** cuelga de este procedimiento una función y dos triggers.",
                "La **Clase 8** decide quién confirma la transacción, y la **12** consume estos "
                "procedimientos.",
            ],
            "notas": {
                "min": 1,
                "explica": "Lo de hoy usa lo que dejaron las clases anteriores y lo retoman las "
                           "siguientes.",
                "pasos": [
                    "Antes: la Clase 1 dejó el esquema y la baja lógica; la Clase 2, los roles y "
                    "la idea de EXECUTE en vez de INSERT; hoy, los procedimientos.",
                    "Después: la Clase 4 decide para cada regla si va en CHECK, trigger o "
                    "aplicación; la 8 retoma quién confirma la transacción; la 12 consume estos "
                    "procedimientos desde la aplicación.",
                ],
                "puente": "Vamos a la demo.",
            },
        },
        "Demo del dia": {
            "ideas": [
                "Crear sp_agendar_cita con sus validaciones y llamarlo con un caso válido.",
                "Llamarlo con una mascota **inactiva** y una **inexistente**: cada una aborta con "
                "su mensaje.",
                "Correr la batería de bloques DO y comprobar con un conteo que cita pasó de **10 a "
                "11**.",
            ],
            "notas": {
                "min": 15,
                "explica": "La demo junta lo de hoy: el procedimiento con sus validaciones, los "
                           "CALL que abortan con su mensaje literal, la batería de pruebas en "
                           "resultado_prueba y el conteo que demuestra que los errores no dejaron "
                           "nada.",
                "pasos": [
                    "1) CREATE de sp_agendar_cita con las tres validaciones (4 min). 2) CALL con la "
                    "mascota 1: cita creada; con la 3 y con la 99: lee cada mensaje en voz alta "
                    "(3 min). 3) La batería: cuatro bloques DO y SELECT * FROM resultado_prueba "
                    "ORDER BY id_prueba (5 min). 4) SELECT COUNT(*) FROM cita: de 10 a 11; y "
                    "pg_get_functiondef para mostrar que quedó guardado (3 min).",
                ],
                "cuidado": "Recrea los datos antes de la demo si ya hiciste pruebas: el conteo de "
                           "10 a 11 solo vale sobre la base recién sembrada.",
                "puente": "Cierre de la clase.",
            },
        },
        "Clase 3 ·": {
            "notas": {
                "min": 3,
                "explica": "Cierre: la regla «una mascota inactiva no agenda» ya no depende de que "
                           "cada pantalla se acuerde. Vive en la base, aborta cuando no se cumple, "
                           "está probada y tiene un contrato que cualquiera puede leer.",
                "pasos": [
                    "Pregunta de salida: «¿por qué no basta con que el CREATE PROCEDURE no dé "
                    "error?». Respuesta esperada: porque los nombres se revisan al ejecutar; la "
                    "evidencia es el CALL y la batería.",
                ],
                "puente": "La próxima clase: funciones, triggers y el plan para cuando algo salga "
                          "mal.",
            },
        },
    },
}
