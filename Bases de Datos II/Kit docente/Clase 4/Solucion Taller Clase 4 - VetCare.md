# Solución Taller Clase 4 — Fn/trigger/backup

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

**Resumen:** Funcion + trigger + plan respaldo.

## Alineacion
- Taller: `Clases/Clase 4 - Funciones disparadores seguridad respaldo/Taller PI - Clase 4 - VetCare.docx`
- Hito: >=1 funcion + >=1 trigger + borrador plan de respaldo
- Entregable: Scripts funcion/trigger + Plan_Backup_VetCare (1 pag.)

## Solucion paso a paso
1. Crear fn_precio_base(p_especie) que RETURN un valor NUMBER util al PI (ej. tarifa base segun especie), verificable con SELECT fn_precio_base('CANINO') FROM dual — una funcion se prueba dentro de un SELECT, no con CALL.
2. Crear trg_audit_cancelacion_cita (AFTER UPDATE ON cita WHEN estado cambia a CANCELADA) que inserte una fila en una tabla de auditoria con usuario, fecha y el id de la cita cancelada — sin que la app tenga que acordarse de registrar nada explicitamente.
3. Redactar el plan de respaldo con las 3 variables que lo hacen verificable: frecuencia (ej. diaria a las 2am), retencion (ej. 7 copias diarias + 4 semanales), y prueba de restore (ej. una vez al mes se restaura en un ambiente de prueba y se valida que los datos coinciden).
4. Actualizar el checklist del PI marcando explicitamente: funcion creada y probada, trigger creado y disparado al menos una vez en pruebas, plan de respaldo redactado con las 3 variables — no basta con "en progreso" sin evidencia.

## Ejemplo / SQL / artefactos
- Codigo/04_func_trigger_backup.sql
- Script demo: `Kit docente/Clase 4/Codigo/04_func_trigger_backup.sql`

## Rubrica corta
- [ ] Funcion (2)
- [ ] Trigger (3)
- [ ] Backup (3)
- [ ] Checklist (2)

## Errores frecuentes
- Trigger vacio.
- Backup sin restore.

Campus Virtual UNIAJC.
