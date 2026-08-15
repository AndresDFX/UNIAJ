# -*- coding: utf-8 -*-
"""Diapositivas de la Clase 1 de Seminario de Sistemas (material del estudiante).

Por que existe
--------------
`Clases/Clase 1 - Conceptos iniciales/` no tenia diapositivas propias: lo unico que
habia ahi era la *Presentacion del Curso* del periodo anterior, mal ubicada dentro de
la carpeta de la clase. Es decir, la Clase 1 era la unica del curso sin material de
estudiante para su tema.

Acompaña al guion `Kit docente/Clase 1/Guion Docente Clase 1 - Conceptos iniciales.md`.
Solo el tema de ESTA clase: nada de logistica del semestre (eso vive en la Sesion 0),
sin bio del docente, sin fechas de periodo y sin anunciar el quiz.

SUPERSEDIDO (2026-2)
--------------------
Desde la reconstruccion del curso, la Clase 1 la genera `build_uniajc_seminario_all.py`
a partir de `seminario_clases_data.py`, igual que las otras 14. Correr este script
sobrescribiria esa salida con la version vieja, asi que se bloquea a proposito. Se
conserva por historia; para cambiar la Clase 1 se edita el modulo de datos.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.exit(
    "SUPERSEDIDO: la Clase 1 de Seminario la genera build_uniajc_seminario_all.py\n"
    "desde seminario_clases_data.py. Correr esto revertiria la reconstruccion 2026-2."
)

ROOT = Path(__file__).resolve().parents[2]
SLIDES = Path(__file__).resolve().parent
sys.path.insert(0, str(SLIDES))

from uniajc_slides_engine import (  # noqa: E402
    AMARILLO,
    CIAN,
    NAVY,
    block_timeline_slide,
    box_note_slide,
    class_cover,
    closing_slide,
    content_slide,
    diagram_boxes_slide,
    new_prs,
    two_column_slide,
)

OUT = (ROOT / "Seminario de Sistemas" / "Clases" /
       "Clase 1 - Conceptos iniciales" / "Presentacion.pptx")


def build() -> Path:
    prs = new_prs()
    class_cover(prs, "Conceptos iniciales de ingenieria de software",
                subtitulo="Que es diseñar software y por que no es programar",
                clase_n=1, idx=1)

    content_slide(prs, "Objetivos de la clase", [
        "Distinguir **programar** de **hacer ingenieria de software**.",
        "Diferenciar **requisito funcional** y **no funcional**, y escribirlos de forma verificable.",
        "Identificar a los **interesados** de un sistema y sus intereses en conflicto.",
        "**Acotar el dominio** del proyecto del semestre (trabajo individual).",
    ], idx=2)

    block_timeline_slide(prs, "Mapa del bloque de hoy (120 min)", [
        ("0-15", "Encuadre del tema"),
        ("15-35", "Prueba diagnostica (sin nota)"),
        ("35-70", "Teoria: conceptos iniciales"),
        ("70-100", "Taller: acotar el dominio"),
        ("100-120", "Puesta en comun y cierre"),
    ], idx=3)

    two_column_slide(
        prs, "Programar no es lo mismo que hacer ingenieria",
        left_title="Programar",
        left_items=[
            "Escribir codigo que funcione **hoy**.",
            "El exito es: «compila y corre».",
            "El alcance cabe en la cabeza de una persona.",
        ],
        right_title="Ingenieria de software",
        right_items=[
            "Que siga funcionando cuando **crece**, cuando lo mantiene **otra persona** "
            "y cuando **cambian** los requisitos.",
            "El exito es: se puede modificar sin romperlo.",
            "El alcance excede a una sola persona → hacen falta planos.",
        ],
        sub="La diferencia se paga en dinero: corregir un error tarde cuesta mucho mas que detectarlo temprano",
        idx=4,
    )

    diagram_boxes_slide(
        prs, "El costo de un error crece con el tiempo",
        boxes=[
            {"id": "req", "label": "Requisitos\n(barato)", "x": 0.9, "y": 3.0,
             "w": 2.4, "h": 1.1, "color": CIAN},
            {"id": "dis", "label": "Diseño", "x": 4.0, "y": 3.0, "w": 2.4, "h": 1.1, "color": CIAN},
            {"id": "cod", "label": "Construccion", "x": 7.1, "y": 3.0, "w": 2.4, "h": 1.1, "color": NAVY},
            {"id": "pro", "label": "Produccion\n(carisimo)", "x": 10.2, "y": 3.0,
             "w": 2.4, "h": 1.1, "color": AMARILLO, "text_color": NAVY},
        ],
        arrows=[
            {"src": "req", "dst": "dis"},
            {"src": "dis", "dst": "cod"},
            {"src": "cod", "dst": "pro"},
        ],
        note="Por eso existe todo lo que veremos este semestre: mover la deteccion de errores "
             "hacia la izquierda de esta linea.",
        idx=5,
    )

    content_slide(prs, "Requisitos: funcionales vs no funcionales", [
        "**Funcional (QUE hace):** «registrar una mascota con ID, nombre y especie».",
        "**No funcional (COMO se comporta):** «la busqueda responde en menos de 2 segundos»; "
        "«la informacion no se pierde ante un corte de energia».",
        "Los **no funcionales** son los que mas se olvidan y los que mas condicionan el diseño.",
        "@@Regla practica:@@ si no se puede **verificar**, no es un requisito — es un deseo. "
        "«Debe ser rapido» no sirve; «responde en <2 s con 50 usuarios» si.",
    ], idx=6, size=15)

    content_slide(prs, "Interesados: no solo el que paga", [
        "**Dueño de la clinica:** quiere metricas del negocio.",
        "**Recepcionista:** quiere agendar rapido, con pocos clics.",
        "**Veterinario:** quiere el historial del paciente a la mano.",
        "Sus intereses **entran en conflicto** (mas datos = mas lento de registrar). "
        "Resolver ese conflicto es trabajo de analisis, no de programacion.",
    ], idx=7, size=15)

    content_slide(prs, "Ciclo de vida: siempre las mismas fases", [
        "Requisitos → Diseño → Construccion → Pruebas → Mantenimiento.",
        "Lo que cambia entre metodologias no son las fases: es **como se recorren**.",
        "Una sola vez y en orden (cascada) o en **ciclos cortos** que repiten todo (iterativo/agil).",
        "Las comparamos a fondo en las Clases 2, 3 y 4.",
    ], idx=8)

    content_slide(prs, "Taller de hoy — acotar el dominio", [
        "**1.** Trabajo **individual**: cada uno llena su propia ficha de dominio.",
        "**2.** Escriban el **problema** en 2-3 frases (quien sufre que).",
        "**3.** Listen **3-5 capacidades** del sistema.",
        "**4.** Identifiquen **2-3 actores**.",
        "**5.** Escriban que **NO** hara el sistema (fuera de alcance).",
    ], idx=9)

    box_note_slide(prs, "Criterio de exito del taller", [
        ("info", "El dominio es concreto: se entiende en 30 segundos sin que ustedes lo expliquen."),
        ("aclaracion", "Hay un actor con un dolor medible, no «usuarios» en abstracto."),
        ("advertencia", "«Una app para la universidad» NO sirve: sin problema concreto, "
                        "todo el semestre se vuelve humo."),
    ], idx=10)

    closing_slide(prs, "Clase 1 lista", [
        "Ya distinguen programar de diseñar",
        "Dominio acotado en su ficha",
        "Siguiente clase: ciclos de vida del software",
    ], accent="En esta materia ustedes son los arquitectos")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUT))
    print("OK ->", OUT.relative_to(ROOT))
    return OUT


if __name__ == "__main__":
    build()
