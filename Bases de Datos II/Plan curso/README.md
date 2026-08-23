# Plan curso — información general vs periodo

## Raíz (`Plan curso/`)
Documentación **general** de la asignatura (no atada a un semestre):
- Microcurrículo oficial
- Plan de curso institucional (plantilla / oficial)

## Periodo `2026-2/`
Versión **puntual** de esta oferta (24/08/2026 – 22/11/2026 · 13 sesiones, 15 temas):
- `PLAN_DE_CURSO_2026-2.md` — plan operativo (clases, fechas, cortes, modalidad)
- `CALENDARIO_2026-2.md` — calendario del periodo
- `calendario_eventos_2026-2.csv` — eventos con detalle docente
- `eventos_calendario_2026-2.csv` — eventos importables a Google Calendar
- `CORREO_BIENVENIDA - <Curso> - 2026-2.md` — correo de bienvenida al grupo
  (va aquí, no en `Entregas docente/`, que es solo la entrega institucional)

- `LEEME - Apps Script del curso.md` — dónde está el `.gs` que crea los encuentros
  (el `.gs` vive en `_privado/` y no se versiona: lleva correos de estudiantes)
- `_privado/` — derivado de la nómina (`.ics`, nómina normalizada, planilla de
  asistencia, el `.gs` de encuentros). **Datos personales: no se versiona.**

Futuros periodos: crear `Plan curso/2027-1/`, etc., sin mover el material general de la raíz.

## Cómo se operan los eventos y el correo

El procedimiento (importar los eventos, invitar a los estudiantes, enviar el correo)
está en [`Manuales/`](../../Manuales/LEEME.md), en la raíz de `Cursos`. Es general:
sirve para cualquier periodo.
