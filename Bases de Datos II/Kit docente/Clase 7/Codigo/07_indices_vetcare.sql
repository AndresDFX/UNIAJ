-- VetCare DB · Clase 7 · Indices

CREATE INDEX idx_cita_fecha ON cita (fecha_hora);
CREATE INDEX idx_mascota_dueno ON mascota (id_dueno);
CREATE INDEX idx_cita_estado_fecha ON cita (estado, fecha_hora);

-- Justificacion PI:
-- idx_cita_fecha: listado del dia / agenda
-- idx_mascota_dueno: busqueda de mascotas por dueno
-- idx_cita_estado_fecha: filtros combinados recepción
