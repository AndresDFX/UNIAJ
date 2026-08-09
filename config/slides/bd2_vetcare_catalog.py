# -*- coding: utf-8 -*-
"""Catalogo tematico BD II 2026-2 — hilo conductor VetCare DB (PI)."""
CLASES = []
def by_n(n: int):
    for c in CLASES:
        if c["n"] == n:
            return c
    raise KeyError(n)
