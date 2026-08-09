-- VetCare DB · Clase 4 · Funcion + trigger auditoria (Oracle)

CREATE OR REPLACE FUNCTION fn_precio_base (p_especie VARCHAR2)
RETURN NUMBER IS
BEGIN
  IF UPPER(p_especie) = 'CANINO' THEN RETURN 45000; END IF;
  IF UPPER(p_especie) = 'FELINO' THEN RETURN 40000; END IF;
  RETURN 35000;
END;
/

CREATE TABLE audit_cita (
  id_audit NUMBER PRIMARY KEY,
  id_cita NUMBER,
  accion VARCHAR2(30),
  detalle VARCHAR2(200),
  fecha_evento TIMESTAMP DEFAULT SYSTIMESTAMP
);

CREATE OR REPLACE TRIGGER trg_audit_cancelacion
AFTER UPDATE OF estado ON cita
FOR EACH ROW
WHEN (NEW.estado = 'CANCELADA' AND OLD.estado <> 'CANCELADA')
BEGIN
  INSERT INTO audit_cita(id_audit, id_cita, accion, detalle)
  VALUES (NVL((SELECT MAX(id_audit) FROM audit_cita),0)+1,
          :NEW.id_cita, 'CANCELACION', 'Cita cancelada');
END;
/

-- Plan backup (documentar en Google Docs): diario logico scripts SQL + semanal export playground.
