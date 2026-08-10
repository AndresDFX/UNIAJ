# Solucion Taller · Clase 3 · Pilas y colas · Stack y Queue

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

## Solucion paso a paso
1. Paso 1 resuelto: Turno se construye igual que Mascota, con atributos private final String id, nombre, dueno y motivo, constructor completo, getters y toString del estilo return nombre + " (" + id + ") - " + motivo + " | dueno: " + dueno; Tener toString desde el principio es lo que hace legible toda la demo de colas, porque cada poll imprime una linea entendible en vez de vetcare.Turno@3f2a1b.
2. Paso 2 resuelto: dentro de SalaDeEspera se declara private final Queue<Turno> cola = new LinkedList<>(); a la izquierda va la interfaz Queue porque es la que define el contrato FIFO, y a la derecha LinkedList porque Queue es interfaz y no se puede instanciar. registrarLlegada hace cola.offer(t) y devuelve cola.size() para informarle al dueno que numero de turno le toco. siguienteEnPantalla hace return cola.peek(), que devuelve la referencia al primero sin retirarlo; por eso el tamano no cambia, y ese es el metodo que alimentaria un JLabel de la pantalla de turnos en la Clase 4.
3. Paso 3 resuelto: atender queda asi: if (cola.isEmpty()) { System.out.println("Sala de espera vacia: no hay a quien atender"); return null; } Turno t = cola.poll(); System.out.println("Pasa a consultorio: " + t); return t; Validar con isEmpty antes de sacar es la version defensiva y explicita; la alternativa es llamar directamente a poll y comparar el resultado con null, porque poll no lanza excepcion, a diferencia de remove(). Lo que nunca se debe hacer es llamar remove() a ciegas: con la sala vacia lanza NoSuchElementException y tumba el programa delante del cliente.
4. Paso 4 resuelto: la pila se declara private final Deque<String> pila = new ArrayDeque<>(); y no con la clase Stack, que hereda de Vector y esta sincronizada sin necesidad. registrar(String consulta) hace pila.push(consulta), que inserta arriba; ultimaAtencion hace return pila.isEmpty() ? "(sin movimientos)" : pila.peek(); y deshacer hace if (pila.isEmpty()) return "Nada que deshacer"; else return "Se deshizo: " + pila.pop(); Como push mete arriba y pop saca de arriba, el ultimo registrado es siempre el primero en salir: eso es LIFO, y es exactamente el comportamiento de un Ctrl+Z.
5. Paso 5 resuelto: en el main se conectan las dos estructuras con while (!sala.estaVacia()) { Turno t = sala.atender(); historial.registrar("Consulta de " + t.getNombre() + " (" + t.getId() + ")"); } Como la condicion del while ya garantizo que la cola no esta vacia, t nunca es null dentro del ciclo. Para la urgencia se usa Deque<Turno> filaConUrgencias = new ArrayDeque<>(); con addLast(nieve) y addLast(toby) para las llegadas normales y addFirst(canela) para la urgencia; se vacia con pollFirst(). Nombrar la operacion addFirst deja escrito en el codigo que ese salto de fila es una excepcion autorizada del negocio y no un descuido del programador.

## Rubrica corta
- [ ] Clase Turno completa con toString y clase SalaDeEspera con Queue correctamente declarada (2)
- [ ] Uso correcto de offer, peek y poll con la diferencia entre mirar y sacar demostrada en consola (3)
- [ ] HistorialReciente con Deque usado como pila y deshacer funcionando (3)
- [ ] Manejo de cola y pila vacias con mensaje controlado, mas evidencia subida a ExamLab (2)

## Errores frecuentes
- Escribir Queue<Turno> cola = new Queue<>(), que no compila porque Queue es una interfaz y necesita una implementacion como LinkedList o ArrayDeque.
- Usar peek() dentro del while que debe vaciar la cola, generando un ciclo infinito porque el elemento nunca se retira.
- Llamar a pop() o remove() sobre una estructura vacia sin validar isEmpty(), lo que lanza NoSuchElementException o EmptyStackException y tumba el programa.

Codigo de apoyo: `Kit docente/Clase 3/Codigo/VetCareSalaDeEspera.java`