# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parent

for name in ["build_uniajc_bd2_curso.py", "build_uniajc_arq_curso.py"]:
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    bad = '\ncontent_slide(prs, "Recursos"'
    good = '\n    content_slide(prs, "Recursos"'
    if bad not in text:
        print("SKIP", name)
        continue
    text = text.replace(bad, good, 1)
    path.write_text(text, encoding="utf-8")
    compile(text, name, "exec")
    print("OK", name)
