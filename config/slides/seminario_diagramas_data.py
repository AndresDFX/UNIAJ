# -*- coding: utf-8 -*-
"""Seminario de Sistemas: el dibujo de cada lamina de codigo de diagrama (ver `diagramas_codigo`).

La clave es el comienzo del titulo TAL COMO SALE EN EL DECK (despues del filtro `_deck` del
builder). Cada dibujo reproduce las cajas, flechas y rotulos del Mermaid de su lamina.
"""

DIAGRAMAS = {
    ("seminario", 1): {
        "El mapa de dominio en Mermaid": "seminario/clase1/dg-mapa-dominio",
    },
    ("seminario", 2): {
        "El recorrido lineal del ciclo de vida": "seminario/clase2/dg-lineal",
        "El ciclo de vida en Mermaid": "seminario/clase2/dg-ciclo",
        "El mismo ciclo en tres vueltas": "seminario/clase2/dg-tres-vueltas",
    },
    ("seminario", 3): {
        "El modelo en V con trazabilidad": "seminario/clase3/dg-modelo-v",
    },
    ("seminario", 4): {
        "El plan de sprints en Mermaid": "seminario/clase4/dg-gantt-sprints",
        "El tablero de flujo con limite": "seminario/clase4/dg-tablero",
    },
    ("seminario", 6): {
        "La priorizacion MoSCoW en Mermaid": "seminario/clase6/dg-moscow",
    },
    ("seminario", 7): {
        "El mapa del backlog": "seminario/clase7/dg-backlog",
    },
    ("seminario", 8): {
        "El diagrama de clases en Mermaid": "seminario/clase8/dg-clases",
        "Lo que NO es una clase del dominio": "seminario/clase8/dg-no-es-clase",
        "Modelo de dominio completo en Mermaid": "seminario/clase8/dg-dominio-completo",
    },
    ("seminario", 9): {
        "El diagrama de casos de uso en Mermaid": "seminario/clase9/dg-casos-uso",
    },
    ("seminario", 12): {
        "El diagrama de secuencia en Mermaid": "seminario/clase12/dg-secuencia",
        "Secuencia de CU-04 Agendar cita": "seminario/clase12/dg-secuencia-cu04",
        "El diagrama de actividad con decisiones": "seminario/clase12/dg-actividad",
    },
    ("seminario", 13): {
        "El mapa de navegacion del prototipo": "seminario/clase13/dg-navegacion",
        "Flujo de tarea con caminos alternos": "seminario/clase13/dg-flujo-tarea",
    },
    ("seminario", 14): {
        "El guion cronometrado de la sustentacion": "seminario/clase14/dg-guion-gantt",
    },
}
