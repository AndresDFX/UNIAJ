# -*- coding: utf-8 -*-
"""Ajuste puntual: modalidad por día Prog II (presencial) / Seminario (virtual)."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

PROG_TEMAS = {
    1: "Presentación del curso · Introducción a POO",
    2: "Colecciones dinámicas ArrayList",
    3: "Pilas y colas",
    4: "Mapas y conjuntos · Interfaces gráficas GUI",
    5: "Parcial 1",
    6: "Eventos y controladores",
    7: "Patrones de diseño",
    8: "Documentación y QA",
    9: "Refactorización con IA · Persistencia de archivos",
    10: "Parcial 2",
    11: "Revisión de código cruzada",
    12: "Integración de módulos",
    13: "Control de excepciones",
    14: "Preparación presentación final · Evaluación de proyectos + cierre",
    15: "Parcial 3",
}
SEM_TEMAS = {
    1: "Presentación del curso · Conceptos iniciales",
    2: "Ciclos de vida",
    3: "Metodologías tradicionales",
    4: "Metodologías ágiles",
    5: "Parcial 1",
    6: "Requerimientos de software",
    7: "Historias de usuario",
    8: "Introducción a UML",
    9: "Casos de uso",
    10: "Parcial 2",
    11: "Avance proyecto integrador",
    12: "Diagramas UML avanzados",
    13: "Diseño de interfaces",
    14: "Evaluación final (prep. sustentación) · Sustentación de proyectos + cierre",
    15: "Parcial 3",
}
PROG_FECHAS = [
    ("2026-08-12", 1, False),
    ("2026-08-19", 2, False),
    ("2026-08-26", 3, False),
    ("2026-09-02", 4, False),
    ("2026-09-09", 5, True),
    ("2026-09-16", 6, False),
    ("2026-09-23", 7, False),
    ("2026-09-30", 8, False),
    ("2026-10-07", 9, False),
    ("2026-10-14", 10, True),
    ("2026-10-21", 11, False),
    ("2026-10-28", 12, False),
    ("2026-11-04", 13, False),
    ("2026-11-11", 14, False),
    ("2026-11-18", 15, True),
]
SEM_FECHAS = [
    ("2026-08-13", 1, False),
    ("2026-08-20", 2, False),
    ("2026-08-27", 3, False),
    ("2026-09-03", 4, False),
    ("2026-09-10", 5, True),
    ("2026-09-17", 6, False),
    ("2026-09-24", 7, False),
    ("2026-10-01", 8, False),
    ("2026-10-08", 9, False),
    ("2026-10-15", 10, True),
    ("2026-10-22", 11, False),
    ("2026-10-29", 12, False),
    ("2026-11-05", 13, False),
    ("2026-11-12", 14, False),
    ("2026-11-19", 15, True),
]
FIELDS = [
    "curso",
    "codigo_fi",
    "grupo",
    "clase_n",
    "fecha",
    "dia",
    "hora_inicio",
    "hora_fin",
    "tipo_clase",
    "es_parcial",
    "parcial_n",
    "sesion_etiqueta",
    "tema",
    "notas",
]


def parcial_n(n: int) -> str:
    return {5: "1", 10: "2", 15: "3"}.get(n, "")


def rows_prog() -> list[dict]:
    rows = []
    for fecha, n, es_p in PROG_FECHAS:
        pn = parcial_n(n) if es_p else ""
        etiq = f"Clase {n} · Parcial {pn}" if es_p else f"Clase {n}"
        notas = (
            "parcial presencial sincrono; [PENDIENTE listado]"
            if es_p
            else "[PENDIENTE listado]"
        )
        rows.append(
            {
                "curso": "Programación II",
                "codigo_fi": "FI303204",
                "grupo": "341C",
                "clase_n": n,
                "fecha": fecha,
                "dia": "Miércoles",
                "hora_inicio": "18:00",
                "hora_fin": "20:00",
                "tipo_clase": "presencial",
                "es_parcial": "si" if es_p else "no",
                "parcial_n": pn,
                "sesion_etiqueta": etiq,
                "tema": PROG_TEMAS[n],
                "notas": notas,
            }
        )
    return rows


def rows_sem() -> list[dict]:
    rows = []
    for fecha, n, es_p in SEM_FECHAS:
        pn = parcial_n(n) if es_p else ""
        etiq = f"Clase {n} · Parcial {pn}" if es_p else f"Clase {n}"
        tipo = "presencial" if es_p else "virtual"
        notas = (
            "parcial presencial sincrono; [PENDIENTE listado]"
            if es_p
            else "[PENDIENTE listado]"
        )
        rows.append(
            {
                "curso": "Seminario de Sistemas",
                "codigo_fi": "FI303301",
                "grupo": "341C",
                "clase_n": n,
                "fecha": fecha,
                "dia": "Jueves",
                "hora_inicio": "18:00",
                "hora_fin": "20:00",
                "tipo_clase": tipo,
                "es_parcial": "si" if es_p else "no",
                "parcial_n": pn,
                "sesion_etiqueta": etiq,
                "tema": SEM_TEMAS[n],
                "notas": notas,
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    print("CSV", path.relative_to(ROOT))


def fmt_fecha(iso: str) -> str:
    y, m, d = iso.split("-")
    return f"{d}/{m}/{y}"


def write_cal_md(
    path: Path,
    nombre: str,
    codigo: str,
    dia: str,
    modalidad_curso: str,
    criterio: str,
    cortes_parciales: list[str],
    clases_rows: list[dict],
    conflicto: str,
) -> None:
    lines = [
        f"# Calendario 2026-2 — {nombre}",
        "",
        f"- **Código:** {codigo}",
        "- **Grupo:** 341C",
        "- **Periodo:** 2026-2 · **10/08/2026 – 22/11/2026**",
        f"- **Horario:** {dia} **18:00 – 20:00** (120 min)",
        f"- **Modalidad:** {modalidad_curso}",
        "- **Docente:** Julian Andres Castaño Espinosa · `julianacastano@profesores.uniajc.edu.co`",
        "- **Total clases:** 15 (festivos = **clase autónoma**, no se omiten)",
        "",
        "## Cortes teóricos (30% / 30% / 40%)",
        "",
        criterio,
        "",
        conflicto,
        "",
        "| Corte | % | Ventana | Clases | Parcial de cierre | Desglose teórico |",
        "|---|---|---|---|---|---|",
    ]
    lines.extend(cortes_parciales)
    lines += [
        "",
        "> **Día de parcial = solo evaluación** (sin tema de trabajo dirigido nuevo). Detalle temático en PLAN_DE_CURSO_*.md.",
        "",
        "> Validar en Acuerdo pedagógico / socialización. Ventanas de corte = bloques temáticos; la fecha del parcial = última clase regular del corte.",
        "",
        "## Clases",
        "",
        "| Clase | Fecha | Tipo | Nota |",
        "|---|---|---|---|",
    ]
    for r in clases_rows:
        n = int(r["clase_n"])
        if r["es_parcial"] == "si":
            tipo = "Presencial (síncrono)"
            nota = f"Parcial {r['parcial_n']} (cierre Corte {r['parcial_n']})"
        else:
            tipo = {
                "presencial": "Presencial",
                "virtual": "Virtual (síncrona)",
                "autonoma": "Autónoma (festivo)",
            }[r["tipo_clase"]]
            nota = "—"
        lines.append(f"| {n} | {fmt_fecha(r['fecha'])} | {tipo} | {nota} |")
    lines += [
        "",
        "## Festivos Colombia 2026 (rango del periodo)",
        "",
        "- 17/08/2026 — Asunción de la Virgen",
        "- 12/10/2026 — Día de la Diversidad Étnica y Cultural",
        "- 02/11/2026 — Todos los Santos",
        "- 16/11/2026 — Independencia de Cartagena",
        "",
        "> En este curso (miércoles/jueves) no cae festivo en día de clase; la regla autónoma aplica si el calendario institucional mueve algún encuentro.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    print("MD", path.relative_to(ROOT))


def patch_json() -> None:
    jpath = ROOT / ".config" / "calendario" / "semestre_2026_2.json"
    data = json.loads(jpath.read_text(encoding="utf-8"))
    regla_nueva = (
        "Criterio de modalidad por sesión (fijo 2026-2): modalidad del curso = Presencialidad asistida. "
        "Prog II (miércoles): clases regulares presencial; Seminario (jueves): clases regulares virtual síncrona. "
        "Parciales = siempre presencial síncrono; festivos = clase autónoma (sin parcial). "
        "Los parciales NUNCA se programan en día festivo ni en clase autónoma. "
        "Si el cierre teórico del corte cae en festivo/autónoma, el parcial se mueve a la última clase regular anterior del mismo corte."
    )
    data["logica_evaluacion"] = regla_nueva
    data["regla_parciales"] = regla_nueva
    data["regla_modalidad_sesion"] = (
        "Por día (Prog II / Seminario): miércoles presencial; jueves virtual síncrona; "
        "parciales presencial síncrono; festivos autónoma. "
        "(BD II / Arquitectura: ver tipo por sesión en su curso; no reescritos en este ajuste.)"
    )
    data["modalidad_cursos"] = (
        "Presencialidad asistida (ver tipo por sesión / día de la semana)"
    )
    p = data["cursos"]["programacion_ii"]
    p["horario"] = "18:00 – 20:00"
    p["modalidad"] = "Presencialidad asistida"
    for cl in p["clases"]:
        cl["tipo"] = "presencial"
    s = data["cursos"]["seminario"]
    s["horario"] = "18:00 – 20:00"
    s["modalidad"] = "Presencialidad asistida"
    for cl in s["clases"]:
        cl["tipo"] = "presencial" if cl.get("parcial") else "virtual"
    jpath.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("JSON", jpath.relative_to(ROOT))


def patch_emails() -> None:
    prog = (
        ROOT
        / "Programacion II"
        / "Entregas docente"
        / "2026-2"
        / "CORREO_BIENVENIDA - Programacion II - 2026-2.md"
    )
    sem = (
        ROOT
        / "Seminario de Sistemas"
        / "Entregas docente"
        / "2026-2"
        / "CORREO_BIENVENIDA - Seminario de Sistemas - 2026-2.md"
    )
    # Re-read/rewrite with UTF-8 to avoid BOM/encoding issues
    prog_text = """# Correo de bienvenida — Programación II · 2026-2

**Para:** estudiantes del grupo  
**De:** Julian Andres Castaño Espinosa · julianacastano@profesores.uniajc.edu.co  
**Asunto sugerido:** Bienvenida · Programación II (FI303204 · 341C) · 2026-2 · Presencialidad asistida · mié 18:00–20:00

---

Estimados estudiantes:

Les doy la bienvenida al curso **Programación II** (código **FI303204**, grupo **341C**) del periodo **2026-2** (ventana académica: **10/08/2026 – 22/11/2026**).

- **Modalidad:** Presencialidad asistida (clases presencial / virtual síncrona / autónoma)
- **Encuentros de miércoles:** **presenciales** (salvo festivo → clase autónoma; los **parciales** son presencial síncrono)
- **Horario:** miércoles **18:00 – 20:00** (inicio práctico de clase: **18:10**)
- **Docente:** Julian Andres Castaño Espinosa · `julianacastano@profesores.uniajc.edu.co`
- **Campus Virtual UNIAJC:** [URL Campus Virtual UNIAJC — pendiente]

**Contenido de las clases** (Presentación del Curso, diapositivas y talleres — carpeta compartida):  
[PEGAR AQUÍ LINK DE LA CARPETA CLASES]

Por favor **revisen en su calendario institucional / Campus Virtual** los eventos del curso (fechas de clase, parciales y demás hitos del cronograma). Es importante que los tengan visibles para organizar el semestre.

En la **primera clase** trabajaremos: Presentación del curso + diagnóstico de conocimientos previos + arranque temático.

Nos vemos pronto. ¡Bienvenidos!

Cordialmente,  
Julian Andres Castaño Espinosa  
Ingeniero de Sistemas · Candidato a MsC en IA  
`julianacastano@profesores.uniajc.edu.co`
"""
    sem_text = """# Correo de bienvenida — Seminario de Sistemas · 2026-2

**Para:** estudiantes del grupo  
**De:** Julian Andres Castaño Espinosa · julianacastano@profesores.uniajc.edu.co  
**Asunto sugerido:** Bienvenida · Seminario de Sistemas (FI303301 · 341C) · 2026-2 · Presencialidad asistida · jue 18:00–20:00

---

Estimados estudiantes:

Les doy la bienvenida al curso **Seminario de Sistemas** (código **FI303301**, grupo **341C**) del periodo **2026-2** (ventana académica: **10/08/2026 – 22/11/2026**).

- **Modalidad:** Presencialidad asistida (clases presencial / virtual síncrona / autónoma)
- **Encuentros de jueves:** **virtuales síncronos** (salvo festivo → clase autónoma; los **parciales** son **presencial** síncrono)
- **Horario:** jueves **18:00 – 20:00** (inicio práctico de clase: **18:10**)
- **Docente:** Julian Andres Castaño Espinosa · `julianacastano@profesores.uniajc.edu.co`
- **Campus Virtual UNIAJC:** [URL Campus Virtual UNIAJC — pendiente]

**Contenido de las clases** (Presentación del Curso, diapositivas y talleres — carpeta compartida):  
[PEGAR AQUÍ LINK DE LA CARPETA CLASES]

Por favor **revisen en su calendario institucional / Campus Virtual** los eventos del curso (fechas de clase, parciales y demás hitos del cronograma). Es importante que los tengan visibles para organizar el semestre.

En la **primera clase** trabajaremos: Presentación del curso + diagnóstico de conocimientos previos + arranque temático.

Nos vemos pronto. ¡Bienvenidos!

Cordialmente,  
Julian Andres Castaño Espinosa  
Ingeniero de Sistemas · Candidato a MsC en IA  
`julianacastano@profesores.uniajc.edu.co`
"""
    prog.write_text(prog_text, encoding="utf-8")
    sem.write_text(sem_text, encoding="utf-8")
    print("EMAIL", prog.relative_to(ROOT))
    print("EMAIL", sem.relative_to(ROOT))


def patch_builds() -> None:
    prog_build = ROOT / ".config" / "slides" / "build_uniajc_prog2_curso.py"
    text = prog_build.read_text(encoding="utf-8")
    old = "Clase 1 presencial · resto virtual · parciales presencial · festivos autónomos"
    new = "miércoles presencial · parciales presencial · festivos autónomos"
    if old not in text:
        raise SystemExit("No encontré texto modalidad antiguo en prog2 build")
    text = text.replace(old, new)
    text = text.replace(
        "Clase 1 presencial / resto virtual / parciales presencial",
        "miércoles presencial / parciales presencial",
    )
    prog_build.write_text(text, encoding="utf-8")
    print("BUILD", prog_build.relative_to(ROOT))

    sem_build = ROOT / ".config" / "slides" / "build_uniajc_seminario_curso.py"
    # Puede estar en UTF-16 por corrupción previa
    raw = sem_build.read_bytes()
    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        sem_text = raw.decode("utf-16")
    else:
        try:
            sem_text = raw.decode("utf-8")
        except UnicodeDecodeError:
            sem_text = raw.decode("utf-16")
    sem_text = sem_text.replace(
        "Horario: **Jueves 20:00 – 22:00** (120 min)",
        "Horario: **Jueves 18:00 – 20:00** (120 min)",
    )
    sem_text = sem_text.replace(
        "Modalidad: **Virtual** (clases y parciales síncronos · festivos autónomos)",
        "Modalidad: **Presencialidad asistida** (jueves virtual síncrona · parciales presencial · festivos autónomos)",
    )
    sem_text = sem_text.replace(
        "Modalidad: **Virtual** (clases y parciales síncronos · festivos autónomos).",
        "Modalidad: **Presencialidad asistida** (jueves virtual síncrona · parciales presencial · festivos autónomos).",
    )
    sem_text = sem_text.replace(
        "('info', 'Jueves 20:00-22:00 (120 min). Modalidad: Virtual (clases y parciales síncronos). Grupo: 341C.'),",
        "('info', 'Jueves 18:00-20:00 (120 min). Modalidad: Presencialidad asistida (jueves virtual / parciales presencial). Grupo: 341C.'),",
    )
    sem_text = sem_text.replace(
        "Jueves **20:00 – 22:00**",
        "Jueves **18:00 – 20:00**",
    )
    sem_text = sem_text.replace(
        'inicio_clase="20:10"',
        'inicio_clase="18:10"',
    )
    sem_text = sem_text.replace(
        "note=\"Parciales síncronos (virtual): P1 10/09 · P2 15/10 · P3 19/11 (Clases 5/10/15). Nunca en autónoma.\"",
        "note=\"Parciales presencial síncrono: P1 10/09 · P2 15/10 · P3 19/11 (Clases 5/10/15). Nunca en autónoma.\"",
    )
    # Guardar siempre UTF-8
    sem_build.write_text(sem_text, encoding="utf-8")
    print("BUILD", sem_build.relative_to(ROOT))


def patch_generator() -> None:
    gen = ROOT / ".config" / "calendario" / "generar_semestre_2026_2.py"
    text = gen.read_text(encoding="utf-8")
    text = text.replace(
        'LOGICA_EVALUACION = (\n'
        '    "Criterio de modalidad por sesion (fijo 2026-2): modalidad del curso = Virtual. Clases regulares = virtual (sincrona); parciales = siempre sincronos (virtual); festivos = clase autonoma (sin parcial). Los parciales NUNCA se programan en dia festivo ni en clase autonoma. Si el cierre teorico del corte cae en festivo/autonoma, el parcial se mueve a la ultima clase regular anterior del mismo corte."\n'
        ")",
        'LOGICA_EVALUACION = (\n'
        '    "Criterio de modalidad por sesion (fijo 2026-2): modalidad del curso = Presencialidad asistida. '
        "Prog II (miercoles): clases regulares presencial; Seminario (jueves): clases regulares virtual sincrona. "
        "Parciales = siempre presencial sincrono; festivos = clase autonoma (sin parcial). "
        "Los parciales NUNCA se programan en dia festivo ni en clase autonoma. "
        'Si el cierre teorico del corte cae en festivo/autonoma, el parcial se mueve a la ultima clase regular anterior del mismo corte."\n'
        ")",
    )
    # Prog II meta
    text = text.replace(
        '        "weekday": 2,\n'
        '        "horario": "20:00 – 22:00",\n'
        "        \"duracion_min\": 120,\n"
        '        "modalidad": "Virtual (clases y parciales sincronos / festivos autonomos)",\n'
        '        "objetivos": (\n'
        '            "Comprender y aplicar los pilares',
        '        "weekday": 2,\n'
        '        "horario": "18:00 – 20:00",\n'
        "        \"duracion_min\": 120,\n"
        '        "modalidad": "Presencialidad asistida (miercoles presencial / parciales presencial / festivos autonomos)",\n'
        '        "tipo_regular": "presencial",\n'
        '        "objetivos": (\n'
        '            "Comprender y aplicar los pilares',
    )
    text = text.replace(
        "Periodo 2026-2 · Grupo 341C · Miércoles 20:00–22:00 (120 min).\n"
        '            "Modalidad: Virtual (confirmar semanas virtuales en Campus Virtual).\n',
        "Periodo 2026-2 · Grupo 341C · Miércoles 18:00–20:00 (120 min).\n"
        '            "Modalidad: Presencialidad asistida (encuentros de miercoles presenciales; parciales presencial).\n',
    )
    # Seminario meta
    text = text.replace(
        '        "weekday": 3,\n'
        '        "horario": "20:00 – 22:00",\n'
        "        \"duracion_min\": 120,\n"
        '        "modalidad": "Virtual (clases y parciales sincronos / festivos autonomos)",\n'
        '        "objetivos": (\n'
        '            "Levantar, analizar y documentar',
        '        "weekday": 3,\n'
        '        "horario": "18:00 – 20:00",\n'
        "        \"duracion_min\": 120,\n"
        '        "modalidad": "Presencialidad asistida (jueves virtual sincrona / parciales presencial / festivos autonomos)",\n'
        '        "tipo_regular": "virtual",\n'
        '        "objetivos": (\n'
        '            "Levantar, analizar y documentar',
    )
    text = text.replace(
        "Periodo 2026-2 · Grupo 341C · Jueves 20:00–22:00 (120 min).\n"
        '            "Modalidad: Virtual (confirmar semanas virtuales en Campus Virtual).\n',
        "Periodo 2026-2 · Grupo 341C · Jueves 18:00–20:00 (120 min).\n"
        '            "Modalidad: Presencialidad asistida (encuentros de jueves virtuales sincronos; parciales presencial).\n',
    )
    # class_dates / apply_parciales — usar tipo_regular del curso
    old_class_dates = '''def class_dates(weekday: int) -> list[dict]:
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
                tipo = "virtual"
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
        target["tipo"] = "virtual"
    return clases'''
    new_class_dates = '''def class_dates(weekday: int, tipo_regular: str = "virtual") -> list[dict]:
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
    return clases'''
    if old_class_dates not in text:
        raise SystemExit("No encontré class_dates/apply_parciales para parchear")
    text = text.replace(old_class_dates, new_class_dates)
    text = text.replace(
        '        clases = apply_parciales(class_dates(meta["weekday"]))',
        '        clases = apply_parciales(class_dates(meta["weekday"], meta.get("tipo_regular", "virtual")))',
    )
    # Fix label map bug + add presencial
    text = text.replace(
        '''        tipo = {
            "autonoma": "Autónoma (festivo)",
            "virtual": "Presencial",
            "virtual": "Virtual (síncrona)",
        }.get(cl["tipo"], cl["tipo"])''',
        '''        tipo = {
            "autonoma": "Autónoma (festivo)",
            "presencial": "Presencial",
            "virtual": "Virtual (síncrona)",
        }.get(cl["tipo"], cl["tipo"])''',
    )
    gen.write_text(text, encoding="utf-8")
    print("GEN", gen.relative_to(ROOT))


def main() -> None:
    rp, rs = rows_prog(), rows_sem()
    write_csv(
        ROOT / "Programacion II" / "Plan curso" / "2026-1" / "calendario_eventos_2026-1.csv",
        rp,
    )
    write_csv(
        ROOT
        / "Seminario de Sistemas"
        / "Plan curso"
        / "2026-1"
        / "calendario_eventos_2026-1.csv",
        rs,
    )
    write_csv(ROOT / ".config" / "calendario" / "eventos_programacion_ii_2026-1.csv", rp)
    write_csv(ROOT / ".config" / "calendario" / "eventos_seminario_2026-1.csv", rs)

    todos_path = ROOT / ".config" / "calendario" / "eventos_todos_cursos_2026-2.csv"
    with todos_path.open(encoding="utf-8-sig", newline="") as f:
        all_rows = list(csv.DictReader(f))
    kept = [
        r
        for r in all_rows
        if r["curso"] not in ("Programación II", "Seminario de Sistemas")
    ]
    write_csv(todos_path, rp + rs + kept)

    criterio_prog = (
        "Criterio de modalidad por sesión (fijo 2026-2 · pedido docente): modalidad del curso = **Presencialidad asistida**. "
        "Clases regulares de **miércoles = presencial**; parciales = siempre **presencial síncrono**; festivos = clase autónoma (sin parcial). "
        "Los parciales NUNCA se programan en día festivo ni en clase autónoma."
    )
    criterio_sem = (
        "Criterio de modalidad por sesión (fijo 2026-2 · pedido docente): modalidad del curso = **Presencialidad asistida**. "
        "Clases regulares de **jueves = virtual síncrona** (incluye Clase 1); parciales = siempre **presencial síncrono** (aunque el día habitual sea virtual); festivos = clase autónoma (sin parcial). "
        "Los parciales NUNCA se programan en día festivo ni en clase autónoma."
    )
    conflicto_prog = (
        "> **Ajuste 2026-2:** se sustituye la regla anterior «Clase 1 presencial · resto virtual». "
        "Ahora todas las clases regulares de miércoles son **presenciales** (Prog II primero en la semana = presencial)."
    )
    conflicto_sem = (
        "> **Conflicto resuelto (prioridad pedido docente):** builds previos podían sugerir «Clase 1 presencial» genérico; "
        "el docente indicó que **la del jueves es virtual**. Se aplica: Seminario Clase 1 = **virtual síncrona**; parciales = **presencial**."
    )
    cortes_prog = [
        "| Corte 1 | 30% | 2026-08-10 → 2026-09-13 | 1-5 | Parcial 1 · Clase 5 (09/09/2026) · Presencial (síncrono) | 10% Parcial 1 · 10% Talleres y Quiz · 10% Asistencia |",
        "| Corte 2 | 30% | 2026-09-14 → 2026-10-18 | 6-10 | Parcial 2 · Clase 10 (14/10/2026) · Presencial (síncrono) | 10% Parcial 2 · 10% Talleres y Quiz · 10% Asistencia |",
        "| Corte 3 | 40% | 2026-10-19 → 2026-11-22 | 11-15 | Parcial 3 · Clase 15 (18/11/2026) · Presencial (síncrono) | 15% Parcial 3 · 20% Proyecto Integrador · 5% Asistencia |",
    ]
    cortes_sem = [
        "| Corte 1 | 30% | 2026-08-10 → 2026-09-13 | 1-5 | Parcial 1 · Clase 5 (10/09/2026) · Presencial (síncrono) | 10% Parcial 1 · 10% Talleres y Quiz · 10% Asistencia |",
        "| Corte 2 | 30% | 2026-09-14 → 2026-10-18 | 6-10 | Parcial 2 · Clase 10 (15/10/2026) · Presencial (síncrono) | 10% Parcial 2 · 10% Talleres y Quiz · 10% Asistencia |",
        "| Corte 3 | 40% | 2026-10-19 → 2026-11-22 | 11-15 | Parcial 3 · Clase 15 (19/11/2026) · Presencial (síncrono) | 15% Parcial 3 · 20% Proyecto Integrador · 5% Asistencia |",
    ]
    write_cal_md(
        ROOT / "Programacion II" / "Plan curso" / "2026-1" / "CALENDARIO_2026-1.md",
        "Programación II",
        "FI303204",
        "Miércoles",
        "Presencialidad asistida (encuentros de miércoles **presenciales** · parciales presencial · festivos autónomos)",
        criterio_prog,
        cortes_prog,
        rp,
        conflicto_prog,
    )
    write_cal_md(
        ROOT
        / "Seminario de Sistemas"
        / "Plan curso"
        / "2026-1"
        / "CALENDARIO_2026-1.md",
        "Seminario de Sistemas",
        "FI303301",
        "Jueves",
        "Presencialidad asistida (encuentros de jueves **virtuales síncronos** · parciales presencial · festivos autónomos)",
        criterio_sem,
        cortes_sem,
        rs,
        conflicto_sem,
    )

    patch_json()
    patch_emails()
    patch_builds()
    patch_generator()

    readme = ROOT / ".config" / "calendario" / "README_eventos_csv.md"
    txt = readme.read_text(encoding="utf-8")
    txt2 = re.sub(
        r"Modalidad por sesión:.*",
        "Modalidad por sesión (Prog II / Seminario 2026-2): miércoles = presencial; jueves = virtual síncrona; parciales = presencial síncrono; festivos = autónoma. Curso = Presencialidad asistida.",
        txt,
    )
    readme.write_text(txt2, encoding="utf-8")
    print("README", readme.relative_to(ROOT))
    print("DONE")


if __name__ == "__main__":
    main()
