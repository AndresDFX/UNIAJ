# -*- coding: utf-8 -*-
"""Normaliza y corrige generar_semestre_2026_2.py (modalidad 2026-2)."""
from pathlib import Path
import re

p = Path(__file__).with_name("generar_semestre_2026_2.py")
raw = p.read_bytes()
if raw[:2] in (b"\xff\xfe", b"\xfe\xff") or (len(raw) > 3 and raw[1] == 0):
    t = raw.decode("utf-16")
else:
    t = raw.decode("utf-8")

# Collapse accidental blank-line inflation (every other line empty)
lines = t.splitlines()
if sum(1 for l in lines if l.strip() == "") > len(lines) * 0.4:
    lines = [l for i, l in enumerate(lines) if l.strip() != "" or (i and lines[i - 1].strip() != "")]
    # still may have pairs; collapse consecutive empties to one, then remove all empties between code
    # Safer: if >40% empty, drop ALL empty lines
    if sum(1 for l in lines if l.strip() == "") > len(lines) * 0.3:
        lines = [l for l in lines if l.strip() != ""]
    t = "\n".join(lines) + "\n"
    print("normalized blank lines")

REGLA = (
    "Criterio de modalidad por sesion (fijo 2026-2): modalidad del curso = Presencialidad asistida. "
    "Clase 1 = presencial; demas clases regulares = virtual (sincrona); "
    "parciales = siempre presenciales y sincronos; festivos = clase autonoma (sin parcial). "
    "Los parciales NUNCA se programan en dia festivo ni en clase autonoma. "
    "Si el cierre teorico del corte cae en festivo/autonoma, el parcial se mueve a la ultima clase "
    "regular anterior del mismo corte."
)

t = re.sub(
    r"LOGICA_EVALUACION = \(.*?\)\n",
    'LOGICA_EVALUACION = (\n    "' + REGLA + '"\n)\n',
    t,
    count=1,
    flags=re.S,
)

MOD = "Presencialidad asistida (Clase 1 presencial / resto virtual / parciales presencial / festivos autonomos)"

t = t.replace(
    '"modalidad": (\n'
    '            "Presencialidad asistida "\n'
    '            "(confirmar calendario virtual del mes en Campus Virtual)"\n'
    "        )",
    f'"modalidad": "{MOD}"',
)
t = t.replace(
    "Modalidad: Presencialidad asistida (confirmar semanas virtuales en Campus Virtual).\n",
    f"Modalidad: {MOD}.\n",
)
t = t.replace(
    "Periodo 2026-2 · Grupo 641A-2 · Lunes 18:00–20:00 (120 min) · Modalidad: Virtual.\n",
    f"Periodo 2026-2 · Grupo 641A-2 · Lunes 18:00–20:00 (120 min) · Modalidad: {MOD}.\n",
)
t = t.replace(
    "Grupo: [PENDIENTE]. Modalidad: [PENDIENTE].\n",
    f"Grupo: [PENDIENTE]. Modalidad: {MOD}.\n",
)
t = t.replace(
    '"modalidad": "Presencialidad asistida"',
    f'"modalidad": "{MOD}"',
)
t = t.replace(
    "No hay festivos en miércoles; todas regulares.\n",
    "No hay festivos en miercoles. Clase 1 presencial; resto virtual; parciales presencial.\n",
)
t = t.replace(
    "No hay festivos en jueves; todas regulares.\n",
    "No hay festivos en jueves. Clase 1 presencial; resto virtual; parciales presencial.\n",
)

new_class = '''
def class_dates(weekday: int) -> list[dict]:
    out: list[dict] = []
    d = START
    n = 0
    while d <= END:
        if d.weekday() == weekday:
            n += 1
            iso = d.isoformat()
            festivo = FESTIVOS.get(iso)
            if festivo:
                tipo = "autonoma"
            elif n == 1:
                tipo = "presencial"
            else:
                tipo = "virtual"
            out.append(
                {
                    "n": n,
                    "fecha": iso,
                    "tipo": tipo,
                    "festivo": festivo,
                    "parcial": False,
                }
            )
        d += timedelta(days=1)
    return out


def apply_parciales(clases: list[dict]) -> list[dict]:
    ranges = [(1, 5, 1), (6, 10, 2), (11, 15, 3)]
    for a, b, pn in ranges:
        regs = [cl for cl in clases if a <= cl["n"] <= b and cl["tipo"] != "autonoma"]
        if not regs:
            continue
        target = regs[-1]
        target["parcial"] = True
        target["parcial_n"] = pn
        target["tipo"] = "presencial"
    return clases
'''

# Remove any previous broken apply_parciales + replace class_dates through set_cell_text
t = re.sub(
    r"def class_dates\(weekday: int\) -> list\[dict\]:.*?def set_cell_text",
    new_class.lstrip() + "\n\ndef set_cell_text",
    t,
    count=1,
    flags=re.S,
)

# Remove duplicate apply_parciales if any remain later
parts = t.split("def apply_parciales")
if len(parts) > 2:
    # keep first occurrence only; drop later defs until next def
    head = parts[0] + "def apply_parciales" + parts[1]
    rest = "".join(parts[2:])
    # drop from start of duplicate body until next top-level def
    rest = re.sub(r"^.*?(?=\ndef )", "", rest, count=1, flags=re.S)
    t = head + rest
    print("removed duplicate apply_parciales")

t = t.replace(
    'clases = class_dates(meta["weekday"])',
    'clases = apply_parciales(class_dates(meta["weekday"]))',
)
# avoid double wrap
t = t.replace(
    "clases = apply_parciales(apply_parciales(class_dates(meta[\"weekday\"]))",
    'clases = apply_parciales(class_dates(meta["weekday"]))',
)

old = 'tipo = "Autónoma (festivo)" if cl["tipo"] == "autonoma" else "Regular"'
new = (
    'tipo = {"autonoma": "Autónoma (festivo)", "presencial": "Presencial", '
    '"virtual": "Virtual (síncrona)"}.get(cl["tipo"], cl["tipo"])'
)
t = t.replace(old, new)

# cierre_parcial uses tipo != autonoma — still valid
p.write_text(t, encoding="utf-8")
print("OK apply", "def apply_parciales" in t)
print("OK presencial branch", 'tipo = "presencial"' in t)
print("OK Clase 1 text", "Clase 1 presencial" in t)
print("OK main", "apply_parciales(class_dates" in t)
# sanity: no regular tipo assignment left in class_dates
print("has regular fallback", 'else "regular"' in t)
