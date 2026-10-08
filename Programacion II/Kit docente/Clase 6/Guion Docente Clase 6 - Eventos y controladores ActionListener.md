# Guion docente · Clase 6 · Eventos y controladores · ActionListener

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** El formulario de VetCare queda conectado: al oprimir 'Registrar mascota' el objeto entra al ArrayList y el listado en pantalla se actualiza.
- **Entregable de hoy:** Proyecto VetCare con la ventana de registro operativa y la clase ControladorRegistro separada de la vista, comprimido y subido a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 6 - Eventos y controladores ActionListener/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Las ideas de cada concepto estan proyectadas y el desarrollo completo esta en las notas del presentador de su lamina. Aqui va, por lamina y en su orden, lo que hay que subrayar.

**[Slide 4] Del programa en línea recta al evento** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Una aplicacion con ventanas no funciona asi.
  - Subrayar: Cada una de esas acciones se convierte en un objeto de evento que entra a una cola, y Swing va sacando esos eventos uno por uno y le avisa al objeto que previamente dijo 'a mi me interesa ese boton'.
  - Subrayar: Eso es programacion dirigida por eventos: usted ya no decide cuando corre su codigo; usted lo deja escrito y registrado, y quien decide cuando se ejecuta es la recepcionista de Huellitas el dia que oprima 'Registrar mascota'.
  - Subrayar: Por eso el metodo que guarda la mascota nunca aparece llamado desde el main: aparece registrado, no llamado, y esa diferencia es la que hay que entender hoy.

**[Slide 5] main(): la ventana arranca en el EDT** — programa completo (24 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 6] ActionListener: el contrato del clic** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Hay tres formas validas de escribirlo en Java y conviene mostrarlas todas: una clase aparte que implements ActionListener, una clase anonima escrita ahi mismo con new ActionListener() {... }, o una expresion lambda e -> registrar() si el proyecto esta en Java 8 o superior.
  - Subrayar: Con una de dos metodos no compila, y el mensaje del editor no lo dice con esas palabras y ahi adentro va su llamada.

**[Slide 7] El formulario: GridLayout de 5 × 2** — programa completo (45 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 8] addActionListener: el botón guarda a quien lo escucha** — programa completo (38 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 9] Separar la lógica de la interfaz** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Separar la logica de la interfaz significa que la ventana no conoce reglas de negocio y que las reglas no saben que existe una ventana.
  - Subrayar: Si toca reescribir todo porque la conversion de la edad estaba adentro del boton, el diseño esta mal.

**[Slide 10] El repositorio no sabe de ventanas** — programa completo (49 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 11] Un clic en cámara lenta** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Vale la pena desarmar en camara lenta lo que ocurre en un click de 'Registrar mascota'.
  - Subrayar: Cuarto, la vista atrapa esa excepcion y la convierte en un JOptionPane, o, si no hubo error, limpia los campos y refresca el area de listado.

**[Slide 12] registrar(): la vista lee, delega y muestra** — programa completo (46 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 13] registrarMascota(): el controlador valida y convierte** — programa completo (43 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 14] getSource y otros escuchadores** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Dos detalles mas que le van a servir.
  - Subrayar: Para eso existe SwingWorker.

## Errores tipicos del docente que no domina el tema

Material de preparacion: no se proyecta.

- Error tipico del docente que no domina el tema: escribir toda la aplicacion adentro de actionPerformed y, peor aun, crear el repositorio dentro del listener. Se ve asi de inocente: 'RepositorioMascotas repo = new RepositorioMascotas();' como primera linea del boton. Compila, no marca error, el estudiante registra dos mascotas y la lista siempre muestra una sola, y el docente termina diciendo en voz alta que 'ArrayList no esta guardando'. Lo que realmente pasa es que en cada click se construye un repositorio vacio nuevo y el anterior se lo lleva el recolector de basura: la coleccion tiene que ser un atributo de la ventana o del controlador, creado una sola vez. El segundo error de la misma familia es registrar el escuchador dentro del metodo que corre en cada click, en vez de una sola vez en el constructor: cada click agrega OTRO listener al mismo boton, y a la quinta pulsacion la mascota se registra cinco veces. Y el tercero es capturar Exception con un catch vacio: la aplicacion no se cae, pero tampoco avisa nada, y el error se vuelve invisible para el estudiante y para usted.


**Demo que usted debe poder repetir:** El docente oprime el boton de la ventana ya corriendo y muestra en vivo como la mascota pasa del formulario al ArrayList, incluyendo que pasa cuando la edad se escribe como texto.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: El formulario de VetCare queda conectado: al oprimir 'Registrar mascota' el objeto entra al ArrayList y el listado en pantalla se actualiza.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de concepto y en las de codigo
(lo que hay que subrayar esta tambien en las notas del presentador de cada lamina). Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente oprime el boton de la ventana ya corriendo y muestra en vivo como la mascota pasa del formulario al ArrayList, incluyendo que pasa cuando la edad se escribe como texto.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 6/Codigo/ClinicaEventosDemo.java`

### 60-105 · Taller guiado (opcional) = avance del PI
Opcional: no tiene lamina en el deck. La guia esta en
`Clases/Clase 6 - Eventos y controladores ActionListener/Taller PI - Clase 6 - VetCare.docx`; si hoy no se hace, se extiende la demo y la practica libre.
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Cree el paquete clinica.vista y dentro la clase VentanaRegistroMascota que extiende JFrame, con los campos ID, nombre, especie y edad, el boton 'Registrar mascota' y un JTextArea de solo lectura para el listado; ejecutela y verifique que abre centrada y que cierra con EXIT_ON_CLOSE.
2. Deje Mascota en clinica.modelo y cree en clinica.servicio la clase RepositorioMascotas con un ArrayList<Mascota> privado y los metodos registrar, buscarPorId, listar y total; compruebe con Ctrl+F que ninguna de esas dos clases tiene un import de javax.swing.
3. Cree ControladorRegistro con el metodo registrarMascota(String id, String nombre, String especie, String edadTexto) que valide obligatorios, convierta la edad con Integer.parseInt dentro de try-catch y lance IllegalArgumentException con mensajes en español; el repositorio debe recibirse por el constructor, no crearse adentro del metodo.
4. Conecte el boton con addActionListener de manera que el cuerpo del listener tenga maximo cinco lineas: leer los getText(), llamar al controlador, refrescar el area, limpiar campos y mostrar el JOptionPane; declare el controlador como atributo de la ventana, nunca dentro del listener.
5. Pruebe y capture evidencia de tres casos: (a) registro valido de M-001 Kira, (b) edad escrita como 'tres', (c) ID repetido M-001; guarde las tres capturas, exporte el proyecto comprimido y subalo a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Proyecto VetCare con la ventana de registro operativa y la clase ControladorRegistro separada de la vista, comprimido y subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Si hubo taller, repasar los criterios de exito del `Taller PI - Clase 6 - VetCare.docx` (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 6/Quiz Clase 6 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: El formulario de VetCare queda conectado: al oprimir 'Registrar mascota' el objeto entra al ArrayList y el listado en pantalla se actualiza.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 6/Solucion Taller Clase 6 - VetCare.docx` — no proyectar completa.
