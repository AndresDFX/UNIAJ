# Guion docente · Clase 7 · Patrones de diseno · Singleton y Factory

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** VetCare queda con un unico repositorio de datos en memoria compartido por todas las ventanas y una fabrica que crea las consultas del dominio.
- **Entregable de hoy:** Clase RepositorioVetCare convertida en Singleton, FabricaConsultas con tres tipos y evidencia de que dos ventanas ven la misma lista, subido a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 7 - Patrones de diseno Singleton y Factory/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Un patron de diseño no es una libreria que se importa ni un archivo que...** — 6 vinetas.

**El problema que motiva el Singleton ya lo vivimos en la clase pasada...** — 6 vinetas.

**El mecanismo en Java tiene tres piezas y las tres son obligatorias (1/2)** — 4 vinetas.

**El mecanismo en Java tiene tres piezas y las tres son obligatorias (2/2)** — 3 vinetas.

**El segundo patron responde a otro problema distinto: quien decide como...** — 6 vinetas.

**Ahora la parte que casi nadie enseña: cuando NO usarlos** — 8 vinetas.


**Demo que usted debe poder repetir:** El docente abre dos ventanas de VetCare, registra una mascota en la primera y la muestra apareciendo en la segunda porque ambas comparten la unica instancia del repositorio.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare queda con un unico repositorio de datos en memoria compartido por todas las ventanas y una fabrica que crea las consultas del dominio.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente abre dos ventanas de VetCare, registra una mascota en la primera y la muestra apareciendo en la segunda porque ambas comparten la unica instancia del repositorio.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 7/Codigo/VetCarePatronesDemo.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Convierta RepositorioVetCare en Singleton: atributo private static instancia, constructor private con un System.out.println que avise cuando se crea, y metodo public static synchronized getInstancia(); ejecute el programa y verifique que el mensaje de creacion aparece una sola vez aunque llame getInstancia() tres veces.
2. Elimine todos los 'new RepositorioVetCare()' que queden en las ventanas y reemplacelos por RepositorioVetCare.getInstancia(); use Ctrl+F en el proyecto para confirmar que no queda ni uno solo fuera del propio metodo getInstancia.
3. Cree la jerarquia Consulta (abstracta) con ConsultaVacunacion, ConsultaControl y ConsultaUrgencia, cada una con su duracionMinutos() y tarifaBase(), y la clase FabricaConsultas con el metodo estatico crear(String tipo, String idMascota) que normalice el texto y lance IllegalArgumentException si el tipo no existe.
4. Ejecute el demo y compruebe dos cosas: en la consola, que el mensaje del constructor sale una sola vez y que los dos identityHashCode coinciden; en pantalla, que al registrar M-002 Michi en la ventana Recepcion y oprimir Refrescar en la ventana Consultorio, Michi aparece junto a M-001 Kira, que fue registrada desde el main.
5. Escriba al final del archivo un comentario de tres lineas justificando por que el repositorio SI es Singleton, por que Mascota NO debe serlo y que problema tendria el Singleton cuando lleguemos a las pruebas; suba el proyecto y el comentario a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Clase RepositorioVetCare convertida en Singleton, FabricaConsultas con tres tipos y evidencia de que dos ventanas ven la misma lista, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 7/Quiz Clase 7 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare queda con un unico repositorio de datos en memoria compartido por todas las ventanas y una fabrica que crea las consultas del dominio.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 7/Solucion Taller Clase 7 - VetCare.docx` — no proyectar completa.
