# -*- coding: utf-8 -*-
"""Helpers compartidos: quiz estudiante (sin clave) + CLAVE DOCENTE + lines PPTX."""
from __future__ import annotations

from typing import Any


def q_om(pregunta: str, opciones: list[str], clave: str) -> dict[str, Any]:
    """Opción múltiple. clave = letra 'A'|'B'|'C'|'D'."""
    return {"tipo": "om", "q": pregunta, "opciones": opciones, "clave": clave}


def q_vf(afirmacion: str, clave: str) -> dict[str, Any]:
    """Verdadero/Falso. clave = 'V'|'F'."""
    return {"tipo": "vf", "q": afirmacion, "clave": clave.upper()}


def q_abierta(pregunta: str, clave: str) -> dict[str, Any]:
    """Abierta corta aplicada (PI / tema del día)."""
    return {"tipo": "abierta", "q": pregunta, "clave": clave}


def normalize_item(item: Any) -> dict[str, Any]:
    """Acepta dict tipado o tupla legacy (pregunta, respuesta)."""
    if isinstance(item, dict):
        return item
    if isinstance(item, (list, tuple)) and len(item) == 2:
        return q_abierta(str(item[0]), str(item[1]))
    raise TypeError(f"Ítem de quiz no soportado: {item!r}")


def student_lines(item: dict[str, Any], num: int) -> list[str]:
    """Líneas proyectables / estudiante: enunciado + opciones; sin clave."""
    it = normalize_item(item)
    lines = [f"**{num}.** {it['q']}"]
    tipo = it.get("tipo", "abierta")
    if tipo == "om":
        for op in it.get("opciones") or []:
            lines.append(f"   {op}")
    elif tipo == "vf":
        lines.append("   ( ) Verdadero    ( ) Falso")
    else:
        lines.append("   Respuesta corta: ____________________________")
    return lines


def clave_text(item: dict[str, Any], num: int) -> str:
    it = normalize_item(item)
    tipo = it.get("tipo", "abierta")
    clave = it.get("clave", "")
    if tipo == "om":
        return f"{num}. [OM] {clave}"
    if tipo == "vf":
        return f"{num}. [V/F] {clave}"
    return f"{num}. [Abierta] {clave}"


def pptx_chunks(quiz: list[Any], *, per_slide: int = 4) -> list[list[Any]]:
    """Parte el quiz en chunks de bullets para content_slide (solo preguntas).

    OM: pregunta + una opción por línea (nivel 1). Sin pipes ni claves.
    V/F y abiertas: enunciado en su línea + pista de respuesta indentada.
    """
    items = [normalize_item(x) for x in quiz]
    chunks: list[list[Any]] = []
    for start in range(0, len(items), per_slide):
        block = items[start : start + per_slide]
        lines: list[Any] = []
        for i, it in enumerate(block, start=start + 1):
            tipo = it.get("tipo", "abierta")
            lines.append(f"**{i}.** {it['q']}")
            if tipo == "om":
                for op in it.get("opciones") or []:
                    lines.append((str(op).strip(), 1))
            elif tipo == "vf":
                lines.append(("( ) Verdadero    ( ) Falso", 1))
            else:
                lines.append(("Respuesta corta: ____________________________", 1))
        chunks.append(lines)
    return chunks
