# Taller de la Clase 6 en ExamLab - configuracion

- **Curso:** Programacion II (FI303204)
- **Taller:** Taller Clase 6 en ExamLab - Eventos, ActionListener y separacion de capas
- **Preguntas:** 5 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** El formulario de VetCare queda conectado: al oprimir 'Registrar mascota' el objeto entra al ArrayList y el listado en pantalla se actualiza.
- **Entregable de la clase:** Proyecto VetCare con la ventana de registro operativa y la clase ControladorRegistro separada de la vista, comprimido y subido a ExamLab.

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante conecta el formulario de VetCare: el boton Registrar mete la mascota en el repositorio a traves de un controlador, y la vista queda sin una sola regla de negocio adentro.

---

## Pregunta 1 - Codigo ejecutable · 20 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## `RepositorioMascotas`: la capa que no sabe que existe Swing

En VetCare hay tres paquetes: `vetcare.modelo` (Mascota), `vetcare.servicio` (repositorio y controlador) y `vetcare.vista` (las ventanas). La regla es dura: **ninguna clase de modelo o servicio importa `javax.swing`**. Si manana la clinica cambia Swing por una pagina web, esta capa no se toca.

`Mascota` ya viene completa. Complete `RepositorioMascotas`:

1. `registrar(Mascota m)`: si el ID ya existe, **lance** `new IllegalArgumentException("Ya existe una mascota con el ID M-001")`. Si no existe, agreguela. **No imprima nada**: el servicio no habla con el usuario, informa lanzando o devolviendo.
2. `buscarPorId(String id)`: devuelve la mascota o `null`.
3. `listar()`: **devuelve un String** listo para pintar en un `JTextArea`, con el encabezado y una ficha por linea precedida de `- `.

**Al ejecutar debe imprimir exactamente:**

```
Total: 1
Error: Ya existe una mascota con el ID M-001
Total: 2
Buscada: M-002 - Firulais (canino, 4 anios)
Buscada: null
Mascotas registradas (2):
- M-001 - Kira (felino, 3 anios)
- M-002 - Firulais (canino, 4 anios)
```

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        RepositorioMascotas repo = new RepositorioMascotas();

        repo.registrar(new Mascota("M-001", "Kira", "felino", 3));
        System.out.println("Total: " + repo.total());

        try {
            repo.registrar(new Mascota("M-001", "Otra Kira", "felino", 5));
        } catch (IllegalArgumentException ex) {
            System.out.println("Error: " + ex.getMessage());
        }

        repo.registrar(new Mascota("M-002", "Firulais", "canino", 4));
        System.out.println("Total: " + repo.total());

        System.out.println("Buscada: " + repo.buscarPorId("M-002"));
        System.out.println("Buscada: " + repo.buscarPorId("M-404"));
        System.out.println(repo.listar());
    }
}

// Paquete vetcare.modelo: NUNCA importa javax.swing
class Mascota {

    private final String id;
    private final String nombre;
    private final String especie;
    private final int edad;

    public Mascota(String id, String nombre, String especie, int edad) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
    }

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    @Override
    public String toString() {
        return id + " - " + nombre + " (" + especie + ", " + edad + " anios)";
    }
}

// Paquete vetcare.servicio: NUNCA importa javax.swing
class RepositorioMascotas {

    private final List<Mascota> mascotas = new ArrayList<>();

    public void registrar(Mascota m) {
        // TODO: si ya existe una mascota con ese id, lance
        //       new IllegalArgumentException("Ya existe una mascota con el ID M-001")
        // TODO: si no existe, agreguela a la lista (sin imprimir nada: el servicio no habla con el usuario)
    }

    public Mascota buscarPorId(String id) {
        // TODO: devuelva la mascota con ese id o null si no existe
        return null;
    }

    public String listar() {
        // TODO: devuelva un String con una mascota por linea, listo para pintar en un JTextArea.
        //       Empiece con "Mascotas registradas (2):" y luego cada ficha precedida por "- ".
        //       Si la lista esta vacia devuelva "Mascotas registradas (0):"
        return "";
    }

    public int total() {
        return mascotas.size();
    }
}
```

**Rubrica esperada (campo Rubrica):**

registrar lanza IllegalArgumentException con el mensaje exacto ante ID repetido y no imprime por consola. buscarPorId devuelve null para M-404 sin excepcion. listar devuelve el String con encabezado y una ficha por linea. No hay ningun import de javax.swing en el archivo. La salida coincide linea por linea.

---

## Pregunta 2 - Codigo ejecutable · 22 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## `ControladorRegistro`: donde vive la validacion

El formulario entrega **texto**: la edad llega como `String`, y alguien va a escribir `tres`. La conversion y las validaciones van en el controlador, no en la ventana ni en el repositorio.

Complete `registrarMascota(String id, String nombre, String especie, String edadTexto)`:

1. **Obligatorios**: si `id`, `nombre` o `especie` vienen `null` o vacios tras `trim()`, lance `IllegalArgumentException("El campo nombre es obligatorio")` (con el nombre del campo que falla).
2. **Conversion**: `Integer.parseInt` dentro de `try-catch`; en el `catch (NumberFormatException)` lance `IllegalArgumentException("La edad debe ser un numero entero, por ejemplo 4. Recibido: tres")`.
3. **Rango**: edad entre 0 y 30; si no, `IllegalArgumentException("La edad debe estar entre 0 y 30 anios. Recibido: 150")`.
4. Si todo esta bien: cree la `Mascota`, llame a `repositorio.registrar(...)` y **devuelva** el mensaje de exito.

El repositorio **llega por el constructor** (ya esta asi en el starter): no escriba `new RepositorioMascotas()` dentro del metodo.

El `main` prueba cinco entradas: valida, edad `tres`, nombre vacio, ID repetido y edad `150`.

**Al ejecutar debe imprimir exactamente:**

```
OK: registrada M-001 Kira (felino, 3 anios). Total: 1
Error: La edad debe ser un numero entero, por ejemplo 4. Recibido: tres
Error: El campo nombre es obligatorio
Error: Ya existe una mascota con el ID M-001
Error: La edad debe estar entre 0 y 30 anios. Recibido: 150
Total final: 1
```

La ultima linea es la que importa: de cinco intentos solo **uno** entro a la lista.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        RepositorioMascotas repo = new RepositorioMascotas();
        ControladorRegistro controlador = new ControladorRegistro(repo);

        probar(controlador, "M-001", "Kira", "felino", "3");
        probar(controlador, "M-002", "Firulais", "canino", "tres");
        probar(controlador, "M-003", "", "canino", "5");
        probar(controlador, "M-001", "Kira repetida", "felino", "3");
        probar(controlador, "M-004", "Rocky", "canino", "150");

        System.out.println("Total final: " + repo.total());
    }

    private static void probar(ControladorRegistro c, String id, String nombre, String especie, String edad) {
        try {
            System.out.println("OK: " + c.registrarMascota(id, nombre, especie, edad));
        } catch (IllegalArgumentException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}

// Paquete vetcare.modelo: NUNCA importa javax.swing
class Mascota {

    private final String id;
    private final String nombre;
    private final String especie;
    private final int edad;

    public Mascota(String id, String nombre, String especie, int edad) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
    }

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    @Override
    public String toString() {
        return id + " - " + nombre + " (" + especie + ", " + edad + " anios)";
    }
}

class RepositorioMascotas {

    private final List<Mascota> mascotas = new ArrayList<>();

    public void registrar(Mascota m) {
        for (Mascota existente : mascotas) {
            if (existente.getId().equals(m.getId())) {
                throw new IllegalArgumentException("Ya existe una mascota con el ID " + m.getId());
            }
        }
        mascotas.add(m);
    }

    public int total() {
        return mascotas.size();
    }
}

class ControladorRegistro {

    private final RepositorioMascotas repositorio;

    public ControladorRegistro(RepositorioMascotas repositorio) {
        // TODO: el repositorio LLEGA por constructor, nunca se crea con new aqui adentro
        this.repositorio = repositorio;
    }

    public String registrarMascota(String id, String nombre, String especie, String edadTexto) {
        // TODO 1: valide obligatorios (null o vacio tras trim) para id, nombre y especie;
        //         lance IllegalArgumentException("El campo nombre es obligatorio")
        // TODO 2: convierta la edad con Integer.parseInt dentro de try-catch;
        //         en el catch (NumberFormatException) lance
        //         IllegalArgumentException("La edad debe ser un numero entero, por ejemplo 4. Recibido: tres")
        // TODO 3: valide el rango 0 a 30; si no cumple lance
        //         IllegalArgumentException("La edad debe estar entre 0 y 30 anios. Recibido: 150")
        // TODO 4: cree la Mascota, llamela repositorio.registrar(...) y devuelva el mensaje
        //         "registrada M-001 Kira (felino, 3 anios). Total: 1"
        return "";
    }
}
```

**Rubrica esperada (campo Rubrica):**

Valida obligatorios, convierte con parseInt dentro de try-catch traduciendo NumberFormatException a IllegalArgumentException con mensaje en español, y valida el rango 0 a 30. El repositorio se usa desde el atributo inyectado por constructor, sin new dentro del metodo. Total final igual a 1 y salida identica a la pedida.

---

## Pregunta 3 - Interfaz grafica Java · 30 pts

**Tipo en la plataforma:** `java_gui`

**Enunciado (campo Contenido):**

## `VentanaRegistroMascota`: el boton que si funciona

El starter ya trae la ventana completa (formulario con ID, nombre, especie y edad, boton **Registrar mascota** y `JTextArea` de solo lectura para el listado), mas `Mascota`, `RepositorioMascotas` y `ControladorRegistro` funcionando. El controlador ya esta declarado como **atributo** de la ventana.

Falta lo unico que importa hoy: **conectar el evento**.

1. Conecte el boton con `addActionListener`. El cuerpo del listener llama a `registrar()` y nada mas.
2. Escriba `registrar()` con **maximo cinco lineas utiles**, en este orden:
   - llamar a `controlador.registrarMascota(...)` con los cuatro `getText()`,
   - refrescar `areaListado` con `setText(controlador...)` o el listado del repositorio,
   - limpiar los campos con `limpiarCampos()`,
   - mostrar el exito en un `JOptionPane`,
   - `catch (IllegalArgumentException ex)` mostrando `ex.getMessage()` en un `JOptionPane` de error.

Prohibido dentro del listener: `Integer.parseInt`, `if` de validacion, `new RepositorioMascotas()`.

**Como se verifica al ejecutar la ventana (los tres casos de la clase):**

- **(a) Registro valido** — ID `M-001`, nombre `Kira`, especie `felino`, edad `3`: el area muestra
  `Mascotas registradas (1):` y debajo `- M-001 - Kira (felino, 3 anios)`; aparece el JOptionPane de exito y los campos quedan vacios.
- **(b) Edad como texto** — edad `tres`: cuadro de error con `La edad debe ser un numero entero, por ejemplo 4. Recibido: tres`, la aplicacion **sigue abierta** y el area **no** cambia.
- **(c) ID repetido** — registrar otra vez `M-001`: cuadro de error con `Ya existe una mascota con el ID M-001` y el listado sigue en 1.

Ninguno de los tres casos debe dejar una traza roja en la consola.

**Tipo de GUI:** `swing`

**Codigo de partida (starter):**

```java
import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.util.ArrayList;
import java.util.List;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

public class Main {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new VentanaRegistroMascota().setVisible(true);
            }
        });
    }
}

class Mascota {

    private final String id;
    private final String nombre;
    private final String especie;
    private final int edad;

    public Mascota(String id, String nombre, String especie, int edad) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
    }

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    @Override
    public String toString() {
        return id + " - " + nombre + " (" + especie + ", " + edad + " anios)";
    }
}

class RepositorioMascotas {

    private final List<Mascota> mascotas = new ArrayList<>();

    public void registrar(Mascota m) {
        for (Mascota existente : mascotas) {
            if (existente.getId().equals(m.getId())) {
                throw new IllegalArgumentException("Ya existe una mascota con el ID " + m.getId());
            }
        }
        mascotas.add(m);
    }

    public String listar() {
        StringBuilder sb = new StringBuilder("Mascotas registradas (" + mascotas.size() + "):");
        for (Mascota m : mascotas) {
            sb.append("\n- ").append(m);
        }
        return sb.toString();
    }

    public int total() {
        return mascotas.size();
    }
}

class ControladorRegistro {

    private final RepositorioMascotas repositorio;

    public ControladorRegistro(RepositorioMascotas repositorio) {
        this.repositorio = repositorio;
    }

    public String registrarMascota(String id, String nombre, String especie, String edadTexto) {
        exigir(id, "id");
        exigir(nombre, "nombre");
        exigir(especie, "especie");
        int edad;
        try {
            edad = Integer.parseInt(edadTexto.trim());
        } catch (NumberFormatException ex) {
            throw new IllegalArgumentException(
                    "La edad debe ser un numero entero, por ejemplo 4. Recibido: " + edadTexto);
        }
        if (edad < 0 || edad > 30) {
            throw new IllegalArgumentException("La edad debe estar entre 0 y 30 anios. Recibido: " + edad);
        }
        repositorio.registrar(new Mascota(id.trim(), nombre.trim(), especie.trim(), edad));
        return "registrada " + id.trim() + " " + nombre.trim() + ". Total: " + repositorio.total();
    }

    private void exigir(String valor, String campo) {
        if (valor == null || valor.trim().isEmpty()) {
            throw new IllegalArgumentException("El campo " + campo + " es obligatorio");
        }
    }
}

class VentanaRegistroMascota extends JFrame {

    // El controlador es ATRIBUTO de la ventana, nunca se crea dentro del listener.
    private final ControladorRegistro controlador = new ControladorRegistro(new RepositorioMascotas());

    private final JTextField campoId = new JTextField();
    private final JTextField campoNombre = new JTextField();
    private final JTextField campoEspecie = new JTextField();
    private final JTextField campoEdad = new JTextField();
    private final JButton botonRegistrar = new JButton("Registrar mascota");
    private final JTextArea areaListado = new JTextArea(8, 40);

    public VentanaRegistroMascota() {
        setTitle("VetCare - Registro de mascotas");
        setSize(640, 420);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel formulario = new JPanel(new GridLayout(4, 2, 6, 6));
        formulario.add(new JLabel("ID:"));
        formulario.add(campoId);
        formulario.add(new JLabel("Nombre:"));
        formulario.add(campoNombre);
        formulario.add(new JLabel("Especie:"));
        formulario.add(campoEspecie);
        formulario.add(new JLabel("Edad:"));
        formulario.add(campoEdad);

        areaListado.setEditable(false);

        setLayout(new BorderLayout(8, 8));
        add(formulario, BorderLayout.NORTH);
        add(new JScrollPane(areaListado), BorderLayout.CENTER);
        add(botonRegistrar, BorderLayout.SOUTH);

        // TODO: conecte el boton con addActionListener. El cuerpo del listener tiene
        //       MAXIMO CINCO LINEAS y solo debe: llamar a registrar(), nada mas.
    }

    private void registrar() {
        // TODO (maximo cinco lineas utiles):
        //   1) llamar al controlador con los cuatro getText()
        //   2) refrescar areaListado con setText
        //   3) limpiar los cuatro campos
        //   4) mostrar JOptionPane con el mensaje de exito
        //   5) capturar IllegalArgumentException y mostrar ex.getMessage() en un JOptionPane de error
        //      (la mascota NO debe quedar registrada en ese caso)
    }

    private void limpiarCampos() {
        campoId.setText("");
        campoNombre.setText("");
        campoEspecie.setText("");
        campoEdad.setText("");
    }
}
```

**Rubrica esperada (campo Rubrica):**

El listener solo delega en registrar(): sin parseInt, sin if de validacion, sin crear el repositorio. registrar() tiene maximo cinco lineas utiles (llamar, refrescar, limpiar, avisar, capturar). Los tres casos se comportan como se describe: el valido aparece en el area y aumenta el total, los dos invalidos muestran JOptionPane con el mensaje del controlador y no alteran el listado ni cierran la aplicacion.

---

## Pregunta 4 - Seleccion unica · 8 pts

**Tipo en la plataforma:** `cerrada`

**Enunciado (campo Contenido):**

## ¿Cual listener respeta la separacion de capas?

**A**
```java
botonRegistrar.addActionListener(e -> {
    int edad = Integer.parseInt(campoEdad.getText());
    if (campoNombre.getText().isEmpty()) {
        JOptionPane.showMessageDialog(this, "Falta el nombre");
        return;
    }
    mascotas.add(new Mascota(campoId.getText(), campoNombre.getText(), campoEspecie.getText(), edad));
    areaListado.append(campoNombre.getText());
});
```

**B**
```java
botonRegistrar.addActionListener(e -> registrar());

private void registrar() {
    try {
        String msg = controlador.registrarMascota(campoId.getText(), campoNombre.getText(),
                campoEspecie.getText(), campoEdad.getText());
        areaListado.setText(controlador.listado());
        limpiarCampos();
        JOptionPane.showMessageDialog(this, msg);
    } catch (IllegalArgumentException ex) {
        JOptionPane.showMessageDialog(this, ex.getMessage(), "Dato invalido", JOptionPane.ERROR_MESSAGE);
    }
}
```

**C**
```java
botonRegistrar.addActionListener(e -> {
    ControladorRegistro c = new ControladorRegistro(new RepositorioMascotas());
    c.registrarMascota(campoId.getText(), campoNombre.getText(),
            campoEspecie.getText(), campoEdad.getText());
});
```

**¿Cual es la version correcta y por que las otras dos fallan?**

**Opciones:**

- [ ] La A, porque valida antes de agregar y evita datos malos en la lista.
- [x] La B, porque el listener solo delega: la validacion y la conversion viven en el controlador y la ventana solo lee, refresca y avisa.
- [ ] La C, porque crear el controlador dentro del listener garantiza datos frescos en cada clic.
- [ ] Las tres son equivalentes: el resultado visible para el usuario es el mismo.

**Rubrica esperada (campo Rubrica):**

Respuesta correcta: la B. A mete conversion, validacion y la coleccion dentro de la vista; C crea un repositorio nuevo en cada clic, asi que los datos se pierden. Se acierta o no.

---

## Pregunta 5 - Respuesta escrita · 20 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Evidencia de los tres casos y justificacion de la arquitectura

**(a) Evidencia (obligatoria).** Describa, caso por caso, lo que observo al ejecutar su ventana en NetBeans. Para cada uno: que escribio en cada campo, el **texto exacto** del cuadro de dialogo que aparecio, que quedo en el `JTextArea` y cual era el total despues.
1. Registro valido de **M-001 Kira, felino, 3**.
2. Edad escrita como **tres**.
3. **ID repetido M-001**.

**(b) Prueba del Ctrl+F.** Diga que busco y que encontro al buscar `javax.swing` en los paquetes `vetcare.modelo` y `vetcare.servicio`. Si aparecio algun resultado, explique como lo elimino.

**(c) Justificacion.** Explique con sus palabras por que el `ActionListener` no debe contener `Integer.parseInt` ni la lista de mascotas. Responda concretamente: ¿como probaria la regla *"no se aceptan dos mascotas con el mismo ID"* sin abrir la ventana, y por que eso seria imposible si la regla viviera dentro del listener?

**Rubrica esperada (campo Rubrica):**

(a) Reporta los tres casos con el texto exacto de los dialogos y el estado del listado y del total en cada uno, coherente con el codigo entregado. (b) Reporta el resultado del Ctrl+F sobre javax.swing en modelo y servicio. (c) Argumenta la testabilidad: el controlador se puede probar desde un main o una prueba unitaria, mientras la logica dentro del listener solo se puede ejercitar a mano con clics.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
