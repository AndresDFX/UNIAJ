from pathlib import Path
src = Path(r"C:\Users\Andre\AppData\Local\Temp\arq_gen")
dst = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\config\slides")
for n in ["part1.py", "part2.py", "part3.py"]:
    text = (src / n).read_text(encoding="utf-8")
    (dst / n).write_text(text, encoding="utf-8", newline="\n")
    nulls = (dst / n).read_bytes().count(b"\x00")
    print(n, "nulls", nulls)
wrap = "from part3 import build_all\nif __name__ == '__main__':\n    build_all()\n"
(dst / "build_uniajc_arq_clases_batch.py").write_text(wrap, encoding="utf-8", newline="\n")
print("wrap nulls", (dst / "build_uniajc_arq_clases_batch.py").read_bytes().count(b"\x00"))