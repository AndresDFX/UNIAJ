# -*- coding: utf-8 -*-
"""Recupera estructuras desde el .pyc y reescribe contenido_parciales_2026_2.py en UTF-8."""
from __future__ import annotations

import marshal
import pickle
from pathlib import Path
from textwrap import dedent

HERE = Path(__file__).resolve().parent
PYC = HERE / "__pycache__" / "contenido_parciales_2026_2.cpython-314.pyc"
OUT = HERE / "contenido_parciales_2026_2.py"
PKL = HERE / "_recovered.pkl"


def _tema(n: int, fecha_dd_mm: str, tema: str) -> str:
    return f"Clase {n} · {fecha_dd_mm} · {tema}"


# Cobertura exacta por parcial (según PLAN_DE_CURSO_2026-2.md + regla fecha_clase <= fecha_parcial)
COBERTURA = {
    ("Programacion II", 1): {
        "cobertura": "Corte 1 · Únicamente clases con fecha <= 09/09/2026 (Clases 1-5):",
        "temas": [
            _tema(1, "12/08", "Introducción a POO"),
            _tema(2, "19/08", "Colecciones dinámicas ArrayList"),
            _tema(3, "26/08", "Pilas y colas"),
            _tema(4, "02/09", "Mapas y conjuntos"),
            _tema(5, "09/09", "Interfaces gráficas GUI"),
        ],
    },
    ("Programacion II", 2): {
        "cobertura": "Corte 2 · Únicamente clases con fecha <= 14/10/2026 en la ventana del corte (Clases 6-10). No evalúa POO/ArrayList/GUI del Corte 1:",
        "temas": [
            _tema(6, "16/09", "Eventos y controladores"),
            _tema(7, "23/09", "Patrones de diseño"),
            _tema(8, "30/09", "Documentación y QA"),
            _tema(9, "07/10", "Refactorización con IA"),
            _tema(10, "14/10", "Persistencia de archivos"),
        ],
    },
    ("Programacion II", 3): {
        "cobertura": "Corte 3 · Únicamente clases con fecha <= 18/11/2026 en la ventana del corte (Clases 11-15):",
        "temas": [
            _tema(11, "21/10", "Revisión de código cruzada"),
            _tema(12, "28/10", "Integración de módulos"),
            _tema(13, "04/11", "Control de excepciones"),
            _tema(14, "11/11", "Preparación presentación final"),
            _tema(15, "18/11", "Evaluación de proyectos + cierre"),
        ],
    },
    ("Seminario de Sistemas", 1): {
        "cobertura": "Corte 1 · Únicamente clases con fecha <= 10/09/2026 (Clases 1-5):",
        "temas": [
            _tema(1, "13/08", "Conceptos iniciales"),
            _tema(2, "20/08", "Ciclos de vida"),
            _tema(3, "27/08", "Metodologías tradicionales"),
            _tema(4, "03/09", "Metodologías ágiles"),
            _tema(5, "10/09", "Caso estudio evaluativo"),
        ],
    },
    ("Seminario de Sistemas", 2): {
        "cobertura": "Corte 2 · Únicamente clases con fecha <= 15/10/2026 en la ventana del corte (Clases 6-10). No evalúa ciclos de vida/metodologías del Corte 1:",
        "temas": [
            _tema(6, "17/09", "Requerimientos de software"),
            _tema(7, "24/09", "Historias de usuario"),
            _tema(8, "01/10", "Introducción a UML"),
            _tema(9, "08/10", "Casos de uso"),
            _tema(10, "15/10", "Caso estudio evaluativo"),
        ],
    },
    ("Seminario de Sistemas", 3): {
        "cobertura": "Corte 3 · Únicamente clases con fecha <= 19/11/2026 en la ventana del corte (Clases 11-15):",
        "temas": [
            _tema(11, "22/10", "Avance proyecto integrador"),
            _tema(12, "29/10", "Diagramas UML avanzados"),
            _tema(13, "05/11", "Diseño de interfaces"),
            _tema(14, "12/11", "Evaluación final (prep. sustentación)"),
            _tema(15, "19/11", "Sustentación de proyectos + cierre"),
        ],
    },
    ("Bases de Datos II", 1): {
        "cobertura": "Corte 1 · Únicamente clases con fecha <= 07/09/2026 (Clases 1-5):",
        "temas": [
            _tema(1, "10/08", "Revisión de Bases de Datos I"),
            _tema(2, "17/08", "Administración de bases de datos (autónoma)"),
            _tema(3, "24/08", "Procedimientos almacenados"),
            _tema(4, "31/08", "Funciones y disparadores"),
            _tema(5, "07/09", "Seguridad y respaldo"),
        ],
    },
    ("Bases de Datos II", 2): {
        "cobertura": "Corte 2 · Únicamente clases con fecha <= 05/10/2026 (Clases 6-9). NO incluye Clase 10 (concurrencia, 12/10):",
        "temas": [
            _tema(6, "14/09", "Optimización de consultas"),
            _tema(7, "21/09", "Índices y particionamiento"),
            _tema(8, "28/09", "Tuning de bases de datos"),
            _tema(9, "05/10", "Gestión de transacciones"),
        ],
    },
    ("Bases de Datos II", 3): {
        "cobertura": "Corte 3 · Únicamente clases con fecha <= 09/11/2026 (Clases 11-14). NO incluye Clase 15 (16/11):",
        "temas": [
            _tema(11, "19/10", "Avance del proyecto final"),
            _tema(12, "26/10", "Integración de aplicaciones externas"),
            _tema(13, "02/11", "Análisis de casos reales (autónoma)"),
            _tema(14, "09/11", "Preparación de presentación final"),
        ],
    },
    ("Arquitectura de Sistemas Computacionales", 1): {
        "cobertura": "Corte 1 · Únicamente clases con fecha <= 07/09/2026 (Clases 1-5):",
        "temas": [
            _tema(1, "10/08", "Introducción a arquitecturas cloud"),
            _tema(2, "17/08", "Modelos de servicio IaaS, PaaS, SaaS (autónoma)"),
            _tema(3, "24/08", "Virtualización y contenedores"),
            _tema(4, "31/08", "Microservicios"),
            _tema(5, "07/09", "Arquitecturas distribuidas"),
        ],
    },
    ("Arquitectura de Sistemas Computacionales", 2): {
        "cobertura": "Corte 2 · Únicamente clases con fecha <= 05/10/2026 (Clases 6-9). NO incluye Clase 10 (costos, 12/10):",
        "temas": [
            _tema(6, "14/09", "Seguridad en la nube"),
            _tema(7, "21/09", "Redes y almacenamiento cloud"),
            _tema(8, "28/09", "Monitoreo y optimización"),
            _tema(9, "05/10", "Integración continua y despliegue (CI/CD)"),
        ],
    },
    ("Arquitectura de Sistemas Computacionales", 3): {
        "cobertura": "Corte 3 · Únicamente clases con fecha <= 09/11/2026 (Clases 11-14). NO incluye Clase 15 (16/11):",
        "temas": [
            _tema(11, "19/10", "Avance del proyecto final"),
            _tema(12, "26/10", "Pruebas de rendimiento"),
            _tema(13, "02/11", "Escalabilidad automática (autónoma)"),
            _tema(14, "09/11", "Preparación de presentación final"),
        ],
    },
}


def patch_questions(parcial: dict) -> None:
    """Elimina fugas de temas fuera del corte."""
    meta = parcial["meta"]
    key = (meta["curso_dir"], meta["n"])

    # ARQ P3: no preguntar costos (Clase 10)
    if key == ("Arquitectura de Sistemas Computacionales", 3):
        for sec in parcial["secciones"]:
            for item in sec["items"]:
                if item.get("id") == "D1" and item.get("requerimientos"):
                    item["requerimientos"] = [
                        "a) Contexto y objetivos (5 pts)",
                        "b) Diagrama lógico (describa capas/servicios) (10 pts)",
                        "c) Estrategia de pruebas de rendimiento (10 pts)",
                        "d) Política de escalado automático propuesta (5 pts)",
                        "e) Riesgos, limitaciones o trabajo futuro del avance (5 pts) - sin evaluar costos/sostenibilidad de Clase 10",
                    ]
                    item["solucion"] = [
                        "Coherencia arquitectura-pruebas-escalado; trade-offs claros; sin secretos en láminas; sin costos de Clase 10.",
                    ]

    # BD2 P3: anclar a avance/integración/casos/prep (no re-examinar C1/C2 a fondo)
    if key == ("Bases de Datos II", 3):
        for sec in parcial["secciones"]:
            for item in sec["items"]:
                if item.get("id") == "A4":
                    item["pregunta"] = (
                        "Para la preparación de la presentación final del proyecto de BD II es clave mostrar:"
                    )
                    item["opciones"] = [
                        "a) Solo capturas sin explicar el avance",
                        "b) Avance del PI, integración con apps, lecciones de casos y guion de sustentación",
                        "c) Únicamente el logo del SGBD",
                        "d) Código ofuscado sin demo",
                    ]
                    item["clave"] = "b"
                if item.get("id") == "D1" and item.get("requerimientos"):
                    item["requerimientos"] = [
                        "a) Problema y objetivos del PI (5 pts)",
                        "b) Estado de avance y entregables listos / pendientes (10 pts)",
                        "c) Diseño de integración con aplicación externa (API/SQL, credenciales, errores) (10 pts)",
                        "d) Una lección de un caso real aplicable a su proyecto (5 pts)",
                        "e) Guion de presentación (orden de láminas / demo) (5 pts)",
                    ]
                    item["solucion"] = [
                        "Evaluar completitud y coherencia con temas del Corte 3 (avance, integración, casos, prep.); pts según rúbrica.",
                    ]
                if item.get("id") == "B4":
                    item["enunciado"] = (
                        "Un avance de proyecto final debería alinear entregables con la integración, "
                        "análisis de casos y la preparación de la sustentación del corte."
                    )
                    item["clave"] = "V"
                    item["justificacion"] = "Trazabilidad con Clases 11-14 del Corte 3."


def recover() -> list:
    code = marshal.loads(PYC.read_bytes()[16:])
    ns: dict = {"__name__": "contenido_parciales_2026_2"}
    exec(code, ns)
    todos = ns["TODOS"]
    for parcial in todos:
        meta = parcial["meta"]
        cov = COBERTURA[(meta["curso_dir"], meta["n"])]
        meta["cobertura"] = cov["cobertura"]
        meta["temas"] = list(cov["temas"])
        patch_questions(parcial)
    PKL.write_bytes(pickle.dumps(todos))
    return todos


def emit_source(todos: list) -> str:
    """Emite módulo Python legible con los parciales ya parcheados."""
    # Representación: import pickle + datos embebidos sería opaco.
    # Mejor: generar fuente con pprint de estructuras.
    import pprint

    parts = [
        dedent(
            '''\
            # -*- coding: utf-8 -*-
            """Contenido de los 12 parciales UNIAJC 2026-2 (4 cursos x 3 cortes).

            Regla de cobertura (obligatoria):
              - Solo clases con fecha en la ventana del corte Y fecha_clase <= fecha_parcial.
              - En BD II / Arquitectura: P2 = clases 6-9 (NO 10); P3 = clases 11-14 (NO 15).
              - Clase 1: se evalua el arranque tematico (no la logistica de Presentacion del curso).
              - Formato en portada: «Clase N · DD/MM · Tema».
            """
            from __future__ import annotations

            ROOT = r"G:\\Mi unidad\\Trabajos\\Empleo\\UNIAJ\\Cursos"


            def _tema(n: int, fecha_dd_mm: str, tema: str) -> str:
                return f"Clase {n} · {fecha_dd_mm} · {tema}"


            def _meta(**kw):
                return kw


            def _sec(titulo, pts, items, intro=""):
                return {"titulo": titulo, "pts": pts, "items": items, "intro": intro}

            '''
        )
    ]

    names = [
        "PROG2_P1",
        "PROG2_P2",
        "PROG2_P3",
        "SEM_P1",
        "SEM_P2",
        "SEM_P3",
        "BD2_P1",
        "BD2_P2",
        "BD2_P3",
        "ARQ_P1",
        "ARQ_P2",
        "ARQ_P3",
    ]

    # Course headers as comments + assign each parcial
    for name, parcial in zip(names, todos):
        # Rebuild meta via _meta for readability of temas with _tema()
        meta = dict(parcial["meta"])
        temas = meta.pop("temas")
        cobertura = meta.pop("cobertura")
        # Keep course fields inline
        parts.append(f"\n{name} = {{\n")
        parts.append('    "meta": _meta(\n')
        for k, v in meta.items():
            parts.append(f"        {k}={pprint.pformat(v)},\n")
        parts.append(f"        cobertura={pprint.pformat(cobertura)},\n")
        parts.append("        temas=[\n")
        for t in temas:
            # t is "Clase N · DD/MM · Tema"
            bits = t.split(" · ", 2)
            if len(bits) == 3:
                n = int(bits[0].replace("Clase ", ""))
                parts.append(f"            _tema({n}, {pprint.pformat(bits[1])}, {pprint.pformat(bits[2])}),\n")
            else:
                parts.append(f"            {pprint.pformat(t)},\n")
        parts.append("        ],\n")
        parts.append("    ),\n")
        parts.append(f'    "secciones": {pprint.pformat(parcial["secciones"], width=100)},\n')
        parts.append("}\n")

    parts.append("\nTODOS = [\n")
    for name in names:
        parts.append(f"    {name},\n")
    parts.append("]\n")
    return "".join(parts)


def main() -> int:
    todos = recover()
    src = emit_source(todos)
    OUT.write_text(src, encoding="utf-8", newline="\n")
    print(f"OK wrote {OUT} ({OUT.stat().st_size} bytes)")
    for p in todos:
        m = p["meta"]
        print(f"\n{m['curso_dir']} · Parcial {m['n']} · {m['fecha']}")
        for t in m["temas"]:
            print(f"  - {t}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
