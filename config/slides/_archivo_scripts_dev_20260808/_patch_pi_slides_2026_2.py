# -*- coding: utf-8 -*-
"""Actualiza slide Proyecto Integrador en Presentación del Curso BD II / Arq."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

BD2_OLD = '''    content_slide(prs, "Proyecto Integrador", [
        'Sistema avanzado de BD para gestión segura y optimizada de información empresarial (ABPr).',
        'Incluye administración, automatización (procedimientos/triggers) y tuning.',
        'Pesa **20%** en el tercer corte.',
    ], idx=10)
'''

BD2_NEW = '''    content_slide(prs, "Proyecto Integrador", [
        '**VetCare DB** — BD avanzada para clínica veterinaria (ABPr).',
        'Integra seguridad/respaldo, procs/triggers, optimización e integración app↔BD.',
        'Hitos: avance **Clase 11** (19/10) · prep. **Clase 14** (09/11) · cierre **Clase 15** (16/11, autónoma).',
        'Pesa **20%** del Corte 3. Enunciado: carpeta `Clases/Proyecto Integrador/`.',
    ], idx=10)
'''

ARQ_OLD = '''    content_slide(prs, "Proyecto Integrador", [
        'Diseño y simulación de una **arquitectura cloud** para una aplicación web o empresarial.',
        'Aplica escalabilidad, seguridad y sostenibilidad.',
        'Pesa **20%** en el tercer corte; cierre con sustentación.',
    ], idx=10)
'''

ARQ_NEW = '''    content_slide(prs, "Proyecto Integrador", [
        '**CloudLite App** — diseño/despliegue de arquitectura cloud (diagramas + labs).',
        'Contenedores (Killercoda / Play with Docker) · CI/CD conceptual (GitHub Actions) · **sin** cloud con tarjeta.',
        'Hitos: avance **Clase 11** (19/10) · prep. **Clase 14** (09/11) · cierre **Clase 15** (16/11, autónoma).',
        'Pesa **20%** del Corte 3. Enunciado: carpeta `Clases/Proyecto Integrador/`.',
    ], idx=10)
'''


def patch(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new.strip() in text:
        print("SKIP already patched", path.name)
        return
    if old not in text:
        # fallback: find block by title
        start = text.find('content_slide(prs, "Proyecto Integrador"')
        if start < 0:
            raise SystemExit(f"MISSING PI slide in {path.name}")
        end = text.find("content_slide(prs, \"Recursos\"", start)
        if end < 0:
            raise SystemExit(f"MISSING Recursos after PI in {path.name}")
        text = text[:start] + new + "\n" + text[end:]
        path.write_text(text, encoding="utf-8")
        print("OK replaced by anchor", path.name)
        return
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print("OK exact", path.name)


def main():
    patch(ROOT / "build_uniajc_bd2_curso.py", BD2_OLD, BD2_NEW)
    patch(ROOT / "build_uniajc_arq_curso.py", ARQ_OLD, ARQ_NEW)


if __name__ == "__main__":
    main()
