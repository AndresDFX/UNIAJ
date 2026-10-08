# -*- coding: utf-8 -*-
"""Programacion II · Clase 9 · laminas de codigo: cada una es un Main.java que corre solo."""

CLASE = 9

LAMINAS = [
    {"k": 2, "titulo": "El contrato del CSV en código", "codigo": r"""
class Main {
    public static void main(String[] args) {
        RepositorioMascotasCSV repo =
                new RepositorioMascotasCSV();
        Mascota m = new Mascota("M001", "Fi;rulais",
                "Canino", 4, "1144556677");
        System.out.println(
                RepositorioMascotasCSV.ENCABEZADO);
        System.out.println(repo.aLinea(m));
    }
}

class RepositorioMascotasCSV {
    static final String SEPARADOR = ";";
    static final String ENCABEZADO =
            "id;nombre;especie;edad;cedula_dueno";
    static final int CAMPOS_ESPERADOS = 5;

    String aLinea(Mascota m) {
        return limpiar(m.getId()) + SEPARADOR
                + limpiar(m.getNombre()) + SEPARADOR
                + limpiar(m.getEspecie()) + SEPARADOR
                + m.getEdad() + SEPARADOR
                + limpiar(m.getCedulaDueno());
    }

    // Un ';' dentro de un dato partiria la linea
    private String limpiar(String texto) {
        if (texto == null) {
            return "";
        }
        return texto.replace(SEPARADOR, ",").trim();
    }
}
class Mascota {
    private final String id, nombre, especie, cedulaDueno;
    private final int edad;
    Mascota(String id, String nombre, String especie,
            int edad, String cedulaDueno) {
        this.id = id; this.nombre = nombre;
        this.especie = especie; this.edad = edad;
        this.cedulaDueno = cedulaDueno;
    }
    String getId() { return id; }
    String getNombre() { return nombre; }
    String getEspecie() { return especie; }
    int getEdad() { return edad; }
    String getCedulaDueno() { return cedulaDueno; }
}
""", "salida": """
id;nombre;especie;edad;cedula_dueno
M001;Fi,rulais;Canino;4;1144556677
"""},

    {"k": 3, "titulo": "guardar(): escribir con try-with-resources", "codigo": r"""
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
class Main {
    public static void main(String[] args)
            throws IOException {
        Path ruta = Paths.get("mascotas.csv");
        new RepositorioMascotasCSV(ruta).guardar(List.of(
                new Mascota("M001", "Firulais"),
                new Mascota("M002", "Michi")));
        System.out.println(Files.readAllLines(ruta));
    }
}
class Mascota {
    private final String id, nombre;
    Mascota(String id, String nombre) {
        this.id = id; this.nombre = nombre;
    }
    String getId() { return id; }
    String getNombre() { return nombre; }
}
class RepositorioMascotasCSV {
    private static final String ENCABEZADO = "id;nombre";
    private final Path ruta;
    RepositorioMascotasCSV(Path ruta) { this.ruta = ruta; }
    private String aLinea(Mascota m) {
        return m.getId() + ";" + m.getNombre();
    }
    /** Escribe TODA la lista. try-with-resources cierra y
     *  vacia el buffer pase lo que pase. */
    public void guardar(List<Mascota> mascotas) {
        try (BufferedWriter escritor =
                Files.newBufferedWriter(ruta,
                        StandardCharsets.UTF_8)) {
            escritor.write(ENCABEZADO);
            escritor.newLine();
            for (Mascota m : mascotas) {
                escritor.write(aLinea(m));
                escritor.newLine();
            }
        } catch (IOException e) {
            System.out.println("No se pudo guardar el "
                    + "archivo: " + e.getMessage());
        }
    }
}
""", "salida": """
[id;nombre, M001;Firulais, M002;Michi]
""", "nota": "Crea (o sobrescribe) mascotas.csv en la carpeta donde se ejecuta."},

    {"k": 4, "titulo": "cargar(): sin archivo no revienta", "codigo": r"""
import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
class Main {
    public static void main(String[] args)
            throws IOException {
        Path ruta = Path.of("mascotas.csv");
        Files.deleteIfExists(ruta);
        RepositorioMascotasCSV repo =
                new RepositorioMascotasCSV();
        System.out.println("Sin archivo: " + repo.cargar());
        Files.writeString(ruta, "id;nombre\nM001;Kira\nx");
        System.out.println("Con archivo: " + repo.cargar());
    }
}
class RepositorioMascotasCSV {
    private final Path ruta = Path.of("mascotas.csv");
    private Mascota desdeLinea(String linea) {
        String[] c = linea.split(";");
        return c.length == 2 ? new Mascota(c[0]) : null;
    }

    public List<Mascota> cargar() {
        List<Mascota> mascotas = new ArrayList<>();
        if (!Files.exists(ruta)) {
            return mascotas;
        }
        try (BufferedReader lector =
                Files.newBufferedReader(ruta)) {
            lector.readLine(); // encabezado: se descarta
            String linea;
            while ((linea = lector.readLine()) != null) {
                Mascota m = desdeLinea(linea);
                if (m != null) mascotas.add(m);
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
        return mascotas;
    }
}
class Mascota {
    private final String id;
    Mascota(String id) { this.id = id; }
    public String toString() { return id; }
}
""", "salida": """
Sin archivo: []
Con archivo: [M001]
""", "nota": "Borra y vuelve a crear mascotas.csv en la carpeta donde se ejecuta."},

    {"k": 4, "titulo": "desdeLinea(): una línea mala no tumba la app", "codigo": r"""
class Main {
    public static void main(String[] args) {
        RepositorioMascotasCSV repo =
                new RepositorioMascotasCSV();
        System.out.println(repo.desdeLinea(
                "M001;Firulais;Canino;4;1144556677", 2));
        System.out.println(repo.desdeLinea(
                "M002;Michi;Felino;2", 3));
        System.out.println(repo.desdeLinea(
                "M003;Pelusa;Felino;uno;1052233445", 4));
    }
}
class Mascota {
    private final String id, nombre, especie, cedulaDueno;
    private final int edad;
    Mascota(String id, String nombre, String especie,
            int edad, String cedulaDueno) {
        this.id = id; this.nombre = nombre;
        this.especie = especie; this.edad = edad;
        this.cedulaDueno = cedulaDueno;
    }
    public String toString() { return id + " " + nombre; }
}
class RepositorioMascotasCSV {
    static final String SEPARADOR = ";";
    static final int CAMPOS_ESPERADOS = 5;
    Mascota desdeLinea(String linea, int numeroDeLinea) {
        String[] campos = linea.split(SEPARADOR, -1);
        if (campos.length != CAMPOS_ESPERADOS) {
            System.out.println("Linea " + numeroDeLinea
                    + " ignorada: se esperaban "
                    + CAMPOS_ESPERADOS + " y llegaron "
                    + campos.length);
            return null;
        }
        try {
            int edad = Integer.parseInt(campos[3].trim());
            return new Mascota(campos[0].trim(),
                    campos[1].trim(), campos[2].trim(),
                    edad, campos[4].trim());
        } catch (NumberFormatException e) {
            System.out.println("Linea " + numeroDeLinea
                    + " ignorada: la edad '" + campos[3]
                    + "' no es un numero entero.");
            return null;
        }
    }
}
""", "salida": """
M001 Firulais
Linea 3 ignorada: se esperaban 5 y llegaron 4
null
Linea 4 ignorada: la edad 'uno' no es un numero entero.
null
"""},

    {"k": 4, "titulo": "main(): cargar, guardar y reabrir", "codigo": r"""
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
class Main {
    public static void main(String[] args)
            throws IOException {
        Files.deleteIfExists(Path.of("mascotas.csv"));
        RepositorioMascotasCSV repositorio =
                new RepositorioMascotasCSV();
        System.out.println("=== Clinica: arranque ===");
        List<Mascota> mascotas = repositorio.cargar();
        System.out.println("Leidas: " + mascotas.size());
        mascotas.add(new Mascota("M001", "Firulais"));
        mascotas.add(new Mascota("M002", "Michi"));
        repositorio.guardar(mascotas);
        System.out.println("Datos escritos en disco.");
        System.out.println("=== Clinica: reapertura ===");
        List<Mascota> verificacion = repositorio.cargar();
        for (Mascota m : verificacion)
            System.out.println("  " + m);
        System.out.println("Total: " + verificacion.size());
    }
}
class Mascota {
    private final String id, nombre;
    Mascota(String id, String nombre) {
        this.id = id; this.nombre = nombre;
    }
    public String toString() { return id + ";" + nombre; }
}
class RepositorioMascotasCSV {
    private final Path ruta = Path.of("mascotas.csv");
    List<Mascota> cargar() throws IOException {
        List<Mascota> lista = new ArrayList<>();
        if (Files.exists(ruta))
            for (String l : Files.readAllLines(ruta)) {
                String[] c = l.split(";");
                lista.add(new Mascota(c[0], c[1]));
            }
        return lista;
    }
    void guardar(List<Mascota> lista) throws IOException {
        List<String> lineas = new ArrayList<>();
        for (Mascota m : lista) lineas.add(m.toString());
        Files.write(ruta, lineas);
    }
}
""", "salida": """
=== Clinica: arranque ===
Leidas: 0
Datos escritos en disco.
=== Clinica: reapertura ===
  M001;Firulais
  M002;Michi
Total: 2
""", "nota": "Borra y vuelve a crear mascotas.csv en la carpeta donde se ejecuta: "
             "por eso dos corridas seguidas dan la misma salida."},
]
