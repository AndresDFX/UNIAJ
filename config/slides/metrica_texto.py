# -*- coding: utf-8 -*-
"""Cuanto mide un texto en una diapositiva: anchos reales de Calibri.

Por que existe
--------------
El motor de slides pinta las vinetas en una caja de alto FIJO y PowerPoint dibuja el texto
igual si no cabe, encima de lo que haya debajo. Mientras el cuerpo fue de 13-16 pt eso casi
nunca pasaba; al subirlo a 20 —que es lo que hace legible una clase virtual, donde el
estudiante ve una ventana compartida y recomprimida— empieza a pasar, y hay que poder
decidir por diapositiva en vez de a ojo.

Aqui vive esa medida, una sola vez, y la usan dos consumidores:

  - `uniajc_slides_engine.bullets()` para elegir el tamano mas grande que cabe.
  - `verificar_desborde.py` para auditar un .pptx ya generado.

Dos cosas que costaron falsos positivos y estan resueltas aqui:

1. **Un ancho medio de caracter no sirve.** Con 0.48 em por caracter una diapositiva de
   14 pt que estaba bien salia como desbordada. Calibri ronda 0.41 em en texto corrido y la
   negrita es mas ancha, asi que se usan los anchos de avance REALES de la fuente, palabra
   por palabra y respetando que cada tramo puede ir en negrita.

2. **El `space_after` del ultimo parrafo no empuja nada.** Contarlo hacia fallar por 8 pt
   diapositivas que entraban justas.

Si Calibri o Pillow no estan disponibles, `disponible()` devuelve False y quien llama debe
seguir con su comportamiento de siempre: medir es una mejora, no un requisito del build.
"""
from __future__ import annotations

import os
import re

UPM = 1000                    # la fuente se carga a 1000 upem y se escala por tamano
INSET_H = 0.2                 # inset horizontal por omision de PowerPoint (0.1 por lado)
INSET_V = 0.1                 # inset vertical (0.05 arriba y 0.05 abajo)

_FUENTES: dict[bool, object] = {}
_ALTO_LINEA = 1.2207          # respaldo: el valor real de Calibri, ver `alto_linea()`
_OK: bool | None = None
_LH: float | None = None      # cache: leer la tabla de la fuente cuesta


def _ruta_fuente(negrita: bool) -> str:
    nombre = "calibrib.ttf" if negrita else "calibri.ttf"
    return os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", nombre)


def disponible() -> bool:
    """True si se puede medir de verdad (Pillow instalado y Calibri en el sistema)."""
    global _OK
    if _OK is None:
        try:
            _fuente(False)
            _fuente(True)
            _OK = True
        except Exception:
            _OK = False
    return _OK


def _fuente(negrita: bool):
    k = bool(negrita)
    if k not in _FUENTES:
        from PIL import ImageFont              # import perezoso: el build no lo exige
        _FUENTES[k] = ImageFont.truetype(_ruta_fuente(k), UPM)
    return _FUENTES[k]


def alto_linea() -> float:
    """Factor de interlineado simple de Calibri: 1.2207 veces el tamano de letra.

    OJO con `ImageFont.getmetrics()`: devuelve (750, 250) para Calibri cargada a 1000 upem,
    o sea 1.0, porque **se come el `lineGap`**. Calibri lo tiene y no es pequeno: la tabla
    `hhea` dice ascender 1536, descender -512 y lineGap 452 sobre 2048 unidades, que es
    1.2207 — un 18 % mas de lo que sugiere PIL. Medir con 1.0 subestima el alto de cada
    parrafo y hace pasar por buenas diapositivas que se salen de su caja, que es justo el
    fallo que este modulo tiene que detectar.
    """
    global _LH
    if _LH is None:
        try:
            from fontTools.ttLib import TTFont
            f = TTFont(_ruta_fuente(False))
            h, upem = f["hhea"], f["head"].unitsPerEm
            _LH = (h.ascender - h.descender + h.lineGap) / upem
        except Exception:
            _LH = _ALTO_LINEA
    return _LH


def ancho_pt(texto: str, size: float, negrita: bool = False) -> float:
    """Ancho de avance de `texto` en puntos, escrito a `size` puntos."""
    return _fuente(negrita).getlength(texto) / UPM * size


_NEGRITA = re.compile(r"(\*\*(?:[^*]|\*(?!\*))+?\*\*)")


def segmentos(texto: str) -> list[tuple[str, bool]]:
    """Parte `texto` en tramos `(cadena, negrita)`, igual que hace `_rich` en el motor.

    Se mantiene aqui porque medir un texto exige saber que tramos van en negrita: la
    negrita de Calibri es mas ancha y una vineta con media linea resaltada puede pasar de
    dos lineas a tres. El patron es el mismo que usa `_rich`, incluido el detalle de que
    admite un `*` solitario dentro del tramo resaltado (`COUNT(*)`).
    """
    out: list[tuple[str, bool]] = []
    for parte in _NEGRITA.split(str(texto)):
        if not parte:
            continue
        if parte.startswith("**") and parte.endswith("**"):
            out.append((parte[2:-2], True))
        else:
            out.append((parte, False))
    return out


def alto_parrafos(parrafos, ancho_in: float, size: float,
                  space_after_pt: float = 0.0, space_before_pt: float = 0.0) -> float:
    """Alto en pulgadas de una lista de parrafos ajustados a `ancho_in`.

    `parrafos` es una lista donde cada elemento es o una cadena o una lista de tramos
    `(cadena, negrita)` de `segmentos()`. El `space_after` no se suma al ultimo parrafo.
    """
    if not disponible():
        return 0.0
    disponible_pt = (ancho_in - INSET_H) * 72
    lh = alto_linea()
    total = 0.0
    n = len(parrafos)
    for i, par in enumerate(parrafos):
        tramos = segmentos(par) if isinstance(par, str) else list(par)
        piezas = [(w, b) for t, b in tramos for w in t.split(" ")]
        piezas = [p for p in piezas if p[0] != ""] or [("", False)]
        lineas, x = 1, 0.0
        for j, (w, b) in enumerate(piezas):
            aw = ancho_pt(w + (" " if j < len(piezas) - 1 else ""), size, b)
            if x > 0 and x + aw > disponible_pt:
                lineas += 1
                x = aw
            else:
                x += aw
        total += lineas * lh * size / 72
        total += space_before_pt / 72
        if i < n - 1:
            total += space_after_pt / 72
    return total + INSET_V


def tamano_que_cabe(parrafos, ancho_in: float, alto_in: float, objetivo: float,
                    minimo: float, space_after_pt: float = 0.0) -> float:
    """El tamano mas grande, de `objetivo` hacia abajo, con el que el texto cabe.

    Baja de punto en punto y nunca por debajo de `minimo`: si ni con el minimo cabe, lo que
    sobra es texto en la diapositiva, no tamano de letra, y devolver algo ilegible taparia
    el problema en vez de mostrarlo. `verificar_desborde.py` es quien lo denuncia.

    Sin metrica disponible devuelve `objetivo`, que es el comportamiento de siempre.
    """
    if not disponible():
        return objetivo
    size = float(objetivo)
    while size > minimo:
        if alto_parrafos(parrafos, ancho_in, size, space_after_pt) <= alto_in:
            return size
        size -= 1
    return max(float(minimo), size)
