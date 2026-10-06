# -*- coding: utf-8 -*-
"""El diagrama que DIBUJA una lamina de codigo (Mermaid, sobre todo), por curso, clase y titulo.

Una lamina que proyecta solo el texto de un diagrama no se entiende: el estudiante tiene que
imaginar las cajas. `pseudo_code_slide` consulta aqui y, si hay dibujo, lo pone a la derecha
del codigo («Lo que dibuja este codigo»). El dibujo es una ilustracion del motor de
animaciones (`pasos: [1]`) que reproduce EXACTAMENTE las cajas y flechas del codigo.

Datos: `<curso>_diagramas_data.py` con
`DIAGRAMAS = {(curso, n): {"comienzo del titulo": "<curso>/claseN/<huella>"}}`.
"""
import glob
import importlib
import os
import re
import unicodedata

import visuales

DIAGRAMAS = {}
_aqui = os.path.dirname(os.path.abspath(__file__))
for _f in sorted(glob.glob(os.path.join(_aqui, "*_diagramas_data.py"))):
    _d = importlib.import_module(os.path.splitext(os.path.basename(_f))[0]).DIAGRAMAS
    for _k, _v in _d.items():
        DIAGRAMAS.setdefault(_k, {}).update(_v)


def _norm(s):
    s = unicodedata.normalize("NFD", str(s).lower())
    return re.sub(r"\s+", " ", "".join(c for c in s if unicodedata.category(c) != "Mn")).strip()


def para(prs, titulo):
    """Ruta del PNG del diagrama de esta lamina de codigo, o None."""
    import ilustraciones
    curso, n = ilustraciones.contexto(prs)
    t = _norm(titulo)
    for clave, huella in (DIAGRAMAS.get((curso, n)) or {}).items():
        if t.startswith(_norm(clave)):
            pasos = visuales.pasos_de(huella)
            return pasos[-1] if pasos else None
    return None
