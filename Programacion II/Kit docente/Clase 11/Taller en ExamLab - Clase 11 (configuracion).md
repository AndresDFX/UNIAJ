# Taller de la Clase 11 en ExamLab - configuracion

- **Curso:** Programacion II (FI303204)
- **Taller:** Taller Clase 11 en ExamLab - Revision de codigo cruzada sobre VetCare
- **Preguntas:** 6 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** Cada estudiante recibe un informe externo con hallazgos priorizados y deja escrito su plan de corrección de VetCare antes de la integración final.
- **Entregable de la clase:** Informe de revisión de una página sobre el proyecto asignado (el de otro estudiante; si el docente autorizó equipos, el de otro equipo): checklist diligenciado con evidencia archivo:línea y cinco hallazgos priorizados con formato Evidencia + Impacto + Sugerencia, subido a ExamLab.

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** El estudiante ejecuta y audita un VetCare ajeno con un checklist de doce items, redacta cinco hallazgos priorizados con Evidencia + Impacto + Sugerencia, parcha los bloqueantes y deja escrito el plan de correccion.

---

## Pregunta 1 - Codigo ejecutable · 20 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## Primero ejecutar, despues opinar

Este es `VetCareParaRevisar.java`, el proyecto que le toco revisar. **No lo arregle todavia**: hoy solo lo ejecuta y provoca los cuatro casos borde de VetCare.

Complete el `main` agregando, uno por uno, los cuatro casos borde marcados con `TODO`:

1. Registrar una mascota con la edad escrita como texto: `"tres"`.
2. Registrar una mascota con el nombre vacio: `""`.
3. Buscar el ID inexistente `"M-404"` e imprimir el **nombre** de lo que devuelve.
4. Llamar a `cargarDesdeCsv("archivo_que_no_existe.csv")`.

Los casos 1 y 3 **revientan la aplicacion**, asi que pruebelos por separado (deje activo uno a la vez y comente los otros). Eso es parte del ejercicio: hay que ver el fallo con los ojos.

**Para cada caso anote textualmente en un comentario al final del archivo:**

```
// CASO 1 (edad "tres"): <se cayo o no> | <nombre de la excepcion y mensaje exacto> | <linea del stack trace>
// CASO 2 (nombre vacio): ...
// CASO 3 (buscar M-404): ...
// CASO 4 (archivo inexistente): ...
```

Fijese especialmente en el caso 4: la aplicacion **no dice nada**. Ese silencio es un hallazgo, no un exito. Guarde este archivo tal como esta: es la evidencia con la que va a escribir el informe.

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        VetCareParaRevisar app = new VetCareParaRevisar();
        app.cargarDesdeCsv("mascotas.csv");
        app.registrar("M-001", "Firulais", "canino", "4");
        app.registrar("M-002", "Michi", "felino", "2");
        app.registrar("M-003", "Rocky", "canino", "9");
        app.listar();

        // TODO CASO BORDE 1: registre una mascota con la edad escrita como texto: "tres"
        // TODO CASO BORDE 2: registre una mascota con el nombre vacio: ""
        // TODO CASO BORDE 3: busque el ID inexistente "M-404" e imprima el nombre de lo que devuelve
        // TODO CASO BORDE 4: llame a cargarDesdeCsv con la ruta "archivo_que_no_existe.csv"
        //
        // Ejecute UNO POR UNO (los que revientan hay que probarlos por separado)
        // y copie TEXTUALMENTE el mensaje o la excepcion que produjo cada caso.
    }
}

class MascotaRev {

    public String dato1;
    public String nombre;
    public String especie;
    public int edad;

    public MascotaRev(String dato1, String nombre, String especie, int edad) {
        this.dato1 = dato1;
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
    }
}

class VetCareParaRevisar {

    ArrayList<MascotaRev> lista = new ArrayList<>();

    public void registrar(String dato1, String nombre, String especie, String edadTexto) {
        int e = Integer.parseInt(edadTexto);
        MascotaRev m = new MascotaRev(dato1, nombre, especie, e);
        lista.add(m);
        System.out.println("Registrada " + dato1);
        if (e >= 18) {
            System.out.println("ALERTA: mascota geriatrica");
        }
        if (e >= 18) {
            System.out.println("Se recomienda control cada 6 meses");
        }
    }

    public MascotaRev buscar(String dato1) {
        for (int i = 0; i < lista.size(); i++) {
            if (lista.get(i).dato1 == dato1) {
                return lista.get(i);
            }
        }
        return null;
    }

    public void listar() {
        for (int i = 0; i < lista.size(); i++) {
            System.out.println(lista.get(i).dato1 + " " + lista.get(i).nombre + " "
                    + lista.get(i).especie + " " + lista.get(i).edad);
        }
    }

    public void cargarDesdeCsv(String ruta) {
        try {
            BufferedReader br = new BufferedReader(new FileReader(ruta));
            String linea = br.readLine();
            while (linea != null) {
                String[] p = linea.split(";");
                lista.add(new MascotaRev(p[0], p[1], p[2], Integer.parseInt(p[3])));
                linea = br.readLine();
            }
        } catch (Exception ex) {
        }
    }
}
```

**Rubrica esperada (campo Rubrica):**

Los cuatro casos borde estan agregados al main y probados. Los comentarios finales reportan textualmente, caso por caso, si la aplicacion se cayo, el nombre exacto de la excepcion (NumberFormatException en el caso 1, NullPointerException en el caso 3) y el comportamiento observado. El caso 4 se reporta como silencio total, no como exito.

---

## Pregunta 2 - Respuesta escrita · 20 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Checklist de doce items con evidencia `archivo:linea`

Recorra el `VetCareParaRevisar.java` de la pregunta anterior con el checklist de la clase. Para **cada** item escriba `cumple`, `no cumple` o `no aplica`, y en **todos** los que marque `no cumple` la evidencia localizable en formato `archivo:linea` (o los pasos para reproducirlo).

| # | Item |
|---|------|
| 1 | Existe una clase de dominio con responsabilidad clara |
| 2 | Encapsulamiento: atributos privados con acceso controlado |
| 3 | Uso adecuado de coleccion (List/Map/Set) |
| 4 | Interfaz grafica o de consola separada de la logica |
| 5 | try-catch en las fronteras (entrada de usuario y archivos) |
| 6 | Persistencia funcionando y tolerante a fallos |
| 7 | Ningun catch vacio |
| 8 | Metodos cortos, una sola responsabilidad |
| 9 | Sin codigo duplicado |
| 10 | Nombres que se explican solos |
| 11 | Sin numeros magicos |
| 12 | Validacion de casos borde |

Use este formato por linea:

```
Item 7 (catch vacio): no cumple - VetCareParaRevisar.java:linea NN, el catch (Exception ex) del metodo cargarDesdeCsv no tiene una sola instruccion adentro.
```

Cierre con **una frase** de resumen: ¿arranco el proyecto?, ¿cuantos items en `no cumple`?

**Rubrica esperada (campo Rubrica):**

Los doce items estan marcados. Cada 'no cumple' trae evidencia localizable en formato archivo:linea o pasos reproducibles, y apunta a defectos que existen realmente en el codigo entregado (campos publicos, comparacion de String con ==, catch vacio, parseInt sin proteger, numero magico 18, duplicacion en el bloque geriatrico, nombres dato1 y e). Cierra con el resumen de arranque y conteo.

---

## Pregunta 3 - Seleccion multiple · 10 pts

**Tipo en la plataforma:** `cerrada_multi`

**Enunciado (campo Contenido):**

## ¿Cuales de estos comentarios sirven como retroalimentacion?

Un revisor escribio estos comentarios sobre `VetCareParaRevisar.java`. Marque **todos** los que son retroalimentacion accionable (se refieren al codigo, traen evidencia y proponen algo).

**Opciones:**

- [x] cargarDesdeCsv:linea 78 tiene un catch (Exception ex) vacio: si el archivo no existe la aplicacion no informa nada y el usuario cree que se cargaron los datos. Sugerencia: capturar FileNotFoundException por separado y mostrar un aviso con la ruta.
- [ ] Este codigo es un desastre, se ve que lo hicieron a ultima hora.
- [x] buscar():linea 62 compara IDs con == en vez de equals: funciona por casualidad con literales, pero fallara con IDs leidos del CSV o escritos por el usuario. Sugerencia: usar dato1.equals(...) y renombrar el parametro a idMascota.
- [ ] Hay que mejorar la calidad general del proyecto y aplicar buenas practicas.
- [x] registrar():linea 47 usa el numero 18 dos veces para decidir si la mascota es geriatrica, y el bloque esta duplicado. Sugerencia: extraer private static final int EDAD_GERIATRICA = 18 y unir los dos if en uno.
- [ ] El companero que escribio esto no entendio nada de la Clase 6.

**Rubrica esperada (campo Rubrica):**

Correctas: opciones 0, 2 y 4. Las demas atacan a la persona, son vagas o no proponen nada. Se califica por acertadas menos las marcadas por error.

---

## Pregunta 4 - Respuesta escrita · 25 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Cinco hallazgos priorizados

Escriba **cinco hallazgos** sobre el proyecto revisado, cada uno con esta estructura exacta:

```
HALLAZGO N - [BLOQUEANTE | MAYOR | MENOR]
Evidencia: <archivo:linea + que se observa, o los pasos para reproducirlo>
Impacto: <que le pasa al usuario de la clinica, no que le disgusta a usted>
Sugerencia: <el cambio concreto propuesto, con nombres de metodos o constantes>
```

Reglas de la revision:
- **Al menos uno debe ser BLOQUEANTE** (algo que tumba la aplicacion o hace perder datos): en este codigo existen varios candidatos reales, eligalos con criterio.
- Prioridad ordenada: los bloqueantes primero.
- **Ninguno puede referirse a la persona, a su esfuerzo ni a "no estudio"**. Se revisa codigo, no gente.
- Cada hallazgo debe ser distinto: no repita el mismo defecto con dos redacciones.
- Al menos uno debe apoyarse en los **casos borde** que ejecuto en la pregunta 1, citando el mensaje textual que observo.

**Rubrica esperada (campo Rubrica):**

Hay cinco hallazgos distintos con el formato Evidencia + Impacto + Sugerencia y prioridad marcada, con al menos un BLOQUEANTE real (parseInt sin proteger, catch vacio, NPE al buscar un ID inexistente o perdida de datos). El impacto esta redactado desde el usuario de la clinica y la sugerencia es concreta. Ningun hallazgo se refiere a la persona.

---

## Pregunta 5 - Codigo ejecutable · 15 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## Parche de los bloqueantes (mostrar, no solo decir)

Una revision gana autoridad cuando el revisor puede demostrar el arreglo. Sobre el **mismo** `VetCareParaRevisar.java`, aplique unicamente estas tres correcciones y deje el resto como esta:

1. **`registrar`**: proteja `Integer.parseInt` (`try-catch` de `NumberFormatException`) y valide que el nombre no venga vacio. Ante un dato invalido: **no** agregue la mascota a la lista e imprima el aviso.
2. **`buscar`**: compare los IDs con `equals` en vez de `==`.
3. **`cargarDesdeCsv`**: elimine el catch vacio. Use `try-with-resources` para el `BufferedReader` y capture informando la ruta.

Ademas extraiga el numero magico `18` a `private static final int EDAD_GERIATRICA = 18;` y una los dos `if` duplicados en uno solo.

En el `main`, deje activos los cuatro casos borde de la pregunta 1.

**Al ejecutar debe imprimir exactamente:**

```
Aviso: no se pudo leer mascotas.csv (archivo inexistente o ilegible), se arranca con la lista vacia
Registrada M-001
Registrada M-002
Registrada M-003
M-001 Firulais canino 4
M-002 Michi felino 2
M-003 Rocky canino 9
Rechazada: la edad debe ser un numero entero, se recibio 'tres'
Rechazada: el nombre es obligatorio
No existe ninguna mascota con el ID M-404
Aviso: no se pudo leer archivo_que_no_existe.csv (archivo inexistente o ilegible), se arranca con la lista vacia
```

Ahora los cuatro casos borde producen **mensajes** y la aplicacion sigue viva hasta el final: eso es lo que va en el informe como "verificado".

**Lenguaje:** `java`

**Codigo de partida (starter):**

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        VetCareParaRevisar app = new VetCareParaRevisar();
        app.cargarDesdeCsv("mascotas.csv");
        app.registrar("M-001", "Firulais", "canino", "4");
        app.registrar("M-002", "Michi", "felino", "2");
        app.registrar("M-003", "Rocky", "canino", "9");
        app.listar();

        // TODO CASO BORDE 1: registre una mascota con la edad escrita como texto: "tres"
        // TODO CASO BORDE 2: registre una mascota con el nombre vacio: ""
        // TODO CASO BORDE 3: busque el ID inexistente "M-404" e imprima el nombre de lo que devuelve
        // TODO CASO BORDE 4: llame a cargarDesdeCsv con la ruta "archivo_que_no_existe.csv"
        //
        // Ejecute UNO POR UNO (los que revientan hay que probarlos por separado)
        // y copie TEXTUALMENTE el mensaje o la excepcion que produjo cada caso.
    }
}

class MascotaRev {

    public String dato1;
    public String nombre;
    public String especie;
    public int edad;

    public MascotaRev(String dato1, String nombre, String especie, int edad) {
        this.dato1 = dato1;
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
    }
}

class VetCareParaRevisar {

    ArrayList<MascotaRev> lista = new ArrayList<>();

    public void registrar(String dato1, String nombre, String especie, String edadTexto) {
        int e = Integer.parseInt(edadTexto);
        MascotaRev m = new MascotaRev(dato1, nombre, especie, e);
        lista.add(m);
        System.out.println("Registrada " + dato1);
        if (e >= 18) {
            System.out.println("ALERTA: mascota geriatrica");
        }
        if (e >= 18) {
            System.out.println("Se recomienda control cada 6 meses");
        }
    }

    public MascotaRev buscar(String dato1) {
        for (int i = 0; i < lista.size(); i++) {
            if (lista.get(i).dato1 == dato1) {
                return lista.get(i);
            }
        }
        return null;
    }

    public void listar() {
        for (int i = 0; i < lista.size(); i++) {
            System.out.println(lista.get(i).dato1 + " " + lista.get(i).nombre + " "
                    + lista.get(i).especie + " " + lista.get(i).edad);
        }
    }

    public void cargarDesdeCsv(String ruta) {
        try {
            BufferedReader br = new BufferedReader(new FileReader(ruta));
            String linea = br.readLine();
            while (linea != null) {
                String[] p = linea.split(";");
                lista.add(new MascotaRev(p[0], p[1], p[2], Integer.parseInt(p[3])));
                linea = br.readLine();
            }
        } catch (Exception ex) {
        }
    }
}
```

**Rubrica esperada (campo Rubrica):**

registrar protege parseInt y valida el nombre vacio, y en ambos casos no agrega nada a la lista. buscar usa equals. cargarDesdeCsv usa try-with-resources y su catch informa la ruta, sin quedar vacio. El 18 quedo en una constante y la duplicacion se unio. La ejecucion completa los cuatro casos borde sin caerse y la salida coincide con la pedida.

---

## Pregunta 6 - Respuesta escrita · 10 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Plan de correccion del autor del proyecto

Ahora cambie de silla: usted es el **autor** del proyecto que recibio la revision. Para cada uno de los cinco hallazgos escriba una linea con las tres decisiones posibles y un **responsable con nombre y apellido**:

```
HALLAZGO N - ACEPTO Y CORRIJO: <que va a cambiar exactamente> - Responsable: <nombre> - Antes del: <fecha>
HALLAZGO N - JUSTIFICO Y DEJO IGUAL: <por que la decision original es valida> - Responsable: <nombre>
HALLAZGO N - DIFIERO: <por que no ahora y para cuando> - Responsable: <nombre>
```

Requisitos:
- Los cinco hallazgos deben tener decision y responsable. **Ninguna linea sin dueño.**
- Al menos uno debe ser `ACEPTO Y CORRIJO` (si hubo bloqueante, ese va aqui obligatoriamente).
- Al menos uno debe ser `JUSTIFICO` o `DIFIERO` con un argumento tecnico real, no "no hay tiempo" a secas.
- Cierre con una frase sobre la devolucion de ocho minutos: **que hallazgo le costo mas aceptar y por que**.

**Rubrica esperada (campo Rubrica):**

Los cinco hallazgos tienen decision explicita (acepto / justifico / difiero) y un responsable identificado por linea. El bloqueante quedo en ACEPTO Y CORRIJO con el cambio descrito. Al menos una justificacion o diferimiento trae argumento tecnico. Cierra con la reflexion sobre la devolucion.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
