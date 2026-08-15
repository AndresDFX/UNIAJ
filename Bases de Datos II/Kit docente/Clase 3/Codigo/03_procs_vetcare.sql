-- VetCare DB · Clase 3 · Procedimiento agendar cita (Oracle Live SQL)
-- Ajustar tipos segun el schema creado por el estudiante.

CREATE OR REPLACE PROCEDURE sp_agendar_cita (
  p_id_cita IN NUMBER,
  p_id_mascota IN NUMBER,
  p_fecha IN TIMESTAMP,
  p_msg OUT VARCHAR2
) AS
  v_activa CHAR(1);
BEGIN
  SELECT activa INTO v_activa FROM mascota WHERE id_mascota = p_id_mascota;
  IF v_activa <> 'S' THEN
    p_msg := 'ERROR: mascota inactiva; no se agenda';
    RETURN;
  END IF;
  INSERT INTO cita(id_cita, id_mascota, fecha_hora, estado)
  VALUES (p_id_cita, p_id_mascota, p_fecha, 'PROGRAMADA');
  p_msg := 'OK: cita agendada';
  COMMIT;
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    p_msg := 'ERROR: mascota no existe';
  WHEN OTHERS THEN
    p_msg := 'ERROR: ' || SQLERRM;
    ROLLBACK;
END;
/
