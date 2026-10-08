# Guion docente · Clase 3 · Pilas y colas · Stack y Queue

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** VetCare queda con la sala de espera modelada como cola FIFO y el historial de atenciones recientes como pila LIFO, ambas conectadas al registro de mascotas de la clase anterior.
- **Entregable de hoy:** Clases SalaDeEspera (Queue) e HistorialReciente (Deque como pila) integradas al proyecto VetCare, con una demo que atiende en orden de llegada las cuatro mascotas del escenario y deshace la ultima atencion registrada; comprimido y subido a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 3 - Pilas y colas/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Las ideas de cada concepto estan proyectadas y el desarrollo completo esta en las notas del presentador de su lamina. Aqui va, por lamina y en su orden, lo que hay que subrayar.

**[Slide 4] Cuando la lista permite demasiado** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Una estructura restrictiva como Queue no ofrece ese metodo; simplemente no existe en su contrato, entonces el error se vuelve imposible de escribir.
  - Subrayar: Esa es la idea grande de hoy: elegir la estructura mas limitada que resuelva el problema no es una limitacion tecnica, es una forma de blindar la regla del negocio dentro del tipo de dato.

**[Slide 5] La cola: FIFO con Queue** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: En VetCare usamos siempre offer/poll/peek porque avisan con false o con null en vez de reventar, y en una recepcion que puede quedar vacia a media manana eso es exactamente lo que queremos. peek es lo que alimenta la pantalla de turnos que ve el publico; poll es lo que hace el medico cuando abre la puerta del consultorio.

**[Slide 6] Turno: lo que guarda la cola** — programa completo (31 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 7] SalaDeEspera: offer y peek** — programa completo (40 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 8] atender(): poll sin sorpresas** — programa completo (39 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 9] La pila: LIFO con Deque** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Eso es literalmente como funciona el Ctrl+Z de cualquier programa.

**[Slide 10] HistorialReciente: push, peek y pop** — programa completo (38 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 11] La cola y la pila trabajando juntas** — programa completo (36 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 12] Por qué son rápidas: ArrayDeque y LinkedList** — 3 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Vale la pena entender por que estas estructuras son rapidas, porque ahi esta el argumento tecnico y no solo el pedagogico.
  - Subrayar: Por eso agregar y sacar por cualquiera de los dos extremos cuesta tiempo constante.
  - Subrayar: La estructura correcta no solo previene errores de negocio, tambien evita que el programa se arrastre.

**[Slide 13] Una cola no se recorre para buscar** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Ademas, recorrer una cola con for-each la muestra pero no la consume; muchos estudiantes imprimen la cola con un for-each, ven todos los turnos y creen que ya los atendieron, cuando en realidad size() sigue igual.

**[Slide 14] La urgencia entra con addFirst** — programa completo (35 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

## Errores tipicos del docente que no domina el tema

Material de preparacion: no se proyecta.

- Error tipico del docente que no domina el tema: escribir Queue<Turno> sala = new Queue<>() y quedarse en blanco cuando VS Code subraya la linea, sin poder explicar que Queue es una interfaz y que necesita una implementacion concreta como LinkedList o ArrayDeque. El segundo clasico es usar la clase Stack solamente porque es la primera que aparece en Google, y no poder responder cuando un estudiante pregunta por que la documentacion recomienda ArrayDeque. El tercero, muy frecuente, es confundir peek con poll durante la demo: el docente llama a peek dentro de un while creyendo que va a vaciar la cola y arma un ciclo infinito en plena clase. El cuarto es llamar pop() sobre una pila vacia sin validar isEmpty(), que con ArrayDeque lanza NoSuchElementException y con Stack lanza EmptyStackException; hay que mostrar esa excepcion a proposito y envolverla en try-catch, porque el PI exige manejo de errores. Ensaye los cuatro casos antes de entrar al salon para que cada mensaje rojo sea una leccion planeada y no una sorpresa.


**Demo que usted debe poder repetir:** El docente encola cuatro mascotas, muestra en pantalla la diferencia entre peek() y poll() atendiendo en orden de llegada, y luego usa push/pop para deshacer la ultima atencion registrada.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare queda con la sala de espera modelada como cola FIFO y el historial de atenciones recientes como pila LIFO, ambas conectadas al registro de mascotas de la clase anterior.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de concepto y en las de codigo
(lo que hay que subrayar esta tambien en las notas del presentador de cada lamina). Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente encola cuatro mascotas, muestra en pantalla la diferencia entre peek() y poll() atendiendo en orden de llegada, y luego usa push/pop para deshacer la ultima atencion registrada.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 3/Codigo/ClinicaSalaDeEspera.java`

### 60-105 · Taller guiado (opcional) = avance del PI
Opcional: no tiene lamina en el deck. La guia esta en
`Clases/Clase 3 - Pilas y colas/Taller PI - Clase 3 - VetCare.docx`; si hoy no se hace, se extiende la demo y la practica libre.
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Cree la clase Turno con id, nombre de la mascota, nombre del dueno y motivo de consulta, mas sus getters y su toString(); verifique imprimiendo un turno suelto en consola antes de meterlo en cualquier estructura.
2. Cree la clase SalaDeEspera con el atributo private final Queue<Turno> cola = new LinkedList<>(); y los metodos registrarLlegada(Turno t) usando offer, siguienteEnPantalla() usando peek y atender() usando poll; verifique que despues de registrar cuatro llegadas y llamar dos veces a siguienteEnPantalla(), cantidad() sigue siendo 4.
3. Haga que atender() valide la cola vacia con isEmpty() y devuelva un mensaje controlado en vez de un null suelto; verifique llamando a atender() cinco veces cuando solo hay cuatro turnos y confirmando que la quinta llamada imprime que la sala esta vacia y el programa no se cae.
4. Cree la clase HistorialReciente con private final Deque<String> pila = new ArrayDeque<>(); y los metodos registrar(String), ultimaAtencion() con peek y deshacer() con pop protegido por isEmpty(); verifique que despues de atender a Firulais, Michi y Rocky, ultimaAtencion() muestra a Rocky y deshacer() lo retira dejando a Michi arriba.
5. Conecte las dos estructuras en un main: cada vez que atender() saca un turno de la cola, registre automaticamente esa consulta en la pila; ejecute el flujo completo con las cuatro mascotas del escenario mas la urgencia de Canela agregada con addFirst sobre un Deque, capture la consola y suba el proyecto a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Clases SalaDeEspera (Queue) e HistorialReciente (Deque como pila) integradas al proyecto VetCare, con una demo que atiende en orden de llegada las cuatro mascotas del escenario y deshace la ultima atencion registrada; comprimido y subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Si hubo taller, repasar los criterios de exito del `Taller PI - Clase 3 - VetCare.docx` (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 3/Quiz Clase 3 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare queda con la sala de espera modelada como cola FIFO y el historial de atenciones recientes como pila LIFO, ambas conectadas al registro de mascotas de la clase anterior.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 3/Solucion Taller Clase 3 - VetCare.docx` — no proyectar completa.
