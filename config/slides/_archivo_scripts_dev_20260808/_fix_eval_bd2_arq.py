# -*- coding: utf-8 -*-
from pathlib import Path
import re
import subprocess
import sys

base = Path(__file__).resolve().parent
ROOT = base.parents[1]

OLD = '''[
            ["1", "10/08", "Presencial", "30%"],
            ["2", "17/08", "Autónoma", "30%"],
            ["3", "24/08", "Virtual", "40%"],
        ],
        note="Parciales sincronos en ultima clase regular del corte (nunca en autonoma). Lun: Clases 5/9/14.",'''

NEW = '''[
            ["1", "10/08–13/09", "Parcial 10% · Talleres/Quiz 10% · Asistencia 10%", "30%"],
            ["2", "14/09–18/10", "Parcial 10% · Talleres/Quiz 10% · Asistencia 10%", "30%"],
            ["3", "19/10–22/11", "Parcial 15% · PI 20% · Asistencia 5%", "40%"],
        ],
        note="Parciales síncronos en última clase regular del corte (nunca en autónoma). Lun: Clases 5/9/14.",'''

for name in ["build_uniajc_bd2_curso.py", "build_uniajc_arq_curso.py"]:
    p = base / name
    t = p.read_text(encoding="utf-8")
    if OLD in t:
        t = t.replace(OLD, NEW)
        print("exact", name)
    else:
        t2 = re.sub(
            r'\[\s*\n\s*\["1", "10/08", "Presencial", "30%"\],\s*\n'
            r'\s*\["2", "17/08", "Aut[^\"]*", "30%"\],\s*\n'
            r'\s*\["3", "24/08", "Virtual", "40%"\],\s*\n\s*\],\s*\n'
            r'\s*note="[^"]*",',
            NEW,
            t,
            count=1,
        )
        print("regex", name, t2 != t)
        t = t2
    p.write_text(t, encoding="utf-8")

# ensure prog2 cover modalidad
p = base / "build_uniajc_prog2_curso.py"
t = p.read_text(encoding="utf-8")
cover = t.split("course_cover")[1][:900]
print("prog2 cover has Modalidad", "Modalidad" in cover)
cover_s = t.split("course_cover")[1][:900] if "course_cover" in t else ""
# seminario
p2 = base / "build_uniajc_seminario_curso.py"
t2 = p2.read_text(encoding="utf-8")
print("sem cover has Modalidad", "Modalidad" in t2.split("course_cover")[1][:900])

for script in ["build_uniajc_bd2_curso.py", "build_uniajc_arq_curso.py"]:
    r = subprocess.run([sys.executable, str(base / script)], cwd=str(ROOT), capture_output=True, text=True)
    print(script, r.returncode, (r.stdout or r.stderr).strip()[:180])
