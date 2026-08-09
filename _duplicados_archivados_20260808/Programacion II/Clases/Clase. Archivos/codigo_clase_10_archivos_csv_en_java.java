import java.io.*;
import java.util.Scanner;

public class GestorPacientesCSV {

    // Definimos el nombre del archivo y el separador estándar para CSV
    private static final String ARCHIVO_CSV = "pacientes.csv";
    private static final String SEPARADOR = ",";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcion = 0;

        // Menú principal del Sistema VetCare (Independiente del IDE)
        while (opcion != 3) {
            System.out.println("\n--- Módulo VetCare: Historial CSV ---");
            System.out.println("1. Registrar nuevo paciente");
            System.out.println("2. Leer historial de pacientes");
            System.out.println("3. Salir");
            System.out.print("Elija una opción: ");
            
            try {
                opcion = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Por favor, ingrese un número válido.");
                continue;
            }

            switch (opcion) {
                case 1:
                    System.out.print("Nombre del paciente: ");
                    String nombre = scanner.nextLine();
                    System.out.print("Especie (Ej. Perro, Gato): ");
                    String especie = scanner.nextLine();
                    System.out.print("Edad: ");
                    String edad = scanner.nextLine(); // Se lee como String por simplicidad
                    
                    guardarPacienteCSV(nombre, especie, edad);
                    break;
                case 2:
                    leerPacientesCSV();
                    break;
                case 3:
                    System.out.println("Cerrando sistema VetCare...");
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
        }
        scanner.close();
    }

    /**
     * Guarda un paciente en el archivo CSV.
     * Utiliza el parámetro 'true' en FileWriter para no sobreescribir el archivo.
     */
    public static void guardarPacienteCSV(String nombre, String especie, String edad) {
        try (FileWriter fw = new FileWriter(ARCHIVO_CSV, true);
             PrintWriter pw = new PrintWriter(fw)) {
            
            // Se construye la línea con el formato: nombre,especie,edad
            String lineaCSV = nombre + SEPARADOR + especie + SEPARADOR + edad;
            pw.println(lineaCSV);
            
            System.out.println("[ÉXITO] Paciente guardado correctamente en el archivo CSV.");
            
        } catch (IOException e) {
            System.out.println("[ERROR] Ocurrió un problema al guardar el archivo: " + e.getMessage());
        }
    }

    /**
     * Lee el archivo CSV, separa los datos por comas y los muestra tabulados.
     */
    public static void leerPacientesCSV() {
        File archivo = new File(ARCHIVO_CSV);
        
        if (!archivo.exists()) {
            System.out.println("El historial está vacío. Aún no hay pacientes registrados.");
            return;
        }

        try (BufferedReader br = new BufferedReader(new FileReader(archivo))) {
            String linea;
            System.out.println("\n--- Lista de Pacientes VetCare ---");
            System.out.printf("%-15s %-15s %-5s%n", "NOMBRE", "ESPECIE", "EDAD");
            System.out.println("----------------------------------------");
            
            // Lee línea por línea
            while ((linea = br.readLine()) != null) {
                // Parseo: Se divide la línea donde encuentre la coma
                String[] datos = linea.split(SEPARADOR);
                
                // Validación para evitar errores si una línea está mal formateada
                if (datos.length == 3) {
                    System.out.printf("%-15s %-15s %-5s%n", datos[0], datos[1], datos[2]);
                }
            }
        } catch (IOException e) {
            System.out.println("[ERROR] No se pudo leer el archivo: " + e.getMessage());
        }
    }
}