# -*- coding: utf-8 -*-
"""Programacion II · Clase 7 · laminas de codigo: cada una es un Main.java que corre solo."""

CLASE = 7

LAMINAS = [
    {"k": 2, "titulo": "RepositorioClinica: el Singleton", "codigo": r"""
import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) {
        RepositorioClinica a = RepositorioClinica.getInstancia();
        RepositorioClinica b = RepositorioClinica.getInstancia();
        System.out.println("Son el mismo objeto? " + (a == b));
    }
}
class Mascota { }
class RepositorioClinica {
    private static RepositorioClinica instancia;
    private final List<Mascota> mascotas = new ArrayList<Mascota>();
    private RepositorioClinica() {
        System.out.println("[Repositorio] Se creo la UNICA instancia de datos.");
    }

    public static synchronized RepositorioClinica getInstancia() {
        if (instancia == null) {
            instancia = new RepositorioClinica();
        }
        return instancia;
    }
}
""", "salida": """
[Repositorio] Se creo la UNICA instancia de datos.
Son el mismo objeto? true
"""},

    {"k": 2, "titulo": "Comprobar que es la misma instancia", "codigo": r"""
import java.util.ArrayList;
import java.util.List;
class Main {
    public static void main(String[] args) {
        RepositorioClinica a =
                RepositorioClinica.getInstancia();
        RepositorioClinica b =
                RepositorioClinica.getInstancia();
        System.out.println("Son el mismo objeto? "
                + (a == b));
        a.registrar(new Mascota("M-001", "Kira", "perro"));
        System.out.println("Mascotas vistas desde b: "
                + b.listar());
    }
}
class Mascota {
    private final String id, nombre, especie;
    Mascota(String id, String nombre, String especie) {
        this.id = id; this.nombre = nombre;
        this.especie = especie;
    }
    public String toString() {
        return id + " - " + nombre + " (" + especie + ")";
    }
}

class RepositorioClinica {
    private static RepositorioClinica instancia;
    private final List<Mascota> mascotas =
            new ArrayList<Mascota>();
    private RepositorioClinica() { }
    static synchronized RepositorioClinica getInstancia() {
        if (instancia == null) {
            instancia = new RepositorioClinica();
        }
        return instancia;
    }
    void registrar(Mascota m) { mascotas.add(m); }
    List<Mascota> listar() {
        return new ArrayList<Mascota>(mascotas);
    }
}
""", "salida": """
Son el mismo objeto? true
Mascotas vistas desde b: [M-001 - Kira (perro)]
"""},

    {"k": 2, "titulo": "Cada ventana pide getInstancia()", "codigo": r"""
import java.util.ArrayList;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new VentanaSucursal("Recepcion");
            new VentanaSucursal("Consultorio");
        });
    }
}
class RepositorioClinica {
    private static RepositorioClinica instancia;
    private ArrayList<Mascota> mascotas = new ArrayList<>();
    private RepositorioClinica() { }
    static synchronized RepositorioClinica getInstancia() {
        if (instancia == null)
            instancia = new RepositorioClinica();
        return instancia;
    }
    void registrar(Mascota m) { mascotas.add(m); }
    int total() { return mascotas.size(); }
}
class Mascota {
    private final String id, nombre;
    Mascota(String id, String nombre) {
        this.id = id; this.nombre = nombre;
    }
}
class VentanaSucursal extends JFrame {
    private final JTextField txtId = new JTextField(6);
    private final JTextField txtNombre = new JTextField(8);
    VentanaSucursal(String punto) {
        super("Clinica - " + punto);
        txtNombre.addActionListener(e -> registrar());
        add(txtId, "West"); add(txtNombre, "Center");
        pack();
        setVisible(true);
    }
    // No crea su repositorio: pide el unico que existe
    private void registrar() {
        RepositorioClinica.getInstancia().registrar(
                new Mascota(txtId.getText().trim(),
                        txtNombre.getText().trim()));
        setTitle("Total: " + RepositorioClinica
                .getInstancia().total());
    }
}
""", "salida": None,
     "nota": "Abre dos ventanas. Se escriben id y nombre y Enter en el nombre registra: "
             "el total del titulo cuenta lo registrado desde AMBAS ventanas (un solo repositorio)."},

    {"k": 3, "titulo": "Consulta: el tipo base", "codigo": r"""
class Main {
    public static void main(String[] args) {
        Consulta c = new ConsultaVacunacion("M-001");
        System.out.println(c.describir());
    }
}

abstract class Consulta {
    protected final String idMascota;
    protected Consulta(String idMascota) {
        this.idMascota = idMascota;
    }
    public abstract int duracionMinutos();
    public abstract double tarifaBase();
    public String describir() {
        return getClass().getSimpleName() + " para " + idMascota
                + " | " + duracionMinutos() + " min | $" + tarifaBase();
    }
}

class ConsultaVacunacion extends Consulta {
    public ConsultaVacunacion(String idMascota) { super(idMascota); }
    @Override public int duracionMinutos() { return 15; }
    @Override public double tarifaBase() { return 35000; }
}
""", "salida": """
ConsultaVacunacion para M-001 | 15 min | $35000.0
"""},

    {"k": 3, "titulo": "ConsultaUrgencia: una subclase", "codigo": r"""
class Main {
    public static void main(String[] args) {
        Consulta urgencia = new ConsultaUrgencia("M-001");
        System.out.println(urgencia.describir());
    }
}
abstract class Consulta {
    protected final String idMascota;
    protected Consulta(String idMascota) { this.idMascota = idMascota; }
    public abstract int duracionMinutos();
    public abstract double tarifaBase();
    public String describir() {
        return getClass().getSimpleName() + " para " + idMascota
                + " | " + duracionMinutos() + " min | $" + tarifaBase();
    }
}

class ConsultaUrgencia extends Consulta {
    public ConsultaUrgencia(String idMascota) { super(idMascota); }
    @Override
    public int duracionMinutos() { return 45; }

    @Override
    public double tarifaBase() { return 120000; }
}
""", "salida": """
ConsultaUrgencia para M-001 | 45 min | $120000.0
"""},

    {"k": 3, "titulo": "FabricaConsultas.crear()", "codigo": r"""
class Main {
    public static void main(String[] args) {
        Consulta c =
                FabricaConsultas.crear("control", "M-001");
        System.out.println(c.getClass().getSimpleName());
    }
}
abstract class Consulta {
    protected final String id;
    Consulta(String id) { this.id = id; }
}
class ConsultaVacunacion extends Consulta {
    ConsultaVacunacion(String id) { super(id); }
}
class ConsultaControl extends Consulta {
    ConsultaControl(String id) { super(id); }
}
class ConsultaUrgencia extends Consulta {
    ConsultaUrgencia(String id) { super(id); }
}

class FabricaConsultas {
    private FabricaConsultas() { }

    public static Consulta crear(String tipo,
            String idMascota) {
        if (idMascota == null
                || idMascota.trim().isEmpty()) {
            throw new IllegalArgumentException(
                    "Falta el ID de la mascota.");
        }
        String clave = (tipo == null)
                ? "" : tipo.trim().toUpperCase();
        if (clave.equals("VACUNACION")) {
            return new ConsultaVacunacion(idMascota.trim());
        } else if (clave.equals("CONTROL")) {
            return new ConsultaControl(idMascota.trim());
        } else if (clave.equals("URGENCIA")) {
            return new ConsultaUrgencia(idMascota.trim());
        } else {
            throw new IllegalArgumentException(
                    "Tipo no soportado: " + tipo);
        }
    }
}
""", "salida": """
ConsultaControl
"""},

    {"k": 3, "titulo": "La fábrica en uso", "codigo": r"""
class Main {
    public static void main(String[] args) {
        Consulta vacuna = FabricaConsultas.crear(
                "vacunacion", "M-001");
        Consulta urgencia = FabricaConsultas.crear(
                "URGENCIA", "M-001");
        System.out.println(vacuna.describir());
        System.out.println(urgencia.describir());
        try {
            FabricaConsultas.crear(
                    "peluqueria espacial", "M-001");
        } catch (IllegalArgumentException e) {
            System.out.println("La fabrica protege el "
                    + "dominio: " + e.getMessage());
        }
    }
}
abstract class Consulta {
    protected final String idMascota;
    Consulta(String id) { this.idMascota = id; }
    String describir() {
        return getClass().getSimpleName()
                + " para " + idMascota;
    }
}
class ConsultaVacunacion extends Consulta {
    ConsultaVacunacion(String id) { super(id); }
}
class ConsultaUrgencia extends Consulta {
    ConsultaUrgencia(String id) { super(id); }
}
class FabricaConsultas {
    static Consulta crear(String tipo, String idMascota) {
        String clave = tipo.trim().toUpperCase();
        if (clave.equals("VACUNACION")) {
            return new ConsultaVacunacion(idMascota);
        } else if (clave.equals("URGENCIA")) {
            return new ConsultaUrgencia(idMascota);
        }
        throw new IllegalArgumentException(
                "Tipo de consulta no soportado: " + tipo);
    }
}
""", "salida": """
ConsultaVacunacion para M-001
ConsultaUrgencia para M-001
La fabrica protege el dominio: Tipo de consulta no soportado: peluqueria espacial
"""},
]
