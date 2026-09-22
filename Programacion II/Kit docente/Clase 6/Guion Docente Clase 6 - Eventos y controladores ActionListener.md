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

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Hasta ahora los programas de VetCare corrian en linea recta: el main...** — 2 vinetas.
  - Una aplicacion con ventanas no funciona asi.
  - Cada una de esas acciones se convierte en un objeto de evento que entra a una cola, y Swing va sacando esos eventos uno por uno y le avisa al objeto que previamente dijo 'a mi me interesa ese boton'.
  - Eso es programacion dirigida por eventos: usted ya no decide cuando corre su codigo; usted lo deja escrito y registrado, y quien decide cuando se ejecuta es la recepcionista de Huellitas el dia que oprima 'Registrar mascota'.
  - Por eso el metodo que guarda la mascota nunca aparece llamado desde el main: aparece registrado, no llamado, y esa diferencia es la que hay que entender hoy.

**ActionListener es una interfaz de java.awt.event que tiene un solo... (1/2)** — 4 vinetas.
  - Con una de dos metodos no compila, y el mensaje del editor no lo dice con esas palabras y ahi adentro va su llamada.

**ActionListener es una interfaz de java.awt.event que tiene un solo... (2/2)** — 3 vinetas.

**Separar la logica de la interfaz significa que la ventana no conoce...** — 5 vinetas.
  - Separar la logica de la interfaz significa que la ventana no conoce reglas de negocio y que las reglas no saben que existe una ventana.
  - Si toca reescribir todo porque la conversion de la edad estaba adentro del boton, el diseño esta mal.

**Vale la pena desarmar en camara lenta lo que ocurre en un click de... (1/2)** — 3 vinetas.
  - Vale la pena desarmar en camara lenta lo que ocurre en un click de 'Registrar mascota'.
  - Cuarto, la vista atrapa esa excepcion y la convierte en un JOptionPane, o, si no hubo error, limpia los campos y refresca el area de listado.

**Vale la pena desarmar en camara lenta lo que ocurre en un click de... (2/2)** — 2 vinetas.

**Dos detalles mas que le van a servir (1/2)** — 3 vinetas.
  - Dos detalles mas que le van a servir.
  - Para eso existe SwingWorker.

**Dos detalles mas que le van a servir (2/2)** — 3 vinetas.

**class VetCareEventosDemo · main()** — 14 vinetas.

**VetCareEventosDemo.java — class Mascota** — 7 vinetas.

**VetCareEventosDemo.java — Mascota()** — 16 vinetas.

**VetCareEventosDemo.java — class RepositorioMascotas** — 4 vinetas.

**VetCareEventosDemo.java — registrar()** — 10 vinetas.

**VetCareEventosDemo.java — buscarPorId()** — 15 vinetas.

**VetCareEventosDemo.java — class ControladorRegistro** — 4 vinetas.

**VetCareEventosDemo.java — ControladorRegistro()** — 7 vinetas.

**VetCareEventosDemo.java — registrarMascota() (1/2)** — 20 vinetas.

**VetCareEventosDemo.java — registrarMascota() (2/2)** — 3 vinetas.

**VetCareEventosDemo.java — reporteListado()** — 11 vinetas.

**VetCareEventosDemo.java — class VentanaRegistroMascota** — 12 vinetas.

**VetCareEventosDemo.java — VentanaRegistroMascota() (1/2)** — 20 vinetas.

**VetCareEventosDemo.java — VentanaRegistroMascota() (2/2)** — 12 vinetas.

**VetCareEventosDemo.java — registrar()** — 13 vinetas.

**VetCareEventosDemo.java — limpiar()** — 9 vinetas.


**Demo que usted debe poder repetir:** El docente oprime el boton de la ventana ya corriendo y muestra en vivo como la mascota pasa del formulario al ArrayList, incluyendo que pasa cuando la edad se escribe como texto.

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
Demo: El docente oprime el boton de la ventana ya corriendo y muestra en vivo como la mascota pasa del formulario al ArrayList, incluyendo que pasa cuando la edad se escribe como texto.
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
