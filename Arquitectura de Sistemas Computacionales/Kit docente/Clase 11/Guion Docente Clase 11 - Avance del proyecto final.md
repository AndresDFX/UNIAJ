# Guion docente — Clase 11: Avance del proyecto final

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI) · encuentro síncrono
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Consolidar evidencias PI en un paquete revisable.
- Detectar huecos (nombres inconsistentes, servicios de más, sin seguridad).
- Salir con backlog claro hacia Clase 12/15.

## Hoy avanzamos el PI en…
**Integrar diagramas v1 + checklist de avance PI**

**Entregable concreto:** Paquete v1: Context + Containers + Deployment + Dockerfile + Actions + informe 60%+

**Herramienta:** Navegador · editores de diagramas y de texto del curso

## Fundamento teórico para el docente
## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 7] La teoria propia del dia: que es una revision de arquitectura (1/2)** — 3 vinetas.
  - Hoy el docente no dicta, audita, y el estudiante no aprende un concepto, demuestra que los que ya tiene forman un sistema.

**[Slide 8] La teoria propia del dia: que es una revision de arquitectura (2/2)** — 2 vinetas.

**[Slide 9] El insumo: las seis piezas del paquete CloudLite v1** — 4 vinetas.
  - Y se audita con preguntas mecanicas que cualquier docente puede hacer sin ser experto en el dominio del proyecto, lo que hace esta tecnica ensenable.

**[Slide 10] Las cinco preguntas de coherencia, en orden (1/2)** — 5 vinetas.

**[Slide 11] Las cinco preguntas de coherencia, en orden (2/2)** — 4 vinetas.

**[Slide 12] Scope creep y arquitectura de papel: las dos patologias con nombre propio (1/2)** — 4 vinetas.
  - Hay dos patologias con nombre propio que arruinan las sustentaciones.
  - La respuesta correcta no es prohibir ideas sino congelar el alcance y abrir una lista de aparcamiento, un anexo donde las capacidades extra quedan escritas como "fuera de alcance v1, candidatas a v2": preserva la idea, protege el cronograma y es lo que hace un equipo profesional al cerrar un release.

**[Slide 13] Scope creep y arquitectura de papel: las dos patologias con nombre propio (2/2)** — 4 vinetas.

**[Slide 14] Retroalimentacion accionable: observacion, evidencia, impacto y accion con fecha (1/2)** — 4 vinetas.
  - El docente debe apuntar a tres hallazgos por proyecto como maximo y marcar cual es el bloqueante, porque un estudiante que recibe once observaciones no corrige ninguna: se paraliza.
  - Conviene nombrar tambien una fortaleza concreta, no por amabilidad sino porque el estudiante necesita saber que conservar; si solo escucha fallas, en la siguiente version cambia todo, incluido lo que estaba bien.

**[Slide 15] Retroalimentacion accionable: observacion, evidencia, impacto y accion con fecha (2/2)** — 2 vinetas.

**[Slide 16] El semaforo: el umbral que decide si el proyecto va a tiempo (1/2)** — 5 vinetas.

**[Slide 17] El semaforo: el umbral que decide si el proyecto va a tiempo (2/2)** — 3 vinetas.

**[Slide 18] Preguntas frecuentes y cierre conceptual () (1/3)** — 4 vinetas.
  - Tres preguntas se repiten y el docente debe responderlas sin titubear.
  - Conviene cerrar diciendo que lo que se estabilice hoy es la base sobre la que la Clase 12 agregara el analisis de rendimiento y la Clase 13 la politica de escalado, y que un proyecto con el paquete v1 incoherente no puede hacer ninguna de las dos, porque no se puede medir ni escalar un sistema que todavia no esta definido.

**[Slide 19] Preguntas frecuentes y cierre conceptual () (2/3)** — 5 vinetas.

**[Slide 20] Preguntas frecuentes y cierre conceptual () (3/3)** — 3 vinetas.

**[Slide 21] El C4 Component: por dentro de la API** — 17 vinetas.


## Referencias a diapositivas
Numeración real del deck `Clases/Clase 11 - Avance del proyecto final/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 11 · Avance del proyecto final
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. Checklist de avance (obligatorio)
5. Errores frecuentes a corregir
6. Rúbrica (recordatorio)
7. La teoria propia del dia: que es una revision de arquitectura (1/2)
8. La teoria propia del dia: que es una revision de arquitectura (2/2)
9. El insumo: las seis piezas del paquete CloudLite v1
10. Las cinco preguntas de coherencia, en orden (1/2)
11. Las cinco preguntas de coherencia, en orden (2/2)
12. Scope creep y arquitectura de papel: las dos patologias con nombre propio (1/2)
13. Scope creep y arquitectura de papel: las dos patologias con nombre propio (2/2)
14. Retroalimentacion accionable: observacion, evidencia, impacto y accion con fecha (1/2)
15. Retroalimentacion accionable: observacion, evidencia, impacto y accion con fecha (2/2)
16. El semaforo: el umbral que decide si el proyecto va a tiempo (1/2)
17. El semaforo: el umbral que decide si el proyecto va a tiempo (2/2)
18. Preguntas frecuentes y cierre conceptual () (1/3)
19. Preguntas frecuentes y cierre conceptual () (2/3)
20. Preguntas frecuentes y cierre conceptual () (3/3)
21. El C4 Component: por dentro de la API
22. Herramientas de hoy
23. Del boceto a la plataforma del curso (diagrama)
24. PI CloudLite — entregable de hoy
25. Manos a la obra (paso a paso)
26. Para continuar (PI)
27. Clase 11 · PI en movimiento

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3][Slide 24]
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Integrar diagramas v1 + checklist de avance PI**.
Entregable concreto: Paquete v1: Context + Containers + Deployment + Dockerfile + Actions + informe 60%+.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 4]
Cubre estos conceptos, en este orden, ~10 min cada uno, con su diapositiva:
- **Checklist de avance (obligatorio)** · [Slide 4]
- **Errores frecuentes a corregir** · [Slide 5]
- **Rúbrica (recordatorio)** · [Slide 6]

**Ninguna se salta**: cada una de esas diapositivas es el mecanismo con que se resuelve
al menos una pregunta de la actividad calificada de hoy.
El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · [Slide 23]
Herramienta del día: **Navegador · editores de diagramas y de texto del curso**.
**Demo que usted debe poder repetir:** Auditar en vivo el paquete de un voluntario

1. Pida a un estudiante voluntario (o a un equipo, si autorizo equipos) que proyecte su C4 Containers y su diagrama de despliegue lado a lado.
2. Compare nombre por nombre: todo servicio del Containers debe existir en el despliegue y viceversa.
3. Senale en voz alta el primer gap concreto que encuentre y escribalo como accion con responsable y fecha.
4. Modele el tono: el hallazgo es sobre el artefacto, nunca sobre la persona.

Narra los clics en voz alta. Si falla la red, proyecta la solución docente de este kit (`Solucion Taller Clase 11 - CloudLite.md`), que trae el resultado esperado.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»

**Cierra la demo en la plataforma del curso** [Slide 23] — es el paso que el estudiante no adivina: pasa el boceto a codigo Mermaid con ayuda de una IA, pegalo en la pregunta de diagrama y muestralo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `C4Component`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en la plataforma del curso** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de la plataforma del curso.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste) · [Slide 25]
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 11/Quiz Clase 11 - Avance del proyecto final.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 27]
Di: «Queda avanzado: Integrar diagramas v1 + checklist de avance PI.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en la plataforma del curso. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: completen el checklist de 10 filas del paquete v1 marcando cada evidencia como si, no o parcial y pegando la ruta o el enlace exacto de cada una, verificando que ninguna fila marcada como si quede sin ruta verificable, porque una fila sin enlace se califica como no.
2. Paso 2: hagan la reconciliacion de nombres llenando la tabla de 5 filas que compara como se llama cada elemento en el C4Container, en el C4Deployment, en el Dockerfile o el ci.yml y en el informe, verificando que la columna de nombre canonico sea identica en las cuatro y aplicando la correccion en el artefacto que este desalineado.
3. Paso 3: escriban en la plataforma del curso el diagrama C4Component del interior de la API con 5 componentes y sus relaciones hacia la base de datos, la cola y el proveedor de identidad, verificando al renderizar que ningun componente sea un contenedor de la Clase 4 disfrazado y que el contenedor contenedor de la frontera se llame igual que en el C4Container.
4. Paso 4: escriban el backlog de 5 items priorizados hacia la Clase 12 con hueco detectado, accion, responsable y fecha, verificando que cada item se pueda cerrar en una semana y que al menos uno provenga del feedback del docente recibido hoy en la cola de revision.
5. Paso 5: empaqueten el ZIP o el repositorio con los diagramas, el Dockerfile, el ci.yml y el informe al 60 por ciento, y suban las 5 preguntas a la plataforma del curso (modulo Talleres) antes del domingo 23:59, verificando que el paquete se pueda abrir en otra maquina y que el informe enlace cada evidencia por su ruta dentro del paquete.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Traer el paquete de la Clase 1 sin actualizar y presentarlo como avance. Compare contra la version anterior.
- Conocer solo la parte que se copio de una plantilla y no el paquete completo. Pregunte al azar por cualquier seccion; si hubo equipo autorizado, pregunte a un integrante distinto del que presenta y si solo uno responde, ese es el hallazgo principal.
- Confundir este checkpoint con la sustentacion final o con el Parcial 3. Aclarelo al abrir la sesion.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Que gap concreto identificaron hoy y quien lo cierra?
1. Su diagrama de despliegue usa los mismos nombres que su C4 Containers?
1. Que evidencia de la rubrica les falta todavia?

## Solución del taller (privada)
`Kit docente/Clase 11/Solucion Taller Clase 11 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 11/Quiz Clase 11 - Avance del proyecto final.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 11/Quiz Clase 11 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase11.png | receta: 1) Abre Navegador · editores de diagramas y de texto del curso y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 11/Capturas/demo-clase11.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase11.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 11/Capturas/evidencia-clase11.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: la plataforma del curso (la plataforma del curso). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
