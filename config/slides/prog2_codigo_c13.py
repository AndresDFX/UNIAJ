# -*- coding: utf-8 -*-
"""Programacion II · Clase 13 · laminas de codigo: cada una es un Main.java que corre solo.

Excepciones: checked propia, try/catch/finally, finally con return, catch especifico antes que
el general y la mala practica del catch vacio (mala a proposito, pero compila y corre).
"""

CLASE = 13

LAMINAS = [
    {"k": 1, "titulo": "Una excepción checked propia", "codigo": r"""
class Main {
    static void validarEdad(int edad) throws DatoInvalidoException {
        if (edad < 0 || edad > 30) {
            throw new DatoInvalidoException(
                    "La edad debe estar entre 0 y 30 anios. Recibi: " + edad);
        }
    }

    public static void main(String[] args) {
        try {
            validarEdad(40);   // sin try/catch (o throws) esta linea no compila
        } catch (DatoInvalidoException e) {
            System.out.println("Capturada: " + e.getMessage());
        }
    }
}

/** Excepcion CHECKED propia: el compilador obliga a capturarla o a declararla. */
class DatoInvalidoException extends Exception {

    public DatoInvalidoException(String mensaje) {
        super(mensaje);
    }
}
""", "salida": """
Capturada: La edad debe estar entre 0 y 30 anios. Recibi: 40
"""},

    {"k": 2, "titulo": "registrar(): try, catch y finally", "codigo": r"""
import java.util.ArrayList;
import java.util.List;
class Main {
    public static void main(String[] args) {
        List<Mascota> agenda = new ArrayList<>();
        registrar(agenda, "M-001", "Firulais", "4", "28.5");
        registrar(agenda, "M-002", "Michi", "tres", "3.2");
        registrar(agenda, "M-003", "Rocky", "6", "32.0");
    }
    static void registrar(List<Mascota> agenda, String id,
            String nombre, String edad, String peso) {
        try {
            Mascota m = new Mascota(id, nombre);
            m.setEdad(edad);
            m.setPeso(peso);
            agenda.add(m);   // el add va DESPUES de validar
            System.out.println("  [OK] Registrada: " + m);
        } catch (DatoInvalidoException e) {
            System.out.println("[AVISO] " + e.getMessage());
        } finally {
            System.out.println("  (finally) Terminado."
                    + " En memoria: " + agenda.size());
        }
    }
}
class DatoInvalidoException extends Exception {
    DatoInvalidoException(String m) { super(m); }
}
class Mascota {
    private final String id, nombre;
    private int edad;
    private double peso;
    Mascota(String id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }
    void setEdad(String t) throws DatoInvalidoException {
        try {
            edad = Integer.parseInt(t);
        } catch (NumberFormatException e) {
            throw new DatoInvalidoException(
                    "La edad debe ser un numero entero.");
        }
    }
    void setPeso(String t) { peso = Double.parseDouble(t); }
    public String toString() { return id + " " + nombre; }
}
""", "salida": """
  [OK] Registrada: M-001 Firulais
  (finally) Terminado. En memoria: 1
[AVISO] La edad debe ser un numero entero.
  (finally) Terminado. En memoria: 1
  [OK] Registrada: M-003 Rocky
  (finally) Terminado. En memoria: 2
""", "nota": "Para que quepa, el aviso al usuario va por consola (en Swing seria un "
              "JOptionPane.showMessageDialog) y los mensajes van acortados."},

    {"k": 2, "titulo": "finally corre aunque haya return", "codigo": r"""
import java.util.List;

class Main {
    public static void main(String[] args) {
        List<Mascota> agenda =
                List.of(new Mascota("M-001", "Firulais"));
        System.out.println("Mascota M-001 -> "
                + buscarNombrePorId(agenda, "M-001"));
        System.out.println("Mascota M-009 -> "
                + buscarNombrePorId(agenda, "M-009"));
    }

    /** finally se ejecuta aunque el try ya hizo return. */
    private static String buscarNombrePorId(
            List<Mascota> agenda, String id) {
        try {
            for (Mascota m : agenda) {
                if (m.getId().equalsIgnoreCase(id)) {
                    // el return NO se salta el finally
                    return m.getNombre();
                }
            }

            return "(no esta en la agenda)";
        } finally {
            System.out.println("  (finally) Busqueda de "
                    + id + " terminada,"
                    + " con return y todo.");
        }
    }
}

class Mascota {
    private final String id, nombre;
    Mascota(String id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }
    String getId() { return id; }
    String getNombre() { return nombre; }
}
""", "salida": """
  (finally) Busqueda de M-001 terminada, con return y todo.
Mascota M-001 -> Firulais
  (finally) Busqueda de M-009 terminada, con return y todo.
Mascota M-009 -> (no esta en la agenda)
""", "nota": "El finally se imprime ANTES que la linea de Mascota: println recibe el "
              "resultado del metodo, y el metodo no termina sin pasar por el finally."},

    {"k": 2, "titulo": "cargar(): del catch específico al general", "codigo": r"""
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
class Main {
    public static void main(String[] args)
            throws FileNotFoundException {
        try (PrintWriter w =
                new PrintWriter("mascotas.csv")) {
            w.println("M-001;Firulais");
            w.println("M-002;Michi");
        }
        System.out.println(DemoExcepcionesClinica
                .cargar("mascotas.csv"));
        System.out.println(DemoExcepcionesClinica
                .cargar("no_existe.csv"));
    }
}
class DemoExcepcionesClinica {
    static List<String> cargar(String ruta) {
        List<String> lista = new ArrayList<>();
        // BufferedReader es AutoCloseable: se cierra solo
        try (BufferedReader lector =
                new BufferedReader(new FileReader(ruta))) {
            String linea;
            while ((linea = lector.readLine()) != null) {
                String[] campos = linea.split(";");
                lista.add(campos[1]);
            }
        // hija de IOException: por eso va primero
        } catch (FileNotFoundException e) {
            System.out.println("  [INFO] No existe " + ruta
                    + ". Se arranca con la lista vacia.");
        } catch (IOException e) {
            System.out.println("  [ERROR] Fallo leyendo "
                    + ruta + ": " + e.getMessage());
        }
        return lista;
    }
}
""", "salida": """
[Firulais, Michi]
  [INFO] No existe no_existe.csv. Se arranca con la lista vacia.
[]
""", "nota": "Crea (o sobrescribe) mascotas.csv en la carpeta donde se ejecuta; "
              "no_existe.csv no debe existir. El bucle interno va simplificado a una lista de "
              "nombres (en la clase arma Mascota y valida cada linea con su propio try)."},

    {"k": 3, "titulo": "setEdad(): validar y lanzar", "codigo": r"""
class Main {
    public static void main(String[] args) {
        Mascota m = new Mascota();
        String[] entradas = {"4", "tres", "", "150"};
        for (String t : entradas) {
            try {
                m.setEdad(t);
                System.out.println("Aceptada: " + t);
            } catch (DatoInvalidoException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
class DatoInvalidoException extends Exception {
    DatoInvalidoException(String m) { super(m); }
}
class Mascota {
    private int edad;

    public void setEdad(String texto)
            throws DatoInvalidoException {
        if (texto == null || texto.trim().isEmpty()) {
            throw new DatoInvalidoException(
                    "La edad no puede quedar vacia.");
        }
        int valor;
        try {
            valor = Integer.parseInt(texto.trim());
        } catch (NumberFormatException e) {
            // excepcion tecnica -> mensaje del negocio
            throw new DatoInvalidoException("La edad debe"
                    + " ser un numero entero. Escribieron: "
                    + texto);
        }
        if (valor < 0 || valor > 30) {
            throw new DatoInvalidoException("La edad debe"
                    + " estar entre 0 y 30 anios. Recibi: "
                    + valor);
        }
        this.edad = valor;
    }
}
""", "salida": """
Aceptada: 4
La edad debe ser un numero entero. Escribieron: tres
La edad no puede quedar vacia.
La edad debe estar entre 0 y 30 anios. Recibi: 150
"""},

    {"k": 4, "titulo": "malaPractica(): así no", "codigo": r"""
import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) {
        malaPractica(new ArrayList<>());
    }

    /** ASI NO: catch vacio a proposito. */
    private static void malaPractica(List<Mascota> agenda) {
        int antes = agenda.size();
        try {
            Mascota m = new Mascota("M-999", "Fantasma");
            m.setEdad("tres");
            agenda.add(m);
        } catch (DatoInvalidoException e) {
            // MALA PRACTICA A PROPOSITO: catch vacio,
            // nadie se entera de nada.
        }
        System.out.println("  Antes: " + antes
                + " | Ahora: " + agenda.size()
                + " -> la mascota nunca entro"
                + " y nadie aviso.");
    }
}
class DatoInvalidoException extends Exception {
    DatoInvalidoException(String m) { super(m); }
}
class Mascota {
    private int edad;
    Mascota(String id, String nombre) { }
    void setEdad(String t) throws DatoInvalidoException {
        try {
            edad = Integer.parseInt(t);
        } catch (NumberFormatException e) {
            throw new DatoInvalidoException("Edad: " + t);
        }
    }
}
""", "salida": """
  Antes: 0 | Ahora: 0 -> la mascota nunca entro y nadie aviso.
"""},
]
