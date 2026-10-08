# Guion docente · Clase 13 · Control de excepciones · try-catch-finally

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** El registro de mascotas de VetCare valida edad, peso e ID y avisa con un mensaje claro en lugar de cerrarse.
- **Entregable de hoy:** Clase DatoInvalidoException mas los setters validados de Mascota y la carga del CSV con try-with-resources, con evidencia de cinco pruebas de entrada (cuatro malas y una valida), subido a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 13 - Control de excepciones/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Las ideas de cada concepto estan proyectadas y el desarrollo completo esta en las notas del presentador de su lamina. Aqui va, por lamina y en su orden, lo que hay que subrayar.

**[Slide 4] Qué es una excepción** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Toda la familia cuelga de Throwable, que se divide en Error (fallas de la maquina virtual, como quedarse sin memoria, que no debemos atrapar) y Exception (fallas del programa o del entorno, que si podemos atender).

**[Slide 5] Checked y unchecked** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.

**[Slide 6] Una excepción checked propia** — programa completo (24 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 7] Anatomía de try-catch-finally** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: La estructura try-catch-finally tiene una anatomia que conviene explicar despacio.
  - Subrayar: En VetCare esto significa que si el CSV esta corrupto a la mitad, el archivo igual se cierra y la aplicacion sigue viva con las mascotas que alcanzo a leer.

**[Slide 8] registrar(): try, catch y finally** — programa completo (47 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 9] finally corre aunque haya return** — programa completo (41 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 10] cargar(): del catch específico al general** — programa completo (43 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 11] throw, throws y la excepción propia** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: throw y throws se parecen en el nombre y hacen cosas opuestas, y esa confusion es la que mas cuesta en el parcial. throw (sin s) es una instruccion que se ejecuta y lanza un objeto en ese instante: throw. throws (con s) es una advertencia escrita en la firma del metodo: public void setEdad(String texto) throws DatoInvalidoException, y significa 'yo no resuelvo esto, quien me llame vera que hace'.
  - Subrayar: De ahi sale la regla de capas que usaremos en VetCare: las clases del dominio (Mascota, Dueno, Cita) validan y LANZAN, porque no saben si hay una ventana, una consola o un servidor al otro lado; la capa de interfaz (el JFrame o el menu de consola) CAPTURA y traduce ese error a un JOptionPane que el usuario entiende.

**[Slide 12] setEdad(): validar y lanzar** — programa completo (43 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 13] El catch vacío** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Y la mejor excepcion es la que no ocurre: validar antes de convertir (revisar null, aplicar trim, verificar isEmpty y comprobar el rango) evita el 80 por ciento de los try-catch de VetCare y hace que el codigo se lea como las reglas del negocio.

**[Slide 14] malaPractica(): así no** — programa completo (39 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

## Errores tipicos del docente que no domina el tema

Material de preparacion: no se proyecta.

- Error tipico del docente que no domina el tema: envolver todo el main en un unico try { ... } catch (Exception e) { } gigante y anunciarle al grupo que 'el programa ya quedo blindado'. Lo que quedo fue ciego: cualquier falla, venga del archivo o de la edad, cae en el mismo saco, se pierde la causa y el usuario no recibe ningun mensaje util. Otras variantes del mismo error son usar excepciones para controlar el flujo normal (lanzar una excepcion para decir que la busqueda no encontro la mascota, en vez de devolver null o un Optional), atrapar Throwable o Error creyendo que 'asi cubro todo', y explicar que las excepciones 'son cuando el programa se dana', lo cual deja al estudiante sin la idea clave: la excepcion es un canal de comunicacion entre la capa que detecta el problema y la capa que sabe como responderle al humano. Antes de la clase practique tres cosas en VS Code: provocar el error de compilacion por catch mal ordenado, mostrar que finally se ejecuta incluso cuando el try hace return, y borrar datos/mascotas.csv para que el grupo vea la diferencia entre FileNotFoundException y IOException; son las tres preguntas que el grupo siempre hace.


**Demo que usted debe poder repetir:** El docente escribe 'tres' en el campo edad, muestra la aplicacion reventando con el stack trace rojo, y en vivo la envuelve en try-catch hasta que responde con un aviso amable.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: El registro de mascotas de VetCare valida edad, peso e ID y avisa con un mensaje claro en lugar de cerrarse.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de concepto y en las de codigo
(lo que hay que subrayar esta tambien en las notas del presentador de cada lamina). Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente escribe 'tres' en el campo edad, muestra la aplicacion reventando con el stack trace rojo, y en vivo la envuelve en try-catch hasta que responde con un aviso amable.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 13/Codigo/DemoExcepcionesClinica.java`

### 60-105 · Taller guiado (opcional) = avance del PI
Opcional: no tiene lamina en el deck. La guia esta en
`Clases/Clase 13 - Control de excepciones/Taller PI - Clase 13 - VetCare.docx`; si hoy no se hace, se extiende la demo y la practica libre.
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Paso 1. Abra el proyecto VetCare en VS Code, cree el paquete clinica.excepciones y dentro la clase DatoInvalidoException que extienda Exception con un constructor que reciba el mensaje; compile y verifique que no hay errores.
2. Paso 2. En la clase Mascota reemplace setEdad(int) por setEdad(String texto) throws DatoInvalidoException: rechace vacio, convierta con Integer.parseInt dentro de un try, atrape NumberFormatException y relance DatoInvalidoException con un mensaje de la clinica, y valide el rango 0 a 30; repita la idea en setPeso con Double.parseDouble y rango 0.1 a 120.
3. Paso 3. En el formulario de registro (JFrame o menu de consola) envuelva las llamadas a los setters en un try-catch que muestre JOptionPane.showMessageDialog con e.getMessage(), devuelva el foco al campo culpable con requestFocus() y NO agregue la mascota a la lista cuando hubo error.
4. Paso 4. Cambie la carga de datos/mascotas.csv a try-with-resources con dos catch separados: FileNotFoundException, que arranca con lista vacia e informa que es la primera ejecucion, e IOException, que muestra el problema real; las lineas del CSV con datos malos se omiten con un aviso, sin tumbar la carga completa.
5. Paso 5. Pruebe el formulario con estas cinco entradas de edad: vacio, 'tres', '-2', '150' y '4'; capture la pantalla de cada caso, arme una tabla de evidencia con entrada, mensaje mostrado y estado de la aplicacion, y suba el codigo mas la tabla a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Clase DatoInvalidoException mas los setters validados de Mascota y la carga del CSV con try-with-resources, con evidencia de cinco pruebas de entrada (cuatro malas y una valida), subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Si hubo taller, repasar los criterios de exito del `Taller PI - Clase 13 - VetCare.docx` (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 13/Quiz Clase 13 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: El registro de mascotas de VetCare valida edad, peso e ID y avisa con un mensaje claro en lugar de cerrarse.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 13/Solucion Taller Clase 13 - VetCare.docx` — no proyectar completa.
