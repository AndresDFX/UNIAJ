Capturas de la Clase 4 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Pendiente: demo-clase04.png — la herramienta del dia en uso
  1. Abrir draw.io o Excalidraw para bocetar · Mermaid dentro de ExamLab para entregar.
  2. Repetir la demo: Convertir el Context de la Clase 1 en Containers, y dejarlo renderizado en ExamLab.
     1. Abra el diagrama C4 Context de la demo de Clase 1 y haga zoom a la caja «CloudLite App». Diga: «hoy no dibujamos otro sistema, abrimos este».
     2. Reemplace esa caja por 3 cajas internas: «App web», «API de turnos» y «Base de turnos». Escriba en cada una sus TRES datos: nombre, tecnologia y responsabilidad en una frase.
     3. Senale la base de datos y diga: «esta no es un Container mas, es un ALMACEN; en el codigo va como ContainerDb y son 2 puntos». Deje el cliente y el correo FUERA del recuadro del sistema.
     4. Rotule CADA flecha con protocolo Y formato: «HTTPS/JSON», «TCP/SQL». Borre a proposito una etiqueta y pregunte que se pierde: sin ella nadie puede decir por donde se rompe.
     5. Proponga una cuarta caja, el worker de avisos, y pida la razon de negocio. Si nadie la da, borrela en vivo: «eso es microservicios teatro». Si alguien la da (el correo tarda y puede fallar), quedese con ella y anote la razon al lado.
     6. Verifique nombre por nombre contra el C4 Context de la Clase 1: si alli decia «Pasarela de pagos», aqui no puede decir «Pagos». Son 2 puntos de la pregunta 13.
     7. Cierre en ExamLab: pegue el codigo Mermaid de la diapositiva del molde, cambie los nombres por los del ejemplo del tablero y proyecte el resultado RENDERIZADO. Diga: «si no renderiza, no hay diagrama; se revisa antes de enviar».
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase04.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=4 python config/slides/build_uniajc_arq_clases_batch.py
