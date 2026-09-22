# Guion docente · Clase 9 · Refactorización con IA · Persistencia en archivos

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** VetCare guarda la lista de mascotas en mascotas.csv al cerrar y la vuelve a cargar al abrir.
- **Entregable de hoy:** La clase RepositorioMascotasCSV con guardar() y cargar() funcionando, el archivo mascotas.csv generado por la propia aplicación y la bitácora REFACTOR.md, subidos a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 9 - Refactorizacion con IA y persistencia de archivos/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Refactorizar es cambiar la forma interna del código sin cambiar ni un... (1/2)** — 5 vinetas.

**Refactorizar es cambiar la forma interna del código sin cambiar ni un... (2/2)** — 3 vinetas.

**Un code smell es un síntoma en el código que casi siempre anuncia un... (1/2)** — 6 vinetas.
  - Quinto, el catch vacío que se traga la IOException y deja al usuario creyendo que guardó.

**Un code smell es un síntoma en el código que casi siempre anuncia un... (2/2)** — 3 vinetas.

**Persistencia es lograr que los datos sobrevivan al proceso que los creó (1/2)** — 5 vinetas.
  - Guardar en disco significa convertir cada objeto Mascota en texto y escribirlo en un archivo que queda en el computador.

**Persistencia es lograr que los datos sobrevivan al proceso que los creó (2/2)** — 3 vinetas.

**Un archivo abierto es un recurso del sistema operativo, y todo recurso... (1/2)** — 4 vinetas.
  - Por eso el error más desconcertante para un principiante es este: el programa corre sin lanzar ninguna excepción, dice 'guardado', y el archivo mascotas.csv aparece con cero bytes.
  - Reemplaza al viejo patrón de finally con verificación de null, que casi nadie escribe bien.

**Un archivo abierto es un recurso del sistema operativo, y todo recurso... (2/2)** — 3 vinetas.

**La persistencia se conecta al ciclo de vida de la aplicación en dos... (1/2)** — 3 vinetas.
  - Cargar al arrancar significa que el main construye el repositorio, pide cargar() y solo después muestra la ventana con la tabla ya poblada.
  - Por eso conviene imprimir una vez ruta.toAbsolutePath() para que el estudiante sepa dónde buscarlo en vez de jurar que el programa no guardó nada.

**La persistencia se conecta al ciclo de vida de la aplicación en dos... (2/2)** — 3 vinetas.

**VetCarePersistencia.java — class VetCarePersistencia** — 2 vinetas.

**VetCarePersistencia.java — main() (1/2)** — 20 vinetas.

**VetCarePersistencia.java — main() (2/2)** — 11 vinetas.

**VetCarePersistencia.java — siguienteId() (1/2)** — 20 vinetas.

**VetCarePersistencia.java — siguienteId() (2/2)** — 1 vinetas.

**VetCarePersistencia.java — class Mascota** — 8 vinetas.

**VetCarePersistencia.java — Mascota()** — 8 vinetas.

**VetCarePersistencia.java — class RepositorioMascotasCSV** — 8 vinetas.

**VetCarePersistencia.java — RepositorioMascotasCSV()** — 4 vinetas.

**VetCarePersistencia.java — rutaAbsoluta()** — 5 vinetas.

**VetCarePersistencia.java — guardar()** — 14 vinetas.

**VetCarePersistencia.java — cargar() (1/2)** — 20 vinetas.

**VetCarePersistencia.java — cargar() (2/2)** — 5 vinetas.

**VetCarePersistencia.java — aLinea()** — 8 vinetas.

**VetCarePersistencia.java — desdeLinea()** — 19 vinetas.

**VetCarePersistencia.java — limpiar()** — 8 vinetas.


**Demo que usted debe poder repetir:** El docente registra una mascota, cierra la aplicación, la vuelve a abrir y la mascota sigue ahí; enseguida abre mascotas.csv en el Bloc de notas para mostrar la línea que escribió el programa.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare guarda la lista de mascotas en mascotas.csv al cerrar y la vuelve a cargar al abrir.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente registra una mascota, cierra la aplicación, la vuelve a abrir y la mascota sigue ahí; enseguida abre mascotas.csv en el Bloc de notas para mostrar la línea que escribió el programa.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 9/Codigo/VetCarePersistencia.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Cree el paquete vetcare.datos y dentro la clase RepositorioMascotasCSV con la constante private static final String SEPARADOR = ";", la constante ENCABEZADO con el texto id;nombre;especie;edad;cedula_dueno y un atributo Path ruta construido con Paths.get("mascotas.csv"); compile el proyecto y verifique que no hay errores rojos antes de seguir.
2. Implemente guardar(List<Mascota>) usando try-with-resources: escriba el encabezado, recorra la lista y escriba una línea por mascota; ejecute, abra mascotas.csv en el Bloc de notas y verifique que tiene exactamente tantas líneas como mascotas más una, y el mismo número de punto y coma en todas.
3. Implemente cargar() de forma defensiva: si el archivo no existe devuelve una lista vacía, descarta la línea de encabezado, ignora las líneas que no tengan cinco campos e ignora las que traigan una edad no numérica, avisando por consola el número de la línea; compruébelo dañando a propósito una línea del archivo y volviendo a ejecutar.
4. Conecte el repositorio al ciclo de vida de la aplicación: cargar() al arrancar antes de mostrar la ventana y guardar() al cerrar; cierre la aplicación, vuelva a abrirla y verifique que el conteo de mascotas en la tabla es el mismo que había antes de cerrar.
5. Haga una revisión asistida por IA de su método guardar(): pídale a la herramienta que señale problemas, aplique como máximo dos mejoras que usted pueda explicar en voz alta, rechace por escrito al menos una sugerencia y registre todo en REFACTOR.md con el formato 'sugerencia / la acepté o no / por qué'; vuelva a correr el flujo completo y confirme que el comportamiento es idéntico.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: La clase RepositorioMascotasCSV con guardar() y cargar() funcionando, el archivo mascotas.csv generado por la propia aplicación y la bitácora REFACTOR.md, subidos a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 9/Quiz Clase 9 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare guarda la lista de mascotas en mascotas.csv al cerrar y la vuelve a cargar al abrir.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 9/Solucion Taller Clase 9 - VetCare.docx` — no proyectar completa.
