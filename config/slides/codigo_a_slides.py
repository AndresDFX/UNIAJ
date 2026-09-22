# -*- coding: utf-8 -*-
"""Parte el codigo fuente de la clase en laminas de codigo, una por unidad logica.

Por que existe
--------------
Programacion II y Seminario traen en `codigo_fuente` el demo COMPLETO de la clase —87.786
caracteres de Java compilable en Prog II, repartidos en 12 archivos— y el deck proyectaba
solo `codigo_slide_lineas`: unas 15 lineas por clase. El estudiante veia el recorte y el
resto existia como archivo en el Kit docente, que es material del docente.

El docente reviso el material y pidio exactamente esto: «mas codigo si es programacion, mas
querys si es BD». Aqui se proyecta el codigo que se dicta, partido por donde tiene sentido
leerlo.

Como parte
----------
Por **unidad logica**, no por numero de lineas: en Java, cada metodo o miembro de nivel
superior; en SQL, cada sentencia. Asi la lamina se titula con lo que ensena
(`registrarMascota()`) y no con «codigo 3/7», y el bloque no se corta por la mitad.

`pseudo_code_slide` ya autoajusta el cuerpo y, si ni al minimo cabe, parte en dos columnas
por un limite de llaves equilibradas. Aqui se apunta a laminas de ~20 lineas para que no
tenga que hacerlo.
"""
from __future__ import annotations

import re

#: Lineas por lamina a las que se apunta. `pseudo_code_slide` aguanta mas —parte en dos
#: columnas—, pero una lamina de codigo que se lee de un vistazo es mas corta que una que
#: cabe: esto es limite de atencion, no de caja.
MAX_LINEAS = 20

#: Un bloque mas corto que esto se junta con el siguiente: un getter de tres lineas no vale
#: una lamina.
MIN_LINEAS = 4


def _sin_comentarios_de_licencia(lineas: list[str]) -> list[str]:
    """Quita el encabezado de comentario del archivo, que no ensena nada proyectado."""
    i = 0
    while i < len(lineas) and (not lineas[i].strip() or lineas[i].strip().startswith(("//", "/*", "*", "*/"))):
        i += 1
    return lineas[i:]


def _firma(linea: str) -> str | None:
    """El nombre legible de la unidad que abre esta linea, o None si no abre ninguna."""
    s = linea.strip()
    # metodo o constructor Java
    m = re.match(r"(?:public|private|protected|static|final|abstract|synchronized|\s)*"
                 r"(?:[\w<>\[\],\s]+\s+)?(\w+)\s*\([^;]*\)\s*(?:throws [\w,\s]+)?\{?\s*$", s)
    if m and m.group(1) not in ("if", "for", "while", "switch", "catch", "try", "return"):
        return m.group(1) + "()"
    # clase, interfaz, enum, record
    m = re.match(r"(?:public|private|protected|static|final|abstract|\s)*"
                 r"(class|interface|enum|record)\s+(\w+)", s)
    if m:
        return "%s %s" % (m.group(1), m.group(2))
    return None


def bloques_java(fuente: str) -> list[tuple[str, list[str]]]:
    """`(nombre, lineas)` por cada unidad de nivel superior del archivo."""
    lineas = _sin_comentarios_de_licencia(fuente.replace("\t", "    ").split("\n"))
    bloques: list[tuple[str, list[str]]] = []
    actual: list[str] = []
    nombre = "estructura"
    prof = 0
    for l in lineas:
        firma = _firma(l) if prof <= 1 else None
        if firma and actual and any(x.strip() for x in actual):
            bloques.append((nombre, actual))
            actual, nombre = [], firma
        elif firma:
            nombre = firma
        actual.append(l.rstrip())
        prof += l.count("{") - l.count("}")
    if any(x.strip() for x in actual):
        bloques.append((nombre, actual))
    return [(n, [x for x in ls]) for n, ls in bloques if any(x.strip() for x in ls)]


def bloques_sql(fuente: str) -> list[tuple[str, list[str]]]:
    """`(nombre, lineas)` por cada sentencia SQL del guion."""
    out = []
    for sent in re.split(r";\s*\n", fuente):
        s = sent.strip()
        if not s:
            continue
        m = re.match(r"(?is)^\s*(CREATE\s+(?:OR\s+REPLACE\s+)?\w+\s+\S+|ALTER\s+TABLE\s+\S+|"
                     r"INSERT\s+INTO\s+\S+|UPDATE\s+\S+|DELETE\s+FROM\s+\S+|SELECT|GRANT|REVOKE|EXPLAIN)", s)
        nombre = re.sub(r"\s+", " ", m.group(1)) if m else "sentencia"
        out.append((nombre, (s + ";").split("\n")))
    return out


def _empaquetar(bloques: list[tuple[str, list[str]]]) -> list[tuple[str, list[str]]]:
    """Junta los bloques cortos y parte los largos, apuntando a MAX_LINEAS."""
    out: list[tuple[str, list[str]]] = []
    pend_nombre, pend = None, []
    for nombre, ls in bloques:
        ls = [x for x in ls]
        if pend and len(pend) + len(ls) <= MAX_LINEAS:
            pend += [""] + ls
            pend_nombre = "%s · %s" % (pend_nombre, nombre) if pend_nombre else nombre
            continue
        if pend:
            out.append((pend_nombre or "codigo", pend))
            pend_nombre, pend = None, []
        if len(ls) <= MAX_LINEAS:
            if len(ls) < MIN_LINEAS:
                pend_nombre, pend = nombre, ls
            else:
                out.append((nombre, ls))
        else:
            trozos = [ls[i:i + MAX_LINEAS] for i in range(0, len(ls), MAX_LINEAS)]
            for i, tr in enumerate(trozos, 1):
                out.append(("%s (%d/%d)" % (nombre, i, len(trozos)), tr))
    if pend:
        out.append((pend_nombre or "codigo", pend))
    return out


#: Unidades que no se proyectan: no ensenan el tema y multiplican las laminas. El archivo
#: completo sigue en `Kit docente/Clase N/Codigo/`, que es donde el estudiante lo abre.
def _vale_proyectar(nombre: str, lineas: list[str]) -> bool:
    n = nombre.lower()
    if n == "estructura":                      # package + imports
        return False
    if n.startswith(("get", "set", "is")) and len(lineas) <= 6:
        return False                           # accesor trivial
    if n.startswith(("tostring", "equals", "hashcode")):
        return False
    return True


def slides_de_fuente(fuente: str, archivo: str = "", lenguaje: str = "java"):
    """Laminas de codigo del demo de la clase: `(titulo, lineas, [], 'codigo')`.

    El titulo dice QUE se esta mirando —`registrarMascota()`— y el archivo del que sale, para
    que el estudiante pueda abrirlo despues.
    """
    if not (fuente or "").strip():
        return []
    bloques = bloques_sql(fuente) if lenguaje == "sql" else bloques_java(fuente)
    if lenguaje != "sql":
        bloques = [(nm, ls) for nm, ls in bloques if _vale_proyectar(nm, ls)]
    base = archivo or ("codigo." + lenguaje)
    out = []
    for nombre, ls in _empaquetar(bloques):
        titulo = "%s — %s" % (base, nombre) if base else nombre
        if len(titulo) > 58:                   # una linea, o empuja el bloque de codigo
            titulo = nombre
        out.append((titulo, ls, [], "codigo"))
    return out


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    sys.path.insert(0, ".")
    import prog2_clases_data as P
    for c in P.CLASES:
        sl = slides_de_fuente(c.get("codigo_fuente") or "", c.get("codigo_archivo") or "")
        if sl:
            print("Clase %d: %d laminas de codigo" % (c["n"], len(sl)))
            for t, ls, _, _ in sl:
                print("   %2d lineas  %s" % (len(ls), t))
            break
