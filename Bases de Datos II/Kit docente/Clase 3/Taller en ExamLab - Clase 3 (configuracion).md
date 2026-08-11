# Taller de la Clase 3 en ExamLab - configuracion

- **Curso:** Bases de Datos II (FI303215)
- **Taller:** Taller Clase 3 en ExamLab - Procedimientos almacenados de VetCare en PL/pgSQL
- **Preguntas:** 5 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://examlab.lovable.app/) · modulo Talleres
- **Hito del PI:** >=1 procedimiento de negocio (agendar cita / registrar consulta)
- **Entregable de la clase:** Script proc + casos de prueba (captura o enlace Live SQL)

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante implementa y prueba sp_agendar_cita y sp_registrar_consulta en PL/pgSQL, con la validacion de negocio de mascota inactiva, y documenta el contrato del procedimiento para la futura aplicacion.

---

## Pregunta 1 - SQL sobre PostgreSQL real · 35 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 1. Implementar sp_agendar_cita en PL/pgSQL

El esquema `dueno`, `mascota`, `veterinario`, `cita` ya esta creado y poblado. Datos que te interesan:

- Mascotas: 1 Firulais (activa), 2 Luna (activa), 3 **Rocky (INACTIVA)**, 4 Mishi, 5 Bobby, 6 Nube, 7 Toby, 8 **Kiara (INACTIVA)**.
- Veterinarios: 1 Laura Restrepo, 2 Diego Moreno, 3 Paula Salazar, 4 Ivan Ortiz.
- Ya existe una cita del veterinario 1 el `2026-09-01 08:00:00`.

**Crea el procedimiento** `sp_agendar_cita(p_id_mascota INT, p_id_veterinario INT, p_fecha_hora TIMESTAMP)` en **PL/pgSQL** que:

1. Verifique que la mascota exista; si no, `RAISE EXCEPTION 'ERROR: la mascota % no existe', p_id_mascota;`
2. Verifique la **regla de negocio del PI**: si `activa <> 'S'`, lance `RAISE EXCEPTION` indicando que la mascota esta inactiva y **no** inserte nada.
3. Verifique que el veterinario no tenga ya una cita **no cancelada** en esa misma `fecha_hora`; si la tiene, lance excepcion.
4. Si todo esta bien, inserte en `cita` con estado `'PROGRAMADA'`.

Despues de crear el procedimiento, **demuestra que funciona** ejecutando:

```sql
CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');
SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado
FROM cita ORDER BY id_cita DESC LIMIT 3;
```

**Sintaxis PostgreSQL:** `CREATE PROCEDURE nombre(...) LANGUAGE plpgsql AS $proc$ DECLARE ... BEGIN ... END; $proc$;`. No uses `IS`/`AS` de Oracle, ni `VARCHAR2`, ni `RAISE_APPLICATION_ERROR`, ni `/` al final. Para detectar "no existe" usa `IF NOT FOUND THEN` despues del `SELECT ... INTO`.

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
```

**Rubrica esperada (campo Rubrica):**

El procedimiento se crea sin error con LANGUAGE plpgsql y dollar-quoting, y recibe los 3 parametros con los tipos pedidos. Implementa las 3 validaciones (mascota inexistente, mascota inactiva, veterinario ocupado) con RAISE EXCEPTION y mensaje informativo, e inserta con estado PROGRAMADA solo en el caso valido. El CALL de ejemplo agrega exactamente una fila y el SELECT final la evidencia. Cero sintaxis Oracle.

---

## Pregunta 2 - SQL sobre PostgreSQL real · 25 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 2. Bateria de pruebas del procedimiento (caso OK + casos de error)

En esta base **el procedimiento `sp_agendar_cita(p_id_mascota, p_id_veterinario, p_fecha_hora)` ya esta creado** (version de referencia), junto con el esquema y los datos. Tambien existe la tabla:

```sql
resultado_prueba (id_prueba SERIAL, caso TEXT, esperado TEXT, obtenido TEXT, paso BOOLEAN)
```

Escribe **cuatro pruebas**, cada una dentro de su propio bloque `DO`, que capturen el resultado y lo registren en `resultado_prueba`. Plantilla:

```sql
DO $$
BEGIN
  CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-20 08:00:00');
  INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
  VALUES ('P1 mascota activa', 'OK: cita creada', 'OK: cita creada', TRUE);
EXCEPTION WHEN OTHERS THEN
  INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
  VALUES ('P1 mascota activa', 'OK: cita creada', SQLERRM, FALSE);
END $$;
```

Los cuatro casos son:

| Caso | Llamada | Resultado esperado |
|---|---|---|
| P1 | mascota 1 (Firulais, activa), vet 2, `2026-09-20 08:00:00` | se crea la cita |
| P2 | mascota **3** (Rocky, **inactiva**), vet 2, `2026-09-21 08:00:00` | excepcion: mascota inactiva |
| P3 | mascota **99** (no existe), vet 2, `2026-09-22 08:00:00` | excepcion: mascota no existe |
| P4 | mascota 2 (Luna), vet **1**, `2026-09-01 08:00:00` (franja ya ocupada) | excepcion: veterinario ocupado |

Termina con **dos consultas de cierre**:

1. `SELECT caso, esperado, obtenido, paso FROM resultado_prueba ORDER BY id_prueba;`
2. Un `SELECT COUNT(*)` sobre `cita` que demuestre que **solo se agrego una** cita (la de P1) y que las 3 pruebas negativas **no dejaron basura** en la tabla.

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

CREATE PROCEDURE sp_agendar_cita(
  p_id_mascota     INT,
  p_id_veterinario INT,
  p_fecha_hora     TIMESTAMP
)
LANGUAGE plpgsql
AS $proc$
DECLARE
  v_activa CHAR(1);
  v_ocupado INT;
BEGIN
  SELECT activa INTO v_activa FROM mascota WHERE id_mascota = p_id_mascota;
  IF NOT FOUND THEN
    RAISE EXCEPTION 'ERROR: la mascota % no existe', p_id_mascota;
  END IF;
  IF v_activa <> 'S' THEN
    RAISE EXCEPTION 'ERROR: la mascota % esta inactiva; no se agenda cita', p_id_mascota;
  END IF;
  SELECT COUNT(*) INTO v_ocupado
  FROM cita
  WHERE id_veterinario = p_id_veterinario
    AND fecha_hora = p_fecha_hora
    AND estado <> 'CANCELADA';
  IF v_ocupado > 0 THEN
    RAISE EXCEPTION 'ERROR: el veterinario % ya tiene cita en %', p_id_veterinario, p_fecha_hora;
  END IF;
  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
  VALUES (p_id_mascota, p_id_veterinario, p_fecha_hora, 'PROGRAMADA');
END;
$proc$;

CREATE TABLE resultado_prueba (
  id_prueba SERIAL PRIMARY KEY,
  caso TEXT NOT NULL,
  esperado TEXT,
  obtenido TEXT,
  paso BOOLEAN
);
```

**Rubrica esperada (campo Rubrica):**

Los 4 bloques DO corren sin abortar el script y registran una fila cada uno en resultado_prueba con el SQLERRM real en los casos negativos. Las 3 pruebas negativas quedan con paso = FALSE por excepcion capturada (o con la semantica claramente documentada) y P1 con exito. El conteo final demuestra que cita paso de 10 a 11 filas, evidenciando que las validaciones no insertaron nada. Se descuenta si el script se cae por no capturar la excepcion.

---

## Pregunta 3 - Seleccion unica · 10 pts

**Tipo en la plataforma:** `cerrada`

**Enunciado (campo Contenido):**

## 3. PROCEDURE o FUNCTION en PostgreSQL

En VetCare necesitas una rutina que **calcule y devuelva** el precio sugerido de una consulta segun la especie de la mascota, para usarla directamente dentro de un `SELECT` sobre la tabla `consulta`.

Cual es la opcion correcta en PostgreSQL?

**Opciones:**

- [ ] Un PROCEDURE, porque en PostgreSQL los procedimientos pueden invocarse dentro de la lista de columnas de un SELECT.
- [x] Un FUNCTION que devuelva NUMERIC, porque solo las funciones pueden usarse dentro de una consulta SELECT; los procedimientos se invocan con CALL como sentencia independiente.
- [ ] Un PROCEDURE con parametro OUT, porque en PostgreSQL es la unica forma de retornar un valor.
- [ ] Da exactamente lo mismo: en PostgreSQL PROCEDURE y FUNCTION son sinonimos y ambos se pueden llamar con SELECT o con CALL.
- [ ] Un FUNCTION, pero solo si se declara LANGUAGE sql; en plpgsql las funciones no pueden retornar valores.

**Rubrica esperada (campo Rubrica):**

10 puntos si marca la opcion 1 (indice 1). Cualquier otra respuesta, 0.

---

## Pregunta 4 - SQL sobre PostgreSQL real · 15 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 4. sp_registrar_consulta: el segundo procedimiento de negocio

El esquema completo (incluidas `consulta`, `insumo`, `factura`, `detalle_factura`) ya esta creado y poblado. Recuerda: ya hay consultas registradas para las citas **2, 5, 7 y 10**, y la tabla `consulta` tiene `id_cita` con restriccion `UNIQUE`.

**Crea el procedimiento** `sp_registrar_consulta(p_id_cita INT, p_diagnostico TEXT, p_precio NUMERIC)` en PL/pgSQL que:

1. Valide que la cita exista; si no, lance excepcion.
2. Valide que la cita **no** este en estado `'CANCELADA'`; una cita cancelada no puede generar consulta.
3. Valide que esa cita **no tenga ya** una consulta registrada (usa `EXISTS` sobre `consulta`), lanzando una excepcion con mensaje claro en vez de dejar que reviente la restriccion `UNIQUE`.
4. Valide que `p_precio > 0`.
5. Inserte la consulta y, en la **misma** operacion, actualice el estado de la cita a `'ATENDIDA'`.

Luego demuestra su comportamiento con tres llamadas, **la segunda y la tercera envueltas en un bloque `DO` con `EXCEPTION WHEN OTHERS THEN RAISE NOTICE '%', SQLERRM;`** para que el script no se detenga:

- `CALL sp_registrar_consulta(1, 'Vacunacion anual antirrabica', 45000);` (cita 1, PROGRAMADA -> debe funcionar)
- `CALL sp_registrar_consulta(4, 'Revision', 30000);` (cita 4 esta CANCELADA -> debe fallar)
- `CALL sp_registrar_consulta(2, 'Duplicada', 40000);` (cita 2 ya tiene consulta -> debe fallar)

Cierra con `SELECT c.id_cita, c.estado, co.diagnostico, co.precio FROM cita c LEFT JOIN consulta co ON co.id_cita = c.id_cita ORDER BY c.id_cita;`

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

CREATE TABLE consulta (
  id_consulta SERIAL PRIMARY KEY,
  id_cita INT NOT NULL UNIQUE REFERENCES cita(id_cita),
  diagnostico TEXT,
  precio NUMERIC(12,2) NOT NULL CHECK (precio >= 0)
);

CREATE TABLE insumo (
  id_insumo SERIAL PRIMARY KEY,
  nombre TEXT NOT NULL,
  stock INT NOT NULL CHECK (stock >= 0),
  precio_unit NUMERIC(12,2) NOT NULL
);

CREATE TABLE factura (
  id_factura SERIAL PRIMARY KEY,
  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),
  fecha TIMESTAMP NOT NULL DEFAULT now(),
  total NUMERIC(12,2) NOT NULL DEFAULT 0
);

CREATE TABLE detalle_factura (
  id_detalle SERIAL PRIMARY KEY,
  id_factura INT NOT NULL REFERENCES factura(id_factura) ON DELETE CASCADE,
  id_insumo INT NOT NULL REFERENCES insumo(id_insumo),
  cantidad INT NOT NULL CHECK (cantidad > 0),
  precio_unit NUMERIC(12,2) NOT NULL
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

-- Consultas (ids 1..4) sobre las citas ATENDIDAS 2, 5, 7 y 10
INSERT INTO consulta (id_cita, diagnostico, precio) VALUES
  (2,  'Vacunacion triple felina', 40000),
  (5,  'Control de peso',          38000),
  (7,  'Otitis externa',           55000),
  (10, 'Desparasitacion',          35000);

-- Insumos (ids 1..6). Ojo: 2 y 5 tienen stock bajo a proposito.
INSERT INTO insumo (nombre, stock, precio_unit) VALUES
  ('Vacuna antirrabica',       12, 22000),
  ('Vacuna triple felina',      3, 31000),
  ('Antiparasitario oral',     40,  9500),
  ('Suero fisiologico 500ml',  25,  7000),
  ('Gasa esteril',              8,  1200),
  ('Jeringa 5ml',              60,   900);

-- Facturas (ids 1..3) y sus detalles
INSERT INTO factura (id_consulta, fecha, total) VALUES
  (1, TIMESTAMP '2026-09-01 09:40:00', 71000),
  (2, TIMESTAMP '2026-09-02 11:35:00', 47000),
  (3, TIMESTAMP '2026-09-05 15:50:00', 60200);

INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit) VALUES
  (1, 2, 1, 31000),
  (1, 6, 1,   900),
  (1, 3, 1,  9500),
  (2, 3, 1,  9500),
  (2, 4, 1,  7000),
  (3, 1, 1, 22000),
  (3, 5, 4,  1200),
  (3, 6, 2,   900);
```

**Rubrica esperada (campo Rubrica):**

El procedimiento se crea y aplica las 4 validaciones con RAISE EXCEPTION y mensajes propios (en particular detecta la consulta duplicada con EXISTS antes de violar el UNIQUE). La llamada valida inserta la consulta y deja la cita 1 en ATENDIDA; las dos invalidas se capturan sin abortar el script y no modifican datos. El SELECT final evidencia el estado resultante.

---

## Pregunta 5 - Respuesta escrita · 15 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## 5. Contrato de los procedimientos para la futura aplicacion

Documenta el **contrato** de los dos procedimientos que construiste, tal como lo consumira la aplicacion de Huellitas. Para **cada** procedimiento (`sp_agendar_cita` y `sp_registrar_consulta`) entrega:

1. **Firma exacta**: nombre y lista de parametros con tipo PostgreSQL y orden.
2. **Como se invoca**: sentencia `CALL` de ejemplo con valores reales.
3. **Precondiciones**: que debe ser verdadero antes de llamarlo (mascota activa, cita no cancelada, ...).
4. **Postcondiciones**: que cambia en la base si la llamada tiene exito (que filas se insertan o actualizan).
5. **Tabla de errores**: cada excepcion que puede lanzar, con el **texto del mensaje** y **que debe hacer la aplicacion** al recibirlo (mostrar aviso al usuario, ofrecer otra franja, bloquear el boton, etc.).
6. **Una decision de diseno justificada** en 2 o 3 lineas: por que la validacion vive en la base de datos y no solo en la aplicacion.

Cierra con una frase que fije la regla del PI: la aplicacion **nunca** hara `INSERT` directo sobre `cita` ni `consulta`; solo llamara estos procedimientos.

**Rubrica esperada (campo Rubrica):**

Ambos procedimientos documentados con los 6 puntos. Las firmas coinciden exactamente con el codigo entregado en las preguntas 1 y 4 (nombres, orden y tipos). La tabla de errores lista todas las excepciones implementadas con el mensaje real y una accion concreta de la aplicacion para cada una. La justificacion menciona que la regla debe valer para cualquier cliente que toque la base.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
