# Guia Docente — Parte Practica por Clase (Bases de Datos II, 2026-2)

> Cada clase = una practica con objetivo propio. La demo se apoya en un
> boceto de pizarra + un script SQL completo (con datos) para que usted lo
> ejecute en vivo **en la consola de ExamLab**, que corre PostgreSQL (PGlite)
> en el navegador: es el mismo motor donde se califica el taller, y varios de
> estos scripts son PL/pgSQL que Oracle Live SQL no compila. El taller y el
> quiz se entregan/presentan en ExamLab (`https://uniaj.examlab.workers.dev/`) — no es la
> plataforma oficial de la UNIAJC, pero es la que usamos para eso en este curso.

## Clase 1 — Revision BD I · Arranque VetCare DB

**Objetivo practico:** Arranque PI: dominio, alcance y borrador ER de VetCare DB
**Por que importa:** sin ER/alcance no hay base para procs ni seguridad.

**Demo en vivo:**
- Pizarra: ER minimo: Dueño —1:N→ Mascota —1:N→ Cita. Marcar PK subrayada y FK con flecha.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Revision BD I»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Revision BD I» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 1 · DDL minimo demo (DB Fiddle / PostgreSQL o MySQL)
-- Objetivo PI: dejar entidades base para el ER.

CREATE TABLE dueno (
  id_dueno INT PRIMARY KEY,
  nombre VARCHAR(80) NOT NULL,
  telefono VARCHAR(30),
  email VARCHAR(120)
);

CREATE TABLE mascota (
  id_mascota INT PRIMARY KEY,
  id_dueno INT NOT NULL REFERENCES dueno(id_dueno),
  nombre VARCHAR(60) NOT NULL,
  especie VARCHAR(40),
  activa CHAR(1) DEFAULT 'S' CHECK (activa IN ('S','N'))
);

CREATE TABLE cita (
  id_cita INT PRIMARY KEY,
  id_mascota INT NOT NULL REFERENCES mascota(id_mascota),
  fecha_hora TIMESTAMP NOT NULL,
  estado VARCHAR(20) DEFAULT 'PROGRAMADA'
);

INSERT INTO dueno VALUES (1, 'Ana Perez', '3001112233', 'ana@mail.com');
INSERT INTO mascota VALUES (10, 1, 'Luna', 'Canino', 'S');
INSERT INTO cita VALUES (100, 10, '2026-09-01 09:00:00', 'PROGRAMADA');
SELECT m.nombre, d.nombre AS dueno, c.fecha_hora
FROM cita c JOIN mascota m ON m.id_mascota=c.id_mascota
JOIN dueno d ON d.id_dueno=m.id_dueno;
```

**Pasos guiados del taller:**
1. Registrar el proyecto con el nombre exacto VetCare - [Apellido] (trabajo individual por defecto; equipo de 2-3 solo si el docente lo autoriza).
2. Llenar la plantilla de la ficha del PI: alcance SI / alcance NO y 3 reglas de negocio propias en formato Condicion -> Accion.
3. Dibujar el ER borrador en Excalidraw o draw.io, pasarlo a Mermaid (erDiagram) con ayuda de una IA y pegarlo renderizado en ExamLab.
4. Exportar tambien el PNG del ER a la carpeta del PI y verificar que los nombres coincidan con el DDL (minusculas, singular, id_<entidad>).

**Entregable:** Ficha del PI (plantilla) + ER en Mermaid renderizado en ExamLab (PNG para tu carpeta) + 3 reglas Condicion -> Accion
**Criterios de exito:**
- Proyecto nombrado y registrado.
- ER PNG con entidades mínimas.
- 3 reglas de negocio propias.
- Alcance SI/NO 5-8 lineas.
- Entrega domingo 23:59.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 1/Quiz Clase 1 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 2 — Administracion de BD · Roles VetCare

**Objetivo practico:** Plan de roles/privilegios de VetCare
**Por que importa:** la seguridad de VetCare DB es un criterio de la rúbrica, y la evidencia son los roles y su matriz — no una promesa.

**Demo en vivo:**
- Pizarra: Tabla simple 3 columnas: Rol | Objeto | Privilegio (llenar en vivo con los 4 roles del taller).
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Administracion de BD»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Administracion de BD» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 2 · Roles y privilegios · PostgreSQL
-- Este es el script de la DEMO: corre tal cual en ExamLab (PostgreSQL en el
-- navegador), sobre el esquema de VetCare ya creado. Los nombres de rol son los
-- mismos que pide el taller: minusculas, y el del veterinario con sufijo `_rol`
-- porque `veterinario` ya es una tabla.
--
-- Se ejecuta de arriba abajo, narrando cada bloque. El bloque 5 es el que convence
-- al grupo: es la unica parte donde se VE que un permiso negado detiene una
-- sentencia — y por eso mismo va SENTENCIA POR SENTENCIA, no de un solo tiro: dos
-- de sus lineas tienen que fallar, y un runner que aborta al primer error se
-- llevaria las siguientes. Correr el script completo una vez antes de la clase.

-- ============ 1) Los cuatro roles ============
-- NOLOGIN: son paquetes de privilegios, no cuentas con las que alguien entra.
-- Una persona recibe el rol despues, con GRANT recepcion TO ana_gomez.
CREATE ROLE admin_bd NOLOGIN;
CREATE ROLE recepcion NOLOGIN;
CREATE ROLE veterinario_rol NOLOGIN;
CREATE ROLE auditor NOLOGIN;

-- ============ 2) Los privilegios, uno por uno ============
-- admin_bd es el unico con privilegios amplios, y sobre las 8 tablas.
GRANT ALL PRIVILEGES ON dueno, mascota, veterinario, cita,
                        consulta, insumo, factura, detalle_factura TO admin_bd;

-- recepcion opera citas y solo LEE los datos con que identifica a quien llama.
GRANT SELECT, INSERT, UPDATE ON cita TO recepcion;
GRANT SELECT ON dueno, mascota, veterinario TO recepcion;

-- veterinario_rol registra la consulta; la cita y la mascota solo las lee.
GRANT SELECT ON cita, mascota TO veterinario_rol;
GRANT SELECT, INSERT, UPDATE ON consulta TO veterinario_rol;

-- auditor verifica: solo lectura, sobre todo lo sensible.
GRANT SELECT ON dueno, mascota, cita, consulta, factura TO auditor;

-- El REVOKE se deja escrito aunque sea redundante (nunca se otorgo DELETE):
-- es la evidencia de una decision de diseno, no una correccion.
REVOKE DELETE ON cita FROM recepcion;

-- ============ 3) La matriz sale del motor, no del documento ============
SELECT grantee, table_name, privilege_type
FROM information_schema.role_table_grants
WHERE grantee IN ('admin_bd', 'recepcion', 'veterinario_rol', 'auditor')
ORDER BY grantee, table_name, privilege_type;

-- ============ 4) Cuando el GRANT es demasiado ============
-- La vista recorta filas (las canceladas) y columnas (el email nunca sale).
-- Se ejecuta con los privilegios de SU PROPIETARIO: por eso recepcion puede
-- consultarla aunque le quitemos el SELECT sobre la tabla dueno.
CREATE VIEW v_agenda_recepcion AS
SELECT c.id_cita, c.fecha_hora, c.estado,
       m.nombre AS mascota, d.nombre AS dueno, d.telefono,
       v.nombre AS veterinario
FROM cita c
JOIN mascota m     ON m.id_mascota = c.id_mascota
JOIN dueno d       ON d.id_dueno = m.id_dueno
JOIN veterinario v ON v.id_veterinario = c.id_veterinario
WHERE c.estado <> 'CANCELADA';

GRANT SELECT ON v_agenda_recepcion TO recepcion;
REVOKE SELECT ON dueno FROM recepcion;   -- ahora solo llega por la vista

-- Privilegio por columna: dos columnas y ninguna otra, sin crear objeto nuevo.
GRANT SELECT (id_dueno, nombre) ON dueno TO veterinario_rol;

-- Evidencia: tiene que devolver EXACTAMENTE dos filas (id_dueno y nombre).
SELECT grantee, table_name, column_name, privilege_type
FROM information_schema.column_privileges
WHERE grantee = 'veterinario_rol' AND table_name = 'dueno'
ORDER BY column_name;

-- ============ 5) La prueba negativa: ver el permiso NEGADO ============
-- No hay una segunda conexion (el entorno tiene un solo usuario con login), pero
-- no hace falta: SET ROLE cambia el rol efectivo DENTRO de la misma sesion, y a
-- partir de ahi los permisos que se revisan son los del rol, no los del dueno.
SET ROLE recepcion;

SELECT id_cita, fecha_hora, dueno FROM v_agenda_recepcion;  -- OK: la vista si
SELECT nombre, email FROM dueno;   -- debe fallar: permission denied for table dueno
DELETE FROM cita WHERE id_cita = 1;  -- debe fallar: permission denied for table cita

RESET ROLE;   -- volver al propietario ANTES de seguir con cualquier otra cosa

-- Si su entorno no permite SET ROLE, no lo esconda: dejelo en pantalla, diga que
-- eso vuelve la prueba negativa una brecha de verificacion del entregable, y
-- muestre cual seria el comando en un servidor real.

-- ============ 6) Ciclo de vida, para la politica ============
-- Alta:   GRANT recepcion TO ana_gomez;
-- Cambio: GRANT veterinario_rol TO ana_gomez; REVOKE recepcion FROM ana_gomez;
--         (los dos, siempre: los permisos NO se acumulan)
-- Baja:   REASSIGN OWNED BY ana_gomez TO admin_bd;  -- antes de borrar el rol
--         DROP ROLE ana_gomez;                      -- falla si todavia posee objetos
```

**Pasos guiados del taller:**
1. Crear los 4 roles (admin_bd, recepcion, veterinario_rol, auditor) con GRANT/REVOKE que corran.
2. Recortar la superficie: vista v_agenda_recepcion + privilegio por columna sobre dueno.
3. Matriz rol x objeto x privilegio de los 10 objetos, justificando privilegio minimo.
4. Redactar 1 pagina: politica de altas/bajas de usuarios, con la prueba negativa (SET ROLE) corrida y su mensaje de error.

**Entregable:** Documento Roles_VetCare + script GRANT/REVOKE ejecutado en ExamLab
**Criterios de exito:**
- Los 4 roles creados, con sus GRANT y el REVOKE explícito de DELETE.
- La matriz real consultada con `information_schema.role_table_grants`.
- Vista `v_agenda_recepcion` sin el email + `GRANT SELECT (id_dueno, nombre)`.
- Matriz de 10 objetos x 4 roles, sin celdas vacías y consistente con los GRANT.
- Política de 1 página con las 5 secciones, cada una con responsable y plazo.
- Entrega domingo 23:59.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 2/Quiz Clase 2 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 3 — Procedimientos almacenados · VetCare

**Objetivo practico:** >=1 procedimiento de negocio (agendar cita / registrar consulta)
**Por que importa:** la regla de negocio deja de vivir en la pantalla y queda dentro de la base, donde vale para cualquier cliente que se conecte.

**Demo en vivo:**
- Pizarra: Flujo: App → llama sp_agendar_cita → valida mascota.activa → INSERT o mensaje de error.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Procedimientos almacenados»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Procedimientos almacenados» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 3 · Procedimientos almacenados · PostgreSQL
-- Script de la DEMO: corre tal cual en ExamLab (PostgreSQL/PGlite en el navegador),
-- sobre el esquema de VetCare ya creado y poblado: 8 mascotas (Rocky=3 y Kiara=8
-- estan INACTIVAS), 4 veterinarios, 10 citas, y una cita del veterinario 1 el
-- 2026-09-01 08:00:00.
--
-- NO es Oracle: nada de IS en vez de AS, VARCHAR2, NUMBER, RAISE_APPLICATION_ERROR
-- ni barra / de terminacion. Ese codigo aqui no compila, y es la forma mas facil de
-- perder los puntos de sintaxis de la pregunta 1.
--
-- Se ejecuta de arriba abajo narrando cada bloque. El bloque 3 es el que convence al
-- grupo: es donde se VE que la validacion detiene el INSERT. Correr el script
-- completo una vez antes de la clase.

-- ============ 1) El procedimiento con sus 3 validaciones ============
-- id_cita no se pasa como parametro: es SERIAL y lo genera el motor.
CREATE OR REPLACE PROCEDURE sp_agendar_cita(
  p_id_mascota     INT,
  p_id_veterinario INT,
  p_fecha_hora     TIMESTAMP
)
LANGUAGE plpgsql
AS $proc$
DECLARE
  v_activa CHAR(1);
BEGIN
  -- Validacion 1: la mascota existe. SELECT ... INTO deja FOUND en FALSE cuando no
  -- devolvio ninguna fila, y eso es lo que pregunta IF NOT FOUND.
  SELECT activa INTO v_activa
    FROM mascota
   WHERE id_mascota = p_id_mascota;

  IF NOT FOUND THEN
    RAISE EXCEPTION 'ERROR: la mascota % no existe', p_id_mascota;
  END IF;

  -- Validacion 2: la regla de negocio del PI.
  IF v_activa <> 'S' THEN
    RAISE EXCEPTION 'ERROR: la mascota % esta inactiva; no se agenda cita',
                    p_id_mascota;
  END IF;

  -- Validacion 3: la franja del veterinario esta libre. Una cita CANCELADA libera
  -- la franja, asi que no cuenta.
  IF EXISTS (SELECT 1 FROM cita
              WHERE id_veterinario = p_id_veterinario
                AND fecha_hora     = p_fecha_hora
                AND estado <> 'CANCELADA') THEN
    RAISE EXCEPTION 'ERROR: el veterinario % ya tiene cita en %',
                    p_id_veterinario, p_fecha_hora;
  END IF;

  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
  VALUES (p_id_mascota, p_id_veterinario, p_fecha_hora, 'PROGRAMADA');
END;
$proc$;

-- ============ 2) El caso valido ============
CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');

SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado
  FROM cita ORDER BY id_cita DESC LIMIT 3;   -- la nueva es la primera fila

-- ============ 3) Los tres errores, SENTENCIA POR SENTENCIA ============
-- Estas tres lineas DEBEN fallar, y por eso no van en un solo tiro: la gracia es
-- leer en pantalla el mensaje exacto que la app va a recibir. Un runner que aborta
-- al primer error se llevaria las siguientes.
CALL sp_agendar_cita(3,  2, TIMESTAMP '2026-09-21 08:00:00');  -- Rocky, INACTIVA
CALL sp_agendar_cita(99, 2, TIMESTAMP '2026-09-22 08:00:00');  -- no existe
CALL sp_agendar_cita(2,  1, TIMESTAMP '2026-09-01 08:00:00');  -- franja ocupada

-- Y la prueba de que no dejaron basura: sigue habiendo 11 citas, no 14.
SELECT COUNT(*) AS citas_totales FROM cita;

-- ============ 4) La bateria: un bloque DO por caso ============
-- Por que un bloque por caso: si los CALL van seguidos, el primero que falla aborta
-- el resto. DO es un bloque anonimo -- se ejecuta una vez y no se guarda -- y su
-- EXCEPTION atrapa el error y deja seguir al caso siguiente.
CREATE TABLE IF NOT EXISTS resultado_prueba (
  id_prueba SERIAL PRIMARY KEY,
  caso      TEXT,
  esperado  TEXT,
  obtenido  TEXT,
  paso      BOOLEAN
);

-- Caso POSITIVO: el exito es que NO haya excepcion.
DO $$
BEGIN
  CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-20 08:00:00');
  INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
  VALUES ('P1 mascota activa', 'OK: cita creada', 'OK: cita creada', TRUE);
EXCEPTION WHEN OTHERS THEN
  INSERT INTO resultado_prueba (caso, esperado, obtenido, paso)
  VALUES ('P1 mascota activa', 'OK: cita creada', SQLERRM, FALSE);
END $$;

-- Caso NEGATIVO: el exito es que SI haya excepcion, y ademas que sea LA esperada.
-- Por eso se verifica el TEXTO con ILIKE y no basta WHEN OTHERS a secas: un typo en
-- el nombre de una columna tambien lanza excepcion, y un WHEN OTHERS pelado lo
-- reportaria como prueba superada.
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

SELECT caso, esperado, obtenido, paso
  FROM resultado_prueba ORDER BY id_prueba;

-- Nota de lectura: aqui `paso` significa «el resultado coincidio con lo esperado»,
-- asi que las dos filas quedan en t. La otra lectura -- «la operacion se completo»,
-- que deja las negativas en f -- tambien es valida. Lo que hay que hacer es usar UNA
-- de las dos para las cuatro filas y decir cual, porque si no, `paso` no significa
-- nada.

-- ============ 5) El contrato, que es el otro entregable ============
-- Firma        : sp_agendar_cita(p_id_mascota INT, p_id_veterinario INT,
--                               p_fecha_hora TIMESTAMP)
-- Llamada      : CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00');
-- Precondicion : la mascota existe y tiene activa = 'S'; la franja del veterinario
--                esta libre (una cita CANCELADA no la ocupa).
-- Postcondicion: 1 fila nueva en cita con estado 'PROGRAMADA'. Si falla, NINGUNA.
-- Errores      : 'ERROR: la mascota % no existe'
--                'ERROR: la mascota % esta inactiva; no se agenda cita'
--                'ERROR: el veterinario % ya tiene cita en %'
-- Decision     : se aborta con RAISE EXCEPTION en vez de devolver un codigo en un
--                parametro OUT, porque abortar deshace lo hecho; un codigo que
--                nadie revise deja la cita creada igual.
```

**Pasos guiados del taller:**
1. Escribir sp_agendar_cita en PL/pgSQL y ejecutarlo en ExamLab (LANGUAGE plpgsql, dollar-quoting, sin sintaxis de Oracle).
2. Incluir las 3 validaciones de negocio del PI, cada una con su RAISE EXCEPTION y su mensaje literal.
3. Correr la bateria de pruebas con bloques DO: 1 caso OK + 3 casos error, escritos en resultado_prueba, mas el COUNT(*) de cita antes y despues.
4. Escribir sp_registrar_consulta, comprobando con EXISTS antes de chocar contra la restriccion UNIQUE.
5. Redactar el contrato del proc en sus 6 bloques (plantilla en este documento) y pegarlo en la pregunta 5.

**Entregable:** 2 procedimientos en PL/pgSQL corriendo en ExamLab + bateria de pruebas con su tabla resultado_prueba + contrato del proc (6 bloques)
**Criterios de exito:**
- `sp_agendar_cita` con sus 3 parámetros y sus 3 validaciones, cada una con su `RAISE EXCEPTION` y su mensaje literal.
- Batería de 4 bloques `DO` que @@no aborta el script@@ y escribe 4 filas en `resultado_prueba` con el `SQLERRM` real.
- El `COUNT(*)` de `cita` demuestra que pasó de @@10 a 11@@ filas: las tres validaciones no insertaron nada.
- `sp_registrar_consulta` detectando la consulta duplicada con `EXISTS` @@antes@@ de chocar contra el `UNIQUE`.
- Contrato de los dos procedimientos con sus 6 bloques y la tabla de errores completa (7 filas); las firmas coinciden con el código entregado.
- Entrega domingo 23:59.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 3/Quiz Clase 3 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 4 — Funciones · Triggers · Seguridad y respaldo

**Objetivo practico:** >=1 funcion + >=1 trigger + borrador plan de respaldo
**Por que importa:** integridad y trazabilidad son criterios de la rúbrica, y la evidencia son el trigger corriendo y la fila de auditoría — no una promesa.

**Demo en vivo:**
- Pizarra: Mismo ER de Clase 1 + una nota junto a Cita: 'AQUI dispara el trigger de auditoria' y junto a Mascota: 'AQUI vive la fn_precio_base'.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Funciones»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Funciones» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 4 · Funcion, triggers y respaldo · PostgreSQL
-- Script de la DEMO: corre tal cual en ExamLab (PostgreSQL/PGlite en el navegador).
--
-- En PostgreSQL el trigger son SIEMPRE dos objetos: una funcion que RETURNS TRIGGER
-- y un CREATE TRIGGER que dice cuando dispararla. No existe el trigger con el cuerpo
-- adentro que se escribe en Oracle, ni los dos puntos de :NEW y :OLD, ni
-- RAISE_APPLICATION_ERROR. Eso aqui no compila y la rubrica lo descuenta.

-- ============ 1) La funcion de precio ============
-- IMMUTABLE: para los mismos argumentos siempre devuelve lo mismo y no lee tablas.
-- COALESCE porque la app puede mandar NULL en la casilla de urgencia, y NULL * 1.35
-- es NULL: la factura saldria vacia en vez de salir mal, que es peor.
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
BEGIN
  v_base := CASE UPPER(p_especie)
              WHEN 'CANINO' THEN 45000
              WHEN 'FELINO' THEN 40000
              ELSE 35000
            END;
  IF COALESCE(p_urgencia, FALSE) THEN
    v_base := v_base * 1.35;
  END IF;
  RETURN v_base;
END;
$fn$;

-- Una funcion se llama con SELECT, no con CALL. Es la diferencia con la Clase 3.
SELECT fn_precio_consulta('Canino', FALSE) AS normal,     -- 45000
       fn_precio_consulta('Canino', TRUE)  AS urgencia,   -- 60750
       fn_precio_consulta('canino', TRUE)  AS minusculas, -- 60750, por UPPER()
       fn_precio_consulta('Conejo', FALSE) AS otra_especie, -- 35000
       fn_precio_consulta('Felino', NULL)  AS urgencia_nula; -- 40000, por COALESCE

-- Y donde se usa de verdad: junto a la tabla, como una columna calculada.
SELECT m.nombre, m.especie,
       fn_precio_consulta(m.especie, FALSE) AS precio_normal,
       fn_precio_consulta(m.especie, TRUE)  AS precio_urgencia
  FROM mascota m
 WHERE m.id_mascota IN (1, 4)
 ORDER BY m.id_mascota;

-- ============ 2) Trigger de auditoria: los DOS objetos ============
CREATE TABLE IF NOT EXISTS audit_cita (
  id_audit        SERIAL PRIMARY KEY,
  id_cita         INT  NOT NULL,
  accion          TEXT NOT NULL,
  valor_anterior  TEXT,
  valor_nuevo     TEXT,
  usuario_bd      TEXT      DEFAULT current_user,
  fecha_evento    TIMESTAMP DEFAULT now()
);

-- Objeto 1: la funcion. NEW y OLD sin dos puntos, y RETURN NEW obligatorio.
CREATE OR REPLACE FUNCTION fn_trg_audit_cita()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $fn$
BEGIN
  INSERT INTO audit_cita (id_cita, accion, valor_anterior, valor_nuevo)
  VALUES (NEW.id_cita, 'CAMBIO_ESTADO', OLD.estado, NEW.estado);
  RETURN NEW;   -- quien y cuando los pone los DEFAULT de la tabla
END;
$fn$;

-- Objeto 2: la asociacion. AFTER porque solo se registra lo que ya paso.
DROP TRIGGER IF EXISTS trg_audit_cita ON cita;
CREATE TRIGGER trg_audit_cita
AFTER UPDATE OF estado ON cita
FOR EACH ROW
WHEN (OLD.estado IS DISTINCT FROM NEW.estado)
EXECUTE FUNCTION fn_trg_audit_cita();

-- La prueba: TRES updates que dejan DOS filas de auditoria.
UPDATE cita SET estado = 'CANCELADA'  WHERE id_cita = 1;  -- cambia  -> audita
UPDATE cita SET estado = 'ATENDIDA'   WHERE id_cita = 3;  -- cambia  -> audita
UPDATE cita SET estado = 'PROGRAMADA' WHERE id_cita = 6;  -- ya era  -> NO audita

SELECT id_audit, id_cita, accion, valor_anterior, valor_nuevo, usuario_bd
  FROM audit_cita ORDER BY id_audit;   -- 2 filas: citas 1 y 3

-- El WHEN es lo que hace la diferencia. Sin el, la tercera fila tambien se escribe y
-- la auditoria se llena de eventos donde no cambio nada. Con IS DISTINCT FROM y no
-- con <> porque <> devuelve NULL si un lado es NULL, y un WHEN que da NULL no
-- dispara: un estado que pasa de NULL a 'PROGRAMADA' se quedaria sin auditar.

-- ============ 3) Trigger que IMPIDE: stock negativo ============
-- El CHECK de la tabla se retira a proposito para mostrar el hueco que tapa el
-- trigger. Un CHECK vigila el valor final de UNA fila; el trigger, ademas, puede
-- mirar el valor anterior y decidir con la fila completa.
ALTER TABLE insumo DROP CONSTRAINT IF EXISTS insumo_stock_check;

-- Sin defensa: el insumo 2 (Vacuna triple felina) tiene 3 unidades.
UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2;
SELECT id_insumo, nombre, stock FROM insumo WHERE id_insumo = 2;   -- stock = -7 (!)
UPDATE insumo SET stock = 3 WHERE id_insumo = 2;                   -- se restaura

CREATE OR REPLACE FUNCTION fn_trg_stock_no_negativo()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $fn$
BEGIN
  IF NEW.stock < 0 THEN
    RAISE EXCEPTION 'ERROR: el stock de % no puede quedar negativo (resultado: %)',
                    OLD.nombre, NEW.stock;
  END IF;
  RETURN NEW;   -- BEFORE: lo que se retorna es lo que se guarda
END;
$fn$;

-- BEFORE, no AFTER: la unica forma de impedir el cambio es correr antes de que se
-- escriba. Un AFTER que lanza excepcion tambien deshace la transaccion, pero para
-- cuando corre el motor ya hizo el trabajo -- y con AFTER no se puede corregir el
-- valor, solo abortar.
DROP TRIGGER IF EXISTS trg_stock_no_negativo ON insumo;
CREATE TRIGGER trg_stock_no_negativo
BEFORE UPDATE OF stock ON insumo
FOR EACH ROW
EXECUTE FUNCTION fn_trg_stock_no_negativo();

-- Con defensa: el mismo UPDATE, ahora rechazado. RAISE NOTICE imprime el mensaje sin
-- abortar el bloque, para que el grupo lea la excepcion en pantalla.
DO $$
BEGIN
  UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2;
  RAISE NOTICE 'FALLO LA PRUEBA: el UPDATE paso y no debia';
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'RECHAZADO (correcto): %', SQLERRM;
END $$;

-- Y el descuento legitimo sigue funcionando: no se bloqueo la operacion, se bloqueo
-- el resultado invalido.
DO $$
BEGIN
  UPDATE insumo SET stock = stock - 2 WHERE id_insumo = 2;
  RAISE NOTICE 'ACEPTADO (correcto): quedan 1 unidades';
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'FALLO LA PRUEBA: %', SQLERRM;
END $$;

SELECT id_insumo, nombre, stock FROM insumo WHERE id_insumo = 2;   -- stock = 1

-- ============ 4) El respaldo: las herramientas reales ============
-- Estos comandos NO corren dentro de ExamLab -- son de linea de comandos, no SQL --
-- pero son los que hay que nombrar en el plan. Se proyectan como referencia.
--
--   pg_dump -Fc -d vetcare -f vetcare_2026-09-15.dump   respaldo logico de LA base
--   pg_dumpall --globals-only -f roles.sql              roles y privilegios: pg_dump
--                                                       NO los incluye
--   pg_basebackup -D /backup/base -Ft -z                copia fisica del cluster
--   pg_restore -d vetcare_prueba vetcare_2026-09-15.dump   el ensayo de restauracion
--
-- La consulta de validacion despues de restaurar, que es lo que convierte «restaure»
-- en «restaure bien»:
--   SELECT (SELECT COUNT(*) FROM cita)     AS citas,
--          (SELECT COUNT(*) FROM consulta) AS consultas,
--          (SELECT COUNT(*) FROM factura)  AS facturas,
--          (SELECT MAX(fecha_hora) FROM cita) AS ultima_cita;
--
-- Y el esqueleto del plan (1 pagina, en Google Docs): 1) que se respalda y con que
-- herramienta cada cosa · 2) frecuencia y ventana, justificada contra el horario
-- lunes-sabado 7:00-19:00 · 3) retencion, en >=2 ubicaciones · 4) RPO y RTO con su
-- justificacion por impacto · 5) el ensayo de restauracion: cada cuanto, la consulta
-- de validacion y quien firma · 6) que NO cubre este plan y cual es el riesgo
-- residual que se asume.
```

**Pasos guiados del taller:**
1. Escribir fn_precio_consulta(especie, urgencia) RETURNS NUMERIC en PL/pgSQL y probarla con SELECT sobre las 3 especies.
2. Crear la tabla audit_cita y el trigger de auditoria en sus dos objetos: fn_trg_audit_cita() RETURNS TRIGGER + CREATE TRIGGER ... EXECUTE FUNCTION.
3. Crear el trigger de stock no negativo (BEFORE UPDATE), evidenciando primero que sin el el stock llega a -7.
4. Decidir donde vive cada validacion: CHECK, trigger o aplicacion (pregunta 4).
5. Redactar Plan_Backup_VetCare con sus 6 secciones (plantilla en este documento): que se respalda y con que, frecuencia, retencion, RPO/RTO, restore de prueba con quien firma, y que NO cubre el plan.

**Entregable:** fn_precio_consulta + 2 triggers corriendo en ExamLab + Plan_Backup_VetCare con sus 6 secciones (1 pag.)
**Criterios de exito:**
- `fn_precio_consulta` con `RETURNS NUMERIC`, `IMMUTABLE`, insensible a mayúsculas, recargo del 35 % y `NULL` tratado como falso (45000 → @@60750@@).
- El trigger de auditoría en sus @@dos objetos@@: `fn_trg_audit_cita() RETURNS TRIGGER` + `CREATE TRIGGER ... EXECUTE FUNCTION`. Cero `:NEW` / `:OLD`.
- Los 3 `UPDATE` dejan @@2 filas@@ en `audit_cita` y el estudiante explica por qué la tercera no se auditó.
- El stock negativo (@@-7@@) evidenciado @@antes@@ del trigger, y el trigger `BEFORE UPDATE` con el mensaje literal de la rúbrica.
- `Plan_Backup_VetCare` con las 6 secciones, RPO y RTO justificados contra el horario de la clínica, y la consulta de validación post-restore.
- Entrega domingo 23:59.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 4/Quiz Clase 4 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 6 — Optimizacion de consultas · VetCare

**Objetivo practico:** Primera pareja de consultas antes/despues del PI
**Por que importa:** la rúbrica pide un análisis de plan de ejecución, y un análisis es un antes y un después medidos — no la frase «la optimicé».

**Demo en vivo:**
- Pizarra: Dos columnas: 'Antes' (consulta con SELECT * y JOIN sin filtro) vs 'Despues' (columnas puntuales + filtro temprano) sobre el mismo dibujo de tablas.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Optimizacion de consultas»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Optimizacion de consultas» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 6 · Optimizacion de consultas (demo del docente)
-- ============================================================================
-- Motor: PostgreSQL. Se corre en ExamLab (PGlite en el navegador), que es donde
-- se califica el taller. Es AUTOCONTENIDO: crea el esquema, siembra el volumen y
-- deja las estadisticas listas, igual que el `setup_sql` de las preguntas 1, 2 y 3.
-- Volumen resultante: 2.006 duenos · 5.008 mascotas · 16 veterinarios · 30.010 citas.
-- SIN indices adicionales: crearlos es la Clase 7, y por eso hoy la evidencia NO es
-- un cambio de Seq Scan a Index Scan sino menos filas y menos pasadas.
-- ============================================================================

DROP TABLE IF EXISTS cita, mascota, veterinario, dueno;

CREATE TABLE dueno (
  id_dueno SERIAL PRIMARY KEY,
  nombre   TEXT NOT NULL,
  telefono TEXT,
  email    TEXT,
  ciudad   TEXT DEFAULT 'Cali'
);
CREATE TABLE mascota (
  id_mascota SERIAL PRIMARY KEY,
  id_dueno   INT NOT NULL REFERENCES dueno(id_dueno),
  nombre     TEXT NOT NULL,
  especie    TEXT NOT NULL,
  fecha_nac  DATE,
  activa     CHAR(1) NOT NULL DEFAULT 'S' CHECK (activa IN ('S','N'))
);
CREATE TABLE veterinario (
  id_veterinario SERIAL PRIMARY KEY,
  nombre         TEXT NOT NULL,
  especialidad   TEXT,
  activo         CHAR(1) NOT NULL DEFAULT 'S' CHECK (activo IN ('S','N'))
);
CREATE TABLE cita (
  id_cita        SERIAL PRIMARY KEY,
  id_mascota     INT NOT NULL REFERENCES mascota(id_mascota),
  id_veterinario INT NOT NULL REFERENCES veterinario(id_veterinario),
  fecha_hora     TIMESTAMP NOT NULL,
  estado         TEXT NOT NULL DEFAULT 'PROGRAMADA'
                 CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))
);

-- Los 6 duenos, 4 veterinarios, 8 mascotas y 10 citas con nombre propio de VetCare.
INSERT INTO dueno (nombre) VALUES
  ('Ana Gomez'), ('Carlos Ruiz'), ('Marcela Diaz'),
  ('Jorge Pineda'), ('Luisa Cardona'), ('Andres Vallejo');
INSERT INTO veterinario (nombre, especialidad) VALUES
  ('Laura Restrepo','General'), ('Diego Moreno','Cirugia'),
  ('Paula Salazar','Dermatologia'), ('Ivan Ortiz','General');
INSERT INTO mascota (id_dueno, nombre, especie, activa) VALUES
  (1,'Firulais','Canino','S'), (1,'Luna','Felino','S'), (2,'Rocky','Canino','N'),
  (3,'Mishi','Felino','S'),    (3,'Bobby','Canino','S'), (4,'Nube','Felino','S'),
  (5,'Toby','Canino','S'),     (6,'Kiara','Canino','N');
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado) VALUES
  (1,1,TIMESTAMP '2026-09-01 08:00','PROGRAMADA'), (2,1,TIMESTAMP '2026-09-01 09:00','ATENDIDA'),
  (4,2,TIMESTAMP '2026-09-01 10:00','PROGRAMADA'), (5,3,TIMESTAMP '2026-09-02 08:30','CANCELADA'),
  (6,2,TIMESTAMP '2026-09-02 11:00','ATENDIDA'),   (7,4,TIMESTAMP '2026-09-03 07:45','PROGRAMADA'),
  (1,1,TIMESTAMP '2026-09-05 15:00','ATENDIDA'),   (2,3,TIMESTAMP '2026-09-08 16:00','PROGRAMADA'),
  (4,4,TIMESTAMP '2026-09-10 08:00','PROGRAMADA'), (6,1,TIMESTAMP '2026-09-10 09:00','ATENDIDA');

-- Volumen. Sin esto la demo no se puede hacer: con 10 citas todo cabe en una
-- pagina de 8 KB y no hay plan mas barato que leerla, asi que la consulta pesima
-- y la optima miden lo mismo y la diferencia se esconde en el ruido de medicion.
INSERT INTO dueno (nombre, telefono, email)
SELECT 'Dueno '||g, '300'||LPAD(g::text,7,'0'), 'dueno'||g||'@mail.com'
FROM generate_series(1,2000) AS g;                       -- duenos 7..2006

INSERT INTO veterinario (nombre, especialidad)
SELECT 'Veterinario '||g,
       CASE WHEN g%3=0 THEN 'Cirugia' WHEN g%3=1 THEN 'General' ELSE 'Dermatologia' END
FROM generate_series(1,12) AS g;                         -- veterinarios 5..16

INSERT INTO mascota (id_dueno, nombre, especie, activa)
SELECT 1+(g%2000), 'Mascota '||g,
       CASE WHEN g%2=0 THEN 'Canino' ELSE 'Felino' END,
       CASE WHEN g%17=0 THEN 'N' ELSE 'S' END
FROM generate_series(1,5000) AS g;                       -- mascotas 9..5008

INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
SELECT 1+(g%5000), 1+(g%12),
       TIMESTAMP '2026-01-05 08:00' + ((g%200)*INTERVAL '1 day')
                                    + ((g%9)*INTERVAL '45 minutes'),
       CASE WHEN g%11=0 THEN 'CANCELADA' WHEN g%3=0 THEN 'ATENDIDA' ELSE 'PROGRAMADA' END
FROM generate_series(1,30000) AS g;                      -- citas 11..30010

-- Sin ANALYZE el optimizador trabaja con estimaciones por omision y el «estimado
-- contra real» de la pregunta 2 sale disparatado por una razon que no es el tema.
ANALYZE dueno; ANALYZE mascota; ANALYZE veterinario; ANALYZE cita;

-- Cifras de control que conviene proyectar antes de empezar (200 dias × 150 citas):
--   30.010 citas · 150 el 2026-03-10 · de esas 91 PROGRAMADA, 45 ATENDIDA, 14 CANCELADA.
SELECT COUNT(*) AS total_citas FROM cita;
SELECT estado, COUNT(*) FROM cita
WHERE fecha_hora >= TIMESTAMP '2026-03-10' AND fecha_hora < TIMESTAMP '2026-03-11'
GROUP BY estado ORDER BY estado;

-- ============================================================================
-- BLOQUE 1 · La agenda del dia: los 4 antipatrones (pregunta 1 del taller)
-- ============================================================================

-- ANTES. Cuatro defectos: SELECT * · joins con coma · to_char() sobre la columna
-- · UPPER() sobre el estado. Devuelve 91 filas.
SELECT *
FROM cita c, mascota m, dueno d, veterinario v
WHERE c.id_mascota = m.id_mascota
  AND m.id_dueno = d.id_dueno
  AND c.id_veterinario = v.id_veterinario
  AND to_char(c.fecha_hora,'YYYY-MM-DD') = '2026-03-10'
  AND UPPER(c.estado) = 'PROGRAMADA';

-- DESPUES. Proyeccion de 6 columnas · JOIN ... ON · predicado de RANGO (sargable)
-- · comparacion directa del estado, que el CHECK ya normalizo. Tambien 91 filas.
SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno,
       v.nombre AS veterinario, c.estado
FROM cita c
JOIN mascota m     ON m.id_mascota = c.id_mascota
JOIN dueno d       ON d.id_dueno = m.id_dueno
JOIN veterinario v ON v.id_veterinario = c.id_veterinario
WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
  AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
  AND c.estado = 'PROGRAMADA'
ORDER BY c.fecha_hora;

-- La evidencia (pregunta 2). Se lee: nodo mas costoso, rows= estimadas frente a
-- actual rows=, y Execution Time. Ojo: `actual time` es POR VUELTA y el tiempo de
-- un nodo INCLUYE el de sus hijos.
EXPLAIN (ANALYZE, BUFFERS)
SELECT *
FROM cita c, mascota m, dueno d, veterinario v
WHERE c.id_mascota = m.id_mascota
  AND m.id_dueno = d.id_dueno
  AND c.id_veterinario = v.id_veterinario
  AND to_char(c.fecha_hora,'YYYY-MM-DD') = '2026-03-10'
  AND UPPER(c.estado) = 'PROGRAMADA';

EXPLAIN (ANALYZE, BUFFERS)
SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno,
       v.nombre AS veterinario, c.estado
FROM cita c
JOIN mascota m     ON m.id_mascota = c.id_mascota
JOIN dueno d       ON d.id_dueno = m.id_dueno
JOIN veterinario v ON v.id_veterinario = c.id_veterinario
WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
  AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
  AND c.estado = 'PROGRAMADA'
ORDER BY c.fecha_hora;

-- Lo que la pantalla de agenda realmente necesita. El LIMIT deja de leer en
-- cuanto tiene 50 filas: por eso baja el tiempo aunque el plan sea el mismo.
EXPLAIN ANALYZE
SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno,
       v.nombre AS veterinario, c.estado
FROM cita c
JOIN mascota m     ON m.id_mascota = c.id_mascota
JOIN dueno d       ON d.id_dueno = m.id_dueno
JOIN veterinario v ON v.id_veterinario = c.id_veterinario
WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
  AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
  AND c.estado = 'PROGRAMADA'
ORDER BY c.fecha_hora
LIMIT 50;

-- ============================================================================
-- BLOQUE 2 · La subconsulta correlacionada (pregunta 3 del taller)
-- ============================================================================

-- ANTES. La subconsulta esta en la LISTA DE COLUMNAS y menciona d.id_dueno, del
-- exterior: no se puede calcular una vez y reusar. El plan lo delata con un nodo
-- SubPlan y loops=2006 — un dueno, una ejecucion.
EXPLAIN ANALYZE
SELECT d.id_dueno, d.nombre,
       (SELECT COUNT(*) FROM cita c JOIN mascota m ON m.id_mascota = c.id_mascota
         WHERE m.id_dueno = d.id_dueno) AS total_citas
FROM dueno d
ORDER BY total_citas DESC;

-- DESPUES. Una sola pasada: el SubPlan desaparece y queda un HashAggregate.
-- COUNT(c.id_cita) y NO COUNT(*): el LEFT JOIN fabrica una fila de NULL por cada
-- dueno sin citas, y COUNT(*) cuenta filas, asi que reportaria 1 donde va 0.
-- Y LEFT y no INNER: el INNER es mas rapido y borra del ranking a los 6 duenos
-- sin mascotas (2001..2006). Mas rapido devolviendo otra cosa no es optimizar.
EXPLAIN ANALYZE
SELECT d.id_dueno, d.nombre, COUNT(c.id_cita) AS total_citas
FROM dueno d
LEFT JOIN mascota m ON m.id_dueno = d.id_dueno
LEFT JOIN cita c    ON c.id_mascota = m.id_mascota
GROUP BY d.id_dueno, d.nombre
ORDER BY total_citas DESC, d.id_dueno
LIMIT 20;

-- ============================================================================
-- BLOQUE 3 · Optimizar no cambio el resultado: la prueba
-- ============================================================================

-- Prueba 1 · los dos COUNT(*) de la agenda, en la misma corrida. Las dos columnas
-- tienen que decir 91.
SELECT (SELECT COUNT(*) FROM cita c, mascota m, dueno d, veterinario v
         WHERE c.id_mascota = m.id_mascota AND m.id_dueno = d.id_dueno
           AND c.id_veterinario = v.id_veterinario
           AND to_char(c.fecha_hora,'YYYY-MM-DD') = '2026-03-10'
           AND UPPER(c.estado) = 'PROGRAMADA')                       AS filas_antes,
       (SELECT COUNT(*) FROM cita c
          JOIN mascota m ON m.id_mascota = c.id_mascota
          JOIN dueno d ON d.id_dueno = m.id_dueno
          JOIN veterinario v ON v.id_veterinario = c.id_veterinario
         WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
           AND c.fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
           AND c.estado = 'PROGRAMADA')                              AS filas_despues;

-- Prueba 2 · EXCEPT en los DOS sentidos, sin LIMIT. A EXCEPT B vacio NO prueba la
-- igualdad: B puede traer filas de mas. Tiene que devolver CERO filas.
WITH antes AS (
  SELECT d.id_dueno,
         (SELECT COUNT(*) FROM cita c JOIN mascota m ON m.id_mascota = c.id_mascota
           WHERE m.id_dueno = d.id_dueno) AS total_citas
  FROM dueno d
), despues AS (
  SELECT d.id_dueno, COUNT(c.id_cita) AS total_citas
  FROM dueno d
  LEFT JOIN mascota m ON m.id_dueno = d.id_dueno
  LEFT JOIN cita c    ON c.id_mascota = m.id_mascota
  GROUP BY d.id_dueno
)
SELECT 'sobra en ANTES' AS lado, * FROM (SELECT * FROM antes EXCEPT SELECT * FROM despues) a
UNION ALL
SELECT 'sobra en DESPUES', * FROM (SELECT * FROM despues EXCEPT SELECT * FROM antes) b;

-- El contraejemplo que vale la pena proyectar 30 segundos: con COUNT(*) en vez de
-- COUNT(c.id_cita), estas 6 filas dicen 1 y la respuesta correcta es 0.
SELECT d.id_dueno, COUNT(c.id_cita) AS bien, COUNT(*) AS mal
FROM dueno d
LEFT JOIN mascota m ON m.id_dueno = d.id_dueno
LEFT JOIN cita c    ON c.id_mascota = m.id_mascota
WHERE d.id_dueno BETWEEN 2001 AND 2006
GROUP BY d.id_dueno ORDER BY d.id_dueno;

-- Lo que NO se puede medir aqui, y hay que decirlo (es la seccion 5 de la
-- pregunta 5): tiempos con la memoria intermedia vacia —vaciarla exige
-- privilegios de administrador—, concurrencia (eso es la Clase 10) y cualquier
-- comparacion por encima de unos cientos de miles de filas.
```

**Pasos guiados del taller:**
1. Reescribir la agenda del dia corrigiendo sus 4 antipatrones (SELECT *, joins con coma, to_char sobre la fecha, UPPER sobre el estado) y probar con COUNT(*) que las dos versiones devuelven las mismas 91 filas.
2. Medir con EXPLAIN (ANALYZE, BUFFERS) las dos versiones, y con EXPLAIN ANALYZE una tercera que le anada LIMIT 50, y anotar las tres en comentarios: nodo mas costoso, filas estimadas vs reales y tiempo.
3. Matar la subconsulta correlacionada del ranking de duenos: LEFT JOIN + GROUP BY + COUNT(c.id_cita), y demostrar la equivalencia con EXCEPT en los dos sentidos.
4. Responder la de seleccion multiple sobre antipatrones (6 afirmaciones, 4 correctas).
5. Escribir la justificacion tecnica de media pagina y guardar 06_opt_antes.sql / 06_opt_despues.sql en la carpeta del PI.

**Entregable:** 2 consultas (antes/despues) + justificacion (media pag.)
**Criterios de exito:**
- La agenda del día con sus @@4 antipatrones@@ corregidos: proyección, `JOIN … ON`, predicado de rango sargable y comparación directa del estado.
- Las dos versiones devuelven las mismas @@91 filas@@, probado con `COUNT(*)` de cada una en la misma corrida.
- Tres planes leídos: `EXPLAIN (ANALYZE, BUFFERS)` del antes y del después, y `EXPLAIN ANALYZE` del después con `LIMIT 50`. Las @@tres@@ versiones van en la mini tabla de comentarios: nodo más costoso, filas estimadas vs reales, tiempo.
- La subconsulta correlacionada convertida en @@una sola pasada@@: `LEFT JOIN` + `GROUP BY` + @@`COUNT(c.id_cita)`@@, con los duenos sin citas todavía en 0.
- La equivalencia del ranking probada con `EXCEPT` en los @@dos sentidos@@: cero filas.
- La justificación de media página con sus 5 secciones, y `06_opt_antes.sql` / `06_opt_despues.sql` en la carpeta del PI.
- Entrega domingo 23:59.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 6/Quiz Clase 6 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 7 — Indices y particionamiento · VetCare

**Objetivo practico:** 3 indices justificados (uno parcial) + historico particionado por ano
**Por que importa:** la rúbrica pide índices justificados, y una justificación es una consulta concreta más la evidencia del plan — no «indexé las columnas importantes».

**Demo en vivo:**
- Pizarra: Tabla caliente (Cita) con una flecha grande hacia un rectangulo 'INDICE idx_cita_fecha_hora' y la palabra 'acelera lectura / cuesta escritura'.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Indices y particionamiento»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Indices y particionamiento» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 7 · Indices y particionamiento
-- Ejecutable en PostgreSQL, incluido PGlite (la consola de ExamLab). Corre completo y
-- EN ORDEN: el valor de la clase esta en el antes/despues, no en el CREATE INDEX.
--
-- Los CINCO nombres de indice de aqui son los EXACTOS que califica la actividad. No los
-- cambie: el plan de ejecucion imprime "Index Scan using <nombre>" y la tabla de
-- justificacion de la pregunta 5 se llena con estos nombres.
--
-- ATENCION: el BLOQUE 0 recrea las tablas desde cero. Correlo en una base vacia o en la
-- consola de ExamLab, no sobre una VetCare DB con datos que quiera conservar. Si ya tiene
-- las 30.010 citas cargadas, salte al BLOQUE 1.

-- =====================================================================
-- BLOQUE 0 · Volumen. Con 50 filas el planeador prefiere Seq Scan por
-- muchos indices que existan: sin volumen esta clase no se puede medir.
-- Reproduce la siembra sintetica de la actividad: 30.000 citas del
-- 2026-01-05 al 2026-07-23, 5.000 mascotas, 2.000 duenos, 12 veterinarios.
-- (En ExamLab hay 10 citas mas puestas a mano en septiembre: 30.010.)
-- =====================================================================
DROP TABLE IF EXISTS cita_hist;
DROP TABLE IF EXISTS cita;
DROP TABLE IF EXISTS mascota;
DROP TABLE IF EXISTS veterinario;
DROP TABLE IF EXISTS dueno;

CREATE TABLE dueno (
  id_dueno SERIAL PRIMARY KEY,
  nombre   TEXT NOT NULL,
  ciudad   TEXT DEFAULT 'Cali'
);
CREATE TABLE veterinario (
  id_veterinario SERIAL PRIMARY KEY,
  nombre         TEXT NOT NULL,
  especialidad   TEXT
);
CREATE TABLE mascota (
  id_mascota SERIAL PRIMARY KEY,
  id_dueno   INT NOT NULL REFERENCES dueno(id_dueno),
  nombre     TEXT NOT NULL,
  especie    TEXT NOT NULL
);
CREATE TABLE cita (
  id_cita        SERIAL PRIMARY KEY,
  id_mascota     INT NOT NULL REFERENCES mascota(id_mascota),
  id_veterinario INT NOT NULL REFERENCES veterinario(id_veterinario),
  fecha_hora     TIMESTAMP NOT NULL,
  estado         TEXT NOT NULL DEFAULT 'PROGRAMADA'
    CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA'))
);

INSERT INTO dueno (nombre) SELECT 'Dueno ' || g FROM generate_series(1, 2000) AS g;
INSERT INTO veterinario (nombre, especialidad)
SELECT 'Veterinario ' || g,
       CASE WHEN g % 3 = 0 THEN 'Cirugia'
            WHEN g % 3 = 1 THEN 'General'
            ELSE 'Dermatologia' END
FROM generate_series(1, 12) AS g;
INSERT INTO mascota (id_dueno, nombre, especie)
SELECT 1 + (g % 2000), 'Mascota ' || g,
       CASE WHEN g % 2 = 0 THEN 'Canino' ELSE 'Felino' END
FROM generate_series(1, 5000) AS g;
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
SELECT 1 + (g % 5000),
       1 + (g % 12),
       TIMESTAMP '2026-01-05 08:00:00'
         + ((g % 200) * INTERVAL '1 day')
         + ((g % 9) * INTERVAL '45 minutes'),
       CASE WHEN g % 11 = 0 THEN 'CANCELADA'
            WHEN g % 3  = 0 THEN 'ATENDIDA'
            ELSE 'PROGRAMADA' END
FROM generate_series(1, 30000) AS g;

ANALYZE dueno;  ANALYZE veterinario;  ANALYZE mascota;  ANALYZE cita;

-- Control: 30.000 | 18.182 PROGRAMADA | 9.091 ATENDIDA | 2.727 CANCELADA. En la base de
-- ExamLab hay 10 citas mas sembradas a mano, y ahi el reparto es 30.010 / 18.187 / 9.095 /
-- 2.728. Si su corrida da otros numeros, el resto del script no cuadra.
SELECT estado, COUNT(*) FROM cita GROUP BY estado ORDER BY estado;

-- =====================================================================
-- BLOQUE 1 · LINEA BASE. Sin este paso no hay clase: el "despues" solo
-- significa algo contra un "antes" medido. Tiene que salir Seq Scan.
-- =====================================================================
EXPLAIN ANALYZE   -- C1 · agenda del dia (rango de fecha + estado)
SELECT id_cita, fecha_hora, estado
  FROM cita
 WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
   AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
   AND estado = 'PROGRAMADA';
-- Esperado: Seq Scan on cita, filas devueltas = 91 (de 150 citas ese dia).

EXPLAIN ANALYZE   -- C2 · mascotas de un dueno
SELECT id_mascota, nombre, especie FROM mascota WHERE id_dueno = 1234;
-- Esperado: Seq Scan on mascota, 2 filas devueltas (id_dueno = 1 + (g % 2000) hace que solo
-- las mascotas g=1233 y g=3233 caigan en el dueno 1234). La FK NO crea indice sola en PostgreSQL.

-- =====================================================================
-- BLOQUE 2 · LOS TRES INDICES DE LA PREGUNTA 1
-- =====================================================================
-- (a) Simple: sirve a cualquier consulta por rango de fecha, con o sin estado.
CREATE INDEX idx_cita_fecha_hora ON cita (fecha_hora);

-- (b) Sobre la FK: "las mascotas de un dueno", y ademas abarata el borrado de un dueno.
CREATE INDEX idx_mascota_dueno ON mascota (id_dueno);

-- (c) PARCIAL: el WHERE es parte de la DEFINICION del indice, no de la consulta. Indexa
--     18.182 de las 30.000 de este script (18.187 de 30.010 en ExamLab) porque la pantalla
--     de agenda nunca pregunta por atendidas ni por canceladas.
CREATE INDEX idx_cita_programada_fecha ON cita (fecha_hora) WHERE estado = 'PROGRAMADA';

-- El paso que se salta la mitad del salon. Crear el indice NO actualiza estadisticas.
ANALYZE cita;
ANALYZE mascota;

-- Las MISMAS dos consultas, sin cambiar una coma.
EXPLAIN ANALYZE
SELECT id_cita, fecha_hora, estado
  FROM cita
 WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'
   AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'
   AND estado = 'PROGRAMADA';
-- Esperado: Index Scan using idx_cita_programada_fecha (gana el PARCIAL: recorre 91
-- entradas y ya sabe que todas cumplen el estado; el completo recorreria 150 y tendria
-- que descartar 59 despues de leer la tabla). Reporte el que VEA, no el que diga esto.

EXPLAIN ANALYZE
SELECT id_mascota, nombre, especie FROM mascota WHERE id_dueno = 1234;
-- Esperado: Index Scan (o Bitmap Index Scan) using idx_mascota_dueno.

-- Evidencia de que existen. indexdef devuelve el CREATE INDEX completo, asi que aqui se
-- ve tambien el WHERE del parcial.
SELECT indexname, tablename, indexdef
  FROM pg_indexes
 WHERE tablename IN ('cita','mascota')
 ORDER BY tablename, indexname;

-- =====================================================================
-- BLOQUE 3 · ORDEN DE COLUMNAS (pregunta 2). Los dos indices llevan las
-- MISMAS dos columnas en orden inverso, y existen para demostrar que el
-- orden decide. Regla: igualdad primero, rango al final.
-- =====================================================================
CREATE INDEX idx_cita_estado_fecha ON cita (estado, fecha_hora);
CREATE INDEX idx_cita_fecha_estado ON cita (fecha_hora, estado);
ANALYZE cita;

EXPLAIN ANALYZE   -- Q1 · estado (igualdad) + fecha (rango) -> favorece (estado, fecha_hora)
SELECT id_cita, fecha_hora FROM cita
 WHERE estado = 'PROGRAMADA'
   AND fecha_hora >= TIMESTAMP '2026-03-01' AND fecha_hora < TIMESTAMP '2026-04-01';

EXPLAIN ANALYZE   -- Q2 · solo rango de fecha -> favorece (fecha_hora, estado)
SELECT id_cita, estado FROM cita
 WHERE fecha_hora >= TIMESTAMP '2026-03-01' AND fecha_hora < TIMESTAMP '2026-04-01';

EXPLAIN ANALYZE   -- Q3 · solo estado, sin fecha -> columna lider ausente en el de fecha
SELECT COUNT(*) FROM cita WHERE estado = 'CANCELADA';

-- Fuerce el experimento: quite el que Q2 estaba usando y vuelva a medir.
DROP INDEX idx_cita_fecha_estado;
ANALYZE cita;
EXPLAIN ANALYZE
SELECT id_cita, estado FROM cita
 WHERE fecha_hora >= TIMESTAMP '2026-03-01' AND fecha_hora < TIMESTAMP '2026-04-01';
-- Esperado: cae en idx_cita_fecha_hora o vuelve a Seq Scan, pero NO usa
-- idx_cita_estado_fecha: su columna lider (estado) no aparece en el WHERE.

-- =====================================================================
-- BLOQUE 4 · PARTICIONAMIENTO (pregunta 3). HOY SE IMPLEMENTA.
-- =====================================================================
-- La trampa: en una tabla particionada la PK DEBE incluir la columna de particion.
-- PRIMARY KEY (id_cita) a secas no compila, y el mensaje del motor no lo dice asi.
CREATE TABLE cita_hist (
  id_cita        INT,
  id_mascota     INT,
  id_veterinario INT,
  fecha_hora     TIMESTAMP NOT NULL,
  estado         TEXT,
  PRIMARY KEY (id_cita, fecha_hora)
) PARTITION BY RANGE (fecha_hora);

-- Rango cerrado por abajo, abierto por arriba: el TO de una es el FROM de la siguiente.
CREATE TABLE cita_hist_2025 PARTITION OF cita_hist
  FOR VALUES FROM (TIMESTAMP '2025-01-01') TO (TIMESTAMP '2026-01-01');
CREATE TABLE cita_hist_2026 PARTITION OF cita_hist
  FOR VALUES FROM (TIMESTAMP '2026-01-01') TO (TIMESTAMP '2027-01-01');

INSERT INTO cita_hist
SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado FROM cita;

-- Prueba del enrutamiento. tableoid es la columna de sistema que dice en que tabla FISICA
-- vive cada fila; ::regclass la traduce a nombre. Sin esto no hay evidencia: solo un
-- INSERT que no dio error.
SELECT tableoid::regclass AS particion, COUNT(*), MIN(fecha_hora), MAX(fecha_hora)
  FROM cita_hist GROUP BY 1 ORDER BY 1;
-- Con la siembra del BLOQUE 0 (todas las citas son de 2026) cae TODO en cita_hist_2026 y
-- cita_hist_2025 queda vacia: eso ya demuestra el enrutamiento. La base de la pregunta 3
-- en ExamLab reparte 5.010 citas entre 2025 y 2026 y ahi se ven las dos particiones.

-- Poda de particiones: lo unico que mejora hoy de verdad.
EXPLAIN ANALYZE
SELECT COUNT(*) FROM cita_hist
 WHERE fecha_hora >= TIMESTAMP '2026-01-01' AND fecha_hora < TIMESTAMP '2027-01-01';
-- Esperado: en el plan aparece SOLO cita_hist_2026. El tiempo no baja de forma apreciable
-- con este volumen, y hay que decirlo: lo que se demuestra es que el motor descarta
-- particiones enteras ANTES de leer.

-- El beneficio real es de mantenimiento: archivar un ano es DROP TABLE de su particion
-- --una operacion de metadatos-- en vez de un DELETE masivo que toca millones de filas,
-- infla el registro de transacciones y sostiene bloqueos largos. Eso es la Clase 8.
-- DROP TABLE cita_hist_2025;
```

**Pasos guiados del taller:**
1. Medir la linea base con EXPLAIN ANALYZE de las dos consultas frecuentes: hay que ver Seq Scan.
2. Crear los tres indices con el nombre exacto, incluido el parcial idx_cita_programada_fecha, y correr ANALYZE.
3. Repetir los EXPLAIN y decir cual indice eligio el planeador y por que.
4. Construir cita_hist particionada por ano, migrar las citas y demostrar el enrutamiento y la poda.
5. Llenar la tabla de justificacion consulta->indice (7 columnas) y el veredicto de particionamiento.

**Entregable:** Script CREATE INDEX + cita_hist particionada + tabla justificacion consulta->indice
**Criterios de exito:**
- La línea base medida @@antes@@ de indexar: `EXPLAIN ANALYZE` de las dos consultas frecuentes con `Seq Scan` a la vista.
- Los @@tres@@ índices con el nombre exacto — `idx_cita_fecha_hora`, `idx_mascota_dueno` y el @@parcial@@ `idx_cita_programada_fecha` con su `WHERE estado = 'PROGRAMADA'` — y `ANALYZE` corrido después.
- Los `EXPLAIN` repetidos mostrando `Index Scan` o `Bitmap Index Scan`, y dicho @@cuál@@ de los dos índices sobre `fecha_hora` eligió el planeador.
- El experimento del orden de columnas: los dos índices compuestos, las @@tres@@ consultas medidas, el `DROP INDEX` que fuerza la comparación y la línea `-- CONCLUSION:` con la regla de igualdad antes que rango.
- `cita_hist` particionada por año: PK que @@incluye la columna de partición@@, las dos particiones sin solaparse, la migración completa y la @@poda@@ evidenciada en el plan.
- La tabla de justificación con sus @@7 columnas@@ y una fila por índice (mínimo 3), la regla de sobre-indexación y el veredicto de particionamiento con @@tus números@@.
- Entrega domingo 23:59.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 7/Quiz Clase 7 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 8 — Tuning · Transacciones · VetCare

**Objetivo practico:** Transaccion de negocio (factura + stock) + notas de tuning
**Por que importa:** facturar es la operación donde Huellitas pierde plata si algo queda a medias: una factura sin líneas, o un stock descontado de una factura que nunca existió.

**Demo en vivo:**
- Pizarra: Linea de tiempo horizontal: BEGIN → INSERT factura → INSERT detalle → UPDATE stock → COMMIT/ROLLBACK con una bifurcacion visual en el ROLLBACK.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Tuning»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Tuning» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 8 · Transaccion de facturacion + descuento de stock
-- Ejecutable en PostgreSQL, incluido PGlite (la consola de ExamLab). Corre completo y
-- EN ORDEN: el bloque 3 solo tiene sentido si antes se tomo la foto del bloque 2.
--
-- ESTO ES PL/pgSQL, NO PL/SQL DE ORACLE. Aqui no existen NUMBER, SQL%ROWCOUNT ni
-- RAISE_APPLICATION_ERROR, y NO se escribe COMMIT ni ROLLBACK dentro del procedimiento:
-- el CALL de nivel superior ya es su propia transaccion.

-- =====================================================================
-- BLOQUE 0 · Esquema minimo y datos. Los stocks son los de la actividad.
-- =====================================================================
-- Los DROP van primero para que el script se pueda correr dos veces sin limpiar a mano.
DROP PROCEDURE IF EXISTS sp_facturar(INT, INT[], INT[]);
DROP FUNCTION  IF EXISTS fn_descontar_stock(INT, INT);
DROP TABLE     IF EXISTS detalle_factura;
DROP TABLE     IF EXISTS factura;
DROP TABLE     IF EXISTS insumo;

CREATE TABLE insumo (
  id_insumo   SERIAL PRIMARY KEY,
  nombre      TEXT NOT NULL,
  stock       INT NOT NULL CHECK (stock >= 0),
  precio_unit NUMERIC(12,2) NOT NULL
);
CREATE TABLE factura (
  id_factura  SERIAL PRIMARY KEY,
  id_consulta INT NOT NULL,
  total       NUMERIC(12,2) NOT NULL DEFAULT 0
);
CREATE TABLE detalle_factura (
  id_detalle  SERIAL PRIMARY KEY,
  id_factura  INT NOT NULL REFERENCES factura(id_factura),
  id_insumo   INT NOT NULL REFERENCES insumo(id_insumo),
  cantidad    INT NOT NULL CHECK (cantidad > 0),
  precio_unit NUMERIC(12,2) NOT NULL
);

INSERT INTO insumo (nombre, stock, precio_unit) VALUES
  ('Vacuna antirrabica',   12, 22000),   -- 1
  ('Vacuna triple felina',  3, 31000),   -- 2  <- el que se va a quedar corto
  ('Antiparasitario oral', 40,  9500),   -- 3
  ('Suero fisiologico',    25,  7000),   -- 4
  ('Gasa esteril',          8,  1200),   -- 5
  ('Jeringa 5ml',          60,   900);   -- 6

-- =====================================================================
-- BLOQUE 1 · EL PROCEDIMIENTO. Una factura tiene VARIAS lineas, asi que
-- la firma recibe dos arreglos paralelos, no un insumo suelto.
-- =====================================================================
CREATE PROCEDURE sp_facturar(
  p_id_consulta INT,
  p_insumos     INT[],
  p_cantidades  INT[]
)
LANGUAGE plpgsql
AS $proc$
DECLARE
  v_id_factura INT;
  v_total   NUMERIC(12,2) := 0;
  v_precio  NUMERIC(12,2);
  v_filas   INT;
  i         INT;
BEGIN
  -- El llamador se equivoco: se rechaza antes de tocar la base.
  IF array_length(p_insumos, 1) IS DISTINCT FROM array_length(p_cantidades, 1) THEN
    RAISE EXCEPTION 'ERROR: insumos y cantidades deben tener la misma longitud';
  END IF;

  -- Total en 0: todavia no se sabe. RETURNING ... INTO evita otro SELECT.
  INSERT INTO factura (id_consulta, total) VALUES (p_id_consulta, 0)
  RETURNING id_factura INTO v_id_factura;

  FOR i IN 1 .. array_length(p_insumos, 1) LOOP
    SELECT precio_unit INTO v_precio FROM insumo WHERE id_insumo = p_insumos[i];
    IF NOT FOUND THEN
      RAISE EXCEPTION 'ERROR: el insumo % no existe', p_insumos[i];
    END IF;

    -- EL GUARDIA. La comprobacion viaja DENTRO del WHERE: comprobar y escribir son
    -- una sola sentencia atomica y nadie puede colarse entre las dos.
    UPDATE insumo
       SET stock = stock - p_cantidades[i]
     WHERE id_insumo = p_insumos[i]
       AND stock >= p_cantidades[i];
    GET DIAGNOSTICS v_filas = ROW_COUNT;   -- 1 alcanzo, 0 no habia stock
    IF v_filas = 0 THEN
      RAISE EXCEPTION 'ERROR: stock insuficiente del insumo % (se pidieron %)',
        p_insumos[i], p_cantidades[i];
    END IF;

    INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit)
    VALUES (v_id_factura, p_insumos[i], p_cantidades[i], v_precio);

    v_total := v_total + (v_precio * p_cantidades[i]);
  END LOOP;

  UPDATE factura SET total = v_total WHERE id_factura = v_id_factura;
  RAISE NOTICE 'Factura % creada por %', v_id_factura, v_total;
END;
$proc$;

-- =====================================================================
-- BLOQUE 2 · CASO EXITOSO
-- =====================================================================
CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3]);
-- Esperado: 22000*1 + 900*2 + 1200*3 = 27.400, y los stocks 1, 6 y 5 bajan a 11, 58 y 5.
SELECT id_factura, id_consulta, total FROM factura ORDER BY id_factura;
SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;

-- =====================================================================
-- BLOQUE 3 · ATOMICIDAD. Aqui esta la clase entera.
-- =====================================================================
-- Foto inicial: estos numeros son el punto de comparacion.
SELECT (SELECT COUNT(*) FROM factura)         AS facturas,
       (SELECT COUNT(*) FROM detalle_factura) AS lineas,
       (SELECT stock FROM insumo WHERE id_insumo = 3) AS stock_3,
       (SELECT stock FROM insumo WHERE id_insumo = 2) AS stock_2;
-- Esperado tras el bloque 2: 1 | 3 | 40 | 3

-- Intento que falla A MITAD: la primera linea (2 del insumo 3, que tiene 40) SI alcanza;
-- la segunda (10 del insumo 2, que solo tiene 3) NO. El DO ... EXCEPTION es para que el
-- script no se detenga; el que decide sigue siendo el procedimiento.
DO $$
BEGIN
  CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 10]);
  RAISE NOTICE 'No deberia llegar aqui';
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'Fallo esperado: %', SQLERRM;
END $$;

-- Foto final: EXACTAMENTE la misma consulta.
SELECT (SELECT COUNT(*) FROM factura)         AS facturas,
       (SELECT COUNT(*) FROM detalle_factura) AS lineas,
       (SELECT stock FROM insumo WHERE id_insumo = 3) AS stock_3,
       (SELECT stock FROM insumo WHERE id_insumo = 2) AS stock_2;
-- Esperado: 1 | 3 | 40 | 3, identico a la foto inicial.
--   * no quedo una factura huerfana,
--   * no quedo ninguna linea de detalle,
--   * y sobre todo el stock del insumo 3 VOLVIO A 40: el descuento que si habia
--     alcanzado se deshizo. Nadie escribio ROLLBACK.

-- Y ahora la misma factura con una cantidad viable del insumo 2.
CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 3]);
SELECT id_factura, id_consulta, total FROM factura ORDER BY id_factura;
SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;
-- Esperado: factura 2 por 9500*2 + 31000*3 = 112.000; insumo 3 en 38 e insumo 2 en 0.

-- =====================================================================
-- BLOQUE 4 · EL MISMO PATRON COMO FUNCION REUTILIZABLE
-- Aqui "no hay stock" es una RESPUESTA, no un error: la funcion informa y
-- el llamador decide. El procedimiento del bloque 1 abortaba.
-- =====================================================================
CREATE FUNCTION fn_descontar_stock(p_id_insumo INT, p_cantidad INT)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $fn$
DECLARE
  v_filas INT;
BEGIN
  -- Una cantidad no positiva no es "no hay stock", es una llamada mal hecha.
  IF p_cantidad <= 0 THEN
    RAISE EXCEPTION 'ERROR: la cantidad debe ser positiva (llego %)', p_cantidad;
  END IF;

  UPDATE insumo
     SET stock = stock - p_cantidad
   WHERE id_insumo = p_id_insumo
     AND stock >= p_cantidad;
  GET DIAGNOSTICS v_filas = ROW_COUNT;

  RETURN v_filas = 1;
END;
$fn$;

-- Reiniciar los stocks para que la prueba de abajo de los valores esperados.
UPDATE insumo SET stock = 8 WHERE id_insumo = 5;
UPDATE insumo SET stock = 3 WHERE id_insumo = 2;

SELECT fn_descontar_stock(5, 3)  AS caso_ok,
       fn_descontar_stock(2, 10) AS caso_sin_stock,
       fn_descontar_stock(2, 3)  AS caso_limite;
-- Esperado: true | false | true. El tercero es el interesante: pide EXACTAMENTE el stock
-- que queda, y con >= en el guardia tiene que pasar.

SELECT id_insumo, nombre, stock FROM insumo ORDER BY id_insumo;
-- Esperado: insumo 5 en 5, insumo 2 en 0, y NINGUN stock negativo.

-- La diferencia con leer primero y decidir despues:
--   SELECT stock ... ; IF stock >= cantidad THEN UPDATE ...
-- deja una VENTANA entre la lectura y la escritura. Con dos recepcionistas facturando el
-- mismo insumo, las dos leen 3, las dos deciden que alcanza, y el stock termina en -2 (o
-- el CHECK revienta). El UPDATE con la condicion en el WHERE no tiene ventana.
-- Aqui no se puede demostrar: PGlite corre UNA SOLA sesion. Ese es el gap que se declara
-- en la pregunta 5 y lo que abre la Clase 10.
```

**Pasos guiados del taller:**
1. Escribir sp_facturar(p_id_consulta, p_insumos INT[], p_cantidades INT[]) en PL/pgSQL: cabecera con total 0, bucle por linea con el guardia stock >= cantidad, y UPDATE del total al final.
2. Probar el fallo a mitad con ARRAY[3,2] / ARRAY[2,10] y demostrar con foto inicial y final que el stock del insumo 3 volvio a 40.
3. Encapsular el descuento en fn_descontar_stock, que devuelve BOOLEAN y no lanza excepcion.
4. Llenar la seccion Transacciones y tuning del informe: inventario de 3 transacciones y checklist de 7 items.
5. Declarar el gap de concurrencia: PGlite corre una sola sesion, y eso es la Clase 10.

**Entregable:** sp_facturar + fn_descontar_stock + seccion Transacciones y tuning del informe (1 pag.)
**Criterios de exito:**
- `sp_facturar(p_id_consulta INT, p_insumos INT[], p_cantidades INT[])` con la firma exacta: cabecera en total 0 con `RETURNING … INTO`, bucle por línea, `UPDATE` condicional con `GET DIAGNOSTICS … ROW_COUNT` y `RAISE EXCEPTION` si no alcanza.
- El caso exitoso ejecutado y evidenciado: factura por @@27.400@@ y los insumos 1, 6 y 5 en @@11, 58 y 5@@.
- La atomicidad probada con @@la misma consulta@@ de foto inicial y final, y dicho con datos que el stock del insumo 3 @@volvió a 40@@ y que no quedó factura ni línea huérfana.
- `fn_descontar_stock` devolviendo `BOOLEAN` — @@`FALSE`, no excepción@@, cuando no hay stock — con la prueba que arroja `true / false / true` y ningún stock negativo.
- La sección del informe con sus 4 bloques: @@3 transacciones@@ con su punto de fallo, el checklist de @@7 ítems@@ con estado y evidencia, la decisión documentada y el gap de concurrencia.
- Entrega domingo 23:59.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 8/Quiz Clase 8 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 10 — Control de concurrencia · VetCare

**Objetivo practico:** Escenarios de concurrencia del PI documentados
**Por que importa:** doble reserva y stock negativo.

**Demo en vivo:**
- Pizarra: La MISMA linea de tiempo T1/T2 de la diapositiva de Clase 10, pero redibujada en vivo con los IDs reales que use el script de demo.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Control de concurrencia»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Control de concurrencia» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 10 · Demo ejecutable: doble reserva y su mitigacion
-- Ejecutar EN ORDEN: primero se ve el problema, despues la solucion.

-- Paso 1: tabla de demo SIN restriccion (asi llegaria si nadie penso en concurrencia)
CREATE TABLE cita_demo (
  id_cita INT PRIMARY KEY,
  id_mascota INT NOT NULL,
  id_veterinario INT NOT NULL,
  fecha_hora TIMESTAMP NOT NULL,
  estado VARCHAR(20) DEFAULT 'PROGRAMADA'
);

-- Paso 2: T1 (Recepcion A) agenda la franja - OK
INSERT INTO cita_demo VALUES (1, 10, 5, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');

-- Paso 3: T2 (Recepcion B) agenda OTRA mascota, MISMO veterinario, MISMA franja.
-- Sin restriccion esto se inserta SIN ERROR -> aqui esta la doble reserva.
INSERT INTO cita_demo VALUES (2, 22, 5, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');

-- Evidencia del problema: dos citas para el mismo veterinario en la misma franja
SELECT id_veterinario, fecha_hora, COUNT(*) AS citas_en_la_misma_franja
FROM cita_demo
GROUP BY id_veterinario, fecha_hora
HAVING COUNT(*) > 1;

-- Paso 4: la mitigacion real - la restriccion que debio existir desde el diseño
ALTER TABLE cita_demo
  ADD CONSTRAINT uq_cita_demo_vet_fecha UNIQUE (id_veterinario, fecha_hora);

-- Paso 5: repetir el intento de doble reserva - AHORA debe fallar
INSERT INTO cita_demo VALUES (3, 35, 5, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');
-- Esperado: error de restriccion unica (ORA-00001 en Oracle) -> la BD rechaza la doble reserva.
```

**Pasos guiados del taller:**
1. Describir escenario doble reserva con tiempos T1/T2.
2. Describir escenario doble descuento de stock.
3. Proponer mitigacion SQL.
4. Anadir seccion al informe PI.

**Entregable:** Informe corto: 2 escenarios (cita doble / stock) + mitigacion
**Criterios de exito:**
- Doble reserva.
- Doble stock.
- Mitigacion SQL.
- Sección informe.
- Domingo 23:59.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 10/Quiz Clase 10 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 11 — Avance PI · VetCare DB

**Objetivo practico:** Demo parcial + checklist de avance (hito formal PI)
**Por que importa:** checkpoint vs rúbrica.

**Demo en vivo:**
- Pizarra: Checklist en 2 columnas: Evidencia (ER, DDL, roles, procs, fn, triggers, opt) | Si/No/Parcial — llenar en vivo con el curso.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Avance PI»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Avance PI» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 11 · Seed ejecutable para la demo de checklist
-- Autocontenido: cree estas tablas minimas si aun no las tiene, o
-- adapte los nombres a su propio DDL (Clases 1-8) antes de correr los INSERT.

CREATE TABLE dueno_demo (id_dueno INT PRIMARY KEY, nombre VARCHAR(80));
CREATE TABLE mascota_demo (
  id_mascota INT PRIMARY KEY, id_dueno INT REFERENCES dueno_demo(id_dueno),
  nombre VARCHAR(60), activa CHAR(1) DEFAULT 'S'
);
CREATE TABLE cita_demo11 (
  id_cita INT PRIMARY KEY, id_mascota INT REFERENCES mascota_demo(id_mascota),
  fecha_hora TIMESTAMP, estado VARCHAR(20)
);
CREATE TABLE insumo_demo (id_insumo INT PRIMARY KEY, nombre VARCHAR(60), stock INT);

-- Datos que permiten mostrar EN VIVO cada punto del checklist:
INSERT INTO dueno_demo VALUES (1, 'Ana Perez');
INSERT INTO dueno_demo VALUES (2, 'Carlos Ruiz');
INSERT INTO mascota_demo VALUES (10, 1, 'Luna', 'S');   -- mascota activa: SI puede agendar
INSERT INTO mascota_demo VALUES (11, 2, 'Rocky', 'N');  -- mascota inactiva: NO debe poder agendar
INSERT INTO cita_demo11 VALUES (100, 10, TIMESTAMP '2026-10-19 09:00:00', 'PROGRAMADA');
INSERT INTO insumo_demo VALUES (50, 'Vacuna antirrabica', 3);  -- stock bajo a proposito

-- Punto del checklist "regla de negocio se cumple": intente agendar la mascota
-- inactiva (id 11) con su sp_agendar_cita y confirme que el proc la rechaza.
-- Punto "stock nunca negativo": intente facturar 5 unidades del insumo 50
-- (solo hay 3) y confirme que su transaccion de Clase 8 hace ROLLBACK.
SELECT m.nombre, m.activa, d.nombre AS dueno FROM mascota_demo m JOIN dueno_demo d ON d.id_dueno = m.id_dueno;
```

**Pasos guiados del taller:**
1. Completar checklist de avance (si/no/parcial).
2. Demo 3-5 min: ER + 1 proc + 1 trigger.
3. Lista de gaps con responsable.
4. Subir avance intermedio a ExamLab (Talleres) si se pide.

**Entregable:** Checklist firmada + enlace/ZIP avance (DDL+procs+ER)
**Criterios de exito:**
- Checklist evidenciada.
- Demo ER+proc+trigger.
- Gaps.
- Avance subido si aplica.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 11/Quiz Clase 11 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 12 — Integracion app <-> BD · Prep. presentacion

**Objetivo practico:** Contrato integracion + preparacion de entrega/sustentacion
**Por que importa:** app llama contrato, no SQL suelto.

**Demo en vivo:**
- Pizarra: Caja 'App' — flecha rotulada con el nombre del proc (ej. sp_agendar_cita) — caja 'Base de datos'. Sin flecha directa App→tablas.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Integracion app <-> BD»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Integracion app <-> BD» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 12 · Contrato app<->BD (Oracle PL/SQL, ejecutable)
-- Regla: la app NUNCA hace INSERT directo a cita/consulta/factura; solo llama estos procs.

CREATE OR REPLACE PROCEDURE sp_agendar_cita (
  p_id_cita IN NUMBER, p_id_mascota IN NUMBER, p_fecha IN TIMESTAMP, p_msg OUT VARCHAR2
) AS
BEGIN
  INSERT INTO cita(id_cita, id_mascota, fecha_hora, estado) VALUES (p_id_cita, p_id_mascota, p_fecha, 'PROGRAMADA');
  p_msg := 'OK: cita agendada'; COMMIT;
EXCEPTION WHEN OTHERS THEN p_msg := 'ERROR: ' || SQLERRM; ROLLBACK;
END;
/

CREATE OR REPLACE PROCEDURE sp_registrar_consulta (
  p_id_consulta IN NUMBER, p_id_cita IN NUMBER, p_notas IN VARCHAR2, p_precio IN NUMBER, p_msg OUT VARCHAR2
) AS
BEGIN
  INSERT INTO consulta(id_consulta, id_cita, notas, precio) VALUES (p_id_consulta, p_id_cita, p_notas, p_precio);
  p_msg := 'OK: consulta registrada'; COMMIT;
EXCEPTION WHEN OTHERS THEN p_msg := 'ERROR: ' || SQLERRM; ROLLBACK;
END;
/

-- Contrato para la sustentacion (documentar tal cual en el informe):
-- sp_agendar_cita(id_cita, id_mascota, fecha)      -> p_msg: 'OK: ...' | 'ERROR: ...'
-- sp_registrar_consulta(id_consulta, id_cita, notas, precio) -> p_msg idem
-- sp_facturar(id_factura, id_consulta, lineas...)  -> ver Clase 8 (transaccion factura+stock)
```

**Pasos guiados del taller:**
1. Redactar contrato de >=3 operaciones.
2. Diagrama flujo app->BD (Excalidraw) opcional.
3. Outline presentacion 5-8 min + quien habla que.
4. Empaquetar borrador entrega final.

**Entregable:** Contrato app<->BD + outline de slides de sustentacion (5-8 min)
**Criterios de exito:**
- Contrato 3 ops.
- Parametros/errores/ejemplo.
- Outline pitch.
- Borrador final.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 12/Quiz Clase 12 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 13 — Analisis de casos reales · VetCare

**Objetivo practico:** Informe de caso -> mejoras concretas al PI
**Por que importa:** lecciónes accionables.

**Demo en vivo:**
- Pizarra: Tabla 4 columnas: Contexto | Fallo | Leccion | Cambio en VetCare — una fila por caso discutido.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Analisis de casos reales»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Analisis de casos reales» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Esta clase no requiere script SQL nuevo: es analisis/discusion sobre lo ya construido.

**Pasos guiados del taller:**
1. Elegir 1 caso (backup, rendimiento o seguridad).
2. Resumir en media pagina que paso.
3. Proponer 3 mejoras concretas a su VetCare.
4. Actualizar informe PI con lecciones de casos.

**Entregable:** Informe 1-2 pag.: caso + 3 mejoras aplicables a VetCare
**Criterios de exito:**
- Caso elegido.
- Resumen.
- 3 mejoras.
- Informe.
- Domingo 23:59.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 13/Quiz Clase 13 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 15 — Presentacion PI · Cierre VetCare

**Objetivo practico:** Sustentacion en vivo y entrega final del PI (20% Corte 3)
**Por que importa:** cierre segun rúbrica 20% Corte 3.

**Demo en vivo:**
- Pizarra: Checklist final de empaquetado: ER, DDL, roles, procs, triggers, optimizacion, transacciones, concurrencia, contrato, informe — marcar completos.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Presentacion PI»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Presentacion PI» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Esta clase no requiere script SQL nuevo: es analisis/discusion sobre lo ya construido.

**Pasos guiados del taller:**
1. Subir el paquete final a ExamLab (modulo Proyectos) ANTES de su turno.
2. Sustentar en vivo 5-8 min con el ER y una ejecucion real en pantalla.
3. Responder el Q&A en vivo del docente (preguntas al azar sobre su modelo).
4. Autoevaluacion: que harian distinto.
5. Cierre del curso.

**Entregable:** ZIP/PDF final subido antes del turno + sustentacion en vivo 5-8 min + Q&A
**Criterios de exito:**
- ZIP/PDF en ExamLab ANTES del turno.
- Sustentacion en vivo de 5-8 min.
- Q&A respondido en vivo (preguntas al azar).
- Autoevaluacion.
- Cierre.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 15/Quiz Clase 15 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Parciales (Clase 5 / 9 / 14)

Solo evaluacion — enunciado + solucion en `Parciales/` (dominio VetCare).
Se presentan en ExamLab con proctoring activado (es evaluacion formal
virtual sincrona por Meet); duracion 90-100 min dentro del bloque de 120.

## Proyecto Integrador VetCare DB

Hilo conductor de todas las clases regulares/autonomas. Avance formal en
Clase 11 (checkpoint) y entrega/sustentacion en Clase 15. Se sube a ExamLab
como Proyecto (individual por defecto; equipo de 2-3 solo si el docente lo autoriza); pesa 20% del Corte 3.
