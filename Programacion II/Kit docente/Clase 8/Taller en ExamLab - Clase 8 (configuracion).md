# Taller de la Clase 8 en ExamLab - configuracion

- **Curso:** Programacion II (FI303204)
- **Taller:** Taller Clase 8 en ExamLab - Javadoc y pruebas de la regla de la agenda
- **Preguntas:** 5 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://examlab.lovable.app/) · modulo Talleres
- **Hito del PI:** Las clases del dominio de VetCare quedan documentadas con Javadoc y la regla 'mascota inactiva no agenda' queda respaldada por pruebas que se ejecutan solas.
- **Entregable de la clase:** Mascota, Cita y AgendaService con Javadoc completo, la carpeta HTML generada y una clase de pruebas con cuatro casos, subidos a ExamLab.

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante documenta con Javadoc Mascota, Cita y AgendaService dejando escrita la regla 'una mascota inactiva no agenda', y la respalda con cuatro pruebas independientes que se ejecutan solas.

---

## Pregunta 1 - Codigo ejecutable · 25 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## Javadoc en el dominio: `Mascota` y `Cita`

Documentar no es adornar: el Javadoc es lo que vera dentro de seis meses quien abra el proyecto (usted mismo, probablemente) y lo que aparece en el autocompletado de NetBeans.

El codigo funciona y no debe cambiarlo. Escriba **el Javadoc que falta** en cada lugar marcado con `TODO`:

1. **Bloque de clase** en `Mascota` y en `Cita`: resumen de una linea de que representa en la clinica «Huellitas» + `@author` con su nombre completo.
2. **Constructores**: un `@param` por cada parametro. En `Mascota` el `@param activa` debe explicar que significa una mascota inactiva (dada de baja o fallecida) y su consecuencia en la agenda. En `Cita` el `@param horario` debe indicar el formato exacto `aaaa-MM-dd HH:mm`.
3. **Cada getter publico**: resumen + `@return`.
4. En `estaActiva()` deje escrita la consecuencia en palabras: **una mascota inactiva no puede agendar citas**.

Reglas de forma del Javadoc: comentario `/** ... */` **inmediatamente antes** del elemento, resumen en una frase que termina en punto, y las etiquetas en el orden `@param`, `@return`, `@throws`.

**Al ejecutar (el `main` no cambia) debe imprimir exactamente:**

```
M-001 - Kira (felino, activa)
M-009 - Rocky (canino, inactiva)
Cita C-01 para M-001 el 2026-09-15 10:00
Kira puede agendar: true
Rocky puede agendar: false
```

Adjunte tambien, en el mismo campo de codigo y como comentario al final del archivo, el comando o los pasos exactos que uso en NetBeans para generar el HTML (`clic derecho sobre el proyecto > Generate Javadoc`) y la ruta donde quedo la carpeta generada.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
public class Main {

    public static void main(String[] args) {
        Mascota kira = new Mascota("M-001", "Kira", "felino", true);
        Mascota rocky = new Mascota("M-009", "Rocky", "canino", false);
        Cita cita = new Cita("C-01", "M-001", "2026-09-15 10:00");

        System.out.println(kira);
        System.out.println(rocky);
        System.out.println(cita);
        System.out.println("Kira puede agendar: " + kira.estaActiva());
        System.out.println("Rocky puede agendar: " + rocky.estaActiva());
    }
}

/**
 * TODO: bloque Javadoc de la clase Mascota.
 * Escriba un resumen de una linea de que representa la clase en la clinica «Huellitas»
 * y la etiqueta @author con su nombre completo.
 */
class Mascota {

    private final String id;
    private final String nombre;
    private final String especie;
    private final boolean activa;

    /**
     * TODO: documente el constructor con un @param por cada parametro.
     * Explique en el @param de activa que significa que una mascota este inactiva
     * (dada de baja o fallecida) y que consecuencia tiene en la agenda.
     */
    public Mascota(String id, String nombre, String especie, boolean activa) {
        this.id = id;
        this.nombre = nombre;
        this.especie = especie;
        this.activa = activa;
    }

    /**
     * TODO: documente con resumen y @return.
     */
    public String getId() {
        return id;
    }

    /**
     * TODO: documente con resumen y @return.
     */
    public String getNombre() {
        return nombre;
    }

    /**
     * TODO: documente con resumen y @return, dejando escrita la consecuencia:
     * una mascota inactiva no puede agendar citas.
     */
    public boolean estaActiva() {
        return activa;
    }

    @Override
    public String toString() {
        return id + " - " + nombre + " (" + especie + ", " + (activa ? "activa" : "inactiva") + ")";
    }
}

/**
 * TODO: bloque Javadoc de la clase Cita, con resumen y @author.
 */
class Cita {

    private final String id;
    private final String idMascota;
    private final String horario;

    /**
     * TODO: documente el constructor con un @param por parametro.
     * En horario indique el formato exacto esperado: aaaa-MM-dd HH:mm
     */
    public Cita(String id, String idMascota, String horario) {
        this.id = id;
        this.idMascota = idMascota;
        this.horario = horario;
    }

    /**
     * TODO: documente con resumen y @return.
     */
    public String getHorario() {
        return horario;
    }

    /**
     * TODO: documente con resumen y @return.
     */
    public String getIdMascota() {
        return idMascota;
    }

    @Override
    public String toString() {
        return "Cita " + id + " para " + idMascota + " el " + horario;
    }
}
```

**Rubrica esperada (campo Rubrica):**

Cada clase, constructor y getter publico tiene su bloque /** */ inmediatamente antes, con resumen en una frase. Los constructores tienen un @param por parametro y los getters su @return. El Javadoc de estaActiva y del @param activa dejan escrita en palabras la regla de que una mascota inactiva no agenda. El codigo sigue compilando y la salida es la pedida.

---

## Pregunta 2 - Codigo ejecutable · 25 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## `AgendaService.agendar`: la regla documentada y lanzada

Este es el metodo que sostiene el negocio. Tiene tres formas de fallar y todas deben quedar **documentadas con `@throws` y programadas**.

Complete `agendar(String idMascota, String horario)`:

1. Si el ID no existe en el mapa: `throw new NoSuchElementException("No existe ninguna mascota con el ID M-404")`.
2. Si la mascota **no esta activa**: `throw new IllegalStateException("La mascota M-009 Rocky esta inactiva y no puede agendar citas")`.
3. Si el horario **ya esta ocupado**: `throw new IllegalStateException("El horario 2026-09-15 10:00 ya esta ocupado")`.
4. Si todo esta bien: guarde el horario y devuelva el consecutivo `"C-0" + (citas.size())` una vez agregada, con la mascota y el horario.

Y escriba el **Javadoc completo** del metodo: resumen que deje escrita la regla *una mascota inactiva no puede agendar*, `@param` de los dos parametros, `@return` y los **tres `@throws`**. Documente tambien la clase con resumen y `@author`.

Escenario del `main`: M-001 Kira (activa), M-002 Michi (activa), M-009 Rocky (inactiva).

**Al ejecutar debe imprimir exactamente:**

```
Cita agendada: C-01 para M-001 Kira el 2026-09-15 10:00
Rechazada: La mascota M-009 Rocky esta inactiva y no puede agendar citas
Rechazada: No existe ninguna mascota con el ID M-404
Rechazada: El horario 2026-09-15 10:00 ya esta ocupado
Citas en agenda: 1
```

De cuatro intentos solo **una** cita quedo agendada: la ultima linea es la prueba de que las tres reglas se aplicaron.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.NoSuchElementException;

public class Main {

    public static void main(String[] args) {
        AgendaService agenda = new AgendaService();
        agenda.registrarMascota(new Mascota("M-001", "Kira", true));
        agenda.registrarMascota(new Mascota("M-002", "Michi", true));
        agenda.registrarMascota(new Mascota("M-009", "Rocky", false));

        intentar(agenda, "M-001", "2026-09-15 10:00");
        intentar(agenda, "M-009", "2026-09-15 11:00");
        intentar(agenda, "M-404", "2026-09-15 12:00");
        intentar(agenda, "M-002", "2026-09-15 10:00");

        System.out.println("Citas en agenda: " + agenda.totalCitas());
    }

    private static void intentar(AgendaService agenda, String idMascota, String horario) {
        try {
            System.out.println("Cita agendada: " + agenda.agendar(idMascota, horario));
        } catch (IllegalStateException | NoSuchElementException ex) {
            System.out.println("Rechazada: " + ex.getMessage());
        }
    }
}

class Mascota {

    private final String id;
    private final String nombre;
    private final boolean activa;

    public Mascota(String id, String nombre, boolean activa) {
        this.id = id;
        this.nombre = nombre;
        this.activa = activa;
    }

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public boolean estaActiva() {
        return activa;
    }
}

/**
 * TODO: bloque Javadoc de la clase con resumen, @author y la regla de negocio central
 * de la agenda de «Huellitas».
 */
class AgendaService {

    private final Map<String, Mascota> mascotas = new HashMap<>();
    private final List<String> citas = new ArrayList<>();

    public void registrarMascota(Mascota m) {
        mascotas.put(m.getId(), m);
    }

    /**
     * TODO: documente este metodo con Javadoc completo:
     *   - resumen que deje ESCRITA la regla: una mascota inactiva no puede agendar
     *   - @param idMascota
     *   - @param horario (formato aaaa-MM-dd HH:mm)
     *   - @return que devuelve cuando la cita queda agendada
     *   - @throws NoSuchElementException cuando el ID no existe
     *   - @throws IllegalStateException cuando la mascota esta inactiva
     *   - @throws IllegalStateException cuando el horario ya esta ocupado
     */
    public String agendar(String idMascota, String horario) {
        // TODO 1: busque la mascota en el mapa; si no existe lance
        //         new NoSuchElementException("No existe ninguna mascota con el ID M-404")
        // TODO 2: si la mascota NO esta activa lance
        //         new IllegalStateException("La mascota M-009 Rocky esta inactiva y no puede agendar citas")
        // TODO 3: si el horario ya esta ocupado lance
        //         new IllegalStateException("El horario 2026-09-15 10:00 ya esta ocupado")
        // TODO 4: si todo esta bien, guarde el horario y devuelva
        //         "C-01 para M-001 Kira el 2026-09-15 10:00"
        //         (el consecutivo se arma con "C-0" + (citas.size() + 1))
        return "";
    }

    public boolean horarioOcupado(String horario) {
        return citas.contains(horario);
    }

    public int totalCitas() {
        return citas.size();
    }
}
```

**Rubrica esperada (campo Rubrica):**

agendar valida en el orden pedido y lanza NoSuchElementException e IllegalStateException con los mensajes exactos. El Javadoc del metodo tiene resumen con la regla escrita, @param de los dos parametros, @return y al menos dos @throws. La salida coincide linea por linea y totalCitas queda en 1.

---

## Pregunta 3 - Codigo ejecutable · 25 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## Cuatro pruebas que se ejecutan solas

Una regla sin prueba es una promesa. Escriba las cuatro pruebas de `AgendaService`.

> **Nota sobre la herramienta:** en ExamLab no hay JUnit disponible, asi que usamos el **mismo diseño** con un mini-arnes ya escrito: el metodo `verificar(String nombrePrueba, boolean condicion)` imprime `[OK]` o `[FALLO]` y lleva la cuenta. En NetBeans usted llevara estas mismas cuatro pruebas a `Test Packages` con `@Test` y `assertEquals` / `assertThrows`: el nombre y el escenario no cambian.

`AgendaService` ya viene completo y correcto. El metodo `nuevaAgenda()` prepara el escenario **de cero en cada prueba** (M-001 Kira activa, M-002 Michi activa, M-009 Rocky inactiva): ninguna prueba puede depender de otra.

Complete los cuatro casos, cada uno terminando en **una** llamada a `verificar(...)` con la condicion real:

1. `mascotaActivaAgendaCitaCorrectamente`: agenda M-001 a las `2026-09-15 10:00` y `totalCitas()` queda en 1.
2. `mascotaInactivaLanzaIllegalStateException`: agendar M-009 **lanza** `IllegalStateException` y la agenda queda en 0 citas.
3. `idInexistenteLanzaNoSuchElementException`: agendar `M-404` **lanza** `NoSuchElementException`.
4. `horarioOcupadoNoDuplicaLaCita`: agenda M-001 a las `2026-09-15 10:00`, luego intenta M-002 en el **mismo** horario: lanza `IllegalStateException` y `totalCitas()` sigue en 1.

Para los casos que esperan excepcion use el patron: dentro del `try` llame al metodo y luego `verificar(nombre, false)` (si llego ahi, **no** lanzo y la prueba falla); en el `catch` haga `verificar(nombre, <condicion del estado>)`.

**Al ejecutar debe imprimir exactamente:**

```
[OK] mascotaActivaAgendaCitaCorrectamente
[OK] mascotaInactivaLanzaIllegalStateException
[OK] idInexistenteLanzaNoSuchElementException
[OK] horarioOcupadoNoDuplicaLaCita
Pruebas ejecutadas: 4 | exitosas: 4 | fallidas: 0
```

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.NoSuchElementException;

public class Main {

    private static int ejecutadas = 0;
    private static int exitosas = 0;

    public static void main(String[] args) {
        mascotaActivaAgendaCitaCorrectamente();
        mascotaInactivaLanzaIllegalStateException();
        idInexistenteLanzaNoSuchElementException();
        horarioOcupadoNoDuplicaLaCita();

        System.out.println("Pruebas ejecutadas: " + ejecutadas
                + " | exitosas: " + exitosas
                + " | fallidas: " + (ejecutadas - exitosas));
    }

    /** Prepara una agenda nueva: cada prueba arranca con su propio escenario limpio. */
    private static AgendaService nuevaAgenda() {
        AgendaService agenda = new AgendaService();
        agenda.registrarMascota(new Mascota("M-001", "Kira", true));
        agenda.registrarMascota(new Mascota("M-002", "Michi", true));
        agenda.registrarMascota(new Mascota("M-009", "Rocky", false));
        return agenda;
    }

    private static void mascotaActivaAgendaCitaCorrectamente() {
        AgendaService agenda = nuevaAgenda();
        // TODO: agende M-001 a las "2026-09-15 10:00" y verifique con verificar(...)
        //       que agenda.totalCitas() quedo en 1
        verificar("mascotaActivaAgendaCitaCorrectamente", false);
    }

    private static void mascotaInactivaLanzaIllegalStateException() {
        AgendaService agenda = nuevaAgenda();
        // TODO: intente agendar M-009 (inactiva). La prueba pasa si SE LANZA
        //       IllegalStateException y la agenda queda en 0 citas.
        //       Estructura: try { agendar; verificar(nombre, false); }
        //                   catch (IllegalStateException ex) { verificar(nombre, agenda.totalCitas() == 0); }
        verificar("mascotaInactivaLanzaIllegalStateException", false);
    }

    private static void idInexistenteLanzaNoSuchElementException() {
        AgendaService agenda = nuevaAgenda();
        // TODO: intente agendar "M-404". La prueba pasa si se lanza NoSuchElementException.
        verificar("idInexistenteLanzaNoSuchElementException", false);
    }

    private static void horarioOcupadoNoDuplicaLaCita() {
        AgendaService agenda = nuevaAgenda();
        // TODO: agende M-001 a las "2026-09-15 10:00" y luego intente agendar M-002
        //       en el MISMO horario. La prueba pasa si se lanza IllegalStateException
        //       y totalCitas() sigue en 1.
        verificar("horarioOcupadoNoDuplicaLaCita", false);
    }

    /** Mini-arnes de pruebas: imprime [OK] o [FALLO] y lleva la cuenta. */
    private static void verificar(String nombrePrueba, boolean condicion) {
        ejecutadas++;
        if (condicion) {
            exitosas++;
            System.out.println("[OK] " + nombrePrueba);
        } else {
            System.out.println("[FALLO] " + nombrePrueba);
        }
    }
}

class Mascota {

    private final String id;
    private final String nombre;
    private final boolean activa;

    public Mascota(String id, String nombre, boolean activa) {
        this.id = id;
        this.nombre = nombre;
        this.activa = activa;
    }

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public boolean estaActiva() {
        return activa;
    }
}

class AgendaService {

    private final Map<String, Mascota> mascotas = new HashMap<>();
    private final List<String> citas = new ArrayList<>();

    public void registrarMascota(Mascota m) {
        mascotas.put(m.getId(), m);
    }

    public String agendar(String idMascota, String horario) {
        Mascota m = mascotas.get(idMascota);
        if (m == null) {
            throw new NoSuchElementException("No existe ninguna mascota con el ID " + idMascota);
        }
        if (!m.estaActiva()) {
            throw new IllegalStateException("La mascota " + m.getId() + " " + m.getNombre()
                    + " esta inactiva y no puede agendar citas");
        }
        if (citas.contains(horario)) {
            throw new IllegalStateException("El horario " + horario + " ya esta ocupado");
        }
        citas.add(horario);
        return "C-0" + citas.size() + " para " + m.getId() + " " + m.getNombre() + " el " + horario;
    }

    public int totalCitas() {
        return citas.size();
    }
}
```

**Rubrica esperada (campo Rubrica):**

Los cuatro casos estan implementados, cada uno con su propia agenda recien creada (independencia real). Los tres casos de excepcion verifican que SI se lanzo la excepcion esperada y ademas el estado (0 o 1 citas), usando verificar(nombre, false) dentro del try. La ejecucion imprime cuatro [OK] y el resumen con 4 exitosas y 0 fallidas.

---

## Pregunta 4 - Seleccion multiple · 10 pts

**Tipo en la plataforma:** `cerrada_multi`

**Enunciado (campo Contenido):**

## Lo que distingue una prueba util de un adorno

Marque **todas** las afirmaciones verdaderas.

**Opciones:**

- [x] El nombre de una prueba debe leerse solo y decir escenario y resultado esperado, por ejemplo mascotaInactivaLanzaIllegalStateException.
- [ ] Una prueba puede depender del estado que dejo la anterior: asi se ahorra codigo de preparacion.
- [x] Una prueba que espera una excepcion debe fallar si la excepcion NO se lanza, no solo cuando se lanza otra.
- [ ] Si la barra de pruebas esta verde, el Javadoc ya no hace falta porque las pruebas documentan el codigo.
- [x] Al comentar la validacion de la mascota inactiva, la prueba correspondiente debe ponerse roja: eso demuestra que la prueba realmente esta ejerciendo esa regla.
- [ ] @param se usa para documentar lo que devuelve el metodo y @return para sus parametros.

**Rubrica esperada (campo Rubrica):**

Correctas: opciones 0, 2 y 4. Se califica por afirmaciones acertadas menos las marcadas por error.

---

## Pregunta 5 - Respuesta escrita · 15 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Rojo, verde y lo que ninguna prueba puede ver

**(a) Rojo y verde (obligatorio).** Comente a proposito la validacion de la mascota inactiva en `agendar`, ejecute las pruebas y luego restaurela. Reporte: que prueba se puso en `[FALLO]`, el texto exacto que imprimio el arnes en rojo, y el resultado despues de restaurar. Adjunte las dos capturas (rojo y verde) en su entrega de NetBeans.

**(b) Refactor > Rename.** Liste los **tres identificadores pobres** que renombro en su proyecto con `Refactor > Rename` de NetBeans (por ejemplo `validar` -> `agendar`, `b` -> `mascotaActiva`, `dato1` -> `idMascota`), en cuantos archivos se propago cada cambio y por que el nombre nuevo es mejor.

**(c) Dos pruebas manuales.** Escriba **dos comportamientos de VetCare que NO se pueden automatizar** con pruebas de codigo, y para cada uno indique los pasos exactos que hara la persona que lo verifique y el resultado esperado. Explique en una linea por que la automatizacion no aplica en esos dos casos.

**(d) Javadoc generado.** Indique la ruta de la carpeta HTML generada y copie el texto del resumen que aparece en la ficha de `AgendaService` sobre la regla de la mascota inactiva.

**Rubrica esperada (campo Rubrica):**

(a) Identifica la prueba que se pone roja al comentar la validacion, con el texto del arnes, y confirma el verde al restaurar. (b) Lista tres renombres concretos con propagacion y justificacion. (c) Propone dos verificaciones genuinamente manuales (aspecto de la ventana, legibilidad de un mensaje, comportamiento del foco) con pasos y resultado esperado. (d) Reporta la ruta del HTML y el texto de la regla tal como aparece.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
