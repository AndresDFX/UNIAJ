# -*- coding: utf-8 -*-
"""BD II · Clase 1 · Ideas proyectadas y GUION de cada lámina (notas del presentador).

Mismo formato que la Clase 4 en `bd2_contenido_data.py` (ver `notas_guion.py`); se fusiona solo.
Los pasos de cada animación salen de `config/animaciones/bd2/clase1/<huella>.js`: «Al entrar» es
el primer fotograma y cada «Clic k» el siguiente. En las láminas de código y en las de una sola
imagen los pasos llevan su propia etiqueta (no hay clic que dar).

Datos que se citan: los del script de la demo de hoy (Ana Pérez y la perra Luna) y, cuando se
habla de «los datos de práctica», los sembrados del curso (6 dueños, 4 veterinarios, 8 mascotas
con Rocky y Kiara inactivas, 10 citas). Las salidas y mensajes de error se comprobaron en
PostgreSQL (PGlite).
"""

CONTENIDO = {
    1: {
        "Encuadre de hoy": {
            "notas": {
                "min": 4,
                "explica": "Hoy no se repite Bases de Datos I: se arranca la base de datos de una "
                           "clínica veterinaria que hoy trabaja en papel. Vamos a decidir qué tablas "
                           "tiene, cómo se identifica cada fila y qué reglas defiende el motor por sí "
                           "solo, y a dejar el modelo en dos formas que deben coincidir: el diagrama y "
                           "el CREATE TABLE.",
                "pasos": [
                    "Lee el tema y la herramienta. Pregunta de arranque: «¿qué pasa en una clínica "
                    "cuando se pierde la ficha de un paciente?». Deja que respondan 1-2 personas.",
                    ("Cierre del encuadre", "«Al final de hoy van a poder decir por qué una cita no "
                     "puede apuntar a una mascota que no existe, y por qué eso todavía no basta»."),
                ],
                "cuidado": "Las herramientas son gratuitas y corren en el navegador: nadie tiene "
                           "que instalar nada hoy. Si alguien no tiene cuenta en ningún lado, DB "
                           "Fiddle funciona sin registrarse.",
                "puente": "Este es el recorrido de las dos horas.",
            },
        },
        "Mapa del bloque": {
            "notas": {
                "min": 1,
                "explica": "Las dos horas en cinco tramos: encuadre, teoría con una lámina por "
                           "concepto, demo en vivo, práctica opcional y cierre.",
                "pasos": ["Señala solo los tramos; no te detengas. La práctica tiene su guía en la "
                          "carpeta de la clase y es opcional."],
                "puente": "Antes de dibujar una tabla, conozcamos para quién la dibujamos.",
            },
        },
        "El cliente: una clínica veterinaria en papel": {
            "ideas": [
                "La clínica atiende unas **150 citas al día** con 16 veterinarios, y guarda todo "
                "en **carpetas de papel**.",
                "El papel duele en tres puntos: fichas que se **pierden**, **filas** para buscar "
                "un historial y **cero métricas**.",
                "Usarán la base el **dueño**, la **recepcionista** y el **veterinario**, y cada "
                "uno espera algo distinto.",
                "Sus intereses **chocan**: un dato de más ayuda a las métricas y le suma clics a "
                "quien agenda.",
            ],
            "notas": {
                "min": 4,
                "explica": "Toda base de datos se diseña para alguien. Nuestro cliente es una "
                           "clínica veterinaria de Cali con unas 150 citas diarias, 16 veterinarios "
                           "y cerca de 5.000 mascotas de 2.000 dueños, y todo vive en carpetas. El "
                           "semestre entero construye la capa de datos de esa clínica: no la "
                           "aplicación ni las pantallas, sino el esquema, sus reglas, sus permisos y "
                           "su rendimiento.",
                "pasos": [
                    "Arriba, los tres dolores, y conecta cada uno con una decisión del curso: la "
                    "ficha perdida se resuelve con una fila que tiene clave primaria (hoy); las "
                    "filas en la sala de espera, con índices (Clase 7); la falta de métricas, con "
                    "consultas agregadas (Clase 6). Abajo, las tres personas y lo que quiere cada "
                    "una, y el recuadro del conflicto: «un campo más en el formulario de la cita le "
                    "da métricas al dueño y le suma clics a la recepcionista».",
                ],
                "ejemplo": "¿Guardamos la raza de la mascota? Al dueño le sirve para saber qué "
                           "razas atiende más; a la recepcionista le cuesta un campo más por cita; "
                           "al veterinario le sirve en la consulta. Se guarda en mascota, una sola "
                           "vez, y no en cada cita.",
                "preguntas": [
                    ("¿Esta columna sobra?",
                     "Responde con otra pregunta: ¿cuál de las tres personas la necesita, y qué "
                     "pierde otra si la agregamos? Así se decide un modelo, no se copia."),
                    ("¿Tenemos que hacer la aplicación?",
                     "No. En esta materia se construye la base de datos: tablas, reglas, roles, "
                     "procedimientos y rendimiento. La aplicación es de otra materia."),
                ],
                "cuidado": "El modelo tiene 8 entidades (dueño, mascota, veterinario, cita, "
                           "consulta, insumo, factura, detalle de factura) y 3 reglas que vuelven "
                           "todo el semestre: una mascota inactiva no agenda, el stock nunca queda "
                           "negativo y todo cambio de estado de una cita queda registrado. Nómbralas "
                           "hoy aunque se resuelvan después.",
                "puente": "¿Por qué esto no es repetir Bases de Datos I? Por el vocabulario con "
                          "que vamos a decidir.",
            },
        },
        "Por que esto no es Bases de Datos I": {
            "ideas": [
                "En BD I se pedía la consulta correcta; aquí, un **esquema** que siga correcto "
                "con tres usuarios y datos malos.",
                "Una **tabla** (relación) guarda entidades de un solo tipo: mascota guarda "
                "mascotas y nada más.",
                "Una **fila** es una instancia concreta e irrepetible: la perra Luna, y solo ella.",
                "Una **columna** es un atributo con su **dominio**: especie solo acepta Canino, "
                "Felino, Ave u Otro.",
            ],
            "notas": {
                "min": 3,
                "explica": "En Bases de Datos I el objetivo era escribir la consulta que devuelve el "
                           "resultado correcto. Aquí el objetivo es diseñar un esquema que siga "
                           "siendo correcto cuando lo usen tres personas distintas, cuando tenga "
                           "cien mil filas y cuando alguien meta datos malos. Para decidir eso hacen "
                           "falta tres palabras precisas: tabla, fila y columna con su dominio.",
                "pasos": [
                    "La tabla mascota con tres filas: «una tabla guarda cosas de un solo tipo; aquí "
                    "no hay dueños ni citas, solo mascotas».",
                    "Se marca la fila de Luna: «una fila es UNA mascota concreta; si la misma "
                    "mascota apareciera en dos filas, ya no sabríamos cuál es la verdadera».",
                    "Se marca la columna especie y aparece su dominio: «una columna no acepta "
                    "cualquier cosa; especie solo admite cuatro valores, y eso lo puede vigilar el "
                    "motor».",
                ],
                "ejemplo": "Si alguien escribe especie = 'Perro' en vez de 'Canino', el dato "
                           "parece correcto pero rompe el conteo de especies del mes. El dominio "
                           "cerrado es lo que evita eso.",
                "preguntas": [
                    ("¿Dominio no era el tema del proyecto?",
                     "La palabra tiene dos usos: el dominio de un atributo (sus valores legales) y "
                     "el dominio del problema (la clínica). Hoy se usan los dos; aclara cuál."),
                ],
                "cuidado": "Sobre estas tres nociones se monta el semestre: los permisos de la "
                           "Clase 2 se dan sobre tablas, las validaciones de la Clase 3 miran "
                           "columnas y los índices de la Clase 7 se crean sobre columnas concretas.",
                "puente": "El mismo modelo se puede mirar de dos maneras: como negocio y como "
                          "tablas.",
            },
        },
        "Nivel conceptual y nivel fisico": {
            "ideas": [
                "El nivel **conceptual** habla el idioma del negocio: dueño posee mascota, sin "
                "tipos ni motor.",
                "El nivel **físico** lo vuelve tablas: columnas con tipo, restricciones y claves, "
                "como telefono VARCHAR(30).",
                "Son **dos vistas del mismo modelo**: el diagrama ER y el CREATE TABLE dicen lo "
                "mismo.",
                "El conceptual está completo cuando otra persona escribe el físico **sin "
                "preguntar**.",
            ],
            "notas": {
                "min": 3,
                "explica": "Hay dos niveles que se mezclan. El conceptual nombra entidades y "
                           "relaciones con palabras del negocio, sin decir nada del motor. El físico "
                           "convierte eso en tablas con columnas tipadas, restricciones y claves. "
                           "No son dos modelos: es el mismo modelo visto de dos formas, y por eso "
                           "hoy se producen dos artefactos que deben coincidir.",
                "pasos": [
                    "Arriba, el nivel conceptual: dos cajas, dueño y mascota, y el verbo «posee». "
                    "«Esto lo entiende la administradora de la clínica; no hay un solo tipo de "
                    "dato».",
                    "Abajo aparecen las tablas dueno y mascota con sus columnas: id_dueno SERIAL "
                    "PK, telefono VARCHAR(30) NOT NULL, id_dueno INT FK → dueno. «Esto ya lo "
                    "entiende el motor».",
                    "Las flechas punteadas unen cada caja con su tabla: «dos vistas del MISMO "
                    "modelo; el diagrama ER es la vista conceptual y el CREATE TABLE la física».",
                ],
                "ejemplo": "«Dueño posee mascota» en el diagrama se convierte en la columna "
                           "mascota.id_dueno con REFERENCES dueno(id_dueno) en el DDL.",
                "preguntas": [
                    ("¿Por qué el diagrama debe llevar tipos y longitudes si es conceptual?",
                     "Porque el criterio de completitud es que alguien pueda escribir el CREATE "
                     "TABLE mirándolo sin preguntar. Sin tipos, el diagrama no se puede traducir."),
                ],
                "cuidado": "No presentes el diagrama y el DDL como dos tareas separadas: si un "
                           "nombre cambia entre los dos, ya no son el mismo modelo.",
                "puente": "Veamos el modelo mínimo de la clínica en su vista conceptual.",
            },
        },
        "ER minimo": {
            "notas": {
                "min": 2,
                "explica": "Este es el corazón del modelo: dueño, mascota, cita y veterinario, "
                           "unidos por tres relaciones uno a muchos. La regla que se lee aquí es "
                           "que la clave foránea vive siempre en la tabla del lado «muchos».",
                "pasos": [
                    "Lee las relaciones en voz alta: un dueño tiene N mascotas, una mascota tiene "
                    "N citas, un veterinario atiende N citas. Señala dónde quedó cada FK: "
                    "mascota lleva id_dueno y cita lleva id_mascota (y también id_veterinario, "
                    "que el diagrama abrevia).",
                    ("Después", "Lee la nota de abajo: la PK identifica cada fila y la FK "
                     "materializa la relación; el motor rechaza una cita con id_mascota 999 si esa "
                     "mascota no existe."),
                ],
                "ejemplo": "Luna (id_mascota 10) pertenece a Ana Pérez (id_dueno 1): la fila de "
                           "Luna guarda id_dueno = 1. Ana no guarda nada de Luna.",
                "preguntas": [
                    ("¿Por qué la FK no va en dueño, con la lista de sus mascotas?",
                     "Porque una celda no guarda listas (primera forma normal) y porque un dueño "
                     "puede tener cualquier número de mascotas. El lado N es el que tiene una "
                     "sola referencia por fila."),
                ],
                "puente": "Ese diagrama, escrito como DDL: la tabla que depende de cita.",
            },
        },
        "El DDL minimo que sostiene el ER": {
            "notas": {
                "min": 3,
                "explica": "La misma información del diagrama, ahora en físico, sobre la tabla "
                           "consulta. Muestra las tres piezas que toda tabla del curso tiene: clave "
                           "primaria, clave foránea y una regla de negocio con CHECK.",
                "pasos": [
                    ("Línea 2", "id_consulta SERIAL PRIMARY KEY: la base genera el número y "
                     "ninguna consulta se repite."),
                    ("Líneas 3-4", "id_cita INT NOT NULL UNIQUE REFERENCES cita: NOT NULL porque "
                     "no hay consulta sin cita, REFERENCES porque la cita debe existir, y UNIQUE "
                     "porque una cita tiene a lo sumo una consulta. Eso convierte la relación en "
                     "1:1."),
                    ("Líneas 5-7", "diagnostico obligatorio y precio NUMERIC(12,2) con CHECK "
                     "(precio >= 0): la primera regla de negocio que defiende el motor."),
                ],
                "ejemplo": "Una segunda consulta para la cita 2 falla con «duplicate key value "
                           "violates unique constraint "
                           "\"consulta_id_cita_key\"», y un precio de −5 con «violates check "
                           "constraint \"consulta_precio_check\"».",
                "preguntas": [
                    ("¿Por qué no pongo id_consulta dentro de cita?",
                     "Porque una cita programada todavía no tiene consulta: la columna quedaría "
                     "vacía en la mayoría de filas. La FK va en la tabla que depende."),
                ],
                "cuidado": "La relación cita-consulta es 1:1 pero no simétrica: la cita existe "
                           "sin consulta; la consulta no existe sin cita.",
                "puente": "El mismo patrón, completo, sobre la tabla de veterinarios.",
            },
        },
        "El patron de tabla": {
            "notas": {
                "min": 2,
                "explica": "Este es el molde de cualquier tabla del curso, aplicado a veterinario: "
                           "clave sustituta, dato natural con UNIQUE, columnas obligatorias, un "
                           "dominio cerrado con CHECK y la baja lógica con DEFAULT.",
                "pasos": [
                    ("Líneas 3-4", "id_veterinario SERIAL es la clave sustituta; tarjeta_prof es "
                     "la natural: UNIQUE para que no se repita, pero puede faltar."),
                    ("Líneas 5-7", "nombre y especialidad son NOT NULL; especialidad solo acepta "
                     "'GENERAL', 'CIRUGIA' o 'DERMATOLOGIA'."),
                    ("Líneas 8-9", "activo CHAR(1) DEFAULT 'S' con CHECK: si no se dice nada, el "
                     "veterinario nace activo, y nunca se borra: se marca 'N'."),
                ],
                "ejemplo": "INSERT INTO veterinario (nombre, especialidad) VALUES ('Laura "
                           "Restrepo', 'GENERAL'); crea el id 1, con activo = 'S' y tarjeta_prof "
                           "nula.",
                "preguntas": [
                    ("¿UNIQUE deja tener varios veterinarios sin tarjeta?",
                     "Sí: en PostgreSQL dos NULL no se consideran iguales, así que UNIQUE admite "
                     "varios nulos. Lo que no admite es la misma tarjeta dos veces."),
                ],
                "cuidado": "El CHECK distingue mayúsculas: 'Cirugia' no es 'CIRUGIA' y se rechaza "
                           "con «violates check constraint \"veterinario_especialidad_check\"». "
                           "Decide el formato del dominio y úsalo igual en todos los INSERT.",
                "puente": "Con las tablas unidas por FK, la consulta típica las recorre con JOIN.",
            },
        },
        "El JOIN de tres tablas": {
            "notas": {
                "min": 3,
                "explica": "La consulta más común del sistema: la agenda con el nombre de la "
                           "mascota y de su dueño. Cada JOIN sigue una clave foránea del diagrama: "
                           "cita llega a mascota por id_mascota, y mascota llega a dueño por "
                           "id_dueno.",
                "pasos": [
                    ("Líneas 1-4", "Las columnas que se muestran, con alias: m.nombre AS mascota "
                     "y d.nombre AS dueno, porque las dos tablas tienen una columna nombre."),
                    ("Líneas 5-7", "FROM cita y dos JOIN, cada uno con su ON sobre la FK."),
                    ("Líneas 8-10", "El WHERE filtra después de unir: citas desde el 1 de "
                     "septiembre y solo mascotas activas; ORDER BY por fecha y hora."),
                ],
                "ejemplo": "Con los datos de práctica (10 citas, ninguna de Rocky ni de Kiara, que "
                           "están inactivas) devuelve 10 filas; la primera es Firulais, de Ana "
                           "Gomez, el 1 de septiembre a las 08:00.",
                "preguntas": [
                    ("¿Da lo mismo poner m.activa = 'S' en el WHERE o en el ON?",
                     "Con JOIN interno, sí. Con LEFT JOIN no: en el ON conserva la cita con la "
                     "mascota en nulo; en el WHERE la elimina."),
                ],
                "cuidado": "Lee bien la leyenda: el producto cartesiano sale con la coma (FROM "
                           "cita c, mascota m sin la condición da 10 × 8 = 80 filas) o con CROSS "
                           "JOIN; con JOIN sin ON, PostgreSQL responde error de sintaxis. El riesgo "
                           "real es un ON equivocado, que no da error y devuelve filas que no "
                           "corresponden.",
                "puente": "Cada JOIN se apoya en una clave primaria. ¿Cuál columna debe serlo?",
            },
        },
        "Clave primaria: natural o sustituta": {
            "ideas": [
                "La **clave primaria** identifica cada fila: no se repite, no admite nulos y el "
                "motor lo verifica.",
                "Una clave **natural** viene del mundo real, como la cédula o el microchip, y la "
                "controla un tercero.",
                "Una clave **sustituta** la genera la base (1, 2, 3) y nunca hay que corregirla.",
                "Si el valor lo controla un tercero, se guarda con **UNIQUE**, no como clave "
                "primaria.",
            ],
            "notas": {
                "min": 3,
                "explica": "Toda tabla necesita una clave primaria: la columna que identifica una "
                           "fila sin ambigüedad. Eso no se discute; lo que se decide es cuál. La "
                           "natural es un dato del mundo real; la sustituta es un número sin "
                           "significado que genera la base. En la clínica gana la sustituta, y el "
                           "dato natural se guarda aparte con UNIQUE.",
                "pasos": [
                    "Arriba, la definición: no se repite y no admite nulos. «No es estilo: el "
                    "motor lo revisa en cada INSERT y UPDATE». Pregunta: «¿cuál columna de dueño "
                    "usarían?».",
                    "La natural, cédula o microchip, y sus tres fallas en la clínica: el dueño "
                    "llega sin la cédula a la mano, el microchip se digita mal y hay que "
                    "corregirlo, y la mascota rescatada no tiene microchip.",
                    "La sustituta: la genera la base, no significa nada y nunca se corrige. Lee la "
                    "regla de abajo y aclara que es convención de oficio, no regla del motor.",
                ],
                "ejemplo": "dueno(id_dueno SERIAL PRIMARY KEY, cedula VARCHAR(20) UNIQUE, ...): la "
                           "cédula no se repite, puede quedar nula un rato y se corrige sin tocar "
                           "las mascotas, que apuntan a id_dueno.",
                "preguntas": [
                    ("¿La clave primaria tiene que ser la primera columna y autoincremental?",
                     "No. El orden de las columnas no le importa al motor, y el autoincremento es "
                     "solo una forma cómoda de generar valores sustitutos."),
                    ("¿La natural no ahorra un JOIN?",
                     "Sí, cuando se busca por ella. Pero si cambia, hay que corregirla en todas "
                     "las tablas que la referencian; la sustituta nunca cambia."),
                ],
                "cuidado": "No digas que la natural «está mal»: es válida cuando el dato es "
                           "estable y lo controla la propia organización. La regla es sobre quién "
                           "controla el valor.",
                "puente": "Elegida la clave, el siguiente error clásico es repetir datos. Primero "
                          "la enfermedad.",
            },
        },
        "Normalizacion 1FN-3FN": {
            "ideas": [
                "Si el teléfono del dueño se copia en cada cita, aparecen tres **anomalías**.",
                "Al **actualizar** quedan dos verdades; no se puede **insertar** un dueño sin cita; "
                "al **borrar** la cita se pierde el teléfono.",
                "Las formas normales son la **cura**: cada dato vive una sola vez, en la tabla de "
                "la que depende.",
                "La **3FN** es el punto de parada práctico; romperla exige una razón medible.",
            ],
            "notas": {
                "min": 5,
                "explica": "Normalizar se entiende mejor empezando por el problema. Si un dato se "
                           "guarda repetido, la base puede contradecirse, no puede registrar cosas "
                           "que existen y pierde datos al borrar otros. Las tres formas normales son "
                           "la cura: cada dato vive una sola vez, en la tabla de la que depende.",
                "pasos": [
                    "La tabla mal diseñada: cada cita guarda el nombre y el teléfono del dueño. "
                    "«Ana Pérez aparece dos veces, con su teléfono dos veces».",
                    "Actualización: Ana cambia de teléfono y solo se corrige una cita. «¿Cuál es "
                    "su teléfono? La base guarda dos verdades».",
                    "Inserción: un dueño nuevo que todavía no pide cita no se puede registrar, "
                    "porque su teléfono solo vive en cita.",
                    "Borrado: se borra la única cita de Luis Mora y su teléfono desaparece con ella.",
                    "La cura: dueno(id_dueno, nombre, telefono) y cita con la referencia al dueño. "
                    "El teléfono vive una vez.",
                ],
                "ejemplo": "Las tres formas, con la clínica: 1FN, nada de listas en una celda (dos "
                           "teléfonos juntos van a otra tabla); 2FN, en detalle_factura el nombre "
                           "del insumo depende solo de id_insumo y sale a insumo, pero el precio "
                           "unitario se queda porque es el precio del día de la venta; 3FN, la "
                           "especialidad del veterinario no se guarda en cita: depende de "
                           "id_veterinario.",
                "preguntas": [
                    ("Si la pantalla muestra todo junto, ¿por qué no una sola tabla?",
                     "Por costo: el teléfono de un dueño con veinte citas viviría veinte veces y "
                     "bastaría una actualización parcial para que el sistema mienta."),
                    ("¿El precio_unit de detalle_factura no es redundante?",
                     "No: es el precio histórico. Si se recalculara con el precio actual, "
                     "reimprimir una factura de hace seis meses daría otra cifra."),
                ],
                "cuidado": "No dictes 1FN-2FN-3FN como una escalera de definiciones sin mostrar "
                           "una anomalía concreta: el grupo termina normalizando por ritual y "
                           "partiendo tablas que nunca se consultan por separado.",
                "puente": "Al separar tablas, alguien tiene que garantizar que las referencias "
                          "apunten a algo real: la clave foránea.",
            },
        },
        "Clave foranea, borrado": {
            "ideas": [
                "La **clave foránea** obliga a que cada referencia apunte a una fila que existe: "
                "la mascota 999 se rechaza.",
                "Al borrar el padre, el comportamiento **se elige**: RESTRICT o NO ACTION, CASCADE "
                "o SET NULL.",
                "Si no se declara nada, el estándar es **restrictivo**: no se borra un padre con "
                "hijos.",
                "En la clínica casi nada se borra: **CASCADE** solo para las líneas de una factura.",
            ],
            "notas": {
                "min": 3,
                "explica": "La clave foránea hace que el motor se niegue a guardar una referencia "
                           "inventada. Esa es la mitad que todos conocen. La otra mitad es qué pasa "
                           "cuando se intenta borrar la fila a la que otros apuntan: eso se decide "
                           "al declarar la FK, y si no se decide, el estándar impide el borrado.",
                "pasos": [
                    "Dos tablas: las citas apuntan a mascotas que existen (1 y 2). «La flecha es "
                    "la FK: cita.id_mascota debe existir en mascota».",
                    "El INSERT con id_mascota 999: el motor lo rechaza y nombra la restricción "
                    "violada, cita_id_mascota_fkey. Nada se insertó.",
                    "El DELETE de la mascota 1, que tiene citas: rechazado. «Sin cláusula ON "
                    "DELETE el comportamiento es restrictivo; eso es regla del estándar SQL, no "
                    "una costumbre».",
                ],
                "ejemplo": "Decisión por relación: mascota → dueño, restrictiva (borrar un dueño no "
                           "puede evaporar el historial); consulta → cita, restrictiva; "
                           "detalle_factura → factura, CASCADE (una línea no significa nada sin su "
                           "factura); detalle_factura → insumo, restrictiva (no se borra un insumo "
                           "ya facturado).",
                "preguntas": [
                    ("¿Qué diferencia hay entre RESTRICT y NO ACTION?",
                     "Las dos impiden borrar el padre con hijos. NO ACTION, la opción por omisión, "
                     "revisa al final de la sentencia y puede diferirse; RESTRICT revisa de "
                     "inmediato. Para este curso se comportan igual."),
                ],
                "cuidado": "CASCADE en mascota → dueño parece cómodo y es peligroso: un DELETE de un "
                           "dueño se llevaría sus mascotas y, en cadena, sus citas y su historia "
                           "clínica.",
                "puente": "Veamos cómo se declara la FK con su comportamiento al borrar.",
            },
        },
        "La clave foranea y que pasa al borrar el padre": {
            "notas": {
                "min": 2,
                "explica": "Dos cosas en un mismo código: la tabla insumo con sus reglas, y una FK "
                           "agregada después con ALTER TABLE, donde se declara explícitamente qué "
                           "pasa al borrar el insumo referenciado.",
                "pasos": [
                    ("Líneas 1-6", "insumo: stock entero, por defecto 0 y nunca negativo (CHECK "
                     "stock >= 0); precio_unit mayor que cero."),
                    ("Líneas 8-9", "El comentario: si no se declara, PostgreSQL asume NO ACTION y "
                     "se niega a borrar."),
                    ("Líneas 10-13", "ALTER TABLE detalle_factura ADD CONSTRAINT fk_detalle_insumo "
                     "... ON DELETE RESTRICT: el nombre de la restricción lo elegimos nosotros y es "
                     "el que aparecerá en el mensaje de error."),
                ],
                "ejemplo": "Con un insumo ya facturado, DELETE FROM insumo WHERE id_insumo = 1 "
                           "responde: «update or delete on table \"insumo\" violates RESTRICT "
                           "setting of foreign key constraint \"fk_detalle_insumo\" on table "
                           "\"detalle_factura\"».",
                "preguntas": [
                    ("¿Por qué ponerle nombre a la restricción?",
                     "Porque el nombre sale en el error: fk_detalle_insumo dice qué se violó; un "
                     "nombre automático obliga a buscarlo en el catálogo."),
                ],
                "cuidado": "El CHECK (stock >= 0) de esta tabla es el que la Clase 4 retira a "
                           "propósito en su demo; aquí queda como la primera defensa del stock.",
                "puente": "Y así se ve, palabra por palabra, el error que devuelve el motor.",
            },
        },
        "Integridad referencial: el error": {
            "notas": {
                "min": 2,
                "explica": "Integridad referencial en vivo: el mismo INSERT funciona con una "
                           "mascota que existe y falla con una que no. Lo importante es aprender a "
                           "leer el mensaje del motor.",
                "pasos": [
                    ("Líneas 2-4", "Cita para la mascota 1, que existe: INSERT 0 1, una fila "
                     "insertada."),
                    ("Líneas 6-10", "Cita para la mascota 999: el error dice la tabla (cita), la "
                     "restricción (cita_id_mascota_fkey) y, en DETAIL, la clave que falta: "
                     "(id_mascota)=(999) no está en mascota."),
                ],
                "ejemplo": "Después del error, SELECT COUNT(*) FROM cita muestra el mismo número "
                           "que antes del segundo INSERT: la sentencia que falla no deja nada.",
                "preguntas": [
                    ("¿De dónde sale el nombre cita_id_mascota_fkey?",
                     "PostgreSQL lo arma solo cuando la FK no tiene nombre: tabla, columna y el "
                     "sufijo fkey."),
                ],
                "puente": "Ahora, por qué en un sistema real casi nunca se borra una mascota.",
            },
        },
        "Baja logica": {
            "ideas": [
                "En un sistema real no se hace **DELETE** de clientes ni pacientes: se marcan como "
                "inactivos.",
                "DELETE choca con las referencias, borra la historia clínica y no se puede deshacer.",
                "La **baja lógica** es un UPDATE: activa = 'N' conserva citas y facturas, y se "
                "revierte.",
                "Ojo: la **FK no defiende** esta regla; para el motor, la mascota inactiva sigue "
                "existiendo.",
            ],
            "notas": {
                "min": 3,
                "explica": "Una mascota que ya no viene no se borra: se marca como inactiva. Borrar "
                           "falla por integridad, destruye el historial y es irreversible; marcar "
                           "conserva todo y se puede deshacer. La consecuencia importante es que "
                           "la regla «una mascota inactiva no agenda» ya no la defiende la FK.",
                "pasos": [
                    "Izquierda, el borrado físico: Luna tiene citas, consultas y facturas "
                    "colgando. Tres problemas: la integridad lo impide, se pierde la historia y es "
                    "irreversible.",
                    "Derecha, la baja lógica: UPDATE mascota SET activa = 'N'. Las referencias "
                    "siguen válidas, el historial queda intacto y se revierte con activa = 'S'.",
                    "Abajo, cómo se declara (activa CHAR(1) DEFAULT 'S' CHECK (activa IN "
                    "('S','N'))), que las consultas del día filtran WHERE activa = 'S', y el "
                    "aviso: para la FK la mascota inactiva sigue existiendo.",
                ],
                "ejemplo": "UPDATE mascota SET activa = 0 WHERE id_mascota = 2; falla con "
                           "«violates check constraint \"mascota_activa_check\"»: los valores son "
                           "'S' y 'N', no 0 y 1.",
                "preguntas": [
                    ("Entonces, ¿quién impide agendar a una mascota inactiva?",
                     "Un CHECK no puede (mira solo su propia fila, y activa vive en otra tabla). "
                     "Lo resuelve un procedimiento almacenado (Clase 3) o un trigger (Clase 4)."),
                ],
                "cuidado": "Si el grupo sale de hoy pensando en DELETE, en la Clase 3 no va a "
                           "entender para qué se valida «mascota activa» antes de agendar.",
                "puente": "Comprobémoslo con código: la FK acepta la cita de una mascota inactiva.",
            },
        },
        "Lo que el DDL NO puede defender solo": {
            "notas": {
                "min": 3,
                "explica": "El código demuestra el límite del DDL: después de dar de baja a la "
                           "mascota 1, el motor acepta una cita nueva para ella. La FK garantiza "
                           "que el identificador existe, no que el negocio lo quiera.",
                "pasos": [
                    ("Línea 2", "UPDATE mascota SET activa = 'N' WHERE id_mascota = 1: la baja "
                     "lógica."),
                    ("Líneas 4-6", "El INSERT de una cita para la mascota 1: INSERT 0 1. El motor "
                     "la acepta porque la mascota 1 existe."),
                    ("Líneas 8-10", "Un CHECK tampoco sirve: solo mira columnas de su propia fila, "
                     "y activa está en mascota, no en cita. Hace falta un procedimiento (Clase 3) "
                     "o un trigger (Clase 4)."),
                ],
                "ejemplo": "Con los datos de práctica, el riesgo se mide con una consulta: citas no "
                           "canceladas cuya mascota tiene activa = 'N'. Hoy da 0 filas; mañana "
                           "puede no darlo.",
                "preguntas": [
                    ("¿Y si pongo la columna activa también en cita?",
                     "Sería un dato repetido: se desincroniza en cuanto cambie la mascota (la "
                     "anomalía de actualización de hace un rato)."),
                ],
                "cuidado": "Las tres reglas del modelo se reparten así: «stock nunca negativo» sí "
                           "cabe en un CHECK; «mascota inactiva no agenda» y «todo cambio de estado "
                           "queda registrado» necesitan lógica programada.",
                "puente": "Volvamos al diagrama: ¿qué lo hace un diagrama y no un dibujo?",
            },
        },
        "Que separa un diagrama ER de un dibujo": {
            "ideas": [
                "Un **dibujo** son cajas unidas por líneas; un **diagrama ER** cumple cinco "
                "condiciones verificables.",
                "Entidades en singular con su PK, atributos con **tipo y longitud**, y cada FK "
                "señalada.",
                "Cada relación lleva **cardinalidad** en los dos extremos y un nombre verbal: "
                "dueno posee mascota.",
                "Prueba: otra persona escribe el **CREATE TABLE** mirándolo, sin preguntar nada.",
            ],
            "notas": {
                "min": 3,
                "explica": "Es fácil dibujar cajas y creer que eso es un modelo. Un diagrama "
                           "entidad-relación bien hecho cumple cinco condiciones que se pueden "
                           "revisar una por una, y tiene una prueba de aceptación muy simple: "
                           "alguien más debe poder escribir el CREATE TABLE con solo mirarlo.",
                "pasos": [
                    "El dibujo: «Dueños» y «Mascotas» unidos por una línea. «¿Qué tipo tiene el "
                    "teléfono? ¿Cuántas mascotas puede tener un dueño? El dibujo no lo dice».",
                    "El mismo modelo como diagrama: dueno y mascota en singular, PK y FK marcadas, "
                    "atributos con tipo, cardinalidad 1..1 y 0..N y el verbo «posee».",
                    "Las cinco condiciones, una por una; detente en la 4: el mínimo dice si la "
                    "relación es obligatoria (0..N: un dueño puede no tener mascotas aún).",
                    "La prueba de aceptación: otra persona escribe el CREATE TABLE mirándolo, sin "
                    "preguntar.",
                ],
                "ejemplo": "Cita y consulta son 1 a 1 pero no simétricas: una cita programada aún "
                           "no tiene consulta, y una consulta no existe sin su cita. Eso se "
                           "materializa como consulta.id_cita NOT NULL UNIQUE.",
                "preguntas": [
                    ("¿Cuánto debe ocupar el diagrama?",
                     "El modelo completo tiene 8 entidades y 7 relaciones y cabe legible en una "
                     "hoja. Si no cabe, se divide por subsistemas (convención, no norma)."),
                ],
                "cuidado": "No aceptes un diagrama sin cardinalidades ni tipos «porque se ve "
                           "ordenado»: la decisión que falta (¿un veterinario puede tener dos citas "
                           "en la misma franja?) reaparece cuando ya hay datos y procedimientos "
                           "escritos encima.",
                "puente": "La condición 2 pide tipos: elegirlos mal es donde se pagan las "
                          "facturas más caras.",
            },
        },
        "Tipos de datos": {
            "ideas": [
                "Un **teléfono** no es un número: como NUMERIC pierde el 0 inicial y el +; va "
                "VARCHAR(30).",
                "Una **fecha** no es texto: como VARCHAR ordena alfabéticamente y no suma "
                "minutos; va TIMESTAMP.",
                "El **dinero** no es flotante: FLOAT acumula error al sumar; va DECIMAL(12,2).",
                "Todo VARCHAR(4000) por comodidad deja a la base **sin validar** nada.",
            ],
            "notas": {
                "min": 3,
                "explica": "Elegir el tipo parece trivial y es donde se pagan los errores más "
                           "caros, porque cambiarlo después obliga a convertir datos que ya existen. "
                           "Hay tres casos clásicos: teléfono, fecha y dinero, y una tentación "
                           "contraria, declarar todo como texto largo.",
                "pasos": [
                    "Teléfono: como NUMERIC se pierden el 0 inicial, el + del prefijo y la "
                    "extensión. Va VARCHAR(30).",
                    "Fecha: como VARCHAR(20), ORDER BY ordena como palabras y no se pueden sumar "
                    "30 minutos para calcular el fin de la cita. Va TIMESTAMP.",
                    "Dinero: FLOAT guarda decimales en binario; 0.1 + 0.2 no da exactamente 0.3 y "
                    "el total deja de cuadrar con sus líneas. Va DECIMAL(12,2), que en PostgreSQL "
                    "es lo mismo que NUMERIC(12,2).",
                    "La tentación contraria: todo VARCHAR(4000). La base ya no valida nada y cada "
                    "pantalla tiene que hacerlo por su cuenta.",
                ],
                "ejemplo": "En PostgreSQL, SELECT 0.1::float8 + 0.2::float8 = 0.3::float8 devuelve "
                           "false; con NUMERIC devuelve true. Y ordenar como texto las fechas "
                           "'2026-10-02' y '2026-9-15' pone la de septiembre después de la de "
                           "octubre.",
                "preguntas": [
                    ("¿Por qué email VARCHAR(120) y no 50?",
                     "Porque el estándar de correo admite direcciones de hasta 254 caracteres; "
                     "120 cubre los casos reales. Son números de convención del curso: nombre 80, "
                     "teléfono 30, especie 40."),
                ],
                "cuidado": "Si vienes de Oracle: allí el dinero es NUMBER(12,2); en PostgreSQL "
                           "NUMBER no existe, se escribe NUMERIC o DECIMAL.",
                "puente": "Además del tipo, el nombre: una mayúscula puede costar veinte minutos.",
            },
        },
        "Convenciones de nombres": {
            "ideas": [
                "PostgreSQL pasa a **minúsculas** todo nombre sin comillas: CREATE TABLE Mascota "
                "crea mascota.",
                "Con **comillas dobles** el nombre se respeta letra a letra, y \"Mascota\" ya no es "
                "mascota.",
                "Regla: minúsculas, **singular**, sin tildes ni eñes, guion bajo y nunca comillas "
                "dobles.",
                "Mismo nombre en diagrama, DDL y Mermaid: cita.id_mascota **apunta** a "
                "mascota.id_mascota.",
            ],
            "notas": {
                "min": 3,
                "explica": "PostgreSQL convierte a minúsculas cualquier nombre escrito sin "
                           "comillas. Por eso la regla del curso es simple: todo en minúsculas, "
                           "singular, sin tildes y sin comillas dobles, y el mismo nombre en el "
                           "diagrama, en el DDL y en el código Mermaid.",
                "pasos": [
                    "CREATE TABLE Mascota crea una tabla llamada mascota: el motor pliega el "
                    "nombre a minúscula.",
                    "SELECT * FROM \"Mascota\" falla: con comillas el nombre se toma letra a letra "
                    "y esa tabla no existe. Error real: relation \"Mascota\" does not exist.",
                    "Las cuatro reglas con su ejemplo: mascota, dueno, detalle_factura, y la FK que "
                    "se lee sola: cita.id_mascota apunta a mascota.id_mascota.",
                ],
                "ejemplo": "El error al revés también existe: CREATE TABLE \"Mascota\" con comillas "
                           "y luego SELECT * FROM mascota responde relation \"mascota\" does not "
                           "exist.",
                "preguntas": [
                    ("¿Por qué singular si la tabla guarda muchas mascotas?",
                     "Porque se nombra por lo que guarda cada fila, y así la FK se lee sola: "
                     "cita.id_mascota."),
                    ("¿Por qué sin eñe?",
                     "Funciona en PostgreSQL, pero complica escribirla en otros teclados, "
                     "herramientas y motores. dueno se escribe igual en cualquier parte."),
                ],
                "cuidado": "El patrón de identificadores es id_<entidad>, con el mismo nombre en la "
                           "tabla propia y en la que la referencia: así el JOIN se escribe sin "
                           "buscar cómo se llamó la columna.",
                "puente": "Con qué herramientas se hace todo esto hoy, y qué demuestra cada una.",
            },
        },
        "Herramientas del dia": {
            "ideas": [
                "Con **draw.io** o Excalidraw se piensa el modelo a mano alzada, sin instalar "
                "nada.",
                "En **DB Fiddle** (PostgreSQL en el navegador) corre el DDL y se ve el error real "
                "del motor.",
                "Un **visor Mermaid** dibuja el texto erDiagram, que se guarda junto al DDL.",
                "DB Fiddle no guarda nada: la **fuente de verdad** es el archivo .sql de la carpeta.",
            ],
            "notas": {
                "min": 2,
                "explica": "Tres herramientas gratuitas, cada una responde una pregunta: ¿cómo es "
                           "el modelo? (draw.io o Excalidraw), ¿el DDL corre? (DB Fiddle, que es "
                           "PostgreSQL real en el navegador) y ¿el diagrama se dibuja? (un visor "
                           "Mermaid).",
                "pasos": [
                    "Recorre las tres cajas de arriba abajo; en la del medio señala el ejemplo: la "
                    "cita con la mascota 999 y el error de FK que se lee en vivo. Cierra con el "
                    "recuadro: DB Fiddle recrea el esquema en cada ejecución, así que lo que vale "
                    "es el archivo .sql guardado en la carpeta del proyecto.",
                ],
                "ejemplo": "La prueba de que el .sql está completo: abrir DB Fiddle vacío, pegar el "
                           "archivo y reconstruir el esquema con sus datos en menos de cinco "
                           "minutos.",
                "preguntas": [
                    ("¿Y Oracle Live SQL?",
                     "Solo como contraste de sintaxis para quien encuentre Oracle en el trabajo. "
                     "El motor del curso es PostgreSQL."),
                ],
                "cuidado": "DB Fiddle no tiene usuarios ni roles reales; los permisos de la Clase 2 "
                           "se practican en PostgreSQL en el navegador con SET ROLE.",
                "puente": "La tercera herramienta merece su lámina: del ER dibujado al código "
                          "Mermaid.",
            },
        },
        "Del ER dibujado al codigo Mermaid": {
            "ideas": [
                "Un ER en **Mermaid** no es una imagen: es texto erDiagram que un visor dibuja al "
                "instante.",
                "Se piensa en un boceto y una **IA** lo traduce; la sintaxis es de la IA, el "
                "modelo es tuyo.",
                "Se **revisa**: entidades completas, cardinalidad bien orientada, PK y FK "
                "marcadas.",
                "Siempre se pega en un **visor**: un diagrama que no renderiza no comunica nada.",
            ],
            "notas": {
                "min": 3,
                "explica": "El diagrama del curso se guarda como texto Mermaid, no como imagen. No "
                           "hace falta dibujar escribiendo código: se piensa en un boceto, una IA "
                           "traduce la sintaxis y uno revisa que el modelo sea el suyo. Al final se "
                           "comprueba en un visor que se dibuje.",
                "pasos": [
                    "El camino: boceto en draw.io o Excalidraw, la IA traduce, sale texto "
                    "erDiagram.",
                    "El texto: dueno ||--o{ mascota : posee se lee «un dueño posee cero o muchas "
                    "mascotas»; dentro de dueno { } van los atributos con su tipo y PK.",
                    "La revisión: entidades completas, cardinalidad en el sentido correcto, PK y "
                    "FK marcadas. «La IA acierta la sintaxis, no tu modelo».",
                    "El visor dibuja el diagrama. Si no renderiza, se corrige ahí mismo.",
                ],
                "ejemplo": "En ||--o{ cada lado es un extremo: || es «exactamente uno» del lado de "
                           "dueno y o{ es «cero o muchos» del lado de mascota.",
                "preguntas": [
                    ("¿Puedo entregar el PNG en vez del texto?",
                     "El PNG sirve para un informe, pero la fuente es el texto: es lo que se "
                     "corrige, se versiona y se compara con el DDL."),
                ],
                "cuidado": "Los nombres del erDiagram deben ser los del DDL: dueno y mascota en "
                           "minúscula, no DUENO ni Dueños. Si difieren, ya no es el mismo modelo.",
                "puente": "Vamos a la demo: todo esto en vivo.",
            },
        },
        "Demo del dia": {
            "ideas": [
                "Crear las tablas con su PK, FK y CHECK, e insertar un dueño, su mascota y una "
                "cita.",
                "Insertar una cita para la mascota **999** y leer el error de clave foránea del "
                "motor.",
                "Pasar el boceto a **erDiagram** y comprobar que los nombres coinciden con el DDL.",
            ],
            "notas": {
                "min": 15,
                "explica": "La demo junta lo de hoy: un boceto, el DDL que corre en PostgreSQL, el "
                           "error de integridad leído en vivo y el mismo modelo pasado a Mermaid.",
                "pasos": [
                    "1) Boceto en draw.io: dueño, mascota y cita con sus claves (3 min). 2) En DB "
                    "Fiddle, el DDL de las tres tablas con PK, FK y CHECK, y los INSERT de Ana "
                    "Pérez, la perra Luna y su cita; corre el JOIN (5 min). 3) Inserta una cita con "
                    "la mascota 999 y lee el error en voz alta: tabla, restricción y DETAIL (2 "
                    "min). 4) Pide a una IA el erDiagram del boceto, pégalo en el visor y compara "
                    "nombres con el DDL (5 min).",
                ],
                "cuidado": "Lleva el script de la demo en un archivo .sql y pégalo: escribirlo en "
                           "vivo consume el tiempo de la parte que importa, que es leer el error. Y "
                           "si la IA devuelve DUENO en mayúsculas, corrígelo frente al grupo: es "
                           "justo el punto de la lámina de convenciones.",
                "puente": "Los cuatro pasos del boceto al código quedan proyectados para la práctica.",
            },
        },
        "Del boceto al": {
            "notas": {
                "min": 2,
                "explica": "Los cuatro pasos para pasar de un diagrama dibujado a uno en texto "
                           "Mermaid. Quedan proyectados mientras el grupo trabaja.",
                "pasos": [
                    "Léelos en orden y subraya dos: en el 2, la IA acierta la sintaxis pero el "
                    "modelo lo revisa cada uno; en el 4, lo que se guarda es el texto Mermaid (la "
                    "fuente), y el PNG es solo para el informe.",
                ],
                "cuidado": "Si alguien pega el código y el visor marca error, casi siempre es un "
                           "nombre con espacio o tilde, o un atributo sin tipo.",
                "puente": "Cerramos.",
            },
        },
        "Clase 1 ·": {
            "notas": {
                "min": 3,
                "explica": "Cierre: hoy la clínica pasó del papel a un modelo con claves, "
                           "relaciones y reglas que el motor defiende solo, y vimos dónde termina "
                           "esa defensa.",
                "pasos": [
                    "Pregunta de salida: «nombren una regla de la clínica que el DDL sí defiende y "
                    "una que no». Respuesta esperada: el stock negativo sí (CHECK); la mascota "
                    "inactiva que agenda no (necesita un procedimiento, que es la Clase 3).",
                ],
                "puente": "La próxima clase: quién puede hacer qué sobre estas tablas (roles y "
                          "privilegios).",
            },
        },
    },
}
