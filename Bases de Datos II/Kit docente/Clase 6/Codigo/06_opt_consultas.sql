-- VetCare DB · Clase 6 · Antes / despues

-- ANTES (anti-patron)
SELECT * FROM cita c, mascota m, dueno d
WHERE c.id_mascota = m.id_mascota AND m.id_dueno = d.id_dueno;

-- DESPUES (proyecto columnas + filtro temprano)
SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno
FROM cita c
JOIN mascota m ON m.id_mascota = c.id_mascota
JOIN dueno d ON d.id_dueno = m.id_dueno
WHERE c.fecha_hora >= TIMESTAMP '2026-09-01 00:00:00'
  AND c.fecha_hora <  TIMESTAMP '2026-09-02 00:00:00'
  AND c.estado = 'PROGRAMADA';
