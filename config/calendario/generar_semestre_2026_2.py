# -*- coding: utf-8 -*-
"""Genera calendario 2026-2 + Acuerdos pedagógicos prellenados (sin listado de estudiantes)."""
from __future__ import annotations
import json
from datetime import date, timedelta
from pathlib import Path
from docx import Document
ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = (
    ROOT
    / "Programacion II"
    / "Entregas docente"
    / "ACUERDO PEDAGOGICO ACTUALIZADO.docx"
)
FESTIVOS = {
    "2026-08-17": "Asunción de la Virgen",
    "2026-10-12": "Día de la Diversidad Étnica y Cultural",
    "2026-11-02": "Todos los Santos",
    "2026-11-16": "Independencia de Cartagena",
}
START = date(2026, 8, 10)
END = date(2026, 11, 22)
CORTES = {
    "corte_1": {
        "pct": "30%",
        "inicio": "2026-08-10",
        "fin": "2026-09-13",
        "clases": "1-5",
        "parcial_cierre": "Parcial 1 al cerrar el Corte 1 (Clase 5)",
        "desglose": "10% Parcial 1 (cierre de corte) · 10% Talleres y Quiz · 10% Asistencia",
    },
    "corte_2": {
        "pct": "30%",
        "inicio": "2026-09-14",
        "fin": "2026-10-18",
        "clases": "6-10",
        "parcial_cierre": "Parcial 2 al cerrar el Corte 2 (Clase 10)",
        "desglose": "10% Parcial 2 (cierre de corte) · 10% Talleres y Quiz · 10% Asistencia",
    },
    "corte_3": {
        "pct": "40%",
        "inicio": "2026-10-19",
        "fin": "2026-11-22",
        "clases": "11-15",
        "parcial_cierre": "Parcial 3 al cerrar el Corte 3 (Clase 15)",
        "desglose": (
            "15% Parcial 3 (cierre de corte) · 20% Proyecto Integrador · 5% Asistencia"
        ),
    },
}
# Misma lógica de evaluación que Acuerdos 2026-1 de Prog. II / Seminario:
# 30/30/40 con parcial en cada finalización de corte + talleres/quiz + asistencia;
# en Corte 3 el Proyecto Integrador sustituye parte del peso de talleres.
LOGICA_EVALUACION = (
    "Criterio de modalidad por sesion (fijo 2026-2): modalidad del curso = Presencialidad asistida. "
    "Prog II (miercoles): Clase 1 presencial · clases regulares 2-15 virtual sincrona · parciales presencial sincrono. "
    "Seminario (jueves): clases regulares virtual sincrona · parciales presencial sincrono. "
    "Festivos = clase autonoma (sin parcial). Los parciales NUNCA se programan en dia festivo ni en clase autonoma. "
    "Si el cierre teorico del corte cae en festivo/autonoma, el parcial se mueve a la ultima clase regular anterior del mismo corte."
)
DOCENTE = "Julian Andres Castaño Espinosa"
CORREO = "julianacastano@profesores.uniajc.edu.co"
EVAL_TEXT = (
    "Acuerdo sobre los aspectos de evaluación\n"
    "(Cálculo teórico 2026-2 · 30% / 30% / 40% — validar en socialización con el grupo)\n"
    "Parciales: Parcial 1 al cerrar Corte 1 · Parcial 2 al cerrar Corte 2 · "
    "Parcial 3 al cerrar Corte 3 (misma lógica que Acuerdos Prog. II / Seminario).\n\n"
    "Primer corte (30%) — [10/08/2026 al 13/09/2026] · Clases 1–5:\n"
    "* 10% Parcial 1 (cierre de corte, Clase 5) | 10% Talleres y Quiz | 10% Asistencia\n\n"
    "Segundo corte (30%) — [14/09/2026 al 18/10/2026] · Clases 6–10:\n"
    "* 10% Parcial 2 (cierre de corte, Clase 10) | 10% Talleres y Quiz | 10% Asistencia\n\n"
    "Tercer corte (40%) — [19/10/2026 al 22/11/2026] · Clases 11–15:\n"
    "* 15% Parcial 3 (cierre de corte, Clase 15) | 20% Proyecto Integrador | 5% Asistencia\n\n"
    "Nota: parciales NUNCA en festivo/autonoma; se mueven a la ultima clase regular del corte."
)
APROBACION = (
    "[PRELLENADO 2026-2 — pendiente socialización con el grupo]\n"
    "Periodo académico: 10/08/2026 al 22/11/2026.\n"
    "Pendiente: aprobación/ajustes con estudiantes, listado oficial, vocero y firmas.\n"
    "No se inventan nombres ni códigos de estudiantes."
)
CURSOS = {
    "programacion_ii": {
        "folder": "Programacion II",
        "nombre": "Programación II",
        "codigo": "FI303204",
        "grupo": "341C",
        "grupo_acuerdo": "341-C",
        "semestre": "4",
        "programa": "Ingeniería de Sistemas",
        "dia": "Miércoles",
        "weekday": 2,
        "horario": "18:00 – 20:00",
        "duracion_min": 120,
        "modalidad": "Presencialidad asistida (Clase 1 presencial · resto virtual · parciales presencial · festivos autonomos)",
        "tipo_regular": "virtual",
        "clase1_presencial": True,
        "objetivos": (
            "Comprender y aplicar los pilares de la Programación Orientada a Objetos (POO) en Java.\n"
            "Implementar y manipular Estructuras de Datos dinámicas en memoria.\n"
            "Desarrollar Interfaces Gráficas de Usuario (GUI) interactivas.\n"
            "Aplicar patrones de diseño y refactorización con apoyo de IA.\n"
            "Construir persistencia básica integrando lectura y escritura de archivos."
        ),
        "metodologia": (
            "Acuerdo sobre los aspectos metodológicos\n"
            "Periodo 2026-2 · Grupo 341C · Miércoles 18:00–20:00 (120 min).\n"
            "Modalidad: Presencialidad asistida (Clase 1 y parciales presencial sincrono · resto virtual sincrona · festivos = clase autonoma).\n"
            "Estructura de clase: Teoría Core · Taller Guiado calificable "
            "(entrega máx. domingo 23:59) · Quiz corto.\n"
            "Enfoque: aprendizaje activo / ABPr con Proyecto Integrador.\n"
            "Calendario: 15 clases (12/08/2026–18/11/2026). "
            "No hay festivos en miércoles; todas regulares.\n"
            "[Detalle en Plan curso/CALENDARIO_2026-2.md.]"
        ),
    },
    "seminario": {
        "folder": "Seminario de Sistemas",
        "nombre": "Seminario de Sistemas",
        "codigo": "FI303301",
        "grupo": "341C",
        "grupo_acuerdo": "341-C",
        "semestre": "4",
        "programa": "Ingeniería de Sistemas",
        "dia": "Jueves",
        "weekday": 3,
        "horario": "18:00 – 20:00",
        "duracion_min": 120,
        "modalidad": "Presencialidad asistida (jueves virtual sincrona / parciales presencial / festivos autonomos)",
        "tipo_regular": "virtual",
        "objetivos": (
            "Levantar, analizar y documentar requerimientos funcionales y no funcionales "
            "de sistemas de información.\n"
            "Diseñar la arquitectura de software aplicando Patrones de Diseño "
            "(Singleton, Factory) y Diagramas UML.\n"
            'Emplear el paradigma "Docs as Code" (Mermaid, Markdown) para la '
            "documentación técnica y manuales de usuario.\n"
            "Desarrollar habilidades de comunicación asertiva para el Storytelling "
            "y sustentación de proyectos tecnológicos."
        ),
        "metodologia": (
            "Acuerdo sobre los aspectos metodológicos\n"
            "Periodo 2026-2 · Grupo 341C · Jueves 18:00–20:00 (120 min).\n"
            "Modalidad: Presencialidad asistida (Clase 1 y parciales presencial sincrono · resto virtual sincrona · festivos = clase autonoma).\n"
            "Metodología orientada a Role-Playing (Arquitectos / Analistas QA), "
            "talleres con Draw.io/Mermaid, peer review.\n"
            "Calendario: 15 clases (13/08/2026–19/11/2026). "
            "No hay festivos en jueves; todas regulares.\n"
            "[Detalle en Plan curso/CALENDARIO_2026-2.md.]"
        ),
    },
    "bases_datos_ii": {
        "folder": "Bases de Datos II",
        "nombre": "Bases de Datos II",
        "codigo": "FI303215",
        "grupo": "641A-2",
        "grupo_acuerdo": "641A-2",
        "semestre": "[PENDIENTE]",
        "programa": "Ingeniería de Sistemas",
        "dia": "Lunes",
        "weekday": 0,
        "horario": "18:00 – 20:00",
        "duracion_min": 120,
        "modalidad": "Presencialidad asistida (ver tipo por sesión en CSV · parciales presencial · festivos autónomos)",
        "objetivos": (
            "[PENDIENTE — completar con Microcurrículo / Plan de curso de Bases de Datos II]\n"
            "Objetivos oficiales aún no cargados en el workspace."
        ),
        "metodologia": (
            "Acuerdo sobre los aspectos metodológicos\n"
            "Periodo 2026-2 · Grupo 641A-2 · Lunes 18:00–20:00 (120 min) · Modalidad: Presencialidad asistida (Clase 1 y parciales presencial sincrono · resto virtual sincrona · festivos = clase autonoma).\n"
            "Estructura sugerida (ajustar al Acuerdo/Plan): "
            "Teoría Core · Taller Guiado · Quiz/comprobación.\n"
            "Calendario: 15 clases (10/08/2026–16/11/2026). Festivos = clase autónoma:\n"
            "17/08 (Asunción), 12/10 (Diversidad Étnica), "
            "02/11 (Todos los Santos), 16/11 (Independencia de Cartagena).\n"
            "[Detalle en Plan curso/CALENDARIO_2026-2.md.]"
        ),
    },
    "arquitectura": {
        "folder": "Arquitectura de Sistemas Computacionales",
        "nombre": "Arquitectura de Sistemas Computacionales",
        "codigo": "FI303380",
        "grupo": "6303C",
        "grupo_acuerdo": "6303C",
        "semestre": "[PENDIENTE]",
        "programa": "Ingeniería de Sistemas",
        "dia": "Lunes",
        "weekday": 0,
        "horario": "10:00 – 12:00",
        "duracion_min": 120,
        "modalidad": "Virtual (clases y parciales sincronos / festivos autonomos)",
        "objetivos": (
            "[PENDIENTE — completar con Microcurrículo / Plan de curso de "
            "Arquitectura de Sistemas Computacionales]\n"
            "Objetivos oficiales aún no cargados en el workspace."
        ),
        "metodologia": (
            "Acuerdo sobre los aspectos metodológicos\n"
            "Periodo 2026-2 · Lunes 10:00–12:00 (120 min).\n"
            "Grupo: 6303C. Modalidad: Presencialidad asistida (Clase 1 y parciales presencial sincrono · resto virtual sincrona · festivos = clase autonoma).\n"
            "Calendario: 15 clases (10/08/2026–16/11/2026). Festivos = clase autónoma:\n"
            "17/08 (Asunción), 12/10 (Diversidad Étnica), "
            "02/11 (Todos los Santos), 16/11 (Independencia de Cartagena).\n"
            "[Detalle en Plan curso/CALENDARIO_2026-2.md.]"
        ),
    },
}
def class_dates(
    weekday: int,
    tipo_regular: str = "virtual",
    clase1_presencial: bool = True,
) -> list[dict]:
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
            elif n == 1 and clase1_presencial:
                tipo = "presencial"
            else:
                tipo = tipo_regular
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
        target["tipo"] = "presencial"  # parciales siempre presencial sincrono
    return clases


def set_cell_text(cell, text: str) -> None:
    paras = cell.paragraphs
    if not paras:
        cell.text = text
        return
    first = True
    for p in paras:
        if first:
            if p.runs:
                p.runs[0].text = text
                for r in p.runs[1:]:
                    r.text = ""
            else:
                p.add_run(text)
            first = False
        else:
            for r in p.runs:
                r.text = ""
def set_merged_row_value(row, start_col: int, text: str, end_col: int | None = None) -> None:
    end = end_col if end_col is not None else len(row.cells)
    for i in range(start_col, end):
        set_cell_text(row.cells[i], text)
def fill_acuerdo(meta: dict) -> Path:
    doc = Document(str(TEMPLATE))
    t0 = doc.tables[0]
    set_merged_row_value(t0.rows[0], 1, meta["programa"])
    set_merged_row_value(t0.rows[1], 1, meta["nombre"])
    set_cell_text(t0.rows[2].cells[1], meta["grupo_acuerdo"])
    set_cell_text(t0.rows[2].cells[3], meta["semestre"])
    set_cell_text(t0.rows[3].cells[1], "2026-2")
    set_cell_text(t0.rows[3].cells[3], "[PENDIENTE — fecha socialización]")
    set_merged_row_value(t0.rows[4], 1, DOCENTE)
    set_cell_text(doc.tables[1].rows[1].cells[0], meta["objetivos"])
    set_cell_text(doc.tables[2].rows[1].cells[0], APROBACION)
    set_cell_text(doc.tables[3].rows[0].cells[0], meta["metodologia"])
    set_cell_text(doc.tables[3].rows[1].cells[0], EVAL_TEXT)
    t4 = doc.tables[4]
    for c in t4.rows[0].cells[3:]:
        set_cell_text(c, "[PENDIENTE — listado]")
    for c in t4.rows[1].cells[2:]:
        set_cell_text(c, "[PENDIENTE — vocero]")
    set_cell_text(t4.rows[2].cells[1], "[PENDIENTE]")
    set_cell_text(t4.rows[2].cells[2], "[PENDIENTE]")
    set_cell_text(t4.rows[2].cells[3], "[PENDIENTE]")
    set_cell_text(t4.rows[2].cells[5], "[PENDIENTE — email vocero]")
    set_cell_text(t4.rows[3].cells[1], "Cali")
    set_cell_text(t4.rows[3].cells[2], "Cali")
    set_cell_text(t4.rows[3].cells[3], "Cali")
    set_cell_text(t4.rows[3].cells[5], "[PENDIENTE — fecha]")
    t6 = doc.tables[6]
    for row in t6.rows[1:]:
        if len(row.cells) >= 3:
            set_cell_text(row.cells[1], "")
            set_cell_text(row.cells[2], "")
    note = doc.add_paragraph()
    note.add_run(
        f"Docente: {DOCENTE} · Correo: {CORREO} · "
        f'Horario: {meta["dia"]} {meta["horario"]} ({meta["duracion_min"]} min) · '
        f'Modalidad: {meta["modalidad"]} · Código: {meta["codigo"]} · '
        "PRELLENADO 2026-2 — campos de estudiantes pendientes."
    )
    out = (
        ROOT
        / meta["folder"]
        / "Entregas docente"
        / "2026-2"
        / f'ACUERDO PEDAGOGICO - {meta["nombre"]} - 2026-2.docx'
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out))
    return out
def calendario_md(meta: dict, clases: list[dict]) -> str:
    lines = [
        f'# Calendario 2026-2 — {meta["nombre"]}',
        "",
        f'- **Código:** {meta["codigo"]}',
        f'- **Grupo:** {meta["grupo"]}',
        f"- **Periodo:** 2026-2 · **10/08/2026 – 22/11/2026**",
        f'- **Horario:** {meta["dia"]} **{meta["horario"]}** ({meta["duracion_min"]} min)',
        f'- **Modalidad:** {meta["modalidad"]}',
        f"- **Docente:** {DOCENTE} · `{CORREO}`",
        f"- **Total clases:** {len(clases)} (festivos = **clase autónoma**, no se omiten)",
        "",
        "## Cortes teóricos (30% / 30% / 40%)",
        "",
        LOGICA_EVALUACION,
        "",
        "| Corte | % | Ventana | Clases | Parcial de cierre | Desglose teórico |",
        "|---|---|---|---|---|---|",
    ]
    for key, c in CORTES.items():
        title = key.replace("_", " ").title()
        lines.append(
            f'| {title} | {c["pct"]} | {c["inicio"]} → {c["fin"]} | '
            f'{c["clases"]} | {c["parcial_cierre"]} | {c["desglose"]} |'
        )
    lines += [
        "",
        "> Cálculo teórico por tercios del periodo. Validar en Acuerdo pedagógico / socialización.",
        "",
        "## Clases",
        "",
        "| Clase | Fecha | Tipo | Nota |",
        "|---|---|---|---|",
    ]
    # Parciales en ultima clase regular de cada corte (nunca autonoma)
    ranges = [(1, 5, 1), (6, 10, 2), (11, 15, 3)]
    cierre_parcial = {}
    for a, b, pn in ranges:
        regs = [cl for cl in clases if a <= cl["n"] <= b and cl["tipo"] != "autonoma"]
        if regs:
            cierre_parcial[regs[-1]["n"]] = f"Parcial {pn} (cierre Corte {pn})"
    for cl in clases:
        tipo = {
            "autonoma": "Autónoma (festivo)",
            "presencial": "Presencial",
            "virtual": "Virtual (síncrona)",
        }.get(cl["tipo"], cl["tipo"])
        notas = []
        if cl["festivo"]:
            notas.append(cl["festivo"])
            if cl["n"] not in cierre_parcial:
                notas.append("refuerzo sin parcial")
        if cl["n"] in cierre_parcial:
            notas.append(cierre_parcial[cl["n"]])
        nota = " · ".join(notas) if notas else "—"
        y, m, d = cl["fecha"].split("-")
        lines.append(f'| {cl["n"]} | {d}/{m}/{y} | {tipo} | {nota} |')
    lines += [
        "",
        "## Festivos Colombia 2026 (rango del periodo)",
        "",
        "- 17/08/2026 — Asunción de la Virgen",
        "- 12/10/2026 — Día de la Diversidad Étnica y Cultural",
        "- 02/11/2026 — Todos los Santos",
        "- 16/11/2026 — Independencia de Cartagena",
        "",
    ]
    return "\n".join(lines)
def main() -> None:
    master = {
        "_comentario": (
            "Calendario académico docente UNIAJC 2026-2. "
            "Fuente de verdad para generación de material."
        ),
        "_actualizado": "2026-08-07",
        "periodo": "2026-2",
        "inicio": "2026-08-10",
        "fin": "2026-11-22",
        "docente": {
            "nombre": "Julian Andres Castaño",
            "nombre_completo": DOCENTE,
            "correo": CORREO,
        },
        "regla_festivos": "No omitir. Marcar como clase autónoma.",
        "festivos_en_rango": FESTIVOS,
        "logica_evaluacion": LOGICA_EVALUACION,
        "cortes_teoricos": CORTES,
        "cursos": {},
    }
    for key, meta in CURSOS.items():
        folder = ROOT / meta["folder"]
        for sub in [
            "Plan curso",
            "Entregas docente/2026-2",
            "Kit docente",
            "Clases",
            "Parciales",
            "Clases grabadas",
        ]:
            (folder / sub).mkdir(parents=True, exist_ok=True)
        clases = apply_parciales(
            class_dates(
                meta["weekday"],
                meta.get("tipo_regular", "virtual"),
                meta.get("clase1_presencial", False),
            )
        )
        cal_path = folder / "Plan curso" / "CALENDARIO_2026-2.md"
        cal_path.write_text(calendario_md(meta, clases), encoding="utf-8")
        acuerdo = fill_acuerdo(meta)
        master["cursos"][key] = {
            k: meta[k]
            for k in [
                "folder",
                "nombre",
                "codigo",
                "grupo",
                "dia",
                "horario",
                "duracion_min",
                "modalidad",
            ]
        }
        master["cursos"][key].update(
            {
                "n_clases": len(clases),
                "clases": clases,
                "acuerdo_prellenado": str(acuerdo.relative_to(ROOT)).replace("\\", "/"),
                "calendario": str(cal_path.relative_to(ROOT)).replace("\\", "/"),
            }
        )
        auton = sum(1 for c in clases if c["tipo"] == "autonoma")
        print(f"OK {meta['nombre']}: {len(clases)} clases ({auton} autónomas)")
        print(f"  - {cal_path.relative_to(ROOT)}")
        print(f"  - {acuerdo.relative_to(ROOT)}")
    json_path = Path(__file__).with_name("semestre_2026_2.json")
    json_path.write_text(json.dumps(master, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK {json_path.relative_to(ROOT)}")
if __name__ == "__main__":
    main()
