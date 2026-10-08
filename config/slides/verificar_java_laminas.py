# -*- coding: utf-8 -*-
"""Compila y ejecuta, CADA UNO POR SEPARADO, los programas de las laminas de Programacion II.

Cada lamina se escribe sola en un `Main.java` de una carpeta temporal vacia, se compila con
``javac --release 17`` y, si no abre ventanas, se ejecuta y su salida se compara con
``salida``. Asi se prueba lo que promete la lamina: se copia, se pega y corre.

    python verificar_java_laminas.py            # todas las clases
    python verificar_java_laminas.py 2 3        # solo esas clases
    python verificar_java_laminas.py -v 2       # ademas imprime la salida real de cada una
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prog2_codigo_laminas as P
import uniajc_slides_engine as E
from prog2_conceptos_data import CONCEPTOS

PROHIBIDO = re.compile(r"vetcare|huellitas|cloudlite|examlab|proyecto integrador", re.I)


def _forma(n, e):
    """Lo que se revisa leyendo: la promesa de la lamina y que quepa sin partir lineas."""
    c, fallos = e["codigo"], []
    ls = P.lineas(e)
    ancho = P.ANCHO_UNA if len(ls) <= P.UNA_COLUMNA else P.MAX_ANCHO
    if len(ls) > P.MAX_LINEAS:
        fallos.append("%d lineas (max %d)" % (len(ls), P.MAX_LINEAS))
    elif len(ls) > P.UNA_COLUMNA:
        izq, der = E._partir_codigo(ls)
        if max(len(izq), len(der)) > P.COLUMNA:
            fallos.append("en dos columnas queda una de %d lineas (max %d): deje una linea "
                          "en blanco entre clases o metodos cerca de la mitad"
                          % (max(len(izq), len(der)), P.COLUMNA))
    for i, ln in enumerate(ls, 1):
        if len(ln) > ancho:
            fallos.append("linea %d de %d caracteres (max %d con %d lineas)"
                          % (i, len(ln), ancho, len(ls)))
        if "\t" in ln:
            fallos.append("linea %d con tabulador" % i)
    if any(ord(ch) > 126 for ch in c):
        fallos.append("caracteres no ASCII")
    if re.search(r"^\s*package\b", c, re.M):
        fallos.append("lleva package")
    if re.search(r"^public\s+(final\s+|abstract\s+)*(class|interface|enum|record)\b", c, re.M):
        fallos.append("clase de nivel superior public (no corre pegada en otro archivo)")
    primera = re.search(r"^(?:final\s+|abstract\s+)*(class|interface|enum|record)\s+(\w+)", c, re.M)
    if not primera or primera.group(2) != "Main":
        fallos.append("la primera clase no es Main")
    if "public static void main(String[] args)" not in c:
        fallos.append("sin main")
    if re.search(r"\bScanner\b", c):
        fallos.append("usa Scanner (la salida dependeria del teclado)")
    if PROHIBIDO.search(c) or PROHIBIDO.search(e.get("salida") or ""):
        fallos.append("nombra el proyecto o la plataforma")
    if not 0 <= e["k"] < len(CONCEPTOS.get(n, [])):
        fallos.append("k=%d no es un concepto de la clase" % e["k"])
    return fallos


def verificar(clases=None, verbose=False):
    javac, java = shutil.which("javac"), shutil.which("java")
    if not javac or not java:
        print("No hay JDK (javac/java) en el PATH: no se puede verificar.")
        return 1
    total, malos = 0, 0
    for n in sorted(P.CODIGO):
        if clases and n not in clases:
            continue
        for e in P.CODIGO[n]:
            total += 1
            fallos = _forma(n, e)
            d = tempfile.mkdtemp(prefix="p2lam_")
            try:
                with open(os.path.join(d, P.ARCHIVO), "w", encoding="ascii", errors="replace",
                          newline="\n") as f:
                    f.write(e["codigo"].strip("\n") + "\n")
                r = subprocess.run([javac, "--release", "17", "-Xlint:all,-serial", P.ARCHIVO],
                                   cwd=d, capture_output=True, text=True)
                if r.returncode or r.stderr.strip():
                    fallos.append("javac:\n" + (r.stdout + r.stderr).strip())
                elif "javax.swing" in e["codigo"]:
                    pass                                   # ventana: solo se compila
                else:
                    try:
                        x = subprocess.run([java, "-cp", ".", "Main"], cwd=d, capture_output=True,
                                           text=True, timeout=30, stdin=subprocess.DEVNULL)
                        real = x.stdout.replace("\r\n", "\n").rstrip("\n")
                        if verbose:
                            print("---- Clase %d · %s\n%s" % (n, e["titulo"], real))
                        if x.returncode:
                            fallos.append("termina con error:\n" + x.stderr.strip())
                        elif e.get("salida") is not None and real != e["salida"].strip("\n"):
                            fallos.append("la salida no coincide. Real:\n" + real)
                    except subprocess.TimeoutExpired:
                        fallos.append("no termina en 30 s")
            finally:
                shutil.rmtree(d, ignore_errors=True)
            if fallos:
                malos += 1
                print("FALLA Clase %d · %s" % (n, e["titulo"]))
                for x in fallos:
                    print("   - " + x.replace("\n", "\n     "))
    print("%d de %d laminas compilan y corren solas" % (total - malos, total))
    return 1 if malos else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    v = "-v" in args
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(verificar({int(a) for a in args if a.isdigit()} or None, verbose=v))
