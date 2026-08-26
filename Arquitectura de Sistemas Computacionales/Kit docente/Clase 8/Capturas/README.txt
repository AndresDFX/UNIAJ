Capturas de la Clase 8 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Ya generadas por `python config/slides/mockups.py` (no hay que tomarlas):
  - salida-actions-run.png — Run verde del workflow: build + test reales, no un `echo ok`

Pendiente: demo-clase08.png — la herramienta del dia en uso
  1. Abrir GitHub Actions · Google Docs.
  2. Repetir la demo: Un workflow de GitHub Actions que corra de verdad.
     1. Cree `.github/workflows/ci.yml` con on: push, un job y 3 steps: checkout, setup, y un comando de prueba real.
     2. Haga commit y push, y abra la pestana Actions del repositorio para ver el run.
     3. Espere el check verde y senale el log del step: «esto es evidencia, no una diapositiva que dice que tenemos CI».
     4. Aclare la frontera: el pipeline llega hasta «listo para desplegar»; no despliega a ningun servidor real en este curso.
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase08.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=8 python config/slides/build_uniajc_arq_clases_batch.py
