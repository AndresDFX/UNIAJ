# -*- coding: utf-8 -*-
"""One-shot: modalidad Virtual + horarios noche 20:00-22:00 (Arq 10-12)."""
from pathlib import Path
import json
import re

ROOT = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos")

CRIT_OLD = (
    "Criterio de modalidad por sesión (fijo 2026-2): modalidad del curso = Presencialidad asistida. "
    "Clase 1 = presencial; demás clases regulares = virtual (síncrona); parciales = siempre presenciales y síncronos "
    "(aunque la sesión de otro modo sería virtual); festivos = clase autónoma (sin parcial). "
    "Los parciales NUNCA se programan en día festivo ni en clase autónoma. "
    "Si el cierre teórico del corte cae en festivo/autónoma, el parcial se mueve a la última clase regular anterior "
    "del mismo corte; la clase autónoma de cierre queda como refuerzo sin parcial."
)
CRIT_NEW = (
    "Criterio de modalidad por sesión (fijo 2026-2): modalidad del curso = Virtual. "
    "Clases regulares = virtual (síncrona); parciales = siempre síncronos (virtual); festivos = clase autónoma (sin parcial). "
    "Los parciales NUNCA se programan en día festivo ni en clase autónoma. "
    "Si el cierre teórico del corte cae en festivo/autónoma, el parcial se mueve a la última clase regular anterior "
    "del mismo corte; la clase autónoma de cierre queda como refuerzo sin parcial."
)

MOD_LONG_OLD = "Presencialidad asistida (Clase 1 presencial · resto virtual · parciales presencial · festivos autónomos)"
MOD_LONG_NEW = "Virtual (clases y parciales síncronos · festivos autónomos)"
MOD_SHORT_OLD = "Presencialidad asistida (Clase 1 presencial · resto virtual · parciales presencial)"
MOD_SHORT_NEW = "Virtual (clases y parciales síncronos)"
MOD_SLASH_OLD = "Presencialidad asistida (Clase 1 presencial / resto virtual / parciales presencial)"
MOD_SLASH_NEW = "Virtual (clases y parciales síncronos)"


def replace_common(text: str, night: bool = False) -> str:
    text = text.replace(CRIT_OLD, CRIT_NEW)
    text = text.replace(MOD_LONG_OLD, MOD_LONG_NEW)
    text = text.replace(MOD_SHORT_OLD, MOD_SHORT_NEW)
    text = text.replace(MOD_SLASH_OLD, MOD_SLASH_NEW)
    text = text.replace("Modalidad: **Presencialidad asistida**", "Modalidad: **Virtual**")
    text = text.replace("Modalidad: Presencialidad asistida", "Modalidad: Virtual")
    text = text.replace("modalidad del curso = Presencialidad asistida", "modalidad del curso = Virtual")
    text = text.replace("Modalidad del curso: **Presencialidad asistida**", "Modalidad del curso: **Virtual**")
    text = text.replace("Parciales presenciales:", "Parciales síncronos (virtual):")
    text = text.replace("parciales presencial", "parciales síncronos")
    text = text.replace("parcial presencial sincrono", "parcial virtual sincrono")
    if night:
        text = text.replace("18:00 – 20:00", "20:00 – 22:00")
        text = text.replace("18:00-20:00", "20:00-22:00")
        text = text.replace("18:00–20:00", "20:00–22:00")
        text = text.replace('inicio_clase="18:10"', 'inicio_clase="20:10"')
        text = text.replace("inicio_clase='18:10'", "inicio_clase='20:10'")
        text = text.replace("→ 18:10", "→ 20:10")
        text = text.replace("18:00→`Inicio de clase: 18:10`", "20:00→`Inicio de clase: 20:10`")
    return text


def read_text_any(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        return raw.decode("utf-16"), "utf-16"
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw.decode("utf-8-sig"), "utf-8-sig"
    return raw.decode("utf-8"), "utf-8"


touched: list[str] = []


def save(path: Path, text: str, enc: str) -> None:
    path.write_text(text, encoding=enc)
    touched.append(str(path.relative_to(ROOT)))


# --- Builds ---
builds = {
    "build_uniajc_prog2_curso.py": True,
    "build_uniajc_seminario_curso.py": True,
    "build_uniajc_bd2_curso.py": True,
    "build_uniajc_arq_curso.py": False,
}
for name, night in builds.items():
    p = ROOT / ".config" / "slides" / name
    text, enc = read_text_any(p)
    new = replace_common(text, night=night)
    new = new.replace("Presencialidad asistida", "Virtual")
    if night:
        new = new.replace("18:00 – 20:00", "20:00 – 22:00")
        new = new.replace("18:00-20:00", "20:00-22:00")
        new = new.replace("18:00–20:00", "20:00–22:00")
        new = new.replace('inicio_clase="18:10"', 'inicio_clase="20:10"')
        new = new.replace("inicio_clase='18:10'", "inicio_clase='20:10'")
    if new != text:
        save(p, new, enc)
        print("OK build", name)
    else:
        print("NOCHANGE build", name)

# --- semestre JSON ---
jp = ROOT / ".config" / "calendario" / "semestre_2026_2.json"
data = json.loads(jp.read_text(encoding="utf-8"))
data["logica_evaluacion"] = (
    "Tres cortes 30%/30%/40%. Parcial al finalizar cada corte en la última clase regular del corte (no en autónoma). "
    "Corte 3 incluye Proyecto Integrador. " + CRIT_NEW
)
night_keys = {"programacion_ii", "seminario", "bases_datos_ii"}
for key, curso in data["cursos"].items():
    curso["modalidad"] = "Virtual"
    if key in night_keys:
        curso["horario"] = "20:00 – 22:00"
    for c in curso.get("clases", []):
        if c.get("tipo") == "presencial":
            c["tipo"] = "virtual"
data["modalidad_cursos"] = "Virtual (todos los cursos)"
data["regla_parciales"] = CRIT_NEW
data["regla_modalidad_sesion"] = (
    "Clases regulares virtual (síncrona); parciales síncronos (virtual); festivos autónoma."
)
jp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
touched.append(str(jp.relative_to(ROOT)))
print("OK semestre json")

# --- uniajc.json ---
up = ROOT / ".config" / "universidades" / "uniajc.json"
uj = json.loads(up.read_text(encoding="utf-8"))
uj["_cursos_workspace"] = [
    "Programacion II (FI303204 · grupo 341C · 2026-1 · mié 20:00-22:00 · 120 min · Virtual)",
    "Seminario de Sistemas (FI303301 · grupo 341C · 2026-1 · jue 20:00-22:00 · 120 min · Virtual)",
    "Bases de Datos II (FI303215 · grupo 641A-2 · 2026-2 · lun 20:00-22:00 · 120 min · Virtual)",
    "Arquitectura de Sistemas Computacionales (FI303380 · grupo 6303C · 2026-2 · lun 10:00-12:00 · 120 min · Virtual)",
    "0. Base (referencia Ingeniería de Software 1 / plantillas institucionales)",
]
uj["periodo_vigente"]["regla_parciales"] = CRIT_NEW
uj["periodo_vigente"]["modalidad_cursos"] = "Virtual"
uj["periodo_vigente"]["regla_modalidad_sesion"] = (
    "Clases regulares virtual (síncrona); parciales síncronos (virtual); festivos autónoma."
)
ex = uj["estandar_material"]["presentacion_del_curso"]["hora_inicio_efectiva"]["ejemplos"]
ex["Programacion II"] = "mié 20:00–22:00 → 20:10"
ex["Seminario de Sistemas"] = "jue 20:00–22:00 → 20:10"
ex["Bases de Datos II"] = "lun 20:00–22:00 → 20:10"
uj["pedagogia"]["_nota_duracion"] = (
    "Periodo 2026-2 (10/08/2026–22/11/2026). Todos los cursos: Virtual. Modalidad por sesión: clases regulares virtual (síncrona); "
    "parciales síncronos (virtual); festivos autónoma. Duraciones: Programación II 341C mié 20:00–22:00 = 120 min; "
    "Seminario 341C jue 20:00–22:00 = 120 min; Bases de Datos II 641A-2 lun 20:00–22:00 = 120 min; "
    "Arquitectura lun 10:00–12:00 = 120 min."
)
uj["pedagogia"]["metodologia_observada_prog2"]["modalidad"] = (
    "Virtual (clases y parciales síncronos · festivos autónomos)"
)
uj["evaluacion"]["_nota"] = (
    "Copia SIEMPRE del Acuerdo pedagógico del grupo. Teórico 2026-2: 30/30/40. " + CRIT_NEW
)
uj["evaluacion"]["teorico_2026_2"]["_logica"] = (
    "Tres cortes 30%/30%/40%. Parcial al finalizar cada corte en la última clase regular del corte (no en autónoma). "
    "Corte 3 incluye Proyecto Integrador. " + CRIT_NEW
)
uj["evaluacion"]["teorico_2026_2"]["criterio_parciales"] = CRIT_NEW
up.write_text(json.dumps(uj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
touched.append(str(up.relative_to(ROOT)))
print("OK uniajc.json")

# --- Markdown plans/calendars ---
md_files = [
    (ROOT / "Programacion II" / "Plan curso" / "2026-1" / "CALENDARIO_2026-1.md", True),
    (ROOT / "Programacion II" / "Plan curso" / "2026-1" / "PLAN_DE_CURSO_2026-1.md", True),
    (ROOT / "Seminario de Sistemas" / "Plan curso" / "2026-1" / "CALENDARIO_2026-1.md", True),
    (ROOT / "Seminario de Sistemas" / "Plan curso" / "2026-1" / "PLAN_DE_CURSO_2026-1.md", True),
    (ROOT / "Bases de Datos II" / "Plan curso" / "2026-2" / "CALENDARIO_2026-2.md", True),
    (ROOT / "Bases de Datos II" / "Plan curso" / "2026-2" / "PLAN_DE_CURSO_2026-2.md", True),
    (ROOT / "Arquitectura de Sistemas Computacionales" / "Plan curso" / "2026-2" / "CALENDARIO_2026-2.md", False),
    (ROOT / "Arquitectura de Sistemas Computacionales" / "Plan curso" / "2026-2" / "PLAN_DE_CURSO_2026-2.md", False),
]
for p, night in md_files:
    text = p.read_text(encoding="utf-8")
    new = replace_common(text, night=night)
    new = new.replace("| Presencial |", "| Virtual (síncrona) |")
    new = new.replace("· Presencial", "· Virtual (síncrona)")
    new = new.replace("Virtual (síncrona) (síncrona)", "Virtual (síncrona)")
    if new != text:
        save(p, new, "utf-8")
        print("OK md", p.relative_to(ROOT))
    else:
        print("NOCHANGE md", p.relative_to(ROOT))

# --- CSV eventos ---
csv_files = [
    (ROOT / "Programacion II" / "Plan curso" / "2026-1" / "calendario_eventos_2026-1.csv", True),
    (ROOT / "Seminario de Sistemas" / "Plan curso" / "2026-1" / "calendario_eventos_2026-1.csv", True),
    (ROOT / "Bases de Datos II" / "Plan curso" / "2026-2" / "calendario_eventos_2026-2.csv", True),
    (
        ROOT
        / "Arquitectura de Sistemas Computacionales"
        / "Plan curso"
        / "2026-2"
        / "calendario_eventos_2026-2.csv",
        False,
    ),
]
for p, night in csv_files:
    raw = p.read_text(encoding="utf-8-sig")
    new = raw
    if night:
        new = new.replace(",18:00,20:00,", ",20:00,22:00,")
    new = new.replace(",presencial,", ",virtual,")
    new = new.replace("parcial presencial sincrono", "parcial virtual sincrono")
    if new != raw:
        save(p, new, "utf-8-sig")
        print("OK csv", p.relative_to(ROOT))
    else:
        print("NOCHANGE csv", p.relative_to(ROOT))

# --- Rules / agents (text) ---
rule_files = [
    ROOT / ".cursor" / "rules" / "uniajc-docente.mdc",
    ROOT / ".claude" / "agents" / "disenador-curricular-uniajc.md",
    ROOT / ".cursor" / "agents" / "disenador-curricular-uniajc.md",
    ROOT / ".claude" / "agents" / "uniajc-dudas-material.md",
]
for p in rule_files:
    if not p.exists():
        print("MISSING", p)
        continue
    text, enc = read_text_any(p)
    new = replace_common(text, night=True)
    # Architecture keep 10:00-12:00 — replace_common night also changes 18->20 which is fine;
    # but may have changed Arq examples incorrectly if they had 18. Fix modalidad-only leftovers.
    new = new.replace("Presencialidad asistida", "Virtual")
    # Fix agent examples that still say mié 18 after night replace should be 20
    new = new.replace("mié 18:00–20:00", "mié 20:00–22:00")
    new = new.replace("jue 18:00–20:00", "jue 20:00–22:00")
    new = new.replace("lun 18:00–20:00", "lun 20:00–22:00")
    new = new.replace("18:00→`Inicio de clase: 18:10`", "20:00→`Inicio de clase: 20:10`")
    new = new.replace('inicio_clase="18:10"', 'inicio_clase="20:10"')
    new = new.replace(
        "Clase 1 presencial · resto virtual · parciales presencial",
        "clases y parciales síncronos · festivos autónomos",
    )
    new = new.replace(
        "Clase 1 presencial; demás regulares virtual (síncrona); parciales presencial; festivos autónoma.",
        "Clases regulares virtual (síncrona); parciales síncronos (virtual); festivos autónoma.",
    )
    new = new.replace(
        "Por sesión: Clase 1 presencial · resto virtual · parciales presencial · festivos autónoma.",
        "Por sesión: clases regulares virtual (síncrona); parciales síncronos (virtual); festivos autónoma.",
    )
    # Footer version strings
    new = new.replace("· Presencialidad asistida ·", "· Virtual ·")
    new = new.replace("· Virtual · Motor", "· Virtual · Motor")  # noop keep
    if new != text:
        save(p, new, enc)
        print("OK rule", p.relative_to(ROOT))
    else:
        print("NOCHANGE rule", p.relative_to(ROOT))

print("\nTOTAL touched:", len(touched))
for t in touched:
    print(" -", t)
