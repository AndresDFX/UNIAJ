# Solución del taller — Clase 7: Ciclo de vida del proyecto

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni compartir pantalla con él antes de que los equipos trabajen: es la respuesta completa del entregable, y verla antes convierte el taller en copia.

## Para qué sirve este documento

Este documento trae el ciclo de vida completo del caso de la biblioteca, con los cinco requisitos escritos y sus criterios de aceptación, más el plan de hitos hasta la sesión 15. Es el modelo que hay que tener a mano en las salas, porque el criterio de aceptación es lo que ningún equipo escribe solo. Si el docente solo alcanza a leer un bloque, que sea **LOS CRITERIOS DE ACEPTACIÓN**.

## El caso que se resuelve aquí

**La biblioteca del barrio · del problema a los requisitos**

Se retoma la ficha cerrada en la sesión 6: los usuarios no pueden saber si un libro está disponible antes de ir, así que hacen viajes que terminan sin préstamo (unas 4 de cada 10 visitas). Causa elegida: el registro de préstamos solo se puede consultar en el mostrador. Restricciones marcadas: presupuesto cero, no hay computador disponible en el mostrador durante la atención, las voluntarias rotan y no se les puede exigir capacitación larga, y nadie puede atender un teléfono en horario fijo.

> Es el mismo caso desde la sesión 1, y hoy es donde se cobra: las cuatro restricciones que en la sesión 6 parecían una formalidad se convierten hoy en requisitos no funcionales que descartan la mitad de las soluciones posibles. Mostrar esa conversión es la lección de la sesión.

## Consigna que se les dio

> Ubiquen su proyecto en el ciclo de vida y escriban lo que falta para avanzar: en qué **fase** están, **tres requisitos funcionales** y **dos no funcionales** con su **criterio de aceptación**, la decisión de hoy que sería carísima cambiar después, y el **plan de hitos** hasta la sesión 15.

**Entregable:** el mapa del ciclo de vida del proyecto en draw.io (PNG en la carpeta del equipo) más la tabla de requisitos y el plan de hitos en el documento del equipo · **17 min de trabajo · 3 min de exposición**

## Respuesta bloque por bloque

### 1. EN QUÉ FASE ESTAMOS

**Se pedía:** La fase donde está el proyecto hoy, y **qué falta exactamente para cerrarla**. Una fase se cierra con un entregable, no con una sensación.

**Respuesta modelo:**

**Fase: requisitos.** La fase 1 —definición del problema— quedó cerrada en la sesión 6 con la ficha, que tiene enunciado, línea base, árbol de causas, actores y criterio de éxito.

**Qué falta para cerrar la fase de requisitos:** la tabla de requisitos con sus criterios de aceptación **validada con la coordinadora de la biblioteca**. Este último detalle es el que distingue una fase cerrada de una fase que se cree cerrada: los requisitos no se aprueban entre los cinco del equipo, se confirman con quien vive el problema.

**Qué NO es cerrar la fase:** tener una idea clara de lo que se va a hacer. Una fase se cierra con un entregable que otra persona puede leer y objetar.

**Cómo calificar:** 15 pts. Se califica que haya **un entregable pendiente concreto**, no una sensación. «Estamos en diseño» vale 5; «estamos en requisitos y falta la tabla validada con la coordinadora» vale los 15. Si el equipo dice que está en construcción sin tener requisitos escritos, es la señal de alarma de la sesión y hay que decírselo en la sala: está a punto de construir algo que va a rehacer.

### 2. TRES REQUISITOS FUNCIONALES

**Se pedía:** Tres cosas que la solución **hace**, escritas desde el usuario: «el usuario puede…». Sin mencionar tecnología.

**Respuesta modelo:**

1. **El usuario puede saber si un libro está disponible sin ir a la biblioteca.**
2. **La voluntaria puede registrar un préstamo y una devolución en menos pasos que en el cuaderno**, sin dejar de atender al usuario que tiene enfrente.
3. **El usuario puede ver qué libros hay sobre un tema**, aunque no sepa el título exacto — es el caso real del estudiante de colegio con una tarea.

Los tres empiezan por el actor y ninguno menciona tecnología: podrían resolverse con una lista publicada, un mensaje automático o una aplicación, y esa apertura es deliberada, porque la decisión de **cómo** es de la fase de diseño y se toma en la sesión 8.

**Ejemplos de requisitos mal escritos, para comparar en clase:** «el sistema tendrá una base de datos con los libros» (decisión de diseño disfrazada de requisito, y tomada dos fases antes de tiempo); «el sistema será rápido y fácil de usar» (no es funcional y no es verificable); «hacer una app para la biblioteca» (es la solución, no el requisito, y es el error de la sesión 6 reapareciendo).

**Cómo calificar:** 25 pts. Dos verificaciones mecánicas: (a) **¿empieza por el actor?** Si empieza por «el sistema tendrá», reescríbalo con ellos y baje a 15; (b) **¿nombra alguna tecnología?** Si nombra lenguaje, base de datos o plataforma, baje a 12 y explique por qué: no es un error de forma, es tomar una decisión en la fase equivocada. Acepte requisitos modestos: tres requisitos pequeños y bien escritos valen más que diez ambiciosos.

### 3. DOS REQUISITOS NO FUNCIONALES

**Se pedía:** Dos condiciones que la solución debe cumplir, **derivadas de las restricciones del árbol de la sesión 6**. Uno de los dos tiene que ser el indicador ambiental de la sesión 5.

**Respuesta modelo:**

1. **Funciona sin computador en el mostrador**: la voluntaria lo usa desde su propio celular, y el usuario desde el suyo. *Viene de la restricción «no hay computador disponible en el mostrador durante la atención».*
2. **Se aprende en menos de cinco minutos y sin manual**, porque las voluntarias rotan. *Viene de la restricción «las voluntarias rotan y no se les puede exigir capacitación larga».*

**Y el que exige el curso, derivado del indicador ambiental de la sesión 5:** *funciona en el computador de siete años del consultorio —en este caso, en celulares de gama baja y con datos móviles—, moviendo menos de 200 KB por consulta*. Este requisito no es decoración: descarta soluciones con imágenes pesadas y con actualización permanente, y por lo tanto **es información de diseño**.

Nótese el efecto conjunto: estos tres requisitos no funcionales **descartan la mitad de las soluciones imaginables** antes de diseñar nada. Eso es exactamente lo que deben hacer, y es la razón por la que las restricciones de la sesión 6 no eran una formalidad.

**Lo que no se acepta:** un requisito no funcional inventado hoy y sin rastro («debe ser escalable», «debe usar la nube»). Si no se puede señalar la restricción de donde salió, no entró por la puerta correcta.

**Cómo calificar:** 20 pts, 10 por requisito. El criterio duro es la **trazabilidad**: pida que señalen la restricción del árbol de la sesión 6 de donde salió. Sin rastro, 4 puntos. Si el equipo incorpora el indicador ambiental de la sesión 5 como requisito no funcional, dé los 20 completos: significa que el curso está acumulando y no empezando de cero cada semana.

### 4. LOS CRITERIOS DE ACEPTACIÓN

**Se pedía:** Para cada uno de los cinco requisitos: cómo se comprueba, con un caso concreto y un umbral. Tiene que poder ejecutarlo otra persona.

**Respuesta modelo:**

**R1 · saber la disponibilidad sin ir.** *Un usuario que nunca ha usado el sistema, con el celular en la mano y sin ayuda, averigua si un libro concreto está disponible en menos de un minuto. Se prueba con tres personas distintas; se acepta si las tres lo logran.*

**R2 · registrar préstamo y devolución.** *La voluntaria registra un préstamo en menos de 30 segundos, cronometrado, mientras el usuario espera. Se compara contra el tiempo del cuaderno, medido antes.*

**R3 · buscar por tema.** *Un estudiante que solo sabe el tema («algo sobre la Guerra de los Mil Días») obtiene al menos un título disponible o la respuesta «no hay», sin preguntarle a nadie.*

**RNF1 · sin computador.** *Todo el flujo de R1, R2 y R3 se ejecuta completo desde un celular, con el navegador, sin instalar nada.*

**RNF2 · se aprende sin manual.** *Una persona que no participó en el proyecto y no recibió explicación registra un préstamo correctamente en el primer intento.*

**RNF3 · menos de 200 KB por consulta.** *Se mide con las herramientas del navegador en tres consultas seguidas.*

Los seis tienen la misma forma: **un actor, una acción, una condición y un umbral**, y todos los puede ejecutar alguien que no sea del equipo. Eso es lo que se está calificando.

**Cómo calificar:** 25 pts, el bloque que decide. La prueba es literal: **lea el criterio y pregúntese si usted podría ejecutarlo mañana sin pedir aclaraciones**. Si no, no es un criterio. «Debe ser intuitivo», «debe funcionar bien», «el usuario quedará satisfecho» valen 0 y hay que reescribirlos en la sala, no en la calificación. Un criterio sin umbral —sin el «en menos de», sin el «al menos»— vale la mitad. Y valore especialmente que aparezca **una persona ajena al equipo** en la prueba: probar con quien construyó es el vicio más común y el más inútil.

### 5. EL PLAN DE HITOS

**Se pedía:** Qué queda **terminado y verificable** en cada una de las sesiones 8, 9, 10, 11, 12 y 14. Y la decisión de hoy que sería carísima cambiar en la sesión 14.

**Respuesta modelo:**

**Sesión 8** · Decidida la alternativa de solución entre dos, con matriz de criterios. Alcance mínimo escrito: qué entra y qué no.
**Sesión 9** · Tres antecedentes fichados con fuente verificable, y la propuesta de mejora respecto a lo que ya existe.
**Sesión 10** · Prototipo de baja fidelidad de las tres pantallas o pasos del flujo principal, y el guion de prueba escrito.
**Sesión 11** · Prototipo v2 corregido, con el registro del uso de IA y las correcciones hechas a mano. *Cierra el corte 2.*
**Sesión 12** · Prototipo probado **con una persona ajena al equipo** y la lista de lo que falló, para la presentación de avances.
**Sesión 14** · Presentación final ensayada y el informe escrito al 80 %. *En la sesión 14 no se construye: se ensaya.*

**La decisión de hoy que sería carísima cambiar en la sesión 14:** *que la solución funcione sin computador en el mostrador.* Si en la sesión 12 se descubre que la voluntaria no puede usar su celular durante la atención, hay que rediseñar el flujo completo, y con él el prototipo y la prueba. Por eso se confirma con la coordinadora **esta semana**, no en la 12: hoy cuesta una pregunta.

**Cómo calificar:** 15 pts. Dos verificaciones: (a) **¿cada hito es verificable?** «Avanzar en el prototipo» no es un hito; (b) **¿está repartido?** Si las sesiones 8 a 12 están vacías y todo aparece en la 14, vale 5 y hay que decirlo en voz alta en la sala: es el patrón exacto de los proyectos que no se entregan. Valore que la sesión 14 esté reservada para ensayar y no para construir.

## Rúbrica del taller

| Criterio | Peso | Por qué pesa eso |
|---|---|---|
| La fase está identificada y se dice qué entregable falta para cerrarla | **15 %** | Cerrar una fase con un entregable, y no con una sensación de avance, es la disciplina que ordena el proyecto. |
| Los tres requisitos funcionales están escritos desde el usuario y sin tecnología | **25 %** | Un requisito escrito desde la tecnología toma una decisión de diseño en la fase equivocada. |
| Los dos requisitos no funcionales se rastrean a restricciones ya escritas | **20 %** | Es lo que conecta el análisis de las sesiones 5 y 6 con la construcción: las restricciones son insumo, no adorno. |
| Cada requisito tiene un criterio de aceptación ejecutable por otra persona | **25 %** | Sin criterio de aceptación no hay validación posible, y la sesión 16 pide demostrar, no afirmar. |
| El plan de hitos reparte el trabajo y cada hito es verificable | **15 %** | Un plan con todo al final es la causa más común de proyectos que no se entregan. |

> Suma **100 %**. La nota es del equipo, no del vocero.

## Si el equipo trabajó otro caso

**Equipos que ya quieren estar en construcción.** Van a decir que están en construcción porque ya hicieron algo. Pregunte por los requisitos escritos: si no existen, están en la fase de requisitos con trabajo adelantado, que no es lo mismo. No lo plantee como un regaño sino con la tabla del costo: lo que construyeron sin requisitos es lo que van a tener que rehacer, y todavía es barato.

**Proyectos de proceso o de gestión, sin pantallas.** Los requisitos funcionales se escriben igual, con el actor y la acción; lo que cambia es que el «prototipo» de la sesión 10 va a ser un formato, un flujo o un tablero, no una pantalla. Aclárelo hoy para que el plan de hitos tenga sentido. Buen criterio de aceptación para estos casos: *una persona ajena ejecuta el proceso completo siguiendo solo el formato, sin preguntar*.

**Equipos con requisitos escritos desde la tecnología.** Es el error más frecuente y no hay que pelearlo: reescriba uno con ellos en la sala, en voz alta, y deje que ellos reescriban los otros dos. La pregunta que lo resuelve siempre es «¿y eso qué le permite hacer al usuario?». La decisión técnica que querían escribir no se pierde: se anota aparte, como candidata de la fase de diseño de la sesión 8.

**Equipos cuyo plan de hitos deja todo en la sesión 14.** Es el hallazgo más valioso de la sesión y hay que actuar hoy. Obligue a definir un hito verificable para la sesión 10, aunque sea mínimo — tres pantallas dibujadas a mano y probadas con una persona—. La razón que funciona con estudiantes: en la sesión 12 hay presentación de avances con retroalimentación, y llegar sin nada a esa sesión desperdicia la única corrección gratis del semestre.

## Errores que hay que ver y no dejar pasar

- **«El sistema tendrá una base de datos con los libros»** → No es un requisito: es una decisión de diseño tomada dos fases antes de tiempo, y cierra opciones sin argumento. «¿Y eso qué le permite hacer al usuario?». Reescríbalo empezando por el actor, y anote la decisión técnica aparte para la sesión 8.
- **«El sistema debe ser fácil de usar»** → No se puede convertir en una prueba que alguien ejecute, así que no se puede validar. Un actor, una acción, una condición y un umbral: «una persona que no lo conoce logra X en menos de Y, sin ayuda».
- **«Estamos en construcción» sin requisitos escritos** → Es construir para rehacer: el error de requisitos descubierto en construcción cuesta decenas de veces más. Los requisitos por escrito primero. Lo ya construido no se tira: se usa como prototipo de la sesión 10.
- **«Debe ser escalable / usar la nube» como requisito no funcional** → No sale de ninguna restricción del proyecto: entró por moda y no por análisis. Que señalen la restricción del árbol de la sesión 6 de donde sale cada requisito no funcional.
- **Un plan con todo el trabajo en la sesión 14** → Es el patrón exacto de los proyectos que no se entregan, y desperdicia la retroalimentación gratis de la sesión 12. Un hito verificable en la sesión 10, aunque sea mínimo. La sesión 14 se reserva para ensayar, no para construir.

## Cierre: qué decir en los 3 minutos finales

Tres minutos y una idea: **el orden de las fases no es burocracia, es economía.** El error barato es el que se encuentra temprano, y todo lo que hicieron hoy —requisitos, criterios, hitos— existe para que los errores aparezcan ahora y no en la sesión 15. Diga en voz alta las dos cosas que conectan el curso: la fase 1 la cerraron en la sesión 6, y los requisitos no funcionales de hoy salieron de las restricciones que escribieron entonces; nada de lo que han hecho fue un ejercicio suelto. Cierre con la advertencia sobre Royce, porque es memorable: el dibujo más famoso de la ingeniería de software —la cascada de una sola pasada— aparece en un artículo que decía que hacerlo así invita al fracaso, y la profesión se quedó con el dibujo y perdió la advertencia. Anuncie la sesión 8: casos reales de proyectos que se saltaron una fase, y la decisión entre sus dos alternativas de solución.

## Con qué se conecta

Hacia atrás: la **sesión 6** entregó la ficha del problema, que es el entregable de la fase 1, y sus restricciones son los requisitos no funcionales de hoy; la **sesión 5** aportó el indicador ambiental, que hoy se vuelve requisito; la **sesión 2** dejó a Royce, que hoy se cierra. Hacia adelante: la **sesión 8** decide la alternativa y fija el alcance mínimo; la **sesión 9** busca antecedentes; la **sesión 10** prototipa contra estos requisitos; la **sesión 11** corrige y cierra el corte; la **sesión 12** prueba con una persona ajena; y el **informe final de la sesión 16** se estructura sobre estos criterios de aceptación.
