# -*- coding: utf-8 -*-
"""Contenido de las clases 2 a 16 de Introduccion a la Ingenieria (FI300101).

Este modulo no tiene contenido propio: junta los tres modulos de corte en un solo
diccionario `TEMAS` para que el builder tenga un unico punto de entrada.

El contenido se parte por corte y no por clase porque cada corte comparte hilo:
  - corte 1 (clases 2-6)  -> intro_ing_corte1_data.py   · cierra con la ficha del problema
  - corte 2 (clases 7-11) -> intro_ing_corte2_data.py   · cierra con el prototipo
  - corte 3 (clases 12-16)-> intro_ing_corte3_data.py   · cierra con el informe final

La clase 1 NO esta aqui: tiene su propio modulo y su propio builder, porque mezcla
diagnostico inicial con el primer tema (ver intro_ing_clase1_data.py).

Si una clase aparece en dos modulos, este archivo falla al importar en vez de dejar que
una sobreescriba a la otra en silencio.
"""

import intro_ing_corte1_data
import intro_ing_corte2_data
import intro_ing_corte3_data

_MODULOS = [
    intro_ing_corte1_data,
    intro_ing_corte2_data,
    intro_ing_corte3_data,
]

TEMAS = {}
for _m in _MODULOS:
    for _n, _t in _m.TEMAS.items():
        if _n in TEMAS:
            raise SystemExit(
                "La clase %d esta definida dos veces: en %s y en un modulo anterior."
                % (_n, _m.__name__)
            )
        TEMAS[_n] = _t

# Coherencia minima: la clave del diccionario y el campo `n` del tema tienen que decir
# lo mismo, porque el builder usa la clave para buscar el tema en el JSON del curso.
for _n, _t in TEMAS.items():
    if _t.get("n") != _n:
        raise SystemExit("La clase %d declara n=%r." % (_n, _t.get("n")))

CLASES = sorted(TEMAS)
