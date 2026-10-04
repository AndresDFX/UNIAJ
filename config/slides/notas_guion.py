# -*- coding: utf-8 -*-
"""Notas del presentador como GUION DE LA LAMINA: todo lo necesario para darla sin buscar fuera.

El docente lo pidio asi (2026-10): «en las notas, todo lo necesario para poder dar esa
diapositiva en especial; estoy usando demasiado Gemini para poder explicar el tema». Las notas
que habia eran el fundamento volcado frase por frase: largo, sin orden y escrito para leer, no
para decir. Aqui cada lamina recibe un guion con la misma forma siempre:

    QUÉ ES (dilo así)       2-4 frases, tal como se le dicen al estudiante.
    CÓMO DARLA (≈N min)     al entrar, y qué decir en cada CLIC de la animación.
    EJEMPLO                 el caso concreto que lo aterriza.
    SI PREGUNTAN            las preguntas que salen siempre, con su respuesta.
    CUIDADO                 el error típico (del estudiante o del docente).
    PASA A LA SIGUIENTE     la frase puente.

El contenido vive en `<curso>_contenido_data.py`:
`CONTENIDO[n][comienzo_del_titulo_visible] = {"ideas": [...], "notas": {...}}`. `ideas` (opcional)
reemplaza las viñetas proyectadas por frases claras escritas a mano; `notas` es el guion.
`aplicar(prs, contenido_de_la_clase)` se llama justo antes de guardar: busca cada lamina por su
titulo VISIBLE y REEMPLAZA sus notas por el guion (el fundamento completo queda en el Kit).
"""
import re
import unicodedata

ORDEN = (("explica", "QUÉ ES (dilo así)"), ("pasos", "CÓMO DARLA"), ("ejemplo", "EJEMPLO"),
         ("preguntas", "SI PREGUNTAN"), ("cuidado", "CUIDADO"), ("puente", "PASA A LA SIGUIENTE"))


def _norm(s):
    s = re.sub(r"\{\{[^}]*\}\}|\*\*|@@", "", str(s))
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).strip()


def entrada(contenido, titulo):
    """La entrada cuyo titulo-clave es comienzo de `titulo` (la mas larga gana)."""
    t = _norm(titulo)
    mejor = None
    for k, v in (contenido or {}).items():
        nk = _norm(k)
        if t.startswith(nk) and (mejor is None or len(nk) > len(_norm(mejor[0]))):
            mejor = (k, v)
    return mejor[1] if mejor else None


def ideas(contenido, titulo):
    e = entrada(contenido, titulo)
    return list(e["ideas"]) if e and e.get("ideas") else None


def texto(notas):
    """El guion formateado para el panel de notas de PowerPoint."""
    out = []
    for clave, rotulo in ORDEN:
        v = notas.get(clave)
        if not v:
            continue
        if clave == "pasos":
            mins = notas.get("min")
            out.append(rotulo + (" (≈%s min)" % mins if mins else "") + ":")
            for i, p in enumerate(v):
                etiqueta = "Al entrar" if i == 0 else "Clic %d" % i
                if isinstance(p, (list, tuple)):
                    etiqueta, p = p
                out.append("  • %s: %s" % (etiqueta, p))
        elif clave == "preguntas":
            out.append(rotulo + ":")
            for q, a in v:
                out.append("  • «%s» → %s" % (q, a))
        else:
            out.append("%s: %s" % (rotulo, v))
        out.append("")
    return "\n".join(out).strip()


def _titulo_de(slide):
    """El titulo visible: el primer cuadro de texto de la banda superior (top < 1.1 in)."""
    mejor = None
    for sh in slide.shapes:
        if not sh.has_text_frame or not sh.text_frame.text.strip():
            continue
        if sh.top is not None and sh.top < 914400 * 1.1:
            if mejor is None or sh.top < mejor.top:
                mejor = sh
    if mejor is not None:
        return mejor.text_frame.text.strip()
    for sh in slide.shapes:
        if sh.has_text_frame and sh.text_frame.text.strip():
            return sh.text_frame.text.strip()
    return ""


def aplicar(prs, contenido):
    """Reemplaza las notas de cada lamina que tenga guion. Devuelve cuantas recibieron guion."""
    n = 0
    for slide in prs.slides:
        e = entrada(contenido, _titulo_de(slide))
        if not e or not e.get("notas"):
            continue
        slide.notes_slide.notes_text_frame.text = texto(e["notas"])
        n += 1
    return n
