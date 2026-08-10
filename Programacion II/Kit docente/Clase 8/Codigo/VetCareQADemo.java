package vetcare.qa;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.NoSuchElementException;

/**
 * Clase 8 de VetCare: dominio documentado con Javadoc y su bateria de casos de prueba.
 * Este archivo se ejecuta sin librerias externas: el metodo main corre los mismos casos
 * que despues se escriben con JUnit (ver el bloque comentado al final del archivo).
 *
 * @author Equipo VetCare
 * @version 1.0
 */
public class VetCareQADemo {

    private static int aprobadas = 0;
    private static int fallidas = 0;

    public static void main(String[] args) {
        AgendaService agenda = nuevaAgenda();
        Cita cita = agenda.agendar("M-001", "2026-09-30 10:00");
        verificar("agendar_mascotaActiva_creaLaCita", cita != null && agenda.totalCitas() == 1);

        agenda = nuevaAgenda();
        try {
            agenda.agendar("M-009", "2026-09-30 10:00");
            verificar("agendar_mascotaInactiva_lanzaIllegalStateException", false);
        } catch (IllegalStateException e) {
            verificar("agendar_mascotaInactiva_lanzaIllegalStateException", agenda.totalCitas() == 0);
        }

        agenda = nuevaAgenda();
        try {
            agenda.agendar("M-777", "2026-09-30 10:00");
            verificar("agendar_idInexistente_lanzaNoSuchElementException", false);
        } catch (NoSuchElementException e) {
            verificar("agendar_idInexistente_lanzaNoSuchElementException", agenda.totalCitas() == 0);
        }

        agenda = nuevaAgenda();
        agenda.agendar("M-001", "2026-09-30 10:00");
        try {
            agenda.agendar("M-002", "2026-09-30 10:00");
            verificar("agendar_horarioOcupado_noDuplicaLaCita", false);
        } catch (IllegalStateException e) {
            verificar("agendar_horarioOcupado_noDuplicaLaCita", agenda.totalCitas() == 1);
        }

        agenda = nuevaAgenda();
        try {
            agenda.agendar("M-001", "   ");
            verificar("agendar_fechaVacia_lanzaIllegalArgumentException", false);
        } catch (IllegalArgumentException e) {
            verificar("agendar_fechaVacia_lanzaIllegalArgumentException", agenda.totalCitas() == 0);
        }

        System.out.println("---------------------------------------------");
        System.out.println("Aprobadas: " + aprobadas + "   Fallidas: " + fallidas);
    }

    /**
     * Prepara el mismo estado inicial para cada caso: equivale al metodo anotado
     * con {@code @Before} en JUnit.
     *
     * @return una agenda con Kira y Michi activas y Rocky inactivo
     */
    private static AgendaService nuevaAgenda() {
        AgendaService agenda = new AgendaService();
        agenda.registrarMascota(new Mascota("M-001", "Kira", true));
        agenda.registrarMascota(new Mascota("M-002", "Michi", true));
        agenda.registrarMascota(new Mascota("M-009", "Rocky", false));
        return agenda;
    }

    private static void verificar(String nombreDelCaso, boolean paso) {
        if (paso) {
            aprobadas++;
            System.out.println("[OK]    " + nombreDelCaso);
        } else {
            fallidas++;
            System.out.println("[FALLA] " + nombreDelCaso);
        }
    }
}

/**
 * Expediente de una mascota de la clinica Huellitas.
 * Una mascota inactiva es la que fue dada de baja del servicio y no puede agendar citas.
 *
 * @author Equipo VetCare
 */
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

    public String getId() { return id; }

    public String getNombre() { return nombre; }

    /**
     * Indica si la mascota puede recibir servicios de la clinica.
     *
     * @return true si el expediente esta activo
     */
    public boolean estaActiva() { return activa; }

    /** Da de baja el expediente: la mascota deja de poder agendar citas. */
    public void inactivar() { this.activa = false; }
}

/**
 * Cita agendada para una mascota en una fecha y hora determinada.
 */
class Cita {

    private final String idMascota;
    private final String fechaHora;

    /**
     * Crea una cita ya validada por el servicio de agenda.
     *
     * @param idMascota expediente al que pertenece la cita
     * @param fechaHora fecha y hora en formato yyyy-MM-dd HH:mm
     */
    public Cita(String idMascota, String fechaHora) {
        this.idMascota = idMascota;
        this.fechaHora = fechaHora;
    }

    public String getIdMascota() { return idMascota; }

    public String getFechaHora() { return fechaHora; }

    @Override
    public String toString() {
        return "Cita[" + idMascota + " -> " + fechaHora + "]";
    }
}

/**
 * Reglas de agendamiento de VetCare.
 * No conoce ventanas ni botones, y por eso se puede probar de forma automatica.
 *
 * @author Equipo VetCare
 */
class AgendaService {

    private final Map<String, Mascota> expedientes = new LinkedHashMap<String, Mascota>();
    private final List<Cita> citas = new ArrayList<Cita>();

    /**
     * Registra o actualiza el expediente de una mascota.
     *
     * @param mascota expediente a guardar; no puede ser null
     * @throws IllegalArgumentException si el expediente viene en null
     */
    public void registrarMascota(Mascota mascota) {
        if (mascota == null) {
            throw new IllegalArgumentException("El expediente no puede ser null.");
        }
        expedientes.put(mascota.getId(), mascota);
    }

    /**
     * Agenda una cita para una mascota registrada y activa.
     * Una mascota inactiva no puede agendar: en ese caso no se crea ninguna cita.
     *
     * @param idMascota identificador del expediente, por ejemplo M-001
     * @param fechaHora fecha y hora en formato yyyy-MM-dd HH:mm
     * @return la cita creada
     * @throws IllegalArgumentException si la fecha y hora vienen vacias
     * @throws NoSuchElementException si no existe expediente con ese identificador
     * @throws IllegalStateException si la mascota esta inactiva o el horario ya esta ocupado
     */
    public Cita agendar(String idMascota, String fechaHora) {
        if (fechaHora == null || fechaHora.trim().isEmpty()) {
            throw new IllegalArgumentException("La fecha y hora de la cita son obligatorias.");
        }
        Mascota mascota = expedientes.get(idMascota);
        if (mascota == null) {
            throw new NoSuchElementException("No existe expediente con ID " + idMascota);
        }
        if (!mascota.estaActiva()) {
            throw new IllegalStateException("La mascota " + mascota.getNombre()
                    + " esta inactiva y no puede agendar citas.");
        }
        String horario = fechaHora.trim();
        for (Cita registrada : citas) {
            if (registrada.getFechaHora().equals(horario)) {
                throw new IllegalStateException("Ya hay una cita agendada para " + horario);
            }
        }
        Cita cita = new Cita(idMascota, horario);
        citas.add(cita);
        return cita;
    }

    /**
     * Cantidad de citas agendadas.
     *
     * @return numero de citas vigentes en memoria
     */
    public int totalCitas() { return citas.size(); }

    /**
     * Copia de la agenda actual.
     *
     * @return lista con las citas agendadas
     */
    public List<Cita> listarCitas() { return new ArrayList<Cita>(citas); }
}

/*
 * ---------------------------------------------------------------------------
 * Version JUnit de los mismos casos. Va en Test Packages, archivo AgendaServiceTest.java
 * (agregar la libreria de pruebas desde el nodo Test Libraries del proyecto).
 *
 * import org.junit.jupiter.api.BeforeEach;
 * import org.junit.jupiter.api.Test;
 * import static org.junit.jupiter.api.Assertions.assertEquals;
 * import static org.junit.jupiter.api.Assertions.assertNotNull;
 * import static org.junit.jupiter.api.Assertions.assertThrows;
 *
 * public class AgendaServiceTest {
 *
 *     private AgendaService agenda;
 *
 *     @BeforeEach
 *     public void prepararAgendaLimpia() {
 *         agenda = new AgendaService();
 *         agenda.registrarMascota(new Mascota("M-001", "Kira", true));
 *         agenda.registrarMascota(new Mascota("M-002", "Michi", true));
 *         agenda.registrarMascota(new Mascota("M-009", "Rocky", false));
 *     }
 *
 *     @Test
 *     public void agendar_mascotaActiva_creaLaCita() {
 *         Cita cita = agenda.agendar("M-001", "2026-09-30 10:00");
 *         assertNotNull(cita);
 *         assertEquals(1, agenda.totalCitas());
 *     }
 *
 *     @Test
 *     public void agendar_mascotaInactiva_lanzaIllegalStateException() {
 *         assertThrows(IllegalStateException.class,
 *                 () -> agenda.agendar("M-009", "2026-09-30 10:00"));
 *         assertEquals(0, agenda.totalCitas());
 *     }
 * }
 * ---------------------------------------------------------------------------
 */
