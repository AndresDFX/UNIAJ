# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parent

BD2 = """    content_slide(prs, "Proyecto Integrador", [
        '**VetCare DB** — BD avanzada para clínica veterinaria (ABPr).',
        'Integra seguridad/respaldo, procs/triggers, optimización e integración app↔BD.',
        'Hitos: avance **Clase 11** (19/10) · prep. **Clase 14** (09/11) · cierre **Clase 15** (16/11, autónoma).',
        'Pesa **20%** del Corte 3. Enunciado: carpeta `Clases/Proyecto Integrador/`.',
    ], idx=10)
"""

ARQ = """    content_slide(prs, "Proyecto Integrador", [
        '**CloudLite App** — diseño/despliegue de arquitectura cloud (diagramas + labs).',
        'Contenedores (Killercoda / Play with Docker) · CI/CD conceptual (GitHub Actions) · **sin** cloud con tarjeta.',
        'Hitos: avance **Clase 11** (19/10) · prep. **Clase 14** (09/11) · cierre **Clase 15** (16/11, autónoma).',
        'Pesa **20%** del Corte 3. Enunciado: carpeta `Clases/Proyecto Integrador/`.',
    ], idx=10)
"""


def fix(path: Path, block: str) -> None:
    text = path.read_text(encoding="utf-8")
    marker = 'content_slide(prs, "Proyecto Integrador"'
    start = text.find(marker)
    if start < 0:
        raise SystemExit("no PI in " + path.name)
    start = text.rfind("\n", 0, start) + 1
    end = text.find('content_slide(prs, "Recursos"', start)
    if end < 0:
        raise SystemExit("no Recursos in " + path.name)
    path.write_text(text[:start] + block + "\n" + text[end:], encoding="utf-8")
    print("OK", path.name)


if __name__ == "__main__":
    fix(ROOT / "build_uniajc_bd2_curso.py", BD2)
    fix(ROOT / "build_uniajc_arq_curso.py", ARQ)
