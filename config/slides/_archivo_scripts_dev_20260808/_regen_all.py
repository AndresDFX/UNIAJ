# -*- coding: utf-8 -*-
import os, sys, traceback
from pathlib import Path
SLIDES = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides")
os.chdir(SLIDES)
sys.path.insert(0, str(SLIDES))

builds = [
    "build_uniajc_prog2_curso.py",
    "build_uniajc_prog2_clase01.py",
    "build_uniajc_seminario_curso.py",
    "build_uniajc_bd2_curso.py",
    "build_uniajc_arq_curso.py",
]
for name in builds:
    print("===", name)
    try:
        ns = {"__name__": "__main__", "__file__": str(SLIDES/name)}
        exec(compile((SLIDES/name).read_text(encoding="utf-8"), name, "exec"), ns)
        if "build" in ns:
            ns["build"]()
        print("OK")
    except Exception:
        traceback.print_exc()

# Arquitectura all clases
print("=== part3 build_all")
try:
    from part3 import build_all
    build_all()
    print("OK arq all")
except Exception:
    traceback.print_exc()

# BD2 all
print("=== bd2 all")
try:
    import build_uniajc_bd2_all as bd2
    if hasattr(bd2, "build_all"):
        bd2.build_all()
    elif hasattr(bd2, "main"):
        bd2.main()
    else:
        print("available", [x for x in dir(bd2) if not x.startswith("_")])
    print("OK bd2")
except Exception:
    traceback.print_exc()