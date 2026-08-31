# -*- coding: utf-8 -*-
"""Lector del calendario de Introducción a la Ingeniería (FI300101) · 2026-2.

Fuente de verdad ÚNICA: ``config/calendario/introduccion_ingenieria_2026_2.json``.
Este módulo NO duplica fechas, temas ni porcentajes: los lee.

Por qué no reusa ``calendario_2026_2.py``
-----------------------------------------
Ese módulo asume **un** grupo por curso, 13 sesiones y el mapeo Sesión → Clase(s)
de material del semestre acortado. Este curso tiene **tres grupos en dos días
distintos**, **16 sesiones** que corresponden 1:1 con los 16 temas, es
**presencial**, y sus cortes cierran en las sesiones 6/11/16 sin parcial escrito.
Forzarlo en la misma estructura habría roto ``validar_calendario.py`` sin ganar nada.

Vocabulario
-----------
* **Sesión N** = bloque real de 90 min en el calendario del grupo (hay 16).
* **Clase N**  = carpeta de material (``Clases/Clase N - …``, ``Kit docente/Clase N/``).
  Aquí **Sesión N == Clase N**: no hay sesiones dobles ni renumeración.
* **Semana autónoma** = semana de festivo. No se omite; lleva tarea concreta y
  ``sesion`` viene en ``None`` porque no consume número de sesión.
"""
from __future__ import annotations

import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.abspath(
    os.path.join(_HERE, "..", "calendario", "introduccion_ingenieria_2026_2.json")
)

_DATA = None

DOCENTE = "Julian Andres Castaño"
CORREO = "julianacastano@profesores.uniajc.edu.co"
CREDS = [
    "Ingeniero de Sistemas",
    "Candidato a MsC en Inteligencia Artificial",
    "Líder Técnico · Speaker Tecnológico",
]

# El JSON de este curso SÍ lleva tildes en su prosa, al contrario que los módulos de
# datos `.py` de los talleres: allí la convención existía por el escapado de cadenas,
# que en JSON no es un problema. Solo se conservan pares con/sin tildes donde la forma
# sin tildes se usa como nombre de carpeta o de archivo (`nombre`, `folder`, `slug`,
# `tema`). Así ningún texto proyectado se escribe dos veces.


def load():
    """JSON completo del curso (cacheado)."""
    global _DATA
    if _DATA is None:
        with open(JSON_PATH, "r", encoding="utf-8") as fh:
            _DATA = json.load(fh)
    return _DATA


def curso():
    return load()["curso"]


def dinamica():
    return load()["dinamica_sesion"]


def plataformas():
    return load()["plataformas"]


def cortes():
    return load()["cortes"]


def temas():
    """Los 16 temas, ordenados por número."""
    return sorted(load()["temas"], key=lambda t: t["n"])


def tema(n):
    for t in temas():
        if t["n"] == n:
            return t
    raise KeyError("No existe el tema %s (hay %s)" % (n, len(temas())))


def temas_acentos():
    """{n: "Tema con acentos"} — lo que se proyecta."""
    return {t["n"]: t["tema_acentos"] for t in temas()}


def grupos():
    return load()["grupos"]


def grupo(codigo):
    for g in grupos():
        if g["grupo"] == codigo:
            return g
    raise KeyError(
        "Grupo '%s' no está en %s. Disponibles: %s"
        % (codigo, JSON_PATH, ", ".join(g["grupo"] for g in grupos()))
    )


def codigos_grupo():
    return [g["grupo"] for g in grupos()]


# ---------- Fechas ----------

def ddmm(iso):
    """'2026-09-01' -> '01/09'."""
    y, m, d = iso.split("-")
    return "%s/%s" % (d, m)


def ddmmyyyy(iso):
    """'2026-09-01' -> '01/09/2026'."""
    y, m, d = iso.split("-")
    return "%s/%s/%s" % (d, m, y)


def sesiones(codigo):
    """Filas del calendario del grupo, en orden, **incluida** la semana autónoma."""
    return grupo(codigo)["sesiones"]


def sesiones_reales(codigo):
    """Solo las 16 sesiones numeradas (sin la semana autónoma de festivo)."""
    return [s for s in sesiones(codigo) if s.get("sesion") is not None]


def fecha_de_sesion(codigo, n):
    for s in sesiones_reales(codigo):
        if s["sesion"] == n:
            return s["fecha"]
    return None


def semanas_autonomas(codigo):
    return [s for s in sesiones(codigo) if s.get("sesion") is None]


# ---------- Piezas listas para las diapositivas ----------

def cortes_slide(codigo):
    """``cortes`` en el formato que espera ``evaluacion_cortes_slide``.

    La ventana y la fecha del cierre de corte se calculan con el calendario **del
    grupo**: los tres grupos comparten porcentajes y desglose, pero no fechas.
    """
    ses = sesiones_reales(codigo)
    fecha_de = {s["sesion"]: s["fecha"] for s in ses}
    out = []
    for c in cortes():
        a, b = (int(x) for x in c["sesiones"].split("-"))
        cierre_n = c["cierra_en_sesion"]
        out.append({
            "corte": c["corte"],
            "pct": c["pct"],
            "ventana": "%s – %s · sesiones %d-%d" % (ddmm(fecha_de[a]), ddmmyyyy(fecha_de[b]), a, b),
            "desglose": c["desglose"],
            "cierre_sesion": cierre_n,
            "cierre_fecha": ddmmyyyy(fecha_de[cierre_n]),
        })
    return out


def contenido_items(codigo):
    """Ítems para ``contenido_clases_slide``: Sesión 0 + las 16 sesiones + autónoma.

    La Sesión 0 (Presentación del Curso) va en el mismo bloque que la Sesión 1: no
    es una semana aparte, es la primera media hora del primer día.
    """
    ta = temas_acentos()
    ses = sesiones(codigo)
    primera = next(s["fecha"] for s in ses if s.get("sesion") == 1)
    cierres = {c["cierra_en_sesion"]: c for c in cortes()}
    items = [{
        "n": 0,
        "label": "Sesión 0",
        "tema": "Presentación del curso: encuadre, evaluación, equipos y plataformas",
        "fecha": ddmm(primera),
        "tag": "mismo bloque de la Sesión 1",
    }]
    for s in ses:
        n = s.get("sesion")
        if n is None:
            items.append({
                "n": "—",
                "label": "Semana autónoma",
                "tema": "Ensayo general de la exposición final (trabajo de equipo, sin docente)",
                "fecha": ddmm(s["fecha"]),
                "tag": "festivo: %s · no se pierde, se trabaja" % s.get("festivo", "festivo"),
            })
            continue
        tags = []
        if n in cierres:
            tags.append("cierra Corte %d (%s)" % (cierres[n]["corte"], cierres[n]["pct"]))
        items.append({
            "n": n,
            "label": "Sesión %d" % n,
            "tema": ta[s["tema_n"]],
            "fecha": ddmm(s["fecha"]),
            "tag": " · ".join(tags) if tags else None,
        })
    return items


def timeline_slots(codigo):
    """``slots`` para ``block_timeline_slide``, con el reloj real del grupo.

    Sin saltos de línea: cada columna del timeline mide ~1,8" y el texto se escribe
    en un solo *run*, donde un ``\\n`` no produce salto fiable en PowerPoint. El
    detalle largo de cada bloque va en la tabla de ``tabla_dinamica``, no aquí.
    """
    g = grupo(codigo)
    reloj = dinamica()["reloj_por_grupo"][g["hora_inicio_oficial"]]
    out = []
    for b, linea in zip(dinamica()["bloques"], reloj):
        # "14:30 - 14:40 Apertura" -> se usa solo el rango horario como rótulo
        rango = " ".join(linea.split()[:3]).replace(" - ", "–")
        out.append({
            "t": "%s · %d min" % (rango, b["min"]),
            "label": "**%s** — %s" % (b["nombre"], b["corto"]),
        })
    return out


def tabla_dinamica(codigo):
    """``(headers, rows)`` con el detalle completo de la dinámica del grupo."""
    g = grupo(codigo)
    reloj = dinamica()["reloj_por_grupo"][g["hora_inicio_oficial"]]
    rows = []
    for b, linea in zip(dinamica()["bloques"], reloj):
        rango = " ".join(linea.split()[:3]).replace(" - ", " – ")
        rows.append([rango, "%d min" % b["min"], b["nombre"], b["que_pasa"]])
    return ["Reloj", "Duración", "Bloque", "Qué pasa"], rows


def linea_horario(codigo):
    g = grupo(codigo)
    return "Horario: **%s %s** (%d min) · Inicio efectivo **%s**" % (
        g["dia"], g["horario"].replace(" - ", " – "), curso()["duracion_min"],
        g["hora_inicio_efectiva"],
    )


if __name__ == "__main__":  # smoke test
    c = curso()
    print("==", c["nombre_acentos"], "·", c["codigo"], "·", c["modalidad"])
    for g in grupos():
        n_real = len(sesiones_reales(g["grupo"]))
        n_aut = len(semanas_autonomas(g["grupo"]))
        print("  %-7s %-8s %-14s S1=%s  S%d=%s  (%d semanas, %d autonoma)"
              % (g["grupo"], g["dia"], g["horario"], g["inicio"], n_real,
                 g["fin"], g["n_semanas_calendario"], n_aut))
        for x in cortes_slide(g["grupo"]):
            print("       corte %d %-4s %s · cierra sesion %d (%s)"
                  % (x["corte"], x["pct"], x["ventana"], x["cierre_sesion"], x["cierre_fecha"]))
    d = dinamica()
    print("== dinamica:", sum(b["min"] for b in d["bloques"]), "min en",
          len(d["bloques"]), "bloques ·", d["equipos"]["cantidad_fija"], "equipos x",
          d["equipos"]["min_por_equipo"], "min")
