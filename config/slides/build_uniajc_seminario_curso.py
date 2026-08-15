# -*- coding: utf-8 -*-



"""Presentacion del Curso — Seminario de Sistemas (UNIAJC · 2026-2)."""



import os



import sys







sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))



from uniajc_slides_engine import (



    new_prs, course_cover, tutor_slide, padlet_slide, content_slide, table_content,
    evaluacion_cortes_slide,



    contenido_clases_slides, box_note_slide, herramientas_slide, closing_slide,



)

import calendario_2026_2 as cal

CURSO_KEY = "seminario"

# Temas del material ya construido (carpetas «Clase N», que NO se renumeran).
# El calendario 2026-2 (13 sesiones) decide en qué sesión se dicta cada uno;
# dos sesiones son dobles (dos temas afines en un bloque de 120 min).
TEMAS_MATERIAL = {
    1: "Diagnóstico · Conceptos iniciales",
    2: "Ciclos de vida del software",
    3: "Metodologías tradicionales",
    4: "Metodologías ágiles",
    5: "Repaso y evaluación del corte 1",
    6: "Requerimientos de software",
    7: "Historias de usuario",
    8: "Introducción a UML",
    9: "Casos de uso",
    10: "Repaso y evaluación del corte 2",
    11: "Avance del proyecto integrador",
    12: "Diagramas UML avanzados",
    13: "Diseño de interfaces",
    14: "Preparación de la sustentación y cierre",
    15: "Cierre y evaluación del corte 3",
}

CT = cal.cortes(CURSO_KEY)








ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))



OUT = os.path.join(ROOT, *['Seminario de Sistemas', 'Clases', 'Presentacion del Curso - Seminario de Sistemas.pptx'])







DOCENTE = "Julian Andres Castaño"



CORREO = "julianacastano@profesores.uniajc.edu.co"



CREDS = [



    "Ingeniero de Sistemas",



    "Candidato a MsC en Inteligencia Artificial",



    "Líder Técnico",



    "Speaker Tecnológico",



]











def build():



    prs = new_prs()



    course_cover(prs, 'Seminario de Sistemas', 'Proyecto integrador de software', [



        'Código: **FI303301** · Grupo: **341C** · Periodo: **2026-2**',



        'Programa: Ingeniería de Sistemas · Facultad de Ingeniería · UNIAJC',



        'Horario: **Jueves 18:00 – 20:00** (120 min)',



        'Modalidad: **Presencialidad asistida** (Clase 1 y parciales presencial · resto virtual síncrona)',



        'Docente: Julian Andres Castaño',



    ], inicio_clase='18:10')



    tutor_slide(prs, DOCENTE, CREDS, CORREO, idx=2)



    padlet_slide(prs, idx=3)



    content_slide(prs, "¿Para qué existe este curso?", [



        'Consolidar conocimientos de Programacion II mediante **análisis, diseño, desarrollo y exposición** de proyectos integradores.',



        'Fortalecer patrones, documentación técnica, pruebas y comunicación efectiva.',



        '@@Objeto de estudio:@@ integración de conocimientos para proyectos de software OO.',



    ], idx=4)



    content_slide(prs, "Objetivo de aprendizaje", [



        '@@Objeto de estudio:@@ integración de conocimientos para el desarrollo y presentación de proyectos de software orientados a objetos.',



        '**Objetivo:** desarrollar un proyecto de software aplicando técnicas avanzadas de **POO**, fortaleciendo la documentación, validación y comunicación efectiva de soluciones.',



        'Consolida lo aprendido en Programación II mediante análisis, diseño, desarrollo y exposición de proyectos integradores.',



        'Se fortalecen patrones de diseño, documentación técnica, pruebas funcionales y despliegue básico de aplicaciones.',



    ], idx=5, size=15)



    content_slide(prs, "Resultados de aprendizaje (RAA)", [



        '**RAA1** — Aplica patrones de diseño y principios de modularidad en proyectos de software. Organiza el código para que sea reutilizable, mantenible y colaborativo.',



        '**RAA2** — Documenta y valida aplicaciones mediante pruebas básicas. Elabora documentación técnica y realiza pruebas/validaciones funcionales del producto.',



        '**RAA3** — Presenta y sustenta proyectos de software de manera clara y estructurada. Comunica la solución tecnológica con calidad y compromiso profesional.',



    ], idx=6, size=15)



    content_slide(prs, "Cómo trabajamos en clase", [



        '**Sesión 0 (hoy)** = logística + acuerdo pedagógico + evaluación + CONTENIDO + **socialización del Proyecto Integrador**.',



        '**Sesión 1** (material «Clase 1», archivo aparte) = diagnóstico de conocimientos previos + arranque temático — mismo bloque de hoy.',



        'Cada jueves (120 min): **Teoría Core** → **Taller / exposición** → cierre. **13 sesiones**: sesión 1 y parciales (**5 / 9 / 13**) **presencial**; resto **virtual síncrona**; dos sesiones son **dobles** (dos temas en un bloque).',



        'Hilo conductor de todo el semestre: **Proyecto Integrador**, con avances y sustentación final. Enfoque ABPr · aprendizaje invertido.',



    ], idx=7)



    evaluacion_cortes_slide(
        prs, "Sistema de evaluación (Acuerdo pedagógico)",
        [
            {"corte": 1, "pct": CT[0]["pct"], "ventana": CT[0]["ventana"],
             "desglose": [f"**Parcial 1** ({CT[0]['parcial_fecha']} · sesión {CT[0]['parcial_sesion']}) · 10%",
                          "Talleres o Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 2, "pct": CT[1]["pct"], "ventana": CT[1]["ventana"],
             "desglose": [f"**Parcial 2** ({CT[1]['parcial_fecha']} · sesión {CT[1]['parcial_sesion']}) · 10%",
                          "Talleres o Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 3, "pct": CT[2]["pct"], "ventana": CT[2]["ventana"],
             "desglose": [f"**Parcial 3** ({CT[2]['parcial_fecha']} · sesión {CT[2]['parcial_sesion']}) · 15%",
                          "**Proyecto Integrador** · 20%", "Asistencia · 5%"]},
        ],
        note="Parciales presencial síncrono · nunca en festivo/autónoma. Día de parcial = solo evaluación.",
        idx=8,
    )







    # Estilo CONTENIDO (lista limpia) — temas desde Plan curso/2026-2/PLAN_DE_CURSO_2026-2.md



    contenido_clases_slides(



        prs,



        cal.contenido_items(
            CURSO_KEY, TEMAS_MATERIAL,
            "Presentación del curso (logística) + socialización del PI",
        ),



        title="CONTENIDO",



        idx_start=9,
        sub=("13 sesiones · los 15 temas se conservan: dos sesiones son **dobles** (dos temas en un bloque). Día 1: Sesión 0 (archivo aparte) + Sesión 1 (diagnóstico · tema)"),



    )



    content_slide(prs, "Proyecto Integrador", [



        '@@Socialización de hoy (Sesión 0):@@ presentamos el PI completo para que lo tengan claro desde la Clase 1.',



        'Diseño, desarrollo y **sustentación** de un proyecto de software orientado a objetos.',



        'Incluye documentación técnica, pruebas basicas y comunicación clara de la solucion.',



        'Pesa **20%** en el tercer corte (además del Parcial 3).',



    ], idx=10)



    content_slide(prs, "Recursos", [



        'Bibliografía (microcurrículo): GoF · Head First Design Patterns · Sommerville · Java Docs.',



        '@@ExamLab@@ (https://examlab.lovable.app/): entrega de talleres + quices/parciales del curso.',



        'Material: carpeta compartida `Clases/` (Presentación del Curso y Clase N).',



    ], idx=11)



    box_note_slide(prs, "Acuerdos importantes", [



            ('info', 'Jueves 18:00-20:00 (120 min). Modalidad: Presencialidad asistida (jueves virtual / parciales presencial). Grupo: 341C.'),



            ('aclaracion', 'Día 1: Sesión 0 (Presentación del curso, archivo aparte) + Clase 1 (diagnóstico + Conceptos iniciales). Material estudiante solo en carpeta Clases/. Talleres y quices/parciales en ExamLab (https://examlab.lovable.app/).'),



            ('advertencia', 'Parciales NUNCA en autónoma: P1=sesión 5 (24/09), P2=sesión 9 (22/10), P3=sesión 13 (19/11, con sustentación final).'),



        ], idx=12)







    herramientas_slide(
        prs,
        [
            {"name": "draw.io", "logo": "drawio.png", "note": "Diagramas UML"},
            {"name": "Mermaid", "logo": "mermaid.png", "note": "Docs as Code"},
            {"name": "Padlet", "logo": "padlet.png", "note": "Rompe-hielo"},
            {"name": "ExamLab", "logo": "examlab.png", "note": "Talleres + quices/parciales"},
        ],
        title="Herramientas del curso",
        sub="Gratis en navegador · Draw.io / Mermaid",
        idx=13,
    )







    closing_slide(prs, "¡Empezamos!", [



        'Seminario de Sistemas · Grupo **341C** · 2026-2',



        'Jueves **18:00 – 20:00**',



        'UNIAJC · Ingeniería de Sistemas',



    ], accent='Proyecto + documentación + sustentación')



    os.makedirs(os.path.dirname(OUT), exist_ok=True)



    prs.save(OUT)



    print("OK ->", OUT)











if __name__ == "__main__":



    build()



