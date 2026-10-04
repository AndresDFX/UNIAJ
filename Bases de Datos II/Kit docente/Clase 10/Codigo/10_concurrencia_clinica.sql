-- VetCare DB · Clase 10 · Demo ejecutable: doble reserva, su mitigacion y el doble descuento
-- Ejecutable en PostgreSQL, incluido PGlite (la consola de ExamLab). Corre completo y EN ORDEN:
-- primero el problema, despues la solucion. La ULTIMA sentencia falla A PROPOSITO: es la prueba
-- de que la base ya no acepta la doble reserva.
--
-- Limite declarado: PGlite tiene UNA sola sesion. No se pueden ver dos transacciones
-- esperandose; lo que si se demuestra es que sin la regla la base ACEPTA el dato invalido y que
-- con la regla lo RECHAZA siempre, sin importar el orden ni la velocidad. La espera de T2 se
-- documenta en una linea de tiempo T1/T2.
--
-- Usa tablas propias (cita_demo, insumo_demo) para no tocar la base del proyecto.

-- =====================================================================
-- BLOQUE 0 · Esquema minimo y datos (los DROP permiten correrlo dos veces)
-- =====================================================================
DROP TABLE IF EXISTS cita_demo;
DROP TABLE IF EXISTS insumo_demo;

CREATE TABLE cita_demo (
  id_cita        SERIAL PRIMARY KEY,
  id_mascota     INT NOT NULL,
  id_veterinario INT NOT NULL,
  fecha_hora     TIMESTAMP NOT NULL,
  estado         TEXT NOT NULL DEFAULT 'PROGRAMADA'
                 CHECK (estado IN ('PROGRAMADA', 'ATENDIDA', 'CANCELADA'))
);
INSERT INTO cita_demo (id_mascota, id_veterinario, fecha_hora, estado) VALUES
  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),
  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),
  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),
  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA');

CREATE TABLE insumo_demo (
  id_insumo INT PRIMARY KEY,
  nombre    TEXT NOT NULL,
  stock     INT NOT NULL CHECK (stock >= 0)
);
INSERT INTO insumo_demo VALUES (2, 'Vacuna triple felina', 3);

-- =====================================================================
-- BLOQUE 1 · El problema: sin regla, la base acepta la doble reserva
-- =====================================================================
-- T1 (recepcion A) y T2 (recepcion B) agendan al veterinario 2 a la misma hora.
INSERT INTO cita_demo (id_mascota, id_veterinario, fecha_hora, estado)
VALUES (4, 2, TIMESTAMP '2026-09-15 10:00:00', 'PROGRAMADA');      -- T1: INSERT 0 1
INSERT INTO cita_demo (id_mascota, id_veterinario, fecha_hora, estado)
VALUES (5, 2, TIMESTAMP '2026-09-15 10:00:00', 'PROGRAMADA');      -- T2: INSERT 0 1, sin error

-- Deteccion: franjas con mas de una cita vigente.
SELECT id_veterinario, fecha_hora, COUNT(*) AS citas_en_la_misma_franja
FROM cita_demo
WHERE estado <> 'CANCELADA'
GROUP BY id_veterinario, fecha_hora
HAVING COUNT(*) > 1;
-- Esperado: 1 fila -> 2 | 2026-09-15 10:00:00 | 2

-- =====================================================================
-- BLOQUE 2 · Limpiar ANTES de crear la regla
-- =====================================================================
-- Con el duplicado adentro, el indice no se puede crear:
--   ERROR:  could not create unique index "uq_cita_demo_vet_franja"
--   DETAIL:  Key (id_veterinario, fecha_hora)=(2, 2026-09-15 10:00:00) is duplicated.
-- Se borra la segunda reserva (la de mayor id).
DELETE FROM cita_demo WHERE id_cita = (SELECT MAX(id_cita) FROM cita_demo);

-- =====================================================================
-- BLOQUE 3 · La regla: indice unico PARCIAL (una cita CANCELADA libera su franja)
-- =====================================================================
CREATE UNIQUE INDEX uq_cita_demo_vet_franja
  ON cita_demo (id_veterinario, fecha_hora)
  WHERE estado <> 'CANCELADA';

-- La excepcion correcta: una CANCELADA en una franja ocupada SI entra (el indice no la mira).
INSERT INTO cita_demo (id_mascota, id_veterinario, fecha_hora, estado)
VALUES (6, 1, TIMESTAMP '2026-09-01 08:00:00', 'CANCELADA');       -- INSERT 0 1

-- El rechazo, capturado y traducido a lenguaje de negocio (asi lo haria un procedimiento):
DO $$
BEGIN
  INSERT INTO cita_demo (id_mascota, id_veterinario, fecha_hora, estado)
  VALUES (5, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA');
  RAISE NOTICE 'FALLO: se permitio la doble reserva';
EXCEPTION WHEN unique_violation THEN
  RAISE NOTICE 'Ese horario acaba de ser tomado, elija otro (%)', SQLSTATE;
END $$;
-- Esperado: NOTICE:  Ese horario acaba de ser tomado, elija otro (23505)

-- =====================================================================
-- BLOQUE 4 · El doble descuento de stock: la condicion dentro del UPDATE
-- =====================================================================
-- Dos ventas de 3 unidades sobre un stock de 3: solo una puede pasar.
UPDATE insumo_demo SET stock = stock - 3 WHERE id_insumo = 2 AND stock >= 3;   -- UPDATE 1
UPDATE insumo_demo SET stock = stock - 3 WHERE id_insumo = 2 AND stock >= 3;   -- UPDATE 0
SELECT id_insumo, nombre, stock FROM insumo_demo;
-- Esperado: 2 | Vacuna triple felina | 0   (nunca negativo)

-- FOR UPDATE corre sin error, pero aqui nunca espera: nadie mas tiene la fila.
SELECT stock FROM insumo_demo WHERE id_insumo = 2 FOR UPDATE;      -- 0

SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado
FROM cita_demo ORDER BY id_cita;
-- Esperado: 6 filas; las dos del veterinario 1 a las 08:00 son una PROGRAMADA y una CANCELADA.

-- =====================================================================
-- BLOQUE 5 · La prueba final: la doble reserva ya no entra (FALLA A PROPOSITO)
-- =====================================================================
INSERT INTO cita_demo (id_mascota, id_veterinario, fecha_hora, estado)
VALUES (5, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA');
-- Esperado (PostgreSQL, SQLSTATE 23505):
--   ERROR:  duplicate key value violates unique constraint "uq_cita_demo_vet_franja"
--   DETAIL:  Key (id_veterinario, fecha_hora)=(1, 2026-09-01 08:00:00) already exists.
