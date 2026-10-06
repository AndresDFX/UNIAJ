# Guion docente · Clase 1 · Conceptos iniciales de ingenieria de software

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Avance del PI (si se hace la practica):** Dominio del proyecto acotado (trabajo individual por defecto)
- **Practica (opcional):** `Clases/Clase 1 - Conceptos iniciales/Taller PI - Clase 1 - VetCare.docx` — no esta en el deck
- **Herramienta:** Google Docs · draw.io
- **Slides:** `Clases/Clase 1 - Conceptos iniciales/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] Programar no es lo mismo que hacer ingeniería de software** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Programar es escribir codigo que funcione hoy.
  - La ingenieria de software es el conjunto de practicas que hacen que ese codigo siga funcionando cuando el sistema crece, cuando lo mantiene otra persona y cuando los requisitos cambian.
  - La diferencia no es filosofica sino economica: un error detectado al analizar requisitos cuesta corregirlo una fraccion de lo que cuesta corregirlo en produccion, cuando ya hay usuarios reales dependiendo del sistema.
  - NOTAS:
  - Esa curva de costo es la justificacion de todo lo que se vera en este curso; sin ella, las metodologias suenan a burocracia arbitraria.

**[Slide 5] Proyecto y producto** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Proyecto y producto son dos palabras que se usan como sinonimos y no lo son.
  - El producto es el software y su documentacion: lo que queda cuando todos se van.
  - El proyecto es el esfuerzo acotado en tiempo y recursos para construirlo.
  - En la clinica, el proyecto es el semestre; el producto es el sistema que la clinica usaria todos los dias.
  - NOTAS:
  - Un proyecto termina; un producto puede seguir vivo diez años.
  - Confundirlos lleva al equipo a pensar «ya entregamos, ya terminamos» y a no dejar nada escrito para quien venga despues.

**[Slide 6] Requisito funcional y no funcional** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un requisito funcional dice QUE debe hacer el sistema: «registrar una mascota con ID, nombre y especie».
  - Un requisito no funcional dice COMO debe comportarse: «la busqueda de un expediente responde en menos de dos segundos», «la informacion no se pierde ante un corte de energia».
  - Los no funcionales son los que mas se olvidan y, paradojicamente, los que mas condicionan la arquitectura.
  - La regla practica que el estudiante debe interiorizar desde hoy es: si no se puede verificar, no es un requisito, es un deseo.
  - «El sistema debe ser rapido» no sirve
  - «responde en menos de 2 s con 50 usuarios simultaneos» si, porque alguien puede sentarse a comprobarlo.

**[Slide 7] La ficha de requisito bien escrito, campo por campo** — 13 vinetas.

**[Slide 8] De frase cruda a requisito verificable** — 12 vinetas.

**[Slide 9] Los interesados y sus conflictos** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Los interesados no son solo quien paga.
  - En la clinica hay al menos tres con intereses distintos: el dueño de la clinica quiere metricas del negocio, la recepcionista quiere agendar rapido y con pocos clics, y el veterinario quiere el historial del paciente a la mano durante la consulta.
  - Esos intereses entran en conflicto: pedir mas datos da mejores metricas al dueño pero vuelve mas lento el registro para la recepcionista.
  - Resolver ese conflicto, decidiendo que se prioriza y documentando por que, es trabajo de analisis, no de programacion.

**[Slide 10] El mapa de dominio en Mermaid** — 16 vinetas.

**[Slide 11] Las mismas fases, distinto recorrido** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Todo desarrollo pasa por las mismas fases —requisitos, diseño, construccion, pruebas
  - Mantenimiento— y lo que cambia entre metodologias no son las fases sino COMO se recorren: una sola vez y en orden (cascada) o en ciclos cortos que repiten todas las fases (iterativo y agil).
  - Hoy solo se nombran; se comparan a fondo en las Clases 2, 3 y 4.
  - NOTAS:
  - Lo importante del primer dia es que el estudiante entienda su rol en esta asignatura: aqui no se construye la casa, se dibujan los planos para que cualquier equipo pueda construirla.
  - Decirlo explicitamente evita que quien esperaba programar se frustre a mitad de semestre.

**[Slide 12] Para qué documentar: depende de quién lee** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Para que sirve documentar si al final lo que se usa es el codigo: depende de quien lee.
  - El codigo lo lee la maquina y quien ya conoce el sistema; los planos los lee quien todavia no lo conoce: el companero que entra a mitad de semestre, quien revisa el diseño, el equipo de Programacion II que va a construir el sistema a partir de estos documentos
  - Y usted mismo dentro de seis semanas cuando ya no recuerde por que decidio lo que decidio.
  - Documentar no es escribir bonito ni llenar plantillas: es dejar por escrito las decisiones y su justificacion, de modo que otro pueda continuar sin volver a entrevistar al cliente.
  - NOTAS:
  - La respuesta esta en quien lee.
  - Por eso en este curso cada artefacto tiene un lector concreto, y la pregunta que se hace al calificar no es cuantas paginas tiene sino si ese lector podria trabajar con el sin preguntarle nada al autor.

**[Slide 13] El mapa del semestre** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Las primeras cuatro clases responden como se organiza el trabajo (ciclos de vida, metodologias tradicionales y agiles); de la sexta a la novena
  - Que debe hacer el sistema (requisitos, historias de usuario, UML y casos de uso); de la once a la catorce, como se ve y como se sustenta (auditoria del avance, diagramas dinamicos, interfaces y sustentacion).
  - Las clases 5, 10 y 15 son de parcial.
  - Todo lo que se produzca en el camino se acumula en un unico paquete de diseno del proyecto, que es el producto real de la asignatura; no hay trabajos sueltos que se boten al terminar la clase.
  - NOTAS:
  - El mapa del semestre cabe en una sola frase, y de el depende saber donde se esta parado en cada clase.
  - Decir esto el primer dia evita la sensacion de estar haciendo tareas desconectadas.

**[Slide 14] La deuda técnica** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Hay un concepto que explica por que este curso existe: la deuda tecnica.
  - La metafora la propuso Ward Cunningham en 1992 hablando de codigo, y funciona igual de bien para el diseno, que es lo que se hace aqui.
  - Un caso tipico que ocurre todos los semestres: el equipo no decide si una Mascota puede existir sin un Dueno registrado, porque en la primera semana parece un detalle.
  - Ahora hay que decidir, ajustar dos documentos, avisar al equipo y probablemente rehacer un wireframe.
  - El trabajo extra es el interes de una decision que costaba dos minutos en la Clase 1.
  - Como convencion practica, los equipos maduros reservan entre el diez y el veinte por ciento de cada iteracion para pagar deuda; no es una regla dura, es una forma de reconocer que la deuda no desaparece sola.
  - Y hay una deuda que nunca conviene tomar: la que se contrae por no saber que se estaba decidiendo algo.
  - NOTAS:
  - Cada vez que un equipo elige la salida rapida en lugar de la correcta, esta pidiendo prestado tiempo al futuro.
  - El prestamo puede ser razonable, igual que un credito, pero se paga con intereses, y los intereses se cobran en forma de tiempo adicional en cada cambio posterior.
  - Tres semanas despues, dos integrantes han asumido cosas distintas; uno diseno la pantalla de registro pidiendo el dueno primero y el otro escribio un caso de uso donde la mascota se registra sola y el dueno se asocia despues.

**[Slide 15] El artefacto desactualizado** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - En un curso de diseno la deuda toma una forma particular y peligrosa: el artefacto desactualizado.
  - Un diagrama que ya no corresponde a la decision vigente es peor que no tener diagrama, porque un documento que no existe obliga a preguntar, mientras que un documento equivocado convence.
  - La primera: cada artefacto lleva fecha y version visibles, de modo que cualquiera pueda saber si esta mirando lo ultimo.
  - La segunda: si una decision cambia, el artefacto se actualiza en la misma semana y el cambio queda anotado en una linea, con la fecha y el motivo
  - Ese registro es lo que en la sustentacion de la Clase 14 distingue a un equipo que diseno de un equipo que improviso y despues escribio el documento hacia atras.
  - Vale decirlo explicitamente porque contradice el habito escolar: aqui no se penaliza cambiar de opinion, se penaliza tener dos verdades circulando al mismo tiempo.
  - NOTAS:
  - Quien lo lea tomara decisiones a partir de informacion falsa y descubrira el problema tarde.
  - De ahi salen dos reglas que este curso aplica a todos los artefactos.
  - Un equipo que cambio tres veces el alcance y lo registro esta mejor evaluado que uno que entrega un documento perfecto que nadie uso.

**[Slide 16] Qué es un modelo** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El segundo concepto de fondo es la palabra modelo, que se usa todo el semestre sin definirla.
  - Un modelo es una representacion simplificada de algo real, construida para responder un conjunto acotado de preguntas.
  - La parte que sorprende al estudiante es que un modelo util es necesariamente incompleto
  - Y la razon es aritmetica y no filosofica: un modelo que incluyera todo seria del tamano del territorio que representa y por lo tanto no serviria para nada, porque un mapa a escala uno a uno pesa lo mismo que la ciudad y no cabe en el bolsillo.
  - La formula que se cita habitualmente es que el mapa no es el territorio.
  - Consecuencia operativa, y este es el criterio que el estudiante debe llevarse: para cada diagrama que va a dibujar hay que poder nombrar dos cosas, cual pregunta responde y quien es la persona que la hace.
  - Si no se pueden nombrar, el diagrama no va.
  - Esas otras preguntas tienen sus propios modelos, y el curso los introduce en las Clases 8, 9 y 12.
  - Reconocer que cada diagrama es parcial es lo que permite tener varios sin contradecirse.
  - NOTAS:
  - En la clinica, un diagrama de casos de uso responde quien hace que y con que finalidad, y le sirve al dueno de la clinica para confirmar que no falta ningun tramite; no responde en cuanto tiempo se busca un expediente ni como se guardan los datos, y quien busque eso ahi va a leer mal.

**[Slide 17] Dos maneras de que un modelo falle** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Puede omitir algo que si importaba para la pregunta que promete responder, y entonces es incompleto donde no debia.
  - O puede incluir tanto detalle que nadie lo lee, y entonces es ruido con apariencia de rigor.
  - La segunda falla es la mas comun en trabajos de curso, porque el estudiante asume que mas paginas equivalen a mas nota.
  - Sirven algunas magnitudes de referencia, todas convenciones de este curso y no reglas del lenguaje: un diagrama de casos de uso legible rara vez pasa de quince o veinte casos
  - Un diagrama con cuarenta elementos ya no se puede discutir en una reunion; una historia de usuario cabe en dos o tres lineas.
  - Y hay una prueba empirica que reemplaza cualquier lista de verificacion: entregue el artefacto a un compañero que no haya trabajado en su documento, sin explicarle nada, y pidale que lo explique en tres minutos.
  - La pregunta previsible aqui es cuantos diagramas hay que hacer entonces, y la respuesta que hay que sostener todo el semestre es que se hacen los que responden preguntas que alguien tiene, y que un diagrama sin lector es trabajo perdido aunque este perfecto.
  - NOTAS:
  - De ahi se sigue que un modelo puede estar mal de dos maneras opuestas, y conviene decirlas juntas porque los equipos suelen corregir una cayendo en la otra.
  - Lo que no pueda explicar, no comunica, y hay que arreglarlo.

**[Slide 18] Cinco rasgos de un documento usable** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Lo anterior conduce al criterio que gobierna todas las entregas de este curso: la diferencia entre un documento que alguien puede usar y uno que solo existe para la nota.
  - Son cinco rasgos y todos son verificables desde afuera.
  - Dos, es verificable: sus afirmaciones se pueden confirmar o refutar, lo que en requisitos significa criterios de aceptacion.
  - Tres, es trazable: cada requisito tiene identificador y se puede seguir hasta el artefacto donde se resuelve.
  - Cinco, es accionable: alguien puede tomar una decision o construir algo con el.
  - Version para la nota: el sistema debe ser amigable e intuitivo y permitir gestionar la informacion de las mascotas de manera eficiente.
  - Version usable: RF-012, el sistema permite registrar una mascota con identificador, nombre, especie, fecha de nacimiento y dueno asociado
  - Criterio de aceptacion, dado un dueno ya registrado, cuando la recepcionista guarda la mascota con esos cinco datos, entonces la mascota aparece en el listado de ese dueno
  - Y si el dueno no existe el registro se rechaza con un mensaje; origen, entrevista con la recepcionista; prioridad, alta.
  - Los tres rellenos que hay que prohibir desde hoy son la definicion copiada de un libro, la historia del origen de la ingenieria de software y las promesas sin sujeto del tipo se garantizara la calidad.
  - NOTAS:
  - Uno, tiene un lector nombrado y una pregunta que responde.
  - Cuatro, esta fechado y versionado.
  - Comparemos en la clinica.
  - Nadie puede construir eso ni puede decir si se cumplio.
  - La segunda version se puede programar, se puede probar y se puede discutir con el dueno de la clinica.

**[Slide 19] Trazabilidad: el hilo del semestre** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El rasgo tres merece su propio parrafo porque es el hilo que amarra el semestre: la trazabilidad.
  - Trazabilidad es poder seguir un requisito desde su origen, es decir quien lo pidio, hasta el artefacto que lo resuelve y el criterio que lo verifica.
  - En este curso la cadena es concreta y siempre la misma: un interesado dice algo en una entrevista, eso se convierte en un requisito con identificador en la Clase 6
  - Se expresa como historia de usuario en la Clase 7, aparece como caso de uso en la Clase 9, se dibuja como pantalla en la Clase 13 y se cierra con un criterio de aceptacion que permite decir si quedo hecho.
  - Dos controles simples permiten auditar esa cadena sin herramientas: todo requisito funcional debe aparecer al menos una vez en algun caso de uso, y todo caso de uso debe poder senalar el requisito que lo origina.
  - Un requisito huerfano, que no aparece en ningun sitio, es una de dos cosas: algo que nadie necesita y hay que eliminar, o un hueco de diseno que nadie noto
  - Ambas conclusiones son valiosas y ambas se pierden si el equipo escribe cada documento como si fuera independiente.
  - Esta es tambien la razon por la que en la Clase 11 se revisa el avance mirando la coherencia entre artefactos y no la cantidad de paginas.


**Demo que usted debe poder repetir:** Convertir en vivo la frase cruda «necesito buscar rapido el expediente de un animal» en un requisito funcional y uno no funcional bien escritos

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy el tema es: Conceptos iniciales de ingenieria de software. Todo lo que vamos a ver esta en las laminas.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de teoria (una por concepto)
y en las de codigo proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Convertir en vivo la frase cruda «necesito buscar rapido el expediente de un animal» en un requisito funcional y uno no funcional bien escritos
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 1/Plantillas/Ficha de dominio - VetCare.md`

### 60-105 · Practica guiada (OPCIONAL) = avance del PI
No hay laminas para esta franja: la guia es el archivo
`Clases/Clase 1 - Conceptos iniciales/Taller PI - Clase 1 - VetCare.docx` (compartirlo, no proyectarlo).
Si hoy no se hace, usar el tiempo para profundizar la teoria y la demo.
**Decir (si se hace):** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Modalidad de trabajo: individual por defecto. Abra su ficha de dominio y escriba su nombre. Si el docente autoriza equipos de 2 o 3 integrantes, la ficha puede ser compartida, pero la entrega en ExamLab siempre es individual y con sus propias palabras.
2. Escriban el problema en 2-3 frases: quien sufre que, y como se nota hoy ese dolor en la operacion diaria de la clinica.
3. Listen 3-5 capacidades del sistema, escritas como verbos de negocio (registrar, agendar, consultar), no como pantallas.
4. Identifiquen 2-3 actores y, para cada uno, que espera obtener del sistema.
5. Escriban explicitamente que NO hara el sistema este semestre (fuera de alcance): sin esa lista, el proyecto crece sin control.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Ficha de dominio: problema en 2-3 frases, 3-5 capacidades, 2-3 actores y lo que queda fuera de alcance

### 105-120 · Sintesis y cierre
Si hubo practica, repasar los criterios de exito del archivo del taller (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 1/Quiz Clase 1 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir (si hubo practica):** «Queda avanzado: Dominio del proyecto acotado (trabajo individual por defecto). Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 1/Solucion Taller Clase 1 - VetCare.docx` — no proyectar completa.
