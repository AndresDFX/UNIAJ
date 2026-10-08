# -*- coding: utf-8 -*-
"""Genera TODO el material de Programacion II 2026-2 (PI VetCare, Java).

Por que existe
--------------
El material del curso venia del periodo anterior: se le habian cambiado los nombres de
carpeta al temario 2026-2, pero el contenido interno seguia siendo el de la secuencia
vieja, corrido una clase (la carpeta "Clase 3 - Pilas y colas" contenia ArrayList, etc.)
y con la agenda de un bloque de 160 min que ya no existe. Ademas el plan 2026-2 fusiono
temas (Mapas+GUI en la Clase 4, Refactorizacion+Persistencia en la 9) y agrego otros
(Documentacion y QA, Revision cruzada) que no tenian material.

Este build deja el curso alineado al plan y, sobre todo, REGENERABLE: cualquier cambio
de convencion se aplica una vez aqui y no a mano en 14 carpetas. Mismo patron que
`build_uniajc_bd2_all.py` y `build_uniajc_arq_clases_batch.py`.

Salidas
-------
  Clases/Clase N - <slug>/Presentacion.pptx      (estudiante)
  Clases/Clase N - <slug>/Taller PI - Clase N - VetCare.docx
  Kit docente/Clase N/Guion Docente ….md|.docx   (regla de oro: teoria desarrollada)
  Kit docente/Clase N/Quiz ….docx + Quiz … CLAVE DOCENTE.docx
  Kit docente/Clase N/Solucion Taller ….md|.docx
  Kit docente/Clase N/Codigo/<archivo>.java
  Kit docente/Clase N/Guia aplicacion Parcial N ….md|.docx   (dias 5/10/15)

Los datos pedagogicos viven en `prog2_clases_data.py` (una sola fuente).
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLIDES = Path(__file__).resolve().parent
sys.path.insert(0, str(SLIDES))

from uniajc_slides_engine import (  # noqa: E402
    block_timeline_slide,
    box_note_slide,
    checklist_slide,
    class_cover,
    closing_slide,
    concepto_slide,
    content_slide,
    herramientas_slide,
    notas,
    new_prs,
    pseudo_code_slide,
    steps_visual_slide,
)
from uniajc_quiz_helpers import clave_text, q_abierta, q_om, q_vf  # noqa: E402
from docx import Document  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.oxml import OxmlElement  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.shared import Pt as DocPt, RGBColor  # noqa: E402

from prog2_clases_data import CLASES  # noqa: E402
from prog2_examlab_data import EXAMLAB as TALLERES_EXAMLAB  # noqa: E402
import examlab_talleres  # noqa: E402

CURSO = ROOT / "Programacion II"
CLASES_DIR = CURSO / "Clases"
KIT_DIR = CURSO / "Kit docente"

AZUL = RGBColor(0x09, 0x52, 0x92)
CIAN_D = RGBColor(0x26, 0x9C, 0xCB)
GRIS = RGBColor(0x2B, 0x2B, 0x2B)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
ROJO = RGBColor(0xA0, 0x20, 0x30)
FONT = "Calibri"
EXAMLAB = "ExamLab (https://uniaj.examlab.workers.dev/)"

PARCIALES = {
    5: ("Parcial 1", "Parcial 1 - POO colecciones e interfaces GUI.docx"),
    10: ("Parcial 2", "Parcial 2 - Eventos patrones QA y persistencia.docx"),
    15: ("Parcial 3", "Parcial 3 - Integracion excepciones y cierre de proyecto.docx"),
}


# ----------------------------------------------------------------- helpers docx
def shade(p, fill):
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), fill)
    pPr.append(shd)


def run(r, *, size=11, bold=False, color=GRIS):
    r.font.name = FONT
    r._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    r.font.size = DocPt(size)
    r.bold = bold
    r.font.color.rgb = color


def para(doc, text, *, size=11, bold=False, color=GRIS, space_after=6, shade_fill=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = DocPt(space_after)
    if shade_fill:
        shade(p, shade_fill)
    r = p.add_run(text)
    run(r, size=size, bold=bold, color=color)
    return p


def banda(doc, text):
    return para(doc, "  " + text, size=13, bold=True, color=BLANCO,
                shade_fill="095292", space_after=8)


def add_inline_docx(p, text, *, size=11, color=GRIS):
    """Soporta @@negrita@@, misma convencion que el motor de slides."""
    for part in re.split(r"(@@.*?@@)", text):
        if not part:
            continue
        r = p.add_run()
        if part.startswith("@@") and part.endswith("@@"):
            r.text = part[2:-2]
            run(r, size=size, bold=True, color=color)
        else:
            r.text = part
            run(r, size=size, color=color)


def bullets(doc, items):
    for it in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = DocPt(2)
        add_inline_docx(p, str(it))


def _resumen(bullets_, max_chars=115, max_items=5):
    """La teoria del guion es larga a proposito; la slide lleva solo la idea central.

    Dos filtros que la slide del ESTUDIANTE necesita y el guion no:
    - Se descarta el parrafo «Error tipico del docente...»: es material de preparacion
      del docente y no tiene ningun sentido proyectado al grupo. Se estaba filtrando.
    - Se corta a `max_items` vinetas (regla del workspace: maximo 5 por diapositiva);
      el desarrollo completo sigue estando en el guion.
    """
    out = []
    for b in bullets_:
        if re.match(r"\s*Error\s+(tipico|típico|de)\s+d(el|e)\s+docente", b, re.I):
            continue
        first = re.split(r"(?<=[a-záéíóúü0-9\)])\.\s", b, maxsplit=1)[0].strip()
        if len(first) > max_chars or len(first) < 12:
            base = b if len(first) < 12 else first
            first = base[:max_chars].rsplit(" ", 1)[0].rstrip(":,;") + "…"
        out.append(first)
    return out[:max_items]


def _quiz_items(c):
    out = []
    for q in c.get("quiz", []):
        t = q.get("tipo")
        if t == "om":
            out.append(q_om(q["q"], q.get("opciones", []), q.get("clave", "")))
        elif t == "vf":
            out.append(q_vf(q["q"], q.get("clave", "V")))
        else:
            out.append(q_abierta(q["q"], q.get("clave", "")))
    return out


# ----------------------------------------------------------------------- slides
import teoria_a_slides as TS
import visuales
from prog2_conceptos_data import CONCEPTOS
import prog2_codigo_laminas as CODIGO_LAMINAS
from prog2_visuales_data import VISUALES

#: Laminas fijas antes de la teoria: portada, encuadre y mapa del bloque. El guion numera
#: sus «[Slide N]» a partir de aqui; si cambia el arranque del deck, cambia este numero.
PRIMERA_TEORIA = 4


def _parrafos(c):
    """Los parrafos de teoria de la clase, en el orden en que los indexa `CONCEPTOS`."""
    vin = list(c.get("teoria", []))
    fund = (c.get("fundamento") or "").strip()
    if fund:
        vin += [p.strip() for p in fund.split("\n\n") if len(p.strip()) > 120]
    return vin


# ------------------------------------------------------------ codigo por lamina
def laminas_de_codigo(c):
    """`[(k, titulo, lineas, notas)]`: los programas completos que van detras del concepto k.

    Cada lamina es un `Main.java` que corre solo (`prog2_codigo_laminas`), no un recorte del
    archivo de la clase: el estudiante lo copia de la lamina y corre sin nada mas.
    """
    return [(e["k"], e["titulo"], CODIGO_LAMINAS.lineas(e), CODIGO_LAMINAS.notas(e))
            for e in CODIGO_LAMINAS.CODIGO.get(c["n"], [])]


def _teoria_slides(c):
    """Las laminas de teoria de la clase: un concepto por lamina y su codigo detras.

    Cada concepto lleva el titulo y las ideas que decide `prog2_conceptos_data`; el parrafo
    completo (y lo que `teoria_a_slides` aparta como frase al docente) va a sus notas. Detras
    de cada concepto, los programas completos que lo muestran (cada uno corre solo).
    """
    vin = _parrafos(c)
    codigo = laminas_de_codigo(c)
    out = []
    for k, (indices, titulo, ideas) in enumerate(CONCEPTOS.get(c["n"], [])):
        # Las notas llevan los parrafos tal cual: partidos en frases por `a_vinetas` se
        # cortaban por las comas del codigo citado («add(0» / «MascotaDelAmigo)»).
        desarrollo = ["DESARROLLO (para explicarlo, no se proyecta):"] + [vin[i] for i in indices]
        out.append((titulo, list(ideas), desarrollo, "content"))
        for kk, tit, lineas, notas_cod in codigo:
            if kk == k:
                out.append((tit, lineas, notas_cod, "codigo"))
    return out


def _errores_docente(c):
    return [b for b in _parrafos(c) if re.match(r"\s*Error\s+t[ií]pico", b, re.I)]


def _apoyo_por_diapositiva(c, base=PRIMERA_TEORIA):
    """Apoyo puntual por diapositiva, en el orden y con el numero real del deck."""
    slides = _teoria_slides(c)
    if not slides:
        return ""
    L = ["## Apoyo por diapositiva", "",
         "Las ideas de cada concepto estan proyectadas y el desarrollo completo esta en las "
         "notas del presentador de su lamina. Aqui va, por lamina y en su orden, lo que hay "
         "que subrayar.", ""]
    for j, (titulo, vin, notas_, tipo) in enumerate(slides):
        num = f"[Slide {base + j}] " if base else ""
        if tipo == "codigo":
            L.append(f"**{num}{titulo}** — programa completo ({len(vin)} lineas): se copia en "
                     "Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida "
                     "esperada esta en las notas del presentador.")
        else:
            # Al guion baja solo lo que le habla al docente (que subrayar, como dictarlo); el
            # desarrollo completo esta en las notas del presentador de la lamina.
            _, al_docente, _ = TS.a_vinetas("\n\n".join(notas_[1:]))
            L.append(f"**{num}{titulo}** — {len(vin)} ideas proyectadas; el desarrollo, en "
                     "las notas del presentador.")
            for x in al_docente:
                L.append(f"  - Subrayar: {x}")
        L.append("")
    err = _errores_docente(c)
    if err:
        L += ["## Errores tipicos del docente que no domina el tema", "",
              "Material de preparacion: no se proyecta.", ""]
        L += [f"- {e}" for e in err]
        L.append("")
    return "\n".join(L)


# Ronda 4: el deck de clase no nombra el proyecto (VetCare / Huellitas / PI). El ejemplo se
# queda con una descripcion generica del dominio. Solo se aplica al texto PROYECTADO: guion,
# taller, solucion y quiz siguen nombrando el proyecto.
_GEN = [
    (r"VetCare Huellitas", "Clinica"),
    (r"(Cl[ií]nica Veterinaria) Huellitas", r"\1"),
    (r'(?<=")VetCare\b', "Clinica"),
    (r'(?<=" )VetCare\b', "Clinica"),
    (r"(?<== )VetCare\b", "Clinica"),
    (r"\bEquipo VetCare\b", "Equipo Clinica"),
    (r"\bpackage vetcare\b", "package clinica"),
    (r"\bvetcare\.", "clinica."),
    (r"VetCare(?=[A-Z])", "Clinica"),           # VetCareApp -> ClinicaApp
    (r"(?<=[a-z])VetCare\b", "Clinica"),        # RepositorioVetCare -> RepositorioClinica
    (r"\bvetcare\b", "clinica"),
    (r"la cl[ií]nica veterinaria Huellitas \(VetCare\)", "una clinica veterinaria"),
    (r"(cl[ií]nica(?: veterinaria)?) Huellitas", r"\1"),
    (r"\b[Ee]n Huellitas\b", "en la clinica"),
    (r"\bde Huellitas\b", "de la clinica"),
    (r"\bHuellitas\b", "la clinica"),
    (r"\b(?:el )?PI de VetCare\b", "el sistema de la clinica"),
    (r"\bdominio VetCare\b", "dominio de la clinica"),
    (r"\b[Ee]n VetCare\b", "en el sistema de la clinica"),
    (r"\bde VetCare\b", "del sistema de la clinica"),
    (r"\ba VetCare\b", "al sistema de la clinica"),
    (r"\bsobre VetCare\b", "sobre el sistema de la clinica"),
    (r"\bel VetCare\b", "el sistema de la clinica"),
    (r"\bsu VetCare\b", "su sistema de la clinica"),
    (r"\bVetCare\b", "el sistema de la clinica"),
    (r"\b(?:del|el) Proyecto Integrador\b", "del proyecto"),
    (r"\bProyecto Integrador\b", "proyecto"),
    (r"\bdel PI\b", "del proyecto"),
    (r"\bel PI\b", "el proyecto"),
    (r"\bPI\b", "proyecto"),
]


def _gen(x):
    if isinstance(x, str):
        for a, b in _GEN:
            x = re.sub(a, b, x)
        # mayuscula inicial si la sustitucion dejo «el sistema…» al comienzo de frase
        x = re.sub(r"(^|[.!?]\s+)(en el sistema|el sistema|del sistema|al sistema|la clinica|en la clinica)",
                   lambda m: m.group(1) + m.group(2)[0].upper() + m.group(2)[1:], x)
        return x
    if isinstance(x, list):
        return [_gen(y) for y in x]
    if isinstance(x, tuple):
        return tuple(_gen(y) for y in x)
    return x

def build_pptx(c):
    c = {k: (_gen(v) if k != 'n' else v) for k, v in c.items()}
    n = c["n"]
    if n in PARCIALES:
        prs = new_prs()
        class_cover(prs, PARCIALES[n][0], subtitulo="Solo evaluacion", clase_n=n, idx=1)
        content_slide(prs, "Indicaciones", [
            "Hoy es **solo Parcial** (virtual sincrono por Meet).",
            "No hay tema nuevo en esta sesion.",
            "Duracion sugerida: **90–100 min** dentro del bloque de 120.",
            "Entra lo visto en el corte hasta hoy; el enunciado y el canal de entrega se comparten al empezar.",
        ], idx=2)
        closing_slide(prs, f"{PARCIALES[n][0]} · Clase {n}",
                      ["Enfocados en la evaluacion del corte",
                       "El tema continua la proxima clase"],
                      accent="Solo evaluacion")
        out_dir = CLASES_DIR / f"Clase {n} - {PARCIALES[n][0]}"
        out_dir.mkdir(parents=True, exist_ok=True)
        prs.save(str(out_dir / "Presentacion.pptx"))
        print("PPTX", out_dir.name)
        return

    prs = new_prs()
    class_cover(prs, c["titulo"], subtitulo=c["subtitulo"], clase_n=n, idx=1)
    idx = 2
    # El deck lleva solo el tema. El taller del PI es opcional y vive en su carpeta
    # (Taller ….docx en Clases/Clase N/; Solucion, Quiz y ExamLab en Kit docente/).
    content_slide(prs, "Encuadre de hoy", [
        f"**Tema de hoy:** {c['titulo']} — {c['subtitulo']}",
        f"Herramienta: **{c['herramienta']}** · Bloque **120 min**",
        "Primero el concepto, despues el codigo que lo muestra y la demo en vivo.",
        "Todo con el mismo dominio: una clinica veterinaria.",
    ], idx=idx); idx += 1
    block_timeline_slide(prs, "Mapa del bloque de hoy (120 min)", [
        ("0-10", "Encuadre y repaso de la clase anterior"),
        ("10-40", "Teoria Core del tema de hoy"),
        ("40-60", "Demo en vivo sobre el tema"),
        ("60-105", "Practica sobre el codigo de la demo"),
        ("105-120", "Repaso de conceptos y cierre"),
    ], idx=idx); idx += 1
    # El guion numera sus «[Slide N]» desde PRIMERA_TEORIA con esta misma lista: si alguien
    # agrega una lamina antes de la teoria y no mueve la constante, el build falla aqui en
    # vez de publicar un guion mal numerado.
    assert idx == PRIMERA_TEORIA, f"Clase {n}: la teoria empieza en {idx}, no en {PRIMERA_TEORIA}"
    for _t, _items, _notas, _tipo in _teoria_slides(c):
        if _tipo == "codigo":
            _s = pseudo_code_slide(prs, _t, _items, idx=idx, lenguaje="Java",
                                   archivo=CODIGO_LAMINAS.ARCHIVO,
                                   interlineado_pt=CODIGO_LAMINAS.INTERLINEADO,
                                   minimo_pt=CODIGO_LAMINAS.MINIMO_PT)
        else:
            # Un concepto por lamina, con su visual si lo tiene: los pasos de su animacion
            # (aparecen con cada clic del docente) o, sin animacion, la ilustracion generada
            # del concepto (`content_slide`). Sin ninguna de las dos, texto a lo ancho.
            _imgs, _pie = visuales.imagenes(VISUALES, n, _t)
            _s = concepto_slide(prs, _t, _items, imagenes=_imgs, pie=_pie, idx=idx)
        if _s is not None and _notas:
            notas(_s, list(_notas))
        idx += 1
    content_slide(prs, "Demo del dia", [
        f"**Herramienta:** {c['herramienta']}",
        f"**Demo:** {c['demo']}",
        "Mismo dominio de la clinica — no otro ejemplo.",
    ], idx=idx); idx += 1
    closing_slide(prs, f"Clase {n} · {c['titulo']}", [
        c["subtitulo"],
        "Repasa las laminas de concepto y el codigo de la demo",
        "Siguiente clase: continuamos el hilo del tema",
    ], accent="Teoria al servicio del proyecto")
    out_dir = CLASES_DIR / f"Clase {n} - {c['slug']}"
    out_dir.mkdir(parents=True, exist_ok=True)
    prs.save(str(out_dir / "Presentacion.pptx"))
    print("PPTX", out_dir.name)


# ---------------------------------------------------------------------- taller
def build_taller_docx(c):
    n = c["n"]
    if n in PARCIALES:
        return
    doc = Document()
    banda(doc, f"Taller PI · Clase {n} · Programacion II")
    para(doc, c["titulo"], size=14, bold=True, color=AZUL)
    para(doc, "Hilo conductor: Proyecto Integrador VetCare (no es un ejercicio suelto).",
         size=11, bold=True)
    para(doc, f"Herramienta: {c['herramienta']}")
    para(doc, f"Hoy avanzamos el PI en: {c['hito_pi']}", shade_fill="FFF8D6")
    para(doc, "Modalidad de trabajo: individual por defecto. El docente puede autorizar equipos de 2 o 3 integrantes; en ese caso el artefacto puede ser compartido, pero la entrega en ExamLab siempre es individual (cada estudiante responde las preguntas abiertas con sus propias palabras) y cualquier integrante debe poder explicar cualquier parte en 60 segundos.", size=10, shade_fill="EDEDED")
    para(doc, "1. Contexto / por que importa al PI", size=12, bold=True, color=AZUL)
    bullets(doc, c.get("contexto") or ["Trabaje sobre su propio VetCare."])
    para(doc, "2. Punto de partida", size=12, bold=True, color=AZUL)
    bullets(doc, c.get("escenario") or ["Use el codigo que ya tiene del avance anterior."])
    para(doc, "3. Pasos guiados", size=12, bold=True, color=AZUL)
    bullets(doc, c["taller"])
    para(doc, "4. Entregable", size=12, bold=True, color=AZUL)
    para(doc, c["entregable"], shade_fill="E8F4FA")
    para(doc, "5. Criterios de exito", size=12, bold=True, color=AZUL)
    bullets(doc, c.get("criterios") or ["Avance real y verificable de su VetCare."])
    para(doc, "6. Antes de entregar (autochequeo)", size=12, bold=True, color=AZUL)
    bullets(doc, [f"☐ {p}" for p in c.get("pistas", [])])
    para(doc, "7. Entrega", size=12, bold=True, color=AZUL)
    p = doc.add_paragraph()
    add_inline_docx(p, f"@@Sube tu taller en {EXAMLAB}@@ — domingo 23:59. Un envio por estudiante.")
    _taller_el = TALLERES_EXAMLAB.get(n)
    if _taller_el:
        examlab_talleres.render_estudiante(
            doc, _taller_el, para=para, bullets=bullets,
            add_inline=add_inline_docx, color_titulo=AZUL,
            titulo="8. Que vas a resolver en ExamLab",
        )
    out_dir = CLASES_DIR / f"Clase {n} - {c['slug']}"
    out_dir.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_dir / f"Taller PI - Clase {n} - VetCare.docx"))


# -------------------------------------------------------------------- solucion
def build_solucion_docx(c):
    n = c["n"]
    if n in PARCIALES or not c.get("solucion_pasos"):
        return
    kit = KIT_DIR / f"Clase {n}"
    kit.mkdir(parents=True, exist_ok=True)
    stem = f"Solucion Taller Clase {n} - VetCare"
    lines = [f"# Solucion Taller · Clase {n} · {c['titulo']}", "",
             "> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.", "",
             "## Solucion paso a paso"]
    lines += [f"{i}. {s}" for i, s in enumerate(c["solucion_pasos"], 1)]
    lines += ["", "## Rubrica corta"] + [f"- [ ] {r}" for r in c.get("solucion_rubrica", [])]
    lines += ["", "## Errores frecuentes"] + [f"- {e}" for e in c.get("solucion_errores", [])]
    if c.get("codigo_archivo"):
        lines += ["", f"Codigo de apoyo: `Kit docente/Clase {n}/Codigo/{c['codigo_archivo']}`"]
    (kit / f"{stem}.md").write_text("\n".join(lines), encoding="utf-8")

    doc = Document()
    banda(doc, f"Solucion Taller · Clase {n} · VetCare")
    para(doc, "DOCUMENTO DOCENTE — PRIVADO (no va en Clases/)", bold=True,
         color=ROJO, shade_fill="FBE4E4")
    para(doc, c["titulo"], size=12, bold=True, color=AZUL)
    para(doc, "Solucion paso a paso", size=12, bold=True, color=AZUL)
    bullets(doc, c["solucion_pasos"])
    para(doc, "Rubrica corta", size=12, bold=True, color=AZUL)
    bullets(doc, ["[ ] " + r for r in c.get("solucion_rubrica", [])])
    para(doc, "Errores frecuentes", size=12, bold=True, color=AZUL)
    bullets(doc, c.get("solucion_errores", []))
    doc.save(str(kit / f"{stem}.docx"))


# ------------------------------------------------------------------------ quiz
def build_quiz(c):
    n = c["n"]
    items = _quiz_items(c)
    if n in PARCIALES or not items:
        return
    kit = KIT_DIR / f"Clase {n}"
    kit.mkdir(parents=True, exist_ok=True)

    doc = Document()
    banda(doc, f"Quiz · Clase {n} · {c['titulo']}")
    para(doc, "Version estudiante — SOLO enunciados. No proyectar la Clave docente.",
         size=10, bold=True, color=AZUL, shade_fill="E8F4FA")
    para(doc, "Individual · 8-10 min.", size=10)
    for i, it in enumerate(items, 1):
        para(doc, f"{i}. {it['q']}", size=11, bold=True)
        if it.get("tipo") == "om":
            for op in it.get("opciones", []):
                para(doc, "     " + str(op), size=10.5, space_after=2)
        elif it.get("tipo") == "vf":
            para(doc, "     ( ) Verdadero    ( ) Falso", size=10.5, space_after=2)
        else:
            para(doc, "     Respuesta: ______________________________", size=10.5, space_after=2)
    doc.save(str(kit / f"Quiz Clase {n} - VetCare.docx"))

    dk = Document()
    banda(dk, f"CLAVE DOCENTE · Quiz Clase {n}")
    para(dk, "DOCUMENTO DOCENTE — PRIVADO. No proyectar.", bold=True,
         color=ROJO, shade_fill="FBE4E4")
    for i, it in enumerate(items, 1):
        para(dk, clave_text(it, i), size=10, shade_fill="E8F4FA")
    dk.save(str(kit / f"Quiz Clase {n} - CLAVE DOCENTE.docx"))


# ---------------------------------------------------------------------- codigo
def build_codigo(c):
    n = c["n"]
    if n in PARCIALES or not c.get("codigo_fuente"):
        return
    cod = KIT_DIR / f"Clase {n}" / "Codigo"
    cod.mkdir(parents=True, exist_ok=True)
    nombre = c.get("codigo_archivo") or f"Clase{n}Demo.java"
    (cod / nombre).write_text(c["codigo_fuente"], encoding="utf-8")


# ---------------------------------------------------------------------- capturas
def _escribir_readme_capturas(c, cap):
    """README de Capturas/ con que imagen va aqui, como tomarla y con que nombre.

    La carpeta se creaba vacia en las 15 clases, y una carpeta vacia no existe en
    git: al clonar el repo desaparecia, asi que el docente no tenia donde leer que
    captura se espera. Es el mismo README que ya escriben Arquitectura y BD II, y
    se reescribe en cada build para que refleje la herramienta y la demo actuales.
    """
    n = c["n"]
    titulo = f"Capturas de la Clase {n} — Programacion II"
    L = [titulo, "=" * len(titulo), ""]
    if n in PARCIALES:
        L += [f"Dia de {PARCIALES[n][0]}: solo evaluacion, sin demo que capturar.", "",
              "Unica captura util, para el registro del corte:",
              "  - La pantalla de ExamLab con el parcial cerrado y las entregas recibidas.",
              "  - Recortar nombres y correos antes de guardar. No se proyecta.", ""]
    else:
        L += ["Ninguna de estas imagenes se proyecta: son el registro del docente y la",
              "referencia del nivel esperado para el proximo semestre.", "",
              f"1) demo-clase{n:02d}.png — la herramienta del dia en uso",
              f"   - Abrir {c['herramienta']}.",
              f"   - Repetir la demo del bloque 40-60: {c['demo']}",
              "   - Capturar solo la ventana util, no el escritorio completo.",
              "   - Recortar a ~1200 px de ancho y guardar aqui con ese nombre.", "",
              f"2) taller-clase{n:02d}.png — evidencia de avance de un estudiante",
              "   - Con permiso del estudiante, capturar su artefacto a medio construir.",
              "   - Recortar nombre y correo antes de guardar.", ""]
    L += ["Despues de agregar una imagen, regenerar el kit:",
          "   python config/slides/build_uniajc_prog2_all.py", ""]
    cap.mkdir(parents=True, exist_ok=True)
    (cap / "README.txt").write_text("\n".join(L), encoding="utf-8")


# ---------------------------------------------------------------------- guiones
def build_guion_md(c):
    n = c["n"]
    kit = KIT_DIR / f"Clase {n}"
    kit.mkdir(parents=True, exist_ok=True)
    _escribir_readme_capturas(c, kit / "Capturas")

    if n in PARCIALES:
        titulo, archivo = PARCIALES[n]
        md = f"""# Guia de aplicacion · Clase {n} · {titulo} (solo evaluacion)

> Dia de **parcial = solo evaluacion**. No hay tema nuevo ni avance del PI en clase.
> Enunciado y solucion: `Parciales/{archivo}`

- **Curso:** Programacion II (FI303204) · 120 min · **virtual sincrono por Meet**

## Checklist 120 min

| Min | Accion |
|---|---|
| 0-10 | Ingreso, asistencia, normas (sin material no autorizado). |
| 10-15 | Entregar enunciado. Aclarar tiempo y canal de dudas de forma. |
| 15-100 | Desarrollo del parcial (silencio de trabajo). |
| 100-110 | Aviso de 10 min; revision de integridad. |
| 110-120 | Recoleccion y cierre. |

## Notas
- No mezclar «tema + parcial» el mismo dia.
- La solucion es privada: archivo `* - SOLUCION.docx` en `Parciales/`.
- El PI VetCare continua en la siguiente clase regular.
"""
        path = kit / f"Guia aplicacion {titulo} - Clase {n}.md"
        path.write_text(md, encoding="utf-8")
        return path

    # El contenido esta proyectado (una lamina por concepto). El guion aporta lo que no
    # cabe en pantalla: que subrayar en cada una.
    teoria = _apoyo_por_diapositiva(c)
    # `fundamento` es desarrollo adicional SOLO para el guion (no entra a la slide,
    # que resume `teoria` via _resumen). Se usa donde la teoria por si sola no
    # alcanza para dictar la clase sin consultar otra fuente.
    pasos = "\n".join(f"{i}. {t}" for i, t in enumerate(c["taller"], 1))
    md = f"""# Guion docente · Clase {n} · {c['titulo']}

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** {c['hito_pi']}
- **Entregable de hoy:** {c['entregable']}
- **Herramienta:** {c['herramienta']}
- **Slides:** `Clases/Clase {n} - {c['slug']}/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

{teoria}

**Demo que usted debe poder repetir:** {c['demo']}

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: {c['hito_pi']}. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de concepto y en las de codigo
(lo que hay que subrayar esta tambien en las notas del presentador de cada lamina). Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: {c['demo']}
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase {n}/Codigo/{c.get('codigo_archivo', '(sin archivo)')}`

### 60-105 · Taller guiado (opcional) = avance del PI
Opcional: no tiene lamina en el deck. La guia esta en
`Clases/Clase {n} - {c['slug']}/Taller PI - Clase {n} - VetCare.docx`; si hoy no se hace, se extiende la demo y la practica libre.
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
{pasos}
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: {c['entregable']}

### 105-120 · Criterios de exito y cierre
Si hubo taller, repasar los criterios de exito del `Taller PI - Clase {n} - VetCare.docx` (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase {n}/Quiz Clase {n} - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: {c['hito_pi']}. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase {n}/Solucion Taller Clase {n} - VetCare.docx` — no proyectar completa.
"""
    path = kit / f"Guion Docente Clase {n} - {c['slug']}.md"
    path.write_text(md, encoding="utf-8")
    return path


def convert_guion(md_path: Path):
    conv = SLIDES / "guion_md_a_docx.py"
    if conv.exists():
        subprocess.run([sys.executable, str(conv), str(md_path)], check=False)


def build_readme():
    KIT_DIR.mkdir(parents=True, exist_ok=True)
    (KIT_DIR / "README.md").write_text("""# Kit docente — Programacion II (2026-2)

Material **privado** del docente. Los estudiantes solo ven `Clases/`.

## Enfoque
Todo el curso avanza el **Proyecto Integrador VetCare** (aplicacion Java para la
Clinica Veterinaria «Huellitas»). Cada clase deja una pieza del mismo producto.

## Por clase
- `Guion Docente Clase N - ….md` + `.docx` (fundamento teorico + minuto a minuto)
- `Quiz Clase N - VetCare.docx` (sin claves) + `Quiz Clase N - CLAVE DOCENTE.docx`
- `Solucion Taller Clase N - VetCare.md|.docx` (privada)
- `Codigo/` demos Java · `Capturas/` evidencias
- Dias 5 / 10 / 15: `Guia aplicacion Parcial N` (solo evaluacion)

## Regenerar
```bash
python config/slides/build_uniajc_prog2_all.py
```

## Proyecto Integrador
- Estudiante: `Clases/Proyecto Integrador/`
- Docente: `Kit docente/Proyecto Integrador/`
""", encoding="utf-8")



def build_examlab_guia(c):
    """Guia para armar el taller de esta clase dentro de ExamLab.

    Va en el Kit docente porque la plataforma no importa preguntas desde archivo:
    el docente las crea en la UI y necesita el texto exacto de cada campo.
    """
    taller = TALLERES_EXAMLAB.get(c["n"])
    if not taller:
        return None
    d = KIT_DIR / f"Clase {c['n']}"
    d.mkdir(parents=True, exist_ok=True)
    md = examlab_talleres.guia_docente_md(
        c["n"], taller, "Programacion II (FI303204)",
        hito=c.get("hito_pi"), entregable=c.get("entregable"),
    )
    out = d / f"Taller en ExamLab - Clase {c['n']} (configuracion).md"
    out.write_text(md, encoding="utf-8")
    print("EXAMLAB", out)
    return out


def main():
    KIT_DIR.mkdir(parents=True, exist_ok=True)
    CLASES_DIR.mkdir(parents=True, exist_ok=True)
    build_readme()
    for c in CLASES:
        print(f"=== Clase {c['n']} ===")
        build_pptx(c)
        build_taller_docx(c)
        build_solucion_docx(c)
        build_quiz(c)
        build_codigo(c)
        build_examlab_guia(c)
        md = build_guion_md(c)
        if md:
            convert_guion(md)
    print("DONE Programacion II")


if __name__ == "__main__":
    main()
