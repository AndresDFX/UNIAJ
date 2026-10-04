# -*- coding: utf-8 -*-
"""BD II · Clase 2 · Ideas proyectadas y GUION de cada lámina (notas del presentador).

Mismo formato que la Clase 4 en `bd2_contenido_data.py` (ver `notas_guion.py`); se fusiona solo.
Los pasos de cada animación salen de `config/animaciones/bd2/clase2/<huella>.js`.

Datos que se citan: los sembrados del curso (6 dueños con 5 columnas, 4 veterinarios, 8 mascotas,
10 citas, una de ellas CANCELADA). Las salidas y los mensajes de error de esta clase se
comprobaron en PostgreSQL (PGlite) con SET ROLE: permission denied for table cita, dependent
privileges exist, permission denied for sequence cita_id_cita_seq, 9 filas en la vista, 2 filas
en column_privileges.
"""

CONTENIDO = {
    2: {
        "Encuadre de hoy": {
            "notas": {
                "min": 4,
                "explica": "Ayer la base guardaba datos; hoy decidimos quién puede hacer qué con "
                           "ellos. Vamos a crear roles, darles solo los privilegios que su trabajo "
                           "necesita, recortar lo que ven con vistas y privilegios por columna, y "
                           "comprobar en el propio motor que un permiso que quitamos de verdad no "
                           "está.",
                "pasos": [
                    "Pregunta de arranque: «si la recepcionista y el veterinario entran con la "
                    "misma cuenta, ¿quién canceló la cita de ayer?». Deja que respondan 1-2 "
                    "personas: nadie lo puede saber.",
                    ("Cierre del encuadre", "«Hoy vamos a diseñar las cuentas de la clínica para "
                     "que esa pregunta siempre tenga respuesta»."),
                ],
                "cuidado": "Todo se hace en PostgreSQL. Si alguien trae sintaxis de Oracle (CREATE "
                           "USER ... IDENTIFIED BY, GRANT CREATE SESSION), avisa desde ya que aquí "
                           "no existe.",
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
                "puente": "Antes de la sintaxis, cuatro palabras que se confunden todo el tiempo.",
            },
        },
        "Los cuatro terminos": {
            "ideas": [
                "Un **objeto** es todo lo que el motor guarda con nombre: una tabla, una vista, un "
                "procedimiento, una secuencia.",
                "Un **esquema** es el contenedor de los objetos; en PostgreSQL el de omisión es "
                "public, como en public.cita.",
                "Un **privilegio** es un permiso atómico sobre un objeto, como SELECT sobre cita.",
                "Un **rol** es un paquete de privilegios con nombre, como recepcion.",
            ],
            "notas": {
                "min": 4,
                "explica": "Administrar una base de datos es decidir quién puede hacer qué sobre "
                           "cada objeto, y dejar rastro de quién lo hizo. Para hablar de eso sin "
                           "enredarse hacen falta cuatro palabras: objeto, esquema, privilegio y "
                           "rol.",
                "pasos": [
                    "Los objetos: cita (tabla), v_agenda (vista), sp_agendar (procedimiento), "
                    "seq_cita (secuencia). «Objeto es todo lo que el motor guarda con nombre».",
                    "Aparece el esquema public que los contiene: el nombre completo de la tabla es "
                    "public.cita.",
                    "El privilegio: SELECT sobre cita. «Es la unidad más pequeña de permiso, "
                    "siempre sobre un objeto concreto».",
                    "El rol recepcion, que agrupa privilegios. Lee la frase final: quién puede "
                    "hacer qué sobre cada objeto, y dejar rastro.",
                ],
                "ejemplo": "SELECT * FROM public.cita y SELECT * FROM cita son la misma consulta: "
                           "el motor busca primero en public.",
                "preguntas": [
                    ("¿Autenticación y autorización no son lo mismo?",
                     "No. Autenticación es probar quién eres (usuario y clave). Autorización es "
                     "decidir qué puedes hacer ya dentro. Alguien puede entrar perfectamente y no "
                     "tener permiso para leer una sola fila."),
                    ("En Oracle el esquema era el usuario, ¿aquí también?",
                     "No. En PostgreSQL esquema y usuario son cosas separadas: un esquema puede "
                     "tener objetos de varios dueños."),
                ],
                "cuidado": "No digas «creo un privilegio» ni «le doy el rol a la tabla»: los "
                           "privilegios ya vienen definidos por el motor; lo único que se crea son "
                           "roles, y los privilegios se otorgan o se retiran.",
                "puente": "Miremos de cerca el privilegio y la frontera que más importa: DDL "
                          "contra DML.",
            },
        },
        "Privilegio: la unidad atomica": {
            "ideas": [
                "Un **privilegio** es la unidad más pequeña de permiso que el motor sabe dar o "
                "quitar.",
                "Los **privilegios de objeto** (SELECT, INSERT, UPDATE, DELETE…) se dan con GRANT "
                "sobre una tabla.",
                "LOGIN o CREATEDB son **atributos de rol**: van en CREATE ROLE o ALTER ROLE, no en "
                "un GRANT.",
                "Quien opera datos usa **DML** (SELECT, INSERT, UPDATE, DELETE) y nunca necesita "
                "**DDL**.",
            ],
            "notas": {
                "min": 3,
                "explica": "Un privilegio es el permiso más pequeño que el motor otorga o quita. "
                           "En PostgreSQL hay que separar dos cosas: los privilegios sobre objetos, "
                           "que se dan con GRANT, y los atributos del rol, como LOGIN, que se "
                           "escriben al crearlo. Y una frontera práctica: DDL cambia la estructura, "
                           "DML lee o cambia datos.",
                "pasos": [
                    "Dos columnas. Izquierda, privilegios de objeto: SELECT, INSERT, UPDATE, "
                    "DELETE, TRUNCATE, REFERENCES, TRIGGER, que se otorgan con GRANT. Derecha, "
                    "atributos de rol: LOGIN, CREATEDB, CREATEROLE, SUPERUSER, que van en CREATE "
                    "ROLE o ALTER ROLE.",
                    "La frontera: DDL (CREATE, ALTER, DROP, TRUNCATE) cambia la estructura; DML "
                    "(SELECT, INSERT, UPDATE, DELETE) toca los datos. «Quien opera datos no "
                    "necesita DDL».",
                ],
                "ejemplo": "Si la cuenta de recepción pudiera ejecutar DROP TABLE cita, un error de "
                           "copiar y pegar borra la agenda completa, y ningún respaldo de anoche "
                           "devuelve las citas agendadas hoy.",
                "preguntas": [
                    ("¿Cómo le doy permiso de ALTER TABLE a alguien?",
                     "No existe como privilegio de GRANT: cambiar la estructura de una tabla lo "
                     "puede hacer su dueño. Por eso el DDL queda en admin_bd."),
                    ("Encontré GRANT CREATE SESSION en internet.",
                     "Es de Oracle. En PostgreSQL poder conectarse es el atributo LOGIN del rol."),
                ],
                "cuidado": "TRUNCATE aparece en las dos listas: es un privilegio de tabla que se da "
                           "con GRANT, y a la vez vacía la tabla entera; no se le da a ningún rol "
                           "operativo.",
                "puente": "Dar privilegios uno por uno a cada persona no escala. Para eso existe el "
                          "rol.",
            },
        },
        "Rol: por que existe": {
            "ideas": [
                "Un **rol** es un paquete de privilegios con nombre que se le da a una persona en "
                "un paso.",
                "Sin roles, 12 empleados y 10 objetos son **cientos de GRANT** escritos uno por "
                "uno.",
                "Con un rol, el paquete se define **una vez** y se otorga con 12 GRANT recepcion "
                "TO persona.",
                "Un cambio de regla es **un REVOKE** sobre el rol, y las 12 cuentas quedan "
                "corregidas a la vez.",
            ],
            "notas": {
                "min": 2,
                "explica": "Un rol existe por una razón aritmética. La clínica tiene diez objetos "
                           "que proteger y doce empleados; dar permisos cuenta por cuenta son "
                           "cientos de sentencias, y cuando cambia una regla hay que acordarse de "
                           "tocar las doce. Con un rol se define el paquete una vez y se corrige en "
                           "un solo lugar: el rol no ahorra tipeo, ahorra olvidos.",
                "pasos": [
                    "Cuenta por cuenta: doce personas, cada una con líneas hacia los diez objetos. "
                    "«Un cambio de regla obliga a tocar doce cuentas sin olvidar ninguna».",
                    "Con un rol: los mismos diez objetos, un solo rol recepcion, y doce GRANT "
                    "recepcion TO usuario.",
                    "El REVOKE sobre el rol corrige a los doce en el mismo instante.",
                ],
                "ejemplo": "Ocho tablas más dos procedimientos son diez objetos; con hasta cinco "
                           "acciones por objeto, la matriz tiene 50 celdas por decidir. Cuando "
                           "entra una recepcionista nueva, su alta es GRANT recepcion TO "
                           "nueva_persona; cuando se va, REVOKE recepcion FROM nueva_persona.",
                "preguntas": [
                    ("¿Un usuario puede tener dos roles?",
                     "Sí, y hereda la suma de los dos. Por eso al cambiar de función hay que "
                     "revocar el rol anterior."),
                ],
                "cuidado": "Los olvidos en permisos son los que producen incidentes: ese es el "
                           "argumento, no la comodidad.",
                "puente": "En PostgreSQL hay un detalle que lo cambia todo: usuario y rol son lo "
                          "mismo.",
            },
        },
        "En PostgreSQL usuario y rol": {
            "ideas": [
                "En PostgreSQL **usuario y rol son lo mismo**: CREATE USER es CREATE ROLE con "
                "LOGIN.",
                "El rol de un cargo se crea **NOLOGIN**: es un paquete de permisos con el que nadie "
                "se conecta.",
                "La persona es un rol con **LOGIN** que recibe el paquete: GRANT recepcion TO "
                "ana_gomez.",
                "Se escribe **veterinario_rol** para leer sin dudas que es un rol; el motor no lo "
                "exige.",
            ],
            "notas": {
                "min": 3,
                "explica": "En PostgreSQL no hay usuarios por un lado y roles por otro: todo es un "
                           "rol. Un rol con LOGIN puede conectarse y lo llamamos usuario; un rol "
                           "sin LOGIN es una bolsa de permisos. Por eso los roles de cargo se crean "
                           "NOLOGIN y la persona, con LOGIN, recibe la bolsa.",
                "pasos": [
                    "CREATE USER ana_gomez es lo mismo que CREATE ROLE ana_gomez LOGIN: un alias, "
                    "el mismo objeto.",
                    "Dos roles: recepcion NOLOGIN (nadie se conecta con él) y ana_gomez LOGIN (la "
                    "persona). La flecha es GRANT recepcion TO ana_gomez: ella hereda todo lo del "
                    "rol.",
                    "La convención: veterinario_rol y no veterinario, porque en GRANT SELECT ON "
                    "cita TO veterinario no se sabe a simple vista si es un rol o un error.",
                ],
                "ejemplo": "Si mañana recepción pierde un permiso, se hace un REVOKE sobre "
                           "recepcion y ana_gomez, junto con las demás recepcionistas, lo pierde en "
                           "el mismo instante.",
                "preguntas": [
                    ("¿Puede haber un rol y una tabla con el mismo nombre?",
                     "Sí: los roles son globales al servidor y las tablas viven en un esquema, así "
                     "que no chocan. El sufijo _rol es solo para leer mejor."),
                ],
                "cuidado": "Si el GRANT «no surte efecto», la causa más común es haberlo dado al "
                           "rol y no haber dado el rol a la persona (falta GRANT recepcion TO "
                           "ana_gomez).",
                "puente": "Así queda escrito, completo, para la recepción.",
            },
        },
        "Crear el rol y otorgar solo lo que el cargo usa": {
            "notas": {
                "min": 3,
                "explica": "El código de hoy en su forma más corta: el rol de cargo sin login, la "
                           "persona con login que lo recibe, y los privilegios exactos que necesita "
                           "la recepción para agendar.",
                "pasos": [
                    ("Líneas 1-2", "CREATE ROLE recepcion NOLOGIN: el paquete. Nace con cero "
                     "privilegios."),
                    ("Líneas 3-5", "La persona: CREATE ROLE ana_gomez LOGIN PASSWORD y GRANT "
                     "recepcion TO ana_gomez. La clave del ejemplo se cambia en producción."),
                    ("Líneas 7-9", "SELECT, INSERT y UPDATE sobre cita para agendar, reprogramar y "
                     "cancelar; solo SELECT sobre dueño, mascota y veterinario, en un único GRANT "
                     "con tres tablas."),
                    ("Líneas 10-11", "USAGE sobre la secuencia cita_id_cita_seq: el SERIAL de "
                     "id_cita la usa en cada INSERT."),
                ],
                "ejemplo": "Sin la línea 10, el INSERT de una cita hecho como recepcion falla con "
                           "«permission denied for sequence cita_id_cita_seq», aunque tenga INSERT "
                           "sobre la tabla.",
                "preguntas": [
                    ("¿Por qué recepción no tiene DELETE?",
                     "Porque cancelar no es borrar: es un UPDATE del estado a 'CANCELADA', y así "
                     "la historia se conserva."),
                    ("¿Y consulta?",
                     "Nada: es el historial clínico, información sensible que la recepción no "
                     "necesita para agendar."),
                ],
                "cuidado": "El error de la secuencia confunde porque el mensaje no menciona la "
                           "tabla cita: léelo en voz alta si aparece.",
                "puente": "Ese «lo que el cargo usa» tiene nombre: mínimo privilegio.",
            },
        },
        "Minimo privilegio aplicado": {
            "ideas": [
                "Con **mínimo privilegio** cada rol recibe exactamente lo que su trabajo necesita, "
                "y nada más.",
                "La **recepción** agenda (S, I, U sobre cita) y no lee consulta, que es historial "
                "clínico.",
                "El **veterinario** lee citas y mascotas y documenta la consulta; **admin_bd** "
                "sostiene el DDL.",
                "Ningún rol operativo tiene **DELETE**: cancelar es un UPDATE de estado y la baja "
                "es activa = 'N'.",
            ],
            "notas": {
                "min": 4,
                "explica": "El principio de mínimo privilegio dice que cada rol recibe exactamente "
                           "lo que necesita para su función y ni un privilegio más. Aplicado a la "
                           "clínica deja una matriz concreta y defendible, y una consecuencia "
                           "llamativa: nadie que opere datos tiene DELETE.",
                "pasos": [
                    "Fila de recepcion: S I U sobre cita, S sobre mascota y nada sobre consulta. "
                    "«No lee el historial clínico porque su trabajo no lo requiere».",
                    "Fila de veterinario_rol: S sobre cita y mascota, S I U sobre consulta, porque "
                    "es quien documenta la atención.",
                    "Fila de admin_bd: todo y además el DDL. Es el único con privilegios amplios.",
                    "La conclusión: ningún rol operativo tiene DELETE. En la clínica las cosas se "
                    "marcan: estado = 'CANCELADA', activa = 'N'.",
                ],
                "ejemplo": "El cuarto rol, auditor, recibe solo SELECT (sobre dueño, mascota, cita, "
                           "consulta y factura) y jamás una escritura.",
                "preguntas": [
                    ("¿No es más fácil darle todo al jefe?",
                     "El permiso no mide la confianza en la persona: mide cuánto se pierde si su "
                     "sesión es robada o comete un error. Con mínimo privilegio, un atacante con "
                     "la sesión de recepción ve agendas; con todo, borra la base."),
                ],
                "cuidado": "Escribe 'S' y 'N' en el tablero: quien asume activa = 0 escribe un "
                           "UPDATE que el CHECK rechaza.",
                "puente": "El contraste en una sola lámina: lo que suele pasar y lo que pide el "
                          "principio.",
            },
        },
        "Minimo privilegio, en concreto": {
            "notas": {
                "min": 1,
                "explica": "Antes y después: la forma habitual de dar permisos en una empresa "
                           "pequeña, y la que pide el mínimo privilegio.",
                "pasos": [
                    "Lee la columna izquierda como un diagnóstico: un admin compartido, GRANT ALL "
                    "«para que no falle», nadie sabe quién borró qué, cuentas vivas de gente que "
                    "ya se fue. Luego la derecha, punto por punto, como su remedio: cuatro roles, "
                    "matriz por objeto, cancelar con UPDATE, baja el mismo día.",
                ],
                "cuidado": "GRANT ALL a todos «para que la práctica no se trabe» deja una matriz "
                           "sin ninguna decisión que defender.",
                "puente": "Un paso más allá del mínimo privilegio: que nadie complete solo un "
                          "proceso sensible.",
            },
        },
        "Separacion de funciones": {
            "ideas": [
                "La **separación de funciones** reparte un proceso sensible para que nadie lo "
                "complete solo y sin rastro.",
                "Si la misma cuenta emite y **borra** facturas, puede cobrar y hacer desaparecer "
                "el registro.",
                "Separando, un rol **emite** (INSERT) y otro **anula** con un UPDATE que deja fecha, "
                "usuario y motivo.",
                "Quien diseña el esquema no opera datos, y quien **audita** solo lee.",
            ],
            "notas": {
                "min": 3,
                "explica": "Separación de funciones es repartir un proceso sensible entre dos o más "
                           "personas para que ninguna lo complete sola sin dejar rastro. En la base "
                           "significa que quien diseña el esquema no es quien opera los datos, y que "
                           "quien audita solo lee.",
                "pasos": [
                    "Una sola cuenta: INSERT de la factura (cobra) y DELETE de la factura (la "
                    "borra). Queda sin evidencia de que existió.",
                    "Funciones separadas: un rol emite con INSERT y otro anula con UPDATE del "
                    "estado a 'ANULADA'. La factura sigue ahí, con fecha, usuario y motivo.",
                    "La regla: nadie completa solo un proceso sensible.",
                ],
                "ejemplo": "Si alguien roba la sesión de recepción, con funciones separadas puede "
                           "emitir una factura, pero no borrarla ni corregir su total.",
                "preguntas": [
                    ("¿Por qué el auditor no tiene UPDATE ni sobre la tabla de auditoría?",
                     "Porque quien puede corregir el registro de lo que hizo puede borrar la "
                     "evidencia, y entonces la auditoría no prueba nada."),
                ],
                "cuidado": "La tabla factura de los datos de práctica no tiene columna estado: la "
                           "animación muestra el patrón. Si se quiere aplicar, primero se agrega la "
                           "columna.",
                "puente": "Ya sabemos qué dar a quién. Ahora la sintaxis exacta.",
            },
        },
        "GRANT y REVOKE: la sintaxis": {
            "ideas": [
                "Un rol recién creado nace con **cero privilegios**: no hace falta revocar nada "
                "para empezar.",
                "Un solo **GRANT** puede dar varios privilegios sobre varias tablas a la vez.",
                "Con GRANT recepcion TO ana_gomez la **persona** recibe el paquete completo.",
                "Un **REVOKE** de algo nunca otorgado no da error, y se escribe para documentar la "
                "decisión.",
            ],
            "notas": {
                "min": 2,
                "explica": "GRANT otorga y REVOKE retira, igual sobre roles que sobre personas. Son "
                           "cuatro sentencias que hay que poder escribir de memoria: crear el rol, "
                           "darle privilegios, dárselo a la persona y, si hace falta, retirar.",
                "pasos": [
                    "CREATE ROLE recepcion NOLOGIN: nace con cero privilegios.",
                    "Dos GRANT: SELECT, INSERT, UPDATE sobre cita (varios privilegios en uno) y "
                    "SELECT sobre dueno, mascota, veterinario (varias tablas en uno).",
                    "GRANT recepcion TO ana_gomez: la persona recibe el paquete.",
                    "REVOKE DELETE ON cita FROM recepcion: nunca se otorgó, así que no cambia nada "
                    "ni falla; se escribe porque deja constancia de que la ausencia de DELETE fue "
                    "una decisión y no un olvido.",
                ],
                "ejemplo": "GRANT SELECT ON ALL TABLES IN SCHEMA public TO auditor da SELECT sobre "
                           "las tablas que existen hoy, no sobre las que se creen mañana; para "
                           "esas existe ALTER DEFAULT PRIVILEGES.",
                "preguntas": [
                    ("¿Hace falta USAGE sobre el esquema?",
                     "Sí, para usar sus objetos; en public viene concedido por omisión, por eso "
                     "hoy no estorba. En un esquema propio es la causa número uno del GRANT que "
                     "«no funciona»."),
                ],
                "cuidado": "Probar los permisos con la cuenta dueña de las tablas no demuestra nada: "
                           "el dueño pasa por encima de todo y nunca ve un error.",
                "puente": "Hay dos formas de dar permisos que hacen daño sin avisar.",
            },
        },
        "WITH GRANT OPTION y PUBLIC": {
            "ideas": [
                "**WITH GRANT OPTION** deja que quien recibe un privilegio lo reotorgue, y el "
                "control se pierde en cadena.",
                "Para revocar esa cadena el motor exige **CASCADE**: avisa que tocará más de lo "
                "pedido.",
                "**PUBLIC** son todos los roles, los de hoy y los que se creen mañana.",
                "Un GRANT a PUBLIC entrega el dato a cualquiera; se limpia con **REVOKE ALL ... "
                "FROM PUBLIC**.",
            ],
            "notas": {
                "min": 3,
                "explica": "Dos mecanismos que hacen daño en silencio. WITH GRANT OPTION permite "
                           "que quien recibió un privilegio lo vuelva a dar, y el administrador "
                           "pierde el control de quién tiene qué. PUBLIC es un rol especial al que "
                           "pertenecen todos, incluso los que se creen mañana.",
                "pasos": [
                    "La cadena: admin da con GRANT OPTION a rol_a, rol_a se lo da a rol_b, rol_b a "
                    "rol_c. «El admin ya no sabe quién tiene el privilegio».",
                    "REVOKE ... FROM rol_a CASCADE: sin CASCADE el motor lo rechaza porque hay "
                    "privilegios que dependen de ese; con CASCADE se van todos los de la cadena.",
                    "PUBLIC: GRANT SELECT ON consulta TO PUBLIC le entrega el historial clínico a "
                    "cualquiera que se conecte, incluido el usuario que se cree mañana.",
                    "La limpieza: REVOKE ALL ON consulta FROM PUBLIC. Es una tarea real de "
                    "endurecimiento en bases heredadas.",
                ],
                "ejemplo": "El mensaje real al revocar sin CASCADE es «dependent privileges exist», "
                           "con la pista «Use CASCADE to revoke them too».",
                "preguntas": [
                    ("Si revoco un permiso a recepcion, ¿por qué ese rol todavía puede leer?",
                     "Revisa si el privilegio está concedido a PUBLIC: lo que recibe PUBLIC lo "
                     "recibe todo rol, también el que se acaba de restringir."),
                ],
                "puente": "Las dos cosas en código, con la REVOKE de la matriz.",
            },
        },
        "REVOKE, y los dos que hacen dano": {
            "notas": {
                "min": 2,
                "explica": "Tres REVOKE con propósitos distintos: dejar escrita una decisión, "
                           "limpiar PUBLIC y deshacer una cadena de reotorgamientos.",
                "pasos": [
                    ("Línea 1", "REVOKE DELETE ON cita FROM recepcion: redundante a propósito; es "
                     "la evidencia de que recepción no borra."),
                    ("Líneas 3-4", "REVOKE ALL ON consulta FROM PUBLIC: nadie lee el historial por "
                     "ser «todo el mundo»."),
                    ("Líneas 6-10", "GRANT ... WITH GRANT OPTION al auditor, y cómo se le quita "
                     "solo la opción de reotorgar: REVOKE GRANT OPTION FOR SELECT ... CASCADE. El "
                     "auditor conserva su SELECT; lo que él concedió desaparece."),
                ],
                "ejemplo": "Si el auditor alcanzó a dar SELECT sobre cita a veterinario_rol, el "
                           "REVOKE sin CASCADE responde «dependent privileges exist»; con CASCADE, "
                           "veterinario_rol pierde ese SELECT y el auditor queda con el suyo, sin "
                           "opción de reotorgar.",
                "preguntas": [
                    ("¿Qué diferencia hay entre REVOKE SELECT y REVOKE GRANT OPTION FOR SELECT?",
                     "El primero le quita el privilegio; el segundo solo le quita la capacidad de "
                     "darlo a otros."),
                ],
                "cuidado": "REVOKE SELECT ON cita FROM auditor CASCADE también le quita su propio "
                           "SELECT, y el auditor necesita leer citas.",
                "puente": "A veces el GRANT sobre la tabla entera es demasiado.",
            },
        },
        "Cuando el GRANT es demasiado": {
            "ideas": [
                "Un GRANT sobre una tabla es **todo o nada**: se ven todas sus filas y todas sus "
                "columnas.",
                "Una **vista** es una consulta guardada con nombre: recorta filas con WHERE y "
                "columnas con SELECT.",
                "La vista corre con los permisos de su **dueño**: recepción la lee sin tener SELECT "
                "sobre dueno.",
                "El **privilegio por columna** recorta solo columnas, sin crear un objeto nuevo.",
            ],
            "notas": {
                "min": 4,
                "explica": "Un GRANT sobre una tabla entrega todas sus filas y columnas. La "
                           "recepcionista solo necesita el nombre y el teléfono de quien llama, no "
                           "su correo. Hay dos formas de recortar: una vista, que recorta filas y "
                           "columnas, y el privilegio por columna, que recorta solo columnas.",
                "pasos": [
                    "La tabla entera: todas las filas, incluida la CANCELADA, y todas las columnas, "
                    "incluido el email.",
                    "La vista: deja fuera las filas canceladas (WHERE estado <> 'CANCELADA') y la "
                    "columna email (no está en su SELECT).",
                    "El privilegio por columna: GRANT SELECT (id_dueno, nombre) da solo esas dos "
                    "columnas. La regla de abajo: ¿filtra filas o cruza tablas? vista; ¿solo "
                    "columnas? privilegio por columna.",
                ],
                "ejemplo": "La tabla dueno tiene cinco columnas (id_dueno, nombre, telefono, email, "
                           "ciudad) y seis filas: con SELECT sobre la tabla se ven las 30 celdas.",
                "preguntas": [
                    ("Si le doy SELECT solo a la vista, ¿no necesita también SELECT sobre dueno?",
                     "No, y es lo más importante de la clase: la vista se ejecuta con los "
                     "privilegios de su propietario. Por eso se puede revocar la tabla y dejar la "
                     "vista."),
                ],
                "cuidado": "Con privilegio por columna, SELECT * falla: el asterisco pide también "
                           "las columnas negadas. Hay que nombrar las columnas.",
                "puente": "Las dos formas, escritas.",
            },
        },
        "Reducir la superficie": {
            "notas": {
                "min": 3,
                "explica": "Los dos mecanismos en código: la vista de agenda para recepción, con "
                           "la tabla revocada, y el privilegio por columna para el veterinario.",
                "pasos": [
                    ("Líneas 1-6", "CREATE VIEW v_agenda_recepcion: id_cita, fecha_hora, el nombre "
                     "del dueño y su teléfono, uniendo cita, mascota y dueño, sin las canceladas. "
                     "El email no está."),
                    ("Líneas 7-8", "GRANT SELECT sobre la vista y REVOKE SELECT ON dueno: recepción "
                     "llega al dueño solo a través de la vista."),
                    ("Línea 11", "GRANT SELECT (id_dueno, nombre) ON dueno TO veterinario_rol: dos "
                     "columnas de la tabla y ninguna otra."),
                ],
                "ejemplo": "Con los datos de práctica la vista devuelve 9 filas: las 10 citas menos "
                           "la que está CANCELADA.",
                "preguntas": [
                    ("¿Por qué no hacer otra vista también para el veterinario?",
                     "Se podría. Si el recorte es solo de columnas y no se quiere mantener un "
                     "objeto más, el privilegio por columna es más simple."),
                ],
                "cuidado": "Si la vista se crea con una cuenta que no puede leer dueno, falla al "
                           "consultarla: corre con los privilegios de quien la creó.",
                "puente": "¿Cómo sabemos que todo esto quedó así? Se le pregunta al motor.",
            },
        },
        "La matriz como hecho verificable:": {
            "ideas": [
                "Una matriz que solo vive en un documento es una **intención**; consultada en el "
                "motor es un **hecho**.",
                "**role_table_grants** devuelve una fila por rol, tabla y privilegio realmente "
                "otorgado.",
                "**column_privileges** agrega column_name y es la que prueba el privilegio por "
                "columna.",
            ],
            "notas": {
                "min": 2,
                "explica": "Lo que dice un documento es lo que creemos haber dado; lo que dice el "
                           "motor es lo que de verdad quedó. PostgreSQL lo expone en "
                           "information_schema con dos vistas: role_table_grants y "
                           "column_privileges.",
                "pasos": [
                    "Documento contra motor: «una matriz escrita es una intención; consultada, es "
                    "un hecho».",
                    "La consulta a role_table_grants y su salida: una fila por rol, tabla y "
                    "privilegio (recepcion · cita · INSERT, SELECT, UPDATE…).",
                    "column_privileges agrega la columna: es la única que muestra el privilegio "
                    "por columna.",
                ],
                "ejemplo": "Si la matriz dice que nadie tiene DELETE, en role_table_grants no "
                           "debe aparecer ninguna fila con privilege_type = 'DELETE' para los roles "
                           "operativos.",
                "preguntas": [
                    ("¿Por qué role_table_grants y no table_privileges?",
                     "Para el propietario que audita devuelven lo mismo; la única diferencia es "
                     "que role_table_grants omite lo que se ve solo por un GRANT a PUBLIC. Se usa "
                     "por convención del curso."),
                ],
                "puente": "Las dos consultas completas.",
            },
        },
        "La matriz como hecho verificable, no": {
            "notas": {
                "min": 2,
                "explica": "Las dos consultas de auditoría: la matriz de privilegios por tabla para "
                           "los cuatro roles y, aparte, los privilegios por columna.",
                "pasos": [
                    ("Líneas 2-5", "role_table_grants filtrada por los cuatro roles y ordenada por "
                     "rol, tabla y privilegio: así se lee como la matriz."),
                    ("Líneas 7-11", "column_privileges para veterinario_rol sobre dueno: debe "
                     "devolver exactamente dos filas, id_dueno y nombre."),
                ],
                "ejemplo": "Después de la lámina anterior, recepcion aparece con INSERT, SELECT y "
                           "UPDATE sobre cita, SELECT sobre mascota y veterinario, y SELECT sobre "
                           "v_agenda_recepcion; ya no aparece SELECT sobre dueno.",
                "preguntas": [
                    ("Me salieron cinco filas en column_privileges, con email y teléfono.",
                     "Entonces se otorgó la tabla completa: column_privileges muestra también los "
                     "privilegios de tabla repartidos por columna."),
                ],
                "cuidado": "role_table_grants no muestra los privilegios por columna: si solo se "
                           "corre la primera consulta, el recorte del veterinario parece no existir.",
                "puente": "La matriz cambia cuando cambian las personas: la política de altas y "
                          "bajas.",
            },
        },
        "La politica de altas y bajas": {
            "ideas": [
                "La **política de altas y bajas** dice quién autoriza cada cuenta, con qué rol nace "
                "y cuándo se apaga.",
                "La **baja** se hace el mismo día del retiro, y las cuentas se revisan cada 3 a 6 "
                "meses.",
                "Evita la **cuenta huérfana**: la del que se fue y cuya clave sigue funcionando.",
                "Prohíbe la **cuenta compartida**: si tres personas usan una, la auditoría no sabe "
                "quién fue.",
            ],
            "notas": {
                "min": 2,
                "explica": "La política de altas y bajas documenta el ciclo de vida de una cuenta: "
                           "quién autoriza que se cree, con qué rol nace, qué pasa cuando alguien "
                           "cambia de función y en cuánto tiempo se desactiva cuando se va. Vale "
                           "porque fija responsables y plazos, no generalidades.",
                "pasos": [
                    "La línea de tiempo: alta (quién autoriza y con qué rol), cambio de función "
                    "(se revoca un rol y se otorga otro), baja (el mismo día), y debajo la "
                    "revisión de cuentas activas cada 3 a 6 meses.",
                    "Los dos riesgos que cierra: la cuenta huérfana del pasante que se fue hace un "
                    "año, y la cuenta compartida que deja a la auditoría sin saber quién fue.",
                    "La frase final: una política sin responsables ni plazos es solo una "
                    "intención.",
                ],
                "ejemplo": "En la clínica: el alta la autoriza la administradora; la recepcionista "
                           "nueva nace con el rol recepcion y nada más; la baja del pasante se hace "
                           "el día de su salida.",
                "cuidado": "El mismo día y cada 3 a 6 meses son prácticas de gobierno, no reglas del "
                           "motor: dilo así.",
                "puente": "Cada fase del ciclo es una sentencia concreta.",
            },
        },
        "Ciclo de vida de una cuenta": {
            "ideas": [
                "En el **alta** la cuenta nace con un solo rol y una clave temporal que caduca al "
                "primer ingreso.",
                "En un **cambio** de función se otorga el rol nuevo y se revoca el anterior: los "
                "permisos no se suman.",
                "En la **baja**: REVOKE, ALTER ROLE ... NOLOGIN y REASSIGN OWNED antes de DROP ROLE.",
                "La **prueba**: con SET ROLE recepcion, el DELETE debe responder permission denied.",
            ],
            "notas": {
                "min": 3,
                "explica": "Cada fase del ciclo de vida se ejecuta con una sentencia: un GRANT o un "
                           "REVOKE. La política le pone responsable y plazo a cada una, y termina "
                           "con una prueba: comprobar en el motor que el permiso retirado de verdad "
                           "no está.",
                "pasos": [
                    "Recorre las cinco tarjetas con su código. Alta: CREATE ROLE ... LOGIN y GRANT "
                    "recepcion. Cambio: GRANT del rol nuevo y REVOKE del anterior. Baja: REVOKE y "
                    "ALTER ROLE ... NOLOGIN. Revisión: la consulta a role_table_grants, cada 3 a 6 "
                    "meses, firmada por alguien. Prueba: SET ROLE recepcion y un DELETE que debe "
                    "fallar. Cierra con el recuadro: antes de DROP ROLE, REASSIGN OWNED.",
                ],
                "ejemplo": "Si ana_gomez creó una tabla, DROP ROLE ana_gomez falla con «role "
                           "\"ana_gomez\" cannot be dropped because some objects depend on it»; "
                           "primero REASSIGN OWNED BY ana_gomez TO admin_bd.",
                "preguntas": [
                    ("¿Por qué no basta con borrar la cuenta?",
                     "Porque PostgreSQL no deja borrar un rol que todavía es dueño de objetos, y "
                     "porque la traza de auditoría debe seguir diciendo quién hizo qué."),
                ],
                "cuidado": "Quien pasa de recepción a auditoría y conserva los dos roles termina "
                           "auditando lo que él mismo modifica: el REVOKE del rol anterior es la "
                           "mitad importante del cambio.",
                "puente": "Esa prueba final depende de lo que este motor permite hacer.",
            },
        },
        "El motor de hoy es PostgreSQL": {
            "ideas": [
                "En el navegador corre todo lo de hoy: CREATE ROLE, GRANT, REVOKE, vistas e "
                "information_schema.",
                "Hay **una sola sesión** y un solo usuario con login: no se entra como recepcion en "
                "otra pestaña.",
                "**SET ROLE** cambia con qué permisos se evalúa lo que escribes, sin abrir otra "
                "conexión.",
                "Lo que debe fallar se ejecuta **una línea a la vez**, y se cierra con RESET ROLE.",
            ],
            "notas": {
                "min": 3,
                "explica": "El motor de la clase es PostgreSQL corriendo en el navegador. Ahí "
                           "funciona todo lo de hoy, con una sola limitación real: hay una sesión y "
                           "un usuario con login, así que no se puede abrir otra conexión como "
                           "recepcion. Para probar un permiso no hace falta: SET ROLE cambia el rol "
                           "con el que el motor evalúa lo que escribimos.",
                "pasos": [
                    "SET ROLE recepcion: desde esa línea los permisos son los de recepcion. SELECT "
                    "* FROM cita funciona, porque tiene SELECT.",
                    "SELECT * FROM consulta falla con permission denied, y el DELETE sobre cita "
                    "también: lo que el rol no tiene, el motor lo niega.",
                    "RESET ROLE devuelve al rol propio. La regla del recuadro: cada línea que debe "
                    "fallar se ejecuta sola, porque un ejecutor que aborta al primer error se lleva "
                    "las siguientes.",
                ],
                "ejemplo": "SET ROLE recepcion; DELETE FROM cita WHERE id_cita = 1; responde "
                           "«permission denied for table cita».",
                "preguntas": [
                    ("¿SET ROLE es lo mismo que conectarse como recepcion?",
                     "No. SET ROLE cambia con qué permisos se evalúa lo que escribo; conectarse "
                     "cambia quién está conectado. Para probar que un privilegio falta, basta lo "
                     "primero; lo que no se prueba aquí es el login ni dos personas a la vez."),
                ],
                "cuidado": "Si olvidas RESET ROLE, todo lo que sigue corre con los permisos "
                           "recortados y parece que «se dañó la base».",
                "puente": "La prueba completa, sobre la vista y el privilegio por columna.",
            },
        },
        "SET ROLE: demostrar en el motor": {
            "notas": {
                "min": 2,
                "explica": "La prueba de que el recorte funciona: como recepcion se ve la agenda "
                           "por la vista y se niegan el DELETE y la tabla dueño; como "
                           "veterinario_rol se leen solo las dos columnas concedidas.",
                "pasos": [
                    ("Líneas 1-3", "SET ROLE recepcion y la vista: 9 filas, sin la cita cancelada."),
                    ("Líneas 4-7", "DELETE sobre cita y SELECT sobre dueño: las dos responden "
                     "permission denied, con el nombre de la tabla."),
                    ("Línea 8", "RESET ROLE: de vuelta al rol propio."),
                    ("Líneas 10-14", "Como veterinario_rol: SELECT id_dueno, nombre devuelve las 6 "
                     "filas; SELECT * falla porque el asterisco pide columnas que no tiene."),
                ],
                "ejemplo": "Recepción ve el teléfono del dueño en la vista aunque no pueda leer la "
                           "tabla dueno: la vista corre con los privilegios de su propietario.",
                "preguntas": [
                    ("¿Por qué ejecutar las líneas una por una?",
                     "Porque las que fallan a propósito abortan un script de una sola corrida, y "
                     "las siguientes no se ejecutarían."),
                ],
                "cuidado": "Este bloque supone que ya se corrió el de «Reducir la superficie»: sin "
                           "la vista, la línea 3 falla por otra razón (la vista no existe).",
                "puente": "Con todo verificado, la decisión se escribe en una matriz.",
            },
        },
        "La matriz es la decision": {
            "ideas": [
                "El script es la traducción mecánica; la **matriz** es la decisión: objetos en "
                "filas, roles en columnas.",
                "Cada celda lleva **S I U D E** o un guion, y ninguna queda vacía.",
                "Un procedimiento va con **E** (EXECUTE): se invoca, no se escribe en su tabla.",
                "La matriz es **coherente** con los GRANT: si nadie recibió DELETE, no aparece "
                "una D.",
            ],
            "notas": {
                "min": 2,
                "explica": "Lo central no es el script sino la matriz rol por objeto. El script es "
                           "la traducción mecánica de una decisión; la matriz es la decisión, y "
                           "debajo de ella van las razones.",
                "pasos": [
                    "La matriz: objetos en filas, roles en columnas y en cada celda las letras. "
                    "Lee la leyenda: S SELECT, I INSERT, U UPDATE, D DELETE, E EXECUTE, guion "
                    "ninguno.",
                    "Se resalta la fila del procedimiento: va con E, nunca con S ni con I. «La "
                    "aplicación invoca la regla de negocio; no escribe en la tabla».",
                    "Las dos reglas de calidad: sin celdas vacías, y coherente con los GRANT "
                    "ejecutados.",
                ],
                "ejemplo": "Una celda bien justificada: «auditor sobre cita: solo S, porque auditar "
                           "es verificar, no corregir». Una X sin texto no es una decisión.",
                "preguntas": [
                    ("¿Por qué E para un procedimiento que todavía no existe?",
                     "Porque la matriz decide el diseño: en la Clase 3 recepción agendará a "
                     "través de sp_agendar_cita en lugar de insertar en cita."),
                ],
                "puente": "Cómo se conecta lo de hoy con las clases vecinas.",
            },
        },
        "Como amarra con las clases vecinas": {
            "ideas": [
                "La **Clase 1** dejó las tablas y las claves que hoy se protegen con roles.",
                "En la **Clase 3** recepción agendará a través de un procedimiento (EXECUTE), sin "
                "INSERT directo.",
                "En la **Clase 4** la auditoría guarda current_user y pg_dumpall respalda los roles.",
                "En la **Clase 12** la aplicación se conecta con una cuenta de servicio y su rol.",
            ],
            "notas": {
                "min": 1,
                "explica": "Lo de hoy no es una isla: protege lo que dejó la Clase 1 y es la base "
                           "de tres clases que vienen.",
                "pasos": [
                    "Recorre la imagen: la Clase 1 llega con tablas y claves; hoy se les ponen "
                    "roles; la 3 cambia el INSERT de recepción por EXECUTE sobre un "
                    "procedimiento; la 4 usa current_user en la auditoría y respalda los roles; la "
                    "12 crea la cuenta con la que se conecta la aplicación.",
                ],
                "cuidado": "Si todos comparten una cuenta, la auditoría de la Clase 4 registrará "
                           "siempre el mismo nombre y no servirá para nada.",
                "puente": "Vamos a la demo.",
            },
        },
        "Demo del dia": {
            "ideas": [
                "Crear los cuatro roles NOLOGIN, otorgar la matriz con GRANT y escribir el REVOKE "
                "de DELETE.",
                "Con **SET ROLE** recepcion, el DELETE sobre cita debe responder permission denied.",
                "Consultar **information_schema** para ver la matriz real y la vista sin el email.",
            ],
            "notas": {
                "min": 15,
                "explica": "La demo junta lo de hoy: los cuatro roles con su matriz, la vista y el "
                           "privilegio por columna, la prueba negativa con SET ROLE y la "
                           "verificación en information_schema.",
                "pasos": [
                    "1) CREATE ROLE de admin_bd, recepcion, veterinario_rol y auditor, todos NOLOGIN, "
                    "y los GRANT de la matriz con el REVOKE de DELETE (5 min). 2) La vista "
                    "v_agenda_recepcion, el REVOKE de dueño y el GRANT por columna al veterinario "
                    "(4 min). 3) SET ROLE recepcion; el DELETE, una línea sola, y lee el mensaje; "
                    "RESET ROLE (3 min). 4) Las dos consultas de information_schema y compáralas "
                    "con la matriz en voz alta (3 min).",
                ],
                "cuidado": "Ejecuta las líneas que deben fallar una por una, y no olvides RESET ROLE "
                           "antes de las consultas de verificación.",
                "puente": "Cierre de la clase.",
            },
        },
        "Clase 2 ·": {
            "notas": {
                "min": 3,
                "explica": "Cierre: hoy cada persona de la clínica quedó con un rol que le da "
                           "exactamente lo que su trabajo necesita, y lo comprobamos en el motor, no "
                           "en un documento.",
                "pasos": [
                    "Pregunta de salida: «¿cómo demuestran que recepción no puede borrar una "
                    "cita?». Respuesta esperada: SET ROLE recepcion, el DELETE responde "
                    "permission denied, y role_table_grants no muestra DELETE para ese rol.",
                ],
                "puente": "La próxima clase: la regla de negocio dentro de la base, con "
                          "procedimientos almacenados.",
            },
        },
    },
}
