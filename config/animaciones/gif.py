# -*- coding: utf-8 -*-
"""Junta los fotogramas de `capturar.mjs` en un GIF animado y saca los fijos para las laminas.

    python config/animaciones/gif.py <carpeta-fotogramas> <salida.gif> [duracion_s] [pausa_final_s]

PowerPoint reproduce el GIF solo, en bucle, sin mando: por eso el ultimo fotograma se sostiene
`pausa_final_s` segundos, para que la idea completa se alcance a leer antes de volver a empezar.
Ademas deja `<salida>-fin.png` (el ultimo fotograma, que se lee solo) y `<salida>-mitad.png`, que
son los fijos para las laminas de continuacion de la misma seccion.
"""
import sys
from pathlib import Path

from PIL import Image


def construir(carpeta, salida, duracion=3.2, pausa=2.5):
    fotos = sorted(Path(carpeta).glob("f*.png"))
    if not fotos:
        raise SystemExit("no hay fotogramas en %s" % carpeta)
    cuadros = [Image.open(f).convert("RGB") for f in fotos]
    # Paleta comun: la marca son pocos colores planos, y una paleta compartida evita el
    # parpadeo de colores entre fotogramas que da la cuantizacion por cuadro.
    base = cuadros[-1].quantize(colors=128, method=Image.Quantize.MEDIANCUT)
    pal = [c.quantize(palette=base, dither=Image.Dither.NONE) for c in cuadros]
    paso = max(20, int(duracion * 1000 / len(pal)))
    # El PRIMER cuadro es el final: la miniatura, la impresion y el PDF muestran solo el primer
    # cuadro de un GIF, y el de t=0 esta casi vacio. Se sostiene un momento y despues anima.
    pal = [pal[-1]] + pal
    tiempos = [int(pausa * 1000)] + [paso] * (len(pal) - 2) + [int(pausa * 1000)]
    salida = Path(salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    pal[0].save(salida, save_all=True, append_images=pal[1:], duration=tiempos, loop=0,
                optimize=True, disposal=1)
    cuadros[-1].save(salida.with_name(salida.stem + "-fin.png"))
    cuadros[len(cuadros) // 2].save(salida.with_name(salida.stem + "-mitad.png"))
    return salida


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) < 2:
        raise SystemExit(__doc__)
    s = construir(a[0], a[1], *(float(x) for x in a[2:4]))
    print("%s · %d KB" % (s, s.stat().st_size // 1024))
