# Taller de la Clase 4 en ExamLab - configuracion

- **Curso:** Bases de Datos II (FI303215)
- **Taller:** Taller Clase 4 en ExamLab - Funciones, triggers y plan de respaldo de VetCare
- **Preguntas:** 5 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://examlab.lovable.app/) · modulo Talleres
- **Hito del PI:** >=1 funcion + >=1 trigger + borrador plan de respaldo
- **Entregable de la clase:** Scripts funcion/trigger + Plan_Backup_VetCare (1 pag.)

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante entrega una funcion de tarifas, un trigger de auditoria de cambios de estado de cita, un trigger que impide stock negativo y el plan de respaldo de VetCare DB.

---

## Pregunta 1 - SQL sobre PostgreSQL real · 20 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 1. Funcion de tarifas fn_precio_consulta

El esquema completo de VetCare esta creado y poblado (mascotas, citas y consultas de las citas 2, 5, 7 y 10).

**Crea la funcion** `fn_precio_consulta(p_especie TEXT, p_urgencia BOOLEAN)` que **retorne** `NUMERIC` con la tarifa base de Huellitas:

| Especie | Tarifa base |
|---|---|
| Canino | 45000 |
| Felino | 40000 |
| cualquier otra | 35000 |

Reglas adicionales:

- La comparacion de especie debe ser **insensible a mayusculas** (`'CANINO'`, `'canino'` y `'Canino'` valen igual). Usa `UPPER()` o `lower()`.
- Si `p_urgencia` es verdadero, la tarifa aumenta **35 %**.
- Si `p_urgencia` llega `NULL`, se trata como falso (usa `COALESCE`).
- Declara la funcion `LANGUAGE plpgsql` y marcala `IMMUTABLE` (solo depende de sus parametros).

Luego **usala en dos consultas**:

1. `SELECT nombre, especie, fn_precio_consulta(especie, FALSE) AS tarifa_normal, fn_precio_consulta(especie, TRUE) AS tarifa_urgencia FROM mascota ORDER BY id_mascota;`
2. Una consulta que, para cada consulta ya registrada, compare el `precio` cobrado contra `fn_precio_consulta(m.especie, FALSE)` y muestre una columna `diferencia`, uniendo `consulta -> cita -> mascota`.

**PostgreSQL:** `CREATE FUNCTION ... RETURNS NUMERIC LANGUAGE plpgsql IMMUTABLE AS $fn$ BEGIN ... RETURN ...; END; $fn$;`. No uses `RETURN NUMBER IS` de Oracle.

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

La funcion se crea con la firma pedida, RETURNS NUMERIC, LANGUAGE plpgsql e IMMUTABLE. Devuelve 45000/40000/35000 correctamente, es insensible a mayusculas, aplica el recargo del 35 % y trata NULL como falso. Las dos consultas corren y muestran valores coherentes con los datos (por ejemplo Firulais canino 45000 y 60750 en urgencia). Sintaxis PostgreSQL.

---

## Pregunta 2 - SQL sobre PostgreSQL real · 20 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 2. Trigger de auditoria de cambios de estado de cita

Regla de negocio del PI: **todo cambio sensible queda auditado**. Aqui la implementas para el estado de las citas.

El esquema y los datos estan creados (10 citas). Escribe el SQL que:

1. Cree la tabla `audit_cita` con: `id_audit` autonumerico PK, `id_cita` INT no nulo, `accion` TEXT no nulo, `valor_anterior` TEXT, `valor_nuevo` TEXT, `usuario_bd` TEXT con `DEFAULT current_user`, `fecha_evento` TIMESTAMP con `DEFAULT now()`.
2. Cree la **funcion de trigger** `fn_trg_audit_cita()` que `RETURNS TRIGGER` e inserte en `audit_cita` el `NEW.id_cita`, la accion `'CAMBIO_ESTADO'`, `OLD.estado` y `NEW.estado`.
3. Cree el trigger `trg_audit_cita` **AFTER UPDATE OF estado ON cita FOR EACH ROW**, con la clausula `WHEN (OLD.estado IS DISTINCT FROM NEW.estado)` para no auditar actualizaciones que no cambian nada.
4. **Prueba el trigger** con estas tres sentencias, en este orden:
   - `UPDATE cita SET estado = 'CANCELADA' WHERE id_cita = 1;`
   - `UPDATE cita SET estado = 'ATENDIDA' WHERE id_cita = 3;`
   - `UPDATE cita SET estado = 'PROGRAMADA' WHERE id_cita = 6;`  (la cita 6 **ya** esta PROGRAMADA)
5. Cierre con `SELECT id_audit, id_cita, accion, valor_anterior, valor_nuevo, usuario_bd FROM audit_cita ORDER BY id_audit;`

**Debe quedar demostrado que se registran 2 filas, no 3**: el tercer `UPDATE` no cambia el estado y la clausula `WHEN` lo filtra.

**PostgreSQL:** la funcion va aparte del trigger y el trigger se declara con `EXECUTE FUNCTION`, no con el bloque `BEGIN ... END` inline de Oracle. En un trigger `AFTER` puedes retornar `NULL`.

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

audit_cita se crea con las 7 columnas y los DEFAULT de current_user y now(). La funcion RETURNS TRIGGER inserta OLD.estado y NEW.estado, y el trigger es AFTER UPDATE OF estado FOR EACH ROW con la clausula WHEN (OLD.estado IS DISTINCT FROM NEW.estado). El SELECT final muestra exactamente 2 filas (citas 1 y 3) y el estudiante evidencia por que la tercera no se audito. Se descuenta por usar :NEW / :OLD de Oracle o por omitir EXECUTE FUNCTION.

---

## Pregunta 3 - SQL sobre PostgreSQL real · 20 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 3. Trigger que impide stock negativo

Regla de negocio del PI: **el stock de un insumo nunca queda negativo**.

En esta base la tabla `insumo` fue creada **a proposito sin** `CHECK (stock >= 0)`, para que puedas ver el problema y resolverlo con un trigger. Insumos disponibles:

| id | nombre | stock |
|---|---|---|
| 1 | Vacuna antirrabica | 12 |
| 2 | Vacuna triple felina | 3 |
| 3 | Antiparasitario oral | 40 |
| 4 | Suero fisiologico 500ml | 25 |
| 5 | Gasa esteril | 8 |
| 6 | Jeringa 5ml | 60 |

Escribe el SQL que:

1. **Evidencie el problema**: ejecuta `UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2;` y muestra con un `SELECT` que el stock quedo en **-7**. Luego devuelvelo a 3 con otro `UPDATE`.
2. Cree la funcion `fn_trg_stock_no_negativo()` que `RETURNS TRIGGER` y, si `NEW.stock < 0`, lance `RAISE EXCEPTION 'ERROR: el stock de % no puede quedar negativo (resultado: %)', OLD.nombre, NEW.stock;`. Si esta bien, `RETURN NEW`.
3. Cree el trigger `trg_stock_no_negativo` **BEFORE UPDATE OF stock ON insumo FOR EACH ROW**.
4. **Pruebe el trigger** con dos bloques `DO` que capturen la excepcion (`EXCEPTION WHEN OTHERS THEN RAISE NOTICE '%', SQLERRM;`):
   - intento invalido: descontar 10 unidades del insumo 2 (solo hay 3) -> debe fallar;
   - intento valido: descontar 2 unidades del insumo 2 -> debe pasar y dejar stock 1.
5. Cierre con `SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;` demostrando que ningun stock quedo negativo.

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

CREATE TABLE insumo (
  id_insumo SERIAL PRIMARY KEY,
  nombre TEXT NOT NULL,
  stock INT NOT NULL,
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

INSERT INTO insumo (nombre, stock, precio_unit) VALUES
  ('Vacuna antirrabica',       12, 22000),
  ('Vacuna triple felina',      3, 31000),
  ('Antiparasitario oral',     40,  9500),
  ('Suero fisiologico 500ml',  25,  7000),
  ('Gasa esteril',              8,  1200),
  ('Jeringa 5ml',              60,   900);
```

**Rubrica esperada (campo Rubrica):**

Se evidencia primero el stock negativo (-7) y se restaura el dato. La funcion RETURNS TRIGGER valida NEW.stock < 0 con RAISE EXCEPTION y retorna NEW en el caso valido; el trigger es BEFORE UPDATE OF stock FOR EACH ROW. Las dos pruebas quedan capturadas sin abortar el script y el estado final muestra el insumo 2 en stock 1 y ningun valor negativo. Se penaliza usar AFTER (no impide el cambio) o RAISE_APPLICATION_ERROR.

---

## Pregunta 4 - Seleccion multiple · 15 pts

**Tipo en la plataforma:** `cerrada_multi`

**Enunciado (campo Contenido):**

## 4. Donde vive cada validacion: CHECK, trigger o aplicacion

Con base en lo que acabas de implementar, selecciona **todas** las afirmaciones correctas sobre donde conviene poner cada validacion en VetCare DB.

**Opciones:**

- [x] Si la regla depende solo de columnas de la propia fila, como stock >= 0, un CHECK es preferible al trigger: es declarativo, mas barato y no se puede olvidar.
- [ ] Un trigger AFTER UPDATE puede impedir que un UPDATE deje datos invalidos, igual que un BEFORE UPDATE.
- [x] Registrar la historia de cambios de estado de una cita requiere trigger o codigo: ninguna restriccion declarativa guarda el valor anterior.
- [ ] Validar solo en la aplicacion es suficiente si quien desarrolla se compromete a no tocar la base con SQL directo.
- [x] Poner la validacion en la base protege tambien a cargas masivas, scripts de mantenimiento y a cualquier otra aplicacion que se conecte despues.
- [x] Abusar de triggers dificulta depurar: efectos ocultos, orden de ejecucion no evidente y costo por fila en operaciones masivas.

**Rubrica esperada (campo Rubrica):**

15 puntos con las 4 opciones correctas y ninguna incorrecta; puntaje proporcional por acierto parcial. Correctas: indices 0, 2, 4 y 5.

---

## Pregunta 5 - Respuesta escrita · 25 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## 5. Plan de respaldo de VetCare DB

Redacta `Plan_Backup_VetCare` (una pagina) para la clinica Huellitas, asumiendo PostgreSQL y una clinica que atiende de lunes a sabado, 7:00 a 19:00. Debe incluir:

1. **Que se respalda**: esquema (DDL), datos, procedimientos/funciones/triggers y scripts de migracion. Indica que herramienta usarias para cada cosa (por ejemplo `pg_dump` logico completo, `pg_dumpall` de roles, copia fisica).
2. **Frecuencia y ventana**: cuando corre cada respaldo y por que a esa hora (relaciona con el horario de atencion).
3. **Retencion**: cuantos dias/semanas/meses se guarda cada tipo, y donde (al menos dos ubicaciones distintas).
4. **RPO y RTO objetivo**: cuanta informacion aceptas perder como maximo y en cuanto tiempo debes estar operando de nuevo. Justificalo con el impacto para la clinica.
5. **Restore de prueba**: procedimiento concreto para verificar que el respaldo sirve, con **una consulta de validacion post-restauracion** (por ejemplo comparar `COUNT(*)` de `cita`, `consulta` y `factura` y el `MAX(fecha_hora)` contra los valores esperados). Indica cada cuanto se ensaya y quien firma la evidencia.
6. **Que NO cubre este plan** y un riesgo residual asumido.

Cierra actualizando el **checklist del PI**: marca como "en progreso" o "listo" los items de seguridad y respaldo y di que falta.

**Rubrica esperada (campo Rubrica):**

Las 6 secciones estan presentes con decisiones concretas y numeros (frecuencias, dias de retencion, RPO/RTO justificados), no formulas genericas. Se nombran herramientas reales de PostgreSQL, no de Oracle. La seccion 5 incluye al menos una consulta de validacion post-restore verificable y una periodicidad de ensayo. Se cierra con el estado del checklist del PI y el gap pendiente.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
