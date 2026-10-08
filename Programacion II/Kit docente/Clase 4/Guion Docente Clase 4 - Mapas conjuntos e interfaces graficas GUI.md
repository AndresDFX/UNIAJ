# Guion docente · Clase 4 · Mapas, conjuntos e interfaces graficas · HashMap, HashSet y Swing

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** VetCare encuentra cualquier expediente por ID en tiempo constante con HashMap y estrena su primera ventana Swing para consultarlo.
- **Entregable de hoy:** Clase RegistroExpedientes con HashMap y HashSet mas la ventana VentanaBuscarExpediente construida a mano (sin arrastrar componentes) que busca por ID y muestra el resultado o un mensaje de error controlado; comprimido y subido a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 4 - Mapas conjuntos e interfaces graficas GUI/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Las ideas de cada concepto estan proyectadas y el desarrollo completo esta en las notas del presentador de su lamina. Aqui va, por lamina y en su orden, lo que hay que subrayar.

**[Slide 4] Mapas y ventanas: un mismo objetivo** — 3 ideas proyectadas; el desarrollo, en las notas del presentador.

**[Slide 5] De la búsqueda lineal al HashMap** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Cuando dos claves distintas caen en la misma casilla (una colision), el mapa guarda ambas en esa casilla y usa equals() para distinguirlas al leer.

**[Slide 6] Expediente: el valor que guarda el mapa** — programa completo (31 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 7] La misma ficha en una lista y en un mapa** — programa completo (36 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 8] Medir: recorrer contra get(clave)** — programa completo (45 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 9] La API de Map y sus trampas** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: La API de Map es corta pero tiene trampas que hay que nombrar en voz alta. put(clave, valor) agrega, pero si la clave ya existia reemplaza el valor anterior en silencio y devuelve el que estaba: eso significa que un HashMap nunca tiene claves repetidas, y que guardar dos veces M-001 no da error, simplemente pisa el expediente anterior, lo cual puede ser exactamente lo que usted quiere o un bug grave si no lo controla. get(clave) devuelve el valor o null si la clave no existe, por eso siempre hay que validar antes de usar el resultado; getOrDefault(clave, valorPorDefecto) es la version comoda. containsKey pregunta por la clave y containsValue por el valor, siendo esta ultima lenta porque esa si recorre todo el mapa.

**[Slide 10] guardar(): put avisa antes de reemplazar** — programa completo (46 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 11] HashSet: el conjunto sin duplicados** — 3 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Lo que un HashSet no le garantiza es el orden: si usted agrega Labrador, Criollo y Persa y luego imprime el conjunto, pueden salir en cualquier orden, porque la posicion la decide el hash.
  - Subrayar: Si necesita conservar el orden de insercion use LinkedHashSet o LinkedHashMap, y si necesita orden alfabetico use TreeSet o TreeMap, que ordenan pero cuestan un poco mas.

**[Slide 12] Un mapa y un conjunto como atributos** — programa completo (46 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 13] Swing: ventana, paneles y componentes** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Ahora la parte grafica, y aqui empieza el segundo bloque de la clase.

**[Slide 14] Paneles y layouts, escritos a mano** — programa completo (37 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 15] El evento, el cierre y el arranque en el EDT** — programa completo (36 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 16] buscar(): get y el caso null** — programa completo (45 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

## Errores tipicos del docente que no domina el tema

Material de preparacion: no se proyecta.

- Error tipico del docente que no domina el tema: pegar una ventana entera —de un tutorial o de una IA— y escribir toda la logica del negocio dentro del actionPerformed del boton. Eso produce una demo bonita en cinco minutos y un curso que no entiende nada, porque el estudiante nunca ve donde se crea el JFrame ni como se conecta el evento. VS Code no trae disenador visual, y en esta clase eso es una ventaja, no una carencia: obliga a escribir la ventana a mano. Escribala completa al menos esta primera vez, y deje claro que la ventana solo lee el texto del JTextField y llama a un metodo del registro: la logica y el HashMap viven en la clase de negocio, no en la interfaz. Los otros tropiezos son mecanicos y hay que provocarlos a proposito: olvidar setVisible(true) y quedarse esperando una ventana que nunca aparece; usar setLayout(null) y posicionar todo con coordenadas fijas que se descuadran al cambiar el tamano; y en la parte de mapas, imprimir un HashMap esperando el orden de insercion y no poder explicar por que salio revuelto. Ensaye la clase completa una vez de corrido antes del miercoles, con cronometro, porque el riesgo real de hoy no es tecnico sino de tiempo.


**Demo que usted debe poder repetir:** El docente busca la ficha H-5000 dentro de un archivo historico de 5.000 expedientes, primero recorriendo un ArrayList y luego con get() sobre un HashMap comparando los nanosegundos, y despues ejecuta la misma busqueda desde una ventana Swing escrita linea por linea.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare encuentra cualquier expediente por ID en tiempo constante con HashMap y estrena su primera ventana Swing para consultarlo.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de concepto y en las de codigo
(lo que hay que subrayar esta tambien en las notas del presentador de cada lamina). Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente busca la ficha H-5000 dentro de un archivo historico de 5.000 expedientes, primero recorriendo un ArrayList y luego con get() sobre un HashMap comparando los nanosegundos, y despues ejecuta la misma busqueda desde una ventana Swing escrita linea por linea.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 4/Codigo/ClinicaBuscarExpediente.java`

### 60-105 · Taller guiado (opcional) = avance del PI
Opcional: no tiene lamina en el deck. La guia esta en
`Clases/Clase 4 - Mapas conjuntos e interfaces graficas GUI/Taller PI - Clase 4 - VetCare.docx`; si hoy no se hace, se extiende la demo y la practica libre.
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Bloque de mapas (minutos 10 a 30): cree la clase Expediente con id, nombre, raza, dueno y nota clinica, y la clase RegistroExpedientes con private final Map<String, Expediente> expedientes = new HashMap<>(); verifique guardando los cinco expedientes del escenario e imprimiendo expedientes.size().
2. Bloque de mapas (minutos 30 a 45): implemente buscar(String id) con get y validacion de null, y guardar(Expediente e) que use containsKey para avisar cuando un ID ya existe antes de que put lo reemplace en silencio; verifique guardando dos veces M-001 y confirmando que el mapa sigue en cinco expedientes y aparece el aviso.
3. Bloque de conjuntos (minutos 45 a 55): agregue private final Set<String> razas = new HashSet<>(); que se llene automaticamente en cada guardar y aproveche el boolean que devuelve add para avisar cuando la raza ya estaba; verifique que al cargar a Firulais y a Toby, ambos labradores, el conjunto reporta la raza repetida y razas.size() cuenta una sola vez Labrador.
4. Bloque Swing (minutos 65 a 95): escriba a mano la clase VentanaBuscarExpediente que extiende JFrame, con un JPanel superior que contenga un JLabel, un JTextField y un JButton, y un JLabel central para el resultado; verifique que la ventana abre centrada, con titulo VetCare y que al cerrarla el programa termina.
5. Integracion (minutos 95 a 115): conecte el boton con addActionListener usando lambda para que lea el ID del JTextField, lo normalice con trim() y toUpperCase(), consulte el HashMap y muestre el expediente en el JLabel central o un JOptionPane de advertencia si no existe, todo dentro de try-catch; capture la ventana con una busqueda exitosa y una fallida y suba el proyecto a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Clase RegistroExpedientes con HashMap y HashSet mas la ventana VentanaBuscarExpediente construida a mano (sin arrastrar componentes) que busca por ID y muestra el resultado o un mensaje de error controlado; comprimido y subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Si hubo taller, repasar los criterios de exito del `Taller PI - Clase 4 - VetCare.docx` (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 4/Quiz Clase 4 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare encuentra cualquier expediente por ID en tiempo constante con HashMap y estrena su primera ventana Swing para consultarlo.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 4/Solucion Taller Clase 4 - VetCare.docx` — no proyectar completa.
