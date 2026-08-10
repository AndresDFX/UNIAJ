# Solución Taller Clase 2 — Roles VetCare

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

**Resumen:** 4 roles + matriz least privilege.

## Alineacion
- Taller: `Clases/Clase 2 - Administracion de bases de datos/Taller PI - Clase 2 - VetCare.docx`
- Hito: Plan de roles/privilegios de VetCare
- Entregable: Documento Roles_VetCare + script GRANT/REVOKE (o plan equivalente)

## Solucion paso a paso
1. Definir los 4 roles minimos: ADMIN_BD (DDL + gestion de roles), RECEPCION (opera citas y datos de contacto), VETERINARIO (registra consultas), AUDITOR (solo lectura sobre todo lo sensible).
2. Construir la matriz rol x objeto x privilegio: por cada rol, listar exactamente que tabla y que operacion (SELECT/INSERT/UPDATE/DELETE/EXECUTE) tiene permitida — no "acceso general", sino privilegio por objeto.
3. RECEPCION puede SELECT/INSERT/UPDATE sobre cita y SELECT sobre mascota/dueno, pero NUNCA DELETE sobre historial clinico ni sobre consulta — solo un veterinario o admin puede borrar ese tipo de registro.
4. AUDITOR recibe unicamente SELECT sobre las tablas sensibles (cita, consulta, factura); ningun privilegio de escritura, ni siquiera sobre datos "poco importantes", porque su funcion es verificar, no operar.
5. Redactar la politica de altas/bajas de usuarios en media pagina: quien autoriza crear un usuario nuevo, que rol se le asigna por defecto, y que pasa con sus privilegios el dia que deja de trabajar en la clinica (revocacion inmediata, no "despues").

## Ejemplo / SQL / artefactos
- Codigo/02_roles_vetcare.sql
- Script demo: `Kit docente/Clase 2/Codigo/02_roles_vetcare.sql`

## Rubrica corta
- [ ] 4 roles (2)
- [ ] Matriz (3)
- [ ] Least privilege (3)
- [ ] Política (2)

## Errores frecuentes
- Todos DBA.
- Sin justificar.

Entrega en ExamLab.
