# -*- coding: utf-8 -*-
"""BD II · Ilustracion generada para cada lamina de viñetas que no tiene animacion propia.

`ILUSTRACIONES[(curso, n)] = {comienzo_de_titulo: "<curso>/claseN/<huella>"}`. `curso` es
bd2 | arq | prog2 | seminario | intro; `n` la clase. La clave `"*"` vale para todas. El titulo
es el que pasa a `content_slide`, sin importar tildes ni mayusculas. El modulo es de
`config/animaciones/` con `pasos: [1]` (un solo fotograma), renderizado con `renderizar.py`.

Las laminas de marco (encuadre, objetivos, agenda, indicaciones, orden de la sesion) no llevan
imagen: ver `_SIN_VISUAL` en `uniajc_slides_engine.py`.
"""

ILUSTRACIONES = {
    ("bd2", 4): {
        "La funcion de tarifas:": "bd2/clase4/ilus-firma-funcion",
        "Donde vive cada validacion": "bd2/clase4/ilus-donde-validar",
        "Plan de respaldo": "bd2/clase4/ilus-plan-respaldo",
        "Lo que PostgreSQL en el navegador": "bd2/clase4/ilus-navegador-papel",
        "Como amarra con las clases vecinas": "bd2/clase4/ilus-amarre",
        "Demo del dia": "bd2/clase4/ilus-demo",
    },
}
