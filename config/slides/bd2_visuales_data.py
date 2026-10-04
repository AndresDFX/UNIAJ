# -*- coding: utf-8 -*-
"""Que visual acompana a cada concepto de Bases de Datos II: animacion, foto o nada.

Clave: el comienzo del titulo de la seccion `###` del fundamento (sin tildes ni mayusculas
importan: se compara normalizado). Valor:

- ``anim``: carpeta/huella en `config/animaciones/` (renderizada a GIF por `renderizar.py`).
  La primera lamina de la seccion lleva el GIF; las de continuacion, sus fijos (mitad, final).
- ``foto``: consulta para Pexels, en ingles. Se usa en las laminas que no tienen animacion.

Una seccion sin entrada se queda en texto a ancho completo: el visual se pone donde explica,
no por decorar. Las laminas de codigo nunca llevan visual (el codigo necesita el ancho).
"""

VISUALES = {
    4: {
        "Funcion y procedimiento": {"anim": "bd2/clase4/funcion-o-procedimiento"},
        "Los tres detalles de fn_precio_consulta": {"anim": "bd2/clase4/fn-precio-consulta"},
        "El trigger: el unico que nadie invoca": {"anim": "bd2/clase4/trigger-dos-objetos"},
        "BEFORE o AFTER": {"anim": "bd2/clase4/before-after"},
        "La auditoria": {"anim": "bd2/clase4/auditoria-when"},
        "El trigger que impide": {"anim": "bd2/clase4/trigger-que-impide"},
        "Las cuatro capas": {"anim": "bd2/clase4/cuatro-capas"},
        "Cuando NO se usa un trigger": {"anim": "bd2/clase4/cuando-no-trigger"},
        "Seguridad y respaldo": {"anim": "bd2/clase4/seguridad-respaldo",
                                 "foto": "server room data backup"},
        "RPO y RTO": {"anim": "bd2/clase4/rpo-rto", "foto": "clock deadline office"},
        "Lo que PostgreSQL en el navegador": {"foto": "laptop code editor database"},
        "Como amarra con las clases vecinas": {"foto": "puzzle pieces connected"},
        "Preguntas frecuentes": {"foto": "students asking questions classroom"},
    },
}

#: Presupuesto de texto de una lamina que comparte el ancho con un visual.
MAX_CAR_CON_VISUAL = 480
MAX_VINETAS_CON_VISUAL = 4
