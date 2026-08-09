# -*- coding: utf-8 -*-
"""Parche one-shot: Sesión 0 vs Clase 1 + TIMELINE con tildes."""
from pathlib import Path
import re

ROOT = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos")
SLIDES = ROOT / ".config" / "slides"


def _read(p: Path) -> str:
    raw = p.read_bytes()
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def _write(p: Path, text: str):
    p.write_text(text, encoding="utf-8", newline="\n")


def patch_texto(text: str, pairs):
    for a, b in pairs:
        text = text.replace(a, b)
    return text


# --- Curso builds: wording Sesión 0 / Clase 1 ---
CURSO_PAIRS_COMMON = [
    (
        "Clase 1: Presentación del curso + **diagnóstico de conocimientos previos** + arranque del tema.",
        "**Sesión 0** (archivo aparte): Presentación del curso (logística, acuerdo, Padlet, evaluación, CONTENIDO).\n"
        "            **Clase 1** (tema): **diagnóstico de conocimientos previos** + arranque temático.",
    ),
    (
        "Clase 1: Presentacion del curso + **diagnostico de conocimientos previos** + arranque del tema.",
        "**Sesión 0** (archivo aparte): Presentación del curso (logística, acuerdo, Padlet, evaluación, CONTENIDO).\n"
        "            **Clase 1** (tema): **diagnóstico de conocimientos previos** + arranque temático.",
    ),
]

# Mojibake variants that appear in some curso builds
CURSO_PAIRS_MOJI = [
    (
        "Clase 1: Presentaci\u00f3n del curso + **diagn\u00f3stico de conocimientos previos** + arranque del tema.",
        "**Sesión 0** (archivo aparte): Presentación del curso (logística, acuerdo, Padlet, evaluación, CONTENIDO).\n"
        "            **Clase 1** (tema): **diagnóstico de conocimientos previos** + arranque temático.",
    ),
]


def patch_curso_build(path: Path, clase1_tema: str, aclaracion: str, sesion0_tema: str, fecha1: str):
    t = _read(path)
    # Normalize common mojibake for key phrases if file is damaged
    t2 = t
    # Replace methodology bullet (try several encodings of the same sentence)
    patterns = [
        r"Clase 1: Presentaci[oó\ufffd]+n del curso \+ \*\*diagn[oó\ufffd]+stico de conocimientos previos\*\* \+ arranque del tema\.",
        r"Clase 1: Presentacion del curso \+ \*\*diagnostico de conocimientos previos\*\* \+ arranque del tema\.",
    ]
    repl_metod = (
        "**Sesión 0** (archivo aparte): Presentación del curso (logística, acuerdo, Padlet, evaluación, CONTENIDO). "
        "**Clase 1** (tema): **diagnóstico de conocimientos previos** + arranque temático."
    )
    for pat in patterns:
        t2 = re.sub(pat, repl_metod, t2)

    # CONTENIDO item n=1
    t2 = re.sub(
        r'\{\s*"n"\s*:\s*1\s*,\s*"tema"\s*:\s*"[^"]*"\s*,\s*"fecha"\s*:\s*"' + re.escape(fecha1) + r'"\s*\}',
        '{"n": 1, "tema": "' + clase1_tema + '", "fecha": "' + fecha1 + '"}',
        t2,
        count=1,
    )

    # Insert Sesión 0 before n=1 in contenido list if missing
    if "Sesión 0" not in t2 and "Sesion 0" not in t2:
        t2 = t2.replace(
            '{"n": 1, "tema": "' + clase1_tema + '", "fecha": "' + fecha1 + '"}',
            '{"n": 0, "kind": "sesion0", "tema": "' + sesion0_tema + '", "fecha": "' + fecha1 + '"},\n'
            '            {"n": 1, "tema": "' + clase1_tema + '", "fecha": "' + fecha1 + '"}',
            1,
        )

    # aclaracion box
    t2 = re.sub(
        r"\('aclaracion',\s*'Clase 1:[^']*'\)",
        "('aclaracion', '" + aclaracion + "')",
        t2,
        count=1,
    )
    t2 = re.sub(
        r'\("aclaracion",\s*"Clase 1:[^"]*"\)',
        '("aclaracion", "' + aclaracion + '")',
        t2,
        count=1,
    )

    # Add sub= to contenido_clases_slides if not present
    if "contenido_clases_slides(" in t2 and "sub=" not in t2.split("contenido_clases_slides(")[1][:800]:
        t2 = re.sub(
            r"(contenido_clases_slides\(\s*prs,\s*\[[\s\S]*?\]\s*,\s*title=\"CONTENIDO\",\s*idx_start=\d+)",
            r'\1,\n        sub="Día 1: Sesión 0 (Presentación del curso, archivo aparte) + Clase 1 (diagnóstico · tema)"',
            t2,
            count=1,
        )

    if t2 != t:
        _write(path, t2)
        print("OK curso", path.name)
    else:
        print("SKIP/unchanged?", path.name)
        # still write cleaned if we want — report key presence
        print("  has Sesión 0:", "Sesión 0" in t2 or "Sesion 0" in t2)
        print("  clase1 tema snippet:", clase1_tema[:40] in t2)


def patch_part2_timeline():
    p = SLIDES / "part2.py"
    t = _read(p)
    old = '''TIMELINE = {
1: [("0-10","Gancho + entregable"),("10-35","Diagnostico previos"),
    ("35-70","Teoria visual cloud"),("70-105","Taller ficha + C4"),("105-120","Checklist · quiz")],
2: [("Lectura","Slides + enunciado"),("Matriz","IaaS/PaaS/SaaS"),("ADR-001","Decision"),("Entrega","Informe")],
3: [("0-15","Encuadre"),("15-45","VM vs contenedor"),("45-60","Demo lab"),("60-105","Taller stub"),("105-120","Quiz")],
4: [("0-15","Encuadre"),("15-50","Monolito vs micro"),("50-65","Demo C4"),("65-105","Taller"),("105-120","Cierre")],
6: [("0-15","Encuadre"),("15-50","STRIDE-lite"),("50-100","Taller"),("100-120","Secretos + quiz")],
7: [("0-15","Encuadre"),("15-50","Zonas + storage"),("50-65","Demo"),("65-105","Taller"),("105-120","Quiz")],
8: [("0-15","Encuadre"),("15-55","CI/CD + YAML"),("55-100","Taller Actions"),("100-120","Quiz")],
10: [("Lectura","Slides"),("Tabla","B/M/A"),("Sostenibilidad","3 acciones"),("Entrega","1 pagina")],
11: [("0-15","Checklist"),("15-50","Revision"),("50-100","Paquete v1"),("100-120","Backlog")],
12: [("0-20","Metricas"),("20-50","Bottlenecks"),("50-100","Pitch"),("100-120","Paquete")],
13: [("Lectura","Slides"),("Politica","Triggers"),("Impacto","Costo"),("Entrega","Seccion")],
15: [("Prep","Paquete"),("Pitch","5-8 min"),("Q&A","3+3"),("Cierre","Reflexion")],
}'''
    new = '''TIMELINE = {
1: [("0-10","Encuadre + entregable PI"),("10-35","Diagnóstico de previos"),
    ("35-70","Teoría visual cloud"),("70-105","Taller ficha + C4"),("105-120","Checklist · quiz")],
2: [("Lectura","Slides + enunciado"),("Matriz","IaaS/PaaS/SaaS"),("ADR-001","Decisión"),("Entrega","Informe")],
3: [("0-15","Encuadre"),("15-45","VM vs contenedor"),("45-60","Demo lab"),("60-105","Taller stub"),("105-120","Quiz")],
4: [("0-15","Encuadre"),("15-50","Monolito vs micro"),("50-65","Demo C4"),("65-105","Taller"),("105-120","Cierre")],
6: [("0-15","Encuadre"),("15-50","STRIDE-lite"),("50-100","Taller"),("100-120","Secretos + quiz")],
7: [("0-15","Encuadre"),("15-50","Zonas + storage"),("50-65","Demo"),("65-105","Taller"),("105-120","Quiz")],
8: [("0-15","Encuadre"),("15-55","CI/CD + YAML"),("55-100","Taller Actions"),("100-120","Quiz")],
10: [("Lectura","Slides"),("Tabla","B/M/A"),("Sostenibilidad","3 acciones"),("Entrega","1 página")],
11: [("0-15","Checklist"),("15-50","Revisión"),("50-100","Paquete v1"),("100-120","Backlog")],
12: [("0-20","Métricas"),("20-50","Bottlenecks"),("50-100","Pitch"),("100-120","Paquete")],
13: [("Lectura","Slides"),("Política","Triggers"),("Impacto","Costo"),("Entrega","Sección")],
15: [("Prep","Paquete"),("Pitch","5-8 min"),("Q&A","3+3"),("Cierre","Reflexión")],
}'''
    if old in t:
        _write(p, t.replace(old, new))
        print("OK part2 TIMELINE")
    else:
        # softer replace accents only
        t2 = t
        for a, b in [
            ('"Diagnostico previos"', '"Diagnóstico de previos"'),
            ('"Teoria visual cloud"', '"Teoría visual cloud"'),
            ('"Decision"', '"Decisión"'),
            ('"1 pagina"', '"1 página"'),
            ('"Revision"', '"Revisión"'),
            ('"Metricas"', '"Métricas"'),
            ('"Politica"', '"Política"'),
            ('"Seccion"', '"Sección"'),
            ('"Reflexion"', '"Reflexión"'),
            ('("0-10","Gancho + entregable")', '("0-10","Encuadre + entregable PI")'),
        ]:
            t2 = t2.replace(a, b)
        if t2 != t:
            _write(p, t2)
            print("OK part2 TIMELINE (soft)")
        else:
            print("WARN part2 TIMELINE not patched")


def patch_part3_guion():
    p = SLIDES / "part3.py"
    t = _read(p)
    t2 = t
    t2 = t2.replace(
        'title_tl = "Ruta autonoma de hoy" if c["tipo"] == "autonoma" else "Mapa del bloque de hoy (120 min)"',
        'title_tl = "Ruta autónoma de hoy" if c["tipo"] == "autonoma" else "Mapa del bloque de hoy (120 min)"',
    )
    old_plan1 = '''        plan = (
            f"### 0-25 Presentacion del curso (PPTX aparte)\\n"
            f"Abre Presentacion del Curso. Acuerdo, Padlet, evaluacion, CONTENIDO. "
            f"Di: diagnostico de conocimientos previos + arranque CloudLite.\\n\\n"
            f"### 25-50 Diagnostico (instrumento + slides Diagnostico)\\n"
            f"Prueba Diagnostica del Kit. Silencio 20-25 min. "
            f"Encuadra con slides «Diagnostico» / areas (cards).\\n\\n"
            f"### 50-75 Teoria visual cloud (Slides gancho → diagramas)\\n"
            f"Cambia a Presentacion.pptx de Clase 1. Capas cloud, CloudLite, C4 Context ejemplo.\\n\\n"
            f"### 75-110 Taller ficha + C4 Context\\n"
            f"Demo draw.io -> bloque Taller ampliado. Solucion en Kit docente/. Bloquea dominios vagos. Checklist.\\n\\n"
            f"### 110-120 Quiz + cierre\\n"
            f"Proyectar slide(s) «Quiz rapido» (solo preguntas). Aplicar "
            f"`Quiz Clase {n} - {c['slug']}.docx`. Corregir con "
            f"`Quiz Clase {n} - CLAVE DOCENTE.docx` (**no proyectar**).\\n"
            f"«Domingo 23:59 ficha+diagrama. Siguiente: IaaS/PaaS/SaaS (autonoma).»\\n"
        )'''
    new_plan1 = '''        plan = (
            f"### Día 1 · Sesión 0 (0-40) — Presentación del curso (PPTX aparte)\\n"
            f"Abre `Presentacion del Curso - Arquitectura…pptx`. Acuerdo, Padlet, evaluación, CONTENIDO.\\n"
            f"Di: «Esto es Sesión 0 (logística). Luego Clase 1 = diagnóstico + tema CloudLite.»\\n\\n"
            f"### Clase 1 · Diagnóstico (40-65)\\n"
            f"Cambia a `Presentacion.pptx` de Clase 1. Prueba Diagnóstica del Kit. Silencio 20-25 min.\\n"
            f"Encuadra con slides Diagnóstico / áreas (cards).\\n\\n"
            f"### Clase 1 · Teoría visual cloud (65-85)\\n"
            f"Capas cloud, CloudLite, C4 Context ejemplo.\\n\\n"
            f"### Clase 1 · Taller ficha + C4 (85-110)\\n"
            f"Demo draw.io → taller ampliado. Solución en Kit docente/. Bloquea dominios vagos.\\n\\n"
            f"### Clase 1 · Quiz + cierre (110-120)\\n"
            f"Proyectar «Quiz rápido» (solo preguntas). Aplicar "
            f"`Quiz Clase {n} - {c['slug']}.docx`. Corregir con "
            f"`Quiz Clase {n} - CLAVE DOCENTE.docx` (**no proyectar**).\\n"
            f"«Domingo 23:59 ficha+diagrama. Siguiente: IaaS/PaaS/SaaS (autónoma).»\\n"
        )'''
    if old_plan1 in t2:
        t2 = t2.replace(old_plan1, new_plan1)
        print("OK part3 plan clase1")
    else:
        # try without escape differences — replace shorter anchors
        t2 = t2.replace(
            "### 0-25 Presentacion del curso (PPTX aparte)",
            "### Día 1 · Sesión 0 (0-40) — Presentación del curso (PPTX aparte)",
        )
        t2 = t2.replace(
            "Di: diagnostico de conocimientos previos + arranque CloudLite.",
            "Di: «Sesión 0 = logística. Luego Clase 1 = diagnóstico + arranque CloudLite.»",
        )
        t2 = t2.replace(
            "\n## Anexo Clase 1 (Presentacion del curso + Diagnostico + arranque)\n\n"
            "### Bloque A — Presentacion del curso (PPTX aparte)\n",
            "\n## Anexo día 1 (Sesión 0 + Clase 1)\n\n"
            "### Sesión 0 — Presentación del curso (PPTX aparte; no es el tema)\n",
        )
        t2 = t2.replace(
            "Hoy: presentacion + diagnostico de conocimientos previos + arranque CloudLite.»\n",
            "Hoy: Sesión 0 (logística) y luego Clase 1 (diagnóstico + arranque CloudLite).»\n",
        )
        t2 = t2.replace(
            "### Bloque B — Diagnostico (instrumentos)\n",
            "### Clase 1 — Diagnóstico (instrumentos)\n",
        )
        t2 = t2.replace(
            "### Bloque C — Arranque tematico (esta Presentacion.pptx)\n",
            "### Clase 1 — Arranque temático (esta Presentacion.pptx; sin bio/evaluación/cronograma)\n",
        )
        print("OK part3 guion soft")

    # Extra EXTRA diagnostico note
    t2 = t2.replace(
        '"Luego: arranque tematico CloudLite (esta misma presentacion)."',
        '"Luego: arranque temático CloudLite (esta misma presentación; Sesión 0 ya quedó atrás)."',
    )
    if t2 != t:
        _write(p, t2)
        print("OK part3 saved")
    else:
        print("WARN part3 unchanged")


def patch_prog2_clase01():
    p = SLIDES / "build_uniajc_prog2_clase01.py"
    t = _read(p)
    if "block_timeline_slide" in t and "120 min" in t and "180 min" not in t:
        print("SKIP prog2 clase01 already ok")
        return
    # ensure import
    if "block_timeline_slide" not in t:
        t = t.replace(
            "from uniajc_slides_engine import (\n"
            "    new_prs, content_slide, table_content, box_note_slide, closing_slide, blank,\n"
            "    bg_white, bullets, footer_num, rect, textbox, _run, _rich,\n"
            "    NAVY, WHITE, CIAN, GRAY, SW, MARGIN, CONTENT_W, add_logo, PP_ALIGN, MSO_ANCHOR, Pt,\n"
            ")",
            "from uniajc_slides_engine import (\n"
            "    new_prs, content_slide, table_content, box_note_slide, closing_slide, blank,\n"
            "    bg_white, bullets, footer_num, rect, textbox, _run, _rich,\n"
            "    block_timeline_slide,\n"
            "    NAVY, WHITE, CIAN, GRAY, SW, MARGIN, CONTENT_W, add_logo, PP_ALIGN, MSO_ANCHOR, Pt,\n"
            ")",
        )
    t = t.replace("180 min", "120 min")
    t = t.replace(
        '''    content_slide(
        prs, "Agenda de hoy (180 min)",
        [
            "**0–15** Encuadre de la clase y acuerdo de trabajo de hoy.",
            "**15–45** Prueba diagnóstica (POO básica / lógica).",
            "**45–100** Teoría Core: clase vs objeto, encapsulamiento, estado y comportamiento.",
            "**100–140** Laboratorio: instalar/verificar JDK + IDE + primer proyecto Java.",
            "**140–170** Proyecto Integrador: enunciado y primer compromiso de avance.",
            "**170–180** Cierre, dudas y tarea de la semana.",
        ],
        idx=2,
    )''',
        '''    block_timeline_slide(
        prs, "Mapa del bloque de hoy (120 min)",
        [
            ("0-10", "Encuadre temático (Sesión 0 ya quedó atrás)"),
            ("10-35", "Diagnóstico de previos"),
            ("35-70", "Teoría Core: clase vs objeto"),
            ("70-100", "Laboratorio: JDK + IDE + HolaPOO"),
            ("100-120", "PI: primer avance · cierre"),
        ],
        idx=2,
    )''',
    )
    # also catch if still Agenda 120
    t = t.replace(
        '''    content_slide(
        prs, "Agenda de hoy (120 min)",
        [
            "**0–15** Encuadre de la clase y acuerdo de trabajo de hoy.",
            "**15–45** Prueba diagnóstica (POO básica / lógica).",
            "**45–100** Teoría Core: clase vs objeto, encapsulamiento, estado y comportamiento.",
            "**100–140** Laboratorio: instalar/verificar JDK + IDE + primer proyecto Java.",
            "**140–170** Proyecto Integrador: enunciado y primer compromiso de avance.",
            "**170–180** Cierre, dudas y tarea de la semana.",
        ],
        idx=2,
    )''',
        '''    block_timeline_slide(
        prs, "Mapa del bloque de hoy (120 min)",
        [
            ("0-10", "Encuadre temático (Sesión 0 ya quedó atrás)"),
            ("10-35", "Diagnóstico de previos"),
            ("35-70", "Teoría Core: clase vs objeto"),
            ("70-100", "Laboratorio: JDK + IDE + HolaPOO"),
            ("100-120", "PI: primer avance · cierre"),
        ],
        idx=2,
    )''',
    )
    _write(p, t)
    print("OK prog2 clase01")


def patch_bd2_timeline():
    """BD2: reemplazar agenda bullet por block_timeline_slide."""
    p = SLIDES / "build_uniajc_bd2_all.py"
    t = _read(p)
    if "block_timeline_slide" not in t:
        # find import from uniajc_slides_engine
        t = re.sub(
            r"(from uniajc_slides_engine import \([^)]+)\)",
            lambda m: m.group(0).replace(")", ", block_timeline_slide)") if "block_timeline_slide" not in m.group(0) else m.group(0),
            t,
            count=1,
            flags=re.S,
        )
        if "block_timeline_slide" not in t:
            t = t.replace(
                "steps_visual_slide, checklist_slide,",
                "steps_visual_slide, checklist_slide, block_timeline_slide,",
            )
    old = '''    content_slide(prs, "Agenda de hoy (120 min)", [
        f"**Tipo:** clase {tipo_lbl} · hilo **VetCare DB (PI)**",
        "**0-10** Encuadre: que parte del PI cerramos hoy.",
        "**10-35** Teoria Core breve (al servicio del entregable).",
        "**35-55** Demo paso a paso con la herramienta del dia.",
        "**55-105** Taller guiado = tarea del PI (equipo).",
        "**105-120** Criterios de exito · quiz/cierre · duda PI.",
    ], idx=idx); idx += 1'''
    new = '''    block_timeline_slide(prs, "Mapa del bloque de hoy (120 min)", [
        ("0-10", f"Encuadre · clase {tipo_lbl} · VetCare"),
        ("10-35", "Teoría Core breve (al servicio del PI)"),
        ("35-55", "Demo con la herramienta del día"),
        ("55-105", "Taller guiado = tarea del PI"),
        ("105-120", "Criterios · quiz/cierre · duda PI"),
    ], idx=idx); idx += 1'''
    if old in t:
        t = t.replace(old, new)
        _write(p, t)
        print("OK bd2 timeline")
    else:
        print("WARN bd2 agenda block not found exactly")


def patch_plans_calendars_correos():
    # PLAN rows
    plans = [
        (ROOT / "Programacion II" / "Plan curso" / "2026-1" / "PLAN_DE_CURSO_2026-1.md",
         "| 1 | 12/08/2026 | Presencial | Presentación del curso · Introducción a POO |",
         "| 1 | 12/08/2026 | Presencial | Diagnóstico · Introducción a POO |",
         "Sesión 0"),
        (ROOT / "Seminario de Sistemas" / "Plan curso" / "2026-1" / "PLAN_DE_CURSO_2026-1.md",
         "| 1 | 13/08/2026 | Virtual (síncrona) | Presentación del curso · Conceptos iniciales |",
         "| 1 | 13/08/2026 | Virtual (síncrona) | Diagnóstico · Conceptos iniciales |",
         "Sesión 0"),
        (ROOT / "Bases de Datos II" / "Plan curso" / "2026-2" / "PLAN_DE_CURSO_2026-2.md",
         "| 1 | 10/08/2026 | Virtual (síncrona) | Presentación del curso · Diagnóstico · Revisión de Bases de Datos I |",
         "| 1 | 10/08/2026 | Virtual (síncrona) | Diagnóstico · Revisión de Bases de Datos I |",
         "Sesión 0"),
        (ROOT / "Arquitectura de Sistemas Computacionales" / "Plan curso" / "2026-2" / "PLAN_DE_CURSO_2026-2.md",
         "| 1 | 10/08/2026 | Presencial | Presentación del curso · Diagnóstico · Introducción a arquitecturas cloud |",
         "| 1 | 10/08/2026 | Presencial | Diagnóstico · Introducción a arquitecturas cloud |",
         "Sesión 0"),
    ]
    note = (
        "\n> **Sesión 0 (no es clase temática):** `Clases/Presentacion del Curso - ….pptx` "
        "(logística, acuerdo, Padlet, evaluación, CONTENIDO). En el **día 1** puede ir "
        "Sesión 0 + Clase 1 dentro del bloque de 120 min. Se mantienen **15 clases** temáticas (1–15).\n"
    )
    for path, old, new, marker in plans:
        if not path.exists():
            print("MISS", path)
            continue
        t = _read(path)
        t2 = t.replace(old, new)
        # also try without accents variants
        t2 = t2.replace(
            "Presentación del curso · Diagnóstico ·",
            "Diagnóstico ·",
        )
        t2 = t2.replace(
            "Presentación del curso · Introducción a POO",
            "Diagnóstico · Introducción a POO",
        )
        t2 = t2.replace(
            "Presentación del curso · Conceptos iniciales",
            "Diagnóstico · Conceptos iniciales",
        )
        if marker not in t2:
            # insert after tabla header section start
            anchor = "## Tabla Clase · Fecha · Tipo · Tema"
            if anchor in t2:
                t2 = t2.replace(anchor, note.strip() + "\n\n" + anchor, 1)
            else:
                t2 = note + t2
        if t2 != t:
            _write(path, t2)
            print("OK plan", path.parent.parent.parent.name)
        else:
            print("WARN plan", path)

    # CALENDARIO nota clase 1
    cals = [
        (ROOT / "Arquitectura de Sistemas Computacionales" / "Plan curso" / "2026-2" / "CALENDARIO_2026-2.md",
         "| 1 | 10/08/2026 | Presencial | Presentación + Diagnóstico + intro cloud |",
         "| 1 | 10/08/2026 | Presencial | Sesión 0 (Presentación del curso) + Clase 1: Diagnóstico · intro cloud |"),
        (ROOT / "Bases de Datos II" / "Plan curso" / "2026-2" / "CALENDARIO_2026-2.md",
         "Presentación + Diagnóstico",
         "Sesión 0 + Clase 1: Diagnóstico"),
        (ROOT / "Programacion II" / "Plan curso" / "2026-1" / "CALENDARIO_2026-1.md",
         "Presentación",
         "Sesión 0 + Clase 1"),
        (ROOT / "Seminario de Sistemas" / "Plan curso" / "2026-1" / "CALENDARIO_2026-1.md",
         "Presentación",
         "Sesión 0 + Clase 1"),
    ]
    for path, old, new in cals:
        if not path.exists():
            continue
        t = _read(path)
        # only first clase row — careful with Programacion replace all
        if path.name.startswith("CALENDARIO"):
            lines = t.splitlines()
            out = []
            done = False
            for ln in lines:
                if (not done) and ln.strip().startswith("| 1 |") and "Present" in ln:
                    ln2 = ln.replace(
                        "Presentación + Diagnóstico + intro cloud",
                        "Sesión 0 (Presentación del curso) + Clase 1: Diagnóstico · intro cloud",
                    )
                    ln2 = ln2.replace(
                        "Presentación + Diagnóstico",
                        "Sesión 0 + Clase 1: Diagnóstico",
                    )
                    ln2 = ln2.replace(
                        "Presentación del curso",
                        "Sesión 0 + Clase 1",
                    )
                    # if still generic Presentación in nota
                    if ln2 == ln and "Presentación" in ln:
                        ln2 = re.sub(r"Presentaci[oó]n[^|]*", "Sesión 0 + Clase 1 (diagnóstico · tema) ", ln)
                    out.append(ln2)
                    done = True
                else:
                    out.append(ln)
            t2 = "\n".join(out) + ("\n" if t.endswith("\n") else "")
            if t2 != t:
                _write(path, t2)
                print("OK cal", path.parent.parent.parent.name)
            else:
                print("WARN cal", path.name)

    # CSV: update tema of first class if Presentación in tema
    for csv_path in ROOT.glob("*/Plan curso/*/calendario_eventos_*.csv"):
        t = _read(csv_path)
        t2 = t
        t2 = t2.replace(
            "Presentación del curso · Diagnóstico ·",
            "Diagnóstico ·",
        )
        t2 = t2.replace(
            "Presentación del curso · Introducción",
            "Diagnóstico · Introducción",
        )
        t2 = t2.replace(
            "Presentación del curso · Conceptos",
            "Diagnóstico · Conceptos",
        )
        t2 = t2.replace(
            "Presentacion del curso · Diagnostico ·",
            "Diagnostico ·",
        )
        if t2 != t:
            _write(csv_path, t2)
            print("OK csv", csv_path)

    # Correos
    for correo in ROOT.glob("*/Entregas docente/2026-2/CORREO_BIENVENIDA*.md"):
        t = _read(correo)
        t2 = t.replace(
            "En la **primera clase** trabajamos: Presentación del curso + diagnóstico de conocimientos previos + arranque temático.",
            "En el **día 1**: **Sesión 0** (Presentación del curso: logística, acuerdo, Padlet, evaluación) y **Clase 1** (diagnóstico de conocimientos previos + arranque temático).",
        )
        t2 = t2.replace(
            "En la **primera clase** trabajaremos: Presentación del curso + diagnóstico de conocimientos previos + arranque temático.",
            "En el **día 1**: **Sesión 0** (Presentación del curso: logística, acuerdo, Padlet, evaluación) y **Clase 1** (diagnóstico de conocimientos previos + arranque temático).",
        )
        if t2 != t:
            _write(correo, t2)
            print("OK correo", correo.name)


def patch_rules_and_agents():
    rule = ROOT / ".cursor" / "rules" / "uniajc-docente.mdc"
    t = _read(rule)
    old = """## Clase 1 (fija)

- La **Clase 1** siempre incluye: (1) Presentación del curso (acuerdo, logística, Padlet, evaluación, cronograma) + (2) **Diagnóstico de conocimientos previos** (prueba de saberes del prerrequisito / fundamentos; no encuesta logística ni evaluación del temario nuevo) + (3) arranque temático de la primera unidad.
- En la **Presentación del Curso** (metodología / Acuerdos / CONTENIDO Clase 1) mencionar explícitamente: «Clase 1: Presentación del curso + **diagnóstico de conocimientos previos** + arranque del tema.»
- Guion/slides de Clase 1 = Presentación del Curso + Diagnóstico + primer bloque temático.
- Wording del plan/CONTENIDO: `Presentación del curso · Diagnóstico · [tema intro]`.
- Instrumento (prueba): `Kit docente/Clase 1/Prueba Diagnostica…` · Registro institucional: `Entregas docente/<periodo>/DIAGNOSTICO…`.
"""
    new = """## Sesión 0 vs Clase 1 (fija)

- **Sesión 0** = `Clases/Presentacion del Curso - ….pptx` (logística: acuerdo, Padlet, evaluación, CONTENIDO, herramientas, cierre). **No es tema de unidad.**
- **Clase 1** = primer bloque **temático**: **Diagnóstico de conocimientos previos** + arranque del tema intro del plan. **Sin** repetir bio/evaluación/cronograma largo (eso es Sesión 0).
- En el **día 1** del calendario pueden ir Sesión 0 + Clase 1 (p. ej. 40–50 min Sesión 0 + resto Clase 1) dentro de 120 min. Se mantienen **15 clases** temáticas numeradas 1–15 (no renombrar el calendario a 16).
- En Presentación del Curso (metodología / Acuerdos): «**Sesión 0**: Presentación del curso. **Clase 1**: diagnóstico de conocimientos previos + arranque del tema.»
- Wording CONTENIDO: celda Clase 1 = `Diagnóstico · [tema intro]` (sin «Presentación del curso»); Sesión 0 como ítem aparte (`n: 0` / `kind: sesion0`) o nota en metodología.
- Instrumento (prueba): `Kit docente/Clase 1/Prueba Diagnostica…` · Registro institucional: `Entregas docente/<periodo>/DIAGNOSTICO…`.
"""
    if old in t:
        t = t.replace(old, new)
    else:
        t = re.sub(
            r"## Clase 1 \(fija\)[\s\S]*?(?=\n# Builds y marca)",
            new + "\n",
            t,
            count=1,
        )
    # Also update bullet 4 about Presentación del curso if needed
    t = t.replace(
        "cronograma estilo **CONTENIDO** (Clases 1–15 en **una sola** diapositiva vía `contenido_clases_slides`; no tabla densa)",
        "cronograma estilo **CONTENIDO** (Sesión 0 + Clases 1–15 en **una sola** diapositiva vía `contenido_clases_slides`; no tabla densa)",
    )
    _write(rule, t)
    print("OK rule uniajc-docente.mdc")

    # uniajc.json clase_1 block
    uj = ROOT / ".config" / "universidades" / "uniajc.json"
    jt = _read(uj)
    old_j = '''    "clase_1": {
      "_regla": "La Clase 1 siempre combina Presentación del curso + Diagnóstico de conocimientos previos + arranque temático de la primera unidad (no solo logística). La Presentación del Curso debe mencionarlo explícitamente.",
      "incluye": [
        "Presentación del curso (acuerdo, logística, Padlet, evaluación, cronograma)",
        "Diagnóstico de conocimientos previos (prueba de saberes del prerrequisito/fundamentos; instrumento en Kit docente / registro en Entregas docente)",
        "Un poco del tema de la primera unidad"
      ],
      "guion_y_slides": "Guion/slides de Clase 1 = Presentación del Curso + Diagnóstico + primer bloque temático.",
      "wording_plan": "Presentación del curso · Diagnóstico · [tema intro]",
      "wording_pptx_curso": "Clase 1: Presentación del curso + diagnóstico de conocimientos previos + arranque del tema.",'''
    new_j = '''    "sesion_0": {
      "_regla": "Sesión 0 = Presentación del Curso (logística). No es clase temática ni cuenta como renumerar a 16 clases.",
      "archivo": "Clases/Presentacion del Curso - ….pptx",
      "incluye": [
        "Acuerdo / logística / Padlet / evaluación / CONTENIDO / herramientas / cierre"
      ]
    },
    "clase_1": {
      "_regla": "Clase 1 = Diagnóstico de conocimientos previos + arranque temático. La Presentación del Curso es Sesión 0 (archivo aparte), no se mezcla como tema dentro del PPTX de Clase 1.",
      "incluye": [
        "Diagnóstico de conocimientos previos (prueba de saberes del prerrequisito/fundamentos; instrumento en Kit docente / registro en Entregas docente)",
        "Arranque temático de la primera unidad"
      ],
      "guion_y_slides": "Día 1: Sesión 0 (Presentación del Curso) + Clase 1 (Diagnóstico + tema). PPTX de Clase 1 solo diagnóstico + tema.",
      "wording_plan": "Diagnóstico · [tema intro]",
      "wording_pptx_curso": "Sesión 0: Presentación del curso. Clase 1: diagnóstico de conocimientos previos + arranque del tema.",'''
    if old_j in jt:
        jt = jt.replace(old_j, new_j)
        _write(uj, jt)
        print("OK uniajc.json")
    else:
        print("WARN uniajc.json block not exact — trying softer")
        if '"sesion_0"' not in jt:
            jt = jt.replace('"clase_1":', '"sesion_0": {"_regla": "Presentación del Curso (logística), archivo aparte."}, "clase_1":', 1)
            _write(uj, jt)
            print("OK uniajc.json soft")

    for agent in [
        ROOT / ".claude" / "agents" / "disenador-curricular-uniajc.md",
        ROOT / ".cursor" / "agents" / "disenador-curricular-uniajc.md",
        ROOT / ".claude" / "agents" / "uniajc-dudas-material.md",
        ROOT / ".cursor" / "agents" / "uniajc-dudas-material.md",
    ]:
        if not agent.exists():
            continue
        at = _read(agent)
        a2 = at
        a2 = a2.replace(
            "Siempre: Presentación del curso + **Diagnóstico de conocimientos previos** (prueba de saberes del prerrequisito/fundamentos; no encuesta logística) + arranque temático de la primera unidad.\n"
            "En la **Presentación del Curso** (metodología / Acuerdos / CONTENIDO) mencionar: «Clase 1: Presentación del curso + **diagnóstico de conocimientos previos** + arranque del tema.»\n"
            "Wording CONTENIDO: `Presentación del curso · Diagnóstico · [tema intro]`.",
            "**Sesión 0** = Presentación del curso (logística, archivo aparte). **Clase 1** = Diagnóstico de previos + arranque temático (sin mezclar bio/evaluación/cronograma en el PPTX de Clase 1).\n"
            "En Presentación del Curso mencionar: «Sesión 0: Presentación del curso. Clase 1: diagnóstico + arranque del tema.»\n"
            "Wording CONTENIDO Clase 1: `Diagnóstico · [tema intro]` (+ ítem Sesión 0 aparte).",
        )
        a2 = a2.replace(
            "Siempre: Presentación del curso + Diagnóstico + arranque temático de la primera unidad. Wording: `Presentación del curso · Diagnóstico · [tema intro]`. Guion/slides Clase 1 = PPTX del curso + Diagnóstico + primer bloque temático.",
            "**Sesión 0** = Presentación del curso (archivo aparte). **Clase 1** = Diagnóstico + tema intro. Wording CONTENIDO: `Diagnóstico · [tema intro]`. Día 1 puede combinar Sesión 0 + Clase 1.",
        )
        a2 = a2.replace(
            "6. Metodología (ABPr, Presencialidad asistida: Clase 1 presencial · resto virtual · parciales presencial, Teoría + Taller + Quiz). **Mencionar explícitamente:** Clase 1 = Presentación del curso + **diagnóstico de conocimientos previos** + arranque del tema.",
            "6. Metodología (ABPr, Presencialidad asistida, Teoría + Taller + Quiz). **Mencionar:** Sesión 0 = Presentación del curso; Clase 1 = **diagnóstico de conocimientos previos** + arranque del tema.",
        )
        if a2 != at:
            _write(agent, a2)
            print("OK agent", agent.name)
        else:
            print("WARN agent", agent.name)


def main():
    patch_curso_build(
        SLIDES / "build_uniajc_prog2_curso.py",
        clase1_tema="Diagnóstico · Introducción a POO",
        aclaracion="Día 1: Sesión 0 (Presentación del curso, archivo aparte) + Clase 1 (diagnóstico + Introducción a POO). Material estudiante solo en carpeta Clases/.",
        sesion0_tema="Presentación del curso (logística)",
        fecha1="12/08",
    )
    patch_curso_build(
        SLIDES / "build_uniajc_seminario_curso.py",
        clase1_tema="Diagnóstico · Conceptos iniciales",
        aclaracion="Día 1: Sesión 0 (Presentación del curso, archivo aparte) + Clase 1 (diagnóstico + Conceptos iniciales). Material estudiante solo en carpeta Clases/.",
        sesion0_tema="Presentación del curso (logística)",
        fecha1="13/08",
    )
    patch_curso_build(
        SLIDES / "build_uniajc_bd2_curso.py",
        clase1_tema="Diagnóstico · Revisión de Bases de Datos I",
        aclaracion="Día 1: Sesión 0 (Presentación del curso, archivo aparte) + Clase 1 (diagnóstico + revisión BD I). Festivos = autónoma en Campus Virtual.",
        sesion0_tema="Presentación del curso (logística)",
        fecha1="10/08",
    )
    patch_curso_build(
        SLIDES / "build_uniajc_arq_curso.py",
        clase1_tema="Diagnóstico · Introducción a arquitecturas cloud",
        aclaracion="Día 1: Sesión 0 (Presentación del curso, archivo aparte) + Clase 1 (diagnóstico + intro arquitecturas cloud). Festivos = autónoma en Campus Virtual.",
        sesion0_tema="Presentación del curso (logística)",
        fecha1="10/08",
    )
    patch_part2_timeline()
    patch_part3_guion()
    patch_prog2_clase01()
    patch_bd2_timeline()
    patch_plans_calendars_correos()
    patch_rules_and_agents()
    print("DONE patch")


if __name__ == "__main__":
    main()
