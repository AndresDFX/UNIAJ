# Taller de la Clase 2 en ExamLab - configuracion

- **Curso:** Bases de Datos II (FI303215)
- **Taller:** Taller Clase 2 en ExamLab - Administracion de BD y roles de VetCare
- **Preguntas:** 5 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** Plan de roles/privilegios de VetCare
- **Entregable de la clase:** Documento Roles_VetCare + script GRANT/REVOKE (o plan equivalente)

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante crea y verifica los 4 roles de VetCare con GRANT/REVOKE reales en PostgreSQL, aplica privilegio minimo con vistas y privilegios por columna, y documenta la matriz de permisos y la politica de usuarios.

---

## Pregunta 1 - SQL sobre PostgreSQL real · 30 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 1. Crear los roles de VetCare y otorgar privilegios

**Todo lo que necesitas esta aqui; si algo no te corre, preguntalo en clase antes de irte.**

El esquema de VetCare (`dueno`, `mascota`, `veterinario`, `cita`, `consulta`, `insumo`, `factura`, `detalle_factura`) ya esta creado y poblado.

En PostgreSQL un **rol** es la unidad de permisos (`CREATE ROLE`), y los permisos se dan y quitan con `GRANT` / `REVOKE`. Escribe el SQL que:

1. Cree **cuatro roles sin login**: `admin_bd`, `recepcion`, `veterinario_rol`, `auditor`.
   Usa `CREATE ROLE <nombre> NOLOGIN;` (el nombre del rol del veterinario lleva sufijo `_rol` para no chocar con la tabla `veterinario`).
2. Otorgue exactamente estos privilegios:
   - `recepcion`: `SELECT, INSERT, UPDATE` sobre `cita`; solo `SELECT` sobre `dueno`, `mascota` y `veterinario`. **Sin DELETE en ninguna tabla.**
   - `veterinario_rol`: `SELECT` sobre `cita` y `mascota`; `SELECT, INSERT, UPDATE` sobre `consulta`.
   - `auditor`: **solo** `SELECT` sobre `dueno`, `mascota`, `cita`, `consulta` y `factura`.
   - `admin_bd`: `ALL PRIVILEGES` sobre `cita`, `consulta`, `factura`, `detalle_factura` e `insumo`.
3. Ejecute un `REVOKE` **explicito y documentado** que quite `DELETE` sobre `cita` a `recepcion` (deja la sentencia aunque sea redundante: es la evidencia de la decision de diseno).
4. Termine con una consulta de **verificacion** sobre `information_schema.role_table_grants` que muestre `grantee`, `table_name` y `privilege_type` para los cuatro roles, ordenada por `grantee, table_name, privilege_type`.

**Nota tecnica importante:** ExamLab ejecuta PostgreSQL en el navegador con **una sola sesion de un unico usuario**. Por eso puedes crear roles y otorgar privilegios (es DDL real y verificable), pero **no** puedes conectarte simultaneamente como `recepcion` y comprobar en vivo que le rebotan las sentencias. Esa parte se analiza en la pregunta 5.

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

Los 4 roles se crean sin error y los GRANT reproducen exactamente la matriz pedida, sin privilegios de mas ni de menos (en particular auditor solo con SELECT y recepcion sin DELETE). Existe el REVOKE explicito de DELETE sobre cita a recepcion. La consulta final sobre information_schema.role_table_grants devuelve filas de los 4 roles y permite auditar la matriz. Sintaxis PostgreSQL, sin CREATE USER de Oracle ni GRANT de privilegios de sistema inventados.

---

## Pregunta 2 - Seleccion multiple · 10 pts

**Tipo en la plataforma:** `cerrada_multi`

**Enunciado (campo Contenido):**

## 2. Privilegio minimo en la matriz de VetCare

La recepcionista de Huellitas solo agenda, reprograma y cancela citas, y consulta datos de duenos y mascotas para identificarlos por telefono.

Selecciona **todas** las afirmaciones que respetan el principio de **privilegio minimo** (least privilege) para el rol `recepcion`.

**Opciones:**

- [ ] Darle DELETE sobre cita es aceptable porque cancelar una cita es basicamente borrarla.
- [x] Cancelar debe ser un UPDATE de estado a 'CANCELADA', no un DELETE: se conserva la historia y basta el privilegio UPDATE.
- [ ] Conviene darle ALL PRIVILEGES sobre cita para no tener que ajustar permisos cada vez que cambie el proceso.
- [x] Sobre dueno y mascota le basta SELECT; no necesita INSERT ni UPDATE porque el alta de mascotas la hace otro rol.
- [x] Si solo requiere telefono y nombre del dueno, es mejor exponerle una vista o privilegios por columna que la tabla dueno completa con email y direccion.
- [ ] El rol auditor deberia tener UPDATE sobre la tabla de auditoria para poder corregir registros erroneos.

**Rubrica esperada (campo Rubrica):**

10 puntos con las 3 opciones correctas y ninguna incorrecta; puntaje proporcional por acierto parcial. Correctas: indices 1, 3 y 4.

---

## Pregunta 3 - SQL sobre PostgreSQL real · 20 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 3. Reducir la superficie: vista de agenda y privilegios por columna

Sobre el mismo esquema de VetCare (ya creado y poblado) y **asumiendo que los roles `recepcion`, `veterinario_rol` y `auditor` ya existen** (los crea el setup de esta pregunta), implementa dos mecanismos de privilegio minimo:

1. **Vista para recepcion.** Crea `v_agenda_recepcion` que devuelva, para las citas **no canceladas**: `id_cita`, `fecha_hora`, `estado`, nombre de la mascota (`mascota`), nombre del dueno (`dueno`), telefono del dueno (`telefono`) y nombre del veterinario (`veterinario`). **No debe exponer el email del dueno.**
   Luego:
   - `GRANT SELECT` de la vista a `recepcion`.
   - `REVOKE SELECT ON dueno FROM recepcion;` para que llegue al dato del dueno **solo** a traves de la vista.

2. **Privilegios por columna para veterinario_rol.** En lugar de dar `SELECT` sobre toda la tabla `dueno`, otorga `SELECT` **unicamente** sobre las columnas `id_dueno` y `nombre` de `dueno`. La sintaxis es `GRANT SELECT (col1, col2) ON tabla TO rol;`

3. **Verificacion (obligatoria).** Termina con dos consultas:
   - un `SELECT` sobre la vista `v_agenda_recepcion` que muestre sus filas;
   - un `SELECT grantee, table_name, column_name, privilege_type FROM information_schema.column_privileges WHERE grantee = 'veterinario_rol' ORDER BY table_name, column_name;`

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

-- Roles ya definidos en la Clase 2 (pregunta 1)
CREATE ROLE recepcion NOLOGIN;
CREATE ROLE veterinario_rol NOLOGIN;
CREATE ROLE auditor NOLOGIN;

GRANT SELECT, INSERT, UPDATE ON cita TO recepcion;
GRANT SELECT ON dueno, mascota, veterinario TO recepcion;
GRANT SELECT ON cita, mascota TO veterinario_rol;
GRANT SELECT ON dueno, mascota, cita TO auditor;
```

**Rubrica esperada (campo Rubrica):**

La vista se crea con las 7 columnas pedidas, excluye el email y filtra las citas canceladas; el SELECT sobre la vista devuelve filas. Se otorga SELECT de la vista a recepcion y se revoca SELECT sobre dueno. Se usa GRANT SELECT (id_dueno, nombre) ON dueno TO veterinario_rol y la consulta a column_privileges evidencia solo esas dos columnas. Se descuenta si se expone el email o si se otorga la tabla completa en vez de columnas.

---

## Pregunta 4 - Respuesta escrita · 25 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## 4. Matriz rol x objeto x privilegio de VetCare

Entrega la **matriz de permisos completa** de VetCare DB (es el nucleo del documento `Roles_VetCare`). Usa una tabla markdown con una fila por objeto y una columna por rol, y en cada celda los privilegios (`S` = SELECT, `I` = INSERT, `U` = UPDATE, `D` = DELETE, `E` = EXECUTE, `-` = ninguno).

Objetos que debes cubrir (8 tablas + 2 objetos de codigo):
`dueno`, `mascota`, `veterinario`, `cita`, `consulta`, `insumo`, `factura`, `detalle_factura`, `sp_agendar_cita`, `sp_facturar`.

Roles: `admin_bd`, `recepcion`, `veterinario_rol`, `auditor`.

Debajo de la matriz, justifica en **4 a 6 lineas** tres decisiones concretas aplicando **privilegio minimo**, por ejemplo: por que ningun rol operativo tiene `DELETE`, por que `auditor` no tiene `INSERT` ni sobre la tabla de auditoria, y por que la app llegara a los datos por `EXECUTE` de procedimientos en vez de `INSERT` directo.

**Rubrica esperada (campo Rubrica):**

La matriz cubre los 10 objetos x 4 roles, sin celdas vacias, y es internamente consistente con los GRANT de la pregunta 1. Los procedimientos aparecen con EXECUTE, no con SELECT/INSERT. La justificacion argumenta explicitamente privilegio minimo en al menos 3 decisiones concretas (ausencia de DELETE, auditor de solo lectura, acceso por EXECUTE). Se descuenta por roles con ALL PRIVILEGES sin justificacion o por objetos omitidos.

---

## Pregunta 5 - Respuesta escrita · 15 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## 5. Politica de altas y bajas de usuarios (y limites del entorno)

Redacta la politica de gestion de usuarios de VetCare DB, maximo una pagina, con estas secciones:

1. **Alta**: quien solicita, quien aprueba, que rol se asigna por defecto, como se entrega la credencial inicial y en cuanto tiempo caduca.
2. **Cambio de rol**: que pasa cuando una recepcionista pasa a ser auxiliar veterinaria (que se otorga y, sobre todo, **que se revoca**).
3. **Baja**: pasos al desvincular a una persona el mismo dia (revocar roles, deshabilitar login, que hacer con los objetos que era dueno, cuanto se conserva la traza de auditoria).
4. **Revision periodica**: cada cuanto se audita la matriz, con que consulta de `information_schema` se saca la evidencia y quien firma.
5. **Limite del entorno de practica**: explica por que en ExamLab (PostgreSQL en el navegador, **una sola sesion y un solo usuario**) pudiste crear roles y verificar la matriz con `information_schema`, pero **no** pudiste conectarte como `recepcion` y ver el error de permiso. Indica que comando de PostgreSQL usarias en un servidor real para hacer esa prueba negativa (por ejemplo `SET ROLE recepcion;` seguido de un `DELETE FROM cita ...` que debe fallar con *permission denied*), y por que la ausencia de esa prueba es una brecha de verificacion en tu entregable.

**Rubrica esperada (campo Rubrica):**

Estan las 5 secciones con responsables y tiempos concretos, no genericos. La baja incluye revocar/deshabilitar y el destino de los objetos, y la revision periodica nombra la consulta de information_schema como evidencia. La seccion 5 reconoce correctamente la limitacion de una sola sesion en PGlite y propone SET ROLE (o conexion como otro usuario) como prueba negativa en un servidor real.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
