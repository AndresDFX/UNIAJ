# UNIAJC · Mapa de cursos y agentes

Workspace docente: Institución Universitaria Antonio José Camacho.

**Docente:** Julian Andres Castaño Espinosa · `julianacastano@profesores.uniajc.edu.co`  
**Periodo vigente:** 2026-2 · **10/08/2026 – 22/11/2026**  
**Calendario maestro:** `config/calendario/semestre_2026_2.json`

## Cursos

| Carpeta | Oferta 2026-2 | Notas |
|---|---|---|
| `Programacion II/` | FI303204 · **341C** · mié **18:00–20:00** (120 min) | 15 clases · Acuerdo 2026-2 prellenado · material previo 2026-1 conservado |
| `Seminario de Sistemas/` | FI303301 · **341C** · jue **18:00–20:00** (120 min) | 15 clases · Acuerdo 2026-2 prellenado |
| `Bases de Datos II/` | **641A-2** · lun **18:00–20:00** · Presencialidad asistida (120 min) | Curso nuevo · código oficial pendiente · 4 clases autónomas (festivos) |
| `Arquitectura de Sistemas Computacionales/` | lun **10:00–12:00** · Presencialidad asistida (120 min) | Curso nuevo · grupo/código pendientes · 4 clases autónomas |
| `0. Base/` | — | Plantillas institucionales (Ing. Software 1) |

## Evaluación teórica 2026-2 (todos los cursos activos)

Misma lógica que Acuerdos de Prog. II / Seminario: **30% / 30% / 40%** con **parcial al cierre de cada corte**.

| Corte | % | Ventana | Clases | Parcial | Desglose |
|---|---|---|---|---|---|
| 1 | 30% | 10/08–13/09 | 1–5 | Parcial 1 (Clase 5) | 10% Parcial · 10% Talleres/Quiz · 10% Asistencia |
| 2 | 30% | 14/09–18/10 | 6–10 | Parcial 2 (Clase 10) | 10% Parcial · 10% Talleres/Quiz · 10% Asistencia |
| 3 | 40% | 19/10–22/11 | 11–15 | Parcial 3 (Clase 15) | 15% Parcial · 20% Proyecto Integrador · 5% Asistencia |

Festivos = **clase autónoma** (no se omiten). Si el cierre de corte cae en festivo, el parcial va en esa ventana autónoma / Campus Virtual.

## Stack de agente

| Pieza | Ruta |
|---|---|
| Agente generador | `.claude/agents/disenador-curricular-uniajc.md` (+ espejo `.cursor/agents/`) |
| Agente dudas | `.claude/agents/uniajc-dudas-material.md` (+ espejo `.cursor/agents/`) |
| Regla Cursor | `.cursor/rules/uniajc-docente.mdc` |
| Perfil marca | `config/universidades/uniajc.json` |
| Calendario periodo | `config/calendario/semestre_2026_2.json` |
| Motor slides | `config/slides/uniajc_slides_engine.py` |
| Skill transcribir | `.claude/skills/transcribir-video/` |

## Builds / regeneración

```bash
python config/slides/build_uniajc_prog2_curso.py
python config/slides/build_uniajc_prog2_clase01.py
python config/slides/guion_md_a_docx.py "Programacion II/Kit docente/Clase 1/Guion Docente Clase 1 - Introduccion a POO.md"
python config/calendario/generar_semestre_2026_2.py
```

## Convención de material

- Nomenclatura **Clase N** (no «Sesión» CUN).
- Plataforma = **Campus Virtual UNIAJC** (nunca “LMS” como nombre · nunca CDigital).
- **Presentación del curso:** docente + oferta (grupo/periodo/horario/URL en **negrita**) + evaluación + cronograma.
- **PPTX de clase:** solo tema de esa clase + nº discreto («Clase N»). Sin fechas de periodo, sin mapa completo del curso, sin bio.
- **Guion de clase:** en `Kit docente/Clase N/` (privado docente). Fundamento + minuto a minuto + práctica + entregable de hoy. Sin carpeta `Guiones/`.
- **Acuerdo pedagógico:** uno por semestre; no borrar periodos anteriores; prefill en `Entregas docente/2026-2/`.
- No borrar `.gslides`/`.gdoc`; generar `.pptx`/`.docx` en paralelo.
- Marca: [uniajc.edu.co](https://www.uniajc.edu.co/) · `#095292` / `#269CCB` / `#FFD000`.
