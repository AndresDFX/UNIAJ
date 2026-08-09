-- VetCare DB · Clase 8 · Transaccion facturacion + stock (orientativo)

-- Pseudobloque / proc:
-- BEGIN
--   INSERT INTO factura ...
--   INSERT INTO detalle_factura ...
--   UPDATE insumo SET stock = stock - :cant WHERE id_insumo = :id;
--   IF stock < 0 THEN RAISE; END IF;
--   COMMIT;
-- EXCEPTION WHEN OTHERS THEN ROLLBACK; RAISE;
-- END;

-- Demo minima portable:
-- UPDATE insumo SET stock = stock - 1 WHERE id_insumo = 1 AND stock >= 1;
-- Si SQL%ROWCOUNT = 0 -> no habia stock -> ROLLBACK de la factura.
