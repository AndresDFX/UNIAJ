# -*- coding: utf-8 -*-
"""Consultas proyectadas de Bases de Datos II: el SQL que se dicta, por clase.

Por que existe
--------------
Bases de Datos II es la materia de las consultas y su deck proyectaba 42 laminas de codigo
sobre 532: el 7%. Todo el SQL que existia en el material ya esta extraido —`CODIGO_SLIDE` y
las sentencias que estaban escritas dentro de la prosa—, asi que subir de ahi era escribir
consultas nuevas. Esto es eso.

La regla que gobierna lo que se escribe aqui
--------------------------------------------
CLAUDE.md §0: **nada se evalua que no se haya ensenado, y nada se ensena que no se use.** Cada
clase de aqui ensena el MECANISMO que su actividad de ExamLab evalua, y lo ensena sobre un
ejemplo ADYACENTE, no sobre el enunciado.

El caso mas claro es la Clase 1: su actividad pide al estudiante escribir el DDL de `dueno`,
`mascota` y `cita`. Proyectar ese DDL seria publicar la respuesta. Asi que el patron —clave
primaria sustituta, FK, CHECK, DEFAULT— se ensena sobre `veterinario` e `insumo`, que son
tablas del mismo modelo VetCare y no son lo que la actividad pide. El estudiante ve el
mecanismo completo y sigue teniendo que decidir el suyo.

Convenciones que respeta todo el SQL de este archivo (son las del curso, y son lo que hace
que el script del estudiante corra a la primera):
  - PostgreSQL, no Oracle: `SERIAL`/`GENERATED ALWAYS AS IDENTITY`, `TEXT`/`VARCHAR`,
    `TIMESTAMP`, `NOW()`. No existen `NUMBER` ni `VARCHAR2` ni `SYSDATE`.
  - todo en minusculas y sin comillas dobles;
  - tablas en singular y sin tildes: `dueno`, `mascota`, `cita`, `veterinario`, `consulta`,
    `insumo`, `factura`, `detalle_factura`;
  - identificadores sustitutos `id_<entidad>`, con el mismo nombre en las dos tablas.

Limite declarado (CLAUDE.md): **este SQL no se ejecuto.** No hay PostgreSQL en el entorno de
generacion. Esta verificado por lectura contra el esquema y las convenciones del curso; la
comprobacion de ejecucion es en ExamLab, que corre PGlite en el navegador.
"""

#: `{clase: [(titulo, [lineas]), ...]}`. Cada entrada es una lamina de codigo.
QUERIES = {

    # ── Clase 1 · DDL, integridad y el primer JOIN ───────────────────────────
    # Evalua: DDL con PK/FK/CHECK/DEFAULT, insertar datos, JOIN de tres tablas y
    # reconocer que el DDL solo no defiende una regla de negocio.
    # Se ensena sobre `veterinario` e `insumo`: la actividad pide dueno/mascota/cita.
    1: [
        ("El patron de tabla: PK, obligatorios y dominio cerrado", [
            "-- Mismo patron que pedira su DDL, sobre otra tabla del modelo.",
            "CREATE TABLE veterinario (",
            "  id_veterinario SERIAL PRIMARY KEY,      -- sustituta: la genera la base",
            "  tarjeta_prof   VARCHAR(30) UNIQUE,      -- natural: unica, pero puede faltar",
            "  nombre         VARCHAR(80) NOT NULL,    -- obligatorio",
            "  especialidad   VARCHAR(40) NOT NULL",
            "    CHECK (especialidad IN ('GENERAL','CIRUGIA','DERMATOLOGIA')),",
            "  activo         CHAR(1) DEFAULT 'S'      -- baja logica, no DELETE",
            "    CHECK (activo IN ('S','N'))",
            ");",
        ]),
        ("La clave foranea y que pasa al borrar el padre", [
            "CREATE TABLE insumo (",
            "  id_insumo  SERIAL PRIMARY KEY,",
            "  nombre     VARCHAR(80) NOT NULL,",
            "  stock      INT NOT NULL DEFAULT 0 CHECK (stock >= 0),",
            "  precio_unit NUMERIC(12,2) NOT NULL CHECK (precio_unit > 0)",
            ");",
            "",
            "-- El comportamiento al borrar el padre SE ELIGE. Si no se declara,",
            "-- PostgreSQL asume NO ACTION: se niega a borrar. Eso es del estandar.",
            "ALTER TABLE detalle_factura",
            "  ADD CONSTRAINT fk_detalle_insumo",
            "  FOREIGN KEY (id_insumo) REFERENCES insumo (id_insumo)",
            "  ON DELETE RESTRICT;   -- no se borra un insumo ya facturado",
        ]),
        ("Integridad referencial: el error que devuelve el motor", [
            "-- Existe la mascota 1, no existe la 999.",
            "INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)",
            "VALUES (1, 1, TIMESTAMP '2026-09-01 09:00:00', 'PROGRAMADA');",
            "-- INSERT 0 1",
            "",
            "INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)",
            "VALUES (999, 1, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA');",
            "-- ERROR:  insert or update on table \"cita\" violates foreign key",
            "--         constraint \"cita_id_mascota_fkey\"",
            "-- DETAIL:  Key (id_mascota)=(999) is not present in table \"mascota\".",
        ]),
        ("El JOIN de tres tablas", [
            "SELECT m.nombre    AS mascota,",
            "       d.nombre    AS dueno,",
            "       c.fecha_hora,",
            "       c.estado",
            "FROM cita c",
            "JOIN mascota m ON m.id_mascota = c.id_mascota",
            "JOIN dueno   d ON d.id_dueno   = m.id_dueno",
            "WHERE c.fecha_hora >= DATE '2026-09-01'",
            "  AND m.activa = 'S'",
            "ORDER BY c.fecha_hora;",
        ]),
        ("Lo que el DDL NO puede defender solo", [
            "-- La FK garantiza que el identificador EXISTA. No que el negocio lo quiera.",
            "UPDATE mascota SET activa = 'N' WHERE id_mascota = 1;   -- baja logica",
            "",
            "INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)",
            "VALUES (1, 1, TIMESTAMP '2026-09-02 08:00:00', 'PROGRAMADA');",
            "-- INSERT 0 1   <-- la acepta: para el motor la mascota 1 existe",
            "",
            "-- Un CHECK tampoco: solo mira columnas de SU propia fila.",
            "-- La regla «una mascota inactiva no agenda» necesita consultar OTRA tabla,",
            "-- y eso es un procedimiento (Clase 3) o un trigger (Clase 4).",
        ]),
    ],

    # ── Clase 2 · Roles, privilegios y minimo privilegio ─────────────────────
    2: [
        # El rol es NOLOGIN (paquete de permisos) y la persona es un rol con LOGIN que lo recibe:
        # asi lo dicen el fundamento, la animacion `login-nologin` y la actividad. Esta lamina
        # proyectaba `CREATE ROLE recepcion LOGIN PASSWORD`, que contradecia a las tres.
        ("Crear el rol y otorgar solo lo que el cargo usa", [
            "-- Los cuatro roles del caso son paquetes de permisos: NOLOGIN, nadie se conecta con ellos.",
            "CREATE ROLE admin_bd NOLOGIN;  CREATE ROLE recepcion NOLOGIN;",
            "CREATE ROLE veterinario_rol NOLOGIN;  CREATE ROLE auditor NOLOGIN;",
            "-- La persona es un rol con LOGIN, y recibe el paquete.",
            "CREATE ROLE ana_gomez LOGIN PASSWORD 'cambiar_en_produccion';",
            "GRANT recepcion TO ana_gomez;",
            "",
            "-- La recepcionista agenda: no lee historias clinicas ni toca facturas.",
            "GRANT SELECT, INSERT, UPDATE ON cita TO recepcion;",
            "GRANT SELECT ON dueno, mascota, veterinario TO recepcion;",
            "GRANT USAGE ON SEQUENCE cita_id_cita_seq TO recepcion;",
            "-- Sin USAGE en la secuencia, el INSERT falla: el SERIAL la necesita.",
        ]),
        # Decia `REVOKE UPDATE ON cita FROM recepcion`, que le quita justo lo que necesita para
        # cancelar (cancelar es UPDATE). El REVOKE de la matriz es el de DELETE. Y el CASCADE
        # quitaba al auditor su propio SELECT: lo que se retira es la OPCION de reotorgar.
        ("REVOKE, y los dos que hacen dano en silencio", [
            "REVOKE DELETE ON cita FROM recepcion;   -- nunca se otorgo: deja escrita la decision",
            "",
            "-- PUBLIC es todo el mundo, presente y futuro. Casi nunca es lo que se quiere.",
            "REVOKE ALL ON consulta FROM PUBLIC;",
            "",
            "-- WITH GRANT OPTION deja que el que recibe vuelva a otorgar.",
            "GRANT SELECT ON cita TO auditor WITH GRANT OPTION;",
            "-- auditor puede ahora hacer: GRANT SELECT ON cita TO cualquiera;",
            "-- Para quitarle esa opcion hay que arrastrar lo que el concedio:",
            "REVOKE GRANT OPTION FOR SELECT ON cita FROM auditor CASCADE;",
        ]),
        # Antes: «Cuando el GRANT sobra», una vista `v_agenda_dia` distinta de la
        # `v_agenda_recepcion` que proyecta la lamina siguiente (CODIGO_SLIDE[2]): dos laminas con
        # el mismo mecanismo y nombres distintos. Ahora la lamina PRUEBA lo que aquella crea: con
        # SET ROLE, la vista y el privilegio por columna, y el DELETE que debe fallar.
        ("SET ROLE: demostrar en el motor que el permiso falta", [
            "-- Cambiar el rol EFECTIVO en la misma sesion: el motor evalua como recepcion.",
            "SET ROLE recepcion;",
            "SELECT count(*) FROM v_agenda_recepcion;   -- 9: la cita CANCELADA no sale",
            "DELETE FROM cita WHERE id_cita = 1;",
            "-- ERROR:  permission denied for table cita",
            "SELECT nombre, email FROM dueno;",
            "-- ERROR:  permission denied for table dueno",
            "RESET ROLE;                                -- de vuelta al rol propio",
            "",
            "SET ROLE veterinario_rol;",
            "SELECT id_dueno, nombre FROM dueno;        -- 6 filas: sus dos columnas",
            "SELECT * FROM dueno;                       -- el * pide columnas negadas",
            "-- ERROR:  permission denied for table dueno",
            "RESET ROLE;",
        ]),
        ("La matriz como hecho verificable, no como documento", [
            "-- Lo que el motor dice que concedio, que no siempre es lo que se creia.",
            "SELECT grantee, table_name, privilege_type",
            "FROM information_schema.role_table_grants",
            "WHERE grantee IN ('admin_bd','recepcion','veterinario_rol','auditor')",
            "ORDER BY grantee, table_name, privilege_type;",
            "",
            "-- Y los privilegios por columna, que la consulta anterior no muestra:",
            "SELECT grantee, table_name, column_name, privilege_type",
            "FROM information_schema.column_privileges",
            "WHERE grantee = 'veterinario_rol' AND table_name = 'dueno'",
            "ORDER BY column_name;",
        ]),
    ],

    # ── Clase 3 · Procedimientos almacenados ────────────────────────────────
    3: [
        # El cuerpo va entre $proc$ (lo dice su leyenda y lo dice la lamina del molde) y la
        # validacion es IF NOT FOUND, la que ensena la clase; p_motivo ya no queda sin usar.
        ("El molde de un procedimiento en PL/pgSQL", [
            "CREATE OR REPLACE PROCEDURE sp_dar_de_baja_insumo(",
            "  p_id_insumo INT,",
            "  p_motivo    VARCHAR",
            ")",
            "LANGUAGE plpgsql",
            "AS $proc$",
            "DECLARE",
            "  v_stock INT;",
            "BEGIN",
            "  SELECT stock INTO v_stock FROM insumo WHERE id_insumo = p_id_insumo;",
            "  IF NOT FOUND THEN",
            "    RAISE EXCEPTION 'El insumo % no existe', p_id_insumo;",
            "  END IF;",
            "  UPDATE insumo SET stock = 0 WHERE id_insumo = p_id_insumo;",
            "  RAISE NOTICE 'Insumo % dado de baja (% unidades): %',",
            "               p_id_insumo, v_stock, p_motivo;",
            "END;",
            "$proc$;",
        ]),
        ("RAISE EXCEPTION en accion: la mascota inactiva", [
            "-- La regla que la FK no puede defender: validar contra OTRA tabla.",
            "DO $$",
            "DECLARE p_id_mascota INT := 3;   -- existe, pero esta inactiva",
            "BEGIN",
            "  IF NOT EXISTS (SELECT 1 FROM mascota",
            "                 WHERE id_mascota = p_id_mascota AND activa = 'S') THEN",
            "    RAISE EXCEPTION 'La mascota % no existe o esta inactiva', p_id_mascota;",
            "  END IF;",
            "END $$;",
            "-- ERROR:  La mascota 3 no existe o esta inactiva",
            "",
            "-- Lo que hay que subrayar: RAISE EXCEPTION no solo avisa, DESHACE.",
            "-- Todo lo que el procedimiento haya escrito antes se revierte.",
            "-- Por eso el orden natural es: validar primero, escribir despues.",
        ]),
        # Su leyenda dice que el error «se registra con SQLERRM en resultado_prueba», y el codigo
        # solo hacia RAISE NOTICE: ahora el caso queda en la tabla, y paso verifica el TEXTO.
        ("La bateria de pruebas: un bloque DO por caso", [
            "-- Cada caso deja su resultado en una tabla, no en un mensaje que se pierde.",
            "CREATE TABLE resultado_prueba (caso TEXT, esperado TEXT, obtenido TEXT, paso BOOLEAN);",
            "",
            "-- Caso de error: debe fallar, y por la razon esperada.",
            "DO $$",
            "BEGIN",
            "  CALL sp_dar_de_baja_insumo(9999, 'inexistente');",
            "  INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)",
            "  VALUES ('insumo 9999', 'no existe', 'no lanzo error', FALSE);",
            "EXCEPTION WHEN OTHERS THEN",
            "  INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)",
            "  VALUES ('insumo 9999', 'no existe', SQLERRM,",
            "          SQLERRM ILIKE '%no existe%');",
            "END $$;",
            "",
            "SELECT caso, obtenido, paso FROM resultado_prueba;",
            "-- insumo 9999 | El insumo 9999 no existe | t",
        ]),
        ("PROCEDURE o FUNCTION: la diferencia es donde se puede usar", [
            "-- FUNCTION devuelve un valor y se puede usar DENTRO de un SELECT.",
            "CREATE OR REPLACE FUNCTION fn_citas_del_dia(p_dia DATE)",
            "RETURNS INT",
            "LANGUAGE sql",
            "AS $$",
            "  SELECT COUNT(*)::INT FROM cita",
            "  WHERE fecha_hora >= p_dia AND fecha_hora < p_dia + 1;",
            "$$;",
            "",
            "SELECT fn_citas_del_dia(DATE '2026-09-01');   -- se puede: devuelve 3",
            "",
            "-- PROCEDURE no: se invoca con CALL y puede manejar transacciones.",
            "SELECT sp_dar_de_baja_insumo(1, 'x');",
            "-- ERROR:  sp_dar_de_baja_insumo(integer, unknown) is a procedure",
        ]),
    ],

    # ── Clase 4 · Funciones y triggers ──────────────────────────────────────
    4: [
        ("La funcion de tarifas, y por que IMMUTABLE importa", [
            "CREATE OR REPLACE FUNCTION fn_recargo_festivo(p_base DECIMAL, p_dia DATE)",
            "RETURNS DECIMAL",
            "LANGUAGE plpgsql",
            "IMMUTABLE               -- mismo resultado para los mismos argumentos",
            "AS $$",
            "BEGIN",
            "  IF EXTRACT(DOW FROM p_dia) IN (0, 6) THEN   -- 0 domingo, 6 sabado",
            "    RETURN ROUND(p_base * 1.25, 2);",
            "  END IF;",
            "  RETURN ROUND(p_base, 2);",
            "END;",
            "$$;",
            "",
            "-- IMMUTABLE permite indexar la expresion y cachear el resultado. Una funcion",
            "-- que lee NOW() o una tabla NO es inmutable: seria STABLE o VOLATILE.",
        ]),
        ("BEFORE o AFTER: uno puede impedir, el otro solo registrar", [
            "-- BEFORE puede cambiar NEW o abortar. Es el que IMPIDE.",
            "CREATE OR REPLACE FUNCTION fn_trg_stock_no_negativo()",
            "RETURNS trigger",
            "LANGUAGE plpgsql",
            "AS $$",
            "BEGIN",
            "  IF NEW.stock < 0 THEN",
            "    RAISE EXCEPTION 'Stock negativo en el insumo % (%)', NEW.id_insumo, NEW.stock;",
            "  END IF;",
            "  RETURN NEW;          -- en BEFORE, devolver NULL cancela la operacion",
            "END;",
            "$$;",
            "",
            "CREATE TRIGGER trg_stock_no_negativo",
            "BEFORE UPDATE OF stock ON insumo",
            "FOR EACH ROW EXECUTE FUNCTION fn_trg_stock_no_negativo();",
        ]),
    ],

    # ── Clase 6 · Optimizacion de consultas ─────────────────────────────────
    6: [
        # 2026-10: la fecha era '2026-09-01' (la siembra va del 2026-01-05 al 2026-07-23: ese
        # dia solo tiene 3 citas escritas a mano) y el comentario prometia «el indice si se
        # usa» en la clase que no tiene indices. Ahora es el dia de toda la clase, 2026-03-10,
        # y las dos versiones devuelven lo mismo (150 citas; verificado en PGlite).
        ("El antipatron y su reescritura", [
            "-- ANTES: funcion sobre la columna -> el motor la calcula 30.010 veces",
            "SELECT id_cita, fecha_hora, estado FROM cita",
            "WHERE TO_CHAR(fecha_hora, 'YYYY-MM-DD') = '2026-03-10';",
            "",
            "-- DESPUES: rango sobre la columna desnuda -> sargable",
            "SELECT id_cita, fecha_hora, estado FROM cita",
            "WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'",
            "  AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00';",
            "",
            "-- Las dos devuelven las mismas 150 citas. Con un indice sobre",
            "-- fecha_hora (Clase 7) solo la segunda podria usarlo.",
        ]),
        ("EXPLAIN ANALYZE: la evidencia, no la opinion", [
            "EXPLAIN (ANALYZE, BUFFERS)",
            "SELECT c.id_cita, c.fecha_hora, m.nombre",
            "FROM cita c JOIN mascota m ON m.id_mascota = c.id_mascota",
            "WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'",
            "  AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00';",
            "",
            "-- Lo que se lee, en este orden (base de la clase, sin indices):",
            "--   el nodo:    Seq Scan on cita c  -> recorre la tabla entera",
            "--   las filas:  rows=150 estimadas contra actual rows=150 reales",
            "--   el filtro:  Rows Removed by Filter: 29860",
            "--   la lectura: Buffers: shared hit=251  (paginas de 8 KB)",
            "--   el total:   Execution Time: ... ms  (cambia entre corridas)",
        ]),
        ("Matar la subconsulta correlacionada", [
            "-- ANTES: la subconsulta se ejecuta UNA VEZ POR DUENO (loops=2006)",
            "SELECT d.nombre,",
            "       (SELECT COUNT(*) FROM mascota m WHERE m.id_dueno = d.id_dueno) AS n",
            "FROM dueno d",
            "ORDER BY n DESC;",
            "",
            "-- DESPUES: una sola pasada, agrupando",
            "SELECT d.nombre, COUNT(m.id_mascota) AS n",
            "FROM dueno d",
            "LEFT JOIN mascota m ON m.id_dueno = d.id_dueno",
            "GROUP BY d.id_dueno, d.nombre",
            "ORDER BY n DESC;",
            "",
            "-- LEFT JOIN, no JOIN: con JOIN desaparecen los duenos sin mascota.",
            "-- COUNT(m.id_mascota), no COUNT(*): el dueno sin mascotas da 0, no 1.",
        ]),
    ],

    # ── Clase 7 · Indices y particionamiento ────────────────────────────────
    7: [
        # 2026-10: la fecha era '2026-09-01' (3 citas escritas a mano) y la salida «rows=41» era
        # inventada; el comentario del orden de columnas afirmaba que sin la columna lider el
        # indice «no sirve», y PostgreSQL 18 (el de PGlite) si puede usarlo con skip scan; y el
        # DDL de la particion no traia la PK ni id_veterinario, asi que el INSERT ... SELECT de
        # la migracion fallaba. Todo verificado en PGlite sobre la siembra de la clase.
        ("Crear el indice y probar que se usa", [
            "CREATE INDEX idx_cita_fecha_hora ON cita (fecha_hora);",
            "CREATE INDEX idx_mascota_dueno    ON mascota (id_dueno);",
            "ANALYZE cita;      -- sin estadisticas frescas el planificador decide a ciegas",
            "ANALYZE mascota;",
            "",
            "EXPLAIN ANALYZE",
            "SELECT * FROM cita",
            "WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'",
            "  AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00';",
            "",
            "-- Antes:   Seq Scan on cita  (rows=150)  Rows Removed by Filter: 29860",
            "-- Despues: Bitmap Heap Scan on cita  (rows=150)",
            "--            ->  Bitmap Index Scan on idx_cita_fecha_hora",
        ]),
        ("El orden de columnas en un indice compuesto", [
            "-- La agenda de UN veterinario: igualdad en uno, rango u orden en la fecha",
            "CREATE INDEX idx_cita_vet_fecha ON cita (id_veterinario, fecha_hora);",
            "ANALYZE cita;",
            "",
            "EXPLAIN ANALYZE SELECT * FROM cita",
            " WHERE id_veterinario = 5",
            "   AND fecha_hora >= TIMESTAMP '2026-03-10'",
            "   AND fecha_hora <  TIMESTAMP '2026-03-11';",
            "-- Index Cond con las DOS columnas: 50 filas, Index Searches: 1",
            "",
            "EXPLAIN ANALYZE SELECT id_cita, fecha_hora FROM cita",
            " WHERE id_veterinario = 5 ORDER BY fecha_hora LIMIT 10;",
            "-- Index Scan using idx_cita_vet_fecha: sale ordenado, sin Sort",
            "",
            "-- Solo fecha_hora (sin la lider): no hay busqueda directa. PostgreSQL 18",
            "-- puede saltar por cada veterinario (skip scan), pero sirve menos.",
        ]),
        ("Particionar el historico por rango de fecha", [
            "CREATE TABLE cita_hist (",
            "  id_cita        INT,",
            "  id_mascota     INT,",
            "  id_veterinario INT,",
            "  fecha_hora     TIMESTAMP NOT NULL,",
            "  estado         TEXT,",
            "  PRIMARY KEY (id_cita, fecha_hora)   -- DEBE incluir la clave de particion",
            ") PARTITION BY RANGE (fecha_hora);",
            "",
            "CREATE TABLE cita_hist_2025 PARTITION OF cita_hist",
            "  FOR VALUES FROM (TIMESTAMP '2025-01-01') TO (TIMESTAMP '2026-01-01');",
            "CREATE TABLE cita_hist_2026 PARTITION OF cita_hist",
            "  FOR VALUES FROM (TIMESTAMP '2026-01-01') TO (TIMESTAMP '2027-01-01');",
            "",
            "-- FROM incluye, TO excluye: el TO de una es el FROM de la siguiente.",
        ]),
        ("El costo de sobre-indexar, que casi nunca se menciona", [
            "-- Cada indice se ACTUALIZA en cada INSERT, UPDATE y DELETE.",
            "-- Seis indices sobre cita = seis escrituras extra por cita agendada.",
            "",
            "-- Que indices existen y cuanto pesan:",
            "SELECT indexrelname, idx_scan,",
            "       pg_size_pretty(pg_relation_size(indexrelid)) AS tamano",
            "FROM pg_stat_user_indexes",
            "WHERE relname = 'cita'",
            "ORDER BY idx_scan;",
            "",
            "-- idx_scan = 0 despues de dias de uso: el indice no sirve a nadie y",
            "-- se esta pagando en cada escritura. Candidato a DROP INDEX.",
        ]),
    ],

    # ── Clase 8 · Transacciones y tuning ────────────────────────────────────
    8: [
        ("Todo o nada: la transaccion explicita", [
            "BEGIN;",
            "",
            "INSERT INTO factura (id_consulta, total)",
            "VALUES (1, 0) RETURNING id_factura;          -- devuelve el id generado",
            "",
            "INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit)",
            "VALUES (currval('factura_id_factura_seq'), 5, 2, 1200.00);",
            "",
            "UPDATE insumo SET stock = stock - 2 WHERE id_insumo = 5;",
            "UPDATE factura SET total = 2 * 1200.00",
            " WHERE id_factura = currval('factura_id_factura_seq');",
            "",
            "COMMIT;      -- o ROLLBACK; y no queda rastro de ninguna de las cuatro",
        ]),
        ("SAVEPOINT: deshacer una parte sin perder el resto", [
            "BEGIN;",
            "INSERT INTO factura (id_consulta, total) VALUES (1, 0);",
            "SAVEPOINT antes_del_detalle;",
            "INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit)",
            "VALUES (currval('factura_id_factura_seq'), 9999, 1, 1000.00);",
            "-- ERROR:  insert or update on table \"detalle_factura\" violates foreign key",
            "--         constraint \"detalle_factura_id_insumo_fkey\"",
            "ROLLBACK TO SAVEPOINT antes_del_detalle;   -- la factura sigue viva",
            "INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit)",
            "VALUES (currval('factura_id_factura_seq'), 5, 1, 1200.00);",
            "COMMIT;",
        ]),
        ("El bloque EXCEPTION y la trampa de tragarse el error", [
            "DO $$",
            "BEGIN",
            "  INSERT INTO factura (id_consulta, total) VALUES (1, 0);   -- cabecera",
            "  BEGIN                     -- bloque con EXCEPTION = savepoint implicito",
            "    UPDATE insumo SET stock = stock - 1 WHERE id_insumo = 5;",
            "    INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit)",
            "    VALUES (currval('factura_id_factura_seq'), 9999, 1, 1000);  -- no existe",
            "  EXCEPTION WHEN OTHERS THEN",
            "    RAISE NOTICE 'algo fallo: %', SQLERRM;   -- <-- LA TRAMPA",
            "  END;",
            "END $$;",
            "-- El bloque interno se deshizo (el stock quedo igual), pero el DO termino",
            "-- bien: la cabecera quedo guardada SIN lineas. La factura miente.",
            "-- Si se captura, hay que RE-LANZAR para que se deshaga todo:",
            "--   EXCEPTION WHEN OTHERS THEN RAISE;",
        ]),
    ],

    # ── Clase 10 · Concurrencia (autonoma) ──────────────────────────────────
    10: [
        # Antes repetia el ALTER TABLE de la lamina siguiente (CODIGO_SLIDE[10]). Ahora es el
        # PROBLEMA, ejecutable sobre los datos sembrados; la solucion es la lamina que sigue.
        ("La doble reserva, reproducida y detectada", [
            "-- Sin restriccion, la base ACEPTA dos citas en la misma franja: ningun error",
            "INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado) VALUES",
            "  (4, 2, TIMESTAMP '2026-09-15 10:00:00', 'PROGRAMADA'),",
            "  (5, 2, TIMESTAMP '2026-09-15 10:00:00', 'PROGRAMADA');",
            "",
            "-- Deteccion: franjas con mas de una cita vigente",
            "SELECT id_veterinario, fecha_hora, COUNT(*) AS citas",
            "FROM cita",
            "WHERE estado <> 'CANCELADA'",
            "GROUP BY id_veterinario, fecha_hora",
            "HAVING COUNT(*) > 1;      -- 1 fila: veterinario 2, 2026-09-15 10:00, 2 citas",
            "",
            "-- Antes de crear el indice unico se borra el duplicado: con el, no se crea",
            "DELETE FROM cita WHERE id_cita = (SELECT MAX(id_cita) FROM cita);",
        ]),
        ("El bloqueo explicito y la actualizacion condicional", [
            "-- Opcion A: bloquear la fila y obligar a esperar",
            "BEGIN;",
            "SELECT stock FROM insumo WHERE id_insumo = 2 FOR UPDATE;   -- 3",
            "UPDATE insumo SET stock = stock - 3 WHERE id_insumo = 2;",
            "COMMIT;",
            "",
            "-- Opcion B: sin bloqueo, la condicion va DENTRO del UPDATE",
            "UPDATE insumo SET stock = stock - 3",
            "WHERE id_insumo = 2 AND stock >= 3;",
            "-- UPDATE 1 si alcanzaba; UPDATE 0 si no (aqui: A ya lo dejo en 0).",
            "-- Se comprueba el numero de filas, no se supone.",
        ]),
        ("Niveles de aislamiento: que anomalia tapa cada uno", [
            "SHOW transaction_isolation;      -- en PostgreSQL: read committed",
            "",
            "BEGIN ISOLATION LEVEL REPEATABLE READ;",
            "  -- la misma consulta devuelve lo mismo durante toda la transaccion",
            "COMMIT;",
            "",
            "BEGIN ISOLATION LEVEL SERIALIZABLE;",
            "  -- PostgreSQL detecta el conflicto y ABORTA una de las dos:",
            "  -- «could not serialize access due to read/write dependencies»",
            "COMMIT;",
            "",
            "-- PostgreSQL no tiene READ UNCOMMITTED real: se comporta como READ COMMITTED.",
            "-- Y serializable no evita el error: obliga a REINTENTAR en la aplicacion.",
        ]),
    ],

    # ── Clase 11 · Verificacion del avance del PI ───────────────────────────
    11: [
        ("La bateria de verificacion del avance", [
            "-- 1. estan las 8 tablas del modelo?",
            "SELECT table_name FROM information_schema.tables",
            "WHERE table_schema = 'public' ORDER BY table_name;",
            "",
            "-- 2. tienen todas clave primaria?",
            "SELECT t.table_name",
            "FROM information_schema.tables t",
            "LEFT JOIN information_schema.table_constraints c",
            "       ON c.table_name = t.table_name AND c.constraint_type = 'PRIMARY KEY'",
            "WHERE t.table_schema = 'public' AND c.constraint_name IS NULL;",
            "-- cero filas = todas tienen PK",
        ]),
        ("Integridad y objetos de negocio, contados", [
            "-- 3. las claves foraneas declaradas",
            "SELECT tc.table_name, kcu.column_name, ccu.table_name AS referencia",
            "FROM information_schema.table_constraints tc",
            "JOIN information_schema.key_column_usage kcu",
            "     ON kcu.constraint_name = tc.constraint_name",
            "JOIN information_schema.constraint_column_usage ccu",
            "     ON ccu.constraint_name = tc.constraint_name",
            "WHERE tc.constraint_type = 'FOREIGN KEY'",
            "ORDER BY tc.table_name;",
            "",
            "-- 4. procedimientos, funciones y triggers que existen de verdad",
            "SELECT routine_name, routine_type FROM information_schema.routines",
            "WHERE routine_schema = 'public' ORDER BY routine_name;",
            "SELECT trigger_name, event_object_table FROM information_schema.triggers;",
        ]),
    ],

    # ── Clase 12 · Integracion app <-> BD ───────────────────────────────────
    12: [
        ("El contrato de la capa de API: siempre parametros ligados", [
            "-- La BD expone operaciones, no tablas. La aplicacion llama, no improvisa SQL.",
            "CREATE OR REPLACE FUNCTION api_agenda_del_dia(p_dia DATE)",
            "RETURNS TABLE (id_cita INT, hora TIMESTAMP, mascota VARCHAR, dueno VARCHAR)",
            "LANGUAGE sql",
            "STABLE",
            "AS $$",
            "  SELECT c.id_cita, c.fecha_hora, m.nombre, d.nombre",
            "  FROM cita c",
            "  JOIN mascota m ON m.id_mascota = c.id_mascota",
            "  JOIN dueno   d ON d.id_dueno   = m.id_dueno",
            "  WHERE c.fecha_hora >= p_dia AND c.fecha_hora < p_dia + 1",
            "  ORDER BY c.fecha_hora;",
            "$$;",
        ]),
        ("La inyeccion de SQL, explicada con las dos versiones", [
            "-- MAL: la aplicacion concatena lo que el usuario escribio",
            "--   \"SELECT * FROM dueno WHERE nombre = '\" + entrada + \"'\"",
            "-- Si entrada = x'; UPDATE cita SET estado = 'CANCELADA'; --",
            "-- el motor recibe DOS sentencias y ejecuta las dos: agenda cancelada",
            "",
            "-- BIEN: el valor viaja como PARAMETRO, nunca como texto de la sentencia",
            "PREPARE buscar_dueno (VARCHAR) AS",
            "  SELECT id_dueno, nombre, telefono FROM dueno WHERE nombre = $1;",
            "",
            "EXECUTE buscar_dueno('Ana Gomez');             -- 1 fila",
            "EXECUTE buscar_dueno(                  -- 0 filas: el UPDATE no corre",
            "  'x''; UPDATE cita SET estado = ''CANCELADA''; --');",
        ]),
        # El contrato de retorno que la capa de API usa: el rechazo de negocio se DEVUELVE en la
        # fila; lo inesperado se captura, el bloque se deshace y tambien se devuelve. Operacion
        # adyacente (cancelar), no las que la actividad pide escribir.
        ("El contrato como fila: ok, mensaje e id_generado", [
            "CREATE OR REPLACE FUNCTION api_cancelar_cita(p_id_cita INT)",
            "RETURNS TABLE (ok BOOLEAN, mensaje TEXT, id_generado INT)",
            "LANGUAGE plpgsql AS $fn$",
            "BEGIN",
            "  UPDATE cita SET estado = 'CANCELADA'",
            "   WHERE id_cita = p_id_cita AND estado = 'PROGRAMADA';",
            "  IF NOT FOUND THEN         -- rechazo de negocio esperado: se devuelve",
            "    RETURN QUERY SELECT FALSE, 'No se puede cancelar', NULL::INT;",
            "    RETURN;",
            "  END IF;",
            "  RETURN QUERY SELECT TRUE, 'Cita cancelada', p_id_cita;",
            "EXCEPTION WHEN OTHERS THEN  -- lo inesperado: se deshace y se informa",
            "  RETURN QUERY SELECT FALSE, SQLERRM, NULL::INT;",
            "END; $fn$;",
            "",
            "SELECT * FROM api_cancelar_cita(3);   -- t | Cita cancelada       | 3",
            "SELECT * FROM api_cancelar_cita(3);   -- f | No se puede cancelar | NULL",
        ]),
        # El diagrama de secuencia que documenta esa operacion: alt / else / end para la rama de
        # error y Note over para la regla de acceso. Validado con mermaid 11 (parse y render).
        ("El flujo de la operacion en sequenceDiagram, con alt y else", [
            "sequenceDiagram",
            "  actor R as Recepcionista",
            "  participant A as Aplicacion",
            "  participant B as Capa de API",
            "  participant T as Tabla cita",
            "  R->>A: Cancelar la cita 3",
            "  A->>B: api_cancelar_cita(3) como parametro",
            "  B->>T: UPDATE solo si esta PROGRAMADA",
            "  alt ok = false",
            "    B-->>A: false, No se puede cancelar",
            "    A-->>R: Muestra el mensaje y no sigue",
            "  else ok = true",
            "    B-->>A: true, Cita cancelada, 3",
            "    A-->>R: Confirma la cancelacion",
            "  end",
            "  Note over A,B: La aplicacion no hace UPDATE directo sobre cita",
        ]),
    ],

    # ── Clase 13 · Analisis de casos reales (autonoma) ──────────────────────
    # Evalua: analizar un caso (respaldo, rendimiento o inyeccion), cerrar una inyeccion
    # con EXECUTE ... USING, archivar los borrados con un trigger BEFORE DELETE y comprobar
    # la restauracion con una consulta de veredicto. Se ensena sobre `dueno` y sobre una
    # tabla propia y sin dependencias, `tarifa`: la actividad pide `mascota` y `cita`, y la
    # base de la clase no trae `insumo`. Verificado en PGlite (PostgreSQL 18) sobre los
    # setups de la Clase 13, las cuatro laminas en orden y acumuladas.
    13: [
        ("SQL dinamico: concatenar el texto o ligar el parametro", [
            "-- MAL: el texto del usuario queda DENTRO de la sentencia",
            "CREATE FUNCTION buscar_dueno_inseguro(p_nombre TEXT)",
            "RETURNS TABLE (id_dueno INT, nombre TEXT) LANGUAGE plpgsql AS $fn$",
            "BEGIN",
            "  RETURN QUERY EXECUTE",
            "    'SELECT id_dueno, nombre FROM dueno WHERE nombre = ''' || p_nombre || '''';",
            "END; $fn$;",
            "",
            "-- BIEN: la sentencia lleva un hueco ($1) y el valor viaja aparte",
            "CREATE FUNCTION buscar_dueno_seguro(p_nombre TEXT)",
            "RETURNS TABLE (id_dueno INT, nombre TEXT) LANGUAGE plpgsql AS $fn$",
            "BEGIN",
            "  RETURN QUERY EXECUTE",
            "    'SELECT id_dueno, nombre FROM dueno WHERE nombre = $1' USING p_nombre;",
            "END; $fn$;",
            "",
            "SELECT COUNT(*) FROM buscar_dueno_inseguro('x'' OR ''1''=''1');  -- todos",
            "SELECT COUNT(*) FROM buscar_dueno_seguro('x'' OR ''1''=''1');    -- 0",
        ]),
        ("El borrado con rastro: BEFORE DELETE y RETURN OLD", [
            "CREATE TABLE tarifa (especie TEXT PRIMARY KEY, valor NUMERIC(12,2) NOT NULL);",
            "INSERT INTO tarifa VALUES ('CANINO', 45000), ('FELINO', 40000), ('OTRA', 35000);",
            "",
            "CREATE TABLE tarifa_borrada (",
            "  especie    TEXT,",
            "  valor      NUMERIC(12,2),",
            "  borrado_en TIMESTAMP DEFAULT now(),",
            "  usuario_bd TEXT      DEFAULT current_user",
            ");",
            "",
            "CREATE FUNCTION fn_trg_archivar_tarifa() RETURNS TRIGGER",
            "LANGUAGE plpgsql AS $fn$",
            "BEGIN",
            "  INSERT INTO tarifa_borrada (especie, valor) VALUES (OLD.especie, OLD.valor);",
            "  RETURN OLD;      -- deja seguir el borrado; NULL lo cancelaria",
            "END;",
            "$fn$;",
            "",
            "CREATE TRIGGER trg_archivar_tarifa",
            "BEFORE DELETE ON tarifa",
            "FOR EACH ROW EXECUTE FUNCTION fn_trg_archivar_tarifa();",
        ]),
        ("La restauracion comprobada: una consulta, un veredicto", [
            "-- 1. al respaldar: la copia y su conteo, calculado y no escrito a mano",
            "CREATE TABLE respaldo_tarifa AS SELECT * FROM tarifa;",
            "CREATE TABLE registro_respaldo (",
            "  tabla TEXT, filas INT, hecho_en TIMESTAMP DEFAULT now());",
            "INSERT INTO registro_respaldo (tabla, filas)",
            "SELECT 'tarifa', COUNT(*) FROM respaldo_tarifa;",
            "",
            "-- 2. el accidente y la vuelta: el trigger ya archivo cada fila",
            "DELETE FROM tarifa;                        -- sin WHERE: borra todo",
            "INSERT INTO tarifa (especie, valor)",
            "SELECT especie, valor FROM tarifa_borrada;",
            "",
            "-- 3. la comprobacion: una fila, un veredicto",
            "SELECT r.filas                       AS esperadas,",
            "       (SELECT COUNT(*) FROM tarifa) AS actuales,",
            "       CASE WHEN (SELECT COUNT(*) FROM tarifa) = r.filas",
            "            THEN 'RESTAURACION OK' ELSE 'REVISAR' END AS veredicto",
            "FROM registro_respaldo r",
            "WHERE r.tabla = 'tarifa'",
            "ORDER BY r.hecho_en DESC LIMIT 1;",
        ]),
        ("Leer un plan de ejecucion ajeno", [
            "EXPLAIN (ANALYZE, BUFFERS)",
            "SELECT d.nombre, COUNT(c.id_cita) AS citas",
            "FROM dueno d",
            "JOIN mascota m ON m.id_dueno   = d.id_dueno",
            "JOIN cita    c ON c.id_mascota = m.id_mascota",
            "WHERE c.fecha_hora >= DATE '2026-01-01'",
            "GROUP BY d.id_dueno, d.nombre",
            "HAVING COUNT(c.id_cita) > 5;",
            "",
            "-- 1. el nodo mas costoso (cost mas alto), no el primero",
            "-- 2. Seq Scan sobre tabla grande con filtro selectivo -> falta indice",
            "-- 3. rows estimadas vs actual: si difieren 10x, ANALYZE la tabla",
            "-- 4. Nested Loop con muchas filas -> suele querer Hash Join",
        ]),
    ],
}
