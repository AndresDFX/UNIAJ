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
