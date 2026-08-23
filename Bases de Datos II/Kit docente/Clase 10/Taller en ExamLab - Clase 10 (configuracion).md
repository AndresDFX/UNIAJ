# Taller de la Clase 10 en ExamLab - configuracion

- **Curso:** Bases de Datos II (FI303215)
- **Taller:** Taller Clase 10 en ExamLab - Control de concurrencia en VetCare (clase autonoma)
- **Preguntas:** 5 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** Escenarios de concurrencia del PI documentados
- **Entregable de la clase:** Informe corto: 2 escenarios (cita doble / stock) + mitigacion

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante documenta los dos escenarios de concurrencia del PI (doble reserva de franja y doble descuento de stock), implementa y prueba las mitigaciones que si son verificables en una sola sesion y explica el limite del entorno.

---

## Pregunta 1 - Respuesta escrita · 25 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## 1. Escenario de doble reserva con linea de tiempo T1/T2

**Clase autonoma: no hay docente en vivo, asi que sigue el guion al pie de la letra.**

En Huellitas hay **dos recepcionistas** atendiendo el telefono al mismo tiempo. Ambas quieren agendar una cita con la **veterinaria Laura Restrepo (id 1)** el **2026-10-12 a las 09:00**. Una llama por Firulais (mascota 1) y la otra por Luna (mascota 2).

El procedimiento `sp_agendar_cita` valida asi: primero hace `SELECT COUNT(*) FROM cita WHERE id_veterinario = 1 AND fecha_hora = '2026-10-12 09:00' AND estado <> 'CANCELADA'`, y si el conteo es 0, inserta.

**Redacta el escenario como una linea de tiempo**, con una tabla de al menos **6 pasos** y estas columnas:

| Momento | Transaccion T1 (Recepcion A) | Transaccion T2 (Recepcion B) | Estado de la tabla cita | Comentario |
|---|---|---|---|---|

Debe quedar explicito el momento exacto en que **las dos** transacciones leyeron `COUNT(*) = 0` antes de que cualquiera insertara, y por que ninguna de las dos validaciones detecto el conflicto.

Luego responde, en 3 a 5 lineas cada punto:

1. **Nombre de la anomalia**: como se llama este fenomeno en la teoria de concurrencia y por que el nivel de aislamiento `READ COMMITTED` (el predeterminado de PostgreSQL) **no** lo evita.
2. **Que pasaria** en el negocio si esto ocurre: impacto para la clinica, la veterinaria y los dos duenos.
3. **Tres mitigaciones posibles**, de la mas fuerte a la mas debil: (a) restriccion `UNIQUE` sobre `(id_veterinario, fecha_hora)`, (b) `SELECT ... FOR UPDATE` sobre la fila del veterinario o de la franja antes de validar, (c) `SET TRANSACTION ISOLATION LEVEL SERIALIZABLE` con reintento en la aplicacion. Para cada una: que garantiza, que cuesta y que debe hacer la aplicacion cuando la base rechace la operacion.

**Rubrica esperada (campo Rubrica):**

La linea de tiempo tiene al menos 6 pasos e identifica con precision el intervalo en que ambas transacciones leyeron COUNT(*) = 0 antes de insertar. Se nombra correctamente la anomalia (lectura fantasma / write skew sobre un predicado) y se explica por que READ COMMITTED no la evita. Las 3 mitigaciones se presentan con garantia, costo y accion de la aplicacion, ordenadas por fortaleza. Se descuenta si la narrativa no distingue el instante de la lectura del de la escritura.

---

## Pregunta 2 - SQL sobre PostgreSQL real · 25 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 2. Reproducir la doble reserva y cerrarla con una restriccion

**Limite del entorno que debes tener presente:** ExamLab ejecuta PostgreSQL **real** en el navegador, pero con **una sola sesion**. No puedes abrir dos conexiones y ver a T2 bloqueada esperando a T1. Lo que **si** puedes hacer, y es lo que se te pide, es demostrar que sin restriccion la base **acepta** el dato invalido, y que con la restriccion correcta lo **rechaza** siempre, sin importar el orden ni la velocidad de las transacciones. Esa es la mitigacion estructural.

La base trae `cita` **sin** ninguna restriccion de unicidad de franja, mas una tabla `evidencia (id_evidencia SERIAL, paso TEXT, resultado TEXT)`.

Escribe el SQL que, en este orden:

1. **Muestre el problema.** Inserta las dos citas del escenario de la pregunta 1:
   - `(id_mascota 1, id_veterinario 1, '2026-10-12 09:00:00', 'PROGRAMADA')`
   - `(id_mascota 2, id_veterinario 1, '2026-10-12 09:00:00', 'PROGRAMADA')`
   Ambas se insertan **sin error**. Registra en `evidencia` el paso `'sin restriccion'` con el resultado.
2. **Evidencie el dato invalido** con una consulta de deteccion:
   `SELECT id_veterinario, fecha_hora, COUNT(*) AS citas_en_la_misma_franja FROM cita WHERE estado <> 'CANCELADA' GROUP BY id_veterinario, fecha_hora HAVING COUNT(*) > 1;`
   Debe devolver la franja duplicada.
3. **Limpie el duplicado** (borra una de las dos citas recien creadas, la de mayor `id_cita`).
4. **Aplique la mitigacion**: un **indice unico parcial**, que es la forma correcta aqui porque las citas canceladas si pueden repetir franja:
   `CREATE UNIQUE INDEX uq_cita_vet_franja ON cita (id_veterinario, fecha_hora) WHERE estado <> 'CANCELADA';`
5. **Pruebe que ahora la base rechaza el conflicto**, capturando el error para que el script no se detenga:
   ```sql
   DO $$
   BEGIN
     INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
     VALUES (4, 1, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');
     INSERT INTO evidencia (paso, resultado) VALUES ('con restriccion', 'FALLO: se permitio la doble reserva');
   EXCEPTION WHEN unique_violation THEN
     INSERT INTO evidencia (paso, resultado) VALUES ('con restriccion', 'OK rechazada: ' || SQLERRM);
   END $$;
   ```
6. **Pruebe que la excepcion es correcta**, no excesiva: inserta la **misma franja** pero con estado `'CANCELADA'`, que **debe** ser aceptada por el indice parcial. Registra el resultado en `evidencia`.
7. Cierre con `SELECT paso, resultado FROM evidencia ORDER BY id_evidencia;` y con la consulta de deteccion del paso 2, que ahora debe devolver **cero filas**.

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

CREATE TABLE evidencia (
  id_evidencia SERIAL PRIMARY KEY,
  paso TEXT NOT NULL,
  resultado TEXT NOT NULL,
  registrado_en TIMESTAMP NOT NULL DEFAULT now()
);
```

**Rubrica esperada (campo Rubrica):**

Se demuestra primero que sin restriccion la doble reserva se inserta sin error y la consulta de deteccion la encuentra. Se crea el indice unico PARCIAL sobre (id_veterinario, fecha_hora) con la condicion estado <> 'CANCELADA'. El intento posterior se rechaza y queda capturado como unique_violation en evidencia, y la insercion con estado CANCELADA si es aceptada, probando que la restriccion no es excesiva. La deteccion final devuelve cero filas y el script no aborta.

---

## Pregunta 3 - SQL sobre PostgreSQL real · 20 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 3. Doble descuento de stock: bloqueo explicito y actualizacion condicional

Esquema completo de VetCare poblado. Insumo 2 (Vacuna triple felina) tiene **stock 3**; insumo 5 (Gasa esteril) tiene **stock 8**.

Dos auxiliares facturan al mismo tiempo y ambas quieren 3 unidades del insumo 2. Hay para una sola. Vas a implementar y comparar **dos** mecanismos de PostgreSQL que resuelven esto.

**Parte A - Actualizacion condicional (sin bloqueo explicito).**

1. Escribe una funcion `fn_tomar_stock(p_id_insumo INT, p_cantidad INT)` que retorne `BOOLEAN`, haga `UPDATE insumo SET stock = stock - p_cantidad WHERE id_insumo = p_id_insumo AND stock >= p_cantidad;`, lea `GET DIAGNOSTICS v_filas = ROW_COUNT;` y retorne `v_filas = 1`.
2. Ejecuta `SELECT fn_tomar_stock(2, 3) AS primera, fn_tomar_stock(2, 3) AS segunda;` y muestra que la primera devuelve `true` y la segunda `false`: la segunda "auxiliar" se queda sin insumo, pero el stock **nunca** baja de 0.
3. Muestra `SELECT id_insumo, nombre, stock FROM insumo WHERE id_insumo IN (2, 5);`

**Parte B - Bloqueo explicito de fila.**

4. Escribe un bloque `DO` que simule la parte critica de una transaccion: primero `SELECT stock INTO v_stock FROM insumo WHERE id_insumo = 5 FOR UPDATE;` (esto **bloquea esa fila** hasta el final de la transaccion), luego valide `IF v_stock >= 4 THEN UPDATE ... END IF;`, y registre con `RAISE NOTICE` lo que hizo.
5. Escribe otro bloque `DO` identico pero pidiendo `FOR UPDATE NOWAIT` o `FOR UPDATE SKIP LOCKED` sobre el insumo 5, y comenta con `--` en que se diferencian los tres comportamientos (`FOR UPDATE` espera, `NOWAIT` falla de inmediato, `SKIP LOCKED` ignora la fila bloqueada).
6. Cierra con un comentario `--` de 3 o 4 lineas respondiendo: **por que en esta sesion unica los tres se comportan igual** (nadie mas tiene la fila tomada, asi que nunca hay espera), **que veriamos en un servidor real** con dos sesiones, y **cual de los dos mecanismos (A o B) elegis para VetCare y por que** (pista: A resuelve la comprobacion y la escritura en una sola sentencia atomica; B es necesario cuando hay que leer, calcular con datos de varias tablas y despues escribir).

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

fn_tomar_stock usa el UPDATE condicional con GET DIAGNOSTICS y la prueba arroja true y luego false, con el stock del insumo 2 en 0 y nunca negativo. Se escriben los bloques DO con SELECT ... FOR UPDATE y con NOWAIT o SKIP LOCKED, y se explica correctamente la diferencia entre los tres. El comentario final reconoce que en una sola sesion no hay espera observable, describe que ocurriria con dos sesiones y elige un mecanismo con argumento tecnico.

---

## Pregunta 4 - Seleccion multiple · 10 pts

**Tipo en la plataforma:** `cerrada_multi`

**Enunciado (campo Contenido):**

## 4. Niveles de aislamiento y anomalias en PostgreSQL

Selecciona **todas** las afirmaciones correctas sobre aislamiento y concurrencia en PostgreSQL, pensando en VetCare.

**Opciones:**

- [x] El nivel por defecto en PostgreSQL es READ COMMITTED: cada sentencia ve una foto nueva de los datos confirmados, asi que dos lecturas dentro de la misma transaccion pueden dar resultados distintos.
- [x] READ COMMITTED evita las lecturas sucias (dirty reads), pero no las lecturas no repetibles ni los fantasmas sobre un predicado.
- [ ] En PostgreSQL, READ UNCOMMITTED permite leer datos no confirmados de otras transacciones.
- [x] Con SERIALIZABLE, PostgreSQL puede abortar una transaccion con un error de serializacion; la aplicacion debe estar preparada para reintentarla.
- [ ] Una restriccion UNIQUE resuelve el problema solo si las transacciones se ejecutan una despues de otra; si son simultaneas, la restriccion no aplica.
- [x] Mantener las transacciones cortas reduce la ventana de conflicto: nunca hay que dejar una transaccion abierta esperando que el usuario llene un formulario.

**Rubrica esperada (campo Rubrica):**

10 puntos con las 4 opciones correctas y ninguna incorrecta; puntaje proporcional por acierto parcial. Correctas: indices 0, 1, 3 y 5.

---

## Pregunta 5 - Respuesta escrita · 20 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## 5. Informe de concurrencia del PI y limites de la verificacion

Redacta la seccion "Control de concurrencia" del informe del PI, con:

1. **Escenario 2: doble descuento de stock**, con linea de tiempo T1/T2 de al menos 5 pasos, igual que hiciste con la doble reserva. Contexto: dos auxiliares facturan la ultima Vacuna triple felina (stock 3, ambas piden 3). Marca el instante del `SELECT stock` de cada una y el del `UPDATE`.
2. **Mitigacion elegida para cada escenario**, con la sentencia SQL exacta que la implementa: cual es para la doble reserva (indice unico parcial) y cual para el stock (`UPDATE ... WHERE stock >= cantidad` o `SELECT ... FOR UPDATE`), y por que descartaste las otras.
3. **Contrato con la aplicacion**: que error recibe la aplicacion en cada caso (violacion de unicidad, funcion que devuelve `false`, error de serializacion) y **que debe hacer**: mostrar mensaje, ofrecer otra franja, reintentar automaticamente, o abortar. Una fila por caso.
4. **Limitacion del entorno, explicitamente.** Escribe por que **no** fue posible reproducir un bloqueo ni un deadlock reales en ExamLab: PostgreSQL corre compilado a WebAssembly dentro del navegador con **una unica conexion**, asi que no existen dos transacciones concurrentes que puedan esperarse. Indica que herramientas usarias en un servidor real para hacer esa prueba (dos sesiones de `psql`, `pgbench`, las vistas `pg_locks` y `pg_stat_activity`) y que evidencia concreta capturarias.
5. **Riesgo residual**: que escenario de concurrencia de VetCare queda sin mitigar y como lo vigilarias.

**Rubrica esperada (campo Rubrica):**

El escenario 2 tiene linea de tiempo de al menos 5 pasos con los instantes de lectura y escritura marcados. Cada mitigacion viene con su sentencia SQL exacta y con el descarte razonado de las alternativas. La tabla del contrato cubre los tres tipos de error con la accion de la aplicacion. La seccion 4 reconoce con precision la limitacion de sesion unica de PGlite y nombra herramientas reales de verificacion. Se identifica al menos un riesgo residual con su forma de vigilancia.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
