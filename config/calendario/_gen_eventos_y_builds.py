# -*- coding: utf-8 -*-
from __future__ import annotations
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos")
SLIDES = ROOT / ".config" / "slides"
CAL = ROOT / ".config" / "calendario" / "semestre_2026_2.json"

CRITERIO_NOTA = "parcial presencial sincrono; nunca en festivo/autonoma; pendiente listado estudiantes"

def must_replace(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        # try ascii-normalized fallbacks for dashes
        raise SystemExit(f"Missing in {label}: {old[:100]!r}")
    return text.replace(old, new)

def patch_builds() -> None:
    # ARQ
    p = SLIDES / "build_uniajc_arq_curso.py"
    t = p.read_text(encoding="utf-8")
    reps = [
        ("Modalidad: **[PENDIENTE \u2014 modalidad]**", "Modalidad: **Presencialidad asistida**"),
        ("Parcial 2 (Clase 10) 10%", "Parcial 2 (Clase 9 \u00b7 05/10) 10%"),
        ("Parcial 3 (Clase 15) 15%", "Parcial 3 (Clase 14 \u00b7 09/11) 15%"),
        (
            "L\u00f3gica Acuerdos 2026-2. Parcial al cierre de cada corte. Listado: [PENDIENTE listado].",
            "Parciales sincronos en ultima clase regular del corte (nunca en autonoma). Lun: Clases 5/9/14. Listado: [PENDIENTE listado].",
        ),
        (
            "Clases 9\u201315: CI/CD, costos/sostenibilidad (Parcial 2 \u00b7 12/10), avance PI, rendimiento, autoescalado, prep. y cierre (Parcial 3 \u00b7 16/11). Ver PLAN_DE_CURSO_2026-2.md.",
            "Clases 9-15: CI/CD + Parcial 2 (05/10); costos (12/10 autonoma sin parcial); avance PI; rendimiento; autoescalado; prep. + Parcial 3 (09/11); cierre 16/11 autonomo. Ver PLAN_DE_CURSO_2026-2.md.",
        ),
        (
            "Lunes 10:00\u201313:00 (180 min). Grupo y modalidad: [PENDIENTE].",
            "Lunes 10:00-13:00 (180 min). Modalidad: Presencialidad asistida. Grupo: [PENDIENTE].",
        ),
        (
            "Parciales 2 y 3 en clase aut\u00f3noma. Listado: [PENDIENTE listado].",
            "Parciales NUNCA en autonoma: P2=Clase 9 (05/10), P3=Clase 14 (09/11). Listado: [PENDIENTE listado].",
        ),
    ]
    for old, new in reps:
        if old not in t:
            print("WARN arq skip:", old[:70])
        else:
            t = t.replace(old, new)
    p.write_text(t, encoding="utf-8")
    print("OK patch arq")

    # BD2
    p = SLIDES / "build_uniajc_bd2_curso.py"
    t = p.read_text(encoding="utf-8")
    reps = [
        ("Modalidad: **Virtual**", "Modalidad: **Presencialidad asistida** (virtual sincrona)"),
        ("Modalidad: **virtual** (grupo 641A-2).", "Modalidad: **Presencialidad asistida** \u00b7 franja virtual sincrona (grupo 641A-2)."),
        ("Parcial 2 (Clase 10) 10%", "Parcial 2 (Clase 9 \u00b7 05/10) 10%"),
        ("Parcial 3 (Clase 15) 15%", "Parcial 3 (Clase 14 \u00b7 09/11) 15%"),
        (
            "L\u00f3gica Acuerdos 2026-2. Parcial al cierre de cada corte. Listado: [PENDIENTE listado].",
            "Parciales sincronos en ultima clase regular del corte (nunca en autonoma). Lun: Clases 5/9/14. Listado: [PENDIENTE listado].",
        ),
        (
            "Clases 9\u201315: transacciones, concurrencia (Parcial 2 \u00b7 12/10 aut\u00f3noma), avance PI, integraci\u00f3n, casos, prep. y cierre (Parcial 3 \u00b7 16/11 aut\u00f3noma). Ver PLAN_DE_CURSO_2026-2.md.",
            "Clases 9-15: transacciones + Parcial 2 (05/10); concurrencia (12/10 autonoma sin parcial); avance PI; integracion; casos; prep. + Parcial 3 (09/11); cierre 16/11 autonomo. Ver PLAN_DE_CURSO_2026-2.md.",
        ),
        (
            "Lunes 18:00\u201320:00 \u00b7 Virtual \u00b7 grupo 641A-2.",
            "Lunes 18:00-20:00 \u00b7 Presencialidad asistida (virtual sincrona) \u00b7 grupo 641A-2.",
        ),
        (
            "Parciales 2 y 3 caen en clase aut\u00f3noma: entrega as\u00edncrona. Listado: [PENDIENTE listado].",
            "Parciales NUNCA en autonoma: P2=Clase 9 (05/10), P3=Clase 14 (09/11). Listado: [PENDIENTE listado].",
        ),
        ("Lunes **18:00 \u2013 20:00** \u00b7 Virtual", "Lunes **18:00 \u2013 20:00** \u00b7 Presencialidad asistida"),
    ]
    for old, new in reps:
        if old not in t:
            print("WARN bd2 skip:", old[:70])
        else:
            t = t.replace(old, new)
    p.write_text(t, encoding="utf-8")
    print("OK patch bd2")

    # Prog2 / Seminario notes
    for name, old, new in [
        (
            "build_uniajc_prog2_curso.py",
            "Fuente: Acuerdo pedag\u00f3gico 2026-2 (te\u00f3rico) \u00b7 Grupo 341C. Parcial al cierre de cada corte. Verificar en Campus Virtual.",
            "Fuente: Acuerdo 2026-2 \u00b7 Grupo 341C. Parciales sincronos en Clases 5/10/15 (sin festivos este dia). Verificar en Campus Virtual.",
        ),
        (
            "build_uniajc_seminario_curso.py",
            "L\u00f3gica Acuerdos 2026-2. Parcial al cierre de cada corte. Listado: [PENDIENTE listado].",
            "Parciales sincronos en Clases 5/10/15 (sin festivos este dia). Nunca en autonoma. Listado: [PENDIENTE listado].",
        ),
    ]:
        p = SLIDES / name
        t = p.read_text(encoding="utf-8")
        if old not in t:
            print("WARN skip", name)
        else:
            p.write_text(t.replace(old, new), encoding="utf-8")
            print("OK patch", name)

def parse_temas(plan_path: Path) -> dict[int, str]:
    text = plan_path.read_text(encoding="utf-8")
    temas: dict[int, str] = {}
    for line in text.splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|\s*[^|]+\|\s*[^|]+\|\s*(.+?)\s*\|?\s*$", line)
        if not m:
            continue
        n = int(m.group(1))
        tema = m.group(2).strip()
        tema = re.sub(r"\s*\*\*Parcial.*$", "", tema).strip()
        tema = re.sub(r"\s*\u00b7\s*refuerzo sin parcial\s*$", "", tema).strip()
        tema = tema.replace("**", "")
        temas[n] = tema
    return temas

def split_horario(horario: str) -> tuple[str, str]:
    # "18:00 – 20:00" or "10:00 – 13:00"
    parts = re.split(r"\s*[\u2013\u2014\-]\s*", horario.strip())
    if len(parts) != 2:
        raise SystemExit(f"Horario no parseable: {horario!r}")
    return parts[0].strip(), parts[1].strip()

def tipo_csv(tipo: str) -> str:
    # user asked: regular | autonoma | virtual
    if tipo == "autonoma":
        return "autonoma"
    if tipo == "virtual":
        return "virtual"
    return "regular"  # presencial síncrona

def gen_csvs(cal: dict) -> None:
    fields = [
        "curso", "codigo_fi", "grupo", "clase_n", "fecha", "dia",
        "hora_inicio", "hora_fin", "tipo_clase", "es_parcial", "parcial_n",
        "sesion_etiqueta", "tema", "notas",
    ]
    all_rows: list[dict] = []
    cfg_dir = ROOT / ".config" / "calendario"
    cfg_dir.mkdir(parents=True, exist_ok=True)

    for key, curso in cal["cursos"].items():
        plan = ROOT / curso["folder"] / "Plan curso" / "PLAN_DE_CURSO_2026-2.md"
        temas = parse_temas(plan)
        h0, h1 = split_horario(curso["horario"])
        grupo = curso.get("grupo") or "[PENDIENTE]"
        if "PENDIENTE" in str(grupo):
            grupo = "[PENDIENTE]"
        rows = []
        for c in curso["clases"]:
            pn = c.get("parcial_n") or ""
            es_parcial = "si" if c.get("parcial") else "no"
            if c.get("parcial"):
                etiqueta = f"Clase {c['n']} \u00b7 Parcial {pn}"
            else:
                etiqueta = f"Clase {c['n']}"
            notas_parts = []
            if c.get("festivo"):
                notas_parts.append(f"festivo: {c['festivo']}")
            if c.get("parcial"):
                notas_parts.append("parcial presencial sincrono")
            if c["tipo"] == "autonoma" and not c.get("parcial"):
                notas_parts.append("clase autonoma / refuerzo sin parcial")
            notas_parts.append("pendiente listado")
            row = {
                "curso": curso["nombre"],
                "codigo_fi": curso.get("codigo", ""),
                "grupo": grupo,
                "clase_n": c["n"],
                "fecha": c["fecha"],
                "dia": curso["dia"],
                "hora_inicio": h0,
                "hora_fin": h1,
                "tipo_clase": tipo_csv(c["tipo"]),
                "es_parcial": es_parcial,
                "parcial_n": pn if pn else "",
                "sesion_etiqueta": etiqueta,
                "tema": temas.get(c["n"], ""),
                "notas": "; ".join(notas_parts),
            }
            rows.append(row)
            all_rows.append(row)

        # per-course CSV in Entregas docente
        out1 = ROOT / curso["folder"] / "Entregas docente" / "calendario_eventos_2026-2.csv"
        out1.parent.mkdir(parents=True, exist_ok=True)
        with out1.open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)

        # config copy
        slug = key
        out2 = cfg_dir / f"eventos_{slug}_2026-2.csv"
        with out2.open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)
        print(f"OK CSV {out1.relative_to(ROOT)} ({len(rows)} filas)")
        print(f"OK CSV {out2.relative_to(ROOT)}")

        # one-line import note in plan
        if plan.exists():
            text = plan.read_text(encoding="utf-8")
            line = (
                "\n> **CSV eventos:** `Entregas docente/calendario_eventos_2026-2.csv` "
                "(UTF-8 BOM). Importar en hoja/calendario cuando exista el listado de estudiantes "
                "(una fila = una clase; filtrar `es_parcial=si` para parciales síncronos).\n"
            )
            if "CSV eventos:" not in text:
                # insert after title
                lines = text.splitlines()
                lines.insert(1, line.strip("\n"))
                plan.write_text("\n".join(lines) + "\n", encoding="utf-8")
                print(f"OK nota CSV en {plan.relative_to(ROOT)}")

    # consolidated
    outc = cfg_dir / "eventos_todos_cursos_2026-2.csv"
    with outc.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(all_rows)
    print(f"OK CSV consolidado {outc.relative_to(ROOT)} ({len(all_rows)} filas)")

    # short README
    readme = cfg_dir / "README_eventos_csv.md"
    readme.write_text(
        "# Calendario de eventos CSV 2026-2\n\n"
        "Archivos `eventos_*_2026-2.csv` y `*/Entregas docente/calendario_eventos_2026-2.csv`: "
        "15 filas/clase por curso, UTF-8 con BOM. "
        "Cuando tengas el listado de estudiantes, importa el CSV a Excel/Google Sheets o genera invitaciones "
        "(una fila = una clase; `es_parcial=si` marca parciales síncronos; nunca caen en `tipo_clase=autonoma`).\n",
        encoding="utf-8",
    )
    print(f"OK {readme.relative_to(ROOT)}")

def rebuild_pptx() -> None:
    sys.path.insert(0, str(SLIDES))
    for mod_name in [
        "build_uniajc_arq_curso",
        "build_uniajc_bd2_curso",
        "build_uniajc_prog2_curso",
        "build_uniajc_seminario_curso",
    ]:
        # reload fresh
        if mod_name in sys.modules:
            del sys.modules[mod_name]
        mod = __import__(mod_name)
        mod.build()
        print(f"OK pptx {mod_name}")

def main() -> None:
    patch_builds()
    cal = json.loads(CAL.read_text(encoding="utf-8"))
    gen_csvs(cal)
    rebuild_pptx()
    print("ALL DONE")

if __name__ == "__main__":
    main()
