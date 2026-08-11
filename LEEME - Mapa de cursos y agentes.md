# UNIAJC · Mapa de cursos y agentes

Workspace docente: Institución Universitaria Antonio José Camacho.

**Docente:** Julian Andres Castaño Espinosa · `julianacastano@profesores.uniajc.edu.co`  
**Periodo vigente:** 2026-2 · **10/08/2026 – 22/11/2026**  
**Calendario maestro:** `config/calendario/semestre_2026_2.json`

## Cursos

| Carpeta | Oferta 2026-2 | Notas |
|---|---|---|
| `Programacion II/` | FI303204 · **341C** · mié **18:00–20:00** · Presencialidad asistida (120 min) | 15 clases · **reconstruido 2026-2** con `build_uniajc_prog2_all.py` · PI VetCare (Java) |
| `Seminario de Sistemas/` | FI303301 · **341C** · jue **18:00–20:00** · Presencialidad asistida (120 min) | 15 clases · **reconstruido 2026-2** con `build_uniajc_seminario_all.py` · PI VetCare (diseño: requisitos, UML, wireframes) |
| `Bases de Datos II/` | **641A-2** · lun **18:00–20:00** · Presencialidad asistida (120 min) | Curso nuevo · **FI303215** · 4 clases autónomas (festivos) · falta confirmación oficial de secretaría |
| `Arquitectura de Sistemas Computacionales/` | lun **10:00–12:00** · Presencialidad asistida (120 min) | Curso nuevo · **FI303380 · 6303C** · 4 clases autónomas · falta confirmación oficial de secretaría |
| `0. Base/` | — | Plantillas institucionales (Ing. Software 1) |

## Modalidad (regla única, 4 cursos)

**Presencialidad asistida**, idéntica en los 4 cursos:

| Sesión | Modalidad |
|---|---|
| **Clase 1** (encuadre) | **Presencial** síncrona |
| **Parciales** (5/10/15 mié-jue · 5/9/14 lun) | **Presencial** síncrona |
| Resto de clases regulares | **Virtual** síncrona |
| Festivos | **Clase autónoma** (único caso asincrónico) |

Fuente de verdad: `config/calendario/semestre_2026_2.json` → `regla_modalidad_sesion`.

## Evaluación teórica 2026-2 (todos los cursos activos)

Misma lógica que Acuerdos de Prog. II / Seminario: **30% / 30% / 40%** con **parcial al cierre de cada corte**.

| Corte | % | Ventana | Clases | Parcial | Desglose |
|---|---|---|---|---|---|
| 1 | 30% | 10/08–13/09 | 1–5 | Parcial 1 (Clase 5) | 10% Parcial · 10% Talleres o Quiz · 10% Asistencia |
| 2 | 30% | 14/09–18/10 | 6–10 | Parcial 2 (Clase 10) | 10% Parcial · 10% Talleres o Quiz · 10% Asistencia |
| 3 | 40% | 19/10–22/11 | 11–15 | Parcial 3 (Clase 15) | 15% Parcial · 20% Proyecto Integrador · 5% Asistencia |

Festivos = **clase autónoma** (no se omiten). Si el cierre de corte cae en festivo, el parcial se mueve a la última clase regular anterior (nunca en festivo).

## Estructura de carpetas por curso

```text
<Curso>/
  Clases/                         ← lo UNICO que se comparte con estudiantes
    Presentacion del Curso - ….pptx        (Sesion 0)
    Clase NN - <Tema>/Presentacion.pptx     (+ taller .docx)
    Proyecto Integrador/Enunciado ….docx
  Kit docente/                    ← privado
    Clase N/  guion (.md+.docx) · Quiz + CLAVE DOCENTE · Codigo/ · Capturas/
    Proyecto Integrador/Guia Docente PI ….docx|.md
  Parciales/                      ← enunciado + SOLUCION (nunca en Clases/)
  Plan curso/2026-2/              ← plan, calendario, cronograma, CSV
  Entregas docente/2026-2/        ← acuerdo, diagnostico, correo de bienvenida
```

Regla del dia de parcial: **solo evaluacion**, sin tema tecnico nuevo. El material del
parcial vive en `Parciales/`, nunca en `Clases/`.

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
# Presentacion del Curso (Sesion 0) — uno por curso
python config/slides/build_uniajc_prog2_curso.py
python config/slides/build_uniajc_seminario_curso.py
python config/slides/build_uniajc_bd2_curso.py
python config/slides/build_uniajc_arq_curso.py

# Material de clase (las 15 clases del curso)
python config/slides/build_uniajc_prog2_all.py         # datos en prog2_clases_data.py
python config/slides/build_uniajc_seminario_all.py     # datos en seminario_clases_data.py
python config/slides/build_uniajc_bd2_all.py
python config/slides/build_uniajc_arq_clases_batch.py

# Cada build *_all/batch genera ademas, por clase:
#   Kit docente/Clase N/Taller en ExamLab - Clase N (configuracion).md
# con el texto exacto de cada campo para crear el taller en la plataforma
# (tipo, enunciado, puntos, rubrica, setupSql, starter code). ExamLab NO importa
# preguntas desde archivo, por eso el entregable es un documento para pegar.
# Especificacion por clase: config/slides/<curso>_examlab_data.py
# Renderizador compartido:  config/slides/examlab_talleres.py
# OJO BD II: el SQL de ExamLab es PostgreSQL (PGlite), no Oracle.

# (build_uniajc_prog2_clase01.py, build_uniajc_clase01_prog2_seminario.py y
#  build_uniajc_seminario_clase01.py estan SUPERSEDIDOS: la Clase 1 sale de los
#  builds *_all.py. Se conservan por historia y abortan si se ejecutan.)

# Proyecto Integrador (los 4 cursos) y parciales
python config/slides/build_uniajc_pi_2026_2.py
python config/parciales/build_parciales_2026_2.py

# Capturas de "salida esperada" de los guiones
python config/slides/mockups.py

# Guion suelto .md -> .docx
python config/slides/guion_md_a_docx.py "<ruta al guion>.md"

# Calendario del periodo  (OJO: regenera los 4 Acuerdos Pedagogicos)
python config/calendario/generar_semestre_2026_2.py
```

## Convención de material

- Nomenclatura **Clase N** (no «Sesión» CUN).
- **La UNIAJC no tiene Campus Virtual/LMS.** Canal de entrega = **ExamLab** (`examlab.lovable.app/app`), que no es oficial de la universidad. Nunca escribir “Campus Virtual” ni incluir listado de estudiantes (privado).
- **Presentación del curso:** docente + oferta (grupo/periodo/horario/URL en **negrita**) + evaluación + cronograma.
- **PPTX de clase:** solo tema de esa clase + nº discreto («Clase N»). Sin fechas de periodo, sin mapa completo del curso, sin bio.
- **Guion de clase:** en `Kit docente/Clase N/` (privado docente). Fundamento + minuto a minuto + práctica + entregable de hoy. Sin carpeta `Guiones/`.
- **Acuerdo pedagógico:** uno por semestre; no borrar periodos anteriores; prefill en `Entregas docente/2026-2/`.
- No borrar `.gslides`/`.gdoc`; generar `.pptx`/`.docx` en paralelo.
- Marca: [uniajc.edu.co](https://www.uniajc.edu.co/) · `#095292` / `#269CCB` / `#FFD000`.
