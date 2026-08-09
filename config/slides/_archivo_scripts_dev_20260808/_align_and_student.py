# -*- coding: utf-8 -*-
"""Alinea builds Prog2/Seminario al formato BD2/Arq + cronogramas en Clases/."""
from __future__ import annotations

import csv
import io
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLIDES = Path(__file__).resolve().parent


def read_any(p: Path) -> str:
    b = p.read_bytes()
    if len(b) > 1 and b[1:2] == b"\x00":
        return b.decode("utf-16-le")
    if b[:2] == b"\xff\xfe":
        return b.decode("utf-16")
    return b.decode("utf-8")


def write_utf8(p: Path, text: str) -> None:
    p.write_text(text, encoding="utf-8")


CLASE1 = {
    "Programacion II": "Presentación del curso · Introducción a POO",
    "Seminario de Sistemas": "Presentación del curso · Conceptos iniciales",
    "Bases de Datos II": "Presentación del curso · Revisión de Bases de Datos I",
    "Arquitectura de Sistemas Computacionales": (
        "Presentación del curso · Introducción a arquitecturas cloud"
    ),
}

CSV_NAME = {
    "Programacion II": "Programación II",
    "Seminario de Sistemas": "Seminario de Sistemas",
    "Bases de Datos II": "Bases de Datos II",
    "Arquitectura de Sistemas Computacionales": (
        "Arquitectura de Sistemas Computacionales"
    ),
}

CFG_CSV = {
    "Programacion II": "eventos_programacion_ii_2026-2.csv",
    "Seminario de Sistemas": "eventos_seminario_2026-2.csv",
    "Bases de Datos II": "eventos_bases_datos_ii_2026-2.csv",
    "Arquitectura de Sistemas Computacionales": "eventos_arquitectura_2026-2.csv",
}

touched: list[str] = []


def touch(p: Path) -> None:
    touched.append(str(p.relative_to(ROOT)).replace("\\", "/"))


def patch_prog2() -> None:
    p = SLIDES / "build_uniajc_prog2_curso.py"
    t = read_any(p)

    if "Modalidad: **Presencialidad asistida**" not in t.split("course_cover")[1][:800]:
        t = re.sub(
            r'("Horario: \*\*Miércoles 18:00[^\n]+",\n)(\s*"Docente:)',
            r'\1            "Modalidad: **Presencialidad asistida** '
            r'(Clase 1 presencial · resto virtual · parciales presencial · festivos autónomos)",\n\2',
            t,
            count=1,
        )

    t = re.sub(
        r'\[\s*\n\s*\["1", "12/08", "Presencial", "30%"\],\s*\n'
        r'\s*\["2", "19/08", "Virtual", "30%"\],\s*\n'
        r'\s*\["3", "26/08", "Virtual", "40%"\],\s*\n\s*\],\s*\n'
        r'\s*note="[^"]*",',
        '[\n'
        '            ["1", "12/08–13/09", "Parcial 10% · Talleres/Quiz 10% · Asistencia 10%", "30%"],\n'
        '            ["2", "14/09–18/10", "Parcial 10% · Talleres/Quiz 10% · Asistencia 10%", "30%"],\n'
        '            ["3", "19/10–22/11", "Parcial 15% · PI 20% · Asistencia 5%", "40%"],\n'
        "        ],\n"
        '        note="Parciales síncronos en Clases 5/10/15 (mié). Nunca en autónoma.",',
        t,
        count=1,
    )

    t = t.replace(
        '{"n": 1, "tema": "Introducción a POO", "fecha": "12/08"}',
        '{"n": 1, "tema": "Presentación del curso · Introducción a POO", "fecha": "12/08"}',
    )

    t = re.sub(
        r'\("info", "Horario fijo del grupo 341C:[^"]*"\),\s*\n'
        r'\s*\("aclaracion", "[^"]*"\),\s*\n'
        r'\s*\("advertencia", "[^"]*"\),',
        '("info", "Miércoles 18:00-20:00 (120 min). Modalidad: Presencialidad asistida '
        '(Clase 1 presencial / resto virtual / parciales presencial). Grupo: 341C."),\n'
        '            ("aclaracion", "Clase 1 = Presentación del curso + arranque temático '
        '(Introducción a POO). Material estudiante solo en carpeta Clases/."),\n'
        '            ("advertencia", "Parciales NUNCA en autónoma: P1=Clase 5 (09/09), '
        'P2=Clase 10 (14/10), P3=Clase 15 (18/11)."),',
        t,
        count=1,
    )

    t = t.replace(
        "Material de clase: carpeta `Clases/Clase N` + talleres en Campus Virtual.",
        "Material de clase: carpeta compartida `Clases/` (Presentación del Curso, Cronograma, Clase N).",
    )
    t = t.replace("Verificar en Campus Virtual.", "")
    write_utf8(p, t)
    touch(p)


def patch_seminario() -> None:
    p = SLIDES / "build_uniajc_seminario_curso.py"
    t = read_any(p)

    # cover: add modalidad if missing after horario
    if "Modalidad:" not in t.split("course_cover")[1][:900]:
        t = re.sub(
            r'("Horario: \*\*Jueves 18:00[^\n]+",\n)(\s*"Docente:)',
            r"\1        'Modalidad: **Presencialidad asistida** "
            r"(Clase 1 presencial · resto virtual · parciales presencial · festivos autónomos)',\n\2",
            t,
            count=1,
        )
        # also single-quote style
        t = re.sub(
            r"('Horario: \*\*Jueves 18:00[^\n]+',\n)(\s*'Docente:)",
            r"\1        'Modalidad: **Presencialidad asistida** "
            r"(Clase 1 presencial · resto virtual · parciales presencial · festivos autónomos)',\n\2",
            t,
            count=1,
        )

    t = re.sub(
        r'\[\s*\n\s*\["1", "13/08", "Presencial", "30%"\],\s*\n'
        r'\s*\["2", "20/08", "Virtual", "30%"\],\s*\n'
        r'\s*\["3", "27/08", "Virtual", "40%"\],\s*\n\s*\],\s*\n'
        r'\s*note="[^"]*",',
        '[\n'
        '            ["1", "13/08–13/09", "Parcial 10% · Talleres/Quiz 10% · Asistencia 10%", "30%"],\n'
        '            ["2", "14/09–18/10", "Parcial 10% · Talleres/Quiz 10% · Asistencia 10%", "30%"],\n'
        '            ["3", "19/10–22/11", "Parcial 15% · PI 20% · Asistencia 5%", "40%"],\n'
        "        ],\n"
        '        note="Parciales síncronos en Clases 5/10/15 (jue). Nunca en autónoma.",',
        t,
        count=1,
    )

    t = t.replace(
        '{"n": 1, "tema": "Acuerdo y conceptos", "fecha": "13/08"}',
        '{"n": 1, "tema": "Presentación del curso · Conceptos iniciales", "fecha": "13/08"}',
    )

    t = re.sub(
        r"\('info', 'Horario fijo del grupo 341C:[^']*'\),\s*\n"
        r"\s*\('aclaracion', '[^']*'\),\s*\n"
        r"\s*\('advertencia', '[^']*'\),",
        "('info', 'Jueves 18:00-20:00 (120 min). Modalidad: Presencialidad asistida "
        "(Clase 1 presencial / resto virtual / parciales presencial). Grupo: 341C.'),\n"
        "            ('aclaracion', 'Clase 1 = Presentación del curso + arranque temático "
        "(Conceptos iniciales). Material estudiante solo en carpeta Clases/.'),\n"
        "            ('advertencia', 'Parciales NUNCA en autónoma: P1=Clase 5 (10/09), "
        "P2=Clase 10 (15/10), P3=Clase 15 (19/11).'),",
        t,
        count=1,
    )
    # double-quote variant
    t = re.sub(
        r'\("info", "Horario fijo del grupo 341C:[^"]*"\),\s*\n'
        r'\s*\("aclaracion", "[^"]*"\),\s*\n'
        r'\s*\("advertencia", "[^"]*"\),',
        '("info", "Jueves 18:00-20:00 (120 min). Modalidad: Presencialidad asistida '
        '(Clase 1 presencial / resto virtual / parciales presencial). Grupo: 341C."),\n'
        '            ("aclaracion", "Clase 1 = Presentación del curso + arranque temático '
        '(Conceptos iniciales). Material estudiante solo en carpeta Clases/."),\n'
        '            ("advertencia", "Parciales NUNCA en autónoma: P1=Clase 5 (10/09), '
        'P2=Clase 10 (15/10), P3=Clase 15 (19/11)."),',
        t,
        count=1,
    )

    t = t.replace(
        "Material: `Clases/Clase N` + entregas en Campus Virtual.",
        "Material: carpeta compartida `Clases/` (Presentación del Curso, Cronograma, Clase N).",
    )
    write_utf8(p, t)
    touch(p)


def patch_bd2_arq_clase1() -> None:
    for rel, old, new in [
        (
            "build_uniajc_bd2_curso.py",
            '{"n": 1, "tema": "Presentación · Revisión BD I", "fecha": "10/08"}',
            '{"n": 1, "tema": "Presentación del curso · Revisión de Bases de Datos I", "fecha": "10/08"}',
        ),
        (
            "build_uniajc_arq_curso.py",
            '{"n": 1, "tema": "Presentación · Introducción a arquitecturas cloud", "fecha": "10/08"}',
            '{"n": 1, "tema": "Presentación del curso · Introducción a arquitecturas cloud", "fecha": "10/08"}',
        ),
    ]:
        p = SLIDES / rel
        t = read_any(p)
        if old in t:
            t = t.replace(old, new)
            write_utf8(p, t)
            touch(p)
        elif new in t:
            print("OK already", rel)
        else:
            # fuzzy
            t2 = re.sub(
                r'\{"n": 1, "tema": "[^"]+", "fecha": "10/08"\}',
                new,
                t,
                count=1,
            )
            if t2 != t:
                write_utf8(p, t2)
                touch(p)
            else:
                print("MISS", rel)


def patch_plan_and_csv() -> None:
    for folder, tema in CLASE1.items():
        plan = ROOT / folder / "Plan curso" / "PLAN_DE_CURSO_2026-2.md"
        text = read_any(plan)
        out = []
        changed = False
        for line in text.splitlines():
            if line.startswith("| 1 |") and "Presencial" in line:
                parts = line.split("|")
                if len(parts) >= 5:
                    nl = "|".join(parts[:4] + [f" {tema} "] + parts[5:])
                    if nl != line:
                        changed = True
                    out.append(nl)
                    continue
            out.append(line)
        if changed:
            write_utf8(plan, "\n".join(out) + ("\n" if text.endswith("\n") else ""))
            touch(plan)

        name = CSV_NAME[folder]
        paths = [
            ROOT / folder / "Plan curso" / "calendario_eventos_2026-2.csv",
            ROOT / ".config" / "calendario" / CFG_CSV[folder],
            ROOT / ".config" / "calendario" / "eventos_todos_cursos_2026-2.csv",
        ]
        for path in paths:
            if not path.exists():
                continue
            rows = list(csv.reader(io.StringIO(path.read_text(encoding="utf-8-sig"))))
            if not rows:
                continue
            h = rows[0]
            ic, inn, it = h.index("curso"), h.index("clase_n"), h.index("tema")
            ch = False
            for row in rows[1:]:
                if len(row) > max(ic, inn, it) and row[ic] == name and row[inn] == "1":
                    if row[it] != tema:
                        row[it] = tema
                        ch = True
            if ch:
                buf = io.StringIO()
                csv.writer(buf, lineterminator="\n").writerows(rows)
                path.write_text(buf.getvalue(), encoding="utf-8-sig")
                touch(path)


def write_cronogramas() -> None:
    for folder, tema in CLASE1.items():
        plan = ROOT / folder / "Plan curso" / "PLAN_DE_CURSO_2026-2.md"
        text = read_any(plan)
        rows = []
        for line in text.splitlines():
            if re.match(r"^\|\s*\d+\s*\|", line):
                parts = [p.strip() for p in line.strip("|").split("|")]
                if len(parts) >= 4 and parts[0].isdigit():
                    n, fecha, tipo, tem = parts[0], parts[1], parts[2], parts[3]
                    parcial = "sí" if "Parcial" in tem else "no"
                    rows.append((n, fecha, tipo, tem, parcial))

        clases = ROOT / folder / "Clases"
        clases.mkdir(parents=True, exist_ok=True)
        codigo = re.search(r"\*\*Código:\*\*\s*(.+)", text)
        grupo = re.search(r"\*\*Grupo:\*\*\s*(.+)", text)
        horario = re.search(r"\*\*Horario:\*\*\s*(.+)", text)
        lines = [
            f"# Cronograma 2026-2 — {folder}",
            "",
            "Documento para estudiantes (carpeta compartida `Clases/`).",
            "",
        ]
        if codigo:
            lines.append(f"- **Código:** {codigo.group(1).strip()}")
        if grupo:
            lines.append(f"- **Grupo:** {grupo.group(1).strip()}")
        if horario:
            lines.append(f"- **Horario:** {horario.group(1).strip()}")
        lines += [
            "- **Periodo:** 2026-2 · 10/08/2026 – 22/11/2026",
            "- **Modalidad:** Presencialidad asistida (Clase 1 presencial · resto virtual · parciales presencial · festivos autónomos)",
            "",
            "> La **Clase 1** incluye la Presentación del curso (acuerdo, logística, Padlet, evaluación, cronograma) **y** el arranque temático.",
            "",
            "| Clase | Fecha | Tipo | Tema | Parcial |",
            "|---|---|---|---|---|",
        ]
        for n, fecha, tipo, tem, parcial in rows:
            lines.append(f"| {n} | {fecha} | {tipo} | {tem} | {parcial} |")
        lines += [
            "",
            "Fuente derivada del Plan de curso 2026-2. Detalle docente interno no se comparte aquí.",
            "",
        ]
        out = clases / "Cronograma 2026-2.md"
        write_utf8(out, "\n".join(lines))
        touch(out)

        src = ROOT / folder / "Plan curso" / "calendario_eventos_2026-2.csv"
        dst = clases / "calendario_eventos_2026-2.csv"
        if src.exists():
            shutil.copy2(src, dst)
            touch(dst)


def patch_config_rules_agents() -> None:
    jp = ROOT / ".config" / "universidades" / "uniajc.json"
    data = json.loads(read_any(jp))
    em = data.setdefault("estandar_material", {})
    em["carpeta_compartida_estudiantes"] = {
        "_regla": (
            "El docente solo comparte con estudiantes la carpeta Clases/ de cada curso. "
            "TODO el material estudiante debe vivir ahí."
        ),
        "incluye": [
            "Presentacion del Curso - ….pptx",
            "Cronograma 2026-2.md",
            "calendario_eventos_2026-2.csv (copia)",
            "Clase N - Tema/Presentacion.pptx + taller estudiante",
        ],
        "no_incluye": [
            "Entregas docente/ (Acuerdo, Diagnóstico)",
            "Plan curso/ (Microcurrículo, planes internos)",
            "Guiones/",
            "Kit docente/",
        ],
    }
    em["clase_1"] = {
        "_regla": (
            "La Clase 1 siempre combina Presentación del curso + arranque temático "
            "de la primera unidad (no solo logística)."
        ),
        "incluye": [
            "Presentación del curso (acuerdo, logística, Padlet, evaluación, cronograma)",
            "Un poco del tema de la primera unidad",
        ],
        "guion_y_slides": (
            "Guion/slides de Clase 1 = Presentación del Curso + primer bloque temático."
        ),
        "wording_plan": "Presentación del curso · [tema intro]",
    }
    if "pedagogia" in data and "duracion_por_curso" in data["pedagogia"]:
        data["pedagogia"]["duracion_por_curso"][
            "Arquitectura de Sistemas Computacionales"
        ] = 120
    # cursos workspace arq line
    cursos = data.get("_cursos_workspace", [])
    data["_cursos_workspace"] = [
        c.replace("10:00-13:00 · 180 min", "10:00-12:00 · 120 min")
        .replace("10:00–13:00 · 180 min", "10:00–12:00 · 120 min")
        for c in cursos
    ]
    write_utf8(jp, json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    touch(jp)

    rp = ROOT / ".cursor" / "rules" / "uniajc-docente.mdc"
    rt = read_any(rp)
    rt = rt.replace("lun **10:00–13:00** · **180 min**", "lun **10:00–12:00** · **120 min**")
    rt = rt.replace("Arquitectura = **180 min**", "Arquitectura = **120 min**")
    rt = rt.replace(
        "usar duración real del curso: 120 o 180 min",
        "usar duración real del curso: **120 min**",
    )
    block = """
## Carpeta compartida con estudiantes

- El docente **solo comparte** la carpeta `Clases/` de cada curso.
- Ahí debe existir: Presentación del Curso `.pptx`, `Cronograma 2026-2.md`, copia del CSV de eventos si aplica, y `Clase N - Tema/` (presentación + taller estudiante).
- **No** poner en `Clases/`: Acuerdo/Diagnóstico (`Entregas docente/`), Microcurrículo/planes internos (`Plan curso/`), guiones (`Guiones/` / `Kit docente/`).

## Clase 1 (fija)

- La **Clase 1** siempre incluye: (1) Presentación del curso (acuerdo, logística, Padlet, evaluación, cronograma) + (2) arranque temático de la primera unidad.
- Guion/slides de Clase 1 = Presentación del Curso + primer bloque temático.
- Wording del plan/CONTENIDO: `Presentación del curso · [tema intro]`.
"""
    if "Carpeta compartida con estudiantes" not in rt:
        if "# Builds y marca" in rt:
            rt = rt.replace("# Builds y marca", block + "\n# Builds y marca")
        else:
            rt = rt.rstrip() + "\n" + block
    write_utf8(rp, rt)
    touch(rp)

    snip = """
## Carpeta compartida con estudiantes
Solo se comparte `Clases/`. Ahí: Presentación del Curso, Cronograma 2026-2.md (+ CSV si aplica), material de Clase N. No poner Acuerdo/Microcurrículo/guiones en `Clases/`.

## Clase 1
Siempre: Presentación del curso + arranque temático de la primera unidad. Wording: `Presentación del curso · [tema intro]`. Guion/slides Clase 1 = PPTX del curso + primer bloque temático.
"""
    for ap in [
        ROOT / ".cursor" / "agents" / "disenador-curricular-uniajc.md",
        ROOT / ".claude" / "agents" / "disenador-curricular-uniajc.md",
        ROOT / ".cursor" / "agents" / "uniajc-dudas-material.md",
        ROOT / ".claude" / "agents" / "uniajc-dudas-material.md",
    ]:
        if not ap.exists():
            continue
        at = read_any(ap)
        at = at.replace("lun 10:00–13:00 (180 min)", "lun 10:00–12:00 (120 min)")
        at = at.replace(
            "120 min Prog. II / Seminario / BD II; 180 min Arquitectura",
            "**120 min** en todos los cursos activos 2026-2, incl. Arquitectura lun 10:00–12:00",
        )
        if "Carpeta compartida con estudiantes" not in at:
            if "# FLUJO ESTÁNDAR" in at:
                at = at.replace("# FLUJO ESTÁNDAR", snip + "\n# FLUJO ESTÁNDAR")
            elif "## Separación material" in at:
                at = at.replace("## Separación material", snip + "\n## Separación material")
            else:
                at = at.rstrip() + "\n" + snip
        write_utf8(ap, at)
        touch(ap)


def rebuild() -> None:
    for script in [
        "build_uniajc_prog2_curso.py",
        "build_uniajc_seminario_curso.py",
        "build_uniajc_bd2_curso.py",
        "build_uniajc_arq_curso.py",
    ]:
        r = subprocess.run(
            [sys.executable, str(SLIDES / script)],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
        )
        print(script, "->", r.returncode, (r.stdout or r.stderr).strip()[:200])


def main() -> None:
    patch_prog2()
    patch_seminario()
    patch_bd2_arq_clase1()
    patch_plan_and_csv()
    write_cronogramas()
    patch_config_rules_agents()
    rebuild()
    print("TOUCHED", len(touched))
    for item in touched:
        print(" -", item)

    print("\n=== CLASE 1 FINAL ===")
    for folder, tema in CLASE1.items():
        print(f"- {folder}: {tema}")

    print("\n=== CLASES/ ROOT FILES ===")
    for folder in CLASE1:
        clases = ROOT / folder / "Clases"
        for f in sorted(clases.iterdir()):
            if f.is_file() and f.name != "desktop.ini":
                print(f"  {folder}/Clases/{f.name}")


if __name__ == "__main__":
    main()
