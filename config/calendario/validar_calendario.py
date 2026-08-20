# -*- coding: utf-8 -*-
"""Valida el calendario 2026-2 contra sus invariantes y contra los documentos derivados.

No modifica nada: solo comprueba y devuelve codigo de salida 1 si algo falla, para
poder usarlo como chequeo antes de publicar material.

Que verifica
------------
A. Invariantes del JSON (fuente de verdad):
   1. Ventana: la primera sesion cae en la semana del 24/08/2026 y la ultima no pasa del fin.
   2. 13 sesiones por curso, numeradas 1..13 sin huecos ni repetidos.
   3. Cada fecha cae en el dia de la semana declarado por el curso.
   4. Las fechas son estrictamente crecientes y separadas por 7 dias (una por semana).
   5. Los 15 temas del microcurriculo estan cubiertos por `clases_material`, sin
      duplicados ni faltantes, y las sesiones dobles son exactamente las que declaran 2.
   6. Ningun parcial cae en festivo ni en sesion autonoma o de sustentacion.
   7. Cada festivo del rango aparece marcado en la sesion que le corresponde.
   8. Los rangos de corte del JSON cubren 1..13 sin solaparse.
B. Coherencia con lo derivado:
   9. El CSV de eventos de cada curso tiene 13 filas y sus fechas coinciden con el JSON.
  10. El CSV importable a Google Calendar tiene 13 eventos y fechas coincidentes.
  11. El CALENDARIO_2026-2.md menciona cada fecha del curso.

Uso
---
    python config/calendario/validar_calendario.py
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
JSON_PATH = Path(__file__).with_name("semestre_2026_2.json")
DATA = json.loads(JSON_PATH.read_text(encoding="utf-8"))

INICIO = dt.date.fromisoformat(DATA["inicio"])
FIN = dt.date.fromisoformat(DATA["fin"])
FESTIVOS = {dt.date.fromisoformat(k): v for k, v in DATA["festivos_en_rango"].items()}
N_TEMAS = 15
N_SESIONES = 13

DIA_IDX = {"Lunes": 0, "Martes": 1, "Miércoles": 2, "Jueves": 3, "Viernes": 4,
           "Sábado": 5, "Domingo": 6}

fallos: list[str] = []
avisos: list[str] = []


def check(cond: bool, msg: str) -> bool:
    if not cond:
        fallos.append(msg)
    return cond


def semana_de(d: dt.date) -> dt.date:
    """Lunes de la semana de `d`."""
    return d - dt.timedelta(days=d.weekday())


def validar_curso(key: str, meta: dict) -> None:
    nombre = meta["nombre"]
    clases = meta["clases"]
    fechas = [dt.date.fromisoformat(c["fecha"]) for c in clases]

    # 2. cantidad y numeracion
    check(len(clases) == N_SESIONES,
          f"{nombre}: tiene {len(clases)} sesiones, se esperaban {N_SESIONES}")
    check([c["n"] for c in clases] == list(range(1, len(clases) + 1)),
          f"{nombre}: la numeracion de sesiones no es 1..{len(clases)} consecutiva")

    # 1. ventana
    check(semana_de(fechas[0]) == semana_de(INICIO),
          f"{nombre}: la sesion 1 ({fechas[0]}) no cae en la semana del {INICIO}")
    check(fechas[-1] <= FIN,
          f"{nombre}: la ultima sesion ({fechas[-1]}) pasa del fin del periodo ({FIN})")
    check(fechas[0] >= INICIO,
          f"{nombre}: la sesion 1 ({fechas[0]}) arranca antes del inicio ({INICIO})")

    # 3. dia de la semana
    idx = DIA_IDX.get(meta["dia"])
    check(idx is not None, f"{nombre}: dia '{meta['dia']}' no reconocido")
    if idx is not None:
        malas = [f.isoformat() for f in fechas if f.weekday() != idx]
        check(not malas, f"{nombre}: estas fechas no caen en {meta['dia']}: {malas}")

    # 4. una por semana, crecientes
    saltos = [(fechas[i + 1] - fechas[i]).days for i in range(len(fechas) - 1)]
    check(all(s == 7 for s in saltos),
          f"{nombre}: hay sesiones que no estan separadas 7 dias: {saltos}")

    # 5. cobertura de los 15 temas
    material: list[int] = []
    for c in clases:
        material.extend(c.get("clases_material") or [])
    check(sorted(material) == list(range(1, N_TEMAS + 1)),
          f"{nombre}: el material cubierto no son las clases 1..{N_TEMAS} exactas "
          f"(hay {len(material)} entradas; duplicados o faltantes)")
    dobles_reales = {c["n"] for c in clases if len(c.get("clases_material") or []) == 2}
    dobles_marcadas = {c["n"] for c in clases if c.get("sesion_doble")}
    check(dobles_reales == dobles_marcadas,
          f"{nombre}: sesiones con 2 clases {sorted(dobles_reales)} != marcadas como "
          f"dobles {sorted(dobles_marcadas)}")
    check(len(dobles_reales) == N_TEMAS - N_SESIONES,
          f"{nombre}: se necesitan {N_TEMAS - N_SESIONES} sesiones dobles, hay "
          f"{len(dobles_reales)}")

    # 6. parciales limpios
    for c in clases:
        if not c.get("parcial"):
            continue
        f = dt.date.fromisoformat(c["fecha"])
        check(f not in FESTIVOS,
              f"{nombre}: el Parcial {c.get('parcial_n')} (sesion {c['n']}) cae en festivo {f}")
        check(c["tipo"] not in ("autonoma", "sustentacion"),
              f"{nombre}: el Parcial {c.get('parcial_n')} (sesion {c['n']}) esta en una "
              f"sesion de tipo '{c['tipo']}'")
    pn = [c.get("parcial_n") for c in clases if c.get("parcial")]
    check(sorted(x for x in pn if x) == [1, 2, 3],
          f"{nombre}: los parciales no son exactamente 1, 2 y 3 (son {pn})")

    # 7. festivos marcados
    for f, festivo in FESTIVOS.items():
        for c in clases:
            if dt.date.fromisoformat(c["fecha"]) == f:
                check(bool(c.get("festivo")),
                      f"{nombre}: la sesion {c['n']} cae en el festivo {f} ({festivo}) "
                      f"pero no lo declara")
                check(c["tipo"] in ("autonoma", "sustentacion"),
                      f"{nombre}: la sesion {c['n']} cae en festivo pero su tipo es "
                      f"'{c['tipo']}'")

    # --- B. documentos derivados
    periodo_dir = ROOT / meta["folder"] / "Plan curso" / "2026-2"
    iso = {f.isoformat() for f in fechas}

    csv_doc = periodo_dir / "calendario_eventos_2026-2.csv"
    if csv_doc.exists():
        with csv_doc.open(encoding="utf-8-sig", newline="") as fh:
            filas = list(csv.DictReader(fh))
        check(len(filas) == N_SESIONES,
              f"{nombre}: {csv_doc.name} tiene {len(filas)} filas, se esperaban {N_SESIONES}")
        check({r["fecha"] for r in filas} == iso,
              f"{nombre}: las fechas de {csv_doc.name} no coinciden con el JSON")
    else:
        avisos.append(f"{nombre}: falta {csv_doc.name}")

    csv_goo = periodo_dir / "eventos_calendario_2026-2.csv"
    if csv_goo.exists():
        with csv_goo.open(encoding="utf-8-sig", newline="") as fh:
            filas = list(csv.DictReader(fh))
        check(len(filas) == N_SESIONES,
              f"{nombre}: {csv_goo.name} tiene {len(filas)} eventos, se esperaban {N_SESIONES}")
        conv = set()
        for r in filas:
            m, d, y = r["Start Date"].split("/")
            conv.add(f"{y}-{m}-{d}")
        check(conv == iso,
              f"{nombre}: las fechas de {csv_goo.name} no coinciden con el JSON")
    else:
        avisos.append(f"{nombre}: falta {csv_goo.name}")

    md = periodo_dir / "CALENDARIO_2026-2.md"
    if md.exists():
        txt = md.read_text(encoding="utf-8")
        faltan = [f.strftime("%d/%m/%Y") for f in fechas if f.strftime("%d/%m/%Y") not in txt]
        check(not faltan, f"{nombre}: {md.name} no menciona las fechas {faltan}")
    else:
        avisos.append(f"{nombre}: falta {md.name}")


def validar_carpetas_drive() -> None:
    """Las carpetas de Drive del JSON deben estar completas y coincidir con el Apps Script.

    El id de `grabadas` vive en dos sitios: el JSON (que alimenta el correo de bienvenida)
    y `apps_script_grabaciones/MoverGrabaciones.gs` (que mueve las grabaciones). Si se
    cambia una carpeta y solo se actualiza uno, las grabaciones acaban en la carpeta vieja.
    """
    gs = Path(__file__).parent / "apps_script_grabaciones" / "MoverGrabaciones.gs"
    texto = gs.read_text(encoding="utf-8") if gs.exists() else None
    if texto is None:
        avisos.append("no existe apps_script_grabaciones/MoverGrabaciones.gs")

    for meta in DATA["cursos"].values():
        c = meta.get("carpetas_drive") or {}
        for tipo in ("clases", "grabadas"):
            ent = c.get(tipo) or {}
            check(bool(ent.get("id")) and bool(ent.get("url")),
                  f"{meta['nombre']}: falta carpetas_drive.{tipo} (id/url)")
            url = ent.get("url", "")
            check("?usp=" not in url and "/u/0/" not in url,
                  f"{meta['nombre']}: la URL de {tipo} no está canónica (trae ?usp= o /u/0/): {url}")
            if ent.get("id") and ent.get("url"):
                check(ent["url"].endswith(ent["id"]),
                      f"{meta['nombre']}: la URL de {tipo} no termina en su propio id")
        # el id de grabadas debe aparecer en el .gs
        gid = (c.get("grabadas") or {}).get("id")
        if texto and gid:
            check(gid in texto,
                  f"{meta['nombre']}: el id de 'grabadas' ({gid}) no está en "
                  f"MoverGrabaciones.gs — el script movería las grabaciones a otra carpeta")
        # y NO debe estar el de clases (sería mandar grabaciones al material compartido)
        cid = (c.get("clases") or {}).get("id")
        if texto and cid:
            check(f"carpetaGrabadas: '{cid}'" not in texto,
                  f"{meta['nombre']}: MoverGrabaciones.gs usa como destino el id de la "
                  f"carpeta de CLASES ({cid}), no el de grabadas")


def main() -> int:
    print(f"Validando calendario {DATA['periodo']}: {INICIO} -> {FIN}")
    print(f"Semana de inicio esperada: lunes {semana_de(INICIO)}\n")

    # 8. cortes
    rangos = []
    for k in sorted(DATA["cortes_teoricos"]):
        a, b = DATA["cortes_teoricos"][k]["clases"].split("-")
        rangos.append((int(a), int(b)))
    cubierto: list[int] = []
    for a, b in rangos:
        cubierto.extend(range(a, b + 1))
    check(sorted(cubierto) == list(range(1, N_SESIONES + 1)),
          f"los cortes no cubren 1..{N_SESIONES} sin solaparse: {rangos}")

    validar_carpetas_drive()

    for key, meta in DATA["cursos"].items():
        validar_curso(key, meta)
        f0 = meta["clases"][0]["fecha"]
        fN = meta["clases"][-1]["fecha"]
        par = "/".join(str(c["n"]) for c in meta["clases"] if c.get("parcial"))
        print(f"  {meta['nombre'][:38]:<38} {meta['dia']:<10} S1={f0}  S13={fN}  parciales={par}")

    print()
    for a in avisos:
        print(f"AVISO: {a}")
    if fallos:
        print(f"\nFALLOS ({len(fallos)}):")
        for f in fallos:
            print(f"  - {f}")
        return 1
    print(f"OK: {len(DATA['cursos'])} cursos validados, sin fallos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
