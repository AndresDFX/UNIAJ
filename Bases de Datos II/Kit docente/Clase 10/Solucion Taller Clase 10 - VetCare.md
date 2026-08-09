# Solución Taller Clase 10 — Concurrencia

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

**Resumen:** 2 escenarios + mitigacion.

## Alineacion
- Taller: `Clases/Clase 10 - Control de concurrencia/Taller PI - Clase 10 - VetCare.docx`
- Hito: Escenarios de concurrencia del PI documentados
- Entregable: Informe corto: 2 escenarios (cita doble / stock) + mitigacion

## Solucion paso a paso
1. Narrar el escenario de doble reserva con linea de tiempo explicita: T1 lee la franja como libre en el segundo 0, T2 lee la misma franja como libre en el segundo 1 (antes de que T1 confirme), ambas insertan y quedan dos citas para el mismo veterinario/franja.
2. Narrar el escenario de doble descuento de stock con la misma logica T1/T2: dos facturas leen el mismo stock disponible antes de que ninguna confirme su UPDATE, y el stock final queda incorrecto (mayor de lo que debería haberse descontado, o incluso negativo).
3. Proponer la mitigacion SQL concreta para cada escenario: UNIQUE(id_veterinario, fecha_hora) para que el segundo INSERT de cita falle automaticamente; y para el stock, un UPDATE con condicion (UPDATE insumo SET stock = stock - x WHERE id_insumo = y AND stock >= x) que falla/no afecta filas si ya no alcanza, en vez de restar a ciegas.
4. Agregar la seccion de concurrencia al informe del PI explicando, en lenguaje simple, por que un simple "usar transacciones" no basta sin la restriccion UNIQUE o la condicion en el UPDATE, y que mecanismo especifico eligio el equipo para VetCare.

## Ejemplo / SQL / artefactos
- Codigo/10_concurrencia_vetcare.sql
- Script demo: `Kit docente/Clase 10/Codigo/10_concurrencia_vetcare.sql`

## Rubrica corta
- [ ] Cita (3)
- [ ] Stock (3)
- [ ] Mitigacion (3)
- [ ] Informe (1)

## Errores frecuentes
- Sin T1/T2.
- Mitigacion vaga.

Campus Virtual UNIAJC.
