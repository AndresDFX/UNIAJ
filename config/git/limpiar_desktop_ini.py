# -*- coding: utf-8 -*-
r"""Saca los `desktop.ini` que Google Drive siembra DENTRO de `.git/`.

El problema
-----------
Este repo vive en `G:\My Drive\...`, y Google Drive escribe un `desktop.ini`
oculto en cada carpeta que sincroniza (es metadata de shell de Windows: guarda el
icono de Drive, apunta a `GoogleDriveFS.exe`). Cuando eso cae dentro de
`.git/refs/`, git rompe: **lee todo archivo bajo `refs/` como si fuera una
referencia**, asi que `.git/refs/desktop.ini` pasa a ser un ref llamado
`refs/desktop.ini` cuyo contenido no es un SHA. De ahi el error:

    fatal: bad object refs/desktop.ini
    error: ... did not send all necessary objects

y con el `git pull`, `git fetch` y `git push` quedan inutilizables.

Por que `.gitignore` no lo arregla
----------------------------------
En el arbol de trabajo si: `desktop.ini` esta ignorado y ahi no molesta. Pero git
**nunca** aplica reglas de ignore a su propio directorio `.git/`, asi que no hay
patron que evite esto. La unica salida es borrarlos.

Que borra y que no
------------------
- Borra solo archivos que se llamen exactamente `desktop.ini` (sin importar
  mayusculas) y solo dentro del directorio de git. Nada mas.
- `refs/` y `logs/` son los criticos (los que rompen git). Los de
  `objects/XX/` son inofensivos —git solo mira nombres de 38 hex ahi— pero se
  limpian igual para no dejar basura.
- Borra ademas carpetas vacias que queden bajo `refs/heads/` o `refs/remotes/`
  por ramas ya eliminadas: son imanes de `desktop.ini` y no sirven para nada.
  `refs/heads`, `refs/tags` y `refs/remotes` NO se tocan: git las espera.

Uso
---
    python config/git/limpiar_desktop_ini.py            # limpia y reporta
    python config/git/limpiar_desktop_ini.py --silencioso   # solo habla si borro algo

Equivalente a mano, si no hay Python cerca (desde la raiz del repo):
    find .git -iname desktop.ini -delete

Sale siempre con codigo 0 para poder colgarlo de un hook sin bloquear nada.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

#: Carpetas que git espera que existan aunque esten vacias.
REFS_ESTANDAR = {"heads", "tags", "remotes"}


def raiz_git(inicio: Path) -> Path | None:
    """Directorio de git (`.git/`) subiendo desde `inicio`.

    Soporta el caso en que `.git` es un ARCHIVO con `gitdir: <ruta>` (worktrees y
    repos con git-dir separado): ahi el directorio real esta en otra parte.
    """
    for d in [inicio, *inicio.parents]:
        g = d / ".git"
        if g.is_dir():
            return g
        if g.is_file():
            try:
                texto = g.read_text(encoding="utf-8", errors="replace").strip()
            except OSError:
                return None
            if texto.startswith("gitdir:"):
                destino = Path(texto.split(":", 1)[1].strip())
                if not destino.is_absolute():
                    destino = (d / destino).resolve()
                return destino if destino.is_dir() else None
    return None


def limpiar(gitdir: Path) -> tuple[list[Path], list[Path], list[str]]:
    """Borra los desktop.ini y las carpetas de refs vacias. Devuelve lo hecho."""
    borrados: list[Path] = []
    dirs_borrados: list[Path] = []
    fallos: list[str] = []

    for actual, _subdirs, archivos in os.walk(gitdir):
        for nombre in archivos:
            if nombre.lower() == "desktop.ini":
                f = Path(actual) / nombre
                try:
                    # Vienen con atributo oculto; en Windows eso no impide borrar,
                    # pero si son de solo lectura hay que quitarlo primero.
                    try:
                        f.chmod(0o666)
                    except OSError:
                        pass
                    f.unlink()
                    borrados.append(f)
                except OSError as e:
                    fallos.append(f"{f}: {e}")

    # Carpetas vacias bajo refs/, de ramas ya borradas (bottom-up para anidadas).
    refs = gitdir / "refs"
    if refs.is_dir():
        for actual, subdirs, archivos in os.walk(refs, topdown=False):
            d = Path(actual)
            if d == refs or archivos or subdirs:
                continue
            if d.parent == refs and d.name in REFS_ESTANDAR:
                continue  # refs/heads, refs/tags, refs/remotes: git las espera
            try:
                d.rmdir()
                dirs_borrados.append(d)
            except OSError as e:
                fallos.append(f"{d}: {e}")

    return borrados, dirs_borrados, fallos


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Borra los desktop.ini que Google Drive deja dentro de .git/"
    )
    ap.add_argument("--silencioso", action="store_true",
                    help="no imprime nada si no habia nada que borrar")
    ap.add_argument("--repo", default=None,
                    help="ruta del repo (por defecto: se busca desde este archivo)")
    args = ap.parse_args()

    inicio = Path(args.repo).resolve() if args.repo else Path(__file__).resolve().parent
    gitdir = raiz_git(inicio)
    if gitdir is None:
        if not args.silencioso:
            print(f"No encontre un repo git desde {inicio}", file=sys.stderr)
        return 0

    borrados, dirs_borrados, fallos = limpiar(gitdir)

    if not borrados and not dirs_borrados and not fallos:
        if not args.silencioso:
            print(f"OK: sin desktop.ini dentro de {gitdir}")
        return 0

    criticos = [b for b in borrados
                if "refs" in b.relative_to(gitdir).parts
                or "logs" in b.relative_to(gitdir).parts]
    print(f"Limpieza de {gitdir}:")
    if borrados:
        print(f"  desktop.ini borrados: {len(borrados)}"
              + (f"  ({len(criticos)} en refs/ o logs/, los que rompen git)"
                 if criticos else "  (ninguno critico)"))
    for d in dirs_borrados:
        print(f"  carpeta de ref vacia eliminada: {d.relative_to(gitdir)}")
    for f in fallos:
        print(f"  !! no se pudo borrar {f}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
