import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * VetCare - Clinica Veterinaria Huellitas
 * Clase 14: preparacion de la sustentacion final.
 * 1) Siembra el juego de datos de demostracion.
 * 2) Chequeo pre-vuelo antes de conectar el videobeam.
 * 3) Ensayo cronometrado de 5 a 8 minutos.
 * Trabajo individual por defecto: si el docente autoriza equipo, agregue los nombres
 * en PRESENTADORES y el reparto de bloques se hace automatico.
 * Ejecutar en Apache NetBeans: clic derecho sobre el archivo y luego Run File.
 */
public class EnsayoSustentacionVetCare {

    private static final String CARPETA = "datos_demo";

    // Modalidad de trabajo: INDIVIDUAL por defecto. Si el docente autoriza equipo de 2 o 3,
    // escriba los nombres aqui y el reparto de bloques se calcula solo.
    // Individual: {"Usted"}   |   Equipo: {"Marta", "Julian", "Sara"}
    private static final String[] PRESENTADORES = {"Usted"};

    // Guion: bloque, evidencia que se muestra en pantalla y minutos planeados.
    // Total 7 minutos, con la demo ocupando 4. El guion no cambia por el numero de expositores.
    private static final String[][] GUION = {
        {"Problema de la clinica Huellitas y solucion propuesta", "Diapositiva con los 3 dolores", "1"},
        {"Arquitectura: clases, herencia y colecciones", "Persona.java al lado de Dueno.java", "1"},
        {"DEMO: registrar dueno y mascota (con validacion de edad)", "La aplicacion corriendo", "2"},
        {"DEMO: agendar cita, buscar por ID y guardar en CSV", "Cerrar y reabrir con los datos ahi", "2"},
        {"Limitaciones, aprendizajes y cierre", "Lista de 3 limitaciones", "1"}
    };

    /** Quien habla el bloque i. Con un solo presentador, todos los bloques son suyos. */
    private static String responsableDe(int i) {
        if (PRESENTADORES.length == 0) {
            return "Usted";
        }
        return PRESENTADORES[i % PRESENTADORES.length];
    }

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        boolean seguir = true;
        while (seguir) {
            System.out.println("");
            System.out.println("=== VetCare | Preparacion de la sustentacion ===");
            System.out.println("1. Sembrar datos de demostracion");
            System.out.println("2. Chequeo pre-vuelo");
            System.out.println("3. Ensayo cronometrado");
            System.out.println("4. Salir");
            System.out.print("Opcion: ");
            String opcion = teclado.nextLine().trim();
            switch (opcion) {
                case "1":
                    sembrarDatosDemo();
                    break;
                case "2":
                    chequeoPreVuelo();
                    break;
                case "3":
                    if (chequeoPreVuelo()) {
                        ensayo(teclado);
                    } else {
                        System.out.println("Primero siembre los datos: nadie ensaya con la aplicacion vacia.");
                    }
                    break;
                case "4":
                    seguir = false;
                    break;
                default:
                    System.out.println("Opcion no valida.");
            }
        }
        teclado.close();
        System.out.println("Recuerde: dos ensayos cronometrados antes de sustentar.");
    }

    /** Datos creibles del dominio veterinario: nombres reales, no 'prueba1' ni 'aaa'. */
    private static void sembrarDatosDemo() {
        File carpeta = new File(CARPETA);
        if (!carpeta.exists()) {
            carpeta.mkdirs();
        }
        escribir(CARPETA + "/duenos.csv", new String[]{
            "D-001;Marta Lopez;3155551212;Calle 5 #23-41",
            "D-002;Julian Perez;3009998877;Carrera 8 #12-30",
            "D-003;Sara Quintero;3126665544;Avenida 4N #10-15"
        });
        escribir(CARPETA + "/mascotas.csv", new String[]{
            "M-001;Firulais;Canino;Labrador;4;28.5;D-001",
            "M-002;Michi;Felino;Criollo;2;3.8;D-001",
            "M-003;Rocky;Canino;Pastor;6;32.0;D-002",
            "M-004;Luna;Felino;Siames;1;2.9;D-003"
        });
        escribir(CARPETA + "/citas.csv", new String[]{
            "C-001;M-001;08:00;Vacunacion anual;Programada",
            "C-002;M-003;09:30;Control de peso;Programada",
            "C-003;M-004;11:00;Desparasitacion;Atendida"
        });
        System.out.println("Datos de demostracion listos en la carpeta " + CARPETA);
    }

    private static void escribir(String ruta, String[] lineas) {
        try (PrintWriter salida = new PrintWriter(ruta)) {
            for (String linea : lineas) {
                salida.println(linea);
            }
            System.out.println("  [OK] " + ruta + " (" + lineas.length + " registros)");
        } catch (FileNotFoundException e) {
            System.out.println("  [ERROR] No pude crear " + ruta + ": " + e.getMessage());
        }
    }

    /** Si esto no da verde, no se conecta el videobeam. */
    private static boolean chequeoPreVuelo() {
        String[] requeridos = {CARPETA + "/duenos.csv", CARPETA + "/mascotas.csv", CARPETA + "/citas.csv"};
        boolean listo = true;
        System.out.println("--- Chequeo pre-vuelo ---");
        for (String ruta : requeridos) {
            int filas = contarFilas(ruta);
            System.out.println((filas > 0 ? "  [OK]    " : "  [FALLA] ") + ruta + " -> " + filas + " filas");
            if (filas == 0) {
                listo = false;
            }
        }
        System.out.println(listo ? "  Listos para la demo en vivo." : "  Siembre los datos con la opcion 1 antes de continuar.");
        return listo;
    }

    private static int contarFilas(String ruta) {
        int filas = 0;
        try (BufferedReader lector = new BufferedReader(new FileReader(ruta))) {
            while (lector.readLine() != null) {
                filas++;
            }
        } catch (IOException e) {
            // El archivo no existe o no se puede leer: para la demo es lo mismo que estar vacio.
            return 0;
        }
        return filas;
    }

    /** Cronometro real: se avanza con Enter al terminar cada bloque. */
    private static void ensayo(Scanner teclado) {
        System.out.println("--- Ensayo cronometrado. Presione Enter al terminar cada bloque ---");
        long inicio = System.currentTimeMillis();
        long anterior = inicio;
        for (int i = 0; i < GUION.length; i++) {
            String[] bloque = GUION[i];
            System.out.println("");
            System.out.println("-> " + bloque[0]);
            System.out.println("   Evidencia: " + bloque[1]);
            System.out.println("   Habla: " + responsableDe(i) + " | Planeado: " + bloque[2] + " min");
            teclado.nextLine();
            long ahora = System.currentTimeMillis();
            double real = (ahora - anterior) / 60000.0;
            double plan = Double.parseDouble(bloque[2]);
            String veredicto = real > plan ? "SE PASO" : "en tiempo";
            System.out.println(String.format("   Real: %.2f min | Planeado: %.0f min | %s", real, plan, veredicto));
            anterior = ahora;
        }
        double total = (System.currentTimeMillis() - inicio) / 60000.0;
        System.out.println(String.format("TOTAL: %.2f min", total));
        if (total < 5) {
            System.out.println("Muy corto: falto profundidad en la demo. Meta: entre 5 y 8 minutos.");
        } else if (total > 8) {
            System.out.println("Se paso: recorte la parte teorica, nunca la demo.");
        } else {
            System.out.println("Tiempo dentro de la ventana. Repita el ensayo una vez mas.");
        }
    }
}
