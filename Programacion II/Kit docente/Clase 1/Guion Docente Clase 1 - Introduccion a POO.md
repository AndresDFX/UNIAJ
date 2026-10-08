# Guion docente · Clase 1 · Introduccion a la Programacion Orientada a Objetos

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** Entorno de desarrollo listo y la primera clase del dominio VetCare escrita
- **Entregable de hoy:** Proyecto Java con la clase Mascota (atributos privados, constructor y toString) y un main que crea dos objetos distintos
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 1 - Introduccion a POO/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Las ideas de cada concepto estan proyectadas y el desarrollo completo esta en las notas del presentador de su lamina. Aqui va, por lamina y en su orden, lo que hay que subrayar.

**[Slide 4] Del programa estructurado al objeto** — 3 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Vale la pena hacer visible el limite de ese enfoque con el mismo dominio del proyecto antes de nombrar la palabra objeto.
  - Subrayar: Eso funciona en un ejercicio de veinte lineas y se cae en cuanto el programa crece, por tres razones concretas.
  - Subrayar: Ordenar la lista por nombre obliga a mover los tres arreglos en perfecta sincronia, y basta olvidar uno para que Luna quede con la edad de otro animal.
  - Subrayar: Antes de la POO un programa era una lista de procedimientos que operaban sobre datos sueltos.
  - Subrayar: Cuando el programa crecia, nadie sabia que funcion tocaba que dato, y un cambio pequeno rompia cosas en lugares inesperados.
  - Subrayar: El programa deja de ser una receta y pasa a ser un conjunto de piezas que se hablan entre si.

**[Slide 5] Clase y objeto: el molde y la pieza** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Recien ahora tiene sentido la analogia clasica.
  - Subrayar: La analogia es util pero tiene tres limites que hay que decir en voz alta, porque el estudiante que se queda solo con la analogia la estira mal.

**[Slide 6] Crear objetos con new** — programa completo (33 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 7] El objeto en memoria: pila y montón** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: En Java una variable local vive en la pila, una zona pequena y ordenada asociada al metodo que se esta ejecutando, mientras que el objeto creado con new vive en el monton, una zona grande donde el programa reserva espacio a medida que lo necesita.
  - Subrayar: Escrito en el tablero: Mascota a =; despues Mascota b = a; despues b.setEdad(4); y finalmente imprime 4, aunque nadie toco la variable a.
  - Subrayar: No hay dos mascotas, hay una con dos nombres.
  - Subrayar: De aqui se deriva un tercer hecho que conviene decir hoy aunque se practique despues: cuando se pasa un objeto a un metodo, el metodo puede modificar el objeto y quien llamo vera el cambio, pero si el metodo reasigna su parametro con un new, la variable de afuera no se enteran de nada.

**[Slide 8] == compara referencias; equals, contenido** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: La respuesta es exacta y hay que darla asi: el operador == compara referencias, es decir pregunta si las dos variables apuntan al mismo objeto, no si los objetos se parecen.
  - Subrayar: Sobrescribirlo significa escribirlo en Mascota para que dos mascotas sean iguales cuando su identificador sea igual.
  - Subrayar: Por eso la regla practica del curso es sin excepciones: con objetos nunca se usa ==, se usa equals; == se reserva para primitivos y para preguntar si algo es null.

**[Slide 9] Abstracción y encapsulamiento** — 3 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Los cuatro pilares se entienden por el problema que resuelve cada uno.

**[Slide 10] Encapsular es proteger una regla** — 3 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: El encapsulamiento se ensena mal cuando se presenta como la orden de poner private y generar getters.
  - Subrayar: Se ensena bien cuando se muestra el problema que resuelve, y en VetCare el problema tiene nombre.
  - Subrayar: La respuesta concreta es que funciona hoy, con un archivo y con usted como unico autor; en la Clase 12, integrando modulos de tres companeros, quien escriba la pantalla de facturacion pondra activa en false por comodidad y usted perdera una tarde buscando por que las citas desaparecieron.

**[Slide 11] setEdad(): el objeto se defiende** — programa completo (35 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 12] Herencia y polimorfismo** — 3 ideas proyectadas; el desarrollo, en las notas del presentador.

**[Slide 13] El constructor: el objeto nace válido** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Eso elimina una familia entera de errores aguas abajo, porque nadie tendra que preguntarse mas adelante si el nombre podria estar vacio.
  - Subrayar: La instruccion reserva memoria y llama al constructor.
  - Subrayar: Por eso desde la primera clase se escribe el constructor completo.

**[Slide 14] Atributos privados y constructor** — programa completo (29 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 15] null y NullPointerException** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Queda el error mas frecuente de Java, y hay que nombrarlo hoy porque su causa es todo lo anterior. null significa que la referencia no apunta a ningun objeto: es un control remoto sin televisor.
  - Subrayar: Las encuestas y los reportes de errores en produccion la ubican de forma consistente como la excepcion mas frecuente en aplicaciones Java, y conviene presentarlo asi, como observacion de la industria y no como ley.

**[Slide 16] El entorno: JDK, javac y java** — 3 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: El entorno cierra la clase y tiene dos reglas duras que producen el noventa por ciento de los tropiezos del primer dia.
  - Subrayar: El amarre con la Clase 2 conviene decirlo explicito al cerrar: hoy quedaron mascota1, mascota2 y mascota3 como variables sueltas, y eso no escala a una clinica con cuatrocientos pacientes, asi que la proxima clase entra ArrayList de Mascota.

## Errores tipicos del docente que no domina el tema

Material de preparacion: no se proyecta.

- Error tipico del docente que no domina el tema: presentar los cuatro pilares como cuatro definiciones que hay que memorizar. El estudiante los aprende cuando ve el problema que cada uno resuelve, no cuando los recita; por eso hoy solo se introducen con un ejemplo concreto de VetCare y se profundizan en las clases siguientes. El segundo tropiezo es olvidar sobreescribir toString(): al imprimir un objeto sale algo como clinica.Mascota@6d06d69c y medio grupo cree que el programa fallo.
- Error tipico del docente que no domina el tema: el primero es explicar el objeto como una variable que agrupa datos y dibujarlo en el tablero dentro de la variable, sin la flecha de la referencia. Es comodo y parece suficiente el primer dia, pero deja al grupo sin modelo mental: cuando en la Clase 2 dos posiciones de la lista apunten al mismo objeto, o cuando un metodo modifique la mascota que recibio, el estudiante no podra explicar por que cambio algo que el no toco, y atribuira al azar o a un supuesto error de Java lo que en la Clase 12 se convertira en errores de estado compartido durante la integracion. El segundo es presentar el encapsulamiento como el procedimiento de poner private y pedirle al entorno que genere getters y setters. El estudiante entrega entonces clases con quince setters publicos, cero validaciones y ninguna operacion del dominio, con lo cual la regla de que una mascota inactiva no agenda cita queda escrita a mano en cada pantalla; en la revision cruzada de la Clase 11 apareceran tres versiones distintas de la misma regla y ninguna sera la oficial.


**Demo que usted debe poder repetir:** Escribir en vivo la clase Mascota y un main que instancia dos mascotas con datos distintos, mostrando que salen del mismo molde

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Entorno de desarrollo listo y la primera clase del dominio VetCare escrita. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de concepto y en las de codigo
(lo que hay que subrayar esta tambien en las notas del presentador de cada lamina). Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Escribir en vivo la clase Mascota y un main que instancia dos mascotas con datos distintos, mostrando que salen del mismo molde
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 1/Codigo/Mascota.java`

### 60-105 · Taller guiado (opcional) = avance del PI
Opcional: no tiene lamina en el deck. La guia esta en
`Clases/Clase 1 - Introduccion a POO/Taller PI - Clase 1 - VetCare.docx`; si hoy no se hace, se extiende la demo y la practica libre.
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Instale y verifique el entorno (JDK 17+ y VS Code con el Extension Pack for Java) y cree un proyecto Java llamado VetCare con paquete clinica. Este paso es el objetivo real del bloque: nadie puede quedarse sin entorno funcionando.
2. Escriba la clase Mascota con al menos tres atributos privados (id, nombre, especie) y un constructor que los reciba todos.
3. Agregue al menos un getter y sobreescriba toString() para que la mascota se imprima de forma legible.
4. En el main, cree DOS objetos Mascota con datos distintos e imprimalos: debe verse que salen del mismo molde pero con valores diferentes.
5. Si termina antes: agregue un setter que valide (por ejemplo, que rechace una edad negativa) y pruebelo desde el main.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Proyecto Java con la clase Mascota (atributos privados, constructor y toString) y un main que crea dos objetos distintos

### 105-120 · Criterios de exito y cierre
Si hubo taller, repasar los criterios de exito del `Taller PI - Clase 1 - VetCare.docx` (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 1/Quiz Clase 1 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Entorno de desarrollo listo y la primera clase del dominio VetCare escrita. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 1/Solucion Taller Clase 1 - VetCare.docx` — no proyectar completa.
