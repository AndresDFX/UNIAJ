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

# CONTENIDO: Sesión 0 + Clases 1–15 (lunes · parciales 5/9/14 · festivos autónomas)
CONTENIDO = [
    {"n": 0, "kind": "sesion0", "tema": "Presentación del curso: logística, evaluación y socialización del PI CloudLite", "fecha": "10/08"},
    {"n": 1, "tema": "Diagnóstico · Introducción a arquitecturas cloud", "fecha": "10/08"},
    {"n": 2, "tema": "Modelos de servicio IaaS / PaaS / SaaS", "fecha": "17/08", "tag": "Autónoma"},
    {"n": 3, "tema": "Virtualización y contenedores", "fecha": "24/08"},
    {"n": 4, "tema": "Microservicios y arquitecturas distribuidas", "fecha": "31/08"},
    {"n": 5, "tema": "Parcial 1", "fecha": "07/09", "tag": "Parcial 1 · presencial"},
    {"n": 6, "tema": "Seguridad en la nube", "fecha": "14/09"},
    {"n": 7, "tema": "Redes y almacenamiento cloud", "fecha": "21/09"},
    {"n": 8, "tema": "Monitoreo, optimización y CI/CD", "fecha": "28/09"},
    {"n": 9, "tema": "Parcial 2", "fecha": "05/10", "tag": "Parcial 2 · presencial"},
    {"n": 10, "tema": "Costos y sostenibilidad cloud", "fecha": "12/10", "tag": "Autónoma"},
    {"n": 11, "tema": "Avance del proyecto final (CloudLite)", "fecha": "19/10"},
    {"n": 12, "tema": "Pruebas de rendimiento y preparación final", "fecha": "26/10"},
    {"n": 13, "tema": "Escalabilidad automática", "fecha": "02/11", "tag": "Autónoma"},
    {"n": 14, "tema": "Parcial 3", "fecha": "09/11", "tag": "Parcial 3 · presencial"},
    {"n": 15, "tema": "Presentación del proyecto y cierre", "fecha": "16/11", "tag": "Autónoma"},
]


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
            "Modalidad: **Presencialidad asistida**",
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
            "De la Clase 2 en adelante, cada sesión sigue la misma estructura: **Teoría Core breve** → **Taller PI CloudLite** → **cierre**. Modalidad: Clase 1 y parciales (**5 / 9 / 14**) **presencial**; resto **virtual síncrona**; festivos = **clase autónoma**.",
            "Herramientas **gratis + navegador** (sin cloud de pago ni Docker Desktop). Talleres y quices/parciales se entregan/presentan en @@ExamLab@@ (no es la plataforma oficial de la UNIAJC, la usamos solo para esto).",
            "Hilo conductor de todo el semestre: **Proyecto Integrador CloudLite**.",
        ],
        idx=6,
    )

    evaluacion_cortes_slide(
        prs,
        "Sistema de evaluación (Acuerdo pedagógico)",
        [
            {"corte": 1, "pct": "30%", "ventana": "10/08 – 13/09/2026",
             "desglose": ["**Parcial 1** (Clase 5) · 10%", "Talleres / Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 2, "pct": "30%", "ventana": "14/09 – 18/10/2026",
             "desglose": ["**Parcial 2** (Clase 9) · 10%", "Talleres / Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 3, "pct": "40%", "ventana": "19/10 – 22/11/2026",
             "desglose": ["**Parcial 3** (Clase 14) · 15%", "**PI CloudLite** · 20%", "Asistencia · 5%"]},
        ],
        note="Parciales síncronos presenciales · nunca en festivo/autónoma. Día de parcial = solo evaluación.",
        idx=7,
    )

    contenido_clases_slide(
        prs,
        CONTENIDO,
        title="CONTENIDO",
        sub="Sesión 0 + Clases 1–15 · grupo 6303C · lunes 10:00–12:00",
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
            {"name": "Play with Docker", "logo": "play_with_docker.png", "note": "Lab contenedores (4h)"},
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
