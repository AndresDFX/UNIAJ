# Taller de la Clase 2 en ExamLab - configuracion

- **Curso:** Programacion II (FI303204)
- **Taller:** Taller Clase 2 en ExamLab - Colecciones dinamicas con ArrayList
- **Preguntas:** 6 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** El registro de mascotas de VetCare deja de vivir en un arreglo de tamano fijo y pasa a un ArrayList<Mascota> que crece con la clinica.
- **Entregable de la clase:** Proyecto NetBeans con las clases Mascota y RegistroMascotas y un menu de consola que agrega, lista, busca por ID y elimina mascotas, comprimido y subido a ExamLab.

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante convierte el registro de mascotas de VetCare en un ArrayList<Mascota> encapsulado que agrega sin duplicar IDs, lista, busca, elimina y depura por edad con Iterator, y entrega el menu de consola completo.

---

## Pregunta 1 - Codigo ejecutable · 25 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## `RegistroMascotas`: una lista que crece con la clinica

`Mascota[] fichas = new Mascota[3];` revienta cuando llega la cuarta mascota. Reemplacelo por un `ArrayList<Mascota>` **encapsulado** dentro de la clase `RegistroMascotas`.

La clase `Mascota` ya viene completa en el starter. Complete `RegistroMascotas`:

1. El atributo ya esta declarado: `private final List<Mascota> mascotas = new ArrayList<>();` (declarado como `List`, creado como `ArrayList`).
2. `existeId(String id)`: recorre con for-each y devuelve `true` si alguna ficha tiene ese ID. **Compare con `equals`, nunca con `==`.**
3. `agregar(Mascota m)`: si el ID ya existe, avisa y **no agrega**; si no existe, agrega y confirma.
4. `cantidad()`: devuelve el tamano real de la lista.

El `main` ya intenta agregar M-001 Firulais, M-002 Michi y **otra vez** M-001.

**Al ejecutar debe imprimir exactamente:**

```
Ficha agregada: M-001 Firulais
Ficha agregada: M-002 Michi
ID repetido: M-001 ya esta registrado
Total de fichas: 2
```

La ultima linea es la prueba de la regla: aunque se intento tres veces, el registro tiene **2** fichas.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        RegistroMascotas registro = new RegistroMascotas();

        registro.agregar(new Mascota("M-001", "Firulais", "canino", 4, "Ana Gomez"));
        registro.agregar(new Mascota("M-002", "Michi", "felino", 2, "Carlos Ruiz"));
        registro.agregar(new Mascota("M-001", "Firulais", "canino", 4, "Ana Gomez"));

        System.out.println("Total de fichas: " + registro.cantidad());
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

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    @Override
    public String toString() {
        return "Mascota " + id + " -> " + nombre + " (" + especie + ", " + edad
                + " anios), dueno: " + dueno;
    }
}

class RegistroMascotas {

    private final List<Mascota> mascotas = new ArrayList<>();

    public void agregar(Mascota m) {
        // TODO: si existeId(m.getId()) imprima
        //       "ID repetido: M-001 ya esta registrado" y NO agregue nada.
        // TODO: si no existe, agreguela a la lista e imprima
        //       "Ficha agregada: M-001 Firulais"
    }

    public boolean existeId(String id) {
        // TODO: recorra la lista con for-each y devuelva true si algun elemento
        //       tiene ese id (compare con equals, nunca con ==)
        return false;
    }

    public int cantidad() {
        // TODO: devuelva el tamano real de la lista
        return 0;
    }
}
```

**Rubrica esperada (campo Rubrica):**

La lista es private final y esta declarada como List creada con ArrayList. existeId compara con equals y agregar rechaza el ID repetido sin aumentar el tamano. cantidad() devuelve size(). No se declara ningun tamano fijo. Las cuatro lineas de salida coinciden exactamente.

---

## Pregunta 2 - Codigo ejecutable · 25 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## Listar con `for` indexado y buscar con `for-each`

Las seis fichas del escenario ya estan cargadas en el `main`:

| ID | Nombre | Especie | Edad | Dueno |
|----|--------|---------|------|-------|
| M-001 | Firulais | canino | 4 | Ana Gomez |
| M-002 | Michi | felino | 2 | Carlos Ruiz |
| M-003 | Rocky | canino | 9 | Luisa Perez |
| M-004 | Canela | felino | 11 | Marta Diaz |
| M-005 | Toby | canino | 1 | Diego Salas |
| M-006 | Nube | felino | 6 | Sofia Lara |

Implemente dos metodos, cada uno con un recorrido distinto **a proposito**:

1. `listar()`: encabezado con el total y luego cada ficha **numerada desde 1**, recorriendo con `for` **indexado** (necesita el indice para numerar).
2. `buscarPorId(String id)`: recorre con **for-each** y devuelve la `Mascota` o `null` si no existe (el `main` ya trata el caso `null`; su codigo no debe lanzar `NullPointerException`).

**Al ejecutar debe imprimir exactamente:**

```
--- Registro de mascotas (6) ---
1. Mascota M-001 -> Firulais (canino, 4 anios), dueno: Ana Gomez
2. Mascota M-002 -> Michi (felino, 2 anios), dueno: Carlos Ruiz
3. Mascota M-003 -> Rocky (canino, 9 anios), dueno: Luisa Perez
4. Mascota M-004 -> Canela (felino, 11 anios), dueno: Marta Diaz
5. Mascota M-005 -> Toby (canino, 1 anios), dueno: Diego Salas
6. Mascota M-006 -> Nube (felino, 6 anios), dueno: Sofia Lara
Encontrada: Mascota M-003 -> Rocky (canino, 9 anios), dueno: Luisa Perez
No existe ninguna mascota con ID M-099
```

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        RegistroMascotas registro = new RegistroMascotas();
        registro.agregar(new Mascota("M-001", "Firulais", "canino", 4, "Ana Gomez"));
        registro.agregar(new Mascota("M-002", "Michi", "felino", 2, "Carlos Ruiz"));
        registro.agregar(new Mascota("M-003", "Rocky", "canino", 9, "Luisa Perez"));
        registro.agregar(new Mascota("M-004", "Canela", "felino", 11, "Marta Diaz"));
        registro.agregar(new Mascota("M-005", "Toby", "canino", 1, "Diego Salas"));
        registro.agregar(new Mascota("M-006", "Nube", "felino", 6, "Sofia Lara"));

        registro.listar();

        Mascota encontrada = registro.buscarPorId("M-003");
        if (encontrada != null) {
            System.out.println("Encontrada: " + encontrada);
        } else {
            System.out.println("No existe ninguna mascota con ID M-003");
        }

        Mascota fantasma = registro.buscarPorId("M-099");
        if (fantasma != null) {
            System.out.println("Encontrada: " + fantasma);
        } else {
            System.out.println("No existe ninguna mascota con ID M-099");
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

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    @Override
    public String toString() {
        return "Mascota " + id + " -> " + nombre + " (" + especie + ", " + edad
                + " anios), dueno: " + dueno;
    }
}

class RegistroMascotas {

    private final List<Mascota> mascotas = new ArrayList<>();

    public void agregar(Mascota m) {
        if (buscarPorId(m.getId()) != null) {
            System.out.println("ID repetido: " + m.getId() + " ya esta registrado");
            return;
        }
        mascotas.add(m);
    }

    public void listar() {
        // TODO: imprima primero el encabezado
        //       "--- Registro de mascotas (6) ---" usando mascotas.size()
        // TODO: recorra con for INDEXADO (int i = 0; i < mascotas.size(); i++)
        //       e imprima cada ficha numerada desde 1: "1. Mascota M-001 -> ..."
    }

    public Mascota buscarPorId(String id) {
        // TODO: recorra con FOR-EACH y devuelva la Mascota cuyo getId() sea igual a id
        // TODO: si ninguna coincide devuelva null (el main ya se encarga de ese caso)
        return null;
    }

    public int cantidad() {
        return mascotas.size();
    }
}
```

**Rubrica esperada (campo Rubrica):**

listar() usa for indexado, imprime el encabezado con size() y numera las seis fichas desde 1. buscarPorId usa for-each, compara con equals, devuelve la mascota correcta para M-003 y null para M-099 sin lanzar NullPointerException. La salida coincide linea por linea.

---

## Pregunta 3 - Codigo ejecutable · 20 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## Eliminar una ficha y depurar el registro sin romperlo

La clinica pide dos operaciones distintas:

1. `eliminarPorId(String id)`: retira **una** ficha usando `mascotas.remove(objeto)`. Si el ID no existe, avisa y no hace nada.
2. `pasarAGeriatria(int edadMinima)`: retira **varias** fichas en un solo recorrido, las de `edad >= edadMinima`. Aqui `for-each` + `remove` lanza `ConcurrentModificationException`: use un `Iterator<Mascota>` y `it.remove()`.

El `main` carga las seis fichas, elimina M-002 Michi y luego pasa a geriatria a las mascotas de **9 anios o mas** (Rocky con 9 y Canela con 11).

**Al ejecutar debe imprimir exactamente:**

```
Retirada del registro: M-002 Michi
Fichas activas: 5
Pasa a geriatria: M-003 Rocky (9 anios)
Pasa a geriatria: M-004 Canela (11 anios)
Fichas activas: 3
```

El programa debe terminar **sin ninguna excepcion**. Si ve `ConcurrentModificationException` en la consola, esta modificando la lista mientras la recorre con for-each.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        RegistroMascotas registro = new RegistroMascotas();
        registro.agregar(new Mascota("M-001", "Firulais", "canino", 4, "Ana Gomez"));
        registro.agregar(new Mascota("M-002", "Michi", "felino", 2, "Carlos Ruiz"));
        registro.agregar(new Mascota("M-003", "Rocky", "canino", 9, "Luisa Perez"));
        registro.agregar(new Mascota("M-004", "Canela", "felino", 11, "Marta Diaz"));
        registro.agregar(new Mascota("M-005", "Toby", "canino", 1, "Diego Salas"));
        registro.agregar(new Mascota("M-006", "Nube", "felino", 6, "Sofia Lara"));

        registro.eliminarPorId("M-002");
        System.out.println("Fichas activas: " + registro.cantidad());

        registro.pasarAGeriatria(9);
        System.out.println("Fichas activas: " + registro.cantidad());
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

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    @Override
    public String toString() {
        return "Mascota " + id + " -> " + nombre + " (" + especie + ", " + edad
                + " anios), dueno: " + dueno;
    }
}

class RegistroMascotas {

    private final List<Mascota> mascotas = new ArrayList<>();

    public void agregar(Mascota m) {
        if (buscarPorId(m.getId()) == null) {
            mascotas.add(m);
        }
    }

    public Mascota buscarPorId(String id) {
        for (Mascota m : mascotas) {
            if (m.getId().equals(id)) {
                return m;
            }
        }
        return null;
    }

    public void eliminarPorId(String id) {
        // TODO: busque la mascota con buscarPorId
        // TODO: si no existe imprima "No se puede eliminar: M-002 no esta registrada"
        // TODO: si existe, quitela con mascotas.remove(objeto) e imprima
        //       "Retirada del registro: M-002 Michi"
    }

    public void pasarAGeriatria(int edadMinima) {
        // TODO: recorra la lista con un Iterator<Mascota>
        // TODO: por cada mascota con getEdad() >= edadMinima imprima
        //       "Pasa a geriatria: M-003 Rocky (9 anios)"
        //       y retirela con it.remove() (NUNCA con mascotas.remove dentro del recorrido)
    }

    public int cantidad() {
        return mascotas.size();
    }
}
```

**Rubrica esperada (campo Rubrica):**

eliminarPorId usa remove(objeto) y trata el caso de ID inexistente con mensaje. pasarAGeriatria recorre con Iterator y elimina con it.remove(), retirando exactamente Rocky y Canela. El conteo baja 6 -> 5 -> 3 y la ejecucion termina sin ConcurrentModificationException. La salida coincide exactamente.

---

## Pregunta 4 - Seleccion unica · 10 pts

**Tipo en la plataforma:** `cerrada`

**Enunciado (campo Contenido):**

## ¿Cual de estos fragmentos revienta en tiempo de ejecucion?

Los cuatro fragmentos compilan sin errores. `mascotas` es un `ArrayList<Mascota>` con las seis fichas del escenario.

**A**
```java
for (Mascota m : mascotas) {
    if (m.getEdad() >= 9) {
        mascotas.remove(m);
    }
}
```

**B**
```java
Iterator<Mascota> it = mascotas.iterator();
while (it.hasNext()) {
    if (it.next().getEdad() >= 9) {
        it.remove();
    }
}
```

**C**
```java
mascotas.removeIf(m -> m.getEdad() >= 9);
```

**D**
```java
for (int i = mascotas.size() - 1; i >= 0; i--) {
    if (mascotas.get(i).getEdad() >= 9) {
        mascotas.remove(i);
    }
}
```

**¿Cual lanza `ConcurrentModificationException` al ejecutarse y por que?**

**Opciones:**

- [x] El fragmento A: el for-each recorre con un iterador interno y la lista se modifica por fuera de ese iterador.
- [ ] El fragmento B: llamar a it.remove() mientras el while sigue activo corrompe el recorrido.
- [ ] El fragmento C: removeIf no puede usarse sobre un ArrayList con objetos propios.
- [ ] El fragmento D: recorrer hacia atras deja indices invalidos y desborda la lista.

**Rubrica esperada (campo Rubrica):**

Respuesta correcta: el fragmento A, porque el for-each usa internamente un iterador y la lista se modifica por fuera de el. Se acierta o no; no hay puntaje parcial.

---

## Pregunta 5 - Proyecto en ZIP · 10 pts

**Tipo en la plataforma:** `codigo_zip`

**Enunciado (campo Contenido):**

## Entrega del proyecto: menu de consola de VetCare

Suba un **ZIP del proyecto NetBeans `VetCare`** (paquete `vetcare`) que contenga, ahora en archivos separados:

- `Mascota.java` con atributos privados, constructor, getters y `toString()`.
- `RegistroMascotas.java` con `agregar`, `listar`, `buscarPorId`, `eliminarPorId`, `pasarAGeriatria` y `cantidad`.
- La clase de arranque con un **menu de consola** hecho con `Scanner` dentro de un `while`, con las opciones:

```
=== VetCare - Registro de mascotas ===
1. Agregar mascota
2. Listar mascotas
3. Buscar por ID
4. Eliminar por ID
5. Salir
Opcion:
```

Requisitos de la entrega:
- El menu debe permitir cargar **las seis fichas del escenario** y volver a mostrar el menu despues de cada operacion, hasta que se elija 5.
- Elegir una opcion que no existe (por ejemplo 9) debe mostrar un aviso y **no** cerrar el programa.
- Incluya dentro del ZIP una **captura de la consola** con el listado final de las seis fichas (`captura_listado.png`).

**Lenguaje:** `java`

**Rubrica esperada (campo Rubrica):**

El ZIP contiene un proyecto NetBeans compilable con Mascota y RegistroMascotas en archivos separados dentro del paquete vetcare. El menu con Scanner y while ofrece las cinco opciones, ejecuta cada una y no se cae con una opcion invalida. Incluye la captura de la consola con el listado de las seis fichas.

---

## Pregunta 6 - Respuesta escrita · 10 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Justificacion: ¿por que abandonamos el arreglo?

En dos parrafos cortos y con datos de su propio codigo:

**(a)** Explique que pasa exactamente cuando la clinica intenta guardar la cuarta mascota en `Mascota[] fichas = new Mascota[3];` (diga el nombre de la excepcion) y que hace `ArrayList` distinto por dentro para que eso no ocurra.

**(b)** El atributo esta declarado `private final List<Mascota> mascotas = new ArrayList<>();`. Responda las tres: ¿por que `private`?, ¿por que `final` si la lista si cambia de contenido?, y ¿por que declararlo como `List` y no como `ArrayList`?

**Rubrica esperada (campo Rubrica):**

(a) Nombra ArrayIndexOutOfBoundsException y explica que ArrayList redimensiona su arreglo interno al crecer. (b) Justifica private como encapsulamiento (nadie modifica la lista sin pasar por los metodos), final como referencia inmutable que no impide cambiar el contenido, y List como programar contra la interfaz para poder cambiar la implementacion.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
