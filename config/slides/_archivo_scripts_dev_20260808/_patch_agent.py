from pathlib import Path
p = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.claude\agents\disenador-curricular-uniajc.md")
t = p.read_text(encoding="utf-8")
old = "6. Metodología (ABPr, Presencialidad asistida: Clase 1 presencial · resto virtual · parciales presencial, Teoría + Taller + Quiz)"
new = "6. Metodología (ABPr, Presencialidad asistida: Clase 1 presencial · resto virtual · parciales presencial, Teoría + Taller + Quiz). **Mencionar explícitamente:** Clase 1 = Presentación del curso + **diagnóstico de conocimientos previos** + arranque del tema."
if old not in t:
    raise SystemExit("missing metodologia line")
t = t.replace(old, new, 1)
old2 = """## Clase 1
Siempre: Presentación del curso + Diagnóstico + arranque temático de la primera unidad. Wording: `Presentación del curso · Diagnóstico · [tema intro]`. Guion/slides Clase 1 = PPTX del curso + Diagnóstico + primer bloque temático."""
new2 = """## Clase 1
Siempre: Presentación del curso + **Diagnóstico de conocimientos previos** (prueba de saberes del prerrequisito/fundamentos; no encuesta logística) + arranque temático de la primera unidad.
En la **Presentación del Curso** (metodología / Acuerdos / CONTENIDO) mencionar: «Clase 1: Presentación del curso + **diagnóstico de conocimientos previos** + arranque del tema.»
Wording CONTENIDO: `Presentación del curso · Diagnóstico · [tema intro]`. Instrumento: `Kit docente/Clase 1/Prueba Diagnostica…` · Registro: `Entregas docente/<periodo>/DIAGNOSTICO…`.
Guion/slides Clase 1 = PPTX del curso + Diagnóstico + primer bloque temático."""
if old2 not in t:
    raise SystemExit("missing clase 1 block")
t = t.replace(old2, new2, 1)
p.write_text(t, encoding="utf-8")
print("OK agent")