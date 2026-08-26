# -*- coding: utf-8 -*-
"""Soluciones del taller por clase — Arquitectura (PRIVADO docente).

Por que existe
--------------
Las soluciones de Arquitectura eran 15 archivos estaticos que nadie regeneraba y
que solo cubrian parte de las preguntas. Aqui la solucion se declara como datos,
pregunta por pregunta y alineada con la rubrica de `arq_examlab_data`, y el build
la escribe como .md y .docx.

Cada pregunta trae tres cosas distintas y conviene no mezclarlas:

  - `respuesta`      lo que se espera, resuelto sobre un dominio concreto
  - `como_calificar` el desglose de puntos, copiado de la rubrica de ExamLab
  - `errores`        lo que llega mal y que hacer con el

`preguntas_frecuentes` es la seccion que baja la carga del docente: son las dudas
que el estudiante trae cada semestre, con la respuesta ya redactada.

Estructura de la actividad
--------------------------
En ExamLab las Clases 1 a 4 comparten UNA actividad de 11 preguntas (ver
`ACTIVIDAD_CORTE1` en `arq_examlab_data`). Por eso las preguntas se identifican
por su numero GLOBAL, que es el que el estudiante ve en la plataforma, y no por su
posicion dentro de la clase.
"""
from __future__ import annotations

from arq_examlab_data import EXAMLAB

#: Dominio de referencia que se proyecta en clase. La solucion NO lo reutiliza a
#: proposito: si el estudiante entrega este mismo, la rubrica le quita los puntos
#: de «hablar de su dominio», y el docente necesita ver como se ve una respuesta
#: sobre otro dominio para poder calificar la diferencia.
DOMINIO_PROYECTADO = "AgendaU"
DOMINIO_SOLUCION = "BiblioLite"

#: Dudas que el ESTUDIANTE trae al taller, con la respuesta corta. Van dentro de su
#: propio documento: es la unica forma de que no acaben como quince preguntas
#: identicas durante la hora de trabajo. Es un subconjunto deliberado de
#: `preguntas_frecuentes` (la version del docente lleva ademas criterio de nota).
DUDAS_ESTUDIANTE = {
    1: [
        ("¿Esta actividad se entrega hoy?",
         "No. Es UNA sola actividad para las Clases 1 a 4, con 11 preguntas. Hoy resuelves "
         "las preguntas 1, 2 y 3; las demás se resuelven en las clases siguientes y la "
         "entrega completa cierra al final del Corte 1. Puedes guardar y volver."),
        ("¿Qué hace que mi dominio sea «concreto» y no genérico?",
         "Que el problema nombre a quién lo sufre con un rol («el auxiliar de biblioteca») y "
         "cómo se mide con una cifra («38 libros devueltos tarde el semestre pasado»). Si tu "
         "enunciado sirve igual para cualquier otro sistema, todavía es genérico."),
        ("¿Los sistemas externos van en un bloque aparte de la ficha?",
         "No. La ficha son cinco bloques y los sistemas externos van DENTRO de ACTORES. "
         "Escríbelos ahí antes de dibujar: son los mismos que van a aparecer como "
         "`System_Ext` en el diagrama de la pregunta 3."),
        ("¿Tengo que escribir el diagrama a mano en Mermaid?",
         "No. Dibújalo en Excalidraw o draw.io y pide a una IA que lo traduzca a Mermaid; "
         "tú revisas el resultado y lo pegas en ExamLab. Lo que se califica es el diagrama "
         "renderizado en la plataforma, no la imagen."),
        ("¿Por qué mi diagrama no puede llevar la base de datos?",
         "Porque hoy entregas el nivel Context, donde el sistema es una sola caja negra. "
         "La base de datos y la API aparecen en el nivel Container, que es la pregunta 9 de "
         "esta misma actividad. Si las dibujas aquí, esa pregunta se queda sin nada nuevo."),
        ("¿Cuántas cajas debe tener el diagrama?",
         "Entre cuatro y ocho elementos en total. Si tienes veinte, es casi seguro que se "
         "colaron piezas internas del sistema."),
        ("¿Puedo cambiar de dominio más adelante?",
         "No. El dominio se cierra hoy y las preguntas 4 a 11 de esta actividad, más las "
         "Clases 7, 11 y 15, reutilizan estos mismos nombres. Si te queda grande, recorta el "
         "bloque «fuera de alcance»."),
    ],
}

SOLUCION = {
    1: {
        "titulo": ("Solucion — Actividad del Corte 1, preguntas 1 a 3 "
                   "(dominio, ficha y C4 Context)"),
        "resumen": (
            "Las tres preguntas que corresponden a la Clase 1, resueltas sobre el dominio "
            "**BiblioLite** (prestamos de biblioteca). El dominio de la solucion es distinto "
            "del que se proyecta en clase (**AgendaU**) a proposito: sirve de contraste para "
            "calificar y evita que esta solucion se convierta en la respuesta que todos "
            "copian."
        ),
        "total": 25.0,
        "nota_actividad": (
            "Estas 3 preguntas valen **25 de los 100 puntos** de la actividad del Corte 1, "
            "que es **una sola para las Clases 1 a 4** y se entrega completa al cierre del "
            "corte. Las preguntas 4 a 11 se resuelven en las Clases 2, 3 y 4."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "Dominio y problema de CloudLite App",
                "tipo": "abierta",
                "puntos": 6.25,
                "respuesta": """**DOMINIO**
BiblioLite: prestamo y devolucion de libros de la biblioteca de la universidad.

**PROBLEMA** (3 frases: quien lo sufre y como se mide)
El auxiliar de biblioteca lleva los prestamos en una planilla de Excel que solo el puede
abrir, y las renovaciones le llegan por WhatsApp a su numero personal. Los estudiantes que
necesitan un libro de reserva no saben si esta disponible sin ir hasta el mostrador. El
semestre pasado se registraron 38 libros devueltos tarde sin cobro de multa, porque nadie
noto el vencimiento.""",
                "como_calificar": [
                    "3 pts el dominio concreto y del tamano adecuado.",
                    "1.5 pts que el problema nombre a **QUIEN** lo sufre con un rol concreto. "
                    "«Los usuarios» no es un rol; «el auxiliar de biblioteca» si.",
                    "1.75 pts que incluya **una cifra** que mida el dolor. Una cifra estimada "
                    "sirve; «mucho tiempo» o «se pierde informacion» no.",
                    "**Si el dominio es generico** («una red social», «una app de la "
                    "universidad», «un e-commerce»), **toda la pregunta vale cero**: sin "
                    "dominio concreto no hay nada que arquitecturar en las clases siguientes, "
                    "y el estudiante llegaria a la pregunta 9 sin sistema que dibujar.",
                    "Se descuenta si el problema pasa de 3 frases.",
                ],
                "errores": [
                    "Dominio generico. Es el error que hay que cortar HOY, porque arrastra "
                    "las once preguntas. La prueba rapida: si el enunciado sirve igual para "
                    "otro sistema, no es un dominio.",
                    "Problema sin cifra: «se pierde mucho tiempo». Pida un numero, aunque sea "
                    "estimado, y aceptelo: el objetivo es que exista algo medible contra lo "
                    "que comparar, no la exactitud del dato.",
                    "Problema que describe la solucion y no el dolor: «el problema es que no "
                    "tienen una app». El problema es lo que pasa hoy sin el sistema.",
                    "Confundir quien sufre con quien paga. El coordinador aprueba el "
                    "proyecto; el que sufre es quien hace el trabajo manual todos los dias.",
                ],
            },
            {
                "n": 2,
                "titulo": "Ficha del dominio (cinco bloques)",
                "tipo": "abierta",
                "puntos": 8.75,
                "respuesta": """**DOMINIO**
BiblioLite: prestamo y devolucion de libros de la biblioteca de la universidad.

**PROBLEMA**
(el mismo de la pregunta 1, repetido para que la ficha se lea completa)

**ACTORES** (2 a 3, con lo que espera cada uno, y los sistemas externos)
- Estudiante: quiere saber si el libro esta libre sin caminar hasta la biblioteca.
- Auxiliar de biblioteca: quiere registrar un prestamo en menos de 30 segundos.
- Coordinador de la biblioteca: quiere saber que titulos se agotan cada semestre.
- Sistemas externos: proveedor de identidad institucional (valida que quien reserva es
  estudiante activo) y correo transaccional SaaS (envia el aviso de vencimiento).

**CAPACIDADES** (3 a 5, verbo + objeto de negocio)
- Consultar disponibilidad de un titulo
- Reservar un ejemplar
- Renovar un prestamo vigente
- Notificar el vencimiento del prestamo

**FUERA DE ALCANCE**
- No cobra multas ni procesa pagos.
- No digitaliza el contenido de los libros.
- No gestiona compras ni inventario de adquisiciones.""",
                "como_calificar": [
                    "2 pts los **cinco** bloques presentes y rotulados en el orden pedido.",
                    "2.5 pts las capacidades (**3 a 5**) en verbo mas objeto de negocio, sin "
                    "nombrar tecnologia. Se descuenta por cada capacidad que sea una pieza "
                    "tecnica.",
                    "2.25 pts los actores (**2 a 3**) con su expectativa explicita, **mas los "
                    "sistemas externos nombrados dentro de este mismo bloque**.",
                    "2 pts el fuera de alcance con exclusiones que un evaluador razonable si "
                    "habria esperado.",
                    "Los sistemas externos de la ficha deben ser **los mismos** que aparezcan "
                    "en el diagrama de la pregunta 3. Compare los dos antes de poner nota.",
                ],
                "errores": [
                    "«Tener login con JWT» o «usar cache» como capacidad. Son medios, no "
                    "fines. Se corrige en el momento preguntando «¿que puede HACER el usuario "
                    "con eso?»: la capacidad seria «autenticar al estudiante».",
                    "Poner los sistemas externos en un bloque aparte. La ficha son cinco "
                    "bloques y van dentro de ACTORES; no penalice la intencion, pero corrija "
                    "la estructura porque la rubrica cuenta cinco.",
                    "Ocho o diez capacidades. El rango es 3 a 5 y es una decision pedagogica: "
                    "con una sola persona y doce semanas, un alcance de ocho capacidades "
                    "garantiza que el proyecto no llegue a ninguna parte.",
                    "Fuera de alcance con cosas que nadie iba a pedir («no viaja a Marte»). "
                    "Debe excluir lo que un evaluador razonable SI esperaria.",
                    "Actores que no son personas: «la base de datos» no es un actor. Los "
                    "actores son humanos con un rol; lo demas son sistemas externos.",
                ],
            },
            {
                "n": 3,
                "titulo": "C4 Context en Mermaid",
                "tipo": "diagrama",
                "puntos": 10.0,
                "respuesta_mermaid": """C4Context
    title Contexto de CloudLite App - dominio BiblioLite
    Person(estudiante, "Estudiante", "Consulta disponibilidad y reserva ejemplares")
    Person(auxiliar, "Auxiliar de biblioteca", "Registra prestamos y devoluciones")
    System(cloudlite, "CloudLite App", "Aplicacion web y API de prestamos de biblioteca")
    System_Ext(idp, "Proveedor de identidad institucional", "Login OIDC de la universidad")
    System_Ext(correo, "Correo transaccional SaaS", "Envio de avisos de vencimiento")
    Rel(estudiante, cloudlite, "Consulta disponibilidad y reserva un ejemplar", "HTTPS")
    Rel(auxiliar, cloudlite, "Registra el prestamo y la devolucion", "HTTPS")
    Rel(cloudlite, idp, "Valida que el usuario es estudiante activo", "OIDC sobre HTTPS")
    Rel(cloudlite, correo, "Solicita el envio del aviso de vencimiento", "API REST sobre HTTPS")
    Rel(correo, estudiante, "Entrega el aviso 2 dias antes del vencimiento", "SMTP")""",
                "como_calificar": [
                    "3 pts **una sola caja** `System` para CloudLite completo.",
                    "2 pts los actores como `Person`, coherentes con la ficha.",
                    "2 pts los sistemas externos como `System_Ext`, los mismos que la ficha.",
                    "2 pts que **toda** flecha lleve verbo de negocio **y** protocolo. Una "
                    "flecha rotulada «usa», o sin protocolo, no suma.",
                    "1 pt que el diagrama renderice sin error dentro de la plataforma.",
                    "**Si aparece un contenedor interno** (base de datos, API, worker, cache) "
                    "se pierden los 3 pts de la caja del sistema: eso es el nivel Container de "
                    "la pregunta 9, y aprobarlo aqui la deja sin nada que revelar.",
                ],
                "errores": [
                    "Base de datos o API dentro del diagrama. Es el error numero uno. La "
                    "regla que hay que repetir: en Context el sistema es UNA caja negra.",
                    "Flechas sin protocolo. Exija `HTTPS`, `OIDC sobre HTTPS`, `SMTP` o "
                    "`API REST sobre HTTPS`; el protocolo es la mitad del criterio.",
                    "Comas dentro de las etiquetas entre comillas: rompen la sintaxis del C4 "
                    "en Mermaid. Se separa con «y» o con guion.",
                    "Pegar el Mermaid que devolvio la IA sin revisarlo: aparecen cajas "
                    "internas o los nombres no coinciden con la ficha. La IA acierta la "
                    "sintaxis; el modelo sigue siendo del estudiante.",
                    "Entregar solo el PNG del boceto y dejar la pregunta vacia. La pregunta "
                    "es de tipo diagrama: si no renderiza, no se puede calificar.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿La actividad se entrega hoy?",
             "No. Es una sola actividad de 11 preguntas para las Clases 1 a 4. Hoy se "
             "resuelven las tres primeras; la entrega completa cierra al final del Corte 1. "
             "Conviene decirlo al abrir el taller, porque es la duda que mas aparece."),
            ("¿Puede cambiar de dominio en la Clase 2?",
             "No. El dominio se cierra hoy y las preguntas 4 a 11 lo reutilizan. Si el "
             "dominio elegido resulta demasiado grande, se recorta el bloque «fuera de "
             "alcance», no se cambia de dominio."),
            ("¿Cuantos actores y capacidades exactamente?",
             "Son rangos, no numeros fijos: 2 a 3 actores y 3 a 5 capacidades. Lo que se "
             "califica no es la cantidad sino la forma: actor con expectativa, capacidad en "
             "verbo mas objeto de negocio."),
            ("¿Los sistemas externos son un bloque de la ficha?",
             "No. La ficha son cinco bloques y los sistemas externos van dentro de ACTORES. "
             "Si un estudiante los pone aparte, corrija la estructura pero no penalice la "
             "intencion: lo que importa es que esten y que coincidan con el diagrama."),
            ("¿El diagrama hay que escribirlo a mano en Mermaid?",
             "No. Se disena en Excalidraw o draw.io, que es donde se piensa el modelo, y se "
             "pide a una IA que lo traduzca. Lo que se califica es el diagrama renderizado "
             "dentro de ExamLab, no el PNG."),
            ("¿Por que el diagrama no puede tener la base de datos?",
             "Porque es el nivel Context, donde el sistema es una caja negra. La base de "
             "datos aparece en el nivel Container, que es la pregunta 9 de esta misma "
             "actividad. Si se dibuja hoy, esa pregunta no tendria nada nuevo que revelar."),
            ("¿Cuantas cajas debe tener el diagrama?",
             "Entre cuatro y ocho elementos en total. Si hay veinte, es casi seguro que se "
             "colaron piezas internas del sistema."),
            ("¿Hay que abrir una cuenta en AWS o en Azure?",
             "No, y ninguna actividad del curso lo va a pedir. Todo se trabaja con draw.io, "
             "Excalidraw, Killercoda y el nivel gratuito de GitHub Actions. No se pide "
             "tarjeta de credito en ningun momento del semestre."),
        ],
    },
}


def mermaid_referencia(n: int) -> str:
    """Mermaid de referencia de la pregunta de diagrama, leido de ExamLab.

    Se lee de alli y no se copia aqui para que la solucion no pueda divergir del
    modelo contra el que se califica.
    """
    for p in (EXAMLAB.get(n) or {}).get("preguntas", []):
        if p.get("tipo") == "diagrama" and p.get("mermaid_esperado"):
            return p["mermaid_esperado"]
    return ""


def opciones(n: int, n_global: int):
    """(opciones, indices correctos) de una pregunta cerrada, leidas de ExamLab.

    La clave se lee de la misma fuente que ve el estudiante: asi no puede quedar
    una solucion marcando una opcion que en la plataforma ya no es la correcta.
    Se busca por numero GLOBAL porque varias clases comparten una actividad.
    """
    for p in (EXAMLAB.get(n) or {}).get("preguntas", []):
        if p.get("n_global") == n_global and p.get("opciones"):
            return p["opciones"], set(p.get("correctas") or [])
    return [], set()
