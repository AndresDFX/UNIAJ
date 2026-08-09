# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parent
out = []
for name in ["build_uniajc_bd2_curso.py", "build_uniajc_arq_curso.py"]:
    lines = (ROOT / name).read_text(encoding="utf-8").splitlines()
    out.append("==== " + name)
    for i, line in enumerate(lines):
        if "Proyecto Integrador" in line and "content_slide" in line:
            start = max(0, i - 2)
            end = min(len(lines), i + 30)
            for n in range(start, end):
                s = lines[n]
                indent = len(s) - len(s.lstrip(" "))
                out.append(f"{n+1:4}|{indent:2}|{s}")
            out.append("")
(ROOT / "_snip_pi_area.txt").write_text("\n".join(out), encoding="utf-8")
print("ok")
