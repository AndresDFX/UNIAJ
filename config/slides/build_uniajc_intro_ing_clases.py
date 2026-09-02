# -*- coding: utf-8 -*-
"""Clases 2 a 16 de Introduccion a la Ingenieria (FI300101) · 2026-2.

**Material general para los tres grupos.** No lleva fechas, ni reloj de pared, ni codigo de
grupo: SB141B, SB141C y LB141F dictan la misma clase con el mismo material. Lo que cambia
por grupo esta en el deck de Presentacion del Curso y en el CALENDARIO del grupo.

La Clase 1 tiene su propio builder (`build_uniajc_intro_ing_clase1.py`) porque es la unica
que reparte los 45 min de teoria entre encuadre del curso y evaluacion diagnostica. De la 2
en adelante todas tienen la misma forma, asi que se generan desde un unico builder que lee
el contenido de `intro_ing_temas_data.py`.

Por clase N genera:

    Clases/Clase N - <slug>/
        Presentacion.pptx
        Taller Clase N - <nombre>.docx           (version estudiante)
    Kit docente/Clase N/
        Guion Docente Clase N - <slug>.md / .docx
        Solucion Taller Clase N - <nombre>.md / .docx
        Taller Clase N - <nombre>.md             (fuente del .docx del estudiante)
        Capturas/README.txt

Los ``{{slide:...}}`` del guion se resuelven contra los titulos REALES del deck, que se van
recogiendo mientras se construye. No hay mapa de diapositivas escrito a mano que se pueda
desincronizar.

Uso:
    python build_uniajc_intro_ing_clases.py          # todas
    python build_uniajc_intro_ing_clases.py 2 3 4    # solo esas
"""
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from uniajc_slides_engine import (  # noqa: E402
    new_prs, class_cover, content_slide, block_timeline_slide, hook_slide,
    before_after_slide, cards_grid_slide, steps_visual_slide, checklist_slide,
    box_note_slide, closing_slide, table_content, two_column_slide,
    diagram_boxes_slide,
)
from guion_md_a_docx import convert  # noqa: E402
import intro_ing_datos as D  # noqa: E402
import intro_ing_temas_data as TD  # noqa: E402
import examlab_talleres  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CURSO = os.path.join(ROOT, D.curso()["folder"])
LETRAS = "abcdefghij"

README_CAPT = """Capturas de la Clase %d - %s

Aqui van las imagenes que el guion pide con el marcador [[captura: nombre.png | receta: ...]].
El convertidor a .docx las inserta si existen; si no, deja el marcador visible para que se
note que falta. No borre el marcador del .md: es el que documenta que hace falta la imagen.

Nombres esperados en esta clase:
%s
"""


# ------------------------------------------------------- resolucion de {{slide:}}

_SLIDE_TOKEN = re.compile(r"\{\{\s*slide:\s*([^}]+?)\s*\}\}")


def _plano(s):
    """Minusculas sin tildes, para comparar fragmentos con titulos reales."""
    s = unicodedata.normalize("NFD", str(s))
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


def _slide_no(titulos, frag, n):
    """Numero de la diapositiva cuyo titulo contiene ``frag``. Unico o falla."""
    fp = _plano(frag)
    hits = [i for i, t in enumerate(titulos, 1)
            if not _plano(t).startswith("portada") and fp in _plano(t)]
    if len(hits) == 1:
        return hits[0]
    raise SystemExit(
        "Clase %d: el fragmento {{slide:%s}} coincide con %d diapositivas.\n"
        "Titulos reales del deck:\n%s"
        % (n, frag, len(hits),
           "\n".join("  %2d %s" % (i, t) for i, t in enumerate(titulos, 1)))
    )


def _etiqueta_slides(titulos, campo, n):
    """`{{slide:a}} {{slide:b}}` -> 'diapositivas 7 y 8'."""
    ns = [_slide_no(titulos, m.group(1), n) for m in _SLIDE_TOKEN.finditer(campo)]
    if not ns:
        raise SystemExit("Clase %d: bloque de fundamento sin {{slide:}}: %r" % (n, campo))
    if len(ns) == 1:
        return "diapositiva %d" % ns[0]
    return "diapositivas %s y %d" % (", ".join(str(x) for x in ns[:-1]), ns[-1])


# --------------------------------------------------------------------- rutas

def _slug(n):
    return D.tema(n)["slug"]


def _dirs(n):
    dir_clase = os.path.join(CURSO, "Clases", "Clase %d - %s" % (n, _slug(n)))
    dir_kit = os.path.join(CURSO, "Kit docente", "Clase %d" % n)
    return dir_clase, dir_kit, os.path.join(dir_kit, "Capturas")


def _corte_de(n):
    """El corte al que pertenece la sesion n, leyendo `sesiones: "1-6"` del JSON."""
    for x in D.cortes():
        a, b = (int(v) for v in x["sesiones"].split("-"))
        if a <= n <= b:
            return x
    raise SystemExit("La sesion %d no cae en ningun corte del JSON." % n)


def _nombres(n, t):
    base = "Clase %d - %s" % (n, t["taller"]["archivo"])
    return {
        "taller": "Taller %s" % base,
        "solucion": "Solucion Taller %s" % base,
        "guion": "Guion Docente Clase %d - %s" % (n, _slug(n)),
    }


# --------------------------------------------------------------------- agenda

def _agenda(t):
    """Los cinco bloques del JSON con la etiqueta concreta de esta clase.

    El reloj es RELATIVO (00:00 a 01:30) a proposito: los tres grupos dictan esta misma
    clase a horas distintas y el material es comun. El reloj de pared de cada grupo esta
    en su CALENDARIO.

    Las sesiones 15 y 16 rompen la estructura de cinco bloques (una es la exposicion final y
    la otra el cierre del curso), asi que pueden declarar `agenda_slots` con su propio reparto.
    El builder verifica que siga sumando el bloque completo.
    """
    if t.get("agenda_slots"):
        total = sum(m for _, m, _ in t["agenda_slots"])
        if total != D.curso()["duracion_min"]:
            raise SystemExit("Clase %d: la agenda propia suma %d min, no %d."
                             % (t["n"], total, D.curso()["duracion_min"]))
        slots, acum = [], 0
        for nombre, mins, label in t["agenda_slots"]:
            desde, acum = acum, acum + mins
            slots.append({
                "t": "%02d:%02d–%02d:%02d · %d min"
                     % (desde // 60, desde % 60, acum // 60, acum % 60, mins),
                "label": "%s — %s" % (nombre, label),
            })
        return slots

    etq = t.get("agenda", {})
    slots = []
    for b in D.dinamica()["bloques"]:
        slots.append({
            "t": "%s–%s · %d min" % (b["desde"], b["hasta"], b["min"]),
            "label": etq.get(b["nombre"], b["corto"]),
        })
    return slots


# ---------------------------------------------------------------- diapositivas

def _slide_teoria(prs, spec, idx, t_reg):
    """Emite una diapositiva de teoria segun su `tipo` y registra su titulo."""
    tipo = spec["tipo"]
    tit = t_reg(spec["titulo"])
    if tipo == "content":
        content_slide(prs, tit, spec["items"], sub=spec.get("sub"), idx=idx,
                      )
    elif tipo == "cards":
        cards_grid_slide(prs, tit, spec["cards"], sub=spec.get("sub"),
                         columns=spec.get("columns"), idx=idx)
    elif tipo == "steps":
        steps_visual_slide(prs, tit, spec["steps"], sub=spec.get("sub"), idx=idx)
    elif tipo == "before_after":
        before_after_slide(prs, tit, spec["before_title"], spec["before"],
                           spec["after_title"], spec["after"], sub=spec.get("sub"),
                           idx=idx, size=spec.get("size", 15))
    elif tipo == "box":
        box_note_slide(prs, tit, spec["notas"], idx=idx)
    elif tipo == "tabla":
        table_content(prs, tit, spec["headers"], spec["rows"], note=spec.get("note"),
                      col_w=spec.get("col_w"), fs_body=spec.get("fs_body", 12), idx=idx)
    elif tipo == "dos_columnas":
        two_column_slide(prs, tit, spec["left"], spec["right"],
                         left_title=spec.get("left_title"),
                         right_title=spec.get("right_title"),
                         sub=spec.get("sub"), idx=idx, size=spec.get("size", 14))
    elif tipo == "diagrama":
        diagram_boxes_slide(prs, tit, spec["boxes"], arrows=spec.get("arrows"),
                            sub=spec.get("sub"), idx=idx, note=spec.get("note"),
                            legend=spec.get("legend"))
    else:
        raise SystemExit("Clase: tipo de diapositiva desconocido: %r" % tipo)
    return tit


def build_pptx(n):
    t = TD.TEMAS[n]
    tm = D.tema(n)
    c = D.curso()
    prs = new_prs()
    T = []

    def t_reg(titulo):
        T.append(titulo)
        return titulo

    class_cover(prs, t["titulo"], t["subtitulo"], clase_n=n, idx=1)
    T.append("Portada · Clase %d" % n)

    idx = 2
    block_timeline_slide(
        prs, t_reg("Agenda de hoy (%d min)" % c["duracion_min"]), _agenda(t),
        sub=t.get("agenda_sub",
                  "La misma estructura de las 16 sesiones. El reloj de pared de su grupo "
                  "está en el calendario del curso."),
        idx=idx, nota=t.get("nota_bloque"),
    )
    idx += 1

    content_slide(prs, t_reg("Objetivos de la sesión"), t["objetivos"], idx=idx)
    idx += 1

    hook_slide(prs, t["hook"], t.get("hook_lines"), eyebrow="Pregunta de entrada", idx=idx)
    T.append("Pregunta de entrada")
    idx += 1

    for spec in t["teoria"]:
        _slide_teoria(prs, spec, idx, t_reg)
        idx += 1

    tl = t["taller"]
    checklist_slide(
        prs, t_reg("Taller de hoy: %s" % tl["titulo"]),
        ["**%s** — %s" % (b["clave"], b["pide"]) for b in tl["bloques"]],
        sub="%d min en equipos · %s · %s" % (tl["min"], tl["reparto_corto"], tl["entregable_corto"]),
        idx=idx,
    )
    idx += 1

    steps_visual_slide(
        prs, t_reg("Cómo se expone en %d minutos" % tl["exposicion"]),
        tl["expo"],
        sub="Habla el vocero con la pantalla ya compartida · cronómetro en pantalla · se corta al llegar a cero",
        idx=idx,
    )
    idx += 1

    if n < c["n_sesiones"]:
        sig = D.tema(n + 1)
        content_slide(
            prs, t_reg("Para la sesión %d" % (n + 1)),
            [
                "@@Trabajo dirigido:@@ %s" % t["ti_siguiente"]["tid"],
                "@@Trabajo independiente:@@ %s" % t["ti_siguiente"]["ti"],
                "**Sesión %d · %s** — %s" % (n + 1, sig["tema_acentos"],
                                             t["ti_siguiente"]["adelanto"]),
                "@@Aviso:@@ %s" % t["ti_siguiente"]["aviso"],
                "**Antes de salir:** el enlace del documento del equipo en el chat, con permiso "
                "de lectura para el docente, y el nombre del vocero de hoy.",
            ],
            idx=idx,
        )
    else:
        content_slide(
            prs, t_reg("Cierre del curso"),
            [
                "@@Lo que queda entregado:@@ %s" % t["ti_siguiente"]["tid"],
                "@@Autoevaluación:@@ %s" % t["ti_siguiente"]["ti"],
                "**%s**" % t["ti_siguiente"]["adelanto"],
                "@@Aviso:@@ %s" % t["ti_siguiente"]["aviso"],
            ],
            idx=idx,
        )
    idx += 1

    closing_slide(
        prs,
        t["cierre_titulo"],
        [
            "%s · Clase %d" % (t["titulo"], n),
            "%s · UNIAJC · Ingeniería de Sistemas" % c["codigo"],
        ],
        accent=t["cierre_frase"],
    )
    T.append("Cierre · %s" % t["cierre_titulo"])

    dir_clase, _, _ = _dirs(n)
    os.makedirs(dir_clase, exist_ok=True)
    out = os.path.join(dir_clase, "Presentacion.pptx")
    prs.save(out)
    return out, T


# ----------------------------------------------------------------------- guion

def md_guion(n, titulos):
    t = TD.TEMAS[n]
    tm = D.tema(n)
    c = D.curso()
    tl = t["taller"]
    nom = _nombres(n, t)
    corte = _corte_de(n)

    L = [
        "# Guion docente — Clase %d: %s" % (n, t["titulo"]),
        "",
        "## Información de la clase",
        "- Asignatura: %s (%s)" % (c["nombre_acentos"], c["codigo"]),
        "- Duración del bloque: **%d min**" % c["duracion_min"],
        "- Tipo: Clase virtual sincrónica por Google Meet · Sesión %d de %d · corresponde al "
        "tema %d del microcurrículo" % (n, c["n_sesiones"], n),
        "- Modalidad: **Virtual (síncrona)** por Google Meet · actividades en plataformas "
        "gratuitas en la nube · los 5 equipos trabajan en **salas de grupo**",
        "- Corte **%d** (%s) · RAA: **%s**%s"
        % (corte["corte"], corte["pct"], tm["raa"],
           " · **cierra el corte**" if corte["cierra_en_sesion"] == n else ""),
        "- **Material general para los tres grupos** (SB141B, SB141C, LB141F): sin fechas ni "
        "horarios de reloj. El reloj de pared de cada grupo está en su "
        "`CALENDARIO_2026-2 - <GRUPO>.md`.",
        "- Enfoque: %s · Estrategia: %s" % (c["enfoque"], c["estrategia_didactica"]),
        "",
    ]
    if t.get("nota_bloque"):
        L += ["> %s" % t["nota_bloque"], ""]
    L += ["## Objetivos de la clase"]
    L += ["- %s" % o for o in t["objetivos"]]
    L += [
        "",
        "## Hoy avanzamos el proyecto en…",
        "",
        "**%s**" % t["avance_proyecto"],
        "",
        "**Entregable concreto:** %s" % tl["entregable"],
        "",
        "**Herramientas de esta sesión:** %s" % " · ".join(tm["herramientas"]),
        "",
        "> %s" % t["herramienta_nota"],
        "",
        "## Fundamento teórico para el docente",
        "",
        "Esta sección está escrita para dictar la clase **sin consultar otra fuente**, y va "
        "dividida por diapositiva: cada bloque dice a qué diapositiva corresponde.",
        "",
    ]
    for b in t["fundamento"]:
        L += ["### %s - %s" % (b["titulo"], _etiqueta_slides(titulos, b["slide"], n)), ""]
        L += [p for par in b["cuerpo"] for p in (par, "")]

    L += [
        "## Referencias a diapositivas",
        "Numeración real del deck `Clases/Clase %d - %s/Presentacion.pptx`. Las etiquetas "
        "[Slide N] del plan y las referencias del fundamento apuntan aquí." % (n, _slug(n)),
        "",
    ]
    L += ["%d. %s" % (i, x) for i, x in enumerate(titulos, 1)]
    L += ["", "## Plan de clase minuto a minuto (%d min)" % c["duracion_min"], ""]
    for p in t["plan"]:
        L += ["### %s" % p["titulo"], ""]
        for x in p["cuerpo"]:
            L += [x, ""]

    L += ["## Errores frecuentes y cómo cortarlos en caliente", ""]
    L += ["| Lo que dice el equipo | Por qué no sirve | Qué pedir en su lugar |",
          "|---|---|---|"]
    for e in t["errores"]:
        L.append("| %s | %s | %s |" % (e["dice"], e["por_que"], e["pida"]))
    L.append("")

    if t.get("dudas"):
        L += ["## Dudas frecuentes del estudiante", ""]
        for d in t["dudas"]:
            L += ["**%s**" % d["p"], "", d["r"], ""]

    L += [
        "## Notas operativas",
        "",
    ]
    L += ["- %s" % x for x in t["notas_operativas"]]
    L += [
        "",
        "## Material de esta clase",
        "",
        "- Deck: `Clases/Clase %d - %s/Presentacion.pptx`" % (n, _slug(n)),
        "- Taller del estudiante: `Clases/Clase %d - %s/%s.docx`" % (n, _slug(n), nom["taller"]),
        "- Solución del taller (**solo docente**): `Kit docente/Clase %d/%s.docx`"
        % (n, nom["solucion"]),
        "- Este guion: `Kit docente/Clase %d/%s.docx`" % (n, nom["guion"]),
        "",
        "> **Recordatorio de datos personales:** ninguna actividad de este curso sube nombres, "
        "cédulas, teléfonos ni fotos de terceros. Si el caso del equipo los trae, se usa el rol "
        "(«la dueña de la papelería», «el auxiliar de la biblioteca»).",
        "",
    ]
    return "\n".join(L)


# -------------------------------------------------------------------- solucion

def md_solucion(n):
    t = TD.TEMAS[n]
    tl = t["taller"]
    sol = t["solucion"]
    L = [
        "# Solución del taller — Clase %d: %s" % (n, tl["titulo"]),
        "",
        "> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni compartir pantalla con "
        "él antes de que los equipos trabajen: es la respuesta completa del entregable, y verla "
        "antes convierte el taller en copia.",
        "",
        "## Para qué sirve este documento",
        "",
        sol["para_que"],
        "",
        "## El caso que se resuelve aquí",
        "",
        "**%s**" % sol["caso_titulo"],
        "",
        sol["caso"],
        "",
        "> %s" % sol["por_que_este_caso"],
        "",
        "## Consigna que se les dio",
        "",
        "> %s" % tl["consigna"],
        "",
        "**Entregable:** %s · **%d min de trabajo · %d min de exposición**"
        % (tl["entregable"], tl["min"], tl["exposicion"]),
        "",
        "## Respuesta bloque por bloque",
        "",
    ]
    for i, b in enumerate(sol["bloques"], 1):
        L += [
            "### %d. %s" % (i, b["clave"]),
            "",
            "**Se pedía:** %s" % next(x["pide"] for x in tl["bloques"] if x["clave"] == b["clave"]),
            "",
            "**Respuesta modelo:**",
            "",
            b["respuesta"],
            "",
            "**Cómo calificar:** %s" % b["como_calificar"],
            "",
        ]

    L += ["## Rúbrica del taller", "",
          "| Criterio | Peso | Por qué pesa eso |", "|---|---|---|"]
    for cr, peso, por_que in t["rubrica"]:
        L.append("| %s | **%d %%** | %s |" % (cr, peso, por_que))
    L += ["", "> Suma **%d %%**. La nota es del equipo, no del vocero."
          % sum(p for _, p, _ in t["rubrica"]), ""]

    if sol.get("variantes"):
        L += ["## Si el equipo trabajó otro caso", ""]
        for v in sol["variantes"]:
            L += ["**%s.** %s" % (v["caso"], v["clave"]), ""]

    L += ["## Errores que hay que ver y no dejar pasar", ""]
    for e in t["errores"]:
        L += ["- **%s** → %s %s" % (e["dice"], e["por_que"], e["pida"])]
    L += [""]

    L += ["## Cierre: qué decir en los 3 minutos finales", "", sol["cierre"], ""]
    L += [
        "## Con qué se conecta",
        "",
        sol["conexion"],
        "",
    ]
    return "\n".join(L)


# ---------------------------------------------------------------------- taller

def md_taller(n):
    t = TD.TEMAS[n]
    tl = t["taller"]
    L = [
        "# Taller Clase %d — %s" % (n, tl["titulo"]),
        "",
        "**%s** · %s (%s)" % (D.curso()["nombre_acentos"], D.curso()["codigo"],
                              "Ingeniería de Sistemas · UNIAJC"),
        "",
        "Equipo: ______  ·  Integrantes: ______________________________________________",
        "",
        "Vocero de hoy: ____________________  ·  Enlace del documento: __________________",
        "",
        "## Qué hay que hacer",
        "",
        tl["consigna"],
        "",
        "- **Tiempo de trabajo:** %d min, en la sala de grupo de su equipo." % tl["min"],
        "- **Exposición:** %d min por equipo, habla el vocero con la pantalla ya compartida."
        % tl["exposicion"],
        "- **Entregable:** %s" % tl["entregable"],
        "",
        "> **%s** %s" % (tl["reparto_titulo"], tl["reparto"]),
        "",
        "## Los %d bloques que tiene que llenar" % len(tl["bloques"]),
        "",
    ]
    for i, b in enumerate(tl["bloques"], 1):
        L += [
            "### %d. %s" % (i, b["clave"]),
            "",
            b["pide"],
            "",
            "> **Se revisa que:** %s" % b["check"],
            "",
        ]

    # Donde se entrega. Iba solo el «documento del equipo en Drive», y el taller se califica
    # en ExamLab: el estudiante tenia que adivinar que su trabajo de equipo se entrega otra
    # vez, individualmente, en otra plataforma. La tabla es el corolario de formato: si los
    # cinco bloques se califican con esos pesos, el estudiante ve los cinco con sus pesos.
    tipo_abierta = examlab_talleres.TIPOS["abierta"]
    L += [
        "## Dónde se entrega: en ExamLab",
        "",
        "El taller se **trabaja en equipo** en el documento del equipo y se **entrega en "
        "ExamLab** (%s), en el módulo Talleres. El enlace lo comparte el docente en el chat "
        "de la reunión al empezar la actividad." % examlab_talleres.EXAMLAB_URL,
        "",
        "- Son **%d preguntas**, una por cada bloque de arriba y en el mismo orden, y suman "
        "**100 puntos**." % len(tl["bloques"]),
        "- Todas son de tipo **%s**: %s" % (tipo_abierta[0], tipo_abierta[1]),
        "- **La entrega es individual aunque el trabajo sea en equipo:** cada integrante pega "
        "en su entrega lo que el equipo acordó. Es la forma de que quede constancia de que "
        "usted estuvo, y de que nadie pierda la nota porque el vocero se cayó de la sesión.",
        "- **Cierra al terminar la sesión.** Esto se califica como actividad en clase, no como "
        "tarea con plazo: se hace en la sala de grupo y se expone el mismo día.",
        "- Si un bloque pide un **dibujo** (un árbol, una línea de tiempo, una pantalla), pegue "
        "el **enlace** al dibujo en la carpeta del equipo y escriba en la respuesta los "
        "elementos que el bloque pide. La caja de texto no recibe imágenes.",
        "",
        "> **ExamLab no es una plataforma oficial de la UNIAJC:** es un canal del docente y se "
        "usa solo para esto. No pide datos personales suyos más allá de su nombre.",
        "",
        "## Cómo se califica",
        "",
        "| # | Bloque | Peso |",
        "|---|---|---|",
    ]
    for i, (b, item) in enumerate(zip(tl["bloques"], t["rubrica"]), 1):
        L.append("| %d | %s | **%d %%** |" % (i, b["clave"], item[1]))
    L += ["", "**Qué se revisa en cada uno:**", "",
          "| Criterio | Peso |", "|---|---|"]
    for cr, peso, _ in t["rubrica"]:
        L.append("| %s | **%d %%** |" % (cr, peso))
    L += ["", "## Cómo se expone", ""]
    for i, s in enumerate(tl["expo"], 1):
        if isinstance(s, tuple):
            L.append("%d. **%s** — %s" % (i, s[0], s[1]))
        else:
            L.append("%d. %s" % (i, s))
    L += [
        "",
        "> **Si se cae la conexión de alguien:** el documento del equipo está en Drive, así que "
        "lo escrito no se pierde. Quien se cayó vuelve a entrar a la sala de su equipo o aporta "
        "por el documento; si era el vocero, expone el siguiente de la lista. La nota es del "
        "equipo.",
        "",
        "> **Regla del curso sobre datos de otras personas:** no se suben **nombres, cédulas, "
        "teléfonos ni fotos** de terceros. Usen el rol: «la dueña de la papelería», «el auxiliar "
        "de la biblioteca». Es una regla de la profesión, no una formalidad del curso.",
        "",
    ]
    return "\n".join(L)


# --------------------------------------------------------------------- escribir

def _escribir(carpeta, nombre, texto, docx=True):
    os.makedirs(carpeta, exist_ok=True)
    md = os.path.join(carpeta, nombre + ".md")
    with open(md, "w", encoding="utf-8") as fh:
        fh.write(texto)
    hechos = [md]
    if docx:
        dx = os.path.join(carpeta, nombre + ".docx")
        convert(md, dx)
        hechos.append(dx)
    return hechos


def build_clase(n):
    t = TD.TEMAS[n]
    nom = _nombres(n, t)
    dir_clase, dir_kit, dir_capt = _dirs(n)

    pptx, titulos = build_pptx(n)
    hechos = [pptx]

    # README de capturas: lista los nombres que el guion pide de verdad
    capt = sorted(set(re.findall(r"\[\[captura:\s*([^\s|\]]+)", md_guion(n, titulos))))
    os.makedirs(dir_capt, exist_ok=True)
    rc = os.path.join(dir_capt, "README.txt")
    with open(rc, "w", encoding="utf-8") as fh:
        fh.write(README_CAPT % (n, t["titulo"],
                                "\n".join("  - " + x for x in capt) or "  (ninguna)"))
    hechos.append(rc)

    hechos += _escribir(dir_kit, nom["guion"], md_guion(n, titulos))
    hechos += _escribir(dir_kit, nom["solucion"], md_solucion(n))

    # El taller del estudiante: la fuente .md vive en Kit docente (regenerable) y el .docx
    # que se reparte va en Clases/.
    md_t = md_taller(n)
    hechos += _escribir(dir_kit, nom["taller"], md_t, docx=False)
    os.makedirs(dir_clase, exist_ok=True)
    dx = os.path.join(dir_clase, nom["taller"] + ".docx")
    convert(os.path.join(dir_kit, nom["taller"] + ".md"), dx)
    hechos.append(dx)
    return hechos


def build(ns=None):
    ns = ns or sorted(TD.TEMAS)
    hechos = []
    for n in ns:
        for h in build_clase(n):
            hechos.append(h)
            print("OK ->", os.path.relpath(h, ROOT))
    return hechos


if __name__ == "__main__":
    arg = [int(x) for x in sys.argv[1:]] or None
    build(arg)
