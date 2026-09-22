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

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Una excepcion es un objeto que Java crea en el momento exacto en que...** — 6 vinetas.

**Java parte las excepciones en dos grupos y esa division decide cuanto... (1/2)** — 4 vinetas.

**Java parte las excepciones en dos grupos y esa division decide cuanto... (2/2)** — 4 vinetas.

**La estructura try-catch-finally tiene una anatomia que conviene... (1/2)** — 6 vinetas.

**La estructura try-catch-finally tiene una anatomia que conviene... (2/2)** — 4 vinetas.

**Throw y throws se parecen en el nombre y hacen cosas opuestas, y esa... (1/2)** — 2 vinetas.

**Throw y throws se parecen en el nombre y hacen cosas opuestas, y esa... (2/2)** — 3 vinetas.

**El catch vacio, ese catch (Exception e) { } que aparece cuando VS Code...** — 7 vinetas.


**Demo que usted debe poder repetir:** El docente escribe 'tres' en el campo edad, muestra la aplicacion reventando con el stack trace rojo, y en vivo la envuelve en try-catch hasta que responde con un aviso amable.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: El registro de mascotas de VetCare valida edad, peso e ID y avisa con un mensaje claro en lugar de cerrarse.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente escribe 'tres' en el campo edad, muestra la aplicacion reventando con el stack trace rojo, y en vivo la envuelve en try-catch hasta que responde con un aviso amable.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 13/Codigo/DemoExcepcionesVetCare.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Paso 1. Abra el proyecto VetCare en VS Code, cree el paquete vetcare.excepciones y dentro la clase DatoInvalidoException que extienda Exception con un constructor que reciba el mensaje; compile y verifique que no hay errores.
2. Paso 2. En la clase Mascota reemplace setEdad(int) por setEdad(String texto) throws DatoInvalidoException: rechace vacio, convierta con Integer.parseInt dentro de un try, atrape NumberFormatException y relance DatoInvalidoException con un mensaje de la clinica, y valide el rango 0 a 30; repita la idea en setPeso con Double.parseDouble y rango 0.1 a 120.
3. Paso 3. En el formulario de registro (JFrame o menu de consola) envuelva las llamadas a los setters en un try-catch que muestre JOptionPane.showMessageDialog con e.getMessage(), devuelva el foco al campo culpable con requestFocus() y NO agregue la mascota a la lista cuando hubo error.
4. Paso 4. Cambie la carga de datos/mascotas.csv a try-with-resources con dos catch separados: FileNotFoundException, que arranca con lista vacia e informa que es la primera ejecucion, e IOException, que muestra el problema real; las lineas del CSV con datos malos se omiten con un aviso, sin tumbar la carga completa.
5. Paso 5. Pruebe el formulario con estas cinco entradas de edad: vacio, 'tres', '-2', '150' y '4'; capture la pantalla de cada caso, arme una tabla de evidencia con entrada, mensaje mostrado y estado de la aplicacion, y suba el codigo mas la tabla a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Clase DatoInvalidoException mas los setters validados de Mascota y la carga del CSV con try-with-resources, con evidencia de cinco pruebas de entrada (cuatro malas y una valida), subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 13/Quiz Clase 13 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: El registro de mascotas de VetCare valida edad, peso e ID y avisa con un mensaje claro en lugar de cerrarse.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 13/Solucion Taller Clase 13 - VetCare.docx` — no proyectar completa.
