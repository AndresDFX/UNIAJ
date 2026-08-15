# -*- coding: utf-8 -*-
"""Genera los 12 parciales estudiante + 12 soluciones UNIAJC 2026-2.

Salida (solo docente): <Curso>/Parciales/
  - Parcial N - ….docx          (versión para aplicar el día del examen)
  - Parcial N - … - SOLUCION.docx

NO van en Clases/ (carpeta compartida con estudiantes).

Uso:
  python .config/parciales/build_parciales_2026_2.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

from contenido_parciales_2026_2 import TODOS  # noqa: E402
from parcial_docx_engine import build_docx  # noqa: E402


def main() -> int:
    generados = []
    for parcial in TODOS:
        meta = parcial["meta"]
        curso = meta["curso_dir"]
        archivo = meta["archivo"]
        est = ROOT / curso / "Parciales" / f"{archivo}.docx"
        sol = ROOT / curso / "Parciales" / f"{archivo} - SOLUCION.docx"
        build_docx(meta, parcial["secciones"], est, es_solucion=False)
        build_docx(meta, parcial["secciones"], sol, es_solucion=True)
        generados.append((est, sol, meta))
        print(f"OK  {curso} · Parcial {meta['n']} · {meta['fecha']} · Sesión {meta['clase']}")
        print(f"    EST: {est}")
        print(f"    SOL: {sol}")
        print("    Temas evaluados:")
        for t in meta["temas"]:
            print(f"      · {t}")

    print(f"\nTotal: {len(generados)} estudiante + {len(generados)} solución")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
