# Guion docente · Clase 1 · Conceptos iniciales de ingenieria de software

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Tipo:** REGULAR · **presencial** (Clase 1 siempre es presencial)
- **Dia 1:** este bloque comparte espacio con la **Sesion 0** (Presentacion del Curso,
  archivo aparte). Sesion 0 = logistica y encuadre; esta Clase 1 = diagnostico + primer tema.
- **Entregable de hoy:** equipo conformado + dominio del proyecto elegido y acotado
- **Slides:** `Clases/Clase 1 - Conceptos iniciales/Presentacion.pptx`

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo:
> todo eso ya se cubrio en la Sesion 0.

## Fundamento teorico para el docente

**Que es la ingenieria de software y por que no es "programar".** Programar es
escribir codigo que funcione. La ingenieria de software es el conjunto de practicas
que hacen que ese codigo siga funcionando cuando el sistema crece, cuando lo mantiene
otra persona y cuando los requisitos cambian. La diferencia se nota en el costo: un
error detectado al analizar requisitos cuesta corregirlo una fraccion de lo que
cuesta corregirlo en produccion. Esa es la justificacion economica de todo lo que se
vera en este curso.

**Producto vs proyecto.** El *producto* es el software (y su documentacion). El
*proyecto* es el esfuerzo acotado en tiempo y recursos para construirlo. Un proyecto
puede terminar y el producto seguir vivo durante años. Confundirlos lleva a creer que
"entregamos, ya terminamos".

**Requisitos funcionales vs no funcionales.** Un requisito funcional dice QUE debe
hacer el sistema ("registrar una mascota con ID, nombre y especie"). Uno no funcional
dice COMO debe comportarse ("la busqueda de un expediente responde en menos de 2
segundos", "la informacion no se pierde ante un corte de energia"). Los no funcionales
son los que mas se olvidan y los que mas arquitectura condicionan. Regla practica para
el estudiante: si no se puede verificar, no es un requisito — es un deseo. «El sistema
debe ser rapido» no es requisito; «responde en menos de 2 s con 50 usuarios» si lo es.

**Interesados (stakeholders).** No solo el que paga. En la clinica veterinaria del
proyecto hay al menos tres: el dueño de la clinica (quiere metricas), la recepcionista
(quiere agendar rapido) y el veterinario (quiere el historial a la mano). Sus intereses
pueden entrar en conflicto, y resolver ese conflicto es trabajo de analisis, no de
programacion.

**Ciclo de vida del software (introduccion).** Todo desarrollo pasa por las mismas
fases —requisitos, diseño, construccion, pruebas, mantenimiento— y lo que cambia entre
metodologias es COMO se recorren: una sola vez y en orden (cascada) o en ciclos cortos
que repiten todas las fases (iterativo/agil). Hoy solo se nombran; se comparan a fondo
en las Clases 2, 3 y 4.

**El rol del estudiante en este curso.** Aqui no se construye el software: se diseñan
los planos. Es la diferencia entre el arquitecto y el maestro de obra. Conviene decirlo
explicitamente el primer dia, porque un estudiante que espera programar se frustra, y
uno que entiende el rol valora el entregable.

**Error tipico del docente que no domina el tema:** empezar por las metodologias
(cascada, Scrum) antes de que el estudiante entienda que problema resuelven. Sin la
nocion de "el costo del error crece con el tiempo", las metodologias suenan a
burocracia arbitraria.

**Sobre el diagnostico de hoy:** no es una nota. Sirve para saber si el grupo llega con
nociones de UML, de requisitos o de trabajo en equipo. El resultado ajusta la
profundidad de las Clases 2 a 4.

## Plan minuto a minuto (120 min)

### 0-15 · Enlace con la Sesion 0 y encuadre del tema
**Decir:** «Ya vimos como funciona el curso. Ahora arrancamos el primer tema. Y algo
importante desde hoy: en esta materia ustedes no van a programar; van a diseñar. Su
producto son los planos que otro equipo podria construir.»

### 15-35 · Prueba diagnostica
Aplicar `Kit docente/Clase 1/Prueba Diagnostica…`. Individual, sin nota.
**Decir:** «No se califica. Me sirve para calibrar el ritmo.»
Mientras responden, pasar asistencia.

### 35-70 · Teoria Core: que es ingenieria de software
Apoyarse en el fundamento de arriba, en este orden:
1. Programar vs hacer ingenieria (el argumento del costo del error).
2. Producto vs proyecto.
3. Requisitos funcionales vs no funcionales, con la regla «si no se puede verificar,
   no es un requisito».
4. Interesados: los tres de la clinica veterinaria y sus intereses en conflicto.
5. Ciclo de vida: nombrar las fases, sin entrar aun en metodologias.

Ejercicio corto en el tablero (5 min): dar la frase cruda «necesito buscar rapido el
expediente de un animal» y convertirla entre todos en un RF y un RNF bien escritos.

### 70-100 · Taller: conformar equipo y acotar el dominio
En equipos de 2-3:
- elegir el dominio del proyecto (por defecto, la clinica veterinaria del PI),
- escribir el problema en 2-3 frases,
- listar 3-5 capacidades del sistema,
- identificar 2-3 actores.

Circular por los equipos con un solo criterio: **bloquear dominios vagos**. Si el
equipo dice «una app para la universidad», no hay problema concreto y todo el semestre
se les vuelve humo. Exigir un actor con un dolor medible.

### 100-115 · Puesta en comun
Dos o tres equipos leen su ficha. El grupo señala que capacidad no se entiende.
**Decir:** «Si nosotros no entendemos su sistema en 30 segundos, un programador
tampoco va a poder construirlo.»

### 115-120 · Cierre y primer contacto con el Proyecto Integrador
Señalar donde vive el enunciado (`Clases/Proyecto Integrador/`) y explicar los tres
casos segun matricula (cursa ambas materias / solo esta / solo Programacion II).
Dejar claro que quien cursa solo Seminario cierra con documento de diseño y prototipo
navegable, **sin escribir codigo**: es una ruta completa, no una version reducida.

## Cierre docente (despues de clase)

- Revisar el diagnostico y anotar el consolidado en `Entregas docente/<periodo>/DIAGNOSTICO…`.
- Anotar que equipos quedaron con el dominio aun sin acotar: hay que cerrarlo en la Clase 2.
