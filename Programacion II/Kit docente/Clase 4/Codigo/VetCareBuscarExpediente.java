package vetcare;

import java.awt.BorderLayout;
import java.awt.Font;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;

/**
 * VetCare - Clase 4: HashMap + HashSet + primera ventana Swing.
 * Clinica Veterinaria Huellitas.
 * Ventana escrita A MANO (sin el disenador visual) para entender la jerarquia.
 * Archivo unico: en VS Code, el boton Run que aparece sobre el metodo main (o Ctrl+F5).
 */
public class VetCareBuscarExpediente extends JFrame {

    // ---- Datos: la inteligencia del sistema vive aqui, no en el boton ----
    private final Map<String, Expediente> expedientes = new HashMap<>();
    private final Set<String> razas = new HashSet<>();

    // ---- Componentes de la interfaz ----
    private final JTextField txtId = new JTextField(12);
    private final JButton btnBuscar = new JButton("Buscar expediente");
    private final JLabel lblResultado = new JLabel("Escriba un ID (ej: M-002) y presione Buscar", SwingConstants.CENTER);

    public VetCareBuscarExpediente() {
        super("VetCare - Buscar expediente");
        cargarDatosDePrueba();
        compararBusquedas();
        construirInterfaz();
    }

    private void cargarDatosDePrueba() {
        guardar(new Expediente("M-001", "Firulais", "Labrador", "Ana Gomez", "Vacunacion al dia"));
        guardar(new Expediente("M-002", "Michi", "Criollo", "Luis Perez", "Control de peso"));
        guardar(new Expediente("M-003", "Rocky", "Pastor Aleman", "Ana Gomez", "Revision de patas"));
        guardar(new Expediente("M-004", "Nieve", "Persa", "Sara Diaz", "Desparasitacion"));
        guardar(new Expediente("M-005", "Toby", "Labrador", "Sara Diaz", "Control geriatrico"));
        System.out.println("Expedientes: " + expedientes.size() + " | Razas distintas: " + razas.size());
    }

    /** Regla de negocio: avisar antes de que put reemplace en silencio. */
    private void guardar(Expediente e) {
        if (expedientes.containsKey(e.getId())) {
            System.out.println("Atencion: el ID " + e.getId() + " ya existia y sera reemplazado");
        }
        expedientes.put(e.getId(), e);              // clave -> valor
        boolean razaNueva = razas.add(e.getRaza()); // add devuelve false si ya estaba
        if (!razaNueva) {
            System.out.println("Raza ya registrada: " + e.getRaza());
        }
    }

    /** Demo del dia: recorrer 5.000 fichas contra preguntarle la clave al mapa. */
    private void compararBusquedas() {
        List<Expediente> archivoHistorico = new ArrayList<>();
        Map<String, Expediente> indice = new HashMap<>();
        for (int i = 1; i <= 5000; i++) {
            Expediente e = new Expediente("H-" + i, "Paciente " + i, "Criollo",
                    "Dueno " + i, "Archivo historico");
            archivoHistorico.add(e);
            indice.put(e.getId(), e);
        }
        String buscado = "H-5000"; // peor caso: la ultima ficha del archivo

        long t1 = System.nanoTime();
        Expediente porRecorrido = null;
        for (Expediente e : archivoHistorico) {   // busqueda lineal: compara una por una
            if (e.getId().equals(buscado)) {
                porRecorrido = e;
                break;
            }
        }
        long nsLineal = System.nanoTime() - t1;

        long t2 = System.nanoTime();
        Expediente porClave = indice.get(buscado); // busqueda por clave: no recorre nada
        long nsMapa = System.nanoTime() - t2;

        System.out.println("ArrayList recorriendo 5.000: encontrado=" + (porRecorrido != null)
                + " en " + nsLineal + " ns");
        System.out.println("HashMap con get(clave):      encontrado=" + (porClave != null)
                + " en " + nsMapa + " ns");
    }

    private void construirInterfaz() {
        JPanel panelSuperior = new JPanel();           // FlowLayout por defecto
        panelSuperior.add(new JLabel("ID de la mascota:"));
        panelSuperior.add(txtId);
        panelSuperior.add(btnBuscar);

        lblResultado.setFont(new Font("SansSerif", Font.PLAIN, 14));

        JLabel pie = new JLabel("Expedientes cargados: " + expedientes.size()
                + "  |  Razas distintas: " + razas.size(), SwingConstants.CENTER);

        setLayout(new BorderLayout(10, 10));           // el JFrame usa BorderLayout
        add(panelSuperior, BorderLayout.NORTH);
        add(lblResultado, BorderLayout.CENTER);
        add(pie, BorderLayout.SOUTH);

        btnBuscar.addActionListener(e -> buscar());    // el evento solo delega
        txtId.addActionListener(e -> buscar());        // Enter tambien busca

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(600, 230);
        setLocationRelativeTo(null);                   // centrada en pantalla
    }

    /** Lee la entrada, consulta el mapa y pinta el resultado. Nada mas. */
    private void buscar() {
        try {
            String id = txtId.getText().trim().toUpperCase();
            if (id.isEmpty()) {
                throw new IllegalArgumentException("Debe escribir un ID, por ejemplo M-002");
            }
            Expediente e = expedientes.get(id);        // busqueda por clave, sin recorrer
            if (e == null) {                           // get devuelve null si no existe
                lblResultado.setText("No existe expediente con ID " + id);
                JOptionPane.showMessageDialog(this,
                        "No existe expediente con ID " + id,
                        "Sin resultados", JOptionPane.WARNING_MESSAGE);
                return;
            }
            lblResultado.setText("<html><b>" + e.getNombre() + "</b> (" + e.getRaza() + ")<br>"
                    + "Dueno: " + e.getDueno() + "<br>Nota clinica: " + e.getNota() + "</html>");
        } catch (IllegalArgumentException ex) {
            JOptionPane.showMessageDialog(this, ex.getMessage(),
                    "Dato invalido", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        // La interfaz se construye en el hilo de eventos de Swing (EDT)
        SwingUtilities.invokeLater(() -> new VetCareBuscarExpediente().setVisible(true));
    }
}

class Expediente {

    private final String id;
    private final String nombre;
    private final String raza;
    private final String dueno;
    private final String nota;

    public Expediente(String id, String nombre, String raza, String dueno, String nota) {
        this.id = id;
        this.nombre = nombre;
        this.raza = raza;
        this.dueno = dueno;
        this.nota = nota;
    }

    public String getId() { return id; }
    public String getNombre() { return nombre; }
    public String getRaza() { return raza; }
    public String getDueno() { return dueno; }
    public String getNota() { return nota; }

    @Override
    public String toString() {
        return id + " | " + nombre + " (" + raza + ") - dueno: " + dueno + " - " + nota;
    }
}
