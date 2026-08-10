import java.util.ArrayList;

/**
 * VetCare - Clase 11: material para la revision cruzada.
 * Clinica Veterinaria Huellitas.
 *
 * Este archivo COMPILA y ARRANCA, pero tiene al menos siete hallazgos de
 * revision (correccion, diseno, legibilidad y manejo de errores) y termina
 * con una excepcion en tiempo de ejecucion. Eso es a proposito.
 *
 * Ejecutar:  java VetCareParaRevisar.java
 *
 * Instruccion para el estudiante: NO corrija nada todavia. Primero ejecutelo,
 * anote la salida real, aplique el checklist y escriba los hallazgos con el
 * formato Evidencia + Impacto + Sugerencia.
 */
public class VetCareParaRevisar {

    public static ArrayList<String[]> datos = new ArrayList<String[]>();

    public static void main(String[] args) {
        System.out.println("=== VetCare Huellitas (version para revisar) ===");

        int consecutivo = 1;
        proceso("M00" + consecutivo, "Firulais", "Canino", "4", "1144556677");
        consecutivo++;
        proceso("M00" + consecutivo, "Michi", "Felino", "2", "1098765432");
        consecutivo++;
        proceso("M00" + consecutivo, "Pelusa", "Felino", "-3", "1052233445");
        consecutivo++;
        proceso("M00" + consecutivo, "Nube", "Felino", "dos", "1052233446");

        System.out.println("Registros en memoria: " + datos.size());

        String[] encontrada = buscarPorId("M002");
        if (encontrada != null) {
            System.out.println("Busqueda 1 encontro a: " + encontrada[1]);
        } else {
            System.out.println("Busqueda 1 no encontro nada.");
        }

        imprimirFicha("M002");

        String[] fantasma = buscarDeNuevo("M009");
        System.out.println("Busqueda 3 devolvio: " + fantasma[1]);
    }

    public static void proceso(String a, String b, String c, String d, String e) {
        int x = 0;
        try {
            x = Integer.parseInt(d);
        } catch (Exception ex) {
        }
        if (x > 25) {
            System.out.println("edad rara");
        }
        String[] v = new String[5];
        v[0] = a;
        v[1] = b;
        v[2] = c;
        v[3] = String.valueOf(x);
        v[4] = e;
        datos.add(v);
        System.out.println("ok " + a + " " + b);
    }

    public static String[] buscarPorId(String id) {
        for (int i = 0; i < datos.size(); i++) {
            if (datos.get(i)[0] == id) {
                return datos.get(i);
            }
        }
        return null;
    }

    public static void imprimirFicha(String id) {
        for (int i = 0; i < datos.size(); i++) {
            if (datos.get(i)[0].equals(id)) {
                System.out.println("Ficha -> id=" + datos.get(i)[0]
                        + " nombre=" + datos.get(i)[1]
                        + " especie=" + datos.get(i)[2]
                        + " edad=" + datos.get(i)[3]
                        + " cc=" + datos.get(i)[4]);
            }
        }
    }

    public static String[] buscarDeNuevo(String id) {
        for (int i = 0; i < datos.size(); i++) {
            if (datos.get(i)[0].equals(id)) {
                return datos.get(i);
            }
        }
        return null;
    }
}
