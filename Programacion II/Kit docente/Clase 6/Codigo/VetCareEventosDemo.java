package vetcare.eventos;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

/** Clase 6 de VetCare: el boton Registrar mascota que de verdad guarda. */
public class VetCareEventosDemo {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new VentanaRegistroMascota().setVisible(true);
            }
        });
    }
}

/** Modelo: una mascota del expediente de la clinica Huellitas. */
class Mascota {

    private final String id;
    private final String nombre;
    private final String especie;
    private final int edad;

    public Mascota(String id, String nombre, String especie, int edad) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
    }

    public String getId() { return id; }

    public String getNombre() { return nombre; }

    public String getEspecie() { return especie; }

    public int getEdad() { return edad; }

    @Override
    public String toString() {
        return id + " | " + nombre + " (" + especie + ", " + edad + " anios)";
    }
}

/** Servicio: guarda las mascotas en memoria. No sabe que existen ventanas. */
class RepositorioMascotas {

    private final List<Mascota> mascotas = new ArrayList<Mascota>();

    public void registrar(Mascota mascota) {
        if (mascota == null) {
            throw new IllegalArgumentException("No se puede registrar una mascota nula.");
        }
        if (buscarPorId(mascota.getId()) != null) {
            throw new IllegalArgumentException("Ya existe una mascota con el ID " + mascota.getId());
        }
        mascotas.add(mascota);
    }

    public Mascota buscarPorId(String id) {
        for (Mascota m : mascotas) {
            if (m.getId().equalsIgnoreCase(id)) {
                return m;
            }
        }
        return null;
    }

    public List<Mascota> listar() { return new ArrayList<Mascota>(mascotas); }

    public int total() { return mascotas.size(); }
}

/** Controlador: traduce el texto de la pantalla a objetos del dominio y valida. */
class ControladorRegistro {

    private final RepositorioMascotas repositorio;

    public ControladorRegistro(RepositorioMascotas repositorio) {
        if (repositorio == null) {
            throw new IllegalArgumentException("El controlador necesita un repositorio.");
        }
        this.repositorio = repositorio;
    }

    public Mascota registrarMascota(String id, String nombre, String especie, String edadTexto) {
        if (id == null || id.trim().isEmpty()) {
            throw new IllegalArgumentException("El ID de la mascota es obligatorio.");
        }
        if (nombre == null || nombre.trim().isEmpty()) {
            throw new IllegalArgumentException("El nombre de la mascota es obligatorio.");
        }
        int edad;
        try {
            edad = Integer.parseInt(edadTexto == null ? "" : edadTexto.trim());
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("La edad debe ser un numero entero. Se recibio: " + edadTexto);
        }
        if (edad < 0 || edad > 40) {
            throw new IllegalArgumentException("La edad debe estar entre 0 y 40 anios.");
        }
        String especieLimpia = (especie == null || especie.trim().isEmpty())
                ? "Sin especificar" : especie.trim();
        Mascota mascota = new Mascota(id.trim(), nombre.trim(), especieLimpia, edad);
        repositorio.registrar(mascota);
        return mascota;
    }

    public String reporteListado() {
        StringBuilder sb = new StringBuilder();
        for (Mascota m : repositorio.listar()) {
            sb.append(m.toString()).append(System.lineSeparator());
        }
        sb.append("Total registradas: ").append(repositorio.total());
        return sb.toString();
    }
}

/** Vista: captura datos, delega y muestra resultados. Nada mas. */
class VentanaRegistroMascota extends JFrame {

    private final JTextField txtId = new JTextField();
    private final JTextField txtNombre = new JTextField();
    private final JTextField txtEspecie = new JTextField();
    private final JTextField txtEdad = new JTextField();
    private final JTextArea areaListado = new JTextArea(10, 32);
    private final JButton btnRegistrar = new JButton("Registrar mascota");

    private final ControladorRegistro controlador =
            new ControladorRegistro(new RepositorioMascotas());

    public VentanaRegistroMascota() {
        super("VetCare - Registro de mascotas");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        JPanel formulario = new JPanel(new GridLayout(5, 2, 6, 6));
        formulario.add(new JLabel("ID (ej. M-001):"));
        formulario.add(txtId);
        formulario.add(new JLabel("Nombre:"));
        formulario.add(txtNombre);
        formulario.add(new JLabel("Especie:"));
        formulario.add(txtEspecie);
        formulario.add(new JLabel("Edad (anios):"));
        formulario.add(txtEdad);
        formulario.add(new JLabel(""));
        formulario.add(btnRegistrar);

        areaListado.setEditable(false);
        add(formulario, BorderLayout.NORTH);
        add(new JScrollPane(areaListado), BorderLayout.CENTER);

        btnRegistrar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrar();
            }
        });

        pack();
        setLocationRelativeTo(null);
    }

    private void registrar() {
        try {
            Mascota mascota = controlador.registrarMascota(
                    txtId.getText(), txtNombre.getText(), txtEspecie.getText(), txtEdad.getText());
            areaListado.setText(controlador.reporteListado());
            limpiar();
            JOptionPane.showMessageDialog(this, "Mascota registrada: " + mascota.getNombre());
        } catch (IllegalArgumentException ex) {
            JOptionPane.showMessageDialog(this, ex.getMessage(),
                    "Datos invalidos", JOptionPane.WARNING_MESSAGE);
        }
    }

    private void limpiar() {
        txtId.setText("");
        txtNombre.setText("");
        txtEspecie.setText("");
        txtEdad.setText("");
        txtId.requestFocus();
    }
}
