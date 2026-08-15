# Guion docente · Clase 13 · Control de excepciones · try-catch-finally

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** El registro de mascotas de VetCare valida edad, peso e ID y avisa con un mensaje claro en lugar de cerrarse.
- **Entregable de hoy:** Clase DatoInvalidoException mas los setters validados de Mascota y la carga del CSV con try-with-resources, con evidencia de cinco pruebas de entrada (cuatro malas y una valida), subido a ExamLab.
- **Herramienta:** Apache NetBeans
- **Slides:** `Clases/Clase 13 - Control de excepciones/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Una excepcion es un objeto que Java crea en el momento exacto en que una instruccion no puede cumplir lo que promete, y que interrumpe el flujo normal del programa para buscar a alguien que se haga cargo. No es un mensaje de texto: es un objeto con tipo, mensaje y rastro de llamadas (stack trace). Toda la familia cuelga de Throwable, que se divide en Error (fallas de la maquina virtual, como quedarse sin memoria, que no debemos atrapar) y Exception (fallas del programa o del entorno, que si podemos atender). En VetCare esto se ve todos los dias: cuando la secretaria de la clinica Huellitas escribe 'tres' en el campo edad y el codigo hace Integer.parseInt(txtEdad.getText()), Java no puede convertir esa palabra en numero, entonces fabrica un objeto NumberFormatException, lo lanza hacia arriba y, como nadie lo recibe, el hilo muere: la ventana queda congelada y en la consola aparece el chorro rojo que asusta al usuario. La excepcion no es el enemigo, es el mensajero; el problema es que nadie la esta esperando.

Java parte las excepciones en dos grupos y esa division decide cuanto codigo debe escribir usted. Las checked (Exception y sus hijas, menos RuntimeException) representan fallas previsibles del mundo exterior: el archivo mascotas.csv que alguien borro, el disco lleno, la carpeta sin permisos; el compilador las vigila y obliga a capturarlas con try-catch o a declararlas con throws, y si no lo hace su proyecto ni siquiera compila. Las unchecked (RuntimeException y sus hijas: NumberFormatException, NullPointerException, ArrayIndexOutOfBoundsException, ArithmeticException) representan errores de programacion o datos que nadie valido, y el compilador las deja pasar en silencio hasta que explotan en ejecucion. La regla practica que le sirve al estudiante es esta: si la falla viene de afuera (archivo, red, base de datos) casi siempre es checked; si la falla viene de adentro (usted no valido, usted no inicializo el objeto, usted se salio del arreglo) casi siempre es unchecked. En VetCare la lectura de datos/mascotas.csv lanza IOException, que es checked, y la conversion de la edad lanza NumberFormatException, que es unchecked; por eso se manejan en lugares distintos del programa y por eso una obliga a escribir throws y la otra no.

La estructura try-catch-finally tiene una anatomia que conviene explicar despacio. En el try va el codigo que puede fallar y nada mas: entre menos lineas tenga el try, mas facil es saber quien fallo. En los catch va la reaccion, y se escriben del tipo mas especifico al mas general, porque Java entrega la excepcion al primer catch que la acepte; si usted pone catch (Exception e) antes de catch (NumberFormatException e), NetBeans marca error de compilacion con el mensaje 'exception has already been caught'. Por la misma razon, al leer el CSV de VetCare, catch (FileNotFoundException e) va antes que catch (IOException e), porque la primera es hija de la segunda. Desde Java 7 se pueden unir tipos hermanos con multi-catch: catch (NumberFormatException | NullPointerException e). El bloque finally se ejecuta siempre, haya o no haya excepcion, e incluso si dentro del try hay un return (lo unico que se lo salta es apagar la maquina virtual con System.exit), y por eso fue durante anios el sitio para cerrar archivos y liberar recursos. Hoy preferimos el try-with-resources, que abre el recurso entre los parentesis del try y lo cierra solo, y funciona con cualquier objeto que implemente la interfaz AutoCloseable, como BufferedReader o PrintWriter: try (BufferedReader lector = new BufferedReader(new FileReader('datos/mascotas.csv'))) { ... }. En VetCare esto significa que si el CSV esta corrupto a la mitad, el archivo igual se cierra y la aplicacion sigue viva con las mascotas que alcanzo a leer.

throw y throws se parecen en el nombre y hacen cosas opuestas, y esa confusion es la que mas cuesta en el parcial. throw (sin s) es una instruccion que se ejecuta y lanza un objeto en ese instante: throw new DatoInvalidoException('La edad debe estar entre 0 y 30 anios.'). throws (con s) es una advertencia escrita en la firma del metodo: public void setEdad(String texto) throws DatoInvalidoException, y significa 'yo no resuelvo esto, quien me llame vera que hace'. De ahi sale la regla de capas que usaremos en VetCare: las clases del dominio (Mascota, Dueno, Cita) validan y LANZAN, porque no saben si hay una ventana, una consola o un servidor al otro lado; la capa de interfaz (el JFrame o el menu de consola) CAPTURA y traduce ese error a un JOptionPane que el usuario entiende. Crear una excepcion propia vale la pena por dos motivos: como DatoInvalidoException extiende Exception queda checked, es decir que el compilador no deja que nadie llame a setEdad sin hacerse cargo del error, y ademas el mensaje ya viene escrito en lenguaje de la clinica y no en lenguaje de la maquina: el usuario lee 'La edad debe ser un numero entero' y no 'For input string: tres'.

El catch vacio, ese catch (Exception e) { } que aparece cuando NetBeans ofrece 'Surround with try-catch' y el estudiante borra el contenido para que no moleste, es el error mas caro del curso. Silencia la falla pero no la arregla: el objeto queda a medio construir, la mascota nunca se agrego a la lista, el usuario cree que guardo y el error reaparece tres pantallas mas adelante como un NullPointerException que no tiene nada que ver con la causa real. Manejar una excepcion significa hacer al menos una de cuatro cosas: informarle al usuario en su idioma, registrar el problema para poder repararlo despues, asumir un valor por defecto que este documentado, o relanzar la excepcion envuelta en otra con mas contexto. Ojo: e.printStackTrace() tampoco es manejar, es apenas dejar una nota en una consola que el usuario final nunca ve. Y la mejor excepcion es la que no ocurre: validar antes de convertir (revisar null, aplicar trim, verificar isEmpty y comprobar el rango) evita el 80 por ciento de los try-catch de VetCare y hace que el codigo se lea como las reglas del negocio.

Error tipico del docente que no domina el tema: envolver todo el main en un unico try { ... } catch (Exception e) { } gigante y anunciarle al grupo que 'el programa ya quedo blindado'. Lo que quedo fue ciego: cualquier falla, venga del archivo o de la edad, cae en el mismo saco, se pierde la causa y el usuario no recibe ningun mensaje util. Otras variantes del mismo error son usar excepciones para controlar el flujo normal (lanzar una excepcion para decir que la busqueda no encontro la mascota, en vez de devolver null o un Optional), atrapar Throwable o Error creyendo que 'asi cubro todo', y explicar que las excepciones 'son cuando el programa se dana', lo cual deja al estudiante sin la idea clave: la excepcion es un canal de comunicacion entre la capa que detecta el problema y la capa que sabe como responderle al humano. Antes de la clase practique tres cosas en NetBeans: provocar el error de compilacion por catch mal ordenado, mostrar que finally se ejecuta incluso cuando el try hace return, y borrar datos/mascotas.csv para que el grupo vea la diferencia entre FileNotFoundException y IOException; son las tres preguntas que el grupo siempre hace.

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
1. Paso 1. Abra el proyecto VetCare en NetBeans, cree el paquete vetcare.excepciones y dentro la clase DatoInvalidoException que extienda Exception con un constructor que reciba el mensaje; compile y verifique que no hay errores.
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
