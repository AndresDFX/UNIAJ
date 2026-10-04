# -*- coding: utf-8 -*-
"""Que visual acompana a cada concepto: los pasos de una animacion, una foto, o nada.

Cada curso declara `<curso>_visuales_data.VISUALES = {n: {comienzo_de_titulo: spec}}` con
`spec = {"anim": "<carpeta>/<huella>"}` (renderizada por `config/animaciones/renderizar.py`)
y/o `{"foto": "<consulta Pexels en ingles>"}`. La animacion manda sobre la foto: explica mas.

`imagenes(VISUALES, n, titulo)` devuelve `(rutas, pie)`. Con una animacion, `rutas` son sus
pasos en orden (`-paso1.png`, `-paso2.png`…): `concepto_slide` pone el primero al entrar y
cada siguiente aparece con un clic del docente. Sin entrada, `([], None)`: el concepto se
queda en texto, y eso es una decision, no un hueco.
"""
import re
import unicodedata
from pathlib import Path

import pexels

RENDER = Path(__file__).resolve().parent.parent / "animaciones" / "render"
_TOKEN = re.compile(r"\{\{\s*slide:[^}]*\}\}")


def _norm(s):
    s = _TOKEN.sub("", str(s))
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn").strip()


def spec_de(visuales, n, titulo):
    t = _norm(titulo)
    for clave, v in (visuales.get(n) or {}).items():
        if t.startswith(_norm(clave)):
            return v
    return None


def pasos_de(anim):
    base = RENDER / anim
    pasos = sorted(base.parent.glob(base.name + "-paso*.png"),
                   key=lambda p: int(re.search(r"paso(\d+)", p.name).group(1)))
    if pasos:
        return pasos
    fin = base.parent / (base.name + "-fin.png")
    return [fin] if fin.exists() else []


def imagenes(visuales, n, titulo):
    v = spec_de(visuales, n, titulo)
    if not v:
        return [], None
    if v.get("anim"):
        p = pasos_de(v["anim"])
        if p:
            return p, ("Clic para avanzar la animación" if len(p) > 1 else None)
    if v.get("foto"):
        f = pexels.foto(v["foto"])
        if f:
            return [f], pexels.credito(f)
    return [], None
