Capturas de la Clase 6 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Ya generadas por `python config/slides/mockups.py` (no hay que tomarlas):
  - salida-secreto-en-imagen.png — Por que un secreto NUNCA va dentro de la imagen (demo de 1 minuto)

Pendiente: demo-clase06.png — la herramienta del dia en uso
  1. Abrir Excalidraw · Google Docs.
  2. Repetir la demo: De amenaza STRIDE a control verificable, en vivo.
     1. Escriba en el tablero: «Tampering: alguien cambia el precio de un item via la API sin permiso».
     2. Pregunte al grupo cual seria el control; guie hasta «autenticacion + validacion de rol antes de aceptar el cambio».
     3. Agregue la columna Evidencia: «en que archivo o diagrama se ve ese control» — sin evidencia, el control no cuenta.
     4. Demo de 1 minuto del anti-patron: muestre un Dockerfile con una API key escrita en texto plano y explique que queda en el historial de la imagen para siempre.
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase06.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=6 python config/slides/build_uniajc_arq_clases_batch.py
