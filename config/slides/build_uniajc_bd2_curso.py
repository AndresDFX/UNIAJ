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

import calendario_2026_2 as cal

CURSO_KEY = "bases_datos_ii"

# Temas del material ya construido (carpetas «Clase N», que NO se renumeran).
# El calendario 2026-2 (13 sesiones) decide en qué sesión se dicta cada uno; dos
# sesiones son dobles y la sesión 13 (16/11) es de sustentaciones del PI VetCare.
TEMAS_MATERIAL = {
    1: "Diagnóstico · Revisión de Bases de Datos I",
    2: "Administración de bases de datos",
    3: "Procedimientos almacenados",
    4: "Funciones y disparadores · Seguridad y respaldo",
    5: "Repaso y evaluación del corte 1",
    6: "Optimización de consultas",
    7: "Índices y particionamiento",
    8: "Tuning y gestión de transacciones",
    9: "Repaso y evaluación del corte 2",
    10: "Control de concurrencia",
    11: "Avance del proyecto final",
    12: "Integración de apps externas · Preparación final",
    13: "Análisis de casos reales",
    14: "Repaso y evaluación del corte 3",
    15: "Presentación del proyecto + cierre",
}

CT = cal.cortes(CURSO_KEY)







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



        'Horario: **Lunes 18:00 – 20:00** (120 min) · Modalidad: **Presencialidad asistida**',



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



        '**Sesión 1** (material «Clase 1», archivo aparte) = diagnóstico de conocimientos previos + arranque temático — mismo bloque de hoy.',



        'Cada lunes (120 min): **Teoría Core** → **Taller / laboratorio en la nube** → cierre. **13 sesiones**: sesión 1 y parciales (**5 / 9 / 12**) **presencial**; resto **virtual síncrona**; festivos = **clase autónoma**; dos sesiones **dobles** y sustentación en la **sesión 13**.',



        'Herramientas **gratis + en la nube**. Talleres y quices/parciales se entregan/presentan en @@ExamLab@@ (https://examlab.lovable.app/) — no es la plataforma oficial de la UNIAJC, la usamos solo para esto.',



        'Hilo conductor de todo el semestre: **Proyecto Integrador VetCare DB**.',



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
                          "**PI VetCare** · 20%", "Asistencia · 5%"]},
        ],
        note="Parciales síncronos presenciales · nunca en festivo/autónoma. Día de parcial = solo evaluación.",
        idx=8,
    )







    # Estilo CONTENIDO (lista limpia) — temas desde Plan curso/2026-2/PLAN_DE_CURSO_2026-2.md



    contenido_clases_slides(



        prs,



        cal.contenido_items(
            CURSO_KEY, TEMAS_MATERIAL,
            "Presentación del curso (logística) + socialización del PI VetCare",
        ),



        title="CONTENIDO",



        idx_start=9,
        sub=("13 sesiones · los 15 temas se conservan: dos sesiones son **dobles** (dos temas en un bloque). Día 1: Sesión 0 (archivo aparte) + Sesión 1 (diagnóstico · tema)"),



    )



    content_slide(prs, "Proyecto Integrador", [



        '@@Socialización de hoy (Sesión 0):@@ presentamos el PI completo para que lo tengan claro desde la Clase 1.',



        '**VetCare DB** — BD avanzada para clínica veterinaria (ABPr).',



        'Integra seguridad/respaldo, procs/triggers, optimización e integración app↔BD.',



        'Hitos: avance + preparación final en la **sesión 10** (26/10, sesión doble Clases 11+12) · **Parcial 3** sesión 12 (09/11) · **sustentación** sesión 13 (16/11).',



        'Pesa **20%** del Corte 3. Enunciado: carpeta `Clases/Proyecto Integrador/`.',



    ], idx=10)







    content_slide(prs, "Recursos", [



        'Herramientas **gratis en navegador** (sin instalacion de SGBD local) — detalle en Plan de curso (pendiente aprobacion docente).',



        '@@ExamLab@@ (https://examlab.lovable.app/): entrega de talleres + quices/parciales del curso.',



        'SQL: **DB Fiddle** / SQLTest.online · PL/SQL: **Oracle Live SQL**.',



        'Modelos ER: **draw.io / diagrams.net** · bocetos: **Excalidraw**.',



        'Bibliografia: Coronel & Morris · Date · Oracle PL/SQL Docs.',



    ], idx=11)



    box_note_slide(prs, "Acuerdos importantes", [



            ('info', 'Lunes 18:00 – 20:00 · Presencialidad asistida: Clase 1 y parciales presencial · resto virtual síncrona · festivos autónoma · Grupo 641A-2.'),



            ('aclaracion', 'Día 1: Sesión 0 (Presentación del curso, archivo aparte) + Clase 1 (diagnóstico + revisión BD I). Festivos = autónoma con actividad en ExamLab.'),



            ('advertencia', 'Parciales NUNCA en autonoma: P1=sesión 5 (21/09), P2=sesión 9 (19/10), P3=sesión 12 (09/11). La sesión 13 (16/11) es de sustentación del PI VetCare.'),



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



