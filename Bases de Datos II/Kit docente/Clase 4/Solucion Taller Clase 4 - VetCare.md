# Solucion del taller · Clase 4 · Funciones, triggers y plan de respaldo de VetCare

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** La funcion de tarifas `fn_precio_consulta` corriendo dentro de dos consultas, el trigger de auditoria que registra 2 filas y no 3, el trigger que impide el stock negativo despues de haber visto el -7 en pantalla, el criterio para decidir si una validacion va en `CHECK`, en trigger o en la aplicacion, y el `Plan_Backup_VetCare` con RPO, RTO y una consulta de validacion post-restauracion que si detecta un respaldo incompleto.

> **El motor es PostgreSQL, no Oracle,** y esta clase es la que mas se paga en sintaxis: en PostgreSQL el trigger **no lleva codigo adentro**. Se escriben dos objetos —una funcion `RETURNS TRIGGER` y luego `CREATE TRIGGER ... EXECUTE FUNCTION nombre_de_la_funcion()`— y dentro de la funcion se usan `NEW` y `OLD` **sin los dos puntos**: `NEW.estado`, no `:NEW.estado`. Anunciarlo antes de arrancar ahorra la mitad de los reportes de error. Un detalle del entorno: la pregunta 3 corre sobre una base donde la tabla `insumo` fue creada **a proposito sin** su `CHECK (stock >= 0)`, para que el estudiante pueda ver el stock en -7 antes de arreglarlo; en las demas preguntas el `CHECK` si esta. Y la pregunta 5 es un **documento**: no hay que contratar ningun servicio, ni abrir cuenta, ni poner tarjeta.

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 4 - Funciones disparadores seguridad respaldo/Taller PI - Clase 4 - VetCare.docx`
- Configuracion en la plataforma: `Kit docente/Clase 4/Taller en ExamLab - Clase 4 (configuracion).md`
- Caso de estudio: `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
- Hito del PI: >=1 funcion + >=1 trigger + borrador plan de respaldo
- Entregable: Scripts funcion/trigger + Plan_Backup_VetCare (1 pag.)
- **Estas preguntas: 100 puntos** en 5 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 1 | Funcion de tarifas fn_precio_consulta | `bd_sql` | 20 |
| 2 | Trigger de auditoria de cambios de estado de cita | `bd_sql` | 20 |
| 3 | Trigger que impide stock negativo | `bd_sql` | 20 |
| 4 | Donde vive cada validacion: CHECK, trigger o aplicacion | `cerrada_multi` | 15 |
| 5 | Plan de respaldo de VetCare DB | `abierta` | 25 |

---

## Pregunta 1 · Funcion de tarifas fn_precio_consulta · 20 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- fn_precio_consulta: la tarifa base de Huellitas, en un solo lugar.
    -- Es FUNCTION y no PROCEDURE porque hay que invocarla DENTRO de un
    -- SELECT, que es justo lo que un procedimiento no puede hacer.
    -- IMMUTABLE es correcto aqui porque el resultado depende unicamente de
    -- los dos parametros: no lee ninguna tabla ni la hora del sistema.
    -- =====================================================================
    CREATE OR REPLACE FUNCTION fn_precio_consulta(
      p_especie  TEXT,
      p_urgencia BOOLEAN
    )
    RETURNS NUMERIC
    LANGUAGE plpgsql
    IMMUTABLE
    AS $fn$
    DECLARE
      v_base NUMERIC;
      v_urg  BOOLEAN;
    BEGIN
      -- COALESCE convierte el NULL en falso. Sin esto, IF p_urgencia THEN con
      -- NULL no entra por ninguna rama (NULL no es verdadero NI falso) y la
      -- funcion terminaria sin RETURN, lanzando
      -- "control reached end of function without RETURN".
      v_urg := COALESCE(p_urgencia, FALSE);

      -- UPPER() en los dos lados de la comparacion: asi 'CANINO', 'canino' y
      -- 'Canino' entran por la misma rama. Comparar contra 'Canino' a secas
      -- es el error mas frecuente de la pregunta.
      CASE UPPER(TRIM(COALESCE(p_especie, '')))
        WHEN 'CANINO' THEN v_base := 45000;
        WHEN 'FELINO' THEN v_base := 40000;
        ELSE               v_base := 35000;   -- cualquier otra especie
      END CASE;

      -- El recargo del 35 %. Se escribe * 1.35 y no + 35 % de nada: el
      -- ROUND(..., 2) esta para que las dos columnas salgan con la misma
      -- escala que la columna precio de consulta, NUMERIC(12,2).
      IF v_urg THEN
        RETURN ROUND(v_base * 1.35, 2);
      END IF;

      RETURN ROUND(v_base, 2);
    END;
    $fn$;

    -- =====================================================================
    -- Consulta 1: la tarifa de las 8 mascotas, normal y de urgencia.
    -- =====================================================================
    SELECT nombre,
           especie,
           fn_precio_consulta(especie, FALSE) AS tarifa_normal,
           fn_precio_consulta(especie, TRUE)  AS tarifa_urgencia
      FROM mascota
     ORDER BY id_mascota;

    -- =====================================================================
    -- Consulta 2: lo cobrado contra la tarifa. Este es el uso que justifica
    -- que sea funcion: va dentro del SELECT, en la misma fila que el precio
    -- real, y la resta la hace el motor.
    -- =====================================================================
    SELECT co.id_consulta,
           c.id_cita,
           m.nombre                                  AS mascota,
           m.especie,
           co.precio                                 AS precio_cobrado,
           fn_precio_consulta(m.especie, FALSE)      AS tarifa_base,
           co.precio - fn_precio_consulta(m.especie, FALSE) AS diferencia
      FROM consulta co
      JOIN cita    c ON c.id_cita    = co.id_cita
      JOIN mascota m ON m.id_mascota = c.id_mascota
     ORDER BY co.id_consulta;

    -- =====================================================================
    -- Comprobacion de las tres reglas del enunciado, en una sola fila.
    -- =====================================================================
    SELECT fn_precio_consulta('canino',  FALSE) AS minusculas_45000,
           fn_precio_consulta('CANINO',  TRUE)  AS urgencia_60750,
           fn_precio_consulta('Conejo',  FALSE) AS otra_especie_35000,
           fn_precio_consulta('Felino',  NULL)  AS null_como_falso_40000;
```

### Salida esperada

```
Consulta 1 -- 8 filas

      nombre  | especie | tarifa_normal | tarifa_urgencia
    ----------+---------+---------------+-----------------
     Firulais | Canino  |      45000.00 |        60750.00
     Luna     | Felino  |      40000.00 |        54000.00
     Rocky    | Canino  |      45000.00 |        60750.00
     Mishi    | Felino  |      40000.00 |        54000.00
     Bobby    | Canino  |      45000.00 |        60750.00
     Nube     | Felino  |      40000.00 |        54000.00
     Toby     | Canino  |      45000.00 |        60750.00
     Kiara    | Canino  |      45000.00 |        60750.00

    Las 8 mascotas, incluidas Rocky y Kiara que estan **inactivas**: la funcion no
    filtra por `activa` y esta bien que no lo haga. Una funcion IMMUTABLE no puede
    leer tablas; quien quiera excluirlas pone el `WHERE m.activa = 'S'` en la
    consulta, no dentro de la funcion. El numero que confirma el recargo es el
    **60750.00** (45000 x 1.35).

    Consulta 2 -- 4 filas

     id_consulta | id_cita | mascota  | especie | precio_cobrado | tarifa_base | diferencia
    -------------+---------+----------+---------+----------------+-------------+------------
               1 |       2 | Luna     | Felino  |       40000.00 |    40000.00 |       0.00
               2 |       5 | Nube     | Felino  |       38000.00 |    40000.00 |   -2000.00
               3 |       7 | Firulais | Canino  |       55000.00 |    45000.00 |   10000.00
               4 |      10 | Nube     | Felino  |       35000.00 |    40000.00 |   -5000.00

    Solo **una** de las cuatro consultas cobro exactamente la tarifa. Dos cobraron
    por debajo y una por encima, y la suma de las diferencias es +3000. La lectura
    que hay que dejar dicha: la funcion es la tarifa **de referencia**, no lo
    facturado; el negocio ajusta caso por caso. Ese hueco entre lo esperado y lo
    cobrado es lo que la Clase 6 va a convertir en una vista de control.

    Comprobacion de las reglas -- 1 fila

     minusculas_45000 | urgencia_60750 | otra_especie_35000 | null_como_falso_40000
    ------------------+----------------+--------------------+-----------------------
             45000.00 |       60750.00 |           35000.00 |              40000.00

    Los cuatro nombres de columna dicen el valor esperado, asi que la fila se
    corrige de un vistazo. Si la ultima columna sale vacia o el script falla con
    "control reached end of function without RETURN", falta el COALESCE.
```

### Como calificar

- **5 pts — la funcion se crea con la firma exacta.** `fn_precio_consulta(TEXT, BOOLEAN)`, `RETURNS NUMERIC`, `LANGUAGE plpgsql` y **`IMMUTABLE`**. 1 pt es de `IMMUTABLE`: es facil de olvidar y el enunciado lo pide de forma explicita. Si el motor no acepta la funcion, no hay puntos de logica.
- **8 pts — las cuatro reglas, 2 pts cada una.** Las tres tarifas 45000/40000/35000 con `ELSE` para «cualquier otra»; la insensibilidad a mayusculas con `UPPER()` o `lower()`; el recargo del 35 %; y `NULL` tratado como falso con `COALESCE`. La ultima es la que mas se pierde y la que mas vale explicar.
- **5 pts — las dos consultas pedidas.** 2 pts la de las 8 mascotas con las cuatro columnas y `ORDER BY id_mascota`; 3 pts la de la diferencia, que exige los **dos** `JOIN` (`consulta -> cita -> mascota`) y una columna `diferencia` calculada por el motor. Escribir la diferencia a mano no vale.
- **2 pts — los valores son coherentes con los datos.** La rubrica nombra el caso: Firulais canino en 45000 y 60750 en urgencia. Se verifica contra la salida de arriba, sin ejecutar nada.
- **Piso de sintaxis.** `RETURN NUMBER IS`, `VARCHAR2` o la barra `/` final impiden que el motor cree la funcion, asi que el efecto ya esta en el primer renglon: no se descuenta aparte.
- **Bono conceptual, sin puntos:** quien explique por que la funcion **puede** ser `IMMUTABLE` —porque no lee ninguna tabla, solo sus dos parametros— y senale que si manana las tarifas se guardaran en una tabla habria que bajarla a `STABLE`, entendio para que sirve la etiqueta. No es decoracion: una funcion `IMMUTABLE` que si lee tablas devuelve resultados viejos y es un error muy dificil de encontrar.

### Errores frecuentes y que hacer

- **`WHEN 'Canino' THEN`** sin normalizar. Funciona con los datos sembrados —que estan capitalizados asi— y falla en cuanto alguien escribe `CANINO` desde otra pantalla. Se detecta con la consulta de comprobacion: `fn_precio_consulta('canino', FALSE)` debe dar 45000, no 35000. Es el error que mas puntos cuesta porque **la salida de la consulta 1 se ve bien**.
- **Olvidar el `COALESCE` del `NULL`.** El sintoma es inconfundible: `ERROR: control reached end of function without RETURN`. La razon merece medio minuto en voz alta: `IF p_urgencia THEN ... ELSE ... END IF` con `p_urgencia` en `NULL` **no entra por ninguna de las dos ramas**, porque `NULL` no es verdadero ni falso. Es la logica de tres valores de SQL apareciendo dentro de un `IF`.
- **Aplicar el recargo como `v_base + 35`** o como `v_base * 0.35`. El primero suma 35 pesos y el segundo devuelve **solo** el recargo. Se detecta en un golpe: la columna de urgencia de Firulais tiene que decir 60750, y cualquier otro numero es este error.
- **Escribir un `PROCEDURE` en vez de una `FUNCTION`.** Se crea sin problema y revienta en la consulta 1 con `ERROR: fn_precio_consulta(...) is a procedure` y la sugerencia de usar `CALL`. Es exactamente la frontera de la pregunta 3 de la Clase 3, ahora en la practica: lo que se invoca dentro de un `SELECT` es una funcion.
- **Un solo `JOIN` en la consulta 2.** De `consulta` a `mascota` no hay camino directo: la especie esta en `mascota`, y `consulta` solo conoce `id_cita`. Hay que pasar por `cita`. Quien intente `JOIN mascota ON ...` desde `consulta` recibe `column co.id_mascota does not exist`, que es el motor diciendo justamente eso.
- **Meter el `WHERE m.activa = 'S'` dentro de la funcion.** Ademas de no poder —una funcion `IMMUTABLE` no debe leer tablas—, mezcla dos cosas: cuanto vale atender un canino, y a quien se le puede atender. La segunda ya la resuelve `sp_agendar_cita` de la Clase 3.

---

## Pregunta 2 · Trigger de auditoria de cambios de estado de cita · 20 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- 1) La tabla de auditoria. usuario_bd y fecha_evento con DEFAULT: los
    --    pone el motor, no el trigger, para que nadie pueda falsearlos desde
    --    la aplicacion. Es el mismo criterio de la matriz de la Clase 2: el
    --    rol auditor lee esta tabla y no escribe en ella.
    -- =====================================================================
    CREATE TABLE audit_cita (
      id_audit       SERIAL PRIMARY KEY,
      id_cita        INT       NOT NULL,
      accion         TEXT      NOT NULL,
      valor_anterior TEXT,
      valor_nuevo    TEXT,
      usuario_bd     TEXT      DEFAULT current_user,
      fecha_evento   TIMESTAMP DEFAULT now()
    );

    -- =====================================================================
    -- 2) La funcion de trigger. En PostgreSQL el codigo NO va dentro del
    --    CREATE TRIGGER: va aqui, en una funcion aparte que devuelve TRIGGER
    --    y que puede ser reutilizada por varios triggers.
    --    NEW y OLD se escriben SIN los dos puntos: NEW.estado, no :NEW.estado.
    -- =====================================================================
    CREATE OR REPLACE FUNCTION fn_trg_audit_cita()
    RETURNS TRIGGER
    LANGUAGE plpgsql
    AS $fn$
    BEGIN
      INSERT INTO audit_cita (id_cita, accion, valor_anterior, valor_nuevo)
      VALUES (NEW.id_cita, 'CAMBIO_ESTADO', OLD.estado, NEW.estado);

      -- En un trigger AFTER ... FOR EACH ROW el valor de retorno se ignora,
      -- asi que RETURN NULL y RETURN NEW dan lo mismo. Se pone RETURN NULL
      -- para dejar claro que esta funcion NO pretende modificar la fila.
      RETURN NULL;
    END;
    $fn$;

    -- =====================================================================
    -- 3) El trigger. Tres decisiones, las tres pedidas por el enunciado:
    --    AFTER  -> auditar lo que YA quedo guardado, no lo que se intento;
    --    UPDATE OF estado -> solo interesa esa columna;
    --    WHEN (OLD.estado IS DISTINCT FROM NEW.estado) -> y solo cuando de
    --    verdad cambio. Esto ultimo no es un lujo: UPDATE OF estado se
    --    dispara cuando la columna aparece en el SET, aunque el valor sea el
    --    mismo. Sin el WHEN habria 3 filas auditadas y no 2.
    --    IS DISTINCT FROM y no <>: con <>, un cambio de NULL a 'ATENDIDA'
    --    daria NULL, el WHEN no se cumpliria y ese cambio no se auditaria.
    -- =====================================================================
    CREATE TRIGGER trg_audit_cita
    AFTER UPDATE OF estado ON cita
    FOR EACH ROW
    WHEN (OLD.estado IS DISTINCT FROM NEW.estado)
    EXECUTE FUNCTION fn_trg_audit_cita();

    -- =====================================================================
    -- 4) Las tres pruebas del enunciado, en orden. La tercera es la que
    --    demuestra que el filtro funciona: la cita 6 ya esta PROGRAMADA.
    -- =====================================================================
    UPDATE cita SET estado = 'CANCELADA'  WHERE id_cita = 1;   -- se audita
    UPDATE cita SET estado = 'ATENDIDA'   WHERE id_cita = 3;   -- se audita
    UPDATE cita SET estado = 'PROGRAMADA' WHERE id_cita = 6;   -- NO se audita

    -- =====================================================================
    -- 5) El cierre pedido.
    -- =====================================================================
    SELECT id_audit, id_cita, accion, valor_anterior, valor_nuevo, usuario_bd
      FROM audit_cita
     ORDER BY id_audit;

    -- =====================================================================
    -- Prueba adicional que conviene mostrar al grupo: el UPDATE de la cita 6
    -- SI se ejecuto -- devolvio "UPDATE 1" -- y aun asi no dejo rastro. Es la
    -- diferencia entre "el UPDATE corrio" y "el estado cambio".
    -- =====================================================================
    SELECT (SELECT COUNT(*) FROM audit_cita)                        AS filas_auditadas,
           (SELECT estado FROM cita WHERE id_cita = 1)              AS cita_1,
           (SELECT estado FROM cita WHERE id_cita = 3)              AS cita_3,
           (SELECT estado FROM cita WHERE id_cita = 6)              AS cita_6,
           (SELECT COUNT(*) FROM audit_cita WHERE id_cita = 6)       AS auditorias_de_la_6;
```

### Salida esperada

```
UPDATE cita SET estado = 'CANCELADA'  WHERE id_cita = 1;   -- UPDATE 1
    UPDATE cita SET estado = 'ATENDIDA'   WHERE id_cita = 3;   -- UPDATE 1
    UPDATE cita SET estado = 'PROGRAMADA' WHERE id_cita = 6;   -- UPDATE 1  <-- corrio igual

    SELECT id_audit, id_cita, accion, valor_anterior, valor_nuevo, usuario_bd ...  -- 2 filas

     id_audit | id_cita |    accion     | valor_anterior | valor_nuevo | usuario_bd
    ----------+---------+---------------+----------------+-------------+------------
            1 |       1 | CAMBIO_ESTADO | PROGRAMADA     | CANCELADA   | postgres
            2 |       3 | CAMBIO_ESTADO | PROGRAMADA     | ATENDIDA    | postgres

    **Dos filas, no tres.** Es el resultado que la pregunta pide demostrar. Y el
    detalle que hay que subrayar en la devolucion: el tercer `UPDATE` **si se
    ejecuto** -- el motor respondio `UPDATE 1`, no `UPDATE 0` -- y aun asi no dejo
    rastro, porque la clausula `WHEN` se evalua por fila y descarto ese disparo.

    El valor de `usuario_bd` depende de con que usuario se conecte el entorno; en
    ExamLab sale `postgres`. No se califica el nombre, se califica que la columna
    tenga `DEFAULT current_user` y que el trigger **no** lo escriba a mano.

    Prueba adicional -- 1 fila

     filas_auditadas | cita_1    | cita_3   | cita_6     | auditorias_de_la_6
    -----------------+-----------+----------+------------+--------------------
                   2 | CANCELADA | ATENDIDA | PROGRAMADA |                  0

    Ese **0** de la derecha es la prueba mas limpia de que el filtro es el que
    trabaja, y no la casualidad.
```

### Como calificar

- **5 pts — `audit_cita` con las 7 columnas** y los dos `DEFAULT`: `current_user` y `now()`. 2 de los 5 pts son de los `DEFAULT`, porque son la razon de ser de la tabla: si el usuario y la hora los pone quien escribe, la auditoria no prueba nada.
- **5 pts — la funcion `RETURNS TRIGGER`** inserta `NEW.id_cita`, la accion `'CAMBIO_ESTADO'`, `OLD.estado` en `valor_anterior` y `NEW.estado` en `valor_nuevo`. Invertir `OLD` y `NEW` cuesta 2 pts: la salida sale con las columnas cruzadas y se detecta sin ejecutar nada.
- **6 pts — el trigger, 2 pts por decision.** `AFTER UPDATE` **`OF estado`**, `FOR EACH ROW`, y la clausula `WHEN (OLD.estado IS DISTINCT FROM NEW.estado)`. Los 2 pts del `WHEN` no se dan si se resuelve con un `IF` dentro de la funcion: funciona, pero el enunciado pide la clausula y hay una razon —abajo, en errores frecuentes—.
- **4 pts — la demostracion de las 2 filas.** 2 pts las tres sentencias en el orden pedido y 2 pts el `SELECT` final mostrando exactamente 2 filas. La rubrica exige ademas que **el estudiante explique por que la tercera no se audito**: si el script muestra 2 filas pero no hay una linea que lo explique, se descuenta 1 de estos 4.
- **Cero sintaxis Oracle.** `:NEW` / `:OLD`, el bloque `BEGIN ... END` dentro del `CREATE TRIGGER`, u omitir `EXECUTE FUNCTION`: la rubrica lo penaliza y en la practica el motor ni crea el objeto, asi que el efecto es automatico sobre los 6 pts del trigger.
- **Bono conceptual, sin puntos:** quien explique por que se usa `IS DISTINCT FROM` y no `<>` —con `<>`, un cambio desde `NULL` daria `NULL`, el `WHEN` no se cumpliria y **ese** cambio se perderia de la auditoria— entendio el unico detalle fino de la pregunta. Aqui `estado` es `NOT NULL` y da lo mismo, pero la costumbre correcta se construye ahora.

### Errores frecuentes y que hacer

- **Poner el codigo dentro del `CREATE TRIGGER`,** como en Oracle. Es el error numero uno de la clase. En PostgreSQL son **dos** objetos: una funcion `RETURNS TRIGGER` con el cuerpo, y un `CREATE TRIGGER` que solo dice cuando dispararla y termina en `EXECUTE FUNCTION nombre()`.
- **`:NEW.estado` en vez de `NEW.estado`.** Los dos puntos son de PL/SQL. El mensaje del motor —`syntax error at or near ":"`— apunta al lugar correcto, asi que este error se corrige solo si el estudiante lee el error.
- **Omitir la clausula `WHEN` y filtrar con un `IF` dentro de la funcion.** El resultado visible es el mismo —2 filas— y por eso hay que explicar la diferencia: con el `WHEN`, el motor **ni siquiera llama** a la funcion; con el `IF`, la llama, entra, evalua y sale. En una carga masiva de 50 000 citas esa diferencia es medible. Se descuentan los 2 pts del `WHEN` pero se reconoce que la logica es correcta.
- **Omitir el filtro por completo y no notarlo.** El `SELECT` final devuelve 3 filas, y una de ellas tiene `valor_anterior` y `valor_nuevo` **iguales**: `PROGRAMADA -> PROGRAMADA`. Esa fila es basura de auditoria, y en un ano son miles. Es el sintoma que hay que ensenar a reconocer.
- **`AFTER UPDATE ON cita` sin `OF estado`.** Funciona, porque el `WHEN` atrapa lo demas, pero hace que el trigger se evalue en cada cambio de `fecha_hora` tambien. Se descuentan los 2 pts de esa decision: el enunciado es explicito y la intencion —auditar **una** columna— debe quedar escrita en el objeto.
- **Escribir `usuario_bd` y `fecha_evento` desde el `INSERT` de la funcion.** Quita el sentido a los `DEFAULT` y abre la puerta a que un dia alguien ponga otro nombre. La regla es la de la Clase 2: el dato de la auditoria lo pone el motor, no el codigo que se audita.

---

## Pregunta 3 · Trigger que impide stock negativo · 20 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- 1) PRIMERO EL PROBLEMA. En esta base insumo NO tiene CHECK (stock >= 0),
    --    asi que el motor acepta encantado un stock imposible. Hay que verlo
    --    antes de arreglarlo: es la mitad del valor didactico de la pregunta.
    -- =====================================================================
    UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2;   -- habia 3

    SELECT id_insumo, nombre, stock AS stock_imposible
      FROM insumo
     WHERE id_insumo = 2;
    -- Vacuna triple felina | -7   <-- ninguna bodega del mundo tiene -7 vacunas

    -- Se restaura el dato antes de seguir. Se escribe el valor absoluto y no
    -- stock + 10, para no arrastrar el error si el UPDATE anterior corrio dos
    -- veces.
    UPDATE insumo SET stock = 3 WHERE id_insumo = 2;

    -- =====================================================================
    -- 2) La funcion de trigger. RETURN NEW al final es OBLIGATORIO en un
    --    trigger BEFORE ... FOR EACH ROW: si devolviera NULL, el motor
    --    cancelaria la fila EN SILENCIO -- el UPDATE diria "UPDATE 0" y nadie
    --    sabria por que. Devolver NEW es decir "sigue adelante con este
    --    valor".
    -- =====================================================================
    CREATE OR REPLACE FUNCTION fn_trg_stock_no_negativo()
    RETURNS TRIGGER
    LANGUAGE plpgsql
    AS $fn$
    BEGIN
      IF NEW.stock < 0 THEN
        RAISE EXCEPTION
          'ERROR: el stock de % no puede quedar negativo (resultado: %)',
          OLD.nombre, NEW.stock;
      END IF;

      RETURN NEW;
    END;
    $fn$;

    -- =====================================================================
    -- 3) El trigger. BEFORE, no AFTER: se revisa el valor ANTES de escribirlo,
    --    que es el unico momento en que todavia se puede vetar o corregir la
    --    fila con un RETURN. Un AFTER llega cuando el dato ya se escribio y su
    --    unico recurso es hacer estallar toda la sentencia.
    -- =====================================================================
    CREATE TRIGGER trg_stock_no_negativo
    BEFORE UPDATE OF stock ON insumo
    FOR EACH ROW
    EXECUTE FUNCTION fn_trg_stock_no_negativo();

    -- =====================================================================
    -- 4) Las dos pruebas, cada una en su propio bloque DO para que la primera
    --    no tumbe el script y la segunda alcance a correr.
    -- =====================================================================
    DO $$
    BEGIN
      -- Intento invalido: descontar 10 de un insumo que tiene 3.
      UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2;
      RAISE NOTICE 'PRUEBA 1 FALLIDA: el trigger dejo pasar un stock negativo';
    EXCEPTION WHEN OTHERS THEN
      RAISE NOTICE 'PRUEBA 1 OK, el trigger bloqueo: %', SQLERRM;
    END $$;

    DO $$
    BEGIN
      -- Intento valido: descontar 2. Debe pasar y dejar el stock en 1.
      UPDATE insumo SET stock = stock - 2 WHERE id_insumo = 2;
      RAISE NOTICE 'PRUEBA 2 OK, el descuento valido paso';
    EXCEPTION WHEN OTHERS THEN
      RAISE NOTICE 'PRUEBA 2 FALLIDA: %', SQLERRM;
    END $$;

    -- =====================================================================
    -- 5) Estado final: ningun stock negativo y el insumo 2 en 1.
    -- =====================================================================
    SELECT id_insumo, nombre, stock
      FROM insumo
     ORDER BY id_insumo;

    -- Y la comprobacion de una sola linea, para no tener que leer las 6 filas.
    SELECT COUNT(*) FILTER (WHERE stock < 0) AS negativos_debe_ser_0,
           (SELECT stock FROM insumo WHERE id_insumo = 2) AS insumo_2_debe_ser_1
      FROM insumo;
```

### Salida esperada

```
Paso 1 -- el problema, antes del trigger

     id_insumo |        nombre        | stock_imposible
    -----------+----------------------+-----------------
             2 | Vacuna triple felina |              -7

    Avisos de los dos bloques DO (van al panel de mensajes):

      NOTICE:  PRUEBA 1 OK, el trigger bloqueo: ERROR: el stock de Vacuna triple felina
               no puede quedar negativo (resultado: -7)
      NOTICE:  PRUEBA 2 OK, el descuento valido paso

    Estado final -- 6 filas

     id_insumo |          nombre          | stock
    -----------+--------------------------+-------
             1 | Vacuna antirrabica       |    12
             2 | Vacuna triple felina     |     1
             3 | Antiparasitario oral     |    40
             4 | Suero fisiologico 500ml  |    25
             5 | Gasa esteril             |     8
             6 | Jeringa 5ml              |    60

    Comprobacion de una linea -- 1 fila

     negativos_debe_ser_0 | insumo_2_debe_ser_1
    ----------------------+---------------------
                        0 |                   1

    Las tres cosas que hay que ver, en este orden: el **-7** existio (el problema es
    real, no una advertencia teorica), el aviso de la prueba 1 trae el **nombre del
    insumo** y el **valor rechazado** (el mensaje sirve para actuar, no solo para
    saber que algo fallo), y el insumo 2 quedo en **1** y no en 3 -- si quedara en 3,
    el trigger esta bloqueando tambien los descuentos validos, casi siempre por
    haber escrito `NEW.stock <= 0`.
```

### Como calificar

- **4 pts — se evidencia el problema y se restaura el dato.** 3 pts el `UPDATE` mas el `SELECT` que muestra el **-7**, y 1 pt devolver el insumo 2 a 3 antes de continuar. Sin la evidencia del -7 la pregunta pierde su sentido: el estudiante estaria arreglando un problema que no vio.
- **6 pts — la funcion.** 3 pts la condicion `NEW.stock < 0` con `RAISE EXCEPTION` que incluya `OLD.nombre` y `NEW.stock` en el mensaje; 3 pts el **`RETURN NEW`** en el camino valido. Este ultimo no es un detalle: sin el, un trigger `BEFORE` cancela la fila en silencio.
- **4 pts — el trigger es `BEFORE UPDATE OF stock ... FOR EACH ROW`.** La rubrica penaliza `AFTER`; se descuentan 2 de estos 4 si se usa `AFTER` —porque la eleccion de momento es lo que se esta evaluando— y los 4 completos si falta `FOR EACH ROW`, porque entonces el trigger es de sentencia y `NEW`/`OLD` ni existen.
- **4 pts — las dos pruebas en bloques `DO` separados,** con la excepcion capturada y el script llegando hasta el final. 2 pts cada una.
- **2 pts — el estado final** demuestra que ningun stock quedo negativo y que el insumo 2 esta en **1**. El 1 es el numero que se busca: en 3 significa que el trigger tambien bloqueo el descuento valido.
- **Bono conceptual, sin puntos, y es el mejor de la clase:** quien escriba que este trigger **sobra** —que la solucion correcta era el `CHECK (stock >= 0)` que la tabla tenia en las otras preguntas, y que el trigger esta aqui solo como ejercicio— acaba de responder por su cuenta la pregunta 4. Vale la pena leerlo en voz alta.

### Errores frecuentes y que hacer

- **Olvidar `RETURN NEW`.** El sintoma es raro y desconcierta: el `UPDATE` valido responde `UPDATE 0`, no da ningun error y el stock no cambia. Un trigger `BEFORE ... FOR EACH ROW` que devuelve `NULL` le dice al motor «descarta esta fila», y lo hace **en silencio**. Es el error mas costoso de depurar de toda la clase.
- **`NEW.stock <= 0`** en vez de `< 0`. Bloquea el caso legitimo de quedarse en cero, que es lo que pasa cuando se gasta la ultima unidad. Se detecta en el estado final: si el insumo 2 quedo en 3, el descuento valido tambien fue rechazado.
- **Usar `AFTER` en lugar de `BEFORE`.** Se descuenta segun la rubrica, y conviene dar la razon exacta porque la de «no impide el cambio» es imprecisa: en PostgreSQL una excepcion en un trigger `AFTER` **si** aborta la sentencia y deshace la escritura. Lo que pierde es todo lo demas: la fila ya se escribio y se indexo para nada, no queda forma de **corregir** el valor con un `RETURN NEW` ajustado, y si hay varios `AFTER` el orden alfabetico decide quien ve que. La validacion va donde todavia se puede decidir.
- **`RAISE_APPLICATION_ERROR(-20001, '...')`.** Es de Oracle y aqui es un error de sintaxis. El equivalente es `RAISE EXCEPTION 'texto % y %', var1, var2;`, y el `%` se sustituye en orden.
- **Usar `NEW.nombre` en el mensaje** en vez de `OLD.nombre`. Funciona, porque el `UPDATE` no toca el nombre y los dos valen lo mismo, y no se descuenta. Pero el enunciado pide `OLD.nombre` y hay una razon: el mensaje describe el insumo **tal como esta**, no como quedaria si el cambio pasara.
- **Poner los dos `UPDATE` de prueba sin bloque `DO`.** El primero lanza la excepcion, el script se detiene, la prueba valida nunca corre y el estado final no aparece. El enunciado da la plantilla del bloque, asi que este es un error de lectura.

---

## Pregunta 4 · Donde vive cada validacion: CHECK, trigger o aplicacion · 15 pts

### Clave y por que

La clave se lee del banco de la plataforma, asi que esta es la que se califica. La columna de la derecha es lo que hay que poder responderle al estudiante cuando pregunte.

|  | Opcion | Por que |
|---|---|---|
| **SI** | Si la regla depende solo de columnas de la propia fila, como stock >= 0, un CHECK es preferible al trigger: es declarativo, mas barato y no se puede olvidar. | **Correcta, y es la moraleja de la pregunta 3.** La regla «el stock no es negativo» mira una sola columna de la propia fila, asi que un `CHECK (stock >= 0)` la resuelve mejor que el trigger: es una linea, el motor la aplica venga el cambio de donde venga, no hay codigo que mantener y **no se puede desactivar por descuido**. El trigger de la pregunta 3 existe como ejercicio; en el PI real esa regla va en el `CHECK` que la tabla ya trae en las demas preguntas. |
| no | Un trigger AFTER UPDATE puede impedir que un UPDATE deje datos invalidos, igual que un BEFORE UPDATE. | **Incorrecta**, aunque no por la razon que suele darse. Es cierto que una excepcion lanzada desde un trigger `AFTER` aborta la sentencia y deshace la escritura; lo falso es el «igual que un `BEFORE`». Un `BEFORE` puede **vetar** la fila o incluso **corregirla** devolviendo un `NEW` modificado, y actua antes de gastar la escritura y los indices. Un `AFTER` llega cuando el dato ya esta puesto y su unica herramienta es hacer estallar todo. Se parecen en el resultado y no en lo que permiten: la validacion va donde todavia se puede decidir. |
| **SI** | Registrar la historia de cambios de estado de una cita requiere trigger o codigo: ninguna restriccion declarativa guarda el valor anterior. | **Correcta, y es la razon de ser de la pregunta 2.** Ninguna restriccion declarativa guarda el valor **anterior**: un `CHECK` mira la fila nueva, una clave ajena mira otra tabla, un `UNIQUE` mira el conjunto. Ninguna recuerda que la cita 1 estuvo `PROGRAMADA` antes de quedar `CANCELADA`. Para tener historia hace falta alguien que escriba la fila de auditoria, y ese alguien es un trigger o codigo de la aplicacion. El trigger gana porque no se puede esquivar. |
| no | Validar solo en la aplicacion es suficiente si quien desarrolla se compromete a no tocar la base con SQL directo. | **Incorrecta,** y es la que hay que desmontar con mas cuidado porque suena razonable. El compromiso de una persona no es un control: el mismo semestre del PI ya hay tres caminos hacia la misma base —la aplicacion web, los scripts de carga y la consola de soporte— y ninguno de los tres pasa por los otros. Ademas el compromiso caduca: la persona rota, entra otra, y la regla no esta escrita en ninguna parte que el motor lea. Validar en la aplicacion **tambien** es buena idea, por la experiencia de uso; lo que no es, es suficiente. |
| **SI** | Poner la validacion en la base protege tambien a cargas masivas, scripts de mantenimiento y a cualquier otra aplicacion que se conecte despues. | **Correcta, y es el argumento central de la clase.** La validacion en la base es la unica que cubre lo que nadie planeo: la carga masiva de fin de mes, el script de mantenimiento que se corre a mano una vez, el `UPDATE` de urgencia que alguien escribe en la consola a las 7 de la tarde, y la aplicacion movil que se contrate el ano entrante. Es la misma frase de cierre del contrato de la Clase 3, ahora aplicada a las reglas y no solo a los procedimientos. |
| **SI** | Abusar de triggers dificulta depurar: efectos ocultos, orden de ejecucion no evidente y costo por fila en operaciones masivas. | **Correcta, y es la contraparte honesta de todo lo anterior.** El trigger es potente justamente porque es invisible: nadie lo invoca y nadie lo ve en el codigo de la aplicacion. Eso mismo lo vuelve dificil de depurar —«¿de donde salio esta fila?»—, el orden entre varios triggers de la misma tabla lo decide el nombre en orden alfabetico y no la intencion del autor, y en un `UPDATE` de 200 000 filas un trigger `FOR EACH ROW` se ejecuta 200 000 veces. De ahi la regla practica: `CHECK` cuando alcance, trigger cuando haga falta, y siempre documentado. |

### Como calificar

- **15 pts con las 4 correctas marcadas y ninguna incorrecta**, con puntaje proporcional por acierto parcial, tal como dice la rubrica. La plataforma calcula el parcial; la clave se lee del banco y es la que se califica.
- El criterio que se esta evaluando es **una regla de decision de tres escalones**, y conviene decirla asi en la devolucion: si la regla mira solo la propia fila, `CHECK`; si necesita el valor anterior, otra fila u otra tabla, trigger; si es experiencia de uso —un mensaje bonito, un boton deshabilitado—, aplicacion, **ademas** de lo que ya este en la base.
- **El par 0 / 5 es el que mide comprension real.** Marcar solo el 0 es «la base siempre gana»; marcar solo el 5 es «los triggers son peligrosos». Marcar los dos es haber entendido que la eleccion tiene costo en las dos direcciones. Vale la pena mirar cuantos marcaron los dos.
- Si mas de un tercio del grupo marca la opcion 4 —«basta con la aplicacion si hay compromiso»—, es senal para abrir la Clase 6 con el ejemplo concreto: la carga masiva de insumos que nadie va a pasar por la pantalla.

### Errores frecuentes y que hacer

- **Marcar la del trigger `AFTER` como correcta.** No es un disparate: efectivamente la excepcion aborta la sentencia. Lo que falla es el «igual que»: un `BEFORE` puede corregir el valor y evita la escritura; un `AFTER` solo puede volar la sentencia entera. Devolver con esa precision, no con un «esta mal».
- **Marcar la de «basta con la aplicacion».** Casi siempre viene de haber trabajado en proyectos con un solo cliente. Basta con nombrar los tres caminos que el propio PI ya tiene abiertos hacia la misma base.
- **No marcar la opcion 5, la de los inconvenientes del trigger.** Suele ser por lealtad: acaban de escribir dos triggers y les parece que reconocerles un costo es contradecirse. Es lo contrario: la decision de diseno solo existe si se conocen los dos precios.
- **No marcar la opcion 0 despues de haber hecho la pregunta 3.** Es la senal de que el trigger de stock se resolvio como receta y no como decision. Aqui la devolucion es directa: la tabla `insumo` de las otras preguntas del taller ya tiene ese `CHECK`, y por eso alli el problema del -7 no existe.

---

## Pregunta 5 · Plan de respaldo de VetCare DB · 25 pts

### Respuesta esperada

| Que se respalda | Herramienta | Frecuencia y ventana | Retencion y ubicacion |
|---|---|---|---|
| Datos + esquema + rutinas, todo junto | `pg_dump -Fc -d vetcare -f vetcare_AAAAMMDD.dump` (formato comprimido, restaurable con `pg_restore`) | **Diario, 20:30.** La clinica cierra a las 19:00 y la facturacion del ultimo turno se cierra hacia las 19:45; 20:30 da hora y media de margen y aun deja la noche libre. | 14 copias diarias + la del domingo durante 8 semanas. **Ubicacion 1:** disco externo del consultorio. **Ubicacion 2:** carpeta cifrada sincronizada fuera de la clinica el mismo dia. |
| Roles, contrasenas y permisos (la matriz de la Clase 2) | `pg_dumpall --globals-only -f roles_AAAAMMDD.sql` | **Diario, 20:25,** justo antes del dump, y **ademas cada vez que se ejecuta un `GRANT` o `REVOKE`**. Se separa porque `pg_dump` de una base **no** incluye los roles: restaurar solo el dump deja una base con datos y sin usuarios. | 30 dias, las dos ubicaciones. Es un archivo de pocos kilobytes: no hay razon para guardar menos. |
| DDL y rutinas como codigo fuente versionado | El repositorio Git del PI: `/db/01_schema.sql`, `/db/02_procedimientos.sql`, `/db/03_triggers.sql`, `/db/migraciones/NNN_*.sql` | **En cada cambio,** con el `commit` correspondiente. El respaldo del esquema no es un archivo que se genera de noche: es el historial del repositorio. | Indefinida. **Ubicacion 1:** repositorio remoto. **Ubicacion 2:** clon local del docente. Se complementa con `pg_dump --schema-only` diario, para poder comparar lo que hay en produccion contra lo que dice el repositorio. |
| Copia fisica para recuperacion rapida | `pg_basebackup -D /respaldos/base_AAAAMMDD -Ft -z` | **Semanal, domingo 02:00,** con la clinica cerrada. Es la que permite un RTO corto: restaurar una copia fisica es copiar un directorio, no reconstruir la base sentencia por sentencia. | 4 copias semanales, solo en la ubicacion 1 por tamano. La primera del mes se conserva 12 meses en la ubicacion 2. |
| Registro continuo de transacciones (WAL) | Archivado de WAL: `archive_mode = on` mas un `archive_command` que copie cada segmento a `/respaldos/wal/` | **Continuo.** Es lo unico que permite recuperar el trabajo hecho **despues** del ultimo dump: sin esto, una caida a las 18:50 pierde el dia completo de atencion. | 7 dias, o el tiempo que cubra hasta la copia fisica mas antigua que se conserve. Ubicacion 1, con copia diaria a la 2. |

**2. Por que esas horas.** La clinica atiende de lunes a sabado de 7:00 a 19:00. Todo lo que bloquea o pesa se corre **fuera** de esa franja: el dump diario a las 20:30 y la copia fisica el domingo a las 2:00, el unico dia sin atencion. El unico proceso que corre en horario de atencion es el archivado de WAL, y corre porque no compite: copia segmentos ya cerrados. La ventana no se pone «en la madrugada» por costumbre: se pone a las 20:30 porque la facturacion del ultimo turno se cierra hacia las 19:45 y un respaldo tomado a las 19:10 dejaria fuera las facturas del final del dia, que son precisamente las que no se pueden reconstruir.

**4. RPO y RTO.**

- **RPO objetivo: 15 minutos.** Es lo que da el archivado de WAL, y se elige mirando que se pierde en cada caso. Quince minutos son, como maximo, una consulta y su factura: la agenda del dia esta impresa en recepcion y las dos se pueden volver a capturar en cinco minutos. Sin archivado de WAL el RPO seria de **hasta 12 horas de atencion** —una caida a las 18:50 volveria al dump de la noche anterior— y eso significa perder unas 25 citas atendidas y toda la facturacion del dia. Las citas se recuperan del papel; **las facturas y los diagnosticos no**, y son las que tienen consecuencia legal y contable. Por eso el archivado de WAL no es un lujo del plan: es lo que convierte un RPO inaceptable en uno aceptable.
- **RTO objetivo: 4 horas en horario de atencion, 12 horas si la falla ocurre fuera.** Cuatro horas es un tercio de la jornada: la clinica puede operar ese tiempo con la agenda impresa y capturar despues, pero no un dia entero. El presupuesto de las 4 horas se reparte asi: 30 min para detectar y decidir, 60 min para restaurar la copia fisica del domingo, 90 min para aplicar los WAL hasta el ultimo minuto disponible, 30 min para la consulta de validacion de abajo, y 30 min de margen. La copia fisica esta en el plan **por este numero**: restaurar desde el dump logico tomaria mas, porque hay que volver a crear indices y restricciones.

**5. Restore de prueba.** Un respaldo no verificado no es un respaldo, es un archivo. El ensayo es **mensual, el primer domingo, a las 3:00**, despues de la copia fisica, y son cinco pasos concretos:

1. `createdb vetcare_restore_AAAAMMDD` — nunca sobre la base de produccion.
2. `psql -d vetcare_restore_AAAAMMDD -f roles_AAAAMMDD.sql` — los roles primero, o el `pg_restore` fallara al asignar propietarios.
3. `pg_restore -d vetcare_restore_AAAAMMDD vetcare_AAAAMMDD.dump` y se **guarda la salida completa**, incluidos los avisos.
4. Se corre la consulta de validacion y se compara contra los valores esperados del dia del respaldo.
5. `dropdb vetcare_restore_AAAAMMDD` y se archiva la evidencia.

La consulta de validacion, con los valores que deben salir para el respaldo de la base sembrada de este taller:

```sql
SELECT (SELECT COUNT(*) FROM cita)          AS citas,          -- 10
       (SELECT COUNT(*) FROM consulta)      AS consultas,      --  4
       (SELECT COUNT(*) FROM factura)       AS facturas,       --  3
       (SELECT SUM(total) FROM factura)     AS suma_facturado, -- 178200.00
       (SELECT MAX(fecha_hora) FROM cita)   AS ultima_cita,
                                       -- 2026-09-10 09:00:00
       (SELECT COUNT(*) FROM pg_proc p
          JOIN pg_namespace n ON n.oid = p.pronamespace
         WHERE n.nspname = 'public')        AS rutinas,
       (SELECT COUNT(*) FROM pg_trigger
         WHERE NOT tgisinternal)            AS triggers;
```

Las dos ultimas columnas son las que hacen que esta consulta sirva de algo. Contar filas detecta un respaldo **truncado**; no detecta el fallo mas comun y mas silencioso, que es un respaldo con **todos los datos y sin las rutinas**: la base restaurada responde perfectamente a los `SELECT`, y el dia que alguien llama a `sp_agendar_cita` no existe, o el trigger de auditoria dejo de registrar sin que nadie se enterara. Se compara contra el numero del dia: al cerrar este taller son **3 rutinas** —`sp_agendar_cita`, `fn_precio_consulta`, `fn_trg_audit_cita`— y **1 trigger**.

**Quien firma:** el ensayo lo ejecuta quien administre la base y la evidencia —salida del `pg_restore` mas la fila de la consulta— queda en `/informe/respaldos/restore-AAAA-MM.md` firmada por el responsable del PI. Si un mes no se ensayo, se escribe que no se ensayo: un renglon vacio en la bitacora es informacion, un renglon inventado es un riesgo.

**6. Que NO cubre este plan, y el riesgo residual.**

- **No cubre el borrado correcto pero indeseado.** Si alguien cancela 40 citas por error y lo hace bien, el respaldo lo copia fielmente. Eso se recupera con la auditoria de la pregunta 2, no con el respaldo.
- **No cubre lo que no esta en la base:** radiografias, consentimientos escaneados, hojas de calculo en el escritorio de recepcion.
- **No cubre la infraestructura.** Restaurar datos en un servidor que no existe no sirve; el plan asume que hay una maquina donde restaurar.
- **Riesgo residual asumido, escrito y firmado:** la copia remota se verifica una vez al mes, no todos los dias. Entre dos ensayos puede haber hasta 30 dias de copias que nadie probo. Se acepta porque la copia local si se verifica con el ensayo mensual y porque el costo de un ensayo diario no se justifica para una clinica de este tamano. **Queda por escrito para que sea una decision y no un olvido.**

**Cierre — checklist del PI**

- **Listo:** matriz de roles y permisos (Clase 2). **Listo:** procedimientos de negocio con sus validaciones y su contrato (Clase 3). **Listo:** validaciones en la base para stock y estados (Clase 4). **Listo:** `Plan_Backup_VetCare` como documento.
- **En progreso:** auditoria de cambios sensibles. Esta la de `cita`; faltan `consulta` y `factura`, que son las dos que tienen consecuencia contable.
- **Falta:** el **primer ensayo de restore ejecutado**. El plan escrito vale cero hasta que exista una fila de evidencia en `/informe/respaldos/`, y ese es el gap principal que se declara hoy.
- **Falta:** los permisos de la matriz **aplicados** con `GRANT` sobre la base real, con el rol `recepcion` sin `INSERT` directo sobre `cita`. Es lo que cierra la Clase 12.

### Como calificar

- **12 pts — las 6 secciones, 2 pts cada una.** Se dan los 2 pts cuando la seccion trae **decisiones con numeros**, y 1 solo si esta presente pero es generica. El criterio para distinguirlas: «respaldo diario en la noche» es generico; «`pg_dump -Fc` a las 20:30 porque la facturacion cierra a las 19:45» es una decision.
- **4 pts — RPO y RTO justificados con el impacto para la clinica,** no definidos. Se pide un numero y la consecuencia de ese numero: cuantas citas y cuantas facturas se pierden, y cuales de las dos se pueden reconstruir del papel. Un RPO sin esa frase vale 1 de los 4.
- **4 pts — herramientas reales de PostgreSQL y bien asignadas.** `pg_dump`, `pg_dumpall --globals-only`, `pg_basebackup`, archivado de WAL, `pg_restore`. Se descuentan 2 si aparece herramienta de Oracle (`exp`/`imp`, `RMAN`, Data Pump) y 2 mas si `pg_dump` figura como si respaldara tambien los roles: es el error tecnico mas comun de esta pregunta.
- **3 pts — la consulta de validacion post-restauracion.** 2 pts que sea verificable, es decir que compare contra valores esperados concretos y no «revisar que los datos esten»; 1 pt la periodicidad del ensayo y quien firma. **Se reconoce como excelente** —sin puntos extra, pero se anota— si la consulta verifica ademas que volvieron las **rutinas y los triggers**: es el fallo silencioso que contar filas no detecta.
- **2 pts — el cierre del checklist del PI** con los items en «listo» / «en progreso» y **al menos un gap declarado explicitamente**. Un checklist con todo en verde no vale los 2 pts: en la Clase 4 es imposible que todo este listo, y la rubrica pide el gap pendiente.
- **Extension.** El enunciado pide una pagina. Se califica que las 6 secciones esten con decisiones concretas; no se premia la longitud y no se descuenta por brevedad si nada falta.

### Errores frecuentes y que hacer

- **Creer que `pg_dump` respalda los roles y los permisos.** No los respalda: `pg_dump` es de **una** base y los roles son del **cluster**. Restaurar solo el dump da una base con todos los datos y sin un solo usuario, y el `pg_restore` empieza a fallar al asignar propietarios. La matriz de la Clase 2 se respalda con `pg_dumpall --globals-only`. Es el error que hay que corregir aunque el resto del plan este bien.
- **Copiar el plan de otro motor.** `RMAN`, `exp`/`imp` o «Data Pump» descalifican la seccion 1: la rubrica exige herramientas reales de PostgreSQL. Se detecta rapido porque suele venir con una redaccion muy distinta del resto del documento.
- **RPO y RTO como definiciones.** «RPO es la cantidad de datos que se puede perder» no responde nada. La pregunta es **cuanta**, en minutos u horas, y **por que esa** y no el doble. Sin la justificacion de impacto son 1 punto de 4.
- **Un RPO de 15 minutos sin nada que lo sustente.** Si el plan solo tiene un dump diario, el RPO **es** de hasta 24 horas, digalo o no el documento. El numero tiene que estar respaldado por un mecanismo —archivado de WAL, o un segundo dump al mediodia para bajarlo a 6 horas—. Escribir un RPO que el plan no puede cumplir es peor que escribir uno honesto y grande.
- **Retencion en una sola ubicacion,** o dos ubicaciones que en realidad son la misma maquina: «disco C y disco D» no son dos ubicaciones. El enunciado pide **dos distintas** y la razon es concreta: un robo, un incendio o un cifrado por rescate se lleva las dos copias que estan en el mismo sitio.
- **Validar el restore «revisando que los datos esten».** No es verificable y no se puede automatizar. La seccion 5 pide una consulta con valores esperados; sin ella, el ensayo depende de la impresion de quien mira la pantalla.
- **El checklist del PI con todos los items en «listo».** Es la senal mas clara de que la seccion se lleno por cumplir. En la Clase 4 hay al menos dos cosas que no pueden estar hechas: el primer ensayo de restore y los `GRANT` aplicados. Pedir la correccion nombrando esas dos.

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**¿Por que mi `CREATE TRIGGER` no acepta el codigo adentro?**

Porque en PostgreSQL el trigger **no tiene cuerpo**. Son dos objetos y en este orden: primero `CREATE FUNCTION fn_x() RETURNS TRIGGER LANGUAGE plpgsql AS $fn$ BEGIN ... END; $fn$;` con toda la logica, y despues `CREATE TRIGGER trg_x BEFORE UPDATE ON tabla FOR EACH ROW EXECUTE FUNCTION fn_x();` que solo dice cuando dispararla. La ventaja de esta separacion es que una misma funcion puede servir a varios triggers de varias tablas; la desventaja es que hay que acordarse de crear los dos.

**¿`NEW` y `OLD` se escriben con dos puntos?**

No. En PostgreSQL son `NEW.columna` y `OLD.columna`, sin `:`. Los dos puntos son de PL/SQL de Oracle. Y hay una regla de disponibilidad que conviene tener presente: en un `INSERT` existe `NEW` y `OLD` es nulo; en un `DELETE` existe `OLD` y `NEW` es nulo; en un `UPDATE` existen los dos. Un trigger que use `OLD.nombre` en un `INSERT` fallara.

**¿`BEFORE` o `AFTER`? Me dijeron que un `AFTER` no puede impedir el cambio.**

La regla practica es correcta —**validar en `BEFORE`, auditar en `AFTER`**— pero esa explicacion es imprecisa y vale corregirla: en PostgreSQL una excepcion lanzada desde un trigger `AFTER` **si** aborta la sentencia y deshace la escritura. La razon real para validar en `BEFORE` es otra y es mejor: es el unico momento en que todavia se puede decidir. Ahi se puede vetar la fila, o incluso **corregirla** devolviendo un `NEW` modificado, y se evita el trabajo de escribir e indexar un dato que se va a rechazar. El `AFTER` llega cuando ya no hay nada que decidir, y por eso es el lugar de la auditoria: audita lo que **quedo**, no lo que se intento.

**¿Por que mi `UPDATE` responde «UPDATE 0» y no da ningun error?**

A la funcion del trigger `BEFORE` le falta el `RETURN NEW`. En un trigger `BEFORE ... FOR EACH ROW`, devolver `NULL` significa «descarta esta fila», y el motor lo hace **en silencio**: sin error, sin aviso, sin cambio. Es el error mas desconcertante de la clase. Regla: todo trigger `BEFORE` de fila termina en `RETURN NEW` en el camino valido. En un trigger `AFTER` el retorno se ignora y da igual devolver `NEW` o `NULL`.

**¿Para que sirve la clausula `WHEN` si puedo poner el mismo `IF` dentro de la funcion?**

El resultado visible es el mismo y las dos son correctas; la diferencia es donde se toma la decision. Con la clausula `WHEN`, el motor evalua la condicion y **ni siquiera llama** a la funcion; con el `IF` adentro, la llama, entra, evalua y sale. En un `UPDATE` de una fila no se nota; en una carga de 50 000 citas son 50 000 llamadas a una funcion que no va a hacer nada. Ademas la condicion queda visible en la definicion del trigger, que es donde alguien la va a buscar.

**¿Y por que `IS DISTINCT FROM` y no `<>`?**

Por los nulos. `'A' <> NULL` no da verdadero ni falso: da `NULL`, y un `WHEN` que evalua a `NULL` no se cumple, asi que ese cambio **no se auditaria**. `IS DISTINCT FROM` trata el nulo como un valor mas y devuelve verdadero o falso siempre. En esta tabla `estado` es `NOT NULL` y da lo mismo, pero la costumbre se construye ahora: en cuanto se audite una columna que admita nulos, `<>` empieza a perder cambios sin avisar.

**Si el `CHECK` es mejor, ¿por que el taller me hace escribir el trigger de stock?**

Para que veas los dos y puedas elegir. La pregunta 3 corre sobre una base a la que **le quitamos el `CHECK` a proposito**, para que primero veas el stock en -7 y despues lo resuelvas con la herramienta que la clase esta ensenando. Pero la respuesta correcta de diseno es la de la pregunta 4: esa regla mira una sola columna de la propia fila, asi que en el PI real va en un `CHECK (stock >= 0)`, que es una linea, no se puede olvidar y el motor aplica sin llamar a ningun codigo. El trigger se reserva para lo que el `CHECK` no puede: mirar el valor anterior, mirar otra tabla o dejar historia.

**En el plan de respaldo, ¿`pg_dump` no basta? Es lo unico que hemos visto.**

Le faltan dos cosas y las dos duelen. Una: `pg_dump` respalda **una base**, no los roles ni las contrasenas, que son del cluster; si restauras solo el dump te queda una base con todos los datos y sin un usuario que la pueda usar, y el `pg_restore` empieza a fallar al asignar propietarios. Para eso esta `pg_dumpall --globals-only`. Dos: un dump es una foto de un instante, asi que tu RPO es «desde el ultimo dump», y con un dump diario eso puede ser un dia entero de atencion. Bajarlo requiere archivar los WAL o, como minimo, un segundo dump al mediodia. Escribir «RPO de 15 minutos» con un solo dump diario es escribir un numero que el plan no puede cumplir.

---

## Cierre de la clase

- Al terminar, cada estudiante debe tener: `fn_precio_consulta` creada, `IMMUTABLE` y usada dentro de dos consultas —con Firulais en 45000 y 60750—; la tabla `audit_cita` con **2 filas y no 3**; el stock en -7 capturado **antes** del trigger y el insumo 2 en 1 despues; las cuatro afirmaciones correctas de la pregunta 4; y el `Plan_Backup_VetCare` con RPO, RTO y la consulta de validacion.
- Lo que hay que verificar antes de cerrar la sesion son **dos numeros y una coherencia**. Los numeros: que la auditoria tenga 2 filas —si tiene 3, falta el filtro y hay una fila con `PROGRAMADA -> PROGRAMADA`— y que el insumo 2 haya quedado en 1 y no en 3 —si quedo en 3, el trigger esta bloqueando tambien el descuento valido, casi siempre por `<= 0`—. La coherencia: que quien marco bien la pregunta 4 no haya escrito en la 3 que el trigger era la unica forma de proteger el stock. Proyectar una entrega voluntaria y leer esas tres cosas toma dos minutos y separa a quien entendio de quien copio la sintaxis.
- Dejar dicho en voz alta lo que sigue. El Corte 1 se cierra con el parcial de la Clase 5, y lo que se evalua de estas cuatro clases es exactamente lo que quedo escrito: la matriz de roles, el contrato de los procedimientos, la decision entre `CHECK`, trigger y aplicacion, y el plan de respaldo con su gap declarado. Y la Clase 6 arranca donde termino hoy la pregunta 1: la diferencia entre lo cobrado y la tarifa de referencia, que ahi se convierte en una consulta de control y en el primer problema de rendimiento del semestre.

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. El motor de la plataforma es PostgreSQL (PGlite en el navegador), no Oracle.
