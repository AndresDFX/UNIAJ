import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
import javax.swing.WindowConstants;
import javax.swing.table.DefaultTableModel;

/**
 * VetCare - Clase 12: aplicacion integrada de punta a punta.
 * Clinica Veterinaria Huellitas.
 *
 * Capas:  Mascota (modelo) -> RepositorioMascotasCSV (datos)
 *         -> ServicioVetCare (logica) -> VetCareApp (interfaz)
 *
 * Un solo main. Una sola instancia de servicio. Un solo archivo de datos.
 *
 * Ejecutar:  java VetCareApp.java
 *
 * Guion de humo: abrir con datos -> registrar -> buscar por ID -> cerrar
 * guardando -> reabrir y verificar que la mascota nueva sigue ahi.
 */
public class VetCareApp extends JFrame {

    private final ServicioVetCare servicio;

    private final DefaultTableModel modelo = new DefaultTableModel(
            new Object[]{"ID", "Nombre", "Especie", "Edad", "CC Dueno"}, 0) {
        @Override
        public boolean isCellEditable(int fila, int columna) {
            return false;
        }
    };

    private final JTextField txtNombre = new JTextField();
    private final JTextField txtEspecie = new JTextField();
    private final JTextField txtEdad = new JTextField();
    private final JTextField txtCedula = new JTextField();
    private final JTextField txtBuscar = new JTextField();

    public VetCareApp(ServicioVetCare servicio) {
        super("VetCare - Clinica Veterinaria Huellitas");
        this.servicio = servicio;
        construirInterfaz();
        refrescarTabla();
        setSize(760, 420);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                cerrarGuardando();
            }
        });
    }

    private void construirInterfaz() {
        JPanel formulario = new JPanel(new GridLayout(5, 2, 6, 6));
        formulario.setBorder(BorderFactory.createTitledBorder("Registrar mascota"));
        formulario.add(new JLabel("Nombre:"));
        formulario.add(txtNombre);
        formulario.add(new JLabel("Especie:"));
        formulario.add(txtEspecie);
        formulario.add(new JLabel("Edad (anios):"));
        formulario.add(txtEdad);
        formulario.add(new JLabel("Cedula del dueno:"));
        formulario.add(txtCedula);
        JButton btnRegistrar = new JButton("Registrar");
        btnRegistrar.addActionListener(e -> registrarMascota());
        formulario.add(new JLabel(""));
        formulario.add(btnRegistrar);

        JPanel busqueda = new JPanel(new BorderLayout(6, 6));
        busqueda.setBorder(BorderFactory.createTitledBorder("Buscar expediente por ID"));
        JButton btnBuscar = new JButton("Buscar");
        btnBuscar.addActionListener(e -> buscarPorId());
        busqueda.add(txtBuscar, BorderLayout.CENTER);
        busqueda.add(btnBuscar, BorderLayout.EAST);

        JPanel izquierda = new JPanel(new BorderLayout(6, 6));
        izquierda.add(formulario, BorderLayout.NORTH);
        izquierda.add(busqueda, BorderLayout.SOUTH);

        add(izquierda, BorderLayout.WEST);
        add(new JScrollPane(new JTable(modelo)), BorderLayout.CENTER);
    }

    /** Frontera: aqui se capturan los errores de datos y se le hablan al usuario. */
    private void registrarMascota() {
        try {
            Mascota registrada = servicio.registrar(txtNombre.getText(), txtEspecie.getText(),
                    txtEdad.getText(), txtCedula.getText());
            refrescarTabla();
            limpiarFormulario();
            JOptionPane.showMessageDialog(this, "Mascota registrada con ID " + registrada.getId());
        } catch (DatosInvalidosException ex) {
            JOptionPane.showMessageDialog(this, ex.getMessage(), "Datos invalidos",
                    JOptionPane.WARNING_MESSAGE);
        }
    }

    private void buscarPorId() {
        Mascota encontrada = servicio.buscarPorId(txtBuscar.getText());
        if (encontrada == null) {
            JOptionPane.showMessageDialog(this, "No existe expediente con ID " + txtBuscar.getText(),
                    "Sin resultados", JOptionPane.INFORMATION_MESSAGE);
        } else {
            JOptionPane.showMessageDialog(this, encontrada.ficha(), "Expediente",
                    JOptionPane.INFORMATION_MESSAGE);
        }
    }

    private void refrescarTabla() {
        modelo.setRowCount(0);
        for (Mascota m : servicio.listar()) {
            modelo.addRow(new Object[]{m.getId(), m.getNombre(), m.getEspecie(),
                m.getEdad(), m.getCedulaDueno()});
        }
    }

    private void limpiarFormulario() {
        txtNombre.setText("");
        txtEspecie.setText("");
        txtEdad.setText("");
        txtCedula.setText("");
    }

    private void cerrarGuardando() {
        try {
            servicio.guardarEnArchivo();
            JOptionPane.showMessageDialog(this, "Se guardaron " + servicio.listar().size()
                    + " mascotas en el archivo.");
            dispose();
        } catch (IOException ex) {
            int opcion = JOptionPane.showConfirmDialog(this,
                    "No se pudo guardar (" + ex.getMessage() + "). Cerrar de todas formas?",
                    "Error al guardar", JOptionPane.YES_NO_OPTION);
            if (opcion == JOptionPane.YES_OPTION) {
                dispose();
            }
        }
    }

    public static void main(String[] args) {
        RepositorioMascotasCSV repositorio = new RepositorioMascotasCSV("mascotas.csv");
        ServicioVetCare servicio = new ServicioVetCare(repositorio);
        servicio.cargarDesdeArchivo();
        SwingUtilities.invokeLater(() -> new VetCareApp(servicio).setVisible(true));
    }
}

/** Error de datos del usuario: no es una falla del programa, es informacion para la interfaz. */
class DatosInvalidosException extends Exception {

    public DatosInvalidosException(String mensaje) {
        super(mensaje);
    }
}

class Mascota {

    private final String id;
    private final String nombre;
    private final String especie;
    private final int edad;
    private final String cedulaDueno;

    public Mascota(String id, String nombre, String especie, int edad, String cedulaDueno) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
        this.cedulaDueno = cedulaDueno;
    }

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public String getEspecie() {
        return especie;
    }

    public int getEdad() {
        return edad;
    }

    public String getCedulaDueno() {
        return cedulaDueno;
    }

    public String ficha() {
        return "Expediente " + id + "\nNombre: " + nombre + "\nEspecie: " + especie
                + "\nEdad: " + edad + " anios\nDueno CC: " + cedulaDueno;
    }
}

/** Logica del negocio: dueno del ArrayList y de las reglas. No sabe que existe Swing. */
class ServicioVetCare {

    private static final int EDAD_MAXIMA = 25;

    private final RepositorioMascotasCSV repositorio;
    private final List<Mascota> mascotas = new ArrayList<>();

    public ServicioVetCare(RepositorioMascotasCSV repositorio) {
        this.repositorio = repositorio;
    }

    public void cargarDesdeArchivo() {
        mascotas.clear();
        mascotas.addAll(repositorio.cargar());
        System.out.println("Mascotas cargadas: " + mascotas.size());
    }

    public void guardarEnArchivo() throws IOException {
        repositorio.guardar(mascotas);
    }

    public List<Mascota> listar() {
        return new ArrayList<>(mascotas);
    }

    public Mascota buscarPorId(String id) {
        if (id == null || id.trim().isEmpty()) {
            return null;
        }
        for (Mascota m : mascotas) {
            if (m.getId().equalsIgnoreCase(id.trim())) {
                return m;
            }
        }
        return null;
    }

    public Mascota registrar(String nombre, String especie, String edadTexto, String cedula)
            throws DatosInvalidosException {
        if (nombre == null || nombre.trim().isEmpty()) {
            throw new DatosInvalidosException("El nombre de la mascota es obligatorio.");
        }
        if (especie == null || especie.trim().isEmpty()) {
            throw new DatosInvalidosException("La especie es obligatoria.");
        }
        if (cedula == null || cedula.trim().isEmpty()) {
            throw new DatosInvalidosException("La cedula del dueno es obligatoria.");
        }
        String texto = (edadTexto == null) ? "" : edadTexto.trim();
        int edad;
        try {
            edad = Integer.parseInt(texto);
        } catch (NumberFormatException e) {
            throw new DatosInvalidosException("La edad debe ser un numero entero. Llego: '" + texto + "'");
        }
        if (edad < 0 || edad > EDAD_MAXIMA) {
            throw new DatosInvalidosException("La edad debe estar entre 0 y " + EDAD_MAXIMA + " anios.");
        }
        Mascota nueva = new Mascota(siguienteId(), nombre.trim(), especie.trim(), edad, cedula.trim());
        mascotas.add(nueva);
        return nueva;
    }

    private String siguienteId() {
        int mayor = 0;
        for (Mascota m : mascotas) {
            String id = m.getId();
            if (id == null || id.length() < 2) {
                continue;
            }
            try {
                int numero = Integer.parseInt(id.substring(1));
                if (numero > mayor) {
                    mayor = numero;
                }
            } catch (NumberFormatException e) {
                System.out.println("Aviso: id con formato inesperado, se ignora: " + id);
            }
        }
        return String.format("M%03d", mayor + 1);
    }
}

/** Unica clase que sabe de archivos. Contrato: id;nombre;especie;edad;cedula_dueno */
class RepositorioMascotasCSV {

    private static final String SEPARADOR = ";";
    private static final String ENCABEZADO = "id;nombre;especie;edad;cedula_dueno";
    private static final int CAMPOS_ESPERADOS = 5;

    private final Path ruta;

    public RepositorioMascotasCSV(String nombreArchivo) {
        this.ruta = Paths.get(nombreArchivo);
    }

    public String rutaAbsoluta() {
        return ruta.toAbsolutePath().toString();
    }

    public void guardar(List<Mascota> mascotas) throws IOException {
        try (BufferedWriter escritor = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8)) {
            escritor.write(ENCABEZADO);
            escritor.newLine();
            for (Mascota m : mascotas) {
                escritor.write(limpiar(m.getId()) + SEPARADOR
                        + limpiar(m.getNombre()) + SEPARADOR
                        + limpiar(m.getEspecie()) + SEPARADOR
                        + m.getEdad() + SEPARADOR
                        + limpiar(m.getCedulaDueno()));
                escritor.newLine();
            }
        }
    }

    public List<Mascota> cargar() {
        List<Mascota> mascotas = new ArrayList<>();
        if (!Files.exists(ruta)) {
            System.out.println("No existe " + rutaAbsoluta() + ": se arranca con la lista vacia.");
            return mascotas;
        }
        try (BufferedReader lector = Files.newBufferedReader(ruta, StandardCharsets.UTF_8)) {
            lector.readLine(); // primera linea = encabezado: se descarta
            String linea;
            int numeroDeLinea = 1;
            while ((linea = lector.readLine()) != null) {
                numeroDeLinea++;
                if (linea.trim().isEmpty()) {
                    continue;
                }
                String[] campos = linea.split(SEPARADOR, -1);
                if (campos.length != CAMPOS_ESPERADOS) {
                    System.out.println("Linea " + numeroDeLinea + " ignorada: llegaron "
                            + campos.length + " campos y se esperaban " + CAMPOS_ESPERADOS);
                    continue;
                }
                try {
                    mascotas.add(new Mascota(campos[0].trim(), campos[1].trim(), campos[2].trim(),
                            Integer.parseInt(campos[3].trim()), campos[4].trim()));
                } catch (NumberFormatException e) {
                    System.out.println("Linea " + numeroDeLinea + " ignorada: edad no numerica ('"
                            + campos[3] + "')");
                }
            }
        } catch (IOException e) {
            System.out.println("No se pudo leer el archivo: " + e.getMessage());
        }
        return mascotas;
    }

    private String limpiar(String texto) {
        if (texto == null) {
            return "";
        }
        return texto.replace(SEPARADOR, ",").trim();
    }
}
