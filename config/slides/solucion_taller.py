# -*- coding: utf-8 -*-
"""Render de la solucion del taller, pregunta por pregunta (PRIVADO docente).

Por que existe
--------------
La solucion docente tiene que responder a los entregables **en el mismo archivo** y
con criterio de calificacion, no ser un resumen de tres vinetas. La version larga
se escribio primero para Arquitectura y BD II la necesita igual, asi que el
renderizador vive aqui y cada curso solo aporta sus datos. Escribirlo dos veces
garantizaba que las dos versiones se separaran en el primer cambio.

Cada pregunta se compone de tres bloques que NO deben mezclarse:

  - `respuesta` / `respuesta_mermaid` / `tabla` / `sql`  -> lo que se espera, resuelto
  - `como_calificar`  -> el desglose de puntos, copiado de la rubrica de la plataforma
  - `errores`         -> lo que llega mal y que hacer con ello

Y opcionalmente `justificacion`, para preguntas cerradas: la clave se lee del banco
que ve el estudiante, no se copia, de modo que la solucion no pueda quedar marcando
una opcion que en la plataforma ya cambio.
"""
from __future__ import annotations

EXAMLAB_URL = "https://uniaj.examlab.workers.dev/"


def _tabla_md(headers, rows):
    L = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    for fila in rows:
        L.append("| " + " | ".join(str(c) for c in fila) + " |")
    return L


def render_md(n, sol, *, contexto, opciones=None, mermaid_referencia=None,
              dominio_proyectado=None):
    """Markdown de la solucion de la clase `n`.

    `contexto` trae lo que cambia por curso y por clase: rutas, hito del PI y
    entregable. `opciones` y `mermaid_referencia` son funciones que leen del banco
    de preguntas del curso, para no duplicar la clave ni el modelo de referencia.
    """
    preguntas = sol["preguntas"]
    L = [
        f"# {sol['titulo']}",
        "",
        "> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab "
        "antes del cierre de la entrega.",
        "",
        f"**Resumen:** {sol['resumen']}",
        "",
    ]
    if sol.get("nota_actividad"):
        L += [f"> {sol['nota_actividad']}", ""]

    L += ["## Alineacion con el taller", ""]
    for etiqueta, valor in contexto.get("alineacion", []):
        L.append(f"- {etiqueta}: {valor}")
    L += [
        f"- **Estas preguntas: {sol['total']} puntos** en {len(preguntas)} preguntas.",
        "",
    ]
    L += _tabla_md(["#", "Pregunta", "Tipo", "Puntos"],
                   [[p["n"], p["titulo"], f"`{p['tipo']}`", p["puntos"]] for p in preguntas])
    L.append("")

    for p in preguntas:
        L += ["---", "", f"## Pregunta {p['n']} · {p['titulo']} · {p['puntos']} pts", ""]

        # `tabla` y `respuesta` pueden convivir (una matriz mas la prosa que la
        # defiende) y entonces comparten UN solo encabezado: la tabla abre, porque
        # es la respuesta, y la prosa la explica. Emitir el encabezado dos veces
        # dejaba el documento con «Respuesta esperada» repetido.
        if p.get("tabla"):
            t = p["tabla"]
            L += ["### Respuesta esperada", ""] + _tabla_md(t["headers"], t["rows"]) + [""]
            if p.get("respuesta"):
                L += [p["respuesta"], ""]
        elif p.get("respuesta"):
            L += ["### Respuesta esperada", "", p["respuesta"], ""]

        if p.get("sql"):
            # El SQL va en bloque propio para que se pueda pegar y correr tal cual
            # en el playground al revisar una entrega dudosa.
            L += ["### Respuesta esperada (SQL que corre tal cual)", "",
                  "```sql", p["sql"].strip(), "```", ""]

        if p.get("respuesta_mermaid"):
            L += ["### Respuesta esperada (dominio de la solucion)", "",
                  "```mermaid", p["respuesta_mermaid"].strip(), "```", ""]
            ref = mermaid_referencia(n) if mermaid_referencia else ""
            if ref:
                L += ["### Modelo de referencia que ve el estudiante", "",
                      "Es el que aparece en el enunciado de la plataforma"
                      + (f", sobre el dominio **{dominio_proyectado}**" if dominio_proyectado else "")
                      + ". Sirve para comparar estructura y conteos, no para calificar "
                        "contenido:", "",
                      "```mermaid", ref.strip(), "```", ""]

        if p.get("veredicto"):
            L += ["**Veredicto (las frases que se piden):**", "", f"> {p['veredicto']}", ""]

        if p.get("salida"):
            # Lo que el motor devuelve: sirve para comparar contra la captura que
            # entrega el estudiante sin tener que ejecutar nada.
            L += ["### Salida esperada", "", "```", p["salida"].strip(), "```", ""]

        if p.get("justificacion") and opciones:
            ops, correctas = opciones(n, p["n"])
            if ops:
                L += ["### Clave y por que", "",
                      "La clave se lee del banco de la plataforma, asi que esta es la que se "
                      "califica. La columna de la derecha es lo que hay que poder responderle "
                      "al estudiante cuando pregunte.", ""]
                L += _tabla_md(["", "Opcion", "Por que"],
                               [["**SI**" if i in correctas else "no", o,
                                 p["justificacion"].get(i, "—")]
                                for i, o in enumerate(ops)])
                L.append("")

        L += ["### Como calificar", ""] + [f"- {x}" for x in p["como_calificar"]] + [""]
        L += ["### Errores frecuentes y que hacer", ""] + [f"- {x}" for x in p["errores"]] + [""]

    if sol.get("preguntas_frecuentes"):
        L += ["---", "", "## Lo que van a preguntar (respuestas listas)", "",
              "Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por "
              "escrito es lo que evita responder la misma cosa quince veces durante el taller.",
              ""]
        for preg, resp in sol["preguntas_frecuentes"]:
            L += [f"**{preg}**", "", resp, ""]

    if sol.get("cierre"):
        # Se admiten las dos formas: una lista de puntos de cierre (BD II) o un
        # parrafo corrido (Arquitectura). Sin este isinstance, un `cierre` de texto
        # se iteraba caracter por caracter y salia una vineta por letra.
        cie = sol["cierre"]
        cuerpo = [cie] if isinstance(cie, str) else [f"- {x}" for x in cie]
        L += ["---", "", "## Cierre de la clase", ""] + cuerpo + [""]

    L += ["---", "",
          "## Politica de entrega",
          "",
          f"La entrega que se califica es la respuesta dentro de ExamLab ({EXAMLAB_URL}). "
          "El documento en Word o Google Docs es opcional y solo sirve para que el estudiante "
          "conserve sus respuestas. " + contexto.get("politica_extra", ""),
          ""]
    return "\n".join(L)
