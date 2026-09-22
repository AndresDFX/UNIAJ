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

#: Presupuesto por diapositiva. MUY por debajo de la capacidad medida (~1150 car): la
#: lamina tiene que leerse de un vistazo, no contener el parrafo. La capacidad era el
#: limite fisico; esto es el limite de atencion. (~1100 car a 20 pt en 6-7
#: vinetas) para que el autoajuste no tenga que bajar de cuerpo casi nunca: una clase virtual
#: se ve en una ventana compartida y recomprimida, y 20 pt es lo que se lee ahi.
MAX_CAR = 800
MAX_VINETAS = 6

#: Una vineta mas larga que esto se parte por el conector mas cercano al medio: son frases
#: que en prosa se leen bien y proyectadas ocupan cuatro lineas.
MAX_CAR_VINETA = 260

#: Secciones que son preparacion del docente y no se proyectan. Se comparan en minusculas y
#: sin tildes contra el titulo de la seccion.
SOLO_DOCENTE = (
    "errores tipicos del docente",
    "errores típicos del docente",
    "error tipico del docente",
    "error típico del docente",
    "errores de docente",
    "error de docente",
    "errores del docente",
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


def a_vinetas(cuerpo: str):
    """`(proyectable, notas)` — lo que va a la diapositiva y lo que va al guion.

    Las frases que hablan al docente sobre COMO dictar no se proyectan: se devuelven aparte
    para que el guion las use como nota puntual de esa diapositiva. Asi el deck lleva la
    informacion y el guion no agrega nada que no este proyectado.
    """
    proyecta, notas, codigo = [], [], []
    for f in frases(cuerpo):
        # 1. el codigo sale del texto y se junta para la lamina de sintaxis
        resto, frags = _extraer_codigo(f)
        codigo += frags
        f = resto or f if not frags else resto
        if not f or len(f) < 12:
            continue
        # 2. lo que le habla al docente sobre COMO dictar, al guion
        if es_instruccional(f):
            notas.append(limpiar_tokens(f))
            continue
        limpia = limpiar_tokens(f)
        if not limpia:
            continue
        # 3. lo que argumenta tambien se dice, no se proyecta: es el «demasiado texto»
        if es_operativa(limpia):
            proyecta += _partir_larga(limpia)
        else:
            notas.append(limpia)
    return proyecta, notas, codigo


# ───────────────────────────────────────────────── CODIGO DENTRO DE LA PROSA

#: Arranques de sentencia que valen una lamina de codigo. El orden importa: se prueba el mas
#: especifico primero para que «CREATE OR REPLACE FUNCTION» no case como «CREATE».
ARRANQUE_CODIGO = (
    "CREATE OR REPLACE FUNCTION", "CREATE OR REPLACE PROCEDURE", "CREATE OR REPLACE VIEW",
    "CREATE TABLE", "CREATE INDEX", "CREATE UNIQUE INDEX", "CREATE ROLE", "CREATE USER",
    "CREATE TRIGGER", "CREATE VIEW", "CREATE FUNCTION", "CREATE PROCEDURE",
    "ALTER TABLE", "DROP TABLE", "INSERT INTO", "SELECT ", "UPDATE ", "DELETE FROM",
    "GRANT ", "REVOKE ", "EXPLAIN ", "ANALYZE ", "VACUUM ", "SET TRANSACTION",
    "BEGIN;", "COMMIT;", "ROLLBACK;", "SAVEPOINT ", "CALL ", "DO $$",
    "RAISE EXCEPTION", "WITH ", "MERGE INTO",
    "public class", "public static", "private ", "protected ", "class ",
    "List<", "Map<", "ArrayList<", "for (", "while (", "if (", "try {",
    "System.out", "new ",
    "docker ", "kubectl ", "git ", "npm ", "mvn ", "java ", "psql ",
    "apiVersion:", "FROM ", "RUN ", "COPY ", "CMD ",
)

#: Longitud minima para que un fragmento valga una lamina aparte: por debajo es un nombre de
#: columna o una palabra clave citada, no una sentencia.
MIN_CAR_CODIGO = 28


#: Palabras funcionales del castellano. Si una aparece en el fragmento, no es una sentencia:
#: es una frase que MENCIONA la palabra clave («el ALTER TABLE debe convertir cada valor»).
_CASTELLANO = (
    "que", "debe", "puede", "cada", "una", "unos", "unas", "los", "las", "del", "por",
    "con", "sin", "mientras", "porque", "asi", "esa", "ese", "esto", "esta", "hay",
    "son", "pero", "cuando", "donde", "como", "para", "sobre", "entre", "desde",
    "aqui", "alli", "ya", "muy", "mas", "menos", "todo", "toda", "nada", "solo",
    "dentro", "fuera", "antes", "despues", "luego", "tambien", "tampoco", "sigue",
    "queda", "deja", "hace", "dice", "vale", "sirve", "pasa", "falla",
    "el", "la", "y", "un", "se", "su", "al", "lo", "les", "nos", "es",
    "devuelve", "permite", "impide", "obliga", "evita", "arroja", "lanza",
    "guarda", "apunta", "existe", "cambia", "convierte", "bloquea", "cuesta",
)


def _es_codigo_real(frag):
    """True si el fragmento es una sentencia y no una frase que la menciona."""
    # Tiene que tener forma de codigo: parentesis, punto y coma, asignacion o tipo.
    if not re.search(r"[(;=]", frag) and not re.search(
            r"(?i)\b(VARCHAR|NUMBER|DECIMAL|TIMESTAMP|INT|CHAR|BOOLEAN|TO|ON|FROM|SET)\b", frag):
        return False
    # Y no puede llevar palabras funcionales del castellano fuera de una cadena literal.
    sin_cadenas = re.sub(r"'[^']*'", "", frag)
    for pal in re.findall(r"[a-záéíóúñ]+", sin_cadenas.lower()):
        if pal in _CASTELLANO:
            return False
    return True


def _extraer_codigo(frase):
    """`(frase_sin_codigo, [fragmentos])`.

    Un fragmento arranca en una palabra clave y termina donde termina la sentencia: en el
    punto y coma, o al cerrar el parentesis que abrio, o al final de la frase.
    """
    fragmentos = []
    texto = frase
    for _ in range(4):                      # una frase puede traer dos o tres sentencias
        pos, arranque = None, None
        for a in ARRANQUE_CODIGO:
            i = texto.find(a)
            if i != -1 and (pos is None or i < pos):
                pos, arranque = i, a
        if pos is None:
            break
        # fin de la sentencia
        j = pos + len(arranque)
        prof = 0
        abrio = False
        fin = len(texto)
        while j < len(texto):
            ch = texto[j]
            if ch == "(":
                prof += 1
                abrio = True
            elif ch == ")":
                if prof == 0:
                    fin = j
                    break
                prof -= 1
                # Cerrado el grupo de nivel superior, la sentencia termina. Sin esto el
                # barrido seguia hasta el siguiente punto y se llevaba la prosa de detras.
                if prof == 0 and abrio:
                    # INSERT lleva DOS grupos: la lista de columnas y el VALUES. Si lo que
                    # sigue es VALUES, la sentencia continua.
                    resto = texto[j + 1:j + 10].upper().lstrip()
                    if resto.startswith("VALUES"):
                        abrio = False
                        j += 1
                        continue
                    fin = j + 1
                    break
            elif ch == ";" and prof == 0:
                fin = j + 1
                break
            elif ch == "." and prof == 0 and j + 1 < len(texto) and texto[j + 1] == " ":
                fin = j
                break
            j += 1
        frag = texto[pos:fin].strip(" ,;:.")
        if len(frag) >= MIN_CAR_CODIGO and _es_codigo_real(frag):
            fragmentos.append(frag)
            texto = (texto[:pos] + texto[fin:]).replace("  ", " ")
        else:
            # no vale lamina aparte: se deja en la prosa y se sigue buscando mas alla
            texto_restante = texto[fin:]
            if not texto_restante:
                break
            texto = texto[:fin] + texto_restante
            break
    texto = re.sub(r"\s{2,}", " ", texto)
    texto = re.sub(r"\s+([,.;:])", r"\1", texto).strip(" ,;:")
    return texto, fragmentos


def _lineas_de_codigo(frag):
    """Parte una sentencia en lineas legibles en monoespaciado."""
    f = re.sub(r"\s+", " ", frag).strip()
    # un CREATE TABLE con lista de columnas: una columna por linea
    m = re.match(r"(?i)^(CREATE\s+TABLE\s+\S+)\s*\((.+?)\)[.;]*$", f)
    if m:
        cols, prof, act = [], 0, ""
        for ch in m.group(2):
            if ch == "(":
                prof += 1
            elif ch == ")":
                prof -= 1
            if ch == "," and prof == 0:
                cols.append(act.strip())
                act = ""
            else:
                act += ch
        if act.strip():
            cols.append(act.strip())
        return [m.group(1) + " ("] + ["  " + c + ("," if i < len(cols) - 1 else "")
                                      for i, c in enumerate(cols)] + [");"]
    # SQL con clausulas: una clausula por linea
    f2 = re.sub(r"(?i)\s+(FROM|WHERE|GROUP BY|ORDER BY|HAVING|JOIN|LEFT JOIN|INNER JOIN|"
                r"VALUES|SET|RETURNING|LIMIT)\s+", lambda m: "\n" + m.group(1) + " ", f)
    lineas = [x.strip() for x in f2.split("\n") if x.strip()]
    if len(lineas) > 1:
        return lineas
    # si sigue siendo una sola linea larga, cortarla por comas
    if len(f) > 95:
        trozos, act = [], ""
        for parte in f.split(", "):
            if len(act) + len(parte) > 90:
                trozos.append(act.rstrip(", "))
                act = ""
            act += parte + ", "
        if act.strip(", "):
            trozos.append(act.rstrip(", "))
        return trozos
    return [f]


# ───────────────────────────────────────────────── QUE VALE PROYECTAR

#: Senales de que una frase es OPERATIVA: define, manda, mide o nombra. Son las que se
#: proyectan; el resto argumenta y se dice.
OPERATIVA = (
    r"\bes\b", r"\bson\b", r"\bse (usa|declara|escribe|crea|otorga|revoca|llama|define)",
    r"\bno (se|acepta|admite|puede|basta|sirve)\b", r"\bhay que\b", r"\bdebe\b",
    r"\bsiempre\b", r"\bnunca\b", r"\bregla\b", r"\bcriterio\b",
    r"\d", r"[A-Z]{3,}", r"\b(VARCHAR|NUMBER|DECIMAL|TIMESTAMP|INT|CHAR|BOOLEAN)\b",
    r"[a-z_]+\.[a-z_]+", r"\bpor ejemplo\b", r":",
)
_RX_OP = [re.compile(p, re.I) for p in OPERATIVA]

#: Giros de argumentacion: explican POR QUE, y eso se dice en voz, no se proyecta.
ARGUMENTA = (
    r"^(la respuesta|eso |esa |ahi |asi |por eso|de ahi|lo importante|lo que |y eso|"
    r"leidas asi|dicho de otro modo|en otras palabras|conviene|vale la pena)",
    r"\b(no es doctrinal|no es casual|no es decoracion|es exactamente eso|"
    r"es la que|es lo que hace|es la diferencia entre)\b",
    r"^(supongamos|imaginemos|piensen)",
)
_RX_ARG = [re.compile(p, re.I) for p in ARGUMENTA]


def es_operativa(frase):
    """True si la frase vale proyectarse: define, manda, mide o nombra algo concreto."""
    f = frase.strip()
    if len(f) < 25:
        return False
    if any(rx.search(f) for rx in _RX_ARG):
        return False
    return sum(1 for rx in _RX_OP if rx.search(f)) >= 2


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
    """Laminas de esta seccion, tipadas.

    Cada una es `(titulo, items, notas, tipo)` con `tipo` en `content` o `codigo`. El codigo
    de toda la seccion va en UNA lamina al final: una consulta se lee en monoespaciado y en
    varias lineas, y los fragmentos cortos solo valen una lamina cuando se juntan.

    Las notas del guion se cuelgan de la PRIMERA lamina: son sobre el concepto.
    """
    # El titulo tambien se limpia: hay secciones que llevan tokens DENTRO del texto —«...y
    # cierre conceptual (de la {{slide:X}} a la {{slide:Y}})»— y no solo al final, asi que
    # quitar el token final no bastaba y el marcador crudo acababa proyectado.
    titulo = limpiar_tokens(titulo).rstrip(" (").rstrip()
    if titulo.count("(") > titulo.count(")"):
        titulo = titulo[:titulo.rfind("(")].rstrip(" ,;")
    proyecta, notas, codigo = a_vinetas(cuerpo)

    out = []
    if proyecta:
        paginas = _empaquetar(proyecta)
        if len(paginas) == 1:
            out.append((titulo, paginas[0], notas, "content"))
        else:
            out += [(f"{titulo} ({i}/{len(paginas)})", pg, notas if i == 1 else [], "content")
                    for i, pg in enumerate(paginas, 1)]
    if codigo:
        lineas = []
        for frag in codigo:
            if lineas:
                lineas.append("")
            lineas += _lineas_de_codigo(frag)
        if not out:
            out.append((titulo, lineas, notas, "codigo"))
        else:
            # El titulo de una lamina de codigo tiene que caber en UNA linea: si envuelve,
            # empuja el bloque de codigo y lo hace desbordar (paso en 3 laminas de Prog II).
            corto = titulo if len(titulo) <= 46 else titulo[:46].rsplit(" ", 1)[0] + "..."
            out.append((f"{corto} — sintaxis", lineas, [], "codigo"))
    return out


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



def _titulo_de(frase: str, tope: int = 72) -> str:
    """Titulo de diapositiva a partir de la frase que abre el parrafo.

    En Programacion II y Seminario la teoria no viene en secciones `###` sino en vinetas de
    parrafo (~1000 caracteres cada una), y cada parrafo abre con su frase tema: «Un ArrayList
    es exactamente esa carpeta que se agranda sola». Eso es un titulo utilizable; lo que no
    sirve es proyectar el parrafo entero sin encabezado.
    """
    f = frase.strip().rstrip(".;:")
    f = re.sub(r"^(Empecemos por|Vamos a|Veamos|Ahora bien,|Y aqui|Pero)\s+", "", f, flags=re.I)
    if len(f) <= tope:
        return f[:1].upper() + f[1:]
    corte = f[:tope].rsplit(" ", 1)[0]
    return (corte[:1].upper() + corte[1:]).rstrip(",;") + "..."


def slides_de_vinetas(vinetas_teoria, incluir_solo_docente: bool = False):
    """Una diapositiva por vineta de `teoria`, con el parrafo entero repartido en frases.

    Es la variante para los cursos cuyo contenido vive en `teoria` y no en un fundamento con
    secciones. `_resumen`/`_slide_summary` dejaban de cada parrafo su primera frase: 76.000
    caracteres de teoria acababan proyectados como ~500 por clase.
    """
    out = []
    for b in vinetas_teoria or []:
        fr = frases(b)
        if not fr:
            continue
        titulo = _titulo_de(fr[0])
        if not incluir_solo_docente and es_solo_docente(titulo):
            continue
        out += slides_de_seccion(titulo, b)
    return out


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    from bd2_fundamentos import FUNDAMENTOS
    for n in sorted(FUNDAMENTOS):
        sl = slides_de_clase(FUNDAMENTOS[n])
        print(f"Clase {n}: {len(sl)} diapositivas de teoria")
        for t, v, notas, tipo in sl:
            print(f"   {tipo:<8}{sum(len(x) for x in v):>5}car {len(v)}v "
                  f"{len(notas)}nota  {t[:50]}")
        break
