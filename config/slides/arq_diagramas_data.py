# -*- coding: utf-8 -*-
"""Arquitectura: el dibujo que va junto a cada lamina de codigo de diagrama (ver `diagramas_codigo`).

Cada ilustracion reproduce EXACTAMENTE las cajas, nombres, flechas y rotulos del codigo de su
lamina; si el codigo cambia, el dibujo cambia con el. (La Clase 4 lo hace por `CODIGO_DIAGRAMA`
de `arq_visuales_data`, que ademas trae las notas.)
"""

DIAGRAMAS = {
    ("arq", 1): {"El C4 Context en Mermaid": "arq/clase1/dg-c4-context"},
    ("arq", 7): {
        "Que tipo de almacenamiento pide cada componente": "arq/clase7/dg-almacenamiento",
        "El Despliegue en Mermaid": "arq/clase7/dg-despliegue",
    },
    ("arq", 11): {"El C4 Component: por dentro de la API": "arq/clase11/dg-c4-component"},
    ("arq", 12): {"El presupuesto de latencia del camino critico": "arq/clase12/dg-latencia"},
    ("arq", 13): {"La maquina de decision del autoescalado": "arq/clase13/dg-autoescalado"},
}
