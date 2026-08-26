# -*- coding: utf-8 -*-
"""Lector del calendario académico UNIAJC 2026-2 para los builds de slides.

Fuente de verdad ÚNICA: ``config/calendario/semestre_2026_2.json``.
Este módulo NO duplica fechas: las lee. Si el calendario cambia (como pasó al
acortar el semestre a 13 sesiones), los builds no hay que tocarlos.

Vocabulario del periodo 2026-2 (semestre acortado: 24/08 → 22/11):
  * **Sesión N** = bloque real de clase en el calendario (hay 13).
  * **Clase N**  = unidad de material ya construida en ``Clases/`` y
    ``Kit docente/`` (hay 15; las carpetas NO se renumeran).
  Dos sesiones son **dobles**: cubren dos Clases de material en un bloque de
  120 min. Por eso 13 sesiones alcanzan para los 15 temas del microcurrículo.
"""
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.abspath(
    os.path.join(_HERE, "..", "calendario", "semestre_2026_2.json")
)

_MESES = None


def load():
    """Devuelve el JSON completo del calendario (cacheado)."""
    global _MESES
    if _MESES is None:
        with open(JSON_PATH, "r", encoding="utf-8") as fh:
            _MESES = json.load(fh)
    return _MESES


def curso(key):
    """Bloque del curso: 'programacion_ii' | 'seminario' | 'bases_datos_ii' | 'arquitectura'."""
    data = load()
    try:
        return data["cursos"][key]
    except KeyError:
        raise KeyError(
            "Curso '%s' no está en %s. Disponibles: %s"
            % (key, JSON_PATH, ", ".join(load()["cursos"]))
        )


def ddmm(iso):
    """'2026-09-21' -> '21/09'."""
    y, m, d = iso.split("-")
    return "%s/%s" % (d, m)


def ddmmyyyy(iso):
    """'2026-09-21' -> '21/09/2026'."""
    y, m, d = iso.split("-")
    return "%s/%s/%s" % (d, m, y)


def sesiones(key):
    """Las 13 sesiones del curso, tal cual el calendario."""
    return curso(key)["clases"]


def sesion_de_clase(key, clase_material):
    """Sesión (dict) en la que se dicta una Clase de material dada. None si no aparece."""
    for s in sesiones(key):
        if clase_material in (s.get("clases_material") or []):
            return s
    return None


def cortes(key):
    """Ventanas de corte + parcial de cierre, listo para ``evaluacion_cortes_slide``.

    Devuelve [{corte, pct, ventana, parcial_n, parcial_sesion, parcial_fecha,
    parcial_clase_material}, ...]. El ``desglose`` lo arma cada build porque el
    nombre del Proyecto Integrador cambia por curso (VetCare / CloudLite / …).
    """
    data = load()
    c = curso(key)
    out = []
    for i in (1, 2, 3):
        ct = data["cortes_teoricos"]["corte_%d" % i]
        p = c["parciales"]["parcial_%d" % i]
        ses = None
        for s in sesiones(key):
            if s.get("parcial_n") == i:
                ses = s
                break
        out.append({
            "corte": i,
            "pct": ct["pct"],
            "ventana": "%s – %s" % (ddmm(ct["inicio"]), ddmmyyyy(ct["fin"])),
            "parcial_n": i,
            "parcial_sesion": ses["n"] if ses else p.get("clase"),
            "parcial_fecha": ddmm(p["fecha"]),
            "parcial_clase_material": (ses.get("clases_material") or [None])[0] if ses else None,
        })
    return out


def contenido_items(key, temas_material, sesion0_tema, sesion0_fecha=None):
    """Ítems para ``contenido_clases_slide``: Sesión 0 + las 13 sesiones reales.

    ``temas_material``: {n_clase_material: "Tema bonito con acentos"} — 1..15.
    Cada ítem sale con ``label`` = «Sesión N» (no «Clase N») porque en 2026-2 los
    dos números ya no coinciden; el número de Clase de material va en el tag para
    que el estudiante sepa qué carpeta abrir.
    """
    ses = sesiones(key)
    items = [{
        "n": 0,
        "kind": "sesion0",
        "label": "Sesión 0",
        "tema": sesion0_tema,
        "fecha": sesion0_fecha or ddmm(ses[0]["fecha"]),
    }]
    for s in ses:
        n = s["n"]
        mats = s.get("clases_material") or []
        fecha = ddmm(s["fecha"])
        tipo = (s.get("tipo") or "").lower()
        tags = []
        if s.get("parcial"):
            tema = "Parcial %d" % s["parcial_n"]
            # Caso Seminario: el calendario mete la sustentación en el mismo bloque
            # del Parcial 3. No inventarlo ni ocultarlo: leerlo del tema del JSON.
            if "sustentacion" in (s.get("tema") or "").lower():
                tema += " + sustentación de proyectos y cierre"
                tags.append("virtual síncrona por Meet")
            else:
                tags.append("virtual síncrona · solo evaluación")
        elif tipo == "sustentacion":
            tema = " + ".join(temas_material[m] for m in mats) if mats else "Sustentación y cierre"
            tags.append("Sustentación del Proyecto Integrador")
            if mats:
                tags.append("material Clase %s" % "+".join(str(m) for m in mats))
        else:
            tema = " + ".join(temas_material[m] for m in mats)
            if tipo == "autonoma":
                tags.append("Autónoma (festivo)")
            if len(mats) > 1:
                tags.append("sesión doble · Clases %s" % "+".join(str(m) for m in mats))
            elif mats and mats[0] != n:
                tags.append("material Clase %d" % mats[0])
        items.append({
            "n": n,
            "label": "Sesión %d" % n,
            "tema": tema,
            "fecha": fecha,
            "tag": " · ".join(tags) if tags else None,
        })
    return items


def resumen_modalidad(key):
    """Frase corta y verdadera de modalidad/parciales para la slide de método."""
    c = cortes(key)
    ses_parciales = " / ".join(str(x["parcial_sesion"]) for x in c)
    return (
        "Clase 1 y parciales (sesiones **%s**) **presencial**; resto **virtual síncrona**; "
        "festivos = **clase autónoma**." % ses_parciales
    )


if __name__ == "__main__":  # smoke test
    for k in load()["cursos"]:
        c = curso(k)
        print("==", c["nombre"], "·", len(sesiones(k)), "sesiones")
        for x in cortes(k):
            print("   corte", x["corte"], x["pct"], x["ventana"],
                  "· parcial sesión", x["parcial_sesion"], x["parcial_fecha"],
                  "· material Clase", x["parcial_clase_material"])
