package vetcare;

/**
 * VetCare - Clinica Veterinaria Huellitas
 * Clase 1: primera clase del dominio. Es el molde a partir del cual se crean
 * los objetos Mascota; todo el proyecto se apoya en ella.
 */
public class Mascota {

    private String id;
    private String nombre;
    private String especie;
    private int edad;

    public Mascota(String id, String nombre, String especie, int edad) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
    }

    public String getId() { return id; }
    public String getNombre() { return nombre; }
    public String getEspecie() { return especie; }
    public int getEdad() { return edad; }

    /** El objeto se defiende: una edad negativa no tiene sentido en el dominio. */
    public void setEdad(int edad) {
        if (edad < 0) {
            System.out.println("Edad invalida, se conserva la anterior: " + this.edad);
            return;
        }
        this.edad = edad;
    }

    @Override
    public String toString() {
        return id + " - " + nombre + " (" + especie + ", " + edad + " anios)";
    }

    public static void main(String[] args) {
        Mascota luna = new Mascota("M-001", "Luna", "Canino", 3);
        Mascota michi = new Mascota("M-002", "Michi", "Felino", 5);
        System.out.println("Pacientes registrados hoy en Huellitas:");
        System.out.println(luna);
        System.out.println(michi);
        luna.setEdad(-2);
    }
}
