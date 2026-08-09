# -*- coding: utf-8 -*-
from pathlib import Path
import subprocess
import sys

base = Path(__file__).resolve().parent
ROOT = base.parents[1]
p = base / "build_uniajc_prog2_curso.py"
t = p.read_text(encoding="utf-8")

start = t.find("course_cover(")
end = t.find("tutor_slide(", start)
cover = t[start:end]
print("COVER BEFORE:\n", cover)

mod_line = (
    '            "Modalidad: **Presencialidad asistida** '
    '(Clase 1 presencial · resto virtual · parciales presencial · festivos autónomos)",\n'
)

if "Modalidad:" not in cover:
    # insert after Horario line
    lines = cover.splitlines(keepends=True)
    out = []
    for line in lines:
        out.append(line)
        if "Horario:" in line and "Miércoles" in line:
            out.append(mod_line)
    new_cover = "".join(out)
    t = t[:start] + new_cover + t[end:]
    p.write_text(t, encoding="utf-8")
    print("PATCHED")
else:
    print("already has modalidad in cover")

r = subprocess.run([sys.executable, str(p)], cwd=str(ROOT), capture_output=True, text=True)
print(r.returncode, (r.stdout or r.stderr).strip())
t2 = p.read_text(encoding="utf-8")
cover2 = t2[t2.find("course_cover(") : t2.find("tutor_slide(")]
print("COVER AFTER has Modalidad:", "Modalidad:" in cover2)
print(cover2)
