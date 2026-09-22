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

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Antes de la POO un programa era una lista de procedimientos que...** — 2 vinetas.
  - Antes de la POO un programa era una lista de procedimientos que operaban sobre datos sueltos.
  - Cuando el programa crecia, nadie sabia que funcion tocaba que dato, y un cambio pequeno rompia cosas en lugares inesperados.
  - El programa deja de ser una receta y pasa a ser un conjunto de piezas que se hablan entre si.

**La distincion que mas cuesta el primer dia es clase contra objeto** — 6 vinetas.

**Los cuatro pilares se entienden por el problema que resuelve cada uno** — 3 vinetas.
  - Los cuatro pilares se entienden por el problema que resuelve cada uno.

**Herencia es que una clase puede extender a otra y reutilizar lo que ya...** — 4 vinetas.

**El constructor es el metodo que se ejecuta al crear el objeto y deja...** — 2 vinetas.
  - La instruccion reserva memoria y llama al constructor.
  - Por eso desde la primera clase se escribe el constructor completo.

**El constructor es el metodo que se ejecuta al... — sintaxis** — 1 vinetas.

**En Programacion I el estudiante trabajo con programacion estructurada:... (1/2)** — 4 vinetas.
  - Vale la pena hacer visible el limite de ese enfoque con el mismo dominio del proyecto antes de nombrar la palabra objeto.
  - Eso funciona en un ejercicio de veinte lineas y se cae en cuanto el programa crece, por tres razones concretas.
  - Ordenar la lista por nombre obliga a mover los tres arreglos en perfecta sincronia, y basta olvidar uno para que Luna quede con la edad de otro animal.

**En Programacion I el estudiante trabajo con programacion estructurada:... (2/2)** — 2 vinetas.

**Ahora el punto que decide el semestre, y por eso va temprano: que es un... (1/2)** — 5 vinetas.
  - En Java una variable local vive en la pila, una zona pequena y ordenada asociada al metodo que se esta ejecutando, mientras que el objeto creado con new vive en el monton, una zona grande donde el programa reserva espacio a medida que lo necesita.
  - No hay dos mascotas, hay una con dos nombres.

**Ahora el punto que decide el semestre, y por eso va temprano: que es un... (2/2)** — 3 vinetas.

**Ahora el punto que decide el semestre, y por... — sintaxis** — 3 vinetas.

**De lo anterior sale la pregunta que aparece sin falta en las primeras... (1/2)** — 3 vinetas.
  - La respuesta es exacta y hay que darla asi: el operador == compara referencias, es decir pregunta si las dos variables apuntan al mismo objeto, no si los objetos se parecen.
  - Sobrescribirlo significa escribirlo en Mascota para que dos mascotas sean iguales cuando su identificador sea igual.
  - Por eso la regla practica del curso es sin excepciones: con objetos nunca se usa ==, se usa equals; == se reserva para primitivos y para preguntar si algo es null.

**De lo anterior sale la pregunta que aparece sin falta en las primeras... (2/2)** — 3 vinetas.

**Recien ahora tiene sentido la analogia clasica (1/2)** — 6 vinetas.
  - Recien ahora tiene sentido la analogia clasica.

**Recien ahora tiene sentido la analogia clasica (2/2)** — 4 vinetas.

**El encapsulamiento se ensena mal cuando se presenta como la orden de... (1/2)** — 6 vinetas.
  - El encapsulamiento se ensena mal cuando se presenta como la orden de poner private y generar getters.
  - Se ensena bien cuando se muestra el problema que resuelve, y en VetCare el problema tiene nombre.
  - La respuesta concreta es que funciona hoy, con un archivo y con usted como unico autor; en la Clase 12, integrando modulos de tres companeros, quien escriba la pantalla de facturacion pondra activa en false por comodidad y usted perdera una tarde buscando por que las citas desaparecieron.

**El encapsulamiento se ensena mal cuando se presenta como la orden de... (2/2)** — 5 vinetas.

**El constructor es la pieza que garantiza que el objeto nazca valido (1/2)** — 6 vinetas.
  - Eso elimina una familia entera de errores aguas abajo, porque nadie tendra que preguntarse mas adelante si el nombre podria estar vacio.

**El constructor es la pieza que garantiza que el objeto nazca valido (2/2)** — 3 vinetas.

**Queda el error mas frecuente de Java, y hay que nombrarlo hoy porque su... (1/2)** — 5 vinetas.
  - Las encuestas y los reportes de errores en produccion la ubican de forma consistente como la excepcion mas frecuente en aplicaciones Java, y conviene presentarlo asi, como observacion de la industria y no como ley.

**Queda el error mas frecuente de Java, y hay que nombrarlo hoy porque su... (2/2)** — 5 vinetas.

**El entorno cierra la clase y tiene dos reglas duras que producen el... (1/2)** — 4 vinetas.
  - El entorno cierra la clase y tiene dos reglas duras que producen el noventa por ciento de los tropiezos del primer dia.

**El entorno cierra la clase y tiene dos reglas duras que producen el... (2/2)** — 4 vinetas.

**Mascota.java — class Mascota** — 7 vinetas.

**Mascota.java — Mascota()** — 13 vinetas.

**Mascota.java — setEdad()** — 9 vinetas.

**Mascota.java — main()** — 10 vinetas.


**Demo que usted debe poder repetir:** Escribir en vivo la clase Mascota y un main que instancia dos mascotas con datos distintos, mostrando que salen del mismo molde

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Entorno de desarrollo listo y la primera clase del dominio VetCare escrita. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Escribir en vivo la clase Mascota y un main que instancia dos mascotas con datos distintos, mostrando que salen del mismo molde
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 1/Codigo/Mascota.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Instale y verifique el entorno (JDK 17+ y VS Code con el Extension Pack for Java) y cree un proyecto Java llamado VetCare con paquete vetcare. Este paso es el objetivo real del bloque: nadie puede quedarse sin entorno funcionando.
2. Escriba la clase Mascota con al menos tres atributos privados (id, nombre, especie) y un constructor que los reciba todos.
3. Agregue al menos un getter y sobreescriba toString() para que la mascota se imprima de forma legible.
4. En el main, cree DOS objetos Mascota con datos distintos e imprimalos: debe verse que salen del mismo molde pero con valores diferentes.
5. Si termina antes: agregue un setter que valide (por ejemplo, que rechace una edad negativa) y pruebelo desde el main.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Proyecto Java con la clase Mascota (atributos privados, constructor y toString) y un main que crea dos objetos distintos

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 1/Quiz Clase 1 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Entorno de desarrollo listo y la primera clase del dominio VetCare escrita. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 1/Solucion Taller Clase 1 - VetCare.docx` — no proyectar completa.
