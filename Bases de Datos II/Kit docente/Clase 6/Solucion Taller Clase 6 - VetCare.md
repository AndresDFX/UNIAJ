# Solucion del taller · Clase 6 · Optimizacion de consultas de VetCare (antes / despues)

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** Las dos consultas del PI reescritas y medidas sobre las 30.010 citas reales de la base: la agenda del dia con sus cuatro antipatrones corregidos y las **91 filas** que las dos versiones tienen que devolver, la evidencia del `EXPLAIN ANALYZE` leida e interpretada —incluida la parte incomoda, que sin indice las dos versiones siguen leyendo las 30.010 filas—, la subconsulta correlacionada de 2.006 ejecuciones convertida en una sola pasada con la prueba de equivalencia por `EXCEPT`, y la justificacion tecnica que va al informe.

> **El motor es PostgreSQL, no Oracle:** aqui se lee `EXPLAIN (ANALYZE, BUFFERS)` con sus nodos `Seq Scan`, `Hash Join` y `Nested Loop`, no un `AUTOTRACE` ni un `TKPROF`. Tres avisos operativos que conviene dar antes de arrancar. Primero: la base de este taller **si tiene volumen** —2.006 duenos, 5.008 mascotas, 16 veterinarios y 30.010 citas, con `ANALYZE` ya corrido y **sin ningun indice** mas alla de las llaves primarias—, asi que las mediciones significan algo. Segundo: la version ANTES de la pregunta 3 ejecuta una subconsulta 2.006 veces y en el navegador **puede tardar de varios segundos a mas de un minuto**; no esta colgada, y hay que decirlo o media clase va a recargar la pagina. Tercero: los milisegundos que aparecen en esta solucion son de una corrida de referencia y **cambian en cada maquina**; lo que no cambia son los conteos de filas, y por eso los conteos son lo que se califica.

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 6 - Optimizacion de consultas/Taller PI - Clase 6 - VetCare.docx`
- Configuracion en la plataforma: `Kit docente/Clase 6/Taller en ExamLab - Clase 6 (configuracion).md`
- Caso de estudio: `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
- Hito del PI: Primera pareja de consultas antes/despues del PI
- Entregable: 2 consultas (antes/despues) + justificacion (media pag.)
- **Estas preguntas: 100 puntos** en 5 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 1 | Reescribir la consulta de agenda del dia | `bd_sql` | 30 |
| 2 | Medir con EXPLAIN ANALYZE: la evidencia del antes/despues | `bd_sql` | 20 |
| 3 | Matar la subconsulta correlacionada del reporte de duenos | `bd_sql` | 20 |
| 4 | Antipatrones de consulta en VetCare | `cerrada_multi` | 10 |
| 5 | Justificacion tecnica del antes/despues (media pagina) | `abierta` | 20 |

---

## Pregunta 1 · Reescribir la consulta de agenda del dia · 30 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- ANTES: la version con los cuatro antipatrones, tal como la escribio
    -- quien la programo. Se corre primero para tener la linea base y, sobre
    -- todo, el numero de filas que la version nueva esta obligada a igualar.
    -- =====================================================================
    SELECT *
    FROM cita c, mascota m, dueno d, veterinario v
    WHERE c.id_mascota = m.id_mascota
      AND m.id_dueno = d.id_dueno
      AND c.id_veterinario = v.id_veterinario
      AND to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10'
      AND UPPER(c.estado) = 'PROGRAMADA';

    -- =====================================================================
    -- DESPUES: la misma informacion util, con los cuatro antipatrones
    -- corregidos. Cada correccion va comentada con su razon.
    -- =====================================================================
    SELECT c.id_cita,                    -- (1) PROYECCION: seis columnas en vez
           c.fecha_hora,                 --     de las ~20 que traia SELECT *.
           m.nombre AS mascota,          --     Menos bytes por fila en el join,
           d.nombre AS dueno,            --     en el ordenamiento y en la red.
           v.nombre AS veterinario,
           c.estado
      FROM cita c
      -- (2) JOIN ... ON explicitos. No hacen la consulta mas rapida -- el plan
      --     es identico -- pero separan la condicion de union de la condicion
      --     de filtro, y asi no se puede "perder" un ON y producir un
      --     producto cartesiano de 30.010 x 5.008 filas sin darse cuenta.
      JOIN mascota     m ON m.id_mascota     = c.id_mascota
      JOIN dueno       d ON d.id_dueno       = m.id_dueno
      JOIN veterinario v ON v.id_veterinario = c.id_veterinario
      -- (3) PREDICADO DE RANGO. La columna queda sola a la izquierda del
      --     operador: eso es lo que la vuelve *sargable*. Con
      --     to_char(fecha_hora, ...) el motor tiene que calcular la funcion
      --     para las 30.010 filas antes de poder comparar, y ademas no puede
      --     estimar cuantas van a pasar. Se usa >= y < , no BETWEEN, para no
      --     tener que pensar si la medianoche del 11 entra o no.
     WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
      -- (4) COMPARACION DIRECTA. El dominio ya esta normalizado por el
      --     CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA')), asi que
      --     UPPER() no protege de nada y solo estorba: con la columna desnuda,
      --     el motor puede usar sus estadisticas de valores frecuentes.
       AND c.estado = 'PROGRAMADA'
     ORDER BY c.fecha_hora, c.id_cita;   -- id_cita como desempate: ver abajo

    -- =====================================================================
    -- EQUIVALENCIA: optimizar no puede cambiar el resultado. Los dos conteos
    -- tienen que dar el mismo numero.
    -- =====================================================================
    SELECT COUNT(*) AS filas_antes
    FROM cita c, mascota m, dueno d, veterinario v
    WHERE c.id_mascota = m.id_mascota
      AND m.id_dueno = d.id_dueno
      AND c.id_veterinario = v.id_veterinario
      AND to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10'
      AND UPPER(c.estado) = 'PROGRAMADA';

    SELECT COUNT(*) AS filas_despues
      FROM cita c
      JOIN mascota     m ON m.id_mascota     = c.id_mascota
      JOIN dueno       d ON d.id_dueno       = m.id_dueno
      JOIN veterinario v ON v.id_veterinario = c.id_veterinario
     WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
       AND c.estado = 'PROGRAMADA';

    -- =====================================================================
    -- Y la version de una sola linea, que es la que conviene pegar al
    -- corregir: si la diferencia no es 0, la reescritura cambio el resultado.
    -- =====================================================================
    SELECT (SELECT COUNT(*) FROM cita c
             WHERE to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10'
               AND UPPER(c.estado) = 'PROGRAMADA')            AS antes,
           (SELECT COUNT(*) FROM cita c
             WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
               AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
               AND c.estado = 'PROGRAMADA')                   AS despues,
           (SELECT COUNT(*) FROM cita
             WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
               AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00') AS ese_dia_en_total;
```

### Salida esperada

```
Version DESPUES -- 91 filas

     id_cita |     fecha_hora      |   mascota    |   dueno    |  veterinario   |   estado
    ---------+---------------------+--------------+------------+----------------+------------
          74 | 2026-03-10 08:45:00 | Mascota 57   | Dueno 52   | Veterinario 1  | PROGRAMADA
        1874 | 2026-03-10 08:45:00 | Mascota 1857 | Dueno 1852 | Veterinario 1  | PROGRAMADA
        3674 | 2026-03-10 08:45:00 | Mascota 3657 | Dueno 1652 | Veterinario 1  | PROGRAMADA
        5474 | 2026-03-10 08:45:00 | Mascota 457  | Dueno 452  | Veterinario 1  | PROGRAMADA
         ... 87 filas mas ...
       28674 | 2026-03-10 14:00:00 | Mascota 3657 | Dueno 1652 | Veterinario 5  | PROGRAMADA

    Equivalencia -- 1 fila

     antes | despues | ese_dia_en_total
    -------+---------+------------------
        91 |      91 |              150

    Reparto de las 91 por franja horaria (mismo dato, agrupado):

     08:45 -> 15    09:30 -> 15    11:00 -> 15
     11:45 -> 16    13:15 -> 15    14:00 -> 15
```

**91 es el numero de la pregunta.** Es el que hay que buscar en cualquier entrega, y no depende de la maquina: el 2026-03-10 tiene 150 citas —150 por dia en toda la base— y de esas 91 estan PROGRAMADA, 45 ATENDIDA y 14 CANCELADA. Si un estudiante reporta 150, se le olvido el filtro de estado; si reporta 0, casi siempre escribio `BETWEEN '2026-03-10' AND '2026-03-10'`, que con TIMESTAMP solo atrapa la medianoche exacta.

Son **seis** franjas y no nueve, y el detalle tiene explicacion: la base genera las horas en pasos de 45 minutos y hace ATENDIDA una de cada tres citas, y las tres franjas que caen en los multiplos —08:00, 10:15 y 12:30— quedan todas ATENDIDA o CANCELADA. No es un error de nadie.

**Sobre el `ORDER BY`:** el enunciado pide ordenar por `c.fecha_hora`, y con eso solo hay entre 15 y 16 filas **empatadas** dentro de cada franja, cuyo orden el motor no garantiza. Dos corridas de la misma consulta pueden imprimir la agenda en distinto orden. Por eso esta solucion agrega `, c.id_cita`: no se exige, y no se descuenta por no tenerlo, pero es lo que hace que la evidencia del estudiante sea reproducible y vale la pena senalarlo en la devolucion.

### Como calificar

- **16 pts — los cuatro antipatrones corregidos, 4 pts cada uno.** (1) La proyeccion con las seis columnas y los alias `mascota`, `dueno`, `veterinario` exactos. (2) Los tres `JOIN ... ON` explicitos. (3) El **predicado de rango** con `>=` y `<` y la columna sola a la izquierda. (4) `c.estado = 'PROGRAMADA'` sin `UPPER`. Los 4 pts del punto 3 son los que mas se pierden y los que mas importan: es el unico cambio que habilita el indice de la Clase 7.
- **4 pts — `ORDER BY c.fecha_hora`.** Se dan completos con la columna pedida. Se anota como observacion —sin puntos extra— si el estudiante agrego un desempate: con solo `fecha_hora` hay 15 o 16 filas empatadas por franja y el orden dentro de cada una no esta garantizado.
- **6 pts — la version ANTES se ejecuto** y quedo como linea base, tal cual, sin «arreglarla» de paso. Sin la linea base la comparacion de la pregunta 2 no tiene contra que medirse.
- **4 pts — los dos `COUNT(*)` coinciden y valen 91.** 2 pts que esten los dos conteos y 2 pts que el numero sea 91. Si coinciden pero valen 150 o 0, la equivalencia esta demostrada y el filtro esta mal: se dan los 2 primeros y no los otros 2.
- **Se descuenta segun la rubrica** si queda `SELECT *`, si sobrevive cualquier funcion sobre `fecha_hora` en el `WHERE`, o si el conteo difiere del de la version ANTES. Lo ultimo es lo mas grave de los tres y conviene decirlo asi: una consulta mas rapida que devuelve otra cosa no esta optimizada, esta rota.
- **Bono conceptual, sin puntos, y es el mejor de la clase:** quien escriba que el predicado de rango **todavia no evita el `Seq Scan`**, porque no hay ningun indice sobre `fecha_hora`, y que lo que gana hoy es dejar de calcular la funcion 30.010 veces y darle al planeador una estimacion correcta, entendio la clase completa y ya escribio la seccion 4 de la pregunta 5.

### Errores frecuentes y que hacer

- **`BETWEEN '2026-03-10' AND '2026-03-10'`** para «el dia». Devuelve **0 filas** y es el error mas comun del semestre: el literal se convierte a `2026-03-10 00:00:00` y solo atrapa la medianoche exacta. La variante `BETWEEN '2026-03-10' AND '2026-03-11'` es peor todavia, porque **si** devuelve algo pero se lleva de contrabando las citas de la medianoche del 11. Con `>=` y `<` el problema no existe y no hay que pensarlo.
- **Cambiar `to_char(...)` por `DATE(c.fecha_hora) = '2026-03-10'`** o por `EXTRACT`. Es mas corto y **mantiene intacto el antipatron**: sigue habiendo una funcion envolviendo la columna, la sargabilidad sigue perdida y los 4 pts no se dan. Vale explicar la regla en una frase: la columna tiene que quedar **sola** a la izquierda del operador.
- **Dejar `SELECT *` y solo cambiar las comas por `JOIN`.** Es media entrega y se detecta al instante porque la salida trae unas veinte columnas, con `id_mascota` repetido tres veces. La rubrica lo penaliza de forma explicita.
- **Perder un `ON` al convertir las comas.** Produce un producto cartesiano silencioso: en vez de 91 filas salen decenas de miles, y en el navegador el sintoma es que la pestana se congela. Es justamente el accidente que los `JOIN ... ON` explicitos existen para prevenir, asi que conviene usar el error para justificar el antipatron 2.
- **Cambiar el resultado y no notarlo.** Las dos variantes tipicas: agregar `AND m.activa = 'S'` «para que sea mas util» —quedan menos de 91 filas— o convertir un `JOIN` en `LEFT JOIN` «por seguridad» —quedan mas—. Las dos son mejoras de negocio, no optimizaciones, y las dos rompen la equivalencia. Si el estudiante quiere el filtro, va en una consulta aparte.
- **Reportar el numero de filas sin haberlo medido.** Se reconoce porque el numero es redondo: 150, 100, 90. El unico numero correcto es **91**, y sale solo de correr la consulta.

---

## Pregunta 2 · Medir con EXPLAIN ANALYZE: la evidencia del antes/despues · 20 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- 1) EXPLAIN de la version ANTES. Se pega la consulta con antipatrones
    --    tal cual, sin tocar nada: es la linea base.
    -- =====================================================================
    EXPLAIN (ANALYZE, BUFFERS)
    SELECT *
    FROM cita c, mascota m, dueno d, veterinario v
    WHERE c.id_mascota = m.id_mascota
      AND m.id_dueno = d.id_dueno
      AND c.id_veterinario = v.id_veterinario
      AND to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10'
      AND UPPER(c.estado) = 'PROGRAMADA';

    -- =====================================================================
    -- 2) EXPLAIN de la version DESPUES.
    -- =====================================================================
    EXPLAIN (ANALYZE, BUFFERS)
    SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno,
           v.nombre AS veterinario, c.estado
      FROM cita c
      JOIN mascota     m ON m.id_mascota     = c.id_mascota
      JOIN dueno       d ON d.id_dueno       = m.id_dueno
      JOIN veterinario v ON v.id_veterinario = c.id_veterinario
     WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
       AND c.estado = 'PROGRAMADA'
     ORDER BY c.fecha_hora, c.id_cita;

    -- =====================================================================
    -- 3) DESPUES + LIMIT 50, que es lo que de verdad necesita la pantalla de
    --    agenda: la recepcionista ve medio dia, no las 91 citas de golpe.
    -- =====================================================================
    EXPLAIN ANALYZE
    SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno,
           v.nombre AS veterinario, c.estado
      FROM cita c
      JOIN mascota     m ON m.id_mascota     = c.id_mascota
      JOIN dueno       d ON d.id_dueno       = m.id_dueno
      JOIN veterinario v ON v.id_veterinario = c.id_veterinario
     WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
       AND c.estado = 'PROGRAMADA'
     ORDER BY c.fecha_hora, c.id_cita
     LIMIT 50;

    -- =====================================================================
    -- LECTURA DEL PLAN. Los conteos de filas son los de esta base y no
    -- cambian; los milisegundos son de una corrida de referencia.
    -- =====================================================================
    -- VERSION       | nodo mas costoso                        | filas est. vs reales | tiempo (ms)
    -- ANTES         | Seq Scan on cita, Filter: to_char()+upper(), Rows Removed by Filter: 29919 | rows=1 vs 91 -> el planeador se equivoco por un factor de ~91 | 118
    -- DESPUES       | Seq Scan on cita, Filter: rango de fecha_hora + estado, Rows Removed by Filter: 29919 | rows=90 vs 91 -> error menor al 2 % | 41
    -- DESPUES+LIM50 | el mismo Seq Scan; el LIMIT no lo evita porque el ORDER BY no tiene indice | 50 de 91 | 39
    --
    -- CONCLUSION: factor de mejora de aproximadamente 2,9x (118 -> 41 ms) en este
    -- entorno. NO es un orden de magnitud, y la razon es la parte honesta del
    -- ejercicio: sin ningun indice sobre fecha_hora, las DOS versiones recorren
    -- las 30.010 filas de cita y descartan las mismas 29.919. Lo que la version
    -- DESPUES si elimina son 60.020 llamadas a funcion (to_char y upper, una vez
    -- por fila cada una), unas 14 columnas de acarreo por fila en los joins y en
    -- el ordenamiento, y -- lo mas importante para el plan -- el error de
    -- estimacion: con rows=1 el planeador cree que va a unir una sola cita y
    -- elige la forma de join equivocada. El salto grande queda pendiente para la
    -- Clase 7: con un indice sobre (fecha_hora, estado) el Seq Scan de 30.010
    -- filas se convierte en un Index Scan de ~150, y ese si es el orden de
    -- magnitud.

    -- =====================================================================
    -- Comprobacion opcional que hace visible el error de estimacion sin tener
    -- que leer el plan completo: el mismo filtro, primero envuelto en
    -- funciones y luego desnudo.
    -- =====================================================================
    EXPLAIN ANALYZE SELECT COUNT(*) FROM cita c
     WHERE to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10'
       AND UPPER(c.estado) = 'PROGRAMADA';

    EXPLAIN ANALYZE SELECT COUNT(*) FROM cita c
     WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
       AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
       AND c.estado = 'PROGRAMADA';
```

### Salida esperada

```
Version ANTES -- forma del plan (los nombres de los nodos son los que hay que
    reconocer; el reparto entre Hash Join y Nested Loop puede variar):

    Nested Loop  (cost=... rows=1 width=...) (actual time=... rows=91 loops=1)
      Buffers: shared hit=...
      ->  Nested Loop  ... (actual rows=91 loops=1)
            ->  Nested Loop  ... (actual rows=91 loops=1)
                  ->  Seq Scan on cita c  (cost=0.00..1050.25 rows=1 width=...)
                                          (actual time=... rows=91 loops=1)
                        Filter: ((to_char(fecha_hora, 'YYYY-MM-DD'::text) = '2026-03-10'::text)
                                 AND (upper(estado) = 'PROGRAMADA'::text))
                        Rows Removed by Filter: 29919
                  ->  Index Scan using mascota_pkey on mascota m  (actual rows=1 loops=91)
            ->  Index Scan using dueno_pkey on dueno d  (actual rows=1 loops=91)
      ->  Index Scan using veterinario_pkey on veterinario v  (actual rows=1 loops=91)
    Execution Time: 118.4 ms

    Version DESPUES -- misma forma, dos diferencias que si importan:

    Sort  (actual rows=91 loops=1)
      Sort Key: c.fecha_hora, c.id_cita
      ->  Nested Loop  (cost=... rows=90 width=...) (actual rows=91 loops=1)
            ->  Seq Scan on cita c  (cost=0.00..750.15 rows=90 width=...)
                                    (actual time=... rows=91 loops=1)
                  Filter: ((fecha_hora >= '2026-03-10 00:00:00'::timestamp)
                           AND (fecha_hora < '2026-03-11 00:00:00'::timestamp)
                           AND (estado = 'PROGRAMADA'::text))
                  Rows Removed by Filter: 29919
            ->  ... los mismos tres Index Scan por llave primaria ...
    Execution Time: 41.2 ms
```

Los cuatro numeros que hay que saber leer en esta salida, y **solo los tres primeros son deterministas**:

1. **`Rows Removed by Filter: 29919`, igual en las dos.** Es la parte incomoda y es la mas instructiva: sin indice, las dos versiones leen las 30.010 filas y tiran las mismas 29.919. El predicado sargable **por si solo** no evita el `Seq Scan`; lo que hace es dejar la puerta abierta para el indice de la Clase 7. Un estudiante que reporte «desaparecio el Seq Scan» no leyo su plan.
2. **`rows=1` estimadas contra `rows=91` reales, en la version ANTES.** Ese 1 no es casualidad: cuando el filtro es una funcion sobre la columna, el motor no tiene estadisticas y aplica una selectividad por omision del 0,5 % por cada condicion; 30.010 x 0,005 x 0,005 da 0,75, que se redondea a 1. Con el predicado desnudo usa el histograma de `fecha_hora` y la lista de valores frecuentes de `estado`, y estima ~90 contra 91 reales.
3. **El plan del `LIMIT 50` conserva el `Seq Scan` completo.** Tiene que conservarlo: para saber cuales son las 50 primeras por `fecha_hora` sin un indice que ya venga ordenado, hay que encontrar y ordenar las 91. El `LIMIT` solo ahorra el transporte de 41 filas. Es el segundo argumento para el indice de la Clase 7.
4. **`Execution Time`.** Aqui 118 -> 41 ms, un factor de 2,9x. **Este es el unico numero que cambia de maquina a maquina** y en el navegador puede variar el doble entre dos corridas seguidas. Se acepta cualquier factor entre 1,5x y 3x; lo que no se acepta es un factor inventado.

Si el entorno rechaza la opcion `BUFFERS`, se corre `EXPLAIN ANALYZE` a secas y se dice en la pregunta 5, tal como autoriza el enunciado. Cuando si funciona, el dato que importa es que el `shared hit` del `Seq Scan on cita` es del mismo orden en las dos versiones -- otra vez: se leen los mismos bloques.

### Como calificar

- **6 pts — los tres `EXPLAIN` corren y corresponden.** 2 pts cada uno. El tercero, la variante con `LIMIT 50`, es el que mas se olvida y la rubrica lo nombra de forma explicita.
- **9 pts — la tabla en comentarios, 3 pts por columna.** Nodo mas costoso, filas estimadas contra reales, y tiempo de ejecucion, **para las tres versiones**: la columna se da completa cuando estan ANTES, DESPUES y DESPUES+LIM50, y vale 2 de 3 si falta la fila del `LIMIT 50`. La exigencia de la rubrica es que los valores esten **tomados del plan real**: se verifica con dos anclas que no se pueden adivinar, el `Rows Removed by Filter: 29919` y las 91 filas reales.
- **3 pts — la linea `-- CONCLUSION:` cuantifica la mejora.** Basta un factor aproximado con los dos tiempos que lo sustentan. **Un factor pequeno y honesto vale los 3 pts completos**, y un 50x sin dos tiempos que lo respalden vale 0: en esta base, sin indices, el factor real esta entre 1,5x y 3x.
- **2 pts — la interpretacion, no el volcado.** La rubrica descuenta si solo se pega el plan. Se dan los 2 pts cuando hay al menos una frase que explique **por que** el numero es el que es, y no solo cual es.
- **Se reconoce como sobresaliente, sin puntos extra pero se anota en la devolucion:** senalar que el `Seq Scan` **no desaparecio** y explicar que sin indice no puede desaparecer. Es la lectura correcta del plan y es exactamente lo contrario de lo que el estudiante espera encontrar, asi que solo llega ahi quien de verdad leyo.
- **No se califican los milisegundos.** Varian por maquina, por navegador y entre dos corridas seguidas. Se califica que esten, que sean coherentes entre si y que sustenten el factor declarado.

### Errores frecuentes y que hacer

- **Pegar los tres planes completos y nada mas.** Es el error que la rubrica penaliza de frente. Un volcado no es evidencia: la evidencia es la tabla de cuatro campos que el enunciado pide, y esa tabla obliga a **elegir** que numero importa.
- **Inventar los numeros.** Se detecta con dos preguntas: ¿cuantas filas descarto el filtro? —tiene que decir 29.919— y ¿cuantas filas reales devolvio? —91—. Quien invento el plan casi siempre pone 150, o un numero redondo, o el mismo `Rows Removed` distinto en las dos versiones.
- **Escribir «el `Seq Scan` desaparecio».** No desaparecio y no podia desaparecer: no hay ningun indice sobre `fecha_hora` en esta base. Es la confusion mas frecuente de la clase y viene de esperar el resultado en vez de leerlo. La correccion es una pregunta: ¿que indice usaria el motor, si no hay ninguno?
- **Reportar un factor de 50x o 100x.** Suele venir de comparar la primera corrida de la version ANTES —con la cache fria y el motor recien arrancado— contra la tercera de la version DESPUES. La forma correcta de medir es alternar: ANTES, DESPUES, ANTES, DESPUES, y quedarse con la segunda de cada una.
- **Confundir `cost=` con tiempo.** El `cost` es una unidad interna y arbitraria del planeador, no milisegundos ni bytes. El tiempo esta en `actual time=` de cada nodo y en el `Execution Time` del final. Comparar costes entre dos consultas distintas casi nunca dice nada util.
- **Omitir el `EXPLAIN` con `LIMIT 50`,** o cambiarlo por un `LIMIT` sin `ORDER BY`. Sin el `ORDER BY` el `LIMIT` **si** puede cortar el escaneo temprano y el plan deja de mostrar lo que la pregunta quiere ensenar: que un `LIMIT` con `ORDER BY` y sin indice no ahorra el trabajo, solo el transporte.

---

## Pregunta 3 · Matar la subconsulta correlacionada del reporte de duenos · 20 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- ANTES: una subconsulta en la lista de columnas. Se evalua UNA VEZ POR
    -- CADA FILA de dueno, es decir 2.006 veces, y cada una de esas veces une
    -- las 30.010 citas con las 5.008 mascotas. AVISO: en el navegador esto
    -- puede tardar de varios segundos a mas de un minuto. No esta colgado.
    -- =====================================================================
    SELECT d.id_dueno,
           d.nombre,
           (SELECT COUNT(*)
              FROM cita c
              JOIN mascota m ON m.id_mascota = c.id_mascota
             WHERE m.id_dueno = d.id_dueno) AS total_citas
    FROM dueno d
    ORDER BY total_citas DESC;

    EXPLAIN ANALYZE
    SELECT d.id_dueno,
           d.nombre,
           (SELECT COUNT(*)
              FROM cita c
              JOIN mascota m ON m.id_mascota = c.id_mascota
             WHERE m.id_dueno = d.id_dueno) AS total_citas
    FROM dueno d
    ORDER BY total_citas DESC;

    -- =====================================================================
    -- DESPUES: una sola pasada. Los dos LEFT JOIN y el COUNT de la COLUMNA
    -- son las dos decisiones de la pregunta:
    --   * LEFT JOIN, porque un dueno sin mascotas -- o con mascotas sin citas
    --     -- tiene que seguir apareciendo con cero. Con INNER JOIN
    --     desaparecen seis duenos del reporte.
    --   * COUNT(c.id_cita) y NO COUNT(*), porque el LEFT JOIN fabrica una
    --     fila con NULL para el dueno sin citas: COUNT(*) contaria esa fila
    --     fantasma y diria 1. COUNT de una columna ignora los NULL y dice 0.
    -- =====================================================================
    SELECT d.id_dueno,
           d.nombre,
           COUNT(c.id_cita) AS total_citas
      FROM dueno d
      LEFT JOIN mascota m ON m.id_dueno    = d.id_dueno
      LEFT JOIN cita    c ON c.id_mascota  = m.id_mascota
     GROUP BY d.id_dueno, d.nombre
     ORDER BY total_citas DESC, d.id_dueno
     LIMIT 20;

    EXPLAIN ANALYZE
    SELECT d.id_dueno,
           d.nombre,
           COUNT(c.id_cita) AS total_citas
      FROM dueno d
      LEFT JOIN mascota m ON m.id_dueno    = d.id_dueno
      LEFT JOIN cita    c ON c.id_mascota  = m.id_mascota
     GROUP BY d.id_dueno, d.nombre
     ORDER BY total_citas DESC, d.id_dueno
     LIMIT 20;

    -- =====================================================================
    -- EQUIVALENCIA con EXCEPT en los DOS sentidos, sin LIMIT. EXCEPT no es
    -- simetrico: A EXCEPT B vacio solo dice que A no tiene nada que B no
    -- tenga. Hacen falta las dos direcciones para probar la igualdad de los
    -- conjuntos, y por eso se unen con UNION ALL: el resultado correcto es
    -- CERO FILAS.
    -- =====================================================================
    (
      SELECT d.id_dueno,
             (SELECT COUNT(*)
                FROM cita c JOIN mascota m ON m.id_mascota = c.id_mascota
               WHERE m.id_dueno = d.id_dueno) AS total_citas
        FROM dueno d
      EXCEPT
      SELECT d.id_dueno, COUNT(c.id_cita)
        FROM dueno d
        LEFT JOIN mascota m ON m.id_dueno   = d.id_dueno
        LEFT JOIN cita    c ON c.id_mascota = m.id_mascota
       GROUP BY d.id_dueno
    )
    UNION ALL
    (
      SELECT d.id_dueno, COUNT(c.id_cita)
        FROM dueno d
        LEFT JOIN mascota m ON m.id_dueno   = d.id_dueno
        LEFT JOIN cita    c ON c.id_mascota = m.id_mascota
       GROUP BY d.id_dueno
      EXCEPT
      SELECT d.id_dueno,
             (SELECT COUNT(*)
                FROM cita c JOIN mascota m ON m.id_mascota = c.id_mascota
               WHERE m.id_dueno = d.id_dueno) AS total_citas
        FROM dueno d
    );

    -- =====================================================================
    -- Y la comprobacion corta, para el momento de calificar: los seis duenos
    -- sin ninguna cita tienen que decir 0, no 1.
    -- =====================================================================
    SELECT d.id_dueno, d.nombre, COUNT(c.id_cita) AS total_citas
      FROM dueno d
      LEFT JOIN mascota m ON m.id_dueno   = d.id_dueno
      LEFT JOIN cita    c ON c.id_mascota = m.id_mascota
     GROUP BY d.id_dueno, d.nombre
    HAVING COUNT(c.id_cita) = 0
     ORDER BY d.id_dueno;
```

### Salida esperada

```
Version DESPUES -- 20 filas

     id_dueno |     nombre     | total_citas
    ----------+----------------+-------------
            3 | Marcela Diaz   |          33
            1 | Ana Gomez      |          28
            4 | Jorge Pineda   |          26
            5 | Luisa Cardona  |          25
            2 | Carlos Ruiz    |          24
            6 | Andres Vallejo |          24
            7 | Dueno 1        |          18
            8 | Dueno 2        |          18
          ... hasta el id_dueno 20, todos con 18 ...

    Equivalencia -- 0 filas

     (el EXCEPT en los dos sentidos no devolvio ninguna fila)

    Comprobacion de los duenos sin citas -- 6 filas

     id_dueno |  nombre   | total_citas
    ----------+-----------+-------------
         2001 | Dueno 1995|           0
         2002 | Dueno 1996|           0
         2003 | Dueno 1997|           0
         2004 | Dueno 1998|           0
         2005 | Dueno 1999|           0
         2006 | Dueno 2000|           0
```

**El ranking.** Los seis primeros son los duenos sembrados a mano, y tiene sentido: son los unicos que tienen mascotas de las dos tandas —las 8 sembradas y las generadas—. Del septimo hacia abajo hay **987 duenos empatados en 18**, asi que el `ORDER BY total_citas DESC, d.id_dueno` no es un adorno: sin el desempate por `id_dueno`, las filas 7 a 20 salen distintas en cada corrida y la evidencia del estudiante no se puede comparar con nada.

**La equivalencia: cero filas es el resultado correcto**, y es la unica forma de afirmar que las dos versiones son iguales. Si devuelve 6 filas —las de los id_dueno 2001 a 2006— el error esta identificado sin necesidad de leer el codigo: se uso `COUNT(*)` en vez de `COUNT(c.id_cita)`.

**Las seis filas con 0** son el numero que separa las tres entregas posibles: 6 filas con 0 = correcto; 6 filas con **1** = se uso `COUNT(*)`; **0 filas** = se uso `INNER JOIN` y esos seis duenos desaparecieron del reporte. Los tres casos se distinguen con esta sola consulta.

**Sobre el rendimiento:** la version ANTES ejecuta el `SubPlan` **2.006 veces** y en cada una recorre las 30.010 citas; el plan lo dice con `loops=2006`. La version DESPUES es un `HashAggregate` sobre un solo recorrido. Aqui la diferencia si es de ordenes de magnitud —de segundos a decenas de milisegundos— y no depende de que haya indices, porque lo que se elimino no fue un escaneo: fueron 2.005 escaneos.

### Como calificar

- **7 pts — la version DESPUES elimina la correlacion.** 3 pts los dos `LEFT JOIN`, 2 pts el `GROUP BY d.id_dueno, d.nombre` y 2 pts **`COUNT(c.id_cita)` y no `COUNT(*)`**. Estos ultimos 2 pts son el corazon de la pregunta y se verifican con una sola consulta: los duenos 2001 a 2006 tienen que decir **0**, no 1.
- **3 pts — el `ORDER BY total_citas DESC, d.id_dueno` y el `LIMIT 20`.** El desempate no es cosmetico: hay 987 duenos empatados en 18 y sin el las filas 7 a 20 cambian entre corridas.
- **4 pts — los dos `EXPLAIN ANALYZE`** corren y se aprecia la diferencia de plan. El ancla verificable es el `loops=2006` del `SubPlan` en la version ANTES: quien lo cita, lo leyo.
- **6 pts — la prueba de equivalencia con `EXCEPT` en los dos sentidos devuelve cero filas.** 4 pts que este la prueba con las dos direcciones y 2 pts que el resultado sea cero. Un `EXCEPT` en un solo sentido vale 2 de los 6, y conviene explicar por que: `A EXCEPT B` vacio no prueba que B no tenga filas extra.
- **Se descuenta segun la rubrica** por usar `INNER JOIN` —que hace desaparecer a los seis duenos sin citas— o por omitir la verificacion. El primero es un error de resultado, no de rendimiento: el reporte que ve la clinica queda con 2.000 duenos en vez de 2.006.
- **Bono conceptual, sin puntos:** quien note que esta reescritura mejora sin necesidad de ningun indice —porque lo que se elimino no fue un escaneo sino 2.005 escaneos— entendio la diferencia entre las dos preguntas del taller. La pregunta 1 prepara el terreno para un indice; esta se arregla sola.

### Errores frecuentes y que hacer

- **`COUNT(*)` en vez de `COUNT(c.id_cita)`.** Es el error firmado de esta pregunta. Con `LEFT JOIN`, un dueno sin citas produce **una** fila llena de `NULL`, y `COUNT(*)` cuenta filas: reporta 1. `COUNT` de una columna ignora los `NULL` y reporta 0. El sintoma es exacto y facil de buscar: los seis ultimos duenos dicen 1.
- **`INNER JOIN` en vez de `LEFT JOIN`.** Mas rapido y **mal**: los seis duenos sin mascotas desaparecen y el reporte deja de cuadrar con el total de clientes de la clinica. Es el mismo principio de la pregunta 1 —optimizar no puede cambiar el resultado— y aqui el `EXCEPT` lo delata.
- **`GROUP BY d.id_dueno` sin `d.nombre`,** con `d.nombre` en el `SELECT`. PostgreSQL lo acepta porque `id_dueno` es llave primaria y determina funcionalmente el resto de la fila, asi que no se descuenta. Pero conviene advertirlo: en cuanto se agrupe por algo que **no** sea la llave, el mismo codigo falla con `column d.nombre must appear in the GROUP BY clause`.
- **Un solo `EXCEPT`.** `A EXCEPT B` vacio dice que A no tiene nada que B no tenga; no dice nada sobre las filas que B pueda tener de mas. El enunciado pide los dos sentidos y por eso las dos partes se unen con `UNION ALL`: una sola lectura, cero filas.
- **Comparar con `EXCEPT` incluyendo el `LIMIT 20`.** Entonces la prueba solo cubre 20 de las 2.006 filas y precisamente **excluye** a los seis duenos con cero, que son los que fallan. El enunciado dice «sin `LIMIT`» por esta razon exacta.
- **Recargar la pagina porque la version ANTES «se colgo».** No se colgo: son 2.006 ejecuciones de una consulta que recorre 30.010 filas, y en el navegador eso tarda. Vale la pena anunciarlo antes de que empiecen, porque el estudiante que recarga pierde el resto de sus respuestas.

---

## Pregunta 4 · Antipatrones de consulta en VetCare · 10 pts

### Clave y por que

La clave se lee del banco de la plataforma, asi que esta es la que se califica. La columna de la derecha es lo que hay que poder responderle al estudiante cuando pregunte.

|  | Opcion | Por que |
|---|---|---|
| **SI** | Envolver la columna en una funcion (to_char(fecha_hora,...) o EXTRACT) impide que el motor use un indice sobre esa columna: se pierde la sargabilidad. | **Correcta, y es el antipatron 3 de la pregunta 1.** *Sargable* viene de «**S**earch **ARG**ument **able**»: el motor solo puede usar un indice cuando la columna aparece **sola** a la izquierda del operador. En `to_char(fecha_hora, 'YYYY-MM-DD') = '2026-03-10'` el indice esta construido sobre `fecha_hora` y la comparacion es sobre otra cosa —el texto que devuelve la funcion—, asi que no hay nada que buscar. Se pierde dos veces: el motor calcula la funcion 30.010 veces y, ademas, se queda sin estadisticas para estimar. La forma correcta es el predicado de rango. |
| **SI** | SELECT * en un join de 4 tablas transporta columnas que nadie usa y encarece el ordenamiento y la red. | **Correcta.** En el join de cuatro tablas de la pregunta 1, `SELECT *` arrastra unas veinte columnas —con `id_mascota` repetido tres veces— cuando la pantalla usa seis. Ese peso se paga en cada etapa: en el ancho de la fila que viaja por los joins, en la memoria del `Sort` —y si no cabe, en un archivo temporal en disco— y en los bytes que salen hacia el cliente. Ademas rompe el codigo el dia que alguien agregue una columna a `cita`. |
| no | Optimizar una consulta puede cambiar el numero de filas que devuelve, siempre que sea mas rapida. | **Incorrecta, y es la mas importante de descartar de las seis.** Optimizar es hacer lo mismo mas rapido; si el resultado cambia, no se optimizo nada, se rompio la consulta y encima se rompio sin avisar. Por eso el taller exige la prueba de equivalencia dos veces: los dos `COUNT(*)` de la pregunta 1 —que valen 91— y el `EXCEPT` vacio de la pregunta 3. La velocidad no es un permiso para devolver otra cosa. |
| **SI** | Una subconsulta correlacionada en la lista de columnas se evalua una vez por fila del exterior; reescribirla como JOIN con GROUP BY suele bajar el costo un orden de magnitud. | **Correcta, y es la pregunta 3 entera.** La subconsulta de la lista de columnas se evalua una vez por fila del exterior, y el plan lo dice sin ambiguedad: `loops=2006`. Reescrita como `LEFT JOIN` + `GROUP BY` pasa a una sola pasada con un `HashAggregate`, y la mejora es de ordenes de magnitud sin necesidad de ningun indice, porque lo que se elimino no fue un escaneo sino 2.005 escaneos. |
| no | Cambiar la coma por JOIN ... ON por si solo hace la consulta mas rapida, porque el motor usa otro algoritmo. | **Incorrecta,** y es la que separa a quien entendio de quien memorizo la lista de antipatrones. En PostgreSQL, `FROM a, b WHERE a.x = b.x` y `FROM a JOIN b ON a.x = b.x` producen **exactamente el mismo plan**: el motor las normaliza a la misma representacion interna. Cambiar la coma por `JOIN ... ON` **si** vale la pena, pero por otras dos razones: separa la condicion de union de la condicion de filtro, y hace evidente cuando falta un `ON` —que es como se producen los productos cartesianos accidentales de 30.010 x 5.008 filas—. Se gana legibilidad y seguridad, no milisegundos. |
| **SI** | EXPLAIN muestra el plan estimado y EXPLAIN ANALYZE lo ejecuta de verdad y reporta filas y tiempos reales; comparar estimado vs real revela estadisticas desactualizadas. | **Correcta, y es la herramienta de la pregunta 2.** `EXPLAIN` muestra el plan **estimado** y no ejecuta nada; `EXPLAIN ANALYZE` lo ejecuta de verdad y reporta `actual rows` y `actual time` al lado de las estimaciones. Comparar las dos columnas es el diagnostico mas rentable que existe: el `rows=1` estimado contra las 91 reales de la version ANTES avisa de que el motor esta ciego sobre ese filtro, y una desviacion parecida en una consulta normal casi siempre significa `ANALYZE` sin correr o estadisticas viejas. |

### Como calificar

- **10 pts con las 4 correctas marcadas y ninguna incorrecta**, con puntaje proporcional por acierto parcial, tal como dice la rubrica. La plataforma calcula el parcial y la clave se lee del banco.
- **La opcion del `JOIN` es el discriminador de la pregunta.** Marcarla es el error mas frecuente y el mas comprensible, porque el taller obliga a cambiar las comas por `JOIN`. La devolucion tiene que ser precisa: el cambio es correcto y obligatorio, pero **no** por velocidad; el plan es identico. Es por legibilidad y por no perder un `ON`.
- **La opcion de «puede cambiar el numero de filas» no admite matices.** Si alguien la marca, la conversacion no es sobre optimizacion sino sobre que significa que una consulta sea correcta. Vale la pena mirar si esa misma persona omitio la prueba de equivalencia en las preguntas 1 y 3: casi siempre van juntas.
- Si mas de un tercio del grupo falla la de sargabilidad, conviene abrir la Clase 7 mostrando en vivo el mismo `EXPLAIN` con y sin el indice sobre `fecha_hora`: es un minuto y deja la idea fijada mejor que la definicion.

### Errores frecuentes y que hacer

- **Marcar la del `JOIN` como correcta.** Se corrige con el dato, no con la teoria: los dos `EXPLAIN` son iguales. Y se aprovecha para dar la razon real del cambio, que es la que va al informe.
- **Marcar la de «puede cambiar el resultado».** Es la unica de las seis que invalida el trabajo del taller completo. La devolucion mas eficaz es devolverle su propio numero: la version ANTES y la DESPUES de su pregunta 1 **tienen** que decir 91 las dos.
- **No marcar la del `SELECT *`,** por pensar que «solo son unas columnas mas». El costo no esta en leerlas: esta en acarrearlas por tres joins y por un `Sort`. Es facil de mostrar con el `width=` que aparece en cada nodo del plan, y ese numero esta en su propia evidencia de la pregunta 2.
- **No marcar la de `EXPLAIN` contra `EXPLAIN ANALYZE`,** casi siempre por no haber leido la segunda mitad de la frase —la de estimado contra real—. Es la parte que mas sirve en el trabajo: la brecha entre las dos columnas es el sintoma de estadisticas desactualizadas.

---

## Pregunta 5 · Justificacion tecnica del antes/despues (media pagina) · 20 pts

### Respuesta esperada

**1. Consulta elegida y para que sirve en Huellitas.** La agenda del dia: la pantalla que recepcion abre al llegar y vuelve a consultar cada vez que entra un paciente, de modo que se ejecuta del orden de **50 a 80 veces por jornada** y siempre con alguien esperando delante del mostrador. Es la consulta mas ejecutada del PI y por eso es la que se optimiza primero: mejorar un reporte mensual habria sido mas facil y no le habria servido a nadie.

**2. Tres cambios concretos.**

- **Cambio 1 — de `to_char(fecha_hora, 'YYYY-MM-DD') = '2026-03-10'` a un predicado de rango `>= '2026-03-10 00:00:00' AND < '2026-03-11 00:00:00'`.** *Por que mejora:* deja la columna **sargable**, es decir sola a la izquierda del operador, y con eso el motor recupera dos cosas: deja de calcular una funcion 30.010 veces y vuelve a poder usar el histograma de `fecha_hora` para estimar la **cardinalidad** del filtro. *Evidencia:* en el plan ANTES la linea del `Seq Scan` dice `rows=1` estimadas contra `actual rows=91`; en el plan DESPUES dice `rows=90` contra 91. El error de estimacion paso de un factor de 91 a menos del 2 %, y con una estimacion correcta el planeador elige bien la forma de los joins en vez de dimensionarlos para una sola fila.
- **Cambio 2 — de `SELECT *` a seis columnas proyectadas.** *Por que mejora:* la **proyeccion** reduce el ancho de la fila que atraviesa los tres joins y el `Sort`. `SELECT *` sobre cuatro tablas trae unas veinte columnas, incluidos tres `id_mascota` y datos que la pantalla no muestra —telefono, correo, fecha de nacimiento—, y todo eso se copia en cada etapa y se transporta al cliente. *Evidencia:* el `width=` del nodo raiz baja de mas de 150 bytes a unas decenas, y con el baja el trabajo del `Sort`, que es el nodo que se lleva la memoria.
- **Cambio 3 — de la subconsulta correlacionada del reporte de duenos a `LEFT JOIN` + `GROUP BY`.** *Por que mejora:* baja el **numero de pasadas sobre la tabla** de 2.006 a 1. La subconsulta estaba en la lista de columnas, asi que se ejecutaba una vez por cada dueno y cada vez recorria las 30.010 citas. *Evidencia:* en el plan ANTES el `SubPlan` aparece con `loops=2006`; en el plan DESPUES ese nodo **no existe** y en su lugar hay un solo `HashAggregate`. Es la unica de las tres mejoras que es de ordenes de magnitud, y es la unica que no necesita ningun indice para conseguirlo.

**3. Que NO cambio.** El resultado. La agenda del 2026-03-10 devuelve **91 filas** en las dos versiones, verificado con un `COUNT(*)` de cada una en la misma corrida. El reporte de duenos devuelve los mismos 2.006 pares `(id_dueno, total_citas)`, verificado con `EXCEPT` en **ambos sentidos**: cero filas. La prueba en un solo sentido no habria servido, porque no detecta filas de mas en el segundo conjunto. Y hay un caso que la prueba protege expresamente: los seis duenos sin citas —los id 2001 a 2006— siguen apareciendo con **0**, que es lo que se pierde con un `INNER JOIN` o se falsea con un `COUNT(*)`.

**4. Que sigue: el indice de la Clase 7.** `CREATE INDEX ix_cita_fecha_estado ON cita (fecha_hora, estado);`, y en ese orden. La razon esta en el propio plan de hoy: la version DESPUES sigue haciendo un `Seq Scan` de las 30.010 filas y descartando 29.919, porque no hay nada que la ayude a llegar directo al dia. Con el indice, ese nodo deberia convertirse en un `Index Scan` sobre las ~150 citas del dia, y ademas el `Sort` deberia desaparecer, porque el indice ya entrega las filas ordenadas por `fecha_hora` —lo que hace que el `LIMIT 50` por fin sirva de algo—. El orden de las columnas importa: `fecha_hora` primero porque es el filtro de rango, y `estado` despues, para poder afinar sin volver a la tabla. La hipotesis se escribe hoy y se **mide** la clase que viene; si el motor decide que no le conviene usarlo, eso tambien es un resultado.

**5. Limites de la medicion, honestamente.** Se midio sobre PostgreSQL compilado a WebAssembly y corriendo **dentro del navegador**, con 30.010 citas, un solo usuario y **sin concurrencia**. Cuatro cosas cambiarian en un servidor real con millones de citas y varios usuarios:

- **Los tiempos absolutos no se pueden trasladar.** El factor de 2,9x medido aqui es una comparacion entre dos consultas en el mismo entorno, no una prediccion de nada. Entre dos corridas seguidas en el navegador la diferencia ya puede ser del doble.
- **La escala favorece a la version optimizada.** Con 30.010 filas la tabla entera cabe en memoria y un `Seq Scan` es baratisimo; con millones de citas no cabe, hay lectura de disco real y ahi la diferencia entre recorrer todo y usar un indice deja de ser de 3x. Lo mismo con la subconsulta correlacionada: 2.006 iteraciones son lentas, 200.000 son inviables.
- **No se midio el costo de escribir.** Cada indice que se agregue en la Clase 7 hay que mantenerlo en cada `INSERT` de `sp_agendar_cita`. En este entorno, sin concurrencia, ese costo es invisible; en produccion, con 150 citas nuevas al dia y varios indices, no lo es.
- **No hubo bloqueos ni competencia por recursos.** Con varios usuarios, la consulta lenta no solo es lenta para quien la lanza: retiene conexiones y memoria de ordenamiento que le hacen falta al resto. Ese efecto es exactamente el que este entorno **no puede** reproducir, y es el argumento principal para optimizar la consulta que se ejecuta 80 veces al dia antes que la que se ejecuta una vez al mes.

*(La opcion `BUFFERS` se uso donde el entorno la acepto; donde no, se corrio `EXPLAIN ANALYZE` a secas, tal como autoriza el enunciado.)*

**Archivos del PI:** `06_opt_antes.sql` y `06_opt_despues.sql` en la carpeta del proyecto, mas los tres planes guardados como texto en `/informe/06-planes.txt`. El plan sirve de evidencia solo si queda guardado: en la Clase 7 hay que poder comparar contra el de hoy.

### Como calificar

- **3 pts — la seccion 1, y 3 pts la seccion 3.** La 1 necesita la pantalla concreta y una **frecuencia**; «se usa mucho» no vale. La 3 necesita la afirmacion de equivalencia **y** el metodo con su resultado (91 = 91, `EXCEPT` vacio). Con los 9 de la seccion 2, los 3 de la 4 y los 2 de la 5, el desglose suma los 20 puntos de la pregunta.
- **9 pts — los tres cambios, 3 pts cada uno.** Cada cambio se parte en tres: 1 pt que se diga **que** se cambio, 1 pt **por que** mejora con el vocabulario correcto —sargabilidad, proyeccion, cardinalidad, numero de pasadas—, y 1 pt la **evidencia anclada al plan**: un nodo que aparecio o desaparecio, un `loops=`, un `rows=` estimado contra el real, un tiempo. Un cambio sin evidencia vale 2 de 3; una evidencia que no se puede verificar en el plan vale 0 de ese punto.
- **3 pts — la seccion 4, el indice propuesto.** 2 pts el `CREATE INDEX` concreto sobre las columnas correctas y 1 pt **la razon tomada de su propio plan** («sigue habiendo un `Seq Scan` que descarta 29.919 filas»). Un indice propuesto «porque acelera las consultas» vale 1 de 3.
- **2 pts — la seccion 5 reconoce los limites del entorno,** nombrando al menos dos: el volumen, la ausencia de concurrencia, el navegador como entorno de medicion, o el costo de escritura que no se midio. La rubrica pide honestidad y aqui se premia: **un informe que admite que midio poco vale mas que uno que finge haber medido produccion.**
- **Vocabulario tecnico, transversal.** La rubrica lo exige de forma explicita. Se descuenta medio punto por cambio cuando la justificacion es circular —«mejora porque es mas eficiente»— aunque la evidencia este bien citada: la seccion existe para explicar el mecanismo.
- **Extension.** Media pagina. Se califica que las 5 secciones esten con contenido verificable; no se premia la longitud. Y se verifica lo ultimo del enunciado, que es facil de olvidar: **los dos archivos `.sql` guardados** en la carpeta del PI.

### Errores frecuentes y que hacer

- **Justificaciones circulares.** «Cambie `SELECT *` porque es mas eficiente» repite la pregunta. La respuesta es el mecanismo: transporta columnas que nadie usa a traves de tres joins y de un `Sort`. Es el descuento mas frecuente de esta pregunta.
- **Evidencia que no se puede verificar en el plan.** «El tiempo bajo mucho» o «se ve mas rapido» no son evidencia. Las que si lo son, y estan en su propia pregunta 2: `Rows Removed by Filter: 29919`, `loops=2006`, `rows=1` contra `actual rows=91`, el `width=` que bajo.
- **Afirmar que el `Seq Scan` desaparecio.** No desaparecio y no podia: en esta base no hay ningun indice sobre `fecha_hora`. Cuando aparece esta frase, casi siempre la seccion 4 tambien esta mal, porque el estudiante ya cree que el problema esta resuelto y entonces el indice de la Clase 7 le sobra.
- **Proponer un indice sobre `estado`,** o sobre las tres columnas en cualquier orden, sin argumento. `estado` tiene tres valores y el 60 % de las filas son `PROGRAMADA`: un indice sobre una columna asi casi nunca se usa, porque leer el 60 % de la tabla por el indice es mas caro que recorrerla. La columna selectiva es `fecha_hora`, y va primera.
- **Declarar la equivalencia sin haberla medido.** «El resultado es el mismo» sin el 91 = 91 ni el `EXCEPT` vacio es una promesa, no una verificacion. Es exactamente lo que la opcion falsa de la pregunta 4 pone a prueba.
- **Saltarse la seccion 5** o escribirla como formalidad («los resultados podrian variar»). Se pide algo concreto: que **si** cambiaria con millones de citas y con varios usuarios. Sin eso, el informe presenta como conclusion general una medicion de un solo usuario en un navegador.

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**¿Que significa exactamente «sargable»?**

Viene de «**S**earch **ARG**ument **able**»: que el motor pueda usar la condicion como argumento de busqueda en un indice. La regla practica es de una linea: **la columna tiene que quedar sola a la izquierda del operador.** `fecha_hora >= X` es sargable; `to_char(fecha_hora, ...) = X`, `DATE(fecha_hora) = X` y `EXTRACT(DAY FROM fecha_hora) = X` no lo son, porque el indice esta hecho sobre la columna y la comparacion es contra el resultado de una funcion. Cambiar `to_char` por `DATE()` no arregla nada: sigue habiendo una funcion envolviendo la columna.

**Corregi el predicado y el `Seq Scan` sigue ahi. ¿Hice algo mal?**

No, esta correcto, y darse cuenta es el mejor resultado del taller. En **esta** base no hay ningun indice sobre `fecha_hora`, asi que no existe alternativa al recorrido completo: las dos versiones leen las 30.010 filas y descartan las mismas 29.919. Lo que si ganaste hoy son tres cosas medibles: 60.020 llamadas a funcion que ya no se hacen, filas mucho mas angostas viajando por los joins y por el `Sort`, y una estimacion correcta —de `rows=1` a `rows=90` contra 91 reales—. La sargabilidad es la condicion **previa** para que el indice de la Clase 7 pueda servir: si dejas el `to_char`, el indice se crea y el motor lo ignora.

**¿Por que la version ANTES estima `rows=1` si devuelve 91 filas?**

Porque el motor no tiene estadisticas sobre `to_char(fecha_hora, ...)` ni sobre `upper(estado)` —solo las tiene sobre las columnas desnudas—, asi que aplica una selectividad por omision del 0,5 % a cada condicion de igualdad. La cuenta sale exacta: 30.010 x 0,005 x 0,005 = 0,75, que se redondea a 1. Y esa estimacion equivocada no es cosmetica: el planeador dimensiona los joins creyendo que va a unir **una** cita. Comparar `rows=` estimadas contra `actual rows=` es el diagnostico mas rentable que existe; en una consulta normal, una brecha asi suele significar que falta correr `ANALYZE`.

**¿`JOIN ... ON` es mas rapido que separar las tablas con comas?**

No. En PostgreSQL las dos formas producen **exactamente el mismo plan**: el motor las normaliza a la misma representacion interna. Aun asi el cambio es obligatorio en el taller y vale la pena en el trabajo, por dos razones que no son de velocidad. Una: separa la condicion de **union** de la condicion de **filtro**, que es la diferencia entre leer una consulta y descifrarla. Dos: cuando falta un `ON`, el motor te avisa; cuando falta una condicion en un `WHERE` con comas, te devuelve un producto cartesiano de 30.010 x 5.008 filas sin decir nada.

**¿Por que `COUNT(c.id_cita)` y no `COUNT(*)`?**

Por los duenos sin citas, que son seis en esta base: los id 2001 a 2006. Con `LEFT JOIN`, un dueno sin citas **si** produce una fila —una fila con todas las columnas de `cita` en `NULL`— y `COUNT(*)` cuenta filas: reporta **1**. `COUNT` de una columna ignora los `NULL` y reporta **0**, que es la verdad. Es la razon por la que la prueba de la pregunta 3 se hace con `EXCEPT`: si usaste `COUNT(*)`, el `EXCEPT` te devuelve exactamente esas seis filas.

**¿Por que el `EXCEPT` tiene que ir en los dos sentidos?**

Porque `EXCEPT` no es simetrico. `A EXCEPT B` vacio solo dice que A no tiene ninguna fila que B no tenga; no dice nada sobre filas que B pueda tener de mas. Para probar que los dos conjuntos son **iguales** hacen falta las dos direcciones, y lo mas comodo es unirlas con `UNION ALL` para leer un solo resultado: cero filas. Y ojo con el detalle que el enunciado subraya: la comparacion va **sin `LIMIT`**, porque el `LIMIT 20` excluye justamente a los seis duenos con cero, que son los que fallan.

**La consulta de la pregunta 3 lleva un minuto corriendo. ¿Se colgo?**

No. Es una subconsulta correlacionada ejecutandose **2.006 veces**, y cada una recorre las 30.010 citas unidas con las 5.008 mascotas: son decenas de millones de filas tocadas, dentro de un motor que corre en el navegador. Espera. **No recargues la pagina**, porque perderias las respuestas de las otras preguntas. Y esa espera es el argumento de la pregunta: cuando la version DESPUES conteste en decenas de milisegundos, la diferencia la vas a haber sentido, no solo leido.

**Mi factor de mejora en la pregunta 2 es de 1,8x. ¿Esta mal?**

Esta bien, y un 1,8x medido vale mas que un 50x inventado. En esta base, sin indices, el factor real esta entre 1,5x y 3x, y ya sabes por que: las dos versiones recorren las 30.010 filas. Escribelo asi en el informe, con los dos tiempos que lo sustentan y con la explicacion. Dos advertencias para medir bien: alterna las corridas —ANTES, DESPUES, ANTES, DESPUES— y quedate con la segunda de cada una, porque la primera paga el arranque del motor; y no compares tu numero con el del compañero de al lado, porque su maquina es otra.

---

## Cierre de la clase

- Al terminar, cada estudiante debe tener: la agenda del dia reescrita con los cuatro antipatrones corregidos y las **91 filas** confirmadas en las dos versiones; los tres `EXPLAIN` con su tabla de lectura y un factor de mejora sustentado; el reporte de duenos en una sola pasada con el `EXCEPT` de los dos sentidos devolviendo **cero filas**; las cuatro afirmaciones correctas de la pregunta 4; y la justificacion tecnica con el indice propuesto y los limites de la medicion, mas `06_opt_antes.sql` y `06_opt_despues.sql` guardados en la carpeta del PI.
- Lo que hay que verificar antes de cerrar la sesion son **tres numeros**, y los tres se leen sin ejecutar nada. Que el conteo diga **91** en las dos versiones —150 significa que falta el filtro de estado, 0 significa que se uso `BETWEEN` con literales de fecha—. Que los seis duenos finales digan **0** y no 1 —si dicen 1, fue `COUNT(*)`; si no aparecen, fue `INNER JOIN`—. Y que la tabla de lectura del plan traiga el **29.919** de `Rows Removed by Filter`, que es el numero que no se puede inventar. Proyectar una entrega voluntaria y buscar esos tres numeros toma dos minutos.
- Dejar dicho en voz alta lo que sigue, porque esta clase termina a proposito con una pregunta abierta. Hoy quedo demostrado que la consulta corregida **sigue leyendo las 30.010 filas**: la sargabilidad por si sola no evito el recorrido completo, solo dejo la puerta abierta. La Clase 7 crea el indice sobre `(fecha_hora, estado)` y vuelve a medir el mismo plan, con dos hipotesis escritas hoy que hay que confirmar o desmentir: que el `Seq Scan` se convierta en `Index Scan` sobre unas 150 filas, y que el `Sort` desaparezca porque el indice ya entrega las filas ordenadas. Y con la contraparte que nadie quiere oir: ese indice hay que mantenerlo en cada `INSERT` de `sp_agendar_cita`, asi que la Clase 7 tambien es sobre lo que cuesta.

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. El motor de la plataforma es PostgreSQL (PGlite en el navegador), no Oracle.
