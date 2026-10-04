# Guion docente · Clase 2 · Colecciones dinamicas · ArrayList

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** El registro de mascotas de VetCare deja de vivir en un arreglo de tamano fijo y pasa a un ArrayList<Mascota> que crece con la clinica.
- **Entregable de hoy:** Proyecto Java con las clases Mascota y RegistroMascotas y un menu de consola que agrega, lista, busca por ID y elimina mascotas, comprimido y subido a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 2 - Colecciones dinamicas ArrayList/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Las ideas de cada concepto estan proyectadas y el desarrollo completo esta en las notas del presentador de su lamina. Aqui va, por lamina y en su orden, lo que hay que subrayar.

**[Slide 4] El arreglo tiene tamaño fijo** — 3 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Empecemos por el problema real de Huellitas.

**[Slide 5] Del arreglo fijo a la lista que crece** — codigo (17 lineas). Leerlo de arriba abajo y ejecutarlo en la demo.

**[Slide 6] ArrayList por dentro: un arreglo que crece** — 3 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Esa arquitectura explica el rendimiento: get(i) es instantaneo porque salta directo a la posicion i del arreglo interno, agregar al final es barato casi siempre, pero add(0, mascota) o remove(0) obligan a correr un puesto a todos los demas elementos.

**[Slide 7] La interfaz List: add, get, size, remove** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: El <Mascota> entre los picos se llama generico y no es decoracion: le dice al compilador que ahi solo entran Mascotas, de modo que si un estudiante intenta guardar un String el error aparece al compilar y no como un ClassCastException en plena sustentacion.

**[Slide 8] agregar(): validar antes de add** — codigo (16 lineas). Leerlo de arriba abajo y ejecutarlo en la demo.

**[Slide 9] buscarPorId(): recorrer y comparar por id** — codigo (11 lineas). Leerlo de arriba abajo y ejecutarlo en la demo.

**[Slide 10] eliminarPorId(): remove(Object)** — codigo (10 lineas). Leerlo de arriba abajo y ejecutarlo en la demo.

**[Slide 11] Recorrer: índice, for-each e Iterator** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Recorrer la lista tiene dos formas y cada una tiene su momento.

**[Slide 12] listar(): el for con índice** — codigo (13 lineas). Leerlo de arriba abajo y ejecutarlo en la demo.

**[Slide 13] pasarAGeriatria(): borrar con Iterator** — codigo (10 lineas). Leerlo de arriba abajo y ejecutarlo en la demo.

**[Slide 14] La lista encapsulada en su clase** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: La ultima idea es de diseno, y es la que hace que este codigo sirva para el resto del proyecto integrador.
  - Subrayar: Eso es encapsulamiento aplicado a colecciones, y es lo que hara posible que en las proximas clases la misma clase RegistroMascotas alimente una tabla de Swing y despues se guarde en un archivo CSV sin cambiar una sola linea de la logica.

**[Slide 15] Mascota: atributos privados y toString()** — codigo (10 lineas). Leerlo de arriba abajo y ejecutarlo en la demo.

## Errores tipicos del docente que no domina el tema

Material de preparacion: no se proyecta.

- Error tipico del docente que no domina el tema: creer que new ArrayList<>(50) ya trae 50 mascotas adentro y hacer get(0) de una, lo que revienta con IndexOutOfBoundsException porque ese 50 es capacidad, no tamano; la lista recien creada tiene size() igual a cero. El segundo tropiezo es la confusion de nombres: los arreglos usan .length (sin parentesis), los String usan .length() (con parentesis) y las colecciones usan .size(); el docente escribe mascotas.length, no compila, y se queda mudo frente al grupo. El tercero es recorrer con i <= mascotas.size(), que siempre falla en la ultima vuelta porque los indices van de 0 a size()-1. Y el cuarto, el mas comun, es escribir ArrayList mascotas = new ArrayList(); sin generico, que compila con una advertencia amarilla, obliga a castear cada elemento al leerlo y termina en ClassCastException en tiempo de ejecucion. Antes de la clase, ejecute usted mismo estos cuatro errores en VS Code para reconocer el mensaje rojo en dos segundos y convertirlo en ensenanza en vez de en silencio incomodo.


**Demo que usted debe poder repetir:** El docente muestra un Mascota[3] que revienta al intentar guardar la cuarta ficha y luego el mismo caso resuelto con ArrayList, imprimiendo size() despues de cada operacion.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: El registro de mascotas de VetCare deja de vivir en un arreglo de tamano fijo y pasa a un ArrayList<Mascota> que crece con la clinica.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de concepto y en las de codigo
(lo que hay que subrayar esta tambien en las notas del presentador de cada lamina). Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente muestra un Mascota[3] que revienta al intentar guardar la cuarta ficha y luego el mismo caso resuelto con ArrayList, imprimiendo size() despues de cada operacion.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 2/Codigo/ClinicaRegistroMascotas.java`

### 60-105 · Taller guiado (opcional) = avance del PI
Opcional: no tiene lamina en el deck. La guia esta en
`Clases/Clase 2 - Colecciones dinamicas ArrayList/Taller PI - Clase 2 - VetCare.docx`; si hoy no se hace, se extiende la demo y la practica libre.
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Cree en VS Code el proyecto Java llamado VetCare con paquete clinica, y dentro de el la clase Mascota con los atributos privados id, nombre, especie, edad y dueno, su constructor completo, sus getters y el metodo toString(); verifique imprimiendo una mascota de prueba y confirmando que en consola sale el texto legible y no clinica.Mascota@1a2b3c.
2. Cree la clase RegistroMascotas con el atributo private final List<Mascota> mascotas = new ArrayList<>(); y el metodo agregar(Mascota m) que rechace un ID ya existente; verifique agregando dos veces la mascota M-001 y comprobando que la consola muestra el aviso de ID repetido y que cantidad() sigue devolviendo 1.
3. Implemente listar(), que recorra con for indexado e imprima cada ficha numerada, y buscarPorId(String id), que recorra con for-each y devuelva la Mascota o null; verifique que buscarPorId("M-003") imprime la ficha de Rocky y que buscarPorId("M-099") imprime que no existe, sin lanzar NullPointerException.
4. Implemente eliminarPorId(String id) usando remove(objeto) y el metodo pasarAGeriatria(int edadMinima) usando Iterator con it.remove(); verifique que despues de eliminar M-002 y de pasar a geriatria a las mascotas de 9 anios o mas, size() bajo exactamente en la cantidad de fichas retiradas y el programa no lanza ConcurrentModificationException.
5. Arme un menu de consola con Scanner y opciones 1-Agregar, 2-Listar, 3-Buscar por ID, 4-Eliminar, 5-Salir dentro de un ciclo while; ejecute el programa cargando las seis fichas del escenario, tome captura de la consola con el listado final y suba el proyecto comprimido mas la captura a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Proyecto Java con las clases Mascota y RegistroMascotas y un menu de consola que agrega, lista, busca por ID y elimina mascotas, comprimido y subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Si hubo taller, repasar los criterios de exito del `Taller PI - Clase 2 - VetCare.docx` (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 2/Quiz Clase 2 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: El registro de mascotas de VetCare deja de vivir en un arreglo de tamano fijo y pasa a un ArrayList<Mascota> que crece con la clinica.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 2/Solucion Taller Clase 2 - VetCare.docx` — no proyectar completa.
