-- VetCare DB · Clase 12 · Contrato app<->BD · PostgreSQL (PL/pgSQL), ejecutable
-- Corre completo y EN ORDEN en PostgreSQL, incluido PGlite (la consola de ExamLab).
-- Regla: la app NUNCA hace INSERT ni UPDATE directo sobre cita; solo llama la capa de API.
--
-- Las dos formas de informar un fallo que fija el contrato:
--   * el error que ABORTA: RAISE EXCEPTION ... USING ERRCODE, con un codigo propio que la
--     aplicacion captura (sp_agendar_cita, BLOQUE 1);
--   * el rechazo de negocio que se DEVUELVE en la fila del contrato (ok, mensaje,
--     id_generado), que la aplicacion esta obligada a revisar (api_cancelar_cita, BLOQUE 2).
--
-- NO es Oracle: nada de IN NUMBER, VARCHAR2, un p_msg OUT con el error, COMMIT/ROLLBACK
-- dentro del procedimiento ni barra / final. En PostgreSQL el CALL es su propia
-- transaccion: si una validacion lanza el error, no queda nada escrito.

-- =====================================================================
-- BLOQUE 0 · Esquema minimo y datos. RECREA las tablas: correr en una base vacia.
-- =====================================================================
DROP FUNCTION  IF EXISTS api_cancelar_cita(INT);
DROP PROCEDURE IF EXISTS sp_agendar_cita(INT, INT, TIMESTAMP);
DROP TABLE IF EXISTS cita, mascota, veterinario, dueno;

CREATE TABLE dueno (
  id_dueno SERIAL PRIMARY KEY,
  nombre   TEXT NOT NULL
);
CREATE TABLE mascota (
  id_mascota SERIAL PRIMARY KEY,
  id_dueno   INT NOT NULL REFERENCES dueno(id_dueno),
  nombre     TEXT NOT NULL,
  especie    TEXT NOT NULL,
  activa     CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN ('S','N'))
);
CREATE TABLE veterinario (
  id_veterinario SERIAL PRIMARY KEY,
  nombre         TEXT NOT NULL
);
CREATE TABLE cita (
  id_cita        SERIAL PRIMARY KEY,
  id_mascota     INT NOT NULL REFERENCES mascota(id_mascota),
  id_veterinario INT NOT NULL REFERENCES veterinario(id_veterinario),
  fecha_hora     TIMESTAMP NOT NULL,
  estado         TEXT NOT NULL DEFAULT 'PROGRAMADA'
                 CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))
);
-- La franja la GARANTIZA el motor (Clase 10); la validacion del procedimiento solo da un
-- mensaje claro. Una cita CANCELADA libera la franja, por eso el indice es parcial.
CREATE UNIQUE INDEX uq_cita_vet_franja ON cita (id_veterinario, fecha_hora)
  WHERE estado <> 'CANCELADA';

INSERT INTO dueno (nombre) VALUES
  ('Ana Gomez'), ('Carlos Ruiz'), ('Marcela Diaz'),
  ('Jorge Pineda'), ('Luisa Cardona'), ('Andres Vallejo');
INSERT INTO veterinario (nombre) VALUES
  ('Laura Restrepo'), ('Diego Moreno'), ('Paula Salazar'), ('Ivan Ortiz');
-- Rocky (3) y Kiara (8) estan INACTIVAS.
INSERT INTO mascota (id_dueno, nombre, especie, activa) VALUES
  (1,'Firulais','Canino','S'), (1,'Luna','Felino','S'), (2,'Rocky','Canino','N'),
  (3,'Mishi','Felino','S'),    (3,'Bobby','Canino','S'), (4,'Nube','Felino','S'),
  (5,'Toby','Canino','S'),     (6,'Kiara','Canino','N');
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado) VALUES
  (1,1,TIMESTAMP '2026-09-01 08:00','PROGRAMADA'), (2,1,TIMESTAMP '2026-09-01 09:00','ATENDIDA'),
  (4,2,TIMESTAMP '2026-09-01 10:00','PROGRAMADA'), (5,3,TIMESTAMP '2026-09-02 08:30','CANCELADA'),
  (6,2,TIMESTAMP '2026-09-02 11:00','ATENDIDA'),   (7,4,TIMESTAMP '2026-09-03 07:45','PROGRAMADA'),
  (1,1,TIMESTAMP '2026-09-05 15:00','ATENDIDA'),   (2,3,TIMESTAMP '2026-09-08 16:00','PROGRAMADA'),
  (4,4,TIMESTAMP '2026-09-10 08:00','PROGRAMADA'), (6,1,TIMESTAMP '2026-09-10 09:00','ATENDIDA');

-- =====================================================================
-- BLOQUE 1 · El error que ABORTA, con codigo propio (USING ERRCODE)
-- =====================================================================
-- Sin USING ERRCODE todo error propio sale con el mismo codigo, P0001. Con un codigo por
-- regla la aplicacion sabe CUAL fallo sin leer el texto: MA = mascotas, CI = citas
-- (convencion propia del proyecto, un SQLSTATE de cinco caracteres).
CREATE PROCEDURE sp_agendar_cita(
  p_id_mascota     INT,
  p_id_veterinario INT,
  p_fecha_hora     TIMESTAMP
)
LANGUAGE plpgsql
AS $proc$
DECLARE
  v_activa CHAR(1);
BEGIN
  SELECT activa INTO v_activa FROM mascota WHERE id_mascota = p_id_mascota;
  IF NOT FOUND THEN
    RAISE EXCEPTION 'ERROR: la mascota % no existe', p_id_mascota
      USING ERRCODE = 'MA002';
  END IF;

  IF v_activa <> 'S' THEN
    RAISE EXCEPTION 'ERROR: la mascota % esta inactiva; no se agenda cita', p_id_mascota
      USING ERRCODE = 'MA001';
  END IF;

  IF EXISTS (SELECT 1 FROM cita
              WHERE id_veterinario = p_id_veterinario
                AND fecha_hora     = p_fecha_hora
                AND estado <> 'CANCELADA') THEN
    RAISE EXCEPTION 'ERROR: el veterinario % ya tiene cita en %',
                    p_id_veterinario, p_fecha_hora
      USING ERRCODE = 'CI001';
  END IF;

  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
  VALUES (p_id_mascota, p_id_veterinario, p_fecha_hora, 'PROGRAMADA');
END;
$proc$;

-- El caso valido: se llama con parametros, nunca armando SQL con texto.
CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');   -- crea la cita 11

-- Lo que recibe la aplicacion cuando falla: el codigo (SQLSTATE) y el mensaje. Cada DO hace
-- de aplicacion: atrapa el error, lo muestra y deja seguir el script. La app real traduce el
-- codigo a un mensaje para recepcion y guarda el texto tecnico en su log.
DO $$
BEGIN
  CALL sp_agendar_cita(3, 2, TIMESTAMP '2026-09-21 08:00:00');    -- Rocky, inactiva
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'codigo % · %', SQLSTATE, SQLERRM;                 -- codigo MA001
END $$;

DO $$
BEGIN
  CALL sp_agendar_cita(99, 2, TIMESTAMP '2026-09-22 08:00:00');   -- no existe
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'codigo % · %', SQLSTATE, SQLERRM;                 -- codigo MA002
END $$;

DO $$
BEGIN
  CALL sp_agendar_cita(2, 1, TIMESTAMP '2026-09-01 08:00:00');    -- franja de la cita 1
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'codigo % · %', SQLSTATE, SQLERRM;                 -- codigo CI001
END $$;

-- La prueba de que los rechazos no dejaron nada: 11 citas (las 10 sembradas + la valida).
SELECT COUNT(*) AS citas_totales FROM cita;

-- =====================================================================
-- BLOQUE 2 · El rechazo de negocio DEVUELTO en la fila del contrato
-- =====================================================================
-- Una funcion de la capa de API no lanza el rechazo esperado: lo devuelve en
-- (ok, mensaje, id_generado). Lo inesperado se captura con WHEN OTHERS: el bloque deshace lo
-- que alcanzo a escribir y tambien se devuelve como ok = false. Nunca WHEN OTHERS THEN NULL.
CREATE FUNCTION api_cancelar_cita(p_id_cita INT)
RETURNS TABLE (ok BOOLEAN, mensaje TEXT, id_generado INT)
LANGUAGE plpgsql
AS $fn$
BEGIN
  UPDATE cita SET estado = 'CANCELADA'
   WHERE id_cita = p_id_cita AND estado = 'PROGRAMADA';
  IF NOT FOUND THEN                -- rechazo de negocio esperado: se devuelve
    RETURN QUERY SELECT FALSE, 'No se puede cancelar', NULL::INT;
    RETURN;                        -- RETURN QUERY no termina la funcion: falta este RETURN
  END IF;
  RETURN QUERY SELECT TRUE, 'Cita cancelada', p_id_cita;
EXCEPTION WHEN OTHERS THEN         -- lo inesperado: se deshace y se informa
  RETURN QUERY SELECT FALSE, SQLERRM, NULL::INT;
END;
$fn$;

SELECT * FROM api_cancelar_cita(1);    -- t | Cita cancelada       | 1
SELECT * FROM api_cancelar_cita(1);    -- f | No se puede cancelar | NULL (ya esta cancelada)
SELECT * FROM api_cancelar_cita(99);   -- f | No se puede cancelar | NULL (no existe)

-- La cancelacion libero la franja del veterinario 1 el 2026-09-01 a las 08:00: el mismo CALL
-- que en el BLOQUE 1 se rechazo con CI001 ahora entra.
CALL sp_agendar_cita(2, 1, TIMESTAMP '2026-09-01 08:00:00');   -- crea la cita 12
SELECT id_cita, id_mascota, estado
  FROM cita
 WHERE id_veterinario = 1 AND fecha_hora = TIMESTAMP '2026-09-01 08:00:00'
 ORDER BY id_cita;
-- 2 filas: la 1 CANCELADA y la 12 PROGRAMADA (el indice unico parcial lo permite).

-- =====================================================================
-- BLOQUE 3 · El contrato, como se documenta (las seis partes)
-- =====================================================================
-- sp_agendar_cita(p_id_mascota INT, p_id_veterinario INT, p_fecha_hora TIMESTAMP)
--   Llamada      : CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');
--   Precondicion : la mascota existe y tiene activa = 'S'; la franja del veterinario
--                  esta libre (una cita CANCELADA no la ocupa).
--   Efecto       : 1 fila nueva en cita, estado 'PROGRAMADA'. Si falla, NINGUNA.
--   Errores      : MA002 mascota inexistente · MA001 mascota inactiva · CI001 franja
--                  ocupada (y 23505 si dos sesiones chocan contra uq_cita_vet_franja).
--   Idempotente  : NO. Un doble clic intentaria dos citas; la segunda la rechaza la base.
--   Version      : 1.
-- api_cancelar_cita(p_id_cita INT) -> (ok BOOLEAN, mensaje TEXT, id_generado INT)
--   Efecto       : la cita pasa a 'CANCELADA' solo si estaba 'PROGRAMADA'.
--   Retorno      : ok = true con id_generado = el id de la cita; ok = false con el motivo e
--                  id_generado NULL (ni 0 ni -1).
--   Idempotente  : SI. Repetirla deja la base igual y responde ok = false.
--   Version      : 1.
