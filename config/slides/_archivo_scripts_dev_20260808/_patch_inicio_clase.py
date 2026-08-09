# -*- coding: utf-8 -*-
import re
from pathlib import Path

SLIDES = Path(__file__).resolve().parent
PATCHES = {
    "build_uniajc_seminario_curso.py": "18:10",
    "build_uniajc_bd2_curso.py": "18:10",
    "build_uniajc_arq_curso.py": "10:10",
    "build_uniajc_prog2_curso.py": "18:10",
}

def patch_file(path: Path, hora: str) -> str:
    text = path.read_text(encoding="utf-8")
    if "inicio_clase=" in text:
        return f"{path.name}: already patched"
    m = re.search(r"course_cover\s*\(", text)
    if not m:
        return f"{path.name}: course_cover not found"
    i = m.end() - 1
    depth = 0
    j = i
    while j < len(text):
        ch = text[j]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                break
        j += 1
    else:
        return f"{path.name}: unbalanced parens"
    call = text[m.start() : j + 1]
    body = call[:-1].rstrip()
    if body.endswith(","):
        new_call = body + f"\n        inicio_clase=\"{hora}\",\n    )"
    else:
        new_call = body + f", inicio_clase='{hora}')"
    text2 = text[: m.start()] + new_call + text[j + 1 :]
    path.write_text(text2, encoding="utf-8")
    return f"{path.name}: OK -> inicio_clase={hora}"

def main():
    for name, hora in PATCHES.items():
        print(patch_file(SLIDES / name, hora))

if __name__ == "__main__":
    main()
