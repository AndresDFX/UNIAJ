# -*- coding: utf-8 -*-
"""Programacion II · Clase 11 · laminas de codigo: cada una es un Main.java que corre solo.

Es el codigo A REVISAR: malo a proposito en lo que la lamina critica, pero compila y corre.
"""

CLASE = 11

LAMINAS = [
    {"k": 0, "titulo": "El código a revisar: main()", "codigo": r"""
import java.util.ArrayList;
class Main {
    public static void main(String[] args) {
        try {
            ClinicaParaRevisar.main(args);
        } catch (NullPointerException e) {
            System.out.println("Se cayo en fantasma[1]");
        }
    }
}

class ClinicaParaRevisar {
    static ArrayList<String[]> datos = new ArrayList<>();

    public static void main(String[] args) {
        int consecutivo = 1;
        proceso("M00" + consecutivo, "Firulais", "Canino",
                "4", "1144556677");
        consecutivo++;
        proceso("M00" + consecutivo, "Michi", "Felino",
                "2", "1098765432");
        consecutivo++;
        proceso("M00" + consecutivo, "Pelusa", "Felino",
                "-3", "1052233445");
        consecutivo++;

        proceso("M00" + consecutivo, "Nube", "Felino",
                "dos", "1052233446");
        System.out.println("Registros en memoria: "
                + datos.size());
        String[] fantasma = buscarDeNuevo("M009");
        System.out.println("Busqueda 3 devolvio: "
                + fantasma[1]);
    }

    public static void proceso(String a, String b,
            String c, String d, String e) {
        datos.add(new String[]{a, b, c, d, e});
        System.out.println("ok " + a + " " + b);
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
""", "salida": """
ok M001 Firulais
ok M002 Michi
ok M003 Pelusa
ok M004 Nube
Registros en memoria: 4
Se cayo en fantasma[1]
""", "nota": "Main envuelve la llamada en un try solo para que la lamina termine: sin el, "
              "ClinicaParaRevisar.main se cae con NullPointerException en fantasma[1]."},

    {"k": 1, "titulo": "proceso(): ¿qué capas fallan?", "codigo": r"""
import java.util.ArrayList;

class Main {
    public static void main(String[] args) {
        ClinicaParaRevisar.proceso("M001", "Firulais",
                "Canino", "4", "1144556677");
        ClinicaParaRevisar.proceso("M003", "Pelusa",
                "Felino", "-3", "1052233445");
        ClinicaParaRevisar.proceso("M004", "Nube",
                "Felino", "dos", "1052233446");
        for (String[] v : ClinicaParaRevisar.datos) {
            System.out.println(String.join(";", v));
        }
    }
}

class ClinicaParaRevisar {
    static ArrayList<String[]> datos = new ArrayList<>();

    public static void proceso(String a, String b,
            String c, String d, String e) {
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
}
""", "salida": """
ok M001 Firulais
ok M003 Pelusa
ok M004 Nube
M001;Firulais;Canino;4;1144556677
M003;Pelusa;Felino;-3;1052233445
M004;Nube;Felino;0;1052233446
"""},

    {"k": 2, "titulo": "Dos búsquedas casi iguales", "codigo": r"""
import java.util.ArrayList;

class Main {
    public static void main(String[] args) {
        int n = 2;
        ClinicaParaRevisar.datos.add(
                new String[]{"M00" + n, "Michi"});
        String[] a = ClinicaParaRevisar.buscarPorId("M002");
        String[] b =
                ClinicaParaRevisar.buscarDeNuevo("M002");
        System.out.println("buscarPorId: " + a);
        System.out.println("buscarDeNuevo: " + b[1]);
    }
}

class ClinicaParaRevisar {
    static ArrayList<String[]> datos = new ArrayList<>();

    public static String[] buscarPorId(String id) {
        for (int i = 0; i < datos.size(); i++) {
            if (datos.get(i)[0] == id) {
                return datos.get(i);
            }
        }
        return null;
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
""", "salida": """
buscarPorId: null
buscarDeNuevo: Michi
"""},

    {"k": 3, "titulo": "imprimirFicha(): el mismo bucle otra vez", "codigo": r"""
import java.util.ArrayList;

class Main {
    public static void main(String[] args) {
        ClinicaParaRevisar.datos.add(new String[]{
            "M002", "Michi", "Felino", "2", "1098765432"});
        ClinicaParaRevisar.imprimirFicha("M002");
        ClinicaParaRevisar.imprimirFicha("M009");
        System.out.println("(M009 no imprimio nada)");
    }
}

class ClinicaParaRevisar {
    static ArrayList<String[]> datos = new ArrayList<>();

    public static void imprimirFicha(String id) {
        for (int i = 0; i < datos.size(); i++) {
            if (datos.get(i)[0].equals(id)) {
                System.out.println("Ficha -> id="
                        + datos.get(i)[0]
                        + " nombre=" + datos.get(i)[1]
                        + " especie=" + datos.get(i)[2]
                        + " edad=" + datos.get(i)[3]
                        + " cc=" + datos.get(i)[4]);
            }
        }
    }
}
""", "salida": """
Ficha -> id=M002 nombre=Michi especie=Felino edad=2 cc=1098765432
(M009 no imprimio nada)
"""},
]
