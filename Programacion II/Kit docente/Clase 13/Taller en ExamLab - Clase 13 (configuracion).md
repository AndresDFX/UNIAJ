# Taller de la Clase 13 en ExamLab - configuracion

- **Curso:** Programacion II (FI303204)
- **Taller:** Taller Clase 13 en ExamLab - Control de excepciones con try-catch-finally
- **Preguntas:** 5 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** El registro de mascotas de VetCare valida edad, peso e ID y avisa con un mensaje claro en lugar de cerrarse.
- **Entregable de la clase:** Clase DatoInvalidoException mas los setters validados de Mascota y la carga del CSV con try-with-resources, con evidencia de cinco pruebas de entrada (cuatro malas y una valida), subido a ExamLab.

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante crea DatoInvalidoException, valida edad y peso con mensajes en lenguaje de la clinica, atrapa el error en el formulario sin perder la aplicacion y carga el CSV con try-with-resources y catch diferenciados.

---

## Pregunta 1 - Codigo ejecutable · 25 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## `DatoInvalidoException` y los setters que validan de verdad

`NumberFormatException: For input string: "tres"` no le dice nada a la recepcionista de «Huellitas». VetCare necesita hablar el idioma de la clinica.

Complete:

1. **`DatoInvalidoException extends Exception`** (checked, a proposito: quien la llame **esta obligado** a decidir que hacer) con un constructor que reciba el mensaje y lo pase con `super(mensaje)`.
2. **`setEdad(String texto) throws DatoInvalidoException`** con las tres validaciones en este orden: vacio, formato (con `Integer.parseInt` dentro de un `try` y **relanzando** `DatoInvalidoException` desde el `catch (NumberFormatException)`), y rango 0 a 30. Solo asigne el atributo si todo paso.
3. **`setPeso(String texto) throws DatoInvalidoException`** con la misma idea usando `Double.parseDouble` y rango 0.1 a 120.0 kilos.

El `main` prueba las **cinco entradas de edad** de la clase (`""`, `"tres"`, `"-2"`, `"150"`, `"4"`) y tres de peso.

**Al ejecutar debe imprimir exactamente:**

```
Rechazada: Falta la edad de Firulais: escribala en anios, por ejemplo 4
Rechazada: La edad de Firulais debe ser un numero en anios: 'tres' no sirve
Rechazada: La edad de Firulais debe estar entre 0 y 30 anios: -2 esta fuera de rango
Rechazada: La edad de Firulais debe estar entre 0 y 30 anios: 150 esta fuera de rango
Edad aceptada: 4
Rechazada: El peso de Firulais debe ser un numero en kilos: 'cero coma cinco' no sirve
Rechazada: El peso de Firulais debe estar entre 0.1 y 120.0 kilos: 0.05 esta fuera de rango
Peso aceptado: 12.5
```

De cinco intentos de edad **solo el ultimo** asigno el valor, y el programa nunca se cayo ni mostro un stack trace.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
public class Main {

    public static void main(String[] args) {
        Mascota firulais = new Mascota("M-001", "Firulais", "canino");

        String[] entradasEdad = {"", "tres", "-2", "150", "4"};
        for (String entrada : entradasEdad) {
            try {
                firulais.setEdad(entrada);
                System.out.println("Edad aceptada: " + firulais.getEdad());
            } catch (DatoInvalidoException ex) {
                System.out.println("Rechazada: " + ex.getMessage());
            }
        }

        String[] entradasPeso = {"cero coma cinco", "0.05", "12.5"};
        for (String entrada : entradasPeso) {
            try {
                firulais.setPeso(entrada);
                System.out.println("Peso aceptado: " + firulais.getPeso());
            } catch (DatoInvalidoException ex) {
                System.out.println("Rechazada: " + ex.getMessage());
            }
        }
    }
}

// Paquete vetcare.excepciones
class DatoInvalidoException extends Exception {

    // TODO 1: constructor que reciba el mensaje y lo pase a la superclase con super(mensaje)
}

class Mascota {

    private final String id;
    private final String nombre;
    private final String especie;
    private int edad = -1;
    private double peso = -1;

    public Mascota(String id, String nombre, String especie) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
    }

    public int getEdad() {
        return edad;
    }

    public double getPeso() {
        return peso;
    }

    public void setEdad(String texto) throws DatoInvalidoException {
        // TODO 2: si texto es null o queda vacio tras trim(), lance DatoInvalidoException con
        //   "Falta la edad de Firulais: escribala en anios, por ejemplo 4"
        // TODO 3: convierta con Integer.parseInt dentro de un try; en el
        //   catch (NumberFormatException ex) RELANCE DatoInvalidoException con
        //   "La edad de Firulais debe ser un numero en anios: 'tres' no sirve"
        // TODO 4: valide el rango 0 a 30; si no cumple lance DatoInvalidoException con
        //   "La edad de Firulais debe estar entre 0 y 30 anios: -2 esta fuera de rango"
        // TODO 5: solo si todo esta bien, asigne this.edad
    }

    public void setPeso(String texto) throws DatoInvalidoException {
        // TODO 6: misma idea con Double.parseDouble y rango 0.1 a 120 kg. Mensajes:
        //   "El peso de Firulais debe ser un numero en kilos: 'cero coma cinco' no sirve"
        //   "El peso de Firulais debe estar entre 0.1 y 120.0 kilos: 0.05 esta fuera de rango"
    }
}
```

**Rubrica esperada (campo Rubrica):**

DatoInvalidoException extiende Exception (checked) y su constructor pasa el mensaje con super. setEdad valida vacio, formato relanzando desde el catch de NumberFormatException, y rango, asignando solo cuando todo pasa. setPeso hace lo equivalente con Double.parseDouble. Todos los mensajes estan en lenguaje de la clinica y la salida coincide caracter por caracter.

---

## Pregunta 2 - Interfaz grafica Java · 25 pts

**Tipo en la plataforma:** `java_gui`

**Enunciado (campo Contenido):**

## El formulario que avisa en vez de reventar

La ventana ya esta armada (campos ID, nombre y edad, boton **Registrar mascota**, area de listado) y `Mascota.setEdad(String)` ya viene con las validaciones de la pregunta anterior lanzando `DatoInvalidoException`. Falta lo que separa una aplicacion usable de un stack trace: **atrapar el error en la frontera**.

Complete el metodo `registrar()`:

1. Cree la `Mascota` con el ID y el nombre del formulario.
2. Envuelva `setEdad(campoEdad.getText())` en un `try-catch (DatoInvalidoException ex)`.
3. En el `catch`: `JOptionPane.showMessageDialog` con **`ex.getMessage()`**, titulo `Dato invalido`, tipo `WARNING_MESSAGE`; devuelva el foco al campo culpable con `campoEdad.requestFocus()`; y **termine con `return`**: la mascota **no** se agrega a la lista.
4. Si no hubo error: agregue la mascota a `registradas`, llame a `refrescarListado()`, limpie los campos con `limpiarCampos()` y avise el exito con un `JOptionPane`.

**Como se verifica al ejecutar la ventana** (las cinco entradas de edad de la clase, con ID `M-001` y nombre `Firulais`):

| Edad escrita | Lo que debe pasar |
|--------------|-------------------|
| (vacio) | Cuadro: `Falta la edad de Firulais: escribala en anios, por ejemplo 4` · listado sigue en 0 · cursor vuelve al campo edad |
| `tres` | Cuadro: `La edad de Firulais debe ser un numero en anios: 'tres' no sirve` · listado sigue en 0 |
| `-2` | Cuadro: `La edad de Firulais debe estar entre 0 y 30 anios: -2 esta fuera de rango` · listado sigue en 0 |
| `150` | Cuadro: `La edad de Firulais debe estar entre 0 y 30 anios: 150 esta fuera de rango` · listado sigue en 0 |
| `4` | Aviso de exito · el area muestra `Mascotas registradas (1):` y `- M-001 - Firulais (4 anios)` · campos limpios |

En los cinco casos la aplicacion **sigue abierta** y en la consola **no** aparece ninguna traza roja.

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
                new VentanaRegistro().setVisible(true);
            }
        });
    }
}

class DatoInvalidoException extends Exception {

    public DatoInvalidoException(String mensaje) {
        super(mensaje);
    }
}

class Mascota {

    private final String id;
    private final String nombre;
    private int edad = -1;

    public Mascota(String id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }

    public void setEdad(String texto) throws DatoInvalidoException {
        if (texto == null || texto.trim().isEmpty()) {
            throw new DatoInvalidoException("Falta la edad de " + nombre
                    + ": escribala en anios, por ejemplo 4");
        }
        int valor;
        try {
            valor = Integer.parseInt(texto.trim());
        } catch (NumberFormatException ex) {
            throw new DatoInvalidoException("La edad de " + nombre
                    + " debe ser un numero en anios: '" + texto + "' no sirve");
        }
        if (valor < 0 || valor > 30) {
            throw new DatoInvalidoException("La edad de " + nombre
                    + " debe estar entre 0 y 30 anios: " + valor + " esta fuera de rango");
        }
        this.edad = valor;
    }

    @Override
    public String toString() {
        return id + " - " + nombre + " (" + edad + " anios)";
    }
}

class VentanaRegistro extends JFrame {

    private final List<Mascota> registradas = new ArrayList<>();

    private final JTextField campoId = new JTextField();
    private final JTextField campoNombre = new JTextField();
    private final JTextField campoEdad = new JTextField();
    private final JButton botonRegistrar = new JButton("Registrar mascota");
    private final JTextArea areaListado = new JTextArea(8, 40);

    public VentanaRegistro() {
        setTitle("VetCare - Registro con validacion");
        setSize(620, 400);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel formulario = new JPanel(new GridLayout(3, 2, 6, 6));
        formulario.add(new JLabel("ID:"));
        formulario.add(campoId);
        formulario.add(new JLabel("Nombre:"));
        formulario.add(campoNombre);
        formulario.add(new JLabel("Edad (anios):"));
        formulario.add(campoEdad);

        areaListado.setEditable(false);

        setLayout(new BorderLayout(8, 8));
        add(formulario, BorderLayout.NORTH);
        add(new JScrollPane(areaListado), BorderLayout.CENTER);
        add(botonRegistrar, BorderLayout.SOUTH);

        botonRegistrar.addActionListener(e -> registrar());
    }

    private void registrar() {
        // TODO 1: cree la Mascota con el ID y el nombre del formulario
        // TODO 2: envuelva la llamada a setEdad(campoEdad.getText()) en un try-catch
        //         de DatoInvalidoException
        // TODO 3: en el catch: JOptionPane.showMessageDialog con ex.getMessage(),
        //         titulo "Dato invalido", tipo WARNING_MESSAGE;
        //         devuelva el foco al campo culpable con campoEdad.requestFocus()
        //         y termine el metodo con return: la mascota NO se agrega a la lista
        // TODO 4: si no hubo error: agregue la mascota a registradas, refresque el area
        //         con refrescarListado(), limpie los campos y avise el exito con JOptionPane
    }

    private void refrescarListado() {
        StringBuilder sb = new StringBuilder("Mascotas registradas (" + registradas.size() + "):");
        for (Mascota m : registradas) {
            sb.append("\n- ").append(m);
        }
        areaListado.setText(sb.toString());
    }

    private void limpiarCampos() {
        campoId.setText("");
        campoNombre.setText("");
        campoEdad.setText("");
    }
}
```

**Rubrica esperada (campo Rubrica):**

registrar() atrapa DatoInvalidoException y muestra ex.getMessage() en un JOptionPane de advertencia, devuelve el foco al campo edad y sale con return sin agregar la mascota. Solo la entrada valida agrega, refresca el listado y limpia los campos. Con las cinco entradas la ventana nunca se cierra ni imprime stack trace, y el listado queda en 1.

---

## Pregunta 3 - Codigo ejecutable · 25 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## Carga del CSV: `try-with-resources` y dos `catch` distintos

"No se pudo leer el archivo" no es lo mismo que "es la primera vez que abres el programa". Son dos situaciones **distintas** y merecen dos `catch` distintos.

El `main` siembra `datos_mascotas.csv` con dos lineas malas a proposito:

```
linea 1: id;nombre;especie;edad          <- encabezado
linea 2: M-001;Firulais;canino;4         <- valida
linea 3: M-002;Michi;felino;2            <- valida
linea 4: M-003;Rocky;canino;nueve        <- edad no numerica
linea 5: M-004;Canela                    <- solo 2 campos
linea 6: M-005;Toby;canino;1             <- valida
```

Complete `CargadorMascotas.cargar(Path ruta)`:

1. Abra el lector con **try-with-resources**: `try (BufferedReader br = Files.newBufferedReader(ruta, StandardCharsets.UTF_8))`.
2. Descarte el encabezado y lleve el **numero real de linea**.
3. Linea con numero de campos distinto de `CAMPOS_ESPERADOS`: avise y **continue**.
4. Edad no numerica: atrape `NumberFormatException`, avise con el valor recibido y **continue**.
5. **Dos catch separados** al final: uno para archivo inexistente (`FileNotFoundException | java.nio.file.NoSuchFileException`) que informa que es la primera ejecucion, y uno para `IOException` que muestra el problema real. **Ningun catch vacio**, y las lineas buenas ya cargadas **no** se descartan.

**Al ejecutar debe imprimir exactamente:**

```
--- Caso 1: archivo existente con dos lineas malas ---
Aviso: linea 4 con edad no numerica ('nueve'), se omite y se continua
Aviso: linea 5 con 2 campos en vez de 4, se omite y se continua
Mascotas cargadas: 3
- M-001 Firulais (canino, 4 anios)
- M-002 Michi (felino, 2 anios)
- M-005 Toby (canino, 1 anios)
--- Caso 2: primera ejecucion, el archivo no existe ---
Primera ejecucion: no se encontro datos/no_existe.csv, VetCare arranca con la lista vacia
Mascotas cargadas: 0
```

Cinco lineas de datos, dos malas, **tres mascotas cargadas**: el archivo dañado no tumbo la clinica.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Path buena = Paths.get("datos_mascotas.csv");
        sembrar(buena);

        CargadorMascotas cargador = new CargadorMascotas();

        System.out.println("--- Caso 1: archivo existente con dos lineas malas ---");
        List<String> cargadas = cargador.cargar(buena);
        System.out.println("Mascotas cargadas: " + cargadas.size());
        for (String m : cargadas) {
            System.out.println("- " + m);
        }

        System.out.println("--- Caso 2: primera ejecucion, el archivo no existe ---");
        List<String> vacias = cargador.cargar(Paths.get("datos/no_existe.csv"));
        System.out.println("Mascotas cargadas: " + vacias.size());
    }

    private static void sembrar(Path ruta) {
        try (BufferedWriter w = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8)) {
            w.write("id;nombre;especie;edad");
            w.newLine();
            w.write("M-001;Firulais;canino;4");
            w.newLine();
            w.write("M-002;Michi;felino;2");
            w.newLine();
            w.write("M-003;Rocky;canino;nueve");
            w.newLine();
            w.write("M-004;Canela");
            w.newLine();
            w.write("M-005;Toby;canino;1");
            w.newLine();
        } catch (IOException ex) {
            System.out.println("No se pudo sembrar el archivo de prueba: " + ex.getMessage());
        }
    }
}

class CargadorMascotas {

    private static final int CAMPOS_ESPERADOS = 4;

    public List<String> cargar(Path ruta) {
        List<String> mascotas = new ArrayList<>();

        // TODO 1: abra el lector con try-with-resources:
        //         try (BufferedReader br = Files.newBufferedReader(ruta, StandardCharsets.UTF_8)) { ... }
        //         Asi el archivo se cierra siempre, con o sin error.
        // TODO 2: descarte el encabezado y lleve el numero real de linea (empezando en 1)
        // TODO 3: linea con distinto numero de campos -> imprima
        //         "Aviso: linea 5 con 2 campos en vez de 4, se omite y se continua"
        // TODO 4: edad no numerica -> atrape NumberFormatException e imprima
        //         "Aviso: linea 4 con edad no numerica ('nueve'), se omite y se continua"
        // TODO 5: DOS catch SEPARADOS al final:
        //         catch (FileNotFoundException | java.nio.file.NoSuchFileException ex) ->
        //           "Primera ejecucion: no se encontro datos/no_existe.csv, VetCare arranca con la lista vacia"
        //         catch (IOException ex) ->
        //           "No se pudo leer el archivo: " + ex.getMessage()
        //         (ningun catch vacio y las lineas buenas ya cargadas NO se descartan)

        return mascotas;
    }
}
```

**Rubrica esperada (campo Rubrica):**

cargar usa try-with-resources con Files.newBufferedReader, descarta el encabezado y reporta el numero real de linea en cada descarte. Tiene dos catch separados: uno para archivo inexistente con el mensaje de primera ejecucion y uno para IOException con el problema real, ninguno vacio. Conserva las tres lineas buenas y la salida coincide linea por linea.

---

## Pregunta 4 - Seleccion multiple · 10 pts

**Tipo en la plataforma:** `cerrada_multi`

**Enunciado (campo Contenido):**

## Excepciones: lo que hay que tener claro

Marque **todas** las afirmaciones verdaderas.

**Opciones:**

- [x] DatoInvalidoException extiende Exception, asi que es checked: el compilador obliga a quien la llame a capturarla o a declararla con throws.
- [ ] Un catch vacio es aceptable cuando el programador sabe que el error no importa; asi el codigo queda mas limpio.
- [x] try-with-resources cierra el recurso automaticamente, con o sin excepcion, y hace innecesario el finally solo para cerrar el archivo.
- [ ] Mostrar ex.printStackTrace() en un JOptionPane es la mejor forma de informar al usuario de la clinica.
- [x] Capturar FileNotFoundException aparte de IOException permite dar un mensaje distinto para la primera ejecucion, cuando el archivo todavia no existe.
- [ ] El bloque finally solo se ejecuta cuando NO hubo excepcion.

**Rubrica esperada (campo Rubrica):**

Correctas: opciones 0, 2 y 4. Se califica por afirmaciones acertadas menos las marcadas por error.

---

## Pregunta 5 - Respuesta escrita · 15 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Tabla de evidencia de las cinco pruebas y justificacion

**(a) Tabla de evidencia (obligatoria).** Ejecute su formulario de NetBeans con las cinco entradas de edad y llene esta tabla, copiando el mensaje **textual** que mostro la aplicacion:

| Entrada | Mensaje mostrado (textual) | ¿Se agrego la mascota? | Estado de la aplicacion |
|---------|---------------------------|------------------------|--------------------------|
| (vacio) | | | |
| `tres` | | | |
| `-2` | | | |
| `150` | | | |
| `4` | | | |

En la ultima columna escriba si la aplicacion siguio abierta y si aparecio alguna traza roja en la consola de NetBeans. Adjunte en su entrega las cinco capturas.

**(b) Checked contra unchecked.** `DatoInvalidoException` extiende `Exception` (checked) y no `RuntimeException`. Explique que le obliga a hacer eso a quien llama al setter y por que en VetCare **conviene** esa obligacion.

**(c) Cero catch vacios.** Reporte el resultado de buscar `catch` en todo su proyecto: cuantos hay y que hace cada uno (informa al usuario, registra, o asume un valor por defecto **documentado con un comentario**). Si encontro alguno vacio, muestre como quedo despues de arreglarlo.

**Rubrica esperada (campo Rubrica):**

(a) La tabla trae las cinco entradas con el mensaje textual que produjo la aplicacion, indica que solo la ultima agrego la mascota y confirma que la aplicacion nunca se cerro ni mostro stack trace. (b) Explica la obligacion del compilador con checked y la justifica como decision consciente para datos de entrada. (c) Inventaria todos los catch del proyecto y demuestra que ninguno quedo vacio.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
