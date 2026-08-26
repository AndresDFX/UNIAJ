# UNIAJC · Mapa de cursos y agentes

Workspace docente: Institución Universitaria Antonio José Camacho.

**Docente:** Julian Andres Castaño Espinosa · `julianacastano@profesores.uniajc.edu.co`  
**Periodo vigente:** 2026-2 · **24/08/2026 – 22/11/2026** (semestre acortado por decisión institucional; la fecha fin no se movió)  
**Sesiones:** **13 sesiones** por curso que cubren los **15 temas** del microcurrículo — **2 sesiones son dobles** (dos temas afines en un bloque de 120 min). Las carpetas `Clases/Clase N - …` y `Kit docente/Clase N/` **no se renumeraron**: el mapeo Sesión → Clase(s) de material está en `<Curso>/Plan curso/2026-2/CALENDARIO_2026-2.md`.  
**Calendario maestro:** `config/calendario/semestre_2026_2.json`

## Cursos

| Carpeta | Oferta 2026-2 | Notas |
|---|---|---|
| `Programacion II/` | FI303204 · **341C** · mié **18:00–20:00** · **Virtual** (120 min) | 13 sesiones / 15 temas (sesiones 8 y 10 dobles) · sin festivos · **reconstruido 2026-2** con `build_uniajc_prog2_all.py` · PI VetCare (Java) |
| `Seminario de Sistemas/` | FI303301 · **341C** · jue **18:00–20:00** · **Virtual** (120 min) | 13 sesiones / 15 temas (sesiones 8 y 10 dobles) · sin festivos · **reconstruido 2026-2** con `build_uniajc_seminario_all.py` · PI VetCare (diseño: requisitos, UML, wireframes) |
| `Bases de Datos II/` | **641A-2** · lun **18:00–20:00** · **Virtual** (120 min) | Curso nuevo · **FI303215** · 13 sesiones / 15 temas (sesiones 7 y 10 dobles) · 2 sesiones autónomas (12/10 y 02/11) · sesión 13 (16/11) = sustentaciones del PI · falta confirmación oficial de secretaría |
| `Arquitectura de Sistemas Computacionales/` | lun **10:00–12:00** · **Virtual** (120 min) | Curso nuevo · **FI303380 · 6303C** · 13 sesiones / 15 temas (sesiones 7 y 10 dobles) · 2 sesiones autónomas (12/10 y 02/11) · sesión 13 (16/11) = sustentaciones del PI · falta confirmación oficial de secretaría |
| `0. Base/` | — | Plantillas institucionales (Ing. Software 1) |

## Modalidad (regla única, 4 cursos)

**Virtual**, idéntica en los 4 cursos. **No hay sesiones presenciales en el campus**, ni
siquiera los parciales:

| Sesión | Modalidad |
|---|---|
| **Sesión 1** (encuadre) | **Virtual** síncrona (Google Meet) |
| **Parciales** (mié-jue: **5/9/13** · lun: **5/9/12**) | **Virtual** síncrona |
| Resto de sesiones regulares | **Virtual** síncrona |
| Festivos | **Clase autónoma** (único caso asincrónico) |
| **Sesión 13 de lunes** (16/11, BD II y Arquitectura) | **Sustentaciones del PI**, virtual en vivo (no es parcial) |

**Cada sesión tiene su propio enlace de Meet**, dentro de la invitación de Calendar de esa
sesión: no hay un enlace único del curso (ver `Manuales/01` y `_nota_meet` en el JSON). Antes
hubo una sola sala para toda la serie, y antes de eso la oferta fue «Presencialidad asistida»
(Sesión 1 y parciales presenciales); si un documento todavía dice cualquiera de las dos cosas,
está desactualizado.

Fuente de verdad: `config/calendario/semestre_2026_2.json` → `regla_modalidad_sesion`.

## Evaluación teórica 2026-2 (todos los cursos activos)

Misma lógica que Acuerdos de Prog. II / Seminario: **30% / 30% / 40%** con **parcial al cierre de cada corte**.

| Corte | % | Ventana | Sesiones | Parcial | Desglose |
|---|---|---|---|---|---|
| 1 | 30% | 24/08–27/09 | 1–5 | Parcial 1 (Sesión 5) | 10% Parcial · 10% Talleres o Quiz · 10% Asistencia |
| 2 | 30% | 28/09–25/10 | 6–9 | Parcial 2 (Sesión 9) | 10% Parcial · 10% Talleres o Quiz · 10% Asistencia |
| 3 | 40% | 26/10–22/11 | 10–13 | Parcial 3 (Sesión 13 mié-jue · Sesión 12 lun) | 15% Parcial · 20% Proyecto Integrador · 5% Asistencia |

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
  Plan curso/<periodo>/           ← plan, calendario, cronograma, CSV de eventos,
                                     CORREO_BIENVENIDA y la nomina (fuera de git)
  Entregas docente/<periodo>/     ← SOLO lo que se entrega a la universidad:
                                     acuerdo pedagogico y diagnostico
```

`Manuales/` (raiz de `Cursos`) tiene los procedimientos que se ejecutan **fuera del repo**:
crear los eventos del calendario e invitar a los estudiantes, e instalar el Apps Script que
archiva las grabaciones de Meet. Son generales: sirven para cualquier periodo.

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
| Iconos de herramientas | `config/slides/assets/herramientas/` + `normalizar_iconos.py` |
| Skill transcribir | `.claude/skills/transcribir-video/` |
| Limpieza `desktop.ini` de Drive | `config/git/limpiar_desktop_ini.py` (hook `SessionStart`) |

## Alistar el semestre (calendario, Meet, invitaciones, grabaciones)

```bash
python config/calendario/generar_semestre_2026_2.py         # calendario, correo, CSV, acuerdos
python config/calendario/generar_eventos_calendario.py      # nominas, planillas, .ics
python config/calendario/generar_apps_script_encuentros.py  # .gs de encuentros (por curso + consolidado)
python config/calendario/validar_calendario.py              # invariantes; sale 1 si algo falla
bash   config/calendario/pruebas_apps_script/probar.sh      # ejecuta los .gs contra un simulacro
```

Fuente de verdad: `config/calendario/semestre_2026_2.json` (fechas, sesiones, parciales,
festivos y carpetas de Drive). Se corrige ahi y se regenera.

**Los encuentros no se crean importando un `.ics`**: importar deja los invitados dentro del
evento pero Google no envia las invitaciones. Se crean con el Apps Script generado, que usa
la API de Calendar (`sendUpdates: 'all'`) y le da a **cada sesión su propia sala de Meet**
del curso. Las sesiones autonomas van al calendario pero sin Meet.

El generador emite **dos** `.gs` de la misma plantilla: uno por curso, en
`<Curso>/Plan curso/<periodo>/_privado/`, y **uno consolidado** con todos los cursos del
periodo en `_privado/<periodo>/`, con las funciones de cada curso y cuatro `*TodosLosCursos`.
Los `.gs` llevan correos de estudiantes y no se versionan; los punteros visibles son
`LEEME - Apps Script del curso.md` (por curso) y `LEEME - Apps Script del semestre.md` (raiz).

Procedimiento paso a paso: **`Manuales/`** (01 alistar un curso · 02 archivar grabaciones).
Estan escritos con `<periodo>` y `<Curso>`: sirven en cualquier semestre.

## Builds / regeneración

```bash
# Presentacion del Curso (Sesion 0) — uno por curso
python config/slides/build_uniajc_prog2_curso.py
python config/slides/build_uniajc_seminario_curso.py
python config/slides/build_uniajc_bd2_curso.py
python config/slides/build_uniajc_arq_curso.py

# Material de clase (las 15 clases de material · se dictan en 13 sesiones)
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

# Iconos de herramientas de las diapositivas
# --ingesta importa los archivos que dejes en la raiz (png/jpg/svg, cualquier
# nombre) con el nombre canonico y archiva el original en assets/herramientas/
# _originales/. Sin --ingesta solo recorta y recentra lo ya instalado, que es lo
# que evita que un favicon de 32 px salga como una mota en la tarjeta.
python config/slides/normalizar_iconos.py --ingesta

# Guion suelto .md -> .docx
python config/slides/guion_md_a_docx.py "<ruta al guion>.md"

# Calendario del periodo  (OJO: regenera los 4 Acuerdos Pedagogicos)
python config/calendario/generar_semestre_2026_2.py
```

## El repo vive en Google Drive: `desktop.ini` rompe git

Sintoma, al hacer `git pull` / `fetch` / `push`:

```text
fatal: bad object refs/desktop.ini
error: github-personal:AndresDFX/UNIAJ.git did not send all necessary objects
```

**Causa.** Google Drive escribe un `desktop.ini` oculto en cada carpeta que
sincroniza (metadata de shell: el icono de Drive, apunta a `GoogleDriveFS.exe`).
Cuando cae dentro de `.git/refs/`, git rompe: **lee todo archivo bajo `refs/` como
si fuera una referencia**, asi que `.git/refs/desktop.ini` pasa a ser un ref
llamado `refs/desktop.ini` cuyo contenido no es un SHA.

**`.gitignore` no lo puede arreglar.** En el arbol de trabajo si esta ignorado
(linea 57) y ahi no molesta; pero git **nunca** aplica reglas de ignore a su propio
directorio `.git/`. La unica salida es borrarlos. Tampoco sirve crear un
`desktop.ini` señuelo: el driver de Drive rechaza que otro proceso escriba con ese
nombre, solo lo escribe el.

**Arreglo:**

```bash
python config/git/limpiar_desktop_ini.py     # o, a mano:  find .git -iname desktop.ini -delete
```

Borra solo archivos llamados `desktop.ini` dentro del git-dir, y ademas las
carpetas vacias que quedan bajo `refs/heads/` por ramas ya borradas (son imanes de
`desktop.ini`). Preserva `refs/heads`, `refs/tags` y `refs/remotes`, que git espera.
Es idempotente y siempre sale con codigo 0.

Corre **automatico al iniciar cada sesion** de Claude Code por el hook
`SessionStart` de `.claude/settings.json`. En una terminal propia hay que correrlo
a mano, o cuando aparezca el error.

Los `desktop.ini` del arbol de trabajo (unos 400) son inofensivos: estan ignorados.

## Convención de material

- Nomenclatura **Clase N** (no «Sesión» CUN).
- **La UNIAJC no tiene Campus Virtual/LMS.** Canal de entrega = **ExamLab** (`https://uniaj.examlab.workers.dev/`), que **no es oficial de la universidad**; ahi van asistencia, talleres, quices/parciales y la entrega del PI. Nunca escribir “Campus Virtual” ni incluir listado de estudiantes (privado).
- **Presentación del curso:** docente + oferta (grupo/periodo/horario/URL en **negrita**) + evaluación + cronograma.
- **PPTX de clase:** solo tema de esa clase + nº discreto («Clase N»). Sin fechas de periodo, sin mapa completo del curso, sin bio.
- **Guion de clase:** en `Kit docente/Clase N/` (privado docente). Fundamento + minuto a minuto + práctica + entregable de hoy. Sin carpeta `Guiones/`.
- **Acuerdo pedagógico:** uno por semestre; no borrar periodos anteriores; prefill en `Entregas docente/2026-2/`.
- No borrar `.gslides`/`.gdoc`; generar `.pptx`/`.docx` en paralelo.
- Marca: [uniajc.edu.co](https://www.uniajc.edu.co/) · `#095292` / `#269CCB` / `#FFD000`.
