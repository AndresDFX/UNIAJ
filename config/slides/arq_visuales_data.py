# -*- coding: utf-8 -*-
"""Que visual acompana a cada concepto de Arquitectura: animacion o nada.

Clave: el comienzo del titulo de la seccion `###` de `arq_fundamentos.FUNDAMENTOS` (se compara
normalizado: sin tildes ni mayusculas). Valor:

- ``anim``: `arq/claseN/<huella>` en `config/animaciones/` (renderizada por `renderizar.py`). En
  la lamina, sus pasos aparecen uno por clic del docente.

Las fotos de Pexels se retiraron (2026-10): una imagen «por poner imagen» no explica nada. Las
laminas de viñetas sin animacion llevan su ILUSTRACION generada (`arq_ilustraciones_cN.py`).

Una seccion sin entrada se queda en texto a ancho completo: el visual se pone donde explica, no
por decorar. Tampoco llevan visual las secciones que el build reemplaza por su lamina curada
(`slides_extra` con el mismo titulo), las de codigo ni las que tienen detras su diagrama.
Las animaciones no nombran el proyecto ni la plataforma: el ejemplo es «la app de turnos».
"""

VISUALES = {
    1: {
        "La ficha de dominio": {"anim": "arq/clase1/ficha-cinco-bloques"},
        "Ejemplo de diagrama C4 - nivel Context": {"anim": "arq/clase1/c4-context"},
    },
    2: {
        "La pila de responsabilidades": {"anim": "arq/clase2/pila-responsabilidades"},
        "IaaS, PaaS y SaaS: los tres cortes": {"anim": "arq/clase2/tres-cortes"},
        "El ADR-001": {"anim": "arq/clase2/adr-seis-secciones"},
    },
    3: {
        "Antes de la virtualizacion": {"anim": "arq/clase3/un-servidor-por-app"},
        "Recorrer el diagrama de las dos pilas": {"anim": "arq/clase3/dos-pilas"},
        "El contenedor: aislamiento": {"anim": "arq/clase3/contenedor-aislado"},
        "Dockerfile, imagen, contenedor y registro": {"anim": "arq/clase3/receta-imagen-contenedor"},
        "Primer ejemplo: el stub": {"anim": "arq/clase3/capas-cache"},
    },
    4: {
        "De donde viene la clase y que se abre hoy": {"anim": "arq/clase4/caja-negra-abre"},
        "Monolito": {"anim": "arq/clase4/monolito-vs-micro"},
        "Las tres reglas del nivel Container": {"anim": "arq/clase4/tres-reglas-container"},
        "Primer ejemplo: los tres contenedores": {"anim": "arq/clase4/cuarta-caja"},
        "Los contratos": {"anim": "arq/clase4/contrato-cuatro-datos"},
        "Lo que se paga al distribuir": {"anim": "arq/clase4/red-vs-funcion"},
        "Timeout, reintento": {"anim": "arq/clase4/reintento-idempotente"},
        "Los datos: donde se rompen": {"anim": "arq/clase4/base-compartida"},
        "Los tres riesgos de distribuir": {"anim": "arq/clase4/riesgo-que-sigue"},
    },
    6: {
        "Seguridad como propiedad del diseno": {"anim": "arq/clase6/triada-cia"},
        "Modelar amenazas": {"anim": "arq/clase6/cuatro-preguntas"},
        "STRIDE": {"anim": "arq/clase6/stride"},
        "Los controles gratuitos": {"anim": "arq/clase6/validar-en-servidor"},
        "Menor privilegio": {"anim": "arq/clase6/menor-privilegio"},
        "Gestion de secretos": {"anim": "arq/clase6/secreto-en-capas"},
        "La politica en cuatro respuestas": {"anim": "arq/clase6/politica-cuatro-respuestas"},
        "Primer ejemplo: autenticacion con token": {"anim": "arq/clase6/token-vida-corta"},
        "Segundo ejemplo: PII": {"anim": "arq/clase6/mensaje-que-revela"},
        "Amenaza, control y donde se ve": {"anim": "arq/clase6/donde-se-ve"},
    },
    7: {
        "El tercer angulo": {"anim": "arq/clase7/tres-angulos"},
        "IP, puerto y protocolo": {"anim": "arq/clase7/ip-puerto-protocolo"},
        "Subred publica y privada": {"anim": "arq/clase7/rutas-subred"},
        "DNS y balanceador": {"anim": "arq/clase7/dns-balanceador"},
        "Los tres nombres de almacenamiento": {"anim": "arq/clase7/tres-almacenamientos"},
        "El caso de la foto de perfil": {"anim": "arq/clase7/foto-perfil"},
        "Trazabilidad: la tabla": {"anim": "arq/clase7/trazabilidad-tabla"},
        "Recorrer una peticion": {"anim": "arq/clase7/peticion-punta-a-punta"},
    },
    8: {
        "Integracion continua": {"anim": "arq/clase8/ci-ciclo"},
        "Entrega continua y despliegue continuo": {"anim": "arq/clase8/cd-ambigua"},
        "GitHub Actions en cinco palabras": {"anim": "arq/clase8/actions-piezas"},
        "Los tres bloques de un workflow": {"anim": "arq/clase8/orden-pasos"},
        "Monitorear y observar": {"anim": "arq/clase8/metricas-vs-logs"},
        "Las cuatro senales de oro": {"anim": "arq/clase8/cuatro-senales"},
        "La tabla de senales": {"anim": "arq/clase8/senal-umbral"},
        "La condicion de fallo": {"anim": "arq/clase8/ci-que-falla"},
        "Donde se ejecuta de verdad la politica": {"anim": "arq/clase8/secretos-enmascarados"},
    },
    10: {
        "Clase autonoma: de gasto de capital": {"anim": "arq/clase10/capex-opex"},
        "Ordenes de magnitud": {"anim": "arq/clase10/ordenes-magnitud"},
        "Primer ejemplo: la tabla de costos": {"anim": "arq/clase10/escala-ordinal"},
        "Segundo ejemplo: por que el driver": {"anim": "arq/clase10/egress-driver"},
        "Right-sizing": {"anim": "arq/clase10/right-sizing"},
    },
    11: {
        "El insumo: las seis piezas": {"anim": "arq/clase11/seis-piezas"},
        "Las cinco preguntas de coherencia": {"anim": "arq/clase11/cinco-cadenas"},
        "Scope creep": {"anim": "arq/clase11/dos-patologias"},
        "Retroalimentacion accionable": {"anim": "arq/clase11/retro-cuatro-partes"},
        "El semaforo": {"anim": "arq/clase11/semaforo"},
    },
    12: {
        "Latencia, throughput y concurrencia": {"anim": "arq/clase12/latencia-throughput"},
        "Por que el promedio miente": {"anim": "arq/clase12/promedio-percentil"},
        "Los umbrales de percepcion": {"anim": "arq/clase12/umbrales-percepcion"},
        "El escenario de carga": {"anim": "arq/clase12/aritmetica-servilleta"},
        "El cuello de botella": {"anim": "arq/clase12/cuello-botella"},
        "Los tipos de prueba": {"anim": "arq/clase12/tipos-prueba"},
        "El ensayo del pitch": {"anim": "arq/clase12/pitch-presupuesto"},
    },
    13: {
        "Escalar vertical y horizontalmente": {"anim": "arq/clase13/vertical-horizontal"},
        "Ausencia de estado": {"anim": "arq/clase13/sesion-en-memoria"},
        "Las cinco piezas del autoescalado": {"anim": "arq/clase13/cinco-piezas-autoescalado"},
        "El limite fisico": {"anim": "arq/clase13/arranque-no-instantaneo"},
        "Elegir la metrica": {"anim": "arq/clase13/metrica-correcta"},
        "Lo que NO escala": {"anim": "arq/clase13/lo-que-no-escala"},
    },
    15: {
        "Sustentar no es describir": {"anim": "arq/clase15/describir-vs-sustentar"},
        "La prueba de tres capas": {"anim": "arq/clase15/tres-capas"},
        "El pitch de 5 a 8 minutos": {"anim": "arq/clase15/pitch-reparto"},
        "El Q&A tecnico": {"anim": "arq/clase15/qa-tres-tipos"},
    },
}


#: Laminas de CODIGO de diagramas (Mermaid C4): el texto solo no se entiende, asi que a su
#: derecha va lo que ese codigo DIBUJA (`pseudo_code_slide(..., imagen=...)`), y sus notas
#: llevan el guion para darla. Clave: comienzo del titulo de la lamina.
CODIGO_DIAGRAMA = {
    4: {
        "Las tres reglas del C4 Container": {
            "anim": "arq/clase4/ilus-c4-reglas",
            "notas": {
                "min": 3,
                "explica": "En Mermaid un diagrama C4 se escribe como texto. A la izquierda está ese "
                           "texto; a la derecha, lo que dibuja. El visor dibuja cualquier cosa que "
                           "tenga la sintaxis correcta, pero hay tres reglas que no revisa por ti.",
                "pasos": [
                    "Lee el código línea por línea señalando su caja en el dibujo: Container → la "
                    "caja de la API; ContainerDb → el cilindro; Rel → la flecha con su rótulo.",
                    "Regla 1: el tercer dato del Container es la tecnología (Node.js). Sin ella, "
                    "el diagrama no dice con qué se construye.",
                    "Regla 2: lo que guarda datos se declara ContainerDb, por eso sale como "
                    "cilindro y no como una caja más.",
                    "Regla 3: cada Rel lleva verbo («INSERT y SELECT») y protocolo/formato "
                    "(«TCP/SQL»). «usa» no le dice nada a quien lee.",
                ],
                "ejemplo": "Mal: Container(api, \"API\") — sin tecnología. Rel(api, db, \"usa\") — sin "
                           "verbo concreto ni protocolo.",
                "preguntas": [
                    ("¿Dónde pruebo el código?",
                     "En cualquier visor de Mermaid (por ejemplo mermaid.live): se pega el texto y "
                     "se ve el dibujo."),
                ],
                "cuidado": "Los nombres (api, db) se repiten idénticos en el diagrama de Despliegue "
                           "y en el de Componentes: si cambian, ya no se puede seguir una pieza entre "
                           "diagramas.",
                "puente": "Ahora el diagrama completo de la app de turnos con el mismo molde.",
            },
        },
        "C4Container en Mermaid: el molde": {
            "anim": "arq/clase4/ilus-c4-molde",
            "notas": {
                "min": 4,
                "explica": "Es el diagrama de contenedores completo de una app de turnos: quién la "
                           "usa, de qué piezas está hecha por dentro y con qué sistema externo habla.",
                "pasos": [
                    "Arriba del código y del dibujo: Person es el cliente, fuera del sistema. "
                    "System_Boundary es el recuadro punteado: todo lo que va dentro es nuestro.",
                    "Dentro, los cuatro contenedores: app web (React), API (Node.js), base "
                    "(PostgreSQL, cilindro) y worker de avisos. Fuera, el correo, en gris "
                    "porque es un sistema externo.",
                    "Recorre las Rel en el orden de una reserva: el cliente reserva por HTTPS, la "
                    "app hace POST a la API, la API escribe en la base y publica un evento, el "
                    "worker envía el correo.",
                ],
                "ejemplo": "Seguir una reserva de punta a punta sobre el dibujo es la mejor prueba de "
                           "que el diagrama está completo.",
                "preguntas": [
                    ("¿Por qué el correo va fuera del recuadro?",
                     "Porque no lo construimos ni lo operamos: es un servicio de terceros. Los "
                     "externos siempre van fuera del System_Boundary."),
                ],
                "cuidado": "Si un contenedor no tiene ninguna flecha, sobra o falta una relación.",
                "puente": "Con este molde se arma el diagrama de cualquier sistema.",
            },
        },
    },
}
