# -*- coding: utf-8 -*-
from pathlib import Path
import re

SLIDES = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides")

specs = [
    ("build_uniajc_prog2_curso.py", "12/08", "Diagnóstico · Introducción a POO"),
    ("build_uniajc_seminario_curso.py", "13/08", "Diagnóstico · Conceptos iniciales"),
    ("build_uniajc_bd2_curso.py", "10/08", "Diagnóstico · Revisión de Bases de Datos I"),
    ("build_uniajc_arq_curso.py", "10/08", "Diagnóstico · Introducción a arquitecturas cloud"),
]

for name, fecha, tema in specs:
    p = SLIDES / name
    t = p.read_text(encoding="utf-8")
    if 'kind": "sesion0"' in t or "kind': 'sesion0'" in t:
        print(name, "already has sesion0")
        continue
    needle = '{"n": 1, "tema": "' + tema + '", "fecha": "' + fecha + '"}'
    insert = (
        '{"n": 0, "kind": "sesion0", "tema": "Presentación del curso (logística)", "fecha": "' + fecha + '"},\n'
        '            ' + needle
    )
    if needle not in t:
        # try with possible spacing from blank-line files
        m = re.search(r'\{\s*"n"\s*:\s*1\s*,\s*"tema"\s*:\s*"' + re.escape(tema) + r'"\s*,\s*"fecha"\s*:\s*"' + re.escape(fecha) + r'"\s*\}', t)
        if not m:
            print("MISS n=1", name)
            continue
        needle = m.group(0)
        insert = (
            '{"n": 0, "kind": "sesion0", "tema": "Presentación del curso (logística)", "fecha": "' + fecha + '"},\n'
            '            ' + needle
        )
    t2 = t.replace(needle, insert, 1)
    p.write_text(t2, encoding="utf-8", newline="\n")
    print("OK inserted", name)

# regenerate curso builds only
import os, sys
os.chdir(SLIDES)
sys.path.insert(0, str(SLIDES))
for name in [s[0] for s in specs]:
    ns = {}
    exec(compile((SLIDES/name).read_text(encoding="utf-8"), name, "exec"), ns)
    ns["build"]()
    print("regen", name)