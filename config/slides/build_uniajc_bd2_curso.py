# -*- coding: utf-8 -*-



"""Presentacion del Curso — Bases de Datos II (UNIAJC · 2026-2)."""



import os



import sys







sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))



from uniajc_slides_engine import (



    new_prs, course_cover, tutor_slide, padlet_slide, content_slide, table_content,
    evaluacion_cortes_slide,



    contenido_clases_slides, box_note_slide, herramientas_slide, closing_slide,



)







ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))



OUT = os.path.join(ROOT, *['Bases de Datos II', 'Clases', 'Presentacion del Curso - Bases de Datos II.pptx'])







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



    course_cover(prs, 'Bases de Datos II', 'Gestión avanzada y optimización', [



        'Código: **FI303215** · Grupo: **641A-2** · Periodo: **2026-2**',



        'Programa: Ingeniería de Sistemas · Facultad de Ingeniería · UNIAJC',



        'Horario: **Lunes 18:00 – 20:00** (120 min) · Modalidad: **Presencialidad asistida** (clases y parciales síncronos)',



        'Docente: Julian Andres Castaño',



    ], inicio_clase='18:10')



    tutor_slide(prs, DOCENTE, CREDS, CORREO, idx=2)



    padlet_slide(prs, idx=3)



    content_slide(prs, "¿Para qué existe este curso?", [



        'Profundizar la **gestion avanzada** de bases de datos: optimización, seguridad, procedimientos y administración.',



        'Diseñar soluciones de alto rendimiento con integridad, disponibilidad y protección de datos.',



        'Consolida habilidades para Arquitectura de Sistemas y Seguridad.',



        '@@Objeto de estudio:@@ gestion avanzada y optimización de BD relacionales.',



    ], idx=4)



    content_slide(prs, "Objetivo de aprendizaje", [



        '@@Objeto de estudio:@@ gestión avanzada y optimización de bases de datos relacionales.',



        '**Objetivo:** diseñar, administrar y optimizar bases de datos relacionales avanzadas, garantizando **seguridad**, **integridad** y **eficiencia** en el manejo de grandes volúmenes de información.',



        'Profundiza en optimización, seguridad, procedimientos almacenados y administración eficiente de los recursos de información.',



        'Consolida habilidades clave para Arquitectura de Sistemas Computacionales y Seguridad.',



    ], idx=5, size=15)



    content_slide(prs, "Resultados de aprendizaje (RAA)", [



        '**RAA1** — Administra bases de datos aplicando estrategias de seguridad y respaldo. Configura políticas de protección y planes de respaldo/recuperación responsables.',



        '**RAA2** — Implementa procedimientos almacenados y disparadores para la automatización de procesos. Desarrolla lógica en el motor de BD para integridad y reutilización.',



        '**RAA3** — Optimiza consultas y estructuras de bases de datos para mejorar el rendimiento del sistema. Aplica índices, tuning y análisis de rendimiento sobre casos reales.',



    ], idx=6, size=15)



    content_slide(prs, "Cómo trabajamos en clase", [



        '**Sesión 0 (hoy)** = logística + acuerdo pedagógico + evaluación + CONTENIDO + **socialización del Proyecto Integrador VetCare**.',



        '**Clase 1** (material en archivo aparte) = diagnóstico de conocimientos previos + arranque temático — mismo bloque de hoy.',



        'Cada lunes (120 min): **Teoría Core** → **Taller / laboratorio en la nube** → **Quiz corto**. Modalidad: **Presencialidad asistida** (parciales presenciales · resto virtual · festivos autónomos).',



        'Herramientas **gratis + en la nube**. Talleres y quices/parciales se entregan/presentan en @@ExamLab@@ (no es la plataforma oficial de la UNIAJC, la usamos solo para esto).',



        'Hilo conductor de todo el semestre: **Proyecto Integrador VetCare DB**.',



    ], idx=7)



    evaluacion_cortes_slide(
        prs, "Sistema de evaluación (Acuerdo pedagógico)",
        [
            {"corte": 1, "pct": "30%", "ventana": "10/08 – 13/09/2026",
             "desglose": ["**Parcial 1** (07/09 · Clase 5) · 10%", "Talleres / Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 2, "pct": "30%", "ventana": "14/09 – 18/10/2026",
             "desglose": ["**Parcial 2** (05/10 · Clase 9) · 10%", "Talleres / Quiz · 10%", "Asistencia · 10%"]},
            {"corte": 3, "pct": "40%", "ventana": "19/10 – 22/11/2026",
             "desglose": ["**Parcial 3** (09/11 · Clase 14) · 15%", "**PI VetCare** · 20%", "Asistencia · 5%"]},
        ],
        note="Parciales síncronos presenciales · nunca en festivo/autónoma. Día de parcial = solo evaluación.",
        idx=8,
    )







    # Estilo CONTENIDO (lista limpia) — temas desde Plan curso/2026-2/PLAN_DE_CURSO_2026-2.md



    contenido_clases_slides(



        prs,



        [



            {"n": 0, "kind": "sesion0", "tema": "Presentación del curso (logística)", "fecha": "10/08"},
            {"n": 1, "tema": "Diagnóstico · Revisión de Bases de Datos I", "fecha": "10/08"},



            {"n": 2, "tema": "Administración de bases de datos", "fecha": "17/08", "tag": "Autónoma"},



            {"n": 3, "tema": "Procedimientos almacenados", "fecha": "24/08"},



            {"n": 4, "tema": "Funciones y disparadores · Seguridad y respaldo", "fecha": "31/08"},



            {"n": 5, "tema": "Parcial 1", "fecha": "07/09"},



            {"n": 6, "tema": "Optimización de consultas", "fecha": "14/09"},



            {"n": 7, "tema": "Índices y particionamiento", "fecha": "21/09"},



            {"n": 8, "tema": "Tuning de bases de datos · Gestión de transacciones", "fecha": "28/09"},



            {"n": 9, "tema": "Parcial 2", "fecha": "05/10"},



            {"n": 10, "tema": "Control de concurrencia", "fecha": "12/10", "tag": "Autónoma"},



            {"n": 11, "tema": "Avance del proyecto final", "fecha": "19/10"},



            {"n": 12, "tema": "Integración de aplicaciones externas · Preparación de presentación final", "fecha": "26/10"},



            {"n": 13, "tema": "Análisis de casos reales", "fecha": "02/11", "tag": "Autónoma"},



            {"n": 14, "tema": "Parcial 3", "fecha": "09/11"},



            {"n": 15, "tema": "Presentación del proyecto + cierre", "fecha": "16/11", "tag": "Autónoma"},



        ],



        title="CONTENIDO",



        idx_start=9,
        sub="Día 1: Sesión 0 (Presentación del curso, archivo aparte) + Clase 1 (diagnóstico · tema)",



    )



    content_slide(prs, "Proyecto Integrador", [



        '@@Socialización de hoy (Sesión 0):@@ presentamos el PI completo para que lo tengan claro desde la Clase 1.',



        '**VetCare DB** — BD avanzada para clínica veterinaria (ABPr).',



        'Integra seguridad/respaldo, procs/triggers, optimización e integración app↔BD.',



        'Hitos: avance **Clase 11** (19/10) · prep. **Clase 12** (26/10) · Parcial 3 **Clase 14** (09/11) · cierre **Clase 15** (16/11, autónoma).',



        'Pesa **20%** del Corte 3. Enunciado: carpeta `Clases/Proyecto Integrador/`.',



    ], idx=10)







    content_slide(prs, "Recursos", [



        'Herramientas **gratis en navegador** (sin instalacion de SGBD local) — detalle en Plan de curso (pendiente aprobacion docente).',



        '@@ExamLab@@ (examlab.lovable.app/app): entrega de talleres + quices/parciales del curso.',



        'SQL: **DB Fiddle** / SQLTest.online · PL/SQL: **Oracle Live SQL**.',



        'Modelos ER: **draw.io / diagrams.net** · bocetos: **Excalidraw**.',



        'Bibliografia: Coronel & Morris · Date · Oracle PL/SQL Docs.',



    ], idx=11)



    box_note_slide(prs, "Acuerdos importantes", [



            ('info', 'Lunes 18:00 – 20:00 · Presencialidad asistida (clases y parciales síncronos) · Grupo 641A-2.'),



            ('aclaracion', 'Día 1: Sesión 0 (Presentación del curso, archivo aparte) + Clase 1 (diagnóstico + revisión BD I). Festivos = autónoma en Campus Virtual.'),



            ('advertencia', 'Parciales NUNCA en autonoma: P1=Clase 5 (07/09), P2=Clase 9 (05/10), P3=Clase 14 (09/11).'),



        ], idx=12)







    herramientas_slide(
        prs,
        [
            {"name": "DB Fiddle", "logo": "dbfiddle.png", "note": "SQL práctico"},
            {"name": "Oracle Live SQL", "logo": "oracle_livesql.png", "note": "PL/SQL · cuenta free"},
            {"name": "draw.io", "logo": "drawio.png", "note": "Modelos ER"},
            {"name": "SQLTest.online", "logo": "sqltest.png", "note": "Multi-motor"},
            {"name": "ExamLab", "logo": "examlab.png", "note": "Talleres + quices/parciales"},
        ],
        title="Herramientas del curso",
        sub="Gratis en navegador · SQL + diagramas ER + entrega/evaluación",
        idx=13,
    )







    closing_slide(prs, "¡Empezamos!", [



        'Bases de Datos II · Grupo **641A-2** · 2026-2',



        'Lunes **18:00 – 20:00** · Presencialidad asistida',



        'UNIAJC · Ingeniería de Sistemas',



    ], accent='Datos seguros, consultas rapidas, proyecto real')



    os.makedirs(os.path.dirname(OUT), exist_ok=True)



    prs.save(OUT)



    print("OK ->", OUT)











if __name__ == "__main__":



    build()



