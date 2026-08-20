# -*- coding: utf-8 -*-
"""Presentación del Curso (= Sesión 0) — Arquitectura de Sistemas Computacionales
UNIAJC · FI303380 · grupo 6303C · 2026-2 · lun 10:00–12:00.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uniajc_slides_engine import (
    new_prs,
    course_cover,
    tutor_slide,
    padlet_slide,
    content_slide,
    table_content,
    evaluacion_cortes_slide,
    contenido_clases_slide,
    herramientas_slide,
    closing_slide,
)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(
    ROOT,
    "Arquitectura de Sistemas Computacionales",
    "Clases",
    "Presentacion del Curso - Arquitectura de Sistemas Computacionales.pptx",
)

DOCENTE = "Julian Andres Castaño"
CORREO = "julianacastano@profesores.uniajc.edu.co"
CREDS = [
    "Ingeniero de Sistemas",
    "Candidato a MsC en Inteligencia Artificial",
    "Líder Técnico · Speaker Tecnológico",
]

import calendario_2026_2 as cal

CURSO_KEY = "arquitectura"

# Temas del material ya construido (carpetas «Clase N», que NO se renumeran).
# El calendario 2026-2 (13 sesiones) decide en qué sesión se dicta cada uno; dos
# sesiones son dobles y la sesión 13 (16/11) es de sustentaciones del PI.
TEMAS_MATERIAL = {
    1: "Diagnóstico · Introducción a arquitecturas cloud",
    2: "Modelos de servicio IaaS / PaaS / SaaS",
    3: "Virtualización y contenedores",
    4: "Microservicios y arquitecturas distribuidas",
    5: "Repaso y evaluación del corte 1",
    6: "Seguridad en la nube",
    7: "Redes y almacenamiento cloud",
    8: "Monitoreo, optimización y CI/CD",
    9: "Repaso y evaluación del corte 2",
    10: "Costos y sostenibilidad cloud",
    11: "Avance del proyecto final (CloudLite)",
    12: "Pruebas de rendimiento y preparación final",
    13: "Escalabilidad automática",
    14: "Repaso y evaluación del corte 3",
    15: "Presentación del proyecto y cierre",
}

# CONTENIDO: Sesión 0 + las 13 sesiones reales (lunes · parciales 5/9/12 ·
# festivos autónomas · sesión 13 = sustentaciones del PI CloudLite).
CT = cal.cortes(CURSO_KEY)

CONTENIDO = cal.contenido_items(
    CURSO_KEY, TEMAS_MATERIAL,
    "Presentación del curso: logística, evaluación y socialización del PI CloudLite",
)


def build():
    prs = new_prs()

    course_cover(
        prs,
        "Arquitectura de Sistemas Computacionales",
        "Enfoque cloud · Proyecto Integrador CloudLite",
        [
            "Código: **FI303380** · Grupo: **6303C** · Periodo: **2026-2**",
            "Programa: Ingeniería de Sistemas · Facultad de Ingeniería · UNIAJC",
            "Horario: **Lunes 10:00 – 12:00** (120 min)",
            "Modalidad: **Virtual**",
            "Docente: Julian Andres Castaño",
        ],
        inicio_clase="10:10",
    )

    tutor_slide(prs, DOCENTE, CREDS, CORREO, idx=2)
    padlet_slide(prs, idx=3)

    content_slide(
        prs,
        "¿Para qué existe este curso?",
        [
            "Comprender y aplicar modelos de **infraestructura moderna** con enfoque en arquitecturas en la nube.",
            "Diseñar, desplegar y optimizar sistemas distribuidos, escalables y seguros.",
            "Práctica al servicio del **Proyecto Integrador CloudLite** (diagramas, labs gratis, CI/CD conceptual).",
            "@@Objeto de estudio:@@ diseño, implementación y gestión de arquitecturas en entornos cloud.",
        ],
        idx=4,
    )

    content_slide(
        prs,
        "Objetivo y resultados de aprendizaje",
        [
            "**Objetivo:** diseñar e implementar arquitecturas con cloud, virtualización y escalabilidad.",
            "**RAA1** — Comprende y aplica modelos de servicio cloud (IaaS, PaaS, SaaS).",
            "**RAA2** — Configura entornos virtualizados y despliega sistemas distribuidos.",
            "**RAA3** — Evalúa seguridad, rendimiento y sostenibilidad de arquitecturas en la nube.",
        ],
        idx=5,
    )

    content_slide(
        prs,
        "Cómo trabajamos en clase",
        [
            "**Sesión 0 (hoy)** = encuadre del curso + evaluación + **socialización del Proyecto Integrador CloudLite** + herramientas.",
            "**Clase 1** = diagnóstico + arranque del primer tema (introducción a arquitecturas cloud) — mismo bloque de hoy.",
            "De la sesión 2 en adelante, cada sesión sigue la misma estructura: **Teoría Core breve** → **Taller PI CloudLite** → **cierre**. Modalidad: sesión 1 y parciales (**5 / 9 / 12**) **presencial**; resto **virtual síncrona**; festivos = **clase autónoma**. Dos sesiones son **dobles** (dos temas en un bloque) y la **sesión 13 (16/11)** es de **sustentaciones**.",
            "Herramientas **gratis + navegador** (sin cloud de pago ni Docker Desktop). Talleres y quices/parciales se entregan/presentan en @@ExamLab@@ (https://examlab.lovable.app/) — no es la plataforma oficial de la UNIAJC, la usamos solo para esto.",
            "Hilo conductor de todo el semestre: **Proyecto Integrador CloudLite**.",
        ],
        idx=6,
    )

    evaluacion_cortes_slide(
        prs,
        "Sistema de evaluación (Acuerdo pedagógico)",
        [
            {"corte": 1, "pct": CT[0]["pct"], "ventana": CT[0]["ventana"],
             "desglose": [f"**Parcial 1** ({CT[0]['parcial_fecha']} · sesión {CT[0]['parcial_sesion']}) · 10%",
                          "Talleres o Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 2, "pct": CT[1]["pct"], "ventana": CT[1]["ventana"],
             "desglose": [f"**Parcial 2** ({CT[1]['parcial_fecha']} · sesión {CT[1]['parcial_sesion']}) · 10%",
                          "Talleres o Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 3, "pct": CT[2]["pct"], "ventana": CT[2]["ventana"],
             "desglose": [f"**Parcial 3** ({CT[2]['parcial_fecha']} · sesión {CT[2]['parcial_sesion']}) · 15%",
                          "**PI CloudLite** · 20%", "Asistencia · 5%"]},
        ],
        note="Parciales síncronos presenciales · nunca en festivo/autónoma. Día de parcial = solo evaluación.",
        idx=7,
    )

    contenido_clases_slide(
        prs,
        CONTENIDO,
        title="CONTENIDO",
        sub=("Sesión 0 + 13 sesiones · grupo 6303C · lunes 10:00–12:00 · los 15 temas se "
             "conservan: dos sesiones son **dobles** y la sesión 13 es de **sustentaciones**"),
        idx=8,
        size=12,
    )

    content_slide(
        prs,
        "Proyecto Integrador · CloudLite",
        [
            "@@Socialización de hoy (Sesión 0):@@ presentamos el PI completo para que lo tengan claro desde la Clase 1.",
            "Diseño y simulación de una **arquitectura cloud** para una aplicación web/API (CloudLite App).",
            "Entregables: diagramas C4/despliegue · lab contenedores (navegador) · CI/CD conceptual · informe + sustentación.",
            "Pesa **20%** en el tercer corte; se construye por avances a lo largo del semestre.",
            "Hilo conductor de cada clase regular/autónoma (teoría al servicio del entregable).",
        ],
        idx=9,
    )

    herramientas_slide(
        prs,
        [
            {"name": "draw.io", "logo": "drawio.png", "note": "C4 · despliegue"},
            {"name": "Excalidraw", "logo": "excalidraw.png", "note": "Bocetos de taller"},
            {"name": "LabEx Docker Playground", "logo": None, "note": "Lab contenedores"},
            {"name": "GitHub Actions", "logo": "github.png", "note": "CI/CD conceptual"},
            {"name": "ExamLab", "logo": "examlab.png", "note": "Talleres + quices/parciales"},
        ],
        title="Herramientas del curso",
        sub="Gratis · navegador / free tier · Floci en evaluación (piloto opcional)",
        idx=10,
    )

    closing_slide(
        prs,
        "¡Empezamos!",
        [
            "Arquitectura de Sistemas Computacionales · **FI303380** · Grupo **6303C**",
            "Lunes **10:00 – 12:00** · Periodo **2026-2**",
            "UNIAJC · Ingeniería de Sistemas",
        ],
        accent="CloudLite con criterio: escalable, seguro y sostenible",
    )

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    prs.save(OUT)
    print("OK ->", OUT)
    return OUT


if __name__ == "__main__":
    build()
