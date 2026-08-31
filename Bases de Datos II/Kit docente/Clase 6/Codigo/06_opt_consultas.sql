-- VetCare DB · Clase 6 · Optimizacion de consultas (demo del docente)
-- ============================================================================
-- Motor: PostgreSQL. Se corre en ExamLab (PGlite en el navegador), que es donde
-- se califica el taller. Es AUTOCONTENIDO: crea el esquema, siembra el volumen y
-- deja las estadisticas listas, igual que el `setup_sql` de las preguntas 1, 2 y 3.
-- Volumen resultante: 2.006 duenos · 5.008 mascotas · 16 veterinarios · 30.010 citas.
-- SIN indices adicionales: crearlos es la Clase 7, y por eso hoy la evidencia NO es
-- un cambio de Seq Scan a Index Scan sino menos filas y menos pasadas.
-- ============================================================================

DROP TABLE IF EXISTS cita, mascota, veterinario, dueno;

CREATE TABLE dueno (
  id_dueno SERIAL PRIMARY KEY,
  nombre   TEXT NOT NULL,
  telefono TEXT,
  email    TEXT,
  ciudad   TEXT DEFAULT 'Cali'
);
CREATE TABLE mascota (
  id_mascota SERIAL PRIMARY KEY,
  id_dueno   INT NOT NULL REFERENCES dueno(id_dueno),
  nombre     TEXT NOT NULL,
  especie    TEXT NOT NULL,
  fecha_nac  DATE,
  activa     CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN ('S','N'))
);
CREATE TABLE veterinario (
  id_veterinario SERIAL PRIMARY KEY,
  nombre         TEXT NOT NULL,
  especialidad   TEXT,
  activo         CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN ('S','N'))
);
CREATE TABLE cita (
  id_cita        SERIAL PRIMARY KEY,
  id_mascota     INT NOT NULL REFERENCES mascota(id_mascota),
  id_veterinario INT NOT NULL REFERENCES veterinario(id_veterinario),
  fecha_hora     TIMESTAMP NOT NULL,
  estado         TEXT NOT NULL DEFAULT 'PROGRAMADA'
                 CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))
);

-- Los 6 duenos, 4 veterinarios, 8 mascotas y 10 citas con nombre propio de VetCare.
INSERT INTO dueno (nombre) VALUES
  ('Ana Gomez'), ('Carlos Ruiz'), ('Marcela Diaz'),
  ('Jorge Pineda'), ('Luisa Cardona'), ('Andres Vallejo');
INSERT INTO veterinario (nombre, especialidad) VALUES
  ('Laura Restrepo','General'), ('Diego Moreno','Cirugia'),
  ('Paula Salazar','Dermatologia'), ('Ivan Ortiz','General');
INSERT INTO mascota (id_dueno, nombre, especie, activa) VALUES
  (1,'Firulais','Canino','S'), (1,'Luna','Felino','S'), (2,'Rocky','Canino','N'),
  (3,'Mishi','Felino','S'),    (3,'Bobby','Canino','S'), (4,'Nube','Felino','S'),
  (5,'Toby','Canino','S'),     (6,'Kiara','Canino','N');
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado) VALUES
  (1,1,TIMESTAMP '2026-09-01 08:00','PROGRAMADA'), (2,1,TIMESTAMP '2026-09-01 09:00','ATENDIDA'),
  (4,2,TIMESTAMP '2026-09-01 10:00','PROGRAMADA'), (5,3,TIMESTAMP '2026-09-02 08:30','CANCELADA'),
  (6,2,TIMESTAMP '2026-09-02 11:00','ATENDIDA'),   (7,4,TIMESTAMP '2026-09-03 07:45','PROGRAMADA'),
  (1,1,TIMESTAMP '2026-09-05 15:00','ATENDIDA'),   (2,3,TIMESTAMP '2026-09-08 16:00','PROGRAMADA'),
  (4,4,TIMESTAMP '2026-09-10 08:00','PROGRAMADA'), (6,1,TIMESTAMP '2026-09-10 09:00','ATENDIDA');

-- Volumen. Sin esto la demo no se puede hacer: con 10 citas todo cabe en una
-- pagina de 8 KB y no hay plan mas barato que leerla, asi que la consulta pesima
-- y la optima miden lo mismo y la diferencia se esconde en el ruido de medicion.
INSERT INTO dueno (nombre, telefono, email)
SELECT 'Dueno '||g, '300'||LPAD(g::text,7,'0'), 'dueno'||g||'@mail.com'
FROM generate_series(1,2000) AS g;                       -- duenos 7..2006

INSERT INTO veterinario (nombre, especialidad)
SELECT 'Veterinario '||g,
       CASE WHEN g%3=0 THEN 'Cirugia' WHEN g%3=1 THEN 'General' ELSE 'Dermatologia' END
FROM generate_series(1,12) AS g;                         -- veterinarios 5..16

INSERT INTO mascota (id_dueno, nombre, especie, activa)
SELECT 1+(g%2000), 'Mascota '||g,
       CASE WHEN g%2=0 THEN 'Canino' ELSE 'Felino' END,
       CASE WHEN g%17=0 THEN 'N' ELSE 'S' END
FROM generate_series(1,5000) AS g;                       -- mascotas 9..5008

INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
SELECT 1+(g%5000), 1+(g%12),
       TIMESTAMP '2026-01-05 08:00' + ((g%200)*INTERVAL '1 day')
                                    + ((g%9)*INTERVAL '45 minutes'),
       CASE WHEN g%11=0 THEN 'CANCELADA' WHEN g%3=0 THEN 'ATENDIDA' ELSE 'PROGRAMADA' END
FROM generate_series(1,30000) AS g;                      -- citas 11..30010

-- Sin ANALYZE el optimizador trabaja con estimaciones por omision y el «estimado
-- contra real» de la pregunta 2 sale disparatado por una razon que no es el tema.
ANALYZE dueno; ANALYZE mascota; ANALYZE veterinario; ANALYZE cita;

-- Cifras de control que conviene proyectar antes de empezar (200 dias × 150 citas):
--   30.010 citas · 150 el 2026-03-10 · de esas 91 PROGRAMADA, 45 ATENDIDA, 14 CANCELADA.
SELECT COUNT(*) AS total_citas FROM cita;
SELECT estado, COUNT(*) FROM cita
WHERE fecha_hora >= TIMESTAMP '2026-03-10' AND fecha_hora < TIMESTAMP '2026-03-11'
GROUP BY estado ORDER BY estado;

-- ============================================================================
-- BLOQUE 1 · La agenda del dia: los 4 antipatrones (pregunta 1 del taller)
-- ============================================================================

-- ANTES. Cuatro defectos: SELECT * · joins con coma · to_char() sobre la columna
-- · UPPER() sobre el estado. Devuelve 91 filas.
SELECT *
FROM cita c, mascota m, dueno d, veterinario v
WHERE c.id_mascota = m.id_mascota
  AND m.id_dueno = d.id_dueno
  AND c.id_veterinario = v.id_veterinario
  AND to_char(c.fecha_hora,'YYYY-MM-DD') = '2026-03-10'
  AND UPPER(c.estado) = 'PROGRAMADA';

-- DESPUES. Proyeccion de 6 columnas · JOIN ... ON · predicado de RANGO (sargable)
-- · comparacion directa del estado, que el CHECK ya normalizo. Tambien 91 filas.
SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno,
       v.nombre AS veterinario, c.estado
FROM cita c
JOIN mascota m     ON m.id_mascota = c.id_mascota
JOIN dueno d       ON d.id_dueno = m.id_dueno
JOIN veterinario v ON v.id_veterinario = c.id_veterinario
WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
  AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
  AND c.estado = 'PROGRAMADA'
ORDER BY c.fecha_hora;

-- La evidencia (pregunta 2). Se lee: nodo mas costoso, rows= estimadas frente a
-- actual rows=, y Execution Time. Ojo: `actual time` es POR VUELTA y el tiempo de
-- un nodo INCLUYE el de sus hijos.
EXPLAIN (ANALYZE, BUFFERS)
SELECT *
FROM cita c, mascota m, dueno d, veterinario v
WHERE c.id_mascota = m.id_mascota
  AND m.id_dueno = d.id_dueno
  AND c.id_veterinario = v.id_veterinario
  AND to_char(c.fecha_hora,'YYYY-MM-DD') = '2026-03-10'
  AND UPPER(c.estado) = 'PROGRAMADA';

EXPLAIN (ANALYZE, BUFFERS)
SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno,
       v.nombre AS veterinario, c.estado
FROM cita c
JOIN mascota m     ON m.id_mascota = c.id_mascota
JOIN dueno d       ON d.id_dueno = m.id_dueno
JOIN veterinario v ON v.id_veterinario = c.id_veterinario
WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
  AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
  AND c.estado = 'PROGRAMADA'
ORDER BY c.fecha_hora;

-- Lo que la pantalla de agenda realmente necesita. El LIMIT deja de leer en
-- cuanto tiene 50 filas: por eso baja el tiempo aunque el plan sea el mismo.
EXPLAIN ANALYZE
SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno,
       v.nombre AS veterinario, c.estado
FROM cita c
JOIN mascota m     ON m.id_mascota = c.id_mascota
JOIN dueno d       ON d.id_dueno = m.id_dueno
JOIN veterinario v ON v.id_veterinario = c.id_veterinario
WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
  AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
  AND c.estado = 'PROGRAMADA'
ORDER BY c.fecha_hora
LIMIT 50;

-- ============================================================================
-- BLOQUE 2 · La subconsulta correlacionada (pregunta 3 del taller)
-- ============================================================================

-- ANTES. La subconsulta esta en la LISTA DE COLUMNAS y menciona d.id_dueno, del
-- exterior: no se puede calcular una vez y reusar. El plan lo delata con un nodo
-- SubPlan y loops=2006 — un dueno, una ejecucion.
EXPLAIN ANALYZE
SELECT d.id_dueno, d.nombre,
       (SELECT COUNT(*) FROM cita c JOIN mascota m ON m.id_mascota = c.id_mascota
         WHERE m.id_dueno = d.id_dueno) AS total_citas
FROM dueno d
ORDER BY total_citas DESC;

-- DESPUES. Una sola pasada: el SubPlan desaparece y queda un HashAggregate.
-- COUNT(c.id_cita) y NO COUNT(*): el LEFT JOIN fabrica una fila de NULL por cada
-- dueno sin citas, y COUNT(*) cuenta filas, asi que reportaria 1 donde va 0.
-- Y LEFT y no INNER: el INNER es mas rapido y borra del ranking a los 6 duenos
-- sin mascotas (2001..2006). Mas rapido devolviendo otra cosa no es optimizar.
EXPLAIN ANALYZE
SELECT d.id_dueno, d.nombre, COUNT(c.id_cita) AS total_citas
FROM dueno d
LEFT JOIN mascota m ON m.id_dueno = d.id_dueno
LEFT JOIN cita c    ON c.id_mascota = m.id_mascota
GROUP BY d.id_dueno, d.nombre
ORDER BY total_citas DESC, d.id_dueno
LIMIT 20;

-- ============================================================================
-- BLOQUE 3 · Optimizar no cambio el resultado: la prueba
-- ============================================================================

-- Prueba 1 · los dos COUNT(*) de la agenda, en la misma corrida. Las dos columnas
-- tienen que decir 91.
SELECT (SELECT COUNT(*) FROM cita c, mascota m, dueno d, veterinario v
         WHERE c.id_mascota = m.id_mascota AND m.id_dueno = d.id_dueno
           AND c.id_veterinario = v.id_veterinario
           AND to_char(c.fecha_hora,'YYYY-MM-DD') = '2026-03-10'
           AND UPPER(c.estado) = 'PROGRAMADA')                       AS filas_antes,
       (SELECT COUNT(*) FROM cita c
          JOIN mascota m ON m.id_mascota = c.id_mascota
          JOIN dueno d ON d.id_dueno = m.id_dueno
          JOIN veterinario v ON v.id_veterinario = c.id_veterinario
         WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
           AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
           AND c.estado = 'PROGRAMADA')                              AS filas_despues;

-- Prueba 2 · EXCEPT en los DOS sentidos, sin LIMIT. A EXCEPT B vacio NO prueba la
-- igualdad: B puede traer filas de mas. Tiene que devolver CERO filas.
WITH antes AS (
  SELECT d.id_dueno,
         (SELECT COUNT(*) FROM cita c JOIN mascota m ON m.id_mascota = c.id_mascota
           WHERE m.id_dueno = d.id_dueno) AS total_citas
  FROM dueno d
), despues AS (
  SELECT d.id_dueno, COUNT(c.id_cita) AS total_citas
  FROM dueno d
  LEFT JOIN mascota m ON m.id_dueno = d.id_dueno
  LEFT JOIN cita c    ON c.id_mascota = m.id_mascota
  GROUP BY d.id_dueno
)
SELECT 'sobra en ANTES' AS lado, * FROM (SELECT * FROM antes EXCEPT SELECT * FROM despues) a
UNION ALL
SELECT 'sobra en DESPUES', * FROM (SELECT * FROM despues EXCEPT SELECT * FROM antes) b;

-- El contraejemplo que vale la pena proyectar 30 segundos: con COUNT(*) en vez de
-- COUNT(c.id_cita), estas 6 filas dicen 1 y la respuesta correcta es 0.
SELECT d.id_dueno, COUNT(c.id_cita) AS bien, COUNT(*) AS mal
FROM dueno d
LEFT JOIN mascota m ON m.id_dueno = d.id_dueno
LEFT JOIN cita c    ON c.id_mascota = m.id_mascota
WHERE d.id_dueno BETWEEN 2001 AND 2006
GROUP BY d.id_dueno ORDER BY d.id_dueno;

-- Lo que NO se puede medir aqui, y hay que decirlo (es la seccion 5 de la
-- pregunta 5): tiempos con la memoria intermedia vacia —vaciarla exige
-- privilegios de administrador—, concurrencia (eso es la Clase 10) y cualquier
-- comparacion por encima de unos cientos de miles de filas.
