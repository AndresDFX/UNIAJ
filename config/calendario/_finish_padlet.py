# -*- coding: utf-8 -*-
from pathlib import Path
import re, sys

ROOT = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos")
PADLET_URL = "https://padlet.com/andres_dfx/uniaj-l77e9uu16trgdvcp"
slides = ROOT / ".config" / "slides"

# Soften comment; keep PADLET_CLEAR_NOTE constant for docentes reading the engine source
eng = slides / "uniajc_slides_engine.py"
et = eng.read_text(encoding="utf-8")
et = et.replace(
    "# Sin nota operativa docente (Clear posts): solo en agente/config/regla, no en PPTX estudiante.",
    "# Nota operativa del docente (reuso del tablero) vive solo en agente/config/regla — no en esta slide.",
)
# Ensure URL constants
if f'PADLET_URL = "{PADLET_URL}"' not in et:
    raise SystemExit("PADLET_URL missing in engine")
# padlet_slide must use PADLET_URL and must NOT render Clear note UI
fn = re.search(r"def padlet_slide\(.*?\n(?=def )", et, flags=re.S)
if not fn:
    raise SystemExit("padlet_slide not found")
body = fn.group(0)
if "rounded(s, MARGIN, ny" in body or "PADLET_CLEAR_NOTE" in body:
    raise SystemExit("Clear note UI still rendered in padlet_slide")
if "url = url or PADLET_URL" not in body:
    raise SystemExit("padlet_slide not using PADLET_URL")
eng.write_text(et, encoding="utf-8")
print("OK engine comment")

# Inspect and optionally clean box_note slides (student OK if about horario/asistencia)
for name in [
    "build_uniajc_arq_curso.py",
    "build_uniajc_bd2_curso.py",
    "build_uniajc_seminario_curso.py",
    "build_uniajc_prog2_curso.py",
]:
    t = (slides / name).read_text(encoding="utf-8")
    # find call box_note_slide(prs
    for m in re.finditer(r"box_note_slide\(\s*prs,\s*([^\n]+),([\s\S]*?)\n\s*\)", t):
        title = m.group(1)
        body = m.group(2)
        print(name, "TITLE", title)
        print(body[:400])
        # If title suggests teacher checklist, remove whole call
        low = (title + body).lower()
        if any(k in low for k in ["checklist", "rutina", "en cada clase", "clear posts", "kit docente", "guion"]):
            print("  -> REMOVE teacher slide")
            t2 = t[: m.start()] + t[m.end() :]
            # also remove trailing comma leftovers carefully
            (slides / name).write_text(t2, encoding="utf-8")
            t = t2

# Rebuild
sys.path.insert(0, str(slides))
for mod in list(sys.modules):
    if mod.startswith("uniajc_slides") or mod.startswith("build_uniajc_"):
        del sys.modules[mod]

import uniajc_slides_engine as engm
assert engm.PADLET_URL == PADLET_URL
src = Path(engm.__file__).read_text(encoding="utf-8")
# ensure rendered function has no Clear posts UI note with Docente label
assert '**Docente:**' not in re.search(r"def padlet_slide\(.*?\n(?=def )", src, flags=re.S).group(0)

outs = []
for mod_name in [
    "build_uniajc_arq_curso",
    "build_uniajc_bd2_curso",
    "build_uniajc_prog2_curso",
    "build_uniajc_seminario_curso",
]:
    m = __import__(mod_name)
    m.build()
    outs.append(getattr(m, "OUT", "?"))
    print("OK", mod_name)

# Verify CSV parciales still good
import csv, json
cal = json.loads((ROOT / ".config" / "calendario" / "semestre_2026_2.json").read_text(encoding="utf-8"))
print("\n=== PARCIALES ===")
for k, c in cal["cursos"].items():
    print(c["nombre"])
    for pk in ("parcial_1", "parcial_2", "parcial_3"):
        p = c["parciales"][pk]
        print(f"  {pk}: Clase {p['clase']} {p['fecha']} {p['tipo']}")

print("\n=== CSV paths ===")
for p in sorted((ROOT / ".config" / "calendario").glob("eventos_*2026-2.csv")):
    print(p.relative_to(ROOT))
for folder in [
    "Programacion II",
    "Seminario de Sistemas",
    "Bases de Datos II",
    "Arquitectura de Sistemas Computacionales",
]:
    p = ROOT / folder / "Entregas docente" / "calendario_eventos_2026-2.csv"
    print(p.relative_to(ROOT), "exists" if p.exists() else "MISSING")

# cleanup temp
for f in (ROOT / ".config" / "calendario").glob("_padlet*"):
    f.unlink()
    print("deleted", f.name)
for f in (ROOT / ".config" / "calendario").glob("_finish*"):
    f.unlink()
    print("deleted", f.name)

print("DONE")
