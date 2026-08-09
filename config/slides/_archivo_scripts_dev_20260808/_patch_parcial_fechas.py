from pathlib import Path
import re

ROOT = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides")

COURSE = {
    "build_uniajc_prog2_curso.py": [
        ("12/08", "Parcial 10% (09/09 · Clase 5) · Talleres/Quiz 10% · Asistencia 10%"),
        ("14/09", "Parcial 10% (14/10 · Clase 10) · Talleres/Quiz 10% · Asistencia 10%"),
        ("19/10", "Parcial 15% (18/11 · Clase 15) · PI 20% · Asistencia 5%"),
    ],
    "build_uniajc_seminario_curso.py": [
        ("13/08", "Parcial 10% (10/09 · Clase 5) · Talleres/Quiz 10% · Asistencia 10%"),
        ("14/09", "Parcial 10% (15/10 · Clase 10) · Talleres/Quiz 10% · Asistencia 10%"),
        ("19/10", "Parcial 15% (19/11 · Clase 15) · PI 20% · Asistencia 5%"),
    ],
    "build_uniajc_bd2_curso.py": [
        ("10/08", "Parcial 10% (07/09 · Clase 5) · Talleres/Quiz 10% · Asistencia 10%"),
        ("14/09", "Parcial 10% (05/10 · Clase 9) · Talleres/Quiz 10% · Asistencia 10%"),
        ("19/10", "Parcial 15% (09/11 · Clase 14) · PI 20% · Asistencia 5%"),
    ],
    "build_uniajc_arq_curso.py": [
        ("10/08", "Parcial 10% (07/09 · Clase 5) · Talleres/Quiz 10% · Asistencia 10%"),
        ("14/09", "Parcial 10% (05/10 · Clase 9) · Talleres/Quiz 10% · Asistencia 10%"),
        ("19/10", "Parcial 15% (09/11 · Clase 14) · PI 20% · Asistencia 5%"),
    ],
}

NOTES = {
    "build_uniajc_prog2_curso.py": "Parciales presenciales: P1 09/09 · P2 14/10 · P3 18/11 (Clases 5/10/15). Nunca en autonoma.",
    "build_uniajc_seminario_curso.py": "Parciales presenciales: P1 10/09 · P2 15/10 · P3 19/11 (Clases 5/10/15). Nunca en autonoma.",
    "build_uniajc_bd2_curso.py": "Parciales presenciales: P1 07/09 · P2 05/10 · P3 09/11 (Clases 5/9/14). Nunca en autonoma.",
    "build_uniajc_arq_curso.py": "Parciales presenciales: P1 07/09 · P2 05/10 · P3 09/11 (Clases 5/9/14). Nunca en autonoma.",
}

row_re = re.compile(
    r'\["([123])",\s*"([^"]+)",\s*"Parcial[^"]+",\s*"(\d+%)"\]'
)

for name, mapping in COURSE.items():
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    by_start = {start: desglose for start, desglose in mapping}

    def repl(m):
        corte, ventana, pct = m.group(1), m.group(2), m.group(3)
        start = ventana[:5]
        if start not in by_start:
            return m.group(0)
        return f'["{corte}", "{ventana}", "{by_start[start]}", "{pct}"]'

    new_text, n = row_re.subn(repl, text)
    print(name, "rows", n)

    # replace note="Parciales ... until closing quote after table_content note
    new_text2, n2 = re.subn(
        r'note="Parciales[^"]*"',
        f'note="{NOTES[name]}"',
        new_text,
        count=1,
    )
    print(name, "notes", n2)

    # fix bd2/arq agreements missing P1
    new_text2 = new_text2.replace(
        "Parciales NUNCA en autonoma: P2=Clase 9 (05/10), P3=Clase 14 (09/11).",
        "Parciales NUNCA en autonoma: P1=Clase 5 (07/09), P2=Clase 9 (05/10), P3=Clase 14 (09/11).",
    )
    new_text2 = new_text2.replace(
        "Parciales NUNCA en autónoma: P2=Clase 9 (05/10), P3=Clase 14 (09/11).",
        "Parciales NUNCA en autónoma: P1=Clase 5 (07/09), P2=Clase 9 (05/10), P3=Clase 14 (09/11).",
    )

    path.write_text(new_text2, encoding="utf-8")
