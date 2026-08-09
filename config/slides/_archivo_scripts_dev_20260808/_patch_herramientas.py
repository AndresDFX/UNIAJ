# -*- coding: utf-8 -*-
"""One-shot patch: logos grandes + listas principales en Presentación del Curso."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLIDES = Path(__file__).resolve().parent

NEW_FN = '''def herramientas_slide(
    prs,
    items,
    title="Herramientas del curso",
    sub=None,
    idx=None,
    columns=None,
):
    """Grid de herramientas con logo PNG + nombre (Presentación del Curso).

    items: lista de dicts ``{name, logo, note?}`` o tuplas ``(name, logo[, note])``.
    ``logo`` = nombre de archivo en ``assets/herramientas/`` (p. ej. ``drawio.png``).
    Preferir **3–5 herramientas principales**; logos grandes (dominantes).
    Colocar **antes** de ``closing_slide``. Marca UNIAJC: bandas navy/cian + acento amarillo.
    """
    norm = []
    for raw in items or []:
        if isinstance(raw, dict):
            norm.append({
                "name": raw.get("name") or raw.get("nombre") or "",
                "logo": raw.get("logo") or raw.get("imagen"),
                "note": raw.get("note") or raw.get("caption") or raw.get("uso") or "",
            })
        elif isinstance(raw, (list, tuple)):
            norm.append({
                "name": raw[0] if len(raw) > 0 else "",
                "logo": raw[1] if len(raw) > 1 else None,
                "note": raw[2] if len(raw) > 2 else "",
            })
        else:
            norm.append({"name": str(raw), "logo": None, "note": ""})

    n = len(norm)
    if columns is None:
        # Máx. 4 columnas; con 3 o menos, una fila y logos más grandes
        if n <= 4:
            columns = n or 1
        else:
            columns = 4
    columns = max(1, min(int(columns), 4, n or 1))
    rows = max(1, (n + columns - 1) // columns)

    s = blank(prs)
    bg_white(s)
    top = title_block(s, title, sub)
    # Nota corta bajo el título
    if not sub:
        hint = textbox(s, MARGIN, top - 0.05, CONTENT_W, 0.32)
        p = hint.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        _rich(p, "Gratis · navegador o free tier · sin software de pago obligatorio", 12, SOFT)

    area_top = top + 0.22
    area_h = SH - area_top - 0.50
    # Más aire entre tarjetas; logos ~2× el tamaño previo (~1.15 → ~2.2–2.4")
    gap_x = 0.38 if columns <= 3 else 0.30
    gap_y = 0.30
    card_w = (CONTENT_W - gap_x * (columns - 1)) / columns
    card_h = (area_h - gap_y * (rows - 1)) / rows
    # Con pocas filas, tarjetas altas para iconos dominantes
    card_h_cap = 4.35 if rows == 1 else (3.35 if rows == 2 else 2.70)
    card_h = min(card_h, card_h_cap)

    grid_h = rows * card_h + (rows - 1) * gap_y
    y0 = area_top + max(0.0, (area_h - grid_h) / 2)

    # Tope de logo por columnas (aprox. 2× el techo anterior de 1.15")
    logo_cap = {1: 2.85, 2: 2.55, 3: 2.40, 4: 2.05}.get(columns, 2.05)
    name_pt = 16 if columns <= 3 else 14
    note_pt = 12 if columns <= 3 else 11
    init_pt = 22 if columns <= 3 else 18

    for i, it in enumerate(norm):
        r, c = divmod(i, columns)
        x = MARGIN + c * (card_w + gap_x)
        y = y0 + r * (card_h + gap_y)
        rounded(s, x, y, card_w, card_h, ALT)
        # filete superior marca
        rect(s, x, y, card_w, 0.08, NAVY)
        rect(s, x, y + 0.08, card_w, 0.035, AMARILLO)

        logo_path = _herramienta_logo_path(it.get("logo"))
        # Reserva ~0.95" para nombre (+ note) debajo del logo
        text_reserve = 0.95 if it.get("note") else 0.72
        logo_side = min(card_w - 0.45, card_h - text_reserve - 0.35, logo_cap)
        logo_side = max(1.15, logo_side)
        lx = x + (card_w - logo_side) / 2
        ly = y + 0.28
        if logo_path:
            try:
                from PIL import Image as _PILImage
                iw, ih = _PILImage.open(logo_path).size
            except Exception:
                iw, ih = (1, 1)
            if iw >= ih:
                pw, ph = logo_side, logo_side * ih / iw if iw else logo_side
            else:
                ph, pw = logo_side, logo_side * iw / ih if ih else logo_side
            s.shapes.add_picture(
                logo_path,
                Inches(lx + (logo_side - pw) / 2),
                Inches(ly + (logo_side - ph) / 2),
                width=Inches(pw),
                height=Inches(ph),
            )
        else:
            rounded(s, lx, ly, logo_side, logo_side, INFO)
            tf = textbox(s, lx, ly, logo_side, logo_side, anchor=MSO_ANCHOR.MIDDLE)
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            initials = "".join(w[0] for w in (it.get("name") or "?").split()[:2]).upper()
            _run(p.add_run(), initials or "?", init_pt, NAVY, bold=True)

        name_y = ly + logo_side + 0.12
        name_h = max(0.40, y + card_h - name_y - 0.10)
        tf = textbox(s, x + 0.10, name_y, card_w - 0.20, name_h, anchor=MSO_ANCHOR.TOP)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        _run(p.add_run(), it.get("name") or "", name_pt, NAVY, bold=True)
        if it.get("note"):
            p2 = tf.add_paragraph()
            p2.alignment = PP_ALIGN.CENTER
            p2.space_before = Pt(3)
            _run(p2.add_run(), it["note"], note_pt, SOFT)

    footer_num(s, idx)
    return s


'''


def patch_engine() -> None:
    engine = SLIDES / "uniajc_slides_engine.py"
    text = engine.read_text(encoding="utf-8")
    start = text.index("def herramientas_slide(")
    end = text.index("# ---------- Layouts densos")
    engine.write_text(text[:start] + NEW_FN + text[end:], encoding="utf-8")
    print("engine OK")


def replace_herramientas_items(path: Path, items_literal: str, sub: str | None = None) -> bool:
    raw = path.read_text(encoding="utf-8")
    m = re.search(
        r"herramientas_slide\(\s*prs\s*,\s*\[(.*?)\]\s*,\s*title\s*=\s*\"Herramientas del curso\""
        r"\s*,\s*sub\s*=\s*\"([^\"]*)\"\s*,\s*idx\s*=\s*(\d+)\s*,?\s*\)",
        raw,
        flags=re.S,
    )
    if not m:
        print("FAIL regex", path.name)
        i = raw.find("herramientas_slide(")
        print(repr(raw[i : i + 220]))
        return False
    old_sub = m.group(2)
    idx = m.group(3)
    new_sub = sub if sub is not None else old_sub
    replacement = (
        "herramientas_slide(\n"
        "        prs,\n"
        "        [\n"
        f"{items_literal}"
        "        ],\n"
        '        title="Herramientas del curso",\n'
        f'        sub="{new_sub}",\n'
        f"        idx={idx},\n"
        "    )"
    )
    path.write_text(raw[: m.start()] + replacement + raw[m.end() :], encoding="utf-8")
    print("OK", path.name, "sub=", new_sub)
    return True


def patch_builds() -> None:
    prog2_items = """            {"name": "JDK 17+", "logo": "java.png", "note": "Runtime / compilador"},
            {"name": "IntelliJ IDEA", "logo": "intellij.png", "note": "IDE recomendado"},
            {"name": "VS Code", "logo": "vscode.png", "note": "IDE alternativo"},
            {"name": "Padlet", "logo": "padlet.png", "note": "Rompe-hielo"},
"""
    sem_items = """            {"name": "draw.io", "logo": "drawio.png", "note": "Diagramas UML"},
            {"name": "Mermaid", "logo": "mermaid.png", "note": "Docs as Code"},
            {"name": "Padlet", "logo": "padlet.png", "note": "Rompe-hielo"},
"""
    bd2_items = """            {"name": "DB Fiddle", "logo": "dbfiddle.png", "note": "SQL práctico"},
            {"name": "Oracle Live SQL", "logo": "oracle_livesql.png", "note": "PL/SQL · cuenta free"},
            {"name": "draw.io", "logo": "drawio.png", "note": "Modelos ER"},
            {"name": "SQLTest.online", "logo": "sqltest.png", "note": "Multi-motor"},
"""
    arq_items = """            {"name": "draw.io", "logo": "drawio.png", "note": "Arquitectura / C4"},
            {"name": "Killercoda", "logo": "killercoda.png", "note": "Labs contenedores"},
            {"name": "GitHub Actions", "logo": "github_actions.png", "note": "CI/CD conceptual"},
"""
    replace_herramientas_items(
        SLIDES / "build_uniajc_prog2_curso.py",
        prog2_items,
        sub="Gratis · Java 17+ · IDE a elección",
    )
    replace_herramientas_items(
        SLIDES / "build_uniajc_seminario_curso.py",
        sem_items,
        sub="Gratis en navegador · Draw.io / Mermaid",
    )
    replace_herramientas_items(
        SLIDES / "build_uniajc_bd2_curso.py",
        bd2_items,
        sub="Gratis en navegador · SQL + diagramas ER",
    )
    replace_herramientas_items(
        SLIDES / "build_uniajc_arq_curso.py",
        arq_items,
        sub="Gratis en navegador · sin cloud con tarjeta",
    )


def patch_part2() -> None:
    part2 = SLIDES / "part2.py"
    p2 = part2.read_text(encoding="utf-8")
    old_h1 = (
        '1: [{"name":"Padlet","logo":"padlet.png","note":"Rompe-hielo"},\n'
        '    {"name":"Excalidraw","logo":"excalidraw.png","note":"Boceto"},\n'
        '    {"name":"draw.io","logo":"drawio.png","note":"C4 Context"},\n'
        '    {"name":"Google Docs","logo":"google_docs.png","note":"Ficha PI"}],'
    )
    new_h1 = (
        '1: [{"name":"Padlet","logo":"padlet.png","note":"Rompe-hielo"},\n'
        '    {"name":"draw.io","logo":"drawio.png","note":"C4 Context"},\n'
        '    {"name":"Excalidraw","logo":"excalidraw.png","note":"Boceto"}],'
    )
    if old_h1 in p2:
        part2.write_text(p2.replace(old_h1, new_h1), encoding="utf-8")
        print("OK part2 HERRAMIENTAS_DIA[1] -> 3")
    else:
        print("WARN part2 class1 block not found")


if __name__ == "__main__":
    patch_engine()
    patch_builds()
    patch_part2()
    print("done")
