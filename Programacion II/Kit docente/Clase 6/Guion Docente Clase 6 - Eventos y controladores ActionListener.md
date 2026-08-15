# Guion docente · Clase 6 · Eventos y controladores · ActionListener

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** El formulario de VetCare queda conectado: al oprimir 'Registrar mascota' el objeto entra al ArrayList y el listado en pantalla se actualiza.
- **Entregable de hoy:** Proyecto VetCare con la ventana de registro operativa y la clase ControladorRegistro separada de la vista, comprimido y subido a ExamLab.
- **Herramienta:** Apache NetBeans
- **Slides:** `Clases/Clase 6 - Eventos y controladores ActionListener/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Hasta ahora los programas de VetCare corrian en linea recta: el main llamaba un metodo, ese metodo llamaba a otro y el programa terminaba. Una aplicacion con ventanas no funciona asi. Cuando usted hace setVisible(true), Swing arranca un hilo especial llamado EDT (Event Dispatch Thread) que se queda vivo esperando que el usuario haga algo: mover el mouse, escribir en un campo, oprimir un boton. Cada una de esas acciones se convierte en un objeto de evento que entra a una cola, y Swing va sacando esos eventos uno por uno y le avisa al objeto que previamente dijo 'a mi me interesa ese boton'. Eso es programacion dirigida por eventos: usted ya no decide cuando corre su codigo; usted lo deja escrito y registrado, y quien decide cuando se ejecuta es la recepcionista de Huellitas el dia que oprima 'Registrar mascota'. Por eso el metodo que guarda la mascota nunca aparece llamado desde el main: aparece registrado, no llamado, y esa diferencia es la que hay que entender hoy.

ActionListener es una interfaz de java.awt.event que tiene un solo metodo: void actionPerformed(ActionEvent e). Implementarla es firmar un contrato que dice 'yo se reaccionar a una accion'. El registro se hace con btnRegistrar.addActionListener(objetoQueEscucha): desde esa linea el boton guarda una referencia a su objeto y, cuando lo oprimen, Swing invoca actionPerformed pasandole un ActionEvent con informacion del disparo (quien lo genero, en que instante, con que comando). Hay tres formas validas de escribirlo en NetBeans y conviene mostrarlas todas: una clase aparte que implements ActionListener, una clase anonima escrita ahi mismo con new ActionListener() { ... }, o una expresion lambda e -> registrar() si el proyecto esta en Java 8 o superior. Un detalle practico que confunde a medio salon: si usted arma la ventana con el diseñador visual y hace doble clic sobre el boton, NetBeans le genera automaticamente el metodo btnRegistrarActionPerformed y deja el addActionListener dentro del bloque gris protegido. Ese bloque no se edita a mano, pero el metodo generado si es suyo y ahi adentro va su llamada.

Separar la logica de la interfaz significa que la ventana no conoce reglas de negocio y que las reglas no saben que existe una ventana. En VetCare vamos a tener tres capas claras: el modelo (Mascota, Dueno, Cita), que solo guarda datos y comportamiento propio; el servicio o controlador (ControladorRegistro, RepositorioMascotas), donde viven las validaciones, la busqueda por ID y el ArrayList; y la vista (VentanaRegistroMascota), que unicamente pinta campos, lee texto y muestra mensajes. La prueba acida es esta pregunta: si mañana Huellitas pide la misma funcionalidad en consola, o migramos a JavaFX, cuanto codigo hay que reescribir? Si la respuesta es 'solamente la ventana', el diseño esta bien. Si toca reescribir todo porque la conversion de la edad estaba adentro del boton, el diseño esta mal. Y hay una razon adicional que se vuelve evidente en la clase 8: a un ControladorRegistro se le pueden hacer pruebas automaticas; a un boton no se le puede.

Vale la pena desarmar en camara lenta lo que ocurre en un click de 'Registrar mascota'. Primero la vista lee texto crudo: txtId.getText(), txtNombre.getText(), txtEdad.getText(); todo lo que sale de un JTextField es String, incluida la edad. Segundo, ese texto viaja al controlador, que hace el trabajo sucio: recorta espacios con trim(), rechaza campos vacios, convierte la edad con Integer.parseInt dentro de un try-catch porque si la auxiliar escribio 'tres' salta NumberFormatException, y le pregunta al repositorio si ese ID ya existe. Tercero, si algo esta mal el controlador lanza una excepcion con un mensaje entendible para un humano ('La edad debe ser un numero entero'); si todo esta bien, construye el objeto Mascota y lo agrega al ArrayList. Cuarto, la vista atrapa esa excepcion y la convierte en un JOptionPane, o, si no hubo error, limpia los campos y refresca el area de listado. Ese ciclo leer-validar-delegar-refrescar es exactamente el mismo que vamos a repetir despues para agendar citas, para buscar expedientes y para guardar en archivo.

Dos detalles mas que le van a servir. El ActionEvent trae e.getSource(), que devuelve el componente que disparo el evento; eso permite que un mismo listener atienda varios botones y decida con un if (e.getSource() == btnBuscar). Es comodo, pero uselo con cabeza: si el metodo se llena de ifs, es mas limpio un listener por boton. Ademas de ActionListener existen otros escuchadores que ya vamos a necesitar en VetCare: ItemListener para el JComboBox de especie, ListSelectionListener para cuando el usuario selecciona una fila del listado de mascotas, y WindowListener para preguntar 'desea guardar antes de salir' cuando lleguemos a persistencia. Y una advertencia de rendimiento: todo lo que usted escriba dentro de actionPerformed corre en el EDT, el mismo hilo que dibuja la ventana; si ahi mete una tarea larga, la interfaz se congela y el usuario cree que el programa se colgo. Para eso existe SwingWorker. Por ahora la regla es simple: listeners cortos que solo leen, delegan y muestran.

Error tipico del docente que no domina el tema: escribir toda la aplicacion adentro de actionPerformed y, peor aun, crear el repositorio dentro del listener. Se ve asi de inocente: 'RepositorioMascotas repo = new RepositorioMascotas();' como primera linea del boton. Compila, no marca error, el estudiante registra dos mascotas y la lista siempre muestra una sola, y el docente termina diciendo en voz alta que 'ArrayList no esta guardando'. Lo que realmente pasa es que en cada click se construye un repositorio vacio nuevo y el anterior se lo lleva el recolector de basura: la coleccion tiene que ser un atributo de la ventana o del controlador, creado una sola vez. El segundo error de la misma familia es pelearse con el bloque gris que NetBeans protege tratando de escribir ahi el addActionListener, cuando lo que hay que editar es el metodo generado. Y el tercero es capturar Exception con un catch vacio: la aplicacion no se cae, pero tampoco avisa nada, y el error se vuelve invisible para el estudiante y para usted.

**Demo que usted debe poder repetir:** El docente oprime el boton en NetBeans y muestra en vivo como la mascota pasa del formulario al ArrayList, incluyendo que pasa cuando la edad se escribe como texto.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: El formulario de VetCare queda conectado: al oprimir 'Registrar mascota' el objeto entra al ArrayList y el listado en pantalla se actualiza.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente oprime el boton en NetBeans y muestra en vivo como la mascota pasa del formulario al ArrayList, incluyendo que pasa cuando la edad se escribe como texto.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 6/Codigo/VetCareEventosDemo.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Cree el paquete vetcare.vista y dentro la clase VentanaRegistroMascota que extiende JFrame, con los campos ID, nombre, especie y edad, el boton 'Registrar mascota' y un JTextArea de solo lectura para el listado; ejecutela y verifique que abre centrada y que cierra con EXIT_ON_CLOSE.
2. Deje Mascota en vetcare.modelo y cree en vetcare.servicio la clase RepositorioMascotas con un ArrayList<Mascota> privado y los metodos registrar, buscarPorId, listar y total; compruebe con Ctrl+F que ninguna de esas dos clases tiene un import de javax.swing.
3. Cree ControladorRegistro con el metodo registrarMascota(String id, String nombre, String especie, String edadTexto) que valide obligatorios, convierta la edad con Integer.parseInt dentro de try-catch y lance IllegalArgumentException con mensajes en español; el repositorio debe recibirse por el constructor, no crearse adentro del metodo.
4. Conecte el boton con addActionListener de manera que el cuerpo del listener tenga maximo cinco lineas: leer los getText(), llamar al controlador, refrescar el area, limpiar campos y mostrar el JOptionPane; declare el controlador como atributo de la ventana, nunca dentro del listener.
5. Pruebe y capture evidencia de tres casos: (a) registro valido de M-001 Kira, (b) edad escrita como 'tres', (c) ID repetido M-001; guarde las tres capturas, exporte el proyecto comprimido y subalo a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Proyecto VetCare con la ventana de registro operativa y la clase ControladorRegistro separada de la vista, comprimido y subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 6/Quiz Clase 6 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: El formulario de VetCare queda conectado: al oprimir 'Registrar mascota' el objeto entra al ArrayList y el listado en pantalla se actualiza.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 6/Solucion Taller Clase 6 - VetCare.docx` — no proyectar completa.
