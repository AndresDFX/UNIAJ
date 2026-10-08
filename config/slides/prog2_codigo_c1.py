# -*- coding: utf-8 -*-
"""Programacion II · Clase 1 · laminas de codigo: cada una es un Main.java que corre solo."""

CLASE = 1

LAMINAS = [
    {"k": 1, "titulo": "Crear objetos con new", "codigo": r"""
class Main {
    public static void main(String[] args) {
        // new crea el objeto y llama al constructor
        Mascota luna =
                new Mascota("M-001", "Luna", "Canino", 3);
        Mascota michi =
                new Mascota("M-002", "Michi", "Felino", 5);
        System.out.println("Pacientes registrados hoy:");
        System.out.println(luna);  // usa toString()
        System.out.println(michi);
    }
}

class Mascota {
    private String id;
    private String nombre;
    private String especie;
    private int edad;

    public Mascota(String id, String nombre, String especie,
                   int edad) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
    }

    @Override
    public String toString() {
        return id + " - " + nombre + " (" + especie + ", "
                + edad + " anios)";
    }
}
""", "salida": """
Pacientes registrados hoy:
M-001 - Luna (Canino, 3 anios)
M-002 - Michi (Felino, 5 anios)
"""},

    {"k": 5, "titulo": "setEdad(): el objeto se defiende", "codigo": r"""
class Main {
    public static void main(String[] args) {
        Mascota luna = new Mascota("Luna", 3);
        luna.setEdad(4);
        System.out.println(luna);
        luna.setEdad(-2);   // el objeto rechaza el dato
        System.out.println(luna);
    }
}

class Mascota {
    private String nombre;
    private int edad;

    public Mascota(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    /** El objeto se defiende: una edad negativa no tiene
     *  sentido en el dominio. */
    public void setEdad(int edad) {
        if (edad < 0) {
            System.out.println("Edad invalida, sigue en "
                    + this.edad);
            return;
        }
        this.edad = edad;
    }

    @Override
    public String toString() {
        return nombre + " (" + edad + " anios)";
    }
}
""", "salida": """
Luna (4 anios)
Edad invalida, sigue en 4
Luna (4 anios)
"""},

    {"k": 7, "titulo": "Atributos privados y constructor", "codigo": r"""
class Main {
    public static void main(String[] args) {
        Mascota rocky =
                new Mascota("M-003", "Rocky", "Canino", 9);
        // rocky.edad = -5;  no compila: edad es private
        System.out.println(rocky.getNombre() + " tiene "
                + rocky.getEdad() + " anios");
    }
}

class Mascota {
    private String id;      // nadie lo toca desde afuera
    private String nombre;
    private String especie;
    private int edad;

    public Mascota(String id, String nombre, String especie,
                   int edad) {
        this.id = id;   // this.id es el atributo
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
    }

    public String getId() { return id; }
    public String getNombre() { return nombre; }
    public String getEspecie() { return especie; }
    public int getEdad() { return edad; }
}
""", "salida": """
Rocky tiene 9 anios
"""},
]
