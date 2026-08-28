# Solucion del taller · Clase 7 · Indices y particionamiento de VetCare

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** La promesa que quedo abierta en la Clase 6, cumplida y medida: los tres indices de las tablas calientes con la evidencia de que el planeador **si** los usa —incluido el parcial, que es el que gana la agenda del dia—, el experimento del orden de columnas con el `DROP INDEX` que demuestra por que un indice cuya columna lider no esta en el `WHERE` se queda sin usar, el historico particionado por ano con sus **2.620 y 2.390** filas enrutadas y la poda visible en el plan, las cuatro afirmaciones correctas sobre sobre-indexar, y la tabla de justificacion consulta → indice que va al informe con su veredicto honesto sobre particionamiento.

> **El motor es PostgreSQL, no Oracle:** aqui hay indices **parciales** (`CREATE INDEX ... WHERE ...`), `Bitmap Index Scan` y `pg_indexes`; no hay `USER_INDEXES`, ni indices de mapa de bits de Oracle, ni `REBUILD ONLINE`. Cuatro avisos operativos. Primero: cada pregunta arranca con su **propia base recien sembrada** y **sin indices** mas alla de las llaves primarias, asi que los `CREATE INDEX` de la pregunta 1 **no existen** en la pregunta 2 —hay que volver a crear lo que se necesite—. Segundo: las preguntas 1, 2 y 4 corren sobre las 30.010 citas, pero la pregunta 3 corre sobre **otra base**, con 5.010 citas repartidas entre 2025 y 2026; los numeros no se pueden mezclar. Tercero: con 5.010 filas el particionamiento **no** va a ser mas rapido, y eso no es un defecto del ejercicio sino su leccion —lo que se demuestra es la poda de particiones y el archivado, no la velocidad—. Cuarto: hay que insistir en el orden `CREATE INDEX` → `ANALYZE` → `EXPLAIN`; quien mida sin `ANALYZE` de por medio va a ver planes que no explican nada y va a creer que el indice no sirve.

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 7 - Indices y particionamiento/Taller PI - Clase 7 - VetCare.docx`
- Configuracion en la plataforma: `Kit docente/Clase 7/Taller en ExamLab - Clase 7 (configuracion).md`
- Caso de estudio: `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
- Hito del PI: >=2 indices justificados sobre tablas calientes del PI
- Entregable: Script CREATE INDEX + tabla justificacion consulta->indice
- **Estas preguntas: 100 puntos** en 5 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 1 | Crear los indices de las tablas calientes y probar que se usan | `bd_sql` | 30 |
| 2 | Orden de columnas en un indice compuesto | `bd_sql` | 20 |
| 3 | Particionar el historico de citas por rango de fecha | `bd_sql` | 20 |
| 4 | Riesgos de sobre-indexar VetCare | `cerrada_multi` | 10 |
| 5 | Tabla de justificacion consulta -> indice | `abierta` | 20 |

---

## Pregunta 1 · Crear los indices de las tablas calientes y probar que se usan · 30 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- PASO 1. LINEA BASE. Sin esto no hay nada que comparar despues, y es lo
    -- que mas se olvida: una vez creado el indice ya no se puede volver a
    -- medir el "antes" sin borrarlo.
    -- =====================================================================
    EXPLAIN ANALYZE   -- C1: agenda del dia
    SELECT id_cita, fecha_hora, estado
      FROM cita
     WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
       AND estado = 'PROGRAMADA';

    EXPLAIN ANALYZE   -- C2: mascotas de un dueno
    SELECT id_mascota, nombre, especie
      FROM mascota
     WHERE id_dueno = 1234;

    -- =====================================================================
    -- PASO 2. LOS TRES INDICES, con los nombres exactos que pide el
    -- enunciado. El nombre no es un capricho: en la pregunta 5 hay que
    -- referirse a cada uno, y en el plan aparece literalmente
    -- "Index Scan using <nombre>".
    -- =====================================================================

    -- (a) fecha_hora es la columna mas selectiva de cita: 30.010 filas
    --     repartidas en 200 dias, unas 150 por dia. Sirve para CUALQUIER
    --     consulta por rango de fecha, sin importar el estado.
    CREATE INDEX idx_cita_fecha_hora ON cita (fecha_hora);

    -- (b) La llave foranea NO crea indice sola en PostgreSQL. Sin este
    --     indice, "las mascotas de un dueno" recorre las 5.008 mascotas, y
    --     ademas cada DELETE de un dueno tendria que hacer lo mismo para
    --     comprobar la integridad referencial.
    CREATE INDEX idx_mascota_dueno ON mascota (id_dueno);

    -- (c) INDICE PARCIAL. Solo indexa las filas PROGRAMADA -- 18.187 de
    --     30.010, el 61 % -- porque la pantalla de agenda nunca pregunta por
    --     citas canceladas. Es mas pequeno que el indice completo y, como la
    --     condicion del indice YA garantiza el estado, el motor no tiene que
    --     volver a la tabla a verificarlo.
    CREATE INDEX idx_cita_programada_fecha
        ON cita (fecha_hora)
     WHERE estado = 'PROGRAMADA';

    -- =====================================================================
    -- PASO 3. ANALYZE. Crear el indice no actualiza las estadisticas: el
    -- planeador decide por costo estimado, y si sus numeros son viejos puede
    -- ignorar un indice perfectamente bueno. Este paso es la diferencia
    -- entre medir y adivinar.
    -- =====================================================================
    ANALYZE cita;
    ANALYZE mascota;

    -- =====================================================================
    -- PASO 4. LAS MISMAS DOS CONSULTAS, otra vez. Identicas al paso 1: si se
    -- cambia una coma, la comparacion deja de valer.
    -- =====================================================================
    EXPLAIN ANALYZE   -- C1 con indices
    SELECT id_cita, fecha_hora, estado
      FROM cita
     WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
       AND estado = 'PROGRAMADA';

    EXPLAIN ANALYZE   -- C2 con indices
    SELECT id_mascota, nombre, especie
      FROM mascota
     WHERE id_dueno = 1234;

    -- El enunciado pide comentar CUAL de los dos indices sobre fecha_hora
    -- eligio el planeador para C1, y la respuesta esperada es el PARCIAL:
    --   * idx_cita_programada_fecha recorre 91 entradas y ya sabe que todas
    --     cumplen estado = 'PROGRAMADA'.
    --   * idx_cita_fecha_hora recorreria 150 entradas -- las citas del dia en
    --     cualquier estado -- y tendria que descartar 59 despues de ir a la
    --     tabla a leer el estado.
    -- El parcial gana por menos entradas y por no tener que reverificar. Si en
    -- tu corrida gano el completo, la diferencia de costo es pequena: reporta
    -- lo que VISTE, no lo que dice esta linea.

    -- =====================================================================
    -- PASO 5. Inventario de lo creado. Es la prueba de que los tres indices
    -- existen con el nombre correcto y con la definicion correcta -- y en el
    -- caso del parcial, con su clausula WHERE.
    -- =====================================================================
    SELECT indexname, tablename, indexdef
      FROM pg_indexes
     WHERE tablename IN ('cita', 'mascota')
     ORDER BY tablename, indexname;

    -- =====================================================================
    -- Comprobacion de una linea, la que conviene pegar al calificar: cuantas
    -- filas indexa cada uno de los dos indices sobre fecha_hora.
    -- =====================================================================
    SELECT (SELECT COUNT(*) FROM cita)                                   AS indexa_el_completo,
           (SELECT COUNT(*) FROM cita WHERE estado = 'PROGRAMADA')       AS indexa_el_parcial,
           (SELECT COUNT(*) FROM cita
             WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
               AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00')        AS entradas_que_leeria_el_completo,
           (SELECT COUNT(*) FROM cita
             WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
               AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
               AND estado = 'PROGRAMADA')                                AS entradas_que_lee_el_parcial;
```

### Salida esperada

```
PASO 1 -- linea base, las dos con Seq Scan

    C1:  Seq Scan on cita  (cost=0.00..750.15 rows=90 width=20)
                           (actual time=... rows=91 loops=1)
           Filter: ((fecha_hora >= '2026-03-10 00:00:00'::timestamp)
                    AND (fecha_hora < '2026-03-11 00:00:00'::timestamp)
                    AND (estado = 'PROGRAMADA'::text))
           Rows Removed by Filter: 29919
         Execution Time: 12.8 ms

    C2:  Seq Scan on mascota  (actual time=... rows=2 loops=1)
           Filter: (id_dueno = 1234)
           Rows Removed by Filter: 5006
         Execution Time: 2.9 ms

    PASO 4 -- las mismas consultas despues de indexar y de ANALYZE

    C1:  Index Scan using idx_cita_programada_fecha on cita
             (cost=0.29..8.62 rows=90 width=20) (actual time=... rows=91 loops=1)
           Index Cond: ((fecha_hora >= '2026-03-10 00:00:00'::timestamp)
                        AND (fecha_hora < '2026-03-11 00:00:00'::timestamp))
         Execution Time: 0.4 ms

    C2:  Index Scan using idx_mascota_dueno on mascota
             (actual time=... rows=2 loops=1)
           Index Cond: (id_dueno = 1234)
         Execution Time: 0.1 ms

    Los cuatro hechos que hay que reconocer en esa salida:

    1. **Desaparecio el `Rows Removed by Filter`.** En C1 pasa de 29.919 a **nada**:
       el motor ya no lee las 30.010 filas para tirar 29.919, va directo a las 91.
       Esta es la diferencia con la Clase 6, donde el predicado sargable por si solo
       no habia conseguido esto. **El indice es lo que faltaba.**
    2. **`Index Cond` en vez de `Filter`.** No es un detalle de vocabulario: un
       `Index Cond` se resuelve **dentro** del indice, sin tocar la tabla; un `Filter`
       se evalua **despues** de leer la fila. Cuando un estudiante ve su condicion en
       `Filter`, el indice no le esta sirviendo para esa condicion.
    3. **El planeador eligio el indice PARCIAL para C1**, no el completo. Es la
       respuesta a la pregunta del enunciado. Tambien puede aparecer
       `Bitmap Index Scan` seguido de `Bitmap Heap Scan`: es igual de correcto, y
       significa que el motor prefirio recoger primero todas las direcciones de fila
       y ordenarlas antes de ir a la tabla.
    4. **`estado` ya no aparece en la condicion.** Con el indice parcial no hace
       falta: la definicion del indice garantiza que todo lo que hay dentro es
       `PROGRAMADA`. Eso es exactamente lo que lo hace mas barato que el completo.

    PASO 5 -- pg_indexes: **4 filas** (3 indices creados + la PK de cada tabla = 5;
    aqui se listan las de las dos tablas pedidas)

     indexname                  | tablename |  indexdef
    ----------------------------+-----------+------------------------------------------------
     cita_pkey                  | cita      | CREATE UNIQUE INDEX cita_pkey ON public.cita
                                |           |   USING btree (id_cita)
     idx_cita_fecha_hora        | cita      | CREATE INDEX idx_cita_fecha_hora ON public.cita
                                |           |   USING btree (fecha_hora)
     idx_cita_programada_fecha  | cita      | CREATE INDEX idx_cita_programada_fecha ON
                                |           |   public.cita USING btree (fecha_hora)
                                |           |   WHERE (estado = 'PROGRAMADA'::text)
     idx_mascota_dueno          | mascota   | CREATE INDEX idx_mascota_dueno ON public.mascota
                                |           |   USING btree (id_dueno)
     mascota_pkey               | mascota   | CREATE UNIQUE INDEX mascota_pkey ON
                                |           |   public.mascota USING btree (id_mascota)

    **Lo que hay que mirar en el `indexdef` del parcial es la clausula `WHERE`.** Si
    no esta, el estudiante creo un indice completo con nombre de parcial, y eso es lo
    que el enunciado penaliza de forma explicita.

    Comprobacion de una linea -- 1 fila

     indexa_el_completo | indexa_el_parcial | entradas_que_leeria_el_completo | entradas_que_lee_el_parcial
    --------------------+-------------------+---------------------------------+-----------------------------
                  30010 |             18187 |                             150 |                          91

    Ahi esta el argumento del indice parcial en cuatro numeros: es **39 % mas
    pequeno** (18.187 contra 30.010 entradas) y para la agenda del dia lee **91
    entradas en vez de 150**. Y ahi esta tambien su limite, que va en la pregunta 5:
    solo sirve cuando la consulta trae `estado = 'PROGRAMADA'`. La pantalla que
    muestre el historico completo de un dia va a usar el otro.

    **C2 devuelve 2 filas** —`(1241, Mascota 1233, Felino)` y
    `(3241, Mascota 3233, Felino)`—: 2 de 5.008, que es el caso ideal para un indice.
    Si alguien reporta 0 filas, casi siempre confundio `id_dueno` con `id_mascota`.
```

### Como calificar

- **6 pts — la linea base con `Seq Scan` en las dos consultas,** 3 pts cada una. Es el paso que la rubrica exige primero y el que mas se salta. El ancla verificable es el `Rows Removed by Filter: 29919` de C1: sin haber corrido el `EXPLAIN` antes de indexar, ese numero no se puede inventar.
- **9 pts — los tres indices con los nombres exactos, 3 pts cada uno.** El del parcial solo se da si el `indexdef` de `pg_indexes` muestra la clausula `WHERE estado = 'PROGRAMADA'`. Un indice completo con nombre de parcial vale 0 de esos 3: la rubrica descuenta «si falta el indice parcial», y aqui efectivamente falta.
- **3 pts — el `ANALYZE cita;` y el `ANALYZE mascota;` despues de crear los indices** y antes de volver a medir. No es burocracia: sin estadisticas frescas el planeador puede ignorar un indice bueno, y entonces el estudiante concluye lo contrario de lo que la clase quiere ensenar.
- **6 pts — los `EXPLAIN` posteriores evidencian `Index Scan` o `Bitmap Index Scan`** en C1 y en C2, 3 pts cada uno. Las dos formas valen igual. Lo que se verifica es que el nodo nombre el indice (`using idx_...`) y que la condicion aparezca como `Index Cond` y no como `Filter`.
- **3 pts — la consulta a `pg_indexes` lista los tres indices.** Con las PK salen 5 filas en total; se aceptan las 5 y tambien una version filtrada, siempre que los tres indices propios esten.
- **3 pts — el comentario sobre cual de los dos indices sobre `fecha_hora` eligio el planeador.** La rubrica lo pide de forma explicita y es el punto que separa a quien leyo el plan de quien lo pego. Se dan los 3 pts si el estudiante nombra el indice que **su** plan muestra y da una razon —normalmente el parcial, por tener menos entradas y no tener que reverificar el estado—. Si nombro el completo pero su plan dice el completo, valen igual los 3: se califica la lectura, no el resultado esperado.

### Errores frecuentes y que hacer

- **Crear los indices primero y medir despues, sin linea base.** Es el error estructural de esta pregunta: cuando se dan cuenta, ya no hay «antes» que medir. La salida es honesta y vale la pena ensenarla: `DROP INDEX idx_cita_fecha_hora, idx_cita_programada_fecha;`, medir, y volverlos a crear. Improvisar la linea base cuesta los 6 pts.
- **Crear el «parcial» sin la clausula `WHERE`.** Queda un segundo indice completo sobre `fecha_hora`, con nombre enganoso, que no aporta nada y que hay que mantener en cada `INSERT`. Es el peor de los mundos y se detecta en una linea, en el `indexdef`.
- **Poner el `WHERE` del indice parcial en el lugar equivocado:** `CREATE INDEX ... (fecha_hora WHERE estado = 'PROGRAMADA')` o `CREATE INDEX ... WHERE fecha_hora >= ...`. La sintaxis es `CREATE INDEX nombre ON tabla (columnas) WHERE condicion;` —la condicion va al final, sobre el indice completo, no dentro del parentesis—.
- **Omitir el `ANALYZE`** y concluir «el indice no sirvio porque el plan no cambio». Con 30.010 filas normalmente el plan si cambia sin `ANALYZE`, asi que el error suele quedar invisible aqui y aparecer despues en la pregunta 2. El habito que se ensena es el orden: crear, `ANALYZE`, medir.
- **Cambiar la consulta entre la medicion de antes y la de despues** —agregar un `ORDER BY`, quitar el filtro de estado, cambiar el dia—. Entonces se estan comparando dos cosas distintas y la evidencia no dice nada. Las dos consultas del enunciado se pegan **literalmente**, las dos veces.
- **Escribir «se uso el indice» sin nombrarlo.** El plan dice `Index Scan using idx_cita_programada_fecha`: el nombre esta ahi y es gratis. La devolucion util es pedir esa palabra, porque es la que obliga a mirar el plan de verdad y la que hace falta en la tabla de la pregunta 5.

---

## Pregunta 2 · Orden de columnas en un indice compuesto · 20 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- PASO 1. Los dos indices compuestos con las MISMAS dos columnas y en
    -- orden invertido. Todo el experimento consiste en que el planeador
    -- elija, y en ver cual elige para cada consulta.
    -- =====================================================================
    CREATE INDEX idx_cita_estado_fecha ON cita (estado, fecha_hora);
    CREATE INDEX idx_cita_fecha_estado ON cita (fecha_hora, estado);
    ANALYZE cita;

    -- =====================================================================
    -- PASO 2. Las tres consultas. Cada una esta disenada para que gane un
    -- indice distinto (o ninguno).
    -- =====================================================================

    -- Q1: igualdad en estado + rango en fecha_hora. Es el caso de libro.
    EXPLAIN ANALYZE
    SELECT id_cita, fecha_hora
      FROM cita
     WHERE estado = 'PROGRAMADA'
       AND fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00';
    -- Esperado: Index Scan using idx_cita_estado_fecha.
    -- Por que: con (estado, fecha_hora) el motor fija estado = 'PROGRAMADA' y
    -- dentro de ese bloque las entradas ya vienen ordenadas por fecha_hora,
    -- asi que lee un tramo CONTIGUO de exactamente 91 entradas y para.
    -- Con (fecha_hora, estado) tendria que leer las 150 del dia y descartar 59.

    -- Q2: solo rango de fecha. estado no aparece en el WHERE.
    EXPLAIN ANALYZE
    SELECT id_cita, fecha_hora
      FROM cita
     WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00';
    -- Esperado: Index Scan using idx_cita_fecha_estado.
    -- Por que: fecha_hora es la columna LIDER, asi que el rango es un tramo
    -- contiguo del indice: 150 entradas. El otro indice esta ordenado primero
    -- por estado, de modo que las citas del 10 de marzo estan repartidas en
    -- TRES tramos distintos y ninguno se puede localizar sin recorrer todo.

    -- Q3: solo estado, que tiene 3 valores y donde PROGRAMADA es el 61 %.
    EXPLAIN ANALYZE
    SELECT COUNT(*) FROM cita WHERE estado = 'PROGRAMADA';
    -- Esperado: Seq Scan on cita (dentro de un nodo Aggregate).
    -- Por que: hay que tocar 18.187 de 30.010 filas. Leer el 61 % de la tabla
    -- brincando por un indice sale MAS CARO que recorrerla de corrido, porque
    -- el recorrido secuencial va en orden fisico. Un indice sobre una columna
    -- de baja cardinalidad casi nunca se usa, y esta es la demostracion.
    -- (Si aparece un Index Only Scan, tambien es correcto: como COUNT(*) no
    --  necesita mas columnas, el motor puede resolverlo dentro del indice
    --  siempre que el mapa de visibilidad este al dia. La conclusion no
    --  cambia: no vale la pena crear ese indice solo para esto.)

    -- =====================================================================
    -- PASO 3. El experimento forzado: se le quita al motor el indice que
    -- estaba usando para Q2 y se ve que hace.
    -- =====================================================================
    DROP INDEX idx_cita_fecha_estado;
    ANALYZE cita;

    EXPLAIN ANALYZE     -- Q2 otra vez, identica
    SELECT id_cita, fecha_hora
      FROM cita
     WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00';
    -- Resultado: vuelve el Seq Scan con Rows Removed by Filter: 29860,
    -- que son las 30.010 filas menos las 150 del dia.
    -- El indice idx_cita_estado_fecha SIGUE EXISTIENDO y contiene fecha_hora,
    -- pero el motor prefiere no usarlo. La razon es la estructura del arbol:
    -- solo se puede entrar por la columna lider. Como estado no esta en el
    -- WHERE, para encontrar las citas del 10 de marzo habria que recorrer el
    -- indice COMPLETO -- las 30.010 entradas -- y ademas ir a la tabla por
    -- cada candidata, porque id_cita no esta en el indice. Sale mas caro que
    -- el Seq Scan, y el planeador lo calcula asi.

    -- =====================================================================
    -- Comprobacion de una linea: los tres numeros que sostienen las tres
    -- conclusiones de arriba.
    -- =====================================================================
    SELECT (SELECT COUNT(*) FROM cita)                                  AS filas_totales,
           (SELECT COUNT(*) FROM cita WHERE estado = 'PROGRAMADA')      AS q3_toca_el_61_por_ciento,
           (SELECT COUNT(*) FROM cita
             WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
               AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00')       AS q2_lee_150,
           (SELECT COUNT(*) FROM cita
             WHERE estado = 'PROGRAMADA'
               AND fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
               AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00')       AS q1_lee_91;

    -- =====================================================================
    -- CONCLUSION: en un indice compuesto va PRIMERO la columna de IGUALDAD y
    -- DESPUES la de RANGO, porque el motor puede fijar la igualdad y luego
    -- recorrer un tramo contiguo; al reves, el rango abre el abanico y la
    -- segunda columna ya no acota nada, solo filtra.
    -- CONCLUSION (2): un indice cuya columna lider no aparece en el WHERE
    -- normalmente queda sin usar, porque a un arbol B solo se entra por la
    -- izquierda. Corolario practico: (estado, fecha_hora) NO reemplaza a
    -- (fecha_hora), pero (fecha_hora, estado) SI reemplaza a (fecha_hora) --
    -- por eso dos indices bien ordenados suelen bastar donde alguien queria
    -- cuatro.
```

### Salida esperada

```
PASO 2 -- que indice eligio cada consulta

    Q1  (igualdad + rango) -- 91 filas
        Index Scan using idx_cita_estado_fecha on cita
            (actual time=... rows=91 loops=1)
          Index Cond: ((estado = 'PROGRAMADA'::text)
                       AND (fecha_hora >= '2026-03-10 00:00:00'::timestamp)
                       AND (fecha_hora < '2026-03-11 00:00:00'::timestamp))
        Execution Time: 0.4 ms
        --> LAS DOS condiciones estan en Index Cond. Eso es lo que significa que
            el orden de columnas es el correcto: el indice resuelve todo.

    Q2  (solo rango) -- 150 filas
        Index Scan using idx_cita_fecha_estado on cita
            (actual time=... rows=150 loops=1)
          Index Cond: ((fecha_hora >= '2026-03-10 00:00:00'::timestamp)
                       AND (fecha_hora < '2026-03-11 00:00:00'::timestamp))
        Execution Time: 0.5 ms
        --> Eligio el OTRO indice. Con las mismas dos columnas. Solo cambia el orden.

    Q3  (solo estado, 61 % de la tabla) -- 1 fila: 18187
        Aggregate  (actual time=... rows=1 loops=1)
          ->  Seq Scan on cita  (actual time=... rows=18187 loops=1)
                Filter: (estado = 'PROGRAMADA'::text)
                Rows Removed by Filter: 11823
        Execution Time: 9.6 ms
        --> NINGUN indice, teniendo dos disponibles que empiezan por estado.
            No es un error del motor: es la respuesta correcta. Tambien puede
            aparecer un Index Only Scan usando idx_cita_estado_fecha, y sirve
            igual para la conclusion.

    PASO 3 -- Q2 despues del DROP INDEX idx_cita_fecha_estado

        Seq Scan on cita  (actual time=... rows=150 loops=1)
          Filter: ((fecha_hora >= '2026-03-10 00:00:00'::timestamp)
                   AND (fecha_hora < '2026-03-11 00:00:00'::timestamp))
          Rows Removed by Filter: 29860
        Execution Time: 11.4 ms
        --> **Este es el resultado de la pregunta.** El indice
            idx_cita_estado_fecha sigue existiendo y CONTIENE fecha_hora, y aun
            asi el motor volvio al recorrido completo: de 0,5 ms a 11,4 ms, unas
            20 veces mas lento. La columna lider es la puerta de entrada al
            indice, y si no esta en el WHERE, el indice esta cerrado.

    Comprobacion de una linea -- 1 fila

     filas_totales | q3_toca_el_61_por_ciento | q2_lee_150 | q1_lee_91
    ---------------+--------------------------+------------+-----------
             30010 |                    18187 |        150 |        91

    Los tres numeros explican las tres decisiones del planeador sin necesidad de
    teoria: 91 de 30.010 (0,3 %) es un caso ideal para un indice; 150 de 30.010
    (0,5 %) tambien; **18.187 de 30.010 (61 %) no lo es**, y por eso Q3 recorre la
    tabla. La regla de bolsillo que se puede dar en clase: por debajo de un 5 % a un
    10 % de la tabla el indice suele ganar; por encima de un tercio, casi nunca.
```

### Como calificar

- **4 pts — los dos indices compuestos creados con los nombres exactos** y el `ANALYZE cita;` de por medio, 2 pts cada indice. Sin `ANALYZE` el experimento se vuelve ruido y el resto de la pregunta puede salir al reves.
- **6 pts — los tres `EXPLAIN` con el indice elegido identificado, 2 pts cada uno.** La rubrica pide **identificar**, no solo ejecutar: hay que nombrar `idx_cita_estado_fecha` en Q1, `idx_cita_fecha_estado` en Q2 y decir que Q3 **no uso ninguno** —o que uso un `Index Only Scan`, que vale igual—. El punto de Q3 se da solo si el estudiante explica **por que** el motor no quiso el indice, no solo que no lo uso.
- **5 pts — el `DROP INDEX` y la nueva medicion de Q2, comparada.** 3 pts que el experimento este completo —`DROP`, volver a medir, y la misma consulta sin cambiar— y 2 pts la comparacion explicita con el numero: volvio el `Seq Scan` con `Rows Removed by Filter: 29860`. Ese numero es el ancla que no se puede adivinar.
- **5 pts — la linea `-- CONCLUSION:`.** 3 pts enunciar bien la regla **igualdad antes de rango** y 2 pts explicar por que un indice cuya columna lider no esta en el filtro suele quedar sin usar. La rubrica acepta como matiz correcto que ese indice todavia pueda servir para un barrido completo tipo `Index Only Scan`, y quien lo mencione muestra que entendio el mecanismo, no la formula.
- **Se reconoce como sobresaliente, sin puntos extra:** el corolario que casi nadie escribe y que es el mas util en el trabajo —`(fecha_hora, estado)` **si** hace innecesario un indice suelto sobre `(fecha_hora)`, pero `(estado, fecha_hora)` **no**—. Es la razon por la que dos indices bien ordenados suelen reemplazar a cuatro, y conecta directo con la pregunta 4.
- **No se califican los milisegundos**, sino los conteos de filas y el nodo elegido. Si un estudiante reporta que Q2 quedo mas rapida despues del `DROP`, casi siempre esta comparando una corrida en frio contra una en caliente: la devolucion es que alterne y repita.

### Errores frecuentes y que hacer

- **Concluir que «los dos indices sirven igual porque tienen las mismas columnas».** Es exactamente la intuicion que la pregunta existe para romper, y se rompe con la propia evidencia del estudiante: Q1 eligio uno, Q2 eligio el otro, y tras el `DROP` Q2 se quedo sin ninguno. El orden no es un detalle de estilo, es la estructura del arbol.
- **Interpretar Q3 como un fallo.** «El motor no uso mi indice» no es un error del motor ni del indice: tocar el 61 % de la tabla brincando por un indice es mas caro que recorrerla en orden fisico. Es la evidencia experimental de la opcion falsa de la pregunta 4, y conviene senalar esa conexion en la devolucion.
- **Cambiar Q2 despues del `DROP`** —agregar un `ORDER BY`, quitar una de las dos cotas del rango, mover el dia—. El experimento consiste en variar **una sola cosa**: el indice disponible. Si tambien cambia la consulta, no hay conclusion posible.
- **Confundir el orden del indice con el orden del `WHERE`.** El orden en que se escriben las condiciones en el `WHERE` es irrelevante: el planeador las reordena. Lo que importa es el orden de las columnas **en la definicion del indice**. Vale la pena demostrarlo en vivo invirtiendo las dos lineas del `WHERE` de Q1: el plan sale identico.
- **Creer que la conclusion es «siempre poner la fecha primero»** o «siempre poner el estado primero». La regla no es sobre columnas concretas, es sobre **el tipo de comparacion**: igualdad primero, rango despues. Se comprueba leyendo Q1 y Q2 juntas: la misma columna gana o pierde el primer puesto segun como se la compare.
- **Olvidar el `ANALYZE` despues del `DROP INDEX`.** No cambia el resultado en esta base, pero mantiene el habito de la pregunta 1 y evita explicaciones raras cuando un plan no coincide con lo esperado.

---

## Pregunta 3 · Particionar el historico de citas por rango de fecha · 20 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- OJO: esta pregunta corre sobre OTRA base. Aqui hay 5.010 citas
    -- repartidas entre enero de 2025 y diciembre de 2026, no las 30.010 de
    -- las preguntas 1 y 2. Los numeros no se mezclan.
    -- =====================================================================

    -- =====================================================================
    -- PASO 1. La tabla padre particionada. NO tiene datos propios: es solo la
    -- definicion de la estructura y la regla de enrutamiento.
    -- =====================================================================
    CREATE TABLE cita_hist (
      id_cita         INT,
      id_mascota      INT,
      id_veterinario  INT,
      fecha_hora      TIMESTAMP NOT NULL,
      estado          TEXT,
      -- La PK TIENE que incluir la columna de particion. La razon es
      -- estructural: PostgreSQL implementa la unicidad con un indice por
      -- particion, y no puede garantizar que un id_cita no se repita entre
      -- dos particiones distintas si no sabe en cual buscar. Con id_cita solo
      -- falla con:
      --   "unique constraint on partitioned table must include all
      --    partitioning columns"
      PRIMARY KEY (id_cita, fecha_hora)
    ) PARTITION BY RANGE (fecha_hora);

    -- =====================================================================
    -- PASO 2. Las dos particiones. El limite inferior es INCLUSIVO y el
    -- superior EXCLUSIVO -- FROM ... TO ... --, y por eso 2026-01-01 aparece
    -- en las dos lineas sin que haya solape: cierra 2025 y abre 2026. Es la
    -- misma logica del predicado de rango de la Clase 6.
    -- =====================================================================
    CREATE TABLE cita_hist_2025 PARTITION OF cita_hist
        FOR VALUES FROM (TIMESTAMP '2025-01-01') TO (TIMESTAMP '2026-01-01');

    CREATE TABLE cita_hist_2026 PARTITION OF cita_hist
        FOR VALUES FROM (TIMESTAMP '2026-01-01') TO (TIMESTAMP '2027-01-01');

    -- =====================================================================
    -- PASO 3. Migracion. Se inserta en la tabla PADRE y PostgreSQL enruta
    -- cada fila a su particion segun fecha_hora. No hace falta ningun
    -- trigger ni ningun CASE: el enrutamiento es del motor.
    -- =====================================================================
    INSERT INTO cita_hist
    SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado FROM cita;

    ANALYZE cita_hist;    -- para que la poda del PASO 5 se vea con numeros reales

    -- =====================================================================
    -- PASO 4. Prueba del enrutamiento. tableoid es una columna de sistema que
    -- dice de que tabla FISICA salio cada fila; el cast ::regclass la
    -- convierte en el nombre. Es la unica forma limpia de demostrar el
    -- reparto sin consultar cada particion por separado.
    -- =====================================================================
    SELECT tableoid::regclass AS particion,
           COUNT(*),
           MIN(fecha_hora),
           MAX(fecha_hora)
      FROM cita_hist
     GROUP BY 1
     ORDER BY 1;

    -- =====================================================================
    -- PASO 5. Prueba de la PODA DE PARTICIONES. En el plan solo debe aparecer
    -- cita_hist_2026: la particion de 2025 no se lee, no se abre, no existe
    -- para esta consulta.
    -- =====================================================================
    EXPLAIN ANALYZE
    SELECT COUNT(*) FROM cita_hist
     WHERE fecha_hora >= TIMESTAMP '2026-01-01'
       AND fecha_hora <  TIMESTAMP '2027-01-01';

    -- Contraprueba util: sin filtro por fecha_hora no hay nada que podar y el
    -- plan tiene que mostrar las DOS particiones bajo un nodo Append.
    EXPLAIN ANALYZE
    SELECT COUNT(*) FROM cita_hist;

    -- Y la trampa que conviene mostrar: si el filtro se envuelve en una
    -- funcion, se pierde la poda igual que se perdia el indice en la Clase 6.
    -- Aqui vuelven a aparecer las dos particiones.
    EXPLAIN ANALYZE
    SELECT COUNT(*) FROM cita_hist
     WHERE EXTRACT(YEAR FROM fecha_hora) = 2026;

    -- =====================================================================
    -- PASO 6. Comprobacion de que no se perdio ni se duplico nada en la
    -- migracion.
    -- =====================================================================
    SELECT (SELECT COUNT(*) FROM cita)      AS origen,
           (SELECT COUNT(*) FROM cita_hist) AS destino,
           (SELECT COUNT(*) FROM cita) - (SELECT COUNT(*) FROM cita_hist) AS debe_ser_cero;

    -- =====================================================================
    -- La operacion de mantenimiento que se vuelve trivial:
    --
    --   DROP TABLE cita_hist_2025;   -- archivar el ano completo
    --
    -- Eso libera las 2.620 filas de 2025 en una operacion de METADATOS: el
    -- motor desengancha el archivo y lo borra. Es practicamente instantaneo,
    -- no genera WAL por fila, no deja filas muertas y no necesita VACUUM.
    --
    -- El equivalente sin particiones seria
    --   DELETE FROM cita WHERE fecha_hora < TIMESTAMP '2026-01-01';
    -- que recorre la tabla, escribe 2.620 registros en el WAL, deja 2.620
    -- filas muertas que hay que aspirar despues, mantiene todos los indices
    -- durante el borrado y NO devuelve el espacio al sistema sin un
    -- VACUUM FULL -- que bloquea la tabla entera --. Con 2.620 filas la
    -- diferencia es un detalle; con dos anos de historia real de Huellitas,
    -- es la diferencia entre un segundo y una ventana de mantenimiento.
    --
    -- Variante que se usa de verdad cuando la ley obliga a conservar el dato:
    --   ALTER TABLE cita_hist DETACH PARTITION cita_hist_2025;
    -- deja la tabla intacta pero fuera del conjunto consultado, lista para
    -- respaldarla con el pg_dump de la Clase 4 y despues borrarla.
    -- =====================================================================
```

### Salida esperada

```
PASO 4 -- enrutamiento: 2 filas

        particion    | count |         min         |         max
    -----------------+-------+---------------------+---------------------
     cita_hist_2025  |  2620 | 2025-01-06 08:00:00 | 2025-12-31 15:00:00
     cita_hist_2026  |  2390 | 2026-01-01 08:00:00 | 2026-12-06 15:00:00

    **2.620 + 2.390 = 5.010.** Son los dos numeros de la pregunta y los que hay que
    buscar al calificar. Tres cosas se leen de esta tabla sola:

    - **Los rangos no se solapan y encajan sin hueco:** 2025 termina el 31 de
      diciembre y 2026 empieza el 1 de enero. Eso es lo que consigue el limite
      superior **exclusivo** de `FROM ... TO ...`.
    - **2026 tiene 2.390 y no 2.380** porque ademas de las citas sintetizadas se
      lleva las **10 citas sembradas a mano** de septiembre de 2026 —las de
      Firulais, Luna y compania—.
    - **El reparto es desigual a proposito** (2.620 contra 2.390): la historia
      sintetica arranca el 6 de enero de 2025 y termina el 6 de diciembre de 2026,
      asi que 2025 esta completo y 2026 le faltan tres semanas y media.

    PASO 5 -- poda de particiones

    Consulta con filtro de 2026 -- 1 fila: 2390

        Aggregate  (actual time=... rows=1 loops=1)
          ->  Seq Scan on cita_hist_2026 cita_hist  (actual rows=2390 loops=1)
                Filter: ((fecha_hora >= '2026-01-01 00:00:00'::timestamp)
                         AND (fecha_hora < '2027-01-01 00:00:00'::timestamp))
        Execution Time: 1.2 ms

    **`cita_hist_2025` no aparece en ninguna parte del plan.** Eso es la poda, y es
    lo que la pregunta pide demostrar. Con una sola particula en el plan puede que ni
    siquiera salga el nodo `Append`: cuando queda una sola relacion, el motor lo
    elimina.

    Contraprueba, sin filtro -- 1 fila: 5010

        Aggregate
          ->  Append  (actual rows=5010 loops=1)
                ->  Seq Scan on cita_hist_2025 cita_hist_1  (actual rows=2620 loops=1)
                ->  Seq Scan on cita_hist_2026 cita_hist_2  (actual rows=2390 loops=1)

    Aqui **si** aparecen las dos, bajo un `Append`. Tener las dos salidas al lado es
    lo que convierte «se podo» en evidencia: sin la contraprueba no se sabe si la
    particion de 2025 falto por la poda o porque nunca hubo nada dentro.

    Con `EXTRACT(YEAR FROM fecha_hora) = 2026` -- 1 fila: 2390, pero:

        Aggregate
          ->  Append  (actual rows=2390 loops=1)
                ->  Seq Scan on cita_hist_2025 ...  (actual rows=0 loops=1)
                      Filter: (EXTRACT(year FROM fecha_hora) = 2026)
                      Rows Removed by Filter: 2620
                ->  Seq Scan on cita_hist_2026 ...  (actual rows=2390 loops=1)

    **El resultado es correcto y la poda se perdio.** Las dos particiones se leen y
    2025 aporta 0 filas despues de descartar 2.620. Es la misma leccion de la
    Clase 6 en otro escenario: envolver la columna en una funcion le quita al motor
    la informacion que necesita para decidir, y aqui lo que pierde no es un indice,
    es una particion entera. Vale la pena mostrar esta salida en clase.

    PASO 6 -- integridad de la migracion: 1 fila

     origen | destino | debe_ser_cero
    --------+---------+---------------
       5010 |    5010 |             0
```

### Como calificar

- **5 pts — `cita_hist` bien creada.** 3 pts el `PARTITION BY RANGE (fecha_hora)` y 2 pts la `PRIMARY KEY (id_cita, fecha_hora)`. Si el estudiante intento `PRIMARY KEY (id_cita)` y el motor lo rechazo, y despues lo corrigio, se dan los 2 pts completos: el mensaje de error es la mejor explicacion de por que la llave tiene que incluir la columna de particion.
- **4 pts — las dos particiones cubren 2025 y 2026 sin solaparse,** 2 pts cada una. Se verifica en el `MIN`/`MAX` del paso 4: 2025 cierra el 31 de diciembre y 2026 abre el 1 de enero. Un solape se detecta al instante porque el `CREATE TABLE` falla —el motor no lo permite—, asi que el error real que aparece es el hueco.
- **4 pts — la migracion inserta las 5.010 filas.** 2 pts que el `INSERT` vaya contra la tabla **padre** —insertar directo en cada particion con un `WHERE` por ano funciona pero se salta lo que se queria ensenar: vale 1 de esos 2— y 2 pts que el conteo cuadre.
- **4 pts — el `tableoid::regclass` evidencia el reparto con 2.620 / 2.390.** 2 pts la consulta y 2 pts que los numeros sean los correctos y con rangos que no se solapan.
- **3 pts — el `EXPLAIN` muestra la poda: solo `cita_hist_2026`.** Se dan los 3 pts con la salida de la poda; se anota como sobresaliente —sin puntos extra— quien haya agregado la **contraprueba sin filtro**, porque es lo que distingue «se podo» de «esa particion estaba vacia».
- **Los 20 pts no cierran sin el comentario final del paso 6:** identificar que lo que se vuelve trivial es **archivar o eliminar un ano completo** con un `DROP TABLE` de la particion en vez de un `DELETE` masivo. Es un requisito explicito de la rubrica y se reparte dentro de los puntos anteriores; una entrega que hace todo el SQL y omite el comentario pierde 3 pts sobre el bloque de la poda.

### Errores frecuentes y que hacer

- **`PRIMARY KEY (id_cita)` a secas.** Falla con «unique constraint on partitioned table must include all partitioning columns». No es una arbitrariedad: la unicidad se implementa con un indice **por particion**, y sin la columna de particion el motor no sabria en cual buscar para garantizarla. Es el error de arranque mas comun y el que mejor se explica solo.
- **Rangos que dejan un hueco:** `TO ('2025-12-31')` en vez de `TO ('2026-01-01')`. El `INSERT` falla con «no partition of relation cita_hist found for row» y el estudiante suele culpar a la migracion. El limite superior es **exclusivo**, asi que la fecha de corte se repite en las dos particiones: cierra una y abre la otra.
- **Insertar en cada particion por separado** con un `WHERE` por ano. Da el resultado correcto y demuestra lo contrario de lo que se pedia: el punto es que el **motor** enruta. Ademas es el habito que rompe el sistema el dia que llegue una fila de 2027 y nadie recuerde que hay que insertar a mano.
- **Confundir particionamiento con indices.** Aparece como «cree la particion para que la consulta use el indice». Son dos mecanismos distintos: el indice encuentra filas dentro de una tabla, la particion decide **que tablas ni siquiera se abren**. Se pueden combinar —y en produccion se combinan—, pero no se sustituyen.
- **Filtrar con `EXTRACT(YEAR FROM fecha_hora) = 2026` y afirmar que hubo poda.** El resultado es correcto —2.390— y en el plan aparecen **las dos** particiones. Es exactamente el antipatron de la Clase 6 reapareciendo: si el estudiante lo cometio, no hay que corregirselo sin mas, hay que hacerle comparar los dos planes.
- **Concluir que particionar «hizo la consulta mas rapida».** Con 5.010 filas **no** hay ganancia de rendimiento apreciable, y el propio enunciado lo dice. Lo demostrado aqui es sintaxis, enrutamiento, poda en el plan y facilidad de archivado. Quien reporte una mejora de velocidad esta midiendo ruido, y esa distincion es la que la pregunta 5 califica de frente.

---

## Pregunta 4 · Riesgos de sobre-indexar VetCare · 10 pts

### Clave y por que

La clave se lee del banco de la plataforma, asi que esta es la que se califica. La columna de la derecha es lo que hay que poder responderle al estudiante cuando pregunte.

|  | Opcion | Por que |
|---|---|---|
| **SI** | Cada indice adicional encarece INSERT, UPDATE y DELETE, porque el motor debe mantenerlo sincronizado con la tabla. | **Correcta, y es el costo que nadie ve porque no aparece en ningun `EXPLAIN` de `SELECT`.** Un indice es una estructura **separada** de la tabla y el motor tiene que mantenerla sincronizada: cada `INSERT` escribe una entrada en cada indice, cada `UPDATE` de una columna indexada borra la vieja y escribe la nueva, cada `DELETE` marca las suyas. En VetCare eso pesa sobre `sp_agendar_cita` y `sp_registrar_consulta`, que son las dos operaciones con alguien esperando en el mostrador. Indexar «cada columna» de `cita` significa multiplicar por cinco o seis el trabajo de escritura de la operacion mas sensible del sistema. |
| no | Un indice sobre una columna de baja cardinalidad como estado, con solo 3 valores posibles, es siempre la mejor inversion. | **Incorrecta, y esta demostrada experimentalmente en la pregunta 2.** `estado` tiene 3 valores y `PROGRAMADA` es el 61 % de las 30.010 filas: Q3 recorrio la tabla completa **teniendo dos indices disponibles que empiezan por `estado`**. Leer el 61 % de una tabla brincando por un indice es mas caro que recorrerla en orden fisico, y el planeador lo calcula asi. La palabra que delata la opcion es **«siempre»**: la excepcion existe —un valor raro dentro de una columna de baja cardinalidad, o el indice **parcial** de la opcion siguiente—, pero eso ya no es «indexar la columna `estado`». |
| **SI** | Los indices ocupan espacio en disco y en memoria cache, compitiendo con los datos que si se consultan. | **Correcta, y es el costo que se paga incluso cuando el indice no se usa.** Ocupa disco, pero sobre todo compite por la **cache**: el motor tiene una cantidad fija de memoria para paginas, y cada pagina de indice muerto que entra ahi expulsa una pagina de datos que si se estaba consultando. Ademas engorda los respaldos de la Clase 4 y alarga cada restauracion, porque los indices se **reconstruyen** al restaurar. Un indice inutil no es neutro: cobra sin dar nada. |
| **SI** | Un indice parcial (WHERE estado = 'PROGRAMADA') puede dar el mismo beneficio que uno completo ocupando una fraccion del tamano, cuando las consultas siempre traen ese filtro. | **Correcta, y es la del indice que se creo en la pregunta 1.** `idx_cita_programada_fecha` indexa 18.187 entradas en vez de 30.010 —un 39 % menos— y para la agenda del dia lee 91 en vez de 150, porque su propia definicion ya garantiza el estado y no hay que reverificarlo. La condicion esta en la ultima frase de la opcion y es la que hay que subrayar: **«cuando las consultas siempre traen ese filtro»**. Una pantalla que muestre el historico completo de un dia no puede usar este indice, y para eso queda el completo. |
| no | Como las FOREIGN KEY crean su indice automaticamente en PostgreSQL, indexar id_dueno en mascota es redundante. | **Incorrecta, y es la mas peligrosa de las seis porque suena a dato tecnico.** PostgreSQL crea un indice automatico para una `PRIMARY KEY` y para un `UNIQUE`, pero **no** para una `FOREIGN KEY`. Sin `idx_mascota_dueno`, «las mascotas de un dueno» recorre las 5.008 mascotas —lo midio la pregunta 1— y ademas cada `DELETE` o `UPDATE` de un `dueno` tiene que hacer ese mismo recorrido para comprobar la integridad referencial. Indexar el lado **hijo** de una llave foranea es una de las poquisimas indexaciones que se pueden dar por buenas casi sin medir. |
| **SI** | Antes de crear un indice hay que tener la consulta concreta que lo va a usar y medir con EXPLAIN; indexar por intuicion produce indices muertos. | **Correcta, y es la regla de trabajo que la pregunta 5 pide adoptar por escrito.** Un indice se justifica con una **consulta concreta** y con la **evidencia** de que el planeador lo eligio, no con una intuicion sobre lo que alguien podria buscar algun dia. Los indices creados por intuicion acaban siendo indices muertos: cobran escritura, cache y espacio de respaldo, y no aparecen en ningun plan. Es literalmente lo que hace la propuesta que abre la pregunta —«un indice sobre cada columna, por si acaso»—, y por eso las dos opciones correctas de este par, la 0 y la 5, son las dos caras del mismo argumento. |

### Como calificar

- **10 pts con las 4 correctas marcadas y ninguna incorrecta**, con puntaje proporcional por acierto parcial, tal como dice la rubrica. La clave se lee del banco de la plataforma.
- **La opcion de la `FOREIGN KEY` es el discriminador tecnico de la pregunta.** Se corrige con un dato, no con una opinion: `pg_indexes` de la pregunta 1 lista `mascota_pkey` y `idx_mascota_dueno`, y **no** hay ningun indice que el motor haya creado solo para la llave foranea. Si mas de un tercio del grupo la marca, vale la pena volver a proyectar esa salida.
- **La opcion de la baja cardinalidad ya esta refutada por su propia evidencia.** Quien la marque tiene en su pregunta 2 un `Seq Scan` en Q3 teniendo dos indices que empiezan por `estado`. Es la devolucion mas eficaz que existe: su experimento contradice su respuesta.
- Si alguien argumenta que un indice sobre `estado` **si** podria servir para buscar `CANCELADA` —2.728 filas, el 9 %—, tiene razon y conviene decirlo: la opcion es falsa por la palabra «siempre» y por «la mejor inversion», no porque un indice de baja cardinalidad sea inutil en todos los casos. Ese matiz es justamente el que hace valiosa la opcion del indice **parcial**.

### Errores frecuentes y que hacer

- **Marcar la de la `FOREIGN KEY`.** Es una confusion muy extendida, probablemente por analogia con la `PRIMARY KEY` —que si crea indice— y por motores donde el comportamiento es distinto. En PostgreSQL el lado hijo de una llave foranea queda sin indexar, y es una de las causas mas frecuentes de lentitud inexplicada en bases que «ya tienen sus llaves».
- **Marcar la de la baja cardinalidad,** normalmente por leer «`estado` se usa en muchas consultas» y concluir que hay que indexarlo. Lo que decide no es cuantas veces aparece la columna, es **que fraccion de la tabla devuelve el filtro**. La regla de bolsillo: por debajo del 5–10 %, el indice suele ganar; por encima de un tercio, casi nunca.
- **No marcar la del espacio y la cache,** por pensar que «el disco es barato». El disco es barato; la memoria de cache y la ventana de restauracion, no. Un indice muerto expulsa paginas de datos utiles de la cache y alarga cada restauracion, porque al restaurar los indices se reconstruyen —eso conecta directo con el ensayo de restauracion de la Clase 4—.
- **Marcar las seis** o marcar solo la primera. Suele significar que la pregunta se contesto antes de haber hecho las tres primeras. Las cuatro correctas estan todas demostradas en el propio taller: la del parcial en la pregunta 1, la de la cardinalidad y su contraria en la pregunta 2, y la de medir antes de crear en la pregunta 5.

---

## Pregunta 5 · Tabla de justificacion consulta -> indice · 20 pts

### Respuesta esperada

| Indice | Tabla y columnas | Consulta del PI que lo usa | Cardinalidad de la lider | Evidencia en EXPLAIN | Costo de mantenimiento | Veredicto |
|---|---|---|---|---|---|---|
| `idx_cita_programada_fecha` | `cita (fecha_hora)` **parcial** `WHERE estado = 'PROGRAMADA'` | Agenda del dia: citas PROGRAMADA de una fecha. ~60-80 ejecuciones por jornada, con alguien esperando en el mostrador | **Alta.** `fecha_hora` tiene ~30.000 valores distintos en 200 dias; el indice cubre 18.187 de 30.010 filas (61 %) | `Index Scan using idx_cita_programada_fecha`, `Index Cond` sobre el rango, **91 filas y `Rows Removed by Filter` desaparecido** (era 29.919). 12,8 ms → 0,4 ms | Una entrada por cada cita PROGRAMADA que agende `sp_agendar_cita`. Al pasar a ATENDIDA, la entrada **sale** del indice: el parcial se mantiene solo | **Se queda.** Es el indice mejor justificado del proyecto |
| `idx_cita_fecha_hora` | `cita (fecha_hora)` | Historico del dia y reportes por rango de fechas, **sin** filtro de estado (cierre de caja, citas canceladas del mes) | **Alta.** La misma columna, pero cubriendo las 30.010 filas | En la agenda del dia el planeador prefirio el parcial. Para la consulta sin filtro de estado si es el elegido: 150 filas por `Index Cond` | Una entrada por **cada** cita, en todo `INSERT` y en todo `UPDATE` de `fecha_hora` (reprogramaciones) | **Se queda, pero es el primer candidato a revisar.** Si en el semestre ninguna consulta por rango sin filtro de estado aparece de verdad, se descarta y queda solo el parcial |
| `idx_mascota_dueno` | `mascota (id_dueno)` | Ficha del dueno: sus mascotas. Se abre en cada atencion, antes de agendar | **Alta.** 2.006 duenos para 5.008 mascotas, ~2,5 mascotas por dueno | `Index Scan using idx_mascota_dueno`, `Index Cond: (id_dueno = 1234)`, **2 filas de 5.008**. 2,9 ms → 0,1 ms | Bajo: `mascota` casi no cambia —una mascota se registra una vez—. Ademas **ahorra** trabajo en cada `DELETE`/`UPDATE` de `dueno`, que sin el recorre las 5.008 mascotas para verificar la llave foranea | **Se queda.** Lado hijo de una llave foranea: es el caso que se puede dar por bueno casi sin medir |
| `idx_cita_estado_fecha` | `cita (estado, fecha_hora)` | La misma agenda del dia, escrita con la igualdad explicita. Creado en la pregunta 2 para el experimento del orden | **Baja en la lider.** `estado` tiene solo 3 valores y `PROGRAMADA` es el 61 % de la tabla | `Index Scan using idx_cita_estado_fecha` en Q1, con **las dos** condiciones en `Index Cond` (91 filas). Pero en Q2 —solo rango— y en Q3 —solo estado— el motor **no lo uso** | Una entrada por cada cita, y la entrada se **reescribe** en cada cambio de estado porque `estado` es la columna lider | **Se cambia por el parcial.** Cubre el mismo caso de uso, es mas pequeno y no se reescribe en cada cambio de estado. Mantener los dos es sobre-indexar |
| `idx_cita_fecha_estado` | `cita (fecha_hora, estado)` | Ninguna propia: se solapa con `idx_cita_fecha_hora`, del que solo se diferencia por llevar `estado` de acompanante | **Alta.** `fecha_hora` como lider | Era el elegido de Q2. Tras el `DROP INDEX` de la pregunta 2, Q2 volvio al `Seq Scan` con `Rows Removed by Filter: 29860`: 0,5 ms → 11,4 ms | Una entrada por cita, mas ancha que la de `idx_cita_fecha_hora` por llevar la segunda columna | **Se descarta,** o **reemplaza** a `idx_cita_fecha_hora` —no se conservan los dos—. Un indice `(A, B)` sirve para todo lo que sirve `(A)`; al reves no |

**1. Regla de sobre-indexacion que adopto.** Ningun indice entra al proyecto sin estas cuatro cosas, y la cuarta es la que casi nadie escribe:

- **(a) Una consulta documentada** que lo use, con su pantalla y su frecuencia aproximada. «Por si buscamos por ahi algun dia» no es una consulta.
- **(b) Evidencia de `EXPLAIN ANALYZE`** de que el planeador lo elige, pegada en `/informe/07-indices.txt`. Un indice que no aparece en ningun plan es un indice muerto que cobra escritura, cache y espacio de respaldo sin devolver nada.
- **(c) El costo de escritura nombrado**: sobre que procedimiento del PI pesa —`sp_agendar_cita`, `sp_registrar_consulta`— y con que frecuencia.
- **(d) Fecha de revision.** Cada indice se vuelve a mirar al final del semestre, y el que no aparezca en ningun plan **se borra**. Sin esta regla la lista de indices solo crece, porque agregar tiene un dueno y quitar no tiene ninguno.

Y una regla derivada del experimento de la pregunta 2, que es la que mas indices ahorra: **antes de crear un indice nuevo, comprobar si uno existente ya lo cubre por su columna lider.** `(fecha_hora, estado)` sirve para todo lo que sirve `(fecha_hora)`; `(estado, fecha_hora)` no sirve para nada de lo que sirve `(fecha_hora)`. Aplicando eso, los cinco indices de la tabla se quedan en **tres**: el parcial de la agenda, el de `fecha_hora` para el historico y el de `mascota (id_dueno)`.

**2. Particionamiento: veredicto para VetCare.** **No, todavia no.** Y conviene decirlo con los numeros propios: Huellitas atiende del orden de **30 a 40 citas por dia**, unos 26 dias al mes, lo que da unas **10.000 citas al ano** y aproximadamente **1,5 MB anuales** en la tabla `cita` con sus indices. A ese ritmo, la tabla tarda **una decada** en alcanzar las 100.000 filas, un volumen que PostgreSQL atiende sin esfuerzo con los tres indices de arriba. Particionar hoy agregaria complejidad permanente —una particion nueva que crear cada ano y que **nadie va a recordar** hasta que un `INSERT` falle con «no partition found for row»— para resolver un problema que no existe. La regla que dejo escrita es un **umbral**: se revisa cuando `cita` pase de **5 millones de filas** o cuando el archivado anual empiece a necesitar una ventana de mantenimiento, lo que llegue primero.

Y sobre lo que **si** quedo demostrado, con honestidad: en ExamLab se particiono una tabla de **5.010 filas**, y a ese volumen la ganancia de **rendimiento no es apreciable** —la tabla entera cabe en memoria y un recorrido completo cuesta poco mas de un milisegundo—. Los dos beneficios que **si** se comprobaron son de otra naturaleza y no dependen del volumen:

- **La poda de particiones en el plan.** Al filtrar por el rango de 2026, `cita_hist_2025` **no aparece** en el plan: no se abre, no se lee, no se estima. Y la contraprueba lo confirma: sin filtro, el plan muestra las dos bajo un `Append`. Eso es una propiedad estructural y se cumple igual con 5 millones de filas, donde si seria una diferencia enorme.
- **La facilidad de archivado.** `DROP TABLE cita_hist_2025;` libera 2.620 filas en una operacion de metadatos: sin WAL por fila, sin filas muertas, sin `VACUUM` posterior. El `DELETE FROM cita WHERE fecha_hora < '2026-01-01'` equivalente recorre la tabla, escribe 2.620 registros en el WAL, mantiene todos los indices durante el borrado y **no devuelve el espacio** sin un `VACUUM FULL` que bloquea la tabla. Con 2.620 filas es un detalle; a escala es la diferencia entre un segundo y una ventana nocturna. La variante que se usa cuando hay que conservar el dato es `ALTER TABLE ... DETACH PARTITION`, y se conecta directo con el `pg_dump` de la Clase 4.

Tambien aprendi un limite que no esperaba y que va al informe: la poda **se pierde** si el filtro se envuelve en una funcion. Con `EXTRACT(YEAR FROM fecha_hora) = 2026` el resultado sigue siendo correcto —2.390— pero el plan lee **las dos** particiones y descarta 2.620 filas en 2025. Es el mismo antipatron de sargabilidad de la Clase 6 apareciendo en otro nivel: alli costaba un indice, aqui cuesta una particion entera.

**Archivos del PI:** la tabla de arriba en `/informe/07-indices.md`, los `CREATE INDEX` definitivos en `/db/04_indices.sql` —los tres que sobreviven, no los cinco— y los planes en `/informe/07-planes.txt`, al lado de los de la Clase 6 para poder comparar.

### Como calificar

- **10 pts — la tabla, con al menos 3 indices y las 7 columnas.** Se reparte por columna, no por fila: 1,5 pts que esten los 3 indices identificados con su tabla y columnas, y 1,7 pts por cada una de las 5 columnas de contenido —consulta del PI, cardinalidad, evidencia, costo, veredicto— evaluadas en el conjunto de las filas. Una tabla con 5 indices y una columna vacia vale menos que una con 3 indices completa.
- **La columna de evidencia es la que decide la nota de esta pregunta.** Tiene que traer el **nodo concreto** —`Index Scan using idx_...`, `Bitmap Heap Scan`— y la caida de tiempo. «Mejoro» no es evidencia. Las anclas que se pueden verificar contra las preguntas 1 y 2: el `Rows Removed by Filter` que desaparece, las 91 filas, las 2 filas de C2, el 29.860 de despues del `DROP`.
- **La columna de cardinalidad se califica por el razonamiento, no por el numero.** Lo que se exige es que distinga **alta** —`fecha_hora`, `id_dueno`— de **baja** —`estado`, 3 valores, 61 % de la tabla— y que conecte eso con la utilidad del indice. Quien escriba «`estado` tiene baja cardinalidad» y aun asi deje ese indice sin justificar el caso parcial, no entendio la columna.
- **La columna de veredicto tiene que decidir de verdad.** Los cinco indices de las preguntas 1 y 2 **se solapan a proposito**, asi que una tabla donde los cinco «se quedan» esta incompleta: falta ver que `(fecha_hora, estado)` y `(fecha_hora)` cubren lo mismo, y que el parcial hace innecesario el `(estado, fecha_hora)`. **Reducir cinco indices a tres con argumento es la mejor respuesta posible a esta pregunta.**
- **4 pts — la regla de sobre-indexacion, operativa y verificable.** «No crear indices innecesarios» vale 1 de 4: no se puede verificar. Se dan los 4 pts cuando la regla dice **quien** decide, **con que evidencia** y **cuando se revisa**. La condicion de retiro —el indice que no aparezca en ningun plan se borra— es lo que la vuelve una regla y no un deseo.
- **6 pts — el veredicto sobre particionamiento.** 2 pts la estimacion de volumen **propia** con la cuenta a la vista (citas por dia x dias), 2 pts la decision con su umbral de revision, y 2 pts —los que exige la rubrica de forma explicita— **reconocer que con 5.010 filas la ganancia de rendimiento no es medible** y distinguir la poda de particiones y el archivado de la mejora de velocidad. Un informe que presente el particionamiento del taller como una mejora de rendimiento pierde los 6 pts completos, aunque el SQL de la pregunta 3 este perfecto.

### Errores frecuentes y que hacer

- **La tabla convertida en una lista de `CREATE INDEX`.** Se reconoce porque las columnas de cardinalidad, costo y veredicto dicen lo mismo en todas las filas, o estan vacias. La pregunta no pide inventariar los indices —eso ya lo hizo `pg_indexes`—, pide **justificarlos uno por uno**.
- **Todos los veredictos en «se queda».** Es la senal mas clara de que no se comparo un indice contra otro. Los cinco indices del taller se solapan deliberadamente, y quien no proponga retirar por lo menos uno se perdio el punto de la clase, que es que **cada indice hay que pagarlo**.
- **Confundir el costo de mantenimiento con el tamano.** «Ocupa 2 MB» no es el costo que se pregunta. El costo es **sobre que escrituras del PI pesa**: cada `INSERT` de `sp_agendar_cita` mantiene todos los indices de `cita`, y un indice cuya columna lider es `estado` se **reescribe** en cada cambio de estado. Ese es el dato que sirve para decidir.
- **Escribir que el particionamiento «mejoro el rendimiento» del historico.** Con 5.010 filas no mejoro nada medible, y el enunciado lo advierte por escrito. Es el descuento mas grande de la pregunta y el mas facil de evitar. La respuesta correcta reconoce el limite y **aun asi** defiende lo que si se demostro: la poda en el plan y el archivado.
- **Un veredicto de particionamiento sin numeros propios.** «Depende del volumen» no decide nada. La rubrica pide una estimacion —citas por dia x dias de operacion— y una conclusion. La cuenta cabe en una linea y es la que convierte la opinion en criterio.
- **Olvidar que la regla de sobre-indexacion necesita una condicion de retiro.** Casi todas las entregas dicen como **crear** un indice y ninguna dice cuando **borrarlo**. Por eso las bases reales acumulan indices muertos: agregar tiene un responsable y quitar no tiene ninguno.

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**¿Por que el planeador eligio el indice parcial y no el completo, si los dos son sobre `fecha_hora`?**

Porque el parcial le cuesta menos por dos razones a la vez. Tiene **menos entradas** —18.187 contra 30.010, un 39 % menos de arbol que recorrer— y, sobre todo, **su definicion ya garantiza el estado**: todo lo que hay dentro es `PROGRAMADA`, asi que el motor lee las 91 entradas del dia y ninguna sobra. Con el indice completo tendria que leer las 150 citas del dia, ir a la tabla por cada una a mirar el `estado` y descartar 59. Si en tu corrida gano el completo, la diferencia de costo entre los dos es pequena: **reporta lo que viste**, que es lo que se califica.

**Cree el indice y el plan no cambio. ¿El indice no sirve?**

Revisa tres cosas en este orden. **Una:** ¿corriste `ANALYZE` despues del `CREATE INDEX`? El planeador decide por costo estimado, y con estadisticas viejas puede ignorar un indice perfectamente bueno. **Dos:** ¿la columna lider del indice aparece en tu `WHERE`? A un arbol B solo se entra por la izquierda; es literalmente el experimento de la pregunta 2. **Tres:** ¿cuantas filas devuelve tu consulta? Si es mas de un tercio de la tabla, el motor **hace bien** en recorrerla completa —eso es lo que pasa en Q3—. Y si tras las tres el plan sigue igual y la consulta devuelve pocas filas, entonces si tienes un hallazgo que vale la pena mirar.

**¿Que es un indice parcial y cuando conviene?**

Es un indice que solo incluye las filas que cumplen una condicion: `CREATE INDEX ... ON cita (fecha_hora) WHERE estado = 'PROGRAMADA';`. Conviene cuando las consultas **siempre** traen ese mismo filtro, y entonces gana dos veces: es mas pequeno y no tiene que reverificar la condicion. Tiene dos limites que hay que conocer. Uno: si una consulta **no** trae `estado = 'PROGRAMADA'`, el motor **no puede** usarlo, ni siquiera parcialmente —por eso el indice completo sobre `fecha_hora` sigue teniendo sentido para el historico—. Dos, y es la parte elegante: cuando una cita pasa a `ATENDIDA`, su entrada **sale** del indice sola; el parcial se mantiene pequeno sin que nadie lo limpie.

**¿Por que la llave foranea no crea su indice automaticamente?**

Porque PostgreSQL crea indice para lo que necesita **garantizar** —la unicidad de una `PRIMARY KEY` o de un `UNIQUE`— y una llave foranea no garantiza unicidad, garantiza existencia, y para eso le basta el indice del lado **padre**, que ya existe. El lado **hijo** queda sin indexar, y eso se paga dos veces: «las mascotas de un dueno» recorre las 5.008 mascotas —lo mediste en la pregunta 1— y cada `DELETE` de un `dueno` hace ese mismo recorrido para comprobar que no queden mascotas huerfanas. Indexar el lado hijo de cada llave foranea es una de las poquisimas indexaciones que se pueden dar por buenas casi sin medir.

**¿`(estado, fecha_hora)` y `(fecha_hora, estado)` no son lo mismo?**

No, y la pregunta 2 existe para que lo compruebes en tu propia maquina. Piensa en el indice como una guia telefonica: si esta ordenada por **apellido y luego nombre**, encontrar «todos los Gomez» es abrir en una pagina y leer seguido; encontrar «todos los que se llaman Ana» obliga a leerla entera. Aqui pasa igual: `(estado, fecha_hora)` fija `PROGRAMADA` y dentro de ese bloque las fechas ya vienen ordenadas, asi que el rango es un tramo contiguo de 91 entradas. Con `(fecha_hora, estado)`, las citas del 10 de marzo estan juntas pero repartidas en tres estados. La regla es **igualdad primero, rango despues**, y el corolario que mas indices ahorra es este: `(A, B)` sirve para todo lo que sirve `(A)`; al reves, no.

**Borre `idx_cita_fecha_estado` y Q2 volvio al `Seq Scan`, pero `idx_cita_estado_fecha` **si** tiene `fecha_hora`. ¿Por que no la uso?**

Porque a un arbol B solo se entra por la **columna lider**, y `estado` no esta en tu `WHERE`. Para encontrar las citas del 10 de marzo con ese indice, el motor tendria que recorrer las **30.010 entradas** completas y ademas ir a la tabla por cada candidata —`id_cita` no esta en el indice, asi que no puede resolverlo sin la tabla—. Eso sale mas caro que el `Seq Scan`, y el planeador lo calcula: `Rows Removed by Filter: 29860`, de 0,5 ms a 11,4 ms. Es la demostracion experimental de la regla, y es el resultado que la pregunta busca.

**¿Por que la PK de `cita_hist` tiene que llevar `fecha_hora`?**

Porque PostgreSQL implementa la unicidad con un indice **por particion**, no con uno global. Si la PK fuera solo `id_cita`, para garantizar que no se repite habria que revisar **todas** las particiones en cada `INSERT`, y el motor no lo hace: exige que la columna de particion este en la llave, porque asi sabe en cual particion buscar. Si lo intentas sin ella, el error es literal: «unique constraint on partitioned table must include all partitioning columns». La consecuencia practica es que `(id_cita, fecha_hora)` permite en teoria el mismo `id_cita` en dos anos distintos; en un historico de solo lectura, alimentado desde `cita`, eso no es un problema, pero hay que saberlo.

**Particione la tabla y no quedo mas rapida. ¿Hice algo mal?**

No, y darte cuenta vale mas que la mejora que esperabas. Con **5.010 filas** la tabla entera cabe en memoria y recorrerla cuesta poco mas de un milisegundo: no hay de donde sacar una ganancia. Lo que si demostraste son dos cosas que **no dependen del volumen**: la **poda de particiones** —`cita_hist_2025` no aparece en el plan, y la contraprueba sin filtro muestra que si aparece cuando no hay nada que podar— y el **archivado**, un `DROP TABLE` de la particion contra un `DELETE` masivo. Escribelo asi en la pregunta 5: la rubrica premia esa distincion de forma explicita y penaliza el informe que presenta el particionamiento como una mejora de velocidad. Prueba ademas el filtro con `EXTRACT(YEAR FROM ...)`: veras que la poda se pierde, y ese hallazgo si es un resultado.

---

## Cierre de la clase

- Al terminar, cada estudiante debe tener: los tres indices de la pregunta 1 con su linea base, su `ANALYZE` y su `Index Scan` verificado en `pg_indexes`; el experimento del orden de columnas con los tres `EXPLAIN`, el `DROP INDEX` y la conclusion de igualdad-antes-de-rango; `cita_hist` particionada con **2.620 / 2.390** filas enrutadas y la poda visible en el plan; las cuatro afirmaciones correctas de la pregunta 4; y la tabla de justificacion de siete columnas con su regla de sobre-indexacion y su veredicto de particionamiento, mas `/db/04_indices.sql` y `/informe/07-planes.txt` guardados.
- Antes de cerrar hay que verificar **tres numeros y una coherencia**, y los cuatro se leen sin ejecutar nada. Que el `Rows Removed by Filter` de la agenda del dia **haya desaparecido** del plan de la pregunta 1 —era 29.919 en la Clase 6 y en la linea base de hoy—. Que tras el `DROP INDEX` de la pregunta 2 aparezca **29.860**, que es el numero que solo sale de haber corrido el experimento. Que el enrutamiento diga **2.620 y 2.390** y no un reparto mitad y mitad. Y la coherencia: quien acerto la opcion de la baja cardinalidad en la pregunta 4 **no** puede haber escrito en la pregunta 5 que `idx_cita_estado_fecha` se queda sin discutirlo, porque su propio Q3 muestra un `Seq Scan` teniendo ese indice disponible.
- Esta clase cierra la promesa que la Clase 6 dejo abierta —el `Seq Scan` de 30.010 filas se volvio un `Index Scan` de 91— y conviene decirlo en voz alta, porque es la unica vez del semestre en que una hipotesis escrita una semana antes se confirma con una medicion propia. Tambien conviene dejar la contraparte: esos indices hay que mantenerlos en cada `INSERT` de `sp_agendar_cita`, y la pregunta 5 obliga a reducir cinco indices a tres precisamente por eso. Y como puente: la Clase 8 deja de hablar de una sola sesion midiendo sola y pasa a **varias sesiones peleandose por la misma fila** —transacciones, aislamiento y bloqueos—, donde el problema ya no es el tiempo de una consulta sino quien espera a quien.

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. El motor de la plataforma es PostgreSQL (PGlite en el navegador), no Oracle.
