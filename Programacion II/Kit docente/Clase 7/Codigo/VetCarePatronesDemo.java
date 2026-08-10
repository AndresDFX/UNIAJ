package vetcare.patrones;

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

/** Clase 7 de VetCare: un solo repositorio (Singleton) y una fabrica de consultas (Factory). */
public class VetCarePatronesDemo {

    public static void main(String[] args) {
        RepositorioVetCare a = RepositorioVetCare.getInstancia();
        RepositorioVetCare b = RepositorioVetCare.getInstancia();
        System.out.println("Son el mismo objeto? " + (a == b));
        System.out.println("id a = " + System.identityHashCode(a)
                + "   id b = " + System.identityHashCode(b));

        a.registrar(new Mascota("M-001", "Kira", "perro"));
        System.out.println("Mascotas vistas desde b: " + b.listar());

        Consulta vacuna = FabricaConsultas.crear("vacunacion", "M-001");
        Consulta urgencia = FabricaConsultas.crear("URGENCIA", "M-001");
        System.out.println(vacuna.describir());
        System.out.println(urgencia.describir());
        try {
            FabricaConsultas.crear("peluqueria espacial", "M-001");
        } catch (IllegalArgumentException e) {
            System.out.println("La fabrica protege el dominio: " + e.getMessage());
        }

        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new VentanaSucursal("Recepcion").setVisible(true);
                new VentanaSucursal("Consultorio").setVisible(true);
            }
        });
    }
}

/** Expediente basico de una mascota de la clinica Huellitas. */
class Mascota {

    private final String id;
    private final String nombre;
    private final String especie;

    public Mascota(String id, String nombre, String especie) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
    }

    public String getId() { return id; }

    public String getNombre() { return nombre; }

    public String getEspecie() { return especie; }

    @Override
    public String toString() {
        return id + " - " + nombre + " (" + especie + ")";
    }
}

/** Singleton: unico punto de acceso a los datos en memoria de VetCare. */
class RepositorioVetCare {

    private static RepositorioVetCare instancia;

    private final List<Mascota> mascotas = new ArrayList<Mascota>();

    private RepositorioVetCare() {
        System.out.println("[Repositorio] Se creo la UNICA instancia de datos.");
    }

    public static synchronized RepositorioVetCare getInstancia() {
        if (instancia == null) {
            instancia = new RepositorioVetCare();
        }
        return instancia;
    }

    public void registrar(Mascota mascota) {
        if (mascota == null || mascota.getId() == null || mascota.getId().trim().isEmpty()) {
            throw new IllegalArgumentException("El ID de la mascota es obligatorio.");
        }
        if (buscarPorId(mascota.getId()) != null) {
            throw new IllegalArgumentException("El ID " + mascota.getId() + " ya esta registrado.");
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

    /** Necesario para poder probar en la clase 8: deja el archivador vacio. */
    public void limpiar() { mascotas.clear(); }
}

/** Tipo base de los servicios que presta la clinica. */
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

    @Override
    public int duracionMinutos() { return 15; }

    @Override
    public double tarifaBase() { return 35000; }
}

class ConsultaControl extends Consulta {

    public ConsultaControl(String idMascota) { super(idMascota); }

    @Override
    public int duracionMinutos() { return 30; }

    @Override
    public double tarifaBase() { return 60000; }
}

class ConsultaUrgencia extends Consulta {

    public ConsultaUrgencia(String idMascota) { super(idMascota); }

    @Override
    public int duracionMinutos() { return 45; }

    @Override
    public double tarifaBase() { return 120000; }
}

/** Factory: la ventana pide un tipo y no se entera de que subclase se construyo. */
class FabricaConsultas {

    private FabricaConsultas() { }

    public static Consulta crear(String tipo, String idMascota) {
        if (idMascota == null || idMascota.trim().isEmpty()) {
            throw new IllegalArgumentException("La consulta necesita el ID de la mascota.");
        }
        String clave = (tipo == null) ? "" : tipo.trim().toUpperCase();
        if (clave.equals("VACUNACION")) {
            return new ConsultaVacunacion(idMascota.trim());
        } else if (clave.equals("CONTROL")) {
            return new ConsultaControl(idMascota.trim());
        } else if (clave.equals("URGENCIA")) {
            return new ConsultaUrgencia(idMascota.trim());
        } else {
            throw new IllegalArgumentException("Tipo de consulta no soportado: " + tipo);
        }
    }
}

/** Dos instancias de esta ventana comparten el mismo repositorio. */
class VentanaSucursal extends JFrame {

    private final JTextField txtId = new JTextField();
    private final JTextField txtNombre = new JTextField();
    private final JTextField txtEspecie = new JTextField();
    private final JTextArea area = new JTextArea(8, 30);
    private final JButton btnRegistrar = new JButton("Registrar");
    private final JButton btnRefrescar = new JButton("Refrescar");

    public VentanaSucursal(String punto) {
        super("VetCare - " + punto);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLayout(new BorderLayout());

        JPanel form = new JPanel(new GridLayout(4, 2, 6, 6));
        form.add(new JLabel("ID (ej. M-002):"));
        form.add(txtId);
        form.add(new JLabel("Nombre:"));
        form.add(txtNombre);
        form.add(new JLabel("Especie:"));
        form.add(txtEspecie);
        form.add(btnRegistrar);
        form.add(btnRefrescar);

        area.setEditable(false);
        add(form, BorderLayout.NORTH);
        add(new JScrollPane(area), BorderLayout.CENTER);

        btnRegistrar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrar();
            }
        });

        btnRefrescar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                refrescar();
            }
        });

        pack();
        setLocationByPlatform(true);
        refrescar();
    }

    private void registrar() {
        try {
            RepositorioVetCare.getInstancia().registrar(new Mascota(
                    txtId.getText().trim(), txtNombre.getText().trim(), txtEspecie.getText().trim()));
            txtId.setText("");
            txtNombre.setText("");
            txtEspecie.setText("");
            refrescar();
        } catch (IllegalArgumentException ex) {
            JOptionPane.showMessageDialog(this, ex.getMessage());
        }
    }

    private void refrescar() {
        StringBuilder sb = new StringBuilder();
        sb.append("Repositorio #")
                .append(System.identityHashCode(RepositorioVetCare.getInstancia()))
                .append(System.lineSeparator());
        for (Mascota m : RepositorioVetCare.getInstancia().listar()) {
            sb.append(m.toString()).append(System.lineSeparator());
        }
        sb.append("Total: ").append(RepositorioVetCare.getInstancia().total());
        area.setText(sb.toString());
    }
}
