# Solución Taller Clase 3 — Stub contenerizado

> DOCUMENTO DOCENTE — PRIVADO. No compartir en Clases/ ni Campus antes del cierre.

**Resumen:** Dockerfile mínimo + evidencia lab navegador.

## Alineacion al enunciado estudiante
- Taller: `Clases/Clase 3 - Virtualizacion y contenedores/Taller Clase 3 — Contenedor stub CloudLite.docx`
- Hito PI: Contenerizar un stub del servicio principal de CloudLite
- Entregable: Dockerfile (+ compose opcional) + captura/enlace lab navegador

## Solucion paso a paso
1. Servicio api-reservas.
2. Dockerfile slim+EXPOSE+CMD.
3. Stub /health 200.
4. Captura timestamp + sección Contenedores.

## Ejemplo / artefactos esperados
- FROM python:3.12-slim
- WORKDIR /app
- COPY app.py .
- EXPOSE 8080
- CMD ["python","app.py"]

## Rubrica corta / checklist de correccion
- [ ] Dockerfile (3)
- [ ] HTTP stub (2)
- [ ] Evidencia (3)
- [ ] Sin secretos (1)
- [ ] Informe (1)

## Errores frecuentes
- Keys en imagen.
- Sin captura ni archivo.

## Entrega / politica
Entrega en ExamLab (https://examlab.lovable.app/) · gratis + navegador · sin cloud con tarjeta.
La UNIAJC no tiene campus virtual propio.
