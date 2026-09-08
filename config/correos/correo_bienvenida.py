# -*- coding: utf-8 -*-
"""Plantilla del correo de bienvenida. Sirve para cualquier curso y cualquier periodo.

Qué resuelve
------------
Cada curso nuevo necesita el mismo correo: cuándo nos vemos, qué fechas anotar, cómo entrar a
la plataforma y qué necesito del grupo. Escribirlo a mano por curso garantiza que a los seis
meses cinco correos digan cinco cosas distintas del mismo ExamLab. Aquí vive **el texto**; el
curso solo aporta **los datos**.

Cómo se usa
-----------
Se arma un `dict` con los datos del curso y se llama a `construir()`, que devuelve el
Markdown, o a `escribir()`, que lo guarda:

    import correo_bienvenida as cb

    cb.escribir({
        "curso": "Estructuras de Datos",
        "codigo": "FI303210",
        "grupo": "341A",
        "periodo": "2027-1",
        "dia": "Lunes",
        "horario": "18:00 – 20:00",
        "inicio_efectivo": "18:10",
        "primera": "02/02/2027",
        "ultima": "10/05/2027",
        "linea_calendario": "15 sesiones de lunes, una por semana, de 120 min.",
        "plataforma_encuentro": "Google Meet",
        "fechas_clave": [
            ("**Primera sesión** (Lunes)", "**02/02/2027**", "Sesión 1 · presentación y diagnóstico"),
            ("Parcial 1", "09/03/2027", "Sesión 6 · en ExamLab"),
            ("Última sesión (Lunes)", "**10/05/2027**", "Sesión 15 · sustentación del proyecto"),
        ],
    }, ruta)

Solo `curso`, `codigo`, `periodo`, `dia`, `horario`, `primera` y `ultima` son obligatorios;
todo lo demás tiene un valor por omisión razonable o se omite del correo si no se pasa. La
lista completa de campos está en `CAMPOS`, y `python correo_bienvenida.py` imprime un correo
de ejemplo para ver la forma sin tener que cablear nada.

Qué NO va en este correo
------------------------
La dinámica de la sesión (el minuto a minuto, cómo se arman los equipos), el stack de
herramientas con su uso, y las reglas de aula. Eso vive en el Acuerdo Pedagógico, en el Plan
de curso y en el LEEME del curso. En el correo solo compite con lo que el estudiante tiene
que hacer antes del primer encuentro, que es lo único que este correo intenta lograr.

Tampoco va un enlace fijo de la sala de la sesión: cada encuentro tiene el suyo y se publica
en la plataforma. Ni la frase de que la universidad no tiene campus virtual propio — al
estudiante se le dice que ExamLab «no es una plataforma oficial de la UNIAJC» y ahí se para.
"""
from __future__ import annotations

import os

#: URLs canónicas de ExamLab. Si cambian, cambian **aquí** y se regeneran los correos.
EXAMLAB_URL = "https://uniaj.examlab.workers.dev"
EXAMLAB_MANUAL = ("https://uxxpzfsfcnqiwwdxoelm.supabase.co/storage/v1/object/"
                  "public/help-docs/manual-estudiante.pdf")
EXAMLAB_VIDEO = ("https://uxxpzfsfcnqiwwdxoelm.supabase.co/storage/v1/object/"
                 "public/help-videos/serie-estudiante.mp4")

DOCENTE = "Julian Andres Castaño"
CORREO_DOCENTE = "julianacastano@profesores.uniajc.edu.co"
CREDENCIALES = "Ingeniero de Sistemas · Candidato a MsC en IA"

#: Todos los campos del `spec`, para no tener que leer el código.
CAMPOS = """
OBLIGATORIOS
  curso                 Nombre con tildes: "Introducción a la Ingeniería"
  codigo                "FI300101"
  periodo               "2026-2"
  dia                   "Martes" (con mayúscula; se minusculiza donde toca)
  horario               "18:30 – 20:00"
  primera               Fecha de la primera sesión, ya formateada: "08/09/2026"
  ultima                Fecha de la última sesión: "17/11/2026"

OPCIONALES — identidad
  grupo                 "LB141F". Si falta, no se menciona el grupo en ningún sitio.
  nota_grupos           Aviso de que hay un correo por grupo. Solo si el curso tiene varios.
  docente / correo_docente / credenciales    Por omisión, los de este módulo.

OPCIONALES — encuadre
  modalidad             "Virtual" (por omisión)
  plataforma_encuentro  "Google Meet" (por omisión) o "Microsoft Teams"
  inicio_efectivo       "18:40" — la hora a la que se arranca de verdad. Si falta, se omite.
  linea_calendario      Una frase sobre las sesiones. Si falta, se omite la viñeta.
  linea_modalidad_sesion  Si falta, se arma con `modalidad` y `plataforma_encuentro`.

OPCIONALES — cuerpo
  fechas_clave          Lista de (hito, fecha, detalle) para la tabla. Si falta, no hay tabla.
  carpetas_drive        {"clases": url, "grabadas": url} — cualquiera de las dos puede faltar.
  examlab               Dict, ver abajo. Si es None, no hay bloque de ExamLab.
  nota_herramientas     True (por omisión) añade la línea de "gratis, sin tarjeta de crédito".
  vocero                True (por omisión) pide el WhatsApp del vocero.
  parrafos_extra        Lista de párrafos en Markdown, justo antes del cierre.

examlab = {
  "que_hay_ahi"    Lista de bullets de lo que se hace en la plataforma. Tiene un
                   valor por omisión genérico.
  "contrasena"     "Temporal#123" si las cuentas ya están creadas; None deja la
                   línea en blanco para que el docente la escriba.
  "cuentas_creadas"  True añade "la cuenta ya está creada, no hay que registrarse".
  "encuesta"       URL de la encuesta de inicio de semestre. Si falta, no se menciona.
}
"""


def _b(x):
    """Marca en negrita si no lo está ya."""
    s = str(x)
    return s if s.startswith("**") else "**%s**" % s


def _cabecera(s):
    curso, codigo, periodo = s["curso"], s["codigo"], s["periodo"]
    grupo = s.get("grupo")
    dia = s["dia"].lower()
    ident = "%s · %s" % (codigo, grupo) if grupo else codigo
    titulo = "# Correo de bienvenida — %s%s · %s" % (
        curso, " · " + grupo if grupo else "", periodo)
    L = [
        titulo,
        "",
        "**Para:** estudiantes del grupo %s" % grupo if grupo else "**Para:** estudiantes del curso",
        "**De:** %s · %s" % (s.get("docente", DOCENTE), s.get("correo_docente", CORREO_DOCENTE)),
        "**Asunto sugerido:** Bienvenida · %s (%s) · %s · %s · %s %s"
        % (curso, ident, periodo, s.get("modalidad", "Virtual"), dia[:3], s["horario"]),
        "",
    ]
    if s.get("nota_grupos"):
        L += ["> " + s["nota_grupos"], ""]
    L += ["---", ""]
    return L


def _encuadre(s):
    curso, codigo, periodo = s["curso"], s["codigo"], s["periodo"]
    grupo = s.get("grupo")
    dia = s["dia"].lower()
    modalidad = s.get("modalidad", "Virtual")
    plataforma = s.get("plataforma_encuentro", "Google Meet")

    quien = "código **%s**%s" % (codigo, ", grupo **%s**" % grupo if grupo else "")
    L = [
        "Estimados estudiantes:",
        "",
        "Les doy la bienvenida al curso **%s** (%s) del periodo **%s** (del **%s** al "
        "**%s**)." % (curso, quien, periodo, s["primera"], s["ultima"]),
        "",
        "- **Modalidad:** %s" % modalidad,
        "- **Modalidad por sesión:** %s" % s.get(
            "linea_modalidad_sesion",
            "todas las sesiones son **%s síncrona** por **%s**." % (modalidad.lower(), plataforma)),
    ]
    if s.get("linea_calendario"):
        L.append("- **Calendario:** %s" % s["linea_calendario"])
    horario = "- **Horario:** %s **%s**" % (dia, s["horario"])
    if s.get("inicio_efectivo"):
        horario += " (inicio práctico de clase: **%s**)" % s["inicio_efectivo"]
    L += [
        horario,
        "- **Docente:** %s · %s" % (s.get("docente", DOCENTE),
                                    s.get("correo_docente", CORREO_DOCENTE)),
        "",
    ]
    return L


def _fechas_clave(s):
    filas = s.get("fechas_clave")
    if not filas:
        return []
    L = ["### Fechas clave", "", "| Hito | Fecha | Detalle |", "|---|---|---|"]
    L += ["| %s | %s | %s |" % (a, b, c) for a, b, c in filas]
    L.append("")
    return L


def _carpetas(s):
    c = s.get("carpetas_drive") or {}
    if not c:
        return []
    L = ["### Carpetas del curso en Drive", ""]
    if c.get("clases"):
        L.append("- **Clases** (Presentación del Curso, diapositivas y talleres): %s"
                 % c["clases"])
    if c.get("grabadas"):
        L.append("- **Clases grabadas** (queda la grabación de cada sesión sincrónica): %s"
                 % c["grabadas"])
    if c.get("grabadas"):
        L += ["",
              "Las grabaciones se suben después de cada sesión. Sirven para repasar, y sobre "
              "todo si faltaron: **no reemplazan la asistencia**, que se toma en la sesión."]
    L.append("")
    return L


DEFAULT_QUE_HAY = [
    "**Asistencia**",
    "**Talleres** (se resuelven y se entregan dentro de la plataforma)",
    "**Quices y evaluaciones**",
    "**Entrega del proyecto**",
]


def _examlab(s):
    e = s.get("examlab")
    if e is None:
        return []
    e = dict(e)
    grupo = s.get("grupo")
    plataforma = s.get("plataforma_encuentro", "Google Meet")

    L = [
        "### Plataforma del curso — ExamLab",
        "",
        "Trabajaremos en **ExamLab**: %s" % EXAMLAB_URL,
        "",
    ]
    que = e.get("que_hay_ahi", DEFAULT_QUE_HAY)
    if isinstance(que, str):
        L += ["**No es una plataforma oficial de la UNIAJC**, pero es donde se desarrolla "
              "todo lo del curso: " + que, ""]
    else:
        L += ["**No es una plataforma oficial de la UNIAJC**, pero es donde se desarrolla "
              "todo lo evaluable del curso:", ""]
        L += ["- " + x for x in que]
        L.append("")
    # Donde está el enlace de la sesión. Es lo que reemplaza al párrafo que antes explicaba
    # que no llega invitación de Calendar: el dato que el estudiante necesita es este.
    L += ["Y ahí mismo publico el **enlace de %s de cada sesión**, antes de que empiece: "
          "**cada sesión tiene el suyo**, así que el de la semana pasada ya no sirve."
          % plataforma, ""]
    L += ["**Por favor verifiquen que pueden entrar ANTES de la primera sesión**, no ese "
          "mismo día:", "",
          "| | |", "|---|---|",
          "| **Dirección** | %s |" % EXAMLAB_URL,
          "| **Usuario** | Su correo institucional `@estudiante.uniajc.edu.co` |"]
    if e.get("contrasena"):
        L.append("| **Contraseña temporal** | `%s` — la aplicación les pide cambiarla al "
                 "entrar |" % e["contrasena"])
    else:
        L.append("| **Contraseña temporal** | ________________________ — cámbienla al entrar |")
    L.append("")
    if e.get("cuentas_creadas"):
        L += ["La cuenta ya está creada%s: no hay que registrarse. Si el correo institucional "
              "todavía no les llegó de Registro Académico, escríbanme y les habilito el "
              "acceso." % (" y ya están matriculados en el grupo **%s**" % grupo if grupo else ""),
              ""]
    else:
        L += ["Si no logran entrar, escríbanme respondiendo este correo **antes de la primera "
              "sesión**: resolverlo en clase nos quita tiempo de clase.", ""]
    L += ["Material de apoyo para usar la plataforma:", "",
          "- **Manual del estudiante (PDF):** " + EXAMLAB_MANUAL,
          "- **Todas las funcionalidades (video):** " + EXAMLAB_VIDEO, ""]
    if e.get("encuesta"):
        L += ["#### Encuesta de inicio de semestre", "",
              "Y una vez dentro, **llenen la encuesta de inicio de semestre**, también en "
              "ExamLab:", "",
              "> " + e["encuesta"], "",
              "**Antes de la primera sesión, por favor.** Es corta, y con lo que respondan "
              "ajusto el arranque del curso. Si la contestan después, la primera sesión ya "
              "pasó y deja de servir para eso.", ""]
    return L


def _cierre(s):
    L = []
    if s.get("nota_herramientas", True):
        L += ["Todas las herramientas del curso son **gratis y desde el navegador**: no hay "
              "que instalar ni pagar nada, y **nunca les voy a pedir una tarjeta de "
              "crédito**. Si una herramienta la pide, no es la que usamos.", ""]
    for p in s.get("parrafos_extra") or []:
        L += [p, ""]
    if s.get("vocero", True):
        plataforma = s.get("plataforma_encuentro", "Google Meet")
        L += ["**Una cosa que necesito de ustedes:** que el **vocero del grupo** me "
              "**responda este correo con su número de WhatsApp**. Lo uso solo para avisos "
              "urgentes del curso —que el enlace de %s falle, una caída de la plataforma el "
              "día de una evaluación— y para tener un canal directo con el grupo. Si todavía "
              "no han elegido vocero, lo definimos en la primera sesión y me escribe "
              "después." % plataforma, ""]
    L += ["Nos vemos el %s. Cualquier duda, respondiendo a este correo." % s["primera"],
          "",
          "Cordialmente,",
          "",
          s.get("docente", DOCENTE)]
    if s.get("credenciales", CREDENCIALES):
        L.append(s.get("credenciales", CREDENCIALES))
    L += [s.get("correo_docente", CORREO_DOCENTE), ""]
    return L


OBLIGATORIOS = ("curso", "codigo", "periodo", "dia", "horario", "primera", "ultima")


def construir(spec: dict) -> str:
    """El correo entero en Markdown."""
    faltan = [k for k in OBLIGATORIOS if not spec.get(k)]
    if faltan:
        raise ValueError("faltan campos obligatorios del correo: %s\n%s"
                         % (", ".join(faltan), CAMPOS))
    L = (_cabecera(spec) + _encuadre(spec) + _fechas_clave(spec)
         + _carpetas(spec) + _examlab(spec) + _cierre(spec))
    return "\n".join(L)


def escribir(spec: dict, ruta: str) -> str:
    """Guarda el correo y devuelve la ruta."""
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(construir(spec))
    return ruta


EJEMPLO = {
    "curso": "Estructuras de Datos",
    "codigo": "FI303210",
    "grupo": "341A",
    "periodo": "2027-1",
    "dia": "Lunes",
    "horario": "18:00 – 20:00",
    "inicio_efectivo": "18:10",
    "primera": "01/02/2027",
    "ultima": "10/05/2027",
    "linea_calendario": "15 sesiones de lunes, una por semana, de 120 min, que cubren los "
                        "15 temas del curso. Ningún festivo cae en lunes: **no hay semanas "
                        "autónomas**.",
    "plataforma_encuentro": "Google Meet",
    "fechas_clave": [
        ("**Primera sesión** (Lunes)", "**01/02/2027**",
         "Sesión 1 · presentación del curso y diagnóstico **sin nota**"),
        ("Parcial 1", "08/03/2027", "Sesión 6 · en ExamLab"),
        ("Última sesión (Lunes)", "**10/05/2027**", "Sesión 15 · sustentación del proyecto"),
    ],
    "carpetas_drive": {
        "clases": "https://drive.google.com/drive/folders/EJEMPLO_CLASES",
        "grabadas": "https://drive.google.com/drive/folders/EJEMPLO_GRABADAS",
    },
    "examlab": {"contrasena": None, "encuesta": None},
}


if __name__ == "__main__":
    print(construir(EJEMPLO))
