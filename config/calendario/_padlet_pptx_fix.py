# -*- coding: utf-8 -*-
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos")
PADLET_URL = "https://padlet.com/andres_dfx/uniaj-l77e9uu16trgdvcp"
CLEAR_NOTE = (
    "Post-clase (docente, NO va en PPTX estudiante): menu ... del tablero -> Clear posts -> "
    "codigo de verificacion -> Delete. Reutiliza los 3 padlets del plan gratis sin borrar el enlace."
)

# --- 1) Engine: URL real + quitar nota Clear posts de la slide ---
eng = ROOT / ".config" / "slides" / "uniajc_slides_engine.py"
et = eng.read_text(encoding="utf-8")
et = et.replace(
    'PADLET_URL_PLACEHOLDER = "[URL Padlet UNIAJC — pendiente; usar QR oficial]"',
    f'PADLET_URL = "{PADLET_URL}"\nPADLET_URL_PLACEHOLDER = PADLET_URL  # compat',
)
# Also handle if already partially updated
if f'PADLET_URL = "{PADLET_URL}"' not in et and "PADLET_URL =" not in et:
    et = et.replace(
        'PADLET_URL_PLACEHOLDER = "[URL Padlet UNIAJC \u2014 pendiente; usar QR oficial]"',
        f'PADLET_URL = "{PADLET_URL}"\nPADLET_URL_PLACEHOLDER = PADLET_URL  # compat',
    )
# Keep PADLET_CLEAR_NOTE for docs but remove from slide rendering
old_block = '''    # Nota docente Clear posts
    ny = y + 4.7
    rounded(s, MARGIN, ny, CONTENT_W, 0.72, ACLAR)
    nt = textbox(s, MARGIN + 0.2, ny + 0.1, CONTENT_W - 0.4, 0.55, anchor=MSO_ANCHOR.MIDDLE)
    _rich(nt.paragraphs[0], "💡 **Docente:** " + PADLET_CLEAR_NOTE, 11, GRAY)
    footer_num(s, idx)'''
new_block = '''    # Sin nota operativa docente (Clear posts): solo en agente/config/regla, no en PPTX estudiante.
    footer_num(s, idx)'''
if old_block not in et:
    # try without emoji
    old_block2 = '''    # Nota docente Clear posts
    ny = y + 4.7
    rounded(s, MARGIN, ny, CONTENT_W, 0.72, ACLAR)
    nt = textbox(s, MARGIN + 0.2, ny + 0.1, CONTENT_W - 0.4, 0.55, anchor=MSO_ANCHOR.MIDDLE)
    _rich(nt.paragraphs[0], "''' 
    # more flexible: regex
    et2, n = re.subn(
        r"\n    # Nota docente Clear posts\n.*?footer_num\(s, idx\)",
        "\n    # Sin nota operativa docente (Clear posts): solo en agente/config/regla, no en PPTX estudiante.\n    footer_num(s, idx)",
        et,
        count=1,
        flags=re.S,
    )
    if n != 1:
        raise SystemExit(f"No pude quitar Clear posts del padlet_slide (n={n})")
    et = et2
else:
    et = et.replace(old_block, new_block)

# Ensure padlet_slide uses PADLET_URL
et = et.replace("url = url or PADLET_URL_PLACEHOLDER", "url = url or PADLET_URL")
# docstring update
et = et.replace(
    "se muestra el placeholder PADLET_URL_PLACEHOLDER.",
    "se muestra PADLET_URL (URL oficial + QR).",
)
# shrink left box height slightly since no bottom note? keep as is for QR layout
eng.write_text(et, encoding="utf-8")
print("OK engine padlet")

# --- 2) uniajc.json ---
uj = ROOT / ".config" / "universidades" / "uniajc.json"
data = json.loads(uj.read_text(encoding="utf-8"))
pend = data.get("_pendientes", [])
data["_pendientes"] = [x for x in pend if "Padlet" not in x and "padlet" not in x.lower()]
data["padlet"] = {
    "_regla": "Mismo Padlet + QR para la Presentacion del Curso de CUALQUIER curso UNIAJC de este workspace.",
    "url": PADLET_URL,
    "asset_qr": ".config/slides/assets/qr_padlet_uniajc.png",
    "slide_helper": "padlet_slide() en uniajc_slides_engine.py",
    "uso": "Solo en Presentacion del Curso (rompe-hielo estudiante), despues del tutor_slide. Sin instrucciones Clear posts en la PPTX.",
    "post_clase_docente": CLEAR_NOTE,
    "nota": "URL oficial + QR en assets. Clear posts solo en docs docentes, nunca en PPTX de estudiantes.",
}
uj.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("OK uniajc.json")

# --- 3) Agents ---
for agent in [
    ROOT / ".cursor" / "agents" / "disenador-curricular-uniajc.md",
    ROOT / ".claude" / "agents" / "disenador-curricular-uniajc.md",
]:
    t = agent.read_text(encoding="utf-8")
    t = t.replace(
        "- Placeholder URL: [URL Padlet UNIAJC — pendiente; usar QR oficial].",
        f"- **URL oficial:** {PADLET_URL}",
    )
    t = t.replace(
        "- Placeholder URL: [URL Padlet UNIAJC \u2014 pendiente; usar QR oficial].",
        f"- **URL oficial:** {PADLET_URL}",
    )
    # Ensure Clear posts stays as docente-only note
    if "NO en PPTX" not in t:
        t = t.replace(
            "- **Post-clase (docente):** menú ⋯ del tablero → **Clear posts** → código de verificación → Delete. Así se reutilizan los 3 padlets del plan gratis sin borrar el enlace ni cambiar el QR.",
            "- **Post-clase (docente, NO en PPTX estudiante):** menú ⋯ del tablero → **Clear posts** → código de verificación → Delete. Así se reutilizan los 3 padlets del plan gratis sin borrar el enlace ni cambiar el QR.",
        )
        t = t.replace(
            "- **Post-clase (docente):** men\u00fa \u22ef del tablero",
            "- **Post-clase (docente, NO en PPTX estudiante):** men\u00fa \u22ef del tablero",
        )
    t = t.replace(
        "9. Pendientes conocidos: URL Campus Virtual, Meet, URL textual Padlet (QR ya fijo), grupo Arquitectura (modalidad = Presencialidad asistida), listados de estudiantes.",
        "9. Pendientes conocidos: URL Campus Virtual, Meet, grupo Arquitectura, listados de estudiantes. Padlet URL ya fija.",
    )
    t = t.replace(
        "10. Padlet: mismo asset QR + padlet_slide en toda Presentación del Curso; post-clase Clear posts (⋯ → Clear posts) para reusar los 3 padlets gratis.",
        "10. Padlet: URL oficial + QR en Presentación del Curso (rompe-hielo estudiante). Clear posts solo en agente/config (nunca en PPTX).",
    )
    # Add rule: no teacher checklist slides in Presentacion del Curso
    if "sin checklist docente" not in t.lower() and "sin rutina operativa" not in t.lower():
        t = t.replace(
            "3. **Padlet / rompe-hielo** (mismo QR institucional para todos los cursos — padlet_slide)",
            "3. **Padlet / rompe-hielo** (URL oficial + QR — padlet_slide; sin nota Clear posts ni checklist docente)",
        )
    agent.write_text(t, encoding="utf-8")
    print("OK", agent.relative_to(ROOT))

# --- 4) Rule ---
rule = ROOT / ".cursor" / "rules" / "uniajc-docente.mdc"
rt = rule.read_text(encoding="utf-8")
padlet_block = (
    "\n## Padlet institucional\n\n"
    f"- **URL:** {PADLET_URL}\n"
    "- **QR:** `.config/slides/assets/qr_padlet_uniajc.png` (misma slide + URL).\n"
    "- En Presentación del Curso: solo rompe-hielo para estudiantes (sin Clear posts ni checklist docente).\n"
    "- **Post-clase (docente):** ⋯ → Clear posts → código → Delete (reusar los 3 padlets gratis).\n"
)
if "## Padlet institucional" in rt:
    rt = re.sub(r"\n## Padlet institucional\n.*?(?=\n## |\n# |\Z)", padlet_block, rt, count=1, flags=re.S)
else:
    # insert after Estándar vigente de slides or after cursos
    rt = rt.replace(
        "6. Marca: `#095292` / `#269CCB` / `#FFD000` — ver `config/universidades/uniajc.json`.\n",
        "6. Marca: `#095292` / `#269CCB` / `#FFD000` — ver `config/universidades/uniajc.json`.\n"
        + padlet_block,
    )
# Presentacion del Curso = estudiantes
if "sin checklist docente" not in rt:
    rt = rt.replace(
        "4. Presentación del curso: grupo(s), docente, recursos, evaluación del Acuerdo pedagógico, cierre con día/hora semanal (usar calendario 2026-2).\n",
        "4. Presentación del curso (para **estudiantes**): grupo(s), docente, recursos, evaluación, cronograma, Padlet rompe-hielo, cierre. **Sin** checklist/rutina operativa del docente ni Clear posts.\n",
    )
rule.write_text(rt, encoding="utf-8")
print("OK rule")

# --- 5) Clean student-facing teacher-path mentions in Recursos slides ---
slides = ROOT / ".config" / "slides"
replacements = {
    "build_uniajc_prog2_curso.py": [
        (
            '"Material de clase: carpeta `Clases/Clase N` + talleres; guiones en `Guiones/` / `Kit docente/`.",',
            '"Material de clase: carpeta `Clases/Clase N` + talleres en Campus Virtual.",',
        ),
    ],
    "build_uniajc_seminario_curso.py": [
        (
            "'Material: `Clases/Clase N` · `Guiones/` · `Kit docente/`.",
            "'Material: `Clases/Clase N` + entregas en Campus Virtual.",
        ),
    ],
}
for name, pairs in replacements.items():
    p = slides / name
    t = p.read_text(encoding="utf-8")
    for old, new in pairs:
        if old in t:
            t = t.replace(old, new)
            print("OK clean", name)
        else:
            # fuzzy: find Kit docente line
            for line in t.splitlines():
                if "Kit docente" in line:
                    print("WARN Kit docente line:", repr(line))
    p.write_text(t, encoding="utf-8")

# Print box_note contents to verify no teacher checklist
for name in ["build_uniajc_arq_curso.py", "build_uniajc_bd2_curso.py", "build_uniajc_seminario_curso.py", "build_uniajc_prog2_curso.py"]:
    t = (slides / name).read_text(encoding="utf-8")
    m = re.search(r'box_note_slide\([\s\S]*?\n\s*\)', t)
    print("---", name, "---")
    print(m.group(0)[:500] if m else "NO box_note")

# --- 6) Fix generar_semestre parcial logic (prevent regression) ---
gen = ROOT / ".config" / "calendario" / "generar_semestre_2026_2.py"
gt = gen.read_text(encoding="utf-8")
gt = gt.replace(
    LOGICA_OLD := (
        'LOGICA_EVALUACION = (\n'
        '    "Lógica de evaluación (réplica Acuerdos Prog. II / Seminario): "\n'
        '    "tres cortes 30%/30%/40%; hay Parcial 1, Parcial 2 y Parcial 3 "\n'
        '    "en la finalización de cada corte (Clases 5, 10 y 15 respectivamente). "\n'
        '    "Si la clase de cierre cae en festivo, el parcial se aplica en esa "\n'
        '    "clase autónoma (evaluación asíncrona / entrega en Campus Virtual)."\n'
        ')'
    ),
    '''LOGICA_EVALUACION = (
    "Tres cortes 30%/30%/40%. Parciales siempre sincronos (presencial/virtual sincrona). "
    "NUNCA en festivo ni clase autonoma. Criterio: ultima clase regular del corte "
    "(mie/jue: 5/10/15; lun Arq/BD II: 5/9/14). Autonomas de cierre = refuerzo sin parcial."
)''',
)
# if LOGICA replace failed, try simpler
if "NUNCA en festivo ni clase autonoma" not in gt and "NUNCA en festivo" not in gt:
    gt = re.sub(
        r"LOGICA_EVALUACION = \([\s\S]*?\)\n\nDOCENTE",
        '''LOGICA_EVALUACION = (
    "Tres cortes 30%/30%/40%. Parciales siempre sincronos. "
    "NUNCA en festivo ni clase autonoma. Ultima clase regular del corte "
    "(mie/jue: 5/10/15; lun: 5/9/14)."
)

DOCENTE''',
        gt,
        count=1,
    )

gt = gt.replace('"modalidad": "Virtual",', '"modalidad": "Presencialidad asistida",')
gt = gt.replace(
    '"modalidad": "[PENDIENTE — modalidad]",',
    '"modalidad": "Presencialidad asistida",',
)
gt = gt.replace(
    "Periodo 2026-2 · Grupo 641A-2 · Lunes 18:00–20:00 (120 min) · Modalidad: Virtual.\n",
    "Periodo 2026-2 · Grupo 641A-2 · Lunes 18:00–20:00 (120 min) · Modalidad: Presencialidad asistida.\n",
)
gt = gt.replace(
    "Grupo: [PENDIENTE]. Modalidad: [PENDIENTE].\n",
    "Grupo: [PENDIENTE]. Modalidad: Presencialidad asistida.\n",
)
gt = gt.replace(
    '"codigo": "[CÓDIGO PENDIENTE]",\n        "grupo": "641A-2",',
    '"codigo": "FI303215",\n        "grupo": "641A-2",',
)
gt = gt.replace(
    '"codigo": "[CÓDIGO PENDIENTE]",\n        "grupo": "[PENDIENTE — grupo]",',
    '"codigo": "FI303380",\n        "grupo": "[PENDIENTE — grupo]",',
)

# Fix cierre_parcial to use last regular
old_cierre = '''    cierre_parcial = {5: "Parcial 1 (cierre Corte 1)", 10: "Parcial 2 (cierre Corte 2)", 15: "Parcial 3 (cierre Corte 3)"}
    for cl in clases:
        tipo = "Autónoma (festivo)" if cl["tipo"] == "autonoma" else "Regular"
        notas = []
        if cl["festivo"]:
            notas.append(cl["festivo"])
        if cl["n"] in cierre_parcial:
            notas.append(cierre_parcial[cl["n"]])'''

new_cierre = '''    # Parciales en ultima clase regular de cada corte (nunca autonoma)
    ranges = [(1, 5, 1), (6, 10, 2), (11, 15, 3)]
    cierre_parcial = {}
    for a, b, pn in ranges:
        regs = [cl for cl in clases if a <= cl["n"] <= b and cl["tipo"] != "autonoma"]
        if regs:
            cierre_parcial[regs[-1]["n"]] = f"Parcial {pn} (cierre Corte {pn})"
    for cl in clases:
        tipo = "Autónoma (festivo)" if cl["tipo"] == "autonoma" else "Regular"
        notas = []
        if cl["festivo"]:
            notas.append(cl["festivo"])
            if cl["n"] not in cierre_parcial:
                notas.append("refuerzo sin parcial")
        if cl["n"] in cierre_parcial:
            notas.append(cierre_parcial[cl["n"]])'''

if old_cierre in gt:
    gt = gt.replace(old_cierre, new_cierre)
    print("OK generar cierre_parcial")
else:
    print("WARN generar cierre_parcial block not exact")

# EVAL_TEXT note
gt = gt.replace(
    '"Nota: si la clase de cierre es festivo (clase autónoma), el parcial se aplica "\n'
    '    "en esa ventana autónoma / entrega en Campus Virtual."',
    '"Nota: parciales NUNCA en festivo/autonoma; se mueven a la ultima clase regular del corte."',
)
gen.write_text(gt, encoding="utf-8")
print("OK generar_semestre")

# --- 7) Rebuild 4 PPTX ---
sys.path.insert(0, str(ROOT / ".config" / "slides"))
# force reload engine
for mod in list(sys.modules):
    if mod.startswith("uniajc_slides") or mod.startswith("build_uniajc_"):
        del sys.modules[mod]

import uniajc_slides_engine as engm
print("PADLET_URL =", getattr(engm, "PADLET_URL", None), getattr(engm, "PADLET_URL_PLACEHOLDER", None))
# verify no Clear in padlet_slide source
import inspect
src = inspect.getsource(engm.padlet_slide)
assert "Clear posts" not in src, "Clear posts still in padlet_slide"
assert PADLET_URL in src or "PADLET_URL" in src

for mod_name in [
    "build_uniajc_arq_curso",
    "build_uniajc_bd2_curso",
    "build_uniajc_prog2_curso",
    "build_uniajc_seminario_curso",
]:
    if mod_name in sys.modules:
        del sys.modules[mod_name]
    m = __import__(mod_name)
    m.build()
    print("OK pptx", mod_name)

print("DONE")
