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

import re

EXAMLAB_URL = "https://uniaj.examlab.workers.dev/"

_SPAN = re.compile(r"`([^`\n]+)`")
#: Igual que `_SPAN` pero para la negrita. Ver `_sin_spans`.
_FUERTE = re.compile(r"\*\*(.+?)\*\*", re.S)


def _sin_spans(texto):
    """Neutraliza el marcado inline del contenido que se emite DENTRO de una cerca.

    La «Salida esperada» va en un bloque cercado, y ahi Markdown no interpreta nada:
    las notas en prosa que acompanan a la salida salian con los acentos graves
    impresos, tanto en el .md como en el .docx. Dentro de una cerca no hay marcado
    inline valido, asi que cualquier `x` es marcado mal puesto y «x» es lo que ya usa
    el resto del repo cuando no hay monoespaciado disponible.

    Lo mismo pasaba con `**x**`, que no estaba contemplado: 11 preguntas de BD II
    —clases 6, 7, 12, 13 y 15— emitian los asteriscos literales en la solucion. Aqui
    se quitan sin sustituto, porque dentro de una cerca no hay con que resaltar. Si la
    nota merece negrita, el sitio correcto es `nota_salida`, que se emite FUERA de la
    cerca justamente para eso.
    """
    return _FUERTE.sub(r"\1", _SPAN.sub(r"«\1»", texto))


#: Una linea abre bloque nuevo (no se une a la anterior) si esta en blanco o si
#: empieza por un marcador de Markdown: vineta, item numerado, cita, tabla o titulo.
#:
#: La segunda alternativa cubre la linea que es ENTERA una negrita, que en este corpus
#: siempre es un rotulo de seccion («**2. Quien los rota**»). Empieza por `*`, asi que
#: la primera alternativa no la reconoce como marcador, y `_reflujo` la pegaba al
#: parrafo siguiente: la solucion de la Clase 6 de Arquitectura salia con «2. Quien los
#: rota El dueno del repositorio, que...» en un solo renglon. Los rotulos 1, 3 y 4 de
#: esa misma respuesta se salvaban solo porque los sigue una vineta.
_ABRE_BLOQUE = re.compile(r"^\s*(?:[-*+]\s|\d+[.)]\s|>|\||#|\*\*.+\*\*\s*$)")


def _reflujo(texto):
    """Une los renglones de un mismo parrafo en UNA linea logica.

    Los campos de prosa se escriben con salto de linea manual a ~80 columnas para que
    el fuente sea legible. El conversor a .docx emite un parrafo por renglon y resuelve
    la negrita renglon por renglon, asi que un tramo `**...**` partido por un salto de
    linea no encontraba su cierre y los cuatro asteriscos salian IMPRESOS en la
    solucion del docente. Estaba en 11 preguntas —BD II clases 6, 7, 12, 13 y 15— y en
    los campos equivalentes de Arquitectura.

    En Markdown un salto de linea simple ya es un salto blando, asi que unir los
    renglones es lo que el formato dice que significan. Se respetan los renglones que
    abren bloque (vinetas, items numerados, citas, tablas, titulos) y las lineas en
    blanco, que son los unicos saltos con significado.

    Y se respeta lo que va DENTRO de una cerca ```: ahi el salto de linea es el
    contenido. Sin esta guarda, el bloque de Python de la clase 12 se unia en un solo
    renglon y la cerca de cierre terminaba pegada a la prosa siguiente.
    """
    bloques, en_cerca = [], False
    for linea in texto.strip().split("\n"):
        if linea.lstrip().startswith("```"):
            en_cerca = not en_cerca
            bloques.append(linea.rstrip())
        elif en_cerca or not linea.strip():
            bloques.append(linea.rstrip() if en_cerca else "")
        elif bloques and bloques[-1] and not bloques[-1].lstrip().startswith("```") \
                and not _ABRE_BLOQUE.match(linea):
            bloques[-1] += " " + linea.strip()
        else:
            bloques.append(linea.rstrip())
    return "\n".join(bloques)


def _tabla_md(headers, rows):
    L = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    for fila in rows:
        L.append("| " + " | ".join(str(c) for c in fila) + " |")
    return L


def render_md(n, sol, *, contexto, opciones=None, mermaid_referencia=None,
              dominio_referencia=None):
    """Markdown de la solucion de la clase `n`.

    `contexto` trae lo que cambia por curso y por clase: rutas, hito del PI y
    entregable. `opciones` y `mermaid_referencia` son funciones que leen del banco
    de preguntas del curso, para no duplicar la clave ni el modelo de referencia.
    `dominio_referencia` es el dominio sobre el que esta resuelto ese modelo, que no
    es el que se proyecta en el deck ni el que resuelve la solucion.
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
                L += [_reflujo(p["respuesta"]), ""]
        elif p.get("respuesta"):
            L += ["### Respuesta esperada", "", _reflujo(p["respuesta"]), ""]

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
                # Antes esto se titulaba «Modelo de referencia que ve el estudiante» y
                # decia que aparece en el enunciado de la plataforma. Es falso: el
                # `mermaid_esperado` del banco se emite en el kit docente bajo
                # «Diagrama de referencia (Mermaid)», que es el unico bloque de esa
                # ficha SIN instruccion de pegar —el enunciado y el flujo de entrega si
                # la llevan—. El estudiante nunca lo ve, y un docente que creyera lo
                # contrario descontaria por no parecerse a un diagrama que nadie
                # proyecto: el criterio rector al reves.
                L += ["### Modelo de referencia del kit docente (el estudiante NO lo ve)", ""]
                L += ["Vive en `Taller en ExamLab - Clase "
                      f"{n} (configuracion).md` y no se pega en el enunciado"
                      + (f"; esta resuelto sobre el dominio **{dominio_referencia}**"
                         if dominio_referencia else "")
                      + ". Sirve para comparar estructura y conteos —cuantas cajas, "
                        "cuales son almacenes, si toda flecha lleva protocolo y "
                        "formato—, **nunca** para calificar contenido ni nombres:", "",
                      "```mermaid", ref.strip(), "```", ""]

        if p.get("veredicto"):
            L += ["**Veredicto (las frases que se piden):**", "",
                  f"> {_reflujo(p['veredicto'])}", ""]

        if p.get("salida"):
            # Lo que el motor devuelve: sirve para comparar contra la captura que
            # entrega el estudiante sin tener que ejecutar nada. Por eso la cerca
            # lleva SOLO la salida: la prosa que la interpreta —que numero es
            # determinista, que hacer si el estudiante reporta otro— va en
            # `nota_salida`, fuera de la cerca. Mezclarlas dejaba parrafos de criterio
            # de calificacion en monoespaciado dentro de lo que el docente compara
            # contra una captura, y de paso perdia la negrita.
            L += ["### Salida esperada", "", "```", _sin_spans(p["salida"].strip()), "```", ""]
            if p.get("nota_salida"):
                L += [_reflujo(p["nota_salida"]), ""]

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
