# -*- coding: utf-8 -*-
"""Programacion II · Clase 8 · laminas de codigo: cada una es un Main.java que corre solo."""

CLASE = 8

LAMINAS = [
    {"k": 1, "titulo": "Javadoc de un constructor", "codigo": r"""
class Main {
    public static void main(String[] args) {
        Mascota kira = new Mascota("M-001", "Kira", true);
        System.out.println(kira.getNombre() + " activa? " + kira.estaActiva());
    }
}
class Mascota {
    private final String id;
    private final String nombre;
    private boolean activa;
    /**
     * Crea el expediente de una mascota.
     *
     * @param id identificador unico del expediente, por ejemplo M-001
     * @param nombre nombre con el que el dueno reconoce a la mascota
     * @param activa true si la mascota esta habilitada para agendar citas
     */
    public Mascota(String id, String nombre, boolean activa) {
        this.id = id;
        this.nombre = nombre;
        this.activa = activa;
    }
    public String getNombre() { return nombre; }
    public boolean estaActiva() { return activa; }
}
""", "salida": """
Kira activa? true
"""},

    {"k": 1, "titulo": "El contrato de agendar(), en Javadoc", "codigo": r"""
import java.util.HashMap;
import java.util.NoSuchElementException;
class Main {
    public static void main(String[] args) {
        AgendaService agenda = new AgendaService();
        agenda.registrar("M-001", true);
        Cita c =
                agenda.agendar("M-001", "2026-09-30 10:00");
        System.out.println("Cita: " + c.getFechaHora());
    }
}
class Cita {
    private final String fechaHora;
    Cita(String fechaHora) { this.fechaHora = fechaHora; }
    String getFechaHora() { return fechaHora; }
}
class AgendaService {
    HashMap<String, Boolean> activas = new HashMap<>();
    void registrar(String id, boolean activa) {
        activas.put(id, activa);
    }

    /**
     * Agenda una cita para una mascota registrada y activa.
     * Si esta inactiva no se crea ninguna cita.
     * @param idMascota expediente, por ejemplo M-001
     * @param fechaHora fecha y hora yyyy-MM-dd HH:mm
     * @return la cita creada
     * @throws IllegalArgumentException si la fecha y hora
     *         vienen vacias
     * @throws NoSuchElementException si no existe
     *         expediente con ese identificador
     * @throws IllegalStateException si la mascota esta
     *         inactiva
     */
    public Cita agendar(String idMascota,
            String fechaHora) {
        if (fechaHora == null || fechaHora.isBlank())
            throw new IllegalArgumentException("Sin fecha");
        Boolean activa = activas.get(idMascota);
        if (activa == null)
            throw new NoSuchElementException(idMascota);
        if (!activa)
            throw new IllegalStateException("Inactiva");
        return new Cita(fechaHora);
    }
}
""", "salida": """
Cita: 2026-09-30 10:00
"""},

    {"k": 1, "titulo": "agendar(): cada @throws en el código", "codigo": r"""
import java.util.HashMap;
import java.util.NoSuchElementException;
class Main {
    static AgendaService agenda = new AgendaService();
    public static void main(String[] args) {
        Mascota rocky = new Mascota("Rocky", false);
        agenda.registrar("M-009", rocky);
        probar("M-009", "  ");
        probar("M-777", "2026-09-30 10:00");
        probar("M-009", "2026-09-30 10:00");
    }
    static void probar(String id, String fechaHora) {
        try {
            agenda.agendar(id, fechaHora);
        } catch (RuntimeException e) {
            System.out.println(e);
        }
    }
}
class AgendaService {
    HashMap<String, Mascota> expedientes = new HashMap<>();
    void registrar(String id, Mascota m) {
        expedientes.put(id, m);
    }

    public void agendar(String idMascota,
            String fechaHora) {
        if (fechaHora == null || fechaHora.isBlank())
            throw new IllegalArgumentException(
                    "La fecha y hora son obligatorias.");
        Mascota mascota = expedientes.get(idMascota);
        if (mascota == null)
            throw new NoSuchElementException("No existe "
                    + "expediente con ID " + idMascota);
        if (!mascota.estaActiva())
            throw new IllegalStateException("La mascota "
                    + mascota.getNombre()
                    + " esta inactiva.");
    }
}
class Mascota {
    private final String nombre;
    private final boolean activa;
    Mascota(String nombre, boolean activa) {
        this.nombre = nombre; this.activa = activa;
    }
    String getNombre() { return nombre; }
    boolean estaActiva() { return activa; }
}
""", "salida": """
java.lang.IllegalArgumentException: La fecha y hora son obligatorias.
java.util.NoSuchElementException: No existe expediente con ID M-777
java.lang.IllegalStateException: La mascota Rocky esta inactiva.
"""},

    {"k": 3, "titulo": "nuevaAgenda(): el mismo estado de partida", "codigo": r"""
import java.util.ArrayList;
import java.util.List;
class Main {
    /**
     * Prepara el mismo estado inicial para cada caso:
     * equivale a {@code @Before} en JUnit.
     *
     * @return agenda con Kira y Michi activas, Rocky no
     */
    private static AgendaService nuevaAgenda() {
        AgendaService agenda = new AgendaService();
        agenda.registrarMascota(
                new Mascota("M-001", "Kira", true));
        agenda.registrarMascota(
                new Mascota("M-002", "Michi", true));
        agenda.registrarMascota(
                new Mascota("M-009", "Rocky", false));
        return agenda;
    }

    public static void main(String[] args) {
        AgendaService agenda = nuevaAgenda();
        agenda.agendar("M-001", "2026-09-30 10:00");
        System.out.println("Caso 1 deja citas: "
                + agenda.totalCitas());
        agenda = nuevaAgenda();
        System.out.println("Caso 2 parte con: "
                + agenda.totalCitas());
    }
}
class Mascota {
    private final String id, nombre;
    private final boolean activa;
    Mascota(String id, String nombre, boolean activa) {
        this.id = id; this.nombre = nombre;
        this.activa = activa;
    }
}
class AgendaService {
    private List<Mascota> expedientes = new ArrayList<>();
    private List<String> citas = new ArrayList<>();
    void registrarMascota(Mascota m) { expedientes.add(m); }
    void agendar(String id, String f) { citas.add(f); }
    int totalCitas() { return citas.size(); }
}
""", "salida": """
Caso 1 deja citas: 1
Caso 2 parte con: 0
"""},

    {"k": 3, "titulo": "Caso positivo y caso negativo", "codigo": r"""
import java.util.HashMap;

class Main {
    public static void main(String[] args) {
        AgendaService agenda = nuevaAgenda();
        Cita cita =
                agenda.agendar("M-001", "2026-09-30 10:00");
        verificar("agendar_mascotaActiva_creaLaCita",
                cita != null && agenda.totalCitas() == 1);
        agenda = nuevaAgenda();
        try {
            agenda.agendar("M-009", "2026-09-30 10:00");
            verificar("agendar_mascotaInactiva_lanza",
                    false);
        } catch (IllegalStateException e) {
            verificar("agendar_mascotaInactiva_lanza",
                    agenda.totalCitas() == 0);
        }
    }
    static AgendaService nuevaAgenda() {
        AgendaService a = new AgendaService();
        a.registrar("M-001", true);
        a.registrar("M-009", false);
        return a;
    }

    static void verificar(String caso, boolean paso) {
        String marca = paso ? "[OK]    " : "[FALLA] ";
        System.out.println(marca + caso);
    }
}
class Cita { }
class AgendaService {
    HashMap<String, Boolean> activas = new HashMap<>();
    private int citas = 0;
    void registrar(String id, boolean activa) {
        activas.put(id, activa);
    }
    Cita agendar(String idMascota, String fechaHora) {
        if (!activas.get(idMascota))
            throw new IllegalStateException("Inactiva");
        citas++;
        return new Cita();
    }
    int totalCitas() { return citas; }
}
""", "salida": """
[OK]    agendar_mascotaActiva_creaLaCita
[OK]    agendar_mascotaInactiva_lanza
"""},
]
