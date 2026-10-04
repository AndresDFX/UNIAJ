# -*- coding: utf-8 -*-
"""Genera TODO el material de Seminario de Sistemas 2026-2 (PI VetCare, diseño).

Por que existe
--------------
El material del curso venia del periodo anterior y no era regenerable: cualquier cambio
de convencion habia que aplicarlo a mano en 14 carpetas, y los guiones traian la agenda
de un bloque que ya no existe. Este build lo deja alineado al plan 2026-2 y regenerable
desde una sola fuente, igual que Prog II, BD II y Arquitectura.

Diferencia clave con Programacion II: esta asignatura es de **analisis y diseño**, no de
programacion. El estudiante no entrega codigo: entrega requisitos, diagramas UML,
wireframes y documentos. Por eso donde Prog II genera `Codigo/*.java`, aqui se genera
`Plantillas/*.md` con el artefacto de diseño de la clase.

Salidas
-------
  Clases/Clase N - <slug>/Presentacion.pptx      (estudiante)
  Clases/Clase N - <slug>/Taller PI - Clase N - VetCare.docx
  Kit docente/Clase N/Guion Docente ….md|.docx   (regla de oro: teoria desarrollada)
  Kit docente/Clase N/Quiz ….docx + Quiz … CLAVE DOCENTE.docx
  Kit docente/Clase N/Solucion Taller ….md|.docx
  Kit docente/Clase N/Plantillas/<artefacto>.md
  Kit docente/Clase N/Guia aplicacion Parcial N ….md|.docx   (dias 5/10/15)

Los datos pedagogicos viven en `seminario_clases_data.py` (una sola fuente).
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
    new_prs,
    notas,
    pseudo_code_slide,
    steps_visual_slide,
)
from uniajc_quiz_helpers import clave_text, q_abierta, q_om, q_vf  # noqa: E402
from docx import Document  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.oxml import OxmlElement  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.shared import Pt as DocPt, RGBColor  # noqa: E402

from seminario_clases_data import CLASES  # noqa: E402
from seminario_examlab_data import EXAMLAB as TALLERES_EXAMLAB  # noqa: E402
import examlab_talleres  # noqa: E402

CURSO = ROOT / "Seminario de Sistemas"
CLASES_DIR = CURSO / "Clases"
KIT_DIR = CURSO / "Kit docente"

AZUL = RGBColor(0x09, 0x52, 0x92)
CIAN_D = RGBColor(0x26, 0x9C, 0xCB)
GRIS = RGBColor(0x2B, 0x2B, 0x2B)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
ROJO = RGBColor(0xA0, 0x20, 0x30)
FONT = "Calibri"
EXAMLAB = "ExamLab (https://uniaj.examlab.workers.dev/)"

# Logo + para que sirve, por herramienta. El campo `herramienta` de cada clase es
# texto libre separado por "·", asi que se mapea por subcadena. Figma y Penpot van
# sin logo a proposito: no hay asset de marca y no se inventa uno.
HERRAMIENTAS = [
    ("draw.io", "drawio.png", "Diagramas UML y de contexto"),
    ("excalidraw", "excalidraw.png", "Bocetos rapidos a mano alzada"),
    ("google docs", "google_docs.png", "Documentos del paquete de diseño"),
    ("mermaid", "mermaid.png", "Diagramas como texto versionable"),
    ("figma", None, "Wireframes y prototipo navegable"),
    ("penpot", None, "Alternativa libre a Figma"),
]


def _herramientas_del_dia(texto):
    """Convierte 'draw.io · Mermaid Live Editor' en items para herramientas_slide."""
    t = (texto or "").lower()
    items = [{"name": n.title() if n.islower() and " " not in n else n,
              "logo": logo, "note": nota}
             for n, logo, nota in HERRAMIENTAS if n in t]
    # ExamLab siempre aparece: es el canal de entrega de todos los talleres
    items.append({"name": "ExamLab", "logo": "examlab.png",
                  "note": "Entrega del taller · domingo 23:59"})
    return items


PARCIALES = {
    5: ("Parcial 1", "Parcial 1 - Ciclos de vida y metodologias.docx"),
    10: ("Parcial 2", "Parcial 2 - Requerimientos UML y casos de uso.docx"),
    15: ("Parcial 3", "Parcial 3 - UML avanzado interfaces y proyecto.docx"),
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
import codigo_a_slides as CS
from seminario_operativo_data import OPERATIVO
import visuales
from seminario_visuales_data import CODIGO_TRAS, LAMINAS, VISUALES

# ------------------------------------------------------------- texto proyectado
# Los decks de clase no nombran el proyecto (VetCare, Huellitas, Proyecto Integrador) ni la
# actividad evaluada (entregable, rubrica, que se califica). El ejemplo se queda; cambia el
# nombre por la descripcion del dominio. Se aplica SOLO a lo proyectado: guion, taller,
# solucion, quiz y ExamLab leen los mismos datos y siguen nombrando el proyecto.
_DECK_SUBS = [
    (r"Ejemplo de toda la clase: VetCare, el sistema de la clinica «Huellitas»\.",
     "Ejemplo de toda la clase: el sistema de una clinica veterinaria."),
    (r"Mismo dominio VetCare — no otro ejemplo\.",
     "Mismo dominio: la clinica veterinaria — no otro ejemplo."),
    (r"subgraph vetcare\[VetCare - el sistema\]",
     "subgraph sistema_clinica[El sistema de la clinica]"),
    (r"\bvetcare\b", "sistema_clinica"),
    (r"subgraph sistema\[VetCare\]", "subgraph sistema[Sistema de la clinica]"),
    (r"@@Por que importa al PI:@@ ?", "@@Por que importa:@@ "),
    (r" Esto es la P2 del hito y vale puntos\.", ""),
    (r"title Sustentacion VetCare", "title Sustentacion"),
    (r"Guion de sustentacion VetCare", "Guion de sustentacion"),
    (r"ERS VetCare", "ERS Clinica"),
    (r"del proyecto VetCare", "del proyecto"),
    (r"paquete VetCare", "paquete"),
    (r"con VetCare en la mano", "con el caso de la clinica en la mano"),
    (r"y VetCare va a", "y el sistema va a"),
    (r"construir VetCare", "construir el sistema"),
    (r"los planos y el prototipo de VetCare", "los planos y el prototipo del sistema"),
    (r"cada concepto de VetCare", "cada concepto del dominio"),
    (r"Un caso de VetCare", "Un caso tipico"),
    (r"secundario de VetCare", "secundario del sistema"),
    (r"Trasladado a VetCare: si Huellitas", "Trasladado a la clinica: si la clinica"),
    (r"en un proyecto como VetCare", "en un proyecto como el de la clinica"),
    (r"\bEn VetCare\b", "En la clinica"),
    (r"\ben VetCare\b", "en la clinica"),
    (r"\bPara VetCare\b", "Para la clinica"),
    (r"\bpara VetCare\b", "para la clinica"),
    (r"\bde VetCare\b", "de la clinica"),
    (r"\bsobre VetCare\b", "sobre la clinica"),
    (r"\bVetCare\b", "el sistema"),
    # frases que le hablaban al docente: se reescriben como concepto
    (r"^Conviene separar dos palabras que se usan como sinonimos y no lo son",
     "Proyecto y producto son dos palabras que se usan como sinonimos y no lo son"),
    (r"Queda una pregunta que el estudiante hace el primer dia y conviene responder sin rodeos: "
     r"para que sirve documentar si al final lo que se usa es el codigo\.",
     "Para que sirve documentar si al final lo que se usa es el codigo: depende de quien lee."),
    (r"(?i)\bel docente que califica,", "quien revisa el diseño,"),
    (r"Conviene tambien aclarar el mapa del semestre en una sola frase, porque de eso depende "
     r"que el estudiante sepa donde esta parado en cada clase\.",
     "El mapa del semestre cabe en una sola frase, y de el depende saber donde se esta parado en cada clase."),
    (r" y que conviene instalar el primer dia sin jerga: la deuda tecnica", ": la deuda tecnica"),
    (r"Aqui es donde los tres casos de matricula se hacen visibles y conviene decirlo en voz alta en el aula:",
     "Aqui se hacen visibles los tres casos de matricula:"),
    (r"^Demo: El docente (\w+)", lambda m: "Demo: se " + m.group(1)),
    (r"^El docente (\w+)", lambda m: "Se " + m.group(1)),
    (r"\bClinica Huellitas\b", "Clinica veterinaria"),
    (r"\bclinica Huellitas\b", "clinica"),
    (r"\b(de|a|para|en) Huellitas\b", r"\1 la clinica"),
    (r"\| Huellitas:", "| La clinica:"),
    (r"\bHuellitas\b", "la clinica"),
    (r"En nuestro Proyecto Integrador", "En un proyecto de software"),
    (r"Para nuestro Proyecto Integrador", "Para este curso"),
    (r"En el Proyecto Integrador", "En un proyecto real"),
    (r"del Proyecto Integrador", "del proyecto"),
    (r"(?i)proyecto integrador", "proyecto de diseño"),
    (r"\bPI\[", "PIN["), (r"> PI\b", "> PIN"), (r"\bPI -", "PIN -"),
    (r"\bel PI\b", "el proyecto"), (r"\bal PI\b", "al proyecto"), (r"\bdel PI\b", "del proyecto"),
    (r"que es el entregable real de la asignatura", "que es el producto real de la asignatura"),
    (r"historia entregable", "historia verificable"),
    (r"cada una entregable y", "cada una terminable y"),
    (r"(su|el) entregable (final|ES|profesional)", r"\1 producto \2"),
    (r"\bentregables\b", "artefactos"), (r"\bEntregables\b", "Artefactos"),
    (r"\bentregable\b", "artefacto"), (r"\bEntregable\b", "Artefacto"),
    (r"\brubrica\b", "lista de verificacion"),
    (r"Lo que se califica", "Lo que importa"),
    (r"lo que se califica", "lo que importa"),
    (r"\bse califica\b", "se revisa"),
]
_DECK_RX = [(re.compile(a, re.M), b) for a, b in _DECK_SUBS]


def _deck(t):
    """Texto proyectado sin nombre de proyecto ni actividad evaluada (ver _DECK_SUBS)."""
    if not isinstance(t, str):
        return t
    for rx, b in _DECK_RX:
        t = rx.sub(b, t)
    return t


def _parrafos_fundamento(c):
    fund = (c.get("fundamento") or "").strip()
    return [p.strip() for p in fund.split("\n\n") if len(p.strip()) > 120] if fund else []


def _es_para_docente(p):
    """Parrafo que le habla al docente (organizacion, matricula, como encuadrar): no se
    proyecta, va a las notas del presentador. La lamina es para el estudiante."""
    t = p.lower()
    return "el docente debe" in t or "trampa pedagogica" in t


def notas_docente(c):
    return [p for p in _parrafos_fundamento(c) if _es_para_docente(p)]


def _laminas(c):
    """Las laminas de teoria de la clase, en orden: un concepto por parrafo y, detras de cada
    uno, el codigo (Mermaid o plantilla) que lo ilustra.

    Cada elemento es `(titulo, items, notas, tipo, extra)`: en `content`, `extra` es el titulo
    original del parrafo (la clave de `seminario_visuales_data`); en `codigo`, la leyenda.

    Antes el codigo iba todo al final del bloque de teoria y la lamina `codigo_slide_lineas`
    detras de todo: el estudiante veia el modelo en V explicado en la lamina 5 y su Mermaid en
    la 10. `TS.intercalar` lo pone detras del concepto con el que comparte vocabulario.
    """
    vin = [_deck(x) for x in c.get("teoria", [])]
    # `fundamento` era desarrollo adicional que SOLO veia el docente. Se proyecta tambien: si
    # vale la pena decirlo, vale la pena que el estudiante lo tenga.
    vin += [_deck(p) for p in _parrafos_fundamento(c) if not _es_para_docente(p)]
    conceptos = []
    for t, it, nt, tp in TS.slides_de_vinetas(vin):
        if tp == "content":
            # Modo concepto: UNA lamina por parrafo, con un titulo que dice lo que es y sus
            # ideas completas (seminario_visuales_data.LAMINAS); el parrafo entero va a notas.
            spec = visuales.spec_de(LAMINAS, c["n"], t) or {}
            conceptos.append((_deck(spec.get("titulo", t)),
                              [_deck(x) for x in spec.get("ideas", it)], nt, tp, t))
        else:
            conceptos.append((t, it, nt, tp, None))
    codigos = [(_deck(t), [_deck(x) for x in it], nt, tp, None) for t, it, nt, tp in
               CS.slides_de_fuente(c.get("codigo_fuente") or "", c.get("codigo_archivo") or "")]
    # El material operativo autorado. En Seminario los artefactos son diagramas Mermaid y
    # plantillas, y la sintaxis de Mermaid decide si un diagrama renderiza o no.
    codigos += [(_deck(tit), [_deck(x) for x in lineas], [], "codigo", None)
                for tit, lineas in OPERATIVO.get(c["n"], [])]
    if c.get("codigo_slide_lineas"):
        codigos.append((_deck(c.get("codigo_slide_titulo", "Codigo de hoy")),
                        [_deck(x) for x in c["codigo_slide_lineas"]], [], "codigo",
                        _deck(c.get("codigo_slide_caption"))))
    # Los que tienen sitio declarado van detras de su concepto; el resto, por vocabulario.
    tras = CODIGO_TRAS.get(c["n"], {})
    fijos = {}
    libres = []
    for cod in codigos:
        clave = next((k for cod_t, k in tras.items()
                      if visuales._norm(cod[0]).startswith(visuales._norm(cod_t))), None)
        if clave:
            fijos.setdefault(visuales._norm(clave), []).append(cod)
        else:
            libres.append(cod)
    out = []
    for lam in TS.intercalar(conceptos, libres):
        out.append(lam)
        if lam[3] == "content":
            for k in list(fijos):
                if visuales._norm(lam[4]).startswith(k):
                    out += fijos.pop(k)
    if fijos:
        raise SystemExit("CODIGO_TRAS apunta a conceptos que no existen: %s" % list(fijos))
    return out


def _teoria_slides(c):
    """`(titulo, items, notas, tipo)` de cada lamina de teoria: lo que leen deck y guion."""
    return [x[:4] for x in _laminas(c)]


_MERMAID = ("flowchart", "graph", "classdiagram", "sequencediagram", "gantt", "statediagram",
            "erdiagram", "journey", "mindmap")


def _lenguaje_de(lineas):
    """Lo que dice la barra del editor. En Seminario no hay SQL ni YAML: hay Mermaid, tablas
    Markdown y plantillas de texto, y el detector generico del motor llamaba «YAML» a una
    ficha de requisito («Actor: Recepcionista») y no reconocia `gantt` como Mermaid."""
    primera = next((x.strip() for x in lineas if x.strip()), "")
    if primera.lower().split(" ")[0] in _MERMAID:
        return "Mermaid"
    if primera.startswith("|"):
        return "Tabla Markdown"
    return "Plantilla"


#: Laminas antes de la teoria: portada, encuadre y mapa del bloque.
_ANTES_DE_TEORIA = 3


def _apoyo_por_diapositiva(c, base=None):
    """Apoyo puntual por diapositiva: que subrayar en cada una, sin repetir su contenido."""
    slides = _teoria_slides(c)
    if not slides:
        return ""
    L = ["## Apoyo por diapositiva", "",
         "Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en "
         "cada lamina, no repite su contenido.", ""]
    for j, (titulo, vin, notas, _tipo) in enumerate(slides):
        num = f"[Slide {base + j}] " if base else ""
        L.append(f"**{num}{titulo}** — {len(vin)} vinetas.")
        for x in notas:
            L.append(f"  - {x}")
        L.append("")
    return "\n".join(L)


def build_pptx(c):
    n = c["n"]
    if n in PARCIALES:
        prs = new_prs()
        class_cover(prs, PARCIALES[n][0], subtitulo="Solo evaluacion", clase_n=n, idx=1)
        content_slide(prs, "Indicaciones", [
            "Hoy es el **parcial**: no hay tema nuevo en esta sesion.",
            "Entra lo visto en el corte hasta hoy.",
            "Modalidad **virtual sincrona por Meet**.",
            "Duracion aproximada: **90–100 min** dentro del bloque de 120.",
            "El enunciado y el canal de entrega se comparten al empezar.",
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
    class_cover(prs, _deck(c["titulo"]), subtitulo=_deck(c["subtitulo"]), clase_n=n, idx=1)
    idx = 2
    # El deck solo lleva el tema. La practica es opcional (a veces se hace, a veces no) y
    # su guia vive en la carpeta: `Taller PI - Clase N - VetCare.docx`. Por eso aqui no
    # hay laminas de taller, entregable, autochequeo ni herramientas de la actividad.
    content_slide(prs, "Encuadre de hoy", [
        f"**Tema:** {_deck(c['titulo'])}",
        f"{_deck(c['subtitulo'])}",
        f"Herramienta del tema: **{c['herramienta']}** · Bloque **120 min**",
        "Ejemplo de toda la clase: el sistema de una clinica veterinaria.",
    ], idx=idx); idx += 1
    block_timeline_slide(prs, "Mapa del bloque de hoy (120 min)", [
        ("0-10", "Encuadre y repaso"),
        ("10-40", "Teoria Core del tema de hoy"),
        ("40-60", "Demo en vivo sobre la clinica"),
        ("60-105", "Practica (opcional, guia en la carpeta)"),
        ("105-120", "Sintesis y cierre"),
    ], idx=idx); idx += 1
    for _k, (_t, _items, _notas, _tipo, _extra) in enumerate(_laminas(c)):
        if _tipo == "codigo":
            _s = pseudo_code_slide(prs, _t, _items, caption=_extra, idx=idx,
                                   lenguaje=_lenguaje_de(_items))
        else:
            # Una lamina por concepto con su visual: los pasos de su animacion (uno por clic
            # del docente) o una foto. Sin visual, las ideas a lo ancho.
            _imgs, _pie = visuales.imagenes(VISUALES, n, _extra or _t)
            _s = concepto_slide(prs, _t, _items, imagenes=_imgs, pie=_pie, idx=idx)
        if _notas and _s is not None:
            notas(_s, list(_notas))
        # Lo que el fundamento le dice al docente (organizacion del curso), debajo de la
        # primera lamina de teoria: se lee al presentar, no se proyecta.
        if _k == 0 and _s is not None and notas_docente(c):
            notas(_s, ["PARA EL DOCENTE"] + notas_docente(c))
        idx += 1
    content_slide(prs, "Demo del dia", [
        f"**Herramienta:** {_deck(c['herramienta'])}",
        f"**Demo:** {_deck(c['demo'])}",
        "Mismo dominio: la clinica veterinaria — no otro ejemplo. Aqui se diseña, no se programa.",
    ], idx=idx); idx += 1
    closing_slide(prs, f"Clase {n} · {_deck(c['titulo'])}", [
        _deck(c["subtitulo"]),
        "Repasen las laminas de teoria: cada concepto esta completo",
        "Siguiente clase: continuamos con el siguiente tema",
    ], accent="Teoria al servicio del diseño")
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
    banda(doc, f"Taller PI · Clase {n} · Seminario de Sistemas")
    para(doc, c["titulo"], size=14, bold=True, color=AZUL)
    para(doc, "Hilo conductor: Proyecto Integrador VetCare — diseño, no programacion.",
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
    if c.get("artefacto_archivo"):
        lines += ["", f"Plantilla de apoyo: `Kit docente/Clase {n}/Plantillas/{c['artefacto_archivo']}`"]
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
    """En esta asignatura el artefacto no es codigo: es una plantilla de diseño
    (requisitos, historia de usuario, especificacion de caso de uso, diccionario
    de datos) que el docente reparte y el estudiante llena."""
    n = c["n"]
    if n in PARCIALES or not c.get("artefacto_contenido"):
        return
    dest = KIT_DIR / f"Clase {n}" / "Plantillas"
    dest.mkdir(parents=True, exist_ok=True)
    nombre = c.get("artefacto_archivo") or f"Plantilla Clase {n}.md"
    (dest / nombre).write_text(c["artefacto_contenido"], encoding="utf-8")


# ---------------------------------------------------------------------- capturas
def _escribir_readme_capturas(c, cap):
    """README de Capturas/ con que imagen va aqui, como tomarla y con que nombre.

    La carpeta se creaba vacia en las 15 clases, y una carpeta vacia no existe en
    git: al clonar el repo desaparecia, asi que el docente no tenia donde leer que
    captura se espera. Es el mismo README que ya escriben Arquitectura y BD II, y
    se reescribe en cada build para que refleje la herramienta y la demo actuales.
    """
    n = c["n"]
    titulo = f"Capturas de la Clase {n} — Seminario de Sistemas"
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
              f"   - Repetir la demo del bloque de teoria: {c['demo']}",
              "   - Capturar solo la ventana util, no el escritorio completo.",
              "   - Recortar a ~1200 px de ancho y guardar aqui con ese nombre.", "",
              f"2) artefacto-clase{n:02d}.png — el artefacto de un estudiante a medio armar",
              "   - Con permiso del estudiante, capturar su diagrama o plantilla de hoy.",
              "   - Recortar nombre y correo antes de guardar.", ""]
    L += ["Despues de agregar una imagen, regenerar el kit:",
          "   python config/slides/build_uniajc_seminario_all.py", ""]
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

- **Curso:** Seminario de Sistemas (FI303301) · 120 min · **virtual sincrono por Meet**

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
    teoria = _apoyo_por_diapositiva(c, base=_ANTES_DE_TEORIA + 1)
    # `fundamento` es desarrollo adicional SOLO para el guion (no entra a la slide,
    # que resume `teoria` via _resumen). Se usa donde la teoria por si sola no
    # alcanza para dictar la clase sin consultar otra fuente.
    pasos = "\n".join(f"{i}. {t}" for i, t in enumerate(c["taller"], 1))
    md = f"""# Guion docente · Clase {n} · {c['titulo']}

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Avance del PI (si se hace la practica):** {c['hito_pi']}
- **Practica (opcional):** `Clases/Clase {n} - {c['slug']}/Taller PI - Clase {n} - VetCare.docx` — no esta en el deck
- **Herramienta:** {c['herramienta']}
- **Slides:** `Clases/Clase {n} - {c['slug']}/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

{teoria}

**Demo que usted debe poder repetir:** {c['demo']}

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy el tema es: {c['titulo']}. Todo lo que vamos a ver esta en las laminas.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de teoria (una por concepto)
y en las de codigo proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: {c['demo']}
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase {n}/Plantillas/{c.get('artefacto_archivo', '(sin plantilla)')}`

### 60-105 · Practica guiada (OPCIONAL) = avance del PI
No hay laminas para esta franja: la guia es el archivo
`Clases/Clase {n} - {c['slug']}/Taller PI - Clase {n} - VetCare.docx` (compartirlo, no proyectarlo).
Si hoy no se hace, usar el tiempo para profundizar la teoria y la demo.
**Decir (si se hace):** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
{pasos}
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: {c['entregable']}

### 105-120 · Sintesis y cierre
Si hubo practica, repasar los criterios de exito del archivo del taller (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase {n}/Quiz Clase {n} - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir (si hubo practica):** «Queda avanzado: {c['hito_pi']}. Entrega en ExamLab, domingo 23:59.»

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
    (KIT_DIR / "README.md").write_text("""# Kit docente — Seminario de Sistemas (2026-2)

Material **privado** del docente. Los estudiantes solo ven `Clases/`.

## Enfoque
Todo el curso avanza el **Proyecto Integrador VetCare**: aqui se producen los PLANOS del
sistema de la Clinica Veterinaria «Huellitas» (requisitos, UML, interfaz), no el codigo.
El mismo producto se programa en Programacion II.

## Por clase
- `Guion Docente Clase N - ….md` + `.docx` (fundamento teorico + minuto a minuto)
- `Quiz Clase N - VetCare.docx` (sin claves) + `Quiz Clase N - CLAVE DOCENTE.docx`
- `Solucion Taller Clase N - VetCare.md|.docx` (privada)
- `Plantillas/` artefactos de diseño · `Capturas/` evidencias
- Dias 5 / 10 / 15: `Guia aplicacion Parcial N` (solo evaluacion)

## Regenerar
```bash
python config/slides/build_uniajc_seminario_all.py
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
        c["n"], taller, "Seminario de Sistemas (FI303301)",
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
    print("DONE Seminario de Sistemas")


if __name__ == "__main__":
    main()
