# Taller de la Clase 14 en ExamLab - configuracion

- **Curso:** Programacion II (FI303204)
- **Taller:** Taller Clase 14 en ExamLab - Preparacion de la sustentacion de VetCare
- **Preguntas:** 6 · **Total:** 100 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** VetCare queda con guion de sustentacion, juego de datos de demostracion sembrado y ensayo cronometrado dentro de la ventana de 5 a 8 minutos.
- **Entregable de la clase:** Guion de sustentacion con bloques, minutos y evidencia que se muestra (mas el responsable nominal solo si el docente autorizo equipo), mas la planilla de tiempos de dos ensayos y el video de respaldo de la ruta feliz, subido a ExamLab.

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** Cada estudiante deja el guion de sustentacion con bloques y minutos, el sembrador de datos de demostracion en [OK], dos ensayos cronometrados dentro de la ventana de 5 a 8 minutos y el plan B grabado.

---

## Pregunta 1 - Respuesta escrita · 25 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Guion de sustentacion: cinco bloques, responsable y minutos

Escriba el guion de la sustentacion de VetCare como una tabla de **cinco bloques**. El total planeado debe quedar entre **5 y 7 minutos** (dejando margen para llegar a los 8 sin pasarse) y la **demo en vivo debe ocupar por lo menos la mitad** del tiempo.

| # | Bloque | Responsable (su nombre; si hay equipo, el del integrante) | Minutos planeados | Que se dice o se muestra exactamente |
|---|--------|--------------------------------|-------------------|--------------------------------------|
| 1 | Problema de la clinica «Huellitas» y que resuelve VetCare | | | |
| 2 | Arquitectura: modelo, datos, logica, ui | | | |
| 3 | **Demo en vivo** (ruta feliz) | | | |
| 4 | **Demo en vivo** (caso de error controlado) | | | |
| 5 | Aprendizajes y siguiente paso | | | |

Requisitos:
- **Ningun bloque puede quedar sin responsable ni sin evidencia.** El trabajo es individual por defecto: si sustenta solo, los cinco bloques son suyos. Si el docente autorizo equipo de 2 o 3, todos los integrantes deben tener al menos un bloque y nadie queda sin intervencion.
- En el bloque 3 escriba los pasos exactos que va a ejecutar: registrar dueño, registrar mascota, agendar cita, buscar por ID, cerrar y volver a abrir mostrando que los datos siguen ahi.
- En el bloque 4 diga **cual error va a provocar a proposito** (por ejemplo escribir `tres` en el campo edad) y **que mensaje debe salir textualmente**.
- Escriba la **primera frase literal** con la que arranca el bloque 1 y la **frase de cierre** del bloque 5. Esas dos son las que mas se olvidan cuando hay nervios.
- Al final, la suma de minutos y el porcentaje que representa la demo en vivo (bloques 3 y 4) sobre el total.

**Rubrica esperada (campo Rubrica):**

La tabla tiene los cinco bloques con responsable identificado por nombre y minutos, sin ningun bloque huerfano (y, si hay equipo, todos los integrantes con al menos un bloque), y el total entre 5 y 7 minutos con la demo (bloques 3 y 4) ocupando la mitad o mas. El bloque 3 detalla los pasos de la ruta feliz y el 4 nombra el error que se provocara y el mensaje esperado. Incluye frase de apertura y de cierre literales y el calculo de porcentaje.

---

## Pregunta 2 - Codigo ejecutable · 25 pts

**Tipo en la plataforma:** `codigo`

**Enunciado (campo Contenido):**

## Sembrador de datos de demostracion y chequeo pre-vuelo

Una sustentacion con la lista vacia se cae sola: no hay nada que mostrar. Escriba el programa que deja los datos de demostracion sembrados y que **verifica** antes de salir a escena.

Complete `SembradorDemo`:

1. `sembrar()`: cree la carpeta `datos_demo` con `Files.createDirectories` y escriba los tres archivos con **try-with-resources**:
   - `duenos.csv` — encabezado `cedula;nombre;telefono` y **4 filas** (Ana Gomez 1094512, Carlos Ruiz 1128733, Luisa Perez 1002945, Marta Diaz 1156420).
   - `mascotas.csv` — encabezado `id;nombre;especie;edad;cedula_dueno` y **6 filas** (M-001 Firulais, M-002 Michi, M-003 Rocky, M-004 Canela, M-005 Toby, M-006 Nube).
   - `citas.csv` — encabezado `id;id_mascota;horario;motivo` y **3 filas** (C-01 vacunacion, C-02 control de displasia, C-03 dieta renal).
   Los datos exactos estan en los comentarios del starter.
2. `escribir(...)`: la escritura real, una sola vez, reutilizada por los tres archivos.
3. `chequeoPreVuelo()`: por cada archivo cuente las **filas de datos** (lineas menos el encabezado) e imprima `[OK]` con el conteo, o `[FALLA]` si no existe o esta vacio, devolviendo `false` en ese caso.
4. En el `main`: siembre, corra el chequeo y solo si todo esta en `[OK]` imprima la linea final.

**Al ejecutar debe imprimir exactamente:**

```
[OK] datos_demo/duenos.csv (4 filas)
[OK] datos_demo/mascotas.csv (6 filas)
[OK] datos_demo/citas.csv (3 filas)
Chequeo pre-vuelo: LISTO PARA SUSTENTAR
```

Este programa se corre **el mismo dia**, minutos antes de sustentar. Si alguna linea sale en `[FALLA]`, no se sale a escena.

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
        SembradorDemo sembrador = new SembradorDemo(Paths.get("datos_demo"));

        // TODO 1: siembre los tres archivos de demostracion
        // TODO 2: corra el chequeo pre-vuelo

        System.out.println("Chequeo pre-vuelo: LISTO PARA SUSTENTAR");
    }
}

class SembradorDemo {

    private final Path carpeta;

    public SembradorDemo(Path carpeta) {
        this.carpeta = carpeta;
    }

    /** Deja datos_demo con duenos.csv, mascotas.csv y citas.csv listos para la demo. */
    public void sembrar() {
        // TODO 3: cree la carpeta con Files.createDirectories(carpeta)
        // TODO 4: escriba duenos.csv con encabezado "cedula;nombre;telefono" y estas 4 filas:
        //         1094512;Ana Gomez;3001112233
        //         1128733;Carlos Ruiz;3014445566
        //         1002945;Luisa Perez;3027778899
        //         1156420;Marta Diaz;3030001122
        // TODO 5: escriba mascotas.csv con encabezado "id;nombre;especie;edad;cedula_dueno" y 6 filas:
        //         M-001;Firulais;canino;4;1094512
        //         M-002;Michi;felino;2;1128733
        //         M-003;Rocky;canino;9;1002945
        //         M-004;Canela;felino;11;1156420
        //         M-005;Toby;canino;1;1094512
        //         M-006;Nube;felino;6;1128733
        // TODO 6: escriba citas.csv con encabezado "id;id_mascota;horario;motivo" y 3 filas:
        //         C-01;M-001;2026-11-20 09:00;vacunacion
        //         C-02;M-003;2026-11-20 10:00;control de displasia
        //         C-03;M-004;2026-11-20 11:00;dieta renal
        // Use SIEMPRE try-with-resources y avise por consola si algo falla.
    }

    /** Escribe un archivo de la carpeta de demostracion con su encabezado y sus filas. */
    private void escribir(String nombreArchivo, String encabezado, List<String> filas) {
        // TODO 7: implemente la escritura con
        //         try (BufferedWriter w = Files.newBufferedWriter(carpeta.resolve(nombreArchivo),
        //                                                         StandardCharsets.UTF_8)) { ... }
    }

    /**
     * Chequeo pre-vuelo: los tres archivos deben existir y tener filas de datos.
     * Debe imprimir una linea por archivo con [OK] o [FALLA].
     */
    public boolean chequeoPreVuelo() {
        String[] archivos = {"duenos.csv", "mascotas.csv", "citas.csv"};
        boolean todoBien = true;
        for (String nombre : archivos) {
            // TODO 8: cuente las filas de datos (total de lineas menos el encabezado).
            //         Si el archivo existe y tiene mas de 0 filas imprima
            //         "[OK] datos_demo/duenos.csv (4 filas)"
            //         Si no existe o esta vacio imprima
            //         "[FALLA] datos_demo/duenos.csv (0 filas): siembre los datos antes de sustentar"
            //         y ponga todoBien en false.
        }
        return todoBien;
    }

    private List<String> leerLineas(Path ruta) {
        List<String> lineas = new ArrayList<>();
        if (!Files.exists(ruta)) {
            return lineas;
        }
        try {
            lineas.addAll(Files.readAllLines(ruta, StandardCharsets.UTF_8));
        } catch (IOException ex) {
            System.out.println("No se pudo leer " + ruta + ": " + ex.getMessage());
        }
        return lineas;
    }
}
```

**Rubrica esperada (campo Rubrica):**

sembrar crea la carpeta y escribe los tres archivos con try-with-resources y los datos exactos pedidos (4, 6 y 3 filas). El metodo escribir se reutiliza para los tres. chequeoPreVuelo cuenta filas descontando el encabezado, imprime [OK] con el conteo correcto y devolveria [FALLA] con false si faltara un archivo. La salida coincide caracter por caracter.

---

## Pregunta 3 - Respuesta escrita · 20 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Planilla de tiempos de los dos ensayos

Haga el **ensayo 1** de pie, hablando cada bloque completo sin saltarse ninguno (si trabaja en equipo, cada integrante el suyo), con cronometro. Ajuste el guion. Haga el **ensayo 2**. Reporte:

| Bloque | Minutos planeados | Ensayo 1 (real) | Ensayo 2 (real) | Diferencia | Que ajusto entre los dos ensayos |
|--------|-------------------|-----------------|-----------------|------------|----------------------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 (demo) | | | | | |
| 4 (demo) | | | | | |
| 5 | | | | | |
| **Total** | | | | | |

Ademas responda:
- **(a)** ¿En que bloque se les fue el tiempo en el ensayo 1 y **que quitaron** para recuperarlo? Sea especifico: que frase, que pantalla o que explicacion sobro.
- **(b)** El **total del ensayo 2 debe caer entre 5 y 8 minutos**. Escriba el minuto y segundo exactos. Si quedo fuera, diga que van a recortar y en cual bloque.
- **(c)** ¿Que porcentaje del ensayo 2 fue **demo en vivo**? Debe ser la mitad o mas.
- **(d)** Una cosa que salio **mal** en el ensayo 1 y no era de tiempo (se congelo la ventana, no encontro el archivo, se le olvido el turno a alguien) y como quedo resuelta para el ensayo 2.

**Rubrica esperada (campo Rubrica):**

La planilla trae minutos planeados y reales de los dos ensayos por bloque con la diferencia y el ajuste aplicado. El total del ensayo 2 esta declarado en minutos y segundos dentro de la ventana de 5 a 8 minutos, con la demo ocupando la mitad o mas. Responde las cuatro preguntas con hechos concretos del ensayo, no generalidades.

---

## Pregunta 4 - Respuesta escrita · 15 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Plan B: el video que salva la sustentacion

El dia de la sustentacion se cae el wifi, el portatil no proyecta o NetBeans decide actualizarse. El plan B se prepara **antes**, no se improvisa.

Reporte:

**(a) Video de la ruta feliz** (2 a 3 minutos, sin cortes, con la pantalla legible). Escriba el **minutaje** de cada momento:

| Momento | Minuto:segundo en el video |
|---------|---------------------------|
| Registrar dueño (Ana Gomez, 1094512) | |
| Registrar mascota (M-001 Firulais, canino, 4) | |
| Agendar cita (C-01, 2026-11-20 09:00) | |
| Buscar por ID (M-001) | |
| Cerrar la aplicacion | |
| Reabrir y mostrar que los datos siguen ahi | |

**(b) Seis capturas** exportadas de esos mismos momentos: liste los nombres de archivo y la carpeta del proyecto donde quedaron.

**(c) Verificacion sin internet (obligatoria).** Diga como comprobo que el video se reproduce **sin conexion**: en que carpeta local esta, con que reproductor lo abrio, formato y peso del archivo. Un enlace de Drive **no** es plan B.

**(d) Disparador.** Escriba la frase exacta que va a decir cuando decida pasar al video, y en que segundo del bloque de demo tomaria esa decision (por ejemplo: "si a los 30 segundos la aplicacion no abrio, paso al video").

**Rubrica esperada (campo Rubrica):**

El video existe y esta descrito con el minutaje de los seis momentos de la ruta feliz. Lista las seis capturas con nombre de archivo y carpeta. La verificacion sin internet reporta ubicacion local, reproductor, formato y peso (no un enlace en la nube). Incluye la frase disparadora y el criterio de segundos para activar el plan B.

---

## Pregunta 5 - Seleccion multiple · 5 pts

**Tipo en la plataforma:** `cerrada_multi`

**Enunciado (campo Contenido):**

## Lo que hunde una sustentacion

Marque **todas** las situaciones que, segun lo visto en clase, hacen fracasar una sustentacion aunque el codigo funcione.

**Opciones:**

- [x] Arrancar la demo con la lista vacia, sin datos sembrados, y perder dos minutos registrando fichas a mano.
- [ ] Provocar a proposito un error de validacion para mostrar el mensaje controlado.
- [x] Dedicar cinco de los ocho minutos a explicar la teoria de POO y dejar la demo para el final, sin tiempo.
- [x] No tener plan B y depender de que el proyector, el wifi y NetBeans funcionen a la primera.
- [ ] Ensayar de pie y con cronometro antes de sustentar.
- [x] Dejar un bloque del guion sin responsable ni evidencia (o, en trabajo en equipo, un integrante sin ningun bloque asignado que solo aparece a responder preguntas).

**Rubrica esperada (campo Rubrica):**

Correctas: opciones 0, 2, 3 y 5. Se califica por acertadas menos las marcadas por error.

---

## Pregunta 6 - Respuesta escrita · 10 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Ronda de jurado: cinco preguntas y respuestas de 30 segundos

Intercambien con otro estudiante -o con otro equipo, si el docente lo autorizo- una ronda de **cinco preguntas de jurado** sobre VetCare. Escriba las cinco preguntas que **recibio** (textuales) y, para cada una, su respuesta en **maximo 30 segundos** (tres o cuatro lineas), diciendo **con que evidencia en pantalla la sustenta** (y, si hay equipo, quien la responde).

Al menos dos de las cinco deben ser preguntas tecnicas incomodas del estilo:
- ¿Por que usaron `HashMap` y no `ArrayList` para los expedientes?
- ¿Que pasa si dos usuarios abren VetCare al mismo tiempo?
- ¿Donde exactamente valida usted que la edad no sea negativa? Muestremelo.
- ¿Por que el repositorio es Singleton y que problema les trajo?
- Si le pido agregar el campo peso, ¿cuantos archivos tiene que tocar?

Formato por pregunta:

```
PREGUNTA N (textual): ...
RESPONDE: <nombre y apellido>
RESPUESTA (30 s): ...
ARCHIVO O PANTALLA QUE VA A MOSTRAR: <clase:metodo, o que ventana abre>
```

Cierre con **una** frase: ¿cual de las cinco preguntas los dejo sin respuesta y que hicieron al respecto antes del ensayo 2?

**Rubrica esperada (campo Rubrica):**

Las cinco preguntas estan transcritas con responsable asignado y respuesta breve de 30 segundos, al menos dos de ellas tecnicas. Cada respuesta indica el archivo, clase o pantalla que se mostraria como evidencia. Cierra identificando la pregunta que los dejo sin respuesta y la accion correctiva tomada.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **100**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
