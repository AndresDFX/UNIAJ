# -*- coding: utf-8 -*-
"""Clase 1 estudiante — Introducción a POO (Programación II · UNIAJC).

Solo tema de esta clase + nº discreto. Sin fechas de periodo, sin mapa del curso,
sin bio docente (eso va en Presentación del Curso).

SUPERSEDIDO (2026-2)
--------------------
Escribe en `Clase 1 - Introduccion a POO`, carpeta que ya no existe: tras la
reconstruccion la Clase 1 la genera `build_uniajc_prog2_all.py` desde
`prog2_clases_data.py`. Correr esto crearia una carpeta huerfana y duplicaria la
clase. Se conserva por historia.
"""
import os
import sys

sys.exit(
    "SUPERSEDIDO: la Clase 1 de Prog II la genera build_uniajc_prog2_all.py\n"
    "desde prog2_clases_data.py. Correr esto crearia una carpeta duplicada."
)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uniajc_slides_engine import (
    new_prs, content_slide, table_content, box_note_slide, closing_slide,
    class_cover, block_timeline_slide,
)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(ROOT, "Programacion II", "Clases", "Clase 1 - Introduccion a POO")
OUT = os.path.join(OUT_DIR, "Presentacion.pptx")


def cover(prs):
    class_cover(
        prs,
        "Introducción a POO",
        subtitulo="Clase vs objeto · encapsulamiento · entorno listo",
        clase_n=1,
        idx=1,
    )


def build():
    prs = new_prs()
    cover(prs)

    # 2ª slide: encuadre (salido de la portada) + puente a objetivos
    content_slide(
        prs, "Encuadre de hoy",
        [
            "Objetivo de hoy: activar el modelo mental de POO y dejar el entorno + el arranque del Proyecto Integrador.",
            "Bloque: **120 min** · Diagnóstico · Teoría Core · Laboratorio · Primer avance del proyecto.",
            "Entorno local: JDK + IDE · sin software de pago obligatorio.",
        ],
        idx=2,
    )

    block_timeline_slide(
        prs, "Mapa del bloque de hoy (120 min)",
        [
            ("0-10", "Encuadre temático (Sesión 0 ya quedó atrás)"),
            ("10-35", "Diagnóstico de previos"),
            ("35-70", "Teoría Core: clase vs objeto"),
            ("70-100", "Laboratorio: JDK + IDE + HolaPOO"),
            ("100-120", "PI: primer avance · cierre"),
        ],
        idx=3,
    )

    content_slide(
        prs, "Objetivos de la clase",
        [
            "Diferenciar con precisión **clase** (molde) y **objeto** (instancia en memoria).",
            "Identificar atributos (estado) y métodos (comportamiento) en un dominio simple.",
            "Dejar el **entorno de desarrollo** listo (JDK + IDE + proyecto compilando).",
            "Comprender el alcance del **Proyecto Integrador** y fijar el primer avance.",
        ],
        idx=4,
    )

    content_slide(
        prs, "Clase vs Objeto (analogía)",
        [
            "@@Clase@@ = el molde de galleta (plano/especificación).",
            "@@Objeto@@ = cada galleta horneada (existe en memoria RAM).",
            "Puedes crear **muchos objetos** a partir de una misma clase.",
            "Cada objeto tiene su propia copia de los **atributos** (estado).",
            "Los **métodos** definen qué puede hacer el objeto.",
        ],
        idx=5,
    )

    table_content(
        prs, "Cuatro pilares de la POO (mapa rápido de hoy)",
        ["Pilar", "Idea clave", "Señal de que lo entendiste"],
        [
            ["Encapsulamiento", "Datos protegidos + API pública", "Atributos private + getters/setters con sentido"],
            ["Herencia", "Reutilizar y especializar", "Subclase sin copiar/pegar código"],
            ["Polimorfismo", "Misma interfaz, distinta forma", "Una lista de Animal con perro/gato"],
            ["Abstracción", "Modelar lo esencial", "Clase que refleja el dominio, no la UI"],
        ],
        idx=6,
    )

    content_slide(
        prs, "Mini-demo en código (mental)",
        [
            "`class Mascota { private String nombre; … }`",
            "`Mascota m1 = new Mascota(\"Luna\");`",
            "`Mascota m2 = new Mascota(\"Rocky\");`",
            "m1 y m2 son **dos objetos**; comparten la clase, no el estado.",
            "Error frecuente: confundir el nombre de la clase con una variable… o dejar referencias `null`.",
        ],
        idx=7,
    )

    content_slide(
        prs, "Laboratorio: entorno listo",
        [
            "Verificar **JDK 17+** (`java -version`, `javac -version`).",
            "Abrir **VS Code** con el Extension Pack for Java y crear el proyecto `Prog2_Clase01`.",
            "Crear paquete `co.edu.uniajc.prog2` y clase `HolaPOO` con `main`.",
            "Compilar y ejecutar. Captura/ok verbal al docente = listo.",
            "Independiente dirigido de la semana: terminar configuración y lectura de conceptos previos.",
        ],
        idx=8,
    )

    content_slide(
        prs, "Proyecto Integrador — primer contacto",
        [
            "Hoy leemos el enunciado, aclaramos el dominio y definimos el **primer avance**.",
            "Entregable de salida: problema en 2–3 frases + **3 entidades** candidatas + 1 funcionalidad cercana.",
            "Criterio de hoy: cada estudiante/equipo deja escrito el problema que resolverá.",
            "Detalle de peso y cortes: Presentación del Curso / Acuerdo pedagógico (no se repite aquí).",
        ],
        idx=9,
    )

    box_note_slide(
        prs, "Para esta semana",
        [
            ("aclaracion", "Independiente: lectura de conceptos previos de POO + entorno 100% funcional."),
            ("info", "Traer a la siguiente clase dudas concretas de ArrayList (siguiente trabajo dirigido)."),
            ("advertencia", "El taller/actividad de la semana se entrega a más tardar el domingo 23:59 (regla del Acuerdo)."),
        ],
        idx=10,
    )

    closing_slide(
        prs,
        "Clase 1 lista",
        [
            "Molde ≠ galleta · Clase ≠ objeto",
            "Entorno arriba · Proyecto Integrador encendido",
            "Siguiente paso del tema: colecciones dinámicas (ArrayList)",
        ],
        accent="Entorno listo · ficha del proyecto escrita",
    )

    os.makedirs(OUT_DIR, exist_ok=True)
    prs.save(OUT)
    print("OK ->", OUT)


if __name__ == "__main__":
    build()
