# Guion docente · Clase 14 · Preparacion de la sustentacion y cierre

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Queda armado el guion cronometrado de sustentacion de VetCare y consolidado el documento final de diseño en una sola pieza coherente.
- **Entregable de hoy:** Un documento en Google Docs con el guion minuto a minuto repartido en bloques con tiempos y evidencia (con responsable nominal solo si el docente autorizo equipo), la tabla de tres decisiones de diseño defendidas y el banco de diez preguntas con su respuesta, mas el indice del documento final consolidado, subido a ExamLab.
- **Herramienta:** Google Docs · draw.io · Figma o Penpot
- **Slides:** `Clases/Clase 14 - Preparacion de la sustentacion y cierre/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Sustentar un paquete de diseño no es leer diapositivas ni narrar lo que el equipo hizo cada semana: es demostrar que las decisiones tomadas son defendibles. El jurado, sea el docente o un cliente simulado de la clinica Huellitas, no esta evaluando cuanto trabajaron sino tres cosas concretas: si el diseño resuelve el problema declarado, si las piezas son coherentes entre si y si el equipo entiende lo que entrego. Por eso una sustentacion es un argumento con evidencia, no un recuento cronologico. La diferencia se nota en la primera frase: quien dice hicimos casos de uso, luego clases, luego pantallas, esta narrando; quien dice Huellitas pierde fichas y tarda ocho minutos en encontrar un historial, y este paquete de diseño ataca esos tres problemas asi, esta sustentando. En VetCare la evidencia esta toda disponible: la tabla de RF y RNF, los diagramas UML, el diccionario de datos y el prototipo navegable. El trabajo de hoy es ordenar esa evidencia para que cuente una sola historia.

El orden de la sustentacion no es libre, es un embudo y tiene una razon logica. Primero el problema, porque nada de lo que sigue tiene sentido si el jurado no sabe que duele en Huellitas. Segundo los requisitos, porque son la promesa concreta: que va a hacer el sistema y con que restricciones. Tercero el modelo, casos de uso y clases, porque muestra como se organiza la solucion. Cuarto la interfaz, porque es donde el jurado por fin ve y toca. Y quinto las decisiones, que es la parte que separa a un equipo que entendio de uno que copio plantillas. Invertir ese orden es el error mas comun: los equipos empiezan mostrando pantallas bonitas, el jurado pregunta que problema resuelve eso y ahi la sustentacion se desarma. Para VetCare doce minutos alcanzan de sobra si se respetan las proporciones: uno y medio para el problema, tres para requisitos, dos para modelo, dos para interfaz en vivo, dos para decisiones y el resto para riesgos y cierre.

Defender una decision de diseño tiene una estructura fija que conviene memorizar: decision, alternativas consideradas, criterio de eleccion y consecuencia asumida. No basta decir que se hizo, hay que decir contra que se comparo y por que gano. Ejemplo concreto de VetCare: decidimos separar Historia_Clinica de Mascota como clases distintas; la alternativa era guardar diagnosticos y tratamientos como campos dentro de Mascota; el criterio fue que una mascota tiene muchas consultas a lo largo de su vida y una relacion uno a muchos no cabe en campos fijos; la consecuencia es que hay una entidad mas y una consulta adicional al mostrar la ficha, lo cual se acepta porque el RNF de busqueda menor a tres segundos se sostiene con un indice. Otro ejemplo: decidimos que la fecha de nacimiento sea opcional; la alternativa era hacerla obligatoria; el criterio fue que en Huellitas muchos dueños de mascotas rescatadas no la conocen y un campo obligatorio los llevaria a inventar datos; la consecuencia es que la edad se muestra como aproximada cuando el dato falta. Una decision defendida asi resiste cualquier pregunta, porque el jurado ya sabe que el equipo penso en la alternativa.

Las preguntas del jurado son bastante predecibles y por eso se preparan. Las mas frecuentes en un proyecto como VetCare son: como sabe usted que este requisito es realmente necesario; que pasa si dos recepcionistas registran la misma mascota al mismo tiempo; por que esta clase existe y no es un atributo de otra; como se cumple el requisito no funcional que usted escribio y como se mediria; que pasa si el sistema se cae a mitad de un registro; que dejaron por fuera del alcance y por que; y quien de ustedes hizo esta parte. Hay que preparar la respuesta de cada una en dos frases, sin discursos. Y hay una regla de oro para cuando no se sabe: no se inventa. La respuesta correcta es reconocer el vacio y proponer como se resolveria, por ejemplo no lo modelamos, lo registramos como riesgo abierto y se resolveria agregando una validacion de unicidad por dueño mas nombre en el diccionario de datos. Un jurado castiga mucho mas la improvisacion detectada que la honestidad tecnica.

El reparto del guion en bloques con tiempos es criterio de evaluacion, no un detalle logistico. La sustentacion es individual por defecto: el estudiante expone los cinco bloques y responde por todos, y lo que se califica es que cada bloque tenga su rango de minutos y su evidencia en pantalla, no quien lo dice. El orden que funciona para VetCare es: abrir con problema y alcance, seguir con requisitos y trazabilidad, luego los modelos UML, despues el prototipo en vivo y cerrar con decisiones, riesgos y siguiente paso hacia Programacion II. Si el docente autorizo equipo de 2 o 3, se agrega el nombre del responsable a cada bloque, todos los integrantes deben hablar al menos dos minutos y ninguno puede hablar solo de lo suyo: cada persona domina una pieza pero debe conocer el todo, porque el jurado tiene derecho a preguntarle a cualquiera sobre cualquier parte. Se ensaya cronometrado al menos dos veces, en voz alta y de pie, porque el tiempo estimado leyendo en silencio siempre es la mitad del real. Ademas se prepara el plan B tecnico: capturas del prototipo por si falla el internet, el documento en PDF descargado y los diagramas exportados a imagen. Y algo que parece obvio pero se olvida siempre: quien maneja el prototipo debe haberlo recorrido antes haciendo clic en cosas que no estaban en el guion, porque el jurado va a hacer exactamente eso.

Error tipico del docente que no domina el tema: tratar la sustentacion como un tramite y evaluarla por la calidad de las diapositivas o por la fluidez del que mas habla. Eso produce tres distorsiones. Primera, se premia a quien mejor habla aunque su diseño sea inconsistente, y se castiga al estudiante timido cuyo paquete es impecable. Segunda, al no preguntar por trazabilidad, el docente no detecta que el prototipo muestra campos que no estan en el diccionario de datos o que hay un RF que ningun diagrama cubre, que es justo lo que va a explotar en Programacion II. Tercera, al no exigir decisiones justificadas, se acepta el como sin el por que y el estudiante nunca desarrolla el criterio profesional, que es el objetivo real de la asignatura. El antidoto es tener una lista fija de preguntas de trazabilidad y hacerlas siempre: señale en el diagrama de clases donde vive el RF-04; muestre el campo de esta pantalla en el diccionario de datos; digame que alternativa descartaron aqui y con que criterio; y dirigirlas a cualquier parte del paquete, no solo a la que el estudiante acaba de exponer (si hay equipo, a un integrante distinto del que expuso esa parte).

**Demo que usted debe poder repetir:** El docente proyecta una sustentacion mal hecha y una bien hecha del mismo paquete VetCare, y luego arma en vivo la tabla de decisiones para justificar por que Historia_Clinica es una clase aparte de Mascota.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Queda armado el guion cronometrado de sustentacion de VetCare y consolidado el documento final de diseño en una sola pieza coherente. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente proyecta una sustentacion mal hecha y una bien hecha del mismo paquete VetCare, y luego arma en vivo la tabla de decisiones para justificar por que Historia_Clinica es una clase aparte de Mascota.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 14/Plantillas/Guion-y-Decisiones-Sustentacion-VetCare.md`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Paso 1. Arme en Google Docs el guion cronometrado de doce minutos con las cinco secciones obligatorias en orden problema, requisitos, modelo, interfaz y decisiones, asignando a cada bloque su rango de minutos exacto y la evidencia que se muestra en pantalla en ese bloque; ningun bloque puede quedar sin rango de minutos ni sin evidencia asociada. Si el docente autorizo equipo, escriba ademas el nombre del responsable de cada bloque y reparta de modo que ningun integrante quede con menos de dos minutos.
2. Paso 2. Llenen la tabla de tres decisiones de diseño de VetCare con las cuatro columnas decision, alternativa descartada, criterio y consecuencia asumida; una de las tres decisiones debe ser sobre el modelo de clases y otra sobre un requisito no funcional.
3. Paso 3. Construyan el banco de diez preguntas del jurado con su respuesta en maximo dos frases, incluyendo obligatoriamente que pasa si dos recepcionistas registran la misma mascota, como se mide su RNF de tiempo de respuesta y que quedo fuera del alcance.
4. Paso 4. Haga un ensayo cronometrado de pie, con el prototipo abierto, y registre el tiempo real de cada bloque; recorte lo que se paso y anote los dos puntos donde se enredo al hablar (si trabaja en equipo, donde se enredo la transicion entre un expositor y el siguiente).
5. Paso 5. Consoliden el documento final armando el indice completo desde problema hasta trazabilidad, verifiquen que los nombres de las clases, los campos del diccionario y los campos de las pantallas coinciden exactamente, y corrijan al menos una inconsistencia encontrada dejando constancia de cual era.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Un documento en Google Docs con el guion minuto a minuto repartido en bloques con tiempos y evidencia (con responsable nominal solo si el docente autorizo equipo), la tabla de tres decisiones de diseño defendidas y el banco de diez preguntas con su respuesta, mas el indice del documento final consolidado, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 14/Quiz Clase 14 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Queda armado el guion cronometrado de sustentacion de VetCare y consolidado el documento final de diseño en una sola pieza coherente.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 14/Solucion Taller Clase 14 - VetCare.docx` — no proyectar completa.
