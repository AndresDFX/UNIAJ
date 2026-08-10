# Solución Taller Clase 4 — C4 Containers + contratos

> DOCUMENTO DOCENTE — PRIVADO. No compartir en Clases/ ni Campus antes del cierre.

**Resumen:** Ejemplo 3 contenedores: web, api, db.

## Alineacion al enunciado estudiante
- Taller: `Clases/Clase 4 - Microservicios y arquitecturas distribuidas/Taller Clase 4 - CloudLite.docx`
- Hito PI: Diagramar componentes/servicios CloudLite y sus contratos
- Entregable: Diagrama C4 Container/Componentes v0.9 + 3 contratos API

## Solucion paso a paso
1. Containers WebApp, ApiReservas, DbAgenda.
2. Flechas HTTPS/SQL/SMTP etiquetadas.
3. 3 contratos API con errores.
4. Export PNG+.drawio.

## Ejemplo / artefactos esperados
- POST /api/reservas — 401/409
- DELETE /api/reservas/{id} — 404/403
- GET /api/disponibilidad — 400

## Rubrica corta / checklist de correccion
- [ ] 2-5 cajas (3)
- [ ] Flechas (2)
- [ ] Contratos (3)
- [ ] Export+informe (2)

## Errores frecuentes
- 12 microservicios teatro.
- Nombres distintos al Context.

## Entrega / politica
Entrega en ExamLab (https://examlab.lovable.app/) · gratis + navegador · sin cloud con tarjeta.
La UNIAJC no tiene campus virtual propio.
