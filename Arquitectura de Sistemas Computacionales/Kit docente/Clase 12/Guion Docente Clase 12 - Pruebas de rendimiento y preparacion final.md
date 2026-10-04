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

**Herramienta:** Navegador · editores de diagramas y de texto del curso

## Fundamento teórico para el docente
## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] Latencia, throughput y concurrencia: la identidad que las une** — 2 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La latencia, o tiempo de respuesta, es cuanto tarda UNA peticion desde que sale del cliente hasta que llega la respuesta completa; se mide en milisegundos y es lo que siente el usuario.
  - El throughput, o caudal, es cuantas peticiones atiende el sistema por unidad de tiempo; se mide en peticiones por segundo, abreviado RPS, y es lo que importa para la capacidad.
  - No se mueven juntas: un sistema puede atender 500 RPS con latencia terrible porque todo espera en cola, y otro puede tener latencia excelente con 3 RPS porque nadie lo usa.
  - Si CloudLite atiende 5 RPS con 300 milisegundos, hay en promedio 1.5 peticiones simultaneas dentro del sistema, y ese numero decide cuantos hilos, cuantas conexiones a base de datos y cuantas instancias se necesitan.
  - La identidad que las une se llama ley de Little: concurrencia = throughput × latencia.
  - Con 5 RPS y 0.3 segundos, 5 × 0.3 = 1.5 peticiones dentro del sistema en promedio.
  - Si la latencia sube a 3 segundos con el mismo trafico, la concurrencia sube a 15, y el pool de conexiones que antes alcanzaba deja de alcanzar.
  - NOTAS:
  - Hay dos magnitudes que se confunden todo el tiempo.
  - (No se proyecta) Rendimiento es la unica parte del curso donde el estudiante puede pasar de opinar a medir, y por eso conviene empezar por el vocabulario exacto.
  - (No se proyecta) La tercera magnitud es la concurrencia, cuantas peticiones estan en vuelo al mismo tiempo, y las tres se relacionan por una identidad que el docente puede escribir en el tablero: concurrencia igual a RPS por latencia.

**[Slide 5] Por que el promedio miente y el percentil no** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El corazon del tema es entender por que el promedio miente y el percentil no.
  - Un percentil es el valor por debajo del cual cae un porcentaje dado de las observaciones ordenadas de menor a mayor: el p95 del tiempo de respuesta es el tiempo tal que el 95 por ciento de las peticiones respondieron en ese tiempo o menos, y el 5 por ciento restante tardo mas.
  - El ejemplo numerico es obligatorio porque convence de inmediato.
  - Suponga 100 peticiones a CloudLite: 95 responden en 120 milisegundos y 5 responden en 4000 porque cayeron en una consulta sin indice.
  - El promedio es 314 milisegundos, una cifra que suena aceptable y que no le paso a nadie: ninguna peticion real tardo 314 milisegundos.
  - El p50, o mediana, es 120; el p99 es 4000.
  - Reportar el promedio esconde a cinco usuarios de cada cien esperando cuatro segundos; reportar p95 y p99 los hace visibles.
  - Un objetivo sin condicion de carga no significa nada: cualquier sistema es rapido sin usuarios.
  - NOTAS:
  - Por eso la industria escribe sus objetivos en percentiles, y por eso un objetivo bien escrito tiene la forma "p95 del endpoint de listado menor a 300 milisegundos con 5 RPS", que tiene metrica, umbral y condicion de carga.

**[Slide 6] Las metricas objetivo, escritas como se verifican** — 8 vinetas.

**[Slide 7] Los umbrales de percepcion, y por que son convenciones** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Por debajo de unos 100 milisegundos la respuesta se percibe instantanea; hasta cerca de 1 segundo el usuario mantiene el hilo aunque note la demora; pasados unos 10 segundos pierde la atencion y cambia de tarea o recarga.
  - Ninguna es regla dura: un reporte pesado puede tener un objetivo legitimo de 3 segundos y un autocompletado necesita estar bajo 100.
  - Junto al tiempo va siempre la tasa de error, el porcentaje de peticiones que fallan, porque un sistema que responde rapido devolviendo errores no cumple.
  - Aqui aparecen tres siglas: el SLI es el indicador que se mide, el SLO es el objetivo interno que el equipo se compromete a cumplir y el SLA es el compromiso contractual con penalidad.
  - NOTAS:
  - De ahi sale la convencion practica para una API interna, que ubica el objetivo de p95 entre 200 y 300 milisegundos dejando presupuesto para que el navegador y la red agreguen lo suyo; para carga de pagina completa la referencia publica de Core Web Vitals considera bueno un renderizado del contenido principal por debajo de 2.5 segundos.
  - Lo que si es regla es que el numero se escribe antes de medir y se justifica con el caso de uso, no se ajusta despues para que la medicion salga bien.
  - (No se proyecta) Los umbrales que el docente debe poder citar son convenciones de percepcion humana bien establecidas, no leyes fisicas.
  - (No se proyecta) Un SLO de 99.9 por ciento de disponibilidad, los "tres nueves", admite unos 43 minutos de caida al mes; el 99.99 baja a poco mas de 4 minutos, y esa diferencia de un decimal suele multiplicar el costo de la arquitectura, lo que amarra con la tabla de la Clase 10.

**[Slide 8] El escenario de carga: aritmetica de servilleta** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Suponga 1000 usuarios activos al dia, cada uno con unas 20 peticiones en su sesion: son 20000 peticiones diarias.
  - Si un 40 por ciento cae en una ventana de dos horas, eso es 8000 peticiones en 7200 segundos, algo mas de 1 RPS promedio en la hora pico.
  - Como el trafico real llega en rafagas, se aplica un factor de pico de 3 a 5 veces y se dimensiona para unos 5 RPS.
  - Ese numero es el que debe aparecer en el informe, y es un orden de magnitud tres mil veces menor que los "10000 RPS" que algun estudiante escribira por sonar ambicioso.
  - (No se proyecta) El segundo componente es el escenario de carga, y el estudiante casi siempre lo inventa exagerado.
  - (No se proyecta) La forma correcta de estimarlo es aritmetica de servilleta y el docente debe hacerla en vivo con CloudLite.
  - (No se proyecta) La leccion es doble: un objetivo de rendimiento sin cuenta de sobre es marketing y no ingenieria, y dimensionar para 5 RPS en vez de 10000 es justamente lo que evita el sobreaprovisionamiento que la Clase 10 senalo como desperdicio.

**[Slide 9] El cuello de botella: siempre hay uno** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El tercer componente es el bottleneck, o cuello de botella: el componente que se agota primero y limita el rendimiento de todo el sistema.
  - En CloudLite los candidatos son pocos y reconocibles.
  - El primero es el problema N mas 1 en el endpoint de listado: la API pide la lista con una consulta y luego, dentro del ciclo, hace una consulta adicional por cada registro para traer un dato relacionado
  - Con 50 registros son 51 viajes a la base de datos y el tiempo se va en latencia de red acumulada, no en CPU.
  - El segundo es el pool de conexiones: si el pool tiene 10 conexiones y llegan 40 peticiones concurrentes, 30 esperan turno y la latencia se dispara aunque la CPU de la API y la de la base de datos esten al 20 por ciento.
  - El tercero, si CloudLite envia notificaciones de forma sincronica dentro de la peticion, es el proveedor externo: el usuario espera a que un tercero responda, y la mitigacion no es mas CPU sino sacar el envio de la ruta critica hacia una cola.
  - (No se proyecta) La afirmacion fuerte, que conviene decir tal cual, es que en cualquier instante hay exactamente un cuello de botella; "todo esta lento" nunca es un diagnostico, es la ausencia de uno.
  - (No se proyecta) Se localiza con las senales doradas de la Clase 8, en particular la saturacion, mirando cual recurso esta cerca de su limite mientras los demas estan holgados.
  - (No se proyecta) Esos tres cubren la mayoria de los casos que los estudiantes van a sospechar.

**[Slide 10] El presupuesto de latencia del camino critico** — 20 vinetas.

**[Slide 11] Los tipos de prueba, por la pregunta que responden** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La prueba de estres sube la carga de forma progresiva hasta que el sistema se degrada o se rompe
  - Y responde cual es la capacidad maxima y como se comporta al fallar; el dato interesante no es el punto de quiebre sino la forma de la falla, porque degradarse respondiendo lento es aceptable y caerse por completo no.
  - La prueba de resistencia, o soak, mantiene carga moderada durante horas y responde si hay fugas de memoria o conexiones que no se liberan; con menos de una hora no se detecta nada y de 2 a 4 horas es lo tipico.
  - No se necesita ninguna herramienta de pago: en Killercoda se puede lanzar un contenedor con k6, hey o Apache Bench y golpear el stub del servicio, y si el lab no carga, el escenario se documenta en papel con la aritmetica de arriba.
  - NOTAS:
  - Los tipos de prueba se distinguen por la pregunta que responden.
  - La prueba de carga o baseline aplica la carga esperada y responde si el sistema cumple el SLO en condiciones normales.
  - Un escenario bien razonado sin ejecucion vale mas que una ejecucion sin objetivo.
  - (No se proyecta) La prueba de picos, o spike test, aplica una subida subita y grande simulando una promocion o una noticia viral, y responde si el sistema reacciona a tiempo; anticipa el limite del autoescalado de la Clase 13, porque arrancar una instancia toma decenas de segundos y un pico mas rapido golpea antes de que llegue la ayuda.

**[Slide 12] Rendimiento sin stress-tool de pago** — 6 vinetas.

**[Slide 13] «Que sea rapido» no es un requisito** — 12 vinetas.

**[Slide 14] El ensayo del pitch: la segunda mitad tiene su propia teoria** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Cinco a ocho minutos son entre 700 y 1000 palabras habladas, lo que alcanza para siete u ocho ideas y no mas, asi que el guion se escribe por presupuesto de tiempo: unos 45 segundos para el problema y el usuario
  - 60 para el diagrama de Contexto, 90 para los Contenedores y las decisiones que los separan, 60 para seguridad y despliegue, 45 para el pipeline y las metricas, 45 para costos y escalabilidad, y 30 de cierre.
  - La regla de oro del pitch de arquitectura es que se presentan decisiones con su trade-off, no un recorrido por las cajas del diagrama: "elegimos base de datos gestionada aunque cuesta el doble
  - Porque no podemos garantizar respaldos manuales" es una frase de arquitecto; "aqui tenemos una base de datos" es una leyenda de imagen.
  - PREGUNTAS FRECUENTES Y CIERRE CONCEPTUAL ()
  - La segunda es si no basta con decir que se usara cache; la respuesta es que una mitigacion sin medicion es una creencia
  - Y que la pregunta correcta es cache de que, con que tiempo de vida, que porcentaje de aciertos se espera y que pasa cuando el dato cambia, porque una cache mal invalidada convierte un problema de lentitud en un problema de datos incorrectos, que es peor.
  - La tercera es cual es un buen p95, y la respuesta debe resistir la tentacion de dar una cifra universal: depende del caso de uso
  - Y el criterio es que el numero este justificado y sea alcanzable con la arquitectura dibujada
  - Quien promete p95 de 50 milisegundos con una consulta que recorre toda la tabla tiene un objetivo incoherente, y eso es un hallazgo mas grave que tener un objetivo modesto.
  - Tres preguntas llegan siempre.
  - (No se proyecta) La segunda mitad de la clase es el ensayo del pitch y tiene su propia teoria.
  - (No se proyecta) Se ensaya hoy con cronometro y en voz alta, porque leer mentalmente siempre da la mitad del tiempo real, y sin leer las diapositivas, ya que en la Clase 15 el criterio es que quien sustenta pueda explicar cualquier parte del sistema; si el docente autorizo equipos, se ensaya ademas con rotacion de expositor, porque alli el criterio aplica a cualquier integrante.
  - (No se proyecta) Hay que decir explicitamente que este ensayo no es la sustentacion, que es la Clase 15, ni el Parcial 3 de la Clase 14, que es evaluacion escrita: son tres cosas distintas y mezclarlas confunde al grupo.

**[Slide 15] Preparación de presentación (5–8 min)** — 5 vinetas.


## Referencias a diapositivas
Numeración real del deck `Clases/Clase 12 - Pruebas de rendimiento y preparacion final/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 12 · Pruebas de rendimiento · Preparación de presentación final
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. Latencia, throughput y concurrencia: la identidad que las une
5. Por que el promedio miente y el percentil no
6. Las metricas objetivo, escritas como se verifican
7. Los umbrales de percepcion, y por que son convenciones
8. El escenario de carga: aritmetica de servilleta
9. El cuello de botella: siempre hay uno
10. El presupuesto de latencia del camino critico
11. Los tipos de prueba, por la pregunta que responden
12. Rendimiento sin stress-tool de pago
13. «Que sea rapido» no es un requisito
14. El ensayo del pitch: la segunda mitad tiene su propia teoria
15. Preparación de presentación (5–8 min)
16. Del boceto al código Mermaid
17. Clase 12 · cierre conceptual

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3]
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Escenario de rendimiento + ensayo 5–8 min de sustentación**.
Entregable concreto: Sección Rendimiento + guion de pitch + paquete casi-final.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 12]
Cubre estos conceptos, en este orden, ~15 min cada uno, con su diapositiva:
- **Rendimiento sin stress-tool de pago** · [Slide 12]
- **Preparación de presentación (5–8 min)** · [Slide 15]

**Ninguna se salta**: cada una de esas diapositivas es el mecanismo con que se resuelve
al menos una pregunta de la actividad calificada de hoy.
El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · [Slide 16]
Herramienta del día: **Navegador · editores de diagramas y de texto del curso**.
**Demo que usted debe poder repetir:** Definir un objetivo de rendimiento que si se puede verificar

1. Escriba la frase mala: «la app debe ser rapida». Pregunte al grupo como la comprobarian; deje que fallen.
2. Reescribala en vivo: «el p95 del endpoint de consulta responde en menos de 300 ms con 50 peticiones por segundo».
3. Explique el p95 con 20 numeros en el tablero: ordene y marque el que deja 95% por debajo.
4. Cierre pidiendo el bottleneck sospechado: «cual pieza creen que revienta primero, y por que esa».

Narra los clics en voz alta. Si falla la red, proyecta la solución docente de este kit (`Solucion Taller Clase 12 - CloudLite.md`), que trae el resultado esperado.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»

**Si se hace el taller, cierra la demo en la plataforma del curso** (sin diapositiva: el flujo está en el `Taller … .docx`) — es el paso que el estudiante no adivina: pasa el boceto a codigo Mermaid con ayuda de una IA, pegalo en la pregunta de diagrama y muestralo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `sequenceDiagram`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en la plataforma del curso** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de la plataforma del curso.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste) · opcional · sin diapositiva
El taller es **opcional** y ya no está en el deck: si se hace hoy, comparte el `Taller … .docx` de
`Clases/Clase 12 - Pruebas de rendimiento y preparacion final/` (los pasos también están en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 12/Quiz Clase 12 - Pruebas de rendimiento y preparacion final.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 17]
Di: «Queda avanzado: Escenario de rendimiento + ensayo 5–8 min de sustentación.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en la plataforma del curso. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: describan el escenario de carga del pico real de su dominio con los 6 datos obligatorios (evento del pico, usuarios concurrentes, peticiones por segundo, mezcla de operaciones en porcentajes que sumen 100, duracion de la ventana y volumen de datos de partida), verificando que la mezcla sume exactamente 100 por ciento y que el pico corresponda a una fecha real del calendario de su dominio.
2. Paso 2: definan las 3 metricas objetivo en una tabla de 4 columnas con numero, ventana de medicion, forma de medirla y consecuencia de incumplirla, verificando que cada objetivo tenga un numero y una ventana (por ejemplo p95 por debajo de 800 ms en 5 minutos) y que ninguna diga rapido o aceptable sin cifra.
3. Paso 3: escriban en la plataforma del curso el sequenceDiagram del camino critico con el presupuesto de latencia repartido por salto, verificando que la suma de los tramos sea menor o igual al objetivo de p95 y que la nota final muestre el margen restante en milisegundos.
4. Paso 4: ensayen el pitch de 5 a 8 minutos con cronometro y llenen la tabla de guion de 6 filas con minuto, seccion, quien habla, mensaje clave y evidencia en pantalla, verificando que la suma de los minutos quede entre 5 y 8, que ninguna seccion pase de 2:00 (y, si el docente autorizo equipo, que todos los integrantes hablen) y que cada seccion tenga una evidencia concreta que se pueda mostrar.
5. Paso 5: cierren los 5 items del backlog de la Clase 11 dejando registro de los residuales, dejen el paquete casi final ordenado en el repositorio o el Drive y suban las 6 preguntas a la plataforma del curso (modulo Talleres) antes del domingo 23:59, verificando que el cuello de botella declarado en el analisis sea el mismo que muestra el diagrama de secuencia.

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
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase12.png | receta: 1) Abre Navegador · editores de diagramas y de texto del curso y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 12/Capturas/demo-clase12.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase12.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 12/Capturas/evidencia-clase12.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: la plataforma del curso (la plataforma del curso). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
