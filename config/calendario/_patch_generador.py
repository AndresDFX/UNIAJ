# -*- coding: utf-8 -*-
import re
from pathlib import Path

p = Path(__file__).with_name("generar_semestre_2026_2.py")
raw = p.read_bytes()
if raw[:2] in (b"\xff\xfe", b"\xfe\xff") or (len(raw) > 2 and raw[1] == 0):
    t = raw.decode("utf-16")
else:
    t = raw.decode("utf-8")

REGLA = (
    "Criterio de modalidad por sesion (fijo 2026-2): modalidad del curso = Presencialidad asistida. "
    "Clase 1 = presencial; demas clases regulares = virtual (sincrona); "
    "parciales = siempre presenciales y sincronos; festivos = clase autonoma (sin parcial). "
    "Los parciales NUNCA se programan en dia festivo ni en clase autonoma. "
    "Si el cierre teorico del corte cae en festivo/autonoma, el parcial se mueve a la ultima clase "
    "regular anterior del mismo corte."
)

t2 = re.sub(
    r"LOGICA_EVALUACION = \(.*?\)\n",
    'LOGICA_EVALUACION = (\n    "' + REGLA + '"\n)\n',
    t,
    count=1,
    flags=re.S,
)
print("logica", t2 != t)
t = t2

pairs = [
    (
        'Presencialidad asistida "\n            "(confirmar calendario virtual del mes en Campus Virtual)"',
        'Presencialidad asistida (Clase 1 presencial / resto virtual / parciales presencial / festivos autonomos)"',
    ),
    (
        "Modalidad: Presencialidad asistida (confirmar semanas virtuales en Campus Virtual).\n",
        "Modalidad: Presencialidad asistida (Clase 1 presencial / resto virtual / parciales presencial / festivos autonomos).\n",
    ),
    (
        "Modalidad: Virtual.\n",
        "Modalidad: Presencialidad asistida (Clase 1 presencial / resto virtual / parciales presencial / festivos autonomos).\n",
    ),
    (
        "Grupo: [PENDIENTE]. Modalidad: [PENDIENTE].\n",
        "Grupo: [PENDIENTE]. Modalidad: Presencialidad asistida (Clase 1 presencial / resto virtual / parciales presencial / festivos autonomos).\n",
    ),
    (
        "No hay festivos en miércoles; todas regulares.\n",
        "No hay festivos en miercoles. Clase 1 presencial; resto virtual; parciales presencial.\n",
    ),
    (
        "No hay festivos en jueves; todas regulares.\n",
        "No hay festivos en jueves. Clase 1 presencial; resto virtual; parciales presencial.\n",
    ),
]
for a, b in pairs:
    if a in t:
        t = t.replace(a, b)
        print("ok", a[:50])
    else:
        print("miss", a[:50])

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

t2 = re.sub(
    r"def class_dates\(weekday: int\) -> list\[dict\]:.*?return out\n",
    new_class.lstrip() + "\n",
    t,
    count=1,
    flags=re.S,
)
print("class_dates", t2 != t)
t = t2

if "apply_parciales(class_dates" not in t:
    t = t.replace(
        'clases = class_dates(meta["weekday"])',
        'clases = apply_parciales(class_dates(meta["weekday"]))',
    )
    print("main apply ok")

old = 'tipo = "Autónoma (festivo)" if cl["tipo"] == "autonoma" else "Regular"'
new = (
    'tipo = {"autonoma": "Autónoma (festivo)", "presencial": "Presencial", '
    '"virtual": "Virtual (síncrona)"}.get(cl["tipo"], cl["tipo"])'
)
if old in t:
    t = t.replace(old, new)
    print("tipo label ok")
else:
    m = re.search(r"tipo = .*autonoma.*", t)
    print("tipo line:", m.group(0) if m else "not found")

p.write_text(t, encoding="utf-8")
print("final", "apply_parciales" in t, "Clase 1 presencial" in t)
