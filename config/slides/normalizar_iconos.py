# -*- coding: utf-8 -*-
"""Normaliza los iconos de herramientas que van en las diapositivas.

Por que existe
--------------
`herramientas_slide()` escala cada icono para que su lado mas largo entre en una
caja cuadrada de la tarjeta. Eso funciona solo si el ARCHIVO viene recortado: la
mayoria de los iconos del kit eran favicons de 16-32 px pegados en un lienzo de
256x256, asi que el dibujo ocupaba entre el 6 % y el 12 % de la imagen y en la
diapositiva salia como una mota, mientras los pocos iconos a sangre (mermaid,
vscode) llenaban la tarjeta. La grilla se veia descuadrada aunque el layout
estuviera bien.

Que hace
--------
1. INGESTA: toma los archivos sueltos que deja el docente (png/jpg/svg, con
   cualquier nombre) y los convierte al nombre canonico que usan los datos de
   cada curso (`bd2_taller_data.HERRAMIENTAS_DIA`, etc.).
2. NORMALIZACION: para cada icono recorta el margen vacio, lo vuelve a centrar en
   un lienzo cuadrado transparente y lo escala con peso optico homogeneo, de modo
   que un logo ancho y uno cuadrado se vean del mismo tamano en la tarjeta.

Uso:
    python config/slides/normalizar_iconos.py            # normaliza lo instalado
    python config/slides/normalizar_iconos.py --ingesta  # ademas importa lo suelto

Despues hay que regenerar las presentaciones para que tomen los iconos nuevos.
"""
from __future__ import annotations

import sys
from math import sqrt
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
DEST = Path(__file__).resolve().parent / "assets" / "herramientas"

#: Donde se buscan los archivos originales. La raiz del repo es donde el docente
#: los suelta; `_originales/` es donde quedan archivados despues de importarlos,
#: para poder volver a generar el PNG si cambian los parametros de normalizacion
#: (el recorte y el reescalado son destructivos).
ORIGENES = (ROOT, DEST / "_originales")

#: Lienzo final. 512 px sobra para el tamano al que se imprime (~1,15") y deja
#: margen si algun dia se usa el icono mas grande.
LIENZO = 512

#: Caja segura: fraccion del lienzo que el lado mas largo del dibujo no debe pasar.
CAJA_SEGURA = 0.86

#: Peso optico: fraccion del lienzo que deberia medir un logo CUADRADO. Los logos
#: anchos se compensan hacia arriba (hasta la caja segura) porque, a igual lado
#: mayor, ocupan menos superficie y se perciben mas pequenos.
PESO_OPTICO = 0.64

#: Archivos sueltos que deja el docente -> nombre canonico del asset.
#: `recortar_a`: (izq, arr, der, aba) en fraccion, para quedarse solo con el icono
#: cuando la fuente es un banner. `fondo_plano`: quita el fondo liso (JPEG sin alfa).
INGESTA = {
    "drawio_icon.svg":         dict(destino="drawio.png"),
    "DB-Fiddle_icon.png":      dict(destino="dbfiddle.png", fondo_plano=True),
    "Examlab_icon.png":        dict(destino="examlab.png"),
    "Oraclelive_icon.jpg":     dict(destino="oracle_livesql.png"),
    "SQLtestonline.icon.jpg":  dict(destino="sqltest.png", fondo_plano=True),
    "google-docs-icons.jpg":   dict(destino="google_docs.png",
                                    recortar_a=(0.10, 0.03, 0.94, 0.66),
                                    fondo_plano=True),
    # Segunda tanda: los que quedaban en baja resolucion.
    "Excalidraw_icon.png":     dict(destino="excalidraw.png", fondo_plano=True),
    "Github_icon.png":         dict(destino="github_actions.png"),
    "Padlet.con.png":          dict(destino="padlet.png", fondo_plano=True),
    # El tile negro y el azul son parte de la marca: quitarles el fondo dejaria
    # el rotulo blanco invisible sobre la tarjeta clara.
    "killercoda_icon.png":     dict(destino="killercoda.png"),
    "Labex_icon.png":          dict(destino="labex.png"),
    # La ballena sirve igual para el nombre canonico `docker` y para el asset
    # heredado `play_with_docker`, que antes tenia un favicon de 32 px.
    "Docker_icon.avif":        dict(destino=("docker.png", "play_with_docker.png")),
}


def _rasterizar_svg(path: Path) -> Image.Image:
    """SVG -> RGBA. python-pptx no embebe SVG, asi que hay que rasterizar."""
    from io import BytesIO

    from reportlab.graphics import renderPM
    from svglib.svglib import svg2rlg

    d = svg2rlg(str(path))
    escala = (LIENZO * 2) / max(d.width, d.height)
    d.width *= escala
    d.height *= escala
    d.scale(escala, escala)
    buf = BytesIO()
    renderPM.drawToFile(d, buf, fmt="PNG", bg=0xFFFFFF)
    buf.seek(0)
    im = Image.open(buf).convert("RGBA")
    return _quitar_fondo_plano(im)


def _quitar_fondo_plano(im: Image.Image, tol: int = 26) -> Image.Image:
    """Vuelve transparente el fondo liso o casi liso de una imagen sin alfa.

    Se toma el color de las cuatro esquinas como referencia y se hace
    transparente todo lo que este a menos de `tol` de distancia. Solo se aplica
    donde el icono viene de un JPEG o de un rasterizado con fondo: en un icono a
    sangre (un cuadrado de color de borde a borde) borraria el dibujo entero, por
    eso es opcional y no automatico.
    """
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()
    esquinas = [px[0, 0], px[w - 1, 0], px[0, h - 1], px[w - 1, h - 1]]
    fondo = tuple(sum(c[i] for c in esquinas) // 4 for i in range(3))
    # Se trabaja sobre el buffer plano: getdata() esta deprecado en Pillow 14 y
    # sobre iconos de 512x512 esto ademas es bastante mas rapido.
    buf = bytearray(im.tobytes())
    for i in range(0, len(buf), 4):
        r, g, b = buf[i], buf[i + 1], buf[i + 2]
        dist = max(abs(r - fondo[0]), abs(g - fondo[1]), abs(b - fondo[2]))
        if dist <= tol:
            buf[i + 3] = 0
        elif dist <= tol * 2:  # borde suave, para que no quede aserrado
            buf[i + 3] = int(buf[i + 3] * (dist - tol) / tol)
    return Image.frombytes("RGBA", im.size, bytes(buf))


def _bbox_contenido(im: Image.Image):
    """Caja del dibujo real, ignorando el margen transparente."""
    return im.getchannel("A").getbbox()


def normalizar(im: Image.Image) -> Image.Image:
    """Recorta el margen vacio y recentra con peso optico homogeneo."""
    im = im.convert("RGBA")
    caja = _bbox_contenido(im)
    if caja is None:                      # imagen totalmente transparente
        return im.resize((LIENZO, LIENZO), Image.LANCZOS)
    dibujo = im.crop(caja)
    w, h = dibujo.size
    k_largo = (LIENZO * CAJA_SEGURA) / max(w, h)
    k_area = (LIENZO * PESO_OPTICO) / sqrt(w * h)
    k = min(k_largo, k_area)
    nuevo = (max(1, round(w * k)), max(1, round(h * k)))
    dibujo = dibujo.resize(nuevo, Image.LANCZOS)
    lienzo = Image.new("RGBA", (LIENZO, LIENZO), (0, 0, 0, 0))
    lienzo.paste(dibujo, ((LIENZO - nuevo[0]) // 2, (LIENZO - nuevo[1]) // 2), dibujo)
    return lienzo


def _cargar(path: Path, opts: dict) -> Image.Image:
    # Pillow abre png/jpg/webp y tambien avif de forma nativa; solo el SVG hay que
    # rasterizarlo aparte. Sea cual sea el formato de entrada, lo que se guarda en
    # el kit es siempre PNG con alfa, que es lo unico que python-pptx embebe bien.
    if path.suffix.lower() == ".svg":
        im = _rasterizar_svg(path)
    else:
        im = Image.open(path).convert("RGBA")
        if opts.get("fondo_plano"):
            im = _quitar_fondo_plano(im)
    if opts.get("recortar_a"):
        l, t, r, b = opts["recortar_a"]
        w, h = im.size
        im = im.crop((int(w * l), int(h * t), int(w * r), int(h * b)))
    return im


def _buscar_origen(nombre: str) -> Path | None:
    for carpeta in ORIGENES:
        p = carpeta / nombre
        if p.exists():
            return p
    return None


def ingestar(archivar: bool = True) -> list[str]:
    """Importa los archivos originales al kit de iconos, con el nombre canonico.

    `archivar` mueve el original a `assets/herramientas/_originales/` para dejar
    limpia la raiz del repo sin perder la fuente.
    """
    hechos = []
    for origen, opts in INGESTA.items():
        p = _buscar_origen(origen)
        if p is None:
            continue
        destinos = opts["destino"]
        if isinstance(destinos, str):
            destinos = (destinos,)
        icono = normalizar(_cargar(p, opts))
        for d in destinos:
            icono.save(DEST / d)
        hechos.append(f"{origen} -> {', '.join(destinos)}")
        archivo = DEST / "_originales"
        if archivar and p.parent != archivo:
            archivo.mkdir(parents=True, exist_ok=True)
            p.replace(archivo / p.name)
    return hechos


def normalizar_instalados() -> list[str]:
    """Recorta y recentra todos los iconos ya instalados.

    Idempotente: un icono ya normalizado vuelve a salir igual, porque el recorte
    parte del contenido y no del lienzo.
    """
    hechos = []
    for p in sorted(DEST.glob("*.png")):
        antes = Image.open(p).convert("RGBA")
        caja = _bbox_contenido(antes)
        ocupacion = 0 if caja is None else max(caja[2] - caja[0], caja[3] - caja[1]) / max(antes.size)
        normalizar(antes).save(p)
        hechos.append(f"{p.name:24s} ocupacion antes {ocupacion * 100:3.0f}%")
    return hechos


def main() -> None:
    if "--ingesta" in sys.argv:
        for linea in ingestar(archivar="--no-archivar" not in sys.argv):
            print("INGESTA ", linea)
        print()
    for linea in normalizar_instalados():
        print("NORMAL  ", linea)
    print(f"\nListo. Lienzo {LIENZO}x{LIENZO}, caja segura {CAJA_SEGURA:.0%}, "
          f"peso optico {PESO_OPTICO:.0%}.")
    print("Regenera las presentaciones para que tomen los iconos:")
    print("  python config/slides/build_uniajc_bd2_all.py")
    print("  python config/slides/build_uniajc_arq_clases_batch.py")


if __name__ == "__main__":
    main()
