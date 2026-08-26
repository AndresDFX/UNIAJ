Capturas de la Clase 13 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Pendiente: demo-clase13.png — la herramienta del dia en uso
  1. Abrir Google Docs · draw.io (opcional nota en Deployment).
  2. Repetir la demo: Vertical vs horizontal, y lo que NO escala.
     1. Dibuje una caja «API» y agrandela: eso es vertical (mas CPU/RAM a la misma maquina, con techo fisico).
     2. Borre y dibuje 3 cajas «API» iguales con un balanceador arriba: eso es horizontal.
     3. Agregue la base de datos abajo, conectada a las 3, y encierrela en rojo: «esta no se multiplica igual; aqui esta el limite real».
     4. Escriba el trigger y el limite: «CPU > 70% por 5 min -> +1 instancia, maximo 4» y amarre con el costo de la Clase 10.
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase13.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=13 python config/slides/build_uniajc_arq_clases_batch.py
