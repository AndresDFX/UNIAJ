# -*- coding: utf-8 -*-
"""Limpieza puntual BD II + Arquitectura (herramientas sin tarjeta, CSV temas). No dejar en repo permanente."""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

HERR_ARQ = """# Propuesta de herramientas — Arquitectura de Sistemas Computacionales (2026-2)

Grupo: **6303C** · FI303380 · lun 10:00–12:00

## Herramientas del curso (lista ajustada)

> Criterio UNIAJC: **herramientas gratuitas + en el navegador**, **sin tarjeta de crédito**. Los estudiantes **no deben instalar** hipervisores, IDEs pesados ni CLIs obligatorias en su PC. Se eliminaron AWS / GCP / Oracle Cloud Free Tier (y cualquier IaaS/PaaS que exija tarjeta).

| Uso en clase | Herramienta (gratis / navegador) | Acceso | Notas |
|---|---|---|---|
| Arquitectura / C4 / diagramas | **draw.io / diagrams.net** (https://app.diagrams.net) | Navegador | Componentes, despliegue, redes |
| Bocetos y talleres colaborativos | **Excalidraw** (https://excalidraw.com) | Navegador | Bajo roce, sin cuenta |
| Contenedores conceptuales (sin Docker local) | **Play with Docker** (https://labs.play-with-docker.com) o **Killercoda** (https://killercoda.com) | Navegador | Labs temporales en browser |
| Kubernetes intro (opcional) | **Killercoda** (labs gratuitos) | Navegador | Solo demos guiadas |
| CI/CD conceptual (opcional) | **GitHub Actions** (cuenta free) + repo free | Navegador | Pipelines simples; sin runner local; sin tarjeta para demos básicas |
| Documentación / entregas | **Google Docs / Drive** o Word Online | Navegador | Talleres en `.docx` en `Clases/` |
| Rompe-hielo / muro | **Padlet** del curso | Navegador | URL institucional del docente |

### Qué NO pediremos
- Cloud IaaS/PaaS que exija **tarjeta** (AWS Free Tier, GCP Free Tier, Oracle Cloud Free Tier, Azure, etc.).
- Instalar VirtualBox/VMware/Docker Desktop/WSL como requisito del curso.
- Software de modelado de pago (Enterprise Architect, Visio de pago, etc.).
- Costos de cloud de pago (el estudiante no asume costos).

### Estado
- **Lista ajustada — pendiente OK docente para generar Clase N.**
"""

HERR_BD2 = """# Propuesta de herramientas — Bases de Datos II (2026-2)

Grupo: **641A-2** · FI303215 · lun 18:00–20:00

## Herramientas del curso (lista ajustada)

> Criterio UNIAJC: **herramientas gratuitas + en el navegador**, **sin tarjeta de crédito**. Los estudiantes **no deben instalar** software de escritorio de pago ni SGBD locales obligatorios. Cuenta gratuita (email) solo si el servicio lo exige.

| Uso en clase | Herramienta (gratis / navegador) | Acceso | Notas |
|---|---|---|---|
| SQL práctico (consultas, DDL/DML) | **DB Fiddle** (https://dbfiddle.uk / https://dbfiddle.dev) o **OneCompiler SQL** | Navegador | Playground inmediato; compartir enlace del ejercicio |
| Alternativa multi-motor (MySQL/PostgreSQL/Oracle-like) | **SQLTest.online Playground** (https://sqltest.online) o **RunSQL** (https://runsql.com) | Navegador | Comparar dialectos sin instalar SGBD |
| Procedimientos / PL-SQL orientativo | **Oracle Live SQL** (https://livesql.oracle.com) | Navegador + cuenta Oracle free | Ideal para procedimientos, funciones y triggers (cuenta free típica **sin tarjeta**) |
| Diagramas ER / modelo | **draw.io / diagrams.net** (https://app.diagrams.net) | Navegador | Exportar PNG/SVG a la entrega |
| Diseño colaborativo rápido | **Excalidraw** (https://excalidraw.com) | Navegador | Bocetos de modelo / flujo |
| Documentación / entregas | **Google Docs / Drive** o Word Online | Navegador | Talleres en `.docx` en carpeta `Clases/` |
| Rompe-hielo / muro | **Padlet** del curso | Navegador | URL institucional del docente |

### Qué NO pediremos
- Instalar Oracle/MySQL/PostgreSQL/SQL Server en el PC del estudiante.
- Licencias de escritorio de pago (Toad, DataGrip de pago, etc.).
- Docker obligatorio en el equipo del estudiante.
- Cloud IaaS/PaaS con tarjeta (no aplica a este curso).

### Estado
- **Lista ajustada — pendiente OK docente para generar Clase N.**
"""

TEMAS_ARQ = {
    1: "Presentación del curso · Introducción a arquitecturas cloud",
    2: "Modelos de servicio: IaaS / PaaS / SaaS",
    3: "Virtualización y contenedores",
    4: "Microservicios",
    5: "Arquitecturas distribuidas",
    6: "Seguridad en la nube",
    7: "Redes y almacenamiento cloud",
    8: "Monitoreo y optimización",
    9: "Integración continua y despliegue (CI/CD)",
    10: "Costos y sostenibilidad cloud",
    11: "Avance del proyecto final",
    12: "Pruebas de rendimiento",
    13: "Escalabilidad automática (Todos los Santos)",
    14: "Preparación de presentación final",
    15: "Presentación del proyecto + cierre",
}

TEMAS_BD2 = {
    1: "Presentación del curso · Revisión de Bases de Datos I",
    2: "Administración de bases de datos",
    3: "Procedimientos almacenados",
    4: "Funciones y disparadores",
    5: "Seguridad y respaldo",
    6: "Optimización de consultas",
    7: "Índices y particionamiento",
    8: "Tuning de bases de datos",
    9: "Gestión de transacciones",
    10: "Control de concurrencia",
    11: "Avance del proyecto final",
    12: "Integración de aplicaciones externas",
    13: "Análisis de casos reales (Todos los Santos)",
    14: "Preparación de presentación final",
    15: "Presentación del proyecto + cierre",
}


def fix_csv(path: Path, temas: dict[int, str], curso_filter: str | None = None) -> int:
    rows = list(csv.DictReader(path.read_text(encoding="utf-8").splitlines()))
    if not rows:
        return 0
    fieldnames = list(rows[0].keys())
    changed = 0
    out = []
    for r in rows:
        if curso_filter and r.get("curso") != curso_filter:
            out.append(r)
            continue
        n = int(r["clase_n"])
        if n in temas and r.get("tema") != temas[n]:
            r["tema"] = temas[n]
            changed += 1
        # dedupe notas "parcial presencial sincrono; parcial presencial sincrono"
        notas = r.get("notas") or ""
        parts = [p.strip() for p in notas.split(";") if p.strip()]
        dedup = []
        for p in parts:
            if p not in dedup:
                dedup.append(p)
        new_notas = "; ".join(dedup)
        if new_notas != notas:
            r["notas"] = new_notas
            changed += 1
        out.append(r)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out)
    return changed


def replace_herramientas_section(md: str, new_block: str) -> str:
    """Replace from '## Herramientas del curso' through '### Estado' block."""
    # Keep content before herramientas; replace from ## Herramientas ... until next ## that is not ### 
    m = re.search(r"^## Herramientas del curso.*?(?=^## [^#]|\Z)", md, flags=re.M | re.S)
    if not m:
        raise RuntimeError("No se encontró sección ## Herramientas del curso")
    # new_block already has the ## heading; strip leading title lines if present
    block = new_block
    # Extract only from ## Herramientas ... (skip title/grupo of standalone file)
    bm = re.search(r"^## Herramientas del curso.*", block, flags=re.M | re.S)
    if not bm:
        raise RuntimeError("new_block inválido")
    section = bm.group(0).rstrip() + "\n\n"
    return md[: m.start()] + section + md[m.end() :]


def patch_arq_build(path: Path) -> None:
    t = path.read_text(encoding="utf-8")
    t = t.replace(
        "Estructura: **Teoría Core** → **Taller / laboratorio cloud (free tier)** → **Quiz / avance PI**.",
        "Estructura: **Teoría Core** → **Taller / laboratorio en navegador** → **Quiz / avance PI**.",
    )
    t = t.replace(
        "Práctica con herramientas **gratis + en la nube** (AWS/Azure/GCP free tier o simuladores).",
        "Práctica con herramientas **gratis en navegador** (draw.io, Killercoda / Play with Docker; sin cloud con tarjeta).",
    )
    old_recursos = """    content_slide(prs, "Recursos", [
        'Herramientas **gratis en navegador** (sin instalación obligatoria) — detalle en Plan de curso (pendiente aprobación docente).',
        'Diagramas: **draw.io / diagrams.net**; bocetos: **Excalidraw**.',
        'Labs cloud/contenedores: **Killercoda** / Play with Docker · CI: **GitHub Actions** (free).',
        'Cloud free tier (demo): Oracle / GCP / AWS Free Tier — sin costos de pago para el estudiante.',
        'Bibliografia: Erl · Buyya · Hwang · docs AWS/Azure/GCP.',
    ], idx=11)"""
    # flexible match on recursos slide
    m = re.search(
        r"content_slide\(prs, \"Recursos\", \[\s*.*?\], idx=11\)",
        t,
        flags=re.S,
    )
    if not m:
        raise RuntimeError("No se encontró slide Recursos en build arq")
    new_recursos = """content_slide(prs, "Recursos", [
        'Herramientas **gratis en navegador**, **sin tarjeta** — lista ajustada; pendiente OK docente para Clase N.',
        'Diagramas: **draw.io / diagrams.net**; bocetos: **Excalidraw**.',
        'Labs contenedores: **Killercoda** / **Play with Docker** · CI opcional: **GitHub Actions** (cuenta free).',
        'Entregas: **Google Docs / Word Online** · Rompe-hielo: **Padlet** del curso.',
        'Bibliografía: Erl · Buyya · Hwang · docs oficiales de contenedores/CI (sin IaaS con tarjeta).',
    ], idx=11)"""
    t = t[: m.start()] + new_recursos + t[m.end() :]
    path.write_text(t, encoding="utf-8")


def main() -> None:
    arq_dir = ROOT / "Arquitectura de Sistemas Computacionales" / "Plan curso"
    bd2_dir = ROOT / "Bases de Datos II" / "Plan curso"

    (arq_dir / "HERRAMIENTAS_PROPUESTA_2026-2.md").write_text(HERR_ARQ, encoding="utf-8")
    (bd2_dir / "HERRAMIENTAS_PROPUESTA_2026-2.md").write_text(HERR_BD2, encoding="utf-8")

    arq_plan = arq_dir / "PLAN_DE_CURSO_2026-2.md"
    bd2_plan = bd2_dir / "PLAN_DE_CURSO_2026-2.md"
    arq_plan.write_text(replace_herramientas_section(arq_plan.read_text(encoding="utf-8"), HERR_ARQ), encoding="utf-8")
    bd2_plan.write_text(replace_herramientas_section(bd2_plan.read_text(encoding="utf-8"), HERR_BD2), encoding="utf-8")

    patch_arq_build(ROOT / ".config" / "slides" / "build_uniajc_arq_curso.py")

    csv_targets = [
        (arq_dir / "calendario_eventos_2026-2.csv", TEMAS_ARQ, None),
        (bd2_dir / "calendario_eventos_2026-2.csv", TEMAS_BD2, None),
        (ROOT / ".config" / "calendario" / "eventos_arquitectura_2026-2.csv", TEMAS_ARQ, None),
        (ROOT / ".config" / "calendario" / "eventos_bases_datos_ii_2026-2.csv", TEMAS_BD2, None),
    ]
    for path, temas, filt in csv_targets:
        if path.exists():
            n = fix_csv(path, temas, filt)
            print(f"CSV {path.name}: {n} ajustes")

    todos = ROOT / ".config" / "calendario" / "eventos_todos_cursos_2026-2.csv"
    if todos.exists():
        n1 = fix_csv(todos, TEMAS_ARQ, "Arquitectura de Sistemas Computacionales")
        n2 = fix_csv(todos, TEMAS_BD2, "Bases de Datos II")
        print(f"CSV eventos_todos: arq={n1} bd2={n2}")

    print("OK cleanup fuentes")


if __name__ == "__main__":
    main()
