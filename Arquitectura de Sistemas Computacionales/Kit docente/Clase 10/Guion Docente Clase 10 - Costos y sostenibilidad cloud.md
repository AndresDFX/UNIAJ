# Guion docente — Clase 10: Costos y sostenibilidad cloud

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Actividad autónoma (festivo, sin encuentro síncrono)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Identificar drivers de costo (cómputo, datos, transferencia, idle).
- Proponer 3 apalancamientos de ahorro sin romper el diseño.
- Redactar sostenibilidad (apagado de labs, imágenes ligeras, sobredimensionamiento).

## Hoy avanzamos el PI en…
**Estimación cualitativa de costos + notas de sostenibilidad**

**Entregable concreto:** Sección Costos/Sostenibilidad del informe (bajo/medio + drivers)

**Herramienta:** Navegador · editor de texto del curso

## Fundamento teórico para el docente
## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 6] Clase autonoma: de gasto de capital a gasto operativo medido** — 3 vinetas.
  - Cuando cada recurso tiene precio unitario, casi cualquier decision de diseno se convierte en una cifra mensual y el arquitecto pasa a ser corresponsable del gasto.
  - Esa es la razon por la que este tema vive en un curso de arquitectura y no en uno de administracion.
  - (No se proyecta) Esta clase es autonoma por festivo: no hay encuentro sincronico y este fundamento se publica tal cual como material de lectura, asi que debe sostener por si solo la comprension del tema.
  - (No se proyecta) Conviene empezar por la economia, porque sin ella el tema suena a contabilidad.

**[Slide 7] CloudLite no tiene factura real, y por que igual se estima (1/2)** — 3 vinetas.
  - Eso no impide el analisis de costo, solo cambia la escala de medida.
  - (No se proyecta) Un componente al que el estudiante no le sabe poner driver es un componente que todavia no entiende.

**[Slide 8] CloudLite no tiene factura real, y por que igual se estima (2/2)** — 3 vinetas.

**[Slide 9] Ordenes de magnitud de costo** — 5 vinetas.
  - Una base de datos gestionada cuesta entre dos y tres veces la maquina desnuda equivalente, porque incluye respaldos, parches y conmutacion por falla.
  - Una funcion serverless suele traer free tier de alrededor de un millon de invocaciones mensuales, asi que un componente poco usado cuesta cero de verdad.
  - (No se proyecta) El docente debe poder citar ordenes de magnitud, y conviene decir en voz alta que son convenciones aproximadas de precios de lista y no reglas duras: las cifras cambian por proveedor, region y ano, pero las proporciones se mantienen estables.

**[Slide 10] Primer ejemplo: la tabla de costos, componente por componente (1/2)** — 5 vinetas.
  - El contenedor de la API queda en Medio, con driver instancias por horas encendidas.
  - (No se proyecta) Y hay un componente que sorprende, el monitoreo de la Clase 8: un sistema que registra cada peticion con detalle puede generar mas gigabytes de logs que de datos de negocio, y la ingesta de logs se cobra por gigabyte; existen casos reales de equipos cuya observabilidad costaba mas que la aplicacion observada.

**[Slide 11] Primer ejemplo: la tabla de costos, componente por componente (2/2)** — 3 vinetas.

**[Slide 12] Segundo ejemplo: por que el driver importa mas que el nivel** — 5 vinetas.
  - El segundo ejemplo muestra por que el driver importa mas que el nivel.
  - Esto tambien desarma la intuicion mas comun del estudiante, que si nadie usa el sistema el sistema no cuesta.
  - (No se proyecta) La conclusion es contraintuitiva y por eso vale en clase: el driver del componente "almacenamiento de archivos" no es el almacenamiento, es el trafico, y la mitigacion no es contable sino arquitectonica, poner una cache o una red de distribucion de contenido delante para que el mismo archivo no salga del origen veinte veces.

**[Slide 13] Right-sizing: tres acciones ancladas en observacion (1/2)** — 4 vinetas.
  - De ahi salen tres acciones de right-sizing.
  - (No se proyecta) Right-sizing es ajustar la capacidad aprovisionada a la demanda observada, y la palabra clave es observada: sin medicion es adivinanza, y la medicion viene de las senales doradas de la Clase 8, en particular la saturacion.
  - (No se proyecta) La tercera es adelgazar el artefacto, que amarra con la Clase 3: una imagen basada en python:3.12 pesa del orden de 1 GB, la variante slim unos 150 MB y una construida sobre alpine puede bajar a decenas de megabytes; eso es menos registro, menos transferencia en cada despliegue y menos tiempo de arranque, dato que reaparece en la Clase 13.

**[Slide 14] Right-sizing: tres acciones ancladas en observacion (2/2)** — 3 vinetas.

**[Slide 15] Sostenibilidad tecnica antes que ambiental (1/2)** — 4 vinetas.
  - Por eso las mismas tres acciones sirven a la vez para la factura y para la huella.
  - (No se proyecta) La sostenibilidad en este curso es tecnica antes que ambiental, y conviene decirlo asi para no caer en discurso vacio.
  - (No se proyecta) Y hay una tercera cara que el estudiante ignora: el costo humano de mantener el diseno.

**[Slide 16] Sostenibilidad tecnica antes que ambiental (2/2)** — 3 vinetas.

**[Slide 17] Preguntas frecuentes y cierre conceptual (1/2)** — 3 vinetas.
  - Tres preguntas aparecen siempre.

**[Slide 18] Preguntas frecuentes y cierre conceptual (2/2)** — 3 vinetas.


## Referencias a diapositivas
Numeración real del deck `Clases/Clase 10 - Costos y sostenibilidad cloud/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 10 · Costos y sostenibilidad cloud
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. Costos sin factura real
5. Sostenibilidad
6. Clase autonoma: de gasto de capital a gasto operativo medido
7. CloudLite no tiene factura real, y por que igual se estima (1/2)
8. CloudLite no tiene factura real, y por que igual se estima (2/2)
9. Ordenes de magnitud de costo
10. Primer ejemplo: la tabla de costos, componente por componente (1/2)
11. Primer ejemplo: la tabla de costos, componente por componente (2/2)
12. Segundo ejemplo: por que el driver importa mas que el nivel
13. Right-sizing: tres acciones ancladas en observacion (1/2)
14. Right-sizing: tres acciones ancladas en observacion (2/2)
15. Sostenibilidad tecnica antes que ambiental (1/2)
16. Sostenibilidad tecnica antes que ambiental (2/2)
17. Preguntas frecuentes y cierre conceptual (1/2)
18. Preguntas frecuentes y cierre conceptual (2/2)
19. Clase 10 · cierre conceptual

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
4. Mensaje sugerido: «Clase 10 autónoma (festivo). Hoy avanzamos el PI en: Estimación cualitativa de costos + notas de sostenibilidad.
   Entregable: Sección Costos/Sostenibilidad del informe (bajo/medio + drivers). Fecha límite: domingo 23:59. Dudas por foro/correo institucional.»

### Cómo debería repartir su tiempo el estudiante (120 min equivalentes)
- **0–15** Leer el encuadre y el objetivo del día; ubicar en qué quedó su CloudLite.
- **15–45** Leer la teoría (lectura guía) y tomar notas directamente en el informe del PI.
- **45–60** Revisar la salida esperada del ejercicio resuelto.
- **60–105** Desarrollar el taller sobre su propio CloudLite.
- **105–120** Empaquetar la evidencia y subirla a la plataforma del curso.

### La demo, en versión asíncrona
**Demo que usted debe poder repetir:** Tabla de costo cualitativo en 5 minutos

1. Dibuje 3 columnas: Componente | Costo (Bajo/Medio/Alto) | Driver del costo.
2. Llene 3 filas de CloudLite: base de datos gestionada (Alto, computo+almacenamiento constante 24/7), API en contenedor (Medio, numero de instancias), object storage de imagenes (Bajo, volumen de datos).
3. Pregunte cual bajaria primero si el presupuesto se corta a la mitad, y exija que justifiquen con el driver, no con intuicion.

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
1. Paso 1: construya en la pregunta 11 la tabla de costos con una fila por cada componente de su despliegue y las columnas componente, driver, nivel B/M/A y apalancamiento; verifique que cada driver sea una variable contable (horas encendidas, GB de salida, GB almacenados, minutos de CI) y no «el uso».
2. Paso 2: fuerce al menos un Alto y un Bajo con su justificacion. Marcar todo como Medio para no decidir es lo que la pregunta busca descartar, y ese criterio vale cero si todas las filas quedan iguales.
3. Paso 3: escriba en la pregunta 12 tres acciones de sostenibilidad, cada una con el artefacto donde se comprueba y como se comprueba; aplique la prueba de que otra persona pueda decir en seis meses, mirando el repositorio, si la accion se aplico.
4. Paso 4: ate al menos una de las tres acciones a un driver de costo de la pregunta 11 y suba la actividad completa del Corte 2 a la plataforma del curso antes del domingo 23:59. Es una clase autonoma: no hay encuentro sincrono, y las dudas van por el foro.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Pedir precios exactos de un proveedor. No es el objetivo: el analisis es cualitativo y por driver.
- Marcar todo como costo «Medio» para no pensar. Fuerce al menos un Alto y un Bajo con justificacion.
- Olvidar el trafico de red saliente, que es el driver que mas sorprende en facturas reales.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Cual es el componente mas caro de su CloudLite y cual es su driver?
1. Que es right-sizing en una frase?
1. Como se conecta el autoescalado con el costo?

## Solución del taller (privada)
`Kit docente/Clase 10/Solucion Taller Clase 10 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 10/Quiz Clase 10 - Costos y sostenibilidad cloud.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 10/Quiz Clase 10 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase10.png | receta: 1) Abre Navegador · editor de texto del curso y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 10/Capturas/demo-clase10.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase10.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 10/Capturas/evidencia-clase10.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: la plataforma del curso (la plataforma del curso). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
