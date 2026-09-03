# Guion docente · Clase 3 · Pilas y colas · Stack y Queue

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** VetCare queda con la sala de espera modelada como cola FIFO y el historial de atenciones recientes como pila LIFO, ambas conectadas al registro de mascotas de la clase anterior.
- **Entregable de hoy:** Clases SalaDeEspera (Queue) e HistorialReciente (Deque como pila) integradas al proyecto VetCare, con una demo que atiende en orden de llegada las cuatro mascotas del escenario y deshace la ultima atencion registrada; comprimido y subido a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 3 - Pilas y colas/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

La clase pasada nos dio un ArrayList, que es una herramienta poderosa justamente porque permite todo: agregar al final, insertar en la mitad, sacar de cualquier posicion, reordenar. Ese poder es un problema cuando lo que usted esta modelando tiene reglas. La sala de espera de Huellitas tiene una regla sagrada: el que llega primero pasa primero. Si la sala de espera es un ArrayList, cualquier programador del equipo (o usted mismo a las once de la noche) puede escribir salaEspera.add(0, mascotaDelAmigo) y colar a alguien sin que nada falle: compila, corre y la clinica pierde la confianza de sus clientes. Una estructura restrictiva como Queue no ofrece ese metodo; simplemente no existe en su contrato, entonces el error se vuelve imposible de escribir. Esa es la idea grande de hoy: elegir la estructura mas limitada que resuelva el problema no es una limitacion tecnica, es una forma de blindar la regla del negocio dentro del tipo de dato.

La cola, o Queue, funciona con disciplina FIFO: First In, First Out, el primero que entra es el primero que sale, igual que la fila del banco. En Java, Queue es una interfaz, no una clase, asi que se declara Queue<Turno> salaEspera = new LinkedList<>(); o new ArrayDeque<>(); intentar new Queue<>() no compila y ese es el primer error que veremos en pantalla. La cola tiene tres operaciones utiles y cada una viene en dos sabores: offer(x) agrega al final y devuelve false si no cabe (la version add lanza IllegalStateException en ese caso), poll() saca y devuelve el primero o null si esta vacia (la version remove lanza NoSuchElementException), y peek() mira el primero sin sacarlo o devuelve null (la version element tambien lanza excepcion). En VetCare usamos siempre offer/poll/peek porque avisan con false o con null en vez de reventar, y en una recepcion que puede quedar vacia a media manana eso es exactamente lo que queremos. peek es lo que alimenta la pantalla de turnos que ve el publico; poll es lo que hace el medico cuando abre la puerta del consultorio.

La pila, o Stack, funciona al reves: LIFO, Last In, First Out, como la pila de historias clinicas sobre el escritorio, donde uno siempre coge la de encima. Sus operaciones son push(x) para poner encima, pop() para sacar el de encima y peek() para mirarlo sin sacarlo. Java trae una clase llamada Stack, pero es codigo de 1995: hereda de Vector, esta sincronizada (lo que la hace mas lenta sin necesidad) y permite acceder por indice, con lo cual rompe la propia restriccion que dice defender. La practica actual es usar Deque<String> historial = new ArrayDeque<>(); y llamarle push/pop/peek, que es exactamente la misma API pero sobre una implementacion moderna. En VetCare la pila guarda el historial de atenciones recientes: cada consulta terminada se apila, la pantalla del medico muestra siempre la de encima con peek, y si registro una atencion por equivocacion, pop la deshace. Eso es literalmente como funciona el Ctrl+Z de cualquier programa.

Vale la pena entender por que estas estructuras son rapidas, porque ahi esta el argumento tecnico y no solo el pedagogico. ArrayDeque es un arreglo circular con dos punteros, uno al frente y otro al final: cuando usted saca del frente no mueve ni un elemento, solo corre el puntero, y cuando el puntero llega al final del arreglo da la vuelta al inicio. Por eso agregar y sacar por cualquiera de los dos extremos cuesta tiempo constante. LinkedList, en cambio, es una cadena de nodos donde cada nodo apunta al siguiente y al anterior, asi que sacar el primero es simplemente mover la cabeza de la cadena. Compare eso con usar un ArrayList como cola: mascotas.remove(0) obliga a desplazar todos los elementos restantes un puesto hacia la izquierda, lo que en una jornada de 300 turnos significa decenas de miles de movimientos innecesarios. La estructura correcta no solo previene errores de negocio, tambien evita que el programa se arrastre.

Un punto que confunde mucho: una cola no se recorre para buscar. Si usted se descubre iterando la sala de espera para encontrar a Firulais y sacarlo del medio, la senal es que ese caso de uso no es una cola pura, y que necesita otra estructura al lado (por ejemplo un Deque que permita addFirst para urgencias, o un HashMap que veremos la proxima clase). En VetCare resolvemos la urgencia sin traicionar el modelo: usamos Deque<Turno> y decimos addLast para el que llega normal y addFirst para el caso critico, dejando explicito en el codigo que colarse es una operacion excepcional y con nombre propio, no un accidente. Ademas, recorrer una cola con for-each la muestra pero no la consume; muchos estudiantes imprimen la cola con un for-each, ven todos los turnos y creen que ya los atendieron, cuando en realidad size() sigue igual. Consumir es poll; mirar es peek o for-each.

Error tipico del docente que no domina el tema: escribir Queue<Turno> sala = new Queue<>() y quedarse en blanco cuando VS Code subraya la linea, sin poder explicar que Queue es una interfaz y que necesita una implementacion concreta como LinkedList o ArrayDeque. El segundo clasico es usar la clase Stack solamente porque es la primera que aparece en Google, y no poder responder cuando un estudiante pregunta por que la documentacion recomienda ArrayDeque. El tercero, muy frecuente, es confundir peek con poll durante la demo: el docente llama a peek dentro de un while creyendo que va a vaciar la cola y arma un ciclo infinito en plena clase. El cuarto es llamar pop() sobre una pila vacia sin validar isEmpty(), que con ArrayDeque lanza NoSuchElementException y con Stack lanza EmptyStackException; hay que mostrar esa excepcion a proposito y envolverla en try-catch, porque el PI exige manejo de errores. Ensaye los cuatro casos antes de entrar al salon para que cada mensaje rojo sea una leccion planeada y no una sorpresa.

**Demo que usted debe poder repetir:** El docente encola cuatro mascotas, muestra en pantalla la diferencia entre peek() y poll() atendiendo en orden de llegada, y luego usa push/pop para deshacer la ultima atencion registrada.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare queda con la sala de espera modelada como cola FIFO y el historial de atenciones recientes como pila LIFO, ambas conectadas al registro de mascotas de la clase anterior.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente encola cuatro mascotas, muestra en pantalla la diferencia entre peek() y poll() atendiendo en orden de llegada, y luego usa push/pop para deshacer la ultima atencion registrada.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 3/Codigo/VetCareSalaDeEspera.java`

### 60-105 · Taller guiado = avance del PI
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
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 3/Quiz Clase 3 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare queda con la sala de espera modelada como cola FIFO y el historial de atenciones recientes como pila LIFO, ambas conectadas al registro de mascotas de la clase anterior.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 3/Solucion Taller Clase 3 - VetCare.docx` — no proyectar completa.
