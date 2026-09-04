# -*- coding: utf-8 -*-
"""Clase 1 de Introduccion a la Ingenieria (FI300101) · 2026-2.

**Material general para cualquier grupo.** No lleva fechas, ni reloj de pared, ni codigo
de grupo: los tres grupos (SB141B, SB141C, LB141F) dictan esta misma clase con este mismo
material. Lo que cambia por grupo esta en el deck de Presentacion del Curso (Sesion 0).

Genera:

    Clases/Clase 1 - Presentacion del curso y diagnostico inicial/
        Presentacion.pptx
        Actividad Clase 1 - Ficha del campo de accion.docx
        Prueba Diagnostica - Introduccion a la Ingenieria.docx      (version estudiante)
    Kit docente/Clase 1/
        Guion Docente Clase 1 - Presentacion del curso y diagnostico inicial.md / .docx
        Solucion Actividad Clase 1 - Ficha del campo de accion.md / .docx
        Prueba Diagnostica - CLAVE DOCENTE.md / .docx
        Capturas/README.txt

Los ``{{slide:...}}`` del guion se resuelven contra los titulos REALES del deck, que se
van recogiendo mientras se construye (``_T``). No hay un ``_slide_map()`` escrito a mano
que se pueda desincronizar del deck.

Uso:
    python build_uniajc_intro_ing_clase1.py
"""
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from uniajc_slides_engine import (  # noqa: E402
    new_prs, class_cover, content_slide, block_timeline_slide, hook_slide,
    before_after_slide, cards_grid_slide, steps_visual_slide, checklist_slide,
    box_note_slide, closing_slide,
)
from guion_md_a_docx import convert  # noqa: E402
import intro_ing_datos as D  # noqa: E402
import intro_ing_clase1_data as C1  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CURSO = os.path.join(ROOT, D.curso()["folder"])
DIR_CLASE = os.path.join(CURSO, "Clases", "Clase %d - %s" % (C1.CLASE_N, C1.SLUG))
DIR_KIT = os.path.join(CURSO, "Kit docente", "Clase %d" % C1.CLASE_N)
DIR_CAPT = os.path.join(DIR_KIT, "Capturas")

NOMBRE_ACTIVIDAD = "Actividad Clase %d - Ficha del campo de accion" % C1.CLASE_N
NOMBRE_DIAG = "Prueba Diagnostica - Introduccion a la Ingenieria"
NOMBRE_GUION = "Guion Docente Clase %d - %s" % (C1.CLASE_N, C1.SLUG)
NOMBRE_SOL = "Solucion Actividad Clase %d - Ficha del campo de accion" % C1.CLASE_N
NOMBRE_CLAVE = "Prueba Diagnostica - CLAVE DOCENTE"

LETRAS = "abcdefghij"


# ------------------------------------------------------- resolucion de {{slide:}}

_SLIDE_TOKEN = re.compile(r"\{\{\s*slide:\s*([^}]+?)\s*\}\}")


def _plano(s):
    """Minusculas sin tildes, para comparar fragmentos con titulos reales."""
    s = unicodedata.normalize("NFD", str(s))
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


def _slide_no(titulos, frag):
    """Numero de la diapositiva cuyo titulo contiene ``frag``. Unico o falla."""
    fp = _plano(frag)
    hits = [i for i, t in enumerate(titulos, 1)
            if not _plano(t).startswith("portada") and fp in _plano(t)]
    if len(hits) == 1:
        return hits[0]
    raise SystemExit(
        "Clase %d: el fragmento {{slide:%s}} %s.\nTitulos del deck:\n%s"
        % (C1.CLASE_N, frag,
           "no coincide con ninguna diapositiva" if not hits
           else "es ambiguo (diapositivas %s)" % ", ".join(map(str, hits)),
           "\n".join("  %2d. %s" % (i, t) for i, t in enumerate(titulos, 1)))
    )


def _resolver(texto, titulos):
    return _SLIDE_TOKEN.sub(
        lambda m: "diapositiva %d" % _slide_no(titulos, m.group(1)), texto)


# ---------------------------------------------------------------- diapositivas

def build_pptx():
    """Devuelve ``(ruta, titulos)``. ``titulos`` alimenta la resolucion de {{slide:}}."""
    prs = new_prs()
    T = []  # titulos reales, en orden

    def t(titulo):
        T.append(titulo)
        return titulo

    class_cover(
        prs,
        C1.TITULO,
        C1.SUBTITULO,
        clase_n=C1.CLASE_N,
    )
    t("Portada · Clase %d · %s" % (C1.CLASE_N, C1.TITULO))

    block_timeline_slide(
        prs,
        t("Agenda de hoy (90 min)"),
        C1.AGENDA,
        sub=("El reloj arranca 10 min después de la hora oficial de su grupo. "
             "La estructura es la misma las 16 sesiones."),
        idx=2,
        nota="Bloque de **90 min** · hoy los 45 min de teoría se reparten entre encuadre (30) "
             "y diagnóstico (15)",
    )

    content_slide(prs, t("Objetivos de la sesión"), C1.OBJETIVOS, idx=3)

    hook_slide(
        prs,
        "¿Qué hace un ingeniero de sistemas un martes a las 10 de la mañana?",
        [
            "Escríbanlo en el muro del curso, en una frase, desde el celular.",
            "No hay respuesta correcta. Volvemos a este muro en 30 minutos.",
        ],
        eyebrow="Pregunta de entrada",
        idx=4,
    )
    t("Gancho · ¿Qué hace un ingeniero de sistemas un martes a las 10 de la mañana?")

    box_note_slide(
        prs,
        t("El diagnóstico de hoy: qué es y qué no es"),
        [
            ("info", "**Son 13 preguntas y 15 minutos.** Tres bloques: qué creen que es la "
                     "ingeniería, qué saben ya, y en qué condiciones van a trabajar este semestre."),
            ("aclaracion", "**No tiene nota. Ni suma ni resta.** No se espera que sepan las "
                           "respuestas: si las supieran, este curso no tendría razón de existir. "
                           "«No sé» es una respuesta válida y útil."),
            ("advertencia", "**No respondan lo que creen que el profesor quiere leer.** Con estos "
                            "datos se planean las 15 sesiones que siguen: una respuesta de adorno "
                            "hace que el curso se planee mal."),
        ],
        idx=5,
    )

    before_after_slide(
        prs,
        t("Ingeniería de Sistemas no es programación"),
        "Lo que casi todos creen",
        C1.NO_ES_CREENCIA,
        "Lo que realmente es",
        C1.NO_ES_REALIDAD,
        sub="La confusión más costosa del primer semestre · se desarma hoy",
        idx=6,
        size=13,
    )

    content_slide(prs, t("Qué es la Ingeniería de Sistemas"), C1.QUE_ES, idx=7)

    cards_grid_slide(
        prs,
        t("Los cinco campos de acción"),
        [(c["nombre"], "**%s.** %s" % (c["corto"], c["ejemplo"])) for c in C1.CAMPOS],
        sub="Uno por equipo · se sortea, no se elige",
        columns=3,
        idx=8,
    )

    steps_visual_slide(
        prs,
        t("El método del curso: de un problema del entorno a una propuesta"),
        C1.METODO,
        sub="Los mismos cuatro pasos, de la actividad de hoy al proyecto de la Clase 15",
        idx=9,
    )

    content_slide(prs, t("El proyecto del curso"), C1.PROYECTO, idx=10)

    content_slide(prs, t("Cinco equipos, los mismos todo el semestre"), C1.EQUIPOS, idx=11)

    act = C1.ACTIVIDAD
    checklist_slide(
        prs,
        t("Actividad de hoy: %s" % act["titulo"]),
        ["**%s** — %s" % (b["clave"], b["pide"]) for b in act["bloques"]],
        sub="%d min en equipos · un campo por equipo, sorteado · la ficha se escribe en la "
            "carpeta del equipo (Google Docs o Slides)" % act["duracion_min"],
        idx=12,
    )

    steps_visual_slide(
        prs,
        t("Cómo se expone en 3 minutos"),
        [
            ("30 s · El campo", "Qué es y de qué se ocupa, en sus palabras."),
            ("60 s · El problema del entorno", "Quién lo sufre y la cifra. Es lo que más pesa."),
            ("30 s · La confusión frecuente", "Qué cree la gente y por qué es falso."),
            ("60 s · Si se hace mal", "A quién le pasa y qué pierde."),
        ],
        sub="Habla el vocero · cronómetro proyectado · se corta a los 3 min desde hoy",
        idx=13,
    )

    sig = C1.TI_SIGUIENTE
    content_slide(
        prs,
        t("Para la sesión 2"),
        [
            "@@Trabajo dirigido:@@ %s" % sig["tid"],
            "@@Trabajo independiente:@@ %s" % sig["ti"],
            "**%s**" % sig["tema_siguiente"],
            "@@Aviso:@@ %s" % sig["aviso"],
            "Antes de salir: el enlace de la carpeta del equipo, con permiso de lectura para el "
            "docente, y el nombre del vocero de hoy.",
        ],
        idx=14,
    )

    closing_slide(
        prs,
        "Nos vemos en la sesión 2",
        [
            "%s · Clase %d" % (C1.TITULO, C1.CLASE_N),
            "%s · UNIAJC · Ingeniería de Sistemas" % D.curso()["codigo"],
        ],
        accent="Ingeniería es decidir con criterio, no solo saber cómo",
    )
    T.append("Cierre · Nos vemos en la sesión 2")

    os.makedirs(DIR_CLASE, exist_ok=True)
    out = os.path.join(DIR_CLASE, "Presentacion.pptx")
    prs.save(out)
    return out, T


# ----------------------------------------------------------------------- guion

def md_guion(titulos):
    c = D.curso()
    act = C1.ACTIVIDAD
    L = [
        "# Guion docente — Clase %d: %s" % (C1.CLASE_N, C1.TITULO),
        "",
        "## Información de la clase",
        "- Asignatura: %s (%s)" % (c["nombre_acentos"], c["codigo"]),
        "- Duración del bloque: **%d min**" % c["duracion_min"],
        "- Tipo: Clase virtual sincrónica por Google Meet · Sesión 1 de %d · corresponde al tema 1 "
        "del microcurrículo"
        % c["n_sesiones"],
        "- Modalidad: **Virtual (síncrona)** por Google Meet · actividades en plataformas "
        "gratuitas en la nube · los 5 equipos trabajan en **salas de grupo**",
        "- **Material general para los tres grupos** (SB141B, SB141C, LB141F): sin fechas ni "
        "horarios de reloj. El reloj de pared de cada grupo está en su `CALENDARIO_2026-2 - <GRUPO>.md`.",
        "- Enfoque: %s · Estrategia: %s" % (c["enfoque"], c["estrategia_didactica"]),
        "",
        "> %s" % C1.NOTA_BLOQUE,
        "",
        "## Objetivos de la clase",
    ]
    L += ["- %s" % o for o in C1.OBJETIVOS]
    L += [
        "",
        "## Hoy avanzamos el proyecto en…",
        "",
        "**Detectar y escribir el problema del entorno que será candidato al proyecto del semestre**",
        "",
        "**Entregable concreto:** %s" % act["entregable"],
        "",
        "**Herramientas:** Padlet (muro de la pregunta de entrada) · Google Docs o Slides "
        "(ficha del equipo) · ExamLab (diagnóstico)",
        "",
        "## Fundamento teórico para el docente",
    ]
    for b in C1.FUNDAMENTO:
        # Un bloque puede cubrir mas de una diapositiva (p. ej. el metodo y el proyecto van
        # juntos). Se resuelven TODOS los tokens del campo `slide`, no solo el primero: asi
        # ninguna diapositiva de teoria queda sin su parrafo en el fundamento.
        ns = [_slide_no(titulos, m.group(1)) for m in _SLIDE_TOKEN.finditer(b["slide"])]
        etq = ("diapositiva %d" % ns[0] if len(ns) == 1
               else "diapositivas %s y %d" % (", ".join(str(x) for x in ns[:-1]), ns[-1]))
        L += ["### %s - %s" % (b["titulo"], etq), ""]
        L += [p for par in b["cuerpo"] for p in (par, "")]

    L += [
        "## Referencias a diapositivas",
        "Numeración real del deck `Clases/Clase %d - %s/Presentacion.pptx`. Las etiquetas "
        "[Slide N] del plan y las referencias del fundamento apuntan aquí." % (C1.CLASE_N, C1.SLUG),
        "",
    ]
    L += ["%d. %s" % (i, t) for i, t in enumerate(titulos, 1)]
    L += ["", "## Plan de clase minuto a minuto (%d min)" % c["duracion_min"], ""]

    L += [
        "### 00:00–00:10 · Apertura · [Slide 4]",
        "Entre a Meet 5 min antes, comparta pantalla con la pregunta de entrada **antes** de que "
        "entre el primer estudiante y déjela ahí los diez minutos:",
        "",
        "> «%s»" % C1.PREGUNTA_ENTRADA,
        "",
        "**[Nota docente]:** abra el muro del curso en Padlet y pegue el enlace en el chat de Meet "
        "(y el QR en pantalla, para quien esté en el celular). Se responde sin crear cuenta. No "
        "corrija ninguna respuesta en voz alta ni señale a "
        "quien la escribió: es el primer día de universidad de varios y el muro tiene que quedar "
        "como un sitio donde se puede escribir sin costo.",
        "",
        "**[Nota docente]:** mientras entran, anote cuántos hay conectados desde la lista de "
        "participantes de Meet. Ese número decide el tamaño de los cinco equipos y lo necesita en "
        "el minuto 55. Verifique también que las **cinco salas de grupo** ya estén creadas: "
        "crearlas en vivo se come la actividad.",
        "",
        "### 00:10–00:40 · Encuadre del curso + tema · deck «Presentación del Curso» y [Slide 6][Slide 7][Slide 8]",
        "Los primeros **12 min** son el deck «Presentación del Curso» del grupo "
        "(`Clases/Presentacion del Curso - Introduccion a la Ingenieria - <GRUPO>.pptx`): "
        "encuadre, dinámica de la sesión, cinco equipos, plataformas, evaluación y contenido. "
        "No lo lea entero: proyecte la dinámica, los equipos, las reglas de las plataformas y los "
        "cortes, y remita el resto al calendario del grupo.",
        "",
        "Los **18 min** restantes son el tema de esta clase, en este orden (son los títulos de las "
        "diapositivas de teoría):",
        "",
        "- Ingeniería de Sistemas no es programación",
        "- Qué es la Ingeniería de Sistemas",
        "- Los cinco campos de acción",
        "",
        "El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente», "
        "ya dividido por diapositiva: esa sección está escrita para dictarla sin consultar otra fuente.",
        "",
        "**[Nota docente]:** al terminar los cinco campos, **vuelva al muro de Padlet** y contraste: "
        "casi ninguna respuesta del curso mencionó negociar un plazo, revisar un permiso mal puesto "
        "o decidir qué se recorta. Ese contraste hace el trabajo que no hace un discurso sobre «el "
        "amplio campo de acción de la profesión».",
        "",
        "### 00:40–00:55 · Evaluación diagnóstica · [Slide 5]",
        "Diga las tres cosas de la diapositiva **antes** de repartirlo, sin adornos: no tiene nota; "
        "no se espera que sepan; responder lo que creen que el profesor quiere leer arruina el "
        "instrumento porque con esto se planean las 15 sesiones siguientes.",
        "",
        "**[Nota docente]:** se aplica en ExamLab: el enlace se pega en el chat de Meet y se "
        "responde en la misma sesión. La versión en documento está en `Clases/Clase 1 - …/%s.docx` "
        "para quien no logre abrir ExamLab. Los 13 ítems y lo que "
        "revela cada uno están en `Kit docente/Clase 1/%s.docx`." % (NOMBRE_DIAG, NOMBRE_CLAVE),
        "",
        "**[Nota docente]:** las tres últimas preguntas (computador, conexión, horas de trabajo) "
        "son las que usa en el minuto 55 para conformar los equipos. Revíselas mientras el grupo "
        "termina; son de conteo, no de ficha individual.",
        "",
        "### 00:55–01:12 · Actividad en equipos · [Slide 11][Slide 12]",
        "Primero **conforme los cinco equipos** (3 min): divida el total de asistentes entre cinco "
        "y mezcle según las respuestas del bloque C — reparta a quien no tiene computador propio y "
        "a quien trabaja más de 20 horas entre equipos distintos, en vez de dejar que se agrupen "
        "por amistad. Después **sortee el campo** de cada equipo delante del curso.",
        "",
        "Luego los **14 min de ficha**, con los equipos ya en sus salas de grupo. No se quede en la "
        "sala principal: entre a las cinco salas con un orden fijo, unos 3 min en cada una, y en "
        "cada entrada revise **una sola cosa**, el "
        "bloque «PROBLEMA DEL ENTORNO», porque es el que alimenta el proyecto del semestre y el "
        "único que no se puede arreglar después.",
        "",
        "**[Nota docente]:** las tres correcciones en caliente, sin discusión — «los usuarios» → "
        "pida un rol concreto y no acepte avance hasta que esté escrito; «se pierde mucho tiempo» → "
        "pida un número aunque sea estimado; «el problema es que no tienen una app» → recuerde que "
        "el problema es lo que pasa hoy **sin** el sistema.",
        "",
        "### 01:12–01:27 · Exposiciones · [Slide 13]",
        "De vuelta en la sala principal: cinco equipos × 3 min, cronómetro en pantalla, habla el "
        "vocero con su documento ya compartido. **Se corta a los 3 min "
        "desde la primera sesión:** si hoy se permite estirar, en la Clase 15 las exposiciones "
        "finales no caben en el bloque.",
        "",
        "**[Nota docente]:** no dé retroalimentación equipo por equipo — cinco rondas de "
        "comentarios no caben en 15 min. Anote y guarde todo para el cierre.",
        "",
        "**[Nota docente]:** exija el enlace de lectura del documento **pegado en el chat** antes de "
        "que empiecen las exposiciones, y que el vocero tenga la pestaña abierta. Buscar el archivo "
        "o pelear con «compartir pantalla» con el cronómetro corriendo se come el turno.",
        "",
        "### 01:27–01:30 · Cierre · [Slide 14]",
        "Dé **dos** observaciones del conjunto (no una nota por equipo) y cierre con la tarea:",
        "",
        "> «%s Y para la próxima: %s»" % (C1.SOLUCION["cierre"], C1.TI_SIGUIENTE["ti"]),
        "",
        "**[Nota docente]:** antes de que salga nadie, verifique las tres cosas: integrantes de "
        "cada equipo anotados, enlace de la carpeta compartida con permiso de lectura, y vocero de "
        "hoy registrado en la bitácora.",
        "",
        "## Actividad / taller (detalle)",
        "",
        "**%s** · %d min · exposición de %d min por equipo."
        % (act["titulo"], act["duracion_min"], act["exposicion_min"]),
        "",
        act["consigna"],
        "",
        "> **Reparto del campo:** no se elige, %s" % act["reparto"],
        "",
        "> **Si se cae la conexión de alguien:** %s" % act["plan_b"],
        "",
        "| Bloque | Qué se pide | Cómo verificar en la rotación |",
        "|---|---|---|",
    ]
    for b in act["bloques"]:
        L.append("| **%s** | %s | %s |" % (b["clave"], b["pide"], b["check"]))
    L += ["", "### Criterio de éxito", ""]
    L += ["| Criterio | Peso | Por qué |", "|---|---|---|"]
    for crit, peso, por_que in C1.RUBRICA:
        L.append("| %s | %d%% | %s |" % (crit, peso, por_que))
    L += [
        "",
        "## Errores frecuentes del estudiante (y cómo corregirlos en el momento)",
        "",
    ]
    L += ["- %s" % e for e in C1.ERRORES]
    L += ["", "## Preguntas frecuentes del estudiante (y la respuesta lista)", ""]
    for f in C1.FAQ:
        L += ["**%s**" % f["p"], "", f["r"], ""]
    L += ["## Preguntas de comprobación oral (no son de evaluación)",
          "Úselas durante la rotación por los equipos, a personas distintas y al azar.", ""]
    L += ["%d. %s" % (i, q) for i, q in enumerate(C1.ORALES, 1)]
    L += [
        "",
        "## Solución de la actividad (privada)",
        "`Kit docente/Clase %d/%s.docx` — resuelta sobre **%s**, que es el campo que produce las "
        "fichas más flojas: tener resuelto el caso difícil sirve para calificar los cuatro fáciles. "
        "**No proyectarla** antes de que los equipos trabajen."
        % (C1.CLASE_N, NOMBRE_SOL, C1.SOLUCION_CAMPO),
        "",
        "## Evaluación diagnóstica",
        "- Versión estudiante (respaldo si ExamLab no abre): `Clases/Clase %d - %s/%s.docx`"
        % (C1.CLASE_N, C1.SLUG, NOMBRE_DIAG),
        "- Clave y lectura docente (qué revela cada ítem y qué decisión cambia): "
        "`Kit docente/Clase %d/%s.docx`" % (C1.CLASE_N, NOMBRE_CLAVE),
        "",
        "## Capturas sugeridas",
        "- 📸 El muro de Padlet con las respuestas de entrada del grupo "
        "[[captura: muro-clase01.png | receta: 1) Al minuto 40, antes de contrastar, capture el "
        "muro completo.  2) Recorte cualquier nombre visible antes de guardar.  3) Guárdela como "
        "Kit docente/Clase 1/Capturas/muro-clase01.png.  4) Sirve como evidencia de participación "
        "del primer corte.]]",
        "- 📸 Una ficha del campo terminada, como referencia de nivel esperado "
        "[[captura: ficha-clase01.png | receta: 1) Con permiso del equipo, capture la ficha mejor "
        "resuelta.  2) Recorte nombres y correos.  3) Guárdela como Kit docente/Clase 1/Capturas/"
        "ficha-clase01.png.  4) Se puede proyectar en la sesión 2 como referencia, ya anonimizada.]]",
        "",
        "## Notas operativas",
        "- **Material común a los tres grupos.** Este guion y su deck no llevan fechas: sirven "
        "igual para SB141B (jueves), SB141C (martes tarde) y LB141F (martes noche).",
        "- Plataforma del diagnóstico: ExamLab (https://uniaj.examlab.workers.dev/). **No es la "
        "plataforma oficial de la UNIAJC**: es un canal del docente. La universidad no tiene "
        "campus virtual propio, así que todo lo demás va por la carpeta compartida del equipo.",
        "- Prohibido pedir cuentas de pago o tarjeta de crédito: todas las herramientas del curso "
        "son de plan gratuito permanente y funcionan desde el navegador.",
        "- **Las cinco salas de grupo se crean ANTES de empezar.** Abrirlas en vivo se come los "
        "17 min de la actividad. Se crean una sola vez y se reutilizan las 16 sesiones.",
        "- Revisar antes de citar la bibliografía: el microcurrículo referencia «IEEE (2014). "
        "Ethically Aligned Design», pero la iniciativa de IEEE que produjo ese documento publicó "
        "sus versiones a partir de 2016. Verifique la edición antes de pedirle al grupo que la "
        "busque; es material de la sesión 4, no de hoy.",
        "",
    ]
    return "\n".join(L)


# -------------------------------------------------------------------- solucion

def md_solucion():
    sol = C1.SOLUCION
    act = C1.ACTIVIDAD
    L = [
        "# Solución — Actividad Clase %d: %s" % (C1.CLASE_N, act["titulo"]),
        "",
        "> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni proyectar antes de que "
        "los equipos hayan trabajado.",
        "",
        "**Resumen:** la ficha de cinco bloques resuelta completa, con la escala de calificación "
        "bloque por bloque y lo que hay que buscar en los otros cuatro campos.",
        "",
        "> %s" % sol["por_que_ese"],
        "",
        "## Alineación con la actividad",
        "",
        "- Consigna del estudiante: `Clases/Clase %d - %s/%s.docx`"
        % (C1.CLASE_N, C1.SLUG, NOMBRE_ACTIVIDAD),
        "- Deck de la clase: `Clases/Clase %d - %s/Presentacion.pptx`" % (C1.CLASE_N, C1.SLUG),
        "- Duración: **%d min** de trabajo + **%d min** de exposición por equipo."
        % (act["duracion_min"], act["exposicion_min"]),
        "- Entregable: %s" % act["entregable"],
        "- Peso: hace parte de «Exposiciones de equipo y actividades en clase» del **Corte 1 (30 %)**.",
        "",
        "| Bloque | Puntos | Qué decide la nota |",
        "|---|---|---|",
    ]
    for b, (crit, peso, _) in zip(sol["bloques"], C1.RUBRICA):
        L.append("| %s | %d | %s |" % (b["clave"], peso, crit))
    L += [
        "| **Total** | **100** | Sobre la ficha del equipo, no sobre cada integrante. |",
        "",
        "---",
        "",
    ]
    for b, (crit, peso, _) in zip(sol["bloques"], C1.RUBRICA):
        L += [
            "## Bloque · %s · %d pts" % (b["clave"], peso),
            "",
            "### Respuesta esperada",
            "",
            b["respuesta"],
            "",
            "### Cómo calificar",
            "",
        ]
        L += ["- %s" % x for x in b["como_calificar"]]
        L += ["", "---", ""]

    L += ["## Qué buscar en los otros cuatro campos", ""]
    for o in sol["otros_campos"]:
        L += ["### %s" % o["campo"], "", o["esperable"], ""]

    L += [
        "## Errores frecuentes (los mismos que corregir en la rotación)",
        "",
    ]
    L += ["- %s" % e for e in C1.ERRORES]
    L += [
        "",
        "## Cierre y continuidad",
        "",
        sol["cierre"],
        "",
        "**Guarde las cinco fichas.** En la sesión 6 (cierre del Corte 1, «Análisis de problemas "
        "tecnológicos del entorno») el bloque «problema del entorno» de las cinco fichas es el "
        "material de entrada: cada equipo elige de ahí el problema de su proyecto. Sin las fichas "
        "de hoy, esa sesión arranca de cero.",
        "",
    ]
    return "\n".join(L)


# ------------------------------------------------------------------ diagnostico

def _items():
    for b in C1.DIAGNOSTICO["bloques"]:
        for it in b["items"]:
            yield b, it


def md_diagnostico(clave=False):
    d = C1.DIAGNOSTICO
    c = D.curso()
    L = [
        "# %s%s" % (d["titulo"], " — CLAVE DOCENTE" if clave else ""),
        "",
    ]
    if clave:
        L += [
            "> **DOCUMENTO DOCENTE — PRIVADO.** Clave de los ítems cerrados y, para cada uno, "
            "**qué decisión del curso cambia** según cómo responda el grupo. Eso último es lo que "
            "hace que el diagnóstico valga la pena: si no cambia nada, no había que aplicarlo.",
            "",
        ]
    L += [
        "- Asignatura: %s (%s) · Clase %d · %s"
        % (c["nombre_acentos"], c["codigo"], C1.CLASE_N, C1.TITULO),
        "- Duración: **%d min** · **%d preguntas**" % (d["duracion_min"], sum(1 for _ in _items())),
        "- **%s**" % d["nota"],
        "- Aplicable a los tres grupos (SB141B, SB141C, LB141F). Sin fechas.",
        "",
        "## Instrucciones",
        "",
    ]
    L += ["%d. %s" % (i, x) for i, x in enumerate(d["instrucciones"], 1)]
    if not clave:
        L += [
            "",
            "**Nombre:** ______________________________________  **Grupo:** ____________",
            "",
        ]
    L += [""]

    bloque_actual = None
    for b, it in _items():
        if b["nombre"] != bloque_actual:
            bloque_actual = b["nombre"]
            L += ["## %s" % bloque_actual, ""]
        L += ["### %d. %s" % (it["n"], it["pregunta"]), ""]
        if it["tipo"] == "abierta":
            if clave:
                L += ["(Pregunta abierta: no tiene clave.)", ""]
            else:
                L += ["_______________________________________________________________________",
                      "", "_______________________________________________________________________",
                      ""]
        else:
            if it["tipo"] == "cerrada_multi":
                L += ["**Marque todas las que apliquen.**", ""]
            for j, op in enumerate(it["opciones"]):
                marca = ""
                if clave and it.get("clave") == LETRAS[j]:
                    marca = "  ✅ **CORRECTA**"
                L.append("- **%s)** %s%s" % (LETRAS[j], op, marca))
            L += [""]
        if clave:
            L += ["> **Qué revela y qué decide:** %s" % it["revela"], ""]

    if clave:
        L += [
            "## Cómo se lee el resultado (10 min después de clase)",
            "",
            "No hay nota que calcular. Lo que hay que producir son **cinco conteos**, y cada uno "
            "cambia una decisión concreta:",
            "",
            "| Conteo | Decisión que cambia |",
            "|---|---|",
            "| Cuántos fallaron los ítems 1, 2 y 3 | Si más de la mitad falla, la sesión 3 "
            "(análisis de caso) necesita más tiempo en el planteamiento del problema y menos en "
            "la herramienta de IA. |",
            "| Cuántos marcaron «ninguna» en el ítem 6 | Si hay varios, la sesión 2 arranca con "
            "5 min de manejo de diagrams.net en vez de darlo por sabido. |",
            "| Cuántos fallaron el ítem 8 | Casi todos fallan. Confirma que la sesión 5 "
            "(sostenibilidad) tiene que empezar por «el software se paga en kilovatios». |",
            "| Cuántos marcaron (c) en el ítem 9 | «Arreglarlo en silencio» es la respuesta más "
            "común y la más productiva para abrir la sesión 4: el debate no es si estuvo mal "
            "hacerlo, sino que los afectados nunca supieron que sus datos estuvieron expuestos. |",
            "| Ítems 11, 12 y 13, en conteo | Deciden dos cosas hoy mismo: si el trabajo "
            "independiente tiene que poder hacerse desde el celular, y cómo se mezclan los cinco "
            "equipos para no dejar juntas a las personas sin computador ni a las que trabajan más "
            "de 20 horas. |",
            "",
            "**Guarde las respuestas del ítem 4** (un problema de su entorno). Es la lista de "
            "candidatos al proyecto del semestre y es el insumo de la sesión 6.",
            "",
            "**Hable al final de la clase con quien haya respondido en el ítem 5 o el 10 que espera "
            "aprender a programar.** Es el perfil con más riesgo de retiro en las primeras semanas, "
            "y basta decirle en qué curso del programa sí aprende eso y por qué este es el que va "
            "primero.",
            "",
        ]
    return "\n".join(L)


# -------------------------------------------------------------------- actividad

def md_actividad():
    act = C1.ACTIVIDAD
    c = D.curso()
    L = [
        "# %s — Clase %d" % (act["titulo"], C1.CLASE_N),
        "",
        "- Asignatura: %s (%s)" % (c["nombre_acentos"], c["codigo"]),
        "- **%d minutos en equipo · %d minutos de exposición**"
        % (act["duracion_min"], act["exposicion_min"]),
        "- Entregable: %s" % act["entregable"],
        "",
        "## Qué hay que hacer",
        "",
        act["consigna"],
        "",
        "> **El campo de cada equipo no se elige:** %s" % act["reparto"],
        "",
        "## La ficha: cinco bloques",
        "",
        "| Bloque | Qué escribir | Está bien cuando… |",
        "|---|---|---|",
    ]
    for b in act["bloques"]:
        L.append("| **%s** | %s | %s |" % (b["clave"], b["pide"], b["check"]))
    L += [
        "",
        "## Cómo se califica",
        "",
        "| Criterio | Peso |",
        "|---|---|",
    ]
    for crit, peso, _ in C1.RUBRICA:
        L.append("| %s | %d%% |" % (crit, peso))
    L += [
        "",
        "> El bloque **PROBLEMA DEL ENTORNO** es el que más pesa porque es la semilla del proyecto "
        "del semestre: en la sesión 6 cada equipo elige de ahí el problema con el que va a trabajar "
        "hasta diciembre. Escríbanlo con quién lo sufre (un rol concreto, no «los usuarios») y una "
        "cifra, aunque sea estimada.",
        "",
        "## La exposición: 3 minutos",
        "",
        "| Tiempo | Qué se dice |",
        "|---|---|",
        "| 30 s | El campo: qué es y de qué se ocupa, en sus palabras. |",
        "| 60 s | El problema del entorno: quién lo sufre y la cifra. |",
        "| 30 s | La confusión frecuente y por qué es falsa. |",
        "| 60 s | Si se hace mal: a quién le pasa y qué pierde. |",
        "",
        "**Habla el vocero de hoy** (rota cada sesión). El cronómetro se proyecta y **se corta a los "
        "3 minutos**. No lean la ficha completa en voz alta: no cabe.",
        "",
        "## Antes de exponer",
        "",
        "- [ ] Los cinco bloques están completos.",
        "- [ ] El problema del entorno tiene un rol concreto y una cifra.",
        "- [ ] El enlace de la carpeta del equipo, **con permiso de lectura para el docente**, ya "
        "está entregado. Buscar el archivo con el cronómetro corriendo se come el turno.",
        "- [ ] Está claro quién es el vocero.",
        "",
        "> **Si se cae la conexión de alguien:** %s" % act["plan_b"],
        "",
        "## Sin datos personales de terceros",
        "",
        "Si el problema del entorno que eligieron involucra a personas concretas (compañeros de "
        "trabajo, clientes, vecinos), **no escriban sus nombres, cédulas, teléfonos ni suban sus "
        "fotos**. Usen el rol: «la dueña de la papelería», «el auxiliar de la biblioteca». Es una "
        "regla del curso y es la primera vez que se aplica el criterio ético que se evalúa en la "
        "sesión 4.",
        "",
    ]
    return "\n".join(L)


# ----------------------------------------------------------------------- capturas

README_CAPT = """Capturas de la Clase 1 — Introduccion a la Ingenieria (FI300101)
================================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Pendiente: muro-clase01.png — el muro de Padlet con las respuestas de entrada
  1. Al minuto 40, antes de contrastar con los cinco campos, capture el muro completo.
  2. Recorte cualquier nombre visible antes de guardar.
  3. Guardela aqui como muro-clase01.png.
  4. Sirve como evidencia de participacion del primer corte.

Pendiente: ficha-clase01.png — una ficha del campo terminada
  1. Con permiso del equipo, capture la ficha mejor resuelta de la sesion.
  2. Recorte nombres y correos: no se versiona nada con datos personales.
  3. Guardela aqui como ficha-clase01.png.
  4. Se puede proyectar en la sesion 2 como referencia de nivel esperado, ya anonimizada.

Despues de agregar una imagen, regenerar el guion:
    python config/slides/build_uniajc_intro_ing_clase1.py
"""


# --------------------------------------------------------------------- orquesta

def _escribir(md_dir, nombre, texto, docx=True):
    os.makedirs(md_dir, exist_ok=True)
    md = os.path.join(md_dir, nombre + ".md")
    with open(md, "w", encoding="utf-8") as fh:
        fh.write(texto)
    salidas = [md]
    if docx:
        out = os.path.join(md_dir, nombre + ".docx")
        convert(md, out)
        salidas.append(out)
    return salidas


def build():
    hechos = []
    pptx, titulos = build_pptx()
    hechos.append(pptx)

    os.makedirs(DIR_CAPT, exist_ok=True)
    with open(os.path.join(DIR_CAPT, "README.txt"), "w", encoding="utf-8") as fh:
        fh.write(README_CAPT)
    hechos.append(os.path.join(DIR_CAPT, "README.txt"))

    # Guion y solucion: kit docente (md + docx)
    hechos += _escribir(DIR_KIT, NOMBRE_GUION, _resolver(md_guion(titulos), titulos))
    hechos += _escribir(DIR_KIT, NOMBRE_SOL, md_solucion())
    hechos += _escribir(DIR_KIT, NOMBRE_CLAVE, md_diagnostico(clave=True))

    # Estudiante: solo .docx en Clases/ (el .md queda en el kit para poder regenerar)
    for nombre, texto in ((NOMBRE_ACTIVIDAD, md_actividad()),
                          (NOMBRE_DIAG, md_diagnostico(clave=False))):
        md = os.path.join(DIR_KIT, nombre + ".md")
        os.makedirs(DIR_KIT, exist_ok=True)
        with open(md, "w", encoding="utf-8") as fh:
            fh.write(texto)
        out = os.path.join(DIR_CLASE, nombre + ".docx")
        convert(md, out)
        hechos += [md, out]

    for h in hechos:
        print("OK ->", os.path.relpath(h, ROOT))
    return hechos


if __name__ == "__main__":
    build()
    print("DONE")
