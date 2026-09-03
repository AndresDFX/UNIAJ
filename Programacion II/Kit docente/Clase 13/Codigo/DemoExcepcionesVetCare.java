import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * VetCare - Clinica Veterinaria Huellitas
 * Clase 13: control de excepciones (checked vs unchecked, try-catch-finally, throw / throws).
 * Ejecutar en VS Code: el boton Run sobre el metodo main, o Ctrl+F5.
 */
public class DemoExcepcionesVetCare {

    private static final String ARCHIVO = "datos/mascotas.csv";

    /** Excepcion CHECKED propia: al extender Exception el compilador obliga a capturarla o a declararla. */
    public static class DatoInvalidoException extends Exception {

        public DatoInvalidoException(String mensaje) {
            super(mensaje);
        }
    }

    /** Entidad del dominio: valida y LANZA. Nunca muestra ventanas ni le habla al usuario. */
    public static class Mascota {

        private String id;
        private String nombre;
        private int edad;
        private double peso;

        public Mascota(String id, String nombre) throws DatoInvalidoException {
            if (id == null || id.trim().isEmpty()) {
                throw new DatoInvalidoException("El ID de la mascota es obligatorio.");
            }
            if (nombre == null || nombre.trim().isEmpty()) {
                throw new DatoInvalidoException("El nombre de la mascota es obligatorio.");
            }
            this.id = id.trim();
            this.nombre = nombre.trim();
        }

        public String getId() {
            return id;
        }

        public String getNombre() {
            return nombre;
        }

        public void setEdad(String texto) throws DatoInvalidoException {
            if (texto == null || texto.trim().isEmpty()) {
                throw new DatoInvalidoException("La edad no puede quedar vacia.");
            }
            int valor;
            try {
                valor = Integer.parseInt(texto.trim());
            } catch (NumberFormatException e) {
                // Traducimos una excepcion tecnica (unchecked) a un mensaje del negocio.
                throw new DatoInvalidoException("La edad debe ser un numero entero. Escribieron: " + texto);
            }
            if (valor < 0 || valor > 30) {
                throw new DatoInvalidoException("La edad debe estar entre 0 y 30 anios. Recibi: " + valor);
            }
            this.edad = valor;
        }

        public void setPeso(String texto) throws DatoInvalidoException {
            if (texto == null || texto.trim().isEmpty()) {
                throw new DatoInvalidoException("El peso no puede quedar vacio.");
            }
            double valor;
            try {
                valor = Double.parseDouble(texto.trim().replace(',', '.'));
            } catch (NumberFormatException e) {
                throw new DatoInvalidoException("El peso debe ser un numero, por ejemplo 12.5. Escribieron: " + texto);
            }
            if (valor <= 0 || valor > 120) {
                throw new DatoInvalidoException("El peso debe estar entre 0.1 y 120 kg. Recibi: " + valor);
            }
            this.peso = valor;
        }

        public String toLineaCsv() {
            return id + ";" + nombre + ";" + edad + ";" + peso;
        }

        @Override
        public String toString() {
            return id + " - " + nombre + " (" + edad + " anios, " + peso + " kg)";
        }
    }

    /** Capa de aplicacion: aqui SI se captura, porque aqui se le habla al usuario. */
    private static void registrar(List<Mascota> agenda, String id, String nombre, String edad, String peso) {
        try {
            Mascota m = new Mascota(id, nombre);
            m.setEdad(edad);
            m.setPeso(peso);
            agenda.add(m);   // el add va DESPUES de validar: nada incompleto entra a la coleccion
            System.out.println("  [OK] Registrada: " + m);
        } catch (DatoInvalidoException e) {
            // En Swing seria: JOptionPane.showMessageDialog(this, e.getMessage(), "Dato invalido", JOptionPane.WARNING_MESSAGE);
            System.out.println("  [AVISO AL USUARIO] " + e.getMessage());
        } finally {
            System.out.println("  (finally) Intento terminado. Mascotas en memoria: " + agenda.size());
        }
    }

    /** Prueba de que finally se ejecuta incluso cuando el try ya hizo return. */
    private static String buscarNombrePorId(List<Mascota> agenda, String id) {
        try {
            for (Mascota m : agenda) {
                if (m.getId().equalsIgnoreCase(id)) {
                    return m.getNombre();   // el return NO se salta el finally
                }
            }
            return "(no esta en la agenda)";
        } finally {
            System.out.println("  (finally) Busqueda de " + id + " terminada, con return y todo.");
        }
    }

    /** Lectura tolerante: el try externo protege el archivo, el interno protege cada linea. */
    private static List<Mascota> cargar(String ruta) {
        List<Mascota> lista = new ArrayList<>();
        try (BufferedReader lector = new BufferedReader(new FileReader(ruta))) {   // BufferedReader es AutoCloseable
            String linea;
            while ((linea = lector.readLine()) != null) {
                String[] campos = linea.split(";");
                if (campos.length < 4) {
                    System.out.println("  [OMITIDA] Linea incompleta: " + linea);
                    continue;
                }
                try {
                    Mascota m = new Mascota(campos[0], campos[1]);
                    m.setEdad(campos[2]);
                    m.setPeso(campos[3]);
                    lista.add(m);
                } catch (DatoInvalidoException e) {
                    System.out.println("  [OMITIDA] " + e.getMessage());
                }
            }
        } catch (FileNotFoundException e) {   // hija de IOException: por eso va primero
            System.out.println("  [INFO] No existe " + ruta + ". VetCare arranca con la lista vacia.");
        } catch (IOException e) {
            System.out.println("  [ERROR] Fallo leyendo " + ruta + ": " + e.getMessage());
        }
        return lista;
    }

    private static void guardar(String ruta, List<Mascota> lista) {
        File carpeta = new File(ruta).getParentFile();   // ruta relativa: sirve en cualquier maquina
        if (carpeta != null && !carpeta.exists()) {
            carpeta.mkdirs();
        }
        try (PrintWriter salida = new PrintWriter(ruta)) {
            for (Mascota m : lista) {
                salida.println(m.toLineaCsv());
            }
            System.out.println("  [OK] Guardadas " + lista.size() + " mascotas en " + ruta);
        } catch (FileNotFoundException e) {
            System.out.println("  [ERROR] No pude guardar en " + ruta + ": " + e.getMessage());
        }
    }

    /** ASI NO: ejemplo intencional de catch vacio, para verlo fallar en clase. */
    private static void malaPractica(List<Mascota> agenda) {
        int antes = agenda.size();
        try {
            Mascota m = new Mascota("M-999", "Fantasma");
            m.setEdad("tres");
            agenda.add(m);
        } catch (DatoInvalidoException e) {
            // MALA PRACTICA A PROPOSITO: catch vacio, nadie se entera de nada.
        }
        System.out.println("  Antes: " + antes + " | Ahora: " + agenda.size() + " -> la mascota nunca entro y nadie aviso.");
    }

    public static void main(String[] args) {
        System.out.println("=== VetCare | Clase 13: control de excepciones ===");

        List<Mascota> agenda = cargar(ARCHIVO);
        System.out.println("Mascotas cargadas del archivo: " + agenda.size());

        System.out.println("");
        System.out.println("1) Entradas simuladas desde el formulario de registro:");
        registrar(agenda, "M-001", "Firulais", "4", "28.5");
        registrar(agenda, "M-002", "Michi", "tres", "3.2");
        registrar(agenda, "M-003", "Rocky", "", "20");
        registrar(agenda, "M-004", "Luna", "150", "8");
        registrar(agenda, "M-005", "Pelusa", "2", "cuatro kilos");

        System.out.println("");
        System.out.println("2) finally se ejecuta aunque el try haga return:");
        System.out.println("  Mascota M-001 -> " + buscarNombrePorId(agenda, "M-001"));

        System.out.println("");
        System.out.println("3) Que pasa cuando el catch queda vacio:");
        malaPractica(agenda);

        System.out.println("");
        System.out.println("4) Turno del usuario. Escriba edades (o 'fin' para salir):");
        Scanner teclado = new Scanner(System.in);
        boolean seguir = true;
        while (seguir) {
            System.out.print("Edad de la mascota: ");
            String entrada = teclado.nextLine();
            if ("fin".equalsIgnoreCase(entrada.trim())) {
                seguir = false;
            } else {
                try {
                    Mascota prueba = new Mascota("M-TMP", "Prueba");
                    prueba.setEdad(entrada);
                    System.out.println("  Edad aceptada. La aplicacion sigue viva.");
                } catch (DatoInvalidoException e) {
                    System.out.println("  " + e.getMessage() + " Intente de nuevo.");
                }
            }
        }
        teclado.close();

        guardar(ARCHIVO, agenda);
        System.out.println("=== Fin de la demo: VetCare nunca se cerro por un dato mal escrito. ===");
    }
}
