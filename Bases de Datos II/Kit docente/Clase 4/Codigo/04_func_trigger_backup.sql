-- VetCare DB · Clase 4 · Funcion, triggers y respaldo · PostgreSQL
-- Script de la DEMO: corre tal cual en ExamLab (PostgreSQL/PGlite en el navegador).
--
-- En PostgreSQL el trigger son SIEMPRE dos objetos: una funcion que RETURNS TRIGGER
-- y un CREATE TRIGGER que dice cuando dispararla. No existe el trigger con el cuerpo
-- adentro que se escribe en Oracle, ni los dos puntos de :NEW y :OLD, ni
-- RAISE_APPLICATION_ERROR. Eso aqui no compila y la rubrica lo descuenta.

-- ============ 1) La funcion de precio ============
-- IMMUTABLE: para los mismos argumentos siempre devuelve lo mismo y no lee tablas.
-- COALESCE porque la app puede mandar NULL en la casilla de urgencia, y NULL * 1.35
-- es NULL: la factura saldria vacia en vez de salir mal, que es peor.
CREATE OR REPLACE FUNCTION fn_precio_consulta(
  p_especie  TEXT,
  p_urgencia BOOLEAN
)
RETURNS NUMERIC
LANGUAGE plpgsql
IMMUTABLE
AS $fn$
DECLARE
  v_base NUMERIC;
BEGIN
  v_base := CASE UPPER(p_especie)
              WHEN 'CANINO' THEN 45000
              WHEN 'FELINO' THEN 40000
              ELSE 35000
            END;
  IF COALESCE(p_urgencia, FALSE) THEN
    v_base := v_base * 1.35;
  END IF;
  RETURN v_base;
END;
$fn$;

-- Una funcion se llama con SELECT, no con CALL. Es la diferencia con la Clase 3.
SELECT fn_precio_consulta('Canino', FALSE) AS normal,     -- 45000
       fn_precio_consulta('Canino', TRUE)  AS urgencia,   -- 60750
       fn_precio_consulta('canino', TRUE)  AS minusculas, -- 60750, por UPPER()
       fn_precio_consulta('Conejo', FALSE) AS otra_especie, -- 35000
       fn_precio_consulta('Felino', NULL)  AS urgencia_nula; -- 40000, por COALESCE

-- Y donde se usa de verdad: junto a la tabla, como una columna calculada.
SELECT m.nombre, m.especie,
       fn_precio_consulta(m.especie, FALSE) AS precio_normal,
       fn_precio_consulta(m.especie, TRUE)  AS precio_urgencia
  FROM mascota m
 WHERE m.id_mascota IN (1, 4)
 ORDER BY m.id_mascota;

-- ============ 2) Trigger de auditoria: los DOS objetos ============
CREATE TABLE IF NOT EXISTS audit_cita (
  id_audit        SERIAL PRIMARY KEY,
  id_cita         INT  NOT NULL,
  accion          TEXT NOT NULL,
  valor_anterior  TEXT,
  valor_nuevo     TEXT,
  usuario_bd      TEXT      DEFAULT current_user,
  fecha_evento    TIMESTAMP DEFAULT now()
);

-- Objeto 1: la funcion. NEW y OLD sin dos puntos, y RETURN NEW obligatorio.
CREATE OR REPLACE FUNCTION fn_trg_audit_cita()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $fn$
BEGIN
  INSERT INTO audit_cita (id_cita, accion, valor_anterior, valor_nuevo)
  VALUES (NEW.id_cita, 'CAMBIO_ESTADO', OLD.estado, NEW.estado);
  RETURN NEW;   -- quien y cuando los pone los DEFAULT de la tabla
END;
$fn$;

-- Objeto 2: la asociacion. AFTER porque solo se registra lo que ya paso.
DROP TRIGGER IF EXISTS trg_audit_cita ON cita;
CREATE TRIGGER trg_audit_cita
AFTER UPDATE OF estado ON cita
FOR EACH ROW
WHEN (OLD.estado IS DISTINCT FROM NEW.estado)
EXECUTE FUNCTION fn_trg_audit_cita();

-- La prueba: TRES updates que dejan DOS filas de auditoria.
UPDATE cita SET estado = 'CANCELADA'  WHERE id_cita = 1;  -- cambia  -> audita
UPDATE cita SET estado = 'ATENDIDA'   WHERE id_cita = 3;  -- cambia  -> audita
UPDATE cita SET estado = 'PROGRAMADA' WHERE id_cita = 6;  -- ya era  -> NO audita

SELECT id_audit, id_cita, accion, valor_anterior, valor_nuevo, usuario_bd
  FROM audit_cita ORDER BY id_audit;   -- 2 filas: citas 1 y 3

-- El WHEN es lo que hace la diferencia. Sin el, la tercera fila tambien se escribe y
-- la auditoria se llena de eventos donde no cambio nada. Con IS DISTINCT FROM y no
-- con <> porque <> devuelve NULL si un lado es NULL, y un WHEN que da NULL no
-- dispara: un estado que pasa de NULL a 'PROGRAMADA' se quedaria sin auditar.

-- ============ 3) Trigger que IMPIDE: stock negativo ============
-- El CHECK de la tabla se retira a proposito para mostrar el hueco que tapa el
-- trigger. Un CHECK vigila el valor final de UNA fila; el trigger, ademas, puede
-- mirar el valor anterior y decidir con la fila completa.
ALTER TABLE insumo DROP CONSTRAINT IF EXISTS insumo_stock_check;

-- Sin defensa: el insumo 2 (Vacuna triple felina) tiene 3 unidades.
UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2;
SELECT id_insumo, nombre, stock FROM insumo WHERE id_insumo = 2;   -- stock = -7 (!)
UPDATE insumo SET stock = 3 WHERE id_insumo = 2;                   -- se restaura

CREATE OR REPLACE FUNCTION fn_trg_stock_no_negativo()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $fn$
BEGIN
  IF NEW.stock < 0 THEN
    RAISE EXCEPTION 'ERROR: el stock de % no puede quedar negativo (resultado: %)',
                    OLD.nombre, NEW.stock;
  END IF;
  RETURN NEW;   -- BEFORE: lo que se retorna es lo que se guarda
END;
$fn$;

-- BEFORE, no AFTER: la unica forma de impedir el cambio es correr antes de que se
-- escriba. Un AFTER que lanza excepcion tambien deshace la transaccion, pero para
-- cuando corre el motor ya hizo el trabajo -- y con AFTER no se puede corregir el
-- valor, solo abortar.
DROP TRIGGER IF EXISTS trg_stock_no_negativo ON insumo;
CREATE TRIGGER trg_stock_no_negativo
BEFORE UPDATE OF stock ON insumo
FOR EACH ROW
EXECUTE FUNCTION fn_trg_stock_no_negativo();

-- Con defensa: el mismo UPDATE, ahora rechazado. RAISE NOTICE imprime el mensaje sin
-- abortar el bloque, para que el grupo lea la excepcion en pantalla.
DO $$
BEGIN
  UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2;
  RAISE NOTICE 'FALLO LA PRUEBA: el UPDATE paso y no debia';
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'RECHAZADO (correcto): %', SQLERRM;
END $$;

-- Y el descuento legitimo sigue funcionando: no se bloqueo la operacion, se bloqueo
-- el resultado invalido.
DO $$
BEGIN
  UPDATE insumo SET stock = stock - 2 WHERE id_insumo = 2;
  RAISE NOTICE 'ACEPTADO (correcto): quedan 1 unidades';
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'FALLO LA PRUEBA: %', SQLERRM;
END $$;

SELECT id_insumo, nombre, stock FROM insumo WHERE id_insumo = 2;   -- stock = 1

-- ============ 4) El respaldo: las herramientas reales ============
-- Estos comandos NO corren dentro de ExamLab -- son de linea de comandos, no SQL --
-- pero son los que hay que nombrar en el plan. Se proyectan como referencia.
--
--   pg_dump -Fc -d vetcare -f vetcare_2026-09-15.dump   respaldo logico de LA base
--   pg_dumpall --globals-only -f roles.sql              roles y privilegios: pg_dump
--                                                       NO los incluye
--   pg_basebackup -D /backup/base -Ft -z                copia fisica del cluster
--   pg_restore -d vetcare_prueba vetcare_2026-09-15.dump   el ensayo de restauracion
--
-- La consulta de validacion despues de restaurar, que es lo que convierte «restaure»
-- en «restaure bien»:
--   SELECT (SELECT COUNT(*) FROM cita)     AS citas,
--          (SELECT COUNT(*) FROM consulta) AS consultas,
--          (SELECT COUNT(*) FROM factura)  AS facturas,
--          (SELECT MAX(fecha_hora) FROM cita) AS ultima_cita;
--
-- Y el esqueleto del plan (1 pagina, en Google Docs): 1) que se respalda y con que
-- herramienta cada cosa · 2) frecuencia y ventana, justificada contra el horario
-- lunes-sabado 7:00-19:00 · 3) retencion, en >=2 ubicaciones · 4) RPO y RTO con su
-- justificacion por impacto · 5) el ensayo de restauracion: cada cuanto, la consulta
-- de validacion y quien firma · 6) que NO cubre este plan y cual es el riesgo
-- residual que se asume.
