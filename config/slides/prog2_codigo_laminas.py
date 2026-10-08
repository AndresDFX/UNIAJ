# -*- coding: utf-8 -*-
"""Las laminas de codigo de Programacion II: un PROGRAMA COMPLETO por lamina.

Antes cada lamina era un recorte del archivo de la clase (un metodo sin su clase, un cuerpo
sin su metodo, sin imports): se entendia, pero al copiarlo a un compilador no corria. Ahora
cada lamina es un `Main.java` que se sostiene solo, igual que las consultas de BD II: se
copia, se pega y corre, sin la lamina anterior ni el archivo del Kit docente.

Datos: `prog2_codigo_cN.py` (uno por clase) con
  ``CLASE = N`` y ``LAMINAS = [{"k", "titulo", "codigo", "salida"}, ...]``
  - ``k``: la lamina va DETRAS del concepto ``k`` (posicion en ``prog2_conceptos_data.CONCEPTOS[N]``).
  - ``titulo``: el de la lamina (no cambia el deck ni el guion).
  - ``codigo``: el programa. Reglas, que `verificar_java_laminas.py` comprueba:
      * compila solo con ``javac --release 17`` (el JDK del curso) en un archivo ``Main.java``;
      * la primera clase es ``class Main`` con ``main`` y ninguna clase es ``public``, para que
        corra pegado en un archivo de cualquier nombre, con ``java Main.java`` o en un
        compilador en linea;
      * sin ``package``, sin ``Scanner`` ni hora/azar en la salida (salvo que el tema lo pida);
      * solo ASCII (el JDK 17 en Windows no lee UTF-8 por defecto);
      * cabe sin partir ninguna linea: hasta ``UNA_COLUMNA`` lineas va en una columna ancha
        (``ANCHO_UNA`` caracteres); mas largo va en dos columnas de ``COLUMNA`` lineas y
        ``MAX_ANCHO`` caracteres, cortadas entre clases o entre dos metodos;
      * nada del proyecto (VetCare, Huellitas, ExamLab...): una clinica veterinaria cualquiera.
  - ``salida``: lo que imprime, exacto (se compara al ejecutarlo). ``None`` en las ventanas
    Swing (solo se compilan) y donde el tema es justamente lo que varia (medir tiempos).
  - ``nota`` (opcional): una linea mas para las notas del presentador.

El archivo completo de la clase sigue en `Kit docente/Clase N/Codigo/`.
"""
import glob
import importlib
import os

#: Letra minima 10 pt (en Meet, a pantalla completa en 1080p, son ~20 px: mas que la letra
#: por defecto de VS Code) e interlineado de 1 pt: una columna de ~26 lineas de ~130
#: caracteres, o dos de ~26 lineas de 60. Se deja una linea de margen.
MINIMO_PT = 10
INTERLINEADO = 1
UNA_COLUMNA = 25
ANCHO_UNA = 100
COLUMNA = 25
MAX_LINEAS = 50
MAX_ANCHO = 60

ARCHIVO = "Main.java"

CODIGO = {}
_aqui = os.path.dirname(os.path.abspath(__file__))
for _f in sorted(glob.glob(os.path.join(_aqui, "prog2_codigo_c*.py"))):
    _m = importlib.import_module(os.path.splitext(os.path.basename(_f))[0])
    CODIGO[_m.CLASE] = _m.LAMINAS


def lineas(entrada):
    return entrada["codigo"].strip("\n").split("\n")


def notas(entrada):
    """Notas del presentador de una lamina de codigo: como correrlo y que debe salir."""
    out = ["COMO CORRERLO: es un programa completo. Se copia entero en un archivo Main.java "
           "(o en cualquier compilador de Java en linea) y se ejecuta: no necesita la lamina "
           "anterior ni otro archivo."]
    if entrada.get("salida"):
        out += ["SALIDA ESPERADA:"] + entrada["salida"].strip("\n").split("\n")
    elif "javax.swing" in entrada["codigo"]:
        out.append("SALIDA ESPERADA: abre la ventana; por consola no imprime nada que comparar.")
    if entrada.get("nota"):
        out.append(entrada["nota"])
    return out
