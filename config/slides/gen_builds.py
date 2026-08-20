"""SCAFFOLDER LEGADO — genera desde cero los build_uniajc_*_curso.py.

⚠️  Los builds de Presentación del Curso YA se mantienen a mano (usan
`evaluacion_cortes_slide` / `contenido_clases_slide` y leen el calendario desde
`calendario_2026_2.py`). Correr este script los SOBREESCRIBE y se pierde ese
trabajo. Por eso exige `--force` explícito.

Fechas: NO se hardcodean aquí. El código generado lee
`config/calendario/semestre_2026_2.json` (13 sesiones en 2026-2).
"""
from pathlib import Path
import sys
import textwrap

slides = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\config\slides")
engine_import = """import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uniajc_slides_engine import (
    new_prs, course_cover, tutor_slide, padlet_slide, content_slide, table_content,
    box_note_slide, closing_slide,
)
import calendario_2026_2 as cal
"""

courses = [
  {
    "file": "build_uniajc_seminario_curso.py",
    "cal_key": 'seminario',
    "title": "Seminario de Sistemas",
    "subtitle": "Proyecto integrador de software",
    "out": "Seminario de Sistemas/Clases/Presentacion del Curso - Seminario de Sistemas.pptx",
    "meta": [
      "Codigo: **FI303301** · Grupo: **341C** · Periodo: **2026-2**",
      "Programa: Ingenieria de Sistemas · Facultad de Ingenieria · UNIAJC",
      "Horario: **Jueves 18:00 – 20:00** (120 min)",
      "Docente: Julian Andres Castano",
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
      "Modalidad: **presencialidad asistida**.",
      "Cada jueves (120 min): **Teoria Core** → **Taller / exposicion** → **Quiz corto** cuando aplique.",
      "Hilo conductor: **Proyecto Integrador** con avances y sustentacion final.",
      "Enfoque: ABPr · aprendizaje invertido (microcurriculo).",
    ],
    "crono": [
      ["S1", "27/08", "Presencial", "Acuerdo y conceptos iniciales"],
      ["S2", "03/09", "Virtual", "Ciclos de vida"],
      ["S3", "10/09", "Virtual", "Metodologias tradicionales"],
      ["S4", "17/09", "Virtual", "Metodologias agiles"],
      ["S5", "24/09", "Presencial", "Parcial 1 (solo evaluacion)"],
      ["S6", "01/10", "Virtual", "Requerimientos de software"],
      ["S7", "08/10", "Virtual", "Historias de usuario"],
      ["S8", "15/10", "Virtual", "Introduccion a UML + Casos de uso (sesion doble)"],
    ],
    "crono_note": "Sesiones 9–13: Parcial 2 (22/10) · sesion doble avance PI + UML avanzado (29/10) · diseno de interfaces (05/11) · preparacion de la sustentacion (12/11) · Parcial 3 + sustentacion (19/11). 13 sesiones cubren los 15 temas: 2 sesiones dobles. Ver CALENDARIO del curso.",
    "pi": [
      "Diseno, desarrollo y **sustentacion** de un proyecto de software orientado a objetos.",
      "Incluye documentacion tecnica, pruebas basicas y comunicacion clara de la solucion.",
      "Pesa **20%** en el tercer corte (ademas del Parcial 3).",
    ],
    "resources": [
      "Bibliografia (microcurriculo): GoF · Head First Design Patterns · Sommerville · Java Docs.",
      "Material: `Clases/Clase N` · `Guiones/` · `Kit docente/`.",
    ],
    "boxes": [
      ("info", "Horario fijo del grupo 341C: jueves 18:00–20:00."),
      ("aclaracion", "Entregas y avances del Proyecto Integrador segun calendario de cortes."),
      ("advertencia", "Asistencia con peso en cada corte."),
    ],
    "close": ["Seminario de Sistemas · Grupo **341C** · 2026-2", "Jueves **18:00 – 20:00**", "UNIAJC · Ingenieria de Sistemas"],
    "accent": "Proyecto + documentacion + sustentacion",
  },
  {
    "file": "build_uniajc_bd2_curso.py",
    "cal_key": 'bases_datos_ii',
    "title": "Bases de Datos II",
    "subtitle": "Gestion avanzada y optimizacion",
    "out": "Bases de Datos II/Clases/Presentacion del Curso - Bases de Datos II.pptx",
    "meta": [
      "Codigo: **FI303215** · Grupo: **641A-2** · Periodo: **2026-2**",
      "Programa: Ingenieria de Sistemas · Facultad de Ingenieria · UNIAJC",
      "Horario: **Lunes 18:00 – 20:00** (120 min) · Modalidad: **Virtual**",
      "Docente: Julian Andres Castano",
      "Meet / enlace de clase: **[URL Meet — pendiente]**",
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
      ["S1", "24/08", "Presencial", "Presentacion · Revision BD I"],
      ["S2", "31/08", "Virtual", "Administracion de BD"],
      ["S3", "07/09", "Virtual", "Procedimientos almacenados"],
      ["S4", "14/09", "Virtual", "Funciones y disparadores · Seguridad y respaldo"],
      ["S5", "21/09", "Presencial", "Parcial 1 (solo evaluacion)"],
      ["S6", "28/09", "Virtual", "Optimizacion de consultas"],
      ["S7", "05/10", "Virtual", "Indices y particionamiento + Tuning y transacciones (sesion doble)"],
      ["S8", "12/10", "Autonoma", "Control de concurrencia (festivo)"],
    ],
    "crono_note": "Sesiones 9–13: Parcial 2 (19/10) · sesion doble avance PI + integracion y preparacion final (26/10) · casos reales (02/11, autonoma) · Parcial 3 (09/11) · sustentacion del PI (16/11). 13 sesiones cubren los 15 temas: 2 sesiones dobles. Ver CALENDARIO del curso.",
    "pi": [
      "Sistema avanzado de BD para gestion segura y optimizada de informacion empresarial (ABPr).",
      "Incluye administracion, automatizacion (procedimientos/triggers) y tuning.",
      "Pesa **20%** en el tercer corte.",
    ],
    "resources": [
      "Practica en la nube (free tier / browser) — sin instalacion de pago obligatoria.",
      "Bibliografia: Coronel & Morris · Date · Oracle PL/SQL Docs.",
      "Plan propio: `Plan curso/PLAN_DE_CURSO_2026-2.md`.",
    ],
    "boxes": [
      ("info", "Lunes 18:00–20:00 · Virtual · Grupo 641A-2."),
      ("aclaracion", "Clases en festivo (12/10, 02/11) = autonomas con actividad en ExamLab; el 16/11 (festivo) se usa para las sustentaciones del PI."),
      ("advertencia", "Parciales SIEMPRE presenciales y nunca en autonoma: sesiones 5 (21/09), 9 (19/10) y 12 (09/11)."),
    ],
    "close": ["Bases de Datos II · Grupo **641A-2** · 2026-2", "Lunes **18:00 – 20:00** · Virtual", "UNIAJC · Ingenieria de Sistemas"],
    "accent": "Datos seguros, consultas rapidas, proyecto real",
  },
  {
    "file": "build_uniajc_arq_curso.py",
    "cal_key": 'arquitectura',
    "title": "Arquitectura de Sistemas Computacionales",
    "subtitle": "Enfoque Cloud",
    "out": "Arquitectura de Sistemas Computacionales/Clases/Presentacion del Curso - Arquitectura de Sistemas Computacionales.pptx",
    "meta": [
      "Codigo: **FI303380** · Grupo: **6303C** · Periodo: **2026-2**",
      "Programa: Ingenieria de Sistemas · Facultad de Ingenieria · UNIAJC",
      "Horario: **Lunes 10:00 – 12:00** (120 min)",
      "Modalidad: **Virtual** (todas las sesiones virtual síncrona por Meet · festivos = clase autónoma)",
      "Docente: Julian Andres Castano",
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
      "Bloque de **120 min** (lunes 10:00–12:00).",
      "Estructura: **Teoria Core** → **Taller / laboratorio cloud (free tier)** → **Quiz / avance PI**.",
      "Practica con herramientas **gratis + en la nube** (AWS/Azure/GCP free tier o simuladores).",
      "Hilo conductor: **Proyecto Integrador** — arquitectura cloud para una aplicacion.",
      "Festivos del lunes = **clase autonoma** (no se omiten).",
    ],
    "crono": [
      ["S1", "24/08", "Presencial", "Presentacion · Intro arquitecturas cloud"],
      ["S2", "31/08", "Virtual", "IaaS / PaaS / SaaS"],
      ["S3", "07/09", "Virtual", "Virtualizacion y contenedores"],
      ["S4", "14/09", "Virtual", "Microservicios y arquitecturas distribuidas"],
      ["S5", "21/09", "Presencial", "Parcial 1 (solo evaluacion)"],
      ["S6", "28/09", "Virtual", "Seguridad en la nube"],
      ["S7", "05/10", "Virtual", "Redes y almacenamiento + Monitoreo y CI/CD (sesion doble)"],
      ["S8", "12/10", "Autonoma", "Costos y sostenibilidad cloud (festivo)"],
    ],
    "crono_note": "Sesiones 9–13: Parcial 2 (19/10) · sesion doble avance PI + pruebas de rendimiento (26/10) · autoescalado (02/11, autonoma) · Parcial 3 (09/11) · sustentacion del PI (16/11). 13 sesiones cubren los 15 temas: 2 sesiones dobles. Ver CALENDARIO del curso.",
    "pi": [
      "Diseno y simulacion de una **arquitectura cloud** para una aplicacion web o empresarial.",
      "Aplica escalabilidad, seguridad y sostenibilidad.",
      "Pesa **20%** en el tercer corte; cierre con sustentacion.",
    ],
    "resources": [
      "Cloud free tier / simuladores (sin software de pago obligatorio en el PC).",
      "Bibliografia: Erl · Buyya · Hwang · docs AWS/Azure/GCP.",
      "Plan propio: `Plan curso/PLAN_DE_CURSO_2026-2.md`.",
    ],
    "boxes": [
      ("info", "Lunes 10:00–12:00 (120 min) · Grupo 6303C · Virtual (todas las sesiones por Meet)."),
      ("aclaracion", "Clases en festivo (12/10, 02/11) = autonomas con actividad en ExamLab; el 16/11 (festivo) se usa para las sustentaciones del PI CloudLite."),
      ("advertencia", "Parciales SIEMPRE presenciales y nunca en autonoma: sesiones 5 (21/09), 9 (19/10) y 12 (09/11)."),
    ],
    "close": ["Arquitectura de Sistemas Computacionales · **FI303380** · 2026-2", "Lunes **10:00 – 12:00**", "UNIAJC · Ingenieria de Sistemas"],
    "accent": "Cloud con criterio: escalable, seguro y sostenible",
  },
]

def py_list(items):
    return "[\n" + ",\n".join("        " + repr(x) for x in items) + ",\n    ]"

def py_rows(rows):
    return "[\n" + ",\n".join("            " + repr(r) for r in rows) + ",\n        ]"

def py_boxes(boxes):
    return "[\n" + ",\n".join("            " + repr(b) for b in boxes) + ",\n        ]"

if "--force" not in sys.argv:
    raise SystemExit(
        "gen_builds.py sobreescribiria los build_uniajc_*_curso.py mantenidos a mano. "
        "Si de verdad quieres regenerarlos desde cero, corre: python gen_builds.py --force"
    )

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
    _ct = cal.cortes({c['cal_key']!r})
    _resto = [
        "Talleres o Quiz 10% · Asistencia 10%",
        "Talleres o Quiz 10% · Asistencia 10%",
        "Proyecto Integrador 20% · Asistencia 5%",
    ]
    _peso_parcial = ["10%", "10%", "15%"]
    table_content(
        prs, "Sistema de evaluación (Acuerdo pedagógico)",
        ["Corte", "Ventana", "Desglose", "%"],
        [
            [str(x["corte"]), x["ventana"],
             f"Parcial {{x['parcial_n']}} (sesión {{x['parcial_sesion']}} · {{x['parcial_fecha']}}) "
             f"{{_peso_parcial[i]}} · {{_resto[i]}}",
             x["pct"]]
            for i, x in enumerate(_ct)
        ],
        note="Lógica Acuerdos 2026-2 (13 sesiones · 15 temas · 2 sesiones dobles). Parcial al cierre de cada corte.",
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
