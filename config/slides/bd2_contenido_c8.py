# -*- coding: utf-8 -*-
"""BD II Clase 8 · Tuning y transacciones: ideas proyectadas y GUION de cada lamina.

Formato y uso: `bd2_contenido_data.py` y `notas_guion.py` (se fusiona solo). Salidas y mensajes
verificados en PGlite (PostgreSQL 18 en Node) con el script de la clase: insumos 1..6 con stocks
12, 3, 40, 25, 8 y 60 y precios 22.000, 31.000, 9.500, 7.000, 1.200 y 900. El caso feliz factura
27.400; el CALL que falla deja las fotos en 1 | 3 | 40 | 3; la factura viable sale por 112.000
con id_factura 3 (el intento fallido consumio el 2 de la secuencia).

Los pasos de cada animacion estan en `config/animaciones/bd2/clase8/<huella>.js`.
"""

CONTENIDO = {
    8: {
        "Encuadre de hoy": {
            "notas": {
                "min": 4,
                "explica": "Las dos clases anteriores hicieron que las consultas leyeran menos. "
                           "Hoy el foco pasa a las escrituras: que una factura con sus líneas y "
                           "sus descuentos de stock quede completa o no quede, aunque algo falle "
                           "a mitad.",
                "pasos": [
                    "Pregunta de arranque: «si el sistema registra la factura, descuenta una "
                    "vacuna y se cae antes de la segunda línea, ¿qué queda en la base?». Deja que "
                    "respondan; casi siempre dirán «la mitad».",
                    ("Después", "Cierra: «hoy vamos a ver por qué no queda nada, y a demostrarlo "
                     "con una foto antes y una foto después»."),
                ],
                "puente": "Primero, qué es exactamente una transacción.",
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
        "Que es una transaccion": {
            "ideas": [
                "Una **transacción** agrupa varias sentencias que describen un solo hecho de "
                "negocio.",
                "Protege de la **falla**: no puede quedar aplicada a medias.",
                "Protege de las **otras sesiones**: nadie ve el estado intermedio.",
                "En PostgreSQL, sin **BEGIN**, cada sentencia es su propia transacción y se "
                "confirma sola.",
            ],
            "notas": {
                "min": 4,
                "explica": "Una transacción es un grupo de sentencias que el motor trata como una "
                           "sola: se aplican todas o ninguna. Facturar una consulta son varias "
                           "sentencias (la cabecera, las líneas y los descuentos de stock), pero "
                           "es un solo hecho de negocio, y por eso va en una sola transacción.",
                "pasos": [
                    "El bloque: BEGIN, el INSERT de la factura, el de su detalle, el UPDATE del "
                    "stock y COMMIT o ROLLBACK. Lee la etiqueta: un solo hecho de negocio.",
                    "Amenaza 1, la falla: si algo se cae a mitad, la transacción no puede quedar "
                    "aplicada a medias.",
                    "Amenaza 2, las otras sesiones: mientras la transacción trabaja, nadie más "
                    "debe ver el estado intermedio, por ejemplo una factura sin líneas.",
                    "Dónde empieza y termina: en PostgreSQL, sin BEGIN cada sentencia es su "
                    "propia transacción y se confirma sola; en Oracle la transacción empieza sola "
                    "con la primera sentencia que modifica datos y dura hasta el COMMIT o el "
                    "ROLLBACK.",
                ],
                "ejemplo": "Facturar la consulta 4 con tres insumos son cinco sentencias: la "
                           "cabecera, tres líneas con su descuento de stock y la actualización "
                           "del total. Si una falla, no debe quedar ninguna.",
                "preguntas": [
                    ("Si PostgreSQL confirma solo, ¿para qué sirve COMMIT?",
                     "Para agrupar varias sentencias en un único hecho: con BEGIN … COMMIT, "
                     "todas se confirman juntas o ninguna."),
                ],
                "cuidado": "No enseñes la regla de Oracle («la transacción empieza sola») como si "
                           "fuera la de PostgreSQL: aquí, sin BEGIN, cada sentencia ya quedó "
                           "confirmada.",
                "puente": "Las cuatro propiedades de una transacción, empezando por la "
                          "atomicidad.",
            },
        },
        "Atomicidad": {
            "ideas": [
                "La **atomicidad** asegura que la transacción se aplica completa o no se aplica.",
                "Sin ella, un corte a mitad deja una **factura a medias** y un stock descontado "
                "que nadie entregó.",
                "Con ella, si la sesión muere sin COMMIT el motor **deshace todo** por su cuenta.",
            ],
            "notas": {
                "min": 3,
                "explica": "Atómico quiere decir indivisible. Si la facturación tiene cuatro pasos "
                           "y el tercero falla, la base no debe guardar los dos primeros: o están "
                           "los cuatro o no está ninguno.",
                "pasos": [
                    "La línea de tiempo: INSERT de la factura, INSERT de la línea 1, UPDATE del "
                    "stock del insumo 1… y se cae la red antes de la línea 2.",
                    "Sin atomicidad: la factura queda, la línea 1 queda, el stock quedó "
                    "descontado y la línea 2 nunca llegó. Nadie recibe un error; el descuadre "
                    "aparece semanas después en el inventario.",
                    "Con atomicidad: la sesión murió sin COMMIT, así que el motor deshace todo. "
                    "Cero facturas, cero líneas, stock intacto. La recepcionista repite la "
                    "operación. Lee la conclusión.",
                ],
                "ejemplo": "Una factura que cobra dos productos con una sola línea registrada y "
                           "un insumo descontado que nadie entregó: eso es lo que evita la "
                           "atomicidad.",
                "preguntas": [
                    ("¿Qué pasa si me desconecto sin COMMIT?",
                     "Si la sesión muere de forma anormal, el motor deshace la transacción. "
                     "Algunos clientes confirman al cerrar de forma ordenada, así que nunca hay "
                     "que depender de eso."),
                ],
                "cuidado": "Atomicidad no garantiza que los datos sean válidos; solo que no "
                           "queden a medias. Eso es la lámina siguiente.",
                "puente": "Completa no quiere decir correcta: eso es la consistencia.",
            },
        },
        "Consistencia": {
            "ideas": [
                "La **consistencia** exige pasar de un estado válido a otro estado válido.",
                "Válido es lo que cumplen las **restricciones declaradas**: PK, FK, UNIQUE, NOT "
                "NULL, CHECK.",
                "La atomicidad **no** produce consistencia: sin CHECK, un stock de −7 se "
                "confirma sin quejarse.",
                "Con **CHECK (stock >= 0)** el mismo UPDATE se rechaza.",
            ],
            "notas": {
                "min": 3,
                "explica": "Consistencia quiere decir que después de la transacción la base "
                           "sigue cumpliendo sus reglas. Pero el motor solo conoce las reglas "
                           "que alguien declaró: si nadie escribió el CHECK, una transacción "
                           "perfectamente atómica puede guardar un absurdo.",
                "pasos": [
                    "Sin restricción: UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2 "
                    "sobre un stock de 3. El contador baja a −7 y el COMMIT pasa sin quejarse: "
                    "atómico, pero inválido.",
                    "Con CHECK (stock >= 0) en la tabla: el mismo UPDATE se rechaza y el stock "
                    "sigue en 3.",
                    "Lee la idea: la atomicidad NO produce consistencia. La regla se declara una "
                    "vez y vale para quien escriba SQL después.",
                ],
                "ejemplo": "Con el CHECK declarado, el motor responde: «new row for relation "
                           "\"insumo\" violates check constraint \"insumo_stock_check\"» y "
                           "en el detalle muestra la fila que habría quedado, con stock −7.",
                "preguntas": [
                    ("Si el procedimiento ya revisa el stock, ¿para qué el CHECK?",
                     "Porque el CHECK vale también para el UPDATE manual o para otro programa "
                     "que no use el procedimiento. El guardia del procedimiento evita llegar al "
                     "error; el CHECK es la red de seguridad."),
                    ("¿Y después del error puedo seguir en la misma transacción?",
                     "En PostgreSQL no: toda sentencia siguiente responde «current transaction "
                     "is aborted, commands ignored until end of transaction block» hasta el "
                     "ROLLBACK. Oracle, en cambio, solo aborta la sentencia que falló."),
                ],
                "cuidado": "El malentendido más caro del tema es creer que la transacción "
                           "garantiza las reglas de negocio. Solo garantiza las que están "
                           "declaradas.",
                "puente": "La tercera letra: qué pasa cuando dos transacciones se cruzan.",
            },
        },
        "Aislamiento": {
            "ideas": [
                "El **aislamiento** exige que dos transacciones a la vez den lo mismo que una tras "
                "otra.",
                "El fallo típico es la **actualización perdida**: las dos leen 3 y las dos "
                "escriben 0.",
                "Primera defensa: que el motor haga la resta en **una sola sentencia** con la "
                "condición.",
                "Segunda defensa: el **nivel de aislamiento**; en PostgreSQL, READ COMMITTED por "
                "omisión.",
            ],
            "notas": {
                "min": 3,
                "explica": "Aislamiento quiere decir que, aunque dos transacciones trabajen a la "
                           "vez, el resultado debe ser el mismo que si hubieran ido una detrás de "
                           "la otra. El fallo más fácil de contar es la actualización perdida.",
                "pasos": [
                    "Quedan 3 vacunas. Recepción 1 y recepción 2 facturan 3 cada una, al mismo "
                    "tiempo, y las dos leen stock = 3.",
                    "Las dos calculan 3 − 3 = 0 y las dos escriben 0. Cada una confirmó una "
                    "venta válida según lo que leyó.",
                    "El resultado: stock 0 con seis vacunas vendidas y tres entregadas de aire. "
                    "Lee la definición de aislamiento.",
                ],
                "ejemplo": "La defensa de diseño: UPDATE insumo SET stock = stock - 3 WHERE "
                           "id_insumo = 2 AND stock >= 3. La resta y la comprobación ocurren en "
                           "una sola sentencia, que bloquea la fila mientras se ejecuta: la "
                           "segunda recepción encuentra 0 y no descuenta.",
                "preguntas": [
                    ("¿Cuáles son los niveles de aislamiento?",
                     "El estándar define cuatro: READ UNCOMMITTED, READ COMMITTED, REPEATABLE "
                     "READ y SERIALIZABLE. PostgreSQL acepta los cuatro nombres, pero READ "
                     "UNCOMMITTED se comporta como READ COMMITTED, que es el valor por "
                     "omisión."),
                    ("¿Lo podemos ver hoy en el navegador?",
                     "No: ahí corre una sola sesión. Se documenta como una línea de tiempo de "
                     "dos transacciones y se estudia en la Clase 10."),
                ],
                "cuidado": "Hoy solo se nombran los niveles; los fenómenos (lectura sucia, no "
                           "repetible, fantasma, interbloqueo) son la Clase 10.",
                "puente": "La última letra: qué asegura que lo confirmado no se pierda.",
            },
        },
        "Durabilidad": {
            "ideas": [
                "La **durabilidad** asegura que lo confirmado sobrevive aunque el servidor se apague.",
                "El motor escribe primero en el **WAL**, un registro secuencial, y después en "
                "las páginas.",
                "El **COMMIT** solo espera que su registro quede grabado: unos cientos de bytes.",
                "Tras una caída, el motor **relee el WAL**: rehace lo confirmado y descarta lo "
                "demás.",
            ],
            "notas": {
                "min": 2,
                "explica": "Durable quiere decir que, una vez que el motor dijo «confirmado», el "
                           "dato no se pierde aunque se caiga el servidor. Lo logra con un "
                           "registro de transacciones (WAL en PostgreSQL, redo log en Oracle) "
                           "donde anota cada cambio antes de tocar las páginas de datos.",
                "pasos": [
                    "El cambio va primero al WAL, un archivo que solo se escribe al final, de "
                    "corrido. El COMMIT termina cuando su registro (el verde) quedó grabado.",
                    "Las páginas de datos se escriben después, sin prisa: el COMMIT no las "
                    "esperó.",
                    "Se cae el servidor. Al volver, el motor relee el WAL: aplica lo confirmado "
                    "y descarta lo que quedó sin confirmar.",
                    "La consecuencia práctica: confirmar fila por fila en una carga de 100.000 "
                    "filas puede ser de 5 a 20 veces más lento que agrupar. Es orden de "
                    "magnitud: se mide en cada motor.",
                ],
                "ejemplo": "El ROLLBACK tampoco es magia: PostgreSQL conserva la versión "
                           "anterior de cada fila modificada y, al deshacer, se queda con ella.",
                "preguntas": [
                    ("¿Puedo hacer ROLLBACK después de un COMMIT?",
                     "No. Confirmar es definitivo; lo único que queda es restaurar desde un "
                     "respaldo (Clase 4)."),
                ],
                "cuidado": "En el navegador no se puede demostrar la durabilidad: nadie puede "
                           "apagar el servidor. Se explica, no se mide.",
                "puente": "Con ACID claro, el procedimiento que factura: su firma.",
            },
        },
        "La firma de sp_facturar": {
            "ideas": [
                "sp_facturar recibe **dos arreglos paralelos**: los insumos y sus cantidades, "
                "por posición.",
                "Primero valida que los arreglos midan lo mismo, con **IS DISTINCT FROM**.",
                "La **cabecera** entra con total 0 y RETURNING … INTO guarda el id generado.",
                "El **total** se calcula en el bucle: 22.000×1 + 900×2 + 1.200×3 = 27.400.",
            ],
            "notas": {
                "min": 3,
                "explica": "Una factura tiene varias líneas, así que el procedimiento no recibe "
                           "un insumo suelto: recibe dos arreglos emparejados por posición. El "
                           "insumo de la posición 1 va con la cantidad de la posición 1, y así "
                           "sucesivamente.",
                "pasos": [
                    "CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3]): consulta 4, una unidad "
                    "del insumo 1, dos del 6 y tres del 5. Las líneas punteadas emparejan cada "
                    "posición.",
                    "Lo primero del cuerpo: si los arreglos no miden lo mismo, RAISE EXCEPTION "
                    "antes de tocar la base. Se usa IS DISTINCT FROM porque con un arreglo "
                    "vacío array_length devuelve NULL, y con NULL el signo de distinto no da ni "
                    "verdadero ni falso.",
                    "La cabecera entra con total 0, porque todavía no se sabe, y RETURNING "
                    "id_factura INTO v_id_factura evita otro SELECT. El total sale del bucle: "
                    "27.400.",
                ],
                "ejemplo": "CALL sp_facturar(4, ARRAY[1, 2], ARRAY[1]); se rechaza con «ERROR: "
                           "insumos y cantidades deben tener la misma longitud» y no deja nada "
                           "escrito.",
                "preguntas": [
                    ("¿Por qué INT y no NUMBER?",
                     "NUMBER es de Oracle y en PostgreSQL no existe: se usa INT para los ids y "
                     "NUMERIC para el dinero."),
                    ("¿Por qué $proc$ y no $$?",
                     "Cualquier etiqueta entre signos de dólar sirve; una con nombre evita "
                     "choques si adentro hay otro bloque entre $$."),
                ],
                "cuidado": "Si se proyecta una firma con un solo insumo, la llamada con dos "
                           "arreglos no compila contra ella.",
                "puente": "El procedimiento en código.",
            },
        },
        "Todo o nada: la transaccion de facturacion": {
            "notas": {
                "min": 2,
                "explica": "Una versión corta de sp_facturar para ver el esqueleto: cabecera, "
                           "bucle con el descuento condicional, el total al final y ningún COMMIT "
                           "ni ROLLBACK adentro. La versión completa está en la lámina siguiente.",
                "pasos": [
                    ("Al entrar", "Líneas 1-4: la firma con los dos arreglos, LANGUAGE plpgsql y "
                     "las variables v_id_factura y v_filas."),
                    ("Líneas 5-6", "La cabecera con RETURNING id_factura INTO v_id_factura."),
                    ("Líneas 7-11", "El bucle: el UPDATE con stock >= p_cantidades[i] en el "
                     "WHERE, GET DIAGNOSTICS para saber cuántas filas tocó y RAISE EXCEPTION si "
                     "fueron 0."),
                    ("Líneas 12-15", "La línea de detalle con el precio leído de insumo, y el "
                     "comentario clave de la línea 15: sin COMMIT ni ROLLBACK."),
                    ("Líneas 16-18", "Al salir del bucle, el total de la cabecera es la suma de "
                     "sus líneas: cantidad por precio."),
                ],
                "ejemplo": "Con el caso feliz, CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, "
                           "3]) inserta tres líneas a 22.000, 900 y 1.200 y deja la factura con "
                           "total 27.400,00. Con ARRAY[3, 2] y ARRAY[2, 10] responde «ERROR: stock "
                           "insuficiente» y no queda nada: ni cabecera ni el descuento del "
                           "insumo 3.",
                "cuidado": "No la presentes como la versión final: le faltan la validación de "
                           "los arreglos y el NOT FOUND del insumo, y su mensaje de error no dice "
                           "qué insumo faltó.",
                "puente": "La versión completa, parte por parte.",
            },
        },
        "sp_facturar en PL/pgSQL": {
            "ideas": [
                "El cuerpo tiene cuatro partes: validar arreglos, **cabecera**, bucle y total.",
                "En el bucle se lee el **precio vigente** y NOT FOUND detecta el insumo que no "
                "existe.",
                "El **guardia** descuenta solo si alcanza; GET DIAGNOSTICS dice si tocó la fila.",
                "Al salir del bucle se escribe el **total**: 27.400 en el caso de prueba.",
            ],
            "notas": {
                "min": 2,
                "explica": "La versión completa del procedimiento, recorrida de arriba abajo. "
                           "Cada parte tiene una razón: rechazar una llamada mal hecha, registrar "
                           "la cabecera, cobrar línea por línea con el precio vigente y dejar el "
                           "total correcto.",
                "pasos": [
                    ("Al entrar", "La llamada de prueba arriba y la parte 1: validar que los "
                     "arreglos midan lo mismo."),
                    ("Parte 2 y 3", "La cabecera con total 0 y el bucle: SELECT precio_unit INTO "
                     "v_precio con IF NOT FOUND; el UPDATE con el guardia; GET DIAGNOSTICS; "
                     "RAISE si fue 0; INSERT de la línea; v_total := v_total + v_precio * "
                     "cantidad (el := es la asignación de PL/pgSQL)."),
                    ("Parte 4 y abajo", "UPDATE factura SET total = v_total. Resultado: 27.400, y "
                     "los stocks de los insumos 1, 6 y 5 pasan de 12, 60 y 8 a 11, 58 y 5."),
                ],
                "ejemplo": "CALL sp_facturar(4, ARRAY[99], ARRAY[1]); responde «ERROR: el insumo "
                           "99 no existe»: sin el NOT FOUND, v_precio quedaría NULL y la factura "
                           "terminaría con total NULL.",
                "preguntas": [
                    ("¿Por qué el precio se lee de la tabla y no se recibe como parámetro?",
                     "Porque se cobra el precio vigente, no el que la aplicación crea "
                     "recordar."),
                    ("¿Por qué el mensaje sale como «ERROR: ERROR: …»?",
                     "Porque el texto del RAISE ya empieza con «ERROR:» y el motor antepone el "
                     "suyo. Es solo el texto; no son dos errores."),
                ],
                "cuidado": "El error de sintaxis más común es cerrar el cuerpo con una etiqueta "
                           "distinta de la que lo abrió: $proc$ al principio y $proc$ al final.",
                "puente": "El corazón del procedimiento: el guardia del stock.",
            },
        },
        "El guardia del stock": {
            "ideas": [
                "El **guardia** pone la condición dentro del WHERE: AND stock >= cantidad.",
                "Comprobar y descontar son **una sola sentencia**: nadie se cuela entre las dos.",
                "Luego **GET DIAGNOSTICS** guarda cuántas filas tocó: 1 alcanzó, 0 no había stock.",
                "Si fue 0, **RAISE EXCEPTION** con el insumo y la cantidad pedida.",
            ],
            "notas": {
                "min": 3,
                "explica": "El descuento de stock no se hace en dos pasos (leer y luego "
                           "escribir) sino en uno: el UPDATE solo toca la fila si alcanza. "
                           "Después, ROW_COUNT dice si la tocó. Ese cero no es un error del "
                           "motor: es la señal de que no había stock, y el procedimiento la "
                           "convierte en excepción.",
                "pasos": [
                    "Las cuatro sentencias dentro del bucle, numeradas, con la condición del "
                    "WHERE resaltada: comprobar y escribir en una sola sentencia.",
                    "Caso que alcanza: insumo 3, hay 40 y se piden 2. ROW_COUNT = 1, el stock "
                    "pasa a 38 y el bucle sigue.",
                    "Caso que no alcanza: insumo 2, hay 3 y se piden 10. ROW_COUNT = 0, el stock "
                    "queda intacto y se lanza la excepción. Lee la nota: el precio se lee de la "
                    "tabla.",
                ],
                "ejemplo": "El mensaje real: «ERROR: stock insuficiente del insumo 2 (se "
                           "pidieron 10)». Cada % del RAISE se reemplaza por los argumentos, en "
                           "orden.",
                "preguntas": [
                    ("¿Por qué no SQL%ROWCOUNT?",
                     "Es de Oracle. En PL/pgSQL se pregunta con GET DIAGNOSTICS v_filas = "
                     "ROW_COUNT, y esa diferencia decide si el código compila."),
                ],
                "cuidado": "Si alguien escribe stock > cantidad en vez de >=, pedir exactamente "
                           "lo que queda falla: el caso límite lo delata.",
                "puente": "Ese cero filas no es un error para el motor: hay dos clases de error.",
            },
        },
        "Error del motor y error de negocio": {
            "ideas": [
                "Un **error del motor** viola una regla que la base conoce: CHECK, FK, tipo, "
                "interbloqueo.",
                "Un **error de negocio** viola una regla que la base no conoce en esa forma.",
                "Un UPDATE que toca **0 filas** es un éxito para el motor: el RAISE lo pones tú.",
                "Nada de **WHEN OTHERS THEN NULL**: si se captura, se relanza con RAISE.",
            ],
            "notas": {
                "min": 3,
                "explica": "Hay dos clases de fallo a mitad de transacción. El motor detecta solo "
                           "lo que viola sus reglas declaradas y aborta por su cuenta. Lo que solo "
                           "es una regla de negocio, como «no hay stock suficiente», el motor no "
                           "lo ve: hay que convertirlo en excepción.",
                "pasos": [
                    "Error del motor: CHECK, clave foránea, tipo incompatible, interbloqueo. El "
                    "motor lanza y aborta solo.",
                    "Error de negocio: stock insuficiente, mascota inactiva, un total que no "
                    "cuadra. Un UPDATE que no toca filas es una sentencia exitosa: el RAISE "
                    "EXCEPTION lo pones tú.",
                    "Nada de capturar y silenciar: EXCEPTION WHEN OTHERS THEN NULL convierte el "
                    "fallo en silencio. Si se captura, se relanza con RAISE a secas.",
                ],
                "ejemplo": "Un UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2 AND "
                           "stock >= 10 devuelve «0 filas afectadas», sin error. Solo el "
                           "procedimiento sabe que eso significa «no hay stock».",
                "preguntas": [
                    ("¿Y si quiero cobrar las demás líneas aunque una falle?",
                     "Existe el SAVEPOINT: deshacer solo esa línea y seguir. Hoy la regla es "
                     "todo o nada, pero conviene saber que la opción existe."),
                ],
                "cuidado": "El mensaje debe nombrar el insumo concreto: quien lea el error tiene "
                           "que poder decir qué línea falló.",
                "puente": "Cuando la excepción sale del procedimiento, ¿qué se deshace y quién lo "
                          "hace?",
            },
        },
        "Donde empieza y termina la transaccion": {
            "ideas": [
                "Un **CALL** escrito sin BEGIN es su propia transacción.",
                "Si la excepción **sale del CALL**, el motor deshace todo lo que ese CALL hizo.",
                "Nadie escribió **ROLLBACK**: el stock del insumo 3 vuelve a 40 solo.",
                "Quien decide el **COMMIT** es uno solo: el llamador.",
            ],
            "notas": {
                "min": 3,
                "explica": "Un CALL escrito por fuera de cualquier BEGIN es una transacción "
                           "completa. Si dentro del procedimiento salta una excepción y nadie la "
                           "atrapa, sale del CALL y el motor deshace todo lo que ese CALL había "
                           "hecho: cabecera, líneas y descuentos.",
                "pasos": [
                    "CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 10]) dentro de su recuadro: una "
                    "sola transacción. Se inserta la cabecera y el insumo 3 baja de 40 a 38: "
                    "alcanzaba.",
                    "El insumo 2 tiene 3 y se piden 10: RAISE EXCEPTION, y la excepción sale del "
                    "CALL.",
                    "El motor deshace todo: no queda factura y el insumo 3 vuelve a 40 solo. Lee "
                    "la conclusión: confirma el llamador.",
                ],
                "ejemplo": "Fotos reales: antes del CALL, 1 factura, 3 líneas, stock_3 = 40 y "
                           "stock_2 = 3; después, exactamente lo mismo. La siguiente factura "
                           "que sí se crea sale con id_factura 3, no 2: el intento fallido "
                           "consumió el 2 de la secuencia, y las secuencias no se deshacen.",
                "preguntas": [
                    ("¿Por qué el id saltó del 1 al 3?",
                     "Porque nextval de una secuencia no se deshace con el ROLLBACK, para que "
                     "dos sesiones nunca reciban el mismo número. Los huecos son normales."),
                ],
                "cuidado": "No digas que la reversión «no se puede demostrar en el navegador»: "
                           "se demuestra con una foto antes y una después del CALL que falla.",
                "puente": "Y cuando sí se quiere agrupar a mano: la transacción explícita.",
            },
        },
        "Todo o nada: la transaccion explicita": {
            "notas": {
                "min": 2,
                "explica": "La misma idea sin procedimiento: BEGIN abre la transacción, las "
                           "sentencias se acumulan y COMMIT las confirma juntas. Hasta el "
                           "COMMIT, nadie más ve los cambios.",
                "pasos": [
                    ("Al entrar", "Línea 1: BEGIN. Líneas 3-4: la cabecera con RETURNING, que "
                     "muestra el id generado."),
                    ("Líneas 6-11", "La línea de detalle (2 gasas a 1.200), el descuento de "
                     "stock y el total de la cabecera, 2.400. currval devuelve el id que esta "
                     "misma sesión acaba de generar."),
                    ("Línea 13", "COMMIT: las cuatro sentencias quedan juntas. Con ROLLBACK, o "
                     "si cualquiera falla, no queda ninguna."),
                ],
                "ejemplo": "Con los datos de la clase, después del COMMIT la factura queda con "
                           "total 2.400,00 y la gasa estéril baja de 8 a 6.",
                "preguntas": [
                    ("¿currval puede devolver el id de otra persona?",
                     "No: currval es por sesión; devuelve el último valor que generó ESTA "
                     "sesión."),
                ],
                "cuidado": "Entre el BEGIN y el COMMIT no se espera a nadie: una transacción "
                           "abierta sostiene bloqueos.",
                "puente": "¿Y si eso mismo se pone dentro del procedimiento?",
            },
        },
        "Por que el procedimiento no lleva COMMIT": {
            "ideas": [
                "Llamado con un **CALL suelto**, el procedimiento ya es una transacción "
                "completa.",
                "La **excepción** que sale del CALL lo deshace todo sin escribir ROLLBACK.",
                "Dentro de un BEGIN, un COMMIT en el procedimiento da **invalid transaction "
                "termination**.",
                "Quien confirma es **el llamador**; si se captura el error, se relanza.",
            ],
            "notas": {
                "min": 2,
                "explica": "El procedimiento no decide cuándo confirmar: lo decide quien lo "
                           "llama. Llamado con un CALL suelto, el CALL es la transacción y la "
                           "excepción la deshace. Llamado dentro de una transacción abierta, "
                           "intentar confirmar desde adentro es un error.",
                "pasos": [
                    ("Al entrar", "Arriba, el CALL suelto: es su propia transacción; la "
                     "excepción que sale deshace cabecera, líneas y stock, y nadie escribió "
                     "ROLLBACK."),
                    ("En el medio", "El CALL dentro de BEGIN … COMMIT: el que decide es ese "
                     "COMMIT de afuera. Si el procedimiento intenta un COMMIT propio, el motor "
                     "responde «invalid transaction termination»; lo mismo dentro de un bloque "
                     "con EXCEPTION."),
                    ("Abajo", "La regla: confirma uno solo, el llamador. Y si se atrapa el error, "
                     "se relanza con RAISE; nunca WHEN OTHERS THEN NULL."),
                ],
                "ejemplo": "Prueba real con un CALL suelto: un procedimiento que descuenta el "
                           "insumo 3, hace COMMIT, descuenta el insumo 4 y después falla deja el "
                           "3 descontado (40 → 39) y el 4 intacto: justo la factura a medias que "
                           "se quería evitar. Y con BEGIN; CALL …; el COMMIT de adentro responde "
                           "«invalid transaction termination».",
                "preguntas": [
                    ("Entonces, ¿nunca se escribe COMMIT en un procedimiento de PostgreSQL?",
                     "Se puede en procesos por lotes y solo si el CALL es de nivel superior. "
                     "En un procedimiento de negocio como este es un defecto: le quita al "
                     "llamador la posibilidad de deshacer."),
                ],
                "cuidado": "No afirmes que PostgreSQL prohíbe siempre el ROLLBACK dentro de un "
                           "procedimiento: con un CALL suelto lo permite. Lo que no permite es "
                           "terminar la transacción desde adentro cuando el CALL está dentro de "
                           "otra o de un bloque con EXCEPTION.",
                "puente": "El otro mecanismo que deshace sin que nadie lo escriba: el savepoint "
                          "implícito.",
            },
        },
        "El savepoint implicito": {
            "ideas": [
                "Un bloque **BEGIN … EXCEPTION … END** crea un savepoint al entrar.",
                "Si algo falla adentro, se deshace **solo lo del bloque** y corre el manejador.",
                "Lo escrito **antes del bloque** sigue en pie hasta que termine la transacción.",
                "Cada vuelta de un bucle con EXCEPTION crea un savepoint: **se paga**.",
            ],
            "notas": {
                "min": 3,
                "explica": "En PL/pgSQL, un bloque que tiene sección EXCEPTION marca un punto de "
                           "retorno al entrar. Si algo falla adentro, el motor vuelve a ese punto "
                           "(deshace lo del bloque) y ejecuta el manejador. Lo que se escribió "
                           "antes del bloque no se toca.",
                "pasos": [
                    "La transacción: la escritura A, y luego el bloque BEGIN … EXCEPTION con su "
                    "bandera (el savepoint implícito) y la escritura B adentro.",
                    "Algo falla dentro del bloque: se vuelve al savepoint, B se deshace y corre "
                    "el manejador. A se conserva.",
                    "La lección: capturar no es lo mismo que dejar propagar. Y el costo: dentro "
                    "de un bucle, un savepoint por vuelta; manejadores solo donde hay una "
                    "decisión que tomar.",
                ],
                "ejemplo": "DO $$ BEGIN CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 10]); "
                           "EXCEPTION WHEN OTHERS THEN RAISE NOTICE 'Fallo esperado: %', "
                           "SQLERRM; END $$; imprime «Fallo esperado: ERROR: stock insuficiente "
                           "del insumo 2 (se pidieron 10)» y la base queda igual: el savepoint "
                           "deshizo lo del CALL.",
                "preguntas": [
                    ("¿Qué es SQLERRM?",
                     "La variable con el texto del error que se atrapó. Sirve para que el aviso "
                     "diga algo útil en vez de «falló»."),
                ],
                "cuidado": "Ese DO con manejador es para que un script siga corriendo y se pueda "
                           "medir, no para arreglar el error.",
                "puente": "El savepoint también se puede escribir a mano.",
            },
        },
        "SAVEPOINT: deshacer una parte": {
            "notas": {
                "min": 2,
                "explica": "Un SAVEPOINT es una marca con nombre dentro de la transacción. ROLLBACK "
                           "TO SAVEPOINT vuelve a esa marca sin deshacer lo anterior, y la "
                           "transacción sigue viva.",
                "pasos": [
                    ("Al entrar", "Líneas 1-3: BEGIN, la cabecera y la marca antes_del_detalle."),
                    ("Líneas 4-7", "Una línea con el insumo 9999, que no existe: la clave foránea "
                     "la rechaza con el error de las líneas 6 y 7."),
                    ("Líneas 8-11", "ROLLBACK TO SAVEPOINT: la cabecera sigue viva. Se inserta la "
                     "línea correcta (insumo 5) y COMMIT."),
                ],
                "ejemplo": "Resultado: la factura con una línea de 1 gasa. Sin el ROLLBACK TO "
                           "SAVEPOINT, cualquier sentencia después del error respondería «current "
                           "transaction is aborted».",
                "preguntas": [
                    ("¿Cuándo usaría esto en la clínica?",
                     "En una factura de varias líneas donde se acepta cobrar las que sí "
                     "alcanzan y avisar de la que no. Hoy la regla es todo o nada, así que no "
                     "se usa."),
                ],
                "cuidado": "En esta versión la cabecera queda con total 0: el ejemplo muestra el "
                           "SAVEPOINT, no el cálculo del total.",
                "puente": "Y la trampa de atrapar el error sin relanzarlo.",
            },
        },
        "El bloque EXCEPTION y la trampa": {
            "notas": {
                "min": 2,
                "explica": "Un bloque que atrapa el error y solo avisa deshace su parte, pero "
                           "deja confirmado lo que estaba antes. El resultado puede ser una "
                           "factura sin líneas que nadie notó.",
                "pasos": [
                    ("Al entrar", "Líneas 1-3: el DO y la cabecera, fuera del bloque interno."),
                    ("Líneas 4-10", "El bloque con EXCEPTION: descuenta una gasa e inserta una "
                     "línea con un insumo que no existe. El manejador solo imprime un aviso: es "
                     "la trampa."),
                    ("Líneas 12-15", "El efecto: el bloque se deshizo (el stock quedó igual), "
                     "pero el DO terminó bien y la cabecera quedó guardada sin líneas. La "
                     "corrección: EXCEPTION WHEN OTHERS THEN RAISE;"),
                ],
                "ejemplo": "Prueba real: el aviso dice «algo fallo: insert or update on table "
                           "\"detalle_factura\" violates foreign key constraint …», queda una "
                           "factura con 0 líneas y la gasa conserva su stock. Con RAISE en el "
                           "manejador, el DO falla y no queda ninguna factura nueva.",
                "cuidado": "El síntoma de esta trampa no es un error: es una factura con total 0 "
                           "y sin líneas que aparece días después.",
                "puente": "Por qué todo esto se escribe distinto en Oracle.",
            },
        },
        "El contraste con Oracle": {
            "ideas": [
                "La misma lógica cambia de sintaxis: **NUMBER**, SQL%ROWCOUNT y "
                "RAISE_APPLICATION_ERROR son de Oracle.",
                "En PostgreSQL: **INT y NUMERIC**, GET DIAGNOSTICS y RAISE EXCEPTION.",
                "En Oracle suele escribirse **ROLLBACK** en el manejador; aquí lo deshace la "
                "excepción del CALL.",
                "La base quedó intacta porque el **CALL** es su propia transacción.",
            ],
            "notas": {
                "min": 2,
                "explica": "Oracle sigue siendo un motor importante y por eso se compara, pero "
                           "el motor del curso es PostgreSQL. La misma lógica de facturación "
                           "necesita cuatro cambios de sintaxis para pasar de un motor al otro, y "
                           "además cambia quién confirma.",
                "pasos": [
                    ("Al entrar", "Recorre fila por fila: tipos, filas afectadas, cómo se aborta, "
                     "qué se hace al fallar y quién confirma."),
                    ("Abajo", "La respuesta a «¿por qué la base quedó intacta?»: el CALL es su "
                     "propia transacción y la excepción propagada la deshace entera. Ningún "
                     "ROLLBACK escrito lo hizo."),
                ],
                "ejemplo": "En Oracle: EXCEPTION WHEN OTHERS THEN ROLLBACK; RAISE;. En "
                           "PostgreSQL ese bloque no hace falta: sin manejador, la excepción sale "
                           "del CALL y deshace todo.",
                "preguntas": [
                    ("¿PostgreSQL guarda una copia de cada tabla antes del CALL?",
                     "No. Conserva la versión anterior de cada fila que cambia (MVCC) y, al "
                     "deshacer, se queda con ella."),
                    ("¿Los UPDATE se acumulan en memoria y se escriben al final?",
                     "No. Cada sentencia se aplica cuando se ejecuta y se ve dentro de la "
                     "misma transacción; lo que se decide al final es confirmarla o no."),
                ],
                "cuidado": "Enseñar la forma de Oracle como si fuera la del curso es el error que "
                           "más cuesta: no compila en PostgreSQL.",
                "puente": "La misma regla de stock con otro contrato: informar en vez de "
                          "abortar.",
            },
        },
        "Abortar o informar": {
            "ideas": [
                "La misma regla de stock admite **dos contratos**: abortar o informar.",
                "sp_facturar **aborta**: si una línea no alcanza, se deshace toda la factura.",
                "fn_descontar_stock **informa**: devuelve false y el llamador decide qué hacer.",
                "Una cantidad cero o negativa sí es un **error**: es una llamada mal hecha.",
            ],
            "notas": {
                "min": 3,
                "explica": "Hay dos maneras de responder «no hay stock». El procedimiento lo "
                           "trata como un fallo y aborta todo. La función lo trata como un "
                           "resultado: devuelve verdadero o falso y deja que quien la llama "
                           "decida si sigue con las demás líneas.",
                "pasos": [
                    "La misma regla arriba (el UPDATE con el guardia) y el primer contrato: "
                    "sp_facturar, 0 filas → RAISE EXCEPTION, se deshace toda la factura.",
                    "El segundo contrato: fn_descontar_stock RETURNS BOOLEAN, RETURN v_filas = 1. "
                    "Si no alcanza devuelve false, sin excepción.",
                    "Cuatro llamadas reales: (5, 3) → true, hay 8 y quedan 5; (2, 10) → false, "
                    "hay 3; (2, 3) → true, pide justo lo que queda; (5, 0) → error, porque una "
                    "cantidad no positiva es una llamada mal hecha.",
                ],
                "ejemplo": "fn_descontar_stock(5, 0) responde «ERROR: la cantidad debe ser "
                           "positiva (llego 0)». El false se reserva para «no alcanza».",
                "preguntas": [
                    ("¿Por qué devolver false si también es un fallo?",
                     "Porque para quien llama es un resultado: puede decidir seguir con otras "
                     "líneas o cancelar. Si la función lanzara la excepción, esa decisión ya "
                     "no se podría tomar."),
                ],
                "cuidado": "El caso límite (2, 3) es el que delata un guardia escrito con > en "
                           "vez de >=: devolvería false.",
                "puente": "La función completa y su prueba en una sola consulta.",
            },
        },
        "fn_descontar_stock: cuando": {
            "ideas": [
                "La firma dice **RETURNS BOOLEAN**: true si descontó, false si no alcanzó.",
                "Tres partes: validar la cantidad, el mismo **guardia** y RETURN v_filas = 1.",
                "Se prueba en **una consulta**: true, false, true, y ningún stock negativo.",
                "Leer primero y decidir después deja una **ventana** entre lectura y escritura.",
            ],
            "notas": {
                "min": 2,
                "explica": "La función tiene tres partes cortas y se prueba en una sola consulta "
                           "con tres casos. Lo que la hace segura es lo mismo que en el "
                           "procedimiento: la condición viaja dentro del UPDATE.",
                "pasos": [
                    ("Al entrar", "La firma y las tres partes: p_cantidad <= 0 → RAISE; el "
                     "UPDATE con el guardia; GET DIAGNOSTICS y RETURN v_filas = 1, que devuelve "
                     "directamente el resultado de la comparación."),
                    ("En el medio", "La prueba con stocks 8 y 3: SELECT fn_descontar_stock(5, 3) "
                     "AS caso_ok, fn_descontar_stock(2, 10) AS caso_sin_stock, "
                     "fn_descontar_stock(2, 3) AS caso_limite; → true | false | true. Después: "
                     "insumo 5 en 5 e insumo 2 en 0."),
                    ("Abajo", "La ventana: si se lee el stock y luego se decide, dos recepciones "
                     "pueden leer 3 a la vez y las dos descontar. Con la condición en el WHERE "
                     "no hay ventana."),
                ],
                "ejemplo": "Antes de la prueba se reinician los stocks (insumo 5 en 8 e insumo 2 "
                           "en 3); si no, los valores esperados no salen.",
                "preguntas": [
                    ("¿Puedo probar la ventana con dos pestañas del navegador?",
                     "No: cada pestaña levanta su propia base en memoria y no comparten nada. "
                     "Se documenta en papel y se estudia en la Clase 10."),
                ],
                "cuidado": "Distinguir el dato inválido (cantidad cero o negativa, excepción) "
                           "del resultado negativo (no alcanza, false) es la mitad del tema.",
                "puente": "Tuning: hábitos de escritura que evitan problemas.",
            },
        },
        "Tuning": {
            "ideas": [
                "Una transacción de negocio debe ser **corta**: milisegundos, no minutos.",
                "Nunca se espera a una **persona** con la transacción abierta.",
                "En cargas masivas, **COMMIT por lotes**: ni uno por fila ni uno gigante.",
                "Filtrar por la **clave primaria** bloquea una sola fila.",
            ],
            "notas": {
                "min": 3,
                "explica": "Aquí tuning no es mover parámetros del servidor, que en el navegador "
                           "no se puede y sin medición es peligroso. Son hábitos de escritura con "
                           "números: transacciones cortas, lotes razonables y filtros que tocan "
                           "pocas filas.",
                "pasos": [
                    "Bien: leer y validar primero, sin transacción, y abrir BEGIN … COMMIT solo "
                    "para escribir. Dura milisegundos.",
                    "Mal: abrir la transacción, mostrar un «¿confirmar?» y que la recepcionista "
                    "se vaya a almorzar. Esas filas quedan bloqueadas para el resto de la "
                    "clínica mientras nadie vuelve.",
                    "Cargas masivas: COMMIT por lotes, del orden de 1.000 a 5.000 filas como "
                    "convención de oficio. Ni uno por fila, que es lentísimo, ni uno solo para "
                    "un millón.",
                ],
                "ejemplo": "UPDATE insumo SET stock = stock - 2 WHERE id_insumo = 3 filtra por "
                           "la clave primaria y bloquea una sola fila; el mismo UPDATE filtrando "
                           "por una columna sin índice tiene que recorrer la tabla para "
                           "encontrar las filas.",
                "preguntas": [
                    ("¿Cuánto es «corta»?",
                     "Del orden de milisegundos a unos cientos de milisegundos. Cualquier cosa "
                     "que sostenga bloqueos durante segundos es sospechosa."),
                ],
                "cuidado": "No prometas cifras exactas de mejora: los tamaños de lote y los "
                           "tiempos se miden en cada motor.",
                "puente": "Vamos a la demo, en el orden en que se proyecta.",
            },
        },
        "La demo, en el orden": {
            "ideas": [
                "Bloques 0 y 1: el esquema con **seis insumos** y el procedimiento.",
                "Bloque 2: el caso que funciona, **27.400**.",
                "Bloque 3: **foto · CALL que falla · foto**, con los mismos números.",
                "Bloque 4: la **función**, que devuelve true, false y true.",
            ],
            "notas": {
                "min": 1,
                "explica": "El script tiene cinco bloques y el valor está en el tercero: hay que "
                           "administrar el tiempo para llegar ahí con calma.",
                "pasos": [
                    ("Al entrar", "Bloques 0 a 2: el esquema (se puede correr dos veces porque "
                     "empieza con los DROP), el procedimiento leído en voz alta y el caso feliz, "
                     "27.400."),
                    ("Bloque 3", "Foto inicial (1 | 3 | 40 | 3), el CALL que falla dentro de un "
                     "DO con manejador y la foto final idéntica. Pregunta al grupo dónde quedó "
                     "el descuento del insumo 3. Cierra con la factura viable: 112.000, insumo 3 "
                     "en 38 e insumo 2 en 0."),
                ],
                "ejemplo": "La factura viable sale con id_factura 3: el intento fallido consumió "
                           "el 2 de la secuencia.",
                "cuidado": "Si el tiempo aprieta se recorta el bloque 4; nunca la pareja de fotos "
                           "del bloque 3.",
                "puente": "Qué se puede demostrar en el navegador y qué no.",
            },
        },
        "Donde corre esto": {
            "ideas": [
                "En el navegador corren el **CALL**, GET DIAGNOSTICS, RAISE y la función.",
                "La atomicidad se demuestra con **foto · CALL · foto** en el mismo panel.",
                "**Dos sesiones** a la vez y la durabilidad real no se pueden demostrar ahí.",
                "Lo que no corre se documenta como una **línea de tiempo** T1 / T2.",
            ],
            "notas": {
                "min": 1,
                "explica": "Todo el código de hoy es PL/pgSQL y corre en PostgreSQL dentro del "
                           "navegador. Como el CALL ya es su propia transacción, no hace falta "
                           "dejar una transacción abierta entre dos ejecuciones para demostrar "
                           "la atomicidad.",
                "pasos": [
                    ("Al entrar", "Izquierda, lo que corre: CALL, GET DIAGNOSTICS, RAISE, la "
                     "función BOOLEAN, las fotos y el DDL dentro de una transacción. Derecha, lo "
                     "que no: dos sesiones a la vez (espera por bloqueo, interbloqueo, "
                     "actualización perdida) y apagar el servidor. Eso se documenta en papel y "
                     "es la Clase 10."),
                ],
                "cuidado": "En PostgreSQL el DDL es transaccional: la vieja advertencia de que un "
                           "CREATE TABLE confirma solo (Oracle, MySQL) no aplica aquí; se menciona "
                           "como diferencia entre motores.",
                "puente": "Vamos a la demo.",
            },
        },
        "Demo del dia": {
            "ideas": [
                "La foto inicial: 1 factura, 3 líneas, **stock_3 = 40** y stock_2 = 3.",
                "El CALL que falla a mitad: el insumo 3 alcanza, el insumo 2 **no**.",
                "La foto final, idéntica: el descuento se deshizo **sin ROLLBACK escrito**.",
            ],
            "notas": {
                "min": 15,
                "explica": "La demo corre el script de la clase y demuestra la atomicidad con dos "
                           "fotos de la misma consulta, antes y después de un CALL que falla a "
                           "mitad.",
                "pasos": [
                    ("Al entrar", "1) Esquema y seis insumos. 2) El procedimiento, leyendo el "
                     "guardia y el GET DIAGNOSTICS. 3) CALL sp_facturar(4, ARRAY[1, 6, 5], "
                     "ARRAY[1, 2, 3]): 27.400 y stocks 11, 58 y 5."),
                    ("Después", "4) Foto inicial: 1 | 3 | 40 | 3. 5) El CALL con ARRAY[3, 2] y "
                     "ARRAY[2, 10] dentro de un DO con manejador: «Fallo esperado: ERROR: stock "
                     "insuficiente del insumo 2 (se pidieron 10)». 6) Foto final: 1 | 3 | 40 | "
                     "3. 7) Si hay tiempo, la función: true | false | true."),
                ],
                "ejemplo": "Después de las fotos, CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 3]) "
                           "crea la factura por 112.000 (9.500×2 + 31.000×3) y deja el insumo 3 "
                           "en 38 y el 2 en 0.",
                "cuidado": "Sin la foto inicial no hay demostración: hay que tomarla antes del "
                           "CALL que falla, con exactamente la misma consulta que la final.",
                "puente": "Cierre de la clase.",
            },
        },
        "Clase 8 ·": {
            "notas": {
                "min": 3,
                "explica": "Cierre: una transacción es un solo hecho de negocio; en PostgreSQL el "
                           "CALL ya la delimita, la excepción la deshace y confirma el llamador.",
                "pasos": [
                    "Pregunta de salida: «si el CALL falla en la tercera línea, ¿qué queda en la "
                    "base y por qué?». Respuesta esperada: nada; el CALL era la transacción y la "
                    "excepción la deshizo. Anuncia que la Clase 10 estudia qué pasa cuando dos "
                    "transacciones se cruzan.",
                ],
            },
        },
    },
}
