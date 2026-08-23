# Taller de la Clase 4 en ExamLab - configuracion

- **Curso:** Programacion II (FI303204)
- **Taller:** Taller Clase 4 en ExamLab - HashMap, HashSet y la primera ventana Swing
- **Preguntas:** 5 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** VetCare encuentra cualquier expediente por ID en tiempo constante con HashMap y estrena su primera ventana Swing para consultarlo.
- **Entregable de la clase:** Clase RegistroExpedientes con HashMap y HashSet mas la ventana VentanaBuscarExpediente construida a mano (sin arrastrar componentes) que busca por ID y muestra el resultado o un mensaje de error controlado; comprimido y subido a ExamLab.

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante indexa los expedientes de VetCare en un HashMap con control de ID duplicado, cuenta razas distintas con HashSet y estrena la ventana Swing que consulta ese registro con un ActionListener limpio.

---

## Pregunta 1 - Codigo ejecutable · 22 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## Del recorrido a la clave: `HashMap<String, Expediente>`

Buscar la ficha H-5000 recorriendo un `ArrayList` de 5.000 expedientes obliga a mirar hasta 5.000 elementos. Un `HashMap` va directo a la clave.

La clase `Expediente` (id, nombre, raza, dueno, notaClinica) ya viene completa. Complete `RegistroExpedientes`, que ya tiene `private final Map<String, Expediente> expedientes = new HashMap<>();`

1. `guardar(Expediente e)`: **antes** de poner nada, verifique con `containsKey`. Si el ID ya existe, avise y **no sobrescriba** (recuerde: `put` con una clave repetida reemplaza en silencio y el expediente anterior se pierde para siempre). Si no existe, guarde con `put(e.getId(), e)`.
2. `buscar(String id)`: use **`get(id)`** (una sola operacion, sin recorrer nada) y trate el caso `null`.

Expedientes del escenario, ya cargados en el `main`:

| ID | Nombre | Raza | Dueno | Nota clinica |
|----|--------|------|-------|--------------|
| M-001 | Firulais | Labrador | Ana Gomez | Refuerzo antirrabico pendiente |
| M-002 | Michi | Criollo | Carlos Ruiz | Control de peso mensual |
| M-003 | Rocky | Pastor Aleman | Luisa Perez | Displasia de cadera en seguimiento |
| M-004 | Canela | Siames | Marta Diaz | Dieta renal desde marzo |
| M-005 | Toby | Labrador | Diego Salas | Primera consulta, sin antecedentes |

**Al ejecutar debe imprimir exactamente:**

```
Expedientes guardados: 5
ID repetido: M-001 ya tiene expediente y no se sobrescribe
Expedientes guardados: 5
Encontrado: Expediente M-003 -> Rocky (Pastor Aleman), dueno: Luisa Perez | nota: Displasia de cadera en seguimiento
No existe expediente con ID H-5000
```

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        RegistroExpedientes registro = new RegistroExpedientes();

        registro.guardar(new Expediente("M-001", "Firulais", "Labrador", "Ana Gomez", "Refuerzo antirrabico pendiente"));
        registro.guardar(new Expediente("M-002", "Michi", "Criollo", "Carlos Ruiz", "Control de peso mensual"));
        registro.guardar(new Expediente("M-003", "Rocky", "Pastor Aleman", "Luisa Perez", "Displasia de cadera en seguimiento"));
        registro.guardar(new Expediente("M-004", "Canela", "Siames", "Marta Diaz", "Dieta renal desde marzo"));
        registro.guardar(new Expediente("M-005", "Toby", "Labrador", "Diego Salas", "Primera consulta, sin antecedentes"));

        System.out.println("Expedientes guardados: " + registro.cantidad());

        registro.guardar(new Expediente("M-001", "Firulais", "Labrador", "Ana Gomez", "OTRA nota que borraria la anterior"));
        System.out.println("Expedientes guardados: " + registro.cantidad());

        registro.buscar("M-003");
        registro.buscar("H-5000");
    }
}

class Expediente {

    private final String id;
    private final String nombre;
    private final String raza;
    private final String dueno;
    private final String notaClinica;

    public Expediente(String id, String nombre, String raza, String dueno, String notaClinica) {
        this.id = id;
        this.nombre = nombre;
        this.raza = raza;
        this.dueno = dueno;
        this.notaClinica = notaClinica;
    }

    public String getId() {
        return id;
    }

    public String getRaza() {
        return raza;
    }

    @Override
    public String toString() {
        return "Expediente " + id + " -> " + nombre + " (" + raza + "), dueno: " + dueno
                + " | nota: " + notaClinica;
    }
}

class RegistroExpedientes {

    private final Map<String, Expediente> expedientes = new HashMap<>();

    public void guardar(Expediente e) {
        // TODO: use expedientes.containsKey(...) para detectar el ID repetido ANTES de poner nada.
        // TODO: si ya existe imprima
        //       "ID repetido: M-001 ya tiene expediente y no se sobrescribe" y termine.
        // TODO: si no existe, guardelo con put(e.getId(), e)
    }

    public void buscar(String id) {
        // TODO: obtenga el expediente con expedientes.get(id) (una sola operacion, sin recorrer nada)
        // TODO: si es null imprima "No existe expediente con ID H-5000"
        // TODO: si existe imprima "Encontrado: " + expediente
    }

    public int cantidad() {
        return expedientes.size();
    }
}
```

**Rubrica esperada (campo Rubrica):**

guardar usa containsKey antes de put y el segundo intento con M-001 no cambia el tamano ni reemplaza la nota. buscar usa get(id) y no un recorrido, y trata el null del ID inexistente sin excepcion. La salida coincide caracter por caracter con las cinco lineas pedidas.

---

## Pregunta 2 - Codigo ejecutable · 18 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## `HashSet` de razas: el boolean que casi nadie usa

La clinica quiere saber **cuantas razas distintas** atiende. Un `Set` no admite duplicados y su metodo `add` devuelve un `boolean`: `true` si el elemento **no estaba**, `false` si ya estaba. Ese boolean es la respuesta gratis.

`guardar` ya esta implementado y llama a `registrarRaza(...)` en cada alta. Complete `registrarRaza(String raza)`:
- Guarde en una variable el boolean que devuelve `razas.add(raza)`.
- Si es `true`, imprima que la raza es nueva; si es `false`, imprima que ya estaba.

Ojo con los datos: **Firulais (M-001) y Toby (M-005) son ambos Labrador**.

**Al ejecutar debe imprimir exactamente:**

```
Raza nueva registrada: Labrador
Raza nueva registrada: Criollo
Raza nueva registrada: Pastor Aleman
Raza nueva registrada: Siames
Raza repetida (ya estaba en el conjunto): Labrador
Expedientes guardados: 5
Razas distintas atendidas: 4
```

Cinco expedientes, **cuatro** razas: el `HashSet` conto Labrador una sola vez sin que usted escribiera un solo `if` de comparacion.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        RegistroExpedientes registro = new RegistroExpedientes();

        registro.guardar(new Expediente("M-001", "Firulais", "Labrador", "Ana Gomez", "Refuerzo antirrabico pendiente"));
        registro.guardar(new Expediente("M-002", "Michi", "Criollo", "Carlos Ruiz", "Control de peso mensual"));
        registro.guardar(new Expediente("M-003", "Rocky", "Pastor Aleman", "Luisa Perez", "Displasia de cadera en seguimiento"));
        registro.guardar(new Expediente("M-004", "Canela", "Siames", "Marta Diaz", "Dieta renal desde marzo"));
        registro.guardar(new Expediente("M-005", "Toby", "Labrador", "Diego Salas", "Primera consulta, sin antecedentes"));

        System.out.println("Expedientes guardados: " + registro.cantidad());
        System.out.println("Razas distintas atendidas: " + registro.cantidadRazas());
    }
}

class Expediente {

    private final String id;
    private final String nombre;
    private final String raza;
    private final String dueno;
    private final String notaClinica;

    public Expediente(String id, String nombre, String raza, String dueno, String notaClinica) {
        this.id = id;
        this.nombre = nombre;
        this.raza = raza;
        this.dueno = dueno;
        this.notaClinica = notaClinica;
    }

    public String getId() {
        return id;
    }

    public String getRaza() {
        return raza;
    }

    @Override
    public String toString() {
        return "Expediente " + id + " -> " + nombre + " (" + raza + "), dueno: " + dueno
                + " | nota: " + notaClinica;
    }
}

class RegistroExpedientes {

    private final Map<String, Expediente> expedientes = new HashMap<>();
    private final Set<String> razas = new HashSet<>();

    public void guardar(Expediente e) {
        if (expedientes.containsKey(e.getId())) {
            System.out.println("ID repetido: " + e.getId() + " ya tiene expediente y no se sobrescribe");
            return;
        }
        expedientes.put(e.getId(), e);
        registrarRaza(e.getRaza());
    }

    private void registrarRaza(String raza) {
        // TODO: add() de un Set devuelve un boolean: true si la raza NO estaba, false si ya estaba.
        // TODO: guarde ese boolean en una variable y segun su valor imprima
        //       "Raza nueva registrada: Labrador"
        //       o "Raza repetida (ya estaba en el conjunto): Labrador"
    }

    public int cantidad() {
        return expedientes.size();
    }

    public int cantidadRazas() {
        return razas.size();
    }
}
```

**Rubrica esperada (campo Rubrica):**

registrarRaza captura el boolean devuelto por add y decide el mensaje con el, sin usar contains ni recorrer el conjunto. Labrador se reporta como repetida en el quinto expediente y cantidadRazas() devuelve 4. La salida coincide exactamente.

---

## Pregunta 3 - Interfaz grafica Java · 30 pts

**Tipo en la plataforma:** `java_gui`

**Enunciado (campo Contenido):**

## La primera ventana de VetCare, escrita a mano

Aqui **no se arrastran componentes**: la ventana se escribe linea por linea para entender que es cada objeto. El starter ya trae el `JFrame` con su titulo, tamano, `JPanel` superior (`JLabel` + `JTextField` + `JButton`) y el `JLabel` central de resultado, ademas del `RegistroExpedientes` cargado con los cinco expedientes de la clinica.

Complete tres cosas:

1. En el constructor: `setDefaultCloseOperation(...)` para que **al cerrar la ventana termine el programa**.
2. En el constructor: conecte el boton con `addActionListener` usando una **lambda de una sola linea** que unicamente llame a `buscar()`. Ninguna regla de negocio va dentro del listener.
3. El metodo `buscar()`:
   - Lee el texto del campo y lo **normaliza** con `trim()` y `toUpperCase()` (asi `" m-003 "` tambien funciona).
   - Si quedo vacio: `JOptionPane` de advertencia con `Escriba un ID de expediente, por ejemplo M-001` y no consulta nada.
   - Dentro de un `try`: consulta `registro.buscar(id)`.
     - Si devuelve `null`: `JOptionPane.showMessageDialog` de tipo `WARNING_MESSAGE` con el texto `No existe expediente con ID M-404`.
     - Si existe: pone el expediente en el `JLabel` central con `setText`.
   - `catch (Exception ex)`: `JOptionPane` de error mostrando `ex.getMessage()`. **Ningun catch vacio.**

**Como se verifica al ejecutar la ventana:**
- Abre **centrada**, con titulo `VetCare - Buscar expediente`.
- Escribir `m-003` (en minusculas y con espacios) y oprimir **Buscar** deja en el centro de la ventana: `M-003 - Rocky (Pastor Aleman), dueno: Luisa Perez | nota: Displasia de cadera en seguimiento`
- Escribir `M-404` abre un cuadro de advertencia con `No existe expediente con ID M-404` y el resultado anterior no se borra por una excepcion.
- Dejar el campo vacio y oprimir Buscar muestra el aviso, sin consultar el mapa.

**Tipo de GUI:** `swing`

**Codigo de partida (starter):**

```java
import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.util.HashMap;
import java.util.Map;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;

public class Main {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new VentanaBuscarExpediente().setVisible(true);
            }
        });
    }
}

class Expediente {

    private final String id;
    private final String nombre;
    private final String raza;
    private final String dueno;
    private final String notaClinica;

    public Expediente(String id, String nombre, String raza, String dueno, String notaClinica) {
        this.id = id;
        this.nombre = nombre;
        this.raza = raza;
        this.dueno = dueno;
        this.notaClinica = notaClinica;
    }

    public String getId() {
        return id;
    }

    @Override
    public String toString() {
        return id + " - " + nombre + " (" + raza + "), dueno: " + dueno + " | nota: " + notaClinica;
    }
}

class RegistroExpedientes {

    private final Map<String, Expediente> expedientes = new HashMap<>();

    public static RegistroExpedientes conDatosDeLaClinica() {
        RegistroExpedientes r = new RegistroExpedientes();
        r.guardar(new Expediente("M-001", "Firulais", "Labrador", "Ana Gomez", "Refuerzo antirrabico pendiente"));
        r.guardar(new Expediente("M-002", "Michi", "Criollo", "Carlos Ruiz", "Control de peso mensual"));
        r.guardar(new Expediente("M-003", "Rocky", "Pastor Aleman", "Luisa Perez", "Displasia de cadera en seguimiento"));
        r.guardar(new Expediente("M-004", "Canela", "Siames", "Marta Diaz", "Dieta renal desde marzo"));
        r.guardar(new Expediente("M-005", "Toby", "Labrador", "Diego Salas", "Primera consulta, sin antecedentes"));
        return r;
    }

    public void guardar(Expediente e) {
        expedientes.put(e.getId(), e);
    }

    public Expediente buscar(String id) {
        return expedientes.get(id);
    }
}

class VentanaBuscarExpediente extends JFrame {

    private final RegistroExpedientes registro = RegistroExpedientes.conDatosDeLaClinica();
    private final JTextField campoId = new JTextField(12);
    private final JButton botonBuscar = new JButton("Buscar");
    private final JLabel etiquetaResultado =
            new JLabel("Escriba un ID (M-001 a M-005) y oprima Buscar", SwingConstants.CENTER);

    public VentanaBuscarExpediente() {
        setTitle("VetCare - Buscar expediente");
        setSize(620, 200);
        setLocationRelativeTo(null);
        // TODO: configure setDefaultCloseOperation para que al cerrar la ventana termine el programa

        JPanel panelSuperior = new JPanel(new FlowLayout());
        panelSuperior.add(new JLabel("ID del expediente:"));
        panelSuperior.add(campoId);
        panelSuperior.add(botonBuscar);

        setLayout(new BorderLayout());
        add(panelSuperior, BorderLayout.NORTH);
        add(etiquetaResultado, BorderLayout.CENTER);

        // TODO: conecte el boton con addActionListener usando una lambda de UNA linea
        //       que solo llame al metodo buscar()
    }

    private void buscar() {
        // TODO: 1) lea el texto del campo y normalicelo con trim() y toUpperCase()
        // TODO: 2) si quedo vacio, muestre un JOptionPane de advertencia y termine
        // TODO: 3) dentro de un try, consulte registro.buscar(id)
        //          - si es null: JOptionPane.showMessageDialog con
        //            "No existe expediente con ID M-404", tipo WARNING_MESSAGE
        //          - si existe: ponga el texto del expediente en etiquetaResultado con setText
        // TODO: 4) capture Exception y muestre el mensaje real en un JOptionPane de error
    }
}
```

**Rubrica esperada (campo Rubrica):**

La ventana abre centrada, con titulo y con setDefaultCloseOperation(EXIT_ON_CLOSE). El listener es una lambda que solo delega en buscar(): no contiene validaciones, estructuras de datos ni logica. buscar() normaliza con trim y toUpperCase, distingue campo vacio, resultado encontrado y no encontrado con JOptionPane, y usa try-catch sin catch vacio.

---

## Pregunta 4 - Seleccion unica · 10 pts

**Tipo en la plataforma:** `cerrada`

**Enunciado (campo Contenido):**

## La demo de los 5.000 expedientes

En clase se busco la ficha H-5000 dentro de un archivo historico de 5.000 expedientes, primero recorriendo un `ArrayList` con un `for` y luego con `get()` sobre un `HashMap`, midiendo nanosegundos. El `HashMap` gano por varios ordenes de magnitud.

**¿Cual es la razon tecnica correcta?**

**Opciones:**

- [ ] El HashMap guarda los datos ordenados por ID, asi que puede aplicar busqueda binaria sobre ellos.
- [x] El HashMap calcula con el hashCode de la clave en que posicion esta el valor y va directo a ella, mientras el ArrayList compara elemento por elemento hasta encontrarlo.
- [ ] El HashMap mantiene todo en memoria RAM y el ArrayList consulta el disco en cada iteracion.
- [ ] El ArrayList es lento porque usa objetos y el HashMap trabaja internamente con tipos primitivos.

**Rubrica esperada (campo Rubrica):**

Respuesta correcta: el HashMap calcula la posicion a partir del hashCode de la clave y va directo al lugar (coste practicamente constante), mientras la lista compara elemento por elemento (coste proporcional al tamano). Se acierta o no.

---

## Pregunta 5 - Respuesta escrita · 20 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Justificacion: estructura de datos y limpieza de la vista

Responda las tres partes con referencias a **su propio codigo** de este taller.

**(a) Mapa contra lista.** ¿Que gano VetCare al pasar de `List<Expediente>` a `Map<String, Expediente>` y que perdio? Mencione al menos una cosa que la lista hacia bien y el mapa ya no (piense en el orden de las fichas y en las fichas sin ID).

**(b) El `put` silencioso.** Explique con el caso M-001 del taller que habria pasado en la clinica si `guardar` no hubiera usado `containsKey`: ¿que dato concreto de Firulais se habria perdido y quien se habria dado cuenta?

**(c) El listener flaco.** El criterio de la clase dice: *"el evento del boton solo lee la entrada y llama al registro"*. Copie su lambda del boton (deberia ser de una linea) y explique que problema aparece cuando la clinica pida manana una **segunda** forma de buscar (por ejemplo desde un menu) si la logica hubiera quedado escrita dentro del `ActionListener`.

**Rubrica esperada (campo Rubrica):**

(a) Identifica la ganancia (acceso por clave en tiempo practicamente constante, unicidad del ID) y una perdida real (el HashMap no conserva orden de insercion, exige una clave). (b) Explica con M-001 que put habria reemplazado la nota clinica en silencio y que nadie recibiria aviso. (c) Muestra su lambda de una linea y argumenta la duplicacion de logica y la imposibilidad de reutilizarla o probarla si vive dentro del listener.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
