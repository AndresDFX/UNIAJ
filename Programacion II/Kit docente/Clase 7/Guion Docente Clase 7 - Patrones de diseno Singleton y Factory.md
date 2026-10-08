# Guion docente · Clase 7 · Patrones de diseno · Singleton y Factory

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** VetCare queda con un unico repositorio de datos en memoria compartido por todas las ventanas y una fabrica que crea las consultas del dominio.
- **Entregable de hoy:** Clase RepositorioClinica convertida en Singleton, FabricaConsultas con tres tipos y evidencia de que dos ventanas ven la misma lista, subido a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 7 - Patrones de diseno Singleton y Factory/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Las ideas de cada concepto estan proyectadas y el desarrollo completo esta en las notas del presentador de su lamina. Aqui va, por lamina y en su orden, lo que hay que subrayar.

**[Slide 4] Qué es un patrón de diseño** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.

**[Slide 5] El problema: un solo archivador** — 3 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: El problema que motiva el Singleton ya lo vivimos en la clase pasada, aunque no le pusimos nombre.
  - Subrayar: En VetCare la ventana de registro creaba su propio RepositorioMascotas.
  - Subrayar: Esa es exactamente la intencion del patron Singleton.

**[Slide 6] Singleton: tres piezas obligatorias** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.

**[Slide 7] RepositorioClinica: el Singleton** — programa completo (25 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 8] Comprobar que es la misma instancia** — programa completo (42 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 9] Cada ventana pide getInstancia()** — programa completo (49 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 10] Factory: quién decide qué objeto crear** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.

**[Slide 11] Consulta: el tipo base** — programa completo (25 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 12] ConsultaUrgencia: una subclase** — programa completo (25 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 13] FabricaConsultas.crear()** — programa completo (45 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 14] La fábrica en uso** — programa completo (43 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 15] Cuándo NO usarlos** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.

## Errores tipicos del docente que no domina el tema

Material de preparacion: no se proyecta.

- Error tipico del docente que no domina el tema: enseñar el Singleton como 'la forma correcta de compartir variables entre ventanas' y terminar poniendo el atributo publico y estatico (public static RepositorioClinica instancia), con lo cual cualquiera puede reasignarlo desde afuera y ya no hay ninguna garantia; o dejar el constructor publico 'porque el editor lo sugiere', que es exactamente lo unico que no se puede hacer. El segundo error clasico es creer que el Singleton persiste datos: los estudiantes cierran la aplicacion, la vuelven a abrir y preguntan donde quedaron las mascotas, y hay que explicar que el Singleton solo garantiza una instancia mientras el programa corre, que la persistencia en archivos es otro tema que veremos mas adelante. El tercero es la patronitis: llenar el proyecto de fabricas que solo devuelven new de una sola clase y de Singletons para cosas que deberian ser objetos comunes, como Mascota o Cita, que por definicion son muchos. Si al preguntar 'que problema resuelve este patron aqui' la respuesta es 'que lo vimos en clase', el patron esta sobrando.


**Demo que usted debe poder repetir:** El docente abre dos ventanas de VetCare, registra una mascota en la primera y la muestra apareciendo en la segunda porque ambas comparten la unica instancia del repositorio.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare queda con un unico repositorio de datos en memoria compartido por todas las ventanas y una fabrica que crea las consultas del dominio.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de concepto y en las de codigo
(lo que hay que subrayar esta tambien en las notas del presentador de cada lamina). Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente abre dos ventanas de VetCare, registra una mascota en la primera y la muestra apareciendo en la segunda porque ambas comparten la unica instancia del repositorio.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 7/Codigo/ClinicaPatronesDemo.java`

### 60-105 · Taller guiado (opcional) = avance del PI
Opcional: no tiene lamina en el deck. La guia esta en
`Clases/Clase 7 - Patrones de diseno Singleton y Factory/Taller PI - Clase 7 - VetCare.docx`; si hoy no se hace, se extiende la demo y la practica libre.
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Convierta RepositorioClinica en Singleton: atributo private static instancia, constructor private con un System.out.println que avise cuando se crea, y metodo public static synchronized getInstancia(); ejecute el programa y verifique que el mensaje de creacion aparece una sola vez aunque llame getInstancia() tres veces.
2. Elimine todos los 'new RepositorioClinica()' que queden en las ventanas y reemplacelos por RepositorioClinica.getInstancia(); use Ctrl+F en el proyecto para confirmar que no queda ni uno solo fuera del propio metodo getInstancia.
3. Cree la jerarquia Consulta (abstracta) con ConsultaVacunacion, ConsultaControl y ConsultaUrgencia, cada una con su duracionMinutos() y tarifaBase(), y la clase FabricaConsultas con el metodo estatico crear(String tipo, String idMascota) que normalice el texto y lance IllegalArgumentException si el tipo no existe.
4. Ejecute el demo y compruebe dos cosas: en la consola, que el mensaje del constructor sale una sola vez y que los dos identityHashCode coinciden; en pantalla, que al registrar M-002 Michi en la ventana Recepcion y oprimir Refrescar en la ventana Consultorio, Michi aparece junto a M-001 Kira, que fue registrada desde el main.
5. Escriba al final del archivo un comentario de tres lineas justificando por que el repositorio SI es Singleton, por que Mascota NO debe serlo y que problema tendria el Singleton cuando lleguemos a las pruebas; suba el proyecto y el comentario a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Clase RepositorioClinica convertida en Singleton, FabricaConsultas con tres tipos y evidencia de que dos ventanas ven la misma lista, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Si hubo taller, repasar los criterios de exito del `Taller PI - Clase 7 - VetCare.docx` (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 7/Quiz Clase 7 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare queda con un unico repositorio de datos en memoria compartido por todas las ventanas y una fabrica que crea las consultas del dominio.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 7/Solucion Taller Clase 7 - VetCare.docx` — no proyectar completa.
