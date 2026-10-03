-- VetCare DB · Clase 10 · Demo ejecutable: doble reserva y su mitigacion
-- Ejecutar EN ORDEN: primero se ve el problema, despues la solucion.

-- Paso 1: tabla de demo SIN restriccion (asi llegaria si nadie penso en concurrencia)
CREATE TABLE cita_demo (
  id_cita INT PRIMARY KEY,
  id_mascota INT NOT NULL,
  id_veterinario INT NOT NULL,
  fecha_hora TIMESTAMP NOT NULL,
  estado VARCHAR(20) DEFAULT 'PROGRAMADA'
);

-- Paso 2: T1 (Recepcion A) agenda la franja - OK
INSERT INTO cita_demo VALUES (1, 10, 5, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');

-- Paso 3: T2 (Recepcion B) agenda OTRA mascota, MISMO veterinario, MISMA franja.
-- Sin restriccion esto se inserta SIN ERROR -> aqui esta la doble reserva.
INSERT INTO cita_demo VALUES (2, 22, 5, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');

-- Evidencia del problema: dos citas para el mismo veterinario en la misma franja
SELECT id_veterinario, fecha_hora, COUNT(*) AS citas_en_la_misma_franja
FROM cita_demo
GROUP BY id_veterinario, fecha_hora
HAVING COUNT(*) > 1;

-- Paso 4: la mitigacion real - la restriccion que debio existir desde el diseño
ALTER TABLE cita_demo
  ADD CONSTRAINT uq_cita_demo_vet_fecha UNIQUE (id_veterinario, fecha_hora);

-- Paso 5: repetir el intento de doble reserva - AHORA debe fallar
INSERT INTO cita_demo VALUES (3, 35, 5, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');
-- Esperado: error de restriccion unica (ORA-00001 en Oracle) -> la BD rechaza la doble reserva.
