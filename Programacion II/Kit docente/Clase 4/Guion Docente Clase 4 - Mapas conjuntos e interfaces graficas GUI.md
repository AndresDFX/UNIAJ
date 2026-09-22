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

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Antes de entrar en materia, el reparto del tiempo, porque hoy son dos...** — 4 vinetas.
  - Si el primer bloque se alarga, la ventana queda sin terminar y la clase se pierde, asi que ponga un cronometro visible.

**El problema tecnico es este: con un ArrayList, buscar por ID obliga a... (1/2)** — 3 vinetas.
  - Cuando dos claves distintas caen en la misma casilla (una colision), el mapa guarda ambas en esa casilla y usa equals() para distinguirlas al leer.

**El problema tecnico es este: con un ArrayList, buscar por ID obliga a... (2/2)** — 2 vinetas.

**El problema tecnico es este: con un... — sintaxis** — 1 vinetas.

**La API de Map es corta pero tiene trampas que hay que nombrar en voz... (1/2)** — 3 vinetas.

**La API de Map es corta pero tiene trampas que hay que nombrar en voz... (2/2)** — 3 vinetas.

**La API de Map es corta pero tiene trampas que... — sintaxis** — 1 vinetas.

**El HashSet es el hermano del HashMap: por dentro es literalmente un...** — 6 vinetas.
  - Lo que un HashSet no le garantiza es el orden: si usted agrega Labrador, Criollo y Persa y luego imprime el conjunto, pueden salir en cualquier orden, porque la posicion la decide el hash.
  - Si necesita conservar el orden de insercion use LinkedHashSet o LinkedHashMap, y si necesita orden alfabetico use TreeSet o TreeMap, que ordenan pero cuestan un poco mas.

**Ahora la parte grafica, y aqui empieza el segundo bloque de la clase (1/2)** — 4 vinetas.
  - Ahora la parte grafica, y aqui empieza el segundo bloque de la clase.

**Ahora la parte grafica, y aqui empieza el segundo bloque de la clase (2/2)** — 3 vinetas.

**class VetCareBuscarExpediente** — 11 vinetas.

**VetCareBuscarExpediente.java — VetCareBuscarExpediente()** — 7 vinetas.

**VetCareBuscarExpediente.java — cargarDatosDePrueba()** — 10 vinetas.

**VetCareBuscarExpediente.java — guardar()** — 12 vinetas.

**VetCareBuscarExpediente.java — compararBusquedas() (1/2)** — 20 vinetas.

**VetCareBuscarExpediente.java — compararBusquedas() (2/2)** — 11 vinetas.

**VetCareBuscarExpediente.java — construirInterfaz() (1/2)** — 20 vinetas.

**VetCareBuscarExpediente.java — construirInterfaz() (2/2)** — 5 vinetas.

**VetCareBuscarExpediente.java — buscar() (1/2)** — 20 vinetas.

**VetCareBuscarExpediente.java — buscar() (2/2)** — 2 vinetas.

**VetCareBuscarExpediente.java — main()** — 6 vinetas.

**VetCareBuscarExpediente.java — class Expediente** — 8 vinetas.

**VetCareBuscarExpediente.java — Expediente()** — 15 vinetas.


**Demo que usted debe poder repetir:** El docente busca la ficha H-5000 dentro de un archivo historico de 5.000 expedientes, primero recorriendo un ArrayList y luego con get() sobre un HashMap comparando los nanosegundos, y despues ejecuta la misma busqueda desde una ventana Swing escrita linea por linea.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare encuentra cualquier expediente por ID en tiempo constante con HashMap y estrena su primera ventana Swing para consultarlo.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente busca la ficha H-5000 dentro de un archivo historico de 5.000 expedientes, primero recorriendo un ArrayList y luego con get() sobre un HashMap comparando los nanosegundos, y despues ejecuta la misma busqueda desde una ventana Swing escrita linea por linea.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 4/Codigo/VetCareBuscarExpediente.java`

### 60-105 · Taller guiado = avance del PI
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
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 4/Quiz Clase 4 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare encuentra cualquier expediente por ID en tiempo constante con HashMap y estrena su primera ventana Swing para consultarlo.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 4/Solucion Taller Clase 4 - VetCare.docx` — no proyectar completa.
