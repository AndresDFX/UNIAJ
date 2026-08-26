Capturas de la Clase 1 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Ya generadas por `python config/slides/mockups.py` (no hay que tomarlas):
  - demo-clase01.png — C4 Context de la demo en vivo: asi debe quedar el tablero al terminar

Pendiente: demo-clase01.png — la herramienta del dia en uso
  1. Abrir Padlet · Excalidraw / draw.io.
  2. Repetir la demo: Dibujar en vivo el C4 Context de un CloudLite de ejemplo.
     1. Abra draw.io en blanco y dibuje UNA caja al centro rotulada «CloudLite App».
     2. Agregue 2 monigotes a la izquierda (Usuario final, Administrador) con flechas rotuladas «consulta», «administra».
     3. Agregue 1 caja gris a la derecha rotulada «Pasarela de pagos (externo)» y una flecha «cobra».
     4. Diga en voz alta: «no dibuje que hay ADENTRO de la caja; eso es Clase 4».
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase01.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=1 python config/slides/build_uniajc_arq_clases_batch.py
