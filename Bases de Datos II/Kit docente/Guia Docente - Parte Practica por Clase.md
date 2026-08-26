# Guia Docente — Parte Practica por Clase (Bases de Datos II, 2026-2)

> Cada clase = una practica con objetivo propio. La demo se apoya en un
> boceto de pizarra + un script SQL completo (con datos) para que usted lo
> ejecute en vivo en Oracle Live SQL / DB Fiddle. El taller y el quiz se
> entregan/presentan en ExamLab (`https://uniaj.examlab.workers.dev/`) — no es la plataforma
> oficial de la UNIAJC, pero es la que usamos para eso en este curso.

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
**Por que importa:** roles son evidencia de administración.

**Demo en vivo:**
- Pizarra: Tabla simple 3 columnas: Rol | Objeto | Privilegio (llenar en vivo con los 4 roles del taller).
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Administracion de BD»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Administracion de BD» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
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
```

**Pasos guiados del taller:**
1. Definir >=4 roles (ADMIN_BD, RECEPCION, VETERINARIO, AUDITOR).
2. Matriz SELECT/INSERT/UPDATE/DELETE/EXECUTE por objeto clave.
3. Justificar privilegio minimo (least privilege).
4. Redactar 1 pagina: politica de altas/bajas de usuarios.

**Entregable:** Documento Roles_VetCare + script GRANT/REVOKE (o plan equivalente)
**Criterios de exito:**
- >=4 roles.
- Matriz privilegio x objeto.
- Justificación least privilege.
- 1 página política.
- Domingo 23:59.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 2/Quiz Clase 2 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 3 — Procedimientos almacenados · VetCare

**Objetivo practico:** >=1 procedimiento de negocio (agendar cita / registrar consulta)
**Por que importa:** la regla vive en un proc reutilizable.

**Demo en vivo:**
- Pizarra: Flujo: App → llama sp_agendar_cita → valida mascota.activa → INSERT o mensaje de error.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Procedimientos almacenados»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Procedimientos almacenados» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 3 · Procedimiento agendar cita (Oracle Live SQL)
-- Ajustar tipos segun el schema creado por el estudiante.

CREATE OR REPLACE PROCEDURE sp_agendar_cita (
  p_id_cita IN NUMBER,
  p_id_mascota IN NUMBER,
  p_fecha IN TIMESTAMP,
  p_msg OUT VARCHAR2
) AS
  v_activa CHAR(1);
BEGIN
  SELECT activa INTO v_activa FROM mascota WHERE id_mascota = p_id_mascota;
  IF v_activa <> 'S' THEN
    p_msg := 'ERROR: mascota inactiva; no se agenda';
    RETURN;
  END IF;
  INSERT INTO cita(id_cita, id_mascota, fecha_hora, estado)
  VALUES (p_id_cita, p_id_mascota, p_fecha, 'PROGRAMADA');
  p_msg := 'OK: cita agendada';
  COMMIT;
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    p_msg := 'ERROR: mascota no existe';
  WHEN OTHERS THEN
    p_msg := 'ERROR: ' || SQLERRM;
    ROLLBACK;
END;
/
```

**Pasos guiados del taller:**
1. Implementar sp_agendar_cita o sp_registrar_consulta en Live SQL.
2. Incluir validacion de negocio del PI (>=1).
3. Ejecutar 2 pruebas: caso OK + caso error.
4. Documentar firma del proc (contrato para la futura app).

**Entregable:** Script proc + casos de prueba (captura o enlace Live SQL)
**Criterios de exito:**
- Proc en Live SQL.
- Validación negocio.
- Prueba OK + error.
- Contrato documentado.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 3/Quiz Clase 3 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 4 — Funciones · Triggers · Seguridad y respaldo

**Objetivo practico:** >=1 funcion + >=1 trigger + borrador plan de respaldo
**Por que importa:** integridad + RAA1.

**Demo en vivo:**
- Pizarra: Mismo ER de Clase 1 + una nota junto a Cita: 'AQUI dispara el trigger de auditoria' y junto a Mascota: 'AQUI vive la fn_precio_base'.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Funciones»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Funciones» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 4 · Funcion + trigger auditoria (Oracle)

CREATE OR REPLACE FUNCTION fn_precio_base (p_especie VARCHAR2)
RETURN NUMBER IS
BEGIN
  IF UPPER(p_especie) = 'CANINO' THEN RETURN 45000; END IF;
  IF UPPER(p_especie) = 'FELINO' THEN RETURN 40000; END IF;
  RETURN 35000;
END;
/

CREATE TABLE audit_cita (
  id_audit NUMBER PRIMARY KEY,
  id_cita NUMBER,
  accion VARCHAR2(30),
  detalle VARCHAR2(200),
  fecha_evento TIMESTAMP DEFAULT SYSTIMESTAMP
);

CREATE OR REPLACE TRIGGER trg_audit_cancelacion
AFTER UPDATE OF estado ON cita
FOR EACH ROW
WHEN (NEW.estado = 'CANCELADA' AND OLD.estado <> 'CANCELADA')
BEGIN
  INSERT INTO audit_cita(id_audit, id_cita, accion, detalle)
  VALUES (NVL((SELECT MAX(id_audit) FROM audit_cita),0)+1,
          :NEW.id_cita, 'CANCELACION', 'Cita cancelada');
END;
/

-- Plan backup (documentar en Google Docs): diario logico scripts SQL + semanal export playground.
```

**Pasos guiados del taller:**
1. Crear >=1 funcion util al PI.
2. Crear >=1 trigger (auditoria o stock no negativo).
3. Redactar plan de respaldo: frecuencia, retencion, restore de prueba.
4. Actualizar checklist PI: seguridad/respaldo en progreso.

**Entregable:** Scripts funcion/trigger + Plan_Backup_VetCare (1 pag.)
**Criterios de exito:**
- Funcion util.
- Trigger auditoria/stock.
- Plan backup 1 pag.
- Checklist PI.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 4/Quiz Clase 4 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 6 — Optimizacion de consultas · VetCare

**Objetivo practico:** Primera pareja de consultas antes/despues del PI
**Por que importa:** optimizar el propio DDL.

**Demo en vivo:**
- Pizarra: Dos columnas: 'Antes' (consulta con SELECT * y JOIN sin filtro) vs 'Despues' (columnas puntuales + filtro temprano) sobre el mismo dibujo de tablas.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Optimizacion de consultas»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Optimizacion de consultas» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 6 · Antes / despues

-- ANTES (anti-patron)
SELECT * FROM cita c, mascota m, dueno d
WHERE c.id_mascota = m.id_mascota AND m.id_dueno = d.id_dueno;

-- DESPUES (proyecto columnas + filtro temprano)
SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno
FROM cita c
JOIN mascota m ON m.id_mascota = c.id_mascota
JOIN dueno d ON d.id_dueno = m.id_dueno
WHERE c.fecha_hora >= TIMESTAMP '2026-09-01 00:00:00'
  AND c.fecha_hora <  TIMESTAMP '2026-09-02 00:00:00'
  AND c.estado = 'PROGRAMADA';
```

**Pasos guiados del taller:**
1. Tomar 1 consulta real del PI (citas del dia / historial).
2. Escribir version antes e ineficiente o real.
3. Reescribir despues y justificar 3 cambios.
4. Guardar 06_opt_antes.sql / 06_opt_despues.sql en la carpeta del PI.

**Entregable:** 2 consultas (antes/despues) + justificacion (media pag.)
**Criterios de exito:**
- Consulta real PI.
- Version después.
- 3 cambios.
- Archivos SQL.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 6/Quiz Clase 6 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 7 — Indices y particionamiento · VetCare

**Objetivo practico:** >=2 indices justificados sobre tablas calientes del PI
**Por que importa:** indices aceleran lecturas frecuentes.

**Demo en vivo:**
- Pizarra: Tabla caliente (ej. Cita) con una flecha grande hacia un rectangulo 'INDICE idx_cita_fecha' y la palabra 'acelera lectura / cuesta escritura'.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Indices y particionamiento»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Indices y particionamiento» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 7 · Indices

CREATE INDEX idx_cita_fecha ON cita (fecha_hora);
CREATE INDEX idx_mascota_dueno ON mascota (id_dueno);
CREATE INDEX idx_cita_estado_fecha ON cita (estado, fecha_hora);

-- Justificacion PI:
-- idx_cita_fecha: listado del dia / agenda
-- idx_mascota_dueno: busqueda de mascotas por dueno
-- idx_cita_estado_fecha: filtros combinados recepción
```

**Pasos guiados del taller:**
1. Identificar 2 consultas frecuentes del PI.
2. Proponer y crear >=2 indices con nombre claro.
3. Justificar columna, cardinalidad y riesgo de sobre-indexar.
4. Opcional: diagrama tabla caliente -> indices en Excalidraw.

**Entregable:** Script CREATE INDEX + tabla justificacion consulta->indice
**Criterios de exito:**
- 2 CREATE INDEX.
- Justificación.
- Riesgo sobre-indexar.
- Diagrama opcional.

**Quiz de cierre:** 8 preguntas (banco completo en `Kit docente/Clase 7/Quiz Clase 7 - VetCare.docx`).
**Entrega:** taller y quiz en ExamLab · domingo 23:59 cuando aplique el taller.

---

## Clase 8 — Tuning · Transacciones · VetCare

**Objetivo practico:** Transaccion de negocio (factura + stock) + notas de tuning
**Por que importa:** factura+stock atomicos.

**Demo en vivo:**
- Pizarra: Linea de tiempo horizontal: BEGIN → INSERT factura → INSERT detalle → UPDATE stock → COMMIT/ROLLBACK con una bifurcacion visual en el ROLLBACK.
- Prompt de apoyo (IA, opcional si le falta tiempo de preparar): "Actua como docente de Bases de Datos II. Usando el dominio VetCare (Dueño, Mascota, Cita, Veterinario, Insumo, Factura), dame un ejemplo minimo en SQL (Oracle/PostgreSQL) sobre «Tuning»: (1) el DDL de las tablas que necesito, (2) datos de ejemplo realistas de una clinica veterinaria (INSERT), (3) el codigo que ilustra «Tuning» paso a paso, (4) en 3 lineas, que debe notar el estudiante cuando lo vea ejecutar."
- Script SQL completo para correr en vivo (con datos de ejemplo):
```sql
-- VetCare DB · Clase 8 · Transaccion facturacion + stock (orientativo)

-- Pseudobloque / proc:
-- BEGIN
--   INSERT INTO factura ...
--   INSERT INTO detalle_factura ...
--   UPDATE insumo SET stock = stock - :cant WHERE id_insumo = :id;
--   IF stock < 0 THEN RAISE; END IF;
--   COMMIT;
-- EXCEPTION WHEN OTHERS THEN ROLLBACK; RAISE;
-- END;

-- Demo minima portable:
-- UPDATE insumo SET stock = stock - 1 WHERE id_insumo = 1 AND stock >= 1;
-- Si SQL%ROWCOUNT = 0 -> no habia stock -> ROLLBACK de la factura.
```

**Pasos guiados del taller:**
1. Implementar bloque/proc que facture y descuente stock atomicamente.
2. Probar fallo a mitad (stock insuficiente) -> ROLLBACK.
3. Completar checklist tuning del PI.
4. Actualizar informe PI: seccion transacciones.

**Entregable:** Script transaccional + checklist tuning del PI (1 pag.)
**Criterios de exito:**
- Transaccion completa.
- Prueba ROLLBACK.
- Checklist tuning.
- Sección informe.

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
presencial); duracion 90-100 min dentro del bloque de 120.

## Proyecto Integrador VetCare DB

Hilo conductor de todas las clases regulares/autonomas. Avance formal en
Clase 11 (checkpoint) y entrega/sustentacion en Clase 15. Se sube a ExamLab
como Proyecto (individual por defecto; equipo de 2-3 solo si el docente lo autoriza); pesa 20% del Corte 3.
