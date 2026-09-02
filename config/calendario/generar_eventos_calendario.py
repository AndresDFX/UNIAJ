# -*- coding: utf-8 -*-
"""Genera los eventos de calendario del semestre y las herramientas de asistencia.

Los eventos son **bloques del calendario personal del docente**: no llevan invitados y
nada de lo que sale de aquí envía un correo. El estudiante no entra por el calendario;
el docente le comparte el enlace de la sesión por el canal que use con el grupo.

Los **datos de estudiantes** siguen haciendo falta, pero solo para las herramientas de
asistencia (nómina y planilla). Ya no alimentan ningún evento.

Entradas
--------
1. `config/calendario/semestre_2026_2.json` — fuente de verdad de 4 de los 7 cursos
   (13 sesiones, fechas, tipo, parciales, sesiones dobles, sustentación).
2. `config/calendario/introduccion_ingenieria_2026_2.json` — los 3 GRUPOS de
   Introducción a la Ingeniería (FI300101), 16 sesiones de 90 min, con fechas que llegan a
   diciembre. Vive aparte a propósito (ver su `_comentario`) y NO se fusiona: se adapta con
   `cursos_introduccion_ingenieria()` de `generar_apps_script_encuentros.py`, que es el
   MISMO adaptador que usa el Apps Script. Se reusa en vez de copiarlo porque el título del
   evento es su identidad: si los dos generadores lo escribieran distinto, el evento del
   `.ics` y el que crea el Apps Script no se reconocerían y quedarían duplicados.
3. El listado de estudiantes de cada curso, descargado del sistema académico.
   Se detecta automáticamente y se aceptan DOS formatos:

   a) **Academusoft "Lista de Alumnos por Grupo"** (`LISTA_DE_ALUMNOS_POR_GRUPOS*.xls`,
      `<grupo> - <MATERIA>.xls`): fila 4 trae `FI###### MATERIA`, grupo y total;
      fila 5 es el encabezado; los estudiantes arrancan en la fila 6 con
      `Tipo de Documento · Identificación · Nombre · Repitente · Institucional`.
   b) **"Detalles de Cuenta"** (`<grupo> - <MATERIA>.xlsx`): encabezado en la fila 2 con
      `DOCUM · NOMBRE · CORREO · INSTITUCIONAL_ESTUDIANTE · COD_MATE · GRUPO · …`.

   Se valida que el código de materia del archivo coincida con el del curso en el JSON;
   si no coincide, el curso se omite (evita cruzar nóminas entre asignaturas). Cuando
   VARIOS cursos comparten código —los 3 grupos de FI300101— el código solo no distingue
   un grupo de otro, así que además se exige que el nombre del archivo diga el grupo; si no
   lo dice, se rechaza en vez de arriesgar la planilla de asistencia de otro grupo.

Salidas
-------
* `<Curso>/Plan curso/2026-2/eventos_calendario_2026-2[ - <grupo>].csv` — **sin datos
  personales**. Formato de importación de Google Calendar (Subject, Start Date, …).
  Versionable. Lleva el grupo en el nombre cuando varios grupos comparten carpeta.
* `<Curso>/Plan curso/2026-2/_privado/`:
    - `bloques_<curso>.ics`      · un bloque por sesión, **sin invitados** (antes se llamaba
      `invitaciones_<curso>.ics` y metía a cada estudiante como ATTENDEE). Sin datos
      personales; se queda en `_privado/` por convención del proyecto.
    - `nomina_<curso>.csv`       · **CON datos personales** (documento, nombre, correo, origen)
    - `asistencia_<curso>.csv`   · **CON datos personales**: planilla estudiantes × sesiones
    - `pendientes_correo_<curso>.csv` · solo si alguien no trae correo institucional
  La regla `_privado/` está en .gitignore: nada de esa carpeta se versiona.

Entrada opcional que mantiene el docente, en la misma carpeta privada:
`correos_manuales.csv` (`documento,correo,nota`) para completar los correos que el export
academico no trae. Se cruza por documento.

El `.ics` y el CSV son el camino manual. El recomendado sigue siendo el Apps Script de
`generar_apps_script_encuentros.py`, por una razón que no tiene que ver con invitaciones:
es el único que le da a **cada sesión su propia sala de Meet**. Procedimiento: carpeta
`Manuales/` en la raíz.

Uso
---
    python config/calendario/generar_eventos_calendario.py

Requisitos: `xlrd` (para .xls) y `openpyxl` (para .xlsx).

Nota de privacidad: este script NO imprime nombres ni correos en consola, solo conteos.
Los archivos con nómina quedan fuera de git a propósito.
"""
from __future__ import annotations

import csv
import glob
import io
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
JSON_PATH = Path(__file__).with_name("semestre_2026_2.json")
PERIODO_DIR = "2026-2"


def privado_de(meta: dict) -> Path:
    """Carpeta privada del curso: todo lo del curso vive en la carpeta del curso.

    Antes estas salidas se juntaban en config/calendario/_privado_<periodo>/, lo que
    obligaba al docente a salir de la carpeta de su curso para buscar la nomina o el
    .ics. Ahora cada curso tiene su `Plan curso/<periodo>/_privado/`, ignorado por git
    porque lleva datos personales.
    """
    return ROOT / meta["folder"] / "Plan curso" / PERIODO_DIR / "_privado"

DATA = json.loads(JSON_PATH.read_text(encoding="utf-8"))
DOCENTE = DATA["docente"]["nombre_completo"]
CORREO_DOCENTE = DATA["docente"]["correo"]

TZID = "America/Bogota"
UTC_OFFSET = "-0500"  # Colombia no tiene horario de verano

TIPO_ETIQUETA = {
    "presencial": "Presencial",   # sin uso en 2026-2 (modalidad Virtual)
    "virtual": "Virtual sincrónica",
    "autonoma": "Autónoma (festivo)",
    # `introduccion_ingenieria_2026_2.json` llama `autonoma_festivo` a lo que este modulo
    # llama `autonoma`. El adaptador lo traduce antes de llegar aqui; el alias esta para que,
    # si algun dia entra sin traducir, la etiqueta salga en castellano y no como slug crudo.
    "autonoma_festivo": "Autónoma (festivo)",
    "sustentacion": "Sustentaciones del Proyecto Integrador",
}

# Los `tema` del JSON son ASCII. Estos eventos los ve el estudiante, así que se
# restituyen las tildes con la misma tabla del generador de calendario (no se duplica).
try:
    from generar_semestre_2026_2 import tema_txt as _tema_txt
except Exception:  # pragma: no cover - fallback si cambia el módulo vecino
    def _tema_txt(cl: dict) -> str:
        return cl["tema"]


# ----------------------------------------------------------------- nómina

def _norm(s) -> str:
    return re.sub(r"\s+", " ", str(s or "")).strip()


def _leer_xls(path: Path) -> list[list[str]]:
    import xlrd

    sh = xlrd.open_workbook(str(path)).sheets()[0]
    return [[_norm(sh.cell_value(r, c)) for c in range(sh.ncols)] for r in range(sh.nrows)]


def _leer_xlsx(path: Path) -> list[list[str]]:
    import openpyxl

    sh = openpyxl.load_workbook(str(path), data_only=True).worksheets[0]
    return [[_norm(c.value) for c in row] for row in sh.iter_rows()]


def leer_filas(path: Path) -> list[list[str]]:
    return _leer_xlsx(path) if path.suffix.lower() == ".xlsx" else _leer_xls(path)


def parse_academusoft(filas: list[list[str]]) -> dict | None:
    """Formato 'Lista de Alumnos por Grupo'."""
    hdr = next((i for i, f in enumerate(filas)
                if f and f[0].lower().startswith("tipo de documento")), None)
    if hdr is None:
        return None
    meta_row = next((f for f in filas[:hdr] if f and re.match(r"^FI\d{6}", f[0])), None)
    codigo = re.match(r"^(FI\d{6})", meta_row[0]).group(1) if meta_row else None
    reporte = next((f[0] for f in filas[:hdr] if f and f[0].startswith("Fecha Reporte")), "")
    estudiantes = []
    for f in filas[hdr + 1:]:
        if len(f) < 5 or not f[1] or not f[2]:
            continue
        estudiantes.append({
            "documento": f[1],
            "nombre": f[2],
            "correo": f[4],
            "repitente": (f[3] or "").upper() == "SI",
        })
    return {"codigo": codigo, "estudiantes": estudiantes,
            "reporte": reporte.replace("Fecha Reporte:", "").strip()}


def parse_detalles_cuenta(filas: list[list[str]]) -> dict | None:
    """Formato 'Detalles de Cuenta' (encabezado con DOCUM / NOMBRE / COD_MATE)."""
    hdr = next((i for i, f in enumerate(filas) if "DOCUM" in f and "NOMBRE" in f), None)
    if hdr is None:
        return None
    cols = {name: i for i, name in enumerate(filas[hdr]) if name}
    i_doc, i_nom = cols.get("DOCUM"), cols.get("NOMBRE")
    i_mail = cols.get("INSTITUCIONAL_ESTUDIANTE", cols.get("CORREO"))
    i_cod = cols.get("COD_MATE")
    estudiantes, codigo = [], None
    for f in filas[hdr + 1:]:
        if i_doc is None or len(f) <= i_doc or not f[i_doc]:
            continue
        if i_cod is not None and len(f) > i_cod and f[i_cod]:
            codigo = f[i_cod]
        estudiantes.append({
            "documento": f[i_doc],
            "nombre": f[i_nom] if i_nom is not None and len(f) > i_nom else "",
            "correo": f[i_mail] if i_mail is not None and len(f) > i_mail else "",
            "repitente": False,
        })
    return {"codigo": codigo, "estudiantes": estudiantes, "reporte": ""}


PERIODO = DATA["periodo"]  # "2026-2"


def _es_de_otro_periodo(p: Path) -> bool:
    """True si la ruta cuelga de una carpeta de periodo distinta a la vigente.

    Programación II y Seminario conservan la nómina de su oferta anterior en
    `Plan curso/2026-1/`. Esa nómina NO debe usarse para los eventos de 2026-2.
    """
    partes = {x.lower() for x in p.parts}
    return any(
        re.fullmatch(r"20\d{2}-\d", x) and x != PERIODO.lower()
        for x in partes
    )


def buscar_listado(carpeta: Path, grupo: str) -> list[Path]:
    """Candidatos, del más específico/reciente al más genérico.

    Se descartan los que estén en una carpeta de periodo anterior.
    """
    pats = [
        f"{carpeta}/**/LISTA_DE_ALUMNOS*.xls*",
        f"{carpeta}/{grupo} - *.xls",
        f"{carpeta}/{grupo} - *.xlsx",
        f"{carpeta}/**/{grupo} - *.xls*",
    ]
    vistos, out = set(), []
    for p in pats:
        for f in sorted(glob.glob(p, recursive=True)):
            rp = Path(f).resolve()
            if rp in vistos or not rp.is_file():
                continue
            vistos.add(rp)
            if _es_de_otro_periodo(Path(f)):
                print(f"   . {Path(f).name}: es de otro periodo -> omitido")
                continue
            out.append(Path(f))
    return out


CORREOS_MANUALES_NOMBRE = "correos_manuales.csv"
CORREOS_MANUALES_GLOBAL = Path(__file__).with_name("_correos_manuales.csv")


def cargar_correos_manuales(meta: dict | None = None) -> dict[tuple[str, str], dict]:
    """Correos que el docente completa a mano (clave: curso + documento).

    El export academico a veces no trae el correo institucional de algunos
    estudiantes. En vez de editar el .xls del sistema, el docente los agrega en
    `_correos_manuales.csv` (curso,documento,correo,nota). Ese archivo es dato
    personal y no se versiona.
    """
    rutas = []
    if meta is not None:
        rutas.append(privado_de(meta) / CORREOS_MANUALES_NOMBRE)
    if CORREOS_MANUALES_GLOBAL.exists():
        rutas.append(CORREOS_MANUALES_GLOBAL)  # compatibilidad con la ubicacion vieja
    out = {}
    for ruta in rutas:
        if not ruta.exists():
            continue
        with ruta.open(encoding="utf-8-sig", newline="") as fh:
            for fila in csv.DictReader(fh):
                doc = _norm(fila.get("documento"))
                correo = _norm(fila.get("correo"))
                if not doc or not correo:
                    continue
                out[doc] = {"correo": correo, "nota": _norm(fila.get("nota")),
                            "origen": ruta.name}
    return out


def cargar_nomina(meta: dict, key: str, manuales: dict,
                  exigir_grupo: bool = False) -> dict | None:
    """La nomina del curso, o None.

    `exigir_grupo` hace falta cuando varios grupos comparten carpeta y codigo de materia
    (los tres de FI300101). El filtro de abajo solo compara el codigo, asi que el primer
    listado en orden alfabetico ganaba para los tres: con el de LB141F en la carpeta, SB141B
    y SB141C recibian ese archivo. Quien llamaba lo detectaba por el nombre y lo descartaba,
    pero ahi se quedaba —era un callejon sin salida, no un filtro— y el listado correcto,
    que estaba en la misma carpeta, no se llegaba a probar. Filtrando ANTES de cargar, cada
    grupo encuentra el suyo.
    """
    carpeta = ROOT / meta["folder"]
    for path in buscar_listado(carpeta, meta["grupo"]):
        if exigir_grupo and meta["grupo"].lower() not in path.name.lower():
            print(f"   . {path.name}: no dice {meta['grupo']} y ese codigo lo usan varios "
                  f"grupos -> no puede ser el de este grupo")
            continue
        try:
            filas = leer_filas(path)
        except Exception as e:  # archivo corrupto o formato inesperado
            print(f"   . {path.name}: no se pudo leer ({e})")
            continue
        info = parse_academusoft(filas) or parse_detalles_cuenta(filas)
        if not info or not info["estudiantes"]:
            print(f"   . {path.name}: sin filas de estudiantes reconocibles")
            continue
        if info["codigo"] and info["codigo"] != meta["codigo"]:
            print(f"   ! {path.name}: es de {info['codigo']}, no de {meta['codigo']} -> omitido")
            continue
        info["archivo"] = path

        # completar los que no traen correo institucional
        aplicados = 0
        for e in info["estudiantes"]:
            if e["correo"]:
                continue
            m = manuales.get(e["documento"])
            if m:
                e["correo"] = m["correo"]
                e["correo_manual"] = True
                aplicados += 1
        if aplicados:
            print(f"   + {aplicados} correo(s) completados desde {CORREOS_MANUALES_NOMBRE}")
        return info
    return None


# ----------------------------------------------------------------- eventos

def curso_sin_grupo(meta: dict) -> str:
    """Nombre de la asignatura, sin el grupo pegado.

    `meta['nombre']` trae el grupo cuando el curso corre en varios («Introducción a la
    Ingeniería · SB141B»), porque ahí es la etiqueta con la que se distinguen en los
    listados. En el título del evento el grupo va en su propio campo, así que aquí hace
    falta la asignatura pelada para no repetirlo dos veces.
    """
    return meta.get("nombre_base") or meta["nombre"]


def titulo(meta: dict, cl: dict) -> str:
    """Título del evento: «[SINCRONICO] GRUPO - Curso - Sesión N».

    Dos cosas que el docente tiene que leer sin abrir el evento, en este orden:

    1. El prefijo `[SINCRONICO]` / `[AUTONOMO]`: si a esa hora hay encuentro o no. Va
       primero porque es lo único que cambia lo que hay que hacer ese día, y porque las
       `[AUTONOMO]` son las únicas que NO llevan sala de Meet.
    2. El GRUPO: los tres grupos de FI300101 comparten nombre de asignatura, así que con
       el nombre pelado no se distinguen. Delante del curso, la agenda lee «SB141C - …» y
       «LB141F - …» de un golpe.

    OJO: este título es la IDENTIDAD del evento. El Apps Script busca «su» evento comparando
    el título exacto (`_buscarEvento_`), así que tiene que salir byte a byte igual que el que
    escribe `generar_apps_script_encuentros._titulo`, que delega en esta función. Si divergen,
    el `.ics` importado y los eventos del Apps Script no se reconocen y el calendario acaba
    con dos series por sesión.
    """
    prefijo = "[AUTONOMO]" if str(cl["tipo"]).startswith("autonoma") else "[SINCRONICO]"
    if cl.get("n") is None:
        # Semana autonoma por festivo de los grupos de Introduccion a la Ingenieria: no tiene
        # numero de sesion (`sesion: null` en el JSON). Sin esta rama saldria «Sesion None».
        cola = "Semana autónoma"
    elif cl.get("parcial"):
        cola = f"Sesión {cl['n']} · Parcial {cl['parcial_n']}"
    elif cl["tipo"] == "sustentacion":
        cola = f"Sesión {cl['n']} · Sustentaciones PI"
    else:
        cola = f"Sesión {cl['n']}"
    return f"{prefijo} {meta['grupo']} - {curso_sin_grupo(meta)} - {cola}"


def ubicacion(cl: dict) -> str:
    """Lugar del evento. En modalidad Virtual no hay campus: todo encuentro es por Meet.

    Las autónomas no tienen encuentro, así que no se les pone un lugar que sugiera lo
    contrario. Si un periodo futuro vuelve a tener sesiones presenciales, el tipo
    `presencial` del JSON las distingue aquí.
    """
    if str(cl["tipo"]).startswith("autonoma"):
        return "Trabajo autónomo (sin encuentro)"
    if cl["tipo"] == "presencial":
        return "UNIAJC (presencial)"
    return "Google Meet (virtual)"


def material(cl: dict) -> str:
    ms = cl.get("clases_material") or []
    return " + ".join(f"Clase {m}" for m in ms) if ms else "—"


def descripcion(meta: dict, cl: dict) -> str:
    """Descripción del evento, en una línea con las partes separadas por ' | '.

    Tres cosas que antes estaban cableadas y ahora salen del curso, porque hay 7 cursos y no
    todos tienen 13 sesiones de 120 min:

    - el total de sesiones sale de `n_clases` (13 en los 4 cursos del semestre corto,
      16 en los grupos de Introducción a la Ingeniería). Estaba escrito «de 13» a mano, así
      que la sesión 16 de un grupo decía «Sesión 16 de 13»;
    - el encabezado usa `nombre_base` si el curso lo trae, para no repetir el grupo dos veces
      («… · SB141C (FI300101) · grupo SB141C»);
    - la semana autónoma por festivo no tiene número de sesión (`n is None`) y lleva su
      propia redacción, con la tarea del equipo.

    El cierre de corte va como parte opcional (`cierre_corte`) y NO como `parcial`: en
    Introducción a la Ingeniería no hay parciales escritos, y marcarlo como parcial haría que
    `titulo()` bautizara el evento «Parcial N · …».
    """
    total = meta.get("n_clases") or len(meta["clases"])
    cab = (f"{meta.get('nombre_base') or meta['nombre']} ({meta['codigo']})"
           f" · grupo {meta['grupo']}")
    if cl.get("n") is None:
        partes = [cab, f"Semana autónoma · {TIPO_ETIQUETA['autonoma']}"]
        if cl.get("festivo"):
            partes.append(f"Festivo: {cl['festivo']}")
        partes.append("No hay encuentro sincrónico: no lleva sala de Meet.")
        if cl.get("tarea"):
            partes.append(f"Trabajo del equipo: {cl['tarea']}")
        partes.append(f"Docente: {DOCENTE} · {CORREO_DOCENTE}")
        return " | ".join(partes)
    partes = [
        cab,
        f"Sesión {cl['n']} de {total} · {TIPO_ETIQUETA.get(cl['tipo'], cl['tipo'])}",
        f"Tema: {_tema_txt(cl)}",
        f"Material docente: {material(cl)}" + (" (sesión doble)" if cl.get("sesion_doble") else ""),
    ]
    if cl.get("festivo"):
        partes.append(f"Festivo: {cl['festivo']}")
    if cl.get("cierre_corte"):
        partes.append(cl["cierre_corte"])
    if str(cl["tipo"]).startswith("autonoma"):
        partes.append("Clase autónoma: trabajo independiente guiado, sin encuentro sincrónico.")
    if cl.get("parcial"):
        partes.append("Día de parcial = solo evaluación (virtual síncrono).")
    if cl["tipo"] == "sustentacion":
        partes.append("Sustentación del Proyecto Integrador (no es parcial).")
    partes.append(f"Docente: {DOCENTE} · {CORREO_DOCENTE}")
    return " | ".join(partes)


def hhmm(horario: str, quien: str = "") -> tuple[str, str]:
    """`'18:00 – 20:00'` -> `('180000', '200000')`.

    El separador da igual (los 4 cursos usan raya larga y los 3 grupos guion normal): la
    expresión solo busca pares HH:MM. Lo que sí importa es que haya DOS: antes esto
    desempaquetaba a ciegas y una cadena mal escrita abortaba con un IndexError que no decía
    de qué curso venía.
    """
    h = re.findall(r"(\d{1,2}):(\d{2})", horario)
    if len(h) < 2:
        raise ValueError(f"horario sin hora de inicio y fin{f' ({quien})' if quien else ''}: "
                         f"{horario!r}")
    (h1, m1), (h2, m2) = h[0], h[1]
    return f"{int(h1):02d}{m1}00", f"{int(h2):02d}{m2}00"


def csv_google(meta: dict) -> list[list[str]]:
    """Las 9 columnas del importador CSV de Google Calendar. Ni una de invitados.

    No es una omisión que se pueda arreglar: el importador CSV/TSV de Google no soporta
    invitados (solo el `.ics` o la API). Este CSV ya era un bloque personal antes del cambio.
    El único correo que aparece es el del docente, dentro de `Description`.
    """
    ini, fin = [x[:2] + ":" + x[2:4] for x in hhmm(meta["horario"], meta["nombre"])]
    rows = [["Subject", "Start Date", "Start Time", "End Date", "End Time",
             "All Day Event", "Description", "Location", "Private"]]
    for cl in meta["clases"]:
        y, m, d = cl["fecha"].split("-")
        fecha = f"{m}/{d}/{y}"  # Google Calendar CSV espera MM/DD/YYYY
        rows.append([titulo(meta, cl), fecha, ini, fecha, fin, "False",
                     descripcion(meta, cl),
                     ubicacion(cl), "True"])
    return rows


def ics(meta: dict) -> str:
    """Los bloques del curso para el calendario PERSONAL del docente. Sin invitados.

    Antes cada VEVENT llevaba un `ATTENDEE` por estudiante (la nómina completa repetida 13
    veces en el archivo) y el calendario se declaraba `METHOD:REQUEST`, o sea invitación
    iTIP: Outlook y Thunderbird lo presentan como «solicitud de reunión» con botones de RSVP.
    Ahora:

    - **no hay `ATTENDEE`**: el archivo no contiene datos personales de nadie;
    - `METHOD:PUBLISH`, que es lo que corresponde a un calendario que solo se publica;
    - **no hay `ORGANIZER`**: con organizador y sin invitados, Google y Outlook pintan el
      evento como «reunión organizada por otro» en vez de como bloque propio.

    Lo que queda es lo mismo de antes: título, descripción, lugar, fecha, hora y zona.
    """
    ini, fin = hhmm(meta["horario"], meta["nombre"])
    # El nombre de los 3 grupos de FI300101 ya trae el grupo dentro («… · SB141C»), asi que
    # el slug distingue los tres y sus UID no se pisan. Importar dos .ics con el mismo UID
    # hace que el segundo SOBRESCRIBA los eventos del primero: mismo UID = mismo evento.
    slug = re.sub(r"[^a-z0-9]+", "-", meta["nombre"].lower()).strip("-")
    L = [
        "BEGIN:VCALENDAR", "VERSION:2.0",
        f"PRODID:-//UNIAJC//Calendario {PERIODO}//ES",
        "CALSCALE:GREGORIAN", "METHOD:PUBLISH",
        f"X-WR-CALNAME:{_esc(meta['nombre'])} {PERIODO}",
        "BEGIN:VTIMEZONE", f"TZID:{TZID}",
        "BEGIN:STANDARD", "DTSTART:19930403T000000",
        f"TZOFFSETFROM:{UTC_OFFSET}", f"TZOFFSETTO:{UTC_OFFSET}",
        "TZNAME:-05", "END:STANDARD", "END:VTIMEZONE",
    ]
    for cl in meta["clases"]:
        stamp = cl["fecha"].replace("-", "")
        # La semana autonoma por festivo no tiene numero de sesion: sin esto, las dos que hay
        # (SB141C y LB141F) saldrian con UID `...-sNone-...`, y dos UID iguales en dos .ics.
        ident = f"s{cl['n']}" if cl.get("n") is not None else f"aut{stamp}"
        L += [
            "BEGIN:VEVENT",
            f"UID:{slug}-{ident}-{PERIODO}@uniajc.edu.co",
            f"DTSTAMP:{stamp}T000000Z",
            f"DTSTART;TZID={TZID}:{stamp}T{ini}",
            f"DTEND;TZID={TZID}:{stamp}T{fin}",
            f"SUMMARY:{_esc(titulo(meta, cl))}",
            f"DESCRIPTION:{_esc(descripcion(meta, cl))}",
            # `_esc` aunque hoy los dos valores posibles no traigan coma ni punto y coma: en
            # iCalendar una coma sin escapar parte el valor en dos y el evento llega raro.
            f"LOCATION:{_esc(ubicacion(cl))}",
            # las autónomas no bloquean agenda: no hay encuentro sincrónico
            "TRANSP:TRANSPARENT" if str(cl["tipo"]).startswith("autonoma") else "TRANSP:OPAQUE",
            "END:VEVENT",
        ]
    L.append("END:VCALENDAR")
    return "\r\n".join(_fold(x) for x in L) + "\r\n"


def _esc(s: str) -> str:
    return str(s).replace("\\", "\\\\").replace(";", r"\;").replace(",", r"\,").replace("\n", r"\n")


def _fold(line: str) -> str:
    """RFC 5545: líneas de máximo 75 octetos, continuación con espacio."""
    if len(line.encode("utf-8")) <= 75:
        return line
    out, cur = [], ""
    for ch in line:
        if len((cur + ch).encode("utf-8")) > 74:
            out.append(cur)
            cur = " " + ch
        else:
            cur += ch
    out.append(cur)
    return "\r\n".join(out)


def escribir_csv(path: Path, rows: list[list[str]], bom: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig" if bom else "utf-8", newline="") as fh:
        csv.writer(fh).writerows(rows)


# ----------------------------------------------------------------- los 7 cursos del periodo

def cursos_del_periodo() -> list[tuple[str, dict]]:
    """Los 7 cursos: los 4 de `semestre_2026_2.json` + los 3 grupos de FI300101.

    Los grupos se traen del adaptador de `generar_apps_script_encuentros`, que ya los pasa a
    esta misma forma (`clases[]` con `n`/`fecha`/`tipo`/`tema`). Se reusa y no se copia: el
    título del evento es su identidad, y dos adaptadores en dos archivos acabarían
    escribiéndolo distinto.

    El import es perezoso a propósito: ese módulo importa ESTE (`import
    generar_eventos_calendario as ev`), así que un import arriba sería un ciclo. Ejecutando
    este archivo como script se cargan dos copias del módulo (`__main__` y la importada); es
    inofensivo porque aquí no hay estado mutable, solo los JSON leídos otra vez.
    """
    cursos = list(DATA["cursos"].items())
    try:
        from generar_apps_script_encuentros import cursos_introduccion_ingenieria
    except Exception as e:      # el otro generador no debe poder tumbar a este
        print(f"AVISO: no pude cargar los grupos de Introduccion a la Ingenieria ({e}).")
        print("       Se generan solo los cursos de semestre_2026_2.json.")
        return cursos
    return cursos + cursos_introduccion_ingenieria()


def alerta_introduccion() -> dict:
    """El aviso de fechas por confirmar que trae `introduccion_ingenieria_2026_2.json`.

    Las 16 sesiones de esos 3 grupos se pasan a diciembre, más de un mes después del cierre de
    los otros cuatro cursos. No se mueve ninguna fecha: solo se repite el aviso, para que no se
    imprima una salida verde sobre fechas que el programa todavía no ha confirmado.
    """
    try:
        from generar_apps_script_encuentros import DATA_II
        return DATA_II.get("alerta_calendario") or {}
    except Exception:
        return {}


def _sufijo_grupo(meta: dict, folders: dict[str, int]) -> str:
    """`' - SB141B'` cuando varios cursos comparten carpeta; `''` en el resto.

    Los 3 grupos de FI300101 son 3 cursos distintos (día, hora y calendario propios) dentro de
    UNA carpeta. Sin el sufijo, el CSV del tercero pisa al del primero sin decir nada.
    """
    return f" - {meta['grupo']}" if folders.get(meta["folder"], 0) > 1 else ""


def _borrar_ics_viejos(privado: Path) -> None:
    """Se lleva los `invitaciones_*.ics` de corridas anteriores.

    Esos archivos llevaban un ATTENDEE por estudiante en cada VEVENT (la nómina completa,
    repetida una vez por sesión). Al renombrar la salida a `bloques_*.ics` dejarían de
    sobrescribirse y se quedarían en disco como copias huérfanas de la nómina.
    """
    for viejo in sorted(privado.glob("invitaciones_*.ics")):
        viejo.unlink()
        print(f"   - borrado {viejo.name} (llevaba la nomina como ATTENDEE)")


# ----------------------------------------------------------------- main

def main() -> None:
    cursos = cursos_del_periodo()
    folders: dict[str, int] = {}
    for _, m in cursos:
        folders[m["folder"]] = folders.get(m["folder"], 0) + 1
    con_eventos = con_nomina = 0

    for key, meta in cursos:
        print(f"\n== {meta['nombre']} ({meta['codigo']} · grupo {meta['grupo']})")
        slug = key                      # unico por curso Y por grupo
        suf = _sufijo_grupo(meta, folders)

        # 1) CSV de eventos sin datos personales (versionable)
        destino = (ROOT / meta["folder"] / "Plan curso" / PERIODO_DIR
                   / f"eventos_calendario_{PERIODO_DIR}{suf}.csv")
        escribir_csv(destino, csv_google(meta))
        print(f"   eventos (sin nomina) -> {destino.relative_to(ROOT)}")

        privado = privado_de(meta)
        privado.mkdir(parents=True, exist_ok=True)
        (privado / "LEEME.txt").write_text(
            "Aqui viven las herramientas de asistencia del curso.\n"
            "nomina_*.csv y asistencia_*.csv llevan datos personales de estudiantes\n"
            "(nombre, documento, correo). bloques_*.ics NO: son bloques de calendario\n"
            "sin invitados, y se quedan aqui por convencion del proyecto.\n"
            "Esta carpeta esta en .gitignore: NO se versiona ni se comparte.\n"
            "Se regenera con: python config/calendario/generar_eventos_calendario.py\n"
            "Procedimiento: ver la carpeta Manuales/ en la raiz de Cursos.\n",
            encoding="utf-8",
        )

        # 2) .ics de bloques del calendario personal: ya NO depende de la nomina, porque ya
        #    no lleva invitados. Antes se escribia despues del porton de la nomina, asi que un
        #    curso sin listado se quedaba tambien sin eventos.
        #    newline="" es obligatorio: el .ics ya trae CRLF (RFC 5545) y sin esto Windows
        #    traduciria cada \n y dejaria \r\r\n, que algunos clientes rechazan.
        _borrar_ics_viejos(privado)
        with (privado / f"bloques_{slug}.ics").open("w", encoding="utf-8", newline="") as fh:
            fh.write(ics(meta))
        print(f"   bloques (sin invitados) -> {privado.relative_to(ROOT)}/bloques_{slug}.ics")
        con_eventos += 1

        # 3) Herramientas de asistencia: estas SI necesitan la nomina real
        manuales = cargar_correos_manuales(meta)
        # Con varios grupos en la misma carpeta hay que exigir el grupo en el nombre del
        # archivo: el codigo de materia no los distingue. Ver `cargar_nomina`.
        comparten = folders.get(meta["folder"], 0) > 1
        info = cargar_nomina(meta, key, manuales, exigir_grupo=comparten)
        # Red de seguridad: si algo cambiara y colara un listado de otro grupo, la planilla de
        # asistencia de dos grupos saldria con los estudiantes de un tercero.
        assert not (info and comparten
                    and meta["grupo"].lower() not in info["archivo"].name.lower()), \
            "%s recibio el listado %s, que no dice %s" % (
                meta["grupo"], info["archivo"].name if info else "?", meta["grupo"])
        if not info:
            print("   sin listado de estudiantes: quedan el CSV y el .ics; falta la planilla.")
            if comparten:
                print(f"     el archivo tiene que decir {meta['grupo']} en el nombre, p.ej. "
                      f"'{meta['grupo']} - INTRODUCCION A LA INGENIERIA.xls'")
            print("   coloca el export del sistema academico en la carpeta del curso y re-ejecuta.")
            continue

        ests = info["estudiantes"]
        con_correo = [e for e in ests if e["correo"]]
        print(f"   listado: {info['archivo'].name}"
              + (f" (reporte {info['reporte']})" if info["reporte"] else ""))
        manual = sum(1 for e in ests if e.get("correo_manual"))
        inst = len(con_correo) - manual
        detalle_correo = f"institucional {inst}" + (f" + personal {manual}" if manual else "")
        print(f"   estudiantes: {len(ests)} · con correo: {len(con_correo)} ({detalle_correo})"
              + (f" · repitentes: {sum(e['repitente'] for e in ests)}" if ests else ""))
        sin_correo = [e for e in ests if not e["correo"]]
        if sin_correo:
            print(f"   ! {len(sin_correo)} sin correo institucional: no hay por donde escribirles.")
            escribir_csv(privado / f"pendientes_correo_{slug}.csv",
                         [["documento", "nombre", "accion"]]
                         + [[e["documento"], e["nombre"],
                             "solicitar correo institucional a Registro Académico"]
                            for e in sin_correo])
            print(f"     -> pendientes_correo_{slug}.csv (para pedirlos a Registro Académico)")

        escribir_csv(privado / f"nomina_{slug}.csv",
                     [["documento", "nombre", "correo", "origen_correo", "repitente"]]
                     + [[e["documento"], e["nombre"], e["correo"],
                         "personal (manual)" if e.get("correo_manual") else "institucional",
                         "si" if e["repitente"] else "no"]
                        for e in ests])

        # Las semanas autónomas no tienen número de sesión (`n` es None): sin este caso la
        # cabecera decía "SNone" y el docente no sabía a qué fecha pasar lista.
        cab = ["documento", "nombre"] + [
            (f"S{cl['n']} {cl['fecha']}" if cl.get("n") is not None else f"Aut {cl['fecha']}")
            + ("(P)" if cl.get("parcial")
               else "(A)" if str(cl["tipo"]).startswith("autonoma") else "")
            for cl in meta["clases"]
        ]
        escribir_csv(privado / f"asistencia_{slug}.csv",
                     [cab] + [[e["documento"], e["nombre"]] + [""] * len(meta["clases"])
                              for e in ests])
        print(f"   nomina + planilla de asistencia -> {privado.relative_to(ROOT)}/")
        con_nomina += 1

    print(f"\nOK. Cursos con eventos: {con_eventos}/{len(cursos)}"
          f" · con nomina real: {con_nomina}/{len(cursos)}")
    print("Los eventos son bloques de TU calendario: sin invitados y sin correos a nadie.")
    print("El .ics sirve de respaldo; el camino recomendado sigue siendo el Apps Script,")
    print("que es el unico que le da a cada sesion su propia sala de Meet:")
    print("  python config/calendario/generar_apps_script_encuentros.py")
    al = alerta_introduccion()
    if al:
        print(f"\nAVISO (Introducción a la Ingeniería): {al.get('titulo', '')}")
        print("  Las fechas de diciembre pasan del cierre institucional 2026-11-22 y están")
        print("  PENDIENTES de confirmar con el programa. No se movió ninguna fecha.")
        print("  Detalle y plan B: LEEME - Apps Script del semestre.md")
    print("\nRecuerda: Plan curso/<periodo>/_privado/ NO se versiona (ahi vive la nomina).")


if __name__ == "__main__":
    # Sin esto, en la consola de Windows (cp1252) un print con tildes revienta o sale ilegible.
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
