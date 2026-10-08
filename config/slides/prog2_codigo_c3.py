# -*- coding: utf-8 -*-
"""Programacion II · Clase 3 · laminas de codigo: cada una es un Main.java que corre solo."""

CLASE = 3

LAMINAS = [
    {"k": 1, "titulo": "Turno: lo que guarda la cola", "codigo": r"""
class Main {
    public static void main(String[] args) {
        Turno t = new Turno("M-001", "Firulais",
                "Ana Gomez", "Vacuna");
        System.out.println(t);
        System.out.println("Motivo: " + t.getMotivo());
    }
}

class Turno {
    private final String id;
    private final String nombre;
    private final String dueno;
    private final String motivo;

    public Turno(String id, String nombre,
            String dueno, String motivo) {
        this.id = id;
        this.nombre = nombre;
        this.dueno = dueno;
        this.motivo = motivo;
    }

    public String getMotivo() { return motivo; }

    @Override
    public String toString() {
        return nombre + " (" + id + ") - " + motivo
                + " | dueno: " + dueno;
    }
}
""", "salida": """
Firulais (M-001) - Vacuna | dueno: Ana Gomez
Motivo: Vacuna
"""},

    {"k": 1, "titulo": "SalaDeEspera: offer y peek", "codigo": r"""
import java.util.LinkedList;
import java.util.Queue;

class Main {
    public static void main(String[] args) {
        SalaDeEspera sala = new SalaDeEspera();
        sala.registrarLlegada(new Turno("Firulais"));
        sala.registrarLlegada(new Turno("Michi"));
        System.out.println("Pantalla (peek): "
                + sala.siguienteEnPantalla());
        System.out.println("Siguen en espera: "
                + sala.cantidad());
    }
}

class Turno {
    private final String nombre;
    public Turno(String nombre) { this.nombre = nombre; }
    public String getNombre() { return nombre; }
    @Override
    public String toString() { return nombre; }
}

class SalaDeEspera {
    // Queue es interfaz
    private final Queue<Turno> cola = new LinkedList<>();

    public int registrarLlegada(Turno t) {
        cola.offer(t); // offer = agregar al final
        System.out.println("Llega " + t.getNombre()
                + " -> turno numero " + cola.size());
        return cola.size();
    }

    public Turno siguienteEnPantalla() {
        return cola.peek(); // MIRA el primero
    }

    public int cantidad() { return cola.size(); }
}
""", "salida": """
Llega Firulais -> turno numero 1
Llega Michi -> turno numero 2
Pantalla (peek): Firulais
Siguen en espera: 2
"""},

    {"k": 1, "titulo": "atender(): poll sin sorpresas", "codigo": r"""
import java.util.LinkedList;
import java.util.Queue;

class Main {
    public static void main(String[] args) {
        SalaDeEspera sala = new SalaDeEspera();
        sala.cola.offer(new Turno("Firulais"));
        sala.cola.offer(new Turno("Michi"));
        while (!sala.estaVacia()) {
            sala.atender(); // en el while nunca es null
        }
        sala.atender(); // sala vacia: sin excepcion
    }
}

class Turno {
    private final String nombre;
    public Turno(String nombre) { this.nombre = nombre; }
    @Override
    public String toString() { return nombre; }
}

class SalaDeEspera {
    final Queue<Turno> cola = new LinkedList<>();

    public Turno atender() {
        if (cola.isEmpty()) {
            System.out.println("Sala vacia: nadie");
            return null;
        }
        Turno t = cola.poll(); // SACA el primero
        System.out.println("Pasa a consultorio: " + t);
        return t;
    }

    public boolean estaVacia() {
        return cola.isEmpty();
    }
}
""", "salida": """
Pasa a consultorio: Firulais
Pasa a consultorio: Michi
Sala vacia: nadie
"""},

    {"k": 2, "titulo": "HistorialReciente: push, peek y pop", "codigo": r"""
import java.util.ArrayDeque;
import java.util.Deque;

class Main {
    public static void main(String[] args) {
        HistorialReciente h = new HistorialReciente();
        h.registrar("Consulta de Firulais");
        h.registrar("Consulta de Michi");
        System.out.println("Ultimo: " + h.ultimaAtencion());
        System.out.println(h.deshacer());
        System.out.println(h.deshacer());
        System.out.println(h.deshacer()); // pila vacia
        System.out.println("Ultimo: " + h.ultimaAtencion());
    }
}

// Deque usado como pila (moderna, mejor que Stack)
class HistorialReciente {
    private final Deque<String> pila = new ArrayDeque<>();

    public void registrar(String consulta) {
        pila.push(consulta); // push = poner encima
        System.out.println("Historial <- " + consulta);
    }

    public String ultimaAtencion() {
        return pila.isEmpty()
                ? "(sin movimientos)" : pila.peek();
    }

    public String deshacer() {
        if (pila.isEmpty()) {
            // nunca pop() sin preguntar por isEmpty()
            return "Nada que deshacer";
        }
        return "Se deshizo: " + pila.pop();
    }
}
""", "salida": """
Historial <- Consulta de Firulais
Historial <- Consulta de Michi
Ultimo: Consulta de Michi
Se deshizo: Consulta de Michi
Se deshizo: Consulta de Firulais
Nada que deshacer
Ultimo: (sin movimientos)
"""},

    {"k": 2, "titulo": "La cola y la pila trabajando juntas", "codigo": r"""
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

class Main {
    public static void main(String[] args) {
        Queue<Turno> sala = new LinkedList<>(); // FIFO
        Deque<String> historial = new ArrayDeque<>();//LIFO
        sala.offer(new Turno("M-001", "Firulais"));
        sala.offer(new Turno("M-002", "Michi"));
        sala.offer(new Turno("M-003", "Rocky"));

        System.out.println("=== El consultorio ===");
        while (!sala.isEmpty()) {
            Turno t = sala.poll(); // aqui nunca es null
            System.out.println("Pasa: " + t.getNombre());
            historial.push("Consulta de " + t.getNombre()
                    + " (" + t.getId() + ")");
        }
        System.out.println("Ultimo: " + historial.peek());
        System.out.println("Movimientos: "
                + historial.size());
    }
}

class Turno {
    private final String id;
    private final String nombre;
    public Turno(String id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }
    public String getId() { return id; }
    public String getNombre() { return nombre; }
}
""", "salida": """
=== El consultorio ===
Pasa: Firulais
Pasa: Michi
Pasa: Rocky
Ultimo: Consulta de Rocky (M-003)
Movimientos: 3
"""},

    {"k": 4, "titulo": "La urgencia entra con addFirst", "codigo": r"""
import java.util.ArrayDeque;
import java.util.Deque;

class Main {
    public static void main(String[] args) {
        Deque<Turno> filaConUrgencias = new ArrayDeque<>();
        filaConUrgencias.addLast(
                new Turno("M-004", "Nieve", "Vacuna"));
        filaConUrgencias.addLast(
                new Turno("M-005", "Toby", "Control"));
        filaConUrgencias.addFirst(
                new Turno("M-009", "Canela", "URGENCIA"));
        while (!filaConUrgencias.isEmpty()) {
            System.out.println("Pasa: "
                    + filaConUrgencias.pollFirst());
        }
    }
}

class Turno {
    private final String id;
    private final String nombre;
    private final String motivo;

    public Turno(String id, String nombre, String motivo) {
        this.id = id;
        this.nombre = nombre;
        this.motivo = motivo;
    }

    @Override
    public String toString() {
        return nombre + " (" + id + ") - " + motivo;
    }
}
""", "salida": """
Pasa: Canela (M-009) - URGENCIA
Pasa: Nieve (M-004) - Vacuna
Pasa: Toby (M-005) - Control
"""},
]
