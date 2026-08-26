Capturas de la Clase 2 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Pendiente: demo-clase02.png — la herramienta del dia en uso
  1. Abrir Google Docs · draw.io (opcional).
  2. Repetir la demo: Llenar un ADR-001 delante del grupo, en 6 lineas.
     1. Abra un Google Doc y escriba los 4 encabezados del ADR: Contexto, Opciones, Decision, Consecuencias.
     2. Contexto: «CloudLite necesita correr una API y una base de datos; lo desarrolla una persona en un semestre y con cero presupuesto».
     3. Opciones: IaaS (control total, mas trabajo operativo) · PaaS (menos control, menos operacion) · SaaS (no aplica, no compramos software hecho).
     4. Decision: PaaS conceptual + contenedores. Consecuencias: se acepta menos control del sistema operativo a cambio de no administrar servidores.
     5. Diga: «un ADR de media pagina que se entiende vale mas que 5 paginas que nadie lee».
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase02.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=2 python config/slides/build_uniajc_arq_clases_batch.py
