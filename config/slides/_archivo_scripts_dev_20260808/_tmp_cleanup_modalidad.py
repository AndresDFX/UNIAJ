# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos")

files = list((ROOT / ".config" / "slides").glob("build_uniajc_*_curso.py"))
files += [
    ROOT / ".cursor" / "rules" / "uniajc-docente.mdc",
    ROOT / ".claude" / "agents" / "disenador-curricular-uniajc.md",
    ROOT / ".cursor" / "agents" / "disenador-curricular-uniajc.md",
    ROOT / ".claude" / "agents" / "uniajc-dudas-material.md",
]
files += list(ROOT.rglob("CALENDARIO_2026-*.md"))
files += list(ROOT.rglob("PLAN_DE_CURSO_2026-*.md"))

subs = [
    (
        "**Virtual** (Clase 1 presencial · resto virtual · parciales síncronos · festivos autónomos)",
        "**Virtual** (clases y parciales síncronos · festivos autónomos)",
    ),
    (
        "**Virtual** (Clase 1 presencial · resto virtual · parciales síncronos)",
        "**Virtual** (clases y parciales síncronos)",
    ),
    (
        "Virtual (Clase 1 presencial · resto virtual · parciales síncronos · festivos autónomos)",
        "Virtual (clases y parciales síncronos · festivos autónomos)",
    ),
    (
        "Virtual (Clase 1 presencial · resto virtual · parciales síncronos)",
        "Virtual (clases y parciales síncronos)",
    ),
    (
        "**Virtual** (clases presencial / virtual síncrona / autónoma)",
        "**Virtual** (clases y parciales síncronos · festivos autónomos)",
    ),
    (
        'course_cover(..., inicio_clase="18:10") → texto `Inicio de clase: 18:10`',
        'course_cover(..., inicio_clase="20:10") → texto `Inicio de clase: 20:10`',
    ),
    (
        "p. ej. 18:00→`Inicio de clase: 18:10`",
        "p. ej. 20:00→`Inicio de clase: 20:10`",
    ),
    (
        "18:00→`Inicio de clase: 18:10`",
        "20:00→`Inicio de clase: 20:10`",
    ),
]

for p in files:
    if not p.exists() or not p.is_file():
        continue
    raw = p.read_bytes()
    if b"\x00" in raw[:4]:
        t = raw.decode("utf-16")
        enc = "utf-16"
    else:
        t = raw.decode("utf-8")
        enc = "utf-8"
    n = t
    for old, new in subs:
        n = n.replace(old, new)
    if n != t:
        p.write_text(n, encoding=enc)
        print("fixed", p.relative_to(ROOT))

print("done")
