# -*- coding: utf-8 -*-
from pathlib import Path
import csv, json, re, sys

ROOT = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos")

# Fix BD2 leftover info line
p = ROOT / ".config" / "slides" / "build_uniajc_bd2_curso.py"
t = p.read_text(encoding="utf-8")
old = None
for line in t.splitlines():
    if "('info'" in line and "641A-2" in line:
        old = line
        break
print("FOUND", repr(old))
if old and "Virtual" in old:
    new = "            ('info', 'Lunes 18:00-20:00 · Presencialidad asistida (virtual sincrona) · Grupo 641A-2.'),"
    t = t.replace(old, new)
    p.write_text(t, encoding="utf-8")
    print("patched info")

CAL = json.loads((ROOT / ".config" / "calendario" / "semestre_2026_2.json").read_text(encoding="utf-8"))
fields = [
    "curso", "codigo_fi", "grupo", "clase_n", "fecha", "dia",
    "hora_inicio", "hora_fin", "tipo_clase", "es_parcial", "parcial_n",
    "sesion_etiqueta", "tema", "notas",
]

def parse_temas(plan_path: Path) -> dict:
    text = plan_path.read_text(encoding="utf-8")
    temas = {}
    for line in text.splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|\s*[^|]+\|\s*[^|]+\|\s*(.+?)\s*\|?\s*$", line)
        if not m:
            continue
        n = int(m.group(1))
        tema = m.group(2).strip()
        tema = re.sub(r"\s*\*\*Parcial.*$", "", tema).strip()
        tema = re.sub(r"\s*[·\u00b7]\s*refuerzo sin parcial\s*$", "", tema).strip()
        tema = tema.replace("**", "")
        temas[n] = tema
    return temas

def split_h(h: str):
    parts = re.split(r"\s*[–—\-]\s*", h.strip())
    return parts[0].strip(), parts[1].strip()

all_rows = []
for key, curso in CAL["cursos"].items():
    plan = ROOT / curso["folder"] / "Plan curso" / "PLAN_DE_CURSO_2026-2.md"
    temas = parse_temas(plan)
    h0, h1 = split_h(curso["horario"])
    grupo = curso.get("grupo") or "[PENDIENTE]"
    if "PENDIENTE" in str(grupo):
        grupo = "[PENDIENTE]"
    rows = []
    for c in curso["clases"]:
        pn = c.get("parcial_n") or ""
        es = bool(c.get("parcial"))
        if es:
            etiqueta = f"Clase {c['n']} · Parcial {pn}"
            tipo = "regular"
        else:
            etiqueta = f"Clase {c['n']}"
            if c["tipo"] == "autonoma":
                tipo = "autonoma"
            elif c["tipo"] == "virtual":
                tipo = "virtual"
            else:
                tipo = "regular"
        notas = []
        if c.get("festivo"):
            notas.append(f"festivo: {c['festivo']}")
        if es:
            notas.append("parcial presencial sincrono")
        if c["tipo"] == "autonoma" and not es:
            notas.append("clase autonoma / refuerzo sin parcial")
        if c["tipo"] == "virtual" and es:
            notas.append("curso con franja virtual; parcial sincrono presencial")
        notas.append("pendiente listado")
        row = {
            "curso": curso["nombre"],
            "codigo_fi": curso.get("codigo", ""),
            "grupo": grupo,
            "clase_n": c["n"],
            "fecha": c["fecha"],
            "dia": curso["dia"],
            "hora_inicio": h0,
            "hora_fin": h1,
            "tipo_clase": tipo,
            "es_parcial": "si" if es else "no",
            "parcial_n": pn if pn else "",
            "sesion_etiqueta": etiqueta,
            "tema": temas.get(c["n"], ""),
            "notas": "; ".join(notas),
        }
        rows.append(row)
        all_rows.append(row)
    outs = [
        ROOT / curso["folder"] / "Entregas docente" / "calendario_eventos_2026-2.csv",
        ROOT / ".config" / "calendario" / f"eventos_{key}_2026-2.csv",
    ]
    for out in outs:
        with out.open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)
        print("OK", out.relative_to(ROOT))

outc = ROOT / ".config" / "calendario" / "eventos_todos_cursos_2026-2.csv"
with outc.open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(all_rows)
print("OK consolidado", len(all_rows))

sys.path.insert(0, str(ROOT / ".config" / "slides"))
import build_uniajc_bd2_curso as m
m.build()
print("OK pptx bd2")
