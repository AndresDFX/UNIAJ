# -*- coding: utf-8 -*-
"""Convierte el fundamento teorico en diapositivas: una por concepto, con TODO el contenido.

Por que existe
--------------
El diseno anterior tenia el reparto al reves. `FUNDAMENTOS[n]` traia el tema desarrollado en
secciones `###` —una por concepto, ~1300 caracteres cada una— y el deck del estudiante lo
resumia a UNA diapositiva con `_slide_summary`: la primera frase de cada vineta, cortada a
110 caracteres y limitada a 5. En Bases de Datos II Clase 1 eso significaba cinco conceptos
distintos (vocabulario, conceptual vs fisico, clave primaria, normalizacion, preguntas
frecuentes) apretados en 551 caracteres, mientras el guion desarrollaba los mismos conceptos
en 15.000. El estudiante que faltaba a clase, o que repasaba para el parcial, no tenia de
donde: lo proyectado no alcanzaba y el guion es material del docente.

La medida que lo desbloquea: `metrica_texto` mide anchos reales de Calibri y
`uniajc_slides_engine.bullets()` baja de 20 a 15 pt hasta que el texto entra, asi que una
diapositiva de contenido admite **~1100 caracteres** en 6-7 vinetas sin desbordarse. El
docstring de `bd2_fundamentos.py` decia que la teoria «no se puede engordar sin romper la
slide»; eso era cierto antes del autoajuste y ya no lo es.

Que hace
--------
Toma el texto de una clase y devuelve diapositivas `(titulo, [vinetas], subtitulo)`:

  - **una diapositiva por seccion `###`**, con el contenido de esa seccion, no su primera
    frase. Si la seccion no cabe, se parte en varias con «(cont.)» y se numeran.
  - **una vineta por frase**, que es como esta escrita la prosa: declarativa y corta.
  - las secciones dirigidas al docente y no al grupo (errores tipicos del docente) se
    excluyen con `SOLO_DOCENTE`.

El resultado es que la informacion que se dicta esta proyectada, que es la regla del curso:
cada tema se sostiene con lo que se ve, sin depender del tema anterior ni del guion.
"""
from __future__ import annotations

import re

#: Presupuesto por diapositiva. Por debajo de la capacidad medida (~1100 car a 20 pt en 6-7
#: vinetas) para que el autoajuste no tenga que bajar de cuerpo casi nunca: una clase virtual
#: se ve en una ventana compartida y recomprimida, y 20 pt es lo que se lee ahi.
MAX_CAR = 1150
MAX_VINETAS = 8

#: Una vineta mas larga que esto se parte por el conector mas cercano al medio: son frases
#: que en prosa se leen bien y proyectadas ocupan cuatro lineas.
MAX_CAR_VINETA = 260

#: Secciones que son preparacion del docente y no se proyectan. Se comparan en minusculas y
#: sin tildes contra el titulo de la seccion.
SOLO_DOCENTE = (
    "errores tipicos del docente",
    "errores típicos del docente",
    "errores de docente",
)

_ABREV = ("ej", "p.ej", "etc", "vs", "sr", "sra", "dr", "art", "núm", "num", "fig", "seg")


def _sin_tildes(s: str) -> str:
    for a, b in zip("áéíóúüñ", "aeiouun"):
        s = s.replace(a, b)
    return s


def es_solo_docente(titulo: str) -> bool:
    t = _sin_tildes(titulo.lower())
    return any(_sin_tildes(x) in t for x in SOLO_DOCENTE)


#: Arranques y giros que hablan AL DOCENTE sobre como dictar, no al estudiante sobre el tema.
INSTRUCCIONAL = (
    r"^conviene\b", r"^hay que (decir|subrayar|detener|insistir|advertir|aclarar|exigir|fijar)",
    r"^conviene (decir|detener|subray|insist|aclarar|fijar|entregar|tener|que)",
    r"^es util (decir|mencionar|aclarar)",
    r"^vale la pena (decir|mencionar|detener)",
    r"^se dicta mejor", r"^la clase se dicta", r"^hay que dictar",
    r"^lo importante,? y hay que", r"^\w+ preguntas? aparecen?", r"^tres preguntas",
    r"^si el estudiante sale hoy", r"^el criterio que conviene entregar",
    r"^la respuesta del docente", r"^cuando en un taller",
    r"\bel docente (debe|deberia|tiene que|puede)\b",
    r"\bse le puede dar hoy al estudiante\b",
    r"\bhay que exigirlas desde hoy\b",
    r"\bconviene que el estudiante\b",
    r"^antes de cualquier otra cosa hay que",
    r"^antes de dibujar una sola tabla hay que decir",
    r"^y conviene decirlo", r"^conviene decirlo",
    r"^eso no significa que", r"^y hay que subrayarlo",
    r"^conviene ser preciso", r"^sobre lo que se puede demostrar conviene",
    r"^ultimo tramo", r"^de ahi sale la regla operativa",
    r"^la demo de la .* debe terminar",
)
_RX = [re.compile(p, re.I) for p in INSTRUCCIONAL]


def es_instruccional(frase: str) -> bool:
    f = frase.strip()
    return any(rx.search(f) for rx in _RX)


def limpiar_tokens(s: str) -> str:
    """Quita los `{{slide:...}}` y arregla la puntuacion que dejan.

    En la diapositiva no puede quedar un marcador crudo (regla del repo), y ademas la
    referencia cruzada no tiene sentido proyectada: la diapositiva ES el sitio.
    """
    # Se come tambien el sintagma que la introduce («de la», «en la», «que abre la»): sin eso
    # quedaba «el diagrama ER de es la vista conceptual».
    s = re.sub(r"\s*(?:(?:de|del|en|la|el|los|las|a)\s+){0,3}\{\{slide:.+?\}\}", "", s)
    s = re.sub(r"\s{2,}", " ", s)
    s = re.sub(r"\s+([,.;:])", r"\1", s)
    return s.strip(" ,;:")


def partir_secciones(texto: str) -> list[tuple[str, str, str]]:
    """`(titulo, ancla, cuerpo)` por cada `### Titulo - {{slide:Ancla}}`.

    La ancla es informativa: con una diapositiva por seccion deja de hacer falta que el
    guion apunte a otra, pero se conserva porque hay secciones que sí se apoyan en una
    diapositiva de diagrama o de codigo que no genera este modulo.
    """
    out = []
    partes = re.split(r"^###[ \t]+(.+?)[ \t]*$", texto, flags=re.M)
    # partes[0] es lo que hay antes del primer ###; luego pares (titulo, cuerpo)
    for i in range(1, len(partes) - 1, 2):
        cabecera, cuerpo = partes[i], partes[i + 1]
        m = re.search(r"\{\{slide:(.+?)\}\}", cabecera)
        ancla = m.group(1).strip() if m else ""
        titulo = re.sub(r"\s*-\s*\{\{slide:.+?\}\}\s*$", "", cabecera).strip()
        out.append((titulo, ancla, cuerpo.strip()))
    return out


def _proteger_abreviaturas(s: str) -> str:
    for a in _ABREV:
        s = re.sub(r"(?i)\b(%s)\.\s" % re.escape(a), r"\1<PUNTO> ", s)
    # decimales y numeracion: 12.5 / 1.2
    s = re.sub(r"(\d)\.(\d)", r"\1<PUNTO>\2", s)
    return s


def frases(cuerpo: str) -> list[str]:
    """Parte un parrafo en frases, respetando abreviaturas y decimales."""
    s = re.sub(r"\s+", " ", cuerpo).strip()
    s = _proteger_abreviaturas(s)
    trozos = re.split(r"(?<=[.;?!])\s+(?=[A-ZÁÉÍÓÚÑ¿«(])", s)
    return [t.replace("<PUNTO>", ".").strip() for t in trozos if t.strip()]


def _partir_larga(f: str) -> list[str]:
    """Parte una frase demasiado larga por el conector mas cercano al medio."""
    if len(f) <= MAX_CAR_VINETA:
        return [f]
    # puntos de corte naturales, de mayor a menor preferencia
    for patron in (r", y ", r", pero ", r", porque ", r", que ", r"; ", r", "):
        cortes = [m.start() for m in re.finditer(patron, f)]
        if not cortes:
            continue
        medio = len(f) // 2
        c = min(cortes, key=lambda x: abs(x - medio))
        if not (len(f) * 0.25 < c < len(f) * 0.75):
            continue
        izq = f[:c].strip(" ,;")
        der = f[c:].lstrip(" ,;")
        der = der[0].upper() + der[1:] if der else der
        return _partir_larga(izq) + _partir_larga(der)
    return [f]


def a_vinetas(cuerpo: str) -> tuple[list[str], list[str]]:
    """`(proyectable, notas)` — lo que va a la diapositiva y lo que va al guion.

    Las frases que hablan al docente sobre COMO dictar no se proyectan: se devuelven aparte
    para que el guion las use como nota puntual de esa diapositiva. Asi el deck lleva la
    informacion y el guion no agrega nada que no este proyectado.
    """
    proyecta, notas = [], []
    for f in frases(cuerpo):
        if es_instruccional(f):
            notas.append(limpiar_tokens(f))
            continue
        limpia = limpiar_tokens(f)
        if limpia:
            proyecta += _partir_larga(limpia)
    return proyecta, notas


def _empaquetar(vinetas: list[str]) -> list[list[str]]:
    """Reparte las vinetas en diapositivas EQUILIBRADAS.

    El reparto voraz —llenar hasta el tope y volcar el resto— dejaba diapositivas huerfanas
    de una o dos vinetas: una seccion de 1019 caracteres salia como 864 + 147, que es
    exactamente el defecto que este modulo viene a corregir, con otra cara. Aqui se calcula
    primero CUANTAS diapositivas hacen falta y despues se reparte parejo entre ellas.
    """
    total = sum(len(v) for v in vinetas)
    n = max(1, -(-total // MAX_CAR), -(-len(vinetas) // MAX_VINETAS))
    if n == 1:
        return [vinetas]
    objetivo = total / n
    paginas, actual, car = [], [], 0
    for i, v in enumerate(vinetas):
        quedan = len(vinetas) - i
        faltan = n - len(paginas)
        # Cerrar la pagina si ya paso su cuota y aun quedan vinetas para las que faltan,
        # cuidando que ninguna pagina se quede vacia.
        if actual and faltan > 1 and quedan >= faltan and (
                car >= objetivo or len(actual) >= MAX_VINETAS):
            paginas.append(actual)
            actual, car = [], 0
        actual.append(v)
        car += len(v)
    if actual:
        paginas.append(actual)
    return paginas


def slides_de_seccion(titulo: str, cuerpo: str):
    """`(titulo, vinetas, notas)` por cada diapositiva que necesita esta seccion.

    Las notas del guion se cuelgan de la PRIMERA diapositiva de la seccion: son sobre el
    concepto, no sobre una lamina concreta.
    """
    proyecta, notas = a_vinetas(cuerpo)
    if not proyecta:
        return []
    paginas = _empaquetar(proyecta)
    if len(paginas) == 1:
        return [(titulo, paginas[0], notas)]
    return [(f"{titulo} ({i}/{len(paginas)})", pg, notas if i == 1 else [])
            for i, pg in enumerate(paginas, 1)]


def slides_de_clase(texto: str, incluir_solo_docente: bool = False):
    """Todas las diapositivas de teoria de una clase, en el orden del fundamento."""
    out = []
    for titulo, _ancla, cuerpo in partir_secciones(texto):
        if not incluir_solo_docente and es_solo_docente(titulo):
            continue
        out += slides_de_seccion(titulo, cuerpo)
    return out


def titulos_de_clase(texto: str, incluir_solo_docente: bool = False) -> list[str]:
    """Solo los titulos, para que `_slide_map` no repita la logica."""
    return [s[0] for s in slides_de_clase(texto, incluir_solo_docente)]


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    from bd2_fundamentos import FUNDAMENTOS
    for n in sorted(FUNDAMENTOS):
        sl = slides_de_clase(FUNDAMENTOS[n])
        print(f"Clase {n}: {len(sl)} diapositivas de teoria")
        for t, v, notas in sl:
            print(f"   {sum(len(x) for x in v):>5}car {len(v)}v {len(notas)}nota  {t[:56]}")
        break
