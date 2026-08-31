Capturas de la Clase 8 — Bases de Datos II
==============================================

El guion embebe automaticamente cualquier PNG que exista en esta carpeta con
el nombre esperado. Mientras no exista, el .docx imprime la receta en su lugar.

1) cap01_demo.png — salida de la demo del docente
   - Abrir ExamLab (PostgreSQL/PGlite) y repetir la demo: CALL sp_facturar(4, ARRAY[1,6,5], ARRAY[1,2,3]) que factura 27.400, y CALL sp_facturar(4, ARRAY[3,2], ARRAY[2,10]) que falla en la segunda linea: el stock del insumo 3 vuelve a 40 sin ROLLBACK escrito.
   - Capturar solo la ventana con el resultado (no el escritorio completo).
   - Recortar a ~1200 px de ancho y guardar aqui como cap01_demo.png.

2) cap02_taller.png — evidencia de avance de un estudiante
   - Con permiso del estudiante, capturar su artefacto a medio construir.
   - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
   SOLO_CLASES=8 python config/slides/build_uniajc_bd2_all.py
