# Guion docente · Clase 2 · Colecciones dinamicas · ArrayList

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** El registro de mascotas de VetCare deja de vivir en un arreglo de tamano fijo y pasa a un ArrayList<Mascota> que crece con la clinica.
- **Entregable de hoy:** Proyecto NetBeans con las clases Mascota y RegistroMascotas y un menu de consola que agrega, lista, busca por ID y elimina mascotas, comprimido y subido a ExamLab.
- **Herramienta:** Apache NetBeans
- **Slides:** `Clases/Clase 2 - Colecciones dinamicas ArrayList/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Empecemos por el problema real de Huellitas. Hoy la clinica guarda las fichas de las mascotas en una carpeta de carton con 50 separadores; cuando llega la mascota 51 toca comprar otra carpeta y volver a organizar todo. En Java eso mismo es un arreglo: cuando usted escribe Mascota[] fichero = new Mascota[50] esta pidiendole a la maquina un bloque de memoria contiguo con exactamente 50 casillas, y ese numero queda grabado en piedra para toda la vida del objeto. El arreglo no tiene metodo para crecer, solo tiene el atributo length, que es de solo lectura; si quiere 80 casillas debe crear otro arreglo mas grande, copiar una por una las 50 fichas viejas y reasignar la variable. Un arreglo es rapidisimo y perfectamente valido cuando usted sabe de antemano cuantos elementos va a tener (los 7 dias de la semana, los 12 meses), pero es una pesima idea para algo que crece todos los dias, como el numero de pacientes de una veterinaria que apenas esta digitalizando su operacion.

Un ArrayList es exactamente esa carpeta que se agranda sola, y aqui viene lo importante: por dentro tambien es un arreglo. La clase ArrayList guarda un arreglo interno oculto (llamado elementData) y lleva dos numeros distintos: la capacidad, que es cuantas casillas tiene el arreglo interno, y el tamano, que es cuantos elementos usted realmente guardo. Cuando usted hace add y el arreglo interno se llena, ArrayList crea silenciosamente uno nuevo aproximadamente 1.5 veces mas grande, copia todo con Arrays.copyOf y sigue como si nada; usted nunca se entera. Esa arquitectura explica el rendimiento: get(i) es instantaneo porque salta directo a la posicion i del arreglo interno, agregar al final es barato casi siempre, pero add(0, mascota) o remove(0) obligan a correr un puesto a todos los demas elementos. En VetCare eso significa que agregar la mascota nueva al final del registro no cuesta nada, mientras que borrar siempre la primera ficha de una lista de 5.000 pacientes es la operacion mas cara que usted puede pedir.

La interfaz de trabajo es corta y hay que dominarla de memoria. Se declara asi: List<Mascota> mascotas = new ArrayList<>(); el List<Mascota> del lado izquierdo es la interfaz (el contrato) y el ArrayList<> del lado derecho es la implementacion concreta. Los metodos que usaremos toda la clase son add(objeto) para agregar al final, get(indice) para leer la posicion indicada, size() para saber cuantos hay, remove(indice) o remove(objeto) para sacar, set(indice, objeto) para reemplazar, isEmpty(), contains(objeto) e indexOf(objeto). El <Mascota> entre los picos se llama generico y no es decoracion: le dice al compilador que ahi solo entran Mascotas, de modo que si un estudiante intenta guardar un String el error aparece al compilar y no como un ClassCastException en plena sustentacion. Ojo con un detalle fino que confunde a todo el mundo: contains e indexOf comparan usando equals, asi que si usted no sobreescribe equals en Mascota, dos objetos con el mismo ID pero creados por separado seran considerados diferentes; por eso en VetCare buscamos por ID recorriendo la lista y comparando m.getId().equalsIgnoreCase(id).

Recorrer la lista tiene dos formas y cada una tiene su momento. El for clasico con indice (for (int i = 0; i < mascotas.size(); i++)) se usa cuando usted necesita el numero de la posicion, por ejemplo para imprimir el listado numerado de la sala de espera. El for-each (for (Mascota m : mascotas)) se usa cuando solo va a leer, es mas limpio y es el que debe volverse su reflejo. Ahora la trampa que se lleva por delante a media clase: si usted borra un elemento dentro de un for-each, Java lanza ConcurrentModificationException, porque el recorrido se da cuenta de que la lista cambio debajo de sus pies. La solucion correcta es usar un Iterator explicito y llamar a it.remove(), o usar mascotas.removeIf(m -> m.getEdad() >= 9). En VetCare esto aparece apenas queremos pasar a control geriatrico a todas las mascotas de nueve anios o mas: se recorre con Iterator, se saca con it.remove() y no truena nada.

La ultima idea es de diseno, y es la que hace que este codigo sirva para el resto del proyecto integrador. La lista no debe ser un atributo publico que cualquiera manipula desde main; debe vivir privada dentro de la clase RegistroMascotas, y el mundo exterior solo puede hablarle a traves de metodos con reglas de negocio: agregar valida que el ID no este repetido, eliminarPorId avisa si la mascota no existe, buscarPorId devuelve null cuando no la encuentra. Eso es encapsulamiento aplicado a colecciones, y es lo que hara posible que en las proximas clases la misma clase RegistroMascotas alimente una tabla de Swing y despues se guarde en un archivo CSV sin cambiar una sola linea de la logica. Programe siempre contra la interfaz (List) y no contra la implementacion (ArrayList), porque si manana necesita cambiar a LinkedList solo toca una linea. Y sobreescriba toString() en Mascota desde ya: sin el, imprimir la lista muestra basura como vetcare.Mascota@6d06d69c y los estudiantes creen que el programa fallo.

Error tipico del docente que no domina el tema: creer que new ArrayList<>(50) ya trae 50 mascotas adentro y hacer get(0) de una, lo que revienta con IndexOutOfBoundsException porque ese 50 es capacidad, no tamano; la lista recien creada tiene size() igual a cero. El segundo tropiezo es la confusion de nombres: los arreglos usan .length (sin parentesis), los String usan .length() (con parentesis) y las colecciones usan .size(); el docente escribe mascotas.length, no compila, y se queda mudo frente al grupo. El tercero es recorrer con i <= mascotas.size(), que siempre falla en la ultima vuelta porque los indices van de 0 a size()-1. Y el cuarto, el mas comun, es escribir ArrayList mascotas = new ArrayList(); sin generico, que compila con una advertencia amarilla, obliga a castear cada elemento al leerlo y termina en ClassCastException en tiempo de ejecucion. Antes de la clase, ejecute usted mismo estos cuatro errores en NetBeans para reconocer el mensaje rojo en dos segundos y convertirlo en ensenanza en vez de en silencio incomodo.

**Demo que usted debe poder repetir:** El docente muestra un Mascota[3] que revienta al intentar guardar la cuarta ficha y luego el mismo caso resuelto con ArrayList, imprimiendo size() despues de cada operacion.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: El registro de mascotas de VetCare deja de vivir en un arreglo de tamano fijo y pasa a un ArrayList<Mascota> que crece con la clinica.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en el VetCare de su equipo?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente muestra un Mascota[3] que revienta al intentar guardar la cuarta ficha y luego el mismo caso resuelto con ArrayList, imprimiendo size() despues de cada operacion.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 2/Codigo/VetCareRegistroMascotas.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Equipos: abran su proyecto VetCare. Esto suma a la rubrica del PI.»
Actividades:
1. Cree en NetBeans el proyecto Java Application llamado VetCare con paquete vetcare, y dentro de el la clase Mascota con los atributos privados id, nombre, especie, edad y dueno, su constructor completo, sus getters y el metodo toString(); verifique imprimiendo una mascota de prueba y confirmando que en consola sale el texto legible y no vetcare.Mascota@1a2b3c.
2. Cree la clase RegistroMascotas con el atributo private final List<Mascota> mascotas = new ArrayList<>(); y el metodo agregar(Mascota m) que rechace un ID ya existente; verifique agregando dos veces la mascota M-001 y comprobando que la consola muestra el aviso de ID repetido y que cantidad() sigue devolviendo 1.
3. Implemente listar(), que recorra con for indexado e imprima cada ficha numerada, y buscarPorId(String id), que recorra con for-each y devuelva la Mascota o null; verifique que buscarPorId("M-003") imprime la ficha de Rocky y que buscarPorId("M-099") imprime que no existe, sin lanzar NullPointerException.
4. Implemente eliminarPorId(String id) usando remove(objeto) y el metodo pasarAGeriatria(int edadMinima) usando Iterator con it.remove(); verifique que despues de eliminar M-002 y de pasar a geriatria a las mascotas de 9 anios o mas, size() bajo exactamente en la cantidad de fichas retiradas y el programa no lanza ConcurrentModificationException.
5. Arme un menu de consola con Scanner y opciones 1-Agregar, 2-Listar, 3-Buscar por ID, 4-Eliminar, 5-Salir dentro de un ciclo while; ejecute el programa cargando las seis fichas del escenario, tome captura de la consola con el listado final y suba el proyecto comprimido mas la captura a ExamLab.
Circular por los equipos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Proyecto NetBeans con las clases Mascota y RegistroMascotas y un menu de consola que agrega, lista, busca por ID y elimina mascotas, comprimido y subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 2/Quiz Clase 2 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: El registro de mascotas de VetCare deja de vivir en un arreglo de tamano fijo y pasa a un ArrayList<Mascota> que crece con la clinica.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 2/Solucion Taller Clase 2 - VetCare.docx` — no proyectar completa.
