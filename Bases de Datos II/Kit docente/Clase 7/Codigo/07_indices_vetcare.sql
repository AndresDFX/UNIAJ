-- VetCare DB · Clase 7 · Indices y particionamiento
-- Ejecutable en PostgreSQL, incluido PGlite (la consola de ExamLab). Corre completo y
-- EN ORDEN: el valor de la clase esta en el antes/despues, no en el CREATE INDEX.
--
-- Los CINCO nombres de indice de aqui son los EXACTOS que califica la actividad. No los
-- cambie: el plan de ejecucion imprime "Index Scan using <nombre>" y la tabla de
-- justificacion de la pregunta 5 se llena con estos nombres.
--
-- ATENCION: el BLOQUE 0 recrea las tablas desde cero. Correlo en una base vacia o en la
-- consola de ExamLab, no sobre una VetCare DB con datos que quiera conservar. Si ya tiene
-- las 30.010 citas cargadas, salte al BLOQUE 1.

-- =====================================================================
-- BLOQUE 0 · Volumen. Con 50 filas el planeador prefiere Seq Scan por
-- muchos indices que existan: sin volumen esta clase no se puede medir.
-- Reproduce la siembra sintetica de la actividad: 30.000 citas del
-- 2026-01-05 al 2026-07-23, 5.000 mascotas, 2.000 duenos, 12 veterinarios.
-- (En ExamLab hay 10 citas mas puestas a mano en septiembre: 30.010.)
-- =====================================================================
DROP TABLE IF EXISTS cita_hist;
DROP TABLE IF EXISTS cita;
DROP TABLE IF EXISTS mascota;
DROP TABLE IF EXISTS veterinario;
DROP TABLE IF EXISTS dueno;

CREATE TABLE dueno (
  id_dueno SERIAL PRIMARY KEY,
  nombre   TEXT NOT NULL,
  ciudad   TEXT DEFAULT 'Cali'
);
CREATE TABLE veterinario (
  id_veterinario SERIAL PRIMARY KEY,
  nombre         TEXT NOT NULL,
  especialidad   TEXT
);
CREATE TABLE mascota (
  id_mascota SERIAL PRIMARY KEY,
  id_dueno   INT NOT NULL REFERENCES dueno(id_dueno),
  nombre     TEXT NOT NULL,
  especie    TEXT NOT NULL
);
CREATE TABLE cita (
  id_cita        SERIAL PRIMARY KEY,
  id_mascota     INT NOT NULL REFERENCES mascota(id_mascota),
  id_veterinario INT NOT NULL REFERENCES veterinario(id_veterinario),
  fecha_hora     TIMESTAMP NOT NULL,
  estado         TEXT NOT NULL DEFAULT 'PROGRAMADA'
    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))
);

INSERT INTO dueno (nombre) SELECT 'Dueno ' || g FROM generate_series(1, 2000) AS g;
INSERT INTO veterinario (nombre, especialidad)
SELECT 'Veterinario ' || g,
       CASE WHEN g % 3 = 0 THEN 'Cirugia'
            WHEN g % 3 = 1 THEN 'General'
            ELSE 'Dermatologia' END
FROM generate_series(1, 12) AS g;
INSERT INTO mascota (id_dueno, nombre, especie)
SELECT 1 + (g % 2000), 'Mascota ' || g,
       CASE WHEN g % 2 = 0 THEN 'Canino' ELSE 'Felino' END
FROM generate_series(1, 5000) AS g;
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
SELECT 1 + (g % 5000),
       1 + (g % 12),
       TIMESTAMP '2026-01-05 08:00:00'
         + ((g % 200) * INTERVAL '1 day')
         + ((g % 9) * INTERVAL '45 minutes'),
       CASE WHEN g % 11 = 0 THEN 'CANCELADA'
            WHEN g % 3  = 0 THEN 'ATENDIDA'
            ELSE 'PROGRAMADA' END
FROM generate_series(1, 30000) AS g;

ANALYZE dueno;  ANALYZE veterinario;  ANALYZE mascota;  ANALYZE cita;

-- Control: 30.000 | 18.182 PROGRAMADA | 9.091 ATENDIDA | 2.727 CANCELADA. En la base de
-- ExamLab hay 10 citas mas sembradas a mano, y ahi el reparto es 30.010 / 18.187 / 9.095 /
-- 2.728. Si su corrida da otros numeros, el resto del script no cuadra.
SELECT estado, COUNT(*) FROM cita GROUP BY estado ORDER BY estado;

-- =====================================================================
-- BLOQUE 1 · LINEA BASE. Sin este paso no hay clase: el "despues" solo
-- significa algo contra un "antes" medido. Tiene que salir Seq Scan.
-- =====================================================================
EXPLAIN ANALYZE   -- C1 · agenda del dia (rango de fecha + estado)
SELECT id_cita, fecha_hora, estado
  FROM cita
 WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
   AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
   AND estado = 'PROGRAMADA';
-- Esperado: Seq Scan on cita, filas devueltas = 91 (de 150 citas ese dia).

EXPLAIN ANALYZE   -- C2 · mascotas de un dueno
SELECT id_mascota, nombre, especie FROM mascota WHERE id_dueno = 1234;
-- Esperado: Seq Scan on mascota, 2 filas devueltas (id_dueno = 1 + (g % 2000) hace que solo
-- las mascotas g=1233 y g=3233 caigan en el dueno 1234). La FK NO crea indice sola en PostgreSQL.

-- =====================================================================
-- BLOQUE 2 · LOS TRES INDICES DE LA PREGUNTA 1
-- =====================================================================
-- (a) Simple: sirve a cualquier consulta por rango de fecha, con o sin estado.
CREATE INDEX idx_cita_fecha_hora ON cita (fecha_hora);

-- (b) Sobre la FK: "las mascotas de un dueno", y ademas abarata el borrado de un dueno.
CREATE INDEX idx_mascota_dueno ON mascota (id_dueno);

-- (c) PARCIAL: el WHERE es parte de la DEFINICION del indice, no de la consulta. Indexa
--     18.182 de las 30.000 de este script (18.187 de 30.010 en ExamLab) porque la pantalla
--     de agenda nunca pregunta por atendidas ni por canceladas.
CREATE INDEX idx_cita_programada_fecha ON cita (fecha_hora) WHERE estado = 'PROGRAMADA';

-- El paso que se salta la mitad del salon. Crear el indice NO actualiza estadisticas.
ANALYZE cita;
ANALYZE mascota;

-- Las MISMAS dos consultas, sin cambiar una coma.
EXPLAIN ANALYZE
SELECT id_cita, fecha_hora, estado
  FROM cita
 WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
   AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
   AND estado = 'PROGRAMADA';
-- Esperado: Index Scan using idx_cita_programada_fecha (gana el PARCIAL: recorre 91
-- entradas y ya sabe que todas cumplen el estado; el completo recorreria 150 y tendria
-- que descartar 59 despues de leer la tabla). Reporte el que VEA, no el que diga esto.

EXPLAIN ANALYZE
SELECT id_mascota, nombre, especie FROM mascota WHERE id_dueno = 1234;
-- Esperado: Index Scan (o Bitmap Index Scan) using idx_mascota_dueno.

-- Evidencia de que existen. indexdef devuelve el CREATE INDEX completo, asi que aqui se
-- ve tambien el WHERE del parcial.
SELECT indexname, tablename, indexdef
  FROM pg_indexes
 WHERE tablename IN ('cita','mascota')
 ORDER BY tablename, indexname;

-- =====================================================================
-- BLOQUE 3 · ORDEN DE COLUMNAS (pregunta 2). Los dos indices llevan las
-- MISMAS dos columnas en orden inverso, y existen para demostrar que el
-- orden decide. Regla: igualdad primero, rango al final.
-- =====================================================================
CREATE INDEX idx_cita_estado_fecha ON cita (estado, fecha_hora);
CREATE INDEX idx_cita_fecha_estado ON cita (fecha_hora, estado);
ANALYZE cita;

EXPLAIN ANALYZE   -- Q1 · estado (igualdad) + fecha (rango) -> favorece (estado, fecha_hora)
SELECT id_cita, fecha_hora FROM cita
 WHERE estado = 'PROGRAMADA'
   AND fecha_hora >= TIMESTAMP '2026-03-01' AND fecha_hora < TIMESTAMP '2026-04-01';

EXPLAIN ANALYZE   -- Q2 · solo rango de fecha -> favorece (fecha_hora, estado)
SELECT id_cita, estado FROM cita
 WHERE fecha_hora >= TIMESTAMP '2026-03-01' AND fecha_hora < TIMESTAMP '2026-04-01';

EXPLAIN ANALYZE   -- Q3 · solo estado, sin fecha -> columna lider ausente en el de fecha
SELECT COUNT(*) FROM cita WHERE estado = 'CANCELADA';

-- Fuerce el experimento: quite el que Q2 estaba usando y vuelva a medir.
DROP INDEX idx_cita_fecha_estado;
ANALYZE cita;
EXPLAIN ANALYZE
SELECT id_cita, estado FROM cita
 WHERE fecha_hora >= TIMESTAMP '2026-03-01' AND fecha_hora < TIMESTAMP '2026-04-01';
-- Esperado: cae en idx_cita_fecha_hora o vuelve a Seq Scan, pero NO usa
-- idx_cita_estado_fecha: su columna lider (estado) no aparece en el WHERE.

-- =====================================================================
-- BLOQUE 4 · PARTICIONAMIENTO (pregunta 3). HOY SE IMPLEMENTA.
-- =====================================================================
-- La trampa: en una tabla particionada la PK DEBE incluir la columna de particion.
-- PRIMARY KEY (id_cita) a secas no compila, y el mensaje del motor no lo dice asi.
CREATE TABLE cita_hist (
  id_cita        INT,
  id_mascota     INT,
  id_veterinario INT,
  fecha_hora     TIMESTAMP NOT NULL,
  estado         TEXT,
  PRIMARY KEY (id_cita, fecha_hora)
) PARTITION BY RANGE (fecha_hora);

-- Rango cerrado por abajo, abierto por arriba: el TO de una es el FROM de la siguiente.
CREATE TABLE cita_hist_2025 PARTITION OF cita_hist
  FOR VALUES FROM (TIMESTAMP '2025-01-01') TO (TIMESTAMP '2026-01-01');
CREATE TABLE cita_hist_2026 PARTITION OF cita_hist
  FOR VALUES FROM (TIMESTAMP '2026-01-01') TO (TIMESTAMP '2027-01-01');

INSERT INTO cita_hist
SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado FROM cita;

-- Prueba del enrutamiento. tableoid es la columna de sistema que dice en que tabla FISICA
-- vive cada fila; ::regclass la traduce a nombre. Sin esto no hay evidencia: solo un
-- INSERT que no dio error.
SELECT tableoid::regclass AS particion, COUNT(*), MIN(fecha_hora), MAX(fecha_hora)
  FROM cita_hist GROUP BY 1 ORDER BY 1;
-- Con la siembra del BLOQUE 0 (todas las citas son de 2026) cae TODO en cita_hist_2026 y
-- cita_hist_2025 queda vacia: eso ya demuestra el enrutamiento. La base de la pregunta 3
-- en ExamLab reparte 5.010 citas entre 2025 y 2026 y ahi se ven las dos particiones.

-- Poda de particiones: lo unico que mejora hoy de verdad.
EXPLAIN ANALYZE
SELECT COUNT(*) FROM cita_hist
 WHERE fecha_hora >= TIMESTAMP '2026-01-01' AND fecha_hora < TIMESTAMP '2027-01-01';
-- Esperado: en el plan aparece SOLO cita_hist_2026. El tiempo no baja de forma apreciable
-- con este volumen, y hay que decirlo: lo que se demuestra es que el motor descarta
-- particiones enteras ANTES de leer.

-- El beneficio real es de mantenimiento: archivar un ano es DROP TABLE de su particion
-- --una operacion de metadatos-- en vez de un DELETE masivo que toca millones de filas,
-- infla el registro de transacciones y sostiene bloqueos largos. Eso es la Clase 8.
-- DROP TABLE cita_hist_2025;
