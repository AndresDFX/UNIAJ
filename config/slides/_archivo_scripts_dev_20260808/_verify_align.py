# -*- coding: utf-8 -*-
from pathlib import Path
import re

base = Path(__file__).resolve().parent
for name in [
    "build_uniajc_prog2_curso.py",
    "build_uniajc_seminario_curso.py",
    "build_uniajc_bd2_curso.py",
    "build_uniajc_arq_curso.py",
]:
    t = (base / name).read_text(encoding="utf-8")
    m = re.search(r'\{"n": 1, "tema": "([^"]+)"', t)
    print(name)
    print("  clase1:", m.group(1) if m else None)
    print("  Parcial 10%:", "Parcial 10%" in t)
    print("  Campus Virtual pendiente:", "Campus Virtual — pendiente" in t or "[URL Campus" in t)
    print("  Clear posts:", "Clear posts" in t)
    print("  listado PENDIENTE:", "PENDIENTE listado" in t)
    i = t.find("Sistema de evaluación")
    if i < 0:
        i = t.find("Sistema de evaluaci")
    print("  eval snippet:", t[i : i + 280].replace("\n", " | "))
    print()

arq = (base / "build_uniajc_arq_curso.py").read_text(encoding="utf-8")
print("ARQ has 12:00", "12:00" in arq)
print("ARQ has 13:00", "13:00" in arq)
print("ARQ has 180", "180" in arq)
