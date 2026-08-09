from pathlib import Path
p = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\.config\slides\part3.py")
text = p.read_text(encoding="utf-8")

old_imp = (
    "from part2 import (\n"
    "    DEMO, EXTRA, FUND, HERRAMIENTAS_DIA, HOOKS, IMAGES, PASOS, QUIZ, TIMELINE,\n"
    ")"
)
new_imp = (
    "from part2 import (\n"
    "    DEMO, EXTRA, FUND, HERRAMIENTAS_DIA, HOOKS, IMAGES, PASOS, QUIZ, TIMELINE,\n"
    "    TALLER_BLOQUE, SOLUCION,\n"
    ")"
)
assert old_imp in text, "import not found"
text = text.replace(old_imp, new_imp)

marker = "    # 12) Taller PI visual"
end_marker = "    # 14) Boxes cierre operativo"
i0 = text.index(marker)
i1 = text.index(end_marker)
new_block = r'''    # 12) Bloque Taller PI ampliado (contexto -> objetivo -> escenario -> pasos -> pistas)
    # NO incluir solucion completa aqui (va en Kit docente/).
    tb = TALLER_BLOQUE.get(n, {})
    label = "Actividad autonoma" if c["tipo"] == "autonoma" else "Taller PI CloudLite"
    if tb.get("contexto"):
        content_slide(
            prs, f"{label} — contexto / por que importa",
            tb["contexto"], idx=idx, size=16,
        )
        idx = _next(idx)
    obj = tb.get("objetivo") or c["pi_hoy"]
    crit_lines = [f"@@Exito:@@ {x}" for x in tb.get("criterios", [])]
    if not crit_lines:
        crit_lines = [
            f"@@Entregable:@@ {c['entregable']}",
            "Evidencia adjunta e integrada al PI.",
        ]
    content_slide(prs, f"{label} — objetivo y criterios", [
        f"@@Objetivo:@@ {obj}",
        *crit_lines,
    ], idx=idx, size=15)
    idx = _next(idx)
    if tb.get("escenario"):
        content_slide(
            prs, f"{label} — escenario / datos de partida",
            tb["escenario"], idx=idx, size=16,
        )
        idx = _next(idx)
    steps_visual_slide(
        prs, f"{label} — pasos guiados",
        [(p, "") for p in c["taller_pasos"]],
        idx=idx,
    )
    idx = _next(idx)
    if tb.get("pistas"):
        checklist_slide(
            prs, f"{label} — pistas (checklist vacio)",
            tb["pistas"], idx=idx,
        )
        idx = _next(idx)
    # 13) Checklist entregable
    checklist_slide(prs, "Checklist entregable de hoy", [
        c["entregable"],
        "Evidencia adjunta (PNG / captura / enlace / YAML)",
        "Integrado al informe o repo del equipo",
        "Campus Virtual UNIAJC · domingo 23:59 (cuando aplique)",
        "Listo para explicar en 60 s por integrante",
    ], idx=idx)
    idx = _next(idx)

'''
text = text[:i0] + new_block + text[i1:]
print("taller block replaced")

# Replace build_taller function entirely up to build_quiz
bt0 = text.index("def build_taller(c):")
bq0 = text.index("def build_quiz(c):")
new_funcs = r'''def build_taller(c):
    if c["tipo"] == "parcial":
        return
    n = c["n"]
    tb = TALLER_BLOQUE.get(n, {})
    folder = CURSO / "Clases" / f"Clase {n} - {c['slug']}"
    path = folder / f"{c['taller_titulo']}.docx"
    doc = Document()
    margins(doc)
    banda(doc, c["taller_titulo"])
    para(doc, "Arquitectura · CloudLite App (PI)", bold=True, color=AZUL,
         align=WD_ALIGN_PARAGRAPH.CENTER)
    para(doc, "Documento estudiante — avance del Proyecto Integrador", color=CIAN_D,
         align=WD_ALIGN_PARAGRAPH.CENTER, shade="E8F4FA")
    h2(doc, "1. Contexto / por que importa al PI")
    bullets(doc, tb.get("contexto") or [
        "Este taller avanza el PI CloudLite (no es un ejercicio suelto).",
    ])
    h2(doc, "2. Hoy avanzamos el PI en...")
    para(doc, c["pi_hoy"], shade="FFF8D6")
    h2(doc, "3. Objetivo")
    para(doc, tb.get("objetivo", c["pi_hoy"]))
    h2(doc, "4. Escenario / datos de partida")
    bullets(doc, tb.get("escenario") or ["Usar el dominio CloudLite del equipo."])
    h2(doc, "5. Entregable")
    para(doc, c["entregable"], shade="E8F4FA")
    h2(doc, "6. Herramientas")
    para(doc, c["herramienta"])
    para(doc, "Prohibido: AWS/GCP/Oracle/Azure con tarjeta; Docker Desktop obligatorio.",
         shade="FBE4E4")
    h2(doc, "7. Pasos guiados")
    bullets(doc, c["taller_pasos"])
    h2(doc, "8. Criterios de exito")
    bullets(doc, tb.get("criterios") or [
        "Artefacto en paquete PI.",
        "Explicacion 60 s por integrante.",
        "Evidencia adjunta.",
    ])
    h2(doc, "9. Pistas (checklist vacio — sin solucion)")
    bullets(doc, tb.get("pistas") or ["Revisar que el artefacto entre al informe/repo."])
    h2(doc, "10. Entrega")
    para(doc, "Campus Virtual UNIAJC · domingo 23:59 · un envio por equipo.")
    doc.save(str(path))
    print("OK taller", path)


def build_solucion(c):
    """Solucion PRIVADA en Kit docente/ — nunca en Clases/."""
    if c["tipo"] == "parcial":
        return
    n = c["n"]
    sol = SOLUCION.get(n)
    if not sol:
        return
    kit = CURSO / "Kit docente" / f"Clase {n}"
    kit.mkdir(parents=True, exist_ok=True)
    stem = f"Solucion Taller Clase {n} - CloudLite"
    md_path = kit / f"{stem}.md"
    lines = [
        f"# {sol['titulo']}",
        "",
        "> DOCUMENTO DOCENTE — PRIVADO. No compartir en Clases/ ni Campus antes del cierre.",
        "",
        f"**Resumen:** {sol['resumen']}",
        "",
        "## Alineacion al enunciado estudiante",
        f"- Taller: `Clases/Clase {n} - {c['slug']}/{c['taller_titulo']}.docx`",
        f"- Hito PI: {c['pi_hoy']}",
        f"- Entregable: {c['entregable']}",
        "",
        "## Solucion paso a paso",
    ]
    for i, step in enumerate(sol.get("pasos", []), 1):
        lines.append(f"{i}. {step}")
    lines += ["", "## Ejemplo / artefactos esperados"]
    for ex in sol.get("ejemplo", []):
        lines.append(f"- {ex}")
    lines += ["", "## Rubrica corta / checklist de correccion"]
    for r in sol.get("rubrica", []):
        lines.append(f"- [ ] {r}")
    lines += ["", "## Errores frecuentes"]
    for e in sol.get("errores", []):
        lines.append(f"- {e}")
    lines += ["", "Campus Virtual UNIAJC. Politica: gratis + navegador.", ""]
    md_path.write_text("\n".join(lines), encoding="utf-8")
    path = kit / f"{stem}.docx"
    doc = Document()
    margins(doc)
    banda(doc, sol["titulo"])
    para(doc, "DOCUMENTO DOCENTE — PRIVADO (no va en Clases/)", bold=True, color=ROJO,
         align=WD_ALIGN_PARAGRAPH.CENTER, shade="FBE4E4")
    para(doc, sol["resumen"], shade="E8F4FA")
    h2(doc, "Alineacion al enunciado estudiante")
    bullets(doc, [
        f"Taller estudiante: Clases/Clase {n} - {c['slug']}/{c['taller_titulo']}.docx",
        f"Hito PI: {c['pi_hoy']}",
        f"Entregable: {c['entregable']}",
    ])
    h2(doc, "Solucion paso a paso")
    bullets(doc, sol.get("pasos", []))
    h2(doc, "Ejemplo / artefactos esperados")
    bullets(doc, sol.get("ejemplo", []))
    h2(doc, "Rubrica corta / checklist de correccion")
    bullets(doc, ["[ ] " + r for r in sol.get("rubrica", [])])
    h2(doc, "Errores frecuentes")
    bullets(doc, sol.get("errores", []))
    h2(doc, "Entrega / politica")
    para(doc, "Campus Virtual UNIAJC · gratis + navegador · sin cloud con tarjeta.")
    doc.save(str(path))
    print("OK solucion", path)
    return md_path


'''
text = text[:bt0] + new_funcs + text[bq0:]
print("build_taller/solucion replaced")

# guion: inject solucion reference after ## Taller
needle = 'f"## Taller\\n{pasos}\\n\\n"\n'
# actual content uses escaped differently - search
idx = text.find('f"## Taller\\n{pasos}')
if idx < 0:
    idx = text.find('## Taller\\n{pasos}')
print("taller needle idx", idx)
if idx >= 0:
    # find the full return fragment start for ## Taller
    # Replace the three f-strings about Taller/Criterio
    old = (
        '        f"## Taller\\n{pasos}\\n\\n"\n'
        '        f"## Criterio de exito\\nArtefacto en paquete PI · evidencia · explicacion 60 s.\\n\\n"\n'
        '        f"## Quiz\\n`Kit docente/Clase {n}/Quiz Clase {n} - {c[\'slug\']}.docx`\\n\\n"\n'
    )
    new = (
        '        f"## Taller (bloque ampliado en Presentacion.pptx)\\n"\n'
        '        f"Slides: contexto PI · objetivo/criterios · escenario · pasos · pistas (sin solucion).\\n"\n'
        '        f"{pasos}\\n\\n"\n'
        '        f"## Solucion del taller (PRIVADO)\\n"\n'
        '        f"`Kit docente/Clase {n}/Solucion Taller Clase {n} - CloudLite.docx` (+ .md)\\n"\n'
        '        f"Usar para correccion; no publicar en Clases/.\\n\\n"\n'
        '        f"## Criterio de exito\\nArtefacto en paquete PI · evidencia · explicacion 60 s.\\n\\n"\n'
        '        f"## Quiz\\n`Kit docente/Clase {n}/Quiz Clase {n} - {c[\'slug\']}.docx`\\n\\n"\n'
    )
    if old in text:
        text = text.replace(old, new)
        print("guion taller replaced")
    else:
        # show context
        print(repr(text[idx:idx+220]))

text = text.replace(
    "Demo draw.io \u2192 taller equipos. Bloquea dominios vagos. Checklist.\\n\\n",
    "Demo draw.io -> bloque Taller ampliado. Solucion en Kit docente/. Bloquea dominios vagos. Checklist.\\n\\n",
)
text = text.replace(
    "Slide de pasos visuales + checklist. Bloquea dominios vagos. A los 90 min pedir evidencia.\\n\\n",
    "Bloque Taller ampliado + checklist. Solucion privada en Kit docente/. A los 90 min pedir evidencia.\\n\\n",
)
text = text.replace(
    '"Herramientas · Demo · Taller · Checklist · Quiz · Cierre",',
    '"Herramientas · Demo · Taller ampliado · Checklist · Quiz · Cierre",',
)
text = text.replace(
    "| 23 | Taller PI |\\n",
    "| 23-27 | Taller ampliado (contexto->pistas) |\\n",
)

old_all = (
    '        if c["tipo"] != "parcial":\n'
    "            build_taller(c)\n"
    "            build_quiz(c)\n"
    "        guiones.append(build_guion(c))"
)
new_all = (
    '        if c["tipo"] != "parcial":\n'
    "            build_taller(c)\n"
    "            build_solucion(c)\n"
    "            build_quiz(c)\n"
    "        guiones.append(build_guion(c))"
)
assert old_all in text, "build_all not found"
text = text.replace(old_all, new_all)

p.write_text(text, encoding="utf-8")
print("DONE part3", p.stat().st_size)