# -*- coding: utf-8 -*-
"""Genera los eventos de calendario del semestre a partir de las listas REALES de estudiantes.

Entradas
--------
1. `config/calendario/semestre_2026_2.json` — fuente de verdad del calendario
   (13 sesiones por curso, fechas, tipo, parciales, sesiones dobles, sustentación).
2. El listado de estudiantes de cada curso, descargado del sistema académico.
   Se detecta automáticamente y se aceptan DOS formatos:

   a) **Academusoft "Lista de Alumnos por Grupo"** (`LISTA_DE_ALUMNOS_POR_GRUPOS*.xls`,
      `<grupo> - <MATERIA>.xls`): fila 4 trae `FI###### MATERIA`, grupo y total;
      fila 5 es el encabezado; los estudiantes arrancan en la fila 6 con
      `Tipo de Documento · Identificación · Nombre · Repitente · Institucional`.
   b) **"Detalles de Cuenta"** (`<grupo> - <MATERIA>.xlsx`): encabezado en la fila 2 con
      `DOCUM · NOMBRE · CORREO · INSTITUCIONAL_ESTUDIANTE · COD_MATE · GRUPO · …`.

   Se valida que el código de materia del archivo coincida con el del curso en el JSON;
   si no coincide, el curso se omite (evita cruzar nóminas entre asignaturas).

Salidas
-------
* `<Curso>/Plan curso/2026-2/eventos_calendario_2026-2.csv` — **sin datos personales**.
  Formato de importación de Google Calendar (Subject, Start Date, …). Versionable.
* `<Curso>/Plan curso/2026-2/_privado/` — **CON datos personales, NO se versiona**
  (la regla `_privado/` está en .gitignore). Todo lo del curso vive en la carpeta del curso:
    - `invitaciones_<curso>.ics`  · un evento por sesión con los estudiantes como ATTENDEE
    - `nomina_<curso>.csv`        · nómina normalizada (documento, nombre, correo, origen)
    - `asistencia_<curso>.csv`    · planilla estudiantes × sesiones (la nota de asistencia)
    - `pendientes_correo_<curso>.csv` · solo si alguien no trae correo institucional

Entrada opcional que mantiene el docente, en la misma carpeta privada:
`correos_manuales.csv` (`documento,correo,nota`) para completar los correos que el export
academico no trae. Se cruza por documento.

Ojo: importar el .ics NO envia las invitaciones (Google no lo hace al importar). Para que
lleguen, usa el Apps Script que genera `generar_apps_script_encuentros.py`, que además deja
una sola sala de Meet en toda la serie. Procedimiento: carpeta `Manuales/` en la raíz.

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
import json
import os
import re
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
    "presencial": "Presencial",
    "virtual": "Virtual sincrónica",
    "autonoma": "Autónoma (festivo)",
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


def cargar_nomina(meta: dict, key: str, manuales: dict) -> dict | None:
    carpeta = ROOT / meta["folder"]
    for path in buscar_listado(carpeta, meta["grupo"]):
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

def titulo(meta: dict, cl: dict) -> str:
    """Título del evento, con el tipo de encuentro al principio.

    El estudiante ve el prefijo antes que nada en su calendario, así que ahí va lo único
    que necesita decidir de un vistazo: si tiene que conectarse/asistir a esa hora o no.
    `[SINCRONICO]` = hay encuentro (presencial, virtual o sustentación);
    `[AUTONOMO]` = no hay encuentro, es trabajo independiente guiado con fecha de cierre.
    """
    prefijo = "[AUTONOMO]" if cl["tipo"] == "autonoma" else "[SINCRONICO]"
    if cl.get("parcial"):
        cuerpo = f"Parcial {cl['parcial_n']} · {meta['nombre']}"
    elif cl["tipo"] == "sustentacion":
        cuerpo = f"Sustentaciones PI · {meta['nombre']}"
    else:
        cuerpo = f"Sesión {cl['n']} · {meta['nombre']}"
    return f"{prefijo} {cuerpo}"


def material(cl: dict) -> str:
    ms = cl.get("clases_material") or []
    return " + ".join(f"Clase {m}" for m in ms) if ms else "—"


def descripcion(meta: dict, cl: dict) -> str:
    partes = [
        f"{meta['nombre']} ({meta['codigo']}) · grupo {meta['grupo']}",
        f"Sesión {cl['n']} de 13 · {TIPO_ETIQUETA.get(cl['tipo'], cl['tipo'])}",
        f"Tema: {_tema_txt(cl)}",
        f"Material docente: {material(cl)}" + (" (sesión doble)" if cl.get("sesion_doble") else ""),
    ]
    if cl.get("festivo"):
        partes.append(f"Festivo: {cl['festivo']}")
    if cl["tipo"] == "autonoma":
        partes.append("Clase autónoma: trabajo independiente guiado, sin encuentro sincrónico.")
    if cl.get("parcial"):
        partes.append("Día de parcial = solo evaluación (presencial síncrono).")
    if cl["tipo"] == "sustentacion":
        partes.append("Sustentación del Proyecto Integrador (no es parcial).")
    partes.append(f"Docente: {DOCENTE} · {CORREO_DOCENTE}")
    return " | ".join(partes)


def hhmm(horario: str) -> tuple[str, str]:
    h = re.findall(r"(\d{1,2}):(\d{2})", horario)
    (h1, m1), (h2, m2) = h[0], h[1]
    return f"{int(h1):02d}{m1}00", f"{int(h2):02d}{m2}00"


def csv_google(meta: dict) -> list[list[str]]:
    ini, fin = [x[:2] + ":" + x[2:4] for x in hhmm(meta["horario"])]
    rows = [["Subject", "Start Date", "Start Time", "End Date", "End Time",
             "All Day Event", "Description", "Location", "Private"]]
    for cl in meta["clases"]:
        y, m, d = cl["fecha"].split("-")
        fecha = f"{m}/{d}/{y}"  # Google Calendar CSV espera MM/DD/YYYY
        rows.append([titulo(meta, cl), fecha, ini, fecha, fin, "False",
                     descripcion(meta, cl),
                     "Virtual" if cl["tipo"] == "virtual" else "UNIAJC", "True"])
    return rows


def ics(meta: dict, estudiantes: list[dict]) -> str:
    ini, fin = hhmm(meta["horario"])
    slug = re.sub(r"[^a-z0-9]+", "-", meta["nombre"].lower()).strip("-")
    L = [
        "BEGIN:VCALENDAR", "VERSION:2.0",
        "PRODID:-//UNIAJC//Calendario 2026-2//ES",
        "CALSCALE:GREGORIAN", "METHOD:REQUEST",
        "BEGIN:VTIMEZONE", f"TZID:{TZID}",
        "BEGIN:STANDARD", "DTSTART:19930403T000000",
        f"TZOFFSETFROM:{UTC_OFFSET}", f"TZOFFSETTO:{UTC_OFFSET}",
        "TZNAME:-05", "END:STANDARD", "END:VTIMEZONE",
    ]
    for cl in meta["clases"]:
        stamp = cl["fecha"].replace("-", "")
        L += [
            "BEGIN:VEVENT",
            f"UID:{slug}-s{cl['n']}-2026-2@uniajc.edu.co",
            f"DTSTAMP:{stamp}T000000Z",
            f"DTSTART;TZID={TZID}:{stamp}T{ini}",
            f"DTEND;TZID={TZID}:{stamp}T{fin}",
            f"SUMMARY:{_esc(titulo(meta, cl))}",
            f"DESCRIPTION:{_esc(descripcion(meta, cl))}",
            f"LOCATION:{'Virtual' if cl['tipo'] == 'virtual' else 'UNIAJC'}",
            f"ORGANIZER;CN={_esc(DOCENTE)}:mailto:{CORREO_DOCENTE}",
            # las autónomas no bloquean agenda: no hay encuentro sincrónico
            "TRANSP:TRANSPARENT" if cl["tipo"] == "autonoma" else "TRANSP:OPAQUE",
        ]
        for e in estudiantes:
            if e["correo"]:
                L.append(
                    "ATTENDEE;ROLE=REQ-PARTICIPANT;PARTSTAT=NEEDS-ACTION;RSVP=TRUE;"
                    f"CN={_esc(e['nombre'])}:mailto:{e['correo']}"
                )
        L.append("END:VEVENT")
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


# ----------------------------------------------------------------- main

def main() -> None:
    total_ok = 0
    for key, meta in DATA["cursos"].items():
        print(f"\n== {meta['nombre']} ({meta['codigo']} · grupo {meta['grupo']})")
        slug = key

        # 1) CSV de eventos sin datos personales (versionable)
        destino = ROOT / meta["folder"] / "Plan curso" / "2026-2" / "eventos_calendario_2026-2.csv"
        escribir_csv(destino, csv_google(meta))
        print(f"   eventos (sin nomina) -> {destino.relative_to(ROOT)}")

        # 2) Salidas con nómina real, en la carpeta privada DEL CURSO
        privado = privado_de(meta)
        privado.mkdir(parents=True, exist_ok=True)
        (privado / "LEEME.txt").write_text(
            "Datos personales de estudiantes (nombre, documento, correo).\n"
            "Esta carpeta esta en .gitignore: NO se versiona ni se comparte.\n"
            "Se regenera con: python config/calendario/generar_eventos_calendario.py\n"
            "Procedimiento: ver la carpeta Manuales/ en la raiz de Cursos.\n",
            encoding="utf-8",
        )
        manuales = cargar_correos_manuales(meta)
        info = cargar_nomina(meta, key, manuales)
        if not info:
            print("   sin listado de estudiantes: no se generan .ics ni planillas.")
            print("   coloca el export del sistema academico en la carpeta del curso y re-ejecuta.")
            continue

        ests = info["estudiantes"]
        con_correo = [e for e in ests if e["correo"]]
        print(f"   listado: {info['archivo'].name}"
              + (f" (reporte {info['reporte']})" if info["reporte"] else ""))
        manual = sum(1 for e in ests if e.get("correo_manual"))
        inst = len(con_correo) - manual
        detalle_correo = f"institucional {inst}" + (f" + personal {manual}" if manual else "")
        print(f"   estudiantes: {len(ests)} · invitables: {len(con_correo)} ({detalle_correo})"
              + (f" · repitentes: {sum(e['repitente'] for e in ests)}" if ests else ""))
        sin_correo = [e for e in ests if not e["correo"]]
        if sin_correo:
            print(f"   ! {len(sin_correo)} sin correo institucional: NO reciben invitación.")
            escribir_csv(privado / f"pendientes_correo_{slug}.csv",
                         [["documento", "nombre", "accion"]]
                         + [[e["documento"], e["nombre"],
                             "solicitar correo institucional a Registro Académico"]
                            for e in sin_correo])
            print(f"     -> pendientes_correo_{slug}.csv (para pedirlos a Registro Académico)")

        # newline="" es obligatorio: el .ics ya trae CRLF (RFC 5545) y sin esto Windows
        # traduciria cada \n y dejaria \r\r\n, que algunos clientes rechazan.
        with (privado / f"invitaciones_{slug}.ics").open(
            "w", encoding="utf-8", newline=""
        ) as fh:
            fh.write(ics(meta, con_correo))
        escribir_csv(privado / f"nomina_{slug}.csv",
                     [["documento", "nombre", "correo", "origen_correo", "repitente"]]
                     + [[e["documento"], e["nombre"], e["correo"],
                         "personal (manual)" if e.get("correo_manual") else "institucional",
                         "si" if e["repitente"] else "no"]
                        for e in ests])

        cab = ["documento", "nombre"] + [
            f"S{cl['n']} {cl['fecha']}"
            + ("(P)" if cl.get("parcial") else "(A)" if cl["tipo"] == "autonoma" else "")
            for cl in meta["clases"]
        ]
        escribir_csv(privado / f"asistencia_{slug}.csv",
                     [cab] + [[e["documento"], e["nombre"]] + [""] * len(meta["clases"])
                              for e in ests])
        print(f"   .ics + nomina + planilla -> {privado.relative_to(ROOT)}/")
        total_ok += 1

    print(f"\nOK. Cursos con nomina real: {total_ok}/{len(DATA['cursos'])}")
    print("Los .ics traen a los estudiantes como invitados (ATTENDEE): importalos en el")
    print("calendario del docente y confirma el envio de invitaciones.")
    print("Recuerda: las carpetas Plan curso/<periodo>/_privado/ NO se versionan (datos personales).")


if __name__ == "__main__":
    main()
