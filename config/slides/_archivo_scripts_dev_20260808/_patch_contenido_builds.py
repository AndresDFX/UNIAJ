# -*- coding: utf-8 -*-
"""One-shot: replace dense cronograma tables with contenido_clases_slides in curso builds."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

IMPORT_OLD = """from uniajc_slides_engine import (
    new_prs, course_cover, tutor_slide, padlet_slide, content_slide, table_content,
    box_note_slide, closing_slide,
)"""

IMPORT_NEW = """from uniajc_slides_engine import (
    new_prs, course_cover, tutor_slide, padlet_slide, content_slide, table_content,
    contenido_clases_slides, box_note_slide, closing_slide,
)"""

# Regex: two consecutive Cronograma table_content(...) blocks
CRONO_RE = re.compile(
    r"\n    table_content\(\s*\n"
    r'\s*prs,\s*"Cronograma de clases \(1–8\)".*?'
    r"\n    table_content\(\s*\n"
    r'\s*prs,\s*"Cronograma de clases \(9–15\)".*?'
    r"\n    \)\n",
    re.DOTALL,
)

SEMINARIO = '''
    # Estilo CONTENIDO (lista limpia) — temas desde Plan curso/PLAN_DE_CURSO_2026-2.md
    contenido_clases_slides(
        prs,
        [
            {"n": 1, "tema": "Acuerdo y conceptos", "fecha": "13/08"},
            {"n": 2, "tema": "Ciclos de vida", "fecha": "20/08"},
            {"n": 3, "tema": "Metodologías tradicionales", "fecha": "27/08"},
            {"n": 4, "tema": "Metodologías ágiles", "fecha": "03/09"},
            {"n": 5, "tema": "Caso estudio evaluativo", "fecha": "10/09", "tag": "Parcial 1"},
            {"n": 6, "tema": "Requerimientos de software", "fecha": "17/09"},
            {"n": 7, "tema": "Historias de usuario", "fecha": "24/09"},
            {"n": 8, "tema": "Introducción a UML", "fecha": "01/10"},
            {"n": 9, "tema": "Casos de uso", "fecha": "08/10"},
            {"n": 10, "tema": "Caso estudio evaluativo", "fecha": "15/10", "tag": "Parcial 2"},
            {"n": 11, "tema": "Avance proyecto integrador", "fecha": "22/10"},
            {"n": 12, "tema": "Diagramas UML avanzados", "fecha": "29/10"},
            {"n": 13, "tema": "Diseño de interfaces", "fecha": "05/11"},
            {"n": 14, "tema": "Evaluación final (prep. sustentación)", "fecha": "12/11"},
            {"n": 15, "tema": "Sustentación de proyectos + cierre", "fecha": "19/11", "tag": "Parcial 3"},
        ],
        title="CONTENIDO",
        idx_start=8,
    )
'''

BD2 = '''
    # Estilo CONTENIDO (lista limpia) — temas desde Plan curso/PLAN_DE_CURSO_2026-2.md
    contenido_clases_slides(
        prs,
        [
            {"n": 1, "tema": "Presentación · Revisión BD I", "fecha": "10/08"},
            {"n": 2, "tema": "Administración de bases de datos", "fecha": "17/08", "tag": "Autónoma"},
            {"n": 3, "tema": "Procedimientos almacenados", "fecha": "24/08"},
            {"n": 4, "tema": "Funciones y disparadores", "fecha": "31/08"},
            {"n": 5, "tema": "Seguridad y respaldo", "fecha": "07/09", "tag": "Parcial 1"},
            {"n": 6, "tema": "Optimización de consultas", "fecha": "14/09"},
            {"n": 7, "tema": "Índices y particionamiento", "fecha": "21/09"},
            {"n": 8, "tema": "Tuning de bases de datos", "fecha": "28/09"},
            {"n": 9, "tema": "Gestión de transacciones", "fecha": "05/10", "tag": "Parcial 2"},
            {"n": 10, "tema": "Control de concurrencia", "fecha": "12/10", "tag": "Autónoma"},
            {"n": 11, "tema": "Avance del proyecto final", "fecha": "19/10"},
            {"n": 12, "tema": "Integración de aplicaciones externas", "fecha": "26/10"},
            {"n": 13, "tema": "Análisis de casos reales", "fecha": "02/11", "tag": "Autónoma"},
            {"n": 14, "tema": "Preparación de presentación final", "fecha": "09/11", "tag": "Parcial 3"},
            {"n": 15, "tema": "Presentación del proyecto + cierre", "fecha": "16/11", "tag": "Autónoma"},
        ],
        title="CONTENIDO",
        idx_start=8,
    )
'''

ARQ = '''
    # Estilo CONTENIDO (lista limpia) — temas desde Plan curso/PLAN_DE_CURSO_2026-2.md
    contenido_clases_slides(
        prs,
        [
            {"n": 1, "tema": "Presentación · Introducción a arquitecturas cloud", "fecha": "10/08"},
            {"n": 2, "tema": "Modelos de servicio: IaaS / PaaS / SaaS", "fecha": "17/08", "tag": "Autónoma"},
            {"n": 3, "tema": "Virtualización y contenedores", "fecha": "24/08"},
            {"n": 4, "tema": "Microservicios", "fecha": "31/08"},
            {"n": 5, "tema": "Arquitecturas distribuidas", "fecha": "07/09", "tag": "Parcial 1"},
            {"n": 6, "tema": "Seguridad en la nube", "fecha": "14/09"},
            {"n": 7, "tema": "Redes y almacenamiento cloud", "fecha": "21/09"},
            {"n": 8, "tema": "Monitoreo y optimización", "fecha": "28/09"},
            {"n": 9, "tema": "CI/CD", "fecha": "05/10", "tag": "Parcial 2"},
            {"n": 10, "tema": "Costos y sostenibilidad cloud", "fecha": "12/10", "tag": "Autónoma"},
            {"n": 11, "tema": "Avance del proyecto final", "fecha": "19/10"},
            {"n": 12, "tema": "Pruebas de rendimiento", "fecha": "26/10"},
            {"n": 13, "tema": "Escalabilidad automática", "fecha": "02/11", "tag": "Autónoma"},
            {"n": 14, "tema": "Preparación de presentación final", "fecha": "09/11", "tag": "Parcial 3"},
            {"n": 15, "tema": "Presentación del proyecto + cierre", "fecha": "16/11", "tag": "Autónoma"},
        ],
        title="CONTENIDO",
        idx_start=8,
    )
'''

PATCHES = {
    "build_uniajc_seminario_curso.py": SEMINARIO,
    "build_uniajc_bd2_curso.py": BD2,
    "build_uniajc_arq_curso.py": ARQ,
}


def patch_file(name: str, replacement: str) -> None:
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    if "contenido_clases_slides" not in text.split("def build")[0]:
        if IMPORT_OLD not in text:
            raise SystemExit(f"{name}: import block not found")
        text = text.replace(IMPORT_OLD, IMPORT_NEW, 1)
    m = CRONO_RE.search(text)
    if not m:
        # Already patched?
        if "contenido_clases_slides(" in text:
            print(f"SKIP (already patched): {name}")
            return
        raise SystemExit(f"{name}: cronograma blocks not found")
    text = CRONO_RE.sub("\n" + replacement.rstrip() + "\n", text, count=1)
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"OK patched: {name}")


def main():
    for name, repl in PATCHES.items():
        patch_file(name, repl)


if __name__ == "__main__":
    main()
