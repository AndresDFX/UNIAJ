Capturas de la Clase 15 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Pendiente: demo-clase15.png — la herramienta del dia en uso
  1. Abrir Google Docs/Slides · diagramas · capturas lab.
  2. Repetir la demo: Modelar una sustentacion de 6 minutos y un Q&A.
     1. Presente usted mismo un CloudLite de ejemplo en 6 minutos cronometrados, con la estructura: problema, decision clave, evidencia, limite conocido.
     2. Hagase una pregunta dificil en voz alta y respondala: «por que no uso microservicios? Porque el proyecto lo sostiene una sola persona y la frontera no se justificaba».
     3. Muestre la rubrica proyectada y senale donde habria perdido puntos su propia demo.
     4. Recuerde la regla de los 60 segundos: quien sustenta debe poder explicar cualquier parte del paquete, y si hubo equipo autorizado, cualquier integrante.
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase15.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=15 python config/slides/build_uniajc_arq_clases_batch.py
