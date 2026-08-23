# Taller de la Clase 3 en ExamLab - configuracion

- **Curso:** Programacion II (FI303204)
- **Taller:** Taller Clase 3 en ExamLab - Sala de espera con Queue e historial con pila
- **Preguntas:** 6 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** VetCare queda con la sala de espera modelada como cola FIFO y el historial de atenciones recientes como pila LIFO, ambas conectadas al registro de mascotas de la clase anterior.
- **Entregable de la clase:** Clases SalaDeEspera (Queue) e HistorialReciente (Deque como pila) integradas al proyecto VetCare, con una demo que atiende en orden de llegada las cuatro mascotas del escenario y deshace la ultima atencion registrada; comprimido y subido a ExamLab.

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante modela la sala de espera de VetCare como cola FIFO y el historial de atenciones como pila LIFO, las conecta (atender apila la consulta) y atiende una urgencia con addFirst.

---

## Pregunta 1 - Codigo ejecutable · 20 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## La ficha del turno, antes de cualquier estructura

Antes de encolar nada hay que tener **que** encolar. Escriba la clase `Turno` con cuatro atributos privados: `id`, `mascota`, `dueno`, `motivo` (todos `String`), su constructor completo, sus cuatro getters y `toString()`.

El `main` ya crea dos turnos sueltos del escenario de la clinica:

| Turno | Mascota | Dueno | Motivo |
|-------|---------|-------|--------|
| T-01 | Firulais | Ana Gomez | vacunacion |
| T-03 | Rocky | Luisa Perez | dolor en pata |

**Al ejecutar debe imprimir exactamente:**

```
Turno T-01 -> Firulais (dueno: Ana Gomez) | motivo: vacunacion
Turno T-03 -> Rocky (dueno: Luisa Perez) | motivo: dolor en pata
```

Verifique este paso antes de seguir: si el `toString()` esta mal, todas las salidas de la cola y de la pila van a salir mal.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
public class Main {

    public static void main(String[] args) {
        Turno t1 = new Turno("T-01", "Firulais", "Ana Gomez", "vacunacion");
        System.out.println(t1);

        Turno t3 = new Turno("T-03", "Rocky", "Luisa Perez", "dolor en pata");
        System.out.println(t3);
    }
}

class Turno {

    // TODO 1: declare los cuatro atributos privados: id, mascota, dueno, motivo (todos String)

    public Turno(String id, String mascota, String dueno, String motivo) {
        // TODO 2: asigne cada parametro a su atributo usando this.
    }

    // TODO 3: escriba los getters getId(), getMascota(), getDueno() y getMotivo()

    // TODO 4: sobreescriba toString() con @Override para devolver exactamente
    //         "Turno T-01 -> Firulais (dueno: Ana Gomez) | motivo: vacunacion"
    //         Mientras no lo haga, la consola imprimira algo como Turno@6d06d69c.
}
```

**Rubrica esperada (campo Rubrica):**

Turno tiene los cuatro atributos privados, constructor que los inicializa todos, los cuatro getters y toString() con @Override. Las dos lineas de salida coinciden caracter por caracter, incluido el separador ' | motivo: '.

---

## Pregunta 2 - Codigo ejecutable · 25 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## `SalaDeEspera`: se atiende en el orden en que llegaron (FIFO)

Complete `SalaDeEspera`, que ya tiene `private final Queue<Turno> cola = new LinkedList<>();`

1. `registrarLlegada(Turno t)`: encola con **`offer`**.
2. `siguienteEnPantalla()`: usa **`peek`** para MIRAR quien sigue **sin sacarlo**.
3. `atender()`: valida `isEmpty()` primero; si hay turno lo saca con **`poll`**. Con la sala vacia imprime un mensaje controlado, **no devuelve `null` suelto ni lanza excepcion**.

El `main` registra los cuatro turnos (T-01 Firulais/vacunacion, T-02 Michi/control de peso, T-03 Rocky/dolor en pata, T-04 Nube/revision de oidos), mira **dos veces** en pantalla y llama a `atender()` **cinco** veces.

**Al ejecutar debe imprimir exactamente:**

```
Llega T-01 Firulais. En sala: 1
Llega T-02 Michi. En sala: 2
Llega T-03 Rocky. En sala: 3
Llega T-04 Nube. En sala: 4
En pantalla: T-01 Firulais (mirar no saca)
En pantalla: T-01 Firulais (mirar no saca)
En sala despues de mirar dos veces: 4
Atendiendo: T-01 Firulais por vacunacion. Quedan: 3
Atendiendo: T-02 Michi por control de peso. Quedan: 2
Atendiendo: T-03 Rocky por dolor en pata. Quedan: 1
Atendiendo: T-04 Nube por revision de oidos. Quedan: 0
La sala esta vacia: no hay turnos por atender
```

Las dos evidencias que buscamos: **peek repetido deja la sala en 4** y **poll atiende en el orden exacto de llegada**.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    public static void main(String[] args) {
        SalaDeEspera sala = new SalaDeEspera();

        sala.registrarLlegada(new Turno("T-01", "Firulais", "Ana Gomez", "vacunacion"));
        sala.registrarLlegada(new Turno("T-02", "Michi", "Carlos Ruiz", "control de peso"));
        sala.registrarLlegada(new Turno("T-03", "Rocky", "Luisa Perez", "dolor en pata"));
        sala.registrarLlegada(new Turno("T-04", "Nube", "Sofia Lara", "revision de oidos"));

        sala.siguienteEnPantalla();
        sala.siguienteEnPantalla();
        System.out.println("En sala despues de mirar dos veces: " + sala.cantidad());

        sala.atender();
        sala.atender();
        sala.atender();
        sala.atender();
        sala.atender();
    }
}

class Turno {

    private final String id;
    private final String mascota;
    private final String dueno;
    private final String motivo;

    public Turno(String id, String mascota, String dueno, String motivo) {
        this.id = id;
        this.mascota = mascota;
        this.dueno = dueno;
        this.motivo = motivo;
    }

    public String getId() {
        return id;
    }

    public String getMascota() {
        return mascota;
    }

    public String getDueno() {
        return dueno;
    }

    public String getMotivo() {
        return motivo;
    }

    @Override
    public String toString() {
        return "Turno " + id + " -> " + mascota + " (dueno: " + dueno + ") | motivo: " + motivo;
    }
}

class SalaDeEspera {

    private final Queue<Turno> cola = new LinkedList<>();

    public void registrarLlegada(Turno t) {
        // TODO: encole con cola.offer(t) e imprima
        //       "Llega T-01 Firulais. En sala: 1"  (use cantidad())
    }

    public void siguienteEnPantalla() {
        // TODO: use cola.peek() para MIRAR sin sacar.
        // TODO: si hay turno imprima "En pantalla: T-01 Firulais (mirar no saca)"
        // TODO: si la cola esta vacia imprima "En pantalla: no hay turnos en espera"
    }

    public void atender() {
        // TODO: valide primero con cola.isEmpty(): si esta vacia imprima
        //       "La sala esta vacia: no hay turnos por atender" y termine (nunca devuelva null suelto)
        // TODO: si hay turno, saquelo con cola.poll() e imprima
        //       "Atendiendo: T-01 Firulais por vacunacion. Quedan: 3"
    }

    public int cantidad() {
        return cola.size();
    }
}
```

**Rubrica esperada (campo Rubrica):**

registrarLlegada usa offer, siguienteEnPantalla usa peek y no altera el size (la linea de control muestra 4), atender usa poll y valida isEmpty antes, imprimiendo mensaje controlado en la quinta llamada sin excepcion ni null. La salida coincide linea por linea y el orden de atencion es T-01, T-02, T-03, T-04.

---

## Pregunta 3 - Codigo ejecutable · 20 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## `HistorialReciente`: deshacer la ultima atencion (LIFO)

La recepcionista registro por error la atencion de Rocky. Deshacer siempre retira **la mas reciente**: eso es una pila.

Complete `HistorialReciente`, que ya tiene `private final Deque<String> pila = new ArrayDeque<>();`

1. `registrar(String nombreMascota)`: apila con **`push`**.
2. `ultimaAtencion()`: mira la cima con **`peek`**, sin sacarla.
3. `deshacer()`: protegido con `isEmpty()`; saca con **`pop`**.

El `main` registra Firulais, Michi y Rocky, y luego llama a `deshacer()` mas veces de las que hay elementos.

**Al ejecutar debe imprimir exactamente:**

```
Registrada atencion de Firulais. En historial: 1
Registrada atencion de Michi. En historial: 2
Registrada atencion de Rocky. En historial: 3
Ultima atencion: Rocky
Deshecha la atencion de Rocky. Quedan: 2
Ultima atencion: Michi
Deshecha la atencion de Michi. Quedan: 1
Deshecha la atencion de Firulais. Quedan: 0
La pila esta vacia: no hay nada que deshacer
```

Fijese en el efecto LIFO: se registro Firulais primero, pero el primero en salir es Rocky.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

    public static void main(String[] args) {
        HistorialReciente historial = new HistorialReciente();

        historial.registrar("Firulais");
        historial.registrar("Michi");
        historial.registrar("Rocky");

        historial.ultimaAtencion();
        historial.deshacer();
        historial.ultimaAtencion();

        historial.deshacer();
        historial.deshacer();
        historial.deshacer();
    }
}

class HistorialReciente {

    private final Deque<String> pila = new ArrayDeque<>();

    public void registrar(String nombreMascota) {
        // TODO: apile con pila.push(nombreMascota) e imprima
        //       "Registrada atencion de Firulais. En historial: 1"
    }

    public void ultimaAtencion() {
        // TODO: use pila.peek() para mirar la cima sin sacarla
        // TODO: si hay algo imprima "Ultima atencion: Rocky"
        // TODO: si esta vacia imprima "Ultima atencion: el historial esta vacio"
    }

    public void deshacer() {
        // TODO: proteja con pila.isEmpty(): si esta vacia imprima
        //       "La pila esta vacia: no hay nada que deshacer" y termine
        // TODO: si hay algo, saquelo con pila.pop() e imprima
        //       "Deshecha la atencion de Rocky. Quedan: 2"
    }

    public int cantidad() {
        return pila.size();
    }
}
```

**Rubrica esperada (campo Rubrica):**

Usa push, peek y pop sobre el Deque como pila. ultimaAtencion no altera el tamano. deshacer esta protegido con isEmpty y con la pila vacia imprime el mensaje controlado en vez de lanzar NoSuchElementException. La salida coincide exactamente y demuestra el orden LIFO.

---

## Pregunta 4 - Codigo ejecutable · 20 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## Integracion: atender apila, y la urgencia se cuela

Ahora las dos estructuras trabajan juntas dentro de VetCare. La cola pasa a declararse `Deque<Turno> cola = new LinkedList<>();` (un `Deque` **tambien** es `Queue`: sigue teniendo `offer`, `peek` y `poll`, y ademas gana `addFirst`).

`HistorialReciente` ya viene completo. Complete en `SalaDeEspera`:

1. `registrarUrgencia(Turno t)`: la urgencia **no hace fila**, entra al frente con `addFirst`.
2. `atender(HistorialReciente historial)`: valida cola vacia; saca con `poll` y **registra automaticamente** esa atencion en el historial (el estudiante no debe llamar a `historial.registrar` desde el `main`: lo hace `atender`).

Flujo del `main`: llegan T-01 Firulais, T-02 Michi, T-03 Rocky y T-04 Nube; se atiende uno; entra la urgencia **T-05 Canela (dificultad respiratoria)**; se atiende dos veces mas; se consulta y se deshace la ultima atencion.

**Al ejecutar debe imprimir exactamente:**

```
Llega T-01 Firulais. En sala: 1
Llega T-02 Michi. En sala: 2
Llega T-03 Rocky. En sala: 3
Llega T-04 Nube. En sala: 4
Atendiendo: T-01 Firulais por vacunacion. Quedan: 3
Registrada atencion de Firulais. En historial: 1
URGENCIA al frente: T-05 Canela. En sala: 4
Atendiendo: T-05 Canela por dificultad respiratoria. Quedan: 3
Registrada atencion de Canela. En historial: 2
Atendiendo: T-02 Michi por control de peso. Quedan: 2
Registrada atencion de Michi. En historial: 3
Ultima atencion: Michi
Deshecha la atencion de Michi. Quedan: 2
Ultima atencion: Canela
```

Canela se atiende **antes** de Michi aunque llego despues: eso es `addFirst`. Y Michi se deshace primero aunque Firulais entro primero: eso es LIFO.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;

public class Main {

    public static void main(String[] args) {
        SalaDeEspera sala = new SalaDeEspera();
        HistorialReciente historial = new HistorialReciente();

        sala.registrarLlegada(new Turno("T-01", "Firulais", "Ana Gomez", "vacunacion"));
        sala.registrarLlegada(new Turno("T-02", "Michi", "Carlos Ruiz", "control de peso"));
        sala.registrarLlegada(new Turno("T-03", "Rocky", "Luisa Perez", "dolor en pata"));
        sala.registrarLlegada(new Turno("T-04", "Nube", "Sofia Lara", "revision de oidos"));

        sala.atender(historial);

        sala.registrarUrgencia(new Turno("T-05", "Canela", "Marta Diaz", "dificultad respiratoria"));

        sala.atender(historial);
        sala.atender(historial);

        historial.ultimaAtencion();
        historial.deshacer();
        historial.ultimaAtencion();
    }
}

class Turno {

    private final String id;
    private final String mascota;
    private final String dueno;
    private final String motivo;

    public Turno(String id, String mascota, String dueno, String motivo) {
        this.id = id;
        this.mascota = mascota;
        this.dueno = dueno;
        this.motivo = motivo;
    }

    public String getId() {
        return id;
    }

    public String getMascota() {
        return mascota;
    }

    public String getDueno() {
        return dueno;
    }

    public String getMotivo() {
        return motivo;
    }

    @Override
    public String toString() {
        return "Turno " + id + " -> " + mascota + " (dueno: " + dueno + ") | motivo: " + motivo;
    }
}

class SalaDeEspera {

    // Deque tambien es Queue: sirve como cola FIFO y ademas permite addFirst.
    private final Deque<Turno> cola = new LinkedList<>();

    public void registrarLlegada(Turno t) {
        cola.offer(t);
        System.out.println("Llega " + t.getId() + " " + t.getMascota() + ". En sala: " + cola.size());
    }

    public void registrarUrgencia(Turno t) {
        // TODO: una urgencia NO hace fila: metala al frente con cola.addFirst(t)
        // TODO: imprima "URGENCIA al frente: T-05 Canela. En sala: 4"
    }

    public void atender(HistorialReciente historial) {
        // TODO: si la cola esta vacia imprima
        //       "La sala esta vacia: no hay turnos por atender" y termine
        // TODO: saque el turno con poll(), imprima
        //       "Atendiendo: T-01 Firulais por vacunacion. Quedan: 3"
        //       y registre automaticamente esa atencion en el historial
    }

    public int cantidad() {
        return cola.size();
    }
}

class HistorialReciente {

    private final Deque<String> pila = new ArrayDeque<>();

    public void registrar(String nombreMascota) {
        pila.push(nombreMascota);
        System.out.println("Registrada atencion de " + nombreMascota + ". En historial: " + pila.size());
    }

    public void ultimaAtencion() {
        if (pila.isEmpty()) {
            System.out.println("Ultima atencion: el historial esta vacio");
        } else {
            System.out.println("Ultima atencion: " + pila.peek());
        }
    }

    public void deshacer() {
        if (pila.isEmpty()) {
            System.out.println("La pila esta vacia: no hay nada que deshacer");
            return;
        }
        String fuera = pila.pop();
        System.out.println("Deshecha la atencion de " + fuera + ". Quedan: " + pila.size());
    }
}
```

**Rubrica esperada (campo Rubrica):**

registrarUrgencia usa addFirst y la urgencia se atiende antes de los turnos que ya esperaban. atender valida cola vacia, saca con poll y registra la atencion en el historial sin que el main lo haga. La salida coincide linea por linea, incluida la evidencia final de LIFO.

---

## Pregunta 5 - Seleccion multiple · 8 pts

**Tipo en la plataforma:** `cerrada_multi`

**Enunciado (campo Contenido):**

## Lo que hay que tener claro de colas y pilas

Marque **todas** las afirmaciones verdaderas sobre el codigo que acaba de escribir.

**Opciones:**

- [x] peek() devuelve el elemento del frente sin retirarlo, por eso llamarlo dos veces deja el size igual.
- [ ] poll() y peek() hacen lo mismo, pero poll() ademas imprime el elemento.
- [x] En una pila (Deque usado con push/pop) el ultimo elemento que entra es el primero que sale.
- [ ] offer() sobre una Queue inserta al frente, igual que addFirst().
- [x] Llamar a poll() o a peek() sobre una coleccion vacia devuelve null, por eso conviene validar con isEmpty() antes.
- [ ] LinkedList no puede usarse como Queue: para eso hay que usar obligatoriamente ArrayDeque.

**Rubrica esperada (campo Rubrica):**

Correctas: las opciones 0, 2 y 4. Se califica por afirmaciones acertadas menos las marcadas por error; marcar todas no da puntaje.

---

## Pregunta 6 - Respuesta escrita · 7 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Justificacion: la estructura correcta para cada necesidad

En un parrafo por punto:

**(a)** ¿Por que la sala de espera de «Huellitas» es una **cola** y no una pila? Diga que le pasaria a Firulais si la sala fuera una pila y siguieran llegando mascotas.

**(b)** ¿Por que el historial de "deshacer" es una **pila** y no una cola? Relacionelo con el Ctrl+Z de cualquier programa que use a diario.

**(c)** La urgencia de Canela rompe el FIFO con `addFirst`. Explique por que eso es una **regla de negocio de la clinica** y no un error de diseno de la estructura.

**Rubrica esperada (campo Rubrica):**

(a) Justifica FIFO con la equidad del orden de llegada y explica que en una pila Firulais quedaria sepultado indefinidamente. (b) Justifica LIFO por la necesidad de revertir la accion mas reciente y lo conecta con Ctrl+Z. (c) Reconoce addFirst como prioridad clinica explicita y no como violacion accidental del orden.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
