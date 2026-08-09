# -*- coding: utf-8 -*-
from pathlib import Path
import re
SLIDES = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides")

p = SLIDES / "build_uniajc_prog2_clase01.py"
t = p.read_text(encoding="utf-8")
if "block_timeline_slide" not in t:
    t = t.replace(
        "    NAVY, WHITE, CIAN, GRAY, SW, MARGIN, CONTENT_W, add_logo, PP_ALIGN, MSO_ANCHOR, Pt,\n)",
        "    block_timeline_slide,\n    NAVY, WHITE, CIAN, GRAY, SW, MARGIN, CONTENT_W, add_logo, PP_ALIGN, MSO_ANCHOR, Pt,\n)",
    )
pat = re.compile(r'    content_slide\(\s*prs,\s*"Agenda de hoy \(120 min\)",\s*\[[\s\S]*?\],\s*idx=2,\s*\)')
repl = (
    '    block_timeline_slide(\n'
    '        prs, "Mapa del bloque de hoy (120 min)",\n'
    '        [\n'
    '            ("0-10", "Encuadre temático (Sesión 0 ya quedó atrás)"),\n'
    '            ("10-35", "Diagnóstico de previos"),\n'
    '            ("35-70", "Teoría Core: clase vs objeto"),\n'
    '            ("70-100", "Laboratorio: JDK + IDE + HolaPOO"),\n'
    '            ("100-120", "PI: primer avance · cierre"),\n'
    '        ],\n'
    '        idx=2,\n'
    '    )'
)
t2, n = pat.subn(repl, t, count=1)
print("prog2", n)
if n:
    p.write_text(t2, encoding="utf-8", newline="\n")

p = SLIDES / "build_uniajc_bd2_all.py"
t = p.read_text(encoding="utf-8")
if "block_timeline_slide" not in t:
    t = t.replace(
        "    herramientas_slide, steps_visual_slide, checklist_slide,\n)",
        "    herramientas_slide, steps_visual_slide, checklist_slide, block_timeline_slide,\n)",
    )
pat = re.compile(r'    content_slide\(prs, "Agenda de hoy \(120 min\)", \[[\s\S]*?\], idx=idx\); idx \+= 1')
repl = (
    '    block_timeline_slide(prs, "Mapa del bloque de hoy (120 min)", [\n'
    '        ("0-10", f"Encuadre · clase {tipo_lbl} · VetCare"),\n'
    '        ("10-35", "Teoría Core breve (al servicio del PI)"),\n'
    '        ("35-55", "Demo con la herramienta del día"),\n'
    '        ("55-105", "Taller guiado = tarea del PI"),\n'
    '        ("105-120", "Criterios · quiz/cierre · duda PI"),\n'
    '    ], idx=idx); idx += 1'
)
t2, n = pat.subn(repl, t, count=1)
print("bd2", n)
if n:
    p.write_text(t2, encoding="utf-8", newline="\n")

for name in ["build_uniajc_prog2_clase01.py", "build_uniajc_bd2_all.py"]:
    tt = (SLIDES / name).read_text(encoding="utf-8")
    print(name, "timeline", "block_timeline_slide" in tt, "agenda", "Agenda de hoy" in tt)