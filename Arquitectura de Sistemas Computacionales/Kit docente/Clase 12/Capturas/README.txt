Capturas de la Clase 12 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Pendiente: demo-clase12.png — la herramienta del dia en uso
  1. Abrir Google Docs · draw.io · (opcional) lab contenedor.
  2. Repetir la demo: Definir un objetivo de rendimiento que si se puede verificar.
     1. Escriba la frase mala: «la app debe ser rapida». Pregunte al grupo como la comprobarian; deje que fallen.
     2. Reescribala en vivo: «el p95 del endpoint de consulta responde en menos de 300 ms con 50 peticiones por segundo».
     3. Explique el p95 con 20 numeros en el tablero: ordene y marque el que deja 95% por debajo.
     4. Cierre pidiendo el bottleneck sospechado: «cual pieza creen que revienta primero, y por que esa».
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase12.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=12 python config/slides/build_uniajc_arq_clases_batch.py
