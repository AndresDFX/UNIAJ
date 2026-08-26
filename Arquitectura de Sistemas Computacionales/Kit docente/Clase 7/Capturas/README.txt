Capturas de la Clase 7 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Pendiente: demo-clase07.png — la herramienta del dia en uso
  1. Abrir draw.io.
  2. Repetir la demo: Dibujar zonas de confianza sobre el diagrama de despliegue.
     1. En draw.io dibuje dos rectangulos grandes rotulados «Subred publica» y «Subred privada».
     2. Ponga el balanceador en la publica y la base de datos en la privada; dibuje la flecha API -> BD cruzando de una a otra.
     3. Pregunte: «si un atacante llega desde internet, con que se topa primero?» — eso es superficie de exposicion.
     4. Verifique en voz alta que los nombres de los servicios son LOS MISMOS del C4 Containers de la Clase 4.
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase07.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=7 python config/slides/build_uniajc_arq_clases_batch.py
