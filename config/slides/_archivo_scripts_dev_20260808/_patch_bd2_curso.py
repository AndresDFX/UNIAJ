# -*- coding: utf-8 -*-
from pathlib import Path
import re

p = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides\build_uniajc_bd2_curso.py")
raw = p.read_bytes()
if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
    t = raw.decode("utf-16")
else:
    t = raw.decode("utf-8", errors="replace")

t2 = t
t2 = t2.replace("inicio_clase='20:10'", "inicio_clase='18:10'")
t2 = t2.replace('inicio_clase="20:10"', 'inicio_clase="18:10"')
t2 = re.sub(r"20:00\s*.\s*22:00", "18:00 – 20:00", t2)
t2 = t2.replace("20:00-22:00", "18:00-20:00")
t2 = t2.replace("Modalidad: **Virtual**", "Modalidad: **Presencialidad asistida**")
t2 = t2.replace("**Virtual** (clases y parciales", "**Presencialidad asistida** (clases y parciales")
t2 = t2.replace("Virtual (clases y parciales", "Presencialidad asistida (clases y parciales")
# closing slide residual
t2 = re.sub(r"(Lunes \*\*18:00 – 20:00\*\*)\s*[·•]\s*Virtual", r"\1 · Presencialidad asistida", t2)
t2 = t2.replace(" · Virtual'", " · Presencialidad asistida'")
t2 = t2.replace(' · Virtual"', ' · Presencialidad asistida"')

p.write_text(t2, encoding="utf-8")
print("curso build patched")
for i, line in enumerate(t2.splitlines()):
    if any(k in line for k in ["18:00", "20:00", "Modalidad", "inicio_clase", "Virtual", "Presencial"]):
        print(f"{i}: {line[:140]}")

par = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\Bases de Datos II\Parciales")
print("PARCIALES:")
for f in sorted(par.glob("*")):
    print(" ", f.name, f.stat().st_size)