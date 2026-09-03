package vetcare;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

/**
 * VetCare - Clase 2: de arreglos fijos a ArrayList.
 * Clinica Veterinaria Huellitas.
 * Archivo unico: en VS Code, el boton Run que aparece sobre el metodo main (o Ctrl+F5).
 * Los bloques 1 a 4 corren solos; el bloque 5 abre el menu y pide datos por consola.
 */
public class VetCareRegistroMascotas {

    public static void main(String[] args) {

        System.out.println("=== 1. El arreglo fijo se queda corto ===");
        Mascota[] fichero = new Mascota[3]; // el tamano se decide hoy y ya no cambia
        fichero[0] = new Mascota("M-001", "Firulais", "Canino", 4, "Ana Gomez");
        fichero[1] = new Mascota("M-002", "Michi", "Felino", 2, "Luis Perez");
        fichero[2] = new Mascota("M-003", "Rocky", "Canino", 9, "Ana Gomez");
        try {
            fichero[3] = new Mascota("M-004", "Nieve", "Felino", 1, "Sara Diaz");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("No cabe la cuarta mascota: fichero.length = " + fichero.length);
        }

        System.out.println();
        System.out.println("=== 2. El mismo caso con ArrayList ===");
        RegistroMascotas registro = new RegistroMascotas();
        for (Mascota m : fichero) {
            registro.agregar(m);
        }
        registro.agregar(new Mascota("M-004", "Nieve", "Felino", 1, "Sara Diaz"));
        registro.agregar(new Mascota("M-005", "Toby", "Canino", 11, "Sara Diaz"));
        registro.agregar(new Mascota("M-001", "Firulais repetida", "Canino", 4, "Ana Gomez"));
        System.out.println("size() = " + registro.cantidad() + " (la lista crecio sola)");

        System.out.println();
        System.out.println("=== 3. Recorrido y busqueda por ID ===");
        registro.listar();
        System.out.println("buscarPorId(M-003) -> " + registro.buscarPorId("M-003"));
        System.out.println("buscarPorId(M-099) -> " + registro.buscarPorId("M-099"));

        System.out.println();
        System.out.println("=== 4. Eliminar sin romper el recorrido ===");
        registro.eliminarPorId("M-002");
        registro.pasarAGeriatria(9); // con Iterator: borrar en un for-each lanza excepcion
        registro.listar();
        System.out.println("Total activo: " + registro.cantidad());

        System.out.println();
        System.out.println("=== 5. Menu de consola (el main nunca toca la lista) ===");
        menu(registro);
    }

    /** El menu solo conversa con RegistroMascotas: no conoce la lista por dentro. */
    private static void menu(RegistroMascotas registro) {
        Scanner sc = new Scanner(System.in);
        int opcion = 0;
        while (opcion != 5) {
            System.out.println();
            System.out.println("1-Agregar  2-Listar  3-Buscar por ID  4-Eliminar  5-Salir");
            System.out.print("Opcion: ");
            if (!sc.hasNextLine()) {
                break; // la consola no tiene mas entrada disponible
            }
            try {
                opcion = Integer.parseInt(sc.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.println("Escriba un numero del 1 al 5");
                continue;
            }
            switch (opcion) {
                case 1:
                    System.out.print("ID: ");
                    String id = sc.nextLine().trim();
                    System.out.print("Nombre: ");
                    String nombre = sc.nextLine().trim();
                    System.out.print("Especie: ");
                    String especie = sc.nextLine().trim();
                    System.out.print("Edad: ");
                    int edad = leerEntero(sc);
                    System.out.print("Dueno: ");
                    String dueno = sc.nextLine().trim();
                    registro.agregar(new Mascota(id, nombre, especie, edad, dueno));
                    break;
                case 2:
                    registro.listar();
                    break;
                case 3:
                    System.out.print("ID a buscar: ");
                    Mascota encontrada = registro.buscarPorId(sc.nextLine().trim());
                    System.out.println(encontrada != null ? encontrada : "No existe esa mascota");
                    break;
                case 4:
                    System.out.print("ID a eliminar: ");
                    registro.eliminarPorId(sc.nextLine().trim());
                    break;
                case 5:
                    System.out.println("Hasta luego");
                    break;
                default:
                    System.out.println("Opcion no valida");
            }
        }
    }

    private static int leerEntero(Scanner sc) {
        try {
            return Integer.parseInt(sc.nextLine().trim());
        } catch (NumberFormatException e) {
            System.out.println("Edad invalida: se registra 0");
            return 0;
        }
    }
}

class Mascota {

    private final String id;
    private final String nombre;
    private final String especie;
    private final int edad;
    private final String dueno;

    public Mascota(String id, String nombre, String especie, int edad, String dueno) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
        this.dueno = dueno;
    }

    public String getId() { return id; }
    public String getNombre() { return nombre; }
    public String getEspecie() { return especie; }
    public int getEdad() { return edad; }
    public String getDueno() { return dueno; }

    @Override
    public String toString() {
        return id + " | " + nombre + " (" + especie + ", " + edad + " anios) - dueno: " + dueno;
    }
}

class RegistroMascotas {

    // La lista vive privada: nadie le mete mano sin pasar por las reglas del negocio
    private final List<Mascota> mascotas = new ArrayList<>();

    public boolean agregar(Mascota m) {
        if (m == null) {
            System.out.println("Ficha nula, no se registra");
            return false;
        }
        if (buscarPorId(m.getId()) != null) {
            System.out.println("ID repetido, se rechaza: " + m.getId());
            return false;
        }
        mascotas.add(m); // add siempre agrega al final
        System.out.println("Registrada: " + m.getNombre());
        return true;
    }

    public Mascota buscarPorId(String id) {
        if (id == null) {
            return null;
        }
        for (Mascota m : mascotas) { // for-each: solo para leer
            if (m.getId().equalsIgnoreCase(id.trim())) {
                return m;
            }
        }
        return null; // null = no esta; quien llama debe validarlo
    }

    public boolean eliminarPorId(String id) {
        Mascota m = buscarPorId(id);
        if (m == null) {
            System.out.println("No existe la mascota " + id);
            return false;
        }
        mascotas.remove(m); // remove(Object), no remove(indice)
        System.out.println("Retirada de la lista activa: " + m.getNombre());
        return true;
    }

    public void pasarAGeriatria(int edadMinima) {
        Iterator<Mascota> it = mascotas.iterator();
        while (it.hasNext()) {
            Mascota m = it.next();
            if (m.getEdad() >= edadMinima) {
                it.remove(); // unica forma segura de borrar mientras se recorre
                System.out.println("Pasa a control geriatrico: " + m.getNombre());
            }
        }
    }

    public void listar() {
        if (mascotas.isEmpty()) {
            System.out.println("(no hay mascotas registradas)");
            return;
        }
        for (int i = 0; i < mascotas.size(); i++) { // ojo: < size(), nunca <=
            System.out.println((i + 1) + ". " + mascotas.get(i));
        }
    }

    public int cantidad() {
        return mascotas.size();
    }
}
