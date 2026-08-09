# patch rules: append inicio_clase rule via python
from pathlib import Path

# 1) uniajc.json — add to presentacion_del_curso.incluye
import json
p = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\universidades\uniajc.json")
data = json.loads(p.read_text(encoding="utf-8"))
inc = data["estandar_material"]["presentacion_del_curso"]["incluye"]
rule = "pie/portada: hora de inicio efectiva = horario oficial + 10 min (course_cover inicio_clase / hora_inicio_efectiva; wording «Inicio de clase: HH:MM»)"
# remove prior variants
inc = [x for x in inc if "inicio efectiva" not in x.lower() and "inicio_clase" not in x]
inc.append(rule)
data["estandar_material"]["presentacion_del_curso"]["incluye"] = inc
data["estandar_material"]["presentacion_del_curso"]["hora_inicio_efectiva"] = {
    "_regla": "En la portada (pie) de Presentación del Curso mostrar horario oficial + 10 min vía course_cover(..., inicio_clase='HH:MM'). No inventar otros horarios.",
    "ejemplos": {
        "Programacion II": "mié 18:00–20:00 → 18:10",
        "Seminario de Sistemas": "jue 18:00–20:00 → 18:10",
        "Bases de Datos II": "lun 18:00–20:00 → 18:10",
        "Arquitectura": "lun 10:00–12:00 → 10:10"
    },
    "wording": "Inicio de clase: **HH:MM**"
}
p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("uniajc.json OK")

# 2) uniajc-docente.mdc
mdc = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.cursor\rules\uniajc-docente.mdc")
t = mdc.read_text(encoding="utf-8")
needle = "1. Sin pie de página con nombre del curso. El nº de slide (idx) puede quedarse."
repl = (
    "1. Sin pie de página con nombre del curso. El nº de slide (idx) puede quedarse.\n"
    "   Excepción Presentación del Curso: pie/portada con hora de inicio efectiva "
    "(horario oficial + 10 min) vía `course_cover(..., inicio_clase=\"HH:MM\")` — "
    "p. ej. 18:00→**18:10**, 10:00→**10:10**. Wording: «Inicio de clase: **HH:MM**»."
)
if "inicio_clase" not in t:
    if needle not in t:
        raise SystemExit("mdc needle not found")
    t = t.replace(needle, repl, 1)
    mdc.write_text(t, encoding="utf-8")
    print("mdc OK")
else:
    print("mdc already has inicio_clase")

# 3) agent md
agent = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.claude\agents\disenador-curricular-uniajc.md")
at = agent.read_text(encoding="utf-8")
a_needle = "1. Portada (asignatura, código FI…, grupo, periodo, programa, horario en **negrita**; **sin** listado ni placeholder Campus Virtual)"
a_repl = (
    "1. Portada (asignatura, código FI…, grupo, periodo, programa, horario en **negrita**; "
    "**sin** listado ni placeholder Campus Virtual). "
    "**Pie/portada:** hora de inicio efectiva = horario oficial + 10 min "
    "(`course_cover(..., inicio_clase=\"HH:MM\")`; wording «Inicio de clase: **HH:MM**»; "
    "ej. 18:00→18:10, 10:00→10:10)."
)
if "inicio_clase" not in at:
    if a_needle not in at:
        # try without special ellipsis
        print("agent needle missing; searching Portada")
        idx = at.find("Portada (asignatura")
        print(repr(at[idx:idx+200]))
        raise SystemExit(1)
    at = at.replace(a_needle, a_repl, 1)
    agent.write_text(at, encoding="utf-8")
    print("agent OK")
else:
    print("agent already has inicio_clase")
