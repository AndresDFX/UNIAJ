# -*- coding: utf-8 -*-
"""Ajuste one-shot: día de parcial = solo evaluación (sin tema técnico)."""
from __future__ import annotations

import csv
import io
import re
from pathlib import Path

ROOT = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos")

RULE_NOTE = (
    "\n> **Día de parcial = solo evaluación:** sin tema de trabajo dirigido nuevo. "
    "Si un tema técnico estaba mezclado con el parcial, se reasigna a la última clase "
    "regular anterior del mismo corte.\n"
)

# plan_path -> list of (old, new)
PLANS: dict[Path, list[tuple[str, str]]] = {
    ROOT / "Programacion II/Plan curso/2026-1/PLAN_DE_CURSO_2026-1.md": [
        (
            "| 4 | 02/09/2026 | Virtual (síncrona) | Mapas y conjuntos |",
            "| 4 | 02/09/2026 | Virtual (síncrona) | Mapas y conjuntos · Interfaces gráficas GUI |",
        ),
        (
            "| 5 | 09/09/2026 | Presencial | Interfaces gráficas GUI · **Parcial 1** |",
            "| 5 | 09/09/2026 | Presencial | **Parcial 1** |",
        ),
        (
            "| 9 | 07/10/2026 | Virtual (síncrona) | Refactorización con IA |",
            "| 9 | 07/10/2026 | Virtual (síncrona) | Refactorización con IA · Persistencia de archivos |",
        ),
        (
            "| 10 | 14/10/2026 | Presencial | Persistencia de archivos · **Parcial 2** |",
            "| 10 | 14/10/2026 | Presencial | **Parcial 2** |",
        ),
        (
            "| 14 | 11/11/2026 | Virtual (síncrona) | Preparación presentación final |",
            "| 14 | 11/11/2026 | Virtual (síncrona) | Preparación presentación final · Evaluación de proyectos + cierre |",
        ),
        (
            "| 15 | 18/11/2026 | Presencial | Evaluación de proyectos + cierre · **Parcial 3** |",
            "| 15 | 18/11/2026 | Presencial | **Parcial 3** |",
        ),
    ],
    ROOT / "Seminario de Sistemas/Plan curso/2026-1/PLAN_DE_CURSO_2026-1.md": [
        (
            "| 5 | 10/09/2026 | Presencial | Caso estudio evaluativo · **Parcial 1** |",
            "| 5 | 10/09/2026 | Presencial | **Parcial 1** |",
        ),
        (
            "| 10 | 15/10/2026 | Presencial | Caso estudio evaluativo · **Parcial 2** |",
            "| 10 | 15/10/2026 | Presencial | **Parcial 2** |",
        ),
        (
            "| 14 | 12/11/2026 | Virtual (síncrona) | Evaluación final (prep. sustentación) |",
            "| 14 | 12/11/2026 | Virtual (síncrona) | Evaluación final (prep. sustentación) · Sustentación de proyectos + cierre |",
        ),
        (
            "| 15 | 19/11/2026 | Presencial | Sustentación de proyectos + cierre · **Parcial 3** |",
            "| 15 | 19/11/2026 | Presencial | **Parcial 3** |",
        ),
    ],
    ROOT / "Bases de Datos II/Plan curso/2026-2/PLAN_DE_CURSO_2026-2.md": [
        (
            "| 4 | 31/08/2026 | Virtual (síncrona) | Funciones y disparadores |",
            "| 4 | 31/08/2026 | Virtual (síncrona) | Funciones y disparadores · Seguridad y respaldo |",
        ),
        (
            "| 5 | 07/09/2026 | Presencial | Seguridad y respaldo · **Parcial 1 (cierre Corte 1)** |",
            "| 5 | 07/09/2026 | Presencial | **Parcial 1** |",
        ),
        (
            "| 8 | 28/09/2026 | Virtual (síncrona) | Tuning de bases de datos |",
            "| 8 | 28/09/2026 | Virtual (síncrona) | Tuning de bases de datos · Gestión de transacciones |",
        ),
        (
            "| 9 | 05/10/2026 | Presencial | Gestión de transacciones · **Parcial 2 (cierre Corte 2)** |",
            "| 9 | 05/10/2026 | Presencial | **Parcial 2** |",
        ),
        (
            "| 12 | 26/10/2026 | Virtual (síncrona) | Integración de aplicaciones externas |",
            "| 12 | 26/10/2026 | Virtual (síncrona) | Integración de aplicaciones externas · Preparación de presentación final |",
        ),
        (
            "| 14 | 09/11/2026 | Presencial | Preparación de presentación final · **Parcial 3 (cierre Corte 3)** |",
            "| 14 | 09/11/2026 | Presencial | **Parcial 3** |",
        ),
    ],
    ROOT / "Arquitectura de Sistemas Computacionales/Plan curso/2026-2/PLAN_DE_CURSO_2026-2.md": [
        (
            "| 4 | 31/08/2026 | Virtual (síncrona) | Microservicios |",
            "| 4 | 31/08/2026 | Virtual (síncrona) | Microservicios · Arquitecturas distribuidas |",
        ),
        (
            "| 5 | 07/09/2026 | Presencial | Arquitecturas distribuidas · **Parcial 1 (cierre Corte 1)** |",
            "| 5 | 07/09/2026 | Presencial | **Parcial 1** |",
        ),
        (
            "| 8 | 28/09/2026 | Virtual (síncrona) | Monitoreo y optimización |",
            "| 8 | 28/09/2026 | Virtual (síncrona) | Monitoreo y optimización · Integración continua y despliegue (CI/CD) |",
        ),
        (
            "| 9 | 05/10/2026 | Presencial | Integración continua y despliegue (CI/CD) · **Parcial 2 (cierre Corte 2)** |",
            "| 9 | 05/10/2026 | Presencial | **Parcial 2** |",
        ),
        (
            "| 12 | 26/10/2026 | Virtual (síncrona) | Pruebas de rendimiento |",
            "| 12 | 26/10/2026 | Virtual (síncrona) | Pruebas de rendimiento · Preparación de presentación final |",
        ),
        (
            "| 14 | 09/11/2026 | Presencial | Preparación de presentación final · **Parcial 3 (cierre Corte 3)** |",
            "| 14 | 09/11/2026 | Presencial | **Parcial 3** |",
        ),
    ],
}


def patch_text(path: Path, replacements: list[tuple[str, str]], label: str) -> None:
    text = path.read_text(encoding="utf-8")
    for old, new in replacements:
        if old not in text:
            raise SystemExit(f"NO MATCH [{label}] in {path}:\n{old}")
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")
    print("OK", label, path.relative_to(ROOT))


def insert_rule_note(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if "Día de parcial = solo evaluación" in text:
        return
    m = re.search(r"(Parciales de este curso:[^\n]*\n)", text)
    if not m:
        m = re.search(r"(los parciales quedan en Clases[^\n]*\n)", text)
    if not m:
        raise SystemExit(f"No anchor for rule note in {path}")
    pos = m.end()
    path.write_text(text[:pos] + RULE_NOTE + text[pos:], encoding="utf-8")
    print("OK note", path.relative_to(ROOT))


# CSV updates: (clase_n, tema, sesion_etiqueta optional keep)
CSV_UPDATES = {
    # path: {clase_n: tema}
    ROOT / "Programacion II/Plan curso/2026-1/calendario_eventos_2026-1.csv": {
        4: "Mapas y conjuntos · Interfaces gráficas GUI",
        5: "Parcial 1",
        9: "Refactorización con IA · Persistencia de archivos",
        10: "Parcial 2",
        14: "Preparación presentación final · Evaluación de proyectos + cierre",
        15: "Parcial 3",
    },
    ROOT / "Seminario de Sistemas/Plan curso/2026-1/calendario_eventos_2026-1.csv": {
        5: "Parcial 1",
        10: "Parcial 2",
        14: "Evaluación final (prep. sustentación) · Sustentación de proyectos + cierre",
        15: "Parcial 3",
    },
    ROOT / "Bases de Datos II/Plan curso/2026-2/calendario_eventos_2026-2.csv": {
        4: "Funciones y disparadores · Seguridad y respaldo",
        5: "Parcial 1",
        8: "Tuning de bases de datos · Gestión de transacciones",
        9: "Parcial 2",
        12: "Integración de aplicaciones externas · Preparación de presentación final",
        14: "Parcial 3",
    },
    ROOT / "Arquitectura de Sistemas Computacionales/Plan curso/2026-2/calendario_eventos_2026-2.csv": {
        4: "Microservicios · Arquitecturas distribuidas",
        5: "Parcial 1",
        8: "Monitoreo y optimización · Integración continua y despliegue (CI/CD)",
        9: "Parcial 2",
        12: "Pruebas de rendimiento · Preparación de presentación final",
        14: "Parcial 3",
    },
}

CONFIG_CSV_MAP = {
    ROOT / ".config/calendario/eventos_programacion_ii_2026-1.csv": ROOT
    / "Programacion II/Plan curso/2026-1/calendario_eventos_2026-1.csv",
    ROOT / ".config/calendario/eventos_seminario_2026-1.csv": ROOT
    / "Seminario de Sistemas/Plan curso/2026-1/calendario_eventos_2026-1.csv",
    ROOT / ".config/calendario/eventos_bases_datos_ii_2026-2.csv": ROOT
    / "Bases de Datos II/Plan curso/2026-2/calendario_eventos_2026-2.csv",
    ROOT / ".config/calendario/eventos_arquitectura_2026-2.csv": ROOT
    / "Arquitectura de Sistemas Computacionales/Plan curso/2026-2/calendario_eventos_2026-2.csv",
}


def update_csv(path: Path, tema_by_n: dict[int, str]) -> None:
    raw = path.read_bytes()
    # strip UTF-8 BOM if present
    text = raw.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    fieldnames = reader.fieldnames
    if not fieldnames:
        raise SystemExit(f"No headers in {path}")
    rows = list(reader)
    for row in rows:
        n = int(row["clase_n"])
        if n in tema_by_n:
            row["tema"] = tema_by_n[n]
            if row.get("es_parcial", "").lower() in {"si", "sí", "true", "1"}:
                pn = row.get("parcial_n") or ""
                row["sesion_etiqueta"] = f"Clase {n} · Parcial {pn}".strip()
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    # write UTF-8 BOM for Excel
    path.write_bytes(("\ufeff" + buf.getvalue()).encode("utf-8"))
    print("OK csv", path.relative_to(ROOT))


def rebuild_todos() -> None:
    paths = [
        ROOT / ".config/calendario/eventos_programacion_ii_2026-1.csv",
        ROOT / ".config/calendario/eventos_seminario_2026-1.csv",
        ROOT / ".config/calendario/eventos_bases_datos_ii_2026-2.csv",
        ROOT / ".config/calendario/eventos_arquitectura_2026-2.csv",
    ]
    out = ROOT / ".config/calendario/eventos_todos_cursos_2026-2.csv"
    all_rows = []
    fieldnames = None
    for p in paths:
        text = p.read_text(encoding="utf-8-sig")
        reader = csv.DictReader(io.StringIO(text))
        fieldnames = reader.fieldnames
        all_rows.extend(list(reader))
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(all_rows)
    out.write_bytes(("\ufeff" + buf.getvalue()).encode("utf-8"))
    print("OK csv", out.relative_to(ROOT))


BUILD_PATCHES = {
    ROOT / ".config/slides/build_uniajc_prog2_curso.py": [
        (
            '{"n": 4, "tema": "Mapas y conjuntos", "fecha": "02/09"},',
            '{"n": 4, "tema": "Mapas y conjuntos · Interfaces gráficas GUI", "fecha": "02/09"},',
        ),
        (
            '{"n": 5, "tema": "Interfaces gráficas GUI", "fecha": "09/09", "tag": "Parcial 1"},',
            '{"n": 5, "tema": "Parcial 1", "fecha": "09/09"},',
        ),
        (
            '{"n": 9, "tema": "Refactorización con IA", "fecha": "07/10"},',
            '{"n": 9, "tema": "Refactorización con IA · Persistencia de archivos", "fecha": "07/10"},',
        ),
        (
            '{"n": 10, "tema": "Persistencia de archivos", "fecha": "14/10", "tag": "Parcial 2"},',
            '{"n": 10, "tema": "Parcial 2", "fecha": "14/10"},',
        ),
        (
            '{"n": 14, "tema": "Preparación presentación final", "fecha": "11/11"},',
            '{"n": 14, "tema": "Preparación presentación final · Evaluación de proyectos + cierre", "fecha": "11/11"},',
        ),
        (
            '{"n": 15, "tema": "Evaluación de proyectos + cierre", "fecha": "18/11", "tag": "Parcial 3"},',
            '{"n": 15, "tema": "Parcial 3", "fecha": "18/11"},',
        ),
    ],
    ROOT / ".config/slides/build_uniajc_seminario_curso.py": [
        (
            '{"n": 5, "tema": "Caso estudio evaluativo", "fecha": "10/09", "tag": "Parcial 1"},',
            '{"n": 5, "tema": "Parcial 1", "fecha": "10/09"},',
        ),
        (
            '{"n": 10, "tema": "Caso estudio evaluativo", "fecha": "15/10", "tag": "Parcial 2"},',
            '{"n": 10, "tema": "Parcial 2", "fecha": "15/10"},',
        ),
        (
            '{"n": 14, "tema": "Evaluación final (prep. sustentación)", "fecha": "12/11"},',
            '{"n": 14, "tema": "Evaluación final (prep. sustentación) · Sustentación de proyectos + cierre", "fecha": "12/11"},',
        ),
        (
            '{"n": 15, "tema": "Sustentación de proyectos + cierre", "fecha": "19/11", "tag": "Parcial 3"},',
            '{"n": 15, "tema": "Parcial 3", "fecha": "19/11"},',
        ),
    ],
    ROOT / ".config/slides/build_uniajc_bd2_curso.py": [
        (
            '{"n": 4, "tema": "Funciones y disparadores", "fecha": "31/08"},',
            '{"n": 4, "tema": "Funciones y disparadores · Seguridad y respaldo", "fecha": "31/08"},',
        ),
        (
            '{"n": 5, "tema": "Seguridad y respaldo", "fecha": "07/09", "tag": "Parcial 1"},',
            '{"n": 5, "tema": "Parcial 1", "fecha": "07/09"},',
        ),
        (
            '{"n": 8, "tema": "Tuning de bases de datos", "fecha": "28/09"},',
            '{"n": 8, "tema": "Tuning de bases de datos · Gestión de transacciones", "fecha": "28/09"},',
        ),
        (
            '{"n": 9, "tema": "Gestión de transacciones", "fecha": "05/10", "tag": "Parcial 2"},',
            '{"n": 9, "tema": "Parcial 2", "fecha": "05/10"},',
        ),
        (
            '{"n": 12, "tema": "Integración de aplicaciones externas", "fecha": "26/10"},',
            '{"n": 12, "tema": "Integración de aplicaciones externas · Preparación de presentación final", "fecha": "26/10"},',
        ),
        (
            '{"n": 14, "tema": "Preparación de presentación final", "fecha": "09/11", "tag": "Parcial 3"},',
            '{"n": 14, "tema": "Parcial 3", "fecha": "09/11"},',
        ),
        (
            "Hitos: avance **Clase 11** (19/10) · prep. **Clase 14** (09/11) · cierre **Clase 15** (16/11, autónoma).",
            "Hitos: avance **Clase 11** (19/10) · prep. **Clase 12** (26/10) · Parcial 3 **Clase 14** (09/11) · cierre **Clase 15** (16/11, autónoma).",
        ),
    ],
    ROOT / ".config/slides/build_uniajc_arq_curso.py": [
        (
            '{"n": 4, "tema": "Microservicios", "fecha": "31/08"},',
            '{"n": 4, "tema": "Microservicios · Arquitecturas distribuidas", "fecha": "31/08"},',
        ),
        (
            '{"n": 5, "tema": "Arquitecturas distribuidas", "fecha": "07/09", "tag": "Parcial 1"},',
            '{"n": 5, "tema": "Parcial 1", "fecha": "07/09"},',
        ),
        (
            '{"n": 8, "tema": "Monitoreo y optimización", "fecha": "28/09"},',
            '{"n": 8, "tema": "Monitoreo y optimización · CI/CD", "fecha": "28/09"},',
        ),
        (
            '{"n": 9, "tema": "CI/CD", "fecha": "05/10", "tag": "Parcial 2"},',
            '{"n": 9, "tema": "Parcial 2", "fecha": "05/10"},',
        ),
        (
            '{"n": 12, "tema": "Pruebas de rendimiento", "fecha": "26/10"},',
            '{"n": 12, "tema": "Pruebas de rendimiento · Preparación de presentación final", "fecha": "26/10"},',
        ),
        (
            '{"n": 14, "tema": "Preparación de presentación final", "fecha": "09/11", "tag": "Parcial 3"},',
            '{"n": 14, "tema": "Parcial 3", "fecha": "09/11"},',
        ),
        (
            "Hitos: avance **Clase 11** (19/10) · prep. **Clase 14** (09/11) · cierre **Clase 15** (16/11, autónoma).",
            "Hitos: avance **Clase 11** (19/10) · prep. **Clase 12** (26/10) · Parcial 3 **Clase 14** (09/11) · cierre **Clase 15** (16/11, autónoma).",
        ),
    ],
}


PARCIALES_PATCHES = [
    # Prog2 P1
    (
        "            _tema(4, '02/09', 'Mapas y conjuntos'),\n"
        "            _tema(5, '09/09', 'Interfaces gráficas GUI'),",
        "            _tema(4, '02/09', 'Mapas y conjuntos · Interfaces gráficas GUI'),",
    ),
    # Prog2 P2
    (
        "            _tema(9, '07/10', 'Refactorización con IA'),\n"
        "            _tema(10, '14/10', 'Persistencia de archivos'),",
        "            _tema(9, '07/10', 'Refactorización con IA · Persistencia de archivos'),",
    ),
    # Prog2 P3
    (
        "            _tema(14, '11/11', 'Preparación presentación final'),\n"
        "            _tema(15, '18/11', 'Evaluación de proyectos + cierre'),",
        "            _tema(14, '11/11', 'Preparación presentación final · Evaluación de proyectos + cierre'),",
    ),
    # Sem P1 — caso estudio = el parcial; eliminar de cobertura temática
    (
        "            _tema(4, '03/09', 'Metodologías ágiles'),\n"
        "            _tema(5, '10/09', 'Caso estudio evaluativo'),",
        "            _tema(4, '03/09', 'Metodologías ágiles'),",
    ),
    # Sem P2
    (
        "            _tema(9, '08/10', 'Casos de uso'),\n"
        "            _tema(10, '15/10', 'Caso estudio evaluativo'),",
        "            _tema(9, '08/10', 'Casos de uso'),",
    ),
    # Sem P3
    (
        "            _tema(14, '12/11', 'Evaluación final (prep. sustentación)'),\n"
        "            _tema(15, '19/11', 'Sustentación de proyectos + cierre'),",
        "            _tema(14, '12/11', 'Evaluación final (prep. sustentación) · Sustentación de proyectos + cierre'),",
    ),
    # BD2 P1
    (
        "            _tema(4, '31/08', 'Funciones y disparadores'),\n"
        "            _tema(5, '07/09', 'Seguridad y respaldo'),",
        "            _tema(4, '31/08', 'Funciones y disparadores · Seguridad y respaldo'),",
    ),
    # BD2 P2
    (
        "            _tema(8, '28/09', 'Tuning de bases de datos'),\n"
        "            _tema(9, '05/10', 'Gestión de transacciones'),",
        "            _tema(8, '28/09', 'Tuning de bases de datos · Gestión de transacciones'),",
    ),
    # BD2 P3
    (
        "            _tema(12, '26/10', 'Integración de aplicaciones externas'),\n"
        "            _tema(13, '02/11', 'Análisis de casos reales (autónoma)'),\n"
        "            _tema(14, '09/11', 'Preparación de presentación final'),",
        "            _tema(12, '26/10', 'Integración de aplicaciones externas · Preparación de presentación final'),\n"
        "            _tema(13, '02/11', 'Análisis de casos reales (autónoma)'),",
    ),
    # Arq P1
    (
        "            _tema(4, '31/08', 'Microservicios'),\n"
        "            _tema(5, '07/09', 'Arquitecturas distribuidas'),",
        "            _tema(4, '31/08', 'Microservicios · Arquitecturas distribuidas'),",
    ),
    # Arq P2
    (
        "            _tema(8, '28/09', 'Monitoreo y optimización'),\n"
        "            _tema(9, '05/10', 'Integración continua y despliegue (CI/CD)'),",
        "            _tema(8, '28/09', 'Monitoreo y optimización · Integración continua y despliegue (CI/CD)'),",
    ),
    # Arq P3
    (
        "            _tema(12, '26/10', 'Pruebas de rendimiento'),\n"
        "            _tema(13, '02/11', 'Escalabilidad automática (autónoma)'),\n"
        "            _tema(14, '09/11', 'Preparación de presentación final'),",
        "            _tema(12, '26/10', 'Pruebas de rendimiento · Preparación de presentación final'),\n"
        "            _tema(13, '02/11', 'Escalabilidad automática (autónoma)'),",
    ),
]


def patch_json_and_rules() -> None:
    # uniajc.json
    uj = ROOT / ".config/universidades/uniajc.json"
    text = uj.read_text(encoding="utf-8")
    old_hitos = (
        '"hitos_lun_2026_2": "Clase 11 avance · Clase 14 prep. presentacion (+ Parcial 3) · '
        'Clase 15 cierre/sustentacion (autonoma)"'
    )
    new_hitos = (
        '"hitos_lun_2026_2": "Clase 11 avance · Clase 12 prep. presentacion · '
        'Clase 14 Parcial 3 (solo evaluacion) · Clase 15 cierre/sustentacion (autonoma)"'
    )
    if old_hitos in text:
        text = text.replace(old_hitos, new_hitos)
    rule_key = '"regla_parciales_solo_eval"'
    if rule_key not in text:
        insert = (
            ',\n    "regla_parciales_solo_eval": "Dia de parcial = solo evaluacion; '
            'sin tema de trabajo dirigido nuevo. El tema tecnico del dia se elimina o '
            'se mueve a la ultima clase regular anterior del mismo corte si no existia '
            'en clases previas. Prep PI / sustentacion van en la clase regular anterior, '
            'no el mismo dia del parcial."'
        )
        # insert before last closing of evaluacion.teorico or after regla_parciales in periodo
        anchor = '"regla_modalidad_sesion": "Clase 1 presencial; demás regulares virtual (síncrona); parciales presencial; festivos autónoma."'
        if anchor in text:
            text = text.replace(anchor, anchor + insert, 1)
    uj.write_text(text, encoding="utf-8")
    print("OK json", uj.relative_to(ROOT))

    # semestre json
    sj = ROOT / ".config/calendario/semestre_2026_2.json"
    st = sj.read_text(encoding="utf-8")
    if "solo evaluación" not in st and "solo evaluacion" not in st:
        anchor = '"regla_parciales":'
        # add sibling key after regla_modalidad_sesion at end
        end_anchor = (
            '"regla_modalidad_sesion": "Clase 1 presencial; demás regulares virtual (síncrona); '
            'parciales presencial; festivos autónoma."\n}'
        )
        addition = (
            '"regla_modalidad_sesion": "Clase 1 presencial; demás regulares virtual (síncrona); '
            'parciales presencial; festivos autónoma.",\n'
            '  "regla_parcial_solo_eval": "Día de parcial = solo evaluación; sin tema de trabajo '
            'dirigido nuevo. No mezclar tema técnico · Parcial N. La prep del PI va en la clase '
            'regular anterior."\n}'
        )
        if end_anchor in st:
            st = st.replace(end_anchor, addition)
            sj.write_text(st, encoding="utf-8")
            print("OK json", sj.relative_to(ROOT))
        else:
            print("WARN semestre json anchor not found")
    else:
        print("SKIP semestre json already has rule")


def patch_agent_md(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    needle = (
        "8. Evaluación teórica: 30/30/40. Parciales **siempre presenciales y síncronos**; "
        "**NUNCA** en festivo/autónoma."
    )
    rule = (
        "8. Evaluación teórica: 30/30/40. Parciales **siempre presenciales y síncronos**; "
        "**NUNCA** en festivo/autónoma. **Día de parcial = solo evaluación** (sin tema de "
        "trabajo dirigido nuevo; no mezclar «Tema · Parcial N»). Prep PI / sustentación van "
        "en la clase regular anterior."
    )
    if "Día de parcial = solo evaluación" not in text:
        if needle not in text:
            raise SystemExit(f"Agent needle missing in {path}")
        text = text.replace(needle, rule, 1)
    # PI hitos wording
    text = text.replace(
        "guía + rúbrica + hitos Clases 11 / 14 / 15",
        "guía + rúbrica + hitos Clases 11 / 12 (prep) / 14 (Parcial 3) / 15",
    )
    path.write_text(text, encoding="utf-8")
    print("OK agent", path.relative_to(ROOT))


def patch_cursor_rule() -> None:
    path = ROOT / ".cursor/rules/uniajc-docente.mdc"
    text = path.read_text(encoding="utf-8")
    if "Día de parcial = solo evaluación" not in text:
        insert = (
            "\n- **Día de parcial = solo evaluación:** sin tema de trabajo dirigido nuevo "
            "(no «Tema · Parcial N»). La prep del PI / sustentación va en la clase regular "
            "anterior; el día del parcial es solo el parcial.\n"
        )
        anchor = "- **Regla de parciales:** siempre síncronos;"
        if anchor not in text:
            raise SystemExit("cursor rule anchor missing")
        # insert after the parciales rule paragraph
        m = re.search(r"(- \*\*Regla de parciales:\*\*[^\n]*\n)", text)
        if not m:
            raise SystemExit("cursor rule regex missing")
        text = text[: m.end()] + insert + text[m.end() :]
    # PI hitos in uniajc.json already; also update any prep+Parcial mention
    text = text.replace(
        "hitos en `Kit docente/Proyecto Integrador/` (privado). Peso Acuerdo: **20% Corte 3**.",
        "hitos en `Kit docente/Proyecto Integrador/` (privado; prep en clase anterior al Parcial 3). "
        "Peso Acuerdo: **20% Corte 3**.",
    )
    path.write_text(text, encoding="utf-8")
    print("OK rule", path.relative_to(ROOT))


def main() -> None:
    for path, reps in PLANS.items():
        patch_text(path, reps, "plan")
        insert_rule_note(path)

    for path, temas in CSV_UPDATES.items():
        update_csv(path, temas)

    for dst, src in CONFIG_CSV_MAP.items():
        dst.write_bytes(src.read_bytes())
        print("OK copy", dst.relative_to(ROOT))
    rebuild_todos()

    for path, reps in BUILD_PATCHES.items():
        patch_text(path, reps, "build")

    parciales = ROOT / ".config/parciales/contenido_parciales_2026_2.py"
    patch_text(parciales, PARCIALES_PATCHES, "parciales")

    # docstring note
    pt = parciales.read_text(encoding="utf-8")
    if "Día de parcial" not in pt:
        old = "  - Formato en portada: «Clase N · DD/MM · Tema».\n"
        new = (
            "  - Formato en portada: «Clase N · DD/MM · Tema».\n"
            "  - Día de parcial = solo evaluación: la cobertura lista los temas en la clase\n"
            "    donde se impartieron (no inventa tema técnico en la fila del parcial).\n"
        )
        if old not in pt:
            raise SystemExit("parciales docstring anchor missing")
        parciales.write_text(pt.replace(old, new), encoding="utf-8")

    pi = ROOT / ".config/slides/build_uniajc_pi_2026_2.py"
    # Fix PI patches carefully (string concat)
    pi_text = pi.read_text(encoding="utf-8")
    old1 = (
        '              ["Prep. presentación", "Clase 14",\n'
        '               "Ensayo + entrega final en Campus Virtual "\n'
        '               "(suele coincidir con Parcial 3 del corte)"],'
    )
    new1 = (
        '              ["Prep. presentación", "Clase 12",\n'
        '               "Ensayo + entrega final en Campus Virtual "\n'
        '               "(prep. del PI; Parcial 3 solo evaluación en Clase 14)"],'
    )
    old2 = (
        '              ["Prep. presentación", "Clase 14",\n'
        '               "Ensayo + entrega final (suele coincidir con Parcial 3)"],'
    )
    new2 = (
        '              ["Prep. presentación", "Clase 12",\n'
        '               "Ensayo + entrega final (prep. del PI; Parcial 3 solo en Clase 14)"],'
    )
    for old, new in ((old1, new1), (old2, new2)):
        if old not in pi_text:
            raise SystemExit(f"PI patch missing:\n{old}")
        pi_text = pi_text.replace(old, new)
    pi.write_text(pi_text, encoding="utf-8")
    print("OK pi", pi.relative_to(ROOT))

    patch_json_and_rules()
    for ap in (
        ROOT / ".claude/agents/disenador-curricular-uniajc.md",
        ROOT / ".cursor/agents/disenador-curricular-uniajc.md",
    ):
        if ap.exists():
            patch_agent_md(ap)
    patch_cursor_rule()
    print("DONE")


if __name__ == "__main__":
    main()
