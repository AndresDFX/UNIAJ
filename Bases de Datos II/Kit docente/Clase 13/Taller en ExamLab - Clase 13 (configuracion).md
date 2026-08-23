# Taller de la Clase 13 en ExamLab - configuracion

- **Curso:** Bases de Datos II (FI303215)
- **Taller:** Taller Clase 13 en ExamLab - Analisis de casos reales aplicado a VetCare (clase autonoma)
- **Preguntas:** 5 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** Informe de caso -> mejoras concretas al PI
- **Entregable de la clase:** Informe 1-2 pag.: caso + 3 mejoras aplicables a VetCare

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante analiza un incidente real de bases de datos y lo convierte en dos mejoras implementadas y probadas sobre VetCare (blindaje de SQL dinamico y auditoria de borrados con restauracion), mas un plan de mejoras priorizado.

---

## Pregunta 1 - Respuesta escrita · 25 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## 1. El caso: que paso, por que y que aprendemos

**Clase autonoma: no hay docente en vivo. Todo lo que necesitas para responder esta en este enunciado.**

Elige **uno** de estos tres casos reales de fallos de bases de datos (o propon otro documentado, citando la fuente):

- **A. Perdida de datos por respaldo no verificado.** GitLab, enero de 2017: durante un incidente de carga, un ingeniero ejecuto un borrado sobre el directorio de datos del servidor equivocado. De cinco mecanismos de respaldo, **ninguno** funciono como se esperaba; se recuperaron datos de una copia de seguridad de casi seis horas antes y se perdio informacion de forma definitiva.
- **B. Rendimiento que tumba el servicio.** Una consulta de reporte sin indice y con `SELECT *` sobre una tabla de decenas de millones de filas, ejecutada cada minuto por un panel de control, agota la memoria y las conexiones del servidor y deja fuera de servicio a toda la aplicacion en hora pico.
- **C. Seguridad: inyeccion de SQL.** Una aplicacion construye sus consultas concatenando lo que el usuario escribe en un formulario de busqueda. Un atacante envia una cadena con comillas y `OR '1'='1'` y obtiene el listado completo de la base, incluidos datos personales de los clientes.

Redacta **media pagina** con esta estructura:

1. **Contexto**: que organizacion o tipo de sistema, que hacia y que estaba en juego.
2. **Que fallo**: la secuencia de hechos, en orden. Se lo mas concreto que puedas.
3. **Causa raiz**, distinguiendola de la causa aparente. La causa aparente suele ser "alguien se equivoco"; la raiz suele ser "no habia un control que detuviera ese error".
4. **Impacto**: datos, dinero, tiempo, confianza.
5. **Leccion en una frase**, redactada como regla accionable ("un respaldo que no se ha restaurado no es un respaldo").
6. **Traduccion a VetCare**: cual de las tablas o procesos de tu proyecto (`cita`, `insumo`, `factura`, `audit_cita`, tu capa `api_*`) es vulnerable al **mismo** tipo de fallo, y por que.

Si eliges un caso propio, incluye la fuente (enlace o publicacion) al final.

**Rubrica esperada (campo Rubrica):**

Las 6 secciones estan presentes. La causa raiz se distingue explicitamente de la causa aparente y apunta a un control ausente, no a la culpa de una persona. El impacto es concreto. La leccion esta redactada como regla accionable. La traduccion a VetCare nombra tablas o procesos reales del proyecto y explica el mecanismo de la vulnerabilidad, no una analogia vaga. Si el caso es propio, trae fuente.

---

## Pregunta 2 - SQL sobre PostgreSQL real · 25 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 2. Mejora implementada 1: cerrar la inyeccion de SQL en VetCare

El esquema `dueno`, `mascota`, `veterinario`, `cita` esta creado y poblado (8 mascotas; **Rocky** y **Kiara** inactivas). La base trae, a proposito, una funcion **vulnerable** que el desarrollador de turno escribio en su momento para el buscador de mascotas:

```sql
CREATE FUNCTION buscar_mascota_insegura(p_nombre TEXT)
RETURNS TABLE (id_mascota INT, nombre TEXT, especie TEXT, activa CHAR(1))
LANGUAGE plpgsql AS $fn$
BEGIN
  RETURN QUERY EXECUTE
    'SELECT id_mascota, nombre, especie, activa FROM mascota WHERE nombre = ''' || p_nombre || '''';
END;
$fn$;
```

Escribe el SQL que:

1. **Demuestre el uso normal**: `SELECT * FROM buscar_mascota_insegura('Firulais');` -> debe devolver 1 fila.
2. **Demuestre el ataque**: `SELECT * FROM buscar_mascota_insegura('Firulais'' OR ''1''=''1');`
   (en SQL, para escribir una comilla simple dentro de una cadena se duplica). Debe devolver **las 8 mascotas**: la concatenacion dejo que el usuario reescribiera el `WHERE`.
3. **Cuantifique la fuga**: `SELECT COUNT(*) FROM buscar_mascota_insegura('x'' OR ''1''=''1');` y compara con `SELECT COUNT(*) FROM mascota;`. Deben coincidir: eso es la evidencia del incidente.
4. **Implemente la version segura** `buscar_mascota_segura(p_nombre TEXT)` con la misma firma de retorno, usando **parametros ligados** en el SQL dinamico:
   ```sql
   RETURN QUERY EXECUTE
     'SELECT id_mascota, nombre, especie, activa FROM mascota WHERE nombre = $1'
     USING p_nombre;
   ```
   (Mejor aun: como aqui no hace falta SQL dinamico, escribe **tambien** una variante `buscar_mascota_directa(p_nombre TEXT)` que use una consulta estatica `SELECT ... WHERE nombre = p_nombre`, sin `EXECUTE`.)
5. **Pruebe que el agujero quedo cerrado**: repite el ataque contra la version segura,
   `SELECT * FROM buscar_mascota_segura('Firulais'' OR ''1''=''1');` -> debe devolver **0 filas**, porque ahora esa cadena completa se compara como un **valor**, no como codigo.
6. **Elimine la funcion vulnerable** con `DROP FUNCTION buscar_mascota_insegura(TEXT);` y deje un comentario `--` con la regla que adoptas sobre SQL dinamico y parametros ligados.

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

-- Funcion VULNERABLE a proposito: concatena la entrada del usuario en SQL dinamico.
CREATE FUNCTION buscar_mascota_insegura(p_nombre TEXT)
RETURNS TABLE (id_mascota INT, nombre TEXT, especie TEXT, activa CHAR(1))
LANGUAGE plpgsql
AS $fn$
BEGIN
  RETURN QUERY EXECUTE
    'SELECT id_mascota, nombre, especie, activa FROM mascota WHERE nombre = ''' || p_nombre || '''';
END;
$fn$;
```

**Rubrica esperada (campo Rubrica):**

Se demuestra el uso normal y el ataque, evidenciando con COUNT que la funcion insegura devuelve todas las mascotas. Se crea la version segura con EXECUTE ... USING (y opcionalmente la variante estatica) manteniendo la firma de retorno. El mismo ataque contra la version segura devuelve 0 filas. Se hace DROP de la funcion vulnerable y se enuncia la regla propia. Se descuenta si no se muestra el contraste cuantitativo antes/despues.

---

## Pregunta 3 - SQL sobre PostgreSQL real · 25 pts

**Tipo en la plataforma:** `bd_sql`

**Enunciado (campo Contenido):**

## 3. Mejora implementada 2: ningun borrado sin traza ni sin vuelta atras

El esquema `dueno`, `mascota`, `veterinario`, `cita` esta creado y poblado con **10 citas**. Esta base **no** tiene las tablas `consulta` ni `factura`, para que el `DELETE` del incidente pueda ejecutarse sin tropezar con llaves foraneas.

Vas a implementar el control que le falto al caso del respaldo no verificado. Escribe el SQL que:

1. **Respaldo logico previo y su bitacora.** Crea `respaldo_cita` como copia exacta de `cita` (`CREATE TABLE respaldo_cita AS SELECT * FROM cita;`) y una tabla `bitacora_respaldo (id_bitacora SERIAL, tabla TEXT, filas_respaldadas INT, hecho_en TIMESTAMP DEFAULT now())`. Inserta en la bitacora el conteo real de filas respaldadas (obtenlo con una subconsulta `SELECT COUNT(*) FROM respaldo_cita`, no lo escribas a mano).
2. **Archivo de borrados + trigger.** Crea `cita_borrada` con las mismas columnas que `cita` mas `borrado_en TIMESTAMP DEFAULT now()` y `usuario_bd TEXT DEFAULT current_user`. Crea la funcion `fn_trg_archivar_cita()` que `RETURNS TRIGGER`, inserte en `cita_borrada` los valores de `OLD` (columna por columna) y haga `RETURN OLD` para permitir el borrado. Asocia el trigger `trg_archivar_cita` **BEFORE DELETE ON cita FOR EACH ROW**.
3. **Reproduce el incidente.** Ejecuta `DELETE FROM cita;` (el borrado accidental sin `WHERE`). Muestra con dos consultas que `cita` quedo en **0 filas** y que `cita_borrada` tiene las **10**.
4. **Restaura.** Repuebla `cita` desde `cita_borrada` (o desde `respaldo_cita`) con un `INSERT INTO cita (...) SELECT ...` de columnas explicitas.
5. **Verifica la restauracion como se debe.** Escribe **una** consulta de validacion post-restauracion que devuelva, en una sola fila: filas esperadas (de `bitacora_respaldo`), filas actuales en `cita`, `MIN(fecha_hora)`, `MAX(fecha_hora)` y una columna `veredicto` con `'RESTAURACION OK'` o `'REVISAR'` segun coincidan o no los conteos (usa `CASE`). Esta consulta es la que faltaba en el caso real: **un respaldo que no se ha restaurado y verificado no es un respaldo**.
6. Cierra con un comentario `--` de dos o tres lineas explicando por que el trigger de archivo y la consulta de verificacion son controles **distintos** y por que hacen falta los dos.

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

Se crean respaldo_cita, bitacora_respaldo (con el conteo calculado, no literal), cita_borrada y el trigger BEFORE DELETE que archiva OLD y retorna OLD. El DELETE sin WHERE deja cita en 0 y cita_borrada en 10. La restauracion repone las 10 filas con columnas explicitas. La consulta de validacion devuelve una sola fila con esperadas, actuales, min, max y el veredicto calculado con CASE. El comentario final distingue correctamente los dos controles.

---

## Pregunta 4 - Seleccion multiple · 10 pts

**Tipo en la plataforma:** `cerrada_multi`

**Enunciado (campo Contenido):**

## 4. Que control habria evitado el incidente

Selecciona **todas** las afirmaciones correctas sobre los controles que previenen los fallos analizados.

**Opciones:**

- [x] Un respaldo solo cuenta como valido cuando se ha restaurado en un entorno de prueba y una consulta de verificacion confirmo conteos y rangos de datos esperados.
- [ ] Escapar manualmente las comillas de la entrada del usuario antes de concatenarla es equivalente a usar parametros ligados.
- [x] Usar parametros ligados (EXECUTE ... USING, o %s desde la aplicacion) elimina la inyeccion porque la entrada viaja como valor y nunca se interpreta como codigo SQL.
- [ ] Tener cinco mecanismos de respaldo garantiza la recuperacion, aunque ninguno se haya probado.
- [x] Un trigger que archiva las filas antes de borrarlas convierte un borrado accidental en un incidente recuperable, aunque no evita el error humano.
- [x] Un indice adecuado mas la eliminacion de SELECT * en un reporte que corre cada minuto pueden ser la diferencia entre un panel util y una caida del servicio en hora pico.

**Rubrica esperada (campo Rubrica):**

10 puntos con las 4 opciones correctas y ninguna incorrecta; puntaje proporcional por acierto parcial. Correctas: indices 0, 2, 4 y 5.

---

## Pregunta 5 - Respuesta escrita · 15 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## 5. Tres mejoras priorizadas para VetCare

Cierra el informe con el plan de mejoras que adoptas a partir del caso. Entrega una tabla de **exactamente tres** filas:

| # | Mejora concreta | Objeto de VetCare que cambia | Riesgo que mitiga | Esfuerzo (bajo/medio/alto) | Impacto (bajo/medio/alto) | Como se verifica | Estado |
|---|---|---|---|---|---|---|---|

Reglas:

- **Dos** de las tres mejoras deben ser las que **ya implementaste** en las preguntas 2 y 3; su estado es `IMPLEMENTADA` y en la columna de verificacion debes citar la prueba concreta que corriste (por ejemplo: "el ataque contra `buscar_mascota_segura` devuelve 0 filas").
- La tercera es una mejora **pendiente**, derivada del caso, con estado `PENDIENTE`, responsable y fecha.
- Cada mejora debe nombrar un objeto real de tu base (tabla, funcion, trigger, indice, rol), no una intencion general.

Debajo de la tabla, responde en 4 a 6 lineas:

1. **Priorizacion**: cual de las tres harias primero si solo tuvieras un dia y por que, usando la relacion esfuerzo/impacto.
2. **Que dice esto de tu diseno**: que supuesto de tu PI quedo en evidencia con el caso analizado.
3. **Actualizacion del informe del PI**: en que seccion del informe final entra este analisis y que frase agregas a las lecciones aprendidas.

**Rubrica esperada (campo Rubrica):**

La tabla tiene exactamente 3 filas con las 8 columnas; dos mejoras estan marcadas IMPLEMENTADA y citan la prueba real ejecutada en las preguntas 2 y 3, y la tercera es PENDIENTE con responsable y fecha. Cada fila nombra un objeto real de la base. La priorizacion argumenta con esfuerzo/impacto y se identifica el supuesto de diseno que el caso puso en evidencia.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
