# Solución Taller Clase 3 — Procedimientos

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

**Resumen:** sp_agendar_cita con validación mascota activa.

## Alineacion
- Taller: `Clases/Clase 3 - Procedimientos almacenados/Taller PI - Clase 3 - VetCare.docx`
- Hito: >=1 procedimiento de negocio (agendar cita / registrar consulta)
- Entregable: Script proc + casos de prueba (captura o enlace Live SQL)

## Solucion paso a paso
1. Crear sp_agendar_cita con parametros IN (id_cita, id_mascota, fecha) y un parametro OUT (p_msg) para devolver el resultado a quien lo llame.
2. Antes de insertar, hacer SELECT activa FROM mascota WHERE id_mascota = p_id_mascota; si activa <> 'S', asignar p_msg := 'ERROR: mascota inactiva; no se agenda' y salir con RETURN sin tocar la tabla cita.
3. Si la validacion pasa, ejecutar el INSERT INTO cita y confirmar con COMMIT; asignar p_msg := 'OK: cita agendada' para que quien llamo el proc sepa que la operacion tuvo exito.
4. Ejecutar dos pruebas obligatorias: (1) caso OK con una mascota activa=S — debe insertar y devolver mensaje de exito; (2) caso error con una mascota activa=N o inexistente — debe rechazar sin insertar nada y devolver el mensaje de error correspondiente (usar EXCEPTION WHEN NO_DATA_FOUND para el caso de mascota inexistente).
5. Documentar la firma del proc como si fuera el contrato que usara la futura app: nombre, cada parametro con su tipo y direccion (IN/OUT), y el listado de mensajes de p_msg posibles — esto es exactamente lo que se reutiliza en el contrato de integracion de Clase 12.

## Ejemplo / SQL / artefactos
- Codigo/03_procs_vetcare.sql
- Script demo: `Kit docente/Clase 3/Codigo/03_procs_vetcare.sql`

## Rubrica corta
- [ ] Proc (3)
- [ ] Validación (3)
- [ ] Pruebas (2)
- [ ] Contrato (2)

## Errores frecuentes
- Sin validación.
- Solo captura.

Entrega en ExamLab.
