# Guion docente · Clase 14 · Preparacion de la sustentacion y cierre

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Avance del PI (si se hace la practica):** Queda armado el guion cronometrado de sustentacion de VetCare y consolidado el documento final de diseño en una sola pieza coherente.
- **Practica (opcional):** `Clases/Clase 14 - Preparacion de la sustentacion y cierre/Taller PI - Clase 14 - VetCare.docx` — no esta en el deck
- **Herramienta:** Google Docs · draw.io · Figma o Penpot
- **Slides:** `Clases/Clase 14 - Preparacion de la sustentacion y cierre/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] Sustentar es defender decisiones** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Sustentar un paquete de diseño no es leer diapositivas ni narrar lo que el equipo hizo cada semana: es demostrar que las decisiones tomadas son defendibles.
  - El jurado, sea el docente o un cliente simulado de la clinica, no esta evaluando cuanto trabajaron sino tres cosas concretas: si el diseño resuelve el problema declarado, si las piezas son coherentes entre si y si el equipo entiende lo que entrego.
  - La diferencia se nota en la primera frase: quien dice hicimos casos de uso, luego clases, luego pantallas, esta narrando; quien dice la clinica pierde fichas y tarda ocho minutos en encontrar un historial
  - Y este paquete de diseño ataca esos tres problemas asi, esta sustentando.
  - En la clinica la evidencia esta toda disponible: la tabla de RF y RNF, los diagramas UML, el diccionario de datos y el prototipo navegable.
  - El trabajo de hoy es ordenar esa evidencia para que cuente una sola historia.
  - Una sustentacion es, por definicion, la defensa oral de un conjunto de decisiones frente a quien las va a evaluar o a usar.
  - El error comun es ordenar la exposicion por documento, primero requisitos y luego diagramas, en lugar de ordenarla por problema resuelto.
  - NOTAS:
  - Por eso una sustentacion es un argumento con evidencia, no un recuento cronologico.
  - En la clinica esa historia empieza por el problema, las fichas de papel que se pierden y los ocho minutos para encontrar un historial, y termina mostrando en el prototipo como cada requisito queda resuelto.

**[Slide 5] El orden en embudo** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El orden de la sustentacion no es libre, es un embudo y tiene una razon logica.
  - Segundo los requisitos, porque son la promesa concreta: que va a hacer el sistema y con que restricciones.
  - Cuarto la interfaz, porque es donde el jurado por fin ve y toca.
  - Y quinto las decisiones, que es la parte que separa a un equipo que entendio de uno que copio plantillas.
  - Invertir ese orden es el error mas comun: los equipos empiezan mostrando pantallas bonitas, el jurado pregunta que problema resuelve eso y ahi la sustentacion se desarma.
  - Para la clinica doce minutos alcanzan de sobra si se respetan las proporciones: uno y medio para el problema, uno y medio para el alcance
  - Dos para requisitos, dos para modelo, dos para interfaz en vivo, dos para decisiones y el ultimo minuto para riesgos y cierre.
  - NOTAS:
  - Primero el problema, porque nada de lo que sigue tiene sentido si el jurado no sabe que duele en la clinica.
  - Tercero el modelo, casos de uso y clases, porque muestra como se organiza la solucion.

**[Slide 6] Cómo se defiende una decisión** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Defender una decision de diseño tiene una estructura fija que conviene memorizar: decision, alternativas consideradas, criterio de eleccion y consecuencia asumida.
  - Ejemplo concreto de la clinica: decidimos separar Historia_Clinica de Mascota como clases distintas; la alternativa era guardar diagnosticos y tratamientos como campos dentro de Mascota
  - El criterio fue que una mascota tiene muchas consultas a lo largo de su vida y una relacion uno a muchos no cabe en campos fijos
  - La consecuencia es que hay una entidad mas y una consulta adicional al mostrar la ficha, lo cual se acepta porque el RNF de busqueda menor a tres segundos se sostiene con un indice.
  - Otro ejemplo: decidimos que la fecha de nacimiento sea opcional; la alternativa era hacerla obligatoria
  - El criterio fue que en la clinica muchos dueños de mascotas rescatadas no la conocen y un campo obligatorio los llevaria a inventar datos; la consecuencia es que la edad se muestra como aproximada cuando el dato falta.
  - NOTAS:
  - No basta decir que se hizo, hay que decir contra que se comparo y por que gano.
  - Una decision defendida asi resiste cualquier pregunta, porque el jurado ya sabe que el equipo penso en la alternativa.

**[Slide 7] Las preguntas previsibles del jurado** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Las preguntas del jurado son bastante predecibles y por eso se preparan.
  - Las mas frecuentes en un proyecto como el de la clinica son: como sabe usted que este requisito es realmente necesario; que pasa si dos recepcionistas registran la misma mascota al mismo tiempo; por que esta clase existe y no es un atributo de otra
  - Como se cumple el requisito no funcional que usted escribio y como se mediria; que pasa si el sistema se cae a mitad de un registro; que dejaron por fuera del alcance y por que; y quien de ustedes hizo esta parte.
  - Hay que preparar la respuesta de cada una en dos frases, sin discursos.
  - Y hay una regla de oro para cuando no se sabe: no se inventa.
  - NOTAS:
  - La respuesta correcta es reconocer el vacio y proponer como se resolveria, por ejemplo no lo modelamos, lo registramos como riesgo abierto y se resolveria agregando una validacion de unicidad por dueño mas nombre en el diccionario de datos.
  - Un jurado castiga mucho mas la improvisacion detectada que la honestidad tecnica.

**[Slide 8] El guion en bloques con tiempos** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El reparto del guion en bloques con tiempos es lo que sostiene una sustentacion, no un detalle logistico.
  - La sustentacion es individual por defecto: el estudiante expone los cinco bloques y responde por todos, y lo que importa es que cada bloque tenga su rango de minutos y su evidencia en pantalla, no quien lo dice.
  - El orden que funciona para la clinica es: abrir con problema y alcance, seguir con requisitos y trazabilidad, luego los modelos UML, despues el prototipo en vivo y cerrar con decisiones, riesgos y siguiente paso hacia Programacion II.
  - Si el docente autorizo equipo de 2 o 3, se agrega el nombre del responsable a cada bloque, todos los integrantes deben hablar al menos dos minutos y ninguno puede hablar solo de lo suyo: cada persona domina una pieza pero debe conocer el todo
  - Porque el jurado tiene derecho a preguntarle a cualquiera sobre cualquier parte.
  - Ademas se prepara el plan B tecnico: capturas del prototipo por si falla el internet, el documento en PDF descargado y los diagramas exportados a imagen.
  - Y algo que parece obvio pero se olvida siempre: quien maneja el prototipo debe haberlo recorrido antes haciendo clic en cosas que no estaban en el guion, porque el jurado va a hacer exactamente eso.
  - NOTAS:
  - Se ensaya cronometrado al menos dos veces, en voz alta y de pie, porque el tiempo estimado leyendo en silencio siempre es la mitad del real.

**[Slide 9] El guion cronometrado de la sustentacion** — 13 vinetas.

**[Slide 10] Guion de sustentacion: doce minutos cronometrados** — 12 vinetas.


**Demo que usted debe poder repetir:** El docente proyecta una sustentacion mal hecha y una bien hecha del mismo paquete VetCare, y luego arma en vivo la tabla de decisiones para justificar por que Historia_Clinica es una clase aparte de Mascota.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy el tema es: Preparacion de la sustentacion y cierre. Todo lo que vamos a ver esta en las laminas.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de teoria (una por concepto)
y en las de codigo proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente proyecta una sustentacion mal hecha y una bien hecha del mismo paquete VetCare, y luego arma en vivo la tabla de decisiones para justificar por que Historia_Clinica es una clase aparte de Mascota.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 14/Plantillas/Guion-y-Decisiones-Sustentacion-VetCare.md`

### 60-105 · Practica guiada (OPCIONAL) = avance del PI
No hay laminas para esta franja: la guia es el archivo
`Clases/Clase 14 - Preparacion de la sustentacion y cierre/Taller PI - Clase 14 - VetCare.docx` (compartirlo, no proyectarlo).
Si hoy no se hace, usar el tiempo para profundizar la teoria y la demo.
**Decir (si se hace):** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Paso 1. Arme en Google Docs el guion cronometrado de doce minutos con las cinco secciones obligatorias en orden problema, requisitos, modelo, interfaz y decisiones, asignando a cada bloque su rango de minutos exacto y la evidencia que se muestra en pantalla en ese bloque; ningun bloque puede quedar sin rango de minutos ni sin evidencia asociada. Si el docente autorizo equipo, escriba ademas el nombre del responsable de cada bloque y reparta de modo que ningun integrante quede con menos de dos minutos.
2. Paso 2. Llenen la tabla de tres decisiones de diseño de VetCare con las cuatro columnas decision, alternativa descartada, criterio y consecuencia asumida; una de las tres decisiones debe ser sobre el modelo de clases y otra sobre un requisito no funcional.
3. Paso 3. Construyan el banco de diez preguntas del jurado con su respuesta en maximo dos frases, incluyendo obligatoriamente que pasa si dos recepcionistas registran la misma mascota, como se mide su RNF de tiempo de respuesta y que quedo fuera del alcance.
4. Paso 4. Haga un ensayo cronometrado de pie, con el prototipo abierto, y registre el tiempo real de cada bloque; recorte lo que se paso y anote los dos puntos donde se enredo al hablar (si trabaja en equipo, donde se enredo la transicion entre un expositor y el siguiente).
5. Paso 5. Consoliden el documento final armando el indice completo desde problema hasta trazabilidad, verifiquen que los nombres de las clases, los campos del diccionario y los campos de las pantallas coinciden exactamente, y corrijan al menos una inconsistencia encontrada dejando constancia de cual era.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Un documento en Google Docs con el guion minuto a minuto repartido en bloques con tiempos y evidencia (con responsable nominal solo si el docente autorizo equipo), la tabla de tres decisiones de diseño defendidas y el banco de diez preguntas con su respuesta, mas el indice del documento final consolidado, subido a ExamLab.

### 105-120 · Sintesis y cierre
Si hubo practica, repasar los criterios de exito del archivo del taller (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 14/Quiz Clase 14 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir (si hubo practica):** «Queda avanzado: Queda armado el guion cronometrado de sustentacion de VetCare y consolidado el documento final de diseño en una sola pieza coherente.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 14/Solucion Taller Clase 14 - VetCare.docx` — no proyectar completa.
