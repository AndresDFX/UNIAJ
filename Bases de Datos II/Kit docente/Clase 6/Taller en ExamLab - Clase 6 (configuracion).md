# Taller de la Clase 6 en ExamLab - configuracion

- **Curso:** Bases de Datos II (FI303215)
- **Taller:** Taller Clase 6 en ExamLab - Optimizacion de consultas de VetCare (antes / despues)
- **Preguntas:** 5 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** Primera pareja de consultas antes/despues del PI
- **Entregable de la clase:** 2 consultas (antes/despues) + justificacion (media pag.)

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante reescribe dos consultas reales del PI con antipatrones, mide la mejora con EXPLAIN ANALYZE sobre 30.000 citas y justifica cada cambio en el informe del proyecto.

---

## Pregunta 1 - SQL sobre PostgreSQL real · 30 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 1. Reescribir la consulta de agenda del dia

Esta base tiene **volumen real**: 2.006 duenos, 5.008 mascotas, 16 veterinarios y **30.010 citas** repartidas entre el 2026-01-05 y el 2026-07-23 (unas 150 citas por dia). Las estadisticas ya estan actualizadas con `ANALYZE` y **no hay ningun indice** mas alla de las llaves primarias.

La recepcion de Huellitas usa esta consulta para imprimir la agenda del dia. Es la version **ANTES**, tal como la escribio quien la programo:

```sql
SELECT *
FROM cita c, mascota m, dueno d, veterinario v
WHERE c.id_mascota = m.id_mascota
  AND m.id_dueno = d.id_dueno
  AND c.id_veterinario = v.id_veterinario
  AND to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10'
  AND UPPER(c.estado) = 'PROGRAMADA';
```

**Tu trabajo:**

1. Ejecuta la consulta ANTES tal como esta (para tener la linea base).
2. Escribe la version **DESPUES** que devuelva **la misma informacion util** pero corrigiendo, como minimo, estos **cuatro antipatrones**:
   - `SELECT *` -> proyecta solo `c.id_cita`, `c.fecha_hora`, `m.nombre AS mascota`, `d.nombre AS dueno`, `v.nombre AS veterinario`, `c.estado`;
   - joins implicitos con comas -> `JOIN ... ON` explicitos;
   - `to_char(c.fecha_hora, ...) = '2026-03-10'` -> **predicado de rango** sobre la columna (`>= TIMESTAMP '2026-03-10 00:00:00' AND < TIMESTAMP '2026-03-11 00:00:00'`), para que la columna quede *sargable*;
   - `UPPER(c.estado) = 'PROGRAMADA'` -> comparacion directa `c.estado = 'PROGRAMADA'` (el dominio ya esta normalizado por el `CHECK`).
   Ordena por `c.fecha_hora`.
3. Verifica con un `SELECT COUNT(*)` de cada version que **ambas devuelven el mismo numero de filas**. Si no coinciden, corrige la version DESPUES: optimizar no puede cambiar el resultado.

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

La version DESPUES corrige los 4 antipatrones exigidos (proyeccion, JOIN explicito, predicado de rango sargable y comparacion directa de estado) y ordena por fecha_hora. Los dos COUNT(*) coinciden, demostrando equivalencia de resultado. Se descuenta si queda SELECT *, si persiste una funcion sobre fecha_hora en el WHERE o si el conteo difiere del de la version ANTES.

---

## Pregunta 2 - SQL sobre PostgreSQL real · 20 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 2. Medir con EXPLAIN ANALYZE: la evidencia del antes/despues

Misma base con volumen (30.010 citas, sin indices adicionales, estadisticas actualizadas).

Genera la **evidencia cuantitativa** de la optimizacion. Escribe, en este orden:

1. `EXPLAIN (ANALYZE, BUFFERS) <consulta ANTES>` usando exactamente la consulta con antipatrones de la pregunta 1.
2. `EXPLAIN (ANALYZE, BUFFERS) <consulta DESPUES>` con tu version optimizada.
   *(Si tu entorno no soporta la opcion `BUFFERS`, usa `EXPLAIN ANALYZE` a secas y dilo en la pregunta 5.)*
3. Una tercera sentencia: `EXPLAIN ANALYZE` de la version DESPUES **anadiendo `LIMIT 50`**, que es lo que realmente necesita la pantalla de agenda.

Despues de los tres `EXPLAIN`, escribe **como comentarios SQL** (lineas que empiezan con `--`) una mini tabla con lo que leiste del plan, con estos campos por version:

```
-- VERSION | nodo mas costoso | filas estimadas vs reales | tiempo total (ms)
-- ANTES   | ...
-- DESPUES | ...
```

Y una linea final `-- CONCLUSION:` indicando el factor de mejora aproximado.

**Como leer el plan:** busca `Seq Scan` (recorrido completo de tabla), `Hash Join` / `Nested Loop`, el `cost=` estimado, `rows=` estimadas frente a `actual rows=`, y `Execution Time`.

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

Los tres EXPLAIN corren y corresponden a las consultas indicadas. La tabla en comentarios reporta nodo mas costoso, filas estimadas vs reales y tiempo de ejecucion para ANTES y DESPUES, con valores tomados del plan real y no inventados. La conclusion cuantifica la mejora. Se descuenta si solo se pega el plan sin interpretarlo o si falta la variante con LIMIT 50.

---

## Pregunta 3 - SQL sobre PostgreSQL real · 20 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 3. Matar la subconsulta correlacionada del reporte de duenos

Misma base con volumen (2.006 duenos, 5.008 mascotas, 30.010 citas).

Huellitas quiere el ranking de duenos por cantidad de citas. La version **ANTES** ejecuta una subconsulta **por cada fila** de `dueno` (2.006 veces):

```sql
SELECT d.id_dueno,
       d.nombre,
       (SELECT COUNT(*)
          FROM cita c
          JOIN mascota m ON m.id_mascota = c.id_mascota
         WHERE m.id_dueno = d.id_dueno) AS total_citas
FROM dueno d
ORDER BY total_citas DESC;
```

**Tu trabajo:**

1. Ejecuta la version ANTES y luego `EXPLAIN ANALYZE` de la misma para registrar la linea base.
2. Escribe la version **DESPUES** que obtenga el mismo resultado con **una sola pasada**: `dueno LEFT JOIN mascota LEFT JOIN cita` + `GROUP BY d.id_dueno, d.nombre` + `COUNT(c.id_cita)`.
   Debe conservar a los duenos con **cero** citas (por eso `LEFT JOIN` y `COUNT(c.id_cita)`, no `COUNT(*)`).
   Agrega `ORDER BY total_citas DESC, d.id_dueno` y `LIMIT 20`.
3. Ejecuta `EXPLAIN ANALYZE` de la version DESPUES.
4. Demuestra la equivalencia: una consulta que compare las dos versiones y devuelva **cero filas** si coinciden. Sugerencia: usa `EXCEPT` entre los dos conjuntos completos (`id_dueno, total_citas`), en ambos sentidos, sin `LIMIT`.

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

La version DESPUES elimina la subconsulta correlacionada usando LEFT JOIN + GROUP BY y conserva los duenos con cero citas (COUNT de la columna, no COUNT(*)). Se ejecutan los dos EXPLAIN ANALYZE y se aprecia la diferencia de plan. La prueba de equivalencia con EXCEPT en ambos sentidos devuelve cero filas. Se descuenta por usar INNER JOIN (pierde duenos sin citas) o por omitir la verificacion.

---

## Pregunta 4 - Seleccion multiple · 10 pts

**Tipo en la plataforma:** `cerrada_multi`

**Enunciado (campo Contenido):**

## 4. Antipatrones de consulta en VetCare

Selecciona **todas** las afirmaciones correctas sobre optimizacion de consultas en PostgreSQL, en el contexto de VetCare DB.

**Opciones:**

- [x] Envolver la columna en una funcion (to_char(fecha_hora,...) o EXTRACT) impide que el motor use un indice sobre esa columna: se pierde la sargabilidad.
- [x] SELECT * en un join de 4 tablas transporta columnas que nadie usa y encarece el ordenamiento y la red.
- [ ] Optimizar una consulta puede cambiar el numero de filas que devuelve, siempre que sea mas rapida.
- [x] Una subconsulta correlacionada en la lista de columnas se evalua una vez por fila del exterior; reescribirla como JOIN con GROUP BY suele bajar el costo un orden de magnitud.
- [ ] Cambiar la coma por JOIN ... ON por si solo hace la consulta mas rapida, porque el motor usa otro algoritmo.
- [x] EXPLAIN muestra el plan estimado y EXPLAIN ANALYZE lo ejecuta de verdad y reporta filas y tiempos reales; comparar estimado vs real revela estadisticas desactualizadas.

**Rubrica esperada (campo Rubrica):**

10 puntos con las 4 opciones correctas y ninguna incorrecta; puntaje proporcional por acierto parcial. Correctas: indices 0, 1, 3 y 5.

---

## Pregunta 5 - Respuesta escrita · 20 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## 5. Justificacion tecnica del antes/despues (media pagina)

Escribe la justificacion que ira al informe del PI, con esta estructura:

1. **Consulta elegida y para que sirve en Huellitas**: en una frase, que pantalla o reporte la usa y con que frecuencia.
2. **Tres cambios concretos** que hiciste en el par antes/despues. Para cada uno: que cambiaste, **por que** mejora (habla de sargabilidad, proyeccion, cardinalidad, numero de pasadas sobre la tabla) y **que evidencia** del `EXPLAIN ANALYZE` lo respalda (nodo que desaparecio, tiempo que bajo, filas que dejaron de leerse).
3. **Que NO cambio**: confirma que el resultado es equivalente y di como lo verificaste (`COUNT(*)` igual, `EXCEPT` vacio).
4. **Que sigue**: que indice propondrias en la Clase 7 para esta misma consulta y por que crees que ayudaria.
5. **Limites de la medicion**: reconoce que mediste sobre PostgreSQL en el navegador con 30.010 filas y sin concurrencia, y di que cambiaria en un servidor real con millones de citas y varios usuarios.

Recuerda guardar tus scripts como `06_opt_antes.sql` y `06_opt_despues.sql` en tu carpeta del PI.

**Rubrica esperada (campo Rubrica):**

Las 5 secciones estan presentes. Los tres cambios estan justificados con vocabulario tecnico correcto (sargabilidad, proyeccion, numero de pasadas) y cada uno se ancla a una evidencia concreta del plan de ejecucion. Se afirma y se demuestra la equivalencia del resultado. La seccion 5 reconoce honestamente los limites del entorno de medicion.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
