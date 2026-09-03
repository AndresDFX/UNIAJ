# Guion docente · Clase 8 · Documentacion y QA · Javadoc y pruebas

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** Las clases del dominio de VetCare quedan documentadas con Javadoc y la regla 'mascota inactiva no agenda' queda respaldada por pruebas que se ejecutan solas.
- **Entregable de hoy:** Mascota, Cita y AgendaService con Javadoc completo, la carpeta HTML generada y una clase de pruebas con cuatro casos, subidos a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 8 - Documentacion y QA Javadoc y pruebas/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Documentar no es llenar el codigo de comentarios. Un comentario como '// suma uno al contador' encima de la linea contador++ no le sirve a nadie: repite lo que ya dice el codigo y ademas envejece mal, porque cuando alguien cambia la linea nadie se acuerda de cambiar el comentario, y entonces el comentario miente. Javadoc resuelve otro problema, que es el del contrato: le dice a quien va a usar su clase que hace el metodo, que espera recibir, que devuelve y en que casos revienta, sin que esa persona tenga que abrir el codigo fuente. En VetCare esa diferencia es concreta: el estudiante que escriba la ventana de citas necesita saber que agendar() lanza excepcion si la mascota esta inactiva, y no tiene por que leer las veinte lineas del metodo para descubrirlo. La documentacion tecnica no describe la implementacion, describe la promesa.

Un bloque Javadoc se escribe con /** y se cierra con */, y va inmediatamente encima de la clase, del constructor, del atributo o del metodo que documenta (si lo pone debajo, no sirve). La primera frase debe ser un resumen corto que termine en punto, porque esa frase es la que aparece en las tablas resumen del HTML generado. Despues vienen las etiquetas: @param una por cada parametro con su nombre exacto, @return si el metodo devuelve algo, @throws por cada excepcion documentada, y a nivel de clase @author y @version. Se pueden usar marcas como {@code M-001} para que un texto se vea con tipografia de codigo y @see para remitir a otra clase. Lo que se genera es un sitio web: en VS Code se corre la herramienta del JDK desde la terminal integrada, «javadoc -d docs -private src/vetcare/*.java», que crea la carpeta docs/ y deja un index.html que se abre en el navegador con la misma cara que tiene la documentacion oficial de Java. Un beneficio inmediato que se ve sin generar nada: apenas usted escribe el Javadoc, VS Code se lo muestra al pasar el cursor cuando alguien invoca el metodo con Ctrl+Espacio.

Ahora bien, la mejor documentacion es la que no hay que escribir, y eso se logra con nombres que se explican solos. Compare 'public boolean verificar(String x)' con 'public boolean estaActiva(String idMascota)': la segunda no necesita comentario. En Java hay convenciones que el mundo entero respeta y que sus estudiantes deben respetar desde ya: clases en PascalCase (AgendaService), metodos y variables en camelCase (agendarCita, idMascota), constantes en MAYUSCULAS con guion bajo (TARIFA_BASE), metodos que devuelven boolean nombrados como una pregunta (estaActiva, tieneCitasPendientes), y metodos que hacen algo nombrados con verbo (agendar, registrar, buscarPorId). Nada de proc1, dato2, aux ni flag. En VetCare hicimos precisamente ese refactor: lo que empezo llamandose 'validar' pasa a llamarse 'agendar', y la variable 'b' pasa a llamarse 'mascotaActiva'; el codigo quedo igual de largo pero dejo de necesitar traductor.

La segunda mitad de la clase es control de calidad. Un caso de prueba tiene cuatro partes y conviene escribirlas en el tablero antes de tocar el teclado: un nombre que se lea como una frase, unos datos o estado de partida, una accion concreta y un resultado esperado. En ingles a esa estructura se le dice AAA: Arrange (preparar), Act (ejecutar), Assert (comprobar). Y no basta con probar que todo salga bien: por cada funcionalidad se necesitan pruebas positivas (mascota activa agenda y la cita queda registrada), negativas (mascota inactiva no agenda y lanza excepcion) y de borde (fecha vacia, ID inexistente, horario ya ocupado). Para la regla de hoy la tabla queda asi: caso 1, mascota M-001 Kira activa, agendar el 30 de septiembre a las 10:00, se espera una cita creada y total de citas igual a 1; caso 2, mascota M-009 Rocky inactiva, misma accion, se espera IllegalStateException y total de citas igual a 0. Fijese que el resultado esperado se define ANTES de correr el programa; si usted primero ejecuta y despues decide que esperaba, eso no es una prueba, es una conformidad.

JUnit es la herramienta que convierte esos casos en codigo que se ejecuta solo. En VS Code se agrega desde la vista Testing (el icono del matraz) con «Enable Java Tests» > JUnit 5, que baja los .jar solo; las clases de prueba viven en la carpeta test/, separadas del codigo de produccion; la convencion es AgendaServiceTest para probar AgendaService. Cada caso es un metodo publico anotado con @Test cuyo nombre describe el escenario (agendar_mascotaInactiva_lanzaIllegalStateException), con un metodo anotado @Before o @BeforeEach que arma el estado limpio antes de cada caso, para que ninguna prueba dependa de la anterior. Las comprobaciones se hacen con assertEquals(esperado, obtenido), assertTrue(condicion) y assertThrows(IllegalStateException.class, () -> agenda.agendar(...)), que es la forma moderna de verificar que algo debe fallar. La diferencia con la prueba manual es importante y hay que decirla completa: la prueba unitaria es automatica, repetible, rapida y prueba logica aislada, y por eso se corre cada vez que se toca el codigo; la prueba manual la hace un humano usando la interfaz, sirve para lo que no se puede automatizar facil (que el JOptionPane se lea bien, que la ventana no se congele, que el flujo tenga sentido para la recepcionista) y no reemplaza a la otra. Y aqui se cobra la clase 6: como la regla de agendar vive en AgendaService y no dentro de un boton, se puede probar sin abrir ni una sola ventana.

Error tipico del docente que no domina el tema: confundir Javadoc con comentarios normales y escribir // encima de los metodos creyendo que eso genera documentacion, o abrir el bloque con /* en vez de /** y despues no entender por que el HTML sale vacio. Muy de la mano va el vicio de documentar lo obvio (un @return 'retorna el nombre' sobre getNombre()) y dejar sin una sola linea el metodo agendar, que es justo donde vive la regla de negocio que nadie adivina. En pruebas los errores son igual de tipicos: llamar 'prueba' a un main con System.out.println donde el docente mira la consola y dice 'si, funciono' (eso no es automatico ni repetible, y nadie se entera cuando se rompe tres semanas despues); escribir pruebas que dependen del orden porque comparten un Singleton sucio de la prueba anterior; e intentar probar la ventana en vez del servicio, que es el sintoma clasico de haber metido la logica dentro del boton. Y el peor de todos, el que hay que desarmar en voz alta: creer que 'si compila, funciona'. Compilar solo significa que la sintaxis esta bien; que la mascota inactiva no pueda agendar cita es algo que solo se sabe si alguien lo comprueba.

**Demo que usted debe poder repetir:** El docente escribe un bloque Javadoc, genera la documentacion HTML con javadoc desde la terminal integrada y luego corre las pruebas mostrando la barra en rojo, corrige la regla y la muestra en verde.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Las clases del dominio de VetCare quedan documentadas con Javadoc y la regla 'mascota inactiva no agenda' queda respaldada por pruebas que se ejecutan solas.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente escribe un bloque Javadoc, genera la documentacion HTML con javadoc desde la terminal integrada y luego corre las pruebas mostrando la barra en rojo, corrige la regla y la muestra en verde.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 8/Codigo/VetCareQADemo.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Documente con Javadoc las clases Mascota y Cita y el servicio AgendaService: bloque de clase con resumen y @author, y en cada metodo publico @param por parametro, @return si aplica y @throws por cada excepcion; el metodo agendar debe dejar escrita la regla 'una mascota inactiva no puede agendar'.
2. Renombre al menos tres identificadores pobres del proyecto (por ejemplo validar por agendar, b por mascotaActiva, dato1 por idMascota) usando Rename Symbol (F2) de VS Code para que el cambio se propague sin romper nada.
3. Genere la documentacion con clic derecho sobre el proyecto y Generate Javadoc, abra el HTML y verifique que en la ficha de AgendaService se lee la regla de negocio y las tres excepciones documentadas; guarde una captura.
4. Cree en Test Packages la clase AgendaServiceTest con un metodo de preparacion que registre M-001 Kira activa, M-002 Michi activa y M-009 Rocky inactiva, y escriba cuatro casos: mascota activa agenda, mascota inactiva lanza IllegalStateException, ID inexistente lanza NoSuchElementException y horario ocupado no duplica la cita.
5. Rompa a proposito la regla (comente la validacion de mascota inactiva), corra las pruebas y capture la barra roja; restaure la validacion, corra otra vez y capture la barra verde; escriba ademas dos pruebas manuales que NO se pueden automatizar y suba todo a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Mascota, Cita y AgendaService con Javadoc completo, la carpeta HTML generada y una clase de pruebas con cuatro casos, subidos a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 8/Quiz Clase 8 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Las clases del dominio de VetCare quedan documentadas con Javadoc y la regla 'mascota inactiva no agenda' queda respaldada por pruebas que se ejecutan solas.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 8/Solucion Taller Clase 8 - VetCare.docx` — no proyectar completa.
