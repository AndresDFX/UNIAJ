Capturas de la Clase 2 — Arquitectura de Sistemas Computacionales
==============================================================

El guion embebe automaticamente cualquier PNG que exista aqui con el nombre
esperado. Mientras no exista, el .docx imprime la receta en su lugar.

Pendiente: demo-clase02.png — la herramienta del dia en uso
  1. Abrir Google Docs · draw.io (opcional).
  2. Repetir la demo: Llenar un ADR-001 delante del grupo, con sus 6 secciones rotuladas.
     1. Abra un Google Doc y escriba los 6 encabezados en orden: 1. Titulo · 2. Estado · 3. Contexto · 4. Decision · 5. Alternativas descartadas · 6. Consecuencias.
     2. Titulo: «ADR-001 Modelo de servicio dominante de CloudLite App». Estado: «Aceptado» y la fecha de hoy. Diga en voz alta: «estos dos rotulos valen 1.5 puntos y son los que se citan en la sustentacion».
     3. Contexto: «lo desarrolla una persona en doce semanas, sin presupuesto ni tarjeta, y tiene que estar en linea el dia de la sustentacion». Subraye que son RESTRICCIONES: «existen tres modelos y hay que elegir uno» no es contexto, es el apunte de clase.
     4. Decision, en una sola frase: «la aplicacion de CloudLite se despliega sobre PaaS». Tache en vivo un segundo modelo si alguien lo propone: «esta seccion vale cero si nombra dos».
     5. Alternativas descartadas, exactamente dos: IaaS, porque habria que operar el sistema operativo sin tiempo para ello; SaaS como nucleo, porque no quedaria arquitectura que disenar. Aclare aqui —y no en la decision— que identidad y correo siguen siendo SaaS satelite.
     6. Consecuencias: escriba UN eje (operacion) con su + y su -, y deje los otros dos al grupo. Diga: «un ADR de una pagina que se entiende vale mas que 5 paginas que nadie lee».
  3. Capturar solo la ventana util, no el escritorio completo.
  4. Recortar a ~1200 px de ancho.
  5. Guardar aqui como demo-clase02.png.

Pendiente: evidencia del entregable (diagrama / YAML / lab)
  - Con permiso del estudiante, capturar su artefacto de hoy.
  - Recortar nombre y correo antes de guardar. No se proyecta en clase.

Despues de agregar una imagen, regenerar el guion:
  SOLO_CLASES=2 python config/slides/build_uniajc_arq_clases_batch.py
