from pathlib import Path
ROOT = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides")

def patch(name, pairs):
    p = ROOT / name
    text = p.read_text(encoding="utf-8")
    for old, new in pairs:
        if old not in text:
            raise SystemExit(f"MISSING in {name}: {old[:100]!r}")
        text = text.replace(old, new, 1)
    p.write_text(text, encoding="utf-8")
    print("OK", name)

mid = "\u00b7"
arr = "\u2192"
acentos = {
    "o_acute": "\u00f3",
    "i_acute": "\u00ed",
    "a_acute": "\u00e1",
    "e_acute": "\u00e9",
    "u_acute": "\u00fa",
    "n_tilde": "\u00f1",
}

# Seminario
old1 = (
    f"        'Modalidad: **Presencialidad asistida** (Clase 1 presencial {mid} resto virtual {mid} parciales presencial {mid} festivos aut{acentos['o_acute']}nomos).',\n"
    f"        'Cada jueves (120 min): **Teor{acentos['i_acute']}a Core** {arr} **Taller / exposici{acentos['o_acute']}n** {arr} **Quiz corto** cuando aplique.',\n"
)
new1 = (
    f"        'Modalidad: **Presencialidad asistida** (Clase 1 presencial {mid} resto virtual {mid} parciales presencial {mid} festivos aut{acentos['o_acute']}nomos).',\n"
    f"        'Clase 1: Presentaci{acentos['o_acute']}n del curso + **diagn{acentos['o_acute']}stico de conocimientos previos** + arranque del tema.',\n"
    f"        'Cada jueves (120 min): **Teor{acentos['i_acute']}a Core** {arr} **Taller / exposici{acentos['o_acute']}n** {arr} **Quiz corto** cuando aplique.',\n"
)
old2 = f'{{"n": 1, "tema": "Presentaci{acentos["o_acute"]}n del curso {mid} Conceptos iniciales", "fecha": "13/08"}}'
new2 = f'{{"n": 1, "tema": "Presentaci{acentos["o_acute"]}n del curso {mid} Diagn{acentos["o_acute"]}stico {mid} Conceptos iniciales", "fecha": "13/08"}}'
old3 = f"('aclaracion', 'Clase 1 = Presentaci{acentos['o_acute']}n del curso + arranque tem{acentos['a_acute']}tico (Conceptos iniciales). Material estudiante solo en carpeta Clases/.'),"
new3 = f"('aclaracion', 'Clase 1: Presentaci{acentos['o_acute']}n del curso + diagn{acentos['o_acute']}stico de conocimientos previos + arranque del tema (Conceptos iniciales). Material estudiante solo en carpeta Clases/.'),"
patch("build_uniajc_seminario_curso.py", [(old1, new1), (old2, new2), (old3, new3)])

# BD2
old1 = (
    f"        'Modalidad: **Presencialidad asistida** (Clase 1 presencial {mid} resto virtual {mid} parciales presencial {mid} festivos aut{acentos['o_acute']}nomos).',\n"
    f"        'Cada lunes (120 min): **Teor{acentos['i_acute']}a Core** {arr} **Taller / laboratorio en la nube** {arr} **Quiz corto**.',\n"
)
new1 = (
    f"        'Modalidad: **Presencialidad asistida** (Clase 1 presencial {mid} resto virtual {mid} parciales presencial {mid} festivos aut{acentos['o_acute']}nomos).',\n"
    f"        'Clase 1: Presentaci{acentos['o_acute']}n del curso + **diagn{acentos['o_acute']}stico de conocimientos previos** + arranque del tema.',\n"
    f"        'Cada lunes (120 min): **Teor{acentos['i_acute']}a Core** {arr} **Taller / laboratorio en la nube** {arr} **Quiz corto**.',\n"
)
old3 = f"('aclaracion', 'Clases en festivo (17/08, 12/10, 02/11, 16/11) = aut{acentos['o_acute']}nomas con actividad en Campus Virtual.'),"
new3 = f"('aclaracion', 'Clase 1: Presentaci{acentos['o_acute']}n del curso + diagn{acentos['o_acute']}stico de conocimientos previos + arranque del tema (revisi{acentos['o_acute']}n BD I). Festivos = aut{acentos['o_acute']}noma en Campus Virtual.'),"
patch("build_uniajc_bd2_curso.py", [(old1, new1), (old3, new3)])

# Arq
arq = (ROOT / "build_uniajc_arq_curso.py").read_text(encoding="utf-8")
old_m = (
    f"        'Bloque de **120 min** (lunes 10:00{chr(0x2013)}12:00).',\n"
    "\n"
    f"        'Estructura: **Teor{acentos['i_acute']}a Core** {arr} **Taller / laboratorio en navegador** {arr} **Quiz / avance PI**.',\n"
)
new_m = (
    f"        'Bloque de **120 min** (lunes 10:00{chr(0x2013)}12:00).',\n"
    "\n"
    f"        'Clase 1: Presentaci{acentos['o_acute']}n del curso + **diagn{acentos['o_acute']}stico de conocimientos previos** + arranque del tema.',\n"
    "\n"
    f"        'Estructura: **Teor{acentos['i_acute']}a Core** {arr} **Taller / laboratorio en navegador** {arr} **Quiz / avance PI**.',\n"
)
if old_m not in arq:
    # try with hyphen
    old_m = old_m.replace(chr(0x2013), "-")
    new_m = new_m.replace(chr(0x2013), "-")
if old_m not in arq:
    raise SystemExit("MISSING arq methodology")
arq = arq.replace(old_m, new_m, 1)
old_a = f"('aclaracion', 'Clases en festivo = aut{acentos['o_acute']}nomas con actividad en Campus Virtual.'),"
new_a = f"('aclaracion', 'Clase 1: Presentaci{acentos['o_acute']}n del curso + diagn{acentos['o_acute']}stico de conocimientos previos + arranque del tema (intro arquitecturas cloud). Festivos = aut{acentos['o_acute']}noma en Campus Virtual.'),"
if old_a not in arq:
    raise SystemExit("MISSING arq acuerdos")
arq = arq.replace(old_a, new_a, 1)
(ROOT / "build_uniajc_arq_curso.py").write_text(arq, encoding="utf-8")
print("OK build_uniajc_arq_curso.py")
print("done")