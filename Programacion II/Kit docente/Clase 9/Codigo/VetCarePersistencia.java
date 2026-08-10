import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

/**
 * VetCare - Clase 9
 * Persistencia de mascotas en archivo CSV, con lectura defensiva y try-with-resources.
 * Clinica Veterinaria Huellitas.
 *
 * Ejecutar desde consola:  java VetCarePersistencia.java
 * (o crear el proyecto en NetBeans y ejecutar la clase principal)
 *
 * Corra el programa DOS veces seguidas: la segunda vez debe recuperar lo que
 * escribio la primera. Esa es toda la leccion.
 */
public class VetCarePersistencia {

    public static void main(String[] args) {
        RepositorioMascotasCSV repositorio = new RepositorioMascotasCSV("mascotas.csv");

        System.out.println("=== VetCare: arranque ===");
        System.out.println("Archivo de datos: " + repositorio.rutaAbsoluta());

        List<Mascota> mascotas = repositorio.cargar();
        System.out.println("Mascotas recuperadas del archivo: " + mascotas.size());

        if (mascotas.isEmpty()) {
            System.out.println("No habia datos previos. Sembrando el arranque de la clinica...");
            mascotas.add(new Mascota("M001", "Firulais", "Canino", 4, "1144556677"));
            mascotas.add(new Mascota("M002", "Michi", "Felino", 2, "1098765432"));
        }

        Mascota nueva = new Mascota(siguienteId(mascotas), "Pelusa", "Felino", 1, "1052233445");
        mascotas.add(nueva);
        System.out.println("Registrada en memoria: " + nueva);

        repositorio.guardar(mascotas);
        System.out.println("Datos escritos en disco.");

        System.out.println("=== VetCare: simulacion de reapertura ===");
        List<Mascota> verificacion = repositorio.cargar();
        for (Mascota m : verificacion) {
            System.out.println("  " + m);
        }
        System.out.println("Total tras reabrir: " + verificacion.size());
    }

    /** Genera el consecutivo M001, M002, ... sin repetir ids existentes. */
    private static String siguienteId(List<Mascota> mascotas) {
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

/** Modelo del dominio: una mascota de la clinica. */
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

    @Override
    public String toString() {
        return id + " - " + nombre + " (" + especie + ", " + edad + " anios) dueno CC " + cedulaDueno;
    }
}

/**
 * Unica clase del proyecto que sabe de archivos.
 * Si manana VetCare pasa a base de datos, solo se reemplaza esta clase.
 */
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

    /** Escribe TODA la lista. try-with-resources cierra y vacia el buffer pase lo que pase. */
    public void guardar(List<Mascota> mascotas) {
        try (BufferedWriter escritor = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8)) {
            escritor.write(ENCABEZADO);
            escritor.newLine();
            for (Mascota m : mascotas) {
                escritor.write(aLinea(m));
                escritor.newLine();
            }
        } catch (IOException e) {
            System.out.println("No se pudo guardar el archivo: " + e.getMessage());
        }
    }

    /** Lectura defensiva: si no hay archivo devuelve lista vacia; una linea mala no tumba la app. */
    public List<Mascota> cargar() {
        List<Mascota> mascotas = new ArrayList<>();
        if (!Files.exists(ruta)) {
            return mascotas;
        }
        try (BufferedReader lector = Files.newBufferedReader(ruta, StandardCharsets.UTF_8)) {
            lector.readLine(); // primera linea = encabezado: se descarta a proposito
            String linea;
            int numeroDeLinea = 1;
            while ((linea = lector.readLine()) != null) {
                numeroDeLinea++;
                if (linea.trim().isEmpty()) {
                    continue;
                }
                Mascota m = desdeLinea(linea, numeroDeLinea);
                if (m != null) {
                    mascotas.add(m);
                }
            }
        } catch (IOException e) {
            System.out.println("No se pudo leer el archivo: " + e.getMessage());
        }
        return mascotas;
    }

    private String aLinea(Mascota m) {
        return limpiar(m.getId()) + SEPARADOR
                + limpiar(m.getNombre()) + SEPARADOR
                + limpiar(m.getEspecie()) + SEPARADOR
                + m.getEdad() + SEPARADOR
                + limpiar(m.getCedulaDueno());
    }

    private Mascota desdeLinea(String linea, int numeroDeLinea) {
        String[] campos = linea.split(SEPARADOR, -1);
        if (campos.length != CAMPOS_ESPERADOS) {
            System.out.println("Linea " + numeroDeLinea + " ignorada: se esperaban "
                    + CAMPOS_ESPERADOS + " campos y llegaron " + campos.length);
            return null;
        }
        try {
            int edad = Integer.parseInt(campos[3].trim());
            return new Mascota(campos[0].trim(), campos[1].trim(), campos[2].trim(),
                    edad, campos[4].trim());
        } catch (NumberFormatException e) {
            System.out.println("Linea " + numeroDeLinea + " ignorada: la edad '"
                    + campos[3] + "' no es un numero entero.");
            return null;
        }
    }

    /** Protege el contrato del CSV: un dato con ';' partiria la linea y perderia el registro. */
    private String limpiar(String texto) {
        if (texto == null) {
            return "";
        }
        return texto.replace(SEPARADOR, ",").trim();
    }
}
