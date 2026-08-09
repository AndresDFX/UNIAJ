# -*- coding: utf-8 -*-
from pathlib import Path
import subprocess
import sys

base = Path(__file__).resolve().parent
ROOT = base.parents[1]
MOD = (
    "Modalidad: **Presencialidad asistida** "
    "(Clase 1 presencial · resto virtual · parciales presencial · festivos autónomos)"
)

# Prog2 uses double quotes
p = base / "build_uniajc_prog2_curso.py"
t = p.read_text(encoding="utf-8")
if 'course_cover' in t and MOD not in t.split("course_cover", 1)[1][:1000]:
    # insert after Horario line inside first course_cover
    needle = None
    for line in t.splitlines():
        if "Horario:" in line and "Miércoles" in line:
            needle = line
            break
    if needle and MOD not in t:
        indent = "            "
        # detect quote style of needle
        q = '"' if '"' in needle else "'"
        addition = f"{indent}{q}{MOD}{q},"
        t = t.replace(needle, needle + "\n" + addition, 1)
        p.write_text(t, encoding="utf-8")
        print("prog2 cover patched")
    else:
        print("prog2 needle", bool(needle), "already?", MOD in t)
else:
    print("prog2 cover already ok")

# Seminario may use single quotes
p = base / "build_uniajc_seminario_curso.py"
t = p.read_text(encoding="utf-8")
cover = t.split("course_cover", 1)[1][:1000]
if MOD not in cover:
    needle = None
    for line in t.splitlines():
        if "Horario:" in line and "Jueves" in line:
            needle = line
            break
    if needle:
        indent = "        " if needle.startswith("        ") else "            "
        q = '"' if '"' in needle else "'"
        addition = f"{indent}{q}{MOD}{q},"
        t = t.replace(needle, needle + "\n" + addition, 1)
        p.write_text(t, encoding="utf-8")
        print("seminario cover patched")
    else:
        print("seminario needle missing")
else:
    print("seminario cover already ok")

for script in ["build_uniajc_prog2_curso.py", "build_uniajc_seminario_curso.py"]:
    r = subprocess.run(
        [sys.executable, str(base / script)],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    print(script, r.returncode, (r.stdout or r.stderr).strip()[:180])
    t = (base / script).read_text(encoding="utf-8")
    print("  cover Modalidad:", MOD in t.split("course_cover", 1)[1][:1000])
