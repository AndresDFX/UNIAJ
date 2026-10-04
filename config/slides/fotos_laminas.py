# -*- coding: utf-8 -*-
"""La foto de una lamina de viñetas, por su titulo (visual minimo de los decks de clase).

Orden de busqueda:
1. `FOTOS` de `fotos_laminas_data.py`: titulo (normalizado, por comienzo) -> consulta en ingles
   escrita a mano. Es la que se cura: una foto que no dice nada del tema es peor que ninguna.
2. Si no hay entrada, una consulta automatica con las palabras de contenido del titulo, en
   espanol (`locale=es-ES`), y el titulo queda anotado en `assets/pexels/_sin_curar.txt`
   para escribirle su consulta.

Devuelve `(ruta, pie)` o `(None, None)` si no hay foto (sin red ni cache): la lamina se queda
en texto y el build no se cae.
"""
import re
import unicodedata
from pathlib import Path

import pexels

try:
    from fotos_laminas_data import FOTOS
except ImportError:  # el dato aun no existe
    FOTOS = {}

SIN_CURAR = Path(__file__).resolve().parent / "assets" / "pexels" / "_sin_curar.txt"
_VACIAS = set("""el la los las un una unos unas de del al y o u a en con sin por para que se su sus
lo es son como cuando donde cual cuales hoy no si mas muy sobre entre desde hasta cada todo
toda todos este esta esto ese esa eso clase dia tema parte uno dos tres cuatro cinco seis""".split())


def _norm(s):
    s = re.sub(r"\{\{[^}]*\}\}", "", str(s))
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn").strip()


def consulta_de(titulo):
    t = _norm(titulo)
    for clave, q in FOTOS.items():
        if t.startswith(_norm(clave)):
            return q, None
    palabras = [w for w in re.findall(r"[a-z0-9_]+", t) if w not in _VACIAS and len(w) > 2]
    return " ".join(palabras[:4]) or "computer", "es-ES"


def para(titulo):
    q, locale = consulta_de(titulo)
    if locale:
        try:
            SIN_CURAR.parent.mkdir(parents=True, exist_ok=True)
            ya = SIN_CURAR.read_text(encoding="utf-8").splitlines() if SIN_CURAR.exists() else []
            if titulo not in ya:
                with SIN_CURAR.open("a", encoding="utf-8") as fh:
                    fh.write(str(titulo) + "\n")
        except OSError:
            pass
    f = pexels.foto(q, locale=locale)
    if not f:
        return None, None
    return f, pexels.credito(f)
