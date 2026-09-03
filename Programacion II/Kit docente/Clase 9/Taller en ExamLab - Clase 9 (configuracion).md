# Taller de la Clase 9 en ExamLab - configuracion

- **Curso:** Programacion II (FI303204)
- **Taller:** Taller Clase 9 en ExamLab - Persistencia en CSV y refactorizacion asistida por IA
- **Preguntas:** 4 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** VetCare guarda la lista de mascotas en mascotas.csv al cerrar y la vuelve a cargar al abrir.
- **Entregable de la clase:** La clase RepositorioMascotasCSV con guardar() y cargar() funcionando, el archivo mascotas.csv generado por la propia aplicación y la bitácora REFACTOR.md, subidos a ExamLab.

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante hace que VetCare escriba mascotas.csv al cerrar y lo vuelva a cargar al abrir, tolerando archivo inexistente y lineas dañadas, y documenta en REFACTOR.md que le acepto y que le rechazo a la IA.

---

## Pregunta 1 - Codigo ejecutable · 30 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## `guardar()`: la clinica escribe su propio archivo

VetCare debe dejar en disco un `mascotas.csv` con **una linea de encabezado y una linea por mascota**, todas con el mismo numero de separadores.

Complete `guardar(List<Mascota>)` en `RepositorioMascotasCSV` (las constantes `SEPARADOR = ";"`, `ENCABEZADO = "id;nombre;especie;edad;cedula_dueno"` y el `Path ruta` ya estan):

1. Abra el escritor con **try-with-resources**: `try (BufferedWriter w = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8)) { ... }`. Asi el archivo se cierra siempre, incluso si algo falla en la mitad.
2. Escriba la linea de **encabezado** y luego una linea por mascota, con los cinco campos en el mismo orden del encabezado.
3. `catch (IOException ex)`: informe con `"No se pudo guardar mascotas.csv: " + ex.getMessage()`. **Prohibido el catch vacio.**
4. Complete `limpiar(String campo)`: si un nombre trae un `;` (por ejemplo `Firulais; el bravo`) la linea quedaria con seis campos y la carga la descartaria. Reemplace `;` por `,` y aplique `trim()`. Use `limpiar` en cada campo de texto que escriba.

El `main` carga las seis mascotas del escenario, llama a `guardar` y despues **vuelve a leer el archivo** para mostrar lo que quedo escrito.

**Al ejecutar debe imprimir exactamente:**

```
Archivo escrito: mascotas.csv (7 lineas)
id;nombre;especie;edad;cedula_dueno
M-001;Firulais;canino;4;1094512
M-002;Michi;felino;2;1128733
M-003;Rocky;canino;9;1002945
M-004;Canela;felino;11;1156420
M-005;Toby;canino;1;1187301
M-006;Nube;felino;6;1143988
```

Seis mascotas, **siete** lineas: encabezado mas una por ficha, sin lineas en blanco al final.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        List<Mascota> mascotas = new ArrayList<>();
        mascotas.add(new Mascota("M-001", "Firulais", "canino", 4, "1094512"));
        mascotas.add(new Mascota("M-002", "Michi", "felino", 2, "1128733"));
        mascotas.add(new Mascota("M-003", "Rocky", "canino", 9, "1002945"));
        mascotas.add(new Mascota("M-004", "Canela", "felino", 11, "1156420"));
        mascotas.add(new Mascota("M-005", "Toby", "canino", 1, "1187301"));
        mascotas.add(new Mascota("M-006", "Nube", "felino", 6, "1143988"));

        RepositorioMascotasCSV repo = new RepositorioMascotasCSV();
        repo.guardar(mascotas);

        // Verificacion: volvemos a leer el archivo que acabo de escribir el programa.
        try {
            List<String> lineas = Files.readAllLines(repo.getRuta(), StandardCharsets.UTF_8);
            System.out.println("Archivo escrito: mascotas.csv (" + lineas.size() + " lineas)");
            for (String l : lineas) {
                System.out.println(l);
            }
        } catch (IOException ex) {
            System.out.println("No se pudo releer el archivo: " + ex.getMessage());
        }
    }
}

class Mascota {

    private final String id;
    private final String nombre;
    private final String especie;
    private final int edad;
    private final String cedulaDueno;

    public Mascota(String id, String nombre, String especie, int edad, String cedulaDueno) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
        this.cedulaDueno = cedulaDueno;
    }

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public String getEspecie() {
        return especie;
    }

    public int getEdad() {
        return edad;
    }

    public String getCedulaDueno() {
        return cedulaDueno;
    }
}

class RepositorioMascotasCSV {

    private static final String SEPARADOR = ";";
    private static final String ENCABEZADO = "id;nombre;especie;edad;cedula_dueno";

    private final Path ruta = Paths.get("mascotas.csv");

    public Path getRuta() {
        return ruta;
    }

    public void guardar(List<Mascota> mascotas) {
        // TODO 1: abra el escritor con try-with-resources:
        //         try (BufferedWriter w = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8)) { ... }
        // TODO 2: escriba primero la linea ENCABEZADO y luego un newLine()
        // TODO 3: recorra la lista y escriba una linea por mascota, uniendo los cinco campos
        //         con SEPARADOR, en el mismo orden del encabezado
        // TODO 4: capture IOException e informe con un mensaje entendible:
        //         "No se pudo guardar mascotas.csv: " + ex.getMessage()
        //         (prohibido dejar el catch vacio)
    }

    /** Quita el separador de un campo de texto para no romper el formato del CSV. */
    private String limpiar(String campo) {
        // TODO 5: si el campo trae un punto y coma (por ejemplo un nombre "Firulais; el bravo")
        //         la linea quedaria con seis campos y cargar() la descartaria.
        //         Devuelva el campo con los ';' reemplazados por ',' y con trim().
        return campo;
    }
}
```

**Rubrica esperada (campo Rubrica):**

guardar usa try-with-resources con Files.newBufferedWriter, escribe el encabezado y una linea por mascota con los cinco campos en orden, sin lineas en blanco intermedias. El catch de IOException informa (no esta vacio). limpiar() neutraliza el separador dentro de los campos de texto y se aplica realmente. La salida coincide caracter por caracter, incluida la cuenta de 7 lineas.

---

## Pregunta 2 - Codigo ejecutable · 30 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## `cargar()`: un archivo dañado no puede tumbar la clinica

Manana alguien va a abrir `mascotas.csv` en el Bloc de notas y lo va a dañar. La carga tiene que **sobrevivir**: descarta lo que no sirve, avisa cual linea fue y conserva todo lo bueno.

El `main` ya siembra un archivo **deteriorado a proposito** (fijese en el metodo `sembrarArchivoDeteriorado`, no lo modifique):

```
linea 1: id;nombre;especie;edad;cedula_dueno     <- encabezado
linea 2: M-001;Firulais;canino;4;1094512         <- valida
linea 3: M-002;Michi;felino;2;1128733            <- valida
linea 4: M-003;Rocky;canino                      <- INCOMPLETA (3 campos)
linea 5: M-004;Canela;felino;11;1156420          <- valida
linea 6: M-005;Toby;canino;cuatro;1187301        <- edad NO numerica
linea 7: M-006;Nube;felino;6;1143988             <- valida
```

Complete `cargar()`:

1. Si el archivo **no existe**: avise y devuelva lista vacia. **No lance excepcion**: la primera ejecucion de la clinica es exactamente ese caso.
2. Lea con **try-with-resources**.
3. **Descarte el encabezado** y lleve un contador con el **numero real de linea** (empezando en 1) para poder decir cual fallo.
4. Linea con distinto numero de campos que `CAMPOS_ESPERADOS`: avise con el numero de linea y siga con la siguiente.
5. Edad no numerica: atrape `NumberFormatException`, avise con el numero de linea y el valor recibido, y siga.
6. `catch (IOException ex)`: informe el problema real. **Ningun catch vacio.**

**Al ejecutar debe imprimir exactamente:**

```
Aviso: la linea 4 no tiene 5 campos y se omite
Aviso: la linea 6 tiene una edad no numerica ('cuatro') y se omite
Mascotas cargadas: 4
- M-001 Firulais (4 anios)
- M-002 Michi (2 anios)
- M-004 Canela (11 anios)
- M-006 Nube (6 anios)
Aviso: no_existe.csv no existe todavia, se arranca con la lista vacia
Archivo inexistente: se arranca con 0 mascotas
```

Siete lineas en el archivo, dos dañadas, **cuatro mascotas cargadas** y la aplicacion viva.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        RepositorioMascotasCSV repo = new RepositorioMascotasCSV(Paths.get("mascotas.csv"));

        // El archivo de prueba se siembra DAÑADO a proposito (linea 4 incompleta, linea 6 con edad de texto).
        sembrarArchivoDeteriorado(repo.getRuta());

        List<Mascota> cargadas = repo.cargar();
        System.out.println("Mascotas cargadas: " + cargadas.size());
        for (Mascota m : cargadas) {
            System.out.println("- " + m.getId() + " " + m.getNombre() + " (" + m.getEdad() + " anios)");
        }

        RepositorioMascotasCSV inexistente = new RepositorioMascotasCSV(Paths.get("no_existe.csv"));
        System.out.println("Archivo inexistente: se arranca con " + inexistente.cargar().size() + " mascotas");
    }

    private static void sembrarArchivoDeteriorado(Path ruta) {
        try (BufferedWriter w = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8)) {
            w.write("id;nombre;especie;edad;cedula_dueno");
            w.newLine();
            w.write("M-001;Firulais;canino;4;1094512");
            w.newLine();
            w.write("M-002;Michi;felino;2;1128733");
            w.newLine();
            w.write("M-003;Rocky;canino");
            w.newLine();
            w.write("M-004;Canela;felino;11;1156420");
            w.newLine();
            w.write("M-005;Toby;canino;cuatro;1187301");
            w.newLine();
            w.write("M-006;Nube;felino;6;1143988");
            w.newLine();
        } catch (IOException ex) {
            System.out.println("No se pudo sembrar el archivo de prueba: " + ex.getMessage());
        }
    }
}

class Mascota {

    private final String id;
    private final String nombre;
    private final String especie;
    private final int edad;
    private final String cedulaDueno;

    public Mascota(String id, String nombre, String especie, int edad, String cedulaDueno) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
        this.cedulaDueno = cedulaDueno;
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
}

class RepositorioMascotasCSV {

    private static final String SEPARADOR = ";";
    private static final int CAMPOS_ESPERADOS = 5;

    private final Path ruta;

    public RepositorioMascotasCSV(Path ruta) {
        this.ruta = ruta;
    }

    public Path getRuta() {
        return ruta;
    }

    public List<Mascota> cargar() {
        List<Mascota> mascotas = new ArrayList<>();
        // TODO 1: si el archivo NO existe (Files.exists), imprima
        //         "Aviso: no_existe.csv no existe todavia, se arranca con la lista vacia"
        //         y devuelva la lista vacia (NO lance excepcion).
        // TODO 2: lea las lineas con try-with-resources
        //         (por ejemplo List<String> lineas = Files.readAllLines(ruta, StandardCharsets.UTF_8);
        //          o un BufferedReader dentro del try con recursos)
        // TODO 3: descarte la linea 1 (encabezado) y lleve un contador con el numero real de linea.
        // TODO 4: si una linea no tiene CAMPOS_ESPERADOS campos, imprima
        //         "Aviso: la linea 4 no tiene 5 campos y se omite" y siga con la siguiente.
        // TODO 5: si la edad no es numerica, atrape NumberFormatException e imprima
        //         "Aviso: la linea 6 tiene una edad no numerica ('cuatro') y se omite"
        // TODO 6: capture IOException informando el problema real (nunca un catch vacio)
        return mascotas;
    }
}
```

**Rubrica esperada (campo Rubrica):**

cargar devuelve lista vacia con aviso cuando el archivo no existe, sin lanzar excepcion. Usa try-with-resources, descarta el encabezado y reporta el numero real de linea de cada descarte. Omite unicamente la linea incompleta y la de edad no numerica, conservando las cuatro validas. El catch de IOException informa. La salida coincide linea por linea.

---

## Pregunta 3 - Proyecto en ZIP · 15 pts

**Tipo en la plataforma:** `codigo_zip`

**Enunciado (campo Contenido):**

## Entrega: el ciclo de vida conectado

Suba el **ZIP del proyecto `VetCare`** con la persistencia integrada al ciclo de vida de la aplicacion:

1. Paquete `vetcare.datos` con `RepositorioMascotasCSV` (los metodos `guardar` y `cargar` que acaba de escribir, ya en archivos separados).
2. **Al arrancar**: `cargar()` se llama **antes** de mostrar la ventana o el menu, y lo cargado es lo que se muestra.
3. **Al cerrar**: `guardar()` se llama al salir (por ejemplo en la opcion Salir del menu, o con un `WindowListener`/`addShutdownHook` si es ventana).
4. Dentro del ZIP incluya:
   - El archivo **`mascotas.csv` generado por la propia aplicacion** (no escrito a mano).
   - `captura_antes.png` y `captura_despues.png`: el conteo de mascotas **antes de cerrar** y **al volver a abrir**, que deben coincidir.
   - `REFACTOR.md` (el de la pregunta siguiente).

**Prueba que debe pasar la entrega:** registrar una mascota nueva, cerrar la aplicacion, volver a abrirla y ver esa mascota en la lista **sin tocar codigo**.

**Lenguaje:** `java`

**Rubrica esperada (campo Rubrica):**

El ZIP trae un proyecto compilable con RepositorioMascotasCSV en el paquete vetcare.datos, cargar() invocado antes de mostrar la interfaz y guardar() al cerrar. Incluye el mascotas.csv generado por la aplicacion y las dos capturas con el mismo conteo antes de cerrar y al reabrir.

---

## Pregunta 4 - Respuesta escrita · 25 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## `REFACTOR.md`: la bitacora de lo que le acepto y le rechazo a la IA

Pidale a una herramienta de IA que revise **su** metodo `guardar()` (pegue su codigo real y pida que señale problemas). Luego escriba aqui la bitacora, con este formato por entrada:

```
Sugerencia: <lo que propuso la IA, en una linea>
Decision: la acepte / la rechace
Por que: <su razon, en sus palabras>
Efecto: <que cambio en el codigo, o que habria pasado si la aplicaba>
```

Requisitos minimos:
- **Al menos dos sugerencias aceptadas** y aplicadas, que usted pueda explicar en voz alta. Para cada una, pegue el antes y el despues del fragmento (2 a 5 lineas).
- **Al menos una sugerencia rechazada** y justificada por escrito. Rechazar bien vale igual que aceptar bien: diga por que no aplica a VetCare (por ejemplo, complejidad innecesaria, dependencia externa que el curso no usa, o algo que rompe el formato del CSV).
- **Prueba de no regresion**: describa el flujo que volvio a correr despues del refactor (guardar, cerrar, reabrir, contar) y confirme que el comportamiento es **identico** al de antes: mismo numero de lineas en el archivo y mismo conteo al reabrir.
- **Una linea final de honestidad**: ¿hubo alguna sugerencia que aplico y **no** entiende del todo? Si la hubo, digala; si la revirtio, digalo tambien.

**Rubrica esperada (campo Rubrica):**

La bitacora tiene al menos dos sugerencias aceptadas con antes/despues del codigo y al menos una rechazada con justificacion tecnica pertinente a VetCare. Cada entrada usa el formato sugerencia / decision / por que / efecto. Reporta la prueba de no regresion con datos concretos (numero de lineas y conteo al reabrir) y responde la linea de honestidad.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
