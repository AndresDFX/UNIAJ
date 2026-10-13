# -*- coding: utf-8 -*-
"""Genera el Proyecto Integrador 2026-2 de los cinco cursos.

BD II, Arquitectura, Programacion II, Seminario e Introduccion a la Ingenieria. La entrega
y la sustentacion son comunes a los cinco (ver `entrega_y_sustentacion`); el resto es de
cada curso.

Estudiante (compartible):
  <Curso>/Clases/Proyecto Integrador/Enunciado Proyecto Integrador - <Curso> - 2026-2.docx

Docente (privado):
  <Curso>/Kit docente/Proyecto Integrador/Guia Docente PI - <Curso> - 2026-2.docx
  <Curso>/Kit docente/Proyecto Integrador/Guia Docente PI - <Curso> - 2026-2.md
"""
from __future__ import annotations

import os
import re
import sys
import unicodedata
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

# El cliente ficticio vive en un modulo aparte porque lo comparten los cuatro
# cursos y, ademas del enunciado del PI, lo consumen las diapositivas de BD II.
# Mientras estaba definido aqui, BD II no lo usaba y su enunciado describia al
# cliente con un parrafo generico que no lo nombraba.
from vetcare_contexto import (  # noqa: E402
    CLIENTE,
    CONTEXTO_VETCARE,
    CONVENCIONES_DATOS,
    ELENCO,
    ENTIDADES,
    ESCALA,
    FUERA_DE_ALCANCE,
    INTERESADOS,
    NOMENCLATURA,
    PERFIL,
    PROBLEMAS,
    REGLAS_NEGOCIO,
)

AZUL = RGBColor(0x09, 0x52, 0x92)
CIAN = RGBColor(0x26, 0x9C, 0xCB)
GRIS = RGBColor(0x2B, 0x2B, 0x2B)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
ROJO = RGBColor(0xA0, 0x20, 0x30)
FONT = "Calibri"

DOCENTE = "Julian Andres Castaño Espinosa"
CORREO = "julianacastano@profesores.uniajc.edu.co"


#: Como se nombra la plataforma en el enunciado del ESTUDIANTE. Parametro porque este
#: generador sirve a varios cursos y solo Arquitectura pidio no nombrarla.
NOMBRE_PLATAFORMA = "ExamLab"


def _plat():
    return NOMBRE_PLATAFORMA


# ---------------------------------------------------------------------------
# Entrega y sustentacion: COMUNES a los cinco cursos (decision docente, 13/10/2026)
#
# Un solo plazo para los siete grupos, una sola forma de entregar y la misma duracion de
# sustentacion. Viven aqui, una vez, porque repetidas en cada curso divergieron: cuatro
# cursos decian 5-8 min de sustentacion e Introduccion 9 + 3.
# ---------------------------------------------------------------------------

#: Modalidad del PI en los cinco cursos este semestre (decision docente, 13/10/2026): antes
#: BD II y Arquitectura eran individuales con equipos de 2-3 «si el docente autoriza», Prog. II
#: y Seminario no lo decian, e Introduccion era de equipo sin tamano.
EQUIPO = "en equipo de 4 a 5 integrantes (máximo 5)"

PLAZO = "domingo 15 de noviembre de 2026, 11:59 p. m."
PLAZO_CORTO = "dom 15/11/2026, 11:59 p. m."
SUSTENTACION = ("15 minutos de exposición + 5 minutos de preguntas por equipo (turno de 20 "
                "minutos); hablan todos los integrantes")
ZIP = ("un solo archivo .zip con todo —código, documentos, diagramas y capturas—; dentro "
       "puede ir cualquier tipo de archivo, y pesa como máximo 50 MB")
ENLACE = "el enlace al repositorio de GitHub o a la carpeta de Drive del proyecto"


def _sin_tildes(texto):
    """Los enunciados de Prog. II y Seminario se escribieron sin tildes ni enes."""
    s = unicodedata.normalize("NFD", str(texto))
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def entrega_y_sustentacion(doc, titulo, sustentacion, *, que_se_sube=None, quien_sube=None,
                           sin_tildes=False):
    """Seccion del enunciado: plazo unico, que se sube, enlace obligatorio y sustentacion."""
    f = _sin_tildes if sin_tildes else str
    h2(doc, f(titulo))
    bullets(doc, [f(x) for x in [
        "@@Plazo único:@@ " + PLAZO + ", en " + _plat() + ".",
        "@@Qué se sube:@@ " + (que_se_sube or ZIP) + ".",
        "@@Enlace obligatorio:@@ junto al .zip va " + ENLACE + ".",
        quien_sube or ("@@Cada integrante sube la entrega del equipo@@ desde su propia "
                       "cuenta: el mismo .zip y el mismo enlace; una sola entrega por "
                       "estudiante."),
        "@@Sustentación:@@ " + sustentacion,
    ]])


def modalidad_equipo(doc, *, sin_tildes=False):
    """Recuadro de modalidad al comienzo del enunciado: que nadie lo lea como individual."""
    f = _sin_tildes if sin_tildes else str
    para(doc, f("@@Modalidad: " + EQUIPO + ".@@ Este semestre el proyecto no es individual: lo "
                "construye el equipo completo y lo sustentan todos sus integrantes."),
         shade="FFF8D6", space_after=8)


def entrega_docente(doc, sustentacion, *, quien_sube=None):
    """Lo mismo, en la guia docente: para responder dudas sin abrir el enunciado."""
    h2(doc, "Entrega y sustentación (común a los cinco cursos)")
    bullets(doc, [
        "Plazo único en ExamLab: " + PLAZO + ".",
        "Se sube " + ZIP + ", y " + ENLACE + " (obligatorio).",
        quien_sube or ("En equipo de 4 a 5 integrantes (máximo 5). Cada integrante sube el "
                       ".zip del equipo desde su cuenta: una entrega por estudiante."),
        "Sustentación: " + sustentacion,
    ])


def _shade(paragraph, fill: str) -> None:
    pPr = paragraph._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), fill)
    pPr.append(shd)


def _run(run, *, size=11, bold=False, color=GRIS, name=FONT):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold
    run.font.color.rgb = color


def _run_inline(p, text, *, size=11, bold=False, color=GRIS):
    """Soporta el marcador @@negrita@@ (convencion del workspace): parte el texto
    en runs y fuerza negrita solo en los tramos marcados.

    Los `code spans` de Markdown pasan a «comillas angulares»: el .docx no es Markdown
    y los acentos graves salian impresos tal cual en el enunciado del estudiante."""
    text = re.sub(r'`([^`\n]+)`', r'«\1»', str(text))
    for part in re.split(r'(@@.*?@@)', text):
        if not part:
            continue
        r = p.add_run()
        if part.startswith('@@') and part.endswith('@@'):
            r.text = part[2:-2]
            _run(r, size=size, bold=True, color=color)
        else:
            r.text = part
            _run(r, size=size, bold=bold, color=color)


def para(doc, text, *, size=11, bold=False, color=GRIS, align=WD_ALIGN_PARAGRAPH.LEFT,
         space_after=6, space_before=0, shade=None):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    if shade:
        _shade(p, shade)
    _run_inline(p, text, size=size, bold=bold, color=color)
    return p


def banda(doc, text):
    return para(doc, f"  {text}", size=13, bold=True, color=BLANCO, shade="095292",
                space_before=10, space_after=8)


def h2(doc, text):
    return para(doc, text, size=12, bold=True, color=AZUL, space_before=12, space_after=6)


def h3(doc, text):
    return para(doc, text, size=11, bold=True, color=CIAN, space_before=8, space_after=4)


def bullets(doc, items):
    for it in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(2)
        _run_inline(p, it, size=11, color=GRIS)


def table(doc, headers, rows):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = "Table Grid"
    for i, h in enumerate(headers):
        cell = t.rows[0].cells[i]
        cell.text = ""
        p = cell.paragraphs[0]
        r = p.add_run(h)
        _run(r, size=10, bold=True, color=BLANCO)
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:fill"), "095292")
        cell._tc.get_or_add_tcPr().append(shd)
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = t.rows[ri + 1].cells[ci]
            cell.text = ""
            p = cell.paragraphs[0]
            r = p.add_run(val)
            _run(r, size=10, color=GRIS)
            if ri % 2 == 1:
                shd = OxmlElement("w:shd")
                shd.set(qn("w:val"), "clear")
                shd.set(qn("w:fill"), "F2F2F2")
                cell._tc.get_or_add_tcPr().append(shd)
    para(doc, "", space_after=4)


def margins(doc):
    for s in doc.sections:
        s.top_margin = Inches(0.7)
        s.bottom_margin = Inches(0.7)
        s.left_margin = Inches(0.85)
        s.right_margin = Inches(0.85)


def portada_estudiante(doc, meta):
    para(doc, "Institución Universitaria Antonio José Camacho — UNIAJC",
         size=10, bold=True, color=AZUL, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    para(doc, "Facultad de Ingenierías · Programa de Ingeniería de Sistemas",
         size=10, color=GRIS, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
    banda(doc, meta["titulo"])
    para(doc, meta["asignatura"], size=14, bold=True, color=AZUL,
         align=WD_ALIGN_PARAGRAPH.CENTER, space_before=8)
    para(doc, f"Código {meta['codigo']}  ·  Grupo {meta['grupo']}  ·  Periodo {meta['periodo']}",
         size=11, bold=True, color=GRIS, align=WD_ALIGN_PARAGRAPH.CENTER)
    para(doc, f"Horario: {meta['horario']}  ·  Modalidad: "
              f"{meta.get('modalidad_texto', 'Virtual (sesiones por Meet)')}",
         size=11, color=GRIS, align=WD_ALIGN_PARAGRAPH.CENTER)
    para(doc, f"Docente: {DOCENTE}  ·  {CORREO}",
         size=10, color=GRIS, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    para(doc, "Versión estudiante — Entrega final en %s: %s" % (_plat(), PLAZO_CORTO),
         size=10, bold=True, color=AZUL, align=WD_ALIGN_PARAGRAPH.CENTER,
         shade="E8F4FA", space_after=4)
    para(doc, "Proyecto " + EQUIPO + " — no es individual",
         size=11, bold=True, color=AZUL, align=WD_ALIGN_PARAGRAPH.CENTER,
         shade="FFF8D6", space_after=10)


def portada_docente(doc, meta):
    para(doc, "Institución Universitaria Antonio José Camacho — UNIAJC",
         size=10, bold=True, color=AZUL, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    banda(doc, meta["titulo_docente"])
    para(doc, meta["asignatura"], size=13, bold=True, color=AZUL,
         align=WD_ALIGN_PARAGRAPH.CENTER, space_before=8)
    para(doc, f"{meta['codigo']} · Grupo {meta['grupo']} · {meta['periodo']}",
         size=11, bold=True, color=GRIS, align=WD_ALIGN_PARAGRAPH.CENTER)
    para(doc, "DOCUMENTO DOCENTE — No distribuir a estudiantes. Incluye rúbrica e hitos.",
         size=10, bold=True, color=ROJO, align=WD_ALIGN_PARAGRAPH.CENTER,
         shade="FBE4E4", space_after=10)


# ---------------------------------------------------------------------------
# BD II — VetCare DB
# ---------------------------------------------------------------------------

BD2_META = {
    "titulo": "Proyecto Integrador 2026-2 — VetCare DB",
    "titulo_docente": "Guía docente · Proyecto Integrador — Bases de Datos II",
    "asignatura": "Bases de Datos II",
    "codigo": "FI303215",
    "grupo": "641A-2",
    "periodo": "2026-2",
    "horario": "Lunes 18:00–20:00 (120 min)",
    "dominio": "VetCare DB",
    "caso_huellitas": True,
}


def enunciado_bd2(doc):
    portada_estudiante(doc, BD2_META)

    h2(doc, "1. Propósito")
    para(doc,
         "Diseñar, administrar y optimizar una base de datos relacional avanzada para "
         "VetCare DB, el sistema de la Clínica Veterinaria «Huellitas», integrando "
         "seguridad/respaldo, objetos "
         "programables (procedimientos, funciones y disparadores), optimización e "
         "integración conceptual con una aplicación externa. Hilo conductor ABPr del curso.")
    para(doc,
         "Peso: 20% del Corte 3 (Acuerdo pedagógico). El Parcial 3 (15%) y la asistencia "
         "(5%) se evalúan por separado.")
    modalidad_equipo(doc)

    h2(doc, "2. Contexto del cliente y dominio — VetCare DB")
    para(doc, CONTEXTO_VETCARE)
    para(doc,
         "@@Nomenclatura:@@ «Huellitas» es la clínica, es decir el cliente que tiene el "
         "problema; @@VetCare DB@@ es la base de datos que usted construye para ella. "
         "Los enunciados de los talleres en ExamLab usan estos mismos dos nombres.")
    para(doc,
         "@@Anexo obligatorio:@@ el caso completo —perfil de la clínica, las 8 entidades, las 3 "
         "reglas de negocio, el elenco de nombres y cómo crece la base durante el semestre— está "
         "en @@Anexo - Caso de estudio Clinica Huellitas@@, en esta misma carpeta. Téngalo a mano "
         "en todas las clases: los talleres se refieren a esos datos.",
         shade="E8F4FA")
    h3(doc, "Qué le toca a Bases de Datos II")
    para(doc,
         "Usted modela y opera la @@capa de datos@@ de VetCare: mascotas, dueños, "
         "veterinarios, citas, historial clínico, insumos/medicamentos y facturación "
         "básica. No se exige la aplicación ni la interfaz gráfica: eso es el alcance de "
         "Programación II sobre el mismo cliente.")
    bullets(doc, [
        "Entidades mínimas sugeridas: Dueño, Mascota, Veterinario, Cita, Consulta/Historial, "
        "Insumo/Medicamento, DetalleFactura (ajuste el modelo con justificación).",
        "Reglas de negocio: no citar mascotas inactivas; stock de insumos no negativo; "
        "auditoría de cambios sensibles (precios, cancelaciones).",
        "Puede ampliar el dominio con 1–2 módulos propios si mantiene coherencia.",
    ])

    h2(doc, "3. Entregables obligatorios")
    bullets(doc, [
        "Modelo de datos: diagrama ER (draw.io / diagrams.net o Excalidraw) + script DDL.",
        "Administración y seguridad: roles/usuarios (o plan de privilegios), política de "
        "respaldo/recuperación documentada.",
        "Objetos programables: ≥2 procedimientos, ≥1 función, ≥2 disparadores con casos de prueba.",
        "Optimización: ≥2 consultas «antes/después» con justificación de índices o reescritura.",
        "Integración: propuesta de cómo una app (API/cliente) consumiría la BD "
        "(contrato de operaciones + ejemplo SQL o pseudocódigo de llamada a procedimientos).",
        "Informe breve (PDF o DOCX) + carpeta de scripts SQL + diagrama exportado (PNG/SVG), "
        "todo dentro del .zip de la entrega (sección 9).",
        "Sustentación en vivo en la última clase: " + SUSTENTACION + ".",
    ])

    h2(doc, "4. Hitos y fechas orientativas (Plan 2026-2)")
    table(doc,
          ["Hito", "Sesión", "Fecha", "Qué entregar / hacer"],
          [
              ["Arranque (opcional)", "Sesiones 1–5", "ago–sep",
               "Definir dominio, borrador ER y alcance"],
              ["Construcción", "Sesiones 6–9", "sep–oct",
               "DDL, seguridad, procs/triggers, tuning"],
              ["Avance PI + integración", "Sesión 10 (doble · Clases 11+12)", "26/10/2026",
               "Demo parcial + checklist · contrato app ↔ BD y pruebas "
               "(cierre: domingo 01/11, 11:59 p. m.)"],
              ["Casos reales", "Sesión 11 (autónoma · Clase 13)", "02/11/2026",
               "Aplicar el análisis de casos al PI (cierre: domingo 08/11, 11:59 p. m.)"],
              ["Parcial 3", "Sesión 12 (Clase 14)", "09/11/2026",
               "Día de parcial = solo evaluación (virtual síncrona por Meet); el ensayo y la "
               "preparación fueron en la Sesión 10 (Clase 12)"],
              ["Entrega final del PI", "—", "15/11/2026",
               "Plazo único en ExamLab: domingo, 11:59 p. m. Un .zip + el enlace al "
               "repositorio o a la carpeta de Drive"],
              ["Sustentación / cierre", "Sesión 13 (Clase 15)", "16/11/2026",
               "Defensa en vivo del PI (15 min + 5 de preguntas) + cierre del curso"],
          ])
    para(doc,
         "Nota: la sesión 13 (16/11) cae en festivo, pero por decisión docente es la "
         "sesión de sustentaciones: no es autónoma y no es parcial. El Parcial 3 es el "
         "09/11 (sesión 12 · material Clase 14). El paquete final se sube a ExamLab a más "
         "tardar el domingo 15/11, 11:59 p. m.; el 16/11 solo se defiende.")

    h2(doc, "5. Herramientas (gratis + navegador)")
    bullets(doc, [
        "SQL: DB Fiddle, OneCompiler SQL, SQLTest.online o RunSQL.",
        "Procedimientos / PL-SQL: Oracle Live SQL (cuenta free, sin tarjeta).",
        "Diagramas: draw.io / diagrams.net · Excalidraw.",
        "Entrega: documentos en Google Docs/Drive o Word Online, dentro del .zip que se sube "
        "a ExamLab.",
    ])
    para(doc,
         "No se exige instalar Oracle/MySQL/PostgreSQL/SQL Server ni Docker en el PC. "
         "No se pide cloud IaaS con tarjeta.",
         shade="FFF8D6", space_after=8)

    h2(doc, "6. Criterios de evaluación (rúbrica resumida — 100 pts → 20% del corte)")
    table(doc,
          ["Criterio", "Pts", "Evidencia"],
          [
              ["Modelo + DDL coherente", "20", "ER + scripts ejecutables"],
              ["Seguridad y respaldo", "15", "Roles/privilegios + plan backup"],
              ["Procs / funciones / triggers", "25", "Código + pruebas"],
              ["Optimización", "15", "Antes/después + justificación"],
              ["Integración app ↔ BD", "10", "Contrato + ejemplos"],
              ["Informe + sustentación", "15", "Claridad, demo, respuestas"],
          ])

    h2(doc, "7. Modalidad de trabajo")
    bullets(doc, [
        "@@En equipo, no individual:@@ equipos de 4 a 5 integrantes (máximo 5).",
        "Todo el equipo trabaja el proyecto completo: en la sustentación hablan todos, y "
        "cualquier integrante debe poder explicar cualquier parte (las preguntas van al azar).",
        "Cada integrante sube la entrega del equipo en ExamLab desde su propia cuenta "
        "(sección 9).",
    ])

    h2(doc, "8. Qué NO es este proyecto")
    bullets(doc, [
        "No sustituye el Parcial 3 (evaluación síncrona por Meet del 09/11).",
        "No es una app GUI completa: el foco es la capa de datos avanzada.",
        "No se copia un enunciado de otra institución: el dominio es VetCare DB UNIAJC.",
    ])

    entrega_y_sustentacion(
        doc, "9. Entrega y sustentación",
        "lunes 16/11/2026, en la última clase (sesión 13; es festivo, pero sí hay clase), "
        "por Meet: " + SUSTENTACION + ".")


def guia_bd2(doc):
    portada_docente(doc, BD2_META)
    h2(doc, "Contexto")
    para(doc,
         "Patrón heredado de Prog. II / Seminario: PI continuo ABPr, 20% Corte 3. "
         "Enunciados viejos viven como .gdoc en Clase 1; aquí se materializa en "
         "Clases/Proyecto Integrador/ (estudiante) + Kit docente/Proyecto Integrador/.")
    h2(doc, "Alineación RAA")
    bullets(doc, [
        "RAA1 Seguridad y respaldo → roles, privilegios, plan de backup/restore.",
        "RAA2 Procedimientos y disparadores → procs, funciones, triggers con pruebas.",
        "RAA3 Optimización → índices, reescritura, evidencia antes/después.",
    ])
    h2(doc, "Hitos docentes (sesiones del calendario · 13 sesiones)")
    table(doc,
          ["Sesión", "Fecha", "Material", "Rol docente"],
          [
              ["10 (doble)", "26/10", "Clases 11+12",
               "Revisión de avance con checklist viva + empujar integración app↔BD "
               "y casos de prueba en el mismo bloque"],
              ["11 (autónoma)", "02/11", "Clase 13",
               "Publicar el caso real y revisar la entrega asíncrona (dom 08/11)"],
              ["12", "09/11", "Clase 14",
               "Parcial 3 (virtual síncrona · solo evaluación: el ensayo fue en la sesión 10)"],
              ["—", "15/11", "—",
               "Cierra la entrega en ExamLab (domingo, 11:59 p. m.): cada integrante sube el "
               ".zip + enlace del equipo"],
              ["13", "16/11", "Clase 15",
               "Sesión síncrona de sustentaciones: turnos de 20 min (15 + 5), preguntas y cierre"],
          ])
    entrega_docente(doc, "lunes 16/11 (festivo, sí hay clase), por Meet: " + SUSTENTACION + ".")
    h2(doc, "Rúbrica detallada (calificar sobre 100 → escala a 20% del corte)")
    bullets(doc, [
        "Modelo/DDL (20): normalización razonable, FK, constraints, nombres claros.",
        "Seguridad/respaldo (15): al menos 2 roles con privilegios distintos; RPO/RTO "
        "en lenguaje simple; procedimiento de restore descrito.",
        "Programables (25): triggers de auditoría o integridad; procs de negocio "
        "(agendar cita, registrar consulta, descontar stock).",
        "Optimización (15): EXPLAIN o narrativa equivalente en playground; índices justificados.",
        "Integración (10): operaciones CRUD vía procs; no hace falta desplegar API real.",
        "Informe+sustentación (15): 15 min de exposición + 5 de preguntas; preguntas cruzadas "
        "al azar sobre cualquier parte del trabajo.",
    ])
    h2(doc, "Evidencias a pedir")
    bullets(doc, [
        "El .zip (scripts .sql, diagrama, informe, capturas) Y el enlace al repositorio o a la "
        "carpeta de Drive: los dos son obligatorios.",
        "Capturas de ejecución en Live SQL / DB Fiddle.",
        "Reparto del guion por bloques temáticos y quién del equipo presenta qué.",
    ])
    h2(doc, "Post-clase Padlet")
    para(doc, "Si usó Padlet en Clase 1: ⋯ → Clear posts → código → Delete (reutilizar cupo gratis).")


# ---------------------------------------------------------------------------
# Arquitectura — CloudLite App
# ---------------------------------------------------------------------------

ARQ_META = {
    "titulo": "Proyecto Integrador 2026-2 — CloudLite App",
    "titulo_docente": "Guía docente · Proyecto Integrador — Arquitectura de Sistemas",
    "asignatura": "Arquitectura de Sistemas Computacionales",
    "codigo": "FI303380",
    "grupo": "6303C",
    "periodo": "2026-2",
    "horario": "Lunes 10:00–12:00 (120 min)",
    "dominio": "CloudLite App",
    # La parte practica de Arquitectura no nombra la plataforma: el estudiante ya sabe cual
    # es y como entrar —eso va en el correo de bienvenida—. Los demas cursos si la nombran.
    "plataforma": "la plataforma del curso",
}


def enunciado_arq(doc):
    portada_estudiante(doc, ARQ_META)

    h2(doc, "1. Propósito")
    para(doc,
         "Diseñar y simular el despliegue de una arquitectura cloud para CloudLite App "
         "(aplicación web/API de un dominio realista a su elección: citas, academia, "
         "inventario liviano, etc.). Integra diagramas, contenedores en lab de navegador "
         "y CI/CD conceptual con GitHub Actions — sin cloud de pago ni tarjeta.")
    para(doc,
         "Peso: 20% del Corte 3 (Acuerdo pedagógico). El Parcial 3 (15%) y la asistencia "
         "(5%) se evalúan por separado.")
    modalidad_equipo(doc)

    h2(doc, "2. Alcance de CloudLite App")
    bullets(doc, [
        "Elegir un dominio concreto y justificar 3–5 capacidades funcionales.",
        "Decidir modelo de servicio dominante (IaaS / PaaS / SaaS) y por qué.",
        "Arquitectura lógica + de despliegue (capas, componentes, red, almacenamiento).",
        "Contenedorización de al menos un servicio (demo en LabEx Docker Playground o Killercoda).",
        "Pipeline CI/CD conceptual (GitHub Actions): build + test + artefactos (sin runner de pago).",
        "Seguridad, monitoreo, costos/sostenibilidad y escalabilidad (al menos un escenario).",
    ])

    h2(doc, "3. Entregables obligatorios")
    bullets(doc, [
        "Documento de arquitectura (PDF/DOCX): contexto, ADRs breves, riesgos, costos estimados "
        "en lenguaje cualitativo (bajo/medio — sin factura real).",
        "Diagramas (draw.io / diagrams.net): al menos (a) componentes/C4-lite, (b) despliegue, "
        "(c) flujo CI/CD.",
        "Lab de contenedores: Dockerfile o compose mínimo + captura/enlace de sesión "
        "LabEx Docker Playground o Killercoda.",
        "Repo o carpeta con workflow GitHub Actions (.yml) que compile/pruebe un stub "
        "(aunque el «deploy» sea simulado).",
        "Sustentación en vivo en la última clase: " + SUSTENTACION + ", con demo de "
        "diagrama + lab.",
    ])

    h2(doc, "4. Hitos y fechas orientativas (Plan 2026-2)")
    table(doc,
          ["Hito", "Sesión", "Fecha", "Qué entregar / hacer"],
          [
              ["Fundamentos", "Sesiones 1–5", "ago–sep",
               "Dominio, IaaS/PaaS/SaaS, boceto C4"],
              ["Profundización", "Sesiones 6–9", "sep–oct",
               "Seguridad, redes, monitoreo, CI/CD"],
              ["Avance PI + rendimiento", "Sesión 10 (doble · Clases 11+12)", "26/10/2026",
               "Diagramas v1 + checklist · escenario de prueba y métricas objetivo "
               "(cierre: domingo 01/11, 11:59 p. m.)"],
              ["Escalabilidad", "Sesión 11 (autónoma · Clase 13)", "02/11/2026",
               "Sección de autoescalado del informe (cierre: domingo 08/11, 11:59 p. m.)"],
              ["Parcial 3", "Sesión 12 (Clase 14)", "09/11/2026",
               "Día de parcial = solo evaluación (virtual síncrona por Meet); el ensayo y la "
               "preparación fueron en la Sesión 10 (Clase 12)"],
              ["Entrega final del PI", "—", "15/11/2026",
               "Plazo único: domingo, 11:59 p. m. Un .zip + el enlace al repositorio o a la "
               "carpeta de Drive"],
              ["Sustentación / cierre", "Sesión 13 (Clase 15)", "16/11/2026",
               "Defensa en vivo del PI CloudLite (15 min + 5 de preguntas) + cierre del curso"],
          ])
    para(doc,
         "Nota: la sesión 13 (16/11) cae en festivo, pero por decisión docente es la "
         "sesión de sustentaciones: no es autónoma y no es parcial. El Parcial 3 es el "
         "09/11 (sesión 12 · material Clase 14).")

    h2(doc, "5. Herramientas (gratis + navegador)")
    bullets(doc, [
        "Diagramas: draw.io / diagrams.net · Excalidraw.",
        "Contenedores: LabEx Docker Playground · Killercoda (sin Docker Desktop obligatorio).",
        "CI/CD: GitHub Actions (cuenta free) — pipelines simples.",
        "Entrega: documento propio, dentro del .zip que se sube a %s." % _plat(),
    ])
    para(doc,
         "Prohibido como requisito: AWS/GCP/Oracle Cloud/Azure Free Tier con tarjeta; "
         "instalar VirtualBox/VMware/Docker Desktop/WSL; software de modelado de pago.",
         shade="FBE4E4", space_after=8)

    h2(doc, "6. Criterios de evaluación (rúbrica resumida — 100 pts → 20% del corte)")
    table(doc,
          ["Criterio", "Pts", "Evidencia"],
          [
              ["Dominio + decisión IaaS/PaaS/SaaS", "15", "Justificación clara"],
              ["Diagramas de arquitectura", "25", "Componentes + despliegue"],
              ["Contenedores (lab navegador)", "20", "Dockerfile/compose + captura"],
              ["CI/CD conceptual", "15", "Workflow .yml + explicación"],
              ["Seguridad / costos / escalabilidad", "10", "Sección en informe"],
              ["Informe + sustentación", "15", "Claridad, demo, respuestas"],
          ])

    h2(doc, "7. Modalidad de trabajo")
    bullets(doc, [
        "@@En equipo, no individual:@@ equipos de 4 a 5 integrantes (máximo 5).",
        "Todo el equipo trabaja el proyecto completo: en la sustentación hablan todos, y "
        "cualquier integrante debe poder explicar los diagramas y el workflow CI/CD.",
        "Cada integrante sube la entrega del equipo desde su propia cuenta (sección 9).",
    ])

    h2(doc, "8. Qué NO es este proyecto")
    bullets(doc, [
        "No sustituye el Parcial 3 (09/11, virtual síncrona por Meet).",
        "No exige cuenta cloud de pago ni gastos del estudiante.",
        "No se pide producción real en Internet: el foco es diseño + simulación en labs gratis.",
    ])

    entrega_y_sustentacion(
        doc, "9. Entrega y sustentación",
        "lunes 16/11/2026, en la última clase (sesión 13; es festivo, pero sí hay clase), "
        "por Meet: " + SUSTENTACION + ".")


def guia_arq(doc):
    portada_docente(doc, ARQ_META)
    h2(doc, "Contexto")
    para(doc,
         "Mismo patrón de peso (20% Corte 3) que Prog. II / Seminario. Enfoque microcurrículo: "
         "arquitecturas cloud, virtualización/contenedores, seguridad, rendimiento y sostenibilidad.")
    h2(doc, "Alineación RAA")
    bullets(doc, [
        "RAA1 IaaS/PaaS/SaaS → decisión de modelo de servicio en el informe.",
        "RAA2 Virtualización y distribuidos → contenedores + diagrama de despliegue.",
        "RAA3 Seguridad, rendimiento y sostenibilidad → secciones explícitas + escenario de escala.",
    ])
    h2(doc, "Hitos docentes (sesiones del calendario · 13 sesiones)")
    table(doc,
          ["Sesión", "Fecha", "Material", "Rol docente"],
          [
              ["10 (doble)", "26/10", "Clases 11+12",
               "Revisar diagramas v1 y bloquear dominios demasiado amplios + "
               "métricas/pruebas de rendimiento en el mismo bloque"],
              ["11 (autónoma)", "02/11", "Clase 13",
               "Publicar el ejercicio de autoescalado y revisar la entrega (dom 08/11)"],
              ["12", "09/11", "Clase 14",
               "Parcial 3 (solo evaluación: el ensayo de la sustentación fue en la sesión 10)"],
              ["—", "15/11", "—",
               "Cierra la entrega en ExamLab (domingo, 11:59 p. m.): cada integrante sube el "
               ".zip + enlace del equipo"],
              ["13", "16/11", "Clase 15",
               "Sesión síncrona de sustentaciones: turnos de 20 min (15 + 5), preguntas y cierre"],
          ])
    entrega_docente(doc, "lunes 16/11 (festivo, sí hay clase), por Meet: " + SUSTENTACION + ".")
    h2(doc, "Rúbrica detallada")
    bullets(doc, [
        "Dominio/servicio (15): problema real, límites claros, no «todo AWS».",
        "Diagramas (25): legibles, convenciones, separación de concerns.",
        "Contenedores (20): lab reproducible; si el lab caduca, capturas + Dockerfile bastan.",
        "CI/CD (15): stages claros; deploy puede ser «echo/simulate».",
        "Seguridad/costos/escala (10): amenazas básicas, estimación cualitativa, autoescalado conceptual.",
        "Sustentación (15): 15 min de exposición + 5 de preguntas al azar a cualquier "
        "integrante sobre cualquier parte; penalizar que hable solo uno.",
    ])
    h2(doc, "Evidencias")
    bullets(doc, [
        "El .zip (con .yml, Dockerfile, diagramas PNG, informe) Y el enlace al repo GitHub o a "
        "la carpeta de Drive: los dos son obligatorios.",
        "Enlace Killercoda/LabEx o capturas con timestamp.",
    ])


# ---------------------------------------------------------------------------
# Programacion II y Seminario de Sistemas — VetCare (PI COMPARTIDO)
#
# Los dos cursos trabajan el MISMO producto: el sistema de la Clinica Veterinaria
# "Huellitas". Prog II construye el software; Seminario disena los planos. Por eso
# el enunciado contempla tres casos segun la matricula del estudiante (A/B/C):
# un estudiante puede estar en ambos cursos, o en uno solo, y no puede quedar
# bloqueado por lo que se hace en el otro.
#
# Contenido heredado de los enunciados originales del docente (que vivian sueltos
# como .gdoc: el de Prog II en Kit docente y el de Seminario dentro de Clase 1).
# ---------------------------------------------------------------------------

CASOS_MATRICULA = [
    "@@Caso A — cursa AMBAS materias (modo full stack):@@ trabaja sobre un unico "
    "VetCare. En Programacion II se califica la calidad del codigo Java; en Seminario, la "
    "calidad de los diagramas y la documentacion de ESE mismo sistema.",
    "@@Caso B — solo Programacion II (modo developer):@@ el docente le entrega los diagramas "
    "UML ya hechos. Su mision es traducir esos planos a codigo Java funcional.",
    "@@Caso C — solo Seminario (modo arquitecto/QA):@@ se encarga del diseno y el plan de "
    "pruebas. Para validar su diseno entrega un prototipo navegable (mockup) o un prototipo "
    "minimo en consola; no se le exige software con interfaz grafica.",
]

PROG2_META = {
    "titulo": "Proyecto Integrador 2026-2 — VetCare (aplicacion Java)",
    "titulo_docente": "Guia docente · Proyecto Integrador — Programacion II",
    "asignatura": "Programacion II",
    "codigo": "FI303204",
    "grupo": "341C",
    "periodo": "2026-2",
    "horario": "Miercoles 18:00–20:00 (120 min)",
    "dominio": "VetCare",
}

SEMIN_META = {
    "titulo": "Proyecto Integrador 2026-2 — VetCare (arquitectura y diseno)",
    "titulo_docente": "Guia docente · Proyecto Integrador — Seminario de Sistemas",
    "asignatura": "Seminario de Sistemas",
    "codigo": "FI303301",
    "grupo": "341C",
    "periodo": "2026-2",
    "horario": "Jueves 18:00–20:00 (120 min)",
    "dominio": "VetCare",
}


def enunciado_prog2(doc):
    portada_estudiante(doc, PROG2_META)

    h2(doc, "1. Proposito")
    para(doc,
         "Construir en Java la aplicacion de escritorio VetCare para la clinica veterinaria "
         "«Huellitas», aplicando los pilares de la POO, estructuras de datos, interfaz grafica, "
         "manejo de errores y persistencia. Es el hilo conductor ABPr del curso: cada clase "
         "aporta una pieza del mismo producto, no ejercicios sueltos.")
    para(doc,
         "Peso: 20% del Corte 3 (Acuerdo pedagogico). El Parcial 3 (15%) y la asistencia (5%) "
         "se evaluan por separado.")
    modalidad_equipo(doc, sin_tildes=True)

    h2(doc, "2. Contexto del cliente")
    para(doc, CONTEXTO_VETCARE)
    h3(doc, "El sistema debe permitir, como minimo")
    bullets(doc, [
        "Registrar duenos (clientes) y sus mascotas (pacientes).",
        "Agendar citas medicas.",
        "Guardar un historial clinico basico por mascota.",
        "Buscar rapidamente el expediente de un animal por su identificador.",
        "Conservar la informacion aunque se cierre el programa.",
    ])

    h2(doc, "3. Requisitos tecnicos obligatorios")
    bullets(doc, [
        "@@Pilares de POO:@@ clases del dominio (Mascota, Dueno, Cita), objetos, "
        "encapsulamiento y herencia usados con criterio, no decorativos.",
        "@@Estructuras de datos:@@ colecciones de Java (List / Map) para gestionar los "
        "registros en memoria.",
        "@@Interfaz grafica:@@ ventanas funcionales con Swing o JavaFX.",
        "@@Manejo de errores:@@ bloques try-catch que eviten que el programa se cierre "
        "(ej.: el usuario escribe texto donde va la edad de la mascota).",
        "@@Persistencia:@@ guardar y leer desde archivos .txt o .csv para no perder datos "
        "al cerrar la aplicacion.",
    ])

    h2(doc, "4. Como se conecta con Seminario de Sistemas")
    para(doc,
         "VetCare es el MISMO producto en las dos asignaturas: aqui se construye el software, "
         "en Seminario se disenan los planos (requisitos, UML, pruebas, manuales). Su "
         "situacion depende de su matricula:")
    bullets(doc, CASOS_MATRICULA)

    h2(doc, "5. Hitos de entrega")
    table(doc,
          ["Sesion (material)", "Fecha", "Que se entrega"],
          [
              ["S10 (doble · Clases 11+12)", "28/10",
               "Avance de codigo + revision cruzada e integracion de modulos: "
               "la aplicacion corre de punta a punta"],
              ["S11 (Clase 13)", "04/11", "Manejo de excepciones y validaciones incorporado"],
              ["S12 (Clase 14)", "11/11", "Version final + ensayo de la presentacion"],
              ["Plazo unico", "dom 15/11",
               "Entrega final en ExamLab hasta las 11:59 p. m.: un .zip + el enlace al repositorio"],
              ["S13 (Clase 15)", "18/11",
               "Sustentacion final: 15 min + 5 de preguntas (mismo dia del Parcial 3)"],
          ])

    h2(doc, "6. Entregables finales")
    bullets(doc, [
        "Codigo fuente del proyecto, dentro del .zip; ademas, el enlace al repositorio "
        "(obligatorio, seccion 8).",
        "Archivo de datos de ejemplo (.txt o .csv) con registros de prueba.",
        "Manual de usuario breve (1-2 paginas) con capturas de la interfaz.",
        "Sustentacion: 15 minutos de exposicion + 5 de preguntas por equipo, turno de 20 "
        "minutos; participan todos los integrantes.",
    ])

    h2(doc, "7. Criterios de evaluacion (100 puntos)")
    table(doc,
          ["Criterio", "Pts", "Que se mira"],
          [
              ["POO", "20", "Clases del dominio bien modeladas; encapsulamiento y herencia con proposito"],
              ["Estructuras de datos", "15", "Coleccion adecuada al caso y justificada"],
              ["Interfaz grafica", "20", "Ventanas funcionales; el usuario puede completar las tareas"],
              ["Manejo de errores", "15", "La aplicacion no se cae ante entradas invalidas"],
              ["Persistencia", "15", "Los datos sobreviven al cierre del programa"],
              ["Sustentacion", "15", "Se pregunta al azar a cualquier integrante sobre cualquier parte"],
          ])

    entrega_y_sustentacion(
        doc, "8. Entrega y sustentacion",
        "miercoles 18/11/2026, en la ultima clase (sesion 13, mismo dia del Parcial 3), por "
        "Meet: " + SUSTENTACION + ".", sin_tildes=True)


def guia_prog2(doc):
    portada_docente(doc, PROG2_META)
    h2(doc, "Contexto")
    para(doc,
         "PI compartido con Seminario de Sistemas: mismo producto VetCare, distinto entregable. "
         "El enunciado original vivia suelto como .gdoc en Kit docente; ahora el documento del "
         "estudiante vive en Clases/Proyecto Integrador/ y esta guia en Kit docente/.")
    h2(doc, "Alineacion RAA")
    bullets(doc, [
        "RAA1 Estructuras de datos → colecciones para registros de VetCare.",
        "RAA2 Eventos y componentes graficos → interfaz Swing/JavaFX funcional.",
        "RAA3 Patrones de diseno → organizacion del codigo, separacion de responsabilidades.",
    ])
    h2(doc, "Los tres casos de matricula (lo que mas dudas genera)")
    bullets(doc, [
        "Caso A (ambas materias): NO calificar dos veces lo mismo. Aqui se califica el codigo; "
        "los diagramas se califican en Seminario.",
        "Caso B (solo Prog II): usted les entrega los diagramas UML ya hechos. Tenga listo un "
        "juego de diagramas base de VetCare para repartir en Clase 11.",
        "Caso C (solo Seminario): no aparece en este curso, pero si un estudiante pregunta, "
        "sepa que alla entrega mockup/prototipo, no codigo con interfaz.",
    ])
    h2(doc, "Hitos docentes")
    table(doc,
          ["Sesion (material)", "Fecha", "Rol docente"],
          [
              ["S10 (doble · Clases 11+12)", "28/10",
               "Revision cruzada (cada estudiante lee el codigo de otro) y empujar la "
               "integracion; detectar trabajos con modulos sueltos"],
              ["S11 (Clase 13)", "04/11", "Verificar que las validaciones existan de verdad, no en el papel"],
              ["S12 (Clase 14)", "11/11", "Ensayo cronometrado de la sustentacion (15 + 5 min)"],
              ["Plazo", "dom 15/11",
               "Cierra la entrega en ExamLab (11:59 p. m.): cada integrante sube el .zip + "
               "enlace del equipo"],
              ["S13 (Clase 15)", "18/11",
               "Parcial 3 + sustentacion final en turnos de 20 min (15 + 5)"],
          ])
    h2(doc, "Errores frecuentes a vigilar")
    bullets(doc, [
        "Herencia forzada solo para «cumplir el requisito» (una clase Animal que nadie usa).",
        "GUI que se ve bien pero no guarda nada: pedir siempre la prueba de cerrar y reabrir.",
        "try-catch vacio que se traga el error sin avisar al usuario.",
        "Que uno solo del equipo haya programado todo: por eso las preguntas al azar a "
        "cualquier integrante en la sustentacion.",
    ])
    h2(doc, "Evidencias a pedir")
    bullets(doc, [
        "El .zip con el codigo fuente compilable Y el enlace al repositorio: los dos son "
        "obligatorios.",
        "Archivo .csv/.txt con datos de prueba.",
        "Captura de la aplicacion corriendo + manual breve.",
    ])
    entrega_docente(doc, "miercoles 18/11 (mismo dia del Parcial 3), por Meet: "
                    + SUSTENTACION + ".")


def enunciado_seminario(doc):
    portada_estudiante(doc, SEMIN_META)

    h2(doc, "1. Proposito")
    para(doc,
         "Disenar la arquitectura, los requisitos y la interfaz del sistema VetCare para la "
         "clinica veterinaria «Huellitas». Su rol en esta asignatura es de @@analista funcional "
         "y arquitecto de software@@: aqui no se construye la casa, se dibujan los planos para "
         "que cualquier equipo pueda construirla.")
    para(doc,
         "Peso: 20% del Corte 3 (Acuerdo pedagogico). El Parcial 3 (15%) y la asistencia (5%) "
         "se evaluan por separado.")
    modalidad_equipo(doc, sin_tildes=True)

    h2(doc, "2. Contexto del cliente")
    para(doc, CONTEXTO_VETCARE)
    h3(doc, "Requerimientos que el veterinario jefe pidio en la primera entrevista")
    bullets(doc, [
        "«Necesito registrar el ID, el nombre y la especie del animal que llega.»",
        "«Necesito buscar rapido el expediente de un animal usando solo su ID.»",
        "«Quiero ver una lista de quienes estan en la sala de espera.»",
        "«Tiene que ser muy facil de usar: no somos expertos en computadoras.»",
        "«La informacion no puede borrarse si se va la luz o apagamos el computador.»",
    ])
    para(doc,
         "Esas cinco frases son material crudo de entrevista, no requisitos formales. "
         "Convertirlas en RF/RNF bien escritos es parte del trabajo.")

    h2(doc, "3. Fases de entrega")
    table(doc,
          ["Fase", "Que produce"],
          [
              ["1. Ingenieria de requisitos",
               "Requisitos funcionales (RF) y no funcionales (RNF) formales y trazables"],
              ["2. Modelado UML",
               "Casos de uso, diagrama de clases del dominio y un diagrama dinamico "
               "(actividad o secuencia)"],
              ["3. Diseno de interfaz (UX/UI)",
               "Wireframes y mockup navegable de las pantallas (Figma, Penpot o Balsamiq)"],
              ["4. Arquitectura de datos",
               "Diccionario de datos y formato de almacenamiento (estructura del CSV o "
               "modelo entidad-relacion basico)"],
          ])

    h2(doc, "4. Como se conecta con Programacion II")
    para(doc,
         "VetCare es el MISMO producto en las dos asignaturas: aqui se disenan los planos y "
         "en Programacion II se construye el software. Su situacion depende de su matricula:")
    bullets(doc, CASOS_MATRICULA)
    para(doc,
         "@@Independencia curricular:@@ si NO cursa Programacion II, su proyecto termina con el "
         "documento de diseno y el prototipo visual navegable. No necesita escribir ni compilar "
         "codigo: su nota depende de la calidad, coherencia y profesionalismo de sus planos.",
         shade="E8F4FA")

    h2(doc, "5. Hitos de entrega")
    table(doc,
          ["Sesion (material)", "Fecha", "Que se entrega"],
          [
              ["S10 (doble · Clases 11+12)", "29/10",
               "Avance: requisitos (RF/RNF) + casos de uso y diagramas UML avanzados "
               "(clases + dinamico)"],
              ["S11 (Clase 13)", "05/11", "Diseno de interfaz: wireframes y mockup navegable"],
              ["S12 (Clase 14)", "12/11", "Documento consolidado + ensayo de la sustentacion"],
              ["Plazo unico", "dom 15/11",
               "Entrega final en ExamLab hasta las 11:59 p. m.: un .zip + el enlace a la carpeta "
               "o al repositorio"],
              ["S13 (Clase 15)", "19/11",
               "Sustentacion final: 15 min + 5 de preguntas (mismo dia del Parcial 3)"],
          ])

    h2(doc, "6. Entregables finales")
    bullets(doc, [
        "Documento de diseno de arquitectura con RF/RNF, UML y diccionario de datos.",
        "Mockup navegable (enlace o PDF exportado).",
        "Plan de pruebas: casos de prueba documentados sobre los requisitos.",
        "Sustentacion: 15 minutos de exposicion + 5 de preguntas por equipo, turno de 20 "
        "minutos; participan todos los integrantes.",
    ])

    h2(doc, "7. Criterios de evaluacion (100 puntos)")
    table(doc,
          ["Criterio", "Pts", "Que se mira"],
          [
              ["Requisitos", "20", "RF/RNF verificables y trazables al pedido del cliente"],
              ["Modelado UML", "25", "Diagramas coherentes entre si y con los requisitos"],
              ["Diseno de interfaz", "20", "Wireframes usables; el flujo se entiende sin explicacion"],
              ["Arquitectura de datos", "15", "Diccionario de datos completo y formato justificado"],
              ["Plan de pruebas", "10", "Casos de prueba que cubren los requisitos criticos"],
              ["Sustentacion", "10", "Se pregunta al azar a cualquier integrante sobre cualquier parte"],
          ])

    entrega_y_sustentacion(
        doc, "8. Entrega y sustentacion",
        "jueves 19/11/2026, en la ultima clase (sesion 13, mismo dia del Parcial 3), por "
        "Meet: " + SUSTENTACION + ".", sin_tildes=True)


def guia_seminario(doc):
    portada_docente(doc, SEMIN_META)
    h2(doc, "Contexto")
    para(doc,
         "PI compartido con Programacion II: mismo producto VetCare, distinto entregable. "
         "El enunciado original vivia suelto como .gdoc dentro de la carpeta de Clase 1; ahora "
         "el documento del estudiante vive en Clases/Proyecto Integrador/ y esta guia en Kit docente/.")
    h2(doc, "Alineacion RAA")
    bullets(doc, [
        "RAA1 Patrones y modularidad → organizacion del diseno, separacion de responsabilidades.",
        "RAA2 Documentacion y validacion → SDD, diccionario de datos, plan de pruebas.",
        "RAA3 Presentacion y sustentacion → defensa clara de las decisiones de diseno.",
    ])
    h2(doc, "Los tres casos de matricula (lo que mas dudas genera)")
    bullets(doc, [
        "Caso A (ambas materias): aqui se califican los planos; el codigo se califica en Prog II. "
        "No exigir codigo compilable en esta asignatura.",
        "Caso C (solo Seminario): cierra con SDD + mockup navegable. Es una ruta completa y "
        "valida, no una version reducida: dejarlo claro desde Clase 1 para que nadie se sienta "
        "en desventaja.",
        "Caso B (solo Prog II): no aparece aca; sus diagramas base los provee el docente en el "
        "otro curso. Mantener un juego de diagramas VetCare listo para repartir alla.",
    ])
    h2(doc, "Hitos docentes")
    table(doc,
          ["Sesion (material)", "Fecha", "Rol docente"],
          [
              ["S10 (doble · Clases 11+12)", "29/10",
               "Revisar que los RF sean verificables (no deseos vagos) y la coherencia "
               "entre casos de uso y diagrama de clases"],
              ["S11 (Clase 13)", "05/11", "Wireframes: exigir flujo completo de una tarea real"],
              ["S12 (Clase 14)", "12/11",
               "Consolidacion del documento + ensayo cronometrado (15 + 5 min)"],
              ["Plazo", "dom 15/11",
               "Cierra la entrega en ExamLab (11:59 p. m.): cada integrante sube el .zip + "
               "enlace del equipo"],
              ["S13 (Clase 15)", "19/11",
               "Parcial 3 + sustentacion final en turnos de 20 min (15 + 5)"],
          ])
    h2(doc, "Errores frecuentes a vigilar")
    bullets(doc, [
        "Requisitos no verificables («el sistema debe ser rapido») sin criterio medible.",
        "Diagrama de clases que no corresponde a los casos de uso entregados.",
        "Mockup bonito que no cubre el flujo critico (registrar → buscar → ver historial).",
        "Diccionario de datos sin tipos ni restricciones: queda inservible para quien programe.",
    ])
    h2(doc, "Evidencias a pedir")
    bullets(doc, [
        "Documento de diseno (PDF o DOCX) con RF/RNF, UML y diccionario de datos.",
        "Enlace al mockup navegable (Figma/Penpot) o PDF exportado.",
        "Plan de pruebas con casos trazados a requisitos.",
        "Todo dentro del .zip, Y el enlace a la carpeta de Drive o al repositorio: los dos son "
        "obligatorios.",
    ])
    entrega_docente(doc, "jueves 19/11 (mismo dia del Parcial 3), por Meet: "
                    + SUSTENTACION + ".")


# ---------------------------------------------------------------------------
# Markdown kits (fuente editable docente)
# ---------------------------------------------------------------------------

MD_BD2 = """# Guía docente — Proyecto Integrador · Bases de Datos II · 2026-2

**Privado docente** · No compartir en `Clases/`.

- **Curso:** Bases de Datos II (FI303215 · 641A-2)
- **Peso:** 20% Corte 3 (Acuerdo)
- **Dominio estudiante:** VetCare DB
- **Enunciado:** `Clases/Proyecto Integrador/Enunciado Proyecto Integrador - Bases de Datos II - 2026-2.docx`

## Hitos (Plan 2026-2 · semestre acortado a 13 sesiones)

Las carpetas de material siguen numeradas 1–15; lo que cambia es en qué sesión se dicta cada una.
Toda entrega intermedia cierra el **domingo siguiente a la sesión, a las 11:59 p. m.**

| Sesión | Fecha | Material | Foco | Cierre de entrega |
|---|---|---|---|---|
| S10 (doble) | 26/10/2026 | Clases 11 + 12 | Avance PI — checklist · Integración app ↔ BD · **preparación de la sustentación** | dom 01/11/2026, 11:59 p. m. |
| S11 (autónoma) | 02/11/2026 | Clase 13 | Análisis de casos reales aplicado al PI | dom 08/11/2026, 11:59 p. m. |
| S12 | 09/11/2026 | Clase 14 | **Parcial 3** (virtual síncrono por Meet · solo evaluación) | **paquete final:** dom 15/11/2026, 11:59 p. m. |
| S13 | 16/11/2026 | Clase 15 | **Sustentación en vivo del PI** (15 min + 5 de preguntas, turno de 20) + cierre (sesión síncrona) | — (el paquete ya está entregado) |

> S13 cae en festivo (Independencia de Cartagena), pero por decisión docente es sesión de
> sustentaciones: no es autónoma y no es parcial. El paquete final se sube a ExamLab a más
> tardar el **domingo 15/11/2026, 11:59 p. m.**; el 16/11 solo se defiende.

## Entrega (común a los cinco cursos)

- **Plazo único:** domingo 15/11/2026, 11:59 p. m., en ExamLab.
- **Un solo .zip** con todo (código, documentos, diagramas, capturas; cualquier tipo de archivo, máx. 50 MB)
  **+ enlace obligatorio** al repositorio de GitHub o a la carpeta de Drive.
- **En equipo de 4 a 5 integrantes (máximo 5)**: cada integrante sube el .zip del equipo
  desde su cuenta (una entrega por estudiante).
- **Sustentación:** 15 min de exposición + 5 de preguntas (turno de 20 min).

## Rúbrica (100 pts)

Modelo/DDL 20 · Seguridad/respaldo 15 · Programables 25 · Optimización 15 · Integración 10 · Informe+sustentación 15.

## Evidencias

Dentro del .zip: scripts SQL · ER · capturas Live SQL/DB Fiddle · informe. Aparte, el enlace
a GitHub o Drive. Sustentación de 15 min + 5 de preguntas.
"""

MD_ARQ = """# Guía docente — Proyecto Integrador · Arquitectura · 2026-2

**Privado docente** · No compartir en `Clases/`.

- **Curso:** Arquitectura de Sistemas Computacionales (FI303380 · 6303C)
- **Peso:** 20% Corte 3 (Acuerdo)
- **Dominio estudiante:** CloudLite App
- **Enunciado:** `Clases/Proyecto Integrador/Enunciado Proyecto Integrador - Arquitectura de Sistemas Computacionales - 2026-2.docx`

## Hitos (Plan 2026-2 · semestre acortado a 13 sesiones)

Las carpetas de material siguen numeradas 1–15; lo que cambia es en qué sesión se dicta cada una.
Toda entrega intermedia cierra el **domingo siguiente a la sesión, a las 11:59 p. m.**

| Sesión | Fecha | Material | Foco | Cierre de entrega |
|---|---|---|---|---|
| S10 (doble) | 26/10/2026 | Clases 11 + 12 | Avance PI — diagramas v1 · Pruebas de rendimiento · **preparación de la sustentación** | dom 01/11/2026, 11:59 p. m. |
| S11 (autónoma) | 02/11/2026 | Clase 13 | Escalabilidad automática aplicada al PI | dom 08/11/2026, 11:59 p. m. |
| S12 | 09/11/2026 | Clase 14 | **Parcial 3** (virtual síncrono por Meet · solo evaluación) | **paquete final:** dom 15/11/2026, 11:59 p. m. |
| S13 | 16/11/2026 | Clase 15 | **Sustentación en vivo del PI** (15 min + 5 de preguntas, turno de 20) + cierre (sesión síncrona) | — (el paquete ya está entregado) |

> S13 cae en festivo (Independencia de Cartagena), pero por decisión docente es sesión de
> sustentaciones: no es autónoma y no es parcial. El paquete final se sube a ExamLab a más
> tardar el **domingo 15/11/2026, 11:59 p. m.**; el 16/11 solo se defiende.

## Entrega (común a los cinco cursos)

- **Plazo único:** domingo 15/11/2026, 11:59 p. m., en ExamLab.
- **Un solo .zip** con todo (código, documentos, diagramas, capturas; cualquier tipo de archivo, máx. 50 MB)
  **+ enlace obligatorio** al repositorio de GitHub o a la carpeta de Drive.
- **En equipo de 4 a 5 integrantes (máximo 5)**: cada integrante sube el .zip del equipo
  desde su cuenta (una entrega por estudiante).
- **Sustentación:** 15 min de exposición + 5 de preguntas (turno de 20 min).

## Rúbrica (100 pts)

Dominio/servicio 15 · Diagramas 25 · Contenedores 20 · CI/CD 15 · Seg/costos/escala 10 · Informe+sustentación 15.

## Herramientas

draw.io · LabEx Docker Playground / Killercoda · GitHub Actions · **sin** AWS/GCP/Oracle Cloud con tarjeta.
"""


def anexo_caso_estudio(doc, meta: dict):
    """Anexo del caso de estudio: el cliente, su operacion y sus reglas.

    Por que es un documento aparte y no un parrafo mas del enunciado: el
    estudiante lo consulta en las quince clases, no una vez. Antes estos datos
    estaban repartidos entre dos diapositivas, un parrafo del enunciado y los
    enunciados de ExamLab, y algunos —la escala de 30.010 citas que evaluan las
    Clases 6 y 7— no estaban escritos en ninguna parte que el estudiante lea.
    """
    banda(doc, "Anexo · Caso de estudio — " + CLIENTE)
    para(doc, meta["asignatura"] + " · " + meta["codigo"] + " · Periodo " + meta["periodo"],
         size=10, color=CIAN)
    para(doc, "Documento de consulta para todo el semestre. Los talleres, los quices y el "
              "Proyecto Integrador se refieren a esta clínica y a estos datos.", size=10)
    para(doc, NOMENCLATURA, size=10, bold=True, shade="FFF8D6")

    h2(doc, "1. La clínica")
    table(doc, ["Dato", "Detalle"], [[k, v] for k, v in PERFIL])

    h2(doc, "2. El problema que la trae hasta aquí")
    para(doc, CONTEXTO_VETCARE)
    bullets(doc, PROBLEMAS)

    h2(doc, "3. Quién va a usar el sistema")
    bullets(doc, INTERESADOS)
    para(doc, "Sus intereses @@entran en conflicto@@: pedir más datos en el formulario de la "
              "cita da mejores métricas al dueño y le hace más lento el trabajo a la "
              "recepcionista. Cuando dude si un dato sobra, pregúntese @@cuál de los tres lo "
              "necesita@@ y qué pierde otro si lo agrega. Ahí están las decisiones de diseño "
              "del semestre.")

    h2(doc, "4. Qué guarda el sistema")
    para(doc, "Ocho entidades. Aquí están descritas por lo que significan para la clínica; "
              "traducirlas a tablas con sus tipos y sus claves es su trabajo.", size=10)
    table(doc, ["Entidad", "Qué es para la clínica"], [[k, v] for k, v in ENTIDADES])
    para(doc, "Cómo se relacionan: un @@Dueño@@ tiene varias @@Mascotas@@; una @@Mascota@@ "
              "tiene varias @@Citas@@; un @@Veterinario@@ atiende varias @@Citas@@; una "
              "@@Cita@@ atendida produce @@una@@ @@Consulta@@; una @@Consulta@@ puede generar "
              "@@Facturas@@; cada @@Factura@@ tiene varias líneas de @@Detalle@@, y cada línea "
              "apunta a un @@Insumo@@.")

    h2(doc, "5. Las reglas del negocio")
    para(doc, "Son tres y no cambian en el semestre. La columna de la derecha dice @@dónde@@ se "
              "hacen cumplir: es lo que conecta este caso con el temario del curso.", size=10)
    table(doc, ["Regla", "Dónde se hace cumplir"], [[k, v] for k, v in REGLAS_NEGOCIO])

    h2(doc, "6. Cómo crece la base durante el semestre")
    para(doc, "El mismo cliente en tres momentos. Conviene tenerlo claro porque los talleres "
              "de optimización no evalúan la base de la primera semana.", size=10)
    table(doc, ["Momento", "Volumen y qué implica"], [[k, v] for k, v in ESCALA])

    h2(doc, "7. Convenciones de datos del curso")
    bullets(doc, CONVENCIONES_DATOS)

    h2(doc, "8. Elenco fijo")
    para(doc, "Use estos nombres en sus ejemplos y datos de prueba. Existen para que su "
              "entrega, la solución del docente y los enunciados de ExamLab hablen de las "
              "mismas personas. @@Están escritos sin tilde a propósito:@@ así están "
              "sembrados en la base, y así hay que escribirlos en un `WHERE` o un "
              "`INSERT` para que coincidan.", size=10)
    table(doc, ["Grupo", "Nombres"], [
        ["Dueños", ELENCO["duenos"]],
        ["Mascotas", ELENCO["mascotas"]],
        ["Veterinarios", ELENCO["veterinarios"]],
        ["Especialidades", ELENCO["especialidades"]],
        ["Servicios", ELENCO["servicios"]],
    ])

    h2(doc, "9. Qué NO cubre el proyecto")
    bullets(doc, FUERA_DE_ALCANCE)
    para(doc, "Si una idea suya no cabe en las ocho entidades ni en las tres reglas, "
              "probablemente está fuera de alcance. Escríbala en el bloque «qué NO hará» de su "
              "ficha en vez de intentar construirla.", size=10)


# ---------------------------------------------------------------------------
# Introduccion a la Ingenieria — proyecto de equipo, sin dominio fijo
#
# Este curso NO tiene un producto ficticio compartido (no hay VetCare ni
# CloudLite): cada EQUIPO elige su propio problema real del entorno (barrio,
# universidad, trabajo, casa) desde la ficha semilla de la Clase 1. Los tres
# grupos (SB141B, SB141C, LB141F) comparten el mismo enunciado, la misma
# rubrica y el mismo calendario POR SESION -- solo cambian el dia y las
# fechas de cada grupo, que ya estan en su propio CALENDARIO_2026-2. Por eso
# este documento ancla las etapas a la sesion y remite al calendario del grupo.
# Solo fecha dos cosas: el plazo unico de entrega (comun a los cinco cursos) y
# el dia de la exposicion final de cada grupo.
# ---------------------------------------------------------------------------

#: ExamLab no tiene los equipos cargados: mientras eso no cambie, el informe (que es del
#: equipo) lo sube cada integrante desde su propia cuenta.
INTRO_QUIEN_SUBE = ("@@Cada integrante sube la entrega del equipo desde su propia cuenta@@ "
                    "(ExamLab todavía no tiene los equipos cargados): el mismo .zip y el "
                    "mismo enlace, una sola entrega por estudiante.")

INTRO_ING_META = {
    "titulo": "Proyecto Integrador 2026-2 — Proyecto de equipo",
    "titulo_docente": "Guía docente · Proyecto de equipo — Introducción a la Ingeniería",
    "asignatura": "Introducción a la Ingeniería",
    "codigo": "FI300101",
    "grupo": "SB141B · SB141C · LB141F",
    "periodo": "2026-2",
    "horario": "Cada grupo tiene su propio día y horario (ver su CALENDARIO_2026-2)",
    "modalidad_texto": "Virtual (sesiones por Microsoft Teams)",
    "dominio": "Un problema real del entorno, elegido por cada equipo",
}


def enunciado_intro_ing(doc):
    portada_estudiante(doc, INTRO_ING_META)

    h2(doc, "1. Propósito")
    para(doc,
         "Este curso no se aprueba con un examen final: se aprueba con un proyecto de "
         "equipo que arranca desde la primera sesión y se defiende en la última semana "
         "de clases. Es una propuesta de mejora tecnológica para un problema real del "
         "entorno de ustedes. No hay que programarla: hay que diseñarla y defenderla con "
         "evidencia.")
    para(doc,
         "Peso: 40% del Corte 3 (exposición final 15% + informe final 20% + asistencia "
         "5%), más una parte de las exposiciones y actividades en clase de los Cortes 1 y "
         "2 (ver el desglose completo en el Acuerdo Pedagógico y en su CALENDARIO_2026-2).")
    modalidad_equipo(doc)

    h2(doc, "2. Cómo se construye, etapa por etapa")
    table(doc,
          ["Etapa", "Qué queda listo"],
          [
              ["1 · Problema y propuesta inicial",
               "Problema del entorno con su cifra, a quién le pasa y las causas "
               "principales. Con esto cierra el Corte 1."],
              ["2 · Ciclo de vida y prototipo",
               "Requisitos, alternativas y decisión, prototipo de baja fidelidad probado "
               "con una persona ajena al equipo. Con esto cierra el Corte 2."],
              ["3 · Evaluación de impacto y ensayo",
               "Impacto positivo y negativo con mitigación, limitaciones y siguiente "
               "paso, guion y ensayo de la exposición final."],
              ["4 · Informe y exposición final",
               "El informe final se entrega en ExamLab a más tardar el domingo 15/11/2026, "
               "11:59 p. m.; la defensa en vivo es en la última clase. Con esto cierra el "
               "Corte 3 y el curso."],
          ])
    para(doc,
         "Las fechas exactas de cada etapa están en el calendario de su grupo.")

    h2(doc, "3. El informe final — 12 secciones (20% del curso)")
    table(doc,
          ["#", "Sección", "Tiene que contener"],
          [
              ["1", "Portada y resumen",
               "Título, integrantes, curso. Resumen de ½ pág: problema con su número, "
               "solución en dos frases, impacto principal."],
              ["2", "El problema",
               "La cifra, cómo se obtuvo, a quién le pasa y las causas principales."],
              ["3", "Actores y afectados",
               "Usuarios, quien opera, y al menos un afectado que no es usuario."],
              ["4", "Antecedentes",
               "Tres soluciones que ya existen, qué hace cada una y por qué no sirve aquí."],
              ["5", "Requisitos y criterios",
               "Funcionales, no funcionales, y cómo se verifica cada criterio."],
              ["6", "Alternativas y decisión",
               "Al menos dos alternativas, los criterios, la elegida y qué se sacrificó."],
              ["7", "La solución y el prototipo",
               "Descripción, capturas y el recorrido principal paso a paso."],
              ["8", "Prueba y hallazgos",
               "Con quién se probó (solo el rol, no el nombre), qué hizo, la "
               "clasificación y el patrón."],
              ["9", "Impacto", "Positivos con indicador y negativos con mitigación."],
              ["10", "Limitaciones y siguiente paso",
               "Lo que se decidió no hacer, con el motivo, y por dónde seguiría."],
              ["11", "Declaración del uso de IA",
               "Qué se pidió, qué se corrigió, qué no se le entregó."],
              ["12", "Referencias",
               "Lo que se citó, en el formato acordado. Nada que no se haya leído."],
          ])
    para(doc, "Extensión total: 9 a 11 páginas. La extensión no es una virtud: un informe "
              "donde la decisión está en la página 18 es un informe que no se va a leer.",
         size=10)

    h2(doc, "4. La exposición final (15% del curso)")
    bullets(doc, [
        "15 minutos de exposición + 5 minutos de preguntas, por equipo (turno de 20 "
        "minutos). Se corta a los 15 minutos sin excepción.",
        "Fecha: la última clase de su grupo — SB141C y LB141F el martes 17/11/2026; "
        "SB141B el jueves 19/11/2026.",
        "Formato: comparte pantalla un integrante; plan B = PDF/capturas en la carpeta "
        "del equipo, subidos antes de exponer.",
        "Todos los integrantes tienen que hablar, y quien responda una pregunta debe "
        "responder sobre SU propio tramo.",
    ])
    table(doc,
          ["Tramo", "Qué se busca", "Pts"],
          [
              ["1 · El problema con su cifra",
               "Arranca por el problema, no por presentaciones. Trae un número y de "
               "dónde salió.", "20"],
              ["2 · Los afectados y la decisión",
               "Incluye un afectado que no es usuario y dice qué se sacrificó.", "20"],
              ["3 · La solución y el prototipo en vivo",
               "Muestra una tarea cumpliéndose, no describe la pantalla.", "25"],
              ["4 · Lo que falló y lo que aprendimos",
               "Hallazgos con personas reales, qué se arregló y qué se decidió no "
               "arreglar.", "20"],
              ["5 · Impacto y siguiente paso",
               "Impacto positivo con número y el negativo con su mitigación.", "15"],
          ])

    h2(doc, "5. Herramientas (gratis + navegador)")
    bullets(doc, [
        "Bitácora y soporte de la exposición: Google Drive (Docs y Slides).",
        "Diagramas y línea de tiempo: diagrams.net (draw.io) · Excalidraw para bocetos.",
        "Póster/infografía (opcional): Canva, alternativa Google Slides.",
        "Asistente de IA (Gemini/Claude/ChatGPT, plan gratuito): solo en los momentos "
        "puntuales que anuncie el docente, con declaración de qué se pidió y qué se "
        "corrigió a mano.",
        "Entrega de talleres, diagnóstico, evaluaciones de corte e informe final: ExamLab.",
    ])
    para(doc,
         "Prohibido como requisito: cualquier nube que pida tarjeta de crédito. Nada de "
         "software de pago ni instalaciones obligatorias.",
         shade="FBE4E4", space_after=8)

    h2(doc, "6. Modalidad de trabajo")
    bullets(doc, [
        "Es un proyecto DE EQUIPO, no individual: equipos de 4 a 5 integrantes (máximo 5), "
        "fijos todo el semestre.",
        "El vocero rota en cada sesión y se anota en la bitácora: al final del semestre "
        "todos han expuesto al menos dos veces.",
        "La autoevaluación individual del cierre del proyecto sí se entrega solo al "
        "docente, uno por integrante.",
    ])

    h2(doc, "7. Qué NO es este proyecto")
    bullets(doc, [
        "No es un examen final escrito: el Corte 3 no tiene evaluación escrita, se "
        "califica con producto (exposición + informe).",
        "No hay que programarlo ni implementarlo: es una propuesta diseñada y defendida, "
        "no un sistema en producción.",
        "No reemplaza las evaluaciones de corte de ExamLab de los Cortes 1 y 2: son "
        "evaluaciones distintas del mismo semestre.",
        "No tiene un dominio fijo: no es «CloudLite» ni ningún otro producto de otro "
        "curso — el problema lo elige cada equipo.",
    ])

    entrega_y_sustentacion(
        doc, "8. Entrega en ExamLab y exposición",
        "en la última clase de su grupo (SB141C y LB141F martes 17/11; SB141B jueves "
        "19/11), por Microsoft Teams: " + SUSTENTACION + ". Se corta a los 15 minutos.",
        que_se_sube=("un solo archivo .zip con el informe final y todo lo que lo respalda "
                     "—documentos, diagramas, capturas del prototipo—; dentro puede ir "
                     "cualquier tipo de archivo, y pesa como máximo 50 MB"),
        quien_sube=INTRO_QUIEN_SUBE)


def guia_intro_ing(doc):
    portada_docente(doc, INTRO_ING_META)
    h2(doc, "Contexto")
    para(doc,
         "Tres grupos (SB141B, SB141C, LB141F), 11 sesiones cada uno, 16 Clases de "
         "microcurrículo (5 sesiones dobles). El proyecto es de EQUIPO (4 a 5 integrantes, "
         "máximo 5), sin dominio fijo: "
         "cada equipo elige su problema real desde la ficha semilla de la Clase 1. Ver "
         "`config/calendario/introduccion_ingenieria_2026_2.json` para el calendario real "
         "de cada grupo — este documento ancla todo a la sesión, salvo el plazo único de "
         "entrega (dom 15/11) y el día de la exposición de cada grupo.")
    h2(doc, "Hitos docentes (por sesión — igual en los 3 grupos)")
    table(doc,
          ["Sesión", "Clase(s)", "Rol docente"],
          [
              ["4", "Clase 6",
               "Cierra el Corte 1. Evaluación de corte en ExamLab (últimos 20 min) + "
               "revisar que el problema del entorno traiga cifra y a quién le pasa."],
              ["7", "Clase 11",
               "Cierra el Corte 2. Evaluación de corte en ExamLab (últimos 20 min) + "
               "verificar que el prototipo se haya probado con una persona ajena al "
               "equipo."],
              ["8 a 10", "Clases 12 a 14",
               "Revisar impacto/mitigación y bloquear equipos que lleguen sin línea "
               "base o sin criterio de aceptación verificable."],
              ["—", "—",
               "Plazo único del informe en ExamLab: domingo 15/11/2026, 11:59 p. m. Cada "
               "integrante sube el .zip del equipo desde su cuenta."],
              ["11 (doble)", "Clases 15+16",
               "Sustentaciones en turnos de 20 min por equipo (15 + 5; se corta a los 15) y "
               "cierre del proyecto. SB141C y LB141F mar 17/11 · SB141B jue 19/11. El "
               "informe ya está entregado."],
          ])
    entrega_docente(doc, "última clase de cada grupo (SB141C y LB141F mar 17/11 · SB141B jue "
                    "19/11), por Teams: " + SUSTENTACION + "; se corta a los 15 minutos.",
                    quien_sube=("Cada integrante sube el .zip del equipo desde su propia "
                                "cuenta: ExamLab no tiene equipos cargados. Una entrega por "
                                "estudiante."))
    h2(doc, "Rúbrica detallada")
    bullets(doc, [
        "Exposición final (100 pts → 15% del curso): 5 tramos de 20/20/25/20/15 — ver "
        "tabla completa en el enunciado del estudiante.",
        "Informe final (100 pts → 20% del curso): 30 pts las 12 secciones completas · "
        "20 huecos resueltos y resumen · 15 declaración de uso de IA · 20 "
        "autoevaluación con evidencia · 15 coevaluación con observaciones.",
        "Penalice con -10 pts de exposición si no hablan todos los integrantes, y otros "
        "-10 si nadie responde una pregunta de su propio tramo.",
    ])
    h2(doc, "Errores frecuentes")
    bullets(doc, [
        "Un equipo que redacta el problema como «existen varios modelos de servicio» en "
        "vez de nombrar la cifra y a quién le pasa — es el error dominante del informe.",
        "Alternativas descartadas que no tienen motivo atado al dominio del equipo.",
        "Consecuencias/impacto que solo listan lo positivo: exigir siempre lo negativo "
        "con su mitigación.",
        "Equipos que dejan la prueba con persona ajena para el final: sin ella no hay "
        "hallazgos que mostrar en la exposición.",
    ])
    para(doc, "Enunciado del estudiante en `Clases/Proyecto Integrador/`, común a los "
              "tres grupos.", size=10)


MD_INTRO_ING = """# Guía docente — Proyecto de equipo · Introducción a la Ingeniería · 2026-2

**Privado docente** · No compartir en `Clases/`.

## Producto
No hay dominio fijo: cada EQUIPO elige su propio problema real del entorno desde la
ficha semilla de la Clase 1 (cinco campos de acción, retomada en la Clase 6). Común a
los tres grupos SB141B, SB141C, LB141F.

**Equipos de 4 a 5 integrantes (máximo 5)**, fijos todo el semestre.

## Hitos (por sesión — igual en los 3 grupos; fecha real en el CALENDARIO de cada grupo)

| Sesión | Clase(s) | Qué cierra |
|---|---|---|
| 4 | Clase 6 | Corte 1: problema y propuesta inicial + evaluación de corte en ExamLab |
| 7 | Clase 11 | Corte 2: ciclo de vida y prototipo probado + evaluación de corte en ExamLab |
| 11 (doble) | Clases 15+16 | Corte 3: exposición final (15%, 15 + 5 min por equipo; se corta a los 15) e informe final (20%, ya entregado en ExamLab) |

Exposición: SB141C y LB141F martes 17/11/2026 · SB141B jueves 19/11/2026.

## Rúbrica
- Exposición final: 100 pts → 15% (tramos 20/20/25/20/15).
- Informe final: 100 pts → 20% (30/20/15/20/15).

## Errores frecuentes
- Problema sin cifra ni "a quién le pasa" (el error dominante).
- Alternativas descartadas sin motivo atado al dominio propio.
- Consecuencias que solo listan lo positivo.
- Prototipo sin probar con una persona ajena al equipo.

## Entrega (común a los cinco cursos)

- **Plazo único del informe:** domingo 15/11/2026, 11:59 p. m., en ExamLab.
- **Un solo .zip** con el informe y lo que lo respalda (cualquier tipo de archivo, máx. 50 MB)
  **+ enlace obligatorio** a la carpeta de Drive o al repositorio de GitHub del equipo.
- **Cada integrante sube la entrega del equipo desde su propia cuenta** (ExamLab no tiene
  equipos cargados): una entrega por estudiante.
- **Exposición:** 15 min + 5 de preguntas por equipo (turno de 20 min); se corta a los 15.

Enunciado del estudiante en `Clases/Proyecto Integrador/`, común a los tres grupos.
"""


def build_one(curso_dir: Path, meta: dict, build_est, build_doc, md_text: str, slug: str):
    est_dir = curso_dir / "Clases" / "Proyecto Integrador"
    kit_dir = curso_dir / "Kit docente" / "Proyecto Integrador"
    est_dir.mkdir(parents=True, exist_ok=True)
    kit_dir.mkdir(parents=True, exist_ok=True)

    est_path = est_dir / f"Enunciado Proyecto Integrador - {slug} - 2026-2.docx"
    doc_path = kit_dir / f"Guia Docente PI - {slug} - 2026-2.docx"
    md_path = kit_dir / f"Guia Docente PI - {slug} - 2026-2.md"

    global NOMBRE_PLATAFORMA
    NOMBRE_PLATAFORMA = meta.get("plataforma", "ExamLab")

    d1 = Document()
    margins(d1)
    build_est(d1)
    d1.save(est_path)

    # El anexo del caso de estudio acompana al enunciado en la carpeta del PI.
    # Solo para los cursos cuyo PI es la Clinica Huellitas: Arquitectura trabaja
    # CloudLite, con un dominio que elige cada estudiante.
    if meta.get("caso_huellitas"):
        anexo_path = est_dir / f"Anexo - Caso de estudio Clinica Huellitas - {slug}.docx"
        d3 = Document()
        margins(d3)
        anexo_caso_estudio(d3, meta)
        d3.save(anexo_path)
        print("OK ->", anexo_path)

    d2 = Document()
    margins(d2)
    build_doc(d2)
    d2.save(doc_path)

    md_path.write_text(md_text, encoding="utf-8")
    print("OK ->", est_path)
    print("OK ->", doc_path)
    print("OK ->", md_path)

MD_PROG2 = """# Guía docente — Proyecto Integrador · Programación II · 2026-2

**Privado docente** · No compartir en `Clases/`.

## Producto
**VetCare** — aplicación de escritorio en Java para la Clínica Veterinaria «Huellitas».
PI **compartido con Seminario de Sistemas**: mismo producto, distinto entregable
(aquí el software, allá los planos).

## Casos de matrícula
- **A** (ambas materias): aquí se califica el código; los diagramas se califican en Seminario.
- **B** (solo Prog II): el docente entrega los diagramas UML ya hechos; el estudiante programa.
- **C** (solo Seminario): no aplica en este curso.

## Hitos
Semestre acortado a **13 sesiones**; las carpetas de material siguen numeradas 1–15.
Toda entrega intermedia cierra el **domingo siguiente a la sesión, a las 11:59 p. m.**

| Sesión | Fecha | Material | Entrega | Cierre |
|---|---|---|---|---|
| S10 (doble) | 28/10 | Clases 11 + 12 | Avance de código + revisión cruzada e integración de módulos | dom 01/11/2026, 11:59 p. m. |
| S11 | 04/11 | Clase 13 | Excepciones y validaciones | dom 08/11/2026, 11:59 p. m. |
| S12 | 11/11 | Clase 14 | Versión final + ensayo | **paquete final:** dom 15/11/2026, 11:59 p. m. |
| S13 | 18/11 | Clase 15 | Sustentación 15 + 5 min (mismo día del Parcial 3) | — |

## Rúbrica (100 pts → 20% del Corte 3)
POO 20 · Estructuras de datos 15 · GUI 20 · Manejo de errores 15 · Persistencia 15 · Sustentación 15

## Errores frecuentes
- Herencia forzada solo para cumplir el requisito.
- GUI que no persiste: pedir siempre la prueba de cerrar y reabrir.
- `try-catch` vacío que oculta el error.
- Que uno solo del equipo haya programado todo → preguntas al azar a cualquier integrante en la sustentación.

## Entrega (común a los cinco cursos)

- **Plazo único:** domingo 15/11/2026, 11:59 p. m., en ExamLab.
- **Un solo .zip** con todo (código, documentos, diagramas, capturas; cualquier tipo de archivo, máx. 50 MB)
  **+ enlace obligatorio** al repositorio de GitHub o a la carpeta de Drive.
- **En equipo de 4 a 5 integrantes (máximo 5)**: cada integrante sube el .zip del equipo
  desde su cuenta (una entrega por estudiante).
- **Sustentación:** 15 min de exposición + 5 de preguntas (turno de 20 min).

Enunciado del estudiante en `Clases/Proyecto Integrador/`.
"""

MD_SEMIN = """# Guía docente — Proyecto Integrador · Seminario de Sistemas · 2026-2

**Privado docente** · No compartir en `Clases/`.

## Producto
**VetCare** — arquitectura y diseño del sistema para la Clínica Veterinaria «Huellitas».
PI **compartido con Programación II**: mismo producto, distinto entregable
(aquí los planos, allá el software).

## Casos de matrícula
- **A** (ambas materias): aquí se califican los planos; el código se califica en Prog II.
- **C** (solo Seminario): cierra con SDD + mockup navegable. Ruta completa y válida,
  **no** una versión reducida — decirlo desde Clase 1.
- **B** (solo Prog II): no aplica aquí.

## Fases
1. Ingeniería de requisitos (RF/RNF)
2. Modelado UML (casos de uso, clases, dinámico)
3. Diseño de interfaz (wireframes + mockup navegable)
4. Arquitectura de datos (diccionario de datos)

## Hitos
Semestre acortado a **13 sesiones**; las carpetas de material siguen numeradas 1–15.
Toda entrega intermedia cierra el **domingo siguiente a la sesión, a las 11:59 p. m.**

| Sesión | Fecha | Material | Entrega | Cierre |
|---|---|---|---|---|
| S10 (doble) | 29/10 | Clases 11 + 12 | Requisitos + casos de uso y UML avanzado | dom 01/11/2026, 11:59 p. m. |
| S11 | 05/11 | Clase 13 | Wireframes y mockup | dom 08/11/2026, 11:59 p. m. |
| S12 | 12/11 | Clase 14 | Documento consolidado + ensayo | **paquete final:** dom 15/11/2026, 11:59 p. m. |
| S13 | 19/11 | Clase 15 | Sustentación 15 + 5 min (mismo día del Parcial 3) | — |

## Rúbrica (100 pts → 20% del Corte 3)
Requisitos 20 · UML 25 · Interfaz 20 · Arquitectura de datos 15 · Plan de pruebas 10 · Sustentación 10

## Errores frecuentes
- Requisitos no verificables («debe ser rápido») sin criterio medible.
- Diagrama de clases que no corresponde a los casos de uso.
- Mockup que no cubre el flujo crítico (registrar → buscar → ver historial).
- Diccionario de datos sin tipos ni restricciones.

## Entrega (común a los cinco cursos)

- **Plazo único:** domingo 15/11/2026, 11:59 p. m., en ExamLab.
- **Un solo .zip** con todo (código, documentos, diagramas, capturas; cualquier tipo de archivo, máx. 50 MB)
  **+ enlace obligatorio** al repositorio de GitHub o a la carpeta de Drive.
- **En equipo de 4 a 5 integrantes (máximo 5)**: cada integrante sube el .zip del equipo
  desde su cuenta (una entrega por estudiante).
- **Sustentación:** 15 min de exposición + 5 de preguntas (turno de 20 min).

Enunciado del estudiante en `Clases/Proyecto Integrador/`.
"""


CURSOS = [
    ("Bases de Datos II", "BD2_META", "enunciado_bd2", "guia_bd2", "MD_BD2"),
    ("Arquitectura de Sistemas Computacionales", "ARQ_META", "enunciado_arq", "guia_arq", "MD_ARQ"),
    ("Programacion II", "PROG2_META", "enunciado_prog2", "guia_prog2", "MD_PROG2"),
    ("Seminario de Sistemas", "SEMIN_META", "enunciado_seminario", "guia_seminario", "MD_SEMIN"),
    ("Introduccion a la Ingenieria", "INTRO_ING_META", "enunciado_intro_ing", "guia_intro_ing", "MD_INTRO_ING"),
]


def build(solo_cursos=None):
    """Regenera el PI de los cuatro cursos, o solo de algunos.

    ``solo_cursos`` (iterable con nombres de carpeta) o la variable de entorno
    SOLO_CURSOS="Bases de Datos II,Arquitectura de Sistemas Computacionales"
    limitan la regeneracion. Existe porque una correccion suele afectar a un curso
    y regenerar los cuatro reescribia documentos identicos de los otros tres:
    el diff se llenaba de .docx binarios que nadie habia revisado.
    """
    if solo_cursos is None:
        env = os.environ.get("SOLO_CURSOS")
        solo_cursos = {x.strip() for x in env.split(",") if x.strip()} if env else None
    else:
        solo_cursos = set(solo_cursos)

    glob = globals()
    for curso, meta, enun, guia, md in CURSOS:
        if solo_cursos is not None and curso not in solo_cursos:
            print("omitido:", curso)
            continue
        build_one(ROOT / curso, glob[meta], glob[enun], glob[guia], glob[md], curso)


if __name__ == "__main__":
    build()
