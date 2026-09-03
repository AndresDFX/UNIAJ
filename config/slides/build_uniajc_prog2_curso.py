# -*- coding: utf-8 -*-
"""Presentación del Curso — Programación II (UNIAJC · FI303204 · 341C · 2026-2)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uniajc_slides_engine import (
    new_prs, course_cover, tutor_slide, padlet_slide, content_slide, table_content,
    evaluacion_cortes_slide, contenido_clases_slide,
    box_note_slide, herramientas_slide, closing_slide,
)
import calendario_2026_2 as cal

CURSO_KEY = "programacion_ii"

# Temas del material ya construido (carpetas «Clase N», que NO se renumeran).
# El calendario 2026-2 (13 sesiones) decide en qué sesión se dicta cada uno;
# las sesiones dobles juntan dos de estos temas en un bloque de 120 min.
TEMAS_MATERIAL = {
    1: "Diagnóstico · Introducción a POO",
    2: "Colecciones dinámicas ArrayList",
    3: "Pilas y colas",
    4: "Mapas, conjuntos e interfaces gráficas GUI",
    5: "Repaso y evaluación del corte 1",
    6: "Eventos y controladores",
    7: "Patrones de diseño (Singleton y Factory)",
    8: "Documentación y QA (Javadoc y pruebas)",
    9: "Refactorización con IA y persistencia",
    10: "Repaso y evaluación del corte 2",
    11: "Revisión de código cruzada",
    12: "Integración de módulos",
    13: "Control de excepciones",
    14: "Preparación presentación final",
    15: "Cierre y evaluación del corte 3",
}

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
    # La Presentacion del Curso es el UNICO deck que nombra la plataforma de entrega y
    # su URL: es donde se explica una vez como se entrega. Los decks de clase nacen en
    # modo generico, porque ahi lo unico fijo es el tema. Ver `new_prs` en el motor.
    prs = new_prs(generico=False)

    course_cover(
        prs,
        "Programación II",
        "Programación Orientada a Objetos",
        [
            "Código: **FI303204** · Grupo: **341C** · Periodo: **2026-2**",
            "Programa: Ingeniería de Sistemas · Facultad de Ingeniería · UNIAJC",
            "Horario: **Miércoles 18:00 – 20:00** (120 min) · Franja Norte-Noche",
            "Docente: Julian Andres Castaño",
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
            "Cada miércoles (120 min): **Teoría Core** → **Taller Guiado** → **cierre**. Modalidad: **Virtual**: todas las sesiones son **virtual síncrona** por Google Meet, incluidos la Sesión 1 y los parciales; festivos = **clase autónoma**.",
            "Talleres y quices/parciales se entregan/presentan en @@ExamLab@@ (https://uniaj.examlab.workers.dev/) — no es la plataforma oficial de la UNIAJC, la usamos solo para esto. Taller calificable: entrega máxima el **domingo 23:59**.",
            "Hilo conductor de todo el semestre: **Proyecto Integrador** continuo. Enfoque: aprender haciendo · aprendizaje invertido.",
        ],
        idx=6,
    )

    ct = cal.cortes(CURSO_KEY)
    evaluacion_cortes_slide(
        prs, "Sistema de evaluación (Acuerdo pedagógico)",
        [
            {"corte": 1, "pct": ct[0]["pct"], "ventana": ct[0]["ventana"],
             "desglose": [f"**Parcial 1** ({ct[0]['parcial_fecha']} · sesión {ct[0]['parcial_sesion']}) · 10%",
                          "Talleres o Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 2, "pct": ct[1]["pct"], "ventana": ct[1]["ventana"],
             "desglose": [f"**Parcial 2** ({ct[1]['parcial_fecha']} · sesión {ct[1]['parcial_sesion']}) · 10%",
                          "Talleres o Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 3, "pct": ct[2]["pct"], "ventana": ct[2]["ventana"],
             "desglose": [f"**Parcial 3** ({ct[2]['parcial_fecha']} · sesión {ct[2]['parcial_sesion']}) · 15%",
                          "**Proyecto Integrador** · 20%", "Asistencia · 5%"]},
        ],
        note="Parcial al cierre de cada corte · nunca en festivo/autónoma. Día de parcial = solo evaluación.",
        idx=7,
    )

    contenido_clases_slide(
        prs,
        cal.contenido_items(
            CURSO_KEY, TEMAS_MATERIAL,
            "Presentación del curso (logística) + socialización del PI",
        ),
        title="CONTENIDO",
        sub=("13 sesiones · los 15 temas del microcurrículo se conservan: dos sesiones son "
             "**dobles** (dos temas en un bloque). Día 1: Sesión 0 + Clase 1 (diagnóstico · tema)."),
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
            "IDE del curso: **Visual Studio Code** con el Extension Pack for Java (JDK 17+).",
            "@@ExamLab@@ (https://uniaj.examlab.workers.dev/): entrega de talleres + quices/parciales del curso.",
            "Bibliografía (microcurrículo): Deitel & Deitel · Design Patterns (GoF) · Head First Design Patterns · JavaFX Docs.",
            "Material de clase: carpeta `Clases/Clase N` + talleres; guiones en `Guiones/` / `Kit docente/`.",
        ],
        idx=10,
    )

    box_note_slide(
        prs, "Acuerdos importantes",
        [
            ("info", "Horario fijo del grupo 341C: miércoles 18:00–20:00 · Norte-Noche."),
            ("aclaracion", "Los talleres guiados se entregan en ExamLab (https://uniaj.examlab.workers.dev/) a más tardar el domingo 23:59 de la semana correspondiente."),
            ("advertencia", "La asistencia tiene peso en cada corte (10% / 10% / 5%). Llega a tiempo y participa."),
        ],
        idx=11,
    )

    herramientas_slide(
        prs,
        [
            {"name": "IntelliJ IDEA", "logo": "intellij.png", "note": "IDE recomendado"},
            {"name": "VS Code", "logo": "vscode.png", "note": "IDE alterno"},
            {"name": "Visual Studio Code", "logo": "vscode.png", "note": "IDE del curso (Extension Pack for Java)"},
            {"name": "Java", "logo": "java.png", "note": "JDK 17+"},
            {"name": "ExamLab", "logo": "examlab.png", "note": "Talleres + quices/parciales"},
        ],
        title="Herramientas del curso",
        sub="Gratis · IDE a elección · entrega/evaluación",
        idx=12,
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
