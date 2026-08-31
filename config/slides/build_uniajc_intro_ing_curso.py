# -*- coding: utf-8 -*-
"""Presentación del Curso (Sesión 0) de Introducción a la Ingeniería · FI300101 · 2026-2.

Genera **un deck por grupo** (SB141B, SB141C, LB141F) y el CALENDARIO de cada uno.
Los tres comparten encuadre, evaluación, dinámica y plataformas; lo que cambia es
día, horario, reloj de la sesión y las 16 fechas. Por eso es un solo builder
parametrizado por grupo y no tres archivos que se van a desincronizar.

Fuente de verdad de fechas/temas/porcentajes: ``intro_ing_datos`` →
``config/calendario/introduccion_ingenieria_2026_2.json``. Aquí no se escribe
ninguna fecha a mano.

Uso:
    python build_uniajc_intro_ing_curso.py            # los tres grupos
    python build_uniajc_intro_ing_curso.py SB141C     # uno solo
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from uniajc_slides_engine import (  # noqa: E402
    new_prs, course_cover, tutor_slide, padlet_slide, content_slide,
    table_content, evaluacion_cortes_slide, contenido_clases_slide,
    herramientas_slide, closing_slide, block_timeline_slide, checklist_slide,
)
import intro_ing_datos as D  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CURSO = os.path.join(ROOT, D.curso()["folder"])
OUT_CLASES = os.path.join(CURSO, "Clases")
OUT_PLAN = os.path.join(CURSO, "Plan curso", "2026-2")


# ---------------------------------------------------------------- diapositivas

def build_pptx(codigo):
    c = D.curso()
    g = D.grupo(codigo)
    din = D.dinamica()
    plat = D.plataformas()
    eq = din["equipos"]
    prs = new_prs()

    course_cover(
        prs,
        c["nombre_acentos"],
        "Fundamentos de la Ingeniería de Sistemas · Proyecto de curso (ABPr)",
        [
            "Código: **%s** · Grupo: **%s** · Periodo: **%s**" % (c["codigo"], codigo, D.load()["periodo"]),
            "Programa: %s · %s · UNIAJC" % ("Ingeniería de Sistemas", "Facultad de Ingeniería"),
            D.linea_horario(codigo),
            "Modalidad: **Virtual sincrónica** por **Google Meet** · Actividades en **plataformas gratuitas en la nube**",
            "Docente: %s" % D.DOCENTE,
        ],
        inicio_clase=g["hora_inicio_efectiva"],
    )

    tutor_slide(prs, D.DOCENTE, D.CREDS, D.CORREO, idx=2)
    padlet_slide(prs, idx=3)

    content_slide(
        prs,
        "¿Para qué existe este curso?",
        [
            "@@Objeto de estudio:@@ %s" % c["objeto_estudio"],
            "Es el curso de **primer semestre** que responde una pregunta concreta: **¿qué hace un ingeniero de sistemas y para qué sirve lo que hace?**",
            "No se programa todavía. Se aprende a **mirar un problema del entorno** y decidir si la ingeniería puede mejorarlo, a qué costo y con qué consecuencias.",
            "@@Objetivo:@@ %s" % c["objetivo"],
            "Créditos: **%d** · Tipo: **%s** · Habilitable: **%s**"
            % (c["creditos"], c["tipo_asignatura"], "Sí" if c["habilitable"] else "No"),
        ],
        idx=4,
    )

    content_slide(
        prs,
        "Resultados de aprendizaje",
        ["@@RAP del programa:@@ %s" % c["rap"]]
        + ["**%s** · %s" % tuple(r.split(" · ", 1)) for r in c["raa"]]
        + ["@@Cómo se demuestran:@@ no con un examen final, sino con el **proyecto del equipo** "
           "que se construye desde la sesión 6 y se expone en la 15."],
        idx=5,
    )

    block_timeline_slide(
        prs,
        "Así es cada sesión",
        D.timeline_slots(codigo),
        sub=("Las 16 sesiones tienen la misma estructura. La conocen desde hoy para "
             "que nadie llegue a los 45 min pensando que todavía hay tiempo."),
        idx=6,
        nota="Bloque de **%d min** · %s **%s** · inicio efectivo **%s**"
             % (c["duracion_min"], g["dia"], g["horario"].replace(" - ", " – "),
                g["hora_inicio_efectiva"]),
    )

    headers, rows = D.tabla_dinamica(codigo)
    table_content(
        prs,
        "El reloj de la sesión, al detalle",
        headers,
        rows,
        note=("La clase **arranca a las %s**, diez minutos después de la hora oficial, para "
              "esperar a quien todavía se está conectando. Esos diez minutos ya cuentan: la "
              "pregunta de entrada queda en pantalla compartida y se responde en el muro."
              % g["hora_inicio_efectiva"]),
        col_w=[1.5, 1.0, 2.2, 6.2],
        fs_body=11,
        idx=7,
    )

    content_slide(
        prs,
        "Cinco equipos · y por qué son exactamente cinco",
        [
            "@@Lo fijo son los equipos: %d.@@ Lo que cambia con la cantidad de matriculados es **cuánta gente hay en cada uno**."
            % eq["cantidad_fija"],
            "**%d equipos × %d min = %d min de exposiciones.** Ese presupuesto es el que no se puede estirar: la sesión cierra a los %d min."
            % (eq["cantidad_fija"], eq["min_por_equipo"],
               eq["cantidad_fija"] * eq["min_por_equipo"], c["duracion_min"]),
            "Si lo fijo fuera el tamaño («de 4 en 4»), un grupo de 35 daría **9 equipos = 27 min** y no alcanzaría el bloque. Por eso se fija el número, no el tamaño.",
            "Con " + "; con ".join(
                "**%d** matriculados, equipos de **%d**" % (e["matriculados"], e["por_equipo"])
                if i == 0 else "**%d**, de **%d**" % (e["matriculados"], e["por_equipo"])
                for i, e in enumerate(eq["ejemplos_tamano"])
            ) + ". El tiempo de exposición es el mismo.",
            "@@Los equipos son estables todo el semestre@@ (el proyecto es del equipo), pero el **vocero rota** cada sesión: al final del curso todos han expuesto.",
            "**Todos los equipos exponen todas las sesiones.** No hay sesión en la que a un equipo «no le toque».",
        ],
        idx=8,
    )

    herramientas_slide(
        prs,
        [{"name": h["nombre"], "logo": h["logo"], "note": h["uso"]} for h in plat["stack"]],
        title="Dónde se trabaja: plataformas gratuitas en la nube",
        sub=("Todas gratis de verdad y desde el navegador · ninguna pide tarjeta de crédito · "
             "ninguna hay que instalar"),
        idx=9,
    )

    checklist_slide(
        prs,
        "Las reglas de las plataformas",
        plat["reglas_proyectadas"],
        sub="Aplican a las %d sesiones · se recuerdan solo hoy" % c["n_sesiones"],
        idx=10,
    )

    ct = D.cortes_slide(codigo)
    evaluacion_cortes_slide(
        prs,
        "Sistema de evaluación",
        [
            {"corte": x["corte"], "pct": x["pct"], "ventana": x["ventana"],
             "desglose": ["**%s**" % d if i == 0 else d for i, d in enumerate(x["desglose"])]}
            for x in ct
        ],
        note=("Cada corte cierra en la sesión %s (%s). La evaluación es **formativa y "
              "continua**: lo que más pesa es lo que se hace en clase cada semana, no un "
              "único examen. Ningún cierre de corte cae en festivo."
              % (" / ".join(str(x["cierre_sesion"]) for x in ct),
                 " / ".join(x["cierre_fecha"] for x in ct))),
        idx=11,
    )

    items = D.contenido_items(codigo)
    aut = D.semanas_autonomas(codigo)
    sub = "Sesión 0 + **16 sesiones** de 90 min · %s · %s a %s" % (
        g["dia"], D.ddmmyyyy(g["inicio"]), D.ddmmyyyy(g["fin"]))
    if aut:
        sub += " · incluye **1 semana autónoma** por el festivo del %s" % D.ddmm(aut[0]["fecha"])
    contenido_clases_slide(prs, items, title="CONTENIDO", sub=sub, idx=12, size=12)

    closing_slide(
        prs,
        "¡Empezamos!",
        [
            "%s · **%s** · Grupo **%s**" % (c["nombre_acentos"], c["codigo"], codigo),
            "%s **%s** · inicio efectivo **%s** · Periodo **%s**"
            % (g["dia"], g["horario"].replace(" - ", " – "), g["hora_inicio_efectiva"],
               D.load()["periodo"]),
            "UNIAJC · Ingeniería de Sistemas · Virtual sincrónica por Google Meet",
        ],
        accent="Ingeniería es decidir con criterio, no solo saber cómo",
    )

    os.makedirs(OUT_CLASES, exist_ok=True)
    out = os.path.join(
        OUT_CLASES,
        "Presentacion del Curso - Introduccion a la Ingenieria - %s.pptx" % codigo,
    )
    prs.save(out)
    return out


# ------------------------------------------------------------------ calendario

def build_calendario(codigo):
    c = D.curso()
    g = D.grupo(codigo)
    ta = D.temas_acentos()
    ct = D.cortes_slide(codigo)
    al = D.load()["alerta_calendario"]
    fest = D.load()["festivos_colombia_2026_en_rango"]
    cierres = {x["cierre_sesion"]: x for x in ct}

    L = [
        "# Calendario 2026-2 — %s · Grupo %s" % (c["nombre_acentos"], codigo),
        "",
        "- **Código:** %s" % c["codigo"],
        "- **Grupo:** %s" % codigo,
        "- **Periodo:** %s · **%s – %s**" % (D.load()["periodo"], D.ddmmyyyy(g["inicio"]),
                                             D.ddmmyyyy(g["fin"])),
        "- **Horario:** %s **%s** (%d min) · **inicio efectivo %s** (se arranca 10 min "
        "después de la hora oficial para esperar a que los estudiantes se conecten)"
        % (g["dia"], g["horario"].replace(" - ", " – "), c["duracion_min"],
           g["hora_inicio_efectiva"]),
        "- **Modalidad:** Virtual (síncrona) por Google Meet · actividades en plataformas gratuitas en la nube",
        "- **Docente:** %s · `%s`" % (D.DOCENTE, D.CORREO),
        "- **Total sesiones:** %d · **temas del microcurrículo:** %d — correspondencia "
        "**1:1** (Sesión N = Clase N, no hay sesiones dobles)" % (c["n_sesiones"], c["n_temas"]),
        "- **Semanas de calendario:** %d" % g["n_semanas_calendario"],
        "",
        "> %s" % g["nota"],
        "",
        "## Aviso sobre las fechas de fin",
        "",
        "**%s.** %s" % (al["titulo"], al["detalle"]),
        "",
        "> **Plan B si el programa exige cerrar antes:** %s" % al["plan_b"],
        "",
        "## Dinámica de la sesión (90 min)",
        "",
    ]
    headers, rows = D.tabla_dinamica(codigo)
    L += ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    L += ["| " + " | ".join(r) + " |" for r in rows]
    din = D.dinamica()
    eq = din["equipos"]
    L += [
        "",
        "**Equipos: %d, fijos.** %s" % (eq["cantidad_fija"], eq["por_que_fija"]),
        "",
        "| Matriculados | Integrantes por equipo | Minutos de exposición |",
        "|---|---|---|",
    ]
    for ej in eq["ejemplos_tamano"]:
        L.append("| %d | %d | %d equipos × %d min = %d min |"
                 % (ej["matriculados"], ej["por_equipo"], eq["cantidad_fija"],
                    eq["min_por_equipo"], eq["cantidad_fija"] * eq["min_por_equipo"]))
    L += [
        "",
        "> **Excepción:** %s" % eq["excepcion"],
        "> **Rotación:** %s" % eq["regla_rotacion"],
        "",
        "## Cortes (30% / 30% / 40%)",
        "",
        "| Corte | % | Ventana | Sesiones | Cierre de corte | Desglose |",
        "|---|---|---|---|---|---|",
    ]
    for x, base in zip(ct, D.cortes()):
        L.append("| Corte %d | %s | %s | %s | Sesión %d · %s | %s |"
                 % (x["corte"], x["pct"], x["ventana"].split(" · ")[0], base["sesiones"],
                    x["cierre_sesion"], x["cierre_fecha"], " · ".join(x["desglose"])))
    L += [
        "",
        "> %s" % D.load()["regla_evaluacion"],
        "",
        "## Sesiones",
        "",
        "> La columna **Clase de material** indica la carpeta `Clases/Clase N - …` y "
        "`Kit docente/Clase N/` que se usa. En este curso **Sesión N = Clase N**.",
        "",
        "| Sesión | Fecha | Tipo | Clase de material | Tema | Trabajo independiente | Nota |",
        "|---|---|---|---|---|---|---|",
    ]
    for s in D.sesiones(codigo):
        n = s.get("sesion")
        if n is None:
            L.append("| — | %s | Autónoma (festivo) | — | %s | %s | festivo: %s |"
                     % (D.ddmmyyyy(s["fecha"]),
                        "Ensayo general de la exposición final",
                        "Subir el ensayo (video o fotos) a la carpeta del equipo",
                        s.get("festivo", "festivo")))
            continue
        t = D.tema(s["tema_n"])
        nota = "cierra Corte %d (%s)" % (cierres[n]["corte"], cierres[n]["pct"]) if n in cierres else "—"
        L.append("| %d | %s | Virtual (síncrona) | Clase %d | %s | %s | %s |"
                 % (n, D.ddmmyyyy(s["fecha"]), s["tema_n"], ta[s["tema_n"]], t["ti"], nota))

    L += ["", "## Festivos Colombia 2026 (rango del periodo)", ""]
    fechas_grupo = {s["fecha"] for s in D.sesiones(codigo)}
    for iso, nombre in sorted(fest.items()):
        golpea = " — **cae en día de clase de este grupo: semana autónoma**" if iso in fechas_grupo else " — no cae en día de clase de este grupo"
        L.append("- %s — %s%s" % (D.ddmmyyyy(iso), nombre, golpea))
    L += [
        "",
        "> %s" % D.load()["regla_festivos"],
        "",
        "## Pendiente",
        "",
    ]
    L += ["- %s" % p for p in D.load()["pendiente"]]
    L += [
        "",
        "Fuente: `config/calendario/introduccion_ingenieria_2026_2.json` "
        "(generado por `config/slides/build_uniajc_intro_ing_curso.py`).",
        "",
    ]

    os.makedirs(OUT_PLAN, exist_ok=True)
    out = os.path.join(OUT_PLAN, "CALENDARIO_2026-2 - %s.md" % codigo)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    return out


# ----------------------------------------------------------------------- LEEME

def build_leeme():
    """`LEEME - Dinamica de sesion y plataformas.md`, en la raiz del curso.

    Es el documento que responde de una sola vez «como es una sesion» y «en que
    plataformas se trabaja», para los tres grupos. Todo sale del JSON: si cambia una
    herramienta o un bloque de la dinamica, este documento cambia solo.
    """
    c = D.curso()
    din = D.dinamica()
    eq = din["equipos"]
    plat = D.plataformas()
    ia = plat["asistente_ia"]

    L = [
        "# Dinámica de la sesión y plataformas — %s" % c["nombre_acentos"],
        "",
        "> Documento del docente. Responde dos cosas de una vez: **cómo es una sesión de este "
        "curso** y **en qué plataformas se trabaja**. Aplica igual a los tres grupos "
        "(%s)." % ", ".join(D.codigos_grupo()),
        "",
        "- **Código:** %s · **Créditos:** %d · **Modalidad:** %s"
        % (c["codigo"], c["creditos"], c["modalidad"]),
        "- **Bloque:** %d min · **%d sesiones** · correspondencia 1:1 Sesión N = Clase N"
        % (c["duracion_min"], c["n_sesiones"]),
        "- **Estrategia:** %s · **Enfoque:** %s" % (c["estrategia_didactica"], c["enfoque"]),
        "- **Fuente única de este documento:** "
        "`config/calendario/introduccion_ingenieria_2026_2.json`",
        "",
        "---",
        "",
        "## 1. Los cinco bloques de la sesión",
        "",
        "Toda sesión tiene los mismos cinco bloques y suman exactamente %d minutos. No hay "
        "bloque negociable: si uno se estira, el que paga es el de exposiciones, que es el "
        "instrumento de evaluación del curso." % sum(b["min"] for b in din["bloques"]),
        "",
        "| # | Duración | Bloque | Qué pasa |",
        "|---|---|---|---|",
    ]
    for b in din["bloques"]:
        L.append("| %d | **%d min** | %s | %s |" % (b["orden"], b["min"], b["nombre"], b["que_pasa"]))
    L += [
        "",
        "### El mismo bloque, en el reloj de cada grupo",
        "",
        "| Bloque | " + " | ".join("%s (%s)" % (g["grupo"], g["dia"]) for g in D.grupos()) + " |",
        "|---|" + "---|" * len(D.grupos()),
    ]
    relojes = [din["reloj_por_grupo"][g["hora_inicio_oficial"]] for g in D.grupos()]
    for i, b in enumerate(din["bloques"]):
        celdas = [" ".join(r[i].split()[:3]).replace(" - ", " – ") for r in relojes]
        L.append("| %s | %s |" % (b["nombre"], " | ".join(celdas)))
    L += [
        "",
        "> **Por qué se arranca 10 minutos después de la hora oficial.** El curso es virtual y "
        "entrar a la sesión nunca es instantáneo: hay quien viene de trabajar, quien pelea con el "
        "micrófono y quien entra desde el celular. Arrancar a la hora exacta obliga a repetir la "
        "primera explicación cinco veces. Esos 10 minutos **no son de descanso**: la pregunta de "
        "entrada queda en pantalla compartida y se responde en el muro del curso. A la hora "
        "efectiva (%s) se arranca el bloque teórico y ahí sí no se espera a nadie."
        % " / ".join("%s en %s" % (g["hora_inicio_efectiva"], g["grupo"]) for g in D.grupos()),
        "",
        "> **El aula.** %s" % din["plataforma_aula"],
        "",
        "---",
        "",
        "## 2. Los cinco equipos",
        "",
        "**%d equipos, fijos.** Lo que cambia con la cantidad de matriculados es cuánta gente "
        "hay en cada uno, no cuántos equipos hay." % eq["cantidad_fija"],
        "",
        eq["por_que_fija"],
        "",
        "**Una sala de Meet por equipo.** %s" % eq["salas"],
        "",
        "| Matriculados | Integrantes por equipo | Minutos de exposición |",
        "|---|---|---|",
    ]
    for ej in eq["ejemplos_tamano"]:
        L.append("| %d | %d | %d equipos × %d min = **%d min** |"
                 % (ej["matriculados"], ej["por_equipo"], eq["cantidad_fija"],
                    eq["min_por_equipo"], eq["cantidad_fija"] * eq["min_por_equipo"]))
    L += [
        "",
        "> **Excepción:** %s" % eq["excepcion"],
        "",
        "> **Rotación:** %s" % eq["regla_rotacion"],
        "",
        "> **Ausencias:** %s" % eq["ausencias"],
        "",
        "**Todos los equipos exponen todas las sesiones.** No hay sesión en la que a un equipo "
        "«no le toque»: por eso el presupuesto de %d min es el que manda."
        % (eq["cantidad_fija"] * eq["min_por_equipo"]),
        "",
        "---",
        "",
        "## 3. Las plataformas: qué significa «gratuitas y en la nube»",
        "",
        plat["_comentario"],
        "",
    ]
    for h in plat["stack"]:
        L += [
            "### %s" % h["nombre"],
            "",
            "- **Para qué:** %s" % h["uso"],
            "- **Por qué esta y no otra:** %s" % h["por_que"],
            "- **Cuenta:** %s · **Gratis:** %s" % (h["cuenta"], h["gratis"]),
        ]
        if h.get("alternativa"):
            L.append("- **Alternativa:** %s" % h["alternativa"])
        if h.get("aviso"):
            L.append("- ⚠️ **%s**" % h["aviso"])
        L.append("")
    L += [
        "### Asistente de IA",
        "",
        "- **Cuándo:** %s" % ia["cuando"],
        "- **Cuál:** %s" % ia["opciones"],
        "- **Regla:** %s" % ia["regla"],
        "- **Gratis:** %s" % ia["gratis"],
        "",
        "---",
        "",
        "## 4. Las reglas de trabajo en la nube",
        "",
        "Se explican completas el primer día y quedan como acuerdo del curso. La versión corta "
        "de estas mismas reglas es la que va proyectada en la diapositiva de la sesión 1.",
        "",
    ]
    L += ["%d. %s" % (i, r) for i, r in enumerate(plat["reglas"], 1)]
    L += [
        "",
        "---",
        "",
        "## 5. Qué herramienta usa cada sesión",
        "",
        "| Sesión | Tema | Herramientas | Trabajo dirigido en clase |",
        "|---|---|---|---|",
    ]
    for t in D.temas():
        L.append("| %d | %s | %s | %s |"
                 % (t["n"], t["tema_acentos"], " · ".join(t["herramientas"]), t["tid"]))
    L += [
        "",
        "> %s" % plat["_nota_mapa_sesiones"],
        "",
        "---",
        "",
        "## 6. Descartadas, y por qué",
        "",
        "| Herramienta | Por qué no |",
        "|---|---|",
    ]
    for x in plat["descartadas"]:
        L.append("| %s | %s |" % (x["que"], x["por_que"]))
    L += [
        "",
        "---",
        "",
        "## 7. %s" % plat["plan_b"]["titulo"],
        "",
        "En un curso virtual la pregunta no es «¿y si no hay red en la sala?» sino **«¿y si se cae "
        "la de alguien?»**. Pasa todas las semanas, así que está previsto por caso:",
        "",
        "| Se cae… | Qué pasa |",
        "|---|---|",
        "| Un integrante del equipo | %s |" % plat["plan_b"]["de_un_integrante"],
        "| El vocero del día | %s |" % plat["plan_b"]["del_vocero"],
        "| El docente | %s |" % plat["plan_b"]["del_docente"],
        "| Google Meet | %s |" % plat["plan_b"]["de_meet"],
        "",
        "> **Regla de diseño:** %s" % plat["plan_b"]["regla"],
        "",
        "---",
        "",
        "## 8. Pendiente",
        "",
    ]
    L += ["- %s" % p for p in D.load()["pendiente"]]
    L += [
        "",
        "Fuente: `config/calendario/introduccion_ingenieria_2026_2.json` "
        "(generado por `config/slides/build_uniajc_intro_ing_curso.py`).",
        "",
    ]

    os.makedirs(CURSO, exist_ok=True)
    out = os.path.join(CURSO, "LEEME - Dinamica de sesion y plataformas.md")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    return out


def build(codigos=None):
    hechos = []
    for codigo in (codigos or D.codigos_grupo()):
        p = build_pptx(codigo)
        c = build_calendario(codigo)
        hechos += [p, c]
        print("OK ->", os.path.relpath(p, ROOT))
        print("OK ->", os.path.relpath(c, ROOT))
    leeme = build_leeme()
    hechos.append(leeme)
    print("OK ->", os.path.relpath(leeme, ROOT))
    return hechos


if __name__ == "__main__":
    build(sys.argv[1:] or None)
    print("DONE")
