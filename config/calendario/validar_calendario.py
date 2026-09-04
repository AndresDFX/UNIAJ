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

C. Introduccion a la Ingenieria (`introduccion_ingenieria_2026_2.json`), BLOQUE APARTE:
   Ese curso no cabe en las reglas de arriba y por eso vive en otro archivo: son 11 sesiones
   (no 13), CON 5 sesiones dobles (dos Clases del microcurriculo en un mismo bloque de 90
   min, mismo patron `clases_material`/`sesion_doble` de `semestre_2026_2.json`), sin
   parciales escritos, y desde 2026-09-04 cierra dentro de la ventana institucional (antes
   llegaba a diciembre). Meterlo en `validar_curso` habria obligado a llenar esa funcion de
   excepciones, con el riesgo de aflojar las reglas de los otros cuatro. Se valida entonces
   con sus propias reglas:
  12. Cada grupo tiene sus 11 sesiones numeradas 1..11, una por semana, en su dia.
  13. La primera cae en la semana de su `inicio` y la ultima es exactamente su `fin`.
  14. Los 16 temas del microcurriculo se dictan por `clases_material`, sin duplicados ni
      faltantes y en orden; las sesiones dobles son exactamente las que declaran 2 clases.
  15. Ningun festivo del rango que caiga en el dia de clase queda como sesion normal: tiene
      que estar declarado como semana autonoma (`autonoma_festivo`) con su tarea. En el
      calendario de 11 sesiones ninguno cae, asi que esta regla no tiene nada que marcar.
  16. Ninguna sesion se marca como parcial (este curso evalua por exposiciones).
  17. Los cortes cubren 1..11 sin solaparse, y cierran en una sesion que existe.
  18. El CSV importable y el `CALENDARIO_<periodo> - <grupo>.md` de cada grupo coinciden con
      el JSON (los tres grupos comparten carpeta, por eso llevan el grupo en el nombre).
  Ya no hay AVISO por cierre institucional: las 11 sesiones caben antes del 22/11.

Uso
---
    python config/calendario/validar_calendario.py
"""
from __future__ import annotations

import csv
import datetime as dt
import io
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

# Introduccion a la Ingenieria: otro archivo, otras reglas. Si el archivo no esta, el bloque C
# se salta con un aviso en vez de reventar: los otros cuatro cursos se siguen validando.
JSON_II = Path(__file__).with_name("introduccion_ingenieria_2026_2.json")
DATA_II = json.loads(JSON_II.read_text(encoding="utf-8")) if JSON_II.exists() else None
CIERRE_INSTITUCIONAL = FIN      # el 22/11 de los otros cuatro cursos

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


# --------------------------------------------------------------------------- bloque C

def validar_grupo_introduccion(g: dict) -> None:
    """Un grupo de Introduccion a la Ingenieria, con las reglas de SU curso.

    Deliberadamente separado de `validar_curso`: aqui son 11 sesiones para 16 temas (5
    dobles), sin parciales, y desde 2026-09-04 el calendario cierra dentro de la ventana
    institucional. Las dos funciones no comparten ni una constante para que aflojar una no
    afloje la otra.
    """
    cur = DATA_II["curso"]
    nombre = f"{cur['nombre_acentos']} · {g['grupo']}"
    n_ses = cur["n_sesiones"]
    n_temas = cur["n_temas"]
    ini_g = dt.date.fromisoformat(g["inicio"])
    fin_g = dt.date.fromisoformat(g["fin"])
    ses = g["sesiones"]
    fechas = [dt.date.fromisoformat(s["fecha"]) for s in ses]

    # 12. numeracion: solo las sesiones reales llevan numero; las semanas autonomas van con
    #     `sesion: null` y NO consumen numero (asi un grupo con una autonoma tendria mas
    #     entradas que sesiones numeradas). En el calendario de 11 sesiones no hay ninguna.
    numeradas = [s["sesion"] for s in ses if s.get("sesion") is not None]
    check(numeradas == list(range(1, n_ses + 1)),
          f"{nombre}: la numeracion no es 1..{n_ses} consecutiva (es {numeradas})")
    autonomas = [s for s in ses if str(s.get("tipo", "")).startswith("autonoma")]
    check(all(s.get("sesion") is None for s in autonomas),
          f"{nombre}: alguna semana autonoma lleva numero de sesion; debe ir con sesion: null")

    idx = DIA_IDX.get(g["dia"])
    check(idx is not None, f"{nombre}: dia '{g['dia']}' no reconocido")
    if idx is not None:
        malas = [f.isoformat() for f in fechas if f.weekday() != idx]
        check(not malas, f"{nombre}: estas fechas no caen en {g['dia']}: {malas}")

    saltos = [(fechas[i + 1] - fechas[i]).days for i in range(len(fechas) - 1)]
    check(all(s == 7 for s in saltos),
          f"{nombre}: hay semanas que no estan separadas 7 dias: {saltos}")

    # 13. ventana propia del grupo
    check(semana_de(fechas[0]) == semana_de(ini_g),
          f"{nombre}: la sesion 1 ({fechas[0]}) no cae en la semana de su inicio ({ini_g})")
    check(fechas[-1] == fin_g,
          f"{nombre}: la ultima semana ({fechas[-1]}) no coincide con su fin declarado ({fin_g})")
    check(len(ses) == g["n_semanas_calendario"],
          f"{nombre}: {len(ses)} entradas de calendario, pero declara "
          f"n_semanas_calendario={g['n_semanas_calendario']}")

    # 14. las clases_material cubren los n_temas del microcurriculo, sin duplicados ni
    #     faltantes, en orden — y las sesiones dobles son exactamente las que declaran 2.
    clases = [c for s in ses for c in (s.get("clases_material") or [])]
    check(sorted(clases) == list(range(1, n_temas + 1)),
          f"{nombre}: las clases dictadas no son 1..{n_temas} exactas (son {sorted(clases)})")
    check(clases == sorted(clases),
          f"{nombre}: las clases no se dictan en orden: {clases}")
    for s in ses:
        n_clases = len(s.get("clases_material") or [])
        marcada = bool(s.get("sesion_doble"))
        check((n_clases == 2) == marcada,
              f"{nombre}: sesion {s.get('sesion')} dicta {n_clases} clase(s) pero "
              f"sesion_doble={marcada}")
        check(n_clases in (0, 1, 2),
              f"{nombre}: sesion {s.get('sesion')} dicta {n_clases} clases, ni 1 ni 2")

    # 15. festivos: el peligro real es programar clase un festivo sin darse cuenta. El 08/12/2026
    #     es martes y fecha fija (no la mueve la Ley Emiliani), asi que golpea a SB141C y LB141F.
    festivos_ii = {dt.date.fromisoformat(k): v
                   for k, v in DATA_II["festivos_colombia_2026_en_rango"].items()}
    for f, festivo in festivos_ii.items():
        if not (ini_g <= f <= fin_g) or (idx is not None and f.weekday() != idx):
            continue
        cae = [s for s, fe in zip(ses, fechas) if fe == f]
        check(bool(cae),
              f"{nombre}: el festivo {f} ({festivo}) cae en {g['dia']} dentro del rango pero "
              f"no hay ninguna entrada de calendario para esa semana")
        for s in cae:
            check(str(s.get("tipo", "")).startswith("autonoma"),
                  f"{nombre}: {f} es festivo ({festivo}) y la entrada es de tipo "
                  f"'{s.get('tipo')}': tendria clase en festivo")
            check(bool(s.get("festivo")),
                  f"{nombre}: la semana del {f} no declara el festivo")
            check(bool(s.get("tarea")),
                  f"{nombre}: la semana autonoma del {f} no trae tarea concreta "
                  f"(la regla_festivos del JSON la exige)")

    # 16. sin parciales escritos: este curso evalua por exposiciones y cortes en sesion
    con_parcial = [s.get("sesion") for s in ses if s.get("parcial")]
    check(not con_parcial,
          f"{nombre}: hay sesiones marcadas como parcial ({con_parcial}); este curso no tiene "
          f"parciales escritos, evalua por exposiciones")

    # 18. el CSV importable del grupo. Lleva el grupo en el nombre porque los 3 comparten carpeta.
    periodo_dir = ROOT / cur["folder"] / "Plan curso" / DATA_II["periodo"]
    csv_goo = periodo_dir / f"eventos_calendario_{DATA_II['periodo']} - {g['grupo']}.csv"
    if csv_goo.exists():
        with csv_goo.open(encoding="utf-8-sig", newline="") as fh:
            filas = list(csv.DictReader(fh))
        check(len(filas) == len(ses),
              f"{nombre}: {csv_goo.name} tiene {len(filas)} eventos, se esperaban {len(ses)}")
        conv = set()
        for r in filas:
            m, d, y = r["Start Date"].split("/")
            conv.add(f"{y}-{m}-{d}")
        check(conv == {f.isoformat() for f in fechas},
              f"{nombre}: las fechas de {csv_goo.name} no coinciden con el JSON")
    else:
        avisos.append(f"{nombre}: falta {csv_goo.name} "
                      f"(se genera con generar_eventos_calendario.py)")

    md = periodo_dir / f"CALENDARIO_{DATA_II['periodo']} - {g['grupo']}.md"
    if md.exists():
        txt = md.read_text(encoding="utf-8")
        faltan = [f.strftime("%d/%m/%Y") for f in fechas if f.strftime("%d/%m/%Y") not in txt]
        check(not faltan, f"{nombre}: {md.name} no menciona las fechas {faltan}")
    else:
        avisos.append(f"{nombre}: falta {md.name}")

    if fin_g > CIERRE_INSTITUCIONAL:
        avisos.append(f"{nombre}: cierra el {fin_g}, despues del {CIERRE_INSTITUCIONAL} en que "
                      f"cierran los otros cursos. PENDIENTE de confirmar con el programa "
                      f"(ver alerta_calendario en el JSON). No es un fallo: no se comprime.")


def validar_introduccion() -> None:
    """Bloque C completo: los cortes del curso y despues cada grupo."""
    cur = DATA_II["curso"]
    n_ses = cur["n_sesiones"]

    # 17. cortes: mismo invariante que en los otros cursos, con su propio total de sesiones.
    cubierto: list[int] = []
    for c in DATA_II["cortes"]:
        a, b = c["sesiones"].split("-")
        cubierto.extend(range(int(a), int(b) + 1))
        check(int(a) <= c["cierra_en_sesion"] <= int(b),
              f"{cur['codigo']}: el corte {c['corte']} cierra en la sesion "
              f"{c['cierra_en_sesion']}, fuera de su rango {c['sesiones']}")
    check(sorted(cubierto) == list(range(1, n_ses + 1)),
          f"{cur['codigo']}: los cortes no cubren 1..{n_ses} sin solaparse "
          f"({[c['sesiones'] for c in DATA_II['cortes']]})")
    check(len(DATA_II["temas"]) == cur["n_temas"],
          f"{cur['codigo']}: hay {len(DATA_II['temas'])} temas y el curso declara "
          f"n_temas={cur['n_temas']}")

    for g in DATA_II["grupos"]:
        validar_grupo_introduccion(g)
        reales = [s for s in g["sesiones"] if s.get("sesion") is not None]
        aut = len(g["sesiones"]) - len(reales)
        print(f"  {(cur['nombre_acentos'] + ' · ' + g['grupo'])[:38]:<38} {g['dia']:<10} "
              f"S1={reales[0]['fecha']}  S{len(reales)}={reales[-1]['fecha']}  "
              f"autonomas={aut}")


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

    # Bloque C: otro JSON, otras reglas, otro bloque. Nada de lo de arriba se toco.
    n_grupos = 0
    if DATA_II is None:
        avisos.append(f"no existe {JSON_II.name}: no se validaron los grupos de "
                      f"Introduccion a la Ingenieria")
    else:
        print(f"\nIntroduccion a la Ingenieria ({DATA_II['curso']['codigo']}), "
              f"{DATA_II['curso']['n_sesiones']} sesiones, JSON aparte:")
        validar_introduccion()
        n_grupos = len(DATA_II["grupos"])

    print()
    for a in avisos:
        print(f"AVISO: {a}")
    if fallos:
        print(f"\nFALLOS ({len(fallos)}):")
        for f in fallos:
            print(f"  - {f}")
        return 1
    print(f"OK: {len(DATA['cursos'])} cursos + {n_grupos} grupos de Introduccion validados, "
          f"sin fallos.")
    return 0


if __name__ == "__main__":
    # Sin esto, en la consola de Windows (cp1252) un print con tildes revienta o sale ilegible.
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.exit(main())
