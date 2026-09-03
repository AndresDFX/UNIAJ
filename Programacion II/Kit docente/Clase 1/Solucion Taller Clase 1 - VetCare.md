# Solucion Taller · Clase 1 · Introduccion a la Programacion Orientada a Objetos

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

## Solucion paso a paso
1. Paso 1 resuelto. En VS Code, con el Extension Pack for Java ya instalado: paleta de comandos (Ctrl+Shift+P) > «Java: Create Java Project» > «No build tools» > elegir carpeta y nombrar el proyecto VetCare. Queda una carpeta src/; dentro se crea el paquete vetcare (clic derecho en src > New Java Package) y ahi la clase con el main. Si VS Code no encuentra el JDK, se corre «Java: Configure Java Runtime» y se apunta el JDK 17+. Este es el paso que mas tiempo consume el primer dia: conviene circular por los puestos en vez de avanzar.
2. Paso 2 resuelto. La clase queda: public class Mascota { private String id; private String nombre; private String especie; public Mascota(String id, String nombre, String especie) { this.id = id; this.nombre = nombre; this.especie = especie; } }. El this. distingue el atributo del parametro que tiene el mismo nombre; sin el, el atributo queda en null.
3. Paso 3 resuelto. El getter es public String getNombre() { return nombre; } y el toString queda: @Override public String toString() { return id + " - " + nombre + " (" + especie + ")"; }. La anotacion @Override no es obligatoria, pero avisa en compilacion si uno escribe mal el nombre del metodo (por ejemplo toSting).
4. Paso 4 resuelto. En el main: Mascota luna = new Mascota("M-001", "Luna", "Canino"); Mascota michi = new Mascota("M-002", "Michi", "Felino"); System.out.println(luna); System.out.println(michi); Deben salir dos lineas distintas: ahi se ve, sin explicarlo, la diferencia entre clase (el molde) y objeto (cada mascota concreta).

## Rubrica corta
- [ ] Entorno funcionando (3)
- [ ] Clase Mascota con atributos private (3)
- [ ] Constructor completo con this. (2)
- [ ] Dos objetos distintos impresos legiblemente (2)

## Errores frecuentes
- Dejar los atributos public 'para que sea mas facil': rompe el encapsulamiento desde el primer dia y despues cuesta corregirlo.
- Olvidar el this. en el constructor: el atributo queda en null y el programa falla con NullPointerException al imprimir.
- No sobreescribir toString(): imprime la direccion de memoria y el estudiante cree que el programa fallo.

Codigo de apoyo: `Kit docente/Clase 1/Codigo/Mascota.java`