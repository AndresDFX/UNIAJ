Capturas de la Clase 10 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Pendiente: demo-clase10.png — la herramienta del dia en uso
  1. Abrir Google Docs.
  2. Repetir la demo: Tabla de costo cualitativo en 5 minutos.
     1. Dibuje 3 columnas: Componente | Costo (Bajo/Medio/Alto) | Driver del costo.
     2. Llene 3 filas de CloudLite: base de datos gestionada (Alto, computo+almacenamiento constante 24/7), API en contenedor (Medio, numero de instancias), object storage de imagenes (Bajo, volumen de datos).
     3. Pregunte cual bajaria primero si el presupuesto se corta a la mitad, y exija que justifiquen con el driver, no con intuicion.
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase10.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=10 python config/slides/build_uniajc_arq_clases_batch.py
