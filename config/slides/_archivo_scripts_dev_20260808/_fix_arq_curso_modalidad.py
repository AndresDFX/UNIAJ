# -*- coding: utf-8 -*-
import re
from pathlib import Path
p = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides\build_uniajc_arq_curso.py")
text = p.read_text(encoding="utf-8")
text = text.replace("\r\r\n", "\n").replace("\r\n", "\n").replace("\r", "\n")
text, n1 = re.subn(r"Modalidad: \*\*Virtual\*\*[^\n']*", "Modalidad: **Presencialidad asistida** (Clase 1 presencial · resto virtual síncrona · parciales presencial · festivos autónomos)", text, count=1)
text, n2 = re.subn(r"Modalidad: Virtual \(clases y parciales s[^\)]*\)\.?", "Modalidad: **Presencialidad asistida** (Clase 1 presencial · resto virtual · parciales presencial).", text, count=1)
text, n3 = re.subn(r"(Lunes 10:00-12:00 \(120 min\)\. )Modalidad:[^.]*\.", r"\1Modalidad: **Presencialidad asistida** (Clase 1 presencial · resto virtual · parciales presencial).", text, count=1)
p.write_text(text, encoding="utf-8", newline="\n")
print("OK", n1, n2, n3)