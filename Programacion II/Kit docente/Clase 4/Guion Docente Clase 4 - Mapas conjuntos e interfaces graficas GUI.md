# Guion docente · Clase 4 · Mapas, conjuntos e interfaces graficas · HashMap, HashSet y Swing

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** VetCare encuentra cualquier expediente por ID en tiempo constante con HashMap y estrena su primera ventana Swing para consultarlo.
- **Entregable de hoy:** Clase RegistroExpedientes con HashMap y HashSet mas la ventana VentanaBuscarExpediente construida a mano (sin arrastrar componentes) que busca por ID y muestra el resultado o un mensaje de error controlado; comprimido y subido a ExamLab.
- **Herramienta:** Apache NetBeans
- **Slides:** `Clases/Clase 4 - Mapas conjuntos e interfaces graficas GUI/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Antes de entrar en materia, el reparto del tiempo, porque hoy son dos temas en un solo bloque de 120 minutos y hay que ser estricto: minutos 0 a 10 encuadre y repaso rapido de cola y pila; minutos 10 a 55 mapas y conjuntos con demo en consola; minutos 55 a 65 pausa; minutos 65 a 95 introduccion a Swing con la ventana construida en vivo; minutos 95 a 115 taller integrado donde la ventana consulta el HashMap; minutos 115 a 120 cierre y entrega en ExamLab. Si el primer bloque se alarga, la ventana queda sin terminar y la clase se pierde, asi que ponga un cronometro visible. El hilo que une los dos temas es uno solo: hoy le damos a VetCare la capacidad de responder en un instante la pregunta que mas hace la recepcionista de Huellitas, que es dame el expediente de la mascota M-004, y ademas le damos una pantalla para hacerla sin abrir NetBeans.

El problema tecnico es este: con un ArrayList, buscar por ID obliga a recorrer la lista comparando uno por uno, lo que se llama busqueda lineal y en el peor caso revisa los 5.000 elementos del archivo historico. Un HashMap resuelve eso con una idea distinta: en vez de guardar solo el objeto, guarda parejas clave-valor, y usa la clave para calcular directamente en que casilla del arreglo interno esta el valor. Ese calculo lo hace el metodo hashCode() del objeto clave: convierte el texto M-004 en un numero, ese numero se transforma en una posicion del arreglo interno, y ahi mismo queda el expediente. Cuando dos claves distintas caen en la misma casilla (una colision), el mapa guarda ambas en esa casilla y usa equals() para distinguirlas al leer. El resultado practico es que get("M-004") no depende de cuantas mascotas haya: con 10 o con 100.000 tarda basicamente lo mismo, y eso es lo que vamos a medir en vivo con System.nanoTime(). En VetCare declaramos Map<String, Expediente> expedientes = new HashMap<>(); y la clave es el ID, que es unico por definicion.

La API de Map es corta pero tiene trampas que hay que nombrar en voz alta. put(clave, valor) agrega, pero si la clave ya existia reemplaza el valor anterior en silencio y devuelve el que estaba: eso significa que un HashMap nunca tiene claves repetidas, y que guardar dos veces M-001 no da error, simplemente pisa el expediente anterior, lo cual puede ser exactamente lo que usted quiere o un bug grave si no lo controla. get(clave) devuelve el valor o null si la clave no existe, por eso siempre hay que validar antes de usar el resultado; getOrDefault(clave, valorPorDefecto) es la version comoda. containsKey pregunta por la clave y containsValue por el valor, siendo esta ultima lenta porque esa si recorre todo el mapa. Para recorrer se usa for (Map.Entry<String, Expediente> e : expedientes.entrySet()) y dentro se leen e.getKey() y e.getValue(); tambien existen keySet() para las claves y values() para los valores. Y algo crucial: si algun dia usted usa un objeto propio como clave, esta obligado a sobreescribir equals() y hashCode() juntos, porque si no, el mapa guardara duplicados que a los ojos del negocio son el mismo.

El HashSet es el hermano del HashMap: por dentro es literalmente un HashMap donde solo importan las claves. Su promesa es una sola y es potente: no admite duplicados y responde en tiempo constante a la pregunta esto ya esta. Su metodo add devuelve un boolean que casi nadie mira y que vale oro: devuelve false si el elemento ya estaba. En VetCare lo usamos para dos cosas concretas: un Set<String> de IDs ya usados, para rechazar un registro duplicado sin recorrer nada, y un Set<String> de razas atendidas, que se llena solo y nos dice cuantas razas distintas ha visto la clinica sin que nadie las cuente a mano; como Firulais y Toby son los dos labradores, al guardar el segundo el conjunto responde false y sigue reportando una sola vez esa raza. Lo que un HashSet no le garantiza es el orden: si usted agrega Labrador, Criollo y Persa y luego imprime el conjunto, pueden salir en cualquier orden, porque la posicion la decide el hash. Si necesita conservar el orden de insercion use LinkedHashSet o LinkedHashMap, y si necesita orden alfabetico use TreeSet o TreeMap, que ordenan pero cuestan un poco mas.

Ahora la parte grafica, y aqui empieza el segundo bloque de la clase. Swing es la biblioteca de escritorio de Java y funciona por anidamiento: la ventana es un JFrame, dentro del frame hay un contenedor donde se ponen paneles JPanel, y dentro de los paneles van los componentes visibles como JLabel (texto fijo), JTextField (caja donde el usuario escribe) y JButton (boton). Como se acomodan esos componentes lo decide un layout manager: el JFrame usa BorderLayout por defecto, que reparte la ventana en NORTH, SOUTH, EAST, WEST y CENTER; el JPanel usa FlowLayout, que va poniendo los componentes en fila; y GridLayout arma una cuadricula de filas y columnas. Todo JFrame necesita tres lineas obligatorias o el estudiante creera que su programa no sirve: setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE) para que cerrar la ventana termine el programa, setSize o pack para darle tamano, y setVisible(true) para que aparezca. Ademas, la ventana debe crearse dentro de SwingUtilities.invokeLater porque toda la interfaz de Swing vive en un hilo especial llamado EDT; hacerlo bien desde hoy evita cuelgues raros mas adelante.

Error tipico del docente que no domina el tema: abrir el disenador visual de NetBeans, arrastrar tres componentes, hacer doble clic en el boton y escribir toda la logica del negocio dentro de jButton1ActionPerformed. Eso produce una demo bonita en cinco minutos y un curso que no entiende nada, porque el codigo generado esta bloqueado, no se puede editar, y el estudiante nunca ve donde se crea el JFrame ni como se conecta el evento. Escriba la ventana a mano al menos esta primera vez, y deje claro que la ventana solo lee el texto del JTextField y llama a un metodo del registro: la logica y el HashMap viven en la clase de negocio, no en la interfaz. Los otros tropiezos son mecanicos y hay que provocarlos a proposito: olvidar setVisible(true) y quedarse esperando una ventana que nunca aparece; usar setLayout(null) y posicionar todo con coordenadas fijas que se descuadran al cambiar el tamano; y en la parte de mapas, imprimir un HashMap esperando el orden de insercion y no poder explicar por que salio revuelto. Ensaye la clase completa una vez de corrido antes del miercoles, con cronometro, porque el riesgo real de hoy no es tecnico sino de tiempo.

**Demo que usted debe poder repetir:** El docente busca la ficha H-5000 dentro de un archivo historico de 5.000 expedientes, primero recorriendo un ArrayList y luego con get() sobre un HashMap comparando los nanosegundos, y despues ejecuta la misma busqueda desde una ventana Swing escrita linea por linea.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare encuentra cualquier expediente por ID en tiempo constante con HashMap y estrena su primera ventana Swing para consultarlo.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en el VetCare de su equipo?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente busca la ficha H-5000 dentro de un archivo historico de 5.000 expedientes, primero recorriendo un ArrayList y luego con get() sobre un HashMap comparando los nanosegundos, y despues ejecuta la misma busqueda desde una ventana Swing escrita linea por linea.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 4/Codigo/VetCareBuscarExpediente.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Equipos: abran su proyecto VetCare. Esto suma a la rubrica del PI.»
Actividades:
1. Bloque de mapas (minutos 10 a 30): cree la clase Expediente con id, nombre, raza, dueno y nota clinica, y la clase RegistroExpedientes con private final Map<String, Expediente> expedientes = new HashMap<>(); verifique guardando los cinco expedientes del escenario e imprimiendo expedientes.size().
2. Bloque de mapas (minutos 30 a 45): implemente buscar(String id) con get y validacion de null, y guardar(Expediente e) que use containsKey para avisar cuando un ID ya existe antes de que put lo reemplace en silencio; verifique guardando dos veces M-001 y confirmando que el mapa sigue en cinco expedientes y aparece el aviso.
3. Bloque de conjuntos (minutos 45 a 55): agregue private final Set<String> razas = new HashSet<>(); que se llene automaticamente en cada guardar y aproveche el boolean que devuelve add para avisar cuando la raza ya estaba; verifique que al cargar a Firulais y a Toby, ambos labradores, el conjunto reporta la raza repetida y razas.size() cuenta una sola vez Labrador.
4. Bloque Swing (minutos 65 a 95): escriba a mano la clase VentanaBuscarExpediente que extiende JFrame, con un JPanel superior que contenga un JLabel, un JTextField y un JButton, y un JLabel central para el resultado; verifique que la ventana abre centrada, con titulo VetCare y que al cerrarla el programa termina.
5. Integracion (minutos 95 a 115): conecte el boton con addActionListener usando lambda para que lea el ID del JTextField, lo normalice con trim() y toUpperCase(), consulte el HashMap y muestre el expediente en el JLabel central o un JOptionPane de advertencia si no existe, todo dentro de try-catch; capture la ventana con una busqueda exitosa y una fallida y suba el proyecto a ExamLab.
Circular por los equipos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Clase RegistroExpedientes con HashMap y HashSet mas la ventana VentanaBuscarExpediente construida a mano (sin arrastrar componentes) que busca por ID y muestra el resultado o un mensaje de error controlado; comprimido y subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 4/Quiz Clase 4 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare encuentra cualquier expediente por ID en tiempo constante con HashMap y estrena su primera ventana Swing para consultarlo.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 4/Solucion Taller Clase 4 - VetCare.docx` — no proyectar completa.
