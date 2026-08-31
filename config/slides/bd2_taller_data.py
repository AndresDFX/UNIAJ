# -*- coding: utf-8 -*-
"""Taller ampliado + soluciones BD II / VetCare (PRIVADO)."""

HERRAMIENTAS_DIA = {
    1: [
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'ER VetCare',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'DDL demo',
        },
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Playground',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Ficha del PI',
        },
        {
            'name': 'Mermaid',
            'logo': 'mermaid.png',
            'note': 'Codigo del ER',
        },
        {
            'name': 'ExamLab',
            'logo': 'examlab.png',
            'note': 'Donde se entrega',
        },
    ],
    2: [
        # ExamLab primero a proposito: es el unico de los tres donde CREATE ROLE y
        # GRANT corren de verdad y donde se califica. Live SQL queda como contraste
        # de sintaxis, no como sitio de trabajo (ver el fundamento de la clase).
        {
            'name': 'ExamLab',
            'logo': 'examlab.png',
            'note': 'PostgreSQL: aqui corre',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Matriz y politica',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'Alterno: SQL suelto',
        },
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Solo contraste',
        },
    ],
    3: [
        # ExamLab primero: el taller es PL/pgSQL y los 100 puntos se califican ahi.
        # Live SQL no puede ejecutar nada de hoy —es PL/SQL de Oracle— y queda solo
        # como contraste de sintaxis (ver el fundamento de la clase).
        {
            'name': 'ExamLab',
            'logo': 'examlab.png',
            'note': 'PL/pgSQL: aqui corre',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Contrato del proc',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'Alterno: PostgreSQL',
        },
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Solo contraste',
        },
    ],
    4: [
        # Igual que en la Clase 3: la funcion, los dos triggers y sus pruebas corren
        # en ExamLab. Lo unico que NO se ejecuta es el respaldo (pg_dump y compania
        # necesitan sistema de archivos): la pregunta 5 es un documento.
        {
            'name': 'ExamLab',
            'logo': 'examlab.png',
            'note': 'Funcion y triggers',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Plan de respaldo',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'Alterno: PostgreSQL',
        },
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Solo contraste',
        },
    ],
    6: [
        # ExamLab primero, y ExamLab no estaba en esta lista: los 100 puntos del taller se
        # califican ahi y es el unico entorno del kit que trae la base CON VOLUMEN
        # (30.010 citas, ANALYZE corrido, sin indices). Medir un antes/despues en una base
        # de 20 filas no mide nada, asi que la herramienta no es un detalle de logistica.
        # SQLTest.online sale: su gracia es comparar motores, y hoy el motor es uno.
        # DB Fiddle sale por la misma razon, y con una consecuencia peor: figuraba como
        # «alterno: SQL suelto», pero ahi no existe la base sembrada, asi que el
        # estudiante que la use mide sobre otros datos y sus numeros no pueden coincidir
        # con el plan que la rubrica exige «tomado del plan real» -- el `Rows Removed by
        # Filter: 29919` y las 91 filas. Un alterno que cuesta puntos no es un alterno.
        {
            'name': 'ExamLab',
            'logo': 'examlab.png',
            'note': 'PostgreSQL con volumen',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Justificacion',
        },
    ],
    # Igual que en la Clase 6: DB Fiddle queda fuera. Los 100 puntos se califican sobre la
    # base sembrada de 30.010 citas, que solo existe en ExamLab; quien mida en DB Fiddle no
    # puede reproducir el cambio de plan ni el reparto de particiones que pide la rubrica.
    # draw.io tambien sale: el diagrama de tabla caliente es un boceto de pizarra del
    # docente, no un entregable, y anunciarlo aqui hacia que el estudiante buscara donde
    # subirlo.
    7: [
        {
            'name': 'ExamLab',
            'logo': 'examlab.png',
            'note': 'PostgreSQL: 30.010 citas',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Tabla de justificacion',
        },
    ],
    # Oracle Live SQL encabezaba esta lista y las tres preguntas de SQL del dia --75 de los
    # 100 puntos-- son PL/pgSQL: `CALL`, `GET DIAGNOSTICS ... ROW_COUNT`, `RAISE EXCEPTION`
    # y una funcion que devuelve BOOLEAN. Alli no compila ninguna. Se queda al final porque
    # el contraste con Oracle SI se ensena (es la pregunta 4), pero como contraste.
    8: [
        {
            'name': 'ExamLab',
            'logo': 'examlab.png',
            'note': 'PL/pgSQL: aqui corre',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Checklist de tuning',
        },
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Solo contraste (pregunta 4)',
        },
    ],
    10: [
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Escenarios T1/T2',
        },
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Demo SQL',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'Pruebas',
        },
    ],
    11: [
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Demo procs',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'ER',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'DDL',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Checklist',
        },
    ],
    12: [
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Contrato app-BD',
        },
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Ops',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Flujo',
        },
    ],
    13: [
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Caso real',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Leccion',
        },
        {
            'name': 'DB Fiddle',
            'logo': 'dbfiddle.png',
            'note': 'Opcional SQL',
        },
    ],
    15: [
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Informe final',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'ER final',
        },
        {
            'name': 'Oracle Live SQL',
            'logo': 'oracle_livesql.png',
            'note': 'Demo SQL',
        },
    ],
}

TALLER_BLOQUE = {
    1: {
        'contexto': [
            '@@Por qué importa al PI VetCare:@@ sin ER/alcance no hay base para procs ni seguridad.',
            'Hoy cierras dominio + entidades mínimas + reglas de negocio propias.',
            'El DDL demo (Codigo/) es semilla; tu ER manda.',
        ],
        'objetivo': 'Arrancar VetCare: ficha + ER borrador + entidades/reglas.',
        'criterios': [
            'Proyecto nombrado y registrado.',
            'ER PNG con entidades mínimas.',
            '3 reglas de negocio propias.',
            'Alcance SI/NO 5-8 lineas.',
            'Entrega domingo 23:59.',
        ],
        'escenario': [
            'Cliente: Clínica Veterinaria «Huellitas» · Sistema: VetCare DB (la base de datos).',
            'Ficha con plantilla fija: VetCare - [Apellido], alcance SI / NO y 3 reglas Condición → Acción.',
            'Diagrama: boceto visual en Excalidraw o draw.io → código Mermaid (erDiagram) → ExamLab.',
            'Nombres en minúscula y singular (dueno, mascota, cita) con id_<entidad>: iguales en ER, DDL y Mermaid.',
        ],
        'pistas': [
            '□ El proyecto se llama VetCare - [Apellido]?',
            '□ Las 3 reglas están escritas como Condición → Acción?',
            '□ El Mermaid renderiza dentro de ExamLab (no basta el PNG)?',
            '□ Hay PK/FK visibles en el ER?',
            '□ Mascota inactiva / stock aparecen como regla?',
            '□ El alcance evita scope infinito?',
        ],
    },
    2: {
        # Los nombres de rol van en minúscula y el del veterinario con sufijo `_rol`,
        # exactamente como los pide ExamLab y como los verifica la solución docente:
        # antes decían ADMIN_BD/VETERINARIO y el estudiante escribía en el script un
        # nombre distinto del que la rúbrica busca.
        'contexto': [
            '@@Por qué importa al PI:@@ la seguridad de VetCare DB es un criterio de la '
            'rúbrica, y la evidencia son los roles y su matriz — no una promesa.',
            'Mínimo privilegio evita que Recepción borre historia clínica: cancelar una '
            'cita es un @@UPDATE de estado@@, nunca un DELETE.',
            'Los `GRANT` de hoy corren de verdad y se auditan con `information_schema`: la '
            'matriz que entregas tiene que decir lo mismo que ejecutó el motor.',
        ],
        'objetivo': 'Los 4 roles de VetCare creados y verificados, más la matriz rol x objeto '
                    'y la política de altas y bajas.',
        'criterios': [
            'Los 4 roles creados, con sus GRANT y el REVOKE explícito de DELETE.',
            'La matriz real consultada con `information_schema.role_table_grants`.',
            'Vista `v_agenda_recepcion` sin el email + `GRANT SELECT (id_dueno, nombre)`.',
            'Matriz de 10 objetos x 4 roles, sin celdas vacías y consistente con los GRANT.',
            'Política de 1 página con las 5 secciones, cada una con responsable y plazo.',
            'Entrega domingo 23:59.',
        ],
        'escenario': [
            'Esquema de VetCare ya creado y poblado: 8 tablas, y los dos procedimientos '
            '(`sp_agendar_cita`, `sp_facturar`) como objetos de la matriz.',
            'Roles a crear: `admin_bd` · `recepcion` · `veterinario_rol` · `auditor` '
            '(minúsculas; el del veterinario lleva `_rol` porque `veterinario` ya es una tabla).',
            '@@Motor:@@ PostgreSQL dentro de ExamLab. Los GRANT son reales, y el permiso negado '
            'se comprueba con `SET ROLE` en la misma sesión: no hay una segunda conexión.',
            'La matriz y la política se escriben en Google Docs y se pegan en ExamLab; la '
            'plantilla en blanco de las dos está en este documento.',
        ],
        'pistas': [
            '□ ¿Los 4 roles con el nombre exacto, en minúscula y con `veterinario_rol`?',
            '□ ¿`recepcion` sin DELETE en ninguna tabla, y el REVOKE escrito aunque sea redundante?',
            '□ ¿`auditor` solo con SELECT?',
            '□ ¿La vista deja fuera el email, y `column_privileges` devuelve exactamente 2 filas?',
            '□ ¿La matriz tiene las 10 filas llenas y los `sp_` con E, no con S ni I?',
            '□ ¿La política dice quién aprueba y en cuánto tiempo, y trae la prueba negativa con `SET ROLE`?',
        ],
    },
    3: {
        # El taller se resuelve en PL/pgSQL dentro de ExamLab, no en Oracle Live SQL:
        # los 100 puntos se califican contra sintaxis de PostgreSQL y la rúbrica
        # descuenta `VARCHAR2`, `RAISE_APPLICATION_ERROR` y la barra `/` final.
        # Las pistas cubren las 5 preguntas, no las primeras.
        'contexto': [
            '@@Por qué importa al PI:@@ la regla de negocio deja de vivir en la pantalla y '
            'queda dentro de la base, donde vale para @@cualquier@@ cliente que se conecte.',
            'Un procedimiento probado es la única forma de que «una mascota inactiva no '
            'agenda» siga siendo cierto cuando aparezcan la app, un script de carga y soporte.',
            'El contrato que escribes hoy es lo que la Clase 12 le entrega a quien programe '
            'la aplicación: firma, errores y qué hacer con cada uno.',
        ],
        'objetivo': 'Dos procedimientos de negocio en PL/pgSQL corriendo en ExamLab, su batería '
                    'de pruebas con evidencia, y el contrato de los dos documentado.',
        'criterios': [
            '`sp_agendar_cita` con sus 3 parámetros y sus 3 validaciones, cada una con su '
            '`RAISE EXCEPTION` y su mensaje literal.',
            'Batería de 4 bloques `DO` que @@no aborta el script@@ y escribe 4 filas en '
            '`resultado_prueba` con el `SQLERRM` real.',
            'El `COUNT(*)` de `cita` demuestra que pasó de @@10 a 11@@ filas: las tres '
            'validaciones no insertaron nada.',
            '`sp_registrar_consulta` detectando la consulta duplicada con `EXISTS` @@antes@@ '
            'de chocar contra el `UNIQUE`.',
            'Contrato de los dos procedimientos con sus 6 bloques y la tabla de errores '
            'completa (7 filas); las firmas coinciden con el código entregado.',
            'Entrega domingo 23:59.',
        ],
        'escenario': [
            'Esquema de VetCare ya creado y poblado: @@8 mascotas@@ —la @@3 (Rocky)@@ y la '
            '@@8 (Kiara)@@ están @@INACTIVAS@@—, 4 veterinarios y 10 citas.',
            'Ya existe una cita del @@veterinario 1@@ el `2026-09-01 08:00:00`: es la que '
            'dispara la validación de veterinario ocupado.',
            '@@Motor:@@ PostgreSQL dentro de ExamLab. El molde es `CREATE PROCEDURE ... '
            'LANGUAGE plpgsql AS $proc$ ... $proc$;` — no hay `IS`, ni `VARCHAR2`, ni `/` final.',
            'El contrato se escribe en Google Docs y se pega en la pregunta 5; la plantilla '
            'en blanco de sus 6 bloques y de la tabla de errores está en este documento.',
        ],
        'pistas': [
            '□ ¿El procedimiento se creó @@y@@ el `CALL` corrió? Crear no es evidencia.',
            '□ ¿La validación de «no existe» usa `IF NOT FOUND` tras el `SELECT ... INTO`?',
            '□ ¿Los 4 bloques `DO` capturan la excepción y el script llega hasta el final?',
            '□ ¿El conteo final de `cita` es @@11@@, y está en la evidencia?',
            '□ ¿`sp_registrar_consulta` inserta la consulta @@y@@ deja la cita en `ATENDIDA`?',
            '□ ¿La cerrada la decidiste por @@dónde se invoca@@ cada rutina —dentro de un '
            '`SELECT` o como sentencia suelta— y no por el `LANGUAGE` que declara?',
            '□ ¿El contrato trae los 6 bloques de @@cada@@ procedimiento y las 7 filas de errores?',
        ],
    },
    4: {
        # Cierre del Corte 1. Todo el código corre en ExamLab; lo único que NO se
        # ejecuta es el respaldo (`pg_dump` y compañía necesitan sistema de archivos,
        # y ExamLab es PostgreSQL en el navegador): la pregunta 5 es un documento y
        # así está declarado, para que nadie pierda el taller intentando ejecutarla.
        'contexto': [
            '@@Por qué importa al PI:@@ integridad y trazabilidad son criterios de la rúbrica, '
            'y la evidencia son el trigger corriendo y la fila de auditoría — no una promesa.',
            'La auditoría es el único mecanismo que @@no se puede evitar olvidándose de '
            'llamarlo@@: nadie invoca un trigger, lo dispara el motor.',
            'El plan de respaldo es lo que un evaluador pregunta primero: cuánto se pierde y '
            'en cuánto tiempo se vuelve a operar, con @@números@@.',
        ],
        'objetivo': 'Una función de tarifas y dos triggers —auditoría y stock— corriendo en '
                    'ExamLab, más el Plan_Backup_VetCare con sus 6 secciones.',
        'criterios': [
            '`fn_precio_consulta` con `RETURNS NUMERIC`, `IMMUTABLE`, insensible a mayúsculas, '
            'recargo del 35 % y `NULL` tratado como falso (45000 → @@60750@@).',
            'El trigger de auditoría en sus @@dos objetos@@: `fn_trg_audit_cita() RETURNS '
            'TRIGGER` + `CREATE TRIGGER ... EXECUTE FUNCTION`. Cero `:NEW` / `:OLD`.',
            'Los 3 `UPDATE` dejan @@2 filas@@ en `audit_cita` y el estudiante explica por qué '
            'la tercera no se auditó.',
            'El stock negativo (@@-7@@) evidenciado @@antes@@ del trigger, y el trigger '
            '`BEFORE UPDATE` con el mensaje literal de la rúbrica.',
            '`Plan_Backup_VetCare` con las 6 secciones, RPO y RTO justificados contra el '
            'horario de la clínica, y la consulta de validación post-restore.',
            'Entrega domingo 23:59.',
        ],
        'escenario': [
            'Esquema de VetCare completo y poblado: 10 citas, con consultas ya registradas en '
            'las citas 2, 5, 7 y 10.',
            '`insumo` fue creada @@a propósito sin@@ `CHECK (stock >= 0)`: el insumo @@2 '
            '(Vacuna triple felina) tiene stock 3@@, y de ahí sale el -7 de la demostración.',
            '@@Motor:@@ PostgreSQL dentro de ExamLab. La función, los dos triggers y sus '
            'pruebas con bloques `DO` corren de verdad y ahí se califican.',
            '@@Lo que NO se ejecuta:@@ `pg_dump`, `pg_dumpall`, `pg_basebackup` ni `pg_restore` '
            '—son programas que escriben archivos y ExamLab corre en el navegador—. La '
            'pregunta 5 es un documento: se califica que nombre la herramienta correcta.',
        ],
        'pistas': [
            '□ ¿La función es `IMMUTABLE` y un canino en urgencia da @@60750@@?',
            '□ ¿Creaste los @@dos@@ objetos del trigger? Una función sola no dispara nada.',
            '□ ¿Está el `WHEN (OLD.estado IS DISTINCT FROM NEW.estado)`, y `audit_cita` quedó '
            'con @@2@@ filas?',
            '□ ¿`usuario_bd` y `fecha_evento` se llenan por `DEFAULT`, no desde el trigger?',
            '□ ¿Se ve el @@-7@@ antes de crear el trigger, y el stock volvió a 3 para probarlo?',
            '□ ¿El trigger de stock es `BEFORE`, y el insumo 2 termina en @@stock 1@@?',
            '□ ¿En la de selección múltiple revisaste @@las seis@@ afirmaciones, preguntándote '
            'si la regla mira solo su propia fila y quién la garantiza cuando el SQL @@no@@ '
            'viene de la aplicación?',
            '□ ¿El plan trae RPO y RTO en números, `pg_dumpall` para los roles y la sección 6 '
            'de lo que @@no@@ cubre?',
        ],
    },
    6: {
        'contexto': [
            '@@Por qué importa al PI:@@ la rúbrica pide un análisis de plan de ejecución, y un '
            'análisis es un @@antes y un después medidos@@ — no la frase «la optimicé».',
            'La pantalla de agenda de Huellitas se abre @@decenas de veces al día@@: es la '
            'consulta que más veces paga cualquier descuido.',
            'Optimizar y @@romper@@ se parecen mucho: las dos versiones se ven bien y una '
            'devuelve otra cosa. Por eso hoy la @@prueba de equivalencia@@ también vale puntos.',
        ],
        'objetivo': 'Dos consultas del PI reescritas y medidas con EXPLAIN ANALYZE sobre una base '
                    'con volumen, con la prueba de que el resultado no cambió, y la justificación '
                    'técnica que va al informe.',
        'criterios': [
            'La agenda del día con sus @@4 antipatrones@@ corregidos: proyección, `JOIN … ON`, '
            'predicado de rango sargable y comparación directa del estado.',
            'Las dos versiones devuelven las mismas @@91 filas@@, probado con `COUNT(*)` de cada '
            'una en la misma corrida.',
            'Tres planes leídos: `EXPLAIN (ANALYZE, BUFFERS)` del antes y del después, y '
            '`EXPLAIN ANALYZE` del después con `LIMIT 50`. Las @@tres@@ versiones van en la mini '
            'tabla de comentarios: nodo más costoso, filas estimadas vs reales, tiempo.',
            'La subconsulta correlacionada convertida en @@una sola pasada@@: `LEFT JOIN` + '
            '`GROUP BY` + @@`COUNT(c.id_cita)`@@, con los duenos sin citas todavía en 0.',
            'La equivalencia del ranking probada con `EXCEPT` en los @@dos sentidos@@: cero filas.',
            'La justificación de media página con sus 5 secciones, y `06_opt_antes.sql` / '
            '`06_opt_despues.sql` en la carpeta del PI.',
            'Entrega domingo 23:59.',
        ],
        'escenario': [
            'La base de este taller @@sí tiene volumen@@: 2.006 duenos, 5.008 mascotas, 16 '
            'veterinarios y @@30.010 citas@@ entre el 2026-01-05 y el 2026-07-23, unas 150 por día.',
            '`ANALYZE` ya está corrido y @@no hay ningún índice@@ más allá de las llaves '
            'primarias: es a propósito, para que la mejora venga de la consulta y no de una '
            'estructura que aún no se ha visto.',
            '@@Motor:@@ PostgreSQL dentro de ExamLab, en el navegador. `EXPLAIN`, '
            '`EXPLAIN ANALYZE` y la opción `BUFFERS` corren de verdad; ahí se califica.',
            'Los @@seis duenos con cero citas@@ (ids 2001 a 2006) están puestos a propósito: son '
            'los que delatan un `COUNT(*)` o un `INNER JOIN` mal elegidos.',
            '@@Aviso:@@ la versión ANTES de la pregunta 3 se ejecuta 2.006 veces y puede tardar '
            'de varios segundos a más de un minuto. @@No está colgada.@@',
        ],
        'pistas': [
            '□ ¿Quedó algún `SELECT *`, o proyectaste las @@6@@ columnas que pide el enunciado?',
            '□ ¿La fecha se filtra con un @@rango@@ sobre la columna, sin `to_char` ni `EXTRACT` '
            'encima de ella?',
            '□ ¿Los dos `COUNT(*)` de la pregunta 1 dan el @@mismo@@ número?',
            '□ ¿Están los @@tres@@ `EXPLAIN`, incluido el de `LIMIT 50`, y la tabla de '
            'comentarios con sus @@tres filas@@ (ANTES, DESPUES, DESPUES+LIM50) y sus tres '
            'columnas?',
            '□ ¿Los números de la tabla los @@leíste del plan@@, o los estimaste? Se compara con '
            '`rows=` frente a `actual rows=`.',
            '□ ¿Contaste `COUNT(c.id_cita)` y no `COUNT(*)`? Mira los duenos @@2001 a 2006@@: '
            'tienen que decir @@0@@.',
            '□ ¿El `EXCEPT` va en los @@dos@@ sentidos y @@sin@@ `LIMIT`?',
            '□ ¿En la de selección múltiple revisaste @@las seis@@ afirmaciones, incluida la que '
            'dice que optimizar puede cambiar el número de filas?',
            '□ ¿La justificación tiene las @@5@@ secciones, y cada cambio se ancla a una '
            'evidencia concreta del plan?',
        ],
    },
    7: {
        'contexto': [
            '@@Por qué importa al PI:@@ la rúbrica pide índices @@justificados@@, y una '
            'justificación es una consulta concreta más la evidencia del plan — no «indexé las '
            'columnas importantes».',
            'La agenda del día y la ficha del dueño son las dos pantallas que Huellitas abre '
            '@@todo el día@@: son las que pagan cada `Seq Scan` sobre 30.010 citas.',
            'Indexar de más también cuesta: cada índice se mantiene en @@cada cita agendada@@. Por '
            'eso hoy el @@veredicto@@ de cada índice vale tantos puntos como crearlo.',
        ],
        'objetivo': 'Tres índices creados con nombre exacto (uno parcial) y probados con EXPLAIN '
                    'antes y después, el experimento del orden de columnas en un índice compuesto, '
                    'el histórico particionado por año con su poda demostrada, y la tabla de '
                    'justificación que va al informe.',
        'criterios': [
            'La línea base medida @@antes@@ de indexar: `EXPLAIN ANALYZE` de las dos consultas '
            'frecuentes con `Seq Scan` a la vista.',
            'Los @@tres@@ índices con el nombre exacto — `idx_cita_fecha_hora`, '
            '`idx_mascota_dueno` y el @@parcial@@ `idx_cita_programada_fecha` con su `WHERE '
            "estado = 'PROGRAMADA'` — y `ANALYZE` corrido después.",
            'Los `EXPLAIN` repetidos mostrando `Index Scan` o `Bitmap Index Scan`, y dicho '
            '@@cuál@@ de los dos índices sobre `fecha_hora` eligió el planeador.',
            'El experimento del orden de columnas: los dos índices compuestos, las @@tres@@ '
            'consultas medidas, el `DROP INDEX` que fuerza la comparación y la línea '
            '`-- CONCLUSION:` con la regla de igualdad antes que rango.',
            '`cita_hist` particionada por año: PK que @@incluye la columna de partición@@, las dos '
            'particiones sin solaparse, la migración completa y la @@poda@@ evidenciada en el plan.',
            'La tabla de justificación con sus @@7 columnas@@ y una fila por índice (mínimo 3), la '
            'regla de sobre-indexación y el veredicto de particionamiento con @@tus números@@.',
            'Entrega domingo 23:59.',
        ],
        'escenario': [
            'Las preguntas 1 y 2 corren sobre una base @@con volumen@@: 2.006 duenos, 5.008 '
            'mascotas, 16 veterinarios y @@30.010 citas@@ entre el 2026-01-05 y el 2026-07-23. '
            '`ANALYZE` ya está corrido y @@no hay ningún índice@@ más allá de las PK: los creas tú.',
            'Las dos consultas frecuentes vienen @@escritas en el enunciado@@ y no se cambian: la '
            "agenda del día filtra `cita` por rango de `fecha_hora` y por `estado = 'PROGRAMADA'`; "
            'la ficha del dueño filtra `mascota` por `id_dueno`.',
            'La pregunta 3 usa @@otra@@ base, a propósito: @@5.010 citas@@ repartidas entre enero '
            'de 2025 y diciembre de 2026, para que haya dos años que particionar. Si ves 5.010 '
            'donde esperabas 30.010, @@no es un error@@.',
            '@@Motor:@@ PostgreSQL dentro de ExamLab, en el navegador. `EXPLAIN ANALYZE`, los '
            'índices parciales, `PARTITION BY RANGE` y la poda de particiones corren de verdad; '
            'ahí se califica.',
            'Los nombres del curso son @@minúsculas y sin eñes@@: las tablas son `dueno`, '
            '`mascota` y `cita`, y la columna es `id_dueno`. Un `Mascota(id_dueño)` no compila.',
        ],
        'pistas': [
            '□ ¿Corriste los `EXPLAIN` @@antes@@ de crear los índices? Sin la línea base con '
            '`Seq Scan` no hay con qué comparar el después.',
            '□ ¿Los tres índices tienen el @@nombre exacto@@ del enunciado, y el parcial lleva su '
            "cláusula `WHERE estado = 'PROGRAMADA'`?",
            '□ ¿Corriste `ANALYZE cita;` y `ANALYZE mascota;` antes de volver a medir? Sin '
            'estadísticas frescas el planeador puede seguir eligiendo el barrido.',
            '□ ¿Dijiste @@cuál@@ de los dos índices sobre `fecha_hora` usó la agenda del día, y '
            'por qué ese y no el otro?',
            '□ En la pregunta 2, ¿hiciste el `DROP INDEX` y volviste a medir @@Q2@@? La '
            'comparación es el punto del experimento, no crear los dos índices.',
            '□ ¿La `-- CONCLUSION:` habla del orden de las columnas, o solo dice que el índice '
            'sirvió?',
            '□ En `cita_hist`, ¿la PK incluye `fecha_hora`? PostgreSQL @@rechaza@@ una PK '
            'particionada que no contenga la columna de partición.',
            '□ ¿El plan de la consulta de 2026 muestra @@una sola@@ partición? Si aparecen las '
            'dos, no hubo poda y eso es lo que se califica.',
            '□ ¿Revisaste las @@seis@@ afirmaciones de la de selección múltiple, incluida la que '
            'sostiene que una `FOREIGN KEY` ya crea su índice? Puedes comprobarlo en el '
            '`pg_indexes` de la pregunta 1.',
            '□ ¿Tu tabla tiene las @@7@@ columnas en las @@3@@ filas, con los números @@leídos del '
            'plan@@ y no estimados?',
            '□ ¿Tu regla de sobre-indexación la puede @@verificar otra persona@@ mirando tu '
            'proyecto? «Indexar con cuidado» no se puede verificar.',
            '□ ¿El veredicto de particionamiento trae tus números de volumen @@y@@ reconoce que con '
            '5.010 filas lo comprobado fue la poda y el archivado, no la velocidad?',
        ],
    },
    8: {
        'contexto': [
            '@@Por qué importa al PI:@@ facturar es la operación donde Huellitas @@pierde plata@@ '
            'si algo queda a medias: una factura sin líneas, o un stock descontado de una factura '
            'que nunca existió.',
            'Hoy no se evalúa que el procedimiento @@funcione@@, sino que @@falle bien@@: la '
            'pregunta 2 vale 25 puntos y consiste en romperlo a propósito y demostrar con datos '
            'que la base quedó intacta.',
            'El patrón que aprendes hoy — comprobar y escribir en @@una sola sentencia@@ — es el '
            'que evita el stock negativo cuando hay dos recepcionistas facturando. Que aquí no '
            'puedas montar las dos sesiones es la @@Clase 10@@, y declararlo suma puntos.',
        ],
        'objetivo': 'La transacción de facturación implementada como procedimiento atómico, su '
                    'atomicidad demostrada con foto antes y después de un fallo a mitad de camino, '
                    'el patrón de descuento seguro encapsulado en una función, y la sección '
                    '«Transacciones y tuning» del informe del PI.',
        'criterios': [
            '`sp_facturar(p_id_consulta INT, p_insumos INT[], p_cantidades INT[])` con la firma '
            'exacta: cabecera en total 0 con `RETURNING … INTO`, bucle por línea, `UPDATE` '
            'condicional con `GET DIAGNOSTICS … ROW_COUNT` y `RAISE EXCEPTION` si no alcanza.',
            'El caso exitoso ejecutado y evidenciado: factura por @@27.400@@ y los insumos 1, 6 y '
            '5 en @@11, 58 y 5@@.',
            'La atomicidad probada con @@la misma consulta@@ de foto inicial y final, y dicho con '
            'datos que el stock del insumo 3 @@volvió a 40@@ y que no quedó factura ni línea '
            'huérfana.',
            '`fn_descontar_stock` devolviendo `BOOLEAN` — @@`FALSE`, no excepción@@, cuando no hay '
            'stock — con la prueba que arroja `true / false / true` y ningún stock negativo.',
            'La sección del informe con sus 4 bloques: @@3 transacciones@@ con su punto de fallo, '
            'el checklist de @@7 ítems@@ con estado y evidencia, la decisión documentada y el gap '
            'de concurrencia.',
            'Entrega domingo 23:59.',
        ],
        'escenario': [
            'El esquema de VetCare ya está creado y poblado: consultas @@1 a 4@@, facturas 1 a 3 '
            'con sus 8 líneas de detalle, y @@6 insumos@@ con stock 12, @@3@@, 40, 25, @@8@@ y 60.',
            'Los stocks bajos son @@deliberados@@: el insumo 2 con 3 unidades es el que va a hacer '
            'fallar la factura de la pregunta 2, y el insumo 3 con 40 es el que tiene que '
            '@@volver@@ a 40.',
            'La consulta 4 es la única @@sin facturar@@: es la que vas a facturar tú.',
            'En la pregunta 2 el `sp_facturar` @@ya viene creado@@ (versión de referencia), así '
            'que puedes demostrar la atomicidad aunque tu propio procedimiento de la pregunta 1 '
            'te haya quedado a medias.',
            '@@Motor:@@ PostgreSQL dentro de ExamLab, en el navegador. PL/pgSQL, `CALL`, '
            '`GET DIAGNOSTICS` y los bloques `DO $$ … EXCEPTION` corren de verdad. Corre con '
            '@@una sola sesión@@: la concurrencia real no se puede montar aquí, y eso es la '
            'Clase 10.',
        ],
        'pistas': [
            '□ ¿Usaste `GET DIAGNOSTICS v_filas = ROW_COUNT;`? En PostgreSQL @@no existe@@ '
            '`SQL%ROWCOUNT`.',
            '□ ¿Dejaste algún `COMMIT` dentro del procedimiento? No va: el `CALL` de nivel '
            'superior @@ya es@@ su propia transacción.',
            '□ ¿El descuento va con la condición `AND stock >= p_cantidades[i]` @@dentro del@@ '
            '`WHERE`, o leíste el stock primero y decidiste después?',
            '□ ¿La factura del caso exitoso quedó en @@27.400@@ y los stocks en 11, 58 y 5? Si no '
            'cuadra, revisa que uses el `precio_unit` @@del insumo@@ y no el de la consulta.',
            '□ ¿La foto inicial y la foto final son @@exactamente la misma@@ consulta? Si cambias '
            'la consulta, la comparación no prueba nada.',
            '□ ¿Envolviste el intento que debe fallar en `DO $$ … EXCEPTION WHEN OTHERS`? Sin eso '
            'el script se detiene y no alcanzas a tomar la foto final.',
            '□ ¿Escribiste la comparación en comentarios `--`, incluida la línea del @@stock del '
            'insumo 3@@? Es la evidencia central de los 25 puntos: sin ella la pregunta queda '
            'sin argumento.',
            '□ ¿Corriste también la llamada @@viable@@ al final? El contraste entre la abortada y '
            'la exitosa es parte de la respuesta.',
            '□ ¿`fn_descontar_stock` @@retorna@@ `FALSE` cuando no hay stock, en vez de lanzar '
            'excepción? Aquí el «no alcanza» es una respuesta, no un error.',
            '□ ¿Verificaste que @@ningún@@ stock quedó negativo después de las tres pruebas?',
            '□ En la de selección única, ¿la explicación que marcaste es válida en '
            '@@PostgreSQL@@, o es la de otro motor? Contrástala con lo que tú escribiste: no '
            'pusiste ningún `ROLLBACK` en el procedimiento y aun así se deshizo todo.',
            '□ ¿Tus 3 transacciones traen las @@tres@@ cosas — tablas que toca, paso que puede '
            'fallar y qué debe pasar si falla? Sin el punto de fallo es una lista de operaciones, '
            'no un inventario de transacciones.',
            '□ ¿Los 7 ítems del checklist tienen @@evidencia@@ y no solo la casilla marcada? Un '
            'nombre de índice, un archivo o una consulta.',
            '□ ¿Declaraste el @@gap de concurrencia@@ y cómo lo abordas en la Clase 10? Reconocer '
            'lo que no se pudo comprobar suma; ocultarlo se descuenta.',
        ],
    },
    10: {
        'contexto': [
            '@@Por qué importa al PI:@@ doble reserva y stock negativo.',
            'Autónoma: escenarios + mitigacion SQL.',
        ],
        'objetivo': '2 escenarios concurrencia T1/T2 + mitigacion.',
        'criterios': [
            'Doble reserva.',
            'Doble stock.',
            'Mitigacion SQL.',
            'Sección informe.',
            'Domingo 23:59.',
        ],
        'escenario': [
            'Narrar T1/T2 sobre Cita/Insumo.',
        ],
        'pistas': [
            '□ Tiempos claros?',
            '□ Mitigacion SQL concreta?',
            '□ Conecta con procs?',
        ],
    },
    11: {
        'contexto': [
            '@@Por qué importa al PI:@@ checkpoint vs rúbrica.',
            'Demo + gaps con responsable.',
        ],
        'objetivo': 'Checklist avance + demo 3-5 min.',
        'criterios': [
            'Checklist evidenciada.',
            'Demo ER+proc+trigger.',
            'Gaps.',
            'Avance subido si aplica.',
        ],
        'escenario': [
            'Evidencias: ER, DDL, roles, procs, fn, triggers, opt.',
        ],
        'pistas': [
            '□ Si con evidencia?',
            '□ Gaps con dueño?',
            '□ Demo <=5 min?',
        ],
    },
    12: {
        'contexto': [
            '@@Por qué importa al PI:@@ app llama contrato, no SQL suelto.',
            'Preparar sustentacion.',
        ],
        'objetivo': 'Contrato >=3 ops + outline pitch 5-8 min.',
        'criterios': [
            'Contrato 3 ops.',
            'Parametros/errores/ejemplo.',
            'Outline pitch.',
            'Borrador final.',
        ],
        'escenario': [
            'Plantilla sp_agendar_cita / consulta / facturar.',
        ],
        'pistas': [
            '□ >=3 ops?',
            '□ Errores esperados?',
            '□ Outline completo?',
        ],
    },
    13: {
        'contexto': [
            '@@Por qué importa al PI:@@ lecciónes accionables.',
            'Autónoma: 1 caso -> 3 mejoras.',
        ],
        'objetivo': 'Caso real -> 3 mejoras VetCare.',
        'criterios': [
            'Caso elegido.',
            'Resumen.',
            '3 mejoras.',
            'Informe.',
            'Domingo 23:59.',
        ],
        'escenario': [
            'Plantilla: contexto->fallo->lección->cambio.',
        ],
        'pistas': [
            '□ Mejoras accionables?',
            '□ Conectan al PI?',
            '□ Evidencia de lectura?',
        ],
    },
    15: {
        'contexto': [
            '@@Por qué importa al PI:@@ cierre segun rúbrica 20% Corte 3.',
            'No confundir con Parcial 3 (Clase 14).',
        ],
        'objetivo': 'Paquete final entregado + sustentacion en vivo de 5-8 min con Q&A.',
        'criterios': [
            'ZIP/PDF en ExamLab ANTES del turno.',
            'Sustentacion en vivo de 5-8 min.',
            'Q&A respondido en vivo (preguntas al azar).',
            'Autoevaluacion.',
            'Cierre.',
        ],
        'escenario': [
            'Checklist empaquetado del enunciado PI.',
            'Turnos consecutivos en el bloque; el orden se sortea al abrir la sesion.',
        ],
        'pistas': [
            '□ Falta evidencia?',
            '□ Cubre todos los bloques (y todos hablan, si hay equipo)?',
            '□ PI != P3?',
        ],
    },
}

SOLUCION = {
    1: {
        'titulo': 'Solución Taller Clase 1 — Arranque VetCare',
        'resumen': 'ER minimo Dueño-Mascota-Cita + 3 reglas + alcance.',
        'pasos': [
            'Trabajo individual por defecto: nombra tu proyecto VetCare - [Apellido] y registralo para identificarlo en todas las entregas del semestre. Si el docente autoriza equipo de 2 o 3, el artefacto puede ser compartido pero la entrega en ExamLab sigue siendo individual.',
            'Listar las entidades minimas del dominio: Dueño (persona que trae la mascota), Mascota (paciente), Veterinario (quien atiende), Cita (agenda de una atencion). Consulta, Insumo y DetalleFactura se agregan en clases posteriores.',
            'Redactar 3 reglas de negocio propias en formato Condicion -> Accion, cada una con el mecanismo con que se implementara (CHECK, UNIQUE, FK, procedimiento o trigger): "una mascota con activa=N no puede tener una cita nueva", "el stock de un insumo nunca puede quedar en negativo", "toda cancelacion de cita queda registrada con usuario y fecha".',
            'Dibujar el ER borrador marcando cardinalidad en cada relacion (Dueño 1-N Mascota, Mascota 1-N Cita) en Excalidraw o draw.io, pasarlo a Mermaid (erDiagram) con ayuda de una IA y pegarlo en la pregunta 2 de ExamLab verificando que renderice; el PNG exportado va a la carpeta del PI, pero lo que califica es el Mermaid renderizado.',
            'Escribir el alcance en dos listas explicitas: que SI cubre el PI este semestre (agenda, facturacion basica, roles) y que NO cubre (ej. pagos en linea, historial clinico completo) para evitar scope creep en clases futuras.',
        ],
        'ejemplo': [
            'DDL: Kit docente/Clase 1/Codigo/01_arranque_vetcare.sql',
            'ER: Dueño 1-N Mascota; Mascota 1-N Cita.',
        ],
        'rubrica': [
            'Registro del proyecto (1)',
            'ER (3)',
            'Reglas (2)',
            'Alcance (2)',
            'Entrega (2)',
        ],
        'errores': [
            'ER genérico.',
            'Sin FK.',
            'Scope infinito.',
            'Entregar el PNG y dejar vacía la pregunta de diagrama: ExamLab califica el Mermaid renderizado, no la imagen.',
            'Reglas escritas como deseos («el sistema debe ser seguro») en vez de Condición → Acción verificable.',
            'Nombres en mayúscula, plural o con tilde: el DDL falla en el PostgreSQL de ExamLab y se pierde la clase depurándolo.',
        ],
    },
    2: {
        'titulo': 'Solución Taller Clase 2 — Roles VetCare',
        'resumen': '4 roles verificados + matriz de 10 objetos + política de altas y bajas.',
        'pasos': [
            'Crear los 4 roles con el nombre exacto que pide ExamLab, en minuscula y sin login: admin_bd (ALL PRIVILEGES sobre las 8 tablas), recepcion (opera citas y lee datos de contacto), veterinario_rol (registra consultas; lleva el sufijo _rol porque veterinario ya es una tabla) y auditor (solo lectura sobre lo sensible).',
            'Construir la matriz rol x objeto x privilegio: por cada rol, listar exactamente que objeto y que operacion (SELECT/INSERT/UPDATE/DELETE/EXECUTE) tiene permitida — no "acceso general", sino privilegio por objeto. Son 10 objetos: las 8 tablas mas sp_agendar_cita y sp_facturar, que van con EXECUTE.',
            'recepcion puede SELECT/INSERT/UPDATE sobre cita y SELECT sobre mascota/dueno/veterinario, pero NUNCA DELETE en ninguna tabla: cancelar una cita es un UPDATE de estado a CANCELADA, y el REVOKE de DELETE se deja escrito aunque sea redundante, como evidencia de la decision.',
            'auditor recibe unicamente SELECT sobre las tablas sensibles (dueno, mascota, cita, consulta, factura); ningun privilegio de escritura, ni siquiera sobre datos "poco importantes", porque su funcion es verificar, no operar.',
            'Recortar la superficie donde el GRANT es demasiado: vista v_agenda_recepcion sin el email del dueno (y REVOKE SELECT ON dueno FROM recepcion), y GRANT SELECT (id_dueno, nombre) ON dueno TO veterinario_rol. Verificar las dos cosas con information_schema.',
            'Redactar la politica de altas y bajas en una pagina, con las 5 secciones del enunciado: alta, cambio de rol, baja el mismo dia (con REASSIGN OWNED BY antes del DROP ROLE), revision periodica con la consulta que sirve de evidencia, y la prueba negativa — SET ROLE recepcion; seguido de la sentencia que debe fallar con permission denied, y RESET ROLE; para volver.',
        ],
        'ejemplo': [
            'Codigo/02_roles_vetcare.sql',
        ],
        'rubrica': [
            'Roles + GRANT/REVOKE verificados (30)',
            'Minimo privilegio en la matriz (10)',
            'Vista y privilegio por columna (20)',
            'Matriz 10 objetos x 4 roles (25)',
            'Politica de altas y bajas (15)',
        ],
        'errores': [
            'Todos DBA.',
            'Sin justificar.',
            'Nombres de rol en mayuscula o veterinario sin _rol.',
        ],
    },
    3: {
        'titulo': 'Solución Taller Clase 3 — Procedimientos',
        'resumen': 'sp_agendar_cita con validación mascota activa.',
        'pasos': [
            'Crear sp_agendar_cita con parametros IN (id_cita, id_mascota, fecha) y un parametro OUT (p_msg) para devolver el resultado a quien lo llame.',
            "Antes de insertar, hacer SELECT activa FROM mascota WHERE id_mascota = p_id_mascota; si activa <> 'S', asignar p_msg := 'ERROR: mascota inactiva; no se agenda' y salir con RETURN sin tocar la tabla cita.",
            'Si la validacion pasa, ejecutar el INSERT INTO cita y confirmar con COMMIT; asignar p_msg := \'OK: cita agendada\' para que quien llamo el proc sepa que la operacion tuvo exito.',
            'Ejecutar dos pruebas obligatorias: (1) caso OK con una mascota activa=S — debe insertar y devolver mensaje de exito; (2) caso error con una mascota activa=N o inexistente — debe rechazar sin insertar nada y devolver el mensaje de error correspondiente (usar EXCEPTION WHEN NO_DATA_FOUND para el caso de mascota inexistente).',
            'Documentar la firma del proc como si fuera el contrato que usara la futura app: nombre, cada parametro con su tipo y direccion (IN/OUT), y el listado de mensajes de p_msg posibles — esto es exactamente lo que se reutiliza en el contrato de integracion de Clase 12.',
        ],
        'ejemplo': [
            'Codigo/03_procs_vetcare.sql',
        ],
        'rubrica': [
            'Proc (3)',
            'Validación (3)',
            'Pruebas (2)',
            'Contrato (2)',
        ],
        'errores': [
            'Sin validación.',
            'Solo captura.',
        ],
    },
    4: {
        'titulo': 'Solución Taller Clase 4 — Fn/trigger/backup',
        'resumen': 'Funcion + trigger + plan respaldo.',
        'pasos': [
            'Crear fn_precio_base(p_especie) que RETURN un valor NUMBER util al PI (ej. tarifa base segun especie), verificable con SELECT fn_precio_base(\'CANINO\') FROM dual — una funcion se prueba dentro de un SELECT, no con CALL.',
            'Crear trg_audit_cancelacion_cita (AFTER UPDATE ON cita WHEN estado cambia a CANCELADA) que inserte una fila en una tabla de auditoria con usuario, fecha y el id de la cita cancelada — sin que la app tenga que acordarse de registrar nada explicitamente.',
            'Redactar el plan de respaldo con las 3 variables que lo hacen verificable: frecuencia (ej. diaria a las 2am), retencion (ej. 7 copias diarias + 4 semanales), y prueba de restore (ej. una vez al mes se restaura en un ambiente de prueba y se valida que los datos coinciden).',
            'Actualizar el checklist del PI marcando explicitamente: funcion creada y probada, trigger creado y disparado al menos una vez en pruebas, plan de respaldo redactado con las 3 variables — no basta con "en progreso" sin evidencia.',
        ],
        'ejemplo': [
            'Codigo/04_func_trigger_backup.sql',
        ],
        'rubrica': [
            'Funcion (2)',
            'Trigger (3)',
            'Backup (3)',
            'Checklist (2)',
        ],
        'errores': [
            'Trigger vacio.',
            'Backup sin restore.',
        ],
    },
    6: {
        'titulo': 'Solución Taller Clase 6 — Optimización',
        'resumen': 'Pareja antes/después VetCare.',
        'pasos': [
            'Elegir una consulta real y frecuente del PI (ej. listar las citas del dia con nombre de mascota y dueno) — no un ejemplo inventado sin uso real.',
            'Escribir la version "antes" tal como la escribiria alguien sin entrenamiento: SELECT * ... con JOIN sin filtro de fecha, trayendo todo el historico.',
            'Reescribir la version "despues": proyectar solo las columnas necesarias, filtrar por fecha_hora >= hoy ANTES del JOIN cuando el motor lo permita, y evitar funciones sobre la columna de fecha en el WHERE.',
            'Justificar por escrito minimo 3 cambios concretos (ej. "se elimino SELECT * porque solo se usan 4 columnas", "el filtro de fecha reduce el conjunto antes del JOIN", "se evito CAST sobre fecha_hora en el WHERE porque bloqueaba el uso de indice").',
            'Guardar ambas versiones como 06_opt_antes.sql y 06_opt_despues.sql en tu carpeta del PI, y si el playground lo permite, adjuntar el resultado de EXPLAIN de cada una como evidencia de la mejora.',
        ],
        'ejemplo': [
            'Codigo/06_opt_consultas.sql',
        ],
        'rubrica': [
            'Consulta PI (2)',
            'Pareja (3)',
            'Justificación (3)',
            'Archivos (2)',
        ],
        'errores': [
            'Caso genérico.',
            'Sin diferencia real.',
        ],
    },
    7: {
        'titulo': 'Solución Taller Clase 7 — Indices',
        'resumen': '2 indices justificados.',
        'pasos': [
            'Identificar 2 consultas frecuentes del PI que filtran o unen por una columna especifica (ej. "citas de un dia" filtra por fecha_hora; "historial de un dueno" filtra por id_dueno via mascota).',
            'Crear los indices correspondientes, ej. CREATE INDEX idx_cita_fecha ON cita(fecha_hora); CREATE INDEX idx_mascota_dueno ON mascota(id_dueno) — con nombres que dejen claro que tabla/columna indexan.',
            'Construir una tabla de dos columnas: consulta frecuente -> indice que la acelera, explicando en una frase por que esa columna tiene suficiente cardinalidad para justificar el indice.',
            'Explicar por escrito el riesgo de sobre-indexar: cada indice adicional ralentiza INSERT/UPDATE/DELETE sobre esa tabla, asi que un indice sin una consulta real que lo use es costo puro sin beneficio — por eso el entregable exige justificar cada indice con su consulta.',
        ],
        'ejemplo': [
            'Codigo/07_indices_vetcare.sql',
        ],
        'rubrica': [
            'Indices (4)',
            'Justificación (3)',
            'Riesgo (2)',
            'Evidencia (1)',
        ],
        'errores': [
            'Sin consulta.',
            'Indexar todo.',
        ],
    },
    8: {
        'titulo': 'Solución Taller Clase 8 — Transacciones',
        'resumen': 'Factura+stock con ROLLBACK.',
        'pasos': [
            'Implementar un procedimiento (o bloque transaccional explicito) que inserte la factura, inserte el detalle_factura y descuente el stock del insumo en una sola transaccion: BEGIN...INSERT...INSERT...UPDATE stock...COMMIT.',
            'Forzar deliberadamente un caso de fallo (ej. intentar descontar mas stock del disponible) y verificar que el ROLLBACK deshace TODO: ni la factura ni el detalle quedan registrados a medias — esa es la prueba real de atomicidad, no solo el caso feliz.',
            'Completar el checklist de tuning: estadisticas actualizadas, existencia de indice sobre las columnas usadas en el JOIN/WHERE de esta transaccion, y verificar que la transaccion no queda abierta mas tiempo del necesario (sin operaciones manuales del usuario en medio del BEGIN/COMMIT).',
            'Actualizar el informe del PI con la seccion de transacciones: que operacion se protegio, que prueba de fallo se ejecuto, y que se verifico despues del ROLLBACK (que el stock e historial quedaron exactamente como antes del intento fallido).',
        ],
        'ejemplo': [
            'Codigo/08_transacciones_vetcare.sql',
        ],
        'rubrica': [
            'Transaccion (4)',
            'ROLLBACK (3)',
            'Checklist (2)',
            'Informe (1)',
        ],
        'errores': [
            'Sin prueba fallo.',
            'Updates sueltos.',
        ],
    },
    10: {
        'titulo': 'Solución Taller Clase 10 — Concurrencia',
        'resumen': '2 escenarios + mitigacion.',
        'pasos': [
            'Narrar el escenario de doble reserva con linea de tiempo explicita: T1 lee la franja como libre en el segundo 0, T2 lee la misma franja como libre en el segundo 1 (antes de que T1 confirme), ambas insertan y quedan dos citas para el mismo veterinario/franja.',
            'Narrar el escenario de doble descuento de stock con la misma logica T1/T2: dos facturas leen el mismo stock disponible antes de que ninguna confirme su UPDATE, y el stock final queda incorrecto (mayor de lo que debería haberse descontado, o incluso negativo).',
            'Proponer la mitigacion SQL concreta para cada escenario: UNIQUE(id_veterinario, fecha_hora) para que el segundo INSERT de cita falle automaticamente; y para el stock, un UPDATE con condicion (UPDATE insumo SET stock = stock - x WHERE id_insumo = y AND stock >= x) que falla/no afecta filas si ya no alcanza, en vez de restar a ciegas.',
            'Agregar la seccion de concurrencia al informe del PI explicando, en lenguaje simple, por que un simple "usar transacciones" no basta sin la restriccion UNIQUE o la condicion en el UPDATE, y que mecanismo especifico elegiste para VetCare.',
        ],
        'ejemplo': [
            'Codigo/10_concurrencia_vetcare.sql',
        ],
        'rubrica': [
            'Cita (3)',
            'Stock (3)',
            'Mitigacion (3)',
            'Informe (1)',
        ],
        'errores': [
            'Sin T1/T2.',
            'Mitigacion vaga.',
        ],
    },
    11: {
        'titulo': 'Solución Taller Clase 11 — Checkpoint',
        'resumen': 'Checklist + demo.',
        'pasos': [
            'Completar el checklist marcando SI/NO/PARCIAL en cada evidencia exigida: ER actualizado, DDL ejecutable, roles definidos, minimo 2 procedimientos, minimo 1 funcion, minimo 2 triggers, minimo 1 optimizacion documentada.',
            'Preparar y ejecutar una demo de 3-5 minutos que muestre en vivo: el ER, un procedimiento ejecutandose con un caso real, y un trigger disparandose (ej. cancelar una cita y mostrar la fila de auditoria creada).',
            'Listar explicitamente los gaps (huecos) que quedan pendientes, cada uno con un responsable con nombre (tu mismo si trabajas solo; repartido si hay equipo autorizado) — no dejar gaps sin dueño.',
            'Subir el avance intermedio (enlace o ZIP con DDL + procs + ER) a ExamLab si el docente lo solicita, como respaldo verificable del progreso a mitad de corte.',
        ],
        'ejemplo': [
            'Codigo/11_checklist_seed.sql',
        ],
        'rubrica': [
            'Checklist (4)',
            'Demo (3)',
            'Gaps (2)',
            'Paquete (1)',
        ],
        'errores': [
            'Si sin enlaces.',
            'Demo sin artefactos.',
        ],
    },
    12: {
        'titulo': 'Solución Taller Clase 12 — Contrato + pitch',
        'resumen': 'Contrato 3 ops + outline.',
        'pasos': [
            'Redactar el contrato de al menos 3 operaciones (ej. agendar_cita, registrar_consulta, facturar) especificando nombre del proc, cada parametro con tipo y direccion IN/OUT, y que retorna en caso de exito.',
            'Para cada operacion, documentar los posibles errores de negocio (ej. "mascota inactiva", "stock insuficiente") con el mensaje exacto que devuelve el proc, y un ejemplo de llamada con valores concretos.',
            'Construir el outline de la sustentacion de 5-8 minutos con la secuencia problema -> modelo -> seguridad -> procs/triggers -> optimizacion -> demo en vivo, dejando claro que dices en cada seccion (y quien la presenta, si hay equipo autorizado: todos deben hablar).',
            'Empaquetar el borrador de entrega final (DDL, procs, contrato, outline) en una carpeta o ZIP organizado, listo para completarse en las Clases 13-15 sin tener que reconstruirlo desde cero.',
        ],
        'ejemplo': [
            'Codigo/12_contrato_ops.sql',
        ],
        'rubrica': [
            'Contratos (4)',
            'Errores (2)',
            'Outline (3)',
            'Paquete (1)',
        ],
        'errores': [
            'Sin errores.',
            'Outline logos.',
        ],
    },
    13: {
        'titulo': 'Solución Taller Clase 13 — Casos reales',
        'resumen': '1 caso -> 3 mejoras.',
        'pasos': [
            'Elegir uno de los 3 casos trabajados en teoria (falta de backup, indices mal disenados, o inyeccion SQL) segun el que mas riesgo represente para el estado actual de tu VetCare.',
            'Resumir el caso en media pagina con la estructura contexto -> fallo -> causa raiz tecnica (no "mala suerte") -> leccion general.',
            'Proponer 3 mejoras concretas y verificables aplicadas al VetCare propio (ej. "agregar prueba de restore mensual", "revisar y eliminar 2 indices sin uso real", "confirmar que todos los procs usan parametros tipados, ninguno concatena texto de usuario").',
            'Actualizar el informe del PI incorporando estas lecciones como una seccion nueva, citando en que clase/entregable anterior se relaciona cada mejora (Clase 4 para backup, Clase 7 para indices, Clase 3/12 para inyeccion SQL).',
        ],
        'ejemplo': [
            'Plantilla contexto->fallo->lección->cambio VetCare.',
        ],
        'rubrica': [
            'Caso (2)',
            'Resumen (2)',
            'Mejoras (4)',
            'Informe (2)',
        ],
        'errores': [
            'Mejoras genericas.',
            'Sin conexión PI.',
        ],
    },
    15: {
        'titulo': 'Solución Taller Clase 15 — Entrega final',
        'resumen': 'Checklist empaquetado + pitch.',
        'pasos': [
            'Verificar el ZIP/paquete final linea por linea contra la rubrica de 100 pts (ER, DDL, roles, procs, funciones/triggers, optimizacion, indices, transacciones, concurrencia, contrato de integracion, informe) antes de subirlo, no despues.',
            'Sustentar 5-8 minutos siguiendo el outline preparado en Clase 12, con evidencia en vivo (no solo diapositivas) de al menos un procedimiento y un trigger ejecutandose.',
            'Completar la autoevaluacion de tu propio trabajo respondiendo con honestidad que harias distinto si empezaras de nuevo (si hubo equipo autorizado, agrega una linea por integrante) — esto pesa en la nota y demuestra criterio, no solo ejecucion.',
            'Cerrar formalmente el curso confirmando que la entrega quedo registrada en ExamLab dentro del plazo, con el enlace o archivo accesible para el docente.',
        ],
        'ejemplo': [
            'Estructura: ER, DDL, roles, procs, fn/triggers, opt, indices, tx, concurrencia, contrato, informe.',
        ],
        'rubrica': [
            'Paquete (4)',
            'Sustentacion (3)',
            'Autoevaluacion (2)',
            'Rubrica (1)',
        ],
        'errores': [
            'Faltan evidencias.',
            'Confundir con P3.',
        ],
    },
}
