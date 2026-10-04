# -*- coding: utf-8 -*-
"""Fotos de Pexels para las laminas, con cache local: el build no depende de la red.

La clave se lee de la variable de entorno PEXELS_API_KEY o de `_privado/pexels_api_key.txt`
(fuera del repositorio: `_privado/` esta en .gitignore). Nunca se escribe en el codigo.

Cada busqueda se guarda en `config/slides/assets/pexels/<slug>.jpg` con su ficha `<slug>.json`
(autor, url de la foto, consulta). Si la foto ya esta en la cache no se vuelve a pedir, asi que
regenerar un curso sin red ni clave sigue funcionando con las fotos ya bajadas.
"""
import json
import os
import re
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CACHE = Path(__file__).resolve().parent / "assets" / "pexels"


def _clave():
    k = os.environ.get("PEXELS_API_KEY")
    if k:
        return k.strip()
    f = RAIZ / "_privado" / "pexels_api_key.txt"
    return f.read_text(encoding="utf-8").strip() if f.exists() else None


def _slug(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:60]


def foto(consulta, orientacion="landscape", indice=0):
    """Ruta local de una foto para `consulta` (en ingles rinde mejor), o None si no hay."""
    CACHE.mkdir(parents=True, exist_ok=True)
    slug = _slug(consulta) + ("" if not indice else "-%d" % indice)
    jpg = CACHE / (slug + ".jpg")
    if jpg.exists():
        return jpg
    clave = _clave()
    if not clave:
        return None
    url = "https://api.pexels.com/v1/search?" + urllib.parse.urlencode(
        {"query": consulta, "per_page": indice + 1, "orientation": orientacion})
    req = urllib.request.Request(url, headers={"Authorization": clave, "User-Agent": "uniajc-slides"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            datos = json.load(r)
        fotos = datos.get("photos") or []
        if len(fotos) <= indice:
            return None
        p = fotos[indice]
        req = urllib.request.Request(p["src"]["large"], headers={"User-Agent": "uniajc-slides"})
        with urllib.request.urlopen(req, timeout=30) as r:
            jpg.write_bytes(r.read())
        (CACHE / (slug + ".json")).write_text(json.dumps({
            "consulta": consulta, "autor": p.get("photographer"), "url": p.get("url"),
            "licencia": "Pexels License (uso libre, atribución opcional)"},
            ensure_ascii=False, indent=1), encoding="utf-8")
        return jpg
    except Exception as e:  # sin red o sin cuota: la lamina sigue sin foto, no se cae el build
        print("pexels: sin foto para %r (%s)" % (consulta, e))
        return None


def credito(ruta):
    """'Foto: <autor> · Pexels' para el pie de la imagen."""
    f = Path(ruta).with_suffix(".json")
    if f.exists():
        d = json.loads(f.read_text(encoding="utf-8"))
        return "Foto: %s · Pexels" % d.get("autor", "")
    return "Foto: Pexels"


if __name__ == "__main__":
    import sys
    print(foto(" ".join(sys.argv[1:]) or "database server"))
