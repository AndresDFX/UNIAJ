# -*- coding: utf-8 -*-
from pathlib import Path
import sys
SLIDES = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides")
sys.path.insert(0, str(SLIDES))
from guion_md_a_docx import convert
root = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\Arquitectura de Sistemas Computacionales\Kit docente")
for md in sorted(root.glob("Clase */Guion Docente *.md")):
    docx = md.with_suffix(".docx")
    convert(md, docx)
    print("OK", md.parent.name)
print("done")