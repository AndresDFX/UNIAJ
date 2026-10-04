# Guion docente · Clase 8 · Introduccion a UML

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Avance del PI (si se hace la practica):** Queda listo el modelo de dominio de VetCare: el diagrama de clases con Dueno, Mascota, Cita, Veterinario y Atencion.
- **Practica (opcional):** `Clases/Clase 8 - Introduccion a UML/Taller PI - Clase 8 - VetCare.docx` — no esta en el deck
- **Herramienta:** draw.io · Mermaid
- **Slides:** `Clases/Clase 8 - Introduccion a UML/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] Qué es UML** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - UML significa Lenguaje Unificado de Modelado y nacio en los anos noventa para resolver un problema muy concreto: tres personas leian la misma frase en espanol y entendian tres sistemas distintos.
  - La especificacion tiene catorce tipos de diagrama, pero en la vida real de un analista se usan cuatro o cinco de forma constante y los demas se consultan cuando se necesitan; querer aprender los catorce es la manera mas rapida de no aprender ninguno.
  - En la clinica, la frase un dueno puede tener varias mascotas parece clarisima hasta que alguien pregunta si una mascota puede tener dos duenos, si el dueno existe antes de registrar la mascota o si al borrar el dueno desaparece la mascota
  - El diagrama contesta esas tres preguntas con dos numeros y una linea, y ahi es donde UML se gana el sueldo.
  - NOTAS:
  - Es un lenguaje grafico estandarizado, no un lenguaje de programacion y no una herramienta; usted puede dibujar UML valido en draw.io, en Mermaid o en el tablero con marcador, porque lo que esta normalizado es el significado de las cajas, las lineas y los numeros, no el programa donde se pintan.

**[Slide 5] Vista estructural y vista de comportamiento** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La vista estructural muestra de que esta hecho el sistema y no cambia con el tiempo: diagrama de clases, de objetos, de componentes y de despliegue.
  - La vista de comportamiento muestra que pasa y en que orden: casos de uso, actividades, secuencia y maquina de estados.
  - Aclaracion importante: los diagramas no reemplazan el documento de requisitos, lo dibujan; cada clase que aparezca hoy debe poder rastrearse a un RF o a una historia del backlog.
  - NOTAS:
  - Los diagramas se agrupan en dos grandes vistas.
  - Un mismo sistema necesita las dos, igual que una casa necesita el plano de plantas y tambien el plano de instalaciones.
  - En la practica profesional los que sobreviven son cinco: casos de uso para acordar el alcance con el cliente, clases para el modelo del dominio, secuencia para entender un flujo complicado paso a paso, actividades para procesos de negocio con decisiones, y despliegue cuando hay que explicar donde vive cada cosa.
  - En la clinica vamos a usar clases hoy, casos de uso y secuencia mas adelante, y el resto se menciona para que sepan que existen.

**[Slide 6] La clase: tres compartimentos** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El diagrama de clases se dibuja con una caja de tres compartimentos: arriba el nombre de la clase en singular y con mayuscula inicial (Mascota, no mascotas), en el medio los atributos y abajo los metodos.
  - Un atributo se escribe con visibilidad, nombre y tipo, por ejemplo -nombre: String o -fechaNacimiento: Date, donde el guion significa privado y el mas significa publico.
  - Un metodo se escribe con su firma y su tipo de retorno, por ejemplo +calcularEdad(): int.
  - Aqui hay que distinguir dos cosas que los estudiantes mezclan: el modelo de dominio, que solo tiene los conceptos del negocio y sus datos, y el modelo de diseno, que ya incluye clases tecnicas como controladores o repositorios.
  - Hoy hacemos modelo de dominio, asi que en la clinica no aparece ninguna clase llamada MascotaDAO ni ConexionBD: aparecen Dueno, Mascota, Cita, Veterinario y Atencion, que son las cosas de las que habla el Dr. Ramirez cuando cuenta como funciona la clinica.
  - Los metodos, en el modelo de dominio, son solo los que pertenecen naturalmente al concepto, como calcularEdad en Mascota.

**[Slide 7] El diagrama de clases en Mermaid** — 19 vinetas.

**[Slide 8] Lo que NO es una clase del dominio** — 15 vinetas.

**[Slide 9] Modelo de dominio completo en Mermaid** — 31 vinetas.

**[Slide 10] Asociaciones y multiplicidades** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Las lineas entre clases son la mitad del valor del diagrama.
  - Una asociacion es una relacion estable entre dos conceptos y se dibuja con una linea recta, un nombre que se lee como frase (Dueno tiene Mascota) y
  - En cada extremo, una multiplicidad que responde cuantos: 1 exactamente uno, 0..1 opcional, 1..* uno o mas, 0..* cero o mas.
  - En la clinica, Dueno 1 --- 0..* Mascota se lee un dueno puede tener cero o mas mascotas y una mascota pertenece a exactamente un dueno; ese 1 del lado del dueno es una decision de negocio que hay que confirmar con el cliente, no una suposicion.
  - La composicion (rombo relleno) se usa cuando la parte no vive sin el todo: en la clinica las Atenciones de una Mascota son parte de su historia clinica y no tienen sentido si se elimina la ficha de la mascota.
  - La agregacion (rombo vacio) se usa cuando la parte sobrevive por su cuenta, como un Veterinario que pertenece a una Sede pero sigue existiendo si la sede cierra.
  - La herencia (triangulo) solo cuando hay un es-un verdadero, por ejemplo Persona con Dueno y Veterinario como especializaciones, decision que solo vale la pena si comparten varios atributos.
  - NOTAS:
  - Cita relaciona a Mascota y a Veterinario, cada cita con exactamente una mascota y un veterinario, y cada veterinario con muchas citas.

**[Slide 11] Del diagrama de clases a la base de datos** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El diagrama que dibujamos hoy no se queda en la clase: es la pieza que viaja mas lejos del proyecto.
  - De cada clase salen los campos del diccionario de datos y, mas adelante, las tablas de la base de datos: la clase Mascota con sus atributos se convierte en la tabla mascota, la asociacion 1 a 0..* se convierte en una llave foranea
  - Y las multiplicidades muchos a muchos se convierten en una tabla intermedia.
  - Para quien cursa tambien Programacion II, este diagrama es el mapa que le dice que clases crear y que atributos poner; para quien solo cursa Programacion II, es lo que recibe ya hecho y debe respetar
  - Y para quien solo cursa Seminario, es el corazon del documento de diseno que se entrega al final junto con el prototipo navegable, una ruta completa y perfectamente valida donde el producto profesional es el plano, no el ladrillo.
  - NOTAS:
  - Por eso el diagrama debe estar limpio: nombres en singular, sin atributos repetidos en dos clases, sin lineas sueltas y sin cajas que no correspondan a ningun requisito.


**Demo que usted debe poder repetir:** El docente dibuja en vivo Dueno, Mascota y Cita en draw.io y borra tres atributos mal ubicados explicando a que clase pertenecen de verdad.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy el tema es: Introduccion a UML. Todo lo que vamos a ver esta en las laminas.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de teoria (una por concepto)
y en las de codigo proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente dibuja en vivo Dueno, Mascota y Cita en draw.io y borra tres atributos mal ubicados explicando a que clase pertenecen de verdad.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 8/Plantillas/Diagrama-Clases-VetCare.md`

### 60-105 · Practica guiada (OPCIONAL) = avance del PI
No hay laminas para esta franja: la guia es el archivo
`Clases/Clase 8 - Introduccion a UML/Taller PI - Clase 8 - VetCare.docx` (compartirlo, no proyectarlo).
Si hoy no se hace, usar el tiempo para profundizar la teoria y la demo.
**Decir (si se hace):** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Paso 1: subraye en el catalogo de requisitos y en el backlog los sustantivos del negocio de VetCare y arme la lista de clases candidatas, descartando las que sean pantallas, reportes o cosas tecnicas.
2. Paso 2: dibuje en draw.io las cinco clases Dueno, Mascota, Cita, Veterinario y Atencion con la caja de tres compartimentos, en singular y con mayuscula inicial.
3. Paso 3: coloque minimo cuatro atributos por clase con visibilidad y tipo (por ejemplo -documento: String, -fechaNacimiento: Date) verificando que ningun atributo este repetido en dos clases distintas.
4. Paso 4: agregue al menos un metodo propio del dominio por clase (por ejemplo +calcularEdad(): int en Mascota, +reprogramar(nuevaFecha: Date) en Cita) y descarte metodos tecnicos como conectarBD o guardarEnDisco.
5. Paso 5: trace las cuatro asociaciones con nombre de relacion y multiplicidad en ambos extremos, leala cada una en voz alta como frase completa, exporte a PNG y .drawio y suba ambos archivos a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Diagrama de clases de VetCare hecho en draw.io, exportado a PNG y al archivo .drawio, con 5 clases, atributos tipados, metodos propios y 4 asociaciones con multiplicidad y nombre de rol, subido a ExamLab.

### 105-120 · Sintesis y cierre
Si hubo practica, repasar los criterios de exito del archivo del taller (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 8/Quiz Clase 8 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir (si hubo practica):** «Queda avanzado: Queda listo el modelo de dominio de VetCare: el diagrama de clases con Dueno, Mascota, Cita, Veterinario y Atencion.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 8/Solucion Taller Clase 8 - VetCare.docx` — no proyectar completa.
