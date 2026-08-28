# Solucion del taller · Clase 8 · Transacciones de facturacion y tuning de VetCare

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** `sp_facturar` completo, con el patron de `UPDATE` condicional que resuelve la comprobacion y el descuento en **una sola sentencia**, la factura 4 por **27.400** y los stocks en 11, 58 y 5; la prueba de atomicidad donde el descuento que **si** habia alcanzado se deshace y el insumo 3 vuelve a 40 —con el detalle que sorprende a todo el mundo, que la factura exitosa despues del fallo sale con el id **5** y no con el 4—; el patron encapsulado en `fn_descontar_stock` devolviendo `true/false/true` sin dejar un solo stock negativo; la explicacion exacta de por que la base quedo intacta; y el checklist de tuning del PI con el hueco de concurrencia declarado por escrito.

> **El motor es PostgreSQL, no Oracle,** y esta clase es donde mas se nota. No existe `SQL%ROWCOUNT`: se usa `GET DIAGNOSTICS v_filas = ROW_COUNT;`. **No se pone `COMMIT` ni `ROLLBACK` dentro del procedimiento:** cada sentencia de nivel superior ya es su propia transaccion, y si el procedimiento lanza una excepcion, todo lo que hizo se deshace solo. Y una diferencia que en Oracle es un error y aqui no: una funcion **puede** ejecutar `UPDATE` y llamarse desde un `SELECT`, que es exactamente lo que hace la pregunta 3. Dos avisos operativos. Uno: cada pregunta arranca con su propia base recien sembrada, asi que la pregunta 2 **ya trae** `sp_facturar` creado —la version de referencia— y no hay que volver a escribirlo. Dos: hay que anunciar antes de empezar que ExamLab corre con **una sola sesion**, de modo que el escenario de dos recepcionistas facturando el mismo insumo a la vez **no se puede reproducir aqui**; eso no es un defecto del taller, es literalmente el entregable 4 de la pregunta 5 y el punto de partida de la Clase 10.

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 8 - Tuning y transacciones/Taller PI - Clase 8 - VetCare.docx`
- Configuracion en la plataforma: `Kit docente/Clase 8/Taller en ExamLab - Clase 8 (configuracion).md`
- Caso de estudio: `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
- Hito del PI: Transaccion de negocio (factura + stock) + notas de tuning
- Entregable: Script transaccional + checklist tuning del PI (1 pag.)
- **Estas preguntas: 100 puntos** en 5 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 1 | sp_facturar: factura + detalle + descuento de stock, todo o nada | `bd_sql` | 35 |
| 2 | Probar la atomicidad: fallo a mitad de la factura | `bd_sql` | 25 |
| 3 | El patron de descuento seguro como funcion reutilizable | `bd_sql` | 15 |
| 4 | Que pasa con el bloque EXCEPTION en PL/pgSQL | `cerrada` | 10 |
| 5 | Checklist de tuning y transacciones del PI | `abierta` | 15 |

---

## Pregunta 1 · sp_facturar: factura + detalle + descuento de stock, todo o nada · 35 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
CREATE OR REPLACE PROCEDURE sp_facturar(
    p_id_consulta INT,
    p_insumos     INT[],
    p_cantidades  INT[]
)
LANGUAGE plpgsql
AS $proc$
DECLARE
  v_id_factura INT;
  v_total      NUMERIC(12,2) := 0;   -- se acumula linea por linea
  v_precio     NUMERIC(12,2);
  v_filas      INT;                  -- para GET DIAGNOSTICS
  i            INT;
BEGIN
  -- --------------------------------------------------------------------
  -- 1) Los dos arreglos tienen que venir parejos. IS DISTINCT FROM y no
  --    <> porque array_length de un arreglo vacio devuelve NULL, y
  --    NULL <> NULL es NULL: con <> la validacion no dispararia y el
  --    bucle de abajo no se ejecutaria ninguna vez, dejando una factura
  --    en cero sin una sola linea.
  -- --------------------------------------------------------------------
  IF array_length(p_insumos, 1) IS DISTINCT FROM array_length(p_cantidades, 1) THEN
    RAISE EXCEPTION 'ERROR: insumos y cantidades deben tener la misma longitud';
  END IF;

  -- --------------------------------------------------------------------
  -- 2) Cabecera primero, con total 0. Hay que insertarla antes que las
  --    lineas porque detalle_factura tiene una FK hacia factura, y
  --    RETURNING ... INTO es la unica forma correcta de recuperar el id
  --    que acaba de generar el SERIAL: currval() o un MAX(id_factura)
  --    serian una carrera con cualquier otra sesion.
  -- --------------------------------------------------------------------
  INSERT INTO factura (id_consulta, total) VALUES (p_id_consulta, 0)
  RETURNING id_factura INTO v_id_factura;

  -- --------------------------------------------------------------------
  -- 3) Una pasada por linea de la factura.
  -- --------------------------------------------------------------------
  FOR i IN 1 .. array_length(p_insumos, 1) LOOP

    -- El precio se toma de la tabla, NO se recibe por parametro: quien
    -- factura no debe poder decidir el precio. Y se guarda en el detalle
    -- (precio_unit) para que la factura de hoy no cambie si manana sube
    -- el insumo.
    SELECT precio_unit INTO v_precio FROM insumo WHERE id_insumo = p_insumos[i];
    IF NOT FOUND THEN
      RAISE EXCEPTION 'ERROR: el insumo % no existe', p_insumos[i];
    END IF;

    -- ----------------------------------------------------------------
    -- EL PATRON DE LA CLASE. La comprobacion del stock va DENTRO del
    -- WHERE, no en un IF anterior. Asi comprobar y descontar son UNA
    -- sola sentencia: no hay ninguna ventana entre el "hay stock" y el
    -- "lo descuento" en la que otra sesion pueda meterse.
    -- Si no habia suficiente, el UPDATE no encuentra fila que cumpla la
    -- condicion y afecta 0 filas -- no falla, simplemente no hace nada --
    -- y por eso hay que preguntarle cuantas filas toco.
    -- ----------------------------------------------------------------
    UPDATE insumo
       SET stock = stock - p_cantidades[i]
     WHERE id_insumo = p_insumos[i]
       AND stock >= p_cantidades[i];

    GET DIAGNOSTICS v_filas = ROW_COUNT;   -- en Oracle seria SQL%ROWCOUNT
    IF v_filas = 0 THEN
      RAISE EXCEPTION 'ERROR: stock insuficiente del insumo % (se pidieron %)',
        p_insumos[i], p_cantidades[i];
    END IF;

    INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit)
    VALUES (v_id_factura, p_insumos[i], p_cantidades[i], v_precio);

    v_total := v_total + (v_precio * p_cantidades[i]);
  END LOOP;

  -- --------------------------------------------------------------------
  -- 4) Recien ahora se sabe el total. Y NO va ningun COMMIT aqui: el
  --    CALL de nivel superior ya es su propia transaccion. Si algo de
  --    arriba hubiera fallado, nada de esto existiria.
  -- --------------------------------------------------------------------
  UPDATE factura SET total = v_total WHERE id_factura = v_id_factura;

  RAISE NOTICE 'Factura % creada por %', v_id_factura, v_total;
END;
$proc$;

-- ======================================================================
-- CASO EXITOSO: 1 vacuna antirrabica (22.000), 2 jeringas (900) y
-- 3 gasas (1.200) para la consulta 4.
-- ======================================================================
CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3]);

SELECT f.id_factura, f.id_consulta, f.total FROM factura f ORDER BY f.id_factura;

SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;

-- ======================================================================
-- Comprobacion de una linea, la que conviene pegar al calificar: el
-- total tiene que cuadrar con la suma de su propio detalle, no con un
-- numero escrito a mano.
-- ======================================================================
SELECT f.id_factura,
       f.total                                     AS total_en_la_cabecera,
       SUM(d.cantidad * d.precio_unit)             AS suma_del_detalle,
       f.total - SUM(d.cantidad * d.precio_unit)   AS debe_ser_cero,
       COUNT(*)                                    AS lineas
  FROM factura f
  JOIN detalle_factura d ON d.id_factura = f.id_factura
 WHERE f.id_factura = 4
 GROUP BY f.id_factura, f.total;
```

### Salida esperada

```
NOTICE:  Factura 4 creada por 27400.00

Facturas -- 4 filas

 id_factura | id_consulta |   total
------------+-------------+-----------
          1 |           1 |  71000.00
          2 |           2 |  47000.00
          3 |           3 |  60200.00
          4 |           4 |  27400.00     <-- la nueva

Insumos -- 6 filas

 id_insumo |         nombre          | stock
-----------+-------------------------+-------
         1 | Vacuna antirrabica      |    11     <-- 12 - 1
         2 | Vacuna triple felina    |     3
         3 | Antiparasitario oral    |    40
         4 | Suero fisiologico 500ml |    25
         5 | Gasa esteril            |     5     <-- 8 - 3
         6 | Jeringa 5ml             |    58     <-- 60 - 2

Comprobacion -- 1 fila

 id_factura | total_en_la_cabecera | suma_del_detalle | debe_ser_cero | lineas
------------+----------------------+------------------+---------------+--------
          4 |             27400.00 |         27400.00 |          0.00 |      3

Los cuatro numeros de la pregunta son 27.400, 11, 58 y 5, y conviene tenerlos a
la vista al calificar porque cada desviacion tiene una causa distinta:

  * Total 27.400 = 22.000x1 + 900x2 + 1.200x3. Si sale 24.100 (22.000 + 900 +
    1.200), el estudiante acumulo el precio sin multiplicar por la cantidad. Si
    sale 0, le falto el UPDATE factura SET total = ... del paso 4 y la cabecera
    quedo con el cero con que nacio.
  * Stocks 11, 58 y 5. Si los tres bajaron UNA sola unidad cada uno, el UPDATE
    dice stock = stock - 1 en vez de stock - p_cantidades[i].
  * detalle_factura pasa de 8 filas a 11. Si quedaron 9, el INSERT del detalle
    esta fuera del bucle.
  * La factura nueva es la 4 y su id_consulta es 4. Coinciden por casualidad
    --hay 3 facturas previas y la consulta pedida es la 4--; no es que el
    procedimiento copie uno en el otro.

El RAISE NOTICE final no se exige, pero cuando esta ahorra media hora de
depuracion en la pregunta 2: es la unica forma de ver el id y el total sin
consultar nada.
```

### Como calificar

- **5 pts — la firma exacta** `sp_facturar(p_id_consulta INT, p_insumos INT[], p_cantidades INT[])` como **procedimiento** en `plpgsql`, mas la validacion de que los dos arreglos vengan parejos con su `RAISE EXCEPTION`. Se acepta `<>` en lugar de `IS DISTINCT FROM`; se anota en la devolucion por que el segundo es mejor —con un arreglo vacio, `array_length` devuelve `NULL` y la comparacion con `<>` no dispara—.
- **5 pts — `RETURNING id_factura INTO v_id_factura`.** Es un requisito explicito de la rubrica. Resolverlo con `SELECT MAX(id_factura) INTO ...` o con `currval()` vale 2 de los 5, y la devolucion tiene que decir por que: el `MAX` es una carrera con cualquier otra sesion, y este taller entero es sobre no dejar carreras abiertas.
- **12 pts — el nucleo: el bucle con el `UPDATE` condicional.** 3 pts el `FOR i IN 1 .. array_length(p_insumos, 1) LOOP`; **5 pts que la comprobacion del stock este en el `WHERE` del `UPDATE`** y no en un `IF` previo —es el aprendizaje de la clase y el que la pregunta 3 vuelve a pedir—; 4 pts el `GET DIAGNOSTICS v_filas = ROW_COUNT;` con su `IF v_filas = 0 THEN RAISE EXCEPTION`. Un `IF` previo que lee y luego decide vale 0 de esos 5 aunque el resultado del caso exitoso sea correcto: funciona por casualidad, porque hay una sola sesion.
- **5 pts — el detalle y el total.** 2 pts el `INSERT INTO detalle_factura` **dentro** del bucle con el `precio_unit` leido de la tabla, y 3 pts el `UPDATE factura SET total = v_total` al final. Se verifica con la comprobacion de una linea: `total - SUM(cantidad * precio_unit)` tiene que dar **0**.
- **5 pts — el caso exitoso ejecutado, con los cuatro numeros:** factura 4 con total **27.400** y stocks en **11, 58 y 5**. 2 pts el `CALL` mas los dos `SELECT` finales que pide el enunciado, y 3 pts que los numeros salgan.
- **3 pts — no aparece `COMMIT` dentro del procedimiento y no aparece `SQL%ROWCOUNT`.** La rubrica lo verifica de forma explicita. Un `COMMIT` dentro **rompe la atomicidad** que la pregunta 2 va a medir: se pierden los 3 pts y hay que avisarlo antes de que llegue a la pregunta 2, porque si no va a concluir lo contrario de lo que la clase ensena.

### Errores frecuentes y que hacer

- **Leer el stock y decidir despues:** `SELECT stock INTO v_stock ...; IF v_stock >= p_cantidades[i] THEN UPDATE ...`. Es el error central de la clase y el mas dificil de ver, porque en ExamLab **funciona**: con una sola sesion nunca se pierde la carrera. Entre el `SELECT` y el `UPDATE` hay una ventana en la que otra recepcionista puede haberse llevado la ultima vacuna. La condicion va en el `WHERE`, y la pregunta 3 pide justificar exactamente eso.
- **Poner `COMMIT` dentro del procedimiento,** por costumbre de Oracle. Es la peor consecuencia posible en este taller: la cabecera de la factura queda confirmada, y cuando la linea 2 falle la factura huerfana **se queda**. La pregunta 2 va a mostrar `factura` con 4 filas en vez de 3 y el estudiante va a concluir que PostgreSQL no es atomico.
- **`GET DIAGNOSTICS` sin usar,** o mal escrito. Tres variantes reales: declararlo y no comprobar nunca `v_filas`; escribir `v_filas := SQL%ROWCOUNT`, que es Oracle y no compila; o comprobar `IF v_filas > 0 THEN RAISE EXCEPTION`, invirtiendo la condicion —entonces falla el caso bueno y pasa el malo—. Sin la comprobacion, el `UPDATE` que no afecta filas **no falla**: la factura sale con el detalle escrito y el stock sin descontar.
- **`v_total := v_total + v_precio`,** olvidando la cantidad. Da **24.100** en vez de 27.400 y es facil de pasar por alto porque el numero parece razonable. La comprobacion `total - SUM(cantidad * precio_unit) = 0` lo detecta sin tener que hacer cuentas.
- **El `INSERT` del detalle fuera del bucle,** o el `UPDATE factura` **dentro** del bucle. El primero deja una sola linea de tres —`detalle_factura` queda en 9 y no en 11—; el segundo funciona pero escribe tres veces la cabecera y es un habito caro cuando la factura tenga treinta lineas.
- **Recibir el precio por parametro** o escribirlo a mano en el `INSERT`. Dos problemas de una vez: quien factura no debe poder decidir el precio, y el detalle debe conservar el precio **vigente al facturar** para que la factura de hoy no cambie cuando el insumo suba de precio. Por eso `detalle_factura` tiene su propia columna `precio_unit`.

---

## Pregunta 2 · Probar la atomicidad: fallo a mitad de la factura · 25 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- ======================================================================
-- 1) FOTO INICIAL. Una sola fila, para poder compararla de un vistazo
--    con la foto final. Aqui sp_facturar YA VIENE CREADO en la base.
-- ======================================================================
SELECT (SELECT COUNT(*) FROM factura)                  AS facturas,
       (SELECT COUNT(*) FROM detalle_factura)          AS detalles,
       (SELECT stock FROM insumo WHERE id_insumo = 3)  AS stock_insumo_3,
       (SELECT stock FROM insumo WHERE id_insumo = 2)  AS stock_insumo_2;

-- ======================================================================
-- 2) EL INTENTO QUE DEBE FALLAR A MITAD DE CAMINO.
--    Linea 1: 2 unidades del insumo 3, que tiene 40  -> alcanza y se
--             descuenta de verdad (queda en 38).
--    Linea 2: 10 unidades del insumo 2, que tiene 3   -> NO alcanza.
--    El DO con EXCEPTION captura el error para que el script siga; sin
--    el, la plataforma se detendria aqui y no habria foto final.
-- ======================================================================
DO $$
BEGIN
  CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 10]);
  RAISE NOTICE 'No deberia llegar aqui';
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'Fallo esperado: %', SQLERRM;
END $$;

-- ======================================================================
-- 3) FOTO FINAL. La MISMA consulta del punto 1, sin cambiarle una coma:
--    si se cambia, la comparacion no vale.
-- ======================================================================
SELECT (SELECT COUNT(*) FROM factura)                  AS facturas,
       (SELECT COUNT(*) FROM detalle_factura)          AS detalles,
       (SELECT stock FROM insumo WHERE id_insumo = 3)  AS stock_insumo_3,
       (SELECT stock FROM insumo WHERE id_insumo = 2)  AS stock_insumo_2;

-- Version directa de la comparacion, la que se pega al calificar: si los
-- cuatro dicen true, la atomicidad quedo demostrada.
SELECT (SELECT COUNT(*) FROM factura) = 3                  AS no_hay_factura_huerfana,
       (SELECT COUNT(*) FROM detalle_factura) = 8          AS no_hay_lineas_nuevas,
       (SELECT stock FROM insumo WHERE id_insumo = 3) = 40 AS el_descuento_parcial_se_deshizo,
       (SELECT stock FROM insumo WHERE id_insumo = 2) = 3  AS el_insumo_2_intacto;

-- ======================================================================
-- 4) COMPARACION Y CONCLUSION.
--
-- ANTES:   facturas 3 | detalles 8 | insumo 3 -> 40 | insumo 2 -> 3
-- DESPUES: facturas 3 | detalles 8 | insumo 3 -> 40 | insumo 2 -> 3
--          ... es decir, IDENTICO.
--
-- Y no es que el procedimiento no hubiera hecho nada antes de fallar:
-- alcanzo a insertar la cabecera de la factura, alcanzo a bajar el stock
-- del insumo 3 de 40 a 38 y alcanzo a escribir la primera linea del
-- detalle. TODO ESO SE DESHIZO cuando la segunda linea lanzo la
-- excepcion. El dato que lo prueba es el mas importante de la pregunta:
-- el stock del insumo 3 VOLVIO A 40. Si solo se mirara el conteo de
-- facturas, no se sabria si el procedimiento fallo antes o despues de
-- empezar a trabajar.
--
-- El mecanismo: el CALL de nivel superior es su propia transaccion, y al
-- propagarse la excepcion se revierte completa. El bloque
-- BEGIN ... EXCEPTION del DO agrega un savepoint implicito, que es lo que
-- permite capturar el error y seguir con el script -- pero lo que se
-- deshizo, se deshizo igual.
--
-- LO UNICO que NO se deshace es la secuencia del SERIAL: el id 4 de
-- factura quedo consumido. Las secuencias viven fuera de la transaccion
-- a proposito, porque si volvieran atras dos sesiones podrian recibir el
-- mismo id. Por eso la factura buena del paso 5 sale con el id 5.
-- ======================================================================

-- ======================================================================
-- 5) LA MISMA FACTURA, AHORA VIABLE: 3 unidades del insumo 2 en vez de
--    10. Mismo procedimiento, mismos insumos, misma consulta.
-- ======================================================================
CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 3]);

SELECT f.id_factura, f.id_consulta, f.total FROM factura f ORDER BY f.id_factura;

SELECT d.id_detalle, d.id_factura, d.id_insumo, d.cantidad, d.precio_unit
  FROM detalle_factura d
 WHERE d.id_factura = (SELECT MAX(id_factura) FROM factura)
 ORDER BY d.id_detalle;

SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;
```

### Salida esperada

```
FOTO INICIAL -- 1 fila

 facturas | detalles | stock_insumo_3 | stock_insumo_2
----------+----------+----------------+----------------
        3 |        8 |             40 |              3

EL INTENTO QUE FALLA

NOTICE:  Fallo esperado: ERROR: stock insuficiente del insumo 2 (se pidieron 10)
DO

El NOTICE 'No deberia llegar aqui' NO aparece: la excepcion corto el CALL antes.
Y el bloque termina en DO, no en ERROR, porque el EXCEPTION lo capturo -- que es
lo que permite que el script continue.

FOTO FINAL -- 1 fila

 facturas | detalles | stock_insumo_3 | stock_insumo_2
----------+----------+----------------+----------------
        3 |        8 |             40 |              3

Comparacion directa -- 1 fila

 no_hay_factura_huerfana | no_hay_lineas_nuevas | el_descuento_parcial_se_deshizo | el_insumo_2_intacto
-------------------------+----------------------+---------------------------------+---------------------
 t                       | t                    | t                               | t

El 40 es el numero de la pregunta. Los otros tres se pueden explicar diciendo que
el procedimiento «no llego a hacer nada», pero el insumo 3 SI habia bajado a 38
antes del fallo, y volvio solo. Eso es lo que la rubrica exige evidenciar y lo que
se descuenta si falta.

PASO 5 -- la misma factura, ahora viable

NOTICE:  Factura 5 creada por 112000.00

Facturas -- 4 filas

 id_factura | id_consulta |   total
------------+-------------+-----------
          1 |           1 |  71000.00
          2 |           2 |  47000.00
          3 |           3 |  60200.00
          5 |           4 | 112000.00     <-- el id 5, NO el 4

Detalle de la factura 5 -- 2 filas

 id_detalle | id_factura | id_insumo | cantidad | precio_unit
------------+------------+-----------+----------+-------------
          9 |          5 |         3 |        2 |     9500.00
         10 |          5 |         2 |        3 |    31000.00

Insumos -- 6 filas

 id_insumo |         nombre          | stock
-----------+-------------------------+-------
         1 | Vacuna antirrabica      |    12
         2 | Vacuna triple felina    |     0     <-- 3 - 3, exactamente en el limite
         3 | Antiparasitario oral    |    38     <-- 40 - 2, ahora si de verdad
         4 | Suero fisiologico 500ml |    25
         5 | Gasa esteril            |     8
         6 | Jeringa 5ml             |    60

Total 112.000 = 9.500x2 + 31.000x3. Y hay dos cosas que vale la pena senalar en
clase con esta salida delante:

  1. La factura salio con el id 5, no con el 4, y no es un error de nadie. El
     intento fallido consumio el 4 de la secuencia, y las secuencias NO vuelven
     atras con el ROLLBACK --a proposito: si volvieran, dos sesiones podrian
     recibir el mismo id--. En cualquier base real hay huecos en los ids y no
     significan datos perdidos: significan intentos que fallaron. Ese detalle no
     hay que explicarlo en el enunciado, pero si hay que estar preparado para la
     pregunta «¿por que hay huecos?».
  2. El insumo 2 quedo en 0 y no en negativo. Es el caso limite exacto: se
     pidieron 3 de 3. El WHERE stock >= p_cantidades[i] acepta la igualdad, que
     es lo correcto --pedir todo lo que hay es una venta valida--, y el
     CHECK (stock >= 0) de la tabla nunca tuvo que intervenir. Los dos
     mecanismos coinciden, que es la senal de que el diseno esta bien.
```

### Como calificar

- **5 pts — la foto inicial y la foto final con la MISMA consulta,** 2 pts cada una y 1 pt que sean literalmente identicas. Si la consulta cambia entre las dos, no hay comparacion posible y se pierden los 5.
- **5 pts — el intento invalido se captura sin abortar el script.** El `DO` con su `EXCEPTION WHEN OTHERS` viene dado en el enunciado, asi que estos puntos se dan por ejecutarlo y por mostrar el `NOTICE` con el `SQLERRM`. Si el script murio en un `ERROR` y no hay foto final, la pregunta se queda sin la mitad de su evidencia.
- **8 pts — la demostracion con datos, 2 pts por cada una de las cuatro afirmaciones:** `factura` sigue en 3, `detalle_factura` sigue en 8, **el stock del insumo 3 volvio a 40** y el insumo 2 quedo intacto en 3. La tercera es la que la rubrica exige de forma explicita: **si no se evidencia la reversion del stock del primer insumo, se descuenta**, porque es la unica que prueba que hubo trabajo hecho y deshecho.
- **4 pts — la comparacion y la conclusion escritas en comentarios `--`.** No basta con que los numeros esten: la rubrica pide compararlos «explicitamente». Se dan los 4 pts cuando el comentario dice **que alcanzo a hacer** el procedimiento antes de fallar y **que se deshizo**. Una conclusion que solo diga «no quedo nada» vale 2 de 4.
- **3 pts — la segunda llamada viable se ejecuta y se muestra el contraste.** Total **112.000**, insumo 3 en 38 e insumo 2 en 0. Sin este paso la pregunta solo demuestra que la base sabe deshacer, no que sabe hacer.
- **Se reconoce como sobresaliente, sin puntos extra:** notar que la factura buena salio con el **id 5** y explicar por que —las secuencias no vuelven atras con el `ROLLBACK`, y no vuelven a proposito—. Casi nadie lo nota y es un dato que en produccion evita dos horas de confusion. Si nadie del grupo lo menciona, conviene proyectarlo y preguntarlo.

### Errores frecuentes y que hacer

- **Mostrar solo el conteo de facturas.** «`factura` sigue en 3, luego hubo `ROLLBACK`» es una conclusion debil: seria igual de cierta si el procedimiento hubiera fallado **antes** de insertar la cabecera. Lo que prueba la atomicidad es el **40** del insumo 3, porque ese descuento **si** se hizo y **si** se deshizo. Es exactamente lo que la rubrica manda descontar.
- **Cambiar la consulta entre la foto inicial y la final** —agregar una columna, mirar otro insumo, contar de otra tabla—. Entonces las dos fotos no son comparables y toda la pregunta se queda sin sustento. Se copia y se pega, literal.
- **Ejecutar el `CALL` invalido sin el `DO ... EXCEPTION`.** La plataforma corta el script en el error y no queda foto final. La captura no es un adorno: es lo que permite que la prueba y su verificacion vivan en la misma respuesta.
- **Concluir que «PostgreSQL no es atomico» porque quedo una factura huerfana.** Cuando esto aparece, el problema no esta en la pregunta 2: hay un `COMMIT` dentro del `sp_facturar` de la pregunta 1. Vale la pena revisar las dos preguntas juntas antes de calificar, porque la confusion se arrastra.
- **Reportar que la factura buena es la 4.** Es la 5, y quien escriba 4 normalmente no la ejecuto o la ejecuto en la base de la pregunta 1. No se descuenta por no **explicar** el salto, pero si por reportar un numero que su propia salida no muestra.
- **Interpretar el insumo 2 en `0` como un error.** Es el caso limite correcto: se pidieron 3 de 3 y `stock >= cantidad` acepta la igualdad. Un stock en cero es un dato de negocio —hay que reponer—, no una violacion; la violacion seria un **negativo**, y para eso estan el patron y el `CHECK`.

---

## Pregunta 3 · El patron de descuento seguro como funcion reutilizable · 15 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
CREATE OR REPLACE FUNCTION fn_descontar_stock(
    p_id_insumo INT,
    p_cantidad  INT
)
RETURNS BOOLEAN
LANGUAGE plpgsql
-- Sin IMMUTABLE ni STABLE: esta funcion ESCRIBE. El valor por omision es
-- VOLATILE y es el correcto; marcarla STABLE haria que el motor se
-- sintiera libre de reusar un resultado anterior, y aqui cada llamada
-- tiene que ejecutarse de verdad.
AS $fn$
DECLARE
  v_filas INT;
BEGIN
  -- Una cantidad de 0 o negativa NO es "no hay stock": es una llamada mal
  -- hecha, y por eso aqui SI se lanza excepcion. Ojo con el detalle: sin
  -- esta validacion, p_cantidad = -5 haria stock = stock + 5 y el UPDATE
  -- devolveria TRUE. Un regalo de inventario disfrazado de descuento.
  IF p_cantidad IS NULL OR p_cantidad <= 0 THEN
    RAISE EXCEPTION 'ERROR: la cantidad a descontar debe ser mayor que cero (llego %)',
      p_cantidad;
  END IF;

  -- El patron de la clase, otra vez: comprobar y descontar en UNA sola
  -- sentencia. La condicion del stock esta en el WHERE.
  UPDATE insumo
     SET stock = stock - p_cantidad
   WHERE id_insumo = p_id_insumo
     AND stock >= p_cantidad;

  GET DIAGNOSTICS v_filas = ROW_COUNT;

  -- Y aqui esta la diferencia de diseno con sp_facturar: "no hay stock"
  -- es una RESPUESTA, no un error. Quien llama decide que hacer con el
  -- FALSE -- ofrecer un sustituto, avisar al mostrador, apartar el
  -- pedido -- en vez de recibir una excepcion que le tumba la
  -- transaccion entera.
  RETURN v_filas = 1;
END;
$fn$;

-- ======================================================================
-- PRUEBA. Las tres respuestas en una sola fila, tal como pide el
-- enunciado. Y observese lo que esto significa: una funcion que hace
-- UPDATE, llamada desde un SELECT. En Oracle seria un error; en
-- PostgreSQL es legal y aqui es lo que se pide.
-- ======================================================================
SELECT fn_descontar_stock(5, 3)  AS caso_ok,         -- insumo 5 tiene 8 -> alcanza
       fn_descontar_stock(2, 10) AS caso_sin_stock,  -- insumo 2 tiene 3 -> no alcanza
       fn_descontar_stock(2, 3)  AS caso_limite;     -- insumo 2 tiene 3 -> justo justo

-- ======================================================================
-- ESTADO FINAL: ningun stock negativo.
-- ======================================================================
SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;

-- Comprobacion de una linea, la que conviene pegar al calificar.
SELECT COUNT(*) FILTER (WHERE stock < 0)              AS negativos_debe_ser_cero,
       (SELECT stock FROM insumo WHERE id_insumo = 5) AS insumo_5_debe_ser_5,
       (SELECT stock FROM insumo WHERE id_insumo = 2) AS insumo_2_debe_ser_0
  FROM insumo;

-- Y la comprobacion de que la validacion de la cantidad tambien funciona:
-- esto tiene que fallar, no devolver TRUE.
DO $$
BEGIN
  PERFORM fn_descontar_stock(1, -5);
  RAISE NOTICE 'MAL: acepto una cantidad negativa';
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'Bien, la rechazo: %', SQLERRM;
END $$;

-- ======================================================================
-- POR QUE ESTE PATRON Y NO "leer primero, decidir despues"
--
-- El patron inseguro es este:
--     SELECT stock INTO v_stock FROM insumo WHERE id_insumo = X;
--     IF v_stock >= v_cantidad THEN
--       UPDATE insumo SET stock = stock - v_cantidad WHERE id_insumo = X;
--     END IF;
--
-- Entre el SELECT y el UPDATE hay una VENTANA. Con dos recepcionistas
-- facturando la ultima vacuna al mismo tiempo:
--
--   Sesion A: SELECT stock -> 1     "hay una, sigo"
--   Sesion B: SELECT stock -> 1     "hay una, sigo"   <-- las dos leyeron 1
--   Sesion A: UPDATE stock = 1 - 1 = 0                (correcto)
--   Sesion B: UPDATE stock = 0 - 1 = -1               (ya no habia)
--
-- Las dos leyeron un dato que era cierto cuando lo leyeron y falso cuando
-- actuaron. El nombre del problema es "comprobar y luego usar": la
-- decision se toma sobre una foto vieja.
--
-- Con la condicion en el WHERE no hay ventana, porque comprobar y
-- escribir son la MISMA sentencia y el motor bloquea la fila mientras la
-- modifica. En el nivel de aislamiento por omision de PostgreSQL
-- (READ COMMITTED), cuando la sesion B intenta actualizar una fila que A
-- esta cambiando, B ESPERA a que A termine y despues VUELVE A EVALUAR su
-- propio WHERE contra la version nueva de la fila. Entonces ve stock = 0,
-- la condicion stock >= 1 ya no se cumple, el UPDATE afecta 0 filas y la
-- funcion devuelve FALSE. Nadie queda en negativo y nadie tuvo que
-- coordinarse con nadie.
--
-- Y hay una segunda red, de la Clase 4: el CHECK (stock >= 0) de la
-- tabla. Si el patron estuviera mal escrito, el CHECK abortaria la
-- sentencia. La diferencia es que el CHECK GARANTIZA -- nunca habra un
-- negativo -- mientras el patron del WHERE EXPLICA y ademas permite
-- responder con elegancia: FALSE en vez de una excepcion.
--
-- LIMITE HONESTO: en ExamLab hay UNA sola sesion, asi que la carrera de
-- arriba NO se puede reproducir aqui. Lo escrito es el razonamiento, no
-- una medicion. Comprobarlo con dos sesiones es el tema de la Clase 10 y
-- es el "gap honesto" que pide la pregunta 5.
-- ======================================================================
```

### Salida esperada

```
Prueba -- 1 fila

 caso_ok | caso_sin_stock | caso_limite
---------+----------------+-------------
 t       | f              | t

true / false / true es el resultado de la pregunta. Y hay algo elegante en esta
prueba que conviene senalar: da lo mismo en que orden evalue el motor las tres
llamadas. Si fn_descontar_stock(2, 3) corriera antes que fn_descontar_stock(2,
10), el insumo 2 quedaria en 0 y la de 10 seguiria devolviendo false. La prueba
es correcta sin depender del orden de evaluacion de la lista de columnas, que es
algo que PostgreSQL NO garantiza y en lo que no conviene apoyarse.

Estado final -- 6 filas

 id_insumo |         nombre          | stock
-----------+-------------------------+-------
         1 | Vacuna antirrabica      |    12
         2 | Vacuna triple felina    |     0     <-- 3 - 3 (caso limite)
         3 | Antiparasitario oral    |    40
         4 | Suero fisiologico 500ml |    25
         5 | Gasa esteril            |     5     <-- 8 - 3 (caso ok)
         6 | Jeringa 5ml             |    60

El insumo 2 quedo en 0 y no en -7: la llamada de 10 unidades no toco nada. Eso es
el WHERE haciendo su trabajo, no el CHECK salvando la situacion -- y la
diferencia importa, porque un CHECK que salta aborta la sentencia mientras que el
WHERE simplemente responde false.

Comprobacion -- 1 fila

 negativos_debe_ser_cero | insumo_5_debe_ser_5 | insumo_2_debe_ser_0
-------------------------+---------------------+---------------------
                       0 |                   5 |                   0

Validacion de la cantidad

NOTICE:  Bien, la rechazo: ERROR: la cantidad a descontar debe ser mayor que cero (llego -5)

Esta ultima prueba no la pide el enunciado y vale la pena hacerla en clase,
porque el agujero que tapa no es evidente: sin la validacion, una cantidad
negativa haria stock = stock - (-5), es decir stock + 5, y la funcion devolveria
true. Un regalo de inventario disfrazado de descuento, y ademas silencioso.
```

### Como calificar

- **4 pts — la firma y el tipo de retorno:** `fn_descontar_stock(p_id_insumo INT, p_cantidad INT)` **`RETURNS BOOLEAN`** en `plpgsql`. Tiene que ser una `FUNCTION`, no un `PROCEDURE`: un procedimiento no puede llamarse desde el `SELECT` de prueba que pide el enunciado. Se descuenta si se declaro `IMMUTABLE` o `STABLE` —hace `UPDATE`, tiene que ser `VOLATILE`, que es lo que ya es por omision—.
- **3 pts — la validacion de `p_cantidad > 0` con `RAISE EXCEPTION`.** Se reconoce como sobresaliente quien ademas cubra el `NULL` con `p_cantidad IS NULL OR p_cantidad <= 0`, porque `NULL <= 0` es `NULL` y no dispara el `IF`.
- **4 pts — el `UPDATE` condicional con `GET DIAGNOSTICS` y el `RETURN v_filas = 1`.** 2 pts que la condicion del stock este en el `WHERE` y 2 pts que devuelva `FALSE` **sin lanzar excepcion** cuando no alcanza. Un `RAISE EXCEPTION` en el caso de stock insuficiente vale 0 de esos 2: contradice de frente el enunciado, que dice que aqui «no hay stock» es una respuesta y no un error.
- **2 pts — la prueba devuelve `true / false / true`** y el estado final deja el insumo 5 en **5**, el 2 en **0** y **ningun negativo**. Es la unica verificacion objetiva de la pregunta y no admite interpretacion.
- **2 pts — el comentario `--` explica bien las dos cosas:** por que leer-y-despues-decidir es vulnerable con varios usuarios, y por que la condicion en el `WHERE` lo evita al resolver comprobacion y escritura en una sola sentencia. Se dan los 2 pts completos cuando el estudiante narra la carrera con las dos sesiones intercaladas; una frase generica sobre «concurrencia» vale 1.
- **Se reconoce como sobresaliente, sin puntos extra,** cualquiera de estas tres: mencionar que en `READ COMMITTED` la segunda sesion **espera y vuelve a evaluar** su `WHERE` contra la fila nueva —que es el mecanismo real, no una metafora—; distinguir que el `CHECK (stock >= 0)` **garantiza** mientras el `WHERE` **explica y responde**; o senalar que con una sola sesion en ExamLab la carrera **no se puede reproducir** y que lo escrito es razonamiento, no medicion. Esa ultima es literalmente el entregable 4 de la pregunta 5.

### Errores frecuentes y que hacer

- **Lanzar excepcion cuando no hay stock.** Es la confusion de diseno de la pregunta y viene de copiar `sp_facturar` sin leer el enunciado. Las dos decisiones son correctas **en su sitio**: en `sp_facturar` la excepcion es necesaria porque tiene que abortar la factura completa; en `fn_descontar_stock` el `FALSE` deja que quien llama decida —ofrecer un sustituto, avisar, apartar el pedido— sin perder su transaccion.
- **Devolver `TRUE` siempre,** o devolver `v_filas` en vez de `v_filas = 1`. Lo primero pasa cuando se olvida el `GET DIAGNOSTICS` y se devuelve un literal; lo segundo no compila, porque `INT` no es `BOOLEAN`. La prueba lo delata al instante: `caso_sin_stock` tiene que salir **`f`**.
- **Volver al patron inseguro dentro de la funcion:** `SELECT stock INTO ...` y luego un `IF`. Aqui es especialmente grave, porque la pregunta entera consiste en **encapsular el patron seguro** para poder reutilizarlo. Si la funcion es insegura, se acaba de crear una herramienta que propaga el error a todo el proyecto.
- **Omitir la validacion de la cantidad** y no darse cuenta de lo que abre: `fn_descontar_stock(1, -5)` haria `stock - (-5) = stock + 5`, cumpliria `stock >= -5` sin problema y devolveria `TRUE`. Un aumento de inventario silencioso, autorizado por una funcion que se llama «descontar». Vale la pena mostrar esta linea en clase.
- **Declarar la funcion como `PROCEDURE`,** y despues no poder ejecutar el `SELECT` de prueba. Un `PROCEDURE` se invoca con `CALL` y no devuelve valor; lo que la pregunta necesita es un valor de retorno dentro de un `SELECT`.
- **Explicar la vulnerabilidad sin narrarla.** «Puede haber problemas de concurrencia» no explica nada. Lo que se pide es la secuencia: A lee 1, B lee 1, A descuenta a 0, B descuenta a -1. Con cuatro lineas queda claro; sin ellas, el estudiante repitio una frase que oyo.

---

## Pregunta 4 · Que pasa con el bloque EXCEPTION en PL/pgSQL · 10 pts

### Clave y por que

La clave se lee del banco de la plataforma, asi que esta es la que se califica. La columna de la derecha es lo que hay que poder responderle al estudiante cuando pregunte.

|  | Opcion | Por que |
|---|---|---|
| no | Porque el procedimiento incluia un ROLLBACK explicito en su bloque EXCEPTION, igual que en Oracle. | **Incorrecta, y es la respuesta que da quien viene de Oracle.** En PostgreSQL **no se pone** `ROLLBACK` dentro de un procedimiento: el `sp_facturar` de referencia no tiene ninguno —se puede verificar en la propia base de la pregunta 2— y la reversion ocurrio igual. Es mas: poner un `COMMIT` ahi dentro es lo que **rompe** la atomicidad, porque confirma la cabecera de la factura antes de que fallen las lineas. |
| no | Porque PostgreSQL guarda automaticamente una copia de seguridad de cada tabla antes de cada CALL. | **Incorrecta,** y ninguna base de datos serie funciona asi. Copiar cada tabla antes de cada `CALL` seria inviable con tablas grandes. El mecanismo real es el opuesto y mucho mas barato: PostgreSQL escribe versiones **nuevas** de las filas modificadas y, al abortar, esas versiones simplemente **nunca se vuelven visibles** para nadie. No se restaura nada, se descarta lo que se habia escrito. |
| **SI** | Porque la sentencia CALL de nivel superior es su propia transaccion: al propagarse la excepcion, todo el trabajo hecho dentro del procedimiento se deshace. Ademas, un bloque BEGIN ... EXCEPTION en PL/pgSQL crea un savepoint implicito, asi que al capturar el error se revierte solo lo hecho dentro de ese bloque. | **Correcta, y hay que quedarse con las dos mitades porque son dos mecanismos distintos.** *Primera mitad:* la sentencia `CALL` de nivel superior es su propia transaccion —PostgreSQL no necesita un `BEGIN` explicito para tenerla—, asi que cuando la excepcion se propaga hacia afuera, **todo** el trabajo del procedimiento se deshace: la cabecera de la factura, el descuento del insumo 3 de 40 a 38 y la primera linea del detalle. *Segunda mitad:* un bloque `BEGIN ... EXCEPTION` en PL/pgSQL crea un **savepoint implicito**, y eso es lo que permite que el `DO` de la pregunta 2 capture el error y el script continue: se revierte lo hecho dentro de ese bloque y la ejecucion sigue por el manejador. Sin la primera mitad no habria atomicidad; sin la segunda, no habria foto final. |
| no | Porque los UPDATE sobre insumo no se aplican hasta que el procedimiento termina; PL/pgSQL los acumula en memoria y los escribe al final. | **Incorrecta, y es la mas tentadora de las cuatro falsas** porque explica bien el resultado con el mecanismo equivocado. PL/pgSQL **no** acumula nada en memoria: cada `UPDATE` se aplica de verdad, y dentro de la misma transaccion el propio procedimiento **puede volver a leer** el stock ya descontado. Se comprueba sin salir del taller: si los `UPDATE` no se aplicaran hasta el final, el patron `WHERE stock >= cantidad` no podria funcionar cuando la misma factura descuenta dos veces el mismo insumo, y funciona. |
| no | Porque el trigger de stock deshizo los cambios anteriores al detectar la excepcion. | **Incorrecta, y en esta base es facil de descartar: no hay ningun trigger.** El trigger de stock es de la **Clase 4** y aqui no existe; lo que protege el stock en esta base son el `CHECK (stock >= 0)` de la tabla y el patron del `WHERE`. Y hay un error conceptual mas de fondo: un trigger reacciona a **una** operacion sobre **una** fila; no tiene ninguna manera de deshacer lo que otras sentencias hicieron antes en la misma transaccion. Eso solo lo puede hacer el gestor de transacciones. |

### Como calificar

- **10 pts con la opcion correcta marcada; cualquier otra respuesta, 0.** Es una pregunta de opcion unica y la rubrica no admite puntaje parcial. La clave se lee del banco de la plataforma y es la que combina las dos mitades: el `CALL` de nivel superior es su propia transaccion **y** el bloque `BEGIN ... EXCEPTION` crea un savepoint implicito.
- **La opcion del `ROLLBACK` explicito es la que mas se marca,** y se corrige con un dato en vez de una explicacion: el `sp_facturar` de referencia esta **en la base** de la pregunta 2 y no contiene ningun `ROLLBACK`. Vale la pena proyectarlo, porque el mismo malentendido es el que hace que alguien escriba `COMMIT` dentro del procedimiento de la pregunta 1.
- **La opcion de «PL/pgSQL acumula los `UPDATE` en memoria» merece medio minuto,** porque explica correctamente el resultado con el mecanismo equivocado y por eso sobrevive a un examen rapido. La refutacion es del propio taller: dentro de la misma transaccion el procedimiento vuelve a leer el stock ya descontado, que es justamente lo que hace posible el patron del `WHERE`.
- Al devolver la pregunta conviene pedir las **dos** mitades de la opcion correcta, no solo la primera. Muchos estudiantes saben que el `CALL` es una transaccion y no saben que el `BEGIN ... EXCEPTION` crea un savepoint implicito —y es la segunda mitad la que explica por que el `DO` de la pregunta 2 pudo seguir corriendo despues del error—.

### Errores frecuentes y que hacer

- **Marcar la del `ROLLBACK` explicito.** Es transferencia directa de Oracle. En PostgreSQL el procedimiento no gestiona su transaccion: la hereda de la sentencia que lo llamo. Quien marque esta opcion conviene revisarle la pregunta 1, porque suele haber un `COMMIT` de mas.
- **Marcar la del respaldo automatico de cada tabla.** Suele venir de la palabra «`ROLLBACK`» entendida como «restaurar». No se restaura nada: se escribieron versiones nuevas de las filas y esas versiones nunca llegaron a ser visibles. La diferencia importa cuando en la Clase 10 haya que entender por que dos sesiones ven cosas distintas de la misma fila.
- **Marcar la del trigger.** En esta base no hay triggers —los de stock son de la Clase 4—, asi que la opcion se cae con un `SELECT` a `information_schema.triggers`. El error de fondo es de escala: un trigger actua sobre una fila y una operacion; deshacer una transaccion es de otro nivel del motor.
- **Contestar bien por eliminacion y no poder explicarlo.** Se detecta en la pregunta 2, donde la conclusion en comentarios queda vaga —«hubo `ROLLBACK`»— sin decir **quien** lo hizo ni **por que**. Las dos preguntas se califican juntas de forma natural: la 4 dice si conoce el mecanismo y la 2 si lo sabe usar.

---

## Pregunta 5 · Checklist de tuning y transacciones del PI · 15 pts

### Respuesta esperada

| Transaccion de negocio | Tablas que toca | Paso que puede fallar | Que debe pasar si falla |
|---|---|---|---|
| **Facturar una consulta** (`sp_facturar`) | `factura` (cabecera), `detalle_factura` (una fila por linea), `insumo` (descuento de stock) | El descuento de stock de **cualquiera** de las lineas: el `UPDATE ... WHERE stock >= cantidad` afecta 0 filas. Tambien puede fallar un `id_insumo` inexistente | **Todo o nada.** Se deshace la cabecera, las lineas ya escritas y los descuentos ya aplicados. Verificado en la pregunta 2: el insumo 3 volvio de 38 a **40**. El mostrador recibe el mensaje «stock insuficiente del insumo N» y decide: sustituir, apartar o reponer |
| **Registrar una consulta y cerrar la cita** (`sp_registrar_consulta`, Clase 3) | `consulta` (alta), `cita` (paso a `ATENDIDA`) | La cita no existe, esta `CANCELADA`, o ya tiene consulta —lo garantiza el `UNIQUE (id_cita)`—. Tambien un precio nulo o no positivo | **Todo o nada.** Si el alta de la consulta falla, la cita **no** puede quedar en `ATENDIDA`: seria una cita atendida sin diagnostico ni precio, invisible para la facturacion. El caso inverso es peor: una consulta cuya cita sigue `PROGRAMADA` se volveria a agendar |
| **Cancelar una cita y liberar la franja** | `cita` (paso a `CANCELADA`), `audit_cita` (traza del cambio de estado, Clase 4) | Que la cita ya este `ATENDIDA` —una cita atendida no se cancela— o que el registro en la auditoria falle | **Todo o nada, y en este orden de importancia:** si la auditoria no se escribe, la cancelacion **tampoco** se confirma. Una cancelacion sin traza es exactamente el caso que la auditoria existe para cubrir. Efecto secundario deseado: la franja queda libre, porque `sp_agendar_cita` no cuenta las `CANCELADA` |

**2. Checklist de tuning.** Siete items, cada uno con estado y con evidencia **concreta** —nombre de indice, archivo, consulta—, no con una casilla marcada:

| # | Item | Estado | Evidencia concreta |
|---|---|---|---|
| 1 | Indices sobre columnas de filtro y join de las consultas frecuentes | **listo** | `idx_cita_programada_fecha` (parcial), `idx_cita_fecha_hora` y `idx_mascota_dueno`, en `/db/04_indices.sql`. Planes en `/informe/07-planes.txt`: `Index Scan using idx_cita_programada_fecha`, 91 filas, `Rows Removed by Filter` desaparecido |
| 2 | Consultas sin `SELECT *` en los reportes | **listo** | `06_opt_despues.sql`: la agenda del dia proyecta 6 columnas en vez de ~20. Revisado a mano el resto de `/db` y de la aplicacion |
| 3 | Predicados sargables | **listo** | Se elimino `to_char(fecha_hora,'YYYY-MM-DD') = ...` y quedo el rango `>= '2026-03-10' AND < '2026-03-11'`. Sin el cambio, `idx_cita_programada_fecha` no se usaria: sargabilidad primero, indice despues |
| 4 | Transacciones cortas, sin esperar al usuario con la transaccion abierta | **parcial** | `sp_facturar` es una sola sentencia `CALL`: no hay interaccion humana dentro. Pero la pantalla de facturacion **arma el carrito** en memoria y llama al procedimiento **una sola vez** al confirmar; falta revisar que ningun formulario deje una transaccion abierta mientras el usuario piensa |
| 5 | Validaciones criticas en la base, no solo en la aplicacion | **listo** | `CHECK (stock >= 0)` y `CHECK (cantidad > 0)`; `UNIQUE (id_cita)` en `consulta`; `CHECK (estado IN (...))`; el trigger de stock no negativo y las validaciones dentro de `sp_facturar` y `fn_descontar_stock`. La aplicacion valida **tambien**, para dar mejores mensajes, no en lugar de la base |
| 6 | `ANALYZE` / estadisticas al dia despues de cargas masivas | **parcial** | Se corrio `ANALYZE cita; ANALYZE mascota;` tras crear los indices de la Clase 7 y se comprobo su efecto —la estimacion paso de `rows=1` a `rows=90` contra 91 reales—. Falta dejarlo **automatizado**: hoy depende de que alguien se acuerde |
| 7 | Plan de respaldo con restauracion probada | **pendiente** | El plan esta escrito (Clase 4): `pg_dump -Fc` diario 20:30, `pg_dumpall --globals-only` 20:25, `pg_basebackup` semanal, WAL continuo, **RPO 15 min / RTO 4 h**. El ensayo de restauracion **no se ha hecho ni una vez**, asi que el RTO de 4 horas es una estimacion sin respaldo. Es el riesgo mas grande del proyecto y se declara como tal |

Cuatro «listo», dos «parcial» y un «pendiente». La lista sirve precisamente porque no esta toda en verde: los tres items que no lo estan son los tres que hay que hacer, y estan nombrados.

**3. Decision documentada: por que `UPDATE ... WHERE stock >= cantidad` y no leer primero.** El patron inseguro deja una **ventana** entre la lectura y la escritura, y en esa ventana el dato leido puede dejar de ser cierto. Con dos recepcionistas facturando la ultima vacuna a la vez:

```
Sesion A: SELECT stock -> 1     "hay una, sigo"
Sesion B: SELECT stock -> 1     "hay una, sigo"
Sesion A: UPDATE stock = 1 - 1 = 0     (correcto)
Sesion B: UPDATE stock = 0 - 1 = -1    (ya no habia)
```

Las dos leyeron un dato que era cierto al leerlo y falso al actuar. Con la condicion en el `WHERE`, comprobar y descontar son **la misma sentencia**: la sesion B espera a que A termine de modificar la fila y —en `READ COMMITTED`, el nivel por omision— **vuelve a evaluar su propio `WHERE` contra la version nueva**, ve `stock = 0`, afecta 0 filas y `GET DIAGNOSTICS ROW_COUNT` lo delata. Nadie queda en negativo y nadie tuvo que coordinarse con nadie.

> **La frase para la sustentacion:** «El stock se descuenta con la comprobacion dentro del `WHERE` porque asi verificar y escribir son una sola operacion indivisible; leer primero y decidir despues deja una ventana en la que el dato leido ya no es cierto, y con dos recepcionistas facturando el mismo insumo esa ventana es un stock negativo.»

**4. Gap honesto: la concurrencia no se pudo comprobar.** PostgreSQL en el navegador corre con **una sola sesion**, asi que todo lo del punto 3 es un **razonamiento, no una medicion**. Concretamente, tres cosas quedaron sin verificar:

- **El escenario de las dos recepcionistas.** No se pudo abrir una segunda sesion, dejar una transaccion a medias y ver a la otra esperar. La carrera que el patron previene **nunca ocurrio** en las pruebas, porque no podia ocurrir: todos los `true` y `false` de la pregunta 3 salieron de una sola sesion, donde el patron inseguro habria dado exactamente los mismos resultados. **Eso es lo incomodo de admitir: el taller no distingue el codigo correcto del incorrecto.**
- **Los bloqueos y su duracion.** No se midio cuanto espera la segunda sesion ni que pasa si la primera no confirma nunca. Tampoco se pudo provocar un **interbloqueo** —dos facturas que descuentan los mismos dos insumos en orden inverso—, que es el problema real de esta operacion en produccion.
- **La diferencia entre niveles de aislamiento.** Todo corrio en `READ COMMITTED` sin poder compararlo con `REPEATABLE READ` ni con `SERIALIZABLE`, que es donde el mismo patron cambia de comportamiento.

**Como se aborda en la Clase 10, en concreto:** la Clase 10 trabaja con dos sesiones simuladas y transacciones explicitas, y ahi se van a hacer tres cosas. **(a)** Reproducir la carrera con el patron **inseguro**, para verlo fallar de verdad y no solo en un comentario. **(b)** Repetir el mismo escenario con el patron del `WHERE` y comprobar que la segunda sesion espera, vuelve a evaluar y recibe `false`. **(c)** Provocar un interbloqueo a proposito y ver como PostgreSQL lo detecta y mata una de las dos transacciones, para decidir una **regla de orden de descuento** —por `id_insumo` ascendente— que lo prevenga. Con eso, el item 4 del checklist puede pasar de «parcial» a «listo» con evidencia, y no antes.

**Archivos del PI:** esta seccion en `/informe/08-transacciones-tuning.md`, `sp_facturar` y `fn_descontar_stock` en `/db/02_procedimientos.sql`, y las salidas de la prueba de atomicidad en `/informe/08-atomicidad.txt` —la foto inicial, la final y el `40` del insumo 3—.

### Como calificar

- **5 pts — el inventario de transacciones, al menos 3.** Cada una vale 1,7 pts y se reparte en tres tercios: **tablas** que toca, **paso que puede fallar** y **que debe pasar si falla**. El tercero es el que se queda corto: «se hace `ROLLBACK`» vale medio tercio, porque no dice que ve el usuario ni que estado queda. Se exige nombrar el paso concreto —«el `UPDATE` de stock afecta 0 filas»—, no «puede fallar algo».
- **5 pts — el checklist con los 7 items, estado y evidencia concreta.** Aproximadamente 0,7 pts por item. **La evidencia es lo que se califica:** un nombre de indice, un archivo, una consulta, un numero. La rubrica dice explicitamente «no solo casillas marcadas», asi que un checklist con siete «listo» y ninguna evidencia vale 1 de 5. **Un checklist con «parcial» y «pendiente» bien argumentados vale mas que uno todo en verde**, y conviene decirlo en voz alta antes del taller: el item 7 —restauracion probada— todavia **no** puede estar listo en ningun proyecto del curso.
- **2 pts — la decision del `UPDATE` condicional, con la frase defendible.** 1 pt el argumento —la ventana entre leer y escribir— y 1 pt que la frase de cierre sea de verdad una frase sostenible en sustentacion, no un parrafo. Se premia con el punto completo quien narre la carrera con las dos sesiones intercaladas.
- **3 pts — el gap de concurrencia reconocido y con plan.** 1,5 pts admitir que con **una sola sesion** el escenario de dos recepcionistas **no se pudo comprobar**, y 1,5 pts un plan concreto para la Clase 10. «Lo vere en la Clase 10» vale 0 de esos 1,5: se pide **que** se va a hacer. Un informe que presente la concurrencia como resuelta pierde los 3 pts completos, aunque todo el SQL de las preguntas 1 a 3 este perfecto.
- **Se reconoce como sobresaliente, sin puntos extra pero se anota:** admitir que en una sola sesion el patron **inseguro** habria dado exactamente los mismos resultados que el seguro, y que por lo tanto el taller **no distingue** el codigo correcto del incorrecto. Es la observacion mas madura que puede hacer un estudiante en esta clase y es la mejor entrada posible a la Clase 10.
- **Extension:** una pagina. Se califica que las cuatro partes esten con contenido verificable, no la longitud. El item que mas se olvida del checklist es el 7, y es el unico del que se espera un «pendiente»: si alguien lo marca «listo», hay que preguntarle cuando corrio el ensayo de restauracion.

### Errores frecuentes y que hacer

- **El checklist como siete casillas marcadas.** Es el error dominante de esta pregunta y la rubrica lo penaliza de frente. Sin evidencia, un «listo» no se puede verificar ni auditar y no significa nada. El minimo aceptable por item es un nombre propio: un indice, un archivo, una consulta, un numero.
- **Marcar el item 7 como «listo» sin haber restaurado nunca.** Tener el plan de respaldo escrito no es tenerlo probado, y esa es exactamente la leccion de la Clase 4: un respaldo que no se ha restaurado es una hipotesis. Es el item en el que un «pendiente» honesto vale mas que un «listo» falso.
- **Presentar la concurrencia como resuelta.** Aparece como «el patron del `WHERE` garantiza que no haya problemas de concurrencia, verificado en la pregunta 3». No se verifico nada: hubo **una sola sesion**. El patron es correcto y el razonamiento es correcto, pero la evidencia no existe todavia. Confundir las dos cosas es lo que la pregunta esta midiendo.
- **Un inventario de menos de tres transacciones,** o tres que en realidad son la misma con distinto nombre. Las tres del taller son bien distintas y estan todas construidas: facturar (Clase 8), registrar consulta y cerrar cita (Clase 3), cancelar cita con su auditoria (Clase 4). Si alguien no encuentra tres, el problema es que no esta releyendo su propio proyecto.
- **Confundir «transaccion corta» con «consulta rapida».** El item 4 no es sobre milisegundos: es sobre **no dejar una transaccion abierta esperando a un humano**. Una transaccion de 50 ms que espera a que alguien confirme en pantalla puede retener un bloqueo diez minutos. La distincion es la que hace util el item.
- **Un plan para la Clase 10 que es solo un titulo.** «Probare la concurrencia» no es un plan. Lo que se pide es el escenario: dos sesiones, que hace cada una, en que orden y que se espera observar. Quien ya lo tenga escrito llega a la Clase 10 con el ejercicio medio hecho.

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**¿Por que no puedo poner `COMMIT` dentro del procedimiento?**

Porque destruye justo lo que la clase quiere demostrar. La sentencia `CALL` de nivel superior **ya es** su propia transaccion: no hace falta abrirla ni cerrarla. Si pones un `COMMIT` despues de insertar la cabecera de la factura, esa cabecera queda confirmada, y cuando la segunda linea falle por stock la factura huerfana **se queda** —con su total en cero y sin un solo detalle—. La pregunta 2 va a mostrarte `factura` con 4 filas en vez de 3 y vas a concluir que PostgreSQL no es atomico, cuando lo que pasa es que le quitaste la atomicidad tu. Si el procedimiento lanza una excepcion, **todo** lo que hizo se deshace solo, sin escribir una linea.

**¿Que es `GET DIAGNOSTICS` y por que no puedo usar `SQL%ROWCOUNT`?**

`SQL%ROWCOUNT` es de Oracle y en PL/pgSQL no existe. El equivalente es `GET DIAGNOSTICS v_filas = ROW_COUNT;` inmediatamente despues de la sentencia que quieres medir —si pones otra sentencia en medio, mides esa otra—. Y es **imprescindible** en este patron por una razon que no es obvia: un `UPDATE` que no encuentra ninguna fila que cumpla el `WHERE` **no falla**; afecta 0 filas y sigue adelante tranquilamente. Sin preguntar cuantas filas toco, tu factura saldria con el detalle escrito y el stock sin descontar.

**¿Por que la condicion del stock va en el `WHERE` y no en un `IF` antes?**

Porque el `IF` deja una **ventana**. Con dos recepcionistas facturando la ultima vacuna: A lee stock 1 y decide seguir, B lee stock 1 y decide seguir, A descuenta a 0, B descuenta a **-1**. Las dos leyeron un dato que era cierto cuando lo leyeron y falso cuando actuaron. Con la condicion en el `WHERE`, comprobar y descontar son **una sola** sentencia: B espera a que A termine con la fila, vuelve a evaluar su propio `WHERE` contra la version nueva, ve `stock = 0`, afecta 0 filas y `ROW_COUNT` te lo dice. En ExamLab las dos versiones funcionan igual porque hay una sola sesion —esa es exactamente la trampa, y es el hueco que tienes que declarar en la pregunta 5—.

**¿Por que la factura buena salio con el id 5 y no con el 4?**

Porque el intento fallido **consumio** el 4 de la secuencia, y las secuencias no vuelven atras con el `ROLLBACK`. Es a proposito: si volvieran, dos sesiones que pidieran un id al mismo tiempo podrian recibir el mismo numero, y entonces el `SERIAL` no serviria para nada. La consecuencia practica es que en cualquier base real **hay huecos** en los ids, y no significan datos perdidos: significan intentos que fallaron. Si alguien te pide «numeracion consecutiva sin huecos» para las facturas —y en Colombia la facturacion electronica lo pide—, eso **no** se resuelve con un `SERIAL`: hace falta una tabla de consecutivos con su propio bloqueo, y cuesta concurrencia.

**En la pregunta 3, ¿por que `FALSE` y no una excepcion, si en `sp_facturar` si lanzamos excepcion?**

Porque son dos decisiones de diseno distintas y las dos son correctas **en su sitio**. En `sp_facturar` la excepcion es necesaria: si una linea no se puede servir, la factura completa no debe existir, y la excepcion es lo que consigue que se deshaga todo. En `fn_descontar_stock` el «no hay stock» es una **respuesta**: quien llama recibe `false` y decide —ofrecer un sustituto, avisar al mostrador, apartar el pedido— sin perder su transaccion. La regla general: **excepcion cuando la operacion no puede continuar; valor de retorno cuando quien llama tiene algo que decidir.**

**¿Una funcion puede hacer `UPDATE` y llamarse desde un `SELECT`?**

En PostgreSQL si, y es lo que pide la pregunta 3. En Oracle seria un error —`ORA-14551`—, asi que si venias de alli el reflejo es dudarlo. Dos cuidados. Uno: **no** la marques `IMMUTABLE` ni `STABLE`; el valor por omision es `VOLATILE` y es el correcto, porque una funcion que escribe tiene que ejecutarse de verdad en cada llamada. Dos: el orden en que el motor evalua varias funciones en la misma lista de columnas **no esta garantizado**, asi que no construyas una prueba que dependa de el. En este caso da igual —revisa por que en la salida esperada—, pero es suerte, no diseno.

**¿Para que sirve el `CHECK (stock >= 0)` si el patron del `WHERE` ya lo evita?**

Para lo mismo que el cinturon cuando ya frenaste bien. Son dos cosas distintas: el `CHECK` **garantiza** —no existe forma de dejar un stock negativo en esa tabla, ni con un `UPDATE` a mano, ni con un procedimiento nuevo mal escrito, ni con una carga masiva— y el patron del `WHERE` **explica y responde**, porque en vez de abortar la sentencia devuelve `false` y permite reaccionar con elegancia. Es la misma pareja de la Clase 4: la restriccion es la garantia, el codigo es la explicacion. Si en tu prueba salta el `CHECK`, no celebres que te salvo: significa que el patron esta mal escrito.

**¿Por que el `DO $$ ... EXCEPTION ... END $$` permite que el script siga despues del error?**

Porque un bloque `BEGIN ... EXCEPTION` en PL/pgSQL crea un **savepoint implicito**. Cuando la excepcion sube desde el `CALL`, el motor deshace lo hecho **dentro** de ese bloque, entra al manejador y continua desde ahi: por eso ves el `NOTICE 'Fallo esperado: ...'` y el bloque termina en `DO` en vez de `ERROR`. Es la segunda mitad de la respuesta correcta de la pregunta 4, y es la mitad que casi nadie menciona. Sin ella no tendrias foto final, y sin foto final no habria prueba de atomicidad.

---

## Cierre de la clase

- Al terminar, cada estudiante debe tener: `sp_facturar` con el `UPDATE` condicional y el `GET DIAGNOSTICS`, la factura **4** por **27.400** y los stocks en 11, 58 y 5; la prueba de atomicidad con las dos fotos identicas, el **40** del insumo 3 recuperado y la factura viable por **112.000**; `fn_descontar_stock` devolviendo `true/false/true` con el insumo 5 en 5, el 2 en 0 y ningun negativo; la opcion correcta de la pregunta 4; y la seccion de transacciones y tuning con las tres transacciones inventariadas, los siete items con evidencia y el hueco de concurrencia declarado, en `/informe/08-transacciones-tuning.md`.
- Antes de cerrar hay que verificar **tres numeros y una ausencia**, y los cuatro se leen sin ejecutar nada. Que el total de la factura nueva sea **27.400** y no 24.100 —24.100 significa que se acumulo el precio sin multiplicar por la cantidad—. Que el stock del insumo 3 haya **vuelto a 40** en la pregunta 2, que es el unico dato que prueba que hubo trabajo hecho y deshecho. Que la funcion de la pregunta 3 devuelva **`f`** en el caso sin stock y que no quede ni un negativo. Y la ausencia: que **no** aparezca la palabra `COMMIT` dentro de ningun procedimiento —si aparece, hay que revisar la pregunta 2 de esa misma entrega, porque la conclusion va a estar invertida—.
- Dejar dicho en voz alta el limite de la clase, porque es el mejor puente del semestre: **todo lo que se argumento hoy sobre dos recepcionistas facturando a la vez no se pudo comprobar**, porque ExamLab corre con una sola sesion. Y hay una consecuencia incomoda que vale la pena decir sin adornos: en una sola sesion, el patron **inseguro** —leer y despues decidir— habria dado exactamente los mismos `true` y `false` que el seguro. El taller no distingue el codigo correcto del incorrecto; lo distingue el razonamiento. La Clase 10 lo convierte en medicion: dos sesiones simuladas con transacciones explicitas, la carrera reproducida primero con el patron malo para verla fallar, luego con el bueno para ver a la segunda sesion esperar y recibir `false`, y un interbloqueo provocado a proposito para decidir la regla de orden de descuento. El item 4 del checklist pasa a «listo» ese dia, y no antes.

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. El motor de la plataforma es PostgreSQL (PGlite en el navegador), no Oracle.
