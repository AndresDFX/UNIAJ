Capturas de la Clase 7 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Pendiente: demo-clase07.png — la herramienta del dia en uso
  1. Abrir ExamLab (Mermaid) · boceto en draw.io o Excalidraw.
  2. Repetir la demo: Del boceto de tres zonas al Mermaid que se califica.
     1. En draw.io o Excalidraw dibuje TRES rectangulos, rotulados «Zona publica», «Zona privada» y «Zona de datos».
     2. Reparta las cajas de CloudLite: `Edge / balanceador` y `App web` en la publica, `API CloudLite` en la privada, `Base de datos` en la de datos — nunca en la publica. El `Cliente / navegador` va FUERA de las tres zonas: es el actor, no algo que usted despliegue, y esa es una de las dos filas sin par de la pregunta 6.
     3. Etiquete cada flecha con su puerto (443 al edge, 8080 a la API, 5432 a la base de datos) y saque una flecha aparte a la `Pasarela de pagos` externa: ahi esta la frontera de confianza, y son 2 de los 14 pts.
     4. Pregunte: «si un atacante llega desde internet, con que se topa primero?» — eso es superficie de exposicion.
     5. Traduzca ese boceto a Mermaid (el codigo de referencia esta abajo), peguelo en la pregunta 4 de ExamLab y proyectelo RENDERIZADO: 2 de los 14 pts son que renderice sin error.
     6. Verifique en voz alta que los nombres de los servicios son LOS MISMOS del C4 Containers de la Clase 4.
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase07.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=7 python config/slides/build_uniajc_arq_clases_batch.py
