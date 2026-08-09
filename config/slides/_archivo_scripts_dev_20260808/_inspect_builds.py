# -*- coding: utf-8 -*-
from pathlib import Path

def read_any(p: Path) -> str:
    b = p.read_bytes()
    if b[1:2] == b"\x00":
        return b.decode("utf-16-le")
    if b[:2] == b"\xff\xfe":
        return b.decode("utf-16")
    return b.decode("utf-8")

base = Path(__file__).resolve().parent
for name in [
    "build_uniajc_bd2_curso.py",
    "build_uniajc_arq_curso.py",
    "build_uniajc_seminario_curso.py",
    "build_uniajc_prog2_curso.py",
]:
    p = base / name
    t = read_any(p)
    print("====", name, "====")
    for i, line in enumerate(t.splitlines(), 1):
        keys = ("table_content", '"n": 1', "Horario", "Modalidad", "note=", "Parcial")
        if any(k in line for k in keys):
            print(f"{i}: {line[:160]}")
    print()
