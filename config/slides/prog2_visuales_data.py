# -*- coding: utf-8 -*-
"""Que visual acompana a cada concepto de Programacion II: animacion, foto o nada.

Clave: el comienzo del titulo del concepto tal como esta en `prog2_conceptos_data.CONCEPTOS`
(se compara sin tildes ni mayusculas). Valor:

- ``anim``: carpeta/huella en `config/animaciones/` (renderizada por `renderizar.py`). En la
  lamina sus pasos aparecen uno por clic del docente.
- ``foto``: consulta para Pexels, en ingles; se usa si no hay animacion renderizada.

Prioridad del curso: estructuras de datos (pila, cola, mapa, conjunto), eventos, patrones y
excepciones, que son procesos con pasos. Un concepto sin entrada se queda en texto a ancho
completo: el visual se pone donde explica. Las laminas de codigo nunca llevan visual.
"""

VISUALES = {
    1: {
        "Del programa estructurado": {"anim": "prog2/clase1/estructurado-vs-objeto"},
        "Clase y objeto": {"anim": "prog2/clase1/clase-objeto"},
        "El objeto en memoria": {"anim": "prog2/clase1/pila-monton"},
        "== compara referencias": {"anim": "prog2/clase1/igual-equals"},
        "Encapsular es proteger": {"anim": "prog2/clase1/encapsular-regla"},
        "Herencia y polimorfismo": {"anim": "prog2/clase1/herencia-polimorfismo"},
        "El constructor": {"anim": "prog2/clase1/constructor-valido"},
        "null y NullPointerException": {"anim": "prog2/clase1/null-control"},
    },
    2: {
        "El arreglo tiene": {"anim": "prog2/clase2/arreglo-fijo"},
        "ArrayList por dentro": {"anim": "prog2/clase2/arraylist-crece"},
        "Recorrer": {"anim": "prog2/clase2/recorrer-iterator"},
        "La lista encapsulada": {"anim": "prog2/clase2/lista-encapsulada"},
    },
    3: {
        "Cuando la lista permite": {"anim": "prog2/clase3/lista-vs-cola"},
        "La cola": {"anim": "prog2/clase3/cola-fifo"},
        "La pila": {"anim": "prog2/clase3/pila-lifo"},
        "Por que son rapidas": {"anim": "prog2/clase3/arreglo-circular"},
        "Una cola no se recorre": {"anim": "prog2/clase3/urgencia-addfirst"},
    },
    4: {
        "De la busqueda lineal": {"anim": "prog2/clase4/busqueda-hash"},
        "La API de Map": {"anim": "prog2/clase4/map-put-get"},
        "HashSet": {"anim": "prog2/clase4/hashset-duplicados"},
        "Swing": {"anim": "prog2/clase4/swing-anidamiento"},
    },
    6: {
        "Del programa en linea recta": {"anim": "prog2/clase6/edt-eventos"},
        "ActionListener": {"anim": "prog2/clase6/listener-registro"},
        "Separar la logica": {"anim": "prog2/clase6/tres-capas"},
        "Un clic en camara lenta": {"anim": "prog2/clase6/clic-camara-lenta"},
    },
    7: {
        "El problema: un solo archivador": {"anim": "prog2/clase7/dos-archivadores"},
        "Singleton": {"anim": "prog2/clase7/singleton-instancia"},
        "Factory": {"anim": "prog2/clase7/factory-decide"},
    },
    8: {
        "Anatomia de un bloque Javadoc": {"anim": "prog2/clase8/javadoc-anatomia"},
        "Un caso de prueba": {"anim": "prog2/clase8/caso-aaa"},
        "JUnit": {"anim": "prog2/clase8/junit-resultados"},
    },
    9: {
        "Refactorizar": {"anim": "prog2/clase9/refactor-misma-salida"},
        "Persistencia": {"anim": "prog2/clase9/ram-a-disco"},
        "Cerrar el recurso": {"anim": "prog2/clase9/buffer-close"},
        "Cargar al arrancar": {"anim": "prog2/clase9/carga-defensiva"},
    },
    11: {
        "Revisar por capas": {"anim": "prog2/clase11/capas-revision"},
        "Retroalimentacion": {"anim": "prog2/clase11/comentario-util"},
    },
    12: {
        "Integrar: piezas": {"anim": "prog2/clase12/capas-dependencia"},
        "El guion de humo": {"anim": "prog2/clase12/guion-humo"},
        "Errores de integracion": {"anim": "prog2/clase12/dos-instancias"},
        "Integrar por goteo": {"anim": "prog2/clase12/goteo-vs-golpe"},
    },
    13: {
        "Que es una excepcion": {"anim": "prog2/clase13/excepcion-sube"},
        "Checked y unchecked": {"anim": "prog2/clase13/checked-unchecked"},
        "Anatomia de try-catch-finally": {"anim": "prog2/clase13/try-catch-finally"},
        "throw, throws": {"anim": "prog2/clase13/throw-throws"},
        "El catch vacio": {"anim": "prog2/clase13/catch-vacio"},
    },
    14: {
        "La sustentacion es una coreografia": {"anim": "prog2/clase14/guion-bloques"},
        "La demo blindada": {"anim": "prog2/clase14/prevuelo"},
        "Tiempo y nervios": {"anim": "prog2/clase14/ensayo-cronometro"},
    },
}
