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

**Programar es escribir codigo que funcione hoy** — 3 vinetas.
  - Esa curva de costo es la justificacion de todo lo que se vera en este curso; sin ella, las metodologias suenan a burocracia arbitraria.

**Proyecto y producto son dos palabras que se usan como sinonimos y no lo...** — 4 vinetas.
  - Un proyecto termina; un producto puede seguir vivo diez años.
  - Confundirlos lleva al equipo a pensar «ya entregamos, ya terminamos» y a no dejar nada escrito para quien venga despues.

**Un requisito funcional dice QUE debe hacer el sistema: «registrar una...** — 6 vinetas.

**Los interesados no son solo quien paga** — 4 vinetas.

**Todo desarrollo pasa por las mismas fases —requisitos, diseño...** — 3 vinetas.
  - Lo importante del primer dia es que el estudiante entienda su rol en esta asignatura: aqui no se construye la casa, se dibujan los planos para que cualquier equipo pueda construirla.
  - Decirlo explicitamente evita que quien esperaba programar se frustre a mitad de semestre.

**Para que sirve documentar si al final lo que se usa es el codigo:...** — 4 vinetas.
  - La respuesta esta en quien lee.
  - Por eso en este curso cada artefacto tiene un lector concreto, y la pregunta que se hace al calificar no es cuantas paginas tiene sino si ese lector podria trabajar con el sin preguntarle nada al autor.

**El mapa del semestre cabe en una sola frase, y de el depende saber...** — 4 vinetas.
  - El mapa del semestre cabe en una sola frase, y de el depende saber donde se esta parado en cada clase.
  - Decir esto el primer dia evita la sensacion de estar haciendo tareas desconectadas.

**Hay un concepto que explica por que este curso existe: la deuda tecnica (1/2)** — 4 vinetas.
  - Cada vez que un equipo elige la salida rapida en lugar de la correcta, esta pidiendo prestado tiempo al futuro.
  - El prestamo puede ser razonable, igual que un credito, pero se paga con intereses, y los intereses se cobran en forma de tiempo adicional en cada cambio posterior.
  - Tres semanas despues, dos integrantes han asumido cosas distintas; uno diseno la pantalla de registro pidiendo el dueno primero y el otro escribio un caso de uso donde la mascota se registra sola y el dueno se asocia despues.

**Hay un concepto que explica por que este curso existe: la deuda tecnica (2/2)** — 3 vinetas.

**En un curso de diseno la deuda toma una forma particular y peligrosa:... (1/2)** — 4 vinetas.
  - Quien lo lea tomara decisiones a partir de informacion falsa y descubrira el problema tarde.
  - De ahi salen dos reglas que este curso aplica a todos los artefactos.
  - Un equipo que cambio tres veces el alcance y lo registro esta mejor evaluado que uno que entrega un documento perfecto que nadie uso.

**En un curso de diseno la deuda toma una forma particular y peligrosa:... (2/2)** — 2 vinetas.

**El segundo concepto de fondo es la palabra modelo, que se usa todo el... (1/2)** — 4 vinetas.
  - En la clinica, un diagrama de casos de uso responde quien hace que y con que finalidad, y le sirve al dueno de la clinica para confirmar que no falta ningun tramite; no responde en cuanto tiempo se busca un expediente ni como se guardan los datos, y quien busque eso ahi va a leer mal.

**El segundo concepto de fondo es la palabra modelo, que se usa todo el... (2/2)** — 5 vinetas.

**De ahi se sigue que un modelo puede estar mal de dos maneras opuestas... (1/2)** — 5 vinetas.
  - De ahi se sigue que un modelo puede estar mal de dos maneras opuestas, y conviene decirlas juntas porque los equipos suelen corregir una cayendo en la otra.
  - Lo que no pueda explicar, no comunica, y hay que arreglarlo.

**De ahi se sigue que un modelo puede estar mal de dos maneras opuestas... (2/2)** — 2 vinetas.

**Lo anterior conduce al criterio que gobierna todas las entregas de este... (1/2)** — 6 vinetas.
  - Uno, tiene un lector nombrado y una pregunta que responde.
  - Cuatro, esta fechado y versionado.
  - Comparemos en la clinica.
  - Nadie puede construir eso ni puede decir si se cumplio.
  - La segunda version se puede programar, se puede probar y se puede discutir con el dueno de la clinica.

**Lo anterior conduce al criterio que gobierna todas las entregas de este... (2/2)** — 4 vinetas.

**El rasgo tres merece su propio parrafo porque es el hilo que amarra el... (1/2)** — 5 vinetas.

**El rasgo tres merece su propio parrafo porque es el hilo que amarra el... (2/2)** — 3 vinetas.

**El mapa de dominio en Mermaid: la sintaxis** — 18 vinetas.

**La ficha de requisito bien escrito, campo por campo** — 13 vinetas.


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
