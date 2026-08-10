# Solución Taller Clase 8 — Transacciones

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

**Resumen:** Factura+stock con ROLLBACK.

## Alineacion
- Taller: `Clases/Clase 8 - Tuning y transacciones/Taller PI - Clase 8 - VetCare.docx`
- Hito: Transaccion de negocio (factura + stock) + notas de tuning
- Entregable: Script transaccional + checklist tuning del PI (1 pag.)

## Solucion paso a paso
1. Implementar un procedimiento (o bloque transaccional explicito) que inserte la factura, inserte el detalle_factura y descuente el stock del insumo en una sola transaccion: BEGIN...INSERT...INSERT...UPDATE stock...COMMIT.
2. Forzar deliberadamente un caso de fallo (ej. intentar descontar mas stock del disponible) y verificar que el ROLLBACK deshace TODO: ni la factura ni el detalle quedan registrados a medias — esa es la prueba real de atomicidad, no solo el caso feliz.
3. Completar el checklist de tuning: estadisticas actualizadas, existencia de indice sobre las columnas usadas en el JOIN/WHERE de esta transaccion, y verificar que la transaccion no queda abierta mas tiempo del necesario (sin operaciones manuales del usuario en medio del BEGIN/COMMIT).
4. Actualizar el informe del PI con la seccion de transacciones: que operacion se protegio, que prueba de fallo se ejecuto, y que se verifico despues del ROLLBACK (que el stock e historial quedaron exactamente como antes del intento fallido).

## Ejemplo / SQL / artefactos
- Codigo/08_transacciones_vetcare.sql
- Script demo: `Kit docente/Clase 8/Codigo/08_transacciones_vetcare.sql`

## Rubrica corta
- [ ] Transaccion (4)
- [ ] ROLLBACK (3)
- [ ] Checklist (2)
- [ ] Informe (1)

## Errores frecuentes
- Sin prueba fallo.
- Updates sueltos.

Entrega en ExamLab.
