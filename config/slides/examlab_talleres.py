# -*- coding: utf-8 -*-
"""Talleres resueltos DENTRO de ExamLab: render para estudiante y para docente.

Por que existe
--------------
Los talleres decian «suba el resultado a ExamLab» y ahi terminaba la instruccion.
El estudiante no sabia que iba a encontrar en la plataforma ni en que forma se
entrega cada cosa, y el material pedia exportar PNG de draw.io o correr SQL en
DB Fiddle cuando ExamLab ya trae editor de diagramas Mermaid, PostgreSQL real
(PGlite/WASM) y ejecucion de GUI de Java en el navegador. Resultado: se salia de
la plataforma para hacer a mano lo que la plataforma hace nativo, y la entrega
quedaba como un archivo suelto imposible de revisar.

Este modulo toma la especificacion del taller por clase (`<curso>_examlab_data.py`)
y genera dos vistas de la MISMA fuente:

  - `bloque_estudiante()`  -> seccion del .docx del taller: que va a encontrar en
    ExamLab, pregunta por pregunta, con su forma de entrega y sus puntos.
  - `guia_docente_md()`    -> documento del Kit docente con TODO lo necesario para
    armar el taller en la plataforma (tipo, enunciado, puntos, rubrica, setup SQL,
    starter code, Mermaid de referencia).

Por que la guia del docente es un documento y no un import automatico: ExamLab NO
soporta importar preguntas desde archivo (el propio banco de preguntas exporta CSV
pero no importa, porque `options`/`starter_code`/`expected_rubric` no caben en CSV
plano). El alta se hace en la UI o con la pestana de IA. Asi que lo util es dejarle
al docente el texto exacto para pegar campo por campo.

Tipos de pregunta soportados por la plataforma (verificado en el codigo de
ExamLab, `src/modules/workshops/WorkshopQuestions.tsx`):
    abierta · cerrada · cerrada_multi · codigo · diagrama · java_gui ·
    python_gui · codigo_zip · red_consola · red_gui · so_consola · bd_sql
"""
from __future__ import annotations

import re

EXAMLAB_URL = "https://uniaj.examlab.workers.dev/"

# Como se le explica al ESTUDIANTE cada tipo: que va a ver y que se espera que
# deje. La clave es que sepa la FORMA de la respuesta antes de abrir la pregunta.
TIPOS = {
    "abierta": (
        "Respuesta escrita",
        "Un cuadro de texto. Se escribe directamente en la plataforma; no se sube archivo.",
    ),
    "cerrada": (
        "Seleccion unica",
        "Varias opciones, una sola correcta.",
    ),
    "cerrada_multi": (
        "Seleccion multiple",
        "Varias opciones y mas de una correcta; marque todas las que apliquen.",
    ),
    "codigo": (
        "Codigo ejecutable",
        "Editor de codigo dentro de la plataforma. El codigo se ejecuta ahi mismo: "
        "corralo y revise la salida antes de enviar.",
    ),
    "codigo_zip": (
        "Proyecto en ZIP",
        "Se sube un .zip con los archivos fuente del proyecto.",
    ),
    "java_gui": (
        "Interfaz grafica Java",
        "Editor de codigo con ejecucion de la ventana Java en el navegador: "
        "vera su interfaz funcionando sin instalar nada.",
    ),
    "python_gui": (
        "Interfaz grafica Python",
        "Editor con ejecucion de la ventana Python en el navegador.",
    ),
    "diagrama": (
        "Diagrama (Mermaid)",
        "El diagrama se escribe como texto en sintaxis Mermaid y la plataforma lo "
        "dibuja al instante. No hay que exportar imagenes ni salir a otra herramienta.",
    ),
    "bd_sql": (
        "SQL sobre PostgreSQL real",
        "Editor de SQL con una base PostgreSQL de verdad corriendo en el navegador. "
        "El esquema y los datos de partida ya vienen cargados: usted escribe y ejecuta "
        "su SQL y se guarda tanto la consulta como lo que devolvio la base.",
    ),
    "red_consola": (
        "Consola de red",
        "Consola del simulador de red para ejecutar comandos de diagnostico.",
    ),
    "red_gui": (
        "Topologia de red",
        "Editor visual para armar la topologia de red.",
    ),
    "so_consola": (
        "Consola Linux",
        "Terminal Linux real en el navegador. Nota: esa maquina no tiene red ni Docker.",
    ),
}


def _tipo(nombre):
    return TIPOS.get(nombre, (nombre, ""))


def total_puntos(taller):
    return sum(int(p.get("puntos", 0)) for p in taller.get("preguntas", []))


def bloque_estudiante(taller):
    """Lineas para el .docx del taller: que va a resolver en ExamLab.

    Devuelve una lista de tuplas (estilo, texto), donde estilo es:
      'h'    encabezado de la seccion
      'p'    parrafo normal
      'b'    parrafo con la primera parte en negrita (marcador @@)
      'li'   item de lista
    """
    out = [("h", "Que vas a resolver en ExamLab")]
    if taller.get("resumen"):
        out.append(("p", taller["resumen"]))
    out.append((
        "p",
        f"El taller se resuelve y se entrega en ExamLab ({EXAMLAB_URL}), en el modulo "
        f"Talleres. Son {len(taller.get('preguntas', []))} preguntas y suman "
        f"{total_puntos(taller)} puntos. Lo que sigue es lo que vas a encontrar en cada "
        "una, para que sepas de antemano en que forma se responde:",
    ))
    for i, p in enumerate(taller.get("preguntas", []), 1):
        etiqueta, comose = _tipo(p["tipo"])
        out.append((
            "b",
            f"@@Pregunta {i} - {etiqueta} ({p.get('puntos', 0)} pts):@@ "
            f"{p.get('titulo_corto') or _primera_frase(p['enunciado'])}",
        ))
        out.append(("li", comose))
    out.append((
        "p",
        "Cada pregunta trae su propio enunciado completo dentro de la plataforma: "
        "puedes resolver el taller leyendo solo ExamLab. Este documento sirve para "
        "prepararte y conservar tus respuestas. La actividad es individual; si el "
        "docente autoriza trabajo en equipo, la entrega en ExamLab sigue siendo individual.",
    ))
    return out


def render_estudiante(doc, taller, *, para, bullets, add_inline, color_titulo,
                      size_titulo=12, titulo=None):
    """Escribe el bloque «Que vas a resolver en ExamLab» en el .docx del taller.

    Recibe los helpers del builder que llama (`para`, `bullets`, `add_inline_docx`)
    porque los cuatro cursos comparten la firma pero no el modulo. Asi el texto se
    define una sola vez aqui y cada curso lo pinta con su propio estilo.

    `titulo` permite que el curso numere la seccion segun su propio indice
    (ej. «9. Que vas a resolver en ExamLab») sin duplicar el encabezado.
    """
    for estilo, texto in bloque_estudiante(taller):
        if estilo == "h":
            para(doc, titulo or texto, size=size_titulo, bold=True, color=color_titulo)
        elif estilo == "b":
            p = doc.add_paragraph()
            add_inline(p, texto)
        elif estilo == "li":
            bullets(doc, [texto])
        else:
            para(doc, texto)


def _primera_frase(texto, tope=150):
    """Resumen de una linea del enunciado, para el indice del estudiante.

    Los enunciados abren con un encabezado markdown numerado
    (`## 3. Medir el plan con EXPLAIN ANALYZE`). Ese titulo es justo el resumen que
    se quiere, asi que se usa tal cual quitandole el `##` y el numero; recortar por
    la primera frase daria «## 3.», que no dice nada.
    """
    lineas = [l.strip() for l in str(texto).splitlines() if l.strip()]
    if lineas and lineas[0].lstrip().startswith("#"):
        titulo = lineas[0].lstrip("#").strip()
        titulo = re.sub(r"^\d+[.)]\s*", "", titulo)  # «3. » al inicio
        if len(titulo) >= 12:
            return titulo.rstrip(".") + "."
        lineas = lineas[1:]

    t = " ".join(" ".join(lineas).split())
    t = re.sub(r"[*`_]", "", t)  # markdown inline: no aporta en el indice
    for corte in (". ", "; "):
        if corte in t[:tope + 40]:
            t = t.split(corte, 1)[0]
            break
    if len(t) > tope:
        t = t[:tope].rsplit(" ", 1)[0] + "..."
    return t.rstrip(".") + "."


def guia_docente_md(n, taller, curso, hito=None, entregable=None):
    """Documento del Kit docente para armar este taller en ExamLab."""
    preguntas = taller.get("preguntas", [])
    L = [
        f"# Taller de la Clase {n} en ExamLab - configuracion",
        "",
        f"- **Curso:** {curso}",
        f"- **Taller:** {taller.get('titulo', f'Clase {n}')}",
        f"- **Preguntas:** {len(preguntas)} · **Total:** {total_puntos(taller)} puntos",
        f"- **Plataforma:** ExamLab ({EXAMLAB_URL}) · modulo Talleres",
    ]
    if hito:
        L.append(f"- **Hito del PI:** {hito}")
    if entregable:
        L.append(f"- **Entregable de la clase:** {entregable}")
    L += [
        "",
        "> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del",
        "> docente (o con la pestana de IA). Este documento trae el texto exacto de cada",
        "> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.",
        "",
    ]
    if taller.get("resumen"):
        L += [f"**Que produce el estudiante:** {taller['resumen']}", ""]
    L += ["---", ""]

    for i, p in enumerate(preguntas, 1):
        etiqueta, _ = _tipo(p["tipo"])
        L += [
            f"## Pregunta {i} - {etiqueta} · {p.get('puntos', 0)} pts",
            "",
            f"**Tipo en la plataforma:** `{p['tipo']}`",
            "",
            "**Enunciado (campo Contenido):**",
            "",
            p["enunciado"].strip(),
            "",
        ]
        if p.get("opciones"):
            L += ["**Opciones:**", ""]
            correctas = set(p.get("correctas", []))
            for j, o in enumerate(p["opciones"]):
                marca = "x" if j in correctas else " "
                L.append(f"- [{marca}] {o}")
            L.append("")
        if p.get("lenguaje"):
            L += [f"**Lenguaje:** `{p['lenguaje']}`", ""]
        if p.get("gui"):
            L += [f"**Tipo de GUI:** `{p['gui']}`", ""]
        if p.get("starter"):
            L += ["**Codigo de partida (starter):**", "", "```" + (p.get("lenguaje") or "java"),
                  p["starter"].rstrip(), "```", ""]
        if p.get("setup_sql"):
            L += [
                "**SQL de partida (`options.db.setupSql`)** - corre antes del SQL del",
                "estudiante, sobre una base limpia. PostgreSQL, no Oracle:",
                "", "```sql", p["setup_sql"].rstrip(), "```", "",
            ]
        if p.get("mermaid_esperado"):
            L += ["**Diagrama de referencia (Mermaid):**", "", "```mermaid",
                  p["mermaid_esperado"].rstrip(), "```", ""]
        if p.get("rubrica"):
            L += ["**Rubrica esperada (campo Rubrica):**", "", p["rubrica"].strip(), ""]
        L += ["---", ""]

    L += [
        "## Al terminar de crearlo",
        "",
        "- Verifique que la suma de puntos sea la esperada: "
        f"**{total_puntos(taller)}**.",
        "- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).",
        "- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,",
        "  para confirmar que el SQL de partida corre y que el starter compila.",
        "",
    ]
    return "\n".join(L)
