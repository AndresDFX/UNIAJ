# -*- coding: utf-8 -*-



"""Presentacion del Curso — Seminario de Sistemas (UNIAJC · 2026-1)."""



import os



import sys







sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))



from uniajc_slides_engine import (



    new_prs, course_cover, tutor_slide, padlet_slide, content_slide, table_content,
    evaluacion_cortes_slide,



    contenido_clases_slides, box_note_slide, herramientas_slide, closing_slide,



)







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



        'Código: **FI303301** · Grupo: **341C** · Periodo: **2026-1**',



        'Programa: Ingeniería de Sistemas · Facultad de Ingeniería · UNIAJC',



        'Horario: **Jueves 18:00 – 20:00** (120 min)',



        'Modalidad: **Presencialidad asistida** (Clase 1 y parciales presencial · resto virtual síncrona)',



        'Docente: Julian Andres Castaño',



    ], inicio_clase='20:10')



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



        '**Clase 1** (material en archivo aparte) = diagnóstico de conocimientos previos + arranque temático — mismo bloque de hoy.',



        'Cada jueves (120 min): **Teoría Core** → **Taller / exposición** → cierre. Modalidad: **Presencialidad asistida**: Clase 1 y parciales **presencial**; resto **virtual síncrona**; festivos = **clase autónoma**.',



        'Hilo conductor de todo el semestre: **Proyecto Integrador**, con avances y sustentación final. Enfoque ABPr · aprendizaje invertido.',



    ], idx=7)



    evaluacion_cortes_slide(
        prs, "Sistema de evaluación (Acuerdo pedagógico)",
        [
            {"corte": 1, "pct": "30%", "ventana": "13/08 – 13/09/2026",
             "desglose": ["**Parcial 1** (10/09 · Clase 5) · 10%", "Talleres o Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 2, "pct": "30%", "ventana": "14/09 – 18/10/2026",
             "desglose": ["**Parcial 2** (15/10 · Clase 10) · 10%", "Talleres o Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 3, "pct": "40%", "ventana": "19/10 – 22/11/2026",
             "desglose": ["**Parcial 3** (19/11 · Clase 15) · 15%", "**Proyecto Integrador** · 20%", "Asistencia · 5%"]},
        ],
        note="Parciales presencial síncrono · nunca en festivo/autónoma. Día de parcial = solo evaluación.",
        idx=8,
    )







    # Estilo CONTENIDO (lista limpia) — temas desde Plan curso/2026-1/PLAN_DE_CURSO_2026-1.md



    contenido_clases_slides(



        prs,



        [



            {"n": 0, "kind": "sesion0", "tema": "Presentación del curso (logística)", "fecha": "13/08"},
            {"n": 1, "tema": "Diagnóstico · Conceptos iniciales", "fecha": "13/08"},



            {"n": 2, "tema": "Ciclos de vida", "fecha": "20/08"},



            {"n": 3, "tema": "Metodologías tradicionales", "fecha": "27/08"},



            {"n": 4, "tema": "Metodologías ágiles", "fecha": "03/09"},



            {"n": 5, "tema": "Parcial 1", "fecha": "10/09"},



            {"n": 6, "tema": "Requerimientos de software", "fecha": "17/09"},



            {"n": 7, "tema": "Historias de usuario", "fecha": "24/09"},



            {"n": 8, "tema": "Introducción a UML", "fecha": "01/10"},



            {"n": 9, "tema": "Casos de uso", "fecha": "08/10"},



            {"n": 10, "tema": "Parcial 2", "fecha": "15/10"},



            {"n": 11, "tema": "Avance proyecto integrador", "fecha": "22/10"},



            {"n": 12, "tema": "Diagramas UML avanzados", "fecha": "29/10"},



            {"n": 13, "tema": "Diseño de interfaces", "fecha": "05/11"},



            {"n": 14, "tema": "Evaluación final (prep. sustentación) · Sustentación de proyectos + cierre", "fecha": "12/11"},



            {"n": 15, "tema": "Parcial 3", "fecha": "19/11"},



        ],



        title="CONTENIDO",



        idx_start=9,
        sub="Día 1: Sesión 0 (Presentación del curso, archivo aparte) + Clase 1 (diagnóstico · tema)",



    )



    content_slide(prs, "Proyecto Integrador", [



        '@@Socialización de hoy (Sesión 0):@@ presentamos el PI completo para que lo tengan claro desde la Clase 1.',



        'Diseño, desarrollo y **sustentación** de un proyecto de software orientado a objetos.',



        'Incluye documentación técnica, pruebas basicas y comunicación clara de la solucion.',



        'Pesa **20%** en el tercer corte (además del Parcial 3).',



    ], idx=10)



    content_slide(prs, "Recursos", [



        'Bibliografía (microcurrículo): GoF · Head First Design Patterns · Sommerville · Java Docs.',



        'Material: carpeta compartida `Clases/` (Presentación del Curso y Clase N).',



    ], idx=11)



    box_note_slide(prs, "Acuerdos importantes", [



            ('info', 'Jueves 18:00-20:00 (120 min). Modalidad: Presencialidad asistida (jueves virtual / parciales presencial). Grupo: 341C.'),



            ('aclaracion', 'Día 1: Sesión 0 (Presentación del curso, archivo aparte) + Clase 1 (diagnóstico + Conceptos iniciales). Material estudiante solo en carpeta Clases/.'),



            ('advertencia', 'Parciales NUNCA en autónoma: P1=Clase 5 (10/09), P2=Clase 10 (15/10), P3=Clase 15 (19/11).'),



        ], idx=12)







    herramientas_slide(
        prs,
        [
            {"name": "draw.io", "logo": "drawio.png", "note": "Diagramas UML"},
            {"name": "Mermaid", "logo": "mermaid.png", "note": "Docs as Code"},
            {"name": "Padlet", "logo": "padlet.png", "note": "Rompe-hielo"},
        ],
        title="Herramientas del curso",
        sub="Gratis en navegador · Draw.io / Mermaid",
        idx=13,
    )







    closing_slide(prs, "¡Empezamos!", [



        'Seminario de Sistemas · Grupo **341C** · 2026-1',



        'Jueves **18:00 – 20:00**',



        'UNIAJC · Ingeniería de Sistemas',



    ], accent='Proyecto + documentación + sustentación')



    os.makedirs(os.path.dirname(OUT), exist_ok=True)



    prs.save(OUT)



    print("OK ->", OUT)











if __name__ == "__main__":



    build()



