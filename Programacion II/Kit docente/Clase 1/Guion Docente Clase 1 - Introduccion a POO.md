# Guion docente · Clase 1 · Introduccion a la POO

- **Curso:** Programacion II (FI303204) · 120 min
- **Tipo:** REGULAR · **presencial** (Clase 1 siempre es presencial)
- **Dia 1:** este bloque comparte espacio con la **Sesion 0** (Presentacion del Curso,
  archivo aparte). Sesion 0 = logistica y encuadre; esta Clase 1 = diagnostico + primer tema.
- **Entregable de hoy:** entorno de desarrollo funcionando + primera clase Java escrita
- **Slides:** `Clases/Clase 1 - Introduccion a POO/Presentacion.pptx`

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo:
> todo eso ya se cubrio en la Sesion 0.

## Fundamento teorico para el docente

**Que es la Programacion Orientada a Objetos y por que existe.** Antes de la POO, un
programa era una lista de procedimientos que operaban sobre datos sueltos. Cuando el
programa crecia, nadie sabia que funcion tocaba que dato, y un cambio pequeño rompia
cosas en lugares inesperados. La POO propone lo contrario: juntar en una sola unidad
—el objeto— los datos y las operaciones que los manipulan. El programa deja de ser
"una receta" y pasa a ser "un conjunto de piezas que se hablan entre si".

**Clase vs objeto (la distincion que mas cuesta el primer dia).** La clase es el
molde; el objeto es la pieza fabricada con ese molde. `Mascota` es la clase: define
que toda mascota tiene nombre, especie y edad. `luna` es un objeto: una mascota
concreta, con nombre "Luna", especie "Canino", edad 3. De una misma clase se crean
tantos objetos como haga falta, cada uno con sus propios valores. Analogia util en
clase: el plano de una casa (clase) frente a las casas construidas con ese plano
(objetos) — cada casa puede estar pintada de distinto color, pero todas tienen la
misma estructura.

**Los cuatro pilares, en una frase cada uno:**

- **Abstraccion:** quedarse solo con lo que importa del problema. Para una clinica
  veterinaria, de una mascota importa su especie y su historial; no importa su color
  favorito. Modelar es decidir que se ignora.
- **Encapsulamiento:** los datos de un objeto no se tocan directamente desde afuera;
  se accede a traves de metodos. El atributo va `private` y se expone con getters y
  setters. Asi el objeto puede validar (ej.: rechazar una edad negativa) en vez de
  quedar a merced de quien lo use.
- **Herencia:** una clase puede extender a otra y reutilizar lo que ya define.
  `Perro extends Mascota` hereda nombre y edad, y agrega lo suyo (raza). Advertencia
  para el docente: la herencia se sobreusa; solo aplica cuando de verdad hay una
  relacion "es un" (un perro ES una mascota). Si la relacion es "tiene un", no es
  herencia, es composicion.
- **Polimorfismo:** el mismo mensaje produce comportamientos distintos segun el objeto
  que lo recibe. Si `Perro` y `Gato` heredan de `Mascota` y ambos redefinen
  `hacerSonido()`, recorrer una lista de mascotas y llamar ese metodo produce "Guau"
  o "Miau" segun el objeto real. El codigo que recorre la lista no necesita saber de
  que tipo es cada una.

**Error tipico del docente que no domina el tema:** presentar los cuatro pilares como
cuatro definiciones que hay que memorizar. El estudiante los aprende de verdad cuando
ve el problema que cada uno resuelve. Por eso hoy solo se introducen con un ejemplo
concreto; se profundizan en las clases siguientes.

**Constructor y `new`:** el constructor es el metodo que se ejecuta al crear el
objeto y deja sus atributos en un estado valido. `new Mascota("Luna", "Canino", 3)`
reserva memoria y llama al constructor. Si no se escribe ninguno, Java agrega uno
vacio por defecto — y ahi es donde aparecen objetos a medio inicializar.

**Sobre el diagnostico de hoy:** no es una nota. Sirve para saber con que llega el
grupo (si recuerdan Java basico, si distinguen tipos primitivos, si han visto clases
antes). El resultado condiciona el ritmo de las Clases 2 y 3, asi que conviene
revisarlo el mismo dia y registrar el consolidado en `Entregas docente/`.

## Plan minuto a minuto (120 min)

### 0-15 · Enlace con la Sesion 0 y encuadre del tema
**Decir:** «Acabamos de ver como funciona el curso. Ahora empezamos el primer tema:
programacion orientada a objetos. Hoy no van a memorizar definiciones; van a escribir
su primera clase Java y a dejar el entorno listo.»
Aclarar que la Sesion 0 y esta clase son el mismo bloque pero cosas distintas.

### 15-35 · Prueba diagnostica
Aplicar `Kit docente/Clase 1/Prueba Diagnostica…`. Individual, sin nota.
**Decir:** «Esto no se califica. Me sirve para saber a que ritmo vamos.»
Mientras responden, pasar asistencia.

### 35-70 · Teoria Core: clase, objeto y los cuatro pilares
Recorrer las diapositivas 5 y 6 apoyandose en el fundamento de arriba.
Orden sugerido: (1) el problema que resuelve la POO, (2) clase vs objeto con la
analogia del plano y las casas, (3) los cuatro pilares con UN ejemplo del dominio
veterinario cada uno.
Pregunta al aire (2 min): «Si `Mascota` es la clase, ¿que seria un objeto?»
Escribir en el tablero la clase `Mascota` con tres atributos y un constructor.

### 70-85 · Mini-demo en codigo
Proyectar el editor y escribir en vivo, sin copiar-pegar:
- la clase `Mascota` con atributos `private`,
- su constructor,
- un getter,
- un `main` que crea dos objetos distintos y los imprime.
**Decir:** «Fijense que las dos mascotas salen del mismo molde pero tienen datos
distintos. Eso es clase contra objeto.»

### 85-110 · Laboratorio: entorno listo + primera clase propia
Cada estudiante deja funcionando su entorno (JDK + NetBeans o el IDE del curso) y
escribe su propia clase con al menos dos atributos y un constructor.
Circular por los puestos: el objetivo real de este bloque es que **nadie se quede sin
entorno**, porque arrastrar eso a la Clase 2 bloquea todo el curso.
Quien termine antes: agregar un segundo objeto y un metodo que imprima sus datos.

### 110-120 · Cierre y primer contacto con el Proyecto Integrador
**Decir:** «Todo el semestre trabajamos un mismo producto: VetCare, el sistema de la
clinica veterinaria Huellitas. Lo que escribieron hoy es la semilla de ese sistema.»
Señalar donde vive el enunciado (`Clases/Proyecto Integrador/`) y recordar que quien
tambien cursa Seminario de Sistemas hara alla los planos del MISMO producto.

## Cierre docente (despues de clase)

- Revisar el diagnostico y anotar el consolidado en `Entregas docente/<periodo>/DIAGNOSTICO…`.
- Anotar quien quedo sin entorno funcionando: son los que hay que atender en la Clase 2.
