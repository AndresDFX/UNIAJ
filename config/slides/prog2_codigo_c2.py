# -*- coding: utf-8 -*-
"""Programacion II · Clase 2 · laminas de codigo: cada una es un Main.java que corre solo."""

CLASE = 2

LAMINAS = [
    {"k": 0, "titulo": "Del arreglo fijo a la lista que crece", "codigo": r"""
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

class Main {
    public static void main(String[] args) {
        Mascota nieve = new Mascota("M-004", "Nieve", 1);
        Mascota[] fichero = new Mascota[3]; // tamano fijo
        try {
            fichero[3] = nieve;   // no existe la posicion 3
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("El arreglo no crece");
        }

        List<Mascota> mascotas = new ArrayList<>();
        mascotas.add(nieve);      // add agrega al final
        mascotas.add(new Mascota("M-005", "Toby", 11));
        System.out.println("size() = " + mascotas.size());
        System.out.println("get(0) = " + mascotas.get(0));

        for (Mascota x : mascotas) {  // for-each: para LEER
            System.out.println(x);
        }

        // Iterator: para BORRAR mientras se recorre
        Iterator<Mascota> it = mascotas.iterator();
        while (it.hasNext()) {
            if (it.next().getEdad() >= 9) it.remove();
        }
        System.out.println("Quedan: " + mascotas);
    }
}

class Mascota {
    private final String id;
    private final String nombre;
    private final int edad;

    public Mascota(String id, String nombre, int edad) {
        this.id = id;
        this.nombre = nombre;
        this.edad = edad;
    }
    public int getEdad() { return edad; }
    @Override
    public String toString() {
        return id + " " + nombre + " (" + edad + ")";
    }
}
""", "salida": """
El arreglo no crece
size() = 2
get(0) = M-004 Nieve (1)
M-004 Nieve (1)
M-005 Toby (11)
Quedan: [M-004 Nieve (1)]
"""},

    {"k": 2, "titulo": "agregar(): validar antes de add", "codigo": r"""
import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) {
        RegistroMascotas registro = new RegistroMascotas();
        registro.agregar(new Mascota("M-001", "Firulais"));
        registro.agregar(new Mascota("M-001", "Copia"));
        registro.agregar(null);
    }
}

class Mascota {
    private final String id;
    private final String nombre;

    public Mascota(String id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }

    public String getId() { return id; }
    public String getNombre() { return nombre; }
}

class RegistroMascotas {
    // La lista vive privada: nadie la toca sin las reglas
    private final List<Mascota> mascotas =
            new ArrayList<>();
    public boolean agregar(Mascota m) {
        if (m == null) {
            System.out.println("Ficha nula, se rechaza");
            return false;
        }
        if (buscarPorId(m.getId()) != null) {
            System.out.println("ID repetido: " + m.getId());
            return false;
        }
        mascotas.add(m); // add siempre agrega al final
        System.out.println("Registrada: " + m.getNombre());
        return true;
    }

    public Mascota buscarPorId(String id) {
        for (Mascota m : mascotas) {
            if (m.getId().equals(id)) return m;
        }
        return null;
    }
}
""", "salida": """
Registrada: Firulais
ID repetido: M-001
Ficha nula, se rechaza
"""},

    {"k": 2, "titulo": "buscarPorId(): recorrer y comparar por id", "codigo": r"""
import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) {
        RegistroMascotas registro = new RegistroMascotas();
        registro.agregar(new Mascota("M-001", "Firulais"));
        registro.agregar(new Mascota("M-003", "Rocky"));
        System.out.println(registro.buscarPorId("m-003 "));
        System.out.println(registro.buscarPorId("M-099"));
    }
}

class Mascota {
    private final String id;
    private final String nombre;
    public Mascota(String id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }

    public String getId() { return id; }
    @Override
    public String toString() { return id + " " + nombre; }
}

class RegistroMascotas {
    private final List<Mascota> mascotas =
            new ArrayList<>();

    public void agregar(Mascota m) { mascotas.add(m); }

    public Mascota buscarPorId(String id) {
        if (id == null) {
            return null;
        }
        for (Mascota m : mascotas) { // solo para leer
            if (m.getId().equalsIgnoreCase(id.trim())) {
                return m;
            }
        }
        return null; // no esta: quien llama lo valida
    }
}
""", "salida": """
M-003 Rocky
null
"""},

    {"k": 2, "titulo": "eliminarPorId(): remove(Object)", "codigo": r"""
import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) {
        RegistroMascotas registro = new RegistroMascotas();
        registro.agregar(new Mascota("M-001", "Firulais"));
        registro.agregar(new Mascota("M-002", "Michi"));
        registro.eliminarPorId("M-002");
        registro.eliminarPorId("M-002");
    }
}

class Mascota {
    private final String id;
    private final String nombre;

    public Mascota(String id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }

    public String getId() { return id; }
    public String getNombre() { return nombre; }
}

class RegistroMascotas {
    private final List<Mascota> mascotas =
            new ArrayList<>();

    public void agregar(Mascota m) { mascotas.add(m); }

    public boolean eliminarPorId(String id) {
        Mascota m = buscarPorId(id);
        if (m == null) {
            System.out.println("No existe: " + id);
            return false;
        }
        mascotas.remove(m); // remove(Object), no por indice
        System.out.println("Retirada: " + m.getNombre());
        return true;
    }

    public Mascota buscarPorId(String id) {
        for (Mascota m : mascotas) {
            if (m.getId().equals(id)) return m;
        }
        return null;
    }
}
""", "salida": """
Retirada: Michi
No existe: M-002
"""},

    {"k": 3, "titulo": "listar(): el for con índice", "codigo": r"""
import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) {
        RegistroMascotas registro = new RegistroMascotas();
        registro.listar();
        registro.agregar(new Mascota("M-001", "Firulais"));
        registro.agregar(new Mascota("M-002", "Michi"));
        registro.listar();
        System.out.println("Total: " + registro.cantidad());
    }
}

class Mascota {
    private final String id;
    private final String nombre;
    public Mascota(String id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }

    @Override
    public String toString() { return id + " " + nombre; }
}

class RegistroMascotas {
    private final List<Mascota> mascotas =
            new ArrayList<>();

    public void agregar(Mascota m) { mascotas.add(m); }

    public void listar() {
        if (mascotas.isEmpty()) {
            System.out.println("(no hay mascotas)");
            return;
        }
        // ojo: i < size(), nunca <=
        for (int i = 0; i < mascotas.size(); i++) {
            System.out.println((i + 1) + ". "
                    + mascotas.get(i));
        }
    }

    public int cantidad() {
        return mascotas.size();
    }
}
""", "salida": """
(no hay mascotas)
1. M-001 Firulais
2. M-002 Michi
Total: 2
"""},

    {"k": 3, "titulo": "pasarAGeriatria(): borrar con Iterator", "codigo": r"""
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

class Main {
    public static void main(String[] args) {
        RegistroMascotas registro = new RegistroMascotas();
        registro.agregar(new Mascota("Firulais", 4));
        registro.agregar(new Mascota("Rocky", 9));
        registro.agregar(new Mascota("Toby", 11));
        registro.pasarAGeriatria(9);
        System.out.println("Total: " + registro.cantidad());
    }
}

class Mascota {
    private final String nombre;
    private final int edad;
    public Mascota(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
    public String getNombre() { return nombre; }
    public int getEdad() { return edad; }
}

class RegistroMascotas {
    private final List<Mascota> mascotas =
            new ArrayList<>();

    public void agregar(Mascota m) { mascotas.add(m); }
    public int cantidad() { return mascotas.size(); }

    public void pasarAGeriatria(int edadMinima) {
        Iterator<Mascota> it = mascotas.iterator();
        while (it.hasNext()) {
            Mascota m = it.next();
            if (m.getEdad() >= edadMinima) {
                it.remove(); // unica forma segura de borrar
                System.out.println("Pasa a geriatria: "
                        + m.getNombre());
            }
        }
    }
}
""", "salida": """
Pasa a geriatria: Rocky
Pasa a geriatria: Toby
Total: 1
"""},

    {"k": 4, "titulo": "Mascota: atributos privados y toString()", "codigo": r"""
class Main {
    public static void main(String[] args) {
        Mascota m = new Mascota("M-001", "Firulais",
                "Canino", 4, "Ana Gomez");
        System.out.println(m);   // llama a toString()
    }
}

class Mascota {
    private final String id;
    private final String nombre;
    private final String especie;
    private final int edad;
    private final String dueno;

    public Mascota(String id, String nombre, String especie,
                   int edad, String dueno) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
        this.dueno = dueno;
    }

    @Override
    public String toString() {
        return id + " | " + nombre + " (" + especie + ", "
                + edad + " anios) - dueno: " + dueno;
    }
}
""", "salida": """
M-001 | Firulais (Canino, 4 anios) - dueno: Ana Gomez
"""},
]
