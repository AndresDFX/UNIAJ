# -*- coding: utf-8 -*-
"""Programacion II · Clase 14 · laminas de codigo: cada una es un Main.java que corre solo.

Ensayo de la sustentacion: guion, datos de demostracion, chequeo previo y ensayo cronometrado.
El ensayo mide tiempo real: su salida varia, por eso va con salida None (corre y termina).
"""

CLASE = 14

LAMINAS = [
    {"k": 1, "titulo": "El guion de la sustentación en código", "codigo": r"""
class Main {
    public static void main(String[] args) {
        int total = 0;
        for (String[] bloque : EnsayoSustentacionClinica.GUION) {
            System.out.println(bloque[2] + " min | " + bloque[0]);
            total += Integer.parseInt(bloque[2]);
        }
        System.out.println("Total planeado: " + total + " min");
    }
}

class EnsayoSustentacionClinica {
    // Guion: bloque, evidencia que se muestra en pantalla y minutos planeados.
    // Total 7 minutos, con la demo ocupando 4. No cambia por el numero de expositores.
    static final String[][] GUION = {
        {"Problema de la clinica y solucion propuesta", "Diapositiva con los 3 dolores", "1"},
        {"Arquitectura: clases, herencia y colecciones", "Persona.java al lado de Dueno.java", "1"},
        {"DEMO: registrar dueno y mascota (validacion de edad)", "La aplicacion corriendo", "2"},
        {"DEMO: agendar cita, buscar por ID y guardar en CSV", "Reabrir y ver los datos ahi", "2"},
        {"Limitaciones, aprendizajes y cierre", "Lista de 3 limitaciones", "1"}
    };
}
""", "salida": """
1 min | Problema de la clinica y solucion propuesta
1 min | Arquitectura: clases, herencia y colecciones
2 min | DEMO: registrar dueno y mascota (validacion de edad)
2 min | DEMO: agendar cita, buscar por ID y guardar en CSV
1 min | Limitaciones, aprendizajes y cierre
Total planeado: 7 min
"""},

    {"k": 2, "titulo": "sembrarDatosDemo(): datos creíbles", "codigo": r"""
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
class Main {
    private static final String CARPETA = "datos_demo";

    public static void main(String[] args) {
        sembrarDatosDemo();
    }

    /** Datos creibles: nombres reales, no 'prueba1'. */
    private static void sembrarDatosDemo() {
        File carpeta = new File(CARPETA);
        if (!carpeta.exists()) {
            carpeta.mkdirs();
        }

        // duenos.csv y citas.csv se siembran igual
        escribir(CARPETA + "/mascotas.csv", new String[]{
            "M-001;Firulais;Canino;Labrador;4;28.5;D-001",
            "M-002;Michi;Felino;Criollo;2;3.8;D-001",
            "M-003;Rocky;Canino;Pastor;6;32.0;D-002",
            "M-004;Luna;Felino;Siames;1;2.9;D-003"
        });
        System.out.println("Datos de demostracion listos"
                + " en la carpeta " + CARPETA);
    }

    private static void escribir(String ruta,
            String[] lineas) {
        try (PrintWriter salida = new PrintWriter(ruta)) {
            for (String linea : lineas) {
                salida.println(linea);
            }
            System.out.println("  [OK] " + ruta + " ("
                    + lineas.length + " registros)");
        } catch (FileNotFoundException e) {
            System.out.println("  [ERROR] No pude crear "
                    + ruta + ": " + e.getMessage());
        }
    }
}
""", "salida": """
  [OK] datos_demo/mascotas.csv (4 registros)
Datos de demostracion listos en la carpeta datos_demo
""", "nota": "Crea (o sobrescribe) la carpeta datos_demo con mascotas.csv donde se ejecuta."},

    {"k": 2, "titulo": "chequeoPreVuelo(): verde o no se presenta", "codigo": r"""
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
class Main {
    private static final String CARPETA = "datos_demo";

    public static void main(String[] args)
            throws IOException {
        Files.createDirectories(Path.of(CARPETA));
        crear("duenos.csv");
        crear("mascotas.csv");
        Files.deleteIfExists(Path.of(CARPETA, "citas.csv"));
        chequeoPreVuelo();
        crear("citas.csv");
        chequeoPreVuelo();
    }

    private static int contarFilas(String ruta) {
        try {
            return Files.readAllLines(Path.of(ruta)).size();
        } catch (IOException e) {
            return 0;   // no existe: es como estar vacio
        }
    }

    static void crear(String archivo) throws IOException {
        Files.writeString(Path.of(CARPETA, archivo), "x");
    }

    /** Si esto no da verde, no se comparte pantalla. */
    private static boolean chequeoPreVuelo() {
        String[] requeridos = {CARPETA + "/duenos.csv",
                CARPETA + "/mascotas.csv",
                CARPETA + "/citas.csv"};
        boolean listo = true;
        System.out.println("--- Chequeo pre-vuelo ---");
        for (String ruta : requeridos) {
            int filas = contarFilas(ruta);
            System.out.println((filas > 0 ? "  [OK]    "
                    : "  [FALLA] ") + ruta + " -> " + filas
                    + " filas");
            if (filas == 0) {
                listo = false;
            }
        }
        System.out.println(listo ? "  Listos para la demo."
                : "  Siembre los datos primero.");
        return listo;
    }
}
""", "salida": """
--- Chequeo pre-vuelo ---
  [OK]    datos_demo/duenos.csv -> 1 filas
  [OK]    datos_demo/mascotas.csv -> 1 filas
  [FALLA] datos_demo/citas.csv -> 0 filas
  Siembre los datos primero.
--- Chequeo pre-vuelo ---
  [OK]    datos_demo/duenos.csv -> 1 filas
  [OK]    datos_demo/mascotas.csv -> 1 filas
  [OK]    datos_demo/citas.csv -> 1 filas
  Listos para la demo.
""", "nota": "Crea la carpeta datos_demo donde se ejecuta; borra citas.csv al empezar para "
              "mostrar primero la FALLA y luego el verde."},

    {"k": 4, "titulo": "ensayo(): planeado contra real", "codigo": r"""
class Main {
    static final String[][] GUION = {
        {"Problema y solucion", "Los 3 dolores", "1"},
        {"Arquitectura", "Persona.java y Dueno.java", "1"},
        {"DEMO: dueno y mascota", "La app corriendo", "2"},
        {"DEMO: cita, busqueda y CSV", "Reabrir", "2"},
        {"Limitaciones y cierre", "3 limitaciones", "1"}
    };

    public static void main(String[] args)
            throws InterruptedException {
        long anterior = System.currentTimeMillis();
        for (int i = 0; i < GUION.length; i++) {
            String[] bloque = GUION[i];
            System.out.println("-> " + bloque[0]
                    + " | Evidencia: " + bloque[1]);
            Thread.sleep(200);   // en vivo: Enter
            long ahora = System.currentTimeMillis();
            double real = (ahora - anterior) / 60000.0;
            double plan = Double.parseDouble(bloque[2]);
            String veredicto =
                    real > plan ? "SE PASO" : "en tiempo";
            System.out.println(String.format(
                    "   Real: %.2f | Plan: %.0f min | %s",
                    real, plan, veredicto));
            anterior = ahora;
        }
    }
}
""", "salida": None, "nota": "Mide tiempo real, asi que la salida cambia en cada corrida. En el "
              "ensayo de verdad cada bloque termina con Enter (Scanner); aqui una pausa de "
              "0,2 s lo simula para que corra solo. El guion va abreviado para que quepa."},
]
