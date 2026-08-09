# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
CREDS_NEW = """CREDS = [
    \"Ingeniero de Sistemas\",
    \"Candidato a MsC en Inteligencia Artificial\",
    \"Líder Técnico\",
    \"Speaker Tecnológico\",
]
"""

BLOCKS = {
    "build_uniajc_seminario_curso.py": """content_slide(prs, \"Objetivo de aprendizaje\", [
        '@@Objeto de estudio:@@ integración de conocimientos para el desarrollo y presentación de proyectos de software orientados a objetos.',
        '**Objetivo:** desarrollar un proyecto de software aplicando técnicas avanzadas de **POO**, fortaleciendo la documentación, validación y comunicación efectiva de soluciones.',
        'Consolida lo aprendido en Programación II mediante análisis, diseño, desarrollo y exposición de proyectos integradores.',
        'Se fortalecen patrones de diseño, documentación técnica, pruebas funcionales y despliegue básico de aplicaciones.',
    ], idx=5, size=15)
    content_slide(prs, \"Resultados de aprendizaje (RAA)\", [
        '**RAA1** — Aplica patrones de diseño y principios de modularidad en proyectos de software. Organiza el código para que sea reutilizable, mantenible y colaborativo.',
        '**RAA2** — Documenta y valida aplicaciones mediante pruebas básicas. Elabora documentación técnica y realiza pruebas/validaciones funcionales del producto.',
        '**RAA3** — Presenta y sustenta proyectos de software de manera clara y estructurada. Comunica la solución tecnológica con calidad y compromiso profesional.',
    ], idx=6, size=15)
    """,
    "build_uniajc_bd2_curso.py": """content_slide(prs, \"Objetivo de aprendizaje\", [
        '@@Objeto de estudio:@@ gestión avanzada y optimización de bases de datos relacionales.',
        '**Objetivo:** diseñar, administrar y optimizar bases de datos relacionales avanzadas, garantizando **seguridad**, **integridad** y **eficiencia** en el manejo de grandes volúmenes de información.',
        'Profundiza en optimización, seguridad, procedimientos almacenados y administración eficiente de los recursos de información.',
        'Consolida habilidades clave para Arquitectura de Sistemas Computacionales y Seguridad.',
    ], idx=5, size=15)
    content_slide(prs, \"Resultados de aprendizaje (RAA)\", [
        '**RAA1** — Administra bases de datos aplicando estrategias de seguridad y respaldo. Configura políticas de protección y planes de respaldo/recuperación responsables.',
        '**RAA2** — Implementa procedimientos almacenados y disparadores para la automatización de procesos. Desarrolla lógica en el motor de BD para integridad y reutilización.',
        '**RAA3** — Optimiza consultas y estructuras de bases de datos para mejorar el rendimiento del sistema. Aplica índices, tuning y análisis de rendimiento sobre casos reales.',
    ], idx=6, size=15)
    """,
    "build_uniajc_arq_curso.py": """content_slide(prs, \"Objetivo de aprendizaje\", [
        '@@Objeto de estudio:@@ diseño, implementación y gestión de arquitecturas de sistemas computacionales en entornos cloud.',
        '**Objetivo:** diseñar e implementar arquitecturas aplicando principios de **computación en la nube**, **virtualización** y **escalabilidad**, asegurando eficiencia y sostenibilidad.',
        'Fortalece la comprensión de infraestructura moderna enfocada en arquitecturas en la nube.',
        'Se abordan conceptos para diseñar, desplegar y optimizar sistemas distribuidos, escalables y seguros.',
    ], idx=5, size=15)
    content_slide(prs, \"Resultados de aprendizaje (RAA)\", [
        '**RAA1** — Comprende y aplica modelos de servicio cloud (IaaS, PaaS, SaaS). Compara casos reales y elige el modelo adecuado según el problema.',
        '**RAA2** — Configura entornos virtualizados y despliega sistemas distribuidos. Usa virtualización/contenedores y despliegues alineados a microservicios cuando aplique.',
        '**RAA3** — Evalúa la seguridad, rendimiento y sostenibilidad de arquitecturas en la nube. Propone mejoras de costos, monitoreo y buenas prácticas de escalabilidad.',
    ], idx=6, size=15)
    """,
}


def patch(name, block):
    path = ROOT / name
    t = path.read_text(encoding="utf-8")
    t2 = re.sub(
        r"CREDS = \[\n    \"Ingeniero de Sistemas\",\n    \"Candidato a MsC en Inteligencia Artificial\",\n    \"[^\"]+\",\n\]\n",
        CREDS_NEW,
        t,
        count=1,
    )
    if t2 == t and "Speaker Tecnológico" not in t:
        raise SystemExit(f"{name}: CREDS pattern not found")
    t = t2
    start = t.find('content_slide(prs, "Objetivo y resultados de aprendizaje"')
    if start < 0:
        if "Objetivo de aprendizaje" in t:
            print(name, "already patched")
            path.write_text(t, encoding="utf-8", newline="\n")
            return
        raise SystemExit(f"{name}: objetivo marker missing")
    m = re.search(r'content_slide\(prs, "[^"]*trabajamos[^"]*"', t[start:])
    if not m:
        raise SystemExit(f"{name}: next slide missing")
    end = start + m.start()
    t = t[:start] + block + t[end:]
    m2 = re.search(r'content_slide\(prs, "[^"]*trabajamos[^"]*"', t)
    head, tail = t[: m2.start()], t[m2.start() :]
    tail = re.sub(
        r"(idx(?:_start)?=)(\d+)",
        lambda mm: f"{mm.group(1)}{int(mm.group(2)) + 1}",
        tail,
    )
    path.write_text(head + tail, encoding="utf-8", newline="\n")
    print("patched", name)


def main():
    for name, block in BLOCKS.items():
        patch(name, block)
    print("done")


if __name__ == "__main__":
    main()