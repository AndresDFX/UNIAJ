# -*- coding: utf-8 -*-
"""Enriquece Clase 1 (diagnostico + PI) y regenera Presentacion del Curso."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides")))

from uniajc_slides_engine import (
    new_prs, content_slide, table_content, box_note_slide, closing_slide,
    blank, bg_white, footer_num, rect, textbox, _run, _rich,
    NAVY, WHITE, CIAN, GRAY, SW, MARGIN, CONTENT_W, add_logo, PP_ALIGN, MSO_ANCHOR, Pt,
)

ROOT = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos")
OUT_DIR = ROOT / "Bases de Datos II" / "Clases" / "Clase 1 - Revision BD I y arranque VetCare"
KIT1 = ROOT / "Bases de Datos II" / "Kit docente" / "Clase 1"

def build_clase1_pptx():
    prs = new_prs()
    s = blank(prs); bg_white(s)
    rect(s, 0, 0, SW, 3.0, NAVY); rect(s, 0, 3.0, SW, 0.08, CIAN)
    add_logo(s, width=2.0, corner="left-top", mt=0.3, mr=0.5, variant="white")
    tn = textbox(s, SW - 2.2, 0.35, 1.8, 0.4)
    pn = tn.paragraphs[0]; pn.alignment = PP_ALIGN.RIGHT
    _run(pn.add_run(), "Clase 1", 12, CIAN, bold=True)
    tf = textbox(s, MARGIN, 1.0, CONTENT_W, 1.5, anchor=MSO_ANCHOR.MIDDLE)
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    _run(p.add_run(), "Revision BD I · Arranque VetCare DB", 26, WHITE, bold=True)
    ps = tf.add_paragraph(); ps.alignment = PP_ALIGN.CENTER; ps.space_before = Pt(8)
    _run(ps.add_run(), "Presentacion breve · Diagnostico · Primer avance PI", 15, CIAN)
    tm = textbox(s, MARGIN, 3.5, CONTENT_W, 2.6)
    for i, ln in enumerate([
        "Hoy avanzamos el PI en: **dominio VetCare + borrador ER + alcance del equipo**.",
        "Bloque **120 min** · Logistica breve (Presentacion del Curso) · Diagnostico · Teoria/demo · Taller PI.",
        "Entregable: ficha de equipo + ER borrador (PNG) + reglas de negocio.",
    ]):
        p = tm.paragraphs[0] if i == 0 else tm.add_paragraph()
        p.space_after = Pt(10); _rich(p, ln, 15, GRAY)
    footer_num(s, 1)

    content_slide(prs, "Agenda de hoy (120 min)", [
        "**0-15** Presentacion del Curso (logistica breve) + Padlet rompe-hielo.",
        "**15-45** **Diagnostico de conocimientos previos** (BD I / SQL / modelo).",
        "**45-70** Teoria Core breve: entidades VetCare + reglas del PI.",
        "**70-90** Demo: ER en draw.io + DDL minimo en DB Fiddle.",
        "**90-115** Taller PI: equipo, alcance, ER borrador.",
        "**115-120** Criterios de exito · cierre.",
    ], idx=2)
    content_slide(prs, "Diagnostico (no califica el temario nuevo)", [
        "Prueba de saberes del prerrequisito (BD I): modelo, SQL basico, integridad.",
        "No es encuesta logistica ni evaluacion del PI todavia.",
        "Instrumento: prueba diagnostica del docente (Kit / Campus).",
        "Resultado: ajustamos el ritmo del arranque VetCare.",
    ], idx=3)
    content_slide(prs, "Objetivo PI de la clase", [
        "@@Hito@@ Arranque PI: dominio, alcance y borrador ER de VetCare DB",
        "**Entregable:** ficha de equipo + ER borrador (PNG) + lista de entidades/reglas",
        "La Presentacion del Curso ya cubrio evaluacion/cronograma; aqui no se repite el mapa.",
        "Todo el semestre el taller = avance del PI (no ejercicios desconectados).",
    ], idx=4)
    content_slide(prs, "Teoria Core (breve) — al servicio del ER", [
        "Repaso rapido: entidad, relacion, PK/FK, 1-3FN (solo lo que usa el PI).",
        "Dominio VetCare: Dueno, Mascota, Veterinario, Cita, Consulta, Insumo, DetalleFactura.",
        "Reglas PI: mascota inactiva no cita; stock >= 0; auditoria de cambios sensibles.",
    ], idx=5)
    content_slide(prs, "Demo del dia", [
        "**Herramientas:** draw.io + DB Fiddle (gratis + navegador).",
        "Boceto ER Dueno–Mascota–Cita y 3 CREATE TABLE minimos.",
        "Mismo dominio VetCare que usaran todo el semestre.",
        "Dejar enlace/script al equipo al terminar la demo.",
    ], idx=6)
    content_slide(prs, "Taller = avance del Proyecto Integrador", [
        "Formar equipo (2-3) y nombrar el proyecto VetCare DB.",
        "Listar entidades minimas + 3 reglas de negocio propias.",
        "Dibujar ER borrador en draw.io/Excalidraw y exportar PNG.",
        "Escribir 5-8 lineas de alcance (que SI / que NO hara el PI).",
    ], idx=7)
    content_slide(prs, "Criterios de exito de hoy", [
        "Diagnostico presentado (individual).",
        "Equipo definido + ER borrador exportado.",
        "Alcance escrito y reglas de negocio listadas.",
        "Entrega del taller: domingo 23:59 cuando aplique (Acuerdo).",
    ], idx=8)
    box_note_slide(prs, "Para el PI esta semana", [
        ("info", "Enunciado completo: Clases/Proyecto Integrador/ (VetCare DB)."),
        ("aclaracion", "Proxima clase autonoma: roles y privilegios del PI."),
        ("advertencia", "Taller de la semana: domingo 23:59 si aplica."),
    ], idx=9)
    closing_slide(prs, "Clase 1 · VetCare arranca", [
        "Diagnostico hecho · dominio elegido",
        "ER borrador + equipo listo",
        "Siguiente: administracion / roles (autonoma)",
    ], accent="Teoria breve · practica = PI")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / "Presentacion.pptx"
    prs.save(str(out))
    print("OK PPTX", out)

def enrich_guion():
    md = KIT1 / "Guion Docente Clase 1 - Revision BD I y arranque VetCare.md"
    text = f'''# Guion docente · Clase 1 · Revision BD I · Arranque VetCare DB

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (Clase 1 especial)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** dominio, alcance y borrador ER
- **Entregable de hoy:** ficha de equipo + ER borrador (PNG) + lista de entidades/reglas
- **Herramientas:** draw.io + DB Fiddle
- **Slides clase:** `Clases/Clase 1 - Revision BD I y arranque VetCare/Presentacion.pptx`
- **Presentacion del Curso:** `Clases/Presentacion del Curso - Bases de Datos II.pptx` (logistica)
- **Prueba diagnostica:** `Kit docente/Clase 1/Prueba Diagnostica - Bases de Datos II.docx`

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo en este guion.
> La Presentacion del Curso cubre evaluacion global / cronograma / Padlet.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo no es un repaso enciclopedico de BD I, sino **activar el dominio VetCare**
y dejar evidencia del arranque del PI (ER + alcance). Teoria minima: entidad/relacion,
PK/FK, normalizacion basica, y las reglas de negocio del enunciado PI.

**Demo que usted debe poder repetir:** ER Dueno–Mascota–Cita en draw.io + DDL minimo en DB Fiddle.

## Referencias a diapositivas (Presentacion.pptx de la clase)
1. Portada Clase 1
2. Agenda 120 min (incluye diagnostico)
3. Diagnostico (no califica temario nuevo)
4. Objetivo PI de la clase
5. Teoria Core breve
6. Demo del dia
7. Taller = avance PI
8. Criterios de exito
9. Para el PI esta semana
10. Cierre

## Plan minuto a minuto (120 min) — texto casi literal

### 0-15 · Logistica breve (Presentacion del Curso)
**Decir:** «Bienvenidos a Bases de Datos II. Hoy hacemos tres cosas: acuerdos del curso,
un diagnostico de lo que traen de BD I, y el arranque del Proyecto Integrador VetCare DB.»
Abrir `Presentacion del Curso` (grupo, horario, evaluacion 30/30/40, Padlet, CONTENIDO).
Padlet rompe-hielo (2-3 min). No alargar checklist operativa del docente.

### 15-45 · Diagnostico de conocimientos previos
**Decir:** «Esto no califica el temario nuevo. Es una foto de entrada: modelo, SQL, integridad.»
Aplicar `Prueba Diagnostica - Bases de Datos II.docx` (individual, silencio de trabajo).
[CAP: enunciado diagnostico en pantalla / Campus]
Recoger. **Decir:** «Con esto ajustamos el ritmo; el PI arranca hoy igual.»

### 45-70 · Teoria Core breve → VetCare
Mostrar slides Teoria + Objetivo PI.
**Decir:** «Todo el semestre el taller avanza VetCare. Hoy: entidades y reglas.»
Cubrir: Dueno, Mascota, Veterinario, Cita, Consulta, Insumo, DetalleFactura;
reglas (mascota inactiva, stock, auditoria). Pregunta al aire: ¿que entidad les falta?

### 70-90 · Demo draw.io + DB Fiddle
**Decir:** «Miren mi pantalla. Mismo dominio que usaran ustedes.»
1) draw.io: Dueno 1—N Mascota; Mascota 1—N Cita.
2) DB Fiddle: CREATE TABLE dueno/mascota/cita + INSERT + SELECT join.
📸 Pantallazo: [CAP: demo draw.io ER VetCare Clase 1]
📸 Pantallazo: [CAP: demo DB Fiddle DDL VetCare Clase 1]
Dejar script `Codigo/01_arranque_vetcare.sql` / enlace en el chat.

### 90-115 · Taller PI (equipos)
**Decir:** «Equipos de 2-3. Esto es el arranque oficial del PI, no un ejercicio suelto.»
1. Ficha de equipo (nombres + nombre proyecto).
2. Entidades + 3 reglas propias.
3. ER borrador exportado PNG.
4. Alcance SI/NO (5-8 lineas).
Circular y empujar evidencia. Entrega domingo 23:59 si aplica.
[CAP: avance ER de un equipo]

### 115-120 · Cierre
Repasar criterios (diagnostico + ER + equipo).
**Decir:** «Enunciado completo en Clases/Proyecto Integrador. Proxima: roles VetCare (autonoma).»
Slide cierre. Dudas.

## Codigo
`Codigo/01_arranque_vetcare.sql`

## Capturas
Ver `Capturas/README_capturas.txt` — pendientes PNG reales.

## Criterios de exito del dia
- Diagnostico aplicado.
- Equipos con ER borrador y alcance escrito.
- Queda claro que el hilo del semestre es VetCare DB.
'''
    md.write_text(text, encoding="utf-8")
    print("OK guion md")
    import subprocess
    conv = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides\guion_md_a_docx.py")
    subprocess.run([sys.executable, str(conv), str(md)], check=False)

if __name__ == "__main__":
    build_clase1_pptx()
    enrich_guion()
    # regenerar presentacion del curso
    import runpy
    runpy.run_path(str(Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides\build_uniajc_bd2_curso.py")), run_name="__main__")