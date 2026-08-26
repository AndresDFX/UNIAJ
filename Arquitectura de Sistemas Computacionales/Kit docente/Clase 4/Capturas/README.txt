Capturas de la Clase 4 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Pendiente: demo-clase04.png — la herramienta del dia en uso
  1. Abrir draw.io / diagrams.net.
  2. Repetir la demo: Convertir el Context de la Clase 1 en Containers.
     1. Abra el diagrama C4 Context de la demo de Clase 1 y haga zoom a la caja «CloudLite App».
     2. Reemplace esa caja por 3 cajas internas: «API (REST)», «Base de datos» y «Worker de notificaciones».
     3. Rotule CADA flecha con protocolo y formato: «HTTPS/JSON», «TCP/SQL». Sin flechas sin etiqueta.
     4. Pregunte al grupo por que el worker esta separado; si nadie da una razon de negocio, borrelo en vivo: «eso es microservicios teatro».
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase04.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=4 python config/slides/build_uniajc_arq_clases_batch.py
