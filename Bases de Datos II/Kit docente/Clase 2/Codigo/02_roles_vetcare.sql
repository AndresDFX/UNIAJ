-- VetCare DB · Clase 2 · Roles y privilegios (Oracle Live SQL)
-- Live SQL da UN solo usuario/schema por cuenta: no siempre se puede CREATE ROLE
-- ni GRANT a otro usuario real. Por eso este script trae DOS partes:
--   PARTE A: ejecutable tal cual en cualquier cuenta Live SQL (GRANT/REVOKE sobre
--            las propias tablas hacia PUBLIC, para demostrar la sintaxis real).
--   PARTE B: la version completa multi-usuario (CREATE ROLE + GRANT a rol),
--            documentada como PLAN si el playground no permite crear usuarios/roles.

-- ============ PARTE A — ejecutable en Live SQL (su propio schema) ============
-- Sirve para demostrar que GRANT/REVOKE son sentencias reales, no solo teoria.
GRANT SELECT ON mascota TO PUBLIC;
GRANT SELECT, INSERT, UPDATE ON cita TO PUBLIC;
REVOKE UPDATE ON cita FROM PUBLIC;

-- Verificacion de privilegios otorgados sobre los propios objetos:
SELECT table_name, privilege, grantee
FROM user_tab_privs_made
WHERE table_name IN ('MASCOTA', 'CITA');

-- ============ PARTE B — plan multi-rol (requiere privilegios DBA) ============
-- Roles conceptuales del PI: ADMIN_BD, RECEPCION, VETERINARIO, AUDITOR
CREATE ROLE recepcion;
GRANT SELECT, INSERT, UPDATE ON cita TO recepcion;
GRANT SELECT ON mascota TO recepcion;
GRANT SELECT ON dueno TO recepcion;
REVOKE DELETE ON cita FROM recepcion;

CREATE ROLE veterinario;
GRANT SELECT ON cita TO veterinario;
GRANT SELECT, INSERT, UPDATE ON consulta TO veterinario;

CREATE ROLE auditor;
GRANT SELECT ON cita TO auditor;
GRANT SELECT ON mascota TO auditor;
GRANT SELECT ON dueno TO auditor;

-- Asignar el rol a un usuario real (equivalente conceptual):
-- GRANT recepcion TO usuario_recepcion01;

-- Matriz minima (documentar tal cual en el entregable):
-- RECEPCION:   Cita CRUD limitado (sin DELETE), Dueno/Mascota solo lectura
-- VETERINARIO: Consulta escritura, Cita lectura
-- AUDITOR:     solo SELECT sobre las tablas sensibles
-- ADMIN_BD:    DDL completo + capacidad de otorgar/revocar roles
