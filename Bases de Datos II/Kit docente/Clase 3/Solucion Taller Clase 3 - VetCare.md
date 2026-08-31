# Solucion del taller · Clase 3 · Procedimientos almacenados de VetCare en PL/pgSQL

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** Los dos procedimientos de negocio del PI escritos en PL/pgSQL y corriendo: `sp_agendar_cita` con sus tres validaciones y `sp_registrar_consulta` con sus cuatro, la bateria de pruebas que demuestra que las validaciones no dejan basura en la tabla, la distincion entre PROCEDURE y FUNCTION resuelta con el criterio correcto, y el contrato de los dos procedimientos documentado tal como lo consumira la aplicacion de Huellitas.

> **El motor es PostgreSQL, no Oracle,** y en esta clase la diferencia se paga caro: tres de las cinco preguntas son SQL que corre. La sintaxis es `CREATE PROCEDURE ... LANGUAGE plpgsql AS $proc$ ... $proc$;` y no lleva `IS`, ni `VARCHAR2`, ni `NUMBER`, ni `RAISE_APPLICATION_ERROR`, ni la barra `/` final. `RAISE EXCEPTION 'texto %', variable;` es el equivalente exacto de `RAISE_APPLICATION_ERROR`. Un detalle del entorno que conviene anunciar antes de arrancar: en ExamLab **cada pregunta arranca con su propia base sembrada**, asi que la pregunta 2 ya trae `sp_agendar_cita` creado —la version de referencia— y el estudiante no depende de que su pregunta 1 haya quedado bien. Y una recomendacion que ahorra la mitad de los reportes de error: escribir `CREATE OR REPLACE PROCEDURE`, para que el segundo intento no choque con «ya existe».

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 3 - Procedimientos almacenados/Taller PI - Clase 3 - VetCare.docx`
- Configuracion en la plataforma: `Kit docente/Clase 3/Taller en ExamLab - Clase 3 (configuracion).md`
- Caso de estudio: `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
- Hito del PI: >=1 procedimiento de negocio (agendar cita / registrar consulta)
- Entregable: 2 procedimientos en PL/pgSQL corriendo en ExamLab + bateria de pruebas con su tabla resultado_prueba + contrato del proc (6 bloques)
- **Estas preguntas: 100 puntos** en 5 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 1 | Implementar sp_agendar_cita en PL/pgSQL | `bd_sql` | 35 |
| 2 | Bateria de pruebas del procedimiento (caso OK + casos de error) | `bd_sql` | 25 |
| 3 | PROCEDURE o FUNCTION en PostgreSQL | `cerrada` | 10 |
| 4 | sp_registrar_consulta: el segundo procedimiento de negocio | `bd_sql` | 15 |
| 5 | Contrato de los procedimientos para la futura aplicacion | `abierta` | 15 |

---

## Pregunta 1 · Implementar sp_agendar_cita en PL/pgSQL · 35 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- sp_agendar_cita: la regla de negocio del PI, escrita una sola vez y
    -- dentro de la base. OR REPLACE para poder corregir y volver a ejecutar
    -- sin borrar antes.
    -- =====================================================================
    CREATE OR REPLACE PROCEDURE sp_agendar_cita(
      p_id_mascota     INT,
      p_id_veterinario INT,
      p_fecha_hora     TIMESTAMP
    )
    LANGUAGE plpgsql
    AS $proc$
    DECLARE
      v_activa  CHAR(1);
      v_ocupado INT;
    BEGIN
      -- 1) ¿Existe la mascota? El SELECT ... INTO deja FOUND en falso cuando no
      --    devolvio ninguna fila, y es la unica forma limpia de distinguir
      --    "no existe" de "existe y esta inactiva". Ojo: esto solo funciona
      --    porque el SELECT trae una columna, no un COUNT.
      SELECT activa INTO v_activa
        FROM mascota
       WHERE id_mascota = p_id_mascota;

      IF NOT FOUND THEN
        RAISE EXCEPTION 'ERROR: la mascota % no existe', p_id_mascota;
      END IF;

      -- 2) La regla de negocio del PI: una mascota inactiva no agenda. Se
      --    escribe <> 'S' y no = 'N' a proposito: si manana el CHECK admite
      --    un tercer estado, la regla sigue siendo correcta sin tocarla.
      IF v_activa <> 'S' THEN
        RAISE EXCEPTION 'ERROR: la mascota % esta inactiva; no se agenda cita',
                        p_id_mascota;
      END IF;

      -- 3) ¿El veterinario tiene la franja libre? Una cita CANCELADA libera la
      --    franja, por eso se excluye del conteo. Aqui NO se puede usar
      --    IF NOT FOUND: un COUNT(*) siempre devuelve una fila, asi que FOUND
      --    seria verdadero incluso con cero citas. Se compara el numero.
      SELECT COUNT(*) INTO v_ocupado
        FROM cita
       WHERE id_veterinario = p_id_veterinario
         AND fecha_hora     = p_fecha_hora
         AND estado        <> 'CANCELADA';

      IF v_ocupado > 0 THEN
        RAISE EXCEPTION 'ERROR: el veterinario % ya tiene cita en %',
                        p_id_veterinario, p_fecha_hora;
      END IF;

      -- 4) Caso valido. El estado se escribe explicito aunque la tabla lo
      --    tenga por omision: el procedimiento es el contrato y no debe
      --    depender de un DEFAULT que alguien puede cambiar manana.
      INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
      VALUES (p_id_mascota, p_id_veterinario, p_fecha_hora, 'PROGRAMADA');
    END;
    $proc$;

    -- =====================================================================
    -- Demostracion pedida por el enunciado: el caso valido.
    -- =====================================================================
    CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');

    SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado
      FROM cita
     ORDER BY id_cita DESC
     LIMIT 3;
```

### Salida esperada

```
CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');   -- CALL, sin filas devueltas

    SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado ...   -- 3 filas

     id_cita | id_mascota | id_veterinario |     fecha_hora      |   estado
    ---------+------------+----------------+---------------------+-------------
          11 |          1 |              2 | 2026-09-15 10:00:00 | PROGRAMADA
          10 |          6 |              1 | 2026-09-10 09:00:00 | ATENDIDA
           9 |          4 |              4 | 2026-09-10 08:00:00 | PROGRAMADA

    La comprobacion de un golpe es el 11: la base venia con 10 citas sembradas,
    asi que el id 11 y el estado PROGRAMADA en la primera fila demuestran que el
    procedimiento inserto y que lo hizo con el estado correcto. Si la primera fila
    dice 10, el CALL no inserto nada y hay que revisar si alguna validacion esta
    disparando de mas.

    Las tres excepciones, para pegarlas al revisar una entrega dudosa (cada una
    aborta el script, por eso van de a una):

      CALL sp_agendar_cita(99, 2, TIMESTAMP '2026-09-16 10:00:00');
      -- ERROR:  ERROR: la mascota 99 no existe

      CALL sp_agendar_cita(3, 2, TIMESTAMP '2026-09-16 10:00:00');
      -- ERROR:  ERROR: la mascota 3 esta inactiva; no se agenda cita

      CALL sp_agendar_cita(2, 1, TIMESTAMP '2026-09-01 08:00:00');
      -- ERROR:  ERROR: el veterinario 1 ya tiene cita en 2026-09-01 08:00:00

    Y la que confirma que CANCELADA libera la franja: el veterinario 3 tiene la cita
    4 CANCELADA el 2026-09-02 08:30:00, asi que esta debe funcionar.

      CALL sp_agendar_cita(1, 3, TIMESTAMP '2026-09-02 08:30:00');
      -- CALL (sin error): inserta la cita 12
```

### Como calificar

- **6 pts — el procedimiento se crea sin error.** `CREATE PROCEDURE` (o `CREATE OR REPLACE PROCEDURE`) con `LANGUAGE plpgsql`, dollar-quoting y los **3 parametros en el orden y con los tipos pedidos**: `INT`, `INT`, `TIMESTAMP`. Es el piso de la pregunta: si el motor no lo acepta, los 21 pts de las validaciones no se pueden evaluar.
- **21 pts — las tres validaciones, 7 pts cada una.** Por validacion: 4 pts que la condicion sea la correcta, 2 pts el `RAISE EXCEPTION` y 1 pt que el mensaje sea informativo, es decir que incluya el valor con `%`. La tercera es la que mas se pierde: tiene que excluir `'CANCELADA'`, porque una cita cancelada **libera** la franja.
- **5 pts — el `INSERT` del caso valido** con estado `'PROGRAMADA'` y en las 4 columnas. Se descuentan 2 si el estado se deja al `DEFAULT` de la tabla en vez de escribirlo: funciona, pero el procedimiento deja de ser autocontenido.
- **3 pts — la demostracion.** El `CALL` corre y el `SELECT` final evidencia la fila nueva. La verificacion es la de la salida de arriba: `id_cita = 11` en la primera fila. Un `SELECT` que no muestre la cita nueva no evidencia nada.
- **Cero sintaxis Oracle.** Es explicito en la rubrica y se aplica sobre los 6 pts del primer renglon: `IS` en vez de `AS`, `VARCHAR2`, `NUMBER`, `RAISE_APPLICATION_ERROR` o `/` final impiden que el motor cree el procedimiento, asi que el efecto es automatico. No hace falta un descuento aparte.
- **Bono conceptual, sin puntos, y vale la pena buscarlo:** si el estudiante escribe en un comentario que la validacion 3 **no** garantiza la unicidad con dos sesiones simultaneas —dos llamadas pueden contar cero al mismo tiempo y las dos insertar—, entendio el limite real de validar leyendo antes de escribir. Es el problema que abre la Clase 10 y se resuelve con una restriccion unica, no con mas `IF`.

### Errores frecuentes y que hacer

- **`IF NOT FOUND` despues de un `SELECT COUNT(*) INTO`.** No falla, no avisa, y la validacion queda muerta: un `COUNT` siempre devuelve una fila, asi que `FOUND` es verdadero incluso cuando el conteo es cero. Es el error mas fino de la pregunta y el que hay que explicar en voz alta al grupo entero: `FOUND` sirve con `SELECT columna INTO`, no con agregados.
- **Olvidar `AND estado <> 'CANCELADA'`** en la validacion del veterinario. La consecuencia es que una franja cancelada queda bloqueada para siempre y la clinica pierde una hora de agenda por cada cancelacion. Se detecta con el `CALL` del veterinario 3 el `2026-09-02 08:30:00`, que debe funcionar.
- **`RAISE EXCEPTION 'ERROR: la mascota ' || p_id_mascota || ' no existe';`** Concatenar en vez de usar `%`. Funciona, pero se descuenta el punto del mensaje informativo si la concatenacion falla con `NULL`: cualquier concatenacion con `NULL` da `NULL` y el mensaje sale vacio. Con `%` el motor imprime `<NULL>` y el mensaje sigue siendo legible.
- **Validar el veterinario antes que la mascota** o mezclar las tres condiciones en un solo `IF ... OR ...`. Corre, pero el mensaje ya no dice cual regla se violo, y la aplicacion de la Clase 12 no puede decidir que hacer. El orden del enunciado es el orden en que la recepcionista necesita las respuestas.
- **Comprobar la existencia con `SELECT COUNT(*) INTO v_existe` y luego el estado con un segundo `SELECT`.** No esta mal y no se descuenta, pero son dos viajes a la tabla para una sola pregunta. Vale senalar la version de arriba: un `SELECT activa INTO` resuelve existencia y estado a la vez.
- **Terminar el bloque con `/`** o abrirlo con `AS $$ DECLARE ... BEGIN ... END; $$` sin etiqueta. La barra es de la consola de Oracle y aqui es un error de sintaxis; `$$` sin etiqueta funciona, pero `$proc$` es mas seguro cuando el cuerpo contiene a su vez cadenas con `$`.

---

## Pregunta 2 · Bateria de pruebas del procedimiento (caso OK + casos de error) · 25 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- P1 - CASO VALIDO: mascota 1 (Firulais, activa), vet 2, franja libre.
    -- Aqui el exito es que NO haya excepcion.
    -- =====================================================================
    DO $$
    BEGIN
      CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-20 08:00:00');
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P1 mascota activa', 'OK: cita creada', 'OK: cita creada', TRUE);
    EXCEPTION WHEN OTHERS THEN
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P1 mascota activa', 'OK: cita creada', SQLERRM, FALSE);
    END $$;

    -- =====================================================================
    -- P2 - MASCOTA INACTIVA: mascota 3 (Rocky). Aqui el exito es que SI haya
    -- excepcion, y ademas que sea LA excepcion esperada. Por eso no basta
    -- WHEN OTHERS: se verifica el texto. Si el procedimiento fallara por
    -- cualquier otra razon -- un typo en el nombre de una columna -- un
    -- WHEN OTHERS a secas lo reportaria como prueba superada.
    -- =====================================================================
    DO $$
    BEGIN
      CALL sp_agendar_cita(3, 2, TIMESTAMP '2026-09-21 08:00:00');
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P2 mascota inactiva', 'EXCEPCION: mascota inactiva',
              'NO lanzo excepcion: la cita se creo', FALSE);
    EXCEPTION WHEN OTHERS THEN
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P2 mascota inactiva', 'EXCEPCION: mascota inactiva',
              SQLERRM, SQLERRM ILIKE '%inactiva%');
    END $$;

    -- =====================================================================
    -- P3 - MASCOTA INEXISTENTE: id 99.
    -- =====================================================================
    DO $$
    BEGIN
      CALL sp_agendar_cita(99, 2, TIMESTAMP '2026-09-22 08:00:00');
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P3 mascota inexistente', 'EXCEPCION: mascota no existe',
              'NO lanzo excepcion: la cita se creo', FALSE);
    EXCEPTION WHEN OTHERS THEN
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P3 mascota inexistente', 'EXCEPCION: mascota no existe',
              SQLERRM, SQLERRM ILIKE '%no existe%');
    END $$;

    -- =====================================================================
    -- P4 - VETERINARIO OCUPADO: vet 1 el 2026-09-01 08:00:00, franja que la
    -- cita 1 ya tiene PROGRAMADA.
    -- =====================================================================
    DO $$
    BEGIN
      CALL sp_agendar_cita(2, 1, TIMESTAMP '2026-09-01 08:00:00');
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P4 veterinario ocupado', 'EXCEPCION: veterinario ocupado',
              'NO lanzo excepcion: la cita se creo', FALSE);
    EXCEPTION WHEN OTHERS THEN
      INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
      VALUES ('P4 veterinario ocupado', 'EXCEPCION: veterinario ocupado',
              SQLERRM, SQLERRM ILIKE '%ya tiene cita%');
    END $$;

    -- =====================================================================
    -- CIERRE 1: el tablero de la bateria.
    -- =====================================================================
    SELECT caso, esperado, obtenido, paso
      FROM resultado_prueba
     ORDER BY id_prueba;

    -- =====================================================================
    -- CIERRE 2: la prueba de que las validaciones no dejaron basura. Se mira
    -- el total y, sobre todo, los tres conteos que deben dar cero.
    -- =====================================================================
    SELECT (SELECT COUNT(*) FROM cita)                                AS citas_totales,
           (SELECT COUNT(*) FROM cita
             WHERE fecha_hora = TIMESTAMP '2026-09-20 08:00:00')      AS de_p1_debe_ser_1,
           (SELECT COUNT(*) FROM cita WHERE id_mascota = 3)           AS de_p2_debe_ser_0,
           (SELECT COUNT(*) FROM cita
             WHERE fecha_hora = TIMESTAMP '2026-09-22 08:00:00')      AS de_p3_debe_ser_0,
           (SELECT COUNT(*) FROM cita
             WHERE id_veterinario = 1
               AND fecha_hora = TIMESTAMP '2026-09-01 08:00:00')      AS de_p4_debe_ser_1;
```

### Salida esperada

```
SELECT caso, esperado, obtenido, paso FROM resultado_prueba ORDER BY id_prueba;  -- 4 filas

              caso          |           esperado            |                        obtenido                         | paso
    ------------------------+-------------------------------+---------------------------------------------------------+------
     P1 mascota activa      | OK: cita creada               | OK: cita creada                                         | t
     P2 mascota inactiva    | EXCEPCION: mascota inactiva   | ERROR: la mascota 3 esta inactiva; no se agenda cita     | t
     P3 mascota inexistente | EXCEPCION: mascota no existe  | ERROR: la mascota 99 no existe                          | t
     P4 veterinario ocupado | EXCEPCION: veterinario ocupado| ERROR: el veterinario 1 ya tiene cita en 2026-09-01 ...  | t

    SELECT ... conteos ...  -- 1 fila

     citas_totales | de_p1_debe_ser_1 | de_p2_debe_ser_0 | de_p3_debe_ser_0 | de_p4_debe_ser_1
    ---------------+------------------+------------------+------------------+------------------
                11 |                1 |                0 |                0 |                1

    Los cuatro numeros de la derecha son la respuesta a la pregunta del enunciado
    -- "las 3 pruebas negativas no dejaron basura" -- y son mas fuertes que el
    total: 11 = 10 sembradas + 1 de P1; cero citas de Rocky (P2 no inserto); cero
    citas el 22 de septiembre (P3 no inserto); y 1, no 2, en la franja del
    veterinario 1 el 1 de septiembre, que es lo que demuestra que P4 no duplico.

    Sobre la columna «paso»: aqui las 4 filas quedan en «t» porque «paso» se
    definio como "el resultado coincidio con lo esperado", y en las pruebas
    negativas lo esperado ES la excepcion. Es la semantica que usa cualquier
    framework de pruebas. La plantilla del enunciado deja las negativas en «f»,
    leyendo «paso» como "la operacion se completo": tambien es correcta y vale los
    mismos puntos, siempre que el estudiante escriba cual de las dos usa. Lo
    que no se acepta es que las cuatro filas digan «t» sin haber verificado el
    texto de la excepcion, porque entonces «paso» no significa nada.
```

### Como calificar

- **16 pts — los cuatro bloques `DO`, 4 pts cada uno.** Por bloque: 2 pts que el `CALL` sea el del caso pedido (mascota, veterinario y franja exactos), 1 pt el manejador `EXCEPTION` que evita que el script aborte, y 1 pt la fila registrada en `resultado_prueba` con `SQLERRM` en los negativos. **El criterio duro es que el script llegue hasta el final:** si se cae en el segundo bloque, los bloques que no corrieron no se califican.
- **4 pts — la semantica de `paso` es coherente y esta declarada.** Se acepta cualquiera de las dos lecturas —«coincidio con lo esperado» o «la operacion se completo»—; lo que se exige es que la misma regla valga para las 4 filas y que el estudiante diga cual eligio, en un comentario o en la columna `esperado`.
- **3 pts — la primera consulta de cierre** devuelve las 4 filas con las 4 columnas y `ORDER BY id_prueba`. Es la pregunta mas facil de la bateria y se pierde por olvido.
- **2 pts — la segunda consulta de cierre** demuestra que `cita` paso de 10 a 11 filas. Se dan los 2 pts con un `COUNT(*)` simple; la version con los cuatro conteos por caso es mejor y vale la pena senalarla como referencia, porque un total de 11 tambien saldria si P1 hubiera fallado y P2 hubiera insertado.
- **Se descuenta si el script se cae** por no capturar la excepcion, tal como dice la rubrica. El sintoma es inconfundible: `resultado_prueba` queda con menos de 4 filas y el error del motor aparece en pantalla.
- **Bono conceptual, sin puntos:** quien verifique el **texto** de la excepcion (`SQLERRM ILIKE '%inactiva%'`) en vez de aceptar cualquier fallo entendio para que sirve una prueba negativa. Es la diferencia entre probar y aparentar que se probo.

### Errores frecuentes y que hacer

- **Escribir los cuatro `CALL` seguidos, sin bloques `DO`.** El script se cae en el segundo y las pruebas 3 y 4 nunca corren. Es el error que la rubrica castiga explicitamente, y el sintoma es que `resultado_prueba` tiene una sola fila.
- **Un solo bloque `DO` con los cuatro `CALL` dentro.** Parece mas elegante y es peor: la primera excepcion salta al manejador y las llamadas siguientes se saltan. Cada prueba necesita su propio bloque justamente para poder fallar sola.
- **`EXCEPTION WHEN OTHERS THEN NULL;`** —capturar y no registrar nada—. El script no se cae, pero la bateria no prueba nada: no queda evidencia de que la excepcion ocurrio ni de cual fue. Es la version silenciosa del error anterior.
- **Poner el texto de la excepcion a mano** en la columna `obtenido` en vez de `SQLERRM`. Entonces la prueba dice lo que el estudiante espera, no lo que el motor respondio, y deja de ser una prueba. Se detecta porque el texto es sospechosamente limpio.
- **Creer que las pruebas negativas dejan filas a medias.** No las dejan, y vale explicar por que: el bloque `DO` con manejador abre una subtransaccion implicita, asi que cuando la excepcion se captura se deshace lo que el `CALL` hubiera alcanzado a hacer, y el `INSERT` en `resultado_prueba` que viene despues si queda. Ese mecanismo es el tema completo de la Clase 8.
- **Reportar «el procedimiento no existe».** En esta pregunta el procedimiento viene creado en el `setup_sql`. Si aparece el error, casi siempre el estudiante esta ejecutando en la base de la pregunta 1 con su propia version a medio hacer, o escribio el nombre con una letra distinta. Revisar el mensaje real antes de aceptar la premisa.

---

## Pregunta 3 · PROCEDURE o FUNCTION en PostgreSQL · 10 pts

### Clave y por que

La clave se lee del banco de la plataforma, asi que esta es la que se califica. La columna de la derecha es lo que hay que poder responderle al estudiante cuando pregunte.

|  | Opcion | Por que |
|---|---|---|
| no | Un PROCEDURE, porque en PostgreSQL los procedimientos pueden invocarse dentro de la lista de columnas de un SELECT. | **Incorrecta.** Es justamente lo que un `PROCEDURE` no puede hacer. En PostgreSQL un procedimiento se invoca con `CALL` como **sentencia independiente**; escribirlo en la lista de columnas de un `SELECT` da `ERROR: sp_x(...) is a procedure` y sugiere usar `CALL`. La frontera es clara: lo que se usa dentro de una consulta es una funcion. |
| **SI** | Un FUNCTION que devuelva NUMERIC, porque solo las funciones pueden usarse dentro de una consulta SELECT; los procedimientos se invocan con CALL como sentencia independiente. | **Correcta.** El criterio de decision no es «cual es mas moderno» sino **donde se necesita invocarlo**. Como el precio sugerido se va a usar dentro de un `SELECT` sobre `consulta`, tiene que ser `CREATE FUNCTION fn_precio_sugerido(p_especie TEXT) RETURNS NUMERIC`, y entonces se escribe `SELECT ..., fn_precio_sugerido(m.especie) FROM ...`. Un procedimiento no cabe ahi. |
| no | Un PROCEDURE con parametro OUT, porque en PostgreSQL es la unica forma de retornar un valor. | **Incorrecta.** Un `PROCEDURE` con parametro `OUT` **si** existe en PostgreSQL y devuelve valores —`CALL sp_x(1, NULL)` los entrega—, pero sigue siendo una sentencia independiente: no se puede poner dentro de un `SELECT`, que es lo que la pregunta necesita. Y el «es la unica forma de retornar un valor» es falso de plano: para eso estan las funciones. |
| no | Da exactamente lo mismo: en PostgreSQL PROCEDURE y FUNCTION son sinonimos y ambos se pueden llamar con SELECT o con CALL. | **Incorrecta, y es la mas importante de descartar** porque es el residuo de otros motores. En PostgreSQL son objetos distintos desde la version 11: la funcion se invoca dentro de una consulta y **no puede** controlar transacciones; el procedimiento se invoca con `CALL` y **si** puede hacer `COMMIT` y `ROLLBACK` en su interior. Esa capacidad transaccional es la verdadera razon por la que existen los dos. |
| no | Un FUNCTION, pero solo si se declara LANGUAGE sql; en plpgsql las funciones no pueden retornar valores. | **Incorrecta.** Al reves de la realidad. `LANGUAGE plpgsql` es precisamente el lenguaje con `DECLARE`, `IF`, bucles y `RETURN`, y las funciones plpgsql retornan valores todo el tiempo —el `sp_agendar_cita` de la pregunta 1 esta escrito en plpgsql—. `LANGUAGE sql` sirve para cuerpos de una sola expresion y es mas rapido cuando alcanza, pero no es una condicion para retornar. |

### Como calificar

- **10 pts si marca la opcion 2 tal como aparece numerada en la plataforma** (indice 1: la funcion que devuelve `NUMERIC`). Cualquier otra respuesta, 0. Es pregunta de opcion unica, sin parcial: la clave se lee del banco.
- El criterio que se evalua no es memoria de sintaxis sino **la regla de decision**: se usa funcion cuando hay que invocarla dentro de una consulta, y procedimiento cuando es una accion que se ejecuta sola y puede necesitar controlar la transaccion. Conviene decirla asi en la devolucion, porque es lo que se aplica en el PI: `sp_agendar_cita` es procedimiento; el precio sugerido es funcion.
- Si mas de un tercio del grupo marca la opcion 4 —«son sinonimos»—, vale abrir la Clase 4 con dos minutos de demostracion en vivo: un `SELECT` con la funcion adentro y un `SELECT` con el procedimiento adentro, para que vean el mensaje del motor. Es mas eficaz que repetir la definicion.

### Errores frecuentes y que hacer

- **Marcar la opcion 4 («da lo mismo»).** Casi siempre viene de material de otros motores, donde la distincion es mas borrosa. En PostgreSQL son objetos distintos y el motor lo dice con un mensaje de error explicito.
- **Marcar la del `PROCEDURE` con `OUT`.** El razonamiento va por buen camino —reconoce que hay que devolver algo— pero no atiende la condicion del enunciado, que es **usarlo dentro de un `SELECT`**. Vale la pena senalarlo asi: la respuesta no es incorrecta por el `OUT`, es incorrecta por donde se necesita invocar.
- **Marcar la ultima («solo si es `LANGUAGE sql`»).** Contradice el propio trabajo del estudiante: acaba de escribir plpgsql en las preguntas 1 y 4. Devolver con esa observacion es mas util que explicar la teoria.
- **Responder bien aqui y despues escribir `CREATE FUNCTION` en la pregunta 4.** Pasa mas de lo que parece. El taller pide un **procedimiento** en las preguntas 1 y 4 porque son acciones que modifican datos; la funcion es para el precio sugerido de esta pregunta, que no se implementa hoy.

---

## Pregunta 4 · sp_registrar_consulta: el segundo procedimiento de negocio · 15 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- sp_registrar_consulta: cierra el ciclo de la atencion. Inserta la
    -- consulta y mueve la cita a ATENDIDA en la misma operacion, para que no
    -- pueda existir una consulta cuya cita siga PROGRAMADA.
    -- =====================================================================
    CREATE OR REPLACE PROCEDURE sp_registrar_consulta(
      p_id_cita     INT,
      p_diagnostico TEXT,
      p_precio      NUMERIC
    )
    LANGUAGE plpgsql
    AS $proc$
    DECLARE
      v_estado TEXT;
    BEGIN
      -- 1) ¿Existe la cita? Igual que en sp_agendar_cita: SELECT ... INTO de
      --    una columna, para que FOUND signifique algo.
      SELECT estado INTO v_estado
        FROM cita
       WHERE id_cita = p_id_cita;

      IF NOT FOUND THEN
        RAISE EXCEPTION 'ERROR: la cita % no existe', p_id_cita;
      END IF;

      -- 2) Una cita CANCELADA no genera consulta. Se permite registrar sobre
      --    una PROGRAMADA (el caso normal) y tambien sobre una ATENDIDA que
      --    todavia no tenga consulta, porque la validacion 3 es la que decide
      --    eso: aqui solo se cierra la puerta a la cancelada.
      IF v_estado = 'CANCELADA' THEN
        RAISE EXCEPTION
          'ERROR: la cita % esta CANCELADA; una cita cancelada no genera consulta',
          p_id_cita;
      END IF;

      -- 3) ¿Ya tiene consulta? Se pregunta con EXISTS ANTES de intentar el
      --    INSERT. La restriccion UNIQUE de consulta.id_cita ya lo impediria,
      --    pero su mensaje seria "duplicate key value violates unique
      --    constraint consulta_id_cita_key", que no le sirve a nadie en el
      --    mostrador. La restriccion es la garantia; el EXISTS es la
      --    explicacion. Se necesitan las dos.
      IF EXISTS (SELECT 1 FROM consulta WHERE id_cita = p_id_cita) THEN
        RAISE EXCEPTION 'ERROR: la cita % ya tiene una consulta registrada',
                        p_id_cita;
      END IF;

      -- 4) Precio estrictamente positivo. Es MAS estricto que el CHECK de la
      --    tabla, que admite precio >= 0: una consulta gratis se registra con
      --    otro procedimiento y con autorizacion, no colandole un cero aqui.
      IF p_precio IS NULL OR p_precio <= 0 THEN
        RAISE EXCEPTION 'ERROR: el precio debe ser mayor que cero; llego %',
                        p_precio;
      END IF;

      -- 5) Las dos escrituras, en la misma operacion. Un PROCEDURE llamado con
      --    CALL corre dentro de la transaccion de quien lo llama: si el UPDATE
      --    fallara, el INSERT tambien se deshace. Eso es lo que hace que no
      --    exista una consulta con su cita sin atender.
      INSERT INTO consulta (id_cita, diagnostico, precio)
      VALUES (p_id_cita, p_diagnostico, p_precio);

      UPDATE cita
         SET estado = 'ATENDIDA'
       WHERE id_cita = p_id_cita;
    END;
    $proc$;

    -- =====================================================================
    -- Demostracion: una valida y dos que deben fallar sin detener el script.
    -- =====================================================================
    CALL sp_registrar_consulta(1, 'Vacunacion anual antirrabica', 45000);

    DO $$
    BEGIN
      CALL sp_registrar_consulta(4, 'Revision', 30000);   -- cita 4: CANCELADA
    EXCEPTION WHEN OTHERS THEN
      RAISE NOTICE '%', SQLERRM;
    END $$;

    DO $$
    BEGIN
      CALL sp_registrar_consulta(2, 'Duplicada', 40000);  -- cita 2: ya tiene
    EXCEPTION WHEN OTHERS THEN
      RAISE NOTICE '%', SQLERRM;
    END $$;

    -- =====================================================================
    -- Cierre pedido por el enunciado.
    -- =====================================================================
    SELECT c.id_cita, c.estado, co.diagnostico, co.precio
      FROM cita c
      LEFT JOIN consulta co ON co.id_cita = c.id_cita
     ORDER BY c.id_cita;
```

### Salida esperada

```
Los dos avisos de los bloques DO (van al panel de mensajes, no a la grilla):

      NOTICE:  ERROR: la cita 4 esta CANCELADA; una cita cancelada no genera consulta
      NOTICE:  ERROR: la cita 2 ya tiene una consulta registrada

    SELECT c.id_cita, c.estado, co.diagnostico, co.precio ...   -- 10 filas

     id_cita |   estado   |         diagnostico          |  precio
    ---------+------------+------------------------------+----------
           1 | ATENDIDA   | Vacunacion anual antirrabica | 45000.00
           2 | ATENDIDA   | Vacunacion triple felina     | 40000.00
           3 | PROGRAMADA |                              |
           4 | CANCELADA  |                              |
           5 | ATENDIDA   | Control de peso              | 38000.00
           6 | PROGRAMADA |                              |
           7 | ATENDIDA   | Otitis externa               | 55000.00
           8 | PROGRAMADA |                              |
           9 | PROGRAMADA |                              |
          10 | ATENDIDA   | Desparasitacion              | 35000.00

    Las tres comprobaciones que hay que buscar en esta salida, en este orden:

    1. La fila 1 paso de PROGRAMADA a ATENDIDA y trae diagnostico y precio: el
       procedimiento hizo sus dos escrituras.
    2. La fila 4 sigue en CANCELADA y con las dos columnas vacias: la validacion
       2 impidio la consulta y, muy importante, no cambio el estado. Si la fila 4
       apareciera en ATENDIDA, el UPDATE se hizo antes de validar.
    3. La fila 2 conserva su diagnostico original, «Vacunacion triple felina», no
       «Duplicada»: la validacion 3 rechazo el segundo registro sin sobrescribir el
       primero.

    El precio sale con dos decimales porque la columna es «NUMERIC(12,2)», aunque el
    «CALL» recibio «45000» sin decimales. No es un error del estudiante.
```

### Como calificar

- **8 pts — las cuatro validaciones, 2 pts cada una.** Cita inexistente, cita cancelada, consulta duplicada **detectada con `EXISTS`** y precio positivo. La tercera es la que la rubrica subraya: si el estudiante deja que reviente la restriccion `UNIQUE` en vez de preguntar antes, esos 2 pts no se dan aunque el resultado final sea el mismo, porque el mensaje que llega a la aplicacion es inservible.
- **4 pts — las dos escrituras.** 2 pts el `INSERT` en `consulta` y 2 pts el `UPDATE` de la cita a `'ATENDIDA'`, **despues** de las cuatro validaciones. Se verifica en la salida: la fila 4 debe seguir en `CANCELADA`.
- **2 pts — la demostracion completa.** La llamada valida corre, y las dos invalidas van envueltas en `DO ... EXCEPTION WHEN OTHERS THEN RAISE NOTICE` de modo que el script llega hasta el `SELECT` final. Si el script se detiene, estos 2 pts no se dan.
- **1 pt — el `SELECT` final** con el `LEFT JOIN` y el `ORDER BY` pedidos, devolviendo las 10 filas. Con `JOIN` en vez de `LEFT JOIN` devuelve 5 y se pierde el punto: el `LEFT` esta ahi precisamente para ver las citas **sin** consulta.
- **Piso de sintaxis.** Si el procedimiento no se crea, no hay puntos de validaciones ni de escrituras. Y una advertencia de correccion: quien haya resuelto bien la pregunta 1 y mal esta casi siempre fallo en el `RAISE EXCEPTION` de varias lineas, que necesita la coma antes de los argumentos.
- **Bono conceptual, sin puntos:** quien escriba en un comentario que el `EXISTS` **no reemplaza** a la restriccion `UNIQUE` sino que la acompana —porque entre el `EXISTS` y el `INSERT` cabe otra sesion— ya entendio el tema de la Clase 10 tres semanas antes. Vale mencionarlo al grupo.

### Errores frecuentes y que hacer

- **Confiar en el `UNIQUE` y no validar con `EXISTS`.** Funciona en el sentido de que no se duplica, pero el mensaje que sale es `duplicate key value violates unique constraint`, que la aplicacion no puede traducir a nada util. Es el error que la rubrica senala de forma explicita.
- **Hacer el `UPDATE` de la cita antes del `INSERT` de la consulta, o antes de validar.** El sintoma esta en la salida: la cita 4 aparece `ATENDIDA` aunque no tenga consulta. Deja la base en un estado que ninguna regla del negocio admite y es exactamente el tipo de inconsistencia que la Clase 8 formaliza.
- **Validar `p_precio >= 0` en vez de `> 0`.** El enunciado pide estrictamente positivo. Ademas hay una razon para no copiar el `CHECK` de la tabla: el `CHECK` protege la integridad del dato, el procedimiento protege la regla del negocio, y aqui la regla es mas estricta que el dato.
- **Olvidar el caso `NULL` en el precio.** `NULL <= 0` no es falso, es **desconocido**, asi que el `IF` no entra y el `INSERT` termina fallando por el `NOT NULL` de la columna, con un mensaje del motor en vez del propio. Es el error de logica de tres valores mas comun y vale explicarlo en voz alta: por eso la condicion empieza con `p_precio IS NULL OR`.
- **Poner los tres `CALL` sin bloque `DO`.** El script se detiene en el segundo, el `SELECT` final nunca corre y no hay evidencia de nada. El enunciado da la plantilla, asi que este error es de lectura.
- **`JOIN` en vez de `LEFT JOIN`** en el cierre. Devuelve 5 filas y desaparecen justo las que interesan —las citas sin consulta, entre ellas la 4—. Cuesta el punto y, peor, esconde la comprobacion mas importante de la pregunta.

---

## Pregunta 5 · Contrato de los procedimientos para la futura aplicacion · 15 pts

### Respuesta esperada

| Procedimiento | Excepcion | Texto del mensaje | Que debe hacer la aplicacion |
|---|---|---|---|
| `sp_agendar_cita` | Mascota inexistente | `ERROR: la mascota 99 no existe` | **No** mostrar el error al usuario: es un defecto del cliente, que envio un id que no esta en el catalogo. Registrar en el log con el id recibido y mostrar «seleccione una mascota de la lista». El selector debe cargarse de la base, no escribirse a mano. |
| `sp_agendar_cita` | Mascota inactiva | `ERROR: la mascota 3 esta inactiva; no se agenda cita` | Aviso al usuario con el motivo, en su idioma: «Rocky esta inactivo y no puede agendar. Reactivelo desde la ficha de la mascota o consulte con la coordinacion». Deshabilitar el boton de agendar mientras la mascota elegida este inactiva. |
| `sp_agendar_cita` | Veterinario ocupado | `ERROR: el veterinario 1 ya tiene cita en 2026-09-01 08:00:00` | No es un error del usuario, es una carrera perdida: alguien tomo la franja primero. Refrescar la agenda del veterinario y **ofrecer las tres franjas libres mas cercanas**, sin perder el resto del formulario. |
| `sp_registrar_consulta` | Cita inexistente | `ERROR: la cita 99 no existe` | Defecto del cliente. Log con el id, mensaje generico y volver a cargar la lista de citas del dia: casi siempre la pantalla quedo abierta con datos viejos. |
| `sp_registrar_consulta` | Cita cancelada | `ERROR: la cita 4 esta CANCELADA; una cita cancelada no genera consulta` | Aviso con el motivo y bloqueo del formulario de consulta para esa cita. Ofrecer la accion correcta: agendar una cita nueva, que es `sp_agendar_cita`. |
| `sp_registrar_consulta` | Consulta duplicada | `ERROR: la cita 2 ya tiene una consulta registrada` | Casi siempre es un doble clic o un reenvio del formulario. **No** insistir: mostrar la consulta que ya existe y ofrecer «editar» en vez de «registrar». La aplicacion deberia ademas deshabilitar el boton despues del primer envio. |
| `sp_registrar_consulta` | Precio no valido | `ERROR: el precio debe ser mayor que cero; llego 0` | Validacion de formulario que **tambien** debe estar en el cliente, para no gastar un viaje a la base. Marcar el campo en rojo con el texto «el precio debe ser mayor que cero» y no habilitar el envio hasta que lo sea. |

**Contrato de `sp_agendar_cita`**

1. **Firma exacta:** `sp_agendar_cita(p_id_mascota INT, p_id_veterinario INT, p_fecha_hora TIMESTAMP)`. Tres parametros de entrada, en ese orden, sin valores por omision y sin parametros `OUT`.
2. **Como se invoca:** `CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');`
3. **Precondiciones:** la mascota existe y tiene `activa = 'S'`; el veterinario existe; el veterinario no tiene otra cita no cancelada en esa misma `fecha_hora`. Quien llama **no** tiene que comprobar nada de esto: puede llamar y atender la excepcion. Esa es la gracia del contrato.
4. **Postcondiciones:** exactamente **una** fila nueva en `cita`, con `estado = 'PROGRAMADA'` y el `id_cita` que asigna la secuencia. Ninguna otra tabla cambia. Si la llamada falla, **ninguna** fila cambia: no hay estados intermedios visibles.
5. **Tabla de errores:** las tres primeras filas de la tabla de arriba.
6. **Decision de diseno:** la validacion vive en la base porque la regla «una mascota inactiva no agenda» es del negocio, no de la pantalla. Manana habra una app web, un script de carga masiva y una consola de soporte tocando la misma base; si la regla estuviera en la app, los otros dos caminos la esquivarian sin enterarse. Escrita una sola vez dentro del motor, vale para **cualquier** cliente que llegue.

**Contrato de `sp_registrar_consulta`**

1. **Firma exacta:** `sp_registrar_consulta(p_id_cita INT, p_diagnostico TEXT, p_precio NUMERIC)`.
2. **Como se invoca:** `CALL sp_registrar_consulta(1, 'Vacunacion anual antirrabica', 45000);`
3. **Precondiciones:** la cita existe; su estado **no** es `'CANCELADA'`; no tiene todavia una consulta registrada; el precio es mayor que cero.
4. **Postcondiciones:** una fila nueva en `consulta` con `id_cita` unico, y la fila correspondiente de `cita` con `estado = 'ATENDIDA'`. **Las dos cosas o ninguna:** el procedimiento corre dentro de la transaccion de quien lo llama, asi que no puede quedar una consulta cuya cita siga `PROGRAMADA`. Esta es la postcondicion mas importante del contrato y es la que la Clase 8 formaliza con la palabra atomicidad.
5. **Tabla de errores:** las cuatro ultimas filas de la tabla de arriba.
6. **Decision de diseno:** ademas del argumento anterior, aqui hay uno propio: el paso «insertar la consulta» y el paso «marcar la cita como atendida» **tienen que ocurrir juntos**. Si la aplicacion hiciera dos llamadas —un `INSERT` y luego un `UPDATE`— una caida de red entre las dos dejaria la base en un estado que ninguna regla del negocio admite. Dentro del procedimiento eso es imposible por construccion.

**Regla del PI, la frase de cierre:**

> La aplicacion de Huellitas **nunca** hara `INSERT` ni `UPDATE` directo sobre `cita` ni sobre `consulta`. Su unico acceso de escritura a esas dos tablas es `EXECUTE` sobre `sp_agendar_cita` y `sp_registrar_consulta`. Lo que la matriz de la Clase 2 escribio como intencion, aqui queda implementado: en la Clase 12 el rol `recepcion` pierde el `INSERT` sobre `cita` y conserva unicamente el `EXECUTE`.

### Como calificar

- **8 pts — los 6 puntos documentados para los dos procedimientos.** 4 pts por procedimiento, a razon de aproximadamente 0,67 por punto. Se descuenta el punto completo cuando la seccion existe pero esta vacia de contenido verificable («precondiciones: que los datos sean correctos»).
- **3 pts — las firmas coinciden exactamente con el codigo entregado** en las preguntas 1 y 4: nombre, orden y tipos. Es el criterio duro de la rubrica y se revisa comparando contra **el script del estudiante**, no contra esta solucion. Si su procedimiento recibe `(p_id_veterinario, p_id_mascota, ...)` en otro orden, su contrato tiene que decir ese orden.
- **3 pts — la tabla de errores.** Debe listar **todas** las excepciones que su propio codigo implementa —normalmente 3 + 4 = 7—, con el **texto real** del mensaje y una **accion concreta** de la aplicacion para cada una. 0,4 pts por fila. Una accion como «mostrar el error» no cuenta: hay que decir que ve el usuario y que hace el sistema.
- **1 pt — la justificacion** menciona explicitamente que la regla debe valer para **cualquier cliente** que toque la base, no solo para la app web. Es la frase que la rubrica pide y es el argumento central de la clase.
- **Se valora, sin puntos adicionales:** distinguir los errores que el usuario debe ver (mascota inactiva, precio invalido) de los que son defectos del cliente y solo van al log (id inexistente). Esa distincion es la que hace un contrato utilizable, y es lo que la Clase 12 va a exigir por escrito.
- **Extension.** Dos paginas es de sobra. Se califica que esten los 6 puntos y la tabla completa; no se descuenta por brevedad si nada falta.

### Errores frecuentes y que hacer

- **Firmas que no coinciden con el codigo entregado.** Es el descuento mas frecuente y el mas facil de evitar: casi siempre el estudiante escribe el contrato de memoria en vez de copiar la cabecera de su propio `CREATE PROCEDURE`. La correccion es literal: copiar y pegar.
- **Tabla de errores con la excepcion pero sin el texto del mensaje.** El mensaje **es** el contrato: es lo unico que la aplicacion recibe y sobre lo que puede decidir. Sin el texto, la tabla no sirve para programar nada.
- **«Que debe hacer la aplicacion: mostrar un mensaje de error».** No es una accion, es la ausencia de una decision. Se pide el comportamiento concreto: que texto ve el usuario, que control se bloquea, que alternativa se ofrece.
- **Mostrar el `SQLERRM` crudo al usuario final.** «ERROR: la mascota 3 esta inactiva» esta bien para el log; en pantalla el usuario necesita el nombre («Rocky») y la salida («reactivelo desde la ficha»). Vale la pena senalarlo aunque el enunciado no lo exija: es la diferencia entre un mensaje tecnico y un mensaje util.
- **Postcondiciones que no dicen que pasa si falla.** «Se inserta la cita» esta a medias. La otra mitad —«y si falla, no cambia nada»— es la que le permite a la aplicacion no tener que limpiar despues de un error, y es la razon de ser del procedimiento.
- **Justificar con la definicion.** «La validacion va en la base porque es mas seguro» no dice nada. Se pide el argumento del caso: tres clientes distintos tocando la misma base y una sola regla que ninguno puede esquivar.
- **Omitir la frase de cierre del PI.** Es una linea y es la que conecta esta clase con la matriz de la Clase 2 y con el contrato de la Clase 12. Si falta, pedirla: no es decoracion, es la decision de arquitectura del proyecto.

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**¿Puedo escribir `CREATE PROCEDURE` como en Oracle, con `IS` y `/` al final?**

No, y el motor lo rechaza de entrada. La forma de PostgreSQL es `CREATE OR REPLACE PROCEDURE nombre(params) LANGUAGE plpgsql AS $proc$ DECLARE ... BEGIN ... END; $proc$;`. Cuatro traducciones que resuelven el 90 % de los errores: `AS` en vez de `IS`, `TEXT` o `VARCHAR` en vez de `VARCHAR2`, `NUMERIC` en vez de `NUMBER`, y `RAISE EXCEPTION 'texto %', var;` en vez de `RAISE_APPLICATION_ERROR`. La barra final simplemente no existe.

**Mi validacion de «no existe» nunca dispara. ¿Que pasa?**

Casi con seguridad esta usando `IF NOT FOUND` despues de un `SELECT COUNT(*) INTO`. Un `COUNT` **siempre** devuelve una fila, asi que `FOUND` es verdadero incluso cuando el conteo da cero. `NOT FOUND` funciona despues de un `SELECT columna INTO`, que puede no traer fila. Con agregados hay que comparar el numero: `IF v_ocupado > 0 THEN`.

**¿Por que el procedimiento valida si la tabla ya tiene un `CHECK` y un `UNIQUE`?**

Porque hacen dos cosas distintas y se necesitan las dos. La restriccion es la **garantia**: no hay forma de meter el dato malo, venga de donde venga. El `IF` del procedimiento es la **explicacion**: convierte `duplicate key value violates unique constraint consulta_id_cita_key` en «la cita 2 ya tiene una consulta registrada», que es lo que la aplicacion puede mostrar. Quitar la restriccion y quedarse con el `IF` es el error grave; quitar el `IF` y quedarse con la restriccion solo deja mensajes inservibles.

**Corri mi script dos veces y me dice que el procedimiento ya existe.**

Es normal: `CREATE PROCEDURE` falla si el nombre esta tomado. Use `CREATE OR REPLACE PROCEDURE` desde el principio y el problema desaparece. Si ya quedo creado y quiere cambiar los parametros, hay que borrarlo primero con `DROP PROCEDURE sp_agendar_cita(INT, INT, TIMESTAMP);` —con los tipos, porque el nombre solo no identifica la rutina—. Recargar el ejercicio en ExamLab tambien devuelve la base al estado sembrado.

**Si valido con un `IF` que la franja esta libre, ¿ya no hay forma de duplicar?**

Con una sola sesion, no. Con dos personas agendando al mismo tiempo, si: las dos pueden contar cero antes de que ninguna haya insertado, y las dos insertar. La validacion leyendo antes de escribir no es una garantia, es una comodidad. La garantia es una restriccion unica sobre `(id_veterinario, fecha_hora)` para las citas no canceladas, y ese es exactamente el tema de la Clase 10. Quien lo escriba hoy en un comentario va tres semanas adelantado.

**¿Cual es la diferencia real entre PROCEDURE y FUNCTION, mas alla de la sintaxis?**

Dos, y las dos importan. Una: la funcion se puede invocar **dentro** de una consulta (`SELECT fn_precio(m.especie) FROM mascota m`) y el procedimiento no; el procedimiento se invoca con `CALL` como sentencia suelta. Dos: el procedimiento puede hacer `COMMIT` y `ROLLBACK` en su interior y la funcion no, porque la funcion corre dentro de la consulta que la llamo. Para el PI la regla practica es simple: si modifica datos y es una accion del negocio, procedimiento; si calcula y devuelve un valor para usarlo en una consulta, funcion.

**En las pruebas negativas, ¿`paso` debe quedar en TRUE o en FALSE?**

Las dos se aceptan, siempre que diga cual usa y la aplique a las cuatro filas. Si `paso` significa «el resultado coincidio con lo esperado», las negativas quedan en TRUE, porque lo esperado era la excepcion: es la semantica de cualquier framework de pruebas. Si significa «la operacion se completo», quedan en FALSE, que es lo que hace la plantilla del enunciado. Lo que no vale es que las cuatro digan TRUE sin haber verificado el texto de la excepcion, porque entonces cualquier fallo —incluso un nombre mal escrito— se reportaria como prueba superada.

**¿Las pruebas que fallan dejan filas a medias en `cita`?**

No, y el mecanismo vale la pena entenderlo porque es el tema de la Clase 8: un bloque `DO` con manejador `EXCEPTION` abre una subtransaccion, asi que al capturar la excepcion se deshace todo lo que el `CALL` alcanzo a hacer. El `INSERT` en `resultado_prueba` que viene **despues** del manejador si queda. Por eso la bateria puede registrar cuatro resultados y dejar una sola cita nueva, y por eso la segunda consulta de cierre debe dar 11 y no 14.

---

## Cierre de la clase

- Al terminar, cada estudiante debe tener: `sp_agendar_cita` creado con sus tres validaciones y el `CALL` que agrega la cita 11, la bateria de cuatro pruebas con las cuatro filas en `resultado_prueba` y los conteos que demuestran que nada quedo a medias, `sp_registrar_consulta` con sus cuatro validaciones y la cita 1 en `ATENDIDA`, y el contrato de los dos procedimientos con la tabla de las siete excepciones.
- Lo que hay que verificar antes de cerrar la sesion es la **consistencia entre las preguntas 1 y 4 y la pregunta 5**: el contrato tiene que describir el codigo que el estudiante entrego, no el de la solucion. Proyecte una entrega voluntaria y compare la cabecera del `CREATE PROCEDURE` con la firma escrita en el contrato: es el chequeo de treinta segundos que detecta la mitad de las entregas flojas.
- Dejar dicho en voz alta lo que sigue. En la Clase 4 aparece el disparador, que es el unico objeto que nadie invoca, y con el la tabla de auditoria que la matriz de la Clase 2 ya reservo para el `auditor` en solo lectura. Y en la Clase 10 se vera por que la validacion de la franja libre que hoy quedo escrita con un `IF` **no** garantiza nada con dos personas agendando al mismo tiempo: la garantia sera una restriccion, no un `IF` mas.

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. El motor de la plataforma es PostgreSQL (PGlite en el navegador), no Oracle.
