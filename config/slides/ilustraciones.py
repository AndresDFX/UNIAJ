# -*- coding: utf-8 -*-
"""La ilustracion generada de una lamina de viñetas, por su titulo.

Sustituye a las fotos de Pexels (2026-10): una foto «por poner imagen» no explica nada. Cada
ilustracion es un modulo del motor de animaciones (`config/animaciones/<curso>/claseN/`) con
`pasos: [1]` —un solo fotograma, el estado completo— dibujado para ESE concepto: un esquema, un
flujo, una comparacion. Se declara en `ilustraciones_data.ILUSTRACIONES` por comienzo de titulo.

Sin ilustracion declarada, la lamina se queda en texto: es preferible a una imagen decorativa.
Los titulos que llegan sin ilustracion se anotan en `config/animaciones/_sin_ilustracion.txt`
para que se dibuje la suya.
"""
import re
import unicodedata
from pathlib import Path

import visuales

# Un archivo de datos por curso (`<curso>_ilustraciones_data.py`), para que el trabajo de un
# curso no pise el de otro; se juntan aqui.
ILUSTRACIONES = {}
for _m in ("bd2", "arq", "prog2", "seminario", "intro"):
    try:
        _d = __import__("%s_ilustraciones_data" % _m).ILUSTRACIONES
    except ImportError:
        continue
    for _k, _v in _d.items():
        ILUSTRACIONES.setdefault(_k, {}).update(_v)

PENDIENTES = Path(__file__).resolve().parent.parent / "animaciones" / "_sin_ilustracion.txt"


def _norm(s):
    s = re.sub(r"\{\{[^}]*\}\}", "", str(s))
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn").strip()


_CURSOS = (("build_uniajc_bd2", "bd2"), ("build_uniajc_arq", "arq"),
           ("build_uniajc_prog2", "prog2"), ("build_uniajc_seminario", "seminario"),
           ("build_uniajc_intro_ing", "intro"))


def contexto(prs):
    """`(curso, n)` del deck que se esta armando: el curso por el builder que llama, la clase
    por la portada («Clase N»). Los titulos se repiten entre clases («Demo del dia»), asi que
    la ilustracion se busca por curso y clase."""
    import inspect
    curso = None
    for fr in inspect.stack():
        nombre = Path(fr.filename).name
        for pref, c in _CURSOS:
            if nombre.startswith(pref):
                curso = c
                break
        if curso:
            break
    n = None
    try:
        for sh in prs.slides[0].shapes:
            if sh.has_text_frame:
                m = re.search(r"\bClase\s+(\d+)\b", sh.text_frame.text)
                if m:
                    n = int(m.group(1))
                    break
    except Exception:
        pass
    return curso, n


def para(titulo, prs=None):
    """`(ruta_png, None)` de la ilustracion del titulo, o `(None, None)`."""
    t = _norm(titulo)
    curso, n = contexto(prs) if prs is not None else (None, None)
    tabla = dict(ILUSTRACIONES.get("*", {}))
    tabla.update(ILUSTRACIONES.get((curso, n), {}))
    for clave, huella in tabla.items():
        if t.startswith(_norm(clave)):
            pasos = visuales.pasos_de(huella)
            if pasos:
                return pasos[-1], None
    try:
        PENDIENTES.parent.mkdir(parents=True, exist_ok=True)
        ya = PENDIENTES.read_text(encoding="utf-8").splitlines() if PENDIENTES.exists() else []
        linea = "%s\t%s\t%s" % (curso, n, titulo)
        if linea not in ya:
            with PENDIENTES.open("a", encoding="utf-8") as fh:
                fh.write(linea + "\n")
    except OSError:
        pass
    return None, None
