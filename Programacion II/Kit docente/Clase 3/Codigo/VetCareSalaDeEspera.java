package vetcare;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

/**
 * VetCare - Clase 3: sala de espera (cola FIFO) e historial reciente (pila LIFO).
 * Clinica Veterinaria Huellitas.
 * Archivo unico: clic derecho sobre el archivo > Run File (Shift+F6) en NetBeans.
 */
public class VetCareSalaDeEspera {

    public static void main(String[] args) {

        SalaDeEspera sala = new SalaDeEspera();
        HistorialReciente historial = new HistorialReciente();

        System.out.println("=== 1. Llegadas a recepcion (offer = al final) ===");
        sala.registrarLlegada(new Turno("M-001", "Firulais", "Ana Gomez", "Vacuna"));
        sala.registrarLlegada(new Turno("M-002", "Michi", "Luis Perez", "Control"));
        sala.registrarLlegada(new Turno("M-003", "Rocky", "Ana Gomez", "Revision de patas"));
        sala.registrarLlegada(new Turno("M-004", "Nieve", "Sara Diaz", "Desparasitacion"));
        System.out.println("En espera: " + sala.cantidad());
        System.out.println("Pantalla de turnos (peek): " + sala.siguienteEnPantalla());
        System.out.println("Despues del peek siguen en espera: " + sala.cantidad());

        System.out.println();
        System.out.println("=== 2. El consultorio atiende (poll = saca el primero) ===");
        while (!sala.estaVacia()) {
            Turno t = sala.atender(); // dentro del while nunca es null
            historial.registrar("Consulta de " + t.getNombre() + " (" + t.getId() + ")");
        }
        sala.atender(); // sala vacia: mensaje controlado, sin excepcion

        System.out.println();
        System.out.println("=== 3. Historial reciente (LIFO) ===");
        System.out.println("Ultimo movimiento (peek): " + historial.ultimaAtencion());
        System.out.println(historial.deshacer());
        System.out.println("Ahora el ultimo es: " + historial.ultimaAtencion());
        System.out.println("Movimientos guardados: " + historial.cantidad());

        System.out.println();
        System.out.println("=== 4. Pila vacia: se valida, no se revienta ===");
        while (historial.cantidad() > 0) {
            System.out.println(historial.deshacer());
        }
        System.out.println("Intento extra -> " + historial.deshacer());

        System.out.println();
        System.out.println("=== 5. Urgencia: pasa de primera, con nombre propio ===");
        Deque<Turno> filaConUrgencias = new ArrayDeque<>();
        filaConUrgencias.addLast(new Turno("M-004", "Nieve", "Sara Diaz", "Desparasitacion"));
        filaConUrgencias.addLast(new Turno("M-005", "Toby", "Sara Diaz", "Control"));
        filaConUrgencias.addFirst(new Turno("M-009", "Canela", "Ana Gomez", "URGENCIA"));
        while (!filaConUrgencias.isEmpty()) {
            System.out.println("Pasa: " + filaConUrgencias.pollFirst());
        }
    }
}

class Turno {

    private final String id;
    private final String nombre;
    private final String dueno;
    private final String motivo;

    public Turno(String id, String nombre, String dueno, String motivo) {
        this.id = id;
        this.nombre = nombre;
        this.dueno = dueno;
        this.motivo = motivo;
    }

    public String getId() { return id; }
    public String getNombre() { return nombre; }
    public String getDueno() { return dueno; }
    public String getMotivo() { return motivo; }

    @Override
    public String toString() {
        return nombre + " (" + id + ") - " + motivo + " | dueno: " + dueno;
    }
}

/** Sala de espera: FIFO puro. No expone la cola, solo las operaciones del negocio. */
class SalaDeEspera {

    private final Queue<Turno> cola = new LinkedList<>(); // Queue es interfaz

    public int registrarLlegada(Turno t) {
        cola.offer(t); // offer = agregar al final
        System.out.println("Llega " + t.getNombre() + " -> turno numero " + cola.size());
        return cola.size();
    }

    public Turno siguienteEnPantalla() {
        return cola.peek(); // MIRA el primero: el tamano no cambia
    }

    public Turno atender() {
        if (cola.isEmpty()) {
            System.out.println("Sala de espera vacia: no hay a quien atender");
            return null;
        }
        Turno t = cola.poll(); // SACA el primero
        System.out.println("Pasa a consultorio: " + t);
        return t;
    }

    public boolean estaVacia() {
        return cola.isEmpty();
    }

    public int cantidad() {
        return cola.size();
    }
}

/** Historial reciente: LIFO. Deque usado como pila (moderna, mejor que Stack). */
class HistorialReciente {

    private final Deque<String> pila = new ArrayDeque<>();

    public void registrar(String consulta) {
        pila.push(consulta); // push = poner encima
        System.out.println("Historial <- " + consulta);
    }

    public String ultimaAtencion() {
        return pila.isEmpty() ? "(sin movimientos)" : pila.peek();
    }

    public String deshacer() {
        if (pila.isEmpty()) {
            return "Nada que deshacer"; // nunca se llama pop() sin preguntar por isEmpty()
        }
        return "Se deshizo: " + pila.pop();
    }

    public int cantidad() {
        return pila.size();
    }
}
