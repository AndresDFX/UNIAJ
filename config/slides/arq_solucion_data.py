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
En ExamLab las Clases 1 a 4 comparten UNA actividad de 15 preguntas (ver
`ACTIVIDAD_CORTE1` en `arq_examlab_data`). Por eso las preguntas se identifican
por su numero GLOBAL, que es el que el estudiante ve en la plataforma, y no por su
posicion dentro de la clase.
"""
from __future__ import annotations

from arq_examlab_data import EXAMLAB

#: Dominio del `mermaid_esperado` del banco: el modelo de referencia que queda en la
#: ficha de configuracion del kit docente. NO se proyecta y NO se pega en el
#: enunciado —se llamaba DOMINIO_PROYECTADO y eso hacia que la solucion afirmara que
#: el estudiante lo ve—. La solucion no lo reutiliza a proposito: si el estudiante
#: entrega este mismo, la rubrica le quita los puntos de «hablar de su dominio», y el
#: docente necesita ver como se ve una respuesta sobre otro dominio para poder
#: calificar la diferencia.
DOMINIO_REFERENCIA = "AgendaU"
DOMINIO_SOLUCION = "BiblioLite"

#: Dudas que el ESTUDIANTE trae al taller, con la respuesta corta. Van dentro de su
#: propio documento: es la unica forma de que no acaben como quince preguntas
#: identicas durante la hora de trabajo. Es un subconjunto deliberado de
#: `preguntas_frecuentes` (la version del docente lleva ademas criterio de nota).
DUDAS_ESTUDIANTE = {
    1: [
        ("¿Esta actividad se entrega hoy?",
         "No. Es UNA sola actividad para las Clases 1 a 4, con 15 preguntas. Hoy resuelves "
         "las preguntas 1 a 4; las demás se resuelven en las clases siguientes y la "
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
         "La base de datos y la API aparecen en el nivel Container, que es la pregunta 13 de "
         "esta misma actividad. Si las dibujas aquí, esa pregunta se queda sin nada nuevo."),
        ("¿Cuántas cajas debe tener el diagrama?",
         "Entre cuatro y ocho elementos en total. Si tienes veinte, es casi seguro que se "
         "colaron piezas internas del sistema."),
        ("En atributos de calidad, ¿puedo decir que los cuatro son importantes?",
         "No. La pregunta evalúa exactamente lo contrario: que elijas dos, los midas con un "
         "número y digas cuál sacrificas. Más disponibilidad exige redundancia y la "
         "redundancia cuesta; arquitectura es elegir qué se sacrifica."),
        ("¿Puedo cambiar de dominio más adelante?",
         "No. El dominio se cierra hoy y las preguntas 5 a 15 de esta actividad, más las "
         "Clases 7, 11 y 15, reutilizan estos mismos nombres. Si te queda grande, recorta el "
         "bloque «fuera de alcance»."),
    ],
}

SOLUCION = {
    1: {
        "titulo": ("Solucion — Actividad del Corte 1, preguntas 1 a 4 "
                   "(dominio, ficha, C4 Context y calidad)"),
        "resumen": (
            "Las cuatro preguntas que corresponden a la Clase 1, resueltas sobre el dominio "
            "**BiblioLite** (prestamos de biblioteca). El dominio de la solucion es distinto "
            "del que se proyecta en clase (**AgendaU**) a proposito: sirve de contraste para "
            "calificar y evita que esta solucion se convierta en la respuesta que todos "
            "copian."
        ),
        "total": 25.0,
        "nota_actividad": (
            "Estas 4 preguntas valen **25 de los 100 puntos** de la actividad del Corte 1, "
            "que es **una sola para las Clases 1 a 4** y se entrega completa al cierre del "
            "corte. Las preguntas 5 a 15 se resuelven en las Clases 2, 3 y 4."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "Dominio y problema de CloudLite App",
                "tipo": "abierta",
                "puntos": 5.0,
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
                    "y el estudiante llegaria a la pregunta 13 sin sistema que dibujar.",
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
                "puntos": 7.0,
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
                "puntos": 8.0,
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
                    "la pregunta 13, y aprobarlo aqui la deja sin nada que revelar.",
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
            {
                "n": 4,
                "titulo": "Atributos de calidad de su CloudLite",
                "tipo": "abierta",
                "puntos": 5.0,
                "respuesta": """**Atributo 1 — Disponibilidad**
Por que pesa en BiblioLite: la semana de matricula todos buscan los libros de reserva a la
vez, y si el sistema no responde el estudiante vuelve al mostrador, que es justo el
problema que veniamos a resolver.
Como lo mediria: el sistema responde el 99,5 % del mes, es decir que acepto hasta unas 3
horas y media de caida, siempre que no caigan en la semana de matricula.

**Atributo 2 — Rendimiento**
Por que pesa en BiblioLite: la consulta de disponibilidad es la accion que mas se repite y
compite contra la alternativa de caminar hasta la biblioteca; si tarda, nadie la usa.
Como lo mediria: el listado de disponibilidad de un titulo responde en menos de 400 ms
para el 95 % de las consultas.

**Conflicto**
Sacrifico disponibilidad antes que rendimiento. Prefiero un sistema que a veces este caido
pero que cuando responda sea inmediato, porque el estudiante que encuentra el sistema
caido camina hasta la biblioteca igual que hoy, mientras que uno que espera diez segundos
deja de confiar en el dato y tampoco vuelve. A cambio acepto no montar redundancia, que es
lo que me permite sostener el proyecto sin presupuesto.""",
                "como_calificar": [
                    "1 pt la eleccion de dos atributos **con una razon atada al dominio**. "
                    "«La disponibilidad es importante» no es una razon; «la semana de "
                    "matricula todos consultan a la vez» si.",
                    "2 pts las dos metricas, con **numero y unidad**. Una metrica sin numero "
                    "(«que sea rapido», «que sea seguro») no suma. El numero puede ser "
                    "discutible; lo que no puede es faltar.",
                    "2 pts la frase de conflicto: **cual sacrifica y que gana**. "
                    "**Cero en este criterio** si la respuesta dice que los cuatro son igual "
                    "de importantes o no elige: es justamente lo que la pregunta evalua.",
                ],
                "errores": [
                    "Elegir los cuatro «porque todos importan». Es la respuesta que la "
                    "pregunta busca descartar: si no se sacrifica nada, no se decidio nada. "
                    "Devuelvala pidiendo que elija dos.",
                    "Metricas copiadas de la clase sin aterrizar: «menos de 300 ms» sirve "
                    "solo si dice de QUE operacion de su dominio.",
                    "Confundir seguridad con disponibilidad: «que nadie lo tumbe» es "
                    "disponibilidad; seguridad es quien puede ver o cambiar que.",
                    "Usar porcentajes sin traducirlos a tiempo. Si escribe 99,9 %, pidale que "
                    "diga cuantos minutos al mes son: es la unica forma de saber si entendio "
                    "lo que esta prometiendo.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿La actividad se entrega hoy?",
             "No. Es una sola actividad de 15 preguntas para las Clases 1 a 4. Hoy se "
             "resuelven las cuatro primeras; la entrega completa cierra al final del Corte 1. "
             "Conviene decirlo al abrir el taller, porque es la duda que mas aparece."),
            ("¿Puede cambiar de dominio en la Clase 2?",
             "No. El dominio se cierra hoy y las preguntas 5 a 15 lo reutilizan. Si el "
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
             "datos aparece en el nivel Container, que es la pregunta 13 de esta misma "
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
    2: {
        "titulo": ("Solucion — Actividad del Corte 1, preguntas 5 a 7 "
                   "(matriz de modelos de servicio, ADR-001 y consecuencias)"),
        "resumen": (
            "Las tres preguntas que corresponden a la Clase 2, resueltas sobre el mismo "
            "dominio **BiblioLite** con el que se resolvieron las preguntas 1 a 4. La "
            "continuidad es deliberada: el ADR-001 de la pregunta 6 decide sobre las "
            "capacidades que quedaron escritas en la ficha de la pregunta 2, y esta solucion "
            "solo sirve para calificar si se lee como continuacion de aquella."
        ),
        "total": 25.0,
        "nota_actividad": (
            "Estas 3 preguntas valen **25 de los 100 puntos** de la actividad del Corte 1, "
            "que es **una sola para las Clases 1 a 4** y se entrega completa al cierre del "
            "corte. Hoy se resuelven las preguntas **5, 6 y 7**; las 8 a 15 corresponden a "
            "las Clases 3 y 4. El estudiante puede volver sobre las anteriores: la "
            "plataforma guarda y no cierra la actividad hoy."
        ),
        "preguntas": [
            {
                "n": 5,
                "titulo": "Matriz IaaS / PaaS / SaaS para su dominio",
                "tipo": "abierta",
                "puntos": 6.25,
                "tabla": {
                    "headers": ["Criterio", "IaaS", "PaaS", "SaaS"],
                    "rows": [
                        ["**Control**",
                         "Total: puedo instalar la libreria nativa que lee el codigo de "
                         "barras del lomo del libro y compilarla en la maquina.",
                         "Medio: elijo runtime y version de Node, no el sistema operativo. "
                         "Esa libreria tiene que existir como paquete puro o no la uso.",
                         "Ninguno: uso el modulo de prestamos que traiga el proveedor y "
                         "BiblioLite deja de ser un sistema propio."],
                        ["**Costo cualitativo**",
                         "Bajo en factura y alto en horas mias: una instancia pequena "
                         "aguanta los 400 prestamos al mes, pero los parches los pago yo.",
                         "Medio: el nivel gratuito cubre la demo y el semestre completo; "
                         "sube si la semana de matricula obliga a mas de una instancia.",
                         "Alto y por usuario: pagar licencia por cada uno de los auxiliares "
                         "no lo sostiene el presupuesto de una biblioteca universitaria."],
                        ["**Operacion**",
                         "**Yo** opero sistema operativo y runtime: parches, version de "
                         "Node, arranque del servicio. El proveedor responde por hardware "
                         "y red.",
                         "**El proveedor** opera sistema operativo y runtime; **yo sigo "
                         "respondiendo** por el codigo de BiblioLite, sus permisos y los "
                         "datos de los prestamos.",
                         "**El proveedor** opera todo el stack; **yo sigo respondiendo** "
                         "por quien tiene cuenta, que rol le doy y que datos cargo."],
                        ["**Time-to-demo**",
                         "Dias: crear la instancia, instalar runtime, configurar servicio y "
                         "proxy antes de ver la primera consulta de disponibilidad.",
                         "Horas: un push del repositorio y el endpoint de disponibilidad "
                         "responde. Es lo unico que cabe en doce semanas.",
                         "Minutos, pero no demuestra nada mio: la demo seria del producto "
                         "del proveedor y no de BiblioLite."],
                    ],
                },
                "respuesta": """La fila que decide la nota es **Operacion**, y conviene leerla antes que las otras tres.
En los tres modelos la responsabilidad no desaparece: se reparte. Lo que cambia de columna a
columna es **cuanto** se reparte, y lo que NO cambia nunca es que el equipo responde por su
propia aplicacion, por sus permisos y por sus datos. Una matriz que en la columna de PaaS o
de SaaS escriba «el proveedor se encarga de todo» esta mal aunque las otras once celdas esten
bien, porque es exactamente la creencia que la clase existe para corregir.

Las otras tres filas se califican por una sola cosa: que hablen de BiblioLite. «Mas control»
es una celda vacia; «puedo instalar la libreria que lee el codigo de barras» es una celda
llena, porque nombra una capacidad de la ficha y dice que se puede o no se puede hacer con
ella. El mismo criterio para el costo: no se pide ningun precio, se pide que diga bajo, medio
o alto **y por que en este dominio**.

Un detalle que suele confundir al calificar: es correcto que la matriz mencione **SaaS
satelite** para identidad y correo, porque esos dos sistemas externos ya estaban en el C4
Context de la pregunta 3 y se consumen como servicio. Eso no contradice nada: la matriz
compara donde vive **la aplicacion propia**, no de donde sale cada dependencia.""",
                "como_calificar": [
                    "2 pts la matriz con los **cuatro criterios en el orden pedido** "
                    "(control, costo, operacion, time-to-demo) y las **cuatro columnas** "
                    "con los encabezados exactos.",
                    "3 pts que las **doce celdas** de comparacion hablen del dominio propio "
                    "y de sus capacidades. Se descuenta **por cada fila** escrita en "
                    "abstracto: una fila entera de teoria general vale 0 de esos 3 pts.",
                    "1.25 pts que la fila de **Operacion** reparta bien la responsabilidad "
                    "en los tres modelos. **Cero en este criterio** si en PaaS o en SaaS "
                    "dice que el equipo deja de responder por su aplicacion, sus permisos o "
                    "sus datos.",
                    "No se descuenta por celdas de dos lineas; si se descuenta por celdas "
                    "de un parrafo. El limite es parte del ejercicio: obliga a decidir que "
                    "es lo esencial de cada casilla.",
                    "No se exige ningun precio y no se premia haberlo puesto. Un numero de "
                    "factura inventado no suma; si contradice la columna (por ejemplo SaaS "
                    "mas barato que IaaS sin explicar por que) se descuenta de los 3 pts.",
                ],
                "errores": [
                    "«En PaaS el proveedor se encarga de todo». Es el error central del dia. "
                    "Se corrige en el momento con una pregunta: si manana un estudiante ve "
                    "los prestamos de otro por un permiso mal puesto, ¿a quien reclama la "
                    "biblioteca? El proveedor no escribio ese permiso.",
                    "Matriz correcta pero generica, copiada de cualquier comparativa de "
                    "internet. Se detecta rapido: si se le quita el encabezado, no hay forma "
                    "de saber de que sistema habla. Devuelvala pidiendo que cada celda "
                    "nombre una capacidad de su propia ficha.",
                    "Confundir el criterio de costo con una cotizacion. La pregunta pide "
                    "costo **cualitativo**; el estudiante que se va a buscar precios pierde "
                    "la hora del taller y llega con tres celdas.",
                    "Invertir control y operacion: escribir que en IaaS el proveedor opera "
                    "el sistema operativo. Es el mismo malentendido de la fila de operacion "
                    "visto del otro lado, y arrastra la decision de la pregunta 6.",
                    "Cambiar de dominio a mitad de matriz (control de BiblioLite, costo de "
                    "un e-commerce). Suele pasar cuando se copia de dos fuentes distintas; "
                    "verifique que las doce celdas hablen del mismo sistema.",
                ],
            },
            {
                "n": 6,
                "titulo": "ADR-001: modelo de servicio dominante de CloudLite",
                "tipo": "abierta",
                "puntos": 12.5,
                "respuesta": """**1. Titulo**
ADR-001 Modelo de servicio dominante de CloudLite App

**2. Estado**
Aceptado — 31 de agosto de 2026

**3. Contexto**
BiblioLite gestiona los prestamos de la biblioteca universitaria: unos 400 prestamos al mes,
con un pico en la semana de matricula, y 38 devoluciones tardias el semestre pasado. El
proyecto lo sostiene **una sola persona durante doce semanas**, **sin presupuesto de nube y
sin tarjeta de credito**, y tiene que estar en linea el dia de la sustentacion de la Clase 15.
La unica capacidad que pide algo del sistema operativo es la lectura del codigo de barras del
lomo del libro, que necesitaria una libreria nativa.

**4. Decision** (una sola frase, un unico modelo dominante)
La aplicacion de BiblioLite se desplegara sobre **PaaS**: se entrega el codigo de la API de
prestamos y del front al proveedor, que opera el sistema operativo y el runtime, mientras el
equipo conserva la responsabilidad del codigo, de los permisos y de los datos de prestamo.

**5. Alternativas descartadas** (exactamente 2, con el motivo en terminos del dominio)

- **IaaS.** Se descarta porque el proyecto lo sostiene una sola persona durante doce
  semanas, y en IaaS esa persona tendria que operar el sistema operativo: parchear la
  instancia, sostener la version de Node y levantar el servicio despues de cada reinicio.
  Cada hora gastada en eso es una hora que no se gasta en la regla de negocio que de verdad
  cuesta, que es la de renovaciones vencidas. La libreria nativa de codigo de barras, que es
  el unico argumento real a favor de IaaS en este dominio, se reemplaza por lectura manual
  del ISBN en el mostrador: es una perdida aceptable frente al costo de operar la maquina.

- **SaaS.** Se descarta porque un sistema de prestamos comprado ya resuelve el problema, y
  entonces no queda nada que arquitecturar ni nada que sustentar en la Clase 15: el
  entregable del semestre seria una configuracion. Ademas el modelo de licenciamiento por
  usuario no encaja con una biblioteca donde el auxiliar de mostrador rota cada semestre, y
  las 38 devoluciones tardias del semestre pasado se resolverian con la regla que traiga el
  producto, no con la que la biblioteca necesita.

**Nota de alcance** (no es una seccion aparte; se escribe dentro de las alternativas)
Identidad y correo se siguen consumiendo como **SaaS satelite**, tal como quedaron en el C4
Context de la pregunta 3. Eso no rompe la decision: el modelo dominante se refiere a **la
aplicacion propia**.

La **seccion 6, Consecuencias**, es la pregunta 7 y esta resuelta ahi mismo. El ADR completo
del curso son esas seis secciones; ninguna otra.""",
                "como_calificar": [
                    "1.5 pts titulo y estado. El titulo tiene que traer el **numero** del "
                    "ADR y el estado tiene que traer **fecha**; «Aceptado» solo, sin fecha, "
                    "vale la mitad de este criterio.",
                    "2 pts el **contexto**: nombra el dominio, el plazo y al menos una "
                    "restriccion real de quien sostiene el proyecto (una persona, sin "
                    "presupuesto, sin tarjeta). **Cero en este criterio** si es teoria "
                    "general o un resumen del tema de la clase. La prueba rapida: si el "
                    "contexto no permite deducir por que se descarto IaaS, no es contexto.",
                    "3.5 pts la decision en **una frase** con **un** modelo dominante. "
                    "**Cero en este criterio si nombra dos o mas modelos**: «un poco de PaaS "
                    "y un poco de IaaS» no es una decision, es no haber decidido. Es el "
                    "criterio que hay que revisar primero, antes de leer el resto.",
                    "5.5 pts las dos alternativas descartadas con el motivo atado al "
                    "dominio: **2.75 pts cada una**. Se pierde **la mitad de cada una** si "
                    "el motivo es generico («es mas caro», «es mas complejo») sin decir mas "
                    "caro o mas complejo **para que** de su sistema.",
                    "**Exactamente dos** alternativas. Con una sola, el ADR no documenta una "
                    "decision sino un hecho: se califica solo la que este. Con tres o mas, "
                    "se califican las dos primeras y se descuenta 1 pt por no seguir el "
                    "formato, que es parte de lo que se evalua.",
                    "Mencionar SaaS satelite para identidad y correo **no** penaliza y no "
                    "cuenta como segundo modelo dominante. Si penaliza que la seccion 3 diga "
                    "«PaaS para la app y SaaS para identidad» como si fueran dos decisiones "
                    "dominantes: ahi ya se nombraron dos modelos.",
                    "Elegir IaaS o SaaS como dominante **no se penaliza en absoluto**. Lo "
                    "que se califica es que el motivo del descarte de los otros dos este "
                    "atado al dominio. Un ADR que elige IaaS porque necesita la libreria "
                    "nativa de codigo de barras y lo sustenta esta perfecto.",
                ],
                "errores": [
                    "Decision con dos modelos. Es el error mas frecuente y el mas caro: "
                    "cuesta 3.5 de los 12.5 puntos. Suele venir de querer no equivocarse. "
                    "Devuelvala con una sola instruccion: «tache uno».",
                    "Contexto escrito como resumen del tema: «los modelos de servicio son "
                    "IaaS, PaaS y SaaS y hay que elegir uno». Eso no es contexto, es apunte "
                    "de clase, y vale 0 de los 2 pts. La instruccion que lo corrige es una "
                    "pregunta: «¿que tienes tu que no tiene otro equipo, y cuanto tiempo "
                    "tienes?». Lo que responda es el contexto.",
                    "Alternativas descartadas con motivo de folleto: «IaaS es mas complejo». "
                    "Pregunte «mas complejo para hacer que, en BiblioLite» y la respuesta "
                    "que dé el estudiante es exactamente lo que debia haber escrito.",
                    "Una sola alternativa descartada, casi siempre SaaS, porque es la facil. "
                    "La que enseña algo es IaaS, que es la que obliga a mirar el costo de "
                    "operacion propio.",
                    "Estado «Propuesto» o «En estudio». El enunciado pide `Aceptado` con "
                    "fecha porque el ADR tiene que quedar cerrado hoy: las Clases 3, 7 y 15 "
                    "construyen sobre esta decision y no puede seguir abierta.",
                    "Agregar secciones que no se pidieron (participantes, diagramas, "
                    "riesgos, opciones consideradas). No es un error conceptual, pero el "
                    "enunciado dice cinco secciones y sin agregar otras: se descuenta del "
                    "formato. Ojo con «Opciones consideradas»: en este curso las opciones "
                    "son la matriz de la pregunta 5, y lo que va en el ADR son las dos "
                    "**descartadas**.",
                    "ADR que contradice la matriz de la pregunta 5. Si la matriz dijo que "
                    "PaaS no sirve porque hace falta la libreria nativa, y el ADR elige PaaS "
                    "sin resolver eso, hay una incoherencia que la sustentacion de la Clase "
                    "15 va a encontrar. Marquela hoy.",
                ],
            },
            {
                "n": 7,
                "titulo": "Consecuencias del ADR-001",
                "tipo": "abierta",
                "puntos": 6.25,
                "respuesta": """**Operacion**
- `+` Dejo de administrar el sistema operativo y el runtime: no vuelvo a parchear la
  instancia ni a levantar el servicio a mano despues de un reinicio. En terminos concretos,
  las tres o cuatro horas al mes que eso costaba se van a la regla de renovaciones.
- `-` Pierdo el acceso a la maquina: cuando la consulta de disponibilidad se ponga lenta no
  podre entrar por SSH a mirar procesos, solo tendre los registros y las metricas que el
  proveedor exponga. Depurar pasa a depender de lo que el panel me deje ver.

**Costo**
- `+` Se abarata el arranque: el nivel gratuito cubre la demo y el semestre, asi que el
  proyecto no necesita presupuesto para existir.
- `-` Se encarece el pico: la semana de matricula, que es cuando todos consultan los libros
  de reserva a la vez, es justo cuando el plan gratuito se queda corto y hay que escalar. El
  costo llega concentrado en la peor semana, no repartido.

**Aprendizaje**
- `+` Tengo que aprender a desplegar con un push y a leer los registros del proveedor, que
  es la forma en que se trabaja en la mayoria de los equipos que voy a encontrar.
- `-` **Amarre al proveedor**: cada archivo de configuracion, cada variable de entorno y
  cada nombre de servicio que escriba es especifico de esta plataforma. Si el ano entrante
  hay que mover BiblioLite a otra parte, la aplicacion se mueve pero la configuracion se
  reescribe completa, y no tengo forma de saber cuanto cuesta eso hasta que toque hacerlo.
  Ademas no voy a poder instalar la libreria nativa de codigo de barras: tendre que buscar
  una alternativa que el proveedor soporte o dejar la lectura manual del ISBN.""",
                "como_calificar": [
                    "3 pts los **tres ejes** presentes y rotulados: operacion, costo y "
                    "aprendizaje. 1 pt cada uno.",
                    "2 pts que **cada eje** traiga al menos una consecuencia positiva y una "
                    "negativa, **marcadas con `+` y `-`**. Un eje con solo positivas vale la "
                    "mitad: la mitad que falta es justo la que la Clase 15 va a preguntar.",
                    "1.25 pts que **al menos una negativa** hable de **amarre al proveedor o "
                    "de perdida de control**. Es la contrapartida que casi nunca se escribe "
                    "y por eso se califica aparte.",
                    "Se descuenta por cada consecuencia escrita como ventaja de folleto («es "
                    "mas facil», «es mas moderno», «es mas escalable») en vez de como algo "
                    "que cambia en el trabajo del estudiante. La prueba: si la frase no dice "
                    "que hace o deja de hacer el estudiante, no es una consecuencia.",
                    "Las consecuencias tienen que corresponder a **la decision de la "
                    "pregunta 6**, no al modelo que le hubiera gustado. Si eligio IaaS y "
                    "escribe «dejo de operar el sistema operativo», el criterio de operacion "
                    "vale cero: esta describiendo otra decision.",
                ],
                "errores": [
                    "Los tres ejes con solo consecuencias positivas. Es el error dominante. "
                    "La instruccion que lo corrige: «por cada `+` escriba el `-` que "
                    "vendria en el mismo paquete».",
                    "Confundir consecuencia con ventaja: «es mas facil de usar». Pida que "
                    "reescriba la frase empezando por «a partir de ahora tengo que...» o "
                    "«dejo de...»; lo que salga ya es una consecuencia.",
                    "No hablar nunca de amarre al proveedor. Se pierde 1.25 pts de 6.25, que "
                    "es un quinto de la pregunta. Vale la pena anunciarlo en voz alta al "
                    "abrir el taller.",
                    "Consecuencias del eje aprendizaje escritas como lista de tecnologias "
                    "(«aprender Docker, Kubernetes, Terraform»). El eje pregunta que hay que "
                    "aprender **para sostener esta decision durante el semestre**, que en "
                    "PaaS es bastante menos que eso.",
                    "Repetir en las consecuencias lo que ya dijo la matriz de la pregunta 5. "
                    "La matriz compara; las consecuencias comprometen. Si el texto es "
                    "identico, todavia no hay consecuencias.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿La actividad se entrega hoy?",
             "No. Sigue siendo la misma actividad de 15 preguntas de las Clases 1 a 4, y "
             "cierra al final del Corte 1. Hoy se resuelven la 5, la 6 y la 7. Conviene "
             "repetirlo aunque se haya dicho en la Clase 1: siempre hay alguien que llego "
             "hoy por primera vez."),
            ("¿Puede cambiar el dominio ahora que entendio mejor el tema?",
             "No. El ADR-001 decide sobre las capacidades de la ficha de la pregunta 2, y las "
             "preguntas 8 a 15 siguen construyendo sobre lo mismo. Si el dominio le quedo "
             "grande, se recorta el bloque «fuera de alcance»."),
            ("¿Puede elegir dos modelos si su sistema tiene dos partes?",
             "No en la seccion de decision, y esta es la duda que hay que atajar antes de que "
             "empiecen a escribir. El modelo dominante es el de **su aplicacion**. Que "
             "identidad y correo sean SaaS ya estaba decidido desde la Clase 1 y se menciona "
             "en las alternativas, no en la decision."),
            ("¿Elegir IaaS baja la nota?",
             "No. Se califica el sustento, no la eleccion. Un ADR que elige IaaS porque "
             "necesita una libreria nativa concreta y asume el costo de operarla esta mejor "
             "que uno que elige PaaS «porque es lo moderno»."),
            ("¿Hay que poner precios en la matriz?",
             "No, y buscarlos es la forma mas rapida de perder la hora del taller. El "
             "criterio dice **costo cualitativo**: bajo, medio o alto, con el por que de "
             "este dominio."),
            ("¿Que fecha se le pone al estado del ADR?",
             "La de hoy, la de la sesion en que se decide. El ADR es un documento fechado: "
             "sirve precisamente para que en seis meses se sepa cuando se decidio y con que "
             "informacion."),
            ("¿Cuantas secciones tiene el ADR y donde va cada una?",
             "**Seis**, y son las mismas en todo el curso: Titulo, Estado, Contexto, "
             "Decision, Alternativas descartadas y Consecuencias. Las cinco primeras se "
             "entregan en la pregunta 6 y la sexta en la pregunta 7, pero es **un solo "
             "documento**: el que se cita en la sustentacion de la Clase 15 y el que sirve de "
             "molde para el ADR-002 en adelante. No hay seccion de «Opciones consideradas»: "
             "ese analisis es la matriz de la pregunta 5."),
            ("El contexto y la matriz de la pregunta 5, ¿no son lo mismo?",
             "No, y conviene decirlo antes de que empiecen a escribir. La matriz **compara** "
             "los tres modelos sobre las capacidades del dominio; el contexto son las "
             "**restricciones** bajo las que se decide: quien sostiene el proyecto, cuanto "
             "tiempo hay y con que presupuesto. La matriz es el analisis, el contexto es el "
             "terreno. Si el contexto repite la matriz, no cumple."),
            ("¿Las consecuencias pueden ser las mismas para los tres ejes?",
             "No. Si la misma frase sirve para operacion, costo y aprendizaje, es una frase "
             "generica. Cada eje pregunta algo distinto: que hago, que pago y que tengo que "
             "aprender."),
            ("¿Hay que abrir cuenta en algun proveedor cloud para responder esto?",
             "No. Toda la actividad es de decision y documentacion; no se despliega nada y no "
             "se pide tarjeta de credito en ningun momento del semestre."),
        ],
        "cierre": (
            "El ADR-001 no es un ejercicio suelto: es el documento que la Clase 3 usa para "
            "saber si el contenedor que se va a construir corre en una instancia propia o "
            "sobre un runtime del proveedor, el que la Clase 7 usa para decidir que dibuja "
            "en el diagrama de despliegue, y el que la Clase 15 le va a pedir en voz alta "
            "cuando pregunte «¿por que asi y no de otra forma?». Cierre la clase diciendo "
            "exactamente eso: quien salga hoy sin decision cerrada llega a la Clase 3 sin "
            "saber que esta contenedorizando."
        ),
    },
    3: {
        "titulo": ("Solucion — Actividad del Corte 1, preguntas 8 a 11 "
                   "(contenedor del stub de CloudLite)"),
        "resumen": (
            "Las cuatro preguntas de la Clase 3, resueltas sobre **BiblioLite** y sobre la "
            "decision de PaaS del ADR-001. El servicio contenedorizado es la **API de "
            "prestamos**, con imagen `bibliolite-api:0.1.0` y puerto **3000**. Ese numero y "
            "ese nombre se repiten en las preguntas 8, 10 y 11: la coherencia entre las tres "
            "es criterio de nota, asi que conviene calificarlas juntas y no una por una."
        ),
        "total": 25.0,
        "nota_actividad": (
            "Estas 4 preguntas valen **25 de los 100 puntos** de la actividad del Corte 1. "
            "La pregunta 11 exige haber ejecutado el ciclo **de verdad** en Killercoda: es la "
            "unica de todo el corte que no se puede responder de memoria, y es la que hay que "
            "anunciar al empezar el taller para que nadie deje el laboratorio para el final."
        ),
        "preguntas": [
            {
                "n": 8,
                "titulo": "El servicio a contenedorizar y su Dockerfile",
                "tipo": "abierta",
                "puntos": 10.0,
                "respuesta": """**Primera parte — la eleccion**
Contenedorizo la **API de prestamos**, que es la caja `api-prestamos` del C4 Context. Elijo
esa y no el front porque es la que tiene la regla de negocio del dominio: decide si un
ejemplar esta disponible y si una renovacion es valida. Tener esa API corriendo en un
contenedor demuestra que la logica de BiblioLite se ejecuta de forma reproducible en
cualquier maquina, que es lo que el front por si solo no demostraria: un front estatico
corriendo solo prueba que se sirven archivos.

**Segunda parte — el Dockerfile**

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev
COPY src ./src
EXPOSE 3000
CMD ["node", "src/server.js"]
```

**Puerto** — `EXPOSE 3000`, el servidor de `src/server.js` escucha en `3000`, y `3000` es el
puerto del contenedor que se documenta en la pregunta 10. Un solo numero en los tres sitios.

**Secretos** — no hay `COPY .` de todo el directorio: se copian `package.json`,
`package-lock.json` y la carpeta `src`, y nada mas. Aun asi existe `.dockerignore` como
segunda barrera, con:

```text
node_modules
.env
.env.*
.git
capturas/
*.md
```

Ni `.env` ni ninguna clave entra en la imagen. La cadena de conexion a la base y la clave del
proveedor de correo se inyectan al ejecutar, con `-e` o con las variables de entorno del
proveedor de PaaS, que es coherente con el ADR-001.""",
                "como_calificar": [
                    "2 pts la eleccion del servicio **con justificacion atada al dominio**: "
                    "por que ese y que demuestra tenerlo corriendo. «Porque es el principal» "
                    "no es justificacion; «porque tiene la regla que decide si el ejemplar "
                    "esta disponible» si.",
                    "5 pts el Dockerfile completo con las **siete instrucciones minimas** "
                    "(`FROM`, `WORKDIR`, `COPY` de dependencias, `RUN` de instalacion, "
                    "`COPY` del codigo, `EXPOSE`, `CMD`) **y** en un orden que aproveche el "
                    "cache: las dependencias antes del codigo. Si el orden esta invertido se "
                    "descuenta 1.5 de estos 5 pts, porque es justo lo que la pregunta 9 "
                    "pide explicar.",
                    "1.5 pts imagen base **ligera y con etiqueta fija**. Se descuenta "
                    "completo por `latest`, y la mitad por una imagen completa sin variante "
                    "ligera (`node:20` en vez de `node:20-alpine`) cuando el servicio no "
                    "necesita nada que justifique el peso.",
                    "1.5 pts **coherencia del puerto** entre `EXPOSE`, el proceso del `CMD` "
                    "y lo documentado en la pregunta 10. Se verifica leyendo las dos "
                    "preguntas seguidas.",
                    "**Si el Dockerfile copia un `.env` o una clave**, o hace `COPY . .` sin "
                    "`.dockerignore` ni mencionarlo, **se pierden los 5 pts del Dockerfile**. "
                    "No es una penalizacion desproporcionada: un secreto queda en el "
                    "historial de capas para siempre y se lee con `docker history` aunque una "
                    "capa posterior borre el archivo. Es el error que el curso corta el mismo "
                    "dia en que aparece.",
                    "Un `CMD` en forma de shell (`CMD node src/server.js`) no se penaliza en "
                    "esta clase, aunque la forma de lista sea la correcta. Si la respuesta lo "
                    "usa, valga la nota completa y comente por que la lista es mejor: el "
                    "proceso recibe las señales de parada directamente.",
                ],
                "errores": [
                    "`FROM node:latest`. Rompe la reproducibilidad, que es el argumento "
                    "entero de la clase: la imagen que hoy funciona manana puede traer otra "
                    "version mayor de Node. Se corrige en diez segundos y hay que exigirlo.",
                    "`COPY . .` antes del `RUN npm ci`. Con eso cada cambio de una linea de "
                    "codigo invalida la capa de dependencias y el build vuelve a descargar "
                    "todo. Es el error que la pregunta 9 hace visible, asi que si aparece "
                    "aqui, revise si en la 9 el estudiante explico lo contrario de lo que "
                    "escribio.",
                    "`.env` dentro de la imagen, casi siempre por `COPY . .`. Pida el "
                    "`.dockerignore` en el momento; es la unica correccion del dia que no "
                    "admite «lo arreglo despues».",
                    "`EXPOSE 3000` con el servidor escuchando en `8080`, o al reves. Es el "
                    "error mas comun y el mas facil de evitar: el contenedor arranca, "
                    "`docker ps` lo muestra vivo y la peticion nunca responde.",
                    "Dockerfile de una imagen que no corresponde al servicio elegido: elige "
                    "el front y escribe un `FROM node` con `npm ci`. Suele ser copiar el "
                    "ejemplo de la diapositiva sin adaptarlo.",
                    "`RUN npm install` en vez de `npm ci`. No se penaliza, pero vale "
                    "explicarlo: `ci` respeta el `package-lock.json` y por eso es el que "
                    "produce la misma imagen dos veces.",
                ],
            },
            {
                "n": 9,
                "titulo": "Imagen, contenedor y capas, sobre su propio Dockerfile",
                "tipo": "abierta",
                "puntos": 4.0,
                "respuesta": """**1. Imagen y contenedor**
La imagen es `bibliolite-api:0.1.0`, el molde: un paquete inmutable con Alpine, Node 20, mis
dependencias y mi carpeta `src`. El contenedor es la instancia que corre de ese molde; de esa
misma imagen puedo levantar dos contenedores a la vez, uno en el puerto 8080 y otro en el
8081 del anfitrion, y cada uno tiene su propio sistema de archivos escribible y su propio
proceso.

**2. Que instrucciones de mi Dockerfile crean capa**
`RUN npm ci --omit=dev` crea una capa con los `node_modules` instalados, y `COPY src ./src`
crea otra con mi codigo. Tambien crean capa los dos `COPY` y el `FROM` trae las capas de la
imagen base. Importa porque cada capa se cachea por separado y se identifica por su
contenido: si la capa no cambio, el build la reutiliza y no la vuelve a construir.

**3. Por que el `COPY` de dependencias va antes**
Porque cambio `src/server.js` muchas veces al dia y el `package.json` casi nunca. Con este
orden, al cambiar una linea de codigo el build reutiliza la capa del `npm ci` — que es la
lenta, la que descarga paquetes — e invalida solo la capa del codigo: el rebuild tarda
segundos. En el orden inverso, con `COPY . .` antes del `RUN`, cualquier cambio de una linea
invalida la capa que contiene el `package.json` y todas las siguientes, asi que el `npm ci`
se vuelve a ejecutar completo cada vez.

**4. Una diferencia con una maquina virtual**
Mi contenedor **comparte el kernel** del anfitrion: dentro solo esta Alpine como sistema de
archivos y mi proceso de Node, no hay otro sistema operativo arrancando. Una maquina virtual
carga su propio kernel y su propio sistema operativo completo sobre un hipervisor, y por eso
arranca en decenas de segundos y ocupa gigas, mientras mi contenedor arranca en menos de un
segundo.""",
                "como_calificar": [
                    "1 pt distinguir imagen de contenedor **sin decir que un contenedor es "
                    "una VM ligera** y sin decir que «la imagen se ejecuta». Se espera la "
                    "idea del molde y la instancia, con el detalle de que de una imagen "
                    "salen varios contenedores.",
                    "1 pt nombrar **al menos dos instrucciones de SU propio Dockerfile** que "
                    "crean capa. Nombrar `RUN` y `COPY` en abstracto vale la mitad: la "
                    "pregunta pide las de su archivo.",
                    "1 pt explicar el efecto del orden en el cache **comparando con el orden "
                    "inverso**. Sin la comparacion no hay explicacion, solo la receta.",
                    "1 pt la diferencia con una VM **en terminos de kernel compartido**. "
                    "«Es mas ligero» o «arranca mas rapido» son consecuencias, no la "
                    "diferencia: valen la mitad si no nombran el kernel.",
                    "Una respuesta que explique la teoria correctamente **sin referirse a su "
                    "archivo pierde la mitad del total**. La pregunta no evalua si sabe la "
                    "definicion: evalua si entiende lo que escribio en la pregunta 8.",
                ],
                "errores": [
                    "«Un contenedor es una maquina virtual ligera». Suena bien y es falso. "
                    "El enunciado lo advierte y aun asi aparece: es la frase que hay que "
                    "corregir en voz alta ante todo el grupo.",
                    "«La imagen se ejecuta». Se ejecuta el contenedor. Parece un detalle de "
                    "lenguaje y no lo es: quien lo dice suele no entender por que puede "
                    "levantar dos contenedores del mismo molde.",
                    "Explicar el cache al reves: decir que el orden correcto es el codigo "
                    "primero. Verifique contra el Dockerfile de la pregunta 8; a veces el "
                    "archivo esta bien y la explicacion mal, y a veces al contrario.",
                    "Enumerar teoria de capas sin abrir su archivo. Es la mitad de la nota. "
                    "La correccion es literal: «vuelva a responder citando las lineas que "
                    "usted escribio».",
                    "Confundir capa con contenedor: decir que cada capa es un contenedor. Las "
                    "capas son de la imagen y son de solo lectura; el contenedor agrega "
                    "encima una unica capa escribible.",
                ],
            },
            {
                "n": 10,
                "titulo": "Construir, ejecutar y verificar el contenedor",
                "tipo": "abierta",
                "puntos": 5.0,
                "respuesta": """**1. Construccion**
```bash
docker build -t bibliolite-api:0.1.0 .
```
Nombre `bibliolite-api` y etiqueta `0.1.0`. La etiqueta es una version, no `latest`: asi
puedo tener dos versiones a la vez y saber cual estoy ejecutando.

**2. Ejecucion**
```bash
docker run -d --name bibliolite-api -p 8080:3000 \\
  -e DATABASE_URL="postgres://..." bibliolite-api:0.1.0
```
En `-p 8080:3000`, el numero de la **izquierda es el del anfitrion** (la maquina de
Killercoda, donde entro yo con el navegador o con `curl`) y el de la
**derecha es el del contenedor** (donde escucha Node, el mismo del `EXPOSE`).
Si los invierto y escribo
`-p 3000:8080`, Docker publica el 3000 del anfitrion hacia el 8080 del contenedor, donde no
hay nada escuchando: el contenedor aparece vivo en `docker ps` y la peticion muere con
`Connection reset by peer` o se queda colgada. El sintoma no dice cual es la causa, y por eso
este es el error que mas tiempo hace perder.

La clave de la base y la del correo entran aqui, con `-e`, en tiempo de ejecucion: no estan
en la imagen.

**3. Verificacion — contrato del endpoint de salud**
- **Ruta**: `GET /health`
- **Codigo de estado**: `200` cuando el servicio esta vivo **y** alcanza la base de datos;
  `503` cuando el proceso responde pero la base no contesta.
- **Cuerpo**: JSON, con esta forma exacta:

```json
{
  "estado": "ok",
  "version": "0.1.0",
  "dependencias": { "bd": "ok" }
}
```

Se verifica con:
```bash
curl -i http://localhost:8080/health
```

El cuerpo lleva las dependencias a proposito: un `200` con el cuerpo vacio no distingue «vivo»
de «vivo pero roto», y es justo lo que la Clase 7 va a consultar desde el balanceador y la
Clase 8 desde el pipeline.""",
                "como_calificar": [
                    "1.5 pts el comando de **build con nombre y etiqueta**. Sin etiqueta, o "
                    "con `latest`, vale la mitad.",
                    "1.5 pts el comando de **run con el mapeo de puertos correctamente "
                    "explicado**: que lado es el anfitrion, que lado el contenedor y **que "
                    "pasa si se invierten**. La explicacion de la inversion es la mitad de "
                    "este criterio; sin ella se queda en 0.75.",
                    "2 pts el **contrato de salud completo**: ruta, codigo de estado y cuerpo "
                    "con su formato. Se descuenta si falta **cualquiera** de los tres, y los "
                    "tres pesan igual.",
                    "El **puerto del contenedor tiene que ser el mismo de la pregunta 8**. Si "
                    "no coincide, se descuenta de los 1.5 pts del run, y ademas revise la "
                    "pregunta 11: el error se propaga hasta la bitacora.",
                    "Distinguir `200` de `503` segun el estado de las dependencias **no es "
                    "obligatorio** pero es la respuesta que merece la nota completa del "
                    "criterio de codigo de estado. Un `200` unico, bien documentado, tambien "
                    "la merece si el cuerpo dice algo verificable.",
                ],
                "errores": [
                    "Invertir el mapeo de puertos y no notarlo, porque `docker ps` muestra el "
                    "contenedor arriba. Enseñe el sintoma: contenedor `Up`, peticion sin "
                    "respuesta. Es la leccion mas util del dia.",
                    "Endpoint de salud que devuelve `200` con cuerpo vacio. El enunciado dice "
                    "por que es peor que ninguno: no distingue vivo de roto. Pida al menos "
                    "un campo verificable.",
                    "`docker build` sin `-t`. La imagen queda sin nombre, la pregunta 11 no "
                    "puede filtrarla en `docker images` y se pierde el punto de coherencia "
                    "alla tambien.",
                    "Poner la clave de la base dentro del Dockerfile «para que el run sea mas "
                    "corto». Es el mismo error de la pregunta 8 disfrazado de comodidad, y "
                    "cuesta los 5 pts de aquella.",
                    "Describir el contrato de salud en prosa sin decir el formato del cuerpo. "
                    "Un contrato sin forma no es un contrato: la Clase 8 va a escribir una "
                    "verificacion automatica contra el.",
                    "Confundir `-p` con `-e`, o usar `--port`. No es conceptual pero se "
                    "corrige rapido y evita media hora de frustracion en el laboratorio.",
                ],
            },
            {
                "n": 11,
                "titulo": "Bitacora del laboratorio: la evidencia de que corrio",
                "tipo": "abierta",
                "puntos": 6.0,
                "tabla": {
                    "headers": ["Comando", "Que esperaba", "Que salio realmente"],
                    "rows": [
                        ["`docker build -t bibliolite-api:0.1.0 .`",
                         "Que construya sin error y que se vean las capas de cada paso.",
                         "`=> [4/6] RUN npm ci --omit=dev` ... "
                         "`Successfully tagged bibliolite-api:0.1.0`. **7 pasos**, el mas "
                         "lento el `npm ci` con 21.4s."],
                        # Pipe escapado: la celda va dentro de una tabla Markdown y un |
                        # crudo la partia en dos.
                        [r"`docker images \| grep bibliolite`",
                         "Una fila con mi imagen, etiqueta 0.1.0.",
                         "`bibliolite-api   0.1.0   9f2c1a4be7d3   58 seconds ago   "
                         "142MB`"],
                        ["`docker run -d --name bibliolite-api -p 8080:3000 "
                         "bibliolite-api:0.1.0`",
                         "Que imprima el identificador largo del contenedor.",
                         "`9d41c7e8b2a5f0c3...` (64 caracteres). Sin salida de error."],
                        ["`docker ps`",
                         "Una fila, estado Up, puertos 0.0.0.0:8080->3000/tcp.",
                         "`9d41c7e8b2a5   bibliolite-api:0.1.0   \"node src/server.js\"   "
                         "12 seconds ago   Up 11 seconds   0.0.0.0:8080->3000/tcp   "
                         "bibliolite-api`"],
                        ["`curl -i http://localhost:8080/health`",
                         "200 y el JSON con estado, version y dependencias.",
                         "`HTTP/1.1 200 OK` · `content-type: application/json` · "
                         "`{\"estado\":\"ok\",\"version\":\"0.1.0\","
                         "\"dependencias\":{\"bd\":\"ok\"}}`"],
                    ],
                },
                "respuesta": """**Descripcion de la captura**
La captura es una sola imagen de la ventana del escenario Ubuntu de Killercoda en la que se
ven al mismo tiempo las tres cosas exigidas: el **prompt del laboratorio**
(`controlplane $`), la **salida completa de `docker ps`** con la fila del contenedor
`bibliolite-api` y el mapeo `0.0.0.0:8080->3000/tcp`, y la **hora del sistema** que imprimi
con `date` en la linea inmediatamente anterior (`Mon Sep  7 14:22:10 UTC 2026`). No es un
recorte: se ve la terminal completa, para que se pueda verificar que las tres cosas son de la
misma sesion.

**Fila de incidente**
El primer `docker run` fallo con
`docker: Error response from daemon: driver failed programming external connectivity on endpoint bibliolite-api: Bind for 0.0.0.0:8080 failed: port is already allocated`.
Causa: en
un intento anterior habia dejado un contenedor con el mismo puerto publicado, detenido pero
no eliminado. Lo resolvi con `docker rm -f bibliolite-api` y volvi a ejecutar el `run`.
Verifique antes con `docker ps -a`, que es donde aparecen los detenidos y donde no habia
mirado.""",
                "como_calificar": [
                    "2.5 pts las **cinco filas** con la salida real pegada **textualmente**. "
                    "Una salida parafraseada («salio bien», «funciono correctamente») no suma "
                    "nada en esa fila. Lo que se busca son marcas que no se pueden inventar "
                    "sin haber corrido el ciclo: el numero de pasos del build, el "
                    "identificador corto, el tamano de la imagen, el `Up N seconds`.",
                    "1.5 pts la descripcion de la captura con los **tres elementos** "
                    "exigidos: prompt del laboratorio, salida de `docker ps` y hora del "
                    "sistema. 0.5 pts cada uno.",
                    "1 pt la fila de incidente con el problema **y** como se resolvio. Si "
                    "nada fallo, se acepta el que estuvo a punto de fallar y por que no "
                    "fallo; lo que no se acepta es dejarla vacia.",
                    "1 pt **coherencia**: nombre de imagen, etiqueta y puerto identicos a los "
                    "de las preguntas 8 y 10. Este punto se pone comparando las tres "
                    "respuestas, no leyendo esta sola.",
                    "Si la bitacora esta hecha con LabEx en vez de Killercoda, **no se "
                    "descuenta**: la alterna esta autorizada en el enunciado. Solo verifique "
                    "que la captura corresponda al entorno que dice usar.",
                    "**Senal de bitacora inventada**: las cinco filas con salidas redondas y "
                    "sin ningun incidente, identificadores de contenedor demasiado "
                    "regulares, tamano de imagen ausente. Cuando aparece, pida la captura y "
                    "la hora del sistema antes de poner nota.",
                ],
                "errores": [
                    "Columna derecha parafraseada. Es el error que vacia la pregunta: sin "
                    "salida textual no hay evidencia de que el contenedor existio. Se avisa "
                    "al abrir el taller, no al calificar.",
                    "Perder el trabajo porque la sesion caduco a la hora. El enunciado lo "
                    "advierte: el Dockerfile se escribe en la carpeta del PI y se **pega** en "
                    "el laboratorio, nunca al contrario, y la evidencia se captura antes de "
                    "cerrar. No es excusa aceptable para no entregar.",
                    "Captura recortada que solo muestra la salida de `docker ps`, sin prompt "
                    "ni hora. Se pierde 1 de los 1.5 pts de la captura y no se puede "
                    "verificar que sea de la sesion propia.",
                    "Fila de incidente en blanco «porque todo funciono». Siempre hay algo: el "
                    "puerto ocupado, el `npm ci` sin `package-lock.json`, el `curl` a "
                    "`localhost` desde la pestaña equivocada. Pida el que estuvo cerca.",
                    "Puerto distinto del de las preguntas 8 y 10, casi siempre porque en el "
                    "laboratorio lo cambio para que funcionara y no volvio a corregir el "
                    "Dockerfile. Cuesta el punto de coherencia y, si el Dockerfile quedo mal, "
                    "tambien en la pregunta 8.",
                    "Pegar la salida como imagen dentro de la respuesta abierta. La columna "
                    "pide texto: una imagen no se puede leer ni comparar con las otras "
                    "preguntas.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Hay que instalar Docker en el computador?",
             "No, y no conviene. El laboratorio es Killercoda en el navegador, con cuenta "
             "gratuita y escenario Ubuntu; si no carga, la alterna es LabEx Docker "
             "Playground, que da solo 3 sesiones al dia en el plan gratuito. Nadie necesita "
             "permisos de administrador en su maquina para esta actividad."),
            ("¿Que hago si la sesion del laboratorio se cierra a la hora?",
             "Volver a abrir el escenario y pegar de nuevo el Dockerfile, que debe estar "
             "guardado en la carpeta del PI. El laboratorio es desechable a proposito: la "
             "fuente de verdad es el repositorio, no la sesion."),
            ("¿Puedo contenedorizar el front en vez de la API?",
             "Si, esta autorizado por el enunciado, pero entonces la justificacion tiene que "
             "sostenerlo: que demuestra tener el front corriendo. Con `nginx:alpine`, el "
             "`RUN` de instalacion no aplica y hay que decirlo en vez de inventarse uno."),
            ("¿Por que no puedo usar `FROM node:latest`?",
             "Porque `latest` cambia sin avisar y la imagen que hoy funciona manana puede "
             "traer otra version mayor de Node. La reproducibilidad es el argumento entero "
             "de la clase: si la etiqueta no fija la version, no hay reproducibilidad."),
            ("¿El `.env` no queda protegido si lo borro en una capa posterior?",
             "No. Las capas son acumulativas y quedan en el historial: `docker history` y "
             "cualquiera que tenga la imagen pueden recuperar el archivo aunque una capa "
             "posterior lo borre. Los secretos se inyectan al ejecutar."),
            ("¿La captura tiene que mostrar la hora?",
             "Si, y es medio punto. La forma mas simple es ejecutar `date` justo antes de "
             "`docker ps`, para que la hora quede en la misma pantalla que la evidencia."),
            ("¿Que pongo en la fila de incidente si de verdad no fallo nada?",
             "El que estuvo a punto de fallar y por que no fallo. Sirve igual: el objetivo es "
             "que quede escrito un sintoma con su causa, que es lo que se va a necesitar en "
             "la Clase 8 cuando el pipeline falle sin explicacion."),
            ("¿Se puede usar Docker Compose?",
             "No hace falta y hoy suma ruido: la pregunta pide un servicio, un Dockerfile y "
             "un `docker run`. Compose entra cuando haya mas de un contenedor, que es a "
             "partir del diagrama de la Clase 4."),
        ],
        "cierre": (
            "Lo que sale de hoy no es «saber Docker»: es una unidad de despliegue con nombre, "
            "version y puerto, y un contrato de salud escrito. Esas cuatro cosas son las que "
            "la Clase 4 va a dibujar como caja `Container`, las que la Clase 7 va a colocar "
            "en el diagrama de despliegue con su puerto real y las que la Clase 8 va a "
            "verificar desde el pipeline. Cierre insistiendo en la coherencia del puerto "
            "entre las tres preguntas: es el detalle que separa una entrega que se sostiene "
            "de una que se cae en la primera revision."
        ),
    },
    4: {
        "titulo": ("Solucion — Actividad del Corte 1, preguntas 12 a 15 "
                   "(monolito modular, C4 Container, contratos y riesgos)"),
        "resumen": (
            "Las cuatro ultimas preguntas del Corte 1, resueltas sobre **BiblioLite**. Las "
            "cuatro son **una sola cadena**: la decision de la 12 fija cuantas cajas puede "
            "tener el diagrama de la 13, las cajas de la 13 son los nombres que la 14 tiene "
            "que citar textualmente, y la 15 analiza las fronteras que la 13 dibujo. Se "
            "califican en ese orden y comparandolas entre si; leidas por separado, las cuatro "
            "parecen correctas incluso cuando se contradicen."
        ),
        "total": 25.0,
        "nota_actividad": (
            "Estas 4 preguntas valen los **25 puntos finales** de la actividad del Corte 1 y "
            "cierran los 100. La 13 es la unica pregunta de tipo **diagrama** de estas cuatro: "
            "si no renderiza, no se puede calificar, asi que conviene pedir que la peguen en "
            "la plataforma temprano y no en el ultimo minuto."
        ),
        "preguntas": [
            {
                "n": 12,
                "titulo": "Monolito modular o microservicios para BiblioLite",
                "tipo": "abierta",
                "puntos": 4.0,
                "respuesta": """**1. La decision**
BiblioLite se construye como **monolito modular**: un solo despliegue de la API de
prestamos, con tres modulos internos de frontera explicita — `catalogo`, `prestamos` y
`notificaciones` — y una sola base de datos.

**2. Los dos criterios**

- **Tamano del equipo**: **una persona**, durante **doce semanas**, con otras cuatro
  asignaturas encima. Partir en servicios significaria mantener tres despliegues, tres
  pipelines y tres registros de log yo solo. El costo de operacion se multiplica por tres y
  el tiempo de desarrollo no se divide por nada, porque el que programa sigue siendo uno.
- **Acoplamiento**: en BiblioLite,
  **reservar un ejemplar y marcar ese ejemplar como no disponible son el mismo cambio**.
  Si separo catalogo de prestamos, esas dos escrituras
  caen en dos servicios y en dos bases distintas, y tengo que resolver a mano lo que hoy
  resuelve una transaccion de una linea. Lo unico que de verdad cambia por separado es
  **notificaciones**: el aviso de vencimiento se puede modificar sin tocar la regla de
  prestamo, y por eso es el unico modulo que algun dia seria candidato a salir. Hoy no sale:
  todavia no hay razon.

**3. Que gano y que pierdo**

- **Gano**: la regla «no se presta el ultimo ejemplar si ya esta reservado» se cumple con
  una transaccion en una sola base. No necesito nada mas para que dos estudiantes no se
  lleven el mismo libro.
- **Pierdo**: no puedo escalar solo la consulta de disponibilidad, que es la operacion mas
  usada en semana de parciales. Si esa consulta se vuelve el cuello de botella, tengo que
  replicar toda la API. Es un precio que acepto hoy y que la Clase 13 va a revisar con
  numeros.""",
                "como_calificar": [
                    "1 pt la decision **nombrada en una frase y sin ambiguedad**. «Un poco de "
                    "los dos», «monolito por ahora pero microservicios despues» o no elegir "
                    "es **cero** en este criterio. El «despues» solo cuenta si va como frase "
                    "aparte y la decision de hoy quedo dicha.",
                    "1 pt tamano del equipo **con numero y plazo**. «Somos pocos» no es "
                    "numero; «una persona en doce semanas» si.",
                    "1 pt acoplamiento diciendo **que partes de su dominio cambian juntas**. "
                    "Se espera un par concreto de su ficha. Repetir la definicion de "
                    "acoplamiento sin aplicarla vale cero.",
                    "1 pt el que gana y que pierde **en terminos del dominio**. «Gano "
                    "simplicidad y pierdo escalabilidad» son etiquetas: valen la mitad si no "
                    "dicen que operacion concreta se beneficia y cual queda limitada.",
                    "**Elegir microservicios NO se penaliza.** Si el estudiante los "
                    "sustenta — por ejemplo porque el modulo de notificaciones tiene un "
                    "ritmo de cambio distinto y lo separa — la nota es completa, **y "
                    "entonces la pregunta 13 debe mostrar esas cajas separadas**. Lo que se "
                    "penaliza es partir por moda.",
                    "Antes de cerrar la nota, mire el diagrama de la pregunta 13. La "
                    "incoherencia entre las dos se castiga alla (3 pts), no aqui: aqui solo "
                    "se evalua el argumento.",
                ],
                "errores": [
                    "«Microservicios porque es lo que se usa en la industria». Es la respuesta "
                    "que la regla del curso ataca de frente. Pregunte en voz alta: «¿quien "
                    "despliega el tercer servicio el domingo antes de la sustentacion?».",
                    "Elegir monolito y creer que es la respuesta comoda o de menor nota. No lo "
                    "es, y conviene decirlo el primer minuto: un monolito modular bien "
                    "argumentado vale exactamente igual. Si no se dice, la mitad del grupo "
                    "escribe microservicios por miedo.",
                    "Confundir monolito modular con monolito sin modulos. Si elige monolito, "
                    "tiene que poder nombrar sus modulos internos; si no puede, lo que "
                    "describio es un solo bloque sin fronteras, que es otra cosa.",
                    "Justificar por tecnologia («React y Node son microservicios»). Ni el "
                    "lenguaje ni el framework deciden esto: lo decide cuantas unidades "
                    "desplegables hay.",
                    "Decidir microservicios y dibujar despues un solo contenedor con la base, "
                    "o al contrario. Es la incoherencia mas frecuente entre las dos preguntas "
                    "y cuesta 3 pts en la 13.",
                ],
            },
            {
                "n": 13,
                "titulo": "C4 Container de BiblioLite en Mermaid",
                "tipo": "diagrama",
                "puntos": 11.0,
                "respuesta_mermaid": """C4Container
    title Contenedores de CloudLite App - dominio BiblioLite
    Person(estudiante, "Estudiante", "Consulta disponibilidad y reserva ejemplares")
    Person(auxiliar, "Auxiliar de biblioteca", "Registra prestamos y devoluciones")
    System_Boundary(cloudlite, "CloudLite App") {
        Container(spa, "Aplicacion web", "React", "Consulta del catalogo y reserva de ejemplares")
        Container(api, "API de prestamos", "Node.js", "Modulos catalogo prestamos y notificaciones")
        ContainerDb(db, "Base de datos de prestamos", "PostgreSQL", "Titulos ejemplares reservas y prestamos")
    }
    System_Ext(idp, "Proveedor de identidad institucional", "Login OIDC de la universidad")
    System_Ext(correo, "Correo transaccional SaaS", "Envio de avisos de vencimiento")
    Rel(estudiante, spa, "Consulta disponibilidad y reserva un ejemplar", "HTTPS")
    Rel(auxiliar, spa, "Registra el prestamo y la devolucion", "HTTPS")
    Rel(spa, api, "Consulta el catalogo y crea reservas", "HTTPS/JSON")
    Rel(api, db, "Lee y escribe ejemplares reservas y prestamos", "TCP/SQL")
    Rel(api, idp, "Valida que el usuario es estudiante activo", "OIDC sobre HTTPS")
    Rel(api, correo, "Solicita el envio del aviso de vencimiento", "API REST sobre HTTPS")
    Rel(correo, estudiante, "Entrega el aviso 2 dias antes del vencimiento", "SMTP")""",
                "respuesta": """**Justificacion de cada caja** (las dos preguntas obligatorias: que responsabilidad propia
tiene y por que se despliega por separado)

- **Aplicacion web (React)** — responsabilidad: presentar el catalogo y capturar la reserva.
  Se despliega por separado porque son archivos estaticos que se sirven desde un CDN y se
  actualizan sin reiniciar la API. Es una unidad desplegable distinta de verdad, no una
  carpeta.
- **API de prestamos (Node.js)** — responsabilidad: las reglas de disponibilidad, reserva y
  renovacion. Es **el** monolito modular de la pregunta 12: los tres modulos van dentro de
  esta caja, no en cajas separadas, y eso es lo que hace coherentes las dos preguntas.
- **Base de datos de prestamos (PostgreSQL)** — responsabilidad: guardar el estado. Se
  despliega por separado porque tiene su propio ciclo de vida: sobrevive a cada nueva
  version de la API y se respalda con otra frecuencia.

**Tres contenedores, no seis.** No hay caja de cache, ni de worker, ni de «servicio de
autenticacion»: la autenticacion la delega el `idp`, que ya es un `System_Ext` y por eso no
se dibuja adentro. Cada caja que no pueda responder las dos preguntas no se dibuja.

**Trazabilidad con el Context de la pregunta 3.** Los cinco nombres se copian tal cual:
`Estudiante`, `Auxiliar de biblioteca`, `CloudLite App`,
`Proveedor de identidad institucional` y `Correo transaccional SaaS`.
Lo unico que cambia es que la caja que en
Context era una sola ahora es una `System_Boundary` con tres contenedores dentro. Estos
mismos nombres son los que la Clase 7 pone en el diagrama de despliegue y los que la Clase
11 revisa en el checkpoint.""",
                "como_calificar": [
                    "3 pts **entre 2 y 5 contenedores, cada uno con su tecnologia** entre "
                    "parentesis. Se descuenta por cada caja de mas sin justificacion: la "
                    "prueba es si el estudiante puede responder las dos preguntas "
                    "(responsabilidad propia, despliegue por separado) de esa caja.",
                    "2 pts los almacenes de datos con `ContainerDb(...)`. Una base declarada "
                    "como `Container` normal pierde este criterio completo, aunque diga "
                    "PostgreSQL: el tipo de caja es informacion, no decoracion.",
                    "3 pts que **TODA** flecha lleve protocolo y formato. Se cuenta flecha por "
                    "flecha: una sola sin protocolo ya descuenta. Formas aceptables: `HTTPS`, "
                    "`HTTPS/JSON`, `TCP/SQL`, `OIDC sobre HTTPS`, `SMTP`, `evento/cola`.",
                    "2 pts que los nombres de sistema, actores y sistemas externos sean "
                    "**identicos** a los del C4 Context de la pregunta 3. Este criterio se "
                    "califica con las dos respuestas abiertas al lado; no se puede evaluar "
                    "leyendo solo el diagrama.",
                    "1 pt que renderice sin error en la plataforma. Si no renderiza, ese punto "
                    "se pierde pero **los otros diez se siguen calificando** sobre el codigo "
                    "que escribio: no se anula la pregunta entera por una coma.",
                    "**Si el numero de cajas contradice la decision de la pregunta 12** — "
                    "cinco servicios sueltos habiendo elegido monolito modular, o un solo "
                    "contenedor habiendo elegido microservicios — **se pierden los 3 pts de "
                    "los contenedores**. Es la unica penalizacion cruzada del dia y hay que "
                    "anunciarla antes del taller.",
                    "Que la API contenga varios modulos **nombrados en la descripcion de la "
                    "caja** es la forma correcta de mostrar un monolito modular en C4. No "
                    "exija cajas internas para los modulos: C4 Container muestra unidades "
                    "desplegables, y tres modulos en un despliegue son una caja.",
                ],
                "errores": [
                    "Dibujar el `idp` o el correo **dentro** de la `System_Boundary`. Son "
                    "sistemas de terceros: si estuvieran adentro, el estudiante tendria que "
                    "desplegarlos. Es el error de frontera mas comun del nivel Container.",
                    "Renombrar las cajas respecto al Context: «Alumno» donde antes decia "
                    "«Estudiante», «Servicio de email» donde decia «Correo transaccional "
                    "SaaS». Cuesta los 2 pts de trazabilidad y rompe las Clases 7 y 11.",
                    "Comas dentro de las etiquetas entre comillas. Rompen la sintaxis del C4 "
                    "en Mermaid y se llevan el punto de renderizado. Se separa con «y» o con "
                    "espacio, como en `\"Titulos ejemplares reservas y prestamos\"`.",
                    "Una caja por cada tabla de la base de datos. Confunde nivel Container con "
                    "modelo de datos. La base es **una** caja `ContainerDb`; lo que hay "
                    "dentro se modela en Bases de Datos II.",
                    "Flechas rotuladas «usa», «se conecta» o «envia datos». Sin verbo de "
                    "negocio y sin protocolo no cuentan, igual que en la pregunta 3.",
                    "Pegar el Mermaid que devolvio la IA sin revisarlo: aparecen cinco cajas "
                    "y una cola de mensajes que nadie decidio, y el diagrama contradice la "
                    "pregunta 12. La sintaxis la acierta la IA; la decision sigue siendo del "
                    "estudiante y es lo que se califica.",
                    "Usar `C4Context` en la primera linea por copiar la pregunta 3. La "
                    "primera linea debe ser exactamente `C4Container`, y con la otra el "
                    "`System_Boundary` no dibuja los contenedores.",
                ],
            },
            {
                "n": 14,
                "titulo": "Los tres contratos de BiblioLite",
                "tipo": "abierta",
                "puntos": 7.0,
                "tabla": {
                    "headers": ["Contrato", "Quien llama a quien", "Verbo y ruta",
                                "Error de negocio"],
                    "rows": [
                        ["Reservar un ejemplar",
                         "Aplicacion web -> API de prestamos",
                         "`POST /titulos/{isbn}/reservas`",
                         "**409** el ultimo ejemplar disponible ya fue reservado por otro "
                         "estudiante mientras este llenaba el formulario"],
                        ["Validar al solicitante",
                         "API de prestamos -> Proveedor de identidad institucional",
                         "`POST /oauth2/introspect`",
                         "**403** el carne es valido pero no corresponde a un estudiante "
                         "activo de este semestre"],
                        ["Avisar el vencimiento",
                         "API de prestamos -> Correo transaccional SaaS",
                         "`POST /v1/mensajes`",
                         "**422** la direccion institucional del estudiante no existe o esta "
                         "desactivada"],
                    ],
                },
                "respuesta": """**Por que estos tres y no otros.** Son las tres fronteras que el diagrama de la pregunta 13
dibuja hacia afuera de la API: una desde el front, una hacia identidad y una hacia el correo.
Los nombres de la columna del medio son literalmente los de las cajas: `Aplicacion web`,
`API de prestamos`, `Proveedor de identidad institucional`, `Correo transaccional SaaS`.

**El 409 es el que importa.** Es un conflicto, no una falla: el servidor esta perfectamente
sano y la peticion esta bien formada, pero el mundo cambio entre que el estudiante vio
«1 disponible» y que apreto el boton. Ese caso aparece en cuanto dos personas hacen lo mismo
a la vez, y en semana de parciales pasa todos los dias. El 409 se retoma en la Clase 13 con
concurrencia y escalado, y en Bases de Datos II con la transaccion que lo evita.

**Nota sobre el tercero.** Si el aviso de vencimiento se hiciera con una cola en vez de una
llamada directa, este contrato se escribiria como **`evento prestamo.por_vencer`** en la
columna del verbo, y entonces el error de negocio no seria un codigo de respuesta sino la
politica del mensaje que no se pudo entregar. Hoy es sincrono porque el diagrama de la
pregunta 13 no tiene cola, y el contrato tiene que describir lo que esta dibujado, no lo que
seria elegante.""",
                "como_calificar": [
                    "3 pts los tres contratos con **quien llama a quien usando los nombres "
                    "exactos** de las cajas del diagrama, 1 pt cada uno. «El front llama al "
                    "backend» no son los nombres exactos: vale la mitad de ese punto.",
                    "2 pts los verbos y rutas **bien formados**: verbo HTTP en mayuscula mas "
                    "ruta con recurso en plural, o el nombre del evento si la comunicacion es "
                    "asincrona. `GET /obtenerDatos` o `POST /hacerReserva` estan mal "
                    "formados; descuente sin dramatizar y muestre la forma correcta.",
                    "2 pts los errores de negocio con **codigo y significado en el dominio**. "
                    "Se pierde el punto del error que diga `500` o «error generico»: eso es "
                    "una falla, no un contrato.",
                    "**Se pierde 1 pt del total si ninguno de los tres es un `409` de "
                    "conflicto.** Es explicito en el enunciado y hay que anunciarlo: es el "
                    "unico requisito de la pregunta que no se puede improvisar al final.",
                    "Un `403` o un `422` bien explicados en el dominio valen igual que el 409 "
                    "en su propia fila. Lo que no se acepta es que los tres sean el mismo "
                    "codigo o los tres del mismo par de cajas.",
                    "Si los contratos citan cajas que **no existen** en el diagrama de la "
                    "pregunta 13, se pierden los puntos de esas filas. Es la senal de que la "
                    "respuesta se escribio sin mirar el diagrama propio.",
                ],
                "errores": [
                    "«500 error del servidor» como error de negocio. Es el error que el "
                    "enunciado descarta con nombre propio: un 500 significa que el sistema "
                    "se rompio, y de eso no se puede hacer un contrato porque nadie promete "
                    "romperse de una forma concreta.",
                    "Los tres contratos entre la misma pareja de cajas, casi siempre "
                    "`Aplicacion web -> API de prestamos`. Se acepta uno repetido si son "
                    "operaciones distintas, pero tres seguidos indican que no se recorrieron "
                    "las fronteras del diagrama.",
                    "Codigo sin significado: «409 conflicto». La mitad del criterio es el "
                    "**que significa en su dominio**. Pida la frase completa: «409 el ultimo "
                    "ejemplar ya fue reservado».",
                    "Confundir 401 con 403: 401 es «no se sabe quien es usted», 403 es «se "
                    "sabe y no puede». En el contrato de identidad el correcto suele ser 403, "
                    "pero no descuente si el 401 esta bien argumentado.",
                    "Contratos hacia la base de datos escritos como si fueran HTTP "
                    "(`POST /ejemplares` hacia PostgreSQL). Ese contrato existe, pero se "
                    "escribe como sentencia SQL o como operacion del repositorio, no como "
                    "ruta REST.",
                    "Inventar rutas para el proveedor de identidad o para el correo sin "
                    "mirar su documentacion. No se penaliza la ruta aproximada, pero si vale "
                    "corregirlo: los contratos con terceros no se eligen, se leen.",
                ],
            },
            {
                "n": 15,
                "titulo": "Los tres riesgos de distribucion de BiblioLite",
                "tipo": "abierta",
                "puntos": 3.0,
                "respuesta": """**1. Que se rompe cuando una pieza no responde**
Si se cae el **Correo transaccional SaaS**: **deja de funcionar** la capacidad «notificar el
vencimiento del prestamo», que es una de las cuatro de mi ficha; el estudiante no recibe el
aviso dos dias antes y se enterara al devolver tarde. **Sigue funcionando** todo lo demas:
consultar disponibilidad, reservar, renovar y registrar el prestamo en mostrador, porque
ninguna de esas operaciones espera respuesta del correo. La reserva se guarda igual: lo que
se pierde es el aviso, no la reserva. Si en cambio se cayera la
**Base de datos de prestamos**, ahi si se cae todo, porque es la unica caja sin la
cual no hay estado.

**2. Que latencia agrega cada salto**
Contando una reserva completa de punta a punta, son **seis saltos de red**:

1. Estudiante -> Aplicacion web (HTTPS)
2. Aplicacion web -> API de prestamos (HTTPS/JSON)
3. API -> Proveedor de identidad institucional (validar el token)
4. API -> Base de datos (leer la disponibilidad del ejemplar)
5. API -> Base de datos (escribir la reserva)
6. API -> Correo transaccional SaaS (confirmacion)

**Antes eran cero.** En el prototipo de una sola pieza con un archivo local, reservar era una
llamada de funcion y una escritura en disco: ni un salto. Dos observaciones que salen de
contarlos: si guardo en cache las claves publicas del `idp`, el salto 3 desaparece de la
mayoria de las peticiones; y si el correo se envia en segundo plano, el estudiante espera
cinco saltos en vez de seis. Contar es lo que permite ver esas dos decisiones.

**3. Que datos quedan expuestos a inconsistencia**
El **estado del ejemplar** (`ejemplares.estado`) se actualiza en el mismo momento en que se
crea la reserva: son **dos escrituras** que deben ocurrir juntas. Si la primera guarda la
reserva y la segunda falla, el ejemplar sigue apareciendo como disponible y el siguiente
estudiante lo reserva tambien: dos reservas sobre el mismo ejemplar fisico, y alguien llega a
la biblioteca a un libro que no esta. Como las dos escrituras viven en la misma base
—consecuencia directa de haber elegido monolito modular—, una transaccion las cubre.
El dato que **no** puedo cubrir es el correo ya enviado: si la transaccion se revierte
despues de que el aviso salio, el estudiante tiene en su bandeja la confirmacion de una
reserva que no existe, y un correo no se puede hacer rollback.""",
                "como_calificar": [
                    "1 pt el riesgo de indisponibilidad **nombrando una caja concreta** del "
                    "diagrama y **distinguiendo que deja de funcionar de que sigue "
                    "funcionando**. «Se cae todo» es media respuesta: media si eligio una caja "
                    "de la que efectivamente depende todo, cero si no eligio ninguna.",
                    "1 pt el conteo de saltos de **una** operacion de punta a punta, con el "
                    "numero dicho. No se verifica si el numero es «el correcto»: se verifica "
                    "que la lista de saltos corresponda a su propio diagrama y que el total "
                    "coincida con la lista.",
                    "1 pt el dato expuesto a inconsistencia **nombrado** y con lo que pasa si "
                    "falla el segundo paso. Se espera un nombre de dato o de campo, no una "
                    "categoria: «los datos del prestamo» no lo es.",
                    "Una respuesta generica sobre «los microservicios son mas complejos» **no "
                    "suma en ningun criterio**, ni siquiera parcialmente. Es la respuesta que "
                    "esta pregunta esta diseñada para detectar.",
                    "Si eligio **monolito modular** en la pregunta 12, la pregunta aplica "
                    "igual y no se le baja nada: los saltos a la base y a los sistemas "
                    "externos son red. Rechazar la respuesta «no aplica porque es monolito» "
                    "es lo correcto, pero explique por que en la retroalimentacion.",
                    "Reconocer que el correo ya enviado no se puede revertir es un detalle "
                    "que merece comentario positivo. No es obligatorio para la nota completa, "
                    "pero es exactamente el tipo de observacion que la sustentacion de la "
                    "Clase 15 premia.",
                ],
                "errores": [
                    "«Si se cae un servicio se cae todo». Es el atajo que la pregunta pide "
                    "evitar de forma explicita. La correccion es concreta: «elija la caja del "
                    "correo y dígame si el estudiante puede reservar sin ella».",
                    "Contar saltos sin mirar el diagrama propio: aparecen cuatro saltos en una "
                    "arquitectura que tiene seis fronteras, o al reves. Cuente con el "
                    "estudiante sobre su Mermaid; toma un minuto y es la parte que mas "
                    "aprende.",
                    "Olvidar que la base de datos es un salto de red. Es el olvido mas comun "
                    "de quienes eligieron monolito: creen que solo cuentan las llamadas entre "
                    "servicios.",
                    "Nombrar como riesgo de inconsistencia algo que se resuelve con una "
                    "transaccion **sin decirlo**. Si las dos escrituras estan en la misma "
                    "base, la respuesta completa incluye que ahi hay una transaccion "
                    "posible; si estuvieran en dos bases, no la habria, y eso es justo el "
                    "costo de partir.",
                    "Confundir riesgo con falla de seguridad («alguien puede robar los "
                    "datos»). Eso es la Clase 6 y tiene su propio entregable; aqui el tema es "
                    "indisponibilidad, latencia e inconsistencia.",
                    "Responder los tres riesgos en un solo parrafo sin numerar. El enunciado "
                    "pide ese orden y con tres criterios de 1 pt cada uno; sin separacion, la "
                    "calificacion se vuelve adivinanza y casi siempre pierde puntos el "
                    "estudiante.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Cuantas cajas debe tener mi diagrama?",
             "Entre 2 y 5, y el numero lo decide la pregunta 12, no el gusto. Con monolito "
             "modular lo normal son tres: front, API y base. Cada caja de mas tiene que "
             "responder «que responsabilidad propia tiene» y «por que se despliega por "
             "separado»; si no responde las dos, se borra."),
            ("Si elijo monolito modular, ¿donde dibujo los modulos?",
             "En la descripcion de la caja de la API, no como cajas aparte. C4 Container "
             "muestra **unidades desplegables**, y tres modulos en un solo despliegue son una "
             "sola caja. Los modulos por separado se dibujan en el nivel Component, que este "
             "curso no exige."),
            ("¿El proveedor de identidad va dentro o fuera de la frontera?",
             "Fuera, como `System_Ext`, igual que en el Context de la pregunta 3. La prueba es "
             "simple: ¿lo despliega usted? Si la respuesta es no, va fuera."),
            ("¿Puedo cambiar los nombres que puse en el Context de la pregunta 3?",
             "No sin volver atras y cambiarlos alli tambien. Son 2 puntos aqui, y los mismos "
             "nombres se usan en el diagrama de despliegue de la Clase 7 y en el checkpoint de "
             "la Clase 11. Un renombre suelto se paga tres veces."),
            ("¿Mi Mermaid no renderiza y no encuentro el error?",
             "Casi siempre es una coma dentro de una etiqueta entre comillas, o la primera "
             "linea escrita como `C4Context` en vez de `C4Container`. Revise esas dos antes "
             "de cualquier otra cosa."),
            ("¿Tengo que usar 409 obligatoriamente?",
             "Al menos uno de los tres contratos, si. No es capricho: el conflicto es el error "
             "que aparece en cuanto dos personas hacen lo mismo a la vez, y es el hilo que la "
             "Clase 13 retoma con concurrencia. Sin ningun 409 se pierde 1 punto de los 7."),
            ("¿Y si mi comunicacion es asincrona?",
             "Entonces en la columna del verbo va el nombre del evento (`evento "
             "prestamo.por_vencer`) y la flecha del diagrama va etiquetada `evento/cola`. Lo "
             "que no puede pasar es que el contrato diga evento y el diagrama muestre una "
             "llamada REST: el contrato describe lo que esta dibujado."),
            ("¿Es peor nota elegir monolito?",
             "No, y conviene repetirlo hasta que se crea: un monolito modular bien "
             "argumentado vale exactamente lo mismo. Con un equipo de una persona y doce "
             "semanas, ademas, es casi siempre la decision defendible."),
        ],
        "cierre": (
            "Con esta clase queda cerrado el Corte 1: hay una ficha de dominio, un Context, un "
            "ADR, un contenedor que corre y ahora un diagrama de contenedores con contratos y "
            "riesgos. Lo que hay que dejar dicho es que **los nombres de estas cajas ya no se "
            "cambian**: el diagrama de despliegue de la Clase 7 los coloca en subredes con "
            "puertos, la tabla de amenazas de la Clase 6 los usa como activos, la Clase 11 "
            "audita que coincidan y la Clase 15 pregunta por que existe cada uno. Y deje "
            "anotado el 409 en el tablero: es el error que la Clase 13 va a volver a abrir "
            "cuando se hable de escalar."
        ),
    },
    6: {
        "titulo": ("Solucion — Actividad del Corte 2, preguntas 1 a 3 "
                   "(amenazas STRIDE, controles y politica de secretos)"),
        "resumen": (
            "Las tres primeras preguntas del Corte 2, resueltas sobre **BiblioLite** y sobre "
            "los diagramas que ya existen del Corte 1. La clave de estas tres es que **no se "
            "puede responder sin abrir el C4 Container de la Clase 4**: la pregunta 2 exige "
            "senalar caja o flecha, y quien no tenga diagrama solo puede escribir intenciones. "
            "Si algun estudiante no entrego el diagrama, ese es el problema a resolver antes "
            "del taller, no durante."
        ),
        "total": 25.0,
        "nota_actividad": (
            "Estas 3 preguntas valen **25 de los 100 puntos** de la actividad del Corte 2, que "
            "es una sola actividad de 12 preguntas para las Clases 6, 7, 8 y 10. La pregunta 2 "
            "depende de la 1: si las amenazas de la 1 son genericas, la 2 no tiene nada donde "
            "aterrizar. Conviene calificar las dos seguidas y de la misma sentada."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "Cinco amenazas STRIDE-lite de BiblioLite",
                "tipo": "abierta",
                "puntos": 8.75,
                "tabla": {
                    "headers": ["#", "Categoria", "Amenaza (actor o dato + camino)"],
                    "rows": [
                        ["1", "**S** — Suplantacion",
                         "Un estudiante puede reservar un ejemplar **en nombre de otro** "
                         "porque `POST /titulos/{isbn}/reservas` toma el `id_estudiante` del "
                         "cuerpo de la peticion en vez de tomarlo del token que valido el "
                         "proveedor de identidad. Basta con cambiar un numero en el JSON."],
                        ["2", "**E** — Elevacion de privilegio",
                         "Cualquier estudiante autenticado puede llamar `POST /prestamos`, "
                         "que es la operacion de mostrador del **auxiliar de biblioteca**, "
                         "porque la API verifica que el token sea valido pero **no verifica el "
                         "rol**. Un estudiante podria registrarse a si mismo un prestamo sin "
                         "pasar por el mostrador."],
                        ["3", "**I** — Fuga de informacion",
                         "Un estudiante consulta `GET /prestamos/17`, `/18`, `/19` con "
                         "identificadores consecutivos y lee **que libros pidio prestados otro "
                         "companero**, porque el endpoint valida que haya sesion pero no que "
                         "el prestamo le pertenezca. El historial de lectura es dato personal."],
                        ["4", "**I** — Fuga de informacion (secretos)",
                         "La cadena de conexion de PostgreSQL y la clave del correo "
                         "transaccional quedaron dentro de la imagen `bibliolite-api:0.1.0` "
                         "por un `COPY . .` que arrastro el `.env`. Cualquiera que descargue "
                         "la imagen del registro las lee con `docker history`, incluso si una "
                         "capa posterior borro el archivo."],
                        ["5", "**R** — Repudiacion",
                         "El auxiliar puede **modificar la fecha de devolucion** de un "
                         "prestamo vencido con un `UPDATE` directo y despues negar haberlo "
                         "hecho, porque la tabla `prestamos` guarda solo el estado actual y "
                         "no existe ninguna bitacora de quien cambio que y cuando."],
                    ],
                },
                "respuesta": """**Por que estas cinco y no una lista de manual.** Las cinco nombran una ruta concreta
(`POST /titulos/{isbn}/reservas`, `GET /prestamos/17`), un actor de la ficha (estudiante,
auxiliar de biblioteca) o un dato del dominio (historial de prestamos, cadena de conexion), y
el camino por el que la amenaza ocurre. Esa es la diferencia que el enunciado exige: «fuga de
informacion» es una categoria; la fila 3 es una amenaza.

**Dos amenazas comparten la letra I y eso esta bien.** La 3 y la 4 son ambas fuga, pero una
ocurre en tiempo de ejecucion por una autorizacion incompleta y la otra en tiempo de
construccion por un archivo que no debia entrar en la imagen. Los controles son distintos y
los momentos son distintos, asi que no son la misma amenaza con otras palabras. STRIDE es una
guia de categorias, no una cuota de una por letra.

**Una sexta que quedo fuera, para tenerla en el bolsillo:** **D** — un script sin
autenticacion golpea `GET /titulos?disponible=true` mil veces por minuto en semana de
parciales y la base se queda sin conexiones libres. No entro en las cinco porque el impacto
academico es menor que los otros, pero si un estudiante la elige, es perfectamente valida y
conecta con el escalado de la Clase 13.""",
                "como_calificar": [
                    "1.75 pts por amenaza bien formada, hasta 5. Una amenaza suma completo "
                    "**solo si nombra el actor o el dato concreto del dominio y el camino por "
                    "el que ocurre**. Los tres elementos: quien, sobre que, y como.",
                    "Una amenaza generica vale **la mitad**: «podrian hackear la base de "
                    "datos», «hay riesgo de fuga de informacion», «un atacante puede entrar». "
                    "La prueba rapida es preguntarse si esa frase se podria copiar sin cambiar "
                    "una letra al proyecto de otro estudiante. Si se puede, es de manual.",
                    "Se descuenta si **dos amenazas son la misma con otras palabras**: «no hay "
                    "autenticacion» y «cualquiera puede entrar a la API» son una sola. Dos "
                    "amenazas de la misma letra de STRIDE **si** se aceptan cuando el camino "
                    "y el control son distintos.",
                    "No se exige una amenaza por cada letra, y no se premia cubrir las seis. "
                    "Cinco amenazas reales de tres letras valen mas que seis frases vacias "
                    "que completan el acronimo.",
                    "Que la amenaza pueda ubicarse en el diagrama del Corte 1 es senal de que "
                    "esta bien formada. Si al leerla no se sabe sobre que caja cae, la "
                    "pregunta 2 va a fallar tambien: dígalo en la retroalimentacion de esta.",
                ],
                "errores": [
                    "Pegar la lista de las cuatro amenazas de ejemplo del enunciado. Estan "
                    "puestas como referencia de **forma**, no como respuesta, y el enunciado lo "
                    "dice. Anunciarlo al abrir el taller ahorra la mitad de las correcciones.",
                    "Listar controles en vez de amenazas: «falta HTTPS», «no hay validacion». "
                    "Eso es la pregunta 2. La amenaza describe **que puede pasar y quien lo "
                    "hace**; el control describe como se evita.",
                    "Amenazas de un sistema que no es el suyo: pagos, tarjetas, transferencias. "
                    "Casi siempre viene de un ejemplo de internet. Devuelvala con la pregunta "
                    "«¿su dominio cobra algo?».",
                    "Confundir repudiacion con negacion de servicio por la letra. Repudiacion "
                    "es «puedo negar que lo hice» y se combate con bitacora; DoS es «te dejo "
                    "sin servicio». Es la confusion mas comun de STRIDE.",
                    "Cinco amenazas que caen todas sobre la base de datos. Si ninguna toca el "
                    "front, la API, el proveedor de identidad ni la imagen del contenedor, es "
                    "que no se recorrio el diagrama pieza por pieza.",
                    "Escribir la amenaza en futuro condicional infinito («podria "
                    "eventualmente llegar a pasar que alguien...»). Pida presente y concreto: "
                    "«un estudiante cambia el numero y lee el prestamo de otro».",
                ],
            },
            {
                "n": 2,
                "titulo": "El control de cada amenaza y donde se ve en el diagrama",
                "tipo": "abierta",
                "puntos": 8.75,
                "tabla": {
                    "headers": ["Amenaza", "Control", "Donde se ve (caja o flecha)"],
                    "rows": [
                        ["1. Reservar en nombre de otro",
                         "El `id_estudiante` se ignora si viene en el cuerpo: se toma del "
                         "`sub` del token verificado contra el `idp`. Verificable con una "
                         "prueba que manda un id ajeno y espera `403`.",
                         "**Flecha** `API de prestamos -> Proveedor de identidad "
                         "institucional` (validacion del token) y **caja** `API de "
                         "prestamos` (la regla que ignora el cuerpo)."],
                        ["2. Estudiante ejecutando la operacion del auxiliar",
                         "Autorizacion por rol en el propio endpoint: `POST /prestamos` exige "
                         "el rol `auxiliar` presente en el token. Verificable con dos tokens "
                         "de prueba, uno de cada rol.",
                         "**Caja** `API de prestamos`, en el modulo `prestamos`. No es del "
                         "front: un control en la `Aplicacion web` solo esconde el boton."],
                        ["3. Leer el prestamo de otro por identificador",
                         "La consulta filtra siempre por el dueno: "
                         "`WHERE id = $1 AND id_estudiante = $2`, con el segundo parametro "
                         "tomado del token. Verificable pidiendo un id ajeno y esperando "
                         "`404`.",
                         "**Caja** `API de prestamos` y **flecha** `API de prestamos -> Base "
                         "de datos de prestamos`, que es donde el filtro se aplica de verdad."],
                        ["4. Secretos dentro de la imagen",
                         "`.dockerignore` con `.env` y `.env.*`, secretos inyectados como "
                         "variables de entorno al ejecutar, y una verificacion en la CI que "
                         "falla si `docker history` menciona `.env`. Verificable: el pipeline "
                         "se pone rojo.",
                         "**Caja** `API de prestamos` (su imagen) y la frontera de "
                         "construccion: el pipeline de la Clase 8, que es donde el control se "
                         "ejecuta solo."],
                        ["5. Cambiar la fecha y negarlo",
                         "Tabla `auditoria` con `quien`, `que`, `antes`, `despues` y "
                         "`cuando`, escrita en la misma transaccion del cambio, y sin permiso "
                         "de `UPDATE` ni `DELETE` sobre ella para el usuario de la "
                         "aplicacion. Verificable: se cambia una fecha y aparece la fila.",
                         "**Caja** `Base de datos de prestamos` (la tabla y sus permisos) y "
                         "**flecha** `API de prestamos -> Base de datos de prestamos`."],
                    ],
                },
                "respuesta": """**Principio de menor privilegio, aplicado a un componente concreto**

Lo aplico sobre la **conexion de la `API de prestamos` a la `Base de datos de prestamos`**. La
API no se conecta como superusuario: usa el rol `bibliolite_api`, al que le concedo
exactamente `SELECT`, `INSERT` y `UPDATE` sobre `titulos`, `ejemplares`, `reservas` y
`prestamos`, mas `INSERT` — solo `INSERT` — sobre `auditoria`.

**Que deja de poder hacer al aplicarlo:** ese rol **no puede** borrar filas (`DELETE`), no
puede alterar la estructura (`DROP`, `ALTER`), no puede leer ningun otro esquema de la misma
instancia, y **no puede modificar ni borrar la bitacora de auditoria** que el mismo escribe.
Eso ultimo es lo importante: si manana aparece una inyeccion de SQL en la API — la amenaza que
Bases de Datos II trabaja con parametros —, el atacante hereda estos permisos y **no** los del
dueno de la base. Puede hacer dano, pero no puede borrar la evidencia de haberlo hecho ni
tumbar el esquema.

**Nota sobre la segunda columna.** Tres de los cinco controles caen en la caja `API de
prestamos`. No es un defecto: es la consecuencia de que casi toda la autorizacion vive donde
estan las reglas de negocio. Lo que si seria defecto es que un control cayera en la
`Aplicacion web`: ocultar un boton no es un control, porque la peticion se puede enviar sin
pasar por la interfaz.""",
                "como_calificar": [
                    "1 pt por cada control **concreto y verificable**, hasta 5. La prueba de "
                    "«verificable» es poder decir en una frase que se hace para comprobar que "
                    "el control esta puesto. «Usar buenas practicas», «mejorar la seguridad» o "
                    "«validar los datos» **no suman nada**.",
                    "2.5 pts por senalar correctamente la **caja o la flecha** de cada "
                    "control, prorrateado: 0.5 pts por fila. Se acepta «caja X» o «flecha X -> "
                    "Y» siempre que el nombre exista en el C4 Container de la Clase 4 o en el "
                    "diagrama de despliegue de la Clase 7.",
                    "1.25 pts el **principio de menor privilegio aplicado a un componente "
                    "concreto, diciendo que deja de poder hacer**. Las dos mitades pesan "
                    "igual: definirlo sin aplicarlo vale 0.6, y aplicarlo sin decir que se "
                    "pierde tambien.",
                    "Un control ubicado en la caja equivocada se corrige y se descuenta solo "
                    "esa fila. El caso tipico es poner en la `Aplicacion web` un control de "
                    "autorizacion: comente por que no sirve (la peticion se puede enviar sin "
                    "el front) en vez de solo tachar.",
                    "Que varios controles caigan en la misma caja **no se penaliza**. La API "
                    "concentra la autorizacion y eso es normal. Lo que se revisa es que la "
                    "caja senalada sea la correcta, no que esten repartidos.",
                    "Si un control no se puede ubicar en ninguna caja ni flecha del diagrama, "
                    "el enunciado da la lectura correcta: probablemente falta una pieza en el "
                    "diagrama. Escribalo asi en la retroalimentacion — es un hallazgo util "
                    "para el checkpoint de la Clase 11, no solo un descuento.",
                ],
                "errores": [
                    "«Usar HTTPS» como control de todo. HTTPS protege el dato en transito y no "
                    "resuelve ninguna de las cinco amenazas de arriba: ni la suplantacion, ni "
                    "el rol, ni el IDOR, ni el secreto en la imagen, ni el repudio. Es el "
                    "control comodin y hay que cortarlo.",
                    "Dejar la tercera columna en blanco o poner «en todo el sistema». Es la "
                    "mitad de la nota y el enunciado explica por que: un control que no se "
                    "puede senalar en un artefacto todavia es una intencion.",
                    "Definir menor privilegio con la definicion del libro y no aplicarlo. Pida "
                    "las dos frases: sobre que componente, y que deja de poder hacer.",
                    "Controles de front para amenazas de API: «deshabilito el boton», «oculto "
                    "el campo». La correccion en clase es una linea de `curl` que manda la "
                    "peticion sin abrir el navegador.",
                    "Confundir autenticacion con autorizacion. La amenaza 2 no se resuelve "
                    "pidiendo login: el estudiante **ya** tiene login. Se resuelve verificando "
                    "el rol. Es la distincion que mas se falla en esta pregunta.",
                    "Un control por amenaza pero sin correspondencia con las amenazas de la "
                    "pregunta 1 — cinco controles para cinco amenazas distintas de las que "
                    "listo. Califique la coherencia entre las dos preguntas; se ve en treinta "
                    "segundos poniendolas al lado.",
                ],
            },
            {
                "n": 3,
                "titulo": "Politica de secretos del repositorio y de la CI",
                "tipo": "abierta",
                "puntos": 7.5,
                "respuesta": """**1. Donde viven los secretos**
- En la **configuracion del repositorio**: los `secrets` del proyecto en GitHub, que se
  inyectan como variables de entorno solo durante la ejecucion del pipeline y que no se
  pueden volver a leer desde la interfaz una vez guardados.
- En **las variables de entorno del proveedor de PaaS** para el servicio en ejecucion, que es
  coherente con el ADR-001 de la Clase 2.
- En **local**, en un archivo `.env` que esta en `.gitignore` y en `.dockerignore`. Lo que si
  se versiona es `.env.example`, con los nombres de las variables y **sin un solo valor
  real**, para que otra persona sepa que necesita sin recibir nada.

Los tres secretos de BiblioLite son: `DATABASE_URL`, `CORREO_API_KEY` y el secreto de cliente
del proveedor de identidad.

**2. Quien los rota**
El **dueno del repositorio**, que en este proyecto soy yo y es la unica persona con permiso de
administracion. Queda escrito en el `README` para que no dependa de la memoria: si manana el
proyecto pasa a dos personas, el responsable sigue siendo un rol, no un nombre.

**3. Con que frecuencia**
- Rotacion programada: **al cierre de cada corte**, es decir cada cinco semanas, y en la
  entrega final antes de la sustentacion de la Clase 15.
- Rotacion inmediata, sin esperar el calendario: si el secreto aparece en un log, en una
  captura de pantalla, en un `docker history`, en el chat del grupo, o si alguien con acceso
  deja el proyecto.

**4. Que esta explicitamente prohibido**
- Escribir un secreto en el `Dockerfile`, en el `README`, en el YAML del pipeline en claro o
  en cualquier archivo que entre a git.
- Hacer `COPY . .` sin `.dockerignore`, que es la via por la que el `.env` entra a la imagen
  sin que nadie lo escriba a proposito.
- Imprimir variables de entorno en el pipeline (`env`, `printenv`, `echo $DATABASE_URL`): el
  log de la CI es publico en un repositorio publico.
- Pegar secretos en capturas de pantalla, en la bitacora del laboratorio o en el chat del
  grupo.
- Commits «temporales» con la clave «que borro despues». No existe el despues: el commit ya
  esta en el historial.

**5. Que hago si un secreto se filtra**
1. **Rotar la credencial**, primero y ya: generar una nueva en el proveedor e invalidar la
   anterior. El historial ya salio del equipo y no se puede recuperar; lo unico que esta bajo
   mi control es que la clave filtrada deje de servir.
2. Actualizar el secreto en la configuracion del repositorio y en el PaaS, y volver a
   despuegar.
3. Revisar los registros de acceso del proveedor por el periodo en que la clave estuvo
   expuesta, para saber si alguien la uso.
4. **Solo despues**, limpiar el historial de git — y sabiendo que es cosmetico: si el
   repositorio es publico, cualquier clon o cualquier indexador ya tiene la copia.

Borrar el commit primero es el orden equivocado: da la sensacion de haber resuelto el
problema mientras la credencial sigue siendo valida.""",
                "como_calificar": [
                    "1.5 pts cada una de las cuatro preguntas respondida **de forma "
                    "concreta**: donde viven, quien rota, cada cuanto, que se prohibe. Son 6 "
                    "pts en total y se califican una por una.",
                    "**Cero en la primera pregunta si la respuesta admite guardar secretos en "
                    "el repositorio en claro**, en cualquier forma: en el YAML, en un archivo "
                    "de configuracion versionado, «comentado» o «solo mientras desarrollo».",
                    "1.5 pts el procedimiento ante filtracion **empezando por rotar la "
                    "credencial y no por borrar el commit**. Si el primer paso es limpiar el "
                    "historial, este criterio es cero aunque el resto de los pasos esten bien: "
                    "el orden ES la respuesta.",
                    "«Quien los rota» exige un **responsable**, no un mecanismo. «Se rotan "
                    "automaticamente» no responde la pregunta: alguien tiene que ser el "
                    "responsable de que ocurra, incluso si la ejecucion es automatica.",
                    "«Con que frecuencia» exige un **numero o un evento del calendario**. «De "
                    "vez en cuando» o «periodicamente» no suman. Se acepta atarla a los cortes "
                    "del curso, que es lo mas realista para un proyecto de doce semanas.",
                    "Mencionar el `.env.example` versionado sin valores reales no es "
                    "obligatorio, pero es la senal de que el estudiante entendio la diferencia "
                    "entre **el nombre** de un secreto (publico) y **su valor** (privado). "
                    "Vale un comentario positivo.",
                ],
                "errores": [
                    "«Los guardo en un archivo de configuracion que no subo». Suena bien hasta "
                    "que se pregunta que impide subirlo. La respuesta completa nombra el "
                    "`.gitignore` **y** el `.dockerignore`: sin el segundo, el secreto no entra "
                    "a git pero si a la imagen.",
                    "Creer que borrar el commit resuelve la filtracion. Es el error central "
                    "que la pregunta esta diseñada para detectar. La frase para el tablero: "
                    "«el historial ya salio del equipo; lo unico que usted controla es que la "
                    "clave deje de servir».",
                    "Poner el secreto en el `Dockerfile` «porque es privado el repositorio». "
                    "El secreto queda en el historial de capas de la imagen, que viaja al "
                    "registro y se lee con `docker history` aunque el repo sea privado. Son "
                    "dos cosas distintas.",
                    "Imprimir el secreto en el pipeline para «verificar que llego». Es la "
                    "forma mas comun de filtrar una clave en un repositorio publico, y se hace "
                    "con buena intencion. La alternativa es verificar la **longitud** del "
                    "valor, no el valor.",
                    "Confundir secreto con variable de configuracion. La URL publica de la API "
                    "no es un secreto; la cadena de conexion si. Si la politica trata todo "
                    "como secreto, en la practica no se aplica ninguna.",
                    "Politica escrita en tercera persona y sin responsable («deberian "
                    "rotarse»). Una politica sin dueno no se ejecuta. Pida el nombre del rol.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Cuantas amenazas por cada letra de STRIDE?",
             "Ninguna cuota. Se piden cinco amenazas reales, no seis casillas llenas. Dos "
             "amenazas de la misma letra son validas si el camino y el control son distintos, "
             "y es lo que suele pasar con la fuga de informacion."),
            ("¿La amenaza tiene que ser posible en mi codigo actual?",
             "No necesariamente: se modela sobre el diseño, y a estas alturas casi nadie tiene "
             "el sistema completo. Lo que si tiene que ser es posible **en su arquitectura**, "
             "es decir, apoyada en una caja o una flecha que usted dibujo."),
            ("¿Que hago si un control no lo puedo ubicar en ninguna caja?",
             "Es informacion, no un problema: significa que al diagrama le falta una pieza o "
             "una frontera. Escribalo asi en la respuesta y anotelo para el checkpoint de la "
             "Clase 11. Vale mas que inventar una ubicacion."),
            ("¿HTTPS no cuenta como control?",
             "Cuenta, pero solo para la amenaza que de verdad mitiga: dato personal viajando en "
             "claro. Lo que no vale es usarlo como respuesta para las cinco filas. Cada "
             "amenaza tiene su control propio."),
            ("¿Menor privilegio va sobre la base de datos obligatoriamente?",
             "No. Puede ir sobre el token del correo transaccional que solo puede enviar y no "
             "leer la bandeja, o sobre el usuario del pipeline. Lo obligatorio es que sea un "
             "componente concreto y que diga **que deja de poder hacer**."),
            ("¿Donde pongo los secretos si todavia no tengo pipeline?",
             "En los `secrets` del repositorio igual: se configuran hoy y el pipeline de la "
             "Clase 8 los consume sin cambiar nada. Lo que no se hace nunca es dejarlos en un "
             "archivo «mientras tanto»."),
            ("¿Tengo que rotar los secretos de verdad durante el semestre?",
             "Al menos una vez, al cierre de un corte, y quedar la evidencia de que se hizo. Es "
             "la unica forma de descubrir que el sistema tenia la clave escrita en dos sitios "
             "que nadie recordaba."),
            ("Se me filtro una clave en un commit, ¿reprueba la actividad?",
             "No. Lo que se califica es el procedimiento: si rota primero y documenta, la "
             "respuesta esta completa. Este es exactamente el incidente que la pregunta "
             "entrena, y es mejor que ocurra en un proyecto de clase."),
        ],
        "cierre": (
            "Lo que se llevan de hoy es que la seguridad se escribe sobre un diagrama, no "
            "sobre una lista de buenas intenciones: cinco amenazas con nombre propio, cinco "
            "controles ubicados en una caja o en una flecha, y una politica de secretos con "
            "responsable y frecuencia. Deje dicho el enlace hacia adelante: el control 4 se "
            "vuelve automatico en el pipeline de la Clase 8, la tabla de amenazas se revisa en "
            "el checkpoint de la Clase 11 contra el diagrama actualizado, y en la sustentacion "
            "de la Clase 15 la pregunta de seguridad es literalmente «¿donde se ve ese control "
            "en su diagrama?»."
        ),
    },
    7: {
        "titulo": ("Solucion — Actividad del Corte 2, preguntas 4 a 6 "
                   "(despliegue en tres zonas, almacenamiento y correspondencia de nombres)"),
        "resumen": (
            "Las tres preguntas de la Clase 7 sobre **BiblioLite**, con el tercer angulo del "
            "sistema: donde se ejecuta cada pieza. La pregunta 4 vale 14 de los 25 puntos y "
            "tiene una trampa deliberada — **la base de datos en la zona publica cuesta 4 "
            "puntos completos** — y la 6 es la que cobra la trazabilidad de nombres que se "
            "viene exigiendo desde la Clase 4. Las tres se califican con el C4 Containers del "
            "Corte 1 abierto al lado."
        ),
        "total": 25.0,
        "nota_actividad": (
            "Estas 3 preguntas valen **25 de los 100 puntos** de la actividad del Corte 2 "
            "(Clases 6, 7, 8 y 10). La 4 es de tipo **diagrama** y es la pregunta con mas "
            "puntos de toda la actividad: conviene que la peguen en la plataforma en la primera "
            "media hora del taller y no al final."
        ),
        "preguntas": [
            {
                "n": 4,
                "titulo": "Diagrama de Despliegue de BiblioLite",
                "tipo": "diagrama",
                "puntos": 14.0,
                "respuesta_mermaid": """flowchart LR
    cliente["Cliente / navegador<br/>estudiante o auxiliar"]
    subgraph publica["Zona publica - internet"]
        edge["Edge / balanceador<br/>443 HTTPS"]
        spa["Aplicacion web<br/>React - estatico<br/>443 HTTPS"]
    end
    subgraph privada["Zona privada - solo alcanzable desde el edge"]
        api["API de prestamos<br/>Node.js<br/>3000 HTTP"]
    end
    subgraph datos["Zona de datos - sin salida a internet"]
        db[("Base de datos de prestamos<br/>PostgreSQL<br/>5432 TCP")]
    end
    idp["Proveedor de identidad institucional<br/>externo - 443"]
    correo["Correo transaccional SaaS<br/>externo - 443"]
    cliente -->|"HTTPS 443 - frontera de confianza"| edge
    cliente -->|"HTTPS 443 - descarga el bundle"| spa
    edge -->|"HTTP 3000"| api
    api -->|"TCP 5432"| db
    api -->|"HTTPS 443 - frontera de confianza"| idp
    api -->|"HTTPS 443 - frontera de confianza"| correo""",
                "respuesta": """**Las tres zonas y por que cada pieza esta donde esta**

- **Zona publica** — lo que internet alcanza directamente: el `Edge / balanceador` en el 443 y
  la `Aplicacion web`, que son archivos estaticos y por definicion publicos. Que el bundle de
  React sea publico no es una fuga: no contiene secretos, porque los secretos viven en la API.
- **Zona privada** — la `API de prestamos` en el **3000**, alcanzable **solo desde el edge**.
  Nadie desde internet abre una conexion directa al 3000. Ese numero no se eligio hoy: es el
  mismo `EXPOSE 3000` del Dockerfile de la Clase 3, y esa coherencia es parte de la nota.
- **Zona de datos** — la `Base de datos de prestamos` en el 5432, **sin salida a internet** y
  alcanzable unicamente desde la zona privada. No tiene puerto publicado hacia afuera ni ruta
  de salida: ni entra ni sale.

**Las fronteras de confianza**, marcadas en tres flechas: la del cliente hacia el edge (ahi
empieza lo que yo controlo) y las dos de la API hacia el `Proveedor de identidad
institucional` y el `Correo transaccional SaaS` (ahi termina). Los dos sistemas externos se
dibujan **fuera de las tres zonas** a proposito: no los despliego yo, no puedo cambiar su
configuracion y no puedo garantizar su disponibilidad — que es exactamente el riesgo 1 de la
pregunta 15 del Corte 1.

**Nada de nombres de proveedor.** No hay VPC, ni zona de disponibilidad, ni nombre de
servicio de marca. Las zonas son conceptuales y el diagrama tiene que servir igual en
cualquier proveedor, que es la posicion del curso desde el ADR-001: no se abren cuentas de
nube de pago.

**Lo que cambia respecto al C4 Containers.** Aparecen dos piezas que alli no existian —el
`Cliente / navegador` y el `Edge / balanceador`— porque son infraestructura, no contenedores
con responsabilidad de negocio. Ese detalle es justo lo que la pregunta 6 pide declarar.""",
                "como_calificar": [
                    "4 pts las **tres zonas presentes y rotuladas**: publica, privada y de "
                    "datos. Los rotulos pueden variar en las palabras, pero las tres tienen que "
                    "existir como frontera visible. Dos zonas valen la mitad.",
                    "4 pts **cada componente en la zona que le corresponde**. **Se pierden los "
                    "4 completos si la base de datos queda en la zona publica**, sin "
                    "prorrateo. Es la penalizacion mas dura del diagrama y hay que anunciarla "
                    "antes del taller: es el error que la pregunta busca detectar.",
                    "2 pts las **fronteras de confianza marcadas**: donde termina lo que el "
                    "estudiante controla y empieza lo que no. Se acepta como etiqueta en la "
                    "flecha, como nota o como estilo distinto, siempre que se pueda senalar.",
                    "2 pts **el puerto de cada componente**. Si falta el de una pieza se "
                    "prorratea; si no hay ningun puerto, es cero. Los puertos tienen que ser "
                    "creibles y **coherentes con el Dockerfile de la Clase 3**: si alla el "
                    "`EXPOSE` era 3000 y aqui aparece 8080 sin explicacion, comentelo.",
                    "2 pts que renderice sin error en la plataforma.",
                    "**Se descuenta por nombrar subredes o servicios de un proveedor "
                    "concreto** (VPC, nombres de servicios de marca, zonas de disponibilidad). "
                    "No es un capricho: el diagrama es conceptual y el curso no abre cuentas de "
                    "pago, asi que un diagrama atado a un proveedor no se puede ni verificar.",
                    "Los sistemas externos **fuera** de las tres zonas es lo correcto. Si el "
                    "estudiante los mete en la zona publica, no descuente de la ubicacion de "
                    "componentes: comente que lo que esta en las zonas es lo que el despliega.",
                ],
                "errores": [
                    "**La base de datos en la zona publica.** Es el error caro (4 pts) y "
                    "aparece todos los semestres, casi siempre por comodidad de dibujo: se "
                    "pone al lado del cliente porque cabe mejor. Repita en voz alta antes del "
                    "taller que la base no se alcanza desde internet nunca.",
                    "Zonas dibujadas pero sin componentes dentro, o componentes sueltos fuera "
                    "de toda zona. Cada pieza que usted despliega vive en exactamente una zona.",
                    "Nombres de proveedor: «VPC», «subnet-public-1a», nombres de servicios de "
                    "marca. Se descuenta y se explica: el diagrama tiene que sobrevivir a un "
                    "cambio de proveedor, que es lo que el ADR-001 dejo abierto.",
                    "Puertos inventados o repetidos: la API y la base en el mismo puerto, o el "
                    "443 en todo. Cada componente escucha en el suyo, y el de la API ya estaba "
                    "decidido desde el `EXPOSE` de la Clase 3.",
                    "Flechas sin direccion o bidireccionales por defecto. La direccion importa: "
                    "que la API llame a la base no significa que la base llame a la API, y esa "
                    "asimetria es la que justifica que la zona de datos no tenga salida.",
                    "Renombrar las piezas respecto al C4 Containers («backend», «servidor», "
                    "«bd»). No se descuenta aqui, se descuenta en la pregunta 6, que es "
                    "peor: alla vale 2.5 pts y ademas hay que listar los renombres.",
                    "Dibujar el diagrama como si fuera otro C4 Containers, con "
                    "`System_Boundary` y `Container(...)`. Este es un diagrama de despliegue: "
                    "la pregunta es **donde se ejecuta**, y por eso se modela con zonas y "
                    "puertos.",
                ],
            },
            {
                "n": 5,
                "titulo": "Tipo de almacenamiento de cada componente de BiblioLite",
                "tipo": "abierta",
                "puntos": 5.5,
                "tabla": {
                    "headers": ["Componente", "Tipo",
                                "Que caracteristica del dato lo exige"],
                    "rows": [
                        ["Base de datos de prestamos",
                         "**Relacional**",
                         "El dato se cruza: un prestamo une estudiante, ejemplar y titulo, y "
                         "la capacidad «saber que titulos se agotan cada semestre» es una "
                         "consulta que atraviesa las tres tablas. Sin relaciones habria que "
                         "resolver ese cruce a mano en la API."],
                        ["Volumen de datos del motor PostgreSQL",
                         "**Bloque**",
                         "Lo monta **un solo proceso** —el motor— y escribe en el a nivel de "
                         "bloque, incluido el registro de transacciones. Ningun otro proceso "
                         "puede escribir ese disco al mismo tiempo, y eso es exactamente lo "
                         "que caracteriza al almacenamiento de bloque."],
                        ["Aplicacion web (bundle de React)",
                         "**Objeto**",
                         "Son archivos completos que se recuperan **enteros y por su nombre** "
                         "(`index.html`, `app.js`), nunca por su contenido. Nadie consulta "
                         "«dame la linea 40 del bundle»: se sirve el archivo tal cual desde "
                         "el edge."],
                        ["Respaldo diario de la base",
                         "**Objeto**",
                         "El `dump` es un archivo inmutable que se escribe una vez, se guarda "
                         "por fecha y se recupera completo el dia que haga falta. No se "
                         "consulta por dentro ni se modifica: se reemplaza."],
                    ],
                },
                "respuesta": """**Lo que BiblioLite NO necesita, dicho a proposito**

BiblioLite **no necesita almacenamiento de objetos para datos del dominio**, y esa es una
respuesta completa, no una omision. El bloque «fuera de alcance» de la ficha de la Clase 1 lo
dice: el sistema **no digitaliza el contenido de los libros**. No hay PDF, ni portadas
subidas por el usuario, ni documentos adjuntos, ni fotos de perfil. Los dos usos de objeto que
si aparecen —el bundle estatico y los respaldos— son de infraestructura, no del dominio.

Si manana el alcance cambiara y se agregara «adjuntar la portada del titulo», ahi si entraria
un almacen de objetos del dominio, y el motivo estaria escrito: una imagen se guarda y se
recupera entera por su nombre, no se cruza con nada. Mientras el dato no exista, agregar el
almacen seria decorar el diagrama.

**Por que el volumen del motor va aparte de la base.** Es la fila que mas se olvida y la que
mas ensena: «relacional» describe **como se consulta** el dato, y «bloque» describe **como se
persiste** en el disco. Son dos capas, no dos opciones que compiten. La base de datos es
relacional **y** se apoya en un disco de bloque; decir solo lo primero deja la mitad de la
historia sin contar.""",
                "como_calificar": [
                    "3 pts la **clasificacion correcta de cada componente** del despliegue. Se "
                    "prorratea entre las filas. La base como relacional y el bundle como "
                    "objeto son las dos que tienen que estar bien; el volumen de bloque es la "
                    "que distingue una buena respuesta.",
                    "2.5 pts que **cada justificacion nombre la caracteristica del dato** —se "
                    "cruza con otros, lo monta un solo proceso, se recupera entero— **y no una "
                    "preferencia**. «Porque PostgreSQL es lo que se usa» o «porque es mas "
                    "rapido» no nombran ninguna caracteristica del dato: esa fila no suma en "
                    "este criterio aunque el tipo este bien.",
                    "**Suma completo quien declare que su dominio no necesita almacenamiento "
                    "de objetos y lo justifique.** Eso incluye justificarlo con el «fuera de "
                    "alcance» de su propia ficha, que es la forma mas solida.",
                    "**Se descuenta quien incluya objeto sin un dato que lo pida**: un almacen "
                    "de archivos en un dominio que no maneja archivos. Es la decision «porque "
                    "suena a cloud» que la pregunta esta diseñada para detectar.",
                    "Que el estudiante distinga el **volumen de bloque** del motor de la base "
                    "relacional que corre encima no es obligatorio para la nota completa, pero "
                    "es el detalle que merece comentario positivo: significa que separo la "
                    "forma de consultar de la forma de persistir.",
                    "La tabla tiene que cubrir **los componentes de su propio despliegue** de "
                    "la pregunta 4. Un componente del diagrama que no aparece en la tabla se "
                    "descuenta de los 3 pts de clasificacion.",
                ],
                "errores": [
                    "Agregar un almacen de objetos «porque toda arquitectura cloud tiene "
                    "uno». Es el error que el enunciado nombra con todas sus letras. La "
                    "pregunta de corte: «¿que archivo de su dominio va ahi?». Si no hay "
                    "respuesta, no va.",
                    "Justificar por preferencia o por popularidad: «uso relacional porque es "
                    "lo que se, porque es gratis, porque lo vimos en Bases de Datos». La "
                    "pregunta es que caracteristica **del dato** lo exige.",
                    "Confundir objeto con bloque. La prueba mas simple: ¿se recupera el archivo "
                    "entero por su nombre (objeto) o lo monta un proceso como disco y escribe "
                    "dentro (bloque)?",
                    "Clasificar el codigo fuente o el repositorio como almacenamiento del "
                    "sistema. El repositorio no es un componente del despliegue: no se ejecuta "
                    "en ninguna de las tres zonas.",
                    "Dejar fuera de la tabla los respaldos. Son el almacenamiento que decide "
                    "si el proyecto sobrevive a un error, y ademas conectan con el RPO y el "
                    "RTO que Bases de Datos II trabaja en su Clase 4.",
                    "Decir «no necesito objeto» sin justificarlo. La declaracion suma completo "
                    "**con** el motivo; sin motivo se parece a un olvido y se califica como tal.",
                ],
            },
            {
                "n": 6,
                "titulo": "Correspondencia entre el C4 Containers y el Despliegue",
                "tipo": "abierta",
                "puntos": 5.5,
                "tabla": {
                    "headers": ["Componente en el C4 Containers",
                                "Componente en el Despliegue", "Zona"],
                    "rows": [
                        ["`Aplicacion web` (React)", "`Aplicacion web`", "Publica"],
                        ["`API de prestamos` (Node.js)", "`API de prestamos`", "Privada"],
                        ["`Base de datos de prestamos` (PostgreSQL)",
                         "`Base de datos de prestamos`", "Datos"],
                        ["`Proveedor de identidad institucional` (`System_Ext`)",
                         "`Proveedor de identidad institucional`",
                         "Externa — fuera de las tres zonas"],
                        ["`Correo transaccional SaaS` (`System_Ext`)",
                         "`Correo transaccional SaaS`",
                         "Externa — fuera de las tres zonas"],
                        ["— (no existe en el C4 Containers)", "`Edge / balanceador`",
                         "Publica"],
                        ["— (no existe en el C4 Containers)", "`Cliente / navegador`",
                         "Fuera: es el actor `Estudiante` o `Auxiliar de biblioteca`"],
                    ],
                },
                "respuesta": """**Por que los nombres tienen que coincidir**
Porque **no son dos sistemas: es el mismo sistema visto desde dos angulos**. El C4 Containers
responde «que piezas hay y de que se encarga cada una»; el Despliegue responde «donde se
ejecuta cada una y por que puerto se habla». Si una pieza se llama `API de prestamos` en uno y
`servidor-backend` en el otro, nadie que lea los dos documentos puede saber si son la misma
cosa o si el proyecto tiene dos backends. En la sustentacion de la Clase 15 eso se lee como
dos sistemas distintos, y en el checkpoint de la Clase 11 se marca como hallazgo de
coherencia. El nombre es el unico hilo que une los tres diagramas del curso: Context,
Container y Despliegue.

**Renombres aplicados: ninguno.** Lo declaro explicitamente, que es lo que pide el enunciado.
Los cinco nombres que venian del C4 Containers —y antes del Context de la Clase 1— se copiaron
letra por letra.

**Las dos filas sin par, que no son un error.** El `Edge / balanceador` y el
`Cliente / navegador` aparecen solo en el Despliegue, y esa asimetria tiene explicacion:

- El **edge** es infraestructura de ejecucion, no un contenedor con responsabilidad de
  negocio propia. En el nivel Container no existe porque no implementa ninguna capacidad de
  la ficha; en el Despliegue es imprescindible porque es lo que separa la zona publica de la
  privada.
- El **cliente / navegador** no es una pieza que yo despliegue: es el actor `Estudiante` o
  `Auxiliar de biblioteca` del Context, dibujado aqui porque el diagrama de despliegue tiene
  que mostrar de donde viene la primera peticion.

Declararlas es mejor que esconderlas: son las dos filas que demuestran que el estudiante
entendio para que sirve cada nivel, y no solo que copio nombres.""",
                "como_calificar": [
                    "2 pts la explicacion de por que los nombres deben coincidir, **en "
                    "terminos de que son el mismo sistema visto desde angulos distintos**. "
                    "«Para que se entienda mejor» o «por orden» valen la mitad: no dicen que es "
                    "el mismo sistema.",
                    "2.5 pts la tabla completa, **una fila por componente, con su zona**. Se "
                    "prorratea. **Se descuenta si la tabla deja fuera algun componente que si "
                    "aparece en alguno de los dos diagramas** — y eso incluye el edge y el "
                    "cliente, que solo estan en el despliegue.",
                    "1 pt **listar los renombres aplicados, o declarar explicitamente que no "
                    "hubo ninguno**. Dejar el tema en silencio es cero en este criterio, "
                    "aunque de hecho no haya renombres: la declaracion es el entregable.",
                    "Si hubo renombres, la respuesta completa dice **cual de los dos diagramas "
                    "se actualizo** para que queden iguales. No importa cual: importa que "
                    "quede uno solo de los dos nombres vivo.",
                    "Las filas «no existe en el C4 Containers» para el edge y el cliente, con "
                    "su explicacion, son la mejor version de esta respuesta. No se exige, pero "
                    "si el estudiante las omite y ademas no menciona el edge en ninguna parte, "
                    "descuente de los 2.5 pts de la tabla.",
                    "Esta pregunta se califica con los dos diagramas al lado y en dos minutos. "
                    "Si un nombre no coincide, verifique tambien la pregunta 4: a veces el "
                    "diagrama esta bien y la tabla mal transcrita.",
                ],
                "errores": [
                    "Tabla con tres filas que ignora los sistemas externos y el edge. Es la "
                    "omision mas comun y la que descuenta: el enunciado dice «algun componente "
                    "que si aparece en **alguno de los dos** diagramas».",
                    "Explicar la coincidencia de nombres como una cuestion de prolijidad. La "
                    "razon es de fondo: sin el nombre compartido no hay forma de saber que los "
                    "diagramas describen un solo sistema.",
                    "Renombrar en el despliegue «porque en produccion se llama distinto» y no "
                    "declararlo. Si de verdad se llama distinto, se declara el renombre y se "
                    "elige un nombre unico. Dos nombres vivos es la peor de las tres opciones.",
                    "No decir nada sobre renombres. Cuesta el punto completo aunque no haya "
                    "habido ninguno. La frase «no aplique ningun renombre» es literalmente la "
                    "respuesta que vale.",
                    "Poner el edge como si fuera un contenedor del C4 y volver atras a "
                    "agregarlo alli. No hace falta y desordena el nivel Container: el edge no "
                    "tiene responsabilidad de negocio. Basta declararlo en esta tabla.",
                    "Zonas que no coinciden con el diagrama de la pregunta 4: la tabla dice "
                    "que la base esta en la zona de datos y el diagrama la dibujo en la "
                    "publica. Cuando pasa, la penalizacion de los 4 pts de la 4 sigue en pie: "
                    "se califica el diagrama, no la intencion.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Cuantas zonas exactamente? ¿Puedo tener cuatro?",
             "Las tres exigidas son publica, privada y de datos. Puede agregar una cuarta si su "
             "arquitectura la pide y la justifica, pero no suma puntos: lo que se califica es "
             "que las tres esten y que cada pieza este en la correcta."),
            ("¿La aplicacion web va en la zona publica o en la privada?",
             "Publica: son archivos estaticos que el navegador descarga. Que sea publica no es "
             "una fuga, porque no contiene secretos. Si su bundle tiene una clave dentro, ese "
             "es un hallazgo de la Clase 6, no un problema de zonas."),
            ("¿Por que la base de datos no puede estar en la zona publica?",
             "Porque un puerto de base de datos abierto a internet es escaneado en minutos, y "
             "porque no hay ninguna razon para que lo este: el unico que le habla es la API, "
             "que vive en la zona privada. Son 4 puntos completos y es el error que la pregunta "
             "busca."),
            ("¿Tengo que usar los mismos puertos del Dockerfile de la Clase 3?",
             "Si. El `EXPOSE` de alla y el puerto de la API de aqui son el mismo numero. Si los "
             "cambio en el laboratorio y no corrigio el Dockerfile, este es el momento de "
             "arreglar los dos."),
            ("¿Puedo nombrar el proveedor de nube que voy a usar?",
             "No en el diagrama: se descuenta. El diagrama es conceptual y tiene que servir "
             "igual en cualquier proveedor, que es justo lo que el ADR-001 dejo abierto. El "
             "proveedor concreto se menciona en el ADR, no en las zonas."),
            ("Mi dominio no maneja archivos, ¿pierdo puntos por no tener objeto?",
             "Al contrario: declararlo y justificarlo suma completo. Lo que se descuenta es "
             "incluir un almacen de objetos sin un dato que lo pida."),
            ("En el despliegue tengo piezas que no estan en el C4 Containers, ¿esta mal?",
             "No, si las declara. El edge y el cliente son los dos casos normales: son "
             "infraestructura y actor, no contenedores con responsabilidad de negocio. "
             "Declararlas es parte de la respuesta de la pregunta 6."),
            ("¿Que hago si me di cuenta de que renombre algo hace dos clases?",
             "Elija un nombre, actualice el diagrama que quedo desactualizado, y **liste el "
             "renombre** en la pregunta 6. Eso vale el punto completo. Lo que no vale es dejar "
             "los dos nombres vivos y esperar que nadie lo note en la Clase 11."),
        ],
        "cierre": (
            "Con el diagrama de despliegue quedan los tres angulos completos: que hace el "
            "sistema (Context), de que piezas esta hecho (Container) y donde se ejecutan "
            "(Despliegue). Deje dicho para donde va cada cosa: los puertos de hoy son los que "
            "el pipeline de la Clase 8 va a consultar en el endpoint de salud, las zonas son "
            "donde se ubican los controles de la Clase 6, el conteo de saltos de la Clase 4 se "
            "puede rehacer ahora con los puertos reales, y la tabla de correspondencia de la "
            "pregunta 6 es literalmente una de las cinco verificaciones del checkpoint de la "
            "Clase 11. Si alguien todavia tiene nombres distintos entre diagramas, hoy es el "
            "ultimo dia barato para arreglarlo."
        ),
    },
    8: {
        "titulo": ("Solucion — Actividad del Corte 2, preguntas 7 a 10 "
                   "(pipeline de CI, condicion de fallo, frontera CI/CD y senales)"),
        "resumen": (
            "Las cuatro preguntas de la Clase 8 sobre **BiblioLite**, con el pipeline escrito "
            "completo y ejecutable. Las tres primeras son **la misma pregunta con tres "
            "profundidades**: el YAML (7), que hace de verdad (8) y hasta donde llega (9); y "
            "las tres se derrumban si el pipeline no puede fallar nunca. La pregunta 7 tiene "
            "**cero automatico si aparece un secreto en claro**, y es la unica penalizacion "
            "total de la actividad."
        ),
        "total": 25.0,
        "nota_actividad": (
            "Estas 4 preguntas valen **25 de los 100 puntos** de la actividad del Corte 2 "
            "(Clases 6, 7, 8 y 10). Se califican en orden y comparandolas: un `ci.yml` correcto "
            "con una explicacion en la 8 que no corresponde a ese archivo es la senal mas "
            "clara de que el YAML se copio de internet."
        ),
        "preguntas": [
            {
                "n": 7,
                "titulo": "El workflow de integracion continua de BiblioLite",
                "tipo": "abierta",
                "puntos": 10.0,
                "respuesta": """```yaml
name: CI BiblioLite API

# 1. DISPARADORES
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:        # para poder correrlo a mano el dia de la sustentacion

jobs:
  construir-probar:
    # 2. ENTORNO DE EJECUCION
    runs-on: ubuntu-latest

    steps:
      - name: Traer el codigo
        uses: actions/checkout@v4

      - name: Preparar Node 20
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      # 3a. CONSTRUCCION
      - name: Instalar dependencias exactas
        run: npm ci

      - name: Construir la imagen del servicio
        run: docker build -t bibliolite-api:0.1.0 .

      # 3b. PRUEBA
      - name: Pruebas de las reglas de prestamo
        run: npm test

      - name: Verificar que la imagen no lleva secretos
        run: |
          if docker history --no-trunc bibliolite-api:0.1.0 | grep -q '[.]env'; then
            echo "La imagen menciona .env: se detiene el pipeline"
            exit 1
          fi

      - name: Levantar el contenedor y verificar el endpoint de salud
        env:
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
          CORREO_API_KEY: ${{ secrets.CORREO_API_KEY }}
        run: |
          docker run -d --name api -p 8080:3000 \\
            -e DATABASE_URL="$DATABASE_URL" \\
            -e CORREO_API_KEY="$CORREO_API_KEY" \\
            bibliolite-api:0.1.0
          for i in $(seq 1 15); do
            if curl -fsS http://localhost:8080/health | grep -q '"estado":"ok"'; then
              echo "Endpoint de salud OK"
              exit 0
            fi
            sleep 2
          done
          echo "El endpoint /health no respondio 200 con estado ok"
          docker logs api
          exit 1

      # 3c. DESPLIEGUE SIMULADO
      - name: Despliegue SIMULADO (no despliega a ningun servidor real)
        run: |
          echo "Imagen bibliolite-api:0.1.0 construida verificada y lista para desplegar."
          echo "En este curso el despliegue se SIMULA: no se abren cuentas de nube de pago."
```

**Coherencia con el Corte 1.** La imagen es `bibliolite-api:0.1.0` y el puerto del contenedor
es el **3000**, exactamente los del Dockerfile de la Clase 3 y del diagrama de despliegue de la
Clase 7. El `-p 8080:3000` publica el 3000 del contenedor en el 8080 del ejecutor, que es donde
el `curl` entra.

**Secretos.** Los dos que el servicio necesita se referencian con `${{ secrets.NOMBRE }}` desde
la configuracion del repositorio, se pasan al paso como variables de entorno y de ahi al
contenedor con `-e`. **Ninguno aparece escrito en el YAML**, y el paso «Verificar que la imagen
no lleva secretos» convierte en automatica la politica que la pregunta 3 dejo escrita: si
manana alguien hace un `COPY . .`, el pipeline se pone rojo antes de que la imagen salga del
equipo.

**Por que el despliegue dice SIMULADO en el nombre.** Porque no despliega. Rotularlo asi no
resta: evita prometer lo que el pipeline no hace, que es exactamente lo que la pregunta 9
pregunta despues.""",
                "como_calificar": [
                    "2 pts los **disparadores declarados**. Se espera al menos `push` a la rama "
                    "principal; `pull_request` y `workflow_dispatch` son deseables y no "
                    "obligatorios. Un `on:` vacio o ausente es cero en este criterio.",
                    "1.5 pts el **entorno de ejecucion** (`runs-on`). Basta con "
                    "`ubuntu-latest`; no se exige justificarlo.",
                    "4 pts los **tres pasos presentes y en orden**: construccion, prueba, "
                    "despliegue simulado. Aproximadamente 1.3 pts cada uno. Si el orden esta "
                    "invertido (prueba antes de construir) se descuenta 1 pt: es una senal de "
                    "que el YAML no se ejecuto nunca.",
                    "1.5 pts que el **despliegue este rotulado como simulado** y no prometa un "
                    "despliegue real. El rotulo va en el nombre del paso, no solo en un "
                    "comentario.",
                    "1 pt **coherencia con el Dockerfile del Corte 1**: misma imagen, mismo "
                    "puerto. Se verifica abriendo la pregunta 8 del Corte 1 al lado.",
                    "**CERO EN TODA LA PREGUNTA si aparece un secreto escrito en claro en el "
                    "YAML.** Es la unica penalizacion total del corte y hay que anunciarla al "
                    "abrir el taller. Un valor de ejemplo evidente "
                    "(`DATABASE_URL: postgres://usuario:CAMBIAR@...`) no cuenta como secreto "
                    "en claro, pero comentelo: es una costumbre que termina en filtracion.",
                    "Que el pipeline incluya una verificacion automatica de la politica de "
                    "secretos de la pregunta 3 no es obligatorio y merece comentario positivo: "
                    "es el paso de una politica escrita a una politica que se cumple sola.",
                ],
                "errores": [
                    "Escribir la cadena de conexion o la clave del correo en el YAML «para "
                    "probar». Cero en la pregunta, 10 puntos. Y el log de la CI es publico si "
                    "el repositorio lo es: ademas de perder la nota, hay que rotar la clave.",
                    "Un `ci.yml` con tres pasos que solo hacen `echo`. Formalmente cumple la "
                    "estructura y se derrumba en la pregunta 8, donde la condicion de fallo es "
                    "cero. Califique las dos juntas para que la nota sea coherente.",
                    "Copiar un workflow de internet con acciones que no aplican: despliegues a "
                    "proveedores de nube, publicacion en registros de paquetes, matrices de "
                    "cinco versiones de Node. Se detecta porque menciona pasos que el proyecto "
                    "no tiene.",
                    "Imagen o puerto distintos de los del Corte 1, casi siempre `8080:8080` "
                    "copiado del ejemplo de la diapositiva. Cuesta el punto de coherencia y "
                    "hace que el paso del `curl` no pueda funcionar.",
                    "`npm install` en vez de `npm ci` en el pipeline. Aqui si vale corregirlo "
                    "con firmeza: en CI el objetivo es reproducir, y `ci` es el que respeta el "
                    "`package-lock.json`.",
                    "Olvidar el `actions/checkout`. El pipeline arranca sin codigo y falla en "
                    "el primer paso con un error que no dice nada. Es el olvido mas comun de "
                    "quien escribe el YAML de memoria.",
                    "Un paso llamado `deploy` sin la palabra simulado. Cuesta 1.5 pts aqui y "
                    "medio criterio en la pregunta 9, donde afirmar haber construido CD "
                    "descuenta la mitad.",
                ],
            },
            {
                "n": 8,
                "titulo": "Que hace realmente el paso de construccion y prueba",
                "tipo": "abierta",
                "puntos": 5.0,
                "respuesta": """**1. Que se instala y se construye**
`npm ci` instala las dependencias **exactas** del `package-lock.json` — no las compatibles, las
exactas — en el ejecutor limpio de GitHub. Despues `docker build` construye la imagen
`bibliolite-api:0.1.0` con el mismo Dockerfile del Corte 1, asi que el pipeline valida tambien
que el Dockerfile siga siendo valido, no solo que el codigo compile. No hay compilacion en el
sentido estricto porque es JavaScript, y conviene decirlo asi en vez de inventar un paso de
compilacion que no existe.

**2. Que se ejecuta en la prueba y que comprueba exactamente**
Tres cosas, en orden de menos a mas costoso:

- `npm test` corre las pruebas de las reglas de prestamo. La que importa: **no se puede
  reservar el ultimo ejemplar disponible si ya tiene una reserva vigente**. Es la regla que
  justifica que BiblioLite exista, asi que es la que se prueba.
- La verificacion de que `docker history` **no menciona `.env`**: comprueba la politica de
  secretos de la pregunta 3 sobre la imagen que se acaba de construir.
- El contenedor se levanta de verdad y se consulta `GET /health` esperando `200` con
  `"estado":"ok"`: comprueba que la imagen **arranca**, que el proceso escucha en el 3000 y que
  el contrato de salud de la Clase 3 se sigue cumpliendo.

**3. Con que condicion el pipeline DEBE fallar**
Cuatro condiciones, y todas se pueden provocar a proposito:

| Si introduzco... | el pipeline lo detecta en... |
|---|---|
| una regla que permite reservar un ejemplar ya reservado | `npm test`, la prueba falla |
| un `COPY . .` que arrastra el `.env` | la verificacion de `docker history` |
| un puerto distinto en el `EXPOSE` o en el `CMD` | el `curl` a `/health`, que agota los 30 s |
| una dependencia que no esta en el `package-lock.json` | `npm ci`, que se niega a instalarla |

**La prueba de que no es decoracion verde:** si cambio la comparacion de la regla de reserva de
`>=` a `>`, el `npm test` se pone rojo y el pipeline se detiene antes del despliegue simulado.
Ese es el error concreto que introduciria para demostrar que el pipeline sirve, y es el que
conviene provocar una vez a proposito para ver el check rojo con los propios ojos.""",
                # La pregunta se califica contra un run que el docente no tiene por que
                # ejecutar: aqui van los dos logs —el verde y el rojo— en el campo `salida`,
                # que es el que el renderizador emite en cerca para comparar contra lo que
                # el estudiante describe. La prosa de criterio va en `nota_salida`, fuera.
                "salida": """== RUN VERDE - el pipeline de arriba cuando pasa ==

CI BiblioLite API  #7  [OK] construir-probar (ubuntu-latest)        1m 48s
  [OK] Traer el codigo                                                 3s
  [OK] Preparar Node 20                                                7s
  [OK] Instalar dependencias exactas       npm ci                     22s
  [OK] Construir la imagen del servicio    docker build ... 0.1.0     41s
  [OK] Pruebas de las reglas de prestamo   npm test                    6s
         3 passing  (reserva del ultimo ejemplar ya reservado: rechazada con 409)
  [OK] Verificar que la imagen no lleva secretos                       4s
  [OK] Levantar el contenedor y verificar el endpoint de salud        14s
         Endpoint de salud OK
  [OK] Despliegue SIMULADO (no despliega a ningun servidor real)       2s
         Imagen bibliolite-api:0.1.0 construida verificada y lista para desplegar.

== RUN ROJO - el mismo pipeline con la regla de reserva rota (>= cambiado por >) ==

CI BiblioLite API  #8  [FALLA] construir-probar (ubuntu-latest)        52s
  [OK]    Traer el codigo / Preparar Node 20 / Instalar dependencias exactas
  [OK]    Construir la imagen del servicio
  [FALLA] Pruebas de las reglas de prestamo   npm test                  5s
            1 failing - reserva del ultimo ejemplar ya reservado:
                        se esperaba 409 y devolvio 201
            Error: Process completed with exit code 1
  [-]     Verificar que la imagen no lleva secretos                omitido
  [-]     Levantar el contenedor y verificar el endpoint de salud  omitido
  [-]     Despliegue SIMULADO                                     omitido""",
                "nota_salida": """Los segundos varian con el ejecutor y no significan nada: lo que
se compara son **los nombres de los pasos, su orden y donde se detiene**. Si el estudiante
describe un run que no se parece a ninguno de los dos, la diferencia esta en su `ci.yml` y ahi
es donde hay que mirar. Los tres `omitido` del run rojo son el argumento entero de la pregunta:
**el pipeline no publica un artefacto que no paso las pruebas.** Un run que se pone verde con la
regla rota es la decoracion verde que este criterio califica con cero.""",
                "como_calificar": [
                    "1.5 pts **que se compila o instala**, dicho sobre su propio archivo. Si el "
                    "proyecto es JavaScript y no hay compilacion, decirlo explicitamente es la "
                    "respuesta correcta y suma completo: inventar un paso de compilacion es "
                    "peor.",
                    "1.5 pts **que se ejecuta en la prueba y que comprueba**. Las dos mitades: "
                    "el comando **y** la afirmacion que verifica. «Corre `npm test`» sin decir "
                    "que comprueba vale la mitad.",
                    "2 pts la **condicion de fallo expresada como algo que el pipeline "
                    "detectaria**. La forma que vale es «si introduzco X, falla en Y». Basta "
                    "una condicion bien formada; dos o mas es lo esperado en una buena "
                    "respuesta.",
                    "**CERO en la condicion de fallo si el pipeline no puede fallar nunca**: "
                    "solo `echo`, o pruebas que siempre pasan, o un `|| true` al final de cada "
                    "paso. Es el criterio central de la pregunta y no admite matices.",
                    "Un `continue-on-error: true` o un `|| true` escondido en el YAML de la "
                    "pregunta 7 anula esta pregunta aunque la prosa diga lo contrario. Vale la "
                    "pena buscarlo: es la forma sofisticada de la decoracion verde.",
                    "Que el estudiante nombre **el error concreto que introduciria** para ver "
                    "el check rojo es la mejor version de esta respuesta. Si lo hizo de verdad "
                    "y lo cuenta, comentelo: es la diferencia entre entender el CI y "
                    "describirlo.",
                ],
                "errores": [
                    "«El pipeline falla si hay un error». Circular y vacio. La correccion es "
                    "una pregunta: «¿que error, exactamente, y en que paso lo veria?».",
                    "Explicar un `ci.yml` que no es el suyo. Se detecta comparando: la prosa "
                    "menciona pruebas de integracion y el YAML solo tiene un `echo`. Cuando "
                    "pasa, califique sobre el YAML entregado y comentelo sin acusar.",
                    "Confundir «no hay compilacion» con «no hay construccion». La construccion "
                    "existe: es el `npm ci` y el `docker build`. Lo que no existe en JavaScript "
                    "es un paso de compilacion a binario.",
                    "Pruebas que solo verifican que el archivo existe o que la funcion devuelve "
                    "algo. No comprueban ninguna regla del dominio y por eso no pueden fallar "
                    "por un error de negocio. Pida una prueba sobre la regla que justifica el "
                    "sistema.",
                    "Poner `|| true` o `continue-on-error` para que el pipeline «se vea verde». "
                    "Es exactamente lo contrario del objetivo: un check que nunca falla no "
                    "informa nada y da una falsa seguridad que en un proyecto real es peor que "
                    "no tener CI.",
                    "Decir que el pipeline fallaria si el servidor de produccion esta caido. No "
                    "hay servidor de produccion: el despliegue se simula. Confundir eso indica "
                    "que la pregunta 9 tambien va a fallar.",
                ],
            },
            {
                "n": 9,
                "titulo": "Hasta donde llega el pipeline: CI, CD y lo realista aqui",
                "tipo": "abierta",
                "puntos": 4.0,
                "respuesta": """**1. Que valida la integracion continua (CI) y cuando actua**
La CI valida que **el codigo de todos integrado sigue funcionando**, y actua en el momento en
que el codigo entra al repositorio compartido: en cada `push` a `main` y en cada solicitud de
cambios. Su pregunta es «¿esto rompe algo?», y su respuesta es un check verde o rojo en
minutos, no en la semana de la entrega.

**2. Que hace la entrega o el despliegue continuo (CD) y en que se diferencia**
La CD toma el artefacto que la CI verifico y lo **lleva a un entorno**. La sigla es ambigua a
proposito y conviene separar las dos lecturas:

- **Entrega continua**: el artefacto queda siempre listo para desplegar y el despliegue lo
  dispara una persona con un boton.
- **Despliegue continuo**: no hay boton; todo lo que pasa la CI llega automaticamente al
  entorno.

La diferencia con la CI es el objeto: **la CI valida, la CD entrega**. Una responde si el
codigo esta sano; la otra lo pone donde los usuarios lo alcanzan.

**3. Cual construi yo y hasta que punto exacto llega**
Construi **integracion continua**, no CD. Mi `ci.yml` llega hasta **«listo para desplegar»**:
instala dependencias exactas, construye la imagen `bibliolite-api:0.1.0`, corre las pruebas de
la regla de prestamo, verifica que la imagen no lleva secretos y comprueba que el contenedor
arranca y responde `200` en `/health`. El ultimo paso se llama «Despliegue SIMULADO» y lo unico
que hace es imprimir que la imagen quedo verificada. **No hay ningun servidor recibiendo esa
imagen**, y el nombre del paso lo dice para no prometerlo.

**4. Que me faltaria para CD de verdad, y por que el curso no lo pide**
Me faltarian cuatro cosas concretas: un **entorno destino** con su URL, un **registro de
imagenes** donde publicar `bibliolite-api:0.1.0`, **credenciales de despliegue** guardadas como
secretos del repositorio, y una **estrategia de reversion** para volver a la version anterior
cuando el despliegue salga mal —porque va a salir mal alguna vez—. Ademas, una verificacion
posterior al despliegue contra el `/health` del entorno real, no del contenedor local.

El curso no lo pide porque las cuatro exigen una **cuenta de nube de pago con tarjeta de
credito**, y la politica del curso —la misma que sostiene el ADR-001— es que todo se hace con
herramientas gratuitas o en el navegador. La consecuencia pedagogica es honesta: se aprende a
construir el pipeline y a saber donde termina, que es mas util que tener un `deploy` que nadie
puede verificar.""",
                "como_calificar": [
                    "1 pt la definicion de CI **atada a cuando actua**. «Integrar el codigo» "
                    "sin el momento vale la mitad: el «cuando» (al entrar el codigo al "
                    "repositorio) es lo que la distingue de cualquier otra cosa.",
                    "1 pt la de CD **y su diferencia**. Distinguir entrega de despliegue "
                    "continuo no es obligatorio, pero es la respuesta que demuestra que el "
                    "estudiante entendio por que la sigla es ambigua.",
                    "1 pt **ubicar correctamente su propio trabajo**, reconociendo que llega "
                    "hasta «listo para desplegar». Se espera que nombre el punto exacto donde "
                    "se detiene, no solo la etiqueta.",
                    "1 pt **lo que faltaria para CD real y por que el curso no lo exige**. Las "
                    "dos mitades: la lista de lo que falta (entorno, registro, credenciales, "
                    "reversion) y el motivo (no se abren cuentas de pago).",
                    "**Se descuenta la mitad del total si afirma haber construido CD.** No es "
                    "una trampa: el enunciado avisa que decirlo suma en vez de restar, y aun "
                    "asi cada semestre alguien escribe «ya tengo CD porque tengo un paso "
                    "deploy».",
                    "Reconocer que el despliegue es simulado **no resta nada** y hay que "
                    "decirlo en la retroalimentacion, porque el estudiante suele creer que "
                    "admitirlo lo perjudica. Saber donde termina lo que construyo es "
                    "precisamente lo que se califica.",
                ],
                "errores": [
                    "«Ya tengo CD porque el YAML tiene un paso deploy». Cuesta la mitad de la "
                    "pregunta. La frase para el tablero: el nombre del paso no despliega nada; "
                    "lo que despliega es que haya un servidor al otro lado.",
                    "Definir CI como «usar GitHub Actions». La herramienta no es la practica: "
                    "se puede tener Actions y no tener integracion continua, y se puede tener "
                    "integracion continua con otra herramienta.",
                    "Usar CI y CD como si fueran una sola palabra («el cicd»). La pregunta "
                    "existe porque la frontera importa; si el estudiante no la puede trazar, "
                    "tampoco puede decir hasta donde llega su trabajo.",
                    "Decir que falta «configurar el servidor» sin nombrar nada mas. Se espera "
                    "una lista de piezas concretas: entorno, registro de imagenes, "
                    "credenciales, reversion.",
                    "Justificar la ausencia de CD por falta de tiempo o de conocimiento. El "
                    "motivo real y suficiente es la politica del curso: no se abren cuentas de "
                    "nube de pago. Es mejor argumento y ademas es verdad.",
                    "Prometer en la sustentacion de la Clase 15 un despliegue automatico que no "
                    "existe. Es la afirmacion que un evaluador tumba en dos preguntas, y aqui "
                    "se esta entrenando justo lo contrario.",
                ],
            },
            {
                "n": 10,
                "titulo": "Metricas y registros de BiblioLite en produccion",
                "tipo": "abierta",
                "puntos": 6.0,
                "tabla": {
                    "headers": ["Senal", "Que se mide en BiblioLite", "Umbral u objetivo"],
                    "rows": [
                        ["**Latencia**",
                         "Tiempo de respuesta de `GET /titulos?disponible=true`, la consulta de "
                         "disponibilidad, que es la operacion mas usada del sistema.",
                         "p95 **menor a 400 ms**. Si el p95 pasa de **800 ms** durante 5 "
                         "minutos, se revisa el plan de la consulta antes de agregar "
                         "capacidad."],
                        ["**Trafico**",
                         "Reservas creadas por hora: respuestas `2xx` de "
                         "`POST /titulos/{isbn}/reservas`.",
                         "Base esperada **20/hora**, pico de **150/hora** en semana de "
                         "parciales. Por encima de **300/hora** se revisa capacidad, porque "
                         "es el doble del pico previsto."],
                        ["**Errores**",
                         "Proporcion de respuestas `5xx` sobre el total de peticiones. Aparte "
                         "y como error **de negocio**: proporcion de `409` sobre las reservas "
                         "intentadas.",
                         "`5xx` **por debajo de 0.5%** en ventanas de 5 minutos. Los `409` no "
                         "son fallas, pero si pasan del **5%** de los intentos hay que "
                         "revisar la interfaz: significa que muestra disponibilidad vencida."],
                        ["**Saturacion**",
                         "Conexiones activas del pool de PostgreSQL sobre el maximo "
                         "configurado (20). Es el recurso que se agota primero, antes que la "
                         "CPU o la memoria.",
                         "Alerta al **80%** (16 conexiones sostenidas 2 minutos). Al 100% las "
                         "peticiones no fallan: se encolan, y el sintoma aparece como latencia."],
                        ["**Registro** (no numerico)",
                         "Bitacora de auditoria: una fila por cambio de estado de un prestamo "
                         "con `quien`, `id_ejemplar`, `antes`, `despues` y `cuando`. Es el "
                         "control de la amenaza 5 de la pregunta 1.",
                         "Objetivo: **100%** de los cambios de fecha de devolucion con fila, "
                         "verificado por muestreo mensual. Retencion **1 ano**."],
                        ["**Registro** (no numerico)",
                         "Log de fallos de envio del `Correo transaccional SaaS`, con el motivo "
                         "que devolvio el proveedor y el `id_prestamo` afectado.",
                         "Objetivo **0 fallos en 24 h**. Con **mas de 3 en un dia** se revisa "
                         "la cuota del plan gratuito y las direcciones invalidas."],
                    ],
                },
                "respuesta": """**Por que estas seis y en este orden.** Las cuatro primeras son las senales doradas
aterrizadas: cada una responde una pregunta distinta que las otras no pueden responder. La
latencia dice si duele, el trafico dice si es por volumen, los errores dicen si se rompe, y la
saturacion dice **que recurso** se agota. Sin la cuarta, un pico de latencia no tiene
explicacion; con ella, la explicacion suele ser el pool.

**Las dos que son registro y no metrica.** Un numero dice **que** algo paso; un registro
permite reconstruir **por que**. La bitacora de auditoria existe para poder responder «¿quien
movio esa fecha?» tres semanas despues, y el log de fallos de correo para poder decirle a un
estudiante por que no recibio el aviso. Ninguna de las dos se puede graficar como una linea, y
las dos son las que salvan una revision.

**Nota sobre los umbrales.** Los numeros de la tercera columna son discutibles y estan puestos
para poder discutirlos: 400 ms sale del umbral de percepcion de «instantaneo» que la Clase 12
trabaja, 20 conexiones es el maximo por defecto de PostgreSQL, y el pico de 150 reservas/hora
sale de la aritmetica de servilleta —unos 900 estudiantes activos, cada uno con una reserva
cada dos semanas, concentradas en la semana de parciales—. Lo que no es discutible es que la
columna exista: sin umbral no se puede decidir cuando actuar, y una senal que no lleva a una
decision no se mira nunca.""",
                "como_calificar": [
                    "1 pt por senal bien formada **con su umbral**, hasta 4 senales. Las "
                    "senales 5 y 6 suman hasta **1 pt adicional entre las dos**: no se premia "
                    "listar mas, se premia que las adicionales aporten algo distinto.",
                    "1 pt que **al menos una sea un registro y no una metrica numerica**: algo "
                    "que se escribe para poder reconstruir que paso despues. Una metrica "
                    "disfrazada de registro («cantidad de errores en el log») no cuenta: sigue "
                    "siendo un numero.",
                    "**Una senal sin umbral no suma, aunque este bien elegida.** Es la regla "
                    "mas mecanica de la pregunta y la que mas se pierde: «medimos la latencia» "
                    "es cero en esa fila.",
                    "Se descuenta si las senales **no se refieren a operaciones del dominio "
                    "propio**. «Latencia de la API» es generico; «latencia de la consulta de "
                    "disponibilidad, que es la mas usada» esta aterrizado. La segunda columna "
                    "es la que se revisa para decidirlo.",
                    "Un umbral que sea claramente irreal (latencia menor a 1 ms, cero errores "
                    "siempre) se corrige pero **no se anula**: el criterio pide que el umbral "
                    "exista y sea discutible. Comente el numero y de el suyo como referencia.",
                    "Distinguir el error de plataforma (`5xx`) del error de negocio esperado "
                    "(`409`) no es obligatorio y es la mejor senal de madurez de esta "
                    "pregunta: significa que el estudiante no va a alertar por algo que "
                    "funciona como debe.",
                ],
                "errores": [
                    "Metricas sin umbral. Es el error numero uno y el enunciado lo dice con "
                    "todas sus letras. Anunciar antes del taller: «una fila sin tercera columna "
                    "vale cero, aunque la senal sea perfecta».",
                    "Copiar las cuatro senales doradas con su definicion de manual y sin "
                    "aterrizarlas: «latencia: cuanto tarda una peticion». ¿Cual peticion? La "
                    "segunda columna pide la operacion concreta del dominio.",
                    "Medir el uso de CPU como saturacion sin haber pensado que recurso se agota "
                    "primero. En un servicio como BiblioLite casi nunca es la CPU: son las "
                    "conexiones a la base. Vale preguntarlo en voz alta durante el taller.",
                    "Poner como registro «los logs de la aplicacion». Demasiado vago. Se pide "
                    "que diga que se escribe en cada linea y para responder que pregunta "
                    "futura.",
                    "Alertar por los `409`. Son el comportamiento correcto del sistema cuando "
                    "dos personas reservan a la vez; alertar por ellos entrena al equipo a "
                    "ignorar las alertas. Lo que se vigila es su **proporcion**, no su "
                    "existencia.",
                    "Seis metricas que son variantes de la misma («tiempo de respuesta», "
                    "«velocidad», «demora»). El limite de 6 no es una meta: cuatro senales "
                    "distintas valen mas que seis parecidas.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿El pipeline tiene que correr de verdad en GitHub?",
             "Si, y es gratis: el nivel gratuito da 2000 minutos al mes en repositorios "
             "privados e ilimitado en publicos. No se pide tarjeta en ningun momento. Un "
             "`ci.yml` que nunca se ejecuto se nota en la pregunta 8."),
            ("¿Que pongo si no tengo pruebas escritas?",
             "Escriba una, la de la regla que justifica su sistema. Con una prueba real que "
             "puede fallar, la pregunta 8 suma completo; con tres `echo` no suma nada. Media "
             "hora de trabajo vale 5 puntos."),
            ("¿Puedo poner el secreto en el YAML si el repositorio es privado?",
             "No. Cero en la pregunta 7, y por una razon de fondo: el log de la CI, los forks y "
             "cualquier colaborador futuro lo ven. La sintaxis de secrets del repositorio es "
             "exactamente igual de facil de escribir."),
            ("¿Por que el despliegue tiene que decir «simulado»?",
             "Porque no despliega. Rotularlo no resta: suma en la pregunta 9, donde se "
             "califica que sepa donde termina lo que construyo. Afirmar tener CD descuenta la "
             "mitad de esa pregunta."),
            ("¿Cuantas metricas exactamente, cuatro o seis?",
             "Cuatro bien formadas ya suman los 4 pts principales; la quinta y la sexta suman 1 "
             "pt entre las dos y solo si aportan algo distinto. Es mejor entregar cuatro "
             "aterrizadas que seis genericas."),
            ("¿Un registro cuenta como metrica?",
             "No, y por eso hay 1 pt aparte: al menos una senal debe ser un registro. La "
             "diferencia es la pregunta que responde: la metrica dice que paso, el registro "
             "permite reconstruir por que."),
            ("¿De donde saco los umbrales si no tengo usuarios?",
             "De la aritmetica de servilleta y de los umbrales de percepcion, que es lo que la "
             "Clase 12 formaliza. El umbral puede ser discutible; lo que no puede es faltar."),
            ("¿Y si mi pipeline falla y no lo puedo arreglar antes de la entrega?",
             "Entregue el `ci.yml` y explique en la pregunta 8 en que paso falla y por que. Un "
             "pipeline rojo con diagnostico correcto vale mas que uno verde que no valida nada, "
             "y es lo que la rubrica premia."),
        ],
        "cierre": (
            "Hoy la politica de secretos de la Clase 6 dejo de ser un documento y se volvio un "
            "paso que se pone rojo solo, y el contrato de salud de la Clase 3 dejo de ser una "
            "promesa y se volvio una verificacion automatica. Deje dicho el enlace hacia "
            "adelante: los minutos de CI son un **driver de costo** de la tabla de la Clase 10, "
            "el cache del pipeline es una de las **acciones de sostenibilidad** de esa misma "
            "clase, los umbrales de latencia de hoy son los que la Clase 12 va a medir con "
            "percentiles, y las senales de saturacion son las que la Clase 13 usa para decidir "
            "la metrica de autoescalado. Y provoque una vez el check rojo delante del grupo: es "
            "el minuto que convierte el CI de decoracion en herramienta."
        ),
    },
    10: {
        "titulo": ("Solucion — Actividad del Corte 2, preguntas 11 y 12 "
                   "(tabla de costos cualitativa y sostenibilidad verificable)"),
        "resumen": (
            "Las dos ultimas preguntas del Corte 2 sobre **BiblioLite**, y las dos con la misma "
            "trampa: se pueden responder con palabras que suenan bien y no dicen nada. La "
            "pregunta 11 la corta con dos reglas mecanicas —**driver contable** y **al menos un "
            "Alto y un Bajo**— y la 12 con una sola: **si no se puede comprobar mirando un "
            "artefacto, vale cero**. Con esas tres reglas, las dos preguntas se califican en "
            "diez minutos."
        ),
        "total": 25.0,
        "nota_actividad": (
            "Estas 2 preguntas cierran los **100 puntos** de la actividad del Corte 2 (Clases "
            "6, 7, 8 y 10). La 11 vale 16.25 puntos, mas que cualquier otra pregunta del corte: "
            "es la que hay que atender primero en el taller. La tabla se construye **sobre el "
            "diagrama de despliegue de la Clase 7**, componente por componente, y quien no lo "
            "tenga a la vista va a dejar filas fuera."
        ),
        "preguntas": [
            {
                "n": 11,
                "titulo": "Tabla de costos de BiblioLite",
                "tipo": "abierta",
                "puntos": 16.25,
                "tabla": {
                    "headers": ["Componente", "Driver de costo", "Nivel B/M/A",
                                "Apalancamiento"],
                    "rows": [
                        ["`API de prestamos`",
                         "**Horas de instancia encendida**: 24 x 30 = **720 h/mes** aunque la "
                         "biblioteca este cerrada de noche. El costo no depende de las "
                         "reservas, depende del reloj.",
                         "**A**",
                         "Escalar a cero fuera del horario de biblioteca (6:00 a 22:00): de "
                         "720 h a **480 h/mes**, un 33% menos. **Comprobable** en la politica "
                         "de escalado y en el conteo de horas facturables."],
                        ["`Base de datos de prestamos`",
                         "**Horas encendida** (no se puede apagar sin perder el servicio) "
                         "**mas GB almacenados**, que solo crecen: un prestamo cerrado nunca "
                         "se borra.",
                         "**A**",
                         "Politica de retencion: los prestamos cerrados con mas de 2 anos se "
                         "mueven a un archivo en almacenamiento de objetos y se borran de la "
                         "tabla caliente. Y resolver la lentitud con **indices** antes que con "
                         "mas CPU. **Comprobable** en el tamano de la tabla mes a mes."],
                        ["Almacenamiento de objetos "
                         "(bundle de la `Aplicacion web` + respaldos)",
                         "**GB almacenados**: el bundle pesa unos 2 MB y cada `dump` diario "
                         "unos 40 MB comprimidos. Mas **GB de transferencia de salida** cada "
                         "vez que alguien descarga el bundle.",
                         "**B**",
                         "Retencion de 30 respaldos diarios y 6 mensuales en vez de guardarlos "
                         "todos, y comprimir el `dump`. **Comprobable** en la politica de "
                         "retencion escrita y en el listado del bucket."],
                        ["Integracion continua (GitHub Actions)",
                         "**Minutos de CI por mes**: cada corrida del `ci.yml` de la Clase 8 "
                         "consume entre 3 y 5 minutos, y se dispara en cada `push` a `main` y "
                         "en cada solicitud de cambios.",
                         "**M**",
                         "Cache de `npm` y de capas de Docker (el `cache: 'npm'` ya esta en el "
                         "YAML), y disparar el pipeline solo en `main` y en solicitudes de "
                         "cambios, no en cada rama. **Comprobable** en el bloque `on:` del "
                         "`ci.yml` y en la duracion de dos corridas consecutivas."],
                        ["`Edge / balanceador`",
                         "**GB de transferencia de salida**: todo lo que sale hacia el "
                         "navegador pasa por aqui, y la salida se paga; la entrada casi "
                         "nunca.",
                         "**M**",
                         "Cachear el bundle con `Cache-Control` de un ano usando el hash en el "
                         "nombre del archivo, y comprimir con gzip o brotli. **Comprobable** "
                         "en los encabezados de respuesta: un `curl -I` los muestra."],
                    ],
                },
                "respuesta": """**Por que dos Altos y un Bajo, y no todo Medio.** La API y la base son Alto por el mismo
motivo y vale decirlo en voz alta: **su costo no depende del uso, depende del tiempo**. Se
pagan encendidas aunque nadie reserve un libro a las tres de la manana. El almacenamiento de
objetos es Bajo porque BiblioLite no digitaliza contenidos —lo dice el «fuera de alcance» de la
ficha de la Clase 1— y por eso guarda megabytes, no terabytes. CI y edge quedan en Medio porque
crecen con la actividad, no con el reloj, y la actividad de un proyecto de curso es pequena.

La escala es **ordinal**: afirma que la API cuesta mas que el edge, **no cuantas veces mas**.
Ese matiz es la razon de que la pregunta prohiba precios: con B/M/A se puede ordenar
honestamente sin inventar una factura, y ordenar es lo que permite decidir donde apalancar
primero.

**Sin precios en dolares, a proposito.** No hay una sola cifra de moneda en la tabla. Cualquier
precio que pusiera seria inventado: no tengo cuenta de nube de pago —eso es la politica del
curso desde el ADR-001— y los precios cambian por region y por nivel. Lo que si es verificable
es la aritmetica de las **720 horas**, que sale del calendario y no de una lista de precios.

**El componente que mas ensena.** La fila de la base de datos es la unica cuyo driver crece
solo, sin que nadie haga nada: cada prestamo cerrado que se acumula suma GB para siempre. Es la
fila donde el apalancamiento tiene que ser una politica escrita (retencion) y no una accion
puntual, y es la que conecta con la Clase 13, donde se vera que esa tabla es tambien la que no
escala.""",
                "como_calificar": [
                    "4 pts **una fila por cada componente del despliegue, sin dejar ninguno "
                    "fuera**. Se compara con el diagrama de la Clase 7 y se prorratea. Los "
                    "sistemas externos (identidad, correo) pueden omitirse porque no los "
                    "factura el estudiante, pero si los incluye con su driver, mejor.",
                    "5 pts los **drivers**: cada uno tiene que ser una **variable contable** —"
                    "horas encendidas, GB de salida, GB almacenados, minutos de CI— y **no «el "
                    "uso»** ni «la cantidad de usuarios». La prueba: ¿se puede poner un numero "
                    "al final del mes? Si no, no es un driver.",
                    "3.25 pts los niveles, **con al menos un Alto y un Bajo justificados**. "
                    "**Si todo es Medio, este criterio vale cero**, sin prorrateo: es la "
                    "respuesta que la pregunta busca descartar.",
                    "4 pts los **apalancamientos, uno por fila, concretos y comprobables**. "
                    "«Optimizar», «reducir costos» o «usar mejor los recursos» no suman. La "
                    "forma que vale: una accion y donde se ve que se aplico.",
                    "**Se descuenta fuerte por inventar precios en dolares** o por presentar "
                    "una factura de un proveedor. La escala es cualitativa y el motivo es "
                    "honestidad: el estudiante no tiene cuenta de pago, asi que cualquier cifra "
                    "seria adivinada.",
                    "Que el nivel Alto se justifique con «el costo depende del tiempo, no del "
                    "uso» es la mejor version de esta respuesta. Si aparece, comentelo: es la "
                    "idea central del tema y la que hace util toda la tabla.",
                    "Un driver aritmeticamente verificable (las 720 horas del mes, los 5 "
                    "minutos por corrida) vale mas que uno correcto pero abstracto. No es un "
                    "criterio aparte: es lo que distingue el 5 de 5 del 3 de 5 en los drivers.",
                ],
                "errores": [
                    "Todo en Medio. Es la respuesta que evita pensar y el criterio de niveles "
                    "queda en cero, 3.25 puntos. Anunciarlo antes del taller: «necesito al "
                    "menos un Alto y un Bajo, y necesito el motivo».",
                    "Inventar precios: «la base cuesta 25 dolares al mes». Se descuenta fuerte "
                    "y ademas es falso, porque nadie en el curso tiene esa factura. La escala "
                    "cualitativa existe justamente para poder responder con honestidad.",
                    "«El uso» como driver. No es contable. La pregunta de correccion es "
                    "directa: «¿el uso de que, medido en que unidad, al final del mes?».",
                    "Dejar fuera la integracion continua o el edge porque «no cuestan». Los "
                    "minutos de CI y los GB de salida son los dos costos que mas sorprenden a "
                    "un equipo real. El enunciado los nombra explicitamente como componentes de "
                    "la tabla.",
                    "Incluir una fila de almacenamiento de objetos del dominio cuando el "
                    "dominio no maneja archivos. Es el mismo error de la pregunta 5 de la Clase "
                    "7: agregar la pieza porque suena a cloud.",
                    "Apalancamientos que son deseos: «reducir el consumo», «ser mas "
                    "eficientes». Sin una accion y sin donde se comprueba, la fila no suma. "
                    "Anticipa que la pregunta 12 tambien va a fallar.",
                    "Confundir el driver con el apalancamiento: poner «cachear» en la columna "
                    "del driver. El driver es lo que **hace crecer** la factura; el "
                    "apalancamiento es lo que la **baja**.",
                ],
            },
            {
                "n": 12,
                "titulo": "Tres acciones de sostenibilidad tecnica verificables",
                "tipo": "abierta",
                "puntos": 8.75,
                "tabla": {
                    "headers": ["Accion", "En que artefacto se comprueba",
                                "Como se comprueba"],
                    "rows": [
                        ["**1.** Imagen base ligera y sin dependencias de desarrollo: "
                         "`node:20-alpine` con etiqueta fija y `npm ci --omit=dev`.",
                         "El `Dockerfile` de la Clase 3: su **primera linea** y su instruccion "
                         "`RUN`.",
                         "`docker images` muestra **142 MB** en vez de los ~1.1 GB de "
                         "`node:20` completo. Cualquiera lo reproduce construyendo las dos "
                         "imagenes y comparando. Menos bytes = menos descarga en cada corrida "
                         "de CI y menos almacenamiento en el registro."],
                        ["**2.** Apagar la `API de prestamos` fuera del horario de la "
                         "biblioteca: escalar a cero de 22:00 a 6:00.",
                         "La **politica de escalado** (la que la Clase 13 formaliza) y el "
                         "registro de horas encendidas.",
                         "La politica dice el rango horario y el conteo de horas facturables "
                         "del mes baja de **720 a 480**. Se comprueba con el registro de "
                         "arranques y paradas: si sigue en 720, no se aplico."],
                        ["**3.** No ejecutar el pipeline en cada `push` de cada rama, y "
                         "reutilizar cache de `npm` y de capas de Docker.",
                         "El `ci.yml` de la Clase 8: el bloque `on:` y la clave "
                         "`cache: 'npm'`.",
                         "Se lee el YAML —los disparadores son `main` y solicitudes de cambios, "
                         "no `push` a cualquier rama— y se comparan las duraciones de dos "
                         "corridas seguidas: la segunda debe ser mas corta porque reutilizo el "
                         "cache. Si las dos duran lo mismo, el cache no esta funcionando."],
                    ],
                },
                "respuesta": """**El vinculo con los drivers de costo de la pregunta 11**

Las tres se apalancan sobre un driver de la tabla anterior, y la segunda es la mas directa:

- **Accion 2 -> driver «horas de instancia encendida» de la fila `API de prestamos` (nivel A).**
  Es literalmente el mismo apalancamiento escrito en esa fila: pasar de 720 a 480 horas al mes.
  Un tercio menos de horas es un tercio menos de energia consumida y un tercio menos de
  factura; la misma decision baja las dos cosas.
- **Accion 3 -> driver «minutos de CI».** Menos corridas y corridas mas cortas.
- **Accion 1 -> driver «GB almacenados» del registro y, de rebote, «minutos de CI»**, porque una
  imagen ocho veces mas pequena se descarga y arranca mas rapido en cada corrida.

Que costo y sostenibilidad se apalanquen con la misma decision no es una coincidencia
retorica: el recurso que no se consume no se paga y no se genera. Por eso la pregunta pide
atar al menos una.

**Por que estas tres pasan la prueba de los seis meses.** El enunciado da el criterio: si otra
persona abre el repositorio dentro de seis meses, ¿puede decir si la accion se aplico? Con las
tres, si: la primera linea del `Dockerfile` esta ahi, el bloque `on:` del `ci.yml` esta ahi, y
la politica de escalado esta escrita con su rango horario. Ninguna depende de que alguien
recuerde haber tenido buenas intenciones.

**Una cuarta que quedo fuera, por si el grupo la propone:** apagar el escenario de Killercoda
al terminar la sesion, comprobable en la bitacora del laboratorio de la Clase 3. Es valida y
esta bien formada —artefacto y comprobacion—, pero es la que viene como ejemplo en el
enunciado, asi que la use como referencia y no como respuesta.""",
                "como_calificar": [
                    "2.5 pts por accion verificable, hasta 3 acciones: **suma completo solo si "
                    "nombra el artefacto Y como se comprueba**. Las dos columnas pesan igual, "
                    "asi que una accion con artefacto pero sin metodo de comprobacion vale "
                    "1.25.",
                    "1.25 pts por **atar al menos una accion a un driver de costo de la "
                    "pregunta 11**. Se exige que el driver exista en su propia tabla: atarla a "
                    "un driver que no listo no cuenta.",
                    "**Una accion que no se pueda comprobar mirando un artefacto vale cero, "
                    "aunque sea razonable.** «Concientizar al equipo», «ser mas eficientes», "
                    "«usar la nube de forma responsable»: cero, sin discusion. La regla es "
                    "mecanica a proposito.",
                    "El artefacto tiene que ser **del proyecto**: el `Dockerfile`, el `ci.yml`, "
                    "la politica de escalado, la bitacora del laboratorio, el diagrama. Un "
                    "«documento de buenas practicas» escrito para la ocasion no es un "
                    "artefacto del sistema.",
                    "Se aceptan las tres acciones del ejemplo del enunciado **si el estudiante "
                    "las aterriza a su proyecto** con su artefacto y su metodo. Copiar la frase "
                    "sin aterrizarla vale la mitad; el enunciado dice que son ejemplos de "
                    "forma.",
                    "La prueba de los seis meses del enunciado es el mejor criterio de "
                    "arbitraje cuando una accion queda en la frontera: «si otra persona abre el "
                    "repositorio dentro de seis meses, ¿puede decir si se aplico?». Uselo tal "
                    "cual en la retroalimentacion.",
                ],
                "errores": [
                    "«Concientizar al equipo sobre el uso responsable de los recursos». Es la "
                    "respuesta que la pregunta esta diseñada para descartar: no hay artefacto y "
                    "no hay comprobacion. Cero, y conviene decirlo antes del taller para que "
                    "nadie gaste tres lineas en ella.",
                    "Acciones ambientales sin conexion con el diseno: reciclar, imprimir menos, "
                    "apagar las luces del salon. La pregunta dice **sostenibilidad tecnica** y "
                    "**verificable en el propio diseno**. No se descuenta la intencion, pero no "
                    "suma.",
                    "Nombrar el artefacto y dejar en blanco el como. Es la mitad de cada "
                    "accion. La pregunta de correccion: «abro ese archivo, ¿que linea me dice "
                    "que se aplico?».",
                    "Atar la accion a un driver que no aparece en su tabla de la pregunta 11. "
                    "Se ve poniendo las dos respuestas al lado y cuesta el 1.25. Suele pasar "
                    "cuando la tabla se hizo de ultimo y sin revisar la 12.",
                    "Tres acciones que son la misma: cache de npm, cache de Docker y cache del "
                    "navegador. Son tres formas de una decision. Pida que toquen artefactos "
                    "distintos.",
                    "Proponer apagar la base de datos por la noche. No se puede sin perder el "
                    "servicio y sin arriesgar el respaldo: es el ejemplo de una accion que "
                    "suena sostenible y rompe el sistema. Corrijala mostrando que la fila de "
                    "la base tiene otro apalancamiento (la retencion).",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Puedo poner precios reales si los busco en la calculadora del proveedor?",
             "No, y se descuenta fuerte. El curso no abre cuentas de pago y los precios cambian "
             "por region y por nivel: cualquier cifra seria una adivinanza con aspecto de dato. "
             "La escala es B/M/A y con eso alcanza para decidir donde apalancar."),
            ("¿Que hago con un componente al que no le encuentro driver?",
             "Volver al diagrama de la Clase 7, que es lo que dice el enunciado. Si un "
             "componente no tiene una variable que haga crecer su factura, o esta mal entendido "
             "o no deberia estar en el diagrama. Las dos conclusiones son utiles."),
            ("¿Por que no puede ser todo Medio?",
             "Porque entonces la tabla no ordena nada, y ordenar es lo unico que la escala "
             "ordinal permite hacer. Sin un Alto no se sabe donde apalancar primero, y ese es "
             "el proposito del ejercicio. El criterio de niveles queda en cero."),
            ("¿La escala B/M/A dice cuantas veces mas cuesta un componente?",
             "No. Es ordinal: dice que uno cuesta mas que otro, no cuantas veces mas. "
             "Confundirlo es lo que lleva a inventar precios; el orden es suficiente para "
             "decidir."),
            ("¿Los minutos de CI cuestan de verdad?",
             "En repositorios publicos son ilimitados y en privados hay 2000 al mes gratis, asi "
             "que en el curso no se paga nada. Aun asi es un driver real: en un equipo con "
             "repositorio privado y varias ramas, los 2000 minutos se agotan a mitad de mes."),
            ("¿Sostenibilidad es lo ambiental?",
             "Aqui es sostenibilidad **tecnica**: decisiones de diseno que reducen el recurso "
             "consumido y se pueden comprobar en un artefacto. Casi siempre coinciden con lo "
             "ambiental —el recurso que no se consume no se genera— pero la que se califica es "
             "la verificable."),
            ("¿Vale apagar el laboratorio de Killercoda como una de las tres?",
             "Es valida y esta bien formada, pero viene como ejemplo en el enunciado. Si la usa, "
             "aterricela a su bitacora concreta; y busque al menos dos que salgan de sus "
             "propios artefactos."),
            ("¿Tengo que atar las tres acciones a un driver de costo?",
             "Solo una es obligatoria y vale 1.25 pts. Atar las tres no suma mas, pero suele "
             "ser lo que pasa naturalmente: la misma decision baja el costo y el consumo."),
        ],
        "cierre": (
            "Lo que queda de hoy es que una decision de arquitectura se puede defender con una "
            "variable contable en la mano: no «la nube es cara», sino «esta pieza se paga por "
            "horas encendidas y la mia esta encendida 720 al mes». Deje anotadas las tres "
            "conexiones hacia adelante: el apalancamiento de escalar a cero es la politica que "
            "la Clase 13 va a escribir con su metrica y su ventana de enfriamiento, la fila de "
            "la base de datos es el componente que alli se vera que **no** escala, y la tabla "
            "completa es una de las piezas del paquete que el checkpoint de la Clase 11 revisa. "
            "Con esto cierra el Corte 2: el sistema ya tiene amenazas con controles, un lugar "
            "donde ejecutarse, un pipeline que lo verifica y un costo que se puede ordenar."
        ),
    },

    11: {
        "titulo": "Solucion del Taller Clase 11 - Checkpoint del paquete v1 (BiblioLite)",
        "resumen": (
            "Taller propio de 100 puntos en cinco preguntas. Es el checkpoint: no se produce "
            "arquitectura nueva, se audita la que ya existe. La solucion resuelve el checklist "
            "de las diez evidencias con ruta real, reconcilia los cinco nombres canonicos entre "
            "diagramas y codigo, abre la API en un C4Component de cinco componentes y deja un "
            "backlog fechado de cinco items hacia la sustentacion. Aqui se documenta tambien la "
            "unica evolucion de arquitectura del semestre: BiblioLite suma la cola de avisos y "
            "el procesador de avisos, que la lista canonica exige desde esta clase."
        ),
        "total": 100,
        "nota_actividad": (
            "**Nota de calendario 2026-2.** Las Clases 11 y 12 caen en la **misma sesion doble "
            "del lunes 26/10/2026**, asi que el criterio de la pregunta 4 —«las 5 fechas deben "
            "ser anteriores a la Clase 12»— no se puede cumplir literalmente: la Clase 12 es hoy. "
            "Se califica leyendolo como **anteriores a la sesion autonoma de la Clase 13 "
            "(02/11/2026)** para los items que bloquean a otros, y en todo caso **anteriores a la "
            "sustentacion de la Clase 15 (16/11/2026)**. Cualquier fecha real entre el 27/10/2026 "
            "y el 13/11/2026 se acepta sin descuento. Anunciarlo en voz alta al abrir el taller "
            "evita quince preguntas identicas."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "Checklist del paquete v1",
                "tipo": "abierta",
                "puntos": 25,
                "tabla": {
                    "headers": ["Evidencia", "Estado", "Ruta o enlace exacto", "Responsable"],
                    "rows": [
                        ["1. Ficha de dominio con 4 capacidades (Clase 1)", "si",
                         "`/informe/01-ficha-dominio.md`, seccion 1",
                         "Autor del paquete"],
                        ["2. Diagrama C4 Context (Clase 1)", "si",
                         "`/diagramas/c4-context.png` con fuente `/diagramas/c4-context.mmd`",
                         "Autor del paquete"],
                        ["3. ADR-001 del modelo de servicio (Clase 2)", "si",
                         "`/adr/ADR-001-modelo-de-servicio.md`",
                         "Autor del paquete"],
                        ["4. Dockerfile del stub y evidencia del lab (Clase 3)", "si",
                         "`/docker/Dockerfile` y `/capturas/clase03-docker-ps.png`",
                         "Autor del paquete"],
                        ["5. Diagrama C4 Container y tabla de 3 contratos (Clase 4)", "parcial",
                         "`/diagramas/c4-container.png` y `/informe/04-contratos.md`",
                         "Autor del paquete - cierra B-02 el 30/10/2026"],
                        ["6. Modelo de amenazas y politica de secretos (Clase 6)", "si",
                         "`/informe/06-amenazas.md` y `/informe/06-politica-secretos.md`",
                         "Autor del paquete"],
                        ["7. Diagrama C4 Deployment con zonas y almacenamiento (Clase 7)",
                         "parcial", "`/diagramas/c4-deployment.png`",
                         "Autor del paquete - cierra B-01 el 28/10/2026"],
                        ["8. Workflow ci.yml con enlace al run verde (Clase 8)", "si",
                         "`/.github/workflows/ci.yml` y el run "
                         "`https://github.com/USUARIO/bibliolite/actions/runs/ID`",
                         "Autor del paquete"],
                        ["9. Seccion de costos y sostenibilidad (Clase 10)", "si",
                         "`/informe/10-costos-sostenibilidad.md`",
                         "Autor del paquete"],
                        ["10. Informe del PI al 60 por ciento o mas", "si",
                         "`/informe/informe-pi.md` (68 por ciento; el indice de la primera "
                         "pagina enlaza cada evidencia por su ruta)",
                         "Autor del paquete"],
                    ],
                },
                "respuesta": (
                    "**Linea de cierre:** 8 filas en `si` sobre 10. Las dos en `parcial` son las "
                    "filas 5 y 7, ambas con item de backlog y fecha.\n\n"
                    "Tres cosas que sostienen esta tabla y que conviene decir en voz alta al "
                    "revisar:\n\n"
                    "1. **Las rutas son rutas dentro del paquete, no descripciones.** "
                    "`/diagramas/c4-container.png` se abre; «el diagrama del container» no se "
                    "abre. La regla del enunciado es dura a proposito: una fila en `si` sin ruta "
                    "se califica como `no` y ademas descuenta 2 pts. Es la unica forma de que el "
                    "checklist no se convierta en una declaracion de buenas intenciones.\n"
                    "2. **Los dos `parcial` no son un fracaso, son el resultado del trabajo de "
                    "hoy.** La pregunta 3 abre la API y, al hacerlo, BiblioLite pasa a tener "
                    "cinco contenedores canonicos en lugar de tres (ver la pregunta 2). Eso deja "
                    "desactualizados exactamente dos artefactos: el C4 Container de la Clase 4 "
                    "—que sigue con tres cajas y una tabla de tres contratos— y el C4 Deployment "
                    "de la Clase 7 —que no tiene la cola en la zona privada—. Un checkpoint que "
                    "descubre incoherencias esta funcionando; uno que sale con diez `si` "
                    "normalmente es uno que no se leyo.\n"
                    "3. **El enlace del run verde debe ser el del estudiante.** Aqui aparece con "
                    "`USUARIO` y `ID` en mayusculas porque este documento es del docente. En el "
                    "paquete real va la URL completa del run de GitHub Actions, y el docente la "
                    "abre: si el run esta rojo o no existe, la fila 8 es `no`, no `parcial`."
                ),
                "como_calificar": [
                    "**10 pts** las 10 filas presentes y en el orden pedido por el enunciado "
                    "(Clase 1, 1, 2, 3, 4, 6, 7, 8, 10, informe). Se descuenta 1 pt por fila "
                    "ausente o desordenada; no se penaliza dos veces la misma fila.",
                    "**8 pts** que cada `si` tenga ruta o enlace verificable. Se reparte "
                    "proporcionalmente entre las filas marcadas `si`: con 8 filas en `si`, cada "
                    "una vale 1 pt.",
                    "**5 pts** que cada `parcial` o `no` traiga responsable **y** fecha de cierre. "
                    "Falta cualquiera de los dos y esa fila no suma.",
                    "**2 pts** la linea de conteo final (cuantas filas en `si` sobre 10).",
                    "**Descuento de 2 pts por cada `si` sin ruta**, aplicado despues de sumar. "
                    "Es el unico descuento de la pregunta y se aplica sin excepcion: es la regla "
                    "que le da valor a las otras nueve filas.",
                    "Se acepta cualquier estructura de carpetas del paquete, siempre que las "
                    "rutas de la tabla coincidan con la del ZIP o el repositorio entregado. "
                    "Abrir dos rutas al azar del paquete es la verificacion mas rentable.",
                ],
                "errores": [
                    "**Diez `si` sin una sola ruta.** Es el error mas comun y el mas caro: la "
                    "tabla queda en 10 pts de estructura y pierde los 8 de rutas mas 20 de "
                    "descuento, con piso en cero. Antes de calificar, avisar en voz alta que las "
                    "rutas se abren.",
                    "**Ruta que apunta a Google Drive o a WhatsApp.** No es ruta dentro del "
                    "paquete ni enlace publico verificable: si el docente no puede abrirlo sin "
                    "pedir permiso, cuenta como `no`. Se acepta un enlace publico de GitHub.",
                    "**`parcial` sin fecha, o con «pronto» y «esta semana».** El enunciado pide "
                    "fecha, y la nota de calendario de arriba fija la ventana valida. Devolver "
                    "para que escriba una fecha real de octubre o noviembre de 2026.",
                    "**Marcar `si` la fila 8 con el enlace al repositorio en vez del run.** El "
                    "repositorio no prueba que el pipeline paso; el run verde si. Es `parcial`, "
                    "con la accion «capturar el enlace del run» en el backlog.",
                    "**Inflar el informe al 60 por ciento contando la portada y la bibliografia.** "
                    "El porcentaje se estima sobre secciones con contenido propio. Si el informe "
                    "tiene los titulos pero no el texto, es `parcial`, no `si`.",
                ],
            },
            {
                "n": 2,
                "titulo": "Reconciliacion de nombres entre artefactos",
                "tipo": "abierta",
                "puntos": 20,
                "tabla": {
                    "headers": ["Nombre canonico", "En el C4 Container", "En el C4 Deployment",
                                "En el Dockerfile o ci.yml", "Correccion aplicada"],
                    "rows": [
                        ["Aplicacion web", "Aplicacion web", "Aplicacion web",
                         "no aplica",
                         "sin cambios - el bundle de React se publica como estatico y el "
                         "pipeline de la Clase 8 solo construye la imagen de la API"],
                        ["API de prestamos", "API de prestamos", "API de prestamos",
                         "`bibliolite-api:0.1.0` y `--name api`",
                         "renombre `--name api` a `--name api-prestamos` en "
                         "`.github/workflows/ci.yml`, paso «Arranque y health»; la imagen sigue "
                         "siendo `bibliolite-api` y el informe trae el mapeo nombre-slug"],
                        ["Procesador de avisos", "Procesador de avisos (agregado hoy)",
                         "no aplica todavia", "no aplica todavia",
                         "agregue el contenedor a `/diagramas/c4-container.mmd` y regenere el "
                         "PNG; el despliegue queda en B-01 y el pipeline en B-03"],
                        ["Base de datos de prestamos", "Base de datos de prestamos",
                         "Base de datos de prestamos",
                         "no aplica (entra como el secreto `DATABASE_URL`)",
                         "sin cambios - en el pipeline la base no es un servicio con nombre sino "
                         "una cadena de conexion inyectada como secreto"],
                        ["Cola de avisos", "Cola de avisos (agregada hoy)",
                         "no aplica todavia", "no aplica todavia",
                         "agregue el contenedor a `/diagramas/c4-container.mmd` y regenere el "
                         "PNG; el despliegue queda en B-01"],
                    ],
                },
                "respuesta": (
                    "**Linea de cierre:** 3 correcciones aplicadas hoy (una en el `ci.yml` y dos "
                    "en `c4-container.mmd`); 2 elementos quedan en `no aplica todavia` en dos "
                    "columnas, con B-01 y B-03 abiertos y fechados.\n\n"
                    "**Por que BiblioLite tiene ahora cinco contenedores y no tres.** La lista "
                    "canonica que esta clase exige es interfaz web, API, procesador asincrono, "
                    "base de datos y cola. La Clase 4 dibujo tres cajas, y eso no fue un "
                    "descuido: fue la decision de monolito modular para un equipo de una persona "
                    "en doce semanas. Lo que aparecio despues fue la evidencia de que el modulo "
                    "de notificaciones no puede vivir en la peticion HTTP. Esta escrito en dos "
                    "artefactos propios: la tabla de riesgos de la Clase 4 dice «si el correo "
                    "esta caido el aviso muere y nadie se entera», y la tabla de senales de la "
                    "Clase 8 tiene una fila entera para «fallos de envio de correo». Un aviso que "
                    "debe reintentarse necesita alguien que lo reintente cuando la peticion ya "
                    "termino. Eso es un procesador asincrono, y para hablarle hace falta una "
                    "cola.\n\n"
                    "**Y por que esto no rompe el ADR-001 ni la decision de la Clase 4.** El "
                    "procesador de avisos **no es un microservicio nuevo**: es la **misma imagen** "
                    "`bibliolite-api:0.1.0` arrancada con otro comando "
                    "(`CMD [\"node\", \"src/worker.js\"]` en lugar de `src/server.js`). Un "
                    "repositorio, un build, un pipeline, dos procesos. El monolito modular sigue "
                    "en pie: lo que cambio es que uno de sus modulos corre fuera del ciclo de "
                    "peticion. Decirlo asi, con el nombre del archivo, es lo que distingue una "
                    "evolucion justificada de un cambio de opinion.\n\n"
                    "**El caso incomodo de la fila 2, que hay que saber responder.** El enunciado "
                    "pide que el nombre canonico quede identico en las tres columnas del medio. "
                    "En un artefacto de codigo eso es literalmente imposible: un nombre de imagen "
                    "de Docker no admite espacios ni mayusculas, asi que `API de prestamos` no "
                    "puede aparecer tal cual en un tag. La regla operativa que se califica es "
                    "esta: **el nombre canonico manda en la prosa y en los diagramas, y en el "
                    "codigo aparece como su slug** (`API de prestamos` -> `api-prestamos`), con "
                    "un mapeo de dos lineas en el informe. Lo que si es un hallazgo real es que "
                    "el contenedor del run se llamaba `api`, un nombre que no se parece a nada: "
                    "ese es el que se renombro."
                ),
                "como_calificar": [
                    "**8 pts** las 5 filas con las 5 columnas, una por elemento de la lista "
                    "canonica. Si el estudiante tiene un sexto elemento real (un edge, un "
                    "almacen de objetos) puede agregar la fila: no resta.",
                    "**6 pts** que el nombre canonico quede identico en las tres columnas del "
                    "medio **al terminar el ejercicio**, o que la diferencia quede explicada. Se "
                    "acepta el slug en la columna de codigo (`api-prestamos` para "
                    "`API de prestamos`) siempre que el informe traiga el mapeo; no se acepta un "
                    "nombre sin relacion (`app`, `servicio1`, `test`).",
                    "**4 pts** la columna de correccion citando **el archivo editado** con su "
                    "nombre, no la accion en abstracto. «Renombre en el diagrama» no suma; "
                    "«renombre en `c4-deployment.mmd`» si.",
                    "**2 pts** las justificaciones de media linea de cada `no aplica` y la linea "
                    "de conteo final.",
                    "Se acepta `no aplica todavia` con un item de backlog fechado para un "
                    "elemento que el estudiante agrego hoy: es el caso de las filas 3 y 5 de esta "
                    "solucion y es la respuesta correcta, no una excusa. Lo que no se acepta es "
                    "la celda vacia.",
                ],
                "errores": [
                    "**Rellenar las tres columnas del medio con el nombre canonico sin haber "
                    "abierto los archivos.** Se detecta en diez segundos: se abre el `.mmd` o el "
                    "`ci.yml` y se busca el nombre. Si no esta, la fila pierde los pts de "
                    "coherencia y la de correccion.",
                    "**Cambiar el nombre canonico para que coincida con el codigo.** Es al "
                    "reves: manda el nombre del dominio, no el identificador que quedo de un "
                    "tutorial. Un canonico que se llama `app` es una senal de que no hubo "
                    "reconciliacion.",
                    "**Poner `no aplica` sin justificar.** Vale 0 en los 2 pts de "
                    "justificaciones, y suele esconder un elemento que si existe pero que el "
                    "estudiante no encontro.",
                    "**Agregar la cola y el procesador sin justificar de donde salen.** Si "
                    "aparecen porque el enunciado los nombra, el diagrama de la pregunta 3 no se "
                    "sostiene en el Q&A de la Clase 15. Pedir la frase: que evidencia propia los "
                    "hizo necesarios.",
                    "**Declarar microservicios porque ahora hay cinco cajas.** Cinco "
                    "contenedores no son cinco servicios: aqui son dos procesos de la misma "
                    "imagen, un estatico, una base y una cola. Si el estudiante cambio el ADR-001 "
                    "sin nueva evidencia, devolver.",
                ],
            },
            {
                "n": 3,
                "titulo": "C4 Component: por dentro de la API de prestamos",
                "tipo": "diagrama",
                "puntos": 25,
                "respuesta_mermaid": """C4Component
    title Componentes internos de la API de prestamos - dominio BiblioLite
    Container(spa, "Aplicacion web", "React", "Consulta del catalogo y reserva de ejemplares")
    Container_Boundary(api, "API de prestamos - Node.js") {
        Component(router, "Router HTTP de /titulos y /prestamos", "Express Router", "Recibe la peticion y valida el esquema de entrada")
        Component(auth, "Verificador de token institucional", "Libreria de JWT", "Valida la firma y la expiracion del token del proveedor de identidad")
        Component(reservas, "Servicio de reservas", "Node.js", "Evita la doble reserva del mismo ejemplar y aplica el limite de 3 prestamos por estudiante")
        Component(repo, "Repositorio de prestamos", "node-postgres", "Encapsula el SQL sobre titulos ejemplares y prestamos")
        Component(pub, "Publicador de avisos", "Cliente de Redis", "Publica el evento prestamo_por_vencer en la cola")
    }
    ContainerDb(db, "Base de datos de prestamos", "PostgreSQL", "Titulos ejemplares reservas y prestamos")
    ContainerQueue(cola, "Cola de avisos", "Redis Streams", "Eventos de aviso de vencimiento")
    System_Ext(idp, "Proveedor de identidad institucional", "Login OIDC de la universidad")
    Rel(spa, router, "POST /titulos/{isbn}/reservas y GET /titulos", "JSON sobre HTTPS")
    Rel(router, auth, "Delega la validacion del token")
    Rel(auth, idp, "Descarga las claves publicas de firma", "HTTPS 443")
    Rel(router, reservas, "Invoca crear_reserva con el isbn y el id del estudiante")
    Rel(reservas, repo, "Consulta el ejemplar disponible y guarda la reserva")
    Rel(repo, db, "SQL 5432")
    Rel(reservas, pub, "Emite el evento prestamo_por_vencer")
    Rel(pub, cola, "XADD en 6379")""",
                "respuesta": (
                    "Conteos que se verifican de un golpe: **5 `Component`** dentro de la "
                    "frontera, **4 elementos externos** (`Container`, `ContainerDb`, "
                    "`ContainerQueue`, `System_Ext`), **8 `Rel`** y la primera linea exactamente "
                    "`C4Component`.\n\n"
                    "**La frontera es la caja de la Clase 4, con su tecnologia.** "
                    "`Container_Boundary(api, \"API de prestamos - Node.js\")` repite el nombre y "
                    "la tecnologia del C4 Container. Ese es el enlace entre los dos niveles: si "
                    "la frontera se llamara `Backend` o `Servidor`, el diagrama seria de otro "
                    "sistema.\n\n"
                    "**Ninguno de los cinco componentes es un contenedor disfrazado.** La prueba "
                    "es de una linea: un componente es codigo que se despliega **dentro** del "
                    "mismo proceso; un contenedor es algo que se despliega **aparte** y se alcanza "
                    "por red. El `Repositorio de prestamos` es codigo que habla SQL: componente. "
                    "La `Base de datos de prestamos` escucha en 5432: contenedor, y por eso esta "
                    "fuera de la frontera. El error que cuesta 10 pts es exactamente ese: meter "
                    "`ContainerDb` o la cola adentro.\n\n"
                    "**El flujo se lee de punta a punta y pasa por los cinco.** Aplicacion web -> "
                    "router (valida el esquema) -> verificador de token (y este consulta las "
                    "claves del IdP) -> servicio de reservas (la regla de negocio: no hay doble "
                    "reserva del mismo ejemplar) -> repositorio (el unico que sabe SQL) -> base "
                    "de datos. Y en paralelo, el servicio de reservas emite el evento al "
                    "publicador, que hace `XADD` en la cola. La regla de negocio no le habla ni a "
                    "la base ni a la cola directamente: siempre a traves de la pieza que "
                    "encapsula ese detalle. Eso es lo que hace que el diagrama sirva para algo, y "
                    "es la respuesta al «por que» de la Clase 15.\n\n"
                    "**Continuidad con lo ya entregado.** El `409` del contrato "
                    "`POST /titulos/{isbn}/reservas` de la Clase 4 se decide en el `Servicio de "
                    "reservas`; la validacion de token de la Clase 6 es el `Verificador de token "
                    "institucional`; el puerto 5432 de la zona de datos de la Clase 7 es la "
                    "unica flecha que sale del repositorio. Nada nuevo: se abrio la caja y "
                    "adentro estaba lo que se venia diciendo."
                ),
                "como_calificar": [
                    "**10 pts** los 5 componentes dentro de la frontera, cada uno con nombre, "
                    "tecnologia y responsabilidad en una frase, cubriendo las 5 "
                    "responsabilidades del enunciado: recibir y validar HTTP, verificar el token, "
                    "regla de negocio, acceso a datos, publicar el evento. Son 2 pts cada una; "
                    "una responsabilidad ausente no se compensa con dos componentes de otra.",
                    "**6 pts** los 4 elementos externos con los nombres canonicos de la pregunta "
                    "2 **y el tipo correcto**: `Container` la web, `ContainerDb` la base, "
                    "`ContainerQueue` la cola, `System_Ext` el proveedor de identidad. 1.5 pts "
                    "cada uno; un tipo equivocado (la cola como `Container`) pierde la mitad de "
                    "su parte.",
                    "**6 pts** las 8 relaciones formando un flujo legible de la web a la base "
                    "pasando por los cinco componentes. Se acepta que dos relaciones no lleven "
                    "protocolo si son internas al proceso; las que cruzan a la base, la cola o el "
                    "IdP si deben llevarlo.",
                    "**3 pts** que renderice sin error en la plataforma. Se verifica abriendo la "
                    "respuesta, no leyendo el codigo.",
                    "**Descuento de 10 pts si un componente es en realidad un contenedor de la "
                    "Clase 4** (la base, la cola o la interfaz web dentro del "
                    "`Container_Boundary`). Es el error conceptual que la pregunta persigue y el "
                    "descuento se aplica completo, una sola vez.",
                    "Se acepta otro reparto de las 5 responsabilidades entre nombres distintos "
                    "(`Controlador` en vez de `Router`, `DAO` en vez de `Repositorio`) siempre "
                    "que la responsabilidad escrita sea la pedida.",
                ],
                "errores": [
                    "**La base de datos como sexto componente adentro.** Es el descuento de 10 "
                    "pts. Devolver con la prueba de una linea: ¿se alcanza por red o corre en el "
                    "mismo proceso?",
                    "**Cinco componentes que son cinco endpoints** (`GET /titulos`, "
                    "`POST /prestamos`...). Un componente es una responsabilidad tecnica, no una "
                    "ruta. Se detecta porque las responsabilidades escritas se repiten.",
                    "**`Component` en lugar de `Container_Boundary`, o `System_Boundary`.** El "
                    "diagrama renderiza pero el nivel queda mal: en C4 Component la frontera es "
                    "el contenedor. Cuesta los 3 pts de render solo si falla; si renderiza, "
                    "cuesta parte de los 6 de externos.",
                    "**Renombrar el contenedor de la frontera.** Si la API se llama `Backend` "
                    "aqui y `API de prestamos` en la Clase 4, el trabajo de la pregunta 2 se "
                    "deshizo en la pregunta 3. Es el chequeo cruzado mas rapido del taller.",
                    "**Publicar el evento desde el router.** Renderiza igual, pero significa que "
                    "el aviso se emite antes de saber si la reserva se guardo. Vale la pena "
                    "senalarlo aunque no descuente: es material del Q&A de la Clase 15.",
                    "**Nueve o siete relaciones.** El enunciado pide exactamente 8. Contar es "
                    "parte de la tarea; se descuenta dentro de los 6 pts de relaciones, no en "
                    "toda la pregunta.",
                ],
            },
            {
                "n": 4,
                "titulo": "Backlog de 5 items hacia la Clase 12",
                "tipo": "abierta",
                "puntos": 20,
                "tabla": {
                    "headers": ["ID", "Hueco detectado", "Accion concreta", "Responsable",
                                "Fecha de cierre"],
                    "rows": [
                        ["B-01",
                         "**[docente]** El C4 Deployment no tiene la cola de avisos ni el "
                         "procesador de avisos, que hoy quedaron en el C4 Container y en el C4 "
                         "Component - Clase 7, fila 7 del checklist",
                         "Agregar los dos nodos a la zona privada de "
                         "`/diagramas/c4-deployment.mmd` con puerto y protocolo (6379 TCP para la "
                         "cola) y regenerar el PNG",
                         "Autor del paquete", "28/10/2026"],
                        ["B-02",
                         "La tabla de contratos tiene 3 filas y ninguna describe la publicacion "
                         "en la cola - Clase 4, fila 5 del checklist",
                         "Agregar la cuarta fila a `/informe/04-contratos.md`: evento "
                         "`prestamo_por_vencer`, productor la API, consumidor el procesador, "
                         "error de negocio «mensaje duplicado» resuelto por idempotencia con "
                         "`id_prestamo`",
                         "Autor del paquete", "30/10/2026"],
                        ["B-03",
                         "El `ci.yml` construye y arranca solo la API; el procesador de avisos no "
                         "se arranca ni se prueba - Clase 8, fila 8 del checklist",
                         "Agregar al workflow un paso que arranque la misma imagen con "
                         "`node src/worker.js`, publique un mensaje de prueba en la cola y "
                         "verifique que el worker lo consume",
                         "Autor del paquete", "02/11/2026"],
                        ["B-04",
                         "La tabla de senales no vigila la profundidad de la cola, que ahora es "
                         "una pieza real del sistema - Clase 8, fila 8 del checklist",
                         "Agregar la fila «profundidad de la cola de avisos» con umbral de "
                         "revision en 500 mensajes, alerta en 1000 y accion «revisar si el "
                         "procesador esta caido»",
                         "Autor del paquete", "05/11/2026"],
                        ["B-05",
                         "La seccion de costos no tiene fila para la cola ni para el procesador "
                         "de avisos - Clase 10, fila 9 del checklist",
                         "Agregar dos filas con driver de costo y nivel B/M/A, y reescribir el "
                         "apalancamiento del procesador: escala a cero fuera de la ventana de "
                         "avisos de las 06:00",
                         "Autor del paquete", "09/11/2026"],
                    ],
                },
                "respuesta": (
                    "**Las 2 lineas de cierre:**\n\n"
                    "> **Bloqueante:** B-01. Mientras el C4 Deployment no tenga los dos nodos, "
                    "B-03 no sabe en que zona corre el procesador ni contra que host de cola "
                    "apunta, y B-05 no tiene una caja a la cual asignarle un driver de costo. Los "
                    "tres items se ordenan detras de el.\n"
                    "> **Deuda tecnica aceptada:** no se va a separar el modulo de "
                    "notificaciones en su propio repositorio con su propio pipeline. Razon: el "
                    "ADR-001 y la decision de la Clase 4 fijaron monolito modular para un equipo "
                    "de una persona, y el procesador de avisos es el mismo artefacto (misma "
                    "imagen, otro comando), asi que separarlo duplicaria el pipeline sin cambiar "
                    "el riesgo. Se revisa si la cola pasa de 1000 mensajes sostenidos, que es "
                    "justo el umbral de alerta que B-04 va a escribir.\n\n"
                    "Los cinco items comparten una forma que conviene exigir: **el hueco cita la "
                    "evidencia y la clase de origen**, la accion **empieza por un verbo** "
                    "(agregar, agregar, agregar, agregar, agregar —aqui todos son de completar, "
                    "que es lo normal en un checkpoint— y no «mejorar» ni «revisar»), y la fecha "
                    "es una fecha. El item marcado `[docente]` es B-01: salio de la cola de "
                    "revision de hoy, no de la autoevaluacion, y por eso es el que encabeza.\n\n"
                    "Sobre el orden: no esta ordenado por esfuerzo sino por **cuantos otros items "
                    "desbloquea**. B-01 desbloquea tres; B-02 cierra la fila 5 del checklist, que "
                    "es la otra `parcial`; B-03, B-04 y B-05 son independientes entre si y podrian "
                    "hacerse en cualquier orden. Decir esto en voz alta cuesta treinta segundos y "
                    "es la mitad de la nota de la pregunta."
                ),
                "como_calificar": [
                    "**8 pts** las 5 filas con IDs `B-01` a `B-05` y las 5 columnas completas. "
                    "Sin IDs no hay como referenciar los items en la Clase 15: se descuenta.",
                    "**5 pts** que cada hueco cite **evidencia y clase de origen**. «Falta "
                    "documentacion» no cita nada; «el `ci.yml` no arranca el worker - Clase 8» "
                    "si. 1 pt por fila.",
                    "**4 pts** que al menos un item venga del feedback del docente, marcado "
                    "`[docente]`, **y** que las 5 fechas sean previas al plazo del calendario. "
                    "Ver la nota de arriba: por la sesion doble del 26/10/2026 se lee como «antes "
                    "del 13/11/2026», y ninguna fecha se penaliza por caer despues del 26/10.",
                    "**3 pts** las 2 lineas de cierre: el item bloqueante **con la razon del "
                    "bloqueo** y la deuda aceptada **con su justificacion**. Nombrar el item sin "
                    "decir por que bloquea vale la mitad.",
                    "Se acepta que los cinco items sean de completar artefactos existentes: en un "
                    "checkpoint eso es lo esperable. Lo que no se acepta es un item que no se "
                    "pueda cerrar en una semana (reescribir la API, migrar a microservicios).",
                ],
                "errores": [
                    "**Cinco items que son cinco tareas del proyecto** («terminar el informe», "
                    "«hacer el pitch»). El backlog es de **huecos de coherencia** detectados hoy, "
                    "no el cronograma del PI. Devolver pidiendo que cada fila apunte a una fila "
                    "del checklist de la pregunta 1.",
                    "**Ningun item marcado `[docente]`.** Cuesta parte de los 4 pts y suele "
                    "significar que el estudiante no paso por la cola de revision. Si paso y no "
                    "lo marco, se acepta con la marca agregada en el momento.",
                    "**Fechas como «semana 12» o «antes de la entrega».** Se pide fecha real. "
                    "Conviene tener el calendario a la vista al calificar: 02/11 y 16/11 son las "
                    "dos referencias que importan.",
                    "**Deuda aceptada que en realidad es un hueco grave** («aceptamos no tener "
                    "manejo de secretos»). La deuda se acepta cuando el riesgo esta acotado y "
                    "argumentado; si lo aceptado es un requisito del curso, no cuenta y ademas "
                    "abre un item nuevo.",
                    "**Item bloqueante elegido por ser el mas grande.** Bloquea el que otros "
                    "necesitan, no el que mas cuesta. Preguntar «¿que item no puedes empezar si "
                    "este no esta?» resuelve la duda en el momento.",
                ],
            },
            {
                "n": 5,
                "titulo": "Huecos tipicos del paquete v1",
                "tipo": "cerrada_multi",
                "puntos": 10,
                "justificacion": {
                    0: "**Hueco.** Es exactamente el ejercicio de la pregunta 2: el mismo "
                       "elemento con tres nombres. Rompe la trazabilidad entre niveles y en la "
                       "sustentacion obliga a traducir en voz alta, que es donde se cae el "
                       "«por que».",
                    1: "**Hueco.** Es el «CI que no es CI» de la Clase 8: un paso que imprime "
                       "`build ok` no verifica nada. Sin al menos un build real y una prueba, el "
                       "run verde no es evidencia de nada.",
                    2: "**No es hueco: es la practica correcta, invertida a proposito.** Fijar la "
                       "imagen base con un tag de version (`node:20-alpine`) es lo que hace el "
                       "build reproducible; `latest` es el antipatron, porque la misma linea "
                       "construye una imagen distinta cada semana. Quien marca esta opcion tiene "
                       "el concepto al reves y perdio 4 pts.",
                    3: "**Hueco.** Es la arquitectura de papel de la Clase 6: la columna «donde "
                       "se ve (caja o flecha)» existe justamente para que ninguna amenaza quede "
                       "sin un punto del diagrama al cual senalar. Cinco amenazas que no se "
                       "pueden senalar son cinco parrafos, no un modelo.",
                    4: "**No es hueco: es el criterio de aprobacion de la pregunta 1.** Que el "
                       "informe enlace cada evidencia por su ruta dentro del paquete es "
                       "precisamente lo que se pide; sin eso, una fila en `si` se califica como "
                       "`no`.",
                    5: "**No es hueco: es el acierto de la Clase 7.** La base en la zona de datos "
                       "y sin IP publica es la regla dura del diagrama de despliegue, la que "
                       "cuesta los 4 pts completos cuando se incumple. Marcarla como hueco "
                       "senala que el estudiante no interiorizo las zonas.",
                },
                "como_calificar": [
                    "**4 pts por cada hueco correctamente identificado, con techo de 10.** Las "
                    "tres correctas son las opciones 1, 2 y 4 tal como aparecen numeradas en la "
                    "plataforma (nombres desalineados, `ci.yml` sin pruebas, amenazas que no se "
                    "pueden senalar). La clave se lee del banco: no calificar de memoria.",
                    "**Se descuentan 4 pts por cada practica correcta marcada como hueco**, sin "
                    "bajar de cero. Marcar las seis da cero, no diez: es el diseno de la "
                    "pregunta.",
                    "Las tres distractoras no son ruido: cada una es un criterio que el curso ya "
                    "califico (tag de version en la Clase 3, enlace por ruta en esta misma "
                    "pregunta 1, zona de datos en la Clase 7). Si un estudiante marca alguna, "
                    "conviene devolverle a que clase pertenece.",
                    "Es la unica pregunta de la actividad que se autocalifica. Sirve como "
                    "termometro: si mas de la mitad del grupo marca la opcion del tag de "
                    "version, el repaso de la Clase 12 debe empezar por reproducibilidad de la "
                    "imagen.",
                ],
                "errores": [
                    "**Marcar las seis para asegurar las tres correctas.** El descuento lo deja "
                    "en cero. Vale decirlo antes de abrir la actividad: aqui marcar de mas "
                    "cuesta.",
                    "**Confundir «tag de version» con «version vieja».** Fijar `node:20-alpine` "
                    "no es quedarse atras: es decidir cuando se actualiza. Es la confusion mas "
                    "frecuente en esta pregunta.",
                    "**Leer la opcion del informe como una acusacion** («enlaza cada evidencia» "
                    "leido como «solo enlaza»). Si varios caen ahi, el problema es de lectura y "
                    "no de concepto; se aclara en voz alta y no se cambia la clave.",
                    "**Marcar la opcion de la base de datos por asociar «zona de datos» con "
                    "riesgo.** Es al contrario. Devolver al criterio de la Clase 7: sin IP "
                    "publica es lo correcto.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Por que aparecen una cola y un procesador de avisos que en la Clase 4 no estaban?",
             "Porque la lista canonica de esta clase los exige y porque el propio paquete ya los "
             "pedia: la tabla de riesgos de la Clase 4 dice que si el correo esta caido el aviso "
             "muere, y la tabla de senales de la Clase 8 tiene una fila para fallos de envio. Un "
             "aviso que hay que reintentar necesita a alguien que lo reintente cuando la peticion "
             "HTTP ya termino. No es un cambio de rumbo: el procesador es la misma imagen "
             "arrancada con otro comando, asi que el monolito modular del ADR-001 sigue vigente."),
            ("Mi nombre canonico tiene espacios y mayusculas. No cabe en un tag de Docker. "
             "¿Como lo reconcilio?",
             "Con un slug. El nombre canonico manda en los diagramas y en el informe; en el "
             "codigo aparece como `api-prestamos` o `bibliolite-api`, y el informe trae dos "
             "lineas de mapeo. Se califica igual. Lo que no se acepta es un identificador que no "
             "se parezca a nada, tipo `app` o `test`."),
            ("Si la Clase 12 es hoy mismo, ¿como pongo fechas anteriores a la Clase 12?",
             "No se puede, y no es su culpa: en 2026-2 las Clases 11 y 12 caen en la misma sesion "
             "doble del 26/10. Ponga fechas reales entre el 27/10 y el 13/11, con los items que "
             "bloquean antes del 02/11. Nadie pierde puntos por esto."),
            ("¿El C4 Component reemplaza al C4 Container?",
             "No. Se suma. Son dos niveles de zoom del mismo sistema: el Container muestra las "
             "piezas que se despliegan aparte, el Component abre una de ellas. En el paquete van "
             "los dos, y la frontera del Component debe llamarse igual que la caja del "
             "Container."),
            ("Mi API tiene ocho responsabilidades. ¿Puedo poner ocho componentes?",
             "El enunciado pide exactamente cinco, y estan elegidas para cubrir el camino "
             "completo de una peticion. Agrupe: lo que valida esquemas va con el router, lo que "
             "arma consultas va con el repositorio. Si de verdad sobra una responsabilidad que no "
             "encaja en ninguna de las cinco, es una senal interesante para el Q&A, pero el "
             "diagrama se entrega con cinco."),
            ("¿La deuda tecnica aceptada me resta puntos?",
             "Al contrario: es parte de los 3 pts del cierre. Lo que resta es aceptar como deuda "
             "algo que el curso pide (secretos, base en zona privada, un run verde). Deuda "
             "legitima es la que tiene riesgo acotado y una condicion escrita para revisarla."),
            ("Mi dominio no manda avisos. ¿Igual tengo que inventar una cola?",
             "No se inventa nada. Si su dominio no tiene ninguna tarea que sobreviva a la "
             "peticion, escriba `no aplica` en esa fila de la pregunta 2 y justifique en media "
             "linea; son 2 pts que se ganan explicando, no rellenando. En el C4 Component el "
             "quinto componente puede publicar a otro destino asincrono real de su sistema."),
            ("¿Cuenta como evidencia un pantallazo pegado en el informe, sin el archivo?",
             "Como `parcial`. La captura prueba que algo paso; la ruta al artefacto prueba que "
             "existe y se puede volver a correr. Deje la captura y agregue el archivo: es el "
             "tipo de item que se cierra en diez minutos y libera una fila del checklist."),
        ],
        "cierre": (
            "Lo que queda de hoy es un paquete que se puede abrir en otra maquina y una lista "
            "corta de lo que le falta, con fechas. Los dos hallazgos que importan quedaron "
            "escritos: los nombres estaban desalineados en el pipeline y el sistema ya "
            "necesitaba una cola y un procesador de avisos que ningun diagrama tenia. Ese "
            "segundo hallazgo es el que hay que llevar a la Clase 12, porque el escenario de "
            "carga y el presupuesto de latencia se calculan sobre las cajas que existen de "
            "verdad: la peticion de reserva ahora termina cuando la API publica en la cola, no "
            "cuando el correo sale. Y el backlog es la agenda: B-01 primero, porque sin el "
            "despliegue actualizado la Clase 13 no tiene sobre que escribir la politica de "
            "autoescalado."
        ),
    },

    12: {
        "titulo": "Solucion del Taller Clase 12 - Rendimiento y ensayo de sustentacion (BiblioLite)",
        "resumen": (
            "Taller propio de 100 puntos en seis preguntas. La primera mitad convierte «va "
            "rapido» en numeros: escenario del pico con seis datos calculados, presupuesto de "
            "latencia repartido salto por salto en un diagrama de secuencia, tres metricas "
            "objetivo con ventana de medicion y el cuello de botella con dos mitigaciones "
            "argumentadas. La segunda mitad es el guion cronometrado del pitch, con los tiempos "
            "reales de dos ensayos y lo que se recorto para entrar en el tiempo."
        ),
        "total": 100,
        "nota_actividad": (
            "**Nota de calendario 2026-2.** Las Clases 11 y 12 caen en la **misma sesion doble "
            "del lunes 26/10/2026**: este taller se abre en el segundo bloque, despues del "
            "checkpoint. Los dos tiempos de ensayo de la pregunta 5 se cronometran **hoy en "
            "clase, con el celular en la mano**; no se aceptan tiempos estimados. **No se pide "
            "ninguna herramienta de carga de pago ni cuenta de nube:** todo el escenario se "
            "aproxima con aritmetica de servilleta mas una medicion real de `curl` contra el "
            "contenedor local del lab, y la pregunta 1 exige declarar el limite de esa "
            "aproximacion."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "Escenario de carga del pico de su dominio",
                "tipo": "abierta",
                "puntos": 22,
                "respuesta": (
                    "**1. Evento del pico.** Lunes **21/09/2026**, primer dia de la semana de "
                    "parciales del Corte 1. La demanda se concentra porque los ejemplares de "
                    "bibliografia obligatoria se reservan casi todos ese dia: es el unico momento "
                    "del semestre en que la misma lista de veinte titulos la busca medio "
                    "programa a la vez.\n\n"
                    "**2. Usuarios concurrentes: 288.** Calculo: 2 400 estudiantes matriculados "
                    "con acceso a la biblioteca, de los cuales un **12 por ciento** entra dentro "
                    "de la misma ventana (2 400 x 0.12 = 288). El 12 por ciento no es un numero "
                    "inventado: es la proporcion de estudiantes que en el semestre anterior pidio "
                    "ejemplares de reserva en la semana de parciales, segun el conteo del "
                    "mostrador.\n\n"
                    "**3. Peticiones por segundo: 15.** Calculo: cada usuario concurrente lanza "
                    "una peticion cada **20 segundos** (busca, lee la ficha, decide, reserva), "
                    "asi que 288 / 20 = 14.4, que se redondea a **15 req/s** sostenidas. Es el "
                    "numero que la pregunta 3 usa como objetivo de capacidad.\n\n"
                    "**4. Mezcla de operaciones.** `GET /titulos` (busqueda) **62 por ciento**, "
                    "`GET /titulos/{isbn}` (ficha del titulo) **20 por ciento**, "
                    "`POST /titulos/{isbn}/reservas` **13 por ciento**, "
                    "`POST /prestamos/{id}/renovacion` **5 por ciento**. Suman **100**. La lectura "
                    "es el 82 por ciento del trafico, pero el 13 por ciento de escritura es el "
                    "que decide el diseno: es el unico que bloquea filas.\n\n"
                    "**5. Duracion de la ventana: 40 minutos**, de 11:40 a 12:20, entre el fin "
                    "del bloque de la manana y el inicio de los parciales de la tarde.\n\n"
                    "**6. Volumen de datos de partida.** **14 800 ejemplares** catalogados sobre "
                    "**9 200 titulos**, **6 300 prestamos historicos** y **240 reservas vivas** "
                    "al abrir la ventana.\n\n"
                    "**Frase de honestidad tecnica.** Este escenario no se va a medir con una "
                    "herramienta de carga: se aproxima con el calculo analitico de arriba mas una "
                    "medicion real de 20 peticiones con `curl -w \"%{time_total}\"` contra el "
                    "contenedor local del lab. **El limite de esa aproximacion es concreto y hay "
                    "que decirlo:** `curl` mide un solo usuario sin contencion, asi que no "
                    "reproduce lo que pasa cuando 288 sesiones compiten por la misma fila de "
                    "`ejemplares` con un bloqueo. El numero de la base de datos del presupuesto "
                    "de la pregunta 2 es por eso una estimacion con margen deliberado, no una "
                    "medicion; lo que si es medible hoy es la latencia sin carga, y eso es el "
                    "piso, no el pico."
                ),
                "como_calificar": [
                    "**10 pts** los 6 datos rotulados y presentes, en el orden del enunciado. "
                    "Son 1.67 pts cada uno; un dato sin rotulo, escondido en un parrafo, no "
                    "suma: el rotulo es lo que hace la tabla auditable.",
                    "**5 pts** que usuarios concurrentes **y** peticiones por segundo traigan el "
                    "calculo que los sustenta, con las dos cifras de entrada visibles (poblacion "
                    "y porcentaje; concurrentes y tiempo entre peticiones). Un numero solo, sin "
                    "operacion, vale 0 de estos 5 aunque sea razonable.",
                    "**4 pts** que la mezcla sume exactamente 100. Se suma con calculadora al "
                    "calificar: es el chequeo mas rapido del taller y falla mas de lo que "
                    "parece.",
                    "**3 pts** la frase de honestidad tecnica **con el limite** de la "
                    "aproximacion. Decir «mediremos con curl» sin decir que curl no reproduce "
                    "contencion vale la mitad.",
                    "Se acepta cualquier evento de pico con fecha real del calendario del "
                    "dominio del estudiante (matricula, entrega de notas, jornada de "
                    "vacunacion). Lo que se exige es la fecha y la razon por la que ese dia "
                    "concentra demanda.",
                ],
                "errores": [
                    "**Numeros redondos sin origen** (1 000 usuarios, 100 req/s). Se detecta "
                    "porque no hay operacion; y ademas suele producir un escenario que ningun "
                    "proyecto academico puede sostener. Devolver pidiendo la poblacion real del "
                    "dominio y un porcentaje justificado.",
                    "**Mezcla que suma 95 o 110.** Cuesta los 4 pts completos. Si el estudiante "
                    "esta en el taller, se le dice y corrige en el momento: el objetivo es que "
                    "aprenda a sumarla, no penalizarlo.",
                    "**Confundir usuarios concurrentes con usuarios totales.** 2 400 "
                    "matriculados no son 2 400 concurrentes; la diferencia es el porcentaje "
                    "simultaneo, y es justo la parte que exige pensar.",
                    "**Peticiones por segundo derivadas de la nada** cuando ya hay usuarios "
                    "concurrentes. El puente es el tiempo entre peticiones de un usuario; sin "
                    "ese dato el calculo no cierra.",
                    "**Frase de honestidad que es una disculpa** («no pudimos medir bien porque "
                    "no tenemos servidor»). No es una disculpa: es declarar el metodo y su "
                    "limite. Reescribirla en una linea con el estudiante.",
                ],
            },
            {
                "n": 2,
                "titulo": "Presupuesto de latencia del camino critico",
                "tipo": "diagrama",
                "puntos": 18,
                "respuesta_mermaid": """sequenceDiagram
    autonumber
    participant N as Navegador
    participant E as Edge / balanceador
    participant A as API de prestamos
    participant D as Base de datos de prestamos
    participant Q as Cola de avisos
    Note over N,Q: Objetivo p95 de POST /titulos/:isbn/reservas igual a 800 ms en el pico del 21/09/2026
    N->>E: POST /titulos/:isbn/reservas
    Note right of E: Terminacion TLS y proxy - 45 ms
    E->>A: POST interno en 3000
    Note right of A: Validacion del token con cache de claves del IdP - 55 ms
    A->>D: SELECT del ejemplar disponible FOR UPDATE
    D-->>A: Fila del ejemplar bloqueada
    Note right of D: Lectura con indice por isbn y estado - 110 ms
    A->>D: INSERT de la reserva y commit
    D-->>A: Commit confirmado
    Note right of D: Escritura y commit - 330 ms cuello de botella
    A->>Q: XADD del evento prestamo_por_vencer
    Note right of Q: Publicacion asincrona sin esperar al correo - 20 ms
    A-->>E: 201 Created con el id de la reserva
    Note right of A: Serializacion de la respuesta - 25 ms
    E-->>N: 201 Created
    Note over N,Q: Suma de tramos 585 ms sobre 800 ms - margen de 215 ms""",
                "respuesta": (
                    "**La aritmetica, que es lo que se verifica a mano:** "
                    "45 + 55 + 110 + 330 + 20 + 25 = **585 ms**, sobre un objetivo de **800 ms**, "
                    "**margen de 215 ms**. Seis notas de milisegundos, una por salto; cinco "
                    "participantes con los nombres canonicos de la pregunta 2 de la Clase 11.\n\n"
                    "**Por que el objetivo es 800 ms y no los 400 de la Clase 8.** Es la "
                    "pregunta que el docente debe poder responder sin dudar, porque parece una "
                    "contradiccion y no lo es. La tabla de senales de la Clase 8 fijo "
                    "**p95 por debajo de 400 ms** para el trafico general, que es el 82 por "
                    "ciento de lecturas de la pregunta 1, y **alerta a los 800 ms**. La "
                    "operacion de escritura tiene su propio presupuesto, mas holgado, porque "
                    "hace dos viajes a la base y uno de ellos con la fila bloqueada. El paquete "
                    "queda coherente si el informe dice las dos cosas: 400 ms para "
                    "`GET /titulos`, 800 ms para `POST /titulos/:isbn/reservas`. Un solo numero "
                    "para todo el sistema es lo que produce objetivos que nadie cumple.\n\n"
                    "**Por que el cuello esta en el commit y no en otra parte.** El `INSERT` con "
                    "su commit se lleva **330 de los 585 ms, el 56 por ciento del camino "
                    "critico**, y es el unico salto que ocurre con la fila ya bloqueada por el "
                    "`FOR UPDATE` del salto anterior. Eso significa que con 288 sesiones el "
                    "tiempo no se mantiene: se serializa, y ese salto es el que decide si el "
                    "pico se sostiene. Es exactamente el insumo de la pregunta 4.\n\n"
                    "**Los 20 ms de la cola son el rendimiento del trabajo de la Clase 11.** "
                    "Antes de que existiera la `Cola de avisos`, este camino terminaba cuando el "
                    "`Correo transaccional SaaS` respondia: una llamada a un tercero por "
                    "internet, que en el peor caso son cientos de milisegundos y en el caso malo "
                    "es un timeout. Publicar en la cola cuesta 20 ms y saca al correo del camino "
                    "critico. La decision de arquitectura de la Clase 11 se ve aqui como un "
                    "numero, y eso es lo que hay que hacer notar en voz alta.\n\n"
                    "**El margen de 215 ms es deliberado.** No es tiempo sobrante: es el colchon "
                    "para lo que el `curl` sin contencion no puede medir (la espera en el pool de "
                    "conexiones y la serializacion de los bloqueos en el pico). Un presupuesto "
                    "que suma exactamente el objetivo es un presupuesto que ya se incumplio."
                ),
                "como_calificar": [
                    "**6 pts** los 5 participantes con nombres canonicos del paquete y el flujo "
                    "completo de la operacion de escritura, ida y vuelta. Un participante con "
                    "nombre generico (`Servidor`, `BD`) pierde su parte: la trazabilidad con el "
                    "C4 Container es el punto.",
                    "**6 pts** una nota de milisegundos por salto. Se cuentan las notas y se "
                    "cuentan los saltos: si hay siete saltos y cinco notas, se descuenta "
                    "proporcionalmente.",
                    "**4 pts** que la suma sea **menor o igual** al objetivo y que el margen de "
                    "la nota final sea **exactamente** la diferencia. Se suma a mano al "
                    "calificar; una suma que no cuadra cuesta los 4 completos, incluso si el "
                    "diagrama es bueno, porque el ejercicio era precisamente sumar.",
                    "**2 pts** el cuello de botella rotulado con la palabra en la nota del salto "
                    "correspondiente.",
                    "Se acepta cualquier reparto de milisegundos que sea defendible en voz alta: "
                    "no hay una respuesta unica. Lo que no se acepta es un reparto plano (todos "
                    "los saltos con el mismo numero), que revela que no se penso donde esta el "
                    "trabajo real.",
                    "Se acepta que un estudiante fije un objetivo distinto de 800 ms si lo "
                    "justifica y lo deja coherente con su tabla de senales de la Clase 8. Lo que "
                    "se exige es que los dos documentos digan lo mismo.",
                ],
                "errores": [
                    "**Suma que excede el objetivo.** Es el error que la verificacion del "
                    "enunciado persigue: si los tramos suman 900 sobre un objetivo de 800, el "
                    "presupuesto declara por escrito que la operacion no cumple. Devolver para "
                    "que ajuste el reparto o suba el objetivo con justificacion.",
                    "**Margen calculado al ojo** (suma 585, objetivo 800, margen «unos 200»). "
                    "Cuesta parte de los 4 pts: el margen es una resta, no una impresion.",
                    "**Cuatro o seis participantes.** El enunciado pide 5. Falta tipicamente la "
                    "cola, porque el estudiante todavia piensa el sistema como el de la Clase 4; "
                    "es la senal de que el trabajo de la Clase 11 no se propago.",
                    "**El correo como quinto participante en lugar de la cola.** Renderiza "
                    "igual, pero deja al tercero dentro del camino critico y contradice la "
                    "decision de la Clase 11. Vale senalarlo aunque el diagrama este bien "
                    "formado: es material del Q&A.",
                    "**Sin `autonumber`.** Parece cosmetico y no lo es: sin numeros de salto la "
                    "parte A de la pregunta 4 no puede citar «el salto 8-9». Se pide agregarlo "
                    "en el momento.",
                    "**Notas de milisegundos sin unidad** (`330` en vez de `330 ms`). Se acepta "
                    "con observacion la primera vez; en el paquete final debe llevar unidad.",
                ],
            },
            {
                "n": 3,
                "titulo": "Tres metricas objetivo verificables",
                "tipo": "abierta",
                "puntos": 18,
                "tabla": {
                    "headers": ["Metrica", "Objetivo con numero y ventana", "Como se mide",
                                "Que pasa si no se cumple"],
                    "rows": [
                        ["Latencia",
                         "p95 de `POST /titulos/:isbn/reservas` **por debajo de 800 ms**, medido "
                         "en ventanas de 5 minutos durante los 40 de la ventana del pico "
                         "(`GET /titulos` mantiene el objetivo de 400 ms de la Clase 8)",
                         "20 peticiones con `curl -w \"%{time_total}\"` contra el contenedor del "
                         "lab, ordenadas de mayor a menor: el percentil 95 de 20 muestras es la "
                         "segunda peor. Cuando exista el edge, el log de acceso da la serie "
                         "completa",
                         "Se agrega el indice compuesto por `(isbn, estado)` sobre `ejemplares`, "
                         "que es lo que sostiene el `SELECT ... FOR UPDATE` de 110 ms; si aun no "
                         "alcanza, se aplica la mitigacion estructural de la pregunta 4"],
                        ["Tasa de error",
                         "**5xx por debajo del 0.5 por ciento** de las peticiones en ventanas de "
                         "5 minutos. Los **409** de doble reserva se cuentan aparte y no son "
                         "error: son la regla de negocio funcionando, con umbral de revision en "
                         "el 5 por ciento",
                         "Conteo de codigos de estado en la salida del script de 20 peticiones y "
                         "en `docker logs api-prestamos`, que ya imprime metodo, ruta y estado "
                         "por linea",
                         "Si el 5xx sube, se baja el pool de 20 a 12 conexiones para que la "
                         "espera se vea como latencia y no como error, y se agrega reintento con "
                         "espera en el cliente. Si los 409 pasan del 5 por ciento **no se toca la "
                         "base**: se corrige la interfaz, que esta ofreciendo ejemplares ya "
                         "reservados"],
                        ["Capacidad",
                         "**15 peticiones por segundo sostenidas** durante los 40 minutos de la "
                         "ventana, con la latencia p95 dentro del objetivo de la primera fila",
                         "Calculo analitico del escenario de la pregunta 1 mas una corrida de 200 "
                         "peticiones secuenciales cronometradas en el lab, que da el techo de un "
                         "solo proceso sin contencion",
                         "Se pasa de 1 a 2 replicas de la API detras del edge —la API no guarda "
                         "estado, asi que se puede— **repartiendo el pool a 10 conexiones por "
                         "replica** para no exceder las 20 del motor. Si con eso no alcanza, el "
                         "limite ya no es la API sino la base, y eso es tema de la Clase 13"],
                    ],
                },
                "respuesta": (
                    "**Linea de cierre:** el promedio no sirve porque se puede cumplir mientras "
                    "el sistema falla. Con 99 peticiones de 100 ms y una de 4 000 ms el promedio "
                    "es 139 ms —parece excelente— y sin embargo hubo un estudiante esperando "
                    "cuatro segundos frente a la pantalla. El p95 dice algo verificable y "
                    "rompible: «1 de cada 20 estudiantes puede esperar mas de 800 ms, ninguno "
                    "mas». Un objetivo que no se puede incumplir no es un objetivo.\n\n"
                    "Dos detalles de esta tabla que valen mas que las cifras:\n\n"
                    "**La fuente de medicion existe hoy.** No dice «Prometheus» ni «un APM»: dice "
                    "`curl` y `docker logs`, que son las dos cosas que el proyecto ya tiene. Es "
                    "la misma honestidad tecnica de la pregunta 1, y es lo que hace la fila "
                    "verificable en la sustentacion, donde el docente puede pedir la corrida en "
                    "vivo.\n\n"
                    "**La columna de la derecha son decisiones, no quejas.** «Se agrega el indice "
                    "por `(isbn, estado)`», «se baja el pool a 12», «se pasa a 2 replicas con 10 "
                    "conexiones cada una». Cada una nombra el artefacto que se edita. Y la fila "
                    "del 409 dice explicitamente que **no** se toca la base: cuando la regla de "
                    "negocio dispara mucho, el problema casi siempre esta en la interfaz que "
                    "ofrece lo que no puede dar."
                ),
                "como_calificar": [
                    "**7 pts** las 3 filas con los 3 tipos de metrica —latencia, tasa de error y "
                    "capacidad— y las 4 columnas. Tres filas de latencia con nombres distintos "
                    "valen una sola: los tipos son los que manda el enunciado.",
                    "**5 pts** que los 3 objetivos traigan **numero y ventana de medicion**. "
                    "`p95 por debajo de 800 ms` sin ventana vale la mitad de su parte; `rapido`, "
                    "`bueno` o `aceptable` valen 0 en esa fila, sin negociacion.",
                    "**4 pts** que la fuente de medicion exista realmente en el proyecto. Se "
                    "verifica preguntando «muestremela»: si nombra una herramienta que nadie "
                    "instalo, no suma. `curl`, `docker logs`, el cronometro del celular y la "
                    "salida de una prueba del lab son fuentes validas.",
                    "**2 pts** que las 3 filas cierren con una decision de arquitectura y no con "
                    "una queja. «Optimizar la consulta» es una queja; «agregar indice por "
                    "`(isbn, estado)`» es una decision.",
                    "Se acepta que el estudiante cuente aparte los errores de negocio (409, 422) "
                    "de los 5xx: es lo correcto y conviene reconocerlo en voz alta, porque "
                    "mezclarlos es el error que hace que la tabla no sirva.",
                ],
                "errores": [
                    "**Objetivos sin ventana.** «p95 menor a 800 ms» a secas: ¿medido cuando, "
                    "sobre cuantas peticiones? Sin ventana no hay como declarar cumplimiento ni "
                    "incumplimiento. Es el descuento mas frecuente de la pregunta.",
                    "**Nombrar Prometheus, Grafana o New Relic sin tenerlos.** Suena bien y no "
                    "es verificable. Devolver a la fuente real: el proyecto tiene `curl` y "
                    "logs, y con eso se puede sostener las tres filas.",
                    "**Contar los 409 como errores.** Hace que el sistema parezca roto justo "
                    "cuando la regla de negocio funciona, y ademas invita a la mitigacion "
                    "equivocada (quitar el bloqueo). Corregir siempre, aunque la fila este bien "
                    "formada.",
                    "**Usar el promedio como objetivo** y descubrirlo solo en la linea de "
                    "cierre. Si la fila de latencia dice «promedio menor a 400 ms», la linea de "
                    "cierre se contradice con la tabla: se devuelve para que las dos digan lo "
                    "mismo.",
                    "**Tercera fila que repite la latencia.** Capacidad es peticiones por "
                    "segundo sostenidas, y viene calculada de la pregunta 1: si el estudiante no "
                    "la conecta con su propio escenario, la fila queda huerfana.",
                ],
            },
            {
                "n": 4,
                "titulo": "Cuello de botella y dos mitigaciones",
                "tipo": "abierta",
                "puntos": 15,
                "respuesta": (
                    "**Parte A. El cuello de botella.** El `INSERT` de la reserva con su commit "
                    "en la `Base de datos de prestamos`: **330 ms de los 585** del camino "
                    "critico, el **56 por ciento del presupuesto en una sola pieza**. Como lo se: "
                    "es el salto 8-9 del diagrama de la pregunta 2, la nota "
                    "`Escritura y commit - 330 ms`. Y hay un segundo argumento que importa mas "
                    "que el numero: es el unico salto que ocurre **con la fila ya bloqueada** por "
                    "el `SELECT ... FOR UPDATE` del salto 6-7, asi que con 288 sesiones "
                    "concurrentes esos 330 ms no se mantienen constantes: **se serializan**. El "
                    "cuello no es solo el mas lento, es el que no escala con la concurrencia.\n\n"
                    "**Parte B, mitigacion 1 (estructural).**\n\n"
                    "1. **Mitigacion:** reemplazar el bloqueo pesimista por una **restriccion "
                    "unica parcial** sobre `(id_ejemplar)` donde `estado = 'reservado'`, y hacer "
                    "la reserva con un solo `INSERT ... ON CONFLICT DO NOTHING`: si no inserta "
                    "fila, el `Servicio de reservas` devuelve el **409** que ya esta en el "
                    "contrato de la Clase 4.\n"
                    "2. **Efecto esperado:** desaparece el viaje de lectura bloqueante (110 ms) y "
                    "el commit se acorta porque la transaccion pasa de dos sentencias a una. Se "
                    "espera recuperar **unos 150 ms de los 440** que hoy consumen los dos saltos "
                    "de base, y sobre todo que la seccion critica dure lo que dura un `INSERT` y "
                    "no lo que dura una ida y vuelta de aplicacion.\n"
                    "3. **Costo o riesgo:** la regla de no-doble-reserva deja de estar en codigo "
                    "legible y pasa a vivir en una restriccion de la base; hay que mantener el "
                    "indice parcial unico y traducir el error del motor a un 409 en la capa de "
                    "servicio, que es una linea facil de olvidar en un `catch` generico.\n"
                    "4. **Trade-off:** acepto que la regla de negocio principal quede menos "
                    "visible en el codigo para conseguir un camino critico de una sola escritura "
                    "y sin bloqueo explicito.\n\n"
                    "**Parte B, mitigacion 2 (de capacidad).**\n\n"
                    "1. **Mitigacion:** pasar de 1 a **2 replicas de la `API de prestamos`** "
                    "detras del edge y repartir el pool de conexiones a **10 por replica**, para "
                    "no exceder las 20 del motor.\n"
                    "2. **Efecto esperado:** no baja la latencia de una peticion aislada —el "
                    "commit sigue costando 330 ms— pero **sostiene las 15 req/s sin que el p95 se "
                    "degrade por espera en el pool**. Recupera el margen que hoy se pierde cuando "
                    "el pool llega a 16 de 20 conexiones, que es el umbral de la tabla de senales "
                    "de la Clase 8.\n"
                    "3. **Costo o riesgo:** duplica las horas encendidas de la fila mas cara de "
                    "la tabla de costos de la Clase 10, que ya estaba en nivel **A**; agrega una "
                    "pieza al despliegue; y tiene un techo duro, porque el motor **no** escala "
                    "con las replicas de la API (es la opcion falsa de la pregunta 6 y el tema "
                    "central de la Clase 13).\n"
                    "4. **Trade-off:** acepto duplicar las horas de computo de la pieza mas cara "
                    "para conseguir que la ventana de 40 minutos no degrade el p95.\n\n"
                    "**Parte C. La mitigacion que no aplicaria.** No cachearia la disponibilidad "
                    "de los ejemplares con un TTL de un minuto, aunque sea la optimizacion mas "
                    "barata del catalogo. Romperia el PI porque la disponibilidad es "
                    "**precisamente el dato que decide si hay doble reserva**: con un cache de "
                    "sesenta segundos, en el pico se ofreceria como disponible un ejemplar ya "
                    "reservado, el 409 pasaria de excepcion a respuesta habitual y la capacidad "
                    "«reservar ejemplar» de la ficha de la Clase 1 dejaria de cumplirse. Cachear "
                    "el resultado de `GET /titulos` si; el estado de un ejemplar, no."
                ),
                "como_calificar": [
                    "**5 pts** el cuello nombrado en una frase **y** respaldado con el salto "
                    "exacto del diagrama y su cantidad de milisegundos. Nombrarlo sin citar el "
                    "salto vale 2; citar el salto equivocado (uno que no es el mayor) vale 0, "
                    "porque el ejercicio era leer el propio presupuesto.",
                    "**6 pts** las 2 mitigaciones con sus **4 lineas rotuladas** (mitigacion, "
                    "efecto esperado, costo o riesgo, trade-off). Son 3 pts cada una, 0.75 por "
                    "linea. Una linea de trade-off que no tiene la forma «acepto X para conseguir "
                    "Y» no suma: la forma es el contenido.",
                    "**3 pts** que una sea estructural y la otra de capacidad. Dos estructurales "
                    "valen 1.5: el punto del ejercicio es que el estudiante distinga cambiar el "
                    "diseno de comprar mas maquina.",
                    "**1 pt** la parte C, con la razon por la que romperia el PI. Nombrar una "
                    "mitigacion absurda («no usaria mainframe») no suma: tiene que ser una "
                    "tentacion real y mal aplicada.",
                    "Se acepta cualquier efecto esperado en milisegundos o porcentaje, aunque sea "
                    "optimista, si esta razonado. Lo que no se acepta es «mejoraria mucho»: sin "
                    "cifra no hay como saber despues si la mitigacion sirvio.",
                ],
                "errores": [
                    "**Cuello de botella declarado sin mirar el diagrama** («la base de datos»). "
                    "Es probablemente cierto y vale poco: el enunciado pide el salto y los "
                    "milisegundos. Devolver al diagrama de la pregunta 2.",
                    "**Dos mitigaciones de capacidad** (mas replicas y un nodo mas grande). "
                    "Cuesta la mitad de los 3 pts del reparto y suele significar que el "
                    "estudiante no ve que el diseno se puede cambiar sin gastar mas.",
                    "**Costo o riesgo en blanco, o «ninguno».** Toda mitigacion cuesta algo; si "
                    "no se ve el costo, no se entendio la mitigacion. Es la linea que mas "
                    "distingue una respuesta pensada.",
                    "**Trade-off que es un resumen** («esta mitigacion es buena porque mejora el "
                    "rendimiento»). Se pide la forma «acepto X para conseguir Y», con X un costo "
                    "real. Reescribirla en el momento cuesta treinta segundos.",
                    "**Proponer microservicios como mitigacion.** Contradice el ADR-001 y la "
                    "Clase 4 sin evidencia nueva, y ademas agrega saltos de red a un camino "
                    "critico que ya tiene el cuello en el commit. Devolver a la tabla de riesgos "
                    "de la Clase 4.",
                    "**Parte C que descarta la mitigacion obvia** («no agregaria un indice "
                    "porque cuesta»). El indice es la mitigacion correcta; lo que hay que "
                    "descartar es lo que rompe una capacidad de la ficha.",
                ],
            },
            {
                "n": 5,
                "titulo": "Guion cronometrado del pitch",
                "tipo": "abierta",
                "puntos": 17,
                "tabla": {
                    "headers": ["Minuto", "Seccion", "Quien habla",
                                "Mensaje clave en una frase", "Evidencia en pantalla"],
                    "rows": [
                        ["0:00 a 1:00", "Problema y dominio", "Autor del paquete",
                         "La biblioteca reserva dos veces el mismo ejemplar y avisa tarde de los "
                         "vencimientos: BiblioLite resuelve consultar, reservar, renovar y avisar",
                         "Ficha de dominio con las 4 capacidades y el C4 Context renderizado"],
                        ["1:00 a 2:30", "Arquitectura logica", "Autor del paquete",
                         "Cinco contenedores y un monolito modular: la decision fue **no** "
                         "distribuir, y esta escrita con su fecha en el ADR-001",
                         "C4 Container renderizado y el ADR-001 abierto en la seccion de decision"],
                        ["2:30 a 3:45", "Contenedor y pipeline", "Autor del paquete",
                         "La misma imagen corre la API y el procesador de avisos, y el pipeline "
                         "la construye y la verifica en cada push a main",
                         "`/docker/Dockerfile` y la captura del run verde de Actions"],
                        ["3:45 a 5:00", "Seguridad", "Autor del paquete",
                         "Cinco amenazas STRIDE, cada una senalada en una caja o una flecha, y "
                         "ningun secreto dentro de la imagen",
                         "Tabla STRIDE con la columna «donde se ve» y el paso del `ci.yml` que "
                         "falla si encuentra un `.env` en la imagen"],
                        ["5:00 a 6:15", "Costos y escalabilidad", "Autor del paquete",
                         "El costo se ordena por driver y no por precio: la API se paga por horas "
                         "encendidas, y por eso escala a cero de 22:00 a 06:00",
                         "Tabla de costos con niveles B/M/A y la fila del presupuesto de latencia "
                         "de hoy"],
                        ["6:15 a 7:00", "Cierre y preguntas", "Autor del paquete",
                         "Lo que falta esta en un backlog con fechas y lo que decidimos no hacer "
                         "esta escrito como deuda aceptada",
                         "Backlog B-01 a B-05 y la linea de deuda tecnica del checkpoint"],
                    ],
                },
                "respuesta": (
                    "**Tiempos reales cronometrados.** `ensayo 1: 9:12` · `ensayo 2: 7:35` · "
                    "`ensayo 3: 6:58`.\n\n"
                    "**Lo que se recorto para entrar en el tiempo (2:14 del primer ensayo):** se "
                    "elimino la lectura del ADR-001 completo —queda abierto en pantalla y se cita "
                    "una sola linea, la de la decision—, se paso de explicar las seis categorias "
                    "de STRIDE a mostrar solo las cinco amenazas propias, y la demo en vivo del "
                    "`docker run` se reemplazo por la captura ya tomada, que era el minuto mas "
                    "riesgoso del pitch.\n\n"
                    "**El reparto suma 7:00, dentro de los 5 a 8 minutos**, y ninguna seccion "
                    "pasa de 1:30. Eso ultimo no es un detalle de forma: una seccion de tres "
                    "minutos significa que el resto del sistema se cuenta a las carreras, y es lo "
                    "que produce pitches donde la arquitectura se explica bien y los costos no se "
                    "alcanzan a mencionar. El bloque mas largo es el de arquitectura logica, que "
                    "es el que sostiene el «por que»; el mas corto es el cierre, que solo tiene "
                    "que dejar dos artefactos en pantalla.\n\n"
                    "**Cada fila cita un artefacto que existe en el paquete v1.** Ninguna dice "
                    "«diapositiva de seguridad»: dicen tabla STRIDE, run verde, Dockerfile, "
                    "backlog. Esa columna es la que convierte el guion en un ensayo verificable, "
                    "porque el docente puede pedir cualquiera de los seis artefactos en el "
                    "momento y debe estar a un clic.\n\n"
                    "**Sobre la columna «Quien habla»:** en este documento dice «Autor del "
                    "paquete» porque es material docente. En la entrega real va **el nombre del "
                    "estudiante**; y si el docente autorizo equipo, van todos los integrantes, "
                    "ninguno con mas de tres filas."
                ),
                "como_calificar": [
                    "**7 pts** las 6 filas con las 6 secciones en el orden del enunciado "
                    "(problema y dominio, arquitectura logica, contenedor y pipeline, seguridad, "
                    "costos y escalabilidad, cierre y preguntas) y las 5 columnas. Una seccion "
                    "fuera de orden se observa pero no descuenta; una seccion ausente si.",
                    "**4 pts** que los minutos sumen entre 5 y 8 **y** que ninguna seccion pase "
                    "de 2:00. Los rangos se suman al calificar: es la verificacion de treinta "
                    "segundos. En equipo autorizado, ademas, deben aparecer todos los "
                    "integrantes y ninguno con mas de 3 filas.",
                    "**4 pts** que cada fila cite un artefacto concreto del paquete. «Slide de "
                    "seguridad» no es artefacto; «tabla STRIDE» si. Se reparte a 0.67 pts por "
                    "fila.",
                    "**2 pts** los 2 tiempos de ensayo cronometrados **y** la linea de recorte. "
                    "Un solo ensayo vale 1; ensayos sin recorte declarado valen 1, porque el "
                    "aprendizaje del ejercicio esta en decidir que sale.",
                    "El indicador de que el ensayo fue real: el primer tiempo casi siempre pasa "
                    "de 8 minutos. Un estudiante que reporta 6:00 y 6:05 en los dos ensayos "
                    "probablemente no cronometro; preguntarle que recorto entre uno y otro "
                    "resuelve la duda sin acusar a nadie.",
                ],
                "errores": [
                    "**Guion que suma 12 minutos.** Cuesta los 4 pts del tiempo y, mas caro, "
                    "garantiza que en la Clase 15 el pitch se corte en la mitad de seguridad. Se "
                    "corrige en clase: se recorta con el estudiante en el momento.",
                    "**Una seccion de 3:00 y el resto de 0:30.** Es el reparto que el enunciado "
                    "prohibe con el techo de 2:00. Casi siempre la seccion larga es "
                    "arquitectura, porque es la mas comoda de contar.",
                    "**Evidencia en pantalla escrita como titulo de diapositiva.** El pitch se "
                    "sostiene mostrando artefactos, no vinetas. Pedir que cambie las seis celdas "
                    "por rutas del paquete.",
                    "**Tiempos de ensayo inventados.** Se detecta porque no hay recorte "
                    "declarado o porque los dos tiempos son casi iguales. Se pide cronometrar en "
                    "el momento: son siete minutos de clase y valen la pena.",
                    "**Mensaje clave que describe en vez de argumentar** («explicaremos la "
                    "arquitectura del sistema»). El mensaje clave es la frase que el jurado debe "
                    "recordar; si es una descripcion del orden del dia, no cumple.",
                    "**En equipo, un integrante con cinco filas y el otro con una.** El "
                    "enunciado pone techo de 3 filas por persona justamente para eso. Se "
                    "redistribuye antes de la Clase 15.",
                ],
            },
            {
                "n": 6,
                "titulo": "Rendimiento: que es cierto",
                "tipo": "cerrada_multi",
                "puntos": 10,
                "justificacion": {
                    0: "**Cierta.** Es la linea de cierre de la pregunta 3, con numeros: 99 "
                       "peticiones de 100 ms y una de 4 000 ms dan un promedio de 139 ms —que "
                       "parece excelente— mientras un estudiante espero cuatro segundos. El "
                       "promedio esconde la cola; el percentil la muestra.",
                    1: "**Cierta.** Es el criterio con el que se califica la pregunta 3: "
                       "«rapido» no se puede cumplir ni incumplir. Un objetivo verificable "
                       "necesita numero **y** ventana de medicion, porque sin ventana no hay "
                       "momento en el cual declarar el resultado.",
                    2: "**Falsa, y es la falsa mas importante del taller.** La base primaria no "
                       "escala con las replicas de la API: es una sola pieza que recibe mas "
                       "conexiones de las que tenia. Es exactamente el riesgo declarado en la "
                       "mitigacion 2 de la pregunta 4 (repartir el pool a 10 por replica para no "
                       "pasar de 20) y es el tema central de la Clase 13, «lo que NO escala». "
                       "Quien la marca perdio 4 pts y necesita ese repaso antes del 02/11.",
                    3: "**Cierta.** Un sistema que devuelve 500 en 40 ms tiene una latencia "
                       "envidiable y no sirve para nada. Por eso la tabla de la pregunta 3 tiene "
                       "una fila entera de tasa de error, con los 409 contados aparte.",
                    4: "**Falsa.** Es justamente el limite que la frase de honestidad tecnica de "
                       "la pregunta 1 obliga a declarar: tres usuarios en un portatil miden "
                       "latencia sin contencion, que es el piso. No reproducen 288 sesiones "
                       "compitiendo por la misma fila con un bloqueo. Medir asi esta bien; "
                       "concluir de ahi el comportamiento en el pico, no.",
                    5: "**Falsa.** A veces el cuello esta en el frontend, y muchas veces no: en "
                       "BiblioLite esta en el commit de la reserva, con 330 de 585 ms. La palabra "
                       "que hace falsa la afirmacion es «siempre»; el cuello se encuentra "
                       "midiendo, no por reputacion de la capa.",
                },
                "como_calificar": [
                    "**4 pts por cada afirmacion correcta marcada, con techo de 10.** Las tres "
                    "ciertas son las opciones 1, 2 y 4 tal como estan numeradas en la plataforma "
                    "(promedio contra p95, objetivo sin numero, tasa de error). La clave se lee "
                    "del banco, no de memoria.",
                    "**Se descuentan 4 pts por cada incorrecta marcada**, sin bajar de cero. "
                    "Marcar las seis da cero: conviene advertirlo antes de abrir la actividad.",
                    "Las tres falsas cubren tres confusiones distintas y vale la pena leer el "
                    "reporte por opcion: la base que escala sola (Clase 13), el portatil como "
                    "prueba de carga (pregunta 1) y el frontend culpable por defecto (pregunta "
                    "4). No son ruido de relleno.",
                    "Si mas de la mitad del grupo marca la opcion de la base que escala sola, la "
                    "Clase 13 debe abrir por ahi: es la mitad del entregable de esa clase y la "
                    "confusion mas costosa del corte.",
                ],
                "errores": [
                    "**Marcar las seis.** El descuento lo deja en cero. Es la unica pregunta "
                    "autocalificada del taller y la unica donde marcar de mas cuesta.",
                    "**Marcar la opcion de la base que escala sola** porque «horizontal es "
                    "mejor». Escalar la API es facil precisamente porque no guarda estado; la "
                    "base guarda estado y ahi esta toda la dificultad.",
                    "**Descartar la opcion de la tasa de error** por parecer obvia. Es cierta y "
                    "vale 4 pts; el reflejo de «esta demasiado facil, debe ser trampa» cuesta "
                    "puntos todos los semestres.",
                    "**Marcar la del frontend** despues de haber escrito en la pregunta 4 que su "
                    "cuello esta en la base. Es la contradiccion interna mas facil de senalar y "
                    "la mas util para el estudiante.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("No tengo herramienta de carga ni servidor. ¿Como mido 15 peticiones por segundo?",
             "No las mide: las **calcula** y lo declara. La pregunta 1 pide justamente eso, y la "
             "frase de honestidad tecnica es donde se dice el limite. Lo que si se mide hoy es la "
             "latencia de una peticion con `curl -w \"%{time_total}\"` contra el contenedor del "
             "lab, veinte veces. Eso da el piso real; el pico se estima."),
            ("¿Por que el objetivo de la escritura es 800 ms si en la Clase 8 puse 400?",
             "Porque son dos caminos distintos. Los 400 ms son para las lecturas, que son el 82 "
             "por ciento del trafico; la escritura hace dos viajes a la base y uno con la fila "
             "bloqueada, asi que tiene su propio presupuesto. Lo que se exige es que el informe "
             "diga las dos cifras y a que operacion aplica cada una."),
            ("¿El percentil 95 se puede calcular con 20 mediciones?",
             "De forma aproximada, si: se ordenan de mayor a menor y el p95 de 20 muestras es la "
             "segunda peor. Con 20 datos el numero es grueso y hay que decirlo, pero es "
             "infinitamente mejor que un promedio. Con 100 mediciones ya es razonable."),
            ("Mi presupuesto de latencia suma mas que el objetivo. ¿Subo el objetivo?",
             "Puede, si lo justifica y ajusta la tabla de senales para que digan lo mismo. Pero "
             "primero mire el reparto: si un salto se lleva mas de la mitad, ahi esta su cuello "
             "de botella y la pregunta 4 se responde sola. Un presupuesto que no cuadra es un "
             "hallazgo, no un error de forma."),
            ("¿Puedo poner cache como una de las dos mitigaciones?",
             "Como estructural, si —siempre que sea cache de **lecturas**, tipo "
             "`GET /titulos`—. Lo que no se acepta es cachear el dato que decide la regla de "
             "negocio: la disponibilidad de un ejemplar cacheada un minuto convierte el 409 en la "
             "respuesta normal del pico. Ese es el ejemplo de la parte C."),
            ("¿El ensayo del pitch cuenta si lo hice solo, en la casa?",
             "Cuenta si esta cronometrado y si declara el recorte. Lo que se califica son los dos "
             "tiempos y la decision de que sacar, no el publico. Dicho eso, el ensayo de hoy en "
             "clase es el que sirve de verdad: en voz alta y con alguien mirando, el tiempo "
             "siempre es mayor."),
            ("Somos equipo. ¿Como reparto las seis filas?",
             "Con el techo del enunciado: ninguno mas de tres filas y todos deben aparecer. La "
             "reparticion que funciona es por bloques tematicos, no alternando frases: quien "
             "escribio el ADR cuenta arquitectura, quien armo el pipeline cuenta contenedor y "
             "CI. Cambiar de voz en mitad de un tema cuesta tiempo y coherencia."),
            ("¿Tengo que mostrar la demo en vivo en el pitch?",
             "No, y normalmente conviene que no. Cinco a ocho minutos no dan para que algo se "
             "cuelgue: la captura del run verde y el `docker ps` ya tomados prueban lo mismo sin "
             "el riesgo. Fue justo lo que se recorto entre el ensayo 1 y el 2 de esta solucion."),
        ],
        "cierre": (
            "Lo que queda de hoy es que el sistema pasa de «funciona» a «funciona dentro de un "
            "numero»: 15 peticiones por segundo durante 40 minutos, p95 de 800 ms en la escritura "
            "y 400 en la lectura, 5xx por debajo del 0.5 por ciento, y un cuello de botella "
            "identificado con su salto y sus 330 ms. Las dos cosas que hay que llevar a la Clase "
            "13 son ese cuello y el riesgo de la mitigacion de capacidad: la API se puede replicar "
            "porque no guarda estado, pero la base no escala con ella, y esa frase es literalmente "
            "la mitad del entregable de la clase autonoma del 02/11. Y del lado del pitch queda un "
            "guion de 7:00 con seis artefactos en pantalla, que es lo que se sustenta el 16/11: "
            "ensayarlo dos veces mas antes de esa fecha es la unica preparacion que hace "
            "diferencia."
        ),
    },

    13: {
        "titulo": "Solucion del Taller Clase 13 - Politica de autoescalado (BiblioLite)",
        "resumen": (
            "Taller propio de 100 puntos en cinco preguntas, de la clase autonoma del "
            "02/11/2026. La politica se escribe componente por componente con disparadores "
            "numericos, minimos, maximos y enfriamiento; se dibuja como maquina de decision que "
            "cierra el ciclo; se declara con nombre y razon tecnica lo que **no** escala —y ahi "
            "esta el hallazgo de la clase: el maximo de replicas de la API no lo decide la API, "
            "lo decide el limite de 20 conexiones del motor—; y se enlaza con la tabla de costos "
            "de la Clase 10 en tres escenarios."
        ),
        "total": 100,
        "nota_actividad": (
            "**Clase autonoma.** El 02/11/2026 es festivo y no hay sesion sincrona: el taller "
            "se resuelve en casa con el fundamento de la clase, que esta escrito para ser guia y "
            "material de estudio a la vez. **La politica es conceptual:** no se pide configurar "
            "un autoescalador real, ni abrir cuenta en ningun proveedor, ni tarjeta de credito. "
            "Lo que se califica es la tabla, el diagrama y los argumentos. Los numeros deben ser "
            "**los mismos** que el estudiante ya escribio en la Clase 12 (presupuesto de latencia) "
            "y en la Clase 8 (tabla de senales): la coherencia entre los tres documentos es la "
            "mitad de la nota."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "Politica de autoescalado de BiblioLite",
                "tipo": "abierta",
                "puntos": 30,
                "tabla": {
                    "headers": ["Componente", "Tipo de escala", "Disparador de subida",
                                "Disparador de bajada", "Minimo y maximo", "Enfriamiento"],
                    "rows": [
                        ["Edge / balanceador", "horizontal",
                         "conexiones concurrentes por encima de 400 durante 3 minutos, medidas en "
                         "el log de acceso del proxy",
                         "conexiones concurrentes por debajo de 120 durante 15 minutos",
                         "min 1 y max 2", "15 minutos"],
                        ["API de prestamos", "horizontal",
                         "p95 de `POST /titulos/:isbn/reservas` por encima de 800 ms **o** CPU por "
                         "encima del 70 por ciento, sostenido 3 minutos",
                         "p95 por debajo de 300 ms **y** CPU por debajo del 30 por ciento, "
                         "sostenido 10 minutos",
                         "min 1 y max 4 (4 replicas x 5 conexiones = las 20 del motor)",
                         "10 minutos"],
                        ["Procesador de avisos", "horizontal",
                         "profundidad de la `Cola de avisos` por encima de 500 mensajes durante 2 "
                         "minutos",
                         "profundidad por debajo de 50 mensajes durante 10 minutos",
                         "min 0 y max 3", "10 minutos"],
                        ["Base de datos de prestamos", "no escala",
                         "no aplica", "no aplica",
                         "capacidad fija: 1 primaria, 2 vCPU, 4 GB y **20 conexiones**",
                         "no aplica - solo cambia en ventana de mantenimiento anunciada"],
                        ["Cola de avisos", "vertical",
                         "memoria usada por encima del 75 por ciento de los 512 MB durante 10 "
                         "minutos",
                         "no aplica - el redimensionamiento a la baja se decide a mano en la "
                         "ventana de mantenimiento, nunca en automatico",
                         "capacidad fija de 1 instancia; de 512 MB a 1 GB en ventana de "
                         "mantenimiento",
                         "no aplica en automatico - 1 ventana por corte (unas 5 semanas)"],
                    ],
                },
                "respuesta": (
                    "**Linea de cierre:** el primero que escala cuando llega el pico es el "
                    "`Procesador de avisos`, porque su ventana de medicion es la mas corta de la "
                    "politica (2 minutos) y su cola acumula de inmediato; el ultimo es la "
                    "`Base de datos de prestamos`, que **no escala en absoluto** y que por eso le "
                    "impone su techo a todos los demas.\n\n"
                    "**El hallazgo de la clase, y hay que decirlo en voz alta: el maximo de la API "
                    "no lo decide la API.** Cada replica abre su propio pool de conexiones y el "
                    "motor acepta 20 en total. Con 5 conexiones por replica, el techo son "
                    "**4 replicas**, y ese numero no sale de la CPU de la API ni del trafico "
                    "esperado: sale de la unica pieza que no escala. Es la definicion operativa de "
                    "cuello de botella estructural, y es la respuesta que el jurado de la Clase 15 "
                    "va a buscar cuando pregunte «¿y si le llegan mil usuarios?».\n\n"
                    "**Por que el minimo de la API es 1 y no 2.** Con 2 replicas habria alta "
                    "disponibilidad: una se puede reiniciar sin cortar el servicio. Con 1, un "
                    "reinicio son unos 20 segundos de caida. Se elige 1 a proposito, porque la "
                    "tabla de costos de la Clase 10 dejo la fila de la API en nivel **A** por "
                    "horas encendidas y el apalancamiento declarado alli era bajar de 720 a 480 "
                    "horas al mes. Es una **deuda aceptada**, no un olvido, y asi debe quedar "
                    "escrita en el informe: se acepta una ventana de 20 segundos en los reinicios "
                    "para conseguir un tercio menos de horas encendidas.\n\n"
                    "**Por que el minimo del procesador de avisos es 0, y la trampa que eso "
                    "esconde.** Escalar a cero es el apalancamiento que la Clase 10 anoto para el "
                    "worker, y aqui se puede porque el aviso de vencimiento sale **dos dias antes** "
                    "de la fecha: un retraso de dos minutos es irrelevante para el negocio. Pero "
                    "hay un detalle que se le escapa a casi todo el mundo: **si el worker esta en "
                    "cero, no es el worker el que ve la cola**. La profundidad la observa el "
                    "orquestador, desde fuera. Si la metrica se midiera dentro del worker, con "
                    "cero replicas nadie miraria y los avisos no saldrian nunca.\n\n"
                    "**Por que los enfriamientos son largos, y el efecto secundario que hay que "
                    "aceptar.** La regla es que el enfriamiento no puede ser mas corto que la "
                    "ventana de medicion, o el sistema decide con datos que todavia esta "
                    "produciendo: sube, y antes de que la replica nueva reciba trafico ya volvio a "
                    "medir alto, y sube otra vez. De ahi los 10 minutos de la API, que igualan la "
                    "ventana de bajada. La consecuencia es incomoda y conviene calcularla: con "
                    "enfriamiento de 10 minutos y un pico de **40 minutos** (el del 21/09/2026 de "
                    "la Clase 12), la politica alcanza a subir de 1 a 4 replicas justo cuando el "
                    "pico esta terminando. Ese es el argumento tecnico para pre-escalar a mano "
                    "antes de las 11:40, y es exactamente lo que la pregunta 4 escribe como accion "
                    "de sostenibilidad."
                ),
                "como_calificar": [
                    "**10 pts** las 5 filas con los 5 componentes del C4 Deployment del "
                    "estudiante y los 6 campos llenos. 2 pts por fila. Los nombres deben ser los "
                    "canonicos de la Clase 11: una fila que diga «servidor» no suma.",
                    "**8 pts** que los disparadores lleven **metrica + umbral numerico + "
                    "ventana** en todas las filas que escalan. **Cero en la fila cuyo disparador "
                    "no tenga numero**, tal como lo anuncia el enunciado: es el descuento por "
                    "fila y no admite excepcion.",
                    "**6 pts** minimos y maximos con dos numeros concretos y sin infinitos. Se "
                    "acepta `min 0` para un procesador asincrono si el estudiante justifica la "
                    "tolerancia del negocio; no se acepta «segun demanda» ni «sin limite».",
                    "**4 pts** el enfriamiento coherente con la ventana: **nunca mas corto que la "
                    "ventana de medicion**. Es la verificacion aritmetica de la pregunta y se "
                    "hace comparando dos celdas de la misma fila.",
                    "**2 pts** la linea de cierre con el primero y el ultimo en escalar.",
                    "Al menos una fila debe ser `no escala`; si el estudiante marca dos (por "
                    "ejemplo base y cola) se acepta, siempre que la capacidad fija este escrita. "
                    "Cinco filas `no escala` no: eso no es una politica.",
                ],
                "errores": [
                    "**Disparadores sin ventana** («CPU por encima del 70 por ciento»). Es el "
                    "error mas frecuente y el mas caro, porque la fila entera se va a cero. Sin "
                    "ventana el sistema escala por un pico de un segundo y entra en oscilacion.",
                    "**`max: sin limite` o `max: segun se necesite`.** El enunciado lo prohibe "
                    "explicitamente. Un maximo abierto es como se producen las facturas de miles "
                    "de dolares que salen en las noticias, y en este curso ademas contradice la "
                    "restriccion de no usar cloud de pago.",
                    "**Enfriamiento de 30 segundos con ventana de 3 minutos.** Es la "
                    "incoherencia que la pregunta 5 pone como opcion falsa. Se detecta comparando "
                    "dos celdas; devolver para que iguale el enfriamiento a la ventana mas larga "
                    "de la fila.",
                    "**Ninguna fila `no escala`.** Casi siempre significa que el estudiante puso "
                    "la base de datos como `horizontal` para que la tabla quedara «completa». Es "
                    "el error conceptual central del tema y hay que corregirlo con la razon "
                    "tecnica, no con la regla del enunciado.",
                    "**Maximo de replicas elegido al azar** (`max 10`) cuando el motor acepta 20 "
                    "conexiones. No descuenta por si mismo si el numero esta escrito, pero deja "
                    "la pregunta 3 sin su mejor argumento: vale la pena senalarlo con la "
                    "aritmetica del pool.",
                    "**Metricas de disparo que el proyecto no puede observar** (latencia p99 "
                    "desde un APM que nadie instalo). Se pide lo mismo que en la Clase 12: la "
                    "fuente debe existir. `docker stats`, el log del proxy y la profundidad de la "
                    "cola son fuentes validas.",
                ],
            },
            {
                "n": 2,
                "titulo": "Maquina de decision del autoescalado",
                "tipo": "diagrama",
                "puntos": 25,
                "respuesta_mermaid": """flowchart TD
    obs["Observar cada 60 segundos el p95 de POST /titulos/:isbn/reservas la CPU de la API de prestamos y la profundidad de la Cola de avisos"]
    obs --> up{"p95 por encima de 800 ms o CPU por encima de 70 por ciento durante 3 minutos"}
    up -->|"Si"| out["Scale out - sumar 1 replica de la API de prestamos hasta el maximo de 4 replicas"]
    up -->|"No"| down{"p95 por debajo de 300 ms y CPU por debajo de 30 por ciento durante 10 minutos"}
    down -->|"Si"| inn["Scale in - retirar 1 replica de la API de prestamos hasta el minimo de 1 replica"]
    down -->|"No"| obs
    out --> cool["Enfriamiento de 10 minutos sin nuevas acciones de escalado"]
    inn --> cool
    cool --> obs
    noesc["No escala - Base de datos de prestamos primaria - 20 conexiones fijas que fijan el maximo de 4 replicas - solo escala vertical en ventana de mantenimiento"]
    noesc -.->|"limite del diseno"| obs""",
                "respuesta": (
                    "**Los seis elementos que pide el enunciado, senalados uno por uno:** el nodo "
                    "`obs` trae el **periodo de evaluacion** (60 segundos) y las tres metricas "
                    "observadas; `up` y `down` son los dos rombos con **los umbrales exactos de la "
                    "tabla de la pregunta 1** —800/70 con 3 minutos para subir, 300/30 con 10 "
                    "minutos para bajar—; `out` e `inn` llevan **su limite** (maximo de 4, minimo "
                    "de 1); `cool` es el enfriamiento de 10 minutos por el que pasan **las dos** "
                    "acciones; y `noesc` es lo que no escala, unido con **arista punteada** "
                    "rotulada `limite del diseno`.\n\n"
                    "**El ciclo cierra, y se puede recorrer con el dedo:** obs -> up -> (No) -> "
                    "down -> (No) -> obs es la vuelta en la que no pasa nada, que es la vuelta "
                    "normal. Las dos vueltas que actuan son obs -> up -> Si -> out -> cool -> obs "
                    "y obs -> up -> No -> down -> Si -> inn -> cool -> obs. Ningun camino termina "
                    "en un nodo sin salida: eso es lo que distingue una maquina de decision de un "
                    "dibujo de cajas.\n\n"
                    "**Por que el enfriamiento esta despues de las dos acciones y no solo del "
                    "scale out.** Es el detalle que se salta la mitad del grupo. La oscilacion "
                    "—subir, bajar, subir— aparece justo cuando la bajada no espera: se retira "
                    "una replica, el p95 sube porque las que quedan reciben mas trafico, y a los "
                    "60 segundos el rombo de subida dice que hay que sumar otra. Un enfriamiento "
                    "que solo aplica a la subida no evita nada.\n\n"
                    "**Por que la arista de `noesc` es punteada y va a `obs`.** No es un paso del "
                    "ciclo: es una **restriccion** sobre el ciclo. La base de datos no participa "
                    "de la decision —nunca se le suma ni se le quita nada— pero condiciona el "
                    "limite del nodo `out`: el maximo de 4 esta ahi por sus 20 conexiones. La "
                    "arista punteada dice exactamente eso, «esto no fluye, esto limita», y es la "
                    "unica forma de que la restriccion quede en el diagrama sin mentir sobre el "
                    "flujo.\n\n"
                    "**Sobre el procesador de avisos.** Tiene su propio ciclo, de la misma forma, "
                    "con la profundidad de la cola como metrica, 500/2 minutos para subir, 50/10 "
                    "para bajar y minimo 0. Se deja fuera de esta lamina a proposito: dibujar los "
                    "dos ciclos duplica los nodos sin agregar una idea nueva, y el enunciado pide "
                    "**el** ciclo de decision. Si un estudiante dibuja los dos y se entiende, se "
                    "acepta sin objecion."
                ),
                "como_calificar": [
                    "**8 pts** el nodo de observacion con **periodo y metricas** y los 2 rombos "
                    "con **umbrales numericos**. Los numeros del diagrama deben ser identicos a "
                    "los de la tabla de la pregunta 1: se comparan celda por celda y una "
                    "discrepancia descuenta, porque el ejercicio es la coherencia.",
                    "**6 pts** los nodos de scale out y scale in **con su limite** escrito en la "
                    "etiqueta («hasta el maximo de 4», «hasta el minimo de 1»). Un nodo que solo "
                    "diga «escalar» vale la mitad.",
                    "**5 pts** el nodo de enfriamiento por el que pasan **ambas** acciones y el "
                    "cierre del ciclo sobre el nodo de observacion. Si el enfriamiento cuelga "
                    "solo del scale out, son 2.5.",
                    "**4 pts** el nodo de lo que no escala con **arista punteada** (`-.->`) "
                    "rotulada `limite del diseno`. Una arista solida no suma: la diferencia entre "
                    "flujo y restriccion es el concepto que se califica.",
                    "**2 pts** que renderice sin error. Se verifica abriendo la respuesta en la "
                    "plataforma. Recordar el consejo del enunciado: umbrales con palabras («por "
                    "encima de») y no con simbolos, que en un rombo de Mermaid rompen el render.",
                    "Se acepta un segundo ciclo para el procesador asincrono, y se acepta que el "
                    "estudiante use `subgraph` para separarlos, siempre que cada ciclo cierre.",
                ],
                "errores": [
                    "**El ciclo no cierra:** el camino «No, No» termina en un nodo sin salida en "
                    "vez de volver a observar. Es el error que la verificacion del enunciado "
                    "persigue y significa que el estudiante penso el escalado como un evento y no "
                    "como un bucle.",
                    "**Umbrales en el diagrama distintos de los de la tabla** (800 en la tabla, "
                    "70 por ciento en el rombo, 500 ms en el nodo). Es el chequeo cruzado mas "
                    "rentable de esta pregunta y falla a menudo porque el estudiante escribe el "
                    "diagrama primero.",
                    "**Simbolos de mayor y menor dentro del rombo** (`p95 > 800ms`). Rompe el "
                    "render de Mermaid y cuesta los 2 pts, pero peor: el estudiante cree que el "
                    "diagrama esta mal cuando solo esta mal escrito. El enunciado lo advierte.",
                    "**Arista solida hacia el nodo de lo que no escala**, o peor, ese nodo dentro "
                    "del ciclo con un scale out propio. Contradice la tabla de la pregunta 1 y "
                    "cuesta los 4 pts.",
                    "**Enfriamiento sin minutos** («esperar un rato»). El nodo tiene que llevar "
                    "el numero, porque es el que hace la politica reproducible.",
                    "**Un rombo unico con las dos decisiones** («¿alto o bajo?»). Renderiza, pero "
                    "esconde que los umbrales de subida y bajada son distintos y separados a "
                    "proposito: esa separacion es lo que evita la oscilacion.",
                ],
            },
            {
                "n": 3,
                "titulo": "Lo que NO escala y por que",
                "tipo": "abierta",
                "puntos": 20,
                "respuesta": (
                    "**Uno. Base de datos de prestamos (primaria de escrituras).**\n\n"
                    "1. **Componente:** `Base de datos de prestamos`, la instancia primaria, tal "
                    "como se llama en el C4 Container y en el C4 Deployment.\n"
                    "2. **Por que no escala horizontalmente:** es la unica instancia que acepta "
                    "escrituras, y esa unicidad es justamente lo que resuelve la doble reserva. "
                    "Dos primarias tendrian que acordar cual de las dos gano el ultimo ejemplar "
                    "del mismo `isbn`, y ese acuerdo es el problema que la arquitectura evita "
                    "teniendo **un solo arbitro**. A eso se suma un limite duro: acepta "
                    "**20 conexiones**, y ese numero es el que fija el maximo de 4 replicas de la "
                    "API en la politica de la pregunta 1.\n"
                    "3. **Que pasa si el pico lo desborda:** las reservas primero tardan y "
                    "despues fallan por agotamiento del pool. El estudiante ve la rueda girando y "
                    "luego un error. Aparece en la senal de **saturacion** de la Clase 8 (pool en "
                    "16 de 20 conexiones) y, cuando ya no queda ninguna, en la de **errores "
                    "5xx**.\n"
                    "4. **Plan alterno, ejecutable sin cloud de pago:** escala **vertical** en "
                    "ventana de mantenimiento anunciada (2 a 4 vCPU), mas una **replica de solo "
                    "lectura** que atienda `GET /titulos`, que es el 82 por ciento del trafico "
                    "segun la mezcla de la Clase 12, mas un **limite de peticiones por usuario** "
                    "en el edge. Los tres se hacen en el lab: la replica de lectura es un segundo "
                    "contenedor de PostgreSQL con replicacion en streaming, y el limite de "
                    "peticiones son tres lineas de configuracion del proxy.\n\n"
                    "**Dos. El limite de envio del proveedor de correo (aspecto no de "
                    "infraestructura).**\n\n"
                    "1. **Componente o aspecto:** la cuota del `Correo transaccional SaaS`, el "
                    "sistema externo del C4 Context.\n"
                    "2. **Por que no escala horizontalmente:** el plan gratuito admite "
                    "**100 mensajes por hora**, y ese techo es de un tercero: no cambia por "
                    "agregar replicas del `Procesador de avisos`. Cinco workers golpeando la "
                    "misma cuota solo consiguen que el proveedor devuelva `429` mas rapido. Es la "
                    "leccion incomoda del tema: **escalar la pieza propia no mueve el limite "
                    "ajeno**.\n"
                    "3. **Que pasa si el pico lo desborda:** los avisos de vencimiento se "
                    "retrasan y el estudiante recibe el correo el mismo dia del vencimiento en "
                    "vez de dos dias antes, que es exactamente la capacidad que la ficha de la "
                    "Clase 1 promete. Aparece en la senal de **fallos de envio de correo** de la "
                    "Clase 8, no en la de latencia.\n"
                    "4. **Plan alterno, ejecutable sin cloud de pago:** la `Cola de avisos` **es** "
                    "la amortiguacion, y esta para eso: el worker consume a ritmo controlado "
                    "—1 mensaje cada 40 segundos, 90 por hora, con margen bajo la cuota— y la "
                    "cola guarda el resto sin perder nada. Mas un agrupamiento por estudiante: un "
                    "correo con tres libros por vencer en vez de tres correos. Ambos son codigo y "
                    "configuracion.\n\n"
                    "**Tres. El limite de 3 prestamos activos por estudiante (aspecto no de "
                    "infraestructura).**\n\n"
                    "1. **Componente o aspecto:** el invariante «ningun estudiante con mas de 3 "
                    "prestamos activos», que hoy vive en el `Servicio de reservas` del C4 "
                    "Component de la Clase 11.\n"
                    "2. **Por que no escala horizontalmente:** es una regla **global** que se "
                    "evalua leyendo y despues escribiendo. Si dos replicas de la API la verifican "
                    "al mismo tiempo, las dos leen «tiene 2» y las dos insertan: el estudiante "
                    "termina con 4. Y aqui esta lo que hay que subrayar: **agregar replicas "
                    "empeora la probabilidad del error en vez de mejorarla**. Es el unico caso de "
                    "la politica donde escalar horizontalmente es contraproducente.\n"
                    "3. **Que pasa si el pico lo desborda:** aparecen prestamos que violan la "
                    "regla, en silencio. No se ve en latencia ni en 5xx —el sistema responde "
                    "`201 Created` con toda normalidad— y por eso hay que buscarlo en el registro "
                    "de **auditoria**, uno de los dos registros que la Clase 8 dejo declarados, "
                    "con una consulta de conteo por estudiante.\n"
                    "4. **Plan alterno, ejecutable sin cloud de pago:** que la verificacion no la "
                    "haga la aplicacion sino la base, en la misma sentencia que inserta "
                    "(`INSERT ... WHERE (SELECT count(*) FROM prestamos WHERE id_estudiante = ... "
                    "AND estado = 'activo') < 3`), de modo que el arbitro siga siendo uno solo "
                    "aunque haya cuatro replicas. Es SQL: no cuesta un peso."
                ),
                "como_calificar": [
                    "**9 pts** los 3 componentes con las **4 lineas rotuladas** cada uno "
                    "(componente, por que no escala, que pasa en el pico, plan alterno). 3 pts "
                    "por bloque, 0.75 por linea. Una linea sin rotulo, fundida en el parrafo, no "
                    "suma: los rotulos son lo que hace la respuesta auditable.",
                    "**5 pts** que las razones sean **tecnicas**. «No nos alcanzo el tiempo», «no "
                    "sabemos como» y «no tenemos presupuesto» valen 0 en esa linea. La prueba: la "
                    "razon debe seguir siendo verdadera aunque el equipo tuviera seis meses y "
                    "dinero.",
                    "**4 pts** que uno de los tres sea la **base de datos primaria de escrituras** "
                    "y uno sea un aspecto **no de infraestructura** (estado de sesion, contador "
                    "global, cuota de un tercero). 2 pts cada condicion.",
                    "**2 pts** que los 3 planes alternos sean ejecutables sin cloud de pago. Un "
                    "plan que empiece por «contratar» no suma; «configurar», «agregar un "
                    "contenedor», «cambiar la consulta» si.",
                    "Se valora especialmente —aunque el enunciado no lo exija— que el estudiante "
                    "diga en cual senal de la Clase 8 aparece el sintoma. Es lo que conecta esta "
                    "pregunta con el monitoreo y suele ser la respuesta que gana el Q&A de la "
                    "Clase 15.",
                ],
                "errores": [
                    "**Tres razones que son la misma** («es un solo servidor»). El ejercicio pide "
                    "tres limites de naturaleza distinta; si los tres son de infraestructura, se "
                    "pierden los 2 pts del aspecto no de infraestructura y ademas la respuesta no "
                    "muestra comprension del tema.",
                    "**«No escala porque no tuvimos tiempo de configurarlo».** Es el error que la "
                    "rubrica castiga con 5 pts. Devolver con la pregunta: ¿seguiria sin escalar si "
                    "tuvieras un semestre mas? Si la respuesta es no, ese no es un limite de "
                    "diseno.",
                    "**Confundir «no escala» con «no lo hicimos».** La base de datos primaria no "
                    "escala horizontalmente aunque se le dedique el semestre completo; el ci.yml "
                    "sin pruebas si se puede hacer. Lo segundo es un item de backlog, no un "
                    "limite.",
                    "**Plan alterno que es cloud de pago** («usar Aurora Multi-Master», «un "
                    "cluster gestionado»). Contradice la restriccion del curso. La replica de "
                    "solo lectura en un contenedor local es la version equivalente y gratuita.",
                    "**Sintoma descrito desde el servidor y no desde el usuario** («se agota el "
                    "pool»). Falta la mitad: ¿que ve el estudiante en la pantalla? Esa es la "
                    "linea que hace util el analisis.",
                    "**Olvidar que escalar puede empeorar las cosas.** Si ninguno de los tres "
                    "bloques menciona un invariante global, vale la pena senalarlo en la "
                    "devolucion: es el concepto mas fino del tema y el que mas se pregunta en "
                    "entrevistas.",
                ],
            },
            {
                "n": 4,
                "titulo": "Impacto del autoescalado en costos y sostenibilidad",
                "tipo": "abierta",
                "puntos": 15,
                "tabla": {
                    "headers": ["Escenario", "Replicas activas", "Costo cualitativo B/M/A",
                                "Accion de sostenibilidad"],
                    "rows": [
                        ["Valle: 22:00 a 06:00 y domingos",
                         "API 1, procesador 0, edge 1",
                         "**B** (en la Clase 10 la API estaba en **A**)",
                         "Bajar la API a 1 replica y el procesador a 0 entre las 22:00 y las "
                         "06:00, y dejar la evidencia en "
                         "`/capturas/escalado-AAAAMMDD.txt` con la salida de `docker ps` y la "
                         "hora del sistema"],
                        ["Dia normal, lunes a viernes en jornada",
                         "API 1 a 2, procesador 0 a 1, edge 1",
                         "**M**",
                         "Mantener activo el disparador de bajada para que la segunda replica no "
                         "quede encendida despues del mediodia; revisar el historial de escalado "
                         "una vez por semana y anotar cuantas veces bajo"],
                        ["Pico del 21/09/2026, 11:40 a 12:20",
                         "API hasta 4, procesador hasta 3, edge hasta 2",
                         "**A**",
                         "Pre-escalar a mano a 2 replicas a las 11:30 y devolver la politica a "
                         "automatico a las 12:30, con las dos horas anotadas en la bitacora: "
                         "evita que el enfriamiento de 10 minutos se gaste la mitad del pico "
                         "subiendo de a una"],
                    ],
                },
                "respuesta": (
                    "**La media linea que explica el cambio de nivel.** En la Clase 10 la fila de "
                    "la API quedo en nivel **A** porque el driver era horas encendidas y se "
                    "calculo sobre **720 al mes** (encendida siempre). En el escenario de valle "
                    "baja a **B** precisamente porque la politica reduce esas horas a unas **480**: "
                    "el nivel no cambio de opinion, cambio de escenario, y el apalancamiento que "
                    "alli estaba anunciado —«escalar a cero fuera de la ventana de uso»— es el que "
                    "hoy quedo escrito como disparador con numero. La tabla de la Clase 10 sigue "
                    "siendo valida como promedio del mes; esta la desagrega en tres momentos.\n\n"
                    "**Frase de cierre.** De las 4 replicas maximas de la API, **3 solo existen "
                    "durante los 40 minutos del pico**: el 75 por ciento de la capacidad maxima "
                    "instalada vive **menos del 0.1 por ciento de las horas del mes** (40 minutos "
                    "sobre 43 200). Dicho al reves, y esta es la conclusion que importa: casi todo "
                    "el costo del PI viene de la **capacidad base**, no del pico, y por eso el "
                    "apalancamiento real esta en el valle —bajar a 1 replica ocho horas cada "
                    "noche— y no en recortar el pico, que es donde la intuicion manda mirar.\n\n"
                    "**Por que la accion del pico es «pre-escalar a mano» y no un disparador "
                    "mejor.** Es la consecuencia aritmetica de la pregunta 1 y conviene decirla "
                    "sin adornos: con enfriamiento de 10 minutos, subir de 1 a 4 replicas toma 30 "
                    "minutos de un pico que dura 40. La politica automatica esta bien para lo "
                    "inesperado; para un pico **con fecha en el calendario** lo correcto es "
                    "anticiparlo. Reconocer que el autoescalado no es la respuesta a todo es "
                    "criterio de arquitectura, no una concesion."
                ),
                "como_calificar": [
                    "**6 pts** las 3 filas (valle, dia normal, pico) con las 4 columnas y las "
                    "replicas **dentro del rango declarado en la pregunta 1**. Se verifica "
                    "comparando con la tabla: un pico con 6 replicas cuando el maximo era 4 es "
                    "incoherencia y descuenta.",
                    "**5 pts** la coherencia de los niveles B/M/A con la seccion de costos de la "
                    "Clase 10, **o** la media linea que explica el cambio. Cambiar el nivel sin "
                    "explicar vale 0 de estos 5; explicarlo bien vale los 5 completos, aunque el "
                    "nivel sea distinto.",
                    "**3 pts** las acciones de sostenibilidad concretas y verificables: deben "
                    "decir **donde queda la evidencia**. «Ser eficientes» no suma; «dejar la "
                    "salida de `docker ps` en `/capturas/` con la hora» si.",
                    "**1 pt** la frase de cierre sobre cuanto del costo viene de capacidad de "
                    "pico. Se acepta cualitativa si esta razonada, pero la version con la "
                    "division hecha (minutos de pico sobre minutos del mes) es la que muestra el "
                    "punto.",
                    "Se valora que el estudiante llegue a la conclusion contraintuitiva —el "
                    "ahorro esta en el valle, no en el pico—. No es obligatoria para los puntos, "
                    "pero es la mejor respuesta posible a esta pregunta y conviene reconocerla en "
                    "la devolucion.",
                ],
                "errores": [
                    "**Replicas del pico por encima del maximo de la pregunta 1.** Es la "
                    "incoherencia mas comun entre las dos tablas y se detecta en cinco segundos.",
                    "**Nivel B/M/A cambiado en silencio.** Si en la Clase 10 la API era A y aqui "
                    "es B sin la media linea, se pierden los 5 pts de coherencia. La media linea "
                    "es facil de escribir y es justamente el aprendizaje.",
                    "**Acciones de sostenibilidad que son intenciones** («optimizar el consumo», "
                    "«usar menos recursos»). Sin artefacto donde comprobarlas no son verificables. "
                    "Pedir la ruta del archivo o el nombre del registro.",
                    "**Valle con 0 replicas de la API.** Bajar la API a cero significa que la "
                    "primera peticion de la manana espera el arranque completo, y el minimo "
                    "declarado en la pregunta 1 era 1: es incoherente con su propia politica. El "
                    "que si va a cero es el procesador de avisos.",
                    "**Frase de cierre invertida** («casi todo el costo viene del pico»). Suena "
                    "razonable y es falso en este proyecto: son 40 minutos al mes. Vale la pena "
                    "hacer la division con el estudiante en la devolucion.",
                ],
            },
            {
                "n": 5,
                "titulo": "Disparadores de autoescalado",
                "tipo": "cerrada_multi",
                "puntos": 10,
                "justificacion": {
                    0: "**Cierta.** Tiene las tres partes que la pregunta 1 exige: metrica "
                       "(p95 de una operacion concreta), umbral numerico (800 ms) y ventana "
                       "(3 minutos sostenidos). Es literalmente la fila de la API de la tabla, y "
                       "el 800 viene del presupuesto de latencia de la Clase 12.",
                    1: "**Cierta.** Es la fila del `Procesador de avisos`: la profundidad de la "
                       "cola es la metrica correcta para un consumidor asincrono, porque mide "
                       "trabajo pendiente y no esfuerzo. Un worker con CPU baja y 800 mensajes en "
                       "cola necesita replicas; uno con CPU alta y cola vacia, no.",
                    2: "**Falsa.** «Cuando el sistema se sienta lento» no es una metrica: no "
                       "tiene numero, no tiene ventana y no la puede evaluar una maquina cada 60 "
                       "segundos. Que el equipo lo revise a diario no lo arregla; lo convierte en "
                       "un procedimiento manual, que es lo contrario de una politica de "
                       "autoescalado.",
                    3: "**Cierta.** Sin maximo, un error de codigo o una rafaga de trafico "
                       "escalan sin techo: asi se producen las facturas de miles de dolares que "
                       "salen en las noticias. En BiblioLite el maximo tiene ademas una razon "
                       "tecnica y no solo economica: 4 replicas por 5 conexiones son las 20 que "
                       "acepta el motor.",
                    4: "**Falsa, y es la trampa fina del taller.** Un enfriamiento de 10 "
                       "segundos no evita la oscilacion: **la provoca**. La ventana de medicion "
                       "es de 3 minutos, asi que a los 10 segundos el sistema decide otra vez con "
                       "datos que todavia reflejan el estado anterior, antes de que la replica "
                       "nueva reciba trafico. La regla de la pregunta 1 es exactamente esta: el "
                       "enfriamiento nunca mas corto que la ventana.",
                    5: "**Falsa.** Es la pieza que la pregunta 3 obliga a declarar como «no "
                       "escala». Sumar primarias de escritura obliga a resolver quien gano el "
                       "ultimo ejemplar del mismo `isbn`, que es el problema que la arquitectura "
                       "evita teniendo un solo arbitro. Escalar la API es facil porque no guarda "
                       "estado; la base guarda estado y ahi esta toda la dificultad.",
                },
                "como_calificar": [
                    "**4 pts por cada afirmacion correcta marcada, con techo de 10.** Las tres "
                    "ciertas son las opciones 1, 2 y 4 tal como estan numeradas en la plataforma "
                    "(disparador con ventana, profundidad de cola, necesidad de maximo). La clave "
                    "se lee del banco.",
                    "**Se descuentan 4 pts por cada incorrecta marcada**, sin bajar de cero. "
                    "Marcar las seis da cero.",
                    "Las tres falsas son las tres confusiones que esta clase tiene que dejar "
                    "resueltas: el disparador sin numero, el enfriamiento demasiado corto y la "
                    "base que se cree elastica. Cada una tiene su contraparte en una pregunta "
                    "abierta del mismo taller, asi que un estudiante que falle aqui y acierte "
                    "alla probablemente adivino en una de las dos.",
                    "Es la unica pregunta autocalificada del taller. Si mas de la mitad del grupo "
                    "marca la del enfriamiento de 10 segundos, conviene abrir la Clase 15 con dos "
                    "minutos de oscilacion dibujada en el tablero: es un concepto que se entiende "
                    "mejor viendolo que leyendolo.",
                ],
                "errores": [
                    "**Marcar la del enfriamiento de 10 segundos** porque «mas rapido reacciona, "
                    "mejor». Es el error mas instructivo del taller: reaccionar mas rapido que la "
                    "medicion es decidir con informacion vieja.",
                    "**Marcar la de la base de datos** por analogia con la API. La diferencia es "
                    "el estado, no la tecnologia; conviene devolver al bloque uno de la pregunta "
                    "3, que el estudiante acaba de escribir.",
                    "**Descartar la del maximo de replicas** por parecer de sentido comun. Es "
                    "cierta y vale 4 pts; el reflejo de «esto es muy obvio, debe ser trampa» "
                    "cuesta puntos cada semestre.",
                    "**Marcar la de «se sienta lento»** porque el equipo si revisa a diario. La "
                    "afirmacion habla de un disparador **valido**, y un disparador es algo que "
                    "una maquina evalua sola: la revision diaria es otra cosa, igual de "
                    "respetable y no automatizable.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("Es clase autonoma y no hubo sesion. ¿Con que resuelvo el taller?",
             "Con el fundamento de la Clase 13, que esta escrito para funcionar sin explicacion "
             "en vivo, y con dos artefactos propios: el presupuesto de latencia de la Clase 12 "
             "—de ahi salen los 800 ms del disparador— y la tabla de senales de la Clase 8 —de "
             "ahi salen los umbrales de saturacion—. Si esos dos documentos estan, la tabla de "
             "hoy se llena casi sola."),
            ("¿Tengo que configurar un autoescalador real en algun proveedor?",
             "No. La politica es conceptual y no se pide ninguna cuenta de nube ni tarjeta. Lo "
             "que se califica es la tabla con numeros, el diagrama del ciclo y los argumentos. "
             "Escribir la politica es lo dificil; aplicarla en una consola es un formulario."),
            ("¿De donde saco el maximo de replicas? Puse 10 al azar.",
             "De la pieza que no escala. Su base acepta un numero fijo de conexiones (aqui 20) y "
             "cada replica abre su pool: si cada una toma 5, el techo son 4 replicas. Ese "
             "razonamiento es el mejor argumento de todo el taller y ademas conecta la pregunta 1 "
             "con la 3."),
            ("¿Puede el minimo ser 0?",
             "Para un procesador asincrono, si, y en BiblioLite es lo correcto: el aviso sale dos "
             "dias antes del vencimiento, asi que un retraso de dos minutos no le importa a "
             "nadie. Para la API que atiende peticiones de usuarios, no: la primera peticion de "
             "la manana pagaria el arranque completo. Con una condicion en el caso del cero: la "
             "profundidad de la cola la tiene que observar el orquestador desde fuera, no el "
             "worker, porque el worker no esta."),
            ("¿Por que el enfriamiento no puede ser corto? Quiero que reaccione rapido.",
             "Porque el enfriamiento mas corto que la ventana de medicion produce oscilacion: se "
             "decide con datos que todavia no reflejan la accion anterior. Sube, mide alto otra "
             "vez porque la replica nueva no recibio trafico aun, y vuelve a subir. Es la opcion "
             "falsa de la pregunta 5 y el error mas comun del tema."),
            ("Mi pico dura 40 minutos y el enfriamiento 10. No alcanza a escalar. ¿Cambio el "
             "enfriamiento?",
             "No: cambie la estrategia. Ese calculo es un hallazgo, no un error, y la respuesta "
             "correcta es pre-escalar a mano antes del pico, porque el pico tiene fecha en el "
             "calendario. El autoescalado sirve para lo inesperado; lo que esta en la agenda se "
             "anticipa. Escribalo asi en la pregunta 4 y gana los puntos de sostenibilidad."),
            ("Mi dominio no tiene cola ni worker. ¿Que pongo en esas dos filas?",
             "Ponga los cinco componentes que su C4 Deployment tenga de verdad. Si no hay cola, "
             "la quinta fila puede ser el almacenamiento de objetos, un servicio de reportes o "
             "cualquier pieza real; lo que no se acepta es inventar una caja para llenar la "
             "tabla. Lo que si es obligatorio es que al menos una fila diga `no escala`."),
            ("¿Puedo decir que nada escala porque el proyecto es academico?",
             "No, y por dos razones. La primera es que el ejercicio es diseñar la politica, que "
             "es gratis; la segunda es que si nada escala, la pregunta 4 no tiene tres escenarios "
             "y la 3 pierde su sentido. Lo honesto es lo que hace esta solucion: la politica esta "
             "escrita, se puede aplicar en el lab con replicas de contenedores, y lo que no "
             "escala esta declarado con razon tecnica."),
        ],
        "cierre": (
            "Lo que queda de hoy es una politica que se puede leer y aplicar: cinco componentes "
            "con disparadores numericos, un ciclo que cierra, tres cosas que no escalan con su "
            "razon tecnica y tres escenarios de costo. Y queda un numero que hay que llevar a la "
            "sustentacion del 16/11 porque es la mejor respuesta del paquete: el maximo de "
            "replicas de la API es 4, y no lo decide la API sino las 20 conexiones de la base de "
            "datos, que es la pieza que deliberadamente no escala. Con eso cierra el Corte 3: el "
            "sistema tiene un numero que cumplir, un cuello identificado, una politica para "
            "crecer y un limite escrito. La Clase 15 no agrega arquitectura: la defiende."
        ),
    },

    15: {
        "titulo": "Solucion del Taller Clase 15 - Entrega final y sustentacion (BiblioLite)",
        "resumen": (
            "Taller de cierre de 100 puntos en cinco preguntas, de la sesion de sustentaciones "
            "del 16/11/2026. No agrega arquitectura nueva: la consolida y la defiende. Indice del "
            "paquete con las 8 filas verificadas desde otra maquina, la lamina unica de 11 nodos "
            "que se proyecta en los 60 segundos de apertura, el Q and A escrito con evidencia y "
            "trade-off en cada respuesta, la reflexion del trade-off mas dificil y los tiempos "
            "reales del pitch. La solucion asume el paquete que se fue construyendo desde la "
            "Clase 1: 7 filas en `completo` sobre 8, y la que queda `parcial` esta ahi a "
            "proposito para mostrar como se responde por un pendiente sin decir «no alcanzo el "
            "tiempo»."
        ),
        "total": 100,
        "nota_actividad": (
            "**Sesion de cierre: lunes 16/11/2026, 10:00 a 12:00, virtual.** El taller es la "
            "**evidencia escrita** de la sustentacion, no un sustituto: se califica junto con lo "
            "que el estudiante defiende en vivo. Dos condiciones operativas que conviene anunciar "
            "en la Clase 13 y repetir por escrito: **el paquete se sube antes del turno** —quien "
            "lo suba durante la sesion pierde los 5 pts de la Parte A de la pregunta 5— y **los "
            "enlaces se abren desde una ventana privada**, porque el error mas comun de esta "
            "entrega no es un archivo que falta sino un Drive que pide permisos. Como en todo el "
            "curso, nada de esto requiere cloud de pago ni tarjeta: el paquete vive en un "
            "repositorio publico de GitHub y en capturas."
        ),
        "preguntas": [
            {
                "n": 1,
                "titulo": "Indice del paquete final",
                "tipo": "abierta",
                "puntos": 25,
                "tabla": {
                    "headers": ["Entregable", "Nombre del archivo",
                                "Ruta dentro del paquete o enlace", "Estado"],
                    "rows": [
                        ["1. Informe de arquitectura completo",
                         "`informe-pi-bibliolite.pdf`",
                         "`/informe/informe-pi-bibliolite.pdf`", "completo"],
                        ["2. Diagrama C4 Context y C4 Container",
                         "`c4-context.png`, `c4-context.mmd`, `c4-container.png`, "
                         "`c4-container.mmd`",
                         "`/diagramas/`", "completo"],
                        ["3. Diagrama C4 Deployment",
                         "`c4-deployment.png`, `c4-deployment.mmd`",
                         "`/diagramas/`", "completo"],
                        ["4. Dockerfile y evidencia del lab de contenedores",
                         "`Dockerfile`, `clase03-docker-ps.png`",
                         "`/docker/Dockerfile` y `/capturas/clase03-docker-ps.png`", "completo"],
                        ["5. Workflow `ci.yml` y enlace al run verde",
                         "`ci.yml`",
                         "`/.github/workflows/ci.yml` y "
                         "`https://github.com/USUARIO/bibliolite/actions/runs/ID`",
                         "**parcial** (el run verde ejecuta `lint` y `build`; falta la etapa de "
                         "pruebas automatizadas, que quedo como B-01 del backlog de la Clase 11)"],
                        ["6. Seccion de seguridad con tabla STRIDE y politica de secretos",
                         "`06-amenazas.md`",
                         "`/informe/06-amenazas.md`", "completo"],
                        ["7. Secciones de costos, sostenibilidad y escalabilidad",
                         "`10-costos-sostenibilidad.md`, `13-escalado.md`",
                         "`/informe/`", "completo"],
                        ["8. Presentacion de sustentacion",
                         "`pitch-bibliolite.pdf`, `guion-pitch.md`",
                         "`/pitch/`", "completo"],
                    ],
                },
                "respuesta": (
                    "**Linea de verificacion obligatoria, debajo de la tabla:**\n\n"
                    "> `verificado desde otra maquina el 15/11/2026`\n\n"
                    "**Linea de cierre:** 7 filas en `completo` sobre 8.\n\n"
                    "**Por que la verificacion desde otra maquina vale 6 de los 25 puntos.** "
                    "Porque es el fallo que mas entregas ha hundido en este curso y no tiene nada "
                    "que ver con arquitectura: el archivo existe, el estudiante lo ve, y el "
                    "docente recibe «Solicitar acceso». El navegador propio lleva la sesion "
                    "abierta y miente sistematicamente. La verificacion correcta son tres pasos: "
                    "ventana privada, pegar el enlace, y confirmar que el PDF **se abre y se "
                    "puede pasar de pagina** —no solo que carga la vista previa—. Si el paquete "
                    "esta en GitHub el riesgo baja mucho, pero sigue existiendo con el "
                    "repositorio privado y con los `.mmd` que solo renderizan si el visor los "
                    "soporta.\n\n"
                    "**Por que los nombres no llevan espacios ni tildes.** No es una preferencia "
                    "estetica: un espacio en un nombre de archivo rompe la URL (`Informe "
                    "Final.pdf` viaja como `Informe%20Final.pdf` y se pega mal en la mitad de los "
                    "clientes de correo), y una tilde puede cambiar de codificacion entre Windows "
                    "y Linux y dejar el archivo inalcanzable desde el pipeline. Es la misma "
                    "leccion de la Clase 11 sobre nombres canonicos, aplicada al sistema de "
                    "archivos: el nombre en prosa puede tener tildes, el nombre del artefacto "
                    "no.\n\n"
                    "**Por que hay una fila `parcial` y por que eso NO cuesta puntos.** El "
                    "enunciado permite `parcial` y solo exige que diga **que falta** entre "
                    "parentesis. Escribir 8 de 8 en `completo` cuando el `ci.yml` no corre pruebas "
                    "es lo que si cuesta: es una afirmacion falsa sobre el propio trabajo, y el "
                    "docente la comprueba abriendo el run en 20 segundos. La fila 5 declarada como "
                    "parcial hace tres cosas a la vez: es honesta, se conecta con el backlog de la "
                    "Clase 11 (B-01) y le da al estudiante la mejor respuesta posible en el Q and "
                    "A de la pregunta 3 —«lo dejamos fuera a proposito porque...»—. Un pendiente "
                    "declarado es un item de backlog; un pendiente escondido es un hallazgo.\n\n"
                    "**Sobre el orden de las 8 filas.** Es el orden del enunciado y no es "
                    "arbitrario: reproduce el recorrido del semestre (informe, logica, "
                    "despliegue, contenedor, pipeline, seguridad, costos, pitch) y es el mismo "
                    "orden en que el jurado va a pedir las evidencias durante el Q and A. Un "
                    "estudiante que reordena las filas «como le queda mejor» pierde 10 pts y, "
                    "peor, pierde el mapa: en la sustentacion va a buscar el archivo mientras el "
                    "cronometro corre."
                ),
                "como_calificar": [
                    "**10 pts** las 8 filas **en el orden del enunciado** con las 4 columnas. "
                    "1.25 pts por fila. El orden se verifica de un vistazo y no admite "
                    "reacomodo: es el orden en que se piden las evidencias.",
                    "**6 pts** rutas o enlaces **reales** y nombres de archivo sin espacios ni "
                    "tildes. Se toman dos enlaces al azar y se abren; si el nombre trae espacios "
                    "se descuenta aunque el enlace funcione, porque el criterio es el nombre.",
                    "**6 pts** la linea `verificado desde otra maquina el <fecha>` con fecha "
                    "**anterior o igual** a la de entrega. Una fecha posterior al turno de "
                    "sustentacion no vale: seria una verificacion que aun no ocurrio.",
                    "**3 pts** el estado de cada fila, con el faltante entre parentesis en las "
                    "parciales. Un `parcial` sin parentesis vale la mitad.",
                    "**Cada archivo que no abra descuenta 3 pts**, tal como anuncia el enunciado, "
                    "y el descuento se aplica sobre el total de la pregunta. Se verifica en "
                    "ventana privada, no en la sesion del docente: si el docente tiene acceso "
                    "porque el estudiante lo compartio con su correo, el archivo sigue estando mal "
                    "publicado.",
                    "Un `parcial` bien declarado **no descuenta**. Conviene decirlo en voz alta "
                    "antes de la entrega: la honestidad no cuesta puntos aqui y ademas se paga en "
                    "la pregunta 3.",
                ],
                "errores": [
                    "**Enlaces que piden permisos.** El error numero uno de esta entrega, todos "
                    "los semestres. La causa es siempre la misma: se verifico con la sesion "
                    "propia abierta. Aplicar el descuento de 3 pts por archivo y dejar la razon "
                    "escrita en la devolucion, porque es un habito profesional que hay que "
                    "instalar.",
                    "**8 de 8 en `completo` con un `ci.yml` que solo tiene un `echo`.** Es "
                    "afirmacion falsa y se comprueba abriendo el run. Cuesta los 3 pts del estado "
                    "y ademas envenena la pregunta 3, porque el estudiante ya no puede usar el "
                    "pendiente como trade-off: acaba de declarar que no existe.",
                    "**Rutas locales del computador** (`C:\\Users\\...\\informe.pdf`). No es una "
                    "ruta dentro del paquete: nadie mas puede abrirla. Se descuenta como enlace "
                    "irreal.",
                    "**Un solo enlace a la carpeta raiz para las 8 filas.** La columna pide la "
                    "ruta **del entregable**; una carpeta con 40 archivos sueltos obliga al "
                    "jurado a buscar. Es el mismo criterio de la Clase 11: el paquete se navega, "
                    "no se explora.",
                    "**Nombres con espacios y tildes** (`Diagrama Despliegue Final (versión "
                    "2).png`). Ademas del descuento, ese nombre delata que no hubo control de "
                    "versiones: «version 2» dentro del nombre es lo que git hace por uno.",
                    "**Linea de verificacion sin fecha** («verificado desde otra maquina»). Los 6 "
                    "pts son de la linea **con fecha**: sin ella no se puede saber si la "
                    "verificacion es de hoy o de hace tres semanas, cuando el paquete era otro.",
                ],
            },
            {
                "n": 2,
                "titulo": "Lamina unica de arquitectura para la sustentacion",
                "tipo": "diagrama",
                "puntos": 25,
                "respuesta_mermaid": """flowchart LR
    estudiante["Estudiante<br/>actor principal"]
    subgraph publica["Zona publica - 10.0.1.0/24"]
        edge["Edge / balanceador<br/>443 HTTPS"]
        spa["Aplicacion web<br/>React estatico<br/>443 HTTPS"]
    end
    subgraph privada["Zona privada - 10.0.2.0/24"]
        api["API de prestamos<br/>Node.js - 3000 HTTP<br/>1 a 4 replicas"]
        worker["Procesador de avisos<br/>Node.js - sin puerto expuesto"]
    end
    subgraph datos["Zona de datos - 10.0.3.0/24"]
        db[("Base de datos de prestamos<br/>PostgreSQL - 5432 TCP")]
        cola[("Cola de avisos<br/>Redis Streams - 6379 TCP")]
    end
    subgraph entrega["Cadena de entrega"]
        wf["Workflow ci.yml<br/>GitHub Actions"]
        img["Imagen bibliolite-api:0.1.0"]
    end
    idp["Proveedor de identidad institucional<br/>externo - 443"]
    correo["Correo transaccional SaaS<br/>externo - 443"]
    estudiante -->|"HTTPS 443"| edge
    estudiante -->|"HTTPS 443 - descarga el bundle"| spa
    edge -->|"HTTP 3000"| api
    api -->|"TCP 5432"| db
    api -->|"TCP 6379 - publica el aviso"| cola
    cola -->|"TCP 6379 - consume el aviso"| worker
    worker -->|"TCP 5432"| db
    api -->|"HTTPS 443"| idp
    worker -->|"HTTPS 443"| correo
    wf --> img
    img -.->|"despliegue simulado"| api""",
                "respuesta": (
                    "**Conteo de nodos: 11 de los 14 permitidos.** Estudiante, edge, spa, api, "
                    "worker, db, cola, wf, img, idp y correo. Los cuatro `subgraph` no son nodos, "
                    "son las zonas. Sobran tres nodos de margen a proposito: es el espacio para "
                    "que un dominio con una pieza mas —un almacen de objetos, un servicio de "
                    "reportes— quepa sin rehacer la lamina.\n\n"
                    "**Los seis requisitos, senalados uno por uno.** (1) Las tres zonas llevan "
                    "**subred**, que es lo nuevo respecto de la Clase 7: alli las zonas se "
                    "describieron por su alcance («solo alcanzable desde el edge») y hoy se les "
                    "pone el CIDR, porque en una lamina de sustentacion no hay espacio para la "
                    "frase. (2) Los 5 contenedores canonicos mas el edge, cada uno con puerto. "
                    "(3) La API con `1 a 4 replicas`, el rango de la politica de la Clase 13. "
                    "(4) La cadena de entrega en su subgrafo, unida por **arista punteada** "
                    "rotulada `despliegue simulado`. (5) Los dos sistemas externos, fuera de las "
                    "zonas. (6) El estudiante entrando por HTTPS 443.\n\n"
                    "**El detalle que va a preguntar el jurado: «¿por que el procesador de avisos "
                    "no tiene puerto?».** Porque no atiende peticiones: **el trabajo lo va a "
                    "buscar a la cola**. Un contenedor sin puerto expuesto es un contenedor al "
                    "que nadie puede llegar desde fuera, y esa es su mejor propiedad de "
                    "seguridad, no una carencia. Decirlo asi —«sin puerto expuesto»— en la "
                    "etiqueta es mas fuerte que dejarla en blanco: la ausencia deliberada se "
                    "escribe.\n\n"
                    "**El otro detalle fino: el `worker` esta en la zona privada y sale a "
                    "internet.** No es contradiccion, y conviene tener la respuesta lista: la "
                    "zona privada **no acepta trafico entrante** de internet pero **si tiene "
                    "salida** (por NAT), y por eso el worker puede llamar al correo transaccional. "
                    "La que no tiene salida es la **zona de datos**: la base y la cola no pueden "
                    "iniciar conexiones hacia afuera, que es exactamente el control que evita la "
                    "exfiltracion de la Clase 6. Entrante y saliente son dos reglas distintas y "
                    "es el error conceptual mas comun sobre subredes.\n\n"
                    "**Por que el rango dice 1 a 4 y no 2 a 6.** El enunciado pone `2 a 6` como "
                    "ejemplo; lo que se califica es que el rango sea **el de la politica propia** "
                    "de la Clase 13. En BiblioLite el maximo es 4 porque cada replica abre 5 "
                    "conexiones y el motor acepta 20, y el minimo es 1 como deuda aceptada por "
                    "horas encendidas. Copiar el `2 a 6` del enunciado teniendo otra politica es "
                    "la incoherencia que esta pregunta busca.\n\n"
                    "**Como se proyecta esta lamina en 60 segundos.** Se recorre el camino del "
                    "usuario con el cursor, en este orden y sin desviarse: estudiante -> edge -> "
                    "API -> base de datos, y despues «y cuando hay que avisar, la API publica en "
                    "la cola y el procesador manda el correo». Doce segundos por salto. La cadena "
                    "de entrega y los externos **no se explican** salvo que los pregunten: estan "
                    "ahi para que se vean, no para narrarlos."
                ),
                "como_calificar": [
                    "**10 pts** las 3 zonas **con su subred** y los 6 elementos —5 contenedores "
                    "canonicos mas el edge— en la zona correcta y **con puerto** en la etiqueta. "
                    "Una base de datos en la zona publica cuesta la mitad de estos puntos: es un "
                    "error de seguridad, no de dibujo.",
                    "**6 pts** el rango de replicas de la API **coherente con la politica de la "
                    "Clase 13** (3 pts) y la cadena de entrega unida por **arista punteada** "
                    "rotulada `despliegue simulado` (3 pts). Arista solida hacia la API significa "
                    "que el pipeline despliega en produccion, que en este curso no ocurre: no "
                    "suma.",
                    "**5 pts** los 2 sistemas externos **fuera** de los subgrafos y el actor "
                    "entrando por **443**. Un sistema externo dentro de una zona propia es el "
                    "error que borra la frontera de confianza de la Clase 6.",
                    "**4 pts** legibilidad: **maximo 14 nodos** —se cuentan, no se estiman— y "
                    "nombres identicos a la tabla de reconciliacion de la Clase 11. 15 nodos es "
                    "cero en este renglon aunque el diagrama sea bonito: el criterio es que quepa "
                    "en una pantalla.",
                    "Prueba practica de la que habla el enunciado, y vale la pena hacerla en voz "
                    "alta con cada estudiante: **seguir el camino del usuario hasta la base de "
                    "datos con el dedo, sin abrir el informe**. Si el docente se pierde, el "
                    "jurado tambien.",
                ],
                "errores": [
                    "**Volver a dibujar el C4 Container.** Es la lamina del semestre, no un "
                    "cuarto diagrama: si no tiene zonas, puertos ni cadena de entrega, es el "
                    "diagrama de la Clase 4 con otro titulo y pierde la mayor parte de los "
                    "puntos.",
                    "**Mas de 14 nodos** por meter cada endpoint, cada tabla y cada libreria. Es "
                    "el error de criterio de esta pregunta: la lamina de sustentacion se optimiza "
                    "para 60 segundos de atencion ajena, no para demostrar cuanto se hizo.",
                    "**Zonas sin subred**, solo con el nombre. La rubrica pide las dos cosas; y "
                    "sin CIDR no se puede argumentar por que la base no es alcanzable desde "
                    "internet.",
                    "**Copiar el `2 a 6 replicas` del enunciado** cuando la politica propia dice "
                    "otra cosa. Es la incoherencia mas facil de detectar del taller: se abre la "
                    "pregunta 1 de la Clase 13 y se compara.",
                    "**Sistemas externos dentro de la zona publica.** «Publica» no significa «de "
                    "otros»: significa alcanzable desde internet **y bajo mi responsabilidad**. "
                    "El proveedor de identidad no esta bajo su responsabilidad y por eso va "
                    "fuera.",
                    "**Nodos que el paquete no tiene** —un almacen de objetos, una cache— puestos "
                    "para que la lamina «se vea completa». En BiblioLite se decidio "
                    "explicitamente en la Clase 7 que no habria almacen de objetos para datos del "
                    "dominio: dibujarlo hoy contradice el propio informe y es el tipo de "
                    "incoherencia que el jurado encuentra en la primera pregunta.",
                ],
            },
            {
                "n": 3,
                "titulo": "Q and A escrito: las 3 preguntas que teme",
                "tipo": "abierta",
                "puntos": 20,
                "respuesta": (
                    "**Pregunta 1 — Decision de arquitectura: «¿por que cinco contenedores y no "
                    "tres microservicios, o uno solo?»**\n\n"
                    "> Porque `ADR-001` decidio monolito modular sobre IaaS: un repositorio, un "
                    "build y un pipeline, con la logica separada por modulos y no por procesos.\n"
                    "> Los cinco elementos no son cinco servicios: son un frontend, **una misma "
                    "imagen corriendo dos veces** (`bibliolite-api:0.1.0` como API y como "
                    "procesador de avisos), la base y la cola.\n"
                    "> La cola y el worker se agregaron en la Clase 11 por el riesgo que la Clase "
                    "4 dejo escrito —«si el correo esta caido el aviso se pierde»—, no por moda "
                    "arquitectonica.\n"
                    "> **Trade-off aceptado:** los dos procesos comparten build y dependencias, "
                    "asi que un `npm install` roto detiene las dos piezas y no puedo actualizar "
                    "una sin la otra. Se acepta a cambio de un solo pipeline mantenible por una "
                    "persona en trece semanas.\n\n"
                    "**Pregunta 2 — Seguridad: «¿como protege el activo mas sensible?»**\n\n"
                    "> El activo mas sensible no son las credenciales: es el **historial de "
                    "prestamos**, que revela que lee cada estudiante. Esta en la fila 3 de la "
                    "`tabla STRIDE` como divulgacion de informacion.\n"
                    "> Tres controles, todos verificables en el paquete: la base vive en la zona "
                    "de datos **sin salida a internet** (`c4-deployment.mmd`), el token se valida "
                    "en cada peticion contra el proveedor institucional, y ningun secreto esta en "
                    "el repositorio: van como secretos del workflow (`06-amenazas.md`, seccion de "
                    "politica de secretos).\n"
                    "> **Trade-off aceptado:** **no** hay cifrado en reposo a nivel de columna. Un "
                    "volcado del volumen expondria el historial en claro. Se acepta porque el "
                    "cifrado por columna habria obligado a descifrar en la aplicacion para "
                    "cualquier consulta por rango de fechas, y el proyecto no tiene la infra de "
                    "gestion de llaves que eso exige; queda escrito como riesgo residual, no como "
                    "olvido.\n\n"
                    "**Pregunta 3 — Escala o rendimiento: «¿que pasa el dia del pico y que no "
                    "escala?»**\n\n"
                    "> El pico esta medido, no imaginado: 15 peticiones por segundo durante 40 "
                    "minutos (21/09/2026, 11:40 a 12:20), del escenario de carga de la Clase 12.\n"
                    "> La reserva completa cuesta **585 ms** contra un presupuesto de **800 ms** "
                    "(`diagrama de secuencia con el presupuesto de 800 ms`), con el commit de la "
                    "base como cuello: 330 de esos 585 ms.\n"
                    "> Lo que **no** escala es la base primaria de escrituras, y ahi esta el "
                    "numero que importa: acepta 20 conexiones, cada replica abre 5, luego el "
                    "maximo de la API son **4 replicas** (`politica de escalado, fila API`). El "
                    "techo de la API lo fija la base, no la API.\n"
                    "> **Trade-off aceptado:** el minimo son **1 replica**, no 2, asi que un "
                    "reinicio son unos 20 segundos de caida. Se acepta para bajar de 720 a 480 "
                    "horas encendidas al mes, que era el apalancamiento declarado en la seccion "
                    "de costos."
                ),
                "como_calificar": [
                    "**9 pts** las 3 preguntas de los 3 tipos exigidos, **en ese orden**, con "
                    "respuesta de **maximo 4 lineas**. 3 pts cada una. Una respuesta de nueve "
                    "lineas vale la mitad: el limite es parte del ejercicio, porque en la "
                    "sustentacion se responde en 30 segundos.",
                    "**6 pts** que cada respuesta **cite una evidencia concreta** del paquete, "
                    "con nombre de artefacto y ubicacion (`ADR-001`, `tabla STRIDE fila 3`, "
                    "`politica de escalado fila API`). 2 pts cada una. «Como se explico en el "
                    "informe» no es una cita.",
                    "**5 pts** que cada una nombre **el trade-off aceptado**, no solo la virtud. "
                    "Aproximadamente 1.7 pts cada una. La prueba es sencilla: si la respuesta "
                    "solo dice cosas buenas del diseno, no hay trade-off; toda decision de "
                    "arquitectura le quita algo a alguien.",
                    "**Cero en la respuesta que se limite a decir que no alcanzo el tiempo.** Es "
                    "explicito en la rubrica. Pero cuidado con el matiz: «lo dejamos fuera a "
                    "proposito porque el pipeline con pruebas exigia... y ganamos...» **si** "
                    "puntua completo. Lo que vale cero es la queja, no el pendiente.",
                    "Se valora que la evidencia citada **exista de verdad**: se toma una de las "
                    "tres al azar y se abre. Una cita a un `ADR-002` que no esta en el paquete es "
                    "peor que no citar, y ademas es exactamente lo que el jurado hace en vivo.",
                ],
                "errores": [
                    "**«No lo alcanzamos a hacer».** Cero en esa respuesta, por rubrica. La "
                    "reescritura correcta se le puede dictar al estudiante: «lo dejamos fuera a "
                    "proposito porque X, y con eso el proyecto gano Y». Hay que ensenar la "
                    "conversion, porque es una habilidad profesional real, no una excusa "
                    "elegante.",
                    "**Tres respuestas sin trade-off**, escritas como folleto de ventas («elegimos "
                    "esto porque es escalable, seguro y mantenible»). Cuesta los 5 pts y es la "
                    "senal mas clara de que el estudiante no entendio de que se trata la materia.",
                    "**Citar el informe en bloque** («esta en el informe»). No es evidencia "
                    "localizable. La cita tiene que decir **cual** artefacto y **cual** parte, "
                    "porque en la sustentacion hay que abrirla en cinco segundos.",
                    "**Elegir el activo sensible equivocado**: casi todos responden «las "
                    "contrasenas», que no estan en la base porque la identidad la maneja el "
                    "proveedor institucional. El activo es el dato del dominio —aqui el historial "
                    "de lectura—, y darse cuenta de eso es la mitad de la pregunta.",
                    "**Preguntas de mentira**, hechas para tener respuesta facil («¿usaron "
                    "Docker?»). El enunciado pide las 3 que **teme**. Si las tres son comodas, la "
                    "pregunta no se hizo: devolver pidiendo la que le da miedo.",
                    "**Respuesta a la de escala sin un solo numero.** «Escalamos "
                    "horizontalmente» no responde nada. Los numeros ya existen desde la Clase 12 "
                    "y la 13; no citarlos aqui es desperdiciar dos semanas de trabajo.",
                ],
            },
            {
                "n": 4,
                "titulo": "Reflexion: el trade-off mas dificil",
                "tipo": "abierta",
                "puntos": 15,
                "respuesta": (
                    "**1. La decision.** El trade-off mas dificil del semestre fue mantener "
                    "BiblioLite como monolito modular con dos procesos en vez de separar las "
                    "notificaciones en un servicio con su propio repositorio y su propio "
                    "pipeline.\n\n"
                    "**2. La alternativa que descarto.** La alternativa era un microservicio de "
                    "notificaciones independiente, con su repositorio, su `ci.yml` y su despliegue "
                    "propio. La defendia yo mismo en la Clase 4, cuando la palabra "
                    "«microservicios» todavia sonaba a la respuesta correcta a cualquier "
                    "pregunta. Lo que me hizo cambiar no fue un argumento teorico sino la "
                    "aritmetica de la Clase 11: trece semanas, una persona, y ya iba retrasado en "
                    "el pipeline que si tenia.\n\n"
                    "**3. Que sacrifico.** Aislamiento de fallos y de dependencias. Los dos "
                    "procesos comparten imagen, asi que un cambio de version de una libreria "
                    "toca las dos piezas y un build roto las detiene juntas. Tambien sacrifique "
                    "la posibilidad de que otra persona trabajara en las notificaciones sin "
                    "tocar mi repositorio. Lo que gane fue concreto: un solo pipeline que "
                    "efectivamente quedo verde, y tiempo para escribir la seguridad y el "
                    "escalado, que de otro modo habrian quedado en el backlog.\n\n"
                    "**4. Como se ve hoy en el paquete.** Quedo escrita en `ADR-001` "
                    "(`/adr/ADR-001-modelo-de-servicio.md`), en la seccion de consecuencias, con "
                    "la frase que resume la decision: «un repositorio, un build, un pipeline, dos "
                    "procesos». Se ve tambien en el `Dockerfile`, que produce **una** imagen, y "
                    "en el C4 Deployment, donde el `Procesador de avisos` aparece como la misma "
                    "imagen con otro comando de arranque.\n\n"
                    "**5. Que haria distinto.** Escribiria las pruebas del pipeline antes de "
                    "agregar la cola. Hoy tengo una cola funcionando y un `ci.yml` sin etapa de "
                    "pruebas, y ese es el unico `parcial` del indice: si volviera a empezar "
                    "manana, la etapa de pruebas seria la Clase 8 y la cola la 11, en ese orden."
                ),
                "como_calificar": [
                    "**8 pts** los 5 bloques **rotulados** y desarrollados, entre 200 y 300 "
                    "palabras. 1.6 pts por bloque. Se cuentan las palabras: 150 son un resumen y "
                    "400 son un desahogo. La version de arriba tiene unas 290.",
                    "**4 pts** que el sacrificio y la alternativa descartada sean **concretos**. "
                    "La prueba: ¿se puede discutir con argumentos? «Sacrifique la simplicidad» no "
                    "se puede discutir; «sacrifique el aislamiento de dependencias: un build roto "
                    "detiene las dos piezas» si.",
                    "**3 pts** que el bloque 4 cite el **artefacto real** con su ruta. Se abre y "
                    "se busca la frase. Si el ADR no menciona la decision, el bloque 4 no cumple, "
                    "aunque el ADR exista.",
                    "Se valora que el bloque 2 diga **quien** defendia la alternativa. La "
                    "respuesta honesta suele ser «yo mismo al principio», y admitir eso por "
                    "escrito es mas valioso academicamente que cualquier decision brillante: es "
                    "la evidencia de que hubo aprendizaje y no solo ejecucion.",
                    "Es una reflexion **tecnica**. Si el texto agradece al docente y no discute "
                    "una decision, se devuelve sin nota parcial y se pide reescribir: el ejercicio "
                    "no se hizo.",
                ],
                "errores": [
                    "**La carta de agradecimiento.** «Aprendi mucho, el curso fue muy completo, "
                    "gracias por la paciencia». No responde ninguno de los 5 bloques. Devolver "
                    "con una pregunta concreta: ¿cual decision te costo mas trabajo tomar?",
                    "**Trade-off que no es un trade-off** («decidi usar Docker»). Si no hubo algo "
                    "que se perdio, no hubo trade-off: hubo una eleccion obvia. Pedir la decision "
                    "en la que las dos opciones tenian defensa.",
                    "**Alternativa descartada generica** («la otra opcion era hacerlo mal»). No "
                    "es una alternativa, es un espantapajaros. La alternativa descartada tiene "
                    "que ser la que alguien razonable defenderia.",
                    "**Bloque 4 sin artefacto** («quedo en el informe»). Cuesta los 3 pts. Es el "
                    "bloque mas facil de la pregunta y el que mas se pierde por descuido: solo "
                    "hay que copiar una ruta.",
                    "**Fuera del rango de palabras.** 120 palabras es no haber hecho el "
                    "ejercicio; 500 es no haber decidido que importa. Ambos casos descuentan "
                    "sobre los 8 pts del primer renglon.",
                    "**«Que haria distinto: nada, todo salio bien».** Con un `parcial` en el "
                    "indice y un cuello de botella identificado, esa frase se contradice con el "
                    "propio paquete. Devolver senalando la contradiccion, que es la mejor "
                    "ensenanza posible de la pregunta.",
                ],
            },
            {
                "n": 5,
                "titulo": "Evidencia del pitch y tiempos reales",
                "tipo": "abierta",
                "puntos": 15,
                "tabla": {
                    "headers": ["Seccion", "Tiempo real", "Quien hablo", "Evidencia mostrada"],
                    "rows": [
                        ["1. Problema y dominio", "1:05", "Autor del paquete",
                         "Ficha de dominio (`/informe/01-ficha-dominio.md`): las 4 capacidades y "
                         "las 3 cosas fuera de alcance"],
                        ["2. Arquitectura logica", "1:40", "Autor del paquete",
                         "Lamina unica de la pregunta 2, recorriendo estudiante -> edge -> API -> "
                         "base de datos"],
                        ["3. Contenedor y pipeline", "1:12", "Autor del paquete",
                         "`Dockerfile` en pantalla y el run verde de "
                         "`/.github/workflows/ci.yml`"],
                        ["4. Seguridad", "1:08", "Autor del paquete",
                         "Fila 3 de la tabla STRIDE (`/informe/06-amenazas.md`) y la politica de "
                         "secretos"],
                        ["5. Costos y escalabilidad", "1:20", "Autor del paquete",
                         "Tabla de costos B/M/A y la fila API de la politica de escalado "
                         "(`/informe/13-escalado.md`)"],
                        ["6. Cierre y preguntas", "1:01", "Autor del paquete",
                         "El unico `parcial` del indice, convertido en item de backlog con fecha"],
                    ],
                },
                "respuesta": (
                    "**Parte A.**\n\n"
                    "> Turno de sustentacion: **lunes 16/11/2026, 10:40 a 10:50** (sesion de "
                    "cierre del curso, 10:00 a 12:00, grupo 6303C, virtual).\n"
                    "> `paquete subido el 15/11/2026, verificado en ventana privada`\n\n"
                    "**Parte B — total real: 7:26.** Suma de la tabla (1:05 + 1:40 + 1:12 + 1:08 "
                    "+ 1:20 + 1:01) y **queda dentro de la ventana de 5:00 a 8:00**, asi que no "
                    "hace falta la linea de recorte. Vale la pena anotarlo igual, porque es lo "
                    "que se aprende de cronometrar: la unica seccion que se paso del guion de la "
                    "Clase 12 fue **arquitectura logica**, 1:40 contra 1:30 planeados, y se sabe "
                    "exactamente por que —se nombraron los cinco contenedores uno por uno en vez "
                    "de recorrer el camino del usuario sobre la lamina—. Si el turno hubiera sido "
                    "de 6 minutos, ese es el recorte: 20 segundos en la seccion 2 y 15 en la 5, "
                    "sin tocar seguridad.\n\n"
                    "**Parte C — autoevaluacion.**\n\n"
                    "> **4 de 5.** El hecho concreto: los 8 entregables del indice existen y "
                    "abren desde otra maquina, y las tres decisiones principales estan escritas "
                    "en ADR con su alternativa descartada. La nota no es 5 por un hecho igual de "
                    "concreto: el `ci.yml` corre `lint` y `build` pero no tiene etapa de pruebas, "
                    "que es el unico `parcial` del paquete y estaba planeado desde la Clase 8.\n\n"
                    "**Por que 7:26 y no 7:00 exactos, y por que eso es una buena senal.** Los "
                    "ensayos de la Clase 12 dieron 9:12, 7:35 y 6:58. El tiempo real quedo entre "
                    "el segundo y el tercer ensayo, que es lo normal: en vivo se habla un poco "
                    "mas despacio que ensayando solo. Un estudiante que reporte exactamente el "
                    "mismo tiempo de su guion probablemente no cronometro; uno que reporte 4:10 "
                    "no dio el pitch, lo leyo.\n\n"
                    "**Por que la columna «Quien hablo» existe aunque el trabajo sea individual.** "
                    "Porque la tabla es la misma para equipos autorizados y para trabajo "
                    "individual, y porque en la sustentacion en vivo el docente compara: si en la "
                    "tabla figuran dos personas y una no dijo una palabra, esa fila es una "
                    "afirmacion falsa. En trabajo individual se escribe «Autor del paquete» —no el "
                    "nombre propio— y con eso basta."
                ),
                "como_calificar": [
                    "**5 pts** la fecha y hora del **turno** —no la fecha de la clase— con la "
                    "confirmacion `paquete subido el <fecha>, verificado en ventana privada`, y "
                    "con la fecha de subida **anterior** al turno. Si el paquete se subio durante "
                    "la sesion, estos 5 pts no se dan: es la unica regla dura de la entrega y hay "
                    "que anunciarla antes.",
                    "**6 pts** la tabla de **6 filas** —las mismas 6 secciones del guion de la "
                    "Clase 12, en el mismo orden— con tiempo real, quien hablo y evidencia "
                    "mostrada. 1 pt por fila. Una fila sin evidencia concreta vale la mitad.",
                    "**3 pts** el total en minutos y segundos **entre 5:00 y 8:00**, o la linea de "
                    "recorte si se paso. La suma se verifica: es la aritmetica mas facil de "
                    "revisar del taller y falla mas de lo que deberia.",
                    "**1 pt** la autoevaluacion de 1 a 5 con **hecho concreto**. «Me esforce "
                    "mucho» no es un hecho; «los 8 entregables abren desde otra maquina» si. Es "
                    "1 punto, pero conviene leerlo con atencion: una autoevaluacion de 5 en un "
                    "paquete con tres `parcial` dice mas del estudiante que toda la reflexion de "
                    "la pregunta 4.",
                    "Se contrasta con lo que ocurrio en vivo. Los tiempos declarados y las "
                    "evidencias mostradas deben coincidir con lo que el docente vio: esta "
                    "pregunta es la unica del curso que se califica con dos fuentes.",
                ],
                "errores": [
                    "**Confundir la fecha de la clase con la del turno.** El turno es una franja "
                    "de 10 minutos dentro de la sesion; escribir «16/11/2026» sin hora no cumple "
                    "y cuesta parte de los 5 pts.",
                    "**Paquete subido el mismo dia, minutos antes del turno o durante la "
                    "sesion.** Es exactamente lo que la Parte A esta disenada para desincentivar. "
                    "Se detecta con la fecha del commit o del archivo, no con lo que diga la "
                    "linea.",
                    "**Tiempos «planeados» disfrazados de reales:** seis filas de 1:10 exactos que "
                    "suman 7:00 redondos. Nadie habla asi. Se detecta por la sospechosa "
                    "regularidad y significa que no hubo cronometro; devolver pidiendo el ensayo "
                    "con el celular en la mano.",
                    "**Total fuera de la ventana sin linea de recorte.** Si el pitch dio 9:40 y "
                    "no hay linea de que se recortaria, se pierden los 3 pts. La linea de recorte "
                    "salva la pregunta: pasarse no es el problema, no saber que sobra si.",
                    "**Columna de evidencia vacia o generica** («las diapositivas»). La evidencia "
                    "es el artefacto concreto que estuvo en pantalla, con su ruta si la tiene. Es "
                    "lo que permite auditar la sustentacion despues.",
                    "**Autoevaluacion de 5 sin hecho, o de 3 por modestia.** Las dos son "
                    "igualmente inutiles. Lo que se pide es un hecho verificable que sostenga el "
                    "numero, en cualquier direccion.",
                ],
            },
        ],
        "preguntas_frecuentes": [
            ("¿Puedo poner `parcial` en varias filas o me castiga?",
             "Puede, y no castiga: el `parcial` bien declarado —con el faltante entre parentesis— "
             "no descuenta un solo punto. Lo que descuenta es un `completo` que no lo es, porque "
             "eso se comprueba abriendo el archivo. Y hay un beneficio adicional: cada `parcial` "
             "honesto es material para la pregunta 3, donde un pendiente convertido en decision "
             "puntua completo."),
            ("Mis enlaces funcionan perfecto. ¿Igual tengo que hacer la verificacion?",
             "Si, y son 6 de los 25 puntos de la pregunta 1. «Funcionan perfecto» casi siempre "
             "significa «funcionan con mi sesion abierta». La verificacion son tres pasos y dos "
             "minutos: ventana privada, pegar el enlace, pasar de pagina en el PDF. El error de "
             "permisos es el que mas entregas ha hundido en este curso y es el mas facil de "
             "evitar."),
            ("¿La lamina unica puede ser el C4 Container que ya tengo?",
             "No, y es la trampa mas comun de la pregunta 2. La lamina de sustentacion tiene "
             "cosas que el C4 Container no tiene: zonas con subred, puertos, el rango de replicas "
             "y la cadena de entrega. Es una consolidacion del semestre en una sola pantalla, no "
             "un diagrama reciclado."),
            ("El enunciado dice `2 a 6 replicas` pero mi politica dice otro rango. ¿Cual pongo?",
             "El suyo, siempre. El `2 a 6` es un ejemplo de formato. Lo que se califica es la "
             "coherencia con la politica de la Clase 13, y copiar el numero del enunciado teniendo "
             "otro en su tabla es justo la incoherencia que la pregunta busca. En BiblioLite el "
             "rango es `1 a 4` y hay una razon tecnica detras: 4 replicas por 5 conexiones son las "
             "20 que acepta el motor."),
            ("En la pregunta 3, ¿que hago si de verdad no alcance a hacer algo?",
             "Convertirlo en decision, que es lo que el enunciado pide literalmente: «lo dejamos "
             "fuera a proposito porque...» y decir que gano el proyecto con eso. La version que "
             "vale cero es «no alcanzamos»; la version que vale todos los puntos es «el pipeline "
             "con pruebas exigia escribir la suite y preferi cerrar seguridad y escalado, que "
             "pesan mas en la rubrica; queda como B-01 con fecha». Es la misma informacion, dicha "
             "como profesional."),
            ("¿Cual es el activo mas sensible de mi dominio? Puse las contrasenas.",
             "Casi seguro que no son las contrasenas: si la identidad la maneja un proveedor "
             "institucional, su sistema no las guarda. El activo sensible es el **dato del "
             "dominio** que revela algo de una persona: en una biblioteca, el historial de "
             "lectura; en una veterinaria, la historia clinica; en un sistema de turnos, con quien "
             "se cito el paciente. Darse cuenta de eso es la mitad de la respuesta."),
            ("Cronometre y me dio 9:40. ¿Pierdo puntos?",
             "Solo si no escribe que recortaria. La ventana es de 5:00 a 8:00 y pasarse es normal "
             "en el primer intento —los ensayos de la Clase 12 empezaron en 9:12—; lo que se "
             "califica es que sepa **que sobra**. Una linea concreta («20 segundos en arquitectura "
             "logica y 15 en costos, sin tocar seguridad») salva los 3 pts y ademas es lo que hay "
             "que hacer si el turno se acorta en vivo."),
            ("Trabaje solo. ¿Que pongo en la columna «Quien hablo»?",
             "«Autor del paquete» en las seis filas, sin el nombre propio. La columna existe "
             "porque la tabla sirve tambien para los equipos autorizados, y ahi si se compara con "
             "lo que el docente vio en vivo: una fila que atribuya la explicacion a alguien que no "
             "hablo es una afirmacion falsa. En trabajo individual la columna es un formalismo, y "
             "esta bien que lo sea."),
        ],
        "cierre": (
            "El curso cierra sin agregar arquitectura: hoy solo se defiende la que ya existe. Lo "
            "que queda en las manos del estudiante es un paquete indexado y verificado desde otra "
            "maquina, una lamina de 11 nodos que explica el sistema en 60 segundos, tres "
            "respuestas con evidencia y trade-off, y un pitch de 7:26 cronometrado de verdad. Y "
            "queda algo que no esta en la rubrica y es lo que se lleva al trabajo: la capacidad "
            "de decir «esto lo dejamos fuera a proposito porque...» en vez de «no alcanzamos». "
            "Todas las decisiones de BiblioLite —el modelo de servicio, el monolito modular, las "
            "cinco piezas, el minimo de una replica, el ci.yml sin pruebas— estan escritas con su "
            "alternativa descartada y con lo que costaron. Eso es arquitectura de software: no la "
            "lista de tecnologias, sino el registro de por que se decidio asi y que se acepto "
            "perder."
        ),
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


def opciones(n: int, num: int):
    """(opciones, indices correctos) de una pregunta cerrada, leidas de ExamLab.

    La clave se lee de la misma fuente que ve el estudiante: asi no puede quedar
    una solucion marcando una opcion que en la plataforma ya no es la correcta.
    En las Clases 1-4 y 6-10 se busca por numero GLOBAL, porque varias clases
    comparten una actividad; en los talleres propios (11, 12, 13 y 15) el banco no
    trae n_global y se busca por la posicion en la lista, que es el numero local.
    """
    banco = (EXAMLAB.get(n) or {}).get("preguntas", [])
    for i, p in enumerate(banco):
        if not p.get("opciones"):
            continue
        propio = p.get("n_global") if p.get("n_global") is not None else i + 1
        if propio == num:
            return p["opciones"], set(p.get("correctas") or [])
    return [], set()
