# -*- coding: utf-8 -*-
"""Renderiza todas las animaciones de una carpeta a GIF + fijos, para insertarlas en el deck.

    python config/animaciones/renderizar.py bd2/clase4 [huella ...]

Por cada `<huella>.js` de `config/animaciones/<carpeta>/` (los `_*.js` son piezas comunes):
captura los fotogramas con `capturar.mjs` y los junta con `gif.py` en
`config/animaciones/render/<carpeta>/<huella>.gif`, con `-fin.png` y `-mitad.png` al lado.
Los fotogramas intermedios van a una carpeta temporal y se borran.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import gif  # noqa: E402

FOTOGRAMAS = 40
ANCHO, ALTO = 800, 640


def pasos_de(mod):
    """Los momentos `t` donde el docente se detiene a explicar, declarados en el modulo."""
    import re
    m = re.search(r"pasos\s*:\s*\[([^\]]*)\]", mod.read_text(encoding="utf-8"))
    if m:
        v = [float(x) for x in m.group(1).split(",") if x.strip()]
        if v:
            return v if v[-1] >= 1 else v + [1.0]
    return [0.35, 0.7, 1.0]


def renderizar(carpeta, huellas=None):
    fuente = AQUI / carpeta
    destino = AQUI / "render" / carpeta
    mods = sorted(p for p in fuente.glob("*.js") if not p.name.startswith("_"))
    if huellas:
        mods = [p for p in mods if p.stem in huellas]
    hechos = []
    for mod in mods:
        with tempfile.TemporaryDirectory() as tmp:
            # Con tiempo limite y un reintento: un Chrome headless que no responde dejaba el
            # render colgado horas sin decir nada.
            for intento in (1, 2):
                try:
                    r = subprocess.run(["node", str(AQUI / "capturar.mjs"), str(mod), "", tmp,
                                        str(FOTOGRAMAS), str(ANCHO), str(ALTO)],
                                       capture_output=True, text=True, encoding="utf-8", timeout=150)
                    break
                except subprocess.TimeoutExpired:
                    if intento == 2:
                        raise SystemExit("%s: el navegador no respondio en 150 s" % mod.name)
            if r.returncode:
                raise SystemExit("%s: %s%s" % (mod.name, r.stdout, r.stderr))
            salida = gif.construir(tmp, destino / (mod.stem + ".gif"))
        # Los PASOS: un fijo en cada pausa que declara el modulo (`pasos: [0.3, 0.6, 1]`).
        # En la lamina, cada paso aparece con un clic: la animacion avanza al ritmo del docente.
        pasos = pasos_de(mod)
        with tempfile.TemporaryDirectory() as tmp:
            for intento in (1, 2, 3):
                try:
                    r = subprocess.run(["node", str(AQUI / "capturar.mjs"), str(mod), "", tmp, "1",
                                        str(ANCHO), str(ALTO), ",".join(str(x) for x in pasos)],
                                       capture_output=True, text=True, encoding="utf-8", timeout=150)
                    break
                except subprocess.TimeoutExpired:
                    if intento == 3:
                        raise SystemExit("%s: el navegador no respondio (pasos)" % mod.name)
            if r.returncode:
                raise SystemExit("%s (pasos): %s%s" % (mod.name, r.stdout, r.stderr))
            for viejo in destino.glob(mod.stem + "-paso*.png"):
                viejo.unlink()
            for k, f in enumerate(sorted(Path(tmp).glob("f*.png")), 1):
                (destino / ("%s-paso%d.png" % (mod.stem, k))).write_bytes(f.read_bytes())
        avisos = [l for l in r.stdout.splitlines() if l.startswith("AVISO")]
        print("OK %-28s %4d KB · %d pasos%s" % (mod.stem, salida.stat().st_size // 1024, len(pasos),
              "" if not avisos else " · PASOS ILOGICOS: " + "; ".join(a[6:] for a in avisos)))
        hechos.append(salida)
    return hechos


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    renderizar(sys.argv[1], sys.argv[2:] or None)
