# -*- coding: utf-8 -*-
"""Programacion II · Clase 12 · laminas de codigo: cada una es un Main.java que corre solo.

La app por capas: ClinicaApp (ventana Swing), ServicioClinica (reglas) y el repositorio CSV.
Las laminas de ventana se compilan y no se ejecutan (salida None).
"""

CLASE = 12

LAMINAS = [
    {"k": 0, "titulo": "main(): una sola instancia de cada capa", "codigo": r"""
import java.util.ArrayList;
import java.util.List;
import javax.swing.JFrame;
import javax.swing.SwingUtilities;

class Main {
    public static void main(String[] args) {
        RepositorioMascotasCSV repositorio =
                new RepositorioMascotasCSV("mascotas.csv");
        ServicioClinica servicio =
                new ServicioClinica(repositorio);
        servicio.cargarDesdeArchivo();
        SwingUtilities.invokeLater(() ->
                new ClinicaApp(servicio).setVisible(true));
    }
}

class RepositorioMascotasCSV {
    RepositorioMascotasCSV(String archivo) { }
    // en la app real lee el CSV: aqui arranca vacio
    List<String> cargar() { return new ArrayList<>(); }
}

class ServicioClinica {
    private final RepositorioMascotasCSV repositorio;
    private final List<String> mascotas = new ArrayList<>();
    ServicioClinica(RepositorioMascotasCSV repositorio) {
        this.repositorio = repositorio;
    }
    void cargarDesdeArchivo() {
        mascotas.addAll(repositorio.cargar());
    }
}

class ClinicaApp extends JFrame {
    ClinicaApp(ServicioClinica servicio) {
        super("Clinica Veterinaria");
        setSize(760, 420);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }
}
""", "salida": None},

    {"k": 1, "titulo": "El constructor registra el cierre", "codigo": r"""
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import javax.swing.JFrame;
import javax.swing.SwingUtilities;

class Main {
    public static void main(String[] args) {
        ServicioClinica servicio = new ServicioClinica();
        SwingUtilities.invokeLater(() ->
                new ClinicaApp(servicio).setVisible(true));
    }
}

class ServicioClinica {
    void guardarEnArchivo() {
        System.out.println("Guardado en mascotas.csv");
    }
}

class ClinicaApp extends JFrame {
    private final ServicioClinica servicio;
    public ClinicaApp(ServicioClinica servicio) {
        super("Clinica Veterinaria");
        this.servicio = servicio;
        construirInterfaz();
        refrescarTabla();
        setSize(760, 420);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                cerrarGuardando();
            }
        });
    }
    private void construirInterfaz() { }
    private void refrescarTabla() { }
    private void cerrarGuardando() {
        servicio.guardarEnArchivo();
        dispose();
    }
}
""", "salida": None},


    {"k": 1, "titulo": "cerrarGuardando(): guardar antes de salir", "codigo": r"""
import java.io.IOException;
import java.util.List;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;

class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new ClinicaApp(
                new ServicioClinica()).setVisible(true));
    }
}
class ClinicaApp extends JFrame {
    private final ServicioClinica servicio;
    ClinicaApp(ServicioClinica servicio) {
        super("Clinica Veterinaria");
        this.servicio = servicio;
        JButton cerrar = new JButton("Cerrar");
        cerrar.addActionListener(e -> cerrarGuardando());
        add(cerrar);
        setSize(300, 120);
    }

    private void cerrarGuardando() {
        try {
            servicio.guardarEnArchivo();
            JOptionPane.showMessageDialog(this,
                    "Se guardaron "
                    + servicio.listar().size()
                    + " mascotas en el archivo.");
            dispose();
        } catch (IOException ex) {
            int opcion = JOptionPane.showConfirmDialog(this,
                    "No se pudo guardar (" + ex.getMessage()
                    + "). Cerrar de todas formas?",
                    "Error al guardar",
                    JOptionPane.YES_NO_OPTION);
            if (opcion == JOptionPane.YES_OPTION) {
                dispose();
            }
        }
    }
}
class ServicioClinica {
    List<String> listar() { return List.of("Firulais"); }
    void guardarEnArchivo() throws IOException { }
}
""", "salida": None, "nota": "Aqui el cierre se dispara con un boton Cerrar (en la app lo dispara la "
              "X, como en la lamina anterior) y guardarEnArchivo() esta vacio: en la app "
              "escribe el CSV por medio del repositorio."},

    {"k": 2, "titulo": "ServicioClinica: dueño de la lista", "codigo": r"""
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
class Main {
    public static void main(String[] args)
            throws IOException {
        RepositorioMascotasCSV repo =
                new RepositorioMascotasCSV();
        repo.guardar(List.of("Firulais", "Michi"));
        ServicioClinica s = new ServicioClinica(repo);
        s.cargarDesdeArchivo();
    }
}
class RepositorioMascotasCSV {
    private final Path ruta = Path.of("mascotas.csv");
    List<String> cargar() {
        try { return Files.readAllLines(ruta); }
        catch (IOException e) { return new ArrayList<>(); }
    }
    void guardar(List<String> f) throws IOException {
        Files.write(ruta, f);
    }
}
class ServicioClinica {
    private final RepositorioMascotasCSV repositorio;
    private final List<String> mascotas = new ArrayList<>();

    ServicioClinica(RepositorioMascotasCSV repositorio) {
        this.repositorio = repositorio;
    }

    public void cargarDesdeArchivo() {
        mascotas.clear();
        mascotas.addAll(repositorio.cargar());
        System.out.println("Mascotas cargadas: "
                + mascotas.size());
    }

    public void guardarEnArchivo() throws IOException {
        repositorio.guardar(mascotas);
    }
}
""", "salida": """
Mascotas cargadas: 2
""", "nota": "Crea (o sobrescribe) mascotas.csv en la carpeta donde se ejecuta. Para que quepa, "
              "la lista es de nombres: en la app son objetos Mascota."},

    {"k": 4, "titulo": "registrar(): la regla vive en el servicio", "codigo": r"""
import java.util.ArrayList;
class Main {
    public static void main(String[] args) {
        ServicioClinica s = new ServicioClinica();
        for (String edad : new String[]{"4", "dos", "40"}) {
            try {
                Mascota m = s.registrar("Firulais",
                        "Canino", edad, "1144556677");
                System.out.println("OK " + m.id);
            } catch (DatosInvalidosException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
class ServicioClinica {
    private static final int EDAD_MAXIMA = 25;
    final ArrayList<Mascota> mascotas = new ArrayList<>();
    public Mascota registrar(String nombre, String especie,
            String edadTexto, String cedula)
            throws DatosInvalidosException {
        String texto = (edadTexto == null)
                ? "" : edadTexto.trim();
        int edad;

        try {
            edad = Integer.parseInt(texto);
        } catch (NumberFormatException e) {
            throw new DatosInvalidosException(
                    "Edad no entera: '" + texto + "'");
        }
        if (edad < 0 || edad > EDAD_MAXIMA) {
            throw new DatosInvalidosException(
                    "Edad fuera de 0 a " + EDAD_MAXIMA);
        }
        Mascota nueva = new Mascota("M00" + (mascotas.size()
                + 1), nombre.trim(), especie.trim(), edad,
                cedula.trim());
        mascotas.add(nueva);
        return nueva;
    }
}
class DatosInvalidosException extends Exception {
    DatosInvalidosException(String m) { super(m); }
}
class Mascota {
    final String id;
    Mascota(String id, String nombre, String especie,
            int edad, String cedula) { this.id = id; }
}
""", "salida": """
OK M001
Edad no entera: 'dos'
Edad fuera de 0 a 25
""", "nota": "Para que quepa: se omiten las validaciones de nombre, especie y cedula (como en "
              "el recorte), los mensajes van acortados y el id sale de un contador simple en "
              "vez de siguienteId()."},

    {"k": 4, "titulo": "registrarMascota(): la frontera con la interfaz", "codigo": r"""
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new ClinicaApp(
                new ServicioClinica()).setVisible(true));
    }
}
class DatosInvalidosException extends Exception {
    DatosInvalidosException(String m) { super(m); }
}
class ClinicaApp extends JFrame {
    private final ServicioClinica servicio;
    private final JTextField txtNombre = new JTextField();
    private final JTextField txtEdad = new JTextField();
    ClinicaApp(ServicioClinica servicio) {
        super("Clinica Veterinaria");
        this.servicio = servicio;
        txtEdad.addActionListener(e -> registrarMascota());
        add(txtNombre, "North");
        add(txtEdad, "South");
        setSize(300, 120);
    }

    /** Frontera: aqui se capturan los errores de datos. */
    private void registrarMascota() {
        try {
            String id = servicio.registrar(
                    txtNombre.getText(), txtEdad.getText());
            JOptionPane.showMessageDialog(this,
                    "Mascota registrada con ID " + id);
        } catch (DatosInvalidosException ex) {
            JOptionPane.showMessageDialog(this,
                    ex.getMessage(), "Datos invalidos",
                    JOptionPane.WARNING_MESSAGE);
        }
    }
}
class ServicioClinica {
    String registrar(String nombre, String edad)
            throws DatosInvalidosException {
        if (!edad.trim().matches("[0-9]+")) {
            throw new DatosInvalidosException(
                    "La edad debe ser un numero entero.");
        }
        return "M001";
    }
}
""", "salida": None, "nota": "Arriba el nombre, abajo la edad: Enter en la edad registra (en la "
              "app hay un boton Registrar y cuatro campos)."},
]
