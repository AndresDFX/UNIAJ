# -*- coding: utf-8 -*-
from pathlib import Path
import os, sys
SLIDES = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides")
os.chdir(SLIDES)
sys.path.insert(0, str(SLIDES))
for name in [
    "build_uniajc_prog2_curso.py",
    "build_uniajc_seminario_curso.py",
    "build_uniajc_bd2_curso.py",
    "build_uniajc_arq_curso.py",
]:
    path = SLIDES / name
    ns = {"__file__": str(path), "__name__": "build_mod"}
    exec(compile(path.read_text(encoding="utf-8"), name, "exec"), ns)
    ns["build"]()
    print("OK", name)