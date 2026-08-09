# ---------- Portadas ----------
def course_cover(
    prs,
    materia,
    subtitulo,
    meta_lines,
    inicio_clase=None,
    hora_inicio_efectiva=None,
    pie_inicio=None,
    hora_arranque=None,
):
    """Portada del curso: banda azul institucional + filete amarillo + logo blanco.

    Pie opcional (solo portada Presentación del Curso): hora de arranque = horario
    oficial + 10 min. Alias: inicio_clase / hora_inicio_efectiva / pie_inicio /
    hora_arranque (p. ej. \"20:10\" o \"10:10\"). Wording: «Inicio de clase: HH:MM».
    No usar en PPTX de Clase N ni inventar otros pies.
    """
    s = blank(prs); bg_white(s)
    rect(s, 0, 0, SW, 3.2, NAVY)
    rect(s, 0, 3.2, SW, 0.08, AMARILLO)
    tf = textbox(s, MARGIN, 1.0, CONTENT_W, 1.6, anchor=MSO_ANCHOR.MIDDLE)
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    _run(p.add_run(), materia, 34, WHITE, bold=True)
    if subtitulo:
        ps = tf.add_paragraph(); ps.alignment = PP_ALIGN.CENTER; ps.space_before = Pt(10)
        _run(ps.add_run(), subtitulo, 18, RGBColor(0xB8, 0xD8, 0xEE))
    add_logo(s, width=2.1, corner="left-top", mt=0.35, mr=0.5, variant="white")
    hora = inicio_clase or hora_inicio_efectiva or pie_inicio or hora_arranque
    meta_h = 2.85 if hora else 3.2
    tm = textbox(s, MARGIN, 3.65, CONTENT_W, meta_h)
    for i, ln in enumerate(meta_lines or []):
        p = tm.paragraphs[0] if i == 0 else tm.add_paragraph()
        p.space_after = Pt(8); _rich(p, ln, 15, GRAY)
    if hora:
        # Pie de portada: inicio efectivo = horario oficial del curso + 10 min
        rect(s, MARGIN, SH - 0.72, CONTENT_W, 0.02, CIAN)
        tf_pie = textbox(s, MARGIN, SH - 0.62, CONTENT_W, 0.4, anchor=MSO_ANCHOR.MIDDLE)
        pp = tf_pie.paragraphs[0]; pp.alignment = PP_ALIGN.CENTER
        _rich(pp, f"Inicio de clase: **{hora}**", 16, NAVY)
    return s


def class_cover(prs, titulo, subtitulo=None, clase_n=None, idx=1):
    """Portada de Clase N: hero institucional limpio (sin bloque meta inferior).

    Solo: logo UNIAJC + título del tema + subtítulo corto opcional
    (p. ej. «Diagnóstico · CloudLite») + badge «Clase N».
    No poner aquí PI / agenda 120 min / gratis+navegador — van en la 2ª slide.
    """
    s = blank(prs)
    # Fondo hero navy a pantalla completa (evita franja + vacío blanco)
    rect(s, 0, 0, SW, SH, NAVY)
    # Acento superior cian + filete amarillo de marca
    rect(s, 0, 0, SW, 0.10, CIAN)
    rect(s, 0, 0.10, SW, 0.055, AMARILLO)
    add_logo(s, width=2.2, corner="left-top", mt=0.42, mr=0.55, variant="white")
    if clase_n is not None:
        badge_w, badge_h = 1.85, 0.42
        bx = SW - MARGIN - badge_w
        by = 0.42
        rounded(s, bx, by, badge_w, badge_h, CIAN)
        tb = textbox(s, bx, by, badge_w, badge_h, anchor=MSO_ANCHOR.MIDDLE)
        pb = tb.paragraphs[0]
        pb.alignment = PP_ALIGN.CENTER
        _run(pb.add_run(), f"Clase {clase_n}", 14, WHITE, bold=True)
    # Título centrado en el eje visual (composición hero)
    title_top = 2.55 if subtitulo else 2.85
    title_h = 2.0 if subtitulo else 1.6
    # Tipografía: títulos largos un poco más chicos para no desbordar
    tlen = len(titulo or "")
    title_pt = 40 if tlen <= 36 else (34 if tlen <= 56 else 28)
    tf = textbox(s, MARGIN + 0.3, title_top, CONTENT_W - 0.6, title_h, anchor=MSO_ANCHOR.MIDDLE)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    _run(p.add_run(), titulo, title_pt, WHITE, bold=True)
    if subtitulo:
        # Filete amarillo corto bajo el título
        line_w = min(3.2, CONTENT_W * 0.28)
        rect(s, (SW - line_w) / 2, title_top + title_h + 0.05, line_w, 0.055, AMARILLO)
        ts = textbox(s, MARGIN + 0.3, title_top + title_h + 0.22, CONTENT_W - 0.6, 0.7)
        ps = ts.paragraphs[0]
        ps.alignment = PP_ALIGN.CENTER
        _run(ps.add_run(), subtitulo, 18, RGBColor(0xB8, 0xD8, 0xEE))
    else:
        line_w = min(3.2, CONTENT_W * 0.28)
        rect(s, (SW - line_w) / 2, title_top + title_h + 0.12, line_w, 0.055, AMARILLO)
    # Nº de slide discreto (tono claro sobre navy)
    if idx is not None:
        tn = textbox(s, SW - 1.2, SH - 0.48, 0.6, 0.3)
        pn = tn.paragraphs[0]
        pn.alignment = PP_ALIGN.RIGHT
        _run(pn.add_run(), str(idx), 11, RGBColor(0x7E, 0xB8, 0xD4), bold=True)
    return s
