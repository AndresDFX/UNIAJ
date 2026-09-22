# Guion docente — Clase 12: Pruebas de rendimiento · Preparación de presentación final

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI) · encuentro síncrono
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Definir métricas/objetivos de rendimiento realistas para CloudLite.
- Diseñar un escenario de prueba (aunque sea cualitativo/simulado).
- Ensayar el pitch de sustentación (prep PI; Parcial 3 es otro día).

## Hoy avanzamos el PI en…
**Escenario de rendimiento + ensayo 5–8 min de sustentación**

**Entregable concreto:** Sección Rendimiento + guion de pitch + paquete casi-final

**Herramienta:** Google Docs · draw.io · (opcional) lab contenedor

## Fundamento teórico para el docente
## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 7] Latencia, throughput y concurrencia: la identidad que las une** — 6 vinetas.
  - La tercera magnitud es la concurrencia, cuantas peticiones estan en vuelo al mismo tiempo, y las tres se relacionan por una identidad que el docente puede escribir en el tablero: concurrencia igual a RPS por latencia.

**[Slide 8] Por que el promedio miente y el percentil no (1/2)** — 5 vinetas.

**[Slide 9] Por que el promedio miente y el percentil no (2/2)** — 4 vinetas.

**[Slide 10] Los umbrales de percepcion, y por que son convenciones (1/2)** — 5 vinetas.
  - Los umbrales que el docente debe poder citar son convenciones de percepcion humana bien establecidas, no leyes fisicas.

**[Slide 11] Los umbrales de percepcion, y por que son convenciones (2/2)** — 4 vinetas.

**[Slide 12] El escenario de carga: aritmetica de servilleta** — 6 vinetas.
  - La forma correcta de estimarlo es aritmetica de servilleta y el docente debe hacerla en vivo con CloudLite.

**[Slide 13] El cuello de botella: siempre hay uno (1/2)** — 5 vinetas.

**[Slide 14] El cuello de botella: siempre hay uno (2/2)** — 4 vinetas.

**[Slide 15] Los tipos de prueba, por la pregunta que responden (1/2)** — 6 vinetas.

**[Slide 16] Los tipos de prueba, por la pregunta que responden (2/2)** — 3 vinetas.

**[Slide 17] El ensayo del pitch: la segunda mitad tiene su propia teoria (1/2)** — 4 vinetas.
  - Hay que decir explicitamente que este ensayo no es la sustentacion, que es la Clase 15, ni el Parcial 3 de la Clase 14, que es evaluacion escrita: son tres cosas distintas y mezclarlas confunde al grupo.

**[Slide 18] El ensayo del pitch: la segunda mitad tiene su propia teoria (2/2)** — 3 vinetas.

**[Slide 19] Preguntas frecuentes y cierre conceptual () (1/2)** — 7 vinetas.
  - Tres preguntas llegan siempre.
  - Conviene cerrar recordando que el bottleneck identificado hoy es insumo obligatorio de la Clase 13: no se puede escribir una politica de autoescalado sensata sin saber que recurso se agota primero.

**[Slide 20] Preguntas frecuentes y cierre conceptual () (2/2)** — 7 vinetas.


## Referencias a diapositivas
Numeración real del deck `Clases/Clase 12 - Pruebas de rendimiento y preparacion final/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 12 · Pruebas de rendimiento · Preparación de presentación final
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. Rendimiento sin stress-tool de pago
5. Preparación de presentación (5–8 min)
6. Paquete de entrega
7. Latencia, throughput y concurrencia: la identidad que las une
8. Por que el promedio miente y el percentil no (1/2)
9. Por que el promedio miente y el percentil no (2/2)
10. Los umbrales de percepcion, y por que son convenciones (1/2)
11. Los umbrales de percepcion, y por que son convenciones (2/2)
12. El escenario de carga: aritmetica de servilleta
13. El cuello de botella: siempre hay uno (1/2)
14. El cuello de botella: siempre hay uno (2/2)
15. Los tipos de prueba, por la pregunta que responden (1/2)
16. Los tipos de prueba, por la pregunta que responden (2/2)
17. El ensayo del pitch: la segunda mitad tiene su propia teoria (1/2)
18. El ensayo del pitch: la segunda mitad tiene su propia teoria (2/2)
19. Preguntas frecuentes y cierre conceptual () (1/2)
20. Preguntas frecuentes y cierre conceptual () (2/2)
21. «Que sea rapido» no es un requisito
22. Herramientas de hoy
23. Del boceto a ExamLab (diagrama)
24. PI CloudLite — entregable de hoy
25. Manos a la obra (paso a paso)
26. Para continuar (PI)
27. Clase 12 · PI en movimiento

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3][Slide 24]
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Escenario de rendimiento + ensayo 5–8 min de sustentación**.
Entregable concreto: Sección Rendimiento + guion de pitch + paquete casi-final.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 4]
Cubre estos conceptos, en este orden, ~10 min cada uno, con su diapositiva:
- **Rendimiento sin stress-tool de pago** · [Slide 4]
- **Preparación de presentación (5–8 min)** · [Slide 5]
- **Paquete de entrega** · [Slide 6]

**Ninguna se salta**: cada una de esas diapositivas es el mecanismo con que se resuelve
al menos una pregunta de la actividad calificada de hoy.
El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · [Slide 23]
Herramienta del día: **Google Docs · draw.io · (opcional) lab contenedor**.
**Demo que usted debe poder repetir:** Definir un objetivo de rendimiento que si se puede verificar

1. Escriba la frase mala: «la app debe ser rapida». Pregunte al grupo como la comprobarian; deje que fallen.
2. Reescribala en vivo: «el p95 del endpoint de consulta responde en menos de 300 ms con 50 peticiones por segundo».
3. Explique el p95 con 20 numeros en el tablero: ordene y marque el que deja 95% por debajo.
4. Cierre pidiendo el bottleneck sospechado: «cual pieza creen que revienta primero, y por que esa».

Narra los clics en voz alta. Si falla la red, proyecta la solución docente de este kit (`Solucion Taller Clase 12 - CloudLite.md`), que trae el resultado esperado.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»

**Cierra la demo dentro de ExamLab** [Slide 23] — es el paso que el estudiante no adivina: pasa el boceto a codigo Mermaid con ayuda de una IA, pegalo en la pregunta de diagrama y muestralo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `sequenceDiagram`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en ExamLab** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de ExamLab.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste) · [Slide 25]
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 12/Quiz Clase 12 - Pruebas de rendimiento y preparacion final.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 27]
Di: «Queda avanzado: Escenario de rendimiento + ensayo 5–8 min de sustentación.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: describan el escenario de carga del pico real de su dominio con los 6 datos obligatorios (evento del pico, usuarios concurrentes, peticiones por segundo, mezcla de operaciones en porcentajes que sumen 100, duracion de la ventana y volumen de datos de partida), verificando que la mezcla sume exactamente 100 por ciento y que el pico corresponda a una fecha real del calendario de su dominio.
2. Paso 2: definan las 3 metricas objetivo en una tabla de 4 columnas con numero, ventana de medicion, forma de medirla y consecuencia de incumplirla, verificando que cada objetivo tenga un numero y una ventana (por ejemplo p95 por debajo de 800 ms en 5 minutos) y que ninguna diga rapido o aceptable sin cifra.
3. Paso 3: escriban en ExamLab el sequenceDiagram del camino critico con el presupuesto de latencia repartido por salto, verificando que la suma de los tramos sea menor o igual al objetivo de p95 y que la nota final muestre el margen restante en milisegundos.
4. Paso 4: ensayen el pitch de 5 a 8 minutos con cronometro y llenen la tabla de guion de 6 filas con minuto, seccion, quien habla, mensaje clave y evidencia en pantalla, verificando que la suma de los minutos quede entre 5 y 8, que ninguna seccion pase de 2:00 (y, si el docente autorizo equipo, que todos los integrantes hablen) y que cada seccion tenga una evidencia concreta que se pueda mostrar.
5. Paso 5: cierren los 5 items del backlog de la Clase 11 dejando registro de los residuales, dejen el paquete casi final ordenado en el repositorio o el Drive y suban las 6 preguntas a ExamLab (modulo Talleres) antes del domingo 23:59, verificando que el cuello de botella declarado en el analisis sea el mismo que muestra el diagrama de secuencia.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Objetivo de rendimiento sin numero, sin escenario de carga o sin bottleneck. Falta cualquiera de los tres y no es un analisis.
- Usar el promedio en vez del p95 y concluir que todo esta bien. Muestre por que el promedio esconde los casos malos.
- Ensayar el pitch leyendo las diapositivas. Cronometre y corte a los 8 minutos.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Que es el p95 y por que no usamos el promedio?
1. Cual es su bottleneck sospechado y en que se basan?
1. Diferencia entre stress test y spike test?

## Solución del taller (privada)
`Kit docente/Clase 12/Solucion Taller Clase 12 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 12/Quiz Clase 12 - Pruebas de rendimiento y preparacion final.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 12/Quiz Clase 12 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase12.png | receta: 1) Abre Google Docs · draw.io · (opcional) lab contenedor y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 12/Capturas/demo-clase12.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase12.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 12/Capturas/evidencia-clase12.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
