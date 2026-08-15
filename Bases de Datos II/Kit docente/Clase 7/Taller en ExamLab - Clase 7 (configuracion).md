# Taller de la Clase 7 en ExamLab - configuracion

- **Curso:** Bases de Datos II (FI303215)
- **Taller:** Taller Clase 7 en ExamLab - Indices y particionamiento de VetCare
- **Preguntas:** 5 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://examlab.lovable.app/) · modulo Talleres
- **Hito del PI:** >=2 indices justificados sobre tablas calientes del PI
- **Entregable de la clase:** Script CREATE INDEX + tabla justificacion consulta->indice

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante crea y valida con EXPLAIN al menos tres indices sobre las tablas calientes de VetCare, construye una tabla historica particionada por rango de fecha y justifica cada indice frente al riesgo de sobre-indexar.

---

## Pregunta 1 - SQL sobre PostgreSQL real · 30 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 1. Crear los indices de las tablas calientes y probar que se usan

Base con volumen: **30.010 citas** (2026-01-05 a 2026-07-23), 5.008 mascotas, 2.006 duenos, 16 veterinarios. Estadisticas actualizadas y **sin indices** salvo las PK.

Las dos consultas frecuentes del PI son:

- **C1 (agenda del dia):** citas `PROGRAMADA` de un dia concreto, filtrando `fecha_hora` por rango.
- **C2 (mascotas de un dueno):** todas las mascotas de un `id_dueno` dado.

**Escribe el SQL que:**

1. Muestre la linea base: `EXPLAIN ANALYZE` de C1 y de C2 **antes** de crear indices. Debes ver `Seq Scan`.
   - C1: `SELECT id_cita, fecha_hora, estado FROM cita WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00' AND fecha_hora < TIMESTAMP '2026-03-11 00:00:00' AND estado = 'PROGRAMADA';`
   - C2: `SELECT id_mascota, nombre, especie FROM mascota WHERE id_dueno = 1234;`
2. Cree **tres indices** con nombres exactos:
   - `idx_cita_fecha_hora` sobre `cita (fecha_hora)`
   - `idx_mascota_dueno` sobre `mascota (id_dueno)`
   - `idx_cita_programada_fecha`: indice **parcial** sobre `cita (fecha_hora)` `WHERE estado = 'PROGRAMADA'`
3. Ejecute `ANALYZE cita;` y `ANALYZE mascota;` para refrescar estadisticas.
4. Repita `EXPLAIN ANALYZE` de C1 y C2 y muestre que el plan cambio a `Index Scan` / `Bitmap Index Scan`.
5. Termine con una consulta que liste los indices creados: `SELECT indexname, tablename, indexdef FROM pg_indexes WHERE tablename IN ('cita','mascota') ORDER BY tablename, indexname;`

**Nota:** un indice parcial ocupa menos y solo sirve si la consulta incluye la misma condicion del `WHERE` del indice. Comprueba en el plan cual de los dos indices sobre `fecha_hora` eligio el planeador para C1.

**SQL de partida (`options.db.setupSql`)** - corre antes del SQL del
estudiante, sobre una base limpia. PostgreSQL, no Oracle:

```sql
CREATE TABLE dueno (
  id_dueno SERIAL PRIMARY KEY,
  nombre TEXT NOT NULL,
  telefono TEXT,
  email TEXT,
  ciudad TEXT DEFAULT 'Cali'
);

CREATE TABLE mascota (
  id_mascota SERIAL PRIMARY KEY,
  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),
  nombre TEXT NOT NULL,
  especie TEXT NOT NULL,
  fecha_nac DATE,
  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN ('S','N'))
);

CREATE TABLE veterinario (
  id_veterinario SERIAL PRIMARY KEY,
  nombre TEXT NOT NULL,
  especialidad TEXT,
  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN ('S','N'))
);

CREATE TABLE cita (
  id_cita SERIAL PRIMARY KEY,
  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),
  id_veterinario INT NOT NULL REFERENCES veterinario(id_veterinario),
  fecha_hora TIMESTAMP NOT NULL,
  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'
    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))
);

-- Duenos (ids 1..6 en este orden)
INSERT INTO dueno (nombre, telefono, email) VALUES
  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),
  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),
  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),
  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),
  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),
  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');

-- Veterinarios (ids 1..4)
INSERT INTO veterinario (nombre, especialidad) VALUES
  ('Laura Restrepo', 'General'),
  ('Diego Moreno',   'Cirugia'),
  ('Paula Salazar',  'Dermatologia'),
  ('Ivan Ortiz',     'General');

-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.
INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, activa) VALUES
  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),
  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),
  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),
  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),
  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),
  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),
  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),
  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');

-- Citas (ids 1..10)
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado) VALUES
  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),
  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),
  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),
  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),
  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),
  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),
  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),
  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),
  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),
  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');

-- Volumen sintetico para que el planeador tenga con que trabajar
INSERT INTO dueno (nombre, telefono, email)
SELECT 'Dueno ' || g, '300' || LPAD(g::text, 7, '0'), 'dueno' || g || '@mail.com'
FROM generate_series(1, 2000) AS g;

INSERT INTO veterinario (nombre, especialidad)
SELECT 'Veterinario ' || g,
       CASE WHEN g % 3 = 0 THEN 'Cirugia'
            WHEN g % 3 = 1 THEN 'General'
            ELSE 'Dermatologia' END
FROM generate_series(1, 12) AS g;

INSERT INTO mascota (id_dueno, nombre, especie, activa)
SELECT 1 + (g % 2000),
       'Mascota ' || g,
       CASE WHEN g % 2 = 0 THEN 'Canino' ELSE 'Felino' END,
       CASE WHEN g % 17 = 0 THEN 'N' ELSE 'S' END
FROM generate_series(1, 5000) AS g;

INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
SELECT 1 + (g % 5000),
       1 + (g % 12),
       TIMESTAMP '2026-01-05 08:00:00'
         + ((g % 200) * INTERVAL '1 day')
         + ((g % 9) * INTERVAL '45 minutes'),
       CASE WHEN g % 11 = 0 THEN 'CANCELADA'
            WHEN g % 3 = 0 THEN 'ATENDIDA'
            ELSE 'PROGRAMADA' END
FROM generate_series(1, 30000) AS g;

ANALYZE dueno;
ANALYZE mascota;
ANALYZE veterinario;
ANALYZE cita;
```

**Rubrica esperada (campo Rubrica):**

Se muestra la linea base con Seq Scan antes de indexar. Se crean los 3 indices con los nombres exactos, incluido el parcial con su clausula WHERE. Tras ANALYZE, los EXPLAIN posteriores evidencian Index Scan o Bitmap Index Scan en al menos C1 y C2. La consulta a pg_indexes lista los 3 indices. Se descuenta si falta el indice parcial, si no se re-ejecutan los EXPLAIN o si no se comenta cual indice eligio el planeador.

---

## Pregunta 2 - SQL sobre PostgreSQL real · 20 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 2. Orden de columnas en un indice compuesto

Misma base con volumen (30.010 citas, sin indices adicionales).

Vas a demostrar experimentalmente que **el orden de las columnas de un indice compuesto importa**.

1. Crea los dos indices compuestos:
   - `idx_cita_estado_fecha` sobre `cita (estado, fecha_hora)`
   - `idx_cita_fecha_estado` sobre `cita (fecha_hora, estado)`
   y ejecuta `ANALYZE cita;`
2. Ejecuta `EXPLAIN ANALYZE` de estas **tres** consultas y observa que indice elige el planeador en cada caso:
   - **Q1** (filtro por estado + rango de fecha):
     `SELECT id_cita, fecha_hora FROM cita WHERE estado = 'PROGRAMADA' AND fecha_hora >= TIMESTAMP '2026-03-10 00:00:00' AND fecha_hora < TIMESTAMP '2026-03-11 00:00:00';`
   - **Q2** (solo rango de fecha):
     `SELECT id_cita, fecha_hora FROM cita WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00' AND fecha_hora < TIMESTAMP '2026-03-11 00:00:00';`
   - **Q3** (solo estado, muy poco selectivo):
     `SELECT COUNT(*) FROM cita WHERE estado = 'PROGRAMADA';`
3. Fuerza el experimento: elimina `idx_cita_fecha_estado` con `DROP INDEX`, vuelve a ejecutar `EXPLAIN ANALYZE` de **Q2** y compara. Explica en comentarios `--` si `(estado, fecha_hora)` sirve o no para una consulta que **no** filtra por estado.
4. Cierra con `-- CONCLUSION:` en una o dos lineas: cual es la regla practica sobre el orden de columnas (columna de igualdad primero, columna de rango despues) y por que un indice cuya primera columna no aparece en el `WHERE` normalmente no se usa.

**SQL de partida (`options.db.setupSql`)** - corre antes del SQL del
estudiante, sobre una base limpia. PostgreSQL, no Oracle:

```sql
CREATE TABLE dueno (
  id_dueno SERIAL PRIMARY KEY,
  nombre TEXT NOT NULL,
  telefono TEXT,
  email TEXT,
  ciudad TEXT DEFAULT 'Cali'
);

CREATE TABLE mascota (
  id_mascota SERIAL PRIMARY KEY,
  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),
  nombre TEXT NOT NULL,
  especie TEXT NOT NULL,
  fecha_nac DATE,
  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN ('S','N'))
);

CREATE TABLE veterinario (
  id_veterinario SERIAL PRIMARY KEY,
  nombre TEXT NOT NULL,
  especialidad TEXT,
  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN ('S','N'))
);

CREATE TABLE cita (
  id_cita SERIAL PRIMARY KEY,
  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),
  id_veterinario INT NOT NULL REFERENCES veterinario(id_veterinario),
  fecha_hora TIMESTAMP NOT NULL,
  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'
    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))
);

-- Duenos (ids 1..6 en este orden)
INSERT INTO dueno (nombre, telefono, email) VALUES
  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),
  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),
  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),
  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),
  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),
  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');

-- Veterinarios (ids 1..4)
INSERT INTO veterinario (nombre, especialidad) VALUES
  ('Laura Restrepo', 'General'),
  ('Diego Moreno',   'Cirugia'),
  ('Paula Salazar',  'Dermatologia'),
  ('Ivan Ortiz',     'General');

-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.
INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, activa) VALUES
  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),
  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),
  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),
  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),
  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),
  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),
  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),
  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');

-- Citas (ids 1..10)
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado) VALUES
  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),
  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),
  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),
  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),
  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),
  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),
  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),
  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),
  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),
  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');

-- Volumen sintetico para que el planeador tenga con que trabajar
INSERT INTO dueno (nombre, telefono, email)
SELECT 'Dueno ' || g, '300' || LPAD(g::text, 7, '0'), 'dueno' || g || '@mail.com'
FROM generate_series(1, 2000) AS g;

INSERT INTO veterinario (nombre, especialidad)
SELECT 'Veterinario ' || g,
       CASE WHEN g % 3 = 0 THEN 'Cirugia'
            WHEN g % 3 = 1 THEN 'General'
            ELSE 'Dermatologia' END
FROM generate_series(1, 12) AS g;

INSERT INTO mascota (id_dueno, nombre, especie, activa)
SELECT 1 + (g % 2000),
       'Mascota ' || g,
       CASE WHEN g % 2 = 0 THEN 'Canino' ELSE 'Felino' END,
       CASE WHEN g % 17 = 0 THEN 'N' ELSE 'S' END
FROM generate_series(1, 5000) AS g;

INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
SELECT 1 + (g % 5000),
       1 + (g % 12),
       TIMESTAMP '2026-01-05 08:00:00'
         + ((g % 200) * INTERVAL '1 day')
         + ((g % 9) * INTERVAL '45 minutes'),
       CASE WHEN g % 11 = 0 THEN 'CANCELADA'
            WHEN g % 3 = 0 THEN 'ATENDIDA'
            ELSE 'PROGRAMADA' END
FROM generate_series(1, 30000) AS g;

ANALYZE dueno;
ANALYZE mascota;
ANALYZE veterinario;
ANALYZE cita;
```

**Rubrica esperada (campo Rubrica):**

Se crean los dos indices compuestos y se ejecutan los EXPLAIN de Q1, Q2 y Q3 identificando el indice elegido en cada uno. Se hace el DROP INDEX y se vuelve a medir Q2, comparando el resultado. La conclusion enuncia correctamente la regla de igualdad-antes-de-rango y explica por que un indice cuya columna lider no aparece en el filtro suele quedar sin usar (o solo servir para Index Only Scan de barrido completo).

---

## Pregunta 3 - SQL sobre PostgreSQL real · 20 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 3. Particionar el historico de citas por rango de fecha

Esta base tiene **5.010 citas repartidas entre enero de 2025 y diciembre de 2026** en la tabla `cita`. Huellitas quiere archivar la historia en una tabla particionada por ano para que las consultas de un ano no toquen los datos del otro.

Escribe el SQL que:

1. Cree la tabla **particionada** `cita_hist` con las columnas `id_cita INT`, `id_mascota INT`, `id_veterinario INT`, `fecha_hora TIMESTAMP NOT NULL`, `estado TEXT`, usando `PARTITION BY RANGE (fecha_hora)`.
   **Ojo:** en una tabla particionada la PK debe incluir la columna de particion, asi que declara `PRIMARY KEY (id_cita, fecha_hora)`.
2. Cree **dos particiones**:
   - `cita_hist_2025` para `FROM ('2025-01-01') TO ('2026-01-01')`
   - `cita_hist_2026` para `FROM ('2026-01-01') TO ('2027-01-01')`
   Sintaxis: `CREATE TABLE cita_hist_2025 PARTITION OF cita_hist FOR VALUES FROM (TIMESTAMP '2025-01-01') TO (TIMESTAMP '2026-01-01');`
3. Migre **todas** las citas: `INSERT INTO cita_hist SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado FROM cita;`
4. **Demuestre el enrutamiento**: `SELECT tableoid::regclass AS particion, COUNT(*), MIN(fecha_hora), MAX(fecha_hora) FROM cita_hist GROUP BY 1 ORDER BY 1;`
   Debes ver las filas repartidas entre las dos particiones, con rangos de fecha que no se solapan.
5. **Demuestre la poda de particiones** (*partition pruning*): `EXPLAIN ANALYZE SELECT COUNT(*) FROM cita_hist WHERE fecha_hora >= TIMESTAMP '2026-01-01' AND fecha_hora < TIMESTAMP '2027-01-01';` y verifica en el plan que **solo** aparece `cita_hist_2026`.
6. Cierra con un comentario `--` explicando que operacion de mantenimiento se vuelve trivial con esta estructura (pista: archivar o eliminar un ano completo con `DROP TABLE` de la particion en vez de un `DELETE` masivo).

**SQL de partida (`options.db.setupSql`)** - corre antes del SQL del
estudiante, sobre una base limpia. PostgreSQL, no Oracle:

```sql
CREATE TABLE dueno (
  id_dueno SERIAL PRIMARY KEY,
  nombre TEXT NOT NULL,
  telefono TEXT,
  email TEXT,
  ciudad TEXT DEFAULT 'Cali'
);

CREATE TABLE mascota (
  id_mascota SERIAL PRIMARY KEY,
  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),
  nombre TEXT NOT NULL,
  especie TEXT NOT NULL,
  fecha_nac DATE,
  activa CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN ('S','N'))
);

CREATE TABLE veterinario (
  id_veterinario SERIAL PRIMARY KEY,
  nombre TEXT NOT NULL,
  especialidad TEXT,
  activo CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN ('S','N'))
);

CREATE TABLE cita (
  id_cita SERIAL PRIMARY KEY,
  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),
  id_veterinario INT NOT NULL REFERENCES veterinario(id_veterinario),
  fecha_hora TIMESTAMP NOT NULL,
  estado TEXT NOT NULL DEFAULT 'PROGRAMADA'
    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))
);

-- Duenos (ids 1..6 en este orden)
INSERT INTO dueno (nombre, telefono, email) VALUES
  ('Ana Gomez',      '3001112233', 'ana.gomez@mail.com'),
  ('Carlos Ruiz',    '3014445566', 'carlos.ruiz@mail.com'),
  ('Marcela Diaz',   '3027778899', 'marcela.diaz@mail.com'),
  ('Jorge Pineda',   '3105551212', 'jorge.pineda@mail.com'),
  ('Luisa Cardona',  '3123334455', 'luisa.cardona@mail.com'),
  ('Andres Vallejo', '3159998877', 'andres.vallejo@mail.com');

-- Veterinarios (ids 1..4)
INSERT INTO veterinario (nombre, especialidad) VALUES
  ('Laura Restrepo', 'General'),
  ('Diego Moreno',   'Cirugia'),
  ('Paula Salazar',  'Dermatologia'),
  ('Ivan Ortiz',     'General');

-- Mascotas (ids 1..8). Rocky (3) y Kiara (8) estan INACTIVAS.
INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, activa) VALUES
  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),
  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),
  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),
  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),
  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),
  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),
  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),
  (6, 'Kiara',    'Canino', DATE '2013-03-03', 'N');

-- Citas (ids 1..10)
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado) VALUES
  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),
  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),
  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),
  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),
  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),
  (7, 4, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),
  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),
  (2, 3, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA'),
  (4, 4, TIMESTAMP '2026-09-10 08:00:00', 'PROGRAMADA'),
  (6, 1, TIMESTAMP '2026-09-10 09:00:00', 'ATENDIDA');

-- Volumen con historia repartida entre 2025 y 2026 (para particionar)
INSERT INTO dueno (nombre, telefono, email)
SELECT 'Dueno ' || g, '300' || LPAD(g::text, 7, '0'), 'dueno' || g || '@mail.com'
FROM generate_series(1, 800) AS g;

INSERT INTO veterinario (nombre, especialidad)
SELECT 'Veterinario ' || g, 'General'
FROM generate_series(1, 10) AS g;

INSERT INTO mascota (id_dueno, nombre, especie, activa)
SELECT 1 + (g % 800), 'Mascota ' || g,
       CASE WHEN g % 2 = 0 THEN 'Canino' ELSE 'Felino' END, 'S'
FROM generate_series(1, 2000) AS g;

INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
SELECT 1 + (g % 2000),
       1 + (g % 10),
       TIMESTAMP '2025-01-06 08:00:00'
         + ((g % 700) * INTERVAL '1 day')
         + ((g % 8) * INTERVAL '1 hour'),
       CASE WHEN g % 11 = 0 THEN 'CANCELADA'
            WHEN g % 3 = 0 THEN 'ATENDIDA'
            ELSE 'PROGRAMADA' END
FROM generate_series(1, 5000) AS g;

ANALYZE dueno;
ANALYZE mascota;
ANALYZE veterinario;
ANALYZE cita;
```

**Rubrica esperada (campo Rubrica):**

cita_hist se crea con PARTITION BY RANGE (fecha_hora) y PRIMARY KEY que incluye la columna de particion; las dos particiones cubren 2025 y 2026 sin solaparse. La migracion inserta las 5.010 filas y la consulta con tableoid::regclass evidencia el reparto. El EXPLAIN de la consulta de 2026 muestra poda (solo la particion 2026). El comentario final identifica correctamente el beneficio de mantenimiento (DROP de particion vs DELETE masivo).

---

## Pregunta 4 - Seleccion multiple · 10 pts

**Tipo en la plataforma:** `cerrada_multi`

**Enunciado (campo Contenido):**

## 4. Riesgos de sobre-indexar VetCare

Alguien propone crear un indice sobre **cada** columna de `cita`, `mascota` y `factura` "por si acaso". Selecciona **todas** las afirmaciones correctas.

**Opciones:**

- [x] Cada indice adicional encarece INSERT, UPDATE y DELETE, porque el motor debe mantenerlo sincronizado con la tabla.
- [ ] Un indice sobre una columna de baja cardinalidad como estado, con solo 3 valores posibles, es siempre la mejor inversion.
- [x] Los indices ocupan espacio en disco y en memoria cache, compitiendo con los datos que si se consultan.
- [x] Un indice parcial (WHERE estado = 'PROGRAMADA') puede dar el mismo beneficio que uno completo ocupando una fraccion del tamano, cuando las consultas siempre traen ese filtro.
- [ ] Como las FOREIGN KEY crean su indice automaticamente en PostgreSQL, indexar id_dueno en mascota es redundante.
- [x] Antes de crear un indice hay que tener la consulta concreta que lo va a usar y medir con EXPLAIN; indexar por intuicion produce indices muertos.

**Rubrica esperada (campo Rubrica):**

10 puntos con las 4 opciones correctas y ninguna incorrecta; puntaje proporcional por acierto parcial. Correctas: indices 0, 2, 3 y 5.

---

## Pregunta 5 - Respuesta escrita · 20 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## 5. Tabla de justificacion consulta -> indice

Entrega la tabla de justificacion del entregable de la clase. Una fila por indice (minimo **3**, los que creaste en las preguntas 1 y 2), con estas columnas:

| Indice | Tabla y columnas | Consulta del PI que lo usa | Cardinalidad estimada de la columna lider | Evidencia en EXPLAIN | Costo de mantenimiento | Veredicto |
|---|---|---|---|---|---|---|

Para cada indice explica:

- **Cardinalidad**: si la columna lider tiene muchos valores distintos (`fecha_hora`, `id_dueno`) o pocos (`estado`), y como eso afecta la utilidad del indice.
- **Evidencia**: el nodo concreto que viste en el plan (`Index Scan using idx_...`, `Bitmap Heap Scan`) y la caida de tiempo.
- **Costo**: sobre que operaciones de escritura de VetCare pesa (por ejemplo, cada cita agendada mantiene los indices de `cita`).
- **Veredicto**: se queda, se cambia por un indice parcial o compuesto, o se descarta.

Cierra con dos parrafos cortos:

1. **Regla de sobre-indexacion** que adoptas tu (por ejemplo: ningun indice sin consulta documentada y sin evidencia de `EXPLAIN`).
2. **Particionamiento: veredicto para VetCare.** Con el volumen real que espera Huellitas, tiene sentido particionar `cita`? Justifica con numeros aproximados (citas por dia x dias de operacion) y reconoce que en ExamLab lo demostraste sintacticamente con 5.010 filas, volumen en el que la ganancia de rendimiento **no** es apreciable: el beneficio comprobado fue la **poda de particiones** en el plan y la facilidad de archivado, no la velocidad.

**Rubrica esperada (campo Rubrica):**

La tabla cubre al menos 3 indices con las 7 columnas, y cada fila trae cardinalidad, evidencia real del plan, costo de escritura y veredicto. La regla de sobre-indexacion es operativa y verificable. El veredicto sobre particionamiento usa una estimacion de volumen propia y reconoce explicitamente que con 5.010 filas la ganancia de rendimiento no es medible, distinguiendo poda de particiones y archivado de la mejora de velocidad.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
