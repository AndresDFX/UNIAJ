from pathlib import Path
import textwrap

slides = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\config\slides")
engine_import = """import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uniajc_slides_engine import (
    new_prs, course_cover, tutor_slide, padlet_slide, content_slide, table_content,
    box_note_slide, closing_slide,
)
"""

courses = [
  {
    "file": "build_uniajc_seminario_curso.py",
    "title": "Seminario de Sistemas",
    "subtitle": "Proyecto integrador de software",
    "out": "Seminario de Sistemas/Clases/Presentacion del Curso - Seminario de Sistemas.pptx",
    "meta": [
      "Codigo: **FI303301** · Grupo: **341C** · Periodo: **2026-2**",
      "Programa: Ingenieria de Sistemas · Facultad de Ingenieria · UNIAJC",
      "Horario: **Jueves 18:00 – 20:00** (120 min)",
      "Docente: Julian Andres Castano",
      "Campus Virtual: **[URL Campus Virtual UNIAJC — pendiente]**",
      "Listado de estudiantes: **[PENDIENTE listado]**",
    ],
    "purpose": [
      "Consolidar conocimientos de Programacion II mediante **analisis, diseno, desarrollo y exposicion** de proyectos integradores.",
      "Fortalecer patrones, documentacion tecnica, pruebas y comunicacion efectiva.",
      "@@Objeto de estudio:@@ integracion de conocimientos para proyectos de software OO.",
    ],
    "raa": [
      "**Objetivo:** desarrollar un proyecto de software con POO avanzada, documentacion, validacion y sustentacion.",
      "**RAA1** — Aplica patrones de diseno y principios de modularidad.",
      "**RAA2** — Documenta y valida aplicaciones mediante pruebas basicas.",
      "**RAA3** — Presenta y sustenta proyectos de forma clara y estructurada.",
    ],
    "how": [
      "Modalidad: **presencialidad asistida** (confirmar virtuales del mes en Campus Virtual).",
      "Cada jueves (120 min): **Teoria Core** → **Taller / exposicion** → **Quiz corto** cuando aplique.",
      "Hilo conductor: **Proyecto Integrador** con avances y sustentacion final.",
      "Enfoque: ABPr · aprendizaje invertido (microcurriculo).",
    ],
    "crono": [
      ["1", "13/08", "Regular", "Acuerdo y conceptos"],
      ["2", "20/08", "Regular", "Ciclos de vida"],
      ["3", "27/08", "Regular", "Metodologias tradicionales"],
      ["4", "03/09", "Regular", "Metodologias agiles"],
      ["5", "10/09", "Regular", "Caso estudio evaluativo · Parcial 1"],
      ["6", "17/09", "Regular", "Requerimientos de software"],
      ["7", "24/09", "Regular", "Historias de usuario"],
      ["8", "01/10", "Regular", "Introduccion a UML"],
    ],
    "crono_note": "Clases 9–15: casos de uso, caso evaluativo (Parcial 2), avance PI, UML avanzado, interfaces, evaluacion y sustentacion (Parcial 3). Ver PLAN_DE_CURSO_2026-2.md.",
    "pi": [
      "Diseno, desarrollo y **sustentacion** de un proyecto de software orientado a objetos.",
      "Incluye documentacion tecnica, pruebas basicas y comunicacion clara de la solucion.",
      "Pesa **20%** en el tercer corte (ademas del Parcial 3).",
    ],
    "resources": [
      "Campus Virtual UNIAJC: **[URL Campus Virtual UNIAJC — pendiente]**",
      "Bibliografia (microcurriculo): GoF · Head First Design Patterns · Sommerville · Java Docs.",
      "Material: `Clases/Clase N` · `Guiones/` · `Kit docente/`.",
    ],
    "boxes": [
      ("info", "Horario fijo del grupo 341C: jueves 18:00–20:00."),
      ("aclaracion", "Entregas y avances del Proyecto Integrador segun calendario de cortes."),
      ("advertencia", "Asistencia con peso en cada corte. Listado: [PENDIENTE listado]."),
    ],
    "close": ["Seminario de Sistemas · Grupo **341C** · 2026-2", "Jueves **18:00 – 20:00**", "UNIAJC · Ingenieria de Sistemas"],
    "accent": "Proyecto + documentacion + sustentacion",
  },
  {
    "file": "build_uniajc_bd2_curso.py",
    "title": "Bases de Datos II",
    "subtitle": "Gestion avanzada y optimizacion",
    "out": "Bases de Datos II/Clases/Presentacion del Curso - Bases de Datos II.pptx",
    "meta": [
      "Codigo: **FI303215** · Grupo: **641A-2** · Periodo: **2026-2**",
      "Programa: Ingenieria de Sistemas · Facultad de Ingenieria · UNIAJC",
      "Horario: **Lunes 18:00 – 20:00** (120 min) · Modalidad: **Virtual**",
      "Docente: Julian Andres Castano",
      "Campus Virtual: **[URL Campus Virtual UNIAJC — pendiente]**",
      "Meet / enlace de clase: **[URL Meet — pendiente]**",
      "Listado de estudiantes: **[PENDIENTE listado]**",
    ],
    "purpose": [
      "Profundizar la **gestion avanzada** de bases de datos: optimizacion, seguridad, procedimientos y administracion.",
      "Disenar soluciones de alto rendimiento con integridad, disponibilidad y proteccion de datos.",
      "Consolida habilidades para Arquitectura de Sistemas y Seguridad.",
      "@@Objeto de estudio:@@ gestion avanzada y optimizacion de BD relacionales.",
    ],
    "raa": [
      "**Objetivo:** disenar, administrar y optimizar BD relacionales avanzadas con seguridad e integridad.",
      "**RAA1** — Administra BD aplicando seguridad y respaldo.",
      "**RAA2** — Implementa procedimientos almacenados y disparadores.",
      "**RAA3** — Optimiza consultas y estructuras para mejorar el rendimiento.",
    ],
    "how": [
      "Modalidad: **virtual** (grupo 641A-2).",
      "Cada lunes (120 min): **Teoria Core** → **Taller / laboratorio en la nube** → **Quiz corto**.",
      "Herramientas de practica: **gratis + en la nube** (sin software de pago obligatorio).",
      "Hilo conductor: **Proyecto Integrador** de sistema avanzado de BD.",
      "Festivos del lunes = **clase autonoma** (no se omiten).",
    ],
    "crono": [
      ["1", "10/08", "Regular", "Presentacion · Revision BD I"],
      ["2", "17/08", "Autonoma", "Administracion de BD (festivo)"],
      ["3", "24/08", "Regular", "Procedimientos almacenados"],
      ["4", "31/08", "Regular", "Funciones y disparadores"],
      ["5", "07/09", "Regular", "Seguridad y respaldo · Parcial 1"],
      ["6", "14/09", "Regular", "Optimizacion de consultas"],
      ["7", "21/09", "Regular", "Indices y particionamiento"],
      ["8", "28/09", "Regular", "Tuning de bases de datos"],
    ],
    "crono_note": "Clases 9–15: transacciones, concurrencia (Parcial 2 · 12/10 autonoma), avance PI, integracion, casos, prep. y cierre (Parcial 3 · 16/11 autonoma). Ver PLAN_DE_CURSO_2026-2.md.",
    "pi": [
      "Sistema avanzado de BD para gestion segura y optimizada de informacion empresarial (ABPr).",
      "Incluye administracion, automatizacion (procedimientos/triggers) y tuning.",
      "Pesa **20%** en el tercer corte.",
    ],
    "resources": [
      "Campus Virtual UNIAJC: **[URL Campus Virtual UNIAJC — pendiente]**",
      "Practica en la nube (free tier / browser) — sin instalacion de pago obligatoria.",
      "Bibliografia: Coronel & Morris · Date · Oracle PL/SQL Docs.",
      "Plan propio: `Plan curso/PLAN_DE_CURSO_2026-2.md`.",
    ],
    "boxes": [
      ("info", "Lunes 18:00–20:00 · Virtual · Grupo 641A-2."),
      ("aclaracion", "Clases en festivo (17/08, 12/10, 02/11, 16/11) = autonomas con actividad en Campus Virtual."),
      ("advertencia", "Parciales 2 y 3 caen en clase autonoma: entrega asincrona. Listado: [PENDIENTE listado]."),
    ],
    "close": ["Bases de Datos II · Grupo **641A-2** · 2026-2", "Lunes **18:00 – 20:00** · Virtual", "UNIAJC · Ingenieria de Sistemas"],
    "accent": "Datos seguros, consultas rapidas, proyecto real",
  },
  {
    "file": "build_uniajc_arq_curso.py",
    "title": "Arquitectura de Sistemas Computacionales",
    "subtitle": "Enfoque Cloud",
    "out": "Arquitectura de Sistemas Computacionales/Clases/Presentacion del Curso - Arquitectura de Sistemas Computacionales.pptx",
    "meta": [
      "Codigo: **FI303380** · Grupo: **[PENDIENTE — grupo]** · Periodo: **2026-2**",
      "Programa: Ingenieria de Sistemas · Facultad de Ingenieria · UNIAJC",
      "Horario: **Lunes 10:00 – 13:00** (180 min)",
      "Modalidad: **[PENDIENTE — modalidad]**",
      "Docente: Julian Andres Castano",
      "Campus Virtual: **[URL Campus Virtual UNIAJC — pendiente]**",
      "Listado de estudiantes: **[PENDIENTE listado]**",
    ],
    "purpose": [
      "Comprender y aplicar modelos de **infraestructura moderna** con enfoque en arquitecturas en la nube.",
      "Disenar, desplegar y optimizar sistemas distribuidos, escalables y seguros.",
      "@@Objeto de estudio:@@ diseno, implementacion y gestion de arquitecturas en entornos cloud.",
    ],
    "raa": [
      "**Objetivo:** disenar e implementar arquitecturas con cloud, virtualizacion y escalabilidad.",
      "**RAA1** — Comprende y aplica modelos de servicio cloud (IaaS, PaaS, SaaS).",
      "**RAA2** — Configura entornos virtualizados y despliega sistemas distribuidos.",
      "**RAA3** — Evalua seguridad, rendimiento y sostenibilidad de arquitecturas en la nube.",
    ],
    "how": [
      "Bloque de **180 min** (lunes 10:00–13:00).",
      "Estructura: **Teoria Core** → **Taller / laboratorio cloud (free tier)** → **Quiz / avance PI**.",
      "Practica con herramientas **gratis + en la nube** (AWS/Azure/GCP free tier o simuladores).",
      "Hilo conductor: **Proyecto Integrador** — arquitectura cloud para una aplicacion.",
      "Festivos del lunes = **clase autonoma** (no se omiten).",
    ],
    "crono": [
      ["1", "10/08", "Regular", "Presentacion · Intro arquitecturas cloud"],
      ["2", "17/08", "Autonoma", "IaaS / PaaS / SaaS (festivo)"],
      ["3", "24/08", "Regular", "Virtualizacion y contenedores"],
      ["4", "31/08", "Regular", "Microservicios"],
      ["5", "07/09", "Regular", "Arquitecturas distribuidas · Parcial 1"],
      ["6", "14/09", "Regular", "Seguridad en la nube"],
      ["7", "21/09", "Regular", "Redes y almacenamiento cloud"],
      ["8", "28/09", "Regular", "Monitoreo y optimizacion"],
    ],
    "crono_note": "Clases 9–15: CI/CD, costos/sostenibilidad (Parcial 2 · 12/10), avance PI, rendimiento, autoescalado, prep. y cierre (Parcial 3 · 16/11). Ver PLAN_DE_CURSO_2026-2.md.",
    "pi": [
      "Diseno y simulacion de una **arquitectura cloud** para una aplicacion web o empresarial.",
      "Aplica escalabilidad, seguridad y sostenibilidad.",
      "Pesa **20%** en el tercer corte; cierre con sustentacion.",
    ],
    "resources": [
      "Campus Virtual UNIAJC: **[URL Campus Virtual UNIAJC — pendiente]**",
      "Cloud free tier / simuladores (sin software de pago obligatorio en el PC).",
      "Bibliografia: Erl · Buyya · Hwang · docs AWS/Azure/GCP.",
      "Plan propio: `Plan curso/PLAN_DE_CURSO_2026-2.md`.",
    ],
    "boxes": [
      ("info", "Lunes 10:00–13:00 (180 min). Grupo y modalidad: [PENDIENTE]."),
      ("aclaracion", "Clases en festivo = autonomas con actividad en Campus Virtual."),
      ("advertencia", "Parciales 2 y 3 en clase autonoma. Listado: [PENDIENTE listado]."),
    ],
    "close": ["Arquitectura de Sistemas Computacionales · **FI303380** · 2026-2", "Lunes **10:00 – 13:00**", "UNIAJC · Ingenieria de Sistemas"],
    "accent": "Cloud con criterio: escalable, seguro y sostenible",
  },
]

def py_list(items):
    return "[\n" + ",\n".join("        " + repr(x) for x in items) + ",\n    ]"

def py_rows(rows):
    return "[\n" + ",\n".join("            " + repr(r) for r in rows) + ",\n        ]"

def py_boxes(boxes):
    return "[\n" + ",\n".join("            " + repr(b) for b in boxes) + ",\n        ]"

for c in courses:
    # Fix accents for Spanish display in PPTX
    repl = {
        "Codigo": "Código", "Ingenieria": "Ingeniería", "Castano": "Castaño",
        "analisis": "análisis", "diseno": "diseño", "Diseno": "Diseño", "documentacion": "documentación",
        "tecnica": "técnica", "comunicacion": "comunicación", "integracion": "integración",
        "validacion": "validación", "sustentacion": "sustentación", "diseno": "diseño",
        "Teoria": "Teoría", "exposicion": "exposición", "microcurriculo": "microcurrículo",
        "ademas": "además", "Bibliografia": "Bibliografía", "segun": "según",
        "Gestion": "Gestión", "optimizacion": "optimización", "administracion": "administración",
        "Disenar": "Diseñar", "proteccion": "protección", "disenar": "diseñar",
        "practica": "práctica", "Practica": "Práctica", "autonoma": "autónoma", "autonomas": "autónomas",
        "asincrona": "asíncrona", "Presentacion": "Presentación", "Revision": "Revisión",
        "Autonoma": "Autónoma", "Indices": "Índices", "informacion": "información",
        "instalacion": "instalación", "Evalua": "Evalúa", "virtualizacion": "virtualización",
        "aplicacion": "aplicación", "simulacion": "simulación",
        "Metodologias": "Metodologías", "agiles": "ágiles", "Introduccion": "Introducción",
        "evaluacion": "evaluación",
    }
    def fix(s):
        if isinstance(s, tuple):
            return tuple(fix(x) for x in s)
        if isinstance(s, list):
            return [fix(x) for x in s]
        if isinstance(s, str):
            for a,b in repl.items():
                s = s.replace(a,b)
            return s
        return s
    for k in list(c.keys()):
        c[k] = fix(c[k])

    body = f'''# -*- coding: utf-8 -*-
"""Presentacion del Curso — {c['title']} (UNIAJC · 2026-2)."""
{engine_import}
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, *{repr(c["out"].split("/"))})

DOCENTE = "Julian Andres Castaño"
CORREO = "julianacastano@profesores.uniajc.edu.co"
CREDS = [
    "Ingeniero de Sistemas",
    "Candidato a MsC en Inteligencia Artificial",
    "Líder Técnico",
]


def build():
    prs = new_prs()
    course_cover(prs, {repr(c["title"])}, {repr(c["subtitle"])}, {py_list(c["meta"])})
    tutor_slide(prs, DOCENTE, CREDS, CORREO, idx=2)
    padlet_slide(prs, idx=3)
    content_slide(prs, "¿Para qué existe este curso?", {py_list(c["purpose"])}, idx=4)
    content_slide(prs, "Objetivo y resultados de aprendizaje", {py_list(c["raa"])}, idx=5)
    content_slide(prs, "Cómo trabajamos en clase", {py_list(c["how"])}, idx=6)
    table_content(
        prs, "Sistema de evaluación (Acuerdo pedagógico)",
        ["Corte", "Ventana", "Desglose", "%"],
        [
            ["1", "10/08 – 13/09/2026", "Parcial 1 (Clase 5) 10% · Talleres o Quiz 10% · Asistencia 10%", "30%"],
            ["2", "14/09 – 18/10/2026", "Parcial 2 (Clase 10) 10% · Talleres o Quiz 10% · Asistencia 10%", "30%"],
            ["3", "19/10 – 22/11/2026", "Parcial 3 (Clase 15) 15% · Proyecto Integrador 20% · Asistencia 5%", "40%"],
        ],
        note="Lógica Acuerdos 2026-2. Parcial al cierre de cada corte. Listado: [PENDIENTE listado].",
        col_w=[1.2, 2.4, 6.5, 1.2],
        idx=7,
    )
    table_content(
        prs, "Cronograma de clases (Plan de curso 2026-2)",
        ["#", "Fecha", "Tipo", "Tema"],
        {py_rows(c["crono"])},
        note={repr(c["crono_note"])},
        col_w=[0.7, 1.3, 1.5, 7.8],
        fs_body=11,
        idx=8,
    )
    content_slide(prs, "Proyecto Integrador", {py_list(c["pi"])}, idx=9)
    content_slide(prs, "Recursos", {py_list(c["resources"])}, idx=10)
    box_note_slide(prs, "Acuerdos importantes", {py_boxes(c["boxes"])}, idx=11)
    closing_slide(prs, "¡Empezamos!", {py_list(c["close"])}, accent={repr(c["accent"])})
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    prs.save(OUT)
    print("OK ->", OUT)


if __name__ == "__main__":
    build()
'''
    # Fix docstring accents
    body = body.replace('Presentacion del Curso', 'Presentación del Curso')
    path = slides / c["file"]
    path.write_text(body, encoding="utf-8")
    print("WROTE", path)
print("DONE")
