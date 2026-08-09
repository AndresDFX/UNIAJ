-- VetCare DB · Clase 12 · Contrato app<->BD (Oracle PL/SQL, ejecutable)
-- Regla: la app NUNCA hace INSERT directo a cita/consulta/factura; solo llama estos procs.

CREATE OR REPLACE PROCEDURE sp_agendar_cita (
  p_id_cita IN NUMBER, p_id_mascota IN NUMBER, p_fecha IN TIMESTAMP, p_msg OUT VARCHAR2
) AS
BEGIN
  INSERT INTO cita(id_cita, id_mascota, fecha_hora, estado) VALUES (p_id_cita, p_id_mascota, p_fecha, 'PROGRAMADA');
  p_msg := 'OK: cita agendada'; COMMIT;
EXCEPTION WHEN OTHERS THEN p_msg := 'ERROR: ' || SQLERRM; ROLLBACK;
END;
/

CREATE OR REPLACE PROCEDURE sp_registrar_consulta (
  p_id_consulta IN NUMBER, p_id_cita IN NUMBER, p_notas IN VARCHAR2, p_precio IN NUMBER, p_msg OUT VARCHAR2
) AS
BEGIN
  INSERT INTO consulta(id_consulta, id_cita, notas, precio) VALUES (p_id_consulta, p_id_cita, p_notas, p_precio);
  p_msg := 'OK: consulta registrada'; COMMIT;
EXCEPTION WHEN OTHERS THEN p_msg := 'ERROR: ' || SQLERRM; ROLLBACK;
END;
/

-- Contrato para la sustentacion (documentar tal cual en el informe):
-- sp_agendar_cita(id_cita, id_mascota, fecha)      -> p_msg: 'OK: ...' | 'ERROR: ...'
-- sp_registrar_consulta(id_consulta, id_cita, notas, precio) -> p_msg idem
-- sp_facturar(id_factura, id_consulta, lineas...)  -> ver Clase 8 (transaccion factura+stock)
