# -*- coding: utf-8 -*-
"""BD II · Clase 11 (Avance del proyecto: revision tecnica): ideas proyectadas y GUION por lamina.

Mismo formato que la Clase 4 en `bd2_contenido_data.py` (ver `notas_guion.py`); se fusiona solo.
Los pasos de cada animacion estan en `config/animaciones/bd2/clase11/<huella>.js`: «Al entrar» es
el primer fotograma y «Clic k» cada uno de los siguientes. En las laminas sin animacion (codigo,
pasos, ilustracion) los pasos llevan su propio rotulo, porque ahi no hay clics.

Las salidas del catalogo se comprobaron en PostgreSQL (PGlite) sobre una base con el modelo
completo: 7 claves foraneas; fn_trg_audit_cita, sp_agendar_cita y sp_facturar como rutinas;
trg_audit_cita como trigger; la mascota 3 (Rocky) inactiva.
"""

CONTENIDO = {
    11: {
        "Encuadre de hoy": {
            "ideas": [
                "**Tema de hoy:** la revisión técnica del avance de la base de la clínica.",
                "Herramienta: **PostgreSQL en el navegador** y un editor de diagramas · Bloque "
                "**120 min**",
                "Gratis + navegador · sin software de pago obligatorio.",
                "Recorrido: teoría del tema, una lámina por concepto, y demo del docente sobre la "
                "base de la clínica.",
                "Cada lámina se sostiene sola: sirve para repasar aunque hayas faltado.",
                "**Conceptos de hoy:** revisión técnica · coherencia entre piezas · verificaciones "
                "cruzadas · control del alcance · el hallazgo útil.",
            ],
            "notas": {
                "min": 4,
                "explica": "Hoy no hay SQL nuevo: hoy se revisa lo construido. Una revisión técnica "
                           "bien hecha encuentra los defectos mientras todavía hay tiempo de "
                           "corregirlos, y deja una lista escrita de qué arreglar.",
                "pasos": [
                    "Lee el tema y pregunta: «si hoy alguien abriera su base sin conocerlos, ¿qué "
                    "sería lo primero que no coincide con lo que dice su diagrama?». Toma dos "
                    "respuestas.",
                    ("Después", "Cierra: «al final cada uno sale con su acta de hallazgos; cada "
                     "hallazgo, demostrado con una ejecución»."),
                ],
                "cuidado": "Esta sesión es doble: la Clase 11 y la 12 van el mismo día. Cuida el "
                           "tiempo de la revisión para que la integración no quede comprimida.",
                "puente": "Primero, qué es una revisión técnica y con qué producto se sale.",
            },
        },
        "Mapa del bloque": {
            "notas": {
                "min": 1,
                "explica": "El recorrido del bloque: teoría con una lámina por concepto, demo de una "
                           "revisión real y práctica opcional.",
                "pasos": ["Señala solo los tramos; no te detengas. La práctica está en la carpeta "
                          "de la clase y es opcional."],
            },
        },
        "Que es una revision tecnica": {
            "ideas": [
                "Una **revisión técnica** busca defectos en un artefacto antes de que cuesten caro.",
                "Tiene cuatro roles: **autor** presenta, **revisores** buscan, **moderador** cuida el "
                "tiempo y **escriba** registra.",
                "Se sale con un producto escrito, el **acta de hallazgos**, no con una nota ni con "
                "un aplauso.",
                "Se revisa el **artefacto**, no la persona, y el problema se registra, no se arregla "
                "en la reunión.",
            ],
            "notas": {
                "min": 5,
                "explica": "Una revisión técnica es una reunión con un solo propósito: encontrar "
                           "defectos en un producto de trabajo mientras todavía es barato "
                           "corregirlos, y salir con una lista escrita. No es una reunión de avance, "
                           "ni una calificación, ni una demostración para lucirse.",
                "pasos": [
                    "El objetivo arriba y el artefacto al centro: puede ser el ER, el script DDL, la "
                    "matriz de roles o un procedimiento. Todo gira alrededor del producto, no de "
                    "quien lo hizo.",
                    "Los cuatro roles: el autor presenta y responde, los revisores buscan defectos, "
                    "el moderador cuida tiempo y tono, el escriba anota cada hallazgo. Entre dos "
                    "personas, una hace de autor y la otra de revisor y escriba.",
                    "El producto es el acta de hallazgos. Si de la reunión no sale nada escrito, no "
                    "hubo revisión: hubo conversación.",
                    "Las dos reglas, dichas antes de empezar: se revisa el artefacto y no la "
                    "persona, y el problema no se arregla dentro de la revisión. Quien se pone a "
                    "corregir el DDL en vivo consume el tiempo de todos.",
                ],
                "ejemplo": "El estándar IEEE 1028 distingue la inspección (formal, con lista de "
                           "verificación y métricas), el walkthrough (el autor guía) y la revisión "
                           "técnica (los pares evalúan si el artefacto sirve). Hoy se hace una "
                           "revisión técnica con lista de verificación, de unos diez minutos por "
                           "persona.",
                "preguntas": [
                    ("¿Esto tiene nota?",
                     "La revisión no califica el producto: es la última oportunidad de mover puntos "
                     "antes de la entrega. Conviene llegar con lo más flojo, no con lo mejor."),
                    ("¿Si el revisor encuentra fallas me bajan la nota?",
                     "No: el revisor par no califica. Encontrar fallas es el objetivo de la sesión."),
                ],
                "cuidado": "El error típico del docente es convertir la revisión en «va bien, faltan "
                           "detalles»: amable, global y sin nada escrito. Sin acta, los defectos "
                           "llegan intactos a la entrega final.",
                "puente": "¿Qué se revisa en una base de datos? No cada pieza: la coherencia entre "
                          "ellas.",
            },
        },
        "Lo que se audita es la coherencia": {
            "ideas": [
                "Un **artefacto** es cualquier producto de trabajo: el ER, el DDL, la matriz de "
                "roles, los procedimientos, el informe.",
                "Cada pieza puede estar bien sola y aun así describir, junto a otra, **bases "
                "distintas**.",
                "El caso más común: el ER se dibujó al inicio y el DDL se fue **parchando** sin "
                "actualizarlo.",
                "Por eso se corren **cuatro verificaciones cruzadas**, cada una entre dos piezas.",
            ],
            "notas": {
                "min": 5,
                "explica": "En una base de datos no se audita cada pieza por separado sino la "
                           "coherencia entre piezas: que todas describan el mismo sistema. Un ER bien "
                           "dibujado y un DDL que ejecuta sin errores pueden describir dos bases "
                           "distintas, y ninguna de las dos piezas «falla» por sí sola.",
                "pasos": [
                    "Las cinco piezas del proyecto, cada una con su visto: el ER, el DDL, la matriz "
                    "de roles, los procedimientos y el informe de optimización. Revisadas solas, "
                    "todas pasan.",
                    "El enlace entre el ER y el DDL se rompe: el diagrama se dibujó en la Clase 1 y "
                    "el DDL se parchó en las Clases 3 a 8 (una tabla de auditoría, una columna "
                    "nueva) sin volver al diagrama. Es el hallazgo más común y el más fácil de "
                    "encontrar si se sabe dónde mirar.",
                    "Las cuatro verificaciones cruzadas, cada una entre dos piezas: el ER contra el "
                    "DDL, la matriz de roles contra los GRANT, los procedimientos contra una llamada "
                    "real y el informe contra el EXPLAIN de antes y después. Cada una toma dos o "
                    "tres minutos.",
                    "La frase de la lámina: se audita la coherencia entre piezas, no cada pieza.",
                ],
                "ejemplo": "La tabla audit_cita apareció en la Clase 4 con su trigger. Si el ER no "
                           "la tiene, el DDL describe una base con una tabla más que el diagrama: "
                           "hallazgo de coherencia, aunque las dos piezas estén bien hechas.",
                "preguntas": [
                    ("¿Y si el DDL es el correcto y el ER el viejo?",
                     "Entonces se actualiza el ER: la fuente de verdad es lo que corre. El hallazgo "
                     "es que no coinciden, no cuál de los dos tiene la culpa."),
                ],
                "cuidado": "No aceptes como evidencia lo que el autor dice («sí, está "
                           "actualizado»): pide abrir las dos piezas lado a lado.",
                "puente": "Las dos primeras verificaciones, en detalle.",
            },
        },
        "Verificaciones uno y dos": {
            "ideas": [
                "De ida, cada entidad del ER debe tener su CREATE TABLE: una **entidad sin tabla** "
                "es un hallazgo.",
                "De vuelta, una **tabla sin entidad** también lo es, y es la revisión que casi nadie "
                "hace.",
                "Una cardinalidad dibujada debe existir como **NOT NULL y REFERENCES** en el DDL.",
                "Verificación dos: cada celda de la **matriz de roles** debe verse en un GRANT, y "
                "nada más.",
            ],
            "notas": {
                "min": 6,
                "explica": "La verificación uno compara el diagrama con el script en los dos "
                           "sentidos y después mira las relaciones. La verificación dos compara la "
                           "matriz de roles de la Clase 2 con los GRANT que de verdad se ejecutaron.",
                "pasos": [
                    "De ida: se recorre el ER entidad por entidad buscando su CREATE TABLE. Dueño, "
                    "mascota y cita lo tienen; insumo no: entidad sin tabla.",
                    "De vuelta: el script tiene CREATE TABLE proveedor y el ER no tiene esa entidad. "
                    "El modelo creció sin registrarse, y es el sentido que nadie revisa.",
                    "Las relaciones: si el ER dice que una cita pertenece a exactamente una mascota, "
                    "el DDL debe tener id_mascota INT NOT NULL y REFERENCES mascota(id_mascota). Si "
                    "dice que un dueño tiene varias mascotas, la clave foránea vive en mascota, no "
                    "en dueño. Una cardinalidad sin restricción es decoración.",
                    "Verificación dos: la matriz dice que el auditor solo lee cita, pero el script "
                    "le dio GRANT SELECT, INSERT, UPDATE ON cita TO auditor. Pasa cuando se copia el "
                    "bloque de recepción y solo se cambia el nombre del rol.",
                ],
                "ejemplo": "La consulta del catálogo que lista las claves foráneas devuelve 7 filas "
                           "en la base completa del curso: una por cada relación del ER (cita con "
                           "mascota y con veterinario, mascota con dueño, consulta con cita, factura "
                           "con consulta y detalle_factura con factura y con insumo).",
                "preguntas": [
                    ("¿Cómo veo los privilegios reales de un rol?",
                     "Con el catálogo: SELECT grantee, table_name, privilege_type FROM "
                     "information_schema.role_table_grants WHERE grantee = 'auditor'; con el GRANT "
                     "del ejemplo devuelve tres filas: INSERT, SELECT y UPDATE sobre cita."),
                    ("¿Una FK sin NOT NULL está mal?",
                     "Depende de la cardinalidad: sin NOT NULL la relación es opcional. Si el ER "
                     "dice «exactamente una», falta el NOT NULL."),
                ],
                "cuidado": "Revisar solo de ida deja pasar las tablas que crecieron sin diagrama, "
                           "que son justo las que la sustentación pregunta.",
                "puente": "La verificación tres separa a quien va bien de quien no: que compile no "
                          "es que sirva.",
            },
        },
        "Verificacion tres": {
            "ideas": [
                "Un procedimiento que **compila** no es un procedimiento que **funciona**: se piden "
                "dos ejecuciones.",
                "El **caso válido** inserta la cita, y el **caso inválido** declarado responde con "
                "su mensaje de negocio.",
                "Verificación cuatro: una optimización se demuestra con el **plan antes y después**.",
                "Un índice que ninguna consulta usa es un **hallazgo**, no un avance.",
            ],
            "notas": {
                "min": 5,
                "explica": "Las verificaciones tres y cuatro piden ejecuciones, no afirmaciones. Un "
                           "procedimiento se prueba con dos llamadas: una que debe pasar y una que "
                           "debe ser rechazada. Una optimización se prueba con el plan de ejecución "
                           "de antes y de después.",
                "pasos": [
                    "CREATE PROCEDURE sp_agendar_cita(…) compiló. Eso solo dice que la sintaxis es "
                    "correcta; todavía no se sabe si la regla funciona.",
                    "Caso válido: CALL sp_agendar_cita(1, 2, …) con una mascota activa (Firulais) y "
                    "una franja libre: inserta la cita.",
                    "Caso inválido declarado: CALL sp_agendar_cita(3, 2, …) con Rocky, que está "
                    "inactiva: el procedimiento aborta con «ERROR: la mascota 3 esta inactiva; no "
                    "se agenda cita» y no inserta nada. Si el autor no puede mostrar esta segunda "
                    "ejecución, el procedimiento no tiene manejo de errores.",
                    "Verificación cuatro: se pide la consulta, el plan de antes (Seq Scan on cita), "
                    "el cambio aplicado y el plan de después (Index Scan using idx_cita_fecha_hora "
                    "on cita). Sin medición, el informe es una opinión; y un índice que ninguna "
                    "consulta aprovecha se anota como hallazgo.",
                ],
                "ejemplo": "Un sp_agendar_cita que compila pero no valida la mascota inactiva pasa "
                           "la primera llamada y también la segunda: inserta la cita de Rocky, que "
                           "debía rechazarse. Solo la segunda ejecución lo delata.",
                "preguntas": [
                    ("¿Cómo confirmo que el caso inválido no dejó nada?",
                     "Con SELECT COUNT(*) FROM cita; antes y después: el número no cambia."),
                    ("¿El plan de después siempre muestra Index Scan?",
                     "No necesariamente: con pocas filas el planificador puede preferir Seq Scan "
                     "aunque el índice exista. Lo que se exige es la medición y que el informe "
                     "explique lo que muestra."),
                ],
                "cuidado": "No marques en verde un procedimiento porque el autor dice que funciona: "
                           "pide la ejecución del caso inválido en pantalla.",
                "puente": "Las verificaciones en SQL: el catálogo responde qué existe de verdad.",
            },
        },
        "La bateria de verificacion del avance": {
            "notas": {
                "min": 4,
                "explica": "El catálogo de la base, information_schema, responde con datos qué "
                           "tablas existen y cuáles tienen clave primaria. Así se verifica el DDL "
                           "sin leerlo línea por línea.",
                "pasos": [
                    ("Líneas 1-3", "Lista las tablas del esquema public en orden alfabético. En una "
                     "base con el modelo completo y la auditoría aparecen 9: audit_cita, cita, "
                     "consulta, detalle_factura, dueno, factura, insumo, mascota y veterinario. "
                     "Cualquier otra es una tabla sin entidad que revisar."),
                    ("Líneas 5-10", "Une cada tabla con sus restricciones PRIMARY KEY mediante LEFT "
                     "JOIN y se queda con las que no encontraron ninguna (c.constraint_name IS "
                     "NULL)."),
                    ("Línea 11", "Cero filas significa que todas las tablas tienen clave primaria. "
                     "Cada fila que aparezca es un hallazgo."),
                ],
                "ejemplo": "En la base completa del curso la segunda consulta devuelve 0 filas: "
                           "todas las tablas, incluida audit_cita, tienen su clave primaria.",
                "preguntas": [
                    ("¿Por qué LEFT JOIN y no JOIN?",
                     "Porque se buscan las tablas que NO tienen PK: un JOIN las descartaría; el LEFT "
                     "JOIN las conserva con NULL en las columnas de la restricción, y el WHERE … IS "
                     "NULL las deja solas."),
                    ("¿information_schema es de PostgreSQL?",
                     "Es del estándar SQL: también existe en MySQL y SQL Server. PostgreSQL tiene "
                     "además su catálogo propio, pg_catalog."),
                ],
                "cuidado": "Corre las consultas sobre la base que el autor va a entregar, no sobre "
                           "una copia de prueba: el catálogo describe la base en la que se ejecuta.",
                "puente": "Una revisión también encuentra lo contrario de lo que falta: lo que "
                          "sobra.",
            },
        },
        "Scope creep": {
            "ideas": [
                "**Scope creep** es agregar funcionalidad sin que nadie lo decida y sin quitar nada "
                "a cambio.",
                "En una base de datos se mide en **entidades**, y el rango sano a esta altura es de "
                "6 a 9.",
                "Quince entidades no es ir adelantado: es el mismo esfuerzo en el **doble de "
                "superficie**.",
                "Las que sobran pasan a **alcance futuro** del informe, con la razón por la que "
                "quedaron fuera.",
            ],
            "notas": {
                "min": 4,
                "explica": "Scope creep es el crecimiento no controlado del alcance: se agregan "
                           "cosas sin decidirlo y sin quitar nada. En un proyecto de base de datos "
                           "tiene un síntoma que se cuenta: el número de entidades.",
                "pasos": [
                    "El mínimo son seis entidades (dueño, mascota, veterinario, cita, insumo y "
                    "factura con su detalle) y el rango sano llega a nueve con una o dos "
                    "ampliaciones justificadas, como consulta o un historial clínico. El modelo del "
                    "curso tiene 8 tablas: dentro del rango.",
                    "Se agregan proveedores, inventario multialmacén, portal de dueños, "
                    "notificaciones… y se llega a 15. Nadie decidió agregarlas y nada se quitó a "
                    "cambio.",
                    "Mismo esfuerzo, el doble de superficie: se termina con quince tablas vacías en "
                    "vez de ocho con procedimientos probados. La acción va al acta: las sobrantes "
                    "pasan a una sección de alcance futuro, con su porqué.",
                ],
                "ejemplo": "Un hallazgo bien escrito: «Artefacto: ER. Observación: 15 entidades, 7 "
                           "sin procedimientos ni datos. Acción: mover proveedor, almacén, portal y "
                           "notificación a alcance futuro.»",
                "preguntas": [
                    ("¿Mover entidades a alcance futuro no se ve mal?",
                     "Al contrario: declarar el límite con su razón es señal de madurez y se valora "
                     "al sustentar."),
                ],
                "cuidado": "Existe el problema inverso: quien recortó tanto que ya no tiene material "
                           "para procedimientos, funciones y triggers. También se escribe como "
                           "hallazgo.",
                "puente": "¿Cómo se escribe un hallazgo para que sirva? Tiene una anatomía fija.",
            },
        },
        "La anatomia fija de la retroalimentacion": {
            "ideas": [
                "«El modelo está flojo, mejórenlo» no sirve, porque no dice **qué mirar** ni cuándo "
                "queda resuelto.",
                "Un hallazgo útil tiene cinco partes: **artefacto, observación, impacto, acción y "
                "responsable con fecha**.",
                "La diferencia es la **verificabilidad**: cualquiera puede comprobar que el hallazgo "
                "se cerró.",
                "Se escriben de **3 a 5** hallazgos por persona, los de más peso primero.",
            ],
            "notas": {
                "min": 5,
                "explica": "La retroalimentación útil se escribe siempre con la misma forma, para "
                           "que el acta sea una lista de tareas y no un desahogo. Cada hallazgo dice "
                           "qué pieza, qué se observó, por qué importa, qué hacer y quién lo hace "
                           "para cuándo.",
                "pasos": [
                    "La versión inútil: «el modelo está flojo, mejórenlo». No dice qué mirar ni cómo "
                    "saber cuándo está resuelto.",
                    "La versión accionable, parte por parte: artefacto, el script DDL; observación, "
                    "detalle_factura no tiene FOREIGN KEY hacia insumo aunque el ER dibuja la "
                    "relación; impacto, se pueden insertar detalles con insumos que no existen; "
                    "acción, agregar la restricción y re-ejecutar el script completo desde cero; "
                    "responsable y fecha, el autor, antes de la próxima sesión.",
                    "La diferencia no es cortesía, es verificabilidad. Y la dosis: de tres a cinco "
                    "hallazgos por persona; más de cinco desmoraliza y nadie los cierra, menos de "
                    "tres suele ser una revisión superficial.",
                ],
                "ejemplo": "La observación se prueba con SQL: INSERT INTO detalle_factura "
                           "(id_factura, id_insumo, cantidad, precio_unit) VALUES (1, 999, 1, 1000); "
                           "si entra, falta la FK; si responde «violates foreign key constraint», el "
                           "hallazgo está cerrado.",
                "preguntas": [
                    ("¿Por qué re-ejecutar todo el script desde cero?",
                     "Porque un ALTER aplicado a mano en la base de uno no queda en el script: la "
                     "prueba de que quedó es que el script completo corra limpio en una base vacía."),
                ],
                "cuidado": "La observación tiene que ser verificable: «la FK no existe» se comprueba; "
                           "«el modelo está raro», no.",
                "puente": "¿Y si la revisión no encuentra nada? Entonces se desperdició.",
            },
        },
        "Un checkpoint sin hallazgos": {
            "ideas": [
                "El único valor de un **checkpoint** es que todavía hay tiempo para corregir.",
                "Con hallazgos escritos, el defecto se **corrige a tiempo**, antes de la entrega.",
                "«Todo bien, sigan así» hace que se deje de revisar y el defecto **llega a la "
                "entrega**.",
                "Revisar el trabajo de otro ayuda: los **defectos ajenos** se ven más rápido que los "
                "propios.",
            ],
            "notas": {
                "min": 4,
                "explica": "Un punto de control intermedio solo vale si de él sale una lista de "
                           "cosas por corregir mientras aún hay clases para hacerlo. Un «todo bien» "
                           "no ahorra trabajo: lo aplaza al momento en que ya no se puede arreglar.",
                "pasos": [
                    "La línea del tiempo: checkpoint y entrega. Entre los dos, la franja verde es el "
                    "tiempo que queda para corregir.",
                    "Con hallazgos concretos: el defecto aparece en el checkpoint, se anota y se "
                    "corrige dentro de esa franja.",
                    "Con «todo bien, sigan así»: el estudiante entiende, con razón, que su trabajo "
                    "está aprobado; deja de revisarlo y el defecto llega intacto a la entrega, "
                    "cuando ya no hay tiempo. Es un costo diferido, no un ahorro.",
                ],
                "ejemplo": "La revisión entre pares tiene un beneficio propio: quien revisa casi "
                           "siempre vuelve a su carpeta y arregla en silencio el mismo problema que "
                           "acaba de señalar.",
                "preguntas": [
                    ("¿Llego con lo mejor o con lo peor?",
                     "Con lo peor: es lo que la revisión puede arreglar. Esconder la parte floja es "
                     "perder justo la ayuda que se vino a buscar."),
                ],
                "cuidado": "Convertir el checkpoint en una clase de repaso porque incomoda no tener "
                           "tema nuevo: el tiempo se va explicando y nadie sale con su acta, que era "
                           "el producto del día.",
                "puente": "Para que los hallazgos salgan de datos y no de opiniones: más consultas "
                          "al catálogo.",
            },
        },
        "Integridad y objetos de negocio": {
            "notas": {
                "min": 4,
                "explica": "Dos verificaciones más con el catálogo: qué claves foráneas existen y "
                           "qué procedimientos, funciones y triggers hay de verdad en la base, no en "
                           "el informe.",
                "pasos": [
                    ("Líneas 1-9", "Une las restricciones FOREIGN KEY con la columna que las lleva "
                     "(key_column_usage) y con la tabla a la que apuntan (constraint_column_usage). "
                     "En la base completa devuelve 7 filas: cita→veterinario, cita→mascota, "
                     "consulta→cita, detalle_factura→factura, detalle_factura→insumo, "
                     "factura→consulta y mascota→dueno."),
                    ("Líneas 11-13", "information_schema.routines lista lo que existe con su tipo: "
                     "con el avance completo aparecen fn_trg_audit_cita (FUNCTION), sp_agendar_cita "
                     "y sp_facturar (PROCEDURE)."),
                    ("Línea 14", "information_schema.triggers devuelve trg_audit_cita sobre cita. "
                     "Un trigger aparece una vez por cada evento que lo dispara; este solo escucha "
                     "UPDATE."),
                ],
                "ejemplo": "Si el informe dice «tres procedimientos» y routines devuelve dos, el "
                           "tercero está en un archivo y no en la base: hallazgo.",
                "preguntas": [
                    ("¿Por qué la función del trigger aparece como FUNCTION?",
                     "Porque en PostgreSQL el trigger son dos objetos: la función RETURNS TRIGGER, "
                     "que es una rutina más, y la asociación CREATE TRIGGER, que está en "
                     "information_schema.triggers."),
                ],
                "cuidado": "La consulta de claves foráneas une solo por nombre de restricción: una "
                           "FK de dos columnas aparecería repetida. En el modelo del curso todas son "
                           "de una columna.",
                "puente": "Ahora todo esto en la demo.",
            },
        },
        "Demo del dia": {
            "ideas": [
                "Cada hallazgo sale de una **ejecución**: el catálogo, el CALL válido y el CALL "
                "inválido.",
                "El ER se compara con el **DDL real**, en los dos sentidos.",
                "Cada hallazgo se escribe con sus **cinco partes**: artefacto, observación, impacto, "
                "acción y responsable.",
            ],
            "notas": {
                "min": 15,
                "explica": "La demo es una revisión real de diez minutos sobre una base completa: el "
                           "docente hace de revisor, ejecuta las verificaciones y escribe los "
                           "hallazgos en vivo con sus cinco partes.",
                "pasos": [
                    ("1 · Catálogo", "Ejecuta las consultas de las dos láminas de código: tablas, "
                     "tablas sin PK (0 filas), claves foráneas (7) y rutinas y triggers. Compara "
                     "cada resultado con el ER."),
                    ("2 · Procedimiento", "CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-11-05 "
                     "10:00:00') inserta; CALL sp_agendar_cita(3, 2, TIMESTAMP '2026-11-05 "
                     "09:00:00') responde «ERROR: la mascota 3 esta inactiva; no se agenda cita». "
                     "Muestra SELECT COUNT(*) FROM cita antes y después de la segunda."),
                    ("3 · Hallazgo", "Escribe un hallazgo completo en el acta, en voz alta, parte "
                     "por parte. Si la base no tiene ninguno real, usa el de detalle_factura sin FK "
                     "y pruébalo con el INSERT del insumo 999."),
                    ("4 · Cierre", "Muestra el acta terminada: de 3 a 5 hallazgos, cada uno con "
                     "responsable y fecha."),
                ],
                "ejemplo": "Tiempos sugeridos: catálogo 5 min, procedimiento 4 min, hallazgo 4 min, "
                           "cierre 2 min.",
                "preguntas": [
                    ("¿Y si la base del estudiante no corre?",
                     "Ese es el primer hallazgo, y el más grave: sin un script que corra de "
                     "principio a fin en una base vacía no hay sobre qué montar lo demás."),
                ],
                "cuidado": "No corrijas en vivo lo que encuentres: anótalo. Corregir dentro de la "
                           "revisión es la regla que más se rompe.",
                "puente": "Para el ER del avance: del boceto al código Mermaid.",
            },
        },
        "Del boceto al codigo Mermaid": {
            "notas": {
                "min": 3,
                "explica": "El diagrama se entrega como texto Mermaid, no como imagen: la imagen "
                           "sale del código. Se piensa dibujando, se traduce a texto, se comprueba "
                           "que dibuje y se guardan las dos cosas.",
                "pasos": [
                    ("Paso 1", "Diseña visual: en Excalidraw o draw.io arrastrar cajas es más "
                     "rápido, y ahí se piensa el modelo."),
                    ("Paso 2", "Traduce con IA: pide el código erDiagram a partir del boceto. "
                     "Revisa el resultado: la IA acierta la sintaxis, no el modelo; los nombres "
                     "tienen que ser los del DDL."),
                    ("Paso 3", "Renderiza y corrige en un visor Mermaid (mermaid.live): si no "
                     "dibuja, no comunica."),
                    ("Paso 4", "Guarda el texto Mermaid, que es la fuente, y exporta el PNG."),
                ],
                "ejemplo": "Una relación en erDiagram: dueno ||--o{ mascota : tiene (un dueño, cero "
                           "o muchas mascotas). Cada entidad lleva sus atributos con tipo y PK o FK: "
                           "int id_mascota PK.",
                "preguntas": [
                    ("¿Por qué no basta una imagen del diagrama?",
                     "Porque el texto se puede revisar, comparar con el DDL y versionar; una imagen "
                     "no se corrige sin volver a dibujarla."),
                ],
                "cuidado": "Revisa que los nombres del erDiagram sean exactamente los del DDL "
                           "(dueno, no Dueño): un diagrama que no coincide con el script es justo el "
                           "hallazgo de coherencia de hoy.",
                "puente": "Cierre de la clase.",
            },
        },
        "Clase 11 ·": {
            "notas": {
                "min": 3,
                "explica": "Cierre: una revisión sirve si sale un acta con hallazgos verificables. "
                           "Lo que se audita es la coherencia entre piezas, y cada hallazgo se "
                           "demuestra con una ejecución.",
                "pasos": [
                    "Pregunta de salida: «nombra un hallazgo de tu propia base con sus cinco "
                    "partes». Toma dos respuestas y corrige la que no sea verificable.",
                    ("Después", "Amarre: la Clase 12, en esta misma sesión, escribe el contrato de "
                     "operaciones, que solo puede apoyarse en procedimientos que existen y "
                     "funcionan."),
                ],
            },
        },
    },
}
