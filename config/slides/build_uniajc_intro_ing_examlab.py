# -*- coding: utf-8 -*-
"""Genera las DOS evaluaciones de corte de Introduccion a la Ingenieria (FI300101).

Produce, por cada corte evaluado (sesiones 6 y 11), tres documentos con destinos
distintos porque tienen lectores distintos:

  Kit docente/Clase N/
    ExamLab Corte X - Configuracion.md / .docx   -> para ARMAR las preguntas en ExamLab
    ExamLab Corte X - CLAVE DOCENTE.md / .docx   -> para CALIFICAR las abiertas
    Evaluacion Corte X - Como prepararse.md      -> fuente del documento del estudiante
  Clases/Clase N - <slug>/
    Evaluacion Corte X - Como prepararse.docx    -> el que se le entrega al estudiante

La CLAVE se queda SOLO en el Kit docente y nunca se copia a `Clases/`, que es la carpeta
que se comparte. Es la unica razon por la que este builder no usa `_escribir(..., docx=True)`
para todo y escribe el docx del estudiante a mano en la otra carpeta: el destino del
archivo es parte de su seguridad.

Por que un builder aparte y no dentro de `build_uniajc_intro_ing_clases.py`: ese recorre
las 16 sesiones y produce deck + guion + taller de cada una. Las evaluaciones son dos, no
dieciseis, y se regeneran por su cuenta cuando se ajusta una pregunta. Meterlas ahi
obligaba a un `if n in (6, 11)` en medio del bucle y a regenerar 16 decks para cambiar una
rubrica.

Uso:
    python build_uniajc_intro_ing_examlab.py          # las dos
    python build_uniajc_intro_ing_examlab.py 6        # solo el corte 1
"""

import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from guion_md_a_docx import convert  # noqa: E402
import examlab_talleres as X  # noqa: E402
import intro_ing_datos as D  # noqa: E402
import intro_ing_examlab_data as ED  # noqa: E402
import intro_ing_temas_data as TD  # noqa: E402

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CURSO = os.path.join(ROOT, D.curso()["folder"])


# --------------------------------------------------------------------------- rutas
def _dirs(n):
    """Las mismas dos carpetas que usa el builder de clases, con el mismo slug."""
    dir_clase = os.path.join(CURSO, "Clases", "Clase %d - %s" % (n, D.tema(n)["slug"]))
    dir_kit = os.path.join(CURSO, "Kit docente", "Clase %d" % n)
    return dir_clase, dir_kit


def _corte_json(n):
    """El corte del JSON del curso que cierra en la sesion n.

    Se busca por `cierra_en_sesion` y no por rango, porque lo que interesa es el corte
    que esta evaluacion cierra. Sirve tambien de comprobacion: si alguien mueve la
    evaluacion a una sesion que no cierra corte, esto falla en vez de generar un
    documento que anuncia un peso que no existe.
    """
    for c in D.cortes():
        if c["cierra_en_sesion"] == n:
            return c
    raise SystemExit(
        "La sesion %d no cierra ningun corte en el JSON del curso: una evaluacion de "
        "corte no puede caer ahi." % n
    )


def _peso(corte_json):
    """El porcentaje que pesa la evaluacion escrita, leido del desglose del JSON.

    El desglose trae lineas como «Evaluación de corte (sesión 6) · 10%». El peso se lee
    de ahi y no se escribe a mano, porque si el Acuerdo cambia el reparto tiene que
    cambiar en un solo lugar.
    """
    for linea in corte_json.get("desglose", []):
        if "valuaci" in linea and "·" in linea:
            return linea.rsplit("·", 1)[1].strip()
    raise SystemExit(
        "El corte %d no declara el peso de su evaluacion en `desglose`: %r"
        % (corte_json["corte"], corte_json.get("desglose"))
    )


def _fechas(n):
    """`SB141B jueves 08/10/2026 · SB141C martes 06/10/2026 · ...`

    Los tres grupos hacen la misma evaluacion en fechas distintas, y dos de ellos el
    mismo dia. El docente necesita las tres fechas juntas para saber cuando abrir y
    cuando cerrar la actividad en la plataforma.
    """
    partes = []
    for g in D.grupos():
        f = D.fecha_de_sesion(g["grupo"], n)
        partes.append("**%s** %s %s (%s)" % (
            g["grupo"], g["dia"].lower(), D.ddmmyyyy(f) if f else "sin fecha",
            g["horario"].replace(" - ", "–"),
        ))
    return " · ".join(partes)


def _reparto(ev):
    """`6 cerradas (52 pts) y 4 abiertas (48 pts)` — se calcula, no se escribe."""
    cerradas = [p for p in ev["preguntas"] if p["tipo"].startswith("cerrada")]
    abiertas = [p for p in ev["preguntas"] if p["tipo"] == "abierta"]
    return "%d cerradas (%d pts) y %d abiertas (%d pts)" % (
        len(cerradas), sum(p["puntos"] for p in cerradas),
        len(abiertas), sum(p["puntos"] for p in abiertas),
    )


# ------------------------------------------------------------------ configuracion
def md_configuracion(n):
    """El documento con el que el docente crea las preguntas en ExamLab.

    El cuerpo (una seccion por pregunta, con enunciado, opciones marcadas y rubrica) lo
    arma `examlab_talleres.guia_docente_md`, que es el mismo renderizador de los cuatro
    cursos que ya usan ExamLab. Aqui solo se le pasa lo que distingue a una evaluacion
    de corte de un taller: que dura 20 min, que es individual, que se aplica dentro de
    la sesion y que su cierre no es «publique y espere al domingo».
    """
    ev = ED.EVALUACIONES[n]
    cj = _corte_json(n)
    libro = ("**Sí**, sobre los documentos del propio equipo (no internet)"
             if ev["libro_abierto"] else "No. Se responde sin consultar material")

    guia = X.guia_docente_md(
        n, ev, "%s (%s)" % (D.curso()["nombre_acentos"], D.curso()["codigo"]),
        kind="Evaluación de corte",
        modulo="Evaluaciones",
        resumen_etiqueta="Qué se evalúa",
        nota_import=[
            "> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del",
            "> docente (o con la pestaña de IA). Este documento trae el texto exacto de",
            "> cada campo para copiar y pegar, con las opciones correctas ya marcadas.",
        ],
        meta_extra=[
            ("Corte", "%d de 3 · el corte vale %s del curso" % (cj["corte"], cj["pct"])),
            ("Peso de esta evaluación", "%s de la nota final del curso" % _peso(cj)),
            ("Cubre", "las sesiones %s" % ev["cubre"]),
            ("Cuándo", ev["cierre"]),
            ("Duración", "%d minutos, cronometrados" % ev["minutos"]),
            ("Modalidad", "Individual · dentro de la sesión sincrónica"),
            ("Libro abierto", libro),
            ("Reparto", _reparto(ev)),
            ("Fechas por grupo", _fechas(n)),
        ],
        cierre_lineas=[
            "- Abra la actividad **al empezar la sesión**, no antes: el enunciado de las",
            "  abiertas revela qué se va a preguntar y esta evaluación se responde en vivo.",
            "- Configure el cierre a los **%d minutos**. Si la plataforma no permite"
            % ev["minutos"],
            "  cronómetro, avise el minuto de cierre en voz alta y cierre usted la actividad.",
            "- Pegue el enlace **en el chat de Meet**, nunca en la diapositiva: ExamLab no es",
            "  plataforma oficial de la UNIAJC y el enlace no debe quedar en material publicado.",
            "- Recuerde en voz alta que es individual, y (si aplica) qué se puede consultar.",
            "- **Si ExamLab falla:** no se pierde la evaluación. Se reprograma dentro de la",
            "  misma semana y se avisa por el canal del curso. Está previsto en el plan B del",
            "  curso; no improvise una evaluación en papel en una sesión virtual.",
            "- Al cerrar, exporte los resultados antes de terminar la sesión: es la evidencia",
            "  del corte y en modalidad virtual no hay hoja que recoger.",
        ],
    )

    # El «por que asi» va al final y no en la cabecera: es la justificacion del diseno,
    # util cuando alguien (incluido el docente de la proxima cohorte) se pregunte por que
    # una evaluacion es a libro abierto y la otra no. No hace falta leerlo para armarla.
    return guia + "\n".join([
        "## Por qué esta evaluación está diseñada así",
        "",
        ev["por_que_asi"],
        "",
        "> Solo hay **dos** evaluaciones escritas en el curso, esta y la de la otra sesión "
        "de cierre. El corte 3 no tiene evaluación escrita: se evalúa con la exposición "
        "final, el informe final y la asistencia. No es una omisión.",
        "",
    ])


# ------------------------------------------------------------------- clave docente
def md_clave(n):
    """La clave: respuesta modelo, rubrica y error comun de cada pregunta.

    Existe aparte de la configuracion porque se usa en otro momento y con otro criterio:
    la configuracion se lee UNA vez, al armar la actividad; la clave se lee mientras se
    califica, buscando una pregunta concreta. Y porque este archivo no se comparte nunca.
    """
    ev = ED.EVALUACIONES[n]
    cj = _corte_json(n)
    abiertas = [p for p in ev["preguntas"] if p["tipo"] == "abierta"]

    L = [
        "# CLAVE DOCENTE · Evaluación del Corte %d (sesión %d)" % (cj["corte"], n),
        "",
        "> **Documento interno.** No va en `Clases/` ni se comparte con el grupo. Contiene "
        "las respuestas y las bandas de calificación.",
        "",
        "- **Curso:** %s (%s)" % (D.curso()["nombre_acentos"], D.curso()["codigo"]),
        "- **Cubre:** las sesiones %s · **Total:** %d puntos" % (
            ev["cubre"], X.total_puntos(ev)),
        "- **Peso:** %s de la nota final del curso" % _peso(cj),
        "- **Reparto:** %s" % _reparto(ev),
        "",
        "Las **%d cerradas** las califica la plataforma. Lo que exige tiempo del docente son "
        "las **%d abiertas** (%d puntos, el %d %% de la evaluación): esta clave existe para "
        "que esas se califiquen con el mismo criterio en los tres grupos." % (
            len(ev["preguntas"]) - len(abiertas), len(abiertas),
            sum(p["puntos"] for p in abiertas),
            round(100 * sum(p["puntos"] for p in abiertas) / X.total_puntos(ev)),
        ),
        "",
        "---",
        "",
    ]

    for i, p in enumerate(ev["preguntas"], 1):
        etiqueta, _ = X._tipo(p["tipo"])
        L += [
            "## Pregunta %d · %s · %d pts · sale de la sesión %d" % (
                i, etiqueta, p["puntos"], p["sesion"]),
            "",
        ]
        if p["tipo"] == "abierta":
            # En las abiertas va el enunciado COMPLETO: la rubrica reparte puntos por
            # cada cosa que el enunciado pidio, y calificar con solo el titulo obliga a
            # tener el documento de configuracion abierto al lado. Las cerradas no lo
            # necesitan: las califica la plataforma y aqui basta el titulo y la marca.
            cuerpo = p["enunciado"].strip().splitlines()
            if cuerpo and cuerpo[0].lstrip().startswith("#"):
                cuerpo = cuerpo[1:]
            while cuerpo and not cuerpo[0].strip():  # la línea en blanco tras el título
                cuerpo = cuerpo[1:]
            L += ["**%s**" % X._primera_frase(p["enunciado"]).rstrip("."), "",
                  "**Lo que dice el enunciado:**", ""]
            L += ["> " + l if l.strip() else ">" for l in cuerpo]
            L += [""]
        else:
            L += ["**%s**" % X._primera_frase(p["enunciado"]).rstrip("."), ""]
        if p.get("opciones"):
            correctas = set(p["correctas"])
            L += ["**Opciones y respuesta:**", ""]
            for j, o in enumerate(p["opciones"]):
                L.append("- [%s] %s" % ("x" if j in correctas else " ", o))
            L.append("")
        L += [
            "**Respuesta modelo:**",
            "",
            p["respuesta_modelo"].strip(),
            "",
            "**Cómo se califica:**",
            "",
            p["rubrica"].strip(),
            "",
            "**Error común (y qué significa si aparece mucho):**",
            "",
            p["error_comun"].strip(),
            "",
            "---",
            "",
        ]

    L += [
        "## Al terminar de calificar",
        "",
        "- Cuente en cuántas de las cerradas falló más de la mitad del grupo. Cada una está "
        "amarrada a una sesión: eso dice qué sesión hay que retomar, y conviene retomarla en "
        "la siguiente aunque el corte ya esté cerrado.",
        "- Los errores comunes de arriba no son adorno: si el error común es la respuesta "
        "mayoritaria, el problema fue la explicación en clase, no el grupo.",
        "- Las abiertas se califican con la rúbrica y no por impresión general. Si dos "
        "respuestas parecidas reciben notas distintas, el criterio que falló es el suyo.",
    ]
    if ev["libro_abierto"]:
        L += [
            "- Esta evaluación es a libro abierto sobre los documentos del equipo. Un "
            "estudiante que no pudo responder las preguntas que piden copiar del documento "
            "está diciendo que su equipo no documentó: hable con el equipo antes del corte "
            "siguiente, porque el informe final se construye sobre esos mismos documentos.",
        ]
    L += [
        "- Exporte los resultados de la plataforma y guárdelos junto a este documento. Es la "
        "evidencia del corte.",
        "",
    ]
    return "\n".join(L)


# ---------------------------------------------------------------- doc del estudiante
def md_estudiante(n):
    """«Cómo prepararse»: lo que el estudiante recibe con anticipación.

    NO trae el listado de las diez preguntas. Publicar los diez titulos convierte una
    evaluacion de criterio en la memorizacion de diez respuestas, y no es lo que el curso
    quiere medir. Trae el formato (cuantas preguntas, de que tipo, cuanto pesa, cuanto
    dura), la guia de repaso por sesion, y —en el corte 2— exactamente que documentos
    tener abiertos.

    Esta escrito en **usted**, que es el trato de los talleres del curso, y en singular
    porque la evaluacion es individual: el taller dice «Averigüen», esto dice «Abra».
    """
    ev = ED.EVALUACIONES[n]
    cj = _corte_json(n)
    tipos = []
    for p in ev["preguntas"]:
        et = X._tipo(p["tipo"])[0]
        if et not in tipos:
            tipos.append(et)

    L = [
        "# Evaluación del Corte %d · cómo prepararse" % cj["corte"],
        "",
        "**%s** · %s (Ingeniería de Sistemas · UNIAJC)" % (
            D.curso()["nombre_acentos"], D.curso()["codigo"]),
        "",
        "Este documento no es la evaluación: es lo que necesita saber para llegar "
        "preparado. Se entrega con anticipación a propósito.",
        "",
        "## Cuándo y cómo",
        "",
        "- **Cuándo:** %s." % ev["cierre"],
        "- **Cuánto dura:** %d minutos, cronometrados." % ev["minutos"],
        "- **Dónde:** en ExamLab. El enlace se pega en el chat de la reunión al empezar la "
        "evaluación, no antes.",
        "- **Cuántas preguntas:** %d, que suman %d puntos — %s." % (
            len(ev["preguntas"]), X.total_puntos(ev), _reparto(ev)),
        "- **Tipos de pregunta:** %s." % ", ".join(tipos),
        "- **Cuánto vale:** %s de la nota final del curso (el corte %d vale %s)." % (
            _peso(cj), cj["corte"], cj["pct"]),
        "- **Es individual.** El taller de la sesión es en equipo; esta evaluación no.",
    ]
    if ev["libro_abierto"]:
        # Las que piden abrir el documento son las abiertas: se cuentan, no se escriben,
        # porque si se agrega o se quita una pregunta el numero tiene que seguirla.
        abiertas = [p for p in ev["preguntas"] if p["tipo"] == "abierta"]
        L += [
            "- **Es a libro abierto, pero sobre los documentos de su equipo**, no sobre "
            "internet. %d de las %d preguntas piden abrir esos documentos y copiar de ahí "
            "— son %d de los %d puntos. Sin los documentos, esas %d no se pueden "
            "responder." % (len(abiertas), len(ev["preguntas"]),
                            sum(p["puntos"] for p in abiertas),
                            X.total_puntos(ev), len(abiertas)),
            "",
            "> Ténganlos abiertos **antes** de que empiece la evaluación. Buscar un "
            "documento mientras corre el cronómetro cuesta la mitad del tiempo.",
        ]
    else:
        L += [
            "- **No se consulta material.** No es desconfianza: lo que se evalúa son "
            "distinciones que va a usar el resto del semestre, y esas hay que tenerlas "
            "puestas, no buscarlas.",
            "- **No tiene que traer nada**, solo haber repasado. La lista de qué repasar "
            "está más abajo.",
        ]
    L += [
        "- **Si no puede asistir ese día**, avise por el canal del curso **antes** de la "
        "sesión. La reposición se maneja según el Acuerdo pedagógico; avisar después de "
        "que la evaluación cerró es otra conversación y más difícil.",
        "- **Llegar tarde no da más tiempo:** el cronómetro es el mismo para todos y la "
        "evaluación cierra a la misma hora.",
        "",
        "## En qué forma se responde cada tipo",
        "",
    ]
    for t in tipos:
        comose = next(X._tipo(p["tipo"])[1] for p in ev["preguntas"]
                      if X._tipo(p["tipo"])[0] == t)
        L += ["- **%s.** %s" % (t, comose)]
    L += [
        "",
        "Las abiertas piden respuestas **cortas**: dos, tres o cuatro líneas, y cada una "
        "dice cuántas. Una respuesta larga que no contesta lo que se preguntó no puntúa más "
        "que una corta que sí. Con %d minutos para %d preguntas, escribir de más es lo que "
        "hace que la última quede en blanco." % (ev["minutos"], len(ev["preguntas"])),
        "",
        "## Qué repasar, sesión por sesión",
        "",
        "Todas las sesiones del corte entran. Esta lista está en orden y es completa: si "
        "repasa esto, puede responder la evaluación.",
        "",
    ]
    for r in ev["repaso"]:
        L += ["### Sesión %d · %s" % (r["sesion"], r["tema"]), ""]
        for item in r["revise"]:
            L.append("- %s" % item)
        if r.get("abrir"):
            L += ["", "**Tenga abierto:** %s" % r["abrir"]]
        L.append("")

    if ev["libro_abierto"]:
        # El checklist repite lo que ya dijo el repaso, y eso es a proposito: es la lista
        # que se mira cinco minutos antes, sin volver a leer las cinco secciones. Se
        # recorta a la primera frase de cada `abrir` para que quepa de un vistazo y para
        # no mantener el mismo texto en dos lugares.
        L += [
            "## Antes de empezar: las pestañas que tiene que tener abiertas",
            "",
        ]
        for r in ev["repaso"]:
            if r.get("abrir"):
                L.append("- [ ] %s" % r["abrir"].split(". ")[0].rstrip("."))
        L += [
            "",
            "Si su equipo no tiene alguno de esos documentos, **dígalo en la respuesta**. "
            "Declarar que falta cuesta menos puntos que inventarlo, y un dato inventado en "
            "una ficha de antecedentes es un problema distinto y más grave.",
            "",
        ]

    L += [
        "## Dos cosas más",
        "",
        "- **ExamLab no es una plataforma oficial de la UNIAJC.** Es un canal del docente y "
        "se usa solo para esto. No pide datos personales suyos más allá de su nombre.",
        "- **Si la plataforma falla**, la evaluación no se pierde ni se da por perdida: se "
        "reprograma dentro de la misma semana y se avisa por el canal del curso. No la "
        "responda dos veces ni escriba a otro lado; espere el aviso.",
        "",
    ]
    return "\n".join(L)


# --------------------------------------------------------------------------- salida
def _md(carpeta, nombre, texto, docx=True):
    os.makedirs(carpeta, exist_ok=True)
    ruta = os.path.join(carpeta, nombre + ".md")
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto)
    hechos = [ruta]
    if docx:
        dx = os.path.join(carpeta, nombre + ".docx")
        convert(ruta, dx)
        hechos.append(dx)
    return hechos


# ───────────────────────────────────────── talleres de equipo en ExamLab (16 sesiones)
#
# Por que se GENERA y no se escribe: cada sesion ya tiene los tres pedazos alineados uno a
# uno en `intro_ing_temas_data` — `taller["bloques"]` (que se pide), `rubrica` (que vale) y
# `solucion["bloques"]` (la respuesta modelo)—, con las mismas claves y en el mismo orden.
# Escribir a mano 80 preguntas a partir de eso era garantizar que se desincronizaran: se
# cambia un bloque del taller y la pregunta de la plataforma queda pidiendo otra cosa. Asi
# el taller que recibe el estudiante, la solucion del docente y la actividad de ExamLab
# salen de la MISMA fuente y no pueden discrepar.
#
# Los cinco bloques dan exactamente las 5 preguntas que ExamLab admite como maximo, y la
# rubrica ya suma 100 puntos, que es el total que pide la propuesta del curso.


def _partes_taller(n):
    """`(taller, rubrica, bloques_solucion)` de la sesion `n`, de donde vivan.

    La Clase 1 no esta en `TEMAS`: su actividad y su solucion viven en
    `intro_ing_clase1_data`, porque esa sesion lleva ademas la prueba diagnostica.
    """
    if n == 1:
        import intro_ing_clase1_data as C1
        sol = getattr(C1, "SOLUCION", None) or {}
        return C1.ACTIVIDAD, C1.RUBRICA, sol.get("bloques") or []
    tema = TD.TEMAS[n]
    return tema["taller"], tema["rubrica"], tema["solucion"]["bloques"]


def taller_examlab(n):
    """Especificacion del taller de la sesion `n` para `examlab_talleres`.

    Una pregunta `abierta` por bloque. Todas abiertas a proposito: el entregable de este
    curso es criterio redactado —una frase de problema, una cifra con su metodo, una razon—
    y no hay forma de calificar eso con opciones. Tampoco se usa el tipo `diagrama`, que
    espera codigo Mermaid: los diagramas de este curso se dibujan en Excalidraw o draw.io y
    Mermaid no se enseña en ninguna sesion, asi que pedirlo evaluaria algo no enseñado. En
    los bloques de diagrama se pide el enlace del dibujo MAS los elementos que la rubrica
    revisa, que es lo que de verdad se califica.
    """
    taller, rubrica, sol = _partes_taller(n)
    bloques = taller["bloques"]
    if not (len(bloques) == len(rubrica) == len(sol)):
        raise SystemExit(
            "Sesion %d: el taller tiene %d bloques, la rubrica %d items y la solucion %d. "
            "Los tres tienen que ir uno a uno: la pregunta k de ExamLab es el bloque k."
            % (n, len(bloques), len(rubrica), len(sol)))
    claves_b = [b["clave"] for b in bloques]
    claves_s = [b["clave"] for b in sol]
    if claves_b != claves_s:
        raise SystemExit(
            "Sesion %d: los bloques del taller y los de la solucion no van en el mismo "
            "orden.\n  taller:   %s\n  solucion: %s" % (n, claves_b, claves_s))

    preguntas = []
    for i, (bl, item) in enumerate(zip(bloques, rubrica), 1):
        criterio, puntos = item[0], item[1]
        enunciado = ["## %d. %s" % (i, bl["clave"]), "", bl["pide"]]
        if bl.get("check"):
            enunciado += ["", "**Se revisa que** " + bl["check"]]
        preguntas.append({
            "tipo": "abierta",
            "puntos": puntos,
            "enunciado": "\n".join(enunciado),
            # La rubrica de la plataforma junta las dos vistas que ya existian: el criterio
            # con el que se reparten los puntos y la comprobacion concreta del bloque.
            "rubrica": "%s (%d pts).\n\nComprobacion: %s" % (criterio, puntos,
                                                             bl.get("check") or "—"),
        })
    return {
        "titulo": "%s — %s" % (taller["titulo"], D.tema(n)["tema_acentos"]),
        "resumen": taller.get("consigna", ""),
        "preguntas": preguntas,
    }


def md_taller(n):
    """Documento del Kit docente para montar el taller de la sesion `n` en ExamLab."""
    taller_datos, _, _ = _partes_taller(n)
    t = taller_examlab(n)
    curso = "%s (%s)" % (D.curso()["nombre_acentos"], D.curso()["codigo"])
    md = X.guia_docente_md(
        n, t, curso,
        entregable=taller_datos.get("entregable", ""),
        resumen_etiqueta="Consigna del equipo",
        nota_import=[
            "> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del",
            "> docente. Este documento trae el texto exacto de cada campo para copiar y pegar.",
            "> Las cinco preguntas son los cinco bloques de la ficha, en el mismo orden y con",
            "> los mismos puntos que la rubrica del taller.",
        ],
        meta_extra=[
            ("Trabajo", "en equipo (%d min en salas de grupo) · **la entrega en ExamLab es "
                        "individual**: cada integrante pega lo que su equipo acordo"
             % taller_datos.get("min", 17)),
            ("Exposicion", "%d min por equipo, habla el vocero"
             % taller_datos.get("exposicion", 3)),
            ("Fechas por grupo", _fechas(n)),
        ],
        cierre_lineas=[
            "- Publique el taller **al empezar** la actividad en equipos, no antes: los cinco",
            "  bloques son la guia de la sesion y adelantarlos vacia el trabajo de la sala.",
            "- **Cierre al terminar la sesion.** Este curso califica esto como «actividades en",
            "  clase» dentro del corte, no como tarea con plazo: el trabajo se hace en la sala",
            "  de grupo y se expone el mismo dia. Si decide dar margen a un equipo que se quedo",
            "  corto, digalo en voz alta y aplique el mismo margen a los cinco.",
            "- Al calificar, la respuesta modelo de cada bloque esta en «Solucion Taller",
            "  Clase %d», con su reparto de puntos bloque por bloque." % n,
        ],
    )
    return md


def build_taller(n):
    _, dir_kit = _dirs(n)
    t = taller_examlab(n)
    hechos = _md(dir_kit, "Taller en ExamLab - Clase %d (configuracion)" % n,
                 md_taller(n), docx=False)
    print("Taller sesión %2d · %d preguntas · %d puntos · %s" % (
        n, len(t["preguntas"]), X.total_puntos(t),
        "/".join(str(p["puntos"]) for p in t["preguntas"])))
    for h in hechos:
        print("   " + os.path.relpath(h, ROOT))
    return hechos


def build_evaluacion(n):
    ev = ED.EVALUACIONES[n]
    cj = _corte_json(n)
    dir_clase, dir_kit = _dirs(n)
    hechos = []

    # Kit docente: configuracion y clave. La clave NO sale de aqui.
    hechos += _md(dir_kit, "ExamLab Corte %d - Configuracion" % cj["corte"],
                  md_configuracion(n))
    hechos += _md(dir_kit, "ExamLab Corte %d - CLAVE DOCENTE" % cj["corte"],
                  md_clave(n))

    # Estudiante: el .md fuente vive en el Kit y el .docx que se entrega va a Clases/,
    # igual que los talleres del curso.
    nombre_est = "Evaluacion Corte %d - Como prepararse" % cj["corte"]
    hechos += _md(dir_kit, nombre_est, md_estudiante(n), docx=False)
    os.makedirs(dir_clase, exist_ok=True)
    dx = os.path.join(dir_clase, nombre_est + ".docx")
    convert(os.path.join(dir_kit, nombre_est + ".md"), dx)
    hechos.append(dx)

    print("Corte %d · sesión %d · %d preguntas · %d puntos · %s" % (
        cj["corte"], n, len(ev["preguntas"]), X.total_puntos(ev), _reparto(ev)))
    for h in hechos:
        print("   " + os.path.relpath(h, ROOT))
    return hechos


def build(ns=None):
    """Todo lo que va a ExamLab: los 16 talleres de equipo y las 2 evaluaciones de corte.

    `ns` limita a unas sesiones concretas. Sin argumentos hace el curso completo, que es lo
    que hay que correr antes de montar la plataforma.
    """
    sesiones = ns or list(range(1, D.curso()["n_sesiones"] + 1))
    todo = []
    print("== Talleres de equipo (uno por sesión)")
    for n in sesiones:
        todo += build_taller(n)
    cortes = [n for n in sesiones if n in ED.EVALUACIONES]
    if cortes:
        print("\n== Evaluaciones de corte")
        for n in cortes:
            todo += build_evaluacion(n)
    print("\n%d archivos." % len(todo))
    return todo


if __name__ == "__main__":
    build([int(a) for a in sys.argv[1:]] or None)
