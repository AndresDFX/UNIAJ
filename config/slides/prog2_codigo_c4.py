# -*- coding: utf-8 -*-
"""Programacion II · Clase 4 · laminas de codigo: cada una es un Main.java que corre solo."""

CLASE = 4

LAMINAS = [
    {"k": 1, "titulo": "Expediente: el valor que guarda el mapa", "codigo": r"""
class Main {
    public static void main(String[] args) {
        Expediente e = new Expediente("M-001",
                "Firulais", "Labrador", "Ana Gomez",
                "Vacunacion al dia");
        System.out.println(e);
    }
}

class Expediente {
    private final String id;
    private final String nombre;
    private final String raza;
    private final String dueno;
    private final String nota;

    public Expediente(String id, String nombre, String raza,
            String dueno, String nota) {
        this.id = id;
        this.nombre = nombre;
        this.raza = raza;
        this.dueno = dueno;
        this.nota = nota;
    }

    @Override
    public String toString() {
        return id + " | " + nombre + " (" + raza + ")"
                + " - dueno: " + dueno + " - " + nota;
    }
}
""", "salida": """
M-001 | Firulais (Labrador) - dueno: Ana Gomez - Vacunacion al dia
"""},

    {"k": 1, "titulo": "La misma ficha en una lista y en un mapa", "codigo": r"""
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Main {
    public static void main(String[] args) {
        List<Expediente> archivoHistorico =
                new ArrayList<>();
        Map<String, Expediente> indice = new HashMap<>();
        for (int i = 1; i <= 5000; i++) {
            Expediente e = new Expediente("H-" + i,
                    "Paciente " + i);
            archivoHistorico.add(e); // una tras otra
            indice.put(e.getId(), e); // clave -> valor
        }
        String buscado = "H-5000"; // peor caso: la ultima

        System.out.println("Lista: "
                + archivoHistorico.size());
        System.out.println("Mapa:  " + indice.size());
        System.out.println(buscado + " -> "
                + indice.get(buscado).getNombre());
    }
}

class Expediente {
    private final String id;
    private final String nombre;
    public Expediente(String id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }
    public String getId() { return id; }
    public String getNombre() { return nombre; }
}
""", "salida": """
Lista: 5000
Mapa:  5000
H-5000 -> Paciente 5000
"""},

    {"k": 1, "titulo": "Medir: recorrer contra get(clave)", "codigo": r"""
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Main {
    public static void main(String[] args) {
        List<Expediente> archivo = new ArrayList<>();
        Map<String, Expediente> indice = new HashMap<>();
        for (int i = 1; i <= 5000; i++) {
            Expediente e = new Expediente("H-" + i);
            archivo.add(e);
            indice.put(e.getId(), e);
        }
        String buscado = "H-5000"; // peor caso: la ultima

        long t1 = System.nanoTime();
        Expediente porRecorrido = null;
        for (Expediente e : archivo) { // una por una
            if (e.getId().equals(buscado)) {
                porRecorrido = e;
                break;
            }
        }
        long nsLineal = System.nanoTime() - t1;

        long t2 = System.nanoTime();
        // busqueda por clave: no recorre nada
        Expediente porClave = indice.get(buscado);
        long nsMapa = System.nanoTime() - t2;

        System.out.println("ArrayList recorriendo 5.000: "
                + (porRecorrido != null) + " en "
                + nsLineal + " ns");
        System.out.println("HashMap con get(clave):      "
                + (porClave != null) + " en "
                + nsMapa + " ns");
    }
}

class Expediente {
    private final String id;
    public Expediente(String id) { this.id = id; }
    public String getId() { return id; }
}
""", "salida": None,
     "nota": "Los nanosegundos cambian en cada corrida y en cada equipo: lo que se compara es el orden de magnitud."},

    {"k": 2, "titulo": "guardar(): put avisa antes de reemplazar", "codigo": r"""
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Main {
    public static void main(String[] args) {
        Clinica c = new Clinica();
        c.guardar(new Expediente("M-001", "Labrador"));
        c.guardar(new Expediente("M-005", "Labrador"));
        c.guardar(new Expediente("M-001", "Criollo"));
        System.out.println("Fichas: " + c.expedientes.size()
                + " | Razas: " + c.razas.size());
    }
}

class Expediente {
    private final String id, raza;
    Expediente(String id, String raza) {
        this.id = id;
        this.raza = raza;
    }
    String getId() { return id; }
    String getRaza() { return raza; }
}

class Clinica {
    final Map<String, Expediente> expedientes =
            new HashMap<>();
    final Set<String> razas = new HashSet<>();

    // Regla: avisar antes de que put reemplace en silencio
    void guardar(Expediente e) {
        if (expedientes.containsKey(e.getId())) {
            System.out.println("Aviso: el ID " + e.getId()
                    + " ya existia: se reemplaza");
        }
        expedientes.put(e.getId(), e); // clave -> valor
        // add devuelve false si ya estaba
        boolean razaNueva = razas.add(e.getRaza());
        if (!razaNueva) {
            System.out.println("Raza ya registrada: "
                    + e.getRaza());
        }
    }
}
""", "salida": """
Raza ya registrada: Labrador
Aviso: el ID M-001 ya existia: se reemplaza
Fichas: 2 | Razas: 2
"""},

    {"k": 3, "titulo": "Un mapa y un conjunto como atributos", "codigo": r"""
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Main {
    public static void main(String[] args) {
        new Clinica().cargarDatosDePrueba();
    }
}

class Expediente {
    private final String id, raza;
    Expediente(String id, String raza) {
        this.id = id;
        this.raza = raza;
    }
    String getId() { return id; }
    String getRaza() { return raza; }
}

class Clinica {
    // Datos: la inteligencia vive aqui, no en el boton
    private final Map<String, Expediente> expedientes =
            new HashMap<>();
    private final Set<String> razas = new HashSet<>();

    void cargarDatosDePrueba() {
        guardar(new Expediente("M-001", "Labrador"));
        guardar(new Expediente("M-002", "Criollo"));
        guardar(new Expediente("M-003", "Pastor Aleman"));
        guardar(new Expediente("M-004", "Persa"));
        guardar(new Expediente("M-005", "Labrador"));
        System.out.println("Expedientes: "
                + expedientes.size()
                + " | Razas distintas: " + razas.size());
    }

    private void guardar(Expediente e) {
        expedientes.put(e.getId(), e);
        if (!razas.add(e.getRaza())) {
            System.out.println("Raza repetida: "
                    + e.getRaza());
        }
    }
}
""", "salida": """
Raza repetida: Labrador
Expedientes: 5 | Razas distintas: 4
"""},

    {"k": 4, "titulo": "Paneles y layouts, escritos a mano", "codigo": r"""
import java.awt.BorderLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;

class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(
                () -> new Ventana().setVisible(true));
    }
}

class Ventana extends JFrame {
    Ventana() {
        super("Clinica - Buscar expediente");
        JPanel panelSuperior = new JPanel(); // FlowLayout
        panelSuperior.add(new JLabel("ID de la mascota:"));
        panelSuperior.add(new JTextField(12));
        panelSuperior.add(new JButton("Buscar expediente"));
        JLabel lblResultado = new JLabel("Escriba un ID",
                SwingConstants.CENTER);
        JLabel pie = new JLabel("Expedientes cargados: 5",
                SwingConstants.CENTER);

        // el JFrame usa BorderLayout
        setLayout(new BorderLayout(10, 10));
        add(panelSuperior, BorderLayout.NORTH);
        add(lblResultado, BorderLayout.CENTER);
        add(pie, BorderLayout.SOUTH);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(600, 230);
    }
}
""", "salida": None},

    {"k": 4, "titulo": "El evento, el cierre y el arranque en el EDT", "codigo": r"""
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

class Main {
    public static void main(String[] args) {
        // La interfaz se arma en el hilo de Swing (EDT)
        SwingUtilities.invokeLater(
                () -> new Ventana().setVisible(true));
    }
}

class Ventana extends JFrame {
    private final JTextField txtId = new JTextField(12);
    private final JButton btnBuscar = new JButton("Buscar");

    Ventana() {
        super("Clinica - Buscar expediente");
        JPanel p = new JPanel();
        p.add(txtId);
        p.add(btnBuscar);
        add(p);
        // el evento solo delega; Enter tambien busca
        btnBuscar.addActionListener(e -> buscar());
        txtId.addActionListener(e -> buscar());
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 120);
        setLocationRelativeTo(null); // centrada en pantalla
    }

    private void buscar() {
        setTitle("Buscando " + txtId.getText().trim());
    }
}
""", "salida": None},

    {"k": 4, "titulo": "buscar(): get y el caso null", "codigo": r"""
import java.util.HashMap;
import java.util.Map;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(
                () -> new Ventana().setVisible(true));
    }
}

class Ventana extends JFrame {
    private final Map<String, String> expedientes =
            new HashMap<>();
    private final JTextField txtId = new JTextField(12);
    private final JLabel lblResultado = new JLabel();

    Ventana() {
        expedientes.put("M-002", "Michi (Criollo)");
        add(txtId, "North");
        add(lblResultado);
        txtId.addActionListener(e -> buscar());
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setSize(400, 150);
    }

    private void buscar() {
        String id = txtId.getText().trim().toUpperCase();
        // busqueda por clave, sin recorrer
        String e = expedientes.get(id);
        if (e == null) { // get devuelve null si no existe
            lblResultado.setText("No existe ID " + id);
            JOptionPane.showMessageDialog(this,
                    "No existe expediente con ID " + id,
                    "Sin resultados",
                    JOptionPane.WARNING_MESSAGE);
            return;
        }
        lblResultado.setText("<html><b>" + e + "</b>");
    }
}
""", "salida": None},
]
