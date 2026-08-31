-- VetCare DB · Clase 8 · Transaccion de facturacion + descuento de stock
-- Ejecutable en PostgreSQL, incluido PGlite (la consola de ExamLab). Corre completo y
-- EN ORDEN: el bloque 3 solo tiene sentido si antes se tomo la foto del bloque 2.
--
-- ESTO ES PL/pgSQL, NO PL/SQL DE ORACLE. Aqui no existen NUMBER, SQL%ROWCOUNT ni
-- RAISE_APPLICATION_ERROR, y NO se escribe COMMIT ni ROLLBACK dentro del procedimiento:
-- el CALL de nivel superior ya es su propia transaccion.

-- =====================================================================
-- BLOQUE 0 · Esquema minimo y datos. Los stocks son los de la actividad.
-- =====================================================================
-- Los DROP van primero para que el script se pueda correr dos veces sin limpiar a mano.
DROP PROCEDURE IF EXISTS sp_facturar(INT, INT[], INT[]);
DROP FUNCTION  IF EXISTS fn_descontar_stock(INT, INT);
DROP TABLE     IF EXISTS detalle_factura;
DROP TABLE     IF EXISTS factura;
DROP TABLE     IF EXISTS insumo;

CREATE TABLE insumo (
  id_insumo   SERIAL PRIMARY KEY,
  nombre      TEXT NOT NULL,
  stock       INT NOT NULL CHECK (stock >= 0),
  precio_unit NUMERIC(12,2) NOT NULL
);
CREATE TABLE factura (
  id_factura  SERIAL PRIMARY KEY,
  id_consulta INT NOT NULL,
  total       NUMERIC(12,2) NOT NULL DEFAULT 0
);
CREATE TABLE detalle_factura (
  id_detalle  SERIAL PRIMARY KEY,
  id_factura  INT NOT NULL REFERENCES factura(id_factura),
  id_insumo   INT NOT NULL REFERENCES insumo(id_insumo),
  cantidad    INT NOT NULL CHECK (cantidad > 0),
  precio_unit NUMERIC(12,2) NOT NULL
);

INSERT INTO insumo (nombre, stock, precio_unit) VALUES
  ('Vacuna antirrabica',   12, 22000),   -- 1
  ('Vacuna triple felina',  3, 31000),   -- 2  <- el que se va a quedar corto
  ('Antiparasitario oral', 40,  9500),   -- 3
  ('Suero fisiologico',    25,  7000),   -- 4
  ('Gasa esteril',          8,  1200),   -- 5
  ('Jeringa 5ml',          60,   900);   -- 6

-- =====================================================================
-- BLOQUE 1 · EL PROCEDIMIENTO. Una factura tiene VARIAS lineas, asi que
-- la firma recibe dos arreglos paralelos, no un insumo suelto.
-- =====================================================================
CREATE PROCEDURE sp_facturar(
  p_id_consulta INT,
  p_insumos     INT[],
  p_cantidades  INT[]
)
LANGUAGE plpgsql
AS $proc$
DECLARE
  v_id_factura INT;
  v_total   NUMERIC(12,2) := 0;
  v_precio  NUMERIC(12,2);
  v_filas   INT;
  i         INT;
BEGIN
  -- El llamador se equivoco: se rechaza antes de tocar la base.
  IF array_length(p_insumos, 1) IS DISTINCT FROM array_length(p_cantidades, 1) THEN
    RAISE EXCEPTION 'ERROR: insumos y cantidades deben tener la misma longitud';
  END IF;

  -- Total en 0: todavia no se sabe. RETURNING ... INTO evita otro SELECT.
  INSERT INTO factura (id_consulta, total) VALUES (p_id_consulta, 0)
  RETURNING id_factura INTO v_id_factura;

  FOR i IN 1 .. array_length(p_insumos, 1) LOOP
    SELECT precio_unit INTO v_precio FROM insumo WHERE id_insumo = p_insumos[i];
    IF NOT FOUND THEN
      RAISE EXCEPTION 'ERROR: el insumo % no existe', p_insumos[i];
    END IF;

    -- EL GUARDIA. La comprobacion viaja DENTRO del WHERE: comprobar y escribir son
    -- una sola sentencia atomica y nadie puede colarse entre las dos.
    UPDATE insumo
       SET stock = stock - p_cantidades[i]
     WHERE id_insumo = p_insumos[i]
       AND stock >= p_cantidades[i];
    GET DIAGNOSTICS v_filas = ROW_COUNT;   -- 1 alcanzo, 0 no habia stock
    IF v_filas = 0 THEN
      RAISE EXCEPTION 'ERROR: stock insuficiente del insumo % (se pidieron %)',
        p_insumos[i], p_cantidades[i];
    END IF;

    INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit)
    VALUES (v_id_factura, p_insumos[i], p_cantidades[i], v_precio);

    v_total := v_total + (v_precio * p_cantidades[i]);
  END LOOP;

  UPDATE factura SET total = v_total WHERE id_factura = v_id_factura;
  RAISE NOTICE 'Factura % creada por %', v_id_factura, v_total;
END;
$proc$;

-- =====================================================================
-- BLOQUE 2 · CASO EXITOSO
-- =====================================================================
CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3]);
-- Esperado: 22000*1 + 900*2 + 1200*3 = 27.400, y los stocks 1, 6 y 5 bajan a 11, 58 y 5.
SELECT id_factura, id_consulta, total FROM factura ORDER BY id_factura;
SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;

-- =====================================================================
-- BLOQUE 3 · ATOMICIDAD. Aqui esta la clase entera.
-- =====================================================================
-- Foto inicial: estos numeros son el punto de comparacion.
SELECT (SELECT COUNT(*) FROM factura)         AS facturas,
       (SELECT COUNT(*) FROM detalle_factura) AS lineas,
       (SELECT stock FROM insumo WHERE id_insumo = 3) AS stock_3,
       (SELECT stock FROM insumo WHERE id_insumo = 2) AS stock_2;
-- Esperado tras el bloque 2: 1 | 3 | 40 | 3

-- Intento que falla A MITAD: la primera linea (2 del insumo 3, que tiene 40) SI alcanza;
-- la segunda (10 del insumo 2, que solo tiene 3) NO. El DO ... EXCEPTION es para que el
-- script no se detenga; el que decide sigue siendo el procedimiento.
DO $$
BEGIN
  CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 10]);
  RAISE NOTICE 'No deberia llegar aqui';
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'Fallo esperado: %', SQLERRM;
END $$;

-- Foto final: EXACTAMENTE la misma consulta.
SELECT (SELECT COUNT(*) FROM factura)         AS facturas,
       (SELECT COUNT(*) FROM detalle_factura) AS lineas,
       (SELECT stock FROM insumo WHERE id_insumo = 3) AS stock_3,
       (SELECT stock FROM insumo WHERE id_insumo = 2) AS stock_2;
-- Esperado: 1 | 3 | 40 | 3, identico a la foto inicial.
--   * no quedo una factura huerfana,
--   * no quedo ninguna linea de detalle,
--   * y sobre todo el stock del insumo 3 VOLVIO A 40: el descuento que si habia
--     alcanzado se deshizo. Nadie escribio ROLLBACK.

-- Y ahora la misma factura con una cantidad viable del insumo 2.
CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 3]);
SELECT id_factura, id_consulta, total FROM factura ORDER BY id_factura;
SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;
-- Esperado: factura 2 por 9500*2 + 31000*3 = 112.000; insumo 3 en 38 e insumo 2 en 0.

-- =====================================================================
-- BLOQUE 4 · EL MISMO PATRON COMO FUNCION REUTILIZABLE
-- Aqui "no hay stock" es una RESPUESTA, no un error: la funcion informa y
-- el llamador decide. El procedimiento del bloque 1 abortaba.
-- =====================================================================
CREATE FUNCTION fn_descontar_stock(p_id_insumo INT, p_cantidad INT)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $fn$
DECLARE
  v_filas INT;
BEGIN
  -- Una cantidad no positiva no es "no hay stock", es una llamada mal hecha.
  IF p_cantidad <= 0 THEN
    RAISE EXCEPTION 'ERROR: la cantidad debe ser positiva (llego %)', p_cantidad;
  END IF;

  UPDATE insumo
     SET stock = stock - p_cantidad
   WHERE id_insumo = p_id_insumo
     AND stock >= p_cantidad;
  GET DIAGNOSTICS v_filas = ROW_COUNT;

  RETURN v_filas = 1;
END;
$fn$;

-- Reiniciar los stocks para que la prueba de abajo de los valores esperados.
UPDATE insumo SET stock = 8 WHERE id_insumo = 5;
UPDATE insumo SET stock = 3 WHERE id_insumo = 2;

SELECT fn_descontar_stock(5, 3)  AS caso_ok,
       fn_descontar_stock(2, 10) AS caso_sin_stock,
       fn_descontar_stock(2, 3)  AS caso_limite;
-- Esperado: true | false | true. El tercero es el interesante: pide EXACTAMENTE el stock
-- que queda, y con >= en el guardia tiene que pasar.

SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;
-- Esperado: insumo 5 en 5, insumo 2 en 0, y NINGUN stock negativo.

-- La diferencia con leer primero y decidir despues:
--   SELECT stock ... ; IF stock >= cantidad THEN UPDATE ...
-- deja una VENTANA entre la lectura y la escritura. Con dos recepcionistas facturando el
-- mismo insumo, las dos leen 3, las dos deciden que alcanza, y el stock termina en -2 (o
-- el CHECK revienta). El UPDATE con la condicion en el WHERE no tiene ventana.
-- Aqui no se puede demostrar: PGlite corre UNA SOLA sesion. Ese es el gap que se declara
-- en la pregunta 5 y lo que abre la Clase 10.
