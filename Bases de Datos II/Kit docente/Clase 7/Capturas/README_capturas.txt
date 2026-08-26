Capturas de la Clase 7 — Bases de Datos II
==============================================

El guion embebe automaticamente cualquier PNG que exista en esta carpeta con
el nombre esperado. Mientras no exista, el .docx imprime la receta en su lugar.

1) cap01_demo.png — salida de la demo del docente
   - Abrir DB Fiddle + draw.io (opcional) y repetir la demo: CREATE INDEX idx_cita_fecha; consulta que lo usaria.
   - Capturar solo la ventana con el resultado (no el escritorio completo).
   - Recortar a ~1200 px de ancho y guardar aqui como cap01_demo.png.

2) cap02_taller.png — evidencia de avance de un estudiante
   - Con permiso del estudiante, capturar su artefacto a medio construir.
   - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
   SOLO_CLASES=7 python config/slides/build_uniajc_bd2_all.py
