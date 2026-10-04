# -*- coding: utf-8 -*-
"""Que visual acompana a cada lamina de Introduccion a la Ingenieria: animacion, foto o nada.

Clave: el comienzo del titulo de la lamina autorada (de `teoria` o de `intro_ing_ejemplos_data`),
comparado sin tildes ni mayusculas. Valor: ``anim`` (carpeta/huella en `config/animaciones/`,
pasos al clic del docente) y/o ``foto`` (consulta Pexels en ingles).

Este curso no pasa por `teoria_a_slides`: sus laminas son autoradas por tipo. Solo las de tipo
`content`, `steps` o `cards` admiten visual; con visual se pintan con `concepto_slide` (sus
ideas a la izquierda, el visual a la derecha), asi que la lamina NO se duplica: el mismo
contenido gana su dibujo. Las de tabla, antes/despues y recuadro se quedan como estan.
Primer semestre: animaciones simples, de rotulos grandes, una idea por paso.
"""

VISUALES = {
    2: {
        "Cómo se lee un hito": {"anim": "intro/clase2/hito-cuatro-preguntas"},
        "Ejemplo: la ley de Brooks": {"anim": "intro/clase2/ley-brooks"},
    },
    3: {
        "Los cinco elementos de un sistema": {"anim": "intro/clase3/cinco-elementos"},
        "Ejemplo: la app que funcionó y la fila": {"foto": "people waiting in line queue"},
        "Ejemplo resuelto: el semáforo de una esquina": {"anim": "intro/clase3/semaforo"},
    },
    4: {
        "Cinco preguntas para decidir": {"anim": "intro/clase4/cinco-preguntas"},
        "Ejemplo: qué falló en el Therac-25": {"anim": "intro/clase4/therac25"},
        "Ejemplo: el correo que deja rastro": {"foto": "person writing email laptop office"},
    },
    5: {
        "Las cuatro etapas de la huella": {"anim": "intro/clase5/etapas-huella"},
        "Ejemplo: el PUE de un centro de datos": {"foto": "data center server room"},
        "Ejemplo resuelto: el reporte diario de una tienda": {"anim": "intro/clase5/reporte-tienda"},
    },
    6: {
        "El árbol del problema": {"anim": "intro/clase6/arbol-problema"},
        "Ejemplo: de la queja al problema": {"anim": "intro/clase6/queja-problema"},
        "Ejemplo: cómo se saca una línea base": {"foto": "smartphone stopwatch timer hand"},
    },
    7: {
        "Las seis fases del ciclo de vida": {"anim": "intro/clase7/seis-fases", "sub_en_anim": True},
        "Ejemplo: las seis fases en la app de turnos": {"foto": "small neighborhood grocery store"},
    },
    8: {
        "Cómo se decide entre dos alternativas": {"anim": "intro/clase8/matriz-decision", "sub_en_anim": True},
    },
    9: {
        "Cuatro maneras de generar una mejora": {"anim": "intro/clase9/cuatro-maneras"},
        "Ejemplo: la búsqueda del antecedente": {"anim": "intro/clase9/busqueda-antecedente"},
    },
    10: {
        "Ejemplo: la pantalla «ver mi turno»": {"anim": "intro/clase10/pantalla-turno"},
    },
    13: {
        "Ejemplo: afectados de la app de turnos": {"anim": "intro/clase13/afectados"},
    },
    14: {
        "Ejemplo: los cinco tramos": {"anim": "intro/clase14/cinco-tramos"},
    },
}
