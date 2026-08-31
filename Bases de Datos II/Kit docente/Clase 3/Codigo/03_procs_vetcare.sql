-- VetCare DB · Clase 3 · Procedimientos almacenados · PostgreSQL
-- Script de la DEMO: corre tal cual en ExamLab (PostgreSQL/PGlite en el navegador),
-- sobre el esquema de VetCare ya creado y poblado: 8 mascotas (Rocky=3 y Kiara=8
-- estan INACTIVAS), 4 veterinarios, 10 citas, y una cita del veterinario 1 el
-- 2026-09-01 08:00:00.
--
-- NO es Oracle: nada de IS en vez de AS, VARCHAR2, NUMBER, RAISE_APPLICATION_ERROR
-- ni barra / de terminacion. Ese codigo aqui no compila, y es la forma mas facil de
-- perder los puntos de sintaxis de la pregunta 1.
--
-- Se ejecuta de arriba abajo narrando cada bloque. El bloque 3 es el que convence al
-- grupo: es donde se VE que la validacion detiene el INSERT. Correr el script
-- completo una vez antes de la clase.

-- ============ 1) El procedimiento con sus 3 validaciones ============
-- id_cita no se pasa como parametro: es SERIAL y lo genera el motor.
CREATE OR REPLACE PROCEDURE sp_agendar_cita(
  p_id_mascota     INT,
  p_id_veterinario INT,
  p_fecha_hora     TIMESTAMP
)
LANGUAGE plpgsql
AS $proc$
DECLARE
  v_activa CHAR(1);
BEGIN
  -- Validacion 1: la mascota existe. SELECT ... INTO deja FOUND en FALSE cuando no
  -- devolvio ninguna fila, y eso es lo que pregunta IF NOT FOUND.
  SELECT activa INTO v_activa
    FROM mascota
   WHERE id_mascota = p_id_mascota;

  IF NOT FOUND THEN
    RAISE EXCEPTION 'ERROR: la mascota % no existe', p_id_mascota;
  END IF;

  -- Validacion 2: la regla de negocio del PI.
  IF v_activa <> 'S' THEN
    RAISE EXCEPTION 'ERROR: la mascota % esta inactiva; no se agenda cita',
                    p_id_mascota;
  END IF;

  -- Validacion 3: la franja del veterinario esta libre. Una cita CANCELADA libera
  -- la franja, asi que no cuenta.
  IF EXISTS (SELECT 1 FROM cita
              WHERE id_veterinario = p_id_veterinario
                AND fecha_hora     = p_fecha_hora
                AND estado <> 'CANCELADA') THEN
    RAISE EXCEPTION 'ERROR: el veterinario % ya tiene cita en %',
                    p_id_veterinario, p_fecha_hora;
  END IF;

  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
  VALUES (p_id_mascota, p_id_veterinario, p_fecha_hora, 'PROGRAMADA');
END;
$proc$;

-- ============ 2) El caso valido ============
CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');

SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado
  FROM cita ORDER BY id_cita DESC LIMIT 3;   -- la nueva es la primera fila

-- ============ 3) Los tres errores, SENTENCIA POR SENTENCIA ============
-- Estas tres lineas DEBEN fallar, y por eso no van en un solo tiro: la gracia es
-- leer en pantalla el mensaje exacto que la app va a recibir. Un runner que aborta
-- al primer error se llevaria las siguientes.
CALL sp_agendar_cita(3,  2, TIMESTAMP '2026-09-21 08:00:00');  -- Rocky, INACTIVA
CALL sp_agendar_cita(99, 2, TIMESTAMP '2026-09-22 08:00:00');  -- no existe
CALL sp_agendar_cita(2,  1, TIMESTAMP '2026-09-01 08:00:00');  -- franja ocupada

-- Y la prueba de que no dejaron basura: sigue habiendo 11 citas, no 14.
SELECT COUNT(*) AS citas_totales FROM cita;

-- ============ 4) La bateria: un bloque DO por caso ============
-- Por que un bloque por caso: si los CALL van seguidos, el primero que falla aborta
-- el resto. DO es un bloque anonimo -- se ejecuta una vez y no se guarda -- y su
-- EXCEPTION atrapa el error y deja seguir al caso siguiente.
CREATE TABLE IF NOT EXISTS resultado_prueba (
  id_prueba SERIAL PRIMARY KEY,
  caso      TEXT,
  esperado  TEXT,
  obtenido  TEXT,
  paso      BOOLEAN
);

-- Caso POSITIVO: el exito es que NO haya excepcion.
DO $$
BEGIN
  CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-20 08:00:00');
  INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
  VALUES ('P1 mascota activa', 'OK: cita creada', 'OK: cita creada', TRUE);
EXCEPTION WHEN OTHERS THEN
  INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
  VALUES ('P1 mascota activa', 'OK: cita creada', SQLERRM, FALSE);
END $$;

-- Caso NEGATIVO: el exito es que SI haya excepcion, y ademas que sea LA esperada.
-- Por eso se verifica el TEXTO con ILIKE y no basta WHEN OTHERS a secas: un typo en
-- el nombre de una columna tambien lanza excepcion, y un WHEN OTHERS pelado lo
-- reportaria como prueba superada.
DO $$
BEGIN
  CALL sp_agendar_cita(3, 2, TIMESTAMP '2026-09-21 08:00:00');
  INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
  VALUES ('P2 mascota inactiva', 'EXCEPCION: mascota inactiva',
          'NO lanzo excepcion: la cita se creo', FALSE);
EXCEPTION WHEN OTHERS THEN
  INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
  VALUES ('P2 mascota inactiva', 'EXCEPCION: mascota inactiva',
          SQLERRM, SQLERRM ILIKE '%inactiva%');
END $$;

SELECT caso, esperado, obtenido, paso
  FROM resultado_prueba ORDER BY id_prueba;

-- Nota de lectura: aqui `paso` significa «el resultado coincidio con lo esperado»,
-- asi que las dos filas quedan en t. La otra lectura -- «la operacion se completo»,
-- que deja las negativas en f -- tambien es valida. Lo que hay que hacer es usar UNA
-- de las dos para las cuatro filas y decir cual, porque si no, `paso` no significa
-- nada.

-- ============ 5) El contrato, que es el otro entregable ============
-- Firma        : sp_agendar_cita(p_id_mascota INT, p_id_veterinario INT,
--                               p_fecha_hora TIMESTAMP)
-- Llamada      : CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');
-- Precondicion : la mascota existe y tiene activa = 'S'; la franja del veterinario
--                esta libre (una cita CANCELADA no la ocupa).
-- Postcondicion: 1 fila nueva en cita con estado 'PROGRAMADA'. Si falla, NINGUNA.
-- Errores      : 'ERROR: la mascota % no existe'
--                'ERROR: la mascota % esta inactiva; no se agenda cita'
--                'ERROR: el veterinario % ya tiene cita en %'
-- Decision     : se aborta con RAISE EXCEPTION en vez de devolver un codigo en un
--                parametro OUT, porque abortar deshace lo hecho; un codigo que
--                nadie revise deja la cita creada igual.
