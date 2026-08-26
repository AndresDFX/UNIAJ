Capturas de la Clase 11 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Pendiente: demo-clase11.png — la herramienta del dia en uso
  1. Abrir draw.io · GitHub · Google Docs.
  2. Repetir la demo: Auditar en vivo el paquete de un voluntario.
     1. Pida a un estudiante voluntario (o a un equipo, si autorizo equipos) que proyecte su C4 Containers y su diagrama de despliegue lado a lado.
     2. Compare nombre por nombre: todo servicio del Containers debe existir en el despliegue y viceversa.
     3. Senale en voz alta el primer gap concreto que encuentre y escribalo como accion con responsable y fecha.
     4. Modele el tono: el hallazgo es sobre el artefacto, nunca sobre la persona.
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase11.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=11 python config/slides/build_uniajc_arq_clases_batch.py
