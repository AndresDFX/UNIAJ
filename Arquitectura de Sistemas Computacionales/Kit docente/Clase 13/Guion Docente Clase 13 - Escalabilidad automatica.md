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

**Herramienta:** Navegador · editores de texto y de diagramas del curso

## Fundamento teórico para el docente
## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 6] Clase autonoma: escalabilidad no es rendimiento** — 2 vinetas.
  - Un sistema puede ser rapido y no escalar, y puede escalar y ser lento.
  - Por eso el orden del temario no es casual: primero se mide y se identifica el cuello de botella, y solo despues se decide como agregar capacidad.
  - (No se proyecta) Esta clase es autonoma por festivo: el estudiante trabaja solo y este fundamento se publica como material de lectura, asi que esta escrito para explicar el tema completo sin apoyo de un encuentro sincronico.
  - (No se proyecta) El rendimiento, tema de la Clase 12, pregunta cuanto tarda una peticion con la carga actual.

**[Slide 7] Escalar vertical y horizontalmente: las dos formas de agregar capacidad** — 5 vinetas.
  - Ademas una sola maquina grande sigue siendo un unico punto de falla.
  - No tiene techo cercano, mejora la disponibilidad porque si una instancia muere las otras siguen atendiendo, y permite crecer en pasos pequenos y baratos.
  - (No se proyecta) Hay dos formas de agregar capacidad y el estudiante debe poder definirlas sin dudar.
  - (No se proyecta) Escalar horizontalmente, o hacia afuera, es agregar MAS instancias iguales trabajando en paralelo, con el balanceador de carga de la Clase 7 repartiendo peticiones entre ellas.

**[Slide 8] Ausencia de estado: donde mas estudiantes fallan** — 4 vinetas.
  - Un servicio sin estado no guarda en la memoria de su propio proceso ninguna informacion que necesite en la siguiente peticion; todo lo que deba persistir vive en un almacen compartido, sea la base de datos, una cache comun o el token que trae el cliente.
  - (No se proyecta) La solucion parcial que casi todos proponen es la sesion pegajosa, que amarra al usuario a una instancia, y hay que decir por que es un parche: si esa instancia se cae la sesion se pierde igual, y el balanceo se vuelve desigual.
  - (No se proyecta) Lo mismo aplica a los archivos subidos de CloudLite: si se escriben en el disco local del contenedor, la mitad de las descargas fallara porque el archivo esta en la otra instancia, y por eso van a almacenamiento de objetos, que fue la decision de la Clase 7.

**[Slide 9] Las cinco piezas del autoescalado (1/2)** — 4 vinetas.
  - Cada numero se justifica.
  - (No se proyecta) Y el maximo es la pieza mas olvidada y la mas importante: es el techo de costo decidido en la Clase 10, y sin el, un error de programacion o un ataque puede escalar la factura sin limite; hay casos documentados de facturas de miles de dolares generadas en horas por autoescalado sin tope.

**[Slide 10] Las cinco piezas del autoescalado (2/2)** — 5 vinetas.

**[Slide 11] El limite fisico: la instancia nueva no aparece al instante** — 5 vinetas.
  - (No se proyecta) Sume el periodo de evaluacion y el sistema reacciona entre 5 y 10 minutos despues de que empezo el problema, asi que un pico subito del tipo que la prueba de spike de la Clase 12 simula ocurre y termina antes de que llegue la ayuda.
  - (No se proyecta) Aqui reaparece la Clase 3: una imagen slim arranca mas rapido que una de un gigabyte, asi que adelgazar la imagen no es solo ahorro de costo, es tiempo de reaccion.

**[Slide 12] Elegir la metrica: la decision mas fina del tema** — 4 vinetas.
  - (No se proyecta) Metricas mejores para ese caso son las peticiones por segundo por instancia, que se deriva del calculo hecho en la Clase 12, la latencia p95 del propio servicio, o la longitud de la cola pendiente.
  - (No se proyecta) Regla de bolsillo: la metrica correcta es la que mide el recurso que se agota primero, es decir el cuello de botella identificado en la clase anterior.
  - (No se proyecta) De ahi que el entregable de hoy no se pueda hacer bien si el de la Clase 12 quedo vacio.

**[Slide 13] Lo que NO escala (1/2)** — 4 vinetas.
  - Declarar lo que NO escala separa un diseno serio de una lista de deseos.
  - Multiplicar la capa sin verificar el limite del recurso compartido no mejora el sistema, lo rompe.
  - (No se proyecta) Tambien conviene enumerar otras piezas que no escalan por replicacion: los limites de terceros, como un proveedor de correo que acepta 100 envios por minuto y rechaza el exceso, de modo que diez workers no envian diez veces mas rapido sino que generan diez veces mas errores; los sistemas de archivos compartidos; y las tareas programadas de tipo singleton, que si corren en seis instancias hacen el mismo trabajo seis veces y pueden duplicar cobros o correos.

**[Slide 14] Lo que NO escala (2/2)** — 3 vinetas.

**[Slide 15] Preguntas frecuentes y cierre conceptual (1/2)** — 3 vinetas.

**[Slide 16] Preguntas frecuentes y cierre conceptual (2/2)** — 3 vinetas.

**[Slide 17] La regla de autoescalado, escrita como configuracion** — 13 vinetas.


## Referencias a diapositivas
Numeración real del deck `Clases/Clase 13 - Escalabilidad automatica/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 13 · Escalabilidad automática
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. Escala para CloudLite
5. Límites y costos
6. Clase autonoma: escalabilidad no es rendimiento
7. Escalar vertical y horizontalmente: las dos formas de agregar capacidad
8. Ausencia de estado: donde mas estudiantes fallan
9. Las cinco piezas del autoescalado (1/2)
10. Las cinco piezas del autoescalado (2/2)
11. El limite fisico: la instancia nueva no aparece al instante
12. Elegir la metrica: la decision mas fina del tema
13. Lo que NO escala (1/2)
14. Lo que NO escala (2/2)
15. Preguntas frecuentes y cierre conceptual (1/2)
16. Preguntas frecuentes y cierre conceptual (2/2)
17. La regla de autoescalado, escrita como configuracion
18. Politica de autoescalado (tabla, no prosa)
19. Del boceto al código Mermaid
20. Clase 13 · cierre conceptual

## Plan de clase minuto a minuto (120 min)

### Modalidad autónoma (festivo)
Esta clase cae en festivo: no hay encuentro síncrono obligatorio. El estudiante trabaja solo,
con `Presentacion.pptx` + el taller de la carpeta `Clases/`. Por eso el material publicado
tiene que ser **autosuficiente**: lo que no quede escrito, nadie lo va a explicar en vivo.

### Qué publicar (antes del día de la clase)
1. En la plataforma del curso: las diapositivas, el taller y el recordatorio del hito del PI.
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
- **105–120** Empaquetar la evidencia y subirla a la plataforma del curso.

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
3. Paso 3: escriba en la plataforma del curso el diagrama Mermaid de la maquina de decision del autoescalado con el nodo de observacion, los dos rombos de decision, las acciones de subida y bajada, el enfriamiento y el nodo de lo que no escala, verificando al renderizar que el ciclo se cierre sobre el nodo de observacion y que los umbrales del diagrama sean los mismos numeros de la tabla.
4. Paso 4: escriba los 3 componentes que NO escalan con su justificacion tecnica y su plan alterno, y la tabla de impacto en costos que enlaza con la Clase 10, verificando que cada plan alterno sea ejecutable sin cloud de pago y que el impacto de costo use los mismos niveles bajo, medio o alto de la seccion de costos.
5. Paso 5: integre la politica en la seccion Escalabilidad del informe, anote la marca de replicas en el diagrama de despliegue si aplica y suba las 5 preguntas a la plataforma del curso (modulo Talleres) antes del domingo 23:59, verificando que la politica no prometa nada que la arquitectura dibujada no pueda cumplir.

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
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase13.png | receta: 1) Abre Navegador · editores de texto y de diagramas del curso y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 13/Capturas/demo-clase13.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase13.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 13/Capturas/evidencia-clase13.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: la plataforma del curso (la plataforma del curso). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
