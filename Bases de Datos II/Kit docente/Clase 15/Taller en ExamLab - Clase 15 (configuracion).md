# Taller de la Clase 15 en ExamLab - configuracion

- **Curso:** Bases de Datos II (FI303215)
- **Taller:** Taller Clase 15 en ExamLab - Entrega final y cierre de VetCare DB (previo a la sustentacion en vivo)
- **Preguntas:** 5 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://examlab.lovable.app/) · modulo Talleres
- **Hito del PI:** Sustentacion en vivo y entrega final del PI (20% Corte 3)
- **Entregable de la clase:** ZIP/PDF final subido antes del turno + sustentacion en vivo 5-8 min + Q&A

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante entrega el script maestro de VetCare que se ejecuta de cero y prueba sus tres reglas de negocio, los KPIs de la sustentacion, el acta de entrega y la autoevaluacion de cierre.

---

## Pregunta 1 - SQL sobre PostgreSQL real · 35 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 1. Script maestro de entrega: VetCare DB de cero, en una sola corrida

**Evaluacion final del PI (20 % del Corte 3). Debe quedar entregado ANTES de tu turno de sustentacion en vivo. Lee el enunciado completo antes de escribir.**

Esta base esta **vacia**: solo existe la tabla `entrega_final` donde registras tu paquete. Debes entregar aqui el **script maestro** de VetCare DB, el mismo que va en el ZIP: se ejecuta **una sola vez, de arriba abajo, sobre una base limpia**, y debe correr **sin un solo error**.

Ese script debe contener, en este orden:

**Bloque 0 - Registro.** Un `INSERT INTO entrega_final (estudiante, codigo, proyecto, enlace_zip)` con tus datos reales. Si el docente autorizo equipo, llena tambien la columna opcional `integrantes`; si trabajas solo, dejala nula.

**Bloque 1 - DDL completo.** Las **8 tablas** del PI: `dueno`, `mascota`, `veterinario`, `cita`, `consulta`, `insumo`, `factura`, `detalle_factura`, con PK, todas las FK y las restricciones de dominio (`CHECK` de `mascota.activa`, `CHECK` de `cita.estado`, `CHECK (stock >= 0)`, `CHECK (cantidad > 0)`, `CHECK (precio >= 0)`). Incluye tambien la tabla de auditoria `audit_cita`.

**Bloque 2 - Datos semilla.** Minimo **5 duenos, 3 veterinarios, 8 mascotas (al menos 2 inactivas), 8 citas en distintos estados, 4 insumos (al menos uno con stock menor a 5) y 2 facturas con sus detalles**. Nombres en espanol, coherentes con una veterinaria de Cali.

**Bloque 3 - Logica de negocio.** Como minimo:
- una funcion (por ejemplo `fn_precio_consulta`),
- un procedimiento de negocio con validacion (por ejemplo `sp_agendar_cita`, que rechace mascota inactiva),
- un trigger de auditoria de cambio de estado de cita sobre `audit_cita`.

**Bloque 4 - Indices.** Al menos **dos** indices con nombre claro sobre las columnas de filtro de tus reportes.

**Bloque 5 - Pruebas de aceptacion de las tres reglas del PI.** Tres bloques `DO` que capturen la excepcion (`EXCEPTION WHEN OTHERS THEN RAISE NOTICE '%', SQLERRM;`) y demuestren que:
1. una mascota inactiva **no** puede agendar cita;
2. el stock de un insumo **no** puede quedar negativo;
3. un cambio de estado de cita **queda** auditado en `audit_cita`.

**Bloque 6 - Consulta de cierre.** Una unica consulta que devuelva el inventario de la entrega: nombre de tabla y numero de filas para las 8 tablas mas `audit_cita`. Puedes construirla con `UNION ALL` de `SELECT 'cita', COUNT(*) FROM cita`, etc.

Sintaxis **PostgreSQL** en todo el script. Nada de `NUMBER`, `VARCHAR2`, `RAISE_APPLICATION_ERROR`, `DUAL`, `SQL%ROWCOUNT` ni `/` de terminacion.

**SQL de partida (`options.db.setupSql`)** - corre antes del SQL del
estudiante, sobre una base limpia. PostgreSQL, no Oracle:

```sql
-- Base limpia para la entrega final del PI.
CREATE TABLE entrega_final (
  id_entrega SERIAL PRIMARY KEY,
  estudiante TEXT NOT NULL,
  codigo TEXT NOT NULL,
  proyecto TEXT NOT NULL,
  integrantes TEXT,  -- opcional: solo si el docente autorizo equipo
  enlace_zip TEXT,
  fecha_entrega DATE NOT NULL DEFAULT CURRENT_DATE
);

INSERT INTO entrega_final (estudiante, codigo, proyecto, enlace_zip)
VALUES ('Ejemplo del docente', '000000', 'VetCare-Demo', 'https://ejemplo.uniajc/entrega-demo.zip');
```

**Rubrica esperada (campo Rubrica):**

El script corre completo sin errores sobre la base limpia. Estan los 7 bloques: registro, DDL de las 8 tablas mas audit_cita con PK/FK/CHECK, datos semilla con los minimos exigidos, funcion + procedimiento con validacion + trigger de auditoria, dos indices nombrados, las 3 pruebas de aceptacion capturadas y la consulta de inventario. Las tres reglas de negocio quedan efectivamente demostradas. Cero sintaxis Oracle.

---

## Pregunta 2 - SQL sobre PostgreSQL real · 20 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 2. Los KPIs que se proyectan en la sustentacion

Esta base trae el **VetCare completo** poblado (8 tablas con datos: 6 duenos, 4 veterinarios, 8 mascotas, 10 citas, 4 consultas, 6 insumos, 3 facturas con 8 lineas de detalle).

Escribe las **cuatro consultas** que vas a proyectar en la diapositiva de resultados. Cada una en una sola sentencia:

**K1 - Carga por veterinario.** Nombre del veterinario, total de citas, cuantas atendidas, cuantas canceladas y el **porcentaje de cancelacion** redondeado a un decimal. Los veterinarios sin citas deben aparecer con ceros y **sin division por cero** (usa `NULLIF` o `CASE`). Ordena por total de citas descendente.

**K2 - Ingresos por mes.** Para cada mes con facturacion: el mes (usa `date_trunc('month', f.fecha)`), numero de facturas y total facturado. Ordena cronologicamente.

**K3 - Top insumos consumidos.** Nombre del insumo, unidades totales vendidas segun `detalle_factura`, valor total generado (`SUM(cantidad * precio_unit)`) y stock restante. Incluye los insumos que **nunca** se han vendido, con 0 (usa `LEFT JOIN` y `COALESCE`). Ordena por unidades vendidas descendente.

**K4 - Ficha de un dueno (historia clinica resumida).** Para el dueno `Ana Gomez`: una fila por cita de cualquiera de sus mascotas, con nombre de la mascota, `fecha_hora`, `estado`, veterinario, diagnostico (puede venir vacio si la cita no genero consulta) y el total facturado de esa consulta (tambien puede venir vacio). Usa `LEFT JOIN` para no perder las citas sin consulta y filtra el dueno por nombre.

Al final, escribe en comentarios `--` una linea por KPI diciendo **que decision de la clinica** habilita cada numero y **que numero concreto** te salio.

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

Las 4 consultas corren y devuelven resultados coherentes con los datos entregados. K1 evita la division por cero y conserva veterinarios sin citas. K2 agrupa por mes con date_trunc y ordena cronologicamente. K3 incluye los insumos nunca vendidos con ceros. K4 usa LEFT JOIN de modo que aparecen tambien las citas sin consulta ni factura, filtrando por el dueno indicado. Los comentarios reportan el numero real obtenido y la decision que habilita.

---

## Pregunta 3 - Seleccion multiple · 10 pts

**Tipo en la plataforma:** `cerrada_multi`

**Enunciado (campo Contenido):**

## 3. Checklist de empaquetado del ZIP final

Vas a subir el paquete final al modulo de Proyectos de ExamLab. Selecciona **todas** las afirmaciones correctas sobre como debe quedar armado el entregable.

**Opciones:**

- [x] Los scripts deben ir numerados en su orden de ejecucion (01_ddl.sql, 02_datos.sql, 03_logica.sql, ...) para que cualquiera pueda reconstruir la base de cero.
- [x] Debe incluirse un README que diga en que motor se probo (PostgreSQL), como ejecutar los scripts y en que orden, y quien hizo que.
- [ ] Basta con adjuntar capturas de pantalla de las consultas funcionando; el codigo fuente es opcional si la demo salio bien.
- [x] El ER debe ir tanto en imagen (PNG o el diagrama Mermaid) como reflejado en el DDL: si no coinciden, el entregable es inconsistente.
- [ ] Conviene incluir las credenciales de tu base de datos en el README para que el docente pueda entrar.
- [x] El informe debe traer las secciones que se fueron construyendo en el semestre: roles y privilegios, respaldo, optimizacion antes/despues, indices, transacciones, concurrencia y lecciones de casos reales.

**Rubrica esperada (campo Rubrica):**

10 puntos con las 4 opciones correctas y ninguna incorrecta; puntaje proporcional por acierto parcial. Correctas: indices 0, 1, 3 y 5.

---

## Pregunta 4 - Respuesta escrita · 20 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## 4. Acta de entrega y reparto de la sustentacion

Entrega el acta que acompana el paquete final. Debe contener:

1. **Identificacion**: tu nombre completo y codigo, nombre del proyecto, asignatura (Bases de Datos II, FI303215), periodo 2026-2 y fecha de entrega. Si el docente autorizo equipo, lista tambien a los demas integrantes.
2. **Inventario del paquete**: tabla con cada archivo del ZIP, su proposito y su orden de ejecucion. Deben aparecer como minimo el DDL, los datos semilla, la logica (funciones, procedimientos, triggers), los indices, el par antes/despues de optimizacion, el script de pruebas de las tres reglas de negocio, el informe y el ER.
3. **Trazabilidad hito por hito**: una fila por clase del semestre (1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13) indicando **que artefacto del paquete** contiene el avance de esa clase. Si algo quedo sin cerrar, dilo aqui.
4. **Guion de la sustentacion (5 a 8 minutos)**: que bloque expones en cada tramo y cuantos minutos, sumando entre 5 y 8. Si trabajas en equipo autorizado, indica quien habla en cada bloque: **todos los integrantes deben hablar**.
5. **Declaracion de autoria y uso de herramientas**: que hiciste tu (y cada integrante, si hubo equipo), y si usaste asistentes de IA o codigo de terceros, en que parte y como lo verificaste.
6. **Estado final declarado**: `COMPLETO`, `COMPLETO CON OBSERVACIONES` o `INCOMPLETO`, con una justificacion de dos lineas y tu firma (y la de los demas integrantes, si hubo equipo).

**Rubrica esperada (campo Rubrica):**

Las 6 secciones estan completas. El inventario nombra archivos concretos con su orden de ejecucion y cubre los minimos exigidos. La trazabilidad asocia cada una de las 11 clases con un artefacto real del paquete y reconoce lo que quedo abierto. El guion de sustentacion suma entre 5 y 8 minutos y cubre todos los bloques; si hubo equipo autorizado, asigna voz a todos los integrantes. Hay declaracion de autoria y uso de herramientas, y un estado final justificado y firmado.

---

## Pregunta 5 - Respuesta escrita · 15 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## 5. Autoevaluacion de cierre: que harias distinto

Cierra el curso con una autoevaluacion honesta. Responde cada punto en 3 a 6 lineas:

1. **La decision de diseno de la que estas mas orgulloso**: cual fue, por que la tomaste y que evidencia tienes de que fue acertada (una prueba que pasa, una consulta que bajo de X a Y milisegundos, un error que la base rechazo).
2. **La decision que cambiarias**: que harias diferente si empezaras VetCare de nuevo desde la Clase 1. Se especifico: un tipo de dato, una tabla que falta, una regla que dejaste en la aplicacion y debio estar en la base, un indice que no servia.
3. **El concepto que mas te costo** de todo el semestre (transacciones, concurrencia, planes de ejecucion, privilegios, triggers) y **como lo desatascaste**. Si todavia no lo tienes claro, dilo: reconocerlo vale mas que fingir.
4. **De Oracle a PostgreSQL**: durante el curso pasaste de material escrito en PL/SQL a resolver todo en PL/pgSQL sobre PostgreSQL. Nombra **tres diferencias concretas de sintaxis o de comportamiento** que tuviste que aprender (por ejemplo `RAISE EXCEPTION` frente a `RAISE_APPLICATION_ERROR`, `GET DIAGNOSTICS ... ROW_COUNT` frente a `SQL%ROWCOUNT`, funcion de trigger separada del trigger, ausencia de `DUAL`) y por que importan.
5. **Lo que se queda sin verificar**: que parte de tu diseno **no** pudiste probar en este entorno (concurrencia real con dos sesiones, roles con usuarios conectados de verdad, particionamiento con volumen real, respaldo fisico) y como lo verificarias en un servidor de produccion.
6. **Nota que te pondrias** a tu propio trabajo en el PI, de 1 a 5, con una linea de justificacion. Si trabajaste en equipo autorizado, agrega en una linea aparte la nota que le pondrias al aporte de cada integrante.

**Rubrica esperada (campo Rubrica):**

Los 6 puntos estan respondidos con especificidad y evidencia, no con generalidades. El punto 1 cita una evidencia concreta y el 2 nombra un cambio de diseno preciso. El punto 4 lista tres diferencias reales entre PL/SQL y PL/pgSQL explicando por que importan. El punto 5 identifica correctamente los limites del entorno de practica y propone como verificarlos en produccion. La autonota viene justificada.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
