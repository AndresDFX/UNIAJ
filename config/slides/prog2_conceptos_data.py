# -*- coding: utf-8 -*-
"""Que se proyecta en cada clase de Programacion II: los conceptos y el codigo, en orden.

Por que existe
--------------
El deck se armaba con `slides_de_vinetas(teoria)` mas el archivo Java entero partido por
metodo. Salian titulos que eran la primera frase cortada («La clase pasada nos dio un
ArrayList, que es una herramienta poderosa...»), laminas «main() (2/3)» y clases de 41 laminas
para dos horas. Aqui el docente decide, clase por clase:

``CONCEPTOS[n]`` -- lista de ``(indices, titulo, ideas)``:
  - ``indices``: parrafos de ``teoria`` (+ ``fundamento`` partido por parrafos, en ese orden)
    que forman el concepto. Si son varios, el primero da la idea y los otros se suman al
    desarrollo de las notas: asi la Clase 1 no repite «el constructor» dos veces.
  - ``titulo``: lo que es, sin «(1/4)».
  - ``ideas``: 3-4 ideas que se proyectan (<= 440 caracteres). El parrafo completo va a las
    notas del presentador, que es donde el docente lo lee mientras explica.

``CODIGO[n]`` -- lista de ``(k, titulo, selectores)``: lamina de codigo que va DETRAS del
concepto ``k`` (posicion en ``CONCEPTOS[n]``). Los selectores sacan unidades completas del
archivo de la clase, que compila entero (`javac`):
  - ``"Clase"``: la clase completa, con su Javadoc.
  - ``"Clase.metodo"``: el metodo o constructor completo, con su comentario.
  - ``"Clase#campos"``: los atributos de la clase; ``"Clase#campos:a,b"``, solo esos.
  - ``"...@desde|hasta"``: solo las lineas entre esos dos textos, incluidas.
  - ``"...~desde|hasta"``: esas lineas se resumen en ``// ...`` (repetible).
    Todo tramo se extiende hasta cerrar sus llaves: lo proyectado sigue balanceado.
  Una lamina de codigo no pasa de ~17 lineas: mas que eso no cabe legible.
  - ``"@extra"``: el bloque ``codigo_slide_lineas`` de la clase (solo donde compila como
    sentencias dentro del archivo: verificado con javac).
El archivo completo sigue en `Kit docente/Clase N/Codigo/`.

Todo lo de aqui se proyecta: nada de VetCare, Huellitas ni Proyecto Integrador.
"""

CONCEPTOS = {
    1: [
        ([6, 0], "Del programa estructurado al objeto", [
            "Con arreglos paralelos (nombres[], especies[], edades[]) la mascota 5 es la casilla 5 de los tres a la vez.",
            "Ordenar, agregar un dato o perder la sincronía rompe el programa en sitios inesperados.",
            "La POO junta en un tipo, Mascota, el estado (sus datos) y el comportamiento (sus operaciones).",
        ]),
        ([9, 1], "Clase y objeto: el molde y la pieza", [
            "La clase es el molde: Mascota declara que toda mascota tiene nombre, especie y edad.",
            "El objeto es la pieza: Luna, Canino, 3 años. Fabricarla se llama instanciar y se hace con new.",
            "De una clase salen tantos objetos como haga falta, cada uno con sus propios valores.",
            "static marca lo que es de la clase y no de cada objeto: Mascota.totalMascotas existe una vez.",
        ]),
        ([7], "El objeto en memoria: pila y montón", [
            "La variable local vive en la pila; el objeto creado con new vive en el montón.",
            "La variable no guarda el objeto: guarda una referencia, como un control remoto guarda el televisor.",
            "Mascota b = a; b.setEdad(4); → a.getEdad() también da 4: hay una mascota con dos nombres.",
            "Los 8 primitivos (int, double, boolean…) sí se copian: int y = x; y = 5; deja x intacto.",
        ]),
        ([8], "== compara referencias; equals, contenido", [
            "== pregunta si dos variables apuntan al mismo objeto, no si los objetos se parecen.",
            "El equals heredado de Object hace lo mismo que ==: hay que sobrescribirlo, por ejemplo por id.",
            "Quien sobrescribe equals sobrescribe también hashCode: HashMap y HashSet usan los dos.",
            "Regla del curso: con objetos, equals; == solo para primitivos y para comparar con null.",
        ]),
        ([2], "Abstracción y encapsulamiento", [
            "Abstracción: quedarse con lo que importa del problema; modelar es decidir qué se ignora.",
            "Encapsulamiento: los datos no se tocan desde afuera; el atributo va private.",
            "Se accede por métodos, y así el objeto puede validar: rechazar una edad negativa.",
        ]),
        ([10], "Encapsular es proteger una regla", [
            "Con public boolean activa, cualquier archivo puede hacer luna.activa = false sin dejar rastro.",
            "Con private y un único inactivar(motivo), hay un solo lugar donde la regla puede romperse.",
            "Generar getters y setters para todo no es encapsular: se exponen operaciones del dominio.",
        ]),
        ([3], "Herencia y polimorfismo", [
            "Herencia: Perro extends Mascota hereda nombre y edad y agrega lo suyo.",
            "Solo aplica si hay relación «es un»; si es «tiene un», es composición.",
            "Polimorfismo: el mismo mensaje, hacerSonido(), da Guau o Miau según el objeto real.",
        ]),
        ([11, 4], "El constructor: el objeto nace válido", [
            "Se llama igual que la clase, no declara retorno y se ejecuta una sola vez, al crear.",
            "new reserva memoria en el montón y llama al constructor.",
            "Si usted escribe un constructor con parámetros, el vacío por defecto desaparece.",
            "El constructor valida: si el nombre llega vacío, lanza; no existe una Mascota sin nombre.",
        ]),
        ([12], "null y NullPointerException", [
            "null es una referencia que no apunta a ningún objeto: un control remoto sin televisor.",
            "NullPointerException ocurre al usar esa referencia: llamar un método o leer un campo.",
            "Casos típicos: una búsqueda que devuelve null, un atributo nunca asignado, una lista sin new.",
            "Defensas: validar en el constructor, devolver listas vacías y leer el mensaje del error.",
        ]),
        ([13], "El entorno: JDK, javac y java", [
            "JDK de soporte extendido (17 o 21), verificado con java -version.",
            "Una clase pública por archivo, con el mismo nombre: Mascota vive en Mascota.java.",
            "javac compila a .class (bytecode) y java lo ejecuta; el IDE hace ambas cosas por dentro.",
        ]),
    ],
    2: [
        ([0], "El arreglo tiene tamaño fijo", [
            "new Mascota[50] reserva exactamente 50 casillas contiguas, para siempre.",
            "No tiene método para crecer: length es de solo lectura; crecer es crear otro y copiar.",
            "Sirve cuando el tamaño se conoce (7 días, 12 meses), no para pacientes que llegan cada día.",
        ]),
        ([1], "ArrayList por dentro: un arreglo que crece", [
            "Guarda un arreglo interno y dos números: capacidad (casillas) y tamaño (elementos).",
            "Cuando se llena, crea otro ~1,5 veces más grande y copia todo, sin que usted se entere.",
            "get(i) es inmediato y agregar al final es barato; add(0, x) o remove(0) corren a todos.",
        ]),
        ([2], "La interfaz List: add, get, size, remove", [
            "List<Mascota> mascotas = new ArrayList<>(); a la izquierda el contrato, a la derecha la clase.",
            "add, get, size, remove, set, isEmpty, contains, indexOf: la API de toda la clase.",
            "<Mascota> es el genérico: si entra un String, el error aparece al compilar.",
            "contains e indexOf usan equals: sin sobrescribirlo, se busca por id recorriendo.",
        ]),
        ([3], "Recorrer: índice, for-each e Iterator", [
            "for con índice cuando se necesita la posición: el listado numerado.",
            "for-each cuando solo se lee: más limpio, debe volverse reflejo.",
            "Borrar dentro de un for-each lanza ConcurrentModificationException.",
            "Para borrar mientras se recorre: Iterator con it.remove(), o removeIf.",
        ]),
        ([4], "La lista encapsulada en su clase", [
            "La lista vive private dentro de RegistroMascotas, no suelta en el main.",
            "Afuera solo hay métodos con reglas: agregar rechaza ids repetidos, buscarPorId devuelve null.",
            "Se programa contra la interfaz (List), no contra la implementación (ArrayList).",
            "toString() en Mascota evita imprimir clinica.Mascota@6d06d69c.",
        ]),
    ],
    3: [
        ([0], "Cuando la lista permite demasiado", [
            "ArrayList deja agregar, insertar, sacar y reordenar en cualquier posición.",
            "La sala de espera tiene una regla: el que llega primero pasa primero.",
            "Con un ArrayList, add(0, otro) cuela a alguien y compila sin queja.",
            "Elegir la estructura más limitada que resuelve el problema blinda la regla del negocio.",
        ]),
        ([1], "La cola: FIFO con Queue", [
            "First In, First Out: el primero que entra es el primero que sale, como la fila del banco.",
            "Queue es una interfaz: Queue<Turno> sala = new LinkedList<>(); new Queue<>() no compila.",
            "offer agrega al final, peek mira el primero sin sacarlo, poll lo saca.",
            "Con cola vacía, poll y peek devuelven null en vez de lanzar excepción.",
        ]),
        ([2], "La pila: LIFO con Deque", [
            "Last In, First Out: siempre se toma el de encima, como la pila de historias clínicas.",
            "push pone encima, pop saca el de encima, peek lo mira sin sacarlo.",
            "La clase Stack es de 1995 (hereda de Vector); hoy se usa Deque con ArrayDeque.",
            "Es el Ctrl+Z de cualquier programa: pop deshace la última atención registrada.",
        ]),
        ([3], "Por qué son rápidas: ArrayDeque y LinkedList", [
            "ArrayDeque es un arreglo circular con dos punteros: sacar del frente solo corre el puntero.",
            "LinkedList es una cadena de nodos: sacar el primero es mover la cabeza.",
            "Un ArrayList como cola obliga a remove(0), que desplaza a todos los demás.",
        ]),
        ([4], "Una cola no se recorre para buscar", [
            "Buscar a alguien dentro de la cola para sacarlo indica que no es una cola pura.",
            "La urgencia se modela con Deque: addLast para el que llega, addFirst para el caso crítico.",
            "Imprimir la cola con for-each la muestra pero no la consume: size() sigue igual.",
            "Consumir es poll; mirar es peek o for-each.",
        ]),
    ],
    4: [
        ([0], "Mapas y ventanas: un mismo objetivo", [
            "Primer bloque: mapas y conjuntos, con demo en consola.",
            "Segundo bloque: una ventana Swing construida a mano.",
            "Objetivo común: responder al instante «dame el expediente de la mascota M-004».",
        ]),
        ([1], "De la búsqueda lineal al HashMap", [
            "En un ArrayList buscar por id es recorrer: en el peor caso, los 5.000 elementos.",
            "HashMap guarda parejas clave-valor y calcula la casilla con hashCode() de la clave.",
            "Si dos claves caen en la misma casilla (colisión), equals() las distingue.",
            "get(\"M-004\") tarda lo mismo con 10 que con 100.000 elementos.",
        ]),
        ([2], "La API de Map y sus trampas", [
            "put(clave, valor) reemplaza en silencio si la clave ya existía: no hay claves repetidas.",
            "get devuelve null si la clave no existe; getOrDefault da un valor por defecto.",
            "Se recorre con entrySet() (getKey, getValue), o con keySet() y values().",
            "Con una clave de clase propia hay que sobrescribir equals y hashCode juntos.",
        ]),
        ([3], "HashSet: el conjunto sin duplicados", [
            "Por dentro es un HashMap donde solo importan las claves.",
            "Responde en tiempo constante «¿esto ya está?»; add devuelve false si ya estaba.",
            "No garantiza orden: LinkedHashSet conserva la inserción y TreeSet ordena.",
        ]),
        ([4], "Swing: ventana, paneles y componentes", [
            "Anidamiento: JFrame contiene JPanel, y el panel contiene JLabel, JTextField y JButton.",
            "El layout acomoda: BorderLayout (NORTH, CENTER…) en el JFrame, FlowLayout en el JPanel.",
            "Tres líneas obligatorias: setDefaultCloseOperation, setSize o pack, setVisible(true).",
            "La ventana se crea en SwingUtilities.invokeLater: Swing vive en el hilo EDT.",
        ]),
    ],
    6: [
        ([0], "Del programa en línea recta al evento", [
            "Antes: main llama un método, ese llama a otro y el programa termina.",
            "Con setVisible(true) arranca el EDT, un hilo que espera acciones del usuario.",
            "Cada acción es un evento en cola; Swing avisa al objeto que se registró para ese botón.",
            "Su código no se llama desde main: queda registrado y lo dispara el usuario.",
        ]),
        ([1], "ActionListener: el contrato del clic", [
            "Interfaz de java.awt.event con un solo método: actionPerformed(ActionEvent e).",
            "btn.addActionListener(escucha) registra; al oprimir, Swing invoca actionPerformed.",
            "Tres formas: clase que implementa la interfaz, clase anónima o lambda e -> registrar().",
            "La lambda solo sirve con interfaces de un único método abstracto, como esta.",
        ]),
        ([2], "Separar la lógica de la interfaz", [
            "Modelo (Mascota): datos y comportamiento propio.",
            "Servicio (ControladorRegistro, RepositorioMascotas): validaciones, búsqueda y la lista.",
            "Vista (VentanaRegistroMascota): pinta campos, lee texto y muestra mensajes.",
            "Prueba ácida: si mañana es consola o JavaFX, solo se reescribe la ventana.",
        ]),
        ([3], "Un clic en cámara lenta", [
            "Primero, la vista lee texto crudo con getText(): todo es String, incluida la edad.",
            "Después, el controlador recorta, rechaza vacíos y convierte la edad con parseInt dentro de try.",
            "Si algo falla, lanza una excepción con un mensaje para humanos; si no, registra.",
            "Al final, la vista muestra el error en un JOptionPane, o limpia y refresca el listado.",
        ]),
        ([4], "getSource y otros escuchadores", [
            "e.getSource() dice qué componente disparó el evento: un listener para varios botones.",
            "Si se llena de ifs, es más limpio un listener por botón.",
            "ItemListener (combo), ListSelectionListener (fila de tabla), WindowListener (cerrar).",
            "actionPerformed corre en el EDT: una tarea larga congela la ventana.",
        ]),
    ],
    7: [
        ([0], "Qué es un patrón de diseño", [
            "Una solución probada, con nombre propio, a un problema de diseño que se repite.",
            "No es una librería que se importa: el nombre comunica el problema y la forma de resolverlo.",
            "Catálogo GoF: creacionales, estructurales y de comportamiento.",
            "Hoy dos, Singleton y Factory, usados con criterio y no por coleccionarlos.",
        ]),
        ([1], "El problema: un solo archivador", [
            "Si cada ventana hace new RepositorioMascotas(), hay dos listas distintas en memoria.",
            "La ventana de citas no ve las mascotas que registró la ventana de registro.",
            "Se necesita una y solo una instancia, alcanzable desde cualquier parte del programa.",
        ]),
        ([2], "Singleton: tres piezas obligatorias", [
            "Un atributo private static del mismo tipo: private static RepositorioClinica instancia.",
            "El constructor private: nadie más puede hacer new.",
            "Un getInstancia() public static que la crea la primera vez y siempre devuelve la misma.",
            "synchronized evita dos instancias si dos hilos entran a la vez.",
        ]),
        ([3], "Factory: quién decide qué objeto crear", [
            "Vacunación, Control y Urgencia: tres consultas con duración y tarifa propias.",
            "Si cada ventana hace el new de cada subclase, las reglas quedan regadas por la interfaz.",
            "FabricaConsultas.crear(\"URGENCIA\", \"M-001\") concentra la decisión y devuelve el tipo base.",
            "Un tipo que no existe lanza IllegalArgumentException: el dato basura no llega a objeto.",
        ]),
        ([4], "Cuándo NO usarlos", [
            "El Singleton es una variable global: esconde dependencias y complica las pruebas.",
            "La alternativa profesional es inyectar por constructor, como en el controlador de la Clase 6.",
            "Una fábrica que solo hace un new, sin reglas, es ruido.",
            "Primero el problema, después el patrón; nunca al revés.",
        ]),
    ],
    8: [
        ([0], "Documentar no es comentar cada línea", [
            "// suma uno al contador repite el código y envejece mal: termina mintiendo.",
            "Javadoc documenta el contrato: qué hace, qué recibe, qué devuelve y cuándo falla.",
            "Quien use agendar() debe saber que lanza excepción sin leer sus veinte líneas.",
        ]),
        ([1], "Anatomía de un bloque Javadoc", [
            "/** ... */ justo encima de la clase, el constructor, el atributo o el método.",
            "La primera frase es un resumen corto que termina en punto.",
            "Etiquetas: @param, @return, @throws; en la clase, @author y @version.",
            "javadoc -d docs genera un sitio HTML; VS Code lo muestra al pasar el cursor.",
        ]),
        ([2], "Nombres que se explican solos", [
            "verificar(String x) contra estaActiva(String idMascota): la segunda no necesita comentario.",
            "PascalCase para clases, camelCase para métodos y variables, MAYÚSCULAS para constantes.",
            "Los boolean se nombran como pregunta (estaActiva); las acciones, con verbo (agendar).",
            "Nada de proc1, dato2, aux ni flag.",
        ]),
        ([3], "Un caso de prueba: preparar, ejecutar, verificar", [
            "Cuatro partes: un nombre que se lee como frase, estado de partida, acción y resultado esperado.",
            "AAA: Arrange (preparar), Act (ejecutar), Assert (comprobar).",
            "Casos positivos, negativos y de borde para cada funcionalidad.",
            "El resultado esperado se escribe ANTES de ejecutar.",
        ]),
        ([4], "JUnit: pruebas que corren solas", [
            "En VS Code: vista Testing, «Enable Java Tests», JUnit 5; las pruebas viven en test/.",
            "Un caso = un método @Test; @BeforeEach arma el estado limpio antes de cada uno.",
            "assertEquals, assertTrue y assertThrows(IllegalStateException.class, () -> ...).",
            "La prueba unitaria es automática y repetible; la manual revisa lo que no se automatiza.",
        ]),
    ],
    9: [
        ([0], "Refactorizar: misma conducta, mejor forma", [
            "Cambiar la forma interna del código sin cambiar su comportamiento externo.",
            "Ejemplo: un manejador de 90 líneas se parte en validar, generarId, aLineaCsv y escribirArchivo.",
            "No es agregar funciones, corregir lógica ni reescribir desde cero.",
            "Prueba: el mismo flujo con los mismos datos da las mismas salidas.",
        ]),
        ([1], "Code smells: los olores del código", [
            "Método largo, duplicación y nombres opacos (a1, x, proceso()).",
            "Números mágicos: if (edad > 25) en vez de la constante EDAD_MAXIMA.",
            "El catch vacío y la clase Dios que es ventana, lista y archivo a la vez.",
            "VS Code los ataca seguro: Rename Symbol (F2), Extract Method y Move.",
        ]),
        ([2], "Persistencia: datos que sobreviven", [
            "La lista vive en RAM: al cerrar la ventana, las mascotas se evaporan.",
            "Persistir es convertir cada objeto en texto y escribirlo en un archivo.",
            "CSV: una línea por registro y un separador; aquí id;nombre;especie;edad;cedula_dueno.",
            "Punto y coma porque los nombres traen comas; y el CSV se puede abrir y leer.",
        ]),
        ([3], "Cerrar el recurso: try-with-resources", [
            "BufferedWriter acumula en memoria y vuelca al disco al llenarse o al cerrarse.",
            "Si no se cierra, el archivo queda en cero bytes aunque el programa diga «guardado».",
            "try (BufferedWriter s = Files.newBufferedWriter(ruta, UTF_8)) { } cierra siempre.",
            "IOException es checked: el compilador obliga a atenderla.",
        ]),
        ([4], "Cargar al arrancar, guardar al cerrar", [
            "El main construye el repositorio, llama cargar() y solo después muestra la ventana.",
            "Carga defensiva: sin archivo, lista vacía; una línea dañada se avisa y se salta.",
            "Una edad «dos» lanza NumberFormatException: se captura y se sigue con el resto.",
            "Imprimir ruta.toAbsolutePath() una vez dice dónde quedó el archivo.",
        ]),
    ],
    11: [
        ([0], "Qué es una revisión de código", [
            "Lectura sistemática del código de otra persona para encontrar problemas antes que el usuario.",
            "En la industria nadie integra su trabajo sin una aprobación escrita.",
            "No es un examen ni un trámite: es un control de calidad barato.",
            "Quien revisa también aprende otra forma de resolver.",
        ]),
        ([1], "Revisar por capas", [
            "Primera capa: ¿abre y hace lo que dice? Se ejecuta antes de opinar.",
            "Segunda: corrección y casos borde: edad con letras, campos vacíos, id repetido o inexistente.",
            "Luego diseño, manejo de errores y legibilidad, en ese orden.",
            "Al final el formato: la capa que menos vale y la que todos comentan primero.",
        ]),
        ([2], "Retroalimentación: evidencia, impacto, sugerencia", [
            "Se habla del código, nunca de la persona.",
            "Evidencia localizable (archivo y línea), impacto (qué se rompe) y una salida concreta.",
            "Ante la duda se pregunta: «¿qué pasa si la edad llega vacía?».",
            "Cada hallazgo se etiqueta: bloqueante, mayor o menor.",
        ]),
        ([3], "El checklist de revisión", [
            "Ítems binarios y verificables, sacados de los requisitos.",
            "¿Clases con atributos privados? ¿Una colección? ¿try-catch en las fronteras? ¿Catch vacíos?",
            "Cumple, no cumple o no aplica; el «no cumple» exige evidencia archivo:línea.",
            "El checklist no reemplaza el criterio: lo ordena.",
        ]),
        ([4], "Recibir la crítica", [
            "Escuchar completo y pedir aclaración antes de defenderse.",
            "Tres respuestas escritas: acepto y corrijo, justifico, o difiero.",
            "El revisor verifica antes de acusar: un hallazgo falso quema el informe.",
            "Antipatrones: la revisión de sello, la de gusto personal y la que rediseña todo.",
        ]),
    ],
    12: [
        ([0], "Integrar: piezas que funcionan juntas", [
            "Cuatro piezas: modelo, datos (repositorio CSV), lógica (servicio) e interfaz (Swing).",
            "Regla de dependencia: UI → servicio → repositorio → modelo; nadie mira hacia arriba.",
            "El servicio no llama a JOptionPane: así se prueba sin abrir la ventana.",
            "Un punto de entrada, un servicio y un archivo de datos.",
        ]),
        ([1], "El guion de humo", [
            "Cinco pasos: abrir con datos, registrar, buscar por id, cerrar guardando, reabrir.",
            "Arranque en orden: repositorio, servicio, cargar datos y solo entonces la ventana.",
            "Al cerrar se guarda, y solo si salió bien se libera la aplicación.",
            "Ventana antes de cargar = tabla vacía aunque el archivo tenga cien mascotas.",
        ]),
        ([2], "Errores de integración y su síntoma", [
            "Dos instancias del servicio: se registra en una y se guarda la otra.",
            "Arranque invertido: tabla vacía y consola diciendo «Mascotas cargadas: 12».",
            "Ruta del archivo distinta, o un CSV que se escribe y se lee en otro orden.",
            "NullPointerException porque buscarPorId devolvió null y nadie lo validó.",
        ]),
        ([3], "El depurador de VS Code", [
            "Breakpoint con clic en el margen o F9; F5 inicia la depuración y se detiene ahí.",
            "F10 pasa a la línea siguiente, F11 entra al método, Mayús+F11 sale de él.",
            "Variables, Watch y Call Stack muestran el estado real y quién llamó a quién.",
            "Un breakpoint condicional (id.equals(\"M009\")) se detiene solo en el caso problemático.",
        ]),
        ([4], "Integrar por goteo", [
            "De un solo golpe: todo junto la víspera y nadie sabe qué módulo lo rompió.",
            "Por goteo: un módulo a la vez, guion de humo después de cada unión.",
            "Contrato escrito: firmas públicas del servicio y orden de campos del CSV.",
            "try-catch en las fronteras y una bitácora con síntoma, causa y corrección.",
        ]),
    ],
    13: [
        ([0], "Qué es una excepción", [
            "Un objeto que Java crea cuando una instrucción no puede cumplir lo que promete.",
            "Tiene tipo, mensaje y rastro de llamadas (stack trace).",
            "Throwable se divide en Error (la máquina virtual) y Exception (el programa y su entorno).",
            "parseInt(\"tres\") lanza NumberFormatException; si nadie la recibe, el hilo muere.",
        ]),
        ([1], "Checked y unchecked", [
            "Checked: fallas previsibles de afuera (archivo borrado, disco lleno); el compilador las exige.",
            "Se capturan con try-catch o se declaran con throws, o el proyecto no compila.",
            "Unchecked (RuntimeException): datos sin validar o errores de programación.",
            "Leer el CSV lanza IOException (checked); convertir la edad, NumberFormatException.",
        ]),
        ([2], "Anatomía de try-catch-finally", [
            "try: solo lo que puede fallar. catch: del tipo más específico al más general.",
            "FileNotFoundException va antes que IOException porque es su hija.",
            "finally se ejecuta siempre, incluso si el try hizo return.",
            "try-with-resources cierra solo cualquier AutoCloseable, como BufferedReader.",
        ]),
        ([3], "throw, throws y la excepción propia", [
            "throw lanza un objeto en ese instante: throw new DatoInvalidoException(\"...\").",
            "throws avisa en la firma que quien llame debe hacerse cargo.",
            "El dominio valida y lanza; la interfaz captura y lo muestra en un JOptionPane.",
            "Una excepción propia que extiende Exception es checked y habla el idioma del negocio.",
        ]),
        ([4], "El catch vacío", [
            "catch (Exception e) { } silencia la falla pero no la arregla.",
            "El error reaparece más adelante como un NullPointerException sin relación aparente.",
            "Manejar es informar, registrar, usar un valor documentado o relanzar con contexto.",
            "La mejor excepción es la que no ocurre: validar null, vacío y rango antes de convertir.",
        ]),
    ],
    14: [
        ([0], "Sustentar es demostrar", [
            "Ante un jurado que duda, se demuestra que un problema real quedó resuelto por un programa que corre.",
            "Al menos la mitad del tiempo, la aplicación corriendo en pantalla.",
            "Orden: problema, solución, arquitectura en 30 segundos, demo en vivo, aprendizajes.",
        ]),
        ([1], "La sustentación es una coreografía", [
            "La exposición se trocea en bloques completos, con evidencia en pantalla.",
            "Las transiciones se dicen: «para mostrar cómo quedan guardados, abro de nuevo la app».",
            "Un guion con minutos y evidencia por bloque: cinco bloques, siete minutos, cuatro de demo.",
            "En equipo, cada integrante toma bloques completos y nadie se queda callado.",
        ]),
        ([2], "La demo blindada: el pre-vuelo", [
            "Datos sembrados y creíbles: tres dueños, cuatro mascotas, tres citas.",
            "El camino feliz ensayado, sin búsquedas improvisadas.",
            "Pantalla limpia: fuente grande, sin notificaciones, el proyecto ya compilado.",
            "Plan B: un video corto de la ruta feliz y capturas listas.",
        ]),
        ([3], "Las preguntas del jurado", [
            "¿Dónde está la herencia? ¿Por qué ArrayList? ¿Qué pasa si borro el CSV?",
            "Se responde con la aplicación o el código en pantalla, en 30 a 40 segundos.",
            "Si no sabe, dígalo y proponga cómo lo averiguaría.",
            "Tenga abiertas las pestañas de cada respuesta.",
        ]),
        ([4], "Tiempo y nervios: el ensayo cronometrado", [
            "El ensayo con reloj revela lo que el papel no: la intro larga, la demo que se atasca.",
            "Se anota el tiempo real de cada bloque frente al planeado, hasta caer entre 5 y 8 minutos.",
            "Restan: leer de espaldas, pedir disculpas, culpar al computador, pasarse del tiempo.",
            "Suman: mirar al jurado, el vocabulario del dominio y admitir las limitaciones.",
        ]),
    ],
}

CODIGO = {
    1: [
        (1, "Crear objetos con new", ["Mascota.main"]),
        (5, "setEdad(): el objeto se defiende", ["Mascota.setEdad"]),
        (7, "Atributos privados y constructor", ["Mascota#campos", "Mascota.Mascota"]),
    ],
    2: [
        (0, "Del arreglo fijo a la lista que crece", ["@extra"]),
        (2, "agregar(): validar antes de add", ["RegistroMascotas#campos", "RegistroMascotas.agregar"]),
        (2, "buscarPorId(): recorrer y comparar por id", ["RegistroMascotas.buscarPorId"]),
        (2, "eliminarPorId(): remove(Object)", ["RegistroMascotas.eliminarPorId"]),
        (3, "listar(): el for con índice", ["RegistroMascotas.listar", "RegistroMascotas.cantidad"]),
        (3, "pasarAGeriatria(): borrar con Iterator", ["RegistroMascotas.pasarAGeriatria"]),
        (4, "Mascota: atributos privados y toString()", ["Mascota#campos", "Mascota.toString"]),
    ],
    3: [
        (1, "Turno: lo que guarda la cola", ["Turno#campos", "Turno.toString"]),
        (1, "SalaDeEspera: offer y peek", ["SalaDeEspera#campos", "SalaDeEspera.registrarLlegada~System.out.println(\"Llega|turno numero",
                                         "SalaDeEspera.siguienteEnPantalla"]),
        (1, "atender(): poll sin sorpresas", ["SalaDeEspera.atender", "SalaDeEspera.estaVacia"]),
        (2, "HistorialReciente: push, peek y pop", ["HistorialReciente#campos",
                                                   "HistorialReciente.registrar",
                                                   "HistorialReciente.ultimaAtencion",
                                                   "HistorialReciente.deshacer"]),
        (2, "La cola y la pila trabajando juntas",
         ["ClinicaSalaDeEspera.main@=== 2. El consultorio|historial.cantidad());"]),
        (4, "La urgencia entra con addFirst",
         ["ClinicaSalaDeEspera.main@Deque<Turno> filaConUrgencias|pollFirst"]),
    ],
    4: [
        (1, "Expediente: el valor que guarda el mapa", ["Expediente#campos", "Expediente.toString"]),
        (1, "La misma ficha en una lista y en un mapa",
         ["ClinicaBuscarExpediente.compararBusquedas@List<Expediente> archivoHistorico|String buscado"]),
        (1, "Medir: recorrer contra get(clave)",
         ["ClinicaBuscarExpediente.compararBusquedas@long t1 =|nsMapa + \" ns\");"]),
        (2, "guardar(): put avisa antes de reemplazar", ["ClinicaBuscarExpediente.guardar"]),
        (3, "Un mapa y un conjunto como atributos", ["ClinicaBuscarExpediente#campos:expedientes,razas",
                                                   "ClinicaBuscarExpediente.cargarDatosDePrueba"]),
        (4, "Paneles y layouts, escritos a mano",
         ["ClinicaBuscarExpediente.construirInterfaz@JPanel panelSuperior|add(pie, BorderLayout.SOUTH);"]),
        (4, "El evento, el cierre y el arranque en el EDT",
         ["ClinicaBuscarExpediente.construirInterfaz@btnBuscar.addActionListener|setLocationRelativeTo",
          "ClinicaBuscarExpediente.main"]),
        (4, "buscar(): get y el caso null",
         ["ClinicaBuscarExpediente.buscar@Expediente e = expedientes.get(id)|</html>\");"]),
    ],
    6: [
        (0, "main(): la ventana arranca en el EDT", ["ClinicaEventosDemo.main"]),
        (1, "El formulario: GridLayout de 5 × 2",
         ["VentanaRegistroMascota.VentanaRegistroMascota@JPanel formulario|add(new JScrollPane"]),
        (1, "addActionListener: el botón guarda a quien lo escucha",
         ["VentanaRegistroMascota.VentanaRegistroMascota@btnRegistrar.addActionListener|});"]),
        (2, "El repositorio no sabe de ventanas", ["RepositorioMascotas.registrar",
                                                  "RepositorioMascotas.listar",
                                                  "RepositorioMascotas.total"]),
        (3, "registrar(): la vista lee, delega y muestra", ["VentanaRegistroMascota.registrar"]),
        (3, "registrarMascota(): el controlador valida y convierte",
         ["ControladorRegistro.registrarMascota@if (id == null|edad > 40) {"]),
    ],
    7: [
        (2, "RepositorioClinica: el Singleton", ["RepositorioClinica#campos",
                                                "RepositorioClinica.RepositorioClinica",
                                                "RepositorioClinica.getInstancia"]),
        (2, "Comprobar que es la misma instancia",
         ["ClinicaPatronesDemo.main@RepositorioClinica a =|listar());"]),
        (2, "Cada ventana pide getInstancia()", ["VentanaSucursal.registrar"]),
        (3, "Consulta: el tipo base", ["Consulta~protected Consulta(String idMascota)|}"]),
        (3, "ConsultaUrgencia: una subclase", ["ConsultaUrgencia"]),
        (3, "FabricaConsultas.crear()", ["FabricaConsultas.crear"]),
        (3, "La fábrica en uso", ["ClinicaPatronesDemo.main@Consulta vacuna|La fabrica protege"]),
    ],
    8: [
        (1, "Javadoc de un constructor", ["Mascota.Mascota"]),
        (1, "El contrato de agendar(), en Javadoc",
         ["AgendaService.agendar~if (fechaHora == null|return cita;"]),
        (1, "agendar(): cada @throws en el código",
         ["AgendaService.agendar@if (fechaHora == null|no puede agendar citas.\");"]),
        (3, "nuevaAgenda(): el mismo estado de partida", ["ClinicaQADemo.nuevaAgenda"]),
        (3, "Caso positivo y caso negativo",
         ["ClinicaQADemo.main@AgendaService agenda = nuevaAgenda()|agenda.totalCitas() == 0);"]),
    ],
    9: [
        (2, "El contrato del CSV en código", ["RepositorioMascotasCSV#campos:SEPARADOR,ENCABEZADO,CAMPOS_ESPERADOS",
                                             "RepositorioMascotasCSV.aLinea"]),
        (3, "guardar(): escribir con try-with-resources", ["RepositorioMascotasCSV.guardar"]),
        (4, "cargar(): sin archivo no revienta",
         ["RepositorioMascotasCSV.cargar~lector.readLine(); //|mascotas.add(m);"]),
        (4, "desdeLinea(): una línea mala no tumba la app", ["RepositorioMascotasCSV.desdeLinea"]),
        (4, "main(): cargar, guardar y reabrir",
         ["ClinicaPersistencia.main@RepositorioMascotasCSV repositorio|mascotas.size());~=== Clinica: arranque|rutaAbsoluta());",
          "ClinicaPersistencia.main@repositorio.guardar(mascotas);|verificacion.size());"]),
    ],
    11: [
        (0, "El código a revisar: main()",
         ["ClinicaParaRevisar.main@int consecutivo = 1|datos.size());",
          "ClinicaParaRevisar.main@String[] fantasma|fantasma[1]);"]),
        (1, "proceso(): ¿qué capas fallan?", ["ClinicaParaRevisar.proceso"]),
        (2, "Dos búsquedas casi iguales", ["ClinicaParaRevisar.buscarPorId",
                                          "ClinicaParaRevisar.buscarDeNuevo"]),
        (3, "imprimirFicha(): el mismo bucle otra vez", ["ClinicaParaRevisar.imprimirFicha"]),
    ],
    12: [
        (0, "main(): una sola instancia de cada capa", ["ClinicaApp.main"]),
        (1, "El constructor registra el cierre", ["ClinicaApp.ClinicaApp"]),
        (1, "cerrarGuardando(): guardar antes de salir", ["ClinicaApp.cerrarGuardando"]),
        (2, "ServicioClinica: dueño de la lista", ["ServicioClinica#campos:repositorio,mascotas",
                                                  "ServicioClinica.cargarDesdeArchivo",
                                                  "ServicioClinica.guardarEnArchivo"]),
        (4, "registrar(): la regla vive en el servicio",
         ["ServicioClinica.registrar~if (nombre == null|La cedula del dueno es obligatoria."]),
        (4, "registrarMascota(): la frontera con la interfaz", ["ClinicaApp.registrarMascota"]),
    ],
    13: [
        (1, "Una excepción checked propia", ["DatoInvalidoException"]),
        (2, "registrar(): try, catch y finally", ["DemoExcepcionesClinica.registrar"]),
        (2, "finally corre aunque haya return", ["DemoExcepcionesClinica.buscarNombrePorId"]),
        (2, "cargar(): del catch específico al general",
         ["DemoExcepcionesClinica.cargar~String[] campos = linea.split|[OMITIDA] \" + e.getMessage"]),
        (3, "setEdad(): validar y lanzar", ["Mascota.setEdad"]),
        (4, "malaPractica(): así no", ["DemoExcepcionesClinica.malaPractica"]),
    ],
    14: [
        (1, "El guion de la sustentación en código", ["EnsayoSustentacionClinica#campos:GUION"]),
        (2, "sembrarDatosDemo(): datos creíbles",
         ["EnsayoSustentacionClinica.sembrarDatosDemo~/duenos.csv|});~/citas.csv|});"]),
        (2, "chequeoPreVuelo(): verde o no se presenta", ["EnsayoSustentacionClinica.chequeoPreVuelo"]),
        (4, "ensayo(): planeado contra real",
         ["EnsayoSustentacionClinica.ensayo@for (int i = 0; i < GUION.length|anterior = ahora;~System.out.println(\"\");|\" min\");"]),
    ],
}
