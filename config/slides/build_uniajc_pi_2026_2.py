# -*- coding: utf-8 -*-
"""Genera el Proyecto Integrador de los cinco cursos, para cualquier semestre.

BD II, Arquitectura, Programacion II, Seminario e Introduccion a la Ingenieria. La entrega
y la sustentacion son comunes a los cinco; lo que entrega cada uno esta en `ENTREGA` y su
carpeta «Plantilla de entrega» en `PLANTILLAS`. El enunciado es corto: que se hace, que se
entrega, como se califica y como se entrega.

SIN DATOS DE UN SEMESTRE (pedido docente, 16/10/2026: «que funcionen los proyectos para
cualquier semestre»). Nada de fechas, periodo, grupos, horario, modalidad (Meet o Teams),
festivos, parciales, tamano del equipo ni pesos en la nota: cambian cada semestre y el
docente los da por otro medio. El plazo se publica en ExamLab, el peso esta en el Acuerdo
pedagogico y las fechas de cada clase en el calendario del semestre (`config/calendario/`).
Los hitos de la guia docente se anclan a la Clase N del material, que no cambia. El nombre
de este archivo (2026_2) es historico: no hay que copiarlo para el semestre siguiente.

Estudiante (compartible):
  <Curso>/Clases/Proyecto Integrador/Enunciado Proyecto Integrador - <Curso>.docx
  <Curso>/Clases/Proyecto Integrador/Plantilla de entrega/

Docente (privado):
  <Curso>/Kit docente/Proyecto Integrador/Guia Docente PI - <Curso>.docx
  <Curso>/Kit docente/Proyecto Integrador/Guia Docente PI - <Curso>.md
"""
from __future__ import annotations

import os
import re
import shutil
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
# Entrega y sustentacion: lo COMUN a los cinco cursos (decision docente, 13/10/2026)
#
# Comun es solo esto: un plazo unico para todos los grupos, un solo .zip de hasta 50 MB, uno
# de los integrantes lo sube y queda para todo el equipo, y la sustentacion dura 15 + 5
# minutos. Repetidas en cada curso, estas reglas divergieron (cuatro cursos decian 5-8 min de
# sustentacion e Introduccion 9 + 3); por eso viven aqui, una vez.
#
# SIN ENLACE (17/10/2026): el campo de enlace de la entrega en ExamLab esta apagado desde el
# 13/10/2026, asi que no se pide repositorio ni carpeta de Drive aparte: todo va en el .zip.
# Los enlaces que van DENTRO de un documento (al prototipo o al mockup navegable) se quedan.
# ---------------------------------------------------------------------------

#: El PI es en equipo en los cinco cursos (decision docente, 13/10/2026): antes BD II y
#: Arquitectura eran individuales, y Prog. II y Seminario no lo decian. El TAMANO del equipo
#: no va en el material (16/10/2026): cambia por semestre y lo indica el docente.
EQUIPO = "en equipo"
SUSTENTACION = ("15 minutos de exposición + 5 minutos de preguntas por equipo (turno de 20 "
                "minutos); hablan todos los integrantes")
ZIP = "un solo archivo .zip —dentro puede ir cualquier tipo de archivo; máximo 50 MB—"
SIN_ENLACE = "No se sube ningún enlace aparte: todo va dentro del .zip."


def _quien_sube(plataforma=None):
    """Una entrega por equipo: ExamLab ya tiene los grupos y lo que sube uno queda para todos
    (17/10/2026; antes cada integrante subia la misma entrega desde su cuenta)."""
    return ("@@Uno de los integrantes sube la entrega del equipo@@ en " + (plataforma or _plat())
            + " y queda para todos.")


def _plazo():
    """El plazo sin fecha: uno solo para todo el curso, el que el docente publica en la
    plataforma. Fechado, el enunciado quedaba viejo al semestre siguiente."""
    return "la fecha y la hora que el docente publica en " + _plat()


# ---------------------------------------------------------------------------
# Lo que entrega CADA curso: especifico, nunca generico (decision docente, 13/10/2026)
#
# NOTA PARA LAS SIGUIENTES VERSIONES. Que va dentro del .zip y que se
# muestra en la sustentacion se escribe con los entregables y las herramientas de ESE curso.
# (Hubo un texto unico para los cinco que le pedia codigo a Introduccion, donde no se
# programa.) Cada pieza sale de lo que el curso ya exige y de su rubrica: aqui no se inventan
# requisitos, se dice como se empacan. El enunciado (arbol + tabla), la carpeta «Plantilla de
# entrega», la guia docente y la guia en Markdown leen la misma entrada: no se desalinean.
#
# Desde el 16/10/2026 el enunciado es CORTO y la entrega trae PLANTILLA (pedido docente: «se
# pierde que tienen que hacer los estudiantes»; «un template de como se deberia ver»). El
# enunciado dice que se hace, que se entrega, como se califica y como se entrega. Los hitos de
# clase y las actividades intermedias NO van ahi: el docente los da por otro medio y siguen
# en la guia docente.
# ---------------------------------------------------------------------------

#: Por curso:
#:   arbol  — lo que se ve al abrir el .zip: (ruta, nota); una ruta con «/» al final es carpeta.
#:   zip    — lo que tiene que tener cada pieza: la tabla del enunciado y de la guia docente.
#:   cuando, muestra (y opcional corte) — entrega y sustentacion. Sin enlace: ver arriba.
#: Los textos van con tildes: Prog. II y Seminario se las quitan al imprimir.
ENTREGA = {
    "bd2": {
        "arbol": [
            ("Informe.docx", "el informe, con las secciones de la plantilla"),
            ("diagrama/Diagrama ER.png", "el modelo: el mismo que crea el DDL"),
            ("scripts/", "corren en PostgreSQL tal cual, en orden"),
            ("scripts/01_ddl.sql", "tablas, llaves y restricciones"),
            ("scripts/02_roles_y_privilegios.sql", "roles, GRANT y REVOKE"),
            ("scripts/03_programables.sql", "procedimientos, funciones, disparadores y pruebas"),
            ("scripts/04_optimizacion.sql", "consultas antes y después"),
            ("capturas/", "la salida de cada script y de cada prueba"),
        ],
        "zip": [
            ("Informe.docx", "Las secciones de la plantilla: portada con integrantes, modelo, "
             "seguridad y respaldo (con el plan de respaldo y recuperación), objetos "
             "programables, optimización, integración app ↔ BD y cómo correr los scripts."),
            ("Diagrama ER.png", "Las entidades del caso Huellitas (ver el anexo), con sus llaves "
             "y cardinalidades. Coincide con el DDL."),
            ("01_ddl.sql", "Todas las tablas, con llaves primarias y foráneas y las "
             "restricciones de las reglas del negocio."),
            ("02_roles_y_privilegios.sql", "Al menos 2 roles con privilegios distintos."),
            ("03_programables.sql", "Al menos 2 procedimientos, 1 función y 2 disparadores, "
             "cada uno con su caso de prueba."),
            ("04_optimizacion.sql", "Al menos 2 consultas con su EXPLAIN antes y después, y el "
             "índice o la reescritura que las mejora."),
            ("capturas/", "La salida de cada script y de cada caso de prueba."),
        ],
        "cuando": "en la última clase del curso",
        "muestra": "ejecutar en vivo un procedimiento y un disparador con sus casos de prueba, "
                   "y una consulta antes y después de optimizarla",
    },
    "arq": {
        "arbol": [
            ("Documento de arquitectura.docx", "con las secciones de la plantilla"),
            ("diagramas/", "cada uno en PNG + su fuente (.drawio o .mmd)"),
            ("diagramas/1 componentes.png", ""),
            ("diagramas/2 despliegue.png", ""),
            ("diagramas/3 ci-cd.png", ""),
            ("app/", "el servicio mínimo (stub)"),
            ("contenedores/Dockerfile", "o docker-compose.yml"),
            ("contenedores/capturas/", "el lab corriendo, con la fecha visible"),
            (".github/workflows/ci.yml", "construye y prueba app/"),
        ],
        "zip": [
            ("Documento de arquitectura.docx", "Las secciones de la plantilla: dominio y "
             "alcance (3 a 5 capacidades), modelo de servicio (IaaS, PaaS o SaaS, y por qué), "
             "decisiones, despliegue y contenedores, CI/CD, seguridad · monitoreo · costos · "
             "escalabilidad, y riesgos."),
            ("diagramas/", "Los tres —componentes (C4), despliegue y flujo de CI/CD—, legibles "
             "y con los mismos nombres en los tres."),
            ("app/", "El servicio mínimo que se contiene y que el workflow construye y prueba."),
            ("contenedores/", "El Dockerfile (o el docker-compose.yml) y las capturas del lab "
             "(LabEx o Killercoda) donde se ve corriendo, con la fecha visible."),
            (".github/workflows/ci.yml", "Las etapas de construir y probar, que pasan; el "
             "despliegue puede ser simulado."),
        ],
        "cuando": "en la última clase del curso",
        "muestra": "el diagrama de despliegue, el contenedor corriendo en el lab (o sus "
                   "capturas, si la sesión del lab caducó) y el workflow con sus etapas",
    },
    "prog2": {
        "arbol": [
            ("LEEME.txt", "integrantes, caso de matrícula y cómo se ejecuta"),
            ("proyecto/src/", "todos los .java"),
            ("datos/", "el .csv o .txt con registros de prueba"),
            ("Manual de usuario.docx", "1 a 2 páginas con capturas"),
        ],
        "zip": [
            ("LEEME.txt", "Nombre del equipo, integrantes, caso de matrícula (A o B) y los pasos "
             "para compilar y ejecutar."),
            ("proyecto/src/", "La aplicación completa y que compila: clases del dominio, "
             "colecciones, ventanas, manejo de errores y lectura y escritura del archivo de "
             "datos. Sin carpetas de compilación (bin, out, target)."),
            ("datos/", "El archivo que la aplicación lee al arrancar y en el que guarda, con "
             "registros de prueba inventados."),
            ("Manual de usuario.docx", "1 a 2 páginas con capturas, en el orden de la "
             "plantilla: registrar, agendar, buscar, ver el historial y qué pasa con un dato "
             "mal escrito."),
        ],
        "cuando": "en la última clase del curso",
        "muestra": "la aplicación corriendo en vivo: registrar una mascota, buscarla por su ID, "
                   "escribir un dato inválido sin que se cierre, y cerrar y volver a abrir para "
                   "mostrar que los datos siguen ahí",
    },
    "seminario": {
        "arbol": [
            ("Documento de diseno.docx", "requisitos, UML y datos, en el orden de la plantilla"),
            ("diagramas/", "cada diagrama en PNG + su archivo fuente"),
            ("mockup/Mockup.pdf", "las pantallas exportadas"),
            ("Plan de pruebas.docx", "la tabla de casos de prueba de la plantilla"),
        ],
        "zip": [
            ("Documento de diseno.docx", "Requisitos RF y RNF verificables y trazables, casos de "
             "uso, diagrama de clases, un diagrama dinámico (actividad o secuencia), "
             "diccionario de datos con el formato de almacenamiento y el enlace al mockup "
             "navegable."),
            ("diagramas/", "Casos de uso, clases y el dinámico, en PNG, con su archivo fuente."),
            ("mockup/Mockup.pdf", "Las pantallas del flujo crítico (registrar, buscar y ver el "
             "historial), exportadas desde Figma, Penpot o Balsamiq."),
            ("Plan de pruebas.docx", "Un caso de prueba por requisito crítico, trazado a su RF."),
        ],
        "cuando": "en la última clase del curso",
        "muestra": "el mockup navegable recorriendo el flujo crítico (registrar, buscar y ver "
                   "el historial) y la trazabilidad de un requisito hasta su caso de uso y su "
                   "caso de prueba",
    },
    "intro": {
        "arbol": [
            ("Informe final.docx", "las 12 secciones de la plantilla"),
            ("prototipo/v1.png", "el prototipo de baja fidelidad"),
            ("prototipo/v2.png", "el prototipo mejorado"),
        ],
        "zip": [
            ("Informe final.docx", "Las 12 secciones de la plantilla, en 9 a 11 páginas. Se "
             "puede entregar en .docx o exportado a .pdf."),
            ("prototipo/", "La v1 y la v2, en PNG o PDF. El enlace al prototipo navegable va en "
             "la sección 7 del informe."),
        ],
        "cuando": "en la última clase de su grupo",
        "corte": "Se corta a los 15 minutos, sin excepción.",
        "muestra": "el prototipo navegable, recorriendo en vivo una tarea de principio a fin, "
                   "como si funcionara",
    },
}

#: Carpeta que acompana al enunciado en «Clases/Proyecto Integrador/»: el .zip ya armado,
#: listo para llenar (CLAUDE.md §4: si la forma del entregable se califica, se entrega).
CARPETA_PLANTILLA = "Plantilla de entrega"
GUIA_GRIS = RGBColor(0x7F, 0x7F, 0x7F)


def _sin_tildes(texto):
    """Los enunciados de Prog. II y Seminario se escribieron sin tildes ni enes."""
    s = unicodedata.normalize("NFD", str(texto))
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def _linea_sustentacion(e):
    return e["cuando"] + ", " + SUSTENTACION + "." + (" " + e["corte"] if e.get("corte") else "")


def _arbol_lineas(arbol, raiz):
    """[(texto, nota)] del arbol del .zip, con conectores ├── └── como en un explorador."""
    hijos = {"": []}
    for ruta, nota in arbol:
        partes = ruta.rstrip("/").split("/")
        padre = ""
        for k, parte in enumerate(partes):
            ultima = k == len(partes) - 1
            clave = padre + "/" + parte if padre else parte
            nombre = parte + ("/" if (not ultima or ruta.endswith("/")) else "")
            hermanos = hijos.setdefault(padre, [])
            if not any(c == clave for c, _, _ in hermanos):
                hermanos.append((clave, nombre, nota if ultima else ""))
            elif ultima and nota:
                hijos[padre] = [(c, n, nota if c == clave else x) for c, n, x in hermanos]
            hijos.setdefault(clave, [])
            padre = clave
    lineas = [(raiz, "")]

    def pintar(padre, prefijo):
        hs = hijos.get(padre, [])
        for i, (clave, nombre, nota) in enumerate(hs):
            ultimo = i == len(hs) - 1
            lineas.append((prefijo + ("└── " if ultimo else "├── ") + nombre, nota))
            pintar(clave, prefijo + ("    " if ultimo else "│   "))
    pintar("", "")
    return lineas


def arbol_docx(doc, arbol, f=str):
    """El arbol del .zip en monoespaciada, con su nota al lado: «asi se debe ver»."""
    lineas = _arbol_lineas([(f(r), n) for r, n in arbol], f("Equipo <nombre>.zip"))
    ancho = max(len(t) for t, _ in lineas) + 2
    for texto, nota in lineas:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.space_before = Pt(0)
        _shade(p, "F4F6F8")
        r = p.add_run(texto.ljust(ancho) + ("← " + f(nota) if nota else ""))
        _run(r, size=9.5, color=GRIS, name="Consolas")
    para(doc, "", space_after=4)


def seccion_entregable(doc, curso, titulo, *, sin_tildes=False):
    """«Qué se entrega»: el arbol del .zip, la plantilla y lo que tiene que tener cada pieza."""
    e = ENTREGA[curso]
    f = _sin_tildes if sin_tildes else str
    h2(doc, f(titulo))
    para(doc, f("Un solo archivo .zip con esta forma. La carpeta @@«" + CARPETA_PLANTILLA + "»@@, "
                "en esta misma carpeta, ya la trae armada: descárguenla, llénenla siguiendo "
                "sus INSTRUCCIONES y comprímanla."), shade="E8F4FA")
    arbol_docx(doc, e["arbol"], f)
    table(doc, [f("Pieza"), f("Qué tiene que tener")], [[f(a), f(b)] for a, b in e["zip"]],
          anchos=[1.9, 4.9])


def seccion_entrega(doc, curso, titulo, *, sin_tildes=False):
    """«Entrega y sustentación»: plazo, cómo se sube, quién sube y qué se muestra."""
    e = ENTREGA[curso]
    f = _sin_tildes if sin_tildes else str
    h2(doc, f(titulo))
    bullets(doc, [f(x) for x in [
        "@@Plazo único para todo el curso:@@ " + _plazo() + ".",
        "@@Qué se sube:@@ solo el .zip, de máximo 50 MB. " + SIN_ENLACE,
        _quien_sube(),
        "@@Sustentación:@@ " + _linea_sustentacion(e),
        "@@Qué se muestra:@@ " + e["muestra"] + ".",
    ]])


def entrega_docente(doc, curso, *, sin_tildes=False):
    """La misma entrega en la guia docente, con lo que hay que revisar al calificar."""
    e = ENTREGA[curso]
    f = _sin_tildes if sin_tildes else str
    h2(doc, f("Entrega y sustentación"))
    bullets(doc, [f(x) for x in [
        "Plazo único en ExamLab: el que usted publique allí, el mismo para todos los grupos. " +
        ZIP[0].upper() + ZIP[1:] + ", sin enlace: el campo de enlace de ExamLab está apagado "
        "y todo va dentro del .zip. Los estudiantes tienen la carpeta «" + CARPETA_PLANTILLA +
        "» con la forma exacta del .zip.",
        "Proyecto " + EQUIPO + " (el número de integrantes lo indica usted cada semestre) "
        "—solo el proyecto: los demás entregables conservan su modalidad—. " +
        _quien_sube("ExamLab"),
        "Sustentación: " + _linea_sustentacion(e),
        "Lo que deben mostrar: " + e["muestra"] + ".",
    ]])
    h3(doc, f("Qué revisar en el .zip"))
    table(doc, [f("Pieza"), f("Qué debe traer")], [[f(a), f(b)] for a, b in e["zip"]],
          anchos=[1.9, 4.9])


def _md_entrega(curso):
    """La seccion de entrega de la guia en Markdown, desde la misma entrada del curso."""
    e = ENTREGA[curso]
    md = (lambda t: re.sub(r"@@(.*?)@@", r"**\1**", t))
    arbol = "\n".join((t + "  ← " + n) if n else t
                      for t, n in _arbol_lineas(e["arbol"], "Equipo <nombre>.zip"))
    filas = "\n".join("  - **%s** — %s" % (a, b) for a, b in e["zip"])
    return ("## Entrega y sustentación\n\n"
            "- **Plazo único:** el que publique el docente en ExamLab, el mismo para todos "
            "los grupos.\n"
            "- **Un solo .zip** (máx. 50 MB) con esta forma —los estudiantes tienen la "
            "carpeta «" + CARPETA_PLANTILLA + "» ya armada—:\n\n```\n" + arbol + "\n```\n\n"
            "- **Qué debe traer cada pieza:**\n" + filas + "\n"
            "- **Sin enlace:** el campo de enlace de ExamLab está apagado; todo va dentro del "
            ".zip.\n"
            "- **Proyecto " + EQUIPO + "** (el número de integrantes lo indica el docente "
            "cada semestre) — solo el proyecto: los demás entregables conservan su modalidad. "
            + md(_quien_sube("ExamLab")) + "\n"
            "- **Sustentación:** " + _linea_sustentacion(e) + "\n"
            "- **Qué muestran:** " + e["muestra"] + ".\n")


# ---------------------------------------------------------------------------
# La carpeta «Plantilla de entrega» de cada curso
#
# Es el .zip ya armado: cada documento con sus secciones (y sus tablas vacias, donde la forma
# se califica), cada script o archivo de configuracion con su encabezado y sus marcas, y un
# «QUE VA AQUI» en cada carpeta que dice que va ahi. Solo estructura: nada de la solucion.
# ---------------------------------------------------------------------------

def _leeme_raiz(asignatura):
    return ("Plantilla de entrega del Proyecto Integrador · " + asignatura + "\n\n"
            "1. Descarguen esta carpeta completa (Drive la baja como .zip) y descomprímanla.\n"
            "2. Llenen cada archivo: reemplacen el texto en gris y lo que está entre < >.\n"
            "3. Pongan en cada carpeta lo que dice su «QUE VA AQUI», y al terminar borren esos "
            "archivos y este.\n"
            "4. Compriman la carpeta en un solo .zip (máximo 50 MB) con el nombre del equipo.\n"
            "5. Uno de los integrantes sube el .zip en " + _plat() + " antes de la fecha y la "
            "hora que publica el docente, y queda para todo el equipo. No se sube ningún "
            "enlace aparte.\n")


def _sql(n, titulo, cuerpo):
    return ("-- Proyecto Integrador · Bases de Datos II · VetCare DB\n"
            "-- Equipo: <nombre del equipo>\n"
            "-- Archivo " + n + " de 04: " + titulo + "\n"
            "-- Corre en PostgreSQL tal cual, en orden: 01, 02, 03, 04.\n\n" + cuerpo)


PLANTILLAS = {
    "bd2": [
        ("Informe.docx", ("docx", "Informe del proyecto · VetCare DB", [
            ("Portada", "Nombre del equipo, integrantes (nombre y código de cada uno), curso, "
             "grupo y fecha."),
            ("Modelo de datos", "Pegue el diagrama ER y explique en 3 a 5 frases las decisiones: "
             "por qué cada tabla, cada llave foránea y cada restricción."),
            ("Seguridad y respaldo", "Lo que puede y no puede hacer cada rol. Debajo de la "
             "tabla, el plan de respaldo y recuperación: cada cuánto se respalda, cómo se "
             "restaura y cuántos datos se pueden perder como máximo.",
             (["Rol", "Qué puede hacer", "Qué no puede hacer"], 2)),
            ("Objetos programables", "Cada procedimiento, función y disparador, con su caso de "
             "prueba y lo que devolvió.",
             (["Objeto", "Tipo", "Qué hace", "Caso de prueba", "Resultado"], 5)),
            ("Optimización", "Cada consulta antes y después, con el costo que da EXPLAIN. Debajo "
             "de la tabla, por qué el cambio la mejora.",
             (["Consulta", "Costo antes", "Qué se cambió", "Costo después"], 2)),
            ("Integración app ↔ BD", "Las operaciones que una aplicación llamaría y un ejemplo "
             "de llamada en SQL.",
             (["Operación", "Recibe", "Devuelve", "Procedimiento que la cumple"], 3)),
            ("Cómo correr los scripts", "El orden (01 a 04), el motor (PostgreSQL) y cualquier "
             "dato que haya que cargar antes."),
        ])),
        ("diagrama/QUE VA AQUI.txt", ("texto", "Aquí va «Diagrama ER.png»: el modelo exportado desde "
         "draw.io o Excalidraw, el mismo que crea 01_ddl.sql. Borren este archivo al "
         "terminar.\n")),
        ("scripts/01_ddl.sql", ("texto", _sql("01", "tablas, llaves y restricciones",
         "-- Una sección por tabla, en el orden en que se pueden crear\n"
         "-- (primero las que no tienen llaves foráneas).\n\n"
         "-- Tabla: <nombre>\n-- CREATE TABLE ...\n"))),
        ("scripts/02_roles_y_privilegios.sql", ("texto", _sql("02", "roles y privilegios",
         "-- 1. Roles\n-- CREATE ROLE ...\n\n-- 2. Privilegios de cada rol\n-- GRANT ...\n"
         "-- REVOKE ...\n\n-- 3. Prueba: lo que cada rol puede y no puede hacer\n"))),
        ("scripts/03_programables.sql", ("texto", _sql("03",
         "procedimientos, funciones y disparadores",
         "".join("-- " + t + "\n-- Qué hace: <una frase>\n-- CREATE ...\n"
                 "-- Caso de prueba: <qué se ejecuta y qué debe pasar>\n\n"
                 for t in ("Procedimiento 1", "Procedimiento 2", "Función 1",
                           "Disparador 1", "Disparador 2"))))),
        ("scripts/04_optimizacion.sql", ("texto", _sql("04", "optimización de consultas",
         "".join("-- Consulta " + n + " · ANTES\n-- EXPLAIN ...\n\n"
                 "-- Consulta " + n + " · CAMBIO (índice o reescritura)\n-- CREATE INDEX ...\n\n"
                 "-- Consulta " + n + " · DESPUÉS\n-- EXPLAIN ...\n\n" for n in ("1", "2"))))),
        ("capturas/QUE VA AQUI.txt", ("texto", "Aquí van las capturas de la ejecución: una por "
         "script (01 a 04) y una por cada caso de prueba, con la salida visible. Nómbrenlas "
         "como el script, por ejemplo 03_procedimiento1_prueba.png. Borren este archivo al "
         "terminar.\n")),
    ],
    "arq": [
        ("Documento de arquitectura.docx", ("docx", "Documento de arquitectura · CloudLite App", [
            ("Portada", "Nombre del equipo, integrantes (nombre y código de cada uno), curso, "
             "grupo y fecha."),
            ("Dominio y alcance", "El problema en 3 frases y quién lo sufre; las 3 a 5 "
             "capacidades que el sistema sí tendrá, y en una lista lo que no hará."),
            ("Modelo de servicio", "IaaS, PaaS o SaaS para cada parte, y por qué. Qué gestiona el "
             "equipo y qué el proveedor."),
            ("Decisiones de arquitectura", "Una fila por decisión importante.",
             (["Decisión", "Opciones consideradas", "Elegida y por qué", "Qué se sacrifica"],
              3)),
            ("Despliegue y contenedores", "Pegue el diagrama de despliegue. Qué servicio se "
             "contiene, cómo se construye la imagen y en qué lab se probó."),
            ("CI/CD", "Pegue el diagrama del flujo. Qué hace cada etapa del workflow y qué pasa "
             "cuando una falla."),
            ("Seguridad, monitoreo, costos y escalabilidad", "Una subsección por tema: amenazas "
             "y controles; qué se mide y con qué alerta; el costo de cada componente (Bajo, "
             "Medio o Alto, con su driver); cómo escala ante un pico."),
            ("Riesgos", "Los riesgos que quedan abiertos.",
             (["Riesgo", "Qué pasa si ocurre", "Cómo se mitiga"], 3)),
        ])),
        ("diagramas/QUE VA AQUI.txt", ("texto", "Aquí van los tres diagramas en PNG, cada uno con su "
         "archivo fuente (.drawio o .mmd): «1 componentes», «2 despliegue» y «3 ci-cd». Las "
         "cajas se llaman igual en los tres. Borren este archivo al terminar.\n")),
        ("app/QUE VA AQUI.txt", ("texto", "Aquí va el servicio mínimo (stub): el código que el "
         "Dockerfile contiene y que el workflow construye y prueba. Responde en una ruta de "
         "salud y trae al menos una prueba. Borren este archivo al terminar.\n")),
        ("contenedores/Dockerfile", ("texto",
         "# Dockerfile del servicio <nombre>: construye la imagen del stub de app/.\n"
         "# Llenen cada paso; las líneas con # son instrucciones de la plantilla.\n\n"
         "# 1. Imagen base (una oficial y liviana)\n# FROM ...\n\n"
         "# 2. Carpeta de trabajo\n# WORKDIR /app\n\n"
         "# 3. Copiar el código y las dependencias\n# COPY ...\n\n"
         "# 4. Puerto que expone el servicio\n# EXPOSE ...\n\n"
         "# 5. Comando que lo arranca\n# CMD [...]\n")),
        ("contenedores/capturas/QUE VA AQUI.txt", ("texto", "Aquí van las capturas del lab (LabEx o "
         "Killercoda) donde se ve el contenedor corriendo y respondiendo, con la fecha visible. "
         "Si la sesión del lab caducó, las capturas bastan. Borren este archivo al terminar.\n")),
        (".github/workflows/ci.yml", ("texto",
         "# Workflow de CI: construye y prueba el stub de app/ en cada push.\n"
         "# Llenen los pasos marcados con #; el despliegue puede ser simulado.\n"
         "name: ci\n"
         "on: [push]\n"
         "jobs:\n"
         "  construir-y-probar:\n"
         "    runs-on: ubuntu-latest\n"
         "    steps:\n"
         "      - uses: actions/checkout@v4\n"
         "      # - name: Instalar dependencias\n"
         "      # - name: Construir\n"
         "      # - name: Probar\n"
         "      # - name: Construir la imagen (docker build con contenedores/Dockerfile)\n")),
    ],
    "prog2": [
        ("LEEME.txt", ("texto",
         "Proyecto Integrador · Programacion II · VetCare\n\n"
         "Equipo: <nombre del equipo>\n"
         "Integrantes: <nombre y codigo de cada uno>\n"
         "Caso de matricula: <A (tambien Seminario) o B (solo Programacion II)>\n\n"
         "Como se ejecuta:\n"
         "1. Abrir la carpeta proyecto en VS Code (o el IDE del equipo).\n"
         "2. Ejecutar la clase <NombreDeLaClaseConMain>.\n"
         "3. Los datos se leen y se guardan en datos/<archivo>.\n")),
        ("proyecto/src/QUE VA AQUI.txt", ("texto",
         "Aqui van todos los archivos .java del proyecto. Una forma de ordenarlos es la de la "
         "Clase 12: modelo (Mascota, Dueno, Cita), datos (leer y escribir el archivo), servicio "
         "(las reglas) y vista (las ventanas). No incluyan las carpetas bin, out ni target. "
         "Borren este archivo al terminar.\n")),
        ("datos/QUE VA AQUI.txt", ("texto",
         "Aqui va el archivo .csv o .txt que la aplicacion lee al arrancar y en el que guarda, "
         "con registros de prueba inventados (nunca datos de personas reales). Borren este "
         "archivo al terminar.\n")),
        ("Manual de usuario.docx", ("docx", "Manual de usuario · VetCare", [
            ("Qué hace la aplicación", "En 2 o 3 frases, para alguien que no la conoce. Todo el "
             "manual: 1 a 2 páginas."),
            ("Cómo se abre", "Qué se ejecuta y qué ve la persona al arrancar. Una captura."),
            ("Registrar un dueño y su mascota", "Los pasos, con una captura."),
            ("Agendar una cita", "Los pasos, con una captura."),
            ("Buscar un expediente por su ID", "Los pasos, con una captura."),
            ("Ver el historial de una mascota", "Los pasos, con una captura."),
            ("Si se escribe un dato mal", "Qué mensaje aparece y cómo se corrige."),
            ("Dónde quedan los datos", "En qué archivo se guardan y qué pasa al cerrar y volver "
             "a abrir."),
        ])),
    ],
    "seminario": [
        ("Documento de diseno.docx", ("docx", "Documento de diseño · VetCare", [
            ("Portada", "Nombre del equipo, integrantes (nombre y código de cada uno), caso de "
             "matrícula (A o C), curso, grupo y fecha."),
            ("Requisitos", "Cada requisito, verificable: si no se puede comprobar, es un deseo.",
             (["ID", "Requisito", "RF o RNF", "Cómo se verifica", "Frase del cliente que lo "
               "origina"], 5)),
            ("Casos de uso", "Pegue el diagrama y especifique el caso principal: actor, "
             "precondición, flujo normal y flujos alternos."),
            ("Diagrama de clases", "Pegue el diagrama: clases del dominio, atributos y "
             "relaciones con su multiplicidad."),
            ("Diagrama dinámico", "Actividad o secuencia del flujo crítico: registrar, buscar y "
             "ver el historial."),
            ("Diccionario de datos", "Cada dato que guarda el sistema. Debajo de la tabla, el "
             "formato de almacenamiento: la estructura del CSV o un modelo entidad-relación "
             "básico.",
             (["Dato", "Tipo", "Obligatorio", "Regla o formato", "Ejemplo"], 5)),
            ("Mockup", "El enlace al mockup navegable (Figma, Penpot o Balsamiq) y la lista de "
             "pantallas que cubre."),
        ])),
        ("diagramas/QUE VA AQUI.txt", ("texto",
         "Aqui van los diagramas en PNG (casos de uso, clases y el dinamico), cada uno con su "
         "archivo fuente. Borren este archivo al terminar.\n")),
        ("mockup/QUE VA AQUI.txt", ("texto",
         "Aqui va Mockup.pdf: las pantallas del flujo critico exportadas desde Figma, Penpot o "
         "Balsamiq. El enlace al mockup navegable va en el documento de diseno. Borren este "
         "archivo al terminar.\n")),
        ("Plan de pruebas.docx", ("docx", "Plan de pruebas · VetCare", [
            ("Casos de prueba", "Un caso por requisito crítico, trazado a su RF.",
             (["ID", "Requisito (RF)", "Pasos", "Resultado esperado", "Resultado obtenido"], 6)),
        ])),
    ],
    "intro": [
        ("Informe final.docx", ("docx", "Informe final del proyecto", [
            ("Portada y resumen", "Título, integrantes y curso. Resumen de media página: el "
             "problema con su número, la solución en dos frases y el impacto principal."),
            ("El problema", "La cifra, cómo se obtuvo, a quién le pasa y las causas "
             "principales."),
            ("Actores y afectados", "Usuarios, quien opera, y al menos un afectado que no es "
             "usuario."),
            ("Antecedentes", "Tres soluciones que ya existen, qué hace cada una y por qué no "
             "sirve aquí."),
            ("Requisitos y criterios", "Funcionales, no funcionales, y cómo se verifica cada "
             "criterio."),
            ("Alternativas y decisión", "Al menos dos alternativas, los criterios, la elegida y "
             "qué se sacrificó."),
            ("La solución y el prototipo", "Descripción de la solución, capturas del prototipo v1 "
             "y v2, el enlace al prototipo navegable y el recorrido principal paso a paso."),
            ("Prueba y hallazgos", "Con quién se probó (solo el rol, no el nombre), qué tareas "
             "intentó, qué falló y qué se arregló."),
            ("Impacto", "Positivos con indicador y negativos con su mitigación."),
            ("Limitaciones y siguiente paso", "Lo que se decidió no hacer, con el motivo, y por "
             "dónde seguiría."),
            ("Declaración del uso de IA", "Qué se le pidió (Clases 3 y 11), qué se corrigió a "
             "mano y qué no se le entregó."),
            ("Referencias", "Lo que se citó, en el formato acordado. Nada que no se haya leído."),
        ])),
        ("prototipo/QUE VA AQUI.txt", ("texto", "Aquí van v1.png (el prototipo de baja fidelidad) y "
         "v2.png (el mejorado), o en PDF. El enlace al prototipo navegable va en la sección 7 "
         "del informe. Borren este archivo al terminar.\n")),
    ],
}


def _plantilla_docx(ruta, titulo, meta, secciones, f):
    d = Document()
    margins(d)
    banda(d, f(titulo))
    para(d, f("Proyecto Integrador · " + meta["asignatura"]),
         size=10, color=CIAN)
    para(d, f("Plantilla: reemplacen cada texto en gris por el del equipo y borren esta línea."),
         size=10, bold=True, color=AZUL, shade="E8F4FA")
    for i, sec in enumerate(secciones, 1):
        h2(d, f("%d. %s" % (i, sec[0])))
        para(d, f(sec[1]), size=10, color=GUIA_GRIS)
        if len(sec) > 2:
            encabezados, filas = sec[2]
            table(d, [f(x) for x in encabezados], [[""] * len(encabezados)
                                                   for _ in range(filas)])
    d.save(ruta)


def escribir_plantilla(est_dir: Path, curso: str, meta: dict, *, sin_tildes=False):
    """La carpeta «Plantilla de entrega»: el .zip del curso ya armado, listo para llenar."""
    f = _sin_tildes if sin_tildes else str
    base = est_dir / CARPETA_PLANTILLA
    if base.exists():
        shutil.rmtree(base, ignore_errors=True)
    base.mkdir(parents=True, exist_ok=True)
    # Nombres de archivo solo ASCII: un .zip armado en Windows puede dañar la «ó» o la «ñ».
    (base / "INSTRUCCIONES - Como usar esta plantilla.txt").write_text(
        f(_leeme_raiz(meta["asignatura"])), encoding="utf-8")
    for ruta, (tipo, *datos) in PLANTILLAS[curso]:
        destino = base / f(ruta)
        destino.parent.mkdir(parents=True, exist_ok=True)
        if tipo == "docx":
            titulo, secciones = datos
            _plantilla_docx(destino, titulo, meta, secciones, f)
        else:
            destino.write_text(f(datos[0]), encoding="utf-8")
    print("OK ->", base)


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


def table(doc, headers, rows, anchos=None):
    """Tabla con encabezado azul. `anchos` (pulgadas, uno por columna; el ancho util de la
    pagina es 6.8): sin ellos Word reparte en partes iguales y una columna de una palabra se
    come media pagina mientras la de texto largo se estira hacia abajo."""
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = "Table Grid"
    if anchos:
        t.autofit = False
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
    if anchos:
        for fila in t.rows:
            for celda, ancho in zip(fila.cells, anchos):
                celda.width = Inches(ancho)
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
    # Sin grupo, periodo, horario ni modalidad: cambian cada semestre (16/10/2026).
    para(doc, f"Código {meta['codigo']}",
         size=11, bold=True, color=GRIS, align=WD_ALIGN_PARAGRAPH.CENTER)
    para(doc, f"Docente: {DOCENTE}  ·  {CORREO}",
         size=10, color=GRIS, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    para(doc, "Versión estudiante — Entrega final en %s, en la fecha que publica el docente"
         % _plat(),
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
    para(doc, f"Código {meta['codigo']}",
         size=11, bold=True, color=GRIS, align=WD_ALIGN_PARAGRAPH.CENTER)
    para(doc, "DOCUMENTO DOCENTE — No distribuir a estudiantes. Incluye rúbrica e hitos.",
         size=10, bold=True, color=ROJO, align=WD_ALIGN_PARAGRAPH.CENTER,
         shade="FBE4E4", space_after=10)


# ---------------------------------------------------------------------------
# BD II — VetCare DB
# ---------------------------------------------------------------------------

BD2_META = {
    "titulo": "Proyecto Integrador — VetCare DB",
    "titulo_docente": "Guía docente · Proyecto Integrador — Bases de Datos II",
    "asignatura": "Bases de Datos II",
    "codigo": "FI303215",
    "dominio": "VetCare DB",
    "caso_huellitas": True,
}


#: Los hitos de la guia docente van por Clase del material, sin sesion ni fecha: el reparto en
#: sesiones y las fechas cambian cada semestre y estan en `config/calendario/`.
HITOS_TITULO = "Hitos docentes (por clase del material; las fechas están en el calendario del semestre)"
HITO_PLAZO = ("Cierra la entrega en ExamLab, en la fecha y la hora que usted publique: uno de "
              "los integrantes sube el .zip y queda para todo el equipo")


def guia_bd2(doc):
    portada_docente(doc, BD2_META)
    h2(doc, "Contexto")
    para(doc,
         "Patrón heredado de Prog. II / Seminario: PI continuo ABPr; su peso en la nota lo "
         "fija el Acuerdo pedagógico de cada semestre. "
         "Enunciados viejos viven como .gdoc en Clase 1; aquí se materializa en "
         "Clases/Proyecto Integrador/ (estudiante) + Kit docente/Proyecto Integrador/.")
    h2(doc, "Alineación RAA")
    bullets(doc, [
        "RAA1 Seguridad y respaldo → roles, privilegios, plan de backup/restore.",
        "RAA2 Procedimientos y disparadores → procs, funciones, triggers con pruebas.",
        "RAA3 Optimización → índices, reescritura, evidencia antes/después.",
    ])
    h2(doc, HITOS_TITULO)
    table(doc,
          ["Clase(s)", "Rol docente"],
          [
              ["Clases 11 y 12",
               "Revisión de avance con checklist viva + empujar integración app↔BD "
               "y casos de prueba"],
              ["Clase 13", "Publicar el caso real y revisar la entrega"],
              ["Antes de la última clase", HITO_PLAZO],
              ["Clase 15 (la última)",
               "Sustentaciones en turnos de 20 min (15 + 5), preguntas y cierre"],
          ], anchos=[1.6, 5.2])
    entrega_docente(doc, "bd2")
    h2(doc, "Rúbrica detallada (sobre 100; se lleva al peso que fija el Acuerdo pedagógico)")
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
    h2(doc, "En la sustentación, además")
    bullets(doc, [
        "Reparto del guion por bloques temáticos y quién del equipo presenta qué.",
    ])
    h2(doc, "Post-clase Padlet")
    para(doc, "Si usó Padlet en Clase 1: ⋯ → Clear posts → código → Delete (reutilizar cupo gratis).")


# ---------------------------------------------------------------------------
# Arquitectura — CloudLite App
# ---------------------------------------------------------------------------

ARQ_META = {
    "titulo": "Proyecto Integrador — CloudLite App",
    "titulo_docente": "Guía docente · Proyecto Integrador — Arquitectura de Sistemas",
    "asignatura": "Arquitectura de Sistemas Computacionales",
    "codigo": "FI303380",
    "dominio": "CloudLite App",
    # La parte practica de Arquitectura no nombra la plataforma: el estudiante ya sabe cual
    # es y como entrar —eso va en el correo de bienvenida—. Los demas cursos si la nombran.
    "plataforma": "la plataforma del curso",
}


def guia_arq(doc):
    portada_docente(doc, ARQ_META)
    h2(doc, "Contexto")
    para(doc,
         "Mismo patrón que Prog. II / Seminario; el peso lo fija el Acuerdo pedagógico de cada "
         "semestre. Enfoque microcurrículo: "
         "arquitecturas cloud, virtualización/contenedores, seguridad, rendimiento y sostenibilidad.")
    h2(doc, "Alineación RAA")
    bullets(doc, [
        "RAA1 IaaS/PaaS/SaaS → decisión de modelo de servicio en el informe.",
        "RAA2 Virtualización y distribuidos → contenedores + diagrama de despliegue.",
        "RAA3 Seguridad, rendimiento y sostenibilidad → secciones explícitas + escenario de escala.",
    ])
    h2(doc, HITOS_TITULO)
    table(doc,
          ["Clase(s)", "Rol docente"],
          [
              ["Clases 11 y 12",
               "Revisar diagramas v1 y bloquear dominios demasiado amplios + "
               "métricas/pruebas de rendimiento"],
              ["Clase 13", "Publicar el ejercicio de autoescalado y revisar la entrega"],
              ["Antes de la última clase", HITO_PLAZO],
              ["Clase 15 (la última)",
               "Sustentaciones en turnos de 20 min (15 + 5), preguntas y cierre"],
          ], anchos=[1.6, 5.2])
    entrega_docente(doc, "arq")
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

PROG2_META = {
    "titulo": "Proyecto Integrador — VetCare (aplicacion Java)",
    "titulo_docente": "Guia docente · Proyecto Integrador — Programacion II",
    "asignatura": "Programacion II",
    "codigo": "FI303204",
    "dominio": "VetCare",
}

SEMIN_META = {
    "titulo": "Proyecto Integrador — VetCare (arquitectura y diseno)",
    "titulo_docente": "Guia docente · Proyecto Integrador — Seminario de Sistemas",
    "asignatura": "Seminario de Sistemas",
    "codigo": "FI303301",
    "dominio": "VetCare",
}


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
    h2(doc, _sin_tildes(HITOS_TITULO))
    table(doc,
          ["Clase(s)", "Rol docente"],
          [
              ["Clases 11 y 12",
               "Revision cruzada (cada estudiante lee el codigo de otro) y empujar la "
               "integracion; detectar trabajos con modulos sueltos"],
              ["Clase 13", "Verificar que las validaciones existan de verdad, no en el papel"],
              ["Clase 14", "Ensayo cronometrado de la sustentacion (15 + 5 min)"],
              ["Antes de la ultima clase", _sin_tildes(HITO_PLAZO)],
              ["Clase 15 (la ultima)", "Sustentacion final en turnos de 20 min (15 + 5)"],
          ], anchos=[1.6, 5.2])
    h2(doc, "Errores frecuentes a vigilar")
    bullets(doc, [
        "Herencia forzada solo para «cumplir el requisito» (una clase Animal que nadie usa).",
        "GUI que se ve bien pero no guarda nada: pedir siempre la prueba de cerrar y reabrir.",
        "try-catch vacio que se traga el error sin avisar al usuario.",
        "Que uno solo del equipo haya programado todo: por eso las preguntas al azar a "
        "cualquier integrante en la sustentacion.",
    ])
    entrega_docente(doc, "prog2", sin_tildes=True)


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
    h2(doc, _sin_tildes(HITOS_TITULO))
    table(doc,
          ["Clase(s)", "Rol docente"],
          [
              ["Clases 11 y 12",
               "Revisar que los RF sean verificables (no deseos vagos) y la coherencia "
               "entre casos de uso y diagrama de clases"],
              ["Clase 13", "Wireframes: exigir flujo completo de una tarea real"],
              ["Clase 14", "Consolidacion del documento + ensayo cronometrado (15 + 5 min)"],
              ["Antes de la ultima clase", _sin_tildes(HITO_PLAZO)],
              ["Clase 15 (la ultima)", "Sustentacion final en turnos de 20 min (15 + 5)"],
          ], anchos=[1.6, 5.2])
    h2(doc, "Errores frecuentes a vigilar")
    bullets(doc, [
        "Requisitos no verificables («el sistema debe ser rapido») sin criterio medible.",
        "Diagrama de clases que no corresponde a los casos de uso entregados.",
        "Mockup bonito que no cubre el flujo critico (registrar → buscar → ver historial).",
        "Diccionario de datos sin tipos ni restricciones: queda inservible para quien programe.",
    ])
    entrega_docente(doc, "seminario", sin_tildes=True)


# ---------------------------------------------------------------------------
# Markdown kits (fuente editable docente)
# ---------------------------------------------------------------------------

MD_BD2 = """# Guía docente — Proyecto Integrador · Bases de Datos II

**Privado docente** · No compartir en `Clases/`.

- **Curso:** Bases de Datos II (FI303215)
- **Peso:** el que fije el Acuerdo pedagógico del semestre
- **Dominio estudiante:** VetCare DB
- **Enunciado:** `Clases/Proyecto Integrador/Enunciado Proyecto Integrador - Bases de Datos II.docx`

## Hitos (por clase del material)

Sin sesiones ni fechas: cambian cada semestre y están en el calendario (`config/calendario/`).

| Material | Foco |
|---|---|
| Clases 11 + 12 | Avance PI — checklist · Integración app ↔ BD · **preparación de la sustentación** |
| Clase 13 | Análisis de casos reales aplicado al PI |
| Antes de la última clase | **Paquete final** en ExamLab, en la fecha y la hora que publique el docente |
| Clase 15 (la última) | **Sustentación en vivo del PI** (15 min + 5 de preguntas, turno de 20) + cierre |

{{entrega}}
## Rúbrica (100 pts)

Modelo/DDL 20 · Seguridad/respaldo 15 · Programables 25 · Optimización 15 · Integración 10 · Informe+sustentación 15.
"""

MD_ARQ = """# Guía docente — Proyecto Integrador · Arquitectura

**Privado docente** · No compartir en `Clases/`.

- **Curso:** Arquitectura de Sistemas Computacionales (FI303380)
- **Peso:** el que fije el Acuerdo pedagógico del semestre
- **Dominio estudiante:** CloudLite App
- **Enunciado:** `Clases/Proyecto Integrador/Enunciado Proyecto Integrador - Arquitectura de Sistemas Computacionales.docx`

## Hitos (por clase del material)

Sin sesiones ni fechas: cambian cada semestre y están en el calendario (`config/calendario/`).

| Material | Foco |
|---|---|
| Clases 11 + 12 | Avance PI — diagramas v1 · Pruebas de rendimiento · **preparación de la sustentación** |
| Clase 13 | Escalabilidad automática aplicada al PI |
| Antes de la última clase | **Paquete final** en ExamLab, en la fecha y la hora que publique el docente |
| Clase 15 (la última) | **Sustentación en vivo del PI** (15 min + 5 de preguntas, turno de 20) + cierre |

{{entrega}}
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
    para(doc, meta["asignatura"] + " · " + meta["codigo"],
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
# universidad, trabajo, casa) desde la ficha semilla de la Clase 1. Todos los
# grupos comparten el mismo enunciado y la misma rubrica; solo cambian el dia
# y las fechas, que estan en el calendario de cada grupo. Por eso nada aqui
# lleva fecha ni codigo de grupo: las etapas se anclan a la Clase del material.
# Lo leen estudiantes de PRIMER semestre: es corto, el informe final es su
# punto clave y deja claro que en el curso no se programa (ver
# enunciado_intro_ing).
# ---------------------------------------------------------------------------

INTRO_ING_META = {
    "titulo": "Proyecto Integrador — Proyecto de equipo",
    "titulo_docente": "Guía docente · Proyecto de equipo — Introducción a la Ingeniería",
    "asignatura": "Introducción a la Ingeniería",
    "codigo": "FI300101",
    "dominio": "Un problema real del entorno, elegido por cada equipo",
}


def guia_intro_ing(doc):
    portada_docente(doc, INTRO_ING_META)
    h2(doc, "Contexto")
    para(doc,
         "16 Clases de microcurrículo; todos los grupos comparten el enunciado y la rúbrica. "
         "El proyecto es de EQUIPO —el número de integrantes lo indica usted cada semestre—, "
         "sin dominio fijo: cada equipo elige su problema real desde la ficha semilla de la "
         "Clase 1. Este documento no lleva fechas: ancla todo a la Clase del material. El "
         "calendario de cada grupo está en `config/calendario/` y el plazo de entrega lo "
         "publica usted en ExamLab.")
    para(doc,
         "En este curso no se programa. El enunciado es corto a propósito y su punto clave "
         "es el informe final; del prototipo dice lo justo (qué es, sus versiones y qué debe "
         "tener). El ejemplo de la biblioteca y los tipos de hallazgo están en las Clases 10 a "
         "12.", size=10)
    h2(doc, "Hitos docentes (por clase del material — igual en todos los grupos)")
    table(doc,
          ["Clase(s)", "Rol docente"],
          [
              ["Clase 6",
               "Cierra el Corte 1. Evaluación de corte en ExamLab (últimos 20 min) + "
               "revisar que el problema del entorno traiga cifra y a quién le pasa."],
              ["Clases 9 y 10",
               "Prototipo v1: exigir textos reales, estado vacío y de error y un destino por "
               "botón, y que se dibuje el alcance mínimo, no una idea nueva."],
              ["Clase 11",
               "Cierra el Corte 2. Evaluación de corte en ExamLab (últimos 20 min) + revisar "
               "el registro de IA (prompt, tres variantes, correcciones y descartes) y pedir "
               "la prueba con una persona ajena antes de la Clase 12."],
              ["Clase 12",
               "Sin prueba hecha no hay ficha de avance: los hallazgos se cuentan por lo que "
               "la persona hizo, con su tipo."],
              ["Clases 13 y 14",
               "Revisar impacto/mitigación y bloquear equipos que lleguen sin línea "
               "base o sin criterio de aceptación verificable."],
              ["Antes de la última clase",
               "Plazo único del informe y del prototipo en ExamLab, en la fecha y la hora que "
               "usted publique. Uno de los integrantes sube el .zip y queda para todo el "
               "equipo."],
              ["Clases 15 y 16 (cierre)",
               "Sustentaciones en turnos de 20 min por equipo (15 + 5; se corta a los 15) y "
               "cierre del proyecto. El informe ya está entregado."],
          ], anchos=[1.6, 5.2])
    entrega_docente(doc, "intro")
    h2(doc, "Rúbrica detallada")
    bullets(doc, [
        "Exposición final (100 pts; su peso, en el Acuerdo pedagógico): 5 tramos de "
        "20/20/25/20/15 — ver tabla completa en el enunciado del estudiante.",
        "Informe final (100 pts; su peso, en el Acuerdo pedagógico): 30 pts las 12 secciones "
        "completas · "
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
        "Equipos que intentan programar el prototipo: el curso pide baja fidelidad navegable, "
        "y aprender a programarlo se come el tiempo de diseñar y de probar.",
    ])
    para(doc, "Enunciado del estudiante en `Clases/Proyecto Integrador/`, común a todos "
              "los grupos.", size=10)


MD_INTRO_ING = """# Guía docente — Proyecto de equipo · Introducción a la Ingeniería

**Privado docente** · No compartir en `Clases/`.

## Producto
No hay dominio fijo: cada EQUIPO elige su propio problema real del entorno desde la
ficha semilla de la Clase 1 (cinco campos de acción, retomada en la Clase 6). Común a
todos los grupos del curso.

**Proyecto en equipo**, el mismo todo el semestre; el número de integrantes lo indica el
docente cada semestre. Es regla del proyecto, no de los talleres ni de las demás actividades.

**En este curso no se programa.** El prototipo es de baja fidelidad y navegable, y se prueba
con una persona ajena al equipo. El enunciado es corto y su punto clave es el informe final; el
detalle del prototipo está en las Clases 10 a 12.

## Hitos (por clase del material — igual en todos los grupos; las fechas, en el calendario de cada grupo)

| Clase(s) | Qué cierra |
|---|---|
| Clase 6 | Corte 1: problema y propuesta inicial + evaluación de corte en ExamLab |
| Clases 9 y 10 | Antecedentes + prototipo v1 de baja fidelidad y guion de prueba |
| Clase 11 | Corte 2: prototipo v2 con IA y su registro + evaluación de corte en ExamLab |
| antes de la Clase 12 | Prueba del prototipo v2 con una persona ajena al equipo |
| Clase 12 | Ficha de avance con los hallazgos y plan de ajustes |
| antes de la última clase | Informe final y prototipo en ExamLab, en la fecha y la hora que publique el docente |
| Clases 15 y 16 (cierre) | Corte 3: exposición final (15 + 5 min por equipo; se corta a los 15) e informe final (ya entregado en ExamLab) |

## Rúbrica (el peso de cada parte, en el Acuerdo pedagógico del semestre)
- Exposición final: 100 pts (tramos 20/20/25/20/15).
- Informe final: 100 pts (30/20/15/20/15).

## Errores frecuentes
- Problema sin cifra ni "a quién le pasa" (el error dominante).
- Alternativas descartadas sin motivo atado al dominio propio.
- Consecuencias que solo listan lo positivo.
- Prototipo sin probar con una persona ajena al equipo.
- Equipos que intentan programar el prototipo: se come el tiempo de diseñar y de probar.

{{entrega}}
Enunciado del estudiante en `Clases/Proyecto Integrador/`, común a todos los grupos.
"""

#: Primeras reglas de todos los enunciados: el equipo y quién responde en la sustentación.
REGLAS_EQUIPO = [
    "@@En equipo, no individual.@@ El número de integrantes lo indica el docente; el equipo "
    "es el mismo hasta el final. Es regla solo del proyecto: talleres, quices y parciales "
    "tienen su propia modalidad.",
    "Todos los integrantes deben poder explicar cualquier parte: en la sustentación las "
    "preguntas van al azar a cualquiera.",
]


def _bloques(doc, bloques, f):
    """Texto de «Qué van a hacer»: str = párrafo, list = viñetas, ("caja", str) = recuadro."""
    for b in bloques:
        if isinstance(b, list):
            bullets(doc, [f(x) for x in b])
        elif isinstance(b, tuple):
            para(doc, f(b[1]), shade="E8F4FA")
        else:
            para(doc, f(b))


def _enunciado_corto(doc, meta, curso, que_hacer, rubrica, reglas, *, sin_tildes=False):
    """Enunciado de una página y media: qué se hace, qué se entrega (con su plantilla), cómo
    se califica, cómo se entrega y las reglas. Nada de hitos de clase ni de actividades
    intermedias: el docente los da por otro medio (pedido del 16/10/2026)."""
    f = _sin_tildes if sin_tildes else str
    portada_estudiante(doc, meta)
    h2(doc, f("1. Qué van a hacer"))
    _bloques(doc, que_hacer, f)
    seccion_entregable(doc, curso, "2. Qué se entrega", sin_tildes=sin_tildes)
    h2(doc, f("3. Cómo se califica (100 puntos)"))
    table(doc, [f("Criterio"), f("Pts"), f("Qué se mira")],
          [[f(a), b, f(c)] for a, b, c in rubrica], anchos=[2.1, 0.5, 4.2])
    seccion_entrega(doc, curso, "4. Entrega y sustentación", sin_tildes=sin_tildes)
    h2(doc, f("5. Reglas"))
    bullets(doc, [f(x) for x in REGLAS_EQUIPO + reglas])


def enunciado_bd2(doc):
    _enunciado_corto(doc, BD2_META, "bd2", [
        "Construir @@VetCare DB@@, la base de datos de la Clínica Veterinaria «Huellitas»: el "
        "modelo, la seguridad y el respaldo, los objetos programables (procedimientos, funciones "
        "y disparadores), la optimización de consultas y la propuesta de cómo una aplicación "
        "la usaría. Todo en PostgreSQL. No se pide la aplicación: solo la base de datos.",
        ("caja", "El caso completo —las 8 entidades, las 3 reglas del negocio y los datos— está "
                 "en el @@Anexo - Caso de estudio Clínica Huellitas@@, en esta misma carpeta."),
        "Cuánto vale en la nota está en el Acuerdo pedagógico del curso.",
    ], [
        ("Modelo y DDL", "20", "El ER y el DDL coinciden; llaves y restricciones de las reglas "
         "del negocio."),
        ("Seguridad y respaldo", "15", "Roles con privilegios distintos y un plan de respaldo y "
         "recuperación."),
        ("Objetos programables", "25", "Procedimientos, funciones y disparadores que corren, con "
         "sus pruebas."),
        ("Optimización", "15", "Antes y después medidos, con la justificación."),
        ("Integración app ↔ BD", "10", "Las operaciones y un ejemplo de llamada."),
        ("Informe y sustentación", "15", "Claridad, demostración en vivo y respuestas de todos."),
    ], [
        "Herramientas gratuitas: PostgreSQL (el mismo motor de ExamLab) o DB Fiddle con "
        "PostgreSQL, y draw.io para el diagrama. No hay que instalar nada de pago.",
    ])


def enunciado_arq(doc):
    _enunciado_corto(doc, ARQ_META, "arq", [
        "Diseñar y simular el despliegue en la nube de @@CloudLite App@@, una aplicación web de "
        "un dominio que elige el equipo (citas, inventario, una academia…): sus diagramas, un "
        "servicio en contenedor y un flujo de CI/CD.",
        ("caja", "Sin nube de pago ni tarjeta: todo se hace en laboratorios gratuitos del "
                 "navegador."),
        "Cuánto vale en la nota está en el Acuerdo pedagógico del curso.",
    ], [
        ("Dominio y modelo de servicio", "15", "Un problema concreto y la decisión IaaS, PaaS o "
         "SaaS justificada."),
        ("Diagramas", "25", "Legibles, con la notación correcta y los mismos nombres en los tres."),
        ("Contenedores", "20", "El Dockerfile y el servicio corriendo en el lab."),
        ("CI/CD", "15", "Etapas claras que construyen y prueban."),
        ("Seguridad, costos y escalabilidad", "10", "Amenazas, costo por componente y cómo "
         "escala."),
        ("Documento y sustentación", "15", "Claridad, demostración y respuestas de todos."),
    ], [
        "Herramientas gratuitas del navegador: draw.io, LabEx Docker Playground o Killercoda y "
        "GitHub Actions. Nada de AWS, GCP o Azure con tarjeta, ni instalaciones obligatorias.",
    ])


def enunciado_prog2(doc):
    _enunciado_corto(doc, PROG2_META, "prog2", [
        "Construir en Java la aplicación de escritorio @@VetCare@@ para la clínica veterinaria "
        "«Huellitas». Tiene que permitir:",
        ["Registrar dueños y sus mascotas.",
         "Agendar citas.",
         "Guardar el historial clínico de cada mascota.",
         "Buscar el expediente de una mascota por su ID.",
         "Conservar los datos al cerrar y volver a abrir."],
        ("caja", "Si cursa también Seminario (@@caso A@@), es el mismo VetCare. Si solo cursa "
                 "Programación II (@@caso B@@), el docente le entrega los diagramas UML."),
        "Cuánto vale en la nota está en el Acuerdo pedagógico del curso.",
    ], [
        ("POO", "20", "Clases del dominio con encapsulamiento, y herencia con propósito."),
        ("Estructuras de datos", "15", "La colección adecuada para cada caso."),
        ("Interfaz gráfica", "20", "Ventanas con las que se completan las tareas."),
        ("Manejo de errores", "15", "La aplicación no se cae con datos inválidos."),
        ("Persistencia", "15", "Los datos siguen ahí al cerrar y volver a abrir."),
        ("Sustentación", "15", "Preguntas al azar a cualquier integrante."),
    ], [
        "Java con Swing o JavaFX, en VS Code o el IDE del equipo. Los datos se guardan en "
        "archivos .csv o .txt.",
    ], sin_tildes=True)


def enunciado_seminario(doc):
    _enunciado_corto(doc, SEMIN_META, "seminario", [
        "Diseñar los planos del sistema @@VetCare@@ para la clínica veterinaria «Huellitas»: "
        "requisitos, diagramas UML, interfaz y datos. Aquí no se programa: se diseña para que "
        "cualquier equipo pueda construirlo.",
        "Lo que pidió el veterinario jefe en la primera entrevista (es material crudo: "
        "convertirlo en requisitos es parte del trabajo):",
        ["«Necesito registrar el ID, el nombre y la especie del animal que llega.»",
         "«Necesito buscar rápido el expediente de un animal usando solo su ID.»",
         "«Quiero ver una lista de quiénes están en la sala de espera.»",
         "«Tiene que ser muy fácil de usar: no somos expertos en computadoras.»",
         "«La información no puede borrarse si se va la luz o apagamos el computador.»"],
        ("caja", "Si cursa también Programación II (@@caso A@@), es el mismo VetCare. Si solo "
                 "cursa Seminario (@@caso C@@), el proyecto termina en el diseño y el mockup: "
                 "no hay que escribir código."),
        "Cuánto vale en la nota está en el Acuerdo pedagógico del curso.",
    ], [
        ("Requisitos", "20", "RF y RNF verificables y trazables al pedido del cliente."),
        ("Modelado UML", "25", "Diagramas coherentes entre sí y con los requisitos."),
        ("Diseño de interfaz", "20", "El mockup cubre el flujo crítico y se entiende sin "
         "explicación."),
        ("Arquitectura de datos", "15", "Diccionario completo y formato justificado."),
        ("Plan de pruebas", "10", "Casos que cubren los requisitos críticos."),
        ("Sustentación", "10", "Preguntas al azar a cualquier integrante."),
    ], [
        "Herramientas gratuitas: draw.io para los diagramas y Figma, Penpot o Balsamiq para el "
        "mockup.",
    ], sin_tildes=True)


def enunciado_intro_ing(doc):
    """Introducción: lo mismo que los otros cuatro, con el informe final como punto clave
    (pedido docente, 13/10/2026) y la exposición calificada por tramos. En este curso no se
    programa: el prototipo se explica en dos frases y su detalle vive en las Clases 10 a 12."""
    portada_estudiante(doc, INTRO_ING_META)
    h2(doc, "1. Qué van a hacer")
    para(doc,
         "Una @@propuesta de mejora tecnológica@@ para un problema real de su entorno —el "
         "barrio, la universidad, el trabajo o la casa—, que se construye clase a clase y se "
         "defiende en la última sesión. Este curso se aprueba con este proyecto, no con un "
         "examen final.")
    para(doc,
         "@@En este curso no se programa.@@ La solución se diseña y se dibuja como "
         "@@prototipo@@: un dibujo que otra persona puede recorrer como si funcionara (en papel, "
         "Excalidraw, draw.io o Google Slides), que se prueba con una persona ajena al equipo. "
         "No hace falta saber programar ni instalar nada.", shade="E8F4FA")
    para(doc, "Se califican el informe final y la exposición final. Cuánto vale cada uno en la "
              "nota está en el Acuerdo pedagógico del curso.")

    seccion_entregable(doc, "intro", "2. Qué se entrega")
    h3(doc, "El informe final: el punto clave")
    table(doc, ["#", "Sección", "Tiene que contener"],
          [[str(i), t, g] for i, (t, g) in enumerate(
              [(s[0], s[1]) for s in PLANTILLAS["intro"][0][1][2]], 1)],
          anchos=[0.4, 1.8, 4.6])

    h2(doc, "3. Cómo se califica")
    bullets(doc, [
        "@@Informe final:@@ las 12 secciones completas y coherentes entre sí.",
        "@@Exposición final (100 puntos):@@ por tramos, así:",
    ])
    table(doc, ["Tramo", "Qué se busca", "Pts"], [
        ["1 · El problema con su cifra", "Arranca por el problema, con un número y de dónde "
         "salió.", "20"],
        ["2 · Los afectados y la decisión", "Un afectado que no es usuario y qué se "
         "sacrificó.", "20"],
        ["3 · La solución y el prototipo en vivo", "Recorren el prototipo navegable cumpliendo "
         "una tarea de principio a fin.", "25"],
        ["4 · Lo que falló y lo que aprendimos", "Qué falló en la prueba, qué se arregló y qué "
         "no.", "20"],
        ["5 · Impacto y siguiente paso", "Impacto positivo con número y el negativo con su "
         "mitigación.", "15"],
    ], anchos=[2.1, 4.1, 0.6])

    seccion_entrega(doc, "intro", "4. Entrega y exposición")
    h2(doc, "5. Reglas")
    bullets(doc, REGLAS_EQUIPO + [
        "Hablan todos los integrantes, y cada uno responde sobre su propio tramo.",
        "Herramientas gratuitas y en el navegador: Google Drive, Excalidraw, draw.io y Google "
        "Slides. IA solo en las Clases 3 y 11, declarando qué se pidió y qué se corrigió; "
        "nunca con datos personales.",
    ])


# Clave de cada curso en ENTREGA/PLANTILLAS, y si su material va sin tildes.
CLAVE_CURSO = {
    "Bases de Datos II": ("bd2", False),
    "Arquitectura de Sistemas Computacionales": ("arq", False),
    "Programacion II": ("prog2", True),
    "Seminario de Sistemas": ("seminario", True),
    "Introduccion a la Ingenieria": ("intro", False),
}


def build_one(curso_dir: Path, meta: dict, build_est, build_doc, md_text: str, slug: str):
    est_dir = curso_dir / "Clases" / "Proyecto Integrador"
    kit_dir = curso_dir / "Kit docente" / "Proyecto Integrador"
    est_dir.mkdir(parents=True, exist_ok=True)
    kit_dir.mkdir(parents=True, exist_ok=True)

    # Sin el periodo en el nombre: el mismo archivo sirve cualquier semestre (16/10/2026).
    est_path = est_dir / f"Enunciado Proyecto Integrador - {slug}.docx"
    doc_path = kit_dir / f"Guia Docente PI - {slug}.docx"
    md_path = kit_dir / f"Guia Docente PI - {slug}.md"

    global NOMBRE_PLATAFORMA
    NOMBRE_PLATAFORMA = meta.get("plataforma", "ExamLab")

    d1 = Document()
    margins(d1)
    build_est(d1)
    d1.save(est_path)
    clave, sin_tildes = CLAVE_CURSO[slug]
    escribir_plantilla(est_dir, clave, meta, sin_tildes=sin_tildes)

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

MD_PROG2 = """# Guía docente — Proyecto Integrador · Programación II

**Privado docente** · No compartir en `Clases/`.

## Producto
**VetCare** — aplicación de escritorio en Java para la Clínica Veterinaria «Huellitas».
PI **compartido con Seminario de Sistemas**: mismo producto, distinto entregable
(aquí el software, allá los planos).

## Casos de matrícula
- **A** (ambas materias): aquí se califica el código; los diagramas se califican en Seminario.
- **B** (solo Prog II): el docente entrega los diagramas UML ya hechos; el estudiante programa.
- **C** (solo Seminario): no aplica en este curso.

## Hitos (por clase del material)
Sin sesiones ni fechas: cambian cada semestre y están en el calendario (`config/calendario/`).

| Material | Foco |
|---|---|
| Clases 11 + 12 | Avance de código + revisión cruzada e integración de módulos |
| Clase 13 | Excepciones y validaciones |
| Clase 14 | Versión final + ensayo |
| Antes de la última clase | **Paquete final** en ExamLab, en la fecha y la hora que publique el docente |
| Clase 15 (la última) | Sustentación 15 + 5 min |

## Rúbrica (100 pts)
POO 20 · Estructuras de datos 15 · GUI 20 · Manejo de errores 15 · Persistencia 15 · Sustentación 15

## Errores frecuentes
- Herencia forzada solo para cumplir el requisito.
- GUI que no persiste: pedir siempre la prueba de cerrar y reabrir.
- `try-catch` vacío que oculta el error.
- Que uno solo del equipo haya programado todo → preguntas al azar a cualquier integrante en la sustentación.

{{entrega}}
Enunciado del estudiante en `Clases/Proyecto Integrador/`.
"""

MD_SEMIN = """# Guía docente — Proyecto Integrador · Seminario de Sistemas

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

## Hitos (por clase del material)
Sin sesiones ni fechas: cambian cada semestre y están en el calendario (`config/calendario/`).

| Material | Foco |
|---|---|
| Clases 11 + 12 | Requisitos + casos de uso y UML avanzado |
| Clase 13 | Wireframes y mockup |
| Clase 14 | Documento consolidado + ensayo |
| Antes de la última clase | **Paquete final** en ExamLab, en la fecha y la hora que publique el docente |
| Clase 15 (la última) | Sustentación 15 + 5 min |

## Rúbrica (100 pts)
Requisitos 20 · UML 25 · Interfaz 20 · Arquitectura de datos 15 · Plan de pruebas 10 · Sustentación 10

## Errores frecuentes
- Requisitos no verificables («debe ser rápido») sin criterio medible.
- Diagrama de clases que no corresponde a los casos de uso.
- Mockup que no cubre el flujo crítico (registrar → buscar → ver historial).
- Diccionario de datos sin tipos ni restricciones.

{{entrega}}
Enunciado del estudiante en `Clases/Proyecto Integrador/`.
"""


# Las guias en Markdown toman su seccion de entrega de la plantilla de cada curso (ENTREGA).
MD_BD2 = MD_BD2.replace("{{entrega}}", _md_entrega("bd2"))
MD_ARQ = MD_ARQ.replace("{{entrega}}", _md_entrega("arq"))
MD_PROG2 = MD_PROG2.replace("{{entrega}}", _md_entrega("prog2"))
MD_SEMIN = MD_SEMIN.replace("{{entrega}}", _md_entrega("seminario"))
MD_INTRO_ING = MD_INTRO_ING.replace("{{entrega}}", _md_entrega("intro"))
assert all("{{entrega}}" not in _m for _m in (MD_BD2, MD_ARQ, MD_PROG2, MD_SEMIN, MD_INTRO_ING))

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
