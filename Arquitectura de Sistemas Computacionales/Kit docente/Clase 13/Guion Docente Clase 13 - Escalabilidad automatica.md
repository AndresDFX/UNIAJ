# Guion docente — Clase 13: Escalabilidad automática

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Actividad autónoma (festivo, sin encuentro síncrono)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Distinguir escala vertical vs horizontal y cuándo aplicarlas.
- Definir triggers cualitativos (CPU, cola, RPS) sin cloud de pago.
- Actualizar el informe PI con la política de escala.

## Hoy avanzamos el PI en…
**Documentar política de autoescalado conceptual de CloudLite**

**Entregable concreto:** Sección Escalabilidad: triggers, límites, qué escala y qué no

**Herramienta:** Google Docs · draw.io (opcional nota en Deployment)

## Fundamento teórico para el docente
## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 6] Clase autonoma: escalabilidad no es rendimiento** — 4 vinetas.
  - Un sistema puede ser rapido y no escalar, y puede escalar y ser lento.
  - Por eso el orden del temario no es casual: primero se mide y se identifica el cuello de botella, y solo despues se decide como agregar capacidad.

**[Slide 7] Escalar vertical y horizontalmente: las dos formas de agregar capacidad (1/2)** — 4 vinetas.
  - Ademas una sola maquina grande sigue siendo un unico punto de falla.
  - No tiene techo cercano, mejora la disponibilidad porque si una instancia muere las otras siguen atendiendo, y permite crecer en pasos pequenos y baratos.

**[Slide 8] Escalar vertical y horizontalmente: las dos formas de agregar capacidad (2/2)** — 3 vinetas.

**[Slide 9] Ausencia de estado: donde mas estudiantes fallan (1/2)** — 4 vinetas.
  - Un servicio sin estado no guarda en la memoria de su propio proceso ninguna informacion que necesite en la siguiente peticion; todo lo que deba persistir vive en un almacen compartido, sea la base de datos, una cache comun o el token que trae el cliente.

**[Slide 10] Ausencia de estado: donde mas estudiantes fallan (2/2)** — 2 vinetas.

**[Slide 11] Las cinco piezas que el entregable debe nombrar (1/2)** — 6 vinetas.
  - Cada numero se justifica.

**[Slide 12] Las cinco piezas que el entregable debe nombrar (2/2)** — 5 vinetas.

**[Slide 13] El limite fisico: la instancia nueva no aparece al instante (1/2)** — 4 vinetas.

**[Slide 14] El limite fisico: la instancia nueva no aparece al instante (2/2)** — 3 vinetas.

**[Slide 15] Elegir la metrica: la decision mas fina del tema (1/2)** — 3 vinetas.
  - Regla de bolsillo: la metrica correcta es la que mide el recurso que se agota primero, es decir el cuello de botella identificado en la clase anterior.
  - De ahi que el entregable de hoy no se pueda hacer bien si el de la Clase 12 quedo vacio.

**[Slide 16] Elegir la metrica: la decision mas fina del tema (2/2)** — 2 vinetas.

**[Slide 17] Lo que NO escala: la mitad del entregable (1/2)** — 5 vinetas.
  - Lo que NO escala es la mitad del entregable y separa una sustentacion seria de una lista de deseos.
  - Multiplicar la capa sin verificar el limite del recurso compartido no mejora el sistema, lo rompe.

**[Slide 18] Lo que NO escala: la mitad del entregable (2/2)** — 5 vinetas.

**[Slide 19] Preguntas frecuentes y cierre conceptual () (1/4)** — 4 vinetas.
  - Tres preguntas aparecen sin falta en una clase autonoma como esta y conviene responderlas por escrito en el foro.

**[Slide 20] Preguntas frecuentes y cierre conceptual () (2/4)** — 4 vinetas.

**[Slide 21] Preguntas frecuentes y cierre conceptual () (3/4)** — 5 vinetas.

**[Slide 22] Preguntas frecuentes y cierre conceptual () (4/4)** — 4 vinetas.


## Referencias a diapositivas
Numeración real del deck `Clases/Clase 13 - Escalabilidad automatica/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 13 · Escalabilidad automática
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. Escala para CloudLite
5. Límites y costos
6. Clase autonoma: escalabilidad no es rendimiento
7. Escalar vertical y horizontalmente: las dos formas de agregar capacidad (1/2)
8. Escalar vertical y horizontalmente: las dos formas de agregar capacidad (2/2)
9. Ausencia de estado: donde mas estudiantes fallan (1/2)
10. Ausencia de estado: donde mas estudiantes fallan (2/2)
11. Las cinco piezas que el entregable debe nombrar (1/2)
12. Las cinco piezas que el entregable debe nombrar (2/2)
13. El limite fisico: la instancia nueva no aparece al instante (1/2)
14. El limite fisico: la instancia nueva no aparece al instante (2/2)
15. Elegir la metrica: la decision mas fina del tema (1/2)
16. Elegir la metrica: la decision mas fina del tema (2/2)
17. Lo que NO escala: la mitad del entregable (1/2)
18. Lo que NO escala: la mitad del entregable (2/2)
19. Preguntas frecuentes y cierre conceptual () (1/4)
20. Preguntas frecuentes y cierre conceptual () (2/4)
21. Preguntas frecuentes y cierre conceptual () (3/4)
22. Preguntas frecuentes y cierre conceptual () (4/4)
23. Politica de autoescalado (tabla, no prosa)
24. Herramientas de hoy
25. Del boceto a ExamLab (diagrama)
26. PI CloudLite — entregable de hoy
27. Manos a la obra (paso a paso)
28. Para continuar (PI)
29. Clase 13 · PI en movimiento

## Plan de clase minuto a minuto (120 min)

### Modalidad autónoma (festivo)
Esta clase cae en festivo: no hay encuentro síncrono obligatorio. El estudiante trabaja solo,
con `Presentacion.pptx` + el taller de la carpeta `Clases/`. Por eso el material publicado
tiene que ser **autosuficiente**: lo que no quede escrito, nadie lo va a explicar en vivo.

### Qué publicar (antes del día de la clase)
1. En ExamLab: las diapositivas, el taller y el recordatorio del hito del PI.
2. La sección «Fundamento teórico para el docente» de este guion, adaptada como **lectura guía**
   del estudiante — es el reemplazo de la explicación en vivo, no un anexo opcional.
3. La **salida esperada** del ejercicio (ver la demo de abajo), para que el estudiante autónomo
   pueda comparar y saber si le quedó bien sin preguntarte.
4. Mensaje sugerido: «Clase 13 autónoma (festivo). Hoy avanzamos el PI en: Documentar política de autoescalado conceptual de CloudLite.
   Entregable: Sección Escalabilidad: triggers, límites, qué escala y qué no. Fecha límite: domingo 23:59. Dudas por foro/correo institucional.»

### Cómo debería repartir su tiempo el estudiante (120 min equivalentes)
- **0–15** Leer el encuadre y el objetivo del día; ubicar en qué quedó su CloudLite.
- **15–45** Leer la teoría (lectura guía) y tomar notas directamente en el informe del PI.
- **45–60** Revisar la salida esperada del ejercicio resuelto.
- **60–105** Desarrollar el taller sobre su propio CloudLite.
- **105–120** Empaquetar la evidencia y subirla a ExamLab.

### La demo, en versión asíncrona
**Demo que usted debe poder repetir:** Vertical vs horizontal, y lo que NO escala

1. Dibuje una caja «API» y agrandela: eso es vertical (mas CPU/RAM a la misma maquina, con techo fisico).
2. Borre y dibuje 3 cajas «API» iguales con un balanceador arriba: eso es horizontal.
3. Agregue la base de datos abajo, conectada a las 3, y encierrela en rojo: «esta no se multiplica igual; aqui esta el limite real».
4. Escriba el trigger y el limite: «CPU > 70% por 5 min -> +1 instancia, maximo 4» y amarre con el costo de la Clase 10.

Publica esto como pasos escritos o como un video corto (3–5 min) grabado con estos mismos pasos.
Sin uno de los dos, el estudiante autónomo no tiene con qué comparar su resultado.


### Seguimiento (lo que sí es tu trabajo esa semana)
1. Revisa las entregas del domingo 23:59 con la lista de errores frecuentes de abajo:
   en modalidad autónoma esos errores aparecen más, porque nadie los corrigió en el momento.
2. Deja feedback breve orientado a la rúbrica del PI, nombrando el error y la corrección.
3. En la siguiente clase regular, dedica los primeros 10 min a los 2 errores más repetidos.
   Es el sustituto de la retroalimentación en vivo que esta clase no tuvo.

### Si ofreces office hours voluntario (opcional, 20–30 min)
Resuelve bloqueos concretos de diagrama/ADR/lab. Usa las preguntas de comprobación de abajo
para detectar quién entendió y quién solo copió la plantilla. No adelantes contenido de Parcial.


## Actividad / taller (detalle)
1. Paso 1: tome los 5 componentes de su C4Deployment de la Clase 7 y clasifique cada uno como escala horizontal, escala vertical o no escala, verificando que al menos uno quede en no escala con justificacion tecnica, porque una politica donde todo escala no es una politica; el resultado abre la seccion Escalabilidad del informe.
2. Paso 2: complete la tabla de politica de escalado con 6 columnas y 5 filas (componente, tipo de escala, disparador de subida, disparador de bajada, minimo y maximo, tiempo de enfriamiento), verificando que cada disparador tenga metrica, umbral numerico y ventana de tiempo, y que ningun maximo quede en infinito o sin definir.
3. Paso 3: escriba en ExamLab el diagrama Mermaid de la maquina de decision del autoescalado con el nodo de observacion, los dos rombos de decision, las acciones de subida y bajada, el enfriamiento y el nodo de lo que no escala, verificando al renderizar que el ciclo se cierre sobre el nodo de observacion y que los umbrales del diagrama sean los mismos numeros de la tabla.
4. Paso 4: escriba los 3 componentes que NO escalan con su justificacion tecnica y su plan alterno, y la tabla de impacto en costos que enlaza con la Clase 10, verificando que cada plan alterno sea ejecutable sin cloud de pago y que el impacto de costo use los mismos niveles bajo, medio o alto de la seccion de costos.
5. Paso 5: integre la politica en la seccion Escalabilidad del informe, anote la marca de replicas en el diagrama de despliegue si aplica y suba las 5 preguntas a ExamLab (modulo Talleres) antes del domingo 23:59, verificando que la politica no prometa nada que la arquitectura dibujada no pueda cumplir.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Prometer autoescalado infinito sin limite maximo ni control de costo (Clase 10).
- Escalar horizontalmente un servicio que guarda la sesion en memoria local: al repartir la carga, el usuario pierde su sesion.
- No documentar QUE NO escala. La base de datos relacional es casi siempre la respuesta y hay que decirlo.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Vertical u horizontal: cual eligieron y por que?
1. Cual es su trigger y cual su limite maximo?
1. Que pieza de su sistema NO escala, y que harian al respecto?

## Solución del taller (privada)
`Kit docente/Clase 13/Solucion Taller Clase 13 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 13/Quiz Clase 13 - Escalabilidad automatica.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 13/Quiz Clase 13 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase13.png | receta: 1) Abre Google Docs · draw.io (opcional nota en Deployment) y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 13/Capturas/demo-clase13.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase13.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 13/Capturas/evidencia-clase13.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
