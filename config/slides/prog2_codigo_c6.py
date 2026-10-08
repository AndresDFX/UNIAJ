# -*- coding: utf-8 -*-
"""Programacion II · Clase 6 · laminas de codigo: cada una es un Main.java que corre solo."""

CLASE = 6

LAMINAS = [
    {"k": 0, "titulo": "main(): la ventana arranca en el EDT", "codigo": r"""
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingUtilities;

class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new VentanaRegistroMascota().setVisible(true);
            }
        });
    }
}

class VentanaRegistroMascota extends JFrame {
    public VentanaRegistroMascota() {
        super("Clinica - Registro de mascotas");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        add(new JLabel("Ventana creada en el hilo de eventos (EDT)"));
        pack();
        setLocationRelativeTo(null);
    }
}
""", "salida": None},

    {"k": 1, "titulo": "El formulario: GridLayout de 5 \u00d7 2", "codigo": r"""
import java.awt.BorderLayout;
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame v = new VentanaRegistroMascota();
            v.setVisible(true);
        });
    }
}

class VentanaRegistroMascota extends JFrame {
    final JTextField txtId = new JTextField();
    final JTextField txtNombre = new JTextField();
    final JTextField txtEspecie = new JTextField();
    final JTextField txtEdad = new JTextField();
    public VentanaRegistroMascota() {
        super("Clinica - Registro de mascotas");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JPanel formulario =
                new JPanel(new GridLayout(5, 2, 6, 6));
        formulario.add(new JLabel("ID (ej. M-001):"));
        formulario.add(txtId);
        formulario.add(new JLabel("Nombre:"));
        formulario.add(txtNombre);
        formulario.add(new JLabel("Especie:"));
        formulario.add(txtEspecie);
        formulario.add(new JLabel("Edad (anios):"));
        formulario.add(txtEdad);
        formulario.add(new JLabel(""));
        formulario.add(new JButton("Registrar"));
        add(formulario, BorderLayout.NORTH);
        add(new JScrollPane(new JTextArea(10, 32)));
        pack();
    }
}
""", "salida": None},

    {"k": 1, "titulo": "addActionListener: el botón guarda a quien lo escucha", "codigo": r"""
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;

class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame v = new VentanaRegistroMascota();
            v.setVisible(true);
        });
    }
}

class VentanaRegistroMascota extends JFrame {
    final JButton btnRegistrar = new JButton("Registrar");

    public VentanaRegistroMascota() {
        super("Clinica - Registro de mascotas");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        add(btnRegistrar);
        // clase anonima: el boton guarda este oyente
        btnRegistrar.addActionListener(
                new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                registrar();
            }
        });
        pack();
    }

    private void registrar() {
        JOptionPane.showMessageDialog(this, "Clic");
    }
}
""", "salida": None},

    {"k": 2, "titulo": "El repositorio no sabe de ventanas", "codigo": r"""
import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) {
        RepositorioMascotas repo =
                new RepositorioMascotas();
        repo.registrar(new Mascota("M-001"));
        repo.registrar(new Mascota("M-002"));
        try {
            repo.registrar(new Mascota("m-001"));
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
        System.out.println(repo.listar() + " total="
                + repo.total());
    }
}

class Mascota {
    private final String id;
    Mascota(String id) { this.id = id; }
    String getId() { return id; }
    public String toString() { return id; }
}

class RepositorioMascotas {
    private final List<Mascota> mascotas =
            new ArrayList<>();

    public void registrar(Mascota m) {
        if (m == null) {
            throw new IllegalArgumentException("Es nula");
        }
        for (Mascota x : mascotas) {
            if (x.getId().equalsIgnoreCase(m.getId())) {
                throw new IllegalArgumentException(
                        "Ya existe el ID " + m.getId());
            }
        }
        mascotas.add(m);
    }

    public List<Mascota> listar() {
        return new ArrayList<>(mascotas); // copia
    }

    public int total() { return mascotas.size(); }
}
""", "salida": """
Error: Ya existe el ID m-001
[M-001, M-002] total=2
"""},

    {"k": 3, "titulo": "registrar(): la vista lee, delega y muestra", "codigo": r"""
import java.awt.GridLayout;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(
                () -> new Ventana().setVisible(true));
    }
}

class Controlador {
    String registrarMascota(String id, String nombre) {
        if (id.trim().isEmpty()) throw
                new IllegalArgumentException("Sin ID");
        return nombre.trim();
    }
}

class Ventana extends JFrame {
    private final JTextField txtId = new JTextField(10);
    private final JTextField txtNombre = new JTextField(10);
    private Controlador controlador = new Controlador();
    Ventana() {
        setLayout(new GridLayout(2, 1));
        add(txtId); add(txtNombre);
        txtNombre.addActionListener(e -> registrar());
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        pack();
    }

    private void registrar() {
        try { // lee, delega y muestra
            String nombre = controlador.registrarMascota(
                    txtId.getText(), txtNombre.getText());
            JOptionPane.showMessageDialog(this,
                    "Mascota registrada: " + nombre);
        } catch (IllegalArgumentException ex) {
            JOptionPane.showMessageDialog(this,
                    ex.getMessage(), "Datos invalidos",
                    JOptionPane.WARNING_MESSAGE);
        }
    }
}
""", "salida": None},

    {"k": 3, "titulo": "registrarMascota(): el controlador valida y convierte", "codigo": r"""
class Main {
    public static void main(String[] args) {
        Controlador c = new Controlador();
        String[][] casos = {{"M-001", "Firulais", "3"},
                {"", "Michi", "2"}, {"M-3", "Rocky", "x"},
                {"M-004", "Nieve", "50"}};
        for (String[] x : casos) {
            try {
                int edad = c.registrarMascota(
                        x[0], x[1], x[2]);
                System.out.println("OK " + edad);
            } catch (IllegalArgumentException e) {
                System.out.println("No: " + e.getMessage());
            }
        }
    }
}

class Controlador {
    int registrarMascota(String id, String nombre,
            String edadTexto) {
        if (id == null || id.trim().isEmpty()) {
            throw new IllegalArgumentException(
                    "El ID es obligatorio.");
        }
        if (nombre == null || nombre.trim().isEmpty()) {
            throw new IllegalArgumentException(
                    "El nombre es obligatorio.");
        }
        int edad;
        try {
            edad = Integer.parseInt(edadTexto.trim());
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException(
                    "Edad no numerica: " + edadTexto);
        }
        if (edad < 0 || edad > 40) {
            throw new IllegalArgumentException(
                    "La edad debe estar entre 0 y 40.");
        }
        return edad;
    }
}
""", "salida": """
OK 3
No: El ID es obligatorio.
No: Edad no numerica: x
No: La edad debe estar entre 0 y 40.
"""},
]
