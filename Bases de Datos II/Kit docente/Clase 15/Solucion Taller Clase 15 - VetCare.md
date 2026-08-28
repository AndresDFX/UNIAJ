# Solucion del taller · Clase 15 · Entrega final y cierre de VetCare DB

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** El **script maestro de referencia** completo —siete bloques que corren de arriba abajo sobre una base limpia sin un solo error, con los `CHECK` nombrados, los totales de factura **calculados** en vez de escritos, las tres pruebas de aceptacion (dos negativas y una positiva, que no se escriben igual) y el inventario que cierra en `5 | 8 | 3 | 8 | 2 | 4 | 2 | 4 | 1`—; los **cuatro KPIs** resueltos con sus numeros exactos, incluida la trampa de que la semilla del banco **no** ejerce las tres condiciones de borde que la rubrica exige y como forzarlas con tres `INSERT`; la clave razonada del checklist del ZIP; el acta de entrega con inventario, trazabilidad de las once clases y un guion de **7 minutos**; y la autoevaluacion modelo, con las tres diferencias PL/SQL → PL/pgSQL y la lista honesta de lo que este entorno no permitio verificar.

> **Sesion 13, lunes 2026-11-16: sustentacion.** Este taller es la **evaluacion final del PI, 20 % del Corte 3**, y tiene que estar entregado **antes** del turno de cada estudiante: el bloque de dos horas se consume en las presentaciones, asi que no hay tiempo de aula para escribir el script. Conviene publicarlo con el taller de la Clase 13 —el 2026-11-02— para que el 2026-11-09, dia del Parcial 3, ya este cerrado. **El motor es PostgreSQL, no Oracle:** nada de `NUMBER`, `VARCHAR2`, `RAISE_APPLICATION_ERROR`, `DUAL`, `SQL%ROWCOUNT` ni `/` de terminacion.

**Cuatro cosas que hay que decir antes de que empiecen, porque cuestan puntos por sorpresa.** (1) La pregunta 1 se califica **ejecutando** el script sobre una base limpia: un solo error de sintaxis a la mitad deja los bloques siguientes sin correr, y por eso vale la pena exigir que lo prueben de cero al menos una vez —la base de ExamLab se vuelve a sembrar en cada intento, asi que se puede—. (2) `entrega_final` **ya trae una fila de ejemplo** del docente: la del estudiante es la `id_entrega = 2`, y quien la borre para «dejarlo limpio» esta modificando la semilla, no entregando. (3) Para tener dos facturas hacen falta al menos dos `consulta`, y `consulta.id_cita` es **UNIQUE**: dos citas distintas y atendidas. Es la cadena de dependencias que rompe mas semillas. (4) Las tres pruebas del bloque 5 **no se escriben igual**: las dos primeras esperan un error y la tercera espera un efecto; envolver la tercera en un `EXCEPTION WHEN OTHERS` no prueba nada.

**Y un defecto de la semilla de la pregunta 2 que conviene anunciar,** porque si no, la mitad del grupo cree que se equivoco. La rubrica exige que K1 conserve los veterinarios **sin citas** y que K3 incluya los insumos **nunca vendidos**, pero en los datos entregados **los cuatro veterinarios tienen citas y los seis insumos se han vendido**: la consulta correcta y la incorrecta devuelven exactamente lo mismo. Igual pasa con el «ordena cronologicamente» de K2, donde las tres facturas caen en el mismo mes y solo hay una fila. Lo razonable es pedir que el estudiante **cree** el caso de borde con tres `INSERT` —un veterinario nuevo, un insumo nuevo y una factura en octubre— y muestre las dos corridas; la solucion lo hace asi y son 6 de los 20 puntos. Ademas, hay que saberlo al calificar: **las tres facturas de la semilla estan descuadradas** —`factura.total` no coincide con `consulta.precio` mas la suma del detalle, ni con la suma del detalle sola—, exactamente la misma inconsistencia que la prueba 5 de la Clase 11. K2 reporta `factura.total`, que es lo que pide el enunciado, y el estudiante que lo note merece reconocimiento, no correccion. Las preguntas 4 y 5 son sobre el paquete y el proceso de cada estudiante: lo que sigue es un **modelo de referencia y no una clave**.

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 15 - Presentacion del proyecto y cierre/Taller PI - Clase 15 - VetCare.docx`
- Configuracion en la plataforma: `Kit docente/Clase 15/Taller en ExamLab - Clase 15 (configuracion).md`
- Caso de estudio: `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
- Hito del PI: Sustentacion en vivo y entrega final del PI (20% Corte 3)
- Entregable: ZIP/PDF final subido antes del turno + sustentacion en vivo 5-8 min + Q&A
- **Estas preguntas: 100 puntos** en 5 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 1 | Script maestro de entrega: VetCare DB de cero, en una sola corrida | `bd_sql` | 35 |
| 2 | Los KPIs que se proyectan en la sustentacion | `bd_sql` | 20 |
| 3 | Checklist de empaquetado del ZIP final | `cerrada_multi` | 10 |
| 4 | Acta de entrega y reparto de la sustentacion | `abierta` | 20 |
| 5 | Autoevaluacion de cierre: que harias distinto | `abierta` | 15 |

---

## Pregunta 1 · Script maestro de entrega: VetCare DB de cero, en una sola corrida · 35 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- ======================================================================
-- VETCARE DB - SCRIPT MAESTRO DE ENTREGA
-- Bases de Datos II - FI303215 - Periodo 2026-2
-- Motor: PostgreSQL. Se ejecuta UNA vez, de arriba abajo, sobre base limpia.
--
-- Regla que gobierna todo el archivo: si hay que ejecutarlo dos veces o en
-- otro orden, no es un script maestro. Y si un numero se puede calcular,
-- no se escribe a mano -- esa es la leccion de las Clases 11 y 13.
-- ======================================================================

-- ======================================================================
-- BLOQUE 0 - REGISTRO DE LA ENTREGA
--
-- entrega_final YA trae una fila de ejemplo del docente. La del estudiante
-- es la id_entrega = 2. No se borra la del docente: modificar la semilla
-- no es entregar.
-- ======================================================================
INSERT INTO entrega_final (estudiante, codigo, proyecto, enlace_zip, integrantes)
VALUES ('Nombre Completo Del Estudiante', '1234567',
        'VetCare DB - Sistema de gestion para clinica veterinaria',
        'https://drive.google.com/mi-entrega-vetcare.zip',
        NULL);   -- NULL porque trabajo solo; si hubo equipo autorizado, va la lista

SELECT id_entrega, estudiante, codigo, proyecto, fecha_entrega
  FROM entrega_final ORDER BY id_entrega;   -- 2 filas: la del docente y la mia

-- ======================================================================
-- BLOQUE 1 - DDL COMPLETO (8 tablas + auditoria)
--
-- Las restricciones CHECK van con NOMBRE propio, y no es cosmetica: el
-- nombre aparece en el mensaje de error, y es lo que permite que la
-- aplicacion traduzca "ck_insumo_stock" a "stock insuficiente" en vez de
-- mostrarle al usuario el texto crudo del motor (Clase 12). Con nombres
-- automaticos el mensaje depende de como los genere el servidor.
-- ======================================================================
CREATE TABLE dueno (
  id_dueno SERIAL PRIMARY KEY,
  nombre   TEXT NOT NULL,
  telefono TEXT,
  email    TEXT,
  ciudad   TEXT DEFAULT 'Cali'
);

CREATE TABLE veterinario (
  id_veterinario SERIAL PRIMARY KEY,
  nombre         TEXT NOT NULL,
  especialidad   TEXT,
  activo         CHAR(1) NOT NULL DEFAULT 'S'
                 CONSTRAINT ck_veterinario_activo CHECK (activo IN ('S','N'))
);

CREATE TABLE mascota (
  id_mascota SERIAL PRIMARY KEY,
  id_dueno   INT  NOT NULL REFERENCES dueno(id_dueno),
  nombre     TEXT NOT NULL,
  especie    TEXT NOT NULL,
  fecha_nac  DATE,
  activa     CHAR(1) NOT NULL DEFAULT 'S'
             CONSTRAINT ck_mascota_activa CHECK (activa IN ('S','N'))
);

CREATE TABLE cita (
  id_cita        SERIAL PRIMARY KEY,
  id_mascota     INT NOT NULL REFERENCES mascota(id_mascota),
  id_veterinario INT NOT NULL REFERENCES veterinario(id_veterinario),
  fecha_hora     TIMESTAMP NOT NULL,
  estado         TEXT NOT NULL DEFAULT 'PROGRAMADA'
                 CONSTRAINT ck_cita_estado
                 CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))
);

-- id_cita es UNIQUE: una cita genera como maximo una consulta. Es una regla
-- de negocio, no un detalle tecnico, y es la que obliga a que dos facturas
-- necesiten dos citas atendidas distintas.
CREATE TABLE consulta (
  id_consulta SERIAL PRIMARY KEY,
  id_cita     INT NOT NULL UNIQUE REFERENCES cita(id_cita),
  diagnostico TEXT,
  precio      NUMERIC(12,2) NOT NULL
              CONSTRAINT ck_consulta_precio CHECK (precio >= 0)
);

CREATE TABLE insumo (
  id_insumo   SERIAL PRIMARY KEY,
  nombre      TEXT NOT NULL,
  stock       INT NOT NULL CONSTRAINT ck_insumo_stock CHECK (stock >= 0),
  precio_unit NUMERIC(12,2) NOT NULL
              CONSTRAINT ck_insumo_precio CHECK (precio_unit >= 0)
);

CREATE TABLE factura (
  id_factura  SERIAL PRIMARY KEY,
  id_consulta INT NOT NULL REFERENCES consulta(id_consulta),
  fecha       TIMESTAMP NOT NULL DEFAULT now(),
  total       NUMERIC(12,2) NOT NULL DEFAULT 0
              CONSTRAINT ck_factura_total CHECK (total >= 0)
);

-- ON DELETE CASCADE solo en id_factura: borrar una factura se lleva sus
-- lineas, porque una linea sin factura no significa nada. Pero NO en
-- id_insumo: borrar un insumo no puede borrar el historial de ventas.
CREATE TABLE detalle_factura (
  id_detalle  SERIAL PRIMARY KEY,
  id_factura  INT NOT NULL REFERENCES factura(id_factura) ON DELETE CASCADE,
  id_insumo   INT NOT NULL REFERENCES insumo(id_insumo),
  cantidad    INT NOT NULL CONSTRAINT ck_detalle_cantidad CHECK (cantidad > 0),
  precio_unit NUMERIC(12,2) NOT NULL
              CONSTRAINT ck_detalle_precio CHECK (precio_unit >= 0)
);

-- Auditoria. A PROPOSITO sin FK a cita: la bitacora tiene que sobrevivir a
-- lo que audita. Si manana se borra una cita, una FK impediria conservar su
-- traza justo cuando es lo unico que queda (Clases 4 y 13).
CREATE TABLE audit_cita (
  id_audit       SERIAL PRIMARY KEY,
  id_cita        INT  NOT NULL,
  accion         TEXT NOT NULL,
  valor_anterior TEXT,
  valor_nuevo    TEXT,
  usuario_bd     TEXT      NOT NULL DEFAULT current_user,
  fecha_evento   TIMESTAMP NOT NULL DEFAULT now()
);

-- ======================================================================
-- BLOQUE 2 - DATOS SEMILLA
-- 5 duenos, 3 veterinarios, 8 mascotas (2 inactivas), 8 citas en los tres
-- estados, 2 consultas, 4 insumos (1 con stock < 5), 2 facturas, 4 detalles.
-- ======================================================================
INSERT INTO dueno (nombre, telefono, email) VALUES
  ('Ana Gomez',     '3001112233', 'ana.gomez@mail.com'),
  ('Carlos Ruiz',   '3014445566', 'carlos.ruiz@mail.com'),
  ('Marcela Diaz',  '3027778899', 'marcela.diaz@mail.com'),
  ('Jorge Pineda',  '3105551212', 'jorge.pineda@mail.com'),
  ('Luisa Cardona', '3123334455', 'luisa.cardona@mail.com');

INSERT INTO veterinario (nombre, especialidad) VALUES
  ('Laura Restrepo', 'General'),
  ('Diego Moreno',   'Cirugia'),
  ('Paula Salazar',  'Dermatologia');

-- Rocky (3) y Kiara (8) quedan INACTIVAS: son las que usa la prueba 1.
INSERT INTO mascota (id_dueno, nombre, especie, fecha_nac, activa) VALUES
  (1, 'Firulais', 'Canino', DATE '2019-04-12', 'S'),
  (1, 'Luna',     'Felino', DATE '2021-08-30', 'S'),
  (2, 'Rocky',    'Canino', DATE '2015-01-20', 'N'),
  (3, 'Mishi',    'Felino', DATE '2022-11-05', 'S'),
  (3, 'Bobby',    'Canino', DATE '2018-06-17', 'S'),
  (4, 'Nube',     'Felino', DATE '2023-02-09', 'S'),
  (5, 'Toby',     'Canino', DATE '2020-09-25', 'S'),
  (5, 'Kiara',    'Canino', DATE '2013-03-03', 'N');

-- 8 citas: 4 PROGRAMADA, 3 ATENDIDA, 1 CANCELADA -> los tres estados.
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado) VALUES
  (1, 1, TIMESTAMP '2026-09-01 08:00:00', 'PROGRAMADA'),
  (2, 1, TIMESTAMP '2026-09-01 09:00:00', 'ATENDIDA'),
  (4, 2, TIMESTAMP '2026-09-01 10:00:00', 'PROGRAMADA'),
  (5, 3, TIMESTAMP '2026-09-02 08:30:00', 'CANCELADA'),
  (6, 2, TIMESTAMP '2026-09-02 11:00:00', 'ATENDIDA'),
  (7, 3, TIMESTAMP '2026-09-03 07:45:00', 'PROGRAMADA'),
  (1, 1, TIMESTAMP '2026-09-05 15:00:00', 'ATENDIDA'),
  (2, 2, TIMESTAMP '2026-09-08 16:00:00', 'PROGRAMADA');

-- Dos consultas sobre dos citas ATENDIDAS distintas (id_cita es UNIQUE).
INSERT INTO consulta (id_cita, diagnostico, precio) VALUES
  (2, 'Vacunacion triple felina', 40000),
  (5, 'Control de peso',          38000);

-- El insumo 2 queda con stock 3 (< 5): es el que usa la prueba 2.
INSERT INTO insumo (nombre, stock, precio_unit) VALUES
  ('Vacuna antirrabica',   12, 22000),
  ('Vacuna triple felina',  3, 31000),
  ('Antiparasitario oral', 40,  9500),
  ('Gasa esteril',          8,  1200);

-- Las facturas nacen en 0 y su total se CALCULA abajo. Escribirlo a mano es
-- lo que dejo las facturas descuadradas del banco de la Clase 11: el numero
-- guardado y el numero derivado dejan de coincidir y nadie se entera.
INSERT INTO factura (id_consulta, fecha, total) VALUES
  (1, TIMESTAMP '2026-09-01 09:40:00', 0),
  (2, TIMESTAMP '2026-09-02 11:35:00', 0);

INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit) VALUES
  (1, 2, 1, 31000),
  (1, 4, 2,  1200),
  (2, 3, 1,  9500),
  (2, 1, 1, 22000);

UPDATE factura f
   SET total = (SELECT c.precio FROM consulta c WHERE c.id_consulta = f.id_consulta)
             + COALESCE((SELECT SUM(d.cantidad * d.precio_unit)
                           FROM detalle_factura d
                          WHERE d.id_factura = f.id_factura), 0);
-- factura 1 = 40000 + (31000 + 2400) = 73400
-- factura 2 = 38000 + ( 9500 + 22000) = 69500

-- ======================================================================
-- BLOQUE 3 - LOGICA DE NEGOCIO
-- ======================================================================

-- Funcion pura: mismo argumento, mismo resultado siempre. Por eso se puede
-- declarar IMMUTABLE y el planificador la evalua una sola vez.
CREATE FUNCTION fn_precio_consulta(p_especialidad TEXT)
RETURNS NUMERIC
LANGUAGE plpgsql
IMMUTABLE
AS $fn$
BEGIN
  RETURN CASE p_especialidad
           WHEN 'Cirugia'      THEN 120000
           WHEN 'Dermatologia' THEN  65000
           ELSE                       40000
         END;
END;
$fn$;

SELECT fn_precio_consulta('Cirugia')      AS cirugia,       -- 120000
       fn_precio_consulta('Dermatologia') AS dermatologia,  --  65000
       fn_precio_consulta('General')      AS general;       --  40000

-- Procedimiento de negocio con validacion. La regla del PI vive AQUI y no
-- en la aplicacion: asi la cumple cualquiera que se conecte, no solo quien
-- pase por la interfaz.
CREATE PROCEDURE sp_agendar_cita(p_id_mascota     INT,
                                 p_id_veterinario INT,
                                 p_fecha          TIMESTAMP)
LANGUAGE plpgsql
AS $proc$
DECLARE
  v_activa CHAR(1);
BEGIN
  SELECT m.activa INTO v_activa
    FROM mascota m WHERE m.id_mascota = p_id_mascota;

  -- IF NOT FOUND funciona porque el SELECT es de una columna a una
  -- variable. Despues de un SELECT COUNT(*) INTO nunca seria verdadero:
  -- COUNT siempre devuelve una fila, aunque valga 0 (Clase 3).
  IF NOT FOUND THEN
    RAISE EXCEPTION 'La mascota % no existe', p_id_mascota;
  END IF;

  IF v_activa <> 'S' THEN
    RAISE EXCEPTION 'La mascota % esta inactiva: no se puede agendar', p_id_mascota;
  END IF;

  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora)
  VALUES (p_id_mascota, p_id_veterinario, p_fecha);
END;
$proc$;

-- Trigger de auditoria: DOS objetos, la funcion y la asociacion.
CREATE FUNCTION fn_trg_audit_cita()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $fn$
BEGIN
  -- El IF hace falta aunque el trigger diga UPDATE OF estado: esa clausula
  -- se dispara cuando la columna se MENCIONA en el UPDATE, aunque el valor
  -- no cambie. Sin el IF, un "SET estado = estado" ensuciaria la bitacora.
  IF NEW.estado IS DISTINCT FROM OLD.estado THEN
    INSERT INTO audit_cita (id_cita, accion, valor_anterior, valor_nuevo)
    VALUES (OLD.id_cita, 'CAMBIO_ESTADO', OLD.estado, NEW.estado);
  END IF;
  RETURN NEW;
END;
$fn$;

-- AFTER, no BEFORE: se audita lo que YA ocurrio. Si la fila termina no
-- cambiando por otro motivo, no queremos un registro que diga que cambio.
CREATE TRIGGER trg_audit_cita
  AFTER UPDATE OF estado ON cita
  FOR EACH ROW
  EXECUTE FUNCTION fn_trg_audit_cita();

-- ======================================================================
-- BLOQUE 4 - INDICES
--
-- PostgreSQL crea indice para la PK y para UNIQUE, y NO lo crea para las
-- llaves foraneas. Los indices de abajo no son decorativos: son las
-- columnas por las que filtran los reportes de la pregunta 2.
-- ======================================================================

-- Reporte de agenda por veterinario y rango de fechas (Clase 6). El orden
-- de las columnas importa: igualdad antes que rango.
CREATE INDEX idx_cita_vet_fecha ON cita (id_veterinario, fecha_hora);

-- Historia clinica por mascota (KPI 4) y apoyo a la FK.
CREATE INDEX idx_cita_mascota ON cita (id_mascota);

-- Indice PARCIAL: la bandeja de pendientes solo consulta las PROGRAMADA,
-- que son una fraccion de la tabla. Mas pequeno, mas barato de mantener y
-- solo se usa cuando la consulta trae el mismo WHERE (Clase 7).
CREATE INDEX idx_cita_programada ON cita (fecha_hora)
  WHERE estado = 'PROGRAMADA';

-- ======================================================================
-- BLOQUE 5 - PRUEBAS DE ACEPTACION DE LAS TRES REGLAS DEL PI
--
-- OJO A LA ASIMETRIA, que es lo que se califica de verdad: las pruebas 1 y
-- 2 son NEGATIVAS -- lo correcto es que revienten -- y la 3 es POSITIVA
-- -- lo correcto es que ocurra un efecto --. Envolver la 3 en un
-- EXCEPTION WHEN OTHERS y no comprobar nada no prueba absolutamente nada:
-- un bloque que no falla imprimiria "OK" tambien con el trigger borrado.
--
-- Cada bloque DO abre una subtransaccion, asi que cuando el handler corre,
-- lo que la prueba intento ya se deshizo (Clase 8). Por eso estas pruebas
-- no dejan basura en la base.
-- ======================================================================

-- PRUEBA 1: una mascota inactiva no puede agendar cita.
DO $$
BEGIN
  CALL sp_agendar_cita(3, 1, TIMESTAMP '2026-09-20 10:00:00');   -- Rocky, inactiva
  RAISE NOTICE 'FALLO LA PRUEBA 1: se agendo cita a una mascota inactiva';
EXCEPTION WHEN OTHERS THEN
  -- RAISE EXCEPTION sin codigo propio produce SQLSTATE P0001, cuya
  -- condicion se llama raise_exception; aqui se captura con OTHERS porque
  -- es lo que pide el enunciado.
  RAISE NOTICE 'PRUEBA 1 OK -> %', SQLERRM;
END $$;

-- PRUEBA 2: el stock de un insumo no puede quedar negativo.
DO $$
BEGIN
  UPDATE insumo SET stock = stock - 100 WHERE id_insumo = 2;   -- stock actual 3
  RAISE NOTICE 'FALLO LA PRUEBA 2: el stock quedo negativo';
EXCEPTION WHEN check_violation THEN
  -- Aqui SI conviene la condicion precisa (SQLSTATE 23514) en vez de
  -- OTHERS: con OTHERS, un error de escritura en el nombre de la tabla
  -- tambien se reportaria como "PRUEBA 2 OK". Una prueba que pasa por el
  -- motivo equivocado es peor que una prueba que falla.
  RAISE NOTICE 'PRUEBA 2 OK -> %', SQLERRM;
END $$;

SELECT stock AS stock_del_insumo_2 FROM insumo WHERE id_insumo = 2;   -- 3

-- PRUEBA 3: un cambio de estado de cita queda auditado.
DO $$
DECLARE
  v_antes   INT;
  v_despues INT;
BEGIN
  SELECT COUNT(*) INTO v_antes FROM audit_cita;
  UPDATE cita SET estado = 'ATENDIDA' WHERE id_cita = 1;   -- estaba PROGRAMADA
  SELECT COUNT(*) INTO v_despues FROM audit_cita;

  IF v_despues = v_antes + 1 THEN
    RAISE NOTICE 'PRUEBA 3 OK -> audit_cita paso de % a % filas', v_antes, v_despues;
  ELSE
    RAISE NOTICE 'FALLO LA PRUEBA 3: audit_cita sigue en % filas', v_despues;
  END IF;
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'PRUEBA 3 CON ERROR -> %', SQLERRM;
END $$;

SELECT id_cita, accion, valor_anterior, valor_nuevo, usuario_bd
  FROM audit_cita ORDER BY id_audit;   -- 1 fila: 1 | CAMBIO_ESTADO | PROGRAMADA | ATENDIDA

-- ======================================================================
-- BLOQUE 6 - CONSULTA DE CIERRE: INVENTARIO DE LA ENTREGA
--
-- UNION ALL no garantiza orden, asi que el ORDER BY no es opcional si se
-- quiere una salida estable para pegar en el informe.
-- ======================================================================
  SELECT 'dueno'           AS tabla, COUNT(*) AS filas FROM dueno
UNION ALL SELECT 'veterinario',     COUNT(*) FROM veterinario
UNION ALL SELECT 'mascota',         COUNT(*) FROM mascota
UNION ALL SELECT 'cita',            COUNT(*) FROM cita
UNION ALL SELECT 'consulta',        COUNT(*) FROM consulta
UNION ALL SELECT 'insumo',          COUNT(*) FROM insumo
UNION ALL SELECT 'factura',         COUNT(*) FROM factura
UNION ALL SELECT 'detalle_factura', COUNT(*) FROM detalle_factura
UNION ALL SELECT 'audit_cita',      COUNT(*) FROM audit_cita
ORDER BY tabla;

-- ----------------------------------------------------------------------
-- 6b. EXTRA: verificar los minimos exigidos, en vez de afirmarlos
--
-- Es la misma idea de la Clase 13: "cumple los minimos" es una afirmacion,
-- y una afirmacion se verifica con una consulta. La ultima fila es la mas
-- interesante -- comprueba que ninguna factura este descuadrada --, y es la
-- que las facturas del banco de la Clase 11 no pasarian.
-- ----------------------------------------------------------------------
  SELECT 'mascotas inactivas (>= 2)' AS requisito, COUNT(*) AS valor,
         CASE WHEN COUNT(*) >= 2 THEN 'CUMPLE' ELSE 'REVISAR' END AS veredicto
    FROM mascota WHERE activa = 'N'
UNION ALL
  SELECT 'insumos con stock < 5 (>= 1)', COUNT(*),
         CASE WHEN COUNT(*) >= 1 THEN 'CUMPLE' ELSE 'REVISAR' END
    FROM insumo WHERE stock < 5
UNION ALL
  SELECT 'estados distintos de cita (>= 3)', COUNT(DISTINCT estado),
         CASE WHEN COUNT(DISTINCT estado) >= 3 THEN 'CUMPLE' ELSE 'REVISAR' END
    FROM cita
UNION ALL
  SELECT 'facturas descuadradas (debe ser 0)', COUNT(*),
         CASE WHEN COUNT(*) = 0 THEN 'CUMPLE' ELSE 'REVISAR' END
    FROM factura f
   WHERE f.total <> (SELECT c.precio FROM consulta c
                      WHERE c.id_consulta = f.id_consulta)
                  + COALESCE((SELECT SUM(d.cantidad * d.precio_unit)
                                FROM detalle_factura d
                               WHERE d.id_factura = f.id_factura), 0);

-- ======================================================================
-- FIN DEL SCRIPT MAESTRO
-- Lo que este script NO cubre, y esta declarado en el informe: el respaldo
-- fisico y su restauracion nunca se ensayaron, y el particionamiento se
-- diseno pero no se probo con volumen real. Se documenta porque un
-- entregable que oculta sus limites obliga al jurado a encontrarlos.
-- ======================================================================
```

### Salida esperada

```
BLOQUE 0 - Registro

INSERT 0 1

 id_entrega |          estudiante            | codigo  |          proyecto           | fecha_entrega
------------+--------------------------------+---------+-----------------------------+---------------
          1 | Ejemplo del docente            | 000000  | VetCare-Demo                | 2026-11-16
          2 | Nombre Completo Del Estudiante | 1234567 | VetCare DB - Sistema de ... | 2026-11-16

Dos filas, y la del estudiante es la 2. La fecha sale de CURRENT_DATE.

BLOQUE 2 - El UPDATE que calcula los totales

UPDATE 2

factura 1 = 40000 + 31000 + 2400 = 73400.00
factura 2 = 38000 +  9500 + 22000 = 69500.00

Ninguno de los dos numeros se escribio a mano, y por eso la ultima fila de la
verificacion 6b puede dar CUMPLE.

BLOQUE 3 - La funcion

 cirugia | dermatologia | general
---------+--------------+---------
  120000 |        65000 |   40000

BLOQUE 5 - Las tres pruebas de aceptacion

NOTICE:  PRUEBA 1 OK -> La mascota 3 esta inactiva: no se puede agendar
NOTICE:  PRUEBA 2 OK -> new row for relation "insumo" violates check constraint "ck_insumo_stock"
NOTICE:  PRUEBA 3 OK -> audit_cita paso de 0 a 1 filas

Las tres lineas empiezan con OK y ninguna dice FALLO: eso es el entregable del
bloque. Fijate en el mensaje de la prueba 2 -- trae el nombre "ck_insumo_stock"
porque la restriccion se nombro a proposito, y ese nombre es lo que la
aplicacion puede traducir a "stock insuficiente" sin mostrarle al usuario el
texto crudo del motor.

 stock_del_insumo_2
--------------------
                  3

Sigue en 3: el UPDATE de la prueba 2 se deshizo completo. El bloque DO abrio una
subtransaccion y el handler corrio DESPUES del retroceso -- es el mismo mecanismo
que hace atomica una funcion de facturacion (Clase 8).

 id_cita |    accion     | valor_anterior | valor_nuevo | usuario_bd
---------+---------------+----------------+-------------+------------
       1 | CAMBIO_ESTADO | PROGRAMADA     | ATENDIDA    | postgres

BLOQUE 6 - Inventario de la entrega (9 filas)

      tabla      | filas
-----------------+-------
 audit_cita      |     1
 cita            |     8
 consulta        |     2
 detalle_factura |     4
 dueno           |     5
 factura         |     2
 insumo          |     4
 mascota         |     8
 veterinario     |     3

Nueve filas, una por tabla. Y notese que audit_cita esta en 1 y no en 0: la
unica fila que tiene la puso la prueba 3. Un inventario con audit_cita en 0
significa que el trigger no se disparo, y entonces la prueba 3 no probo nada
aunque haya impreso OK.

6b - Verificacion de los minimos (4 filas)

              requisito              | valor | veredicto
-------------------------------------+-------+-----------
 mascotas inactivas (>= 2)           |     2 | CUMPLE
 insumos con stock < 5 (>= 1)        |     1 | CUMPLE
 estados distintos de cita (>= 3)    |     3 | CUMPLE
 facturas descuadradas (debe ser 0)  |     0 | CUMPLE

Los estados distintos siguen siendo 3 despues de la prueba 3: la cita 1 paso de
PROGRAMADA a ATENDIDA, pero quedan PROGRAMADA (3, 6, 8), ATENDIDA (1, 2, 5, 7) y
CANCELADA (4).

Si alguna fila dice REVISAR, la verificacion esta haciendo su trabajo y hay que
volver al bloque 2 antes de entregar. La ultima es la que mas importa: es la
unica que compara un dato guardado contra el mismo dato derivado, y es
exactamente la comprobacion que las facturas de la Clase 11 no pasaban.
```

### Como calificar

- **6 pts — el script corre completo, de arriba abajo y sin un solo error, sobre la base limpia.** Es la condicion de la que dependen los demas puntos y se verifica ejecutandolo, no leyendolo. Si un `CREATE` de la mitad falla, todo lo que venga despues tampoco corre: en ese caso se califica hasta donde llego y se devuelve el mensaje de error exacto, que casi siempre es un `REFERENCES` a una tabla que se crea mas abajo o un `INSERT` que viola una FK por orden. Incluye los 2 pts del **Bloque 0**: el `INSERT` en `entrega_final` con datos reales, y sin borrar la fila de ejemplo del docente.
- **8 pts — Bloque 1, el DDL.** 4 pts las 8 tablas mas `audit_cita` con sus PK; 2 pts **todas** las FK —`mascota→dueno`, `cita→mascota`, `cita→veterinario`, `consulta→cita`, `factura→consulta`, `detalle_factura→factura` y `detalle_factura→insumo`—; 2 pts las cinco restricciones de dominio que el enunciado enumera. Se reconoce como sobresaliente **nombrar** los `CHECK` —`ck_insumo_stock`— porque el nombre viaja en el mensaje de error y es lo que permite traducirlo a un mensaje de negocio (Clase 12); y justificar que `audit_cita` no lleva FK, que el `ON DELETE CASCADE` va solo en `id_factura` y que `consulta.id_cita` es `UNIQUE` porque es una regla de negocio.
- **5 pts — Bloque 2, la semilla, contra los minimos del enunciado:** 5 duenos, 3 veterinarios, 8 mascotas con **2 inactivas**, 8 citas en distintos estados, 4 insumos con **uno de stock menor a 5**, 2 facturas con detalle. Se verifica con el inventario del bloque 6, no contando a ojo. El fallo mas comun no es de cantidad sino de **cadena de dependencias**: dos facturas exigen dos `consulta`, y `consulta.id_cita` es `UNIQUE`, asi que exigen dos citas atendidas distintas. Se reconoce como sobresaliente **calcular** el `factura.total` con un `UPDATE` en vez de escribirlo: es la leccion de la Clase 11 aplicada a la propia entrega.
- **7 pts — Bloque 3, la logica.** 2 pts la funcion; 3 pts el procedimiento con la validacion **efectiva** —que la prueba 1 lo demuestre, no que el `IF` este escrito—; 2 pts el trigger de auditoria **como dos objetos**, la funcion `RETURNS TRIGGER` y el `CREATE TRIGGER`. Se reconoce como sobresaliente declarar la funcion `IMMUTABLE` con su razon, usar `AFTER` y no `BEFORE` para auditar, y conservar el `IF NEW.estado IS DISTINCT FROM OLD.estado` explicando que `UPDATE OF estado` se dispara cuando la columna se **menciona**, aunque el valor no cambie.
- **3 pts — Bloque 4, los indices:** 1,5 cada uno, con nombre claro y sobre columnas que **algun reporte de la pregunta 2 filtra de verdad**. Un indice sobre una columna que nadie consulta cuesta escritura y no da nada, y eso resta. Se reconoce como sobresaliente el orden igualdad-antes-de-rango en `(id_veterinario, fecha_hora)`, un indice **parcial** con su justificacion, y senalar que PostgreSQL **no** indexa las llaves foraneas automaticamente.
- **4 pts — Bloque 5, las tres pruebas,** algo mas de 1,3 cada una, y se califica el **resultado**, no la intencion: la prueba 1 tiene que imprimir el mensaje de mascota inactiva, la prueba 2 el de la restriccion de stock y la prueba 3 tiene que mostrar que `audit_cita` **crecio**. Aqui esta el discriminador de la pregunta: **las dos primeras son negativas y la tercera es positiva**, y por tanto no se escriben igual. Un `EXCEPTION WHEN OTHERS` alrededor de un `UPDATE` que funciona no prueba nada —imprimiria «OK» tambien con el trigger borrado—, y eso cuesta el punto completo de la prueba 3. Se reconoce como sobresaliente usar `WHEN check_violation` en la prueba 2 y explicar por que ahi la condicion precisa es mejor que `OTHERS`.
- **2 pts — Bloque 6, el inventario,** en **una sola** consulta con `UNION ALL` y las 9 tablas. Se descuenta si no lleva `ORDER BY`: `UNION ALL` no garantiza orden y la salida deja de ser estable para el informe. Detalle que vale la pena revisar: si `audit_cita` sale en **0**, el trigger no se disparo y la prueba 3 no probo nada, aunque haya impreso «OK».
- **Cero sintaxis Oracle, y es eliminatorio por bloque:** un `NUMBER`, un `VARCHAR2`, un `RAISE_APPLICATION_ERROR`, un `DUAL`, un `SQL%ROWCOUNT` o un `/` de terminacion **no compila**, asi que el bloque donde aparezca no corre y pierde sus puntos por la via de los hechos. Al devolver la nota conviene decir el equivalente correcto —`NUMERIC`, `TEXT`, `RAISE EXCEPTION`, `GET DIAGNOSTICS ... = ROW_COUNT`— porque es el punto 4 de la pregunta 5.

### Errores frecuentes y que hacer

- **Un script que solo corre a la segunda,** o que exige comentar unas lineas para pasar. Es el error mas caro porque arrastra a todos los bloques siguientes. Causas habituales: `REFERENCES` a una tabla que se crea mas abajo, `INSERT` de `mascota` antes de `dueno`, o `CREATE TRIGGER` antes de su funcion. La comprobacion es barata: ejecutarlo una vez de cero, que en ExamLab se puede porque la base se vuelve a sembrar en cada intento.
- **Escribir el `factura.total` a mano.** Funciona, pasa la corrida y deja la entrega con el mismo defecto que se documento en la Clase 11: el numero guardado y el numero derivado dejan de coincidir sin que nadie lo note. El `UPDATE` que lo calcula son cuatro lineas y ademas habilita la ultima fila de la verificacion 6b.
- **Solo dos facturas «porque el enunciado pide dos», y una sola consulta.** Falla, y el mensaje no es obvio: `consulta.id_cita` es `UNIQUE` y `factura.id_consulta` es `NOT NULL REFERENCES consulta`, asi que dos facturas necesitan dos consultas, que necesitan dos citas atendidas distintas. Es la cadena de dependencias que rompe mas semillas.
- **Escribir la prueba 3 con el molde de las dos primeras:** un `UPDATE` envuelto en `EXCEPTION WHEN OTHERS THEN RAISE NOTICE` y nada mas. No prueba nada: el bloque no falla, imprime «OK» y seguiria imprimiendolo con el trigger eliminado. Una prueba positiva necesita **comparar** el antes con el despues, y esa comparacion es la prueba.
- **`RAISE_APPLICATION_ERROR`, `NUMBER`, `VARCHAR2`, `DUAL`, `SQL%ROWCOUNT` o un `/` al final de los bloques.** Es material heredado de PL/SQL y en PostgreSQL no compila. Los reemplazos: `RAISE EXCEPTION 'texto %', var;`, `NUMERIC` y `TEXT`, un `SELECT` sin `FROM`, y `GET DIAGNOSTICS v_filas = ROW_COUNT;`.
- **Un trigger «de una sola pieza»,** con la logica dentro del `CREATE TRIGGER`. En PostgreSQL son siempre dos objetos: la funcion `RETURNS TRIGGER` y la asociacion que la llama con `EXECUTE FUNCTION`. Es la diferencia con Oracle que mas se repite y merece estar en la respuesta de la pregunta 5.
- **Indices puestos para cumplir el requisito:** `CREATE INDEX ON dueno(nombre)` cuando ningun reporte filtra por ahi, o un indice sobre una columna que ya tiene PK. Cuestan escritura, no aportan lectura y delatan que el bloque 4 se lleno sin mirar el bloque de consultas.
- **Borrar la fila de ejemplo de `entrega_final`** para «dejar la tabla limpia». Modificar la semilla no es entregar, y ademas hace que el script deje de ser reproducible sobre la base tal como se recibe.
- **Un inventario sin `ORDER BY`,** o repartido en nueve consultas sueltas. El enunciado pide **una** consulta, y sin `ORDER BY` el orden de un `UNION ALL` no esta garantizado, asi que la captura del informe puede no coincidir con la del docente al reejecutar.

---

## Pregunta 2 · Los KPIs que se proyectan en la sustentacion · 20 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- ======================================================================
-- ANTES DE EMPEZAR: LA SEMILLA NO EJERCE LAS CONDICIONES DE BORDE
--
-- La rubrica exige que K1 conserve los veterinarios SIN citas y que K3
-- incluya los insumos NUNCA vendidos. Pero en los datos entregados los 4
-- veterinarios tienen citas y los 6 insumos se han vendido, y K2 tiene sus
-- 3 facturas en un mismo mes. Es decir: la consulta correcta y la
-- incorrecta devuelven exactamente lo mismo, y nadie se enteraria.
--
-- Un KPI que no se ha probado contra su caso de borde es una suposicion.
-- Asi que primero se CREA el caso de borde -- tres INSERT -- y despues se
-- corre cada consulta. Esto es lo mismo que se hizo con el respaldo en la
-- Clase 13: la prueba que falta es la que decide si el control existe.
-- ======================================================================

-- Un veterinario recien contratado, sin citas todavia -> pone a prueba el
-- LEFT JOIN de K1 y la division por cero.
INSERT INTO veterinario (nombre, especialidad) VALUES ('Sara Quintero', 'Odontologia');

-- Un insumo que aun no se ha vendido -> pone a prueba el LEFT JOIN de K3.
INSERT INTO insumo (nombre, stock, precio_unit) VALUES ('Collar isabelino', 15, 18000);

-- La consulta 4 (cita 10, Desparasitacion, 35000) estaba sin facturar. Al
-- facturarla en octubre, K2 pasa a tener dos meses y su ORDER BY empieza a
-- significar algo. Ojo: si haces este INSERT antes de la primera corrida de
-- K2, tus numeros de septiembre no cambian pero aparece una fila mas.
INSERT INTO factura (id_consulta, fecha, total)
VALUES (4, TIMESTAMP '2026-10-02 10:15:00', 35000);

-- ======================================================================
-- K1 - CARGA POR VETERINARIO
--
-- Tres decisiones deliberadas:
--   LEFT JOIN  -> conserva al veterinario sin citas (si fuera JOIN, Sara
--                 desapareceria y el reporte diria que la clinica tiene 4
--                 veterinarios cuando tiene 5).
--   NULLIF     -> evita la division por cero justo en esa fila; sin el, la
--                 consulta no devuelve un numero raro: revienta entera.
--   ORDER BY con desempate -> tres veterinarios tienen 2 citas, y sin el
--                 segundo criterio el orden entre ellos no esta garantizado
--                 y la diapositiva puede salir distinta en la sustentacion.
-- ======================================================================
SELECT v.nombre                                          AS veterinario,
       COUNT(c.id_cita)                                  AS total_citas,
       COUNT(*) FILTER (WHERE c.estado = 'ATENDIDA')     AS atendidas,
       COUNT(*) FILTER (WHERE c.estado = 'CANCELADA')    AS canceladas,
       ROUND(COALESCE(COUNT(*) FILTER (WHERE c.estado = 'CANCELADA') * 100.0
                      / NULLIF(COUNT(c.id_cita), 0), 0), 1) AS pct_cancelacion
  FROM veterinario v
  LEFT JOIN cita c ON c.id_veterinario = v.id_veterinario
 GROUP BY v.id_veterinario, v.nombre
 ORDER BY total_citas DESC, v.nombre;

-- FILTER es la forma moderna y legible. El equivalente portable, por si el
-- motor de destino es viejo, es COUNT(CASE WHEN c.estado='ATENDIDA' THEN 1 END).
-- Lo que NO sirve es COUNT(*) sin filtro con LEFT JOIN: contaria 1 para el
-- veterinario sin citas, porque la fila extendida con nulos existe.

-- ======================================================================
-- K2 - INGRESOS POR MES
--
-- date_trunc('month', fecha) lleva toda fecha del mes al dia 1 a las 00:00,
-- y agrupar por esa expresion es lo que produce un mes calendario de
-- verdad. Se agrupa por la expresion, no por el alias.
-- ======================================================================
SELECT date_trunc('month', f.fecha) AS mes,
       COUNT(*)                     AS facturas,
       SUM(f.total)                 AS total_facturado
  FROM factura f
 GROUP BY date_trunc('month', f.fecha)
 ORDER BY mes;

-- ADVERTENCIA HONESTA PARA LA SUSTENTACION: este KPI suma factura.total,
-- que es lo que pide el enunciado. En los datos entregados ese total NO
-- coincide con consulta.precio + suma del detalle en ninguna de las tres
-- facturas originales -- es la misma inconsistencia que la prueba 5 de la
-- Clase 11 --. La consulta esta bien; el dato guardado es el que discrepa.
-- Si el jurado pregunta cual es la cifra buena, la respuesta es que hay que
-- elegir UNA definicion y hacerla cumplir con una restriccion o un trigger.
SELECT f.id_factura, f.total AS total_guardado,
       (SELECT c.precio FROM consulta c WHERE c.id_consulta = f.id_consulta)
       + COALESCE((SELECT SUM(d.cantidad * d.precio_unit) FROM detalle_factura d
                    WHERE d.id_factura = f.id_factura), 0) AS total_derivado
  FROM factura f ORDER BY f.id_factura;

-- ======================================================================
-- K3 - TOP INSUMOS CONSUMIDOS
--
-- El LEFT JOIN trae los insumos nunca vendidos y el COALESCE convierte su
-- SUM nulo en 0. El cast a NUMERIC(12,2) es para que la columna de valor
-- salga con dos decimales tambien en la fila del insumo sin ventas.
-- ======================================================================
SELECT i.nombre                                           AS insumo,
       COALESCE(SUM(d.cantidad), 0)                       AS unidades_vendidas,
       COALESCE(SUM(d.cantidad * d.precio_unit), 0)::NUMERIC(12,2) AS valor_generado,
       i.stock                                            AS stock_restante
  FROM insumo i
  LEFT JOIN detalle_factura d ON d.id_insumo = i.id_insumo
 GROUP BY i.id_insumo, i.nombre, i.stock
 ORDER BY unidades_vendidas DESC, valor_generado DESC;

-- ======================================================================
-- K4 - FICHA DE UN DUENO (historia clinica resumida)
--
-- Los dos primeros JOIN son internos a proposito: una cita sin mascota o
-- sin veterinario no puede existir, hay FK que lo garantizan. Los dos
-- ultimos son LEFT porque una cita PROGRAMADA todavia no tiene consulta, y
-- una consulta puede no estar facturada: si fueran JOIN, la ficha mostraria
-- solo lo ya cobrado, que es justo lo contrario de una historia clinica.
-- ======================================================================
SELECT m.nombre       AS mascota,
       c.fecha_hora,
       c.estado,
       v.nombre       AS veterinario,
       co.diagnostico,
       f.total        AS total_facturado
  FROM dueno du
  JOIN mascota m        ON m.id_dueno       = du.id_dueno
  JOIN cita c           ON c.id_mascota     = m.id_mascota
  JOIN veterinario v    ON v.id_veterinario = c.id_veterinario
  LEFT JOIN consulta co ON co.id_cita       = c.id_cita
  LEFT JOIN factura f   ON f.id_consulta    = co.id_consulta
 WHERE du.nombre = 'Ana Gomez'
 ORDER BY c.fecha_hora;

-- Filtrar por nombre es lo que pide el enunciado y conviene decir en voz
-- alta que en produccion se filtraria por du.id_dueno: dos duenos pueden
-- llamarse igual, y el nombre no es identificador. Ojo tambien con el
-- ultimo LEFT JOIN: factura.id_consulta no es UNIQUE, asi que si una
-- consulta llegara a tener dos facturas, esta ficha duplicaria la cita. Es
-- exactamente lo que produce api_facturar de la Clase 12 cuando una visita
-- lleva tres insumos.

-- ======================================================================
-- LO QUE HABILITA CADA NUMERO (esto es lo que pide el cierre del enunciado)
--
-- -- K1: Paula Salazar sale con 50,0 % de cancelacion, el peor indicador de
-- --     los cinco. DECISION: ninguna todavia, y decirlo es parte del
-- --     analisis -- son 1 de 2 citas, y una tasa sobre dos casos no es una
-- --     tasa. Lo que habilita es una medicion con mas volumen antes de
-- --     tocar la agenda. Laura Restrepo concentra 4 de las 10 citas: ahi si
-- --     hay una decision inmediata de reparto de carga.
-- -- K2: septiembre cierra en 178.200 con 3 facturas -> ticket promedio
-- --     59.400. DECISION: es la linea base contra la que se compara
-- --     octubre; con la factura de octubre (35.000) la caida es visible al
-- --     instante y dispara la revision de citas atendidas sin facturar.
-- -- K3: la gasa esteril es la mas vendida en unidades (4) y solo genera
-- --     4.800; la vacuna triple felina vende 1 unidad, genera 31.000 y
-- --     queda con stock 3. DECISION: la reposicion se prioriza por la
-- --     triple felina, no por la gasa. Unidades y valor ordenan distinto, y
-- --     ordenar por la columna equivocada invierte la decision.
-- -- K4: Ana Gomez tiene 4 citas y 2 sin consulta, una de ellas PROGRAMADA
-- --     para el 2026-09-08. DECISION: es la lista de llamadas de
-- --     confirmacion de la semana, y ademas explica por que la ficha usa
-- --     LEFT JOIN: las citas sin consulta son precisamente las accionables.
-- ======================================================================
```

### Salida esperada

```
K1 - Carga por veterinario (5 filas, con Sara Quintero ya insertada)

   veterinario   | total_citas | atendidas | canceladas | pct_cancelacion
-----------------+-------------+-----------+------------+-----------------
 Laura Restrepo  |           4 |         3 |          0 |             0.0
 Diego Moreno    |           2 |         1 |          0 |             0.0
 Ivan Ortiz      |           2 |         0 |          0 |             0.0
 Paula Salazar   |           2 |         0 |          1 |            50.0
 Sara Quintero   |           0 |         0 |          0 |             0.0

La fila que importa es la ultima, y es la que la semilla original no permitia
ver: 0 citas, 0 atendidas, 0 canceladas y 0.0 de porcentaje **sin que la
consulta reviente**. Sin el NULLIF esa fila no sale mal: la consulta entera
falla con "division by zero" y no hay diapositiva. Y sin el LEFT JOIN, Sara
simplemente no aparece y el reporte afirma que la clinica tiene 4 veterinarios.

Tres veterinarios empatan en 2 citas, asi que el desempate por nombre no es un
adorno: sin el, el orden entre Diego, Ivan y Paula no esta garantizado y la
captura del informe puede no coincidir con lo que se proyecte en vivo.

K2 - Ingresos por mes

Primera corrida, con las 3 facturas originales (1 fila):

         mes         | facturas | total_facturado
---------------------+----------+-----------------
 2026-09-01 00:00:00 |        3 |       178200.00

Con la factura de octubre (2 filas):

         mes         | facturas | total_facturado
---------------------+----------+-----------------
 2026-09-01 00:00:00 |        3 |       178200.00
 2026-10-01 00:00:00 |        1 |        35000.00

178.200 = 71.000 + 47.000 + 60.200. Con una sola fila, el "ordena
cronologicamente" de la rubrica no se puede comprobar; con dos, si.

Contraste total guardado / total derivado (4 filas):

 id_factura | total_guardado | total_derivado
------------+----------------+----------------
          1 |       71000.00 |       81400.00
          2 |       47000.00 |       54500.00
          3 |       60200.00 |       83600.00
          4 |       35000.00 |       35000.00

Las tres facturas de la semilla estan descuadradas -- y no por poco -- bajo la
definicion "precio de la consulta mas la suma del detalle". La unica que cuadra
es la 4, la que se acaba de crear calculando el numero. No es un error del
estudiante ni de la consulta: es el dato guardado, y es la misma inconsistencia
de la prueba 5 de la Clase 11. Llevar esta tabla a la sustentacion es mejor que
esperar a que el jurado la encuentre.

K3 - Top insumos consumidos (7 filas, con Collar isabelino ya insertado)

         insumo          | unidades_vendidas | valor_generado | stock_restante
-------------------------+-------------------+----------------+----------------
 Gasa esteril            |                 4 |        4800.00 |              8
 Jeringa 5ml             |                 3 |        2700.00 |             60
 Antiparasitario oral    |                 2 |       19000.00 |             40
 Vacuna triple felina    |                 1 |       31000.00 |              3
 Vacuna antirrabica      |                 1 |       22000.00 |             12
 Suero fisiologico 500ml |                 1 |        7000.00 |             25
 Collar isabelino        |                 0 |           0.00 |             15

Dos cosas para la sustentacion. La ultima fila es la que prueba el LEFT JOIN con
COALESCE: 0 unidades, 0.00 de valor, y **aparece**. Con un JOIN interno se
perderia justo el insumo del que interesa saber que no rota.

Y el orden: la gasa esteril encabeza por unidades con 4.800 de valor, mientras
la vacuna triple felina vende una sola unidad, genera 31.000 y se queda con
stock 3. Ordenar por unidades y ordenar por valor dan rankings casi invertidos,
y la decision de reposicion cambia por completo segun la columna elegida. Eso es
lo que hay que decir al proyectar la lamina.

K4 - Ficha de Ana Gomez (4 filas)

  mascota | fecha_hora          |   estado    |  veterinario   |       diagnostico        | total_facturado
----------+---------------------+-------------+----------------+--------------------------+-----------------
 Firulais | 2026-09-01 08:00:00 | PROGRAMADA  | Laura Restrepo |                          |
 Luna     | 2026-09-01 09:00:00 | ATENDIDA    | Laura Restrepo | Vacunacion triple felina |        71000.00
 Firulais | 2026-09-05 15:00:00 | ATENDIDA    | Laura Restrepo | Otitis externa           |        60200.00
 Luna     | 2026-09-08 16:00:00 | PROGRAMADA  | Paula Salazar  |                          |

Cuatro filas: las dos mascotas de Ana Gomez (Firulais y Luna) con dos citas cada
una. Dos traen diagnostico y total; dos vienen con las dos ultimas columnas
vacias, porque son citas PROGRAMADA que todavia no generaron consulta.

Esas dos filas vacias son la razon de ser del LEFT JOIN, y conviene decirlo asi
en la sustentacion: con JOIN interno la ficha mostraria 2 filas en vez de 4 y
seria un historial de cobros, no una historia clinica. Ademas la cita del
2026-09-08 sigue PROGRAMADA: es exactamente la fila accionable del reporte.
```

### Como calificar

- **6 pts — K1.** 2 pts que corra y devuelva las cuatro columnas pedidas mas el porcentaje redondeado a un decimal; **2 pts el `LEFT JOIN` que conserva al veterinario sin citas**; 2 pts el `NULLIF` o el `CASE` que evita la division por cero. Y aqui viene el detalle que hay que tener presente al calificar: **con la semilla tal como llega, los cuatro veterinarios tienen citas**, asi que la consulta correcta y la incorrecta devuelven lo mismo. Se otorgan los 4 pts de borde solo si el estudiante **crea** el caso —un `INSERT` de un veterinario nuevo— y muestra la fila con ceros, o si al menos deja escrito en un comentario que la semilla no lo ejerce.
- **4 pts — K2.** 2 pts el `date_trunc('month', f.fecha)` en el `SELECT` y en el `GROUP BY` con el conteo y la suma correctos; 2 pts el orden cronologico **demostrado**, que con las tres facturas originales cae todo en un solo mes y no se puede comprobar: se otorgan si el estudiante agrega una factura en otro mes o lo advierte por escrito. El total de septiembre es **178.200,00**. Se reconoce como sobresaliente notar que `factura.total` **no** coincide con `consulta.precio` mas el detalle en ninguna de las tres, que es la misma inconsistencia de la Clase 11: la consulta esta bien, el dato guardado es el que discrepa.
- **4 pts — K3.** 2 pts las cuatro columnas con el `SUM(cantidad * precio_unit)` y el orden por unidades descendente; **2 pts el `LEFT JOIN` con `COALESCE` que incluye el insumo nunca vendido**, que —igual que en K1— la semilla no ejerce, porque los seis insumos aparecen en `detalle_factura`. Se reconoce como sobresaliente el analisis del orden: la gasa esteril lidera en unidades con 4.800 de valor mientras la vacuna triple felina vende 1 unidad, genera 31.000 y queda con stock 3, de modo que **unidades y valor dan rankings invertidos** y la decision de reposicion cambia segun la columna elegida.
- **4 pts — K4.** 2 pts las seis columnas con los `JOIN` correctos y el filtro por `Ana Gomez`; 2 pts los `LEFT JOIN` a `consulta` y a `factura` de modo que salgan **4 filas**, dos de ellas con diagnostico y total vacios. Este es el unico KPI cuyo caso de borde **si** esta en la semilla, asi que aqui el `LEFT JOIN` se verifica directamente: si devuelve 2 filas, son `JOIN` internos. Se reconoce como sobresaliente decir que en produccion se filtraria por `id_dueno` y no por nombre, y que el ultimo `LEFT JOIN` puede duplicar filas porque `factura.id_consulta` no es `UNIQUE`.
- **2 pts — los comentarios de cierre,** medio punto por KPI, y se exigen las **dos** mitades que pide el enunciado: el numero concreto obtenido y la decision que habilita. «K1 muestra la carga de trabajo» no vale; «Laura Restrepo concentra 4 de las 10 citas, hay que repartir» si. Se reconoce como sobresaliente la honestidad estadistica en K1: el 50 % de Paula Salazar son 1 de 2 citas, y una tasa sobre dos casos no habilita ninguna decision todavia.
- **Criterio general de esta pregunta:** se califica el resultado contra los datos entregados, no la elegancia. Cualquier consulta que devuelva las filas y los numeros correctos vale completo, use `FILTER`, `CASE WHEN` o subconsultas. Lo que no vale es una consulta cuya correccion no se pueda distinguir de su incorreccion, y de ahi el peso de los cuatro puntos de borde.

### Errores frecuentes y que hacer

- **`JOIN` interno donde el enunciado pide `LEFT JOIN`,** en K1, K3 o K4. En K4 se detecta al instante —devuelve 2 filas en vez de 4—, pero en K1 y K3 **no se nota con esta semilla**, y ahi esta el riesgo: el estudiante entrega una consulta incorrecta que da el resultado correcto, la proyecta en la sustentacion, y el dia que la clinica contrate un veterinario el reporte lo borra del informe.
- **Dividir sin proteger el cero.** `canceladas * 100.0 / total_citas` no devuelve un valor raro para el veterinario sin citas: **la consulta entera falla** con «division by zero» y no hay diapositiva. `NULLIF(total, 0)` la deja en `NULL` y el `COALESCE` externo la muestra como 0.0.
- **`COUNT(*)` en lugar de `COUNT(c.id_cita)` con `LEFT JOIN`.** La fila extendida con nulos existe, asi que `COUNT(*)` devuelve **1** para el veterinario sin citas: el reporte inventa una cita. Es el error clasico del `LEFT JOIN` con agregados y conviene mostrarlo en pantalla.
- **Agrupar K2 por `f.fecha` en vez de por `date_trunc('month', f.fecha)`.** Devuelve una fila por factura, no por mes, y con tres facturas parece plausible. La comprobacion es contar filas: si hay tantas filas como facturas, no se agrupo por mes.
- **Sumar en K3 `SUM(d.cantidad) * i.precio_unit` en vez de `SUM(d.cantidad * d.precio_unit)`.** Usa el precio **actual** del insumo en lugar del precio al que se vendio. Con esta semilla coinciden y no se nota; en produccion, cualquier cambio de precio reescribe la historia de ventas. `detalle_factura.precio_unit` existe exactamente para eso.
- **Reportar solo el ranking por unidades y decidir con el.** Es el error de interpretacion mas caro de esta pregunta: la gasa esteril encabeza la lista y es el insumo que **menos** importa reponer. La decision de reposicion se toma cruzando valor generado con stock restante.
- **Comentarios de cierre genericos:** «este KPI sirve para tomar decisiones». El enunciado pide el numero concreto obtenido y la decision concreta que habilita. Sin el numero no hay evidencia; sin la decision, el KPI es un adorno.
- **Presentar el 50 % de cancelacion de Paula Salazar como un hallazgo.** Son 1 de 2 citas. Un porcentaje sobre dos casos es ruido, y el jurado lo va a senalar. Decirlo primero convierte un error en criterio.

---

## Pregunta 3 · Checklist de empaquetado del ZIP final · 10 pts

### Clave y por que

La clave se lee del banco de la plataforma, asi que esta es la que se califica. La columna de la derecha es lo que hay que poder responderle al estudiante cuando pregunte.

|  | Opcion | Por que |
|---|---|---|
| **SI** | Los scripts deben ir numerados en su orden de ejecucion (01_ddl.sql, 02_datos.sql, 03_logica.sql, ...) para que cualquiera pueda reconstruir la base de cero. | **Correcta.** El criterio no es el orden alfabetico sino el **orden de ejecucion**: `01_ddl.sql`, `02_datos.sql`, `03_logica.sql`, y asi. La prueba de que sirve es la que se acaba de hacer en la pregunta 1: si alguien que nunca vio el proyecto puede reconstruir la base ejecutando los archivos en el orden en que estan numerados, el paquete funciona. Y hay dependencias que el numero tiene que respetar: los privilegios sobre las funciones van **despues** de crearlas, porque un `GRANT` sobre una funcion que no existe falla (Clase 12). |
| **SI** | Debe incluirse un README que diga en que motor se probo (PostgreSQL), como ejecutar los scripts y en que orden, y quien hizo que. | **Correcta, y el motor es el dato que mas se olvida.** Un script PL/pgSQL ejecutado contra Oracle no falla «un poco»: no compila. El README tiene que decir PostgreSQL, la version si se conoce, el orden de ejecucion y quien hizo que. Ese ultimo punto no es burocracia: es lo que permite preguntarle a la persona correcta en la sustentacion, y en un equipo autorizado es la unica base objetiva para calificar aportes desiguales. |
| no | Basta con adjuntar capturas de pantalla de las consultas funcionando; el codigo fuente es opcional si la demo salio bien. | **Falsa, y es la opcion mas tentadora,** porque la demo salio bien y las capturas se ven convincentes. Una captura demuestra que **algo** funciono una vez en una maquina; no permite reejecutar, ni revisar, ni corregir, ni reutilizar. Un entregable de bases de datos que no se puede volver a ejecutar no es verificable, y es precisamente el reflejo del error de la Clase 13: confundir la evidencia de que algo ocurrio con la capacidad de reproducirlo. |
| **SI** | El ER debe ir tanto en imagen (PNG o el diagrama Mermaid) como reflejado en el DDL: si no coinciden, el entregable es inconsistente. | **Correcta, y la segunda mitad es la que tiene filo:** «si no coinciden, el entregable es inconsistente». El ER en imagen sirve para explicar y el DDL es lo que la base realmente ejecuta, asi que cuando discrepan hay dos verdades y una es falsa. El caso tipico es un diagrama con una tabla o una relacion que el DDL no tiene —o al reves, un `CHECK` que existe en la base y no en el diagrama—, y el jurado lo encuentra en treinta segundos comparando las dos laminas. |
| no | Conviene incluir las credenciales de tu base de datos en el README para que el docente pueda entrar. | **Falsa, y es la unica opcion cuya respuesta incorrecta tiene consecuencias fuera del curso.** Las credenciales no van en el README, ni en los scripts, ni en el codigo de la aplicacion, ni en el repositorio: van en **variables de entorno**, y el README explica **cuales** hay que definir sin decir sus valores. Dos razones concretas: un ZIP se reenvia y se sube a sitios que no se controlan, y una credencial en un archivo versionado queda en el historial aunque se borre despues. Lo que el docente necesita para revisar es el script que reconstruye la base, no una cuenta ajena. |
| **SI** | El informe debe traer las secciones que se fueron construyendo en el semestre: roles y privilegios, respaldo, optimizacion antes/despues, indices, transacciones, concurrencia y lecciones de casos reales. | **Correcta, y ademas es la lista de comprobacion del informe.** Las secciones no se inventan al final: son los hitos del semestre —roles y privilegios de la Clase 2 y la 12, respaldo de la 4 y la 13, optimizacion antes/despues de la 6, indices y particionamiento de la 7, transacciones de la 8, concurrencia de la 10 y lecciones de casos reales de la 13—. Si alguna esta vacia, la señal no es «falta redactar»: es que ese hito no se cerro, y es mejor declararlo que dejar que se note en las preguntas. |

### Como calificar

- **10 pts con las cuatro correctas —0, 1, 3 y 5— y ninguna incorrecta;** puntaje proporcional por acierto parcial, como declara la rubrica de la plataforma. Conviene revisarla en voz alta antes de los turnos de sustentacion, porque las cuatro correctas son literalmente la lista de verificacion del ZIP y varios paquetes se arreglan en cinco minutos con ella.
- **La opcion 4 —credenciales en el README— se corrige aparte y sin ambiguedad,** porque es la unica con consecuencias fuera del curso. Las credenciales van en **variables de entorno** y el README dice cuales definir, no sus valores. Un ZIP se reenvia, se sube y se copia; y una credencial en un archivo versionado sigue en el historial aunque se borre en un commit posterior. Si algun paquete entregado las trae, hay que avisarlo de inmediato y pedir que se roten, no solo descontar el punto.
- **La opcion 2 —capturas en lugar de codigo— es la que mas se marca,** porque la demo salio bien y la captura se ve convincente. El argumento que hay que devolver: una captura prueba que algo funciono una vez en una maquina, y no permite reejecutar, revisar ni corregir. Es el reflejo exacto del error de la Clase 13, con el respaldo que existia como archivo y no como capacidad.
- **En la opcion 3 lo que se califica es la segunda mitad:** «si no coinciden, el entregable es inconsistente». Vale la pena hacer la comparacion al revisar —ER contra DDL— porque encontrar la discrepancia antes de la sustentacion es un regalo, y despues es una pregunta incomoda.
- **Errores de seleccion tipicos:** marcar solo 0 y 1 —quedarse con lo «mecanico» del empaquetado y dejar fuera la coherencia ER/DDL y las secciones del informe—, o marcar las seis, que con puntaje proporcional resta y delata que no se leyeron las dos negativas.

### Errores frecuentes y que hacer

- **Marcar la opcion 4.** Es el error que hay que atender primero, y no por los puntos: si el paquete entregado incluye credenciales de verdad, hay que avisarle al estudiante y pedirle que las cambie. La regla es la misma que se aplico en la Clase 12: la conexion se arma desde variables de entorno y en el codigo no hay ni usuario ni contrasena.
- **Marcar la opcion 2 razonando «pero la demo funciono».** Que funcionara es la condicion minima, no la evidencia. La evidencia es que otra persona pueda reconstruirlo, y eso solo lo da el codigo con su orden de ejecucion.
- **Descartar la opcion 3** porque «el ER es solo documentacion». Es la que se usa para explicar el diseno en la sustentacion: si contradice el DDL, la explicacion describe una base que no existe.
- **Descartar la opcion 5** porque «el informe es aparte del ZIP». El informe es parte del entregable y sus secciones son los hitos del semestre. Una seccion vacia no significa que falte redactar: significa que ese hito quedo abierto, y declararlo vale mas que disimularlo.
- **Marcar las seis opciones.** Con puntaje proporcional, las dos incorrectas restan; y ademas las opciones 1 y 3 del propio taller ya contradicen a la 2 y a la 4, asi que marcarlas todas es responder sin leer.

---

## Pregunta 4 · Acta de entrega y reparto de la sustentacion · 20 pts

### Respuesta esperada

| Orden | Archivo del ZIP | Proposito | Se ejecuta |
|---|---|---|---|
| — | `00_README.md` | Motor y version (PostgreSQL), como ejecutar, orden de los scripts, que variables de entorno definir —**sin valores**— y quien hizo que | No |
| 1 | `01_ddl.sql` | Las 8 tablas mas `audit_cita`, con PK, FK y los `CHECK` nombrados | Si |
| 2 | `02_datos_semilla.sql` | Datos de prueba coherentes con una veterinaria de Cali; los totales de factura se **calculan** al final del script | Si |
| 3 | `03_logica.sql` | `fn_precio_consulta`, `sp_agendar_cita` con su validacion y el trigger de auditoria (funcion + asociacion) | Si |
| 4 | `04_indices.sql` | `idx_cita_vet_fecha`, `idx_cita_mascota`, el parcial `idx_cita_programada` y el unico parcial `uq_cita_vet_franja` de la Clase 10 | Si |
| 5 | `05_optimizacion_antes_despues.sql` | El par de `EXPLAIN (ANALYZE, BUFFERS)` de la Clase 6: `Seq Scan` con `Rows Removed by Filter` antes, `Index Cond` despues | Si |
| 6 | `06_api.sql` | `api_agendar_cita`, `api_registrar_consulta` y `api_facturar`: el contrato `(ok, mensaje, id_generado)` de la Clase 12 | Si |
| 7 | `07_privilegios_api.sql` | Rol `app_vetcare`, `REVOKE`/`GRANT` con firma exacta y el `SECURITY DEFINER SET search_path` sin el cual la app no puede usar la API. **Obligatoriamente despues del 06** | Si |
| 8 | `08_seguridad_sql_dinamico.sql` | `buscar_mascota_segura` con `EXECUTE ... USING`, `DROP` de la version vulnerable y la evidencia 8 → 0 (Clase 13) | Si |
| 9 | `09_respaldo_y_restore.sql` | `respaldo_cita`, `bitacora_respaldo`, `trg_archivar_cita`, la consulta de veredicto y el guion de `pg_dump`/`pg_restore` **aun sin ensayar** | Si |
| 10 | `10_pruebas_aceptacion.sql` | Las 3 reglas de negocio del PI mas la bateria de 5 pruebas de la Clase 11, con la prueba 5 en `cumple = FALSE` documentada | Si |
| — | `app/cliente.py` | Cliente Python de la Clase 12: solo llama a las funciones `api_*`, con `%s` y sin un `INSERT` directo | No (no se evalua ejecucion) |
| — | `er_vetcare.png` + `er_vetcare.mmd` | El ER en imagen y en Mermaid. Tiene que coincidir con `01_ddl.sql`: si no, el entregable es inconsistente | No |
| — | `informe_vetcare.pdf` | Roles y privilegios, respaldo, optimizacion antes/despues, indices, transacciones, concurrencia y lecciones de casos reales | No |
| — | `acta_entrega.pdf` | Este documento: identificacion, inventario, trazabilidad, guion, autoria y estado final firmado | No |

Modelo de referencia del acta. Las cifras y los nombres son de ejemplo; lo que se califica es que las seis secciones existan y que el inventario, la trazabilidad y el guion sean **verificables contra el ZIP entregado**.

### 1. Identificacion

- **Estudiante:** Nombre Completo Del Estudiante · **Codigo:** 1234567
- **Proyecto:** VetCare DB — Sistema de gestion para clinica veterinaria
- **Asignatura:** Bases de Datos II — **FI303215** · Grupo 641A-2
- **Periodo:** 2026-2 · **Fecha de entrega:** 2026-11-16
- **Integrantes:** trabajo individual. (Si el docente autorizo equipo, se lista aqui cada integrante con su codigo, y las secciones 4, 5 y 6 se desglosan por persona.)

### 2. Inventario del paquete

Es la tabla de arriba. Dos reglas que la gobiernan: los archivos numerados se ejecutan **en ese orden** y ninguno necesita que se comente una linea para correr; y `07_privilegios_api.sql` va obligatoriamente **despues** de `06_api.sql`, porque un `GRANT` sobre una funcion que todavia no existe falla.

### 3. Trazabilidad hito por hito

| Clase | Tema | Artefacto del paquete que lo contiene |
|---|---|---|
| 1 | Revision BD I · arranque VetCare | `01_ddl.sql` + `er_vetcare.mmd`: las 8 tablas y el modelo del que salio todo |
| 2 | Administracion de BD · roles | `07_privilegios_api.sql` (rol `app_vetcare`, `REVOKE`/`GRANT`) + informe §roles y privilegios |
| 3 | Procedimientos almacenados | `03_logica.sql`: `sp_agendar_cita` con la validacion de mascota inactiva |
| 4 | Funciones · triggers · respaldo | `03_logica.sql` (`fn_precio_consulta`, `fn_trg_audit_cita` + `trg_audit_cita`) y `09_respaldo_y_restore.sql` |
| 6 | Optimizacion de consultas | `05_optimizacion_antes_despues.sql`: el par de `EXPLAIN` con `Seq Scan` → `Index Cond` |
| 7 | Indices y particionamiento | `04_indices.sql` (compuesto y parcial) + informe §particionamiento, **diseñado y no probado con volumen real** |
| 8 | Tuning · transacciones | `10_pruebas_aceptacion.sql`: facturacion atomica y `CHECK (stock >= 0)` demostrado |
| 10 | Control de concurrencia | `04_indices.sql` (`uq_cita_vet_franja` parcial) + informe §concurrencia con el reintento ante 40001 |
| 11 | Avance PI | `10_pruebas_aceptacion.sql` (bateria de 5 pruebas) + tabla `checklist_pi`, **con la prueba 5 en `FALSE` y explicada** |
| 12 | Integracion app ↔ BD | `06_api.sql`, `07_privilegios_api.sql` y `app/cliente.py` |
| 13 | Analisis de casos reales | `08_seguridad_sql_dinamico.sql`, `09_respaldo_y_restore.sql` e informe §lecciones aprendidas |

**Lo que quedo abierto, declarado aqui y no escondido:**

1. **El respaldo fisico no se ha ensayado.** El guion de `pg_dump` / `pg_restore` esta escrito en `09_respaldo_y_restore.sql` y **nunca se ha ejecutado de punta a punta**. Es el item 12 del checklist de la Clase 11 y sigue en `NO`. Viene abierto desde la Clase 11 y es la consecuencia directa del caso que analice en la Clase 13.
2. **El particionamiento se diseño y no se probo con volumen real.** El criterio de partition pruning esta en el informe; con las 8 citas de la semilla no se puede demostrar.
3. **Las facturas 1 a 3 del avance de la Clase 11 quedan descuadradas.** No es un olvido: es el hallazgo de esa clase, y la correccion —calcular el total en vez de escribirlo— ya esta aplicada en `02_datos_semilla.sql`.

### 4. Guion de la sustentacion — **7 minutos**

| Tramo | Bloque | Min |
|---|---|---|
| 1 | El problema de la clinica y el modelo en una lamina | 0,5 |
| 2 | ER y tres decisiones de diseno (`activa`, `audit_cita` sin FK, `consulta.id_cita` UNIQUE) | 1 |
| 3 | **Demo 1:** `sp_agendar_cita` rechaza una mascota inactiva | 1 |
| 4 | **Demo 2:** stock — el `CHECK` bloquea el negativo y la transaccion deja todo como estaba | 1 |
| 5 | Optimizacion: `EXPLAIN` antes y despues, y el indice que lo explica | 1 |
| 6 | Seguridad: la inyeccion cerrada (8 → 0) y el `SECURITY DEFINER` que hace usable la API | 1 |
| 7 | KPIs: las cuatro laminas de la pregunta 2 | 1 |
| 8 | Lo que falta —el restore sin ensayar— y como lo verificaria | 0,5 |
| | **Total** | **7** |

Cabe en la ventana de 5 a 8 minutos con margen, y el tramo 8 es deliberado: declarar el limite antes de que lo pregunten cambia el tono de la ronda de preguntas. **Plan B en tres niveles:** si la base no responde, se proyecta la salida guardada de `10_pruebas_aceptacion.sql`; si el proyector falla, se cuenta con el ER impreso; y si hay que cortar a 5 minutos, se sacrifican los tramos 5 y 7 —los unicos que no demuestran una regla de negocio—. Si el docente autorizo equipo, cada tramo lleva un nombre y **todos los integrantes hablan**; el reparto natural es modelo y demos para quien escribio la logica, y optimizacion, seguridad y KPIs para quien escribio las consultas.

### 5. Declaracion de autoria y uso de herramientas

El modelo, el DDL, la logica, los indices, las consultas y las pruebas son mios; los escribi y los ejecute. Use asistentes de IA en tres puntos concretos, y en los tres verifique el resultado ejecutandolo: (1) para recordar la sintaxis de `RETURNS TABLE` en PL/pgSQL, que verifique creando la funcion y llamandola —y ahi encontre el error de ambiguedad por sombreado de nombres—; (2) para redactar los comentarios del script maestro, que revise uno por uno contra lo que hace el codigo; (3) para revisar la ortografia del informe. **No** use codigo de terceros sin adaptarlo. Las consultas de la pregunta 2 las escribi contra los datos reales y comprobe cada numero ejecutandolas: el 178.200,00 de septiembre y las 4 filas de la ficha de Ana Gomez salen de la corrida, no de una estimacion.

### 6. Estado final declarado

> **COMPLETO CON OBSERVACIONES.**

Los siete bloques del script maestro corren de cero sin errores y las tres reglas de negocio quedan demostradas con su salida; las dos observaciones son el respaldo fisico sin ensayar —item 12 del checklist, con fecha comprometida el 2026-11-06— y el particionamiento sin volumen real. Declaro `COMPLETO CON OBSERVACIONES` y no `COMPLETO` precisamente porque esas dos cosas estan identificadas y fechadas: un `COMPLETO` con un item en `NO` seria la misma afirmacion sin verificar que estudie en la Clase 13.

**Firma:** _________________ · Nombre Completo Del Estudiante · 1234567 · 2026-11-16

### Como calificar

- **2 pts — Identificacion completa:** nombre y codigo, nombre del proyecto, asignatura con el codigo **FI303215**, periodo **2026-2** y fecha de entrega; y los integrantes si el docente autorizo equipo. Es la seccion mas facil y la que mas se entrega a medias —falta el codigo de la asignatura o la fecha—, asi que conviene revisarla primero.
- **5 pts — Inventario del paquete.** 3 pts que nombre **archivos concretos** con su orden de ejecucion y 2 pts que cubra los minimos del enunciado: DDL, datos semilla, logica, indices, el par antes/despues de optimizacion, las pruebas de las tres reglas, el informe y el ER. «Scripts SQL» como una sola linea vale 1 de 5. Se reconoce como sobresaliente registrar la dependencia de orden que si importa: los privilegios sobre las funciones van **despues** de crearlas, porque un `GRANT` sobre una funcion inexistente falla.
- **6 pts — Trazabilidad de las once clases,** algo mas de 0,5 por fila. Se exige que cada clase apunte a un **artefacto real del paquete**, no al tema: «Clase 6 → optimizacion» vale 0; «Clase 6 → `05_optimizacion_antes_despues.sql`, el par de `EXPLAIN`» vale completo. **Y la mitad de la nota de esta seccion esta en reconocer lo que quedo abierto:** un acta que declara las once clases cerradas cuando el checklist de la Clase 11 tiene el respaldo en `NO` es una contradiccion entre dos entregables del mismo estudiante, y es mejor senalarla al calificar que dejarla para el jurado.
- **4 pts — Guion de sustentacion.** 2 pts que los minutos sumen entre **5 y 8** —se verifica sumando, y un guion de 12 minutos no cabe en la ventana— y 2 pts que cubra todos los bloques: modelo, reglas de negocio, optimizacion, seguridad y resultados. Si hubo equipo autorizado, **todos los integrantes deben tener voz asignada**, y un tramo sin nombre cuesta 1 pt. Se reconoce como sobresaliente reservar el tramo final a declarar el limite conocido, y traer un plan B para cuando la base no responda.
- **2 pts — Declaracion de autoria y uso de herramientas,** y se califica la **especificidad**, no la confesion. «Use IA para algunas partes» vale 0,5; «use IA para recordar la sintaxis de `RETURNS TABLE`, y lo verifique creando la funcion y llamandola» vale completo, porque describe el uso **y** la verificacion. Una declaracion que diga que no se uso ninguna herramienta es perfectamente valida.
- **1 pt — Estado final justificado y firmado,** con una de las tres etiquetas del enunciado. Se reconoce como sobresaliente el `COMPLETO CON OBSERVACIONES` **con las observaciones nombradas y fechadas**: es mas creible que un `COMPLETO` que contradice el checklist, y es la misma leccion de la Clase 13 aplicada al propio acta.
- **Criterio transversal:** el acta se califica **contra el ZIP**, no por si sola. Un inventario que nombra `05_optimizacion_antes_despues.sql` cuando ese archivo no esta en el paquete es peor que no mencionarlo: convierte el acta en una declaracion falsa. Vale la pena abrir el ZIP con el acta al lado y marcar las filas que no existen.

### Errores frecuentes y que hacer

- **Un inventario en prosa:** «entrego los scripts, el informe y el diagrama». No sirve para verificar nada. La rubrica pide archivos concretos con su orden de ejecucion, y ese orden es lo que permite que otra persona reconstruya la base sin preguntar.
- **Trazabilidad que repite el temario.** Una tabla con «Clase 8 → transacciones» copia el programa del curso; lo que se pide es «Clase 8 → `10_pruebas_aceptacion.sql`, la facturacion atomica». Si una clase no tiene artefacto, se dice, y eso vale mas que inventar una correspondencia.
- **Declarar las once clases cerradas cuando no lo estan.** Es el error de fondo de la seccion 3 y suele venir de querer que el acta «quede bien». El jurado tiene el checklist de la Clase 11 con el respaldo en `NO`, asi que la contradiccion se ve; y declarar el pendiente convierte una debilidad en criterio.
- **Un guion que no suma,** o que suma 12 minutos. La ventana es de 5 a 8 y se verifica sumando la columna. Un guion de 12 minutos no es ambicioso: garantiza que el corte llegue justo antes de los resultados.
- **En equipo autorizado, un guion con un solo expositor.** El enunciado exige que **todos** hablen. El reparto natural es que cada uno presente lo que escribio, y eso ademas hace verificable la declaracion de autoria.
- **Declaracion de autoria generica:** «todo el trabajo es mio» sin detalle, o «use IA» sin decir donde ni como se verifico. Las dos formas incumplen la misma exigencia: la seccion pide especificidad, en las dos direcciones.
- **Estado `COMPLETO` con observaciones evidentes en el propio paquete.** Es la afirmacion sin verificar de la Clase 13, aplicada al acta. `COMPLETO CON OBSERVACIONES`, con las dos observaciones nombradas y fechadas, es una declaracion mas fuerte, no mas debil.
- **Nombrar en el inventario archivos que no estan en el ZIP.** Convierte el acta en una declaracion falsa y es facil de detectar: se abre el paquete con el acta al lado. Si un archivo no llego a existir, se retira del inventario y se declara en el punto 3.

---

## Pregunta 5 · Autoevaluacion de cierre: que harias distinto · 15 pts

### Respuesta esperada

Modelo de referencia: lo que se califica es la **especificidad y la evidencia**, no coincidir con estas respuestas. Una autoevaluacion honesta que difiera en todo puede valer 15 de 15.

### 1. La decision de diseno de la que estoy mas orgulloso

Poner las reglas de negocio **en la base y no en la aplicacion**. Concretamente `CHECK (stock >= 0)` en `insumo` y la validacion de mascota inactiva dentro de `sp_agendar_cita`. La tome despues de la Clase 8, cuando entendi que una regla que vive solo en la aplicacion la cumple quien pasa por la aplicacion, y cualquier otro camino —una consulta manual, un script de carga, otro programa— la ignora. **Evidencia:** la prueba 2 del script maestro intenta `UPDATE insumo SET stock = stock - 100` sobre un stock de 3 y el motor la rechaza con «violates check constraint “ck_insumo_stock”»; despues del bloque, el stock sigue en 3 porque la subtransaccion se deshizo completa. No es una opinion sobre mi diseno: es una linea de salida que puedo proyectar.

### 2. La decision que cambiaria

**Calcularia `factura.total` desde el principio en vez de guardarlo escrito a mano.** En la Clase 1 lo puse como una columna que se llenaba al insertar, y en la Clase 11 descubri que las tres facturas del avance estaban descuadradas: el total guardado no coincidia con `consulta.precio` mas la suma del detalle, y nadie se habia enterado en dos meses. Si empezara de nuevo haria una de dos cosas, y las dos son mas trabajo por adelantado y menos despues: o no guardar el total y derivarlo en una vista, o guardarlo y sostenerlo con un trigger que lo recalcule en cada cambio del detalle. Lo que **no** volveria a hacer es tener el mismo dato en dos sitios sin nada que los mantenga iguales. La correccion ya esta en `02_datos_semilla.sql`, donde el total sale de un `UPDATE` que lo calcula.

**Segunda, mas pequena y del mismo tipo:** nombraria las restricciones desde el primer dia. Un `CHECK` sin nombre produce un mensaje de error que depende de como el servidor lo genere, y por eso al principio la aplicacion mostraba el texto crudo del motor al usuario.

### 3. El concepto que mas me costo

**La concurrencia, y en particular por que un `SELECT COUNT(*)` no puede bloquear nada.** Venia de la Clase 8 con la idea de que una transaccion «protege» lo que lee, asi que no entendia como dos sesiones podian agendar la misma franja si las dos verificaban antes. Lo desatasque el dia que entendi que un bloqueo se pone sobre **filas que existen**, y la fila conflictiva todavia no existia cuando cada sesion hizo su conteo: no hay nada que bloquear. De ahi salio que la unica solucion real es un punto de serializacion **fisico** —el indice unico parcial `uq_cita_vet_franja`— y no una verificacion mas cuidadosa. Lo que **todavia** no tengo claro, y lo digo en vez de fingir: cuando conviene subir a `SERIALIZABLE` y pagar los reintentos del 40001, frente a resolverlo con una restriccion. Entiendo los dos mecanismos y no tengo criterio propio para elegir con volumen real.

### 4. De Oracle a PostgreSQL: tres diferencias que tuve que aprender

1. **`RAISE EXCEPTION 'texto %', var;` en lugar de `RAISE_APPLICATION_ERROR(-20001, 'texto')`.** No es solo otro nombre: en PostgreSQL no hay que administrar un rango de numeros de error propios, la interpolacion va con `%` y el codigo por omision es `P0001`. Importa porque todo el material de partida estaba escrito con la forma de Oracle y **no compila**: no da un aviso, no arranca.
2. **Un trigger son dos objetos: la funcion `RETURNS TRIGGER` y el `CREATE TRIGGER` que la asocia.** En Oracle el cuerpo va dentro del trigger y se usan `:NEW` y `:OLD`; aqui son `NEW` y `OLD` sin dos puntos, y la funcion se puede reutilizar en varias tablas. Importa porque el error tipico es escribir la logica dentro del `CREATE TRIGGER` y no entender por que no compila.
3. **`GET DIAGNOSTICS v_filas = ROW_COUNT;` en lugar de `SQL%ROWCOUNT`,** y junto con eso que `IF NOT FOUND` sirve despues de un `SELECT columna INTO` pero **nunca** despues de un `SELECT COUNT(*) INTO`, porque `COUNT` siempre devuelve una fila aunque valga 0. Importa porque es un error que **no falla**: el `IF` simplemente nunca se cumple y la validacion se cae en silencio, que es la peor clase de defecto.

Y una cuarta que no era de sintaxis sino de habito: no hay `DUAL`. `SELECT 1 + 1;` funciona sin `FROM`.

### 5. Lo que se queda sin verificar

- **La concurrencia real.** El entorno de practica es de **una sola sesion**, asi que nunca vi dos transacciones peleando por la misma franja: lo demostre con el indice unico, que es el control correcto, pero no con dos sesiones simultaneas. **Como lo verificaria:** dos clientes `psql` abiertos, `BEGIN` en los dos, el `INSERT` de la misma franja en ambos y observar que uno espera y despues recibe `23505`; y para el escenario de `SERIALIZABLE`, comprobar que el `40001` aparece **en el `COMMIT`** y que el reintento la resuelve.
- **Los privilegios con usuarios conectados de verdad.** Probé `app_vetcare` con `SET ROLE`, que es lo que el entorno permite y demostro lo importante —que sin `SECURITY DEFINER` la app no puede usar su propia API—, pero no con una conexion autenticada real. **Como lo verificaria:** crear el rol con `LOGIN` y contrasena, conectarme como el desde otro cliente e intentar el `INSERT` directo, revisando ademas `pg_hba.conf`.
- **El particionamiento.** Diseñé la particion por rango de `fecha_hora` y con ocho citas el planificador no tiene nada que podar. **Como lo verificaria:** cargar del orden de un millon de citas con `generate_series` y comprobar en el `EXPLAIN` que solo se leen las particiones del rango consultado.
- **El respaldo fisico, y es el que mas me pesa.** El guion de `pg_dump`/`pg_restore` esta escrito y **no lo he ejecutado**. Lo que si tengo es el respaldo logico con su trigger de archivo y su consulta de veredicto, y se exactamente por que no es suficiente: vive en la **misma** base. **Como lo verificaria:** `pg_dump` completo, `pg_restore` en una base vacia, correr encima la bateria de cinco pruebas de la Clase 11 y exigir el mismo resultado —incluido el `cumple = FALSE` de la prueba 5— y cronometrarlo para saber si el RTO de 4 horas que declare es real o es un deseo.

### 6. Nota que me pondria

**4,2 de 5.** El diseno esta completo, corre de cero y las tres reglas de negocio estan demostradas con salida verificable, no afirmadas. Lo que me impide ponerme mas es lo de arriba: el item mas importante del plan de respaldo sigue sin ensayar desde la Clase 11, y despues de estudiar un incidente que ocurrio exactamente por eso, mantenerlo abierto es una decision y no un descuido.

### Como calificar

- **2,5 pts — punto 1, con evidencia concreta.** El orgullo no se califica; la evidencia si. Valen una prueba que pasa con su mensaje, un tiempo o un plan que cambio, o un error que la base rechazo. «Estoy orgulloso de mi modelo, quedo bien normalizado» vale 0,5 de 2,5; «la prueba 2 intenta dejar el stock en -97 y el motor la rechaza con “violates check constraint ck_insumo_stock”» vale completo.
- **2,5 pts — punto 2, un cambio de diseno preciso.** El enunciado enumera lo que cuenta: un tipo de dato, una tabla que falta, una regla que quedo en la aplicacion y debio estar en la base, un indice que no servia. «Lo haria mejor» o «estudiaria mas» vale 0. Se reconoce como sobresaliente que el cambio salga de un hallazgo del propio semestre —las facturas descuadradas de la Clase 11, la funcion de solo lectura vulnerable de la Clase 13— porque demuestra que el hallazgo se convirtio en criterio.
- **2 pts — punto 3, el concepto dificil y **como** se desatasco.** El «como» es la mitad de la nota: nombrar el concepto sin contar que lo desbloqueo vale 1. **Y reconocer que algo sigue sin estar claro se premia, no se castiga:** vale los 2 pts completos si esta formulado con precision —«no tengo criterio para elegir entre `SERIALIZABLE` con reintentos y una restriccion unica»— porque eso es una duda tecnica util, y no lo vale un «no entendi las transacciones».
- **3 pts — punto 4, las tres diferencias PL/SQL → PL/pgSQL,** 1 pt cada una, y solo se otorga con el **por que importa**. Enumerar «`RAISE EXCEPTION` en vez de `RAISE_APPLICATION_ERROR`» vale 0,5; añadir que el material de partida no compila y hay que reescribirlo, vale 1. Diferencias que valen: el trigger como **dos** objetos y `NEW`/`OLD` sin dos puntos; `GET DIAGNOSTICS ... = ROW_COUNT` frente a `SQL%ROWCOUNT`; la ausencia de `DUAL`; `NUMERIC`/`TEXT` frente a `NUMBER`/`VARCHAR2`; los delimitadores `$$`; que no haya `/` de terminacion. Se reconoce como sobresaliente el `IF NOT FOUND` que **no** funciona tras un `SELECT COUNT(*) INTO`, porque es un defecto que no falla: la validacion se cae en silencio.
- **3 pts — punto 5, los limites del entorno y como verificarlos en produccion.** 1,5 pts identificar correctamente al menos dos —una sola sesion, asi que no hay concurrencia real; roles probados con `SET ROLE` y no con conexiones autenticadas; particionamiento sin volumen; respaldo fisico sin ensayar— y **1,5 pts el metodo concreto**, que es lo que separa una queja de un plan: dos clientes `psql` con `BEGIN` para ver el `23505`, un rol con `LOGIN` desde otra conexion, `generate_series` para el volumen, `pg_dump`/`pg_restore` con la bateria de la Clase 11 encima y cronometro. Un «no pude probar la concurrencia» sin metodo vale 0,5.
- **2 pts — punto 6, la autonota justificada,** 1 pt la nota y 1 pt que la justificacion sea coherente con el resto del documento. Cualquier nota es aceptable si se sostiene; lo que no se sostiene es un 5,0 despues de declarar cuatro cosas sin verificar, ni un 3,0 despues de entregar un script que corre completo. En equipo autorizado, la linea con la nota al aporte de cada integrante es obligatoria.
- **Criterio transversal, y es el que decide la nota:** esta pregunta se califica por **especificidad**, no por longitud ni por autocritica. Media pagina de humildad general vale menos que cuatro lineas que nombran un `CHECK`, una consulta y un numero. La honestidad tampoco es un adorno: una autoevaluacion que contradice el acta —«todo verificado» aqui y un item en `NO` alla— pierde puntos en las dos preguntas.

### Errores frecuentes y que hacer

- **Generalidades en el punto 1:** «me gusto como quedo el modelo», «aprendi mucho». La pregunta pide evidencia, y evidencia es una prueba, un mensaje de error, un tiempo o un plan de ejecucion. Sin numero ni salida, no hay punto.
- **Un punto 2 que es un proposito y no un cambio de diseno:** «estudiaria mas», «empezaria antes», «organizaria mejor mi tiempo». Puede ser cierto y no es lo que se pregunta. Lo que se pide es una decision tecnica concreta que hoy se tomaria distinta.
- **Fingir que todo quedo claro en el punto 3.** Es el error mas costoso porque el enunciado dice explicitamente lo contrario —«reconocerlo vale mas que fingir»— y porque una duda bien formulada demuestra mas dominio que una seguridad vaga. Lo que no vale es la version generica: «no entendi las transacciones».
- **Un punto 4 que solo enumera.** Tres pares de terminos sin el «por que importa» valen la mitad. La consecuencia practica es la respuesta: el material heredado **no compila**, y hay defectos —como el `IF NOT FOUND` tras un `COUNT(*)`— que no fallan y por eso se cuelan.
- **Confundir en el punto 5 lo que no se probo con lo que no se hizo.** «No implemente particionamiento» es una tarea pendiente; «diseñe la particion y con ocho filas el planificador no tiene nada que podar» es un limite del entorno, que es lo que se pregunta. Y en los dos casos falta la mitad que mas vale: **como** se verificaria.
- **Ponerse 5,0 despues de declarar cuatro cosas sin verificar,** o castigarse con un 3,0 tras entregar un script que corre completo y demuestra las tres reglas. Las dos son incoherentes con el propio documento, y la coherencia es justo lo que se califica.
- **Escribir una autoevaluacion que contradice el acta de la pregunta 4:** «todo quedo verificado» aqui y el item 12 del checklist en `NO` alla. Es la misma afirmacion sin comprobar del caso de la Clase 13, cometida en el ultimo documento del semestre.

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**¿Cuando tengo que entregar esto, si el 2026-11-16 es la sustentacion?**

**Antes** de tu turno. El bloque del 2026-11-16 se consume en las presentaciones, asi que no hay tiempo de aula para escribir el script maestro, y el 2026-11-09 es el Parcial 3. En la practica el taller se publica con el de la Clase 13 —el 2026-11-02— y la ventana util es esa semana y la siguiente. Si llegas a tu turno sin haber entregado, sustentas sobre un paquete que nadie pudo revisar, y eso se nota en la ronda de preguntas.

**Mi script falla a la mitad y no se donde. ¿Como lo depuro sin volverme loco?**

Lee el **primer** error, no el ultimo: en un script largo, un fallo temprano provoca una cascada de errores que no significan nada. Y las tres causas cubren casi todos los casos. Una: un `REFERENCES` a una tabla que se crea mas abajo —el DDL va en orden de dependencia, `dueno` antes de `mascota`, `cita` antes de `consulta`—. Dos: un `INSERT` que viola una FK por el mismo motivo. Tres: un `CREATE TRIGGER` antes de su funcion. Ejecutalo bloque por bloque hasta encontrar el que revienta, y despues **vuelve a correrlo completo de cero**: la base de ExamLab se vuelve a sembrar en cada intento, asi que puedes hacerlo tantas veces como quieras, y esa corrida limpia es la que se califica.

**Puse solo dos facturas como pide el enunciado y me falla el INSERT. ¿Por que?**

Por la cadena de dependencias, y es lo que rompe mas semillas. `factura.id_consulta` es `NOT NULL REFERENCES consulta`, asi que dos facturas necesitan **dos consultas**; y `consulta.id_cita` es **UNIQUE**, asi que esas dos consultas necesitan **dos citas distintas**, y con sentido, ambas `ATENDIDA`. Si tu semilla tiene una sola consulta, la segunda factura no tiene donde apoyarse. Revisa el orden completo: dueno → mascota → veterinario → cita → consulta → factura → detalle_factura.

**En la pregunta 2 mi consulta con JOIN normal da el mismo resultado que con LEFT JOIN. ¿Entonces da igual?**

No da igual, y que den lo mismo es precisamente el problema: **la semilla no ejerce el caso de borde.** Los cuatro veterinarios tienen citas y los seis insumos se han vendido, asi que la consulta correcta y la incorrecta son indistinguibles con estos datos. Creale el caso: `INSERT INTO veterinario (nombre, especialidad) VALUES ('Sara Quintero', 'Odontologia');` y un insumo nuevo sin ventas. Ahi veras que con `JOIN` interno desaparecen del reporte y con `LEFT JOIN` aparecen con ceros. Vale 4 de los 20 puntos de la pregunta, y es el habito que importa: un KPI que no se ha probado contra su caso de borde es una suposicion. La excepcion es K4, cuyo caso de borde si esta en los datos —dos de las cuatro citas de Ana Gomez no tienen consulta—.

**Los totales de las facturas no me cuadran con los detalles. ¿Esta mal la base?**

Los datos son los que son y tu observacion es correcta: **las tres facturas de la semilla estan descuadradas**, y no por poco. `factura.total` no coincide con `consulta.precio` mas la suma del detalle en ninguna de las tres. Es la misma inconsistencia que encontro la prueba 5 del taller de la Clase 11, y no es un error de tu consulta. K2 pide sumar `factura.total`, asi que suma eso. Lo que se premia es que lo digas: lleva a la sustentacion la tabla que compara el total guardado con el derivado y la conclusion, que es la de la Clase 11 —hay que elegir **una** definicion del total y hacerla cumplir con una restriccion o un trigger, porque el mismo dato en dos sitios sin nada que los mantenga iguales siempre termina divergiendo—.

**¿Puedo escribir la prueba 3 con el mismo molde que las dos primeras?**

No, y es el error mas comun del bloque 5. Las pruebas 1 y 2 son **negativas**: lo correcto es que revienten, y el `EXCEPTION` es lo que atrapa la prueba. La 3 es **positiva**: lo correcto es que ocurra un efecto —que `audit_cita` crezca—, y ahi un `EXCEPTION WHEN OTHERS` no prueba nada, porque el bloque no falla y el `RAISE NOTICE` imprimiria «OK» tambien con el trigger eliminado. Una prueba positiva **compara**: cuenta las filas antes, hace el `UPDATE`, cuenta despues y verifica que subio en 1. Ese `IF` es la prueba.

**¿Es obligatorio el trigger de auditoria si ya tengo la tabla `audit_cita`?**

Si, y son cosas distintas: la tabla es donde se guarda, el trigger es lo que garantiza que **siempre** se guarde sin que nadie tenga que acordarse. Si la bitacora la llena la aplicacion, solo queda traza de lo que pasa por la aplicacion. Dos detalles que cuestan puntos. Uno: en PostgreSQL son **dos objetos**, la funcion `RETURNS TRIGGER` y el `CREATE TRIGGER ... EXECUTE FUNCTION` que la asocia; escribir la logica dentro del `CREATE TRIGGER` no compila y es la herencia de Oracle que mas se repite. Dos: la verificacion esta en el inventario del bloque 6 —si `audit_cita` sale en **0**, el trigger no se disparo y tu prueba 3 no probo nada aunque haya impreso «OK»—.

**En la autoevaluacion, ¿me perjudica admitir que no ensaye el restore o que no entendi algo?**

Al contrario, y esto es en serio. El punto 5 **pide** lo que no pudiste verificar, y el punto 3 dice literalmente que reconocer una duda vale mas que fingir. Lo que perjudica es lo otro: declarar «todo verificado» cuando el checklist de la Clase 11 tiene el item del respaldo en `NO`, porque entonces hay dos entregables tuyos que se contradicen y el jurado lo va a encontrar. La diferencia entre una debilidad y un criterio esta en el metodo: no basta «no pude probar la concurrencia», hace falta «no pude, porque el entorno es de una sola sesion, y en produccion lo probaria con dos clientes `psql`, `BEGIN` en los dos y el mismo `INSERT`, esperando ver el `23505`». Eso no es una excusa: es la unica prueba que falta, y ya sabes escribirla.

---

## Cierre de la clase

- Al terminar, cada estudiante debe tener entregado: el **script maestro** con sus siete bloques corriendo de cero sin un solo error, las tres pruebas de aceptacion imprimiendo `OK` y el inventario cerrando en `5 | 3 | 8 | 8 | 2 | 4 | 2 | 4 | 1`; los **cuatro KPIs** con sus numeros —178.200,00 en septiembre, las 4 filas de la ficha de Ana Gomez, el 50,0 % de Paula Salazar y la fila del insumo nunca vendido—; las **cuatro opciones correctas** del checklist del ZIP; el **acta** con inventario, trazabilidad de las once clases y un guion de entre 5 y 8 minutos; y la **autoevaluacion** con las tres diferencias PL/SQL → PL/pgSQL y la lista de lo que no se pudo verificar.
- Cinco comprobaciones antes de subir el ZIP, todas de mirar un numero o abrir un archivo. Que el script maestro corra **de cero y de una sola vez**, sin comentar nada —la base de ExamLab se vuelve a sembrar en cada intento, asi que no hay excusa para no haberlo probado—. Que las tres lineas del bloque 5 digan `OK` y ninguna diga `FALLO`, y que `audit_cita` salga en **1** y no en 0. Que en la pregunta 2 el reporte muestre **la fila con ceros** del veterinario sin citas y la del insumo sin ventas: si no estan, la consulta no se probo contra su caso de borde. Que cada archivo que nombra el acta **exista** en el ZIP, y que el ER coincida con el DDL. Y que el guion **sume** entre 5 y 8 minutos, contando la columna.
- Este taller cierra el semestre con la misma idea con la que se cerro la Clase 13, porque es la que atraviesa el curso: **una afirmacion no verificada no es un resultado.** «El script corre» se comprueba ejecutandolo de cero; «los datos cumplen los minimos» se comprueba con la consulta 6b; «la regla de negocio esta» se comprueba con una prueba que la viola a proposito y falla; «el KPI conserva los casos sin datos» se comprueba creando el caso; y «tengo respaldo» se comprueba restaurando. Lo que se lleva un estudiante de Bases de Datos II no es la sintaxis de PL/pgSQL —eso se busca— sino el reflejo de preguntarse **como se comprueba** antes de declarar algo hecho. En la sustentacion del **2026-11-16** eso se ve en treinta segundos: quien trae numeros propios y sabe cual le falta esta parado sobre su trabajo; quien trae adjetivos, sobre su memoria. Y de las dos cosas que este paquete deja abiertas —el restore sin ensayar y el particionamiento sin volumen—, la primera es la que hay que decir en voz alta antes de que la pregunten.

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. El motor de la plataforma es PostgreSQL (PGlite en el navegador), no Oracle.
