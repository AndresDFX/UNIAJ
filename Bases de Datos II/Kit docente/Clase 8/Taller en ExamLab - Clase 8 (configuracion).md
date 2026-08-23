# Taller de la Clase 8 en ExamLab - configuracion

- **Curso:** Bases de Datos II (FI303215)
- **Taller:** Taller Clase 8 en ExamLab - Transacciones de facturacion y tuning de VetCare
- **Preguntas:** 5 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** Transaccion de negocio (factura + stock) + notas de tuning
- **Entregable de la clase:** Script transaccional + checklist tuning del PI (1 pag.)

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante implementa la transaccion atomica de facturacion que descuenta stock, demuestra el rollback cuando el stock es insuficiente y entrega el checklist de tuning del PI.

---

## Pregunta 1 - SQL sobre PostgreSQL real · 35 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 1. sp_facturar: factura + detalle + descuento de stock, todo o nada

Esquema completo de VetCare creado y poblado. Datos que necesitas:

- Consultas registradas: `id_consulta` 1, 2, 3 y 4.
- Facturas ya existentes: 1, 2 y 3 (de las consultas 1, 2 y 3).
- Insumos: 1 Vacuna antirrabica **stock 12** ($22.000), 2 Vacuna triple felina **stock 3** ($31.000), 3 Antiparasitario oral **stock 40** ($9.500), 4 Suero fisiologico **stock 25** ($7.000), 5 Gasa esteril **stock 8** ($1.200), 6 Jeringa 5ml **stock 60** ($900).

**Crea el procedimiento** `sp_facturar(p_id_consulta INT, p_insumos INT[], p_cantidades INT[])` en PL/pgSQL que, de forma **atomica**:

1. Valide que los dos arreglos tengan la misma longitud; si no, `RAISE EXCEPTION`.
2. Inserte la cabecera en `factura (id_consulta, total)` con total `0` y recupere el id generado con `RETURNING id_factura INTO v_id_factura`.
3. Recorra las lineas con `FOR i IN 1 .. array_length(p_insumos, 1) LOOP`. Para **cada** linea:
   - obtenga `precio_unit` del insumo (si el insumo no existe, `RAISE EXCEPTION`);
   - descuente stock con el **patron de UPDATE condicional**:
     ```sql
     UPDATE insumo SET stock = stock - p_cantidades[i]
      WHERE id_insumo = p_insumos[i] AND stock >= p_cantidades[i];
     GET DIAGNOSTICS v_filas = ROW_COUNT;
     IF v_filas = 0 THEN RAISE EXCEPTION 'ERROR: stock insuficiente del insumo %', p_insumos[i]; END IF;
     ```
   - inserte la linea en `detalle_factura` con el `precio_unit` vigente;
   - acumule el total.
4. Al final, `UPDATE factura SET total = v_total WHERE id_factura = v_id_factura;`

Luego **ejecuta el caso exitoso**:

```sql
CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3]);
SELECT f.id_factura, f.id_consulta, f.total FROM factura f ORDER BY f.id_factura;
SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;
```

El total esperado es `22000*1 + 900*2 + 1200*3 = 27.400`, y los stocks de los insumos 1, 6 y 5 deben bajar a 11, 58 y 5.

**PostgreSQL:** no existe `SQL%ROWCOUNT`; se usa `GET DIAGNOSTICS v_filas = ROW_COUNT;`. Tampoco pongas `COMMIT` dentro del procedimiento: cada sentencia de nivel superior ya es su propia transaccion, y si el procedimiento lanza una excepcion **todo** lo que hizo se deshace.

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

El procedimiento se crea con la firma pedida y usa RETURNING ... INTO, el bucle sobre los arreglos, el UPDATE condicional con GET DIAGNOSTICS ROW_COUNT y RAISE EXCEPTION ante stock insuficiente. La llamada exitosa crea la factura 4 con total 27.400 y deja los stocks en 11, 58 y 5. No aparece COMMIT dentro del procedimiento ni SQL%ROWCOUNT. Los SELECT finales evidencian el resultado.

---

## Pregunta 2 - SQL sobre PostgreSQL real · 25 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 2. Probar la atomicidad: fallo a mitad de la factura

En esta base **`sp_facturar(p_id_consulta INT, p_insumos INT[], p_cantidades INT[])` ya esta creado** (version de referencia), junto al esquema y los datos. Estado inicial relevante: `factura` tiene 3 filas, `detalle_factura` tiene 8, y el insumo 2 (Vacuna triple felina) tiene **stock 3**.

Escribe el SQL que demuestre la atomicidad:

1. **Foto inicial**: una consulta que muestre en una sola fila `COUNT(*)` de `factura`, `COUNT(*)` de `detalle_factura` y el `stock` de los insumos 3 y 2. Guarda esos numeros; son tu punto de comparacion.
2. **Intento que debe fallar a mitad de camino**, capturando la excepcion para que el script no se detenga:
   ```sql
   DO $$
   BEGIN
     CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 10]);
     RAISE NOTICE 'No deberia llegar aqui';
   EXCEPTION WHEN OTHERS THEN
     RAISE NOTICE 'Fallo esperado: %', SQLERRM;
   END $$;
   ```
   La primera linea (2 unidades del insumo 3, que tiene 40) **si** alcanza; la segunda (10 unidades del insumo 2, que solo tiene 3) **no**.
3. **Foto final**: repite exactamente la consulta del punto 1.
4. Escribe como comentarios `--` la comparacion y la conclusion. Debe quedar demostrado que:
   - **no** quedo una factura huerfana en `factura`,
   - **no** quedo ninguna linea en `detalle_factura`,
   - y sobre todo que el **stock del insumo 3 volvio a 40**: el descuento que si habia alcanzado se deshizo.
5. Finalmente, **haz que la misma factura funcione** con una cantidad viable del insumo 2 (`CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 3]);`) y muestra el resultado, evidenciando el contraste entre la transaccion abortada y la exitosa.

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

CREATE PROCEDURE sp_facturar(
  p_id_consulta INT,
  p_insumos     INT[],
  p_cantidades  INT[]
)
LANGUAGE plpgsql
AS $proc$
DECLARE
  v_id_factura INT;
  v_total NUMERIC(12,2) := 0;
  v_precio NUMERIC(12,2);
  v_filas INT;
  i INT;
BEGIN
  IF array_length(p_insumos, 1) IS DISTINCT FROM array_length(p_cantidades, 1) THEN
    RAISE EXCEPTION 'ERROR: insumos y cantidades deben tener la misma longitud';
  END IF;

  INSERT INTO factura (id_consulta, total) VALUES (p_id_consulta, 0)
  RETURNING id_factura INTO v_id_factura;

  FOR i IN 1 .. array_length(p_insumos, 1) LOOP
    SELECT precio_unit INTO v_precio FROM insumo WHERE id_insumo = p_insumos[i];
    IF NOT FOUND THEN
      RAISE EXCEPTION 'ERROR: el insumo % no existe', p_insumos[i];
    END IF;

    UPDATE insumo
       SET stock = stock - p_cantidades[i]
     WHERE id_insumo = p_insumos[i]
       AND stock >= p_cantidades[i];
    GET DIAGNOSTICS v_filas = ROW_COUNT;
    IF v_filas = 0 THEN
      RAISE EXCEPTION 'ERROR: stock insuficiente del insumo % (se pidieron %)',
        p_insumos[i], p_cantidades[i];
    END IF;

    INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit)
    VALUES (v_id_factura, p_insumos[i], p_cantidades[i], v_precio);

    v_total := v_total + (v_precio * p_cantidades[i]);
  END LOOP;

  UPDATE factura SET total = v_total WHERE id_factura = v_id_factura;
  RAISE NOTICE 'Factura % creada por %', v_id_factura, v_total;
END;
$proc$;
```

**Rubrica esperada (campo Rubrica):**

Se toman foto inicial y final con la misma consulta y se comparan explicitamente. El intento invalido se captura sin abortar el script y se demuestra con datos que factura y detalle_factura no crecieron y que el stock del insumo 3 volvio a 40, es decir que la operacion parcial se deshizo. La segunda llamada viable se ejecuta y se muestra el contraste. Se descuenta si no se evidencia la reversion del stock del primer insumo.

---

## Pregunta 3 - SQL sobre PostgreSQL real · 15 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 3. El patron de descuento seguro como funcion reutilizable

Mismo esquema y datos (insumo 2 con stock 3, insumo 5 con stock 8).

Encapsula el patron de descuento en una funcion reutilizable:

1. Crea `fn_descontar_stock(p_id_insumo INT, p_cantidad INT)` que **retorne** `BOOLEAN` y:
   - valide `p_cantidad > 0` (si no, `RAISE EXCEPTION`);
   - ejecute el `UPDATE insumo SET stock = stock - p_cantidad WHERE id_insumo = p_id_insumo AND stock >= p_cantidad;`
   - obtenga las filas afectadas con `GET DIAGNOSTICS v_filas = ROW_COUNT;`
   - retorne `TRUE` si `v_filas = 1` y `FALSE` si `v_filas = 0` (**sin** lanzar excepcion: aqui el "no hay stock" es una respuesta, no un error).
2. Pruebala en una sola consulta que devuelva las tres respuestas en columnas:
   ```sql
   SELECT fn_descontar_stock(5, 3) AS caso_ok,
          fn_descontar_stock(2, 10) AS caso_sin_stock,
          fn_descontar_stock(2, 3)  AS caso_limite;
   ```
   Esperado: `true`, `false`, `true`.
3. Muestra `SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;` y confirma que **ningun** stock quedo negativo (insumo 5 en 5, insumo 2 en 0).
4. Explica en un comentario `--` la diferencia clave entre este patron y `SELECT stock ... ; IF stock >= cantidad THEN UPDATE ...`: por que leer primero y decidir despues es inseguro cuando hay varios usuarios facturando a la vez, y por que el `UPDATE` con la condicion en el `WHERE` resuelve la comprobacion y la escritura en **una sola** sentencia atomica.

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

La funcion retorna BOOLEAN, valida cantidad positiva, usa el UPDATE condicional con GET DIAGNOSTICS y devuelve FALSE en vez de excepcion cuando no hay stock. La consulta de prueba arroja true/false/true y el estado final deja el insumo 5 en 5 y el 2 en 0, sin negativos. El comentario explica correctamente por que el patron leer-luego-decidir es vulnerable y por que la condicion en el WHERE lo evita.

---

## Pregunta 4 - Seleccion unica · 10 pts

**Tipo en la plataforma:** `cerrada`

**Enunciado (campo Contenido):**

## 4. Que pasa con el bloque EXCEPTION en PL/pgSQL

En la pregunta 2 el `CALL sp_facturar(...)` fallo despues de haber insertado la cabecera de la factura y de haber descontado el stock del primer insumo, y sin embargo la base quedo exactamente como antes.

Cual es la explicacion correcta en PostgreSQL?

**Opciones:**

- [ ] Porque el procedimiento incluia un ROLLBACK explicito en su bloque EXCEPTION, igual que en Oracle.
- [ ] Porque PostgreSQL guarda automaticamente una copia de seguridad de cada tabla antes de cada CALL.
- [x] Porque la sentencia CALL de nivel superior es su propia transaccion: al propagarse la excepcion, todo el trabajo hecho dentro del procedimiento se deshace. Ademas, un bloque BEGIN ... EXCEPTION en PL/pgSQL crea un savepoint implicito, asi que al capturar el error se revierte solo lo hecho dentro de ese bloque.
- [ ] Porque los UPDATE sobre insumo no se aplican hasta que el procedimiento termina; PL/pgSQL los acumula en memoria y los escribe al final.
- [ ] Porque el trigger de stock deshizo los cambios anteriores al detectar la excepcion.

**Rubrica esperada (campo Rubrica):**

10 puntos si marca la opcion 2 (indice 2). Cualquier otra respuesta, 0.

---

## Pregunta 5 - Respuesta escrita · 15 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## 5. Checklist de tuning y transacciones del PI

Entrega la seccion "Transacciones y tuning" del informe del PI (una pagina), con:

1. **Inventario de transacciones de negocio de VetCare**: al menos **tres** operaciones que deben ser todo-o-nada (facturar y descontar stock, registrar consulta y cerrar cita, cancelar cita y liberar franja, ...). Para cada una: que tablas toca, cual es el paso que puede fallar y que debe pasar si falla.
2. **Checklist de tuning**, con estado (`listo` / `parcial` / `pendiente`) y evidencia para cada item:
   - [ ] indices creados sobre las columnas de filtro y join de las consultas frecuentes
   - [ ] consultas sin `SELECT *` en los reportes del PI
   - [ ] predicados sargables (sin funciones sobre columnas filtradas)
   - [ ] transacciones cortas: nada de esperar entrada del usuario con la transaccion abierta
   - [ ] validaciones criticas en la base (`CHECK`, trigger, procedimiento), no solo en la aplicacion
   - [ ] `ANALYZE` / estadisticas al dia despues de cargas masivas
   - [ ] plan de respaldo con restore probado (viene de la Clase 4)
3. **Decision documentada**: por que el descuento de stock se hace con `UPDATE ... WHERE stock >= cantidad` y no leyendo primero. Escribe la conclusion en una frase que puedas defender en la sustentacion.
4. **Gap honesto**: que no pudiste comprobar en ExamLab porque PostgreSQL en el navegador corre con **una sola sesion** (por ejemplo el comportamiento con dos recepcionistas facturando el mismo insumo al mismo tiempo) y como lo abordaras en la Clase 10.

**Rubrica esperada (campo Rubrica):**

El inventario trae al menos 3 transacciones con tablas, punto de fallo y comportamiento esperado ante el fallo. El checklist tiene los 7 items con estado y evidencia concreta (nombre de indice, archivo, consulta), no solo casillas marcadas. La decision sobre el UPDATE condicional esta bien argumentada y el gap de concurrencia se reconoce explicitamente con su plan de abordaje.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
