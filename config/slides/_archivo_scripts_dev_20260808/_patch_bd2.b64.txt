# -*- coding: utf-8 -*-
from pathlib import Path
import py_compile

p = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides\build_uniajc_bd2_all.py")
text = p.read_text(encoding="utf-8")

old = (
    "from uniajc_slides_engine import (\n"
    "    new_prs, content_slide, table_content, box_note_slide, closing_slide,\n"
    "    blank, bg_white, footer_num, rect, textbox, _run, _rich,\n"
    "    NAVY, WHITE, CIAN, GRAY, SW, MARGIN, CONTENT_W, add_logo, PP_ALIGN, MSO_ANCHOR, Pt,\n"
    ")"
)
new = (
    "from uniajc_slides_engine import (\n"
    "    new_prs, content_slide, table_content, box_note_slide, closing_slide,\n"
    "    blank, bg_white, footer_num, rect, textbox, _run, _rich,\n"
    "    NAVY, WHITE, CIAN, GRAY, SW, MARGIN, CONTENT_W, add_logo, PP_ALIGN, MSO_ANCHOR, Pt,\n"
    "    herramientas_slide, steps_visual_slide, checklist_slide,\n"
    ")\n"
    "from bd2_taller_data import HERRAMIENTAS_DIA, TALLER_BLOQUE, SOLUCION"
)
assert old in text
text = text.replace(old, new)

old_mid = (
    "    content_slide(prs, \"Demo del dia\", [\n"
    "        f\"**Herramienta:** {c['herramienta']}\",\n"
    "        f\"**Demo:** {c['demo']}\",\n"
    "        \"Sigan el mismo dominio VetCare (no inventen otro caso).\",\n"
    "        \"Al final de la demo: dejar enlace/script compartible al equipo.\",\n"
    "    ], idx=idx); idx += 1\n"
    "    content_slide(prs, \"Taller = avance del Proyecto Integrador\", c['taller'], idx=idx); idx += 1\n"
    "    content_slide(prs, \"Criterios de exito de hoy\", [\n"
    "        \"Entregable del dia listo o con gaps explicitos y responsable.\",\n"
    "        \"Evidencia en playground (enlace) o archivo SQL/PNG en Drive del equipo.\",\n"
    "        \"Actualizacion mental de la checklist PI (que criterio de rubrica avanzo).\",\n"
    "        \"Entrega a Campus Virtual / Drive segun indique el docente — domingo 23:59 si aplica taller.\",\n"
    "    ], idx=idx); idx += 1"
)

new_mid = (
    "    content_slide(prs, \"Demo del dia\", [\n"
    "        f\"**Herramienta:** {c['herramienta']}\",\n"
    "        f\"**Demo:** {c['demo']}\",\n"
    "        \"Sigan el mismo dominio VetCare (no inventen otro caso).\",\n"
    "        \"Al final de la demo: dejar enlace/script compartible al equipo.\",\n"
    "    ], idx=idx); idx += 1\n"
    "    tools = HERRAMIENTAS_DIA.get(c[\"n\"])\n"
    "    if tools:\n"
    "        herramientas_slide(prs, tools, title=\"Herramientas de hoy\",\n"
    "                           sub=\"Gratis · navegador o free tier\", idx=idx)\n"
    "        idx += 1\n"
    "    tb = TALLER_BLOQUE.get(c[\"n\"], {})\n"
    "    label = \"Actividad autonoma\" if c[\"tipo\"] == \"autonoma\" else \"Taller PI VetCare\"\n"
    "    if tb.get(\"contexto\"):\n"
    "        content_slide(prs, f\"{label} — contexto / por que importa\", tb[\"contexto\"], idx=idx, size=16)\n"
    "        idx += 1\n"
    "    obj = tb.get(\"objetivo\") or c[\"hito_pi\"]\n"
    "    crit = [f\"@@Exito:@@ {x}\" for x in tb.get(\"criterios\", [])] or [\n"
    "        f\"@@Entregable:@@ {c['entregable']}\",\n"
    "        \"Evidencia en playground o archivos del equipo.\",\n"
    "    ]\n"
    "    content_slide(prs, f\"{label} — objetivo y criterios\", [f\"@@Objetivo:@@ {obj}\", *crit], idx=idx, size=15)\n"
    "    idx += 1\n"
    "    if tb.get(\"escenario\"):\n"
    "        content_slide(prs, f\"{label} — escenario / datos de partida\", tb[\"escenario\"], idx=idx, size=16)\n"
    "        idx += 1\n"
    "    steps_visual_slide(prs, f\"{label} — pasos guiados\", [(t, \"\") for t in c[\"taller\"]], idx=idx)\n"
    "    idx += 1\n"
    "    if tb.get(\"pistas\"):\n"
    "        checklist_slide(prs, f\"{label} — pistas (checklist vacio)\", tb[\"pistas\"], idx=idx)\n"
    "        idx += 1\n"
    "    content_slide(prs, \"Criterios de exito / entregable\", [\n"
    "        f\"**Entregable:** {c['entregable']}\",\n"
    "        \"Evidencia en playground (enlace) o archivo SQL/PNG del equipo.\",\n"
    "        \"Actualizar checklist PI (que criterio de rubrica avanzo).\",\n"
    "        \"Campus Virtual UNIAJC — domingo 23:59 cuando aplique taller.\",\n"
    "    ], idx=idx); idx += 1"
)
assert old_mid in text, "mid not found"
text = text.replace(old_mid, new_mid)

# Replace build_taller_docx body via markers
t0 = text.index("def build_taller_docx(c):")
g0 = text.index("def build_guion_md(c):")
new_funcs = '''def build_taller_docx(c):
    if c['tipo']=='parcial': return None
    tb = TALLER_BLOQUE.get(c['n'], {})
    doc = Document(); banda(doc, f"Taller PI · Clase {c['n']} · Bases de Datos II")
    para(doc, c['titulo'], size=14, bold=True, color=AZUL)
    para(doc, "Hilo conductor: Proyecto Integrador VetCare DB (no es un ejercicio desconectado).", size=11, bold=True)
    para(doc, f"Herramienta: {c['herramienta']}")
    para(doc, f"Hoy avanzamos el PI en: {c['hito_pi']}", shade_fill="FFF8D6")
    para(doc, "1. Contexto / por que importa al PI", size=12, bold=True, color=AZUL)
    bullets(doc, tb.get('contexto') or ["Trabaje sobre el dominio VetCare del equipo."])
    para(doc, "2. Objetivo", size=12, bold=True, color=AZUL)
    para(doc, tb.get('objetivo', c['hito_pi']))
    para(doc, "3. Escenario / datos de partida", size=12, bold=True, color=AZUL)
    bullets(doc, tb.get('escenario') or ["Usar el DDL/ER VetCare del equipo."])
    para(doc, "4. Actividades (pasos guiados)", size=12, bold=True, color=AZUL)
    bullets(doc, c['taller'])
    para(doc, "5. Entregable", size=12, bold=True, color=AZUL)
    para(doc, c['entregable'], shade_fill="E8F4FA")
    para(doc, "6. Criterios de exito", size=12, bold=True, color=AZUL)
    bullets(doc, tb.get('criterios') or [
        "Avance real del VetCare del equipo.",
        "Evidencia ejecutable o diagrama exportado.",
        "Criterio de rubrica del PI movido hoy.",
    ])
    para(doc, "7. Pistas (checklist vacio — sin solucion)", size=12, bold=True, color=AZUL)
    bullets(doc, tb.get('pistas') or ["Revisar evidencia antes de subir."])
    para(doc, "8. Entrega", size=12, bold=True, color=AZUL)
    para(doc, "Campus Virtual UNIAJC — domingo 23:59 cuando aplique.")
    out_dir = CLASES_DIR / f"Clase {c['n']} - {c['slug']}"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"Taller PI - Clase {c['n']} - VetCare.docx"
    doc.save(str(out)); print("TALLER", out); return out


def build_solucion_docx(c):
    if c['tipo']=='parcial': return None
    sol = SOLUCION.get(c['n'])
    if not sol: return None
    kit = KIT_DIR / f"Clase {c['n']}"
    kit.mkdir(parents=True, exist_ok=True)
    stem = f"Solucion Taller Clase {c['n']} - VetCare"
    lines = [f"# {sol['titulo']}", "",
             "> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.", "",
             f"**Resumen:** {sol['resumen']}", "",
             "## Alineacion",
             f"- Taller: `Clases/Clase {c['n']} - {c['slug']}/Taller PI - Clase {c['n']} - VetCare.docx`",
             f"- Hito: {c['hito_pi']}", f"- Entregable: {c['entregable']}", "",
             "## Solucion paso a paso"]
    for i, s in enumerate(sol.get('pasos', []), 1):
        lines.append(f"{i}. {s}")
    lines += ["", "## Ejemplo / SQL / artefactos"]
    for e in sol.get('ejemplo', []):
        lines.append(f"- {e}")
    if c.get('sql'):
        lines.append(f"- Script demo: `Kit docente/Clase {c['n']}/Codigo/{c['sql']}`")
    lines += ["", "## Rubrica corta"]
    for r in sol.get('rubrica', []):
        lines.append(f"- [ ] {r}")
    lines += ["", "## Errores frecuentes"]
    for e in sol.get('errores', []):
        lines.append(f"- {e}")
    lines += ["", "Campus Virtual UNIAJC.", ""]
    (kit / f"{stem}.md").write_text("\\n".join(lines).replace("\\\\n", "\\n") if False else "\\n".join(lines), encoding='utf-8')
    # fix: write with real newlines
    (kit / f"{stem}.md").write_text("\\n".join(lines), encoding='utf-8')
    doc = Document(); banda(doc, sol['titulo'])
    para(doc, "DOCUMENTO DOCENTE — PRIVADO (no va en Clases/)", bold=True, color=RGBColor(0xA0,0x20,0x30), shade_fill="FBE4E4")
    para(doc, sol['resumen'], shade_fill="E8F4FA")
    para(doc, "Alineacion al enunciado", size=12, bold=True, color=AZUL)
    bullets(doc, [
        f"Taller: Clases/Clase {c['n']} - {c['slug']}/Taller PI - Clase {c['n']} - VetCare.docx",
        f"Hito: {c['hito_pi']}",
        f"Entregable: {c['entregable']}",
    ])
    para(doc, "Solucion paso a paso", size=12, bold=True, color=AZUL)
    bullets(doc, sol.get('pasos', []))
    para(doc, "Ejemplo / SQL / artefactos", size=12, bold=True, color=AZUL)
    bullets(doc, sol.get('ejemplo', []) + ([f"Script demo: Codigo/{c['sql']}"] if c.get('sql') else []))
    para(doc, "Rubrica corta", size=12, bold=True, color=AZUL)
    bullets(doc, ["[ ] "+r for r in sol.get('rubrica', [])])
    para(doc, "Errores frecuentes", size=12, bold=True, color=AZUL)
    bullets(doc, sol.get('errores', []))
    out = kit / f"{stem}.docx"
    doc.save(str(out)); print("SOLUCION", out); return out


'''
# Fix the broken md write in new_funcs - rewrite carefully
new_funcs = new_funcs.replace(
    '(kit / f"{stem}.md").write_text("\\\\n".join(lines).replace("\\\\\\\\n", "\\\\n") if False else "\\\\n".join(lines), encoding=\'utf-8\')\n'
    '    # fix: write with real newlines\n'
    '    (kit / f"{stem}.md").write_text("\\\\n".join(lines), encoding=\'utf-8\')\n',
    '(kit / f"{stem}.md").write_text("\\n".join(lines), encoding="utf-8")\n'
)
# The above is messy because of escaping in this patch file itself.
# Let's rebuild new_funcs more carefully after insertion using a second replace.

text = text[:t0] + new_funcs + text[g0:]

# Fix md write line if broken
text = text.replace(
    '(kit / f"{stem}.md").write_text("\\n".join(lines).replace("\\\\n", "\\n") if False else "\\n".join(lines), encoding=\'utf-8\')\n'
    '    # fix: write with real newlines\n'
    '    (kit / f"{stem}.md").write_text("\\n".join(lines), encoding=\'utf-8\')\n',
    '(kit / f"{stem}.md").write_text("\\n".join(lines), encoding="utf-8")\n',
)

# guion slides_ref
old_ref = (
    "    slides_ref = [\n"
    "        \"Slide 1 portada (Clase N + titulo VetCare)\",\n"
    "        \"Slide Agenda 120 min\",\n"
    "        \"Slide Objetivo PI de la clase\",\n"
    "        \"Slide Teoria Core\",\n"
    "        \"Slide Demo del dia\",\n"
    "        \"Slide Taller = avance PI\",\n"
    "        \"Slide Criterios de exito\",\n"
    "        \"Slide Para el PI esta semana\",\n"
    "        \"Slide Cierre\",\n"
    "    ]"
)
new_ref = (
    "    slides_ref = [\n"
    "        \"Slide 1 portada (Clase N + titulo VetCare)\",\n"
    "        \"Slide Agenda 120 min\",\n"
    "        \"Slide Objetivo PI de la clase\",\n"
    "        \"Slide Teoria Core\",\n"
    "        \"Slide Demo del dia\",\n"
    "        \"Slide Herramientas de hoy (logos 3-4)\",\n"
    "        \"Bloque Taller ampliado: contexto / objetivo / escenario / pasos / pistas\",\n"
    "        \"Slide Criterios de exito / entregable\",\n"
    "        \"Slide Para el PI esta semana\",\n"
    "        \"Slide Cierre\",\n"
    "        \"Solucion PRIVADA: Kit docente/Clase N/Solucion Taller Clase N - VetCare.docx\",\n"
    "    ]"
)
assert old_ref in text
text = text.replace(old_ref, new_ref)

text = text.replace(
    "### 55-105 · Taller guiado = tarea del PI\n"
    "**Decir:** «Equipos: abran su carpeta VetCare. Esto suma a la rubrica del PI.»\n"
    "Actividades:\n",
    "### 55-105 · Taller guiado = tarea del PI\n"
    "**Decir:** «Equipos: abran su carpeta VetCare. Esto suma a la rubrica del PI.»\n"
    "Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).\n"
    "Actividades:\n",
)

text = text.replace(
    "        build_pptx(c)\n"
    "        build_taller_docx(c)\n"
    "        md = build_guion_md(c)\n",
    "        build_pptx(c)\n"
    "        build_taller_docx(c)\n"
    "        build_solucion_docx(c)\n"
    "        md = build_guion_md(c)\n",
)

p.write_text(text, encoding="utf-8")

# Fix potential double-escaped newlines in build_solucion_docx md write
src = p.read_text(encoding="utf-8")
# Normalize any literal backslash-n join mistakes to real "\n".join
src = src.replace(
    '(kit / f"{stem}.md").write_text("\\\\n".join(lines), encoding=\'utf-8\')',
    '(kit / f"{stem}.md").write_text("\\n".join(lines), encoding="utf-8")',
)
src = src.replace(
    '(kit / f"{stem}.md").write_text("\\n".join(lines), encoding=\'utf-8\')',
    '(kit / f"{stem}.md").write_text("\\n".join(lines), encoding="utf-8")',
)
p.write_text(src, encoding="utf-8")
py_compile.compile(str(p), doraise=True)
print("BD2 patch OK")
# show md write line
for i,l in enumerate(src.splitlines(),1):
    if 'stem}.md' in l:
        print(i, l)