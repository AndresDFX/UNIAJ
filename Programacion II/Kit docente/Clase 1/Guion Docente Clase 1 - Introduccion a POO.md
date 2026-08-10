# Guion docente · Clase 1 · Introduccion a la Programacion Orientada a Objetos

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** Entorno de desarrollo listo y la primera clase del dominio VetCare escrita
- **Entregable de hoy:** Proyecto NetBeans con la clase Mascota (atributos privados, constructor y toString) y un main que crea dos objetos distintos
- **Herramienta:** Apache NetBeans
- **Slides:** `Clases/Clase 1 - Introduccion a POO/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Antes de la POO un programa era una lista de procedimientos que operaban sobre datos sueltos. Cuando el programa crecia, nadie sabia que funcion tocaba que dato, y un cambio pequeno rompia cosas en lugares inesperados. La POO propone lo contrario: juntar en una sola unidad, el objeto, los datos y las operaciones que los manipulan. El programa deja de ser una receta y pasa a ser un conjunto de piezas que se hablan entre si. En VetCare, en vez de tener por un lado un arreglo de nombres y por otro un arreglo de edades que hay que mantener sincronizados a mano, se tiene una clase Mascota que guarda juntos su nombre, su especie y su edad.

La distincion que mas cuesta el primer dia es clase contra objeto. La clase es el molde; el objeto es la pieza fabricada con ese molde. Mascota es la clase: define que toda mascota tiene nombre, especie y edad. La variable luna es un objeto: una mascota concreta, con nombre Luna, especie Canino, edad 3. De una misma clase se crean tantos objetos como haga falta, cada uno con sus propios valores. La analogia que funciona en clase es el plano de una casa (la clase) frente a las casas construidas con ese plano (los objetos): cada casa puede estar pintada de distinto color, pero todas tienen la misma estructura.

Los cuatro pilares se entienden por el problema que resuelve cada uno. Abstraccion es quedarse solo con lo que importa del problema: para la clinica Huellitas, de una mascota importa su especie y su historial, no su color favorito; modelar es decidir que se ignora. Encapsulamiento es que los datos de un objeto no se tocan directamente desde afuera sino a traves de metodos: el atributo va private y se expone con getters y setters, de modo que el objeto pueda validar (por ejemplo, rechazar una edad negativa) en vez de quedar a merced de quien lo use.

Herencia es que una clase puede extender a otra y reutilizar lo que ya define: Perro extends Mascota hereda nombre y edad, y agrega lo suyo. Advertencia importante: la herencia se sobreusa, y solo aplica cuando de verdad hay una relacion 'es un' (un perro ES una mascota); si la relacion es 'tiene un', no es herencia sino composicion. Polimorfismo es que el mismo mensaje produce comportamientos distintos segun el objeto que lo recibe: si Perro y Gato heredan de Mascota y ambos redefinen hacerSonido(), recorrer una lista de mascotas y llamar ese metodo produce Guau o Miau segun el objeto real, sin que el codigo que recorre la lista necesite saber de que tipo es cada una.

El constructor es el metodo que se ejecuta al crear el objeto y deja sus atributos en un estado valido. La instruccion new Mascota("Luna", "Canino", 3) reserva memoria y llama al constructor. Si no se escribe ninguno, Java agrega uno vacio por defecto, y ahi es donde aparecen objetos a medio inicializar que despues fallan con NullPointerException en el peor momento. Por eso desde la primera clase se escribe el constructor completo.

Error tipico del docente que no domina el tema: presentar los cuatro pilares como cuatro definiciones que hay que memorizar. El estudiante los aprende cuando ve el problema que cada uno resuelve, no cuando los recita; por eso hoy solo se introducen con un ejemplo concreto de VetCare y se profundizan en las clases siguientes. El segundo tropiezo es olvidar sobreescribir toString(): al imprimir un objeto sale algo como vetcare.Mascota@6d06d69c y medio grupo cree que el programa fallo.

**Demo que usted debe poder repetir:** Escribir en vivo la clase Mascota y un main que instancia dos mascotas con datos distintos, mostrando que salen del mismo molde

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Entorno de desarrollo listo y la primera clase del dominio VetCare escrita. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en el VetCare de su equipo?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Escribir en vivo la clase Mascota y un main que instancia dos mascotas con datos distintos, mostrando que salen del mismo molde
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 1/Codigo/Mascota.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Equipos: abran su proyecto VetCare. Esto suma a la rubrica del PI.»
Actividades:
1. Instale y verifique el entorno (JDK + Apache NetBeans) y cree un proyecto Java Application llamado VetCare con paquete vetcare. Este paso es el objetivo real del bloque: nadie puede quedarse sin entorno funcionando.
2. Escriba la clase Mascota con al menos tres atributos privados (id, nombre, especie) y un constructor que los reciba todos.
3. Agregue al menos un getter y sobreescriba toString() para que la mascota se imprima de forma legible.
4. En el main, cree DOS objetos Mascota con datos distintos e imprimalos: debe verse que salen del mismo molde pero con valores diferentes.
5. Si termina antes: agregue un setter que valide (por ejemplo, que rechace una edad negativa) y pruebelo desde el main.
Circular por los equipos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Proyecto NetBeans con la clase Mascota (atributos privados, constructor y toString) y un main que crea dos objetos distintos

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 1/Quiz Clase 1 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Entorno de desarrollo listo y la primera clase del dominio VetCare escrita. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 1/Solucion Taller Clase 1 - VetCare.docx` — no proyectar completa.
