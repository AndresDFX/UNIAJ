Capturas de la Clase 3 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Ya generadas por `python config/slides/mockups.py` (no hay que tomarlas):
  - salida-docker-build-run.png — Build y run del stub en LabEx Docker Playground (lo que debe verse en pantalla)
  - salida-docker-ps.png — Evidencia del entregable: el contenedor corriendo (`docker ps`)

Pendiente: demo-clase03.png — la herramienta del dia en uso
  1. Abrir LabEx Docker Playground · alterna si no carga: Killercoda.
  2. Repetir la demo: Construir y correr el stub en LabEx Docker Playground.
     1. Abra labex.io e inicie sesion con su cuenta de Google o Microsoft (advierta en voz alta: la sesion es temporal, guarden capturas antes de cerrarla).
     2. Escriba un Dockerfile minimo en vivo: FROM nginx:alpine y COPY de un index.html de una linea.
     3. Ejecute docker build -t cloudlite-stub . y luego docker run -d -p 80:80 cloudlite-stub.
     4. Ejecute docker ps y senale las columnas IMAGE, STATUS y PORTS: «esta es la evidencia que entregan».
     5. Si la red falla, proyecte las capturas de `Kit docente/Clase 3/Capturas/`.
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase03.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=3 python config/slides/build_uniajc_arq_clases_batch.py
