# -*- coding: utf-8 -*-
"""BD II · Clase 5 · Parcial 1: GUION de las láminas «Indicaciones» y de cierre (la portada no).

Cómo conducir la sesión de parcial por Meet: tiempos, canal de entrega, dudas y desconexiones.
Nada del contenido del examen. Fuente: la guía de aplicación del parcial que arma
`build_uniajc_bd2_all._guia_parcial_cuerpo` y la portada del instrumento
(`config/parciales/contenido_parciales_2026_2.BD2_P1`): lunes 21/09/2026, 18:00-20:00, Clases 1 a 4.
"""

CONTENIDO = {
    5: {
        "Indicaciones": {
            "notas": {
                "min": 15,
                "explica": "Hoy es el Parcial 1: solo evaluación, sin tema nuevo, por Meet como "
                           "todas las sesiones. Esta lámina responde lo que todos preguntan al "
                           "minuto 0: qué entra, cuánto dura y cómo se entrega.",
                "pasos": [
                    "Minutos 0-10. Pasa lista y, con esta lámina en pantalla, anuncia cuatro cosas: "
                    "el canal de entrega (decídelo antes de abrir: el documento editable compartido "
                    "por el chat y devuelto por el mismo canal o por correo), el cierre del envío "
                    "en el minuto 110 (19:50), el material autorizado (por defecto, ninguno) y que "
                    "las dudas de contenido no se responden.",
                    ("Minutos 10-15",
                     "Comparte el enunciado por el chat y confirma en voz alta que todos lo abrieron "
                     "antes de arrancar el reloj. Deja esta lámina proyectada: ahorra la mitad de "
                     "los mensajes por privado."),
                    ("Minutos 15-100",
                     "Silencio de evaluación con cámara y micrófono abiertos, que es la única "
                     "supervisión posible. Avisa el tiempo a los 50 y a los 80 minutos."),
                    ("Si alguien se desconecta",
                     "Que siga respondiendo el documento sin conexión y te escriba por correo al "
                     "reconectarse; anota la hora. El tiempo perdido por una caída comprobable no "
                     "se descuenta, y ese criterio se anuncia al minuto 0 para que nadie lo use "
                     "después como excusa."),
                ],
                "ejemplo": "Dudas que sí se responden: «¿esto pide una consulta o una explicación?», "
                           "«¿el punto b) es obligatorio?», «no puedo abrir el archivo». Dudas que "
                           "no: «¿esta opción es la correcta?». La respuesta, igual para todos: «Eso "
                           "es lo que la pregunta evalúa; responde con lo que recuerdes de la "
                           "clase».",
                "preguntas": [
                    ("¿Qué entra?",
                     "Las Clases 1, 2, 3 y 4. La portada del enunciado las lista con su fecha y "
                     "trae el reparto de puntos por sección."),
                    ("¿Puedo usar mis apuntes?",
                     "Lo que anunciaste al minuto 0, y por defecto no. No lo cambies a mitad del "
                     "parcial: invalida el de quien ya respondió sin ellos."),
                    ("¿Tengo que ejecutar el SQL?",
                     "No: se responde escrito y se califica la lógica de la consulta. No se pide "
                     "captura de ejecución."),
                ],
                "cuidado": "Decide el canal de entrega antes de abrir la sesión: si no lo anuncias "
                           "al minuto 0, lo vas a improvisar al minuto 105 con medio grupo "
                           "escribiendo por privado.",
                "puente": "Al minuto 100, pasa a la lámina de cierre para recibir las entregas.",
            },
        },
        "Parcial 1 · Clase 5": {
            "notas": {
                "min": 20,
                "explica": "Los últimos veinte minutos: recibir las entregas, confirmar a cada uno "
                           "que su archivo llegó y cerrar sin comentar el parcial.",
                "pasos": [
                    "Minuto 100: aviso de 10 minutos. Proyecta esta lámina mientras llegan los "
                    "archivos.",
                    ("Minutos 100-110",
                     "Acusa recibo por el chat, uno por uno, con el nombre y la hora de cada "
                     "archivo que llega. Anota quién no ha entregado."),
                    ("Minuto 110",
                     "Cierra el envío. A quien se desconectó, recíbele el archivo por correo con la "
                     "hora anotada y aplica el criterio anunciado al minuto 0."),
                    ("Minutos 110-120",
                     "Cierre: «hoy solo se evaluó; la próxima clase, el 28 de septiembre, es "
                     "Optimización de consultas (Clase 6)». Ningún comentario sobre las respuestas: "
                     "todavía hay quien está enviando."),
                ],
                "ejemplo": "Acuse en el chat: «Recibido: (nombre), 19:46». Con eso no hay reclamo "
                           "posible sobre una entrega perdida.",
                "preguntas": [
                    ("¿Cuándo veo la nota?",
                     "En la siguiente sesión, con la retroalimentación escrita sobre el mismo "
                     "documento que entregaste."),
                    ("Se me cayó el internet y no alcancé a enviar, ¿qué hago?",
                     "Envíalo por correo apenas te reconectes. Si la caída es comprobable, no se "
                     "descuenta."),
                ],
                "cuidado": "No resuelvas preguntas del parcial en voz alta al cerrar, ni siquiera "
                           "«la fácil»: hay quien todavía está enviando y cualquier comentario se "
                           "vuelve pista.",
                "puente": "Próxima sesión: Clase 6, Optimización de consultas.",
            },
        },
    },
}
