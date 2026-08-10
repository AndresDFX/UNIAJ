# Solución Taller Clase 7 — Indices

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

**Resumen:** 2 indices justificados.

## Alineacion
- Taller: `Clases/Clase 7 - Indices y particionamiento/Taller PI - Clase 7 - VetCare.docx`
- Hito: >=2 indices justificados sobre tablas calientes del PI
- Entregable: Script CREATE INDEX + tabla justificacion consulta->indice

## Solucion paso a paso
1. Identificar 2 consultas frecuentes del PI que filtran o unen por una columna especifica (ej. "citas de un dia" filtra por fecha_hora; "historial de un dueno" filtra por id_dueno via mascota).
2. Crear los indices correspondientes, ej. CREATE INDEX idx_cita_fecha ON cita(fecha_hora); CREATE INDEX idx_mascota_dueno ON mascota(id_dueno) — con nombres que dejen claro que tabla/columna indexan.
3. Construir una tabla de dos columnas: consulta frecuente -> indice que la acelera, explicando en una frase por que esa columna tiene suficiente cardinalidad para justificar el indice.
4. Explicar por escrito el riesgo de sobre-indexar: cada indice adicional ralentiza INSERT/UPDATE/DELETE sobre esa tabla, asi que un indice sin una consulta real que lo use es costo puro sin beneficio — por eso el entregable exige justificar cada indice con su consulta.

## Ejemplo / SQL / artefactos
- Codigo/07_indices_vetcare.sql
- Script demo: `Kit docente/Clase 7/Codigo/07_indices_vetcare.sql`

## Rubrica corta
- [ ] Indices (4)
- [ ] Justificación (3)
- [ ] Riesgo (2)
- [ ] Evidencia (1)

## Errores frecuentes
- Sin consulta.
- Indexar todo.

Entrega en ExamLab.
