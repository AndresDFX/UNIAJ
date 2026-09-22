# Guion docente — Clase 8: Taller de aplicación del ciclo de vida

## Información de la clase
- Asignatura: Introducción a la Ingeniería (FI300101)
- Duración del bloque: **90 min**
- Tipo: Clase virtual sincrónica por Microsoft Teams · Sesión 5 de 11 (sesión doble junto con la Clase 7) · corresponde al tema 8 del microcurrículo
- Modalidad: **Virtual (síncrona)** por Microsoft Teams · actividades en plataformas gratuitas en la nube · los 5 equipos trabajan en **salas de grupo**
- Corte **2** (30%) · RAA: **RAA3**
- **Material general para los tres grupos** (SB141B, SB141C, LB141F): sin fechas ni horarios de reloj. El reloj de pared de cada grupo está en su `CALENDARIO_2026-2 - <GRUPO>.md`.
- Enfoque: Aprendizaje basado en competencia + Aprendizaje Invertido · Estrategia: ABPr — Aprendizaje Basado en Proyectos

> **Esta es una sesión de taller, no de contenido nuevo.** La teoría se comprime a 20 minutos —cuatro casos y dos herramientas— y la actividad en equipos se extiende a 40, porque el entregable es una **decisión**: cuál de las dos alternativas de solución se construye, con qué alcance y cómo se va a validar. Es la fase de diseño empezando de verdad.

## Objetivos de la clase
- Identificar, en un caso real, **qué fase se saltó** y qué habría costado no saltarla.
- Comparar dos alternativas de solución con una **matriz de criterios** y decidir con argumento.
- Definir el **alcance mínimo** del proyecto: qué entra en el semestre y qué queda fuera.
- Escribir el **plan de validación**: cómo se va a saber que la solución sirve.

## Hoy avanzamos el proyecto en…

**Decidir cuál de las dos alternativas se construye, con matriz de criterios, y fijar el alcance mínimo del semestre y el plan de validación**

**Entregable concreto:** la matriz de decisión, el alcance mínimo con su lista de exclusiones y el plan de validación en el documento del equipo, más el flujo de la alternativa elegida en draw.io

**Herramientas de esta sesión:** diagrams.net (draw.io) · Google Drive (Docs y Slides)

> La matriz de decisión y el alcance van en el **documento del equipo**; el flujo de la alternativa elegida se dibuja en **diagrams.net (draw.io)**. Hoy no se usa IA: la decisión tiene que ser defendible por el equipo, y una recomendación de asistente no es un argumento — además desconoce las restricciones locales, que son justamente el criterio que decide.

## Fundamento teórico para el docente

Esta sección está escrita para dictar la clase **sin consultar otra fuente**, y va dividida por diapositiva: cada bloque dice a qué diapositiva corresponde.

### La pregunta de entrada: 45 minutos y una fase saltada - diapositiva 4

Proyectado en la lamina «La pregunta de entrada: 45 minutos y una fase saltada» (5 vinetas).

- El código llevaba años funcionando.

- Lo que falló fue el **paso controlado de una fase a la siguiente**: un despliegue que dejó una versión antigua activa en uno de los servidores, un sistema automático operando a velocidad de máquina, y ninguna manera de frenar rápido cuando empezó a hacer daño.

- En cuestión de minutos las pérdidas fueron enormes y la firma no sobrevivió como empresa independiente.

- La fuerza está en la pregunta, y el nombre lo pueden buscar ellos cuando se les pida citar la fuente.

### Los cuatro casos: qué contar y cómo exigir la fuente - diapositiva 5

Proyectado en la lamina «Los cuatro casos: qué contar y cómo exigir la fuente (1/2)» (5 vinetas).

- Cuatro casos, cinco minutos en total, un minuto y algo por caso.

- Un sistema automatizado de manejo de maletas de una escala sin precedentes, contratado con el plazo de apertura ya fijado y sin pruebas a escala real; retrasó la apertura del aeropuerto muchos meses, funcionó parcialmente durante años y terminó abandonado.

- La demanda del primer día era perfectamente previsible —una fecha anunciada, una población conocida— y aun así el sitio no aguantó.

### La matriz de decisión: cómo se decide sin que la decisión ya estuviera tomada - diapositiva 6

Proyectado en la lamina «Los cuatro casos: qué contar y cómo exigir la fuente (2/2)» (5 vinetas).

### Alcance mínimo y plan de validación: el entregable del taller - diapositivas 7 y 8

Proyectado en la lamina «La matriz de decisión: cómo se decide sin que la decisión ya estuviera tomada (1/2)» (5 vinetas).

- «Elegimos la lista publicada en vez de la aplicación; perdemos la actualización en tiempo real y ganamos que funcione sin conexión y sin capacitar a nadie.» Un equipo que puede decir qué perdió entendió que estaba decidiendo, no acertando.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 8 - Taller de aplicacion del ciclo de vida/Presentacion.pptx`. Las etiquetas [Slide N] del plan y las referencias del fundamento apuntan aquí.

1. Portada · Clase 8
2. Agenda de hoy (90 min)
3. Objetivos de la sesión
4. Pregunta de entrada
5. Cuatro proyectos que se saltaron una fase
6. Cómo se decide entre dos alternativas
7. Alcance mínimo: qué entra y qué no
8. El plan de validación, y dos trampas
9. La pregunta de entrada: 45 minutos y una fase saltada
10. Los cuatro casos: qué contar y cómo exigir la fuente (1/2)
11. Los cuatro casos: qué contar y cómo exigir la fuente (2/2)
12. La matriz de decisión: cómo se decide sin que la decisión ya estuviera tomada (1/2)
13. La matriz de decisión: cómo se decide sin que la decisión ya estuviera tomada (2/2)
14. Alcance mínimo y plan de validación: el entregable del taller (1/2)
15. Alcance mínimo y plan de validación: el entregable del taller (2/2)
16. Taller de hoy: Decisión de la solución y alcance mínimo
17. Cómo se expone en 3 minutos
18. Para la Clase 9
19. Cierre · Nos vemos en la sesión 9

## Plan de clase minuto a minuto (90 min)

### 00:00–00:10 · Apertura · [Slide 4]

Comparta pantalla antes de que entre el primero:

> «Una empresa perdió cientos de millones de dólares en 45 minutos por un despliegue mal hecho. ¿En qué fase estaba el error?»

**[Nota docente]:** no dé el nombre de la empresa. Van a responder «en la programación» y esa es la respuesta equivocada que hace la clase.

**[Nota docente]:** avise en el minuto 2 que **hoy la actividad dura 40 minutos** y que el entregable es una decisión, no un análisis. Los equipos administran distinto el tiempo cuando lo saben.

### 00:10–00:30 · Teoría comprimida (20 min) · [Slide 5][Slide 6][Slide 7][Slide 8]

Reparto estricto:

- **6 min** · Los cuatro casos [Slide 5], minuto y medio cada uno. Revele que el de la apertura es el cuarto y **vuelva al muro**.

- **6 min** · La matriz de decisión [Slide 6]. Lo esencial es la trampa del paso 3: **los pesos se deciden antes de mirar las alternativas**.

- **5 min** · Alcance mínimo [Slide 7]. Dicte la prueba: *si construimos solo esto, ¿le sirve de algo a la persona que vive el problema?*

- **3 min** · El plan de validación y las dos trampas [Slide 8]. **No lo recorte**: es lo que va a decidir la calidad de la Clase 12.

**[Nota docente]:** si va retrasado, recorte los casos a cuatro minutos y quédese con el del aeropuerto (requisitos) y el de la firma financiera (operación).

### 00:30–01:10 · Taller extendido en salas de grupo (40 min) · [Slide 9]

**3 min** para organizarse. El documento del equipo y draw.io abiertos.

**Ritmo sugerido dentro de la sala** —dígaselo al repartir, porque 40 minutos sin estructura se van en discutir la primera línea:

- 10 min · las dos alternativas escritas en una frase, y los criterios con sus pesos **antes** de calificar.

- 12 min · calificar con justificación de media línea, decidir y escribir qué se pierde.

- 10 min · el alcance mínimo y la lista de «versión siguiente».

- 5 min · el plan de validación: con quién, qué tareas, qué se observa.

**[Nota docente]:** entre a las cinco salas dos veces. En la primera ronda revise **que los pesos estén escritos antes de las calificaciones**; en la segunda, que el alcance mínimo resuelva algo por sí solo.

**[Nota docente]:** si un equipo llega sin las dos alternativas del trabajo independiente, hágalas escribir en cinco minutos ahí mismo. Sin dos alternativas no hay decisión que tomar y la sesión se les pierde.

### 01:10–01:25 · Exposiciones · [Slide 10]

5 equipos × 3 min. **El minuto obligatorio es «qué perdimos al decidir»**: es lo que demuestra que decidieron en vez de acertar.

**[Nota docente]:** los cinco enlaces en el chat antes de arrancar.

**[Nota docente]:** anote la alternativa elegida y el alcance mínimo de cada equipo. En la sesión 10 se prototipa exactamente eso, y en la 12 se prueba.

### 01:25–01:30 · Cierre (5 min) · [Slide 11][Slide 12]

Una idea: **decidir no es acertar.** Una decisión de ingeniería se defiende con criterios escritos antes, con una justificación por criterio y con la lista de lo que se sacrificó.

Recuerde las dos trampas de la validación —no probar con el equipo, no preguntar «¿le gusta?»— porque se van a aplicar en la Clase 12.

Anuncie la sesión 9: **antecedentes y fuentes**. Antes de construir hay que saber qué ya existe y quién lo intentó, con fuentes que se puedan verificar.

## Errores frecuentes y cómo cortarlos en caliente

| Lo que dice el equipo | Por qué no sirve | Qué pedir en su lugar |
|---|---|---|
| «(A) una app y (B) una app con más funciones» | Es la misma idea dos veces: no hay decisión que tomar y la matriz no enseña nada. | Una alternativa que **no use ninguna tecnología nueva**. La comparación entre lo que ya se puede hacer y lo que se quiere construir es la más instructiva. |
| Los pesos y las calificaciones escritos al mismo tiempo | Ahí se cuela la decisión ya tomada: sin mala intención, los pesos se acomodan para que gane el favorito. | Los criterios y los pesos primero, en el documento, y solo después las calificaciones. |
| Una matriz de puros números, sin justificaciones | El número no se puede discutir ni defender; la justificación sí. Sin ella la matriz es un adorno. | Media línea por casilla: por qué ese número para esa alternativa en ese criterio. |
| «No perdemos nada con esta decisión» | Si una alternativa fuera mejor en todos los criterios no habría habido nada que decidir. | Qué se sacrifica, concreto y verificable. Y que se diga en la exposición final. |
| «Vamos a probar el prototipo entre nosotros» | Quien construyó sabe dónde hay que tocar: la prueba está decidida antes de empezar. Es el error del Therac-25 en pequeño. | El rol de una persona ajena al equipo y cómo la van a contactar, hoy mismo. |

## Dudas frecuentes del estudiante

**¿Y si las dos alternativas nos parecen igual de buenas?**

Entonces los criterios están mal elegidos o los pesos no reflejan sus restricciones. Revisen los requisitos no funcionales: casi siempre hay uno que una de las dos no cumple, y ahí se rompe el empate. Y si de verdad empatan, elijan la más simple: es la que se puede construir y probar en el tiempo que queda.

**¿Podemos cambiar la decisión después?**

Sí, y por eso se escribe la matriz: si en la Clase 10 aparece un dato nuevo, se cambia una calificación y se ve si la decisión se mueve. Eso es rediseñar con argumento. Lo que no funciona es cambiar de idea sin registro, porque en la Clase 15 nadie va a poder explicar por qué se hizo lo que se hizo.

**¿El alcance mínimo no nos va a dejar con un proyecto muy pobre?**

Al contrario. Se califica lo que funciona y se puede demostrar, más lo que ustedes declaran que dejaron fuera y por qué. Un alcance mínimo cumplido y probado con un usuario real, con su lista de «versión siguiente», se ve dirigido; un proyecto grande a medias se ve incompleto.

**¿A quién le pedimos que pruebe el prototipo?**

A alguien que viva el problema y que no sea del equipo: el actor que identificaron en la sesión 6. Si no logran conseguir a nadie, ese es un problema de proyecto, no de logística, y hay que resolverlo ahora. Y recuerden la regla del curso: se usa el **rol** de la persona, no su nombre ni sus datos.

## Notas operativas

- **El reparto de hoy es distinto: teoría 20 min, actividad 40 min.** Avísele al grupo en el minuto 2: los equipos administran mejor 40 minutos cuando saben que los tienen.
- **Dé el ritmo interno de la sala al repartir** (10-12-10-5). Cuarenta minutos sin estructura se van en discutir la primera línea.
- Entre a cada sala **dos veces**. Primera ronda: que los pesos estén escritos antes de las calificaciones. Segunda: que el alcance mínimo resuelva algo por sí solo.
- Si un equipo llega sin las dos alternativas, deles **cinco minutos** para escribirlas y sugiera que una no use tecnología nueva. No los deje improvisar veinte minutos.
- **Anote la alternativa elegida y el alcance mínimo de cada equipo.** En la sesión 10 se prototipa eso mismo y en la 12 se prueba: la lista es la que permite detectar desvíos.
- Exija el **rol** de la persona ajena que va a validar y cómo la van a contactar. Si un equipo no puede nombrar a nadie, el proyecto falló el criterio de acceso a los actores y hay que reducirlo hoy.
- Si un equipo cita montos o fechas de los cuatro casos, pida fuente y año. Las cifras de estos casos circulan con variaciones.

## Material de esta clase

- Deck: `Clases/Clase 8 - Taller de aplicacion del ciclo de vida/Presentacion.pptx`
- Taller del estudiante: `Clases/Clase 8 - Taller de aplicacion del ciclo de vida/Taller Clase 8 - Decision de la solucion y alcance minimo.docx`
- Solución del taller (**solo docente**): `Kit docente/Clase 8/Solucion Taller Clase 8 - Decision de la solucion y alcance minimo.docx`
- Este guion: `Kit docente/Clase 8/Guion Docente Clase 8 - Taller de aplicacion del ciclo de vida.docx`

> **Recordatorio de datos personales:** ninguna actividad de este curso sube nombres, cédulas, teléfonos ni fotos de terceros. Si el caso del equipo los trae, se usa el rol («la dueña de la papelería», «el auxiliar de la biblioteca»).
