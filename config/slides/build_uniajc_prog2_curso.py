# -*- coding: utf-8 -*-
"""Presentación del Curso — Programación II (UNIAJC · FI303204 · 341C · 2026-2)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uniajc_slides_engine import (
    new_prs, course_cover, tutor_slide, padlet_slide, content_slide, table_content,
    evaluacion_cortes_slide, contenido_clases_slide,
    box_note_slide, closing_slide,
)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(
    ROOT, "Programacion II", "Clases",
    "Presentacion del Curso - Programacion II.pptx",
)

DOCENTE = "Julian Andres Castaño"
CORREO = "julianacastano@profesores.uniajc.edu.co"
CREDS = [
    "Ingeniero de Sistemas",
    "Candidato a MsC en Inteligencia Artificial",
    "Líder Técnico",
]


def build():
    prs = new_prs()

    course_cover(
        prs,
        "Programación II",
        "Programación Orientada a Objetos",
        [
            "Código: **FI303204** · Grupo: **341C** · Periodo: **2026-2**",
            "Programa: Ingeniería de Sistemas · Facultad de Ingeniería · UNIAJC",
            "Horario: **Miércoles 18:00 – 20:00** (120 min) · Franja Norte-Noche",
            "Docente: Julian Andres Castaño",
            "Campus Virtual: **[URL Campus Virtual UNIAJC — pendiente]**",
            "Listado de estudiantes: **[PENDIENTE listado]**",
        ],
    )

    tutor_slide(prs, DOCENTE, CREDS, CORREO, idx=2)
    padlet_slide(prs, idx=3)

    content_slide(
        prs, "¿Para qué existe este curso?",
        [
            "Profundizar el paradigma **POO** en Java: aplicaciones avanzadas, eventos, estructuras de datos y patrones básicos.",
            "Metodología activa basada en **proyectos** (ABPr) para construir soluciones sostenibles y éticas.",
            "Complementa Programación I y prepara para Ingeniería de Software.",
            "@@Objeto de estudio:@@ desarrollo avanzado de aplicaciones orientadas a objetos.",
        ],
        idx=4,
    )

    content_slide(
        prs, "Objetivo y resultados de aprendizaje",
        [
            "**Objetivo:** diseñar e implementar aplicaciones avanzadas con POO, eficientes, mantenibles y escalables.",
            "**RAA1** — Implementa estructuras de datos aplicadas a la resolución de problemas.",
            "**RAA2** — Desarrolla aplicaciones con manejo de eventos y componentes gráficos.",
            "**RAA3** — Aplica patrones de diseño básicos para optimizar la arquitectura del software.",
        ],
        idx=5,
    )

    content_slide(
        prs, "Cómo trabajamos en clase",
        [
            "**Sesión 0 (hoy)** = logística + acuerdo pedagógico + evaluación + CONTENIDO + **socialización del Proyecto Integrador**.",
            "**Clase 1** (material en archivo aparte) = diagnóstico de conocimientos previos + arranque temático — mismo bloque de hoy.",
            "Cada miércoles (120 min): **Teoría Core** → **Taller Guiado** → **Quiz corto**. Modalidad: **presencialidad asistida** (dos semanas al mes la clase puede ser virtual).",
            "Taller calificable: entrega máxima el **domingo 23:59**.",
            "Hilo conductor de todo el semestre: **Proyecto Integrador** continuo. Enfoque: aprender haciendo · aprendizaje invertido.",
        ],
        idx=6,
    )

    evaluacion_cortes_slide(
        prs, "Sistema de evaluación (Acuerdo pedagógico)",
        [
            {"corte": 1, "pct": "30%", "ventana": "10/08 – 13/09/2026",
             "desglose": ["**Parcial 1** (Clase 5) · 10%", "Talleres / Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 2, "pct": "30%", "ventana": "14/09 – 18/10/2026",
             "desglose": ["**Parcial 2** (Clase 10) · 10%", "Talleres / Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 3, "pct": "40%", "ventana": "19/10 – 22/11/2026",
             "desglose": ["**Parcial 3** (Clase 15) · 15%", "**Proyecto Integrador** · 20%", "Asistencia · 5%"]},
        ],
        note="Parcial al cierre de cada corte · nunca en festivo/autónoma. Día de parcial = solo evaluación.",
        idx=7,
    )

    contenido_clases_slide(
        prs,
        [
            {"n": 0, "kind": "sesion0", "tema": "Presentación del curso (logística) + socialización del PI", "fecha": "12/08"},
            {"n": 1, "tema": "Diagnóstico · Introducción a POO", "fecha": "12/08"},
            {"n": 2, "tema": "Colecciones dinámicas ArrayList", "fecha": "19/08"},
            {"n": 3, "tema": "Pilas y colas", "fecha": "26/08"},
            {"n": 4, "tema": "Mapas y conjuntos", "fecha": "02/09"},
            {"n": 5, "tema": "Interfaces gráficas GUI · Parcial 1", "fecha": "09/09"},
            {"n": 6, "tema": "Eventos y controladores", "fecha": "16/09"},
            {"n": 7, "tema": "Patrones de diseño", "fecha": "23/09"},
            {"n": 8, "tema": "Documentación y QA", "fecha": "30/09"},
            {"n": 9, "tema": "Refactorización con IA y persistencia", "fecha": "07/10"},
            {"n": 10, "tema": "Parcial 2", "fecha": "14/10"},
            {"n": 11, "tema": "Revisión de código cruzada", "fecha": "21/10"},
            {"n": 12, "tema": "Integración de módulos", "fecha": "28/10"},
            {"n": 13, "tema": "Control de excepciones", "fecha": "04/11"},
            {"n": 14, "tema": "Preparación presentación final", "fecha": "11/11"},
            {"n": 15, "tema": "Parcial 3 · Cierre", "fecha": "18/11"},
        ],
        title="CONTENIDO",
        sub="Día 1: Sesión 0 (Presentación del curso) + Clase 1 (diagnóstico · tema)",
        idx=8,
    )

    content_slide(
        prs, "Proyecto Integrador",
        [
            "Una aplicación completa que integre **estructuras de datos**, **GUI/eventos** y **patrones**.",
            "Orientada a una necesidad real del entorno.",
            "Se construye por avances a lo largo del semestre; pesa **20%** en el tercer corte.",
            "El enunciado detallado se trabaja desde la Clase 1.",
        ],
        idx=9,
    )

    content_slide(
        prs, "Recursos",
        [
            "Campus Virtual UNIAJC: **[URL Campus Virtual UNIAJC — pendiente]**",
            "IDE recomendado: IntelliJ IDEA / VS Code / NetBeans (Java 17+).",
            "Bibliografía (microcurrículo): Deitel & Deitel · Design Patterns (GoF) · Head First Design Patterns · JavaFX Docs.",
            "Material de clase: carpeta `Clases/Clase N` + talleres; guiones en `Guiones/` / `Kit docente/`.",
        ],
        idx=10,
    )

    box_note_slide(
        prs, "Acuerdos importantes",
        [
            ("info", "Horario fijo del grupo 341C: miércoles 18:00–20:00 · Norte-Noche."),
            ("aclaracion", "Los talleres guiados se entregan a más tardar el domingo 23:59 de la semana correspondiente."),
            ("advertencia", "La asistencia tiene peso en cada corte (10% / 10% / 5%). Llega a tiempo y participa. Listado: [PENDIENTE listado]."),
        ],
        idx=11,
    )

    closing_slide(
        prs,
        "¡Empezamos!",
        [
            "Programación II · Grupo **341C** · 2026-2",
            "Miércoles **18:00 – 20:00**",
            "UNIAJC · Ingeniería de Sistemas",
        ],
        accent="POO con propósito: código limpio + proyecto real",
    )

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    prs.save(OUT)
    print("OK ->", OUT)


if __name__ == "__main__":
    build()
